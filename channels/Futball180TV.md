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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 509K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 14:51:53</div>
<hr>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywlk-lHzeNCeoeNN_Jiqx2xrNkirD6Vu503ukSJHy5a53Fqd6feQcP956JIBaM8h-1nm5YfqPTwkrWE5iNbrywnhDt5WdB0TygfginqH89hg8RWGb2zGKrxYSdEFOP0pQE4QCnGnTn5LSzFliJQX4A1egRiJbQzX5D85R9R3Aivzo_Yg3xKElYIysI9HX9nDyfGeY8IcDO0SW4XfftbzaIEykBFOhCAClljRSOpKBXvYzshWo8npqy00R0jkrW07_c9WQ19OSBXTcTDGHPabEyn2R3xYr4wl5w2WOE8gcGRiLnoWn5dKLZ89VEsYtu2jUROeeH2DE4vI5E9wPkjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteR7XqaN5FUFgLlu8vFNX0_Ki3NNllHo04vCpjlVF_9v8CtrAun7pD-xHWe7QOkgiMnBaseSRrWEvLWswUyIJeCwsYQ8_5n6UaVNNas8JXlnUL8PV_46GNPwTJnLvj_82i5Su6Ql-IxdRrRe995HYPnL_Qq9h2Adpr4aI2TQ-o166-uNthzenKVnND1yNxxV4PzHwDhB-tZbzxJKRQdULi0KupU8mPMtqm_JE0yLd4FfDZ2hCSAo2nzrQN3ltkg9cgMi2JAspz6nMR_z6QcwsDVNt-r9aRlbI1E8dUOQPN6s8LNjl99oqOXxwqs0RBT3_o_FuOcb2SaIHxH77NqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFsubHB4HPc3NDVspKB5sf82GciA4_ImB1xkQ7AJ4WJJSbJ07irfQbVBXuWkj0tHYLbJreKFgHcl_hdB9qEezM1b115qxmCYoDzFm4NIZ6S3KpSmlWACwg8V8UGv9lJ1BiWDgUv1wxZAm0cze_9OGayhuHSNri5SM6mLSOqqYaUayALeQKrKb42utQe1ly27Ddlebd6edBZeBT_y0Gf6BQMPp7L72UauCYwXwruToBs-iiMePAPsbwjSYkLSm5aY-fW7IHxEq3zPMragAJPF1MBHwcpATyBgJrSlwP5iJ205qeVsLC4ysmpxFMz2XO1L7UbPyfmFtVe7NpThfDXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=rzj-GnaW7Lkc8Tg1sJ3IYsxpEkmiXuSvkwUrlCjZmxUOncah77CKcs20mCENV4AjjXXZQRv5bqWQZbE2jILCz4R55VlaoyZ-GfUUvF2Z3EWgP947zZiI9wJYHQPwOI0FKF-KnaC9A_74JICXbRd0ityaxglmyJuX1ztyeOB-0Fv6Cn10nlymt_YdWa-MlUy5B5OFgROiErs9SdsbWMfb7AaGN9ixA1wap7LFpHBqmCWrnDUC9QyOU9D-zlwEszthd2gmRpC1lka2LCAhzfg9aTeJYXTgK0vJsV4QdXiMc0TRD6vlQI4RImfBAIK1PEQmUF_jao2kjek6no_PW2h10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=rzj-GnaW7Lkc8Tg1sJ3IYsxpEkmiXuSvkwUrlCjZmxUOncah77CKcs20mCENV4AjjXXZQRv5bqWQZbE2jILCz4R55VlaoyZ-GfUUvF2Z3EWgP947zZiI9wJYHQPwOI0FKF-KnaC9A_74JICXbRd0ityaxglmyJuX1ztyeOB-0Fv6Cn10nlymt_YdWa-MlUy5B5OFgROiErs9SdsbWMfb7AaGN9ixA1wap7LFpHBqmCWrnDUC9QyOU9D-zlwEszthd2gmRpC1lka2LCAhzfg9aTeJYXTgK0vJsV4QdXiMc0TRD6vlQI4RImfBAIK1PEQmUF_jao2kjek6no_PW2h10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=JE3oXaQIcJl5VMC6RWko3urdr4xDXT02GQ5hx7muWpmzih-MkrOCrOPtx9wa7jNh_swhSG1kSI1eNrzG2RELxmTMs1vO0iooQ0dbQmtv8VzwUwkonG67Jd6E9T2z23-_a0MdhbwN_1F_o9pIbfJdZXH5DMfQYO5VR0fonlnXwXRpk-aY9RFPxMT6V22OjzLm3ABYGW8KNkS3gETDwDQfoN5NuvI421cRUqz3r2eJlsyjfg3FHZNv6La6O3IJNwCYFUhnhi-IgNPJ4If2YCjt6OWt-PJT8QfuF61Puu12mpB4nzV1LCbNiXFrKc1LLBPa25IcS31kVXAM5tuaOC2r_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=JE3oXaQIcJl5VMC6RWko3urdr4xDXT02GQ5hx7muWpmzih-MkrOCrOPtx9wa7jNh_swhSG1kSI1eNrzG2RELxmTMs1vO0iooQ0dbQmtv8VzwUwkonG67Jd6E9T2z23-_a0MdhbwN_1F_o9pIbfJdZXH5DMfQYO5VR0fonlnXwXRpk-aY9RFPxMT6V22OjzLm3ABYGW8KNkS3gETDwDQfoN5NuvI421cRUqz3r2eJlsyjfg3FHZNv6La6O3IJNwCYFUhnhi-IgNPJ4If2YCjt6OWt-PJT8QfuF61Puu12mpB4nzV1LCbNiXFrKc1LLBPa25IcS31kVXAM5tuaOC2r_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=iwHU_DiJ3CDNCdfOPVnUpMUhOCJYio-kL1skJZaGTIivjI59KuLhroDF62FO2w9proYLQjBFHvCHsl6kSj_TdqRjr8Q1jBEE41klFL32jUd_yirKV7VwZRXb8CXI9UHjNzQdZ3dAR_-HRyYfdR1Lm7hf2GsLSWmZaYaVQhar8H2Gq-a8A1ZHsOLbDBW6KioQpB-68_87QckKOoxt2vfXfuMbrJOHoKThFvqgPeNV73Znx5qUS5111p_2gNDl5DgJ-_IPvJFEpQ1Bsnabma0gPpTk7E9OJJnUglx-hDD-_e2B1fWMItoe8l4am5r_3UajgomEWLXDUsyOnLRLbnyeCw8umgJAco50OwEs_PolyUjBgX7jOQfLAMEmVvMqkflin5GpKq44GNqL38g9MDabQKLsdZzjVqaNnQkcL1RREUOlBgM9m0_R3_3fB8gCBq78k0cKiJDfSxUjQe5SO96Ur9BzNoLCMqCaHYvFiOfq0XaZevLaq6Bd-TuDQekJNSNiy4Bxqu0WUi9dfcymRNKjcaVe_oFsBGrs1LXXQsz0e6nbtI6yrExP1U3IKObZldREfhxzNy9YJUsyEd8PIJ8L2cf70pypupYjvK23G6SpYMbHFAa1zDqfhY6yqxiuiL7QW5tLyjBfTmx-HJSI1v6-dG5HZjkEeIf71Tl1Lc1Rgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=iwHU_DiJ3CDNCdfOPVnUpMUhOCJYio-kL1skJZaGTIivjI59KuLhroDF62FO2w9proYLQjBFHvCHsl6kSj_TdqRjr8Q1jBEE41klFL32jUd_yirKV7VwZRXb8CXI9UHjNzQdZ3dAR_-HRyYfdR1Lm7hf2GsLSWmZaYaVQhar8H2Gq-a8A1ZHsOLbDBW6KioQpB-68_87QckKOoxt2vfXfuMbrJOHoKThFvqgPeNV73Znx5qUS5111p_2gNDl5DgJ-_IPvJFEpQ1Bsnabma0gPpTk7E9OJJnUglx-hDD-_e2B1fWMItoe8l4am5r_3UajgomEWLXDUsyOnLRLbnyeCw8umgJAco50OwEs_PolyUjBgX7jOQfLAMEmVvMqkflin5GpKq44GNqL38g9MDabQKLsdZzjVqaNnQkcL1RREUOlBgM9m0_R3_3fB8gCBq78k0cKiJDfSxUjQe5SO96Ur9BzNoLCMqCaHYvFiOfq0XaZevLaq6Bd-TuDQekJNSNiy4Bxqu0WUi9dfcymRNKjcaVe_oFsBGrs1LXXQsz0e6nbtI6yrExP1U3IKObZldREfhxzNy9YJUsyEd8PIJ8L2cf70pypupYjvK23G6SpYMbHFAa1zDqfhY6yqxiuiL7QW5tLyjBfTmx-HJSI1v6-dG5HZjkEeIf71Tl1Lc1Rgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=rxolQvcPvP-QkV43_bZ3QM4-_ncyZv98JPFsBnLP5lii8iXyADuctzoKfA-Qq-Q72ySpDmZxZaUMNGFO5TSAeOQcpkgnOFJYO-J7StB91XZwKB3OGqMaeILtv6_S5jHIG8l-bgzn724szV9diJpfXYhfC7hLjAFhb8Fg5m0iS1R7Yg-2pb0XPCr_HwBYm3b4oSYEsbj5-KJQQ8rrmn8AxoVYw5ltI3a4LM2OY6kRtdq0ltrSgvUmXNRdssnRGKE_Yz37mc8E-k9-mNkw7SLVivTbmm4ecxn1bHGhFEXJHpHQ5PNkRjCI-b9ztrwXee2gm3BKgD7IHo_NafEdhcYVDGh0GR06OZpNKnKdyYllSyLIuKeMvKQfpioL1SLgAvIlwlqpWbbAEpwZYzDLo-zPptib6fODaOwns7M7CwEt4acqC_6tCYdH9jrQgAf1JfbqlxFPVffXx4RBg85C9yokjGL4iD1iXI1FdE5fv393JYXH-gEH5j3RXAxs4rVzOqSVPt7GV2aEQ7C18AKR-KDJiwDCTq1JX-NbUHz3xyBgLNgc_Q-FMHPsye20WdXhtxIX9Xa2XQRyhMxetXQe7WvjKxgvzK-ZBO2_VlkHYqnl4pfpIytZHrsb54u0-iKVqRC6AwG55w4HCaUJ1cfL2Q-eik-Ye8-QWiD6LAt9bWuyc2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=rxolQvcPvP-QkV43_bZ3QM4-_ncyZv98JPFsBnLP5lii8iXyADuctzoKfA-Qq-Q72ySpDmZxZaUMNGFO5TSAeOQcpkgnOFJYO-J7StB91XZwKB3OGqMaeILtv6_S5jHIG8l-bgzn724szV9diJpfXYhfC7hLjAFhb8Fg5m0iS1R7Yg-2pb0XPCr_HwBYm3b4oSYEsbj5-KJQQ8rrmn8AxoVYw5ltI3a4LM2OY6kRtdq0ltrSgvUmXNRdssnRGKE_Yz37mc8E-k9-mNkw7SLVivTbmm4ecxn1bHGhFEXJHpHQ5PNkRjCI-b9ztrwXee2gm3BKgD7IHo_NafEdhcYVDGh0GR06OZpNKnKdyYllSyLIuKeMvKQfpioL1SLgAvIlwlqpWbbAEpwZYzDLo-zPptib6fODaOwns7M7CwEt4acqC_6tCYdH9jrQgAf1JfbqlxFPVffXx4RBg85C9yokjGL4iD1iXI1FdE5fv393JYXH-gEH5j3RXAxs4rVzOqSVPt7GV2aEQ7C18AKR-KDJiwDCTq1JX-NbUHz3xyBgLNgc_Q-FMHPsye20WdXhtxIX9Xa2XQRyhMxetXQe7WvjKxgvzK-ZBO2_VlkHYqnl4pfpIytZHrsb54u0-iKVqRC6AwG55w4HCaUJ1cfL2Q-eik-Ye8-QWiD6LAt9bWuyc2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYWN8khDNA171IifoPf_jF8RVsQcrSllvExIaO7i2BWv3vBwkK5xwFukTwhs44BHFf4qCOUEd3AZp8NvFmN0SMS4-Gfu9cAyjWWs47uOi33jSpESNi3kNaPdNYYS5X9mGk6AWZ6hDWyuojZU2Nr8rIleEA2xaLdS06DEaKOOkhkE5iiEjjMW63jJo6s8Rj_ZsJaaT3yCzg-r8lzM13QmK1CK_gXQPvjZuFlpNJmORSV82hkrfgFiXPPc5W_p_JuGsahuw4Z7h49QQQTfbk6meSETHnSZUUQYRfVghGALuG5YYkCsMdP0XHtDU0yy1FjWHQ4fRHc2nlYq8rLihDSG1CXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYWN8khDNA171IifoPf_jF8RVsQcrSllvExIaO7i2BWv3vBwkK5xwFukTwhs44BHFf4qCOUEd3AZp8NvFmN0SMS4-Gfu9cAyjWWs47uOi33jSpESNi3kNaPdNYYS5X9mGk6AWZ6hDWyuojZU2Nr8rIleEA2xaLdS06DEaKOOkhkE5iiEjjMW63jJo6s8Rj_ZsJaaT3yCzg-r8lzM13QmK1CK_gXQPvjZuFlpNJmORSV82hkrfgFiXPPc5W_p_JuGsahuw4Z7h49QQQTfbk6meSETHnSZUUQYRfVghGALuG5YYkCsMdP0XHtDU0yy1FjWHQ4fRHc2nlYq8rLihDSG1CXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF1-yhk5ZPwncMpxE04gU0qNSxjDG9sTLNYsr8WxQ4IUNzL4QudpdxwwjMy0yd1ykz8lwv6B3XDLMzKwM084nKxxr4w2ShjdBp6_5HtWTn-LkiH6FGV05EL51b490xEg7Ai-ptp6UhKvAXYynnRcQZ5XoC-GwLCTC9TG70_WSokqkfONd_LvgC3VRIe0qOtMtJd5XiTMKZcyuppel_s6jUKx-Qye9olhm-nnDa5C3kUI1WXgNbVNYl0hjc3xHV2cUkPdGqylVkfAbYBMPuqNJWzHUKvmNqqA98k8O4B0nrcGxzNh7sktKE-LcYiXMvuRnhd_V8V8tiFaVSaw6Hb1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=KBghbBdkTbEnqPsWphy71_vTIdjJ8EJR_VeXPmQlr83Tctralg87rMC5YDDe9VBLgPYIivaWZ_9-UwI_MfKo9gPJ5_pNAnNwq1mlEi4C_OsanVFlVtByu12WnlU6gzrhVj6u5CaETGKdY8lHsEbFoG_XXvz--n29ZKDRyPGe7oN5yUDfpe1CtET_4NJnuVDOTjqAqwTCb3ZVoMLAZ2oFRSXqGwy7zbftsayst5tNkPXimwT3r1exPqu_sRcEsEmFMF0LEVESpG9Karkcf1XxBE7aKdqmZqY4Ok-DInUILB7fAzg2Wbm5XMeRTJ6NWCUmec1tmm1lkD1yvW8wHH3b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=KBghbBdkTbEnqPsWphy71_vTIdjJ8EJR_VeXPmQlr83Tctralg87rMC5YDDe9VBLgPYIivaWZ_9-UwI_MfKo9gPJ5_pNAnNwq1mlEi4C_OsanVFlVtByu12WnlU6gzrhVj6u5CaETGKdY8lHsEbFoG_XXvz--n29ZKDRyPGe7oN5yUDfpe1CtET_4NJnuVDOTjqAqwTCb3ZVoMLAZ2oFRSXqGwy7zbftsayst5tNkPXimwT3r1exPqu_sRcEsEmFMF0LEVESpG9Karkcf1XxBE7aKdqmZqY4Ok-DInUILB7fAzg2Wbm5XMeRTJ6NWCUmec1tmm1lkD1yvW8wHH3b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=gfGuOc2NowV-pHHaSYDbTJvD2oOeLezU77YcIGE57HMlBiRiLMZ8jbuknAxcAIBMB3xVJ7RiudH-qEDDXSFD8evvzVSU7bhKFKWJz8l8qHoJrY1JU7U3ErNVIpDW-G81Z79-LnpyyYybKtY4IbUQRaD5nFs_XgpdnF-6J9vxiZO0RgFZjtFI-o8IVQ3jsjslhZ5nhxi0Rj-gE15MnrSXWSHk17NvUE27wxq9mXF3MbEB6Ik6fUjd5MV6v2nifDUgYYjV-V0YEgDKvIrGLk8EQr0OSwzaPjR8kuiL5ZHTpnKJSWb6gbvX_3omqWqyuh-WReB-Oprzz64n9lbRvN_GSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=gfGuOc2NowV-pHHaSYDbTJvD2oOeLezU77YcIGE57HMlBiRiLMZ8jbuknAxcAIBMB3xVJ7RiudH-qEDDXSFD8evvzVSU7bhKFKWJz8l8qHoJrY1JU7U3ErNVIpDW-G81Z79-LnpyyYybKtY4IbUQRaD5nFs_XgpdnF-6J9vxiZO0RgFZjtFI-o8IVQ3jsjslhZ5nhxi0Rj-gE15MnrSXWSHk17NvUE27wxq9mXF3MbEB6Ik6fUjd5MV6v2nifDUgYYjV-V0YEgDKvIrGLk8EQr0OSwzaPjR8kuiL5ZHTpnKJSWb6gbvX_3omqWqyuh-WReB-Oprzz64n9lbRvN_GSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6u-DIIpODXzM2PIULJFifFpAyMcfodoiieKgM1OGuCzSipPzWBIb7_Dw9utAtrq0ZtWSOSthOSJSIoNj4nn6Xwx8baJwWnfwyrVRlWMJxK9_p1RnX3no3Wu-jeuLCv5Oh7wm0vNLap6m4jZ0TtHUMK71AAeM2GEiibVNtBavbJyUmq07EeQSoh8NV_I_VDgEDtP3PK06giZ3wxDlAcSXffWssNGmMVzvFDvDWJrOkmYx9_1l6jZU8J6asUzfN5iyLaaDKUsqNlMb5pXusH21mGpWC5bWKZb6BelmQVjmPQvUcYKKsNe_mmTI1Y-Rq4Ney7B2E5wGh-tPiqqHQVt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfVj1U7IiPlU25S1ytVEL69YgSdgPQqZY_0ZzcluOBiAscTTLP-RCJ_Xg2Tr5mAabH9U1knGLeOu9pnoqIb_KCHtjHb9pYaFWEg2L4rniK0aPg7Zm1lfCqqaQ4CcUB4DJdiQ3I-SozhL6kcB3-Eb8xGo03PTxTiEC_Sv4yidB64W4AdhHEb-s8rJN7DRa-h4_SyVjCvuAX2JSSS9H5WfvnsF70MhlaxmvGHwKzM3rggr1E5GkUwE5-z-8P7yWxYaRS5pFM18GVCJhRN2-bCUmwrvak_8TGvS8Yel4PoTktwJi3YIUrpkgjzPalD8qtBAhM2IpPRzFT5PdLcIRbG21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmCSEQLeRfu0FgFvxGyGXzhuS0GUuNrAPXwk1TTjloW302wnH1WZ2C8mN6hAm78L5frqQfDj81ZX5FGLSMeTl7mQT8YlsW3_Cag7gdKuz6SotkrlrmEgnkdcUSM5ardpsVQs6yeY2RZMgneGz9F-zB95c79WsawyMG63hFmVn9gZHfETqsUQuJcvuA2aSwDRWHk3kqEm-jenzjayqKHm5431NTdt1tA9SR0iMJHyYpqNcHOc15J2KxNVkACn5EJFXx6RoyKjDmNEhNCs6bCI5LdVaGL3v0od2qB6igr24P_2W53Jt3iD-qiUH4xRSGj3QJ4s6jllaPSz9TwMxm9vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vrk6kDWvQOyCb2LYAmoL4JqpfkDBsyMKfhsZEouFH2zqCxaI_3WON4myvKhyhPM5TS5SjIR7_wQlv5GrWff6Ypjl4NFb_l_8q31kvj6XbiD58Mjt6t-Ktxmf8ZsjGP5UV2r8-0AxFymJC9imTwOwWKBAQqRBMc1-TiNa0I7L_C9HiLUMqy6PmA_gZCgf7jDvlEMMoYI89u7ZeQjZ12OOA2IKrm6Fgy5B-ZvHVIyxMJCo2CeuZPWooeUSHooIA5W2sdVV3QoSV1Q6czDSoH0l12MaFjNjEOychfKHVlKF1-kiwztlc8D7K6eJ3lEGB01kYrnZFrZNA7-jcydOG4Lhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz7Aqp19dumCuBJt9BhiTlKBQmwjMCHeZJ8kqtMEjzwDVPCOy6KhvNyZvZPLFZdtQvJZN33lmqxC3Ont2w2FhDfSbdEDbNTQ1fLXDv3hjvW5PWlUR-VkzRJaI5myswMtn-U046yskNjIPxKiCDuMfFAHRdVzy0cUjCLoT2RwaiLbs-38CO4luplGlSTT2ixc_kI12SzITOqBu8CwJxmRpxt6s-E2yHCPwQxGomnd93gh88ZvsvbKBbPhWzZ-rRhSuBKNYGUq5cm0UF9Zt3N0wAfswxTP1X7EjgW1DSWszDetKEMkQ-3PawO1VgD2pwjJfvefCghH2KdZ5Oc8NtlyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NghHiHD6utRz5aMlzmeUhDzU0GeN7be9BSUClcOxMjrGdjpUR5e35Ej2Hhg1wwF3OgcvKuByF_nUB3dZjymfRa6mgj5g2dKqhr99y0zW-kBrpfiJ8eClyCPTrIoV5WccK3Cu67HznBdpvPc6vulLCJbey2_K0zbCDLLtMmnAe32S_w4gvOM4yW4MAdWOS1D_qqe4uQY9R_hiy9GnTnKsgvdCxNTt_u5t0UJdmzNT_5AP-pQqA7uaoz6B20njEO8BVTfOXnaAEkaR1H3jO4rQyNZdQ4ZuF6kUbDriIVA2UhOURTL0bTFILeQvvogm6OuOQv-6VUOvwiMHKaD4YRX8Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUIZzvBSx22mef0TZCkWue5sCA_SFu4SP4iWYj6mdhEtZu_8mKVr1qpDsK-xzF9HLglmD6mG7W-BFp6TZa9Lu5eVtJkw-GK-CJwJhYchvHU2ZwXo7hy08QzdF6DP1YqbMuIc5AgRFuVUd6c5hgISy8xXwVLjcxsRu4g_axVAncEPa2PWwdKIQQhdIDiIIdBKg27sMPyEE2aAFvPLmvTgsok5FVSXVZBFbMbvceC4KcDRhicMUyZt2_7cqUwQSXPO0Z_B0LlPvjUXE4o-ADqM43pc76ZDFl6MFeZ6dlZcSmMoF_KUP6uhztrp-oeOTnxy6nM5zx_ejB_tpjIAaJ2ctSO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUIZzvBSx22mef0TZCkWue5sCA_SFu4SP4iWYj6mdhEtZu_8mKVr1qpDsK-xzF9HLglmD6mG7W-BFp6TZa9Lu5eVtJkw-GK-CJwJhYchvHU2ZwXo7hy08QzdF6DP1YqbMuIc5AgRFuVUd6c5hgISy8xXwVLjcxsRu4g_axVAncEPa2PWwdKIQQhdIDiIIdBKg27sMPyEE2aAFvPLmvTgsok5FVSXVZBFbMbvceC4KcDRhicMUyZt2_7cqUwQSXPO0Z_B0LlPvjUXE4o-ADqM43pc76ZDFl6MFeZ6dlZcSmMoF_KUP6uhztrp-oeOTnxy6nM5zx_ejB_tpjIAaJ2ctSO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlHZ1OzHkfq7VPCtZq2RmLVm7a60BAffpkdRQNYWuPZSvfRe_lzRnZbpbJMrItH1o8tmj3zCQtrAfeYQ1TCZDUJjN8TyovWTX_zCWD23M0VKDkSHZ-IlothpOKr16osaqx9-2_7mPVsWNC6Ap7WsOkyLdbKWtW6fCR6lytGXP1qYV-bsI82qvS6KC8LVt8Ni7DzLLg5Sa0NemsngFN4AuopxyMXtwf1gw2Ip9aD7Me5tms0wo-X8t6JjD4pjswQZsKGrzoYSAk2HifBaeTx6tcIwIiPdLsTytWg8xUz98hnO4oCcQzClMb8LIciEM3KatUORyI14mJwkidmjre6WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBSWY7uIqWKgOHOQ-SxjnqIlDObQpFB3boezBvLEsq1ntfRrtJZOn0py0imVSUQ-tRCp8Drv7xuLcpKLRgegej5hgvv4w6NdwoXvOIwDxWwtyRl1tUG-EXDuVEsfoy8jhN3NTBXmUwb8mJO1bwap2FTYhjFQUD6fIsBIvmJe55746piQA1BgDeDrij4HiHgBEnlqVT7-F-NEIB5nI5RLHAgWxIFUnNwYvWe_MXLiNSBBV8O0z8tDDvMIvfZxPxGwZbx6qx7MksRrGjpiY1PoDx1cDW9RXXA5JaltnxJOqgvghrLSiRoop6_kUZkm-al_FVebFoaEhdNyQPUDiZ3buA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=L9coTCBKLqnWofIFP8HDhD2MCjFa1mwTkPaRwZUbZjES-X0M1Oa7CJE_nGyYN-GcrUNhN4_NAA0SLGsshpJiOp-Q9q11rI_hK_WyyljIiFXtYUMqaiXLzBkFDBXZE0r4YvwgTjWAVURnXjMts7a6EoE1-Wu_buiLERg3j6fh-jP7I75BjBniOVCSDVy4EP0_HmlbOuwMhfHDIXl6X6WVRWXNHPysp0KoMKafgBlNEtq_cFWh_6gQDYvJBjGpkaj9w3sWHHjeqAZ1SNJiyQIzQu8SQMPRY_KSdxjeaPirWgWlAoy5Pj-GN7nCsLPubBzBypZtWoYkfLg65kvndjiJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=L9coTCBKLqnWofIFP8HDhD2MCjFa1mwTkPaRwZUbZjES-X0M1Oa7CJE_nGyYN-GcrUNhN4_NAA0SLGsshpJiOp-Q9q11rI_hK_WyyljIiFXtYUMqaiXLzBkFDBXZE0r4YvwgTjWAVURnXjMts7a6EoE1-Wu_buiLERg3j6fh-jP7I75BjBniOVCSDVy4EP0_HmlbOuwMhfHDIXl6X6WVRWXNHPysp0KoMKafgBlNEtq_cFWh_6gQDYvJBjGpkaj9w3sWHHjeqAZ1SNJiyQIzQu8SQMPRY_KSdxjeaPirWgWlAoy5Pj-GN7nCsLPubBzBypZtWoYkfLg65kvndjiJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvAX6t0C0AP-Noawa3OFS9ontZOCrW1tg9e-WGI88gwG6AQ3rCZzCKgwNoe4pmuqIXSACBOnV0pVNN_1M5WfxFz1MDWqvLtvXTm6uOGSNFynf7toZcz-bp4x6qMiZ0TuftDEh3E4pTlIvpdFxlBc__a_VtTR-AfSIlMX37wBjpQ9ewDIFj5DUMwrlsiALaDBrciFSnpGcRxpTHaAIW7xc7wIKdkcJbg1YQRVZMmuB8SVlfpkAIyHW9keXCYdJPj78dmQZx7dRzcGtj7XIC5L38BPyDr_9E7wXpdvFSO-14gDkorVXdB6dw3GalGgIznQYQC2BWjzrKd5YGtqD8V6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYlFjJbZxttLH3nKIF9rMW-1Eaaxz3-8JiZQcbbPxjjwAjTNSsy9Z_ok7ZfOROjVuW4GPKqm30h808ugOIHrV8H7p6KqqWjc2zCc0WcvoDGrYQm4vGSl9rL_fKFZz9aF06Pw45X3TY7af4DVLvF_r32UZFA8_PiNKOgY7ZTyHE6Kk6TEEjtxXd3X3gDnY3apnnKl-jiWiv6ZNsyZBYapUNRFO17dAXBJUOyaVDb6boNDq-e7eZ2hFX_ldqbEexqKjcUA53msNYxQZzgeRjB7IAThO5v9fE4SA0Fqsn7_U0ILpUU1MlRSOEEEC8QVxcBxGe6ceMzYFCeDtXETxloB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGfTVLdNnnKIiMqf7nFtG_3Yf_UbnfkOH4vEx96TCT9e7wtZq3EjdaBfB69mL-Ze4zeog5JxsrudhGlFEiC-YCakGa1bk4jJdFiuvuqfF-VL5gsDZLJRANnRfNipsJeLUL0M0_oXLneSmLPKmawZvFsgFSNX3RDBLAYpY5bcTU10YpsaPpADvY4c4m4MlONxEiRGivvAI_dK1bHrEoD0KNIl_r93Iom2yclN-D89M33AVqLgcUt5liWfHtsVbolY7litfX6K67bj9RjYLZlsAXigtqOjMcpOvY5q5Y5RphufyxwI_tIAZnrzTtyvqVNippDYO0zWwPro2TNLTXaNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZ0OCFb2p0xoEf3VRSDV4omsFvuYe-WIJXEc08uHmrpeTOUt-xWaoHmoW1QlIEPESD2DDTCdtQekAOA_DC8PsPIqt5HGwd7ZxvW5E-xdzLrfi6ONvvJCRQBG3VVF4UC6SdPccX_2sC1-bHV15J5uqiWFC55i95SWgFrNq1Daxvou-H2Hz686HQybARryeWbvlCJ27nO2hGyyUF2linOh0ey7xhYATlO8_81edrCYPm4McIzBAlacsDyfOSGSR7Xiz0WNjObrGh0a44LbDGDtC-YnJD1rBAoUuykNIdrebu8Sw5r9hO9miopoG7f75OfTeasz4Ti78V1eitY5RsqVHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epKUuna1OW5bNk7Ce4m0Jet_-up7kgJe3Zb1BQUup4on8imrQ3NBBgCIHGLw2vxlkluINnbnZMZKBQdqT-iXM_eINOw1XcdM62p0JQlIvbZAyCWUpReSqqD8zWJrkLpxPhfxTR1D9tFZQGROXE93qM4De5gOtixbPNRuenPUqz-I4nS_5AyfAlfS_NWpCxfqfQCE5WNVl55VF8_fWPIwHJT3bBR7hre8x__R7cR21sMdXxUKVCapmQzwzrcuvelazBfvzGEbq_o_zaN0dcZUbEgfDJJXkdZ8XQ471_sKrvIBvwsGL8tTuihzWZiYwYCa6jfT-5fGScveYK31AcUEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8eax0RGSHovMnqy516j7RogVNouQexNOqG43MsxXpVtydg__sG3Sd2Z0bOBrFNchchUWvDm18r3pqqwYK7r1HZhlPE-qzuLodCXOMaoEZqN2iDinISZiswmDYBtt2JIHNROj_8SkPdMiRMhh-EzyfVBWHalvfMhtsR2MSTzTi09iXRjd2q0uCcT8ML9Nx5-4VqUv1w54XhjaqCioeMr6k4Y9DoCAkY9g4x2AZg6Ohiw2nV13Ax091KTjwAVOYtUMpFd-N5TouDvyLzNtAxdxoIMXsvc8nkSB33_wO_uGLDnoosZeO7LJuJ7vGMjvf6_ZijCuoshje-kXE2Y4Pe7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkaQd_AOm7syMRypEcc-miOl_dIEdL293oHqEu71SUE8yzAE2qfxy0kxBzEA3erfVkSkWZiJQXQDrHbqZOncqBBjvBl8DVPTkNIZ5SsRp7DM4gUsHz6Ixe5xCiaD44n-YuZT93nvDXrW_mvY9J7UZkjaAw_DdDMuqLS27vUuehJqlS3QJeJluCocX3O686ef5n1s_kGt1yDDS0PvXdIUhtBkttq9IAsOyTvntjgYMyRThRKonno1DIdLlXCQ1fggjcQ8txTCp3TyhpXbq89HlJxr6f3SQr59QsudH3bhCvYLepQCo-_W9xCqYglxh_agfOkUUECt2GUWUVEimd2tKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MmRsl9_eVxkPaoUF9_H1qPmgI_BY8ZQoS2YcDp5tN6dW2HAS7AhUfi13VqHRAaIBG1VFxm-pfL8RP3AVd5MFX_z1a7sQZ3Njk-w4ki-wniqa4Nu-PZ3bYPN8joQ2i_m_BK7RXAibf1v4956cRUi4qiGQ2SGAcOUpFjcD37uZURU2N8FFpTXGatO25-V8fedtLdYhbjjvZVTw_nPNtkyrI9VvrLfMRMfnR5AZuKzP8d9Bj9AxtYrJSJVRlTiArBHeeW9vm0qZxFqR94mYzQ5SoQLuapTb1fRb_kZkc2iFdkIf_5c_UduegvBILHwnb6Sa3MEKmVXq37UTeVdo2n3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhE9JsW1G3TXEq8r9oj8qhZ1RZTY9TWze9NqExerkloiwRO-OWMTxLXyBO5YLoNSWPv4WtPtt8FzL5uQ1xZmUrg4rmD439tn8k__nBwjuoeV0HKcxTGdWBj1KOv4Ns5RUAxg_QozVJVbufOqKPjkquUb2h6sMHLafC_2bWjIdmDJlipzwNzekmEf4FVpDmhF7Xr93gObbock6iJ65OI_YK2VDWwR6ez3r7UFrewUaQa3urbtEj4gPzVFMxgMUjIsUT78J9milmpolgz-Qa0Ic9UrI3hdPH2ctp2FuFRrk5YwK7ZFaTUxYDableKj3JifSEtEQHo2ZPyh_6t3Wk0KsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXnW8Tn-XSGuaVCoqKx4hiNM5-Y0JuHIexnMgFch02f9MHiTJBtIFrmTOfsgf4yPwQ-1pOrjXQ0lt9qfAgCPBmoyA-Nb2T134LJofhLycwHWPoSNYRTqn4HLDsFOEwboVdWhnRCkzzLrwXgR_fU3MQKsjRJNWLfL-qIRMT2bczXPxbnOdTRp74K6e3zCIj4LF7Wnb70CQh7xcateE9ez2g9VlbjiB-ITwz1jdu6FgF2qTVVx5Z5Tl-2l5oUniDHgneOb8JwxXF9BEVRW38U8X-hfE9QzNxQgznw8XFeUf6Pj_nT0SgmPanv4XPcD3_hrVSCMy6CDTlHg9mR3er5poA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=Zf5AELZs-dSQKUjKO4tpCygrsMTqpK8SOmEaPs998Y2fmtb4Yu4b-62QFvkpU0M4Xrh1NodIbYJ0zjIQqP9hx7R-DGpouoLx96iOLQod8IP2rmGFxD-0OfkbQHxsQEOJzVV2FI_aP3VWH0Nn7lDWYUav1RZZqr57L2-MIgP6HVzIbzbFhsVLiUUggxMe6uBZ7yRLZuvl9zY6YD6XP8fKu7dBQDpZqrkbajODXL1OJVos9FCKIsYg0Ow1H-_-85Qpowkllk3NzIvVTgEJCjCFnPHA2fusnmqKmo3e_u7_7_1X91UzscLhRNYJf4i_Cg-MEjUyE9hse2eq0x5l4pA8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=Zf5AELZs-dSQKUjKO4tpCygrsMTqpK8SOmEaPs998Y2fmtb4Yu4b-62QFvkpU0M4Xrh1NodIbYJ0zjIQqP9hx7R-DGpouoLx96iOLQod8IP2rmGFxD-0OfkbQHxsQEOJzVV2FI_aP3VWH0Nn7lDWYUav1RZZqr57L2-MIgP6HVzIbzbFhsVLiUUggxMe6uBZ7yRLZuvl9zY6YD6XP8fKu7dBQDpZqrkbajODXL1OJVos9FCKIsYg0Ow1H-_-85Qpowkllk3NzIvVTgEJCjCFnPHA2fusnmqKmo3e_u7_7_1X91UzscLhRNYJf4i_Cg-MEjUyE9hse2eq0x5l4pA8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuPPDqbCvgFxQQUmDmzto0eaDERlLTc3FKLI5FpJm8ZLDhgiK25nrNfhQnfVfkJZA1mmVqiHRoXjy8bHSoIxLt0FPcQFaZ5PdpYHVhGlLV79siVkUmE0L7CsEynUgvOmqHY1FCaIFsHxWcfXnXbFXPNMjEz3SCaH5wi48I0fLNq8LrJZt-mX2svdJmH_Y9Wc0Ec09654B_Pnn8eK0Hw4yQAIF8yctE7GH4kXTC7RIzn0BERFaQTLX05uaLWV6CZGDXr-EizRkFQJyrWZDMBjZk-D3YPRFIFiFpLqDpKzdiO2apmrL-QUk2edHOR6WsVSKZwbl_lES5pDPjAUb57VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCS17qSYs_m1Q7ovlM1FaJJ_7l6iXbHfI6qx-xcDBQV9IkIl0x5MZEbm0N654o9jk3P2rSV4BYs07oFHfKOiXnke7-91MNnRNCbmdWUFUl5lIXb6tOZD8QP2DFqbv99e6bs6PO1AOuVOSF1BGMqxP8EPgl9IlD0CJldqI1LcwtytaGg5e8fcvZDtbSeP4Y5-fcTMtlcRTh6klwxNTuefn1MJMHbJPq27xUiryLPFbBuTuQeayA845hcWH934VKUVXXsJ8SOS87g1j1Cx6zkW5hqIJLhlUu0rYJRkKAtjKzK3GsgGtznlH3qCWaP_otXasgaVXuq99e2gwLeQeHrixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URLfdsaR5yoB8b7a7Y0Cll4MLqutzN7cSRP-KM1CACIKgnr5NSytFgQdAClkJtcq_yw7uhuorUu6EiXHHYGk50zsBXxCuznNRjNf1aPqMVNA69ht0qtNslAG0ko6ZWLWxpfVGackpcDoNaTQ48z7YeDEVnXDJSAESIXA5WsfLJh8qB6jG-mb_fbvEVrd17FqhWHrKNi50IwGlM_lEi_UmAL4--Unmwewvwlvx4vu9Ab2E-KGjGOdPQA-StqeRfJbLHo0ccEhUo0KBXJqgvCXKELELUBNLOiIwKZkOA7_viWMCwvdkssy17uioLzWslDVhLitjvNL5rQ8EeAeW7ojwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BADG2IkF2SvBKgGzmaWR3yikRaymIbSaJRKAwxYzSXA0fQStiV5uO3jlHN3ey5EcK6KU9wJHveBPqMOhBNh5q99koY_5oYj1bTabae2E0bH-_m2fVc0ogMeglgKwrxqvkrIsQIC0unmPEazJGuDpL44PCgALULq9SyVFiofs-ymKZ0jgXcHI_dqHGuAz9-xL2AykTesysn6j0rmns0KYjjkjCJ_D769o6mjpKolPKso43B4LU83AFe8pLR90bkqrg0DgYbL7Yb4_Y4pvXIsA659JQqYYDct4OcX3yvSQRsr03iwVLJp20fUMEHaN5sMoJ1P2G00tQJkzfqfFZKOt0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=X4AZZzKXrgixeg-I9OAMg74_FE2Ft6FvOBWmQyEsTvCD8xExNv9Zs29oeRbBgHTuX5EcbwOzX-RbZWE9K_c5YhjMOV0IkpAi1I4V6myrO4o7oOef7y-voPZtbPULgMHYLbbFW4Si9GhBBv_cBUDh2tSK9SzyhbhZrhoCrZFhI78oPN7jH6WZMR7CFh7L--o0TuxLX_JMyP1aZlvPZrRYivlgkqKZssrKXwmDFT4BuyoG42FipIjufQBAZ1wuUrPVgnuP_pi-USIZfOpQiHd4CZlZ9Mx-LhXNq9efD2DkHGJSZloDvcHeUr4GWWEZ11K3ME_GUkIZZA5w-q7usvz8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=X4AZZzKXrgixeg-I9OAMg74_FE2Ft6FvOBWmQyEsTvCD8xExNv9Zs29oeRbBgHTuX5EcbwOzX-RbZWE9K_c5YhjMOV0IkpAi1I4V6myrO4o7oOef7y-voPZtbPULgMHYLbbFW4Si9GhBBv_cBUDh2tSK9SzyhbhZrhoCrZFhI78oPN7jH6WZMR7CFh7L--o0TuxLX_JMyP1aZlvPZrRYivlgkqKZssrKXwmDFT4BuyoG42FipIjufQBAZ1wuUrPVgnuP_pi-USIZfOpQiHd4CZlZ9Mx-LhXNq9efD2DkHGJSZloDvcHeUr4GWWEZ11K3ME_GUkIZZA5w-q7usvz8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptCRICwDyBr0E-5S6AlZM-PNWeeucJAs6LgBM4QvL_5nIRw9g4YYQjEbpDPFeu9LFLbqjELBy_TtiLiepvQMfJNF_vf48JALk2EsVD-Z2nfMG3tErJPLTTnAHKwsCnXLZJcdFxMhQdv11tlOIajXYFXQzJk0qT-wKO7d0nK7du5Zkp_wTITZhLObaNn7uVWxrxQGWGj99TF8tOsdnbizDArXX2bMYsS20AaBDJ9tu1TTW3N7QiA5E30ytZXKe02fQZLSdzW8rM73IbFrSnnjdpBI1DmPaDmSE4PflM_wq4CCWOnu-5braxH3Q98mHs8PPFj_stHKu7x0VRxh-au1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOJtHF1o1ZiaHbz5_7ElLyIW18HVNmuOFWzih47papb23PD5YlOSYh_sw6Val7oj_sqlwPAYsG2C_gzVOCjVNKVEfaGNrvCI11yPAhHUvR8a_8-xCzET0RY73JkuyFcKLWy9p-D9dRW0Ygx7B4WsSOXy3ISIf3IMOHHCLyqaw9FalXL1RFu1vDNv_2JOJh7mpVpMzzM1PX7abZqmHDYaWG1QcgthNbj1NUY7Rnihi4XfQPLdPhVDiahp4vKAZvt9ZKyTHS9wcHdw_l_wgKcUSz2jGA59VKPNuVbezgLQkvgcJNDRsJfpkDW_laIkvNIgWcUp6TqXv12_1AERKRRs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=p1NukQB4IMHyNBueUlz46zXNJJNAYF-amR26P_A7XzhTkXyk9BOSbTlZi9rAoEeppps614y-iV9012mTktbFRhB83MGtlIB9wT9JeJETkuUBA9qjNtgZLN6pikPvuYkdQ1Xk2xAXOjLQ14WxdxlvX5IeASrXYmu2PLiK1oV17VJLmLPLIikOUbYf9zj4qDY_asYluGxabZMiRf2pJnwiK1B1dVwmgCw3nKwI0G1j68T54lEXd6h7D01EeF_OB1jngJUV-dI57DY9I9H1D8MORc7YU5tChq4--e3fvUuqZ4cu-4liXr8N5zci9ong7ppytIwe_MJoOMUSuAXG8mCGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=p1NukQB4IMHyNBueUlz46zXNJJNAYF-amR26P_A7XzhTkXyk9BOSbTlZi9rAoEeppps614y-iV9012mTktbFRhB83MGtlIB9wT9JeJETkuUBA9qjNtgZLN6pikPvuYkdQ1Xk2xAXOjLQ14WxdxlvX5IeASrXYmu2PLiK1oV17VJLmLPLIikOUbYf9zj4qDY_asYluGxabZMiRf2pJnwiK1B1dVwmgCw3nKwI0G1j68T54lEXd6h7D01EeF_OB1jngJUV-dI57DY9I9H1D8MORc7YU5tChq4--e3fvUuqZ4cu-4liXr8N5zci9ong7ppytIwe_MJoOMUSuAXG8mCGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i007Ap3meWuYKGSpHtqtiTuP3VzUXIYYHAPWJ5LewUbSDaArgG0WqngscWnZLOijRUhlZWpajXP_SGywbBvI11jE1K8tVv_yRIC3OkobH5vaL-uMWVLfl7D85R-Ql7TkTPsmdt0NRs2Ad1jZespBNR50k7UTvSQO1jKTf7e4ds6BViLhu0mJ1Uw2CwpJ9P1gKy0g1Q7pWjdR_ZeLVdpTiEBD8T5kapkflye1ouCt-T6uHW5EItL2fQ983EhHd_oL7GZSe20KxKFT6iaXDEvecbiY2UP5d67g9cMe5N1NsTgosk45EdS__d2sHx0eUaR303RJhAO2-Zc086oN01nr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=hp1l3laTkP_c9RNbnp-784B38FZc9SGHsXW2r80J7xxtg2XFkSP-MekQYRq8TbSDsJfszCdzltxIcXEO175Bm65Fzjl1ydphB28DHDHmBcjWQ6Z3Rpf17q7o9yiWapyPPtYv1O1l-khlOtgwqJaV6V4ZbsZ3bQs1eUWYGaIKXqgA0Y5EIAuOTbWlnPA0vzgYi6UvtPGU5PvapVj4YWTM_Znm54guON0EJRfFHtmp9zZH2cf_0nyGytqjm_FVkU61IVTAZNMCH5UlvR97L4kawh6HY-BIHKD4tNE2GWtA2UWcNqq2mBvMYFAO3HhOx6P7VJY8nQF5VmOCnwPnwB4W_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=hp1l3laTkP_c9RNbnp-784B38FZc9SGHsXW2r80J7xxtg2XFkSP-MekQYRq8TbSDsJfszCdzltxIcXEO175Bm65Fzjl1ydphB28DHDHmBcjWQ6Z3Rpf17q7o9yiWapyPPtYv1O1l-khlOtgwqJaV6V4ZbsZ3bQs1eUWYGaIKXqgA0Y5EIAuOTbWlnPA0vzgYi6UvtPGU5PvapVj4YWTM_Znm54guON0EJRfFHtmp9zZH2cf_0nyGytqjm_FVkU61IVTAZNMCH5UlvR97L4kawh6HY-BIHKD4tNE2GWtA2UWcNqq2mBvMYFAO3HhOx6P7VJY8nQF5VmOCnwPnwB4W_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuOtBQIHoROopenUv06ZPASXSIiHzH61cIiLpXxQEvSpWsDGawVh1hPtd9tlpL-e9_YUsmd6y9SxT01RS1ZilcjzYxdNAIR5OcfN5YFiLkIlwltMVARdJrYfbbFziNszjeOvh80lZ-l85Uq__0E8YiTPx3uLYG3Nxk2cxlqOD-e5XfxHTLkM5H6cR4pO4XLlNOSJycxNHj4OAi0Y03ZjRuRhbWniCbfzVgC3rG-8ScBycjGxEvo0pd3PbxXaj29EMtHMePTmNYEhNeW7Gw61Y1vQaJ_oNA8CuqStN5M89O2FqUMojTsdl9ny1C0EXSdNZ-I-0sE2y5gx-BcZK9QegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2UMGyCYflvlRA_UHZDTTi3uZqi90r9Fst3QEBja8UPcrpIEXMPbL0LU7o92H_LJ0TOmv7ixh5ADaGYtOvuEVReob7NmInzG5rJWkj7iMWIc68P2YuRVANBNJATvDCc-xKiIH3BCsTSrGPlRHklIGtUxHXbPwbPgPPh3P-7jwrnzgqrqzO7mSKxHzTtpwe2_C7Yn7yQHEUPrmZc1b6cvwmDIgKky5osbLJDMvoFVaz0CHJhBkrkdga3QDKJV1aAm6OY8xPKiGQKApfmw0iQnzrgHI6KD1a7UAT0fNgSo6b-jOnLWh3K3q1vwhpMy05HrcpT-tMpG3sP7xlsPp-p3nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dagVnN0j38PZxQNLWaBfzCrOvJEC-zuPl927M9nViv1CGcSH9PXeFusjVXqQqzxeyjo8K72U6sxqg-HwoO-TjyFsNDvJh7E2Dj0v5va0l5NKEiGhDRyGdgSR-QVAvTX17ZC_ONqksdeuyqhtfmSoL7rJ20WowqHzHvURtqx2vik_B70b9af4MyFXIMOaXf6fDp6_-j0XDjcRmRAmFC7Wxe4hiGxXMrgjUzLt78PM4lqSLhgMcwbI4dfYleGJIg3AeBWEBeFG7b6rPL0DHdcWcWRm3Xbrp171D8gvqZzoPknfxd0zrmXfpUjs-29xffmnh8QxZWbUN4eysarjFZZjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7Nyj0D9twGiBK57adkcto9zMnYUSHNMLjc_AU4acHBHg9qhSsUB14d2B1REubDS568qdxISzpbryi9rokyFsJFdpaA6MQ6FFzyYRf3soJVoQtkCLCrft97UdHhwjnSMJ4_mXLPBvBLPX0CS5uZTZvSZlJWibFKJPFb1IW0_Doq8Wx2d1qygvX4NyUSeKs3LL12jK9LEULgBeofCKsfQPFrjdE3zDeCzGJoxWn1bl5GRYTMP65_kw2HVP3apaDGi--QxNh0WBq_GUpYwgA48IvUOOoMW99-y5rC3SINvTxyHteU_oogMVsSKba7_zEBRJ_bqHYDMBzM9n-uWL9y-fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=V7o6z2Rfi85Qi1TbkBK-oiin7zhwB6VFTDu-wopq8Trp1wpcwnz93u-pQ5bagIdBAZkX5RnndjdZ9pf0kuGbNF-ZQi1WEI0nnjlGFBqoTDdvoR_Z60B8PugyYuLA17ODrH0bHBS_kdI7wuVxRz4vDIx93TgTZ5-oyDyenvCKiPVpm1D6_M0p3T9R8zRR5LiqL2EBP-vwF8CmdVUyRVxZSV2NgWwUGkqkM5SkHWmKmg54bU-zV0jDjn4juU2ezddhccNZVo2asGOftH9Aj-vtcxDSpjKZyQX-UluOcqS6amF-2y_YvPTeffrWz-KbRA0rUxt_gCzdjf0pnXokCHOljw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=V7o6z2Rfi85Qi1TbkBK-oiin7zhwB6VFTDu-wopq8Trp1wpcwnz93u-pQ5bagIdBAZkX5RnndjdZ9pf0kuGbNF-ZQi1WEI0nnjlGFBqoTDdvoR_Z60B8PugyYuLA17ODrH0bHBS_kdI7wuVxRz4vDIx93TgTZ5-oyDyenvCKiPVpm1D6_M0p3T9R8zRR5LiqL2EBP-vwF8CmdVUyRVxZSV2NgWwUGkqkM5SkHWmKmg54bU-zV0jDjn4juU2ezddhccNZVo2asGOftH9Aj-vtcxDSpjKZyQX-UluOcqS6amF-2y_YvPTeffrWz-KbRA0rUxt_gCzdjf0pnXokCHOljw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=NYCG42rGgJw7iSwCg_cVhaXA9uZ63peofsqbxxHQ66PjBMkPXrXICWo6R4x04h07aerbiIA0ZdGt19YjdFurDn2OWv0OlUNhvUodTGx-MFfbco0QGNAS47whQwUX4kkx2lHEALKqP17WM4TM3Hp393YktJ3we6lOa-duYwNAtItq7nmp8_0sgtMNl_LiJxD37UuNMhm73-ErndJeVHY0lEaiq1PU6VI_ndGtFrLpVTLCNYpr-P0LCphE0R-6BA9_PMcc60exx_hUASwO-QGVgDHQCCP_PfoE1JYfK1eG7tFlV7oIPPLe0_VYb-oHLAlokTkO2LY07bCkw7pLgSg0uxY9Yk4P3FslfipzX-qP6ZAHFOuHIYcwsareYhMrKAJ5hWVWvsiIgU8FPi8O9Dwhr5UErJEHI5a2MTpZ9WI-Qzk-PTYIF6VWpObChbVmfmGX4jk2uOzwU2Lw9WRgbWRlcBHopo4nIUzZKS3ld2k4uaKulIN-6wB1B-I9IrXDELn22NrVJ2sbmWrFs7_gWttpbhSvbCVK8at7d0h1hJiASnL-F7mHIp3eJjokZtkvkzk37StT4kVV2bvMV7CMe3F6m-WzJvmmIKgxxPh3c6i0YlgghNWbC-C_uI57kYuqfo2XIucAQgBklKKSwxZt8ssdsNoX57fVUZqimGbPuEv3lqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=NYCG42rGgJw7iSwCg_cVhaXA9uZ63peofsqbxxHQ66PjBMkPXrXICWo6R4x04h07aerbiIA0ZdGt19YjdFurDn2OWv0OlUNhvUodTGx-MFfbco0QGNAS47whQwUX4kkx2lHEALKqP17WM4TM3Hp393YktJ3we6lOa-duYwNAtItq7nmp8_0sgtMNl_LiJxD37UuNMhm73-ErndJeVHY0lEaiq1PU6VI_ndGtFrLpVTLCNYpr-P0LCphE0R-6BA9_PMcc60exx_hUASwO-QGVgDHQCCP_PfoE1JYfK1eG7tFlV7oIPPLe0_VYb-oHLAlokTkO2LY07bCkw7pLgSg0uxY9Yk4P3FslfipzX-qP6ZAHFOuHIYcwsareYhMrKAJ5hWVWvsiIgU8FPi8O9Dwhr5UErJEHI5a2MTpZ9WI-Qzk-PTYIF6VWpObChbVmfmGX4jk2uOzwU2Lw9WRgbWRlcBHopo4nIUzZKS3ld2k4uaKulIN-6wB1B-I9IrXDELn22NrVJ2sbmWrFs7_gWttpbhSvbCVK8at7d0h1hJiASnL-F7mHIp3eJjokZtkvkzk37StT4kVV2bvMV7CMe3F6m-WzJvmmIKgxxPh3c6i0YlgghNWbC-C_uI57kYuqfo2XIucAQgBklKKSwxZt8ssdsNoX57fVUZqimGbPuEv3lqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=NCT7Wy-482C9GrUZBH3kBZ_13MhJrFpgSsyurfh4h7AuLps3rOkUXXOGKKRZwUqJk3FpSxe-EuNIQnRoE2n_35Pkh13xROiatsoFNLopzrCA2UFXBRGy85NNsB-kMgE2or6mEcy1SmeM2vsyMdfc4P9RB7D9iJJpUVQ6DO8WvGnawWtjr23oWSKdRlePlyP1vg3N0Y4YW1M2RW0Bb3ZPVyyCyj5nfTHX1v5zB6ivbEY6UCHaBFV9xqVdcZi1WfxkSsZ3G5CEgTXT3PYGKkSidxHTKbDERQAyH4zmMvqXKq_jZP-3MPfG_y0Vjo32AH6XAiVJNSlM8IDEGlcMM06eVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=NCT7Wy-482C9GrUZBH3kBZ_13MhJrFpgSsyurfh4h7AuLps3rOkUXXOGKKRZwUqJk3FpSxe-EuNIQnRoE2n_35Pkh13xROiatsoFNLopzrCA2UFXBRGy85NNsB-kMgE2or6mEcy1SmeM2vsyMdfc4P9RB7D9iJJpUVQ6DO8WvGnawWtjr23oWSKdRlePlyP1vg3N0Y4YW1M2RW0Bb3ZPVyyCyj5nfTHX1v5zB6ivbEY6UCHaBFV9xqVdcZi1WfxkSsZ3G5CEgTXT3PYGKkSidxHTKbDERQAyH4zmMvqXKq_jZP-3MPfG_y0Vjo32AH6XAiVJNSlM8IDEGlcMM06eVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=TIerLsHplmP3tK3cZ3v3diSVb4iOpXJ2aHFIkGqWTzIoSSM4aRJwcVOJzW2aqKSuPf9rYUWuXj5e2G8Nu3T3pgKoj2P6os-Xh8EXUtUVSatdJNNQ_rZrQTcbOKbPqg3dV6-lyK9fjhqCysg9zFNnVHmo3DwoN_8duU6xco16wh_EFXBHVBH7x9qE8NmhXO2exirlk_6L7zjX3lVPJe_Inf6hvTHKQUAZQjvxhpaawVXrZePgwYu1oMaZoIv3dEgHLY_GhJTh1qwUY0aN0chq-PRIqNWMR_rlYmQ-2Pda5x2ath2-gKTBtjveZnFbUdYhmtWECAuQaZR_fo91XQTk1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=TIerLsHplmP3tK3cZ3v3diSVb4iOpXJ2aHFIkGqWTzIoSSM4aRJwcVOJzW2aqKSuPf9rYUWuXj5e2G8Nu3T3pgKoj2P6os-Xh8EXUtUVSatdJNNQ_rZrQTcbOKbPqg3dV6-lyK9fjhqCysg9zFNnVHmo3DwoN_8duU6xco16wh_EFXBHVBH7x9qE8NmhXO2exirlk_6L7zjX3lVPJe_Inf6hvTHKQUAZQjvxhpaawVXrZePgwYu1oMaZoIv3dEgHLY_GhJTh1qwUY0aN0chq-PRIqNWMR_rlYmQ-2Pda5x2ath2-gKTBtjveZnFbUdYhmtWECAuQaZR_fo91XQTk1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOMjg0EdqniXdJg5CzuzZ0IkUWVYCewKcYL8f27q5Em8rX-dh3WbBiKg3Mi9EiWRvLz0Uoqh6pCAN7ol2M87tnYHx0HR91froEHCgQFX7bAMDmNPgLqlRja32sq3VEXWVSGQ_u9uw84jp5GuLKXQoN5cC7XRD7yHV_Izdn0p8hvTO_5heQnzN7RY4HBrbnDMjLh8-T1xvKva5uD_a2EN6KUaahwe6p_RG7kb_MWBKLoWUAV16fK11ZRyXL6LC23LUhlDXGeeCt0d-AgUfjbZrIwfBccRDAV2_JKc96fr4ACRphMH6S4yqgPWsA1znar_bgyMQnyEgjp5IXr_5XW5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=eJuoHkjZNgAd5_FzX0pyiVtwUS5nVO5o8PL-bdY5Z-Y3DlBwmgdTC42R2Z2BYCSAYQa8dYAdPi3P4M6TmH7tYAQfDbFkjeWB3SElI0lJYz1PP5M_HwJ36Quq4Y86FMmqzqtf1pqB9sra_m3YgTtFO5fNMyaebyohZC3hzx3MduabkgFlbufdCjZ-MAGGfVHfLKVR8gPTpgmLwl4TObmxbX14eAbAC--TvVgpOx3Gd0OFhgm3JvVvDvtu53WLnt8jOxq3QvsDu6OtZQxyvd5zjnTPfeZyFXhveNszW_8CBB-Hymc-mjTttjsOVDVLXlHF-86UfeUuwIZA32NPBLkuizZ58_DucGXdaXRCuomCmWqUmMz2C61kQNbir1uqM1zLzMJ3sg066V1IyV0JVP3XH_XHrPPV-w9sTWOd-yFqwcunEX_Oz6jsVC0d352iAMv8iC-NiO4u8oQm482D_Lv-4Eso981xUmjq5eFMKAPIEOQq-ameR8zJV-MocNlDYiUaFFJOo0tquN1ICo4WRk3e57OoELdCINnOYT1auaoMSx4LYO_bjRFUNPZFpyXmlCi1GBFUvtN028Iy74kkPU6pefJh5Cl3ST2AgpodPft6RBTPaAvEzMP_ykcLuCkHgMIOXrtzmH0c_MX8AZiQ2TNndEzv65jJdwXqlJAr0bAcAJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=eJuoHkjZNgAd5_FzX0pyiVtwUS5nVO5o8PL-bdY5Z-Y3DlBwmgdTC42R2Z2BYCSAYQa8dYAdPi3P4M6TmH7tYAQfDbFkjeWB3SElI0lJYz1PP5M_HwJ36Quq4Y86FMmqzqtf1pqB9sra_m3YgTtFO5fNMyaebyohZC3hzx3MduabkgFlbufdCjZ-MAGGfVHfLKVR8gPTpgmLwl4TObmxbX14eAbAC--TvVgpOx3Gd0OFhgm3JvVvDvtu53WLnt8jOxq3QvsDu6OtZQxyvd5zjnTPfeZyFXhveNszW_8CBB-Hymc-mjTttjsOVDVLXlHF-86UfeUuwIZA32NPBLkuizZ58_DucGXdaXRCuomCmWqUmMz2C61kQNbir1uqM1zLzMJ3sg066V1IyV0JVP3XH_XHrPPV-w9sTWOd-yFqwcunEX_Oz6jsVC0d352iAMv8iC-NiO4u8oQm482D_Lv-4Eso981xUmjq5eFMKAPIEOQq-ameR8zJV-MocNlDYiUaFFJOo0tquN1ICo4WRk3e57OoELdCINnOYT1auaoMSx4LYO_bjRFUNPZFpyXmlCi1GBFUvtN028Iy74kkPU6pefJh5Cl3ST2AgpodPft6RBTPaAvEzMP_ykcLuCkHgMIOXrtzmH0c_MX8AZiQ2TNndEzv65jJdwXqlJAr0bAcAJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=XKA5BJKJCZTKsvpTVxoqhCa84AqFAVBiJUGpOrwcZb6akYNuXw3D0Vjjl-duO1yldcXCEBTTXCgH5y2i2Lr2KB1LXebES2ZXIxM0NjxGKHxCeglJvv_I-X48yA0ylivUi8rBQGIkTAQiEEGQqJQyPvva5FKvGMO2-xpgjY9c2CO-xgiWDCZpaz3iWtsYNGN9KsbSGsjOuKW7cPdZzDiWDUTC1uhqoRErDEmUXo5zaJJ9lKmRbxdCRasTf_SfaTOo5w8R0FNy4wzlTQH2nHtYlfMNEjwowflPZB9wNlwsVfemZ-RlU_mUyAHVWpRp2cVmWoj287sYhY2vb3a9fj3BQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=XKA5BJKJCZTKsvpTVxoqhCa84AqFAVBiJUGpOrwcZb6akYNuXw3D0Vjjl-duO1yldcXCEBTTXCgH5y2i2Lr2KB1LXebES2ZXIxM0NjxGKHxCeglJvv_I-X48yA0ylivUi8rBQGIkTAQiEEGQqJQyPvva5FKvGMO2-xpgjY9c2CO-xgiWDCZpaz3iWtsYNGN9KsbSGsjOuKW7cPdZzDiWDUTC1uhqoRErDEmUXo5zaJJ9lKmRbxdCRasTf_SfaTOo5w8R0FNy4wzlTQH2nHtYlfMNEjwowflPZB9wNlwsVfemZ-RlU_mUyAHVWpRp2cVmWoj287sYhY2vb3a9fj3BQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx8vPlXNfTsw_R-7ogHd04ezuRk4ZVP9HTipuovv5UFLZJtj_0RutPLvVE_YvGKD2KK15B2jyqdoWP9E-oxCtDMc0MIOlYHqEKWSKHgfBZIqZg75GBsw6UpCa7nIs1oHINAxtPlhrfWTkOebZDETtEeZHcypTFs9F_PeBAySxhgvOzKamfeeKlkHd30hpr9vDmmOZtmW9u6p_DDWR5AuIPNTVEXGOn2wnzASIq52K4tEZcBIwtbXEK5T-0dA0ZvRfqFRSCWaFG2lZeo6lQe9FpPunGho-fTo_jnMip7ufjMwa7nZDJoa3ADhut57MJrtriONNFYP5PoVEooRdZ6K9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=dc9BMf5N7UjMT5bBbDNXgI-Gnyb-fJxyb9bk9eA84nVKtKMQEXsQyTZXIbGLWXrqW4rasR5GUALq8Pl4BSqr8sVuUXnErteJfIKmVfWD81bz3FRvYXg6qxbi4Buvc-gj6nuuu-B7DqZy8-h_WevYsyVxhnqawChkSl3c8sgmDhWmBuwzrw53utmfFrK2iEj6VryjZmrvZyvtGRwjCYBvFj38hEyXBlI-wy36FuQAy0Fu8lUbXocDSBeiRo1BBZUhzZDZlTiEU84ShSDcXHpxHMoWotf5h1XKnP-BwsgAK3lBabOlOjXjRESkV-CX9QjypIjQ0T1LbCOTGgfmQELo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=dc9BMf5N7UjMT5bBbDNXgI-Gnyb-fJxyb9bk9eA84nVKtKMQEXsQyTZXIbGLWXrqW4rasR5GUALq8Pl4BSqr8sVuUXnErteJfIKmVfWD81bz3FRvYXg6qxbi4Buvc-gj6nuuu-B7DqZy8-h_WevYsyVxhnqawChkSl3c8sgmDhWmBuwzrw53utmfFrK2iEj6VryjZmrvZyvtGRwjCYBvFj38hEyXBlI-wy36FuQAy0Fu8lUbXocDSBeiRo1BBZUhzZDZlTiEU84ShSDcXHpxHMoWotf5h1XKnP-BwsgAK3lBabOlOjXjRESkV-CX9QjypIjQ0T1LbCOTGgfmQELo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=F8VeOkWwq9p8VMfNZhVUAA3aX7CY6f3vF1s5OoE9feH5Ty5-mSKoWicDxq9z8tHKcow0yxPfxrm4M7Uf-ZTMj3LsglKtn0Dn5qJWVR_D8I7FZEt2Ykqsti_riTUBV0PSI9qIvVwYI9tSwb64OPE4Vv2HE-Emv_PhgQ4p2V3xygH5hsWEcvZSU_f7MSd48rhGqp69AshGXWAeKjfwGpfUvqK6FdpP6r6KZ94WOGbEXmlw4RY-5UNbKHcN5pZmptm4j-U67M-L80tpGNzeMf1emu26B6-cv61dE6EOPPtPVBMJZZovYeeyL4rDleRurRKGMBYVLGrrEekXzwJHEEE75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=F8VeOkWwq9p8VMfNZhVUAA3aX7CY6f3vF1s5OoE9feH5Ty5-mSKoWicDxq9z8tHKcow0yxPfxrm4M7Uf-ZTMj3LsglKtn0Dn5qJWVR_D8I7FZEt2Ykqsti_riTUBV0PSI9qIvVwYI9tSwb64OPE4Vv2HE-Emv_PhgQ4p2V3xygH5hsWEcvZSU_f7MSd48rhGqp69AshGXWAeKjfwGpfUvqK6FdpP6r6KZ94WOGbEXmlw4RY-5UNbKHcN5pZmptm4j-U67M-L80tpGNzeMf1emu26B6-cv61dE6EOPPtPVBMJZZovYeeyL4rDleRurRKGMBYVLGrrEekXzwJHEEE75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=LdBrNY-XJwhqWPN7UJe9e2hvtt1322o8-Ck0BB5uurgGS5TDvotuMzfwg2VZ8s_11hwYTBxfBKbF7PsOXnUhP8UCDmCgBOaB49atthO3-0E25a4DHXDnz7iSKfY2jMsAy7cMXfXsqTl2BL3OQ2_TlWUvkMvw17df-XX2ppr_PYsIVBvj7F8JvLn5w6qyeSCs2efApY3WuLZTwJpFPqrIyXMCkLsOmaDnAmTnNxG7SrXvH1qXG5br1ADtfC7o11_0q8_uARMizFALoryCd7e5HYPPwYcxvLRGW6-MFETCl8iOAB3J0WMFSxiXM3uZuP1rKlKOdSHi8MthxN82YpamJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=LdBrNY-XJwhqWPN7UJe9e2hvtt1322o8-Ck0BB5uurgGS5TDvotuMzfwg2VZ8s_11hwYTBxfBKbF7PsOXnUhP8UCDmCgBOaB49atthO3-0E25a4DHXDnz7iSKfY2jMsAy7cMXfXsqTl2BL3OQ2_TlWUvkMvw17df-XX2ppr_PYsIVBvj7F8JvLn5w6qyeSCs2efApY3WuLZTwJpFPqrIyXMCkLsOmaDnAmTnNxG7SrXvH1qXG5br1ADtfC7o11_0q8_uARMizFALoryCd7e5HYPPwYcxvLRGW6-MFETCl8iOAB3J0WMFSxiXM3uZuP1rKlKOdSHi8MthxN82YpamJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=TR_dRVTmgp5227_lj0b3spvdCGA6QncF6M8agddjw5fakVLgQYZaraA9slf6vEHa2-4fyLuv4i2L0uayodczKRcHs80r_EK8bBLkcvxqSnifNMaO4IET9P3A38sRjPllzG2952-RjwAd-n_ze5Wn-M9As0uKk06sXkXV0yoR67O8-fO7hF8nsu9VFdViovd_yxZBu2Q1mI28DoEP8_Vju5tqn-hVNuJeWanbRJXR4ZZ60W2f1_QjaoaS7GP6Anx2RNqRIyJuHU0AZbNFon2XgOR4WVQEwzzbAAczl7UkqJK5fad8wj8kjgf8GWNBge81_4_cBqSCRqjij_m1u6i79kvVAGgbugCfqnih_2mYBi-touPXlxttc_Ec4_zqLCS_bZ1fuZ18jlxmmlCiCQNKGq3WvnP-UticdW0z0tliWlTrxNRRjfCQCgHKZatvDripQzEnznsFaBLEi17-HtvCi82PeBEqMr4QxmAAuNIYvsa3YTRSVZ-mwHxyo6G7pnZkWculxSKIWhG3tfAwPnwNxDOxH8Xj2KdQDc59-r1GcbW1etCjQKR-coM3a8_jULpJZoA66GXb7O1OWVgqUwTh11YGxIb6swPrU4pcbev7usDAhrwi0Kik4nD9Rjt7q1vOEaq1hYGZFPDcYC0WwVNrQueI-xdaLlNelLT5hCa09cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=TR_dRVTmgp5227_lj0b3spvdCGA6QncF6M8agddjw5fakVLgQYZaraA9slf6vEHa2-4fyLuv4i2L0uayodczKRcHs80r_EK8bBLkcvxqSnifNMaO4IET9P3A38sRjPllzG2952-RjwAd-n_ze5Wn-M9As0uKk06sXkXV0yoR67O8-fO7hF8nsu9VFdViovd_yxZBu2Q1mI28DoEP8_Vju5tqn-hVNuJeWanbRJXR4ZZ60W2f1_QjaoaS7GP6Anx2RNqRIyJuHU0AZbNFon2XgOR4WVQEwzzbAAczl7UkqJK5fad8wj8kjgf8GWNBge81_4_cBqSCRqjij_m1u6i79kvVAGgbugCfqnih_2mYBi-touPXlxttc_Ec4_zqLCS_bZ1fuZ18jlxmmlCiCQNKGq3WvnP-UticdW0z0tliWlTrxNRRjfCQCgHKZatvDripQzEnznsFaBLEi17-HtvCi82PeBEqMr4QxmAAuNIYvsa3YTRSVZ-mwHxyo6G7pnZkWculxSKIWhG3tfAwPnwNxDOxH8Xj2KdQDc59-r1GcbW1etCjQKR-coM3a8_jULpJZoA66GXb7O1OWVgqUwTh11YGxIb6swPrU4pcbev7usDAhrwi0Kik4nD9Rjt7q1vOEaq1hYGZFPDcYC0WwVNrQueI-xdaLlNelLT5hCa09cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQXWl0g70K2-0nhba-Te9NDGFalbHwi0dEvgV-x26w7JWwHGWvl7J8Z7lEuJTx71z-2gBvoDDwjvx4rf8gZMBBTt0pmYdRmMWdlNTgo-ZukjWa1yXV4ochf6Fou-kvkNGGws0tRLMeX8UaaPZQrucDKDMwVZHKTVItwTtQvRSXIbzlhp5T_ryWa9jebA8xlkkq8z1d6nemfOvtoS1crJREOu4vcA-eZo9ZQMIOP5bslqS8w0npifaRXPkRnYTtvaWCChgR0b3FNeNET05pHJBDR7olnRzq5EwCvAFqHPZ4bL6tZJpIz7ja4nVy2uGxEoz6gM5D8i5O14q_o3JzDKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=G86dia93A_LNpwAAdue7oFUN1lSh-UXzSm_d4mce29B6kvptREo2Zz_wZ5-TDK9-i4D4jbyM9oVhJqYP8NvISWmr2FInYGEr2ndNva6MaZZEkmhPr0H3SuRIr7LIcD3EP6c2JZPYSGzsVbGW_KRH46iAmLr2RfUgWI1lwEK8Uo08kBUU8nwpa2sgsdxbkG31OawIY0gm-UHzueVAFsb6KvqOrdlBptkyCQsnH21pJNPOsA8QPGO1bt532PjcOrbIgqacdqziCEwYThm3BbtM4PVHLJSmf3WWz_EnuGHR9X269KBRxTCWIcSX8ZpTmJEnjwFpTlV019eauW97kOGUbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=G86dia93A_LNpwAAdue7oFUN1lSh-UXzSm_d4mce29B6kvptREo2Zz_wZ5-TDK9-i4D4jbyM9oVhJqYP8NvISWmr2FInYGEr2ndNva6MaZZEkmhPr0H3SuRIr7LIcD3EP6c2JZPYSGzsVbGW_KRH46iAmLr2RfUgWI1lwEK8Uo08kBUU8nwpa2sgsdxbkG31OawIY0gm-UHzueVAFsb6KvqOrdlBptkyCQsnH21pJNPOsA8QPGO1bt532PjcOrbIgqacdqziCEwYThm3BbtM4PVHLJSmf3WWz_EnuGHR9X269KBRxTCWIcSX8ZpTmJEnjwFpTlV019eauW97kOGUbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOvqzulaTPTiy7T8YBvOEIPxRN8_Yj0o7nHDiXA-ZCR70n4N118qRU6V_W7GvhAH5GuSzOtE1I_iczd4Oyd1ulfnmpqKtq5KQ8nfWtURlE_HGNk3SIZTmBRKhduKtETBhU9ALzh54eM9Eni3W0B4R8_qgphffMmuoSl9y8eSLeuObLHYNLGJRRBf7Nk5XPVce0_dVHXE-yjkWZFqj-dJ66HJNtc6rJhFhDQl-mDzOYrl2d05biQseFy4Zn-43F9672YSrxgXI7KpfnpCE2TSfplCWd40_0hANodtArj3uymb0SOy2_EH_RhEkxHAnqvO22D4CFCo_W2IIWO7QDQ0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWW_A5QrxSZhcn8EbVbcx3HD38wLC2ymNXdEwRybmNTHJlMCZJiebJj5W64r2QaGCnE7RFZhOUcHXLc04UJHnLVAbSZ0MG546PWu2eNYhu0onBfDPsnEbdnHn5xndRsSszPQl5P-RNSlVQxbECD0oBlYhJCoSgI1OnRmnc_lZ3iuxYhTl47MEVCFGWaEuvHUs98s9katxo_JfDLA6rbYdCJxKqK6kYNHSeDJ8lrNu7j805AtzVC7nRkZdRy4jMxtj-1UbIHXMO7uvl5Q4lSUrmhN-P-UqrbmrVdgsCkGQLK6A9000_yChDXnRJV2jqWIFqY-C6x9bUxKW4GwKPzehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q18P5nAFsu5QJWnMxiznvzmGCNWjEcVq5fdO-W6lr6DyV1uNuROphM09VykVI95rqleCrHGI4rbbBewvu4JP9-7YX6ivkebgqwy0luc2ffo5D5OWNsfeBBB0Mj6dXUhyNxGNODaNhuWZeZR24f_hgtV_jLCryPjJY4LybUbha4SWp9z9bHVI-9hmmIt1aXgaOjWQrwbQrFbtH7qq1HLeWQmqVNMOh5LNBwbGpVqQhuLevalsQnjQ2IG6aovaLw0VsbqF_VzoHtL7iBtsJI4p-aQASzJ1EgsE6N95lq59wSGe8_7-TkHKf4yHhl20BewFXNDvhzistsjQ6axl3zszWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3r1FYGP0QVYPx9HmYfabYxbiYUas1WQKGIpO9tXjrlE0MwmEq-0KDp47piguULwjvBrWWd-P6JOeFmciaF_dwxq6SRgPClA8S_CV-QdgE6cM6baAujK-xxZZ-xrYHfSBwcElHJGxEpv9NVpWJGChK9RoE0D3dEHRz_WZSul9t6PRyRpKnG3wcxnTBjq6yPCsHflcQt3F2M50Si4W5GboO5udCLwA7NgN5z9RwG5NxENKd3vZs9egW53uZckCZntzbilpLkp6492Ygad1ictb2j_XKOl2SdYnx-BAX-_yhBblZVWgkwE8RDUJSId4-P0Ll5QHLNVC4rUVmWQRtuTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZehE4xR5cEgtXfhNd_bq6jyWN4lD7BlewctUKNmZ9AAuiSUhe07lA_EpqDiW51cjs94iVM-JekaKY5cP_lYXY0LRoX7uKVlBd5aRmUnnxhWECPBlkneUs_Z2WfnVaSfiZrnjF598RR1caZXT_6BGNv8WqQES9uDiAwclXC-JBHFW0AU1BUJILwTOBeidQkDPJU04gDo5ddmAVepdHvpx9RaRX-oLkcay7-EQ15MweT4F_KGiXLYFO2k8zz5toGD1HrthiLG0zOdWd9IsD_9ByTyz7zD13Q7wJcrUODkBJwNpLDjXFdyb_Veu-mYcCBiHoJipbBjZ0ycuJ8ftfg14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0bNb34LqgkRFhH3Ch24M0jQR34T8-dpRD4iVvGRAYpamzOXJMQ10qo9B50ouWcG0CNP-_baoWoJHr7wIMZ0j-O3USPIAgoFHAxRZ6d4o8Eimlp3PXCJGh18tyRjKjN9w1ZOjdCeatzjrnSz0EV01-j7UNTjoOZxX5qkcZ5VuxoBzGK3AsVgfPWloRjXE-QJcUO0mlrifaDG5hl_u7OMv4aYa7oAryqdutsTI7wluuPHtGaAYoLD17hjw5rwcW36edYcyfDpXwFEWiZ4RuGMSmTM86is7NjvuTKqrFuyInajlmUD0O0wiGwn2X8f7TXMe5jU9v_qlo4OnoNv1gUQcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYsVpTK5YkOdeCCCFn5b6GKb4kk-yLt4SplsqCOb0nva1Cos37HLc2A9MOEpKtkQa1N6k7Jo2ioKDjuKWulFa6d0jTNpXR8XiLPV-4G2dflaH5AUFxD71ROMMKVNur48qoBvajGwOXr2EeceVp1BIrZzZyi5wd_fE0JdQcMRMicd2BWzGgENuRt1LFteLEgnm6BPVjFkIXdy4XiU1k8c-izn4rzgAdK6NPeCYM4x4dQMYShXN1bfYWiQyeXvubT-gu3zgWoBrP7YjsogYpUCE_eGoYXdK9T6VYAlmP2J-qi7rDhu_jLkxfW_bKWq8z2XH71bO1VEDdmCOrRpvtS65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPWsvCHFs7_ygyaLzpbQLY0S0ilTHlvQ7dE2FoRyxifQGkxqEHFxLwo2PnR072JH3sB7nI5w86A0okbJv7bP51zI1CI-4y5y0RYeyqQN1tVnAV3XZz8PP1zivot19lmswLma9G9Zsdgze94Z4c3mC0vA_vfwRDM4pxsF2EOJf87zuhA4Ll2tcOT7V1DopHLH5Psk7iL2JheNDvWCuGJ-ZPUqLJ4lomp3tBfS6Als2d1DvWZd_cer4DHJ83IpPo2jO5SoUZgoh4QDysoCHOJu92CRD_HlddiqS-2q8n4EKd1LOfnGVA-q5_iBp_BrpEpZTU6XEAgYUtx7IdY5WOy-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpJpADDqzw5BeEnoS8C1RY0tT4WJTRIw2LTzG1CWFC9cu-Y_x9ZIm0AMI9HaZ8YIFGjwRclJ3W7NtLb369Eyc1QzFcgJrl4Tk20FQjPgxPRXpz_j4OjSfeui5ontpUweP0fNtftL91cFHBsOeFEjViUSHBtzQdhOjlOtWQazm9TkyuiI34picD0dlkdZwTxfFy-H8k8gqde9vh_erwhtjyk_WKhJ4vGbYs9zeFb_zBIt4bBlNZnvB2glfngAJcNMr5tgWu3ZiblpE7TxjC827gMOoH6Sf_C8x16Uv6BZkbGmHxltUdyY74HveDYkDKuR6JuYFq4CfE723uRNEMqvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ-_lmeVLbeidxqrPtnuGv692kXh3pNq5t4wORoGyVRrGDIOCAyyTib4lBPRudEOjiZ_ojoPXxO-IT-r9J5Avk_x6GXBGxa9zTRp0ne6p6l31aX4Mijnu5ASnI0UiLqSVT5hOf78M4_E54WFCJukcehHBtU188xO7RnFl1IrBgza84ZCHGs2yTeEvfMqjEbeZPP-MVDZZjTZgxoNMwve7fGGlO3gj8Vu1XjoX1288FTLIQzmm2rhFk0SZQMSL-1zSiBOJiTpg53DXgQ1QMHlNxjIzIGQ6sx123hYsnjFmhuOhyj_sGuSnPZp6oaqqUHq-q1X3UwtIiBhagPJkvJU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUJLsLKHfHQpERJtsqTWPjzKnQHou_ZjPzRMtG_yXDibJ9_OBUhGfYyjvjRwwiDzWI92One6oYn6MniDNoQGRVxEtSqjG3gQN5KBxG6PHZkQdXRY7jaU-knwY1gny5tbEEva2OSxW_U4FVLKejU1CgaWDFeM7D6eg7ObfvPTLP-cB8SIjbqnEMvGrQuNiPrPRmAaHXWMea_HRtrK2ixrKar-eZJjkanpVTSTo9HF_CMCc1hFwr5JpxMuRrztVW-HbZVFq9pGiTvTEjVq468F55NiJqRZEanVGBIvc28MiREqtw7MPopEiDONb4iJOi11VCh11r3VwzT-WVjctKJnpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH87XMmnHkS4RwwYGUHeUqrZxPUOUqq6SHC32yiqwkb-QMex-aa_hFfdyVdpFNBFng2h7I1p7sod_QkuD4J7999__AxHK5fFSqXhkRFupnkBqLLL356MG5oomazgiogH3wHWF9dkIsw7RTrVGBWVtoGdMhTUozR-5GOz-XeCrtSZeCjZSoIvvxuaCf3uzbowx1RZ9eTjmc9sr3DuAmh6h28S_7kiZPSWmXtkoFibSQ_Jz6fVvuuTGi3cfbW-jea18liayjifey0VQLkowKjIEAs06yyy5TeaPNaoD4dz4VNnOFSzb4L6iWuZnXSvfxG3RTMeX0WQDv0EVM7EbS5Qow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGEN5FsL9Br4ckENYWy3o-ifl7jRvZNirHSRuGHwnkk8wg7c8sNg2gduQPK4j4n1luWFYR6DyraPhJ_0rM8DJXi6MFt7ccXlMJQAxKdNdjFxivjKFqQjIfAW9LxTgSuiurUVQ6FOOq9wLyLGLUkI9tNPMXWafAHEapIJVza4xi-ticVtP7aKv4Qn8fBVpVgGtOni8s9wUhkgshbihtxSkCiJr49wnBh9MZ5dP80RiG6RrgOK2sXy3nF50zjSf8HmXynk7sM7yTfk7KHFFHhs0y57Qh80j-3P34sm3twTRg5PGoXlw8DX9eLhykBp7CPRgsr-y8kSwNO5VmFnUKgBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=BxrqKA3oDfjS4tehoSRIytUo3NDR1VrBOLGV4FuISKU_AQSyWJrK2w-AMNBZVlrCMSndKccuCsDY2oQgUwYQpdDZF4Fzrd7g8hBHblBUWJCfLhDZfNb91r9zCjYwkVVpL6F4SYsWk8TT5gom3zHYzbry2261siJ_7W0l9xjRScvmbETFJb4P5wNBW9ncg9DY-MDXKodJnBFYJeWFH9HTh4tLf6QZ9PD_PJYMSmXIo-GqycFChFozV04jthSx2tct-ejPx0k95TnICOQMcl39xbYYhxhHZL5yYgF9EvGh7P-KQLmNxKEYVTYIj5opJge0CZlRx4aIrfNMpoQL96H7GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=BxrqKA3oDfjS4tehoSRIytUo3NDR1VrBOLGV4FuISKU_AQSyWJrK2w-AMNBZVlrCMSndKccuCsDY2oQgUwYQpdDZF4Fzrd7g8hBHblBUWJCfLhDZfNb91r9zCjYwkVVpL6F4SYsWk8TT5gom3zHYzbry2261siJ_7W0l9xjRScvmbETFJb4P5wNBW9ncg9DY-MDXKodJnBFYJeWFH9HTh4tLf6QZ9PD_PJYMSmXIo-GqycFChFozV04jthSx2tct-ejPx0k95TnICOQMcl39xbYYhxhHZL5yYgF9EvGh7P-KQLmNxKEYVTYIj5opJge0CZlRx4aIrfNMpoQL96H7GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4iJw7xpP5CgJGlyI5DyELqsuijT0X0iW8JdXTbQjBTZ4EYzplzOhiKXLclOjfQea8nQa_d-5fdNrS5ERwpRU4cJu7oNWqlDSOKRKFgAYfGquc2RqV6jE5IzqUMHVFHtmw7dcWzg7ce1pUihF0bavfzdBslrrbySgvGd2KbWiywHa1xYkYPY-gHTQguPPJtFlMgz8LYfRIXsfXmaNQQRp8ncWet_vf88AIvvxsrccQZ7to2SFludD6_v4yEdO41Xo1wOTTBa6dXdg53MBN4lqVAZAZxpnK6N8fCBTCRyLk0nHq_VoO8nCUfrukTPssehVuD_XUwlRU9EFSFZXwt9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=T5t1zSu7x9Cb2jVXd7iINfiTtIeNRJn9VHHYvrhyZcUSxJHHH7yOmdrKhL2oG3WXGPr3mSL9inpNZsk0jXiBIuT-A9uLb-T3_qMMTddm_CnZVptU4YZx-OburM59ZfbGXO0heicJ_rZ8Typ_uCA994pUBllOR43nCQVAk5y6WpBDwQlYKgozRV3IxAuxlsibSMp_2s2tlpqMdD3sVDf6NonGWWaEyNk0Q2FvFTMvD_wcixTNvatvWSMrmGarKYHylRQ7gVrlt96Gn-d9ZmF27-hUC__XqR1ffS_0xXWcVYTN5s8LWRcm3r8zPc52i09WzuKUvg3UaoiTBjxHueSZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=T5t1zSu7x9Cb2jVXd7iINfiTtIeNRJn9VHHYvrhyZcUSxJHHH7yOmdrKhL2oG3WXGPr3mSL9inpNZsk0jXiBIuT-A9uLb-T3_qMMTddm_CnZVptU4YZx-OburM59ZfbGXO0heicJ_rZ8Typ_uCA994pUBllOR43nCQVAk5y6WpBDwQlYKgozRV3IxAuxlsibSMp_2s2tlpqMdD3sVDf6NonGWWaEyNk0Q2FvFTMvD_wcixTNvatvWSMrmGarKYHylRQ7gVrlt96Gn-d9ZmF27-hUC__XqR1ffS_0xXWcVYTN5s8LWRcm3r8zPc52i09WzuKUvg3UaoiTBjxHueSZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_ANaQu-C_s1Gu7t5O5Ni-6UH6Khd0rK1EF9s1cQH6TvV_t5SnNGELC1KQ8yn2HMhVTvI-bFF8cEHRmx0GRQ0rtx2gufWnzjUs9aWZKrSvdDCOWr00W-UyI9gBsnl-Jn_1T-B3yEQQP1RfhNMGM1aurr6uilZnjIGHm9CTAcjIwXW8k_GXkrPmZVZF9L-RT6n1ueL9V25p-nkE_WwZiJkzz_BoMO6Nnwknn11EIVY6Nu-gRSHbfaCvot5GM6nFc7tnoPWpqhyq9ARRew-910cmrzYSIyKDRIYp-bxSVbAAkIKg5GPYObx7AWkXB6Rzj7k8TOW3eYr66Vgvuj7tObpK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_ANaQu-C_s1Gu7t5O5Ni-6UH6Khd0rK1EF9s1cQH6TvV_t5SnNGELC1KQ8yn2HMhVTvI-bFF8cEHRmx0GRQ0rtx2gufWnzjUs9aWZKrSvdDCOWr00W-UyI9gBsnl-Jn_1T-B3yEQQP1RfhNMGM1aurr6uilZnjIGHm9CTAcjIwXW8k_GXkrPmZVZF9L-RT6n1ueL9V25p-nkE_WwZiJkzz_BoMO6Nnwknn11EIVY6Nu-gRSHbfaCvot5GM6nFc7tnoPWpqhyq9ARRew-910cmrzYSIyKDRIYp-bxSVbAAkIKg5GPYObx7AWkXB6Rzj7k8TOW3eYr66Vgvuj7tObpK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF7nS0mrCAE4ExWw9FQYrW291vfzKFudef9n65lzCIpE7Qnr0nxRkt_IqoF9GZlMpwmrJSckTYX0OwCowpPFS6jNo9MMe2V6wzOvD1AfP4JOMdDCOwDBOQaLXE4-9SijJo1y62kX-YgbOvZRzTHuSs2IryMEXP96PDACbD35NnyBT_zk3cgqRCi5YpMdkLI0KRPz4prt71xrca3ZjKgEZfz-jkFug15IbxaWS-hdINQD0mwlrtMD5hPxfWtW5UocWdRzQ27wuWRJ0cTo_RLAQ5KSBiEmRd1FIOHDpWXFm4wlM-zdeI6Mt60uxDdrjudpjn1HpJBP2HsMDDrNz-Glgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=P1HBJgJwEN_NOiGCV_kC_5fNyOBEgB2y2C_PcjVgGc2gHhMLZxpoAA5uuS_SScrKEQ9v0UypqSaGNOk0wVd_Ck9zXmEb-NmgrPp6_d4wWzP8BKXVwmA4b028OCPJgJWo7bHp0y48EHXtREeLETyqcezJRmYwaNGJ3TNHlk6v0pP_qvarbH-GY8QBiATv1MpI40u30J40HSQ7aM3LNbjnoEyVcbl4iaRZWOGg9pKizK-8dcDnocSAXFW3C5i5j1ueTDmKLSKnT5gD5jS5poh34UaZBGr-fz7Ni_iNtoFPGZIZMecdtd7zHqv1fmJPjjmCHVZlqEZKCgOmMFwWs8aHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=P1HBJgJwEN_NOiGCV_kC_5fNyOBEgB2y2C_PcjVgGc2gHhMLZxpoAA5uuS_SScrKEQ9v0UypqSaGNOk0wVd_Ck9zXmEb-NmgrPp6_d4wWzP8BKXVwmA4b028OCPJgJWo7bHp0y48EHXtREeLETyqcezJRmYwaNGJ3TNHlk6v0pP_qvarbH-GY8QBiATv1MpI40u30J40HSQ7aM3LNbjnoEyVcbl4iaRZWOGg9pKizK-8dcDnocSAXFW3C5i5j1ueTDmKLSKnT5gD5jS5poh34UaZBGr-fz7Ni_iNtoFPGZIZMecdtd7zHqv1fmJPjjmCHVZlqEZKCgOmMFwWs8aHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=KEp0lvmjSa-r-Z8UU0aMwdX9HjgWSUglAS-nBPsXgv-ZWsoDU0As4sko9FkygPSiefXT_KVAJtrfO5tDXA2iuWYoYq7bnFAhvqEx55aDGdEt_jPjI2zWTIX3s2WSCHLJtnpDh4Zs41s9-LBU28XMdT7Njge3l66nOJvMjP-qb09e-EnH-pfJ4BI3MIenPp4qqE0fDItLpIgWVw1xTmyGUYkG8SIuvZ2cRPCEifpByxJblax6uxOfT-YzsIETQVa-_afIV3v9CBHO7ue7oVaaheIyZGzd0p5m1bzscO-AChd7N4OOXYAoxtTxmuDC7xI65HsMRW9e4d4zJlZL4fkpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=KEp0lvmjSa-r-Z8UU0aMwdX9HjgWSUglAS-nBPsXgv-ZWsoDU0As4sko9FkygPSiefXT_KVAJtrfO5tDXA2iuWYoYq7bnFAhvqEx55aDGdEt_jPjI2zWTIX3s2WSCHLJtnpDh4Zs41s9-LBU28XMdT7Njge3l66nOJvMjP-qb09e-EnH-pfJ4BI3MIenPp4qqE0fDItLpIgWVw1xTmyGUYkG8SIuvZ2cRPCEifpByxJblax6uxOfT-YzsIETQVa-_afIV3v9CBHO7ue7oVaaheIyZGzd0p5m1bzscO-AChd7N4OOXYAoxtTxmuDC7xI65HsMRW9e4d4zJlZL4fkpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQPSob1GMEpOCj2dKNhHkVuM1ELrgUfzEMimjT8UvbKMv-6P_xh-J4MgcGgsrTGK8NBnmExeSqTP8gHjhh7UIdkPi9DvEQwYcaqbWxukpHkiswq7c5m1bO6f_b8bmJZqxnSezAWcNEBi535d87PaTTFbqImk6Haiq5utrs8cyi_1zcHdrYw6YYwXwUbUsRfMDkVx08CC7WU_m01ZUgiW0F0OxseXrz6Bf18TanvflsLXoABGUKoj_QqqwPpy6sFqs5dE7j8hckzElzTA8ZtbNzFR3HzqQ8_gbPWGDAYuv_6odSLLhXzowHt7t2ZjkxPpXTZNdJxkIlGzu5iBTtQKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRI7rDMtKQtUwxGqSN3ne3zIC9LDBMiT6FF6kqap-joMO56jGHAtLxBoJ8RXUTnuoYr4n5ilMwqcMYcMOWCf2FvSSlvD8_j5Lcxg4mUMh3qXH6Xgl3szfbJ6gfR5uWj8X0NS6JkHwYUo_cJubVae6qJpxFwcOj5pRlQsa_HmbYXWD6RryjZV8vcUoW3k7m9guSPj82OY7q327fMV9FO69q5xuK5ac4at8KTtMIdeyDCQQ5qgWnHj9MNdJpxrwxNsq5RDjizOz1WeQzPVKEemokmAXZNRplJLt66lJi8tX50Ua95xRmvqNgiMMotwDpZxq_HA95koR_xHTlRlTpQw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=QNlXdKFo9qL3769PSW14HlwrnPeERT1477KxnvytFh-jDnMHwL-QTYj0PEJVZQcfMnv6h2S-3KTEi3YeZ_YKw93umiIKsXMst7SIjiNWQFAIGEJwgFSIWYwp1AZaFwkI-ZeIhrjkAJuHXWitPYP0UvI5-HK9thszXbBpH51A34RXrNMQhVLeqZSXBMgKQw-O6mDkswP48JTLlCBXmmR6AKs6AFkvXGo5MEshkodbmym08NcdT0yf23gpTRRkLiJbmPTkLDkaEYoADQTMftuX1OhkYPMY2hVM9U7O1zuNwSR6bdiYz9NpnDsyLWR0d_AyW-S9VseBixQFvVM-wALkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=QNlXdKFo9qL3769PSW14HlwrnPeERT1477KxnvytFh-jDnMHwL-QTYj0PEJVZQcfMnv6h2S-3KTEi3YeZ_YKw93umiIKsXMst7SIjiNWQFAIGEJwgFSIWYwp1AZaFwkI-ZeIhrjkAJuHXWitPYP0UvI5-HK9thszXbBpH51A34RXrNMQhVLeqZSXBMgKQw-O6mDkswP48JTLlCBXmmR6AKs6AFkvXGo5MEshkodbmym08NcdT0yf23gpTRRkLiJbmPTkLDkaEYoADQTMftuX1OhkYPMY2hVM9U7O1zuNwSR6bdiYz9NpnDsyLWR0d_AyW-S9VseBixQFvVM-wALkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=ImYjQqmwOXwrXsxmNS1K1SfJaXsWcSmj9ZyksKlRUj6Oybts3I1Se_DjyIXNr-qvmsU4A2cMwxHrW0ox-DZutHG_vdbqdnDiq8lmjptWTsJcp3MMMkA1FnztWbGHU70xjz2Bt7gtq80qfyWb24IG8rhnEJQQysExvr-30yHLnMCGbpX_h0RcEzBxT4_uHsl-12Nrvi6svjNAgDdHDYv3J3WolNGJHyPchtl3w6zcOXssbNwDgBloqvZeEL1WGfAczTBXFveKPqrJo2hIc-inAry8jrVaCAcMpCT6XxiSUOB2ksFaj-5_HRQH78V9iMD3aGgpyXxh571dAufhjvs7Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=ImYjQqmwOXwrXsxmNS1K1SfJaXsWcSmj9ZyksKlRUj6Oybts3I1Se_DjyIXNr-qvmsU4A2cMwxHrW0ox-DZutHG_vdbqdnDiq8lmjptWTsJcp3MMMkA1FnztWbGHU70xjz2Bt7gtq80qfyWb24IG8rhnEJQQysExvr-30yHLnMCGbpX_h0RcEzBxT4_uHsl-12Nrvi6svjNAgDdHDYv3J3WolNGJHyPchtl3w6zcOXssbNwDgBloqvZeEL1WGfAczTBXFveKPqrJo2hIc-inAry8jrVaCAcMpCT6XxiSUOB2ksFaj-5_HRQH78V9iMD3aGgpyXxh571dAufhjvs7Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzhHuXhKFJJWu3DR3nrfuMgOb6pjDpNR1P0XWmmH8qLs5UPf3DIzRK8yeMlgRsl_q0xNPZJ2pFBIrRhR1dBB-Qhh2MpDjB3QfvG98qFKApJ7idNZBaDXxr_UidPdiA3_ePE8HJkWI2UAGA6eR1sz_m78ODTZJa7MacZ-GpFy15yh77f1fLHnhf1qeq6upzAPEX7uNAgCzF_Ex792rq4Yt3OsKd8okh7y0S06vvvumkMIVsMMClXtmW-wOiJwRw7L_UimtJZjmQHjvdL2-rKIcj3q5cCblnGCK2BeevN3kpmwxnF01J8_Yrxf8rSHdBcnJyy_oc1fyLS4He5wP4uTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTWIHE47tpb3sVSv23FMiwrWzihaIBrngU7LVm6L9Jz6Eua7hqARzJkDClH3v9o-joAtPDo5spauXQa-HoizrMdjjUHDCtFXv_Hj_eiz2JZaKdyOu1e6rzLz7_lXT4__-flPogbDcJniIP1In_5K2C3qnVcOrK0Iwd0-d_Ehtfy9ZtLQLyOm_zsMk3reQULpj8duv28j0QmwSh9s-nQfMUBX9bPZdtaaGPPMTdqU-UHLNJ82DHaF9d03LfQJB-Mg2kCLa2jCURGKC9q7EV2CxZ6q3tG9Hb8kMHIxFqtvwAP_SGTGrTJGidN1qdIZ7Q2g-6AIttlm3fW-Out-oc2HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=OJ_TXsaTskFo-QlB17H_aWve1pkHVdZuwS-K_V4-YGwW5djcH-9mHsHaIuTLi3J-97MAwzIapWYZozr8eNpNUteCqrSuYp2zGgAZqJos1-scud1FkqIfu6iKdHB96QRm1ADKLkwy8h7PoAa38k5kd17akk3oqtDXQLu8uBNkDDpbrPabw0IBkpvJr47QLutiwAGcOgfFxOm7KmnFZ94aCsUE0orpB0RTctYctD2yeZwql1q9Bw49VFqx7c0BGZLaz7oHoLO50A4UJkOCtE9e73ud0DtmAH1wTb7-k1wfoIjW2ueI7jE0D0p3qaPWXdJERyC5ZDGbVwgNDJzbH_3_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=OJ_TXsaTskFo-QlB17H_aWve1pkHVdZuwS-K_V4-YGwW5djcH-9mHsHaIuTLi3J-97MAwzIapWYZozr8eNpNUteCqrSuYp2zGgAZqJos1-scud1FkqIfu6iKdHB96QRm1ADKLkwy8h7PoAa38k5kd17akk3oqtDXQLu8uBNkDDpbrPabw0IBkpvJr47QLutiwAGcOgfFxOm7KmnFZ94aCsUE0orpB0RTctYctD2yeZwql1q9Bw49VFqx7c0BGZLaz7oHoLO50A4UJkOCtE9e73ud0DtmAH1wTb7-k1wfoIjW2ueI7jE0D0p3qaPWXdJERyC5ZDGbVwgNDJzbH_3_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5m7Y6YGs5150WDqwoA-VckGiSL9FId5Ofl6ms-WAm4sQWM9JmHIClXEtlcont6mlF4GXjtsNlqI7BmXqL28KQYxMxHZnFfkjTyQ46wikqYOy83df9idX4j9oWZ4CSUYLZxsj31BJ_P43MvRBHbaXBvJ6OaQWrGKGmCMs9u9uNMqjoAzT2VS0u9nOKibSOZ0jIns3Z8hYjroCekyAsfhDFPu-4PQmAYJwMsrXyds6bt-FbcSFXCceyTiH4kwuM4HGmMroNwqVnt9hnWDIgBboGNkR75178Yk6Kmjpntg7w8gNdNQdsz1kaiVZcu93y8ahDDUkOD-FgAbZU812RGCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWGxEw9e6BcCPSpLLXcY8nNG8otFE0Hk9Zd7TR4w3tdkuqeV63Bto1xYBuPQRpf2TUFGjA5vJZ82y_pj9k247_43PNC6GD5Wfld7a02K3Z8I8lhrP1gRkf9uxI7_Rt6UXfo6NQG66cfz_Ugv56UXGJowoiOL-7WSIXgNdD9GzodeVZRzo4HL3d9r1RIdE7o5anfCOfu3gD7W-lpFLs8vw0bWio8HYV27Szc2YsYAVfPeYYGHzlq5f_Gz7g0LJgdtPqY6-RrrAPs2qwnpcroB7NnJ3C9mAtbZ7ywy2JReyvgQOpqYv9LW7rAf62i9Ef7blWCOyV5ZXzONzFwDmndkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc7L_RPHeb5OfVvwAoiVRo08ewSKu-dyN8oU348aU_XfhabtIGqDSR_pdRVK9JtAz0jGAv7ICp-oKizS9Yc9oUwej331XLUY_MzdxsoFGcFroszHnOZ5ofQr9s_1ipEJmqWkDNZUI0kJguGZFLAVF1gOSGQpfNTvpU4vMwPn5EEWpAOJ1D4o8HsNtjyGXUTYzUGnfSqIOjVaTWGr6OKKhRG9UgwrvG5ElO-Lkwk9hRxHEWQi4yl7z6I5CDYgE1DNKM-B3nw6uTTFSabCG4qlEiQefZ1BJSYtlGF4E_PmlmaUpQKut0S4mp0Q4DYB4Uor92q_tZQgV_ejqF-XFPeDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOzQJ-WzTiU1c43cZ3Tb70FHMVk1SXoAW1bilf_MWSi7-i7K9hWDSeDNqBzkv5l8MamVla2722NtMWaOVFc1WVc84ZNbWqtDNy0LcPv_h1U6885rUR50kde2UYNlW5BhemAuXM2V9wPOI5SGxlB-r2FWlGnbmRmZeZbmZe4awGNuAGcakhU2RvwBpK83EwNdNEtlYq7jbhxigTP7u7BcWWILZzGPEBFVmafrY1iJsBru1NtMQ4ICnXDdJa-IDHmlWutEI7eQzyLR5Jl16y1fFeogW9yKiBFX5Vd6GeE5jvo7zf0mnOQwBRByF1mepQCBCxdOLaBp_0x__QU3-YnaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=ljoFGf6cXIie9FUTtOcDqCzVGg7i1Lz0B8POFUmjl5xfXUQ-_SbePEWTAVejPXBOPisuv4SAmlXqrPMuSp0sjh-YeTl9bNP8aNcdpBuqIEj9bCfjUEItOBf6GNdlisEoBcWbJ7aZG7IWZTtfqSsQZxknSEDzHqfQdpJI8DzDPFJBqH2ZhVch9hRkevi_1uNB4TD0HI9kVWfE0cGi9OaE9pdEkIxbcWmlZg0io76fF9KY4fBDix4Aha1mwqaJxOEIVRQzjhmsP2uJIQ3ABpJt3J4IQAATKcbnzUOLpEm08MaEZkwLz3e9xSNUiPYnqzYgn2gYdprmh8OtGQxp77De7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=ljoFGf6cXIie9FUTtOcDqCzVGg7i1Lz0B8POFUmjl5xfXUQ-_SbePEWTAVejPXBOPisuv4SAmlXqrPMuSp0sjh-YeTl9bNP8aNcdpBuqIEj9bCfjUEItOBf6GNdlisEoBcWbJ7aZG7IWZTtfqSsQZxknSEDzHqfQdpJI8DzDPFJBqH2ZhVch9hRkevi_1uNB4TD0HI9kVWfE0cGi9OaE9pdEkIxbcWmlZg0io76fF9KY4fBDix4Aha1mwqaJxOEIVRQzjhmsP2uJIQ3ABpJt3J4IQAATKcbnzUOLpEm08MaEZkwLz3e9xSNUiPYnqzYgn2gYdprmh8OtGQxp77De7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7xGV62-UMEeTKu72lr39dNR_5gEN7Gk8_RD--quTQOWb8ozm8yyTEfNoHhYzwXoJxKGlxQSN3NGkwiw3aVk6WkJYtL_90iKS_fYTkueyPFciMXG_KATif5-tP2pDtFFUg0ygulySOyX805ap6kv4pJCq2H3msDUEubfGxjIYky5M6ONUoZgQYtrFHNlvALWVCtCCmF-68m888t3KppTJDwH2qXMKmYlFVgX8E49a_5u6eqtvOyx04KtwMCqoq0FeBiNzSjOmsc_VhIeDb3G04NZcYIJXSwLeACpzneXbIJzLibMqcGh9iTtVewX1Nh0yBjl6Xvb6PwsY5-xgIv85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzvc8X3qFtlsy8Wrih8qmom6T9auDXDCaFxMw4xFwCB7olbcipeQYRveQXw3e2GpOb9sIPIeVzNp4JVSsIn7eOlPCp9l0HE8P67RrXGxUPuiHAkz7leFRyb4bb2NLjUtHgOEzJORCvgMrFqWyRXNyhMXZnwa07dyPhx_19bdO7FzkZULZfLkUX9YaHVaAAb_VAx5auXalaJi3yESewm5SHIa5Hiic5MVPU4ZuFUzTxACyH0FhIP5KwBLTZo6YwbhMw5_jloi-6ocZVrTb7DdBMcyAdkacYoE6SdGvB4sDXDQHdbke-z5JjRmt7OGH77NB5V2YMXh-RK9I45gS8VqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=r7HAfoIP-vJmJ_66Tpc_AMlj1ur1_-f5hTTzccPaZf1e3mQ2h3X4BKG4GlNwEpMLe0IgHLvPW4rligE7RogYT6M14cVoDrxqWYz6faF5E_8dwt4hFb1n5Cbrir5Whe_NYw8sWIvnpFa2CytbKbVKTDfI0pSAYPsAxxcq5z4ETRLuG2d5s2XSqcDkhRAL01XcP7j57zKFh3EFrkpoviO2CjkKm3WwfMeualbAgA7uQ3EqJOM3qvXXwerwECMN7hbxwJ1WhwzEV6zXwD_9HGnNPwu-mvlFuMhkl4mdIV5n6blhwn3k7SNe_1W6EiER6hxA20oV4NwgUt_zyeXHvvjxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=r7HAfoIP-vJmJ_66Tpc_AMlj1ur1_-f5hTTzccPaZf1e3mQ2h3X4BKG4GlNwEpMLe0IgHLvPW4rligE7RogYT6M14cVoDrxqWYz6faF5E_8dwt4hFb1n5Cbrir5Whe_NYw8sWIvnpFa2CytbKbVKTDfI0pSAYPsAxxcq5z4ETRLuG2d5s2XSqcDkhRAL01XcP7j57zKFh3EFrkpoviO2CjkKm3WwfMeualbAgA7uQ3EqJOM3qvXXwerwECMN7hbxwJ1WhwzEV6zXwD_9HGnNPwu-mvlFuMhkl4mdIV5n6blhwn3k7SNe_1W6EiER6hxA20oV4NwgUt_zyeXHvvjxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
