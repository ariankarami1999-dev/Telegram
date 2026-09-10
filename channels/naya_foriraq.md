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
<img src="https://cdn4.telesco.pe/file/JK7-_qx5xkL0QfOBTABpiRDGfAP6DZIezg0aiFdXkUxBC-Zrb4VPuPPuNw_Bc0m-qOXRa2QeRVvJdSivWR8cY5psj5ZKwB_VwPEk1fmL7x_nnb9nbLKl60rRRIfU7ou7EgnlirDMo-k-zJ17l2rk1qNQi8puLcKLXptNaWF6cAf_hNkOG_ev-lYeDfpOBcgZ6RoiPSp6G42MFmWVWYQBY_HPueEknxznaj11sMoWobfyZ3wUBAae7FmYMFp2zZDjnf2AbqPOl4g0NyaC3soCUbT-AK_Ob9UYSiCdRWnEm-NcABo1pfy9gV9bN0uFW1_mlMPuY7UEKckFlsiD21t7wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انباء اولية عن تحرير القوات المسلحة اليمنية لجزيرة ميون في قلب مضيق باب المندب</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/naya_foriraq/90028" target="_blank">📅 15:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ باقتحام منطقة ذوباب المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/naya_foriraq/90027" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حادثة على بعد 98 ميل بحري جنوب غرب المكلا اليمنية</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/90026" target="_blank">📅 14:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAskaqOrQxFQ4Q7QuZxswZmORUK-W_vaz0GlxHsvPEIF93WYLYi-aEZi6zeoWS_H8TCQYMWrKshLrMddzvKDfmY0UVt3cI070HH5zh2tWe3nYuS_3GUAEVmSnNu3A3sjH92rMBXfodGpxjRyX9D7k1nr543rKyYYmzNfa5c7kkwEc6MtKT_Sq4Aq0luNPn22Wkb1PF1RyPu2zqFPP6KW2rhH9fQ_TQCJExqxmGV5qVyUNunMXwtgqsNxkR2oIYRACGThftDUqpOwfWHxpvDQFyA-WR7u9bArdPEyLf9ShveCxqvhbG3U4T6ztZQzDJPQ2Vkh47Fo1Un3urmQ0xOIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثة على بعد 98 ميل بحري جنوب غرب المكلا اليمنية</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/naya_foriraq/90025" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">العراق يعلن عن مناقصة لشراء ناقلتين نفطيتين عملاقتين لمدة 180 يوم لمرورهما بمضيق هرمز</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/90024" target="_blank">📅 14:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سقوط عدد كبير من القتلى إثر اندلاع حريق في سفينة أجنبية في مرفأ صيني</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/90023" target="_blank">📅 14:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAP9jl9fckZhbDzoAudUgTndlOBR3VvujlGCguurG1kLhrKXTJFEX9TKwqpb52C2MuS6x-m2QId2Xb24I6I4N4Mj9YHLx7K9XPak8dyPSk42K047nIsoT_Yd1wBZlf36vmZlQnd_6DfZ8I6y4xll3u8Ylt5Tw_UvYbZhoiZgDVDiU08H0BwP8fJ-yrfLQZvjAkcOgHbgM8JVx2pGSVtiKcMLdkzfeJiRk-2tcv9GjapZf-8IdDvjOjJ4DAUdYJ1oDNLcfOMZmEHneY2ElJJ1x5AmndiLyJx6ofATQnUf75mi7I-n38E4WRTgJlp4aHQSFNBX1oBMvV_9YIottlMQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر مغردا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90022" target="_blank">📅 13:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترفيهي
الاعلام السعودي: ‏قوات المرتزقة تنفذ عملية إعادة تموضع في الساحل الغربي.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90021" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مرتزقة الامارات تمنع مرتزقة السعودية المنسحبين من الساحل الغربي من العبور باتجاه عدن وتشتبك معهم بمختلف الأسلحة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90020" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مرتزقة الامارات تمنع مرتزقة السعودية المنسحبين من الساحل الغربي من العبور باتجاه عدن وتشتبك معهم بمختلف الأسلحة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90019" target="_blank">📅 13:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWwZU__QWY_-rR4UIQFrD3GbtiApdXeZKsKUmtavStjyqiF3aRcw7I1nPY_KjvfcgObXmOv6U_83SwdDgHhr_rw1_iRmBpi6FDjQy-EwHDBGMVnicUEedUSsciHb2gpZ8gO0Y008A-S8MCMJdC8dTXY8AVqxU8XJeeD908bXhgz05FGzVlEtjKWFfnZBAAI56loaluDItmpal6uvlS7d7S5OJ9jDuHMF3xo3bUzoZ1sAu0Btw0MOEXiieZ5Ls2bIrfAcXzVoo56VjZ_SGj0aUpIusbyIqp_6YChj1YiuKq9gXF15sFHvJE5f0J2zyOTSPkmL_I2NmI8BS8BZVfcI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز 102 دولار للبرميل.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/90018" target="_blank">📅 13:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90017" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90016" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📰
رويترز تقول ان باكستان سترد على الحوثيين وفق اتفاقية مكة من يبيض الديج.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90015" target="_blank">📅 12:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سقوط عدد كبير من القتلى إثر اندلاع حريق في سفينة أجنبية في مرفأ صيني</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90014" target="_blank">📅 12:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8265c7835.mp4?token=od5QJ2UoYpIhYxxbZ9JtcGDmqwufA498EnuX1stBKQP9X7qslIOG06SpIzKWWqbqlPR-WytiV9hUiCiqxMc8X1WrKb1n70lEwQkEI3pZtvZbtBxhax-7OLGIP-lhYK-DJosvt9iQTkSLFjwA4RJC0FDGWHQwHTcn91yorrMLSeDZS0-2ZqP3mvWUjRy1RHlWlQmJK2GeJ4gOGEkj4jM7fNv9B4giBIRVuNprF8D0PeoUaBKTsyJqK2IwL399ZBAIbO6Atvb-LodXRUb_lacYRDPbh-OTWE8_8dM2iJhbwevZMj5JLki8r92qTqbdOAO2BY9q2Wa_HtXbuFY_evUZUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8265c7835.mp4?token=od5QJ2UoYpIhYxxbZ9JtcGDmqwufA498EnuX1stBKQP9X7qslIOG06SpIzKWWqbqlPR-WytiV9hUiCiqxMc8X1WrKb1n70lEwQkEI3pZtvZbtBxhax-7OLGIP-lhYK-DJosvt9iQTkSLFjwA4RJC0FDGWHQwHTcn91yorrMLSeDZS0-2ZqP3mvWUjRy1RHlWlQmJK2GeJ4gOGEkj4jM7fNv9B4giBIRVuNprF8D0PeoUaBKTsyJqK2IwL399ZBAIbO6Atvb-LodXRUb_lacYRDPbh-OTWE8_8dM2iJhbwevZMj5JLki8r92qTqbdOAO2BY9q2Wa_HtXbuFY_evUZUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر لنايا:
رتل امريكي شوهد في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90013" target="_blank">📅 12:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIffS4Np6hECGR1KJYsfMhlTNJGZh3ir2mByGS-8cz6D4rS7I5udfj90HwFnu32p2piVjZo2FtZZiieEXqTBGbzSEIQPrPlzq1t-MGAaw8UErfGWOmtSAbGa7uC8trxvO62gUbq8MBdnB0Q2yKa0Dj07Ak6pZV98uPoqM_HYeSkXpn6Y0iC7rDGPrgnuY3cbvR7GmXNbn5m_L8djE4yjD36-j4HOu1l0549tfHKYFtlbQkB7yqtRMftmosQVAqkgCuH3LKT4EEF3wFTspuAE2ryiql9dvKlGrtGFzlfdzFkv_K1DRj6m_t2C9rAO4FhgMpiFlouO-FzWGk1fx6K1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية والاعلام اليمني داخل مدينة الخوخة بعد السيطرة عليها</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90012" target="_blank">📅 12:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoRomSBNRsOB3RAQQ7c4rZUDqsvrSoncaKWvnkdL44uAgawd45DocerhcHs5P-d3wJWEADGR6gkufq6e-0ji6vIjsrxtUBEPfWkN4uS5fPt28X-RT75AfNe-iGAQgXNEKQiEoeQqvgkAhoOXLDJ7XK42guKZVTePPRrENC-Kq7xBwOzjE0Mf6a2YMgExqrAIQwotdcRLTw_HeFCH5LoAAWLPCIszr7_IQZSVVLGkkqaUB03C_6NVrD5_v4EUS2LqfEpFZy3l0wnit3vagJV46mbHoZkDLfi5ArP6YfwVhzux-1E8G1wBAeZ9QErJCItvwI3TRaZjYSedmYe0IopvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز 102 دولار للبرميل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90011" target="_blank">📅 12:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
منظومات الدفاع الجوي ستصل قريباً من كوريا الجنوبية وتركيا والولايات المتحدة، لا توجد مهلة محددة مع الفصائل لتنظيم السلاح.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90010" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
الجيش اليمني:
تمكنت القوات المسلحة اليمنية بعون الله من إسقاط طائرة استطلاع مسلح نوع كاريال تابعة للعدو السعودي وذلك أثناء قيامها بأعمال عدائية في أجواء محافظة حجة، وتم إسقاطها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90009" target="_blank">📅 11:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
🇾🇪
قراءة سريعة / ماذا حدث  البارحة في اليمن ؟
- حققت قوات أنصار الله في اليمن مكاسب كبيرة على الأرض، حيث سيطرت على مدينة المخا الساحلية، بما في ذلك مينائها الرئيسي ومطارها.
‏- تتمتع المدينة بأهمية استراتيجية، إذ تقع على ساحل البحر الأحمر اليمني بالقرب من ممر باب المندب، أحد أكثر الممرات البحرية حساسية في العالم.
‏كان ميناء ومطار المخا بمثابة قاعدة عسكرية إماراتية قبل أن تستخدمهما لاحقاً القوات الحكومية اليمنية المدعومة من السعودية بعد انسحاب الإمارات من اليمن .</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90008" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi9dfVheuXZKPFgZlDfJQIRn5UBERysfou-YUAUuvMlK6qz7hrMW-f_rukSw6xF55gkJxNqMQwlNc24VCNoOwzRo6rCq2cmbEw5wOtYXaH6ED5HJMqkhYuI6qeBYG8LnKSKh4qw34xp5GnjsHIjLB6gxl4SVPQzRe0vnZNkrsgoE5KzcvQ9ERs2KDLpzviG6l0n6OhQyLjKm4HMO5wY-_4njuqCVh0VNiEuPK6C7eEB1ijBS7xUyTpKhUdQdUgXfD-V_DjkTH6mKvyoNhi9Mgdam7d17PdYvpuWWYx3hq4Z3GIp3wgWVugHJNBCfqw5tc9B9SA1UjKTJ_zK1yV9XtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43657329e5.mp4?token=oEkRCmp2BmULQuhHUz5gNf9XGg9pDm6O510sF4kzbxJ9o2lP_wtokpX_f3riXexHDcfdA922rZBYuHc6iVN7KkGRxMH5YVSTu_miKncnnsh5-sm3RqB2nUV4iieq1f-o6ushrz7kTSJDmqSX2L7v4_d-pXSO5w1vSttbfQDr6hhoY7JlbxUYjA9-QnZTaHhDVkdrBnXtKETrj66QZRPqFqzNy2ne-ZeBHrjp1p0SY6fzCLOETzlEWpnewmItMB2yqROx-M1BP89sjoqZJfaJ2Y5sRxVP85SXWIUQnkA4KncX46hccAJQ44Z99bmuBPkfE3j7JUvS86n15q8VbcmxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43657329e5.mp4?token=oEkRCmp2BmULQuhHUz5gNf9XGg9pDm6O510sF4kzbxJ9o2lP_wtokpX_f3riXexHDcfdA922rZBYuHc6iVN7KkGRxMH5YVSTu_miKncnnsh5-sm3RqB2nUV4iieq1f-o6ushrz7kTSJDmqSX2L7v4_d-pXSO5w1vSttbfQDr6hhoY7JlbxUYjA9-QnZTaHhDVkdrBnXtKETrj66QZRPqFqzNy2ne-ZeBHrjp1p0SY6fzCLOETzlEWpnewmItMB2yqROx-M1BP89sjoqZJfaJ2Y5sRxVP85SXWIUQnkA4KncX46hccAJQ44Z99bmuBPkfE3j7JUvS86n15q8VbcmxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
صور الأقمار الصناعية من 9 سبتمبر تظهر أضرارًا كبيرة في مصفاة جازان التابعة لأرامكو السعودية، مع تدمير ما لا يقل عن أربعة مستودعات تخزين نفط على الأقل في الضربات الحوثية الأخيرة.
‏كما يظهر أثر حرق/سحابة دخان غير عادية في منطقة معالجة النفط داخل المنشأة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90006" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90005" target="_blank">📅 08:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stUfEhNTZrNIMPZkAsSqCIqd3uF9huGxQ_Jg9-kFkIiqDFsQICwxmW3tSMonUgHUxDBd8A0zTsSDtyjJLyC5UKxBKDMJGhTqNVwMNekSqTCDrDtAThTXPfbQ4jl0aPo2zLDgKH-MWpoqPsoDr3F3UT-KPvYToHC7bm0LpPKpP5Rl1kNITwQpxdpxe3WUp2jBVNWAu_NKnuaGAH2Yr6nFY_reaZyJeCbHjE8PWlLqy1S4GzdWx0_BnBZw-qPRc6FwbO1Y4IffJYhKSvMlNkdu4vbs6G8j6EtXimpd6_77SiT11Ho4nK76vykU3fsBOME_QLHkc9vi26Cwy5B3VvuIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة بالسعودية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90004" target="_blank">📅 07:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYuciyMiN_6P_FUEBhJvPZ0vKdoUVPy75gpKG3nEHDW_bWc5WDrYSOL3nKZM7TWM-0sXOmzKcQei3RRJEDh3IBZDg012OV1yra3-el88UJECKJ_XVvVEindPO7VUiUj0D9_mkFMnGS87dyq4z8fLfrPOH96bZ-ccXSs1PItx1nlla0GssrcwOKoev6VPcrtBkMW_RSD9hzLWos-5YY3Pc70hs8_Z5RtMBRnY1b1y1iszWQnnp36R7n5Eh0yJiG9z0BpNi7VBhhZD-f9zCbobl5SMd5ncGaZkE3zhQzxobnFI4AGqOIpjfEHNsV0Hup63_VTvscvvZ40mQ4IQwIzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربات صاروخية تدك خميس مشيط</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90003" target="_blank">📅 07:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90002" target="_blank">📅 07:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90001" target="_blank">📅 07:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990b969f2e.mp4?token=cCInFw6TyxGueCafRFSULT1_fB5SQLFoUW0tZMNQihG_v02SHHRpICmlUPFSpXsyA8m0YYimKentHbIWYz3sTTZHvWIv2mn88bOoSsQ81Kb83RladxZpJGJ3W2ISAiFiJXMjH0czdySiYQ0XsNFdS7qoEyFlQnWTog0GMAYJjfB6P1RvJfNpf2-eLcF-Xatno_0gQwluh8wwDXFQfvloqFXeYgpV_T6qUs4G7f_1MZdrMnrgzcYWqfgy-C4PItp_OLuh31kfb2siUQZaj1Lm0EMvsv5G_uuqo65Fw-5Y_nhZK5eA2v3uSd-4PU-m1VKtG76wEY_e-dXUYJ_mhDoLM2XHPkBtksJ2nsHzC-RoWth3AMuuaSjnDP9oc-A-m8wxDS0AkqOkEqnuR1zDojZ7q7pvZZKCf0blH3TgEf8VwqxyGHKA48D6Y6FMAt2ZXYtXycpvS2C_FZSN_fsCjvIRTtAjf-86fEDieaNuaVv2CjM0BPXOmZet_GJY_t7u5yq6wFkKkI8vZOfIqwdnsZzvbc6QmEGQCdYxFtra2wsSPUsEvknpndywgC65vtNx1XhdCXBTw2DZJpFQ6YLJV4k2_xC7t8iy_3He5Wtpsvc8760aPNL1nTFuAd3fQ57mh0IMDkcrwrrSGTLtMQ4iXiBZ9yFAIT0Wi9jwwEuqNOaXaC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990b969f2e.mp4?token=cCInFw6TyxGueCafRFSULT1_fB5SQLFoUW0tZMNQihG_v02SHHRpICmlUPFSpXsyA8m0YYimKentHbIWYz3sTTZHvWIv2mn88bOoSsQ81Kb83RladxZpJGJ3W2ISAiFiJXMjH0czdySiYQ0XsNFdS7qoEyFlQnWTog0GMAYJjfB6P1RvJfNpf2-eLcF-Xatno_0gQwluh8wwDXFQfvloqFXeYgpV_T6qUs4G7f_1MZdrMnrgzcYWqfgy-C4PItp_OLuh31kfb2siUQZaj1Lm0EMvsv5G_uuqo65Fw-5Y_nhZK5eA2v3uSd-4PU-m1VKtG76wEY_e-dXUYJ_mhDoLM2XHPkBtksJ2nsHzC-RoWth3AMuuaSjnDP9oc-A-m8wxDS0AkqOkEqnuR1zDojZ7q7pvZZKCf0blH3TgEf8VwqxyGHKA48D6Y6FMAt2ZXYtXycpvS2C_FZSN_fsCjvIRTtAjf-86fEDieaNuaVv2CjM0BPXOmZet_GJY_t7u5yq6wFkKkI8vZOfIqwdnsZzvbc6QmEGQCdYxFtra2wsSPUsEvknpndywgC65vtNx1XhdCXBTw2DZJpFQ6YLJV4k2_xC7t8iy_3He5Wtpsvc8760aPNL1nTFuAd3fQ57mh0IMDkcrwrrSGTLtMQ4iXiBZ9yFAIT0Wi9jwwEuqNOaXaC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أرتال القوات اليمنية تبدء بالإنتشار في مدينة المخا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90000" target="_blank">📅 07:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f44cc781.mp4?token=QMpfDvi5PodHMllUSPYhGRANZuXiFrF4RdfwVE5GXB8BDnSBmedIs4xsvftyCvpQwYda6xSYGKMUGjWlfVwKY2QH7OyDgRtjTA4OIQ900pBEa80fC8ln77HFey72gT1xH2qHmnBiXT5xQ1leNG9FZJcm4esry-Khhql2TNGfmDqobL2BenQ3cXKpurkXRFRYfGh7Qod0Y6YwoAPvPCzNIT2_1F4vvL0Q5oMCV25XkT3HzR629Z18oDzG7SY61LJ0f2spgCkqFfzcNkJUw94GESNtI-X7Kpa8MIIEKyerwJC1mp5Qvsp0pr0w0b7WMsCEIp0J96CaqqdXPBAD-IVWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f44cc781.mp4?token=QMpfDvi5PodHMllUSPYhGRANZuXiFrF4RdfwVE5GXB8BDnSBmedIs4xsvftyCvpQwYda6xSYGKMUGjWlfVwKY2QH7OyDgRtjTA4OIQ900pBEa80fC8ln77HFey72gT1xH2qHmnBiXT5xQ1leNG9FZJcm4esry-Khhql2TNGfmDqobL2BenQ3cXKpurkXRFRYfGh7Qod0Y6YwoAPvPCzNIT2_1F4vvL0Q5oMCV25XkT3HzR629Z18oDzG7SY61LJ0f2spgCkqFfzcNkJUw94GESNtI-X7Kpa8MIIEKyerwJC1mp5Qvsp0pr0w0b7WMsCEIp0J96CaqqdXPBAD-IVWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🇾🇪
القوات اليمنية تصل إلى مطار مدينة المخا.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89999" target="_blank">📅 06:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI_PESWuv8GRNSwZCu1xngfPQ6PzZN54Em1G1yipYJK3Z9IAZHPFXmtSjiTvHIPlaPgcKNe6eEtJZiI5E8_aEiD_6xa2XczdpODzxteLO-AQkWH3VctaQrPABEgo-Hu6PPmKxlNBADbqN4ie6uxVczdMHSfOf-ESXbG1J0qApnCkRa8w6zPxNyLrZyTiZq0fTp3f56YsoAqz5LXF88vGHiliiorvdsMpsLFH768XleQlMy7jLb67HOeNvBPOBXok43ojYEI20T0togOn7Rrj07ZLJ0_jGq4K7Z1j00p7Py-jB0D87r0X_wZr_vEjA7SAoxA50YDxFMUKYmhQPf5kYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
السلام على زيد بن علي
اليوم يومك يـ الشريط الساحلي
من با يرد السيل لا روس التباب
من بعد يختل و المخاء والهاملي
من كل باب الزحف قادم يا ذُباب</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89998" target="_blank">📅 05:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
🇸🇦
هروب مرتزقة السعودية من مدينة المخا عقب سيطرة القوات اليمنية على يختل والتقدم نحوها.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89997" target="_blank">📅 05:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
بعد أن زعم الإنتصار على إيران.. ‏ترامب: سينخفض ​​سعر النفط بمجرد أن ننتصر في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89996" target="_blank">📅 05:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcba18ca4e.mp4?token=tXu0BtxOki5weztiKxwG1WhS0GoQICsEKVGys5fv9tyjKOQO8a8ItN3QutpGXgr2CcxuyAaEfrL9Ulyui07qsVUGV4YyMqnLQ_KaUx5q4xlo1zC9xFAxp6n9xAaF-pPlZnYzo6I-Ou5hPzYy5w_2k2b36Ytowov56CRH7NEURV7VwFz-LFPH6-jhApybb6jJJ8T0EA3PJDUxhoVq-aW82lWWZeiqIb_eI2Wcwu6dcShxoyGMw9pYR12nqi1EJUDHPkBLWs2pYanaM0nI-Be1gcYAQjiWvzKjQm53j_ra2Qka3iTXHkDHstQhw-ODvzxcPh8HDGxfo1W4abohbAZNAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcba18ca4e.mp4?token=tXu0BtxOki5weztiKxwG1WhS0GoQICsEKVGys5fv9tyjKOQO8a8ItN3QutpGXgr2CcxuyAaEfrL9Ulyui07qsVUGV4YyMqnLQ_KaUx5q4xlo1zC9xFAxp6n9xAaF-pPlZnYzo6I-Ou5hPzYy5w_2k2b36Ytowov56CRH7NEURV7VwFz-LFPH6-jhApybb6jJJ8T0EA3PJDUxhoVq-aW82lWWZeiqIb_eI2Wcwu6dcShxoyGMw9pYR12nqi1EJUDHPkBLWs2pYanaM0nI-Be1gcYAQjiWvzKjQm53j_ra2Qka3iTXHkDHstQhw-ODvzxcPh8HDGxfo1W4abohbAZNAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب
😭
: لقد انتصرنا في حربنا على إيران.  ‏يجب تسمية مضيق هرمز بمضيق ترامب.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89995" target="_blank">📅 05:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGNVhMwPn_Kj-dB7xrK3QKFx40ZhmZLIgSaBM_t2jxMUY2TIKTHYkLUBTDV-wR6eA68Ol6ktadWuVnKtSzHAjgptxVn6jRyU0VhbRlzC_9stVNFf6__WybddtLsmLwr6_h4X_A7l1NcYp6b5sDvjGrg3SMNEg8nFdiKnz2iKjHBlO6XkY54MFueo5gZagPrUqTpWqf1knX5VYUrwrQ6lSdgV8g0fvlrmgJOUzZ3yOhx8fvGmX4xHI8D67vdUVG9foWfNK3QqN9Hf3VnMjHdeW8la8Ib8v76LfTgj6HJfDmzFQ2OShCuj1KnGboKNHOSQsp7s-gDz6qIkORa1GhV9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب
😭
: لقد انتصرنا في حربنا على إيران.  ‏يجب تسمية مضيق هرمز بمضيق ترامب.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89994" target="_blank">📅 05:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9641772f6.mp4?token=YsZjQgXca3c8ER6rsvq8MNbVgzO9D9bmTsDzfwXM87E1OYjhR8Qw2chBsCI0cf6cqe8P7L8ocw10tgvxLOmPQPPqPVXtEPwuoS44Qq-FR2G_QEJNH4LVovF06jN62WRMTWG-SvJIbQMThkwyRZnE_igUoAd4D_JC74aZjsoxKQzMxdGuEdeRn3jcCYOZjkOe99OvuIw4562Tq0Dxxt5F9ZO_FC3qUlREcqIVSMPN1MarEQtKs1KWb-_cKXF2eb2_8hT6ybVvK20Bpp0ICJVLueeOZlnF7FdpOJpIgkaCRc_qfMzO8AIXOBFT53_7Qys16B9M97gssw2OwIr6vpEeyIFUoWauvCUWc1qba4mVyBJLGBjxqYc1Hq5h7L27jPCjVUqTHo4UZ7YFfjf-GVnD0448QB06aXRQMYd2gO-vqA1cH02SrcZI6d9DpYvnkYDq6WNczuMGUO-gPES5yAi4aTHW3z4AHq9JwXRxxiPqFlTaLFZUMLbqrzJYnaghsziw0LB_H8ONF-u9IIRq0TlrxMZ3hOg3caVsD8SFurHMhaqh8ZgRb9gjFNhX1E-ozSxmMoEgrvmWD7uVNB7HMlkgmuT8TcoK-oVJ80JsPP73C0xZGKk8kC3cSHzbuglAlG4lWxnstMwyzd6O5QzviJ63BgQx_swOLEYtzXkjzttzrsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9641772f6.mp4?token=YsZjQgXca3c8ER6rsvq8MNbVgzO9D9bmTsDzfwXM87E1OYjhR8Qw2chBsCI0cf6cqe8P7L8ocw10tgvxLOmPQPPqPVXtEPwuoS44Qq-FR2G_QEJNH4LVovF06jN62WRMTWG-SvJIbQMThkwyRZnE_igUoAd4D_JC74aZjsoxKQzMxdGuEdeRn3jcCYOZjkOe99OvuIw4562Tq0Dxxt5F9ZO_FC3qUlREcqIVSMPN1MarEQtKs1KWb-_cKXF2eb2_8hT6ybVvK20Bpp0ICJVLueeOZlnF7FdpOJpIgkaCRc_qfMzO8AIXOBFT53_7Qys16B9M97gssw2OwIr6vpEeyIFUoWauvCUWc1qba4mVyBJLGBjxqYc1Hq5h7L27jPCjVUqTHo4UZ7YFfjf-GVnD0448QB06aXRQMYd2gO-vqA1cH02SrcZI6d9DpYvnkYDq6WNczuMGUO-gPES5yAi4aTHW3z4AHq9JwXRxxiPqFlTaLFZUMLbqrzJYnaghsziw0LB_H8ONF-u9IIRq0TlrxMZ3hOg3caVsD8SFurHMhaqh8ZgRb9gjFNhX1E-ozSxmMoEgrvmWD7uVNB7HMlkgmuT8TcoK-oVJ80JsPP73C0xZGKk8kC3cSHzbuglAlG4lWxnstMwyzd6O5QzviJ63BgQx_swOLEYtzXkjzttzrsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  أتوقع أن تنتهي حرب إيران عقب انتخابات التجديد النصفي مباشرة.  ‏أطلب منكم أن تسمحوا لنا بإكمال المهمة التي بدأناها خلال أعظم عامين في تاريخ الرئاسة. لقد كان هذان العامان الأكثر نجاحًا في تاريخ الرئاسة.‏  خسراتنا للانتخابات النصفية يعني خسارة الكثير…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89993" target="_blank">📅 05:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0685f235c.mp4?token=VAGV1zcCUUmAPoAIs1LwSJMJpgsoHArryXL7k1t96VvQ3wE_Lpnb06ytNfqR7cFK88a2Ilzx62vMi_DIZRvxJr9hbFjJ8UNGJzdyqVYNwkOIg4Ghtgr9zyqR3L6LCubGR2tuNsjwE_LgYZsIqJwFU2hFpLxUkFglQFbodQHGJ4O4nWL4nx8qOcxYc9LsSY-EZ48wpd-5FUB2VshtoClYg75zefhDFzmnsE6t16MyLZtjTxoINDKTRtTjvwtnZ50SCnHvucaTO3JqoP7FBO5WjnObeUHbBYr-zxcuFdIxA8u2YogE259lQ8d97tiHMgY9CuvUZZ-t-ufxs-biEfZ_uHqBCgVCBsLgGLoUSgsCI4ypnFR9PHokYIiHel74O52iM3bUp7elf103bE4OsdRgqiK0C3cYOpQmQh4aAoHTx-g5SZiKUKsv_04C6hplxdBL3B_8hxrxKZZVMDRQWeOODRNL66WpgAemuWw8jsdPBmU39smEeiOv886UrUMS2oCLHpdHoyYKqzfCFOIA5H6QidT1YOavYwzUoFd_tRm2AeOkRvKAcreXN5nllJ03V0Lmv4Cw1TZS6Ju_QaJOui85Y2QzJ4fN7Jz4LDz2bVuHxera_CKKlCAlSgoQNgO9Rc9KVJEOKenmi7zSPVGuBb1F7TXGTzsgWZzhzBkqrkzZb34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0685f235c.mp4?token=VAGV1zcCUUmAPoAIs1LwSJMJpgsoHArryXL7k1t96VvQ3wE_Lpnb06ytNfqR7cFK88a2Ilzx62vMi_DIZRvxJr9hbFjJ8UNGJzdyqVYNwkOIg4Ghtgr9zyqR3L6LCubGR2tuNsjwE_LgYZsIqJwFU2hFpLxUkFglQFbodQHGJ4O4nWL4nx8qOcxYc9LsSY-EZ48wpd-5FUB2VshtoClYg75zefhDFzmnsE6t16MyLZtjTxoINDKTRtTjvwtnZ50SCnHvucaTO3JqoP7FBO5WjnObeUHbBYr-zxcuFdIxA8u2YogE259lQ8d97tiHMgY9CuvUZZ-t-ufxs-biEfZ_uHqBCgVCBsLgGLoUSgsCI4ypnFR9PHokYIiHel74O52iM3bUp7elf103bE4OsdRgqiK0C3cYOpQmQh4aAoHTx-g5SZiKUKsv_04C6hplxdBL3B_8hxrxKZZVMDRQWeOODRNL66WpgAemuWw8jsdPBmU39smEeiOv886UrUMS2oCLHpdHoyYKqzfCFOIA5H6QidT1YOavYwzUoFd_tRm2AeOkRvKAcreXN5nllJ03V0Lmv4Cw1TZS6Ju_QaJOui85Y2QzJ4fN7Jz4LDz2bVuHxera_CKKlCAlSgoQNgO9Rc9KVJEOKenmi7zSPVGuBb1F7TXGTzsgWZzhzBkqrkzZb34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من التحرير والسيطرة الكاملة لمديريتي حيس والخوخة ومثلث المخا من قبل القوات اليمنية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89990" target="_blank">📅 05:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🇺🇸
رويترز:
تعرضت عدة طائرات عسكرية أمريكية لأضرار خلال هجمات ليلية استهدفت قاعدة موفق السلطي الجوية في الأردن.
إصابة طائرة أي 10 ثاندربولت وتضرر 8 مقاتلات من طراز إف 15.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89989" target="_blank">📅 05:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65019f0f60.mp4?token=buBbUF0k90ZlGi5_NjnCwfuedEqTSTQSguhen7hdkZY4Ob9aORGr3BgqhG6GTI_HjkxVlHCMp72QGIMAFK3ZSkQZoSz-J01amoLeDF7SSPB9u8ZObHp6afYS5EVgvKl60azxZu6EqrxacZe9151wynlflolRR00_7epi4SKQQv6QkCfuC86YQ6uxOfzFH1MbPriHQ0Elq_M3ywHRf02t8U2dOewxRmkJxsgrcxr-dweIrpS-qBJpWd3b6tJawI5X9BOYXWOENAjfVao0LDWCFcjhG9NhcaMy9Bhz3Y7fLerPmrkbwUplwNs3H1NXIiQQQlIstw0wCxQWjs1eP6gvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65019f0f60.mp4?token=buBbUF0k90ZlGi5_NjnCwfuedEqTSTQSguhen7hdkZY4Ob9aORGr3BgqhG6GTI_HjkxVlHCMp72QGIMAFK3ZSkQZoSz-J01amoLeDF7SSPB9u8ZObHp6afYS5EVgvKl60azxZu6EqrxacZe9151wynlflolRR00_7epi4SKQQv6QkCfuC86YQ6uxOfzFH1MbPriHQ0Elq_M3ywHRf02t8U2dOewxRmkJxsgrcxr-dweIrpS-qBJpWd3b6tJawI5X9BOYXWOENAjfVao0LDWCFcjhG9NhcaMy9Bhz3Y7fLerPmrkbwUplwNs3H1NXIiQQQlIstw0wCxQWjs1eP6gvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنة تتحرك نحو المخا بعد السيطرة على يختل.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89988" target="_blank">📅 05:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
ترامب:
أتوقع أن تنتهي حرب إيران عقب انتخابات التجديد النصفي مباشرة.
‏أطلب منكم أن تسمحوا لنا بإكمال المهمة التي بدأناها خلال أعظم عامين في تاريخ الرئاسة. لقد كان هذان العامان الأكثر نجاحًا في تاريخ الرئاسة.‏
خسراتنا للانتخابات النصفية يعني خسارة الكثير من الإنجازات التي تحققت.‏
أطلب منكم أن تتصرفوا وكأنني أنا المرشح في بطاقة الاقتراع!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89987" target="_blank">📅 04:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXN0nTe1TnwoyKd2bVxdFC9EBng29tU9gp2qRvFVUNlAeRXgpFEZKQicTOfYjDW_eTUa92LzsA7jIzBIDTf4cN9M5DbS3aEc4rvI96B5Ks0b-OuvI-rodfPu5Bz_uPL9m70c9_yYQwbuKzFOqdHZwk76ZHRACkikOH1M6HUkbH4OXUKINDS8OhJtgbtT2GZWrGo5SDBYkmNSOnf8n4rygrYRuPk194G4DgMnG1wLRnFkXtW8JcH5_fIAuus1vbJHyEfGVXcCp_WNPhtZ2SBtnB3uoKhxEiIfFGl09S_l-fpERAGxcbmVb8SUJB34erGll9llLL5Rvwzh1wtg0PLqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني لنايا: تم إستهداف قاعدة خالد الجوية في خميس مشيط بعدد من الصواريخ والمسيرات الإنقضاضية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89986" target="_blank">📅 04:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات في ابها وخميس مشيط</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89985" target="_blank">📅 04:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89984" target="_blank">📅 04:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكير</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89983" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكير</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89982" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8305181b5.mp4?token=QVeN-N4y_2GuzOSHwVVIbR8PQnA0BOBMeYaw3RcmSaq8v-BilviFUEJ8GfmlpGj8zLCahbQ_3bQS_mcqnoYKQgzUmickoaAOl1st3EZ_ahKVHSmSuHxLqEleNtuJqDIXxzI1lceCp_pi0oGqCNI73WgF-szQ6zjLlFrD_gSrPuLFmsOWNVKFN8o9pZffRpAnz0tGEkOXQuiWz4ZAXCLbC1VMrBIk3kCj_wrbiC5__Inp2mAeT0vUDYMSjrQdnZJjvxi4lyXPz5GJje2Jl0uVIQXadBYAG9iodW9L7rndGNXwPDupYaAG8_lT0QWtcNiWEzyaHWdj9Jz1cqZFnw3EyVzhbcGhYL7UQVD6eGBpiJKCaUo1cBYomLGqsibYdX29SBOjrvIe4cBxzP3mHcTtuJ2ms7BUh2zK8sErNLk4J51TMTNvu09mQP3QX-Hw4uPkSTfSlZh6Lx7KBv7aHc1E7ymLlmHIrQI1p4sB16tjaxj5JC0o_sDIJ4VtYfHOi7M5D0teitYFAoCHqHcSqNenq30ixrxXbNeqpcZdripmVYmwTwXj-JmzXBCApxPG1jIIxVLafuN_969VhfxTQEBKldB-NSN81fCyB82m73csN564Gas-hEsgq9iCtwxMwD0r9fDzwLDJvCa3o-clO4TaoLGSc3sppZDRHJjiQl0ZZCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8305181b5.mp4?token=QVeN-N4y_2GuzOSHwVVIbR8PQnA0BOBMeYaw3RcmSaq8v-BilviFUEJ8GfmlpGj8zLCahbQ_3bQS_mcqnoYKQgzUmickoaAOl1st3EZ_ahKVHSmSuHxLqEleNtuJqDIXxzI1lceCp_pi0oGqCNI73WgF-szQ6zjLlFrD_gSrPuLFmsOWNVKFN8o9pZffRpAnz0tGEkOXQuiWz4ZAXCLbC1VMrBIk3kCj_wrbiC5__Inp2mAeT0vUDYMSjrQdnZJjvxi4lyXPz5GJje2Jl0uVIQXadBYAG9iodW9L7rndGNXwPDupYaAG8_lT0QWtcNiWEzyaHWdj9Jz1cqZFnw3EyVzhbcGhYL7UQVD6eGBpiJKCaUo1cBYomLGqsibYdX29SBOjrvIe4cBxzP3mHcTtuJ2ms7BUh2zK8sErNLk4J51TMTNvu09mQP3QX-Hw4uPkSTfSlZh6Lx7KBv7aHc1E7ymLlmHIrQI1p4sB16tjaxj5JC0o_sDIJ4VtYfHOi7M5D0teitYFAoCHqHcSqNenq30ixrxXbNeqpcZdripmVYmwTwXj-JmzXBCApxPG1jIIxVLafuN_969VhfxTQEBKldB-NSN81fCyB82m73csN564Gas-hEsgq9iCtwxMwD0r9fDzwLDJvCa3o-clO4TaoLGSc3sppZDRHJjiQl0ZZCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  القوات اليمنية تتمكن من السيطرة على مدينة يختل.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89981" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89980" target="_blank">📅 04:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89979" target="_blank">📅 04:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892188075c.mp4?token=WO-fcU78JtAHTApIjJbjO4yzvDExcLQp0S1PYQBhgwYbd5pIMqPac-vyU89Be_5rUN0s21aHGUKr4NdAzM5iw26TrGIxfM6ZSo443TOrVVtoxSsE9EE0a0z-vVRdLas5c0ZKqq8ZSyp5IQKgRDj21td-vuBhqBqbJdR5zB_fRGVBQHfuhbzraxUdoFBoKtDXonhEj3T2kuGfOypn-D1Zp3apqjKs5LIvALp7PneLKUrZ-u3dBpSx07EeJM00qa2GmFUEcfoiAGN2xyutmOOj78UhdaOFDxm1PxgdIeqassEmqby6E4nhIrEcPPczZl4me0V1TtgpgnOxX7cb8nag-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892188075c.mp4?token=WO-fcU78JtAHTApIjJbjO4yzvDExcLQp0S1PYQBhgwYbd5pIMqPac-vyU89Be_5rUN0s21aHGUKr4NdAzM5iw26TrGIxfM6ZSo443TOrVVtoxSsE9EE0a0z-vVRdLas5c0ZKqq8ZSyp5IQKgRDj21td-vuBhqBqbJdR5zB_fRGVBQHfuhbzraxUdoFBoKtDXonhEj3T2kuGfOypn-D1Zp3apqjKs5LIvALp7PneLKUrZ-u3dBpSx07EeJM00qa2GmFUEcfoiAGN2xyutmOOj78UhdaOFDxm1PxgdIeqassEmqby6E4nhIrEcPPczZl4me0V1TtgpgnOxX7cb8nag-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/89978" target="_blank">📅 04:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8ca1cfd7.mp4?token=KfWeRM01LoidqaWxq6l91kIGVV4S8ahzYKYoyiJK4M_xWhY3vP4dIYTy4nDIVxn9-AzGliFbm6QIxO_w5F0khpoIk5f04aTL6DU5meJp3DwN1Phtzi3QQqh0BcG3OEmtsEm3kp_ihAo5kpvY3xp0Yh921502F7YrsTtjY4MK1VFSpI7NW1NFvGvvzfILtpaBNAHNexkS96nooF2t7xi3Tb-3kdDnmwk_V1Cf309oGWK8u8PWGQzymCDWHPMYyB7XSTu7Xi3bW6d0L4QK94xoDd9tB_ZgwEY3qAqiFVNd8Y41iMKq_AD3udPwr5S_uAK_ZKMs1zQmocoH3cCu0wLmK4ovFUasJk1rGfWJTtbJCKtYY2PcQJqiMo5bbssM2reTL-BwISb7ZLasQpADIYV4y1Wsl5ANJOxmcV8Ns0T4jQofFsFxiGu3iADZ2HgfnlLSCX5WTh-L2n2frqz2yHe5htKhiZAXtW1jKpAmrDcR0W-MEdzIufyktRFnHgtEleVWS8hfeSzUbmUv7n4_UiL4rJVPVNjGP29RH1IpIsvoXqUUp5Z1Ay-hbDOgN_hxssooGWU7Loq5AzWtRMgiH5cfEUvOWAUS2X2oWb-r1NtNg9dFxl8dwrZVIQKiqhBLupf0ITmwAZRQ0yjZM8ahsiG_nBisWP8ZtecPjfgUMCQ-jQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8ca1cfd7.mp4?token=KfWeRM01LoidqaWxq6l91kIGVV4S8ahzYKYoyiJK4M_xWhY3vP4dIYTy4nDIVxn9-AzGliFbm6QIxO_w5F0khpoIk5f04aTL6DU5meJp3DwN1Phtzi3QQqh0BcG3OEmtsEm3kp_ihAo5kpvY3xp0Yh921502F7YrsTtjY4MK1VFSpI7NW1NFvGvvzfILtpaBNAHNexkS96nooF2t7xi3Tb-3kdDnmwk_V1Cf309oGWK8u8PWGQzymCDWHPMYyB7XSTu7Xi3bW6d0L4QK94xoDd9tB_ZgwEY3qAqiFVNd8Y41iMKq_AD3udPwr5S_uAK_ZKMs1zQmocoH3cCu0wLmK4ovFUasJk1rGfWJTtbJCKtYY2PcQJqiMo5bbssM2reTL-BwISb7ZLasQpADIYV4y1Wsl5ANJOxmcV8Ns0T4jQofFsFxiGu3iADZ2HgfnlLSCX5WTh-L2n2frqz2yHe5htKhiZAXtW1jKpAmrDcR0W-MEdzIufyktRFnHgtEleVWS8hfeSzUbmUv7n4_UiL4rJVPVNjGP29RH1IpIsvoXqUUp5Z1Ay-hbDOgN_hxssooGWU7Loq5AzWtRMgiH5cfEUvOWAUS2X2oWb-r1NtNg9dFxl8dwrZVIQKiqhBLupf0ITmwAZRQ0yjZM8ahsiG_nBisWP8ZtecPjfgUMCQ-jQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"سيتفاجأ العدو بتقنيات غير مسبوقة في البر كما تفاجأ في البحر" | سيد القول والفعل</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89977" target="_blank">📅 03:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عضو المكتب السياسي لانصار الله حزام الاسد: ‏سواحلنا الغربية جمهورية يمنية لا ملكية سعودية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89976" target="_blank">📅 03:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08c86dfa5.mp4?token=CBU7xNxlukJGpF_kkj_n64plfvk4NPKY7NMs5NOfenXDOiMh78Sqxu53YlM_CaMpD5wt8CvktyPnrIjdtIl6uvIvSzKrG4pbIbuBBmInkUzPh90ggotkPumclDAxXLQtxJKDONjTCvuVnb36ccX6YRIMex7TjCG5kZ6J-0w6ovOSdqZqmkWYvIlYCIjnqgCjaHUooIaZJCUoOU5_WKU5HE7JdECbCZk1WB3RukgVdUTXgAxi-Gd-DWcedjlnfliRXF14Lc8zJi-SyjCBi5Mt9G45txxTQnW1sTeybEkay6m39LTzleXDDqsGTejBDhq7wyNJSCY0ae1n_N7c4mdJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08c86dfa5.mp4?token=CBU7xNxlukJGpF_kkj_n64plfvk4NPKY7NMs5NOfenXDOiMh78Sqxu53YlM_CaMpD5wt8CvktyPnrIjdtIl6uvIvSzKrG4pbIbuBBmInkUzPh90ggotkPumclDAxXLQtxJKDONjTCvuVnb36ccX6YRIMex7TjCG5kZ6J-0w6ovOSdqZqmkWYvIlYCIjnqgCjaHUooIaZJCUoOU5_WKU5HE7JdECbCZk1WB3RukgVdUTXgAxi-Gd-DWcedjlnfliRXF14Lc8zJi-SyjCBi5Mt9G45txxTQnW1sTeybEkay6m39LTzleXDDqsGTejBDhq7wyNJSCY0ae1n_N7c4mdJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تشن هجمات صاروخية ومسيرة على تجمعات المرتزقة في مدينة المخا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89975" target="_blank">📅 03:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89974" target="_blank">📅 03:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89973" target="_blank">📅 03:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89972" target="_blank">📅 03:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b73cba78.mp4?token=RBxrLc2MQ99WhQNjWFraduz1hwY_qKMiJZeTgCCSjsNQT3ZRZdxkDsdqYP_iahyevt0T-jl3lbs_DJdbHK1uPYUyDi89ikTBqECrRuTYFmYzJwypzpG1Bu02QT9b4pJv6ISo3sFnsTov2A1x5YTpznJ_bbekUQPzaTVrLIfO9sz-7kqRNy9N4Ibt2itVwzxPLOguI_rVJmYoah0tXTaGOrlWr27gf11iMp7HiRVUxHodNfoi4X6n-qIJa-Fq9VmPh4I-h5njU0rsgP96Jm8bivmXPy9-qS-enClCO14YQ3CtZ3mZARnfZ5AkipIzjULTXLci0Dt9VnIIj9-LP7AKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b73cba78.mp4?token=RBxrLc2MQ99WhQNjWFraduz1hwY_qKMiJZeTgCCSjsNQT3ZRZdxkDsdqYP_iahyevt0T-jl3lbs_DJdbHK1uPYUyDi89ikTBqECrRuTYFmYzJwypzpG1Bu02QT9b4pJv6ISo3sFnsTov2A1x5YTpznJ_bbekUQPzaTVrLIfO9sz-7kqRNy9N4Ibt2itVwzxPLOguI_rVJmYoah0tXTaGOrlWr27gf11iMp7HiRVUxHodNfoi4X6n-qIJa-Fq9VmPh4I-h5njU0rsgP96Jm8bivmXPy9-qS-enClCO14YQ3CtZ3mZARnfZ5AkipIzjULTXLci0Dt9VnIIj9-LP7AKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هجوم مسلح من قبل مجهولين يطال عجلة في محافظة ميسان جنوبي العراق؛ مقتل 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89971" target="_blank">📅 03:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b99828a1.mp4?token=uAtrKl-Oh72uYTn0jvCtS2kf9UEJi7qJDQM9G2kEVQo_3MTB1VtRyYmfgVg1uH5BUybfmGMHxg4Pkd2fUcLFCfCrQoyU-KU7B4jEcAI-vCB3GaiVBFf-g6y20dhV1DIvke6EzaLBkjx5yyMjaSRLfIJhLCqdbHYAiU54PNDqnZHFDjQJ_hfA1TgeA2dvCIbQ04ow1Ki-rZOM2OaJvolqerInAuGmay5de_Wvtx9AV-jw-zRWEjc4VPxvdzdnVsniJxQRREUxQFIn_eW4GuU671vXUHRfmYeAhl9RGITrMn7Dg3AsqYAYbItbiKHAlkZ1RTd-Xvyb9mKWoZwJG6absA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b99828a1.mp4?token=uAtrKl-Oh72uYTn0jvCtS2kf9UEJi7qJDQM9G2kEVQo_3MTB1VtRyYmfgVg1uH5BUybfmGMHxg4Pkd2fUcLFCfCrQoyU-KU7B4jEcAI-vCB3GaiVBFf-g6y20dhV1DIvke6EzaLBkjx5yyMjaSRLfIJhLCqdbHYAiU54PNDqnZHFDjQJ_hfA1TgeA2dvCIbQ04ow1Ki-rZOM2OaJvolqerInAuGmay5de_Wvtx9AV-jw-zRWEjc4VPxvdzdnVsniJxQRREUxQFIn_eW4GuU671vXUHRfmYeAhl9RGITrMn7Dg3AsqYAYbItbiKHAlkZ1RTd-Xvyb9mKWoZwJG6absA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الإمارات تلقي القبض على مرتزقة السعودية أثناء الهروب من المخا نحو عدن.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89970" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d8f857b.mp4?token=tXHIk8I0JVnqYYkU7B7WqxGV9PSpRQ8X0JMRFP6_nfQrxY6h2Wyavy6hWt4nLq_knjkoqD5F7431qrZiLxxo5Z1cyx9FVvCASgnXZyJfj6llBHIoQTeL2A5uiBtTIWK2G1v0of4019zpQ65E90AUtiGzSOUnb-SfP4x0cpbZe8NXjrBiYeqgPpyXGx8Ku8QDAGvCJ1JQ6xEQZwnVdbvWTFLoiTTSrXL3B6RRVMMRd1_UdWFdd_os_thMsLnlVxbMP3lPOCrNxefT9HVSMHcgXhxTRfAZ8m8LpS8gBVdsvC3yJh656CxeapCvm74xcV8_1VIb7adQaAEKQwspNWAUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d8f857b.mp4?token=tXHIk8I0JVnqYYkU7B7WqxGV9PSpRQ8X0JMRFP6_nfQrxY6h2Wyavy6hWt4nLq_knjkoqD5F7431qrZiLxxo5Z1cyx9FVvCASgnXZyJfj6llBHIoQTeL2A5uiBtTIWK2G1v0of4019zpQ65E90AUtiGzSOUnb-SfP4x0cpbZe8NXjrBiYeqgPpyXGx8Ku8QDAGvCJ1JQ6xEQZwnVdbvWTFLoiTTSrXL3B6RRVMMRd1_UdWFdd_os_thMsLnlVxbMP3lPOCrNxefT9HVSMHcgXhxTRfAZ8m8LpS8gBVdsvC3yJh656CxeapCvm74xcV8_1VIb7adQaAEKQwspNWAUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ياليتنا كنت معكم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89969" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJV5_OYUCMemKVNwzsMoxm9r74D62k-vUQAM2jzDFY8ID77ApvfAcaMM0gfGssBnjjQ6StraYCi6cTr0LVnIJHHAjmfpEIMqZpspGgveOtoWgjFGXm2gp4wdh5vGUBAwAK6nm7rQo5ZWDVpL_Be9WaVV5ZtNAfGKeN8_sK-H40M8avYNjrarg6b0IJZ_R2UQeltd9kAWRdvbHKz6OMfQodgA0YaUvh7sDiG0zYu5hEikOD8J23PxxL5mzX6UwliNq0c0e2mHZEkm0T6VDccLdYPg2b9KkEMxlMFiqzjvM2Xd9hrCzUn3sswV2l1mJbYEYYjRSZ6t5erhTKi3l9ezGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالة من الرعب يعيشها مرتزقة السعودية داخل مدينة المخا مع اقتراب انصار الله منها والبعض يبدأ بتسليم سلاحه للاستفادة من العفو الذي اعلنه الانصار</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89968" target="_blank">📅 03:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
🇸🇦
إنهيارات كبيرة في صفوف المرتزقة.. أحد مرتزقة السعودية بعد الهجوم الواسع للقوات اليمنية على مناطق الساحل الغربي، يصف مايجري لهم بالموت الأحمر.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89967" target="_blank">📅 02:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b27177a.mp4?token=Xx8Ak9jVqtoMgRAK3MK-X7ICXYBTBYljBrLNt56XKPOCfXOPWqUqLRM0Zq9U7SEMz4S2zeXSXPP59_8x48YWy08kRzZ5iH_m4AtdvO6svzHDgnPgXDsIjKVlOk_Q7XSOUPWTql9vpnUAuF5JPf59AQylFuNgY-doneQqia6AGryjGavgSdVbKW1RqfH92wYWkJvBmxy-_3fluBdzVKeMG2mMfnKlKkz19m5gWLNp1hzcXIRhioviQOo20MPYhb1CkxWDeCEuf3_qV4kDqrZT1QTN_DTTZMvgCKXz84zukiL80zSbkrivZy6MQPehGZtLGExWNnbs4m08Al4Zs2swVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b27177a.mp4?token=Xx8Ak9jVqtoMgRAK3MK-X7ICXYBTBYljBrLNt56XKPOCfXOPWqUqLRM0Zq9U7SEMz4S2zeXSXPP59_8x48YWy08kRzZ5iH_m4AtdvO6svzHDgnPgXDsIjKVlOk_Q7XSOUPWTql9vpnUAuF5JPf59AQylFuNgY-doneQqia6AGryjGavgSdVbKW1RqfH92wYWkJvBmxy-_3fluBdzVKeMG2mMfnKlKkz19m5gWLNp1hzcXIRhioviQOo20MPYhb1CkxWDeCEuf3_qV4kDqrZT1QTN_DTTZMvgCKXz84zukiL80zSbkrivZy6MQPehGZtLGExWNnbs4m08Al4Zs2swVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تبدأ بدخول جبل النار شرقي مدينة المخا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89966" target="_blank">📅 02:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تبدأ بدخول جبل النار شرقي مدينة المخا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89965" target="_blank">📅 02:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581883b196.mp4?token=YXU5W3vJrt9jdyqfH1-6QzjmSjSzT-DZkogP0E9CuFWW6mZlKYjEZpFI8yJQtt8nrPvBmjokivL76CkN4sHJG_5nu9Z6P4LIedJfVEgg45eFlukhd6ZNKWxJpVQl-wP_MfAHQC6HacPbIC29Ldo1l_RFITe3G2MP_wYcEL9ASHcDM-MuaRAK21o0BTa0EG1vtav_0ulvNNi9H9kY9V0XDvBINqYbThIGbn_Z7zKW2t60RvkPt53tPVel805FpjB-nvEFIzyX_PQ1RKKh1iTAG6fgTMoCqlT6fz0WIGiIe7nn3pyHR6TfiRcNqlMi1TJFqqyLpbW-V_evGV2uyn-Qeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581883b196.mp4?token=YXU5W3vJrt9jdyqfH1-6QzjmSjSzT-DZkogP0E9CuFWW6mZlKYjEZpFI8yJQtt8nrPvBmjokivL76CkN4sHJG_5nu9Z6P4LIedJfVEgg45eFlukhd6ZNKWxJpVQl-wP_MfAHQC6HacPbIC29Ldo1l_RFITe3G2MP_wYcEL9ASHcDM-MuaRAK21o0BTa0EG1vtav_0ulvNNi9H9kY9V0XDvBINqYbThIGbn_Z7zKW2t60RvkPt53tPVel805FpjB-nvEFIzyX_PQ1RKKh1iTAG6fgTMoCqlT6fz0WIGiIe7nn3pyHR6TfiRcNqlMi1TJFqqyLpbW-V_evGV2uyn-Qeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
العدو السعودي يشن ‏غارات جوية على محيط جبال النار شرقي مدينة المخا⁩ في محاولة لمنع تقدم القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89964" target="_blank">📅 02:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تحكم قبضتها على حيس وتواصل تقدمها باتجاه الساحل الغربي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89963" target="_blank">📅 02:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇸🇦
هروب جماعي لمرتزقة السعودية من مناطق واسعة في الساحل الغربي اليمني.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/89962" target="_blank">📅 02:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
مصدر لنايا:
اليوم أقيمت أولى جلسات المحكمة للمجاهد العراقي المختطف في أمريكا "محمدباقر السعدي" والذي أختطف في فترة سابقة أثناء تواجده في دولة تركيا؛ يذكر أن القوات الأمنية الأمريكية وفرت للمجاهد المختطف ظروف صعبة حيث منعت إيصال الطعام إليه لعدة أيام.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89961" target="_blank">📅 01:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
هجوم مسلح من قبل مجهولين يطال عجلة في محافظة ميسان جنوبي العراق؛ مقتل 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89960" target="_blank">📅 01:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز قاعدة الملك فهد الجوية في السعودية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89959" target="_blank">📅 01:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
بعد طرد مرتزقة السعودية.. رجال أبوجبريل يتمكنون من السيطرة والإنتشار في منطقة حيس اليمنية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89958" target="_blank">📅 01:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8933ee5aa.mp4?token=bYEgf4mL7NMoq3U6mH3hmDnPOLZG3AqzZeNeYb60SZA4UYfKseI5tV5bC7ltAB2KcFe1ndGsQozv2cXUy4oUBcGjn4mjVVtQkzVMN2q_LiO1S8We6wSD8aQLAGE8u9Klu7TG3jZ-jhZ5_svcR7kvx6i-l0TPcS2YWVMKw1AhrZ1AcLsOmCZql3nT1arkVWevpS9nKXZgznqE53RJpNefe_XJQWQ-ZBgaDByhSY3kjyH2TGbIgQ7PlZeTTH8sej5n86MJqVUwwh-Mweq8g84qu_6KWSo6_csokTvV05Hm8GuFJ-WwcGE5zxyLJ9YoEAJRjOhaZ6xrF5QOdVeuX_LMvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8933ee5aa.mp4?token=bYEgf4mL7NMoq3U6mH3hmDnPOLZG3AqzZeNeYb60SZA4UYfKseI5tV5bC7ltAB2KcFe1ndGsQozv2cXUy4oUBcGjn4mjVVtQkzVMN2q_LiO1S8We6wSD8aQLAGE8u9Klu7TG3jZ-jhZ5_svcR7kvx6i-l0TPcS2YWVMKw1AhrZ1AcLsOmCZql3nT1arkVWevpS9nKXZgznqE53RJpNefe_XJQWQ-ZBgaDByhSY3kjyH2TGbIgQ7PlZeTTH8sej5n86MJqVUwwh-Mweq8g84qu_6KWSo6_csokTvV05Hm8GuFJ-WwcGE5zxyLJ9YoEAJRjOhaZ6xrF5QOdVeuX_LMvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات اليمنية تحرر منطقة حيس من مرتزقة السعودية وتسيطر عليها بالكامل.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89957" target="_blank">📅 01:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سماع دوي انفجارات في سيريك والمناطق الساحلية من مدينة ميناب جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89956" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOYmFbfWgWDzhSPlcsiiu69QxzJ0gmhQEuwGpWEPRo741UgkaVs-cCiljqkdrxa0GeNb8NatVQQsqMWeXTAqjw9pmC56RnpWKeJVAl_pRrAnVT0n8zSUxJkhthkt-nJ9CuodQph2BlaDhZbKqGQUJS2q2TD3K0y5Gjd3mBKO7EdJ-rZS9kyki7SEc_iCRaYkbUgp2gvkoMfQjde4a-mo0DrUNwyr8Y_el9gQB_jSEc7-IEd0P9--V7x9BSzzCoZY1-c4zav9S3yppnS1geqTjzQ0XM0PaJMME9CrujtaB5CvMyU5fsPnxYVQ75y7yuWb5yyMig5Q7P6NnamFhi3RrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات اليمنية تحرر منطقة حيس من مرتزقة السعودية وتسيطر عليها بالكامل.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89955" target="_blank">📅 01:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي: تم تفعيل أنظمة الإنذار بشأن اختراق طائرات معادية في عدة مناطق في شمال البلاد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89954" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">طيران مسير يخترق شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89953" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طيران مسير يخترق شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89952" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سماع دوي انفجارات في سيريك والمناطق الساحلية من مدينة ميناب جنوبي إيران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89951" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عدوان سعودي على محافظة الجوف اليمنية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89950" target="_blank">📅 00:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">التلفزيون الإيراني: دوي انفجارات في جزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89949" target="_blank">📅 00:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">التلفزيون الإيراني: دوي انفجارات في جزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89948" target="_blank">📅 00:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط يصدر عفوا رئاسيا عن كل المخدوعين بجبهات الساحل الغربي لمن ألقى سلاحه وعاد إلى رشده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89947" target="_blank">📅 00:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
انفجارات تسمع في سيريك</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89946" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A80UpMDNw4wD61sM1Dw9MTc_GiWVD-Ai1a_dXApV4N5F5fIN9me0XaNZwQf42itlNbUEZRPC-s4V9S1ZpLnLjPq1hO9_u2dVnVFymaJ3gUXoFgvRlVXZ9p_3gDDjB3Zgt8XtIHC62ifEM473u8R5pQD3sL74_pCLEF9kl9kWrFXLEn4V9TZeKuvgO1IaydRtwXnmqf8ojGkTB9-mn2FCoImwXt1yvGRJPQkcGN0YHjbDpy68B52vZ7qqo1pU0lWYjbn5CGXkGkqNa82I627CDMY67x8Wg_Pn8o0cVo705UCDMF4XfJ83J2-TXL7PWQv2Ks4jgYT96CbYb5vIWrmRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية: الادعاءات الواردة في بيان جامعة الدول العربية تتعارض مع الواقع
وزارة الخارجية بجمهورية إيران الإسلامية، أصدرت بيانًا أدانت فيه بشدة ورفضت جميع الاتهامات والادعاءات الباطلة الواردة في البيان الختامي لاجتماع وزراء الخارجية في "جامعة الدول العربية" ضد البلاد.
أكدت جمهورية إيران الإسلامية، مع التأكيد على سيادتها المطلقة على الجزر الثلاث: أبو موسى، وتنب الكبير، وتنب الصغير، أن أي ادعاءات إقليمية في هذا الشأن لا تتمتع بأي شرعية قانونية أو تاريخية.
جاء في البيان أن أوجه عدم الاستقرار في المنطقة هي نتيجة للعدوان العسكري المباشر من قبل الولايات المتحدة وإسرائيل، وليس بسبب وجود إيران؛ وإيران دائمًا ما تؤكد على الأمن في الخليج العربي بالتعاون مع الدول الساحلية.
رفضت وزارة الخارجية الادعاءات بالتدخل في شؤون اليمن، وأكدت على ضرورة الحفاظ على وحدة وسلامة أراضي هذا البلد ودعم الحوارات اليمنية-اليمنية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89945" target="_blank">📅 23:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
🇮🇶
مصدر امني لنايا...
قوة أمنية كبيرة تنتشر داخل مدينة الصدر بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89944" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab93955bb.mp4?token=dzXZ2WeoVI_d-VlM-LDbs6ltqyBmZLkxr2b-lkR2S6fvWPbtkou1E0NdpMUXN8yNTfwBS8u3GFTrC8aH-ttBnuSStaWxx80AN-yAPONbgSy6j3SSyuuv3326nhK-OZo-2fkfPhfbqwdqNTsydT_kLa5kG_9tq2uBPmfhwJdCPOVHwAhU5AkSUnxfX6s3RZ2MaM5U3v6CojMXA39t2aZrqzrmTaovlvBoiloOyoZ0QvkFFtIZYgmN4YGs_eErkwA2NwY85ndR_Z1uD7_dQcc_4cUXytNpsXgJJKLZBSAOiy4ZxLo21lHksce7hHwah6WJuZxKX7LxRG8km8XOjMdPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab93955bb.mp4?token=dzXZ2WeoVI_d-VlM-LDbs6ltqyBmZLkxr2b-lkR2S6fvWPbtkou1E0NdpMUXN8yNTfwBS8u3GFTrC8aH-ttBnuSStaWxx80AN-yAPONbgSy6j3SSyuuv3326nhK-OZo-2fkfPhfbqwdqNTsydT_kLa5kG_9tq2uBPmfhwJdCPOVHwAhU5AkSUnxfX6s3RZ2MaM5U3v6CojMXA39t2aZrqzrmTaovlvBoiloOyoZ0QvkFFtIZYgmN4YGs_eErkwA2NwY85ndR_Z1uD7_dQcc_4cUXytNpsXgJJKLZBSAOiy4ZxLo21lHksce7hHwah6WJuZxKX7LxRG8km8XOjMdPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "أعتقد أن الحرب ستنتهي فورًا بعد الانتخابات. لأنهم لم يعودوا قادرين على الاستمرار. إنهم يائسون ويحاولون التأثير على الانتخابات."</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89943" target="_blank">📅 22:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c763a585fa.mp4?token=ox8UGbNaWBNSliFFG1rPwscv4YahdqM4ijrqh0lXwSI9qM_NzlChO_I0iJJV5R0kYCwmnoUGI3_SijAcDR_yiymH8AjKNNmRKk9bFhARXl3QxbOUAEmhLJiKfyHnhQzdPL0VeyzG2vn9FFPoveMFPuxmn-biiz2xgNCv8JLmAk_pStdpGGuALsqTUZ1yQZOl0H5uH_k1KfmFSxgjge7IMRfr1piS92e3_J2j7zt0qU0__D5IxPqW76ilmGv0qY4zYcbkcYA2MlSqVKWfZCb2-ZNoW-X9OeHcSwKa3Q59-iPfcWfbAdFTKwOzXYqAAS0Dc-frGGk03NGowUJqSnoN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c763a585fa.mp4?token=ox8UGbNaWBNSliFFG1rPwscv4YahdqM4ijrqh0lXwSI9qM_NzlChO_I0iJJV5R0kYCwmnoUGI3_SijAcDR_yiymH8AjKNNmRKk9bFhARXl3QxbOUAEmhLJiKfyHnhQzdPL0VeyzG2vn9FFPoveMFPuxmn-biiz2xgNCv8JLmAk_pStdpGGuALsqTUZ1yQZOl0H5uH_k1KfmFSxgjge7IMRfr1piS92e3_J2j7zt0qU0__D5IxPqW76ilmGv0qY4zYcbkcYA2MlSqVKWfZCb2-ZNoW-X9OeHcSwKa3Q59-iPfcWfbAdFTKwOzXYqAAS0Dc-frGGk03NGowUJqSnoN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول أسعار الوقود: لا يمكن أن نسمح لإيران بامتلاك أسلحة نووية، عد الانتخابات، ستنخفض أسعار النفط بشكل كبير.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89942" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b379fbf2a.mp4?token=vpJrHJWVTYhW0AWDWxNt-jWN4foVlvPzkTEEhuDdHRdCS0um6HVxBgdr5-ElwfzhZ285Egwcw3cBFayyXparGqvmvgozZ7EOYQm090MUjc4foAgvCoLvz3OEGheban4NBg0byaQpzs0eSSmMsssNr1tNxYbujiYXLFWhCqlEG9RT3KKTjf2lGgt8dvKnhioawgt4psADQazhmKD34I4x-8AoaM8pnBF0q_MVkydeZJMS8K-kdbDwJlo8P7YSd-Tk-TQM6KLd7B52J0oR_9nYz46DTD497bHqHd9SPoI-HEyAT6DDXwPg9gFHgpnlbEM7XrMr4z75d9MPXpKQAJy4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b379fbf2a.mp4?token=vpJrHJWVTYhW0AWDWxNt-jWN4foVlvPzkTEEhuDdHRdCS0um6HVxBgdr5-ElwfzhZ285Egwcw3cBFayyXparGqvmvgozZ7EOYQm090MUjc4foAgvCoLvz3OEGheban4NBg0byaQpzs0eSSmMsssNr1tNxYbujiYXLFWhCqlEG9RT3KKTjf2lGgt8dvKnhioawgt4psADQazhmKD34I4x-8AoaM8pnBF0q_MVkydeZJMS8K-kdbDwJlo8P7YSd-Tk-TQM6KLd7B52J0oR_9nYz46DTD497bHqHd9SPoI-HEyAT6DDXwPg9gFHgpnlbEM7XrMr4z75d9MPXpKQAJy4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول أسعار الوقود:
لا يمكن أن نسمح لإيران بامتلاك أسلحة نووية، عد الانتخابات، ستنخفض أسعار النفط بشكل كبير.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89941" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇮🇶
ماذا حدث في سمنان بايران   تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89940" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعترف:
انصار الله هاجموا الأربعاء مدن "خميس مشيط" و"أبها" و"جازان" السعودية بصواريخ باليستية وطائرات مسيّرة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89939" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03c8641d.mp4?token=ss_euObBAbWzOeTjU2AdNuZLSNJWefEOfNKdcdQ__cUSpn8ZnB7ev6EdNSAYh71MH5kyU-SOEEYNVN-LzTUhIVvQoF4cEGuF3xtVZRKIaj_kIU8O78cBjxV4ghz6v5H9xUiuTd3ORoGveIQq2tUo-UDAGRCeHZqrlTvROs08RJjSISSCSZZdUk8CYNg5kJdwm-ljbY4e5WN-JbsmfuRXt1EcSAR9NVBN8lKEqW8TpOQ2iDfegsrU54aCVPzZ2PWRX1AObXNwBggR_rqgqwe6ioWamIiVUSqD__jEPy6A9XQsue660YS8YxnoPAODoSdot4M56ruYjYKv0DusUqb9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03c8641d.mp4?token=ss_euObBAbWzOeTjU2AdNuZLSNJWefEOfNKdcdQ__cUSpn8ZnB7ev6EdNSAYh71MH5kyU-SOEEYNVN-LzTUhIVvQoF4cEGuF3xtVZRKIaj_kIU8O78cBjxV4ghz6v5H9xUiuTd3ORoGveIQq2tUo-UDAGRCeHZqrlTvROs08RJjSISSCSZZdUk8CYNg5kJdwm-ljbY4e5WN-JbsmfuRXt1EcSAR9NVBN8lKEqW8TpOQ2iDfegsrU54aCVPzZ2PWRX1AObXNwBggR_rqgqwe6ioWamIiVUSqD__jEPy6A9XQsue660YS8YxnoPAODoSdot4M56ruYjYKv0DusUqb9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني...
أصوات الانفجارات التي تُسمع في محافظة أربيل شمالي العراق تعود إلى إطلاق ألعاب نارية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89938" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
🇺🇦
رئيس وزراء النرويج:
طائرة زيلينسكي كادت تتعرض لضربة بطائرة مسيّرة أثناء توجهها إلى أوسلو.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89937" target="_blank">📅 21:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T40RcRI2wKB92B6ulKEbFk0Eve98jEFxqMwqHZe8F9Kg4a81WnQP-sHpkLTjJ7m96JhcRwygXM1tx0X-cBjK9q4k92u-9H75N80jK_LoqiA9fhk19G-NvSLV9etI3qOR5_GPPwUOyBJ709TY0Ku4DxdSU3QmTSsLF4W9nJyRtlem2jjO2NZYFFxgAuhxlRZUWkJL71Ga2FCg2iD26parUziZk6KIGT7poWWRhavnsg04PEksLm69to9Hb6ScN0Zy6SQJ1f5h7xvpWnkbfxIBFPveoCbs0jhIIVjfeqx-qwZfqouS7ZgqLi_dAWjkxbSjejhundbecTynXTIDEVfdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
شركة «أبل» تطلق هاتفها الجديد iPhone 18 Pro Max.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/89936" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
سمع صوت انفجار من البحر في جنوب مدينة جاسك</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89935" target="_blank">📅 19:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇷🇺
🇨🇳
🇮🇷
صوتت الصين وروسيا ضد الجهود المبذولة لممارسة الضغط على إيران في وكالة الطاقة الذرية الدولية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89934" target="_blank">📅 19:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29b3df097.mp4?token=txpahwEkP76MVWSuny6C3QOGPpFWyFEPZIdWAXXAcavHqOpeQ5VnBWbwhvdtRvx4Z6SFrnQeezL6kEa9mTNhYvIUDEFB0l_C69zqKX9ps1monn5sTHQejcM3IFojTZlqg-YHN9ZdF5EPvKHB0e6lrQwL9ErwD_rQ8sYsuULX8aystk0Ja3juH68K-SpLJEjSj93O3Sq5tQx5Dte9fyzB1Leo_WPEgcJM_p37PBVs8Ht2bb8umIpgX0VsFU-j8OpHqh8gEnnHtJlmoGziIbaFmLUlKWTVkTSEfMzmYdUgqqLVuAgPlbBSCsOeQnPLpxJN86qrNSwAgfK5xORbX1GvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29b3df097.mp4?token=txpahwEkP76MVWSuny6C3QOGPpFWyFEPZIdWAXXAcavHqOpeQ5VnBWbwhvdtRvx4Z6SFrnQeezL6kEa9mTNhYvIUDEFB0l_C69zqKX9ps1monn5sTHQejcM3IFojTZlqg-YHN9ZdF5EPvKHB0e6lrQwL9ErwD_rQ8sYsuULX8aystk0Ja3juH68K-SpLJEjSj93O3Sq5tQx5Dte9fyzB1Leo_WPEgcJM_p37PBVs8Ht2bb8umIpgX0VsFU-j8OpHqh8gEnnHtJlmoGziIbaFmLUlKWTVkTSEfMzmYdUgqqLVuAgPlbBSCsOeQnPLpxJN86qrNSwAgfK5xORbX1GvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راح اكبر مشچبي
🚀
#قريبا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89933" target="_blank">📅 19:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
وكالة معلومات الطاقة الأمريكية:
انخفضت صادرات النفط من ينبع في السعودية بنحو 50٪ في شهر أغسطس مقارنة بشهر يوليو، وذلك بسبب الاضطرابات التي شهدتها مضيق باب المندب.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89932" target="_blank">📅 19:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">القوات المسلحة اليمنية ‏تستهدف منطقة حيس بالصواريخ الباليستية والطائرات المسيرة</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89931" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار داخل مجمع السفارة الأميركية بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89930" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#وثائقي
«الثأر العراقي»
«ملحمة العراقيين في حرب رمضان: ما بين المعلن والخفي» تفاصيل تحت بند سمح الان بالنشر ..
🔻
إنتاج: مکتب الاعلام والعلاقات لحركة النجباء فی الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89929" target="_blank">📅 19:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇵🇰
وزير الدفاع الباكستاني يعرب للجمهورية الاسلامية الايرانية عن أمله في التوصل إلى حل دائم للقضايا بين السعودية واليمن.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89928" target="_blank">📅 19:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇾🇪
🇾🇪
على خلفية تواصل الضربات اليمنية على ارامكو..
بلومبرغ: شركة داو الأمريكية تدرس الانسحاب من شراكتها في مشروع أرامكو السعودية البالغة قيمته 20 مليار دولار.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89927" target="_blank">📅 18:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdafc6b1b9.mp4?token=Zmuos9VYy3bDAYH5hQVmbfLTrpZq05dHrqvDQ3030m1UK04WgoacsNP4810NlXAt8aDYcUPhiavC55BtIzmznZ0HzcwUIYTJ2qLM_QG5BGQjXhBEk95a0ic8MrJ5_-i8tu6F6INYi6EituSTk8Em8meYiFq2hd8A-7Z8jIXuVGnjgxtRImBmf-MfyJVDufnbxhBEiFbg8WHpmhz3Yf_aolLePf9S6aMeBPhpbjfa9TaKmYwrFm-2-R-H7B5K3DM_NQoyLrv9Pgb4bHxrlGs-v9ONri-_k4UIvbKk3NNoBuYMHcRVoKVuSUVejGV0GW1UHy-riIuykaArWReLYue1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdafc6b1b9.mp4?token=Zmuos9VYy3bDAYH5hQVmbfLTrpZq05dHrqvDQ3030m1UK04WgoacsNP4810NlXAt8aDYcUPhiavC55BtIzmznZ0HzcwUIYTJ2qLM_QG5BGQjXhBEk95a0ic8MrJ5_-i8tu6F6INYi6EituSTk8Em8meYiFq2hd8A-7Z8jIXuVGnjgxtRImBmf-MfyJVDufnbxhBEiFbg8WHpmhz3Yf_aolLePf9S6aMeBPhpbjfa9TaKmYwrFm-2-R-H7B5K3DM_NQoyLrv9Pgb4bHxrlGs-v9ONri-_k4UIvbKk3NNoBuYMHcRVoKVuSUVejGV0GW1UHy-riIuykaArWReLYue1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا:
رتل كبير للاحتلال الامريكي شوهد في قضاء الشرقاط ضمن محافظة صلاح الدين شمالي العراق ويتجه لجهة غير معروفة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89926" target="_blank">📅 18:21 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
