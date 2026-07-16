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
<img src="https://cdn4.telesco.pe/file/mhddfIF3UZKE9MMdSea_W9XeWiN2X-PfYZhxvkIO5zXSVO0j1dOYskuhDb0HvGT6H_pXNGgNHXup8ueXqzWKJQ1eHL2Krx4VP6bjyjXIsMIuRw9fAjnwGYgQGcRLX81TlsJ75MS84c87V_-_rDfhcC0KLfLg-QSlotV7z8El8LuyXhnxM7QI9_XLHs155cLAD-dwZlKby8bV6DxTAm_cTuuGekOe4f1qbk88rejd-vwh6p4Tv7yZ8_YzbxUrGZ1WY2Wps145AhpkBs2xUr_CQcVQl4g3VCtMMrjMBJ9quHNIzkwzgpF4QjDQBq27NJpqpaYnzBkCCGh0Fxy8MBgrvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 513K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1IULus141wSHgXIgC-tYRosmDCCwIMaXqsvn7V_ii1LxU0IGrxdjCTq-f8-BTBb6fidt3HTz7vyqAhq_8YV3ZPUrVCVnfpWnrAbVLzOArqo-3n_DB8ah8nQTG49fGoRXxV7-AlT41g1exY3lEieItfqu2kMs58MdoUFDBQw4HCNvw8jEjC6I-yYDvvNWXjzErDLV0AU2xTzt0deX0RXjfM9scbyG4YtZSXjRSZ4jDhOlos--jhBPYL_RQcVIKVE3k1w-oJO0b6dnmmDWLmFLIEyHpGQJS528H9xlcHkny0aeNYnLAUXAZW6wDHLY-yNXsa75zjzgjAMU6qtE4vAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF52F6v7MPjLFZEnIFHIyQaYZ47YYdbelVpev4SLClFx-0oMFvnIheMP5F7_ORqmmsu5NbjEyCh6fx-1HKTq7_kuq5_4iMnSJ-LJUnhMmYLHKNDaZ9-VI2F22aeynrM8PTQ8WAm9uYoF2Ais1m3FQvoGfZpA_Aequ0DLTAV6ODQ-_98jceX35uTuRD5JJRW0UscxlbzF49OrbMkfHglF1xtIG6rVBaNtOWCmf3aVe_Qmr1lrMJJXEXHIgddJ1Wu1emZCtepgWj8L6AAZSce3CLADHxgisWFXYjxcBFrlWzuvc_BDpiVAMZc3foe3RISC7xmyQuQGePGaahPDJySIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKWegOwoJ4CXCU_tbjfYoXdjRwIJXC-t5SeEDfXthHvkHDfNgJcbZKVGiPRMLXXs7IEbLdfombzBhC0b4Chig34bpzSlC0sqiuGzr__BFr6r7V0nly_g24-YmX3La_If5qU_zafwIKIqTkW7DC7iv6GFBu5U7hyfr06b7ZsyAO2V1J81gVMGt3uQtVQnhrg91WLjlPa242_kZ2MnK7257bnsQBupTWsUAtCdfj_7CJjOocItVWtApeaOusX52FVKNtPUlUy3Yda-hM1EY7XSVy4Xp8RCITJgmAJfXgG9qrmZp-o-WjFtngu0OyHAb0MP0tl4ALF8mVhphnjwd-Vtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTTexaXUwQmActVJe3mYDNVRRlPdDESviz9N9cKZmNmS1_g5Ogdathg4LnwAfyP6RB1JNxiLwpbp5Lj5NWDCnsC5NUKqrIU_lBIIaZdmUlrQBwcS34-UmXqx5PvfjZ_qEbuzJpKHFUA8tAOCuMX8UzxXu1s3tExVnCnJTOS-basUlNwgmRxE5yLpzLxZ7lRA5AUFgL74_Uf4rT9RhGheyvtkPl6ptmyp1a_Hjc18mTHd_Q8CjAKPskqR956XRZlO3qzqeJWwD31t1nNXd9GrAMULldOtqpLwgXdpiaSM_kb1atS-krp0ud5HQ7iBV6q3oE_CjwTP82FZ3KW7xRQyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz4jLlajVE0Lm1qwN7bE2AOj_SmETswLgX5OhcycaM6Jdpvz5D-U1XbRrwOyt_uj3wgTZQJ32HhjrSOk0Sr5zdqIGrhRwrMLv4CJCDIfqgolGa-d9GpnaD0WxXuqaAn5g8ce3mUcWzQw94mstrMkVub3ayVXZ6jgovkM90_9Y6e_qSDuHnJooRtze_GoYwxr_-GfeZD7y1tpRaiP9FhhoAEVHInBFrhIfqY3wJFQDBAXl4X-0OXTQ5xJJ_tkt7d1nUfa2M4n_e6GRQ8AiQUerBx-I5RZZge6JHZE4d2K-42RdqlX353ckJQV2tsaTMs32jm2IA7WhZ3ewPWZ40ooYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlard4F-Xn_E8N2v_8xeaM4F1C5ISlyF-6a8vuXk7iIAF2k3k5K56F46i1sw592pUxBHkNPdBNCG8-FcWCVeHLQdKQGIU0KmS62cD67OW7ed0LiLbToIoAUZ3qHB-91ixY6prBzy-1WaT8wsSprpBJpLljUAt022KVAIR3vpE8XC2BcRSZ9KQxwBm2Dx09OjvnCk5cRUKxdsBPk5oLPUqsX5uz4Ge2m854mdr3kBg_ZaRyeJYNVwBQ88aKkZGIMEHbYEv20SDSlRWuhsFTvDM8t0E695ZujlX3nJX81fAEhDFNXifBnX-c-sGQwqgaogSKr9cuTgwQosl07McUEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBIUqCn7HQlP-up2dQ5125J3rkwF3b0alICRINxkAeLu0-KbbzNvzV51R_eh67D4F-WRKs4QSz4HVEZ9vy5cRVau18tkw8vChukmZZ4KeDRat7LJ5BMKKFFUeaESAHN2VoqnN-7wycUsOe218hsoKls_8nQOzaKry99SM8js5PE5SfLKLQxs0Pi-QPdEKD5RtLavPwFQbzSKEbXNtx1A1LtRAMU5GPrO6OOa8K7PFggY83eJzy4X1R660PmB2gQDMxM98NR2te9Q455YMAb7FioWjgwVi_mBr9Z8l4Zeqa6Y9FiUNv3Ajg0bLOHrao1MdzOnu0rYfwiqYtUNOlLtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw-0wEMO6p44o2rzBJhc0cValDcD-NwO9j6qaC_-sgxEAGfaQGdZMnkJO--o4b7J1d32lTYyiSZ1TssGDm5ukay1gKrQiNFlEcG7F2-PgSFIVGpDVqMtxqzXINgel4naz7f3H7cvTaR9fLmtGnyZzmOLgIsnknyuhvM5YOZQhd-Z6hKb2Nu2rdsBf6LT7q7Kk_dsOsKBFp8X4n2vaSSWiaCzOHe6qaVS0zJ6-NQtVhwC-lFKZDQ1H1BHced9q16ibiPUp3agVM24xCZYvGoxtxk7AOCXh4jdcHh-ljck3cFnEFmHoNMh0gN9O9rtg8iBbwXc_RP5StGD_qLV29bogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0qwlQJ4APseUIBTilNAHHYmuM1nVooCsWFvxV7z7X73UOxATSZWjT18DHOhN-NrJwew6fj6h-EoQ2R0KgGH5_AuCDEl13_KPnUsVA8PaY0xa07mp8XPfeRgGC4XT4OWg4PqMyU4uLvgnXfmCgu-OghdYt1Lt2bsLi5jSb72kfTCCRSF4qtPUI22qaxtQ076JGj34cbyYM5TuCXnEH182hFP1X2smXg_VS3aD3LcYsyCiKjnroL5oLULiRl4eTT60QCpJ2xiymxNY2Zw5r99RAvCwp5AxB3Bffp_hRGBokdkIcvyF_dG4mxSb1yfemWO_6K5F8DbOeBk7wgEKOZLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsvHhlDdalZDMgfuE_bfRKfS3o1mcELK5xabyI56KuV85hBNELOAYxyofkoYaYmblmNQPbWhUj73O2v3hWKkA3rqPW1WfriFszHYMZdQXxB3rg4oaDL-wUZZhlzbYoAyznLvdQeIfNp-zOzz1cvTYIVv5oNnLdMWlZzy0GOoXVItSyPbZsL7B-MDPeHcCS6wImuGWEaTtkfvSznlTlCIbbuY-8FcXHYeA9xoDG1Qy2tSGoIM6IpcovbQ428WlHeu6NLQiAv6GEG_6_sXCjFiBzTaE2kHRRmMdPWxTWYgExqQK0zmMKenTVwxhAC0oSVCuH63c6oLM3BcxMYHaThvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5pGA1QTNGWe_P60Eh59RtXzOOQVSlelDrjX-EmAoUiTMoLhRPT7OrA0rUF1x8PhhadoyfKh7DabzR-FS6AjUfJwghboMS0oIFxTva0QtZjRX7W43_WXeqZ3lZeqU23nzTQdMMQ50kuGtd4iT3LutISISThs8QP4Tdy2_4lg5lZXjhsjd5nljmRVmIXa7JFqQVutN-w-1cb32fbJc8ZJXJhnUK1ZzcC5qgOnYfo-r20OTFKjAdighcqP7sPX_9VdeLEWcD059Or3VU2p3ApHiAourVxcQPeqB8AQzls-TVbosW1SMXpueqxp-jNdHhz5SR8eI8YktlkZ7V7S_xvlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kS-OqDCwga4iA2I_evu88QFhdaIgNBBTLV5XnSKWT9OcDU_XryXe7gQCgsBETo4FYQV7Y3GvvP6U6lHoNTa3X6mvbuYH7igz34kWNb5q5GSg-Mr-92AtroKc79u3smVysQUbhCvC-yDXNMlZffhzIUX3FJ9QyJcDHQm9nm9plICOvEL-nZF6hqGU7BXdDFQOenIWcv9GKq8QSVsGIpVn8-lchyO94ohwPkqc_uRWFLNSeSnxWIHCH5bwZYFb5o2pkYBc65PI8sEaxWXhQA9sIXCNEEbiptvkVPh4IsV5kCXmGwanFKmYZyF7RZ85fFSY8DJVHcPMqrZ70OUE8rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpg0uvlB4SPhNvcn_FTjx3l6Q2wM9tjdi1DcgaUZ0ouPoS1HKhG5affL0mbqWrIjs4CUTB1fmlnxT5TK3M3mWNgQcwWh3ed14m5nhgYC7Z9mJoqAY3_wcUe5QZHQU_chx2hhDQc_AkvED24oe_T6e49BgQznyHEI4T4pt1gv6rkLKr5GBtjkOgNCVVcI2cZHX55_864Lp67zkEY6vccLpOKVBf8RQUeqc_GjhP-zD4v8_bDOKFURwHdvpxjotDF8HAcm6WdPGxQHueRpsG3Wypqc-Amuf-mz8y767I5cMjVPePm7gMogsDB9d-l6nesvGimtIEzk207cDl_weVfacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTkZcuUVIDXX-4BWkP7FHLxUD1qIhFrN0Y5mY5xZ2McE2C_EhLiEGaCTHzg7FdXuJlivYX4GtT49CSYYA5Q4COtj2vnhAYsr3r0tGjex5X7XLVnDeXEh8JJR3icqNIzSlUNSnifEW0xEnprf9YJqOu2A5HCweF2ZL9qpUAZmRnrPlWLAB9K7e_6jIsEG7rSPbXrZWeSNQ5cyYLUhYV1dYEnIDo5XMgIO5rJh2nb7thnuwkKDCFd5xDbAIpAljRaBShy_uqYglY2T06IJEsh9lv_8Po5R8UHQW34KWX8_9DE8WQxAAsIWBMbourh9VaHEqkJ7vQgnVtS0JGjUDGzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_JFtDeThjS6eBLbAF5D4dlklL4Jzug1pj7Cm2Eq3J1j-9HyY7vplR3TZzrfwbSLjJfCii1PMlqZ8XrqCB2xOJfqdJvAl2XOsk4UcBZzkLxK0C9OUtcI7-uaFIqWJUpSViULQlIxWBKvTdBdA5NvvxxUweCuho58B0Y65NUylibtoMNZ3gbXgdCk-6AY-9MX029AnMh0zzwT1PqKaHA8Z6d7rkotHV5BJJyq85HesgbzfUC2NZaB5XD0969hKliLsFwfMAyz93Jw15wkuW6gVe4S76sjeXio7OUW2XCR0bzzuyuc-pJX7V4nK6Me-kxjPHnJHUp_ACTR-SViiVMpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjFhuAenKQM89fzTmSfhmwjlFxnnUWDjiy35sgFHrh38DjSdqHRzzM1xmNQ8Y6NE8QJNnQfZ8x9VBViKhOauOdkX7CY0hdSwHf2huvgSzBRUCzjAtWtahyhccsQtzNYdL3thW1hSzG4nEw8Y-UW-PtGNku5L3iTimikbMZVx4oj2oWVjRQJbxeKi_q8AYeElinh6AkxRE832j8rjhOJOGhANfcJ6TPNvV5QD8FexoDVkVxUF6YCk0h0aT8Horz7vwpDh6wdYqk6IYWPaXJIKLiwg3u6T9SSI7BOQzru87yAFg-wz4VAKqNxoW10jy4WNBPJyJkaeDdYykm9yPLidUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPaibF1C3IoEkJUH-wRWYoluk_91G8ocvOFpNEQNQwbH_UoeV4sMr6BYeawcP5caaBZrs2Sh1WH0YLllxsLZhd8jyo2LZ_fFT5_qZSV0UB2JJjnPSK9M5hjmQd_RpJMDDIDzefUqS7juJcvnJH0u5QhA_-CZlULxDIi8z0lasvpBonwmkhFodN_CNYuAw1lYlZqwrGeOAGIQjwf0H399IOxnE6FDJhfPIlrFrPu376tZln4fzGwJqgUCUilVyMv2BHkmaNPvXYEDcbCAQQwPjQadaATdn-LXs9af7kIfqJd21PJu6UTnFHz15j2GAZ9F7vyF69s3kF3ttTJTlligVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoPlbqhFqECZq8hx09ERitieaXS7pSaNsoL_MLCGFBMfu1wlaI5AmT0DySCZQ1uTztSHpi5GkbOCvph4Xk664JG3Of__2iKd4KD8yQRpSkabOCwaIYu5_3bR2SvZ2i97afu8pweqDxOTtzrg8Bg4uEa3oRaCxViX55GTPH2DLdA1LaTZKDfxZww7L7STI1s7VV79MKa8_pg4qrhegzarw1Ysz_ERWKuF9JaLWOUO6MXelt4K0k4pwteovhfKQ2tI7-hFJ7JUnvVBXXBBFNFXGVD7v2OPzu4fqIZq-NMzwKUIW-OaV0PXK96G5kUtR7p5mlraxLW20uGBIBboNrRL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2MjEQTHVNucdUo0fM_-vOTYOutnugm0qdmMqdI4GVDylfNcs-MvpkaJwHEM2hVSInKqcX-Ow20mabh7pUK0ZpNT2vNqKnF7JZ-_ozf76kjwW3r6QU43vLqUqcl_J0m8TbSSLOgdkANXC4csKfynTXSGE4w2tkGjWZtHOUlWRdrdQy0EwgIoVmW-vGSLyhHjCE6i-1XdeT5xYZpzC2mAddMqjJI9NvIp_f0czhelpWO2iy2LLF1JPo5PhgGn1JKJ_oMSkmTd9cdPkpd7zBU9vcLq44Le09Beqaf8_WtD2NL3MTk-Ip8i057FOAtrt7htnXt27Qx2hLM9iQTG79i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXClf3SE5oPpS8Nf3kIu8tl2oG3cyNAnoZWngsvaoJu8tOsgGDgZw0BcgvMFboDWbDj9841y0waKxl9ZFtGarq000YtdI9JaRrAn0tvahFVczfxYO-m17mpDSacl3qeXlqN8zpecrm0AJq0FstzYpq4rqJxPjtqBvwgVW4eH2cZqFTBzBV0X_lZvTPdL1BqoLJGtwLt8PknJbrJBdb_QTcOyBXTJhNkWFxsvlli_-wBgEcf-JrUDasRZ5i6CI6T_forpCkRQUdH3Q6Mo-tWuHajDQwwOl0kyHKYCTsTUGg9iRFSB5khutU4gwjpwa6mERRY2OtPvKuN5rsK-EwiUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیش بینی مهم ترین مسابقات امروز والیبال در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
بونوس 100% بونوس اولین واریز
⚡️
بونوس 100% ورزشی یکشنبه‌ ها
⚡️
آپشن های متنوع با ضریب بالا
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25861" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bm-2gMgjfnEZ8SXV8OskO19KOPhjr5X72sYUGDI325cv51-Qb_BBT0Tme0IJtrLQRXicn3BneBKboRyDjjdLAFWA5J5FJzcOKNQP5Zn3dBfIMd75GCuWe9mQJtKQIWn_6yKwj6SXqA3NL7r7rAGnCILKhY__WspzbABYpipuwgpSfAK-pkY5IubsFZZIXSAuP1Ed8RwNiQoJzp9otgwjFPasT2Rrli9aocF3X8SBa4YHgXdWuzMMzpSzIDRLrnB-FBRAEwX6xb9TomMXlcAXsuAqh4e3Z0CMnLk6nKioz0Ry5K9qbY65jC1M61WCkDfBSBrkIfegPVTtFti4QEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLyYY9jpUt0IG1JhSmEO8iNm1ZytGtG7afvI8xFj2VlR9FMlGO9D3YOqrVgChsJX1XpO6yVyzY8F9oL4v9lqIutpwH89ENz-3zIcXiWy81FxzW-uFhoHlaD2B9VbyjvFjhhrzm09yOxfirNoyXS1DDMk-mGyYZ9MiJhtbulo2IJBPmVWhIXnpKt9xw9UwZUYs-USDVJxFmNuGUzxxomPt26DnMxGURSooZd3K5sAY2gQIEE6cgFQK3n7AVK3PH4DHTnIRLxX_qM51hyPEWb3MLYfGrielnfi7WtaFdIUILhjKKWit5LxJRO4ET2MsnCT-1o-T5PtBja897hript70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9hT6NWKkTiruRxQv-aUHKSCjcWMD7UdcDXdlIi2IQFSckuMJf9qyZQjHn4jjM8LTHnTap9MFqKyxwxBQK9YgeCOuZA-RR9JZDFLuje3eU0typ3crgu_WqbQYyV8wiGm7OHy1iFFubth5KtS6PU4IfUqtRKAbh2HEhyddoWaEaeub6hGtzuTndO8YZyDR3UvuR-UsjvwgwOgN1B3MFH20S5FYL0TvCRxg-xDAZgriMjf1n81fHxDzVfcfT1WtLtYjEOfvL4T94nUOaFYsLuPpuoRJfS5XnuoLwnowWnUNL3Hxey7oED6x_2dKrD6VwhNcy9ATEz2LrYtpLONB7N2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=Fu8ABEpNHu_q8zLNrv7hHyOK0fPcVCtSH-r1y4NwEo7BsBunyIqx2fkM1c9vrhzlTlLi9lqQ1Tlf_QT5R5Io3SVmOcPSAtEPkw1K7VEun4oTVWXTwwR7xTNSgvCmvpDl8gvsPKq3TcKPIzkKLWkNL-JTgnmLCizRRW9TJv3Dy0pTv_uBBODdE8ucEwzc10c-A0mRwWx73I7KXkk_cMS-6ByGr0jSn5BllNO6RdvDF5IXcmH0uqKWsfbY4erUw2V0M4ssNPboqQpQFfx7WMeAh0FBFtrmN5sbtuko7hrhs_NB1qXUD4kDe2lhtIIsjI1zl1islcao1ptnb4OnDmRB-V_EkWnEzaemhU1FRNdq-w5ZSQ3PN94aqqEW0s_rv9BJJcLJ3GCYIYuMR_aDNQL8Ovbzskv3x3ejR7u8PizT2atr7pcnepvLylLHpzPepQR6XywPZIjpT1FvaELRS7epbmGWd9PmCA1bHuTIo7rPMZ5H9K_kBgKqdB_C9RsNtzoFb3bLzcd4_TkcE94SbGlWiN-lwbvc0tgUNsD5BZ_Aoczxsy9x9-eqRkZb28BFxGJv7CzU7StlgDqI3AlGgDre3ddsY0fFNuCCg1isnzfgVjsxNLwCi4NVtsBeJkAm2NVjHaGkLY_zPJpvFYxUx7idoMKeSGrfXRTRuuJtqhSoVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ZkAtoveEhhRVQV5kd06YMu8FcrHimQzz1lboRO6ksc-e1A3qBBkmi1d2N_ITaBwLgeEovP9f1AIiXYMukdVsT29FrZWtcbcqM49k__lRPN3BJv-ZhGULF2G_AkqmPVuduXY3qFtf55DnrqmU9ZhXt6gNWiO4py4P9MHPI-Qn6xgqXnlpyWjU-GM7CJ9rn5Ev85VcwejkOR-inJ9LIo5yNR0zlSAQbSwaI-r__Qy3x-1tdQrXTMdiV6R_39d_pxcgU7P07bvTI_ri12Rj0q_ucVVKhhWhORvB7PK_b9pZJ6wIVDlY49GzbOa6abeFPIIo3VjvyRpptrMM7jaIwr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjT1p6dZVHhKgCdYBLiC8VU_40q2Wg7ihPwT_cuiLU5LQ6b1mq8zfeqkL6oKr80IjyhhF0wQSSo8TCvQcL9CCbP_1Vte8KjYMnqzWy5Eq5hsNik9tYtoAV-S9hy1IoDw9kztAusjiIpK9VsGfoTjLiZ-uVRZ4a4l5Z9TN_fOrVf_XaAc2WWy9FaFZeHsUK6la-ZDXudgue4iLVgJZM-6-K2tvQlZRsWWnKa12_5OsaYLwEkekd4n2lPv9Mr1hfE4XpqcLGom1FiO6PzeRlyNbdMCRcjyITfxUIZT5wY4C7PIrhortk-gJ-ncyAgWemSnKWbm0kmwRCZ6RjN_6-0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSXzOGkKsDDbL9EOxh6QdHi1tk1w3fBYbhVk0-SyiBY50x-fgcmXMACaIdDy0YS5s8642-p6Z-KG4rTByOkoqXm20N-rfOXwt81Y9YcUbfqJk49ChHGPNd6AOy0DMamzmd2IDvianSpPVf2jpqxeI-Q7vAkYxnlJk4n6fWK975VoN9GdJZ3n14sX0NGEcLAHNAzqVaZgLqOH8MsoaTlbQI8E2WafU5FhWExVfhNZTLyBHX5z2I8L5s4CNhIvyI_2EYwDqJErsa_2cYy7-FoNUr14PRjc7TIIKbk_HBR3VGxG_-xIGjkcl7uU-I0UTArGHYWmqOyU10pHTIdnBAzdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=cryYCxLW5oU9ijXeCAm7MFD8Olh_XACHYzWXzTgsWSzjWFdJIz9lQzpjTJIs7jKFzW0Hp10ooEEc5bIN0vvXSSK5mlc92SRUGW_t83n_RpahOdVHUxGn61MrR70ArtHN-lY7qzY8hL0bMrG3biOaq17hJUWjhd2ZBsSPfK0oUTrUXiSKENoKp6yiLVpCdVMB4NsvPZ8Od-fd3qyXh0HhvFF3PP3CpHMlprTuTkJAmAwc0H9GHUcwDNxDwD7hFWY7EpmTZjLx2QrtbMge0biOQTCDpkuolKRd74oulJkdXUATyVs2nLsC9pQ26H3-uI9y0hjxl6s_B2YDjBgKOSRinIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeKQ0Ejvp0YIeLWK195OLoOUCH7D4Z5J-mOBzH9X6Zwl9M5j7pDCIS24e7sMADx_pJ5z1fj7Gyj0cPAg-gO-Rbh1DiYK9UY_ITJiUPqjOWorZ-rmVfQOIJVeUCFncBL7-S-UQFRXhpmHR-D4x3zpNYmOLgxi3g3IO8ibTs5gElc_TM3HYdoDBjbf005G1w5KcDCHPhDzdm5sxvRICbNW_-ofxqID3CMSB7EU7s1PRQp_BlOVc5fINRC0Gj08j3yxr1VuGiB1LH6bqlxasGwTv8kGStAvK0vX-zpFPZpcltlNKOACz1wRFvTMUfAtRixDsCtcD_y-5S7l6aCmvczoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=AOPAVyoatbtCMAQFPci_tBnQHe0H4gfWtB0yXakR-9M7mgl_yMqpHHKNQ3pZG7zrvy_IDYhgCbNrTQbuoTczeF5hfIgT5iW7omwbXkWavu3YMvOSjo8jEz6wE2LqzTl98iEBhHPxtF4dYWKbZrJMFxWLkoLG0w-YmMA4VzvV35iZj3q9jGwQPZ16mEUEQQ4EnLYNChYuHkr4IOcsuSr-YILKhKJRAK-phCMsDKrOntR6duQc8C42QZ41wug0glZBPMnkw7Vnw4Qg7CL998QTL-AsLRIThMllQKA_OWWqyd3IQ3kV1_in2TGy0UqbUM953iSSO9pd-8aLxzRAzobwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlHEZ2BU8gHW554_9dxDtQRm80dMH1UXyQf39ZH_jwJ9Phy41HSOrnZhFru_HaUt2Ku_ckGA1Fncvm4g0jcZ-OKO7GNt7S_xQ6eKVaIee13JkpB6trA7MAFuCsHNMTJbQmA5FSM2MGoxwwoAaFygPQzQQcctcqbKsIoDN0q-ybVJoL2OOr2XW9MMI2fUYo9KTYnCouvp3Am_BEhn4MiKyCFtX91FKLowPaPKPY-DY16XMWbM0e_KiCT_FeT_4pHn0Vy9q86DTljNhVqMay9BTapd3w6jNCOl2h55z7V0jeWpoFDaNRJrIvFFAlmYG2GjiVWIsUAbz8wHANxbZ9kPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=DI0ERWI5rGqVuNd_nmd7j5zFV0TGNrDgw6WidperlUbFqHSgwOsJsURO9DLjXTR0N3GVlHA9_NeyQrTbNmEgkYPJkpymZP1WYq3D4CmV4FffuWQd2V9IFmcpRC6YTBTcj2dT7s-zw4wKLDjY1Hj1aXN8Ico-XP_KTUgyQk-Im93P1JcQja2D2hnDG3e58URZWseBaz4fzJQ24Xfr5oExeyea3__hJvu6xYosqZDAmcXscOuFnhgHroW75OqW7ut4bPO2qJepgp9s6cyJKmcdFdpc3GJQKe-vo0GeHKC_6vcfKBjViGX42e_fNY1LoYNX9oWf1LI9xNWJqdfNO6OfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=vq7baF_jmKQ7Wi3NLdxaWGWIQ5Y1JPIe3GRVjiNC95914g9hb0qObZyv3ejdMLPxNnCgTOjYKT1Yzmia3iDFWmdiEGG252fiJR_E6ZPFgaSFmqnaa7aq9ephXVHlwWnspEAMWgSZpYgsA--JNPgLRP4Ne4RNflcYcZ4UuTqzqApcCZqyo-35T01NXVJbujW-ENSxPgADUi_gUdy72WsS1j3Ni3Hrz-G-ij0LZQV5Dx2mxuL0ALz9kuMPi8hSk1mV7dXwewO_HN0bJSxOLsTF0LmaluAG90izH2Xag3jgJn4A_47NBy1dj2S8-QAOhA0ADvMOAKchJFz7iw1mMZe8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlk-YXMg9ShBP2Lk1wHaMutolpiaG5zX4ZRJA3pKntA4w_N_lU4ZssR9R_3G28g9ijc4Pn5zvso1GMvBNntFo81dpKht8jrtkMr2uskaVlg0ybbLViDUHk5AfXtYRyln98D3XKnXWvU-wRfa2aBXzqAY-zYy-hYlXYSa0PLX-y9p9IeHZ6Cye6rUCFHtbpmj09Sx0wUMyv628Kv1J4r4gs9XULuy2S9x8j_LgznHPsNgOl_DqbtuIhDWOZxLNdJxiUei5Cp3GQn4jyZHSJc_FAKnZPDCes9GRDVfQpWxOD7oOEhuX3lw3mBPPFqsxguzNJNHA7knhhAU1kr2RapD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😈
لذت رقابت های والیبال با بونوس ویژه ی وینرو
🏐
🏐
بونوس 3+1 وینرو مخصوص والیبال
🏐
🎲
با وینرو همیشه برنده ای
💰
🎰
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال برروی رقابت‌های لیگ ملت‌های والیبال در طول مسابقات،‌ درصورت پیشبنیی اشتباه مبلغ 5 میلیون ریال‌اعتبارپیش‌بینی رایگان ورزشی از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr25
📩
@winro_io</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25832" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwXUKj0HKfOEPHsNVwy6glA8BU2GVizua-XOaqVhInHvxVimWVSpYpa8pdRt7r0_c8Lpwl2IhnxCk63TOx4lQPGUrx1MYKdW-To93EuZ9jy5aQ88FGHoegjfm9ZIa2OFm3inGbm0DzRE_zTdFWneGB3i0HD8CfE7l4fiSuMYQXvMryd7DyxN1uy25OKUWbBkymtQzB83JOs-jLzASB7jeUSzI1mF5pFD-wv-s5p9uyKjabKeBq7ADxUiBdsRCgG1830DKY-EIH9SIFofqN6tPmUo6AL3eAGK5KO4cTRdoImSFPE4Gwg_8JaXrXhrp01QggwXnMlfojBcaNfNSRZ9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEcR0BSHJqTTO9Brj77H5SYCYctIfBcsqJ_NeWFNLKV15phO1-8LEeVu9708QdXnLyfJw6gIx-A7goAKThnKRt7w4AD7Xz7diwl7fD7x3x3NqlAfDp8-fQumQ1bHJ38-RVzFun5j07PCi4Llt6ZONFjeznnNNhfTwgiXTaS3WAgjEam362yigmRVVEcJpHey7LuCsSfWK-I5-LITr8gzv4G0L52gwfeoaNKcYrBmstbqcE64Iw13KxLvXLMKAbAt3fwWLHaGLpJ56_lIRpD1-6blNMY7ayHVAFFFo2q--KcW1u3TtQmX-bEIpgbFKRAifr6BjlRaVALvyTWKvTxi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GV-sjv4PFIL25qAjhCkam_SoYxMzlrVdc69N9mSphFp0-8RRd0leCnsKj0kS12QwYmqJ5y8L43jy2JJ4fqYnjCxbmby2gCwPMxVl89sNL7aD_dqBlyg6QDm_2Jxa04ukQEfOw6Z2VrP4brRIfJby4gf03JBTO6xtauNKfws2Z7SC0VWC9gHFhHs8y_Si2blf5FcXUkgKfhCzZZIIcTOgCcDjWo4vh5y_zHzSImB4lZFB1or2jKQzy7UctngezyMP5Hu-1KBu14UqCAKy5NorjF3kuxk6RMoaVNF3qZ569yxh9fOqJ0VX5BZARg9tB2LrnJL45gpQgbaJ-5DNtoMGcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reCa3FbhfY1bVG2BwIODG3fxHw-eVMjCkfEzAfynRXUmEpW1pYGld1Z5a8K0VgDxj6Gl4J6zGTPsbPu04VUF_BfTDKnf_PpTK1adtTHrkCifpTUP4Y_YDvNPggUVKNscQXXShxfMxAYWc7flPvO1N5IXI9phWtw_O9_WJ6dgRxM23F4JJ3VUQgTDfiPjqnr4iW9WEMFEWw8ENWTaWbdGc2UCoZpngbbSIlXIIeHYgz0v3aFBl5QseaumRoLU3YD0hjwZlL6UbCkFQXUW2wvIkrzyi9IZX5i9PBib103UIMx0sxO8hf_Tg3o7idPU510bWeVTx3CafDkoGdCURbgx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=GeuhnMwH64381Fshj2l74Crw-kjpMs099Dy2CweCmObBHOZLdxd09KNA-hx_Ul7eKgwoz7qnCSZgYF-BPIe_1gQUAuYWSQUtoC_SnKUN3uwZ2CughJFgho29bau4yUg_xfrUQ5NzCt1svOLsfLDbfuTKh2I240Q2F3LcwWFqEESN9mQHOHy1JeE7RCj3soaILipSf7lZxXCSPRLx-Tq2w4yCCYNP_Kkegd9RglOO7s50lGke0l18tx8vJ22Wbo09S4gvZr7fA_lWY1yzFiiuQPJynuH_yX39NKRfGuhxOvRawfTV-Dg37Wmt1wLpEJ9TJ2Q6wL4EhEaKIUD-Ktlncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=GeuhnMwH64381Fshj2l74Crw-kjpMs099Dy2CweCmObBHOZLdxd09KNA-hx_Ul7eKgwoz7qnCSZgYF-BPIe_1gQUAuYWSQUtoC_SnKUN3uwZ2CughJFgho29bau4yUg_xfrUQ5NzCt1svOLsfLDbfuTKh2I240Q2F3LcwWFqEESN9mQHOHy1JeE7RCj3soaILipSf7lZxXCSPRLx-Tq2w4yCCYNP_Kkegd9RglOO7s50lGke0l18tx8vJ22Wbo09S4gvZr7fA_lWY1yzFiiuQPJynuH_yX39NKRfGuhxOvRawfTV-Dg37Wmt1wLpEJ9TJ2Q6wL4EhEaKIUD-Ktlncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNMhX_y_7JQ5LSMZHB8tpycb20oy9pyOEnhu5R75QPY7vR1uudFjXV0LFY0PXvFZzkTMNk6Q-zs3_QMCWgMKNS9wTZ3Kfjz7HDK0eWR6YWWvK405Epwv2gPfH2gdaJ8dkalUJEeiR3sqGbZ2p6dFn9zhL5Oi_u56vUKIMxuByBQYKLSp4Um-XblHRgLStEakp-HwRktv73tyK1MzPYm-kqxIocw_iwIsNV7fNVFRV2KRs6V1pgp-rH5vEVw_geHcpV59LrZ5jqMqOobU-MeuPHnfp2vRZUQdUKk5CWno_zI-I2UTEzP_8eEVxKN3jBVvBiMnYaBvbNobCcOHIBgUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd_zqRZVtb_e2z_vNoZJl0ye75zpZzxqJpRt3SSz5WWOpFMpCRrst9U-La5ghGlKREBkvbW5F5RdVka4DHOnTBG2qHSObkOEsKmO2bkvzf9aYxgcVKv6QUkdV1EDwdjxdO9zbXNe38DD_mvAf7RMajvc51SG7d-bWcNb5upZiPPbuZwAdHvBvA1CWa4yM5N1sXCegR6viBv1KNmLyANaWjHNOQGAA7eVlwnIpOBUn5UQE87yye5fK_spPlL39auGDusb7OWqYN2Q-psOB2WuLyBnoZ7H_Agba8keZRY-F9fjCcQ-8ZKJz-kt_NQAEY-VaqFAHArH_kdw8aFAH2LL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=TLqE7V3T487w1NVB0q_1ZfmvUSSzpjEUgN8pnQFt3LLbzI_peuVezu_GYTOQMUic7tNjOH8jM7nC7ccmqo1gclsvQrVV7xJCd-OEwSjsTOn-LQXPpzfKnSJINZHNRt2kSYtCXumHu6EOcuu8uMJKrnGwhVlIf7d08kl5dldJ3VZk9RYu2KSkRbe9qwPohJF1yrgb7MD4etEnWaTjV66dj4O1kZTzHGOv5MDWQy9nq2mnSI5DnHWdti_6B536pqvhlTT8t-e9qvfkR4gEVXpoJKymY_S6fE_hSbGo2uRLdG2W722VPsQ8P2KRvUBhkwcAJuPAJ0AD5bc6QvDiO-P09Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=TLqE7V3T487w1NVB0q_1ZfmvUSSzpjEUgN8pnQFt3LLbzI_peuVezu_GYTOQMUic7tNjOH8jM7nC7ccmqo1gclsvQrVV7xJCd-OEwSjsTOn-LQXPpzfKnSJINZHNRt2kSYtCXumHu6EOcuu8uMJKrnGwhVlIf7d08kl5dldJ3VZk9RYu2KSkRbe9qwPohJF1yrgb7MD4etEnWaTjV66dj4O1kZTzHGOv5MDWQy9nq2mnSI5DnHWdti_6B536pqvhlTT8t-e9qvfkR4gEVXpoJKymY_S6fE_hSbGo2uRLdG2W722VPsQ8P2KRvUBhkwcAJuPAJ0AD5bc6QvDiO-P09Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpocuhSHefo0dAewdza8rsPgncroaqfpkvQSxYqCYmtCuZk_iMswSm3ySxpIoTT4ealC7EPGYbI2Ie-LfxeO7yIdN9lVhDHYz0hi_gL_m2sw4REh9WAuin2AVUo0D9t_fLQuw8NTc1CWe1e7-6APIPAQsg9SL8k9jFowGqJ-y2LAxRLx-_Gok5PrAtAVmgQPSdjtyGINA4dUn3w6E2gyQnJZe3JoaP6hO2ERI8OIFaAk5uTPv8jML0ZG3iYw3vxAJ2HZsl2NvlTwFTA7xvxyA6r1z5FERVNjGJZ2dC6cXFBMccqZemJD51s7ShC9aZK-tTdhoeWEXGKtjGZFWrREZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=HUYM54gSOQmkNstwH8O-wBiWsHnIKmHaPcEECZsN7Hdpo0jMzRivlrlBxA0LObcVQ-_DlGWMluKQSj0b8KwBbS3CwW_Wvst9jZiRKYzZA0kUziD8Fr7Z1SRJYj6CrzFUCHZcsjUdg3lpaHBQPuijtLxwzCPAH7KsP39cZPC6rdUBR9fuuOEPZHorPEH1A4pM0bY7Ieme0zEFI0d350vPg_tEaH0lamNkRu9j8VsnGKXIVj8uJtK-K1zYqkiEYvWTUPkE9PY5cidf-f5w3xtMpr1jrxYmDwnLt9S9hh3nn9_5dQGi9YnXtynp2_xumlMo0GACvWuBBXeTtJtGwGDP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=HUYM54gSOQmkNstwH8O-wBiWsHnIKmHaPcEECZsN7Hdpo0jMzRivlrlBxA0LObcVQ-_DlGWMluKQSj0b8KwBbS3CwW_Wvst9jZiRKYzZA0kUziD8Fr7Z1SRJYj6CrzFUCHZcsjUdg3lpaHBQPuijtLxwzCPAH7KsP39cZPC6rdUBR9fuuOEPZHorPEH1A4pM0bY7Ieme0zEFI0d350vPg_tEaH0lamNkRu9j8VsnGKXIVj8uJtK-K1zYqkiEYvWTUPkE9PY5cidf-f5w3xtMpr1jrxYmDwnLt9S9hh3nn9_5dQGi9YnXtynp2_xumlMo0GACvWuBBXeTtJtGwGDP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijFSfiUdVC6hHD8DspDVVRW2lgAeo0kQqLTrluev_jDQNx1d76C1gND1LH73Y63JyfvHJK6Ty4WuzBNv4sAr7BL2xIRFiEyBdzuaJKY1ZiiXcbySL2DhTDTTdYxifOAypGiISnaMBIpD6PSVePth1ru9zYKl_lGJqVliQcKkXw2q57nWGXhVlgMqxqN0I0GQUE8fvJkzbqoMyCyA00P48qaCUkPE7NC-hxD4IyuPb9UjOiaBdqcdCtwrucVap7gG4wjTC2j11er6dJ2oO5dsUX1rXOKlGzICSNuVgwRVsQjDBCX-9MXFFnybk3eOzknjsx46T15ymVKO0v1CdLYn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evxIN4AromMHykgCDB30PmztIHVan_81JsfnurN1l8g1A82d-9olhQ92EoJXhtdB6mIco6SZQCi7AalFJk06Wo7APO8K5ZEyKznWW8ZsuyaAxpxHw1krdF210knKGzZyplxf5B8v2K7n1JjmMZWnjEPNYtYKW2SjEemhvuq7N_nybRHRBVeF5Hhi67KEP18OBCT1Q2K72AdvRUgmgrO4Sw4MmddWy4ZEqnXAU_9OgOPfxGWQypCKbqYrxzpPHO9ZJ4hHRCNDzS6EC7pyNbJjNEaJv7KrEqDHAbwsgmWstnWmR0Il-SO1dO8_AasdUBxp1Trzr3tVHkVX449ehUk2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig1JM-HGlo5m-Uq8eKbFde0349yTijZY23QhEci5M5uaV9BaC00mDfpukHjEH6kqpO9lPXVXGNnmMH-CHS-ss81oRw5O04KJalaAl80AWNrt9E456FonYJsG5P33M5dsnO5SzNVG8oRPpoL6WESPR4IheTRHOZZKpRCrEbNsfQUn65DXtKp_CblZdmAiN9nm6m9lyjj1GN2hX0vBN040KRE2-WZAvpM7_gPZnNexi0Gj5J236_89cOAuYWd1Dbc67VSorUwdAo7q-JJWDeEyU32AqRPkzL3lYIZv-fzTJug7Hx0vwJ0MP618ODrinWQyMRJ8Tt-S6g1pB_w13U7sKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIrSIWvwu90rvol-ZRYVnRLl9-6Q79TEs_iUOG6C4w_i14EOTeYwvDyVCmyxG3-4dxUQ1gjkx5gxlJiDpZM9U27rgH6t96FtznRDNBGWj97FhVEjI_K4lwg0OwB__eHgeJclvprHxw9siDcjjY1BztZkXFI2595k-8iNzgHdMsdqWGSU7YhDMLlImdmmk5en4e5QsSBOvnGu7v1MSBXGzBm54gd4fWkwbmsM-wqvL9KXACunIBLwA_ORrN1YyoKny8Rbx_boZlZHcsqDeHuP4ZGFtOVYeP3Eee2Lsa0IVdznjm1ua46MuoCzA9giXTZzIRNlTzOGCrTzU097WQMCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUUVCsvQJEd0Xz24CJreTF9yk0yKNnWEAOqU0pkC6fYSG6mVVpDmbpcueqDlsun1mjaoXgxTNC72QVUKnGPdmKEQARQ4pwlOXuKYQplZcNErxm7Y4LyTnnS4ASwiwNaBjMJrA8rUcmDI4YZyzqNuyzotXnclKQQn0Ks-nFK_9NBmmzuXvZ6SUyhDYDfvsuY4b28G-IzYPn5hciJDQlZLg1mpUqnJY7qKFLgDnFGeNWjIxbb8joLX77n8ln3fof0HQjgwMhBmN4CvJy6DcbVZ7aQ5mFe668c4BJldwtxGg1S0PzKQJpTgTrmIxshkHVKx-OC6iTFPhU-nL_unqcPwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4YILq_F-mewJANE9pud7XEK7IAC5y8rFwfcMuO7y8kn-210-AiOMtIGfkJks2BGZZmW1KUrvK33y_Y4atAIPuj9qErFpEt4qXha8Eqe3waUQ1YkZwy4tNwaQY_FCsLibDcAkQb1bFuSx1eOCjb2zR5TdxHZq6oqzMoqRgFtIcCq7l4KVng0OHTvaKIUMEhhxNSUVS6QJkPTrfOnbEwU2TlKQiL4k7X0T54EoPvLHxrDyStJmYmg7o63a7sbUbspNbEPoFyvcEk8n_PSfuajZ-HrQ5NRDpcxw9z53e2gCGDfUiI5a-dK0jfw-x63VqAmp0zLyEk2zD-F0slcmlDfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKc66m_33dEEPyL6WldrIZhDgCawuXDmYXjUH6rMrssZF0akYI8QvD6M3gI0nBpZVNsgtSAgRDLCd6zSQXnQpEwRHqnDAudGgGkdjAqxYtAZQtzLhHy8zpBKWC-XjXkeA_Az3l0as-UDyiZenanEzJWRuP5AI8gytoPLqcRYPqNJMrkPfkQI4ce_Utcx12Lsq68_9f4G-7CJYjl1Dc0XVFSOBEiubHL8JuakQZSMk6zr4JVfLEypTx7ZKTQRHpeJwxfuGdVSTBKw-icFEhjnsBT1z8Fx4zvHugjkPkBn6vcTQeOPU1sFQQykzPQ0tPcALxtDeAnOazrGKUyW8bwlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2isg5zNHt_CLA8ksnGhzWBJU8tiQgSx7s7r4810bfuI8nhEilenxXgOoB_v8630aDI69WclDxGuM6TrWHJ7XADlE32jrwQnExp7DuTC8x_E5Ps7bdc7fyVhnSGK74tQTGVsRC6_qINk_3_BKEu_0Qn7-NIswzvQ0szN5jUMoKYqXvbWUIPBKe1Odsx4T-C1DM3C3m57Eo7KmaQfsKAxWCFKmPrHs_20K_TjWJ0Nz2X1atYtOqzLoerV0VOz1i5HTF97DV1EYAwmIsW_hV7_Bu4eOD_270yViRIhkNnmU9eX03SKD099d3N29sqFMEhlIo2DJ_m0qIX4AcnU2v3U8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chGET9TjqzhbKt5mMvT401ErqnhMZ2beZc5SieR8K3Q0_ULNPLg-MiCQ02_UIV9TINRgz1n1xDa4kqChH2ZUyv3D4FrZW_trlyIOgBmIx3B6lKsUQpygcjyho1a-pwG6Qk7-iuwMNBDg3R3auP2dnPoX4-UHri-Y-0ifHmEcTKm4N2eWsN9D_YgfOsewK0SJNR68YSQzTYiIxKIX9ybz0Cjc_seSYca7wDWmfWTSjKzuvILIA3NG15hIKEhW7WB3tU3Z-gJj5DoucIaSCapI2_AExWC4U25IRVFGrDV3WiOuspQoo6xB6vHEz9GZ-ZseIYctS34UIIKbQFs3fMD9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUI2EwyLRYxr8XisnXlxVU-Iar-ymsW2AMc908DECmoIVZFdhosT0LKm3R-cpujbYxBHXVeeg1l_I5a_KK3nUS4wpqJLZataBinh7diQLFEBuT0YXJJl9yfBSz-Rz5z-K-tCAGLPsdfV6aWFM0_pyhdhVKD61QYkpX8xcqOI0phkwECNUdRtSKzUf-4q1OYh46HJfLiNzJmf6cy5Nsxxe9JQCSkGUQLAbJxU_dwGkwgjo7yGwEQRrjsvSg79v68BGQPurwnA0ZlZ10N3oj92EREjZbhLOwY7FPilf7A9YUtGe4zeEalqeUucy6Z4lbOnmkdz70Dxi7ymuC9pIjaQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=pj8SHb7Y1HEoanHyvcRPhXixPnRDFf3bk0wkv3uKOpGiNCwVFvkpxz8Gn4N85yWhmwt4Nr8IgEOso0-SwDvPKnsmHQq_kMYEdZPLXPRKphl0CFFUufApg8smHlQiwtEB88TGTeoR1Ktq5uW0hgZvrZtZPZt-krOh8CWSL65enR9UYGxIBzI1STZeYzn4qLBja_FzzYdzusMQDFu973jWckoT297jyqiMiGyBiOyMVkeBR27BaJhUrIoXXsXcEZLQS1DQHtcQG9fa1AosetQFDCnlBZ3jCfTy5zQjH5fAPRh57NKBaCMr655o8ott4pE5BQFj-4cDEDmIJdVaO8x4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=pj8SHb7Y1HEoanHyvcRPhXixPnRDFf3bk0wkv3uKOpGiNCwVFvkpxz8Gn4N85yWhmwt4Nr8IgEOso0-SwDvPKnsmHQq_kMYEdZPLXPRKphl0CFFUufApg8smHlQiwtEB88TGTeoR1Ktq5uW0hgZvrZtZPZt-krOh8CWSL65enR9UYGxIBzI1STZeYzn4qLBja_FzzYdzusMQDFu973jWckoT297jyqiMiGyBiOyMVkeBR27BaJhUrIoXXsXcEZLQS1DQHtcQG9fa1AosetQFDCnlBZ3jCfTy5zQjH5fAPRh57NKBaCMr655o8ott4pE5BQFj-4cDEDmIJdVaO8x4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=unkwVJwFnvXdbNWGE0AoeI8IlwZPMM8D8fJ_xlUdsdejLrnH64jNUyHte7Ce3XXA8pO72YZqF0DBdGvg2CJ2sPbOO3qfnmaydVvPmH28C-_aBP5so1378PH_62msualtKL9gEUboWFpWbETQFVYoMOQmwtSn6oJWAWzWss-ZQR8opesRaS2nYOH0pk51bPoyfJc7_Ik6eRwJQIAGl2FlcIIsrMEkJLQ9hrZMm222RP_-k4hpJDH2brePxo7X0fCV1Cdi4VOBb_VOMIs1wrCjFM07XxvTp3aFsBwwm3uE5_V_0NdE8X2eq2ofWg_X-E2lHl22wxrzUuBOarz6i_zpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=unkwVJwFnvXdbNWGE0AoeI8IlwZPMM8D8fJ_xlUdsdejLrnH64jNUyHte7Ce3XXA8pO72YZqF0DBdGvg2CJ2sPbOO3qfnmaydVvPmH28C-_aBP5so1378PH_62msualtKL9gEUboWFpWbETQFVYoMOQmwtSn6oJWAWzWss-ZQR8opesRaS2nYOH0pk51bPoyfJc7_Ik6eRwJQIAGl2FlcIIsrMEkJLQ9hrZMm222RP_-k4hpJDH2brePxo7X0fCV1Cdi4VOBb_VOMIs1wrCjFM07XxvTp3aFsBwwm3uE5_V_0NdE8X2eq2ofWg_X-E2lHl22wxrzUuBOarz6i_zpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=tTinuN1hojNx4AZEjZ4bjmVxe056yKw9AKxJSqOCs4xhfmNFbKTWWYE3HMW5ytAxRB9fQMn8mdfP13GMZEYxcYkTvs0Td0Iiud-7iohHtvRwRu3EOAlDHtxg6qQJHiZU7XwA7Kq2Num8QAjrxma8MqCYIChxsgcaJw1iwonA1mLxeknPnCB57WneuaHtFfitcfKp9aczmahLPeY5ZFbYUaNNAvGfdnaPE15LkkVzxE7EAVBVtpbD5dHgq_EIklp8Jv5j7MUksLQkSs0Sh8JBaN0_ZaIvg55J2vA53piKRnWzQX8S1RTHHDXZLt4VyXTUxz0pJ200oM8TnlLE1JT9sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=tTinuN1hojNx4AZEjZ4bjmVxe056yKw9AKxJSqOCs4xhfmNFbKTWWYE3HMW5ytAxRB9fQMn8mdfP13GMZEYxcYkTvs0Td0Iiud-7iohHtvRwRu3EOAlDHtxg6qQJHiZU7XwA7Kq2Num8QAjrxma8MqCYIChxsgcaJw1iwonA1mLxeknPnCB57WneuaHtFfitcfKp9aczmahLPeY5ZFbYUaNNAvGfdnaPE15LkkVzxE7EAVBVtpbD5dHgq_EIklp8Jv5j7MUksLQkSs0Sh8JBaN0_ZaIvg55J2vA53piKRnWzQX8S1RTHHDXZLt4VyXTUxz0pJ200oM8TnlLE1JT9sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i45yOfLnyW0N-TOpfjO2o9c20gg__IyLZluctSh_AVRSU21AmD34w0ZaXPX5Q-5d9grLizlHBX9nfEFe_w5MxNNHEZZ399ZNm_TZC0idd9vAt4i1nHe8ORvF6wLgJJOFMJGCFUFMwPqJufwLYqGle7znDISLx9S-9oRvKtLk060fW0vpvWeeZDbW6UCQgW0UXPsws2CVupavNykEtKEK9JvpIRMlsefgRGSugBk_0lw9QqkCwS-gtivMksC8fR_ALz2wXQTDoLfm9mwXCvQZZvXbJaf3Gozr2Fm_MRffW6RDUP_Dr4JOtmxWPvmsTMNj-FO7wyCp__CCL5CQDG1rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt2HftJucqIs_Lso651qJe-y7-WavOoxRN0NMEYZujdlazwfIpkEpBEbtR72O8zYwuguSIs1V2Wa7DENLJ0AC8AblioO5yPelH7IqW9DAta7dJNz5o3OGzVcR7Q32ARKdvQXsLaiT_se5lj1F2FygCJ17Rx66010W2iJszw50QwLLKijROHKF1M6CcNB64FQPezyQBPtA4Onp13ADgzHolW7fp-BN1F6ylvLqnNkXmwy4F3or9J_QCQcITKbCt8xEeZYRbSuUatpMhxOdM4Ym-XlhK2lZgIE4oMuo-_UaeH9BkUhEwBOOM8LYQxTD_eRz0a4lh1XpBKHvghfTerfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-SfMVHPpNpZlTzwQTH2stw-LBL9Z_4YkX7o0UUjxP8qkbhIwi_-Azewz2I5WeuTCAuJYBnmfMx0Joi9gYFSK-LWRMaTyHsMcUn9Yrewgebx4jPXtrpECYRFO8xL1VwjfAGNAcOImTqFm-NVWIIwMBJfpLUIUx5mvMdCWsCA8eUJ0qoVHwZw-veKmjl6cPdCONTLfZXjOmKfAbGKUzvsvURk-Ygm2e7_zaIlhmeOPiHUhscO1I1Uh5DcIi23Do5mN_Iyho9BaKvGXPss63IAeP4x9BE4LLwFHbrWjVQ8mxGWREQKevIG8hvP_SR6Pozal6G_5VsBIMHh1gx7hYbkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=FRfJA55DAMfeH3AGey0jb08C4oQJx4PTmRVjPTFvPmv8tRX5O7WSPiRLJZKLGch7jTuW-KJkHue1HA3d_SMYlDeTGwkisVhw4qsfcZ8_wwqxj9RFdBF6KFvNCTZkx1ir_kYqIYyTs0RnFwhtDXqTl_a1EVcgswqg-9rwp939N3DfsNGLbH0DUe2ZE6cBt18P38ojxCxou9frmZpgUEKKdRCIjdL9rq7imzr30SgVqZiqZqV8-5CvjpUhyL8WM-iGkdnr0BPn4Tu_tVqEhmzliIEYXdkKKqVwjgyyG-hJddM9HdPnWKcMFd3AQ3VPbcJ1GDdZwW3_VQlXfaR1yrxYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=FRfJA55DAMfeH3AGey0jb08C4oQJx4PTmRVjPTFvPmv8tRX5O7WSPiRLJZKLGch7jTuW-KJkHue1HA3d_SMYlDeTGwkisVhw4qsfcZ8_wwqxj9RFdBF6KFvNCTZkx1ir_kYqIYyTs0RnFwhtDXqTl_a1EVcgswqg-9rwp939N3DfsNGLbH0DUe2ZE6cBt18P38ojxCxou9frmZpgUEKKdRCIjdL9rq7imzr30SgVqZiqZqV8-5CvjpUhyL8WM-iGkdnr0BPn4Tu_tVqEhmzliIEYXdkKKqVwjgyyG-hJddM9HdPnWKcMFd3AQ3VPbcJ1GDdZwW3_VQlXfaR1yrxYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba7gp9dkBPpjFpNGYSksSJhCCrFMpGvnt1jjiLYFk-p7T_pg1drZxaraOtfN_XBkOc5wbtJ4VGLRHguMBmis88o8uKWrPAbJdpWp6mQkDpuZFuMR9tBmZ1OknjpynK3Cy1HmaD3UM7gKTI8eHOT170CjgozyTtMyqqTDjIYKvf9-vELjs53srdexsdGxvc7MUJeXOjvCUyDits9DVu3HT0NAl2yqVnXJEo2TVDmlcenrgDdTXuz4CJdIjH5xK3BCSMcKO7aWqJnU6WFkQT75K82nfbmy9zzxUU2YxDJ5cfrBrfWWKEksv0iS5OK11lyCa3PKwJHJD3HJ-FPOlai8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=CMaH2DLU5Hr8G5tYZd1WDN3juZTVlaLMLGpg9-GRe2VW05cbvC3Uz2OLrmkoBys-W3B2SbiUiUubPI9M1bTDB4Iiz10B--RUKHUF3P8l2RPIQATSRrC2io_s5J94tBvVJz-2pCA850dDE5vXfwalSeFBFmv7KpRqZbLPGqXDS4NNf1xhXvByQaR4JOSHZPNM20xAegMPWdN2Clj9U7dmS1XHc5iPVUJOuqUkHM3gy-wNoCPzdZbjR9s6bkl2cXXGGwuBoIbCdOn47HDKPyA6wtcHBKcBEc283NtE38pBNH8UbrdUkV9fJCJJPNt9siwIkk1ntWJFOVF4s4kfDRxGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=CMaH2DLU5Hr8G5tYZd1WDN3juZTVlaLMLGpg9-GRe2VW05cbvC3Uz2OLrmkoBys-W3B2SbiUiUubPI9M1bTDB4Iiz10B--RUKHUF3P8l2RPIQATSRrC2io_s5J94tBvVJz-2pCA850dDE5vXfwalSeFBFmv7KpRqZbLPGqXDS4NNf1xhXvByQaR4JOSHZPNM20xAegMPWdN2Clj9U7dmS1XHc5iPVUJOuqUkHM3gy-wNoCPzdZbjR9s6bkl2cXXGGwuBoIbCdOn47HDKPyA6wtcHBKcBEc283NtE38pBNH8UbrdUkV9fJCJJPNt9siwIkk1ntWJFOVF4s4kfDRxGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eshuSjLUOas9RNeA1RUeFZVjUxj5cORHYS6OAp_AUnpt1UbLnOk_xXy3kRYwQ0R_3qvqv_Ky5NlNvvu2nbvoCIIHWMWEiOC6OUOpF7WIcfLE9IHCT0CCne1uga9VRUoblZY7ofuUKUIHG-37ThE-QX7p2QG6X11Uk2diblXpFa3O7HwTZGHU80abBacmkT3ipRjuB5JfXf5h8szSv6N0IdMvXnB-njGuZNESuywC_68yqimnYSJAZ7I5hL8vrxVHnaVhJcikyoXJLE_ff7WmgVJjCGsp_vWBLjcIbOee6O_i6pmqA1UwOHDnk2yWpunWitdtmsH4bwYJ_Ciu7IOg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=O9NdGkPURDdltPP2UHz4YECd9o-mO8aJtrn8iKLmjIoarhvEKnBr7qBnrUCUQfEfJztG3ppSdbjFHJaCltpy0fLAQwgDwqpk-3fr4cDKlx0GU_bYmgvbx8C5pj30O0zkQceF4V_Dz8sRfVURtFufy_k9QPYe4g0nBVABLvHtWrtoLki_xu9pKTxXCZpMeGDUNdSYrrkgahiVAH6emYm3_z8hroK428oP25tIoH8iYnF6Rh45suAg5dCczXeP8gnwV0wEiPPooltKxF7ZfqQeynNWUzzP6sLBGvM_GYH00wz17LpHLqXDrHyZsd0Ybb5HBt1B53s-dphV_02d1Cdfjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=O9NdGkPURDdltPP2UHz4YECd9o-mO8aJtrn8iKLmjIoarhvEKnBr7qBnrUCUQfEfJztG3ppSdbjFHJaCltpy0fLAQwgDwqpk-3fr4cDKlx0GU_bYmgvbx8C5pj30O0zkQceF4V_Dz8sRfVURtFufy_k9QPYe4g0nBVABLvHtWrtoLki_xu9pKTxXCZpMeGDUNdSYrrkgahiVAH6emYm3_z8hroK428oP25tIoH8iYnF6Rh45suAg5dCczXeP8gnwV0wEiPPooltKxF7ZfqQeynNWUzzP6sLBGvM_GYH00wz17LpHLqXDrHyZsd0Ybb5HBt1B53s-dphV_02d1Cdfjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=cLDAPu6Z0AObUGeAGugovJ9ISHa8Ugm2fUKgEW2bYdY7gMMmMMcyVdXFty9t16PYd00t7ORmsS-RP8e3E9ZPEGu6fVRkYEH5YCkE5uhmFm7UnCgOsq7x7s_y9DaHwm4iOhoWRslGv-ucDSYWyyrYaMCJwNIF0JJfhmq_zhLV-kT2RTymsh7AI1L6p2Ox_1aMTtE2XmEBYa5YVF35gXwWGbEH0sJDUqm2JTAe7X4tzxPPYDRPzHrtKMbW-3JYnvGWCwI2fLmqfjxMztEhpN5mSC-t6uAgdbdCoU1KuMqz6EkMX-FVRzhMgLBEcAa1ib__bcp9aT12AIuVkZNZWSsflzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=cLDAPu6Z0AObUGeAGugovJ9ISHa8Ugm2fUKgEW2bYdY7gMMmMMcyVdXFty9t16PYd00t7ORmsS-RP8e3E9ZPEGu6fVRkYEH5YCkE5uhmFm7UnCgOsq7x7s_y9DaHwm4iOhoWRslGv-ucDSYWyyrYaMCJwNIF0JJfhmq_zhLV-kT2RTymsh7AI1L6p2Ox_1aMTtE2XmEBYa5YVF35gXwWGbEH0sJDUqm2JTAe7X4tzxPPYDRPzHrtKMbW-3JYnvGWCwI2fLmqfjxMztEhpN5mSC-t6uAgdbdCoU1KuMqz6EkMX-FVRzhMgLBEcAa1ib__bcp9aT12AIuVkZNZWSsflzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpca-jFZ0f8F1UPGbDPamHAlKc1yK2uW1RnsYduVPsFuvov18BW3ThfFkkqiQtnphXS5RXHxiMuLsmmCRwdYhw3aMVW6dCGj1eaFRFtmqoBKnlgW-XA8CPGGem60sA2vnqgYZ3erPMezBiY2f6ExdNTryJmXRTiUC2DNseKIEzWXurJrIodeZLUXoVq-8UOjHgF6s-LMBnRYsePLyoiKIPxrfW6HWEJMLPOPkc2Ol9iDnmGd0j9eX_S7iVxUpA4w0Q8Riw8klIibEGGWXYcuuvqfAXhW6FZ6dTkTYXGHVbq9bO1Oii1XUhmizdRUBXCJ7lIHuRdbjYUVdyplXy00Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEVelnCmcjaXbMmK2FI_lxkv8AEAvFbZWKl8T-RyvmrXc2Vgdt3fNHK6ThvtEbNZSMbC1tvdY1mBKb-oQD9-PUhzoQ-4QP0N4bGVdlqBg1TKt7K_6AKMMEU6sgk8I5BO1XwrO9E3FobtS6XYVRQfv1rEZRQaXIKJsDODq_ajm8RzABCADkypwwXGTvfLYQkyctyInPtyi2tgPlXakBRkNr3wHuaRS19qBuSjff0YK9phtFRTy13TCSgeGwEhMtUL9goDVANnJgWvDednXKgFam6TMInWUIqBV3xJRCJtT-Itmeiz9zX_coshPqyGS9Q3xwDabju5ndkPzTfgw7OXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bw2sJdF6Okg0L9MQQaZb1Uplz4FyURRCKf6tu7J-OWN8idRYQPtja_Svdahwc97X2ZAC0MiNrgbXKgVDZ7Lf0tVoWNs71hC60d5CnCCX1ARqKspF8E09OE5CFv-j7K8xNh6LSkTW5gYnMIGNIvokmLd2RtWo1bN_XQ9_mW4tgcbM3AY_pseLPMexeh3FBGCJeM1p3LCuae5u9maQ532y24auy8ciCNLO4Z7wB3fqPITF8V1SmyM1Ivjhm8G3f3GYoUvPOpEdw06har0uRF7Ln-bIJywFUij5k2a8yt_TY9AByRyok9GaQF6G5Ku_omnGALHLE8uya9US0SZUoJt9BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qndnMYldQ5hPIs-F_i7iJsU9izdDqNRsJEFc6UmZ9apjRnKU8B8XiA2yM3VTfJ0qQCwchVn2plNYVJhOYTCx8aeO6qSMg1x4iz3-nKBRgqyI-ZV0SQxLbSyAXS7rmTDJPJVyGGLPfeSvhIKJmBEuNcPX12nIdyQl2wc3mMRsuOgrnEsxOmgtmhqHPwRCprRQTVeNr29M995WSYHwW_OoPpnhgVEnJVZdMZDK8ZcE9dmeSSiSUX6O4xFFcVAhQPZPDteYgQS09OXkvNdSLNvlDDrCyY0JRPDDwMZfUuSV4nVAoRK1lEVkNcqQv8Ihkv3vAMKa4nMu6IpVXTAvh_0uNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC07RKBvt7fYLpnN8F1VZeZ7ELnLH6paKBLNDy-sQ6BKoEv63uydpuZubftYrCC90s51FKDyE-mgF8Sze3-WsAwWMxbDsTjuf_Zhh4GoSHr1YJfPBgpXP7vXkjgSOXiBwbjZ2T527mSKrBdDbwPWUMOLbHB9vKnzy1JEtNkXmJO2yeOnlehl1TRF0JhoBhGzXwNhdcR7pLfz3Wh_2rbSs1_9lK72C-sO0-TGHESPKLntykv4SNSxKMNn-Q6x3cK28z8-Siov33QcOa_M_tVBrOfXNEIyhDgMwAfo4-ZzGtklX3VXRjYZy6zIxKC5H-I66HrD2NXfSK_l9Z2u-YI4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=RNmKtuAPK0_V4GjNjTz6lV7IsOHY38MrHU1LDctfJokNrC4i-rNdpSSwzcgoc6PT7jCkLSxT08_9NJLWPwZjX32fTnpnrc03-wA-YYdhEOU7ROPY227efSt1YDHGTsYqV3i7M_SRLohrpyXgwIqmsM0dOHdrKfymgwFhZsMMkVg526ScL0ZbONkX-imr3B-usnigG9mtw8UwseltucToF_Ciaf0t1zNujie0GNjjgxxKWEKkX5lnvNTzmU1Gh3USC4bpXgx9Az63GVh1zi_f8gyFGfHvE-PYofdJZ-z25P7x0R0s61j-AYceR7Ov9bMgLx4ZPn9ixqHfkok0-Fr5VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=RNmKtuAPK0_V4GjNjTz6lV7IsOHY38MrHU1LDctfJokNrC4i-rNdpSSwzcgoc6PT7jCkLSxT08_9NJLWPwZjX32fTnpnrc03-wA-YYdhEOU7ROPY227efSt1YDHGTsYqV3i7M_SRLohrpyXgwIqmsM0dOHdrKfymgwFhZsMMkVg526ScL0ZbONkX-imr3B-usnigG9mtw8UwseltucToF_Ciaf0t1zNujie0GNjjgxxKWEKkX5lnvNTzmU1Gh3USC4bpXgx9Az63GVh1zi_f8gyFGfHvE-PYofdJZ-z25P7x0R0s61j-AYceR7Ov9bMgLx4ZPn9ixqHfkok0-Fr5VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qadAB3R7xbieVm-bIEy-7zt2TNOnrmCYy7fKIsacoXP0VSjUP6YXEvinlSiP6meWwtoervDQjRcSY29gq5_1vZo6Un0BvVtWV2__rpRTCdPRvr9KynBYxLHc35IDfpttxv5IAUKyOoScT7gz8erqhdOkVtj9_cbRQxRobadwNxpN7k7-hoxJLAMVq0ilqdB_FlYRgww1qJuCIkc-tU8OrQTyz7k0uefZfigY_9lIo5NN0UUiTaytcJUH1c-YV-IjHZJb2sywuaGDoYVQk3SuL1kTCSjmb2KTDn64wMvfNQXLwUdn5T1bXz53V4OwTbGcqhJFQN6AxRrKF7MfrSf-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu8biM5CPJAegZ3__sopxqlOu3qlBZZmY_BLmDdWeJMx07Vscbw3iW0ylfpvOyjd4089n2JgF46GQEkV4dMNTxKxi3_FZNTGfCS4iMS38hJH3ZtOTmCxofkNMGQ5GlR3V_tHLrvCKrnNwFQdPmQ4TSQLSqWwrXjwCGxT-KIv1VZ72wR5pDOg8q6HfshXEKeMAcdCFwK-5qpJ5NjmhmEo1w1MZbl5rbpG1i4-8LTaWJMHfktFqkjCOPsDmMnQ-CJ4-lGfc1g-lnq_-uL2s56xC__1DPrLnM4h8RkDzDjKoGC93AmTzE_EL_BqoZJFwdsXHlnUl7rWN8scBoypM3RTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKV0t3J1EGPKs-O337_rkvjehtUPpviLzpnM9TBm5lGI1QOo2xZCPjMrm5e05m1jTOyxJtxeGifRqJJ4ebo_iGg_TvozmQsxtxp3Gn092P64e8Wbo0gtz-rU4wSUu_GQ0_oQwUxqaf37mp9Lih7WdormvV0K65Zm2mPeLrZA0M9oqD-71Ia_NIstRE2DGak2kohWoJ0QrkZzgayjVgHRVWJHQDyyT5pifWcvJap97m3fWvNr3wu5fNfMEk3nVVJTxnQ-J9Zv2AqVpPT7j8JjXoxwx_f-4bk6ygjxTPEUJiv_WWzv921om3HRrAdk0nY-CniL4vNWbbrdVt1MfTEUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSletHNxdSch3v4Et7cDz5xz3AENctPsQke1exF_I6rMH8GWqLZxD4WHjxHNtKa7zRo7tbEUF6hidkBlNu3Z8Ql7jkR3-cIUZF_M-t63KN9D5gOH5Yq82Cf0Y4pXzZi1J8wwvczaNpgDLqXCQl3CRvexhG__7rx-EQQAjk9OlOnPO0YpO-n_n9auymfA-XC3d0m8D4xN4kSu1_S0xv0R9uSDaN22rL2ucPMz0cIsHd_YjLzfOoIJ4O06n7EMeWfgM8embmnfylLwSaM_9u2vx8q6btbvGKEHm5dkG98KyF4WHTbCfeLyc2azuRJAK9BRJ53ZbE04q66nhwk9zXMX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
