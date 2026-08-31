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
<img src="https://cdn4.telesco.pe/file/QH-zbGjjcljjsEvscO7RIcOD2BEuiev61JdkBIC55Rju-gozCDcJSxmzyxJ1k6PEKJYN50WcW-T0PVFpyZgByBfjQFTDFUdJyfDV97SMHVloOVx_xrYbLuzM6SgisUMQlUq-bKtEQJ5qlPLV3M4ciGO2ofTSdxqVzbWcNXuSdNAza36UIwC1dpFEb4IEzqN6AYmp6afnsli3w64G72UcNzXQQxgYUCe-hmoHBfKRuNR4NCDtDG09aSnqE_clHIBPO2ocoW8iTbwZfEewD1XIeqfJIdP6nKm8BJajOqSa5p7RjGz4pXt2gxzova-k3MtVAexrlnztXlFd3onkPXVumQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 441K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-21803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNWMKyyFXBiI9ehewt6GD2i9iJGExxZzM67B-oChq-oQmKePtgltwD_l8ZMs9SW_YLiijIr8JTtlfq6apJusy0fwS-VF1ZF0351vm6LDFRWOIbvBQBbXUN9-uFYfXhwK05FVHBcSq82LG18lmAdHNA1BhkdnT6Jh4pRIbPqwCJbN46WbCVuuYyIfIKzGHWvtuWx6A_xZJdOeMGN29e0jvR1Wdi8FEOtEb5v31e9Nch9CgvKcbGA6JSEdz2uShQuHZnAv8tQ84jFew2YqBouyW3V-ikqN0Xpj3TuaVQVxFkn2bRxLHdlI8Oi88FI1MzRj9-q6c4ac_JyrqPmzePPl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاظر بر خلاف رسانههای رژیم که گفتمد هواپیما های امریکایی از منطقه فرار کردند،  ۴ سوخترسان که همه آنها از قطر بلند شده‌اند، مشغول عملیات بر روی تنگه هرمز هستند و یک سوخترسان هم از اسرائیل به سمت خلیج فارس در حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/withyashar/21803" target="_blank">📅 03:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/21802" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCU-RgBbEMzMkLWhue82Y7279009mClgfFrW6nQXMWC5fN69JgSzRx5ESjNpzaf7TGZp2VuH8aZONSNB0h8bGtcMSdZRo3J6sp12A8t_sXKaq6nY1_fFYNX1gG3PKqzpLotbhsIu_vKXvcFWPy-BQgTK2q4RaAdQ2xZGZ-cS_33aEsWQYbwh4yNb5am3FrAoYutBJrMe-TB7A6uSdlDQDA91Tv3yhDqfXX8oRjU3sfs5YBn2wjlmEzguJ2r2bIHQ3QtOJfv-GAunpN_Retg4uqUVD5wRwqlIrM-x5Fb4DgRAMlTnREe0zWoyHFgVK2XCC27P71j0bNf1lPqdoJmZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز فلای‌کیش‌که از مهراباد داره میاد امام ! آیا دارن تخلیه میکنند مهرآبادو ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/21801" target="_blank">📅 03:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای‌انفجار از تنگه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/21800" target="_blank">📅 03:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش اردن در بیانیه‌ای ادعا کرد که ۸ موشک را پس از نفوذ به حریم هوایی این کشور رهگیری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/21799" target="_blank">📅 03:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال 14 اسرائیل : تو حمله هوایی آمریکا به لارک ایران ده‌ها نفر از پرسنل سپاه پاسداران کشته و حدود ۱۰۰ نفر دیگه هم زخمی شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/21798" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/21797" target="_blank">📅 02:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLS0q2pOO_gFzkiGP9mRj4VV-gmxHgpAAMAl_lLza40K8rCR6ZfCwC_1n0iWgY1nfTI9BJ80SlzBGGp1J9xfpfsxga-KGzkbjx0vIgKc928bD6ZJQmrWOFrI0Y2Dp5aZnPmewnyTakqV7FKK3k0RRjvF4AEPv3fg6HyvP7_y9uGWCUquUJnGm8N2bUJ-pHXVAb2oasUaloyxrfHn0ycyWE2WbQlg89PhhsI3-ITCqHkn-vq1JLGEx8HV8vpOJr4UDxzi7D9zqpoOBgeRMbKuVqW2yaGDKV-QKqAJiMivKbayKzUxVX_jMzXe_v6zWbBRdvNazjSfUOKBMaiOVNcUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/21796" target="_blank">📅 02:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فردا ملت همیشه در صف ، در پمپ بنزین و صرافی ها ! قیامت می کنند
@WarRoom</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/21795" target="_blank">📅 02:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی سپاه با این ویدیو تایید کرد فقط اردن رو زده و نام عملیات امشب تنبیه متجاوز بوده
@WarRoom</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/21793" target="_blank">📅 02:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چنل‌تلگرام رو پین کنید بالا حتما و نتفیکیشن های اینستاگرام رو هم روشن کنید کاملا ، چنل یوتبوب رو ساب کنید این هفته هر جور شده استارت میزنم   https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/21792" target="_blank">📅 02:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک منبع آمریکایی به فاکس نیوز گفت:
تاکنون تأثیرات جدی‌ای مشاهده نشده است. تقریباً تمام موشک‌های شلیک‌شده تا این لحظه مورد هدف قرار گرفته و منهدم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/21791" target="_blank">📅 02:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/21790" target="_blank">📅 02:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/21789" target="_blank">📅 02:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/21788" target="_blank">📅 02:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خسته باشم ویس میدم تو دایرکت نده تو مخی</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/21787" target="_blank">📅 02:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/21786" target="_blank">📅 02:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/21785" target="_blank">📅 02:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/21784" target="_blank">📅 02:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/21783" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امارات هیچ خیری نیست
😃</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/21782" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادمین های فیک نیوز تلگرام کل کشور های حوزه خلیج فارس را با خاک یکسان کردند
😂
😂
😂
@WarRoom</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/21780" target="_blank">📅 02:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مقام ارشد آمریکایی به فاکس نیوز :
تمام‌ موشک‌های شلیک شده رو رهگیری کردیم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/21779" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدا و سیما : داریم پاسخ میدیم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/21778" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پایگاه العدید قطر هم مورد حمله موشکی قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/21777" target="_blank">📅 01:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/21776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/21776" target="_blank">📅 01:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار در قطر
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/21775" target="_blank">📅 01:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تتر ۲۰۸.۰۰۰ تومان (رکورد تاریخی)
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/21774" target="_blank">📅 01:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">@WarRoom
جنگ مادر شوهری</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/21773" target="_blank">📅 01:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d2a6238.mp4?token=JQRTaAunttjuMQdKUkZ-xNuM3aeskWzLNV3NIvyghwAADujVtKmY8AUUmMyybYXDZ9V-lFCuM2uHiXBSZU7t6HdHFXQy3yLTFlF6qMy88hbdAgo_ff2VBnFgk3OQw_YaSGKeVws-_dvZQCvF1aEqeNhI5f89B-SzOV5E4LNRe9soW44dAYXWSLc89iMOp1JIQ8r1DbPdLiAvcAlo34kAvBGGaIDgXig9bc0yRZk1Cw7KWCkBihcd0ENGnM5RcKMXdLR7y5_MIk86En1SFGXCd2RQBnyCw-OPGbBPKPbcN6vquFSgXt-ebL6iFfSR2a_XrPusxoc0LoC-F9liBMCxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d2a6238.mp4?token=JQRTaAunttjuMQdKUkZ-xNuM3aeskWzLNV3NIvyghwAADujVtKmY8AUUmMyybYXDZ9V-lFCuM2uHiXBSZU7t6HdHFXQy3yLTFlF6qMy88hbdAgo_ff2VBnFgk3OQw_YaSGKeVws-_dvZQCvF1aEqeNhI5f89B-SzOV5E4LNRe9soW44dAYXWSLc89iMOp1JIQ8r1DbPdLiAvcAlo34kAvBGGaIDgXig9bc0yRZk1Cw7KWCkBihcd0ENGnM5RcKMXdLR7y5_MIk86En1SFGXCd2RQBnyCw-OPGbBPKPbcN6vquFSgXt-ebL6iFfSR2a_XrPusxoc0LoC-F9liBMCxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/21772" target="_blank">📅 01:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=Nr7MGeaheWR7kViEhZE8RYCTXh1-T2yq45W-ruMnbXGsvxZ7tn4VWuLXVYcGCiKQoWbaNgG2WB8e6A7TFuHHRqnTAVY81kdooTB5jHGyK0JuYoaZnXi62pdQ4XiXigfJiPzKTHoyWMKSrCM9sXT7iEPYy3PDze7TkEyCPymdeX-E7LBGppNBD9IGvHRF_HXwkHyozPjubtE2vEfeoWDlj5uYtfUI8zZuVlEf2NxPs5DKF8_V1EjHGA0uE_e_U4O-gfM7Hxl9kFxi2wRGiK-4MdOQAJ_YQzkApL4wgAOt5X6MzpxdQe40M5BvjFgVe58nv8nkTEOXornL-o0-9nXXbbTT19xBEesLWi6V5lMq_mhlQEM4qWnp-DkDrOoS5kQ6aI6SO9tuNgepCAy0Zfd4KV60tgpSuRzim1JZAUPbq_jRHFG6O_ht_-hluApB31L2ae9nj0M-CKnF4r5quqvVQUceRvW48a-uZRhnqqik2Tv6_QnvduhJVnXtQ2qw6CPu9gzUfSnaZFXnyw3Ql4T_oJ6Gp1uMhm7s3hEVsMy2vxw2DBifFfwpPtOIbw6zqCXb8uo0Sq2pSjhI0fKTUkfpzZSdlD3THS64c7fABEfI2JGXdf0SPqk4CWXbq54nol4MJ9AkYKsLHkxM06-IXVkKPM0kXrFY7q9bX7Bc7V5yLQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=Nr7MGeaheWR7kViEhZE8RYCTXh1-T2yq45W-ruMnbXGsvxZ7tn4VWuLXVYcGCiKQoWbaNgG2WB8e6A7TFuHHRqnTAVY81kdooTB5jHGyK0JuYoaZnXi62pdQ4XiXigfJiPzKTHoyWMKSrCM9sXT7iEPYy3PDze7TkEyCPymdeX-E7LBGppNBD9IGvHRF_HXwkHyozPjubtE2vEfeoWDlj5uYtfUI8zZuVlEf2NxPs5DKF8_V1EjHGA0uE_e_U4O-gfM7Hxl9kFxi2wRGiK-4MdOQAJ_YQzkApL4wgAOt5X6MzpxdQe40M5BvjFgVe58nv8nkTEOXornL-o0-9nXXbbTT19xBEesLWi6V5lMq_mhlQEM4qWnp-DkDrOoS5kQ6aI6SO9tuNgepCAy0Zfd4KV60tgpSuRzim1JZAUPbq_jRHFG6O_ht_-hluApB31L2ae9nj0M-CKnF4r5quqvVQUceRvW48a-uZRhnqqik2Tv6_QnvduhJVnXtQ2qw6CPu9gzUfSnaZFXnyw3Ql4T_oJ6Gp1uMhm7s3hEVsMy2vxw2DBifFfwpPtOIbw6zqCXb8uo0Sq2pSjhI0fKTUkfpzZSdlD3THS64c7fABEfI2JGXdf0SPqk4CWXbq54nol4MJ9AkYKsLHkxM06-IXVkKPM0kXrFY7q9bX7Bc7V5yLQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگه بابا جنگه !!!
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/21771" target="_blank">📅 01:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a23e19932.mp4?token=BPe5vDHI7AvDIk7HzZyQj79BV1TEQA-20k6DGSNWDSGIpXazimwKwS5OO2aUxLBBnjgp5TKZBJ2ZfYCHBmHf2QXgsrEwa-zV4N09EcWiov0CxGvrmb6SYBdwHAeTqEmvCR7MSxSquXOjFPR2nMw82X0CreRz5HH_1S6KqJ_5BlUdHvJv2fXBWl60VGj3ltVXEBdDLKeX6TmpHrbYJRgXs05Ax5bdR4himGeR9CVp5Rw-ejGwwOhyNQujbb6YBuZI9a9qBrWuOSp_mkFn9JAzVO9bxRfbKxcblOuexsmxfzGY4R61Jt79VEYU0sGSiS9ocZqiPsBQ-T1JwebU5fWluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a23e19932.mp4?token=BPe5vDHI7AvDIk7HzZyQj79BV1TEQA-20k6DGSNWDSGIpXazimwKwS5OO2aUxLBBnjgp5TKZBJ2ZfYCHBmHf2QXgsrEwa-zV4N09EcWiov0CxGvrmb6SYBdwHAeTqEmvCR7MSxSquXOjFPR2nMw82X0CreRz5HH_1S6KqJ_5BlUdHvJv2fXBWl60VGj3ltVXEBdDLKeX6TmpHrbYJRgXs05Ax5bdR4himGeR9CVp5Rw-ejGwwOhyNQujbb6YBuZI9a9qBrWuOSp_mkFn9JAzVO9bxRfbKxcblOuexsmxfzGY4R61Jt79VEYU0sGSiS9ocZqiPsBQ-T1JwebU5fWluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشکهای جمهوری اسلامی‌به اردن رسیدند و پدافند درگیر شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/21770" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گزارش دیدبانهای اتاق جنگ :  ۳ انفجار در ابتدا حدود ۸:۴۵ دقیقه شب و ۳ انفجار بعد از ۱۵ دقیقه ۹:۰۰ شب تهران در لارک اتفاق افتاد تهران @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/21769" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چنل‌تلگرام رو پین کنید بالا حتما و نتفیکیشن های اینستاگرام رو هم روشن کنید کاملا ، چنل یوتبوب رو ساب کنید این هفته هر جور شده استارت میزنم
https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21768" target="_blank">📅 01:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منابع عربی: پایگاه موفق السلطی اردن هدف موشک‌ها و پهپادهای ایرانی است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21767" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش صدای انفجار اردن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21766" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز ادعا کرد ایران از ۳۲ شهر در حال شلیک موشک است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21764" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فاکس نیوز: جنگ بزرگ آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21763" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21762">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21762" target="_blank">📅 01:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21761">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21761" target="_blank">📅 01:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرودگاه مهرآباد تا اطلاع ثانوی تعطیل شد @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21760" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی:یک بار دیگر اراده ما را آزمایش کنید و بهای سنگین تری بپردازید، انتقام در راه است؛ فقط بدوید!‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21759" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک مقام آمریکایی: برای نخستین بار در یک ماه گذشته، حملاتی را علیه ایران انجام دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21758" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ اسرائیل در خبری فوری اعلام کرد ارتش آماده هر سناریویی است و یک بانک اهداف گسترده دارد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21757" target="_blank">📅 00:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرودگاه مهرآباد تا اطلاع ثانوی تعطیل شد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21756" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من رژیم ایران رو نابود میکنم، اینو بهتون قول میدم و مطمئنم این کار شدنیه.اونا خیلی ضعیف تر از قبل شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21755" target="_blank">📅 00:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21754" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار من تو مسیر بندرعباس میناب بودم  از کنار دیوار خیاط دانشگاه هرمزگان موشک بلند شد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21753" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سی‌ان‌ان: دور جدید حملات نظامی امریکا به ایران شروع شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21752" target="_blank">📅 00:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش صدای انفجار جدید از لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21751" target="_blank">📅 00:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های عبری : جالب خواهد بود ببینیم رژیم ایران چگونه به حمله آمریکا واکنش نشان خواهند داد، زیرا عدم واکنش به این حادثه می تواند نشانه حقارت باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21750" target="_blank">📅 00:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21749" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیانیه سپاه : دشمن در هر دو عرصه اقتصادی و نظامی، تبعات این محاسبه غلط را خواهد پرداخت
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21748" target="_blank">📅 00:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21747" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام:ایران میخواست یه سری مین رو توی تنگه هرمز بفرسته که ماهم جواب کارشو دادیم.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21746" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21745" target="_blank">📅 23:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آکسیوس : دستکم ۷۰ تن سپاهی کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21744" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسرائیل جنوب لبنان رو داره برای فصل کاشت آماده میکنه و شخم میزنه
😂
🔥
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21743" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آکسیوس:ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21742" target="_blank">📅 23:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21741" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ادعای آکسیوس : ایران در حال آماده‌سازی برای پرتاب راکت‌های حامل مین‌های دریایی به داخل تنگه هرمز بود
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21740" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای رسانه های رژیم :
حمله ای که آمریکا انجام داد با پهپاد بوده که از اردن بلند شدن، حداقل چندین پهپاد MQ9 از پایگاه موفق سلطی امروز به سمت منطقه تنگه هرمز آمدند.
فرماندهی سنتکام اکنون در آنجا می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21739" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تسنیم: برخی گزارش‌های اولیه غیررسمی حاکیست که بر اثر جنایت دشمن آمریکایی تاکنون ۲ نفر به شهادت رسیده و ۲ نفر نیز مجروح شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21738" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سید محمد مرندی: رژیم ترامپ مرتکب یک اشتباه بزرگ شد.
@WarRoom
😂
🔥</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21737" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21736" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری های تروریستی رژیم ، فارس و تسنیم این حمله را تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21734" target="_blank">📅 23:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش های منتشر شده از کشته و زخمی شدن تعدادی از افراد سپاه در پی حمله نظامی آمریکا به جزیره لارک.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21733" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21732" target="_blank">📅 23:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به گزارش دیدبانهای اتاق جنگ :
۳ انفجار در ابتدا حدود ۸:۴۵ دقیقه شب و ۳ انفجار بعد از ۱۵ دقیقه ۹:۰۰ شب تهران در لارک اتفاق افتاد تهران
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21731" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21728" target="_blank">📅 22:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه های عرزشی : درحال حاضر قایق‌های تندروی سپاه در تنگه هرمز،از چراغ‌های جستجو برای خواندن نام کشتی‌ها از روی بدنه آن‌ها در شب استفاده می‌کنند و سپس با استفاده از رادیو، با نام کشتی‌ها تماس می‌گیرند تا به آن‌ها هشدار دهند که تحت نظر سیستم قرار دارند و از آن‌ها می‌خواهند که از عبور خود منصرف شوند،درغیر این صورت با آن‌ها برخورد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21727" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارشاتی‌از‌ لارک هست ولی شب میلاد هم هست و عرزشی ها فشفشه بازی میکنن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21726" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21725" target="_blank">📅 22:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5076i5YycexYsxkr9e0UUXzVsttck-hLyTBVSAX0m34eWZQBUrgrhnJGUINKsFFEMYP7HIPW-sKZVuHVVTHUdHliAPuiB0hGxNQr11Yvp7ub6uvrNlXrNS7fSJTEI0kdXY70cODqNnRgEDyo0TNNStbICQ84aMwXxCn7Hleq8uvsAEEzGuafQNatbR5b-wvqo0YwOt7D7APiOFjKvSu7H-bgykJew8K0Non1AJSakmiiSmtz3kCBeqU9hlovukEAAyzQVcTglHQIXQKKaJizrLYPTo0CDYSXuc1eDZabbucx-qHVhLQinjcWCTPzEYtxEtUZWv2G7WPFA8hvyaVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگال کانال ۱۲ اسرائیل : مقامات ارشد رژیم ایران به دلیل وخامت اوضاع اقتصادی در کشور و ترس از بازگشت اعتراضات، در حال بررسی فرار هستند
مارک لوین به ترامپ ؛ اگر درست باشد، آقای رئیس‌جمهور، الان بهترین زمان است که مخالفان و نیروهای مقاومت ایران را مسلح کنید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21724" target="_blank">📅 22:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21723" target="_blank">📅 21:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شبکه I24NEWS:کشتی های جنگی ترکیه به طرز خطرناکی در دریای مدیترانه به کشتی های نیروی دریایی ارتش اسرائیل نزدیک شدند که باعث هشدار و سطح آماده باش رزمی در نیروی دریایی اسرائیل شده
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21722" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از تنگه صدا میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21721" target="_blank">📅 21:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21720" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyGJ_9Vr0og6DqKtH4-inLAgvC7wryzJS9rMjrLI6KudpeeSjbnn05mTSjPYZoDw6ro464MTSDe2pjVyD0RLoWe5KWgUjGpte3FroxzTPfHgJOQ2KIjgdP3pJWvEk2wjPlZ5gNjXEpaFnzhzvTnssyvhuqlW5U3SJV4w9zJ-d6kZTBVjNKRrspmDe_gQ4YwmsWloj8OqP6elCtxkMC-AkftBWgXXdeiZ9yqi9qc_5qikktJl4GTZHscTfyGn7IGQOUjdWa8qbOmgub4xZEBFeZybgXf0axxJ-p2-zS919Y7fcNMKGzFlu6Qe9hCDHv5-UI1rZNNgnG47p3fXsn5XKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی با تأخیر زمانی از حادثه‌ای در ۱۲ مایل دریایی شمال خصب، عمان دریافت کرده است.
یک نفتکش هنگام عبور از تنگه هرمز توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته است.
این پرتاب دقیقاً رأس سه ساعت پیش از طرف دیدهبان‌های اتاق جنگ گزارش شده بود ولی من از ترس حرف مردم به علت این‌که ساعت، ساعت معمول حمله نبود گزارش نکردم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21719" target="_blank">📅 20:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعزام بسیجیا با قایق‌ماهیگیری، برای مقابله با ناو‌های آمریکایی؛
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21718" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK1hRbVn0ZiCFDQb1YlwaH5tdRY2FqBfkoY4wuZm4QrBUKVz5xgvm-2C79_tMVMKPcNk1RPI6bWvOpYEfTF0Sd6T_vNstXKddu2d-FcddXOpqawNK8yEuxSUwbY3zY_s1r5Bn_EtjwONTsR2UUbs8zNtU_1mASHt2Se5F5v3ubjFkFkkFtIVFdTMdmSML5CDdvb_aWZQz3rJgK2qunSQDqFPN77fZtmfFH096WqiBqpxwkdWTEcrxSU864VnM6KURT6reh8BCcqfFhZZbtCC7ieGAMTzJgkln3Snh29vOHGnkyvs977bp6rP3aI72T0pKHxVrqlCSBdkW4fiFf_FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرنده «CMV-22B Osprey» مستقر در ناو هواپیمابر، کد اضطراری ۷۷۰۰ را بر فراز خلیج عدن ارسال کرده و در حال حرکت به سمت صلاله در سلطنت عمان است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21717" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy1pkXLSDPzePhnWMLlMnCaZWjZKPlW663t4Jz4VvTKDfF3f-TrT49xgtApAydVdOw7OlWFbVzExTreLpSH2ST6M5o-k1XHs-IxqZuKKf7UqnDnXVqc7HIj-5lnCp4-RIv9JM9TNO_VqHgRDwPCpgq3Gc34tqsNGt2-1oSZU1nz3MFIBnI5-aq7rJ7KhME1fuFaElYpnLd1ywYJLVu_o56cz8KoshxiZ04AXRnMjLwMpOOod1uB3P40fDgwqF5Pkwvi12N28g_9mUc2mmpFwjxHyQQwsCy11tY6PmcYbW_V9uQyDJYapdgey5VyDMIxATOD2Wuhcw3FEGPFYyDvZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91FBSu0a9UCFvzjcMUyTtURnsppXnSaEoqGuiJFggMZ4xQsnj6Qf4TwWq5QxkXttDMfzLZ-cZ7skIX2Xoooo6XsCg-QAmi8wvLKDxrzx530P9C8KypOOzjB0jh_puFHHrAcZ_0W-SHHovypbF25kMWI0ClnddjjqS7DNWqm5sdEJEi_BjejZEzRsxO_h7g8_R8oyUEkf2sLsKRcTG1j6fRbe-TdU1WnwplXADfjB_acGXt-pz6WSLDzBko2xI04nt4wQvqkO7jgOf18Mi225bw1Phx0025Wpa9mkYNNnkDtcLYSRabWvWZacHPNI2LQS0fS11mPD97aKRJWgPtODw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیکلاس مادورو از زندان:
«این عکس‌ها را به‌عنوان هدیه‌ای کوچک برای همه نوه‌هایم، چه پسر و چه دختر، و برای همه مردم شریف و بزرگواری که ما را دوست دارند، می‌فرستم.می‌خواهم بدانید که ما استوار ایستاده‌ایم؛ با قلب‌هایی سرشار از عشق شما. عشقی که به ما می‌رسد و به دعا، کنش و تلاش همیشگی، همبستگی و حمایت واقعی تبدیل می‌شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21715" target="_blank">📅 17:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن» آمریکا، بامداد یکشنبه ۳۰ اوت، پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پایان مأموریت طولانی خود در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت. خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند. این ناو در جریان مأموریت خود در خاورمیانه از عملیات نظامی آمریکا پشتیبانی کرده و یکی از طولانی‌ترین دوره‌های استقرار ناوهای هواپیمابر آمریکایی در سال‌های اخیر را پشت سر گذاشته است. آبراهام لینکلن قرار است پیش از بازگشت به پایگاه خود در آمریکا، برای استراحت و بازیابی خدمه در تایلند توقف کند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21714" target="_blank">📅 15:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21713" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
👺</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21712" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و تواشنگتن امیدوار است مجبور به استفاده از آن نشود
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21711" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پرونده جدید : مأموران ایرانی، کودکان زیرسن قانونی 15 و 17 ساله را در شمال اسرائیل، از طریق اینترنت اغفال ، جذب کرده و با پرداخت مبالغی به صورت جداگانه، آن‌ها را برای عکس‌برداری از مکان‌های استراتژیک و نقاشی کردن نوشته‌های گرافیتی استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21710" target="_blank">📅 14:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر انرژی اسرائیل : اسرائیل دوباره به ایران حمله خواهد کرد حتی اگر آمریکا توافقی امضا کند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21709" target="_blank">📅 13:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21708" target="_blank">📅 13:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رویترز : بانک مصر در حال بررسی پیشنهاد وزارت خزانه‌داری آمریکا برای قطع ارتباط شعب امارات از بانکداری واسطه‌ای دلاری به دلیل تراکنش‌های ادعایی مرتبط با ایران است. بانک مرکزی امارات بازرسی ویژه و فوری از این شعب آغاز کرده است. بانک مصر اعلام کرد عملیات در امارات عادی است و اقدام آمریکا هنوز پیشنهادی بوده و تنها به شعبه امارات محدود می‌شود، نه عملیات در مصر یا سایر نقاط.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21707" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLqU4UF2jyxCHm9b_CUbD_ADoBfZQMfsEGsUQ7WbjsrMEPZMsWZAI9oaDT-VhnMgVxGKwd59UQxtzQpD7k6nnwKzJxoZ9Vl1dsM_UtlHgGM821nnGsLw4_p9sZewv6Zzh668tuKuu10dyIDTZ5dNt3rSpfWAOM8KImUlq8BxnQsJ61srQXVI7lBu4lSQ8irDNsYTERvJJQuGL-dT96GU0i5JVYhuH3AwT5TH3DodKjF2zlFIEgvZL7IdOkzBU98_xDa69JSvI7MoVY0tBkSO-Q7PW7BtoIdmMgcKaqi1DeM1TCpfgg9b_V5FGwSsBF5bzby4gL7JsoCBrnOmK_yqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق، انتقال محموله‌های نفتی خود را از طریق عملیات انتقال از یک کشتی به کشتی دیگر (ship to ship) در خارج از تنگه هرمز، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21706" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آکسیوس به نقل از گزارش سنتکام میگه جمهوری اسلامی یه مشت آشغال ریخته بود (۲۰۰ شئ شکل مین) تو تنگه میگفتن مین‌گذاری کردیم ولی کلا ۱۱ تا مین انداختن تو آب، که ازون ۱۱ تا ۵ تاش درست انجام شده بوده
.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21705" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqQL4LIn9lW4qb_F84B6RFSbdqr1199qk7iMX8DLhz2vKTRVrkvH2GYi37_fpRCJsV1SiZF-u_dWAs4wYoSI9eTmI7dbdv-JfhMa_k5hHq-hM5BO1npbicUPzqk0UjG7Pel_kA-AzVmkz3BglHQR9ru8J8vFuOR40DFCn-zkgmh57igtaOuxbVrMFsgwgykdyzmSQQsDDQutnsio-lMz-q67Arn1TCC5XuGAbUqAbibTKSa1U8IO9ttiRfvFTZF5aQBs6fxtLc3wit0jtjLWkuH03to-pYGgzcGIbTzNJoSK5shr2k-0HPqIjt9g2NC6-28bW3jCxFysTTbxOfpcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند جنگنده F-16C/D گارد ملی هوایی اوهایو
از بال ۱۸۰ شکاری و اسکادران ۱۱۲ شکاری در مسیر خاورمیانه هستند. این جنگنده‌ها با کال‌ساین‌های
TABOR11 تا TABOR16 و TABOR21 تا TABOR25 و TABOR17
ابتدا به پایگاه لاژس در آزور پرتغال می‌روند و سپس راهی خاورمیانه می‌شوند. در این عملیات، هواپیمای سوخت‌رسان
GOLD10 (AE066E / 62-3569)
پس از سوخت‌رسانی به جنگنده‌های TABOR11 تا TABOR16 و
GOLD12 (AE44FF / 23-46116)
در حال بازگشت به پایگاه گارد ملی هوایی بنگور است. همچنین
GOLD22 (AE0479 / 58-0061)
برای ادامه سوخت‌رسانی به جنگنده‌ها در حال حرکت است و
GOLD25 (AE5FAC / 19-46065)
نیز در این مأموریت حضور دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21704" target="_blank">📅 09:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از منابع: مدیر سازمان اطلاعات مرکزی آمریکا (سیا) پیشنهادی را به مسکو ارائه کرده است مبنی بر برگزاری یک اجلاس که در آن ترامپ، پوتین و زلنسکی حضور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21703" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">@WarRoom
جعبه شیرنی ۲</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21702" target="_blank">📅 02:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشایان</strong></div>
<div class="tg-text">سلام یاشار جان. این یه پیام دلیه که برات می‌نویسم زیاد ربطی به ماجراهای روزمره نداره. خوشحالم که پیدات کردم اینارو بهت بگم چون بنظرم خیلی بیشتر ازینا حقته بدونی. من ۳۰ سالمه. ۸ سالم بود که تو دبستان شهید باهنر تجریش با رفیقام قفل وبسایتت بودیم. تو زمانی که آخوند نمی‌ذاشت بچه های ایران نفس بکشن یاشار رپفا یه تنه آرتیستای جدید و سبک جدید حمایت می‌کرد و میاورد بالا و من چون اینترنت خونمون دایل آپ بود می‌رفتم پاساژ البرز تجریش، یه مغازه بود مسعود موزیک که سی دی پستای جدید وبسایتتو برامون میزد و اون زمان رپ برای ما انگار تمام آزادی و چیزی بود که نداشتیم. و امروز برام اصن عجیبه که حتی پزشو نمیدی و زیاد به روی خودت نمیاری که اگه تو نبودی اصن چیزی به نام رپ فارس با اون دوره تاریخیش که هیچوقت دیگه اونطوری نشد به وجود نمیومد. الان شاید نسل جدید باورشون نشه اما ما یادمون نمیره تو کی بودی و چیکار کردی. تو فری استایل همه رپرا یه پسر عینکی لاغر بود که کم کم همه فهمیدن این یاشار رپفاعه. خوشحالم که الان از طریق این کانال از حالت باخبرم. به امید یه روز که تو ایرانمون، توی یه ایونت که کتاب خاطراتت از رشد موسیقی زیرزمینی ایرانو نوشتی و برا علاقه مندا امضا می‌کنی بیام و کتابتو بخرم و امضاتم بگیرم. عشقی داداش.</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21701" target="_blank">📅 02:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">@WarRoom
جعبه شیرنی</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21700" target="_blank">📅 02:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromalireza</strong></div>
<div class="tg-text">سلام یاشار جان عشقی
امروز دو تا مشتری اومدن (من صندوق دار یه مغازه شیرین عسلم تو پایین شهر) دو تا مشتری اومدن زرتشتی بودن و اصالتا یزدی واقعا خیلی آدمای با شخصیت و خوش رو خوشتیپ خوش صحبت با فرهنگ بالا با اصالت و واقعا زیبا بودن اصا انرژی مثبت فراوان اصلا خیلی حالم خوب شد و انرژی گرفتم
ولی در روز چند رأس عرزشی میان مغازه واقعا آدمای کثیف بی شخصیت بی ذات پرو و طلبکار بد رو کثافت و کثیف بد تیپ بد چهره شبیه خوک میمونن و شپشو ان آدم حالش بهم میخوره و واقعا اعصاب خورد کنه وجود شون حروم زاده های بی مغز قاتل
واقعا بی صبرانه منتظر روزیم که از دست این شیعه ها و عرزشیا خلاص شیم و مردم با اصالت مونو ببینیم و کلی کیف کنیم</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21699" target="_blank">📅 02:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار :
P-8 Poseidon
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21698" target="_blank">📅 01:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با یاشار : تنگه دعوا شده
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21697" target="_blank">📅 01:25 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
