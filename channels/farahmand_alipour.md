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
<img src="https://cdn4.telesco.pe/file/YuffSiIJRxPQnemTXBhjKPPqlMtnMA7U45lbFksn5CRG5gkVF0l4Y0VMLzlLAzPjiLdAQdBLsRltrVDGyo6-X6j0KkDNJpm8O4XzLghknrILqVJbGDnVyFcbyPYfloji8m700-7jr-JH1R3v6Im5rpJIIpuYEgr1eMSvZ2iCadru761i_DLWDs9gf4_PgbTQajwy_BGkxUygrWokWfsyBJP6oOPaCNMggJFcoMovsSVpXvglycB7BWlXlOJiPLTjtSIZeXFuzBxoVN2KFtxHGWD3AfcbHR-PzKjKm0WvXRXO2myhGX9CzLDufetpoWVJqberjcMrulRy3rIW-eUQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 22:28:39</div>
<hr>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=fxY3sYIQnUGitJz9GluPireU255L2NQ1NQah29966T2l06jqbQZfJh1q_oItAyAxgonLs3lXzVnSuE2frDcV0C-0FnQEv6mgLcgjrBhzbWFenauE8CIh23Gl5KGx8Wwp7lBn3WbVINDcD2LC-RSMgXgCLABCoXAYCQ1bYn-Ub6WJrFwE-jzXaNK3I-dRa-nm7OyRjFeu5CKZOa-USszjuElSk_TFLTQVin648u9WDeS93Py5gOhISuQ6ClMBLCMChNRTC8Q9KsuejtvZ2EBoJFz24fmhpprl6-uIK-vEOAVLFuBjKE4-ERe2ZhMvDCdE6XC3pAlwvLqqUnS0Ch28IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=fxY3sYIQnUGitJz9GluPireU255L2NQ1NQah29966T2l06jqbQZfJh1q_oItAyAxgonLs3lXzVnSuE2frDcV0C-0FnQEv6mgLcgjrBhzbWFenauE8CIh23Gl5KGx8Wwp7lBn3WbVINDcD2LC-RSMgXgCLABCoXAYCQ1bYn-Ub6WJrFwE-jzXaNK3I-dRa-nm7OyRjFeu5CKZOa-USszjuElSk_TFLTQVin648u9WDeS93Py5gOhISuQ6ClMBLCMChNRTC8Q9KsuejtvZ2EBoJFz24fmhpprl6-uIK-vEOAVLFuBjKE4-ERe2ZhMvDCdE6XC3pAlwvLqqUnS0Ch28IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbqRS81I6dl_3R8TOESEgEtB_rCrtsKUtwXDFVV73iDIslQZxUyIf4G0wCD9TGWicMj5q5sU4zEYBFFgzI8_xahUghv8BhJB8LH-DFXQJiggGCJHJwzC3oRHVE0B8we9V-I4ldEs4IHtAqkXb_mL7HCkbfuteJGbq6LZPaerZix1QI0XcOuS51ttGllNE22LKZaKeVrQRnlK2pymDzIwkdPGeYVergoSrfis3khPYj-6hvMnGl3r4eHRmGTmNiph2HRKbvczAtsZdl2XJKK1bIJ3wJoXsa5hwHJSLYU7TzEtlQ_ptj4JVexp4DIrOPR4EpOSKwWi_ORx9OV2Lw83Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCifBJcmvWNzkkHO9bP26HCXu905TdnULK3CVRW5o1ir4phaa8OrmAhAPHtC4nqP1M63iL23yVWPVZ-tlbq8T-C0Jul5Jz6AKXEiyZugBJXWoNoFI8btuFlECWD4tNop4aOi8eoXhBtEp64qp3ZOlDWxoSeDO6XnUl_1F7T-D9Yc_P_hYpCJ6iNQ2CTYfRdTTUN_Q3lZ-ujUm86bLL8gyYBodr_lOg2JPxhUqc6VvRQP8dA0sjMDTIDaaQSJhI3Ccz9VAz93iPEkBwKV47cc_KTDnaXp90j3-zKCxENZdmBowXsoHBOhsmvk4B1e1kd7Zd5dym2-l1-6Nn0GSCdi6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=iBjPYP0URPrKZ1JcOluBUzaQ_7S0Scp2Au7zY0OV7b91KqHRF-1k_HuI0pLk9U-Zy5lnDl10bS8rW8XW0pSTQPxENnHJEZMyEDmhPfBGH_R-CVpIXA0bYjmcnq0ds2N3nTtJKoZ5Gjlnoj_DTS2_dHDF0UXu1NDWD_wjRb1kDW-3azOSsbbBPdYLNm4sc4Rw33RQK962GCILyI99BzGXEjALEmHnAdd2kttLVGZIS93MSMOrbbzEFloku2Yr_0nrhHGhJwjpRcePw4ucPpOMEBy3pzq1YDMkO_T26EuWDYWSrDCZYQxtld8N3s3g0QLIU93BsgSMQ36KRtS2Ombs7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=iBjPYP0URPrKZ1JcOluBUzaQ_7S0Scp2Au7zY0OV7b91KqHRF-1k_HuI0pLk9U-Zy5lnDl10bS8rW8XW0pSTQPxENnHJEZMyEDmhPfBGH_R-CVpIXA0bYjmcnq0ds2N3nTtJKoZ5Gjlnoj_DTS2_dHDF0UXu1NDWD_wjRb1kDW-3azOSsbbBPdYLNm4sc4Rw33RQK962GCILyI99BzGXEjALEmHnAdd2kttLVGZIS93MSMOrbbzEFloku2Yr_0nrhHGhJwjpRcePw4ucPpOMEBy3pzq1YDMkO_T26EuWDYWSrDCZYQxtld8N3s3g0QLIU93BsgSMQ36KRtS2Ombs7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=B5BwTY_vmvGhV0yNyI2nPPouF6Fp1jB9IdNN0nN3dOmlvBTRjvph3IaqHUA4ymtzPRM7YAkQXABPZHNTut-GauqQLfC3XFcVAKQlnPVQtDMwJRqloBQPcPBibE4UCHP1cA_gp63xsiFHDQ8bLN53DTd3eBpXtPMBwbOaTXDNHQ7m79BMgi3F5yZMNaQR3TvvhV08dm7jJcPkqRh-w1afR-VuyCoCwu3Ou5G9AjC6LAEy1Th7kEu7O314mqdRDwcdL2Ifu6Lu0sYEkk21qr_7ENjiB5KPrFyaLicHB230x661NtStJ6hd0L56JkOe762bO-IbTU07Agqj8fUQx_SIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=B5BwTY_vmvGhV0yNyI2nPPouF6Fp1jB9IdNN0nN3dOmlvBTRjvph3IaqHUA4ymtzPRM7YAkQXABPZHNTut-GauqQLfC3XFcVAKQlnPVQtDMwJRqloBQPcPBibE4UCHP1cA_gp63xsiFHDQ8bLN53DTd3eBpXtPMBwbOaTXDNHQ7m79BMgi3F5yZMNaQR3TvvhV08dm7jJcPkqRh-w1afR-VuyCoCwu3Ou5G9AjC6LAEy1Th7kEu7O314mqdRDwcdL2Ifu6Lu0sYEkk21qr_7ENjiB5KPrFyaLicHB230x661NtStJ6hd0L56JkOe762bO-IbTU07Agqj8fUQx_SIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=PwVIZeCuwabU8Gic8DBEQ-yzclXtpr9c6pBmDATeAgfSPrs8hwtD90kXcv3urWDOuIx3X1cx8BR29ep2BnjAZFevljaw4a_kBjaTEQoAMgjHAa9xIyIP6HQ1kmnrAE2gaDYIZNYkYQBB0deBCSYNnu4rW0T1YJrlCwkLyQuE22liIAw5ErGhABfPAdmTSvSNcCybDEJFanc76D6ifkfn4HKQ-t0CUswDBAjhqewb2wXln9fljr5T2ENeAddAI2wVw5PhXzlLyS6D_ANF4mcKIIZ4vd_rQX3rYilVs1iVWIaOAoAwz46-jOX3aC_DPZa_L2v3AyZ9rBHrmHhuykM4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=PwVIZeCuwabU8Gic8DBEQ-yzclXtpr9c6pBmDATeAgfSPrs8hwtD90kXcv3urWDOuIx3X1cx8BR29ep2BnjAZFevljaw4a_kBjaTEQoAMgjHAa9xIyIP6HQ1kmnrAE2gaDYIZNYkYQBB0deBCSYNnu4rW0T1YJrlCwkLyQuE22liIAw5ErGhABfPAdmTSvSNcCybDEJFanc76D6ifkfn4HKQ-t0CUswDBAjhqewb2wXln9fljr5T2ENeAddAI2wVw5PhXzlLyS6D_ANF4mcKIIZ4vd_rQX3rYilVs1iVWIaOAoAwz46-jOX3aC_DPZa_L2v3AyZ9rBHrmHhuykM4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KRkG0QcucR0MIfIjVoWjQZL4ea64ZU_RITlhcwtJwxus1NxfQo_eGShdZzbYGP3u-Cbdttcpgy9w-Of1b6wDUAjyy9Rg2VoO1uxWKSSq9mCRNl5lemMUtqjNqqxt2UExu0hb569orYJ3LPJBykmVOvDlAakkfBjHIxAZ8ba2TbHrClUzSr3RuuA23-prABlrfScad5U4wvkmrD2ZyH0np7nixKjltl6JLjkUUnKqdpAUKhi43tKUQI1XqRD6_4tWNrvFzgaxoCD5VXFZSlxxXuorCOakbb-W4DiOxvGP_QxDAIJ5ETXDfIkLmjN5EbmPsKnfEqbe3tqs3sTqu-Xcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KRkG0QcucR0MIfIjVoWjQZL4ea64ZU_RITlhcwtJwxus1NxfQo_eGShdZzbYGP3u-Cbdttcpgy9w-Of1b6wDUAjyy9Rg2VoO1uxWKSSq9mCRNl5lemMUtqjNqqxt2UExu0hb569orYJ3LPJBykmVOvDlAakkfBjHIxAZ8ba2TbHrClUzSr3RuuA23-prABlrfScad5U4wvkmrD2ZyH0np7nixKjltl6JLjkUUnKqdpAUKhi43tKUQI1XqRD6_4tWNrvFzgaxoCD5VXFZSlxxXuorCOakbb-W4DiOxvGP_QxDAIJ5ETXDfIkLmjN5EbmPsKnfEqbe3tqs3sTqu-Xcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Q8xfu240ZYM2JnmVRsVlb9oTvu9BkYcxJvoDVUc3w0mz7YUrqZETZtK3PHvz4dxzrz_Iq93-V1thC8_ksQJEjO3IztcL4qAlw9187f-7RIhia5bqzB7Gd31ZNagNodW_lxUbZHCEDEo_ThYJ857AAzgS7pihuqbU_6ZgiFMptwvPRwL2ylTMxUHvaUxo6ZyvIgVYEb098AqdblCfT6xNbF8IofeIMjL9JoHlCBC_-ETVy7qexl4QehsuEpLAyb3oT3SA7uR7gXAr7SCqH6w4cFvUC6P3URLFPpViNFnF7OrfcmndxyPI06li_EcVhypR9b3QFBIAKF9hs9DT5zdmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Q8xfu240ZYM2JnmVRsVlb9oTvu9BkYcxJvoDVUc3w0mz7YUrqZETZtK3PHvz4dxzrz_Iq93-V1thC8_ksQJEjO3IztcL4qAlw9187f-7RIhia5bqzB7Gd31ZNagNodW_lxUbZHCEDEo_ThYJ857AAzgS7pihuqbU_6ZgiFMptwvPRwL2ylTMxUHvaUxo6ZyvIgVYEb098AqdblCfT6xNbF8IofeIMjL9JoHlCBC_-ETVy7qexl4QehsuEpLAyb3oT3SA7uR7gXAr7SCqH6w4cFvUC6P3URLFPpViNFnF7OrfcmndxyPI06li_EcVhypR9b3QFBIAKF9hs9DT5zdmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R0Jtn8D8_5ueJPvtptqQP4CN1Z-DTJDvCzKitQ3PzSgb2lcm9Ug9WFjG2YlGx3kenvg1BHCy9rFBqPrt8aS-iEwp5HL2kvyqgWvBo0534haR6g1GIiJFhJJ1yL9hzJiebyzOZe-D_KyTK-0vWkOHVkJGKF3grnGvegVCu1VrNHFZfFr__iQteMTVN8_ptVB-lQOIR6s84Kl6i6rKTQJbjgAA_uNV8c6Q9D_eKt4CMCa5SofMl7gWokou_sx9GfKW2J2PaXjB5ZI04g7D_zK30WyGRJBBgkHhhO2GBUsWHgBDD2KeAswV_xAeHg7YoHGI3ZpkcIsSmTYwRuVMVMv_dH4EVJ2rf8MVmLW6DUSmAhTQXAJTsrNi8yCyfPDm3RGnwdPZOpCo0YSHXvLuQKoVICUL3NRabfKXRlefRw2n47scq_YddRPyqudz3xfTk2JZtOuRtvzTLalPO9NGfvTEAOw9IoBPnpwU7GoVvNEZNgFHqRa46c6auOktk9SYMaRXpAkOYTsCXKBZ7c7e_9ays6rb6Jn35HMQnjtiBs5wqrpHjq87r_MWm0oO8eN53fcPAh0Z5jaYw2Sd_w3DL4Xt15352xP3muegHNqOM4VtXWMe_Dg_KsxZzZlN1OzYrL7cHeA14ncjj_hncw0KmN-fugR35pb0QWhb9wKoHuRpjNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R0Jtn8D8_5ueJPvtptqQP4CN1Z-DTJDvCzKitQ3PzSgb2lcm9Ug9WFjG2YlGx3kenvg1BHCy9rFBqPrt8aS-iEwp5HL2kvyqgWvBo0534haR6g1GIiJFhJJ1yL9hzJiebyzOZe-D_KyTK-0vWkOHVkJGKF3grnGvegVCu1VrNHFZfFr__iQteMTVN8_ptVB-lQOIR6s84Kl6i6rKTQJbjgAA_uNV8c6Q9D_eKt4CMCa5SofMl7gWokou_sx9GfKW2J2PaXjB5ZI04g7D_zK30WyGRJBBgkHhhO2GBUsWHgBDD2KeAswV_xAeHg7YoHGI3ZpkcIsSmTYwRuVMVMv_dH4EVJ2rf8MVmLW6DUSmAhTQXAJTsrNi8yCyfPDm3RGnwdPZOpCo0YSHXvLuQKoVICUL3NRabfKXRlefRw2n47scq_YddRPyqudz3xfTk2JZtOuRtvzTLalPO9NGfvTEAOw9IoBPnpwU7GoVvNEZNgFHqRa46c6auOktk9SYMaRXpAkOYTsCXKBZ7c7e_9ays6rb6Jn35HMQnjtiBs5wqrpHjq87r_MWm0oO8eN53fcPAh0Z5jaYw2Sd_w3DL4Xt15352xP3muegHNqOM4VtXWMe_Dg_KsxZzZlN1OzYrL7cHeA14ncjj_hncw0KmN-fugR35pb0QWhb9wKoHuRpjNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CNhNpX85petd8WqXLOhXTy8iBI6sU1n_ftxm2GRZB6nlLvoDYlpReWEFJ9755i-eB9imhzc4brv86u9S0DtpTe7nr2cmY5A7RdFew02TvrfpUjelv-xJ_RVu39ENqzacI6aU_T0kIZ2Mm1hp2HePgl05hI3Ott6dpeRO7KUR8NXpOl--qiKrW4_hhtkUnq2aQec6sYIaX_v_9KIzrDzE6AzrSBUEoA2ydzeg1GzWC0kFPNzm5DQkxamnOZusJgEn8_2bx9AcLxgehiAoxQCVMajl4b-kHl1p3ff9_9CZWGkjOp3HAkq4MfhdRmAdn31FBaGdOa-iy811sfqZyi2vkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=CNhNpX85petd8WqXLOhXTy8iBI6sU1n_ftxm2GRZB6nlLvoDYlpReWEFJ9755i-eB9imhzc4brv86u9S0DtpTe7nr2cmY5A7RdFew02TvrfpUjelv-xJ_RVu39ENqzacI6aU_T0kIZ2Mm1hp2HePgl05hI3Ott6dpeRO7KUR8NXpOl--qiKrW4_hhtkUnq2aQec6sYIaX_v_9KIzrDzE6AzrSBUEoA2ydzeg1GzWC0kFPNzm5DQkxamnOZusJgEn8_2bx9AcLxgehiAoxQCVMajl4b-kHl1p3ff9_9CZWGkjOp3HAkq4MfhdRmAdn31FBaGdOa-iy811sfqZyi2vkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XpDEXwzxOLmmDGFTYqI5lNaDuA_xo4jooA1FPDVUufO4ZjcSGltl_m_8bk38zp0lahUDPDAD2ANmqjbScicDxk8zSkEwF7LejA_QpCnRMcgqLiomlZ2Ciy1kUgc5mOBCK9xhN5yHRXkXCIcF39IY7yVJi6RKHVcevmTSC5zS9dUo_HDXscUbEsLOHcUA7pEhGriVkHH6bpNIAlVG-nBXTjvc0sjWqNM8ivUgUBBFKCMKUHvMDBlA3fcaqageOMBDxIaqB014YjFHxm2_mZkqn5dDG8Skwc6-7VP4YUfaZBjoRgJeGO1iRb1vpabyFxJwZns4q11153VME3rI4zUgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XpDEXwzxOLmmDGFTYqI5lNaDuA_xo4jooA1FPDVUufO4ZjcSGltl_m_8bk38zp0lahUDPDAD2ANmqjbScicDxk8zSkEwF7LejA_QpCnRMcgqLiomlZ2Ciy1kUgc5mOBCK9xhN5yHRXkXCIcF39IY7yVJi6RKHVcevmTSC5zS9dUo_HDXscUbEsLOHcUA7pEhGriVkHH6bpNIAlVG-nBXTjvc0sjWqNM8ivUgUBBFKCMKUHvMDBlA3fcaqageOMBDxIaqB014YjFHxm2_mZkqn5dDG8Skwc6-7VP4YUfaZBjoRgJeGO1iRb1vpabyFxJwZns4q11153VME3rI4zUgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7tJQKsfI6_MXZ7UT-EjETQhYEE0onoNDBKwfpwi-kqYfaXtu_Tc5V4OGBx-1DBrfFnOzy2kcLDb9kAfMhemSjMBlr8a7owMTxYvMjDCitDL5BQVdkj_ixrVlxEW8g6_kOKw2d59K0PNmvddhxjhfFU7RycIk9QtZaw2Tzel_sj4VJDK_j6e2qlAbz9sKIFC6ln4H8x1nTbOL8DQU7PTQ_MaLL94MXf1RvLN3h8IhlLlCD17MUHhdqrBPaQ_ZasCWn19nofChmRGfDCZdf3CaRzbbTtX6yQsDe9hLozX3aMSMYqSskTzqmDDO3qpdF8Kp5jyr1NG4KKcWOzydrtlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNJalDL6SenRw0C4yCDZf0Lb-IUP15h5CuSyAMDiNBYgoDPYbJyhqgbO827HL1whhqERJ04mCtloliHQmg9bgwXq3iLnwx6zgFxodb0GZ4EbYJmXyaQZrTXhmafZQBhh35Q76wsmqVjTVVjlVVOMH5I0tJ5vs4gd6r7_vwaa79FJbNJzHlbbfERloY5gYo4riJzFYKzEh5eFMJqq_JC92bJmoux78C5s-8L10-PuFe4BsRvAEXxqjtf0wxNmsNawOdj68ceNdbAzk1EV_nbbBsfCgQSMq1PXX5yL2VPzYnPPeNsC0NWxZ85vGVtgLYOcywSkyVh51iOP8Zja6voE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WtX78rbdrEINybh2aR5z7dQ90BjbzW89tCGTSs72-Envw3pVRsm1YGteXMa1IWzKFx9ghgvCMpTD4Aovy3WgU6iZgiMb1g914huR_sOYtLhNU-7GPCid7oPZoUq32aIvVqbD0dkVTUAyKpmuE22klTlQ8dHQS4zRiUjEPQYfKndSflxeQq-gNzJSve31tFdlo0wSkE3wxeVbbRzOFkUazADk2LFxFcpn7c7dkOYJF4_tRN1GlVRT54qYkRboNYydBhnoM2t_KEhi3EOIlHD-owjeASdDGtdRj1IwrKZISWTGxELY7_hFxcMIEGEtKsJKsEhP0YlgJvtxwfiJbyG5Zxlt7StJ27LDjgJOrejgobc9-cL1ZX9PiJopqn8rSKj2VrorO39WcCnYveHppNymXlpGUBaKzZUcVH2IxBBMoFO6fgrGYQtgrU05FqswT5eM06sDo1K_7qHgVEJMnprrO7OI-QsrvHXma4LRqzbjEJ6Z_UTloa-CIhQw4Eb66s__pZyc5sOpOeTygoopKj0sSxmRbll2x4wFoEqft7xONhTCozGGg0P_epXRy3tUHKYK0Bc6vsxxPm0BVhqfyCi7Mmr7Q8-uuUjUZ3wKHYPE-Q1XSaDEB7lyYafoeWuzr-gpKVH4svHWrcnRnoZcOYBpoJiPXKCy5pAiITe9E_vL2SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WtX78rbdrEINybh2aR5z7dQ90BjbzW89tCGTSs72-Envw3pVRsm1YGteXMa1IWzKFx9ghgvCMpTD4Aovy3WgU6iZgiMb1g914huR_sOYtLhNU-7GPCid7oPZoUq32aIvVqbD0dkVTUAyKpmuE22klTlQ8dHQS4zRiUjEPQYfKndSflxeQq-gNzJSve31tFdlo0wSkE3wxeVbbRzOFkUazADk2LFxFcpn7c7dkOYJF4_tRN1GlVRT54qYkRboNYydBhnoM2t_KEhi3EOIlHD-owjeASdDGtdRj1IwrKZISWTGxELY7_hFxcMIEGEtKsJKsEhP0YlgJvtxwfiJbyG5Zxlt7StJ27LDjgJOrejgobc9-cL1ZX9PiJopqn8rSKj2VrorO39WcCnYveHppNymXlpGUBaKzZUcVH2IxBBMoFO6fgrGYQtgrU05FqswT5eM06sDo1K_7qHgVEJMnprrO7OI-QsrvHXma4LRqzbjEJ6Z_UTloa-CIhQw4Eb66s__pZyc5sOpOeTygoopKj0sSxmRbll2x4wFoEqft7xONhTCozGGg0P_epXRy3tUHKYK0Bc6vsxxPm0BVhqfyCi7Mmr7Q8-uuUjUZ3wKHYPE-Q1XSaDEB7lyYafoeWuzr-gpKVH4svHWrcnRnoZcOYBpoJiPXKCy5pAiITe9E_vL2SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7YqIBrLDmzMpeUtJJrrKkD9gjJJP5NXkZgYS0s5wxBn3y2kpkAfSjVNrqHpTvlAnFJGmn2d2hMPF_fnTXTTFLCdCZEX1hZnUpF8bUKHJXdjYKrShvuZo4oub5y6hhYbRHeXhEbdzapWRxNjuxv0L_g0bTnin3x2hs2_6Al4aJI8KwQt_-fSmiu3alYsSL19ZX80H1EarwaigQpSzUHAggypAOB5Y011sdmJXrVsg6883aUYY-pjbFHzZCofG9pZvWEgvW1ORQjkaEejuVQ5Dj-UuF8N6yZfckl_6oS46CXQVsUmwHSqlqUAU2RNxPBsmGkHkl2O8UIqnlEm6OiCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZvnAgvJiPgiB0E93keP_sKxzJBom55aHvmeqhkhPOYb3Zns73OLZ4hrDAa07rIxnVdvD_HJVk951L8-hzxZw_BvQzxCSRP0QF-F4HEFTHlmKDk1FFiC6_h6R45xZb1Z2eKCjVD0LK5hEB3Q1Fnsw3T84qATU4fwdEN0i9EbYHFJSAHrjLnNMrmiARp5d2h95dhqRp50fOjwYJF-0W2kB7G9k79Kg48I_CMckoEo0aliHLO30IJ0BjssopVfX3Rk-wzu6WcpNDYP5mCAhY0AaHomHRrKGpY8M7xdAV6AECmdh1TH-RQER93IwyytVCpsLSn8m4QS1_rD1sLUF2MCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8tGOBpBDRt23O4HJh7YaVZDW8hH28HcOPqYqO7RQkkokPEVg8zQfmUWgoh3jjMvLRn6qCKTU5oZBmgCMds6A1IaiO2ZjDDdBEAzMrqSRWBWI4vDTDsgZYPvOVJcVVM3wmFJSe1ysWPemrF6QSmpYAeflobKejts4ZbrFHyU8UPFJ72HzMkVGpy4gUw0paSexxYhsia3Ex3vPIwTDRm22vdFPfTb02sQdZ6Rrv6ksAwE_Of6h4hZGJcFXqGo7IFsQub-XHRkwzrk3qkUHY4jLCeiOz0IAielldxTgVlgcDmfwcUworm5E_FWi6VVrswmhbg9ieOJORVv4Sm_b0PcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPe5KlR_hY8H-um6AFxGaE_CKoOKEzAcp6BaBs6f2vdG6RKK8f_PwJk9sAEmsDCAJPROalpiVs1eD_GJiiVoEG98EkL1WIR9eIly-zpn-pezng1Aj_h7fn7qkz-kuemp4gdnMYozka5C8pRteKEhmmdZD_lOiCp2jIetr8y2ixB5B4bHB2lvG7AP13VSi90_p-wf7GqF7fYuQJr7vRhCEiyPLViq21Pi4fg3YFUHgFoh9fPqoNkvz5ZWO8X4HxZNsiSp-G4OU56TeM9V9EIZp3xqvQiEo9EER1rSvsxoUBt3tG_3oxaAjIKMKrxSWw7apFt3k7_TP-VQPMrQICbBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=hkfZNZhyfG6hYtKMv-AjT5s1yebpBxN8-V0Kk32zn4CmIv4uMeQxe2ySUoXBkM-HZbOeNf-0CVhyrr-BPsD09A6u-iapuNBvORnRenJ9Xw558xPa5Qk39ZrNuGZnNFcJIWVPHuxqB4QuxjIfHokrKpCbjwYiVRCKlHVt7fgfInalQZlQ5vbwQvUTsFzHAD329BditsLVl6u6dRWGAWZS4kUwh5jZWxk2jrKHfKVyRpqQFUK4DWZTcgY64lEEzWCHQYNULO_8T0PXkmIxzhA5_BI5yNU3BeMg6p_BihUA97HGJXVayIu6Lm5OHdG6N5jjgiqRTWp6UypnU-ZYGLgMAYTQ-7ky2-j-2KTMw56IEZlBuBPdWGhJpDTTZo7H98vcVcmj7IwWpE8uctV7SLTZXZQvfaOPeMhme-P7tGbUz-cxR8T1eWIRKZbVZb3it9JCmgjm7BwqzGleAuHVyifV2eI7BySbF1MfKYkCJTu3MedGN0WwtvuWh8mpe6lPkVX4SClhFn0TN4RS8xRKcidSse6kkx9rZvvKJjK3h7HtEQ69FkrNNs8_K2r_pTILPkGKNoNU92xO_3oLTGmUdCUbf41Bcrp2YhvxJQeXPAokWiIWKi-uhL7VCreXyvtYYfqrI62WpOdOLxnLoQw7spAkhpl0fycvO72UIAAovY61j6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=hkfZNZhyfG6hYtKMv-AjT5s1yebpBxN8-V0Kk32zn4CmIv4uMeQxe2ySUoXBkM-HZbOeNf-0CVhyrr-BPsD09A6u-iapuNBvORnRenJ9Xw558xPa5Qk39ZrNuGZnNFcJIWVPHuxqB4QuxjIfHokrKpCbjwYiVRCKlHVt7fgfInalQZlQ5vbwQvUTsFzHAD329BditsLVl6u6dRWGAWZS4kUwh5jZWxk2jrKHfKVyRpqQFUK4DWZTcgY64lEEzWCHQYNULO_8T0PXkmIxzhA5_BI5yNU3BeMg6p_BihUA97HGJXVayIu6Lm5OHdG6N5jjgiqRTWp6UypnU-ZYGLgMAYTQ-7ky2-j-2KTMw56IEZlBuBPdWGhJpDTTZo7H98vcVcmj7IwWpE8uctV7SLTZXZQvfaOPeMhme-P7tGbUz-cxR8T1eWIRKZbVZb3it9JCmgjm7BwqzGleAuHVyifV2eI7BySbF1MfKYkCJTu3MedGN0WwtvuWh8mpe6lPkVX4SClhFn0TN4RS8xRKcidSse6kkx9rZvvKJjK3h7HtEQ69FkrNNs8_K2r_pTILPkGKNoNU92xO_3oLTGmUdCUbf41Bcrp2YhvxJQeXPAokWiIWKi-uhL7VCreXyvtYYfqrI62WpOdOLxnLoQw7spAkhpl0fycvO72UIAAovY61j6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=PGZTKBJuUCEKWjcLxH3yHqwlWD93Z_Pm9oDCfYN6uai60j6YeN5rwMNuHC7wfGLyXjePrBUZ51YnmdBtFeoSiuMOOqVr5jIrPE4IYJGtgH99bUWsr65Fv_93ZGSTKkILfEDLxpduGay6xuOPBoEYrqJkQFVGrvRErz5yV_UzsM8ViMojRzBats7wB64Hkwac41eME96KqdQeM2CHnZywmuPKYE93oS4FzAFuqcnKfFLABm-WKkJhB4sUqRpK7xwhMtS_pb-eKnDLacdOjmGi_a8jzn5smlEEROuMokpy-jbfcfAnjGy1vNNIYlQNcR1vUPluB5Q031nnv9AyAZF_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=PGZTKBJuUCEKWjcLxH3yHqwlWD93Z_Pm9oDCfYN6uai60j6YeN5rwMNuHC7wfGLyXjePrBUZ51YnmdBtFeoSiuMOOqVr5jIrPE4IYJGtgH99bUWsr65Fv_93ZGSTKkILfEDLxpduGay6xuOPBoEYrqJkQFVGrvRErz5yV_UzsM8ViMojRzBats7wB64Hkwac41eME96KqdQeM2CHnZywmuPKYE93oS4FzAFuqcnKfFLABm-WKkJhB4sUqRpK7xwhMtS_pb-eKnDLacdOjmGi_a8jzn5smlEEROuMokpy-jbfcfAnjGy1vNNIYlQNcR1vUPluB5Q031nnv9AyAZF_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGfNSk1ReUlRY9YVNvd42rcGXKjIhsj9RkrE3BM0ptoe9OgD8xYtnpk55DbRKQtYk_lJaQhF99RKJd3yjvzMygnO7j5VjNjraAxNjDxhK1zwbo0cI80WaafgujqklB5o01Y0oy56HzMvi1CnzYq37L2enfdBMTaKcHKB9wsxZQQkWTmf6Phh5ayZRSkuOLswqfhbyPAicta-lrRdLhqHGPJ1_3MFBntE2WqSB_XUE3aipOGEg3ptXtrYxPVNuZuSOkJ7TZn46BuSGXBJxyni8of73WpMPCEGDcnUyzErNSMgq80eunZJEzhyru08bY7pxzcGJIGiJOSMw5e1sBfkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwNxaLYeZUbxZv7PaD5spNVsS6JEaRR5hTD4shCak_CoigrXE7LIz9TNt6PIxKtKSD2VpEJS1gKy_it-DizW5mkSLgVES1CkI1JZH5GbKvLrxmguMa1__EPrU2wzq3gUmfwOvHvQ91iB0zDEpLlEUrMTI-DF34DQHDoXOfHVnZq5Badf5xjBfzOdeGqO-BvF4k99kzLQbnWXKVjYegmMsNcD_xaF36T8ZCUOOZsxwnvYkUaCL5lKuFTK9S_7QRMsOGNZNcG7wuJerWhgMBnujWkcyGIR9hfC0VmRG8OP5DOUq2tsGGndlssJPxikwzMO70WS6Ie_-eTm988XwA3f-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nirB5df49sxsmVhyAjyjiEJkpBxk9xgpa5vVupZl6XElSci6PfdBVDH4X-KQ4hfGkAHnY6yxOru8JvF3NerZDnP4iTFhXtU7nRO8Cxwp5ujFcTigsjjqmoKN7Ap1FsmjKPfN_FwTU6MpRu66zAxd_umhvYWWvbLqEd4NmXJxBJllqcUPdEIA_iNodhtUl8YcD_8tx2Ru5bq-F25rxk3ntu68gPKfv3J858UYtHSJsBTCZptdDUQvkKeOeE9i4ejmtj5xS9vrLlRBVRX9XCvxFo1lwDcbxS6KBNDPqZjsb5bwAKvcYYwF2lzU4KFLeNXZET6hNSPeQfqQoibUO4oVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBFqJ3b3TCUWtvOP0toKxB3vK6AROCL-0QFKo2s_x4RSNiFhlCxQiwCV25AIb19mJ6Y_kjfZlWBeAltHNYH7y6nz4AG0WDfO0vvZsStEKuXwEAyH50fL-WSSDurXUrYvcVKfCtt3m2YHfNivEfB_ruBJX5f8aV38NF35UNWEEZ9ITIf5FJLcOROxLEGkjxpkWpcIbhuncxIs7P8_U1CuLjkqv_4df1ON9wGpZafxEc6b9QGfpMpz1R7Rjly0FdEpvnIQ0IRMTPcaSXffIXLqknPInnWzT-7t3eJFbVqMi2tbdvOauvf9XoV4bkFIMhhl9-oXyV95GuyhlGMXtgPjcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKa2Z5_Kcvoeu4aH8TQaQ-LqSJS3gmN7Fj0fFt3ZJc7cDBuyfZrtkiKzndaILgY4uPC0Vc6eDHMSkDB0lZER0JP-ZJiRcQYZbKa-HR35mFpjXd8HQH3fYMDxLlvlad72ytNPqGmX8pLKdOwi82PJA3oebjYky7Jux89emeEBzY3OLsTvL1LagEzamuAhqzANEUkJtUi8uU98zrdYc6nfXpGfJmY6wL4C_R1EVCbVX990efadvnhhOA2-GGKORbX2WMXKkQvNcOGrMvVkoa_86taVo9-_jWX6fexP8lB8cBfy2qVeh8QemiF-EPmnz31z2UXMURMqh4U2GJTsIKxcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWs5b06WnYELyNLi5GNQBUvRuxa7WaoQYvnCV0_pNMtYROaVBKbqxkrJVRJX12Omd23cITTsWA1v7eMgqZ8mAxJTuQI07zwV18Flu5_IVbDTQYHoBL-RO64aBinbxRORsZDBQdn2dNenbaiNKwUWSnScV_10rLqJP9uePrNn61UnZGA-fHbR-URugl51uudLkUqhejRp-pSYGlwGw5Zpd_AlfjLOLvjuTuWqFZ3gY-SDEWnInLx_4r-hnKcayubrUO-lreAmDiLImHpIPQ-p1I7725u9kjCliwPXCDSExlhfi3EavuQo3tEwLzeSaGggH9QHVlXSCfD9Q2FxBxytCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1pU8MgWPBG8bMq-VxIwP36bdiW2SvwcaetmY43tHbL4efj8cfhQVGt_9HZmoQMHXKUhiTo_v6tMW5kJFmsIsY6V0rZuX4ZMSmEWb1bas1YDCBAEFH_OfjYBt8K2Nq_SxO8sdpCXwNYlbsPQRZG72oqPt2vaASH6lWLZ0pFgp9lhZoodEkbk5tGBoNJD0mUdEL7MF3UOHVm1lxtWWqOMhZW2PTeae6dNkZJrBNtqVMt9wNkpVFArRYx4aKcGfK1c0GPXbP68RXde4GC8SSoVJK7T_crLtuw_h3mS7uvMMoE5kxiDuSA7QlYDM0R4DCaiHIjY3AnWgu4PVXKVn33z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=GzifHpbiK1Upy2KiCKDmzIogYhYKO1kTfebPTrKfIlhvM2hZy4e2vRMDgJU97oMiyqCecQQ1d056bC7FFl_6EqRP29ocvHKcl6mGW-LHG9jLn_RpSboIlwFuRWlq9H4O-03BZs0rLiKXNTxIDhFmowKDX48wO913qE5uLjm1NDYBnbys40dGuOkJ-fn8-r4GCkPRbAvyKlC5oU05iekJme2V-uRhp06VHu9w18GKoXSbNFTbN8TGPrZ6xsG6XOyXuhWMrsE-XpWhZIzSNZYEwvWnh4XUMzs1V4i9aF-VvFEBLTvy1dO9xSIvdLbO9NXP1pTj43CUDv40DxoXGHn9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=GzifHpbiK1Upy2KiCKDmzIogYhYKO1kTfebPTrKfIlhvM2hZy4e2vRMDgJU97oMiyqCecQQ1d056bC7FFl_6EqRP29ocvHKcl6mGW-LHG9jLn_RpSboIlwFuRWlq9H4O-03BZs0rLiKXNTxIDhFmowKDX48wO913qE5uLjm1NDYBnbys40dGuOkJ-fn8-r4GCkPRbAvyKlC5oU05iekJme2V-uRhp06VHu9w18GKoXSbNFTbN8TGPrZ6xsG6XOyXuhWMrsE-XpWhZIzSNZYEwvWnh4XUMzs1V4i9aF-VvFEBLTvy1dO9xSIvdLbO9NXP1pTj43CUDv40DxoXGHn9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aynUsCvoStup9Vli_xrlibvyf-YbYIyeTZEU1pzneijvWVt4K4cX9BXehetlLoKlEqb7hsacX-y61Gx0CUX80Anh-cMGII-t9H3fGCEX2e_vG533ayesZ4-oiH7Uw_8sGTdFy79OyOAUbkKmpe4fw2dbM6zlxW0ZqCy9bLkO8RkddFbiWhJjIw5uUNu4U_s43IzTGEoW7YAA-SJbc7RRTjqUCb5ATj3GcIzPvUlJxmIIeAtK3Kt_PxMp2Dikp_cxdGYMAso0JCYmoKT3nMDIDjW4AVLrIf2Dmu392gaYeO0frIRbSFfAlOyNhoKmbLWBgwcHZmpe6smKzezzbWN97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=cr08PFC0ss5epr5a7O2UnugIpyxupBgEDxtVB8oJS0fNjeI5wuQQGf6pjPP3w3phNSHOoQsqT_ov4T_24U900hjtw0f4YRnbAHzefs2z0N0k36fffO1FlqqsHDzvljilwcDw4MAnA8p-gW06DSuGopMEQl3h1_q0OZay-J1EfZHkgbgpOrlTeFHKeiTzMleJEHiQCX1BR4BzJqVqny8PO1IBkCk9ZQnbFOMrb8hmZQ7ndCk9ev5I6HbtpjGwbI4ASL5Sc8vLpBDQgDNkgxRUfJkDai89sVaf9BV8-L2hcyk_8OQLAFDXniTvuE5qoRtaVkQXmtotBp0ij5jND5SQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=cr08PFC0ss5epr5a7O2UnugIpyxupBgEDxtVB8oJS0fNjeI5wuQQGf6pjPP3w3phNSHOoQsqT_ov4T_24U900hjtw0f4YRnbAHzefs2z0N0k36fffO1FlqqsHDzvljilwcDw4MAnA8p-gW06DSuGopMEQl3h1_q0OZay-J1EfZHkgbgpOrlTeFHKeiTzMleJEHiQCX1BR4BzJqVqny8PO1IBkCk9ZQnbFOMrb8hmZQ7ndCk9ev5I6HbtpjGwbI4ASL5Sc8vLpBDQgDNkgxRUfJkDai89sVaf9BV8-L2hcyk_8OQLAFDXniTvuE5qoRtaVkQXmtotBp0ij5jND5SQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t34Dmr6JCsc2LQcoLxfrPHXp3kojGWpK-2gcM3EA61ikFWVdBhCc9pZbt7tjhxson4IGYKOBL4-R40MUmAuKoenfWULTXD-joXiBozJRBbcj2TJqW95B_UomwaMSJdfB5wo2e-32g7epZL2jxp3uqLFLLhkIsd4BEPgvlN-IjRdX-VYt2eYVP43KwBlMG8Iovdoz943gn9bBX-Xs6UAKHa03uqYdDuqHfNP8SleGklmG9Fjhyy4Tb6tmKJh2TtJ-GVBeT8X9exOde8s4GaROPo5LLAtpVej8DLmC6jXpUvC_iorFtvVV-2iGM3MzEN_u48UwAwgW3SKQSM8xuxwYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBnQGuyqHIMfUYIVS7QnVqSgu_MwwjZRvZ-8E9Z_Ym9Vbz0GPqon3QwlJHJRa_kYYOGsozA2GN-m_b8QVGVPZweLf2XXU03tnZjhH9JCxqDcdPsK6K-X1Ryr_i00Wl00eWlWskVo7D3sepm_M7M_d6fJfjj66NwFly66VQXzv9mUjo52RD0KLOo55kMhapD1QfDG3-jDz6Pi5mb7BTuUgMv33ca0gHkPcTU7zSP322CltMz39-z4n7juprXjgCFWYtzoFogbS7JAhN5Tt0UJOdJ8OEioaAOJZrq2ao4eZd6luSdzhIAkk6bcWdiMS21jZucoT7p25eUMxzC-EoVo1JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBnQGuyqHIMfUYIVS7QnVqSgu_MwwjZRvZ-8E9Z_Ym9Vbz0GPqon3QwlJHJRa_kYYOGsozA2GN-m_b8QVGVPZweLf2XXU03tnZjhH9JCxqDcdPsK6K-X1Ryr_i00Wl00eWlWskVo7D3sepm_M7M_d6fJfjj66NwFly66VQXzv9mUjo52RD0KLOo55kMhapD1QfDG3-jDz6Pi5mb7BTuUgMv33ca0gHkPcTU7zSP322CltMz39-z4n7juprXjgCFWYtzoFogbS7JAhN5Tt0UJOdJ8OEioaAOJZrq2ao4eZd6luSdzhIAkk6bcWdiMS21jZucoT7p25eUMxzC-EoVo1JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=bpu_ZgmGJV_72qdtTEyczzKIhGnWeWhcZ0dzIsUPXLZccGfplV5tCfMM9Wwwc8Y5PMucEqsYB7r0zjfgriQWg0AeuyA7RHJsBVIiTnoUh686V6Ge7C7ACF57fEnFklyMzwgzS0vdDN2sn9AT05eF1cmsYerNG4fzOMcCaZyZJMw8c1iJE_uph6i_ZnDLSATLTyPyZXs3iziDU8JValJcXsMVnWxawjfv6_JTymRBopEjqJTi_STcWEfeKDa3eUB_EMHt7jAj2fh_pZVNh2NE_RsR4lIu783Bc-_Qfy2b_vW8kTaKFWhrYyQiyjH0pUa5VK5nTeunyLWtPp8xxpjqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=bpu_ZgmGJV_72qdtTEyczzKIhGnWeWhcZ0dzIsUPXLZccGfplV5tCfMM9Wwwc8Y5PMucEqsYB7r0zjfgriQWg0AeuyA7RHJsBVIiTnoUh686V6Ge7C7ACF57fEnFklyMzwgzS0vdDN2sn9AT05eF1cmsYerNG4fzOMcCaZyZJMw8c1iJE_uph6i_ZnDLSATLTyPyZXs3iziDU8JValJcXsMVnWxawjfv6_JTymRBopEjqJTi_STcWEfeKDa3eUB_EMHt7jAj2fh_pZVNh2NE_RsR4lIu783Bc-_Qfy2b_vW8kTaKFWhrYyQiyjH0pUa5VK5nTeunyLWtPp8xxpjqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BQLoLjklgzUvbVWP7bMtKjw1gkpbgse3-Yq7AUmxeU4WC7Bw1UXWx_7k6axMcB-37_D5mwkb5jpHdNhNmEKg6oD_0XmHMTCMqSioJm8Z4NC3xyaupkdAxV4NxL5R8xXayV5HR35Ckzhxs2ArKqdhfyJoi50M_6lTbBIfjrANIQksdD_qaNFe8vlsLBPSYxtouLX_Tbi-m_EXechzRztvE7VOmEWoBg6gbJ6YZjeJGfa_5Z1BgTaasQpkGdWVUbqLT1oDL09NPHq0Fa5TcEUdqFRKKK3hkE2puW9GlI5UplYDOdNrIge9TTJQDSq65xF6lmCjG9nNcapNtJ9rnTflOfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BQLoLjklgzUvbVWP7bMtKjw1gkpbgse3-Yq7AUmxeU4WC7Bw1UXWx_7k6axMcB-37_D5mwkb5jpHdNhNmEKg6oD_0XmHMTCMqSioJm8Z4NC3xyaupkdAxV4NxL5R8xXayV5HR35Ckzhxs2ArKqdhfyJoi50M_6lTbBIfjrANIQksdD_qaNFe8vlsLBPSYxtouLX_Tbi-m_EXechzRztvE7VOmEWoBg6gbJ6YZjeJGfa_5Z1BgTaasQpkGdWVUbqLT1oDL09NPHq0Fa5TcEUdqFRKKK3hkE2puW9GlI5UplYDOdNrIge9TTJQDSq65xF6lmCjG9nNcapNtJ9rnTflOfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qurni1KbAp5T7hM0FOPbiVv8A5O_vj5xD7KyCzWLjkn4q572fhhw0TrxP9y6gimAMzhPrAyp-r3E6n7v3kJ6g2iwelvpKlI29x-Bb5ckOwLf4uHsOmyqmtQ6NMG6U1OxIyW35HSUgAAGvZ9LEnQ03DICi1iRTLEw84qlglhT869UT5iQMLvvB6AieL7OZGV3UUUgmv3yo24lZ7worlSD7SipioxbiIo94voa8TomHOSYNf_D9WNqv5e0XcOsYteGSRivQq1kWyqWuEwmb-9EKGOSMI0Z94WUfpP_gOotFuwxGrxWULS_cgKpy09OYqI9Cs77ytxWBQKQPGA0apuWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4tPm_b_tTupNf-8A8Ld2cxRPIZMhOR8GeLQmFD73P0ZiwOjF6s7uNdqxKJ4NWM19hDql7pXfMGU3M6WVZ_mSEaTmExxa3lN7eUyFLYK9zZbRtScIbLTO822bk2AFOOfijUJQ4xp7QbHw65do0sxvKmuNPQUql2Alh9SYMTu2vbuoISxIUU1duKR327gTw6whl650l0I7CPdRB2mfyHib8DCKufC8ELc06UWHQKYq-QMBwq94wp-KeWGuK_2M9kUABsPA_ATwetULbm8W17crFjGOhRn169yxojTbxPIuZMrDxTspLYyFGgeZMn1m8zSLFa4MltcJO21IZ0f8MkAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsiSwqUPxt0UP_-b9eD8iKA-QR1DUq9RItJOPVrcgmk6QtaUUettuSyjhECOHTMNqiNP3wtSROBMgw0e6FsncYd5Rw1hXAWjVzY2KH8EZC3qB0z0xHKjIylVTRnwYvVPCuxR1_aoPIos2xVNX6mP_Hb2PnwHPewidcN3JJE-8qKhhrTF4Jkmze_IHuA_rBrRLt6yJPTASRB4qaJeXE8ZeRBhZr-aaTpiZ5dow8lORw90cB4DWrb-sLmasGrWpkG5Je_t871AmYFaCcwbOdUlViEt9MTxq6dyhCkd3_PHGZeZtbFgZXX6HEkp6dEBjdejPercrlDweZKjhmoBaYKdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMAPzwtRbnY7NG5GD4BKQ49z-0-oJ6db69sSvFnL_gVMTPw_ZCJJHr73XjvTx6XgqX4GWNfNfcjTxfcdsj0EcpA1GBNH7Q99rySpNDYM-7ORBiA2vud3JBiIPs32smHzah_BZVq472Mg7hmzLT4IxhDVgzs68c7yeNRDmOZ1yIVoB-yz2AhvM1Hez0N4zZTHvL6YUdKxxd5O-YHyILdLPcU7TqGsydx-Unqzq9iRD2_tNiera06BsHX35vztLQ0lzPVj4LLA7HE9FDNZEl7RDIqgbreKsXL7L1J1be8lBiX4w4UXGFFQA_ysxaIjUPSOaxey8L53kYaGck9RyGne3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADS9tc2v9k5ZbOTZTaWmk37vWsgb8EKkAaexbPtK_-FQ95kmFABOpYC5HPyU7qvZc7ES4fDxUlqdsy25Mb6WTHhpa5AlHaYIN7gbXtSyZYDEoXiNDkBcTQ6DLz285T-lhrtEqf9K3WZYu82JQAaJ_Vbzjp_T1feU2gemhfRtdYVlXA5v-JiOKkhFxHaftEYvpwBH0A3VmFcbzIDG_f1uluSdLzV011KWIohJ508EzmocZmNsebl0MRNCDi15URfUZg4-D2Rr07fnEqkTOKbA-oAjBZe3zeWLQOYzuvH8kzMg7WA1di3ANAcjJO0CeLhJ6VOFklY6-vAgX2pjawctVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBXMcTS392YXQjRM8JV1fcmZ_ziB0PYdvzlie0j_T9AdaF1_MJ4DUlv8OhXuokbytKA7dDtq2-J2-qzmxfigWqFyoRoGkQCGrUuxgHqKhupl78pC1Zlm20nzN39R6hvF_6e5cbiyX7hXn6yPN-9tm2LEhCEM736WS1FQmpqWq0dpw1n5pGEFeTuXhrcKlF5U-GUGkWLQUz5Fd5NbCUyDHCAkfeg0pU4Lx_TGiOewuKhdKbsZ4MKYbB2L4BI0rB07QIOR1I-oEP_M0_PCfWL8H_6q-4p0sciq-5egPZi2EM-yzJHYbG5wY5dkXl8IqOEkxjUEiqo6k9LCjAkId3anQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaRfvPQxLaAr2ryFTC2dS7tJFE-0V0zQEp66IaVDyVBK6s1x245EtAfqB35UJU5gp1tMQvmqHc3AFDu0K_oA7oi54y0OtXNScxgV4BEwkofSmYo6mwbBBI7nZIYx1QNIQVPI8ZOjaJoA4Ut7qRq2FmbHwfBl-tMTTLITGXyQ7RkgfI_TRHJmV5lpP06EA56uGkOgaFJRB2Xrbppj6QtMr5s9q7JD2NCloiA9YjJjzxbt76DxASl7GOQZ_jBf-CPZWHGIgP1jsY5G_gHazAiJHpBQzlgn-6kFGyth2ahsZvMFKL0za0oolM3XzsLOry3Sv4Ebq7RBti63X0Hp_YXqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJbqMrV2Vnp35IJ6WayhQ_qCpIg6NA_h7llboA6Bc3ozH1tMvbxrhwIh7Iplje4OEDBIewZ2FPY5Aj0krD_6csO1ImKEtcS6S9T1SDB_C2DmmTNTeFkIB_s_2DdlAXGRurgfOI8IH-EC23EiWMiNxpAurykacD-SvXLPPCMElvmZGAC33otxW8qsETvQq0epsNlVY8LIdpHjRHcLqCiFXpw1Z04jPKhlQv4GDVelgMV69N9zy6Xnfq1vKtfe5CaaWArSI6ISdPuPDpZPj_M2nW3o1Tg8jdY_cEW9xuHcIJ4FKnlYcrkdyCpdIN3W0JAM3nkI8K8UiPTBp6RPFe6WWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJZUXmuZI_vhK3jA-ndG85RjarXU8VH63K1blZxkzGkmbAYzIiHSEJCpkFbUc9TRJKQI0mB04w1vqPMni7TX9X8UXYVoLHwxeewMopLRKMsrcu5h0w3c6zCvDnOZfTvwhYayFfaQRNKHB0uY-KD-TEst6pkJtsOZFkIWxMCQcnQjNflZ70wjMUVoUw3xu7q0KzHNxh6m5imhqW5ZVYpnVVsAROYnLCJZAsHL97ZKFzGRhYBARETgRcW3zV2ELwQF9CPqbzLVzdwmH-6LmCr-f_Sd-B5J-03tiFseTtjFXC8mSDjlLUpE3dZXHHsUFKAk8I3NqjgZHTZztDjC1aQR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCpjXmbdAEFrkAz9m-Zl68DICGyR1_ZnXd2ljLPtHrXpz8ox8lib7n2t9coHPvd8lZMrINb4W4I1Vg94PDW80ApVP3vT4CScJKVS2kfqR-8NPf1bwQ-wr3ynDPKXNBWgE_x8BFbXYV-ZyHVN2JbKDbDW5RSSNdKM8NjXDGjdVibktUhYjuLMm1UER-V5bMTQ4JFpFbENRBRYWl8wvSnKSK1jKVTWz4dnzdilcUiYP0wjZHHMz7MunfPl-A5BONKHZAe5yXSZDxDY9sI3ppAWttRvRNmoB6GQNls2ABTWwcsClYdoOG0O_nIJ-lOLnqILBmf450vuq1l5g2UCUHTrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTNPAjlzTGj1M6eBKWDQEGMMCOPPt0R6k6uq7AvQMFz5KRpfDiwMJegNfNlcoBZc_iN5m0I1LDr_xRqAHpNjF3Mzz3zswmAravnAXg3wFqTDnINO7kAtPBzJmHbNWPMBh-7EWz6dkVHYEzOu4cEYoCEI4L0nNokAyO-jey2OwNMrNAs0Ej0rIzDCuf8a-Pf7rB-rvwwtstDN-RLRQ3hJvqCWPoH1iNF7LS6NL7pLCQzOD89xsmYVKvhtmlVMWVaHlUn4DoNbRGDkBfMIiJmHL4bdnN4Sw1gQ34muXQqMz-rHzYXit2QL-ARdlpc3fe_sH4CWsGVZTwfekHGYKCpFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWCWlpFQMh5PUXJ94q7QozzlBJlHgdgEgNAEXEW8jBoApcI4ID6bJe1GGknXX5t1kcAadAz2zb-BGjDvbU3t-6Nto4LO66rNvKFhOjGw2aNSkc-nMlw0UoPjfk_PxDOkKg_MAJKNYbYevOLtxKJHaI8o8vvD3cERFc_0-jSZwvtD5-qybyKoguNIgds1fTSv0VMV4X4_PkW6IOckmkxwgl0F6eTky1xL-Qmp1exc0LYKSXgwGaarxagzO3ui1PvphAj-nN-MWKY0lmtUm5wkyRvLAi2oUnolDrOnpqChLtFyLKPFYzBwa7YzzDsk2zEBOZS3pzqM0asT8pyt9LAkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMJGJD__Bpbs96kwM7KBQkMGpSlOa-pojoV72vLG5lBYyiUH7jH2ceNzvvgG9zAYHlnXmvChIXcSUqU11qBdUXbkosUGTfU3YifDAeGXCogdQEF8y-gs10NAkrE-Z9xzdy8d-olfmHT2GH9R5uQdtmHkhV2tUq3CEB--kgh49_9GvbCEMXOdc7BKrxcl7rqDqN6at_cf7gNouSS4RRI5E9gYO20qwsI-pPGkTyVthY_seS9YlTgCZ2-UjGawJtugUMyVkdJLwKCWvr-81boZUwq4JY9by3_vm6ql4sEzzN74z7n1rOTu6FTlgBgGRyLHluozpQRVg_Ey13JQgxucJW2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMJGJD__Bpbs96kwM7KBQkMGpSlOa-pojoV72vLG5lBYyiUH7jH2ceNzvvgG9zAYHlnXmvChIXcSUqU11qBdUXbkosUGTfU3YifDAeGXCogdQEF8y-gs10NAkrE-Z9xzdy8d-olfmHT2GH9R5uQdtmHkhV2tUq3CEB--kgh49_9GvbCEMXOdc7BKrxcl7rqDqN6at_cf7gNouSS4RRI5E9gYO20qwsI-pPGkTyVthY_seS9YlTgCZ2-UjGawJtugUMyVkdJLwKCWvr-81boZUwq4JY9by3_vm6ql4sEzzN74z7n1rOTu6FTlgBgGRyLHluozpQRVg_Ey13JQgxucJW2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
