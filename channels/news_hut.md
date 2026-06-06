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
<img src="https://cdn4.telesco.pe/file/qeghiE8jeUaI8iy7zxIkIG0DnkQ3UgsNuSCjJ2lwj8uOgij4MwKXcJK7gT4TA29EGphsBdLksGURx2IoiQzq_ScWSecjUzg6EOFPGiEHO3Zs5ZWma1jYXre2Va82CO_pQ1caR4nH7fEIY-ZovabaB6OvpJX7sYmScLjup-95iPuAZL1h3uHTHCR_9MLHX0xYns1e5nmu9doYWDXZKCrHATJB4JTL7H-dDqFos3eRjqkNpxNXbpfKnpNciYVms_GOOkKb_Fv8hYuYRR8SfYxxLXlaODCgBSyhErSFs1KIn-3NUFgUK_hGbQDpXO4AFq3M6skobeWEu0l5Zq373IA9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=BRmcZRcd-5urSXMbXW0BPcjUj72XeyWZ8F3NOak5F7kNBv2AhnYHrRaM0nZE-Zq-bmPaa2MZQ66wCW37r7QB015RY2kbCB0vlIpaLCEJ8ws_3ZK_qbiBcxFXUgxEF_CWgQXGCSqXnm1ABw78WjC8r350G3Jq8IffalCdN2CIDSMWZxdcv9FJcsj4Jwaudd4FEy2c-r_VggD5bPznuC5EyNe4TT7jnfJqiKSAG_PwZAk5mALgx2mAZdroJcAkau4EnbzrZr_i--5Tncnv0EZFI39kEsOakR1y4QONt9L0_lbt2MlVeV9gxJy5pFcKFdAWmZU6QK84pS4mnbZEhSiUng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط یه آتش‌فشان تو هاوایی امریکا به شکلی آخرالزمانی فوران کرد
الانه که تسلیم تیتر بزنه کائنات انتقام مارو از امریکا گرفت
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJcIJZoR0nJQFjO3bLILI2behQ6eXgzFAPWu9pVgmSYXOX4FhRXD_4L39tqZrlSZphfMcMLy3goFbKtpwj1I_eGTD0YINJ4FruGH7zgqZ0wiwPO65I9_usrXu7CbzbWjHLXRO8Z7t0_GjgvX0uPLDlxs5QC0GMDkISWp0N4TiBKWEKFSeBrPGK0x2YzCt92iUQ5hpOM-lpeoDsYstRtt7wlH9xuNet0XpKXUkoVu4YvdSud6WeqPlSHp3WfNTn7UX0FYUS1342rsAJTuktGZnEXTa5WYw66WYM7JNuBfASrr9KdIhqosdPFXXE6aZVPYzi012DtUlfl8XLipo7xa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJoilsnCOSS0hN7TiXSKCk3nH_0REtNYj3C4Sg2qak7bAFn_vcLx1wv0_kkAg0PWwP1XK9FWdpUMrqTEv0XkpHJGYw6h45j-eKr4gnujygo0vhy5ASk_oWQq7QaiaOgVj918awLRYw-SE0Ok2jWj-3SnMenR9UpdAvZ2XZ8jtjT1wqLbvRP078oUNpPL9nDcsTtvhlU4iQHfvnPyop-6l5UIgltP5D0IXspxo-JAYofP24TIQh8oXjsBCbhN7DadmLeJcOLdwepFPqTyaZddNTiH6YrW1DGDOUzixkIjyzctHKPayy81-5bRzYAq8g68Qeo43BwWUciLT8cNoa9X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KW6xl70wlMU3oa010Y__BnOrBb89Iu7Xe05923jQc_6bFau3WG6dx5ynpKhecqy9Ecxsy5D16LpQ4Q5fPLGSFSiI2HGWFBbwGyIwiF6x-3F1EyInjw6hfT-COdWUhzsthJsHTe-ufMYtQn8yHR5sKqDUu6MbUuWzlSOnFtp5GfwLTrwTcP9rg9qPjOjl7i2KIbUmN3j9YlZNlBhfYnGsh1FxiciAYE1dOP9cwa4eKEe8mua_E1D7XAiUw7bNr12PMnGTKMAzs39g04pOB6ZQ4bzrMPEerHDdZ-Z_5knoxN6NO0uUk6cu4CGEiUxw1ynPJuHfQhSgqTW_rYmZ-RBl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxdxCMvUFAhSBM7fsMrP1dnqBrub-MQIfPjWDkB6jtkVxjVLIZvmNoJhrggxSTddapIdvYYtQhoqvU7UdUNgkKR0a3l6GEnggqIDqVKwfGyag3Dl6Lk9Jmie1YfFYFlGNxMlJO9xAcYCuaiStDBjIia-k4Vs5uCzMdEl_Qy32nwP6aAyc9m14mKK3nQ7yodFjaeANlVVLSDZaoggAOUa1jmx2oGTxUSfwpkG52piUxnyeIXdHRcj1YT1_wyBeJg9PYHDgyBPLC2NAEa8v4Nj9L13M7OkZgrgYY7ZcaAYEhJqYXrVvZB826USy-6e8f5DgJtBYqXaWxKkC_nTMxmWFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa546373.mp4?token=G_K7kwpThL5yrr18HSrjRqjTAZ3pF4Gmv71JfxsjLcwhPKG7lT8gN2cRkOeNMbOvb2SOzsxBszjAsq7NwigYME-KADWmQAJFxhZWyGbVez6vUkPmT_kirNh5YRdCcD9BKelLcHJs1BsKQrrrotTh2b11yVdw9tns1e4-JJ04FKwC2SVZrLE9ZSPmrvPhTdWnDW5fRdpYOTKIV_2YVzghdCPXfvbe5XhdHtYWNMWrtMOuYq_CebDApcsWH12B4NP3uq8V11U7G_Jk12X1JfEnBj-hcMKlbZxsYDezFMQ1cxPDSINMkeuLrDM6M495A453cz5TKjccVV85KLQcLGbkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بعد از درگیری های دیشب سپاه با چندین پهپاد و موشک به بحرین و کویت حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65338" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIamXerxess</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXMIaXZ8SKnVPVosUb_DseL1nI40jXQf-8zy2OBYE4ow3RJYLCoy3eL-PkULlkMQkV0DVaIg9yxhQpsqGgTyur66pQMOR8XnqoScskdi4LZ-tiD8SZuVhw-qOuS3lkoAM1o0pGholGwvvNIdcHSzjJR-Dqc-Ri51uw-LQrm_7rnU1W6jlg-Rrt5-P_U-KX1fEUeUx2FB3rLGFzHnx2wyu6HpmJdZ62lJ6p8GQnaXIE5VXeXd2aTj0-zjZeuVbMga91v80lmLtU32AKhh5RhfJaz2kjVJw3cgpj99xyD0XhKI2BoY6qaADiF0dJn7nTglTCX-WdqdIleJ06ZoJCw0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥊
پیش بینی بدون ریسک بر مبارزه
Muhammad
🥊
Bonfim
🥊
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LladEuRVWOXufEgB68FdTi2sMUZSuuwIsFBDeSv5cYSoLswBgd6yTuSZcKUzwVfq4vI-r_ABEpTb3IQVw4PCzLRsQ28lR0xeDsDbr6vvdk-IMg0MD9U0ub7Zp3kc69YANnfkZZpNO7TIlyBLzVmqUdA9NmbBmXPOvEAVfPffktWY5bkzaVtSWTVMrwzdf5ifbrP2_voE69d4d7aWNS4zB1s50CnmoXnFDUHua0WLxnlUNdPdynMiOqtXF5UAUznasT4u4wz64ybhQJ2af-eJ94SvmyIWiYnXoIboI2oCKYrVDOJOjWRyJMjjBm0UK1MwN4MGwTxE2EDmPdPkOq2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQVUZ9qaa8VoL555zTz7uiTTTJ93fYRbriWVe5x-tUay-ybdVp9SCssgmKzdRuqIJs7q8RT7Ct3ndJTSKcDcDp2OriFpewDcoeRWYCPV6rBfOmI-oiykPvO9EPxelkJbxL3voxou9fN1W29kq15jei4EWemhEbQ_u0o14ZGGQPJIiOvchXMZYd0qjtNVnhaOLVy4jPq9RtbDgW1TiyaozJHeoTMXYTmvcQL-ZOjEqqE69ZMRjCVA-U-ElBL70tfMRfIKmD4pUpgYp2tAKnrfgru_N8Emf7grRac5mcZHWkCpvBVaZ0lM4TatjnRo9KWG9ZdnqyJPmGxfIT38MQMjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887b98bc21.mp4?token=hABZHLDuBqfun-vP7isEWkomVco7JuffiIKyl4Er7uo32INI6on98CzM3kGQYiStp_IM017quPbmCf2iyRo5xkOX7XUnRSIx5he0GiJwmD_Frlx4umOYqsJnt31Sbn-2-Uej2YEbyKAEmFyhSVEHX86RIz-B1FVaasNrkDYyqFKqKv5rLyQIQSi3w4J3dNUuR6Ocv4MAtQ8zNHJF4M9qKVKviYrStWaCPvsdmMWRsCNoe-G3gQe-KBCC9nUlq6BHvoLBQ0pjqmjET4SyR7XryU0jf9PZJiRV4gl0tePlXSwKP1vC3n-KAU1PbSQCIv6G11QcpuPNIhWkLLHahyK-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: ایران با آمریکا به توافق نرسیده است چون رهبرانش «قوی» و «مغرور» هستند اما «آنها چاره‌ای ندارند.»
کمی زمان می‌برد. شما درباره ۴۷ سال فرار از هر کاری که می‌خواستند صحبت می‌کنید.
یعنی، این باید مدت‌ها پیش انجام می‌شد. این باید توسط رؤسای جمهور دیگر یا کشورهای دیگر انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=vBG2qlSXCgi5FzqjjlxS59-SU155wYHqpzosPCJtd1on9QBIWgd1to3woFxSef2ZYfXscs2f8RBo20kKhV4Dt-YQcnnVy1ghtq8DNZ9w-LEffAEvQcXxjlx2wrRC39kArpJVHvYEuR1V6tZAiBLPlHCM69KvNwIDSKbjW4n8QDQgfTUn2FAgiVV0OmY3Yhi5BVq1s22pGjHMY1vhuOUmbI9I12CbyS2I2AbClGNmGg_ND900tbssjhKEiriorv02x1KcjB_G7OCoSRPMWA8Fh1zJJ9nm6osfemxm9aNWrsqA9gfyrVcZ__5s4umJerq-OALKdVy440RXcZp5PUs_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e15
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4ZD0Y3Efj9HCxDsHNectq2yecEM-BjsYiayyKOI80AB1hFyTkVA3nSpN2EPfy8SEAW_mcR8PTxPZMXUZ8J4yrb5uwiGwEIdxkhtvp54aly1n1d8U_sS1ggmi7CoLWKXn7KQoAvBPFZyMlk02bLYVvj5aPNHkb4uvP1o4iT25L_Qh5SPiNGx4F_eI_SqLddVFwwbnYy_2f87_5Yc_ID7zHGxHKrReFWGB5audEd6Lfs3DFOlSEWA8Kd4nER-RWDNM0moA0klptKYLBd5SdobS69bhp9iv2RSLTKeVcs_ZUGU-L5rCMK7oTh2df1wbYKc7wrFqVTVBUgImJxNol1P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdccc3a3f6.mp4?token=apzN_6CQvjE3Vm6gemZIZjrx_RcXWHl-ARg4-ubogeLezrCs8XFEIQrbF9Lx59ck5lHKO-ge2e43rSxnvVxbiGvFyihBRXnxZXmA1rg-b6o_mRak54MsV0jLh6N64iIxmhpx5x0s1bJV3tmOwafFEKfJO8R0xoQEhoDZ5V83dxQKo-6fKWwCqyAfQHIc81IytBACDezAQTn27bLRlx9lZZEPmiURIIAQyPRn56yp8Kc74wSCq6HGk8qYhh6u03uMTlxxxm5AeWwsfLA38zlM1tTDJkQ0ML3tEc7zHW31JPxuS_B4S0Fsb1X-sV8E_6tRYVqHvh9LTJWpoXmgSYBIzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد.
ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba9ea726.mp4?token=M9umTfjhVW65jgZ5FXElVFnA_2pUrnNHfCERa8ozMEa00oPdeS24p7P4QuV-IwL_6Rstx-ow8_DGA7M-MJDvQ-jO872UHAlk7x5tm-X8n97qC2usbhuJp9j7fy75GNKdXDMficehEPJeIfKwx26RP7urpyQExShBACuGD9_VFH2yUYpRHhEaFE2l7OAygO2EhxYNYs8zy_RsLY6BNxZDIxPiGVKCfSAY-JDVm_qgaX-FcL7YoOEtZblG1yXhlzrKF7fEYkODN7cfzuVZH1Xz_BJGrYXLqRW6ks5kyxCrbZuOTASiGVpbT-92lFyE1k6MLJveOc-ht_3xN1RUfRNudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
مقدار زیادی نفت وارد کشور ما می‌شود و مقدار زیادی نفت وارد جهان می‌شود که مردم حتی از آن خبر ندارند. و به همین دلیل است که قیمت هر بشکه نفت ۹۷ دلار است نه ۳۰۰ دلار.
وقتی کل این موضوع (ایران) حل شود، نباید زمان زیادی ببرد — به هر حال، این کار انجام خواهد شد.
وقتی همه چیز حل شود، قیمت نفت ممکن است حتی از قبل هم پایین‌تر بیاید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5enZftL_oUXzwdzfG104wQSgK1hlaG7wAOhvSZf6lENQXMP_kLhYGcli0jS8xfSIXxt4juk2Tc4lvCAMih1sTMVZ2tQLnA2M_VQXJHunBqwfKMyrB-7GGJVhaxAeyJBPOVtq_-IHOBlAndaqigbAkY9V2kEyzRIYxc8HCGA4kT6BZA0bIEnnhPc_Gz2evaWJJ2GWlQpOihsh2pDUo9JQtr6ygGC-xd9hfoPCHfjdErvM96k4JM2mZrRaEJlI1cbeWQipsP582qZeiemccnLJGc-5RnxEb6i13lIHFGz83aNnuFdlc-QZvp47ZvtP-xqrIYkQXxbQeOa799rdI_-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhi1INbTD-9KGiid6nSyRXysoyi90ao5Atu6VcuzAbXInzeUrKW8GrsWDN0r8qjn3v_RIBso6Unu6xegfDMhBaTdomDlGgKuF9krbP6nAXk1cpAxQ6b1jX642AeTAOl5wlxkaHXSMDpx9BgLHL-juKbcoJYg6pXbcxj_onu4PqwsgGMOr5xcV4-3p10erIV4C5zGDyzaabAnzKUQy4IyTCXcI-jZ_4U4sbxfupiR6ZWShkzbkghmAurrUFHhreTwYK-qL-8Hf3AcKnqnGutZq8GehrMJHWtnoP0u-OFKbBX2UGiwgEyYU005pxEbYpW11cqh37OcQIhqp1um3NYhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWQkPtinq8b1RGHLGh0Y_1wAJs4fqk7YeGmtW9JOEhUzN4NlqcwwTW5-z6ckYBsK_13wBh-DyWaA0gsZozeLHEPeeTfe_bxh1uThAQSbr4Y4GuzZi1gQqEAPN3lVHPBkAWcBsYmHX-w3I2YvTfImmRaii1Wu_aXDdEAYKhVsFpvqrootD1xG12WQhmSZ6sVgbhADOcl7sC13nlTfHcATL3i6b1MRdD8pO1uJ2Q91tGOp_pnKN5tC41FtM0uehqldYY0xatS7tTsrcDX06n2d_UUQk4FAWySP33fDf3mhIy4xfXUO2Am55spateUSPkWl3OKhb4geIs6kwG3vQOMdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ya2vEMaDN8NLgqfZ3ilE165IQv6SEVwRrIcGnaPtsMzDSOs-QP6YFgqrNBiDoJAKjGR3eyqPdlfSYlUEXBuErHoovCCvKlYOHKATRtX2dypbH3a_3xQYP-2uNJ6B76hFj2l9O4nCP-BOd_Xiyh8q34zWykCDLS8FBnQnuEzEBeWfzz6JrKEKR0xOWIb_YWp2VjoVVQKHyYa_7ZPdpPr26p10q0jWdPnLjDR9qP4Pgg9Gq-UVli5ccCfSMo3GDCl6as4wUpDMdonw-JXIRVFo77cyP17FkpLVT2SGkbwLyo6J0RzRp2YRoacYMJrCxfocyOfnvxdlzmxbuSZSIW-NPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=Ya2vEMaDN8NLgqfZ3ilE165IQv6SEVwRrIcGnaPtsMzDSOs-QP6YFgqrNBiDoJAKjGR3eyqPdlfSYlUEXBuErHoovCCvKlYOHKATRtX2dypbH3a_3xQYP-2uNJ6B76hFj2l9O4nCP-BOd_Xiyh8q34zWykCDLS8FBnQnuEzEBeWfzz6JrKEKR0xOWIb_YWp2VjoVVQKHyYa_7ZPdpPr26p10q0jWdPnLjDR9qP4Pgg9Gq-UVli5ccCfSMo3GDCl6as4wUpDMdonw-JXIRVFo77cyP17FkpLVT2SGkbwLyo6J0RzRp2YRoacYMJrCxfocyOfnvxdlzmxbuSZSIW-NPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIxfVHfNMpB0RPzh1oDU6m7C0DodXHMgnmwdgfr1xeMicN83_9IpPHWem0_pYeyXulMFeVLi1KqUx8QAukE7401fsXNATm4mPAUBUMLC1dHpxDGQrOlFwvBOSdtqUoeJz29VCPJ6Owe04W6K4poJwvEATNUso8Sr_BXF8QvY0Y-FzzsYiT3IL4as_s-yvdYtcl08eMLjpvJShR6hlsIoXkuF_dDDPqjOlZsjFFiCFRn3JEW7KYWcjkBey4M9efsA__T3yw6MwSvUc68V3G2_ExLLazyonhZUuYf2ItG77EIPzfwgsZXgIaWruVvjZ7cBniRbEkeUHLb52FMjWXpbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QZD3R7a1gyNGoFG9q5vGUBRgSoaDt0N6EaCAM_bmGxa_CFUOfQNMpjv5FuI_gymVYPJn2fXnmQw26n3IHDGSIcRK3TSYUj9pLCvkE7v_NnpyBnEVEwgvgqnZqGV2WbJD3koxobvQ89jYYQ5hfyMWD69twA-a_z30hlEkbmf8_5dtAFHeau3R4bz5LqCmWaThRjRx3MHu6JHCBu1xNcyhhzHaeG70GqGVqbkRnjYjI7HyiVCXonMxOpWNjm59O7JGrj7fvx7cSGSUifHLU8nbUfkenZlfjyMYtFMv1D7EzHItf3d-DtLIF1afID6B2mhb7VaJYX-IsgBznNYNBSFrgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QZD3R7a1gyNGoFG9q5vGUBRgSoaDt0N6EaCAM_bmGxa_CFUOfQNMpjv5FuI_gymVYPJn2fXnmQw26n3IHDGSIcRK3TSYUj9pLCvkE7v_NnpyBnEVEwgvgqnZqGV2WbJD3koxobvQ89jYYQ5hfyMWD69twA-a_z30hlEkbmf8_5dtAFHeau3R4bz5LqCmWaThRjRx3MHu6JHCBu1xNcyhhzHaeG70GqGVqbkRnjYjI7HyiVCXonMxOpWNjm59O7JGrj7fvx7cSGSUifHLU8nbUfkenZlfjyMYtFMv1D7EzHItf3d-DtLIF1afID6B2mhb7VaJYX-IsgBznNYNBSFrgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/drDPrq1SjCIl1z5kUaEOCamiaZ_0Ji6kq2HEjfQMwr8xeWek-LUr2PEfdgWCTpDF9SIaIpnQTLnKAJNIGAzNZ1XaQtnIUkbsMznlCKka6JcVVpMcUBUG3fO8t7ZxIynZXqxw0NJhkHiMX763BbfYPdSLLi0ng9P2rd_7w29mKrzaDR1gwb8UEpFxwWoeYL_qEc3aZyLGhMe2p5QPeWqfhTIHXQm3nUGx6yAWyK8_9KYpOzQsXcTYPXOrzYogbwWcTaGrkRul7LQfJE0dlZgSarCe_gbKxAhwn4Sdt45D_EzaIk-rrtCzaO_wGBRoUrnkdofiW0RJfFRYIhxerIPdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vc3UK9Nom4LbgNoPW0zBavKywGUEdp3XTU9eg4u_ro9zT3ouran62UQlHC86ef8U9_fy_AJ9BpxlYNkHrT4I2_8LbWsoJMuwPgGr_-hAFyytmlFu4-CGpn-b3a1-wREnMicC9KubXudZSba960_fXs4tBKNeGDhC23GOqwiQ4JFXhhIwkNfy-i-8wcWVYf-XUzk4PqzgPH1fqSASzi1wg5X0QZsmRM-ftM903VpvceAcDhb261gqZixr6B5Dp-4dA-g28mq0Pwuln5X9oVRjezE1z50kjHYIucGToVEmAxpGco2lOivT9jug9fZkxUce406lE7peI_hVZPkBT57pLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GlIlyIa-yNZXceh9ce1KGTJj9vAUlsjWkY-8560BYqwJ2bPth_LGAeJhvOOQeVMuDJjZ_PBkRcOJshMRUqgZPxXTwSXazSSP9Ls3GTDbORKGtyKzb20GE23WcaKsQu-CYAE0heO0IQ2-QKcE9nYR0eJAL4EdisHAFyP4HHcglQN9WCVgENk0fk2dBJVv4ne08568x_dD9DVjCSrB-PG_JEHGTefooKuTWyQ71pSbvkrlp6btFsbBedZPS-STxR5fgm6WNNpCihkmGFscB5WeX1NVAy5jdN0ha0_LXopZ3_RCkBJmIYpcomR2iPivNd_7XfjO9oH4pPxBiori38Ghig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJy60hX1WCJ9joufOHqya5X_DKTFVG728CzHDCZm_FsdP6a9IiM-Qk5dsi38flCo8IsI8to8zboVNYobYFd06A-w2evdwnQz52CEOhmy11Z0JjJKVwmjbLx9JMO6SoHjjqSR3ymEgrEiM6AWtDwfcfejX6PuDjEb-40O2ioNlLZpUJwXcPmWWSTJo1G6OCGgtqM1ZWvwoHb6qtScz9B3EdXgQa3OZ82MILZZX9y4RL1URfZP1T1YGRIBLjYyo3Cg_UaDUvQTmlFC19am4NnKNxYqgjEAkerA7DTOOJ6tx2cMaAF6INUlzIzeIuSMmVbshA3PQurOL5AjB1w5HvRX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=cIcp7Ff6qEXdnkpYlPI_a7-HxRUVex6MggcfxLvYhlweguhfAMON9ge7VqPRJTA0C0IoBK8lifZapva2KhEIurPrTRNwcH4Kp2aM-acmASsR_dJAsDRZu__PG3NaFpPzknxMI5im2_0pdn6hWynIxcfrS98bA8jjT6ES8IIqrCDPKgXfx_O2PdLkUQQxrwRIMRxYP2_GtKw6O2WOCOLWGNBg24zb6S0tQFZdFwk-LH-9yNkuU-vqErCm69PRChRPYG-nzW0O0ZvEpSuUJWL28c1qF9557mpmO0VZG7m6T77wtVR2OLbmvLH3SFMHIXmprAPndkeWvHVWakm3MBFB_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=cIcp7Ff6qEXdnkpYlPI_a7-HxRUVex6MggcfxLvYhlweguhfAMON9ge7VqPRJTA0C0IoBK8lifZapva2KhEIurPrTRNwcH4Kp2aM-acmASsR_dJAsDRZu__PG3NaFpPzknxMI5im2_0pdn6hWynIxcfrS98bA8jjT6ES8IIqrCDPKgXfx_O2PdLkUQQxrwRIMRxYP2_GtKw6O2WOCOLWGNBg24zb6S0tQFZdFwk-LH-9yNkuU-vqErCm69PRChRPYG-nzW0O0ZvEpSuUJWL28c1qF9557mpmO0VZG7m6T77wtVR2OLbmvLH3SFMHIXmprAPndkeWvHVWakm3MBFB_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3ivYyJbWzZEGwS2edk3A2Me66Kfz0jiW8hvgBcP5zOuQd44FbKCyZ_1rF60uhyrzHi0HMT0HuXlClXNAjS8TIeI0g9RIruzFe2dtJlnE7IA-S60UIn-vigoLessC96Ir_DYxfmAphtIkX8iNNUPCQTzniJucOZ8s2KbmOlk_4U9-0Ht3cqJAmUS-BLEbcHHh2t5TfDARO2bwFaf1hg-y4g83RMrYmU9IEkiFqmFSYK8yLQCEvk_nPeeTYqLTAS_W8Gqm04JdSSL3x_pkPeixquR0pfO68J3bfOhulYDPPDJjHjir_FDdJ5FBGpCd7SfeQ9iM1t47lYkqjeSW9Y08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=vCHvAH-Bj50cO_dbbDA-0gGe8IIUQvUbZ3IniB0lCdt8mt8TKoZ4AFxJq4l_iwsM7H0UFSszN5AGlnUDCtXQLPgWlnAHGXQxMkAasEcNmdb5NLUgnzUHJqO7cn9Zi5w8KpeyQBZeyzCQJS5V0Z9T8pMMC9A2bJ6I-mLckRH85Gt0Zipo4iS8i5zeuR3JM8lDW5wKNBxYOXZUkdZF9NBZZAPexEhWFj6lEHZF7teT6_hcyVfPUyVEqtzZz3tAlo1kzOCPQ5xPnTPk24UjcFI_smK0ic3RzoTWDBgYpNP7Z4sRBko5tAlbX-4OB_y6Q85bc4kMoT94KpTnaWaZ7hChhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=vCHvAH-Bj50cO_dbbDA-0gGe8IIUQvUbZ3IniB0lCdt8mt8TKoZ4AFxJq4l_iwsM7H0UFSszN5AGlnUDCtXQLPgWlnAHGXQxMkAasEcNmdb5NLUgnzUHJqO7cn9Zi5w8KpeyQBZeyzCQJS5V0Z9T8pMMC9A2bJ6I-mLckRH85Gt0Zipo4iS8i5zeuR3JM8lDW5wKNBxYOXZUkdZF9NBZZAPexEhWFj6lEHZF7teT6_hcyVfPUyVEqtzZz3tAlo1kzOCPQ5xPnTPk24UjcFI_smK0ic3RzoTWDBgYpNP7Z4sRBko5tAlbX-4OB_y6Q85bc4kMoT94KpTnaWaZ7hChhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=oV-Hsf-TTmuGvyJqNLzSzQg6L0B5J6E1I3rOJ8FltapaQvj-Ns2C3vwaUGDi8Nn_OYU2dmKiTX6aRpzvR7rlPEfEyIoj3uwueug5qXTIiqyDTkBhJajXKUp2k45eKy3ILhoT76wOUtpY3g_Z7pQuCGYHgckl_dCGCJEFuEUh8v_npAG8-SvtkuE7z-5SRtyWRaQrkF1w_XjdU8bJ1rp0pDn1N-9c_UajIN35nplcbfO1JIwypQgTKxrAxJeLncPLs4bVFlUyl1yHzo7IUKnTlzBDr5qf1X92stSEH9X_m3Of_g8xkr1dLgd0hOiES-YzwUKUVsLkB2r-akkiRvQqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=oV-Hsf-TTmuGvyJqNLzSzQg6L0B5J6E1I3rOJ8FltapaQvj-Ns2C3vwaUGDi8Nn_OYU2dmKiTX6aRpzvR7rlPEfEyIoj3uwueug5qXTIiqyDTkBhJajXKUp2k45eKy3ILhoT76wOUtpY3g_Z7pQuCGYHgckl_dCGCJEFuEUh8v_npAG8-SvtkuE7z-5SRtyWRaQrkF1w_XjdU8bJ1rp0pDn1N-9c_UajIN35nplcbfO1JIwypQgTKxrAxJeLncPLs4bVFlUyl1yHzo7IUKnTlzBDr5qf1X92stSEH9X_m3Of_g8xkr1dLgd0hOiES-YzwUKUVsLkB2r-akkiRvQqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Hn6rIJCd0UjdVjS3UnQOE_Mme1ZK6ral3ADYDHjeLaFICjq5L8MyoyoU9MnYUh9Bqh2FVZVMQM8UWCQcMyVrg4tGuaa2nhQ6FCOGRrp2xSKOZuiKNdlhRJVhWuxvc-HNZPjRLssKpxXR4dVZ6T2JoBmGWY_MBjdXB2Likuj1rPE_bB8o_7zWhTbdc21Cz3zJjLKbTu4GBszwA814tPTX-8Azqif4qenfPxhtb_fvpKnEjwLqC_qSwjTgycVgUl-y2uExqqwCIdu5zFklUmTHhT9d6oaR-Lc8yFTOtXnjNnou0mjUjLmHp41Hyke5IHA36nPmmrCTBPuSMe2wqFYxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=Hn6rIJCd0UjdVjS3UnQOE_Mme1ZK6ral3ADYDHjeLaFICjq5L8MyoyoU9MnYUh9Bqh2FVZVMQM8UWCQcMyVrg4tGuaa2nhQ6FCOGRrp2xSKOZuiKNdlhRJVhWuxvc-HNZPjRLssKpxXR4dVZ6T2JoBmGWY_MBjdXB2Likuj1rPE_bB8o_7zWhTbdc21Cz3zJjLKbTu4GBszwA814tPTX-8Azqif4qenfPxhtb_fvpKnEjwLqC_qSwjTgycVgUl-y2uExqqwCIdu5zFklUmTHhT9d6oaR-Lc8yFTOtXnjNnou0mjUjLmHp41Hyke5IHA36nPmmrCTBPuSMe2wqFYxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=cSJTGWIExoBvy6e3a7DLTLqoTDWQpvO7kvsZHNiiA3brv_lNw37Bq8D0Obw1CLWFeObtRtcyOPli0IgAjaJ8mSVOgRghcSNSwHus5yKFrQkHsqstO3reMGXrbtLGH4Ss36knheN2sRg2D3KLAU833d21azEBmiVDdnvO1qhw8A45D9aRX3xyV4Nnlbgm6qECahcWG4w1C8VQM2XHc-2ik3zfc21fDF6Ja062yAVtDBRYV_vQ4oOsYBIlVulL9SCdaWJwqRjIMW5vEBm20QZIHCsYMqYRNiX7SXO0M8mrqCPLfkL5qiUe6YhgQt_mdd8NcMX0zXraRGOzLPLDq2nW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=cSJTGWIExoBvy6e3a7DLTLqoTDWQpvO7kvsZHNiiA3brv_lNw37Bq8D0Obw1CLWFeObtRtcyOPli0IgAjaJ8mSVOgRghcSNSwHus5yKFrQkHsqstO3reMGXrbtLGH4Ss36knheN2sRg2D3KLAU833d21azEBmiVDdnvO1qhw8A45D9aRX3xyV4Nnlbgm6qECahcWG4w1C8VQM2XHc-2ik3zfc21fDF6Ja062yAVtDBRYV_vQ4oOsYBIlVulL9SCdaWJwqRjIMW5vEBm20QZIHCsYMqYRNiX7SXO0M8mrqCPLfkL5qiUe6YhgQt_mdd8NcMX0zXraRGOzLPLDq2nW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=MBtXgDTNCJT3OKe774JCYsTaRI8hPN6mm1ATrLwZQ7d9tUdkZSf0IKlfj3xHITfk1vcK7sIHTwTxEXR4lUZdmzdlwP8UwDJNjX9bOLMQyfKEOMBEQ2ZMvDvAWCQ7FKW9Kd-LicD7imGBug_fuDdDQSvR73gj_n4bHMwpm7uZpzuzzLPNjzhYgvYwR6ruP6CAcL8E3FDTT6gV2mkmD-HbrpvdufBkf3kORpX_pRX8nf0BGyg2Kh0FDMsETMCyFUnTP33cXo-aCs7Vgxed1z4Oe71g8d2Th7qrtYVhkcKxhnYXnZZ28pcYLZSvytJ321iC50NMZJUJd7yjZZIdOLJxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=MBtXgDTNCJT3OKe774JCYsTaRI8hPN6mm1ATrLwZQ7d9tUdkZSf0IKlfj3xHITfk1vcK7sIHTwTxEXR4lUZdmzdlwP8UwDJNjX9bOLMQyfKEOMBEQ2ZMvDvAWCQ7FKW9Kd-LicD7imGBug_fuDdDQSvR73gj_n4bHMwpm7uZpzuzzLPNjzhYgvYwR6ruP6CAcL8E3FDTT6gV2mkmD-HbrpvdufBkf3kORpX_pRX8nf0BGyg2Kh0FDMsETMCyFUnTP33cXo-aCs7Vgxed1z4Oe71g8d2Th7qrtYVhkcKxhnYXnZZ28pcYLZSvytJ321iC50NMZJUJd7yjZZIdOLJxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=LQJmoH3ZwfSXb-Z-CQwjdzzplsyTjU61lvCnC8AnT54Tj5XtmnzZkcbJIZo_eh--XzICYL_2IP0ThuPIt9BPsgpV65JMi9Um3E5b3tqxY2xJXPVNnr3jbl8sE_v3F7YNe-I3whQe2Tf3q9prXyrI53JjlJKzaCaKAmirphmo77OS4K7N1PahUlT43d14yRhsaEGyXg9g3ztRE5U7GYM8Juy8s9CglEP-zr-mtDuP5OkLbXJ2lMAqq8KZQ89XKIZqm18b2VcEhOWh9HvuJbxLLOQMARxE55RnKi_gL_TioYNq5ITNk2B3aAZuGEWlZSvQNK6BdcmnzqvkzzBPAEk_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=LQJmoH3ZwfSXb-Z-CQwjdzzplsyTjU61lvCnC8AnT54Tj5XtmnzZkcbJIZo_eh--XzICYL_2IP0ThuPIt9BPsgpV65JMi9Um3E5b3tqxY2xJXPVNnr3jbl8sE_v3F7YNe-I3whQe2Tf3q9prXyrI53JjlJKzaCaKAmirphmo77OS4K7N1PahUlT43d14yRhsaEGyXg9g3ztRE5U7GYM8Juy8s9CglEP-zr-mtDuP5OkLbXJ2lMAqq8KZQ89XKIZqm18b2VcEhOWh9HvuJbxLLOQMARxE55RnKi_gL_TioYNq5ITNk2B3aAZuGEWlZSvQNK6BdcmnzqvkzzBPAEk_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSWhoRGotjno5VTjUZ-MKCV_wm5bggARGFiXQtU33HBzJDRvBDKHGPotezvAr9be9Zt-zo0BSqLxVafiN3U5iNgNuLzEzdneGdeMIegK2nIXDLNmj07GBfNfmFeeHZ1cdeeAhQ_JDPIoe_gee6S31LYdiJLNyimhxk_pfg3VX_I1xx11q8_eVBFjZAdHko3VZjUvbEQzAOF6wcsPgaYomiKJaBt_XpWgQxrsVqd3_0Kt2BZhE2rB38e0BdxDNGoex039_srJGmvnOtmtxUXWzcXrAHyeX_pb-0Mna6o7wvB_ec0UWIlp6YsPw1EQ6QrxT71f7U3LE_FSWHXAvxEaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmbAj3ftZ0JXKJJhpQQdJSaZCWBucxtF3G_pXGpd00nTrA-71DRtTwAfxjFH1_mC39l9D22tpO_Ayl3o1T4ZU_VX0w_GLbbUuTTPKa1nDDDi-mt3dl71qyRj43wagEcp2uwapAiR7v-FQfeECWFPCs4taDPGdIDOVLAOWo-z71Y7hvZIg0gIU7vJPlFO-45nqcisiQBZt9oMsiq0-HoThQy-b8cgE2It_e1Vwbq9WSlSUpOBHwi_NN1oijTPCqmwo1V73lD5cI2w48yhc12qDezBeZcLk_dztmB98oMJaEtDtA0IqSEKJAeIANyhLnqriBzfPgQNPvZAaAXmy-S8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM7ehEUaBw-1oO0wy8Scysd8cl_dohB6TgiJVBy26EuNCsVmWqxNN9aX6dOEt6CV0IAqqCAK5LXL4NUc6VQuBNRhw_ge3mXKGn8cctFBMmZFxHS1sxhvLqysASTXbIYiyYbAfPyJnSDiU-33ITGQW2UEPSjKOtJ48QdGPYOGQsYX1LwemaJAEfeW3omFIg3nD8IpDhucp2cbJ_WLvF4piFjmd2kqzXqGov-E16fX3bXsoVZDnJPpEgPC20SqG4A1T5Xe3tjv5AYURCsAOOEl37xSLSCXkUujSzKI2gu_6Hvepu0dSv8U3i2DjIlN68UlWR_zVM0Vx_wUOG3HfeWrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=gCrone_r2SvtZWnlxBA1UN9JwzEGy6N4pDe3sNxTdShBoHwWVndRaDEl2m1OaMw5CblVbGe52P1D-6iFDCqGWFFSeAysqW6jjjYA1KCcDJAT-nPGbp_fbq9OAYevgfa_bZq4iSWxuEBOFPetGbUIPJceKN7Y3A1bp1dn2gXfJzVaDbwiOM26dWz1Drs9RXpmw57MMk6xz7Dm_DHsrIAsXo8XvGG1oVM85b97NYpzDJW172BgUjZpJnwssMYs40no0kmCgR6cToVJ_GSqKvO7YzxibVXvYcnZFTaOeLDwsiRXDARb07Hc3CU8SmR1ZdALkO3dBNp9FAeBgtiQYdjgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=gCrone_r2SvtZWnlxBA1UN9JwzEGy6N4pDe3sNxTdShBoHwWVndRaDEl2m1OaMw5CblVbGe52P1D-6iFDCqGWFFSeAysqW6jjjYA1KCcDJAT-nPGbp_fbq9OAYevgfa_bZq4iSWxuEBOFPetGbUIPJceKN7Y3A1bp1dn2gXfJzVaDbwiOM26dWz1Drs9RXpmw57MMk6xz7Dm_DHsrIAsXo8XvGG1oVM85b97NYpzDJW172BgUjZpJnwssMYs40no0kmCgR6cToVJ_GSqKvO7YzxibVXvYcnZFTaOeLDwsiRXDARb07Hc3CU8SmR1ZdALkO3dBNp9FAeBgtiQYdjgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-EGHgVqYsqH4rYlzxB2dO0kwd3I2-rNVsfyS9c42_nHbrYqZ0usAmnkzeQ2QfEq_IqIrfxGu1o4LO-KRisWjO0-d7nHwoSAL4hFEvVpdMy38TFdZLDV7iiDTEcwUVi8RcZcq2opR801dXJTAba7J25pQjCfUsp6FWW0yfs-onADhSoOFz9stDja5zVx9AIkd48Umlx7o0lHe8R0wNOmxvjZ9hPpSJRAj0rs6tMMYEBFktZ1W_0CMg9-ryvddxfqnAKC5NuLZqqAPJGD5pB9JDcqFeN8KVf99ofyVHR6OehgwpF37bT34Zu4rvzJcwIySr015eQ5ByTwoT98eMeRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITt5ZTcTBlph4OEtphsv5j3wgoLBDpWVqxdLpumNAKXZzjWMSfb6uqqydMUJkz_vveEbSHnNfwbMJvPmVysNY-sBQpTfkC92U_pZLc6Tr1urKoDYK2W8GDjziep5MjkCNlH97-FwM9HmrBT72XDGNss6Qf0bLtPnkFlU311tMyTn1G43XXaPBCr0obI5VvoFPhvCFG0gaNbZnr_TnC_4uc2uXAse053SsMOHnBHR8GmduMGru1KtnLJ735KrcLyqQ_Tgs6SofosP36FpRcO-_Anx3Wy6hTBF61AYHX1PHESVP3Y9yIAkZ0IdgL4NcU7OQCHg6UdB5W6WaEJb77wa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smtTP83QFIDtHA_6HvGSmepRfS02TnKHrCsPMsKg2A-UbKAfqHJAaPjs1sLHp_wUu3Ok2wlX_LgEfDYq_tzRBQt8Bf726T4Sr6KaVYqS7Yj4tQwFrxULyCUCQgrELNyj5Q-2oLBm5ewcgC1ft8qhHV7m5uD8nwtzbANe0wVql0v45kif2LpF6sMtqgGO7pEGe3KmSgGHFT13uisQY2YMq_yXUyDLmgVWOSnlInoF2vsss2s9Y5x10ETGujG04HsUfu_tReKER5tGvQNYok8RrbIy2TJuFcC-tjdB_OSM9XDRI_jTW7ISeGdhAgds-UzddqHDfCacVCs8JwcN6o-ZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=JJUlAEDwQC9qw0XMN6pfzuyE9FXXFdFzPC0c5ytRgLwosYSin6ec5poFumuXDq5930hL_wbRzRqu8IwE9LcUEjSWenjXnDGwWawITtau2tewoaec_TH8BrUDSq2sm1aK9XSwq4I_rmBCdaHyJ_VWZE4G_LRc6n4rmyi8LoDfcF6bpVsmakUirN4HrQUmpvIaw3tRyLcTPHYC-3z45DFZI92ap1mnm06XeRYr8lPRqOZ8AfTC2w75snBUBkOmYVdUpYe1L4ZEke2SaP6HqAiwIvZkZMTlokgPtmQJbEiFcIrROLEvOfDIteRZrxS9EOJUG_5VQx-p2IfP28Qs9rIJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=JJUlAEDwQC9qw0XMN6pfzuyE9FXXFdFzPC0c5ytRgLwosYSin6ec5poFumuXDq5930hL_wbRzRqu8IwE9LcUEjSWenjXnDGwWawITtau2tewoaec_TH8BrUDSq2sm1aK9XSwq4I_rmBCdaHyJ_VWZE4G_LRc6n4rmyi8LoDfcF6bpVsmakUirN4HrQUmpvIaw3tRyLcTPHYC-3z45DFZI92ap1mnm06XeRYr8lPRqOZ8AfTC2w75snBUBkOmYVdUpYe1L4ZEke2SaP6HqAiwIvZkZMTlokgPtmQJbEiFcIrROLEvOfDIteRZrxS9EOJUG_5VQx-p2IfP28Qs9rIJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=C25ySuk6J3eug3oITcGC_SO0l2tmhVSAKZkH-uLZxYFISCtUx9SjVkt1YuFKa5Pf-T_1D69xnbefmXDsag8JsiUUT37Tt3k4Aa8weLnZEa-8FOIJp232q71nNllm3kjT0H3XuQp0HXYjv8URhtBZEc26NeFKMxJ6S2RL0Lqa-TA5PCRLy31L-mlzmQDvObgXa2nKDXUDj2rFDlBYdJ75t-kDBoENJ1GeKkqifV1dFs9-GFp9xVv65XidkioCHElE6wrgX9s-wbYm0cx0Qbl3f871x5DRiQWPRLsSN6IFjssk1RxG8qoIAaVWAOrbvHoby_yA1Mnd8oqbR4D3NH_Tvjv5o93jp1uIk7cnzo6KaauNuggRAg046QRSsUKtSumzJS9QFsK1EIdTTLhiWGOKWotLjTzt6YQJNemR4oWKqx025aL4IoLQuft1Sb1plvzeUw5bM200IFwj7XDhBKFtOgv1cyQSolZK2G7PfLxgq1ZMuAy30HPhYULcRuovt8V1BR_nIIcBODRVNbJEUbiJNbEAIVoIgGoazRZLXAEt3SAIR0Qp1OLhqBeveVxOVZTylZNtfR2Ex8AL3CI2RaLUvV-BPouF8QTgoREjSOKUT_UtQD5Q8nzuiAFiGTMvU4xeOrgIwbgjYQtzuKmHGolrfznFRKO2PmQ5RPKehdpgxco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=C25ySuk6J3eug3oITcGC_SO0l2tmhVSAKZkH-uLZxYFISCtUx9SjVkt1YuFKa5Pf-T_1D69xnbefmXDsag8JsiUUT37Tt3k4Aa8weLnZEa-8FOIJp232q71nNllm3kjT0H3XuQp0HXYjv8URhtBZEc26NeFKMxJ6S2RL0Lqa-TA5PCRLy31L-mlzmQDvObgXa2nKDXUDj2rFDlBYdJ75t-kDBoENJ1GeKkqifV1dFs9-GFp9xVv65XidkioCHElE6wrgX9s-wbYm0cx0Qbl3f871x5DRiQWPRLsSN6IFjssk1RxG8qoIAaVWAOrbvHoby_yA1Mnd8oqbR4D3NH_Tvjv5o93jp1uIk7cnzo6KaauNuggRAg046QRSsUKtSumzJS9QFsK1EIdTTLhiWGOKWotLjTzt6YQJNemR4oWKqx025aL4IoLQuft1Sb1plvzeUw5bM200IFwj7XDhBKFtOgv1cyQSolZK2G7PfLxgq1ZMuAy30HPhYULcRuovt8V1BR_nIIcBODRVNbJEUbiJNbEAIVoIgGoazRZLXAEt3SAIR0Qp1OLhqBeveVxOVZTylZNtfR2Ex8AL3CI2RaLUvV-BPouF8QTgoREjSOKUT_UtQD5Q8nzuiAFiGTMvU4xeOrgIwbgjYQtzuKmHGolrfznFRKO2PmQ5RPKehdpgxco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/togjPWjscMtT-5iOs9h9jvgQ8RMBQwz3nuHS_lOfUGy8_9iTP44uzseRMVsiRPuDZlEG6PaQA0BYmsoRlnpGCt5Zr2SP4YungyCBuIjOvlVXzey7X9PEah5EgqbW5Tk-BeMo8cfrukwBcIO_ik19lIzejU0GNtXAojmTMhcTz5NBdx5Zn-8czsUAOjabSVVfqpH3xINrKFXlWlb0vW5oqWmU6-ldyH2iqnyy1BcJOt5bOuM7gr3W11XChahbngOMglnFOa63V374x0BOYP5o80xU0KzmfR3Jb15ruFGkeNtE0NMzZZYUYxGAomo2Cj4IqmJHy0gKs3ZM3BhiSETmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=VcoUfEXiC7WgjCjUV041kS-P6OTVy3FWg6iaKorOSRPKybjDPNwQVkh5Ab0XS9OUvnSLSBNx7TVchs2qc4CC-N1gbz3hQ5FN5NDbW1n4B2nlkDn71uYEviGq_pnfc7oxbW3d2vN4GbSeTKMzcblfAiMB5rit8n83_x8mE7VsJHh1GF3liJrx6NMo2s3XGVuHpsEiX-gxmybB6XdvbAY3XZkpP_TYWGZoYXgXRQRxEbGR90duVwJ15Xp3cxIFYhNl-Odma4fdnBYmzlbFR7fLTeR-hINAH2iku0roRBoX-QhC-ExcnmAiV5rBf1DQHlTazmG6cC-nzfWfULJd2WnkEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=VcoUfEXiC7WgjCjUV041kS-P6OTVy3FWg6iaKorOSRPKybjDPNwQVkh5Ab0XS9OUvnSLSBNx7TVchs2qc4CC-N1gbz3hQ5FN5NDbW1n4B2nlkDn71uYEviGq_pnfc7oxbW3d2vN4GbSeTKMzcblfAiMB5rit8n83_x8mE7VsJHh1GF3liJrx6NMo2s3XGVuHpsEiX-gxmybB6XdvbAY3XZkpP_TYWGZoYXgXRQRxEbGR90duVwJ15Xp3cxIFYhNl-Odma4fdnBYmzlbFR7fLTeR-hINAH2iku0roRBoX-QhC-ExcnmAiV5rBf1DQHlTazmG6cC-nzfWfULJd2WnkEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYVT54rviHxnYqLxGfOL7hwLhkUnymHM5iKjSpkrwrjMXzo4q_kKFbqLdhcIekZBpOMHOuCtPo9ecoZxmknjviIDuF9op3HJL94NsVlDgcNyAc56s-NWsRRo3KImt0FVCotiK0k8Iz7D5v2ILL8qswYB4ofE0jHhCpCjDnYDIkwyKbbCynAcLqt7BRop-_iXd3HfHi_fx-KXURmnzWogsc_pwP_xwycszXpb7X_yMrjWEyVlzMv7ovgADuWWsWpEOG79zLGxrxL3k3HAhb9ccy4VhyzujxKl9tQsuzzDtO-RuUxX2n-HcH-Rzqp_tkI-Hr4HrZY8B16NZ5sboLL-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=rKxgRGVPae6pdpEmguS6Pwuz1ZamjjwrhhFXT27wpx5w54Y_qeVxarlV-ZpAeg5rzNvoOqdfqCjtNq8xgseTSD8icQMwG0t6U8ZAI1XYzQBtmLx9_YwUoz2gIn6ZidRG6WEFzZ6_IH8OXIX01dCc6PNRnBUhORcOB_GnLyN1PrhIprUzlBn7xL5s7du1IlHhKiNNPRq6WpUk5uukWWg1FO_RCD7NaomFoR_s6h-kzZgfbwAj5KbyjEcaTwt83QwBuXcBr42UYlSOx4_Imb4RKbkZAsGWI0zNlGVNBrlCuDSygpz0mS90XfFGblkzD4_j6pv8f26D910hITyl2PO03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=rKxgRGVPae6pdpEmguS6Pwuz1ZamjjwrhhFXT27wpx5w54Y_qeVxarlV-ZpAeg5rzNvoOqdfqCjtNq8xgseTSD8icQMwG0t6U8ZAI1XYzQBtmLx9_YwUoz2gIn6ZidRG6WEFzZ6_IH8OXIX01dCc6PNRnBUhORcOB_GnLyN1PrhIprUzlBn7xL5s7du1IlHhKiNNPRq6WpUk5uukWWg1FO_RCD7NaomFoR_s6h-kzZgfbwAj5KbyjEcaTwt83QwBuXcBr42UYlSOx4_Imb4RKbkZAsGWI0zNlGVNBrlCuDSygpz0mS90XfFGblkzD4_j6pv8f26D910hITyl2PO03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIDl1z1mzmfqI-uh5ZNKOOOUrtlLhjAjdhcLzQRJNKWJ72Brwsv2WIE-KinE9AKWsPzzxylqjNZSk82WsY1DQWckg7SY3HZ5iic1Mn4tkPmLCHpZ76c5xD37e-5jR40U4fvk8-UbHDLrdUDUGTipmfODUN68m4bOR-IO8ThXX_F_WSf1SxXcXx_tapc0CCsT7HOUWbqHVmjuuFix0ClfT4WhZY5DRymCnSAP8TNPgwuhcGEJkk0c5ozXauSKzfHHhUOiy7okYvi8jG6CgQvpwKsHs1OIOipa9wawMmqKJOdZNFUl8e4BcoFfA99laPXlob4LW7rxVtZ1q9vG_pvPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=XB9mBYfOeJFZeTEkzDhzLYEb1xR6GwHLBbDYsAn73-9iG0qCkax8o9v9RMDmMYDVoSihki_H1U-KoUjZAq1qJWxKI958fc1WZASSgYB1xhNbJI93a6C3WNKpAvam7KMGqiybRVLutLU4VlTTFzqTECrHC6XY7vATYTLeWPQXAjkuri6Nx-JdOfruJUJ9-IckEa-2hn6NUNiDyEXPJXnW4Xc9YqrDgIbbV9Ok6n_tlksXVCHqwb-yQ3HXYvDpbV-14r8bBzsS2UOkWyYiZN2xFG0fd4IIRUNHaP_aqIBa4q9OzCEA4a8GEBJwJUs6zCfLaX8-A34WzOhiJPBepNCyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=XB9mBYfOeJFZeTEkzDhzLYEb1xR6GwHLBbDYsAn73-9iG0qCkax8o9v9RMDmMYDVoSihki_H1U-KoUjZAq1qJWxKI958fc1WZASSgYB1xhNbJI93a6C3WNKpAvam7KMGqiybRVLutLU4VlTTFzqTECrHC6XY7vATYTLeWPQXAjkuri6Nx-JdOfruJUJ9-IckEa-2hn6NUNiDyEXPJXnW4Xc9YqrDgIbbV9Ok6n_tlksXVCHqwb-yQ3HXYvDpbV-14r8bBzsS2UOkWyYiZN2xFG0fd4IIRUNHaP_aqIBa4q9OzCEA4a8GEBJwJUs6zCfLaX8-A34WzOhiJPBepNCyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=hKuKl6EPlUA565ihHb_pt0D7hx7n-zvXVZayAFJX0DX2VbxA7ZpWbpHP_y78nzw9oV4pf1rNlUEjMyzPSUGhCqWa4NeJ5UjZe0CG92u1kenUki_EzggFPlS3p4WVpfJCmEuZhnT41jLjw1SQcESKwgcmEqCkOBp27nKdLYYe3sqrgQl1SeWM-aMonKAw7aP70z6ru8MfT9qEa4vXUottSWlhqKh8ltITqQIkmj6kACSY5l6n-Zr2KfEBUdfvqidi8ZJVKldYQF5_RubKpMdQ8QN44PddqUdOZnZKLwEajWz7_0z16QoiFrNRSwSA2knojezz7tsTyNV40lHXJrCDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=hKuKl6EPlUA565ihHb_pt0D7hx7n-zvXVZayAFJX0DX2VbxA7ZpWbpHP_y78nzw9oV4pf1rNlUEjMyzPSUGhCqWa4NeJ5UjZe0CG92u1kenUki_EzggFPlS3p4WVpfJCmEuZhnT41jLjw1SQcESKwgcmEqCkOBp27nKdLYYe3sqrgQl1SeWM-aMonKAw7aP70z6ru8MfT9qEa4vXUottSWlhqKh8ltITqQIkmj6kACSY5l6n-Zr2KfEBUdfvqidi8ZJVKldYQF5_RubKpMdQ8QN44PddqUdOZnZKLwEajWz7_0z16QoiFrNRSwSA2knojezz7tsTyNV40lHXJrCDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUsFM9fp7qqp--vuHTunW6e0UCKJHYjSVeM-l4cO2kdW-zBsaKVN1VAs57jL5CMKeB0gHsPPiFvEl0p5l3jND2qIut0DOfReAiqEvxln3LSEwdxs1ziPFgUEF42q1ZQcGXcS85jGcmr9yxJCHLSeVhpd4YcLsvJ9YLG-XyzBPCMqKdGNlTdk3p2RqqfZ-MxWYhfB9TyZyW_uw4YnRIw_8iBq35kRArqTeqtfLIqD2IwNGP0nx_H6s_10zPXDvXMB6aRnTPdkOrEQQLo4e664YEy5sjLYSxNwM7eeucdy_uEG5NsWvumLcYHCSR4huiVF2RpiUGP-LEBZCedWPrc7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=KoxmuTu39hsSUetDm0GfArljs2qwa0aJUNc3NsJfrf3uVKdc8dvYlQG62ZDIdtEGlT7obzn5fxiSGFAKCQdDqeJyu6qRDDMrTetW5fe195iguu31GLR36hSm1xn9m4xKbfT8VNGiNb2lcfYserGqLd77vTX9_yf5WZv4BUPpN68A99gQAcB06BBmgELMA8Ag9Yw1jMdOG1nR6pth0CrlbFKosXZwiOHnDYeef6N845PZ-Sa66VDQYKoUlT6B0n5R-zUbX86mepmvfIPqTzSWAEbAXWdHvhv7DtZaUDSqsRG57CxDTTisq45Pc-otNOZb0jklwdhWl2b-YgpqlSlU0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=KoxmuTu39hsSUetDm0GfArljs2qwa0aJUNc3NsJfrf3uVKdc8dvYlQG62ZDIdtEGlT7obzn5fxiSGFAKCQdDqeJyu6qRDDMrTetW5fe195iguu31GLR36hSm1xn9m4xKbfT8VNGiNb2lcfYserGqLd77vTX9_yf5WZv4BUPpN68A99gQAcB06BBmgELMA8Ag9Yw1jMdOG1nR6pth0CrlbFKosXZwiOHnDYeef6N845PZ-Sa66VDQYKoUlT6B0n5R-zUbX86mepmvfIPqTzSWAEbAXWdHvhv7DtZaUDSqsRG57CxDTTisq45Pc-otNOZb0jklwdhWl2b-YgpqlSlU0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGiEApa9V-JK5rOonF-jz06xp0ku1Aaa6yrW5GKq3_N3_jYO6fzzqgHOZFO1fN2OggABMUufNqzid_7A3wqIjjlV44InRSsQ-zLYWPT7kScEX48-6utCEVZgYMGkujmD2LsVtCc0lOfAeV9yp2qrYmTUVr4ajRPYGyRzsuc4JG1X6h0jhyX2qJNaKbbaNM3_V-OzGo9t5srluj4FQIOuEHcwSy1ddpIb7yZJZr2b0_Odv610JNIs6DnaW25nsnsA9LReCdpmilEDjmWhRR_ZSgy2TTOPU3_5jMf9kYeP6oE2qJix4oIMyhcEOTcM4Kbye81g0zF3AaoZeVa3D9Gq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BGy436ksCLNwul3uI_bxgZvy84izI_2geFz_YheZJk3GMZNC-lgmX7Oq8vxcfbZ9XCUYHcQkR41Za89JEPtoIswsOobStpT0M_KCfNJpiTwn5eqMAyLbr5MaIohuaDYybh1AOEmGnQg2eqt12o0OK1tZYlrAHyMAAN8uRtPFxbRgcPnfBe0JNRhTnAkzw4hku7RguXoi9__WIdyjmj8LeQirZh_SiNoqLZ_FASjBLO-gfs4eJmSy_-4lDbe8_gUdXOpnStr0WKt1b3BuCDK0bcRTkDX8HRp89xmTVixSY4QpuRoyvuplndTTHjs2o5MEi6Fh6LxADglEwZIVa3Af2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BGy436ksCLNwul3uI_bxgZvy84izI_2geFz_YheZJk3GMZNC-lgmX7Oq8vxcfbZ9XCUYHcQkR41Za89JEPtoIswsOobStpT0M_KCfNJpiTwn5eqMAyLbr5MaIohuaDYybh1AOEmGnQg2eqt12o0OK1tZYlrAHyMAAN8uRtPFxbRgcPnfBe0JNRhTnAkzw4hku7RguXoi9__WIdyjmj8LeQirZh_SiNoqLZ_FASjBLO-gfs4eJmSy_-4lDbe8_gUdXOpnStr0WKt1b3BuCDK0bcRTkDX8HRp89xmTVixSY4QpuRoyvuplndTTHjs2o5MEi6Fh6LxADglEwZIVa3Af2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=U-g9jSikF006UU8qqdmvgB_ZSprCa_pkrM5Ou3ou4I6t0t2_MtL3ZAl5hCodG1u7nHjC2hrf5h1RnPyMqDGdnzWkyAjxFvjjLOxy9_cji0PKBx3rMhEg1w9wmC4eZwej3_wwf4C3UB8nxHASWexpJT2bTb48AilaegKJhhwhbLAyFEk0fEbvS6v1_9zaSg-85PX-Ju34K-4Tl8AKJxDd9-EavrroL0QvJirIrTbbK9H9rXJyLYPLsdHJc-Aif184ZbZ1hJ2QEWYUdgkSmfg1jXJHPq-wovJoQHjbNWQ-nbWu9fdP4EU1jWLYtbpAatPmIR6I8H02HmxUe7KMYjtoMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=U-g9jSikF006UU8qqdmvgB_ZSprCa_pkrM5Ou3ou4I6t0t2_MtL3ZAl5hCodG1u7nHjC2hrf5h1RnPyMqDGdnzWkyAjxFvjjLOxy9_cji0PKBx3rMhEg1w9wmC4eZwej3_wwf4C3UB8nxHASWexpJT2bTb48AilaegKJhhwhbLAyFEk0fEbvS6v1_9zaSg-85PX-Ju34K-4Tl8AKJxDd9-EavrroL0QvJirIrTbbK9H9rXJyLYPLsdHJc-Aif184ZbZ1hJ2QEWYUdgkSmfg1jXJHPq-wovJoQHjbNWQ-nbWu9fdP4EU1jWLYtbpAatPmIR6I8H02HmxUe7KMYjtoMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=JhN_C3iCt8FP4FXDPS-kL0FMRd6lIpIBkBuTW14-LCPNwF0ndX6lkAlPlNbRIqQd_Zf1AUV0wpDR3S3Vs51sAAEN-vgW0K9u_s-A_1oCtB1mmGLmOXAUOwbeWBdw-5pGi_0GKVnoDXDuE0j9-4t8URDydGBTt3hIzAXm9hWcUnjRatPoEiuI0L61mN3hE3zZq3QUHbiASVdE9c1LZw8bs8UeNsMISzFjOxhsSCh7f3co1JCEYMUzeKKMjTMBG7u6r3i6TwqHM-vyPDgHtgHj3gL9PcOn5pyqhbekDs0_XN86pjyKh04k0Dn707AUvsWVUmQ3-WQOV1SuMJvAPfOe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=JhN_C3iCt8FP4FXDPS-kL0FMRd6lIpIBkBuTW14-LCPNwF0ndX6lkAlPlNbRIqQd_Zf1AUV0wpDR3S3Vs51sAAEN-vgW0K9u_s-A_1oCtB1mmGLmOXAUOwbeWBdw-5pGi_0GKVnoDXDuE0j9-4t8URDydGBTt3hIzAXm9hWcUnjRatPoEiuI0L61mN3hE3zZq3QUHbiASVdE9c1LZw8bs8UeNsMISzFjOxhsSCh7f3co1JCEYMUzeKKMjTMBG7u6r3i6TwqHM-vyPDgHtgHj3gL9PcOn5pyqhbekDs0_XN86pjyKh04k0Dn707AUvsWVUmQ3-WQOV1SuMJvAPfOe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=a99F2ntsVngMIyP63Dha9hGe_0vcpZNhsCadFzUUgInTV9ezuH60DJsfWIj934_ZJEvY1Kjg_3OP4Fg89rZGzZEM0xsEine0ezZ9TBfdRV0EZqLvlbbKL-5-omFZOn5GfQ_oSIif_Z7mxERLbFH41KdLU6IjkOXCw0oHFznSGRdT-m9jdAVrTmSz9v_71LtQRFOtuLsTeDJ7rCEHwaV1zzAbRgrzd8juJZKgITWk8cqB-vn9kVb0hSoZqp1o819bHy7lJcOEY7dQCqIV7XlVaya4rfxwwSszfkVaOMnKgkqR5NrWKa-ci2HY2HkE8VrGzX3Nqwg2Y7esOr_a-gbM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=a99F2ntsVngMIyP63Dha9hGe_0vcpZNhsCadFzUUgInTV9ezuH60DJsfWIj934_ZJEvY1Kjg_3OP4Fg89rZGzZEM0xsEine0ezZ9TBfdRV0EZqLvlbbKL-5-omFZOn5GfQ_oSIif_Z7mxERLbFH41KdLU6IjkOXCw0oHFznSGRdT-m9jdAVrTmSz9v_71LtQRFOtuLsTeDJ7rCEHwaV1zzAbRgrzd8juJZKgITWk8cqB-vn9kVb0hSoZqp1o819bHy7lJcOEY7dQCqIV7XlVaya4rfxwwSszfkVaOMnKgkqR5NrWKa-ci2HY2HkE8VrGzX3Nqwg2Y7esOr_a-gbM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2I-kb1IQuiYjrZKARl2TlfGhyLj05GRZBRem92eAMhHauVqxo_5LCYfW74E4efQw0RTsVnMTSqMkahFy6dkIIYLfAGJau8AEFpkUr1uwDWzRXCFUlTVbj_s_wznltarNBEQ_KD42zQjmhea-6IzrcUmLi841NcWUVxIA1gn3Q84arpIJ4beYFBtXaQpJ9Qmf7OJtyswep-jZ_NqNc4c0osUhCWLXxqjpQPQn251MRRwpUP4Y2xpFG_M5E8V9VV89-rBlDhdimTAPtu4wuprX8QVHPsUwKb73XdZvBmYv9fcSx_F_4XbCPH7crkYWpVhiyXuQLUWKiQG4Fb9PyFMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sv1hy3ZlMoa09cNatkOa6zWHMTuSUiUjN1C-wDpNiZQmQkDYnceusjOSg6N8H3zBMbY7QoZZGcVVQfE-mziKyjZu2NgUBFysgZMqgycNW315RM-AeNm7QG3BAgzvYgSOWdgNFCnt3xkU8OuVG1N4tk7fYMayaylD6IvRCWg1zSKFlEZy20Qaw7jLTTSvv-OJdslj9o1sHQLDw6bNWJD3rMI1UQSTy2jveRgrYjY8wpaN17Pdjg4xkjvtmOIeodTv6AJMX4LnO07kr9bRASQ_GKkhwCQVadR3cJI7RPJNq1wmkIIjzZGpFxSdtG5TPdvtpzeZn_dbcSfqy25LyxfVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGmUSFuV4xbW_1hIDTSrepYdqrKPaA_1t5Nz9NsCgkqDJqrE1MMFw_PUZ8bkeg9kqblvbOYwQti2FuoqRviocGA1C_CjQkD9TYfu4uQq5W3UyZw77H2qpnHVDTImCoQ7P-BBTAl7pxINBs3EAwTRkeAUGDCIo3fHK6IlRdoPTTAUFISt-T3sMAjzif1jedpjZwGyJ3tFAqWGzHU6NnMpHN0hxd9ckzj-aeEQYDjjmc-elfupYC241zU8w6XVTeTHWMqPz8Xv_VNOSsZtnH84fF0oeyPXcQMjizbMtWIGcNwlQm440mc7IFrs__EXCUxJz0DKhqxkI6oHhJf00yO0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-4f7ksS6mhMaZpSK6E9VFayQF608T-EoB8xLZd-jBUmNsrzLMZwhvdKpOk8x2MB2E9akRWTd1wR7vT3wIobEA5BrOmls3CpVF7rusweCRUGsnTy7bLsf5vW8-sc7Vxde2y36pq8yKPhmTjhgnWPijMKf6fJbcjZZQJMljTsLV8t_4dcPgHui3IoC4LracZfylLA9I1Rs41x50sbdhdSciRvs8TsuRVsE107NMmyI8bikj8iH-wlK4yr_IxCIAJX4u-Q86H98PcW0RiVVzAes3gBWqG29ozrkcrNrK9oXCcX0cnbkJ0Yv9NuyXnk5nEH3aJsk9TzDmVgR6DH3vwppw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcVzkC9VuCvZVunkpu_PSIxfn3NMquubPHtbL5DHFecuSOzAjcRJZa3mJ3q7v9pUWFJ1Q3QSAhAzOMAmnutFj5YZ5NA1Gr3VCVBWDltUiH7joRn3W07Ji7e6oeD5cXouxFozGxDO48ngk9Hie0j4aMuFz4bbQ3yqEhHlDuI8BKreoq3_c76Obwkqti02l_FP_iWhFlTp0UK6FrrxX8RRKCqbs98dXS6tirGH96mmSDONCOiR3gQJnFWDEuYJGHtlIbXyI7OtKoC6FlkAHw-dofNNt-4n0UeN3qqHNi-QTenDDfOQjDc5uDuBgj7MFhSzXXLWhfMFhSvzjQHJUcXsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=eJ3sGH2-fsTB5CEr4NJJ6Qi4wMqKS3x3Lw2Oyl7yJ5k6eBlQVIYrbw8Yedhf_XTAd0Nt9evdZLc-VrU9hlrcJNInXYTb0JYlTb-T9FvrWY6rQuCmn18SJjGL_hrxVTRFBW-C5RsiVSBnn8gsOJj-C_7jG7PmQLM39hf3cZ9f2vk7DlSrplpJwXrIWOHikY0dGwbViDjAT4uFBMl7U9VKowudUJW70EeeIvrsVUf2_sPZDyoAqwYo6R_YWGNUiwz9w9BAYoIB-7QE-LdyuNAOqXf8JEFijY8GdpILaJDkBYg9x7wdQpd--aR3ZholPFAqdeZCs1cJoF3RCXfZrL_upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=eJ3sGH2-fsTB5CEr4NJJ6Qi4wMqKS3x3Lw2Oyl7yJ5k6eBlQVIYrbw8Yedhf_XTAd0Nt9evdZLc-VrU9hlrcJNInXYTb0JYlTb-T9FvrWY6rQuCmn18SJjGL_hrxVTRFBW-C5RsiVSBnn8gsOJj-C_7jG7PmQLM39hf3cZ9f2vk7DlSrplpJwXrIWOHikY0dGwbViDjAT4uFBMl7U9VKowudUJW70EeeIvrsVUf2_sPZDyoAqwYo6R_YWGNUiwz9w9BAYoIB-7QE-LdyuNAOqXf8JEFijY8GdpILaJDkBYg9x7wdQpd--aR3ZholPFAqdeZCs1cJoF3RCXfZrL_upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNLPn0xNffOugkUUWYpJH4i0Xz0hlcoSBdAJefVJXWo5n9919RC18I3fIC42pPSrFwS79RFN42qqebSokQgGtoYNv6X26TxwO-Vda5vwG-1lHt1GNSQSRRlCMMH-lv7Q343tjVQwZ5u_DNXGmyNiTnM4uLgq9OE5tbv92xGWUtbFKAThU7WXRNEagpVloOMtG6O3mn4FZFmxYwUyIpQxbbMgCbCw2hiJe-Zk1ljIAC-zQ1ARf3ZdVnVJxgS9iYtBwlnN6Win_71BSIep7hZ70lxBmuT3lvDqwlc5gb7FHprkzFpjyRoJWqff0TDBPJ4j7cTYqu-mOI3Yz7Vsq4kyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVLWEhEO6tKi08lPiE19Uz_hBW3z0KHQzDq4fadIQDHiU_pAdOQaVrX0_YjfoYwZ-FFHOvgMFEIQS9uUNEHjznvS7YXy5wnYix0gSVEvLmeWYsjgzeOJuSMppdHkxPjPlXARFz0ZeR8PKv2NwumyGWFJ5ujTw_KQJCx4Vkdgv0jll1DQWACnDsZo01IforTP28xBsvtMk8uL8-CqiHzxQCGqDP4CXM3Y0NYXwzYzbeSz8HZ3qbYNQq38nH77yULjoSqVWSO5fbxCpolI000xlQibJl40Qd_orZOhOvKZQNZKfNydQnRGRB_trVk12lscwd8-16GNiOX3IPqimxIsjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHULoIm1fO7SU4HHYzbOEw9mJgJvF9tGmZIob--luVtFaFJVUOQY-2UXbUPIrHT3dRdScoPFJtbI9s-C6vFBnNscTVoI7MlITZS51LPgQw9L2wPHCGr05xSfhB_0zXMKEUQ2syVjB3bSWz5yvLud3n0UjXV_tWVO6JopEwHqm2B3bM2XNZXo6Z5c6yLA4Ewho6zgMLMXDq6jiW8PjHevhIuucObAAF4YiMAJJkLJ7fuW6upIjIufqOdgMuE2QAWFDcIS5BKG9HV-S38olyop_aB7WAUyLrSz1FtLbQzMOQsh9vu6KaEEtn38nKUAXHTEtWTlnGwwNdsHeHoHLXL70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2BMFhpEtFzQ9VHsaUUfYW3qQM3Jm1jTtw4Uq-vgDwS6OyPPAAfqxZ1bbiH9SiJlwY1W16dX_WDHvEmMTP_vXLjr0abbvoH8oP9rAk1qFc_DR-RdArdDeSMVfPdPDaifvXMeZX9G_QwNWEGkbJCFFPMNZVIoFe0wF-jSnT_QN6s0keqNDFlKmm-Wcz92AS6yMbt3dzHsbltFQ49VQuLCkCDd6JG6pVdSl8t5FOT03qyDElzhn-pPNWPQZLbRgFQ6c4PWmi8AT9qVBNSMAaehdzzhcFPhZoRqcYQ0UDHZtEtqTTyRw7Fm_U1K6pP0stZUH0o-iVyXX1ETtyCkgtDGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahYPVvHg5l6wvFH8BwfahN7REYmkPnKfkA1Y-auLqmL-RKOWkdA99LFM9sd-EP6jfWdImtWd8zh5B0ZG1Dr0PQ7COHfnS-FUHIZnvLwPaP_xygPewfs70ZbxZDJ9Ommy1-0IUr5TTKAEGhoqoWzy1USH_h2UA29zJbd11HgWhOSCcWNmZUipDcMQqkTYiK2NmhPjkxjHghCWZozxBBCmAS3iry4xcVZ3Br_DuRAqDk_6WlVqs4TzlPDMmPnAZimH_x8r2W4lR19kPeYkjdl8CWcSxd47EysAOro3X2Cj2yOlk7vHEvQT8hSUZPnIGxgb-6ZeKrGqzc1hZOX7fSZtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CndRSUMqPW1dyYiArBTTuhrP9UpeU8mYePj324tC-tWCN_-enReeyLIkPpKR_DTZEqvhJxHjH92eG2PgZhYhUpSxH1uOQMdE93_6TTF_tsqrKv1tzE3swMkuP0BdxY894tPJTfK6eYPA7jnFnc5TUPAUY2lVjPhPcCnbF2cf4DG_A_iT2IwaV4__Ypgg0EhQKg4F6tffjLq0h_ADlEWo3KPFszutNNSzEUR78ulRFyK80WuP2wNBBp0HGpN_enFQYbOFOZxyyA6wwRJGhbAHK1m-eUXfWQEJy7LrmLeR5OFD3CS62l6zigOxJUE3qb0ClhRsuvIsSHHsoz6C7dH6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=Awu2xhkkDU6Z_BehAQBpJkxHg4L0aV6pmSBsnHXKXQczHOgfN2UujoEyu8mtDkcSxfw9OXGjEHC6AiVCMMuNBcDr_gMzVTvTnF6J-wfwtM9_BoFNiFNrJKrUvzxf26OQkL-OXfn2BSD4mKq8DOCpkl_26TW153NkWrJitmqCo4YglR5kTN64cizki-RMEqKfkLwW1PwgyVt9234_6Z4cCsdoXu3eHA08fHucWfNw7lTHVpWcuscINlgQ5wFWj-bQ876E0UsVaV_6n9boSWsibnC2T75dR3Rapg4UH1T4OXqgrtxaGZtBU7peJxd_7gNhPe8LIZRRBIgr5EoNQbm26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=Awu2xhkkDU6Z_BehAQBpJkxHg4L0aV6pmSBsnHXKXQczHOgfN2UujoEyu8mtDkcSxfw9OXGjEHC6AiVCMMuNBcDr_gMzVTvTnF6J-wfwtM9_BoFNiFNrJKrUvzxf26OQkL-OXfn2BSD4mKq8DOCpkl_26TW153NkWrJitmqCo4YglR5kTN64cizki-RMEqKfkLwW1PwgyVt9234_6Z4cCsdoXu3eHA08fHucWfNw7lTHVpWcuscINlgQ5wFWj-bQ876E0UsVaV_6n9boSWsibnC2T75dR3Rapg4UH1T4OXqgrtxaGZtBU7peJxd_7gNhPe8LIZRRBIgr5EoNQbm26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DUy1QHTX09J0F9ADA4XEkqMcC7h2kTTAzBke_7gBPe4cRWGMy6fyiBdO3VqKVb7JQY5JOPBw0JUZ4T1UNbQXVLzYYaOn3BG0lQyA1hfMF-nqFLwh9RY2OmNoWkoe8iSMnhBdVF6m_eVBFmRR_aSMt-evsOlLYBo8wABdbf1eVF3ghOR9AKbiSm40BIrU-mN8X1fCIWBhUkizkx3voW7W-V7VGcss2SmFAMQNXpR0n7OzKrwUvPO5idJqEDzvObZIRwc4QkVQ7V9lU3JrmorpVq9pCuVfU7fP9nX3edgWVOHW_BWKck4PS1i8tzKkVdIFAyVwUJa50C40jocf1AN2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DUy1QHTX09J0F9ADA4XEkqMcC7h2kTTAzBke_7gBPe4cRWGMy6fyiBdO3VqKVb7JQY5JOPBw0JUZ4T1UNbQXVLzYYaOn3BG0lQyA1hfMF-nqFLwh9RY2OmNoWkoe8iSMnhBdVF6m_eVBFmRR_aSMt-evsOlLYBo8wABdbf1eVF3ghOR9AKbiSm40BIrU-mN8X1fCIWBhUkizkx3voW7W-V7VGcss2SmFAMQNXpR0n7OzKrwUvPO5idJqEDzvObZIRwc4QkVQ7V9lU3JrmorpVq9pCuVfU7fP9nX3edgWVOHW_BWKck4PS1i8tzKkVdIFAyVwUJa50C40jocf1AN2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=fYv3bMmY6qmWQLBmBOl5e1HOdBwTFzcnL5-hmcvKIf4yt-1bbjAKQ2sEsE6jBfKEzkxrVEuRQb-P4Lwxu3-k1qHr9aSHba7u-l9D9Sj-1mLvHFTEoK3q6JppQAy5kUsINniz4xA2ai5dRmc8jLL7L983SoyQaE5EOS-FRJgGyceBeylSI1EGGr_ibBaQAChY1VkCFQ6wtMfX1LRLuM31dqvLdT3zqMwXuDn_ZSUfjf9yQ6w5Huu-48O9bryTLl8IYjhFz8vPaEVpgvtlqVRl8dBn4d-3qgemV9f1b2cGErTIzvaJNpRV2xJOK9D5zmWF90EzifcZDnidTG06h8B-MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=fYv3bMmY6qmWQLBmBOl5e1HOdBwTFzcnL5-hmcvKIf4yt-1bbjAKQ2sEsE6jBfKEzkxrVEuRQb-P4Lwxu3-k1qHr9aSHba7u-l9D9Sj-1mLvHFTEoK3q6JppQAy5kUsINniz4xA2ai5dRmc8jLL7L983SoyQaE5EOS-FRJgGyceBeylSI1EGGr_ibBaQAChY1VkCFQ6wtMfX1LRLuM31dqvLdT3zqMwXuDn_ZSUfjf9yQ6w5Huu-48O9bryTLl8IYjhFz8vPaEVpgvtlqVRl8dBn4d-3qgemV9f1b2cGErTIzvaJNpRV2xJOK9D5zmWF90EzifcZDnidTG06h8B-MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNsCV6nZGMK6HuEIUCrKavLB5ZJ_Fle0qYlBJmjorJBCW5tzanhqRNkrlxlpEgGMHD90y9UGR5b3_t276u5b5gVCKBS7XqINLLHSGT7nhi45vJXNUlOmA_5sjoo1SVzDpzT507v_T3eKZJVFrrZlLczDBsyYeByDeaNjhk7TXk8KpCfkfqrR7m-79eCTl4U3Emx8P3GLdiehxmFV2gZ4_3ObmSWqy5fhye5xKGHQ2XsCQVWx99wO4qgN8FbN07F9vE4SOBfwXH693-ToO1a5B17dnhxOJriUbiftSxKb_eQ9q8auRZ1rxCc-y-eAVtVbf_lT523b_oKLUzg8k0sQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=OqF4ZU5FvjD3QpaMwGf62QU9OgNv61vUZmf-xTmEKnUGL8na1ZU1w8lezM_My-ceUG9EB96uC-WFh8JXwKx90WSk3EP5XIY96LE4Zhkpn2xicj0O1Ss5KuHse3Qmf6AH74PU4_w0KEGxK24x5aI7znIkUOKAbFNt5xqxJhTFJfv2xTAp7jGWZVP0ColFSSriaTbJoJhBkn1BVYLW20c_wVEEPsFPVkFQ17DRkSnSse162KYFeQ9-p2i2348TVyS-CvPVbGUmeQTpvzQMSSR8WhepPiqxIqbY-CWZsWMnFV5MRwK2dAFB8A-FnpbrErGWzxecD3YgO6ZJcK_3h-8xkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=OqF4ZU5FvjD3QpaMwGf62QU9OgNv61vUZmf-xTmEKnUGL8na1ZU1w8lezM_My-ceUG9EB96uC-WFh8JXwKx90WSk3EP5XIY96LE4Zhkpn2xicj0O1Ss5KuHse3Qmf6AH74PU4_w0KEGxK24x5aI7znIkUOKAbFNt5xqxJhTFJfv2xTAp7jGWZVP0ColFSSriaTbJoJhBkn1BVYLW20c_wVEEPsFPVkFQ17DRkSnSse162KYFeQ9-p2i2348TVyS-CvPVbGUmeQTpvzQMSSR8WhepPiqxIqbY-CWZsWMnFV5MRwK2dAFB8A-FnpbrErGWzxecD3YgO6ZJcK_3h-8xkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=Sv6Tpe0enCz3bRoMMDObFk3s2Bnw_7S-uQx-6KyiLDxO5EmK6Uo9PjptzN2D6sinW4oD4gvRyrP2X76YFCW9BriCx_4mmEWvOLiWgRD-QR7YMOWo2nA0GMqLGX-E8WJfQHACbXYsX4BZYoBGe4n8AiPfdvAlRHgwqfk84vyDgYFJqwxxSlZXSgtEiLTknWu0sQYAjIwso32Bfuo7ktuNTVFUWfMggV3F9Jk3bTrtRXGzOFrN-YUyDjTSaQMjT1XygszWuNtKeeOlZPHeb2jC1rvU3dJr43BGBr5l6d3-ScUBJJOxzYWnOCw9xNXAak9FSrxIxDS7EqQJTVUGrsyX-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=Sv6Tpe0enCz3bRoMMDObFk3s2Bnw_7S-uQx-6KyiLDxO5EmK6Uo9PjptzN2D6sinW4oD4gvRyrP2X76YFCW9BriCx_4mmEWvOLiWgRD-QR7YMOWo2nA0GMqLGX-E8WJfQHACbXYsX4BZYoBGe4n8AiPfdvAlRHgwqfk84vyDgYFJqwxxSlZXSgtEiLTknWu0sQYAjIwso32Bfuo7ktuNTVFUWfMggV3F9Jk3bTrtRXGzOFrN-YUyDjTSaQMjT1XygszWuNtKeeOlZPHeb2jC1rvU3dJr43BGBr5l6d3-ScUBJJOxzYWnOCw9xNXAak9FSrxIxDS7EqQJTVUGrsyX-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=ezu_4Dmd43J5DpmXIqcFJlXvKP4SfCWbBm5U4waufo92bKwQSnOrXSI59K82EAAOpMpr4JCUl3vdTQzEaL5D_fxVX3WMrUlZ8N2HYiE_nUFHWbVwwH1M3xASuVfJ6UwvvQCLUBZ7tapm3zSJCQ27AAMHi42dXY2iuJQ0hm6jaft46Vc76qCPFQFSran_PM3yYOC2PDJdejPeTq7DhOT7oFOEDfLDUnI4mViZwG-hGLtl4LTAO-SpI2HPy2O4_dHtt1bK72EVeSJvQ7f9BaMoKL4n4PWm3V4aMlojSySIWb5vQbdee4w-Xci93-Q6VZK33R4tS9KBaTxkFTJmXHdUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=ezu_4Dmd43J5DpmXIqcFJlXvKP4SfCWbBm5U4waufo92bKwQSnOrXSI59K82EAAOpMpr4JCUl3vdTQzEaL5D_fxVX3WMrUlZ8N2HYiE_nUFHWbVwwH1M3xASuVfJ6UwvvQCLUBZ7tapm3zSJCQ27AAMHi42dXY2iuJQ0hm6jaft46Vc76qCPFQFSran_PM3yYOC2PDJdejPeTq7DhOT7oFOEDfLDUnI4mViZwG-hGLtl4LTAO-SpI2HPy2O4_dHtt1bK72EVeSJvQ7f9BaMoKL4n4PWm3V4aMlojSySIWb5vQbdee4w-Xci93-Q6VZK33R4tS9KBaTxkFTJmXHdUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=NChJgzbm8B8qh5tQ6lTIZTagXsS4lyEG6zxxLaqjzI8UJTzwWCFGa2dT7i78XxvUpvBMIWjrlvdsoFT7GhpTL1JWm5AJC2hlUFfUYdetzC4b6Ee8_UysLXj_iKKpqrmhHuTunAV32aen214mhgbU_yhEfMBc_EEz7t_3XMe3NXYjumngnxcjC94bjIuXLQA-vHYHNL2a0fSU4LbisIJyPdvVBb-3-8Q6w0jQZvn-I3x9p28TgNTaYSC2b8hNOC71Vzne8efF5YtGb5VdghLxu-o1ZV7yFZdhbZpe39VWdnbOwM-bafXpQjCtpXAq_DR5keisxLQAWOWNnbmE1Wk3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=NChJgzbm8B8qh5tQ6lTIZTagXsS4lyEG6zxxLaqjzI8UJTzwWCFGa2dT7i78XxvUpvBMIWjrlvdsoFT7GhpTL1JWm5AJC2hlUFfUYdetzC4b6Ee8_UysLXj_iKKpqrmhHuTunAV32aen214mhgbU_yhEfMBc_EEz7t_3XMe3NXYjumngnxcjC94bjIuXLQA-vHYHNL2a0fSU4LbisIJyPdvVBb-3-8Q6w0jQZvn-I3x9p28TgNTaYSC2b8hNOC71Vzne8efF5YtGb5VdghLxu-o1ZV7yFZdhbZpe39VWdnbOwM-bafXpQjCtpXAq_DR5keisxLQAWOWNnbmE1Wk3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
