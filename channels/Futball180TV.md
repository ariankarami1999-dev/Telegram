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
<img src="https://cdn5.telesco.pe/file/rd1PQJJYcNCsoz5lOXocl4dAccTnGEqHfpNqOsrkGScXw75XQRQ-O5_BhcZue26wfzTRioG5A3Ry8bnMmsatOGJpACUe-35mBVK6w6Z8mlc6O5ImEGdWfa_YvJ7NdgPp63ekynj7uTDdF3zVFZV5rTQn6qInKlVvkUfOpF4lQhwqnBXfmocbqLijaWSU7KaUzXN3iQkNRLwhEOwf_rU5Jipz2NW56O0khWMmVEFE4Tu09Xx605zDTfgf30bUkB6MXMixt304RBnHaZA67jQz2cXLuGiLLUNb9Kj9MoHzSO2Phuy60Dwf-u7tvZiwxjHAbtgjOrLqjAEsYyD6ELiFig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 486K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 03:25:29</div>
<hr>

<div class="tg-post" id="msg-103043">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/Futball180TV/103043" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103042">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❗️
ریدم حاجی اینجارو داشته باشید
🔻
حسین کلهر مجری سابق صداوسیما مصاحبه کرده گفته که یه شب تو خونه حشری شده بعد زنگ زده وزارت اطلاعات که براش یه پرستو بفرستن تا چنتا اعتراف داشته باشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/103042" target="_blank">📅 01:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103041">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9yqnQbmCjLC8AfdXFuboSp-kEJwMVnCSz9IcDturHUERKcQIT03nw2HEkHvOgYXdYWmbcE0YL88jCgec2zutSwkyeRhFJrwsiCNcoYW1K4KT6HQAZf-DMuMzXg8Xsg8YOY4vJ8k4FmrB6pycqHkfm78oJDpeAkxlYhiK3H-p9GzSwC_VKHV4Gw-MOzEbGn1k7mSJXWO5VOYNKtMlzmSWctcSUKaw239aT6XdblPzMAuizdPGpSROBp_cPNjo2JBhFytwvfvTdkdxVkGExNAks9OWz4IW5hc1mceHy9GeviFVoSJW8YmtNhi1Han99Q8K8H5FENc8S6IuiTQrpVolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇪🇸
بنظر فصل‌آینده عقب زمین بارسا قراره حسابی تیمشونو شوهر بده؛ مگه اینکه دکو کنار این سه نفر یه مدافع باتجربه اضافه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/103041" target="_blank">📅 01:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geO7JYq7pbYufsHvHOLhXM4hdnQFdzyQUFJPF74hPjM-4fU6I_yrkvpvYVUNkDGTOkoYfUIfh_WZUn2R4mV06sSz1MLINYl48ecVJTkAjezi6MxoxR5VW1zcX-Ktzzxx88m6_eI4WLfZBbRYa_X-I3VcG03iBcbYYat83-8nmdKWR5L0J3K-tY3tvNz49ouviuA2T4q2uibSCTTRDMvW-V2XSeuGb2O2jEoQhgDov0k_Tz5wJrH6Jfwl_BjslgaoiljRWQ9IV80mCpzYyrg2lTuOTrtxTOMuIaO5gmg-OYl8Qk_aQCf9GOFSadeAxaQnrRxrbS1zIpia8h8OruZRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
لیورپول تمام حقوق آرائوخو رو پرداخت میکنه. همچنین بند خرید اختیاری داره و با پایان فصل‌آینده در صورت نیاز قابلیت فعال‌سازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103040" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103039" target="_blank">📅 01:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0fpaHTeIvoiAXfI9wBm7KoJrI5cf9kKCztjZrcFNEwggbL2cUbI8zJuFWTqtTYSxTTxTCrg-Oty8gSu1EB93up90zKoFQZ2D90z_R-O7nyqbKH0oIK55nSxOzjUr3v1Tr73Lu2X9hvDNv-ya9q4_OVOpkhmwLzR7N5iGesR9oyC4U6qWVTgCG4hmmzEHVvRAZP4bj7EFB60CmO8XsXFVaIr8B3mE_lEIyxct7tf9g1M-37DEGhA6Qd1jO01LKoSDn7upaeKgrNEKR8uU2g8pWz4iiT-Mno0u9OZD5MOoP-ofijHUX88bCznyuQyY4K3oHwbwqj9JHcTbVIwSvWB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
بگایی‌هایی که اسطوره آرائوخو در سالیان اخیر برای بارسلونا به همراه خودش داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103038" target="_blank">📅 01:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3Ii9bGbpMwrAM_-JoJj2GO6EedoZMdLJb60FSjuIEFZwxTwP-ubf8GtBPNd_y5OW94PidfJcJ_Rew0pxnCJjTOxHJ8-NFOTszVhCyScaIzr8Wgnl4hG-mEKrtl0S2ohW4NpVXY5xPP0S0sRX8nhPZiNNBeuRWtnOvtcd1IIWAJacfSV1Ya1oeBRjYMUzgcTnozaOQkprD8HyWYD9t6T-4eTR_2XwFCUSCzGHvMDTZImCrlc67jqavSqIp7VVyibqBcC00Eh8P-ZyGt-dmxmYrpAqyHMB0gwlZvbq_ZWxA3H7YDcEgpbi_TuhQJzkGFL2r3xugsfk0clSuPtZUlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/103037" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103036" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103036" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Iia147b9xFq1rVQrG6--X1ufiUg476tDXHaKQrhVZVVMLdenFQvCKd0lIBhBeM-mHeU2Xw5UrfYlMHsSEHutkFu9-CN-cV7LZd-NLQfFb3bS1J1LlX89wEnCubHSkZ7V_PwyA05Ordqz_QjziSLVtpkCupKtf0YAIkAj2_yFu3x-orYLAb7ph-NnXAo5C3DEkqv7AFPIF2Qd04OUIxRAhMWl56m2rQjaPpltlzpfE4QLlnedWlndqKT9j9M_Un5TYUlL4dmWazWYe262nLPDIHRsYLlmFxnUd2C7Lp-LAMA29wDbnpmNtc7yPQuUkcnYkaRtRpo5RCNiMTlhpMcj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Iia147b9xFq1rVQrG6--X1ufiUg476tDXHaKQrhVZVVMLdenFQvCKd0lIBhBeM-mHeU2Xw5UrfYlMHsSEHutkFu9-CN-cV7LZd-NLQfFb3bS1J1LlX89wEnCubHSkZ7V_PwyA05Ordqz_QjziSLVtpkCupKtf0YAIkAj2_yFu3x-orYLAb7ph-NnXAo5C3DEkqv7AFPIF2Qd04OUIxRAhMWl56m2rQjaPpltlzpfE4QLlnedWlndqKT9j9M_Un5TYUlL4dmWazWYe262nLPDIHRsYLlmFxnUd2C7Lp-LAMA29wDbnpmNtc7yPQuUkcnYkaRtRpo5RCNiMTlhpMcj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103035" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoeVft7QeZfJ966c2p0gHdk8nEHWBI4OkinOIEgxr9zZ-7Ah55EuqDYJkj-Gy53i8WbLyZ8gJNSCgmPw4SjMWSHu2gcC2nzZmqG5161qrybRagYWMYF_lcStpYvGq65aoxHucfj47B_C9a1-gORwf_OmRzPKf4fedFVDLubdrlMWIHAMzIujAuSW9JAovn7huOZATmoCSKaWj-y7qMxvHZciryhaqRTuUm4Pc4TzC8HXQCdozjItTTa7_pI9kIx65N_XRwaS7-lrpikvXXXbOFRSlqOcAro4XJDn3n7PVGjeIlnEOBkXzUIYDIoeD0NFqq9AQ6BmoevmVZS9EboL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
مهاجمای پریمیرلیگ خایه کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103034" target="_blank">📅 01:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G83-X4zbP6OqAjXx_ADnjZB23jKY0vPp2hAOHIaFtdjvQlNsULB_Y2BKx9h_w7JfSFxMgDz5OByYLGcYjqvjoW_HQ41D9WxQMpCT3tEvTlwx-N8AkOaglSdHdkOAUIxRe9CboLpVeVb0YaL0oVjM9A6o02fc9muS42Ic5hBHyXKTF2whGv8OX5APKJZtNeEww8PcCHYo6RKW6dhXoHdHRuJ7ttZBFJEOswcs7jimFBliI6LTgoIIzCOpp-oiDydg-3MIxu08cASlpEgJbKyfCawGAmgWf2Mbbw3o6x97ggpcxqeSpwQPMdgx3zOsykUE7y4kgvH4hKWHOT2q7WVMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤣
🤣
🤣
دکووووووو بیشرف داره چیکار میکنه تو نقل‌وانتقالات امسال با بارسااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103033" target="_blank">📅 01:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/103032" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejSsc8GdZB9p_JX2rQPFnSiJS4twBRexiryLK8D2G67NDXJ2gV03BbmwavGGINq_x7zf4HfgGk7q0BhX6dArPcs-IQgxn6wZuvn1mVdjacKHZXT-xQpOfzSXTLJfJ260pdIfmO0euRueRnexyVzHUOcrhjvs84mNfr4IJmPA6cOjjEJStJApVxkC44VpirZOl88gxgTWJiC49BkXO4pC3BKJdEykYL7Ety_qJ2AYfKueSLNgoB0OIPP4hLrdyi5U7cQGlBAtbHzHmRn4ORH27kE9qUhaBOgbDP2QUJ8K2cC-phO2esiGIVIfcMJwjF4giQFFSq6CHfgXU2iFzjErWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری
و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103031" target="_blank">📅 00:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103030" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k04J5wiQWbe-OdHLgrJREUuHijHqJw_KDIJBXUZl9mM_zBBlaO5wyYE7CeGiOxqa7MidRSKVH4bf11VRogG4RYAiWz9bLbMW6-S65ndPlYUDKDxWvkdr8uvTfOsvLjsYI69t58CVQm8rizCAJ8xc6Tmg4s3YLMYZax1UAvBMIq_YJf4mW7NrSxumxiRIvzHLpEn3MW68iNOePZcXY50sy-m-YcYev-lNvjvIlMsPTS-iHR6J9ojQHdsngdiGop12ChN4ND6REx8wqj7Zjc_bZt4EmC38yewEgadTpKqjTl6DY1G8lJ53wGbGeJeT0lHHZo5KTcQZ4rO5tViuExk0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشتون راموس عجب بدن حقی ساخته
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103029" target="_blank">📅 00:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZiXv2pwHbFl1tjm0IOOxLCPx4q0bNR5sKs59aoNpRXAZZR0FqKZMgDOcOvmm7xZSV49UJZYkf-oiYqvVF7fZF1mUbUWsGrNy0UXD__LebvvqA7A0xZaOZuczj_Xm4D-7EnDUVoAa5OBQCVSw0qUGiE5aJkoLUE3UPU2jM8I95ojN5ZEHyBZPhpfjUHLc1XQS70f1nWVzMGGXPMOlwRvdsdYh1ze3Lwk9LM45wRg5aFSn9C0F-Gbe_imRahJYJ6AvMctOa3kvniav7dEBVfeDFFC7AItXkgtee1zGKQCSUJPgkpkYYPlcrhIT-KxUy_XPF2M-8S_llvjK4GT2tQ_YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
آاس
: برخلاف شایعات، درحال حاضر شهر میامی آمریکا شانس‌اصلی میزبانی از سوپرجام اسپانیا در سال ۲۰۲۷ است. شانس استانبول و ریاض کم است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103028" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRdFqo9DrDFkuET0QawFzkBTxxe9FNrw_4s-YUfvnLn8WDqRKJ7KPlrfcWpCcq_x4Eqrd-d8ZzCYoPv8JFASOmbu6caMg4sb7xd1JlA3cb6SnGVg1iUl-KYbPJPvdAIjJlqUqsiravu7mIz-JVSZX4oT40rAc2Z7u11spygW3-37pdSISW38D-Jsx1uAhCAX6AqilZK2C6YHDufa0C7yd6PLZ2AOGaxK3Gds48osdUe5KoHKXZFMOIe4d0zbZyhGoPSGAubVlqx0LLxqryG0VC0HQTCo5Wmb9q41lUOuD4AxJHZDExKi1Xkzji6U2IXD36GpfpCYc-zZssPkVLsWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APuAL5r_a6kjv6jZbZ0lPJ4Z3stJZL6CaW8e8HwHWZOAmYcJdtpzK36IWmn0Gf1Y66hDe1vVY4sFBM4DbYnD6VvIfarF17Nw1LF-bGZcS5aKqgg3YALYs6tPYxytNbIYWIyt0GnRcEey6VMuxyAZZHTptjp2v8A4JD7lAyQiImobwxZ19ntnSrWEE6yDXKNa4fpy8DgmJB2EhImArE-bzQCPif4XEUxAlXVnAHWjhi4QNiXsQ_uLFeY3r5qs29S-P8M9xc5QtIN-vwS9xO4cWtiUAS3o9LfUc_IciYODdQCNzNbUaOtlEQuMzTNig63Utl9wEvSnZR1D4h6fHjJsVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔵
ادعا شده کول پالمر هنگام جلسه تاکتیکی مشغول تماشای ویدیوهای سوفی رین روی گوشیش بوده و ژابی آلونسو هم بعد از دیدن این موضوع، اونو از تمرین اخراج کرده و گفته فعلا برو چشمم بهت نیوفته تا ببینیم چی میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103026" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnlkZ10BJ9pH2fcv3xghaDQradFVWkAqDrkSy7cL4wh5YTvkrfwa7STTV7IMoI6T1qnWtIPwRrlOvVI76Dy0Cpm7c_f5EuGaRQE7Jh0ZCxEQmrLGRo3g5LFMfq2l0mr3c2hAQOUjRBRK95SCzAagoSwgRNRztnSWkjhJsNCRhj_ACrx3v_DT9nq5HWrnL8BzbV2ivtxMP2CG0zlranHk1kATUK-w91Mt2uO6o06ahLH8_BYo6WC8eC8FXfGJtB_iQl-Twu_9crA1Bqpzm0-pW8LzBdzZrGYOelOOrvSdY4LZOM_ZbTovw1-n5hyellu1Vr8c2_WOdsQABqp6Z5RWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl0gM2MA29GKWc8ODjpWS9RzZ4lRoBlMow6e56UIIJQTnNqUIm32_tZlnMfvmfIiTi-xsG0Iq2fYbJmI87Tl3_qEAjcndPToHjmanBPIjlx_JV14JC1WdY19k661beBmMvQDa0mR1uOaokOxipoJp85qKRPV-1-y7QwhQF1u5lum8Zmpy4Q6CcDKPf_Z_7YRndYW6BCNfThsWUZC7jxSuKkCKnc0OXOjSG_zKMOg8zIH9Ckfm1QnZ4X43szFpj5FCIYlhxsFkG1V30ut3fuG94Lpzd5ufaVX-0OfsWeD3LjpJFstdpe7flE8CEdkGXt_aVw2rVSf-GpaNAC_H1TTng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بازیکن مورد علاقه‌م تو رئال مادرید؟
🎙
یان دیومانده:
قطعا کریستیانو رونالدو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103024" target="_blank">📅 23:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaXMFGfXyZgZ_8fTFpwBKBBUhtUT52AWn3MAw6WYopxH84gpJZm3ikGA_EPmWOe8ISBwbUWJXAAUh7YLEme6KKuSlGautRXCGB8UFYU9XZuoT3hjKKnvSFVAcIVZrjR6bbbNu6hXt4ueTLl-7v9_GBRXwGG_33tNeOuh1n_f1PNadVlGneiQuscgyiAg7secLOeeX3Q7BRNypvseG8Fp8yfDdYtqEWxbJIDt9g0W04ghI2OeCZwnmuCo5sLDp0LL2la9S_U5TCs9RMv7VprlecE1NU45wpRqEe_60QU1zmiXDc4DORzbsNzoSEZDlY4IcnveHG1kswk28O3sBb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شات خوشگل از مسی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103023" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdg9_HXIf9pgkXSh0kABCrtzlzH3S3pVXUsw1cJmqrFe65w7lMoYpco_IQB_73wa-C1dRKh_bbrsFL_wPGlcdm-Oj6yorqTpa-NWqUxADNUELJALXOJhiKXy3mC5mqkB849X323Q1oQixeICLUzRwaRd2B_DUeA1Z0Q9LkE-HfWKK086gWixqdwjUoq6VUAm_jgQgdsSsL7bKppTzRhTENDosKuFdkP4dy2hb6z4y3V_IalZwEqDV0c9PEpMyhtwzCXSBB93jdYoQN6cjDv_8alXRGVI7MtIdw1R58_UC-0OnU-abukqv_JXpCwkucCHdIanpwemhpSqx4oRO6PQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جیدون سانچو تو انتقالی عجیب به الریان قطر پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103022" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چیچاریتو: من کریستیانو رونالدو رو آدم مغروری نمی‌بینم. اون فقط روحیه رقابت‌طلبی داره و همیشه تلاش می‌کنه بهترین باشه. وقتی هم به موفقیتی می‌رسه و ازش درباره اون موفقیت می‌پرسن، میگه: «آره، من به این موفقیت رسیدم.» اما جامعه تحمل اینکه یه نفر از خودش خوب بگه رو نداره و اینو غرور می‌دونه. ولی از نظر من، غرور وقتیه که چیزی رو بگی که حقیقت نداره؛ یعنی بگی بهترینم، در حالی که هنوز نتونستی ثابتش کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103021" target="_blank">📅 23:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRM7LSLrRvUMbL9el3mhrRXmLrE_bIp4QuGQ4j8La61HGs5QQjzYmTAA5GfvMRZxDLkE5z3KYlgByxhI1P-G_mcZ9BKPayyw4V6QAcvKHitDBKpMTLIhuT8KlQbo7edX6ko3Hc_ajjpu4r-DWEBVbfZdDYe91QBYvjWAFJtniBl4TxIYoWCbPn93DfmhYRt_bDjiXUEezQGUZAFYgPyY3j671FAOkPesoAc2NarHHmrQ41mVBWpK8Jhduergad2xVbcBHTlZ3qVg1zLjbTxkoYaa0_VUhqT3URNcdFHv_xIkEUbzf4VIwM5Vj97rxdE2o9McJfjbY171817g9y2gbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
بازگشت تیبو کورتوا به تمرینات رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103020" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
جلل‌الخالق؛ اختراع جالب دهه نودی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103019" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103018" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncp17sQ89n-bK_jqVTXn9gSlmGkrz3HmHfv2MfyAZn-xaVU6W3G1Oi0XjPUAlBr2B554RmXKd8sf4ymcNNdC_dImEyysoIB-V1ngpWnrsj7EA4nJcISXYSoGvCnkABRe7lRuB8PCQy6Ftb2xgeplt9-UaCCv2Xg5dYsFH02OoVy8pp2eneKrHxONpViHiE0f7SglDt15oq1TxvVWuOguiY67Qg72SDVfTjo5TM3rIBi6pUxU1GiA_63cudhctJ-6CK_xrFsnIzmnRpGKPsIeiInyp4OnTPbFVpJ6K_gWwFXiJEZpK4sm_1CA2EmyMC4ExNmQWSPpfw05D5FlEALJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103017" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EqRYZqqwzOoqPr5Ci6lW-otxcneqF7oU-u3jwh9sIJxO6y7IJvUmlUZiYCKCBBN_2sXtYFQTBUHhLP07nRDCxFpGnW2Ov9RO8BNTdPcFX2QlJQuAZLeX-__fRFyFFpbyjzePlMnuF3kscof4JJkBsKnIfZ9bnQj2hwByw4Z-A4HOHOsi-dYPkAWuVpXy6mXQBrk5MYpFvNpA3RaCgJxFIBSKYLv5AFH6kq6KlGoU8eW8yTOfYW29iz8zFfDe9-twZeRcypP-cvXTxL7z7V6Tg1zR4FyMB6Ne6lQakrwWe1GTEuzh415PNo_D4WSSmWETAkLY6dQZ1z-xGfYRP5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوپینگ با ما چه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103016" target="_blank">📅 22:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nndNR2eOhx610itFlYMZXkHreP46eHIGRSyx0U7pwQ6ZJH4l_uXxqXdO7yUC9xcs5-eIa_13UGZ60S9zGzYv8ksLfG_kL5kacfxgrk1Nb-5CS2CtKndO_84Y1a-y4SqctFav7Jy69-ukdz8ifBtd5IFvHUwmnb2L0vWOlJ0AoabY9PBkHGZrPeBDc3hzZ9CTjFusjKAodsUSHF3ddUsk3VZHGiWfrc80TBzMRDC6FGl4oiqqrm-GydWU4veGawWmXxTQHe-kxawKkeo5KK15DRNvYuTC0-7QcK_z0du6_dh1hF5CtHZLxXH4v4aTKap_pFNTaVeX9Mk8wl64pn8b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utMP8LXUuHuKi1T5Tp58JOMet8Bz8nLHRI-hsW5pHbY8M0WxBe3BQJXV1eDkiS-r3pyww2E9_NSgK2hfqQx3dBl3QwTgdgxtdqBJh6gOItQqWQ6wDzwpPCo-MP7B4yyzaPtXo6O1zADuP1HGbeJa_E9rH0sZzYDNNBRJwoybBSfQ5kCA_c3Ld5YkdQIqc6_qYH1ST1oyoNIOr0KN3XtEBAaWAmLgfBqc0j8z4IMXfBHBWDSZv5-Hi2fRpeZZ592SdeuwoytG5QA5vGs2ocXiq_sJaGDUPDAzZJFmSUBQmp3inVP4EQAYzBUN4l9SddpqCpqmelxmAsgGtlF1MXCBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzF-NA8ynDHNJ3nKSh98tatDT57mvgI1njE64JabyJnpjZBE7id3Wc48eQnAgD0SIPjaTuEMxs4qKzk58rfQ6yC89B9lvxwPS6kXyI1AAGLdgHlnxCAn5Rfgm22XG5WSN7IoIrXiMjiU628T-ASx3nmZ-GauxissE7OLhxm-OIxQAoKL2Op9WD-UOk5byrzQuxkxKaF6Q5YPPEHT-_2NgJcFu2RbT1-os16cpulCbRp0qu6_0PN26AHxdhcgV34gl-do63pua9mUMaAbP53pw3VO9lBn-bJUc3Casuw6L-_5-dHcSisO6nyqG6Y3xrze_C9ticUCU8InG2HGS9ZPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
اولین حضور دیومانده تو تمرینات رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103013" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuxpmzIfjOp6lvbP7ARaPV0ZLvrpXaxzKVK7O7QeIw7oVXgFI_3OdhhN2KAFLKqfsIGN3dhIS1J0Kc79eF3mLwCDcqml0gYJBkRT-6b9efCQjDpGUay1doc1sNE67E2GcLuHJuQO8b7lYHWLLqKiA9TO07_sioOyk7SuwMtqDy7d6dIyIWpVF-lj2KJEHeBAvr2pYR9UNMoPqbEbBkSzYoXf7lmcbScC59m2sF8uSyPBEEumkXForzDdbdZiDPEtNULNurhYK8IB7T7JrcoozIb9NBW5Gy-j6NXMwNfGsn3YDILzooMLiqvXkzRb1KMATCjWC_g0q8bjNGOt_kqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: رولی گلر مارسی با عقد قراردادی دو ساله به سیتی‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103012" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQoIpY9ThSgFgkv4v5rNjIP1jP3OM28mmiZGEYIO0dB5nOEZlfcFgFQ5RH5i_VCYrjEvN-U0UWIXeMpb-pTDoXaDA-LNDhqikeIjRiRIVcHOwsq0O7SIqKqIVKAITZNLA0VPsiEPXnmmlb1z8VYPnckkgKQwIaha-9RRcBi9WhNIKyu67dhPqk8gxzyKB2zRiovJnfnTIKdXUGoVGSYFPuuArKFte9InUOHA0fYpCTMr1AqMjDS-zoGJK0YMlUQKMKpQfsZ55Vwil5b1RnsHn_JOgg1rLrQUwTn7MWHUmsyKJVNBkQUt9_Tls6NSFAgyIxvRYjWCtDesyZltb13_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
ژائو کانسلو در تمرینات الهلال؛ مذاکرات با بارسا جهت انتقال دائمی به کاتالان‌ها ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103011" target="_blank">📅 20:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVx_E5uaAOpbMPfzQegfvt-cgC4_GA8LZH61amkvPRliG2atGD-uhzTmckXLZW-iOw8B743oMPJUxOVFdQuUzqrOBK-Fa74KhOhEfwIa4xO4-ktbLTsdwWAyMpXdeYYhgA1hfxiqQoUbi6m08xLlPXZvUC425t20vj_0KvwxEXMwTrU1-kQ6fXEBvmn9y2DnOo0hFIqltUC2v9HYpQYqcgHORNLS2ESVzITEgh-i5_8If7mazXxFqGOBeKkosX9LsnqWeODmUFQ6tx1Vani3FCcej7xnd5wZgGokWoBlGnmA2U4UPfDoVVz8I2pBdDIzx6ruLw-6v5zNe6Z7O_BEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جناب مالدینی بهتره یه تست DNA از پسرت بگیری:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103010" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwQ32IpzeT6ta27DDOMe1ijUYjJicRA5hoptJ5SE44cLZcsP9Crcs-D01eYDru58aMe-REoxUeMUpO08nLc7j1jKGsbx1mEtnXZpd524cfijg-z_sFQZ_2EUaetFy6xD3sK5e4Cs3rsRRHy_7cMJSYInfIQXAbvJa2dfedqOCvcOKadGgAYcrHxCPgdTegazyM-dLzuePE7q-42rLzmHDD5FhSk4Pp2BRQYtRWTl3-gpqn1VrNAyJaHnbTazrHn1S16I7gIrtRWTSbhw2_fjIaOeR37HAGSznSZw4r_niHC-Zjfap1mDcEYKTh-tdnUIYI9f853Nx6wBUosFu-WJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🔵
سهراب بختیاری‌زاده فاز گواردیولا گرفته و تو شرایط کمبود بازیکنی که داره، گفته که اندونگ رو هیچ‌جوره نمیخوام چون جو تیم رو بهم میریزه! از طرفی گفته آدان ۴۰ ساله رو برای نیمکت‌نشینی میخوام و تا نیم‌فصل که پنجره نقل‌وانتقالات بسته‌هست، باید برگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103009" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پیشنهاد اولیه بارسا برای خرید رودری بسیار پایین از حد انتظار بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103008" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق‌و‌نوش لامین‌یامال در ایام تعطیلات در کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103007" target="_blank">📅 19:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSS3CU6yaXOwhHamKAcASjy-r8Rr1iYc0Q5kVY8sV4qWYWdfz7-XvNs3zGXRyNWfrj7q_GRbgtfoLjFCRPtms8lGzFrcijILO33sRB_STXrUX-OEY_ms-MWUlX-1JpmIBcYf4st55Z6WlXR6ttdtU8A9e7Mo-hc6Ri28Gx096DWyCz8L3k0sUPUBQULDQBi2XCere8fVJNlJttl1qoF7IM5SZE7c8pkJMX-EdIUVDLDFWGMRRcRZ-k_Yujw4ADcO6bu0yETVGCJRQHzo_WoA8MX4SirMghovHrzH60Ok_nG25KiL86PN0GD_DFuLiBI30eANH-1h37sYBuj1XbTrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
دقایقی‌پیش سه‌کشور عربستان، پاکستان و ترکیه پیمان دفاعی سه‌جانبه امضا کردند که شکلی که هر کشوری مورد حمله قرار بگیرد، دو کشور دیگر حق دخالت و حمایت مستقیم را دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103006" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpecby5haGTOuMEBnsXdI2oEqPn7utEUgETM8XlTML5TEv5DuHFnTx92s2k3-ozL03uA1lMEYhKeLEtq9fSUMA1CdPRFt2hEVafPsi6YGCFnvClHVZaQXx3MypB36lfnXmo005pmMxK2WSKmvF47m2UTqYxDgVpBWTx3w7CN6VmvyvgZ-45r6_OQ7AQUYrN5VSkZPqqdewUrtMgLbkYDWB8GZqb4Nz3VZl3e5E94lL6N2PglqfHHeG8c-zOezhvpUIEesIKRMb4K7H5fJae84tNgHmNiG5SVYr5Kg_QjGVh5gKWoyLajuOqJWNz3RMrQQwES9_rv5L1z2mCJ2ZKFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین دریبل ثبت‌شده در فصل‌گذشته اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103005" target="_blank">📅 19:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsK72Y-NXfT8ChQ1vfmzrqgAxfg09r9Nh1BVP2BzG_VhHoswGTQcGhtuqhVMzIkXTRxGY2N-Jf9XseyaIXCiDWKpxmsvaYbMWuFksyPZgKm_5LvodNassimLIfVSXa5KwfcgfzrEdUVoLQ1CPO-0N4dLsnEGREMaaaCnyFIKo_txfnycz_Ahn_dXHkmcazb933_ynPL9aFsHKw4KQB4klcAXgBJkqEzrXlXUK4vZBoxPnAhK1R58VV-bkDP9uuGSaFHpAlZhoN-0ER8kJ07tyzxiDNH3k6InxINg-9qRVZo9PFIQtJkqO82H-5qMHjhWfGvk8elC6zboR36ZbsPfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خوشحالی بعد از اولین گلت چجوریه ؟
🎙
دیومانده:
به این شکل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103004" target="_blank">📅 19:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
صحبت‌های روز گذشته پدر زنده‌یاد مسعود ذات‌پرور بر سر مزار این قهرمان و اسطوره ملی و میهنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103003" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تو مسابقه مردان آهنین دیشب نزدیک بود دوتا بازیکن با همدیگه سر یه چیز کسشر دعواشون بشه که بخیر گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103002" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL0Hd3gOoXxIp3ZKnA2YB1nYPufECzG5KkJOMkT77AyAnbt2LKUYKNz-RiKQaNXhWJTPBJPOqNjojeEwZTMmvSfKjnMYnRhiRP2vE6d2UWmBVdizGKbg-xgKkbJMdgrOHRt2KGLTE52FYQ6t_v-RntBqpihogr1b_MS7nBFl05RA386306Ze-h0UHZv8OvYqJFWPXLMDqKEKatt1cx2XZn3NVKcVVs8fLme9CUnOp7jtWDM9eRGIX7qah44DEVHzIOS2VMwgwcYhSlZlFFZuKVOYTlZ_P-Ylo-ljhkvyMbKHtByLVJrQmXdbal7LtjneGyPnGSJAd4SjRYS8fpjjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWSe-wPZ6xXjy6P0wuKKaYiCdanBA0IAFkwB0QeliMTcIMDYHvxrz6yTDtac3gB6akI6Hs3KXLQzt7ZUQVoOT4eQBybuGnDcxf4YRJRUvp1uMjD0JS1WZEA_Z8WZdQmd7LbUqZYf-Y6OFQcmODxUH_AP_2SiIFOybYLSexnaWJUrGwx7sjr9wdKRf0yYeT_Tt0rOmyPMe20e9mddg5-Ft57cw2T6nu_FQ1XgZd_mucP9pyNQfbTPfxI7Irck4RM9vZNNjInkCLS9ckMAaGNBUYXIItTgep8Wt5W0fWYsb2ytWRq-HtjBt23ts542x_ziWLDDL3b3kUDJC3i9JPu7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMB3KisPyQu8xYIlf0mMKRyY8kR0fytcyAZiF8wdMgzB-_EeFdod2Hd8QSJLymwLSiHwEou7vrRnfQEaQtghitaUM10b8GIceOBp47IQOdd7SquimSEpoXvtJRikAOg1NFB0-fyJ53KmuD4oAm24pjCH8IwhnPB_3SC1TVC0PJ_XD264S-sttYREa5EPyvJsVYzL_72ZLZd3HxDyjhtR8L-NQghOKpbb3q-4uP6grfOkIG3XHK6-y-DZ8BdsNa8UTYLwtFVVOHynFkuPLoKoYRoxWx02OPbIxCnzMuzKdZDEwi4GX4nYojXw53sdpPxIMysIGSWZQmRqWPVB7RWVoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102999" target="_blank">📅 18:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBgapaOaGtG1eM8UOKUMmaZFINBXxnuV3c7ipx0u5oVHFHIFriD_J4XaOgt2CX3d0O3RJ-9hW0FNbAX3h9I3dOqvjCUadE5pivtOQrBFNr3GtauUG4eXmziIHW6lvavtGmF6wPGjHPLOhioOIik9ZgUd7kvEswSLhXzigybDXBIoHrIi4r-VxpJOZtrgIT984zHYtsRKQq23h3WT57LfPUdyoocD7871FkN2r3NPX2pUIzBn57CUNGZLTC2bZFvthv_FiuKY3dKkG0A3ktMyRaXCEIFHXrBGHu2VCdNYT8QGzYTSGBighL0KjFYjGBCS8y1NtFlAVcKFIUjQjeaPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byG-6E_DjEx782N_P4gxbgRpNpPQelw4-KNo-HJ8qYS4dG1u5tmsCZkS0bqJCvCiNZBjvWEoNYb7xnN0iRuzyzPWXqpd0R26SpSl72eRcHxKzpqZwd2eTSTJB6kmfpSMNb3sWDS40rFHyu4Fux4dVcsp0QjL890Ne81Yq4fUdj7eVykzPafcPfXYyKyjQEooJYjCgiqlO2pZRXdFxa9zJR4EEuMskZFfrp7GHRTNYMQDImaC1PONZQLkUbZF2tupHMhlA1J12cMVC2kBQlerUW0eIWvnzYxJ4ieJLO3NyHrN1WakkGIQOfIeD43wz5emMeNEYP-T_EbSYUpxQ1SVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvKSyds0qk3afQchL5rG7EUTZ0CTC1YT7Fb9jTTrb6fG3JZaSb4SHaOsFwlmi6rhJkbnh4AoxqGNLIE6bbNZA5j1ovxbRxCyLGnS4UILHWb9uuMUhs9JVJT_GAsxGuzsAewDi885wcTd225G38E_j73i65ZHfkFiZ_KKoEwyaVo1HYnIFZ7T3RR4JKCdIPpnIW8A3PgtBAs9k6KvvO-byqF1FJyzxEB2PJ1uTu5g1RohY9hRKqBQhfN909V4Bm3poxZ3Uw9iX65Xw0TCjUxSfPGbqK2LOzZnCUfmMVSxnDeGfxUy5klMpU7iqXIvxwKtbyppl3M37aD7Rs8F9aAkow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102996" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3QFHfBb23W3o_29-pcBnN1XEOnGSUDqU2Gfbzp1nsaOBteN3NLhNj-oREUOLt-WeTbcF-yMaz0yPPRhw4Pt3GwCGGJRFGhh-a6zX6nOXXUtvOTwWUW4B3QyzZfPYRrVD56b_R7OgVJm2paIA5IERTulnVOrcJfuFJ_JkjZZ_aEQyr0Jf89R9oJF4M_UY70HDiiJaqObZsEQYaJSDM_9f0O4ASIsI9DEl2ThaVTPtxJhgOQ5XZhDUq2eHPjtWnhF2WBlGjHNA4pQ8PyCucDNYmjszYbYSggxNcdSOZ0gFzKsLXQ552YfhIS0iyK_Fsa7cnTmTeWLpw8H5B4D1HTJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیومانده در تست های پزشکی رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102995" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
❌
#فوووووری
از رومانو: رونی باردغجی‌ بازیکن جوان بارسلونا که در فصل‌گذشته معمولا ذخیره لامین‌یامال بود، به صورت قرضی از کاتالان‌ها جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102994" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOwpflDIYXSiIAczLWOqj0V3lUrYDpnIeLdT_0E2m-7BG5gVPd4_YOy0A2evpK_Rdw2fxtI-uOZXi69wWbCRN1qw2LeL6oj4Xr8AUlU-LB60Kv4CVuJ7nOzUV2gpNr6jyAKt4g3uxd0B41iMVR87MvQa1hXdYUf3bTpdsnGfHr18jkNZPbWQgYOTuTszCDC9hblg8SQBSY0T2bqtbGuJPiIYH0EJgxan5aCEKhUr94dEwWbXtzM4BkYTzKFLCmyazlj0P8KNd61LBCbohnSL3ZbVonUtfkFw8IbwAos21Y_6SQzR5Phgp1h5LzH5GsHCpOfUc2aI2Gp0gECB8qpU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
✅
بنظر باید تا اواخر امشب شاهد خبر HERE WE GO رودری باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102993" target="_blank">📅 17:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txei8WbWxE2RDmmzJ7UfdIKj60PdyzicHmXVPs1pzYIAhBJGtS2eQcYA9yglA7WUlvfM0nosk3y9itIO31L_fGqr7XJSZKDaMInWq3sgVHlBZHb6Gu5q_4BvkiV2PXQr25mG7z6aSxos2m7tYW5DaoiQyfzBcglFVRMVL534DSo-MmqEL5grq2xmp_icsJGVsH2KwQYGeVYLxt3dQm0UJXAfaVbzK6qTtFkB42i7yvzceMh60mQeHIe-zBavrk6WQbk3tCcisDS2qfHTk8499wvPe0QpBX2anVEO9xPPTzCZeZZ9rXLvvAXm2g4sJZO0rHrtq-83Ul7uNMkU66WadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
#فوووووری
#تکمیلی
از RAC1:
🔻
رودری روز ۱۲ آگوست(چهارشنبه) زیر نظر هانسی‌فلیک تمرین خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102992" target="_blank">📅 17:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از RAC1: رودری با مبلغ ۵۰ میلیون یورو به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102991" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای رئال: اون دو هفته ای که ما با رودری به توافق رسیده بودیم و وینی هم تو راه آرسنال بود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102990" target="_blank">📅 17:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مسابقه مردان آهنین و فرامرز خودنگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102989" target="_blank">📅 17:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwlG3VCsMAu5m88ubns_MEi8UBW80xcvNu7kEh3tBx5iagZ2iowGUFM3ceXaUjDgxzVSJrzHEEWaXfqvc3emLUKia2Fv0uxtugbokORIXRTnIGV-Tdsv8aBkX6i6SreblizdEFSpwoe9wzsjAYmfQBOglexgvApw9YHeBJAe2n43-iWygQY67w8sEO5eXVEvs9O_BYX8PyOuhCDFvG_PRSkJavZQMk1QAvCuZmmgMgSg6BoemA3zJYsDkfBiUEnPDCwL985WObs2Ch076Ty0rYBD1zsQXhowwU5dPhUnGA1iuqXu7GLwEnOY8771YvQ8M8VtS-XukmFSs3WVF5nY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
اورنشتین: بارسا پیشنهاد ۴۵ میلیون یورویی برای خرید رودری ارائه داده؛ درخواست سیتی برای رودری ۸۰ میلیون یوروئه.
📰
رومانو: بارسا حاضر به بیشتر کردن مبلغ پیشنهادی خودشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102988" target="_blank">📅 16:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=T_8QwxpFQz5bMnY60GOdVbDXuMDC2smyumxkiKbsHg9EdWU4Xa9K-32nfkQVjNQqciO9BP1CDIg9S-WbOUpXUSSyMottQ0T5zh2f8m-NJMJF8IBXgBmHZX-WdjTxdCyMdW3q-ZVl2VadZEeiqPhAa8z3KW_G-4sW6yP_mPFvUYZ_OCSmKtz4EZc8xHnH2SqH3ovr6J6rPU9d47qpcOnH8zays0nZ8zQe3FZrgRS8qib9JSpheBh6n9b_ebg6zkTwVaDq768Va_5sdtAxadnqlJmDkSKEWvX5swb7a2RDh2Wh2oQqbN7RpaaxkIMBr9uAqJALFUAOU-PZJ7Pj3-hTnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=T_8QwxpFQz5bMnY60GOdVbDXuMDC2smyumxkiKbsHg9EdWU4Xa9K-32nfkQVjNQqciO9BP1CDIg9S-WbOUpXUSSyMottQ0T5zh2f8m-NJMJF8IBXgBmHZX-WdjTxdCyMdW3q-ZVl2VadZEeiqPhAa8z3KW_G-4sW6yP_mPFvUYZ_OCSmKtz4EZc8xHnH2SqH3ovr6J6rPU9d47qpcOnH8zays0nZ8zQe3FZrgRS8qib9JSpheBh6n9b_ebg6zkTwVaDq768Va_5sdtAxadnqlJmDkSKEWvX5swb7a2RDh2Wh2oQqbN7RpaaxkIMBr9uAqJALFUAOU-PZJ7Pj3-hTnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات گرما روی رفتار مردم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102987" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=HtDj0fPbrSkOpckrIIJh5evjnKu4rsAssetTmAjFnfkB7q1vlRZamQEN22TUqC2BNhl_NhhvTWa7MDITyOtLAoOy6vnmSPrlT5X9tm0qlEcV1_X6rvxMCu7RsoEDKFEFbip1LqHy3bMcwQ7nrL49aP_WoMDxRFbFBE0h3Rj_4IbQFQbI8FXYb99EsrJWiNYYFrl-d-3P74rtSieJ7aJrl73kmIWbF6gA5dzXIMdxJk-uGlmKmSF1FFM5gyZMpWrqajRkNo017h8q6Q3aVIRIdbPPMEFVaEjrmPBhGLqZQY6mmrsbN61m7epO1dzqh0hvDGSXSQ9LCpLgSqwfUT64qK5fgMYiEitsIO3v3pr-k7a3Exo1zlbfLle_wi5FfK8Hj7QsjLdAj0gJO4RbVksYhpxbimOoFuZDewIKC-zfVzj-OARWlf5pgqMniiyEPmLbAyvGc_Sqh5a3cZ7EbQOwqR3BCUcEft-a7GGvp5odbn3BDerVncgponUv2keHpFE2HFTzB0bf7GeoEkBrDN8-VNw8ZBD8vZtst2xw4k-UChjslk0v3sPwCxRW5BkjPNoKPwc-LSaDR4V5y7MNeW2ZrCowqTo4OVHTladraOYSLSkz64xc2ynIyQ_17karbnvyaGcEbFX1sJORbbsfJ3fbxmyD6kVgZ6L19NZIjzEUn1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=HtDj0fPbrSkOpckrIIJh5evjnKu4rsAssetTmAjFnfkB7q1vlRZamQEN22TUqC2BNhl_NhhvTWa7MDITyOtLAoOy6vnmSPrlT5X9tm0qlEcV1_X6rvxMCu7RsoEDKFEFbip1LqHy3bMcwQ7nrL49aP_WoMDxRFbFBE0h3Rj_4IbQFQbI8FXYb99EsrJWiNYYFrl-d-3P74rtSieJ7aJrl73kmIWbF6gA5dzXIMdxJk-uGlmKmSF1FFM5gyZMpWrqajRkNo017h8q6Q3aVIRIdbPPMEFVaEjrmPBhGLqZQY6mmrsbN61m7epO1dzqh0hvDGSXSQ9LCpLgSqwfUT64qK5fgMYiEitsIO3v3pr-k7a3Exo1zlbfLle_wi5FfK8Hj7QsjLdAj0gJO4RbVksYhpxbimOoFuZDewIKC-zfVzj-OARWlf5pgqMniiyEPmLbAyvGc_Sqh5a3cZ7EbQOwqR3BCUcEft-a7GGvp5odbn3BDerVncgponUv2keHpFE2HFTzB0bf7GeoEkBrDN8-VNw8ZBD8vZtst2xw4k-UChjslk0v3sPwCxRW5BkjPNoKPwc-LSaDR4V5y7MNeW2ZrCowqTo4OVHTladraOYSLSkz64xc2ynIyQ_17karbnvyaGcEbFX1sJORbbsfJ3fbxmyD6kVgZ6L19NZIjzEUn1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وقتی صحبت از خایه میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102986" target="_blank">📅 16:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102985">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=smX2TLoj01e-0CKypcVrYh3WYv1j0gN3ShsCCVw44mEXjamVoicWHaIseWo5gXRudjKAPZQFnOUPB1XbgqjgeswOhsFty_MEDgry8bTqEtR8jBbi_H61Xxfvw1ii2ZN2jFIc8e2pIVoKhIXpytb5GimHO3TzgCeK4EWhlA9I-mx5BrAUKBsgymTYPJyv1w2iW-4zcqq3sRzbtSxrHF5qZ4cElck5P0hOO0SJpGI6SuV09cjWeMmEGwFTU5xP4ufz-o6j1wRcLRrPDcM1V4gk92V5ss2FT0cL9AmgukL50gTTHAJCe1IO_gJAf-cwqS8AyOGqQQSfL5JxjoDGt1E5aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=smX2TLoj01e-0CKypcVrYh3WYv1j0gN3ShsCCVw44mEXjamVoicWHaIseWo5gXRudjKAPZQFnOUPB1XbgqjgeswOhsFty_MEDgry8bTqEtR8jBbi_H61Xxfvw1ii2ZN2jFIc8e2pIVoKhIXpytb5GimHO3TzgCeK4EWhlA9I-mx5BrAUKBsgymTYPJyv1w2iW-4zcqq3sRzbtSxrHF5qZ4cElck5P0hOO0SJpGI6SuV09cjWeMmEGwFTU5xP4ufz-o6j1wRcLRrPDcM1V4gk92V5ss2FT0cL9AmgukL50gTTHAJCe1IO_gJAf-cwqS8AyOGqQQSfL5JxjoDGt1E5aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گذاشت همه چیو رونالدو انتخاب کنه
#احترام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102985" target="_blank">📅 16:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQvWhnqjR__0thO0ti9NPHn3Txewzff9xJwIaT1LTcyfXLezaGqvhPha42vRYxXh9g9OyMjZ6qgZYPFF0nr04hxMJCqxN-tPJmk5ZKpJNlWsLfOztnejjmJSC06f5F9G3kQePC1I67vZB3VcVWTNOotBGwxYl4wmt-aE1ZraObiyu6OCShhnk0AYfh4qtM_AcsuyHbxXtw5tRvYKMj-WsEJ4c5mdgJCo69M8VqyRKlgg7v3pQZZv2LJgTJvPyNH77k9E8g5alWn_qbcUkQrTSoySxBI5PuZUaQbdbjVQki5TGS_yo6mm4m5pgTy39nqVci5JJPnlz3_9z0C_YLhLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
منچسترسیتی به توافق با لیل بر سر ایوب بوعدی نزدیک شده است.
این معامله در حال نهایی شدن است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102984" target="_blank">📅 15:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=AgUQJkZ44AZJw7dQwtJoRHzK_M-OJUNT8yuWCLgK6XAPp4zrhSiWmudkbxg0hBKe-mIQi1m37IS8QKzFdBdJf2uooIkRhUHVTzAzkhdbUQnc8xvEi7KWSd_Xq8N9jeX_NlPBu6ohU2sQFp9TNZmga08WRdpwxOFOfKGgKJTXgTUnPDLNo43GGK8DcKZxxgYxo193wtRwTxjVnctJ3pyijPQwNidNRtPzn4ViIshPN1rNmlwpyJ7ldgFpJNlYhLlgt4AD1gxdc3R0n3hNb0piajrGk5uC7snmOvMWO6u0e1yQV_9d7j6SdgLFgIJSl-ME2aHEI9J_sVSd4mcdSVl0kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=AgUQJkZ44AZJw7dQwtJoRHzK_M-OJUNT8yuWCLgK6XAPp4zrhSiWmudkbxg0hBKe-mIQi1m37IS8QKzFdBdJf2uooIkRhUHVTzAzkhdbUQnc8xvEi7KWSd_Xq8N9jeX_NlPBu6ohU2sQFp9TNZmga08WRdpwxOFOfKGgKJTXgTUnPDLNo43GGK8DcKZxxgYxo193wtRwTxjVnctJ3pyijPQwNidNRtPzn4ViIshPN1rNmlwpyJ7ldgFpJNlYhLlgt4AD1gxdc3R0n3hNb0piajrGk5uC7snmOvMWO6u0e1yQV_9d7j6SdgLFgIJSl-ME2aHEI9J_sVSd4mcdSVl0kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسابقات جذاب دو امدادی المپیک ۲۰۱۲ با قهرمانی کشور جامائیکا و رهبری اوسین‌بولت افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102983" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=uFGxgI5IpeBD35ZGcmjJmoZc6z07pgqArtuWLLpCGqeXMkmD53XhgPPMKYgRCuiN_Q18sciGktz6pR2Txg3A3OE6VQQ58gSyydshyswd4LZsDk5kq2hgF75hcEstLe9Lsoze_qbmeopEoVxYHme_46oNDY7UZbiugYChmAE1lYTVCqoFZYYO_dMi0rDU0NBVfiUQGTvlc9GVmYlduMddfCCwL2b23IRhbEzAV91TbxRJVeA8hfXJz6rUqWgbLj7seBU4VKGoGfthsAAyyOjEQDg2ocQbjE3aeAm0Cd2uM3xVDw9cxoXiFO5gNJR7RJraLQZ5dK2k-CImyQb42DYRTrxu4qenVvPxSmGqYSIXG0JIaY1QtaJcwJhF6S-4oWLrfaJLHXsiHZqmHOcxH2JJeO2kIzaOCCdkuHjfMMUZMrWZjJofTXhOaxH3Cka8hq-_L6nx6uvuRL6uyibI65UuOAiLBL-NTqt3xOa9_S67o5131s2B-BbPP0Kkzok_6pA9r-1Mm_tp1KwEri6qpJ2UkW26EkgcUCA4WHZw0uaLRTw2Z7JUWubajOFR_2yxiOmsD5c28kakERUy90nfJjZixOBEmfUjeoHC6xwOh7JF1Z66wge54VJGEL_CW-QLnYEYSdprrelgAgPeopZharmFmk8PVAxHlzzcpgyHR6_GudI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=uFGxgI5IpeBD35ZGcmjJmoZc6z07pgqArtuWLLpCGqeXMkmD53XhgPPMKYgRCuiN_Q18sciGktz6pR2Txg3A3OE6VQQ58gSyydshyswd4LZsDk5kq2hgF75hcEstLe9Lsoze_qbmeopEoVxYHme_46oNDY7UZbiugYChmAE1lYTVCqoFZYYO_dMi0rDU0NBVfiUQGTvlc9GVmYlduMddfCCwL2b23IRhbEzAV91TbxRJVeA8hfXJz6rUqWgbLj7seBU4VKGoGfthsAAyyOjEQDg2ocQbjE3aeAm0Cd2uM3xVDw9cxoXiFO5gNJR7RJraLQZ5dK2k-CImyQb42DYRTrxu4qenVvPxSmGqYSIXG0JIaY1QtaJcwJhF6S-4oWLrfaJLHXsiHZqmHOcxH2JJeO2kIzaOCCdkuHjfMMUZMrWZjJofTXhOaxH3Cka8hq-_L6nx6uvuRL6uyibI65UuOAiLBL-NTqt3xOa9_S67o5131s2B-BbPP0Kkzok_6pA9r-1Mm_tp1KwEri6qpJ2UkW26EkgcUCA4WHZw0uaLRTw2Z7JUWubajOFR_2yxiOmsD5c28kakERUy90nfJjZixOBEmfUjeoHC6xwOh7JF1Z66wge54VJGEL_CW-QLnYEYSdprrelgAgPeopZharmFmk8PVAxHlzzcpgyHR6_GudI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
روایت سبزی‌فروش اوکراینی از حمله پهپاد روسی که جون سالم به در برده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102982" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102981">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a246a820de.mp4?token=gb1BUSu2CpKgTt0b1Q4sRmVQBe0JVb2pM5kpxiRKlWNVSBZQZbe-2mMoKRvkD4beuGhjrpY7CEnsq2GzERS9Yh4u328tx6LI7SFeVoElL2RFAr5hUaIInRAeCiUmPwoeBLDV9y8q4Id4Pg4qwO5ubZdJcDL-sx05_IY9cZ7tEHfZ2nNsVVirEsWEvBn4EytQbO8gOttrN01oyfUgLFwFMEkNipsPxchlXQed0-pBxIqV_6NAIrC45JH85CDAqIU6F9bqgPzdsf6HUxC3gTOCCpzymoCP89H9nGY-cRezPUxiLj_DVGwNDpYGparvyu_5MB8TNHxUi3ZK5TcEIL-YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a246a820de.mp4?token=gb1BUSu2CpKgTt0b1Q4sRmVQBe0JVb2pM5kpxiRKlWNVSBZQZbe-2mMoKRvkD4beuGhjrpY7CEnsq2GzERS9Yh4u328tx6LI7SFeVoElL2RFAr5hUaIInRAeCiUmPwoeBLDV9y8q4Id4Pg4qwO5ubZdJcDL-sx05_IY9cZ7tEHfZ2nNsVVirEsWEvBn4EytQbO8gOttrN01oyfUgLFwFMEkNipsPxchlXQed0-pBxIqV_6NAIrC45JH85CDAqIU6F9bqgPzdsf6HUxC3gTOCCpzymoCP89H9nGY-cRezPUxiLj_DVGwNDpYGparvyu_5MB8TNHxUi3ZK5TcEIL-YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇹🇷
جو پشم‌ریزون در مراسم معارفه محمد صلاح در ترکیه؛ کشور‌های همسایه ما دارن تو آرزوهای ایرانی زندگی میکنن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102981" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892883543d.mp4?token=hDuqdjNlQ_W-6LIfN57UBEvSbQ-X4L4tHoQgezKDH3o0FtXrXQg2ibiB6euSD_8DugQboq0iL78cNmXlyreZuvcXGnfulFXFeub0ABZ_-jvwt6GrmnSV44Y3VKzfcd4LAro0NEfEg1r4hMTeGEk4ouTe3DiW-g4uZxNKRXXnSd8w3lsamQYxgsR5uu4jvn8fGbEGrqhr1a5foKoWdECSzyMSWo0XGDnRhdXzGb9FRaUIoJv73OyFy893LKZqqPBgaYsWFmpDYKk0FMQ-9s0cK_ZpcL4Bt3APAkxpz5n6veyxjZAOkuLZz3qwo1doqzZW9456MpPP3TycOjeceNtiq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892883543d.mp4?token=hDuqdjNlQ_W-6LIfN57UBEvSbQ-X4L4tHoQgezKDH3o0FtXrXQg2ibiB6euSD_8DugQboq0iL78cNmXlyreZuvcXGnfulFXFeub0ABZ_-jvwt6GrmnSV44Y3VKzfcd4LAro0NEfEg1r4hMTeGEk4ouTe3DiW-g4uZxNKRXXnSd8w3lsamQYxgsR5uu4jvn8fGbEGrqhr1a5foKoWdECSzyMSWo0XGDnRhdXzGb9FRaUIoJv73OyFy893LKZqqPBgaYsWFmpDYKk0FMQ-9s0cK_ZpcL4Bt3APAkxpz5n6veyxjZAOkuLZz3qwo1doqzZW9456MpPP3TycOjeceNtiq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
سرخیو راموس: فراتر از یک مدافع.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102980" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_lHqq54_D-GR97YQ7yowx4F3FdJ0V5V1nnC3IG3Hee-2tFGOxf6qIAAf0GoTXqaCsLzyCghWY_S_AxeHMNyq0oWapqaQRCpm_rK5sLh3Z6FCk3-_NvdPsq5nFzpoEwFOCvL_TrdrJ1F2FrNAtH4Z06CyeMhAJFAVYrJYUYulnV_2ZEbIHXvcoml63C0DxHMt9aPkzRtSHeU5shBpIQEeHZRS6VQOKQ8qHEJJ46w1OGy-jmhIeTLAPOGxtrKJAVlGTHmuZp8S2rYafrIaVdxpPjfREf3zoKPxK_9c3mB0vzNjOlKer8RQa2VcPBZbk5fFB_U3acXBq9egRqxXl7_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: روز دوشنبه قراره یه خبر بمب راجب خولیان آلوارز بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102979" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXjJ5jzl7lftBp3yjd1H4HsKAjUIDTco9glOvKY989OCFsH1Z3uRbY_TppGckd5Sf-vxrqNfvcUZEzojPmiJwVoBgRvRqJecRhYcMONS-VrYw02TCLHBvVybX-pK-GG-rbsWl6ErYTWOypWKiqGiPF5EpJYtqV9g9dlebkTe0q1mQoN9bvAI7fs-vHTopaOs4sjKOA7YfVDfMCyhVIPcuvO__oMMsGngxQ8kgs7i-Z0BS9hZKN4ogrE0xlb0J8sOD9XnwqD_2ghYpW_jb635oyrPIUkII2PaJKW8e8Gnv7A9MaPfnM-wpKpO8YZVp53JTsfT3vAfziGwchFUeFjb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
نقل و انتقالات تابستانی رئال به پایان رسید و رئال مادرید معتقده که ترکیب تیم ۹۵ درصد تکمیل شده. تنها استثنا، پیشنهاد بسیار نجومی برای یکی از بازیکناست در لحظات پایانی تغییراتی ایجاد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102978" target="_blank">📅 14:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5d0Q5p6W6M8mFVyQf-7aWolE031BMb_9lnTzanAI7FEw7QhqxAMBDHHAsBzmMTIftvNHmnX14zDhGThFGI5OodB3ZL6Ga7e4Dd-CZVtMYELYBJYAqb0noHHIuQ56GWsyA5AOJlCMk9phoFoDbOFRvs4ZuJo-CxSCW3rLmK2VMHDS8HIm-p5OBrizPMIZJ3E8E3qg6cTHt9aO50STDc0xi3F9H0cIhPD-ha4dn4oJydW-y4J2Hvkg8dkLEtrcNG1Gp60VhEOjzpcNkBJ5NGs8fB_LWtUZwt4bN-vi0fHpSgP39oMCGuGmDloAazepDUbNL4ZW5oGik4kjU86bBIfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رومین مولینا:
آرژانتین، جیبوتی و مکزیک از جمله فدراسیون‌های فوتبالی هستن که از جیانی اینفانتینو حمایت میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102977" target="_blank">📅 14:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlXT3fcPMNQAQbqRwG8QE-xnWAhu4oVXTW_pFLN_ULQdKn6tekmP7eRJe6HFXeAItci_Z-yZbyn8XnivFf0-bfF2I-lXzhkAe6zwGCh6yddcycxh6gY72Wx2i1CxoqZeRtGHM2G9o_Hq-FfcpqJVPHNq_OlD5Su9Pcv8Qi1PFU0TpmG0Nro3mBVUoPcJPJJfL9e_vL9aC7KL6Mr9tcbONC8GtspsTIFQ-BRjYwaHpMQr7mIRx4FXSCayyWhprsXv6d5NaBJfUIap2SvdGHLSVJSTzMxD_apq-TikHe0rEOctLm9yK0RXHBdpOZ6TsvxZi9MxSF-f6YDVMDRCyTPagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
برخی از ستارگان فصل‌آینده سوپرلیگ ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102976" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9noE2Oud44fNMJzK6qONXpwAdJj3yd9EeqNs_YZriLM3GX4JqxdSQncZlsCjpSHysfjk-xy2CoOY5h-MDs5ey-1lvztloRNPuHxIFsYYfCoUGOraxXPbY6_pqEKXxFxnkr11t-MdUIej8FxG7P9M-dVChoCTwBaD9vEApxWCikeJrx-2JI8pZ08fdZ3DcfFkHNcw3z5CnVuWtvVc_V-SYTHLvWKF-Nj7s_xgXnONw4s7WRNpSghkCe1lqpzWcGme8iyZ989tcJ9OqBKxJ8fRg-mnuo50JgP2wVqh6TpZHHr3B3qEcVzTq1mZjzgT4yU4HuJh4pW0VCMQ2-_ePKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسطوره موسی جنپو، وینگر فصل گذشته استقلال به پانتولیکوس، تیم یازدهم سوپرلیگ یونان در فصل گذشته پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102975" target="_blank">📅 13:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102974">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6I3sAdykoC3s50xVCDZyn7QUa3pxR3O3qtg3me129UBBUno40zDMtiVY3xDywi2CjhyLmJgRCdQafR-DDcIgdf91ULxeSkVL4Xa_A2kepOQzjVVU0rxk8MeOJFl3R6dtCsQwbUOZOVVG_qMkT4yS7MlKOx3RlolZ2VlJYN8KdZp7WdzsbyRBo3TXXGIbhm7Y4hnGoOQMSixXikJLs49kuvMRL_uQx7Pp7Wu7jLqe6TZwAfW7bs0husxyv0EyE2PU_a1AwVdqhiHdx56EttVJmSRaFf3YwLuKZnpgjvp6lA0XKw_yzISMapIZdXslanmQTtjn0U4-QWr4oeod3q_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول برای جذب بردلی بارکولا به توافق اولیه دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102974" target="_blank">📅 13:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
این شما و این گرونترین خرید تاریخ باشگاه رئال مادرید: یان دیومانده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102973" target="_blank">📅 13:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102972">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4YQ_GKZkijnrCoNTaTTcZBQa47JYOU-F714i_y7-xY6l5EB4LfCB5GFonpj8q6pRrbOgS0wGjWfuM194OTtl_VA14G47UTMad-N9MAua43KTRZw5NnIdIa1ehXPNQG0plEDZlXrSBhC2qobZeMl8N-U766Lgwav5BG98j2OLrrzeSqzG4xaGAJsWht4O0FrXqUR_uOwpGJaajKMdGA-F4aH-bSq4_95OoZVRGNRogL7xIAej3xEKYVn_U9KkbHqPF45KR3V6C3Cy3XxMifdmXIZA0-kKNqvv6bIPou_3UN3snf6nmKem_WPQyf6wCiVzF0xENk9SGayMycN4zxo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
تتوی گابریل ماگالایش از جام پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102972" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWNRZow_fsA-IW4H6pjFzLHHXwQnuKMJS81MEDAh8WQNNL64_RmGkeFhSnIR3yjCk9jgl5d077NYR4bE4uQg0vVYaOntoNzWYvnUQq76zY-SFwBcnsyQ3tXv3bmA6i5N2mx16xqSGjDMgFBXF6UniDAGvSSRYrD1x7H95zkx2Vq1AnXkRxHmQy2oLIWhQbU4TBBKt3tEFfVzEGn734znUmrxrUYaew-xboWQ2Ktw_ivq6OkXKjiegjg8baJcYQ6w_Zd4BhkdIH1F918ZaukSbBBr30UTrZ5HUrRetvN3kG4oqCfK46AK-tgaK67cMgZdM5ZfnLt-WrRiUa5q9kCGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔵
دی‌مارتزیو:
اولین انتخاب مارسکا برای پر کردن جای رودری، انزو فرناندزه. سرمربی سیتی میخواد دوباره با هافبک آرژانتینی چلسی کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102971" target="_blank">📅 13:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102970">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvjxk8gMvOyRH_q8ikdASt1k9C9HeQunytA9Efn40Gl3q1I5-utzsa8mlI3d8yrfM9eVlkeDK4unQfL1rdy20SMHbxrsRPDqvP9GYISsMPpwZG_0L2meRrLrgox5wvMZcIm_j91ISLPL-WgvvPUZ19v_AL5CzIiXKo_rmavC9Xtc6LPdMeqtrdwSbx2KBmOKZhxM1j2FewJ1humtjF07UCG2uLeSXDPYTx7LAMd64qDfrYoJyPuOYhOhtjRn07IzrQi6nP8x_t9vwtRRhdlyncKXug_-HD0o5eMTMjKvanCpURwhFYTmd_EiED9YWnZHAhAKKRg9Wqv0DadtPJBt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
بایندر سنگربان منچستریونایتد با عقد قراردادی قرضی راهی سلتاویگو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102970" target="_blank">📅 13:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXcM-eXQI9GEDAeN2TJBr0HwG_IRxBHbFm61u_3zVkIgvZirpixMO_STE8t0dcvx2AXuZloU0xFTRaKrzklmQzcRjvSGmE824XFGjzHVPbjU46HtrDhbV6b9jpuPqnfz_ZR5L4LsAKtCR_dHEZvhX_rjsiDbeyf9dGvQ4tK9yJlpyMpT518XKZ5AhNmbmUBnIw8JXQlJJJzwm4xq298tyiMO0bH7pLefzWy2SRnlWpHuxjf7CU8aEPZgWF8s44pZ-PQNjcrBMJrypSbhJE8JYr6a47Vb194GAF3zceEyXsxRGKjC1HamPIXUYmhPgH2ScRPdvuTaJYxiw6xy4f5sbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇹🇷
🇪🇸
#فوووووری
از آلفردو مارتینز: مسابقات سوپرکاپ اسپانیا در هفته اول فوریه ۲۰۲۷ به میزبانی استانبول برگزار میشه و برخلاف دوره‌های قبل، این‌بار خبری از برگزاری مسابقات در عربستان نخواهد بود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102969" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102968" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIOwFq6jLMqx8xZkobvRG_GdEaCdcHkDkJiDj9rL2dr95yw_a_DIAkcXcIZpe-DXlxpyIZpB7ciWq31RLvcBg25gWVY2GqtQ3X5_FvmCq_Pf4RApP0e1l7JaZbpj1KlG2sbQ7oeyUQZ4J8fnyfATXKJMuuiPHkn42oKVIu4Bh4R5g-8SQkMOYratvkDccfjlPmitdwZ9ZTth7a0nSKowIsnluoEFzbQQMtEsrvvAe4pQLq2y0f6YqOalDPkLSz3rEMNqKrarWWJ7yOL1_yX99gJJuVYLOweaPK2LzrYbEVidbT3WgjmqCTDgqIviO1MbQjmx32n3xb9F-aFU1KLn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102967" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSsaqQzO1ByHW4WN7G2VsS6Cc1ofx71xpTSXxEepk1baciG7TaCPJ2gJnilzHRB2RDjdGk_MRskuFHN0MYdEUG4NXuWvvm9bA1gooqAHfjsc-8DZkUKf-4_w64bdNrCTxgcp-I2Np6zvSMDqmsUzBjrdx1OtCBKlRVKaJqfpuHAC1-XdYjeVnfl7hKCq34CvmduPpUQDSX9hTV5L8uz7KDdgBfpykPvDUpWs_wwHWYMi9qGJpaGfnRzPuIoY4ezz10wDC3b9w4_tNFAqQf-aVPYwXFlucwhJiAKQb2YGNUaX17RXkl3hzJIr7aFPtSBbWG_tLD2kTT0NPYOKDXANAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXazBTkSSx9PxSCur3H5Vq9snEucFC2Rmnb3c8CbjKgWy4u9ZgZroAPfiG1R2C7mizWduclLxMlLZHpIgyKwFkpgbRRoAkGjfseQLEBP7tP4kSiPN-m4oABWfuc_WBkgx235Pkk-9W8fF-eKwuJ3IA8C-JREFSRYhaOhgdC7PrOWSys9JNHD5dEHrBnPvTtxuNFCmtZHEnOBnGwlseCI_4OGy2ghwv_l_nsWndNSwsQgBzgurEJbazb-8LN5L5elLFSqB6ZwUaq9kkFsK9Ydl_NOwyHPx_0wQTdJz2HkkK4fhIKN1Gzn_mEEENlbkDAY54W2nyOTLJ4zge-jFDxXYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الکلاسیکو فصل بعد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102965" target="_blank">📅 12:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcmlqKSgo6u0yYwYEFoNMpTuShMv2WLK_6VL8GWG4QBDUvvaCP8jHTHA-7WZJ5TklrgIgKxKuE-UfXWp9mRJWNe7HPFydxHnnBGBlwoGj9vMOzNR6hTPCI6YEzks4oR4Fja2csMGcs0o768JvDDyrhsn99RROsaf2l3Sn3vDwnodBDv3A0vutLrRcvyn6UllGmjHMlZH4jBfC8ZVVDZQEabegTyhTo0YdivFKYNTynCMcNJuREXEkgwr1JwPGSLJDl2ELemA_9239m0NHmK-731j75oWo-woxtCEDVwpalBsJwXfMp_2_-Ki_ips_rgjJc5_iAQ2t0Mi5G61WDjMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxOqWSCGajvsXHgYuEnOTtnCyvskb0MuGGnO7lSw1NhJtWUqFo7RR7RbD9WFlaA_kppScJqNBQDRWNbhBZfx32zA2hKQN5lR-PTQOifx8CJ6Eeey04zz34dnBm3kTTwG-5ytSbw29Q6MljyO51ds70rQSxrf5pjFojykDQD28vzECDv5KJ_nvD0wVXKLQcE7QUjnnhZThI_g5t1ENNTIiMm7Su9cTUYUAkSNZjUjl5pjPh5iE0KZuMBvHlQUe7f3DHJcsUYsnqbOW6o3QusxtAm4VxZnAZ7RITmpQOrsk6wJds_PaHzPIAUYAfS3MR1NosXtvEUdmC801FlLaHGeqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
⚪️
تونی کروس:
اگه کریستیانو رونالدو هیچ‌وقت از رئال مادرید نمی‌رفت، پنج بار پشت سر هم قهرمان لیگ قهرمانان اروپا می‌شدیم. واقعا هیچ تیمی حریفمون نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102963" target="_blank">📅 12:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دوتا سرباز روسیه‌ای با چوب تونستن پهپاد انتحاری اوکراین رو منهدم کنن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102962" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqaV5u9zu8OzRtdHo7AArEIOuWXsqTVreFbxauuVQZJkcqf-4h50H5Tq4nO7_iBzVwHtis4Ad5ywaiaHcx05t14nqlUm0qPiiL3a3RBAx0f77w6s9azFD-9ww4dLgU-wAw8mKBU2AysTge4pFzqYIv8kQo9fGXyiIFbIebVvzjxmGYZPO54LoWryg_VKP2gPzDW4bpzNuu3zZyS2X3ivAY1RuCZRJGzBoduBCkROvNygm1b_V43qLxDAEaCS_Fy08cYkQwCKYj67tbeMX7fCvt9xzNPuBlWT7JU1M9pwGCPnINng6Xa4SzmvRJx8N1cbGGouDQGyTSRM49y-UEbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت پاداش قهرمانی تو سری آ و پاداش صعود به لیگ برتر انگلیس.
💵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102961" target="_blank">📅 12:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSoU-8JvDgNsUtJ_ML8VGcLB5so8v9Ln6BURvJfdrXNrxIQUsNyqvUNDAXhv1_mQaQ6MbkQOcG2jgUNyd6tmZCzEJX4AlMf98NgBDWVqBL0IBh5CdZogT1D-FLnCcWRHDvGBZhzQfLLBqw01Af9Ieyiq9YPe2lGD9yfyPzrvt1-3PdG28TMW8p31rnGVdfxTfa7fdzrdmKAlfk3cMn54xme3W8DG_M19dHi9AgzSAdUevBn1j0AP4H7Awz69gRtSEh-bcW0VZv5iDXEIljVEgEP0AgZJajinMpHN8MwT-vduPO5fXQEQxhBEOvbcZkDm7mIvlvmj6NcSogdPpJBTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار اگه تو فوتبال به جایی که حقش بود نرسید ولی زندگیو برده‌...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102960" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
👀
یک زن ۹۷ ساله بریتانیایی با ایستادن روی بال هواپیما، بار دیگر نام خود را در کتاب رکوردهای جهانی گینس ثبت کرد. بتی برومج که پیش از این نیز عنوان مسن‌ترین بال‌پیمای زن جهان را در اختیار داشت، با این اقدام شجاعانه موفق شد رکورد قبلی خود را ارتقا دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102959" target="_blank">📅 12:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇪🇸
بارساییا بهش Welcome بگن یا زوده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102958" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZLkEu0XgxogEOqQtm-Nguk1KzZq3bN3_PRTynqJimGkSBaU6El5ureJE5D_eFa7TKPAW2WIW-aaEMc9gn7gap6ahhHt3MWyV9RwPsoYpP7JzLlsosXIIjVjczXw_5qqPSQDx2SPZDQM7JTo_0LXCxfHSf_tWqn6HWlx7vUTLxU5hWWgOzqS-IhV3TfogwCzXCl1v0LUQKWD3ddln01V6IEyDOsMiJ3O0MkoVyhzx6V4EnxvSIOQ2Ce-t8itGd49_Rb4wNY854mdSf6aDHiUSDceWsukATCZr-eLKtHTW7nSbVyDCGMjHsu5-PFQn48Hn88Y5Y190bp3uILx5syRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUZcYRn7hCiktplYpcWNEqj5hhvFYUXT6G7ccCH9b2AxQYDF3v3RHPEP5KTmc7vr-A00BNMOHpYajCbOP2ZZa8ZO7knA_4O7NT7czVMmETy9rjepX5UUAoLVOPlA7FNoah1KwOP-qpTJ6XWfY-YLCyd25ii7KiPFTH7FS8Ll5UG8aLtIPTymQFVFkLfv5VGdADmD6r3ZrRw9ceCxg2FmpnCs5OU0ISGmyYaarE4O2da_HoFAvqi_DlBUp646eBFDYLt7oavUxdk1RCIFgwC9uy2pUt-m9eGrtYL4jpNvlihkCUPd2sjk0aAHl0vVf7VeTEcf1iCcJ-FEY9wphiSLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
از کیت سوم و خوشگل میلان رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102956" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIsbltTz0ZE6YT0c9b-HuwTcC2nX5v5Q5UdNtd6OFhgH-h7_bLTryRQ10Ij0nwZBGrnGoO8Wsxo-j-eB9gzC52V9dgnGQo0vD3DgblsapzRBySHUBnAK3w5W5r25Ek87H8R4o_aSL5dp2LabRgeF5qspJx9dEWUIDrWhOYOvT6h5PRrwUe5Vc-fuZgUk8kPFMUuQ18CGiIZlmCnUH1Rfv536B9Ax3azxBWg9XpZ-ZIIw8cJluduHnljKIYgJiKaGqg44JtwE8eWh_g_HkDZKkN-fIpWTsuxuAULKYV4G3n7_eeNT8KCCWrpGLU8p8SB1TTEDicNfVdDzJ1Mn08f4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6PuFiuBl6zcNPeANGFrFm2N2XxfAiPOxbgpwRJfJRO_uKR2chYfon6WP9Kj8dHzj-C-PyrUVLyum3bHWAyyky_soUn-kwGcxsC85Gmlw4vgVDqutS7UGWwDVMiGZUIRaCV26zKgz6vYBTcjHiu_No90iEqs9xaCp1m5mqin6w1td_HgQueIl56jC4rNZkeh7bBjSHD4UebLIOG4J7YBUN96EM-l5uRKw9U6NEY6CpBRcv3zOqM540kUwQ77PToyOaH6-7BjYp4pytxVZ66UGgfa9IHXolBCZxIoW3vUgR9iB9tgko2DQpRl_OInGNpNyXgVrJqPkqKTZQQlh2sgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuYEVpJ3n07y83NXJfe47s8cTQWquWija3As7suItLwAewFAWttmg8z0gjgcSzJhug881UTkbN3f1pgW6bJArCOqQR4i4DON4zvEdoxXeKs9Zd38eP-cadOujOdnbJMS1hIQ0zqdrRy2p9IMJZnrgbh2BGsZ-cXzWHPEoJ21tdsSLf8bRShpIiVKf3rtf7zr3778M-WC8olvG9wG-Sk1zw3wYkr0dEpIOYHBZASSBpMuvXq-TRmhPbbj4aiONPahRK1UA7W3Z4GPd-bzqRjMNaMwlPlesjyc4_m6QHsu72tpV6UIwftJWiDbQWOdH4KzL_6dEK-XnkGgmSP4imZTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USCUHjqwtvlefgwzP0WpK-dpvl6iwesm327r5IR8z8H04JrkIbRwU-KtHK4vhW-gaWMWerijZWsUm5PFXCcREHMnOV3reuheGm7rXifpnmDyZvYyjaKXlgnAHLXIuGZRxlxjW5airnnC21p85QMFMfeEG5K__qlXPyxLknIRsK11kCtKVpGbI4psRQvz-DUlg6406FGy5okfw_pxl_DMudDvtxlrj-XaMfBxCG6erWTW9ILHYgD6nNiqkJF9u6Tky_TY_BANE_h8HoYVH_wvXh-yQR7CUX876Uio_cKcPGBMetvcUcI2SpxB8xDOeoQA64_nUbnnbRk2k3kHbbzGxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
کیت سوم زیبای یوونتوس در فصل ۲۷-۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102952" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زیباترین گل‌های لیونل‌مسی‌که برنده پوشکاش نشدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102951" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
یک ورزشکار دبیرستانی در آمریکا در آخرین مانع مسابقه دوومیدانی زمین خورد اما سپس با یک حرکت شگفت‌انگیز به خط پایان رسید!
🤯
🏃‍♀️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102950" target="_blank">📅 11:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔝
▶️
عبدالله موحد کسی که واژه‌ی پهلوان بسیار برازنده‌ی او بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102949" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nj5eYo-r_khJrLuxUDLMpaekCbaq-t1NPR7m86YE_oPOryQ3iBjLj2B-6uGl9oVX5ioXv81eiiHfO1bB7VxkKxwHVtizemm8bmdHeUn7tySe8J_zHFKzKGY60-19WgGvp2b6Dqc3wBIOOBK1O3d33d3vZqw_6A23fuSrm1vqE-AbbJOe5Pqho7sCBvaUCQy77yP_k6S5LW1DrbQc2XFkIN88Ez4ql42zeDbf2QZ4jEA4LVhFx9Cb9_X_waNMReRqqsbn_O4-WZR7EBzt1JOgKZWODJmaxZ1enoQ0OD0ExPo-YPVg0BrBDSBrUEqy6vTdyjV_VwHSieTXTRNZSJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
قرارداد رودری با بارسلونا پس از توافق با شرایط شخصی تا سال 2030 اعتبار دارد.
دستمزد رودری 15 میلیون یورو خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102948" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات کیه‌لینی از طرز دفاع ایتالیایی
🇮🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102947" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=EEMtIO3w0GEeoguJoQEYg1cLDbHe57aaCV-7o5iXQsBtgfEYXNY1Mz2klne4_nHyDdElqLBNohTOVZo_a1LD57TyF_HUH3P6FB89ZvwGqDxAQjAuq71jzwwgtK2UL6JM80aBWRm6zzpUPgoDMyZdJLItFjedYm8tLc8Vo4M_Ky_wTVAHxRDnkqHcJtVF6JuE8z5Q5usAIaqOvFpmmdMOQcKE9ofTpv-lkx6X6-mH5tWnFeGJYWpnVV7XrxAV12sXy3bITuT9XNOL1jmzp8g4VkPmJPnNNN2dCOQg9zNmC8q4JHWsw04mlDbSj4iWFHahk0ErT-cf2--CiZsJpIB0ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=EEMtIO3w0GEeoguJoQEYg1cLDbHe57aaCV-7o5iXQsBtgfEYXNY1Mz2klne4_nHyDdElqLBNohTOVZo_a1LD57TyF_HUH3P6FB89ZvwGqDxAQjAuq71jzwwgtK2UL6JM80aBWRm6zzpUPgoDMyZdJLItFjedYm8tLc8Vo4M_Ky_wTVAHxRDnkqHcJtVF6JuE8z5Q5usAIaqOvFpmmdMOQcKE9ofTpv-lkx6X6-mH5tWnFeGJYWpnVV7XrxAV12sXy3bITuT9XNOL1jmzp8g4VkPmJPnNNN2dCOQg9zNmC8q4JHWsw04mlDbSj4iWFHahk0ErT-cf2--CiZsJpIB0ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
جوری که رودری تیم جدیدشو انتخاب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102946" target="_blank">📅 09:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=e-hzSpHcu2RytFqNgldlJhzefbkQBkGMbnmBkSfkd5Pz6HeJtDtxRWSbaQPKFIQtRWAoomPpKsXBNTovZiginZKrBk_pHBdMsz0kWwMoURYfxTswO6WKLpV9vnSOpJwtVLpG9s72ybyxIJK1z6H5ategELWQRfEws3aaZDGour9jiIiT_aRIS8drBI76YbEybA7j0OOYTkdGnmIAiejUYrBc2y0jjnE3obfRxBlUfIY-DQ5MgI2QVfsPiI1nRWkkuqYO1kwfBIyweiuhajtJS0Au544o3xfoI1XYugVGakd09mlg8ejPzJigc4-F65omgrjgF0_IlNazk_ijl1qqNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=e-hzSpHcu2RytFqNgldlJhzefbkQBkGMbnmBkSfkd5Pz6HeJtDtxRWSbaQPKFIQtRWAoomPpKsXBNTovZiginZKrBk_pHBdMsz0kWwMoURYfxTswO6WKLpV9vnSOpJwtVLpG9s72ybyxIJK1z6H5ategELWQRfEws3aaZDGour9jiIiT_aRIS8drBI76YbEybA7j0OOYTkdGnmIAiejUYrBc2y0jjnE3obfRxBlUfIY-DQ5MgI2QVfsPiI1nRWkkuqYO1kwfBIyweiuhajtJS0Au544o3xfoI1XYugVGakd09mlg8ejPzJigc4-F65omgrjgF0_IlNazk_ijl1qqNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بهترين آسيايى تاريخ فوتبال؟
👀
يكى از آندرريتد ترين بازيكنايي كه ديدم. با اين که هميشه تاتنهام رو دوست داشتم ولى سون و حتى كين حيف شدن و اون طوری كه بايد ديده نشدن
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102945" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCAjK_4DkY39ayJyiq8vgzWIAzbcuQdtfCwPnt4qxsMBOeSGGYGAa-yk4cwFBdl5bw4uvnLdXoL6GloRbHKfpKQJRamlF_6trnl6HCl7oXlfK5UqAoUl6Z3Wz8RcbfZtXY_K2SWEwMYbo2paonwGKLRnWUISM-JrVhlERqg5Tbhaqzczr3cFw2QJP4i_q1Gz7P_49egtyBd8oMSPcn97HibigOnlFRfTf7vXdSiPrF-kW1ymaSzYdFiUOKyMoCVIm_H4zSGHzWjwT-aE9h952KRPtjZNH--RQLbpHI9dEvu7gLW0DZSCSh1OXqlFX5UUzjcAJfdlW4cSADu6tcjVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پله اسطوره برزیل، در 4 بازی بجای دروازه بان بازی کرد. تو اون سالها اگه گلر مصدوم یا اخراج می‌شد اجازه تعویض داده نمیشد و یه بازیکن تو زمین باید جاشو می‌گرفت. این اتفاق چهار بار برای اسطوره فقید برزیلی ها افتاد و تو هیچ بازی گل نخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102944" target="_blank">📅 09:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=l98lRUdjZc8VbUC9y8zoya9LvMw1twRgZYfqrzKbBOj6MX6LuBeuiIGp1tAEw7R5CI12y8AJze_8wsoXSH0ZiraAXQaToiXfxbWowP63VUg6xl-_l3Ye2kAH8PZXV9s5Gv6xM4r4pypXQd4Ssn3Yis0Qu7aHJ0SYmatFS-8W6lSYmR1dBxXPR6CBhnwetoyHv6bMYXcl5sstnVvgM2s2YpU9PwBMEKJ7mpNnde5nOmzkbSWY3tPMMi9ojJJhHAavMhg-DJGI-S7GYqHLyC3THo_ss7zvm6YRWk20_PBXqRTbR4aS763FmNBtKM9Qv0yAUtxbSxc7mTMlREGkcJ7Y3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=l98lRUdjZc8VbUC9y8zoya9LvMw1twRgZYfqrzKbBOj6MX6LuBeuiIGp1tAEw7R5CI12y8AJze_8wsoXSH0ZiraAXQaToiXfxbWowP63VUg6xl-_l3Ye2kAH8PZXV9s5Gv6xM4r4pypXQd4Ssn3Yis0Qu7aHJ0SYmatFS-8W6lSYmR1dBxXPR6CBhnwetoyHv6bMYXcl5sstnVvgM2s2YpU9PwBMEKJ7mpNnde5nOmzkbSWY3tPMMi9ojJJhHAavMhg-DJGI-S7GYqHLyC3THo_ss7zvm6YRWk20_PBXqRTbR4aS763FmNBtKM9Qv0yAUtxbSxc7mTMlREGkcJ7Y3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇹🇷
محمد صلاح در مراسم معارفه امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102943" target="_blank">📅 02:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCHXY5S94lxjbQXoXboDPLsECw-tTGzsyWA8j6ak9hbVoxgYtH9k8-KSw3aJk0LYZCppdsZljZPp_8y5VLe8o-MKlzQZW4wrQ5Ny3S7EvKJfU1Q1Bq8XSP0jgJKGtfA03eu6wBI_pMYwZigs6FS_apZ1VlE3OT1IHodbw6rF5PVrMuphu7YvVf9mMBLqBfNSPCVqiWUiAszNE3AbEdlpB_MgMJICbHUmewqBoaikentzT25exXZ_6at4GZUdoR8DAU_k2a0gkVh2K3hHETdSBdfvr9O4h8eROz-eOTZebfYFMtmf4mY6i2MYOjCC5bKW6LDvztbQWNUeLdHTDnDdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
فوووووری از فابریزیو رومانو: توافق بین رودری و باشگاه بارسلونا بر سر شرایط شخصی صورت گرفت. مذاکرات بین بارسلونا و منچسترسیتی به زودی آغاز خواهد شد تا این انتقال در سریع‌ترین زمان ممکن نهایی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102942" target="_blank">📅 02:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbSSfO2QzwoAXTwnqBckgQqPRPSzV61_AG8dRPbszZ1LWjULOxxwcfFQAXxv5_W-avkuJk-zEyowAUQI12Ad0ZfraJiRo0XW_VuXjynsBB5FJ-dzV-ZImLqv7IPDpNTc3miSw6cpURxsyCgmcje5eAms7gw0UZ8xevnDJ1GYIvv1bbUw4BFDzG7exs1OtNc8blUHQdCXHsZhjd8xwq-1Jv4OHWCwLFBPznF3sP5FPnU7Oam9whX7tiPYcGqSCyt61wi7RFhnC9eXWDhH6N55_Gg1usqw9P_bwpclvrv57Hg077zqgbDoiUF90Ac8MSZ35TPIICpkMhE8nzWM2OmUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
⚽️
رومانو: ناپولی بدنبال عقد قرارداد با گابریل ژسوس هست اما آرسنال این بازیکن رو قرضی نمیده و میخواد با دریافت پول به صورت قطعی بفروشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102941" target="_blank">📅 01:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=ML4kDGSPIkC62YXATVvH724M9S5B7ZLLMaktIbsqm2hz7GS5acAGlsbP95M8akJkPA5LF3JRQtnKsevQsy2m99V0suyDDowZVjl_Apk6U7yUyP2Ga5YNLh3dhQMlr68ad2Ym0iLY9rbtdvh1AK6RbEjZ_NpiCOcYqbNNOqhjRyKvWIsECTQdExIN8Ec8ve6W0FOHfWX0kv8DD12cFW2wL3iY3tH6VZ6KB2KTLi0KB4suONYLIbH5q9_1vm3TCGbDUlbOzkoU9HlzvNaEvHamBjYP_Xs8JeIjDwX02fiU8nIuOxzjqwZtqYK8mfqZMKSpdjSjM8DC9B89dFLHK_PB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=ML4kDGSPIkC62YXATVvH724M9S5B7ZLLMaktIbsqm2hz7GS5acAGlsbP95M8akJkPA5LF3JRQtnKsevQsy2m99V0suyDDowZVjl_Apk6U7yUyP2Ga5YNLh3dhQMlr68ad2Ym0iLY9rbtdvh1AK6RbEjZ_NpiCOcYqbNNOqhjRyKvWIsECTQdExIN8Ec8ve6W0FOHfWX0kv8DD12cFW2wL3iY3tH6VZ6KB2KTLi0KB4suONYLIbH5q9_1vm3TCGbDUlbOzkoU9HlzvNaEvHamBjYP_Xs8JeIjDwX02fiU8nIuOxzjqwZtqYK8mfqZMKSpdjSjM8DC9B89dFLHK_PB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کل‌کل پرزیدنت پزشکیان و مجری برنامه :)
پزشکیان:ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟ :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102940" target="_blank">📅 01:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=pTZ2Dr4ZTlHdab-DhXHahluUtvDVc0rX8ax8U8Z7wwSuiCQKG8Y4yCSETpcOSS1sntFr97Wr7u8-x0sFBViZkAJ3Nq8URGdix8RWDIy-oX9poACtV0dbtXdR8y69HfbG_6XlCQJNp-kg_ugv2_QaycgODoif3ofVpHEPvXdt2qilyfmW72IRuvT0gTN5wKsIyBQbEOhT9Qta7T0MQimm5V4_yg-Kyt-qzgNV88piqzLaFvCMfoHKnlXurhNoII8MksOMV9Ypl7vHRJiz1mBVBnZJFU3AawLrbVi37tDpWhOn2m-R-eOGGPXwdUSwGP9wKF1iBCy2Hwr0XFeVnCpnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=pTZ2Dr4ZTlHdab-DhXHahluUtvDVc0rX8ax8U8Z7wwSuiCQKG8Y4yCSETpcOSS1sntFr97Wr7u8-x0sFBViZkAJ3Nq8URGdix8RWDIy-oX9poACtV0dbtXdR8y69HfbG_6XlCQJNp-kg_ugv2_QaycgODoif3ofVpHEPvXdt2qilyfmW72IRuvT0gTN5wKsIyBQbEOhT9Qta7T0MQimm5V4_yg-Kyt-qzgNV88piqzLaFvCMfoHKnlXurhNoII8MksOMV9Ypl7vHRJiz1mBVBnZJFU3AawLrbVi37tDpWhOn2m-R-eOGGPXwdUSwGP9wKF1iBCy2Hwr0XFeVnCpnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
جو پرشور هواداران فیورنتینا در استقبال از ماستانتانو ستاره جدید این‌تیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102939" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra @Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102938" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KoDBuZjP3pNoYsNFAs8wTzs3moFIPDjfJUjvgDoq80Ase1kcHRr5ygLb1CmYgqGiP7GUzTzBfxTo_hR3VKdm-RAKLCc84Trvei4iMbryRtnLWqvoQxhEJv29I2hXVmT0maWvp1S29eNZK19RrcwJP4rltDPstuM2FjSW-m2JPfGwtc0SRD7abXHLoqOwAE2HYdORsAqcAJJeWoUBM9GWlUz0hxZakBajDHKOI1yxzijwARa8J1GAriiDI0JSQ0UIxrq1Wz-_DzJr5lHJMY1bcgGqeLuK7q8jmApto3AmexRnyjC3ulxc9e6EXCmYFTNuWk2ql4FgQ-AYdFP5Jnif4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra
@Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102937" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFYcRiySjOyR138VMmn3aymfs_yJzqJBUq1DXV9BwPAsRP7783cfLDnnLpKgprxiRoBtH6LqLx4LnrWUTtg1m9IF5Splz5LIaP8694KqC3gv-ffyifYrJYdY1p2G_bLIErSEGAgAWlIuC-EeS6nmrjXXEQTmJQnukRSOb5L3ZxVanssUq6g7KGT1r2AOvHwTUsuijPipb294mqYTQOoYpOPorMAefwngswvYRtrju1vIl6bOG1ulG3VmcS3MOGPSLsQsNmiJu9nMfDZPyGtXUhXKH5rwgQfOOlc4XSgBmTPejmppxO5yeVwvJIPMGphhPdUwvIuvoVaQM6ROvdfHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
پپ چاواریا از رایو وایکانو به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102936" target="_blank">📅 00:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxdIe4TBx6dBQNEcUpDUb58felXAN5wYxJQk1lUk5tp1NtXwQc-xliXzJxceMmzZsr1AWiZ5_dPegVHJodLox-J7IPY5IARgnD8gD_wKZ6P5wkl1OeUAkyfXewQUchneryCINO64D5K3ULVw11FpI0Ch7NRkkfCvn1mn8D-qrOCm-O3nV1h3toWHdvVWxpkgA3owSpLgkBugrgaIDm4WxmAuNusAD0BgEG_Ux-QiwFpX8S1JGBcjd35RkvE53sd1SJrsCH-nTyjQV3WELn13SdGQ_uXG9SV2TRKMB2ct_mMX5wuqTids_Ofp_QdrEa45W1qy_DpZremJNMqd9PzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
📰
فابریزیو رومانو:
🔺
رئال مادرید هفته پیش اوکی داده بود که حاضره ۵۰ میلیون یورو واسه رودری بده، اما سیگنال‌هایی که الان از سمت رئال میاد نشون می‌ده اونا رودری رو دیگه دور از دسترس می‌بینن! چون رودری چراغ سبز رو به بارسلونا داده، برای اولين بار درها رو به روی بارسا باز کرده و حتی با هانسی فلیک و دکو حرف زده. دکو داره سخت تلاش می‌کنه تا این انتقال جفت‌وجور بشه و الان همه‌چی آماده‌ست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102935" target="_blank">📅 00:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke2vGng2HTTtte5uAnhPn1DrVxcR8ezaW6g8EWDlMlggtV7KLcv8gFQ8MqY83FKzfJRrUvxYxTSgRP62W89tMcVvEVLZgSXPIpPNB90XQDNenGUziCTsuSwxfnLSfoohwexoeYJBFUjx2WuGnrvzd5fxhlxeaQ3sAxf7Gkg1UeC5hOOetN9Ms5GuIRCEAHo4DelPq7neUCTQKVEy-O5gLYbQxVNtqbbq08hq0AwVoAR61QJ-2yJrfoHOaC6dU42S4wEMqPWarNWFZtM4jcgFdv-TZAh_y0N5oMkekWw2njzeydCBkXj_IhR76ntGH0PUN-goksL6UtQum_CZxj0yLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ورونیکا بروناتی: کریستین رومرو ستاره خط‌دفاع آرژانتین در آستانه توافق و حضور در اتلتیکومادرید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102934" target="_blank">📅 00:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uebT75nNqGY-Zz6-tke1LUAb--CWJXd5IaSOnf94vtWBAHBgAXztjWhh8wE0fYjoN4-FaDozbDv0GguRIrjGYYKNMBo1yUp7B59yVXkjBCxZYzzW45Yc0UFqC7PAMds26rOrKfh51Oz-EiVqhO5xuw-F_c4r8vma7zxU89u3n2TOcXyDaEs0PUj6Zfb5MQlBRT-n6fIMrVKo2_uqV6dfxUMfsD3OMrDBOsh8-9LkcMRJumKoC-8ha1LFzFmCoDKk2Y4FwwHI73D7KvwuKwIUSm73gCNZk3bFV85CiLFKH4YQLPQ1z_hCqsDPwaKuM882yY4JYume1MN2U4asiaOF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
گاستون‌ایدول خبرنگار مطرح آرژانتین: آلوارز هفته‌آینده به تمرینات اتلتیکو برمیگرده و خبری از اعتصاب نیست. اتلتیکو هرگز این بازیکن رو برای فروش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102933" target="_blank">📅 00:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102930">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkrS8LVzKQTp5P4m4q4GWjPHY3YB6Um6MCZEg8ys129ziBZGrfJEY-zy4VJUf13Cb0JpFn4SwLJMS7rzi8y0wioPyiE70eOi7281kb4Kn2M4fiRyOEgQTg-jjCglh3ZLH5I8-QAhQMssThLUivuwNqLZJLyyPEME2vQuS2VI2l9N2JFSXt9CxgVxKVuPFh9RzmVbPlk1bNBPX9HlBno7eNqBlth65N90uiCgVFx1MEDhUg4otG84AW92h83jPPHH3v-VCz1BS38KIqEZI5ZtQTM0Ee328i1o85CVEkhwdyGWw1mu8ZBdm_JRmwFBF8mARd7FT_a4c7QZMHTQQnIErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
باشگاه هایی که بیشترین هزینه رو تو فصل 2026/27 داشتن؛ طبق معمول چلسی در صدر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102930" target="_blank">📅 23:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6oscbMimDp4ztht4ItK_pImMXVHnAe3vs-w0YR9MjsLIYSpc77RcrLxlvlYQtESh6-o2iio3utJglFGXzgfN7Dv7KFxgpU1dDZomU9hMuqW-2t_s6fyyZt-YkCMnGupqs-I22Tyjat9I3StfFLgCAeK9ZXIejR_ImgVF4a1Lz06FiJjZel0c8ScaAYmpBjeArGmMhc1Fp4_GM8BCQpwuzLUIRvyP4V-7TN3lQ-2UDrIyXN6j2AIv2bXr121fm5QYUCt0Cop6QfjOIx7x2uD8QHbC1ymyizep3OkI74p0-9nRw5Qh448eSnaGDb2EALtxucD1rpTDIsMfXIwqXikwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ال ناسیونال: تیاگو مسی از همین نوامبر به لاماسیا اضافه میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102929" target="_blank">📅 23:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_IbMOjfYKgxVph4VkPO4KsgoAuvVyEjft_OSBx4nF4fm-qH36E2knXefFETPdAfRWhzUg_Cx0FZdMqEj7fj1Bm498vPy7X8bVTTcTCfuhuJrclRpOIoQs60eQNxSITzr5nhvBcqxwutY7QjtRFwBBdh7lbBq1Dx1Tf4zm8wOTLFxvRhMktQgET9cqrNzOFSXL4hU6N5PdA6bamBGx75FbNmxWOHmyJY4RHN9qZ0gFpM-Y0HAoCnd7RqYrlVt_XHXaqAAyZ5oDekfAFE78BsHS7mE_gH4n4d52hFQVkNzfh9gZDQQBH7Iy3YisShm87LfSB40S5RbtYdsYg0O9AXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف تو آرایشگاه داره موهاشو کوتاه میکنه بعد جرارد رومرو بنگی زنگ زده ازش در مورد رودری سوال میپرسه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102928" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
