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
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 02:24:02</div>
<hr>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsuMVwbycOVcKxuIsl8NhNoah4C8Lf-fvDjm9Qx_apRKyHEmvAOY39Pg_XtQb1s0Satath6r65ylCGxZ0Epe7_A3YyqakeYvcaNRozmd-hDudHiUXQRKs1VL0pCMueM9rAIHksMWSYN7-rYaqPGiaRYgXmVuLk8iRkye2Zv-ySE90tEjfd82Nc_I_suh4lAZd8Y0O4CvgtAWQsRiYXGALnytfvYIkHBZObGkDGHWta2AkziBjcfS4twnE6A-rCgYSZiCWLNL5r70ggzVB2fJ8frEXWYv9IBkZL1kJsacTZCGSp4ReGAROkc3slwLZO96LRaYHpJpCi7kGWhGmtir6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk6fphPF7k3GAXKniH27qXUdVZijx136CtDbuOAq0OBZEl9OeXV1Pszr9daS0G2CH7aZMkw5Cn2ftqgqBFI4q-_pniyjcykRvEc8RCyseJZt_rivU95z_joaDJA0kSXzjWWE9MuOV2ynElWJp4Nw8b_BGD5hicnT5klD_szuGWAqr7L56R5zdYGVTgfaADOXjoigXBmPO5uG6VRKYmg7RH6f8epGoGniHMmvlhFXEywxgpwsyrqOk05qGkmW_rwSb1hgG3VWuh5Eai26eQP9fdm5OHFXZDucPZf6pPOeVTO9aTzm4LdEq0YgJGlz7G47N41UbH4QlR1inWtAc3eCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6brwnxT1KHRZ1oIIDlge8EKLDpyqE-k5ojbhuIWve_P1e2hOaIzxcKxiYFp5t_FKUWpDK93JPKxmsD2f9k6VpK0Q7ylFw4QKPoUsrx-RBwlbZBCg6iQgc3XcKEm8V3dgdsKMgySEi-Vgl8_Gz5C3LGc4A6HOSH8Uir-6h76-9Ds_MNPGVJfsmqXiQUQ5oU1dH6VVKyHmgEuX0F475bYz31iR3JP6LKP2_6sp5s1CgrKDRB9XR2UOxtOPswelfiiWpcM5ZEy8OSMjEXVagRH0O2IvzOrA63mfo2StM3Rg5GiLMqgPOXybErSYq0CYEWR5g6WEXZRhoC95X2JTmjGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=NpsOrkHhLId6WrzLPIaTn9R5Bzc1MXHlA0o25toRQDE-tdPsTNL4S1PW97N31Uz2T7gnllzKw8BnVRSB-wSlW9pdLAIP0pfO61jnj8YOwXwgDPS-csc6VxuX2UiHQGekLZXb_zbxXdz6VhCefpSpJsn59X8FKsu50gHX0ZetvE1pPs4MtjGkUGIL6nO6fP4t5BGrv8lazKHqWEuqNvsOxgH7aP27qu16hJZfxWCTCd0v6g8io5WAu5J7G_aeDTxanitAdhqR_-6EHdXqA3_zGOks50nI5Jfjxhrarvwgs9jdxl1WYla-aK_Drgahw5n_fPDu7z2-9MprlaKZNzLQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=NpsOrkHhLId6WrzLPIaTn9R5Bzc1MXHlA0o25toRQDE-tdPsTNL4S1PW97N31Uz2T7gnllzKw8BnVRSB-wSlW9pdLAIP0pfO61jnj8YOwXwgDPS-csc6VxuX2UiHQGekLZXb_zbxXdz6VhCefpSpJsn59X8FKsu50gHX0ZetvE1pPs4MtjGkUGIL6nO6fP4t5BGrv8lazKHqWEuqNvsOxgH7aP27qu16hJZfxWCTCd0v6g8io5WAu5J7G_aeDTxanitAdhqR_-6EHdXqA3_zGOks50nI5Jfjxhrarvwgs9jdxl1WYla-aK_Drgahw5n_fPDu7z2-9MprlaKZNzLQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=FDhka07Yw7ba_Px9xtaNN5IxGTJ5AYpa9pwHk0g9Y5gmRNHtr0fXjkhJgRkEk0T53ICWxfWPgh9kxASkeSqirPXz7l3xpYAZaJvjIiBPSu71iU5QuneEJInXtvnGrY17ncJxY-u_MQ42dqlqTJ5gU75K8lDHjUm6bXNa1apJTuTnEjBvK6KUPxZBf8z_dATDVg0U6dl8_Nl5JdlYV7n-5Gz5bS7J4OL5Pa6TKlRgM8gxrUhSBxbFaIsyFTXkbSjT3hB5W4OA1szeUV8FbKaRo36vP8MjUyVohaRqHEVIq7NBpw5cUnwV1JH7ByjrjWNaq3gZ9mL766sIjAfDJuKsVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=FDhka07Yw7ba_Px9xtaNN5IxGTJ5AYpa9pwHk0g9Y5gmRNHtr0fXjkhJgRkEk0T53ICWxfWPgh9kxASkeSqirPXz7l3xpYAZaJvjIiBPSu71iU5QuneEJInXtvnGrY17ncJxY-u_MQ42dqlqTJ5gU75K8lDHjUm6bXNa1apJTuTnEjBvK6KUPxZBf8z_dATDVg0U6dl8_Nl5JdlYV7n-5Gz5bS7J4OL5Pa6TKlRgM8gxrUhSBxbFaIsyFTXkbSjT3hB5W4OA1szeUV8FbKaRo36vP8MjUyVohaRqHEVIq7NBpw5cUnwV1JH7ByjrjWNaq3gZ9mL766sIjAfDJuKsVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=QP4u0GGh_esgs89ia2to3tAMHxvkeZ92d29XjOLH3lvtOaktR6__MzS0mvvgaooy1CK9tsj4kTu08dccsa4UxSIFPCtcGsPIGYsKmC_B1tS1cxT5bZIMm7Oi6ZRA9QA8Ra1IFNMymKA0DKTvbTQoCr8MPkpRAR3f_3s8OmCiyzohxtBaH7fOdQ7GtyvLm1C5hGQSe2syvnal0T787e9_W_2AHpLnBGj1zimV0hoZm6NexmO3PklS705EK-SqhHqWfdP_SIYxpow5ANyEL_33RVG8OT154doZDvK07a2r3Qto-Czl6mJIb2H0ZVp_X9LFv1ei3-bIuiPYKyyy1Q6gS5pu06ybQcLS8MwzNSOrIT3GGuPP2QeC3crybxGEjS_2hdUzm1EPz3LM2m4h3DR0cFyB65YvUNub_RmnPH2nPr-al9XxKHXMBWro8ffB350Oj4ppIfXGRAsKLDuzVb2GGkEt81Wk66YSW4iZI_y8cbQD28qeu29j5oPIUvGVW15gqgvXpID84Y-7gO6q43fNbnIRKupAsG01XTVdEgZ80YfEBmIuETQpPS8QA37CSR8TvEvZtMrvoammd5nj2SVednE1gKouL4x3lbVK1NCbXvh5tQ7Wej2OUsKEZkEHNp3x661CkUaJQjDIa3sF7-4T2mImxW5YO_yGv7Ui3cTO11M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=QP4u0GGh_esgs89ia2to3tAMHxvkeZ92d29XjOLH3lvtOaktR6__MzS0mvvgaooy1CK9tsj4kTu08dccsa4UxSIFPCtcGsPIGYsKmC_B1tS1cxT5bZIMm7Oi6ZRA9QA8Ra1IFNMymKA0DKTvbTQoCr8MPkpRAR3f_3s8OmCiyzohxtBaH7fOdQ7GtyvLm1C5hGQSe2syvnal0T787e9_W_2AHpLnBGj1zimV0hoZm6NexmO3PklS705EK-SqhHqWfdP_SIYxpow5ANyEL_33RVG8OT154doZDvK07a2r3Qto-Czl6mJIb2H0ZVp_X9LFv1ei3-bIuiPYKyyy1Q6gS5pu06ybQcLS8MwzNSOrIT3GGuPP2QeC3crybxGEjS_2hdUzm1EPz3LM2m4h3DR0cFyB65YvUNub_RmnPH2nPr-al9XxKHXMBWro8ffB350Oj4ppIfXGRAsKLDuzVb2GGkEt81Wk66YSW4iZI_y8cbQD28qeu29j5oPIUvGVW15gqgvXpID84Y-7gO6q43fNbnIRKupAsG01XTVdEgZ80YfEBmIuETQpPS8QA37CSR8TvEvZtMrvoammd5nj2SVednE1gKouL4x3lbVK1NCbXvh5tQ7Wej2OUsKEZkEHNp3x661CkUaJQjDIa3sF7-4T2mImxW5YO_yGv7Ui3cTO11M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=albaARGDr9MhOa8NNUjwho7k4J2ZV7tytk_uR3-VaaWPDu9DdGH4OGBgunKIgBsIXSaRPqMvedubnZXkq-3cinew6MwiljyH27_ZNmWdAfE8noe2aBgqS-uW0cEJtM6GTRn6wUGtGsfWxn1vDyBSOFp0py0uOlvYFG7hsfXfFJ_qYUN5yzzUu4rIlSehWwg64LFRoaU3NOdo-65qYW4630yY8M_xcZ-5lyb19DDMIYcvoQaZ-Z0U86F4btL265UW4R4vP7Hx7C0GLQmhyCFBiFoIXVlAKEEgxeM7aRNiqAuSheMavoYmnRlFWudAVVi6LIdpG8r44iaHLvDpcE_N_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=albaARGDr9MhOa8NNUjwho7k4J2ZV7tytk_uR3-VaaWPDu9DdGH4OGBgunKIgBsIXSaRPqMvedubnZXkq-3cinew6MwiljyH27_ZNmWdAfE8noe2aBgqS-uW0cEJtM6GTRn6wUGtGsfWxn1vDyBSOFp0py0uOlvYFG7hsfXfFJ_qYUN5yzzUu4rIlSehWwg64LFRoaU3NOdo-65qYW4630yY8M_xcZ-5lyb19DDMIYcvoQaZ-Z0U86F4btL265UW4R4vP7Hx7C0GLQmhyCFBiFoIXVlAKEEgxeM7aRNiqAuSheMavoYmnRlFWudAVVi6LIdpG8r44iaHLvDpcE_N_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=oV90wpUwlnX7REgk0nivDjP0Ekb7KqbUu2nVVEsL5pvq7DAsiqA7KBeCw1KKCY4FxlFBO_zhN0TOgPNjH8yi2RJcoeoeF62l660orL7G_JrWL2OWa4sTM2v2SxzG7tbOqdPoYfzKPlW35MepJ4J8jyl_3fPAn-GbB61txjkcYay3i8VQ2cHMj5GruLAlHvIbzW51k-hdvsqkcJ-MkAdhatDVIKlUb5sBxCEnrL_p8AHqVFyX4GVdcF5alpLxXL2vLY3FC0XZE1618fBJFPBtcoTStxEsvbwDXLQCode287fK6R-wL6AtoaRq0PDhzVSF92bu8EvefxmBNQkZ0gaVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=oV90wpUwlnX7REgk0nivDjP0Ekb7KqbUu2nVVEsL5pvq7DAsiqA7KBeCw1KKCY4FxlFBO_zhN0TOgPNjH8yi2RJcoeoeF62l660orL7G_JrWL2OWa4sTM2v2SxzG7tbOqdPoYfzKPlW35MepJ4J8jyl_3fPAn-GbB61txjkcYay3i8VQ2cHMj5GruLAlHvIbzW51k-hdvsqkcJ-MkAdhatDVIKlUb5sBxCEnrL_p8AHqVFyX4GVdcF5alpLxXL2vLY3FC0XZE1618fBJFPBtcoTStxEsvbwDXLQCode287fK6R-wL6AtoaRq0PDhzVSF92bu8EvefxmBNQkZ0gaVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYEbrPDASk0_yM0O7MKeCGB8P5lNf_UavqZzFPJnOcpz236tVO4taop9I8RRJtOSsgBWtzyu4UfKw9Vw2q4QVX-bk1dCQNnNF2ODns9VFjQ0u8_Zu6P2LVeut88YEcW2Cu9fTmSk9YO_n8gtZi2egFP-sznv0QYhcq0geiWotR2T9YflvRDHxLfovtH-dm2TnYC9zVDLM5vVAf_rtViHFLzx4G5QlivLomCwcbR4fuMpyI2E21pj2zRUqsK_SzC_40abJ79XIy1ibNWDsdh3kT17ZDYc2o8hIXUrmrHM5cbudeBaeK3bzAeY2UZi8cd5GyodxQc1EuZ_SI_HrigFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNHJBkk5TMH3XQaR9bg-mymnLFPyNqofrG0Cf9xNgWal85uQsyf9rAPpX7AqnIrqAA1eykw-G1T9gKbTD8RfMeKw2dp82-1XpzzHVs6tzi4HWdsNKVDtU3M73WbSWF2PhU9mtOY050uSorCTQQRYnzULVGlm56OFM82P3ZQRZ8q4exgQJQLt94wE0QntyGjCRsb8aiCAa77L9N4Z54Ave3rO7MzPVjzzSCAm_lRC4HIC9YMy05S3rf51-yGcDbXogy7FyIqEMKarLuqfP5p0M3FuFuFTmrYS67Pm3m6BQWlbIuusfTh26dfQzqJmkJO6vYLAX2d9pMgOzSPhQhlpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=LO5pjx4hVSTB0OlnZ-MfAXj3AoAPi6yQueU8hiqfGYIHxBviOAz5N8BhFrqi61wS2OZuZJK0G5118oVUeQ0E1QEtWu8QVgVnSdn632JtunWttNg1yprFXgmO1Mbyj56_vioLPhaVuk3HStSQTtZ-eG8AQ4xosICB0TKcFNSjYnkwNeJEaMlOF8bNiVMVVchra0aDj4LatdrchF9rcSRRu9q3lKNgo2mR_xPzrt5M_3ZeVq_HmWd1Jqx2O7QhEFYWOmLbre8UN9fVLZJOzlqa5-3QWXU9m1mxe-xnPKy2F0PvL9Mlor1mVeZ4-xjcf9z9kTmwlZbDZWQ8dJ8x9g8-uD_RS10vByjfA6Eh2MVhYLi6sX6Ojw-LBRjiVkGsyrMoM4dbNpyZIs_xlaW6ziZWsIk0Ol3CxmHyR0IhtF62DFL5Ov3uh-fH7LYMrl0b3wIxdmvOFNooiaTYJbCzCzfxBtQy6ARd-ymvflHt071SbGRTW5mLa5jzu-q-YJ5WPygEarMTy_g7Gi7ChC3Q9IHssE-kJKP-iL8OnYlg-tsJx7c6hOs3kZszs-h98tB4nNjtJWUJhXo1CIlEpdxbs_Ys3xNtKG2wd9q68Jgn7DSf_nBYhTUDuxmPlNw8_sGDwcG5BhxxBMReQXtVsgPb7q76Esra7OUZioU-3d7C9iWNp3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=LO5pjx4hVSTB0OlnZ-MfAXj3AoAPi6yQueU8hiqfGYIHxBviOAz5N8BhFrqi61wS2OZuZJK0G5118oVUeQ0E1QEtWu8QVgVnSdn632JtunWttNg1yprFXgmO1Mbyj56_vioLPhaVuk3HStSQTtZ-eG8AQ4xosICB0TKcFNSjYnkwNeJEaMlOF8bNiVMVVchra0aDj4LatdrchF9rcSRRu9q3lKNgo2mR_xPzrt5M_3ZeVq_HmWd1Jqx2O7QhEFYWOmLbre8UN9fVLZJOzlqa5-3QWXU9m1mxe-xnPKy2F0PvL9Mlor1mVeZ4-xjcf9z9kTmwlZbDZWQ8dJ8x9g8-uD_RS10vByjfA6Eh2MVhYLi6sX6Ojw-LBRjiVkGsyrMoM4dbNpyZIs_xlaW6ziZWsIk0Ol3CxmHyR0IhtF62DFL5Ov3uh-fH7LYMrl0b3wIxdmvOFNooiaTYJbCzCzfxBtQy6ARd-ymvflHt071SbGRTW5mLa5jzu-q-YJ5WPygEarMTy_g7Gi7ChC3Q9IHssE-kJKP-iL8OnYlg-tsJx7c6hOs3kZszs-h98tB4nNjtJWUJhXo1CIlEpdxbs_Ys3xNtKG2wd9q68Jgn7DSf_nBYhTUDuxmPlNw8_sGDwcG5BhxxBMReQXtVsgPb7q76Esra7OUZioU-3d7C9iWNp3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqv5r6M-fA8v93AWTFBt5-fuzjSgw2QZ-W5k6YOAeUNAyH-UxnyGJ5LcwWzRoK9JLhrjhHorITBoWq5zeB3oWO6_8sN4cnkGAWf9CXikve7eVDSmIlfxRlacLJOfEJxvIqW5c_9ZiznlOT3c7BQe_qab4KT5kR_9VcsfDluViZ81fFM66D2WI6lOICB1QnLidvFungJoJ113DdraC7dE2daVjIPpCxDFivFu81O9lAOyWYlym0UFeOoI98XIZsAJb7HLcFo5c7jp5RNKNB3UWOmhTqWmF--jfkYkJ7Io514GAWE0mSIXxCbTwhomiBaemqR-hc103OEBYaJwx6yGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NstiRBNr6vcF5YI0yjpyBoP9P8_OD3kMGoxWnT81UJbkCCuDs7i_78eRKh9DwIwIY7HgoKc-Czs5zrc6WntKaUzL8s5pBnQcV9JFW_VKFUJw4Zf7Aqt6W9HeIHKoXUVeUDc8AapiluLJfRA18g4wOVB7a5xBle33gULk-jlxkujH8W5JdfGVQscEc0pNKEN62LnILZRXSmuJvJR5SpHb5WDOR2Ecjqt6gu8sb72-q3be1dw8mmXeCQBtTzs8LOjbLUyniPyqL8AwJuLeklbrNld5oUrxu9KP4wc82DGkXNOfB-yZ9B7is5g-LxI38e43sXKqi6xTY-u7jv-2IzrWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyRT4cbrswyh5LDrQy2g687y43P6ILQugxTmPSBrwWGTINJQjxDBWST2FJV2h2bqhxE7Xw9OiGu32VShiA-9ym8C6bABIriEm8-_qQT3aMuj-DLNRQ-dsl2pX4EZtqHCKCVFgYonzPG4IasTlFRYIEc1kKD8vTHRigHJKfnvKw0SHqi_atx6exquCHYvaQu7hYWJ-N01jhUdUmjuMcwk4d411DXYIK2sCtHWIrHj6EIQg43tgEluTM_FIqk3oSklsBIaTUUfPTqwi23x-9SJs7iQ2tCsb8rhqzaRSFuJK1WX3nGs_ZZp502lQITdCjzwvDxqaaERRDlonyzIO07rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_3QIxECkOXoweECMRV2Bjxbe8Wr5LDsy1EOyBPMvLBkbRH0H0UVR8juS3OlmxDSp3ILprZo8oj9dCr2kvXHkwm_kQieq1Nx2I3zcbXhVVUyy12ckwRpIzNr9mX5_XUSGAyfYG7If2dXDnERN0hjJtjpq1mdIIn4Jo_4y7KwfzVBjLXdjT_lGaQd9ucWvcihtcwEm8bEEbOXL5piBZ4YCLjT5rTDG0aq2zD8BAMv3hd9Lpj-WuWAUqGrjxMQnepN2QNbqIbkI2R_pScIyEDkgwu5jsDrHvvWDB7S0GYfqxO_siB1pDsE237k0v6gzHT30dnbEvK4oKyomg58TJGupQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=UqX3rnTyIp9IQcaOpr0nygc__45ei1czU9KKG3rvGNtcy0AIawvJ65FHZlQyjt9DQcM85Bo5z_fXcz9PJaT2cpeQGw-0nSgEjAOGt5BmhBd9DY_NMGHZhtMBObtC19V6cv5vb1e_xPSf1AnJzmwHsSPl_CVTVJUXaXk8cn4QBXE36URlUHqbsDXsQVsHIDmLKuUVXbZm_rTBEkdLb2JMAGYDBT1Tt8erL3C86wT3pnuY64SjkLjjBgXDeTw8Re7SNkj0alc3-A6x9PLne8amn1E3ygrdfhYCqA7blWp9bYh98XY4-Z0Mc3c_Top08OTeXM0O-4Q9f_9RHxoPCyfK5gNAx9Ry9WdTgNUGwdLXbDzwr2nboYIMecmb9KLjmLE_gBwfmYRL__4ZfOpgi_q1YkGwZaXkh9s9U2MqbwDOiKSUIsGuJnAPgnwluYM-Y49PRN45RIcc8G2UWR2ZiiNbKt43ueWVqCsxN1Cq-rdgHeKKLJpbCbNH5Z6BMAP5QuOPs5s2OTIO9gBIIT_PNnUq0u3qSLaE4-e29rEWr3FIsUFDkBn-wyI9s_riH3Oe1rG1uVBV_Om2z4Egwe68h89nJjaJ3vx2sLmZiU_AzQuOTJ5VYX5GGZhLid4AiHKW1rx9yAlBywRPSe4C1hAPQnlmdXvjJQQuAJJ4NJcRX5GNNpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=UqX3rnTyIp9IQcaOpr0nygc__45ei1czU9KKG3rvGNtcy0AIawvJ65FHZlQyjt9DQcM85Bo5z_fXcz9PJaT2cpeQGw-0nSgEjAOGt5BmhBd9DY_NMGHZhtMBObtC19V6cv5vb1e_xPSf1AnJzmwHsSPl_CVTVJUXaXk8cn4QBXE36URlUHqbsDXsQVsHIDmLKuUVXbZm_rTBEkdLb2JMAGYDBT1Tt8erL3C86wT3pnuY64SjkLjjBgXDeTw8Re7SNkj0alc3-A6x9PLne8amn1E3ygrdfhYCqA7blWp9bYh98XY4-Z0Mc3c_Top08OTeXM0O-4Q9f_9RHxoPCyfK5gNAx9Ry9WdTgNUGwdLXbDzwr2nboYIMecmb9KLjmLE_gBwfmYRL__4ZfOpgi_q1YkGwZaXkh9s9U2MqbwDOiKSUIsGuJnAPgnwluYM-Y49PRN45RIcc8G2UWR2ZiiNbKt43ueWVqCsxN1Cq-rdgHeKKLJpbCbNH5Z6BMAP5QuOPs5s2OTIO9gBIIT_PNnUq0u3qSLaE4-e29rEWr3FIsUFDkBn-wyI9s_riH3Oe1rG1uVBV_Om2z4Egwe68h89nJjaJ3vx2sLmZiU_AzQuOTJ5VYX5GGZhLid4AiHKW1rx9yAlBywRPSe4C1hAPQnlmdXvjJQQuAJJ4NJcRX5GNNpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=noEnKieLz9AJ_aETZffXeDyoOntHnSL-EC-BDN8YDGp7c-J5-teF_oavPhOE9WFEDo7uoLN_J0zSUmdVdjHF7fG0yrBiqG7CUHTlwnfb3vkIAxD3pKSVB5j_SCuFWjGsPnCEYjK5xc0mRDK3IYfdLwmKWtPXn4V5MXEDnspZqrUUjCR2TV6vYH8GF2wjOSiQ_O1LqQ2Go-WuOlMqXj0riMBXq57n34Q1g7GIdgSI-laGQmX9QanJXFMnKfTEzMx5qdDMVhLZYjtI7W4d6dnClA-KyHvtVQLx5TFIfyThTrB9wM68w9YRyiTMMRnQceOnpXxO6T_5oQN9-bO2VCl7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=noEnKieLz9AJ_aETZffXeDyoOntHnSL-EC-BDN8YDGp7c-J5-teF_oavPhOE9WFEDo7uoLN_J0zSUmdVdjHF7fG0yrBiqG7CUHTlwnfb3vkIAxD3pKSVB5j_SCuFWjGsPnCEYjK5xc0mRDK3IYfdLwmKWtPXn4V5MXEDnspZqrUUjCR2TV6vYH8GF2wjOSiQ_O1LqQ2Go-WuOlMqXj0riMBXq57n34Q1g7GIdgSI-laGQmX9QanJXFMnKfTEzMx5qdDMVhLZYjtI7W4d6dnClA-KyHvtVQLx5TFIfyThTrB9wM68w9YRyiTMMRnQceOnpXxO6T_5oQN9-bO2VCl7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtymVvGw7XtdlRB1N_WnYWcmkYBmetdQGunSGUzuxx27EECZubeSU2nOLQ2Hfma6Nggnfb1PqoqAx3hxsoaINibmvGeNTvblOjK2DiMx2RmwpobEcWjUI_2ApN3tYaH3ghBeMYtYdQQG4UgHk19VoFyVi23iUvPjf9U2AZ0aEf6gktVn1nlnWJshnBYkPzouChEZDWPyUSRrBwf_XfsxUjFryxDviSAsOBV49fua4quJ-qU3UPWJ6jyuqsT3fcLKaOG-BaJBYMXwPgyh1_rqU6g8NriQiA-Mlui6Pfunm6R9Rb1Akm2z8qwhdeJuOYWbcY2gmjYSk39GnB5ie3mJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-syMXX5iW4XGycr2Eh0pwj3eWUncJirbCmkzeNUMNEyU70wu7AW-PUyRb3Gs_G4QjNFNCNOf8LynKZb3TLcH2wMbNwv5zorRhpm78gakHkLLboRAn_m354Td70vEAnhx2zni9iCKv5e5mKbS8RSHPETt_FnYFLrCmbBnlhz7dGZO_iMJAW3R6UDIciJphZUfXKLheArDRLlqHr5NDKQoJqRwB3OgwcJtLTWOwfkh3LRv3bKJD7oQFLTbf3zx7FjPFdsriYL4kiA0fs7EIm32CxQN51d4Tw64r8gavqfMe8dJR5Q7h9t9BwzvHOk4_mFuiR-ac-_FNheOpW_LQ8F3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqbEVcH95fXX7r3ryZzmNGkGPqdjMU10irCgUbW2vINoRn5TCQn6w4AFro3yik7Pk6SNcn9Xqa3hbHuAA-jjhw90ZSsFpUaRONXZZtYxImK1MMNSikyRWV6Zr-od4jlqz7afL0-c5fAkEPkwgahJeNIePOvCtdtvN9pdsZf93CO-tCgij34w_pXxjBSF79cvkS9dOQnQO-DexQUcre5pFZKV87Gls74zH8PlYZss7lE2cIwT9XEjKjrjQGR2OXye2Jcyy6SYINAmaYaMFVkkXbkFbhd8ewYAZI9oaYrnlPxeuI8U-aBBLKru7VO8McgtsB6XJFihJ4rIfq-op8ZkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhxSDNGMCgBKOB2mYlhIkOxt9WK8C-fBGiqwtegTqvEPmPWjvSKUrLBA5GTUjJC7EWnvRDGqWIq_t48PXhw8Ex7p8SSRHWlh8Zos_hPpf52bdv6mf6k9JgE3URhG0u1Jl7L45T9lE5ndugN2Kz8U7NJ8KqFWfo6sINvTJtZFOGpUUG0UDn8yhtoccE67rk5CDOtfLGkqxvTTv9jLa-uurumAp5ZNEuNT5JfsbPOKdS4aDBccXFvNXk3UsDV87Jsema_H9Epf3TEdRJ9bhe9QT3zHMR2MP9Pw_WUFfbZHzuYsFqoOb0mNuycpw0TIG_kXkZklKJKvTQ9sHTruDvBtDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ0XHqV-k185nrDdVWY3jixeRK3nK4LPxn-VhC5C86Vf0juos5Cig5PN0FDwGRGwsI9ie0ATNcSlTz6qtEL19hZZlYu9Cs4ziDfRhR9by2WumOkmmzz3mHJPU8jZOD4RRCus2PGFc6GPQxdaoL375EvY3AG2njTAi3eBBUfp_NR3jdgdGXj32fONz7P__Ve-gFhAotUkrRFWwkfdFWNAKFCF6msyHIQ6-601Ny8xPb1aVYHnrB0bhRfIqbYVFBgIBPmphTi-zQHQr93XNQ8IbM6qE2ezCUmJa_bxrPJfQ67zJjEMwbATBqJLImC-4Bk7C1Qz01HsL-r2cK2Ar82CIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnsnD3BcQfR2o6kQJPx0HKcRH1sb7L26EBLvmPQsdRZyHZ5AGbqIObc7mnHxM9FPn8Tf1mAc3-7bbVPLkAPONFKgar0h8RRYUb3y_LvqrPCx5eiFJ7APQSS6B5TvvnAKMiNDxw835rliC3vkmYaVWZEsPpZdVARMS2BdPC5RbMHwtK_ZGFcXgjvwljULIiH3wi5zp1T6D_pXalW3ILeRyfnNugsK3oxD6KCq8aRhccOmX7OTIBrGfkaQNhAa0e3_4F3Y6VGyduAonCzFKcO96xykWpN8ZZdojNpGhxenIZuzZwCo5FDi5nanA8ZjNn3robVaeb2W20go15hYKvTyJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjFtU22YRnXmgJBqrlb6Q4OsSz3AnBuEhs7rMZSoxuhgkqwA7sMzsaTBRdOdeK0X8QDNkw7VpQNk7n4Lj528kYpCur3Zm43Sen6PxUVtvJtybq37lyA6-a9SZswsH8uAUd0e0Ug3tdRPWvoSg97e2b-KWLVbG1YUNjD8iG4rPIuo1u673qHKaf2ChRb9KtHBO5mzp7najjLPMsR4pAySeKeBDQOlvde09fiWVbmvAbgwjA1zUG4F05mVko6nVUW9AEWkCb5sAFkKvi3LARdMfVyiduv3Cf0WMjOk8WHtjbXspy5iPE3znf6NkfC8_JtLf756VoxfON3Yx88FMZp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=O6CJiax7YIyrOEYi1LOU-FpLSF-WvMZAbNW3BTVVEWST2KZI4TVHxiOYk8xp-lYWH5wd1BJYaj6n_-Xlkr0c_2xkNNmR4Ff1Pg15LPqwABkQL83NS2tJe5B6W0sf71-VZPyVYzi1nn1lKHd1_Ndcq_oArPsMk_2VJu1yhLPYAn1JPl1SrXqce4Ewy-Y6BNlsNjntXapsUAAeJRJA3PTbu25rx1VErDaX6ktxVdYM10BMPnnsHNBBr9klEYW3ALSCkbBhhW2NGRHidtoXw8a8nrenAA72ZiN7tjpJPwvt3UrVycLKFUVhLmZVj9rP4KBPucX3vO_kcuD42tOr-wRmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=O6CJiax7YIyrOEYi1LOU-FpLSF-WvMZAbNW3BTVVEWST2KZI4TVHxiOYk8xp-lYWH5wd1BJYaj6n_-Xlkr0c_2xkNNmR4Ff1Pg15LPqwABkQL83NS2tJe5B6W0sf71-VZPyVYzi1nn1lKHd1_Ndcq_oArPsMk_2VJu1yhLPYAn1JPl1SrXqce4Ewy-Y6BNlsNjntXapsUAAeJRJA3PTbu25rx1VErDaX6ktxVdYM10BMPnnsHNBBr9klEYW3ALSCkbBhhW2NGRHidtoXw8a8nrenAA72ZiN7tjpJPwvt3UrVycLKFUVhLmZVj9rP4KBPucX3vO_kcuD42tOr-wRmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFidTfVSw49_dRdRvgNvSPb3sgEqIqCuC3ILqWTz2JiTWVXCLn4B8EQnAKh4wGPll3zh20DcWaQ0n9_L3Fwu77BNamm8QvTOqGlFrtRTCCpnnGGyaYi-uAr8wE0r1S2te7sSXU9ckdjbdDnkzitglDcfqif74VCc_6ri3wFjaXbyuZVTY-MX_F58XwXPvddE8LL02uOqNwlyb6DjYALnzMJ2ZXue9S_v5CrxRqRXx5iTtPVqv5ZgH-xzvjhX7oO3Bo3jUSb36fil-oIyjPHoVl0vEWXd-jSSRcFtXVU4wBGD-3H1Gsf3LxSae3qEHUfILn1IYxck3tPyrs7ysaJcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=RXeWluQ6Cyi4rg9szfPu20TSEtWcBSNaLHSbqGp6AbPT8PwodQL3h55N_76d9q9f38fj1_PoMhZ5sKQCtmfxe_vfA_63KsZy6uCnBnkXpMyQDF5CFMqPN4FNzu-F8N2xsB5iUjaBFJO4vjbhbi6paX9ugmJeoHrcNuK7dWqWR5bhaxuUsPRdJksXGW0_hAeIAfsgAbVN3duH6fwVDh6lQnCzu-SHOYHZHZ3nsnO8yA7_IT2tv0zt5n24mk80KGtdugPS7Om842cY5OoQWZ946zIoeF7FVN1qR-uYmTQjfsRAQXihJOO8usB7KfJfuuwSWVrpJusmiX18cgHE4uqntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=RXeWluQ6Cyi4rg9szfPu20TSEtWcBSNaLHSbqGp6AbPT8PwodQL3h55N_76d9q9f38fj1_PoMhZ5sKQCtmfxe_vfA_63KsZy6uCnBnkXpMyQDF5CFMqPN4FNzu-F8N2xsB5iUjaBFJO4vjbhbi6paX9ugmJeoHrcNuK7dWqWR5bhaxuUsPRdJksXGW0_hAeIAfsgAbVN3duH6fwVDh6lQnCzu-SHOYHZHZ3nsnO8yA7_IT2tv0zt5n24mk80KGtdugPS7Om842cY5OoQWZ946zIoeF7FVN1qR-uYmTQjfsRAQXihJOO8usB7KfJfuuwSWVrpJusmiX18cgHE4uqntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkNvduIB2GS4ZNHJIcs9POc83drw4AOz9caLsBZVtNo5jtyf4dxB9ntC4Hu5mSUIQeU9u73WVGn1tegumJsdcMP4xB7G9ng7lWfYYkgLSG0RVFYmAAkdzudIcEFHAGf-9WReIf1pZtZyb08db2w8sfyWk6keRu5ZZ1u6OV4v0yjQATEexHvKfTCH8b8t49ikwFUDzBjFdgbrsK_RnM3txRKoLPx4EHzzPudefHF-aFE39wDz2alshdjRLWlzX-mqmk_84wRTmla1IYIj2bIekIyyr6mP1zBjBiu5hH8EzoSnnUJvNuZ1nvh_6VhIGiLUgN2e9ahu3ShoXfXiOZqnsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJveqcxCHz3GYiNLteghfJvZbz0oFcQe7eJ86U4inc6KTRuLFf-z_AoCm9r3YbIRTN6HSBbvRzAXGVAG07Hpri6hAEO3BAKecABkXzpa0Y6vJvuZBhoN7VVR9dbm9eYMl2hIpYX3jh_vGDJaCOwnTsa3mI_CvjJFJ0_lz4SmZ-zRWHC4xVOxIfnKgeu4Ip-GpDlIiJSAaECtetY6L50wtta5CldwNeID6SQ1c164WZG_4iFURXaAGof0zcGcYAFxzQdoVL5lwMgk5VP5lj7fjax9Y-uEgZnchzH4gSftf8tO58FtdAj4gkr0JTODiFaukx_FykiHoAO7oEgZB_q9Py4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJveqcxCHz3GYiNLteghfJvZbz0oFcQe7eJ86U4inc6KTRuLFf-z_AoCm9r3YbIRTN6HSBbvRzAXGVAG07Hpri6hAEO3BAKecABkXzpa0Y6vJvuZBhoN7VVR9dbm9eYMl2hIpYX3jh_vGDJaCOwnTsa3mI_CvjJFJ0_lz4SmZ-zRWHC4xVOxIfnKgeu4Ip-GpDlIiJSAaECtetY6L50wtta5CldwNeID6SQ1c164WZG_4iFURXaAGof0zcGcYAFxzQdoVL5lwMgk5VP5lj7fjax9Y-uEgZnchzH4gSftf8tO58FtdAj4gkr0JTODiFaukx_FykiHoAO7oEgZB_q9Py4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vKaTqjMQrFAZDkF73HuRBXNG_spPO6Hq48YUX1IW1WVoAcHnb7pamneanwbC7T55U5SUR5VwfE8VNDDNsHoJWnQyaQapigGkSa16rrXhTrjmVUr1cHcQyWTXjii5C4Lk0VcDSgnBZ2N0DvlRaxVgGIGcjJLgn7kp92VcFD1anrVCBsN9Utoy8zp88Ftdd21DFs5oaaCHrJA5OAjE6Ag6g5Rh_mxX0RGRlP0Qijje2elfyY6o8Mz3qi0ObpV_6hTFu2EvjYvrMOGqLx87ozQsJTYlel1fbWdcAYHKrI9LpCb47uhmErVXrhFJwmQlgvScAbIf4oQ22vXpQz4QZF_YbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vKaTqjMQrFAZDkF73HuRBXNG_spPO6Hq48YUX1IW1WVoAcHnb7pamneanwbC7T55U5SUR5VwfE8VNDDNsHoJWnQyaQapigGkSa16rrXhTrjmVUr1cHcQyWTXjii5C4Lk0VcDSgnBZ2N0DvlRaxVgGIGcjJLgn7kp92VcFD1anrVCBsN9Utoy8zp88Ftdd21DFs5oaaCHrJA5OAjE6Ag6g5Rh_mxX0RGRlP0Qijje2elfyY6o8Mz3qi0ObpV_6hTFu2EvjYvrMOGqLx87ozQsJTYlel1fbWdcAYHKrI9LpCb47uhmErVXrhFJwmQlgvScAbIf4oQ22vXpQz4QZF_YbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZs4FvyXbtqOV6xN_mK4_rcrxuzj7QRxBC2ur9ECjM1Jbf93POZjkhJL_vP4n8vRK1vKudZUNu_p0DmaowFHLYmWQBXQeyc0bMmu-1A8nFHnwh8GotTINPumqhqDp8xURLvRlm_9Kq7ik4Xu3hpv5xNoNjWqq-lFCpMtTeP9_sCl8x7biYpTgVsJv2LTKqo0XzZ4DF1Vk0ckDqPH5QqyLhxXwJx9fd6KrlewuEIqRHqibBkU7m3v0W5d-G5BMv1V36khZc6vKmp96ykWurjhaN-6eCugqotDvvoiMKSYgq0dwgeXE-8teLW8llMkeplXUM1Qkkb_PtzfOkGco0km9Qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZs4FvyXbtqOV6xN_mK4_rcrxuzj7QRxBC2ur9ECjM1Jbf93POZjkhJL_vP4n8vRK1vKudZUNu_p0DmaowFHLYmWQBXQeyc0bMmu-1A8nFHnwh8GotTINPumqhqDp8xURLvRlm_9Kq7ik4Xu3hpv5xNoNjWqq-lFCpMtTeP9_sCl8x7biYpTgVsJv2LTKqo0XzZ4DF1Vk0ckDqPH5QqyLhxXwJx9fd6KrlewuEIqRHqibBkU7m3v0W5d-G5BMv1V36khZc6vKmp96ykWurjhaN-6eCugqotDvvoiMKSYgq0dwgeXE-8teLW8llMkeplXUM1Qkkb_PtzfOkGco0km9Qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnY9m-jZBF696IHE_SDI0qci8TV9rRwCtYtHtsH47trdVm0yrzJJXzvZSmtjfFA1tU-9tK_GR74qo8x-qp7kzOkvFtiFSnrJDAPSHAhgSSubGqI1vdV_GpoumvAbENrZb3QnIpQ4ihskTRsIATGFPhIfR18jiRDedM8C7A57JaPnfd9JDhfXW0qzmcpVDa7-euSF9-YpVpPl9VuvXL12xHFMYm-Xh5Z2M5Yr1VYfvTUZPwc-18Ka9wDQKjL0iUc9yP9YRRKIh6-B6bTt1EqiDBGKxdpnXl2_MRNXsJpyZRCWHonQo3e2pgYud9SMzQU5KtNTVZ1LTk9BmZH2hTcAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLVpFrFyDyIJNUr7Pw20QcM5Q1g1SxdB3ik-ejgmF2yG9AWFTxzjcKG2WZ91Cuuo1ZzinXKUS9Ov10CYaNZdOycdMYj8EqwNKroa0MXJ5DBu8N42N7Sh80Fqo0pjtZPx2yghB2uk1_f12AvGlTwXev6B8wqBjuYN0Xkzws3cMyexXrQGKMCTG1yGdnfhM5tMQ0Wu4SvaG5wvoGpURgM2_vmCeJTGtAeJlS9uDyQzu3vrluh6QPYW2xB9gepDLSTqteihg9OaKFwEoG6HNxqxIrbRYOTJsigMkEXb9zON_SjsTIq9ZUDplL3nRlMDgNxsCblwTePfk14Q0W7he3SOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvbWqWthx2Es7ZCwJaNpIsVKcCZgaQwx6kufbmHvMQjpBE7P2swfS3sZGeKLBTR2mKgTvWugv1bviOf1_M0pV1qYFyng77Pgh7TuxSTr1Qt7EZy9FtppKNfbxiJmNht0_xqdcJWkMxp9c4LEHm8SdZQBvSB_qLQCmaKuFA807Xr_z3tJNVvzIlKn4C8tG35TuRREqbKbeGcCTbmlaYDnsh1NhYvlWFQ8miy9WaJvVVeDphfmwDDGsWE7LgYaS4zX4wdTNhTVFGXMYXGnv1oA3Qj59TES3CCA_VKpy5ZY7HIRnttfZZr8fCPIvgujnFN0T-2Qe34IUqtKJvVgWSL8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsLWcICAiLAAiODNbL6jLSUvHnMMGrPReE5CftJ1cd_U93tx639uIknv5lGCv1HDeBgf0IsmoKVTYMPglzNWx_uM59_ci5otconAmSQkzfmSckmJEU_YiYuyneXwVnTQKL6UgwbsmrTftVZgYG-HqEUDIG50fDh5Wa18-Zh7POQI5zpJeVe9nhJW8aJFVC4EYN9c81tM-rEzovKoWNbGdqQjSzf9Cmio-AFLfu_vq4_5_Xe1n3d1XJKYITxSpX4DyVrBGLyCmtLynSzAwvuUV7Xx3JpL8LtoZ-bbLalzGCEk9nuxpDBB9JmvwVAyQoxbbnohn-fTXZYoLLisHXzr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uixdmq79oKhm0LDzLS5ACkI0grINDxGE8sWgspZjIA4z6hKw4Px7lyFB2Sr2ORPNM9dvpNY8cR-e2DIHk3TZmfs6p7Epf__ok7-B1wre_th0SkD80h9SWXZl9KyROmYH8ev3vFPo1lgORpjtaTUCPyNulDSCRe4QsQITuU2PEU0POwuqtRTCShOsEpDU0-53o-VBNAtUO71xNMrqPYealT4ri2NNbTPwnClNt1rBro3A1znGJnUapqfbzAc-1Y1mG7jsMJ1KtuYrEqb5RWEfCW4VIjm9OGCf6C04IwHZsv_gavH0mf8JBNzB9kiUGne6tJLuBzVoL3h-fm5x7LZW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4j0-PZhJpTD_A-CtbijSiC5e1YMN5qZn1yq_4QqmktViHENJGsAKNM-1ISqsedskf08I3hhLXGNYAm5RkfXkGQSHg3J7X98ccbCne74RiSY7Pf_9_6aIK-neWPS1VjXYqtKdxdEW7Q1_bNbMEDQN5NHsj31eE8vs1eie8_YQ_G4Y1Xhk1BqzU4SddwPg_gcpj_IHfqOLt6_L02ZUhdpX37dYRj_I3YDS3IL8_PyZeEuvBqx9xwym4UgP9mCFR_JxyLgcsmbNjDazSSoV5Gq_LKSh9YGZl24Afy_3rD8h9FYw1qSJjZQcMD8U7JK0fbjPNKKnSepmTEjNNFDylBzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULlAvbz7SwF1SDM3-lq8i3Esl7grY4VQfzRavdx8f1NzAHwjxUih7QvRABosMITwL2l9Nc7MuurXJ-wFut_p4oJKXLubIqoHAnxyGVtJMK5RaRJ1I98y0QbisD6m-dvR5MF4L6mfz01QutY4O1IlV87-TcopIbmRljxjuqiCC8TxbGvDxsGzOiIwCVR_P0BI-vlIsLkRGNHiiIRoTbTNE_qycVGIHN-L9HJBrVy9VEzglEmhgHoQ01HWK7OjTlGXdHM7Mq3JI1s7PyKh8tOF7TXiz1O9qabnBA1Pts9Zx-UMOiv5EIOmZP4UkRSyU98f833k9Qo_eSaFcepg6b6MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWrq2kWRuJR9k0PQlIQM9poRoHtwy-amCGCTUR5WP8lnclFw8NNpYOFdxb_ZGdSdBHw9Sr862_96Lghbca1ptmsCYMRP9XIiKcz94AB67MnrG2HiUwPmYzzHVqHul7UnJhyZVQmTJZW1G7WnEDZAJ8yS6uzRrPF1GMeLsJ6kr24WRtyRTl56D1ZSCaZpStsUMIqsEAnv8VREF8QE4G53P3k_DKsOvM9_pVmtGZrF8HQzqv8EkGPxCWfMaQ8y7YNFdtEpn48BqOaHNMm2DAqQfUtUCAV969QFm8w16HLiMKS8Q2r5wrUardcgEAhuZFCuU1SMu6rZ2iD_fyU9blpxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhCWqH34Fsqf9DEWV-b63L1l0r49Gpl6EqUFmP3joiQE0EuSbQ4_Bm1n1eIdbSQ0j1b5uEkVSTAxyqhqiRADhqq8ckqKjK-UxzWzly_k5DV2cZOhFMR3CG71m2SK0u-xeSy-Ys9eXFmcZDDtnbK1AFUgolTfiv3yiIQ9rVPfVk-hnAdld8GJbD0UcAxgaqnRv7EZaxN1dD8BNpjvW6dtQ0-1jbQrpqXlyZeM6zeeIyHe97PiHMJq6IuP1D2J3rppwAYhRpbFo7DJOWwJwmUMjj3mI83n4cdapKBznPFoyhjhy5VR5e0gKBiLbvLuLyx2oL1GKEqr5y3QKK8eNzz4YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOOnh1Imlkd4iR-ZpiI6bqHHB0ef6gUsudr4bjrk-Y_OXBq_QYnc1GvdPFMOjucBzi3rYlY2I2QIullvMOc11gA6Kcb7RjGrJjYsZpMoMMDZKB1ZXOevwpajOcVJ_csYobk91NI_9GjUxgwXYmYcHkZEMDV7lgbz01dkIMZNlnDJ4SfbH52UHWNCPRHtzz6zIDt951WPVrTl_0sNnK7s0HhLYZ7-EOdn6iDBjU2eVmFqAHs_OUbZAXseDci2KdMUmgTzy3sHFRY0ylxH8EaGZh936CDpZIlPm6x_xOAjoIv707ly8FgInyD8eEaVguXxZILYnppH5SZOktYwKOeXiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrIGBp2D49sYabhlQdZcX6ufJNr1k-0bQBK5Fb4qlYHeY_AQ3akC_e6rR-FizjqJvfAPveJmDIu0sktImfNTv-_-250n4VDnUxMVjtuyjdD4EZZj3Z6TQAMpu75mFa-LkY0Gmnr6v8Dw418WJE_PFGVEjzuvx4ubBUlTHIguQl-3vC0Pu4Mtq6IIPhjo6cvQ9K07loYxWFV5yJYlE4TEt7vCbk7L5qPyii1UDo2tuIc4hjvD4sgxkbLyf3su4kTmdyh7cwTJH8l1snjhyDRxADBCaugyvIi2479k0xcit8SU5ZgQIMkl_GzA-POArxflFuUFyvQpaT9-xMIjTbublQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh5JoqZ0ZSPRhE_4HdsYMsLxBNbaT7eWwKsGgJ9QHGE2gMO3q23CtE-zDMtQmJzub4CIXLnoh5pnpIjiUCBBzteK1WgBoNWUeAitWl2-8Dh93FlgUZWI-OtQE2E7HM87ir5DzWpiscgOKa3NvM43-13QTLXF0ZQYtQjIFONF7cQ2UG6aD3U9yXon6QkqZdphVox1-yqrc6d2zkcdrftREjGjeHM3FBP9BDnhowjZvHjkBfgzVrA7By3L7c-_qf6dDIca_6PjaSCIjkWcAZloecH8pUEbUUwFW7Yic_Xlo_rmdYkfqdNgM6oe-5UO2pUUmbDzr6oIqjotFbF7dvTKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
