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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 675K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-97214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ecc5660.mp4?token=MP8s6kVjJJbi6etWd19yEVla0vtkppmhtUSv-iHgi6944LTvsHGtSqaTaTCfOZiO3AXbfcuQe0bhG76Sk9V9XiSaOi6AuT59YTMdtNwBYvpScy9vduSHIiiLgrWJKDF5kvzh3SmYSqp-n191ZXQS1yKuNkxCFwwGzvWcldCfoAKGsFPI65POHCKeaHKeDwsvFMVl-iqD-IAe7hFSdwNxzpWlNhunbOXi9_-WMUqQL9Orp6PnkT4xg92nRcwfEZO5IV3hFXVmwbWUl45IBAWN4ONTaVuCWvZdXdw_Vf-_NnQc3DKnCrmqteJbMIswzYnt3n7BGbACOueA0fAUHK-uBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی دیروز اندریک بسته آدامس انجلوتی رو پیدا کرد و به همه تیم آدامس داد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/Futball180TV/97214" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خوشحالی معروف نروژی های بعد از صعود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/97213" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=eP1GzxtDkngr-GYN7pga8dlWAVGDJfwaxwLUEQZEQny8pmXGbmUGhrglp_aquFWBtVKfgx17luVdjHdfJukc9b_QkthcnlKcn_Ylxoajfib47dmxIbpTKKBLYdQWSVSsyOOuH71hdUUpybRjy0fJ-hzi205BUkyvxz6jkufKyVNumJMsP7NukXt2J3yV5Jxikyxat1JbqD9W7f4RFvYVYmNnJowC0sdGuNVUEzHQGFyNBSL6eUlc0TemZoUZFk7bxfYVGDzjqUt9pvKrXRVN2l2yZBPyYVb5Q0Nox8l7TveedmReSWK9HDhSTlp-TQtMKI8wlOI_wduC6zXclRlz8G6oiR2SN5g09I0fjrvU4BX-gkMvPdt5FaPpBL9rlYZm2vIj6azOY7fvLI9FPlflgrpBlcFzMemqFvRBlTVhjscADmsUrbhx2jnPShoWiAsB_3II_oDNAEGoszYxRmk8uxmXwrZaxvH8cNxB2CZMbjPLiBXtKnCIEH9vzJhhc22dI2DkmB2yS8g7ZXZvwez6nDkwGC__di_5zDlBtGaTgbvEM3zSg9oNTab06EdWzJG3n84CFHT4jgtLrU-5p2O-e890SXjxE-z-_KuZaoWLu77GG2vLtITfnLMI9AfYZY4k3U6_k8EBDlsQb6FhR7OX_z2ZrJ7ASO34MyKvhKghU_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/97212" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/97211" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN-BL8sLXKsb5aPFNrwEeQ-41OZGMtueyiGXe3CG-E6J2T5E7zW1VVrjFrmXYxRltheJKCFJhg31s6Q1GBmJUAJSniDZG_JEBTpklrnx2GgQSWhSx8ffy9CUs__h5GNn7iD59vmace8ZfckdhzlKYrvir3uWBRlb-qmQpHvp7Mu5ooBQ1gcv_OUiJtHilnExk6Cfeo0qrJ2f_3-8dNsIvaQ0J8U32YBXsskVb5k-h6-RIIgLmaS2OoVTlYg2LtkKLm2SFDdQPpEqQ3qbvPkM54tkG5A7Irejf4EjcAY5PHKGwAtFDpe1V3s6Q31dH2k5WzsPnlTy1msErtTXjDVYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
زمان برگزاری ال‌کلاسیکوهای فصل ۲۰۲۶/۲۷ مشخص شد
💢
بازی رفت:
📅
۳ آبان ۱۴۰۵ (۲۵ اکتبر)
🏟️
در ورزشگاه نیوکمپ
📍
هفته دهم لالیگا
🔽
بازی برگشت:
📅
۱۹ اردیبهشت ۱۴۰۶ (۹ می)
🏟️
در ورزشگاه سانتیاگو برنابئو
📍
هفته سی‌وپنجم لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/97210" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSgeMvKfLjsao-E_XxFASl4Gb15tfsZmWEkhx_IysXdGB8cv5iDs1x6f5n6r8JL0m8Kq4jZrn-IAMd-C1b-z-nswnxqAscWlLLMjX9U2Or5Pigjyxlb9HipgzyMKFmGTgK6zS8BL6smBWbewDreDrJbEeWpK9on5jQhyOWM8aJO82eT1BN7nY9ivYshwcFKU3IOh-V96c13OLR21BUsPW205FpOmjTC_sVqXDrFcO4yX5p1wkGwDo3OpHkU77XLCRLPt-rQ2Po6V8ICqgC8tKYBTdpdUbT4-hlf6x9rG1TBkmKxJVF1MYvLRd4__m5BwtrKgaRzYIK0YiJjeXu2nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/97209" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYNwPXogb9wHk7TvnS5qd-tqY_AeGh9b8xIDk2YZCP-NBPHNVuCcEHW8XmyoggCC9NC1NMT9ALOv_IemEH6E8HZ7D2noIGuYe5bfQfOYxjjyaYBXAuATziJAjMNCUH0Ku1XdCULSzblyFQ5dvQ8pobIY8OgGBU406xhDy7-2rhyD2oypRIJgF1kVeXyMZdCT8n1rR59a8CTUBLd6lEgzRWuiVr7kfLTZJZzqrJKih8I3TktvuxQT4bPnh7bL7KeqtstDCfFaevysW8QRHuOt7pu32e2TGH4Yfo7NgSjYbg_nxQpbfGQ-kQi7nflOlx74JdL4Tq9ZopD2NA6VPq1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود نروژ به جمع ۱۶ تیم پس از جدالی سخت برابر ساحل عاج؛ هالند باز هم درخشید!
🇳🇴
نروژ
😀
-
❗
ساحل عاج
🇨🇮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/97208" target="_blank">📅 22:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XStuP8CEO271rYO54lbIsrjqSg9bY1dGzxRiOW68oH3H1GTPzFpKFyzo64lxHZPgF9NKtpR2P7xUUfuUva4nZmn4F2TRM1wF-pdebCdFuXDlt5BHkj3JOV78OykM3Gc0FnYPiPbm3XsGgY82con08m7n--mfT8LWiXUaZP96OZ4fA0XkFGkNKkuqw-M4gm5gvmrWlxtPI_LmdBMBqDJu1mbBohzC2qyi8gLdbW53-mMVIpL1Jejmj7i_ThfjB1YJVUhytLswp-V8zQH-uXgsrPUyHPeMTmKBC2aPoO1aiGx3HQG6Q_eWR3rBqbTsGxYFVsh5N1W4OvN1pm160-YorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فووووری
؛ برنامه هفته‌اول لالیگا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/Futball180TV/97207" target="_blank">📅 22:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇳🇴
گل دوم نروژ به ساحل عاج هالند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/97206" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هالند بازم گلزنی میکنه</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/97205" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نروژ دومی رو زددددد</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/97204" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/97203" target="_blank">📅 22:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4771a77adf.mp4?token=rE9o9zIS67SAdbepAjpsW6PV3UWWP70S7Pw_uWB0tBtIFCyul2N5RVod0e8HsV1UDn9OZsP62tg3kw5lGzacgLkQHBVaijwV4Y6jnf-lJEygvIOsbHwq-lAIS567E-Liq1cJF7NbKTqdSIYfjOVCD0TP8jvMi7FgmG9NZnQnLdUKq5etGy5_qu0M9ejvVotetwRZph51z29P_d3zAv-Z-JDsPorFaO6U79sY8Ky0k4U9H6N6CGhw1t3PK749pltTtV_iODK6vFypAgxzyR3sf4t-HD_N82NMYiABY0sKp0IZhNN54uhhiL0WD5zquZt7rs1bjG0Sjtntf5SKd5fZa66Bs6k7BaZVNXC4viiDGxcdHWA8Ul1i8yI8KlFhHEciN9fFje5HNClQFjZ1x6JhvOG1gI2ezGfxWtkK-Nm3xULo511rArE05QIrP-Da8NOQfRKSqfPfZusIpfrjqvQueCarWmCIB0-kkfIna4z8ZPS93Ve6LDOjJ-VFolzynuvA7ve2-X0ejogsZAu8Y2UbW0_ICHJ09EaEmetLD1qMiFh4cJkuGDLHW91-NuZlDqWo90SVOCp6iAhmIGKSJ2EvZr7Q7xdPPynCzg5SzTWveYGtoz3LnLi8VeO8tKJngYNZUIbC4_B7yrWf0ynI3ODwSir1D5W1AzrNOB9AwmFZ_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل مساوی ساحل عاج توسط آماد دیالو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/97202" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ساحل عاج زدددد آماد دیالو</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/97200" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/97199" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چیییییو کشیدن بیرون از رو خط ساحل عاجیا</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97198" target="_blank">📅 21:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۶۰ دقیقه از بازی گذشت</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97197" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97196" target="_blank">📅 21:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97195" target="_blank">📅 21:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv3gJNoeSqs9KDfq3fDZd_nOIOtWxQCPRc63LUV0Y3WlyFJQQlKttp6HxFLhG4aWurnhilb9VxXvFO8Wwj-ZPXLj9BhEeTwGy3im2Rjyb5z0eFpscCTOy546sYHDbetrWftdA2x7PSLEratgx9VYg-oyY3vT2bbDiyDWswVRoz8_r6gtC-392a96cKC_IBj0s8cV019POAaT8Dvmd_gTea-j0GPjBifjUAuotUNs7XQtCd_3Nrt6TLNVuA0TBSYPCkFKdh4Iqs9Mof9UtvEE5onohwvzzhW3kUQsA2B4TE44g2O7fsT65veIaD6pzndkeRGcoYvPR3k5KHwwtliLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97193" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPbZxq7ZjPd7bId3Ty7SzpIliJ6fQglgzC8W6PLeJCV6JVkJW7U042P9bm2DZ82Szp_zZHyE4sM3nAMdm4MHGf5DMx8bq6IXm_LtO4Gg6_vZhCL1CBbNXx-nlh0EQmyr73VmukXH_uI56mMR3ojunY90Yw9ORxB230XAnPGb6N2h_B3QM7R3RaBkp2rm81EcEbICQa8GgYCeM7OudKb5e_1MiytN3lQULG71_HzWKmlfdM_5oGpY547Wiw_uS4T9Dh4e0Ys6jE2hMwLhwLzp0zlz7YrCkPP7UwBE3a1lxAzV0ziQ58RWgg2GKiyzIlnLqou1SZJH2mJTLJkyHxx7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🏆
🇪🇸
ادعای پشم‌ریزون یامال: فکر می‌کنم امسال جام قهرمانی جهان رو بالای سرم میبرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97192" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSCgONXzi4vFqBbCM-wsEtHJFe7k1BpfV1kuY7pWs7GSjXbdMbAjwz0PIEvoBI0zxwXlOEGkIreG2mb_CZYMhmZ7EdpO5gPzoLfmfq30sxaEtQtiNOhXzy3LcmV7-SjJmH8_DzlWiPlS-BAJ03yp2KkJPo3jmryXMnbTXPZ3pcw4tjniEugTKAYVDGPtbFzr4SSrd0IQ1lHuZuCT9OXmE3IEo-UK2TPQQr99r_GvS7csjgQ8Su37IJJGxqKC7MkuaIh9wlWzxrLWk1aiWk22nj_HqUvOeIJpKK2w7OZ444r3Qzw49KLKnaLvvL5woE7gUY9kr0S4CxyRe55zyPGHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
👀
لامین یامال:
🇫🇷
🇪🇸
فرانسه بهتر از ما؟ نه. آنها ما را شکست ندادند، بنابراین نمی‌توانند بهتر از ما باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97191" target="_blank">📅 21:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97189">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtS5vDne2F9eLwDJ4JajkGPCxJNUtLA6Tf85nkk-1WvGbDx1fv2hOZ9J50rs2dfGtunHQOMacxXVaoDOx0MBcZvd1YNqqSKDLT5Vn8eOmBL3133qHJQhBh6Zb7n-j7nIcyVRKL-zAwS2NwMivwGJGtSlRJl4BJE8p1WqWNaSbH9hVMaKhg6jsnZ4NVTz-DOfxJ7nztNSPFxYjV4GZwtzaJJlBc4McflSgCaMNrBplexIYM-vDw8hnIK54_w_j8NYB3LHNdPu82O2Y9-9Y6TkndpDkkGpx-GXPyHNFCN6L_waVnKrRP43Jwel_tcf1gE2blXLOLJwc0d3Qyrxsvqf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqvXvksAOhXQKELxhKds_TWINJddXZ-f0bFhB1n-SL8YGcv49ovqjIaTIXuw-xibmDE-9Rjo8wTElPeZpEWMw2fOKaoNEJ7gMlLrm8fPT0NvUe83OQWVPNmdC0ombmG2vjMuYpdrXyks78Ky1VHGFdmriloEIXgIW4ssh5DLDs2qjdONkMlCTfoU2bf8xXbAtv8UYqtBzbRsFgcQ5sTxsLSEPkvt2E3LJTYhCvNO2Pl2QoKTA9dSS0U76c1MwDYf47bXgG4khWRfSxAraM-CAySVu_HThCH0NCKS4rV-WwjPH-pcfXBzE2Du3LRyk4oXdb16H4ip6OIm5hfokN4PSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
نمرات بازیکنان دو تیم در پایان نیمه‌اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/97189" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97188">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏆
پایان نیمه اول | ساحل عاج‌ 0 _ نروژ 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97188" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97187">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇳🇴
🔥
🔥
🔥
سوپرگل اول نروژ به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97187" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97186">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام چه گلی زد نروژ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97186" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97185">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گللللللللللللل نروژ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97185" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97184">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkPrsQvD5OyifD6wF7jUVVzjy_n9FmcPTFZQUt2UtIcD7neuN6Qtl4LFWiiBQjnLOxreoxgTwbKi8ltMiiMdD63nfqrg58IDqpCg4l9lPd2DA6Un8r8_0OyBsEJ0dcGKel_9hAYJ3H8RCzleuIt2zAd9KjQTzffIsVXFnxNBjXczp2x8EjCyrXeTpaZcIF6I2zQoFkwb8WhFv5p65ifFAaZUoW2X_TnpSPTrutA4eySOgq4I3QucbTxBSmMiC86iSEOY2qnOxJ0jxX8oHMHvcoEfYuTNxAinjnf9e8D83io05r9vS8rXE5isJ3yYCNngMoDJvipqQhHAO71yQzyv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت همیشه حاضر در صحنه پیج این دونفرو پیدا کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97184" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97183" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Nvm2iG2IU8rgWQUJNoMUt75dGLUq4Xwfd-elYZAWUj6GEWTnDK7aj5fchJOofHDLpyQxfmayLYPMvI3jmmHURiznxLoEr_QKSeK4HPh9vFzrXjuUyNxKbvQ6q_Gwezo0BEFgixHjZvVXGxoLOluztwyFH4PiFIh4pRRJee4azxmg5vlZMQIQ41klOxelnIxpZuJQ_28nfzBNfh-AFwZYXZGZpjf7z2329sQELTAPKVnbMOwGrKrGFRfWHlYeRUie3anG1zRZSrOq7Dmx3IHq2_EdlHIdDNBw9Bwc77kNUKvIMO4Y5CYgwzUMM6ZaO142zK2NP_JoHKiqZ5XmOALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97182" target="_blank">📅 21:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ49E_h2nNMB0uPvwma25AVXAOVKB53JXzSGoexPwkyJlFZZh8x8vWVjCpCJs9SwlJOHBUgBoPUwngUcJHghNO3ZZmk3AYrZNTTlYfhpNOr6d34q8BN1OxCqdCxmHQ6e4AHVTQpXHdIUMH1MWk7A2_aPXYuT82uCGGRF-kocpiLFBxvypaLgeYWxeGp8DqtqKc7S8UBntCL98nM2SLzQ6tl1rDCbUTOlMikvZxjCkFVz9He9vPu6JqE-4xm33hoClkStQNYWuAHZ2UrsMW9cbZDtWr77h2rq1ndpwU2UfBOjhyr5E43uRGMYmTIseKH7Tct8K8qQ4e68A2lEeGhGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو 39 سالگی فقط 81 گل دیگه نیاز داره تا به تعداد گل خودش تو 24 سالگی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97181" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ-eaeiAYzA94eVSwhDK4RsbDKOZfjuSy65X7zIYi8SwhaY6-ftm3fUbh4gngcBZZ5vJA3-ccKyuu1x8zud9f-VqQ5Aj8ovppiSg0hvabKfZOPGa8VJd8VA1PWgZnapLLV9TYL3RUmlLAm2WpCYcdSCx8Wt6N4iLx94JpboFpGB9OTVy8D-_8oXMh-5ZDCzlWbmLswAVAjF45SOPz6gFPBc30mevToHdsmV8O5aE-CDvhnyhJe_WI6bhPareJpx1e4Wd5QxQFPtvXMOU15XZN44PV-AEemnWkXw7HYnk0bwxCFGJN2wv8UlVhXgct146Yx2nrdOcPqaQUlYGAgJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
آماده ام و میتونم 90 دقیقه جلو اتریش بازی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97180" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97178">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8OuNYoQWpznauk_U2v-lzT7nPH1aUJ7WiElarJCweydb32_Q_09BlFW3NT-7mbmtArrzV4QjvQcIEZS_3OM4tjcBhNf9HmGqr81muZ1ZsEJNRY2hDp3GLEqMcEEOef5L37CocVSuRLyRh2HSTv2w894YwluCKS7W0nJbIKARbCxrv-glql4lzBErf85BGhkoGsa-JAeYTbMG9UbMv9V52tBpjicv7IOqkwdOLPYJqoDGuQQMHWGPi32LUTQADc-D0ndkqGkH1Mva48AkxfUqHv1O2o1bJOtnxscAalwXFav_qoLpglXWL2mGTZtQ5tBcmQ3ggwvdIkS2dBkATl57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0H3ED74G3LL7B95vEogFJrsP-zt-oav91d_LbZQysHyoWP7DFT52d0k6vx0QvOE38KBisdP_gPMgFgv5lHhtsN5fwBQIN51gaHrLGxD0TNjL3GERB70DaUDIzyGixDkLT0ZUFIBrZPZAyMv3RODnttqqtInQXVA92jn6xq7hNcRCEKyNYtCyJL-Uv42o8uMYT091y9QH8Exe2yMI-R-05xs6YSlUTMr-BC3KtLAlF6-Hf4bsfMFxlO0K2RcI37X8_W4R-m4UmAq5H8E5He6-2o0BxJqw18VVdquLPaf2eH4x8qaCn5FbmtFbKguzT-kXAJYWdFbD5ZkYWpvrfyn8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🆚
🇸🇪
🗓️
۱۰ تیر
⏰
۰۰:۳۰
فرانسه
🆚
سوئد
📌
صعود
فرانسه یا شگفتی سوئد؟
⚽
🔥
فرانسهِ نایب‌قهرمان دوره قبل با عملکردی کم‌نقص وارد مرحله حذفی می‌شود، اما سوئد با انگیزه بالا به دنبال توقف یکی از مدعیان اصلی جام است.
👀
⚡️
فرانسه مقتدرانه صعود می‌کند یا سوئد شگفتی می‌سازد؟
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97178" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97177">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJj6gj5N_w2NC3H5PYy0MvEAWjXeHVlyonSR27OEB2d2guEa99I_xJcD_c2TEY-Ew9Rg1-Ticmf3PPn9Rixv6iT7QRNvxohl5d83Rny0pjDE35LPhlKFx5qUoUBobldddorHYVc9ZyM3tukKRrC8gpAJBV8SF7kUxHi0HuTLijyqPUzs4IYwSMIDIUqS2WyhVn2wJlJrAjR9z3qmxtF1BzDrTOEWBSZcwY-PUKrS2q-8bKvUMsXNYwPJlaV9bvM6si11E9fskIMR___joN8jlJAwgIV0u_C8s50R-NxP8MzVH7loHg70Bdjh8PCj0yUyoIn37lyRI7aKum7MwJ5Lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
رسمی | فصل جدید رقابت‌های لالیگا از ۱۶ آگوست (۲۵ مرداد) آغاز میشه.
☑️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97177" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97176">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf-BXq-SWDGPbTORJzjgxeKusDAhdeloeJI2W8EFFCPifXq0F7KZLdxHUjnGRzptkgYun1LTkmhpDzOE8eEQpdThvGMZxnPvDc3CJhxDItz7kcAXVntC1R7WCQbQeSWygNN6i4qode_0t1SFi1zwyP8Yk_8PSGOCpWbSH-pHnMH7Bsd4cPlUiG31GAbBOw9lqZTX65IXhuQaWT6jZAMdbJ8AgkRiKMpwzjY7rJaR_BLlKVYKy_S0N2aGlMtTWWqUXMiU9ISruaQHa2G-fCPBPzfCRr8q7QrNzrEodNggPTw6zJLb7phUSF--OA2xS6HdaQJgm0FFebeVJOCLGYmTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردی بادوم زمینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97176" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97175">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شروع بازی نروژ و ساحل عاج</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97175" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ خداداد عزیزی اعلام کرد که داستان حضورش در پرسپولیس منتفی شده و با تراکتور ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97174" target="_blank">📅 20:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180
#فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه ادامه دارد. در صورت موفق نشدن آبی‌ها، قرارداد برخی از بازیکنان فعلی که قرار بود جدا شوند، فورا تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97173" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97172">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhgwH8TzyXlcsvE5DYPr-PToevqX2eDJzEbo9RpLLq-v2NOvZh_VGRTXyvnZ_C44FOqYtujwTvX84__mLGFrzhJT8RTt_sNOF9iHrFrLTxXF2WkyfKJRIaM299QXjBm7jqdDaE26TcHvBQjzUp_ixLA538H3A6Aqp7V1BqWgVXfeCNrblEY_07JiREfQUVl8cqyG88yu7Gl_kRymI0GP6T3ThgYHFf9LhuXMtVbeSqTuW2zKcAsm26tvPl87XmwdM3gn6dqABcddfrh1oebcrgPbz4Ag0EI94EpKylblYA7jvGJrwNn6UgoMffKJG01XSZ0cRjTMYOIAWuGE9siC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین: متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97172" target="_blank">📅 20:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97171">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_NvxfRNm9z1eVRXwSpOKUDdpIAvoFMl-6QuWTL6959-r5Asoskk6pCB5VT4HUeNVk2jSBCOwfdRvM_LRx1eyG-aMNpk-iHd56Ptjc9egmEC72vhltBtbwR4iyp8pD2DE6q-tUNmPi0oEsPo7DQoKa3xQH3MYzJ3aqF8fedPmOHkC63cIuHBqVlKr3-W22bhEc2WXKAanw9nKyaw9ptd0yqyJf10FkSg8qrv9ToxkxovWEvx9ON1FucNgRz-Br4be0tr66c0GzQLvWy9UJjRLwnC-E80f_4T9WZYOZg_WG4Mh4-vMqQm1idEONnCHYfUt-fDLKNMlRueFSLV6K_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین:
متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97171" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97170">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5dOxiT2IMpiXQp2bnBefDbpcVhenh5M_vFlYHKJuz5_Q5XHg_p75geK47M4mdP_EvGKJVuRP8EnX_xJFlbaXO0miz_y7aN5-R9CuhvCCfqgmHabcUOZ6jGUwkh0JwcUuqJ3qmIqC75C5EQO3SOu_ZVnwPdHXP95iBhRR89XBu0Y_GAnjtjSmOJqcN0E6ad0oL9djQGlSy0KDDtMLXsjdR2nmoZpZmucFSJhNGni-Wb6qdjfvq_GZF4P2qJj-J598RpDmqY5l5maFJ34FhUhSCECOAwgfA4Eo9cZpXNcVAc3WSlzpX8iGE-0Vn5P8H0RUPGaMZ6Uuyb3ydzTrZgzhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97170" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97169">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYtCFxkNBg3by8gBv634rfmcLH_m6O_MFKsaVjEIiVLmfLD4n9ji5eNRkfDS1naTwYVDOd6xgVR_xNSf6PAfITM7IpKuXj7hafpHopaUCybroVdoUDw9Z7sNa8FT7g3KcCFRnXlJp5-_2RhqJoCaEJQVovfdgSB0dxUfK-bs-uU7CzpiqkEF2y5aoWHIE0DCNneAifdwwZAey1-68PjlspLPrpuYo3jMwEOcQpqejkkMP3DMOwwn2hzDeHacTT31Lthyf1i-igaTbbwIsLmjBw3Ien25s9qI2M_hojsAZ6gHmCBO2RF3F2Yk2_4QUn-ma0OyKuLGkeoNEFt8oG1WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین وینگرها در جام جهانی تاکنون:
🇧🇷
8.29 - وینیسیوس جونیور
🇳🇱
7.85 - کودی جاکپو
🇧🇪
7.84 - لیاندرو تروسارد
🇨🇮
7.71 - یان دیوماندی
🇫🇷
7.67 - مایکل اولیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97169" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97168">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=ENXrPmbsMvejbszH2UQAln9S81oP9hbSKWo2pzpWDmBeIJnvrVL4OSLOUhdMbGDk8XNvP1PEzUSAQObQMKZ2lnv_UTPTuZRZs8OfuHvbqIFNmchP9UySdQw_Lq7PdQat5g17diknunhyb3lVgVD4xxLdvD0heY-G5ZsRnL0PHorCC0mJt-2eotfiXrGdLingQSV3rSjHw8_MJTVgTIb9xFj7TM1lfdwE4eQIFm-1yaCJbujMx6vs2cYW3fFcpSboyKMyH6loaf205ajrkw6kZpfY2SQSGccPIzfSiQZOhuavY7wlJ5o69dbLmD7t4z6rA15vRKhnp64Ofd_tXkPmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=ENXrPmbsMvejbszH2UQAln9S81oP9hbSKWo2pzpWDmBeIJnvrVL4OSLOUhdMbGDk8XNvP1PEzUSAQObQMKZ2lnv_UTPTuZRZs8OfuHvbqIFNmchP9UySdQw_Lq7PdQat5g17diknunhyb3lVgVD4xxLdvD0heY-G5ZsRnL0PHorCC0mJt-2eotfiXrGdLingQSV3rSjHw8_MJTVgTIb9xFj7TM1lfdwE4eQIFm-1yaCJbujMx6vs2cYW3fFcpSboyKMyH6loaf205ajrkw6kZpfY2SQSGccPIzfSiQZOhuavY7wlJ5o69dbLmD7t4z6rA15vRKhnp64Ofd_tXkPmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇵🇾
خوشحالی پاراگوئه‌ای‌ها از صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97168" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97167">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grfBEd1FRVsqmKdqA0oEftW1kIZH1Q1xZ7E1f2A05BqpsSDskwvfHFaZBTg3ExnjPqOURVF1Aa3OMpPdrmE-Vyk7hpS5OfeUEeFFgzCfKdKQdjT0_OLz6mxmZmERb4x-enz8ONcfYcOGivfLGitcK5TyWKrs0aap1TSPZoVQ_AXwG9a-By-iq5tC4e74rBbmPNjy9k-dvk62LyKDYBUkKwMCyzbqFWSYBwdafeNvGsbb-jcXnjmly_TyDngrXz_ov2aOkHHXxjSRlju1opj-WOWojLxBtkEKac4UX4SeVTdVsH56feGpMMApgOqq9Q86o-tUaQnNlxTlPi7EGb-6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
جاشوا کیمیش دو بار از گورتزکا خواست که پنالتی ششمو بزنه. پاسخ
نه
بود. بعد او از والدمار آنتون، ناتان براون و مالک چاو خواست. هیچکدوم قبول نکردن. تنها کسی که پا پیش گذاشت جاناتان تاه بود...کسی که هرگز در یک مسابقه رسمی پنالتی نزده بود.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97167" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvg5bh5o4XgXGHHl-t-iTtAmFQ7PhipamVaLN3dQWvpiN1y5HeLbZ5R1Ow2ANYPpD9sHEGqPlbbickXxTn9JFENWfrlBtFOXhF-HRAuy3Mas1XVTxpE7LHZ_CR-nNwEziMH-muy5MA_ifiec5YX388oxmbSmDxQWEZGec8a1P_skyBacJ9Wt2FwurdBhnqukgUossqRVCDjI_r1zIvmtUC8BjczyYnOsVisH0Bovtxs_PmEbMh8xsWy1wS3f3kdtSbMQVhue1iRpFbXiuayaoZJKVa45y5giS1_WFIIFDG0W_06Rj7UzMGlvtboWVhW3uR4hcbMkcwvR9JJMhzyRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk5cGivFVkb4JWkrdK4eXYeK-HzDKtiCdQJT5rMS4CoGopIOH13_zRBAp2djnPDkyN2uAF-Bme6rLS7G0AYdfwxXwkDCqLWYDO4-ysET6cZNMkyObCTkN9Qr-RwKZiA8v45RYikOnAQrPgkhfk-z0HC0G3_X7FT3OvDc_qgtHh3_49Kz9TgGVkkafCTFP5LblkbWZE9ZphtaV5aYZLrLciofxSMIPsltJrFdlcGLsfph0yoCDRr0VT79oDd2TuVUI_mzzMICgtR4WUU-WsGwGwCdZNHFs2uyIoOwo7QaEfF5YezKfouORPb9ztOwxgSQYz-4WTgfj1d86HUceZ2lmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
ترکیب رسمی ساحل عاج و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97165" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⁉️
ستارگان جام جهانی کفش خود از کجا تهیه می‌کنند؟
🏆
جام جهانی یک تجارت میلیارد دلاری است. آدیداس چگونه با تولید کفش‌های دست‌ساز فوتبال، سهم بزرگی از این بازار را در اختیار دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97164" target="_blank">📅 19:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-9XJmAd8BQvjYvBXDEhn_O5F5lUgrhN1RUtsL-_FiiJLFh72qDsO9XJ0Jso-jBaDdqEZq40ZVghHtH6bczCAk73xzMahVw7mX2HQePjALC0AtxRcUgX3-r5jxXFYeIvkVywXsgPxK6001coXltd_bd26ItPcDaziMjsM5TnNzaJP9izxP_8kgAKvAj_yUSgvMhLrOOBRm4NYf2iVe4WRl4JVcHwQol5P47TIom7u6YwzFQnKVFlDwCkYwLScHmnFQG_AAyZlHYm8Ew57ATOnwiZKkB5VH4ZXKJ5MUJ5A5l3rgqjr3K19R_aCVAneqTfXI35wGTSvLiAaba1CNmBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ترکیب اصلی PSG بعد از اینکه یان دیومانده رو جذب کنن واقعا پشم ریزونه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97163" target="_blank">📅 18:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMUYFOw4KPTT8Yf8RVt9hDTy9sIYPuzaqBDiaRlay392g6_FCpeDWyP9-iK0PKY8MbSknOKLK-rPt-CBzs9sZRVZKtIz9zUk95Ay8gc7e6Rqp-1wpz2bKCYO_dMkBNx2tFy7QW_t9TTVDX26d6J-EPD57A-7eLv71JqzzG2lzJwXX6OpGAaM3pbgyK1Sqevr2ogWk5zXwye7azbFNqo8hVzpHStyyleDIO0Za88156IqtowE_h6YEK7mJLqLgN77TzSLwH_ONuezKBYdiNIt1gvUyXnJT96lst20-OWi9aLj3NNB2vQuF8pse2Kim1uEyOhJHpDIBHA76OlCMN1XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فووووری
و
#رسمیییییی
؛ با اعلام باشگاه بارسلونا، آنسو فاتی با عقد قراردادی دائمی به مبلغ ۱۱ میلیون یورو راهی موناکو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97162" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erF3-LiHJ36KyBnMHlt-ECso37k5UpN4E2mJRUSFgYqsSDgYlDGIBrMrQrVPPkLmpAb5XnTXW9g3Ungu1pySn1cj0ufuUzRN8qKb3g_bxZR0Uuv0mgPj54Qf93Ajmv9TjSxEIF4DUW1Tfv5Se5RonKqJ14COTL2RuCdkPmYxqIG0VeeijSgqNqsrgT9iLzYfZ7VRQ5O-wfWh-OJ-iW_AKRFB4TLxnkIOi-M7JIlMj2K2djePapLcW-nC0AOCyQbwkmVpWXbvevc7KbWN1VxCQLtkJ-r5_6daEPTVzn-74KXAicRQqBzJOSZLuCaTvS91bTMrLYqDZmwYFwZF5oV_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
؛ با اعلام منابع خبری اسپانیا، باستونی ستاره اینتر در آستانه عقد قرارداد با رئال‌مادرید به مبلغ ۶۰ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97161" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO0kFbOL052jYPnrwIcMFmNcMk8s3C8Rw6WhlzDrqe15gJ1xY42Ug98Cee6bklDM7Yhn3WaeaDuU-YEQGQibrIp03n5EPn7a31X7Gb3rSVB62DGv5vHcC8yXxC4SSGfrZcafhi4u1UPSe6NcQIpkxW2wVQ3sPL8Q2H1qVO-aJQ5Xa417Ij5DvESAn3qXcvZMAK3SVZwav87DqYmACNbH2dX7nIaF2xaOT57-V_D7Aqad1UUbrYwGFJeB4iSCye-p8kFZbFwkVaYJu8j61TXErhCXY3OGfXKZ_7tX3uYyhE-ztAyvxKnUAmWx7EyosuIjCM16pq5KySiL_o0MO9Pckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی ژائو پدرو شدیداً توی ترکیب برزیل حس میشه؛ آنچلوتی به خاطر دعوت نیمار مجبور شد ستاره‌ی این روزهای چلسی رو از لیست خط بزنه و حالا توی تورنومنت مهمی مثل جام جهانی یه مهاجم شش دنگ نداشته باشه.
درست بود وقتی مهاجم نداری نیماری که تو سه سال گذشته ۹۰ درصد بازی‌هارو به خاطر مصدومیت از دست داده رو دعوت کنی ولی ژائو پدرو با اون آمار فوق العاده رو نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97160" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پشماتون بریزه؛ سر صحنه آخر پنالتی دیشب پاراگوئه یهو تلویزیون قطع شد نزدیک بود نصف جمعیت سکته بزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97159" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد باخت ژاپن جلوی برزیل، اسپید رفت که یه هوادار ژاپنیو دلداری بده که طرف هی داد میزد "مسی، مسی" اسپیدم کلش کیری شد و گفت خفه شو مادرجنده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97158" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97152">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_jpV-Oj2rIfwDy81uPHJCwzzaIdYSiaF2V78BaZvAK4lQPS2m-IcpFgSrgsLuLg7WVVtIMQ8OChsNeZn0LAOqY-oyad6c_JICNY9YyMYOjosYWjVnLwi2cjxCEOEd1Atkke8WjVuxRfBLuqI8cxCPrL3Mm4Y5RW4mKzlf_Vsp1HmYKi-Xq-KLJf6vGu2fovQk5JtiKCaAmKyUaWoycXZoHO-ORJdZyQiAhu3kh7Zg1lktoIXTZjZ888ZiZBRI9l-V9LUYF02SUlmwY31Tjf3YoxkQKQhxWO0S8y-NVdqvz849ed1aJzknrAH5DnEa948Pk575qenvpFvIfboHT1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr7mDNhh5tU9MrH9aptILSx45JoyfoEuRIfSiWUkMBNKnv6sVwLMv4rYw3k0tgRA27yZWA3U4aOorvG-eLVZ-w5gXxTyyjf0DZJIc1q4GoRYj43kJbOc-41ANb8HYFHHqyDbFPPzLpdTfwq3X9EhWLvocYgQ8kQ0c7UcFMV9oLKGE7mS0dXN8Y4FCz-Z-QUlhMHK2kmih5RZBhi14DIRNIGXyWhRqF4wYjJrzj8Fty9yAu13d99JYENF3tsCz65Rc3npcujyIdWy6AhVPX2iqfHBSbw1exgjqzc1mGdswPKrKcDqiFO4hH378IhHzk3G-NmroGxjwYSiXOqbM8b_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et4vyubH4Scfsze-GX_R_OVEeDy0vaw1fEU4APsnFXezwXfr957FkNpG_K-WGAJEcWrIj8hUzs4G5vdqcGnOFqpDVUmlqNO3P5RQiBLqWVHeZEurUpjmBjFCVXDg8M8TmUKD3Xj-NRc5rnqt_ndwhC8oqCH6kc6wDG_oqU9_d46pR8e_n7eoPv9CLs5iweKGmgn5hNRQ5zniGlmsXO8BqFdCRDaOd02Aub3YJzOfbW2ELaPL1pMfJakZTxTC6tkoea9mMeFeX8SnEPxjhYmrehAK8e9ERUYsHwCt8PVDg67D4TatNEoQb72_6rOIpPDVZR1pvu48JEB8uNUMsd5SYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffk-j_2WMb54LPvzQ5MVK21bRhntXjK83J8kv3tk4WL_HlZQGLdJoOnuq2GVgTgzP6xYOjt5bWVAE2vDGZLVsmpQd0qEVtR7ii2XySB18ikx3tn--jJtePyldZ275VxqcCJ8AwadmOzNBB8nVsgpuDA3H9Egm_i5-Fn1P3Tfb_JmJtIASZUeM6QUYmZrfd7xQm2Mi5OmnR-Inz2-hgRp3VwhID3bE5WisKPbLtWcihoT4ukDk0M1PuL8E6VGc7etVEyW7U8T5pZ5Vhbm85hTQpm5czLwVr5G3SaZ6LxSG5Cwo9PlVGrfeuX1K2OJDLZip-NnLrqQ8Ggm3POlWoZFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrCbZ_nUnuzgc492HhxgBrcH4JIqSMkPxLJ8DiJWsp7MZPo4JnHgMqQeS_R30BapSiCEM0YZgBSZd0vnkEurmdtPSDPWvkxywkesCGD67cpjDF0PBRw-2rv7jNHvle4NuxJ94TJASEPqUH7zaW4-8_9C8GHClzkHcxC6mNs8v8RJ761Qaw29gQ0nvkuwmNV6730yDhnJIm0zjNN89IrbXwd-7bAg9HOdq_uQ9KpMEAt6sMCNt-B8Edwc_3eV0uLmCgse3fb04Mg6pQhtlqgcUlSPcRSjn3Eth7lDY7r1ZOr5Z9DTVMLsyWxz0dBpakjHx343_WpV2QYgBa8bhxXi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJOeSzlHYJwiZHjtHIfmWLyS6fuBwG5BezaaU2NmMboqwR_Exstds4stCpsSOF5sbmrV2L6VVG3PRaSKPt70kHTgR3EShIthkTelzOwKHD61Ala9w_0wi2XviA0HfoFUgc6F6F8GOB_aREGx0cYnd9qmglQinYOQZSjYzkPtm6FNpyGH_N4DRx7tObwaxXBYbIIvXYxpz7DsOnvqKgsjghws34SeHGwnKLFd77T3gowXOQMDIEszO4MLcRbZOL7N_uprApi2ZIZFO7X6Yl7IA1v2Yp9yrh_vOdbcRgp9xoPf8rtGtzlkKhRXA45KVbF3BYXJtgLnmIIY77MQ5b0vhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فضای‌امنیتی فوق‌العاده در استادیوم‌های مسابقات این دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97152" target="_blank">📅 18:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd1P5st4TeRDZxSFwZqjFistvV2rw1joUqyoN4JYtzg4vSM_KmiKe-EfvjMvcmQpxVp-jSVPFzJu_A5oFfB1DszK1DOkw9BRwDRTC4UVt6H-o-ceJdzI55iqLbqMqjUngG6IX0TmsTqx--fjl5cqD71dVaL7niqqDx3FVz6qdCpHCCBJhRxwn-XYUczJv_fO3GlwZ-xFTvPtw5I6DNYypoWjZp6yNKuPd7rUkn507R0jntz_HWVnh8GUrYVh1az51xYFi9kwx1fdVtarBBx73gx_QhiigTyBggx4FLr09kqDYc5se1e6evmdfZ3d56_723AR9k34-KY2qpJDaXTZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAikrWcrtrM_z29MaXtb7iKxNMQyJeHwY8wWvEtK5c3W3fKBRehxQs9HkUg6o-CPVNajWsIipeqTHUBEBUYxEiYwrwm94YpeslGvV5Lj478WPO8-M1g6uu65BCiezmSqyKE_AGYNOuTw8iIlBLmdfz8v4pDAdP8OnOT9qYbj-99hHMJLmFCD92-lBhJiIOWP1nXko_CjsBJSaK3qXPLQcR1Q5iOP9O2GIGUQPcmIiqUyNaJbSxSU3wGWbcOIKdajVz0cm3mLvQtcpNWI6zaY5OXGqt-Zy37Mt6b54bHR1RCHDUN1MoucmQssty3GI3cgTxG8xx50rsryhAMwb5TKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjcUdfBvg4hwo6xz47bdMaEqZLz146mbhbvreg4cCgVUNfz2sS8SwnffohVFjCTpwaQhXtQGUyIHlss4Z3QQE2ROQoIhwIxJwhmn5uNLWm9ymYImylsVC4y0cf8rrW5SC0qskM7mD18q-REhQWf0tahaaibUQ3CCjCeph2vkQSilOTwfFP8HxeZ0u3D2hj7poQiwfXf3CWSv3OPBd6gAV4aBMIrY6OGQLqxTw_YBNrJ4j0QojhmInLlYhbCx-9698ip76UCrkefVYSNkCKVWljQdYt1YeAVj-c5e8AXcD5L9uyqJ-SxuBcRlLLWzmsi0vg56jxEsPLZPTQpDLG8WRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsCG14gT-cr2-1qXtbel5I8RUmwRqHUloRZcXlcLeSEiLiRazGQoGRWaB2jCTI2XgEKlD2qESzYE0S8Sz6dRyxfXZC0DxDQ7vIXlE5v-HdYOHAzRWKSc-xqLLu_nNRF8Woj0GuORGUR5zCmdOlhV2EJvRqOTC1lLmdljCA1bsiuBBmWJbf6nBCph6FBPFgo2iVyeIoikR79zFHfpthqWG-HUggN8IyU-HjaO8mGhwLGpJDpAIF92hQHfo5HF6PyjbJLoUiQgbNJa7niQBCJbFGa2HDIK3HxjOyF13gV-KmNRogRDLYwlTufSCJR8bkH8nBPWyE23VgqZVM24NBwcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9-WVK_Cqh2vfGtRoNeutZx-26UVn78gn7m6oKywvWYYwX_HeXCxq1qQQlQb6p8R722FPa61ejsy14OxAJogIp-CA9IgyDz6Ev3NOiAN_ue4c8xwenL7b1QFv3DF7zs2HQw6cARuUyjGJ6jVtT1SBkRy4gfgRAxI4O2RSkHk_EWcN7WVkQF6be8E8JKLWV3oDoN7EnBorXTZF_hzIL5RPew0esg9_pn0ZKjpmRmPXhNMNrXHMplGleFxFuc8zDKLXKsUxPGaCgIv-cjBqfZoZC4AIIg8f0nkIyhKDJkKzzm5ywpjdd_C-zb7KbzHH0g5cV1K_PaV4S9zdfHjZF9bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/api1yG50cffQvSM8KvIRh8cPPywIlgTcpYvoI1Yz6cLlRl0j3ShpWI8Qyp9TCQNnZeMi9SrkOpOkpxZC5nSLRPkkPKbuKYmxfLvT3o2lhcfgoQTNq4GRrDNSay17kky6FFMgCxTBs11tr0CwcGg1tzLyS6mUC5cdIuczq99T4iVXFwIPDbPTVmJAez2hm1g4qdLxpxI_yiNfpRWA_uSKPxsFR0bR8lIwE0Wem_PzhC33uMs_v71axgUcmdQz-xGgTLPo01S_p4b2yFWuzD4o_vUzBxUjX9sCs1bU7XmkL9c5tqoKNJnvStYYjrDDoy7stWuH2xF56AFVgjk0E9Usdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO3GA46_JNqh6kO0sh5zeXoWIa5l-I0VdR2GXLIoDpRkkHE-6zWscCfS94ocoT_E505ME_oSotIYbkyBUMG3DUZVf6DUfoAOg4AiU0oPw_8_5qB1phYMz_EO_8FFJpXk9LmwFiGEw7MFraE9f8XLXolG74i6bRT-j3OF6tmCEpNHZXhb_RgnOlv257Y2g1-IFMybk1ABTVEbbnevfSGjpRaikMAV8lpqFy6FmMkw8CXR3FlwMFIzToCbaS_FwqNqdAndeSxvwHoo_2w-nk-77pJx60yOaYbYmJUypT0x1niTLURGtKZkRi3ax0_Ch3rQDn7ujMrJiYTaFaoomxhMlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
همسر ریاض‌محرز در ورزشگاه‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97145" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFnrR4CJ_xmvl6713UKlVZUlPZuG9MdOtbQTJh0GbMffuax9orxRP2EevfgVjBkEiCEHSu2aYN03_vSa2gylGokXWXrc-_5vaMH4Haq5aAZ9rdQ2g8efvVMzhcL3BNh5R8RQE937YEmZpeTo9qPMgZw62ENoGZ_4V_yRwiyiAubt2o08ia_gN4APfMuviQm5ps7-_q_cCwZGsw-8vefiyY7cmHFJe0_-j72-0IemDpW-LXA59Om8MEoy0avfrY1bQ296CHnry-3weUvPnypQsUELIW2yjxI_c-xzu42J590D4cYa2jy8ymM8pg7H23wcqVgnovdEf9-SnnHhXhlW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
فوری و رسمی؛
گونزالو راموس به میلان پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97144" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEEOATv53qeVl9LsocCFne0yfUaeucyr3r7lttOMwwxfhw6k41-IS3ZdiCEj5lYG6iuQbu2PL4fE8w8v-E-4n-i2I0TJFmhKd400NpTY7RbR65eYdl6CcR8QLd7iU0ALcmi4mTo3iAermeL51A4Hxs60VHYQ5TtPvWRxVopmjqtUl9QS8XKOyyRZ-Te6EwTbAZe2CEvR7QM4AOwARZlhmTikIBTZt6-6Bb-pR02mmWBbCYa5r4zBj1I1xhuGdvlFXyBLN0ZdiJmXRig8U2XKsSaNI2qp37_iPobJ66dVLvXhhgNywOLXKnC9gn3LEQ-oHI_HCu8LhVhGz99PbEfvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
رتبه‌بندی نامزدهای برنده توپ طلا تا ژوئن ۲۰۲۶ از نگاه‌ وبسایت Goal :
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین.
👑
🏴
🇫🇷
دمبله
🇫🇷
اولیسه
🇫🇷
امباپه
🇪🇸
یامال
🇦🇷
لیونل‌مسی
🇬🇪
کوراتسخیلیا
🇳🇴
هالند
🇵🇹
ویتینیا
🇨🇴
لوئیس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97143" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI56XeyVo_DZxZMoqiBjn-sZzpKpVQVHxZdTjBzJLHVIh6VfzKzuY_bHhnBVZ43yOTEnbtTjeV7l_8VfsGguo2HykRxrCINFxXZyP0vPEKDChJVUglQSpJCGrVW4OCUseNmliW9VcOGvXYQHADBf5PWPLiTuc3_P_hScR0jjw6EeRBhzGVMa0E5M3uoMCwNnuAVhUyEd-iE1PhSaXgXqo_5I9p7UqnJ_ScpOc1jzWP5rR9WbCrbtqXnJqE3WBzHfO5IpbYIK_EOsffd7fcTUAg_Ei2C_AE_nJhAv88HeiGhsS8cNzsP0dbc9IrwO3OO3w__fCWFCLkxvlbCHRFyQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
❌
فوری؛ فابریزیو رومانو:
فعلا هیچ پیشرفت یا مذاکره جدیدی بین رئال مادرید و چلسی بر سر جذب انزو فرناندز وجود ندارد. انزو مورد توجه رئال است، اما در حال حاضر جزو اولویت‌های باشگاه نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97142" target="_blank">📅 17:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=qjuaImvd4YIHyZ79g4eS2EzMwD-6pPVBqShbNV_bDq17AzKBRD6ORwD0p2dEa-cpcWSKXJOGRoJU0Af3J2vIMwLzVR4yXlHEN7oywjCT-CK8ZlWn7LF8wCrmJ06BhnsIZ4UxxsSKtWALevH_m6UDODvX2FDUSRaosEqiua835wZ7dBwQPDd9GkZOlSdWKqAZ0PKYPS6EWng6l7E0vDlB_W5uLBD4aJ8b2NHF-FMNSLo7sM-HE6Z-kyVLnYL-qdH-fhK3zvRDUpFeJ3qQ2o2_dB8bnKlhkkVBU-JnmkucAB9fHob8iBiMUw_p6pRRQ2cv7pvEsrHBMi_x3XmeZiLQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=qjuaImvd4YIHyZ79g4eS2EzMwD-6pPVBqShbNV_bDq17AzKBRD6ORwD0p2dEa-cpcWSKXJOGRoJU0Af3J2vIMwLzVR4yXlHEN7oywjCT-CK8ZlWn7LF8wCrmJ06BhnsIZ4UxxsSKtWALevH_m6UDODvX2FDUSRaosEqiua835wZ7dBwQPDd9GkZOlSdWKqAZ0PKYPS6EWng6l7E0vDlB_W5uLBD4aJ8b2NHF-FMNSLo7sM-HE6Z-kyVLnYL-qdH-fhK3zvRDUpFeJ3qQ2o2_dB8bnKlhkkVBU-JnmkucAB9fHob8iBiMUw_p6pRRQ2cv7pvEsrHBMi_x3XmeZiLQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
اسطوره‌های‌بیشمار در حین‌بازی برزیل و‌ ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97141" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXClCROgwUHR72LigITGXNUuZ71iER4pcuMCWV4h7y0BV5sz7T7EqOTWEWrSI3ICmFrk3NEylLdBV8Rj13PEA178I9CkEuOhdMnio6XE7iFmN2dERy26Z7TyGgfhw9VZ-QKZs6ZwRuevilN04SUK7cz16C0MDxPYEoXOSMELPmdO6hRfLs9BbPqUYVpNfK0PfxjW0ffpPWTyS14EYmP3-pege9SeQszppNTo3qKAgvn0ShEQm9c-g1Ul8RT2FxwTQrjVU4lVCt9Q01fJrz39e3GA7oqxWhEJfy9OPdMGstG2obduOtYPW0zVn6bObuzubf6n45kFvtsNq6TF_fOnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWXRO6fGcgyyN_ruNLRgIP72sXG6d2U8mj3uoDEAReK55Ex-EDGMJgIi_AghFNOtHp8zTVMLPNomUUJnKI4NwhM1nheFYBvoOqajj6DQNoC0H_xVD17rHrkjHu2H1QaghT39Z_eNN3vL4-9yDdLh_-QXoXwFIFiV_hOSF-x-50unOKONcDnI1qJTGGSZNhrr5hzFIvAQGHM2N-jkqV3dx6CtnQGWQwy1__yBfZF1tAi_sQDv1ddcNMuTxCZWbl4JakcHdqyzaL5nUiqy36nCwOuRkcEiw_qyOlf9YI25RpKvx6nCbsmRBqGe-sEdnwotwJrh9S1mwfiYhhwIY3bHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtAbMf1VFm1U5JcwyPNszJ_aRl6B62rftTWr426x0bJ38cmV0nOiyWKtmGABnTgHgVa2Qd4GbCInrqZnepaizusuRl6dUhlh7VMrY6DVmYo5ea825qBBWtlTOQyIl-b7JhCvn1GOCaFdQHGCWTSAQSTzPcbRwpz3U-kEzKOTpgcDsEo2PP49LmbXZqZtchAmQBOQiWdcLYRqCp5AQotEiX1mirxVgxdsyzISOoqONC-p8UBvozTZS42jJ05qw9mBfWc4Z7MztZrYUBxj1bnUj9sOGzJ7Hi6Nq2NiQs8AVwmTsVAxGMqda-eG1MpbGzDQu9WOogbl8xn-VnEpqV5n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTBGo53SqqWw8cjEEfpwrOLVCm119bjfpwBnP0opIeWt5JYs929S7xhEUhgD14v3mXuYkSsp5cx0XeXy0cZx9XsluemJxw6HGq9BPACrm9xDIYykoq1f_tBgyKD40QySHBb-CEqdqq78jkohSlQi6W2P5tqI58mfV8Yj10YUCT7dFRy97FSWBPxfToBFhSp70WcJqyEqve1jxfgHY7LLnSfCY-jLPZCfAp9kTKRUi9JZdgay8raWQoV_KYpvT_M57R3zRT2eo21ijrP3SZpKpO_LkTxPJ95Dk1OE7xF3NAmL-NZsA2WjrhsK5C3PmFULZIKo5KkJH7jky-ApqZ4_vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97137" target="_blank">📅 17:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">😛
یکی دوتا منبع خبری آمریکایی صبحی گزارش داده بودن که جان‌سینا و زن ایرانیش قراره دو هفته دیگه بیان شیراز برا یه پروژه تبليغاتی. ایشالا که خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97136" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97134">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XO1yU98nyN_46KB5vtiT4pkOAQFTTcO8vqB05zMMhVjU1aEHckvuYwVNQ4IXstrxVYVmylA5FqtKc5w8ENUeIYelni_vXlP8SOnN2d6Va9Xrj2IhvfrJm-70Gj3Q10-CZnjsDqQq57sfLEEn32V_UJG-WAuGQ0JtZ4YOfn1HA6KqImdB4NDT7LS7tOkl2cBsOaUnFmDfKPjUf1H9fTkmidf2zQTZ4VKSqyJwAVHYyqF1Oz6WGZqA7FQsITzPc1vHVen3aBn2v_DTnot2qjQ5yBhMulwKupWW1bPmyhLupjS14y9ea28X9y7y6RpQxb9q4-uyr-nqkscrywG6YnHE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS_maPiAj703K6qmXK1wSq3Ug5VCnioloeL4QFDtKlib5Ui1vDQ6znKqHKMd_-ch3dklGm1RbFBuJC9kcSOUpaMFN7dGw_nUk6D4dkS1uTy3T_0i4UfDShkE6cteRiskzdJXfSZ2tUrSNk9u8TJ9p8ZpTnSwktUCIcD7rxDIPxAh3pnpzRlRFSrxcwrPZ_Wz4c1VECbKFsAvzX8x7SJkG0-iX2VMD5y8vK34t64XUZ_lChhqOOviof-shPiIRCJAqnokJ_bEdYzTDt7cYLoHUq4SWP5f_V-iw-zRivH0IsInTisMv4Eji3yEq_ss8aJpwvS_QFbqZpY4BxrosW1UgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهر جدید جان سینا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97134" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=ZJd9qZh60IZu3H3vJ8BKer3skOyvdOmgS8PKMrKhFqs_1kC24PdyANQ0TAoypoGVKjEuSELCODyNhAjvgV2Mr_l6CCOaDwHKsXHK0V9tADFVFEbYdi6Yb9f8ETU8jpXGHfxw_6fVhOkbgSBrkOApasmi8mPntERzJjB88XUgJfh7pdTUCq_AdtuygRkfNZ9W3m5z1RwkB2duvfdD5uSD_eJZ_1-EnC2poH5riCfY0M9nkISAF1hWrE6OQAltqAQDY6km-PPRnHecpMQkZxIlI8JRggcHBy5p6rWRb8aGCR4L7a6bR-BcmVkqjnp2uSb-gea605mJ6iE18jFzKCxeFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=ZJd9qZh60IZu3H3vJ8BKer3skOyvdOmgS8PKMrKhFqs_1kC24PdyANQ0TAoypoGVKjEuSELCODyNhAjvgV2Mr_l6CCOaDwHKsXHK0V9tADFVFEbYdi6Yb9f8ETU8jpXGHfxw_6fVhOkbgSBrkOApasmi8mPntERzJjB88XUgJfh7pdTUCq_AdtuygRkfNZ9W3m5z1RwkB2duvfdD5uSD_eJZ_1-EnC2poH5riCfY0M9nkISAF1hWrE6OQAltqAQDY6km-PPRnHecpMQkZxIlI8JRggcHBy5p6rWRb8aGCR4L7a6bR-BcmVkqjnp2uSb-gea605mJ6iE18jFzKCxeFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
واکنش آنجلوتی به گل‌ لحظات‌آخر مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97133" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYep70SPxg8pCg78X6OKR5KpMbKwkqcQtVaJluhOXqO0P_PEl0iwQWbKK5o6UfZRz5nFsiTbZ_IsPnbBauIGVuw-bEIWIKmVyakHfabTAoZvNv0FhyvvX7JGJkLZkIeHdU3x6wxs0jYrsrVWbdhQax20UF2iRJBfOYz2Yb5ng19LD_mZz1Ie1E0RDKR5_iImqja5ECR-CwLSJYbzb9KYyxztG00xceTpa6YQFE8uqXO_cbn-k_S6QZr_spttgTrvDX2esrwpELHqd3e_C-qi-YMVCGqnKOABqnPhMNdQJJVQ745GoLZqATVeuYrP0IKrx-9bxJ9J4ZDH7LhF56HX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
طبق رده‌بندی فیفا، پیروزی پاراگوئه مقابل آلمان چهارمین شگفتی بزرگ تاریخ جام جهانی محسوب می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97132" target="_blank">📅 16:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180
؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97131" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=dQ_x2HcQqReTNRYX7628vtTWlkjod7y9Xi-5jo5fzNiLgk1kUvw88j17r6BhocUNknYpkcoJAnBfx6rSwBBRvktgDcptVjXkg4tcISi5gXY5n-FkiXxHMinV-TH0MrBPYbppjxUdpPZx3x-aert0xj6uVPigxDNuDXxeQuYKFxLPfOGx_53BlSHg3PcxshPkj7TvjTo_5zuBxp64030_RrNoTn6Ojcg_APZf_QjLldKeEZfwTh-1Nt7NC5VmT6V7xXEpBPEIVYJiuyUPmnPfnU9z0t94AUYUsyuNNQq6Pt2OKvMN1nwfFonD-c7VrLs_awor5cv6IqrvaN7zZIXVhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=dQ_x2HcQqReTNRYX7628vtTWlkjod7y9Xi-5jo5fzNiLgk1kUvw88j17r6BhocUNknYpkcoJAnBfx6rSwBBRvktgDcptVjXkg4tcISi5gXY5n-FkiXxHMinV-TH0MrBPYbppjxUdpPZx3x-aert0xj6uVPigxDNuDXxeQuYKFxLPfOGx_53BlSHg3PcxshPkj7TvjTo_5zuBxp64030_RrNoTn6Ojcg_APZf_QjLldKeEZfwTh-1Nt7NC5VmT6V7xXEpBPEIVYJiuyUPmnPfnU9z0t94AUYUsyuNNQq6Pt2OKvMN1nwfFonD-c7VrLs_awor5cv6IqrvaN7zZIXVhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
شادی دو‌خانم برزیلی روی سکوهای استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97130" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyGQWIFxQt0-7UUyPmtY4zvPxBxiJkKFdwgcYBJx8E269UPHUyhEp-oaVEhSwVgrtGhLPnjWSkO3BqCUcqiIKUzBhCcTs9AAcuE1_k8e4u9RGRYme_zZnEkGCVcMC5orHNbYwT0qbI2ErH0jxrfK6Yf_9P7dDeWhKyRtrEr9TXA-DafBrd4mGu6JUVF6wGUu6ly-8HwYM95Sj1D6x_TN8h0rFWFW0x-RcNZIbYjAt5hC-pGml-uyB-q5LXis-HENf6Ya-24SEcbVEIF8hOkXyN8CvaDyiAx11VC65yFulGj9rNfU4euC_Y1XdmcuG3Qka3YZYynCXT595-41u615Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8 سال پیش تو چنین روزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97129" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97128" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=tPOykDGasPaLf6yPihWvSfjIdkpd0juUlhyGwAbcVRN-m9dAjkK6mlTt65MxAUHO4m-7p5h4cN_tra1GjFv75KmkbK2HlALp2xqugBg_ZkCWPGqPYaVIKSZwi-uRm9Ukw_AU6dvi7gAXWPvnCJn3MPwyH2RwoW0L3tQ7hKYVUhFUAZAZMLIpy-QSK2gI0UAQKawnvLYKOPoifb-7XbrsL1xegoScTzcr2J3c-2KcWDqBAjlFSs4FdVSvElAHOoeQVePebZGGSc5PVmkTkhT42vzksQ-NY4bpRIBlZ8fktnXcTK9xvK4ZkMzl3Dzjq5R4vLLu6i6G7tzQgETnJNVHnjmQD49OYA-iHn825FoHmswJkjbBW23nDIwrqzaieY2_Eg5KdF9k3L-RcwTuqcdg3n8TytDrC7mu2xKnG2k8eJmC6TL7mfwm85FNnQ3EVvjN2Zp3nuqyodW5Ge-9-O-WiIbVH_pjf5Sg5WOJdREzkvHcvUHDcrAFEqnTRnZ5O_TEIg5Y6v1ExWRQki6C5Z_oEDTQuqI0fMEhpNwXYLKJ-27TrXuM5auc4e5ca9g2D14x1sdiczqKWOJDZwFaLXMqyLV_gNJJcTBDjtUnZGv33yYAdlS5MDU0dRNkML6fXiOmDY4jrMHmmvyHsMG0iFbPjxpzUyUw-WwB7HBNZR5ZwAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=tPOykDGasPaLf6yPihWvSfjIdkpd0juUlhyGwAbcVRN-m9dAjkK6mlTt65MxAUHO4m-7p5h4cN_tra1GjFv75KmkbK2HlALp2xqugBg_ZkCWPGqPYaVIKSZwi-uRm9Ukw_AU6dvi7gAXWPvnCJn3MPwyH2RwoW0L3tQ7hKYVUhFUAZAZMLIpy-QSK2gI0UAQKawnvLYKOPoifb-7XbrsL1xegoScTzcr2J3c-2KcWDqBAjlFSs4FdVSvElAHOoeQVePebZGGSc5PVmkTkhT42vzksQ-NY4bpRIBlZ8fktnXcTK9xvK4ZkMzl3Dzjq5R4vLLu6i6G7tzQgETnJNVHnjmQD49OYA-iHn825FoHmswJkjbBW23nDIwrqzaieY2_Eg5KdF9k3L-RcwTuqcdg3n8TytDrC7mu2xKnG2k8eJmC6TL7mfwm85FNnQ3EVvjN2Zp3nuqyodW5Ge-9-O-WiIbVH_pjf5Sg5WOJdREzkvHcvUHDcrAFEqnTRnZ5O_TEIg5Y6v1ExWRQki6C5Z_oEDTQuqI0fMEhpNwXYLKJ-27TrXuM5auc4e5ca9g2D14x1sdiczqKWOJDZwFaLXMqyLV_gNJJcTBDjtUnZGv33yYAdlS5MDU0dRNkML6fXiOmDY4jrMHmmvyHsMG0iFbPjxpzUyUw-WwB7HBNZR5ZwAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97127" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB9OiYgB_i6qzVerzjJo3crBSqY7XPn0lsh5TQgsiWX_OrlRoHgv4OC3iWVQpb7JcxSfWIB9CErNFiXkeKVIDytERMhgAHKwJCO0Kr801cVdcdaWM93CM_k7HChiBAaQOQyZzvdZzLf8UaxWUBx2pJ8KECDNhdNaahlcVoYFX1Nrod_1AW6BYTW1Qrnt-me-DFULskDC0Hc_e9_7tied7fTT0QXn5BB5jiiQ5yUMN7tMwt5eZVsGaNgdU2HQtbLYwcP8kh9X1nwTYrcd4jJGwAqM778z5QyKa7XuZsIITkwtvmr-bd0hY0MTYbL5oEABR-AIrfanYltIn0zepp_2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسیر احتمالی فرانسه در مرحله حذفی جام جهانی
:
🇸🇪
مرحله یک‌شانزدهم نهایی: سوئد (قطعی)
🇵🇾
مرحله یک‌هشتم نهایی: پاراگوئه (قطعی)
🇲🇦
یک‌چهارم نهایی: مراکش
🇵🇹
🇪🇸
نیمه نهایی: پرتغال یا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97126" target="_blank">📅 16:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f012c953.mp4?token=clc-Qth-MDT6ZoVXTo17H5tg72Rk9XWByOVVk9A9dKtp-4Ds5Lgj-lZXmpbysLJzEcHcgyqd3OfXyvhwdUr-Jza6XZcqAC43LMLAiXgMYDi5HL2o59zW6R88J8-HYCayCuBp9Ez7eA8H7p_5iz7LmFNqAtPQUPYB9zZxTbAwkXavwHng9nfsmdBQ2trq7HomMuqkkWdOO37GMHrXZ0oAIQJ2X2gWxsbsIuklRqghZ_QmxjMwvMVoD1IjBWgNbLWJEWbNMTl4B9yOC60Ud1qM50rlauAR_IabukUPpEE7-KmhpuDJoyP4w3-FeiSX__TlxOXIn-8uLulPO_rmPwyyqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f012c953.mp4?token=clc-Qth-MDT6ZoVXTo17H5tg72Rk9XWByOVVk9A9dKtp-4Ds5Lgj-lZXmpbysLJzEcHcgyqd3OfXyvhwdUr-Jza6XZcqAC43LMLAiXgMYDi5HL2o59zW6R88J8-HYCayCuBp9Ez7eA8H7p_5iz7LmFNqAtPQUPYB9zZxTbAwkXavwHng9nfsmdBQ2trq7HomMuqkkWdOO37GMHrXZ0oAIQJ2X2gWxsbsIuklRqghZ_QmxjMwvMVoD1IjBWgNbLWJEWbNMTl4B9yOC60Ud1qM50rlauAR_IabukUPpEE7-KmhpuDJoyP4w3-FeiSX__TlxOXIn-8uLulPO_rmPwyyqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
مراحل آماده‌شدن همسر‌نیمار برای بازی ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97125" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CukL-qli2qBA9nf46jzgmeEGerFNYvc_xfkHLYUEOFQ_yLyU8BbSaBiqG1_8brkVasrpQ2xzLdII32GuoA6PVwBD0RFsIkKOevidxB9RyqfXwNEXn_8ceFwVC9HsXwxochTe4aDP_FBKbOVyN6utctIyyeIqsOryQ21hAqFG_mnsZg95CRW8S3lF8tj1OnlVqA_nJqvMFk3sHoHxgOHtLmxVdyqKOCrR-zrI0hXByBeXVgZGlQGgs2sxMR1nBTbzoAiJjO9dGRidQ3zqKMgMnx6XOvEQFYEXg0ID1XhbuiGPbTZbXq9-G8j5UIsjkBjWjLTSmO7oqbvjNd1Y394qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالد کومان از سرمربیگری هلند استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97124" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=c6HXzayVh07_RKxfUHuaG78f4AcEWNSenP9U8pdKfB36okAkM7ejKqWz3oR-s-6Bh-gjlD7jhhpNJGyEaSBmv8QtlXxVAqUozlgUaLHUvjqal8WZ3Tda6TKyOtknjJ--70xCYbhog8-Y92qysGcY0ViHDuOEHLZIVaR3NZ8biQaCfcFxYjbmprQvLiImbCplu7bHnOygZGfILCqj_x0UIJN3BgtJdC0dXTjl5UbwjmQZ2dUD_-8SneQi1jmw9jlbIvZv-s6ESiP4iIMUSrJyxpsOAGrIfmkVnSLPz_VKpJh8LYlkh7oF-lstLcegK3zsKoYhA37WYcRpwD-nauo0ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=c6HXzayVh07_RKxfUHuaG78f4AcEWNSenP9U8pdKfB36okAkM7ejKqWz3oR-s-6Bh-gjlD7jhhpNJGyEaSBmv8QtlXxVAqUozlgUaLHUvjqal8WZ3Tda6TKyOtknjJ--70xCYbhog8-Y92qysGcY0ViHDuOEHLZIVaR3NZ8biQaCfcFxYjbmprQvLiImbCplu7bHnOygZGfILCqj_x0UIJN3BgtJdC0dXTjl5UbwjmQZ2dUD_-8SneQi1jmw9jlbIvZv-s6ESiP4iIMUSrJyxpsOAGrIfmkVnSLPz_VKpJh8LYlkh7oF-lstLcegK3zsKoYhA37WYcRpwD-nauo0ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم مشکل دارن: نه مردم فلان کشور وضعشون بدتره
❗️
جامعه توش جُرم زیاد شده: نه فلان کشور بیشتر مجرم داره
‼️
مردم شاد نیستن: نه توی این کشور مردم غمگین ترن.
❗️
اینم از فوتبال ما مینویسیم اینجور فوتبال بازی کردن قشنگ نیست بدون بی ادبی ...جوابی که میدن: فلان کشور بدتر بود. یه عده ام که متعصب الکی بدو بیراهاشو به ما میگن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97123" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">💥
🇧🇷
شادی‌طرفداران بنگلادشی پس از صعود دراماتیک برزیل به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97122" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=lNB1byWow0KrtJQEfOQHcortmMF0_agy-cGa7JF5bVkm3q9W9BEje1oDIIFd_BkXahpUtGdpk6AJFLH-2tdhiM-cFIe_5eVlmK4oY3nuT3vRPmwRJDnpZ1trL_2baARP3zhzp_gFE7SYCJWc9IYbvXQXjqym5JpV3CZq0r2TCS4WlOaOL2cUn3aKb18a5wOhGmpwZgn3eMAEbebcXttj4o0QD49Jm2EddLvj5S5nwgaxI2cL1lQige0ma5IR2lN6_KTHjtaP1LXcoxeJMQSkGQ-HIi_llLfqwLKQktchtWCFBm-GDpQjqXWt_BK4TSY4oYCOj9TWzjR-q0QMV4AJAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=lNB1byWow0KrtJQEfOQHcortmMF0_agy-cGa7JF5bVkm3q9W9BEje1oDIIFd_BkXahpUtGdpk6AJFLH-2tdhiM-cFIe_5eVlmK4oY3nuT3vRPmwRJDnpZ1trL_2baARP3zhzp_gFE7SYCJWc9IYbvXQXjqym5JpV3CZq0r2TCS4WlOaOL2cUn3aKb18a5wOhGmpwZgn3eMAEbebcXttj4o0QD49Jm2EddLvj5S5nwgaxI2cL1lQige0ma5IR2lN6_KTHjtaP1LXcoxeJMQSkGQ-HIi_llLfqwLKQktchtWCFBm-GDpQjqXWt_BK4TSY4oYCOj9TWzjR-q0QMV4AJAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
❗️
اقدام جالب نیمار در بازی دیشب بعد از ورود یک خانم جیمی‌جامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97121" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qESArOofTWEytfn1v4h7u3BxDsaM_g5Y26SSfBVSJjky4GeCA5hSFDG2r0y3hrPBPFcfPWkXCnFhheGAfRUCfzNYc3XEco8_uinz2RaNn7CLxklO0m0451Ov1BVVW7Lrls7TLo42_KB4CyyaT5KP6oVRRMdZbsa9cezBvF0XfHZ1lMYoq-FzWo4tRhpUtNgQXWnj3m28CNFsQn8w0wx1tJQ7oRvdCqY2sdyIMjt-IzPuFWXDqmL3m5v5swZgiZ6UtpwMd1tlvmD2zg9gHTnr88xre2n6lJP-MQRdZb6AKZurGCy7vAxCNm709PmMPCbKxh1MmYEAZFdkJakkQb_W2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
- کوپه:
😂
فرلان مندی پس از اینکه یکی از سگ‌هایش یک پسر ۱۷ ساله را گاز گرفت و به دو سگ دیگر حمله کرد، به دادگاه احضار شده است
❗️
دادستانی خواستار محکومیت مندی به شش ماه زندان، جریمه و غرامتی تا ۲۲۵۰۰ یورو بابت آسیب‌های جسمی و روانی و دوره درمان است!
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97120" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbpVjb3HRZBDKDYJ2oZdTjQxYxfAAVfoS_xDzbvRRNQef9ZaSiMWLtHJc2KBM9BiP3kHaxEjjRKBYcSq_Sh4dlAHaXHEARIrWFgORgVkMqN-1blm8IvX-pv-rX69xAR0rw37XxIUmGhJ5qqlYTqgIZ7JmnIlLS9fETVD04MYCcbOx8L3HACCf2esIfvDdPogwDkMSLD-QFsQzEpUWIPJN8zIBdcZgMxqdqyjrjZRTrSev5ASkclIQRsfChIj5AWc7giQXEvWgjIWAFoKCqXA6_hHMiJmbhOcJoNi1qN4VRtxKfSw8oaH-rf_Hdy3S_tb_zCALZSV6Y66F1VTu65Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حواشی‌جذاب مسابقات انگلیس در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97119" target="_blank">📅 15:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=CrW5k6HdHLkcSqmzxn5xtpjmF3Z849deFZ_3rN8f_nclIbaLDRt4nx2egxYP0KbRnLq8FTI1hhK8aMcaXjgDNi4hePoClE3CCIXcs2J36932kDcr8W9oH84MYWuJRCeNers54Nl6AIo9CwRTI1QBuG4quRM2VqcyXF1Em5NRm7_WmZybgKsrLSDb48M8AKNM1ByfIJ21qrP58vosmrD-oVroiQQqUTaiyCaNbVUOHW7srlHQAJaJqN0jqm_n9vX5SYcW91bR17ZTsnZoDprNpCNlk4NIEJ7Ux3j05H9sb0WYmJG26O7Z9mR0CUQ6r-xcpNmzb_N2RVOPyg6iKB5zXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=CrW5k6HdHLkcSqmzxn5xtpjmF3Z849deFZ_3rN8f_nclIbaLDRt4nx2egxYP0KbRnLq8FTI1hhK8aMcaXjgDNi4hePoClE3CCIXcs2J36932kDcr8W9oH84MYWuJRCeNers54Nl6AIo9CwRTI1QBuG4quRM2VqcyXF1Em5NRm7_WmZybgKsrLSDb48M8AKNM1ByfIJ21qrP58vosmrD-oVroiQQqUTaiyCaNbVUOHW7srlHQAJaJqN0jqm_n9vX5SYcW91bR17ZTsnZoDprNpCNlk4NIEJ7Ux3j05H9sb0WYmJG26O7Z9mR0CUQ6r-xcpNmzb_N2RVOPyg6iKB5zXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
طرز برخورد صحیح ماموران امنیتی استادیوم های آمریکا با هواداران بی‌انضباط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97118" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=vTI2RIzITRFYazPORjM7ZnLvv1zfWzVsjsEuscPx8OZCcLjDwCvqSmSwl2LWu1RGfPHBoOIisbNcI1szp_qw_ZVEdodueMyotptriKx8363zy4HuOlK1swjVtSlBD8ky9O_Hdt4PfYVslmXZBqxlW7MhoAoZw2MfL38mvvdKwEXQ8h7dMLWxA6ARg6CZ1rnG7os9RBkfR8iciVWRf_rhacoCscjfEQwgSHHCLFxmGxoRf5q_dTQFmDCW-Eyh3PPDCOYE7nXjXuUf2IQQYuWIDdK7H5-FEfT9yigPl4ij4vPY2Pbb4WpeJi0ngmOecyO3_Y5ECNPCHgkyo7ofqL2BMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=vTI2RIzITRFYazPORjM7ZnLvv1zfWzVsjsEuscPx8OZCcLjDwCvqSmSwl2LWu1RGfPHBoOIisbNcI1szp_qw_ZVEdodueMyotptriKx8363zy4HuOlK1swjVtSlBD8ky9O_Hdt4PfYVslmXZBqxlW7MhoAoZw2MfL38mvvdKwEXQ8h7dMLWxA6ARg6CZ1rnG7os9RBkfR8iciVWRf_rhacoCscjfEQwgSHHCLFxmGxoRf5q_dTQFmDCW-Eyh3PPDCOYE7nXjXuUf2IQQYuWIDdK7H5-FEfT9yigPl4ij4vPY2Pbb4WpeJi0ngmOecyO3_Y5ECNPCHgkyo7ofqL2BMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇯🇵
انیمیشن حمید‌سحری از بازی ژاپن و برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97117" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqbJD2RQMySrwIxmpxgVX1--P7iybL6c-6-ooA6NdFHPGlESIqz8OjwfdEs0t352bWMPIyQVa-VqulBVM9lZN65RU9fMBQZD5BextlRj3ZYsFRzwaFQvq1NCHYs0kSNULaLpStXhsU6DgyohEZMZUGPVrOLKFfUt_WBtkYBeQGkkprKgEFDi8HE7Rsta0ggZIaji1GWyKIHOz5A0bbKK8CJGw6IKMBZpH6xYJs8jyHQxcQxjLh7sYJ4kV2cQPxVNzh-Ya0GQDugD_Ya14GFZ-mYkIOhRLm4K-onFIY7NSDKZo0Pn_v5Lc0HUVt684KrfN-L6wEsfLsRkWbc6J7Pw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوکوریا :
ترجیح میدم کچل بشم تا یه تتو از لوگوی بارسلونا داشته باشم، من حاضرم برای وینی و امباپه فداکاری کنم تا همه چی رو برنده شیم، تمام کارهای کثیف داخل زمین رو انجام میدم و فقط هدفم اینه به پیروزی برسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97116" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=GLH4prLYG6oZn8a3o_RmbIg4Zh2LN3nSQjbvuLdR5F51CVnUTxK3_DT_Ugo5pMQ2dM45LmywckZQfRcDeLXGnO8ot5Lky0Txoa8KruEaTepYVpHyFOQUdwM6k-rSCfllNzc5srxkL1ukaIDbmq-CA5qcFsWArbj6DbJeQbJQKfMXStlu_91yE9r-BuJj78T3NgM6r4tpdQ5vetQaWg-JIT6TPStceb1sCqcjFDxcRaV6KMvQ3ltEhyfGUOjUnTL9G2XsDYgDb-XiXDMDIF-Rm_T6xevmuvy2I-gsWYGEGxx6A_8ZUkcjBdyoOBAr36Hwp8SaibJZ5eOq8CVwd6Pkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=GLH4prLYG6oZn8a3o_RmbIg4Zh2LN3nSQjbvuLdR5F51CVnUTxK3_DT_Ugo5pMQ2dM45LmywckZQfRcDeLXGnO8ot5Lky0Txoa8KruEaTepYVpHyFOQUdwM6k-rSCfllNzc5srxkL1ukaIDbmq-CA5qcFsWArbj6DbJeQbJQKfMXStlu_91yE9r-BuJj78T3NgM6r4tpdQ5vetQaWg-JIT6TPStceb1sCqcjFDxcRaV6KMvQ3ltEhyfGUOjUnTL9G2XsDYgDb-XiXDMDIF-Rm_T6xevmuvy2I-gsWYGEGxx6A_8ZUkcjBdyoOBAr36Hwp8SaibJZ5eOq8CVwd6Pkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوشحالی شدید میثاقی از حذف تیم‌ملی ژاپن از جام‌جهانی؛ چشم دیدن پیشرفت فوتبال کشورهای دیگه رو ندارن تا به مردم اینجوری نشون بدن که تیم قلعه‌نویی عالی بوده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97115" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=vrrCaeW-rx41MYmaHe24HpAjCyT3rpx801QieYc1QGanw8f-Z4oZBUftm91Hl2ToWm3o00yDzEeVOLAXmmLIKtbg8sdEeyJdV0_Yg9oS7AwQVnre4ETcXqQNhFIYZllD-FxRh9YB6B8vsuJHl8eUL0sy-ZhY-FvPFfBE3jCm85-WCJud1jfjqO4-kOq3ob33TjLHUTp8ijvD8reZoaMtEXSZP392ADpTOpAc9jJcG-p_jeSJeGUw9XJbsXqVvTtOlFxvdakxtpJP8NVDeuRJ5QRDJ5VU7iZqvpfL1qXEiQiPS7T1-6QSdVX30gaSgisd-ZTGGRjWq_KST5VCizj7d1J9MEFKYCwBhLWO8AwQi-n1OVePBtQIxAGalTCJnLidbdcP5N4p-Z47M3c7iHRslN3dODvJYVA-ZMJG1YjU0X7WVEGLRT3LYcGkh1kzwh2Qq4dle9g4ZmzjGeov3WYtzcA_zJHeoRDQd2vCy_ttWj5EG0fNiO18ukMe6_4Qe7jAmi8Z26eUKtmvTqTBn_pdbEc4vOYFYw6ch2wTH6023G6AsBO_3N9hyZmy5NQ3nw-aM_V3TLiu55IE5idMMCKOMNGwx4iveNeclBjHFJPCve-PUVx6DwtCGYguaOY1po58LHsAPhh2dD94Wms_gW6-DB0_K1UysI_wjz_oLZs_0Q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=vrrCaeW-rx41MYmaHe24HpAjCyT3rpx801QieYc1QGanw8f-Z4oZBUftm91Hl2ToWm3o00yDzEeVOLAXmmLIKtbg8sdEeyJdV0_Yg9oS7AwQVnre4ETcXqQNhFIYZllD-FxRh9YB6B8vsuJHl8eUL0sy-ZhY-FvPFfBE3jCm85-WCJud1jfjqO4-kOq3ob33TjLHUTp8ijvD8reZoaMtEXSZP392ADpTOpAc9jJcG-p_jeSJeGUw9XJbsXqVvTtOlFxvdakxtpJP8NVDeuRJ5QRDJ5VU7iZqvpfL1qXEiQiPS7T1-6QSdVX30gaSgisd-ZTGGRjWq_KST5VCizj7d1J9MEFKYCwBhLWO8AwQi-n1OVePBtQIxAGalTCJnLidbdcP5N4p-Z47M3c7iHRslN3dODvJYVA-ZMJG1YjU0X7WVEGLRT3LYcGkh1kzwh2Qq4dle9g4ZmzjGeov3WYtzcA_zJHeoRDQd2vCy_ttWj5EG0fNiO18ukMe6_4Qe7jAmi8Z26eUKtmvTqTBn_pdbEc4vOYFYw6ch2wTH6023G6AsBO_3N9hyZmy5NQ3nw-aM_V3TLiu55IE5idMMCKOMNGwx4iveNeclBjHFJPCve-PUVx6DwtCGYguaOY1po58LHsAPhh2dD94Wms_gW6-DB0_K1UysI_wjz_oLZs_0Q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
آقای‌ناگلزمن خدا ازت نگذره که دختران سرزمین ایران رو اینجوری ناراحت کردی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97114" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=It5uFOBEOnF_oMJFCutBODUNsJtr9LZb064pkEXGTMqTF54HRQcu2IEKAvw1duECwT9OfoooLmt8AMlZlw9LXoNdh3nhbYqW2dA0JsFOnbfh24PtCC1z6VeFtBvjxYYOrVPsCGUcTaMk8WetOELwIi72LonqvPUN32jFjuYD9ww55V-kroptP46hd0SK-lW_bDeBWgpwG05gNWgxIqzUwsrNzHvp_IcLKqK6wjf1gMImjcSxsYUIkYMgTDq3WD6JT4wvLt5zDcJ62f7fuikV1PNKurrmKazz3PnSyeU4DqHoRWj8RTjSzQM5FfqZf27ku6cy3FY_TuF8qPggqKu2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=It5uFOBEOnF_oMJFCutBODUNsJtr9LZb064pkEXGTMqTF54HRQcu2IEKAvw1duECwT9OfoooLmt8AMlZlw9LXoNdh3nhbYqW2dA0JsFOnbfh24PtCC1z6VeFtBvjxYYOrVPsCGUcTaMk8WetOELwIi72LonqvPUN32jFjuYD9ww55V-kroptP46hd0SK-lW_bDeBWgpwG05gNWgxIqzUwsrNzHvp_IcLKqK6wjf1gMImjcSxsYUIkYMgTDq3WD6JT4wvLt5zDcJ62f7fuikV1PNKurrmKazz3PnSyeU4DqHoRWj8RTjSzQM5FfqZf27ku6cy3FY_TuF8qPggqKu2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvXKT0Hyp520VkU0N-_tQTxpBK9F4bkKle4pWOy-BxqxAxFC4zebLftISekrh9mu9CQxzLSRcAH0P7e3UbaDFOc8fPxN3mEMFp8vYe6nc8BOQ4Lpr_GC5TRft-n5TW3E7UQzw9a0UgkBefLyz0FMvzS-_b-gC0Ntz3bObYDV2ZzNycr3486Ro7mx9AFyYl5VNzAizIgLrwI0_1oVetLS52-q9yCOs-IaXApIzN1lSeimJbpox_8fMOEdQQ1EW0K-diFGgqgq0rx_KY7UOmtTaRAdyViCjo23qClx9rm4O0zRNifunfWK1o6aNTuTOEgrHLwRFNZqYDNnJ3U82VRvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6fe2vRDCtmX37AT1jr3VOFtQVjHOyqXnxurTTEtzoaeTZDg-bqWUqbAVSn16ZH3s5jjtAhsrd4YFaMoMD6netSXLzF2CZef3RyN0nizP93LxAZPy0ZxX02xVG57O3Qf4vdfEbtEsH66yshnbCC6RA8aumfnBTgoybw3MPA3ZAVGxslZQOLTHv6DFjpqmj1CIaw-6dCp2NyOr6BzqKf6ppzUsmHd-66dOOSkigvrKIqqZtKCc-kyqerrspSvzZzxul87GnyXq2LZteYN_F8jG6Z6HrGfhMhCOMjsmqqSXOT8EfgC6c6VWjU4mEuOqI3Jn0M49vN9CJ13biYD1pKgIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRAumbdJkdofCI06gn2ft157uhohKRAPyBYWli4mehzO2K6CbncHY0GZrRJ25CWYQe10nA-C4rm3z7AH2eo8xfHlOMVvCCIxDu4_eIg5kGhF1YhTLjbuvn3bt40TXiMf2CYxL_I8WdZU-x8t2mslUWkyDPVwW5ZtuvNFobwCWxfZnoJxikRNRuI7rfMQS2Xh3ooxqWMjVl8AI7QNeqpqToDGXwJTBTV3xSUr2ZScgp_InBVy0WLufdRuX6tpsrn-ijc63XrROSx9G1M-JS1UkdNKQRbyDGD-9tozjXFZGXy26iSoYW23MZqG_F1f9w3Da1VCaTiQkBE4fBS_WZy4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM8pfAa11sNdj5jkP_KfK9M3saLbsRt3RJ4i8ugL6nRavPX9qR2EsVfFxJQJAFIgvI1GmbvWbYqWyZ2XpqB-6dCzMvmLt7hYqcU2s30pnhQ7LS-6tyLLl4-DigrhQ7MOk8Gp_5e7Lq1br1iLOxHeIpMmg8uRWgZyazP_X-MSzh9wvJtzv-8ajbp2EygxxB-Z2LVrcQT2Zx37HpAD4bNlGaYNQqSShqHx2gb0oulHmdb7TPIGm5-uROAzaoJoh3pOFKWvb1Nk24-jN4T6nNQzGvSE1bDhX5pCjLtB3HAERi4LORk0YXM0fdK5B0h5x3N1hIuhyuYSTG1YYRpvukt4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-VNCAbWDmeM7KEFpx9gNglfTw4u5DIyjEZqpzRp9hJdRJJ5bDRMCdUmxSPzqebiXtZSp_yLmemBtnpsdTDk9UYBcVyYszI0KDW3hU5hzAPPBaIB7kvaEA9eSUC_vTDQJKyOF6ZpE288VEnUPmP0TEGycOo2y0ET-PtzQp8hsJ47KDfRnXavnD13QN5-vdKXsUrQHESzTzb3Zibuq3h6JCGC97AkgS0F14KsUO0ko7aO5oV8zCeaVFnXq4ZXiZ7GH0XkpzsBDdQ_OqVDCSegArVILtmpcx7yIQdAWHdgjrr24TGoGdEn9TkSqbq_XwWSa9_CH5PYXg0CV4VGiVvp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lveapnshaJEJl0_J4gxXu-0C9zVQICZp-rWzTSW7nQiIpoAe1JVLY-L7JS7GdtpJCb-K0lIzbKZmdty2_PzvpALyg7D1q8LyhIvWqAYDjDPaTRRjXUg5MBQNWoLYbtF2uIyImOa4tyYbsqwDrxI0fTzBCqWdnCS0Ol0BfANNRH5UgfKTc2vL0b50XHsjzo4htr1wErSMM2wDgAiItQ3GXcTG-0TR8M8jWawaTZ_P-sesIcpDwEpiacdumL-ch7TrvrXAyM3jCBDnYBhly8Y2FNydjKJzCOeCTS0_p1UEe2prpAJHR0F6KfgjDyd8wgcT24TM0v2eAzYD3COO8j-Khw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_fOAD5PcRFtZoynpxA8AIscwjQDS9TqDtI5pBxZVKFsVDGhdjPly_4dC2CjyVKSH_fJ9mT9sQTCzu7aBBu1jLftCONpV6zUEmwbcCO8aBk3vfwNfPaowi4pRJ9aYinl0x6eIusF_WXm3lbJkex3bQWh8Mni8VY5aPCtC7YXoz1kbMNY65GZ_BiztwUttiCLBsu8xMXhugy-p7A2lpB5ZLEX80yqWgI_bZ91U9NpxeYmVIhSI_rgAarXH9ptvum6PNs3oLn5uvM0AKvGLKjTI0rkzZC7eqNbIp9RmuVFZeSlK5uPX1wfZ0CiCEjFHZWNkoyi1EBc6k3yt_Yg-_ozZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR1xvZOFuJUBhmKAc9O2w0tN28Fry_1jVQ4Kw_l706Ym8I9SKL9_xjtih35-Zvd0FBCBetxkNmAYjU9NIv1-nmUfAuXLmeLOCgRrc1hbvR9Lj-UKZDsOmRapzlEeos-xiXPZNRJI6NEb-lqs5r8pU0bXlkBBcxvFZsNpnAANaj_FAtxRclcs6m8oLV3reGs0yx1MvjVlaBgYbNYGaKPLN_YOvsYdDbwPrABvRd7zFVbDZb-zUdVPnX-tNsAzJIr1dazBVkZ8gKt6MF9yqDg_dT4Jp5cAYbQnTdjaXX5hDBO52f3Udjt6ijw81yeiBNvGW-hVEel-qlHWokDyvyVUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIT3aczvlgkWYX3-wELnW1fQmVGQxPvnzeG31cKlwPdmkjYmVhn9YzX2X7ddbeMa0QvcvsCIisgb9uxJklHh4Xp78kgeWW-DTsnRbNHh7oJj7tA1soo7vvAvUL1eMDnYH7nKjT433hY08qBC35DqOG0HReOhTPpKAZYlre00Q8ga1MIrIAlUyH_-_Ccul2MoBmcXDDETcxIdi7fOY9NGQoiUiYfx6nL0dW7V4YQGIgsKcmkPo-Z7h93Ws-OkmrgTP_e2fb9Q70q8q2D21Cfh8NSK--ytQ1USVl5S6nFPkEpbJ1bHskoRkGYdBdahCZfBK0tppkuORHzjxGN-87ZqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/st1KDr8lnQr4wMSCZ2NhfqKQTfruVYGM2DAwkkHnRJWhJ2xp6mmvykiTj44itsz6w7ClDGLdMMcyFaIIpeFRba_rh4VOUscIsGAfM9XCXTlaEHmDYzeG8IC4v13at1bhoJSETF0v_1-m4_JHv7bAnPpBtgicJ0oX_P42CJOpaKV6CUdodkBwaeBrKmtE7qg_Gb1_N679e57Iuvbg9HOMjiB0_ab24kEVoVF_cDKKjiOV5-gemjs4Mj5WAXBpiRpHVSzyvq4ZzyagDmBHmIQIIo4qChrg3eSi__wZ-RrdWuUp7phcB1-BrRSs4hy2mW4DsMTZ8YDGs0ng-7s_AzzJFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2zhQlEU7UjbyrG4gl0VDFDcsxO33gbESoN6BU8QZZiBbp3VDNuyGQq14vDOCe5-zWd1YPVq1bVZmeOpLoeJTJgpNPXo0yVi-8zUKzZDHcaUAQiCtjdV13sq5_cvazOX7bE8Ias6fCZ0vY2Mx0-fN76wBX1J2I44AKCvGkK30XlNTGskAmqno-MWShw2zdLLdoOHhgWhZ6VNAcc8-XIl1gD5WANftZLG76ch3fBg_k7t6y9Z7nQtxAcwpCu2LjeopUA5DQWWBRRMYOLmTq2mBHN1u8q4sjVIsue4rLAcPWWFsN568mFlH3PEEdS2MSA_1l3ovpxQmtEJabWahPmOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=ch2J57ZWUYr-O5sh3ra-_8Lg3RYcbGZoLspc1Ox0S3zLI5cGlnKjzWNlNyRvkW88HTAxl0bA7iIhWM65MCRJ1_X2NO8Dqbh77DPpi9Cc6sbpo--hGedkaOOqK-ushomKePvO5k9qCbF-6_rcnOP8U6m4EFLGi1pX_xX-maKsbQ_SKu8HalKndNWeD2hQgu-jQNL7eOfWp-hQT17KthC9eA1_SUHZQ0UWCve0seHyXEq5r_aGng6YacrG7iIB1P15j97J05LV90OKsuBDt7m5CTpTeZiGn6MUUHGvul0H12VhJmx8g5z9KFmE1xXNLvq7lXE-EDYVM1aPekmqU_4eYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=ch2J57ZWUYr-O5sh3ra-_8Lg3RYcbGZoLspc1Ox0S3zLI5cGlnKjzWNlNyRvkW88HTAxl0bA7iIhWM65MCRJ1_X2NO8Dqbh77DPpi9Cc6sbpo--hGedkaOOqK-ushomKePvO5k9qCbF-6_rcnOP8U6m4EFLGi1pX_xX-maKsbQ_SKu8HalKndNWeD2hQgu-jQNL7eOfWp-hQT17KthC9eA1_SUHZQ0UWCve0seHyXEq5r_aGng6YacrG7iIB1P15j97J05LV90OKsuBDt7m5CTpTeZiGn6MUUHGvul0H12VhJmx8g5z9KFmE1xXNLvq7lXE-EDYVM1aPekmqU_4eYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC6WtwQSRHGTNI0kSk4JRtuBqBg9sWPom3tzmhXluceS7a1CEMQOSQvAgiUQfqB5RX1_0Wu3C4XALfk2xhCCa91xhagfnD4gm9ESd8mebbIAZmz3EOBINF1OPRehZ-om72cg5vUpCA-Dz8eMfo7m7rea6LXWIVPbjFiJhSMBdCzODpm6IhgN8Rw3UxjE6PVgMxWX7k5bzefoDgGvFHu1WOp7eZpF5Oeyz6bPakwaoPgJn4vEe0fpnsSBudn2UecWND6N8uFpceCp050hAYomeXFOCDoYZ2_0LfHYry_CqTihHvDPMybY4gGzyTI6HhzNfPH0msOiKkLHiWstLschzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=fFrdAg1K6284k9T23QFzpODF1FZmyIaWSDReNmQXxo1r4VDrY34IzXn3xQQwtpYcCj97rBd8_-Z5tnV43dWBZjXJyE0GLhH8HaqFU1ghncKPJ_rVI19j-xpFfXjoor7tZz5huK3-zq-HxJYrie0ULa2xORP-558aG5EVqNxQ9d9ndgePj5RMg75z2XB0iMHfVJUGk-nkw4OCHEac0-9svYyEpTmx7K5pFqAs4yi0LLe000p65r8eSPGbxBYdXhKc25VF06T-zQMUbNXjoXa0UY-Qi-WPOF8Iy9izo3KxLwp2XbqlMMQehsiOpP72WlMmNi2GkfLE4dkU-x9MBy2X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=fFrdAg1K6284k9T23QFzpODF1FZmyIaWSDReNmQXxo1r4VDrY34IzXn3xQQwtpYcCj97rBd8_-Z5tnV43dWBZjXJyE0GLhH8HaqFU1ghncKPJ_rVI19j-xpFfXjoor7tZz5huK3-zq-HxJYrie0ULa2xORP-558aG5EVqNxQ9d9ndgePj5RMg75z2XB0iMHfVJUGk-nkw4OCHEac0-9svYyEpTmx7K5pFqAs4yi0LLe000p65r8eSPGbxBYdXhKc25VF06T-zQMUbNXjoXa0UY-Qi-WPOF8Iy9izo3KxLwp2XbqlMMQehsiOpP72WlMmNi2GkfLE4dkU-x9MBy2X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=HVpCDPvxCvnbcUSw5jTevN0rIecS3JK5jbOKIF4-txjNpMZoD2LCaZ5duXP2RT0d7pHXLgcMg_FgHcu87L5Yz70glzBwSI1J_OYsyoikeG_NrXvun2Z-NAzkZpHuL27wj7MxyjgBaj84DMLnokZbOHjQY1rH4sJLx_rht7gMuVAJlJKCbUMzMLieV-Fkj2IG7lgsTZo17aEc0pv9mVD2KPFVyrTJ2luuag8uzFJku4Z9kCXzIiU597MjebCxnsU3hwwPLYETyehAyr_Hd-a82jLiDT9zWDRa4A6la6roS6h3BpExD13DikD775VNCeb7RwZQbm7d1a7E7ByYsMoHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=HVpCDPvxCvnbcUSw5jTevN0rIecS3JK5jbOKIF4-txjNpMZoD2LCaZ5duXP2RT0d7pHXLgcMg_FgHcu87L5Yz70glzBwSI1J_OYsyoikeG_NrXvun2Z-NAzkZpHuL27wj7MxyjgBaj84DMLnokZbOHjQY1rH4sJLx_rht7gMuVAJlJKCbUMzMLieV-Fkj2IG7lgsTZo17aEc0pv9mVD2KPFVyrTJ2luuag8uzFJku4Z9kCXzIiU597MjebCxnsU3hwwPLYETyehAyr_Hd-a82jLiDT9zWDRa4A6la6roS6h3BpExD13DikD775VNCeb7RwZQbm7d1a7E7ByYsMoHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTb7LJ2kXbna76z6GgYCZNBP9Oobcp9NT7MnRvM4H9cKffWV6g9EbIdy0ct9bjYwvG5HX0nBw8zfyJjrye77JycheQwHqDzbps5J62ZGR8i6GYDHh93YBqRw7AWZ6bFl6SgeC8pahagm1jlUx0U_rhZDNChQ8Pm327yC9NLTubum4WsdyOd-YUUfMUBNny238QmSFvA-j0CwxjKT6J8m_Kj8ZzhKUUnRBqI-YW7mh0K9OIGlVUsgavsFzYoALWGZOjuYSjCxGZCJ7pKUhuQT-2A9jPpsUUrD16a38X1AX2aY18RoHtDOmeJHIrkFfKv9S38-AR5cx2K0aojD7YoAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97097" target="_blank">📅 12:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7oAY_UTi1gKqvJQMTUWhWjM7n2lqA1zbD94OFagh8Lim9WgjMG3rNbutvBv6NNQdyBhtyZFjDGHsdV3qo-Bdht9oz6sZZzpGRgfgfXO_KO4iTQNsmeFUPc_Mbj2mAr0bxsY0SzfMo9czdeNp9r5b2Pdh9eyR0F7FeAzgUxU3GXBUISxFgCLPAdLOmHchoQ5keeqCR4DNqRZVy5X7Oj734qa2gA1ZGCEKaNi0mYf2tQ4ewOmuom6LZzI65iDYjJ8c_zP1V7A1PwY4NPQZFOWBSGsJmBUAV3g6dHtlN3vanSaU_9g4Ql1kb-j73NcBJF34SH9eb0J4EeJGf1_BQfxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇱
رونالد کومان سرمربی هلند درباره ضربات پنالتی دیدار با مراکش
:
"
من سعی می‌کردم تیم را بر اساس تفکر درباره اینکه چه کسی می‌تواند پنالتی بزند تغییر دهم. دی یونگ را از دست دادم، خاکپو را از دست دادم و سپس سعی کردم بازیکنان واجد شرایط را قرار دهم. موفق نشدند، به من چه ربطی دارد و چه کار میتوانم انجام دهم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97096" target="_blank">📅 12:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97093">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPcmjg-22mXdFTYh7XhvnQJ8-Yvrk5_GkP4x8WJTOfwRHGB6Pmryvh6TM5Qf_IfWo-BGKrOmk1PfjYjjGWzmZtpoYczOqKqptVR14jOOc5p6b-pZs--IbsMNUerrIoZWpop7B4NQ58abM4BtOpSDg43nCOB802uuWS59aAfxwMMIdvA0ClTVSoxtokKVNkauzGFTNwSk0mtZfoc8iDzMvXxKYtTJ2u0bRggJHRyvEnY-9b2uupohJxA-jm3A5gLuv3jmyl1OOzTkwyFm3aIaZoFmYfNuIar-kkxfCZuVAEilIVN7QYnGVObscDJK9kDb6ygSDoq2tTfkrLPqFk7Rog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8xg-sDNwu0pa-9LRMTRFpMOfWAro6ddsOxtAKlm-fL714rwWshL9T8UMbNEznBgnxubBmx_3ZCvJHcH_SKnbZlqGO0dERgYb0q0KALGRaljLR1Il5VikuEMXMC0_2YhIqKD4dAtfLkeMd9MMzQz1abxMCbgVqj7GR2qfMqrDUvC9HdRApuebgjIVSMHYy896i8FcAJEzYCWVNDfb6hpnbg7ko6hASUX8xKRTICINaQIzpQ6NRNo5PPi1a3fPddn9RT7I3rDO4nQgAKrOGMPtGel2D3j9EhrtGC7ILnWRLbJzIPFDVIcc4jgu0JxMHUO-kiJQ93xYf8FQMpaVKQ5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9-PY6zRpKkl7_qpi-JBgemsl3Oy9jItJ8leTW7UtexWDq5_PstifEzm4IYjFeG5Gry49YYIdZkfhlOVBB8XqUqCz4B_aVgWPjTZwONv5OnqvSXwZtgO5EfXFrGAFw3FfzzW2ubG_4eZgic1XDc6izYsCNCI3K5iqMtwED02nVeDpSE21fV4sd6_N9KRKImHybgW_igmMyjfpwV-JBa2RUvIEg3GIew9n-HVcs48orEgNws60pCbZG7KCxejVrtmPSE7tTFyIEUDuT1WSyWKJKhB2ZCNDIUhESyhFdZuBRtXQ4yKoq4r23yetlVIsxp-ZLNO8tc2n1Ud-hsKXI9eVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇷
همسر اندریک در بازی دیشب با ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97093" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97092">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">▶️
🤩
حس‌‌وحال دیدنی رختکن تیم‌فوتبال چادرملو اردکان بعد از صعود به آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97092" target="_blank">📅 11:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97091">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SARzMqpLPcNNkocfzPSCGe6Fx2Szm4rBXxyvmYVyFBRSGcYRbd8Fs0lprbm0sUUtKD_d-8ferQWvZ6KIed45KmJdO61huqFA9E87-ADJ3M16DW5ifux6iJenJxbl2ZJ0RE-rrPi_owNexfT4aqa-UDmwS6aGBCCoAxLbTQYc1afnK4cIYOhC_FfCXwFtusetVqgjne_h_CBaGetclJt5ly_Ruzy85qBPoTxsR_JTuXgFVi9mw2M7M01y-w05M96OoEuxsv92P1Bnih-JF9_L6dYuFSjHOTIa8Z5yC_kWvAWc0onnLpgvCQlC1_V8B7S_7iUta2kizIj3qMbmdZA3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97091" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBUxJ9IHOk0JUqWtg_FjS2QExKmndlEFMUzqair9V-Mctt8G4-2fpZGS9mFdHnEuftsNdpC30frAF808HETcTRd8Vm5cknHaRWerywlNdIT_C-4FDTucMW97OWVLANZ6_erBn8YG33vWcjLG5XdtAuQDiUMgJgHLZ-x_QOWx2AS7tStxB4j-TIbNVVBd8d2POfPbJKWlJfANReV91Uuz4xASg3HgTI3ZENOLpUWHtBZkxxFHtiWs73FxSrK4jpWY8mDLHApejPd7uDx6nL86CQPevooeNMo2g_c2Hd7xecTs_aQRFw9mkMzb3wl0ZQkcnJHCu8oTW0YEXVhAT6HMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPdOMMRfu54AC7hqa78K0hRSnTLZh08YXMsWh4PcOnwK9DaGC3H7O2xdNkPP9kyG13g1fcrNqFH8_iO6tKerkzfvDEUUmoKGZlfYyhV6_z8o-38Y4Fe1eU3fZ7JFI8_8KK0JtlYc6CviVEbgeM5MYSMyPORR8NCofo8Aq4JBxhyfeuE4YKnYvw9Kuyv9M-SLIZwM5jZnqzs8wbQ5QrG3DbqeVeAr9MbkybNeMT4drwR50x-ZtdK2TlDY4uSCA-7m90ZMk1T7_O-ri2WnLNrJZVCHIUXrGyRmH_9Yprwhz_oViPvpwb0iVVtzV4rN47xfUWOv-RkGalwCM73SyCitgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwI9kxkPrxWNpYctuHVfe_Bw-j3N9JTq-2E3ugyHy4oRmVGyKd6YXgudaaQ2FAowOFupfTtstSTlk0rgOWSreaGTE101GGnt9MPdoGdyC1CIq7xKlVt3eQZDWbBIJxw4ZSYZ_6H30YqPsQI49ru6AKLBGuYL6d0knPmVXMbN_AAHflbjjpAMF4hZmvJBNP8QjokmFxaPdxmYQB-C24MA-yG90DJLmE2pYcKgulxUkSbgPCDG-MvV4aB0vpCtApzMj3i8sPCBEaliw7nJJhFNroHxVz06V1PLI5VdQbj8HUMIrHDeqgTx412m7Y700LF1JR__Huyiwea5qsOSobt-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5jjXBwjkw8zoILhPiFUL8p1g5hMGURU_5TzdrLPVHwTj1W8M25vaLIaIual2beTow39ilNbj31wt7K0CneJ3axYwq4ZWEzdqgAIuoDK5rCpxOeT5k2VIF129hlKSoRsMTp4tnz6MOmuNIn5JSjZxP4U1oRgQfwWcqvH3HGzfac_xRi97lfXG8wi9roMW_FbE25pF5On0aG9k5R-HOcq-xZRq0oP0hPQjNdT2IZPdk3nUq3G-9mKuHaRijW-WmDvgtBZoNS2EyTI3n1eYWU2JFx4nbzx_-h3gDVmLCKgbRQZtP-G7rYWUPQZ854GylOslVop4ayX7kQ-p9vW0-5SSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOHACD0EEIGTYmO1x2rauZbnnYn8MQQEqJUAYbr4EA9FAhMs9UPwIgO-zYjbOKiCkz00XUSVO0SdklOxCKsfeVmxTHzWSJF4wCZOvOTjpRqaXfG4Zgk88Mi3vK7TNHa7KNhNSE02wshdt1Vwi4m5KeZh5xdFOMixyzuvA3Sy3qa0AjvgC9qHprIQ2I5tYuqhbbfLFgzWmJoGG2Fvdo2iitNowiUwFGjKTil2BFuBPmbiB150qsQHBFnsHmsaioYKOP1mZdXoXQ0YpRFQHq6nI2wfg5aCxvVCVsC1Y9qqYWhb8rtoyhXH1IROzaFRRpqp5VB7z_Zp7X2ocYEv8mgcKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر رونالدو نازاریو در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97086" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=HR35oEKWYfh8JYx3RBExotvyA9xPzFDJv22Xg8U-0l8vdCV8HClhau91zsWeha3p2TKWHz-C_FhDGgwTbMV-z6PPZLV2AmqK4pSV-R1G_WtpRtfU857mqUVG7km-pNlObqvvJL-Qo4f9CEy0KKKD5vFKpXThgAZfT4FUQQNsuyNEaI2ugg8coYm5BuuzHHKRrllz4QW7mLtLrxhXbysnsfQJjdIlYd_wFxphfhaUrYPfsadaISlXM24v3J9zWZ55-NT1FYs8DD8BK5qwE6Z6kg7WalYqjseV29V8JEWJYkZPLCoabES4fQpxWDziOCKbrJcdK2osv6cWMLEY08mR6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=HR35oEKWYfh8JYx3RBExotvyA9xPzFDJv22Xg8U-0l8vdCV8HClhau91zsWeha3p2TKWHz-C_FhDGgwTbMV-z6PPZLV2AmqK4pSV-R1G_WtpRtfU857mqUVG7km-pNlObqvvJL-Qo4f9CEy0KKKD5vFKpXThgAZfT4FUQQNsuyNEaI2ugg8coYm5BuuzHHKRrllz4QW7mLtLrxhXbysnsfQJjdIlYd_wFxphfhaUrYPfsadaISlXM24v3J9zWZ55-NT1FYs8DD8BK5qwE6Z6kg7WalYqjseV29V8JEWJYkZPLCoabES4fQpxWDziOCKbrJcdK2osv6cWMLEY08mR6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند تو اردوی نروژ داشت غذا می‌خورد یهو‌ تو آینه خودشو دید رید به خودش
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/97085" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=RyFBdLdYPXHZmI7-B3sCTIxx0jx3wGG_z2mg5_5Qo1QRKn_wU6JlV-3AckE0wCNDB-dm_0bmFF6ItZLFojiHVvqsxGGpvK2N5WxmR5wJx_OSaIqBCJQyS7JQKYUBtUOf7BJAqQZ-AT9sHj3Q-mEszSfoEIbKN626Y9FNDlDFVkGHi74oBTfqGmpOhAAFzOLSic5jIj2vRHeD4S_71VAWqmQCLENDqf3g9n9uoweWkcb-MmPXvEPwQZm18JqV_wvC45IbpHA3Vt3pdzqxhnF_o0SwXLYHfiQlmwZ-XOoqlWanSBxZAetW-KoQI-L94AbpbyAiAyrEWAATK_4bM9olnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=RyFBdLdYPXHZmI7-B3sCTIxx0jx3wGG_z2mg5_5Qo1QRKn_wU6JlV-3AckE0wCNDB-dm_0bmFF6ItZLFojiHVvqsxGGpvK2N5WxmR5wJx_OSaIqBCJQyS7JQKYUBtUOf7BJAqQZ-AT9sHj3Q-mEszSfoEIbKN626Y9FNDlDFVkGHi74oBTfqGmpOhAAFzOLSic5jIj2vRHeD4S_71VAWqmQCLENDqf3g9n9uoweWkcb-MmPXvEPwQZm18JqV_wvC45IbpHA3Vt3pdzqxhnF_o0SwXLYHfiQlmwZ-XOoqlWanSBxZAetW-KoQI-L94AbpbyAiAyrEWAATK_4bM9olnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
🇲🇦
خوشحالی سرمربی مراکش و خانواده‌ش بعد بازی و شکست دادن هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97084" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=XUNwdLApZwAOqiOEAT6CEi9Tv62Mo8eO2n1T7AI5nI_zeL4J7xydP5h6zJHf9HWKCoKvngYMN43JgvKYqWMfPZZYf8YjHdgzeAMCAwvaBBpo72KI_NRpirPyhP5dL_yyzjGZpwFbufP2z6CCPPBmdNpkMxaQSCRra3dDAmmzwa2uKVj7VpqF5DeO62NtJXrhfNsZc31oFyJ4TC9iL1wgel_bphALXcgEUui_U1bvLAtTEq-o_odwkDKII1WX5qj8mKPBwRGJCqQ7VZ-SbzadCg4fq_MBbL6th-XvlBaa4_IeNmZKNIFOD4S1B-EPxaC6ElhtfeK2fhiUUez5bVd4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=XUNwdLApZwAOqiOEAT6CEi9Tv62Mo8eO2n1T7AI5nI_zeL4J7xydP5h6zJHf9HWKCoKvngYMN43JgvKYqWMfPZZYf8YjHdgzeAMCAwvaBBpo72KI_NRpirPyhP5dL_yyzjGZpwFbufP2z6CCPPBmdNpkMxaQSCRra3dDAmmzwa2uKVj7VpqF5DeO62NtJXrhfNsZc31oFyJ4TC9iL1wgel_bphALXcgEUui_U1bvLAtTEq-o_odwkDKII1WX5qj8mKPBwRGJCqQ7VZ-SbzadCg4fq_MBbL6th-XvlBaa4_IeNmZKNIFOD4S1B-EPxaC6ElhtfeK2fhiUUez5bVd4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇪
🇵🇾
خلاصه‌بازی دیشب پاراگوئه و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97083" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
