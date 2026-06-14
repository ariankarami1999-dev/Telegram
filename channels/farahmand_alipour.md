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
<img src="https://cdn4.telesco.pe/file/ZrXuPUqlNrc0vh43nv6XWRLjb3nlEoLniLr96zNXgYPtBnJ3gyEWIxVrk1WGopuJLjDaEv2_l2JxUCqQqHUU4z3ukiUC2_xA2x3lO_6xPWRwuS72GJRqTQqL06vgJuXggT5i92JxraNI7LIZcoNWtrVpIV7OsiWJh-38rbDYXOHSuH-Ajmjol2N7KsKDoEniOxTyyxKXYaooz6SWWgaqmfHuVuoHp93voWwzgLglpNWz3bWXu-jYlPBVjaNfyL8TfxCopDqG2QaHZk__Sa81ee5RzxXZaPqs4Tb81UcAEPQFL_CC9_gN_e3BH0FS10LG3Q00_UucsWg08j0YKDNhOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNMVmk5kk9580hCIUT_or_h0VtIQFJr_H49C2h0nZxUAYhiGraBg9eADo67OEtSclphit2yRxIRU41bQLssY3MxUrfsgg_s8CoDxRw_nBDBQNrQq_LJo_w1ZnOTadeH7DjlkQQLsrXgz-2UymRQ4DEuZf1Xq9RjWMwfS4AR2EaLsUY7iSJHzaWbkL5Oqbbxh-U6S2FMIebSKsMYef8S8lBePHLjPeU1ijhJryZvDtYGsbRChtndunFCOdO46pNYNjx03fUPnOlybq84nH93YJaezeaRjLuzWka9sxTYXjjml3Xx2iPn1HcUgPQVaKsP0xkCQGKTagpN4Kvp8u3TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCih9Wib4QqmE-nmlaYMaTAww_1_BKpyJYTVv2ZOMd-hrWF-Vp44dbm9FbzDE9N4HtLIm5Ub1jnCNU4X5D1fHdGmw05wH6Dr2vU3CObOS4VpKgmktmRRGIpaV1PlGOgUTuovF6m78HtxKYgvobyT-yj91baQgxlHG6Ipd6qnnqWyqyM30J82m1cc1RLEPag1GodvEYB6jsqQF21Y8lUllGZz7SLtKkzRt-pTpAXbv90MDW_tzZIUSG4TiIkY6j118Li1QiqjEj4v-2pSQpsjmiOuB_MZG4JxeKK35Uk09rehQc54HMbegpsgIqf6zDnajP2DQ1gq6toc7KwLss85OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=eAysldjlsqceRApPskBWBUvGYuLqnczF-RICTMtWLrqLhEQjz4a9Ua5KnKsg0sl2ce3SAYtt0OXZKgH9jBr8jTb7Iy5pTcqcdPkVotL4W5cDLpg64n2brMwD_8AjdzB_UkN6LqcwRuCabDkx8IbHJuwR2e612_mV-E0XRLYrIcETtJKCTTScgfrqbgv2shdZ8Kz5ydCCiv0L4NxrlSp4ajkUfJbjX5qGuEddq_9ga17xvcAl2j5tjtE3WItRplqbdM45RoW3039sZktlxJP7ZG-6D3RMGIFnl-9VWjdIbRcuQTyt0Eq328RpJRVsps621xXAe9diDLFRrJ0v633OsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=eAysldjlsqceRApPskBWBUvGYuLqnczF-RICTMtWLrqLhEQjz4a9Ua5KnKsg0sl2ce3SAYtt0OXZKgH9jBr8jTb7Iy5pTcqcdPkVotL4W5cDLpg64n2brMwD_8AjdzB_UkN6LqcwRuCabDkx8IbHJuwR2e612_mV-E0XRLYrIcETtJKCTTScgfrqbgv2shdZ8Kz5ydCCiv0L4NxrlSp4ajkUfJbjX5qGuEddq_9ga17xvcAl2j5tjtE3WItRplqbdM45RoW3039sZktlxJP7ZG-6D3RMGIFnl-9VWjdIbRcuQTyt0Eq328RpJRVsps621xXAe9diDLFRrJ0v633OsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVSjK1Pys7o8iLxjYOIOToBXmoeGDk2jjeAMvCH2D15uqlr5gz8nukm-dZi-QrF-ubzMK-lR6adqbNfFDmtHd6RT9SGexlOz7cOwkeVmvbki_PFepCN-aJYVEq7klvtxZSzBytgbacvB-0t7Yd9c7yqQxf8c_CoTMzu1yGx-yXPXqrczpQARsO3WIDaoFFZaHd-fj2aCJxayu7wA1usIwxMSRc5IOLWxNWQuMc2v97DQgsdbsHeL-2i2AOdkg0ZVQcnfRsKfURsCuo1JsH_SutHrhriEHRDSRMF3x1Di4ecpsgI0vSSNyAvWfCGH94U-UZof1ddOyWR7dMaLJu0-Zwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVSjK1Pys7o8iLxjYOIOToBXmoeGDk2jjeAMvCH2D15uqlr5gz8nukm-dZi-QrF-ubzMK-lR6adqbNfFDmtHd6RT9SGexlOz7cOwkeVmvbki_PFepCN-aJYVEq7klvtxZSzBytgbacvB-0t7Yd9c7yqQxf8c_CoTMzu1yGx-yXPXqrczpQARsO3WIDaoFFZaHd-fj2aCJxayu7wA1usIwxMSRc5IOLWxNWQuMc2v97DQgsdbsHeL-2i2AOdkg0ZVQcnfRsKfURsCuo1JsH_SutHrhriEHRDSRMF3x1Di4ecpsgI0vSSNyAvWfCGH94U-UZof1ddOyWR7dMaLJu0-Zwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxvMDMbyy1RBGs9z-I4v_VyISib2O9Is0Mg9Q7fvhfhE2irrbBeimiX-jY19R8na68_wfU2gGtblY78-BdkqjkiIq6xWrvwZI8VWf6FzBDuE8WISQoxtkRdNS8zCJ77OCAZTry_v_uONtBfcS05K95DHN33uTtU7fBc-FM2sbzdSFlKNBeVgH8zp7-QfWak-TNUDuYQfjHjTwlnJ3pxgtma5YeGYfqabv0AOZoQZQrf7bHjI0wvOAfjs8es8VDq4hty-oKoghtArPBPpiKBgfKRaHJ8x_aNkFJC_vsUxlHJZXaQXVIKvvsrlz45ifouYzzhuLeG2awBlrB54Xn9yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=LQmMyXxwzeJoQRKEjBKf2kbP_zmJrzVtjIrC34RQpqD_KRnxY96OK0Pvae10eRIQXd7x-aDjtmqNkB4g0en2b7qSjUjOoR46wM79A_-a4i3r4zrGcKA6Sco7jblAGG1NO5rSl71b3FEswXqLQY2tNaUJpkNP83VrtOoPX4v3wYTOsQLc6uloCVQjJUekQFs5Q2RWr0l9OmjDH6SzpCcuOxODWyRTrLf35GGvqJ6J75pstHscAM-dVPK_v0eTfyidZLOQczg7mqoUHmSPDZBht4etwdOfif2hJozPtLtABwF--c5t8eyx-2tY1iwpHO0RynQYqs5xVKzUV2xiLB0bwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=LQmMyXxwzeJoQRKEjBKf2kbP_zmJrzVtjIrC34RQpqD_KRnxY96OK0Pvae10eRIQXd7x-aDjtmqNkB4g0en2b7qSjUjOoR46wM79A_-a4i3r4zrGcKA6Sco7jblAGG1NO5rSl71b3FEswXqLQY2tNaUJpkNP83VrtOoPX4v3wYTOsQLc6uloCVQjJUekQFs5Q2RWr0l9OmjDH6SzpCcuOxODWyRTrLf35GGvqJ6J75pstHscAM-dVPK_v0eTfyidZLOQczg7mqoUHmSPDZBht4etwdOfif2hJozPtLtABwF--c5t8eyx-2tY1iwpHO0RynQYqs5xVKzUV2xiLB0bwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnoSkR-Rj9T4YzlAZkjvyNcX4JyPrVEfnqYg651mUf94GyN_aUlKjffCKg0V_cloFI8zkmrWe8NJkHlPy5deabB5F_J9AJgsiOz2qirxpyiC6Bua1xwS5smaHPj2MWtlEo302W0Krabf7eSAEa44xZczzREEUUiLhFCvMI3mPjxEfiKsEUfYHB-wW--RlWXxMPo16AX6SENU4HC73IElhqqzDvN6aCf-04cbUo1XX6_NaqMRfFVFdQmoq3tses3gOhdpQHgi3IblIUuZlUTQubywHQOaUBpX8hiB2YJCZcp7ObvtpqZIok_RJW2HYXamKQsSaTlKx5EocN9n0l5Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPeYhVF2UVVvidUO1MTL_kc03ielRCXbZTP1c_rP6iRd69Pzw0outZj2adyL2jSZsdCBohZVt_0Ej1sElyoR7I2ijoRyKTxSpqvIMr_0Pb7omZ6IsBzU0RP_V93Jh4s3M_OBm9BN4mCcOd27tB-7jmMnsqnJpk9C-1LBbvrc_-hn23GZ_QR1miAUDF0sA8--hjtLY2rrnh0WncA7In4L4E6uoet7G-vGKBvzuAee62vVpYH2e1sV_iYRJ8zT48SfzA5KsTlQa8geHN-XeCRp8KGRHiendeqhm8CT--q9srjBnLtxql5yY_ib3pKWa5CiY4qRwoda_ZZfPnIjCZc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTh-tJwWK6FfIre48N7D7KOWU0jsjUTbi4EkOdf4gNQCbuvN03JzxkoNfRg0RSsPhaWMa994w4s2OsmuL3laz8xLAjNrmOQx2gVK7J5lPb9aRKzT__3KfOF21KUDaaSH_r_tET_DOIc0PGzejLQNHH0W-F1dt6KC73Pbiw7NKhUGauV04PzdQsHwGD3YSTf3e28Y4sCHC6KpJxttQPkLRqwsHBHIj1ZPPsD2U3-L1t3UoMUTd_nwK1v_Vgt-CQHrC8yaxJ2REpgzXV-S0biy3FDePfQ25I4wNp90jnscFx1dIKPDceJrqzciJFjoXP9dShAYcP2mbh8xR4L3q742Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=GMoF-QJEDa7V2CnHgOB4Ow7ydDMWlxpvFcX9vQT_gLHh3tjluXJWzXtVg26ipKvyCF5gkgc2S8l3PSXkc_3plS9YITIRaKoZma_RsYyJCNF7eVsWC1LUsLsJIj3STCRgAG1CheLRq-mm33Vp1mrgmTDvdKz4sI1g7GSkhdhub3BvQJS3ouBmDhvJ08G85HX8rWzONPUPTIsFwN_wW__zW1UGEu1pl3vJRsrFcqNnUKFQ4vk2pN-C89NlqxtyTRufoIngbsEVgLCmrNPptNZwCTrFsNaLolgIzRbRksiB_iX7SoRWuxz5a3VchLyppX1ryZB_JrKfzhqn8Wge9NixpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=GMoF-QJEDa7V2CnHgOB4Ow7ydDMWlxpvFcX9vQT_gLHh3tjluXJWzXtVg26ipKvyCF5gkgc2S8l3PSXkc_3plS9YITIRaKoZma_RsYyJCNF7eVsWC1LUsLsJIj3STCRgAG1CheLRq-mm33Vp1mrgmTDvdKz4sI1g7GSkhdhub3BvQJS3ouBmDhvJ08G85HX8rWzONPUPTIsFwN_wW__zW1UGEu1pl3vJRsrFcqNnUKFQ4vk2pN-C89NlqxtyTRufoIngbsEVgLCmrNPptNZwCTrFsNaLolgIzRbRksiB_iX7SoRWuxz5a3VchLyppX1ryZB_JrKfzhqn8Wge9NixpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut9X9J7g361syPqP9n1i45gdwEt0IQf-tOiYnWEZrM4FHAj3GDE0-r0lrKBrYgzhzWmqLuZIQmbbe7Oq8N4w7zISvWZfveXDe7hoJcamk2v833LUYk6P51c2qdG25yoy6hWiNzc-1I0G9Q0314OWG_P0lXMVaz6hExP0PWaVUkDUpOlA1rzBPK0v8YGA6UMSf9rZpPMfF1jbxdzdS6Py03dX46bjp6IEF7DD_kGi-oEt9tcML8kF0vaBGmExQ6ZEnDzgccqqwQTdUltHk4dxLdQ4uO4BY20ghrLWbvCEen2GiSFd4m5rY6r6VM5nOSgrQN4KqzuuB76TKqmPgETAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY0vgXIDaO8v8QGHupnLNwzyfwnPy-XdjmVuY6zI7XbgL5GzBneh6YEk1JqUncqwvFL5J4LSUXqesldFBQT9nV3dpcmcqr6iuXaQOFZ99N0RJwOgsfzFzLPOUt_xghSoc32OKEJkySRM7yj-MdajTqUOSZls5DuGmBJccIySRj9a9C4a8hN5OPwc7CWTrikrpITU2TpOvTtI99SDDUtTVvCfDdPL3Cpo1Qw1VpQ-gAdfngAZaXgvuuOncEQQuZx0zbWdPr_w8Cm1RCA23oVb6NoGJjz0lPd-og_My38j8-gqlCD4aJiLhbWsJcZdjxZi6QmYVrYTwsvChU0Ekd8VLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCiaxrFWARb5QcDAJLks30DAURilfzh7K7tbq8OiR3XiUYUmPFi-1bO51QWWYPj_Wu0eCCSZdcLFGV5hlKxK3c8lIisXHGq670ybYmbej3c3wKwN2p78vLOcC2K3QEViy1KF9hDwCTWws876Ho-_9C2dZDCGZsGnF5sp1o44duux_W2kBMfNnX0OJVJRzJ5IjgfOyi1-75Zck4uco9F9_fZXImQZ5-vjqI1cJMXmsgkmmDmbIRZ5E__MukBwurkMeTbV_W9e7xbHR19E_Zdf_r8KLsGBmrJH5L3PyBLkAmZl39ct71MP_PJFHTCmgzO93pKPDGtpByYoG7BF6_hYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsmRMegjodXB7b7UGARnAr3j5tqjFr9-_dUn7yvrRs3eP6O8T_rkmu2YAqWx9cOZqXHU1lejHomWO2mbkseX_YL891BUbpu-AdIzk8wpZs5sCTqf1qt9n6-Z_qyGGPjUkKHZ-KvLJEOIFEYsMQauZXBMfIkIitgThTho6zDtxOg5SHjVkCPh40m7WUtq7FPOO_t6DNf5Wjgov-Spt-nrgu91MizA8Ztk7iNKCYNPulFyMfSeVVcck6hAHSb_KxVFY94IRylULaPJ2vOCx2C2tTEpVdux_pcQhDJta41vwn8cYCTc1VzMinDU4RJbMY48SAx4XksTaunBRHKWKfq9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=sgYjfq37lcv-6Xf4Wg6NXPBhn2ZRrVV2-PvkwrGVfyNAdbBBxvxLZTpbKMGWenTjoDrGIBQaqWPw6jQaECOeO8ZkIhn3aJsN-ORZCTx446apNe4k90JZuUia4bjY3F4sYTKzkRb0z3rR3uuflVYeADzH9h2jfF7dQmAULFsRo7klRVS-l0M877xnvE5JEN7P4GomDGu5opTT-8OviisyIqs5xb9mgyPbpTmzgjlW3rxuzvzAKsrif6Lq6_mdVBQ-kaIy3LEaf4hS7U-kArGwMJ5SL2ioHlB5JD27OI7_ODCh8JHRZdoXXRYW33NBDE0khPpyTebVRjiujW38exqKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=sgYjfq37lcv-6Xf4Wg6NXPBhn2ZRrVV2-PvkwrGVfyNAdbBBxvxLZTpbKMGWenTjoDrGIBQaqWPw6jQaECOeO8ZkIhn3aJsN-ORZCTx446apNe4k90JZuUia4bjY3F4sYTKzkRb0z3rR3uuflVYeADzH9h2jfF7dQmAULFsRo7klRVS-l0M877xnvE5JEN7P4GomDGu5opTT-8OviisyIqs5xb9mgyPbpTmzgjlW3rxuzvzAKsrif6Lq6_mdVBQ-kaIy3LEaf4hS7U-kArGwMJ5SL2ioHlB5JD27OI7_ODCh8JHRZdoXXRYW33NBDE0khPpyTebVRjiujW38exqKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0CRItJtBcPUX8pFoqxj8ruLbQTiPXKheBTgHBQIuczMITEvANCd0rvzVtfQdpQwAlizJMLNwQjhUlxrJVIwMtexM2DCsjgQA8L4lIlq2ZE9OJ6Dy9aLHuAxFpU72wbXxKxXa6gomJBdPH1ZDv4Dzh0GlySmaTRC8XA5GIKnDW8ocAE_vguAveUNlwse-bKwT6HGoUVcfLhB98kbFgcUHtHcuz14zZeBRtwZefcKWJTDBKlDMYd5AX-6jUoS070_oB00HTyGCV0mkXrSxi1k4AOB8CNpBmtvz_t7gBQ7CfSNRqdAcCZY-2_bglZb-k49cEK5jq8BzYoAudrMp6_JZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuXFBWFGEhtHhIy4NatZhJ8mzRxyKnly7ZHl5wwP8QxHZRgr-m5QEhh9DBlUnjkVAsIQPri6wIjIL3XdfkEZVv2t09IF1ScEe8qhB0RyLZV77OyTMh5s9ExG4vn1BcgG3uZWj02yZUhOIDJrInC8xArQRbZw8JOLqrycLToV1aHbfKjgn93rUoCGFhdPtLUl51yI3CilQLbNyZkZk510iw55AjTVPn0HicDmdDkRh49pnklMqyuKh0QTWO4S-Rm-uzKUQuXNGHtw8Wy9p2Ck7YinA3Y-Ru4KN-6KlEKgLXE_DoA9U8qYwwKPL-_oOcSgKPGgA61pBlEnDRJ_U1MGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=HU7hMyhNp9vkWiyk5pP-FodnCwQSUud1_dAia2tkiAcHe9UuApakJvvZt-9CeghI-3Xzl7KxkevUBnhMz0Mg3WHDEWRLFWjo7KtywjLFP28hiVzPcKuymic9RIcOo-1WdbdWapRqilWWk33dN8IZIL4bANueFAtYVoRwcgq1XGBJt2FPJT_D1Vk0vRhW1T98Q1X9LAvk-qYa4q-W44G5ZXW-Gm70yd9DLyp7Prb76PPSnn1Cm2ancucXtWT9mjIK72nO_i03ELzsN0N-VFXilCVQ8dtAC8MFfce-qQEOkq5EPGCIGlix_SD5bdzHIy44ur3pJDkt6-JNfhVT8DDr4moxPYUPInu61nLCu5Hw11y2ukpPXhIOY4G0o0BAVyS3-uoXwPaAJxeAfW_QPViHfWNQfwMQDBiMbu9svce0DPQ1gtoSYprX4cZUk4iHAWmWVwfV6SEKNhGvjrMBnHiQo3iuSSKNHvXZUUxpl589mv-4nFLsgc5DlpaNjGFvjIXdwV3KVdbrgGNvj3_lDvw8lpW9Vw0CffNykOa4YUCiCgYWAlacHEBFaIhr9X8KU2DpU458gQupAZ79gDJ8G0iq5DIMCJ_8xEbnHYGaXO9eDVoXUV7IIyggUaD0-peg48FkludBzWfHJ0m2qDRR61nW9YNtDYp-WEDTxfRAdHmLLEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=HU7hMyhNp9vkWiyk5pP-FodnCwQSUud1_dAia2tkiAcHe9UuApakJvvZt-9CeghI-3Xzl7KxkevUBnhMz0Mg3WHDEWRLFWjo7KtywjLFP28hiVzPcKuymic9RIcOo-1WdbdWapRqilWWk33dN8IZIL4bANueFAtYVoRwcgq1XGBJt2FPJT_D1Vk0vRhW1T98Q1X9LAvk-qYa4q-W44G5ZXW-Gm70yd9DLyp7Prb76PPSnn1Cm2ancucXtWT9mjIK72nO_i03ELzsN0N-VFXilCVQ8dtAC8MFfce-qQEOkq5EPGCIGlix_SD5bdzHIy44ur3pJDkt6-JNfhVT8DDr4moxPYUPInu61nLCu5Hw11y2ukpPXhIOY4G0o0BAVyS3-uoXwPaAJxeAfW_QPViHfWNQfwMQDBiMbu9svce0DPQ1gtoSYprX4cZUk4iHAWmWVwfV6SEKNhGvjrMBnHiQo3iuSSKNHvXZUUxpl589mv-4nFLsgc5DlpaNjGFvjIXdwV3KVdbrgGNvj3_lDvw8lpW9Vw0CffNykOa4YUCiCgYWAlacHEBFaIhr9X8KU2DpU458gQupAZ79gDJ8G0iq5DIMCJ_8xEbnHYGaXO9eDVoXUV7IIyggUaD0-peg48FkludBzWfHJ0m2qDRR61nW9YNtDYp-WEDTxfRAdHmLLEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=j1wNcPWCkr1LNyyxaxPETXFeQSsdqPxmpM5c0ZXgvjL491gpAvohEdvAOQuLk43Tha_tAkxoik2CotVRAgvEAK2GSc15FnCfRVmkqH-9azpkRp-F1RLOBQbxUDuOUEm9fcIphCqSDd-MNPDTpmw5uLo5lGG8UzNGrU6E-t-nFG3WI0bQ2JwKgh6G2Euy-kp42boqbeYXaf-TV-sYv1khpw4Kpl60KyWhLue75IL5lP3CHCkndQAGiKUSmghv7ChbMDOrJgCvKXXqeiJWhkDbRwroSIOHdO2EtQGqJ1BZgNe2T3jk6zidjVDkkrMwFwnQQjbCrlXr_eNdrNpnOYwSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=j1wNcPWCkr1LNyyxaxPETXFeQSsdqPxmpM5c0ZXgvjL491gpAvohEdvAOQuLk43Tha_tAkxoik2CotVRAgvEAK2GSc15FnCfRVmkqH-9azpkRp-F1RLOBQbxUDuOUEm9fcIphCqSDd-MNPDTpmw5uLo5lGG8UzNGrU6E-t-nFG3WI0bQ2JwKgh6G2Euy-kp42boqbeYXaf-TV-sYv1khpw4Kpl60KyWhLue75IL5lP3CHCkndQAGiKUSmghv7ChbMDOrJgCvKXXqeiJWhkDbRwroSIOHdO2EtQGqJ1BZgNe2T3jk6zidjVDkkrMwFwnQQjbCrlXr_eNdrNpnOYwSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSM9waJUfDv4tqs9thE1iEqbxisCW8y896z8cDrEv0wnKgqqx_Z_gyfH7tBt0zYXwwmOH1SNhKm7Pky-wsFMqJye-e5WrNDq0WCSjjaTWLhUpHvOAtfUCRyROj0w81YZCjD9ZgHILWuw2dZnHGVCuU3CyvXCq8UOPH1M5g1rIKktWJscdqaTPEs099Vk5slkr0eEPNnXyj7cg52saUJ9bSkOemeBuk4sszErFOhG0X0ZyjrK-mP5hQEcL0tHuoajMeTC7-0iAPwl9W5ZRj7uVYWAeir8Gk4iIpOUVB5YsKBcAxPbE3Lf5fcNwVEsNC1snV-mAL9-gKYT3j4UAUlNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=MAatiBJ8TBL4hYAmgRqXwGQOuwcKVx4IbkCv4xvvPS69OODPXe2RLFewKdLm9Vs-chDMzSstS9JDScZf9SIz1TCG-XrTJQAxgTSt8fHa7Sc2R_UFUomejT_Zf2FzDuCZbXhXYv2Pdm-2IzLR_fqHURGeEwLGDGE6x6quhzU_rkHXUbSF6RcsPHous0xJGqQFfmT3ppzncCAKOqd3NYk7tq7dOATk6aZY3-UXb6u5kM8gtUnWtoDzNC2tTBQSzHnT_9edBhDXsFf88gw5uKuHkyvueiTpKFyjlT3nW6nax5neqclmJmhYMgehSeVGGzYc0dRSiZ5fDYfWlpJN4ViLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=MAatiBJ8TBL4hYAmgRqXwGQOuwcKVx4IbkCv4xvvPS69OODPXe2RLFewKdLm9Vs-chDMzSstS9JDScZf9SIz1TCG-XrTJQAxgTSt8fHa7Sc2R_UFUomejT_Zf2FzDuCZbXhXYv2Pdm-2IzLR_fqHURGeEwLGDGE6x6quhzU_rkHXUbSF6RcsPHous0xJGqQFfmT3ppzncCAKOqd3NYk7tq7dOATk6aZY3-UXb6u5kM8gtUnWtoDzNC2tTBQSzHnT_9edBhDXsFf88gw5uKuHkyvueiTpKFyjlT3nW6nax5neqclmJmhYMgehSeVGGzYc0dRSiZ5fDYfWlpJN4ViLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amJ76g0TO3wsQ-7q7oPc_fQjvtKTll2Ols9jDH_4gDLSa2cB6Q_ZDBooGU-qBupb3HdgVdF9K0eNM-wHN74t_Mjjc0QdM2CwdfKnPAVI6w5tqZ06p0dWa9Kzl7T3RWClbeTrTibaj7HS1QHMeL9T1XvFM4p3F_WVWxPxhUTLQ0XDyLOIbrRuu9ZuXANHYcZWUFb5h19zHtxJ_SGCwaXgST_bcAWnN2quQHHEygfGGHAUUXKfvlZ1Ode9rrHrWhfbruSKL4pv5cDGit-JAM2ap5t9WEHeWWapj3JFFozpNEF7M6ZpI2EroU9AQi5xaS9Bno-6d-FEPDihf3tjvdxd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=OD58EQjHrRTx3VXpzLTqVICELnZaMZ3d1AhiKdI8d1Nc70U-ks-W9t9NJQMgNFO1JGgWJJ06C9do_8Xu0gvq3qoK8CdDb87TTYR-NLxxw3DZd3XxC2Uol4jZyYGuCvVvFHDJmCjc71ldek7k3cSb9WMpvej5yRLprENlSm27GYcJ7Fli8Us7sx1IDQSrKtKLZG1n44_wHB121ekQSFruQysdjGhXVadmpNJExRHauQ9W05WZ6obhdUQZkURHNFra3UT6C7ffZHqWSEtf8ntY225w6qnmyJpgrv39Q0E7SG8ud47Csr4LgZKze-dueaO-KIikjY1DKNlYQholt8aIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=OD58EQjHrRTx3VXpzLTqVICELnZaMZ3d1AhiKdI8d1Nc70U-ks-W9t9NJQMgNFO1JGgWJJ06C9do_8Xu0gvq3qoK8CdDb87TTYR-NLxxw3DZd3XxC2Uol4jZyYGuCvVvFHDJmCjc71ldek7k3cSb9WMpvej5yRLprENlSm27GYcJ7Fli8Us7sx1IDQSrKtKLZG1n44_wHB121ekQSFruQysdjGhXVadmpNJExRHauQ9W05WZ6obhdUQZkURHNFra3UT6C7ffZHqWSEtf8ntY225w6qnmyJpgrv39Q0E7SG8ud47Csr4LgZKze-dueaO-KIikjY1DKNlYQholt8aIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=awK_wLctyP__XZYWaPfLS3LHhb9xwgzpy-_jn_kr0UY9R9zYQld1eDtedeaNnBajrQNVy1VwoOP-dBLjVfEl3Oj_77OLZq949BxVHfY0g9vGm92d1CK3GdoKQfiocip8rGsnAIHLEtQhjLIS5Jo8o46-G_cPlHfwqxgLTIBHo8KC2UdhVOkJb9DPvKp2aCGpF9ykX3VpdgqvcQlQ_F27EkcTI5VuFmwJuW6DK_lt3RhsZZSwf_LV5Pfv0yF2TwCUnUA13E1SV8E74iAWR9Sk_DlFuQFiuIAU15t8UiSBSFxcSMkpOoccJfETHd4feYvqNBaM52483BEC4O5K3j9oWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=awK_wLctyP__XZYWaPfLS3LHhb9xwgzpy-_jn_kr0UY9R9zYQld1eDtedeaNnBajrQNVy1VwoOP-dBLjVfEl3Oj_77OLZq949BxVHfY0g9vGm92d1CK3GdoKQfiocip8rGsnAIHLEtQhjLIS5Jo8o46-G_cPlHfwqxgLTIBHo8KC2UdhVOkJb9DPvKp2aCGpF9ykX3VpdgqvcQlQ_F27EkcTI5VuFmwJuW6DK_lt3RhsZZSwf_LV5Pfv0yF2TwCUnUA13E1SV8E74iAWR9Sk_DlFuQFiuIAU15t8UiSBSFxcSMkpOoccJfETHd4feYvqNBaM52483BEC4O5K3j9oWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq_lEhESbQKw2Qi_xsmBmAitV-yj4kzgcQnTszClJzFsmmL3o6Uu3Uv8HMYlI1RMuD0K2sBzQKf6rGM2nv4gCI11LMw6ahj4mL-1cpGMvG3GaZzOScyIMUPyLVOyvnNbX5Z5qVAZGAYjB78K-UoCGm6yALNcK3M7m4UjpgPA1UzDAA_fOKP8yL6UCirC7C9BaeG2fPT49VuZXLvadeeVy30cAA-qQ7HkPX6gOEEGh1Vb8Xn5q2Hovldaaln91g4ANiNGOGAMJfjIKz6cpxKDYh09Eu4XVTqElnjwKvnDbjljfZAuDz6tvcVS06ZT4DsXmvKsRfMgAn8LMMKEJz1xbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=U6LJ3Bm37KTQKO9FFnAt3iIdOsfz0sON56Wlc1C8SQpmQHDNqGigrdgMZAmAy9wq2r9Nv6xT0y8KeYS_ZiJkCIPC7K_JNvRqsaf4SvURCuKIy_Xkr9KOYzdCaDHJLxUH2TWL9k3eXOBIjJBzLn2zdy8BzHAc3P-N9GC9_oFU2K5RBZ9opjDtP5QZnfHTL1Nrx-1CL2VknzBrzkdPIB07yfnSfGvqOZYczc7-BO-BPTKkbJKwN-rIYBXcmWJAN2p35BPmi5f7ZBTuNLBtkioOuKb9aw6ykWpx9sDMTGyD-eGBZF1T73-RbzWOnUGHUQbd24l0FZgRNQ5nT7FMeKRp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=U6LJ3Bm37KTQKO9FFnAt3iIdOsfz0sON56Wlc1C8SQpmQHDNqGigrdgMZAmAy9wq2r9Nv6xT0y8KeYS_ZiJkCIPC7K_JNvRqsaf4SvURCuKIy_Xkr9KOYzdCaDHJLxUH2TWL9k3eXOBIjJBzLn2zdy8BzHAc3P-N9GC9_oFU2K5RBZ9opjDtP5QZnfHTL1Nrx-1CL2VknzBrzkdPIB07yfnSfGvqOZYczc7-BO-BPTKkbJKwN-rIYBXcmWJAN2p35BPmi5f7ZBTuNLBtkioOuKb9aw6ykWpx9sDMTGyD-eGBZF1T73-RbzWOnUGHUQbd24l0FZgRNQ5nT7FMeKRp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFMPRaJ152cg250-tYqfyTbR7V3oyz8EqPeONWk2qXBPceN0Ul3BQDYi_93jUui5WYzgJEQNnNmlTu0bkiSQdZRxwvCtXZzrpUnmvcAGhLR431VKA43_4z54aT6g-gRxs6YKp0llMrh6FV6S-EtXFeiVl2MJ7PhqQi2rriNkZsbKkuL_jNLhH06vdfHsb9S108WMHm3pAocShAH1RfRtYJqgXdDJZLgtRxTZAeAaV24lfA5UWDpADEQ1mpk1blacYnypivku4e83-yRCQe8CxImTVPO9-Oap3DpxNALYWAygyrTROzbrNM2CNvjbCZByH8nmxGrt7D5BbWn0VlhNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQZrS_N7h2M-A5idqAP98CD7-uMyqN2z-EB0KNzkM0jjwHoFf6VwBdgKLhYyQWr2OSlww6yv_vAWZ8utW-cZkPVPd3FAF4C2KCsNWweOHu7k9NXnPo_Vn338IafQCJyy7SmC0HIsvFAcDmNyEw4gSb-jqIqgdW2tH9FUmM4OtMHrRlFqlZFFrOJQKsUfo5O2vAfd-Pgvm0MDCPzfXQnD-UQ8yeoH6ry8panv03XWJRF3qa1r9lp5YddLaRb33_2ACUdvLievj-RbVIHH7lUtTkUnZUoraeUKbZifPy14Rbajmt6e7xwL7MxDGNZcxkXdS2O5Ga4SmGp2Eju6FfOzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbKmHMkfr65fCWmGyou6PAvS9XiBXSzt9DRQnA7V-7Bikby-2P2Quz8pcIgs1UD0AH9S2I-X2vq_9VKcJoJElgg18aagenVa1JRCn1Iz8yFrTP6DozpTSEqqZl7BmyMLZ6VraixoU5rEXlvb1FnSj2-F0PVbliaQInu8FuE_m38ton4Cn_YiTi6gmfJAQfu6GMjY7U4VcQVfnJSWIwCIXVsidUweoKsIyBeL_xNHvzNLziUfStH760OHs8doYjwdhJf16zfm1Kg2K3b2HNumGZkOh_93aL0fwScPVEUSP1xCVNgKv5ko8BHFdo0DvKpQn5-R1xb_LwnWtfgYw-H56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvjpfMP4o6rh8V-3EOqOBeAsZwP6FX2Wwgh95wskVUfJR5Jvp0R3WvMkPG0GM-FM0p4ZQm9Wmk2CMkTKWOwUtpkKPvbctlfX7oR53v6-klM2twxhdVPatOzy1hsT14ZqI1jaceu-J1WTYVwo4tvFfobNv_ERSxRdg2WZYyi8u_BJYhCf2iyvn0CmFp6e_5CVIqrBbMGCymK5IgZ6DxOClVQIWWv1ejUCPg7aIN0Lznka4W-MR3Xg4aBnoiyUC61vBYJ2qfYHgwG_XIb5N8AajjeyGaAgW3sw0eOE2SuCgl6xDDq-ElZi-SbaWhQ8QMWHv3jFZ88vrz_pZQgJLwhf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4U0Xjkm5X0b-RGGdcAxPAg9xP_SN7KqtY0d_8d1s5TZFVlnwshvD3hb8tZcg83BgKV-5mC6HxjcJeSpzZuK5cY6gxFI6CZIKaRq1psN31F0ZCk6qrRbeMog6L1VUxRtre5xOzD0P7-Ybz4B9R_7g4NYwU9JVCPpof0U_TZDa_psFKvNNqATUSlOfdLz-BB3-4eLl01B8iaE9EnYBC4W8p0cY5bJuxUCAHmKjTHNIpimXnwt18PhlJDOxHw0s9HEKahbIeq3DygGPvWofF-Gr4TCT9Y6yz23SZt1TEouaH33WDsADoMALR8mkabHI2Es5b2i47so9UH7n_OFXUMr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfSpVV1UCB0-uHPbcHfXI9oQxekYIgrL6rQCyAMOP1juwNLh4gFieuCzpZ0nqdqEnTAQskPYfMf_lXUsCwKO5M55yi9byzMxM2xwf4uMtJXzoH5ZU08rKo8290T8koCABpUVLTimGK2EnJl2Dd9t53dlfgjKIUUmzsyt_3n2g-Tv_-qIlu8jAwiIernZiToz6NcTJi67ITWdKgBrfv1yk0LVei3iQP-s0fV1RLvnWj4vEK2Dr38XF91bCOxMRgm-9-Ap-TJ2lCPcW-ezih27uWUXXxxnBJFuiDGBHj2bN_ItnQHwN2DujTHoUGq5EUNwxkacVLmSlpv_JLp5aG5iWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=kINkI20CD6rFP1nm00YO2S1MGymgC_CfXqeMguMPWxdcwBGtc26Q-gtfT60xKSGRDgy3vtMyX9a1rfEbMVEYp3SGavgPRuY66bbRvQVd-4fldvfK38sicHvsTR883xT56gvaDOVEvmik2gb1gUnhwqI6GRhc1Q1IjU4YTfghhQ6SGHu4P6vul0UZxWAkVu2KIYSuy7xC140-VFN7bmkvjIrUw2k76lW6V1sIcLE0f_1H_6mumrU2QKkVwNMlXDBjtqEf6VLqPClhyzK1ShyqPo1Cz1iPqZfvIlfHHwgrLs42phAJhjsDSK0DtW3TgwG0iCbLVK4UPnm2VLKM_lGImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=kINkI20CD6rFP1nm00YO2S1MGymgC_CfXqeMguMPWxdcwBGtc26Q-gtfT60xKSGRDgy3vtMyX9a1rfEbMVEYp3SGavgPRuY66bbRvQVd-4fldvfK38sicHvsTR883xT56gvaDOVEvmik2gb1gUnhwqI6GRhc1Q1IjU4YTfghhQ6SGHu4P6vul0UZxWAkVu2KIYSuy7xC140-VFN7bmkvjIrUw2k76lW6V1sIcLE0f_1H_6mumrU2QKkVwNMlXDBjtqEf6VLqPClhyzK1ShyqPo1Cz1iPqZfvIlfHHwgrLs42phAJhjsDSK0DtW3TgwG0iCbLVK4UPnm2VLKM_lGImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyRqk-jkXhpm2tTAopkKnzt54kljKd6t1VHO62QHOptOntGwjswQDkL29sseYqLZ0A1KaSttzvpTdLRnlgQzH5BgVuZXPuGNR9xPd5MS5nmMkwOHBzA-vquABOJrQrQxeBDiYEQkUMrSZoieehDngO0W0Btznc8sEtSs6ojSH4dkAKcJJERRqNSfG43EAhi1epF3nWXNsHXovucPeTnMCRpEpGGZdY_JKiO5nGoxcbvsMCozDvu0ArSFv0UOeRcss7ywU7pv0Z8TZwoOPquuQjt9B3oFTANwfv4PG7N7T_GGBkej8NgpIFuq-ucsrHyXF3TdGxbx6X9cBW0VDSI2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7YjrvQ8OywB-Z4iNAZOGNVEw-MCTqAIahyQ-OJ7JWKPLtF2Nqof0URSXnWKyTJ3JGXRbPW8PdzrNyagm9P7t1wdLzb43lX2mdkB151onumIeIIuO4UagGVgZIbjle_KDTbHFEKfVglMyQUcvJeR8CjENNR-Hn8lQPPyNm-ZlsHKDtQr2LFGJ9PTFwb-LbZ_VS5p7Y0Rmgl-cBOmuFepjaoiZo-53vv7crCKsq5K-fzQVZokiQ8Nx216sbsSI4a4TaYYv3R16ZQTMfadUgf1dNSxcYD201jRotx8eg-BdhzQHQ0xfyBcGiwWn7xj9Tlbva3L5-HBxRRFfkCTkf52_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6potElphT5xIAra_K1vDD53tYK7yw1bpoMbrFsRfVql1S95kVyFxSWSyOYRt_4AqXQ1W_mlgrtzHF0G0P9dbyGWZH6rasLCAn1zuuzfEfL-AMr94pZGKG9uKgqdcNkuhKJ-_rhKsf05Npn0MVH8_8bvnzNrMjywjTw3Kp_n09iTKXK_nSoDlg5SCQnTHUeh1uGjOx_SD9-yQw-KwYW-U0cOwHl51VwQ7ZctH-1MQjPqAqM9O42Z4yDc3FDaBdcz5Y-PfNNS3Id7xkyShx5ob32_8jlgSXF8BI1WabGHf7zGWRgpEZfmfbeEb5eKLAMWJRAjOlHNyWFntRk4gQqspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMBqoI1b3qqDgm7UC_p8aGmdMIijHe4KPPtM4T9bAmvHOwL_Trt04pRGidHNP46uDeevSIHeWvdbmQtwi8GPRKAcbQ4brkyyvjeOXEjH6esFpA8cQsxaZXV86qbRjs1PosF1Kyp5sOOWHyP3ztsoVxXREUXcL65S9tbMP2t-WxxtS2NpiaUUjZcncSqOLvPpuwI_eNxRVvJnPToQOYx1BLY9EqYWq3ajyJ-pjPI10O7cfbFjynDlx_-ptf-kEGVjauJO0eyI2R-u_C5jnIWbYYgERUwfR-65oChAezS8dNRjtSb-59luTZEWLRa8NaOlj31HisVfpSlBtIHg-k0Lzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=J9FFGRoklRe8IGDmt0FrNzYJzzmAHe91EevVqSEWO7Zj6PghK07kVRYtpbIBKFElhSwMGu9QHoPiQlbvho6YgJPUnI5JZRRMIynH9gNYUM3q9kc6JNZWpSowV4XOBRcaJCO2GSmDnor7vAo_pojJRt_0VaHUu1iOLtPt4L9GQUqfQYsvzJmjRVOL41zfUSkQrI04VcR9sfVMVdoxc4B_dyRMcmH9HMD25Sv0Zvr22-JmxWvITLG3SKBqKpikCwOJYYE_k9BMt8bkJKVKhgK6BmAU5D5JZXXcWOz55zRnm-MBhaBbyW5IML_m9W0cnYPd6jrG3NnsFPtGMQvrypoJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=J9FFGRoklRe8IGDmt0FrNzYJzzmAHe91EevVqSEWO7Zj6PghK07kVRYtpbIBKFElhSwMGu9QHoPiQlbvho6YgJPUnI5JZRRMIynH9gNYUM3q9kc6JNZWpSowV4XOBRcaJCO2GSmDnor7vAo_pojJRt_0VaHUu1iOLtPt4L9GQUqfQYsvzJmjRVOL41zfUSkQrI04VcR9sfVMVdoxc4B_dyRMcmH9HMD25Sv0Zvr22-JmxWvITLG3SKBqKpikCwOJYYE_k9BMt8bkJKVKhgK6BmAU5D5JZXXcWOz55zRnm-MBhaBbyW5IML_m9W0cnYPd6jrG3NnsFPtGMQvrypoJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDjhb09E0K82tEBrZaLkyD_NzjOqmLN9hJAfiytQFGMr-aHjeR4aRP6w5wVatZLgtXIqztVp5bEJyljwE2cKMwFzuFS-mbynRCncKhAvD0DAaHfy-oF9Yp1dnpz2NbvBOYqW_yOP_sKg4zmpQbPmIGvh2p9pCnPMWJFZZHDp_qKu1V3yymNBE-6pezM2TyiveyrwLKTRltAy9vsrUZey7vNhsvTW9DS0ySeW3rcjbXrIE9YON8QC0djwroItxFyayn7RqmezWRWXeGR400_fT52_lhoc_2wlJUSMRUJlhdBluZVPESnSZ8TdZh7QYqdjNej-EPGhBrd7-GFC3GSMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STr3B_FEjAl1fQZy8Yk2MVWt3YTn1GBZJXlq4LhEpeAtFgBgnoXIyh8Gv7D-PLepNcBE2Ok_AEcRtML9CFi6YfyvLv_nzsor0_j3Mimkt0cR9R9b5WcGIy7qy4qDYT-zgvu0YJbWxMBwZ1k5rS1sED9jXvcPkGCgl9iRu2gOSD8VKNpA7WhJoIEsoqLlzmtnqgXBBOf3KzL0VvgEm505mYVOYaTyuq5Mj1VlnCjLb-W_gEJtw0naZG6bPoGiykrNgowBFLrelrOyPFvPevawiD-RPu6lVCqZ5Fz5Q5NDHKJLT_QRy19W1PH3RTGFfUVqmq0Q3NJXQslxXDswIFeydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfYNOwFPDMyWp4FoIPvXJcHUnzFCzwf0H3xU7hCHBSYe1Gcb8iOUQAVgO_1iatvwABnfnI7EKQ0NOoLbHhKUdCFw3EGkJpqxoi7bGkhnwePA53Q-lPDecI7jiMMjK4lyH5zC2pIggYpFf_a3OvRc567qWEImxyS054mSvsfylUcWqtelkqguAyHZjNBLgEI2GsB3UYyF3bUVZE9NiPKKLo6ELAkCZ4lyowNIpO-Sy4VyPAtXHtedKHZKUBp6xwSyqtbpUvYjZ2Q0WyrsYaSRBLxoi97LLfhA0PcbFIhi5vyy6P13-I6KK0oLRNvD8ao3w0dqq9IG32iqpZ0EupKbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap2rL0gXFBYM0rU_JwiKRkje9pM0BS4yodSj9krEGnR_ax9bykQK5JqvaFvJiPgloSAEP-eXPeOC65dmCrKGOEEsU-aTUxn2AFXwm9H_MbKntw5Ut7VBfQR78oUParsJ88OfpKKtlp6FAlzOIiz-j7d7zqiRCqrZ7guAfIFUf_ytkGNcUHDXzNF-kLppEEVcMwI9Wis1yQqnRs6wuY9AoF_fTQYfET74caQWSH7NS-oVRhbK9wRTT5vAyjvlgGS_FB-0yi_zO1o1p86vp5Q3OZbrrwI8M5WSJ1eC9KTohsQ9QD8st0u2zjMAHkjcPkViypZ9Dxt7hrAJ1UBIZiDSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H12BIMkUgzVBhRjh7KxI5Z3iLKd4eac5nweDxjaWC0LXtrxmfOUBaR8ZIY-atlQbJmNJM4e9Oi2uTZgJ5jnFscPi52Odt2WgRhxBcgtQe4C1aho7pxMgwGbEYa23ZLVYtRnvvHJCfs96_ItLKJkJSGP9wQTCTFrlOEH10v3fe9CXlvkQg78rD8qb84boy7KQWXt5b_1Ay7VnvDo8on1Flv63jB0SsKkIv_AK0icwbJ0mqvSyzXELBHanhb5ikgLOm11XP_cj8wVdVo4lVsgBYtfFLdVNjABfx0i5q3aWCB_FTNwYoCb63OE-iYDJinD6gCBkdRWPViAGmTL_qro-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkRyXXRmb8c1ZNJgMQs6nNdG6WOgWnu8KlrxJCz5pamdqQV23sZXBQ0XbM0Rnwwiv6ww8qZc-uyFdG_T0WSJ6pN9SQ6eXAVSY7vUUA3QPsvkBOXlTZISBVocTfHhvFRCJFZQ-PqOwkkiQW_lMsF-llljbPamvheyeGtQF_zOOHgXlomm-cgMZ1PqslZF0I6wQJtgKn484XgN0t7i54eAxiB65TKrVD-98PG5dvSNuA0B_MaYR5W0HP9kkCioMf_qqz8Kcq18iKblimd31p3-5ozgdQSwgZ4GdZ5hg_E8H5DiFEtOtmiEQxgpmWfx_vre-zGhjGkuk0otYj41mHl7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUfc-mYnHrDXkFSC6OjY7rJRhDNdz1fITmn8nDrWqkuKjwWELDFRO43OemeE5kgoIQ9IyE5EOJu_W2GUHH29Sn7m8obe4ejGVBc9cFt2bTHVAxISXVwRjJU3vQzBnyFJPF52ZAXx7qgmsp9bJ3Rhf_e94GO1e3FuWRkiMLuFEkJDWh2-Bf0un87Mv5OEQzX4NNagSNo8HXy42TU7xvo8X35jFxBI10MA7tN3RfvalcqhqewfajrccSCXVVWQ6GzDPeUBlyZc8Ct9CT-woDl-4ZiDIB4uebBfI--6jPu1lltIZ_A_TWYxwQECYCuV3tJxl1J4WuvaUxDZ7wu5kjLkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1SyIjBO_cr_yqwOuVxyGOCsxz0oNg0ixAiZ_7Hz4A15L7-Yj_oI6l8ZOwlyxeDxvXdDK-MB-AhasbuZmhndlXZBcuwMiRdsLAnnxq0hGDxmpLZ5WY9qKfo_XZ_eNNSPQhHUZLcqJ8qdXAMTJWTSHMBY_NNtturKgskOrlMM8wBa-72DvpcOXb8UvrYPlz4sUsX9iN9M3v3p3Nd68ge4GOX6HRfgA9en5A5iaYRcQUHBw2FImlxBQgylQ8wNEbaozW_YOKvmV4iWj6260jikC0Izt6skCCNwcGxEE5KqtYd6dwMQ4zDHZfS42rDJxKXYtiUf95ynAoaE7WQo4jSp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzMMAoIsToc4lJ__x_rjh4gJjmI4UaPN_NtOuGEByuT0siOnEPsf6At8R124AUZWArv7d5OEQF7uDG7V9CHspwPoG_kC4j3rm8npV3JgkJ_jNrQPMsNnxANsnjhaoLRGiSF0ANbTK6OgIt3PZKsIVnqJ88h_OYx0g-gx7-LVqm0-nbm_oyX92DapmS_4AY74FIC-BXpkYONDYdrhKU45R1bxZteRPMi2LBtzcbSmE6q1u2i0VGf5ss-S4j24-9o656dNV0h2RegItZPJjIaWURFVOCIwqWBLfRyKJQXqUk1nyOK6HNjz_Vj7cnXrvX7EKIUDXEoOkVGA4_hccepJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5YkXLyGPWChnhG76qfYcnsIP4ssAJO_RxUqfep5YcJHzoEQzwNwsTzt1mleaE5j0BK6FFif7M-ml-ZYGDC3g0az0jI3OoEqyx-9KTepBzbl9dN9wL7MWVrsHe4vU5Vml2Xvi7RxQoqhx-dUP-jitjaxGkhhmRFugVwb1D8ftPGShQ-AnIWfDa48Bfgq9lESp-ZMhcPB97s61_ZGHLMZkvTuAm236_PSuP5ht7b6iFvQUj8urgUCicvGyjrkF3zteDYZXp_SvdORvgD6Hjn7yqEDLk-3EU8k5SBBaJ8iDHucNdBxkK1OgVjtEuVtdY9fmeXO9z8oHmj0XmtiYu6zYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
