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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 535K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfxP8gb1t-vA6Eah-xdhVtumuSv18iS7aiaj4EaxyvPFnBmj6hsOuHmcyIYdtKqDXQeSTOJ0wNwC31stTxLIeiYz2d2Hcawik5-RW4wizrYNYroWfj7IPDo4wJEIPsjJXauHVCwBlWr4LBAH_2XcNWKEp1CiYhAfD4ceaL9d9BeVHUnBDgp7fSOuh6qzgg4ezptuIS5jKPONFYrzTD0tjMgGO4blns7HZfGgaWqA3iohK1tHqhGK4m_gTLexZJZOAKA4FdDi-lBkPrVSGXhvkyrtmsSpodq_zx3viASj9npCeSaCYBAsCHCU0_FcdXN1bTvN-1VoqQ_yihMdr1ycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clueHMXRwImuQOT7jECUiS2sSI9KyajBws4zMzuOU7di_HH-zTfgV1VsNMegsGf71CVq2lGRN95e0c9dmq7_RGCxg6RvBKImR5JpMwKW3-cSSpsnFTecwn2fR_7LlfvZi7pgTzy3gt0ZHmsMUgvtNjvx4y3Kx6vfo4niPMe9UWb_DaLIAH2zjozplrNHHrgwZZtgr-iks7fA_COGUEL2ADoutHs8msj95dakRBgL08FsXJJhMttJNAKccJQ3rmlyw3UFNTxWQ5LH4e3gpw-NH3Mnt3tMQZ4VbDasH6xUyvDV1wk1wBEVoD5ZYDB-eWlwKBTHfcQJrR4axd1uAKrqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZk2dWg-5cR5S753TyFKFgrwh1sSjlX1UGvi63GZFkcvNy92DOoHaigoC_ay7M4_LMGH_4Nb4jKpU0nszgoJInh4OGOk0PcEEmniUuvoHWi3FLtIYzuS8XewzQTCbDw5WF84gLVvz1roGAjxzoZF9PTplVWfPB4H0H18-xZUrQb5ATPyXmrNvvAuGQSkMJt_YqokQXD0ZS_xaRhqwBZ5vnlqEUVibizDTm8Su6iGMLyhRF-ZHdKHhy6fMhxSRkixbO_j7-x7vYrr6jOSJ0zmlFXOHoXOk2T9dUHKJoPtniufH-F6YFvkYko2WWSZr3ZVQdEoE4zI18zEoQ4epvvzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVk1rew7ouBTwZkJHy2bdPCBeOd7wU4Se9eu95wc6dLuZk7lzD8Fo34DzmOrUWpArsTFBE7v5TOqy6eQVSCRUWgYVC8gUiliwecVkH7YjqEJObMlgJ6SYoNSca_yLlcptn2204WVCbbtozaUl4k4wkN2R8VznE8BFJCpjuT53_PRfLjnSqRxmNj4KItr44ikIvO9wCm4xTryzico5e7SX1KfCIBdNGC5jHS38va5o0bwqGWQhvKrgWvTH6OLMzo2OTGmvNHWQOLU5hts9SPDGjrulMriR_GM6n1VAZ20Vv8YUBcvjeOQsszlAku7612UbuZcKCd-m0LLNSAjqlJoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmaI17uaAk7T7jxuNTe-cegAhxTm9iCQL2hjrebPTMGtF-ihqiopGy0D0gy4Ree05S5QPSZQUHP6eyXtAtKMP3nt_dfznwjdMGzDhIha1dCHBhls_90GZ3ycQi_KhgibUwnba1Gdnb9gj-GXL_uI7M-r_udMTGpC1boWEScFYoHQ9xRGNMNkgmFAccR660-mwYStyoulgniEMeyosGAri-KyJsyWPPHhVlii9LqTDHuNrggLCXIuYAwCML-4GDz0W_ZV5on63AKKje1Vpl-7hE6Y6LOVJjZgvkJzpuzexJ6kAyvQj8stcIl6gGHWUYj3b2BvDO91k-og19aza23iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo7dPkxJHJExPnczQqFzZDSBXrlNZfvtHOB468fihtHcDVVgzb3lGDiEUaVZnq6LNPn8btUabfNCtJLc1zV5kbXpDpblqs0tr7tCUu9BxEGxuH3sar0gCET1s4rQCoVtrtvs_5pYrxnCWZL9xbMghTgk082eimqQzqb6lsnaEPC1w74PkkCeQVeLF7p4z9z_S4BHO0QBO318M9v3FR4dTOAvAzEwa1QWzgBxyYIP1975xV2RjTYdZxkCOaYc5EC2lBV-YI2jhcu1ZgmENmoS8dikFqD2IFbp-bVUFg2zy2P4SaofvbgCL6W8vt4c_JWdmhfKK9Z6V7wLpkHGAodQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMg_vVJY5hwsUHX2GQ5ThU_IOiB45O6h3WLg_CM8StWZsNGzT8MoQniCD8kKrFouOi2v1fU3BpfcCGxbZnFFs_TRzfn2NWEunMz8kW_CCstIl-GMPQBil2InKMJALXJmrnt4lB-i1lMWWFvPOsZGgTy5O0Spp77JGTx6_qSFyALfqN7APmWvrM8a76u7ngyvIjfezc8PS9DQOOjbIexknCu7YyNAUDnwAIa-cA6DETih5rXbXRXG8qAa7RMqmkQd6zxYeyAD0uKOVES4yPBnLusHRjAmmvQJ9nVcgeDkTZgFwO6nUAPZrCPswhC72voPmdHKdgMLtIck6wqgd6xXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2O9vEwDrGP7GHrc3hkkhvoau5uTr07Jykao-JgOJIz32i1mNaYOlzKDWaKnNnV7XPyaIxlm2X9iL4FtLbSWHJCcplPkUyqr2gkBcc9yWUrmV2bFr5KHX97f_e13JhdyN0u9muBQzCg1FTLRrKDE4YH2-R1spJMkVwibfFqhluQFLFtLLLIlgqZTe70FTXc6lvqmJV5LecuoNNisq00DKViultKY3JIbWSAjT2mSJ6V-DLgibyLHWmG_UaBwseku_ThPTvtqQloLUZFNqNrauuXfi62S5vGjScxYLTWbDyFuzJE6gZG58jfWfCLhZS4-NC2Tf69AB2YdQab9cKY7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-65pl8uMQ7Pv2FL5cjKJ_wtj3RPGru9vba4KGN4L1KYUyYLhkS5-K8tpwpNXIBNffStJiYYrO1xcetrMxb4IREuGZ5AXVUOmCUFybuspohEPNpiEdvPZ4lvum7wKRjiy9_NhybRaP0QOY8xH0Utk5QWcsowOjlyJhxKooRnzgXv_Alh7HPaYccPvFkKaSOB-3pS0OvpkQzpdALIKX-ifghmdsLwI24mautfnZ7Ulfc81lihmvt_gXYfmYIHIcr7P2PU0H0StqniNt551d-rrpXcx7GLbOn9QPSUTPbDwssCXNPQtCAsiZuNH_hismHkjM4JTVemH70f4Q9dz3kTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb93Z-bbGx1HOMtozJkZvjATUBSxmCp2Co267nspnyTGYAdfqTRIAH7tYszWRCRmlVn3a4-bUu2l4Bqzvu7mFCMgKc_0wCZZmHkTlVG51y4rI225dJ5MQ5Lr0FEDcsHDiQc4wH_J9hcv6NgNvRuIgCL5aUOqKxMLvzhglMk4YG5sbY8L-dKb_T-GbfLO1qlqU-4H5BHHYTgSYSxw_wGXLuiHfG85qj8cO8pfBy1LRrgH9njFavw6gdSZicGKO1hOEb4HJxoY8GBYj-KtbRRUGbzSGficbdPp2TWP32ho695cYfB5wX89v1xIKfeWUBexlmCnN0_e0MWsMnhloNVc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHbBrssoWVhhv6D8mW2QBTXGD1IxPE6i6SteKmfB6uvw8j6RLOdqUycw53dP8o3WUJPMvqVTr2gcZpze4ASgeScfiudsLc60RC2bGggXy5jfgS8MZf_qjgIdbwatzepF1QPiSVP64jW1YqzizISiPJQ8X3A-yzpoTdWAql-bN9u8A2cqhPyEq3sfjh4A9MlusdTFehXdfYaWva2AFr9zJDeQTUFvYnQj-4wI_wuZn5QdLl2PMKspM3vvNe5Zf-a_EeD0XKwL5v6QNmzi3LXQGrOG2h_tudomOneErhzG-6G2EXYPiGxF1kYnUuS06sJlAPKw0KS3VFYb0Bh5ZKwHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcnpPsBeyiSsZ_YcUnn9ypIs3vLD5UYgIysqc7fRwIAEZWBYg0LI2AvS6hF2RcoT0a39PeB-X5PwxVYLO3bWcHI4ZNPfMnI34H0jaxQW4ZntfMWKS_NWyLwbkNmEbcKvZSOYlrtnNB5JhYan2OdfEYSct8QhKba29xifUCsvuV-FP4Uie3d4FIbuuiTW6aTklk9IWhkxhCUYtGJHklOonL8uNeYP0MKZu-Z8NUFpudtXWSg2RMi4Nr1tnB3W8Q3wfoTmkaMBqNaY4Z-kSOvwayS59-52wEJEB6pWsgk-hWQ-BtHb5SSPxKRdCYwdTMZmHos5mEYNw0eHDLjA4kbMQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHraIypG60UJV2mma5PX3YfTxmv1Yzl5dPsMkekACW9KM7qa5xymIuaNX5Q0zVQVzY9RFNZKjyC59hKj9wK0to_QNGDoN6g3ubqKLPxi7-BPI0jc5cWDRkNDiyXOxdhrSqDXq8lvw0QxxpEu9nTyndlvBJAE1Hou8zyCzveX5BTm_iA4i1D0993mmd5031qQ7276IGuP4SRC8LFzjM_cjxXGqWm6rcknqU3NWT0ep2ef1kdfJ8xAbtB3DsTVTq4DTQMapwR_OPL8va5VeE_lkmmnFCm7DEpVKYnHuofMAyvl9Psx-uHg6tQKeNg2KJoNeT5i1fvxr9w1m96cINNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tza--ZDT7lsGycKmWj76pHW-r6zVrBT-yUri5yHWzmAkd5rOr6LC0-Amu6VQjXdS5MloYRJI4pCe61fhfWrpaZjTp5HJWnCfFINqDaImJgdwEoswGl69zx2pQdqsmDKteZN9eO6B6b6COkLBZ1Bvf-1M325biuTkPCG6dpoJJ2ledfx28bhiDfykeKXSs-HPSDMu7zLRaRG2jcT0ZRHUl1SNHbOXMuLZpFxXEzqj9RldzGkVzkldOHQN56VIzVuFXSW-7FCBPv1tnWazcFM8OPbT8jEJ1JqIePfvLTC9VV-h5FskZP0R4Gf5bd3SAlBdz4_IQO7WaIoURNcQ2Jn-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9pUUYzLjbmvmi1lROAuExOMgaGZQh2AY92G_wIS05QIyuM9GoqWI-iOfS5-kKn9zXDVmkmYGFKnwxq1XchGB_89s2YczGuA4roRLy7r5bcXrXLQ3LJbf5ATw8Xc7iERjdboKnzF7n3q3LIQgAVb-GbMZnfzvBCsdbNO04-_WNDewAmj4fGaYcMtAoeyNQCjBDc8McLtIaWWbBXy6fKyQZA_1C_I0vsg5aSqugygYr0VlXKFEFf7TdT8dG1od8uSQR6ibxUoJ2BUHvddt901CAslI0o60K7fZmbMNSOYiMjWJDQoFfQ2jXPAIInBVTIdSv4s0DDZKOo1C6BegSkaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfJKT4oWPWDhcGNh_HSkfM4bp7k-26v2gvjP87CB5RXgPKXOBaKYvY05PfZOwmWFon58lx-qOU1h0JTeAR-WwHl4t588iTd3lGStWqjSg-vyNwsl9382l0eY-edZF_5I2mzC-DEF8c3fumY6PKf8DBzfb1P9Xipd4RWtExzMNH4LQAjvhsH0Xdu4LiUFZ0xAwR62RAZVHu8HJNfbYgO5C60KBSTayecgL0st5vXF2vXVJdMfMS9rHKvxnFR3MnJB0m-krEBD4JctfeX1W6KbrUOOjy088BcVXq27bOznyTy6YPf6fcBzd15H-EWFoSKhY6U_eXG_uafaXMd4N3Bd_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh9hyEzZoK6DkU7uHnmPqwZzzAJso8ujWYOCkchSzmfB69heDk3IHzZyglZJGC7iAR3e7TLlWUmTKREou48wqWqhT5QNkBr1-faMi6OtVaThMhRwez-hS4gOvckSQJ-imzFzfaCJGCwZlHR83U7Ku8FFmJvf4Uk2AtK2fyzkH0FzbBXWmQ27E2mwzPVImbFr7VxJxQP7Y-dWyirO1cuLuZa6BWkZbgJu1QBLg9y4113OQQMckKu7KVtv6UtvRozc2z2I92oP0ol0J64CQv5QwGXQo0nEyDJzBNqBgjfqpd5icg-M8O08cKAvLGAoIucaMh3VY7xXtWHxSHQLCDSeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8GSJojYmHbaxpDqdpujhSn960MEKzhlXkP8MGApwFpaJj6rHY5U_JsXevMzHO9YRGGI_8o-1qVJ7iEquHxWEVKF0vtQK9CkL-37jvtDphnIDdwqaeE1nHj1nL1yAJO61R9RfJKpBA9Ou_STFqyTH_D0897IDDENxRVCuJwiflwyOJjybjwZYaq0xkihOIYomtNLnCMtCnfuf0iE_kOevfG_XO7vvgHxATn4u0e6OWuV_bZqxtCOJH1aAVoOHc-brPVvrp5UhQ_glt9lETzBtEQp7uUccpj6qG5LfGRg2aj6zon4U_JU-EcT3rx1ph76jo5eT5jmjZ0gRRyOmF34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-lNsM-Adkjw7M_a2P90yrWe8aAa5GFPPW7NP3kn-bN4eiYDGj0RRArpZy_WCHOXTmNWrLH5qXDO7x9EWxbvQC_w7enDvXquxuKeh0t9-wWRSKm1FqRdVVDlS-Z8C6sH3hUyA-irrFadfdoOqlUSpn-OWRL83FqxNyyZ3pRVnt_9aOfosw6ktJTm3yUuSc5HBl-1rNySaGf7UKNMdRvNRUFANhtG6Wjt7KXcDJRBcE0OeMZ6Ig2DFwqnm9O7r-uIXzlVpqCTKlv3xAa6eUSsKL0QuGFFzNYqo6LeoCGos0P3KKE-c9z1-c14YBf_E8XI9S42hiFdBg_ZtaISf30H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJffoNMyL9gwqHSZRp-5EfYkv7Ci4geB_4ser8aXrsJk2MGWY88zcad_9eWx3QtZTu4gb3IRN0jJNW8fSIBi6Zd-l2oGEBRSU-JmEab2H2oEVzLe_WTMRxcbF5B_RPw_dImuK2N4wi9cNRI1j8-MKz_zxOjaqp_mWW_E89Xc6rERWEDby59MW4vDZO0FmMi9yRhz2OEOqwWeG-_NuE0CM7-sLGJ08NxstlEPoqx4yjRU69gaUTk-O2Pg0iSrpnxzZEpJAyLN_zVzq37gFFnmUOaiMgNbozuO4GczIyyV-kGhvLOHMVBrI0hjswnfIHg7JDhi0dlovsgwsyBoh5rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbiCkPrT29di3jZuclRDvyiwRA0_9CHenN3InJ6uaJAQepUdm_96fxuy-bsag5mdcG5Pc15UpmnZtxmgyAegrJv9PbO3K3gpB1UUnKs6OeoM5DDfmI5CYV1HdNvgZwxsruTHvdMYnsYSz80RAhK7tR58X0jlhcKDNNnPMYFwrbYmxvxtcN4dnklRGvbNmZZXtP9VlX-Mu1f6LFzOI6wc278OwODaTm7DIC7jK6Lu7Jhjacu6dQNp2HFQO4py4azppnqei9uiU_MqOesbpLiNPlIeFUGgM4ySFbKU4jumDHZIStWARaEix7xoFb1W9Z6TlgbYf-Aa62lPt72v5pa7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeTqv4FXr31EsCdi8KcfP_MOaBhZe51Rftq9GLaUD2kdDBpwzV-35YL_DQxlGOWxpmOTrrS0GZ-zhmGDcAhPeify79h9sfllU9okoG7i4iJDhKY0fZ6jDriv9klxxtvQiJYh35k1NrdvzzXAQdZH7gIoPGyJUEZJ_VQrKE2XgV2Kgk2Awo4DMdtGuXF8A7bl1cMrVyrHpLXQxl43vFQX02fkdCMf5P7CZ2eV2afuI9b0PFbpbu9hB0RuzKlQ9_gHPeEopCvsO2RpeK3QMVVmaGZNzv8IKHQKBd23JcmU-Ti3KIiIk00VRDBW_JJIPJWRF5jt2QLJxIGaX0M6hczN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppM2Lnhl3CEtjq8VdrmBzYXigAeCEDzfM7cGakzXO9lX4q92aVE63LPiVs5QclSrkVnqR6NBkwWDIZ6vW58bxEMYasODJ8_NLR9EdJJofDW_2genE13KM7OQdleou8d6k36G5U_SDoxk_IT6olFDU5GOscAUvaKxOYjx2YK61H0MWtUW5pLcDiphoO1AfZw0LHvprzfM1aIot8vyrLcOZBW5r6S_FqD8tJ6yJ0YZPMMga__1YRwl58MgIx0PPqGJeGV-qIJ43qzTZVF0aNhmwP4B3qz1Z1Zu6DZ82-cEli2I9CYjbbCbJSUeReUDB1B7fkL9eaMLs0XU9d9mtFF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLXiaX1BU7BxXFeqPwbs-Eankxn4fcER_1ASlQOvLZw5Y4j6KvgW81dtuPpM1Fk89tC69Kzesn2LnfMEm3psmsSm87fFURy5YE1Kv3h0hrgHU6rqeL9v71Kf86l6tQto7Zf3KyQRhOkfW_edD0PmgI-ObDm9UGYYKc7htVZGLLeNx5f9YPe7QI_neSo5ZPjSVxIjVMIsuKeV39w_iMHCAycXgd1pc29MZ1SiqYWzMid_e0yXSF0-9lZbdTEwU_pGcniUlAu4ONdGZxQOuYThNtrsndD_RlSBmAnFK7oxnz81c6Z37kkffQQ39ZqneY8z_KZhuXriVKVOu8AW4BujmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=rlTzCR7UhMECd3gH8uzIHuTGeG_mI-u5JHwnINyTJi8OJK4WGyIjEtQkOqDvU0a1y1kZD878b5zfwfQrqH_kjdGrmJjlaXZLtkyb5qZ7Iu81l4rX4NxQ7Deg3Pb2Y-3uX74_ydTP2RFe0kLaxU1EoeKfUYeSrow8-G6QxvyzybVjfQpaC2HpWCq98Gmtq1bnLg2koDdq99njllgas6M0QGLsndfLAKC1HACkgqJLfl4Ujlt5qeRLb4xapfkSI2SinftVm2xmhT_x7H_MAz_8MQ7T3DPS6I2VGu1xaGHScx2tkze_dSwYAguww8Def7SV8VQ8aZYDYrZCjfdDsfaXNi5KcBo7fSv5SdHLcOCBE-C2CFQkwRXdS5G-glCFAorSEuI6vujVnmcohgBn5mjiNHMcGzM0kZwNrwl3oOBzgjR12QFAYFyoe92YJvC5-nuoHY0r0gHba-hUQyrwlPhTDvD1TWoX9c0h-6ae92SLMmTcgKS2H1rym8m2uQ4lOE_L9P-cHrinFz4phqhp8y_xcEdxfl5JbYfyuovoOsJGF0ox3KFo3a-6aWMEyOZ6r_i3J8Y1fXKVpQYr2FXnc1lX5A_Wu3daNk-UeIf3D7-OG8ANZgFl7fLhpTg2rdF0TJ77L7IarFKMmsNk5i9Lh1jjnqVTPErvC_N7OkrmiOB8Iqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=rlTzCR7UhMECd3gH8uzIHuTGeG_mI-u5JHwnINyTJi8OJK4WGyIjEtQkOqDvU0a1y1kZD878b5zfwfQrqH_kjdGrmJjlaXZLtkyb5qZ7Iu81l4rX4NxQ7Deg3Pb2Y-3uX74_ydTP2RFe0kLaxU1EoeKfUYeSrow8-G6QxvyzybVjfQpaC2HpWCq98Gmtq1bnLg2koDdq99njllgas6M0QGLsndfLAKC1HACkgqJLfl4Ujlt5qeRLb4xapfkSI2SinftVm2xmhT_x7H_MAz_8MQ7T3DPS6I2VGu1xaGHScx2tkze_dSwYAguww8Def7SV8VQ8aZYDYrZCjfdDsfaXNi5KcBo7fSv5SdHLcOCBE-C2CFQkwRXdS5G-glCFAorSEuI6vujVnmcohgBn5mjiNHMcGzM0kZwNrwl3oOBzgjR12QFAYFyoe92YJvC5-nuoHY0r0gHba-hUQyrwlPhTDvD1TWoX9c0h-6ae92SLMmTcgKS2H1rym8m2uQ4lOE_L9P-cHrinFz4phqhp8y_xcEdxfl5JbYfyuovoOsJGF0ox3KFo3a-6aWMEyOZ6r_i3J8Y1fXKVpQYr2FXnc1lX5A_Wu3daNk-UeIf3D7-OG8ANZgFl7fLhpTg2rdF0TJ77L7IarFKMmsNk5i9Lh1jjnqVTPErvC_N7OkrmiOB8Iqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=TbxuxGswDF46rMJh7mEyqbozzZyEE7-6zC6AuyLMdeSvasMFmVJdatbgckO_i-7oyKlajtFcgWLqpS6uib-O2yK8mD7GRw98_FAkXLA1Sk0kXXdjeme4Rw3F_LhsrmDzBdB_4liPD7FwRE5r4SNqpA1B76BpGP94u1zW3GV8W2p-5NDvTQ04_7HB_GPpS1AWDGCHasbRCMbCrVcCzmkgl05Sc045YDNAerB6-9yLrvsF5U9hmtR64aA7fWfaZlR5mDSsirakf0vF6-f2e517s3cb9dgGFpaclHkT59yy6opmzWx98MQlvBR5xB0O6wR6qVhzQJN4aJNkgTiPeG_dXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=TbxuxGswDF46rMJh7mEyqbozzZyEE7-6zC6AuyLMdeSvasMFmVJdatbgckO_i-7oyKlajtFcgWLqpS6uib-O2yK8mD7GRw98_FAkXLA1Sk0kXXdjeme4Rw3F_LhsrmDzBdB_4liPD7FwRE5r4SNqpA1B76BpGP94u1zW3GV8W2p-5NDvTQ04_7HB_GPpS1AWDGCHasbRCMbCrVcCzmkgl05Sc045YDNAerB6-9yLrvsF5U9hmtR64aA7fWfaZlR5mDSsirakf0vF6-f2e517s3cb9dgGFpaclHkT59yy6opmzWx98MQlvBR5xB0O6wR6qVhzQJN4aJNkgTiPeG_dXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=uY29yekSXdXRx0Fn-ENSV2kOONr4MJYAMbkFbh15K9Rn0EM4AtxEFqI46mcTeeiEtxBHNqPu7xG6GuWjjupEdiihchVhVxys54HV2SvAyS3n9FnmPsArhWntRLkTRVy5pP7Z-iAG_wDYgrCvMovzDsBs9p5ov4D9hLBriVnpqyTdVtYHfaYf8vwyFlA2qT8HgiLA-USoRPL-leTMuhwJpVORmV_mrM_IgDI95461OryjeNsO8tiJsw-lKntcwUOXDBiWw360TJkaf-B-vNk9DNrd4Uw9aIfwdH9YwzeKHVZM9VlV1Ky3TJLrCt3AA90iViNnwcBLBM3lA2gQZ2N6Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=uY29yekSXdXRx0Fn-ENSV2kOONr4MJYAMbkFbh15K9Rn0EM4AtxEFqI46mcTeeiEtxBHNqPu7xG6GuWjjupEdiihchVhVxys54HV2SvAyS3n9FnmPsArhWntRLkTRVy5pP7Z-iAG_wDYgrCvMovzDsBs9p5ov4D9hLBriVnpqyTdVtYHfaYf8vwyFlA2qT8HgiLA-USoRPL-leTMuhwJpVORmV_mrM_IgDI95461OryjeNsO8tiJsw-lKntcwUOXDBiWw360TJkaf-B-vNk9DNrd4Uw9aIfwdH9YwzeKHVZM9VlV1Ky3TJLrCt3AA90iViNnwcBLBM3lA2gQZ2N6Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nly9Avq5v9FsnA4Elf1Y8FKcehk7RYvHTiGUxptXMX3w8ZPVNoRTeR_bjTYXGboqyzhNxdXkdPk59B2gPY7d_yLyJUHFOJDwxg4GfSuAkmphuAa3j0h6IKqOcXHUTcJSfvXA0DMVUPTWMqPwke-5YyMcmWaplKonweZQ9ysbeOzjCoV2HFDdXkCeSL64-0TYwwmLO61Jhc-YfaY2s4cwoUaThzYbeOrF7-fQmw-88takHHndKmou1lnadEocLv84tN67WCPXRNCm3besw6NyQaOB3llWeRE-dZn0X1cbmDfjelG7bHdfBmHnRVcOsxF39nSaR9nBn1W970zHPcOJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-3UMVyStN9IGXzen1pU8EpOItprcTLIobfmouYaQkNs8ZzCoWICwlFNYF9uwIA-em_eKG3JSw2Rv-bjgxuAixAqD0A9lBMyPzomiW_MluymY6krOHuelBbAoCll9s-e3kxuuSA-TX78cRWl5RqV5abUkOxGVxVx-ySsy6acEdC9NmDEj58i8ClUyC24ghJsG4rBT0SNVOuW1yHkEzmDGZPvX1_XQh0opvAlO5meST2i90SPUnWQUqf00PWo67Rv4SWyPBGwIWWPa9lHy8Y6T803Hvtgsuv9zRKV8nJlGDDbdrn4X99kp80AZJQ1_ojpt6vTrzWs7Hm4u4ABK8PA7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS5kgn9ApiyCpk6Lf0EFuQPZagyTwnScgNffoLKGvPkHk4RldvC3WaBbyz9ZuwPnej2Wf_BWhx70whw0Cl4Pg4MeGzHOMzZdI7CkkoQ4x_ZxEwSHkrJpSsH9Mrg7hdtstanQ1fdEQS1x9h_o1GVL4buVehS1myMvKu_u4pboJ_8cNyXSmQj2yaX6hficX7amMkMSa-K3uhxh6cnvgc7NsRX8K2kmWcVDHdJtIOSNfoHqnmAOH9aQDB3Wi_e9exAd_0-2WMOBmzdXCACVxh0eW8U65QysnlzLi5MzrQWKURJsKZMwBc1ePaucf7W-S6YE8hV6X8Z82pSbfi1QhebpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnlsVOgAEhfzS-6zV5EoCeX7jIIMCKonQVmfYKRkb-brKOSTJlKbetExtmYVbKshHZl6ylb_QEJ8OFMeh5o3FSiRPg7UWc5RASda6Bzvq9xTpa6qn-1ckUUFqF2SaVg_MjrhiS4k0aAsjCSN5dAQwSQ3M2dZZZRhAXUhO1CzOnipUXpylWbKE3Pv3njObJgCm9KpQp6EZykkq4TrAHZbkucseIu0kF6Q9eSBvYtXjSgIKc3ByAl_xDjVj0rUbSxsdDFqlDIxCANhCNvjlnlM1vQdQSx08ETt3ArNTnyh7ehTnxNAeewCUS0ehs0DWVP88o1qTjzc0dFtZuonk7dEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/octddM0hblzRKu2CBc1B9WVNjbADCSjKr6wBrCFngNckoARs8afmwcLuif8FburasyqKXFGBmE7vgWqxf1tdHl0tpKd3SfTCz9Davzhi9XiQOwwRIBbXZf6sDRrVYHICAzZqZKXuZeqwA9fNgAjzzVhl5STPO1I0bhdxXXZIp_q-30MvOhl6cI8Sf3Tv60a5zlAv3rcCd5fO2Fch-SvU_dUlL1IqEJ8z4n8kpdhAvC2JYYOjdMNHQmyf1oS-TuTb2FBu-RYMv6bfn37zwndaR9Ud6ykez2pK8B1bKN7hcIje5uuLn4baqnMqPr9omKvR8NC7Om-_2COqynd7D--nHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzsMs502RsvgSHY9wWGUIV_8_VUOcPkFn2ttRuMHNbAPKWiVrCyXWVmHyc-Hl8UvzYp0cIy__jtk7z1Hw8TS73dSYFXBp3nisChVeYYWb5eTbbl-IwGxE_yBiqn9OQc4tw2VCuF5tDGFyeQm2caCOIuHl1URs1USa0E4O8HdWnvfIu9yn39cl0wYEpj6cBCRdMT3Qtjciq8QSq-cQPGY6ZgH48lrZAshSLroD3gPzw6eM4asL5Tvpco-S04n0PdEn3-9hiD7u5nGfp_cxPjY-R1mBFrvPy5tCvmTXJvqLlKUN16wX7bOOIVlbbx6oFN5fAKECvEhHQdhMDuRDpP3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_LkXG9ytsMofTrPCj8bv5AOXjpWaiJsZWScK2G1GUZZOkSj-LuMhHLUD9feiTF4GNtn4ODG0Tu6HmBh7PP7ouBiL1x5Xyh_WKHk16tDFdLzORSmVMVIgHQ_OryECeoqg5G1XQxAZOoWV8GvFLoGx1IfqWhusYSsL3NxKJTq9PO_3rnrYRTm0RqcLLt4MuYxlJOeQ9qIWFwfkxxvH-m2PWpYpLmFOT6Stor3-DJ6zD6BybH9GL5ymhmf_wUgSu2FoLo2zZunHW0aufCMWmoH266tkpeeejI9T1TtYSVeJmrU5kMRyKXj2AtMorSe2EcZ9fBsfMv_2-7MGXX_svSUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixZ_8M4tMb2p3gny5Y4lC0rycqtgJKHLQrTVetrcLJ6iLMuOvVrH-uweLJv29XWdvi8JGkO6nGg9vHYncSMxnJVaq9CHry8wKhbHgVmjD6zCYEKHYCBKz3AZBNGOY3EQJTP-ymI9XAIC8iYKbdFhFrZ2W1jircMx7r5k-Lz3NLrqQuxkssg7nWHtH55pYfQe19tRoeTSDOk_Swh9EsaSARjHmTSkuhyXIX6MR3B1a7TAqPZCh_TkyAlEZXqI4hpQHyH1X7RJzB5PByMxPDGurMpbtwmq8myXB0DqDkP-d0mWZBQ7UQRQlQ3VRKszqJB29NADQ252RB6JQyMocTxYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=pCV1D_gCwMxREqNJh0hUS5r2GkUtqFAKKxgJkPOTxoz2NnVHvjH19WUDYAcry8U44peMypLhhv_ZtdWo-iN6TRsCtg46_q0bpLrYMGo7sPRYhADTUmUmpx62cUp3dVTp5qdx34LVK8vGG4DfZmU4Dtzk6M-0Gw3cYsuA3wUfMT11FoJuPDd8iGgHTn9JXcJm_uKB9CdSSeyBdOtcK6NZhaBN2ECWHCySHxDltUS8ySOpQsHxauqof0UBdAgKYZAyFRN4sGrw4yL-m-ZVauKM1yFsOuLXzvl_u4WDPWIoigDibJ8eOWI_mmY7x3auvyhbv_Lxkb6ooZ2Ve_5F1CXoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=pCV1D_gCwMxREqNJh0hUS5r2GkUtqFAKKxgJkPOTxoz2NnVHvjH19WUDYAcry8U44peMypLhhv_ZtdWo-iN6TRsCtg46_q0bpLrYMGo7sPRYhADTUmUmpx62cUp3dVTp5qdx34LVK8vGG4DfZmU4Dtzk6M-0Gw3cYsuA3wUfMT11FoJuPDd8iGgHTn9JXcJm_uKB9CdSSeyBdOtcK6NZhaBN2ECWHCySHxDltUS8ySOpQsHxauqof0UBdAgKYZAyFRN4sGrw4yL-m-ZVauKM1yFsOuLXzvl_u4WDPWIoigDibJ8eOWI_mmY7x3auvyhbv_Lxkb6ooZ2Ve_5F1CXoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=Yvwqch9kApchezOHxyUpzqaCSuq-vhdE7wT7BRMTJNuVeFW6GZ6uqcEQYUkTsnzQo2ucrmeTwCUqxqzRdsO27t2nLt0oTG2BvoCCisxFrgeF1QkktzAYKNYqKW46A_nv1Fl3_5xM0nQXjEcH7Cnj_NjduK-y0t9IVvVaaJKHo-lxtw7EaTt3jrBQgIZHqC580RrAngF_Ib3IQ-4YSvGWcxH5RRnIuiNYT7YnN1SrrQ5cAvoDlnk6wruVEfPBFKxnM5GVIBUnwYPSiQjex4AieK7PbE3ymIVYLu2N7O3wWpCGGACnluZOjq6xGwPonMQBoY8oDnBYfC7tVNZPwzVYoXSOb8gFyPYf-RFA1t2B_m1Vv7-YMvs2FrhsGtjAhN-YilAePO1PplrM3g5do14ATx6w_AyO6ESNSNw7aOOosoTYwHfzIoLwDACJrRvAPJvW9H7lIFUfgaBui7mHf1FliSEstswLQNmsf8vMajmr45TMslNzHrQpnu7TbBm8UZWjgwGHG80b_zvqUFEj-NaEmJcZzRrPSDXM4Ssv7WEbdY0hiiLW1KlhKI7LcZX-P59WHcIXYyJq3lWIZQ0VVCGDhu32CZisRxZIRUfsT97qfaSck6RqtNJUAxlh8lQsBZ26axQuBeAbtmjChlfcs-zFi3Bg0KH3ONtNlMcsbGfqK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=Yvwqch9kApchezOHxyUpzqaCSuq-vhdE7wT7BRMTJNuVeFW6GZ6uqcEQYUkTsnzQo2ucrmeTwCUqxqzRdsO27t2nLt0oTG2BvoCCisxFrgeF1QkktzAYKNYqKW46A_nv1Fl3_5xM0nQXjEcH7Cnj_NjduK-y0t9IVvVaaJKHo-lxtw7EaTt3jrBQgIZHqC580RrAngF_Ib3IQ-4YSvGWcxH5RRnIuiNYT7YnN1SrrQ5cAvoDlnk6wruVEfPBFKxnM5GVIBUnwYPSiQjex4AieK7PbE3ymIVYLu2N7O3wWpCGGACnluZOjq6xGwPonMQBoY8oDnBYfC7tVNZPwzVYoXSOb8gFyPYf-RFA1t2B_m1Vv7-YMvs2FrhsGtjAhN-YilAePO1PplrM3g5do14ATx6w_AyO6ESNSNw7aOOosoTYwHfzIoLwDACJrRvAPJvW9H7lIFUfgaBui7mHf1FliSEstswLQNmsf8vMajmr45TMslNzHrQpnu7TbBm8UZWjgwGHG80b_zvqUFEj-NaEmJcZzRrPSDXM4Ssv7WEbdY0hiiLW1KlhKI7LcZX-P59WHcIXYyJq3lWIZQ0VVCGDhu32CZisRxZIRUfsT97qfaSck6RqtNJUAxlh8lQsBZ26axQuBeAbtmjChlfcs-zFi3Bg0KH3ONtNlMcsbGfqK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=KGWwA2wECQO9qhccg2fk-2rED-gBRRiGenr2qBPj-0ExUGjJ0F_5X-H3MpOHuX3mx1WxNg2sQ5wIIbapio8SQcoU-Gukyd987_BhajXNgIAeyWwpTUfdYQcbUewILZ_VAJNEhLCrruGB45mZgkm8eXIMT-39GX1WcEPVnwIfhotztOzGa6f3XNU5My3MWffv9dAxT-tzIwbJD002WSKZLXMbqpz64K15hN6tHShmmwe6UVbxpXvS60MC7d9EER-MBGW8xfvYD_xfTMs4ENhbe3o3Rf-IUCTYAtnSFQK6bTFl976E2XjhHSKDelOwffJD8FVrKoEgXzpHho8h2Ox_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=KGWwA2wECQO9qhccg2fk-2rED-gBRRiGenr2qBPj-0ExUGjJ0F_5X-H3MpOHuX3mx1WxNg2sQ5wIIbapio8SQcoU-Gukyd987_BhajXNgIAeyWwpTUfdYQcbUewILZ_VAJNEhLCrruGB45mZgkm8eXIMT-39GX1WcEPVnwIfhotztOzGa6f3XNU5My3MWffv9dAxT-tzIwbJD002WSKZLXMbqpz64K15hN6tHShmmwe6UVbxpXvS60MC7d9EER-MBGW8xfvYD_xfTMs4ENhbe3o3Rf-IUCTYAtnSFQK6bTFl976E2XjhHSKDelOwffJD8FVrKoEgXzpHho8h2Ox_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=gBicIgG9pm3x-tJ2RIxULra8k9cKIpiYOscY-jYVCUcxmBpJzR7zg0-36N8OuyB2eCEpkp0tR3z5GkbFmIhFZnWbXV-EZ-EY4jsQM6aulBDL30RULLBpfZSy7zaGcxk2LE6VekO_R_L_qdR_IOB5-1Czub-QUhXw6L93gC6aLmlB-0LPXS1-3fm-ybfyi-tknRgFADnEAISos3Wo05aQK9xRQUjB78Pjm8t0HEy95LP8dN4B_31oEi_yy918YLbmnrcVKs7saCxtsW3heWYx2yb37TRMrZI-y2WQ8Kf-8dJCcNs4ifMS6KFXHgcA-lTfujk_exgbu2xu3cew5BnnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=gBicIgG9pm3x-tJ2RIxULra8k9cKIpiYOscY-jYVCUcxmBpJzR7zg0-36N8OuyB2eCEpkp0tR3z5GkbFmIhFZnWbXV-EZ-EY4jsQM6aulBDL30RULLBpfZSy7zaGcxk2LE6VekO_R_L_qdR_IOB5-1Czub-QUhXw6L93gC6aLmlB-0LPXS1-3fm-ybfyi-tknRgFADnEAISos3Wo05aQK9xRQUjB78Pjm8t0HEy95LP8dN4B_31oEi_yy918YLbmnrcVKs7saCxtsW3heWYx2yb37TRMrZI-y2WQ8Kf-8dJCcNs4ifMS6KFXHgcA-lTfujk_exgbu2xu3cew5BnnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSF1k0sK8vl9cJPysRE0auE5m_y3cmTTFdUbvdDxPRATu5btp0T5sYFf6cD4wpWc-Dx4uYNG6x_usMMHYbQU6d2ZEo3k4NcO4BJMW70ac-GZEDxy2dyJFQsrLIr-WfwzL1Q8ADyquGuNVfEcWVgToRM1meSxIgwvpqH92SI6MOIqc7wMHfDNgvrosUvdfpQYOpa9jAkiywk0wmnS1ORgwzw7OSQgLgXiYFERx30ATmxyTIqd5nUAASsMEWGvgtbL9xcbgwEx_Sx_kAgsuih6UtloYYtCedNXANZp78KPY0PxLAZhgv49pdI9HiPXF4iKMPMDLTFITmdftknqWJZBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=I8-CrFUO66bkI_t0GWDdGWEzj5-BALcsf9E7Inkl7L5qil1bBtRMjBvFwFpEODHA88WZOE1FmTduj-XzLtzv7yozSnV-FG2zZkSparXeqU1anVP0z0WF41k4HVI0xtp7sJg5us_ODA4kuUnzE5nLgbcrXpseTVoR0iSNYN-snpefTTxTn0k7S2R-Hm-lxU1Bq9OkJzyfoj_3_KWf8cOz7YHAXuFjhgzUwcapUPdLNY48AUgaU_K9po5LGWSQ_9_flgb0QdZX9LPgDsw8DLrxVUtIiYCj2relJz7_zwlmVfDigeZBrgi5gj1Rn39bWzaBjNzwoNnXQ9Tm1rFosP3nag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=I8-CrFUO66bkI_t0GWDdGWEzj5-BALcsf9E7Inkl7L5qil1bBtRMjBvFwFpEODHA88WZOE1FmTduj-XzLtzv7yozSnV-FG2zZkSparXeqU1anVP0z0WF41k4HVI0xtp7sJg5us_ODA4kuUnzE5nLgbcrXpseTVoR0iSNYN-snpefTTxTn0k7S2R-Hm-lxU1Bq9OkJzyfoj_3_KWf8cOz7YHAXuFjhgzUwcapUPdLNY48AUgaU_K9po5LGWSQ_9_flgb0QdZX9LPgDsw8DLrxVUtIiYCj2relJz7_zwlmVfDigeZBrgi5gj1Rn39bWzaBjNzwoNnXQ9Tm1rFosP3nag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDw4XY26XQUFt38WAgUu35MwaI9FCOcG6_RGXgVlS0R5Fn7yqTKgsh2S3lg-xcCSHbkEHtbrmVNT_qj8IL_vIAV6-h0_GojXhZMBYK5VJuODDDJc3AIprCmFt0FfizshBWthl1itlA00YPpYYG9PGlZ2YjFl1auRbMR1Pjsevd0DRgwXKx21jXV7GYwymMQq8JUXVxulllhivLycDhI-MfHxWzrw54Y4ujv-58mIs-LaiN-p7Rlf_0h64JSShyn4M89qbUJHxqZbnPoegr1WyYhKfMiGIWsX5NapoeAXKCd0dnclwGBipGMRw0Z6R0taH17rjaYgOMSOkbtriQkQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDYynUaGog3y0X0XqAq1hBpg0XnLxHDcK2UTqICFqgk7dz-KzW5a4xtFPsZvFBGO_y3iGiycUlV310ZxO1IdiA1eki2uiVMn13jyDYA9winx0tAUf8vRUJLuMm9vHnY9ijMuKzMWWzSQa3C6jd517pST3wj_goJV44z0OjSxECRerb04rd0Qd_rRhG6AFH5RY-h2KgRyrnwBe0g68pOzhNQzVK3O4e-J3GknMCc6crulgcWIUh7B4bZrQVcKIuHh9nn4CfJrglb3s1mf3e8lwpb4-hyNX1CZetjHoIFNgIttrtK9epiw78rvU4Fb3o2sXx44x7-iZeyVYtAj0wI9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=LWXbCVigQtA3y7HE6l80sz3RC8QWT-OBrIb591mtEbrKRxfSouWfVmp5EVcY6N908Afzp0qiPoIRHj6g884tGPrE_gyXpr7hHz6TF_guNngzgDj3wQIaLRzzAuOXOV9UQOMp-CrS9TOc0n_gN3xSL7sKJaftJR9oyCKF9GejrHZ4V28TXlZjcWCBYH8vxHF_705A1BS2mh3H-HushnPPxsdIGMVHzuVV9xcioZCwwUpGWRR5Kf6towrGeY6kspUBYTB-rQsvEVCZA94XEsfCeKjyh-6v5PEJa8D5Ia7RWE8kNU0akokH3vUA-zeOWlNzCTJa3S40sTxGNnwa8CAB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=LWXbCVigQtA3y7HE6l80sz3RC8QWT-OBrIb591mtEbrKRxfSouWfVmp5EVcY6N908Afzp0qiPoIRHj6g884tGPrE_gyXpr7hHz6TF_guNngzgDj3wQIaLRzzAuOXOV9UQOMp-CrS9TOc0n_gN3xSL7sKJaftJR9oyCKF9GejrHZ4V28TXlZjcWCBYH8vxHF_705A1BS2mh3H-HushnPPxsdIGMVHzuVV9xcioZCwwUpGWRR5Kf6towrGeY6kspUBYTB-rQsvEVCZA94XEsfCeKjyh-6v5PEJa8D5Ia7RWE8kNU0akokH3vUA-zeOWlNzCTJa3S40sTxGNnwa8CAB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=szuF91iU1P7r6b1c7vaUwfM15OETkeRazbBlht6gEAi9wCz9TB73ayM4OpfxXbM_WMrE2Ro0Jz0MsOKl-tED-L9OJz7qeoAWtejQd1JERlsE_F1DVEMeHkBg2rIfIM--riZ7kYmPzhjlUT0jG-Iv-kgjzQXFySpFXa6gwB4aNbbBfTJ8-hbQ_DsqzsCK3XeNMmOG9l53QGck8MfjvGaS4rOiZlI-6e-E3LMzzrJGQojzm3iYL1JaPMX6rYSCRRcADYilcF9cAV6EuwhyZOX54FYBO6c6_q9m8ZXA-4BiFqnxuBaGh2PHjlwmGL32YXlZRZY-Rxd057FgQaxiTgSKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=szuF91iU1P7r6b1c7vaUwfM15OETkeRazbBlht6gEAi9wCz9TB73ayM4OpfxXbM_WMrE2Ro0Jz0MsOKl-tED-L9OJz7qeoAWtejQd1JERlsE_F1DVEMeHkBg2rIfIM--riZ7kYmPzhjlUT0jG-Iv-kgjzQXFySpFXa6gwB4aNbbBfTJ8-hbQ_DsqzsCK3XeNMmOG9l53QGck8MfjvGaS4rOiZlI-6e-E3LMzzrJGQojzm3iYL1JaPMX6rYSCRRcADYilcF9cAV6EuwhyZOX54FYBO6c6_q9m8ZXA-4BiFqnxuBaGh2PHjlwmGL32YXlZRZY-Rxd057FgQaxiTgSKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MumhJf6TOiJ7OVl_lxIteUtEYxe0TRPyq3UrrhQI4Kbd-5c4fcNrFdaKWuT2HDiYyW1f5vmYLsLh6BoYP32W8EbBwrHK5M0RCLOA7zgdroEO176NjxxtRa125KuYn0UfO8zGjzKWWu3UIHH7547DXSnxTQFIOHXUodlPw4TiXdbwoUUtN3BGQH1B7oCsxP4TTul-BlGDVVT68728_tHpAq4kSTfFgcouYB_xxx5gIJKDvMsMJLKcATDISHYHKLOXR1GtHHvT2NjV3dGtFn5GcPBY4sJruterkNf12CxVQGkQptsiTsBpO4lr_rYZcEIqclHgwlWSJ4nuZpO-Pzi9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8Quv-LtWTegReMThdgf2u7tIS_ljP2vYqlTc1auoOwEIeKMJEq0Qq8yZSMd3XStkTnwevXyJLj53RffzRz5_VPXxG8oA0uM06uuxww6axM14_bZ7vN4lg9lpF4Nu6Akfm5GBIzCOIqUVnEocDaeBclXsv81jhE5Mvppg7Fpw3VdoXi5vZviqsgJDEsQDv6L8xMh_FSBY-XDOX_-Q2VrlWCei3Qv-nyXMrijmATkIxwjLziY5SVuURnk2--j-eGlNLDDsIcx_MB4qxhi8j-Y5VLt_Y4jBonXUymVsWBxrXontf9-SEUeppGFK3C1RiOeiBan4MUMVGYJzphNUxNxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=qHMfn5GvmQRcT_1mPU3FgSz9UDbzri79GoJwNdURXnln1vRA5HDeGoajfr16fG4hfh2w1PVPNrRl8_Xpcq1rO8-5eKbcV7axrg9n3j5GWc_OHERYWNvCdyUJb2GMIH2Wu1Iw6YuHQFSS9lhRgYB8bYXfVA9CnqEDIV1RukjEx_Oj_jJBtUYNsxEAdCAi1k7c4w8Gc3LlGy-_OrvHboNppa2Vwct_rklMg7PqeCmEI0KUMw_5KZm9iIGzq4RwIKzVEqLf7zVbGjCN3_iHmqEeRqMo9OvM8kIOEBfqjTe8MrWvtRuzzMuJkcVVd9LbDkQ1dWMo__gKqiF2Wry-Sqdk2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=qHMfn5GvmQRcT_1mPU3FgSz9UDbzri79GoJwNdURXnln1vRA5HDeGoajfr16fG4hfh2w1PVPNrRl8_Xpcq1rO8-5eKbcV7axrg9n3j5GWc_OHERYWNvCdyUJb2GMIH2Wu1Iw6YuHQFSS9lhRgYB8bYXfVA9CnqEDIV1RukjEx_Oj_jJBtUYNsxEAdCAi1k7c4w8Gc3LlGy-_OrvHboNppa2Vwct_rklMg7PqeCmEI0KUMw_5KZm9iIGzq4RwIKzVEqLf7zVbGjCN3_iHmqEeRqMo9OvM8kIOEBfqjTe8MrWvtRuzzMuJkcVVd9LbDkQ1dWMo__gKqiF2Wry-Sqdk2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=owJsRmza46Y6llPQx1RNGtgM_X1OBfutfRZuigf6SuLPo2birGG1CFfhBvpQENf0FMCRInVN4LoXMOi3f-8VXi2mv8sX7s3GdWEBZZRoSpfwPkk1EnyKo3OE-bMRWTIr89qPStmhByNhcrJDBhj7G10aE76FTR0uXmEY2QCvPKYlNRmIAasDv577ApFrZTFFwE-AM530W2Dr4GZc8neGbC8TQpCwPrW9V_q5a_gKxLvN3EiS18GEWZvuKTEmFWs4Wi-jeAzCU8hk3n3wZfnZwqJClwjEuB8dXMRc9CeCdVRttBY-pbn6-ZdRd66etZmYvkbnLukqFQdrzGjsCm5IcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=owJsRmza46Y6llPQx1RNGtgM_X1OBfutfRZuigf6SuLPo2birGG1CFfhBvpQENf0FMCRInVN4LoXMOi3f-8VXi2mv8sX7s3GdWEBZZRoSpfwPkk1EnyKo3OE-bMRWTIr89qPStmhByNhcrJDBhj7G10aE76FTR0uXmEY2QCvPKYlNRmIAasDv577ApFrZTFFwE-AM530W2Dr4GZc8neGbC8TQpCwPrW9V_q5a_gKxLvN3EiS18GEWZvuKTEmFWs4Wi-jeAzCU8hk3n3wZfnZwqJClwjEuB8dXMRc9CeCdVRttBY-pbn6-ZdRd66etZmYvkbnLukqFQdrzGjsCm5IcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS9JXZKFqma6oAvArCyLGKAP1UjVavVV7SOXeB3_AN-KT14ttEQkexLT0EEIguCOU84nJyiAf1loFRhLD2gs3nGG6vUqQgAcotZt7r-pk0W0w_luXKITn6xYvmTPGPb13x5jtn696ToddawgQnMHQ9k3FFDGUb4tP_oa3pEx_Ju16-_hrLYDQsQJA45iMpqNe0QlkhSEn7-_Z7nHA59AK1n_uz6eIXcnK-WFRwPzbD0pb9S6_M7wB8jqJVelATli1SqLX7Nz6UGK0rp7YH1T2kx6HtNXHAkaVoqOAxLlpYjHKDWHzPBnUQg0Xwa7XqjHF_3C325DpfEWX2QfDm7DkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PammvpfZY_c_YWuqZC_3y36ycU0RGCw1wwyEmzThFrXx3V6mXHlmtKnyXq6l86FqD2g5j8j4hcKDKgHOwOfkvcCN_YhkDGuQWEGk5xyM1NdpqPEEi2to_WFbzgkZLkjw_aYcnWKCEVM2s6f9bHg-oMlpEAuy4SvnRU9ePswzQd2RuS3lwVAUtxCzp3SpPhhXAUBPihhh4pXRCqSxlrg6puRt10u0WEEbBo869YpunTKHUccz6jDSEajaFf377SO4v1LKmWRgaf0MdJafgQkfQqe_Nw7xToZVSM9u29SZeAW0IQDUh5wNrHySwpZzM6t2X3EHbiREm2TDfpMlUYdYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEmMcmi_RCfjC0CbEr0hv1_pr5kvK6kTh5zCshzRN5fqVCNRnvzY0rSAly44NjgC_bX7AMgo7vy3fVYDWmQedqO3Yz3-nIQtncy54QQTsIxY1kiXUzepXoPw7Cg4Up5JRck1u7VFVjSxjNOD47wNk5-EEmHg12Xpl-WBFTBOixWGiOwvwVf1940cRlR_BJd8MTZ9YKcxNp2NjUFXyQtZISbxM6X3ZTAcvucEgW8llVqgAp9nPllTQYx522l7_UogMPLhUNp84LY6_qRMa4epXvziJUBsihc6gwTThz-u-9x5QNp9R5bLUFHr8MNl8N91g8yh6sYIByUVjqG1MUDvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHFBVNb0TnRjGbCFewaguJHToCW6jDMP586ReQSgh7ET2cEqHmAxn8V7EtNTotQl10weBunzQcq9xRLZ35Ix-e-UFhIB6zwyyPW46IQqJqEMTaNNOCIlRib0Kz99s4x6LhaGhfLkPoKEysQ5kHxOGpPS3sPexi2bUFJSJO6pZHwE0RylqDV6RauqzSFt_qZjTq_bR8Bi3cI-JUOzRJQe6MMiQMW-rU7dgp-8lYu4mJBBIGbtQ-Rottpdhrlxn5MvCn9VxxAjU9j3uPhoPfd217JMK8JlcVsAK2vIbsc6y9OMBIgWJR6VBnewGQtB5_vBGEBk8UR6idJqzd4vd566PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-LbVcp1lIlt3P1Ke7Eu-CORURV-koHFR7xZGvW59gzeBiDL1l1czfvWDNXJC6RJQDjpnbNqC499Luvfd-qOiZWTi3JNiiQKg--daRg8Hri3PbMinAYAtw-fpOwdQdigYNYvR7qjaka6uYpLbQy6TkotIrevOZ_vfKEXK-jyomtswdv0smTw26QyWtBk1DMdM80c2CWAeLejR4I3KRKEvuQf3il5iFkMkVEPYXTx-hEMdpZVBc_nuzWbrRk5CESdWczG2IpR-94Cvysy6Kl0kijXatdQnlsw8W1vv_f7MXG3R9etSC0VPMoU1x539yXMwOjb6ssYyL8uWmNC0eyunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twRLXyuyhsBw7-f0wjcxeWGZ_M55LwZU-WXWNmmuvpMyxpHEGfbQHHbqYL-BxT-tAXbpqDAbm87ADaH2KUghwjmo-l_YIG5pJq5tHgdv_enlsN5CWAS3mhk_XgCFlWBhQweMo2lNtsbu1EsWQ4jQVDIGP4TBjocVHs1e3XCCdtgsJxuyb8QXqshnvhnaER8Saz81XFWRVWluNuotQo3HOrbaO9x1VnqTTZ-4W_y8vVgD5sAzWe3dzPjg4Vod_6m2oUVdTFB8PsPD7T0zUDHyCU9ncpuqRR5Bq8tWYKTVIm47tAtAvgTf3SflBp6ViMmQDzZjsyVNNP8pDsXnT06I3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcpEpSsZdTSBVfcKQH7mfxwKUj3jeC6vXSneOKyh4zbuMcrLaqt4UYbCz49pBuZTJXFfuneqngzJ2XH0EIaInJTgPQ85jCtesxwlzyBXrnmNpXk8_OHQkO52kshVHSCSF2NzFJ1JeEovExAiPiHj-z5mcYm6isFIzxVl32kgR1J4XSrs2NMpC4v7reOmoT_D9c_b1p4qDcjLmC085gUlE5JTinUDxxaZ7cdFsxa0MNQr0aZ_-xLtc8rC0JeuWTOW3eFJqiA3VRvqwzGtOkDsm3vNS-Y8-2bCw0YZCnoXLZWaaDE_ka_8Mf8s-Lt5iXDlpYF9gAJ_ztSkpIhaYu7dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf8COxivz_pnsrH7dWziUP0LA2A6gBYrUvkWDqc3ELjsIYKzCm_Z_-AFiK6CjAchl3gKaa70GvbyMmPZWgE2TFqKSc5dTgKM8vcaX0mfpBhxouVdUXdQW95k4TbX2is3ygN3o8tOQe6rw4HKVvPIMVai9_zeOExuV54WvecKmKgy1iLmoCw-GyqlaNEo2z_KwfU87ZRKr7DtbwUXmUWl3iK1-76IysvvOS_GdKartOPcufBQXN7oBTD3-4WY2A2olLPu9wv4SaYGrQbVHTF06DMkpM4U6ksiFw36B7m20uz8hZMrtuUAnBKfMqUNbB9yhN81QspYnYvGpB_DdsAx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UaWO8A64JYOmbessW15OiDwjuRZxNgnwWRpe9Dt5pfirE8vSf27YXZpmALIScHqut-Yq1RaLqEPcXTQRlbfv8uqiZcj3qe2xYa0qpiO8jAhLOO_WTV-1ZTjknVHMPnZQrlrQ30NH5-1b9YV4cZuAqy8zySZgNGDnkhETBdLVApaQ_uH8XzHthjVAjDt1bpwnOFVoTTNCLXaJVN1UmaRDmrXeFIn5JzoP0yMXRSkUEfM3oI-cBgqsZkg4ZB1p73GXS_keIRjgwroinx-9xlpC1L5aXyI-al1YNaJs5NeZRMaUZZ4PfCFRAaLeMKlXYRrgQmwoNY4TjfOxknPGgTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLtGIidmbX5uivy9ngqTtL5UaFK36HH8CepokXJuxRTnxmxPElDhkjF2jBXwskkeY3kwn-Azmj_n2H45G_2WwcJVnSO0ZR3PtczvSkT_X2Xed7rTMXRkKrp_MHNmlJwzCrUKikkRKtgAzbAWwZCCZjMFP9wHg6R6v4iwjTDOEMZWiyYUm7t5XK3sZEkHEHwJrNIgFrqPf_NHJom8BgTwAOOJ4k6mdQ3tut9OkTJCqaS3SAjSjmma25y_JhQhynoKFvQ1XUvYJvXdeRqm6M-PlnjS72NjSXz9d1-EJVpRoslEa3V4fvX1iYZth3xhMwryTMsdLqvRwl-bEo9y17gBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVfwgbtZn-iZsyaYS5AOGLcaUUBGad9CP6PBac6sfyHFR5_iTI4udZ6C8wSplisOiq6vwfQMjP-xHceibt3YFRPg_4gq3ue1lqdr2zIAp6-1l7YX0lGFHxzX3l6aNBC2x-Z5AgE2LzUbwpv-y1Vq4ryV_Q1KD5FTaaDuCAPO3rPKCl-gMdb6sbW-SUEVkplxFx3f0zxkqpVDLfqBCrwzG2JAHM9_Iwou6YkJCzYT7Gabdfoxq0F9DW2Q1hlMH3JlUGRFF8K2rFrBXoI4ay2z_QlQAlTzoEY7aYqrretEfDwdoU8O3CLUDT1j5GOrEgfM3KnF_bsE-3my062nlHnRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH9zo8p5LsViMqG60ffaOlF8eeJf2gOCwb4qQXbtKUVsZNCJLPf3FZZI3I6ca0AFZDEHsLizIdrdJj0RvFpuowLNmw5lMQVWrEE06kQ3MG-UQQ_PXUqkyEpZ8jZ_PCgBYlzcyahn7lAmNguKpWK6qBHp46t3vjzgzab_5O88OHvXJEtxhHoHIY0z7JDUV19wXvTx8qnE5Wupx3920juaWbmv1sut48nKyXcTmY_B0FMTgA35nCLvB0M3oRedXYLeylqp7RCVQBUUUXMFgmbO8zHUE4zsZpcSJYJJLp_cNfWG96EQ9UfjT1SXNRH1_mllbVgZTG7VwRDPbS7L7kaHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=BWce3sIM231pwfFJuBzVJxZ2S31p7JiW-q3kEfWBT0KV4dCZBSANQKgnPqD3pPp0cvZfUDHZVT2xhwsXqGE4-kkMyM3h53Bar5xWHvimB50kEXwWZlfJqvrxxzwswuct581nrVhfVNj2Bvc_GS___Ehyo-2cXkdMhMoFZ2ARD8kSjY2yglbeTFmm01FuY2YFjA_ZgzOrkuKsxngty200GT9WiCIDay_f4mnx_Kn0YB5cC2d2pb1a8pZ0lJUBZcxkexBvDcsT-VJHWYcnpyRsSvkgzHKVKwt6OiJ2uaIt_3yxpsE3tED0FA3NOvma7tq2wmZaq764DNkLnvUWKS5FDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=BWce3sIM231pwfFJuBzVJxZ2S31p7JiW-q3kEfWBT0KV4dCZBSANQKgnPqD3pPp0cvZfUDHZVT2xhwsXqGE4-kkMyM3h53Bar5xWHvimB50kEXwWZlfJqvrxxzwswuct581nrVhfVNj2Bvc_GS___Ehyo-2cXkdMhMoFZ2ARD8kSjY2yglbeTFmm01FuY2YFjA_ZgzOrkuKsxngty200GT9WiCIDay_f4mnx_Kn0YB5cC2d2pb1a8pZ0lJUBZcxkexBvDcsT-VJHWYcnpyRsSvkgzHKVKwt6OiJ2uaIt_3yxpsE3tED0FA3NOvma7tq2wmZaq764DNkLnvUWKS5FDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZdx34TQW2PuPHI63YrBNwpTm7sIwxUbDe5owQzrd-NG9s6oIx9AXCT_ueSdWnIkBFfe9zugua-yjxgPb9G2J7gv_8x0FXiA3ULKyPTExogYscxU2egs9Z7VlfsWChHkI1ORXN_D4TuVE4MDsYHvRmqsFXrqRBGu9y5T_MdhQvUGhnOdZXk31uf1FNLiKQCndS6013faSa-Au3_wXUy-OOBTHCvO-x_BZ_xvK5Zn9TeoYTO9BodKP97BFRJYB3ZZC1iOv5-qjBXvr_l9_h71avVA3GxZrYe1Z897GZCjuXr_c5FAaP1XoX6uE3fIW17exW0XEF3AT9zsPOHkyKra-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-1-4Hp0x_IE47dUk1CqRQwe5wzYT6ycXtr01h3LD92IfitoleSrDA3Z0SqUcQBytL99OtSPMuvkdDK9gDacuXIgzSmZoktY89MwCRQHETqZa7zIugIGyMjXnmqaxJJK9vM9mXktW4WF5beqDk8DJD2-VbmMvA0NPfkeZi0FxoUdAabKORWZkALfBXTPat6-cbo4GX0p-lY3KP2pB7FMz7_89Tnfqrt0N9Bp3tf5USfLuTcPQUzdGe_hZ7d31wUKdZqksIauNiUjbaDkdelq4IkhTbqXbB9eISDxd1I8MV79H-5xsLwB9w8ik2B0dluBy4qdh2DNxMadlgIycd6CYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbND-2CZvQzEGlDRZ8nNzU0aexn3eunQphJBwtcsZ57jMIjJxMuVBGjGWPfPTifICjlmbkLdxXGkUZPZVtlrGQU7Ph6UypgvdMOi8_y20zWof8QJ5sFczmQFKedzxAVKnCaJxAAiIxLQbkrFuvTV3Gwy_ntapPN_lc9qeBXtoxQxA-tAWfVaMtJ_UUJ6lh0PLwpkq4l_zFzHS0dzcgakSIASC8oKHTgcm5jNYe0MMVG5DlI8ZGHsDvbEC0yWnofdoE-048iSSBHo49HlwW0ZWI9IGKvOY5nYZieaR1SHQCx6GcaETPVSNoLBajZRmpdVqe6WbVlQlug5wkMhi6oPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueVH8IiBm8BeFd0y723224qcV-NgQFja7ddeo8HQsEif0fzoGoxT5agIBFV2we5TDcMO_ewKf_2PzxLNN0Hh-LwdMqSZpZUKR6ZB01Ky3qD68fptGbkzsy6yRczlS5HDejeyied-4ljn3OCv5su6vjGFR20UhQSA6MeuBEixre69ZRbj39TdLsPryUeIS1f0ZTB9_Zy7U-16BYW_iICao6Ohve8VERLJRj2haYb203v04tBegPGSnqoC8CNIPHKg3PJ-ni3YF78YMH7LxGHAKGgELaALg_6mGhCEvS9yBiG8iN6KprRR2av6_Hg7OS1iXbZw2PDR5me8sKTg2bc0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAU1AZ7c3tnkzMLhh9iltJdsDAJ9Hujzy7iUNreAjbDiPXhS3cP42_kGPcEksc7Pz9oBesd8Oqb_BAERwiTintRrng7OLSoTUxBEsuGauTvjQ6S0R37v8OXfFqj82EIYHj0fFV37reWSkpZBl2U0KZOyWTq_6zAXWp9zv0eJlLs2Z_l9FkWo6RpVV6SD8iSWoomn3e7ta3Svikv0SJ1alTr4ZQTRKxoUr1O48ZDSOySa4yQ1VBhdgWuQpV26VeX8OMvQXSeMYTECjTP7zg3NjgVioHVXK6nhjjyu9GFk-EmkVKq5G8qqgbls-xvtuBiFVjXghdBD8Sn_A4GPqL0zSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMd1YZAClsoZjM9Ff_zpF2py9sF6B0AfhOKMhLRb5AGdQp_SfeUk3p0v-YKFzdcLxcPf-Hp0gKheRIjW7Kir68NbtuJjdJrbYqU1e-M85EtQe0bay1Hnv4odjALz5gLmJIf9_1dcgeVU5B37Qe4voMAUfyKQhT5wqSq3RWVJNDcu29Eu9yaeqyZ06EvYOrvRRh1XFYCrjyYiwUhS2CrbyzhTUoOoSouYZhYIeVhCHCRLl89l6900x2Eq3-KnO8FF7Aj6FPJ3Tp_orFVZTFmxp53jDm8YVAC0TyaqZWr2aU7xfxvybnjF9AVQZHPl3IXPISjaZ9rK86GO3siPfTuHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx-X6Pn96FwAFKYGJ3kU9JNZBQA7OY8WIwqNJ5exWG-rHmoisPM26wOf5We8YoiEfkZCelOubxR2adgRHFW8tMpial9QpRoI8lcejmW7j3A_rywkaHm73HvAQcD6snXTVbcwan6dGlElHTG9FWM63cRTFLdtUfWY7a47kN8iJAyK14yWpunCeeFKzi3CyfHueJK8mBOB49pGnx2WYIPCzNrqRtHZhZ34SoQTAxYB9wbbApckY7cIaC2A2RF9m7QYSI-JI10QL0_sK8AZsqVfE-Uy3xbr0K0YAmIeh7-1O6M90DSHqs3vvgi-kqKbyckGXo8GC2t_Wcqp8NiTPCLm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwswfonAbgbYkKeQo65zdl-FD3i3q2euiLt-ZQ2XzKpPdv_j2oHp21_StSDRxhwjkOplhZVATWQkzmpsva-KA2G0nnD74tf3vwOFCez0eOcI2I75VNq1qIts1ECgrsFtC8K9VQapQXm2Is3yUdafAoQPlNT884hhyKKnzRvtmktHZK_qGIoW8XJ55HeSgsCQRllL6P2vTlWjviFdMUYjMw79BmKAP-NCRADm2tluanWePR2POMy8eY0rJ2cyy9d9GpwnkTwrUh6alD-uaAnNtXPpfeHDF0QisWV97uhtNMArvS30lUCcDwuDawul2MxftJ4uGKEBwzeXA1H-tUolsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxlNJvyQEkZzRzM8aY19T9fycFlB6px3FwdWpNbodBrm0WMZujR9TYkuc2hkRWVPEzEQGuUT73HR68Pob2YiUfRiNj1QxxaPFnYiLrFMRli5uoyyHb1pnJhlj7s0H31ozP6mbNRihm3MZipaWO5hM5er3wGpxU5B50uUh-TH-LQbEGHLEKYg1CiEzER44fmaNKLPL00syL0HML5eF-jS9m9fFfsKCOe3MzgtFs3bgBlWezATM_jTWSJTSAiF8Gv2OqdGnJpisdiiWH5_ln_JEpeTxky2gakD-yLROVPCOx8bsL0uYzx_Uh9Se4NwBMkUu9nm68AMv0i9c_5DIZNB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RawSSzhq3Bb8QyQMWt6T8_iZgEdk6CbpcgZx_6WzEVY-g-04PIOBRiYAUsKaPpps769CN5hiu48WX6F0JsxNChlH5VZvknTrmY7j8nIWxN2tjfxZS147IGs_ZhnvYkvH47kfKkOeeCz0g4O7QKogIORKpU6qwNHNTkT74872lK6MAQb0gMOPofgPGfqzX-Z-ObKoXvBqGS-xe-vXk9N2wGOXRepuxVSo6gXdHn1MRxMktPosJyfRhpIOtfWXZWU4JP2j_eVgO7i9PqJpqq4nYKDjbEctTtTpxW7KXCuBD6oKD1pGp53RvNdq7_xfgUiy4Sd16RVBBTdIzp4OZr3sbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXPVK0t04VUwlQualOU7-F4PpUw02ZXPhFkY0byyg4Plk_QqvsT2iQZB6UPh8ZL3JKOM3axHARW9JxfpPOL5ei1Iy00HN4qRurWoYmWwrwehszVPapmLq9zJEunyG7N7L7WjR-213KhxXDNp15VncTsfghKc7yn40kkq0CJGAJc7TgugNvle35xB48MSQEccZng_qk3E2nJiBS8pN3aPq3qR7ug4lbQchxwfZHdhRVjIEilBHXUGkwhNWwEMqALtO3BwvBagNjA9Hp9os1WnVPZSPM2iYONHWx__HexmgrH3JYQOXww3TwhPBWwGyqtzfkJ5DK768i5zBdP8qE3vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvt7e6_Sxf8Bwl-AJ0gjNttL-r1ik7h6tNEWzpyrAPBHHXdgq9zsnFMbRwqF5PiWVLGU0Efz5z5Iv7lbZaHU6PvvyJFPfk9A-4TNJNVtFlJ8oPyJJWbBYKkxle1btgfIGHN-vpnwKEb65hFw4c3qNwtECxICcFzzr0hy8nKI0_N67cuFo09HqQrkgYGHqJVPz48YDE2nt0yf0ihhIJefbVxaTtkbNOa5KE83hxtBc_GYSPRBv4shPCsyxup6EiTzEDJxQWStU_hnJWhyehCMIzAIvT0rXdcmAcIFW6DdIvNcuuXZTrhrOofQkssdC1d2m-JrM4TOo5AtwgPjt32CbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2FbN9NZDFywWqC18D4V_PBzJDM1bVr5w6FbThio7klsE0ZCg8k93A0mpUpFc-Da__F1_AbE8hNqpzl0MReYXBKfsyGVVGorn4hU_LuQIgjOWaeEFaIp2UjsUaJijZpdpAd_h1ppveo8nJ98JKrOt4BIZ4EwS_z_967gSY8x41Bboj9KdWhGeSjiUPm4WKIGhTuLbCWrGAD2nwVg__88h6CrgnGIjdynf1wWtSqLfBD6DFs4dveJBZCJqp589v7mG9fO5DY4mCu66Ro-gnZZAcUPd-DycCwkoFEluya6g5agdFRHOPbx7dcR7emQ1pgheHNxHab7Cd3j-oliDzjt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=fYyHXVoXdSqrZDfiORzSpKMWZsDi4npCQzi9bhKjBDkfAdyjqWlrFzAWGYDzv7t8tkYkrp-evmart-jKq6COgZ2Ly1oIDY-T2uLLruKvavFhb7UtXYjzpeDzYOOb_Ox9eH5KGcr3TIBCEq05Tm2L7Nh43G0UEGgtI7hpwA1hK1jZv80TwiwAu4usF-i7mgbukHaFSsSAqBc6oc2yiwFa31-vsVPkYDfjUprOGYVXMnWWGNpY_X5rKDiKg-9O3F3pUcnxwtqE4oV3qM5MwSUbR5oHyJfOTxftNCY3Cu370Zt_r7jeUoocukmxPeg0_G3s45vxsBQECaY_8rGU9LwYs08FCyawM2ktAkxDHNESwyZUNkTQTkvkKHy5BYwqu3DTZz4iQ3Drl85EoZRn2JXFermFQm_Lqfnl96uB-1b7Caw3sZjv_iY6Ic_eJzRWKyNmk6yND3KRl0Z2xXt5nT1i2j9-x625swOLju1tCJkhHsaMDXD_drrW0onb5l4_nlUtzlSTqXpfWTRvW_yO776-U67nvEUm_eepLyZJ-H-5aNx_faKssSf7j5f9OLs4GFGpcEj-jN5uYypZlN_V5QjDIkKA-WM_5nvZIAjxO4Y0rjaigBpLkmpYIckyOqnt5Pb8oES-3xKv3gA2hXhaxo6PQY8vf8jtwu8rsPbZwt0Qzto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=fYyHXVoXdSqrZDfiORzSpKMWZsDi4npCQzi9bhKjBDkfAdyjqWlrFzAWGYDzv7t8tkYkrp-evmart-jKq6COgZ2Ly1oIDY-T2uLLruKvavFhb7UtXYjzpeDzYOOb_Ox9eH5KGcr3TIBCEq05Tm2L7Nh43G0UEGgtI7hpwA1hK1jZv80TwiwAu4usF-i7mgbukHaFSsSAqBc6oc2yiwFa31-vsVPkYDfjUprOGYVXMnWWGNpY_X5rKDiKg-9O3F3pUcnxwtqE4oV3qM5MwSUbR5oHyJfOTxftNCY3Cu370Zt_r7jeUoocukmxPeg0_G3s45vxsBQECaY_8rGU9LwYs08FCyawM2ktAkxDHNESwyZUNkTQTkvkKHy5BYwqu3DTZz4iQ3Drl85EoZRn2JXFermFQm_Lqfnl96uB-1b7Caw3sZjv_iY6Ic_eJzRWKyNmk6yND3KRl0Z2xXt5nT1i2j9-x625swOLju1tCJkhHsaMDXD_drrW0onb5l4_nlUtzlSTqXpfWTRvW_yO776-U67nvEUm_eepLyZJ-H-5aNx_faKssSf7j5f9OLs4GFGpcEj-jN5uYypZlN_V5QjDIkKA-WM_5nvZIAjxO4Y0rjaigBpLkmpYIckyOqnt5Pb8oES-3xKv3gA2hXhaxo6PQY8vf8jtwu8rsPbZwt0Qzto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJZDwPDS-Z2gOP_gZvp2PHISaKym98al7xY9Qpfn6V0eYH4gb4KjWVHl3lGJgAoY0LCdLX25ysBVHE5XNhrJlt6qXvNiLJYbOZEl2mfQGATNUl4JiP5gz_FkcIZgshBxr8Qzjw7hVhILbETubWCjXqFM7GVTM8CdJhPSIf3tXlXha7VNVTu6cWVy8xXhIoeefNlaOVn0VZfN83fXdCW6dEKqPbGGJ8p_cUAsSsQuMDTEDQ7W8uxSCM5I4DHJP4-uXKl4nuOu6XwXmGKVLIbRiMReSh0vxFU8OjzkDs_pCHptUgCqZBbDqjTOwO-G329_hdw0ZRs8KzNrxYMdmKS9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=O0JZ85sjh_zBs9BwDh1we-8jsdwdr3Nl7I93xX9AC5XPx1noGk-IAGX08h9p6FI5xuJhHwDUa73B3eddVsrXuKkBY6M5Zy7KqEHjYVVAj3nMMjzJKIG8HPScillLq4l6KNAQDnuSa5ibfNSz5QpuBbREqpahkazalgj-xMP9YvA3RGVlAz3xBBjnc1mNigjm6zUaIwjHEyZbR8zrmQuv5PZbm6l77VtU5m4k2MuT0IYrtlg021fQUUn9--NnAIsv1RhedLyceD0CaDXQOBGEjxPF41qax5u8mq1CUeoMv2m8hK7GM_qZ-6K3dm1l-jD7GFxOo8Yv8UOGptmdUZYqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=O0JZ85sjh_zBs9BwDh1we-8jsdwdr3Nl7I93xX9AC5XPx1noGk-IAGX08h9p6FI5xuJhHwDUa73B3eddVsrXuKkBY6M5Zy7KqEHjYVVAj3nMMjzJKIG8HPScillLq4l6KNAQDnuSa5ibfNSz5QpuBbREqpahkazalgj-xMP9YvA3RGVlAz3xBBjnc1mNigjm6zUaIwjHEyZbR8zrmQuv5PZbm6l77VtU5m4k2MuT0IYrtlg021fQUUn9--NnAIsv1RhedLyceD0CaDXQOBGEjxPF41qax5u8mq1CUeoMv2m8hK7GM_qZ-6K3dm1l-jD7GFxOo8Yv8UOGptmdUZYqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_MogopVP4cpKx1OL8vx1-kHzZBSHSR24QAWA59hh1PrHFda9TTovFsADwv6eELsO86DqmbZ2wD1Nn37F00R2iQ8qynX3t9bgDZgmYVnbXaTqOdj1JqrTMhYQ6WFpNoARSm62gJ9WtfG2wrKkFM6uY-hVN3kbMPULxCkM7X2aDT8mFRdg7kRdtLND10w89P7nBaEm2PlOL4JFDQzy1q59SG-3JgzLvhmmqa8I6101k87Cr_owrSiOx_bKnA9bC1nLR7MoS3jKdnVzilkbI8EHyMzk7BWBDu2UdoE7eZ3PBDGUoxADTMjLdWYaxDm6dsIFqnEJppAPycFi3_MbUHrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF4z8iFFczzFUtmM6X7cRKflJDw-nhyyC2H9NNypS4d_mDNXlz3zORMyg9tS987F3CmO6kC4xv7xEU_tD-xi2jK2TW75fviG38w2xO3GCJc5HiGlKYKWZA9Ui-ON_3y3SgvjpX1whMmDMFzl1K70TTcjo3IbnB7iZLoHYgaqJjNFp8GUU_wAAy2st4PzU11lsh6whZPI7KHOdV1WlgN6l-jpuOX4DDfhcOA8I34ZTNawBYKia8_3dymehBViiN8uYvkWDf2x94xgcVOhzMkAHxqPWaNn4ww4mZSGrfedYlnd0Ruk3rAdAUxQNLDgH2DIpfcRQUYEmf_6zewxkrHo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBN0F-DQIlMBCefE7FVP_AsLK2MJbu1U5Od1ykNZ01Uu5nV2KbVe8qq-GzQY1J0SmyX2PNmmHaP4EYeHyyis0DrSKk9lw65I9IRM5Nzh1UVWmldsb0vRTCcEynYrx_N1uSxk6xr65FdphjMuXJUCTEGOyY3ijVCVgKLMz--YAP0fGDaRTWdqlMje9MMRX8lTNXxND68hALdkZjuTdAUz2iyl0cJYAun8ToULo6i7P5SMNErxdYthamiea2dDGoclE9OckYLEICr15Vut4K2Le2XcCKxPZaiVeDr0uwO0NJ0a04LKS_MEnghDPsnkfBMY6YltapvDdDu_-Sq6NjCOkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLBlIUd3Rm4LvpSqt9lWTU7l6Y1xG9RLA67zNlV7F0aob-DiU5euKuhKdjYvbq1YdQm1_4_AOucoJMstRs0rf70FAvluwWi5pn4ExKzbrJ_Xz97qy1WA1rpDC8PPtgdCzT0ROm2E4V44mWJgIaGxxGZciA7F2udAYnfaewOTohCoXn4m3nWJxSw9nJKTA-DGOSPD5w3TAu90B93ilJuh5o67EFEdMwT1KA1u2egYfUQ1YIJLoU2W2X1ix2zr7M6Q1TqN0ftMsRSPZ-yvF-CCOMKbqrshT5WCTFgoVS7pwsU-T_-uSKs_OI6gd9sEvZ1SIaDtop0tG4w6-W9YUNQmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=Fe30m0WuoaA4aeMp1BlcA1o3MysB6HqZQBFnHuh8gPzIbFAcrfd-5FpXVHOzkJ0U3Cm0lfeBpZroH5ds6mbUdnwehiJoEL8TVd86MBNwJlM4zPVxhJa9KFKa5pRMn5r2tmkfG_eHeIwfib4F2RwBtzJsQRcGllqI-xLjWKZ1ApzJDEBgzH9Ze3Xx64Rp2M1j8iLFOInmUm94OFqMcB9wWCQgOYLxnDCGMJdGaGiNjZhOPuceIwGYOVrXtLnD8J9XrWvOGMwhjhMcWedQkUtzUx3_xZL6K6V-FYwH-c-tdHwYzHsvbbecmqVEgDw2FHCG3TRi2_OI3ER8L4rWSVV-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=Fe30m0WuoaA4aeMp1BlcA1o3MysB6HqZQBFnHuh8gPzIbFAcrfd-5FpXVHOzkJ0U3Cm0lfeBpZroH5ds6mbUdnwehiJoEL8TVd86MBNwJlM4zPVxhJa9KFKa5pRMn5r2tmkfG_eHeIwfib4F2RwBtzJsQRcGllqI-xLjWKZ1ApzJDEBgzH9Ze3Xx64Rp2M1j8iLFOInmUm94OFqMcB9wWCQgOYLxnDCGMJdGaGiNjZhOPuceIwGYOVrXtLnD8J9XrWvOGMwhjhMcWedQkUtzUx3_xZL6K6V-FYwH-c-tdHwYzHsvbbecmqVEgDw2FHCG3TRi2_OI3ER8L4rWSVV-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=gIsVdv5NDr6W3uVKprfHfpZiFiJHuZa8PDAS--WBiyuZ8pnANKgJV4VfCpxhSbhhYrGjbDCPBLdY0hJINzTQb82OKuJNXngJI2_MzBr5YwHmj6Rb-gqDdOACInJ0naC2AT8CeP6t-9lTeykrFEopfR2jdQECFNGFKqUwVjNyyKKEAisi6e65fcKJNNrRakinkdmdWamOjBsr9Yc_WlpydLcrTAFeMgmwsf_L1WQJAiq1fIkHCbJJtu9V3EVQVeOMGD-ueRkPhG1qu8wPMjJwfd4vAJh5gsFU8RCAwqq0heWwao8rVJG-XmwrmTRebIVJvY7Hjzc66HifF_CnPYV2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=gIsVdv5NDr6W3uVKprfHfpZiFiJHuZa8PDAS--WBiyuZ8pnANKgJV4VfCpxhSbhhYrGjbDCPBLdY0hJINzTQb82OKuJNXngJI2_MzBr5YwHmj6Rb-gqDdOACInJ0naC2AT8CeP6t-9lTeykrFEopfR2jdQECFNGFKqUwVjNyyKKEAisi6e65fcKJNNrRakinkdmdWamOjBsr9Yc_WlpydLcrTAFeMgmwsf_L1WQJAiq1fIkHCbJJtu9V3EVQVeOMGD-ueRkPhG1qu8wPMjJwfd4vAJh5gsFU8RCAwqq0heWwao8rVJG-XmwrmTRebIVJvY7Hjzc66HifF_CnPYV2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enuaRayzOEWneO3VeJXap2e8AzEBCHCRSTDRL3k49noyyU8HU0hBl7X8a-k_0AEdOM_I2FRWjfKMdcoCSbVNiJd4WYqEk19w9LgB2F2k84lV5nQNlSmAlrjNPa6vbAdhDHteF0TXd1FCSkkQphggsYUVAjjI4XeQRRZ0FVrGyrxkU6wuLCKx_SxjHnb4tARbEJMvua8z4FKU73IgnrhEhtDfS4gmsiOHGcn8O5Fumq5hnWaFExeNZb9_LGh35GuNbTTMJPsneySOStJ28-9IF5yd_LadeytBaSJNefCMIg5v6YRtJjWvBPOen253Nk4f-CpN975o11r4Uql9Z4qwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4vY1DpBcxuQAuLOxJsL46wCsQqZMhujIhddQQeSdokSsJ-e6om2QoNFTl_Vkw_ayF4h-VGnli5JYgz9F9ak3FC6dhTLF8Vgx84Or9jBpA7kJnXVyXQRwMs0_Xsimsoxr7BmVQ4k1XMv0enNTw7uW3hKvbN5YGCf3yrnsLj8O1bun40ba4LjlIT3Royx7-mPHxw_k40-SDKKnhBEWpcoCQ98obiSIrLi2s_459yoWU7VcgA01NQIJ_MUNxocCwGCg_IRZ69MfW94uUCzQsAQfaOBQ3o_qvaDWseFlq6DBU5GPYMqiq1p3L_d7zFHtQ81fbIoBSzMhM_8uurWOqhD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=J91fq9ilhItxVR3i9_4CVMzGC9MXsvf73UIrlJ4b-9x5a724usaCqy3T6z2uwmMZByB2Ccx6swsgx0uXMs6YDB227uTwPoU-nNMNx8JfWW9XqfysL05Br68rYrotP7NzXCkwhGp0pv5jz709Yzvg56zvuXJOlLVMT_2XXSsu9UTHP-o3ef_qnm4_ah2brtK4ALgF2Sn5f0ojlAnvghv9Ryl-pLKFYKPKGuxtftQXBpfIkEh3SEbgQS5MNa81nVlZ3HlAr7UjLmbnx_xcSgXS4bLkCzdnCB6hppcWADCHLgOcKOLnJy9oBi7987PQb9d1giVzA2B9aOnY7OwoRMLB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=J91fq9ilhItxVR3i9_4CVMzGC9MXsvf73UIrlJ4b-9x5a724usaCqy3T6z2uwmMZByB2Ccx6swsgx0uXMs6YDB227uTwPoU-nNMNx8JfWW9XqfysL05Br68rYrotP7NzXCkwhGp0pv5jz709Yzvg56zvuXJOlLVMT_2XXSsu9UTHP-o3ef_qnm4_ah2brtK4ALgF2Sn5f0ojlAnvghv9Ryl-pLKFYKPKGuxtftQXBpfIkEh3SEbgQS5MNa81nVlZ3HlAr7UjLmbnx_xcSgXS4bLkCzdnCB6hppcWADCHLgOcKOLnJy9oBi7987PQb9d1giVzA2B9aOnY7OwoRMLB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=Jw7fOF30-ZDkND3ldKkLW3dtWd5Z0e-dwVne9IqVQTjRQOIfoOpUr__SBfLi6TvnvTfAuvKBwP8iMt2Q-swDXfJzufR8ClO9qSbyHDbmovhrBDC3pQD-mCW5bmKKAd9WSGUjb_xoF4rya1A8ooGcjUnuWtyYdTKqmyAKbCCpVXCgsQGuuJ1rNnR9Odj9n3TUl465LdadwzxQcJUJoI5bIFP7cv_1F7plrgJyXTYwVg3V6csm633G2V2fJ4DHiWWE6rCMsK0O322a9QKZzqJ_CzZ56hq9vpJ8LjYs74civfsUdqQ6vV5MtrVU2mtCjyvL13kzec7yItiFEJfN9U8-tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=Jw7fOF30-ZDkND3ldKkLW3dtWd5Z0e-dwVne9IqVQTjRQOIfoOpUr__SBfLi6TvnvTfAuvKBwP8iMt2Q-swDXfJzufR8ClO9qSbyHDbmovhrBDC3pQD-mCW5bmKKAd9WSGUjb_xoF4rya1A8ooGcjUnuWtyYdTKqmyAKbCCpVXCgsQGuuJ1rNnR9Odj9n3TUl465LdadwzxQcJUJoI5bIFP7cv_1F7plrgJyXTYwVg3V6csm633G2V2fJ4DHiWWE6rCMsK0O322a9QKZzqJ_CzZ56hq9vpJ8LjYs74civfsUdqQ6vV5MtrVU2mtCjyvL13kzec7yItiFEJfN9U8-tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=JQqRqKwL6KUuc-aO385jo3i_qPTHEbqmwE2NXlNc8kphYofyxAxt1XpdTsMP3nUUT6ZvusB4Xt979Ja73fArDtHSezYAWfiLm5NyVLxBb2biVJ6joRoHvK-e6qTb5jwGEBiGjzVAp67lL2kxwX5YuQdx7uqg-16OhGeAGNB3EFOsfwH8THqF25hiB5tYpjwcojQDpmlCeb--J4ON2Ug0M0Hkzw4xvgmVs7AiPKNNwKpSWsXCN6EYwwO8jrcg2Rpg8ALIv3Y3jJlWmA9ScNM1pCu7AvaZvPAKssSSL-MrA5Mv5pw-8cw4L3uNTfPldQFXXdjbIXRIfiSEDuXTSNrscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=JQqRqKwL6KUuc-aO385jo3i_qPTHEbqmwE2NXlNc8kphYofyxAxt1XpdTsMP3nUUT6ZvusB4Xt979Ja73fArDtHSezYAWfiLm5NyVLxBb2biVJ6joRoHvK-e6qTb5jwGEBiGjzVAp67lL2kxwX5YuQdx7uqg-16OhGeAGNB3EFOsfwH8THqF25hiB5tYpjwcojQDpmlCeb--J4ON2Ug0M0Hkzw4xvgmVs7AiPKNNwKpSWsXCN6EYwwO8jrcg2Rpg8ALIv3Y3jJlWmA9ScNM1pCu7AvaZvPAKssSSL-MrA5Mv5pw-8cw4L3uNTfPldQFXXdjbIXRIfiSEDuXTSNrscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
