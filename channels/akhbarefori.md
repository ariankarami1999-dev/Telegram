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
<img src="https://cdn4.telesco.pe/file/EO0nGAgN7y0ioDz39dUd0ETLm18aF0ymHcc-WZ71t5mKinEnKubP5tVyT7PcYd8JKmO3K1r7i-GimMyqfB6KgF0fX0llHfYhQ6NZP5b6q6OVkvCRtYqtYtt8HntatS85WMWU3m20-2bZhNVe_6ltm0NRtpOSsQrM7D1lV5jAokEjNkfjLUxb5O3uzHbuZtp51KFFTBjNpZcSLQk438bWS_FVcXALVyVDHC4FaTWPu_I-DpHtQsaDXnPJv3nNVZ0WbyMbEpOHo5S72a23iZnfMCY6Dq4l1AHYmHB0T3eGBwZ9hkQrfQHFlW7CBbAN_k3XwpHj0_QbrBKrl5_52LX9OQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-673338">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تکذیب دستور تخلیه شهر چابهار
🔹
معاون استاندار و فرماندار ویژه شهرستان چابهار با رد شایعات منتشرشده در فضای مجازی، اعلام کرد تاکنون هیچ‌گونه دستور تخلیه یا هشدار رسمی برای شهروندان این شهرستان صادر نشده و شرایط در چابهار عادی است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/673338" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673337">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e2e810a90.mp4?token=E9oP-GE_t8S3_Oi-LMmYu_h-sVsRUKbmA6VU2qsMeKu81uDzziSj56MfVF3KPk_dzHnbXhFgSqk8aWn4YSlLtKpQS8kXGyyfV-fKYQc_qFVN8LvrOr8aYQx-xFGlymKM2Q38v0bN8WOevYKWdYf7vl4tmGSSCDJtRPiBFupAFYVWN0nBKETNfTYnSP-m1bwn5P5yx6FBed7rMtgmh1nw1NonLUqP0F-Yy-6DZUskgTs5fKy_Wtau9ZYaACtRNqqQIqxhpLMC7imxK_5f3FMpcYYJ5wRhvDtabkx5WvY-7vEizb55nTXMy0j0MFR5YTgl-CddpZ9_0NDOWA_t2S0cyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e2e810a90.mp4?token=E9oP-GE_t8S3_Oi-LMmYu_h-sVsRUKbmA6VU2qsMeKu81uDzziSj56MfVF3KPk_dzHnbXhFgSqk8aWn4YSlLtKpQS8kXGyyfV-fKYQc_qFVN8LvrOr8aYQx-xFGlymKM2Q38v0bN8WOevYKWdYf7vl4tmGSSCDJtRPiBFupAFYVWN0nBKETNfTYnSP-m1bwn5P5yx6FBed7rMtgmh1nw1NonLUqP0F-Yy-6DZUskgTs5fKy_Wtau9ZYaACtRNqqQIqxhpLMC7imxK_5f3FMpcYYJ5wRhvDtabkx5WvY-7vEizb55nTXMy0j0MFR5YTgl-CddpZ9_0NDOWA_t2S0cyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: حمله به تاسیسات هسته ای دارخوین رسواکننده است
سخنگوی وزارت امور خارجه:
🔹
سکوت و بی تفاوتی باعث تقویت اعتماد ما به آژانس نخواهد شد اینکه آژانس اعلام موضع نمی کند قرار نیست در اصل موضوع تفاوتی ایجاد کند
🔹
حمله به تاسیسات دارخوین نشان می دهند آمریکا با شکوفایی و پیشرفت ایران مشکل دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/673337" target="_blank">📅 11:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673336">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af10731a21.mp4?token=uEFbU6WsvMg0ElQYfMpaetuuW2LhNWUdVadv0UKB8sLZeCWMU-qcfYczdTA4nHK2_SQHPoSXaKa3sjIyuzRRhj2huPLcvWQ2NW3phODcJslG5kn9T5xQYz9h33HuCI9gwOSaAhj-AmFD4mNRP6JTip7RU7fGe3kbXjJRWKbrSkksllX5D8bX6puQhE6r7KP3i7OFBnSLpyJXFtvFMeHh8Fjkhv30Z_yLUSSMX9zgjr0VXgQswmyHeEk9Fy1CxiAIuQByg240zMbHBc0EvMZTBieqX9EiDv92plT0mNC26MQ8QkjfIdIOLlpoZY7ixVxuy6bo30ZVlAMvLzRFCo3L9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af10731a21.mp4?token=uEFbU6WsvMg0ElQYfMpaetuuW2LhNWUdVadv0UKB8sLZeCWMU-qcfYczdTA4nHK2_SQHPoSXaKa3sjIyuzRRhj2huPLcvWQ2NW3phODcJslG5kn9T5xQYz9h33HuCI9gwOSaAhj-AmFD4mNRP6JTip7RU7fGe3kbXjJRWKbrSkksllX5D8bX6puQhE6r7KP3i7OFBnSLpyJXFtvFMeHh8Fjkhv30Z_yLUSSMX9zgjr0VXgQswmyHeEk9Fy1CxiAIuQByg240zMbHBc0EvMZTBieqX9EiDv92plT0mNC26MQ8QkjfIdIOLlpoZY7ixVxuy6bo30ZVlAMvLzRFCo3L9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: سفر نخست وزیر عراق به ایران بسیار مهم است و نقطه عطفی در روابط دو کشور است
🔹
در جریان این سفر چند سند و یادداشت تفاهم به امضا خواهد رسید.
🔹
وزیر کشور امروز به پاکستان سفر خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/673336" target="_blank">📅 11:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673335">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbcwStjlCw9zxUmtQDuLqdxWDu-1HYbnQ_up99JD4d_cz6uMeSgixtogwvJUF6zHekd79J7O1jUSsASNBE1kgxZFEgh2PzOl0muXmlbNaAWLt6n92oIvU-GCaUMA62Omes0JnVOaIbBUBUBLs655ndtzNHPQdxdv9QyBat4xzxgsGz23loVqyrcCDhHdT_Oe_6ImBr4siR6ynr1mPOengwBJlJLJo4BGbIw6qBVhPTQ-jB1Ry96Lrg3hduLeAzLzJ3fvcLf15jVvDouvVBmvt4x1v-Gv5ObrQFfHxw-hu7dLn6I6xBGBvIdAKsty-vwg9TTG51-yZNw2LXL31WNCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین بروزرسانی رده‌بندی فیفا پس از جام جهانی
ایران با دو پله سقوط، در رده ۲۲ جهان ماند اما همچنان دومین تیم آسیاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/673335" target="_blank">📅 11:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673334">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جاسک
سپاه هرمزگان:
🔹
عملیات انهدام کنترل‌شده مهمات عمل‌نکرده امروز از ساعت ۱۲ تا ۱۶ در محدودهٔ بندر جاسک انجام می‌شود و به‌همین‌دلیل احتمال شنیدن صدای انفجار در این محدوده وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/673334" target="_blank">📅 11:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzKIrLNhDbvu8w5v9LNVyASGvMuCjVIE0INA5dKvSz9W3NmA9hu3otXs2X0res8grM2ejvoWvHxzWB3D9dYg-S9lFH0SxCWp3v46a3olmZ4unPc486r7jAKI8WoSKcAg3ZXpGW2O4J2IUdO32_qSjeO8vmga5GTZL-qPf-uwvGSSQhlQLtr-odc_Qu5bl3Te0GhEyRbdKUZER6TTLXyERYJUVt-yYbWvz4tgykQNfI08UqEyq6hWKdhUSHRJ0wVL4tRhR-xbRWAYm8GPhbL9oULMQld5GV32jYE1jpYLPFCJyVTp9Wib2txJdGM6pUl9qxy1D2oFDpRftLDDoos-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حالا با آمریکا چه باید کرد؛ جنگ یا توافق؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/673333" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae38190a32.mp4?token=OySxtZKXWPfz6T_VZ_MeHFyXC3rn7kdFLXbohYtR8vUqmfmGw8d189St9FuSDjaqURfBAedTCqhvGTcpkOQx07omaq33DkSEhJAaPy1c6vZAhhc5b3eKraPIm9uxVonjXDhVo_Y89_DgATR2kGm12ndEGaBB6PKD_FuOj8RGT7ywwqW1IxZ9DPCaRYnMkzxnnbWB-0UVnrZKylemizTu-ancKwNtY1fZHYYvql8rly3rzVe80Zj785LUsMeJI1wJw8a2jd0gNuxGrqyzTBRE5NDZVsiQy79SKmPwaKtEuk5fH-bynXoFnTO8NLv9I6uvpg-aXM5E-s3LE7glTPKsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae38190a32.mp4?token=OySxtZKXWPfz6T_VZ_MeHFyXC3rn7kdFLXbohYtR8vUqmfmGw8d189St9FuSDjaqURfBAedTCqhvGTcpkOQx07omaq33DkSEhJAaPy1c6vZAhhc5b3eKraPIm9uxVonjXDhVo_Y89_DgATR2kGm12ndEGaBB6PKD_FuOj8RGT7ywwqW1IxZ9DPCaRYnMkzxnnbWB-0UVnrZKylemizTu-ancKwNtY1fZHYYvql8rly3rzVe80Zj785LUsMeJI1wJw8a2jd0gNuxGrqyzTBRE5NDZVsiQy79SKmPwaKtEuk5fH-bynXoFnTO8NLv9I6uvpg-aXM5E-s3LE7glTPKsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از برج مراقبت ترافیک دریایی بندر چابهار، قبل و بعد از تجاوز دشمن آمریکایی  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/673332" target="_blank">📅 11:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609401abbf.mp4?token=vj8UrIxoxOlsNdMQiyb6LQL2pQgD69z_8lGxqgaJnpi2R6zGz6vQP9wOM4GiimVPRn528wN2QR8yLvFz4mPLBE9rJJo59PVhbw3OjGgdSGkmn4eSUc6CimLPQpn5QUcsEmMZOfZlAePnOAweZoI5Lhvn_ypqRLBHqIpCRp69rIalDpugmD5MPjDkfKVtFBk5dhPg1XXI02zvV-qKDQbSP1b920BpaAGDuFg_ix1dGIGzfixX4WHvvgLi1Ygvgx6u9BC6iasXyNWVS-b7-RTyKKc1iHkKR_gB_n_aCk0N7Ymms_k4nG-qfAxGj9wR_hxeplIpUkmd8rLigMUOzl1kcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609401abbf.mp4?token=vj8UrIxoxOlsNdMQiyb6LQL2pQgD69z_8lGxqgaJnpi2R6zGz6vQP9wOM4GiimVPRn528wN2QR8yLvFz4mPLBE9rJJo59PVhbw3OjGgdSGkmn4eSUc6CimLPQpn5QUcsEmMZOfZlAePnOAweZoI5Lhvn_ypqRLBHqIpCRp69rIalDpugmD5MPjDkfKVtFBk5dhPg1XXI02zvV-qKDQbSP1b920BpaAGDuFg_ix1dGIGzfixX4WHvvgLi1Ygvgx6u9BC6iasXyNWVS-b7-RTyKKc1iHkKR_gB_n_aCk0N7Ymms_k4nG-qfAxGj9wR_hxeplIpUkmd8rLigMUOzl1kcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امور خارجه به ادعای ترامپ مبنی بر آزادی یک شهروند آمریکایی از زندان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/673331" target="_blank">📅 11:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بقایی: مذاکره و دیپلماسی دو بال برای تامین منافع ایران است   سخنگوی وزارت امور خارجه:
🔹
دیپلمات‌های ما از ترس فریب وظیفه ذاتی خود را ترک نخواهند کرد؛ همانطور که نیروهای مسلح ما به واسطه تکنولوژی برتر دشمن وظیفه دفاع از کشور را فراموش نخواهند کرد
🔹
ایران…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/673330" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc10b46a1.mp4?token=bvyjwm0E_djqgfe5MxrW3gmeoZDi0qWe8O3_vAyi75YdMsROQGmSRA-hqLd3TyrnltyU1tldZYCXmijwM1n596I_TdfIkdfv5K2MP0629O90qqpx8gyyS9626Wq4fHjSxeUYiCLmWkalouu57tc-Lm3s0C1iRM2YuSjG1nGZwOuitAhXfVDvD6riyFS_zABqHxQ2PEzsKWBAH07uyhNBByBTcip-5k8bNOa1eR46SJ2saHfeCn3YPQT_NhMRffyw7MXRUsunizUPm6p3sHFAxXbqXKizzytgoxEvrrmd18ml56BXLy8LfQ5wDrYViGzBymikn2NtVPXmwbXgiIg_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc10b46a1.mp4?token=bvyjwm0E_djqgfe5MxrW3gmeoZDi0qWe8O3_vAyi75YdMsROQGmSRA-hqLd3TyrnltyU1tldZYCXmijwM1n596I_TdfIkdfv5K2MP0629O90qqpx8gyyS9626Wq4fHjSxeUYiCLmWkalouu57tc-Lm3s0C1iRM2YuSjG1nGZwOuitAhXfVDvD6riyFS_zABqHxQ2PEzsKWBAH07uyhNBByBTcip-5k8bNOa1eR46SJ2saHfeCn3YPQT_NhMRffyw7MXRUsunizUPm6p3sHFAxXbqXKizzytgoxEvrrmd18ml56BXLy8LfQ5wDrYViGzBymikn2NtVPXmwbXgiIg_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش پربازدید کاربران فضای مجازی به بازی‌های آرژانتین در جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/673329" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cdf03eb42.mp4?token=FwHxPWDXqcuQCkQ_RYcbPA554zS9KUYdu4B3MJNG8b5Ce0LvLs1buoQ7jyIL0nJVYXyiOyfYE4MVWB34tWRI-5q2i7hmGdZDmmLZt7aErafTG-rsuURleXeIZwVoy7vB8hRQYtas8obRdadksfsG4iOHjggRdlzyErtYVC9F8MRRrWFXY9LCoz5ueWgE1YequOHZmnRNNu_sSYzjIX-NJBu1zJjhCA3m1-Q1OttXMLJUgKUmDZtamWoI3PU5R1pgPys7J_Cm1cLz1iQklbdT-xpST-E_p_9o1MhXmmnbL7xTVBs8DwgzpbDSTCAglLaPVk7QtGeOohCeWAHO_GvvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cdf03eb42.mp4?token=FwHxPWDXqcuQCkQ_RYcbPA554zS9KUYdu4B3MJNG8b5Ce0LvLs1buoQ7jyIL0nJVYXyiOyfYE4MVWB34tWRI-5q2i7hmGdZDmmLZt7aErafTG-rsuURleXeIZwVoy7vB8hRQYtas8obRdadksfsG4iOHjggRdlzyErtYVC9F8MRRrWFXY9LCoz5ueWgE1YequOHZmnRNNu_sSYzjIX-NJBu1zJjhCA3m1-Q1OttXMLJUgKUmDZtamWoI3PU5R1pgPys7J_Cm1cLz1iQklbdT-xpST-E_p_9o1MhXmmnbL7xTVBs8DwgzpbDSTCAglLaPVk7QtGeOohCeWAHO_GvvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: مذاکره و دیپلماسی دو بال برای تامین منافع ایران است
سخنگوی وزارت امور خارجه:
🔹
دیپلمات‌های ما از ترس فریب وظیفه ذاتی خود را ترک نخواهند کرد؛ همانطور که نیروهای مسلح ما به واسطه تکنولوژی برتر دشمن وظیفه دفاع از کشور را فراموش نخواهند کرد
🔹
ایران عزم خود را برای پاسخ قاطع به تهدید زیرساخت‌ها اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/673328" target="_blank">📅 11:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تخم‌مرغ گران‌تر شد، کوچک‌تر هم شد!
🔹
قیمت هر شانه تخم‌مرغ در تهران به حدود ۴۸۰ هزار تومان رسیده؛ یعنی ۸۰ هزار تومان افزایش در دو هفته، خریداران می‌گویند با وجود قیمت‌گذاری شانه‌ها بر اساس وزن ۲ کیلو، تخم‌مرغ‌ها ریزتر و سبک‌تر شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/673327" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b84bbe73.mp4?token=XHzbMwCGfxVPAu5nxJbULuA_y22e2SKK4AzCB2TzPBe5CDbzmz2rBLEvTPcG9oyFeDcfvvtOUGm5dgBqn0DBcb5fi5Qokd_BT1tp0Ih7RjmWHPwZeTRNciT7rL08pMkCiIhKB33HePoJezotAZJCCqVwGLLJjDbpSCfnRQJ-W_D624829V7-u-l3RF1UR8B0RjLYhX5BqGNKfuOkypQwGk6Mc-KQiNTQc79xLaH39fXtdPlaj3EtpKZZdyyCPSwInyfVJnFlNdiVaTmubB76JK54B9ssutmA6HNBtQhSWmX3bW9x-pXXM9fRzuYkwDzVENDIGY9W63wNOvHqxyLEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b84bbe73.mp4?token=XHzbMwCGfxVPAu5nxJbULuA_y22e2SKK4AzCB2TzPBe5CDbzmz2rBLEvTPcG9oyFeDcfvvtOUGm5dgBqn0DBcb5fi5Qokd_BT1tp0Ih7RjmWHPwZeTRNciT7rL08pMkCiIhKB33HePoJezotAZJCCqVwGLLJjDbpSCfnRQJ-W_D624829V7-u-l3RF1UR8B0RjLYhX5BqGNKfuOkypQwGk6Mc-KQiNTQc79xLaH39fXtdPlaj3EtpKZZdyyCPSwInyfVJnFlNdiVaTmubB76JK54B9ssutmA6HNBtQhSWmX3bW9x-pXXM9fRzuYkwDzVENDIGY9W63wNOvHqxyLEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله: هواپیما با موفقیت فرود آمد و محاصره شکسته شد
🔹
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/673326" target="_blank">📅 11:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Rta_BiZc2HGlg-r5YHFNvhNy5vv6h1QOWrTIcr188VxAQ0u6Af0oclByf0dGm5o5JmLVLOlEVMILMFs3Ps7bnTF-Ufdn1MQHAXCMM0WbngSWwVWIOsHOyx6NQNQie3Rw2hGi7H2MCR4DBoxDRgwkJv_nX1XdhAo8fZqbbJnSPjZdHcOUO1K6Fn4OfDaYLUIBJn6TywdzhcwLotGoZSrDARzMQanG4t13RZeFd5J4KCpyO-ywXnF1SggaGBrdPdiiSqqB5PenN8QOBU8hvPily-675U-QRZKbwwtIRIRCGVbvCM00e13JB2p1E7RKOVYG6_UINhMZjxoTbFfd8D6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597a7bb75c.mp4?token=Rta_BiZc2HGlg-r5YHFNvhNy5vv6h1QOWrTIcr188VxAQ0u6Af0oclByf0dGm5o5JmLVLOlEVMILMFs3Ps7bnTF-Ufdn1MQHAXCMM0WbngSWwVWIOsHOyx6NQNQie3Rw2hGi7H2MCR4DBoxDRgwkJv_nX1XdhAo8fZqbbJnSPjZdHcOUO1K6Fn4OfDaYLUIBJn6TywdzhcwLotGoZSrDARzMQanG4t13RZeFd5J4KCpyO-ywXnF1SggaGBrdPdiiSqqB5PenN8QOBU8hvPily-675U-QRZKbwwtIRIRCGVbvCM00e13JB2p1E7RKOVYG6_UINhMZjxoTbFfd8D6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مقامات آمریکایی این‌قدر در معرض گزارش‌های ساختگی هستند که هر خبری دوست ندارند را هوش مصنوعی می‌دانند
🔹
وقتی آمریکا حرف از دیپلماسی می‌زند معنیش تهدید و تحریک و تحمیل خواسته‌هایشان است.
🔹
ما هیچ وقت پیشگام در نقض عهد نبودیم.صورت مسئله روشن است یک تفاهم مادامی ارزش دارد که طرف های آن به اجرای آن متعهد باشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/673325" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b519d16da.mp4?token=VP109NDXvKUAFRJny2sMowwcvM01yH4hE4Tdf9uPwvip7D08FqMdpGnjmSUf7VuF28I5cBnhM4-gRThMTuXgAKsc7o9CDqy6U1hQ73FA0ic8GwAkzYTdOJS017vzeUX2_5kav0Sbc5rjywEeAocN3EJouoJvd2qFZ4ly2A_b49aG8OJwS5UkmhGcrZZ0Slv2D9dwLjlJd86GeUbgd5QFKkMuw3eR8uOLe9E7ywMaWxbrCW4yHsuoMehDcDmIn-Q-Atl7tcqsSjFuxdA4P2_JPTpTsWxl32AJPY5EqHjWMskBTvG0bKoD6YSJO0ursEI3c6KdTb-7hvYNA7gJlY-Wjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b519d16da.mp4?token=VP109NDXvKUAFRJny2sMowwcvM01yH4hE4Tdf9uPwvip7D08FqMdpGnjmSUf7VuF28I5cBnhM4-gRThMTuXgAKsc7o9CDqy6U1hQ73FA0ic8GwAkzYTdOJS017vzeUX2_5kav0Sbc5rjywEeAocN3EJouoJvd2qFZ4ly2A_b49aG8OJwS5UkmhGcrZZ0Slv2D9dwLjlJd86GeUbgd5QFKkMuw3eR8uOLe9E7ywMaWxbrCW4yHsuoMehDcDmIn-Q-Atl7tcqsSjFuxdA4P2_JPTpTsWxl32AJPY5EqHjWMskBTvG0bKoD6YSJO0ursEI3c6KdTb-7hvYNA7gJlY-Wjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: ایده‌های از طرف میانجی‌ها ارائه شده است
🔹
پیشنهادهایی مطرح شده از سوی میانجی‌ها و دریافت کرده‌ایم، اما درباره جزئیات بگذارید ورود نکنم. اینکه ایده‌هایی واصل شده بله تایید است.
🔹
بند ۵ یادداشت تفاهم حق مدیریت ایران بر تنگه هرمز را…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/673324" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZR7aeNFpmHjti6qewXsVBgF5X9Wsd_uoTFMcLuDBlmorowUcEq6IbW1vwivfBop4YhHYIDHh3T8m5I94qAt-J2ArBHTjhmMzbYLxHhvs2NvY9PikM2VkScJExge3SFvtyMBtHIbrp2PmgLJZp3AB5vB7PdsvU4tBJwcDE7C7CdP2gCbo83LbWYxWx84DbQ0z4g27lS22hHiDCYTK8rb87H7WYTt5b6U1Zn7egmQY2Ju_S_dcfFMI8lPKUNDfECqZX1lYZaB9_UcV1tz79i8Pr-fogC12nY_NCBL2wwz258DB4D-BYsPh8ZGusBUmS0wHRNIRrNg76bE-1iKrWLVLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNnDHEjbw7dXns6WcpEleIjWSU-_zNeVV6u_YSSZLWJAs38sMEydXvNdjcNNyReOwmduYperazPE3dN7A_OHMCUXWdG2AI0J4mSy8px12mL9MWgypsxgQbwdiraOXeQwwQAAkqA7VjT3G6EneiLr-i-w7qpbnsYflHeSGX336rO1H96nTYqdjcOo2GythmVMs561fyo_XelnJ0R5Nz-PAmuUYfCEX6SVXMyCpbDJ75R0ZPX4pXwpA9S9oKYvZOGrxXU2LLWVOOmrOlT5HRfw3NvflWRF_Nqn3S_4BT0sUGWUOf6kEvaR2yEBOguIOM_vrxeCr4wt7wAGHcOm_Z9dCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7cd88cb1.mp4?token=n1roViAn3Iiuw-13IqrFHBN1LJ5Uoi0X43MVveX7dPchBiILusKuoNavArqjDma44Gj9HfVnG8lgb_sWAPB01LzSjHDMEcOnKO28gpRGvX55eNBlZ9A_ZWlJB2uG-7fkiSbnl-Skhhurnh3C_L_8npZnpAh5CztinvE15za6zCzohjaEQ7e_2FvCOPcxKXyv00my7SaauXnF1MNHZjClGWFB9HjCHbtvmqC1Xe-bxS6i1kognEuvYBLFA8N2_CC3GWyIswHIfrYDwYU1tJNHSkaPPmH1HKLHYfdOc1OMrkVHwlu6YrIjNiABLB2lSG6Kw8c8Zrpd4_z8S1YG4nMEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7cd88cb1.mp4?token=n1roViAn3Iiuw-13IqrFHBN1LJ5Uoi0X43MVveX7dPchBiILusKuoNavArqjDma44Gj9HfVnG8lgb_sWAPB01LzSjHDMEcOnKO28gpRGvX55eNBlZ9A_ZWlJB2uG-7fkiSbnl-Skhhurnh3C_L_8npZnpAh5CztinvE15za6zCzohjaEQ7e_2FvCOPcxKXyv00my7SaauXnF1MNHZjClGWFB9HjCHbtvmqC1Xe-bxS6i1kognEuvYBLFA8N2_CC3GWyIswHIfrYDwYU1tJNHSkaPPmH1HKLHYfdOc1OMrkVHwlu6YrIjNiABLB2lSG6Kw8c8Zrpd4_z8S1YG4nMEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اعضای تیم ملی اسپانیا مدال طلای جام جهانی را دریافت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/673321" target="_blank">📅 11:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceed8baef.mp4?token=qVMCjeUODVUmP5_6OWmWNd2ERTD4pK_1ANnESc8y2di5QboRxmO4fmqc-9pRhS_FArPyzeXQMx63-jLTu3v_aUW-5yuxuRhiW6rx6qKPuuy5jjBI5e2fFZnm1iKQlKzUmQaKLOlSpORrcOssB2JL80DV8MisW08n230WSVKGXqayW8TgyhY706ThWx5GxZyKaFuA6WvBhN1k-LVTBo_OLiv2m5sd12B6JMQ-68KsJRfwc2DcVlNZK6ZpBTJlG8z3mXc2JwIfFOruJABQPtnw9Q4cTnfhoniXXfE4_yvm5pRVnD7_JHjypwdWNmEav8tDtgBsyZFxiapCx6kYpvyOEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceed8baef.mp4?token=qVMCjeUODVUmP5_6OWmWNd2ERTD4pK_1ANnESc8y2di5QboRxmO4fmqc-9pRhS_FArPyzeXQMx63-jLTu3v_aUW-5yuxuRhiW6rx6qKPuuy5jjBI5e2fFZnm1iKQlKzUmQaKLOlSpORrcOssB2JL80DV8MisW08n230WSVKGXqayW8TgyhY706ThWx5GxZyKaFuA6WvBhN1k-LVTBo_OLiv2m5sd12B6JMQ-68KsJRfwc2DcVlNZK6ZpBTJlG8z3mXc2JwIfFOruJABQPtnw9Q4cTnfhoniXXfE4_yvm5pRVnD7_JHjypwdWNmEav8tDtgBsyZFxiapCx6kYpvyOEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: ایده‌های از طرف میانجی‌ها ارائه شده است
🔹
پیشنهادهایی مطرح شده از سوی میانجی‌ها و دریافت کرده‌ایم، اما درباره جزئیات بگذارید ورود نکنم. اینکه ایده‌هایی واصل شده بله تایید است.
🔹
بند ۵ یادداشت تفاهم حق مدیریت ایران بر تنگه هرمز را تثبیت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/673320" target="_blank">📅 11:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=Q7SbP3L-IPKQApMHAbieDj1I54fUlKeD1Qg7GymoyL4o3jlKdxtdcnlDLS91BW3EAUL1Pp00rxdKtpcFwHQ39efZ4l1qsFe9aMzn0CTgiKNz08-YMbW0xHoIQ_XlbiMA6w1_YCWwOTWcrt1QnOkn6ZWQe8JI2FV-1C_HJsOeCC2aUsSnpZmt2ItIwA9vcDs18yoZ7Rp7apfIgO6uhPwlsbo2olIlIfgXYbdQjwzOg6LJlyshUzg9n1U8heOENfV_BJdYFHNzeOXwAq337G3EqBlIbjm_-SSB3-nS-jxk-1Ibf0789_09jCLRI6vQj8ttYOfmVHoniumVVYiUjaM4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=Q7SbP3L-IPKQApMHAbieDj1I54fUlKeD1Qg7GymoyL4o3jlKdxtdcnlDLS91BW3EAUL1Pp00rxdKtpcFwHQ39efZ4l1qsFe9aMzn0CTgiKNz08-YMbW0xHoIQ_XlbiMA6w1_YCWwOTWcrt1QnOkn6ZWQe8JI2FV-1C_HJsOeCC2aUsSnpZmt2ItIwA9vcDs18yoZ7Rp7apfIgO6uhPwlsbo2olIlIfgXYbdQjwzOg6LJlyshUzg9n1U8heOENfV_BJdYFHNzeOXwAq337G3EqBlIbjm_-SSB3-nS-jxk-1Ibf0789_09jCLRI6vQj8ttYOfmVHoniumVVYiUjaM4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: هیچ بهانه ای برای پیمان شکنی آمریکا وجود دارد/ دشمن فریبکار، خدعه‌گر و وحشی است، اما این دلیل برای عقب‌نشینی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/673319" target="_blank">📅 10:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقائی: قهرمانی اسپانیا در سیاسی‌ترین جام جهانی تاریخ رقم خورد/ رویکرد ضدتجاوز اسپانیا محبوبیت جهانی این تیم را رقم زد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/673318" target="_blank">📅 10:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51adb6372.mp4?token=obvyEUPlEkCrcboqZUA1HNcYcZpqJyXVA_riVTNZj5AEf9o0d9WVfFlzYeKu2B454pT4-rpxU6a6BxHMHvBuA1gPAVxGCUa_FPEm6KktRl5JQdGdv61Acy9GkCUPiSw96yuO_xvofW81CSOqOFh-HAxW8xj6SKl6HQzNimf_wQTmiij1T1edZpKx_DAUBt16EgOJDIRx7Pm-_cSr2nggnTIXpncssszrH6nQcKtOQ5WKdsc9MoCUNRPzNgiOAF5rj-C63CoIg_Sn02BhACVXGdzwbKFBn31MY6fdQ_dYWEAosbpylTs3Ss7W34-AIILGAXJIG7Iex2YPc6L2nRa4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51adb6372.mp4?token=obvyEUPlEkCrcboqZUA1HNcYcZpqJyXVA_riVTNZj5AEf9o0d9WVfFlzYeKu2B454pT4-rpxU6a6BxHMHvBuA1gPAVxGCUa_FPEm6KktRl5JQdGdv61Acy9GkCUPiSw96yuO_xvofW81CSOqOFh-HAxW8xj6SKl6HQzNimf_wQTmiij1T1edZpKx_DAUBt16EgOJDIRx7Pm-_cSr2nggnTIXpncssszrH6nQcKtOQ5WKdsc9MoCUNRPzNgiOAF5rj-C63CoIg_Sn02BhACVXGdzwbKFBn31MY6fdQ_dYWEAosbpylTs3Ss7W34-AIILGAXJIG7Iex2YPc6L2nRa4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام تأسیسات آمریکا در پایگاه ملک فیصل اردن
🔹
تصاویر ماهواره‌ای انهدام بخش‌هایی از تأسیسات نیروهای آمریکا را در پایگاه هوایی ملک فیصل در اردن نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/673317" target="_blank">📅 10:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673316">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای الحدث: وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673316" target="_blank">📅 10:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268c33ffdb.mp4?token=aGR5Rt-7WIcY0Gz1LfBrryJocQ5KtJrMYlaLrbESRYTyg-YH2s8VcvuFVRQArCz_x-rcUO8olFeGvzdVCqR8rcVAZuLVEF5IUC-AdTIYtM8CTlnr0Xzwm4vpdLy9E5Qhxao0dCCPNImY9WxkyJQJhs1_cQXyfzyZOlXC8DXE4gsF7vl9495Qg7eLxhsUjcnkf06_NkFcfmQO-DFdNgZ_3FPBsrvmJMVYk9_F7cl4iQQBYvEn_Xx4haZYadxRxPe4kT_EOucD8SqB8rCkm0GjyMgUbp1Pxjfk2c48R2JxNpGbjJHpsNvbGMhwmIh0lyEyo5gMV_iE6Pybh3481fwZZ11AZbEgp9HQWOIAkGSM0LJcmtNBAA-aFnQ7pW5yO5tnEgZUH0Dep4CeXUvkc67qFHn3CyL-VhL2rKmszM318yABCzM4uHgA0gIE72ybAd7fRbQgzMHzcHc2y8376WT2OlowomkCUb2mw-8TJxtU-17VcAZpQw0eMR3K-STZE-BO3Y4O9-dTvaPedIiYk0eCQ8xPGbt9T-WjPMWjK08wrh9CeM1ZshtkmdSDXWxqTm4wG8-0XB6jnkrq6pRxKCNW2w2YTevi-6oyksv65Omqn6aFz04qtdxXDJOA9HrIBclPmyx0LA1VnW7JOSDU1UwVx-WMhJV5DNyq7N3pKLsMjB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268c33ffdb.mp4?token=aGR5Rt-7WIcY0Gz1LfBrryJocQ5KtJrMYlaLrbESRYTyg-YH2s8VcvuFVRQArCz_x-rcUO8olFeGvzdVCqR8rcVAZuLVEF5IUC-AdTIYtM8CTlnr0Xzwm4vpdLy9E5Qhxao0dCCPNImY9WxkyJQJhs1_cQXyfzyZOlXC8DXE4gsF7vl9495Qg7eLxhsUjcnkf06_NkFcfmQO-DFdNgZ_3FPBsrvmJMVYk9_F7cl4iQQBYvEn_Xx4haZYadxRxPe4kT_EOucD8SqB8rCkm0GjyMgUbp1Pxjfk2c48R2JxNpGbjJHpsNvbGMhwmIh0lyEyo5gMV_iE6Pybh3481fwZZ11AZbEgp9HQWOIAkGSM0LJcmtNBAA-aFnQ7pW5yO5tnEgZUH0Dep4CeXUvkc67qFHn3CyL-VhL2rKmszM318yABCzM4uHgA0gIE72ybAd7fRbQgzMHzcHc2y8376WT2OlowomkCUb2mw-8TJxtU-17VcAZpQw0eMR3K-STZE-BO3Y4O9-dTvaPedIiYk0eCQ8xPGbt9T-WjPMWjK08wrh9CeM1ZshtkmdSDXWxqTm4wG8-0XB6jnkrq6pRxKCNW2w2YTevi-6oyksv65Omqn6aFz04qtdxXDJOA9HrIBclPmyx0LA1VnW7JOSDU1UwVx-WMhJV5DNyq7N3pKLsMjB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: قهرمانی اسپانیا در سیاسی‌ترین جام جهانی تاریخ رقم خورد/ رویکرد ضدتجاوز اسپانیا محبوبیت جهانی این تیم را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/673315" target="_blank">📅 10:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqyAD4zjxdo_DUKprl-834lNuDsvwLTaF-5crFOI85UJbYJiBlj-s7LtpqgMBnUfLlp2FW4Dumw2pgzBpgoG4E3OpDI2clRxY08xdDGsHCH4CFMaTvVJrFYnKd7-7jcIXNrdv5VsmAxCFdlFGAbodyacltzxqYay919mIKKQV3kOFo8eHZ08qlXg5PLcd5wturo-dPXJ-Gg2ReZdbDTSjHqN7tgdebWhZcI_AgHrK8BVQNhAKuxYolimR4Dmz2l8zcC02q4xPotw_JC_GvrqWqx06LXdHPcW1CyPOOD3HqrFqActkbdklHV26BXpNThqjW3OXiwmPoy0REGyiELI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر روی جلد the week درباره بن بست آمریکا مقابل ایران
🔹
نشریه the week یک تصویر خاص را برای روی جلد خود انتخاب کرد که نشان می دهد سیاستمداران آمریکایی هیچ راهی برای پایان دادن به جنگ با ایران ندارند و در این جنگ گرفتار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/673314" target="_blank">📅 10:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673313">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693f1cb965.mp4?token=JN_HSsCYbdIdRlcBbyx3FJvPSmiq9y1c8qRQJwIkBPaT7MRXknZuT53CpV2JnZI96VCoXGjFrYtVJ3889d6_mvOUiJ6M1rQjyHXvdaz-TN3jYOPIX9RWY7MrLWs_E0TKRZ-8KNLV2xL_Kj77Km7hBbnKF7GA_G75kaziTkZdxNRtWg19exdKhq1puD-RI52wZaDELOXduzhayCwvNxTMQyBHzYsvYDgrfu-B-vp9oNHgEYvZ8WkA0dpslzD1L4EkgNl_y7wGjRbOoa97w4VkAYhdrogqwcsAKvRcw9cwUwFaX_3VQfNQEVIDbsPg1ZN59PWO90P2pcO69KxjeQKUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693f1cb965.mp4?token=JN_HSsCYbdIdRlcBbyx3FJvPSmiq9y1c8qRQJwIkBPaT7MRXknZuT53CpV2JnZI96VCoXGjFrYtVJ3889d6_mvOUiJ6M1rQjyHXvdaz-TN3jYOPIX9RWY7MrLWs_E0TKRZ-8KNLV2xL_Kj77Km7hBbnKF7GA_G75kaziTkZdxNRtWg19exdKhq1puD-RI52wZaDELOXduzhayCwvNxTMQyBHzYsvYDgrfu-B-vp9oNHgEYvZ8WkA0dpslzD1L4EkgNl_y7wGjRbOoa97w4VkAYhdrogqwcsAKvRcw9cwUwFaX_3VQfNQEVIDbsPg1ZN59PWO90P2pcO69KxjeQKUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: سواحل مکران و خلیج‌فارس قلب ناگسستنی ایران هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/673313" target="_blank">📅 10:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
اعلام آمادگی پوتین برای تماس با رهبر معظم انقلاب
سخنگوی ریاست جمهوری روسیه:
🔹
در حال حاضر هیچ ترتیب خاصی برای تماس تلفنی بین ولادیمیر پوتین رئیس‌جمهور روسیه و آیت‌الله سید مجتبی خامنه‌ای رهبر جدید ایران، وجود ندارد؛ اما پوتین آماده چنین تماس‌هایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/673312" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673311">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267327f2c2.mp4?token=QuaQXGciJvktgXQ3zPcHxvQKTKNRKMqnecmR6jHITwmlHUxVNCx1X5bKrDJFRufJaPt3stb5idnRSnwDgHSiezjRlQttNCgjlbfJzfaCuqQWVOmNPZV13MTGDhTJYnQX4GjRl5ViONtiJVbvbrSgNG-Er2ff5sNSf8nIz0BNee7352TVomn5NFWvRZ4IcBrWCDJGiiJAToU7fjYESfZRO3IAzcGisQI5PXxohM9NA9wlrIva634HJDnbxYpiJ2nOusB2lsxGoYfUwXY0XikJv8yOdoEWC4yOrdK8i86Bt3NNXd8JIhTPy-k0d8aZBrAkmRJIES0q4AwEa1tPClwkAVpV7sM7suIgU2QAZMnW7JcmOjgYXp-jus5qFW8rpTEWrTyL6k5GK9txi0n6j9QdcPJUehfskE0CEfqBUdTRT-G8d9rO2zGOugSW1dgLkTmtUvAk_sHLHaoatiSw0tMTaamJbwLMgsCptsjaAY-q9wgk-w1ux-6-hIkdYzjdEuVLy2NZvJoE5t9U2kD5GB87Yxe4pXk1RI_fxFZqyGnBEJVNSrNP8g1E1j4OKGLc0LzLPOaOEP8cwGD4uK8Ce6x1XlF8M_dSklQogk_eJE8nTWUXIVmpW5UdVvPOy4j6Uzx_s2bY5GrLqPBsbBY36etl2t_y-gP2O466YfRNMQe2nlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267327f2c2.mp4?token=QuaQXGciJvktgXQ3zPcHxvQKTKNRKMqnecmR6jHITwmlHUxVNCx1X5bKrDJFRufJaPt3stb5idnRSnwDgHSiezjRlQttNCgjlbfJzfaCuqQWVOmNPZV13MTGDhTJYnQX4GjRl5ViONtiJVbvbrSgNG-Er2ff5sNSf8nIz0BNee7352TVomn5NFWvRZ4IcBrWCDJGiiJAToU7fjYESfZRO3IAzcGisQI5PXxohM9NA9wlrIva634HJDnbxYpiJ2nOusB2lsxGoYfUwXY0XikJv8yOdoEWC4yOrdK8i86Bt3NNXd8JIhTPy-k0d8aZBrAkmRJIES0q4AwEa1tPClwkAVpV7sM7suIgU2QAZMnW7JcmOjgYXp-jus5qFW8rpTEWrTyL6k5GK9txi0n6j9QdcPJUehfskE0CEfqBUdTRT-G8d9rO2zGOugSW1dgLkTmtUvAk_sHLHaoatiSw0tMTaamJbwLMgsCptsjaAY-q9wgk-w1ux-6-hIkdYzjdEuVLy2NZvJoE5t9U2kD5GB87Yxe4pXk1RI_fxFZqyGnBEJVNSrNP8g1E1j4OKGLc0LzLPOaOEP8cwGD4uK8Ce6x1XlF8M_dSklQogk_eJE8nTWUXIVmpW5UdVvPOy4j6Uzx_s2bY5GrLqPBsbBY36etl2t_y-gP2O466YfRNMQe2nlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کیک خیس فوق‌العاده خوشمزه، اونم بدون فر ‌همزن و فقط در ۲دقیقه
😍
مواد لازم:
🔹
۲ عدد موز
🔹
۲ عدد تخم‌مرغ
🔹
۲ قاشق غذاخوری شکلات صبحانه
🔹
۲ قاشق غذاخوری پودر کاکائو
🔹
۱ و نیم لیوان آرد
🔹
۲ قاشق چایخوری بکینگ پودر
🔹
۱ قاشق چایخوری وانیل
🔹
نصف لیوان شیر
🔹
…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/673311" target="_blank">📅 10:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsAh_hYnSQ32OFL8EX-r0zjd3V7QFy7ej5zHOh369fkLmapg6glBd7WHfbNysIRLbe34FBpEcPdQD5SvdgURlNlZVCZ07f8E9QXM6CcMwIZ9lQk3GgKBxpCrvymDU6-o7OVJpDsTBMJeN5IUOasFMAeMgNWKMUKH-UJIawmI7JQMAT0HoSIu2x5OB0BDqlo1uVvNVSCqi94MxBVxWscpBnUTP1ZFzwPn9ShsqHEM-tp_TuDdLCda7lWNZ_xQDixk_nhGguDyJ4HMjIRlPLJfWwrHkbiSqms317lwbM5ykXC_uo1nLqTPW14bNYTBDi1SgKKm6qSJCv8eDKu0hZMZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای بیژن مرتضوی، موسیقی‌دان مازندرانی بین دو نیمه فینال #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673310" target="_blank">📅 10:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e669f7f60c.mp4?token=PrOuodmD_Z8x3zg4Fo3Ungx5BqFDSWj9nvEdNNv0GWmQiGDHx_wM_XeYWRr_t3v6Di0Dw73oy3QfR3Vvwq3mcV4f9pi2LTtmYOWDcFFHf710I1j8vopbpscOk0G51wBaXV-L4kbUhNJ0KsJHRBWJ9BjH6m1Zj3y3MRRdzbYeKUDDiwOfxXw8cSkQQHdQ4LI0lnessWmtc4ow0Y2BM1PDplYKG6VPZKYQUwzwmdaQKM9zzI4UML1nJlhQvCAVW6i6dNPcFgkSuKWMpvbpaUEpTlUw892FZLIXVXXzNw_5USWUStimCx0oY63KrvyjBWrMpLqXI5ldc-J4-Y6Yr7ypAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e669f7f60c.mp4?token=PrOuodmD_Z8x3zg4Fo3Ungx5BqFDSWj9nvEdNNv0GWmQiGDHx_wM_XeYWRr_t3v6Di0Dw73oy3QfR3Vvwq3mcV4f9pi2LTtmYOWDcFFHf710I1j8vopbpscOk0G51wBaXV-L4kbUhNJ0KsJHRBWJ9BjH6m1Zj3y3MRRdzbYeKUDDiwOfxXw8cSkQQHdQ4LI0lnessWmtc4ow0Y2BM1PDplYKG6VPZKYQUwzwmdaQKM9zzI4UML1nJlhQvCAVW6i6dNPcFgkSuKWMpvbpaUEpTlUw892FZLIXVXXzNw_5USWUStimCx0oY63KrvyjBWrMpLqXI5ldc-J4-Y6Yr7ypAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظ اسطوره‌های بچگیمون؛
خداحافظ نسلی که به مستطیل سبز معنا می‌بخشیدید
آخرین رقص همه‌شون در جام جهانی با اشک‌ گره خورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/673309" target="_blank">📅 10:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در شمال غربی دریای عمان
🔹
یک کشتی در فاصله ۸ مایلی شمال‌غربی «خصب» در عمان هدف پرتابه‌ای ناشناس قرار گرفته و خدمه با ایمنی کامل کشتی را ترک کردند.
🔹
آتش‌سوزی در کشتی هدف‌گرفته شده خاموش نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/673308" target="_blank">📅 10:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdgiIos3v4AbkRlTM4hJ-HEvXIETS8_yrHJdzPolZkp6gGJd5sq9YAaeXg67KXjo-umAXzpz0ilHrJNL74iVJLc_r8Vssg9Dlj9qssN4gOcTY1QZRognbS95sBdb_V5meS8e1g42O6BzA_7F_5KfYzTg3FqON31hlE-xSuQYcwlkpbgyPQ1IOgefsd8lEfd1IIwuMwyKzkQ8kc1oSOU8zeUUY-OTdYo54r3Nf8VIWy6CgTRexOr0Xh2OJYzP-HK0TeTLjPBc7p8CGlpUG4ZX2PMlKHWVnzUsc1uPCLOMbX5Efzf7qn6lNEKbVe6Y-7C1pSOlLd09Cry6KL7h_Pi_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ایران به قهرمانی اسپانیا در جام جهانی ۲۰۲۶
سفارت ایران در مادرید:
🔹
به نام ملت ایران، صمیمانه قهرمانی درخشان اسپانیا در جام جهانی را تبریک می‌گوییم.
🔹
این قهرمانی کاملاً شایسته بود؛ دستاوردی که حاصل استعداد، تلاش، فداکاری و روحیه کار تیمی است.
🔹
این پیروزی تاریخی را به همه مردم اسپانیا صمیمانه تبریک می‌گوییم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/673307" target="_blank">📅 10:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند  روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/673306" target="_blank">📅 10:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQRendKore7_R94y_x_d9OmFo1VGtzWYBQhrZMzRKP9X1dDazmyXpX6A15WbnLeDutcFiP0SBZsC9qyRqjaDMGRVMNJ3-LhpimMAc4dYFapxsx9_VOXQWRgF3bWFYyF2fko3MXyD97obmk2zF4FHdcOd_ipb-BxwuJdJO_9-cLYzmOEEfo3jeFezZSHOqhNhv7U4SvwLS4-ZdbxHE50h94iEsPfnCoddTBlWUcF5ztzI9qM0-g1bdq2B8KwcdxnPNKQIzclZfDTPe-w0mjWXdr8lUsill-nW3McKeatpckGDzVsnNWMhUXJfLBBntt7BvdLI_zvZNZrjfuhuurjeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام فهرست داروهای ممنوعه عراق پیش از اربعین
؛
۱۴ دارویی که ممکن است در مرز عراق برایتان مشکل‌ساز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/673305" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04c55b88b.mp4?token=kykL9qsT7uNYhUyBkbru_fIsFwsw5Skgdzt-8ou3u7Zems8kqAJxR5NxFuzMYaK1vDGKjzHwDwwfNvaPBZwJcxQ_jlzOUZg8whz4l4H6w7c4Pqlo3egIvJT7hHOy8ZjjS_SO6tdJUm7HgKdP9F9bjpGMByyANmF_kHJZsR9iK2EYjnCc8jWkWMmq9dJ5i1ApZ2IdVgQF1H2L7utOcoT4qX02hCb9c_91LtC1FocBDBo7ELRzKz8C0nsKN_KvxKZfpwNiNdfTuMHTMtU1FX3x8YzUHrNTcRLaI7PUvo7qpW9tYgc3IAOpUNSnK742ZGkTNbje76mYErjOtlzy8yETtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04c55b88b.mp4?token=kykL9qsT7uNYhUyBkbru_fIsFwsw5Skgdzt-8ou3u7Zems8kqAJxR5NxFuzMYaK1vDGKjzHwDwwfNvaPBZwJcxQ_jlzOUZg8whz4l4H6w7c4Pqlo3egIvJT7hHOy8ZjjS_SO6tdJUm7HgKdP9F9bjpGMByyANmF_kHJZsR9iK2EYjnCc8jWkWMmq9dJ5i1ApZ2IdVgQF1H2L7utOcoT4qX02hCb9c_91LtC1FocBDBo7ELRzKz8C0nsKN_KvxKZfpwNiNdfTuMHTMtU1FX3x8YzUHrNTcRLaI7PUvo7qpW9tYgc3IAOpUNSnK742ZGkTNbje76mYErjOtlzy8yETtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علاقه‌ی بی‌پایان مردم به خوک زرد؛ بیشترین هو کردن تاریخ ورزشگاه مت‌لایف به نام رئیس‌جمهور کودک‌کش آمریکا ثبت شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/673304" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صداهای شنیده در اصفهان ناشی از انفجارهای کنترل شده است
مدیرکل مدیریت بحران استانداری اصفهان:
🔹
انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده در جنوب و غرب شهر اصفهان بهارستان  و محدوده صفه و محدوده شهر ابریشم از صبح روز جاری تا بعدازظهر ادامه دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673303" target="_blank">📅 09:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
♦️
کوزران کرمانشاه دوباره لرزید
🔹
به فاصلۀ ۵ دقیقه از زمین‌لرزۀ اول، پس‌لرزۀ دیگری به بزرگی ۵.۷ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.  #اخبار_کرمانشاه در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/673302" target="_blank">📅 09:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07536f9517.mp4?token=j8bggeYH0l_E7ffnPYLxA7Kv1ERbKgGhjFrBGrBAqlgZ1VdhbzpnGEDea12HcfLp6s32e685nqq3nopuMzS2hWQ0FsqFfbJruMyRUwlFjkD90mOC3jL6K_bcleYakt0J7YnKCAF0JJoNon-yC_k9MyNKo1AVKmekDmkCyO3AtCY1N-CTgC6Qit8iyVsO74cm8lwPa0Rwns8lLA-l75UUYjbnT6UtV3iUVIJIOGS_smzBSO95uVxJFKFAqCj7s3AJKybv1saCtEzA3n5sULl0gD49af4TEfl4KLMfS0ZsZfJWWTC3qDmV8U16qCKilxxCRDDe8jAJ9Aag1AMtzNAIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07536f9517.mp4?token=j8bggeYH0l_E7ffnPYLxA7Kv1ERbKgGhjFrBGrBAqlgZ1VdhbzpnGEDea12HcfLp6s32e685nqq3nopuMzS2hWQ0FsqFfbJruMyRUwlFjkD90mOC3jL6K_bcleYakt0J7YnKCAF0JJoNon-yC_k9MyNKo1AVKmekDmkCyO3AtCY1N-CTgC6Qit8iyVsO74cm8lwPa0Rwns8lLA-l75UUYjbnT6UtV3iUVIJIOGS_smzBSO95uVxJFKFAqCj7s3AJKybv1saCtEzA3n5sULl0gD49af4TEfl4KLMfS0ZsZfJWWTC3qDmV8U16qCKilxxCRDDe8jAJ9Aag1AMtzNAIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت‌های بزرگ همیشه اهل حق را «برهم‌زننده آرامش جهان» می‌خوانند؛ اما ما اجازه نخواهیم داد آرامشِ ظلم، جای عدالت را بگیرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/673301" target="_blank">📅 09:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673300">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ظریف:‌ پایان جنگ و صلح پایدار نیازمند نگرش جدیدی به امنیت منطقه است
🔹
هشدار پلیس به زائران اربعین:حمل برخی   داروها در عراق جرم است
🔹
نرخ پارکینگ مرز مهران ۶۰ هزار تومان تعیین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/673300" target="_blank">📅 09:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
چند نقطه شهر بوشهر هدف اصابت پرتابه دشمن قرار گرفت
فرماندار بوشهر:
🔹
دقایقی پیش چند نقطه شهر بوشهر مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت. / ایرنا
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/673299" target="_blank">📅 09:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
انفجار در قلب پایگاه آمریکایی بحرین؛ تصاویر ماهواره‌ای از خسارت به مرکز فرماندهی و داده‌های هوش مصنوعی پس از حمله کوبنده ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/673298" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
انفجار در قلب پایگاه آمریکایی بحرین؛ تصاویر ماهواره‌ای از خسارت به مرکز فرماندهی و داده‌های هوش مصنوعی پس از حمله کوبنده ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/673296" target="_blank">📅 09:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHytBbDViE9vF61jBIZL3hKz4yBDSdhjgX4IyrSgSxmVokA1-xPEDBRPLemDsxsh1vPkinlT9yS1j9F3oB4SgRCB6EwRdEz_hqveqCyWKbMfydm_Tphe18434XH-mvTnc1QED23Pvjh4nIAEs9CrIuTCQdE11fP3Bh3NuQqiklYcp2RuflgM2-X7lWgtsB0y0qWKYnip5sr4L7jHWtvjBn83Mcm9KwcVjEQKAl7EIHGIoanTrOy9E1lOHBitU7uiXKttDJj4O-bGGrKdOEyOqnXyDhXQbeAj-wJDqQJmL2SzUP4mT2LQoFR5jQ-NtPpajM4oGSNcAlTV3zMrHkDTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار سهام بعد از ۸ روز مثبت شد/ تسخیر کانال ۴.۸ میلیون واحد
🔹
شاخص کل بورس تهران ۷۸ هزار واحد رشد کرد و به تراز ۴ میلیون و ۸۳۳ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/673295" target="_blank">📅 09:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
اسپانیا برای دومین بار قهرمان جهان شد/ پایان رؤیای مسی در شب سرخ نیوجرسی
⬛️
🇦🇷
0️⃣
🏆
1️⃣
🇪🇸
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/673292" target="_blank">📅 09:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=hV3wspVdAR4yNa-C8GkpwDnImuSGmVBJIRDDNHKN_TYh72kNEpg7V11Fc3wJusGMjTOFWHa4vItZoSw7_vc39NTAc7sYZMtRsDHYVGH8OvN4ZXk4yHdR8JbevUb8ZwB_cRMmNwH9ybZf8pCj1k34-6g68mTvRHYfkGOwjjKqGNMO133ieApREwGat4gJmAa5c4mYXLzgyEiPdzbn_cVC9gxjfeBSp_Dv6s_N5ls8M9QgkdcrosTYLIyFgsR_dRfRx6S4v8GIxMFffHHy3r-s7orre0v2rHlzP_uPmsHiWnmm19m_D2Wh5ieDvlibfXI1MrP9qD0Q7LDOZvX1y-fOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=hV3wspVdAR4yNa-C8GkpwDnImuSGmVBJIRDDNHKN_TYh72kNEpg7V11Fc3wJusGMjTOFWHa4vItZoSw7_vc39NTAc7sYZMtRsDHYVGH8OvN4ZXk4yHdR8JbevUb8ZwB_cRMmNwH9ybZf8pCj1k34-6g68mTvRHYfkGOwjjKqGNMO133ieApREwGat4gJmAa5c4mYXLzgyEiPdzbn_cVC9gxjfeBSp_Dv6s_N5ls8M9QgkdcrosTYLIyFgsR_dRfRx6S4v8GIxMFffHHy3r-s7orre0v2rHlzP_uPmsHiWnmm19m_D2Wh5ieDvlibfXI1MrP9qD0Q7LDOZvX1y-fOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلگرام حالا از تصاویر اسلایدی پشتیبانی می‌کند
🔹
«پاول دورف»، مدیرعامل تلگرام، اعلام کرد که قابلیت Carousels به این پیام‌رسان اضافه شده است. او به شوخی گفت با این قابلیت کاربران اکنون می‌توانند تصاویر گربه‌ها را درون اسلایدهای ارائه خود بگذارند. با این ویژگی می‌توان با کشیدن انگشت به چپ و راست بین عکس‌ها جابه‌جا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673291" target="_blank">📅 09:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a1672b48.mp4?token=GPZuC6nXC4MJIsfZ2zrAJZN7cZbJ0AVdBKHyOMGNXgQZLCrqnyK-9FTUbI3uI5ZgsajVTPh1bh8OtZFjfWuaWzHtCx48OmyH-i6H9h2fu9Hj8H66aqQ9756jLxSkkO7qV7ptA68ceSf71y36i7wMScjLTUdn7S2pR-OKH9tOkj8fk1Ayf0QHBVMbRLZ36-F1KRDEoH9D-xRCkW1cu2tswI33j6QCCtLpbb5GizySsIRtic91wD_eDfu_OnhR4wbdc30ReHVwq3hLtFmXITwRB2e404lDIm076Ca1n3Gw8beYTjuRdi46EaHT-Og1x8PJ8PcqhS8Uh5a-sNkJrzcMPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a1672b48.mp4?token=GPZuC6nXC4MJIsfZ2zrAJZN7cZbJ0AVdBKHyOMGNXgQZLCrqnyK-9FTUbI3uI5ZgsajVTPh1bh8OtZFjfWuaWzHtCx48OmyH-i6H9h2fu9Hj8H66aqQ9756jLxSkkO7qV7ptA68ceSf71y36i7wMScjLTUdn7S2pR-OKH9tOkj8fk1Ayf0QHBVMbRLZ36-F1KRDEoH9D-xRCkW1cu2tswI33j6QCCtLpbb5GizySsIRtic91wD_eDfu_OnhR4wbdc30ReHVwq3hLtFmXITwRB2e404lDIm076Ca1n3Gw8beYTjuRdi46EaHT-Og1x8PJ8PcqhS8Uh5a-sNkJrzcMPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه‌ای دقیق در آسمان اردن؛
اصابت مستقیم موشک به پایگاه هوایی موفق السلطی اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/673286" target="_blank">📅 09:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مدیرکل مدیریت بحران آذربایجان‌غربی: بامداد امروز دوشنبه، نقطه‌ای در حوالی ارومیه هدف اصابت پرتابه دشمن قرار گرفت
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673285" target="_blank">📅 08:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIFbfDONoeZS98SGwJvxqYXqCNA00l0CfwNTs84R26PdgIuyMr_odyY6zFIvjvm8pdT8RdU83PsBneKCdPMS8trZ4d21OJD0rg67Eb-vvVj05--HwQ2jfYz5SmVCKGtR3ebvpqnkPFFXmymh3HEQCB8cAYUohCb0MfLWQs2bIr0hs9O4d66bRfeyH85JosLzpvlgozqPIPl74l26vu1cNVrixFwvemyVM0-4V_jHXTCf9Vnq-6A00HwKnuZJGlMkmOYSH2IRt7toQgWhGNTD2ywZBrI7uFkpOmMCPZnNYKw0LtLLkKlb5XCJCPrkZ1HT-opAcClB_mk9fLYYvPY2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار فرمانده نیروی هوایی عربستان و معاون فرمانده تروریستی سنتکام
🔹
این دومین دیدار میان وزارت دفاع عربستان و سنتکام در روزهای اخیر با هدف تقویت همکاری نظامی است.
🔹
این مذاکرات همزمان با تشدید تنش‌های منطقه‌ای و تجدید رویارویی میان تهران و واشنگتن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/673284" target="_blank">📅 08:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2jabE0Ouzt4ZxHCLZr00hgcaEPTcpaRVkqeeGdLC5vmq62tO3WXNYOShLfsMIkR-NadW5Fhm4u16tFbAMfjDSUSGlcl4v_ZnttLK3QeG-1Y2-RSPevNHYVkGwKaiY92lnDmB5-5Xk0UD0f8R7mCBwyLGt_THxLmi8bxrZrS68gxjuXhHU37uepN-GUXICEVAkP8hmmHrWctSJEqfw7FIycbnfFzMe0HS_6kPuvBq3unCYGlriaqZHY8VAK04j9vjrlxR_X3TYWKwaL0mfVYOwokW-JRWADHwUcpiLCkIfKR-Xnveo0PfMvqmLrxPE65_mTxPb77ojwaXSE23Q4C2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امام جمعه اهل سنت میرجاوه ساعت ۴ صبح توسط افراد  ناشناس ترور شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/673283" target="_blank">📅 08:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITmX2B9--j4gGreFeQfxik3QJnuPMXJeYN81VZ0rao70tA8N6WVUCa0Hkg6ZEwM0WUlfc1CrGj_WeKLSeUncSX9lUV0CmoiIWa6YfedoQ7bNOvgxKrgLETtCURXTnXdG1TFU3MgYqS0ulGBJHyp1RkYwZIOB4Y-wxF5SmPvNchprGhOJ6hrvrVQYrTsYlsKuaV6F_Rn3H3cqFtnU45nC4jU38pyiJWUcwfqv6qy4luJ4F8DrVlwjwS-BDlJDUVVB_-iJ6-LemzZoEz0PnspRL2PBNJ3qkH1w5yGKOqFXeblzL8ZO-l2T9PRsWMNvBOfAaw2d6jc4oEzDCUki9D3OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/673281" target="_blank">📅 08:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
فقط ۲ روز تا پایان مهلت استفاده از اعتبار کالابرگ باقی مانده است
🔹
معاون اقتصادی وزارت تعاون، کار و رفاه اجتماعی: مهلت استفاده از اعتبار یک میلیون تومانی کالابرگ خردادماه، تا پایان ۳۱ تیرماه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/673280" target="_blank">📅 08:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کیهان: اقدامات افراطی وبدگمانی به مسئولین ، نشاط جامعه را از بین می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/673279" target="_blank">📅 08:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
منابع محلی از شنیده‌شدن صدای چندین انفجار در کویت خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/673278" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
صدای انفجار در نزدیکی پایگاه پشتیبانی دریایی بحرین شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/673277" target="_blank">📅 08:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
گزارش صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن به کشورمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/673276" target="_blank">📅 08:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ9 در آسمان اسلام‌آباد غرب
🔹
یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان اسلام آباد غرب رهگیری و ساقط شد./ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/673275" target="_blank">📅 07:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یک منطقه در خورموج شهرستان دشتی مورد تهاجم دشمن آمریکایی قرار گرفت  یک منبع آگاه:
🔹
یک منطقه در خورموج شهرستان دشتی مورد تهاجم دشمن آمریکایی قرار گرفت.
🔹
این حمله موجب قطعی برق در برخی نقاط خورموج شده است/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/673274" target="_blank">📅 07:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادارات سیستان و بلوچستان به دلیل گرمای هوا امروز، ۲ ساعت زودتر به پایان خواهند رسید
🔹
روبیو به عبور موشک ایرانی از سامانه پدافندی در اردن اذعان کرد
🔹
رگبار باران و وزش باد شدید در ۶ استان نوار شمالی کشور از امروز تا چهارشنبه
🔹
دریای خزر تا فردا مواج و تعطیل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/673273" target="_blank">📅 07:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.  #اخبار_کرمانشاه در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/673272" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
♦️
منابع عربی از حملۀ هوایی و شنیده‌شدن صدای انفجار در پایگاه‌های آمریکایی بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/673270" target="_blank">📅 07:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
زلزلۀ ۵٫۲ ریشتری در کوزران کرمانشاه
🔹
ساعت ۷:۱۳ دقیقۀ صبح امروز، زمین‌لرزه‌ای به بزرگی ۵٫۲ ریشتر حوالی کوزران در استان کرمانشاه را لرزاند.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/673269" target="_blank">📅 07:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K52_nm344kYUipuSjXebGe5K0iEaRSX-esjXdaKrQwNts5GChfEjwYROpSy32icQHqVR6Xe4_lSHa04JxhANsqbjw9m6rJSRBGe-RfmTDeOXo6yJ-rvszBFAdwCs_IjOf6bSEfCC_OLGJCFZ_Cm4c8aBU7qyFFnCl-wdiyntHeA-2EcnKqbv4xgMDsK6ersY6M4xnCbhB2dDMzclF-iLqPbB363fqhEFIScPf6adQ8TVyYPJOTxGaknxGKVef0RJPvQbgAFYHaOSIrBDisphAo1JAdsHcLVAEVWtmJz2v9tadJaBfvwMSul8OSSWV_xwJ8_TPxTeQVyMICoQ6zI3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۹ تیر ماه
۵ صفر ‌‌۱۴۴۸
۲۰ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/673268" target="_blank">📅 07:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند  روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/673267" target="_blank">📅 05:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: بهای نفت خام برنت از ۹۰ دلار در هر بشکه عبور کرد و به بالاترین سطح خود از ژوئن (خرداد) تاکنون رسید
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/673266" target="_blank">📅 04:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/673265" target="_blank">📅 04:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مهر: صدای چند انفجار در شهرستان دشتی بوشهر شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/673264" target="_blank">📅 04:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4b0f0d21.mp4?token=FYcT9QkvDKzMl94xObl6Vkddc37r9ogKrC7GvmjpKQSnW3ELeopYUED8xbWsLqM-ZJmSKlFS6MYHXp1Bimh8dcbX8pa-pGMSed07UD3AE8s55c169Q-8ZDMsf8I1NE4Uythl5htZ2OpanHOY3Wor3f9nvgQYZVoTbKU3m_qvxNsz20z5n4LFdsPVa-5vzT0M0Ut5UgRx1GPht7Loqhz9mQwrB5wZ5yYiw9MVvpch7LEPmauOTv5xsA1r-KkXkFoeKpFijXmI61xWPkez8utWEZTt2rEAfiIY4__xYUKLuHbAomMnbi-svR4WvTD8wQgwNJ7gS8k3p3rvsswLBwFpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4b0f0d21.mp4?token=FYcT9QkvDKzMl94xObl6Vkddc37r9ogKrC7GvmjpKQSnW3ELeopYUED8xbWsLqM-ZJmSKlFS6MYHXp1Bimh8dcbX8pa-pGMSed07UD3AE8s55c169Q-8ZDMsf8I1NE4Uythl5htZ2OpanHOY3Wor3f9nvgQYZVoTbKU3m_qvxNsz20z5n4LFdsPVa-5vzT0M0Ut5UgRx1GPht7Loqhz9mQwrB5wZ5yYiw9MVvpch7LEPmauOTv5xsA1r-KkXkFoeKpFijXmI61xWPkez8utWEZTt2rEAfiIY4__xYUKLuHbAomMnbi-svR4WvTD8wQgwNJ7gS8k3p3rvsswLBwFpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرمربی آرژانتین درحالی که سعی در کنترل احساسات خود داشت گفت: تا عمق وجودم درد میکشم!
🔹
به اعتقاد من، مسی بهترین بازیکنی است که تاکنون پا به زمین فوتبال گذاشته است.
🔹
ساختن و تکرار کردن همچین گروه قدرتمندی بسیار دشوار خواهد بود و این درد دارد.
🔹
اسکالونی نتوانست اشک های خود را کنترل کند و نشست خبری را ترک کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/673263" target="_blank">📅 04:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60f4fe31b.mp4?token=ufb3L1cxb_OmM1Ct_AURC2yPJLjeTAQfT9LOXBkvelggyBBUj2Us1umRhpXGnj-7fUMRlaMS2RNZzHr3ywrIojNczeTJEghHFN4-XQ6OARZI1pSTjnxBxPeuDRMe2GvojOJvZe6c578RJFtOQ78lHnBMB2By-r2vVap81KG1qB579RmtlDJYVKjb-7BfbFK6OPsELts5_9JvFtFDm_B8hhPFT3K6FNXL_ce4msKzsl8XLcNhEGJq9oRYFdKPD7APXn9zRcM14BFkJ2U6mxAjvrVcyBoO88797yuMvSmwBhndGWnXc2OoH2faN9i-IY0kHplpIEwxIjpZ1dei8yYEGAmUsnVwrjaCeUaoOqk56n2k2ZTC5bOR-BUp-U2Jek3zKzXa3tO5FLZxucPtwpTG_lZax4XwAiHnzOZT8Kz1IkYOS5CnPzTKndVCta-f4RdJleRS7SzWt0Kog_Pzaa-vxNmffSzA3b8IJVUZ2YWgioYWu3RFf-MmQ35yQCZ8SleqnrStmT8ZNOllst5bITtaXNRSDg3Jj56fOwAd91TFB4LZggL7kZDji7gk-KnQpEf96rV4xKlFJkhrQoNbw8xWrGIMJcVoeBVY3_3Z60abcAW3ggNMb7m5kl4f4jEoe01HD3d3zo4g3nbxmD1knneseUfGsgN281fG7ZUmQ-bPK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60f4fe31b.mp4?token=ufb3L1cxb_OmM1Ct_AURC2yPJLjeTAQfT9LOXBkvelggyBBUj2Us1umRhpXGnj-7fUMRlaMS2RNZzHr3ywrIojNczeTJEghHFN4-XQ6OARZI1pSTjnxBxPeuDRMe2GvojOJvZe6c578RJFtOQ78lHnBMB2By-r2vVap81KG1qB579RmtlDJYVKjb-7BfbFK6OPsELts5_9JvFtFDm_B8hhPFT3K6FNXL_ce4msKzsl8XLcNhEGJq9oRYFdKPD7APXn9zRcM14BFkJ2U6mxAjvrVcyBoO88797yuMvSmwBhndGWnXc2OoH2faN9i-IY0kHplpIEwxIjpZ1dei8yYEGAmUsnVwrjaCeUaoOqk56n2k2ZTC5bOR-BUp-U2Jek3zKzXa3tO5FLZxucPtwpTG_lZax4XwAiHnzOZT8Kz1IkYOS5CnPzTKndVCta-f4RdJleRS7SzWt0Kog_Pzaa-vxNmffSzA3b8IJVUZ2YWgioYWu3RFf-MmQ35yQCZ8SleqnrStmT8ZNOllst5bITtaXNRSDg3Jj56fOwAd91TFB4LZggL7kZDji7gk-KnQpEf96rV4xKlFJkhrQoNbw8xWrGIMJcVoeBVY3_3Z60abcAW3ggNMb7m5kl4f4jEoe01HD3d3zo4g3nbxmD1knneseUfGsgN281fG7ZUmQ-bPK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی که نتانیاهو قبل از فینال جام جهانی منتشر کرد
🔹
نتانیاهو قبل از بازی فینال در تماس تلفنی خطاب به رئیس‌جمهور آرژانتین، خاویر میلی: ما از آرژانتین به طرق مختلف حمایت می‌کنیم، از جمله فردا (در فینال). من پنهان نمی‌کنم که طرفدار آرژانتین هستم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/673262" target="_blank">📅 04:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0381272b35.mp4?token=lhHvXUAuQpfIvfpC5x4C-6XEj-MH5wyNelyhMCPWC0qq0HL-yZpYc5MhpoUceNe1kFwPXRhdSZ1vuK_22he7uWxyVwleDYav9WquOEvflTZBsfPd0RQ9M26hzNfJ_Hnr5cG0XSDHKW4Pd7a42WiY-l7GL7FpXBO2kJY_LXZhZKwr4B-nfrl3oRBlWZQ6CJfR6OYfI12rgJxLu1koeaW_S5hJz4_bo7mWxvz49YXZBLQz6MIitSUJ6hEHhk9LA9DWtGgcdi1WK9au3uE14I2wX409GUgXOm7zo25nvieZzxkCF5imSESjk5epwtGgC2csLUdQAdAFZkNhVMY3OlnUXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0381272b35.mp4?token=lhHvXUAuQpfIvfpC5x4C-6XEj-MH5wyNelyhMCPWC0qq0HL-yZpYc5MhpoUceNe1kFwPXRhdSZ1vuK_22he7uWxyVwleDYav9WquOEvflTZBsfPd0RQ9M26hzNfJ_Hnr5cG0XSDHKW4Pd7a42WiY-l7GL7FpXBO2kJY_LXZhZKwr4B-nfrl3oRBlWZQ6CJfR6OYfI12rgJxLu1koeaW_S5hJz4_bo7mWxvz49YXZBLQz6MIitSUJ6hEHhk9LA9DWtGgcdi1WK9au3uE14I2wX409GUgXOm7zo25nvieZzxkCF5imSESjk5epwtGgC2csLUdQAdAFZkNhVMY3OlnUXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: فکر می‌کردیم دو نفر در حملات ایران کشته شدند اما احتمالا سه نفر بودند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/673261" target="_blank">📅 04:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52efb5cec6.mp4?token=TVPuQwqMsc-fuuidCBRsTtfvZKlFA6Um-fa7W-YyWkvRdPD-6Pd3zUKNQC3k0QeKMyYZ4vzsl2P86cUebKO2Enp6-EGut5cB4sr61_K9FI0ndFIn4ojGsCzdtc8QcvVRObHRr0DJsX561AvIemekXI1knPMgA4P07YgEvP9fM9Txq8SNPGw9ZtiHEh_UtJE8YjsncqlOP5Lduv8P7ixvUj3NHWj_bQd1j8on85Rm-cNZCAuARQpugNJnxBxv7E8SPVXDA-kQ9LSvVceCvK4o4Px4uzGZF8ggsZ3iBgMR5VdnUi4IEMjL6i1mBwlh3ZYNp3v5HgpmBEden9DJp2fDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52efb5cec6.mp4?token=TVPuQwqMsc-fuuidCBRsTtfvZKlFA6Um-fa7W-YyWkvRdPD-6Pd3zUKNQC3k0QeKMyYZ4vzsl2P86cUebKO2Enp6-EGut5cB4sr61_K9FI0ndFIn4ojGsCzdtc8QcvVRObHRr0DJsX561AvIemekXI1knPMgA4P07YgEvP9fM9Txq8SNPGw9ZtiHEh_UtJE8YjsncqlOP5Lduv8P7ixvUj3NHWj_bQd1j8on85Rm-cNZCAuARQpugNJnxBxv7E8SPVXDA-kQ9LSvVceCvK4o4Px4uzGZF8ggsZ3iBgMR5VdnUi4IEMjL6i1mBwlh3ZYNp3v5HgpmBEden9DJp2fDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت حملات مکرر آمریکا به سیریک اعلام شد
🔹
دشمن سعی دارد با حمله به سیریک، اشراف اطلاعاتی ایران به تنگۀ هرمز را قطع کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/673260" target="_blank">📅 04:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuVWMsOjHnvP-A3ru_dmR-QRqD841qkxTOWc7Kh1zLv7IKaT5p0LI8nt2Z_K6EcBAkzqFXLARDufx3YkwPBxKBnBJbu74oZa9ZZDFMXe1mRInvaC4VDWLtDiKwcZ8c40RR_KnnF1KnC53EGBBAMFzNGJT3FvslcA6d1CLwewQ5slBtKNVh-TqTOF5DN9pVXah67EXsEVVEGkY8q0cR1PnDEfK35-VHPaGoFlBRvPJaQui_ZcKKqUH-hgLF1ANCrKRZ2tGY8BPIrJ46RdEWlVCitgknIAPqAAbNWOuVW6_AQXjCxOWsTrgXTY5KDEIzxrc1YEO9-OqQU0vUOx__9MTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یامال بر دیوارهای غزه
شکرا یامال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/673259" target="_blank">📅 04:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=F3Zx18zGDaJGoZnscDDm9Krx5JheWWkkCDnncb7Uq-dWnOtvlkY2zxKra3mBlPX9_eFYYYrJjrw1IN3snsbtmemFJaegmoi_coH9jZIIUDcgCJnZLJZFFnOgM1n8MbrMHQX0yCB5dYUOtZ0KTx-Q5F5_mt9_XIZAxZf12eFqoWUJYM0-QJID71gbd-MiXHn4m49xduo1z6OhmAWJX_bjiqF4GTHVberP2jevucfZfl1t4pBjCjr8S9aXNhBnYbJ8f-TqeTJVWyjyu06pYeu5mlJcpQIRrEsR4GaVkvdPie6YNZvptMIm8_L5zTwMAttUgVZMNyXKHuGvltlYwbAOmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce1378.mp4?token=F3Zx18zGDaJGoZnscDDm9Krx5JheWWkkCDnncb7Uq-dWnOtvlkY2zxKra3mBlPX9_eFYYYrJjrw1IN3snsbtmemFJaegmoi_coH9jZIIUDcgCJnZLJZFFnOgM1n8MbrMHQX0yCB5dYUOtZ0KTx-Q5F5_mt9_XIZAxZf12eFqoWUJYM0-QJID71gbd-MiXHn4m49xduo1z6OhmAWJX_bjiqF4GTHVberP2jevucfZfl1t4pBjCjr8S9aXNhBnYbJ8f-TqeTJVWyjyu06pYeu5mlJcpQIRrEsR4GaVkvdPie6YNZvptMIm8_L5zTwMAttUgVZMNyXKHuGvltlYwbAOmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش صداوسیما از تبریز: صدای ۳ انفجار از غرب تبریز شنیده شد
🔹
این اولین حمله به تبریز در دور جدید حملات دشمن به کشورمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/673258" target="_blank">📅 04:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای خوک هار: امشب ضربات سختی به ایران وارد کردیم
🔹
ما امشب به احترام سه سرباز کشته‌شده، ایران را به‌شدت هدف قرار دادیم.
🔹
ایران احتمالاً تعدادی موشک و پهپاد در اختیار دارد، اما تعداد آن‌ها زیاد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/673257" target="_blank">📅 04:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای
خوک هار: امشب ضربات سختی به ایران وارد کردیم
🔹
ما امشب به احترام سه سرباز کشته‌شده، ایران را به‌شدت هدف قرار دادیم.
🔹
ایران احتمالاً تعدادی موشک و پهپاد در اختیار دارد، اما تعداد آن‌ها زیاد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/673256" target="_blank">📅 03:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سفارت آمریکا برای اتباع خود در بحرین هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در منامه از تمامی شهروندان این کشور خواست هوشیاری لازم را حفظ کرده و از دستورالعمل‌های مقامات محلی پیروی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673255" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673254">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک شناور در شمال‌غربی منطقه «کمزار» در نزدیکی سواحل عمان دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/673254" target="_blank">📅 03:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673253">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/673253" target="_blank">📅 03:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
صدای دو انفجار در حوالی خورموج بوشهر شنیده شد
🔹
در استان بوشهر، صدای دو انفجار از حوالی خورموج به گوش رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/673252" target="_blank">📅 03:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjFijP77yDIVyw-L9XVs3gA_VRAQs9rxoMpJXMFy0Sz8vjyJ5oqRw2LsW1FXMx0_-ERK-cZMZhJID4Dssjk97iJudlGbQ78o0UNSXScWohkBuFLFkpCHAdjEpefAq0TfeUNb9xRVN9nyySEi7hYmq_CFNMtARsTp5VbQwPJCSk7KMk3ctgdQtEMsqkE4ma9aP7lhCo6ojPCPmQWw-HM8tjRBIimeGrNNsba9jQiqPow9mORORzcMVkuvt1ViIQ7kxQIe4K46kfsfXsv9f2Yf0CaWYIP-AXwCcTD0jykoJiV4PyBQzC17JawELumIOR8mCWUTB3ckYbG8HYyq_09Y2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه دریایی در نزدیکی سواحل عمان خبر داد و اعلام کرد یک شناور در شمال‌غربی منطقه «کمزار» دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/673251" target="_blank">📅 03:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/673250" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شنیده شدن دست‌کم ۳ انفجار در جاسک
🔹
منابع محلی از شنیده شدن دست‌کم سه صدای انفجار در شهر جاسک واقع در استان هرمزگان خبر می‌دهند.
🔹
هنوز اطلاعات دقیقی از منشأ و علت این صداها در دست نیست و مقامات رسمی تا این لحظه واکنشی به این حادثه نشان نداده‌اند. وضعیت در منطقه تحت بررسی است.
🔹
جزئیات تکمیلی در خصوص این رویداد و خسارات احتمالی آن متعاقباً اعلام خواهد شد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/673249" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صدای دو انفجار در حوالی خورموج بوشهر شنیده شد
🔹
در استان بوشهر، صدای دو انفجار از حوالی خورموج به گوش رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673248" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCWqQJnk2FfHvUKXHgJE7FzSIxFSfYXmRTclDuESA8hROkh0UfMb97He7fNCpNKWcS0KTz4gA1XhyuuqdxbSNXMi6fZPkriQUWh9pVs3OiZmL9Yvp4eucGJbExHGUBfqGlJpboE_8NoG1pW79CynxO6Lospj6L7p1wiyk8IEoGne6jj_dQb5bhfE5m1iibv9h0k0kCtgtXXY3oHvvOxMS69vx1FVKd_yw1_Zdcnn9eaZ48PUwucd3DoMsYo7R7rcqOqmLLPJzDKc8Xfr3SNRpd-HcRCZiY8vNm2HBGNbRtt2KNPhZ7_LzQbb_84sN7pRVRetxLxFuqGqlwG01mQy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر معنادار از مسی و جامی که ۳.۵ سال پیش بر روی دستان او بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673247" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
برخی منابع از شلیک موشک به سمت کشتی‌های متخلف در سواحل امارات گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/673246" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ساکنان محلی از شنیده شدن صدای چند انفجار در محدوده شهرستان سیریک خبر دادند
🔹
بامداد دوشنبه برخی منابع خبری و ساکنان محلی از شنیده شدن صدای انفجارهایی در شهرستان سیریک خبر دادند.
🔹
هنوز ماهیت صداهای شنیده شده توسط مردم مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/673245" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سفارت آمریکا برای اتباع خود در بحرین هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در منامه از تمامی شهروندان این کشور خواست هوشیاری لازم را حفظ کرده و از دستورالعمل‌های مقامات محلی پیروی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673244" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/673243" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای انفجار در امارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/673242" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
صدای چند انفجار در چابهار شنیده شد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/673241" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی
🔹
لحظاتی پیش گزارش‌های مردمی حاکی از شنیدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی در خوزستان است.
🔹
اخبار تکمیلی از زبان منابع رسمی به‌زودی ارسال می‌شود./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/673240" target="_blank">📅 03:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی
🔹
لحظاتی پیش گزارش‌های مردمی حاکی از شنیدن صدای چند انفجار در بندر ماهشهر و بندر امام خمینی در خوزستان است.
🔹
اخبار تکمیلی از زبان منابع رسمی به‌زودی ارسال می‌شود./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/673239" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c661eb85.mp4?token=Kw7O-Haub2js2ydqrrvTtwqxaHbUoSUGgEeYYSlr3IwGnA9C_sIr1_m7-1mRnLNkgYEFwrDcBjPN1Y93AJxKQ3gALwLfHNhU3dCj90-3WoxhFqLHc5KJY8nqchS9UZv4VFq83lXz6yerGkNGCGieOZKZVPbiuGPosxFIvKKj0ujIY8I1dBm7uTdpJMU9DaYp9j5tNEIwPnKB61dp5W-tKZ-tpxt_2bdHuCtDQgGXh4mdTTi0ddJ4ThLb9JM2YyyWT948C6Intwct8XzeMVbiw8yS3jZS3xsmzZWioqPqvbb7gN96DTSKVE0lX3kA5-7hO4fwcG3S6QuWKL_MXmTKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c661eb85.mp4?token=Kw7O-Haub2js2ydqrrvTtwqxaHbUoSUGgEeYYSlr3IwGnA9C_sIr1_m7-1mRnLNkgYEFwrDcBjPN1Y93AJxKQ3gALwLfHNhU3dCj90-3WoxhFqLHc5KJY8nqchS9UZv4VFq83lXz6yerGkNGCGieOZKZVPbiuGPosxFIvKKj0ujIY8I1dBm7uTdpJMU9DaYp9j5tNEIwPnKB61dp5W-tKZ-tpxt_2bdHuCtDQgGXh4mdTTi0ddJ4ThLb9JM2YyyWT948C6Intwct8XzeMVbiw8yS3jZS3xsmzZWioqPqvbb7gN96DTSKVE0lX3kA5-7hO4fwcG3S6QuWKL_MXmTKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش حماس به قهرمانی اسپانیا  باسم نعيم عضو دفتر سیاسی جنبش حماس:
🔹
ما پیروزی شایسته اسپانیا در جام جهانی فوتبال را تبریک می‌گوییم، این شادی را به فلسطین و حامیان آن هم تبریک می‌گوییم. «حتی اگر تنها فایده این پیروزی، آزار صهیونیست‌ها و همدستانشان باشد، همین…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/673238" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
انهدام پهپاد متخاصم در جنوب کشور
🔹
یک پهپاد متخاصم در آسمان جنوب ایران، توسط سامانه پدافند نیروهای مسلح ایران مورد ساقط شد.
🔹
اخبار تکمیلی بزودی اطلاع‌رسانی خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673237" target="_blank">📅 02:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN2t88jGGx-q4Oz5nWs5IW-Op75v2szFXl7mfqPwe7VSSlgdsAVwgi1lQBbazoTNjnFNb4xV_usk9rDZMkZ35ENmP8g_sYwkz16xYyEYP61fHRQjKEx7vXIAYbbc4knZ0xkJFXA4jVxhFClYTJHkQjzeKbR7smn2jWG1WCCnwli2mPvUcfQ-qZ76AfYx0aCi9kUkc2i6pgXFZj9C6sBmtPRoJjAdI3qVTusthf0Si_Pffs0XHtCEH-korRukFL_wwgCdK2f6DsELjKEL3xkByJFYcSDuPem-Z_ksIYt38jleQKL2lqL7LS0yxCDoomYpBETUg5m8D0DSGd80eg775Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb6a899b6.mp4?token=LnEz2AzQEL6YS_9xMzE9sJ4D2dfAmfAeKZ70-Y2_4eIk1fuDMRuM9JsS885yoiET91IJ9_qX-Z4OmxvN8vG-6ULH_HKs58kFcu9PN74S_kj3Or93rcPOSdsDP0EAnJ7Sm3UPmCsVOT_JwMRKsTMrc0VOerZDWVX5IMKWfBNYxd5h_3-Y9ywoRMxXcGE7SEOS4GW6O-j1sbHEsPATNZ47f3cjtgO83j5V497239fU9PLt0yiNaIOsSw0jLKSsonHawRMKaem3wDjP2NqHCcHbGllnMkxhaUz0jLOZuw5t9s3ll9iNSBj96EIYryh9hVvBpbb85Ik1dPOaSucVoDH2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb6a899b6.mp4?token=LnEz2AzQEL6YS_9xMzE9sJ4D2dfAmfAeKZ70-Y2_4eIk1fuDMRuM9JsS885yoiET91IJ9_qX-Z4OmxvN8vG-6ULH_HKs58kFcu9PN74S_kj3Or93rcPOSdsDP0EAnJ7Sm3UPmCsVOT_JwMRKsTMrc0VOerZDWVX5IMKWfBNYxd5h_3-Y9ywoRMxXcGE7SEOS4GW6O-j1sbHEsPATNZ47f3cjtgO83j5V497239fU9PLt0yiNaIOsSw0jLKSsonHawRMKaem3wDjP2NqHCcHbGllnMkxhaUz0jLOZuw5t9s3ll9iNSBj96EIYryh9hVvBpbb85Ik1dPOaSucVoDH2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بورخا ایگلسیاس، مهاجم تیم ملی اسپانیا با بی‌میلی ودر کمال بی‌توجهی به رئیس دولت تروریستی آمریکا، دست داد
🔹
علت دست دادن ایگلسیاس: «من نمی‌خواهم به زندان بروم!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/673235" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
صدای انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار در تبریز به گوش رسید، هنوز هیچ جزییاتی مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/673234" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای سنتکام: از ساعت ۷ عصر امروز به وقت شرق آمریکا (ET)، برای نهمین شب پیاپی موج جدیدی از حملات علیه ایران را آغاز کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/673233" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f0d26c63.mp4?token=qA76QjU55SSwE1tgXgWYdsdZTn0Co-BcJN6gV3yVeFVhKSmG2APSQbarLmURXK4NbQ37lag5vVqLT6KL-050Q6tlVDSAg37LlgydkkIddXNbU-upxQlo8ZALDEXhjFpyCwF3GHAx4SOqBRmyZbdJNtI6-qNCxdDm1nPUDdZhDmVJwONilZI8JVGCeZc6aJyUqtuy8NXexjzJrVAdk0VumFosjpuSHYY1ewLHW7ZznF-grUVmNzybU7Rw_sYYQuB4m9L6OVD5Osp-GPlxBl3-hICZTHkMutapMmdWweRU9etG6aPaSfG8ExGahlGpLBR3-bFn7Ls9pp6_8WLJl51e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون مقرهای تروریست‌ها تحت حملات شدید ایران
‎
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/673232" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLNmTUVkfjVA5sur3frCwb9VppNZ0rDZrlhCpZ6lM6cn0N_edpto1cR2Yye7zJVwtJWultKRBMpIJ30iu6wGNTRjuwUqfpi0NIVWBV5ni6bu4mWsKnTxgpQvI1pSkK8U_dbfO0S3MxleGxMuEpgfnD5-fCVLiz5TASnYjeLwdoXf1rvDYUoK8ywE59zcUJ_BTuc0wNeY_boHGUTSYWybtadcgp_uDRoGY4_cFoLZRoMHXGgEMU1pupTfoFO1W9NfMzidu5ldgCkf2peQn_H2BwbYFwxLI1bmyg5Nb9zEIr35jzusfTF9KKgmKPRfY4injqIph9kbSIxYhQ3a5p-ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-T0UgpED3zYEOWJ4jeF540GD8l94T1ONStQ6vY7WN3L5NO73SEdNN8GjTNA1z6A6HMdetrcSBVzxGgv0yAyrrqRgBsI8LhVmXbWxGFZiw1PW5_2YBJ0VVTFo48WZ7SzNf987GNhXG7AM4-bdLBsalFLUosy4awjXMtye2bY_5MhYeGu7DDZQmOI9D_CB5AGNPCuwa6rnbFC8Z4uoDznvYiyfhBlg0vGAyNj34Bsm9ccAUpyJNDyvvYFjaAxHOc6-IF9zZXEkLqog5ZLniCErm8QO20HPj_3zY61NC7LVd21ALnm5ch7j1n-UVyjWMmVbx4RPqZERTrNXpaCgLG6bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چشم‌های یامال احساس تنفر نسبت به ترامپ کودک‌کش را فریاد می‌زنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/673230" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdc7cef56.mp4?token=YAM_xG6gg1_O-BF4v6mvLwdooyQPk5ultOf6knKTBbQyLKnVnUieockMF-b1_c3eYaxB5E-p53GzUGwM9SvZ4_7zFmwViCjtPAWAQTGl9VhELbH7uCSH2N_Jiu1advtMPDLoqLjKzrT1609oRfgPRHCsQnWDEAeUZSoVKChZbaZv3YuZ8i-y5_PI0QTqd5bdfrGeD6IkkgLozijtAKItYm-3yS8QeN3hrVWWdXJ9Ux_rc0IEn7DHbC8me06i7akOn28TmLbQZaZSP721sv2mNNeFcmLZx79m0WKRU_DSmq937S9hCRPXleaxaP0P0sT3e-zHb1rgawnm8u5GLBNaTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن در ضاحیه بیروت در پی قهرمانی اسپانیا و شکست آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673229" target="_blank">📅 02:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3bc53ff5.mp4?token=WLMCR776wHEusVC5ZAzlc0No_5j__pMkyBBAAFxBViBJ4K-Z-HWduIanqTcZYuYUgGFtrIPJOEn0dqUX_FLfYlr3L0uSrG02cb5k3Vlwc_apRhLx-Q2YgtdexgXOTxnbn7EcbNAL0J2vGV6R3s-tkZTZrcgvTOp7hEIMcM1BNIhw0Cm30hdrpatvwwB1lHe4s2qBj_Egk3LMWJl-WOH9gu3rECoowKe0hlKCfZ12kKO1DN5QufzPr_bM1Ktt2fjC26i-W3zlECYMPXiJpXRCPSbs99ciBUex2vAHLsQJdf4MBJqnFEH-ywD3uywDnfwM4lXwWZshSH4FX3uZ5Q9uzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غزه درطول جام جهانی طرفدار اسپانیا بود ، همان طور که اسپانیا حامی فلسطین بود و معترض سرسخت به جنایات اسراییل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/673228" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
واکنش حماس به قهرمانی اسپانیا
باسم نعيم عضو دفتر سیاسی جنبش حماس:
🔹
ما پیروزی شایسته اسپانیا در جام جهانی فوتبال را تبریک می‌گوییم، این شادی را به فلسطین و حامیان آن هم تبریک می‌گوییم. «حتی اگر تنها فایده این پیروزی، آزار صهیونیست‌ها و همدستانشان باشد، همین کافی است.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/673226" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDJZWxeqsqr6qTSdXAtk3MNifjIjc0nxoLEvXrUsLe4eYbQb8yUhQ0vl-BrlFKj16Q051gVUr4p4lUJuBw1ecQhedOnOi3tyixBtdnBVuHrGEcldoPbdNy81-uCs32OjKSMBtqKSbNgsAwB949UQmdV1F_aoKlPd4iaQ2xFfSYvpjO-FYiflE5ydvjVVmrmF-nBs9Q8Xy6TvboqyuaqvECQXYZTTfJWHrNrK7IlCCW_xYD-3t3wjUFEQ0sPeP6jikZhmdyB-udSjRClY3Pj9Iow9W1RgMx4gPYFTN4Rwh1SL_RFbXTEUezPUYH41gXUR_rbGeR4QDYNaQ91TpE7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
طرح علاء اللقطه هنرمند فلسطینی به مناسبت قهرمانی تیم فوتبال اسپانیا در جام جهانی
۲٠۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/673225" target="_blank">📅 02:33 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
