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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 23:41:22</div>
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
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kQIsifVaA_D_OU9YVRrSISpW-sFI3m720kkVE-BErWFlikY6zg9TkbymjNC9rqKSc4dOp05Oejh_QzjGtZ21T9chCcpDZJI4h_XBNz-odRGrnj4xz_MFS6QOtjRexEiFx7G1XJa_yN68jdsH1ZT1JD1rs0tuSp9QRalU9fGV6xumOuemzYNXIIP9YOBROHVxBrfgkzCMbQndOXlsznoJR4H7jbhE9UxNsj2m7hASMzMHQkSYa36bMOXHzRHRSZ0mSTaE-22pWcSIYlx0Zl3JErQeszk8kUQUamkv3XMwpb_kPbtzNPlSoPKLA970fke3QM_dl98XD19zO0TPeNxNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kQIsifVaA_D_OU9YVRrSISpW-sFI3m720kkVE-BErWFlikY6zg9TkbymjNC9rqKSc4dOp05Oejh_QzjGtZ21T9chCcpDZJI4h_XBNz-odRGrnj4xz_MFS6QOtjRexEiFx7G1XJa_yN68jdsH1ZT1JD1rs0tuSp9QRalU9fGV6xumOuemzYNXIIP9YOBROHVxBrfgkzCMbQndOXlsznoJR4H7jbhE9UxNsj2m7hASMzMHQkSYa36bMOXHzRHRSZ0mSTaE-22pWcSIYlx0Zl3JErQeszk8kUQUamkv3XMwpb_kPbtzNPlSoPKLA970fke3QM_dl98XD19zO0TPeNxNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfWzwYJ8am1II61GJf0Z4Hsquip9uSwHzYNN6LAaEtlH4lEOpsJm8EC2MUiGNgZi2Lk4G_HD72Mtj5zjJiN9Wt1RwkwScP4qoulktpfx-SzI7jEe1925tQnlZwIZnY8uDvica7XXXoRhpEffzHptA0IlGYId264JkGMh81WMjyN2zXgibGloiL-muBnRkxW0RFK9M-2PaRBvV-yHHwiP-pK_xUkoqSojsoQ1SFySjHh9UXp9JM-mJBoc9r0QGLRoSQ2KwdhUroCuIL8_XB7Mw8z_O6C4NW-BPsPs-4IzR6coTzypg5khcTAzgc1wd3gz8oXJp4VchyVZVF3jfzyvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX4Foqt0CVilhmMve053tAfOp6bVtLFB_3BK0zxgmoPbPQknNDd-gO2Qz6OHAHG72SycEwvSc0JuXblYMtEbCeJHi88Bq8cgblSX_N3MPFZX_mi_0TzqUG5ExImrQzdx7xjbSdEaFhwyE8-MzgjxOUxa7JawjbyJc_MD7aHINq2UnluprOcC9GoNJkd3sElj0sq7_5F4N5H-200h-215QehVBvaZu_-oJbhHBQVo7slvbNyTcSTQxPdz1OdKCD25mO1KHigoqnsX9-eIfMkjWEiflE4NAgHheKAXrnA8wMWOhvERKZtr2O6kQ1pi9mlpnU9rzAzmVN6vdDbK3vxIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=beB3qJXlyybevOWEvQObbct00_mXXUqZOxigjTBFQa81kZOdWC06QdSvetrbhGV3n4tUjSGCLMsmCMQ7nrSpXNIYJNNuGQ3mIS0nFwXY1cCZf4n8Utqw7-dhDvw-p4YPLgyVQxhQgMFz1_EbmZRnB0NjqJvueOIYdsmxjY9e30gHSqgNFBGhvvfH6RyrCDXpOqQq9vhWdG213M0f47vYn7UUaPM_o_4V0_bvl5-sWSl6ztaE1N9B5086Vug9X6A--gqkhxOCkGVYp83BLlyOHJn-iHjWv3HIt0rcxBm4AYt2uwVTPa4DnMDrTXFHfzvJ_3W_xSV4dyWJa6lMZLxIIHmwnjU8AAXpqfG69mNV5gi_zhnljUaCh8wMX_C6I9r4_sAGtECUosVBVMUWhvcSvloBXprJyAMiYCJrYweQU_KMltk0FPX6LPhNbQKpPYRThBMJtSRljQfKRSX4sgwc8JciJnGXDoYSYzGw_XEHMnQwRA8RvdbRjF4AAmSEQRzzgXIY9Ki1ot3isqqJqpy8YQK1dx8W8eNHRZPYS870U7aamnF6io9axJiXyhSYFtTODHB50WTIfF0OLrYE852wb-vsnpnYU9pgVQiqVewPsgtNxh35ISCKY66Fz00CxISiq8TpHPvXqpFjCKA9BxRPzisfXZ1R0FByEErmYjidSFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=beB3qJXlyybevOWEvQObbct00_mXXUqZOxigjTBFQa81kZOdWC06QdSvetrbhGV3n4tUjSGCLMsmCMQ7nrSpXNIYJNNuGQ3mIS0nFwXY1cCZf4n8Utqw7-dhDvw-p4YPLgyVQxhQgMFz1_EbmZRnB0NjqJvueOIYdsmxjY9e30gHSqgNFBGhvvfH6RyrCDXpOqQq9vhWdG213M0f47vYn7UUaPM_o_4V0_bvl5-sWSl6ztaE1N9B5086Vug9X6A--gqkhxOCkGVYp83BLlyOHJn-iHjWv3HIt0rcxBm4AYt2uwVTPa4DnMDrTXFHfzvJ_3W_xSV4dyWJa6lMZLxIIHmwnjU8AAXpqfG69mNV5gi_zhnljUaCh8wMX_C6I9r4_sAGtECUosVBVMUWhvcSvloBXprJyAMiYCJrYweQU_KMltk0FPX6LPhNbQKpPYRThBMJtSRljQfKRSX4sgwc8JciJnGXDoYSYzGw_XEHMnQwRA8RvdbRjF4AAmSEQRzzgXIY9Ki1ot3isqqJqpy8YQK1dx8W8eNHRZPYS870U7aamnF6io9axJiXyhSYFtTODHB50WTIfF0OLrYE852wb-vsnpnYU9pgVQiqVewPsgtNxh35ISCKY66Fz00CxISiq8TpHPvXqpFjCKA9BxRPzisfXZ1R0FByEErmYjidSFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7YqIBrLDmzMpeUtJJrrKkD9gjJJP5NXkZgYS0s5wxBn3y2kpkAfSjVNrqHpTvlAnFJGmn2d2hMPF_fnTXTTFLCdCZEX1hZnUpF8bUKHJXdjYKrShvuZo4oub5y6hhYbRHeXhEbdzapWRxNjuxv0L_g0bTnin3x2hs2_6Al4aJI8KwQt_-fSmiu3alYsSL19ZX80H1EarwaigQpSzUHAggypAOB5Y011sdmJXrVsg6883aUYY-pjbFHzZCofG9pZvWEgvW1ORQjkaEejuVQ5Dj-UuF8N6yZfckl_6oS46CXQVsUmwHSqlqUAU2RNxPBsmGkHkl2O8UIqnlEm6OiCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJf9VB7UqN9fYdFi5pPgMBiYREJD947Zs6iCmlZFpWbk2QWACIbUhy25Gg0Timo3pv8qmLMSxamtqtO9MUyYpVflCXT-sud12auS03sdGc9IVc38v83c2ElaBJtD-ajlicC8F1Hb3Jks1K7MrcLvasmBlUG_yF0f11ey-Rohl5FzxVnJPfwUvPsOZe2ZpL6oPkCcG4GaplDVf53FqSwM7Trocj1j5SA_1E2zu67muT5EZWItXYl5f1vIrgIWJJqM7ZrlK5QDXUTau8Z9m5Oj-b84sBr7savrdtvZqvSOS9-4GqyLUIUSGuGde_MIM_pF89ZcAlCPddkVs4keWMTZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNI4fUjMoX-rcCKhr3R0yc2SFcJFZ9ZSBTRP-8d0EobMEJ2_WOrWxbSc99hEQxmMiQv32W_5PpGqTi5Zx2z8W6LYGV7zBe9ae2P3xpn9N1TCLFLgEbMPMvImrTvwpCCX8dlmI5OVj5b9jiUK5jmTEFGkVX7mdI6aUG_1RI_aajqNsqqTq2FSXi0UjYsUzjOxCKAZ3f6k900y8r4FIeglaJFo_JlIah51m-KC86Afa92uMZJDybO1S4qQRsziErmG1Sw5hLlmOYzYkdWOWFEJZVlvgQYNrvge-60H2msEnw-VCx6E8svfJ3HA1oaKpWYBfcqTygTIMX89kehpF86zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbJ6GqA9SwWIXb0iDhrL6Mj79gLbS0Cen-yIe3gMUD8pyBIVNPaHx3ZLbLha8kFHiDaeONf3UE3irqPQA3PYEwP0uflHnKrOZR7yOIjM0bxLTjLxUis9FfSeqh5yvRpQKMaCBaD_n_aPWXJ1MVrPt21-34Hp6qZUXZhBBpRDI-_pwoxJL4BRoaPXt02jJkks3BaDkYLxmyEk51MuiE7Qq9TEE9HqE-kxdqLYb3-jm9DXde4FRtcgOVn3aPuKMTM1Ji7Bf_IyDx9f6kjCY9xS9ULrasYFB-A6w6ZW_81J3yG0ZVX-Ms_sfWQx_BsScj0yH0NOe2ehx3paT2YO5yLSKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=mM5FeTK8YvSorlGInY9ujy-6KBioVHcVZahI-pStJgKbojpka8EDxTOElNJJLCxFGAVI_G3i0f4b8krXOgrdnSTeKnQfmVX-RZMt8unwq5NlyLRpzbYzttuK4-HxPyLu1DFobHy3mxWjQ6zjdUbOu2JR7cn9VOEQ4umxMNsMkjj8MVP-5KjKPdQo657Y7hr8st-nSR2lTOC-DIOhcmpngIHZbNo_JH6YhGtR0W5U_O_B4yxBTwpFsyJ-IY0SB_OqiF7p2DHccNAHpGR-1uphFZ7Z8ii-Beosrd3j-05dy6Z83K6kZp1IZZnA73AmBniIol9V70_is2PLO98tvhWXjRPNVgyZTaRe9OWv7wdSIPRNkRTdVSkIIt_vlprv5SvuYiqRzp7NJ70L-pNG24OsuIvLu13m-DFqZy78B6LnocWdWl5ms0WLGKncGZYtdiaS1hgau0o6Mkfg0tlXRYeRrmmdnFQrRYPO_F33AapMMyydvQstEw0fnJU9IdtI7EK9ZFDxoEz2gprnFRzWOjEF0O-FjWUJzOyG5KJSp7UxdyfDaeah-jM5kWgx0AWa-pM5Tzp3MF12Sa_W2BW_gvfgL-nifJ1sTJ9VAMQMNv3cGzfTqEfjJJoF-1nKJR-qO1TQhKfdlTXu70Azgr5BKGdh7oYG-EdlBIiKgVpXuRvvSoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=mM5FeTK8YvSorlGInY9ujy-6KBioVHcVZahI-pStJgKbojpka8EDxTOElNJJLCxFGAVI_G3i0f4b8krXOgrdnSTeKnQfmVX-RZMt8unwq5NlyLRpzbYzttuK4-HxPyLu1DFobHy3mxWjQ6zjdUbOu2JR7cn9VOEQ4umxMNsMkjj8MVP-5KjKPdQo657Y7hr8st-nSR2lTOC-DIOhcmpngIHZbNo_JH6YhGtR0W5U_O_B4yxBTwpFsyJ-IY0SB_OqiF7p2DHccNAHpGR-1uphFZ7Z8ii-Beosrd3j-05dy6Z83K6kZp1IZZnA73AmBniIol9V70_is2PLO98tvhWXjRPNVgyZTaRe9OWv7wdSIPRNkRTdVSkIIt_vlprv5SvuYiqRzp7NJ70L-pNG24OsuIvLu13m-DFqZy78B6LnocWdWl5ms0WLGKncGZYtdiaS1hgau0o6Mkfg0tlXRYeRrmmdnFQrRYPO_F33AapMMyydvQstEw0fnJU9IdtI7EK9ZFDxoEz2gprnFRzWOjEF0O-FjWUJzOyG5KJSp7UxdyfDaeah-jM5kWgx0AWa-pM5Tzp3MF12Sa_W2BW_gvfgL-nifJ1sTJ9VAMQMNv3cGzfTqEfjJJoF-1nKJR-qO1TQhKfdlTXu70Azgr5BKGdh7oYG-EdlBIiKgVpXuRvvSoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Q3TclZy9FaQf1mIXTZ1edDFZ8FAKhy3Iq_ZHe7M6W6M3vtcbjVnjaqxbFVpGbcydxB4KpUo7Oaj4_pMoOtVZu5T1iYS3VesemjFGxn9N9OzMbMc6mhf9twBbDjzYl8dRLdbv1kc6f33I8bUntEx1GOCLELXJSo86U2cuNw3pVkwVCrZbV6RReg-ZDUdGWcyCa-wniq-XJnMnCWDFieOeKtOzItFqbQLQikZ-Wp0IGbwwjeuqxMEzsMTpUJ_Y5HzkSN7u306t5nscBhs4t9dKbH0-yUk-oRuxFTsgARDykpXnZMdqxslEyfmK7_4V8XC1V12GyNCriKZO5ML_gp8IXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Q3TclZy9FaQf1mIXTZ1edDFZ8FAKhy3Iq_ZHe7M6W6M3vtcbjVnjaqxbFVpGbcydxB4KpUo7Oaj4_pMoOtVZu5T1iYS3VesemjFGxn9N9OzMbMc6mhf9twBbDjzYl8dRLdbv1kc6f33I8bUntEx1GOCLELXJSo86U2cuNw3pVkwVCrZbV6RReg-ZDUdGWcyCa-wniq-XJnMnCWDFieOeKtOzItFqbQLQikZ-Wp0IGbwwjeuqxMEzsMTpUJ_Y5HzkSN7u306t5nscBhs4t9dKbH0-yUk-oRuxFTsgARDykpXnZMdqxslEyfmK7_4V8XC1V12GyNCriKZO5ML_gp8IXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0VWf__7tW5CfQdgAN3lapz9m9FT52o--he54K1ea_17cLtYP-zkJ3HxFHTE-dnFwz8zDftBOPq6PN8m1RXT1eny2Yv6gMJgo59wPfZCQILxUWbPpET7IzUqY-jPgfDwWQIRqeedoxqZOgwYqqDjyJ5m2Y1Fo37CrRDibOZA7bCDNxWggB4_1MBOYce4FF49S5F67dQbNIOZSKxiC4H1UXt4_snpbPDDngizcloCjQeT5AUpTnzOoirbM_SqRSGCtufK_E1p2Imh2nWYaB9n2e7H35hATI6WiFF_dwfcGZnDreVYkjP7j_Cx6bPHQfW3NcO11VdQ4TyvN5AWFK7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJTs-43fW5XkF4RH84kY2dtMgRM3zg20EONyQTnfE4PlGaf-UZysn7hJ7IQoAsiaoo6ODHftw7gGJSqYBC4hWf-TnXc7YnFGny9AlhGdkh1TFpHgElaFxTih4nR8u-04xArSMVyvKLZVwJ0TviEdX5lnVXrRpKUGkJz2_Mg5bimpK_nnjw_6JTSgxJlNPTrQLnWH9u2zdmksJwFp9JviMEP2g6HOJiBQnhWIf0JQiBEctpRCD8sJqFSzSldaL4OG3OIo3at8RFgypw4jNoIFuHgGEYI2LZV1LQwFXZV7cODaKePAoa4Kv5mD0cAZk78nGRHv2T3hqBS0x5wPVSRhDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-3FvyXDOYNSXEeUPckaL2IbRNwV5wSD-IazH1BhIJMY9IRaLYxiidcEYT5LaDOIe901Xxmh2Sy36CGrCwp_D9JFOObRgXc10zRyWvWDHXOIk8QBK5ksoLc5fLvX4x47HVhdape9YuEWmETjISc_c60_q_FkBRJ6D0um9Ttq19QJQbNIy2wr9yv4tF4kHndU_NFyKWu2NvgqLiu_Sxc-7pcrLFtepi9R0-qLHwuZiKFJZ9i0aWhczac0rtDgE_WP8zB8FCvaxw03ui0ba0SYHHTQhILnisojK3Lst44rCSdXhPbOE6gkmkNTfbdmUHlIAQ91hk8TXy29ryzjtSVHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqDDuXFNCesVuQ-ZeSOIoGWNG7M90RuSK19EMUjYWxe1kLDrgDGCnFWIbWMvEUxH_8gwv7ad02ffzlyrAXM_hgE-mSqB5mVTy-KK9A_TCYodF1ZwCrvBd43G1ej5Osg9A3OjL7g31dLZ7LO_Z5zKwS88S6JPrOLSoEIkyvYQey5ESwYEfmjRwP09-vn6MBvi10ksIQu3sWJJ4mxelwR_IHbheoYPGarRygX9meEa5I2u5r4Gc32-WibY0xApVjGxkNqJ4V77jSmpi2XDVLn9SPruQaDthAlkry-KDb5jsIxJ4L_ayQ405pfiyki-XJBHgaSKm9RM62BR4GGC6yjA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3aYM2k1hTVx6FbpT82wbwj9MGubr1Vp6cIwRekdmH1b_JSOEx23dqSrxBWfV1jYEOaqlygWwVKwqGFdHJYMdvIHdrfIOiKe9cB0jRSlL7GrfzwzEWR7RyUWLudUSKiy50PXMegadW6a98E3KiIIAt9hcO8lFCsKt8WlpSGcouFEO7XUq_p4bUkJACYB9TDT0lyvwbbDeaWpk-yi6eRBVAjBdc1dhjIJ4I350OpQzlT2gLbz3p3GpuLScZwayUWE2yKwlp8dZjdAGOqDjtJ7qbzUgyMlFNqdeWb-eNm3mActvS68wf3o3CuVP2d0jEbFCKF9wj7H3cmW5jYz2SMuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1_irQQ334W7hIKc_0nKjNypx0CzWmcMvjePOgeaCXzdkYNoU0BuB3MrYUOfBHzZoTuK9qQ-HS35l3TWCIpdH0M07uSvoh_CauYsvj5NDl2yuV0_dCBHVwek3vivA8LYrC6KuyzQA5uARZBpR65QyjfOSwwR_xNrJNBsjMRFxFJ9te6QRLhu8-fh077g192q4UQf88r_PfVP47KCt0Xwy8Dp7Gd2rin8yFPou9E_eX5MMdF1DGaWrf3qV4jh6xNxOP0s0pQbIdW3qhz89NoXAnHHLwMaDCNTUYrlwEmOkS0ZBiFGvaWDmJRHJNueLXSuNZKiUD8na06AgBj-1MIl9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_ziQvtmduJxCYSDDrIVLBa5bJbsWxaX-t0gAfk103SljIcC-uBdRLewahoARbvu1XAloneFPDwagATk5EiGp_4lUAYf7ZXbfzE2ltjZaHSpZ7rpqHueinjZakEfJA_aPXzRScBm_ua_S8Cgels-f3FJzQvpGVJHl5l0OI1NElZ5wHJY3O9AJF-_TXjrD7ALt4Z8gWdP96mZu91q4FVcOsHSz4ltMovYwTWimTVHE3IKoWd0X0EWK3XDIU78VnpQJDcxoFMlE6evNkgfANt_Zdvcm1EWKsDRJomMMp8lGJw45XC92TDRrarFL4GecYIwpIxP2q1oVtwjIAxal47pWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=d9aAXMJF05465Eb9rJ5j4S5PlLSa1H78nF4KY5TxTxQqAElI842AQFeRXQgqU1dGfzKHEIJGapki7nvdCuNIsPZxD3D_2ernUNxgJadu4HnF5i1PczP_Hdjl7p-_hNf8juDyFDW6c16r2tLdxSLTOVRt1k6RqReE2dGMxDVa9mAWvtzFnMppBJzFhqs48VkzOsd81Me7jV1fhaz-ss60mUlyR-VQrd4NKF9Z9im7yR_jCqMTNCdHmmPXLCCf8XbCFrG3uhCXWoRrYQaBk1HG6g0ci-U9sirLiNZHeuk8-OoDQDtSgI5SYdXhO5MBiAOnl7G9sHwJvLJbV-5dHHhn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=d9aAXMJF05465Eb9rJ5j4S5PlLSa1H78nF4KY5TxTxQqAElI842AQFeRXQgqU1dGfzKHEIJGapki7nvdCuNIsPZxD3D_2ernUNxgJadu4HnF5i1PczP_Hdjl7p-_hNf8juDyFDW6c16r2tLdxSLTOVRt1k6RqReE2dGMxDVa9mAWvtzFnMppBJzFhqs48VkzOsd81Me7jV1fhaz-ss60mUlyR-VQrd4NKF9Z9im7yR_jCqMTNCdHmmPXLCCf8XbCFrG3uhCXWoRrYQaBk1HG6g0ci-U9sirLiNZHeuk8-OoDQDtSgI5SYdXhO5MBiAOnl7G9sHwJvLJbV-5dHHhn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njR8KUluqEglvFdumCQA2u6ggVHhMI6EGrYaHhVLmavQ1tJQQZ-hpgZoczIjcj8uBVFv-bQr_nEDq4UDwDpvM8mH_WnmG6q3vYSEVQ-yOLCAYFTL9KYe3kebfqCy09jtH4Xih1gk1i4DH6I3Upjj24MTBRg8NCxFNEU9vtJRZa2Fk0s2on_1z3NEQTdPs-S-qjUj1B5JYuYcaUdIV3TyIHVO2E89I-Dd-JFWLlRMxQPr1TNaIADWzRghZUXwIIJ9Flx29fiNIXi3S43OuttzaH2zP6HYM7Zov2bIvW_8ozdGCr6ArUh2VUZMezVRn9MM7n8N8GjfHcTOzZ7ztMkm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QZs-n0-2WGgbPKIFHIiOcI0VDsNyHskA87RrTZ5RDqg662ZczFHYOvV2zA_7-prLQKtvWtJ-ueRWdqlMvj_1NX2KLYxqvw-tldqVfxU__wKojuWlJwG_4HbxUetxEGgnm1xWQCHtVkeGZHeP801opy8bparTJL8rQeea2WaGEABzX6DgJtdDPkYhyZlj_jUOVmbBNoNIrY__kij1oUKC2mWKk1zpDZanNVRHnVQpolMH34nIHtEK0xMNPQdu_wFMLaUPxaHyieiUxM6joHK04IBZpr3Qhhzh2mbIEEQ_t1Lh1Og6cex_6OCQjn0DgtKti24RHhc1QptP5nT-gjSjdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QZs-n0-2WGgbPKIFHIiOcI0VDsNyHskA87RrTZ5RDqg662ZczFHYOvV2zA_7-prLQKtvWtJ-ueRWdqlMvj_1NX2KLYxqvw-tldqVfxU__wKojuWlJwG_4HbxUetxEGgnm1xWQCHtVkeGZHeP801opy8bparTJL8rQeea2WaGEABzX6DgJtdDPkYhyZlj_jUOVmbBNoNIrY__kij1oUKC2mWKk1zpDZanNVRHnVQpolMH34nIHtEK0xMNPQdu_wFMLaUPxaHyieiUxM6joHK04IBZpr3Qhhzh2mbIEEQ_t1Lh1Og6cex_6OCQjn0DgtKti24RHhc1QptP5nT-gjSjdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHOm_d2r-YNcea3AEi8X7MBzbFl7DSpIV-tCqRT-smev8J79JNPjhdtjQzJvOjZNELdjI3OtDWNwjadmV2fb0qmwye3d1BdS_M7XK_udv7ZAAkFs1KhVJptoMMembBy0catZjCT9mTr6-q3CLV1rQ5b0wBwdSkrRCNt366-MDrBqJq2iykKKP19Dg1z8pEV1X_8SRm3wVdszLHgFw61PgpaQSt8V3s2QwWettCkKbyKfsnt_c4vEkwM-IYRUEBtxWqYzz75USxATDNWG2vPyEZAcBHecCZcNsL7PVCg5bQ_D2BxrNGidkPYcX723Qb-77xR-loPIWFHIqz1lt19d3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGIbFF_W6OXkZNj5dX1CXpCby0v1FleksqdZjiZxyCl-jJ90_mv3k_GkqmxL1wdkzgNebJjjnLWMHTqL1of2EwGix5rLSxxRyLGS3gNAda0LSvK-0QlFg80p3t9-pNRnxbDTxCAcHaV5iISoYPnMC-HCeo5neo3PIvUzQfkJcUcWx8RivZlwAhufVZOKpM8JcdwRttQvpnMvdK1iptKfE2bEvZ5SUmr-UJibkBcwqkL5H1_wrla0W4iu8ESQlSbjcu8MXBXNtE0ArREky3kr8INCTKrmlB3-e-pKPejVnFgrfayGfKnvMvGm5oZb1YSVfhoMDY1s--TNjZHQbUpFPMbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGIbFF_W6OXkZNj5dX1CXpCby0v1FleksqdZjiZxyCl-jJ90_mv3k_GkqmxL1wdkzgNebJjjnLWMHTqL1of2EwGix5rLSxxRyLGS3gNAda0LSvK-0QlFg80p3t9-pNRnxbDTxCAcHaV5iISoYPnMC-HCeo5neo3PIvUzQfkJcUcWx8RivZlwAhufVZOKpM8JcdwRttQvpnMvdK1iptKfE2bEvZ5SUmr-UJibkBcwqkL5H1_wrla0W4iu8ESQlSbjcu8MXBXNtE0ArREky3kr8INCTKrmlB3-e-pKPejVnFgrfayGfKnvMvGm5oZb1YSVfhoMDY1s--TNjZHQbUpFPMbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vN1JP3WGFL329Tp72ytx-siZRf48LgsdvB-RPTwtU61FYxkZ_blC8IkRpX4mqXS2ru3xa1uakYdlUABH0WnBnc5yEJ_kQFtF9SX8uN4ydrG_cwaJ0bDmS0qufscUZL_HH9g4T9fuRrKb87Qb7wNFZKaKXocPnhU_iBN0upIuwFoCoiC51fCBtGl-2bbHFSYVMjUlk-Lo9LSIiQec2mh8cmElRXQmRtExFVMtYugtWUXk5kzhG7oaHsGXumbRDvU-quuwcmaGjAmc0aE-r5f3Qc660oYaKUFqeIU-3SayacwTWnLkNovND_g_pPPye8eR0nASD2vs2aR9WzPEYY7Vxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vN1JP3WGFL329Tp72ytx-siZRf48LgsdvB-RPTwtU61FYxkZ_blC8IkRpX4mqXS2ru3xa1uakYdlUABH0WnBnc5yEJ_kQFtF9SX8uN4ydrG_cwaJ0bDmS0qufscUZL_HH9g4T9fuRrKb87Qb7wNFZKaKXocPnhU_iBN0upIuwFoCoiC51fCBtGl-2bbHFSYVMjUlk-Lo9LSIiQec2mh8cmElRXQmRtExFVMtYugtWUXk5kzhG7oaHsGXumbRDvU-quuwcmaGjAmc0aE-r5f3Qc660oYaKUFqeIU-3SayacwTWnLkNovND_g_pPPye8eR0nASD2vs2aR9WzPEYY7Vxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-SjK6djsop-zMfwTrta8CuilUV-lQlhOT4vg_xMkWYVRWFbVLFI9W2zOFLvos8GAd2sk_8-6u6pCcMkQJIsPtzsm2nEEqHi1JUdqxhW397x_T_-gKQ0chRYwPR1vfxjJ3kgZcKAPBMU1KdPy5jYICpJDV7abvSc2W4MlfPDGa9_1_wLTplzut1XS1c49M0Jo8LXayTtEm1AclNfyEaVz6UrTr6EO2iQeCJJQfA3qh5KOzp0GzCOniIltRDlQBCFbYmlT80m8D7YWtZVJ2KhW1qG7UTwkwPSokOSon20lyzXvYHRR8x0NhxcUX9gSSaNDXIMLQI10nxOcJuLb1Krxxvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-SjK6djsop-zMfwTrta8CuilUV-lQlhOT4vg_xMkWYVRWFbVLFI9W2zOFLvos8GAd2sk_8-6u6pCcMkQJIsPtzsm2nEEqHi1JUdqxhW397x_T_-gKQ0chRYwPR1vfxjJ3kgZcKAPBMU1KdPy5jYICpJDV7abvSc2W4MlfPDGa9_1_wLTplzut1XS1c49M0Jo8LXayTtEm1AclNfyEaVz6UrTr6EO2iQeCJJQfA3qh5KOzp0GzCOniIltRDlQBCFbYmlT80m8D7YWtZVJ2KhW1qG7UTwkwPSokOSon20lyzXvYHRR8x0NhxcUX9gSSaNDXIMLQI10nxOcJuLb1Krxxvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnRuvcebQ4rIaqp781XeCnhLFQAg5EcgYWb6N3b3F-lHAC08nzebC1E2tENnMdF_cYNaz2LznANulx5u1r22WsJBd31Hk718229yNV4tF1jQAiFgW_6cKIn-ECUMWawfWotBTw_4Rt2PR3m599E5s-QQ5XjuNVl22pOrbJqPhrJa3df_R-8uJCU9mSgMzq7xS_ZkydfBA4yDJlRa4Tb6VyA7fMKtKJkRDZu91Lq6NLDjLdwTNwiS9DCHQ9pF2QsCI7QJnWf4jSn7HAamiml5PeIpCJRhREpeQ-khCN8QIAtYfeQr9zV0AciFVE80-ntQPSTEWPJNYh-VrInv7uUIaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBIc4T7L_2js1Zw31CcOHUOLgal9lXibh1phZEZyha_6Y0I8MZW7xACGgl5qfb3yWc1Pk9jtcEr1p1pLI1tWemGfx2TtPg6Ce68HdzHfVqVkT-A_YXsGPfVUCP46fO44BpkuXidPd2iGwXyo2-tgpXJRZjwPm8qufxJes6RBlPMFrqajYbhbvwmnNzBbAkZeKUNveQymjFIPYxOKWE2UA8xbEjdlmDj5spPK9vj13dLmwnLIt9x-8gX5Gx87cxiQtCFPx4_LweZGkjBqlvWgzGx3v8-AgWEwDGj5qd9nnGLqYa4IuAaS5-btyghLNhWb-8zZmHjL96O5GrBUsmdntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD2Vh_NwTKiUVKElMQkA5Iw9mHPCF8jOMUubMMzWOge1RhNy2tj3jDmRf1tJBj5NoI3_FiGqriyMIRg6n8zdmQvKdI9wpGXd2jgTGli2xqriV4lMJjAnI2el9xnv00STYyu54UglmFIltUyHWIhU88pIr8a8cOzNHjh4KtqpX4HloTy9JaI3UBLK0G3m7kFSP66QoDHM9rjLaa41bgSjSMfYQYDa7p-V5LDLkbTCNqzHxwofDEUidwj9DaThKS7NKny-fGe_brovK--ceReBfPPaveB09olCLHPyd3bH6eJ7IqpsmhIYffZo1LXeOQR9_yk0SPwPqXCC7tfYk_Sqcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKbDwmbyA8z3GsWuupcYTbXhv7xt6zd8lOGJUBYW0QWFOcbk1dMBSb6am9xvwltJ5uyMHW0e2fipFi-lJnd5QEhoSywGeS2uebkxRB27QEIoRqMecdtuTBiHcodEBq2BjHqf4yLnzCCc_iJLVlTsXhAfTwC3Gse8H2JkQv1a2c74-1VnXyCt2-wQJCowIgtn3w3xteYnxE-b_TtnsQWsOjBzOLVq3bkW8X-DiBPRUgogPpe_5CYHvqVOyrHQSv4n47Dyq8ZC6NBaIgGYHTUZCKVvOOQW1PJTR-IOEVadAHKEHE8ROtz7g4WMMZHcrtOgCwzs-_RyauzcNt5rIJpeVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bejPvNtpdZPfTF1w2F_s25cLxSfDatLbEtZNnANME52-HFEf70ST2wk-QjUjnJRXz51xRM-vSBJT3n2HjiFRWyxvQuApx9-lpwXYEvvrQ1hnLbLOvCbQCYUOLW83tIy0KERHx0cGQ5nqi7sXd901oZj7-iFbX5npRt9ouxuM0ngrfW0xbmwhIYPHQ9iZ1CqMadeh2gSdfLZuBgvcjQYDuQhfPV3CqPO614sMwd6DVcnZE3dYUTPcYInqMCmpfgbqhIxsrXBOTlKJFmS2P_5P6FqXoRFYBXP6b20pqEegF_1BIlXO2WgomPv0Ahjv6Xe1xHSjv5HOfsZp5YCfu639eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLl2PtrMOkHrmqEF3nLbEXsBIPXn0InF_WHez6zCzdVth2bvoTwOuzRPFinNr8U7MpjTGgJHpVZQmJB4_Z7iSo60J4Z2Rv4visU7_XQqxOIvA1AT8xFfdKsc6kijkNMzhkufDQW7I3D8BQ5uwNGZtBc6ssEllMWVKtb7gXrLrxzSv2NgP-gWaP6GIAI810GRVmHL2bmmtKS0gOkvQCDM6nltHwVzCify72Yr4i9qbopovqYs0tLg3k_C_mnYcPj5EaQgZnZ7TsrE1Xh0_c8iX2CkD0JWQq8WDAWe_4_guDkfQTvMl7W8ncuWY8j0SOlFgrpivNSxGpo1HeJ5SHebGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEH8mm5BZ6XhHZPyGV6oIsJu7ykMbYaDuzLNJH6SmtT376J-NC4_rrls7k9fHq7FCCtxvtf8IYkIVryUMb2V6M0U4zAuuZBMHoFQPCiaAgUUzB40paqxGSuEOFQ6wmFNci4M8UuoU-y0MFo48icb768ApZkB_jUqxBqbYMbbmuw5orz3EKz8nWcJw9stg_CfUT8LTDHOipDWGCk6wgtA7ndpVBHZZVfvQkotLHBXBBw6ShHb4hnYBsnu4H_3z-pJfwAY5m4xk8mLoZHZLAIkkPXhFb6xoIK8wgFuMMSo6hM7_vbJm_fDt8WzWJVqyaRq_ceVCBxsEfOOJTwX1e95cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCGntCGBgQ93FOZNf6iFtFChTloPvHBCeNfvqR6kkqA70VTErhPhKka15LQkQwI1Ph1JITVspiztiS3mVeDOrnYkqUTMMtYBylMZmj7I-pDmKMI_NKsfUd-pMnUUX0OhgvlbdrjNvBR1f32MLoCuYesLV8Zks4qQD5tDdmwwUW-AT4gkuJot2C_1AAC9uHhm3RBRNkdNU3es02JQ2RbIOu6y1BMVH_FE_K25uWwwkI-2StoMqO7K1JY-EpKRvZ2f4YsUK7i8SNU9vo029TwE0KLtwC7bz_jPY0OQiA6jqNZDbqM9P4Y5oeeeXU8wMRWWbnkyzLZOrJdSdfOBmd1RSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYRErpLnfG4xwNI2NOQZKOh0srCW6tg_312f9gQRapLr-wTB0_j-66zDTdmZ3QJcBCf6Q7Dcqeq0hBjuNL5irCKqoiDsKYn3vvmikFcg-kKoPws42-xcoqn3zJ56KCeADbKPRQbKPJGrsfq-7Efa0o2L6AZJD7LmcBWVea1eNOSnm9TD82s6_rqlL_sYZ_IB04EHdagzGP_LnY09xdsZAFwpav8_3hcyOoo_1aiGafwOwFlfyM6OdsEtMO9Sz_tAxFP1yoQJ9ca-3DqMczboM8TvoeOBYXxMSTT3_8VFq8IbpBfInDAA7ImJ9vHUZGj-d4HoNZCstUT3lX60iFc5jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alARyQsLYhcdGI-p8i9n9s77C9DGoHi_BeNXZ0aUNnAHRg9x2IlYp9mdxJER1OZp_4EyDzD7qeDb79lW53HmvWlDG7lxRBKlcPN1656r9wL-7IkJD2xrlJd8j_m4EsA8wpgZzQcPwjlEZ57qxwp6UuH3dChMPIanBinCuUdPKDtmjjXxk_KQIZ63GjJcBYblI8liDnSKdWh_Bw4EYGuwASa41_MjVT2-MtJB5cqZP8GHkqADf6DAlVKIZMjDyB8XJSwF15VRXFXPeaQUaQUrolUyJzxO0qZzY5UoEFCgPYYLwKZfdypP4fRqb4eerlqRLIbf69PGv5axyRXSNnInqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gti4iiMXlcmIlKHXYw7YpVBdKDjACz0ChC3_0wYlgfyd6af49Wb9f4YAGS-JcrPYHX4aTmxgmMUQ-DcuuSieY8g-zHj2J_D7jYX5qbHvkQRvTdtR7YVlrT70fgM-_m-VkuLtHaRT7qb97RdSeR-P1imGiphSl1pDmFu0xCkqfPgSz5hkagJztx1VjBY-HgPCNXPFFYAdup3U9ymAcB0c2Edzm8AnEaZLJaiRTSKfnW4sJXen4GfgJz18HTAuka9wS8jMyZ-w-UWJqZb9AgG4GTPwlSNncF3192vmbnX1jQCzwOFflKF3Y-qyG7_dyMe9_nKx35sCuYL6VyQ1Pqp9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO-JJKxQx2kRlTCNAyiFKkdQpAlv1myveWI1bhRpn5LaMPu6jeir4HwbHT6sUtH5xpVtj7rzliTqZtFWc0b0u6alswq0F5jO0l2iJu8XnhBVxx9pCfbxlB1i3hiDHUyJv95YpuBJIWgMrc5loL-7W4jWLH6L_XROZPJ8bLxeeiA116yF34VQTUsL1hciML57yZJId5D6OL_c_JVbG1FNPcj-xBKyZKmA1tw56taE0fV-nhprKAJm_NVmuVucu1B2icDa5rGnDJ-ouWVV3DzVAzJAtb7QoFsbZPcbBHvHcS4UvZZn3vTYh5EiW2FT2iVb3rRxvtSK0rjUzLzPyK_aeA.jpg" alt="photo" loading="lazy"/></div>
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
