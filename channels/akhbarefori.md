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
<img src="https://cdn4.telesco.pe/file/hz1dAJAz7YUKMn4vI8n8wN7bI4_Yn8SDCs5GkSkVTmPAybU9qVca62UqqtJOxMys8T4hAMqvcnAURn6BduFGp4A8J_BtUWJCYByslbIfZez0ErOErVGwMizN13ur4TQFdBtWRdRt_hFwALlKUrFZMeatzWOeGSxt1psgIZLMHai5861tOwfEvRQP7WSmciPjZXQQEG_oLQkRYnrtKIhmotdp62tZKGKMBzqIGcBkLRm4IMM044TJlmSV_aXyAEgaRMLLbfKBbP0gO83345hIdGmxTrNOn6Q8KVwyjBRFYJf-QV0cmkfd5XfgA-vcMApwGCMGYju-3NLkjUSJRZ4R9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-658497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVStYOQoR08ighijEz2g7S7s85mUK9as6r0NNt1CUKxzP8Qn_m60I8whBhko8XrCqCYCmkNVNKJ2FJpJzh3NMmvmcspnurdPNqHBC0VJ0WCdxuFmbrRk8BhsKFvEO9nr_dyj6UHifuGqXbxErRX-dgoDf08_ek31MxCfFTrz49MZ-WA4oqPb25eIHax_JMrwtggtyI-JgI_jgpuQzcW9HXH74sWPCmhQPdxEuPypz4zBNDaiza28TN4r_HmBt4HJGWuwxpwnW8yo3F1ee6eITaIAkj0boygAOALDiIgeWA_a-24w1vgrEFLeQVTLboX59Q2uwzu6dE2sLTkuaHHxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: استراتژی‌های اشتباه و تصمیمات بدون فکر، صحنه بازی را به شکلی فاجعه‌بار به نقطه صفر برمی‌گرداند؛ زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند و مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.
ایرانی متفاوت خواهید دید!</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/658497" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
♦️
وزیر علوم: مجازات قضایی و انتظامی برای کسانی که در دانشگاه پرچم مقدس ایران را آتش زدند
🔹
کسانی که پرچم منحوس پهلوی را در دانشگاه برافراشتند و پرچم مقدس جمهوری اسلامی ایران را آتش زدند، از لحاظ قضایی و انتظامی به پرونده‌شان رسیدگی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20 · <a href="https://t.me/akhbarefori/658496" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای الحدث: نشست قریب‌الوقوع کشورهای میانجی‌گر واشنگتن و تهران
الحدث:
🔹
پاکستان، قطر، عربستان سعودی، مصر و ترکیه برای ارزیابی تلاش‌های میانجی‌گری تشکیل جلسه می‌دهند.
🔹
نشست پنج‌جانبه به دنبال یافتن تضمین‌هایی برای اجرای توافق بین آمریکا و ایران است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/akhbarefori/658495" target="_blank">📅 18:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCU4GZVwe5GpvSqzXrbWW-jIDv_dU1HfkdDJBU-QMMPBzXOTbWxRkrF0dU0cddO_sjwSJYEUpPo1YsLokC5nZ7ut8ZtzZIsh4BdZ7OyuaTO_8KQPFpVuAhRH164H_Iliz2HEKa4_cTsgy8su6HYinoM9kt-438fHdtj8yyfTnNfH7BuhwDU6VH1g0grSSI4BjgqqgjWneoVxMLLlBjvNMeINygRlYtnF9GXUZl-WfgrpaKPgG3CjJWSqGrJ9EWwgw3x4fYvowwUZZ2K7_b4j-WLp2ukHOqFbZYePbhG_EKpsRHlIgVFhn1v3gRxjTiW6cDzipRWPPiLhoKczaXp7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/658494" target="_blank">📅 18:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تخلیه اضطراری طبقات مختلف پنتاگون در پی هشدار امنیتی  سی‌ان‌ان:
🔹
در ادامه حادثه امنیتی امروز در وزارت جنگ آمریکا، عملیات تخلیه پرسنل از چندین طبقه ساختمان پنتاگون آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/658493" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پنتاگون در پی یک حادثه امنیتی تعطیل شد
🔹
وزارت جنگ آمریکا، دقایقی پیش در پی بروز یک حادثه امنیتی، درب‌های اصلی ساختمان پنتاگون را بست.
🔹
گزارش‌های اولیه حاکی از آن است که این تعطیلی در پی شناسایی و احتمال وجود مواد خطرناک و مشکوک در محوطه ساختمان صورت گرفته…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658492" target="_blank">📅 18:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پنتاگون در پی یک حادثه امنیتی تعطیل شد
🔹
وزارت جنگ آمریکا، دقایقی پیش در پی بروز یک حادثه امنیتی، درب‌های اصلی ساختمان پنتاگون را بست.
🔹
گزارش‌های اولیه حاکی از آن است که این تعطیلی در پی شناسایی و احتمال وجود مواد خطرناک و مشکوک در محوطه ساختمان صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/658491" target="_blank">📅 18:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=k5XmWOrIMhgEiYXQxuRygxiBCI6LElqg16sQnM_KEw146rKyOQG7igE8aTr28w3pmgIflVZlOArLW13tNgdg6FHsdUNITU4p6DsTw-JDSSpgNs-3vbSFFsCTn9aGx2tnSk5uDhQrJlIExrl-5rXv1kmZsxvzl_npAn3L0DYHdgaENNpi9NCnCoYmLD9mPhX5-pzqOa3k0_vN8q0VJjDjfifCQzxFuQes7ttaGWLDswQKvWFnevNts7gbAcaiDmihfsKWCUI3ooGAf2bYXmAtnjzauodlWerQDXMCwNmTZwtVuG9aEl6sH7xdrM0YR153Jy2xTv9auRP2WOanblUJpS8LhNyknv00PTFkXyQ_RpGNiDjvhbkCGTPTWmcdVRB-uNh3e74yYFWaLquOoHy4N6JNNJITNzwOZ0drCX8WVHTMR6uKiRjpx2PxTK0xfQS_6-I5oTDsKCaNmnnPIl8mEIaisuotqCNBbTMu5LE9mq8ypEkhHhKXwJX8-w3wmbEUGPRRcApxcKFEqPoWqdvVOgfnDf51tI1MZ3k-sv7A8SCcD10xCoVIw69ALvdxwDMbrR0Rd5YEr3_IXX1HWnzxlfvxlmKzaojtr-mcHT8nhmnUVBBS44HpFD5OrD6i6Gmd2x-HZCm70KWSyi7BygYXbw87o2G_Ewk31mWPUSL9wtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=k5XmWOrIMhgEiYXQxuRygxiBCI6LElqg16sQnM_KEw146rKyOQG7igE8aTr28w3pmgIflVZlOArLW13tNgdg6FHsdUNITU4p6DsTw-JDSSpgNs-3vbSFFsCTn9aGx2tnSk5uDhQrJlIExrl-5rXv1kmZsxvzl_npAn3L0DYHdgaENNpi9NCnCoYmLD9mPhX5-pzqOa3k0_vN8q0VJjDjfifCQzxFuQes7ttaGWLDswQKvWFnevNts7gbAcaiDmihfsKWCUI3ooGAf2bYXmAtnjzauodlWerQDXMCwNmTZwtVuG9aEl6sH7xdrM0YR153Jy2xTv9auRP2WOanblUJpS8LhNyknv00PTFkXyQ_RpGNiDjvhbkCGTPTWmcdVRB-uNh3e74yYFWaLquOoHy4N6JNNJITNzwOZ0drCX8WVHTMR6uKiRjpx2PxTK0xfQS_6-I5oTDsKCaNmnnPIl8mEIaisuotqCNBbTMu5LE9mq8ypEkhHhKXwJX8-w3wmbEUGPRRcApxcKFEqPoWqdvVOgfnDf51tI1MZ3k-sv7A8SCcD10xCoVIw69ALvdxwDMbrR0Rd5YEr3_IXX1HWnzxlfvxlmKzaojtr-mcHT8nhmnUVBBS44HpFD5OrD6i6Gmd2x-HZCm70KWSyi7BygYXbw87o2G_Ewk31mWPUSL9wtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب الله منتشر کرد
🔹
تصاویری از عملیات هدف قرار دادن سربازان ارتش تروریست اسرائیلی در شهر خیام، جنوب لبنان، با هلیکوپتر تهاجمی ابابیل توسط سربازان مقاومت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658490" target="_blank">📅 18:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c91665100f.mp4?token=VI5A2I4zOHwmvjINVEydk3Yb953jm-PYpZn2PfFyTfr5pnTQHEl45tc_0hlUGK4zvFtdBguIG5mHXZoeK2xFF5jusGsJD1bW10ezvZf7FiYqfzH9vgFMyBt1rO1DJ0QlVNTwqsn6JvL-BEbm_QQES178gPJBu_smNk3eNnYwNdrHol4wAnzpyOY1QOdY8es6WL4QdF8PAv49AbOtSafJRy1LTP96r2Ke2GTU9-_FRWKQSGmMzy8lck8673WmEDfEB1Zom8qLhwbSQW5V9NqgYoSJnas-ljMD-MEM9xfDnuwG8oP34tfcwiEUdLl8IpCiBFhNiB6gQsX2_qG_o0vjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c91665100f.mp4?token=VI5A2I4zOHwmvjINVEydk3Yb953jm-PYpZn2PfFyTfr5pnTQHEl45tc_0hlUGK4zvFtdBguIG5mHXZoeK2xFF5jusGsJD1bW10ezvZf7FiYqfzH9vgFMyBt1rO1DJ0QlVNTwqsn6JvL-BEbm_QQES178gPJBu_smNk3eNnYwNdrHol4wAnzpyOY1QOdY8es6WL4QdF8PAv49AbOtSafJRy1LTP96r2Ke2GTU9-_FRWKQSGmMzy8lck8673WmEDfEB1Zom8qLhwbSQW5V9NqgYoSJnas-ljMD-MEM9xfDnuwG8oP34tfcwiEUdLl8IpCiBFhNiB6gQsX2_qG_o0vjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ترامپ برای بار چندم به اعلام پیروزی ایران توسط رسانه‌های دنیا اعتراف می‌کند
ترامپ:
🔹
مشکل این است که این می‌تواند بزرگترین توافق تاریخ باشد. آنها می‌توانند پرچم سفید تسلیم را تکان دهند و بگویند «الحمدلله» و رسانه‌های جعلی بگویند «این یک پیروزی بزرگ برای ایران بود».
🔹
این دیوانه‌وارترین چیزی است که تا به حال دیده‌ام، ما داریم آنها را می‌کشیم. این ماییم که داریم آنها را می‌کشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658489" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
حنظله از نفوذ به ارتباطات مرتبط با مقامات موساد خبر داد
🔹
گروه هکری «حنظله»، امروز پنج‌شنبه اعلام کرد که موفق به دسترسی به اطلاعات و مکالمات مرتبط با شماری از مقامات پیشین و کنونی در دستگاه اطلاعاتی اسرائیل (موساد) شده است.
🔹
این گروه همچنین اشاره کرده که به داده‌هایی مربوط به فعالیت‌ها و عملیات‌های سایبری دست یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658487" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA_kHn0ByvNP7agiLYEWQZa0O14c4UFwlyF2_57H_FB9rZFnZLT2tkMgphXXEHjf7lfOUivsnR6roiMEazxmmSVz4e1PqmODxGU90I_TwIIP5n_aeW6lWVfFg_5fXpoTRF0YgzCHgxjBbw4iyTS3JJI_HU33nmzAU2d5Hsc_xq2RJG89HAH9PnQzD-VtP4LMqpPZ2mV_qgHIVUISjvDpx-2fAzsD1CbinRnQtM_6J2zX5c7fFMkEKtGQCRXbRFhMoo4hhdCg_ijqAGUqcDM39tdsBDCRG9fL__74Q0ayJDkFbYzT40Ej14SoI0OBgQOaWm0pCGLw19fIp3YpQfrgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/658486" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cc32c8bb.mp4?token=BEmFxP_yhn1R-4d9JjSxMtUjD7dv4PN5e--QdSyvl1ffSu43SeCr65594I3ty4z-dlol5c6pfNcGON4FYJhl6lJNeZZhnB8Ry6aX5Kklet9UmLhXSybNAOZbLFB0LKCKUzvNvMcYsQKS0gfIK1drfdpkHXJCKkmik9CRHaI_VStTJkGJFK67jSAbYe2MoyIexLtN72BnHzijv4sWTXqTFLCAa1rlojx_q2TpxMMuX5N-vI4oszy_F0ZvmhdvWxpY709NRVkhJuAWQlfqk9XHVhzODMDrSH16Ghsfw0ul_oEVkVIJBvhpmu1MzlnnAui7mC0eIpM09dCF-d48rLX7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cc32c8bb.mp4?token=BEmFxP_yhn1R-4d9JjSxMtUjD7dv4PN5e--QdSyvl1ffSu43SeCr65594I3ty4z-dlol5c6pfNcGON4FYJhl6lJNeZZhnB8Ry6aX5Kklet9UmLhXSybNAOZbLFB0LKCKUzvNvMcYsQKS0gfIK1drfdpkHXJCKkmik9CRHaI_VStTJkGJFK67jSAbYe2MoyIexLtN72BnHzijv4sWTXqTFLCAa1rlojx_q2TpxMMuX5N-vI4oszy_F0ZvmhdvWxpY709NRVkhJuAWQlfqk9XHVhzODMDrSH16Ghsfw0ul_oEVkVIJBvhpmu1MzlnnAui7mC0eIpM09dCF-d48rLX7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همیشه دنبال تصرف خارک بوده‌ام
ترامپ:
🔹
ترجیح من همیشه تصرف جزیره خارک بوده است. راستش را بخواهید، نمی‌دانم آمریکا جراتش را داشته باشد یا نه. اگر این کار را بکنید، کلی پول درمی‌آورید.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658484" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafc936097.mp4?token=gWPG-Ql__jVKGrtB5AlfSZ6Mkc9HZj7JEUMPfse5t60q7TLu5GCHRjU8bUlMqzVZnsgM2di_XotNQVdQHc-XlB26GmCO9dM-wFhrUePY7o5v-CZYHzWYp_HEX2YyLEmhYhmjmR6zhIbAZJorL0ebVP7KqFvHB71TRLMx87VUpmf9rOF9jMMENiCD0SShOZMJM_dKcLt8AFp5SP5p7hNhtTpEUtOXVhUF7iWEkDBx_VyfpaAS55ZI2457wZlKDCC-hRoOg0tBQEl0lAF0GkQFao_34-j8QhcaKpAi0SQ4bJ7Uf-kYmap3vyRinE_bKtdJRnn2kVhRDlNQKRUkvLtAaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafc936097.mp4?token=gWPG-Ql__jVKGrtB5AlfSZ6Mkc9HZj7JEUMPfse5t60q7TLu5GCHRjU8bUlMqzVZnsgM2di_XotNQVdQHc-XlB26GmCO9dM-wFhrUePY7o5v-CZYHzWYp_HEX2YyLEmhYhmjmR6zhIbAZJorL0ebVP7KqFvHB71TRLMx87VUpmf9rOF9jMMENiCD0SShOZMJM_dKcLt8AFp5SP5p7hNhtTpEUtOXVhUF7iWEkDBx_VyfpaAS55ZI2457wZlKDCC-hRoOg0tBQEl0lAF0GkQFao_34-j8QhcaKpAi0SQ4bJ7Uf-kYmap3vyRinE_bKtdJRnn2kVhRDlNQKRUkvLtAaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین بی شرمانه ترامپ نسبت به ملت شریف ایران؛ در حال متوقف کردن یک ملت بسیار شرور هستیم
ترامپ:
🔹
ما در حال متوقف کردن یک ملت بسیار شرور هستیم که هزاران نفر از مردم ما را کشته است. اکنون، ایران در موقعیت نهایی قرار دارد آنها چاره‌ای ندارند. تنها نکته منفی این است که همه در مورد آن اشتباه مینویسند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658483" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607e2db7d7.mp4?token=pSYt28EaADyiRg7AEn51mY8yceNgUkp22-H-zJF0oaH_huxb4MvvyxhmoqBym_FrIJA9a4im_KidDrWA6x1R57i0MBBfd8-LEyGhZvyqlIsux6mYRIGkfjTPj4asmamrQdJzrbAHnZ6A4s5oUWQ91R813-aAlbuz8_FmGC82Qynfb3YI6p6FO1kZESipssxHxpzQkeNktCYoddu_HhcqfPSqZw4Sc7Y23cVWLapHaaHOCstaFCCzjeFs-YzXhQgrq9gfy-fWO5HtwjWyivGo48DYeY0ib1Xvkz-L07ZLEM_hM3sjf2y4hJvxsmdCXvw8tF6mYrLaToNh8J0y5UQWOXO25m-k46iTgeWDJN26OBWKIGKSte4f1VLbhO3NRss2cdsMtY_uWyYlI-Z3MW8K3V01rnmSuemCg2WpznwKJgrhNNe9eiywOuJCOEH--CvZFa85VHl2Y7dccx1RBMJIRPJ0rrm0HENlclzdBiXH4n6Wnt4_jClfxdX2sGPn1_ZSvXgdeyrndnlyzY4cmdERtbKCWrQEdk9y78DsU8V1nU-t9D5fKO5P9yu2Pj4q6auCY0exzvZGiPQWSYzBkFaJVQ3gr3iE6C_9NXY8OK8NpgZUVSyws_tg5h_VS3MAX0TYBkkP_ewvg1PRLja5kLITeav4KfDC59CeVrxrsMDQIUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607e2db7d7.mp4?token=pSYt28EaADyiRg7AEn51mY8yceNgUkp22-H-zJF0oaH_huxb4MvvyxhmoqBym_FrIJA9a4im_KidDrWA6x1R57i0MBBfd8-LEyGhZvyqlIsux6mYRIGkfjTPj4asmamrQdJzrbAHnZ6A4s5oUWQ91R813-aAlbuz8_FmGC82Qynfb3YI6p6FO1kZESipssxHxpzQkeNktCYoddu_HhcqfPSqZw4Sc7Y23cVWLapHaaHOCstaFCCzjeFs-YzXhQgrq9gfy-fWO5HtwjWyivGo48DYeY0ib1Xvkz-L07ZLEM_hM3sjf2y4hJvxsmdCXvw8tF6mYrLaToNh8J0y5UQWOXO25m-k46iTgeWDJN26OBWKIGKSte4f1VLbhO3NRss2cdsMtY_uWyYlI-Z3MW8K3V01rnmSuemCg2WpznwKJgrhNNe9eiywOuJCOEH--CvZFa85VHl2Y7dccx1RBMJIRPJ0rrm0HENlclzdBiXH4n6Wnt4_jClfxdX2sGPn1_ZSvXgdeyrndnlyzY4cmdERtbKCWrQEdk9y78DsU8V1nU-t9D5fKO5P9yu2Pj4q6auCY0exzvZGiPQWSYzBkFaJVQ3gr3iE6C_9NXY8OK8NpgZUVSyws_tg5h_VS3MAX0TYBkkP_ewvg1PRLja5kLITeav4KfDC59CeVrxrsMDQIUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو را به هرکسی می‌پرستید هوای پیشکسوتان ایران را داشته باشید | همین حالا مجتبی محرمی نه درآمد دارد نه بیمه است
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658482" target="_blank">📅 18:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af52ba85d3.mp4?token=Vc2rQgqI47gJfTO_x6GGMyAsoXCTWuHJD41Yd8alWpFQdquCNnFMGnzP_sNvPZXtAj7xsnAhAA3hxih-8vCGw_ryDx2KgV5Gh_uO-G3TXsUsrtt3FNSEd-JlaSCkcbAwiycuNjEwJBS-QFFUI-vgwZzz6Fpk4kAhcLE6d2LucK8misxUGr2CCD-0NLP5X7qIQoHWKQiKzM1loV2MDTyeo7ytkLVGwMWM7pKzmZLnGpVF2bxJdwRNKsdJiW4pWcm2ytsRKHqtVl27wyMvZJEHaH5w8hI0stol2iwYWKGrr3azv08ewGc7nzRwyYjKeR2Xccrf4SmemNQn4t7mCfWY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af52ba85d3.mp4?token=Vc2rQgqI47gJfTO_x6GGMyAsoXCTWuHJD41Yd8alWpFQdquCNnFMGnzP_sNvPZXtAj7xsnAhAA3hxih-8vCGw_ryDx2KgV5Gh_uO-G3TXsUsrtt3FNSEd-JlaSCkcbAwiycuNjEwJBS-QFFUI-vgwZzz6Fpk4kAhcLE6d2LucK8misxUGr2CCD-0NLP5X7qIQoHWKQiKzM1loV2MDTyeo7ytkLVGwMWM7pKzmZLnGpVF2bxJdwRNKsdJiW4pWcm2ytsRKHqtVl27wyMvZJEHaH5w8hI0stol2iwYWKGrr3azv08ewGc7nzRwyYjKeR2Xccrf4SmemNQn4t7mCfWY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت دو پهپاد انتحاری به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار تروریست‌های تجزیه‌طلب کُرد در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/658481" target="_blank">📅 18:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxne4YZ7yarV18v1hQRDF1149Z6vYChbrTBMRR4qQQsoFz47JvPm6_RTifDMrHAMci_sEIvPWWBspJ-7sOb2w-2xfQUr1j3zMpTWAMgc-YxS6NmltYmiUY4JK6BEp23YV99uPx37VO7W2YN9xj9kGf5FVmHtz9DXCbOVELp_4T5xfO2L5C044HrYRLXcSKiPsduV8xq-cACnP9-PjzGK15BMudCBfWN3UxJrGB19peGsr7QIkTEEv-psmkkrtAp_bMX9Ws2GJ194Wimwg5l8xpOfB_wjP_NTNE2z3MQ3SEW2XW0qOkAAnrtnDvzPJoQQhdXETewpSA-orF6Fb89KFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهستی گنجوی، بانوی شاعری که نمی‌شناختید
🔹
مهستی گنجوی تنها یک شاعر نبود؛ او بانویی دانشمند، موسیقی‌دان و چهره‌ای فرهنگی در عصر سلجوقیان بود که در روزگاری مردسالار، با استعداد و دانش خود به شهرتی کم‌نظیر رسید. آثار و آوازه او گواه حضور فعال زنان در شکوفایی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/658480" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای بلومبرگ درباره دیدار امنیتی سطح‌ بالای ایران و امارات
بلومبرگ:
🔹
ایران و امارات نخستین دیدار امنیتی رو در رو در سطح بالا را از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران برگزار کرده‌اند؛ اقدامی که نشانه‌ای از تلاش برای کاهش تنش‌ها توصیف شده است؛ ابوظبی برای حفاظت از اقتصاد و سرمایه‌گذاری‌های خود به دنبال ثبات است و تهران نیز به بهبود روابط با یکی از شرکای مهم تجاری پیش از جنگ علاقه‌مند است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/658479" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7accbfba0.mp4?token=EKIwJ5T11c3_XikeGTaVBZ8a4Gr8sDvzQUXcjs7_qcJKik9e1SIxnIlZ9rrqGSOsKPm8sIqLz79lJCrb5fT3H-Jm1Vpr3xRq-h3GCoBKyn93OFMNtfVewJACsGTEvn-kAlU2jE3k29ROAx2GOUBJGxVvsYRukqfQin-GFLLjSCOkXSbyYXFIIxVCQEFm82xpXu2crMdLFWPPVCm0Ni52ZSZrxiU0DVw-8vF9VJnhe79JDwz-xUOZcBS_PQztsivBZHR1zyP0-2nmzKOwUUn9yKzp39plGtOpU4TOmloct6YRAhi6nxCSRx9m0H0O0Zm6vi-hPfiyYgXfNrqjI1sgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7accbfba0.mp4?token=EKIwJ5T11c3_XikeGTaVBZ8a4Gr8sDvzQUXcjs7_qcJKik9e1SIxnIlZ9rrqGSOsKPm8sIqLz79lJCrb5fT3H-Jm1Vpr3xRq-h3GCoBKyn93OFMNtfVewJACsGTEvn-kAlU2jE3k29ROAx2GOUBJGxVvsYRukqfQin-GFLLjSCOkXSbyYXFIIxVCQEFm82xpXu2crMdLFWPPVCm0Ni52ZSZrxiU0DVw-8vF9VJnhe79JDwz-xUOZcBS_PQztsivBZHR1zyP0-2nmzKOwUUn9yKzp39plGtOpU4TOmloct6YRAhi6nxCSRx9m0H0O0Zm6vi-hPfiyYgXfNrqjI1sgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش ربات‌های نظافتچی هوش مصنوعی در چین
🔹
چین در خانه‌های پکن در حال آزمایش ربات‌های نظافتچی مجهز به هوش مصنوعی است؛ این ربات‌ها در کنار نیروهای خدماتی کار می‌کنند و هرچند بخشی از کار را سبک‌تر کرده‌اند، اما هنوز به کمک انسان نیاز دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/658478" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658476">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR6d-ZMLOI6G-hmj0yKa2V-NdiqS95i9wzBFrwbwxe9m1AFWIFYD58n358I5bq7hWyH-2tpWLZkTdHSOxi7ooxne8YfI9lnwLkorWek8a2GpgXzRRJUzAAUm8Ff_-HOODo7EP9WtM4au6adjfgLbaASwpGxvB09keqylT8G6RB1E1y76VhSiroy72G1qwy3F79Rg8BGuIF3DkJDtEsMoMVfqLWoRH68c7AQuwNmUChZ5ji-nNDKriySxvaWPHkCUKgxI1SJXGglYsHml_n-RE0pOHDeupJaoS2u7J9tcRfh25rSBIE7NpS7dN1Dbgcjpro0X7Y7DGpjWjkYDAUP3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBwpasxEyCblyhZ3hCiLwQZFeEDkHZ6kznHSXL1B6FWHa4qmtT9scjBSMZbDFrnLZGrt2vJuF4ZkR8ChB8Hw4h8AZU54rwV3kqBLa_hEIy_W8IAMPAMTwJyRK3VmDDiMuk2hsxtpvgmNEFhZYlBmaw8hOhj5o6zmu3F4TRuU8MLuo4duxE2GhnVi_PsZxTBajjdQMbQx0mzB9cmfg9_nn5S9zP3tLqlvEs37vNTJ-4JXl7boQJtRTcOIuoWR2kpQZUR0Qfzjs7PcbRc6ZrFGTfDiSRCkE7eAVn8qf7zitIjyFJ9_U7iED5KSuDQOyvybHcG_0XF4XudUDF3_ciS4TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از ورزشگاه آزتکا مکزیک پیش از شروع مراسم افتتاحیه مسابقات جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/658476" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658475">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYrF0QXq7K4Y80k6cX8Vmvs_RQQBVYcvOPwhMw2qxHS8P_U2QRqSBgrQuzBH5hsWQdzwZPf9F-VyhlN4TYaK69qIJf_fMTY-j3puj_6XyrfjCJwJTuNBJicvhlN0EA7H6-Fv90Oxvt9OPyaIQw15mC2McSWvtWjhbra52xtaBG9ZGerz1y70SUPdiYBAkKA9t8h9sjUJR8kcoEqWvC8CKFdI7lF-jhX_9BsTTY3L3HJv7Wl9XGtb-hu4Kb5BFUiaouZVG0nYpcVCXqva9RNXck3cacASqohtfO-HO-8All1RrI_MUekOOTA0wZTak_VkRqPa0HG5CXJajWsTCZGgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: کارشناسان تأکید دارند که ایران با بمباران، تسلیم نمی‌شود
🔹
دونالد ترامپ حملات به ایران را از سر گرفته است، به این امید که تهران را تحت فشار قرار دهد تا توافقی متناسب با خواسته‌های واشنگتن را بپذیرد، اما کارشناسان هشدار می‌دهند که این اقدام تأثیر معکوس خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658475" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658474">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/041fe85849.mp4?token=Q0-K-t4oAs6FN-wXnOcLQksbgeS4VcF_QWMCmJQpwTMtw3rFsx38wMDdVMOMiuQCBpwPqqBtjrJu8iVPXqZCeSM4lNkiaQJXLxlUD0Aff1qRimN9044R3hQt5qceqNGPYbQKtQAL9ZjzD2DGV09RacflrHY5pku6f7odwbP-OpDvmixrpCOFQtOqA5S6RFk4gZWnBqUmNKcFDFjcKlWMMUcw4zA1WMsmSbjdPG8i3-Nh_u1DLYZeHexA-lv7t6-KLYv3F_6DhvT8rAHWeHrigdwvWx-JQno-vqy7BdXXAQmw8GSombxnzC5fW6CQvsUTGM8P4aUA6LLjUzaYPlIsfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/041fe85849.mp4?token=Q0-K-t4oAs6FN-wXnOcLQksbgeS4VcF_QWMCmJQpwTMtw3rFsx38wMDdVMOMiuQCBpwPqqBtjrJu8iVPXqZCeSM4lNkiaQJXLxlUD0Aff1qRimN9044R3hQt5qceqNGPYbQKtQAL9ZjzD2DGV09RacflrHY5pku6f7odwbP-OpDvmixrpCOFQtOqA5S6RFk4gZWnBqUmNKcFDFjcKlWMMUcw4zA1WMsmSbjdPG8i3-Nh_u1DLYZeHexA-lv7t6-KLYv3F_6DhvT8rAHWeHrigdwvWx-JQno-vqy7BdXXAQmw8GSombxnzC5fW6CQvsUTGM8P4aUA6LLjUzaYPlIsfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفری از این تیم ملی ایران، باید فوتبال را ببوسند و کنار بگذارند
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/658474" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658473">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
صدای چند انفجار در استان اربیل عراق
🔹
منابع عراقی از شنیده شدن چند صدای انفجار در اربیل عراق خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658473" target="_blank">📅 17:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8e764a90.mp4?token=DGC2zzFFUDanOawbMD1-H66CEpHRf3rOyjBxsHLLS1Cv7zba1Q7HjtiZeEUFdlbAVllDO8eepXdipv9-3URjwAgqZQOJY8sI_drPuZotqF9GltopCjTI2MKHilkHOFVPVDZWYmCXd-IPMq9tnn9Ko0kKFBsFbbWyk0Ws9yRtRuaCsrOg6o-7foOpzXQ8W5cz2rQg0pt-c829rqfGvnR2WmJaTvugs4TTKmvhM89vaQ1hh3mbmGzvhq8jgXAtjMmGVU7s_FfDgN0CY3M8U8TvLFr0EwayD4rgDuipUfZavFLmmw-ttCmPw5Qn65WW8j0syiY_hkA5kjluSrQKQwf8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8e764a90.mp4?token=DGC2zzFFUDanOawbMD1-H66CEpHRf3rOyjBxsHLLS1Cv7zba1Q7HjtiZeEUFdlbAVllDO8eepXdipv9-3URjwAgqZQOJY8sI_drPuZotqF9GltopCjTI2MKHilkHOFVPVDZWYmCXd-IPMq9tnn9Ko0kKFBsFbbWyk0Ws9yRtRuaCsrOg6o-7foOpzXQ8W5cz2rQg0pt-c829rqfGvnR2WmJaTvugs4TTKmvhM89vaQ1hh3mbmGzvhq8jgXAtjMmGVU7s_FfDgN0CY3M8U8TvLFr0EwayD4rgDuipUfZavFLmmw-ttCmPw5Qn65WW8j0syiY_hkA5kjluSrQKQwf8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا مکزیک است؛ چند ساعت مانده به افتتاحیه رسمی جام جهانی
🔹
با حضور صدها پلیس و نیروی امنیتی جو امنیتی شدیدی در مسیرهای منتهی به ورزشگاه آزتک، میزبان بازی افتتاحیه، برقرار شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/658471" target="_blank">📅 17:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emJ16fyptPnF51cSl2z3d5iCJ_QQnWBF0OGN_2YZ1uDUBR3VRS-BbEVM7xTzaCsH5HZUzts48y8MNL3n_14Ru3_H6gBQq2zTdSAxK2fjow9EQLlhFyMliF8EYiTxcWl9k6abxvyQiBHgwkW1muum742FtnM6inVBS8MzxAqq0s49bMmNwEmk5shEXpX5gfYvG1lOdTaowW_iGi9HcQgVQfF1atZEY5CMY1SiM7ZL-fpCUATrKisMQzAYR5DLkJ1Oc43yRGLp7l6cHZ-cgyYYo4R1TEZ5j_vRF5aWpKgcSS_Xo7u29u5Cxm4qCC51_WQdF5builX9ORAK-sTxCAd1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد مدهرست، روزنامه‌نگار انگلیسی: یک چیز هست که ترامپ هیچ‌وقت در موردش دروغ نمی‌گوید: دزدیدن نفت. دولت دزدان دریایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/658470" target="_blank">📅 17:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای
وال استریت ژورنال: آمریکا امشب به ایران حمله خواهد کرد تا ایران توافق را امضاء کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/658469" target="_blank">📅 17:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4616e0d1.mp4?token=sVoUC9yn8gDpA6_47-kXKySKmhecPmrEJIIpx4klG3ooUXlTeuvrktOP6fQdijnXD-VMrpxfPdpfZIVdect_Zgd7ubgRqn0ap0QJiULIW1Fte11I31C3lpE1D2YTXTxOezQQ85WYXSN89k88VehA3OuWbSVBUmJLOHyQ6_YDmXqln_h0sJTnUcQUY35hQsnWrnfE8cpCIJvcrnrQJKry-A94rIYnGECdjOUAqy-6ENMjhmuxLlinqjtwbGH8cs1McOunEyHubMeYl5HUgQy1LXpAIqgXDjomZzSc2Rqa-h6Jl2laLI2dp5WYcopMBLz2ShdrDm7ugM2OM8qSwkxj6yqsW9ZCGgeiAhftoCLs7hRZ4SM38U6Wa3CAKxHmhOZ_0hfELISoRxirQBfMKuOxf_h1VT3kb1kuVmVGbejNRE9IB3nDhj7ii6amvDZ88ScXZ8pwxzhnf1iSM4g_9ljYHJb5huE_4AK4HX1vxFmfsY_WU7-YfOFoeZ9ZXa7-ddIuU7SBLvNmGRD-_1tS_gDZa0DQhkLzBggQykkmyftDWSz-OQQrC8jGcWykRKW6mAksNjGtHQ_R3BsigUOhnM495lsha_OUD7qVBKEXIp1ys6xu1JS_4-oJTaOluzCDZKwnqlILJsrOM6kQyHH1elhHDCYhpUmL9QVBph4dZiLihCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4616e0d1.mp4?token=sVoUC9yn8gDpA6_47-kXKySKmhecPmrEJIIpx4klG3ooUXlTeuvrktOP6fQdijnXD-VMrpxfPdpfZIVdect_Zgd7ubgRqn0ap0QJiULIW1Fte11I31C3lpE1D2YTXTxOezQQ85WYXSN89k88VehA3OuWbSVBUmJLOHyQ6_YDmXqln_h0sJTnUcQUY35hQsnWrnfE8cpCIJvcrnrQJKry-A94rIYnGECdjOUAqy-6ENMjhmuxLlinqjtwbGH8cs1McOunEyHubMeYl5HUgQy1LXpAIqgXDjomZzSc2Rqa-h6Jl2laLI2dp5WYcopMBLz2ShdrDm7ugM2OM8qSwkxj6yqsW9ZCGgeiAhftoCLs7hRZ4SM38U6Wa3CAKxHmhOZ_0hfELISoRxirQBfMKuOxf_h1VT3kb1kuVmVGbejNRE9IB3nDhj7ii6amvDZ88ScXZ8pwxzhnf1iSM4g_9ljYHJb5huE_4AK4HX1vxFmfsY_WU7-YfOFoeZ9ZXa7-ddIuU7SBLvNmGRD-_1tS_gDZa0DQhkLzBggQykkmyftDWSz-OQQrC8jGcWykRKW6mAksNjGtHQ_R3BsigUOhnM495lsha_OUD7qVBKEXIp1ys6xu1JS_4-oJTaOluzCDZKwnqlILJsrOM6kQyHH1elhHDCYhpUmL9QVBph4dZiLihCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از آغاز تا پایان ماجرای حملات بامداد
🔹
جزئیات ضربات نیروهای مسلح به پایگاه های آمریکایی در منطقه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/658468" target="_blank">📅 17:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4uQgmRA4BGz0lYeWblCpnKBd3IkTWHupWLODH2FNgQ2yFicq_BZiRx012UJDSc0fOORzr9tPM5WDaIGPTbk-hOyI0E5LMVSH6piRyKQCPFGHSrw1zrCSMwGZU1pP_EeR0BWP9bVTWr6j-sPsMSQcHFkElAJUBLlOoUrqjUO-nob9EfS-NybePsM3MwL-jJSUzzkCQSlk_BeO7R55ki8GZ9VWbNBFeCRlpDuQn8rutsg7-eAI-1-JYhzA-MbmZCMtKloWYSvBiytfqKYydUkd6I6I3PRxBNK-e7BQL2d7Psk41bLvcl1Nxzge_NL4LwH9jafFiOwPcRHUYlJ-xnMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: دریافت‌کننده جایزه صلح فیفا یک روز قبل از شروع جام جهانی فوتبال، ایران را بمباران کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/658467" target="_blank">📅 17:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJOs3cf_7O56oRZTSeLzmjhOcB92wRO3mLiBklduF-HQfE8zttmWNWpbY6f5EvatbPqO1iWdzkMrItFArIzh2XHkgxy_l6_zTvdqZh2otqb3p8UaP4gQldpt1sbKXowX3kzi5AMiIVxsuHW3VTimn2Dfw_HrPok1rYhB6y5d2G9jl0d9YJil52iCY_WtrblwqSFt8R0avm6VoCoW6DMbejRxfsv94xZy61HBpfGqQbOxh8ntjdudq78VJl0Ly-vj-j3BkDk9i4UMb9zgGceASwVpAST3OISNxZKu0wEeHyR8xvoCADvjlVVOGCASwpWVyYtJMM4KdwLmt6TSnI2aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوگوهای جام جهانی از سال ۱۹۳۰ تا ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/658466" target="_blank">📅 16:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d414eaa82a.mp4?token=OsMKRxrc-Ne7gkkQ0BXsK8wd6lj02G-PFiSqCt8JeI2DfCyWdeskaa69BJBpt1DdAlQugd6sfh4kEhTrvDmPR4hGaF-vbZn5nQ3QBmRLuH9VDbOp8wZQz-epau0tfrorermM3bqlnDgJ3_fxE--1tHQpzZdGmnMoOhAQNseL5AVZxRydxFU_RpOSPRyaQP_7qEY6WMnlE5AqQHCe8C1nbBl8k3XAjKucQFtYE4mz5XbrXGqtZO2LMHI3az5tKLAoulSw64r4odRhpNd2U4pTvVYamnid8yMuYWw-qhuXWSYdpI6P9LKlqBYlkJs0OCHS9UNQzzGB8W8FOS0sd_LlAGKLyAgxwaDwk9kxMjna9egukgh4wDEdm7BkNCh2DiSjkxfNXTGYjONhSVOrVDzr5b2jhE52rz21de5NdimHVVeGcaMHGLAfrp2inHj3sf80lctWBaKnzlyppYcPx0SJ1H2G0KUgNC4Ha1VJ4pO0Z_u5JIAsYQHBp-0-JM-nR-IVT9YBRfdauq8RTQBw9dMZi7LdDKTsSm7lNLj_yxolvbBHZjsjSf_a7mDZoT12HpNFXxIp7gxsdRjpgurbdZiyXwi9_Ic5PXGqp-mkSaNZXcGcwuSvO6M33ecbKm6MK9tHvnnJCPrvMAnbf5hNRnGnPhnV2xZOVKZEiDDm0pg81mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d414eaa82a.mp4?token=OsMKRxrc-Ne7gkkQ0BXsK8wd6lj02G-PFiSqCt8JeI2DfCyWdeskaa69BJBpt1DdAlQugd6sfh4kEhTrvDmPR4hGaF-vbZn5nQ3QBmRLuH9VDbOp8wZQz-epau0tfrorermM3bqlnDgJ3_fxE--1tHQpzZdGmnMoOhAQNseL5AVZxRydxFU_RpOSPRyaQP_7qEY6WMnlE5AqQHCe8C1nbBl8k3XAjKucQFtYE4mz5XbrXGqtZO2LMHI3az5tKLAoulSw64r4odRhpNd2U4pTvVYamnid8yMuYWw-qhuXWSYdpI6P9LKlqBYlkJs0OCHS9UNQzzGB8W8FOS0sd_LlAGKLyAgxwaDwk9kxMjna9egukgh4wDEdm7BkNCh2DiSjkxfNXTGYjONhSVOrVDzr5b2jhE52rz21de5NdimHVVeGcaMHGLAfrp2inHj3sf80lctWBaKnzlyppYcPx0SJ1H2G0KUgNC4Ha1VJ4pO0Z_u5JIAsYQHBp-0-JM-nR-IVT9YBRfdauq8RTQBw9dMZi7LdDKTsSm7lNLj_yxolvbBHZjsjSf_a7mDZoT12HpNFXxIp7gxsdRjpgurbdZiyXwi9_Ic5PXGqp-mkSaNZXcGcwuSvO6M33ecbKm6MK9tHvnnJCPrvMAnbf5hNRnGnPhnV2xZOVKZEiDDm0pg81mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره ناب مرتضی فنونی زاده از علی پروین با تقلید صدای سلطان!
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/658465" target="_blank">📅 16:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658463">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: امشب بمباران بیشتری علیه ایران انجام خواهد شد، و این بمباران بزرگتر و قوی‌تر خواهد بود!
🔹
ترامپ: اگر ایرانی ها توافق را امضا نکنند، بشدت بمباران خواهند شد؛ عجله کنید، هنوز می‌توانیم به بزرگترین توافق تاریخ برسیم! #Devil
🇮🇷
…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/658463" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658462">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUCYCeH2H1iozaQPhbWr3D4_ZEgnYzn4lEWD1jajULVEB9K9qa9kmiwaP3fxLu508mMNyAyvssBmr3daCHyGWJ32O7b3pm-_21y00fO8CCmm9252zQ7XkmZ9F_N7mp6DJPo-RWwE3dwRP1mHZ1oaVst62zm8gbj8bLsb5iH1CEZfSKmNiHPZrZ-EwL25vsRE1G_uYj_A6wLrIU9vl35sSHHIWK7lNOahXkwd0AHmMbYpAOpq2U9BlXTI5HvUnLDay6DvwRmCaNYlh24m3wXEQKohRyDSOxsBvXxd2EG_hyOAiajP1vMpMjU7UmAENEtYf0e_raFiWArKltU2XVraiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ترامپ راهی جز تسلیم در برابر ایران ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658462" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658461">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ: ما با جنگنده و هواپیما‌های خود بر فراز تهران پرواز میکنیم و ایرانی ها از آن خبر ندارند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658461" target="_blank">📅 16:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ترامپ متوهم: مردم در ایران نمی‌توانند آب بنوشند و من نمی‌خواهم این اتفاق بیفتد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/658460" target="_blank">📅 16:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اراجیف ترامپ: پل‌ها هدف بعدی حملات ما هستند! اما من نمی‌خواهم این کار را انجام دهم زیرا وقتی این کار را می‌کنم، مردم رنج می‌برند  ترامپ:
🔹
ما برای معترضان ایرانی سلاح فرستادیم، اما از کردها بسیار ناامید شدیم زیرا آنها سلاح ها را به معترضان تحویل ندادند.…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/658459" target="_blank">📅 16:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
یاوه‌گویی وزیر خزانه‌داری آمریکا درباره پولهای بلوکه‌ شده ایران
اسکات بسنت در شبکه اجتماعی ایکس:
🔹
هر خسارتی که ایران به متحدان ما در خلیج فارس وارد کند، از محل وجوهی که از حساب‌های ایران برداشت می‌شود، جبران خواهد شد.
🔹
هر عوارضی که به نهاد مدیریت آبراه خلیج فارس پرداخت شود، با برداشت وجوه از حساب‌های آنها خنثی می‌گردد. هر حمله‌ای که ایران انجام دهد، تنها پیامدهای اقتصادی و مالی متوجه آن را عمیق‌تر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/658458" target="_blank">📅 16:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: ما با ایران در حال مذاکره هستیم!  ترامپ:
🔹
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
🔹
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم. ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم!
🔹
ایرانی‌ها بسیار مغرور…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/658457" target="_blank">📅 16:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ترامپ در مصاحبه با فاکس نیوز: ما با ایران در حال مذاکره هستیم!
ترامپ:
🔹
اگر ایران توافق را امضا نکند، آن را به شدت بمباران خواهم کرد
🔹
ترجیح می‌دهم جزیره خارک را در اختیار داشته باشم. ما هنوز به اندازه کافی به ایران ضربه نزده‌ایم!
🔹
ایرانی‌ها بسیار مغرور هستند و ۴۷ سال است که در خاورمیانه قلدری می‌کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/658456" target="_blank">📅 16:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صیادان هرمزگانی از تردد در تنگۀ هرمز خودداری کنند
مدیرعامل اتحادیه شرکت‌های تعاونی صیادان هرمزگان:
🔹
تمامی شناورها و فعالان حوزۀ صیادی موظف‌اند با رعایت کامل دستورالعمل‌های ابلاغی، عملیات صیادی خود را تنها در آب‌های سرزمینی و محدودۀ ۱۲ مایلی ساحل انجام دهند.
🔹
هرگونه تردد، فعالیت و حضور شناورها در محدودۀ تنگه هرمز اکیداً ممنوع اعلام شده و صیادان موظف هستند تا اطلاع ثانوی از نزدیک شدن و تردد در اطراف این منطقه خودداری کنند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/658455" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be5416d91.mp4?token=ZxebxnXM0ioXFS3rikvSbXo_QHjkEWoMP4ftTtHbWlAPDr0Z5PTOqaeovHeEdK1A_kUfUrpKH99vuPrt_TnVnYPIvpDZXwRx4DgaanOa2azMqsgCn7y_BVpNjpSvM_0fKGNFI884h_dZE1cdpetEOV7JQT45TpNha0zwCoG8n9k6YUHJK3zALBVWu0NfX7iNuzOS5hNRazq7CbnqbKdNFTwoJpqQUqhgAwYX2f-uGB4GcqRtTGzxSjYi8LkLExuijSeMr63d42IPTrvPA_EajNLdhI694a2SFDC9s3jEYS2Wh9pJ8mfaEUSasOeuvJf7sTABjN9TdmPYLCQdU_X-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be5416d91.mp4?token=ZxebxnXM0ioXFS3rikvSbXo_QHjkEWoMP4ftTtHbWlAPDr0Z5PTOqaeovHeEdK1A_kUfUrpKH99vuPrt_TnVnYPIvpDZXwRx4DgaanOa2azMqsgCn7y_BVpNjpSvM_0fKGNFI884h_dZE1cdpetEOV7JQT45TpNha0zwCoG8n9k6YUHJK3zALBVWu0NfX7iNuzOS5hNRazq7CbnqbKdNFTwoJpqQUqhgAwYX2f-uGB4GcqRtTGzxSjYi8LkLExuijSeMr63d42IPTrvPA_EajNLdhI694a2SFDC9s3jEYS2Wh9pJ8mfaEUSasOeuvJf7sTABjN9TdmPYLCQdU_X-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزدک میرزایی کارشناس شبکه اسرائیلی اینترنشنال: حالا اگه تیم ایران بازی اولش رو بُرد و صعود کرد چی بگیم!؟ اگر بازی اولو ببرن نمیشه دیگه جمعشون کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/658454" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3be75479.mp4?token=OAwNPmhzypLP9kmU1-WBhDGPSG81Mo6HzH3Ji2AGoQWaL38QqWk6SIYQXuzYK2RBrviyLuq493OP25OlRLOQ62_15ZENRYykISLhMprAntJiimctnf5u2NqBS0lCU4z1zKAsfhov5--n0dsgaDd8VGgf6e7ym6lSuvZIhJrz8dUQFt2e2xQKqYSCP9gerc2TFxLmOlsXkLz5I6TQT-mhBVPe__FpyKQRPTs6CZdQxEuJwl-EjvCDKzL8nyfTKJECT2NvUmlaq7gQGvILVguqGd4dTXAASEaUnnHUrOXEjXB7cgYVy8jsVa7vSnUBxaP6k1JK541HNBaCOzZ91LBC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3be75479.mp4?token=OAwNPmhzypLP9kmU1-WBhDGPSG81Mo6HzH3Ji2AGoQWaL38QqWk6SIYQXuzYK2RBrviyLuq493OP25OlRLOQ62_15ZENRYykISLhMprAntJiimctnf5u2NqBS0lCU4z1zKAsfhov5--n0dsgaDd8VGgf6e7ym6lSuvZIhJrz8dUQFt2e2xQKqYSCP9gerc2TFxLmOlsXkLz5I6TQT-mhBVPe__FpyKQRPTs6CZdQxEuJwl-EjvCDKzL8nyfTKJECT2NvUmlaq7gQGvILVguqGd4dTXAASEaUnnHUrOXEjXB7cgYVy8jsVa7vSnUBxaP6k1JK541HNBaCOzZ91LBC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوان‌گرایی در تیم ملی شوخی است | حاج صفی دیگر باید برود تیم پیشکسوتان بازی کند
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/658453" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658452">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nci8gLdtBKtWUEYaHjciAZMmBMQyxL8cWRo42bPvWbiEKpZbPV_iQnotVeZA4FArrzIIPrOLbH-fisneo4ON38L_V9Tl5XGfGL6Hmw-lCGtp3ibE_-3fXXRE5mtnP5PsujgMW-axNMR87w0r6yO1dBbJztIXVgHNl_IP6CjckwLoic7Zm7jOMzs__EJaDeUMUq4PEUGraw3GIiihONloRXoMKeRKvq6dGPmdiwAi2FoH-sSB6NranTbW9efyW6Cvj8gYIWniW1q7MGl06MYWBtMh3QHDIFuf7kugYbAMqIzpSbq8GQrZKAYeIuzIE2qAXkk9RMLPsn0eRnhFb8kcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف سواد مالی، تربیت بچه‌ایه که پول براش ابزارِ ساختن زندگیه، نه دغدغه یا دردسر #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/658452" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658451">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f645fb06f.mp4?token=PClSfQhjmI2jGf0oACqnXOQEWKeYPokxl6FOh3MgSaabkOg4aFVS-pKI3qb2U7Qc_bbf9qQ2mIgPKSEbHnrEsg_SCl7uuglW0-J0DSziNt26cIr_rN1VjLAWO9oF8t4gSlldJzAjvS96J-c1H3H4gqNpvRc_TjqbpwI2SLyDjhWzVpYQ2bF4atm6Nw2PDZ0O8bQ8Nvz2DltwBNRF_fijGBVxyfAYMyLAXM53BGh7Vd7i89K8VmPh6a3dOLGy50Rng4QF-2fpmZ7D3hDbdrLYglBXz9r593SUbvuJCNwVt8O8YXjmV7kpJEzUwjcl1oM-2Bie5iDF8W_cjQ08yxxsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f645fb06f.mp4?token=PClSfQhjmI2jGf0oACqnXOQEWKeYPokxl6FOh3MgSaabkOg4aFVS-pKI3qb2U7Qc_bbf9qQ2mIgPKSEbHnrEsg_SCl7uuglW0-J0DSziNt26cIr_rN1VjLAWO9oF8t4gSlldJzAjvS96J-c1H3H4gqNpvRc_TjqbpwI2SLyDjhWzVpYQ2bF4atm6Nw2PDZ0O8bQ8Nvz2DltwBNRF_fijGBVxyfAYMyLAXM53BGh7Vd7i89K8VmPh6a3dOLGy50Rng4QF-2fpmZ7D3hDbdrLYglBXz9r593SUbvuJCNwVt8O8YXjmV7kpJEzUwjcl1oM-2Bie5iDF8W_cjQ08yxxsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش متجاوز صهیونیستی در خاک سوریه ایست و بازرسی ایجاد کرد
🔹
نظامیان رژیم صهیونیستی در ادامه تجاوزات خود به خاک سوریه، یک ایست بازرسی در جاده «معریه - عابدین» در حومه غربی درعا ایجاد کردند.
🔹
این گشت نظامی با استقرار در این محور، اتوبوس‌های حامل دانش‌آموزان مقطع آموزش پایه و نیز خودروهای غیرنظامیان را متوقف و بازرسی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658451" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyFEXnlPyyOKISbXdoEyitVtY3EgSDL-dPUbUVfLIfe_-l_fghz-boZF84A1V-XMaOkggBa7HShvaNU4xaTdeJzUsUKiekDQqAFlN7trAeHLnCoPjRnpe30_xfyZamHVO2MTxiKiDpETtv7tuFrzrIdKPgjIay5-WyOUneJGKLbjnBS0nYWT37onCnxBVHfIQCJqqmFtpl3egJCjoxHMi98GEW16yqK5kpMNVgPoS1hpwAb_AtOLjYPq_DsmyMWLjfAOFgXRAzXAW1p6X_aXCyLZLrBrLehT0DFx6rbA0xqGA9XUk7h5_Ge2FZ9t1TQIItWmW7KvTKZnCYU0yIo0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنده‌گویی جدید ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
ترامپ:
🔹
ایالات متحده امشب به ایران ضربه‌ای بسیار سخت خواهد زد (ناوگان دریایی، نیروی هوایی، رادار، ضد هوایی و تمام اشکال دیگر دفاعی آن، همراه با بیشتر توان تهاجمی‌اش، از بین رفته‌اند!)
🔹
در آینده‌ای نه چندان دور، ما جزیره خارک و دیگر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت، درست مانند کاری که با ونزوئلا انجام داده‌ایم، که برای هر دو کشور ونزوئلا و ایالات متحده آمریکا بسیار موفقیت‌آمیز بوده است. از توجه شما به این موضوع سپاسگزاریم!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/658450" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897d5d518b.mp4?token=fCD6oSEEgs6LOG8QVUcAfNq64z4Stl3tvVltRliW-CQQdrVogCJvVwc_gHjC1TA0JD_5UvFVccqNJyYbOTLY1J78z0tDQJf3dYf3hDFjyvtQ5K99bBmyssnCmq_Hnb0ALIf_mbY019rCK3xV6RUF2GCN48azQY0gYgLLswh_qQhqZBsxcUjCvW1E9gdT0JKPzrln_Xeqsv-tkAKX8tUQEUn9TvSWimW35d6vynMYFZgchcSn78mMXS2C1Kj6OyEyN4Ob4LUMfuwejjzkwIhtayizaFn3Ff_Ux5qMDGtGcXi9bkqkBisc9g4bRqzC7nGieo8yI1D7_UkpJkJ_F3EE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897d5d518b.mp4?token=fCD6oSEEgs6LOG8QVUcAfNq64z4Stl3tvVltRliW-CQQdrVogCJvVwc_gHjC1TA0JD_5UvFVccqNJyYbOTLY1J78z0tDQJf3dYf3hDFjyvtQ5K99bBmyssnCmq_Hnb0ALIf_mbY019rCK3xV6RUF2GCN48azQY0gYgLLswh_qQhqZBsxcUjCvW1E9gdT0JKPzrln_Xeqsv-tkAKX8tUQEUn9TvSWimW35d6vynMYFZgchcSn78mMXS2C1Kj6OyEyN4Ob4LUMfuwejjzkwIhtayizaFn3Ff_Ux5qMDGtGcXi9bkqkBisc9g4bRqzC7nGieo8yI1D7_UkpJkJ_F3EE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/658449" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVfNV81200NIi_CByuGQTTQic1frnFtSCFE9qm5AaERcVWch0Y5YJ4BRo5KDD_ji6qLhKwh8a6MkntcXOf6P4L072NTZciHeNzSaaUCZYz_dRrcQNiMFBPShHPR-zgHyobMZJCs2hbuRpKOHuAeLZRXT8GaQ_asZL_6lPfBThBzNDoXUg5Og2p8OIVaJjCyp1J4z4zeZblQ03RtI8yw5GaTsijzO0-5mLXTThMCasHk8PG38gl8w4O16hLIQfbV9duzGEOSzVSeI05UwNqFQadhtCW-LNiqb5sUwTboe6A5vxC-dwjGQUYXMx_P0wuV21OR4Arw-E0fGJO6ZVXn4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی جرایم مالی و ژئوپلیتیک: اگر محاصره دریایی آمریکا علیه ایران مؤثر بود… چرا باید ریسک بازگشت به جنگ را بپذیریم؟!
🔹
اگر اسکورت کشتی‌ها توسط آمریکا کافی بود… چرا باید ریسک بازگشت به جنگ را بپذیریم؟! اگر زمان به نفع ما بود… چرا باید ریسک بازگشت به جنگ را بپذیریم؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/658448" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1663ac3f.mp4?token=uyJNtrpKwYcTc2qinWuhe6mDLRDBSFOEWDgWfZKaNiXiZ98RCCg3V5FMHpKsRqxLx75pfq79Y5Iftet8vld1S7zcjyO8RIX0mjrziWbdCgzE7KFx1UE8-NOdd1K-Zejjbl4VJC1eI6WwsUgLT0cdY81PhbblWopvZQbdckooY78Z-glmKjoxMO1FWV7qnuxjFNMZf5U8VIOOitxryIfeEpzvTABn3yP2KKm1HeQhOuE3lGe8GkIfGdcVW5VHZf8vVAHISsOm44hi_tCVIU6tuJ3iKPChkWs6_hnfy4q7wDcjxyo7qd-K3aorZq9YsrO2khR1EUZ8UAxpP2NfUjkAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1663ac3f.mp4?token=uyJNtrpKwYcTc2qinWuhe6mDLRDBSFOEWDgWfZKaNiXiZ98RCCg3V5FMHpKsRqxLx75pfq79Y5Iftet8vld1S7zcjyO8RIX0mjrziWbdCgzE7KFx1UE8-NOdd1K-Zejjbl4VJC1eI6WwsUgLT0cdY81PhbblWopvZQbdckooY78Z-glmKjoxMO1FWV7qnuxjFNMZf5U8VIOOitxryIfeEpzvTABn3yP2KKm1HeQhOuE3lGe8GkIfGdcVW5VHZf8vVAHISsOm44hi_tCVIU6tuJ3iKPChkWs6_hnfy4q7wDcjxyo7qd-K3aorZq9YsrO2khR1EUZ8UAxpP2NfUjkAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در نارمک تهران| ۱۸ اسفند ۱۴۰۴
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/658447" target="_blank">📅 15:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
آمریکا ورود هواداران تیم ملی فوتبال ساحل‌عاج به خاک این کشور را ممنوع کرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658446" target="_blank">📅 15:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از سمت دریا در محدوده سیریک
🔹
دقایقی پیش صدای انفجارهایی در محدوده دریایی شهر سیریک از سوی منابع محلی و ساکنان شهر گزارش شده است.
🔹
هنوز هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.
🔹
به نظر می رسد این صداها مربوط به درگیری ها یا تبادل آتش در خلیج فارس و تنگه هرمز باشد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658445" target="_blank">📅 15:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkS8FJJca-BEDzO6hdjfMzheYlXWhuwCXGuKfK0--NBssMc1X8U0_FZsTbL4laJGtUtUXBeAKSnEQzbm_rUnpti6krbqXv4IrnJdY44E8Ce9K34-PtDp717ifiu2wnhE54NamXwM41_Agk73pqCTpPO8--JgzEXD24ncTB60VyAejeNp9-oGKlwZ1AY3U4iJCEVHgvFJIyicLx72Ub1NwxQO1ZujCKCgzmaZjVo3bHN2fW5GeR5UUkIbuLkWkBZ7cPgunSd7AjSlVMXD8-e-unFRcW4vM4Qciha_pysvop2PEzVenopWLmBH4oTF9jeUwUYEbGHiNLm5JMZ6dx_YCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلندترین و کهن‌ترین درختان ایران
🔹
عکس راست: بلندترین درختِ ایران. «بلوط بُلَندْمازو» با ارتفاع بیش‌ از ۶۰ متر
🔹
عکس چپ: کُهن‌ترین درختِ ایران. «سرو ابرکوه» با سن حدودا ۴۰۰۰سال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658444" target="_blank">📅 15:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIBBenBv7PK-5_zczvc_P9oTGeOSpf6MTnMq9eGp6ZtNzRfr_Y4eb2mktCY7OQqTw9rResCv08jOKFmlLqe-g2Ic2m6YeVVbUjXFthHackWvdRHM3M3mTvkObj5Bq4FIXgalmJEnEt7nNZ1tjMYXCiGsIaXO9wbigZvkaQ5hLdNf9YuPM7Zc5Pnl9pMIgZDRCFRsqT6jol59Y6P6XkpIUz4HdDtSEG4QBsiRPEy8IfYOgmBnK6DNI5TQ-30sSPXIWWAg6XkAbn8OOYrp-oBnDF7J5tthuFYdl5MhSweMGPKdEAxx18w_3tDaksIxnFvZt4Tzy68F54B1SWeixqCXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایشگاه فرهنگی مذهبی عطر سیب
ویژه عرضه محصولات فرهنگی مذهبی و ملزومات ایام محرم
🔹
میدان آئینی امام حسین (ع)
▪️
از تاریخ ۲۱ خرداد تا ۲۸ خرداد از ساعت ۱۶
🔹
افتتاحیه امروز ساعت
۱۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658443" target="_blank">📅 15:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031593c481.mp4?token=QPuXyQ7mM4XsoAOMuGaM-i0ts2vWEK680MrQ0zdt8iuEQ5ScjHSrxw2F3JRDHne5JaNh_qwJysmZGSSv_Nz3fIa-L3i20i1ZG_Cz1QOLMvJd9M6cQ5Q8n4SxAn_sRAH7WE_6XbERcHBMfBUx5qPtv6lFBnVAlfiYSa91B3sgikPE4KRdzXRNFNREdU5sO-by-TgpDzWQulteNTsVVlEafAMf-T0damZPUypL_tds7Ratv2utsiJmMMNu0AiHXlwp_LGbOPhMLbEARM9jFgADTjtZ5vMChrM7Aq308P0ICGyp-N6INmWvw-9RMEXDa36Sy4DmIZuaufhyWTyyyxYRng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031593c481.mp4?token=QPuXyQ7mM4XsoAOMuGaM-i0ts2vWEK680MrQ0zdt8iuEQ5ScjHSrxw2F3JRDHne5JaNh_qwJysmZGSSv_Nz3fIa-L3i20i1ZG_Cz1QOLMvJd9M6cQ5Q8n4SxAn_sRAH7WE_6XbERcHBMfBUx5qPtv6lFBnVAlfiYSa91B3sgikPE4KRdzXRNFNREdU5sO-by-TgpDzWQulteNTsVVlEafAMf-T0damZPUypL_tds7Ratv2utsiJmMMNu0AiHXlwp_LGbOPhMLbEARM9jFgADTjtZ5vMChrM7Aq308P0ICGyp-N6INmWvw-9RMEXDa36Sy4DmIZuaufhyWTyyyxYRng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر سابق سیا: ترامپ دچار افول ذهنی جدی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658442" target="_blank">📅 15:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNC73YQsQZIBScL87jsIL1W9iUMIMvUI6SA2iURA7Wl79UDNFTTbrWDNxPWC73M2cpgIfRUtoM1vsh5rnH0oEcHNLmhmM6uk64GWBrnIs0P6w8USV-EUkuZksLVDTw5Dim4vhZQMNWqANsO3VmqX0qjmxVs2IuW2F8I68pjlQSmg9d6LcVHotzwAd3VosqJIuzgP_xNLMf5YAgIppGov-1Z9Pp2Vx9hkfjgbkJFvU5_U1zlW6qXZV0sfClNWbf5i1lYhN_kn3yCE7C1nb6EIxyOSj02re_eewjfDeFAA9YFJj8DlcZXJkJA7uuD59RoZ0zIJxF8bzjE_3QKFPkrYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشفتگی نتانیاهو از کارآمدی پهپادهای حزب الله لبنان
نتانیاهو:
🔹
ما با چالش‌های متعددی، به ویژه پهپادهای پرتاب شده توسط حزب‌الله، روبرو هستیم و برای مقابله با آنها تلاش می‌کنیم.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/658441" target="_blank">📅 15:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeCJHzAElF_DRZcG9UVi0_k3NOnu17LVr-ttVPLUMweaqxRJE2fzucAdlIY6lGBQn8Gm9bXoHjG4C8wjTD_JyVvTeTyO0_iSTZYwHUdBuAZhUmmouara70Og6d4CiQ5heu0jkOIafEMrRKAvfDoHqWdt3UN9DiYKyzMxgROtiAo0duF9h0CwM0godj4apT9Z8IB3DXj_drR7KClWz2DyJCyYcxjjC9NkOSeZl9jXv1qdA0UqbakhC5DMBDAbifeEN6GYfwm76mGl5WBLEHFamknYhBQ7QTIUQLBslhizUuZE8ltU7_3rSXtf_O474arGS207L7NfqC1SNV_s4zKY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر علی احسانیان، در ایام جنگ رمضان در شهر نیس فرانسه به طرز مشکوکی به قتل رسیده بود، پیکر مطهرشان برای تدفین امروز به کشور برگشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658440" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مرشایمر: ترور سردار سلیمانی اشتباهی بزرگ بود/ ایران از این جنگ قوی‌تر خارج می‌شود
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
ترور سردار قاسم سلیمانی اشتباه بزرگی بود. ایران ممکن است از این درگیری در موقعیت اقتصادی و ژئوپلیتیکی قوی‌تری خارج شود.
🔹
نقش ایران در تنگه هرمز به تهران اهرمی راهبردی و ماندگار می‌دهد و ممکن است فشارهای بین‌المللی در نهایت به کاهش بخشی از تحریم‌ها منجر شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/658439" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یک منبع نزدیک به تیم مذاکره‌کننده، ادعای سی‌ان‌ان درباره مذاکرات جدید ایران و آمریکا را تکذیب کرد
🔹
این منبع آگاه تأکید کرد که جمهوری اسلامی ایران در روند مذاکرات بر مواضع و خطوط قرمز اعلام‌ شده خود ایستادگی کرده و از مطالبات اصلی خود عقب‌نشینی نکرده است.
🔹
متنی که پیش‌تر از سوی طرف ایرانی مورد تأکید قرار گرفته، همچنان مبنای مواضع تهران است و پیش‌بینی تیم مذاکره‌کننده این است که در نهایت طرف آمریکایی ناچار به پذیرش چارچوب‌های اصلی همان متن شود.
🔹
علت اصلی افزایش فشارها، ایستادگی ایران بر مواضع خود در مذاکرات است
🔹
متن مورد نظر ایران، به دلیل تأمین منافع و مطالبات تهران، تاکنون با موافقت کامل طرف آمریکایی مواجه نشده و همین مسئله یکی از مهم‌ترین موانع دستیابی به تفاهم نهایی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658437" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658436">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: ایران در برابر هیچ فشاری عقب‌نشینی نمی‌کند و در صورت عبور دشمن از خطوط قرمز، پاسخ قاطع خواهد داد. او تأکید کرد ایران آغازگر جنگ نیست اما در دفاع از امنیت و تمامیت ارضی خود با قدرت عمل می‌کند و نیروهای مسلح در بالاترین سطح آمادگی قرار دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658436" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658435">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeEwExjRk1aznLvG0Eek_jhvcjKLe8RrZsyFS22pHCgkC-7aPS9xEUDOIFnZVWo017FLztlGw5eZuDrFhdVGXX5r-dmSsBDT2jAXhm0_AGfX67MIIInMXPg6fuwW1d2Hqfj8bN_Fx3wdMGS-4C_i9qlS4L7yMMUmTGBumJossv3hCkOQ8IIxM_OTwWPbRn0DY6rjYRglJQGn1QkVUwXHMjhyN9ixXbGJBobbhQT-ayasqzI7kE2foXTppvh1NBCctPH5ibqeMKWGGEQ9yIuR7aEoJIR_eMWd0zkID2a4r0LknvMNoDEqcp8w-XGG-gdUj3EcEK_wwj8OkorLmsWGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه مسابقات امروز جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/658435" target="_blank">📅 15:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658432">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcvAkQRHDIPVWyfvPh9uEwCgKVqH3mLK739tb4TrSOQW8kpWY2nD-4g5WmjcWHQKjfU1dnYlNflRMrigpnDSCWEqeSLy4JIHMJu8BYPW_ISrg6b02KO4Bxhw64QX2e99vRDwgnz0PDS1uQhVqfUq-mzbpopiIfSUUaCesNnHZ967ooI2TllyqxqwYBZb4fIjA1EqoAxJ32MEkrgORyu3bzmTk1RtRuaIFv1_robhaEVBf6JwRbMbohIehc3T631CRD55vFQEcbor_uVKKwzhYCXUBFLiuTnAlTiHy7MO-wW41TkA5dEPFDW9vEfgoENlqOwQ6ITTJMYjWfzX0ytAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKog0doRnwU7jTlY3OMLqiBHhMyS7TYQNqX9OSSVrYdg_F6xWCe2g3CeNVnRXAqgkPuOeloqvb-KfaAiPQWtt7LXqzT9eD4cX4f1djfEgZlYzhIt2FE1ZB1kg10pc80WfKjZK9yWuSOyLQb_42-bJpAT31C6YHr4lwE6oSHv8PhIptjqciyMpTLVE6ju8wYbMhZBXhxl2y9NS9wVQRNkAbQ0hN3UP8BicwAHK8ct-Q6M23fJvw2QAtLoyxEkqQNJqiabxTZxf1LmZWQMJo9CUSh3KUni719lI3ftIdmkd-DEC7DqdztwpoBs1FdJdzcsMTITLuzZf7L_txtvP3HLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fo5-6axboqeX372OJ9Ux_yJ8wwcKcwef8TMNeGTRh6oHbqiBpCkkWF_lz0GsCR1UjMQM-Q3yOrjqJrWvxRJ7K67Caf0J3cFNT55GZ9l4RB7ibAZWKxzSnypgTVe0us-l_ziVr2JgxjJHLH-cJMvVPDOMfwiE1UaFtqUscq5MQ9h-269B0zZKFGz3iHjh1w4FBuu8rMH51s6Ab4B7_Eormw6aAP6thPAsgzw7G5zCyxa8AE7uMtz6d_piZXUzwkYpHUoA_taQnK9lASyYvbPQASDWfGSBch9FM5gQ5j6d_TNwCCAH8r4X-B3xGUVf5kkafBzd4FtdX9s0FylDs6TP3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از دانشمند ایرانی که توسط عوامل موساد به شهادت رسید
🔹
دانشمند متعهد و نخبه، شهید دکتر علی احسانیان که در تاریخ ۸ فروردین ماه در میانه جنگ تحمیلی سوم در شهر نیس فرانسه در حالی که مشغول تحقیقات در حوزه هوش مصنوعی بود، توسط عوامل موساد هدف حمله ترور قرار گرفت و به شهادت رسید./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658432" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658431">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658431" target="_blank">📅 15:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658430">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با پرویز دهداری دشمن شدند؟ | من در خواب نامه استعفا را در هواپیما امضا کردم
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658430" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658429">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658429" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUWF4hJU1WwdS6diyjtP4wOkly-I8zBk6FhrXpxmWhSpnLLNBlK-3qJK0xDWavc-jH3HTM4TbZVyZl9pDH0lpk7pt2iPdQqUoAj1xBbMT8AdaE8Juzk-C7jS2aQD2VfXUvr7aBmc7g4BNGgLBN9Z_B3yKg9TW51m_YntQE7cH0ZR2YRseN9-LDr5WFHW3so2Bq5pGOm9EOtkep2pezYgsEBXpv0-ykCfvKOqM5u9veZ7fWxHQhcsDVKKyo_rFaNgeiw6QOEr0gDZB6hixt2YK0yS1TsXe4FTdwCiYlm5qzaeHWNObXtB8g7igYUZAoHfL_lCqE13Tf8nWV2pg0lmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسدود شدن دوباره تنگه هرمز چه بلایی سر جهان می آورد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658428" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658427">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsdLHnrlCk31aG0z-3BOiAJWrV76sZKzUlmvvlTO_QEIVl314yjW4mDOgdgWTyJyo-OimDwWuapMVEzFNvg5OkvxFtt7CrqFvxwSS2BwAQhCIdaa1xAxe5vSxkRV9WzIrjm-01ocv3qp8INRhzJZ112TPJ5qGpCzjwCPo5oEdI_93ChP_-iXQrY36Sim8huWBn7rrge1re8cF7CcYgyC5hnlvyxp5f0aOvUPB--_S9XL7Jb3HIkG7EITnOdDW18wWIJkq508mK6yru3yVvRukSJ5_4-O2W6HsX7tuYOyWU7SKFA5GYW95PbKwhXY9atw3rmxcuBeBwb2lpqQ4rdIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658427" target="_blank">📅 15:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPOt5BI1He2RJYpHJ0rDXwauxoW3HpoQpOwrGiz2WGt2_tI-wU6kQ_HCFrNizw-4WfMnXpPGFgp8IJOhFQYiLTm-DEBRckVOd2RNtw5xRpjXMmUbCXRMsSd7Ginq5GjHfXGk4WaArLTy5L2JzRKI_AVRPAaU13tmwMCLdXu7CfsXINFOHOsaydYK1cTIsnNzcrIEYPuA6xHCyq0HWPoVBBHyD7n7RtfH0p9kbyWXJ3O0tHmbv6ME58618VVbny51LpTK5AanlBJwvteCBHZPZxsjT9krN3d0Rrqv9-Dm_LcszRnUnQuL5xGFc0pkq9mPnS_yeEu14PCcJNESBksa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmEF5DHf4KAY2ed_52mcDLdwknCt1Y0QFV8PsdRL1Or19WUnb-Usc5heLiguS_q5-QxjuhJMnaS0fFTFA0Liyx_DerORJT6gTQsHmzlgILPrpHl5mcsZsLmNlje234aKJsHnkWbeoQRy5BcP6ZpLie9eJ6hL-B207FKhdR2K-2xvx1WaR5U72aQKV_wHEKqIQtf817g8oRNOUNwgItqxuR789-bEZJ3yNN3nn4u3iFtaWFMR_dysUc5bC_XinLeSW9XAseE3we9FpWTs56qjswHDQvuxtvtE1-pyOOKv3CV_AhNyhhcfLHowl0exL3L9-CSDu9HFrIk5XMvpWTGbww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس حمله رژیم صهیونیستی به صور در لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/658425" target="_blank">📅 14:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ2f0T4Ixg1tEDOiK7zGawIfGcE5xb290udeK8tZPOb3C5GNVNQLF8SBO8G_RzZJDH1H0NKqRJ8HM3La1c3aTJSIwCqLN7LbnBtZMnwXVywAN8v5-4nj8lazE-nQMdlng5C95X4YpKbPDHa1hfBs4T8OcaW1D3_JuXPiPsP5a90TEHUjNj6MJfQNpUszcYYETtG8-kN9sDB85EHBmZSxLtBoZn0SNy4Flw_vQ8ebJ1jS_ep3NrERc6NZLgrG4qYnhMuXaGVlYeMjmk3SzPVD6hwB68TlKzIbidvXZ-RAIodkDWx0XKIFv1vFbOM3jbhSS1-LWqmTRjo8WwH1HjzVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت ۹۲.۰۳ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658424" target="_blank">📅 14:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزیر دفاع انگلیس استعفا کرد
🔹
به گزارش بی‌بی‌سی، جان هیلی در نامه‌ استعفا، خطاب به نخست‌وزیر بریتانیا کر استارمر نوشت «برنامه سرمایه‌گذاری دفاعی بسیار کمتر از آن چیزی است که در این مقطع خطرناک برای دفاع و کشور مورد نیاز است».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658423" target="_blank">📅 14:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8e9317bd.mp4?token=V_G1GmJrcGGBQf1FFYlvzA-FDDFLsNveF4798qzL9qYUrJRK7IBOn0ydIJCKGyU8xcb1PnAF4HfCxhw5AOoQk6hxBuvOkBCsIQObr5_pBbBh-DKzZ5milTVrjYCOpgM3hc1ubPLHI8yDo49JoNrzmBW7lMMeNCj29eUzfyHfec5Xv4ljffkNFR4PtdC2QKGaSmIMz6PxyrS3-zKkeQ7rhu6OHjTkqa1-89fint3cMoLmif3f_6KQWtSr2p10Hk_4wqE3Qs4OJAq0zkXU7K5WxGYA4rd7IyqLn4SrhpmnbL24V3KdPpJJ2Fjvw_e55Ufxn4i0rjte7dWMIIA24ZIITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8e9317bd.mp4?token=V_G1GmJrcGGBQf1FFYlvzA-FDDFLsNveF4798qzL9qYUrJRK7IBOn0ydIJCKGyU8xcb1PnAF4HfCxhw5AOoQk6hxBuvOkBCsIQObr5_pBbBh-DKzZ5milTVrjYCOpgM3hc1ubPLHI8yDo49JoNrzmBW7lMMeNCj29eUzfyHfec5Xv4ljffkNFR4PtdC2QKGaSmIMz6PxyrS3-zKkeQ7rhu6OHjTkqa1-89fint3cMoLmif3f_6KQWtSr2p10Hk_4wqE3Qs4OJAq0zkXU7K5WxGYA4rd7IyqLn4SrhpmnbL24V3KdPpJJ2Fjvw_e55Ufxn4i0rjte7dWMIIA24ZIITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال از لحظه عبور جنگنده و واکنش عجیب فیلمبردار در همان لحظه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/658421" target="_blank">📅 14:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7K-2l7iDHEcPsCmfgn-jaCvsKouzJ1iJ_jjcVo6Ytn7JYaRcWmDwp_No4mPsQ5l2mkFkNd6NG7EWq6dr4IpaYFliNYi2HDxGNAWN0eAI5ArStwMVGCzQADOf1IkiXWu4KSJGzdNg9BldUMY07uDKo61ByhBd7aVdynjV798qxdN8HPn1JaZC1fMXJe0NBcy4HNKQYkb_EqHK0FuebZIe-tbgW34IKk_PmCd8kONmkrSgRYjBb4UfVY4r1_Od2RUwOm81rOfDsDLnEMfVALLhT_ZksAqdXTdpiJaXHC9cyFKDOlSMasMW1pqZxUciYlrk0b3r2hXLEEQZ0iB1hat1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: آمریکا باید بین پذیرش شروط ایران و تتمه حیثیتش یکی را انتخاب کند
فرمانده کل سپاه در دوران دفاع مقدس هشت ساله:
🔹
رئیس‌جمهور نامتعادل آمریکا خیال می‌کند با بمب می‌تواند از باتلاق و بن‌بست خودساخته خارج شود. اما با موشک‌های ایرانی، بیشتر در منجلاب فرو خواهد رفت.
🔹
واشنگتن باید بین پذیرش شروط ایران و از دادن تتمه حیثیتش در جهان، یکی را انتخاب کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/658420" target="_blank">📅 14:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723170ae96.mp4?token=X8VrSw_cp3uuMnKRpzLM5SA5BcA4ZeqNR3zXkfuxSUGNBYO-zKL0NWUluIgVjP_eJOoFSVu4UqaduwrkeFVBC7IHzo68Civ0F7lH1yMl6MAsetx9r9yAFuwujlKcFjlgU7ygBuSHIcwxoTgFtWY_xVQHuPGqPx_2Cq1fNs1yfFYPC0IdTDKYZsy7LBvLv-snboaP3-2NnZzKONckh2J_yLm9LhFUWd1PWmDLf638zp5XCM4VTt2YZVfTon6_WsFXOw51NZOdw9H6PnLh6YrwK0PwuCDEae9mYbMx-nVIDCGO4jkuCGAIUaeReQKwUWuyUum0WD0MPpqAOQ1NAgKzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723170ae96.mp4?token=X8VrSw_cp3uuMnKRpzLM5SA5BcA4ZeqNR3zXkfuxSUGNBYO-zKL0NWUluIgVjP_eJOoFSVu4UqaduwrkeFVBC7IHzo68Civ0F7lH1yMl6MAsetx9r9yAFuwujlKcFjlgU7ygBuSHIcwxoTgFtWY_xVQHuPGqPx_2Cq1fNs1yfFYPC0IdTDKYZsy7LBvLv-snboaP3-2NnZzKONckh2J_yLm9LhFUWd1PWmDLf638zp5XCM4VTt2YZVfTon6_WsFXOw51NZOdw9H6PnLh6YrwK0PwuCDEae9mYbMx-nVIDCGO4jkuCGAIUaeReQKwUWuyUum0WD0MPpqAOQ1NAgKzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات موشکی بامدادی هوافضای سپاه به پایگاه های آمریکا در منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/658419" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: لحظاتی پیش صدای انفجار در محدوده سیریک و از سمت دریا شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658418" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پیام تسلیت رهبر انقلاب اسلامی در پی ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)
متن پیام رهبر انقلاب اسلامی به شرح زیر است:
🔹
خبر ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)، موجب تأثر و اندوه فراوان گردید و حوزه‌های علمیه بویژه حوزه مقدسه نجف اشرف را در سوگ نشاند.
🔹
سال‌ها حضور در حوزه مقدسه نجف اشرف و کسب فیض از محضر بزرگان آن، ‌چون مرحوم آیت‌الله سیدابوالقاسم خویی (ره) و تربیت شاگردان و تألیف کتب و اشراف بر جریان علمی آن حوزه و ارشاد مؤمنین و مقلدان، تنها بخشی از خدمات وجود این فقیه بود که فراموش نخواهد شد و آثار صالحه آن باقی خواهدماند ان‌شاءالله.
🔹
اینجانب این ضایعه مؤلمه را به حوزه نجف اشرف و عموم مقلدان و ارادتمندان آن مرجع فقید بویژه به ملت مقاوم و نستوه افغانستان و خاندان معزز ایشان، تسلیت عرض نموده و از درگاه خداوند متعال برای آن فقید سعید، علو درجات و حشر با اولیای الهی، و برای بازماندگان صبر جمیل و اجر جزیل مسئلت می‌نمایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/658417" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52003f3ccf.mp4?token=nIkMPqrBUqVpQm_0FH-_E4Kj9chwVrXO1LS5qU72Hsl4gjqAJvBOozxfrCgaFfMS-g_FSXMlqaZrA8T_KPHYdDUzXnjKrfStkgl6IwS_iWWj0UrbZi3Z9t2wvJ4R69nFFJooW6H9_CGfqnigeQb_0Avq_cRowLlWQqWdW_2eybnaMtGTCzojLwQlsfvdMhN_crj8whnzCGmfHwxIk9fvIfqHXFUjG-Irzmk0MSLPeYvRQm5C2BiOq9M4Ymotzk9kPCOtqcd2eLIEgVXQjtB4Ka5bNp7cMcn1d4509IGWe3Uln2nsFdOLF_B1vNuVr3FPr0Pt5bVJULf6TbM_lFlCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52003f3ccf.mp4?token=nIkMPqrBUqVpQm_0FH-_E4Kj9chwVrXO1LS5qU72Hsl4gjqAJvBOozxfrCgaFfMS-g_FSXMlqaZrA8T_KPHYdDUzXnjKrfStkgl6IwS_iWWj0UrbZi3Z9t2wvJ4R69nFFJooW6H9_CGfqnigeQb_0Avq_cRowLlWQqWdW_2eybnaMtGTCzojLwQlsfvdMhN_crj8whnzCGmfHwxIk9fvIfqHXFUjG-Irzmk0MSLPeYvRQm5C2BiOq9M4Ymotzk9kPCOtqcd2eLIEgVXQjtB4Ka5bNp7cMcn1d4509IGWe3Uln2nsFdOLF_B1vNuVr3FPr0Pt5bVJULf6TbM_lFlCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای فداکاری عجیب ناصر محمدخانی | وقتی ناصر محمدخانی قید بازی در بوندس‌لیگا را بخاطر رفاقت زد
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658416" target="_blank">📅 14:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhiX0nBZdjyvXHFEe5PELOqZGhuc2REFAXkAqh36kVsQz2i__FyYYc1squT-BW7KrIK4gC270K_AkSfjAxGwwzRyi7eH7fW0e_h6UtzXqI4MjxX-4767YO_BI-EA6UGx17Tya4krRvY_BRzW3-EQBvM3XIpf0TwwEm_cGIc8TFs5pX-EbUN0LlfTMcXbsuMPfLi_RVLyWE5rdNM4e2uTGRAmMXwj_oI6RzNAAhI_IBqtg4qi-mIfCbDExmQRc2uzwxtoGcHjiQB0eJpJuzOqK0MJ23S1Wub0JiusDQTq9i0DDUKjJTVgfHYd1sisJqQnhMVhBFHem9V2s4SuKz6S0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای جهانی در کف قیمت ۶ ماهه ترمز زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/658415" target="_blank">📅 14:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiqpJdm9AOibJFuVJEETBt1aRGWCVjBhgxSywLkzPi741oQs26jRtLXzQPiodBw8o3ruQRsEityg5nyfuSMHArmJzZnON5wt69z37VsTP_yNl5JylVMFGlZBlyZDOjKEdhY2dgmosPkWsypVe7t3KqfrdB8MO2e-Qch2CZoFjBcxQ7IYg4q_I1mYNTnK1jS98oH8WSbovZxGy87O13jGaEJoUEtDU8RKMk06DTUtO02tzDVR1OkFu_Fz3vePFZuf1jnBwC7zotzAZuXvLehZrowBRKrUhKkjHIhReLbVVqyJHFYXG4M8BKZA5lEAlAvxy2L1ct2dmK-8ZviwizjYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: در حقوق بین‌الملل تجاوز نظامی با واژه‌سازی مشروع نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658414" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تیزر قسمت دوازدهم از فصل چهارم
🔹
در این قسمت ادامه روایت از تجربه‌ نزدیک به مرگ آقای مسعود نبی چنانی که به دلیل بیماری کرونا به کما می رود و با جدا شدن روح از جسم در عالم برزخ مواردی از جمله مرگ ۵ نفر از اطرافیان را درک می‌کند و بعد از بیرون آمدن از کما، به ترتیب مرگ آن نفرات که یکی از آنها همسر ایشان هستند را می‌بیند
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: مسعود نبی چنانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/658413" target="_blank">📅 14:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531db40f5.mp4?token=BPk6OzM0IF-yAPL0Gv0e79t0uny-6s9Gkz2mxqxM35zOkNwP-g7pnml_gP8_E1v24teY8Y7xts42e--pGLOxXEaBS5KPKMl9KPntbpuSFElkpUBoKVu5R6pglQ4VWUa7_BMaDUxlb_xnMKvfViUYRWaPGOvMe23YMBb3WLKZo3KXKdBCATrW9ms5LIAc-t8Hr36YsyUhEQjf997tEC8JnX6mywQzTNJe5ZCyhSarBdysJfz4SF95GhH5M_8oDHU5tThNxI3PoGNw6ghsZAtGKkH1hQ0BcGC89iRCsfS_jrNf6CmiRzDwpddwQEKEvS5kzWudJGdJlwGgzdPtRRSbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531db40f5.mp4?token=BPk6OzM0IF-yAPL0Gv0e79t0uny-6s9Gkz2mxqxM35zOkNwP-g7pnml_gP8_E1v24teY8Y7xts42e--pGLOxXEaBS5KPKMl9KPntbpuSFElkpUBoKVu5R6pglQ4VWUa7_BMaDUxlb_xnMKvfViUYRWaPGOvMe23YMBb3WLKZo3KXKdBCATrW9ms5LIAc-t8Hr36YsyUhEQjf997tEC8JnX6mywQzTNJe5ZCyhSarBdysJfz4SF95GhH5M_8oDHU5tThNxI3PoGNw6ghsZAtGKkH1hQ0BcGC89iRCsfS_jrNf6CmiRzDwpddwQEKEvS5kzWudJGdJlwGgzdPtRRSbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایران گورستان تمام آرزوهایم شود، باز قلبم را در خاکِ پاکِ این وطن، دفن خواهم کرد
❤️‍🩹
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658412" target="_blank">📅 14:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
پیش‌نویس توافق نهایی تهیه شده است  ادعای رسانه بریتانیایی امواج به نقل از یک منبع با اشاره به سفر قطری ها به تهران:
🔹
متن آماده است. دیشب نهایی شد؛ اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658411" target="_blank">📅 13:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2qvgB2z027nBV79lh63S-5bWhCbDzj7mZSZu0v64rJ4SEVTPly-ISdSmgpvi4xowN5Qs_rD3XkeEESybaYtd2LHoUe2pJtaMCFtUg4soLoCpFRaeojy18OOUtEW6PFq-17Tq_3bRI6mdtodV8vvIe18kACVzAIaaUp5VwysxYyxOem5tbxtMqFW3mmyXi0NlkC_k6mWV7mxoxlEfkUMQsfVorEOnQdcLkxPzv7rEsNRT7y-0wpOXikybgJoRTXshONwwyFrVYwbLe_zlPucdMacUxhDA4t_zS-BdPIibogg1t_PPDgM3BHtnFIxCJt63Xi3R61UoxXfHg6IX9TW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از درخواست فیفا؛ تغییر لباس هائیتی یک روز مانده به آغاز
جام جهانی۲۰۲۶
🔹
فیفا خواستار حذف تصویر نبرد "ورتیرس" روی لباس هائیتی شده بود، چون این امر سیاسی تلقی میشد.
🔹
این تصویر مربوط به سال ۱۸۰۲ است که ناپلئون سربازان لهستانی را برای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه استقلال این کشور جنگیدند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658410" target="_blank">📅 13:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIDPedyYMBRho8o202C5xKaBxGKz-u098yD8abUlmq2e934OS-7A7ITboBcpeScGFNkQxjRkeJEAcvKGlCngs_W-5NipKYn-DGMbRgmeq8Q6K2qlI3inT6Q116jpKNw9nYpr3a36_rCPDYn0e2908V3YqQoOJ0WwtxF0aA5lrwwKJMhtWuXwfNbjoDI4ixez1r4rNzPIdVaBqcEkBCqRXHryagZ3n4pEkSkrAyjQb8hdqYwdmskKgG_5yswQtZYfralM0My863qxEDFwDYqZbaG6FkSRfY6tS_Vka7AHzlEsH1qD8NWAUVdHDEcXMgT1BV_Halsx60EguqeDWyKojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1v2aHZm-v4YS32OhtqTwMdCzXjpOA546NfTazqqE9vcZMRl9diTDlmWIXEII-gV41yia4eMoznR5gV1gZ_hAF7_LHyZOxPkHt4dXGHmCVA7RF7Y5M7wL87r9TChL6oC3r6Bo8n52YQs5PEaOiwPSiAY5iSg8qB2S4QzDfGffwMq1_kumsTAX4n-X2eMtfd5myJi-biQx7ZJXAiTRoPMyPnBae_caX4cBxYLmRsLo194vSBbsVHhzdhHmGlMLlikzPq-1wWy5WsV59Q-lScn_nSwOzk9TU2jVUWtHYceR9cRpBnPoIgmhZIFfBEd7YvnuR1-hcNKEVrILc2qlW2ZEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بقائی: تخریب مخازن آب آشامیدنی در سیریک، اوج زوال اخلاقی در سامانۀ حکمرانی آمریکاست
🔹
سخنگوی وزارت خارجه با انتقاد از حمله آمریکا به مخازن آب آشامیدنی سیریک، آن را اقدامی عامدانه و «جنایت جنگی» توصیف کرد و آن را نشانه‌ای از زوال اخلاقی در نظام حکمرانی آمریکا دانست.
🔹
او با استناد به نقل‌قولی از سیمون وی، این حمله را افشاگر ماهیت واقعی قدرت آمریکا و مغایر با ادعاهای حقوق بشری آن معرفی کرد و نتیجه گرفت که بی‌اعتباری اخلاقی، نشانه افول قدرت‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658407" target="_blank">📅 13:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cfee9959.mp4?token=rFF6kwMpnPzZEwlQxpMvssCMuSFJMpKt7xtd0hfAeA1zoK1O3LnUjk6sgIkoHlGWdsNrC4GhJnNqS3SIwxfMrV2yw0HBSkRx8GyNR8RJv0HrWpk9ru38VNxQiTSrnVUrgkt8sMAabeEcsUh1VY9jzwesjZDSt3CQoDVHXmcwqg6dw_8vVZfobCde9kh237ZohnqXes4FMUMIW82-Gxjf7GgHIDi4IQlIBTom7pALEi3--dhrarnnWkJcQtWQ6T9ctIrsVjRxXzKUrSRO4tZq5hoINHLI1g33-o_MdRnWkngo_xzc_qIzoUMkRk8OwpoYeSD07rlpjfJfx4eT4qwoeCJly6pBzOZkq_tBtZyjGp2nMfLkA_nB34EzDyMzJtO-At7-uDqcZnOtQdEjA8KV0l7kCuK37lJQ2EIQaywP2oCnPoTKGxUaCzOAPMFRT2od5PFmQsQ3p8V3EeFMHY5-7I1wFbJVHJxXbbx7HUO0CatIeEb5WmY21foONkUmaiE1zK9VQAJXF8Qs5a0XOTII8v1jdQ5EmSLq5kZUtbi1U24saegSgaHR7k54R6cI0ajumFnC2Gp2AEPGpQynvvF9zzCM-VKbnKLe1e9J5iSC0pR5IIpKEhTqdrSM9ZJwKbhVUTVO0s-GT5qHcKQnXvrBKSn5VCEayctgEJUni9GGWHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cfee9959.mp4?token=rFF6kwMpnPzZEwlQxpMvssCMuSFJMpKt7xtd0hfAeA1zoK1O3LnUjk6sgIkoHlGWdsNrC4GhJnNqS3SIwxfMrV2yw0HBSkRx8GyNR8RJv0HrWpk9ru38VNxQiTSrnVUrgkt8sMAabeEcsUh1VY9jzwesjZDSt3CQoDVHXmcwqg6dw_8vVZfobCde9kh237ZohnqXes4FMUMIW82-Gxjf7GgHIDi4IQlIBTom7pALEi3--dhrarnnWkJcQtWQ6T9ctIrsVjRxXzKUrSRO4tZq5hoINHLI1g33-o_MdRnWkngo_xzc_qIzoUMkRk8OwpoYeSD07rlpjfJfx4eT4qwoeCJly6pBzOZkq_tBtZyjGp2nMfLkA_nB34EzDyMzJtO-At7-uDqcZnOtQdEjA8KV0l7kCuK37lJQ2EIQaywP2oCnPoTKGxUaCzOAPMFRT2od5PFmQsQ3p8V3EeFMHY5-7I1wFbJVHJxXbbx7HUO0CatIeEb5WmY21foONkUmaiE1zK9VQAJXF8Qs5a0XOTII8v1jdQ5EmSLq5kZUtbi1U24saegSgaHR7k54R6cI0ajumFnC2Gp2AEPGpQynvvF9zzCM-VKbnKLe1e9J5iSC0pR5IIpKEhTqdrSM9ZJwKbhVUTVO0s-GT5qHcKQnXvrBKSn5VCEayctgEJUni9GGWHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار ارشد بی‌بی‌سی از جشن و شادی مردم لبنان در برابر سفارت ایران می‌گوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/658405" target="_blank">📅 13:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=c5S6n-NJzoXMjcI0eVQo4DN54PKhfTAXLjhQrFfVAtULBZuwywYZxnNkMcHcFpClZnTRfwWpnQKlV4KcAOTgMNOX1dBmvBnB-AD_aqUTij15BSnFa7gcYdsa5aGvXFsbSKBIQUP18uIi_spwJQEQ6gzh1qwSMokmwtWX47y6r_4sN4Rj9km5UVTX0kzutlAJkyiJ92Bz9Zsi8ZVr3DkRwwebaq-odTwtKRICfRPyPSF6qPKYSr4qDyxw5IrWuWBnQG065ho8r6WDgI749jABFCKVi6yfHV6cv11qtvV_rHGMJSWFTer_UNobgzmI0xGigxULYH3pQdeVHttkfRWQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=c5S6n-NJzoXMjcI0eVQo4DN54PKhfTAXLjhQrFfVAtULBZuwywYZxnNkMcHcFpClZnTRfwWpnQKlV4KcAOTgMNOX1dBmvBnB-AD_aqUTij15BSnFa7gcYdsa5aGvXFsbSKBIQUP18uIi_spwJQEQ6gzh1qwSMokmwtWX47y6r_4sN4Rj9km5UVTX0kzutlAJkyiJ92Bz9Zsi8ZVr3DkRwwebaq-odTwtKRICfRPyPSF6qPKYSr4qDyxw5IrWuWBnQG065ho8r6WDgI749jABFCKVi6yfHV6cv11qtvV_rHGMJSWFTer_UNobgzmI0xGigxULYH3pQdeVHttkfRWQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست‌نوشتهٔ شهید فرشته افشردی، دختر سرلشکر شهید باقری، که در میان آوار‌ها به‌جا مانده‌ بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658404" target="_blank">📅 13:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a7a0f469.mp4?token=u_OWVjl3sh-J6j3VaVxqKqaShkuz31w5GM3M4pJJaFV0FvgfleONXeNgF3TVdkZJBCNrW6NQxwPxg1Gf_9sh4vDJrTajlWl_BBVik6GJEH4p1yr70JMMcUvDubS1xXtrV8wM3jgMgCAqXGwOjzxAF3VPyOMwk6LqSJJjBUiQtbNuxzYIwqQFnWE74QkrVhLXL-cxYH3sxTCBvCC6Mj6E0s3Qv2PrspO9XjViNeHrurTOQUM_sSqOEeQzrJ4RM1h4lFGaNxWSEzv6eVF-z4XII2Ic6WAmn-5dPUWTuRQl6ggLOlowiGlWcw9UPUUvVyzbkBRfzkEnZZiAOxHtxfLIoFLTzbutkbsEt-DF6WZHMxMCFaREKhIgIGt4BWdPvmeAfb79j4etFv3wOIKk8TxBL1zKmu4q90Rjww7NVMY36f2tO7lC-Pn85KtrHzPvj7pt18CCwxGe42Ck8bY0hanbrtK38-uQAIPTgpU6huZzJRivHcUN0NqgzSDdGBbrqaamp-LD5_87JxyoRTIkj3hpaFPaQ0QIq-sORpKjhf7KcoLusA89xcgOiCL6FJ9cF_Kiollq_eZsFVQ3U8UAChBa2_9PwdsV_8Gly33A9j4bexO6CzhWkBlfE2B5lYOQeeYhmciZbH5xjTj3LPUmQCX4uLD43xYXAIkrgVpUCbKKFRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a7a0f469.mp4?token=u_OWVjl3sh-J6j3VaVxqKqaShkuz31w5GM3M4pJJaFV0FvgfleONXeNgF3TVdkZJBCNrW6NQxwPxg1Gf_9sh4vDJrTajlWl_BBVik6GJEH4p1yr70JMMcUvDubS1xXtrV8wM3jgMgCAqXGwOjzxAF3VPyOMwk6LqSJJjBUiQtbNuxzYIwqQFnWE74QkrVhLXL-cxYH3sxTCBvCC6Mj6E0s3Qv2PrspO9XjViNeHrurTOQUM_sSqOEeQzrJ4RM1h4lFGaNxWSEzv6eVF-z4XII2Ic6WAmn-5dPUWTuRQl6ggLOlowiGlWcw9UPUUvVyzbkBRfzkEnZZiAOxHtxfLIoFLTzbutkbsEt-DF6WZHMxMCFaREKhIgIGt4BWdPvmeAfb79j4etFv3wOIKk8TxBL1zKmu4q90Rjww7NVMY36f2tO7lC-Pn85KtrHzPvj7pt18CCwxGe42Ck8bY0hanbrtK38-uQAIPTgpU6huZzJRivHcUN0NqgzSDdGBbrqaamp-LD5_87JxyoRTIkj3hpaFPaQ0QIq-sORpKjhf7KcoLusA89xcgOiCL6FJ9cF_Kiollq_eZsFVQ3U8UAChBa2_9PwdsV_8Gly33A9j4bexO6CzhWkBlfE2B5lYOQeeYhmciZbH5xjTj3LPUmQCX4uLD43xYXAIkrgVpUCbKKFRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام جهانیه و توپش؛ مرور توپ‌های ادوار جام‌های جهانی از ۱۹۳۰ تا ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/658403" target="_blank">📅 13:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اصابت پرتابه آمریکایی به لنج باری سیریک در دریای عمان   فرماندار سیریک:
🔹
بامداد امروز پرتابه دشمن آمریکایی به یک لنج باری متعلق به اهالی این شهرستان در دریای عمان اصابت کرد؛ این لنج حامل کالاهای اساسی بود که ساعت ۵ صبح از شهر خصب عمان به سمت سیریک حرکت…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/658402" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حمله پهپادی ارتش به ناوگان پنجم آمریکا در بحرین
ارتش جمهوری اسلامی ایران:
🔹
در پی تجاوز آمریکا به جنوب کشور، ناوگان پنجم این کشور در بحرین را با پهپادهای انهدامی هدف قرار داده است. بنا بر این گزارش، در این حمله آنتن‌های ارتباطی و تأسیسات راداری سامانه پاتریوت هدف قرار گرفتند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/658400" target="_blank">📅 12:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حملات شب گذشته منجر به مصدومیت ۵ نفر در استان‌های تهران و هرمزگان شد
جعفر میعادفر، رئیس سازمان اورژانس کشور در
#گفتگو
با خبرفوری:
🔹
مطابق آخرین آمار ما از ساعت ۲۴ شب گذشته تاکنون ۵ مصدوم در نتیجه حملات داشته‌ایم.
🔹
۳ نفر در استان تهران در شهر ورامین، ری و ۲ نفر هم در استان هرمزگان جزیره سیریک مصدوم شده بودند که همه آن‌ها مرخص شده‌اند و حال عمومی آنها مساعد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/658399" target="_blank">📅 12:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKIePsrFbnWcSct9Rz8GM2Cw5baC7J5tlC7K6OGKNBx9Hxawfb4DjhAkElh0lMr2EOrb9XKwOir1FG9YO63dGKITMfYEAXGrRbhdVVoXFgB0sQxth50Tlr9zOmE_o9RVlr7Lma2H4WhT312WlNK9Jncq2KiRDTEA-pZrJZvBzks3r2-AVUcfcVjWT7wEhgL_H9oAcHElNiUfXmSKa82w6kfM0116fTAPT0BKrCugvzsLzAYh3ZkJ652_bJ5MFZyqvNzflZnPmPNLUUcmrOhP1sPW19azfY17AGFQtjdWTwxaakDpzq2c0yKpOcGsLHAqMVd438JZDriQqEWIKjo0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بین بزرگترین و کوچکترین بازیکن جام‌جهانی بیشتر از ۲۵ سال فاصله‌ است!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658398" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAj6n5BAj1E9tY4rgqBJTVNDNR3hhZX3oN0CZpuPL44WJPEVprP-OdUpk4A0WvOGzQ_gOSEE897GLLnkrs8XQoH1ry1GYp-L7NR_QHVscuPpcDNwttf_ShpFol2LWy_mNhzhTq7cr0zfk6bXsvXIYkyZOllGnqnWMsNQwl8TXDXIRmd3E5Tr3HH97L96IM4gdGa4PjJxeltuWvNwqv53jo6hE2vQWLT4IrHw5q0jDkNK0IxhS3YkO5l5mND4vc5FtuYLXBia4gyw3wCw3ZVrxZYDvEIb1Jmo1SdQNEp2C-st7rPiV0tzLrsb1I0v5Us0ovqSdwY-mezI2cZki-cZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج‌فارس: تنگه هرمز تا اطلاع بعدی بسته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658396" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پیش‌نویس توافق نهایی تهیه شده است
ادعای رسانه بریتانیایی امواج به نقل از یک منبع با اشاره به سفر قطری ها به تهران:
🔹
متن آماده است. دیشب نهایی شد؛ اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/658395" target="_blank">📅 12:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08fa32d868.mp4?token=KbYxbrclsTdxzlRvkkftOI75LpwiOQFWCbMzL7HwKRX_4ThhOR15HNq_V0OUsYr2WvCwRojDqseCkHNMcX7Rt7fn0VssVIrRe4cagVGnwqzuF6ccxi3llmuJdJ85pg_-qFXh6_kFIJU-phGl4SGJn2FrvepP09alKggasWhj7k9A_Jc3oH_BGb4968szhrhlLXGKQNmMHmGfCEEsHhDnLwQSBw_blJHilN22aBcPNfigC_vVhGDub9d5hZl73h3blzug1goWH2jV8yzDiazrqPRccgWp3j9k6hOiuAb6L41SZ3u5nRxDmj3xJRvl30vHXVP16dOwz1X3sUuUCsTomw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08fa32d868.mp4?token=KbYxbrclsTdxzlRvkkftOI75LpwiOQFWCbMzL7HwKRX_4ThhOR15HNq_V0OUsYr2WvCwRojDqseCkHNMcX7Rt7fn0VssVIrRe4cagVGnwqzuF6ccxi3llmuJdJ85pg_-qFXh6_kFIJU-phGl4SGJn2FrvepP09alKggasWhj7k9A_Jc3oH_BGb4968szhrhlLXGKQNmMHmGfCEEsHhDnLwQSBw_blJHilN22aBcPNfigC_vVhGDub9d5hZl73h3blzug1goWH2jV8yzDiazrqPRccgWp3j9k6hOiuAb6L41SZ3u5nRxDmj3xJRvl30vHXVP16dOwz1X3sUuUCsTomw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد، شهر بادگیرها
🇮🇷
#ایران_زیبا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/658394" target="_blank">📅 12:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54178dc8c1.mp4?token=dPTiwazcT7AZ8QPCcAGr98kryoP7XcYK9JlgD9nop46dvCEn-m96F9tvlZs8X_RwP2jTH9xWxK8_Z6Zz0ZO-4VSeh0bYls0PQcVa-Fr3ubwsSZCbZEODhV6zAvTHeb3qwIh_GDCYBdRAjQHPDPwY8MGQNt3N0rcmCASler2ycuepVPIIBw6xV_mqfaanlGd5wJz-blX1fRZxSzW8ytVJ5SfQUz1lOtW9Tae02SHUnS_OJ09Bs8YJXO_vGbXx_ulORS9CiVr82h0x7F-SbeovnY0OImJd8AKjf9Jx-_8Llm-g1hQ4lEY0awPhK5xVYd0VHtE99RIaA8OFlJtv6KgE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54178dc8c1.mp4?token=dPTiwazcT7AZ8QPCcAGr98kryoP7XcYK9JlgD9nop46dvCEn-m96F9tvlZs8X_RwP2jTH9xWxK8_Z6Zz0ZO-4VSeh0bYls0PQcVa-Fr3ubwsSZCbZEODhV6zAvTHeb3qwIh_GDCYBdRAjQHPDPwY8MGQNt3N0rcmCASler2ycuepVPIIBw6xV_mqfaanlGd5wJz-blX1fRZxSzW8ytVJ5SfQUz1lOtW9Tae02SHUnS_OJ09Bs8YJXO_vGbXx_ulORS9CiVr82h0x7F-SbeovnY0OImJd8AKjf9Jx-_8Llm-g1hQ4lEY0awPhK5xVYd0VHtE99RIaA8OFlJtv6KgE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان ارتش اردن به حملات موشکی ایران  ارتش اردن مدعی شد:
🔹
بامداد امروز هدف حمله با ۲۰ موشک قرار گرفته که از خاک ایران به سمت منطقه الازرق شلیک شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/658392" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658390">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
همه حجاج تا ۲۳ خرداد به کشور بر‌می‌گردند
مجید اخوان، سخنگو و سرپرست روابط عمومی سازمان هواپیمایی کشوری در
#گفتگو
با خبرفوری:
🔹
وضعیت پروازها طبق روال گذشته در همان فرودگاه‌هایی که طی اطلاعیه‌های گذشته فعال بوده است، هم‌چنان ادامه دارد. فعال شدن فرودگاه‌های غرب کشور در حال بررسی است.
🔹
تا ۲۳ خرداد بازگشت حجاج به کشور به پایان می‌رسد و از طریق هفت فرودگاه امام، مشهد، گرگان، زاهدان و...برمی‌گردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658390" target="_blank">📅 12:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658389">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=JNMQHSHSnF4bz3BVmdu-qjwWDGPqtBpdhhXS6GA3Ht_CrFfb9S5IrWarZbUOAhF3PKJUzIVc5hfFNX8IPInfUXDUGsI3S4cUVDpPep0AXI70ZpU7XCHV8rBP75Gdcov0gjDnGMu87Yx1t4B7lRflfalZJ3VeCBPB92oExa-mGt3UYN4sGDN753DzU-Y5IMUOSPb8ZKHT1dAELLlE3JvK1LvmJvmK3NRpeODJfsDQtV3Kw9kF5zriWlmMmQtdFMBOgUgBx89fpXTs2lc8duYFtYdBxKk58GgBGHlBsC-t4qSivt7GOH0ztJRyUhr1FYH-zFtdQbBXTNqSLEXhdAtHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=JNMQHSHSnF4bz3BVmdu-qjwWDGPqtBpdhhXS6GA3Ht_CrFfb9S5IrWarZbUOAhF3PKJUzIVc5hfFNX8IPInfUXDUGsI3S4cUVDpPep0AXI70ZpU7XCHV8rBP75Gdcov0gjDnGMu87Yx1t4B7lRflfalZJ3VeCBPB92oExa-mGt3UYN4sGDN753DzU-Y5IMUOSPb8ZKHT1dAELLlE3JvK1LvmJvmK3NRpeODJfsDQtV3Kw9kF5zriWlmMmQtdFMBOgUgBx89fpXTs2lc8duYFtYdBxKk58GgBGHlBsC-t4qSivt7GOH0ztJRyUhr1FYH-zFtdQbBXTNqSLEXhdAtHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواد خیابانی: سردار تو تیم نیستی ولی هستی، بعضیا وقتی نیستن، نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658389" target="_blank">📅 12:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658388">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA4Q068bjBiT0a1a5q1WsG2EmZDiM814GxIH4foVlyeSeBWiPKdq7-J2-Nc8t9xh36qex-ckLhZu0G6RRPja71YStgs4aHsJTwQEP3PCTD37EpD6hlgSOLcuZHQ2j0RjZghVxHnAeXhDklT3zde8FjLwIM8trdoKG-f8sqJZTAp-KotxjY3vcZrjK9qpjGc7iCZxzPdc5_TOBsh6S8tapt3crGQGno2_SEWKkotfJByf9xeXRqW4JArclK5o_KlUiXIXmif_RSZsQX-C8suDNKghYvp7PAw4sSxoq-q463AHKZgb15I5FITFA6E67wGlOZktdWRF3SyKbAElXM-z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658388" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbV7ox8cFqPl8ZESYDwzJe7raZAOlcfjt1BBjj-W4KMB9M1jHUDX875jZ7T29MoVWgOT7I60-As8k7SisHtFqv9BRrYyUvs2hESxu_mCfugL0ZY9BPeg7XOdxlpAxSKM40A5dBrU3JslBdbd_Apa3dBpgpi7Qb1EWVwJ2xIipAKjw_Aljx0jCIrENPFKPl_XrLqW5EmzrgeNJPiglgGxwUyHm2oH1JrW0pgks3Nszw1Hh6SkIgz6aqGUPPdSi9m1X6XDFJfE0W9EBqRVKpn72XeLuy6LOhjqJMMyTmCTTr-ufZDEzrdOrKvaPEl1k7w_iUL-u04Fo1T7ERHPDiA4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiLy2s7xsjoaIiS6vkXBMmtzhwlISapEm3cVnsimTGK2FaNvqAIHeascmu9cgkRGB6T9mP-SGbLuqHblOFhkLywwzUa4L5l4OBsJhqbJjPzZY3RCYbSkaoml7oQ2HSRnfUEWHo92dYg5w1Wt80zP-3tTupP0lOtqaI45gX1r0fuXYYm3zCSZuVC3Soi_MU5feZDRdLC6-HsBMGrAo4xJZpJPny-WyA7mrytaCIrbC3xmJM1Auwcq6M-uhCVFRhO7t1_HJ0ZkfvSMIF2oyRBqVjjlM9buJUWGpNksOp8Wi-8eadqWmJns_-MK6PodmJ48KEAjMPaQDZp4yFHPOkEevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSEnCQ1Nb3-zE-EHm00Y1HcwPxD01ZflJI_FawygL1nsT5gdfLNEt-0ugU9fcFVhuCyQjdjfBcl4uqaeWQYpbkGLsz36JCazv04i7YvnsHWymsD043ghtd1UMxrEMPgfe_8cE5zHglMvdNmgwVAfvuYTWMKxp-d1Y7esd0wLUB2zmBkBnyIuJwUnYxfCHP97sUyLwW-rneBLKFtLxTVkxisV0eNw-DBFLDBDP5cta2jME2jqn-lrKmUGd-K5t_t9O5pj1XVONj8ImPdlWikoqxbCxjNcSQSsotFhFnKdFwh1VTm9b6penplHpFUCywHukCxY9Jw1LwyMRlJRcxIf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwExCyIupDUG0CvLnD2-MDuCkEZo3d07exESfy4EbzjeqK73SEaxyfCqkKXFfIDpMXekpfkWZOy4wTIYz-ROACGDpb9vefNqc9gXtHI-l59z0ZHf2YIpetZSVpq6C9R9Ta9wVpz3BL0Y1cVvMyp_uH-aX-H6CGq5Q5Qbpoge56oOmvpzewx6PAnIcpq5v1xeptZKFXKXxk1bl-Dq3BNyvGdRtyoEdhHOA-gnAojm0iMmNc2CoOHLSIf-9FG2AippKCVs8mgT8zyRZB1d4Tj7J8eD5zZwOTV0zurrpaVECAMo8BxeuHZrWczVjrD_qc6DJ_xtYM7c1ZAxtvmCKYXmsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رونمایی فیفا از جایزه کفش طلا؛ توپ طلا و دستکش طلا برای بهترین‌های جام جهانی ٢٠٢۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658383" target="_blank">📅 11:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مصاف ایران بانایب قهرمان جهان
🔹
تیم ملی والیبال ایران در دومین مسابقه خود در هفته نخست لیگ ملت‌ها ۲۰۲۶ از ساعت ۲۳ امشب به مصاف بلغارستانی می‌رود که در حال حاضر نایب قهرمان جهان است.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/658382" target="_blank">📅 11:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSocZ4BXXSkv7tkjvQhmZ9_YLlxcTO76b2-0kVKvhGJ0CTE6ltO9LEYVaxQVmmQ1JTcEzQbluzunLOa4fp1BROKjBWKGMyA-dLlwhPiJJebMzG8jghnYCOW4rHX4XjncF7a9IFp5nt7Sl1XTZKo1le5oB36B0tGhN3KLw18DzLHjz2_SbuPXn-PPEiKa64UuGH1IZJTXbwSEONZl23cLHRFAXM2FKhEDoEckhVAIjBMmt2o-efjpdLD61IYoCr8oFHRAB27zFMsCfIgm_DHUxers8P4wcB18HtSrNj5akj6xor1bqjSHM3mP1XkAjlEya3MSDYBc1rpOrqeVGDmzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz1HrncVhmJZE9RAptHr1OOSG8d7YZi0yQ5xqJ4AghZ_wEZGxvBjYHT_hDsQ33je7zTPLfBDHGuB7V8vdRhaYozthg_omr_gF1gpCBZYFsjYd-07oxM1LF4QgBmUPGzXiNbiqk_rcUE2WaGa9D6sH8T8_rcblVxhMWcV89hUFCPqiNm_TBE5OIA95L-ng5TxFwDAdp4BdS8w9SpzNU2m35b4LtD2OO_UfvjuFuVEBHDzckTt4DVR2gQP5hDVJ-4uPjPoWufqyWS7V64epvFlzCqvq6HsqsIMJEvAnAf9KHYHp5tnvKSDLueaw_XiUa-WKpoc8kH9OUGXKMCGGK3oWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت‌های روان‌شناختی و مغزی تک‌فرزندان نسبت به چندفرزندان
🔹
بر اساس یافته‌های روان‌شناختی، تک‌فرزندان در مقایسه با کودکان دارای خواهر و برادر، از خلاقیت، انعطاف‌پذیری و ریسک‌پذیری بیشتر و روان‌رنجوری کمتری برخوردارند، هرچند ممکن است همدلی کمتری نشان دهند. این تفاوت‌ها که به دلیل تعامل و وقت بیشتر والدین با تک‌فرزند ایجاد می‌شود، منجر به افزایش ماده خاکستری در نواحی مرتبط با کنترل احساسات در مغز آن‌ها می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658380" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJLIu429mlAJTXlVvhYIZcAYLrAfmVWBLFeUoZI9WY9n1vV7SlqdlNP2fAHMUWX2wt1-lTpi55U72pe-rIRVBtFKFfxMRnkODTl7WlYarVN6J5YgljuwC4BCTeAZWl41OGHT5MwOTabOA2I_REsXvgsGlvyo7LZwbYU4ahZs96emaCqmUxTykrM74nO4WGB9izSE0JAQaggQPgFvZPcgLhh_AtvOZeBzrQhVH2FRuz0IcMStnjuXOTLNd0ma-0S4TxoMoZQ2LOWXVcRXXjT8ewlEUIuZnRDzTa9-0E26LDWMx5T5AxVERE7RMcRECaK-iATkgF8rf3tW050eL6DVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیکنان بالای ۴٠ سال جام جهانی ٢٠٢۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/658379" target="_blank">📅 11:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zat79mk-7KQw1nPv8Z4iiFY0rmZQOC-6SOAotEL5LaDZCFNk5xKYhwTF3BWmiNapUPOao-0MgOVddUcAsbg2UUnPRIXm7cNG-KwPwsuJF4li2T4hxVMndnCHKGWsN2bWGSrJRBymKAoY_iQ_YD1BUHObC_g_pKIDL4D4s6R8_OFymT-pV-QBz_WS7T6IVM9btG_DfgX0Ev46OK4W77WwVM1A5OOCxmArPm3Lt76IgIAsY3SvSqhGmzUUMtB1xyB2WVIW5PnHRDyW5QFnOB7jR29FBGLiZd_bmOL9DxhLPF_jkMJDpAZyGyt4euzS8sRuKSvJ-1lTY-Ws6qseUMXQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در محکومیت نقض فاحش آتش‌بس توسط آمریکا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/658377" target="_blank">📅 11:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad965b180c.mp4?token=U45dqAVwCPZPKyUtoC4IMauaxwYjpfS-fgqjtSjcSj3NEWCx9hnJVFy6c6QJ7-y7sBz_GTR6uhZubKzBWsKX2emq7ILlNXo1P7c-hD1vbjnsDUmp_5v7Qr1sqAev_yUL2dyvJC6uT5ZCjHJEQl9ki431AjiarA_DcrfB7ZaSbLfTbCiX5uje-BXXAKOjsbZjFcx_Cx9fB69hXEhJlDoJEc4Q6f0QpTT1iZosKFmKdu480p57n1_WdZuqDpGMkrYKDiMHiB1OWqcEMGf5DPzKCNNzydfjE6t0lu91XG2GRKXymmlHrZyI9ZsImH1ITh4Em6MxAxrkR39BlJiqdyfjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad965b180c.mp4?token=U45dqAVwCPZPKyUtoC4IMauaxwYjpfS-fgqjtSjcSj3NEWCx9hnJVFy6c6QJ7-y7sBz_GTR6uhZubKzBWsKX2emq7ILlNXo1P7c-hD1vbjnsDUmp_5v7Qr1sqAev_yUL2dyvJC6uT5ZCjHJEQl9ki431AjiarA_DcrfB7ZaSbLfTbCiX5uje-BXXAKOjsbZjFcx_Cx9fB69hXEhJlDoJEc4Q6f0QpTT1iZosKFmKdu480p57n1_WdZuqDpGMkrYKDiMHiB1OWqcEMGf5DPzKCNNzydfjE6t0lu91XG2GRKXymmlHrZyI9ZsImH1ITh4Em6MxAxrkR39BlJiqdyfjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که در فضای مجازی منتشر شده، نفتکش دچار آتش‌سوزی در نزدیکی سواحل عمان را نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/658374" target="_blank">📅 11:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuR48T2pa1CWZ2g1mn2tXt3qm0_qgZW0IFtkgQqZhlPhmOcnLO-FYDw8lGrVvtTs8UkQCl9GG7UiIKMBAi-SGwAKZ4O-cqG1dmwy6NhL0O194AwuJZlC3LPFJlQhFcn4EkqegeFcCWgafvgOo4pAaFs0AqXFFjZF2RVCW4DfNqMfsMA5T796UV4FYcK6srxsVjf-5T6Stnv1CY8PtbY5BaBW6PRmdoolLn2OuQ-Iql2FIrK0s3paanT-6L_y6XIF6yUkXDL6BtGWUCExO2YVYXYJ-wUfzkGa7KDnR8frQEQDQ4vBVaDrRuZDYc_8UTIghlDuhf7FaR_K7d3ons8mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دیشب باز هم ترامپ گفت توافق نزدیک است یا ایران به دنبال توافق است؟
🔹
ترامپ به دنبال ساخت واقعیت جدیدی در اذهان عمومی است، او می‌خواهد القا کند آمریکا از موضع قدرت مذاکره می‌کند و ایران مشتاق توافق است. ولی در این بازی کسی که بیشتر فریاد می‌زند، معمولا دست خالی‌تری دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/658373" target="_blank">📅 11:08 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
