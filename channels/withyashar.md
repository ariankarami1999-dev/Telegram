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
<img src="https://cdn4.telesco.pe/file/BCbA99rckAyKz2GUIxK4n71XL3x2mQYFDupAxHeCekMjFIzYziLS5kITo4WSQrRd0aSKY_Y3kr4i-InYzeFCNN-x_mer4qJ1d4_UpcGREWErMNA5-fvghmWC2oKvX0eB0VCeaG7SckV7N_tVi67TvDKaxfXxORHQwpy6E0WxHGdAYSbguh7NKXoLzt5gSXRQHJzHsX0MWAZ-__vEc0Q1JKOlJ9Lg5fBy8NtJnh8KLA8ZltSWHp1NCeWcZ_osCe_dVe4roiB6xSngN7piXZqAXiuU6rs__ILQvjJ8ShjJhcADycnDKp7A2b7pxmy5Ryy63B1jUTXG25h8cq285G7v7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 350K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 02:39:36</div>
<hr>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارشهای زیاد میگین که موج چندین انفجار در آق‌ قلا پنجره ها رو هم لرزونده ! آیا تررور هدفمند بوده ؟! هالیودی‌زدن ؟ همه سرگرم جنوب بودن هدف اصلی اونجا بوده ؟ خواهیم دید چه خواهد شد ! @withyashar</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/17015" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/17014" target="_blank">📅 02:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ، درباره ایران: ما به آن‌ها ضربه بسیار سنگینی وارد کردیم و من می‌گویم که ما به نسبت ۲۰ به ۱ به آن‌ها ضربه زدیم.
هر بار که آن‌ها به ما ضربه می‌زنند، ما ۲۰ برابر آن‌ها ضربه خواهیم زد.
وقتی آن‌ها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ خواهیم داد.
ما از نظر نظامی، پیروز شده‌ایم.
چند وقت پیش با ما تماس گرفتند. آن‌ها چقدر مشتاق به امضای یک توافق هستند. اما من نمی‌دانم که آیا آن‌ها شایسته امضای توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/17013" target="_blank">📅 02:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9jyd80YcIi34QGMezKgJYaHOHXJC8WwJJEHkAnO-Kz6-QXR7lDuJPxrKa9l69LdMbHv-SC_LisygJpfBU90mgLhR7qte9Wn--50fut-MSUY78BevBq-ge5y74vL-C629_q1z0vFCqGvEqm_N8PErQvzU9zOqX0Py0wSIIAE4a69At_MBZMqyGDbeBWs05OUR8oin8PL4tdfL5CUyZGlmhbzZCpIM3RAgEsm-WQnA9vrypvbaPQVlSzL23l3oafPryLd37C5tWLqxoPYIKZ1VajKGnagwDOi10EtyPyAdSVAZVlnngvIIopj21j6mOFVNkgYxWUyxym0MVXqUrZcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/17012" target="_blank">📅 02:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید باور نکنید ولی ده ها پیغام دارم استان گلستان در شمال کشور ۳ انفجار انجام گرفته !!!
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/17011" target="_blank">📅 02:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار در‌بندر لنگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/17010" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانشهر
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/17009" target="_blank">📅 02:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند @withyashar کاره موساده</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/17008" target="_blank">📅 01:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سپاه چرا انتقام نمیگیره
😾
🤣
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/17007" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajCGf8HGmRoBneepA817pCjDVy2oPG1kuVu1wcZSLroQBV1OHsrUxdUpBj8rr9RiDsFyoA3XMZ4_8EerP02Po8KY_r-cGf2hT5OZRs4H6b4LvOmJAlmlUoYKcCSfwzqtyOE6WCMulsYo_y5kMMaC2I4yYMadF9rBpu860fJ3rAYk-FvdKrgRG4FeXyZF--HO1UdWPFzBELgON-Z6PDDEJ5xXKynRhtn2RCbeG-xOWuNNPQAc-TkPEhdvdEOemJXSA8iifjO_14k9tuKR1XfSVEfZndlKLIVugmyEyNeC00fZ2h4UExIuDE0Pd_0xOgL9n9dhHDufg9U53g3HXAknug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ما تازه فرود آمدیم (انگلیس)و با هواپیمای جدید نیروی هوایی خود که قبلا به پایگاه نیروی هوایی سلطنتی میلدنهال بریتانیا فرستاده شده بود، ملاقات کردیم.
در مسیر بازگشت ما از ترکیه به ایالات متحده عملاً هیچ انحرافی در مسیر پرواز وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/17006" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با لبخند وارد شوید
😁</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/17005" target="_blank">📅 01:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش دو انفجار‌ جدید بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/17004" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند
@withyashar
کاره موساده</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/17003" target="_blank">📅 01:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/17002" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فاکس نی
وز به نقل از مقام کاخ سفید:
مرا
سم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/17001" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاهورا</strong></div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/17000" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHN3_D78NXngwAFGBfP7NEtMr7U4bJruQMx0GgfO1CwLBfO4dZumJjhokfoubjHHLGhOxEqQmPMoyb2n2lDEOFGeyUzlud2TkaidfbSbsbrAGzUn4CuNMwl_mCgyzbCskVMo2oAcdyJPxW0hcxarlKLbnXJiipyjCnVR_T3emSh9M3atjomAcCnsWWJpy7i1AaGINNpRbunG3ip433ribDUR4AhLmh1GXVK9c3FKlT4T3bs_A_G3wT4dvhm9hsPGWj2i7GDXE7ar4v_YnWL2hLKeDxa4rSIghvTsLakpg4n7k2QGBpgdeUdWHpeGd2DjEG7yWFTC14V1ElOY1x1Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاطی که امشب
تا این لحظه
مورد حملات امریکا بود :
از چابهار در شرق تا بوشهر در غرب، خط ساحلی جنوب ایران + جزایر
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16999" target="_blank">📅 01:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/withyashar/16998" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک مقام آمریکایی به شبکه سی‌ان‌ان گفت که "توافق آتش‌بس با ایران، حداقل به صورت موقت، متوقف شده است."
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/16997" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدا و سیما : اسرائیل در این حملات به جنوب ایران دست داشته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16996" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3v7-L5x21GKQhfkbu9S87Uhcr57fMaQcwVk9cJnWqOVV0O4JeqZlZ5smbkVKaToLCmk1pHCgkYF2hoJvcKIS6hTyBX5OXSBAp2o5ELsTFcmPqL0-BG-6GhkYxP9-l30n8nlugi5enoQo64XofjSPIIOCNDB7cBZMH0U1OBh-JUXFJ_klOHBMypN6yzW5iTWEdnYOBM5XUZrDcuDZKbVqG0oZ2xKimuNmp-GbUsl6yQ98vBrO2rfzxPyjwco_juM9pOPIa5oi1YiBlH73fwG153Jr6t2AwcnLVsS5ZLAOd3WNoHOSvqrRL7fSpPrzDbaKEECzWHDEK8TabCe6EZ96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر وقتی سیستان و بلوچستان ، فرودگاه ایرانشهر رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16995" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق‌ جنگ با یاشار : هر کسی دستشویی‌‌ داره بره بین دو نیمست
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16994" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تکمیلی : وقتی ستاد امنیتی بوشهر نمیدونه کی‌زده و میگه دشمن نمیگه امریکا یعنی‌ ممکنه این حملات از سمت کویت یا بحرین یا جای دیگه باشه ! در نتیجه من از‌کجا بدونم کی‌زده !!!! وقتی اینا به کشور های دیگه حمله میکنند آنها هم متقابلا جواب میدهند خیلی ساده است ! @withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16993" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ : این یک انتقام برای بمباران کشتی‌های ایرانی دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد! @withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16992" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ7k5I1IEwN1FKObYp0avbCWtZkHBQUbG50ovvcFXoWvYiqqpdv31DgnYz0Jad9pnpc1ZJCYCKqCM2sunyZoXgcAB4XWY64IT5xGi69v74zC_sElpQC3bK120nrVhxN-YH9PFIZ94OLLUZ9kzbbYgKZcdu6cwKZPUyWwzGacO5niu2JBzSI7YIDKb7LV0Gkb6sLv_CFhLh2i046F0PR2ZWcixqFea6w2gWMkgOPog-AAh_haAVbX9TeMaY-yp9bKmd9RXGnu1Mm7dKrrrs2I8HkKMMJuNs06874Ds9tuGq-m_aT0AJz2jsxd3tUGpRSI6fecJ7HL79iOwuZJtq9Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار  @withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16991" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فاکس‌نیوز: ناو گروه باکسر از ساعتی قبل وارد نبرد شده!
این ناو پس از چند هفته وقفه، روز گذشته به حوزه فعالیت سنتکام در شمال دریای عرب رسید و اکنون در حال پشتیبانی حمله به ایران است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16990" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a052382f.mp4?token=H0e8E8b28TPRdXkHpKeyVGPmTm4TL_WC8mn3ft03dhqEcVWn6PcNbApGnZ8lyZRZ1eBvIKeqelPlC4z3pPEtNiWydfJ0BdoiSp0KURMpenHLWKj0e993sFI6gg3SMG1ERE7ciy-ZKMTimus8Rc2Itvecm987GG0KhIG2lKcqwNFkVXXKEed-bPg3_mJWh7TVflzxSQoPMhs-0I-LSPB6YUC_zTtqWpDIYbCHf-apIL3rzB06sVE4XDsLzh4mXsJQgisy9ctnamATwMCjs7GZIf0-4Z9BF2fchoELhEMoVnfFUKKTqzwE4lzKcmdp3SRMxQAzrzPnhq-BUbyhWN2H1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a052382f.mp4?token=H0e8E8b28TPRdXkHpKeyVGPmTm4TL_WC8mn3ft03dhqEcVWn6PcNbApGnZ8lyZRZ1eBvIKeqelPlC4z3pPEtNiWydfJ0BdoiSp0KURMpenHLWKj0e993sFI6gg3SMG1ERE7ciy-ZKMTimus8Rc2Itvecm987GG0KhIG2lKcqwNFkVXXKEed-bPg3_mJWh7TVflzxSQoPMhs-0I-LSPB6YUC_zTtqWpDIYbCHf-apIL3rzB06sVE4XDsLzh4mXsJQgisy9ctnamATwMCjs7GZIf0-4Z9BF2fchoELhEMoVnfFUKKTqzwE4lzKcmdp3SRMxQAzrzPnhq-BUbyhWN2H1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج کنترل دریایی اسکله کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16988" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایرانشهر بلوچستان زدن الان ۳ انفجار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16987" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvkW3GoK9Ee0OM9LCH0afpUCT4AGuj0VyBaHDa8IJnE1asX6oa3Wy7Mpz2gQ8YizT2ol-CEC0S9en1MLm0CfWLI18Q_lKiCqd8viRX8bB9XM74NcEs15bQQY4NH7hgQx2bCHNrIuwvgvB0j45kg1Nh0YljOLpXK6A-pu13szOM4dFbTWZiQpv4Aa89bnFWpzQsa4oHjqcweXoVSZWeZHRNIrApfsztG2lP909Z0XzaFLApeRw6X1urtFds_PoNF8KY8q8viKGY_Pw4m_ECrqf_-Uq7l2jl6TTddPmWHlDHBvOO9iwXJTSo6dRRps_5bFcTnG4DzP0-6QT8xtXsehjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت : ۱۰ سوخترسان و یک هواپیمای آواکس هم اکنون در منطقه، چهار سوخترسان از تل آویو بلند شده و به سمت منطقه خلیج فارس میاید.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16986" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه های رژیم : رهگیری و انهدام دو موشک کروز در آسمان بوشهر توسط پدافند ایران
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16985" target="_blank">📅 00:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای انفجار کنگان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16984" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چند سوخت رسان جدید آمریکایی  از تل آویو بلند شدن ، امشب شب دراززززززه و قلندر بیدار
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16983" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16982" target="_blank">📅 00:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16981" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16980" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستانی که نمیتونن جوین بشن، این پست رو سیو کنن، فردا عضو بشن یا با یک VPN دیگه امتحان کنن. جریانش رو قبلاً برای بچه ها در وویس گفتم، به خاطر امنیت شما و چنل هست. من از شماره ایران استفاده نکردم و محدودیت عضو میخوریم
🥹
🙌🏾</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16979" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارشات رسانه های رژیم از کشته شدن چندتن از نیروهای سپاه پاسداران در چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16978" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsbVSyqihdiM2U-osAgWEZn7COQ5hnUH-ZEGHDfCIATbqkH21EAvVEnEhbBEzDdyfJGm0EJ3j3_Bk6cCZSJrz_jE-zRxVfzujt6NoQlBIt-7QR-s0f9HIbYNHy1R-KTZXKY3Jbh955gWfsIadtLEmwzfUGIFQRMCLQU4e1cigDi7H2ba6NSgRFB9Ca9xksNLuwr1tIOI6B8j9iY35gWKe1jt6fAkUXN1pv0lTTONDOsXOD83NqFSARLwfhKwH7wiviQ6Zadp8329WdwwSS26UQZofFrYUK9ZPIN05aKh72CTG551NxyGDk8OgYRvzLJIEzTXf-DhuXy3ZHeJoW12yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16977" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اطراف بندرلنگه چهار انفجار
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16976" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACaqeVdkXfXtW0272UOLWsAQ9FirjJMz4kYqM5OE5I2PEshF-DibBPgcwvnoMsL_B_GluHAo9yDkNXeamUgA8hfYbZuuvyBliEEL3bpZscdqpEbJoWuLGhmRJ-ExTlEFhlzyxUGWd_hspQ0ww1ezsf3Si_1SqLOI-k7phr979fEzfiwIBVCB-Qg8PW4AsV1240v8IEmvvwKCwvFmvmDAstFLbiiQ06-bV8FgwjW3Fc5CK-EBBWAPlGz2nTOFPBGGR-trKkUxMnFylDc5wPCpf8AWXOgl3VU-5rK-KmaryhCL6AFizZ0R_4AUs2O0tgva-xvNmK9gBrf4eHh5zccUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16975" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tebLZDkg4J-q1J2zhykDpqevqzwsWJ_G1dkjTWrHVhNhyCtCjmQj27Pyuovdlo1-H6bUm9GEtJf_sRmSgW-4CuspLMbOSzBOwLoSiZc4_t-7GycBVhRPdRGYtkgBeAbleadrvAEomK-yXoEMIflO51loRTfjqTjHTN7gXf_pUr7rxAf25T8BdQN9V0LIuKPsXvNPUgzwbZxrAn0SIoBjnWkE4aDenXRPqneGUuJYxjtpfC16NbvZnx3mKrMSl_1_Lrhol4aQy0YrlAKnWN_3f66FNdRDyP2AUaqF6CX81cykatbaWkNc2EcUPgnAr4u5WbiKiR5061OM-2AQv1P6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16974" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صدای انفجار در‌ جاسک
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16973" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوموسی
‎
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16972" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار صدا و سیما:
در پی حمله آمریکا به مناطقی از بندر چابهار، ترکش‌هایی از این پرتابه‌ها به بیمارستان امام علی این شهر اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16971" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=aiOjJ6_5vTAtZTErXzz5KhH1umbKIoms-6nRTcwZJDWJHx3bCsrdsDLApzFJIX50GWkd-DSpBTQ_XJdtd0C2Yq3pK4E1f4aGzJemtuBaO7-Xnw04n4XD4KeQaVYPyjUGWPffC8mqQISwQkPek1KmFEz3tCeShGclwlXniwqRRaKA-wutDda5SSocSiBOUT7UF1oBt8mTQKPYGASJVN7yqWc84pQNHRa1A3IIWUEu7eKHGe8BpqU_UMUltplRWpvZPuI0GsSxOn7sIRPLaOW0982rkRvzUYqkTgKXx6xvWxwTwp1z3DiFM4rrMqI8MM2bZrRevKLj_J79tOjhaj3RQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=aiOjJ6_5vTAtZTErXzz5KhH1umbKIoms-6nRTcwZJDWJHx3bCsrdsDLApzFJIX50GWkd-DSpBTQ_XJdtd0C2Yq3pK4E1f4aGzJemtuBaO7-Xnw04n4XD4KeQaVYPyjUGWPffC8mqQISwQkPek1KmFEz3tCeShGclwlXniwqRRaKA-wutDda5SSocSiBOUT7UF1oBt8mTQKPYGASJVN7yqWc84pQNHRa1A3IIWUEu7eKHGe8BpqU_UMUltplRWpvZPuI0GsSxOn7sIRPLaOW0982rkRvzUYqkTgKXx6xvWxwTwp1z3DiFM4rrMqI8MM2bZrRevKLj_J79tOjhaj3RQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16970" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=b3LZhnKOzTH7CkdGNQ0FHQe3qpKGeFfL62vHZF-2lmRIEUhaK7SDT5CnqkURVKU_kOuHHQGZ9wjZ4l0KA-vx-NG0RyXQnligeVMvHIzBJQNt9yqj4ygn2A1yOK2fta_RNB_a6nhdKRwAggkcCCCQtXAJtkqb5ghpTV94hkKL_Fxa9HahHQRtTj3mH0miiqeuZ3mkgl3QpDJq_NLki0PW3CHYnMYhx149MJo04CMdPa0ph_9Z6a1ZRNIJWK77njJEZ4jxpMPoCAYPD995v2jeMH7CzRLnNaeN0ajuM0jAZMvl-hlOuVx0jOl9sHFe8Xa20xC_4EjKX_iSLKjWF2yuSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=b3LZhnKOzTH7CkdGNQ0FHQe3qpKGeFfL62vHZF-2lmRIEUhaK7SDT5CnqkURVKU_kOuHHQGZ9wjZ4l0KA-vx-NG0RyXQnligeVMvHIzBJQNt9yqj4ygn2A1yOK2fta_RNB_a6nhdKRwAggkcCCCQtXAJtkqb5ghpTV94hkKL_Fxa9HahHQRtTj3mH0miiqeuZ3mkgl3QpDJq_NLki0PW3CHYnMYhx149MJo04CMdPa0ph_9Z6a1ZRNIJWK77njJEZ4jxpMPoCAYPD995v2jeMH7CzRLnNaeN0ajuM0jAZMvl-hlOuVx0jOl9sHFe8Xa20xC_4EjKX_iSLKjWF2yuSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16969" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=Q9sF0NsP1KmBHtcL2xQdClZzSMRkQeIb3b7DreUbxldw8u3NohOOxdulMCfnvdJ1gfSYpbPWdZJA-hLwYRjXby8Wk32rtiCYyXfBKQxlpKgeoWDGMYIjlJ6kEPeOPUSpUKZl1rduAq2Bt0qEyKxMOYoKOBE41yJZ1kGi9EmFuy1S5T1wmL0jYR2dyjR5Vbwh-y9GH8gM8czyZDqGwc1EN1gLr54y40yeW7-LEA1HQ00YZ3jzCXoPyQP1EXkHz4-YrpmOn6tbkWMw5Ndx3Z2qTMMGi6T_yz-vs0iLIERUxPyPnCsqcyoZgeS0Pmr6LbwuFaFBhTiKjlw_MUzg7stSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=Q9sF0NsP1KmBHtcL2xQdClZzSMRkQeIb3b7DreUbxldw8u3NohOOxdulMCfnvdJ1gfSYpbPWdZJA-hLwYRjXby8Wk32rtiCYyXfBKQxlpKgeoWDGMYIjlJ6kEPeOPUSpUKZl1rduAq2Bt0qEyKxMOYoKOBE41yJZ1kGi9EmFuy1S5T1wmL0jYR2dyjR5Vbwh-y9GH8gM8czyZDqGwc1EN1gLr54y40yeW7-LEA1HQ00YZ3jzCXoPyQP1EXkHz4-YrpmOn6tbkWMw5Ndx3Z2qTMMGi6T_yz-vs0iLIERUxPyPnCsqcyoZgeS0Pmr6LbwuFaFBhTiKjlw_MUzg7stSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به اسکله شهید کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16968" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش انفجار بندر جاسک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16967" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGhPazTTFrQISKxsMsKnmSlATEJfNadlL4CkiclLwfOdPaUevFsbzXgboB7dE2ZXumYum80CMKhvyJzIalUcaTL5ZjRYqc-JUZ4Z_gNIRxE4g0sHbQFIJvvCoUlkPy7nyDVYiU6wBvNs0bTjCKmqCQpkMLXtUlDVHpzrtBODb7cpVHo95Xn30G7ccj7wpqv5E37ZyZqM0pEQgL4dqTDG_7Nlg_jRBA9wPZ1PGyHutStwnEmW9PgQA6pwdHCawvAJYHRKf1ybLxV6v0sskoRQu64Wi8eAgNoNzvBw9GQkYOMfqGUTkUoWqev583AfSy_m8HNdiVS5E49zRDpobbgGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icVIC4BfcasNrq4mvvjJr7OfcBlE8CZvac2n2kbkOR4iaaA9NsX9QkSmFGIM1bbQALzJJktxs2MBbfzQzVnl8q3eWaXGHZIrVKT7dboB-J3YqjO73azLlnyAWdP2ycDZBbGJy0LStqx109ZR8uMwV2ghxYTYXTk2xqBN6UhLvVpzFy71XV0aLsAqEcFLBwJDttO4qiqCxvU25syvDijGBXBXxfAKmEiAHx4W80Ym5_V1bVvZIFbqaAojKBLskr2AuksE1d6hDg9W2TOz6D7mMU2ej4g05HQ7_M261KozSGdH5E9wJOXAp2K0uv1rDt7ZwfdgqW0TYINmNErU4Z_83g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16965" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های رژیم :  شروع حملات موشکی ایران به مواضع امریکا
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16964" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlqbhJ8dPaEzHsYkS5x2PWInJI7HjPnPdBzcJOfArEljRWfoDHPNKYDpuLhuczEeaa9Sjl0ekQ4TkSWRhe2T5qBN-sPovcOEpU-rQqUdMRGZ4IreRn2Y5lqGvckz8_DJ7UXezfouusS-RJOhsD5S5G-DNfFr9LFK1QJWmY2EG3cenazgvq2jUw3aXEGF-56T9MtipndnIYrqUVzu9HT0fP0nMhpJ2c2EVcIGIp6M6VhKNzoW0qvz4dE4gVCnd72bkfz4M5EKPar5ZPpu7YnzSA68bfT_Yb-PgNC6ysLFKVPBeWKhcMyZ0ArphFu0Xyvz2mkU3RYtis88Od1688_RTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16963" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=YdUmnZlsXFusG0dgEpfwdFOK9YBtwW1IZODF2BD6FqROcOMCLTWCf93WpKG0a2JZxgmWIDNlMJrA9mBkOKqQgr9SP__4dXyckD2XfdClOm2PSZtPp8HHxnFU4nJGEfmzdiva5gwl-fJ5CbCYHDozvQDeZ5tCyRGL4Ayh5GabX-hPO6ZYBPfSho767lQ_HN8PLX5q0_u7_2U74-6iEUKTwdYjmcqEQGpOxJyWuSGQbn6LVpjeVsBuQr8y6JspUB8F5VqI-SoUfhAq1_UQVIlRhQgSFRYB2Wumj4khTMa_UvP8GIohN-S5ymoLSbmav8FDly5hSXzAYHmIj6lV1jXVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=YdUmnZlsXFusG0dgEpfwdFOK9YBtwW1IZODF2BD6FqROcOMCLTWCf93WpKG0a2JZxgmWIDNlMJrA9mBkOKqQgr9SP__4dXyckD2XfdClOm2PSZtPp8HHxnFU4nJGEfmzdiva5gwl-fJ5CbCYHDozvQDeZ5tCyRGL4Ayh5GabX-hPO6ZYBPfSho767lQ_HN8PLX5q0_u7_2U74-6iEUKTwdYjmcqEQGpOxJyWuSGQbn6LVpjeVsBuQr8y6JspUB8F5VqI-SoUfhAq1_UQVIlRhQgSFRYB2Wumj4khTMa_UvP8GIohN-S5ymoLSbmav8FDly5hSXzAYHmIj6lV1jXVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16962" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=PNQ1yeiNXhnsHSxgRyIcbkQJapOy16p7l_7VBG478W7yHvthqh9bgRPU2ZeO3c4Mq76s8JORZBEHI5d2h-2JtXIXFSGh-6qUBBa26vz_cUxwpDylGbFcNGI3uxx6BYHeQFrvoaDVhKPhcvEuOy3R5ztlF9MC1ABkD5gwCs5S3lbkFGx5KBSlnoHN5EsCTGXSSW-o1SiQThZEDJovYOvYQejsoxiaVk_YoCf6iqt_lQtqzvYA4xnGspOs_qxLXewP03dV_xgCvA2KZRMNuBYBC0846ZIndEK0VsSF8L6TpuI7gemP_pSqFBL0N0nhYWC8oUcoQe1BPhtOXVb3BESzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=PNQ1yeiNXhnsHSxgRyIcbkQJapOy16p7l_7VBG478W7yHvthqh9bgRPU2ZeO3c4Mq76s8JORZBEHI5d2h-2JtXIXFSGh-6qUBBa26vz_cUxwpDylGbFcNGI3uxx6BYHeQFrvoaDVhKPhcvEuOy3R5ztlF9MC1ABkD5gwCs5S3lbkFGx5KBSlnoHN5EsCTGXSSW-o1SiQThZEDJovYOvYQejsoxiaVk_YoCf6iqt_lQtqzvYA4xnGspOs_qxLXewP03dV_xgCvA2KZRMNuBYBC0846ZIndEK0VsSF8L6TpuI7gemP_pSqFBL0N0nhYWC8oUcoQe1BPhtOXVb3BESzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16961" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hay8NV4TVVipOpvkc0219E8FBk37f8GuDhdE3OjgGoq1Gm1BBIS-yltDOpTuXFqXX4-RdtPSUFG6RwUsIJnocvpIb_oXKpxZ79XOKXyKwSdt75YopguA8wOU-dX91NPT2VABlgB3R6-XefxF3dS-m08MJN5cjfrNJUwXrNw3OfnoywlVj0MyapZEv6LVbiKt4zD-nR_ZkCiXpG7MHHPRS_4OQBgvLBvG7fYBwPyKXPN48pSaCcxCm7w1n1XdtNETng0MNkbQBf2yLZ4bqtmp6PyVTRbCQuOTpz31USCguUBR5gmrpnUfzzatylF5frVLEGFsRliajL7HvvWVZMdrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی سازی سمت اسکله باهنر بندرعباس رو دارن میزنن
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16960" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16959" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرودگاه بندر چابهار مورد هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16958" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=YZ57Rh6Kco0rHmyaBMHh2Mm6RN5cPQL-KohaybN6Zgoe1twOJK6-fdNNwtu71oQpHZw1ySQ8IDKaS_rdYZ26DhGvkmqw7l3o0uAJyhzkYrcYflqR0tLntMnXsja_74DMVmEimyNTk0hpKXxOQ5q8OB_Sn1xWthEzy_t14bwe_IFPx7v9agBJJ0WZtMS9JM1xEH_cAlz8CemdIn01eWoOmSinNUx2gBy8rJzoYoMuvsLklh8Js9g8uO82ysaxZfDvdmDbDOg9bam_pDuX3Ntl6eOFhZifVBFG4z2461AOQEJCP2SQIm1Lq7HRjjBA8S7XCBoOXwSnLMmkz1ZhwHsy2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=YZ57Rh6Kco0rHmyaBMHh2Mm6RN5cPQL-KohaybN6Zgoe1twOJK6-fdNNwtu71oQpHZw1ySQ8IDKaS_rdYZ26DhGvkmqw7l3o0uAJyhzkYrcYflqR0tLntMnXsja_74DMVmEimyNTk0hpKXxOQ5q8OB_Sn1xWthEzy_t14bwe_IFPx7v9agBJJ0WZtMS9JM1xEH_cAlz8CemdIn01eWoOmSinNUx2gBy8rJzoYoMuvsLklh8Js9g8uO82ysaxZfDvdmDbDOg9bam_pDuX3Ntl6eOFhZifVBFG4z2461AOQEJCP2SQIm1Lq7HRjjBA8S7XCBoOXwSnLMmkz1ZhwHsy2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16957" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16956" target="_blank">📅 00:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدای ‌جنگنده در‌آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16955" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۶ انفجار سیریک
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16954" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16953" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش
بیش از ۲۰ انفجار در چابهار و امتداد ساحل
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16952" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9xyqqxGkrzjfDdvNX2QlJPdIk3UKyH1K8rQ_OeODT_9wVs4DQIdzIHXpCnebsLo-DV_ifJaQRMQbIKrwjHBRc_EUG5uw4QxSvSS9NqX6C39QYbTpnjym3O6pzDhGpyBkVY8Yt_7r2dzKquxIv356WMeGAGky-UL48cjTkkhpzz24EeiPtsmPpBK4xc3LW7x-HRj2ZMKVV-l-8RRxU9txjn6k9vEopXoBq7lCBhqTaaFIly24SBEgAIhvQdSK_EvbJuP9KHtRauEJyq7arNAP8vTwbX8tdOi7oVHqjyk8J_44L1iaLjAzuvf20Ilr6kSqL_IMc1oIGoecq-5ZRFGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16951" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vizTIZdaFhy_kUYkaje0ONkw4akiyG5AxlqMzMk02R792PRgzWD5ddcamRd3QEjdLxRwW5lwuDmnIqQ8I_MZsGEnimqB8eyVfT4Ugbmox__AxSGFXLTGHE2Bnf3iQmuRRYKNB5MCSLjVZm766iIyb3YO9uWB4SSHpeiejAHQMXhkBJIV1Q6ZoktBrlPyxAX6M57mGPKA5wFxlJELXP7qOKDI90et_W7W7547y6ZMo6d0d6GqGx_SfTQciXL5ZUGx9u3MwsZJ1jLULHHffXm0sihwrzNI4nHO1Y3SxFcxAwTOWZ27R8qiaeAx64P8AIrHyox4HZZ9OPqgbQOiIoWiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام: به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16950" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دو انفجار الان بوشهر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16949" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش انفجار‌ از‌ بوشهر و خارک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16948" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeYwuCfC_6RuJIE0QXgfwFWXRnoJqwWCCL-aPUpNbOnWerQwsq2jtZ5bhi3-cTrTzF77WNNnLNdDHh90bEyg9-33svIByejn30GaTrOlZs_xHjQsrY8GspFgWZIrQvBmNVRsHujHAOI9B-Qi2T6EbPUpeZ_dVPyJrK07hnCEKfXrK3v6bYaRC6_HWitgFDX4hmqD1UdjVvLC6rFZibmBUt-PPXk456t-N_wu3HdsyB6qVkNcxIqVDBH9PrvO78jQTzi64T5YNbxz5cnSOCtNjlL-eafofi_pDO6xgU1-3xeSEMN9TgyBISmMGXCEwFify-DjEfjJo6uKgCTb1N2vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله چابهار الان
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16947" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش پالایشگاه لاوان رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16946" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بندر عباس دوباره زددددد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16945" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=FtRb0NBp3HlmTWMSLJJVEE6FdA024GHSelYvgVFX6a2goizA7cITKujS407ibn-u6tgMGVnk-g1SfRbpbrm2_cfunuV7sLgOQUZn8EKHRiue6wtIZstcNe98nueQvECYitqOCj1VWT8PCivj2NCkx2YfX4gtnXolfU74oIZ9Xw2D30hsj_HO3br4-0osxnRCyDIY8e5Kkl0j9_f7kwyN-8zzjNpTuv3gKiu-MLQzsnWIzuQkGQWWRgbtVCaRQfPcERrykXZDxauF2R2IAAsMMhdcaBU2Dh7zSAjyWz6N6ENSdMIuJ3b5AS-8LxDRD9eK2vZA600-OUwptgMhUFWqCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=FtRb0NBp3HlmTWMSLJJVEE6FdA024GHSelYvgVFX6a2goizA7cITKujS407ibn-u6tgMGVnk-g1SfRbpbrm2_cfunuV7sLgOQUZn8EKHRiue6wtIZstcNe98nueQvECYitqOCj1VWT8PCivj2NCkx2YfX4gtnXolfU74oIZ9Xw2D30hsj_HO3br4-0osxnRCyDIY8e5Kkl0j9_f7kwyN-8zzjNpTuv3gKiu-MLQzsnWIzuQkGQWWRgbtVCaRQfPcERrykXZDxauF2R2IAAsMMhdcaBU2Dh7zSAjyWz6N6ENSdMIuJ3b5AS-8LxDRD9eK2vZA600-OUwptgMhUFWqCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فیلم چابهار گویا پایگاه امام علی بوده
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16944" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش انفجار‌‌ پادگان ارتش در‌کنارک
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16943" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16942" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش انفجار لا‌وان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16941" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۳ انفجار دیگه چابهار / اسکله چابهار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16940" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار بندر کنارک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16939" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16938" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۳ انفجار چابهار
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16937" target="_blank">📅 23:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چابهار رو زددددد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16936" target="_blank">📅 23:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16935" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منابع محلی از مقابله پدافند هوایی با یک پهپاد متخاصم در آسمان جنوب کشور خبر می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16934" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک پایگاه دریایی سپاه پاسداران در سیریک مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16933" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدای جنگنده ها  در نوار ساحلی خلیج فارس به سمت ایران شنیده میشود</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16932" target="_blank">📅 23:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارشات از تحرکات موشکی سپاه در مناطقی از کشور</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16931" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش انفجار‌ سیریک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16930" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پدافند درگیر شددددد</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16929" target="_blank">📅 23:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جنگ بندر‌عباس با آمریکا شروع شد
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@wirhyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16928" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه دونه دیگه بندرررر عباسسسس دومیش‌
🚨
🚨
🚨
🚨
💥
💥
💥
💥
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16927" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش انفجار‌ بندرعباس
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16926" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زددددددد</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16925" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال استریت ژورنال: دولت ترامپ و عراق به توافقی برای تشدید کنترل‌های مالی با هدف جلوگیری از رسیدن دلار آمریکا به ایران و شبه‌نظامیان تحت حمایت تهران دست یافته‌اند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16924" target="_blank">📅 23:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقامات ارشد آمریکایی به CNN: حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16923" target="_blank">📅 22:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز: قیمت قراردادهای آتی نفت برنت با افزایش 5.2 درصدی، در پایان معاملات به 78.02 دلار به ازای هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16922" target="_blank">📅 22:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ونس معاون رئیس‌جمهور آمریکا: عملیات نظامی آمریکا ادامه خواهد داشت، مگر اینکه ايران از شلیک به کشتی‌ها دست بردارد.
@withyashat</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16921" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگه با روال همیشگی پیش بریم مهمونی باید دقیقا حدود ۳ ساعت دیگه شروع بشه بچه ها دارن میان کم کم و حضور ۲ هواپیما p8 poseidon  هم دلبری میکنه @withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16920" target="_blank">📅 22:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16919" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obj6VCVNldX04o62HXA_X01T2vWN4XZzq1chFah7dc0hbZhPFZ8w9J4Oc6onExeB3The-KgZI9QoCvQYVS46Qmpot_bBF2i-2ebFSqWZxbeufmOOQYAzBvtTQ6I_FkOTMaTusndxZz4QrR2iPVh1SDLsZPlcF6kp7wJ0ASOLs9JI15ZB8LhcPJr33eQiSykLQZb2YPRj5TXZQGdXYhzVHtLdw75AsEfH6O7fSa7tlqJK9G9SlhW5amz2EBloHLkC6qsVE1RsnDjEByHU1_wQcK9A2PojqceH7Q4Wc9GBAbQRvFpWKSJs0qEu-oySdLQa86UZueo6ILGcjJq8xauxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صیادان امید عربی و مرتضی هرمزی که در پی حمله ارتش آمریکا به اسکله ماهیگیری بندرعباس به شهادت رسیدند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16918" target="_blank">📅 22:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">درگیری در منطقه‌ی سردست و کشته شدن یک پاسدار
یوسف محمدی ازپاسداران تیپ ۳۶انصارالمهدی زنجان دردرگیری با مهاجم‌ها درمنطقه سردشت کشته شد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16917" target="_blank">📅 22:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر خارجه آمریکا: رئیس‌جمهور ترامپ امروز به کنگره اطلاع داد که دولت او قصد دارد طبقه‌بندی سوريه را به عنوان کشوری حامی تروریسم لغو کند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16916" target="_blank">📅 22:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9720f86d.mp4?token=KabeapQYQFm3tPXLk8UXhKJlX_h-cfmrT9xMNhjW1_GVrqAOWhVzb6qS7I3ncLBhg7aJh0OuP3INFxK78R2_RpvhME-aBWtME39fjHRigFoXqwbDRLjdDmt0gectTwkZDMhWl8lFlK24ueP_TutBYbLyph8D8Of0b88fFY0h1dFl4hL6EUuz31YnRDpVU4F-v-DVmME6X1xsBVvbG70rNyCtgTCRLnUKuUMIayzBEaGguyIq7PH8T-vbcUAvwMsiSBmeRuZWADKH7HMm1BxB4maQ321YDvLYaC_cjil844rngh4Glf7fQ0gE_4L-I8fr4LdO0jtyUYa1ncBLKs6gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9720f86d.mp4?token=KabeapQYQFm3tPXLk8UXhKJlX_h-cfmrT9xMNhjW1_GVrqAOWhVzb6qS7I3ncLBhg7aJh0OuP3INFxK78R2_RpvhME-aBWtME39fjHRigFoXqwbDRLjdDmt0gectTwkZDMhWl8lFlK24ueP_TutBYbLyph8D8Of0b88fFY0h1dFl4hL6EUuz31YnRDpVU4F-v-DVmME6X1xsBVvbG70rNyCtgTCRLnUKuUMIayzBEaGguyIq7PH8T-vbcUAvwMsiSBmeRuZWADKH7HMm1BxB4maQ321YDvLYaC_cjil844rngh4Glf7fQ0gE_4L-I8fr4LdO0jtyUYa1ncBLKs6gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16915" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16914">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN5ggsCncPTkn_NsbShe8ZjgqtfioNtoMgTR2rAOO022skB4y0IHarpq9NpR3AkJiHl6IZ7scWxq3JfvhXVVY3Qd76BZ5nN9XpJr4OZoTAUtkQt7MNhU3vAndYtD3bEo3zt5jEKfwSlOK1cfST0XxV5WLKC8OfKLh-aCC6HG9l0wCMf4DqvYBLGQ3yVAT9IjrX5mEg4J5GUEo7z41osTHG6ZrBIqFDNqnlhpYHwYokW5TkadBwHuBWfzgLyoLZ61uiwI_j_cVQD3gXCz96RO-x1SSU38xfNuIFB7GrjE0XoKkQK6RVN-Gl8BjAjscQ0L7hQqMFv3_KoIczzHIqq7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با روال همیشگی پیش بریم مهمونی باید دقیقا حدود ۳ ساعت دیگه شروع بشه
بچه ها دارن میان کم کم و حضور ۲ هواپیما p8 poseidon  هم دلبری میکنه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16914" target="_blank">📅 21:31 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
