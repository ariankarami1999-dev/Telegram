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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVlk4X1EUtS8ij1HLOr6uEK1maAUZBw9GQALpf_nfaX4El7lEGwIKLsBJ2dzVGtrghxsMF8iKwMlgiQQASy7-_5WEZUrLRLIRPagLSUiYtOAtr3SpMrxiBq006mLul7rfzCFMUAL_gGRibzHeNtSP76rZmIOozh6zF-BYzwA01iIhDREA28NEzhsqb_MlloQ-ppfQf8aWzVZk-W5iDoi72xZq0UwH0EoRARpSAWrLbh9Q2hH0TgWYnKgrAdTbhML3CnPO1Z-Rth4ae8jGn8TnEJfpQOW8kDaYrCmN-GDu56nmZi3nNuW123DqYP95VDk3gzqsDF2S1dfp33GVFZ89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJcIJZoR0nJQFjO3bLILI2behQ6eXgzFAPWu9pVgmSYXOX4FhRXD_4L39tqZrlSZphfMcMLy3goFbKtpwj1I_eGTD0YINJ4FruGH7zgqZ0wiwPO65I9_usrXu7CbzbWjHLXRO8Z7t0_GjgvX0uPLDlxs5QC0GMDkISWp0N4TiBKWEKFSeBrPGK0x2YzCt92iUQ5hpOM-lpeoDsYstRtt7wlH9xuNet0XpKXUkoVu4YvdSud6WeqPlSHp3WfNTn7UX0FYUS1342rsAJTuktGZnEXTa5WYw66WYM7JNuBfASrr9KdIhqosdPFXXE6aZVPYzi012DtUlfl8XLipo7xa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LladEuRVWOXufEgB68FdTi2sMUZSuuwIsFBDeSv5cYSoLswBgd6yTuSZcKUzwVfq4vI-r_ABEpTb3IQVw4PCzLRsQ28lR0xeDsDbr6vvdk-IMg0MD9U0ub7Zp3kc69YANnfkZZpNO7TIlyBLzVmqUdA9NmbBmXPOvEAVfPffktWY5bkzaVtSWTVMrwzdf5ifbrP2_voE69d4d7aWNS4zB1s50CnmoXnFDUHua0WLxnlUNdPdynMiOqtXF5UAUznasT4u4wz64ybhQJ2af-eJ94SvmyIWiYnXoIboI2oCKYrVDOJOjWRyJMjjBm0UK1MwN4MGwTxE2EDmPdPkOq2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQVUZ9qaa8VoL555zTz7uiTTTJ93fYRbriWVe5x-tUay-ybdVp9SCssgmKzdRuqIJs7q8RT7Ct3ndJTSKcDcDp2OriFpewDcoeRWYCPV6rBfOmI-oiykPvO9EPxelkJbxL3voxou9fN1W29kq15jei4EWemhEbQ_u0o14ZGGQPJIiOvchXMZYd0qjtNVnhaOLVy4jPq9RtbDgW1TiyaozJHeoTMXYTmvcQL-ZOjEqqE69ZMRjCVA-U-ElBL70tfMRfIKmD4pUpgYp2tAKnrfgru_N8Emf7grRac5mcZHWkCpvBVaZ0lM4TatjnRo9KWG9ZdnqyJPmGxfIT38MQMjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVqCDbrSIxQ0zIxUrl9TEzbujq9I6JI6yYRFrccm3Z9K5lS_E3GDayDMkalZSCoB-w1AJaAJC_fIs61everV_mFlf5CDTo_W6WRNUN-E71YDiy9RXuBt8xZCRITnNCgIowA_QJlGYfSCgdRIhb4tEy5zvuMFWH9XWRNg1yTdFD4xuW2yVvrnliYXNd4iAd8yAjkrtfjRTQvLb6gGnfbdCUuI4eZqEdgHGjjM-gCKnUgcGa0AzUGBmm3NrWxnbK6U1zLGehUu6PiraY5M0PQMxGIijkSZgD3lbKJ5WL7XISckmeyj_nv5BfLvXZ_FNGDkJSSRmWzRxWgITBvl9EUiaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgVjvh8_pDBcW00Px942cA70jaLLiEqFz951DwGHvw42GB4Shm1QKUTc1hTkQ9gDVB5bLpAq1hfzoCvH0hM4aD4MmLfWrW4bm9Q8eFhYnmSYWs95teGN1zywS-8EXf1-stHWXgnTheZhesWP553aPTZlI0E-HFa6GtmxAlA1pnMdxJ_4vtSEUPwAfQUszIb-uxwZG5oJ9hw6LpjuTc-gqzOL1YMRAyo7RH7BY559Br3OX21gTHyRDgBidmDKtc-SO0yO5r-mkmuAUtoAqVsGj4yIl-oQcdimieC7AUYEiC74yYJQsCd0QVb1EeHAhdiQ-FJFBEJZXMjv7AgRHZdnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGJTTBnMuXuqgz5KMtcCO9qJeExKAQ1gaAShbdq3xguICNsIAymAN96mJw0Sy4fDBtOUAuZzbYkNywnLOstKLdMiuyg6kF-v_KIJ5vefdIv7ZaOVNrIgiami5N2g827_p-DgZZnE1k-aXyqcf4MQXUjFKvHmZphGb6XR_vT7lGhmONGdYQTCDbJsZ-q6Zb9aKKVrGN9wafWhR01bDMAGVxvx6swIPqypJZfH61kqeXkvJNCxn1pSj1-APvy_mnPrN8RSmVzKiAzjy_1j0qUCvxi0ica77cj9zeY9bokkowFG4G5Jy8oUbytRSRNHGP_hcjA_EGrJWd8t6nlzKcDI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=FMPDdIH8bbMtwlhyvzgRoFZitaK14Bqy4DmekdK3WhgqKjxMoo3uWobEK1L32Z5mUAyIdTAXOFMglNZkjxxQS1SIsWzVSAoIybWttvbzTn5Si6YEpaILw0IMN_J7KFi_W_zv345k7bgwtYM2C-Z-4Yq4QQoMWzCE6Vwu0kwZRLtgMmGh2pB0eMAN7KCiVF9vTU94W6jcNAS7I-7HjH1ke21lkNqCS6RSMGGK9CWbmOUn-AJ7TcXopuWrWth-rySk4Bd4hMmuETRzjB87Rv258qZp8ToV82EtRDVOSzg7kFPPcdLF3_SJxH5_pVXTll02GQEhucHt1TucmaltGdHspg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=FMPDdIH8bbMtwlhyvzgRoFZitaK14Bqy4DmekdK3WhgqKjxMoo3uWobEK1L32Z5mUAyIdTAXOFMglNZkjxxQS1SIsWzVSAoIybWttvbzTn5Si6YEpaILw0IMN_J7KFi_W_zv345k7bgwtYM2C-Z-4Yq4QQoMWzCE6Vwu0kwZRLtgMmGh2pB0eMAN7KCiVF9vTU94W6jcNAS7I-7HjH1ke21lkNqCS6RSMGGK9CWbmOUn-AJ7TcXopuWrWth-rySk4Bd4hMmuETRzjB87Rv258qZp8ToV82EtRDVOSzg7kFPPcdLF3_SJxH5_pVXTll02GQEhucHt1TucmaltGdHspg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW8krhE5-b8sCvzNW4fDiZCImfX1HEaIqFC1CD6OZUDb6IzyX_sreE2bHZeIJUFmnySjpnoq-4BhCMZqcyfZrUcB8PKhbwl2uWVRFwVWHHXggJP5nbtDJmkPepbzSvLUbja8SpEtGv21Tjsty8-2GBG2vzJXQw6JDMncrzJ_GVW9zvyMOTkSHEJHStQMfezAtcxFOxFlat3R06dowoLY5u4Hg7qujg78ZmgxdaSSeyrAFU8PxPiyZYqIszU_H9fVSJ4Fe5v-n4dzCFjsHCeR1sQd04PCSmjPbnOHhWAoXnriruBQ3E02k2dTwuek43MB4j6DCln19lyJhpXjUl3PoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=Ed5dbPbzBBR1efBAY9a-zPwljPEBL6OBXiZo71BrlCOIN3jT_GlOFL-BizYZ42UJbuqPrf5oNUaM5ZCbMrHv8Amzrey2cbfEKGqHoMe_swo4C83srv_6DT1T-FO2wo7RaY0lDfafoKt6ty6uR_9WTjWza3SR8HFFZX7QCmlQdIJveqtmodukLv8lTIQbPSVREz81YApROEiFkOay_yi564RyyfI3snlE5xl4vvZSER59vu-dXglOYvRQn_WZ4KWA8Ag185ulcE6UYCzcHqvKbgojkRGNIOxD42G9qCJ4029oUwZuUjlrjsAycbKRnNVy2ZLgL2n1mnapnr-zbJtesg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=Ed5dbPbzBBR1efBAY9a-zPwljPEBL6OBXiZo71BrlCOIN3jT_GlOFL-BizYZ42UJbuqPrf5oNUaM5ZCbMrHv8Amzrey2cbfEKGqHoMe_swo4C83srv_6DT1T-FO2wo7RaY0lDfafoKt6ty6uR_9WTjWza3SR8HFFZX7QCmlQdIJveqtmodukLv8lTIQbPSVREz81YApROEiFkOay_yi564RyyfI3snlE5xl4vvZSER59vu-dXglOYvRQn_WZ4KWA8Ag185ulcE6UYCzcHqvKbgojkRGNIOxD42G9qCJ4029oUwZuUjlrjsAycbKRnNVy2ZLgL2n1mnapnr-zbJtesg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o71m0fvdjIxs8hCZarqFucg9Z-6AZpR-YWCCIxqGL7Q7PlBgVx2A8IimL9Ybs823vPYRSVaiuZZ53OYJozWOEy3p23HXYvST1PQBinCYtR0tVk2o7TeNdpS3AaxC1e6QUw0mXdd7B9YjEHtALBTzetpxmBoGDNS5Qjj1cFpPfjiJsTa5n99FyHQgdUNVuHPXtx7bbC1ZSZqzrdwWBNgiPMdQ_Cpfonms5hagHQMAN9AmRIldbTUhMNpF6lMNK8N46XmBwnwntv0qQCmGjHff-ozaW1ZtCk69caljYa5YF3EGkmNq1UdM58Y82zX0IkL6oel96KS6iffRAq1kolRUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AHTSbJnjTwzDkBgl9fiQZgmWY2dsSRNpT8Gh2vnYZqtAjAg6Bxe-ys6plJ714iotMi6UTy70RiWksUfaDIqqz0YEFcupgxCH7GyzogVj2YrPMxL0hiZJmshoJKGCTzO61l23MAdhbSAWpUHPOeXPQVRHK9xgQVItl3cVJLJ1qD-5DT34c8GmJiM7pxMPOr0BmVpar9DS2q_Go65oJ3BJePF7vSz0h4tqM9--1D6IiIi21PuukK0klVZqnO6chPzKSeGnP-CavRjU4JSNLYJTDG1ETW_uWYIlO6aLZMF2AD7ZtQeYaB2Gp-0QB2kBYADMLDYHSuLbUR4SRFn3P8FcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g8eFzW1s3T5SIbV2BdAHbuvd3VHgh-aGu_2fxZ7qef31GEdaUkRz0I0x7wEpELv4hNBRyc5P2IrDQDa_oKpDTiMNe6cZLjLn9BET9vHA3tU53HfZkISsWiOt9rtUy01YTyrBYXm8MdQwDJcEn1Ka4tyzFwGXwUo4i5QYLxnmc8oo07N6ypZX5R57EgfCWlLnfiL5QILo0q0Ro-iASYnhvfpROiEU_M4Ge2UfYSSs1GPoLtbyxSWst2bJV98BxxxYho3DkKdZzwI_rTK0pRC7CBqaujoa4dgyy-K0eyQDpJYjJOhqrQ_nj9IAREKPwKr8G9Tj7Z3NWzo6QhJlCJqkqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMiGeECiB0VQSq1kctSy3-Q98itA68DCSYhqboIaaYZebAbQGdMdxt8G5uR5rBhTAvWesG9__XfcEphSaQH72wZ4vFJNgtpAGlJOLn9mElfQr9NCg8Fmon2W8zp9Gq4hnLh5wzOZ_gF8NSNLSKXdIivJWkmNsyh2sFVsc7nOcX1FfJpBt9dSsrt_dm0DyhCNKjf9sSjvHrX3d02rQM2TMK5i0_d9ty3BJc2yLqrnCh67u5gS2MHRBSlch_r1JW0J5Tn-F0aBDVak8PQn6Qmfa4rrNsxFoji7X6Zeb1hsHPbGJorEg84-CQshGNgg95OHSTdb-SamVub_klwzcMe3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=V5UJPg4v1fp9ODV4fry-2O7XUbx5bgcGH9RNkAnFzN4eMQeNf1Ko4oVENV_uy7ngI9SjjSXxgQ7Rq8PFu7FujT6x_wP5nkAVaq99leHaD7T9mDj6CWsQ6ifqObzEFlmy6-CbMCHmLpPsD33t0f2h2eNmU1XejHuKil5RTSWHH1JGF8gq2VlIz9xbGgo7qgYs6mOdUDVXJaYI7uBQXGqgirF3deL-LxU6LspYL1nghDb0-Myqbg3C46Uq54ypjbmOJ2wSIaPEJMf95EajvcLxhxx55JMuhL9haa1UF5Bx3xzMTebmiISY1CRnmf7fglg_5cow5JuD7Kx_2vo6mKIi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=V5UJPg4v1fp9ODV4fry-2O7XUbx5bgcGH9RNkAnFzN4eMQeNf1Ko4oVENV_uy7ngI9SjjSXxgQ7Rq8PFu7FujT6x_wP5nkAVaq99leHaD7T9mDj6CWsQ6ifqObzEFlmy6-CbMCHmLpPsD33t0f2h2eNmU1XejHuKil5RTSWHH1JGF8gq2VlIz9xbGgo7qgYs6mOdUDVXJaYI7uBQXGqgirF3deL-LxU6LspYL1nghDb0-Myqbg3C46Uq54ypjbmOJ2wSIaPEJMf95EajvcLxhxx55JMuhL9haa1UF5Bx3xzMTebmiISY1CRnmf7fglg_5cow5JuD7Kx_2vo6mKIi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcrYSoVDc8pCBF9uDQrm40we6EtyHKPWUbnSVjT0OEUkoEaNtfLeh0tA9xSriPkxo0Vsiiok2sQcfXtsTymxuZAcpg9TslbkpMmKqIXEJ6e3IjdTV5GB5EmNcbMF_n202qog-UQiHmFQDkrf1BNldvBzPKojCnZ40VlCwyRRDVM4kjFQf9x9vBFi10wcF96DnOb7Onc9hEF42LmxdzhIhTT8t7NAjwsxK68CbbvHSNix0OqDcTH684lVNfKjUEdxermamk4T3zQILVzgVi55G9rugqE9Wy1EXgRIKn9fqqc1UxTgSNUiRKh0Wc5376PJpckFADCaphxp1MTy7CFgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=ZPm3QH1g-BytWS5qErSjnJwvtPUpmSDAKkIeXkTR40ikSqQQzalGKXDG1YYb5UCxhODd3qWa5oi_nrJKLSIixh_GbGdpbUnGcExJpkhECajwxJqZwmb95lo-gM9t9DxGLYQV067o65GSlTE7YnKjgKg4Kc0zBL-B3qYtaH5nkwWVbz-9LJKcCpN16Hdq6wHKORHA0spEH1m4Q_T71r4JCpJJBRoWE0tg7iWoS0EF_J7kwn9nn0YOpG6bGWYTNMb-tUBny4iCIGlMdodVFFsZ6ApODH81eqN41j0VY5FaGSKEKRjRDY2sOdZKSzIjMjF4t6ai2cwp2eWR92c2WFwH4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=ZPm3QH1g-BytWS5qErSjnJwvtPUpmSDAKkIeXkTR40ikSqQQzalGKXDG1YYb5UCxhODd3qWa5oi_nrJKLSIixh_GbGdpbUnGcExJpkhECajwxJqZwmb95lo-gM9t9DxGLYQV067o65GSlTE7YnKjgKg4Kc0zBL-B3qYtaH5nkwWVbz-9LJKcCpN16Hdq6wHKORHA0spEH1m4Q_T71r4JCpJJBRoWE0tg7iWoS0EF_J7kwn9nn0YOpG6bGWYTNMb-tUBny4iCIGlMdodVFFsZ6ApODH81eqN41j0VY5FaGSKEKRjRDY2sOdZKSzIjMjF4t6ai2cwp2eWR92c2WFwH4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=ZaouIJaDaopuwPiTdNeQFUwKLPx_ijSItJoOBacXaENDoUk5x65Abrw7JyXR92SNK8H9OLQNnipTHvRyaquoyBt52s8CDp9KgQcSx3qJvTD4rFCe3y2QBF3zpxE3fgs5es-ckOrOa2Rq7J81shn3kfhzCoMqOifWip2LDCASoWf-PAujV5a-YZxYwMugHjqtZDhsr30AjEAT0jo1z5MmKhLh08OtntrZKBo2Kkx79BmCnfNU48bH10CIG6V5Xle35mpROd-s_bkip1kkicdSa7juKoPdPZfiw6WDIMTUPsdW3R0ahXPGWYUVc4of6ip3BH6vbJeeh7ySpRLQPQavBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=ZaouIJaDaopuwPiTdNeQFUwKLPx_ijSItJoOBacXaENDoUk5x65Abrw7JyXR92SNK8H9OLQNnipTHvRyaquoyBt52s8CDp9KgQcSx3qJvTD4rFCe3y2QBF3zpxE3fgs5es-ckOrOa2Rq7J81shn3kfhzCoMqOifWip2LDCASoWf-PAujV5a-YZxYwMugHjqtZDhsr30AjEAT0jo1z5MmKhLh08OtntrZKBo2Kkx79BmCnfNU48bH10CIG6V5Xle35mpROd-s_bkip1kkicdSa7juKoPdPZfiw6WDIMTUPsdW3R0ahXPGWYUVc4of6ip3BH6vbJeeh7ySpRLQPQavBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=OnIHzWsOJbdMam6sWS-kQKuyCQuyYopeNZp7KR7BaCQxbMP1lOwTu_IpbsgrVjiPOUSYo7p1rCB7Pqssj0vP57rHjlcZr5zGVVhu3KH6k7jkxUAtbFosAss1JN9FawbWnkW-q8g6sHzSGrAjHWCh-yxddyolMWGkXilADnTPFkH7RpKECedSiSzlTKcLrYyoVTgnE_-G7Z_vcu59jI_esrfNNYJUD3BKXSDefTC6qGRhudrdZ6H_3dJcpZNrGTKumwM_Xaa_YixtqFDJLvy6BwpT2JO7R3V_Wz2OjI152JsJFBL3CxJ_CtPaKHf8A2bcI9gF8sDqo7ZlOIHxb9VfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=OnIHzWsOJbdMam6sWS-kQKuyCQuyYopeNZp7KR7BaCQxbMP1lOwTu_IpbsgrVjiPOUSYo7p1rCB7Pqssj0vP57rHjlcZr5zGVVhu3KH6k7jkxUAtbFosAss1JN9FawbWnkW-q8g6sHzSGrAjHWCh-yxddyolMWGkXilADnTPFkH7RpKECedSiSzlTKcLrYyoVTgnE_-G7Z_vcu59jI_esrfNNYJUD3BKXSDefTC6qGRhudrdZ6H_3dJcpZNrGTKumwM_Xaa_YixtqFDJLvy6BwpT2JO7R3V_Wz2OjI152JsJFBL3CxJ_CtPaKHf8A2bcI9gF8sDqo7ZlOIHxb9VfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=a0fNaq9YpLyF8diObz7fJ-AG6O7xTBYhMJkrowb2uQqIFnQMXPpi8GuzA-7sju9bTHduS9yfR-6Usgm9cl5Uc7_kN9DjheZ3G7wHxNjfcHYjiMZJFC100tATJ16Q1EjAH-M3k-exePbuQb8HSIDQo3EnLh17nicvvsgF-DsB_aklpPIM14rj8nhmSarxM5eNk9tZTH5Ybb77qnNUDoLkbWWm76ZNrv2w9_mcOMPkOdc5jgIjh-hgvV1hQiV9rsASxudVrZr2ieatG4HjZXsS2sCR2vsL7-Go6QyPPpr9IbOAHgk9ZEeBLjIsVATwY_zwkTSTGcXbvbWdc_c9WwNt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=a0fNaq9YpLyF8diObz7fJ-AG6O7xTBYhMJkrowb2uQqIFnQMXPpi8GuzA-7sju9bTHduS9yfR-6Usgm9cl5Uc7_kN9DjheZ3G7wHxNjfcHYjiMZJFC100tATJ16Q1EjAH-M3k-exePbuQb8HSIDQo3EnLh17nicvvsgF-DsB_aklpPIM14rj8nhmSarxM5eNk9tZTH5Ybb77qnNUDoLkbWWm76ZNrv2w9_mcOMPkOdc5jgIjh-hgvV1hQiV9rsASxudVrZr2ieatG4HjZXsS2sCR2vsL7-Go6QyPPpr9IbOAHgk9ZEeBLjIsVATwY_zwkTSTGcXbvbWdc_c9WwNt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=V2x2WtikJzWwzQ7g_0AT7hxZLXZUMyrioc9V7IvX8SPBtNulRqjzk6-R4j51RPa8Qtks5ogB93wbcrW526_1DHulUQQj94fN9nMIbEepKdpwM6OogyuRihDbFy7QHlu1Ur5SpqoXXfFETJ2EaGOmRS7vP_A1Vk6_whCiCXIA2OwGHnfMAl7_6c_8dLjXc10654El9kSIZ4IWQsN65o_LifsLN6oe_-2rsyseWYPBOLun1zyZnhfygP7hmMzLcS3NCwNxPVZja-hXY95nT0Nq4HFmevtdhcj8ivo-ysm1UzhcD9AZxNnc14ae5LiKKKMpB82L8rGB8XAv7ggPdPRfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=V2x2WtikJzWwzQ7g_0AT7hxZLXZUMyrioc9V7IvX8SPBtNulRqjzk6-R4j51RPa8Qtks5ogB93wbcrW526_1DHulUQQj94fN9nMIbEepKdpwM6OogyuRihDbFy7QHlu1Ur5SpqoXXfFETJ2EaGOmRS7vP_A1Vk6_whCiCXIA2OwGHnfMAl7_6c_8dLjXc10654El9kSIZ4IWQsN65o_LifsLN6oe_-2rsyseWYPBOLun1zyZnhfygP7hmMzLcS3NCwNxPVZja-hXY95nT0Nq4HFmevtdhcj8ivo-ysm1UzhcD9AZxNnc14ae5LiKKKMpB82L8rGB8XAv7ggPdPRfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=QJO75F8CooHYFodlU34Y0LFi0Iv3qM4auhxufAcUYRpS1ZO9watpGBgqcft1HcclrtpjR8XstQkp6gvW8O7kj9pBZMy0CpJTf9nvps2fanquJ2crxKfzoC1FrQilswBWusRIIVWet2Mz-7OU5SnWUroo7wOQ_E0X3f-Ga4R8I5vn1whKe5QvQ9B6fRHE6c64ZmiKE2cRgFp_QhwoHDqjp1SLDfEcQbDIryrilTAgq1p_GDOMnXeLW9vB59a-CLQ2xHxlgCscbTIQuW4zFYYJDFTbJ7QdUkoBJIC-GiJrWlcUaK98wHxilAGNUiGkinZxQrIsrUMSNe9022n0wVg3fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=QJO75F8CooHYFodlU34Y0LFi0Iv3qM4auhxufAcUYRpS1ZO9watpGBgqcft1HcclrtpjR8XstQkp6gvW8O7kj9pBZMy0CpJTf9nvps2fanquJ2crxKfzoC1FrQilswBWusRIIVWet2Mz-7OU5SnWUroo7wOQ_E0X3f-Ga4R8I5vn1whKe5QvQ9B6fRHE6c64ZmiKE2cRgFp_QhwoHDqjp1SLDfEcQbDIryrilTAgq1p_GDOMnXeLW9vB59a-CLQ2xHxlgCscbTIQuW4zFYYJDFTbJ7QdUkoBJIC-GiJrWlcUaK98wHxilAGNUiGkinZxQrIsrUMSNe9022n0wVg3fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwVHegPJPgqtnwtT2k7BUpbwpAZh78n918YRBv87v6r_ROQdYKzNEM6k_7eSkfJCbEPn8mNN5fqaOrTK6lujIznLXqTkloooK8s8T0KoVnQX8wXmc_6q2fDuIXGa_8xtDv2_l_4_3DBXreYOVITpWya5YwmGt75uly5bjV1fBnrdv_EqWvLns3MzFgwrruY5esrbAuHVVv9XzktP9WMmIjiNE4XVdVXkBZDLS2Y7V5W-Zu9TksP0Nl3_cHnQ8vTRoQ1gI8Ta8GdhPeJtyUPAuOOOrZA8CokRCWENMZMSFClm52eN62eiwJqTMRGNSejyCCvAOCtTH0XyzLL58_12Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWHkH2RFD13biUVHbTDUz7jCw0QJwSvkfJQUVo9sGfPhqVQzxgnsH6Vbddo-zNB6OOi26KcqhBrnz-Iz8Iw4A8GzxC3YD4L2bno3pIzcmiTTZ8IZt9s_sgU8WjvTAUqIrpF1e9RZinze_iFweZxNL8EjhTJBUGOsQFsMnCvvRjwI5l_Oys4yo_XGlnGV-Y3T07MhgFBnfbLe4J4JewSmNFh2t95G0UkqivmFxhUDwbNmoKTpEimxgVcdRm-KEvDbMF-olq2iYkX4e49FNaMe0bnS0qVvPWa6pvOl-RfORYCxeqjaHrhUuGc-LdnkAMW5TGA0mSCcdZeUpi3thyH-zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM7ehEUaBw-1oO0wy8Scysd8cl_dohB6TgiJVBy26EuNCsVmWqxNN9aX6dOEt6CV0IAqqCAK5LXL4NUc6VQuBNRhw_ge3mXKGn8cctFBMmZFxHS1sxhvLqysASTXbIYiyYbAfPyJnSDiU-33ITGQW2UEPSjKOtJ48QdGPYOGQsYX1LwemaJAEfeW3omFIg3nD8IpDhucp2cbJ_WLvF4piFjmd2kqzXqGov-E16fX3bXsoVZDnJPpEgPC20SqG4A1T5Xe3tjv5AYURCsAOOEl37xSLSCXkUujSzKI2gu_6Hvepu0dSv8U3i2DjIlN68UlWR_zVM0Vx_wUOG3HfeWrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKXI4QULtgFZHA9iwUVC617QNqhnkI2PCr4nUU-gxn9Z1NtznL1kF5KNEK4uQnteNHUsJRqcX4jrExqL-aLeotlWkS_bDgW4cW6i6SfT-bNJzMhIwygHXsXoFdNdKUf0X2LRl_YzU7CIPHaqil9xZ7rCFv_-j1tMZLw_CnpzwF03EB2bbOHksfPhq38WM0M1qxGbPgPciveWU-U_62YW2iljQod9ve-BpW3X9NhN-nIY1CrchpjadNfNjxCcj80LD1tiecCKywoeThrDAXuR2YkH7bN7P1y41sbyerWbKvByVr7sW8R9FX61jrA4NioTO6kr4i0REmsZC4YalLObuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT-abg_MtLjkhVO79r_5Mkq191_LNnaxArxP7Zxzt8AIYFelFqfOu39Hb7V66n8pasiIPc4QwuFFG_x1eXMzBry9Ye3n6l26phce01VT3ib9edl_NJjAnjdX9c4k4QhmJAxrrDe8Fv9-56fo-aCDo90lrfqk2UBBKofDoAUHsEiEuc5PWTSmBide7WJY1PjueOFmStjDVFHV6ZtR_320UKIM9_pbbz9azEEnqNGBIfw_MKh54PnIiTjFPy_Q8gpz4C2ZN1CnaxFdMNGD7oSkmyNEYs_84ToxGOR94rPd26zmYX1uH83ATPcu6287kyslpRiPh2ezmXqcrvspNzlADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkZzLd3A97Xa6KeeXo2NGrcUaOozHeI_vNEUkaVaPxEeAys-5UaqiLKB4i9SDEfJ6Yj3sfZGLMfprOq__Z5AhxBR0ozBSK_wngR-2bX0aXHAH85ycXnf-c443AybLYIgQAm67lCj8B88abSoBu0qNHHRYa9zHEZx3DQetPsHqMufDB99LT8BjAmhgkFzy0WeBq-FofR7bldh6UdJxjribfFQuKaUp3dYHuxnx_p9jkDrRHVV2PHKEOVklL3X6T1SWb1IKdJ11zntlHUT_N0dIjBpiqoQYSwN3ztX9D0Vw64cntPsmrYSWigKx0HYnRX1CaJW8X2CGxeo47Ty5jvsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=KyURL27yD_KMLWAqvN1SinBvEyXRB5Z3JYOf70xEqINQvgsk3uyODh5JbM7JwcfbVmKfkSWx16dU7V3MDPZfnprTz3d7xhptaWEcMKOYLgz_SsTFPp8YyNh18NwMY_rV1CKB-_uLVjVOtzyXvwQ3MW38qIMlbdbWQyHbSyu_H82dIn3rmlNmkbG3DztrFyCHYsijkFwrMcLzBpiZD1VyD2iIYrCcaVkdxoaccct_ECdduaKhceOL7CK1w1biu9KPTxUBjx2ugv-Ge6WwREPyHAULf9G9sbPiZjUroIxpL1ds6cWj74_TpvMigcM0saNKBE0SygF0-SsGRNqd866i0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=KyURL27yD_KMLWAqvN1SinBvEyXRB5Z3JYOf70xEqINQvgsk3uyODh5JbM7JwcfbVmKfkSWx16dU7V3MDPZfnprTz3d7xhptaWEcMKOYLgz_SsTFPp8YyNh18NwMY_rV1CKB-_uLVjVOtzyXvwQ3MW38qIMlbdbWQyHbSyu_H82dIn3rmlNmkbG3DztrFyCHYsijkFwrMcLzBpiZD1VyD2iIYrCcaVkdxoaccct_ECdduaKhceOL7CK1w1biu9KPTxUBjx2ugv-Ge6WwREPyHAULf9G9sbPiZjUroIxpL1ds6cWj74_TpvMigcM0saNKBE0SygF0-SsGRNqd866i0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXfLrKYzqfguekA_O8zESxKyqtSUFEP6qr8MR07zQCZP2omoFYfV46zxcMKgGxSnODXuJbzB3JK28oUU3-_wOyCagfTXhduWsatl6VD7MA499ZE8SwdMX0Mh-YdVoqHed_a5QuWJ39nFbhrJH-mbsYch492V1SO4r97QmkkDMSHORXPHGG4l-CbWgis_JDHHlAaMsgZlr9ZCrNLjSrfvlBVpuHjMz1mP18f0AP9t_y42u3d8zxUh34yqFf0PbZvqEFxEWd8GtAUkZSfxrAT-A3BWbfE0oCo66aPMwiqdOKJq2Vm11w2W0gMEr4PVk7NHuETKYrK-qxWnq39Qd1wZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYVT54rviHxnYqLxGfOL7hwLhkUnymHM5iKjSpkrwrjMXzo4q_kKFbqLdhcIekZBpOMHOuCtPo9ecoZxmknjviIDuF9op3HJL94NsVlDgcNyAc56s-NWsRRo3KImt0FVCotiK0k8Iz7D5v2ILL8qswYB4ofE0jHhCpCjDnYDIkwyKbbCynAcLqt7BRop-_iXd3HfHi_fx-KXURmnzWogsc_pwP_xwycszXpb7X_yMrjWEyVlzMv7ovgADuWWsWpEOG79zLGxrxL3k3HAhb9ccy4VhyzujxKl9tQsuzzDtO-RuUxX2n-HcH-Rzqp_tkI-Hr4HrZY8B16NZ5sboLL-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=eKc-oDRW9uZ1-DfITaOhUwNXLzDTtgOpCXJeQrY8UxzXhVLYVtscUVGY1txv-gv5DeWpqfN77CJs3MCdZ0o2-EbIRr_iISEV6n37qWErkBaOSBLHpoZYQOhutEta-xrRcy9caRKNQCE2yR2fX_atlOYZSSCwGetK9hcyzAYbmtWCA-FWqPc5klIwVo22-_VIjb6oAhLZLoJJty58QyyuUj4TlymX7y3xB3PmyLYBiqgXEMrzpthyxoDCHVapYGNKnfcAnrOHkbkYmVOlDt4aqIkbkKCEpzFRm8ZSVUUosvTIxr1XDv2HNxfjSi_ZjgNZP86hu5nSV0GQTjRQ5Xoqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=eKc-oDRW9uZ1-DfITaOhUwNXLzDTtgOpCXJeQrY8UxzXhVLYVtscUVGY1txv-gv5DeWpqfN77CJs3MCdZ0o2-EbIRr_iISEV6n37qWErkBaOSBLHpoZYQOhutEta-xrRcy9caRKNQCE2yR2fX_atlOYZSSCwGetK9hcyzAYbmtWCA-FWqPc5klIwVo22-_VIjb6oAhLZLoJJty58QyyuUj4TlymX7y3xB3PmyLYBiqgXEMrzpthyxoDCHVapYGNKnfcAnrOHkbkYmVOlDt4aqIkbkKCEpzFRm8ZSVUUosvTIxr1XDv2HNxfjSi_ZjgNZP86hu5nSV0GQTjRQ5Xoqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAuu8MKPSlEPWtgqimsee0VnlF_nhhPdaCyJgteSmE01gf7b8O3ZNsHSsWWR9QkPdOu4ANKE-BOKugP0rdhc81pXQGnft0osGp7AUe5IxtrrjTAUEl7ZQY8qjEP8_G6421lIhJbkUjEisQYYyYPB7Hy7AoNNGgevG59lEuZYQHQ8ZWkxzRnfMDQymnm3XPMtoRKwcL98FpmNMpP5a3pm-Ue405kQFShkqTejHRuOGdOlukDVd-gU5BDoD4FncPW5ty2mzU-avZA-ykQ3DNgqdQfqqs1K2BzTdEaYnSXpYhGkSzl6d-vdk9RD6_mbrgGmDddN5NnQC-YMQJnSNM7O4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=MaAUJkKj89o7oPb7DHys7SJweDCkj-CeMjyF5htZ6TCw0J1mJ4oGqqsSrwi8xVU-VEQLY667UpiJbOhk38bqhkmOnB4yjWy2V2T46Ms8ojiF7scUt1CWdwc2kWaojW_hj_Eq-qcBxuR5nXRDuq4RoI51jlBvGQPjha8cHh-CYucDo86U55_weNEpfNzH9CoX8TJ5jJea9pmenI3Zmn9_SzOnXjy24WwgjkDh0hZMX95QdlZQRyTQ2GU-ruavA1prCmmsWwK4ICaSevAXAgRS09spACV2RiXCKaHrAHJGyVqJHBHOEsKJSgFTJhnvUuDj86EFom7TTsbnvAD3Sl3ttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=MaAUJkKj89o7oPb7DHys7SJweDCkj-CeMjyF5htZ6TCw0J1mJ4oGqqsSrwi8xVU-VEQLY667UpiJbOhk38bqhkmOnB4yjWy2V2T46Ms8ojiF7scUt1CWdwc2kWaojW_hj_Eq-qcBxuR5nXRDuq4RoI51jlBvGQPjha8cHh-CYucDo86U55_weNEpfNzH9CoX8TJ5jJea9pmenI3Zmn9_SzOnXjy24WwgjkDh0hZMX95QdlZQRyTQ2GU-ruavA1prCmmsWwK4ICaSevAXAgRS09spACV2RiXCKaHrAHJGyVqJHBHOEsKJSgFTJhnvUuDj86EFom7TTsbnvAD3Sl3ttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=rfpf6qoPksO1bBJd1ii1brqWkSajkpolq8oi-nYxxyZM4lOUC8me-NfZIJDYOmCXgMbfUgHHSkJNssFeYbXgowgUC4UAWQiYKzwA8VTYExm7cICEeEj9imzhRuOhvE9L3orFBAqtxpH-dKKSexfJOVoH6k6U_Ha6NW7epzyOtDaWo0iZX3fxXwSBDhkX83u05e8CLeu0oKvD630v2WhuOfxR_nPpI3ZaIB4ryOk2d5ZxvHDBQnPbGHAGvc-FYsL5XYGFcL0RhEUBHoaRzYcygFDklZKNzdw7H3v6wae-msgRj1V5hTAPL1weY3mk55jINk8oPItoiKbyZ5tehFGHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=rfpf6qoPksO1bBJd1ii1brqWkSajkpolq8oi-nYxxyZM4lOUC8me-NfZIJDYOmCXgMbfUgHHSkJNssFeYbXgowgUC4UAWQiYKzwA8VTYExm7cICEeEj9imzhRuOhvE9L3orFBAqtxpH-dKKSexfJOVoH6k6U_Ha6NW7epzyOtDaWo0iZX3fxXwSBDhkX83u05e8CLeu0oKvD630v2WhuOfxR_nPpI3ZaIB4ryOk2d5ZxvHDBQnPbGHAGvc-FYsL5XYGFcL0RhEUBHoaRzYcygFDklZKNzdw7H3v6wae-msgRj1V5hTAPL1weY3mk55jINk8oPItoiKbyZ5tehFGHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO5Knn8dP2Xbz86b7uUvJhvBCi_ynJfWQ1z87puVssGhlHtx535Ka3hLKqAf7kKM8l8kCDoYLJ-HnWSxV51oZ7MpcTmP5lgiHhIg60F0e1wLOZXc6qjISs9GbQ39-KdjBx6fZLZ7C1r7AIJpw-EsGPvuLecKxKmTSuF02-cBZ5gFWOUE1ctpjLDCgzI2z0jUKdq43YNAdcEcxVxAN-Om6hRpEEZkJCDUHx4jVy5lG87CXI-kStZNb7PGl9ty1pW8cZiDRF-ICFL0yftRz3MYjgz6bnWChkQ0FfUofgLw2gX0Nvo7K2MjOxnsSwASQd5rB2Cth_XaiTA0czkYqco9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=aefHgbQwD38iy9n0i9HAjSfhpctT1zLEzXSMtbcBZDpK3QNAFGeshZWtCSkJwlpw0WA4N7EWroR3jG2mx3SdH-T9O4UjW7D1sfgKHGt_VFxmE1CBVTzkBPWcIBkWeISxaorzfySHMlbpY-7edtFcfD7jooujjZHAdwCeCTH_z_B_EzhqDiGTBj_AogUhkLqTTj1MDbTtMlihdSSyHODxOuYYoZctFX4uM_QGCEZdd-lHs6e9DKy7ACCoYnaSgvbUgNjk09AqoIxFepoltYfkS1iiGBpuxL5xVTotwI2RcoHp-JhHLRqtUoUwMV1_LO2hhfOwtQ4_Q2RJ9LjScsMOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=aefHgbQwD38iy9n0i9HAjSfhpctT1zLEzXSMtbcBZDpK3QNAFGeshZWtCSkJwlpw0WA4N7EWroR3jG2mx3SdH-T9O4UjW7D1sfgKHGt_VFxmE1CBVTzkBPWcIBkWeISxaorzfySHMlbpY-7edtFcfD7jooujjZHAdwCeCTH_z_B_EzhqDiGTBj_AogUhkLqTTj1MDbTtMlihdSSyHODxOuYYoZctFX4uM_QGCEZdd-lHs6e9DKy7ACCoYnaSgvbUgNjk09AqoIxFepoltYfkS1iiGBpuxL5xVTotwI2RcoHp-JhHLRqtUoUwMV1_LO2hhfOwtQ4_Q2RJ9LjScsMOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSge-PzO6EuqjaAdF2Gdn0eT9V0zy3UcwobA1ubRVA5FIvPHiV3yq6rY_XG19T-9HhEnmpwSz5hL4b95IThdGwGR6qoe63mFW-ZeJZvNTFRKLFCKb7mmlJsHfajax383UccT44hI19TiFfXXT7Lt-ppY1DQwb0KqaYIeVDqBZ72Na_j8i9VYJMa6UzE0GFBbZ61_tKcDAP0gdm3i2sTK_CKZwaf5zRK7KnDBKquX-pTf0Y3YX7DhwVz2uQ813GP5tXj3w0dk4u5gXAAfyf4XyPtDxojE1pv3q8QsXWzwimo9NBlM2j3wDdY_1l-xHGzqaI5a7ZpLuIA-r5V6GMY4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=OWsYODwe7mxL7cX1K78i5I8GiKW0251pig7LWaZSrtCLPcP_6_c3WK8tnC3jXExMaqsxnMrzsWuzyozJ1wRlINTIblZRjLbXYBMo-QokQYBUGHYoneSIIezJoAnpYhiVmdY6X7IG-oDITiamKWJebP84fxznz7M_Gq1QrWBBYJeDlOzEpYXAUE1Ulsx77fZ7CJyqE09R2daiYIVtk3udSujU324WMmRjckNjnspVqBtGWeflgQTp9byTM74zD_z-wVhC5GJzdRWpgXWFvtSGPCOh3sY-RGisjSp1kCx0J1Qwtj7scA8XqBCZJvBwxAa76zm4SMZtoOshuzbX_My2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=OWsYODwe7mxL7cX1K78i5I8GiKW0251pig7LWaZSrtCLPcP_6_c3WK8tnC3jXExMaqsxnMrzsWuzyozJ1wRlINTIblZRjLbXYBMo-QokQYBUGHYoneSIIezJoAnpYhiVmdY6X7IG-oDITiamKWJebP84fxznz7M_Gq1QrWBBYJeDlOzEpYXAUE1Ulsx77fZ7CJyqE09R2daiYIVtk3udSujU324WMmRjckNjnspVqBtGWeflgQTp9byTM74zD_z-wVhC5GJzdRWpgXWFvtSGPCOh3sY-RGisjSp1kCx0J1Qwtj7scA8XqBCZJvBwxAa76zm4SMZtoOshuzbX_My2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=WuQdJlR9FOdrc41Q1IDhvpWY8OBfRMPkt880Lf-TfrDthoJAFJn0pxcqWHFptGHpFA8ON7EzsnXQwVHcCY0sTo6sKwfFYRQd00E5Ld_a0isrNxMBq-ByblfgUyBevQER34amS_RId_sS8iScAFFhNe-7yqaQUlxxwjdjNXfeyHhkP9qhW36-l4D45VVKXcmJi9Cfl9NiFl-Pr7d4fBwiJgMXZLXFXgGPKGBD-jcyzucldGC3d_-oQnCeGYKqojX8q2HDm39fhALifakoDbaNZ4Ax5NMoxmSGkvlwnACaUR7_5UlnkqJCfJCNQQzezHxy78lo6adux6samtI68jDc0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=WuQdJlR9FOdrc41Q1IDhvpWY8OBfRMPkt880Lf-TfrDthoJAFJn0pxcqWHFptGHpFA8ON7EzsnXQwVHcCY0sTo6sKwfFYRQd00E5Ld_a0isrNxMBq-ByblfgUyBevQER34amS_RId_sS8iScAFFhNe-7yqaQUlxxwjdjNXfeyHhkP9qhW36-l4D45VVKXcmJi9Cfl9NiFl-Pr7d4fBwiJgMXZLXFXgGPKGBD-jcyzucldGC3d_-oQnCeGYKqojX8q2HDm39fhALifakoDbaNZ4Ax5NMoxmSGkvlwnACaUR7_5UlnkqJCfJCNQQzezHxy78lo6adux6samtI68jDc0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=cBPq2v1LeEdmfUqOAgD1P-4Ny1ELSIiuHQMyYwRW_DZgyt1wT4GciLKRbhoq5_c4bAM10yVQiiTdR3MEUScEaiK1ksgWDS7k4AOAKcg6MJNIYyIP9r31HnbB9JoeWqWl1YVtygiU03vZTJXnntCuuuYSJ5LsjNYJmPRT6BtsRM5YpSben0rZYyJve9rgtxWOrwc9eCyAUCuVoWxQ8-GV8dpLArT82jIucGIfzmUtxtEa_1hFl2-3RgXMgzunKj1oMVK4i2Pp1BrLAXWlDwbxHQ4Q4qK2UBSyGy_6FyBiegFERwyh1oalYszo9KM-AZf6HbgN7dqZyjI2Ll4Nxw5zeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=cBPq2v1LeEdmfUqOAgD1P-4Ny1ELSIiuHQMyYwRW_DZgyt1wT4GciLKRbhoq5_c4bAM10yVQiiTdR3MEUScEaiK1ksgWDS7k4AOAKcg6MJNIYyIP9r31HnbB9JoeWqWl1YVtygiU03vZTJXnntCuuuYSJ5LsjNYJmPRT6BtsRM5YpSben0rZYyJve9rgtxWOrwc9eCyAUCuVoWxQ8-GV8dpLArT82jIucGIfzmUtxtEa_1hFl2-3RgXMgzunKj1oMVK4i2Pp1BrLAXWlDwbxHQ4Q4qK2UBSyGy_6FyBiegFERwyh1oalYszo9KM-AZf6HbgN7dqZyjI2Ll4Nxw5zeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKXblvq_GNZjl2e2ZotR4EDMsgW9BTFHM7-b1gJFWYPnv0EKHzxoX3-VDBaYPVcpSSDh8aCKGzGjzfmKmOYse1YYWYOzFXll7QkuREQoAOtZ2rmySCLygudOcILnrvv05xBTF5T3sp5CGzqlHHvVQkgVMiWgaw5VmEhRf4IMYA56yEOc06j3gex6TsrkpzcJtlLrS7rY1f9ez6IehajG7Y7EAhU-F1UNu3UYTJ1yDHWZplx9iOLduvATVX9Tso4B2l-j_BB2EJsOFzwKsjYuzVL0p93hnDdrcrRHjFu-hQzY_-D_wNunhkCp6ih9imd6Qd9omATPc3KvfIR-Xj747g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pVyHEfFge7d3YVT3CNktT8U8W_3c8RWI2aL_GiZRt6FTdzQ1zTCVAEUHOoWVOcS7mdtJrJ5jriZ3ZgQe-GtXuaLgziFBJGipatvXnKDeE7LZtvMTENEDoFzGpEnIuuG_QVkLvUIra_xz9-ICklxCFtlvx9jdF5tKxSKyjGRxKFaLf4P_Kw7XdFb4oB2e22MefV6fD0pNXn4E5L6-xCp4WksF-ozK92d9fV5jM-f9a_OdzVP4zII2Arog_ENVKQjjdhPL_zvHKkkTL8c9gqN3nNVfzlzW1H46KCS3I4ERzM2YNeuWSIUJFVqql5ioDEi4VwJ_leDOPgTaL3-Vk8ykaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGmUSFuV4xbW_1hIDTSrepYdqrKPaA_1t5Nz9NsCgkqDJqrE1MMFw_PUZ8bkeg9kqblvbOYwQti2FuoqRviocGA1C_CjQkD9TYfu4uQq5W3UyZw77H2qpnHVDTImCoQ7P-BBTAl7pxINBs3EAwTRkeAUGDCIo3fHK6IlRdoPTTAUFISt-T3sMAjzif1jedpjZwGyJ3tFAqWGzHU6NnMpHN0hxd9ckzj-aeEQYDjjmc-elfupYC241zU8w6XVTeTHWMqPz8Xv_VNOSsZtnH84fF0oeyPXcQMjizbMtWIGcNwlQm440mc7IFrs__EXCUxJz0DKhqxkI6oHhJf00yO0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjXQhA813-2hqSm4exyPWbumch7iN5fJr1kEB6-vbsyQw-X1b2k_sK2ZUfnzIpsV3HXPpcgJwazhbtM-oi8WW7tbaXdS5cFpX3cJeQPckPYwxrSCfcpRsC1cwRNlRLUrfcLKwRYlKMFLR-vnwIII3TMeoc-MdDK6Pb-LT_1Gcy5Er3R49wKnvmYOzLSDOmtyvR6RBigOKwEdoBmnnPRxjsGQXxsaacPtvQCuqu_EqXLeU69lrLwJ-lvO3tyE9jLvk8XDHCS5uoz7S3CsgpW03NjMl4SfViZwhPhC_651Eoe8tAkLqTzgJQEgKqduXXy0mJ48kKKunR4lrsd5A2vk4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-5rpo-QE-MHlCkPNpvPvwaGn56wHB3ryOExS4TdUpiO3vx8o2bvFRnqbZ_MtRfRuiaAbB90L5YkEcwMku_l6UA4pN9ytQC3jaKfBuXwaTT_v0D5Z1YuuNNSoNo1GIW8OPA5Pr2a_HRM-Z52KKh-MkKfBfxcm1_QR-0_4Q0JeXM1qi71UYoyWZJDeGMqRAvtjTn6jhIkiem6sgf5hJrEBrYxhh11Aa7d4ivh3u9WKckoEWizKQbBLgXlBGOOk1iDwArlFMHHW-i2USsgR_qOPB2fGpPWzdx9Q7YDPBBczdRMJkijalOta_ko_E3QAzBl6YsMm9Ok2N0fBKVls48YSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=eJ3sGH2-fsTB5CEr4NJJ6Qi4wMqKS3x3Lw2Oyl7yJ5k6eBlQVIYrbw8Yedhf_XTAd0Nt9evdZLc-VrU9hlrcJNInXYTb0JYlTb-T9FvrWY6rQuCmn18SJjGL_hrxVTRFBW-C5RsiVSBnn8gsOJj-C_7jG7PmQLM39hf3cZ9f2vk7DlSrplpJwXrIWOHikY0dGwbViDjAT4uFBMl7U9VKowudUJW70EeeIvrsVUf2_sPZDyoAqwYo6R_YWGNUiwz9w9BAYoIB-7QE-LdyuNAOqXf8JEFijY8GdpILaJDkBYg9x7wdQpd--aR3ZholPFAqdeZCs1cJoF3RCXfZrL_upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=eJ3sGH2-fsTB5CEr4NJJ6Qi4wMqKS3x3Lw2Oyl7yJ5k6eBlQVIYrbw8Yedhf_XTAd0Nt9evdZLc-VrU9hlrcJNInXYTb0JYlTb-T9FvrWY6rQuCmn18SJjGL_hrxVTRFBW-C5RsiVSBnn8gsOJj-C_7jG7PmQLM39hf3cZ9f2vk7DlSrplpJwXrIWOHikY0dGwbViDjAT4uFBMl7U9VKowudUJW70EeeIvrsVUf2_sPZDyoAqwYo6R_YWGNUiwz9w9BAYoIB-7QE-LdyuNAOqXf8JEFijY8GdpILaJDkBYg9x7wdQpd--aR3ZholPFAqdeZCs1cJoF3RCXfZrL_upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDPXqwFrXAIleexU_lRVpFrVxsA9C1ICGXCs78KhP9ySVzc4iHtPohhpGxkLIJNra9AMfI8T_oLU5aKKsHbjPztgpDj0CnXxldHfQRZ8rY7PZ77W395Xy6lPpaqy3aQm1KEp8AYZjWHCK54bT-B1cFHwcNmNwCIUvdip0rtZYnY6i7vxAA92CgSd8VRNhIOkdUxC5Sf0saHWIdI5XrKPgUu6hWdZh6sBeG_-9BTkLs2Y_GFr2aq76mSDg4MeNx8rvn7kO9te4xZ15FReSBupXBWf5KbS5tortmW-rWomd62WDr3fHs3x91UfYERRGmiJlOePTsq3DAC6C8szb0XsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVLWEhEO6tKi08lPiE19Uz_hBW3z0KHQzDq4fadIQDHiU_pAdOQaVrX0_YjfoYwZ-FFHOvgMFEIQS9uUNEHjznvS7YXy5wnYix0gSVEvLmeWYsjgzeOJuSMppdHkxPjPlXARFz0ZeR8PKv2NwumyGWFJ5ujTw_KQJCx4Vkdgv0jll1DQWACnDsZo01IforTP28xBsvtMk8uL8-CqiHzxQCGqDP4CXM3Y0NYXwzYzbeSz8HZ3qbYNQq38nH77yULjoSqVWSO5fbxCpolI000xlQibJl40Qd_orZOhOvKZQNZKfNydQnRGRB_trVk12lscwd8-16GNiOX3IPqimxIsjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHULoIm1fO7SU4HHYzbOEw9mJgJvF9tGmZIob--luVtFaFJVUOQY-2UXbUPIrHT3dRdScoPFJtbI9s-C6vFBnNscTVoI7MlITZS51LPgQw9L2wPHCGr05xSfhB_0zXMKEUQ2syVjB3bSWz5yvLud3n0UjXV_tWVO6JopEwHqm2B3bM2XNZXo6Z5c6yLA4Ewho6zgMLMXDq6jiW8PjHevhIuucObAAF4YiMAJJkLJ7fuW6upIjIufqOdgMuE2QAWFDcIS5BKG9HV-S38olyop_aB7WAUyLrSz1FtLbQzMOQsh9vu6KaEEtn38nKUAXHTEtWTlnGwwNdsHeHoHLXL70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw86tykafkZL4JxVJSZaZvlzR-xM_Z-I-upnzdnTU9qiuo5ORpoXG-kOxPMmURD1O-uLyevL2s_D0pK38IcK_euQs6x_mtYODa1KSLC6E-_Feqg9MCg84C-0cEQC5DNEMxMPYWVGWWvOEUF5GxDpbgbAonHa-kcNyfIpXfraq_H4MxGSb8_ow-1jVb1-odMgDGKNg9yEwOqtux7KoF3P0qpCJjDqwuO0Cxk-wkrbtQXzAn0hc1e2XwVyyCBwyVb1Iv4XajXDnN0sFMoJ66H3h7gLipSlT98UaPDlfR3_S4Xnl3LnyH2Lamh51kAkbO16IRggMdKPQ_1yGR1Fr2WDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIwUuTdrkxOfsNq9_822SpZNxOARb0KM86PspKWLGXBqFQHZGuMXwpbvabrj_CPgMgJ8d3Sof1DQfCT_GJtTu9an9Amc_61rSn-4E2mnzM01DQfGx389T6Kq2IzoLPvVcxKzz9hFqyq8V_ARpZNrRwlj9ll7ZcVtHf-9Cv8Zh81akU07YArIbBaLPtjSy9_gl8jEe8whXmj6kQDcsUgTslMDTJ1EH1yoSqouwAQONvOvSyLAb9k_l--SzgvLTWCEFtvQke64kUYu_HYqO2pZAPtvKIaAfcWqHf3S3Y9w2t97EcOQJ0cxfP_3CHk37FjKeUP3Wt7JIP9wEsZ3q-5VcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPkzxdcWCuL-3mUJL0fJPGyWaUCUKNR4Mz6aA06i0DsK2rCHe7emndoEiXkRcuCjZT-amk1xAalhDCUMf3XkVkNWYQi_C2nyIvtJLrd5-kHSNKl0KRnLnKhufXMu5VXU-6lcyNPBunQXfbnzuXeG4iDdgTO9ABGcqy0cAr6WaSd92BenYpSQAkdaA7oohtk3H0ajEajKeXlu6zjRdlMjy6aIrpva8f8sqP__akAb0RnQlR1BvqFi8l0_XgS1Z4UtRcoQq0IM_nW-g6QwLUpl9_QhVrNVuY3A1JbdxUYkWaLDr4_rUItl1EItYwzzUttmkKOnYOE8mG9r_yn21Roytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dbXo346w-OISRF6R5cV76c-g4uzJP_77OYlowlAl3gccJqDD24tdSOKk3ctS-26qCOTeRdCazcXMujN9NzxZPs1rocMHOJN3wT8WatCdxY5rTMreMY-0YHgGHJP9WSjC4tS9IfGfrn29PvH_Ld5Fe7d_Iq1CY5iMIK9NLRH6SP09_su1Wxjc1hCcmR9yOWi0NHCgaN6zMuXfCSSbAwRdpgQQ8lKgFPdrVSrJCfPIDnB7pKY7PO4ZUMf9y4T5x7TbhIxAXguF6zjSvRvwSoozvnoRkpZ1Wy1HOMkykVpJj9WJ_tScuw-tswTI2C6bUmiiuKTFAliIbn3DdT8Qu70XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dbXo346w-OISRF6R5cV76c-g4uzJP_77OYlowlAl3gccJqDD24tdSOKk3ctS-26qCOTeRdCazcXMujN9NzxZPs1rocMHOJN3wT8WatCdxY5rTMreMY-0YHgGHJP9WSjC4tS9IfGfrn29PvH_Ld5Fe7d_Iq1CY5iMIK9NLRH6SP09_su1Wxjc1hCcmR9yOWi0NHCgaN6zMuXfCSSbAwRdpgQQ8lKgFPdrVSrJCfPIDnB7pKY7PO4ZUMf9y4T5x7TbhIxAXguF6zjSvRvwSoozvnoRkpZ1Wy1HOMkykVpJj9WJ_tScuw-tswTI2C6bUmiiuKTFAliIbn3DdT8Qu70XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=kqJUpWV1xhyphKOMkaAYaED11eeeGMaeMqLDeD6aNSoDyLbzedBXUpIxBERtwzALjxLKvGNgjYf-_13gVmmweNEFD_2m9e12xhBmc0-WPXRRzx28AYcuIIhFL4_Qjp3z2XsgqH6Kgu21hpDKJPhWfmLjZVl6UBnpqEYcu1Sog8UHjRYbKHYFt0FVSQBz8MClAoiQLXMondaRti8mLJCCDGRGVImGbgvmc1x-17n_BZgBOvXnIXIsvFdW_suAZQH2NMESDUPXdH2uEwnHOYRdlwWZMRj5H2vHukb741JMRKJ2VTXY6w_bpwcWSlkeMkTqosKAN2MccR_hR0AWZu69ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=kqJUpWV1xhyphKOMkaAYaED11eeeGMaeMqLDeD6aNSoDyLbzedBXUpIxBERtwzALjxLKvGNgjYf-_13gVmmweNEFD_2m9e12xhBmc0-WPXRRzx28AYcuIIhFL4_Qjp3z2XsgqH6Kgu21hpDKJPhWfmLjZVl6UBnpqEYcu1Sog8UHjRYbKHYFt0FVSQBz8MClAoiQLXMondaRti8mLJCCDGRGVImGbgvmc1x-17n_BZgBOvXnIXIsvFdW_suAZQH2NMESDUPXdH2uEwnHOYRdlwWZMRj5H2vHukb741JMRKJ2VTXY6w_bpwcWSlkeMkTqosKAN2MccR_hR0AWZu69ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXP7M_2p7bJZmnWonys7CZ8GXciEvcUt67BvyvWUYwqjSHtf13UGgiMNoGe50BP1dfxwV5NFqfQBvylcc8PVMl07ByJmaZLMBnCy0kBdT3R4otdwvbSkRER4f6AAu3qzZwlEPWSFVQKQupEfg5wSXBfz4Eug2atXSd87iW4HmIkINVUnRtTRQlCAKS12mu48jgnMgSFioKZ5-SvZBp6pPXaVJAYRDhVKbvZCsYwSbtEWLKIx2NPShaL4hO_cyVjNytePZ9GkEenmD3tI-JRPJNzBm6oIgkmUpCd6K9XdSxCGidegUGFLVyDSzAWKniAeletXyGTPFWWUFGwwzj0TGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=K8EO__aXgOrVf4VCm9sqmJmf_5M5BFJUX84asoFzyZ6MRRu9qzT3K0PsuRurJHRTIftpk_YMhhpjmSHOX7E_U69LMHrcYYpIhHoX5qe3vGlzs7ISqeC6hN5qRXOUJchKfclbclg5y6Q69byJDNNrlmj77gGOwFyxYy6x5JzRZK9_TYxBLFHGRybSxoC8R7LNF0OqxpFatkU_FJZ-eM_LAZkSG5ZdYOVkwLC6My4X8AiXegxE1NtATApxZRKoYe5pb757kJeU4s2EZSV73If72n3YM4LJht39nWsqf696l4EUMaqA1n2Wl4hFKaMkpjUY4xebdbPiYD_49WOnEvG6dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=K8EO__aXgOrVf4VCm9sqmJmf_5M5BFJUX84asoFzyZ6MRRu9qzT3K0PsuRurJHRTIftpk_YMhhpjmSHOX7E_U69LMHrcYYpIhHoX5qe3vGlzs7ISqeC6hN5qRXOUJchKfclbclg5y6Q69byJDNNrlmj77gGOwFyxYy6x5JzRZK9_TYxBLFHGRybSxoC8R7LNF0OqxpFatkU_FJZ-eM_LAZkSG5ZdYOVkwLC6My4X8AiXegxE1NtATApxZRKoYe5pb757kJeU4s2EZSV73If72n3YM4LJht39nWsqf696l4EUMaqA1n2Wl4hFKaMkpjUY4xebdbPiYD_49WOnEvG6dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
