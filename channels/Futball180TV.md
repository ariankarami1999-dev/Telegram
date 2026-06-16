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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 600K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-93631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe2321092.mp4?token=ByvfqKe4otftZBMlhPBmWD9MNHIC9BCUB-eSojsyMsJLvkYy_dydq9yk8_W8Kcid1jZrC6OxeEmpFpTpR3NtJP_gIh29LZdPtfS7XDmSLT2RcGdQOPTApqx7Ywuvliq4R__NjJ1fnckgCkS8Y06bhgPq_NfAuiXaacD8jYDKs5wJJm6iuWrwJqhKUxdCFwTE8-W8fZyLFGuBtEcya5x7rAp1UAr6gaYTYYWN5ext6zeeXZd1UNtIRYnYZH5PeO1IklDfwF8TlmhrFU2ntl-oDes2AbGSAsA3gMWnaAmoh6xnCZKg_MsHcyylr0lQU3OrvdGdnkxlC9CF_v7P12kVmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe2321092.mp4?token=ByvfqKe4otftZBMlhPBmWD9MNHIC9BCUB-eSojsyMsJLvkYy_dydq9yk8_W8Kcid1jZrC6OxeEmpFpTpR3NtJP_gIh29LZdPtfS7XDmSLT2RcGdQOPTApqx7Ywuvliq4R__NjJ1fnckgCkS8Y06bhgPq_NfAuiXaacD8jYDKs5wJJm6iuWrwJqhKUxdCFwTE8-W8fZyLFGuBtEcya5x7rAp1UAr6gaYTYYWN5ext6zeeXZd1UNtIRYnYZH5PeO1IklDfwF8TlmhrFU2ntl-oDes2AbGSAsA3gMWnaAmoh6xnCZKg_MsHcyylr0lQU3OrvdGdnkxlC9CF_v7P12kVmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
تلفظ صحیح اسم چند تا از بازیکنای پرتغال به گفته خودشون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93631" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93630" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93630" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV3fPQBJ8lxOGAumtw0sga25Vd9LRZcgYxwxTS0e6fKLH_9fRqpNmr6vi8qg_yJYwtnyed0Wq3cS6ym1yz-l1tOdzh3EiYgFpwAylhikkNgzaSkuCxtZljoyJpC13cifloFXV6fNN7cOFsQT1SnoRPhwAatdx2IimFB-jRcTSqbzuqv7SHL5bLBt6j0PY6OhUBYKvsGxJlHK4J0DsOASBpHd8U5wynxJ609HLLGXp5e2YFWnw_BgS_hbO3W3wkC347-nGskJxHCAUSpTi463pMge8SBg-WfGajxlmouuEhiYLKvRxhqrdq4363QrJKYyJXj2MlvNhIy4vMoQkiREoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93629" target="_blank">📅 16:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qeKz5jCAhq00XYTlmRuwo94UnsiJpEdPGdyDe8eDAia0etBv9iXIzmoAgYgRGpBXIaTaUn9Rk_4YzoByFNeD_Oa1pbHo7HTtdO_zN_khRi9COs5hQ_dlsxT8kdPKtptUrg-7f7dyvkPRwKtKl9IGPvY6C-6J6ZZWc3J_c0h6MD4S8vhsNyLmJywXmx8Sj9HtJxKVwZqU1ecFIm4GI6_E6tFzFFCogLEn_3StgHzXmmQaGR32_v8dE_nMMqNSSwUMFGzdGpXSt9m8T5K08tZrkiIZoba9A1hi-UMtLyLNs8zfldkVRbs_vx0wWu10s4QZcQ3TJA1Q-3QupePbgCbFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2SG60999SPYHrnwSzCuE4anr0ifscrC44kbtho7ZMGsG_DoUAioHEmjT778zNauY96L5acO0hNvBRSZqXOtfpm_ImHwcswodNLFwbj8SLHGL2nxXVLG_30Cjvh8nConLqBIE7BSuXr1saQRebfvZxXqXyInHz8wJ2Qx1-xMQ8ja0nKZ6xmOziI3MRlgEBTmCaXGTlkfetAQjZmNaY56DP9anD1JCr6x7M6vtHYVlMFkeZ3H3SdpElWJlGjhaNIehYzUrYyYjob1isDWD_jKPSLSUMTTqdHg_MSKEhkG6C4b47X1g959nOUk5FJ3Ot3g4bnG6-TsNrpxXinbTDELoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4AOBYV_YHVMIMK9xIQOXxyJEqmchkV0hpLiZuudGGUnSdScWgbRzYzitBnOvmHj7c8gkdwL8VpyhdgRmiCagg4qD53KDfkbB3MlBC5y2Y1VdtKVXEV-4FOai_RuYkZ1xyUub47RTH_7vHTVk7s3ZeX09rYP48OuLiC8M1CCdUPuLRV9mBNa6vKQ9JgMtdYQaeJnJkNfC7QPYyJk6nIDT__TQCn1HohoD-x1h1Gjarp3nbtqdIfe-Jyh8w0ClHDzmQIgfbAjdaWNNZqvRmVxFcrM3klVRUirXGmMhoVM2XBg2bluXpKrF3R9VpMtHAyn6Z8j0AISZ_XXcS4oprHwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9O9YZvO4F4N_McckXaWxue_GOXBdpfpxc1WPI8-FMd3TytF4j3BrQoGD_AtG8XAkHjFQoWV9362DUdENTYZv-37oljFK4GLoxu20B3lR3_8sVoulffP1W2HpRj3HxVl6wN5y5IT0ufdVgpZtMOP3GYY-cIfDfWH2vgIno4tniLPvXKpcCtBAJynzbSo3Ty8OT7i-RxPNjEF_Ej1R1BJtLzVmnY_jmn9jEVJhZ7zxGlvTFCRyHl7RT_5vh4jT5M_BdBJsDa7v-IGa3tIBhZU107t72jVEtrA23h6odSiEvrIAZTiOg0DsQYNUDM-yuETWfof2MMqhSota4fmFx1VSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق خودم کیت هرینگتون دل‌ها (جان اسنو) بازی مراکش و برزیل تو استادیوم دیده شده.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/Futball180TV/93624" target="_blank">📅 16:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51044e08bd.mp4?token=PlHL_V2_eJyUr7y1OQhFypvpe4pn_joyOVA_PVu7YQ7sigPi5gjotPV91G5zgA9ABeXwwYGgMt7hkZikjNQuHXo47GnDelz9NMKY-NAMltBpqhUUExjH_4HkPR2DjS74lcwC9N9CSf7sJomYwBfFFxS6_RW1VoCUwgiPKOKnrpgIbzKaltacxop8uPmDm9Mf58uN105MMH9Mwrx4_E2_5M5oXb4UTNHLJLemt_ZxQuq3nQ6IeRZF_5GVl8jBtFJBmoowKExRNUXXrZ40XHaWyauJyXPzfRQjfYuVsV3_8wtaw559UTw5n80mCFcdt8fPvziKUakGQdEUopzKMCQr-jX2wosAi4CSMDEYFM3bYhQaNWpJlaUJAF8n8jVorzD4LPsT50zKstQKMVQ8EbNU1anEr4pptCConhyVF56J9IjIk3JHhZU3HGGtuW1-4TkII7OPQ5YAasQJVDVMJEXgq-1MNig_eU8r2tHFlyT6vnO8fDzM3iz2b7ePSocbyGhJho4rWtq9L3RRmul3vx5fmvWVOZBY3rfeGfGb93t0bBtC-8c_IpYq2X_F6eA33OKtzIuqwOcbb5EAVVqxFeJN4JKRX3sKNMLYESgj26pcjg-3oStnsJax_VpuOFyHdnf7ZTjUI-kMn5EjysGlHth2zHeXvQYCRP1sQk827yReiD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51044e08bd.mp4?token=PlHL_V2_eJyUr7y1OQhFypvpe4pn_joyOVA_PVu7YQ7sigPi5gjotPV91G5zgA9ABeXwwYGgMt7hkZikjNQuHXo47GnDelz9NMKY-NAMltBpqhUUExjH_4HkPR2DjS74lcwC9N9CSf7sJomYwBfFFxS6_RW1VoCUwgiPKOKnrpgIbzKaltacxop8uPmDm9Mf58uN105MMH9Mwrx4_E2_5M5oXb4UTNHLJLemt_ZxQuq3nQ6IeRZF_5GVl8jBtFJBmoowKExRNUXXrZ40XHaWyauJyXPzfRQjfYuVsV3_8wtaw559UTw5n80mCFcdt8fPvziKUakGQdEUopzKMCQr-jX2wosAi4CSMDEYFM3bYhQaNWpJlaUJAF8n8jVorzD4LPsT50zKstQKMVQ8EbNU1anEr4pptCConhyVF56J9IjIk3JHhZU3HGGtuW1-4TkII7OPQ5YAasQJVDVMJEXgq-1MNig_eU8r2tHFlyT6vnO8fDzM3iz2b7ePSocbyGhJho4rWtq9L3RRmul3vx5fmvWVOZBY3rfeGfGb93t0bBtC-8c_IpYq2X_F6eA33OKtzIuqwOcbb5EAVVqxFeJN4JKRX3sKNMLYESgj26pcjg-3oStnsJax_VpuOFyHdnf7ZTjUI-kMn5EjysGlHth2zHeXvQYCRP1sQk827yReiD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عذرخواهی ابوطالب حسینی از علی اکبری بابت قضیه توله‌شیر معروف این شخص
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/93623" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP6HGutUg3dAnLgD5-aPJzECWKtsgdPsUWNgf5nk_Xlw7uEit0P6RpajI2eE-96Jpl_VDkYz1okSm1AqURjZoFZ-GLwBNmNThHiA_MEDgFFEDG7NlG0YjayBXjUSRpDf8l4kv0F537VWzq-okDc90BN_AzJ3jcNxd7ffaWc2LHs7OkmuRvob-CCJ98wQ2wOZmtBJskJjEPhHQfTvjwNQPSfXMDFgWNJaYwgROIDMgDMKDolksLuqJ0FHrtWo2anlaOKi0Dv4qrIvZaaJLcAo8HYTVXQaQmdQ6BfPY29vPplLUk8CxM2eVLmfl7L6rcVVD-gUJiPllxdici3Sipa44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی عشقتون هم دیشب تو استادیوم بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/93622" target="_blank">📅 16:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coHQ6vgJHMJNo6adK_ERwUwEm8rc46JZxMxQLHuNAik9V4H-0N9WjqEJZjnioUyjEORyCGoAzo5iB-UNaVP1Nw6RvEZJy72YE219CjqyYgEi-cnDRJ3S6b3tki6oprydX_ARSwZLNkFiBeDPk1EbjiIKCaBlbM177OLRmgdbvlq7G-0mnC3gHtelmr7QE0RCEO8u9silyBf3jAI-tuDCYXk6SElMz7VYcdcGzgqAJAt7I9_qgqpUys_IWqJ8x2MbWrXvj_KialFIStz_NUN6oOXZ3TNh5wfVBGm9rPqqlGPfX1ceNF_vvwM-qA4GFAHS739sy3dXNTCoVri8wbGc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
گلوبو برزیل:
الهلال قصد جذب رافینیا رو داره و میخواد شانسشو برای جذب این بازیکن امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/93621" target="_blank">📅 16:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9081fb593.mp4?token=V_ho4aezVGrW7_ASPVLC1gBh-znOGEeXACC80qo7t3nCsobqRIGbwIcz5_ywCJiUPPmj7jIyvWsjCQsKooZRXS-j5Lmc2puobcrx1hqRobP1ExlIeSs8MbJW8Ilj4bE6mls42qSCx2xRuCdCkoiF1OVKjKW300r7fwVJbLV9nzUyfb9Yt2ZjnfSSGy3trTpqMZsL2RD53WKKcfrp2OWI8zaiCED1y_M7XQfMyKFTqO_l5dkx-G6xSrbI98ada9gQfXYGaiSa6-wsqD2jnYRjP9O8FiYFCRcGyrwd15wnoibCSifsCxM1n8i5A98JsYrNS43UqF27EKLlpBbqwVlZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9081fb593.mp4?token=V_ho4aezVGrW7_ASPVLC1gBh-znOGEeXACC80qo7t3nCsobqRIGbwIcz5_ywCJiUPPmj7jIyvWsjCQsKooZRXS-j5Lmc2puobcrx1hqRobP1ExlIeSs8MbJW8Ilj4bE6mls42qSCx2xRuCdCkoiF1OVKjKW300r7fwVJbLV9nzUyfb9Yt2ZjnfSSGy3trTpqMZsL2RD53WKKcfrp2OWI8zaiCED1y_M7XQfMyKFTqO_l5dkx-G6xSrbI98ada9gQfXYGaiSa6-wsqD2jnYRjP9O8FiYFCRcGyrwd15wnoibCSifsCxM1n8i5A98JsYrNS43UqF27EKLlpBbqwVlZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ابوطالب‌حسینی این‌شکلی از برزیلی‌ها تعریف میکنه. ناموسا عالی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/93620" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54665bfac3.mp4?token=suGPRq2dGmnVplbVGhSQqVX_SYWgzwEnE2csjgny2iemxYTXBc1bgbcUnvygoNfryFuvsyo9emXkKfWXIEbF5FsIaVsb1AVbnOoio-HO_Rkn7zjG9oaTaNc7SUhcxIg1s3VLfGPj8yZnF06hPleParGuseq3apDbVyHWfjMdOba85um50aVtd7_nfRT_Zcx5TbUIE5ze0dy4uDdUNRm9gyWRtxVEwWuzsgSM0qSY57WEwt4yvW5_1zAl4iszq4BSR-UKNmFa6W7Nulrptit8c2s7Qx_DeIz1PG6E5W8O5xPTCdq6TseDLUa8Eg7PtMN_VCaEV_EaMjMmXeu278rN9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54665bfac3.mp4?token=suGPRq2dGmnVplbVGhSQqVX_SYWgzwEnE2csjgny2iemxYTXBc1bgbcUnvygoNfryFuvsyo9emXkKfWXIEbF5FsIaVsb1AVbnOoio-HO_Rkn7zjG9oaTaNc7SUhcxIg1s3VLfGPj8yZnF06hPleParGuseq3apDbVyHWfjMdOba85um50aVtd7_nfRT_Zcx5TbUIE5ze0dy4uDdUNRm9gyWRtxVEwWuzsgSM0qSY57WEwt4yvW5_1zAl4iszq4BSR-UKNmFa6W7Nulrptit8c2s7Qx_DeIz1PG6E5W8O5xPTCdq6TseDLUa8Eg7PtMN_VCaEV_EaMjMmXeu278rN9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
از داف‌های مراکشی حاضر در ایالات متحده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/93619" target="_blank">📅 16:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX88eZtw59D9prwSRXgqdboyAR0TzniCUTB21Ye2zyZm34ngrBeRuGL6FrBjUS3jZHk8miea3Tz7OUsyDUJf_8IdaF4O74mIia7R_2wcAgUXdHrb27_7BaT30z0Si90j8vRi9twX08A3lmUTLtbSH5dUObmOqgnVNCJaEpjf0YQLBg7oIS_kSMq3MNKqCeqL4343MArft2cul9oF0b6R4czIbqMBq8dD_gu17lRNHh8CIjkkSAP9oWoioe1Jqgtqr6Xi4nY_rmSBIMN_5cz4YH6qe2JRNAGrNKKigS4LqXTuj2BcCpklLJkUj3l4VHABuo2aYUgq68gGspGEkGbMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری - بیلد:
دورتموند برای فروش فلیکس انمچا در تابستون امسال، بیش از ۱۲۰ میلیون یورو میخواد. رئال مادرید هم یکی از مشتریان جدی این هافبک آلمانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/93618" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSk2r-kPclP1rnPK4cSTYwWAv0Qrx1oYFHTzX-QoLxJgdi-dlN5YhIU7rh0h2Nw8c9ccXQwY7oPnW7lpDbnHWKKQTIO6-uacwT1RNTXEWD6U7Zwq9KgCSTbv2tenQ9oA3f2TgfRgDN5iK1iUvoxYPyHG3i047w88Fss3hA7OVFXtWQZPQUOgzeYipV2Cn1DnkNwmpXej3vAhhrYU_irULu8iWd-0DGvaBZjlN46hKWsOtNant2oZ0niDQdeA2WkRgA2iaQ7zFOoE8LJmRKUVACZ_yI81vO6rzE8yGhcBDD9VrxHcyiqzJZTWhhpnUETOAZPb6HGiObywZGT5zYq-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های آسیایی همچنان در جام جهانی شکست‌ناپذیر موندن! فوتبال آسیا تا اینجای مسابقات حسابی قدرت‌نمایی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/93617" target="_blank">📅 15:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e6f229bd.mp4?token=IOijtUIkselSOdTYJIc3L9F3mQoA_DNJaS4rX8iVV9bBTzq0aunuFuaCXPJiCcOGlQax9EnOWsDGY2SwoLzRdrRWIUKgOktP9oio-m--_LuOi6h1a4lsB5RHIhFnX28aS91Rf4sUAyxOAkTmQBbwMWs8H_wqhM24AsG_hz2a1FaMjL_UgGvxJZHf7DTIb4Y8BxbJalK1zu5EnrnMOu_M40YccYNDSrc22pgJX8fa2iNEaGIElU9p98Z9RbrpYYiWHdW5Q1ZZGKokHt6LgFJ73NY-bFmugzu5B4cC4ic6HKfWnrI1KwBlN8h10LBYLpBnwlH8yfte3_dRvzQOTqxeUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e6f229bd.mp4?token=IOijtUIkselSOdTYJIc3L9F3mQoA_DNJaS4rX8iVV9bBTzq0aunuFuaCXPJiCcOGlQax9EnOWsDGY2SwoLzRdrRWIUKgOktP9oio-m--_LuOi6h1a4lsB5RHIhFnX28aS91Rf4sUAyxOAkTmQBbwMWs8H_wqhM24AsG_hz2a1FaMjL_UgGvxJZHf7DTIb4Y8BxbJalK1zu5EnrnMOu_M40YccYNDSrc22pgJX8fa2iNEaGIElU9p98Z9RbrpYYiWHdW5Q1ZZGKokHt6LgFJ73NY-bFmugzu5B4cC4ic6HKfWnrI1KwBlN8h10LBYLpBnwlH8yfte3_dRvzQOTqxeUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
با یه بچه تو شکم انصافا خوب چالش جام‌جهانی رو رفتتتت
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93616" target="_blank">📅 15:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3061863.mp4?token=PwSxnCbiMW3yN0_8CmSVs4_jpBQ5Qp7yAfEWsdHRRHIBU0QVuyfsp4Iv-ZmBtlE9XAgt92TH1kRLR5PcX05QQygze4DjkyOYyZpqrnoA8axZ7lQJVx7Jp_PFB2hcbyg0nX3ovBt3Z8pOywWSwXouilw6jdLFj6Faq2eWoL893bOyAlgZ1MSOMJkUFb2L7h7UXu9Y2E-w2jYatYOve0sWGx0dJOqtywSqn8Ua2H0Vb-WuWZE7ZXBrT2saH6LTeFnQ0gifj5oRMSkUVWMULVNlRwinaIvcTv9NndgBuIbuXMmMzpqOKjibwMone5qZrcUefyZOuNuy09lIprl1nm3U8od-2caDbwOt2Ida_FkMR4Q7svu79G8pfndEJpXynpnJFoDVqUhiOh3TISjnh_VJHpDFpXGU_5clYN5jECbZbRF-N-CrbnrolwMCV-razImkEm2hD2nZgK1l52hBnGiqVwLuIxHAIR0W4UTN435Z7mLSNeUJylI_5C_vu12w0xbkRWgldLgON2FCv3du08GPNts3AR_3aZ8tUqVp97WS11nZbIj-uAFrs3bkotqHeo0ZAafWANzI1MMd-LuGTXwM65dwtGhMNBPAygD7FYVidj6JeG5E5zFaRyiwPp0yJFyLpDhbmkjeLvACAP3fWeTddrPLJE6ws9-MdrBndVJ7r7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3061863.mp4?token=PwSxnCbiMW3yN0_8CmSVs4_jpBQ5Qp7yAfEWsdHRRHIBU0QVuyfsp4Iv-ZmBtlE9XAgt92TH1kRLR5PcX05QQygze4DjkyOYyZpqrnoA8axZ7lQJVx7Jp_PFB2hcbyg0nX3ovBt3Z8pOywWSwXouilw6jdLFj6Faq2eWoL893bOyAlgZ1MSOMJkUFb2L7h7UXu9Y2E-w2jYatYOve0sWGx0dJOqtywSqn8Ua2H0Vb-WuWZE7ZXBrT2saH6LTeFnQ0gifj5oRMSkUVWMULVNlRwinaIvcTv9NndgBuIbuXMmMzpqOKjibwMone5qZrcUefyZOuNuy09lIprl1nm3U8od-2caDbwOt2Ida_FkMR4Q7svu79G8pfndEJpXynpnJFoDVqUhiOh3TISjnh_VJHpDFpXGU_5clYN5jECbZbRF-N-CrbnrolwMCV-razImkEm2hD2nZgK1l52hBnGiqVwLuIxHAIR0W4UTN435Z7mLSNeUJylI_5C_vu12w0xbkRWgldLgON2FCv3du08GPNts3AR_3aZ8tUqVp97WS11nZbIj-uAFrs3bkotqHeo0ZAafWANzI1MMd-LuGTXwM65dwtGhMNBPAygD7FYVidj6JeG5E5zFaRyiwPp0yJFyLpDhbmkjeLvACAP3fWeTddrPLJE6ws9-MdrBndVJ7r7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
یه‌کم دیگه ادامه دار بود این عروسک نماد‌ جام‌جهانی همون وسط لخت میشد و ادامه داستان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93615" target="_blank">📅 15:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybl8i8GA1tWjNqgytLcPa5Jj0ZMqNUFHPB6xZYXWfq_rbtfEEry3DKqB2E1JLJdj07_Zxzt_9-ozrhxQpn--fxo7SUL7JyOElouoSYkGWHv6YyIalUWtSS988wIXgr9Qj1SRi55KtX3jw3foJgZRopvps00gCWWY3k8vY4CftJbQlInJh-nrQvC0tCiFtVdtrcYYUuSsG2z89-onGuHRs67xDnfn0B5ZHllGluXOuCkSo_vdFaf7byOXd9jKDyJ_l3Ik80MKcYcGMYkObQv7gup32EJ_ZuJMC9Y-UB7U-qkHFnP1wcpcyh5oNvkPQ-ntn8sObBMaDyn31F0a1JptJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویتنی رایت قبلا هم به ایران سفر کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93614" target="_blank">📅 14:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhZeMUN_owuu9hkmK52GgQFPoIqN4kNPt62XMaDdBL18JHRqt40_rMLUAUfKs7LfwJFRB84bMKg0Eh7IMZVoFJhxAxfQSOCyZjn0aRZaWMQ7IoswO9pE2KxJWU4VJRXZGwcJ1XbDQvJ1L0sxjGNbzvDoOMHm_Q-0ID-ikBefU0udWZ3V9lq-NVY1m-j2e7KJUi0PblEIkpvREgJgsq0wzU8RbjQ35se9k2Wn-5EOp0xtLm5LBKfG8y8oI1t-nT6JJhfvEHWpRsNwtdX2kqR_Z06HwMMHUVHFqBbQlDibfEE6G9JPIxfTgcv0cIBd15f6u21yMrWPtqzm4ETdL6tbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇹🇷
در اتفاقی عجیب، شبکه TRT ترکیه، گزارشگر بازی ایران و نیوزیلند رو با ۳۰ سال سابقه بدلیل ارائه اطلاعات غلط به بینندگان حین پخش بازی، اخراج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93613" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os3XfUvVMf08GOapQ8wJDCR_1HSDmHK7R2YyfdRnQ-rk2xkbaNKmYZtYLk2OilPC-EAhEIIDQKMkjh0rWbzHdvy_cVT_-UMKxS5E0W4R32oEHyX1OhWZEEzEXcWVpMv11Rs3kQWdx1CDOHvv_erYaYuM3Lnp_nWJg5SYRVJYmvOn_J8ZQKZqbs0a-M8WICWBPiwSzR0g4Io9OCT1EG_JvROyNnalUlI4ytemqYmixa8T7tCYgEJrSx-Kg0FsggdIim8Y7KbcXmLIWthGaWGt08ag_Bd-2dBDVleugUqizu8rpjvsGMDmX6nLYk1_rnTRJbYdupcmIzAgKGyYaXk-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
📊
🏆
👏
در تحسین تیم گمنام و شگفتی‌ساز؛ کیپ‌ورد در بازی دیشب مقابل اسپانیا درحالی‌که مالکیت لاروخا ۷۴ درصد بود، تنها یک خطا در طول بازی انجام داد که رکورد کمترین میزان خطا در تاریخ جام‌جهانی را شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93612" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری؛ فدراسیون فوتبال ایران درحال رایزنی فشرده با فیفا برای صدور مجدد مجوز و ویزای نفرات ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93611" target="_blank">📅 14:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووووری؛ نشریه لکیپ فرانسه: دونالد ترامپ دستور مستقیم ابطال ویزای برخی از اعضای ایران از جمله ترابی و طارمی را صادر کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93610" target="_blank">📅 14:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTNu7Jy6CnF6sdzVTuN0FDulJCFbtpkJRTvaGi0fV0Z8X22V3hqj87iYZo8peNWnO82EGvU-S29nR8Bn0_1UHpz_ycxm8yGOy6UyZGE3xgJ1SI0Bh8gUGZZK9qBmtfzIBHg50NYhEUDI70LsIEmB_GNuaXrIVRjMnHhJDb9OB0f0_lmntur7tRFdUUK6be_YVdQU81D3uc8BSWqUpWDyphUzDLClldcDVILF-slARgLd3ZfQLAbG5I2sFOWV5QCSBCSh0zD42LWC-CYdd8iLU6WCRlCnk1mbrIbWVJ9LD20obm1yjJPYp6NQjDHMcJljvv_xq-31MbX1lHzHk25RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری؛ ایالات متحده ویزای مهدی ترابی را نیز باطل کرد. دلیل این تصمیم رفتار بازیکنان علیه حاکمیت ایالات متحده اعلام شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/93609" target="_blank">📅 14:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ بدلیل اظهارات دیشب طارمی، ایالات متحده ویزای این بازیکن را کنسل کرد و این بازیکن نمیتونه ایران رو مقابل بلژیک همراهی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93608" target="_blank">📅 14:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY4NeoyAc3rg7VxrXjFv5twE1tdEIxcu6qDrU7OXrkI0X87pWAFym_SLUF2mzTPhg4-r7mfgL3BJPGkrvMwux3-XuIATh5ISsCqYDDx-oLZrJSdzupPyRUbKoddkTbqxe_-Y4vWf7KaP7Ld35is5yf-dYHGu3uXvUAlSgH3TW9HIv6iIH8J2CLx2T0j4qoxjLNvXw0ZT1DGJReCGWonE7Fasj8B_DJKbdezA9PzqpV2IPlKY_A4Amc7GWC-rwASAUsvo7BDBS4BgtmpXKJ7WMxI2n1Eilv4Zke4RhsAE_qrAKgU0vanhRJcnipexxh75CgmWpzDDQSkhtzxD9HW3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ بدلیل اظهارات دیشب طارمی، ایالات متحده ویزای این بازیکن را کنسل کرد و این بازیکن نمیتونه ایران رو مقابل بلژیک همراهی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/93607" target="_blank">📅 14:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01d8ca26c.mp4?token=E1cSnY0O2oJlpVBCUHtsbNLOPltc8VhA1Gj4fUmxfk2g74p0x8it0Ojne5n7MtvI__EEZICyJCfKkyc_PvOVZ2maL8vxOHvsub0SV9RD2ZlSNZrp0QItNr8MaXdfcl2AI2-jzUBfZAe6mumyD1KBHNXyBUfGBtABmRycq6xgpbbPTlUZ7BY_Pn28-p4edXLx7pMhyx7SjOd69tPr3ruEtxPQ-c42cle7ngkRPV_jTfQOhjl-cUkjQTq462M3RPhom-zUM_EZ3EdjPMUYPmjGMERe2lmhIFY5UFIyMuFYH5dYsbbdcHxIpGaYctuNorKpBH5ak3BpcUy5TQTW35uL5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01d8ca26c.mp4?token=E1cSnY0O2oJlpVBCUHtsbNLOPltc8VhA1Gj4fUmxfk2g74p0x8it0Ojne5n7MtvI__EEZICyJCfKkyc_PvOVZ2maL8vxOHvsub0SV9RD2ZlSNZrp0QItNr8MaXdfcl2AI2-jzUBfZAe6mumyD1KBHNXyBUfGBtABmRycq6xgpbbPTlUZ7BY_Pn28-p4edXLx7pMhyx7SjOd69tPr3ruEtxPQ-c42cle7ngkRPV_jTfQOhjl-cUkjQTq462M3RPhom-zUM_EZ3EdjPMUYPmjGMERe2lmhIFY5UFIyMuFYH5dYsbbdcHxIpGaYctuNorKpBH5ak3BpcUy5TQTW35uL5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
هوادار جذاب عربستان خوشحال از کسب اولین امتیاز در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93606" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67027c74d2.mp4?token=XYWVD2xD_UNozinfCno0tZ-oSby1sDti1ZhMS1T2Inl20un8tiXjLAew8CK2HnQv_OQLgbZWykuCtT6uC2JhI79GGum53_8Jev7-6HaaIrk9paSpNtiiSEEDGa63zempsm_EMNNUZWhful9drwV3eNgwpbpDL4SntnDVrzt1_yCawFsGk2FyfRFNGuYCI0jxC-MVf5jKJ_myK0RPwzdiur-51PXpcM3Hcdure9zFsafeKiCj4CTm1Ap2YMOQosju5Wc8VLZErdMoXAOS87q1CxniIdZP-Sdd_logN-bS6c02vCgK3UN7ZNk69stAThH2npkdBk2RS1pKju1J6p0Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67027c74d2.mp4?token=XYWVD2xD_UNozinfCno0tZ-oSby1sDti1ZhMS1T2Inl20un8tiXjLAew8CK2HnQv_OQLgbZWykuCtT6uC2JhI79GGum53_8Jev7-6HaaIrk9paSpNtiiSEEDGa63zempsm_EMNNUZWhful9drwV3eNgwpbpDL4SntnDVrzt1_yCawFsGk2FyfRFNGuYCI0jxC-MVf5jKJ_myK0RPwzdiur-51PXpcM3Hcdure9zFsafeKiCj4CTm1Ap2YMOQosju5Wc8VLZErdMoXAOS87q1CxniIdZP-Sdd_logN-bS6c02vCgK3UN7ZNk69stAThH2npkdBk2RS1pKju1J6p0Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
خلق حماسه‌ای جدید از دکتر علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93605" target="_blank">📅 14:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=DFdWyL5WGvQWDyj0Aehr2noisQnunbIXhXxcT3_9FfntXHLhGhWPEZVAiFdceR8Yk4KKy2lsUUA16UYt58klo3bv3o_flJotZeAC0OhMN6B4pQ1ZyoNk_WpmCoYU4bWP5OA34bMXnbPeiIS0r9yOzgRHN60dHEAYaZZySYyELBFDZ3nRyIsnMGoMmv12g8y6dZWMUI39En1AaJP6dKu4w3csnI-1OHKvdludi-tlGYrF2t7zGRy9a-_kzcWxu6BanriMSdwEvaORc8QNq3hisbVrSdhF9zDYDbpcXutBc1yq9A35H05_fUgT3yZDX3VvY1DgTYgm_gWkrbglyBWz6QXvhrF-k7bOfs1zRpQdFJtWlvOWGG2qYsZGK3VhD7oyVsWjmPOzrHnH9ZiWStJabitJkR7TH0gxir91mMtC8JA_koaReUO_5nbl1vlYD5DJIJoNTeA2gsALlhePSziLBi8oURVonTZ657YZqXBC-vbK-IhvPet6mvo3maNnFMgxVqXXwOsrbbdVvtPhliRN9tiHpKJEvkHqcyW89XbGEE4tEr9RO1QpsdB893D1pB5qgZnHSlyIePswWI35T6IUqLTjEFUi27tF1RS-QD52OQf0zfN2HdUaMcDSYADnw8FYOrM73xgWGTB5aQtcmZbuEOy7-RXdIVU-MpxBiF2aE_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=DFdWyL5WGvQWDyj0Aehr2noisQnunbIXhXxcT3_9FfntXHLhGhWPEZVAiFdceR8Yk4KKy2lsUUA16UYt58klo3bv3o_flJotZeAC0OhMN6B4pQ1ZyoNk_WpmCoYU4bWP5OA34bMXnbPeiIS0r9yOzgRHN60dHEAYaZZySYyELBFDZ3nRyIsnMGoMmv12g8y6dZWMUI39En1AaJP6dKu4w3csnI-1OHKvdludi-tlGYrF2t7zGRy9a-_kzcWxu6BanriMSdwEvaORc8QNq3hisbVrSdhF9zDYDbpcXutBc1yq9A35H05_fUgT3yZDX3VvY1DgTYgm_gWkrbglyBWz6QXvhrF-k7bOfs1zRpQdFJtWlvOWGG2qYsZGK3VhD7oyVsWjmPOzrHnH9ZiWStJabitJkR7TH0gxir91mMtC8JA_koaReUO_5nbl1vlYD5DJIJoNTeA2gsALlhePSziLBi8oURVonTZ657YZqXBC-vbK-IhvPet6mvo3maNnFMgxVqXXwOsrbbdVvtPhliRN9tiHpKJEvkHqcyW89XbGEE4tEr9RO1QpsdB893D1pB5qgZnHSlyIePswWI35T6IUqLTjEFUi27tF1RS-QD52OQf0zfN2HdUaMcDSYADnw8FYOrM73xgWGTB5aQtcmZbuEOy7-RXdIVU-MpxBiF2aE_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر زیبایی از یادبود شهدای میناب در رختکن تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93604" target="_blank">📅 14:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93603" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8207116ca.mp4?token=FUpQbLxyD67Ftlhcpp37DQ31T25oEGMeELwjwYhHaQDkMDH14ivNakV_HQFHOWVw3ZkDgvI-9az8O8M_Dnc-uX1_qKGpmgjd83M-MQBmsyujMuvIWvSCRQBD1m9xoypGGm_q5HirM4d28Qtr7n4q7GaNTwJAVFmQ0GMZeuh-zrH6_kItFtKWHEh_UZb1HSOPK6KNbJxLA_ELt90ZLANPyTGlNe357mFQAydwJ7Hd5LN6JeX8U8CO7urKPJk-6hlOiL2Bo2y1QIdImjIOxckYgmtv4xVlrOZqIFNgDDjcjuFmX5ROK1nI8-h52lNA5RwE2Gpz_KGllcsf9qV5hnxgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8207116ca.mp4?token=FUpQbLxyD67Ftlhcpp37DQ31T25oEGMeELwjwYhHaQDkMDH14ivNakV_HQFHOWVw3ZkDgvI-9az8O8M_Dnc-uX1_qKGpmgjd83M-MQBmsyujMuvIWvSCRQBD1m9xoypGGm_q5HirM4d28Qtr7n4q7GaNTwJAVFmQ0GMZeuh-zrH6_kItFtKWHEh_UZb1HSOPK6KNbJxLA_ELt90ZLANPyTGlNe357mFQAydwJ7Hd5LN6JeX8U8CO7urKPJk-6hlOiL2Bo2y1QIdImjIOxckYgmtv4xVlrOZqIFNgDDjcjuFmX5ROK1nI8-h52lNA5RwE2Gpz_KGllcsf9qV5hnxgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
کراش‌فوتبالی رویا میرعلمی بازیگر سینما:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93602" target="_blank">📅 14:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArjhEOVbhKPN4bUADeIhW5o9xcI43PdlZAEKLPvdQAhHLIVbhnJ3FDvwb2H1YJSpa0B4xKJN6kFjzL2Bbri4WuxfysfzORHfQH7JmcPbwz8QW2XModyN4Jdp9s2KYTUWJcRXhAMkMbRvQ1Wx1uySjaMzQIqGFs3U3BCxx406BhsYNc34VlviSrQOnETciHnBuebtvqllKNMSmRFwjkK7TqH79GyJbOR6zIEkzEfN2a_Tu1H3Tgovz-WPRIveUhb70hqQfQY-JWo1UBRq7d74DOOF-6ehNCVWLgu5hkY2oKKc0UBDcKEu5eC4ttFYzfep23xgJPs4nffLFFIyFoLmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تیمی از بازیکنایی که نذاشتن الی جاست و کریس وود هتریک گل و پاس گل بکنن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93601" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
❗️
گوشه‌ای از درگیری دیشب ایرانی‌ها در LA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93600" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/422fafe762.mp4?token=Csmc8eJjFFII9gBRPZw5juSYHGDMSQH2tiAd88eZDQnF9427rylIKk6tGB-aTAn1tkZyELaLsbJK571DbIOWhLSzdJ4xtE5nVSQy6kHyH9Q91ufCbqu5x2hp97M6PuY4oYRTsy2EWdxF8t55J0kVpJikGTFoiVlwrXHrR3VCWLGj-2kkO8A_9OX_BjMIJ128KitBgsphFL64uqbuUCH5ZUh0bh4k3XemIlUFy_4Zw5Rbx3gt4lAVkUAazbF-u7tj4MkeTjEHa6ZxMnCeF4aq1sUjFbx6FunutIY5VipAUkNFFNlLejpZ3l-yZvdT9ofKdmT0K_vigKjm2XmLQA3_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/422fafe762.mp4?token=Csmc8eJjFFII9gBRPZw5juSYHGDMSQH2tiAd88eZDQnF9427rylIKk6tGB-aTAn1tkZyELaLsbJK571DbIOWhLSzdJ4xtE5nVSQy6kHyH9Q91ufCbqu5x2hp97M6PuY4oYRTsy2EWdxF8t55J0kVpJikGTFoiVlwrXHrR3VCWLGj-2kkO8A_9OX_BjMIJ128KitBgsphFL64uqbuUCH5ZUh0bh4k3XemIlUFy_4Zw5Rbx3gt4lAVkUAazbF-u7tj4MkeTjEHa6ZxMnCeF4aq1sUjFbx6FunutIY5VipAUkNFFNlLejpZ3l-yZvdT9ofKdmT0K_vigKjm2XmLQA3_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
تشویق جانانه علیرضا بیرانوند در بازی دیشب؛ صداشو کم کنید درتون نره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/93599" target="_blank">📅 13:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-kShMDc2wUfd3XgimE12x-URLDAY__zLJM7VbW8GXwcJ-RSJ9wJxfn034BhIslwD3_1UzB-mIG0H8lJeIv4FEYRxJW8ibx4T6uc_mNtF1ZTzD_KWcTVFFCKKa5nAp45TsD--K9Bkqs4owES7sF5Qw4kO0yfFrlFt9kK1VCH0iSkUJM5Y_0Jiupp7TPcVX-yURDuWKIwfk2nYO8edyW0xtR1fKcaK9LImilo82VPP_j-3JKhEdKAMFWU3PQyjp13WeUJm542w2rG3S0d9V9yQbTEKJRoyFOfJie0JkBzYmQQZ-_BzXIBMZBcGBi5FTm7_HMIgCNmsOGx13Nfb2W9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
هوادار اتلتیکومادرید در پی‌توهین نژادپرستانه به وینیسیوس و با شکایت این بازیکن، امروز پس از چند هفته تحت‌تعقیب بودن، بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93598" target="_blank">📅 13:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpvCtgb8TUMX89xGHnDVRK2mV64pjXIUciLIK-O0uPdRj-7L7BMVZW6_1f8aigk7RLPBbqauQ2WYSRymuKguApE8wWx1HO_ZIQNWS12X6qSnkE4TwW9d_UlykSw8UskqyUbYQqVWkBB2lzLgFoIR0IdJCwRbgiMelHHlPjO_VHlB8dclahgmwwiNEgzXJ0-LrqyR3eOJZa3I-aYV1TG6KKqkdeq3BBi9qijmSfYl5BC5HTH_WQwTcReVsfykbG85JFAY68LHHzXUEIwpgfhDlWZDtNbXm-D395atLZMCn-ajflFBLy4FdHCUIPZrH_606px0W7BD9U5UFM9T1gKM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8piAo7xywJGVbtJpMjZyuEE1AMZNCuZgDh2WKJf0f5tzzslLW920tQiNBx9x53XxYLxYFe2vB_nAOiMfgDdk4s2IXNAc8vny0ASieAHBwaDsmpyIPTIza2MAwiRmHdbvMEEP1zaUPxNKI2JSx4RXRNxe8kypAysnWqybJNmfOwhbV1jFs4LCQFDz80phBCBrypXub6ob_yGwcIpdQl64OuabsZzvSXMa3cci99P297JVXQBAlw-0Ex0m7b-Sg0aK6P8uPlpoY0wYfULleLbPdOqbRV_ULWx2dd0hkVDIhifpBqUpCiK54oVoLFmuLL6u6uxUzsg03r__pEsEQ7wBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbaPu7rjOPKrL6tEvP8mHYZxafD8cClSZYM7T3Q313FQUFlrSZx7JIskUj3ZdGMneehYwYdK2I6HKk4lz2AhPvb-dC7RRXhT5q9woTJlgPu_DDdvQFF29et1YE0gAvD62SbhSOkvJBXJrTzzqxvmOqHoLP_1uezdwKKoNOvTN3_PIS_RFkyoVPG96Puy3Z4-74uQiH3Lmruq4jtzSk3kr8cUjWfx-C28I73hF77L3SeiswYnhxsPSNbyJjfXdwqPsFtxZWhcVOed2f8D8Ih89FuAZ1nDDoPSn9-PZ2YQLUqmM3A7w8HIIuiQuUohdjh-Lf_rol2ymAHdOugMtyLvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k95_j_i0inVsHSBMO0O_pP8JISdutbzgoC0DtZ5VmBrccAY7aDoc7PM5RRveotf0qlHY2Wib3LoPrbh7v7pe6rCJ_LUs7UFhIb3yuIKapI9URfy2Fzi1u4ka6RbujpmA4QDOyCUg3X6njcP7llDHuPMwXf-GvJI9Yqvu6AUKzbld7lM_nCa3-Uyiyld8Jxk4tRYPC8rLxU74Wl2H3jfgs4lMVV4xn1Wr9_KRMbaLfatIBedrVTq4agKcJja2mgL6Wl-26uqrAsMBKaJKXFC0cXCxWzzmX2P-RYQDP5Kpr3A6EpbLMOQ38KJx70nzVdPxKP9d6H12tc29Qml9MPnLNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب بانو ویتنی رایت پورن استار محبوب آمریکایی که اوقات خوبی رو برای جوانان وطن ساخته برای حمایت از تیم ملی تو استادیوم حضور داشته.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/93594" target="_blank">📅 13:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93593">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzKDY0VJNzy45ajfGWg6pMpinwpuTeCJPw5ZbUMqIpZiJF4PxDHcFegANBSDSHovE-LPFMoDDJLp9AHko8lMAo-qILS7o6Xo9HBwL5zUqre4Qh9I9XQg1jGDtqwq8LBhXRSH-4KapOPBsEMaPDLxc1pVZLSYQ87NXcrXtVwas2getcPtjmqyBvhKyYzye_JPB2zkpADzennY0h7560YlEWop5L8pfVCjWyJX-mxCpuVy52bvnll7TRacNsDv9naBCSYzpoBst8chC_yr6l2LjriGUQg5m2EPlDg14TG9XiyIkOagO4aSsIsYUrbaXTI0Qzp7CaNCiuMEjYDnG4f7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
◾️
آ اس:
چلسی به جذب آلوارو کارراس علاقه داره و رئال مادرید هم با فروشش مخالفتی نداره. از طرفی مورینیو هم مشکلی نمیبینه که فصل بعد مارک کوکوریا دفاع چپ اصلی تیم باشه و فران گارسیا یا آلوارو کارراس نقش ذخیره و جانشینش رو برعهده بگیرن.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93593" target="_blank">📅 13:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93592">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGIr4p96CJ_jlTK2yKoQgVsV3Ejc_bpmsEZr7e5Fm27aYjuhWzFCyUH4YEk2iVG1jGaUWFjwjYyJqMnJmON5PG5-Zjmb_MNBeR6d8S9xDqDUa8K-uY7eYkDjHPHIPxVGa1ey3X6enERckVmIA9KAyyvPupzrkMZdYXgz_Cf5PwBeYbrdP-W0ovt2S_v2jzuyRdwxpifNw4kDpAie1Fqsk_7KkWAqCVKUUlXABaw6f9Rp-UFpOjL57kFU0xF2sWnMpE76YLxMsbQo4k-n1UKjaLJzw_XVMbtk_UBD29GT1sp_HuAN9zBwFgI3HwwY5oRC92dFC3UUEyIxDpOXZG8kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
گییرمو اوچوا که تو بازی اول مکزیک هم حسابی درخشید اعلام کرد که این جام جهانی فعلی آخرین حضور او خواهد بود و پس از آن از بازی‌های ملی خداحافظی خواهد کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93592" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93591">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTrspxW1mUit_Kkjgt5kyzES8_baPN2nc13AuTS9vhQm1l-6V8qZGmyFy1CmHfbHybLKYjsPMBsukCg7ybzTL9UP5MN37Mqnokp_HxOVJIj32rH0AwIsaIyL7wuSZJbhMdlqlGaU4qnEtR3GAIlshbuAKlzWGk8fUI2K5OHXGkU2Z_PUYsY-Gn8mSKqCmnRhc4qxQ-sWVqMdm3i2ZciKL6CiIswSnbFC4IgV_syPyeeGsPvKuBBi7EzCsm2xbt2vw1m1VqMchTrkHtdPAhmqpitnPAobr0B0ERJ5q3TgFR5lWVpFnftFJzQUkltBOPDZZlUa4dlqSFi1A75dFCFfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
توپ لو رفته برای فینال جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93591" target="_blank">📅 12:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93590">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1eb0b0af4.mp4?token=Os9FzFp2l1RsTE74rInlHhSsLpdN06dk5RRcykjNeVfpRe-PFUZ-n2C13BISY7b4vonK_UIyxDxU3hhwQLIaovUs3IQgMREBAnAUs74AGJDYkh2iNxi_R6xyfy26OYTRDo_Xn_H00rDlvoVMNXdeMyKrMOzRVSiVLgfH8_I7fJJn6dwgNWVWGYhLkWvZrIc_TpI6k9l0pzK6PzuyDiRDTnTTUP4-fnBjEQwy332Su5ljlIAjrLekFHvRTA6LwCbPeqVuORSLf4xmGkhyAQJNxktyGLYESR0nzz1VGFDLAMFqTC8-A5E9tHzBHIyLWBBEtcJUTAs6MByjXtFweMk0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1eb0b0af4.mp4?token=Os9FzFp2l1RsTE74rInlHhSsLpdN06dk5RRcykjNeVfpRe-PFUZ-n2C13BISY7b4vonK_UIyxDxU3hhwQLIaovUs3IQgMREBAnAUs74AGJDYkh2iNxi_R6xyfy26OYTRDo_Xn_H00rDlvoVMNXdeMyKrMOzRVSiVLgfH8_I7fJJn6dwgNWVWGYhLkWvZrIc_TpI6k9l0pzK6PzuyDiRDTnTTUP4-fnBjEQwy332Su5ljlIAjrLekFHvRTA6LwCbPeqVuORSLf4xmGkhyAQJNxktyGLYESR0nzz1VGFDLAMFqTC8-A5E9tHzBHIyLWBBEtcJUTAs6MByjXtFweMk0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
خار خلاقیتو این برزیلی‌ها گاییدن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/93590" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjrjnhkft1P7crMAo7gRSZRRtD8QTM0H5ETY-5O4qCExvG6j3tbD0toR3DUFJBKudcDU3lV662nDlJwapc92ZWyS7zlr35jxeiy98yBipmTitCJpd8U4e6S1f-1JVW4zz2b9rdArOia71revhXE5C56tupG3CBEUydL-jfmJAC2AuAPfLDO277M_p2PvwN9Z7Qlyu8PzJK6Kj3pgcNkmauBw0v7l7hVMe7DGZSLo22rAV0Asa7kM34UmZBADBHtKWQbu7Kt306PVNAzhGwitlL9MIb8jKwC5hDsmlX8cTDoWOhgGSyvpGtI7F7v7ZhOzfgA-2Hpearg9gujI8-M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید از تمدید قرارداد آنتونیو رودیگر تا سال 2027 خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93589" target="_blank">📅 12:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a46feaa24.mp4?token=NnBoZB3zAv8Nq2B05GuIJmA-8BPZyyTUTn1iAO_RQu2gDrGvjyPiodosbsp6omJwt3fCaxfqUEHXiUmjLOQcOdXqzGWtYTaVlnifeKz2koHVq8CDYcqkCYZd2VMFUgQ9K67Agbkee-PnAROBq8Mi3IFjyjlH_6SdHUqUcby19Gq6iPf0nFlw8EAqwzgvLMHPgQtf-0tRo3coB9AZLViAOTmutRRkU9H7mumtZ6yH4Q2MXJRLQZ7d3MFOzRyJBpgLDPk946uz9Y6zLJSPiozlNWZu8yZYn4ChQ_GwJwlIlklF98P4z74g8W5fsZvZd5U77cuBvEqY9eaPRVbyn7rDSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a46feaa24.mp4?token=NnBoZB3zAv8Nq2B05GuIJmA-8BPZyyTUTn1iAO_RQu2gDrGvjyPiodosbsp6omJwt3fCaxfqUEHXiUmjLOQcOdXqzGWtYTaVlnifeKz2koHVq8CDYcqkCYZd2VMFUgQ9K67Agbkee-PnAROBq8Mi3IFjyjlH_6SdHUqUcby19Gq6iPf0nFlw8EAqwzgvLMHPgQtf-0tRo3coB9AZLViAOTmutRRkU9H7mumtZ6yH4Q2MXJRLQZ7d3MFOzRyJBpgLDPk946uz9Y6zLJSPiozlNWZu8yZYn4ChQ_GwJwlIlklF98P4z74g8W5fsZvZd5U77cuBvEqY9eaPRVbyn7rDSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
مصاحبه جالب گلر کیپ‌ورد بعد پایان بازی دیشب و درخشش جلو اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93588" target="_blank">📅 12:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=AvqXoaIB778roDhavQ2jgQTyGQM3uTCPQoyXLc89bpmQwpIl_T8jXVnw-pAcX54xVvtIzRMHVc3E_vIRPqm7u6U-HcSW9VCvPgh8ZAZ53xqsf4Qgr_xNWA2rUJYfOB3yLqVjvKxC8xvAhKKFH5ttvIC_w7hbkALWqRKfzIaKP0-x_HFsCg6Pc6zQlnur48nfJ7byUMp0ylrlhDiVtS3qZr7A5vJJTybOWi17QawnTbcs313Z7q65Ia0XKd-Rrxr1L22gNgnw4YNChLwPVzIVqFdInlIWqk8H26i1f-0bfkkA0_gxRcFmYbgQpeOPrH0_X0hv-Wz7TBN2cMNpTCt1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49a9fe65c.mp4?token=AvqXoaIB778roDhavQ2jgQTyGQM3uTCPQoyXLc89bpmQwpIl_T8jXVnw-pAcX54xVvtIzRMHVc3E_vIRPqm7u6U-HcSW9VCvPgh8ZAZ53xqsf4Qgr_xNWA2rUJYfOB3yLqVjvKxC8xvAhKKFH5ttvIC_w7hbkALWqRKfzIaKP0-x_HFsCg6Pc6zQlnur48nfJ7byUMp0ylrlhDiVtS3qZr7A5vJJTybOWi17QawnTbcs313Z7q65Ia0XKd-Rrxr1L22gNgnw4YNChLwPVzIVqFdInlIWqk8H26i1f-0bfkkA0_gxRcFmYbgQpeOPrH0_X0hv-Wz7TBN2cMNpTCt1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
🇧🇷
برزیلی‌های ساکن آبادان در جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93587" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a638ae04ef.mp4?token=FDsKI6_ePIBZ__UXli_wfKqs1GW65cOni9hOzi3yHFAzaL9U-Csu8Kv8RKxMct7npr64Igse_zG8Cn6ZctrXagUxTsxBRCbEL7JqwYvAc3Gxzjffohgn3vVzq4vZLQqi4RiR6JFa22Tv3F23DgPH-Eqa2vKHl9VTpGVdcyqYUMRuoFc4cyeCkvQs8HiJ2m_AeQbuwiulbZKo8FmdfzoLIYazLpUpwCJX15yXJtMzvFS-FdE3nZbFMES76icZYi266Wn1xzsuDy06ipUPB_eCNTqhM0x7OdzTzEgFpFq5mNfogcfQjDXd8cLlwdvYERRREPR25g1idgHsfbkcwtE3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
پاراگوئه با این سیستم هواداراش حیفه امسال شگفتی‌ساز نشه و به مراحل بعدی نره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/93586" target="_blank">📅 11:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYIt76jbpb4VQGmu0tacVuWrUQ67iGyLqM6IGLNx9WT2pPnFlCEF_hkm7JVVJyXDUuoifCmk_RgIr1q-Gz7QtV8GNLqt5ncz7X6oFiCJi4d2RJrcqSEpcK1vudH8_FUVjxja_o_ldnZ0VkQICZsKLzhDMzzHkf7vc0PQxK0KSaOyquKp7tn0XcD8bp2OR5zD4cVvhaj--khzvsvW19V-x5YwlU6RZTG2dMYRFYFLnwONR9RfO99CgveB96XsscLciS5bGTSK6OF4qCGX8sRK4uGY8mGQrjdn6Q2NCoCtqtwhCMMW2_NEizuWkwjv4SunX7nMtbPDiRXA4a6j-up7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93585" target="_blank">📅 11:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15c36b833.mp4?token=mvXYn6P-OKf73WGSuLQoCtTIGkksWCWOsomqrdV5tPWd7M-u6ucccTSCzUtynJgSNgrD_zuIT30neWalkvfjZ87onGmIKXjKCotroom05-dEtxdxK0vw7abT_iEFhijfiwxfpVuOEKxHRI0nWPvq3skd7L1TlQrQ46yfz6T-LVfYsDfZMJ_q6yJnZt6Gi-x129wihzNeh5bwuIDu5YYWVks7q88U3LhZtlpftpC7oCMTxjCPiZ67PUtDEyBvPvTv9QTM_Io5G1X19YHBFQUlUC4JGzuXgcJIS1lsJIGudBe6bk1ajnytuikwNwMSiqVkgeWI0E3mflHLvzPXcqhOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
توجهتون رو به گزارشگر کانادا جلب میکنم.
مهدی گاییدی
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93584" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93582">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K07xfeqxUt9fKE6PAZ3y8hDdgmp2D00W85pp6kovANAb298wwbnUkcI_9qrOnTZtIcPGaH32-g-g1yMPFDh2rWHLmKpqemS9pAtDL_G4bgRr7Ie5rdHNcB8WrC6xoWnkQJsqhHLTSJd_NUsdXcIZTBFNSEOk4hEmoiKBGkguH0NtpEdTCTDQ3nx_lSap16a3_OnQLMJs0MAwr_RthlTZRcnee9q0z07qSITcib-1JYOzpvC_z0GqyAfyejEV0mOQOnXVEsYcY6ZNTbxXdfjJ1oj5bQs1_wenYr561uHCZmITTpsrUY7KwoMQAFShLb06X8UOmxD_58a9CRR0J5z4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKeAXHdJ2LHs9tg6s5fUR2p9fQ34gVwK_Cbw55mQXkU5Ji9o0UVDkhKJ65DwqgLFBCmgSqKYhXjzteh32clvTQaWt3RMyR829LXmRZ_H9mkJDWP1YtmSAlVvLh889bx61yp8TeTbUH1wdEvvxsw6FOgyH_LG3GcwJHmZUHnw0q2ksvjIy_TCNt_QghnDm4TLOB0R0FA4xpdde4IEw8QwVrf1cT6pzWDPK8_ZLY5DatHHKvO49jUWTD40g8oT5yG8gg_kaA-PipYPY__Pcagp78wMsrV3mekiGwYa9DcIy5YHvrgnYEpJBP8FmnCPHJMkka6ndPfSFWjXhOVXxQokbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/93582" target="_blank">📅 11:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93581">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPVCkuxxzPcW7KGBqNH6CZya9p9LpaOLTSD2mIgttbnLlNWiEK4XLX9vSgDj3MAKq-_fAm4EOnbQ15pYZWpofe57ibbuddu7J488pGk06xjC8AQ3NEMIg9Zv0meSXYOt1PGBHFxT2jQVgOEc-U2dA1YBOTzhAEEH82TGcRqgc3a298sWiVAlv1vYdR_GgpTjrFUJpDllB3sTKs4n_dkEXRzG2QAfP5W85v5SuuNFxuj7WAOvp-a2cAVP2Q3pg2dZP_gg-XKROIMHdIWY5GwjlxvG4etTvLZ-eBLD5z2N55dioKS8j54nUwTf5TP0a2cyv5CNjMf-KJB2GrKN9S1taA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
گزارش اتلتیک از گزینه‌های باشگاه رئال مادرید برای تقویت خط دفاعی:
◀️
نیکو اشلوتربک
◀️
روبن دیاز
◀️
الساندرو باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93581" target="_blank">📅 11:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93580">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=f5h-7_mMrIc9L4ZVB0OHxjRt5dgE3vQh2YYlIehya__6M7WSp9PcbopQ_PRrI6EJt_sDF8KVhshrLSscTezR5cgJU8bmzhqyg7A8EPVExNci4D5oHZusVpAiO3F7CNlP1XpdjtwQKszZmdLCMYxGXOHV0VwDB5oCN7iLMRVM6UkHjkT-OqY2Ofar3kNEFDCSIW-I8_SH4etYxqpyqkZYVAvRSYETndN7Htw8dkK1zSpmncipucWiTVVatbOl18vppQ5TW4MHUPmy3NDjsIpBHeh4rFchr_3VqJBKaPakMUP5LH-Z9qbxwl7dmyUneBTHDS1oWYSfLMhJI9sXy2hI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7db3cbe5.mp4?token=f5h-7_mMrIc9L4ZVB0OHxjRt5dgE3vQh2YYlIehya__6M7WSp9PcbopQ_PRrI6EJt_sDF8KVhshrLSscTezR5cgJU8bmzhqyg7A8EPVExNci4D5oHZusVpAiO3F7CNlP1XpdjtwQKszZmdLCMYxGXOHV0VwDB5oCN7iLMRVM6UkHjkT-OqY2Ofar3kNEFDCSIW-I8_SH4etYxqpyqkZYVAvRSYETndN7Htw8dkK1zSpmncipucWiTVVatbOl18vppQ5TW4MHUPmy3NDjsIpBHeh4rFchr_3VqJBKaPakMUP5LH-Z9qbxwl7dmyUneBTHDS1oWYSfLMhJI9sXy2hI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🙂
کل‌کل بامزه ابوطالب با امیر علی‌اکبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/93580" target="_blank">📅 11:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93579">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItIVgaeJcpCIMShStRbDrS8aORC7r4XASSs7JGKOKhfu9nfIiAGAQxchyz4xgJ-SqMeht_zkpDStg-KngZj-c4aKw94U-e_NIXskTeAuBH4IKJssGAVPPlsjRG4V3UVgM12oQBB0Fwmt8dIsY0XiSAoYd8UGEWa8VZZEBGkZyXDY0aXqKPMDNn99IDH8UG4T8tEpMeKxkvHfwtlfDHyk9y55bOqBY_Hr0ZbA1g7U3FNnQSVPFEXTnI0hSLUytzZBaKyFhMf68-iNW01c3KDTT-IzHQZm7twqSW3aFpWbF-C4QiHWXCsKFLpqO-ajFVAT-uBJ3Zp9ymvK-HsUKwznCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93579" target="_blank">📅 11:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etluSQzAVkZQ_2ifvSnuGCMm9WMlWkra8LNC6djgtSwCCi25vxEqpmIQXJTXDCALLDhjt3q7rqIwUERsF3m5Oy55BDMo9_5atjndlDb0jY7VCVunB8OcNaiocmbXjjeV1-IIZlIIque-mu2F_5boRg-NlLJrgF8f_XM-NJovQ7S-q5vJ0P25USgXO0szgFi6YsLf642TwxvQy9t3llEon-oPnJM8sEdUeVB21bz6sKmbtQxNnU1oeuiiG3X3JjqTgsNCFUr-t0VFMcK-DTnhFKrc28QyUcmESrG6H3eR0QnQb2el4G1a2-Lyzs8mTkmmM873HFo84IewIwtvXkb1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنبد کاغذین:
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/93578" target="_blank">📅 11:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93577">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=CE-h9nzvnPqrqR6Gt8PBDn97DHjZMnfwvB5RGleY4iDliU_8UtOSdAlTp1QCIhJLQmAL4FFT_UlhFl71_zxnRzk2xO6v9ntxG5Q1PVIkBmokGmF2tWvDpH_67qRI-3fh2P0P9iE1ZHYLl0tmUoYfI6VcVMiAXh85Ml1tBevxdWlw777ohS-8q-wITAk6FHtW6sweIqVyt1TqmzkV7iwh_-8ZLHtZQo3J3udRFFDgMSFyZAVi7soL_VkDgkUxekrF2svQHgGWHXHe7bCBzykfAa1fE96Lg78APmF4yOA2yZ0HkXR7AQpCJCe-2gnHQTaZPARcwo1Up8f8BWrp-s_9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a7c2e1de.mp4?token=CE-h9nzvnPqrqR6Gt8PBDn97DHjZMnfwvB5RGleY4iDliU_8UtOSdAlTp1QCIhJLQmAL4FFT_UlhFl71_zxnRzk2xO6v9ntxG5Q1PVIkBmokGmF2tWvDpH_67qRI-3fh2P0P9iE1ZHYLl0tmUoYfI6VcVMiAXh85Ml1tBevxdWlw777ohS-8q-wITAk6FHtW6sweIqVyt1TqmzkV7iwh_-8ZLHtZQo3J3udRFFDgMSFyZAVi7soL_VkDgkUxekrF2svQHgGWHXHe7bCBzykfAa1fE96Lg78APmF4yOA2yZ0HkXR7AQpCJCe-2gnHQTaZPARcwo1Up8f8BWrp-s_9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇸🇦
🇺🇾
عربستان سعودی در بازی سخت مقابل اروگوئه به تساوی یک بر یک دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93577" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=lWgR62ntO8L8tWRedktuRYp-0MDttqyKarmqnnljJJvpDl8lr8MoD5nLEOm5ktvoi0c8uJAi1QydBdTcqI_Sct2Lumz_poBvsXjP1ZbMz7WjrHlwOXHNPXMSf--5ZnjJAcGjzrG4kpEylzCGy2MbI2oFMJIMBeLXlm2XJSwjacIUnQP6zUu7rmicR2dlbDT4_u2Gg37GvN8MxhME5EB2XAJfiSZFjcFGq0ZdTePcmpeIrvpJfRiaB8UdVV5tdl0Nt8KUtkUAMQZ_ju0hloXd-f_8PU-tmpIT1TXuGmixU3pi5ym2torq100I15UivUXFQj5x3wjk7BJl9daXjfJTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31883b78b2.mp4?token=lWgR62ntO8L8tWRedktuRYp-0MDttqyKarmqnnljJJvpDl8lr8MoD5nLEOm5ktvoi0c8uJAi1QydBdTcqI_Sct2Lumz_poBvsXjP1ZbMz7WjrHlwOXHNPXMSf--5ZnjJAcGjzrG4kpEylzCGy2MbI2oFMJIMBeLXlm2XJSwjacIUnQP6zUu7rmicR2dlbDT4_u2Gg37GvN8MxhME5EB2XAJfiSZFjcFGq0ZdTePcmpeIrvpJfRiaB8UdVV5tdl0Nt8KUtkUAMQZ_ju0hloXd-f_8PU-tmpIT1TXuGmixU3pi5ym2torq100I15UivUXFQj5x3wjk7BJl9daXjfJTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فیروز کریمی: از اینکه ژاپنی‌های رختکن رو جارو میکنن بدم میاد چون خودم شلخته‌ام!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93576" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93575">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4_391xtkoS237of1wZKtNa9evaleQKzirx9DFhZil9UR4lQqTDkuI2v9c23LwkfK8BgfZl1UHcxqw5gwX5yxOgTdyFSq0OxFDd1R9qhnDHBYHv-siT_K2s5g9displP1ISuhpWA0da2hPwUOJSB8RCrGCjFKvGGPvr2MBAfghobiUXJqALWuxk52jbcrJCMo9mg_wx-FckJ62YgViR5nfzJq0OYN9wE7N295xlrzGb02P1oeG1Ky6Xc0nmgtgYRimditd5bAY3-V2dT-7OHMzVVmg8OOGOiZnzTWmTqIzWiTv5oGCEK9tXeN258MBSWh6X_PhhUSARpH2WTY7OPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
#فکت
؛
پشماتون بریزه که کیپ‌ورد مقابل اسپانیا، بیشتر از آرسنال در فینال چمپیونز لیگ مقابل پاریسن‌ژرمن مالکیت توپ داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93575" target="_blank">📅 10:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93574">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=aW1FNNzaqvcyZz5w3o2OUFci_bC6enwn5bv8BqY7Aa05gXexv8O1XoDHNW1QMhNifWS4zoQp_FDqWSdt8RU_xOH-fnjopXxuWEgThF_5jeai8ct4CS1GHD92RmECgusjEvGqbkV_sDcOfa6xqPrq6NoBTi6Up-lespmJ2b_8c5RGxZ5tV_cZ9zxvanr6c7qSiDeu0p-7g9THoynrFfIwqNnLmOl_KV44F9R_DZME4kQ9JgqnnYQ562-b4_8dWo-PQbDpqy1JZNLbaiIlr5DTt4NljZoFAs1yf-dcMtffTlvEcMMptQIJHsBpyPOg-gyBdsQ__0BtVHewO9HNWBYm9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f4a62cae.mp4?token=aW1FNNzaqvcyZz5w3o2OUFci_bC6enwn5bv8BqY7Aa05gXexv8O1XoDHNW1QMhNifWS4zoQp_FDqWSdt8RU_xOH-fnjopXxuWEgThF_5jeai8ct4CS1GHD92RmECgusjEvGqbkV_sDcOfa6xqPrq6NoBTi6Up-lespmJ2b_8c5RGxZ5tV_cZ9zxvanr6c7qSiDeu0p-7g9THoynrFfIwqNnLmOl_KV44F9R_DZME4kQ9JgqnnYQ562-b4_8dWo-PQbDpqy1JZNLbaiIlr5DTt4NljZoFAs1yf-dcMtffTlvEcMMptQIJHsBpyPOg-gyBdsQ__0BtVHewO9HNWBYm9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
بررسی تساوی عجیب اسپانیا مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/93574" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93573">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=pI82HjhdCDatl3PEq1PJZaF6bTHOuQScww4XbEgQJdPeOjOLeijOul22Pfayz14E-QsinG3ZR2PjhJa_VPejrCG4Tcl403fSlk2b1_wE5z1NXLMQqbH8Qm-f2eUJlfd2AU63PbYTGO_OWbHx9VZuvJlMv3yRSWxt77s2rMRavMoHSfQXoDAOnwmCqTerjK5kF3xSmnlesM6uhu4iHcGKb34IH-77ECtFf434t1Tx-1G52fzI1ToSFz76JBnDfPQEddk6rIzp3f-O3te11qC_lHoT_3IESbi9e_4wMvsKRRoJ8gmcth6nTi4hiFc11Q8VwcVs57IeE4Aesf2RzwyNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49803c87d4.mp4?token=pI82HjhdCDatl3PEq1PJZaF6bTHOuQScww4XbEgQJdPeOjOLeijOul22Pfayz14E-QsinG3ZR2PjhJa_VPejrCG4Tcl403fSlk2b1_wE5z1NXLMQqbH8Qm-f2eUJlfd2AU63PbYTGO_OWbHx9VZuvJlMv3yRSWxt77s2rMRavMoHSfQXoDAOnwmCqTerjK5kF3xSmnlesM6uhu4iHcGKb34IH-77ECtFf434t1Tx-1G52fzI1ToSFz76JBnDfPQEddk6rIzp3f-O3te11qC_lHoT_3IESbi9e_4wMvsKRRoJ8gmcth6nTi4hiFc11Q8VwcVs57IeE4Aesf2RzwyNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
👀
سوال ابوطالب‌حسینی از امیرعلی اکبری: شرخری میکنی؟
😂
😂
جوابشو ببینید عالیه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/93573" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93572">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdL_zIUz5OGDRWAvGkNgkHxzuWuoNhhzCEQ3Kv4S-7dydZ6R0jWa6S5SPB8KpDRxeD8Bq3YkEW4y1ZEyVQZ8-WWN40OrE155XaCLeKE6liv22ALd2ZfGzXLN8r5cOuuB4jiRCf-Uh0lETc4daFoZCwme7tL9-Y7Du-8j3NalDLGiOoz5vj7dXjOEZqdkM7jrhmy3r_1_N3WV_JAQvm6gp7vWsZV08mD8s0WYrpfez-9ov8YnpxEzmluWHS81AzMqH0-zZzhZBa6GNLiL4Q8tznlW_z8AubRy8aa1tad7pSVcXiBB6TX_LbPjt1IVmP53O82IR2UPzUUDwT0RZo0-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ویزای مهدی ترابی یک روزه بوده و منقضی شده و اون دیگه امکان ورود مجدد به آمریکا رو نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93572" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93571">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHBeMiQAFfoxwzg5iB4YoJKcO_VNJ4yD9Qf2OUzrd0QyvRajfadwLkJLpvATneAxtTL9LsxJPQmPCJA-dwt0qFCPcw79-uIoMW8gGgQN8jSnfsjwxgkRurU2u89d3kAeYjvvYUQnhGK61rZhWOUDZTRLbRel3Vw4Eo9Q--vNP0_eSyybIjQHGmURFbnIuyRQbMksKAzTksH5tVhU2IBkFhmA9dL9CYMEYt3jS5wGa41AqYuxR8ZsjSR1N-gbphEv5tARvvXYXt1YntZkzGz6M1y_p9XaYNdM1jWZSTs2dQVg9cfxILmLcnjTUJx5W9DTQjY5QFqRMuuPPuo6PishWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/93571" target="_blank">📅 10:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93570">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=K55JqNacbKjw2ZhB_GMAj-Fyl64nOLkqys8SNRemKvT1AXGwq2aoy2OERUIwNu0lLtOrvs140mFsCAAPowIiuMphw_lh3xiMwsufnc-hxdOxXfT1aQg7-ZeYTRTd8VjCRB4edR32UELo8Vng69QXzNWWADIS1IpbHE2UTjrCv1VZSrZ9vUNZ6z-t0obVs8Y5NkDuViajVYbYtvE4rYxU00b48Qa7A50USwDxzVuV-0SgyURcrBeqeV0VcjrI2aHvGo9mvkMyqNNW3Rz8TKWM623LGfQb-HHhq69sLdN6u8eU8SlYeLsF4wBGp1FDVlIzGuti7ma8D17-n8jgbHdjvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd4dbbaa8e.mp4?token=K55JqNacbKjw2ZhB_GMAj-Fyl64nOLkqys8SNRemKvT1AXGwq2aoy2OERUIwNu0lLtOrvs140mFsCAAPowIiuMphw_lh3xiMwsufnc-hxdOxXfT1aQg7-ZeYTRTd8VjCRB4edR32UELo8Vng69QXzNWWADIS1IpbHE2UTjrCv1VZSrZ9vUNZ6z-t0obVs8Y5NkDuViajVYbYtvE4rYxU00b48Qa7A50USwDxzVuV-0SgyURcrBeqeV0VcjrI2aHvGo9mvkMyqNNW3Rz8TKWM623LGfQb-HHhq69sLdN6u8eU8SlYeLsF4wBGp1FDVlIzGuti7ma8D17-n8jgbHdjvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
😂
حسین‌ماهینی بازیکن سابق پرسپولیس: تقریبا همه بازیکنان قلیون میکشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93570" target="_blank">📅 10:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93569">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c278508f69.mp4?token=ouH_ttaYDBpklP5dQuUFSMsL5cWSWAZJpglugwZ0mpNg8cU7WwLR0YSBnwmF4gn4O56IqSYgx7guoawJIIKukYYE9I2o1u5JD7SkaX3H0URxXQU6qaX27tSzZk1YW5Jbj5wsKdXOVzsV-FZdAQ6HG4IEsTF2rXQCSRlGKlFlUdP-7ve4Eg50yR3CUe5Us_5d1Vj-g_5v0fw-2tbwXcZpodc3Uoj4TduD3ds7OOk3USwXCLqsYP7hDEwW_SPsMwANLgreAGruoAg3ABo2EzNSVpexOY4yr7d6VQ6CyHsBMOByPeYuqGzegYqTpFg-KQbOYD9DDlf-FwohsIcqqfi_2IxBxz1Ld9z3eZGmBixqZ90sP1PYnCmwla403QGeWRzQP3gKCwAt-RiJNqqSoZ7FxNQpnWzSlwJxcswzvnN6zeSEJxkGjxY4iWwrg-EEPzwrm3Z9t1iQvP63k1diG-QbP49FItjPQLbTEbDgQzd8qWnytFs2hQPT0SWrebJt-FdUU2H2KMVMjJ9F6RZQZLL-ANzPiVCpzlb3hAZjVfp_zAgJ81cElyAXE04tavH6XqRS-SKDKNU4MIlZnQBAn0_Va1h3aiEdiWYNkYoJ-XMlvVTZh8XUI-pi26GrtJHORcLIl8kctqTWCQ4dT48nP_J_hoiyWW1Y34RdsLOxZyvOvUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c278508f69.mp4?token=ouH_ttaYDBpklP5dQuUFSMsL5cWSWAZJpglugwZ0mpNg8cU7WwLR0YSBnwmF4gn4O56IqSYgx7guoawJIIKukYYE9I2o1u5JD7SkaX3H0URxXQU6qaX27tSzZk1YW5Jbj5wsKdXOVzsV-FZdAQ6HG4IEsTF2rXQCSRlGKlFlUdP-7ve4Eg50yR3CUe5Us_5d1Vj-g_5v0fw-2tbwXcZpodc3Uoj4TduD3ds7OOk3USwXCLqsYP7hDEwW_SPsMwANLgreAGruoAg3ABo2EzNSVpexOY4yr7d6VQ6CyHsBMOByPeYuqGzegYqTpFg-KQbOYD9DDlf-FwohsIcqqfi_2IxBxz1Ld9z3eZGmBixqZ90sP1PYnCmwla403QGeWRzQP3gKCwAt-RiJNqqSoZ7FxNQpnWzSlwJxcswzvnN6zeSEJxkGjxY4iWwrg-EEPzwrm3Z9t1iQvP63k1diG-QbP49FItjPQLbTEbDgQzd8qWnytFs2hQPT0SWrebJt-FdUU2H2KMVMjJ9F6RZQZLL-ANzPiVCpzlb3hAZjVfp_zAgJ81cElyAXE04tavH6XqRS-SKDKNU4MIlZnQBAn0_Va1h3aiEdiWYNkYoJ-XMlvVTZh8XUI-pi26GrtJHORcLIl8kctqTWCQ4dT48nP_J_hoiyWW1Y34RdsLOxZyvOvUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
عشق‌بازی یه زوج برزیلی تو استادیوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/93569" target="_blank">📅 09:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93568">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d211a827.mp4?token=IQ8P-psZvnKv8cwHjihnKzHuJWeAYhQ_NcRaz-XIViEKckmnBVlf2Y721rYAHItozlK9JXi760Ku7AjmZT6VRlQnCAwBQKoDGrvv800YFBvUQZdHig7NJQFqRz-UnURbglGWRqIlEI2a7FcBTrWGl6nY8MmWxu2o5mzlducHCt1a7aKgRoir2926m2YIOgfiAtfDmf6w9Rabb-gN9x4qBx688EZLe-EFf9Z-V_MsWwU2X2GMvwJzXlQJioSLpZICoDz2x2FUbN8Rxm3NipUGKRJaeWrkXtgPNiZ9FMQo8mq9IjaCcZ04Q69gluPVcg3SWZiIsGZlka70ruy4L3OreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d211a827.mp4?token=IQ8P-psZvnKv8cwHjihnKzHuJWeAYhQ_NcRaz-XIViEKckmnBVlf2Y721rYAHItozlK9JXi760Ku7AjmZT6VRlQnCAwBQKoDGrvv800YFBvUQZdHig7NJQFqRz-UnURbglGWRqIlEI2a7FcBTrWGl6nY8MmWxu2o5mzlducHCt1a7aKgRoir2926m2YIOgfiAtfDmf6w9Rabb-gN9x4qBx688EZLe-EFf9Z-V_MsWwU2X2GMvwJzXlQJioSLpZICoDz2x2FUbN8Rxm3NipUGKRJaeWrkXtgPNiZ9FMQo8mq9IjaCcZ04Q69gluPVcg3SWZiIsGZlka70ruy4L3OreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت سریال‌های نمایش‌خانگی در ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/93568" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93567">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14cad201b.mp4?token=dnLthTLFxMc9R-87DY9cDBMS5TkIi8KxMLrvQaAo3LEHTiwWOUH1SGO158Py-gu1x2DUf6tEiT5kxsaG9wBeSNgZGX-0ssZF3AM7Pimgy2g3G9ed8sfbZq20s33pafrjz927e3S2M9QC_KpAnEAdOY8tJW_dsYqw2liPuWYxPsdrtOcsBE6v6dpJqUG1T5k77uH-vS29aUb7-4jPbe2OLsYpXPnDa1mSsInaXIJLTuqzmPTKGPDGMBjvoa4XcNMRAR96x3IIL47OTnRR611c5ADq9zx8LpK_rGtLx8Tij4giOM9q2qQO3I97dApFTg3Peel2bjJMaYLwY0uVUsqCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14cad201b.mp4?token=dnLthTLFxMc9R-87DY9cDBMS5TkIi8KxMLrvQaAo3LEHTiwWOUH1SGO158Py-gu1x2DUf6tEiT5kxsaG9wBeSNgZGX-0ssZF3AM7Pimgy2g3G9ed8sfbZq20s33pafrjz927e3S2M9QC_KpAnEAdOY8tJW_dsYqw2liPuWYxPsdrtOcsBE6v6dpJqUG1T5k77uH-vS29aUb7-4jPbe2OLsYpXPnDa1mSsInaXIJLTuqzmPTKGPDGMBjvoa4XcNMRAR96x3IIL47OTnRR611c5ADq9zx8LpK_rGtLx8Tij4giOM9q2qQO3I97dApFTg3Peel2bjJMaYLwY0uVUsqCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
یکی از بازیکنای ایران موقع گرم‌کردن اینجوری توپو کوبید تو صورت یه هوادار نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/93567" target="_blank">📅 09:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93566">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlU8n21XJiEio926F1syb3AW4hTqQA6zXrsSXoClNG1R31CYz-KTGj9xjDCQBzAvPefs1tt3bh_qShYNRQn1o5oDkUzrGw0-wZ7_eirEn7Fl7qXGw6JD8iQ3D1GAXtJF36czcliY-673NCYE2Hl-t7SEQE89TTMjdC3DmYWdR7v6p0U7g7lqbRIPyFr2KR62Zk8iXI8yBPtjwvdxmrmZpLzkrM88b_dRJAadNQZRt1hOPiDcQLV18rF8yW5YpyI2vkeKQkczm_bnLsBvmP52dEI8twx2wLOKsuCMO5mhkxXmZw6Us40blnXJIGAM-9wbtI0JvrBLOCuI-gdKsh0d3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
پست جدید همسر نیمار که در آمریکا حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/93566" target="_blank">📅 08:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93565">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKLO45OEXZ96PMjD2bfRiD586je_FyeMXq7gATqWQc7I0mz5jLehKCK39YhnT0FQBgf_L6Dbk53aKXmXRg6rq8xpBt9XV4bPWGDZUbiuS6cwQDKQ6oLDmkKYfEi5Vupvv357lePulcfXvRxBKJvkMvtLRSTNcCQg8_hUAQJ_hsl9wE04mwiiYPA5ceE5r0_Mfw0ruwatsRwirt2Su5SzYdmd1pwv0rarfH_CtIryC73YvW8brjTD62qKsu4wJcVstAasNMlkW1ZJ4_o6xPJ-CCqB2C6lbQQP-zMMI7lTLJYb1NQFC9h2-eCQKWRZKjOV-rO-Uoh0fl95fDbTdT229A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که به یاد تمامی جاویدنامان سربلند ۱۸ و ۱۹ دی‌ماه برافراشته شد، روحتون شاد و یادتون گرامی شما هرگز فراموش نخواهید شد
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/93565" target="_blank">📅 07:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93564">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba8e65935.mp4?token=IKl1AP5-XHZPSbV7AyqIWTlKiQUbnHISswwtQydEPVQ-fTJkUC5pcMeIiMqmMsg-SL_Xc_tMxHqTjLEIcOC_Lfr-Sk8Kx5LywQkzEtqOZHopcuuWb6CzvBiWeWMQp8ZwBFdqDz75M_XA1oo5Qw3trWQLWzZ2DBidz5eOvlk0Pf-dlstodWmPbx-8845dod0GTSMEdAOZF-KgdrMHc-pRx8nWj-S8pT7NZ1SkmeaQqKj6wR3wfg03zF_tQdH16QlGuyvZVtOioKwastqTRKryZOVyiGhMwEkHbZ-JJ80rWVrHwmh_uu01J6giM6OPjdt-MNf78KpAZoHxxeC9q9GLZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba8e65935.mp4?token=IKl1AP5-XHZPSbV7AyqIWTlKiQUbnHISswwtQydEPVQ-fTJkUC5pcMeIiMqmMsg-SL_Xc_tMxHqTjLEIcOC_Lfr-Sk8Kx5LywQkzEtqOZHopcuuWb6CzvBiWeWMQp8ZwBFdqDz75M_XA1oo5Qw3trWQLWzZ2DBidz5eOvlk0Pf-dlstodWmPbx-8845dod0GTSMEdAOZF-KgdrMHc-pRx8nWj-S8pT7NZ1SkmeaQqKj6wR3wfg03zF_tQdH16QlGuyvZVtOioKwastqTRKryZOVyiGhMwEkHbZ-JJ80rWVrHwmh_uu01J6giM6OPjdt-MNf78KpAZoHxxeC9q9GLZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
درگیری هواداران ایرانی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/93564" target="_blank">📅 07:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93563">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de82df63b1.mp4?token=FPmTz-AjXPDBftFlEDAGFpZc49DM1ak37aEZBukqMJjjXrGgs_DBHXAL2wLAbVgQ604f0egzPFw1ytkfgFOxngUNODi-KhJCeQaB3EAoi1D4fnYs0KOquq--mHgWF_T7NhTFSpFJiUvl41j87D6ueZ8orEVc9Kpz_Py98_cJYae-xOM6SJtTddBXoHEr6BaOjyqFOtiRU3QAhoIjJvHCysu1toAqGDZTq3BtR-yej9PBAuQDNun7X7Ik7BNwZQdXI9oZnPFSH6DTDI824fdYQZSV4dBUWNPzSWs--OoRVFmmV2Up40Oo5kl62zWc9E5Btml0vubTIPyoBVcfG3kj0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de82df63b1.mp4?token=FPmTz-AjXPDBftFlEDAGFpZc49DM1ak37aEZBukqMJjjXrGgs_DBHXAL2wLAbVgQ604f0egzPFw1ytkfgFOxngUNODi-KhJCeQaB3EAoi1D4fnYs0KOquq--mHgWF_T7NhTFSpFJiUvl41j87D6ueZ8orEVc9Kpz_Py98_cJYae-xOM6SJtTddBXoHEr6BaOjyqFOtiRU3QAhoIjJvHCysu1toAqGDZTq3BtR-yej9PBAuQDNun7X7Ik7BNwZQdXI9oZnPFSH6DTDI824fdYQZSV4dBUWNPzSWs--OoRVFmmV2Up40Oo5kl62zWc9E5Btml0vubTIPyoBVcfG3kj0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد تند یک هوادار ایرانی حاضر در ورزشگاه از عملکرد تیم قلعه‌نویی مقابل نیوزیلند
❌
صدا رو کم کن بگا نری خوشتیپ
👩‍🍼
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/Futball180TV/93563" target="_blank">📅 07:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93562">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگه به قلعه‌نویی باشه که الان میاد میگه نیوزیلند ده روز پیش فقط یه گل از انگلیس خورد و باخت پس طبیعیه ما نتونیم ببریمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/Futball180TV/93562" target="_blank">📅 07:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93561">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
اینکه در ادامه آمار بذارن که هنوز تیم‌های آسیایی باخت ندادن بشدت آزارم میده  سطح هلند و اروگوئه و ترکیه و جمهوری چک کجا. نیوزلند کجا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/93561" target="_blank">📅 06:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93560">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/Futball180TV/93560" target="_blank">📅 06:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO4dtzNXu6ociMovasfnkP4TGhJjDHK7VJ_eG4wimIgkczWTgO8-qWqbC3hN-SzC1E4zHj5Yiy-pl-qOEGfytZbCQjYauTCizOAumqYZkCAyuJYQ4z-P_jst5C1syTc9RsDp3ZElQ54zpJBIJoCnuU1wtGiBJn9cmZ07it3pQ14rj6qBhTihmRFCdG5m_tRe0wpQSn9k7lLGMXCk_F8jfKXmoU4YS1pUevX-KM08OOsd5wrgBhPD7tNZEoLKvIPhZZoxtyIEOsDbl-mZfzZJZr0StbfTf4ccTq3uwOzEOGX7o0KOp_iwHVg-05HCQZqzsmCKmwZGpv5BnMS-TNCSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
قلعه‌نویی میتونه الان تا ۵ روز دیگه از جدول اسکرین بگیره وگرنه خاطره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/Futball180TV/93559" target="_blank">📅 06:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4LaGY0803XDAjU3cNBK1x9AVQkzBO1eq8Td2iSsU6ruUgkoqtbVND2qoTqguexSRLqjzLAzs0eVQNYwhvcIHnGocYioHFmYM9459ExmDDrlU8sk4J6wsuF9Y1pDf3DRKLoxvKolQfNxgkKTEXnLiFFmc-WTrWnEjqUHHuzo4GZDMTngh5Q1_eKolRkV6M-DZSnONU7UgPvZeVXTNpDjYqY7G1hMK7RPSYinZY-bxewxEocxsdajW2zPgFEmYXLy07ytAFt_4rAEhFhScnqCVMsOpI5saThRob15Y4L2SuLyo3le-rBOTPoxdj5FHSopJuQr64lsluLEfBZ9aszz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
رامین‌رضاییان بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/Futball180TV/93558" target="_blank">📅 06:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/Futball180TV/93557" target="_blank">📅 06:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSHkzPEp2dkcKzA-Elsc8T7V7Sr9DO12XmTI2a0xcdPEsodl_o1JcjmYl7AIA_94Y_0nOTI2e6z7CDG48R_oDqAfSQ7OJRmCLhqR1OgkYkMf8inBUdEKoNhHBDrDHFsWzpv3DZMIF6hnKP0y1rnr9Vdpt-gcID82Giq9qXm7Q3vep9B8HCdIRwPatflcP54gAnCrsqNxvP_XSHoR3xcoys1geOgiLHM6EOSAgUZNjzfipKLdvaAbopwrAmryAol6SfOeSyChbqu01DwqblzVAvnk0RDCG9yojyotjXQ27qJZP-uaoOpxcD5sONAkKvRTKXMheinhnRsvRkOnQZLYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ منتخب ایران مقابل آسون‌ ترین تیم گروهش از باخت فرار کرد
🇳🇿
نیوزیلند
😀
-
😀
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/93556" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آخرین موقعیت تیم قلعه</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/93555" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آخرین دقیقه بازی</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/Futball180TV/93554" target="_blank">📅 06:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93553">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گل نشددددد</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/93553" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93552">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاید آخرین کرنر</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/93552" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93551">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کرنر برا منتخب ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/93551" target="_blank">📅 06:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/93550" target="_blank">📅 06:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93549">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حاج صفی زرد گرفت</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/93549" target="_blank">📅 06:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پلن این بوده طبق حرفاشون ۴ امتیاز بگیرن
ینی اگه این بازیو نبرن حداقل یه برد جلو مصر یا بلژیک باید کسب کنن که با این وضعیت ریدهههههه</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/93548" target="_blank">📅 06:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93547">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcOhVuY4KaQzFlyDik7wJmJhbGknrZJjqq3vvvAcXL5U3UShD8jY_hhPInaJqp0dQ15VJk2Rnyy3rUO2Mz9NnbFBSauqdu4z-9pytiA-4SbTUonsBAxSO3_pMYWkKHmYUGx_Gi3UH64Hw3S7P2gjQDMsBmqCcFRhwCLDCZ0vpI0B9vke2ZxE-vlUZrtJen3-WfqEITCmynwMgi_-aWcxe-Kj_UY4WeI13YLY6HhVC9SKHWiyIh5z130sMAeidRxJlq65rbbN372M-uIPsXSozZtoFRKosaMCN3WvVClYanA50WI4bUsP1_h1u-WeQG6Cp8grXI2TKV3OBzZIwGXFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فوریییییی
؛ به دونالد ترامپ اجازه داده خواهد شد تا مانند جام باشگاه‌های جهان، جام جهانی را هم همراه با تیم قهرمان بالا ببرد.
🔺
عجب قابی بشه بالا بردن‌ جام‌ توسط قلعه نویی در کنار ترامپ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/Futball180TV/93547" target="_blank">📅 06:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">علیپور هروقت توپ نزدیکش میشه فرار میکنه
مرد حسابی آوردنت بازی کون بدی پس؟</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/93546" target="_blank">📅 06:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyMFA_WLFOlpRXUO5qobPeAd3ehFxRwF7kxy019zdYS_DVmpqNr_g868Ocd-UCEc2OK3J5EYAeTOzpuIsmZdwjqY2b12Q7KQOhvCJwFJcrtHK_6MCWdMQprM2AxnFyNsV6LJGBU-HS_LkwwWi-1nV-JT8GXZYIyPd_VjofEFaTpQvOBwyn5_V31290kM7Hk-yMIxIkI4SU-fKMJf2f0zXfU6eLYVBZuLLinHE7gAxf7lcfq7n56ovBYzBGyOqDULCxvhcDwu1Qdrhz6x1gxI0MO-lZE4u4BjLLmtCRRf9b5Nuo6QuVd9WLlMIYGv7nArS3EBgOPAtBtRyJQ-0PrWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/93545" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93544">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عزت‌اللهی ریددد</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/93544" target="_blank">📅 06:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93543">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الان دقت کردم اونایی که پرچم شیر و خورشید دارن هم بعد گل محبی خوشحالی کردن
😐</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/93543" target="_blank">📅 06:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دو دقیقه پاسکاری کنید چی میشه مگه
😐</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/93542" target="_blank">📅 06:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏با اختلاف بی کیفیت ترین بازی جام تا اینجا این بازی ایران و نیوزلنده. قشنگ هر دو افتضاحن.
کریس وود پشت محوطه استپ سینه کرد، با سرعت ۰.۵ چرخید، سه بار زد تو سر توپ، ۳ دقیقه فکر کرد بعد توپه گل شد</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/93541" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/93540" target="_blank">📅 06:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93539">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/93539" target="_blank">📅 06:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlacArbA6JDOh5YF5OtsJh47KjUHTpP_zgvZfwXei1Im1rdOE8veal03TpyDXfD2XNy-aFftDZxVTf4zOLW_G4qPU2UP6o0JTC5z7jnEt95Dt8l5AghLPHSmBNfHADOVHeaUeXXkR-vmglFpAQPStYFnoz7ggBeos5KlUuasNGSPedSYWi_T-sC-pSItDd1tCKBQDWacj59Hwxdms210-Q4kI_d_U0DzjtjaNu-YWdRB4ceZ4Q8nZ-gusQJDiT94SeuPtgMbnD2h3t3o1vUuR0Z_PcQlVK65XfdjDj2AVCfviFns37ja5w-yXDGOY9R7G5tLDepvhEv7SgFFIg4cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت میکنم که این سکوت منطقی تره
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/93538" target="_blank">📅 06:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93537">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هافبک وسط نیوزیلند بیشتر بهش میخوره ورزش کبدی بازی کنه تا فوتبال
😔</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/93537" target="_blank">📅 06:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2axtRJBoaVnRafADWoTgzGCIZRlSQjTeCzJdDE1zI0Auk7wwe-b5wUXYatn7oZuj73DT8U8g6zhaPlu_OdXwRRli-0ssZn48ClUWxau39aU5Uo-Ofm-aYNC9TCBxV8odhwGrV-cvAkcuyeDivU6tuidk3wGe8S0-RIR5zRwumfhJcscpG_JfUfqJ3EW8-OiN6m12z70fo9h3K3jytfv2JvPJGmXMABPPkwO0fl0DLk_gifVvS9n37GGHbvU5Ck8wcMUplLRpT6IdZH_8lGYrlw6-mZkEqGr1YvddRF4Au3zJ4CuAoHnZGFFLQbmlT1CH-ndXs-lhNcN_SuMzWvPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
کوارتسخلیا مناطق جنگ‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/93536" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اینقدر اختلاف ساعت کیری زیاده که ایران صبح شده اونجا هنوز شب نشده
😐</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/93535" target="_blank">📅 06:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نیوزیلند تعویض کرد</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/93534" target="_blank">📅 06:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رامین‌رضاییان یه حرکت دیگه بزنه تو تیم منتخب هفته قرار میگیره</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/93533" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کرنر برا منتخب ایران</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/93532" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حاج صفی بجا قدوس اومد</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/93531" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93530">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=hxuQBa4-6HLBS3uK2uEdWC5YW5mn0uQLxFil2Kh_vlZrCcFvWLthXga0cFppuZJFfnzMJgGJejxVQ6SNZobQqR85JK7ZT4gYoxWRlJmkheVJ-Rz2l71OQWhjLf_43Ljgmhr3DaB9NJqvogKkbPw_lvV2l1BtE0-ogZagF1UZDhcCGVzXuTjNUz2pabLtI8i29dzlzvU72lyBWPt3pNSb_Zqe1yn30OofITlrjme16f3iS3e8Dv2oqP1cs-H3aRkM78t7-ccSX_XxqGCi7kQX6i1wr3zfb-Xd02jXujze2fzd-Xwq4YkWzU-Gk02UFXoyiwEIBRag_V18JYqqMRB09w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=hxuQBa4-6HLBS3uK2uEdWC5YW5mn0uQLxFil2Kh_vlZrCcFvWLthXga0cFppuZJFfnzMJgGJejxVQ6SNZobQqR85JK7ZT4gYoxWRlJmkheVJ-Rz2l71OQWhjLf_43Ljgmhr3DaB9NJqvogKkbPw_lvV2l1BtE0-ogZagF1UZDhcCGVzXuTjNUz2pabLtI8i29dzlzvU72lyBWPt3pNSb_Zqe1yn30OofITlrjme16f3iS3e8Dv2oqP1cs-H3aRkM78t7-ccSX_XxqGCi7kQX6i1wr3zfb-Xd02jXujze2fzd-Xwq4YkWzU-Gk02UFXoyiwEIBRag_V18JYqqMRB09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌دوم منتخب ایران به نیوزیلند توسط محبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/93530" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان  حسین‌زاده و دنیس درگاهی میاره بازی این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/93529" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محمد محبی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/93528" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گل‌دوم برای تیم قلعه‌نویی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/93527" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان
حسین‌زاده و دنیس درگاهی میاره بازی
این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/93526" target="_blank">📅 06:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این مهاجم نیوزیلند شجاع رو گذاشته رو کیرش میچرخونه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/93525" target="_blank">📅 05:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نزدیک بود سومی هم بخوریم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/93524" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
