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
<img src="https://cdn4.telesco.pe/file/OkNnPhH7KymmABjXjlJA3J4cTf_AikVTNSbnH1m4bDqm2NWJha84kZoIGCy220omjQvpXfiZyP81aMPa7vRsfjA6FFCglZgFwNTD1lEsxrrdfRZCyuPTiHl-w1JugPXxQBdJyt8O3VvwfxlTJ8-HKCcUMbDy0hbCyaKUBngeRLl-kFrq9TYzamj5_moK0N_dYiNJUTp22EzDwIzDnGIZf7YqE1_bnhlOTx7Sc2_7PCewFqGL2yFB7DQRmWj_jmERyePfxGyLKRZfWLo-rXS6wRiQmIV-r3yquTpWK9H5jgKKOhNBUHl_2oHGdCq9wVqJf05BrhR4d1eHTquHnYMBcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 22:20:19</div>
<hr>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmdV0K1cTjg4Tp3ThMH4SZmCM25-sdFKHPpRAKMmaMd-yI2p9hO70Nvre7kToiCxtlAWWcdh3QT9blRqCPwGVTl_wxxJ6Dmi8DLTqdcMepwB3f8IiBpyYwcbUGkL5T2ZSSXTa129P7-AiX5aGwDAU_jFE0h81ptJbaCv9KYnt2cmn3B92nAKVk2TgkM44op9elJE8ZWFWBRXCM0QV_dgkRR9ewpJ09fZn3rqMseK2NcmhP1hc-I-E53FlZ8FJv6n_WG3CrYJFPDX8cARKCE09CWOQkoU6aZ2rw6Deq7jIyrhnj8KISoIhDtfFf2Xe8hrf6cHn8hgx02zaWSRJzXaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سطح اختلال شدید
GPS
تو کشور‌های خلیج فارس :
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/135462" target="_blank">📅 22:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گزارش‌ها از اختلال شدید اینترنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/135461" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2GiiwfCsf27fUOAsdJffWYp9PVpMFK9voMeC9YDJAwdANn-YSFTP7X4R8OdUIxrht6PzlsZqJvHCFxIRfubF5bjv_deqT7Igsel_e6REAUqfK0dFCjAP_RzJq8E5c0BjSoCDygOTpXWrV88AI9SsUVdnYPsvNmN0DxKdaLgwNjbQYdXUoM63fkq2zyOWRNvmEWbAI-nQdMsGd5ADoAto0V9GCyqOd3LMyoGx_RP1j8F9D9M7p0FLYmTqtomVNKCvY2mvmohvM9_ACAyErmTlrFTzs7e2P6xb-SvV-KwaZDWh8pG4Tao6Xgb8Y1AQMAp_ATDj_52nTD0DtEQaMpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست : فداکاری‌های شما، تنها باعث افزایش اراده ما میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/135460" target="_blank">📅 22:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما:
اگه اینا بیان جزایر ما رو هم بگیرن بازم دنیا به اخر نمیرسه که.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/135459" target="_blank">📅 22:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وقتی به اعتراض میگی اغتشاش،
به جاوید نامان دی ماه میگی تروریست،
مردم هم به حمله ترامپ میگن کمک بشردوستانه
🤔
چیزی که عوض داره، گله نداره...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/135458" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
استانداری هرمزگان: دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در حاشیه شهر سیریک و جاسک منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/135457" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wx0upt5R8nlXOJ7RXHwgzhiBeDZI0hcSaoYZOSYhxFpUhtUrFIj4td5ZvbqN983ic5P1YLUv1zHcECK1iRnBHagPSOYjoEa0i8FNFq1zmpRz6uo_BcB6Xg9ls20lS_uYgAYUZxGfjnGCLPwg_28iZKtZDqD2ZrtQVl9HLhQJ4HTZkZNalwuRUXT7RVaBHJdHCDBUDIW3-iIbr5mcZuUaT36f220sJrvxVLZCP6U-zhIRsVduoW9U_2SZ99Dke-pSodYJIY6FFRPmVG4GwojnGfPcizT8Ur7mCoAxSlqA4OO3BR58W0pR0AFOrv5finzDIKQhXAZ2VtXp7k5ibbKJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود از شهر جاسک در ایران به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135456" target="_blank">📅 22:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از شلیک موشک های بالستیک-تاکتیکی اتکامز از سامانه هایمارس به سمت اهدافی در داخل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/135455" target="_blank">📅 21:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135454" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sih38NvYYzcl2QoXn4FQwK-N1lgV12keqh2RwTgJayadDX_u_07whNk9tu1EruPyb29FjIqKm3MFzml5WD1W1r8ldl97DZVaydc1aMF0SKji7qi24ilezYj94JsI54p8O7f30Y9l84VjYPgGZhD5k_uzvCX_9ZUoZQ6-u7FEibIC7jaT7RDskpcXr_zVXmnUA5YZ004_AsDP6d01KIU17FZYamQdq6r-S0-qr-MSBPXsqYF20O4wyMO2R1Wzel_i__Ln6OQ-vSRatgCVie-Pp0gW9zcHZTuUMnnBSSJJGBCq7rKinlLsnpWUbhayEaWsoNnf76HUGUmT9V_imV6vPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ هواپیمای سوخت‌رسان آمریکایی اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/135453" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/خبرگزاری i24news: نهادهای دفاعی اسرائیل در حال آماده‌سازی برای وقوع یک جنگ بسیار جدی در کل منطقه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135452" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / رویترز: ترامپ دستور شلیک قدرتمند در ساعات آینده را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135451" target="_blank">📅 21:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDSPnfkxpE6jQavJA139mxfCItzgxCJ6GKK-qmby289D6grrlrncaWw9HsSCGYV9df2p1AU-JEBrYZwaTMVSK3nyE0aM7J_LikIhXknSdtv2c6tQYuXS6jO3bjg2dQeKZ5nfiBNovo-KF132XSmImR0E0b925N0rVKhFgbEybVdt2i3dPVaItcd8quWGRIuaD521qtVykC5dbAITJpI7KhMbeScSLaSyunPghgTqXcIufappMiWoVk1aJRH_U-wRDoSXUBzuIqdcEng3KhVqguJ5l5mVEs-f3Z0HcM08vT-gcfJ0w5Szp4w1JIWmFoXsDlMhzrAIMOFzg8aDb-eeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DbZBcjFYM8JJrNCwG2GdIhYhQvWxMZkF316N5owk2ogF71Un67QHGlpf2VBjM4EBS48BOXl4ZhL26MD-hMt0iqOTLu9BLyige-UNywuX0GxBI_U_ykHGTEQh9Y7e1UdEAbajxapr2qiIyDD6BJZaHIpMHYo463WlSWbttK3PSGaHR1qiE46FTbTGqa9EhhmKTNMpmkOZQPilG9uPzr9AzOo619GwpZ6ahft85akIcoqjeePLu7B1J_4h6yLzFyeIiG-bXzoJ1pOUF_ky03Bz6i3jma1vXR_KNt3oJksZo4-hNsrL9Tg1LtvdIHhiOpv_GAgOM6D4hv43U3JIFfgLxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای هشدار زودهنگام و کنترل هوابرد E-3G از عربستان سعودی برخاسته و هم‌زمان هواپیماهای سوخت‌رسان نیز از تل‌آویو به پرواز درآمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135449" target="_blank">📅 21:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌های بالستیک ایران شبانه به پایگاه هوایی موفق السلطی در اردن حمله کردند.
🔴
دست کم دو اصابت مستقیم تأیید شد، دو نظامی آمریکایی کشته و یک نفر نیز مفقود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/135448" target="_blank">📅 21:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/135447" target="_blank">📅 21:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر اختصاصی که میزان تخریب گسترده در کشور بحرین را نشان می‌دهد، در پی حملات موشکی ایران به یک مجموعه استخر مورد استفاده سربازان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135446" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135444" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135443" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmA2v7UTPvoRSPI8PBqktnQyPIcqlBi6oUS6FkacP0VeVrsnu5vXx6YhTUHjb6em2OGbTdQRffztUsJ1C30SKWZaeoFNWtwmikQNYiL5AtILhAxPilnK0A8LnAFgGoXyJbvKjVJ9goZ6SRPvqPqgqjEccMLoNRQc9XgAESVVzYZXtOTrbS475TDVCKevDyIQvR9_UZnDtyXJqhyqXJ9g8fXOoSPi6GvjmkutujNQGc5OIp0WsNd3ahExeiVYCuOTHechaHzuUGL48-qKfH-V9nDTGQe6xqONX2WvPv2gHk2Vbd1DHYxGPSbSLK3jaHIipsOHGlvlhem65ARu_HDJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی روسیه به قطار مسافربری در زاپوریژیا؛ تلفات جانی گزارش نشد
🔴
رسانه United24 اعلام کرد در پی حمله پهپادی روسیه به یک قطار مسافربری در منطقه زاپوریژیا، لوکوموتیو و چند واگن این قطار آسیب دیدند.
🔴
با این حال، به‌دلیل تخلیه به‌موقع مسافران و خدمه پس از اعلام هشدار حمله هوایی، این حادثه هیچ‌گونه تلفات جانی بر جای نگذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135442" target="_blank">📅 21:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تعدادِ سرباز‌های کُشته‌ آمریکا؛ از اول جنگ، توسط ایران، به عدد ۱۶ رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135441" target="_blank">📅 21:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری / رویترز‌ : خبر کشته های امریکا به کاخ سفید رسیده است و ترامپ بسیار عصبانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135440" target="_blank">📅 21:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135439" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
استانداری هرمزگان: فعالیت ادارات در روز یکشنبه با حضور ۵۰درصدی کارکنان و براساس تشخیص مدیران دستگاه‌ها خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135438" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135437" target="_blank">📅 21:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از تجمع مردان عنکبوتی تو تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/135436" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135435" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در خلیج عدن ربوده شد
🔴
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی تجاری در فاصله ۶۵ مایل دریایی جنوب المکلا در یمن، هنگام حرکت به‌سمت شرق در خلیج عدن، توسط افراد غیرمجاز تصرف شده است.
🔴
بر اساس به‌روزرسانی UKMTO، کشتی پس از تصرف به آب‌های سرزمینی سومالی منتقل شده و این رویداد رسماً در طبقه‌بندی «کشتی‌ربایی» قرار گرفته است.
🔴
تحقیقات درباره جزئیات حادثه ادامه دارد و به کشتی‌های عبوری توصیه شده با احتیاط حرکت کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135434" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IZsXetjzfHuF5_enEVYzDtlgbb1q2vQu2noQgqs0WUt1jtCuyWy6nAMNNTpRQiEYu2B_kD7zXG2H5m4Kaw8hoQoH43kYTyt1PeL84JMjrfBhY-3moRAqV9T77TZw-aAEdUipB0L2_vBAKpKckxh2y8zwoJR7P8X6hC_h7lDFH1pxtxZFOtg7XH_4mqTMOpB83fjmJyXaX3ny23Qb_xFL_C3KK-A3rs3p0pvPJheCzWS0zQ5rqtk1DRfMztExhzKHds_1UACB819Cw3wOzcbgw-8h2e-xkv6z0SW4gEjpq3jsWrx9ch0wlqSPRz_-L5MVTfV-vJvNeRMFQpJv5y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135433" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری /ادعای کانال ۱۳ اسرائیل: در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود:
هفته‌ای سرنوشت‌ساز در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135432" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QM4lOny5TgZZkOSz6K9z45EkH3UI60FaqNy1zGrP_GQrE-MzBsTJJpByZmacjFk6lxtTjT438S5-x-xu_X0EkTAJyRACtcLR5eTmJJCXDdi5ReNZxnRtn3kgsiF1EM3Sc8psz-wVtZnXHYeX9FR2w__CxdoPjpsvAXCjjA9N8GORmKwXzjO0a9q_WArKWlGM2746qoJeZhTrV5KqXi6XMRQDe-IBvUq6ONRs5ssj_-LsRlWmAerWDlusCiVbz0mtHvlgHncQbxIxC32Co_sQHuktThkXcsUn5wHb7fUkJGl2GX4y_D3EcallF907JpCHK9j5R5FbpPE4yx3NoVcHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلار در آستانه 200,000 تومان...
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135431" target="_blank">📅 20:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری/ گزارشات از حمله به یک کشتی دیگر در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135430" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/ گزارشات از حمله به یک کشتی دیگر در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135429" target="_blank">📅 20:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0IKfupj5ui9nScmO0_YbQVAO8zDqZEClM5pUV0s92jCs8ZKgs4z24KG2iFtkzrL14uj91qsM8Ip1sF74x8odR5I8tJq5abXq9hVeWiS8dX_cBeLWGwUxtXJRAmqTyjiwAy2nVn4ZStTzTlD5apNe7OvpcEnCCjO0M2N2UM8PbD5WVPrsGUOAeaTWGkA0dDLUU75FGoRzdt1goRNjnFuh7xVF_tJU2St7-uoiT1E9o2I6xQVrTbZmYGxWEY-u6bqR7szTcQ1w5sekVwz-nu9tLgKfZMH16qlxa7NSu9-XYvJ83yn-R0BZ3fWe4JhdUe4qePKckFQ9kdMRKGe7Qu-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بخش مهم بیانیه امشب مجتبی خامنه‌ای: با توجه به نقض آتش بس و حملات شدید آمریکا، یه درس فراموش نشدنی بهشون خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135428" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=Cl0actOyISjKId23n-YuR2XF3gsqQusQGPR3yi15VLxo_0kEJBiEzobYK2n-TvOBl3salL2qrzZf-Zca3twQMdh5R5jajlqY_YmkikGdZMDNyL0Wb0HYh4kp3TtyA_q1yCGe--df4Byk6vr-qJnC06fReZjcRsFgmH3UXTZAotGMVSEc6hkavOmFBNgfRhjX8I4LCRn5BMtnQCPCVH5DexYgvgUhCKqxBlSff8Mr8TqRU_6R_6zV4mC6f76MrzwI8crE4BAYnJYXW8DpLsz-TrCB4s5Hx82Er5nK4pKB-iWQskGCbENLLYKdozFmV22fZydAWbejam77DMFxelgyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=Cl0actOyISjKId23n-YuR2XF3gsqQusQGPR3yi15VLxo_0kEJBiEzobYK2n-TvOBl3salL2qrzZf-Zca3twQMdh5R5jajlqY_YmkikGdZMDNyL0Wb0HYh4kp3TtyA_q1yCGe--df4Byk6vr-qJnC06fReZjcRsFgmH3UXTZAotGMVSEc6hkavOmFBNgfRhjX8I4LCRn5BMtnQCPCVH5DexYgvgUhCKqxBlSff8Mr8TqRU_6R_6zV4mC6f76MrzwI8crE4BAYnJYXW8DpLsz-TrCB4s5Hx82Er5nK4pKB-iWQskGCbENLLYKdozFmV22fZydAWbejam77DMFxelgyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک شهروند اردنی، یک ویدیو منتشر کرد که در آن موشک‌های ایرانی را نشان می‌دهد که به سمت پایگاه‌های نظامی آمریکایی در اردن در حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135427" target="_blank">📅 20:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCr1H-kv45GTBscjw0FNBXiP_C0rz8cOERzsfAqfL_pGs0kFUynisLr975IPSsE-WZ45-Hc5MoE0GG_fHRM7SOQXZeEWQWqnftE4wdaxCCvJ8YMCdWdG2lBi2AlLHdhrQ5DevO-k2Yb66uLTf7ORnWqqFYyvvxzqqW6tyu_lWE5SAYaBwtC9AaBdurMyfnlFrirPyJFmoQA1oELoCEPXFZM7w6DAg2zMnJuA1om4YbSgt0KKYrj2xU6MGYfAgTKViiVotwZBZ7n2X8i65n6hcQVo5iHGulyelnTO0Oow2m45xrMGWIGZyGBJBLx9EXFtwOyrS-otk6-FmvWIMwavFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز، تعدادی هواپیمای جنگنده دیگر در پایگاه‌های نظامی آمریکایی در خاورمیانه مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135426" target="_blank">📅 20:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5_TkDQHWj1x1RDUZR2Uh534BiiivVidsgKoBqPubK0YRsqghnISlpBw31wuN8CVnWCIHTnWuIZz-0m8Q6N-0UuqUNZEJE0zqChsWJPL7uCcSfJYdWYnsyu37nbg8y-MizBgq2dg0PJ8uXJRQ5caFl71oLyou5RGyl0NM2dgup-AfA9UqqpoOSXcP-otibKVJFhLUn8EccngCdeHDG5MFzFat3W08NV-rPQcLaDAyaFq5UyGwMBN43_JkhxaAIEDgL3SSFQkwTUpWDVNdgiZ1d_DoKuPT1iyJkFintEeSWVpRf6Wi_qkPyigyl3NmkHFXyA9rDcJpRBJHTxVedR8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر از ۱۹۵۰۰۰ تومن هم عبور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135425" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
استانداری هرمزگان ‌از شهروندان خواست تا اطلاع ثانوی از تردد غیر‌ضروری در جاده‌ ها و محورهای مواصلاتی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135424" target="_blank">📅 19:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حملات اسرائیل به نزدیکی تپه علی الطاهر در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135423" target="_blank">📅 19:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مقامات آلمان هشدار امنیتی صادر کردند
🔴
وزیر کشور آلمان با هشدار درباره افزایش سطح تهدیدهای امنیتی اعلام کرد: این کشور وارد وضعیت «تهدید بالا» شده است.
🔴
بر اساس اطلاعات دستگاه‌های اطلاعاتی داخلی و متحدان برلین، احتمال وقوع حملات در خاک آلمان در هر زمان وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135422" target="_blank">📅 19:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران از مرز ۱۹۴ هزار تومان عبور کرد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135421" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: «ما بار دیگر تأکید می‌کنیم که هدف قرار دادن تأسیسات تولید برق و آب شیرین‌کن در کویت، از تمام خطوط قرمز عبور می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135420" target="_blank">📅 19:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
عربستان حمله به اردن را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135419" target="_blank">📅 19:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od0zTfF57CvNQiUDY_An4RAO2MJ04iwbCTL92c5qCTTV6692YS_9vtPp1-xKcs09KwemF4VRfYiTi-DLSyPl7nvMPimioZZxrMu023y7AbveDAvEYXkIusBI_11dHfGGS38QaP6Rq4OpFqOJgSQKAJwQmldVFFP5mL9LszXdMr5Q1b_uR7-4yHGoHsw3W7tZR_wK4HSIrZQgQCayrilXJT1Q2tonvRJ0clzkCMzBmkwzlqwyeQrrBVszlUEJX9-D9bkwHtTw2GreFs-TXKLfxSFezCZA2HdY_UkGWeUnRx_cskTio91z6YK3zAmlOpc68AtiatVTJmrvCCWFlx-XoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت خبرنگار بی بی سی
🔴
گوگل مپ داره تمام نقاطی رو در کشورهای منطقه که هدف حملات ایران قرار گرفتند کدر می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135418" target="_blank">📅 19:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اسماعیل بقائی، سخنگوی وزارت خارجه :
قرار بود ۱۲ میلیارد دلار پول بلوکهِ شده آزاد بشه، اما نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135417" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مقام آمریکایی: ترامپ عجله‌ای برای ضربه نهایی ندارد و چند روزی‌ست عملیات دوگانه‌ای را آغاز کرده که شامل محاصره دریایی و حمله به مواضع ایران در نزدیکی تنگه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135416" target="_blank">📅 19:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیویورک پست : رسانه دولتی رسمی ایران روز شنبه به مردم هشدار داد که «از پایگاه‌های نظامی آمریکا فاصله بگیرند»؛ این هشدار در حالی صادر شد که تهران حملات خود در منطقه خلیج فارس را تشدید کرده و رسماً تعهد خود به تفاهم‌نامه دوجانبه با آمریکا را که از همان ابتدا آن را نقض کرده بود، به حالت تعلیق درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135415" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
چند سرباز اوکراینی : قبل از اینکه پهپاد انتحاری روسیه به خودروشون بخوره، از ماشین پیاده شدن و فرار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135414" target="_blank">📅 19:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
العربیه به نقل از برخی منابع آمریکایی مدعی شد دولت دونالد ترامپ در کنار حفظ فشارهای نظامی، به دنبال وادار کردن ایران به مذاکره یا پذیرش مطالبات واشینگتن است. بر اساس این گزارش، آمریکا از چند روز گذشته حملات به مواضع ایران در نزدیکی تنگه هرمز را افزایش داده و هم‌زمان محاصره دریایی علیه کشتی‌ها را بار دیگر اعمال کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/135413" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
استانداری هرمزگان: در ساعت 12:30، 16:30، 16:40 نقاطی در حوالی سیریک هدف حمله نظامی آمریکا قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135412" target="_blank">📅 18:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep_TmedS_zWEAfB58rJ3qYWp6zE4YhCFaXjNzimPHsy-jJ2zobFwL8w628YnXHXsRIyuJkpcbCW0Jfdz-4obAs0Xm6s4kKapGOxxS4H2_muvFseIcAAjF_0TQPu_73LnKLrPn3_XeD5Sjzh68CuyUR3yI5z2Mx0EYQpOW6DKBUdyl6msnsJpYQrxNS3RGPcoAYpgLy1oWQGvMlGM00H7W2R9xmCWXYLyJb2MdOTzJWyaKP2Uc71z9XHvl90d_OhheKWSqtzkX0FNqh-YBESDJgd8fpdVDbzR_3bgofUC2f94RQr8Ju2UGBXUsuLnXQ7gAZuABdhsuCgeNhQff5_Dqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: اگر ترامپ به هدف قرار دادن غیرنظامیان ادامه دهد، امارات متحده عربی هدف بعدی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135411" target="_blank">📅 18:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9w2b1ZxsYW8lgCPF70aZOCLvx6G1q1UcnMnZSQh7CijcDLoyIYm0Zu2cQs2wVfQmMaFLhnzf9AliStBJRxgEWJOc3v_QsNI0KcrbdBzrzKixr706a-pTJnD33KMfle_F0sCvymtMmQYlKwZznGe1Ih7RwcjyYGgiShZL-54-tixdvl4MK1Il5BPasIVthnQ-OIGjy4SF_cn4nqmDPoA0urUT4zP17NRmDC9hOKDuSM-cnHVF9tJsTNowlB8NJtMlIct2vQascI9efpANqOcm5zPIDPLRnEKV8bSiXBxu8MVRbql9jSPMikWXNJ_LsP1X6p29wTuMumYjs06NzqRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ کلی هزینه کرد که پل تو جنوب رو بزنه، اما بخاطر اینکه رودخونه‌ی کنار پل خشک شده بود، مردم یه جاده خاکی از همونجا درست کردن و تردد میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135410" target="_blank">📅 18:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: توافق‌نامه تفاهم باید محترم شمرده شود و از هرگونه تشدید بیشتر تنش‌ها جلوگیری گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135409" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
امام‌جمعه قزوین:
بازماندن اینترنت بین‌الملل در شرایط فعلی به‌صلاح کشور نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135408" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipyNjRnxfNapU1tgMmtqPtnL120805k_hy2zfSABcU9qyvVl4G06DmpNtQP4A8BEbbdat6K9U2vpiSKA6wBOJK6JSktq2dq591UtjnPo0hmVZ0HUvh8LvbUk0jd43rNK27XQbTjdCExM1WQqMdaRL0M_zZASdoOqtLOyIwWc411l1Gj5w6gvQrwgTvPWZ6uE5xwdDi0340Ig1Hlwo8EGcdebOdvCiLx4wnixwLFgojDYLLvBNk44BfRP7F0d4OLOMIeQBePghWmKzlRsepZCfHBTJTwdRYuM_F_ti77B6XVFJinl5a0qTBAOYPsMfU5QlLkr5J_azCJmriSCSP--XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز تا همین لحظه، ستون‌های دود از کویت به چشم می‌خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135407" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
به دستور قوه قضاییه پس از پایان جام جهانی اینترنت قطع خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/135406" target="_blank">📅 18:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135404">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به دستور قوه قضاییه پس از پایان جام جهانی اینترنت قطع خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/135404" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135403">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
انتشار ویدئوی بمب‌افکن B-2 در حساب ایکس دن اسکاوینو، گمانه‌زنی‌ها درباره ایران را افزایش داد
🔴
دن اسکاوینو، معاون رئیس دفتر کاخ سفید، در حساب کاربری خود در شبکه اجتماعی ایکس ویدئویی از پرواز یک بمب‌افکن رادارگریز B-2 نیروی هوایی آمریکا منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135403" target="_blank">📅 18:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135402">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO8LkJ5rMieXXkUd9lzPXmDKCniD-R2mVoTuJOJw6W6Mk31T7Jr3M6WaQpt5FsoXb0G-Hq_zQ-1-c8ebmT1ArfQYTUvEu_hsBzuYHjnx3mW9Y1Cz_XidFJ2i4KqovsBuMG6BcWwv1lBWkB-dOkPcFeQknVrrGuMDe_BIndVIWytkOzRu8JNAjGz5Jphzs9B-F2DJR6iwxLYvE43z3kw-Tw-GRujMiUJ3j9e-Up5EuuSWWGO1-gc3yfmx5E9MDEELL2zb0Roeg3JLFycI8_S08EVMwv5d1y19rqRw0GQ5pSv0Fqx0HS6FzVJtuEeYAiDNHdbOBZHKIPPyzNPGLlk3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدهی ملی آمریکا به‌طور رسمی به رکورد تاریخی ۳۹.۵ تریلیون دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135402" target="_blank">📅 18:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات آمریکایی: دست‌کم ۱۳ نظامی آمریکایی از دوشنبه زخمی شده‌اند.
🔴
بر اساس این گزارش، حداقل سه پرواز تخلیه پزشکی در روزهای اخیر، نیروهای مجروح را از منطقه خارج کرده است.
🔴
به گزارش آسوشیتدپرس، از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، ۱۴ نظامی آمریکایی کشته و ۴۲۷ نفر زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135401" target="_blank">📅 18:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTuqGLC4qwofgPVJkW_uTADGO8acOuyYaseWvflXnQgIFQqV0YLsCb0fapdxkOfbc1X99zcgQsg6vxI3eSmh4JqtrmMzRQmjt0sGTB7WDE_bLhNzet7KWfWx5lGw5Bqb5jgSV6Q0mOMcOOBjM0OWiVbzdFo7INQ7CguIlaLss0dl05HT0ql3PyCwXTHI7fM_Ry-SLo52bNF5dNCRxvxjqCY_8B9owfYr1nxX2BeUmL0b7v-Vst1lYlnSYaQw9iqGBOSUbelbsUP2MkaDZaf8yjKsARRTL1JMEFb4cgQwhuYLN595fbLdyHIVdIDTxPep5TOQHaB8Zr-AkXSsFhRusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر هوایی نشان می‌دهد، نیروگاه شمال شعیبه کویت که یکی از مهم‌ترین تأسیسات تولید برق و آب شیرین‌کن در این کشور به شمار می‌رفت، بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135400" target="_blank">📅 18:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJJ9M1oBNfApS1Q7EPodHstnIdtHaZN7XwybFqZJXkZ6GO2heaMOQ_9LXa6JcPocGG6BvhZzv59RG0k4wD_uXijyucTRSLmQO4eD1LJQG7yD1jg-wZ9C4s4PzUi68xgUTt6HKqMfFl1IyHaPL3gz8fDjsmG3IwB_9sixDOnLNCRAegAYcBLRSi9Y4FBc0hGKlliH7abGpveJBvE1s1JzhCfau1EMWh3Yfw1Pkhg5o0qBeF89zce6W0PEMRUF1KM1a_zZcNiUIq4Ra7TuNLFV0zSwUxMZnHuzGG0ioFg5dHimn5iNWbA1vQn7IE5Gt7BUsoEulqoHwRy66V6odu2vqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله‌ی نیروهای هوایی و فضایی آمریکا:
پنتاگون درحال ارسال جنگنده‌های
F-35
و
F-16
بیشتری به خاورمیانه‌ست، اقدامی که نشون دهنده‌ی آمادگی آمریکا برای گسترش عملیات هواییه.
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135399" target="_blank">📅 18:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی های نوید کلهرودی در سال ۱۴۰۳ که دقیقا داره به وقوع میپیونده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135398" target="_blank">📅 17:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس : اگر آمریکا امشب نیز به ایران حمله کند، فرودگاه های دبی و ابوظبی در امارات را موشک باران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135397" target="_blank">📅 17:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عوستاد رائفی پور :  اگر ناوگان امریکا رو غرق کنیم ابرویشان در جهان میرود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135396" target="_blank">📅 17:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e079109218.mp4?token=bUXYcG2mmpWLOt66yuLlEcIC9PtnSxHQvDuuuVcPvpNXnK4ultX7DRhTj0OqwEnN50QyEtpPqr2S-dEnX0V-Ck9WOp6enqA1TgoU1aNJMAKmDXU_lhLzfQxf0R5IpqqOQcGRBcLurncEAoBp2CIMBJaLDWRT9UoELl0eiiK2m1y84kMLyjHTWu15RPh2fFqqBJtPUY7ugpVNIHrxb2cSfrlLWEPswfvxM8kjCUPpqPZy22LF6M03F_VZTBgIYq3TUOSfLUhgSkln2dicJTN9qONXgj3FlSSe3_jfUeuJB0OqrPrQNjAaDMhsfM5l0dhlLVRuvcAM0LAEownLCdqV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e079109218.mp4?token=bUXYcG2mmpWLOt66yuLlEcIC9PtnSxHQvDuuuVcPvpNXnK4ultX7DRhTj0OqwEnN50QyEtpPqr2S-dEnX0V-Ck9WOp6enqA1TgoU1aNJMAKmDXU_lhLzfQxf0R5IpqqOQcGRBcLurncEAoBp2CIMBJaLDWRT9UoELl0eiiK2m1y84kMLyjHTWu15RPh2fFqqBJtPUY7ugpVNIHrxb2cSfrlLWEPswfvxM8kjCUPpqPZy22LF6M03F_VZTBgIYq3TUOSfLUhgSkln2dicJTN9qONXgj3FlSSe3_jfUeuJB0OqrPrQNjAaDMhsfM5l0dhlLVRuvcAM0LAEownLCdqV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم تشییع جنازه ۴۵ تن از نیروهای حزب‌الله لبنان که در درگیری های اخیر با ارتش اسرائيل کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135395" target="_blank">📅 17:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
بلومبرگ: عراق مسیر زمینی سوریه را جایگزین تنگه هرمز کرد
🔴
تنها در عرض چند ماه، سوریه به سهمی بیش از یک‌چهارم از کل حجم صادراتی خاورمیانه رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135394" target="_blank">📅 17:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135393">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: به خاورمیانه سفر نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135393" target="_blank">📅 17:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135392">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtC8HvAJiz-RHX4tvElllBZ0-ykiw41pZObmEVoPNDWugjmtAqyuGvAedZ_xeiY84je7vaiZ4WwLcXoFD98gV8_6UeFgPPuyY3EInEU62uOCFMFPh1XHlywjdJCUr6T4sGR_yrfB3lVJgO5Q0LNlTH4zJGSJd7F3aM7__vTF3DKuyFNzJWnMqL32Y3UMdOWUn5eNtU_d7XVyLfvTBJI8LR7I4444wkMnaRZT48W8ACSW9u9i8n0p5KoNFJMuL_JDXHy5Hv7q35ihl5EEsgsnn-wX1J1D7JtAYLTCtVN9JB8aejI-23pCd1Qr0vLHd9K7isB5JTZX3kY2R5SAczi8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: تصمیم دولت؛ نرخ سوم بنزین: ۱۰ هزارتومان
🔴
برخلاف نظر قطعی مجلس و در مغایرت کامل با ماده۴۶ قانون برنامه هفتم، متاسفانه "سازمان برنامه و بودجه"، ایده گران‌سازی بنزین را در دولت با قدرت جلو می‌برد و ظاهرا قرار است از ابتدای مردادماه اجرایی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135392" target="_blank">📅 17:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135391">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/21a6e4c8cc.mp4?token=k5J4JV90k3czHrlwvBufOAAbpVVP9WEjoDu1Dc7RTAZ61Y9hyhk0XdOUqyvDe2B9RIrn9uVYmeFR36Zdn6iAEwWZAwppfwgnLqgEEVDsadmAADai0OD-m-o7R0DhNWxf_OVGRVEYJ4Z0giXFaIAtkHA_RkULq5UBt92xZXDMW1vVu_yDwY3yRGbDCm8pGMFnWZOmqwJ-9AnmsvDn13FXghcU8BkTAPyMGIOfLf2kPmi1pniE2C_trCFDsP2Wlp0IoskWE4zBQuGDAQE2UHBVm7fc1o0B-zjLG6va5_vmnmi4fUv10urYe7RE-oucoWQMgIRsBtHd58H4rRr-pTXBhSJiVE3kjNXlsyw3SDyfgjOtgR7f8VZAxNDgKG66UF6ykAJ01NLtl16EwxQlAvciJZcVRt1xL6GOEejxGluh6R-In8UkUKFfhl8dKjzs79GO07jPXGFQqajcPk57_uFUrFXyG5Z-NbhMWotOcrR1JqD9yseSpf8ZpY05brPP9L52KBxFwA0m2RhRCBBPvH4-GOJ3EjcxRLA_NeBsOVMUfOgAJ_0qfeBQAJPYY5cxn59GhePYaitoJ1z23wl1BENlpGtcysXJ_oEp1PbBAnNP_SX-ucIiiE-1RWHcw40ret30B4TNElZxyLefsAaCaqqKvbyRsuteBbuiv8JOv9Xt218" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/21a6e4c8cc.mp4?token=k5J4JV90k3czHrlwvBufOAAbpVVP9WEjoDu1Dc7RTAZ61Y9hyhk0XdOUqyvDe2B9RIrn9uVYmeFR36Zdn6iAEwWZAwppfwgnLqgEEVDsadmAADai0OD-m-o7R0DhNWxf_OVGRVEYJ4Z0giXFaIAtkHA_RkULq5UBt92xZXDMW1vVu_yDwY3yRGbDCm8pGMFnWZOmqwJ-9AnmsvDn13FXghcU8BkTAPyMGIOfLf2kPmi1pniE2C_trCFDsP2Wlp0IoskWE4zBQuGDAQE2UHBVm7fc1o0B-zjLG6va5_vmnmi4fUv10urYe7RE-oucoWQMgIRsBtHd58H4rRr-pTXBhSJiVE3kjNXlsyw3SDyfgjOtgR7f8VZAxNDgKG66UF6ykAJ01NLtl16EwxQlAvciJZcVRt1xL6GOEejxGluh6R-In8UkUKFfhl8dKjzs79GO07jPXGFQqajcPk57_uFUrFXyG5Z-NbhMWotOcrR1JqD9yseSpf8ZpY05brPP9L52KBxFwA0m2RhRCBBPvH4-GOJ3EjcxRLA_NeBsOVMUfOgAJ_0qfeBQAJPYY5cxn59GhePYaitoJ1z23wl1BENlpGtcysXJ_oEp1PbBAnNP_SX-ucIiiE-1RWHcw40ret30B4TNElZxyLefsAaCaqqKvbyRsuteBbuiv8JOv9Xt218" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتشار ویدئویی از عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/135391" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135390">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuVDOaXl_S1kQInErzGDKR8E9uRxtqddHE6Okw72KiQlZ_nV2_m-GI4izfhxfej7TblV2FSnyv1ocIMBI5D9JO4mHtaoBbEDaNavNtbqVdXre0JcXwAd3-d6B5Vi8Evfqi7jEa27xattjCvTz3fHEMZIeJIgqFsp4cEmzU617_D0plE7_E-yI3e89xEPUdB9XVTot8xk2eD4Y7tvp6Fi6jux35UgEP-m4HxCCsJP0SPswAhMpu2N6dFfsZMtFlq3AoXh8f72ymheJvEsxTPkvKyvmY0_W0MWeP5vk5u4JAYlRIyCTF_xkZ_ejYt6ENfmKY5lggFCmRWal8jEDLVy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام امنیتی
ایرانی به فارس :
اگه آمریکا به زیرساخت‌های ایران حمله کنه، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135390" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تسنیم: مراسم بزرگداشت آقا تو مصلی تهران تعویق خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135389" target="_blank">📅 17:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns48dFnwIxyqVB_U1OxNch5ceh2o-LhhfUEPbfhsemCq5UHzT4HhCnPxqclFXxFBFu2W7_OBtaSjZm-rV69SLbe7VQNV1nTI3DgJWFFnsVrgnXhhqZGr54JThuBZgJLGeAh_hftH1bij6RsRrniJao6l-KzyI6cPqqEfeKtbo9FyBxakBUaqfKSbFE998UQ-AdD1BqhPE_mdUlSidbNLPsPdnP32-0Rky0oxGi_JY_Q98iD7A_2ZjialwKdOFwTrplkwlmNF87J1UR7a_XtyV63voe5LztHE3FultPqq5pkNtyHZG2BOXMvErH0l2UFOyMP4mqj546oY1wvPamuyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135388" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB6neZno4O3R_Dj3zRMrEuJCJ_E7jsaqC-IapY8RPoRD4RDwxhZDQe-3why1-r38fMpDv2TlTx-dyAGbQcerBcTln5euC7S_4z2KxqKadzgc6yk7j06Z_uzAshvrx24DuZVXDvToVwI0F8eO5scwEnTgG7wEwZ0gKok_pLeR3o6xWxN7vWqoiaCRi48pjZwamsotbHDMxvZitcQjSvbuWARtaAM274duDCR1caCK1QoxC4zUjPmOCIZIf6QuVd879TaOOoLViNPXB932XPqwoQnhKkbcesxy_Y2UoD7iDWwKQcZpeg3nKKgb8JpwyLwWjppOJlX9w4-Ze8kbwwdz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولید گدبان سفیر اسرائیل در سازمان ملل:
"موج آهنین در حال برخاستن است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135387" target="_blank">📅 17:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K803vtekASjHP1A41mCPo9WQhvrXMefjZGPtmFsG3BUHYuYVmXmbOk-_en_yWxg0jKwuBrfdowH0pvIPH0z7e3rFc8kuqmicL1xMLOfgfrnIcoX7OwHVREJo8aLxlBouECD40b_H9eeNq2Rb2WD0biB6yC4nm7VJRLsp-25eqmiLdgtKg9esyGPyszTVjgB6YIyHlhrhigrcePmvtHWxKRGZYaHOapXN6tb_5whsNwKTFSmLXE1SZ9IILGaizRD2qK-x6-jqG2YbPSx21XJ68KkluPRNiy_El2h1lkCwBzd6KqrEE4mMZUV0yBF1S_kuPSN2hY8o2t1xcihdVY3DTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qt301OLL2zybx2zopp7l7ki1bDrrKUdCTA5Rl_tVdd3B6CdxjXQ9tBbcJ2INnJkewFRPx9HEipIvYZGRd2zV-HV-NNbQDQbudwcHjNMOR3kNIgijGKbB3kya1FyKNrAg-aXGWVRy2_ErH7UKmoPw5Eh4GM5uvhhMkszOMFeojQV0FctRmcrmjz24ahY_f2qYPd5n_VQGN6an8i2wFaNBb_uD8Z-uhf7QZVAxew-4TFNOWOWrlR8IszYjEin0dKyH9YChnHW1wLh-QaYNa-gzsyPtQAc7d_krVI2_907c0RHKkSj-dg6VMhB9eraETrdWuZIGct4nnpeUHs-6Fkjowg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از پل جاده بندر عباس رودان در زمان حمله و اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135385" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGQyqF2aPVktgIOjdVCzUQr1YKBk-ZiqYrUaez-cNE-rqSoQcdBuesl18r9MwiQRKSGj_dDQGXniOsOECoLxaLlONAxUhzXhjRUAu0BAlxAtgF7fjHwsBsDpy8EsEbIQ9TCSFaro600is8N0pSEDRsQBHRniS56e6Gl_8TFTdT6xFdkl-JCqM_bsqPq5cy_ueWWKRlFa4oH1lajcTTkZDGhhm6XviEV26yqkQw1FC6o0QG4y0AdOooyMWTW3qY_7djgF2-nIedvhEx4BAtQsym3DUepzIuN8E5zadO4kdcuSij3XXEdM6TCsNyl6y-ZOswVyXd_h6GQwez7hN-A-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkPl74XNxlKebhRKDVhhXeIGn6wHsuvyZ7KvhxeVsLfrGFPbVUlwEOMs4JuXDdGGzaybG4yY6tnWKOZrMD4xB-GhrEKMX1xXc734Pm8wRL8FuZYCHnzut6ezIgbfP5V6St-iDxZJJH2mv8KM99VDcfekE6i1JlGmmucpHI8XAwelXBbgbFRTpSCgPEOKzk3u32MN4NkcQ7Agm2zof2Xt38Qsx3c6qhfW8v4wcgOwpnF1PMRcAkCPgAdX1ztMNpIt_WX5wJrv8K64-H4A-ZyyyXclf1luqKGKyHQ8K92J4hxHd2LC5ctdB1gevAUlVMlqGP1jNQQnDm0p6af3HBVpKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران، اسکله شمالی شرکت ملی نفت کویت (KNPC) را که نفت خام را صادر می‌کند، در کویت مورد حمله قرار داد.
🔴
این تأسیسات در حال حاضر در آتش است و دود ناشی از آن از طریق تصاویر ماهواره‌ای قابل مشاهده است.
(منبع: MerruX)
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135383" target="_blank">📅 16:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IDpFOLF3xaXeT6PT7FWmAa5x5cLK66XS_ZSPKvZYoEeLTOaVI0mNcdbywu9qJx0BkmCyDH-pc2Pgy16j_Efb9NcKPouAJ3SDJxhSv2R2JTstazMcja5BsuuWedaj-ewoxfB4c-Is3jQcGqBxH_B1Z06RJ787XjQdNf_yBGzSDglYleHCRYmLwfq825V1B_pG4J9pE0ackq7pkMMiaUgv9cLgfCKSFBzDtyECsa0sBdhDlOO9jpAQafcP-YIO460E9a-6qchLPhsVBYTv7KtrOztblu7c6isF2Khc3yPXVTbm9KrQ-TvjuZm-9Coqk26zNxxJ8fOxhuIDEgy9KRoSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی جالب در تجمع امت معکوس
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135382" target="_blank">📅 16:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پست دستیار سابق ترامپ
B2
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135381" target="_blank">📅 16:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
انقدر تو جامعه شکاف و دشمنی بین مردم افتاده که بهترین کار انجام یک رفراندوم اساسی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/135380" target="_blank">📅 16:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/ایران تعلیق تمام تعهدات ذیل یادداشت تفاهم با ایالات متحده را اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135379" target="_blank">📅 16:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
می‌دونید چیه ؟
حماس هم می‌گفت ما منتظریم شما زمینی وارد بشید جهنم درست کنیم براتون....
حزب الله هم می‌گفت زمینی جرات دارید وارد بشید، وارد شد و....
سپاه می‌گفت جرات دارید موشک بزنید، موشک زد
گفت جرات دارید دست به رهبر ما بزنید... دست زد
حالا هم میگن جرات دارید حمله زمینی کنید
🔴
همانطور که قالیباف گفت، واقعیات را باید پذیرفت هیچ جوره از آمریکا بهتر نیستید مگر اینکه در مرحله آخر با زیرساخت‌ها قمار کنید که محکوم به باخت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135378" target="_blank">📅 16:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCBpECNGrFiOsWaDon6OBgY5d-pA_sQFimjYVG5N-HcVsNiv_mNePakh8b0hsCMYSYURQ70JzSsnsf7FunfvcDT1ydLFnBkXMaQUP-afOeu_ktHe3XTRs1T-8pQidctgem8eNLTbq9xingkFitiu-kp90f8MCMBJM8OTtV093j4edV6h3gNRMO8K4rj5rgNCdr6QcwsGqhNdHXHjqrP5jwDJtjtg-d4fUlO8LTAz3Vjt7QkyyMhkmM4DKl8WuS06le_Tn-mg8ETrvod_cPZVVVEVqhfS1vRJOr2--cypdm1cFBtd9cy9vzYOGF13-4HD7rNy9A4_7PuR6WsmCHSoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی حمله آمریکا به پل‌های بندرخمیر، 8 نفر از هموطن‌هامون شهید شدن
🔴
عبدالرحیم جعفری فرد
🔴
محمد مؤیدی
🔴
همایون چترزرین
🔴
مازیار چترزرین
🔴
مریم پراکنده دل
🔴
سوگند دردمند
🔴
فاطمه زهرا اکبری
🔴
مریم حیدری‌پوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135377" target="_blank">📅 16:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599d7cb052.mp4?token=LmIHNX8-AlTy9OA6gh3aB-t7cY-RGEwnyNAzp2uImKpgXnKRacOB02jeiWcri1Bvn12Upe99uIWszw9X9Utla9d6ZEynJmtb3RDZq1EmffYqjP38SLtsyj1HzG38Xo4MFgxoCrf3TNA9OcUC3s3_OHt-ae-iawaVqj-8bIZdpxXpGMyg7_OFHM17ta_ldFyx8hU8j_m19CRJKDgfHK-Z9-WiSQwFGror2PFx1_rukCyXvMfXm589bRYRPvrSzAxpr_42XdRFaj0tt3M5aX-dX74mRCgiRtbx1gtXAE19V4-uHyRb2DVMonc6mKM0RykKPvyCcUppaNEKrX_oiEPLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599d7cb052.mp4?token=LmIHNX8-AlTy9OA6gh3aB-t7cY-RGEwnyNAzp2uImKpgXnKRacOB02jeiWcri1Bvn12Upe99uIWszw9X9Utla9d6ZEynJmtb3RDZq1EmffYqjP38SLtsyj1HzG38Xo4MFgxoCrf3TNA9OcUC3s3_OHt-ae-iawaVqj-8bIZdpxXpGMyg7_OFHM17ta_ldFyx8hU8j_m19CRJKDgfHK-Z9-WiSQwFGror2PFx1_rukCyXvMfXm589bRYRPvrSzAxpr_42XdRFaj0tt3M5aX-dX74mRCgiRtbx1gtXAE19V4-uHyRb2DVMonc6mKM0RykKPvyCcUppaNEKrX_oiEPLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کنونی جان فداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135376" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a740eae1.mp4?token=IQ0cGtfs79Q50GcvtovZ3nVgj5OYgV9aTtexfk_8Y_05NF1uNdkK8rN82RF4Jki3ythbd0FyJofKx4NLMhoDN4mE8obPd35iS703wN-soqFT0S2MzjQKHHVSL1wUVqo2bP4H5Oq7D50Y0YlYYNqJ1K067j9rZ0emQ0bESziQotQ8YBgR6fTgjhrOdEHpwEB6V68mQvPffsjW3kuc5xIWc2GdTEDDGtIIUGRCTthxbQA0CtpUIiWXoHXFZSDSKQllbrdVVPgdlSFVhHCuL4ciSFplZD0LFeGxGGyJJLO1-JcBIXJtS7gCnYKJpH35tklkCGICE9yWBvIQOh_gZVe_2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a740eae1.mp4?token=IQ0cGtfs79Q50GcvtovZ3nVgj5OYgV9aTtexfk_8Y_05NF1uNdkK8rN82RF4Jki3ythbd0FyJofKx4NLMhoDN4mE8obPd35iS703wN-soqFT0S2MzjQKHHVSL1wUVqo2bP4H5Oq7D50Y0YlYYNqJ1K067j9rZ0emQ0bESziQotQ8YBgR6fTgjhrOdEHpwEB6V68mQvPffsjW3kuc5xIWc2GdTEDDGtIIUGRCTthxbQA0CtpUIiWXoHXFZSDSKQllbrdVVPgdlSFVhHCuL4ciSFplZD0LFeGxGGyJJLO1-JcBIXJtS7gCnYKJpH35tklkCGICE9yWBvIQOh_gZVe_2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با کدوم پول میخواهید بجنگید؟
🔴
ما نخواهیم سر غرور مسخره شما یا مثلا انتقام یه نفر زیر ساخت‌ها نابود بشه باید کیو ببینیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135375" target="_blank">📅 16:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
منابع عربی از حمله به پایگاه هوایی شیخ عیسی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135374" target="_blank">📅 16:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMgWerkPXYGMr-a_d3ie_bhrHE49axEXT9KEDm5J7BUHSD3H54f5Qv8e3gVRPiOok0Kr605tH6Ktiowm95VnePB7xSmDAXDUmB2bb00V2qjO87wH7x6gLRdNMxujuqPegnQ2LnLx8FWbwSk7vTqhKbQ9AD7IXreKNNq-5S-wS-nh9IarJwrwDwwkQoqXA9ZY_n9V-xOr8TfyydXxqbcc0YoR5sc_7aol4VOb7nyQTeZSd6Mv4LpA1Sf1jshjUi26NxxbdHeRp0SaEO-rEPd_LNn9nNuw6o7NmeNvrW-whWrfugd5-xdQL6W6xDC1EY-81Pe95POQmU02yQUcyTvwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: فیلد مارشال ایرانی به ایالات متحده اخطار داد که در صورت حمله زمینی، راه بازگشتی برای سربازان آمریکایی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135373" target="_blank">📅 16:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/5f8e3863cc.mp4?token=rV8cvQdGwsmmtwUE-qAQk_119yVksqtl201E-a7OojdjZZQ9e1mezDBeDQ4oGQU4H5x2MSovDXf0RJQgBOL5zjQqx-0oaM5XbzNNVYvOFsC-I0hQccPFpTnxXPDD2hILFZn5JcuE6PryGB6yUQwhmJoBXt4C89R1Eck0SbZdXtSEnAVIF2-wf9osFoiSFW5pahivh1QRdPej9MWSQ_dTtC8zSFEDCI71B13HVznVV9VNDCzFS5MccYAw1GbzNkcG98veaL3FIDb7HHLnXjmIJhLsSLzT771oA-5JjIcmlxalJbLa5JhdBzgM7hdGI77y4zS4cGpBHKQOn-LYoaPG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/5f8e3863cc.mp4?token=rV8cvQdGwsmmtwUE-qAQk_119yVksqtl201E-a7OojdjZZQ9e1mezDBeDQ4oGQU4H5x2MSovDXf0RJQgBOL5zjQqx-0oaM5XbzNNVYvOFsC-I0hQccPFpTnxXPDD2hILFZn5JcuE6PryGB6yUQwhmJoBXt4C89R1Eck0SbZdXtSEnAVIF2-wf9osFoiSFW5pahivh1QRdPej9MWSQ_dTtC8zSFEDCI71B13HVznVV9VNDCzFS5MccYAw1GbzNkcG98veaL3FIDb7HHLnXjmIJhLsSLzT771oA-5JjIcmlxalJbLa5JhdBzgM7hdGI77y4zS4cGpBHKQOn-LYoaPG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر منتسب به آکادمی سعد در کویت که مربوط به آموزش های امنیتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135372" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سازمان ملل: ما همچنان نگران تنش های منطقه‌ای هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135371" target="_blank">📅 15:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔴
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135370" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ تمایلی به دیدار با نتانیاهو ندارد و اختلافات واشنگتن و تل‌آویو بر سر ایران، به تعویق این دیدار و کاهش هماهنگی‌های سیاسی دو طرف انجامیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135369" target="_blank">📅 15:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ در حال بررسی یک عملیات گسترده علیه ایران است، از جمله بمباران تأسیسات زیرساختی، حملات بیشتر علیه تأسیسات هسته‌ای و بمباران سایت «کوه کلنگ»
🔴
او هنوز تصمیم نهایی خود را نگرفته
🔴
رئیس‌جمهور آمریکا ممکن است که در روز‌های آینده دستور تشدید عملیات را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135368" target="_blank">📅 15:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135367" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135366" target="_blank">📅 15:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135365" target="_blank">📅 15:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
انفجار در منطقه میناء کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135364" target="_blank">📅 15:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135363" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/135362" target="_blank">📅 15:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ممدانی شهردار نیویورک: به دنبال قانونی برای بازداشت نتانیاهو هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135361" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مقامات آمریکایی به «الحدث» گفتند: ترامپ در حال بررسی گزینه انجام حمله‌ای گسترده به زیرساخت‌های ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135360" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت سوریه اعلام کرد یک کامیون حامل میوه که به سمت مرز لبنان در حال حرکت بود را توقیف و درون آن چندین  قبضه گلوله و موشک ضد زره کورنت/هویزه کشف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135359" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK3u6D1MSkOV3aMPPP2zyAPGlrKx9biZjX7SwtU2xMLIyu3T5JorXC7S528Xj62jqtHJqYGOHLq_kTkiRt4T9ljAHoitWJFXkBZNFxO0z303ulo4zYECPi_rRNh1fAmNGqpy84_zcZYiNim2OCZq7tOyRVbMMb-7wPaNX4WkKc1x7qQy3or8rCTJiCx3Ur9-6lmq_is_YW3kcZQwRe-YeJ9zIUzFHJQ0bZU7TnuyGCANZI5c2m1GdWtJD8itLU8rxA03hRAYHVUPOYRLmjWm_GpH0iDD6Af3gKz4GIV1p68aPSl2onA1g5rEUuSoI95duiau-KRvSLl_oFLCwBd5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه های نظامی در اردن هنوز بعد از گذشت چند ساعت در حال سوختن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135358" target="_blank">📅 15:14 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
