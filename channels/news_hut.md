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
<img src="https://cdn4.telesco.pe/file/slUOgzZ26LQzNTPbnAtSW8BTuR8XqeiMFhyGDgZkpFP8Tuz4CsN7IOkscu4IKbYYT493gfVMXVb8UlJAvrUCAdB9tAwQ_-F5hG0-Oph8K2D_ItKCMb9R4Bnif4Vi0qxCLqJwewAmyavF_PLSqVmYqNS9vdCQjbd3bqanD2UjwaVzgulGW3hLx6zjoyuf-rLXu5TXsRh-4ns_NvoiKo3YfKAbPWww1rOejUQ63w9VswM0BhKqCpG5pvgb_7w0LOI9T2oPMt5MHeqevsNTD1MoaJUS3zW1UVtJnL6iqmrrQIfIIslS4NZom2qkS-OVmPbQzW6ic-fv33bkMtf5lTvfCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-65347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=HzA01cLnumOwxlJKzeFnlDD5vN4-Gsm76qiQTI0CG1fdNtd-hokFOMI9ePKZeHbl2ZV9h-BQlxPg8LUTY1_6Osh8ateuPosMeuczfEg8ZWcRzxXE9T-0BF7NqRqmcjIXANg0vrSwDriisiArtdW-xQyo7bsDRY1GhDfpxjDtTAeofpqJiYIbE0gCkaovTQYe-RgAYoBE5dBuL7ObfoDkD1g0yhw2KF3PhvaYdBilVq7PxER1iAODFRJnp0qBiD_sAKmQNd63E33jlOllLo-7C8u7qfWrmO7QMb_dNbsDKZQgTmvqyKHr0rihO7eIdcXXhjvBYOR_H8S90VOlBQRwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
@News_Hut</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/news_hut/65347" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVlk4X1EUtS8ij1HLOr6uEK1maAUZBw9GQALpf_nfaX4El7lEGwIKLsBJ2dzVGtrghxsMF8iKwMlgiQQASy7-_5WEZUrLRLIRPagLSUiYtOAtr3SpMrxiBq006mLul7rfzCFMUAL_gGRibzHeNtSP76rZmIOozh6zF-BYzwA01iIhDREA28NEzhsqb_MlloQ-ppfQf8aWzVZk-W5iDoi72xZq0UwH0EoRARpSAWrLbh9Q2hH0TgWYnKgrAdTbhML3CnPO1Z-Rth4ae8jGn8TnEJfpQOW8kDaYrCmN-GDu56nmZi3nNuW123DqYP95VDk3gzqsDF2S1dfp33GVFZ89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام وزارت آموزش و پرورش رسما امتحانات نهایی پایه‌های یازدهم و دوازدهم، به صورت نهایی و حضوری از تاریخ ۱۳ تیر برگزار خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/news_hut/65346" target="_blank">📅 17:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65345">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65345" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJcIJZoR0nJQFjO3bLILI2behQ6eXgzFAPWu9pVgmSYXOX4FhRXD_4L39tqZrlSZphfMcMLy3goFbKtpwj1I_eGTD0YINJ4FruGH7zgqZ0wiwPO65I9_usrXu7CbzbWjHLXRO8Z7t0_GjgvX0uPLDlxs5QC0GMDkISWp0N4TiBKWEKFSeBrPGK0x2YzCt92iUQ5hpOM-lpeoDsYstRtt7wlH9xuNet0XpKXUkoVu4YvdSud6WeqPlSHp3WfNTn7UX0FYUS1342rsAJTuktGZnEXTa5WYw66WYM7JNuBfASrr9KdIhqosdPFXXE6aZVPYzi012DtUlfl8XLipo7xa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمهوری اسلامی پاکستان به دلیل فراخوان اعتراضات مردمی اینترنت منطقه کشمیر رو قطع کرد
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/65344" target="_blank">📅 15:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=oK6UOHEdyvk6UM4VYUytC2YIeH3_jScftyrUVZdOnbA6wdX_3pYc7TB3-4vjmPB3IvSGzlB7Sd9-MIOhpZahd4YWIc-EfNZ3yZPavTLPEU6RsrFXk1d-9oCW6lKV4FT_-yBPhllSFHMNlNlmIr9_YVgwkOaXpxIEWMw4MSDYbPIZKtBl2rKHJKUwe1NXx8c7L5A7aqF9VW9BTOcKZ3kMx114wgDT3gGuPSaHSWskskTfcrub3Jxj6_2N0Ct3YKf931GodUyghEVk18KsQhGnpToADYo1r5fvq__9LtAf5_ZAsGMjoJOod2VSVIohGYoDrx9y7bZkANE48zPAxptJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65343" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65339">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65339" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65338">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65338" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65337">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65337" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LladEuRVWOXufEgB68FdTi2sMUZSuuwIsFBDeSv5cYSoLswBgd6yTuSZcKUzwVfq4vI-r_ABEpTb3IQVw4PCzLRsQ28lR0xeDsDbr6vvdk-IMg0MD9U0ub7Zp3kc69YANnfkZZpNO7TIlyBLzVmqUdA9NmbBmXPOvEAVfPffktWY5bkzaVtSWTVMrwzdf5ifbrP2_voE69d4d7aWNS4zB1s50CnmoXnFDUHua0WLxnlUNdPdynMiOqtXF5UAUznasT4u4wz64ybhQJ2af-eJ94SvmyIWiYnXoIboI2oCKYrVDOJOjWRyJMjjBm0UK1MwN4MGwTxE2EDmPdPkOq2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
بیانیه فرماندهی مرکزی ایالات متحده(سنتکام) درباره اتفاقات و درگیری‌های دیشب:
چند لحظه پیش، نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند. پهپادهای حمله‌ای تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای ایالات متحده پس از آن برای دفاع در برابر حملات بیشتر، سایت‌های راداری نظارتی ساحلی ایران در خارک و در جزیره قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در دفاع از خود آماده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65336" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQVUZ9qaa8VoL555zTz7uiTTTJ93fYRbriWVe5x-tUay-ybdVp9SCssgmKzdRuqIJs7q8RT7Ct3ndJTSKcDcDp2OriFpewDcoeRWYCPV6rBfOmI-oiykPvO9EPxelkJbxL3voxou9fN1W29kq15jei4EWemhEbQ_u0o14ZGGQPJIiOvchXMZYd0qjtNVnhaOLVy4jPq9RtbDgW1TiyaozJHeoTMXYTmvcQL-ZOjEqqE69ZMRjCVA-U-ElBL70tfMRfIKmD4pUpgYp2tAKnrfgru_N8Emf7grRac5mcZHWkCpvBVaZ0lM4TatjnRo9KWG9ZdnqyJPmGxfIT38MQMjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم خمینی در سال ۱۴۰۴ Vs مراسم خمینی در سال ۱۴۰۵
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65335" target="_blank">📅 10:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65334">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65334" target="_blank">📅 09:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65333" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65332">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65332" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65331">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65331" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامپ:
ما خیلی سریع از ایران خارج خواهیم شد، و این خروج به هر شکلی که باشد، چه به صورت یک توافقنامه و چه به روش بسیار سخت، بسیار قوی خواهد بود. روش بسیار سخت شاید آسان‌تر باشد.
اما ما خارج خواهیم شد، و قیمت کودهای شما به شدت کاهش خواهد یافت، درست مانند چهار ماه پیش. قیمت کودهای شما کاهش یافته است.
انرژی، نفت و گاز شما همگی به شدت کاهش خواهند یافت. و صادقانه بگویم، فکر می‌کردم قیمت‌ها خیلی بالاتر برود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65330" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  ما یک سلاح هسته‌ای را از بین بردیم. این قرار بود کشوری توانمند باشد که حضور هسته‌ای داشته باشد. ما تا حد زیادی این کار را تمام کرده‌ایم. به هر طریقی، این کار تمام شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65329" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65328">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65328" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65327">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65327" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">«منبع ایرانی: ادعای العربیه مبنی بر موافقت تهران با انتقال ذخایر اورانیوم به کشوری ثالث کذب است
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران روز جمعه گزارش یک رسانه سعودی مبنی بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به کشوری ثالث را رد کرد و آن را نادرست خواند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65326" target="_blank">📅 22:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65325" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxsyNuu987TwQ6zRZc2_DP4_Fc5C437sVG09RWqMm6sZAcwB0-iSqAln0jG5WDvlpGgS9ZaxAo72ZNDC3gNihN0rKU0DtCWXzRTtXT750m3e3FasftlQFBvw2y5fgfGXtQ4REXcKymh9CZdNLr-g_wTAgONq-j5gFDXOyoH7mcF8xqKni0AqNVBRHaUiiTvPMjcim3BCbialtEG0IwMiDdwUdMqkRvX0ZrNLrWUM-f-T9sKK1ZGBLmrx35P21kV98eH8kFfV0dxSuZpccJ002lRpW3uHYl3P6HoPFZvJdqV5XOjF1sHnwOShUTA5L7-04_nMpD0LYSL4_xBAC3I9Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65324" target="_blank">📅 21:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izupdr4F8yflZZkrPgUvu4yCLKRKANQ9XV3t2yCo3gCfrb83pog6mwcHjKciwHGsVvfkWX7o1jAnIWqcIuqsQn-RRlVO1DbOYv3XPX9kcs9AC74LX4i2CT1iZhm_FhIc-77_q_7c1SAmVEsN-_DMTIUcMajmLZkOQ4cG9veHvYCQ-DZYrvmD-yM85DRMJDnc85GhFbEiSK5OlzqZLIDq6Gomz21-Y8-PL4SBtpj32ZUr_quFsfyWaMKCdp_ndquFP2GIRccDA1ZcEZJkgzvbMX9n7RvPW_ER_Bx4dLNOubwFs5bmSn0bazECC1yw8wCQfZUarqFu56MbGE1OfvJWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
صحبت‌های جوزف عون، رئیس جمهور لبنان بر علیه نعیم قاسم، حزب‌الله، ایران، اسرائیل و امریکا:
به نعیم قاسم(دبیرکل حزب‌الله) می‌گویم مردم لبنان، مردم شما نیستند. شما نماینده مردم لبنان نیستید. مردم لبنان از جنگ بین اسرائیل و حزب الله به ستوه آمده‌اند. دشمنی بین اسرائیل و لبنان باید یک بار برای همیشه پایان یابد!
ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
حزب‌ الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
خطاب به اسرائیل، از جنگ از سال ۱۹۴۸ خسته نشده‌اید؟ واقعاً می‌ خواهید در صلح زندگی کنید؟ بیایید بنشینیم و صحبت کنیم
ما آماده‌ایم. ما مایل هستیم. ما متعهدیم. آیا شما هستید؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65323" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTJcpAf5GZaVAgpg71-3ei1fJfSCnAct4JhTG9WVEqmkMyVT-q8EqKLpIXNLPvmmBwUEFxVepRNRN7-j9SAyUiXaQqUZ73baZlj4aJm3TnXh8h4mHwhEx0npNqQeI5moW0_etQLE1mJbd5qV-2jl1dd9581HptagdVdbouQp0i1vpdCAmkb5Q2SQr02J8UlYlrgDoMXGXwc8cSKae-NJyA_dG2QRvDoOG8T77dSGai5CAoth7pjU8kZuHGC1rpLqra3Mi_fJV21HYjSuRRFZ4hOTf71ttL0MSh095Y7v10CtxLhdl2_e666ZlMCqkua4-wpiHZXpbX_JLVDCfsxBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65322" target="_blank">📅 20:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=jxGixoHDqE1MB06lPARSELhllWBNwyUH_TOW1J_k7TMLQVjqaCc-i-J7MzsRU2_ijpMdS49iK9RaruiFhsFfoK2IkF8-VPv_HOK5-1e3iCxx-H8wT-1eM3rYQNiE01FglPuRWHtb1iQwZRTpLQMRlErwQNexTYCyRhs0fVwDo4oErZr87NpKbCeF5bitjqh9rfWjm5kcgIYJ2ZWULcM2o9Yq50rIq5suq7L_0XNOgPteBXvpx2HwaPxzchzaCxgbEwLfuk9-NGoATwUmqY3Kq09ngx7ZK3hZunwuqTXd0uU-mj01-vBG_WLsGzQzbZFWJ1tCyU9krc4LiKWrqCmJew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=jxGixoHDqE1MB06lPARSELhllWBNwyUH_TOW1J_k7TMLQVjqaCc-i-J7MzsRU2_ijpMdS49iK9RaruiFhsFfoK2IkF8-VPv_HOK5-1e3iCxx-H8wT-1eM3rYQNiE01FglPuRWHtb1iQwZRTpLQMRlErwQNexTYCyRhs0fVwDo4oErZr87NpKbCeF5bitjqh9rfWjm5kcgIYJ2ZWULcM2o9Yq50rIq5suq7L_0XNOgPteBXvpx2HwaPxzchzaCxgbEwLfuk9-NGoATwUmqY3Kq09ngx7ZK3hZunwuqTXd0uU-mj01-vBG_WLsGzQzbZFWJ1tCyU9krc4LiKWrqCmJew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65321" target="_blank">📅 20:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwM7oqBRjaWjtEYlZfDAPIxrU6DR4S3oU-Yut5tg0cImIzzbLh5RGkPBTB7QlfYHku3PF1qPkIVCAmfkfiFubr7WCod7VwKzzikQJ28lxS-0SC_sk27I4M5wX6vKE7qYSxedGZcbMc8GEP_k9R0K6qWrldHcROxmfukxsxpadJCGlx_gWGEP-B6F8PvrVh-1VkQxzoLrIliRf4u2cbbeP8Pq09cMA7USYfxaP1iYFsniIAKegcJtJyhru-h2fuJwl2MNYO40YOal-ZLlIO50AFyDcYZw4lp3iGjwyUlMSgvcw-bxJYwaM-bJCyHD_gq4pnapnVH6dJ6Gcy6vPBn2ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65320" target="_blank">📅 20:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QCZxdzx8rXJ93u637DikRfzkfFIc2p_ExhIpqvTsFIq7gEC8wP8IMQB5ScHGErYfDHSo9wL9HUhgVAmEfMkZbzI-iApQ8utDvT2Jgdz8D40xzFLc9Hg3J8A4YfDbpgPopWEOLCAsjdMfiVGcr7PI-Kzsd9sSr00Jk4wasL8XAnY5FX_nK2tQ8kqbfDOH8orMdRj7hcd9LsbB1oOGXdzjo4zY3Xc60apQXjUNR9Cnw9kxxOMgXdje1ZQsH3m5CAe0PGKZCZezLDBunfd7zSidsSY0rL7p5r9pEBehZIiqutY0zra1ztBwl2udA9UIC7XBuj1fj-y300oOYF6qR8J49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=QCZxdzx8rXJ93u637DikRfzkfFIc2p_ExhIpqvTsFIq7gEC8wP8IMQB5ScHGErYfDHSo9wL9HUhgVAmEfMkZbzI-iApQ8utDvT2Jgdz8D40xzFLc9Hg3J8A4YfDbpgPopWEOLCAsjdMfiVGcr7PI-Kzsd9sSr00Jk4wasL8XAnY5FX_nK2tQ8kqbfDOH8orMdRj7hcd9LsbB1oOGXdzjo4zY3Xc60apQXjUNR9Cnw9kxxOMgXdje1ZQsH3m5CAe0PGKZCZezLDBunfd7zSidsSY0rL7p5r9pEBehZIiqutY0zra1ztBwl2udA9UIC7XBuj1fj-y300oOYF6qR8J49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qevNANzPO0-6hPUz3usE_4TqP-OegMjSpurDtCaThJjWc6c-1ZxMrvid1IBxit0nVOAf3ysQC5QUBYlTk2ZTQwFjzG5m2-BHxKxoq_HQy3ty4BjpaukgbPjbz0MAd0kVNMdbZcsrDYy4WbdLSwGgOnxi1s6Zhxvk7ktyGuuNSNuY8VPQ-D7h8BpUTydsyAACzyRGWZNo5x7i70o85TlcKiRx3uAihP90YfFGiujoujzVuZN5jCqsxmcQlHXXXrZW_JX-vOgsK75yQMSyorziexi5ZfL4TlMdkCQ2IIYZx4SDFfm9-4v-8-19-2hlopeLLVltdUBoz7qPy24RUwzzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ohtW766xFNcGhbe1TOMRstag5YkE10PrDmy0_32GuC28HCzRYQeF01ig2vcOV8oK8Re254PU2FhajftEprknLIwWL-xYfD4HBZ8uLdmcZtt80dwuZBKYvxY-iuVp-V3EcA5UatFijkyZoFeRivmFujn_zVD6N4kzKV6GL6WiQ9I0qYw335IaOdTQgtzkXGEqOzgDlTdYaLpel26esNws_wE3Za-drUWJcKm6RGBrIvMolUdRy8xXJG4z_VWtO5OQvd6ulKpsHb-lOIZgty3cIu-srEDOyWy3M-JSLyaU7CV_ee0BQxURu44W8lcZ46xtv_j7kga0J-DTsi0dvY5f8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q5PNfy2bX18Eoj9Z1I_EwwRMAyk_Q1fIfy5-FUWHFdhO7-ganIZf6TO2BUluTPuHjIstYpEG-HhiqNu5qPRxclHedI0Yfd9FW3Qgmegl3VonyTFCB5W9D15VOxzC7TYqbJdwvuwsWiuPFYEWDhJ186uvUrgbRTEOdT-OrA0rplYa_hHPUpBwqT5zxsiHrdDSr_o6HNefTVgfKgAoH9VbheLYJvwqKwt_mqxkZHzKthqqCk_bU8tEQaxd3xn4qiD3sbSYqydIE0VaW3UnGES4hDD6vGzqRx4bAaUyo80UyQm9jET9pY_uVT3bvGyywUmJVQtK4opvdBSs52b2JSksJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blKYlc36gs2iqgIBN0GtKxNhMJlcrs8jAs-QqvqUJ28vo-Et38ZrGfN3S_5I3RXSlS-139mL5pUwPk-qd_AIrgFCjXya1w2h9YoL46dutDOLXgudgSgDI9rqevx76I4hTItYJyvI2Ol4Dg3uQCdo8sQFiCEfh8gmTQaePGdXdY-exv_yKhqZ3rHPoW4lmc94sKH_C8_RPf6VL9Q2e9SnAzbASci8QppcvmA7KGG9eHe9IVH-7Ugr4ErigkpdtAPgIpPeLb3vmQD8eksSzwwZDOSIeOiAdIm4YrsT3WANgS_C2MvEk_4jypE72wwHT7NJ1eu6iSGV3l3RGMeA4X9KgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=ZjkqaBur7pBJ_oCRwWwNJox75iK7eomU_gtXzJykHBxDVCgkmPmTeVKACj3hLnZhDxwTIAgXLC3n0ntoqOB6vjMzoCvp9xjtNjpQC7d66l0omHYM2usVMfMpQz6s4kVwE2jrl0meuhXV9HjkHemvKlBLAXDMoeiDtuY7iGp4IQsKzkBJVriQ2sQpRkq5SxNwuEggEJ903hD3OMNKwC3PkBWN15D4BrV9qFX9qoi4Xs54U3mMUWMqtsXxAmIDeQJc2TDvEshu6uiX9sUZQ5C_gvvklZbNTRCo1WNobWObWa2dhUPgbstB-EjneWAXQy4I6Rs-nY57xX3-U6Di0jaxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=ZjkqaBur7pBJ_oCRwWwNJox75iK7eomU_gtXzJykHBxDVCgkmPmTeVKACj3hLnZhDxwTIAgXLC3n0ntoqOB6vjMzoCvp9xjtNjpQC7d66l0omHYM2usVMfMpQz6s4kVwE2jrl0meuhXV9HjkHemvKlBLAXDMoeiDtuY7iGp4IQsKzkBJVriQ2sQpRkq5SxNwuEggEJ903hD3OMNKwC3PkBWN15D4BrV9qFX9qoi4Xs54U3mMUWMqtsXxAmIDeQJc2TDvEshu6uiX9sUZQ5C_gvvklZbNTRCo1WNobWObWa2dhUPgbstB-EjneWAXQy4I6Rs-nY57xX3-U6Di0jaxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeAGfSrunhekwPJoT_BUDaCgNBoLYW-gegamKlB2qjEFbSCQM-guxWvNM5CG9akZmwtRJy40Q4xOCqQ4A3LzpjPJoRmrFlO12jEo6N5YfVxRkkbuNBE-NgepSsU9bpOSUEDiBNCu36Itpv6AEeP94gwqeLYSVbmy9M_ENJGBrydyUQkCZksV0JfJpVGIzSOmjXEtZJC2k5InnnfOheSWkLK8U2y81lOX2oH_V56ohigl71vJjJlQyVT5lNBXpWPPMXOZPU8idxD4gvaJFyMXRtPstlQAycyFPNq6PkzYDDs84LFzIdRtUVgGRSbnFfsTYHUXOvhD20uss0P4a_FvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=AhDlfl3IzIUJIDwMqocgcCLv_jWDWabynXQB-jGeX_pwRvtiRjaJSvqz2Hm5LZQiBTNcHqWy0M13dFjIfWstEDraEa529WrLF2XjzeVBgG0kqlULyZDmxz7riQ_9T1EYfnb2fed3arvsWpY51xmqxoO_IWVIug5XhGomu9vmm_CTI2WY2Zpg4jmiiGj7byje3IJxszcu0pKNHUcoCaoqc_t3TMBCOIZhM55DRE50OVeQE3PujICGp7ueXiEoDWs9JVNAMupv6ZoVKcXj80GG1Yh2pmtys8h-WrRME4WQGT8P4GFl5yS3L6qwgHiErFFrjFq2sCcCrXy-xKBc2LGdZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=AhDlfl3IzIUJIDwMqocgcCLv_jWDWabynXQB-jGeX_pwRvtiRjaJSvqz2Hm5LZQiBTNcHqWy0M13dFjIfWstEDraEa529WrLF2XjzeVBgG0kqlULyZDmxz7riQ_9T1EYfnb2fed3arvsWpY51xmqxoO_IWVIug5XhGomu9vmm_CTI2WY2Zpg4jmiiGj7byje3IJxszcu0pKNHUcoCaoqc_t3TMBCOIZhM55DRE50OVeQE3PujICGp7ueXiEoDWs9JVNAMupv6ZoVKcXj80GG1Yh2pmtys8h-WrRME4WQGT8P4GFl5yS3L6qwgHiErFFrjFq2sCcCrXy-xKBc2LGdZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=aS58Wc7X8pzj_iBCjapwJCHt7MNTkPbAw1nq6Tv4sQ0VjqGC4gPoopmuvMZzOd7hM-n5vQ-oxkdZF963ZSceBFH_iJHMObLQmssisN6-w24Pl-Gk9ZOejajbKQynOxAcus7nxvbJgOxYJI1gfOtB5mWy9ON99AWD1sHjl6_Ems0Ny_X1xcMwz9PXilhyd3Z0dK6W3ENvBSq5rl4pKTEeNP5SYHuCSZLXy2gpTekgNm-1HGQUEaebl5RBA8otwAUYAGxDw9tGGXlK8rm81Vw4WzySF1unblI69oHWW1nIKipzZskm7B6z4HYx8oKJNwSBpEwtIWNvkqMwKURbaMg0PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=aS58Wc7X8pzj_iBCjapwJCHt7MNTkPbAw1nq6Tv4sQ0VjqGC4gPoopmuvMZzOd7hM-n5vQ-oxkdZF963ZSceBFH_iJHMObLQmssisN6-w24Pl-Gk9ZOejajbKQynOxAcus7nxvbJgOxYJI1gfOtB5mWy9ON99AWD1sHjl6_Ems0Ny_X1xcMwz9PXilhyd3Z0dK6W3ENvBSq5rl4pKTEeNP5SYHuCSZLXy2gpTekgNm-1HGQUEaebl5RBA8otwAUYAGxDw9tGGXlK8rm81Vw4WzySF1unblI69oHWW1nIKipzZskm7B6z4HYx8oKJNwSBpEwtIWNvkqMwKURbaMg0PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=uacjbSshPemh2eZHGkQ5KsnQrngmgTB6AC0knE6sBQxSI5sFCPHcg2XD-VFJbl77sIxmlYgEyiEX1KbvFmz8MRxOSJmkByNluSqvKDS5x-MwhEWRLM1hJ4V_12ZWIZE7CDAU6u3AaQytet4K0nGg6VKk6lyJUSEA_0gIl143FzPWsYNEL2MB7FBv8HTQ0V2Zi2wtod0gKH65_hQcboOeC_cD-mq7l9OU5It6oe-OU-EDipiE5F24Ka5xfbCNnBWzEkjfYbm6Zmf6O-1cAj47yc_uRUiaCnKl6Iv2y3vgyyS_da58MRlR7VO1G4U8PySNzyTfxnyjr_2-rDOmPruEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=uacjbSshPemh2eZHGkQ5KsnQrngmgTB6AC0knE6sBQxSI5sFCPHcg2XD-VFJbl77sIxmlYgEyiEX1KbvFmz8MRxOSJmkByNluSqvKDS5x-MwhEWRLM1hJ4V_12ZWIZE7CDAU6u3AaQytet4K0nGg6VKk6lyJUSEA_0gIl143FzPWsYNEL2MB7FBv8HTQ0V2Zi2wtod0gKH65_hQcboOeC_cD-mq7l9OU5It6oe-OU-EDipiE5F24Ka5xfbCNnBWzEkjfYbm6Zmf6O-1cAj47yc_uRUiaCnKl6Iv2y3vgyyS_da58MRlR7VO1G4U8PySNzyTfxnyjr_2-rDOmPruEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=UO8iyMTuB1K3vqPMHLHyieTwJEk6-UdfGTDEeMUd9WJPF31qm603vloJOA_dhyG0d9LRXTG_omP2ubpoR_M1VuF1DxKnlUQgkiMBKrJGLpG6p93PSWhK9hHahKxE8B0t14YJ4eMNSDCLfyt78wG_rgixBFhrSPBdWwjoqF1lxySwxCm9335mrBB3CXbYxgkBdqKMAUguqbOME3C3d_T1FiBZ3iOqCMt-yufsrUDXtNYj2Mq3Q72pUYPD3GGn2NUOl_XN-c3z0L_IdJBxjNSHFLjF0HU9T74RStGNFVEtzb9cd_AR4vyfq7-o0a0JsKZwDiyaE4nY7SkkiJBZWiNnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=UO8iyMTuB1K3vqPMHLHyieTwJEk6-UdfGTDEeMUd9WJPF31qm603vloJOA_dhyG0d9LRXTG_omP2ubpoR_M1VuF1DxKnlUQgkiMBKrJGLpG6p93PSWhK9hHahKxE8B0t14YJ4eMNSDCLfyt78wG_rgixBFhrSPBdWwjoqF1lxySwxCm9335mrBB3CXbYxgkBdqKMAUguqbOME3C3d_T1FiBZ3iOqCMt-yufsrUDXtNYj2Mq3Q72pUYPD3GGn2NUOl_XN-c3z0L_IdJBxjNSHFLjF0HU9T74RStGNFVEtzb9cd_AR4vyfq7-o0a0JsKZwDiyaE4nY7SkkiJBZWiNnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=RUQORyGn4_MbSiXnXbfPsdKfiacQrYD4sYyQ-YhZXpcnDwWmXyqc3QSnkR_6EWMxkfk_UzT52z-PRd21K-DSe0yxqbhVbqYWvrcVFpmcDiAyXLrImdW5zZ7NO-9bxk-6xmftHhO-D0bS1aSxnnBEw0gaaQPSKpjWKYQ58dHeylRsaq5cTvX24K4_hjsLu2IM217dnd1OAHQeqJNZ6NIoj8sVYXaXAO8MquHSzLTRow_RY-A-7ZDaOZUhctr-ZGcgxEe54CNIj-69Z5SSsgni5ITjVfDP0QwxQAb-lx0DpmFYH3TuSFtLCM85Gq36SUKeKPcZJhWUzhZ8bBBB2u_aaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=RUQORyGn4_MbSiXnXbfPsdKfiacQrYD4sYyQ-YhZXpcnDwWmXyqc3QSnkR_6EWMxkfk_UzT52z-PRd21K-DSe0yxqbhVbqYWvrcVFpmcDiAyXLrImdW5zZ7NO-9bxk-6xmftHhO-D0bS1aSxnnBEw0gaaQPSKpjWKYQ58dHeylRsaq5cTvX24K4_hjsLu2IM217dnd1OAHQeqJNZ6NIoj8sVYXaXAO8MquHSzLTRow_RY-A-7ZDaOZUhctr-ZGcgxEe54CNIj-69Z5SSsgni5ITjVfDP0QwxQAb-lx0DpmFYH3TuSFtLCM85Gq36SUKeKPcZJhWUzhZ8bBBB2u_aaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=oV0jQh82BDxAhg2piZFdTQ6RimkqH_YIC3KBqhn-YZijnod0wjBrEQpNSyarp8Sp4ZKd9npua_AYXMkNm-4nGu30uNnwPEZY9mhU1aVXX5nlzWPNOk6vzZCXKjfc5v_PZyoC49FQ2uNjDSF2wT-LiVdhbatGMCKlHSDHkCUXRqabCdq5YVlnQXYVn51VUi1ga5mO_tDJI4bjSXY_x3viwkPWGrZ4UJbMScf5dTuCg6kDQNt8YV8Arp7pFeASSw_CsdzQY3WT7RjSG-5Q4mcwk7FHXBXXE96vIS-nd9iseLrfht3X_oFSZ5mEcc6rd-9XP7nARlrIB9qfZTpT9VaYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=oV0jQh82BDxAhg2piZFdTQ6RimkqH_YIC3KBqhn-YZijnod0wjBrEQpNSyarp8Sp4ZKd9npua_AYXMkNm-4nGu30uNnwPEZY9mhU1aVXX5nlzWPNOk6vzZCXKjfc5v_PZyoC49FQ2uNjDSF2wT-LiVdhbatGMCKlHSDHkCUXRqabCdq5YVlnQXYVn51VUi1ga5mO_tDJI4bjSXY_x3viwkPWGrZ4UJbMScf5dTuCg6kDQNt8YV8Arp7pFeASSw_CsdzQY3WT7RjSG-5Q4mcwk7FHXBXXE96vIS-nd9iseLrfht3X_oFSZ5mEcc6rd-9XP7nARlrIB9qfZTpT9VaYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1tErYxg-nxI8EOb3r0mNYZbiz3KH8Ng-joxmcEJt0RZ9xML9rFDYxGnyJTcKrGN_-fRcl5Fvkg1I7c6kew8jQkV1XilwynnXtEplsHkrOgi2eFvQaUb4OQZVA2ZEDLpiM6zjmKaxCUb4YB8m9l2ZN-NKtoS6PAtD2qL-g5Sf6V8IhlkNhFMZMKAl9W79XHB9yxNNhTYUzjoNzegz0iPXmh0eyGZwmzvqjGyJzFT1zFTXW-pfJ9bW8jPaFW1wy_wrsVOHF2xg-93G9LU7Tw5zQxK0-erva0ZV4x4Nsbvq8DhM4FdRze_Zvlq1F7_in71jWukJ5zaSEq8hU1SIp6VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRwjrv3TTs2iiUJetlNmwECTcHeLF7nurtuuwEIEhcgMFI9ivJJSv6qFq9qmYWeAiMjciOGus3imz2d8MDfmNVSTteng69aJxFd5nZNcTgMC0VfOG0gAOOpPISjldU_Vss3h9Y8VmxqlSrzq_QxVWncBJrCeKLaMhDkA0O01fDIvLuSBpJBP6woek5_UOY-EaOEmN996V1PZuFkpfRWZ4h9zyOP_YRdb7FVH4SFvR7XzV9b87oo8zyd2xIrqNYtDQjgClW7PLfRxdlXBASQWjhPmI0SMGT4RK_Az7GtyV6_kOb0CxUvcmzzQPg-n4my-olgUbuzmivRiq2nqhyX7Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM7ehEUaBw-1oO0wy8Scysd8cl_dohB6TgiJVBy26EuNCsVmWqxNN9aX6dOEt6CV0IAqqCAK5LXL4NUc6VQuBNRhw_ge3mXKGn8cctFBMmZFxHS1sxhvLqysASTXbIYiyYbAfPyJnSDiU-33ITGQW2UEPSjKOtJ48QdGPYOGQsYX1LwemaJAEfeW3omFIg3nD8IpDhucp2cbJ_WLvF4piFjmd2kqzXqGov-E16fX3bXsoVZDnJPpEgPC20SqG4A1T5Xe3tjv5AYURCsAOOEl37xSLSCXkUujSzKI2gu_6Hvepu0dSv8U3i2DjIlN68UlWR_zVM0Vx_wUOG3HfeWrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CytOSdIXg_NiVTBCZAVa7xRQNSAKHblaqIVyE4cwK5JjWzfBiriSwy7AB82Cu97Z49GQpji7PSMlkiT15Bdog4uniHEWPK6Cy9HhNRoR9MK3Eyji9UFKkVB_j-tIqnfRJ-T_DjPhHYBXIWxaG3p_KdGRRnRxpBtpegRJVZYWo_aXEG6Gtl8RCB0IBeIm5CD5ylAPE6Eij8c8oVF9C4b4WbId2N6irguQo0ay2eDdt7ChCh4bFIgRfa9ZZMJk2ixjiktOd3FWsKf-PU6TBlrdUFjCydVabCgDj4RpB0QyS14XltO76KsEOQKzqr-mREOxpMWMQ_0O8tOT4ExMXdijMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQBj44H3EO2E-e9pw3oPNW1ah8m4vxlO1G_1Y-cYeNY3T5RQAceKxot9TbwWJlPzbBGuelPH_7vQNJ2Ohv69J5RPJJuW1PCzMpOzHhGF7Nj4K_PP8nbmMEcFHii8DE4riBU87KPIDL1nxbT2bIXj-wAKurSNx973OkqusViFWQcZjes-Ds04fIDywencfKdkT56TNbGrXeBzvc7oh2iwqAqdjONvLTmg0U6rhumCBsljDye0y_oD2ZTk5lpvMjAgvQm9Lzg-3i9ZfllfQDhDEskRXYj4wWx08XQ5QJJWsvvLxu7sGQQeOEvMswshbWWniJAORSopm_Xqpbr4T4G6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilfXuwPAdPd0-ZzpbIqK3iyW4la5ceZC2ObgggJzxfkjeJ2w8yeYy8a5joZsfLmxO6WMqhZM55SnTnSCaQRKZ-WyNH9JQrnfDpZsEi9M4OsM7fyXolPM-6RJ-d-Rur8oNGPia0tu8ELVBBXCtJJuRc-STIoc3nSk7f3KrsCXL7xt_Y9Pd-BJ2XWuiSZMvtYcZNwgdJQkHa_cxRaeHpg-CyWa3R5_BHPik5T00zW3BBHD2MkTllpd_Q8iVWeWvZw474GGPnpx7xVlkIRPSP_7aucsUy6bOmImzmiC0afEX5G7gCDGX4VnM2q3jt0TVfaqlsepkZk2urXCXoq6Zbpg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=iymViV0aQ-nhm5Jvu99V-EkFnpXpO30HdUUyVLwx2fae94m064H3y4OUY4XAz_eQ3Z_f7rJAtsJUwz-BerHFuM4XXbAs3hvYypJq21LyyK-4Rk8N96BqW7PodXDPem1t2oZL0x7kEyNZvJMAkaxTreJ3v0XndF7clTp-BCmGe9H_4HhNH0KZQG1ww3TwnJqqNWpfAYqttihLKbx0YOHfCY3mZam71bZhuUze3AMmgDi2eH86W8y9esS5AILA_dt4GHSpqwVtUhcQZkM-4SoTxqkZwSOZ5sNDHuR1pqoKjUE2LBCK-xwtQlATXr1UeqGRiRgUMSs5qkbwC0XjJ1zrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=iymViV0aQ-nhm5Jvu99V-EkFnpXpO30HdUUyVLwx2fae94m064H3y4OUY4XAz_eQ3Z_f7rJAtsJUwz-BerHFuM4XXbAs3hvYypJq21LyyK-4Rk8N96BqW7PodXDPem1t2oZL0x7kEyNZvJMAkaxTreJ3v0XndF7clTp-BCmGe9H_4HhNH0KZQG1ww3TwnJqqNWpfAYqttihLKbx0YOHfCY3mZam71bZhuUze3AMmgDi2eH86W8y9esS5AILA_dt4GHSpqwVtUhcQZkM-4SoTxqkZwSOZ5sNDHuR1pqoKjUE2LBCK-xwtQlATXr1UeqGRiRgUMSs5qkbwC0XjJ1zrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh1OmIqFcxx6fQiqreD90xQB3BlhJicomcctcDaqPYUPowz7nSKaZ32oWma2CZwIh2HFw4XLofneNhcfY0tqaIsWjEPV7Pepzf7fBGu-HXu_YoL2SfkG67WNzyhU3gb6c6GwWQr-CUeRUSDkQn6cfuvgwyYCezeZl4hZhhKxbN8AYx40E25VYRJMVT6I-Z6xQj7n_mvB1l8uaeK5RvwkufojJXUbK7N8nA-cK72q0Mt8qeUvLiaPWM_IpzOEJgQ0CUHq0VZczyBu5qvphbDIr3YSzrz26eTJ0WgfoQdjGZvuGxm_LCEr3EfEYD_sjEG6I1lHxnoJjkh5h1UkaeALwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SINZmv_W-MPFajtz0q_CLlhiTCxvRSFkn338noD0I-fgKsfSF9VtlAui4IEOBl4-ejLFRX_sdtVEXzBf49qae3sg3maRXigcqi-bjbZFhLjM7Wut-JIBDFXXxwDY8f5ykXRrn0APJk_87Wn2D35fFHXYrzshDWSv9bVP-ycE3KALSeaRTCvDgLyiE1sKH9HvW2xEOH_ILLWHa3PTEOkdEbcgMLXlMn7m4cw2BxRQ4qJHUBTZ0fjsrlQxWlU5RTZ9mztVt80VZ06wlVc8SRLgiu4_As9wgR5-GAJY6GcTeyaTpf1E4y8eHxB6kyTBCWd2QcWLuBb2vtA7dgctu0wpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=bZCdvVOiSO_Ev5ENRnyALWGEqttpXUlPz3faTgxu2VL9VnT2xFX4BDF9GgJC3hWfvJa_GVP5JSXBB58LYehg8KASCElXtX7zrv6OgejPJ26q61HN-54CqFkeA4hsr4zBZPqZ1HHWFwmh5wuJpA7mRSMy3_dozCz3_20FTucWP3i_9KzdKsxO_-qLxcWoDFDf407qQItl_-QiyhCCF68A4m0xNCGsiCuPeF3356Z_tkOtKPIeHHNpz__O14I6vjdZ0KJdgSfCCWnttXO51HSlEVRw8il9UesOhlDBBmAXqRPL-hVDNIL-h5JUdibkaLOBmU-9uS5JTJFjODaqLr7pYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=bZCdvVOiSO_Ev5ENRnyALWGEqttpXUlPz3faTgxu2VL9VnT2xFX4BDF9GgJC3hWfvJa_GVP5JSXBB58LYehg8KASCElXtX7zrv6OgejPJ26q61HN-54CqFkeA4hsr4zBZPqZ1HHWFwmh5wuJpA7mRSMy3_dozCz3_20FTucWP3i_9KzdKsxO_-qLxcWoDFDf407qQItl_-QiyhCCF68A4m0xNCGsiCuPeF3356Z_tkOtKPIeHHNpz__O14I6vjdZ0KJdgSfCCWnttXO51HSlEVRw8il9UesOhlDBBmAXqRPL-hVDNIL-h5JUdibkaLOBmU-9uS5JTJFjODaqLr7pYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHeTQwX8R1L44RtK6PNV3kozkSNNrsL8Wr_taGteZddjqHVQDxAZniRHnbIEoyCnkD7ozvKQ4uivKEChbQ91sfRFbDYmVHmfvEOHtHnTdMbhi8JbsQzFRim80y943f0le_ss31ZwT6ulerys88vwHF9ZhVm_9PXjD5fzteCdyiQUirkOJxu72uKw7CbQbz0auY9q-kKlQGHMHYaU_6k7JfG7gQT1PLuGH5Iz2Ua5BSTvCwOBJTmW611LmV5XwfIaukZ8eLMW-TPZzMaBfEZi2X9_bwrBKeqIidDKJQNqnUk_DoHfqiIwyhfSvkFmBneWwmXk6sz9XbmNub6XC-Kd7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=hz80ce7ablGhF2ZkPIxYj7kzc1gtS_ag5K6u5mDY3ZY0xuGZa3G5wB6jEFiwATV-Ws6wpip8_BXKPmvudQcrJhDd5SWFjFXmmiMtTvntAZkg3pthokHmhouimPPMHj50ZRxzlNRvUkpiNU_kOzEUQube0Td-97sBCBxcAw_crabkcdbqbOVwmvlrWKFj_EXsbckbWQYawyIgiCDELPOGtPXFZf8Gp7msGwQ0xEV_sG90dFEnXW5EAiEmzr3LHaPuzG-TSshJjJ5i-iJFR1yz-wle1luMboLP0se0GUrebDUWiqzgKjLCPBfgzgItSClyP0gtXC8jed-XTLJCB8vT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=hz80ce7ablGhF2ZkPIxYj7kzc1gtS_ag5K6u5mDY3ZY0xuGZa3G5wB6jEFiwATV-Ws6wpip8_BXKPmvudQcrJhDd5SWFjFXmmiMtTvntAZkg3pthokHmhouimPPMHj50ZRxzlNRvUkpiNU_kOzEUQube0Td-97sBCBxcAw_crabkcdbqbOVwmvlrWKFj_EXsbckbWQYawyIgiCDELPOGtPXFZf8Gp7msGwQ0xEV_sG90dFEnXW5EAiEmzr3LHaPuzG-TSshJjJ5i-iJFR1yz-wle1luMboLP0se0GUrebDUWiqzgKjLCPBfgzgItSClyP0gtXC8jed-XTLJCB8vT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=Q6Q7e45Tr4z6veSrQNFZyCR_h39ip0tQ3PXSqEixUTDt2YkABMvVFzO1-LnFl7-P6z4I_Cud1raNol11BgZk9AmWEcFxJ-R98nmoZKaIfXUNtPsvZJ89cZDNaauIY6LsCW8ULebwOv1YFp-92JVlXU9fMIwR8txhEThWN0VHrxHDcAORqa5oTENGxIVWP1rzwsyEpcGwRYZaCqW2yhISwzlnSjPVFB7T6SL2Ke5Nid-96RodDwh9V5z6Ie74P2gMRVjx5hI1417qAGXyLRXF0ugufv9AfDa9ccorjCC1Tvupf0ClYRg-eQPuT-CHGsI7ReBM4SwcJx0ruT0Icpx5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=Q6Q7e45Tr4z6veSrQNFZyCR_h39ip0tQ3PXSqEixUTDt2YkABMvVFzO1-LnFl7-P6z4I_Cud1raNol11BgZk9AmWEcFxJ-R98nmoZKaIfXUNtPsvZJ89cZDNaauIY6LsCW8ULebwOv1YFp-92JVlXU9fMIwR8txhEThWN0VHrxHDcAORqa5oTENGxIVWP1rzwsyEpcGwRYZaCqW2yhISwzlnSjPVFB7T6SL2Ke5Nid-96RodDwh9V5z6Ie74P2gMRVjx5hI1417qAGXyLRXF0ugufv9AfDa9ccorjCC1Tvupf0ClYRg-eQPuT-CHGsI7ReBM4SwcJx0ruT0Icpx5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezhm86IkJbresHApN_PVYsuEyUhYsHDfZTh6F9UpMD1nAPdDl1w0fApY2iy3yYv7TMNkZlocLTWhw-3HkvfobekKrMOpT_m-Uag6LznG-rldvI9xtXs0_FfrMPdyKylLXaL5YTcM-WEMGr5DP_eT_c8n5J_hsEWGsNlxNGDzMbVtln1QP59WFQZ5V77I3MC90-tW0-1z5tAUM7HI4hEtge8RK4WrWRrvzpGSg3ra2oOvrdBtvNfYao5hLsm6VJoBks3lAJ496ymfw4PR4JPlp6CH8dPJfqnsuhveh6ZhmF9uTM_IMUG7N_Q1uPevg-gUN55Y5cMC4Q9J2D2yIK0KeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=MkIOxw96A1bcaBBy-lfDZ4sAYR6tIHTCspiuzm8qKv89UGYVXmcUI5IuObtwFlmbiOBAa4DD3dEJ8ZhZTSu3cg7QUfBXkaQnuG1M5rYcvzmkrUev4Hqqd6PnZ9BdfLx6Mue1LpdZE7cBIskTbvKetpXVdrw_yRXFKrSBr6Uj5DzxkDeWAVUqtDWPzwPgHZxiE_xhndfX3nbrFGuCkXXBBY4s4MpQHh5oFAzOz6_xK-P6UM_SKU49vLGoZcAr-RrWrZJ-6NVDk7Widv7uMNWaFwnTTr0FNOSyRyhZ2BsZ0Ad7A_k51C7A8Pa182AH9NnsEkiiTEkVgFwC_4lA6gLeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=MkIOxw96A1bcaBBy-lfDZ4sAYR6tIHTCspiuzm8qKv89UGYVXmcUI5IuObtwFlmbiOBAa4DD3dEJ8ZhZTSu3cg7QUfBXkaQnuG1M5rYcvzmkrUev4Hqqd6PnZ9BdfLx6Mue1LpdZE7cBIskTbvKetpXVdrw_yRXFKrSBr6Uj5DzxkDeWAVUqtDWPzwPgHZxiE_xhndfX3nbrFGuCkXXBBY4s4MpQHh5oFAzOz6_xK-P6UM_SKU49vLGoZcAr-RrWrZJ-6NVDk7Widv7uMNWaFwnTTr0FNOSyRyhZ2BsZ0Ad7A_k51C7A8Pa182AH9NnsEkiiTEkVgFwC_4lA6gLeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpNNuhYPM0G_uTFXOtEWdNJsqIQ1Af42hoAs1sgQ03PJBWpQEq9pORQK_F_Dgc6_K_NUCrlQeNZERdT3SD7He73DMPRfOTEW8Lrp8PSUfxM8OEqJ2UlOec9erhFxYOs-PspYOdfbrlnLv_EE7oBVd9Ee97Y1BucctJMSK2Mon1mvslmGidaxIa-63EaU0mG_ZRE_BAdGHyOZvArUuBfUGN1ozo3fqNOVHtHt-3Z2c7UR4kPe6IocjRGxR9pqCDl26mDzpaah687dtW9pXbNxtENf86C6xomEMl30SBYChpw--HkLvZvrluetAQKQ-IDLGggOy7LzcSDOf7QZO0agVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=IZVT3CV0fpvbxpVCvtZmIUSVOBTqewPkfL7Mq40R1n77OJjd_m_YMjjJGAVGK0GWod5MWBvOjLUKN2EIDigesNJpcjKfMARfGFzYKbYTP7Hn1L9Zhn2AoAE1HSZ-I530B5vfb64bQEOO3jUq6obvzbz0RBUz07Gnh6UptlQuPib0Sohz7ewncMle5Nhh18hykDd__RmKSJALatWQ5z-U8PO9pMmK5iFyAUjtB9D1a15EfFS7C7TnbLA9_tPJ6QP0LTtsi0yVhVeEZud9t4l4sgpGc9MTvKNM8NIxvRNxTrGXwzih293uMJuLypwuaqKKeLlMBM0YOnzElVYQHFRqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=IZVT3CV0fpvbxpVCvtZmIUSVOBTqewPkfL7Mq40R1n77OJjd_m_YMjjJGAVGK0GWod5MWBvOjLUKN2EIDigesNJpcjKfMARfGFzYKbYTP7Hn1L9Zhn2AoAE1HSZ-I530B5vfb64bQEOO3jUq6obvzbz0RBUz07Gnh6UptlQuPib0Sohz7ewncMle5Nhh18hykDd__RmKSJALatWQ5z-U8PO9pMmK5iFyAUjtB9D1a15EfFS7C7TnbLA9_tPJ6QP0LTtsi0yVhVeEZud9t4l4sgpGc9MTvKNM8NIxvRNxTrGXwzih293uMJuLypwuaqKKeLlMBM0YOnzElVYQHFRqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=PT5X_GRLzIfb28RUlYQ3iFrlVjX6juLqlIcC9FuvBftJpCp3-JPFS-yW_gzHDdW3CRH80Q6JA4rDhgYh0iDJhYmzatIh5uMc1KARkWwaAsLhjE636jEJxf7wCSdvWBIbgBmI1SgITzZDlBV2eYF1ICbFOOxWv5QjrdFYoy9XmxcTE0KZhLHg67NXlZD7g9rSgdSZqbIXy7dFDImYJpvPqjiUd4bPMiIucN_9JJsMTHvPwqcl_kFZ-UnoFhaoxKH7GO7dXul34fUSuPN9jyGFi8I8daZJ4StJxagr-ffr1bBR1oP9RZQn46IlKAJXBWrlLbn7hsYEcwH0QjbUyXEVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=PT5X_GRLzIfb28RUlYQ3iFrlVjX6juLqlIcC9FuvBftJpCp3-JPFS-yW_gzHDdW3CRH80Q6JA4rDhgYh0iDJhYmzatIh5uMc1KARkWwaAsLhjE636jEJxf7wCSdvWBIbgBmI1SgITzZDlBV2eYF1ICbFOOxWv5QjrdFYoy9XmxcTE0KZhLHg67NXlZD7g9rSgdSZqbIXy7dFDImYJpvPqjiUd4bPMiIucN_9JJsMTHvPwqcl_kFZ-UnoFhaoxKH7GO7dXul34fUSuPN9jyGFi8I8daZJ4StJxagr-ffr1bBR1oP9RZQn46IlKAJXBWrlLbn7hsYEcwH0QjbUyXEVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=MhdKiwbtx6Fh_rx5lIo6RniEY0sD73676dRFidIIGGALy-eRN2eHDoAeqMirhIkIRbUc1E2cF94hRDcLnvGi_UUykJ09xNI90QKar0uLik0lOGW9TMWlRpk6sd64_9wcgkUADqkc3KyxYpDit8FjSlKQ2oqVg3VljLR4Pfp9AAw1UN_0bNYcvBf20bKO1a8VbGzpjJEYCneGdCYEozfWnE-7KP1vfAI9fZojDz-odBjWH72UWU0qf5t7q7d7gC9w81hnAEflT4s2rnZ4sqWkIbS3AEj0T4KhvKae8l0YYRurdzX274zFhBGCSPTrPHfSNI5JN15Rw2az3oM8JDOj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=MhdKiwbtx6Fh_rx5lIo6RniEY0sD73676dRFidIIGGALy-eRN2eHDoAeqMirhIkIRbUc1E2cF94hRDcLnvGi_UUykJ09xNI90QKar0uLik0lOGW9TMWlRpk6sd64_9wcgkUADqkc3KyxYpDit8FjSlKQ2oqVg3VljLR4Pfp9AAw1UN_0bNYcvBf20bKO1a8VbGzpjJEYCneGdCYEozfWnE-7KP1vfAI9fZojDz-odBjWH72UWU0qf5t7q7d7gC9w81hnAEflT4s2rnZ4sqWkIbS3AEj0T4KhvKae8l0YYRurdzX274zFhBGCSPTrPHfSNI5JN15Rw2az3oM8JDOj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=BsZMa9Cai6lEM93KV3rFLtFITY7DK8eABT6-607QoIkh0xeYdbSuvkqEziBfUwNPgJabmfory_-6hFx3dmjFOFDFZbaXFjUrqvLyjRdAaBsYlAKVvvnwFtg9vJh3aQLEoPhqEBqQRGl4NSJ7Pjsa-00dvkEoCR_fWP5N5H3exBCOYTTkvGTJa6YPWlq0LPK5xNntMgafR8-eKdDYY6tFKMRxVqOXUovyOW3Kb40cfSYlsBDLD0nKxuFL_vK5hzy0girY0MIO9-ZJJgHoiGgqMjULCjW5FECupk0sW_4G-4lCqUK-nUf0YvyZh_wDKh2sF9RvPAKg5ioumlU930M3ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=BsZMa9Cai6lEM93KV3rFLtFITY7DK8eABT6-607QoIkh0xeYdbSuvkqEziBfUwNPgJabmfory_-6hFx3dmjFOFDFZbaXFjUrqvLyjRdAaBsYlAKVvvnwFtg9vJh3aQLEoPhqEBqQRGl4NSJ7Pjsa-00dvkEoCR_fWP5N5H3exBCOYTTkvGTJa6YPWlq0LPK5xNntMgafR8-eKdDYY6tFKMRxVqOXUovyOW3Kb40cfSYlsBDLD0nKxuFL_vK5hzy0girY0MIO9-ZJJgHoiGgqMjULCjW5FECupk0sW_4G-4lCqUK-nUf0YvyZh_wDKh2sF9RvPAKg5ioumlU930M3ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bikTnQGi8XS4_RVjrQtqktpD4_Ak4vanV-n8UtYQMhUMx_SPFGoa8uq6mq3-JK049J2ofaV4cqLKhMTn1kZYTdwSsWXNP92miZ2DHb3xWCWuii49EGIoDUi0eIklVNHjayjSwZI8fyv6DuCsStQ9nxQoyjdXaDW9g-hqCnJM3x5qFR2dW5zmdQ4IWJCyqROW7UlfPSMlLWHxQls8umTIBxFQxOxzIKxjzIS5QiUXfUIBDKasY251cvjJ013zv23qSbeshGv0V6UWOO6PSx0k3LRfS679TRnEdY34F_2fh7KaqOMX523obXBpiDD7dgJXfIP4PYXbWoHAxTUCWjnhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dud97-mbS__LGrF-brxiNWtsv_djxG_-SW_H-uJ8fK_FSD82SN6HLAI2orPvTDzVLk8E5yBxU-B09ODjcxviVfL9QM5D1tNVhnwqtl2vBQR-8v7ihieunXUjmPyg-1gll0T93amw2Z2ysizX-wnZ9ROmlnWSGoGJUhGaY_AMIB8I2kci1OK5l7-I7RFHyzu_yRTPlAJHXpTs8TpwHx-AqCDwLnAYJg4u8xXTy7fh0ArXhxTNz71sPTD1nAtxoFUsnj5j_wEsL1iqMbutjpxRdm5HVDZI8SEZUrgCewyRs5O9GquSmVIb9xzsyG1KtA_0LDM8RoqyX405eOpRbGlPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2oHLKJUTaGMSfwRriNkakX6RO9e6mUYxOVbs3SMHiINqDwEff-M55FlWeZMg8khAA8CZFB5PlgUZQc0UBfC9yJjZt14os2N-8Am0c1rZqKhcESNU0pTK15ov28YwG4ekpNeVT17_pU6ls5lElDYzVOr28dN2-WHTiQuQEDqphKysESRaN8i7dvhBwPsZRqF9WO8DMymJBf5GkDDnO_U2ogZgz5fe_lbT5OjBxH8cV0bd1oSxZ0nwAs0cXuliKI3ihAZqA96XpLwvPXiiqGF2Ld3jkITu3ep6Yf4dzJ7KcV7RJBFnYStsDb_iPjeS62hRhhNV9fxh723iqIZw1i8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRH_VvBvw45AvXzLVkjC_63C-XPBCaSlRNIakoAwspqCx7JKswWZyG6y4PphD-LNpw6eh5wx9CPhYa47z5EclgA2LcFRtl1f1uZpzFgPgRyKJ8xgQB3b_uF89reVIclx2Gg47Zcqam1AJkMWLFmZMkUSisI9f7T9QanRcdovkkJs1MjEsVZte8W2pklh81iYTRuBGydQ4-SJoRreY1yZYVw65yrGJHPgUxVq9QbeDDhALJ329yf9SbRCbO6_5-01UrfukvdG_FTl7dea86uq-Aa17zSfeJsLo0kodGPm0eNoHahxppAvorYQp3GXg33PL0OIGMF_C6zOn9MZSbohxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9esx7gygy0hMj7dQV3f_6i26jTIy55USoMbjZ6PP1sAETbY-kbnLWYtYdChf8S7V6bBelov9mosGoAM42-_I4XLX5pf26zCznpuNez8dr3cyVyI34QhR8_DrQ3L0d_PMFxW3DWChJxeNYFhWkmCjDvcYcQHxqolWpJuEyi4N0DyHQNIjU2egNqOJNPCQCBt4pvzku8J8VyIzxdGeYNPyB96ArDKtZNJo2sHZBNsQrEi3iKn7eH81Eo35pDUC79GuZ_NLVdam6znqANAlWd8VCcNF_EfH7drvNu2jsndj0-ccQbNCoD4xnf2M262uHzA-c6BMpAMb3UxL0YEdgw-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=M0KUnxoKxS2NB0ICIm75HdGGXqO2YvRruGYlFqaXT5c55GYn9kHR3ilW45DDMbcrK0UyUdZ-Hc_6yg7bYD-CzjzagzXOia4pryCq5jeWVuDCM6KavOMTpyuToS45svERKSUKFUmWgV8sotP4CEGfvTEcHuIemYy4k9axVqfv8Ayon8VE-fjShf3FQIoSs1EhrtFey5DqamihSquvOIUMJ7r--WezTDhjsAKhjvDw5JwTtrXIqMxHaktxBy9dxlYx-vXpNqJO1u4tFlO5pwO41Oj2dE4XPKJQr8qS5DcKLGProaYZWD_vyWGTWmD-AXgqiJ_waW8aoVgt1jKSAcxT_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=M0KUnxoKxS2NB0ICIm75HdGGXqO2YvRruGYlFqaXT5c55GYn9kHR3ilW45DDMbcrK0UyUdZ-Hc_6yg7bYD-CzjzagzXOia4pryCq5jeWVuDCM6KavOMTpyuToS45svERKSUKFUmWgV8sotP4CEGfvTEcHuIemYy4k9axVqfv8Ayon8VE-fjShf3FQIoSs1EhrtFey5DqamihSquvOIUMJ7r--WezTDhjsAKhjvDw5JwTtrXIqMxHaktxBy9dxlYx-vXpNqJO1u4tFlO5pwO41Oj2dE4XPKJQr8qS5DcKLGProaYZWD_vyWGTWmD-AXgqiJ_waW8aoVgt1jKSAcxT_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHpvxcTZ5TBVYDnGzA_P8KkIF4ICs-qviOAwlMpqmFgNKqvErwFViOSEJZorTCv3fvyWEjgUQx_UAk1rgShj-q8i6oouVyq4a5G9rNE2XBMpKznTLp_lVc8zGUvbesVEMHS7BU5E0pIXYiktZgrpLElnUaqYAf6qDdRYfjyfPy9uuXD82Ib1URy8k-o6X6mGytniroWF2-TSFa83V0ZU8-d5jWVn7SIEifvyFtX4xT-Y7bfIUg1tKg4vQv067a3Ah2KutRh1oJngHfKkmlrdjXOTt_QL9_lTTI34sgdQjBSRC5bQgXBtzvc877n6GEDDkBVlG1Vd6R1gqmqeUAEOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmpFuENz8o8J8Jk_uagCPBDgoc7gCj42J0BWiVZiqZle7q0d8A5-NsP2PIW7MUXzd2Kmm9ldNnulSBH8xgSNBJDwDwflwJo7EVocc0kuBXM_ZCcD9egjFSLEDn726AvE8GpqFlW6hqffaEHmGd_ACfrtQVHdGhufIncUiZIPgxGz7UhqoTO_cyInRIpJGjCIevxjCE853L9GCj_KYibQjbKbdrkcOZsdOXVD_QB3e0HEmUHY480E2is5JyBH2RlbAxnLgatn4iJ4A2EGdjEeD_6G4aHuG1tU3tOiaU3CgC_g2gDqkQOrmaKe7zPULDlJO0pa-vack4kuinfLD9yTPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeXIxdXcYDqEyrP2Uw0jSktUI-QjplNTDoGPmchCoMhbtioJjOtQDgj57EHUN_QDq6ORFFZPN_XVw6S5StRpuZKCfBL9ZpO27szRjy8VVos0BOM1vqJUZX5CUJp3skBxhc2sCARE_mWKfSeRJN7hdPllM7CQ1evtMWRYvW4SkASl6e9D8iQu15r9KAj249-WT8vQaqL7WBT0wL3fFS8ZbJ4HTqyy-w1eVBy1dmN8lNiuCN--h6LT7Vqywec25eeiaZSNRVnA0S2vAv9YP2VtNfVhLlK4MypHPV8-OVqonQ5dVqoCiqdXdMLIJBBaMDe1XUwlb2tGyhRTeaWWhzpVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7CYfQl81KdXoEtBnbqAi6-FA-MyajBJU6-m6wOh2m7lw--Ebf2Guvf7eHeuNO9wBoCIUQ9LFXsIIh_wMApVMM1phhI9FM7962iTMkL8aHhvqKwUFk5fSXnjbxgR7V95IBAYt2327vAzs52Zzd8qXbT6q3qi1h5JOjG-0efbdvdvLGZn1gZWHSq76qrwRXm4Av9LUZMYxBzxuG1EwwObCICh5eVO3E9CRED9M3Yo8GiCEBZkS7WdGyjsreIdVHd6m5GoZ6FGKvGbdTSWMK9uD_KDaJ6JX08RaZzFXVtP9CuPPlQlYYFBaTjGQU0Z_dGRodsig0CDsZsKwaMsfXvMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiS3BWEEVAIhJYBFYQZYHYEaSbc9PSh7mb_42Y8B45fMVHWNHpCP3CUvyYjeLuM6U7_slIG8C8dhehizBt0KLmfj9ZlVGOo8BU3Ug13r92yTlxxY9H0ZaJe577s_vfyah8LSTZH5iz51ieSTQ8kEHxEam2VqlTJRcNGXiPOhodE_vr9JAYKW5vK0YuyujVE5px2FdywIR7ChndoaXdiSuSd0xn4hTbpZliSfB99m2ApYHjlRjd26pMyrbUKUA8PsG9A7kffAPpLTUPh4XsFCGbE8Eds-Bb5XkOxaoidy2DwDNtBup1i9dMIOyVl766rmi5zBAEVvq4VveVdKqK6CFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5z4ttppgU1e-_t3JgYGdSm16-KH4ah5vWo0ifyh2hmcDZ16QsSV707prQ5_YQFrHZ0PvBe3W_XejSk-JDPJY3CaBXK2Y0yc5M7M9Rps2uQVBJUA2jbZhtVaBPUh1AH2MDhfKA5vdQtRF75HCKgNGAAO8W3PX08FAQnf6n7Kt8sAP_jZY4qaSoTie3UtFcvqqA0j_hyQYQTe6EG-IWnuMb-oIx_HFp6JTcD4zTyXfo3kyt31rM1ji2xxkJJ4TYMeVMV_lJ5EdO_C3woSP0gWaLIyFlbxvGhGSNuiy84AxVceUoejo090MzVwadlK2vE5Lvam5VtMsR8CfoV8bf8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=gBCZXwjcHfycXFlw-SCTHgJwgzhBmEaVGJMZLMgBAjbVKB8OHPsSE6pIxtIKt9THtpTlyurajXyrgx-wBQPR3BxS9QRJu-jKtVNzo0OVIsNSTZQVBkVnfxeLVcG1ACzE78CxqMpDKYvvfvhz1KG0OYJtXX1lwQ_qgYqH9mM3dNzHkFjFCQo3WGdn2XtYWhc3XPATq86FyvJDbxMJ7gmdVxYagD0HT5aQ_bCRu3XVDLAbgMM8To7vso3iCIWzmwL5GwpC-XEzW9ICqrmNyCOflitsU2PigKhHs3GoO__GEI3fik4Glbz-gBVuiOP0i2p1E3bpRyRRFS1bCFj6wp3HGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=gBCZXwjcHfycXFlw-SCTHgJwgzhBmEaVGJMZLMgBAjbVKB8OHPsSE6pIxtIKt9THtpTlyurajXyrgx-wBQPR3BxS9QRJu-jKtVNzo0OVIsNSTZQVBkVnfxeLVcG1ACzE78CxqMpDKYvvfvhz1KG0OYJtXX1lwQ_qgYqH9mM3dNzHkFjFCQo3WGdn2XtYWhc3XPATq86FyvJDbxMJ7gmdVxYagD0HT5aQ_bCRu3XVDLAbgMM8To7vso3iCIWzmwL5GwpC-XEzW9ICqrmNyCOflitsU2PigKhHs3GoO__GEI3fik4Glbz-gBVuiOP0i2p1E3bpRyRRFS1bCFj6wp3HGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=PvibRSf88fYBFXfTuVOZaPdMGYgnvIuKOqRm-deEfUdrF9Z9AHCBjZs3ZsFv71EotQ1jTnqrOgJ_E_yPyUzb6lE8-zaK7Ey7mPMAjTCs5DPKaca4y9wM9Z6XLMFt65hTthtRReVXZnmJQiFxicUu8W2uWvumHShnvPO0saJqCPG2Wfk-zcL7YlmgR4mG-5gRTzsWRYij8z3Kzb_tgh7Wt86YPZLTRGG7MCKRkJ4i-7q9V_kHkAg9i-tjbttSOf-RyZ_bwd_Om_TnVvjsW5wx13DRhddouOxyitHU7xqhEQ9KN053W5GCH7QTgdecplyVPRYRIkKlR1_khFnHEJZFuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=PvibRSf88fYBFXfTuVOZaPdMGYgnvIuKOqRm-deEfUdrF9Z9AHCBjZs3ZsFv71EotQ1jTnqrOgJ_E_yPyUzb6lE8-zaK7Ey7mPMAjTCs5DPKaca4y9wM9Z6XLMFt65hTthtRReVXZnmJQiFxicUu8W2uWvumHShnvPO0saJqCPG2Wfk-zcL7YlmgR4mG-5gRTzsWRYij8z3Kzb_tgh7Wt86YPZLTRGG7MCKRkJ4i-7q9V_kHkAg9i-tjbttSOf-RyZ_bwd_Om_TnVvjsW5wx13DRhddouOxyitHU7xqhEQ9KN053W5GCH7QTgdecplyVPRYRIkKlR1_khFnHEJZFuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrJ0gV5DVxgxdAT3wzYGFL4laRr9hOfEbXa7LQXUUMoPPol86mziHG0IerrLmid1nEy78yvBrzbYoPLcuxZrB0dQEYxCxCQFBOD7S94sZfEIzP2N_UmueS2UFVzKTicQjHQCKspJfC9Fy-lJTALdJZztcUYrgxCIFcSrwoWGz5_PIaoq6aLaXakgQNt5mrwp0i-dILCyy53nyb7TVZ0TFJN2aLsMldouoHkm-uZt_Af0Tq4y8ZQN6O3ZBE73AzbgvwZzp99I-FyXR-awTBTCM0Kk7Hfs8ynwWYaNUiLx5uvPb9QI85WEb7_uhVPOki_IuSY1XExubsDhWjhXAtyNBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=sntQb-PxN0aAcvSmTR66ifjWlsfLuGjigemgHpyicoL-9VsIIWtkn4J3KMtOylz4yiBNiVwowSwAPmClmvGcH5SYtBMzAhrTRWwbnRqVAjoUHqkAqkfqXIZELuIcJBMo_9SNsMpTKAN4zYF4djBa3Qly8PCU2NYIPyOP5Bz4iyM7HglXsMshtZ1xrg1SDgPEysRPU4vvqAl1QAuUFKTg7OrRWnBcbjpvGO05n89dI95_UgbbK47abZ43xg10UH77EFzwVFAsH-hdIbZs4mGw8Uc1pj6zEXtV29f-UyqWdS-YAwQsjCSmPNbaYc8hfcZFQJ7kZG1FvCrjVP6eDdb2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=sntQb-PxN0aAcvSmTR66ifjWlsfLuGjigemgHpyicoL-9VsIIWtkn4J3KMtOylz4yiBNiVwowSwAPmClmvGcH5SYtBMzAhrTRWwbnRqVAjoUHqkAqkfqXIZELuIcJBMo_9SNsMpTKAN4zYF4djBa3Qly8PCU2NYIPyOP5Bz4iyM7HglXsMshtZ1xrg1SDgPEysRPU4vvqAl1QAuUFKTg7OrRWnBcbjpvGO05n89dI95_UgbbK47abZ43xg10UH77EFzwVFAsH-hdIbZs4mGw8Uc1pj6zEXtV29f-UyqWdS-YAwQsjCSmPNbaYc8hfcZFQJ7kZG1FvCrjVP6eDdb2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=PQWnmxEOXPG6_hmsfuvmceMgNvu7CuKtG5EfJyScdg5odqKZ5Gdz_0gScr2uOl9gWcKOWjnDtj8caiBYYQMxw_4CfXwg7J-k1IuGnXR6CHYcj9r2bZR7MZXmTpaej9UN4_l2eq0xDcIFCyqV86n4xXoBKPFHKIgBCdrDIAXsvH7eFLvf1cKEgnzQ1PLueHTfeaDocjxFDKHsEDRFEAVrcsAodmJ5YwH3Wj-2pQ_lZQ15W3AKO1KvdqJF_dEUASfL5pYHcm2HPBQZNcRAYjjqPvVIK_FI59Dk0YQbs5_8V2w1Ukn_XbUEXjkJ_jdbSfJoMwvIQJT23ZO62-H5ofun6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=PQWnmxEOXPG6_hmsfuvmceMgNvu7CuKtG5EfJyScdg5odqKZ5Gdz_0gScr2uOl9gWcKOWjnDtj8caiBYYQMxw_4CfXwg7J-k1IuGnXR6CHYcj9r2bZR7MZXmTpaej9UN4_l2eq0xDcIFCyqV86n4xXoBKPFHKIgBCdrDIAXsvH7eFLvf1cKEgnzQ1PLueHTfeaDocjxFDKHsEDRFEAVrcsAodmJ5YwH3Wj-2pQ_lZQ15W3AKO1KvdqJF_dEUASfL5pYHcm2HPBQZNcRAYjjqPvVIK_FI59Dk0YQbs5_8V2w1Ukn_XbUEXjkJ_jdbSfJoMwvIQJT23ZO62-H5ofun6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=MI7nTQIh4uvo7RIrVcAdv-nM8P5Hx4PDpLvZufQJ_vKkTkDDAEKxM8ut-2hShnTtXxVNcSMX0lKoQt4q15vjITDuislFx_lsUgcy37SjiR9lm3sIRq_EnA-c3RqZnJljg0iVqJEyCGOVVF89Z0jdToecENl5C0hEb09it_HhQE31Ts7d9tLv8IxBs8gmrbcLswqKc6ZL5q2tOQuXnicVv-lYkm1I2YbeRsZmMGMfFXvjh7J9nPsnRJk69LW5uFTCjeGdBbYEJu9VBjPokUc6JWNAfmcrBc0K22-4TfYaWGmtpW7_LpNXm5E7vz7XUt_fhUpmkmlMoolrrCRbDvPoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=MI7nTQIh4uvo7RIrVcAdv-nM8P5Hx4PDpLvZufQJ_vKkTkDDAEKxM8ut-2hShnTtXxVNcSMX0lKoQt4q15vjITDuislFx_lsUgcy37SjiR9lm3sIRq_EnA-c3RqZnJljg0iVqJEyCGOVVF89Z0jdToecENl5C0hEb09it_HhQE31Ts7d9tLv8IxBs8gmrbcLswqKc6ZL5q2tOQuXnicVv-lYkm1I2YbeRsZmMGMfFXvjh7J9nPsnRJk69LW5uFTCjeGdBbYEJu9VBjPokUc6JWNAfmcrBc0K22-4TfYaWGmtpW7_LpNXm5E7vz7XUt_fhUpmkmlMoolrrCRbDvPoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=EiagJZi_GgvRzRdmxi_Z7sT-Y6u8-sPeAAYG9MA4xRLfHLZLLeP_N983wdKYPsu57r5ifRgQImKQIP3Lqu3ofX4TkbIex4OwGgT-rNdzFtq0zzxReBp_DMYbiaRfzOZ4ipDOc43VjGCO_LEIV81IgyvBQFznWkvhc4UnRIWHdrystbqhmly0R-CXsj_Q-FN4kRL4snHMk9wYcG6BkoHeAo2lF3rAGX1af_IIRk_uUpGZstmGUTnt0zAuoSlfndMgY2q3VT6GEf5Bjm6ldbuLtmtHvpdca9Yy6KPMMdIwkXfdju5L9_g_kEkLdWThWsmKBC5RtWqVyvmOw-7MaCMJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=EiagJZi_GgvRzRdmxi_Z7sT-Y6u8-sPeAAYG9MA4xRLfHLZLLeP_N983wdKYPsu57r5ifRgQImKQIP3Lqu3ofX4TkbIex4OwGgT-rNdzFtq0zzxReBp_DMYbiaRfzOZ4ipDOc43VjGCO_LEIV81IgyvBQFznWkvhc4UnRIWHdrystbqhmly0R-CXsj_Q-FN4kRL4snHMk9wYcG6BkoHeAo2lF3rAGX1af_IIRk_uUpGZstmGUTnt0zAuoSlfndMgY2q3VT6GEf5Bjm6ldbuLtmtHvpdca9Yy6KPMMdIwkXfdju5L9_g_kEkLdWThWsmKBC5RtWqVyvmOw-7MaCMJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
