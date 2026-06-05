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
<img src="https://cdn5.telesco.pe/file/DXS4la6HD-4NjPxFR3uS_9x919RdS_T4AckDu0wBxXbpWodE89S1KxVBemTkNMEkXcea2iYxycwHiMQte_BKdUCzbae-qZnWvpF8aU_i2GMubgOudoorEX525is7kGc86tPJJC8jfO2VgY-hDA5Le2x5GYP8itWgQ24WNcjMFaQ_7fEe2U-sDNQZGEzP3po1m0cZQVDU1vRXFnv4fCdkvYhKyC_-VZ08eOZXbV7KLBBcYscDSctEgo-0UNpMkEN5slVt-v4YIM9Up7L6YtXkbCIWHaOU1xZkXIiItTZTXkKN6ZvIPp9bqY_hd9YEfu42-kRr7n3ttar3w5Yr1gqWNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 187K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=X0w_LGpsx20dVYMzCGu5xQrlhMcSdYN3Vbn62tvKE_g0jTIK2kcDcBN5XYTA-SfVxHv8SkkSnZgxzAit5nNH06CY0aNzLwnPAyCo5C4gsb2gU5j-tZubfCMvGD9xefA_VXUg_J0FDs8ZFP83bkfogeAk5mTLCa-8O8yvySzsjriuLFs6RBHjktpI7vQuFF_GPqIXSRtnD0aTeW7n3syKmcJr6IBENNMWYUnEJr8GHZ7if11ltkhTUktekh5dh4rwjNbWZ6o5ZRkiXOoIkf5DXdhTDXXSj7dyukKvKaUDQ-lPwfwo7lx4O91CQ3_x4xm7Wi0KmiiFVBltHZutY3ZpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=X0w_LGpsx20dVYMzCGu5xQrlhMcSdYN3Vbn62tvKE_g0jTIK2kcDcBN5XYTA-SfVxHv8SkkSnZgxzAit5nNH06CY0aNzLwnPAyCo5C4gsb2gU5j-tZubfCMvGD9xefA_VXUg_J0FDs8ZFP83bkfogeAk5mTLCa-8O8yvySzsjriuLFs6RBHjktpI7vQuFF_GPqIXSRtnD0aTeW7n3syKmcJr6IBENNMWYUnEJr8GHZ7if11ltkhTUktekh5dh4rwjNbWZ6o5ZRkiXOoIkf5DXdhTDXXSj7dyukKvKaUDQ-lPwfwo7lx4O91CQ3_x4xm7Wi0KmiiFVBltHZutY3ZpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور مکزیک در کنفرانس مطبوعاتی یه توپیو انداخت وسط خبرنگارا و یه خانومی انقدر ذوق توپ داشت که با کله رفت تو کف سالن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/91006" target="_blank">📅 11:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ded-9umeAAI1VelVTgxtfHbgAF5oEjc6jSXXitoCsm6hwr-XQ4YD_Afbbcr3KD0xSUpUDUNG9xMTfidJrrSrtuV1_Qog3-AeT7JxVR2kXIMB8IQi1FeomjlwtQmHqAOVOlYLs69FCPuIy2n8ZEBLUXj5JoUW8X5FXDGlO6wA-CGYQEy6hR-DLrB7tmZbAz9wqDJwNBqwxIwyUJDU5XMW3hd6ZbSYX0yMGPySdkkRl-s0uxY5lvkeV9mDF1eEs8etdiLI35weVPxo-TjXIx3KQ6FMbNgqje2QWfgV15W8yjEn9FMiqE2CQjrfqmUbW2MjD5hUfGeGAIMSu-AsVItEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ded-9umeAAI1VelVTgxtfHbgAF5oEjc6jSXXitoCsm6hwr-XQ4YD_Afbbcr3KD0xSUpUDUNG9xMTfidJrrSrtuV1_Qog3-AeT7JxVR2kXIMB8IQi1FeomjlwtQmHqAOVOlYLs69FCPuIy2n8ZEBLUXj5JoUW8X5FXDGlO6wA-CGYQEy6hR-DLrB7tmZbAz9wqDJwNBqwxIwyUJDU5XMW3hd6ZbSYX0yMGPySdkkRl-s0uxY5lvkeV9mDF1eEs8etdiLI35weVPxo-TjXIx3KQ6FMbNgqje2QWfgV15W8yjEn9FMiqE2CQjrfqmUbW2MjD5hUfGeGAIMSu-AsVItEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور با انتشار این ویدیو نوشت: و شما ادامه خواهید داشت...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/91005" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czWrgvN644A9BsDJMnPVLW0RAjITVu8wern0C3-Uao3Lcl_pWHc6LHP5NeokxivFe3qB9uLIXI3xTeO52rPrpJVuDgZ2PfQVxzOCaiuxorKJSaqfWnwAUGaJ1CLRWsrc-iaEeRWTKL716OcmujP1Z0_WF4aHUXVOok2ft0zSWOhBaq-x_RM8WhHC4fwLzmucbVw7_d0WOzdVdM8qeSI7LHeG3zKuGmNvjl0jd_em5lxeJpSZqORim7Gvdf_5ygsqSuU8Bz2gU3KddA6I7nRee4Jqvnpvgo8eeC-IWqh9cOBtWC9joodVnhgW9ZgYwtCw0x0iNoIiFy2fv1HvrRGZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/91004" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsFa7z8B-E0jp6U1Hjv0F0K72wIV1zCp53xU3AKaYQLmpu08bdM1NjFodN52lC5IB57NZGKOYm5-o3N9o2Kj3fx81YrY0-UwMJ54QoYP1w4rWw7sLIzC6KXzK4jGB-B9OXdRoM4tvO80rPuFQkJekl_OFZZuoXXwr6ISJl5pon6ovpv8Fwdmu0wiECLd1_KvMOYYqXkwTqtgclQ2JynAysKe7064W470JjyO1rH-9VBZlwANIrMSfmA-Fvxy1PK1ddWWchi2RTPJIVj7BogQPaTe9m_ywI_yZ7puSU25p4bmh6KZlheLZZ-xJ9YXUC_JIKdv-ytbWmMI5gXNHdV4HCvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsFa7z8B-E0jp6U1Hjv0F0K72wIV1zCp53xU3AKaYQLmpu08bdM1NjFodN52lC5IB57NZGKOYm5-o3N9o2Kj3fx81YrY0-UwMJ54QoYP1w4rWw7sLIzC6KXzK4jGB-B9OXdRoM4tvO80rPuFQkJekl_OFZZuoXXwr6ISJl5pon6ovpv8Fwdmu0wiECLd1_KvMOYYqXkwTqtgclQ2JynAysKe7064W470JjyO1rH-9VBZlwANIrMSfmA-Fvxy1PK1ddWWchi2RTPJIVj7BogQPaTe9m_ywI_yZ7puSU25p4bmh6KZlheLZZ-xJ9YXUC_JIKdv-ytbWmMI5gXNHdV4HCvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شکیرا از ارتباط عمیقش با جام‌جهانی میگه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/91003" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwdzxk20RPi296LZwGHw55A17Jxse7cBJf5z5ALL8yaetht-f0oAMeaaOOB3X27qECn4vCnoXqlaJNjAevquABwQ0ch47HrzyzzS8IsCEbS0p1VCI0ABTvl4jvCEoWxfQXWPHi4KWjvUKsdq0KqURazA3y95J0f5zGPtvWMCW0-OMkAFyRmFGTwZDxn47NU2V6sV8cPr_TYyNFm15nJsBsatD2dCcwWCUJXl8cXvaYhiz7Kwujhe6LDI8C7ODZNTwZixyctUMEoZ2nLnqgUXZeGKGjS7WxEfN6gCjdymR2aZghOz9Kkq0OI-aHpMrK5ywA1ElaPNam1BuliL0Vpvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇲🇦
پشماممممممم؛ رسانه‌های مراکشی میگن که یاسین بونو گلرشون در آستانه جام‌جهانی با نورا فاتحی بازیگر هندی ریخته رو هم و به زنش خیانت کرده که شدیدا در کشورش جنجال آفرین شدههههع
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91002" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=MJLeOtFVKib8GPuhEttxy6h7lNgN8s42dhLLvsRCldUJTxc8BdoV_0DuMYVrJuabGtERfxEYVM0rRKm_jeWKdcRb6iS4ckNWbSI_I18T8aUgovI_h4HNWeMD5qIBlIqR3rcjR5s62nG-ujKibXmQvoMi7Hi1hiny1_T9tjGBQ7rhZknSlKwCzdCRYiMtMKE_C-CdrxggLHG8NQd5KP9daM6s0_oq0-TZ_lCBGNj80xQSNvT4e1_hdUlFbZ3ZbS-tStlImGEgohnB03biRwaAadUO8Fbz2Zj6Z6J8H9NQuLppU9GjDFtqi7hSG_L5LM6hYscioRWNm1SfpR0Zy_34Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=MJLeOtFVKib8GPuhEttxy6h7lNgN8s42dhLLvsRCldUJTxc8BdoV_0DuMYVrJuabGtERfxEYVM0rRKm_jeWKdcRb6iS4ckNWbSI_I18T8aUgovI_h4HNWeMD5qIBlIqR3rcjR5s62nG-ujKibXmQvoMi7Hi1hiny1_T9tjGBQ7rhZknSlKwCzdCRYiMtMKE_C-CdrxggLHG8NQd5KP9daM6s0_oq0-TZ_lCBGNj80xQSNvT4e1_hdUlFbZ3ZbS-tStlImGEgohnB03biRwaAadUO8Fbz2Zj6Z6J8H9NQuLppU9GjDFtqi7hSG_L5LM6hYscioRWNm1SfpR0Zy_34Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو مراسم اجرای حرکات نمایشی ربات کنگ‌فو کار در شانگهای، ربات کسخل مسخلش در میره و با لگد محکم به شکم یه بچه میزنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91001" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiijI7RlfLrSm6zfiLhBhDX4INEihmJvL1-_mqIhM1MBorqpdG-R7-I7uCwWA19RDANK9kOHLtG-Oz3IvlNsbAiUcCXiy_zjtkh5JQrVClwgW8WpXgVzPMnGqaDDzkN9pFjnypPtAhNJvo2ttwwN9q1YqAimqFKTYluGmQtOIlmdkXDg8VRPbIWFRStiVjOyMtmygkTQOZYuDO-oYDu5ZuokkWsyWFD9w5h-yZbdAnd5NVSSewT_fNb0WHwmF5arKpxgkaMA8KYI9B3SCPhveJOr2dQV7MxUzzRGB9OjY_qUHZCVxvW05A3WhRpwuOv5kw7rkyKaK2zhAgPMzUZQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دنیای امروز به بالایی میگن آفریقایی به پایینی میگن اروپایی
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91000" target="_blank">📅 10:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=cIieW2VRm7w9Sxg2fn2kPS-_eB8oDYEENDwT20_yj7c9Jyj6o7VgewVWSVNGj7dP9S8X_mTxUNEhIoK24ElQIiHc0cxEWr0wwMbO-5uU4H-MpJU_263cDpgZQ8tL7kDh0yBeseYhlu2grWf7o_edmRBx8ggtORqhy0LKeHZKoZJaPo0XIMEEqfuS66Uu4nWTcmZucle_3rPXjmBn0GVUD2Am2mcOBw4QaDnf20ZOzhYgCb7BiDi_PFQyJuZ1ylyrJO1-gNsGrgHTPnTdxDQuS-iq1lyAuNYH2mUpN9CU--sQIroALcTCC1lzLRIqfK0o-FKQABwuAjSqO76lBEjBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=cIieW2VRm7w9Sxg2fn2kPS-_eB8oDYEENDwT20_yj7c9Jyj6o7VgewVWSVNGj7dP9S8X_mTxUNEhIoK24ElQIiHc0cxEWr0wwMbO-5uU4H-MpJU_263cDpgZQ8tL7kDh0yBeseYhlu2grWf7o_edmRBx8ggtORqhy0LKeHZKoZJaPo0XIMEEqfuS66Uu4nWTcmZucle_3rPXjmBn0GVUD2Am2mcOBw4QaDnf20ZOzhYgCb7BiDi_PFQyJuZ1ylyrJO1-gNsGrgHTPnTdxDQuS-iq1lyAuNYH2mUpN9CU--sQIroALcTCC1lzLRIqfK0o-FKQABwuAjSqO76lBEjBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇿
عملکرد دیدنی پسر زیدان در چارچوب خط دروازه الجزایر در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90999" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtaxoUyjQqq0fBrUXgA-1rBMsgxuTh0XzzntJEKcTq5Fs9LvLEkmL-SVFfktHuVk_s4wTRVk48EC_Az1ZRmAmWvDkxq8RBGXyV_YPMnHZoBpeePm-aBls49Yu0DfRpNcDrJlse7pZOaicau-HwWfiBLcnjr7Ob0FJqkWl0-J8920zrWZJwbJAlmrTT6-RFMZ9E4JUpaCsUV4REo3u0gNRulqNWOqi2BUvge5irDzMoIBE4ZogOXvnxqQkYlyKySDCCcLqfFTlZE9aNF4yPlMYfvS3vfxZsGwtUoAq5PXzDry2e2B5UsZrVRfpCcqpXNd1xWJ_PGL6e9mj4bu3eeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90998" target="_blank">📅 09:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDA-Mt459xfaLhuh4IM708L3PZoY34QC51MgWhQZRp5dup6mCWR305rnxNxeiulvg5iXC5YgY64ODJxJOLxpakbCbHzFbhiG2q6dSzldRNjKq9i-SeKpEUinJgzopcEc9gotkXH5Ve9luYcoM8BrnwzCZ66ujXm22jcFnkB3M0UDhKqh0y8qGBh4Q62ehUFJi5DoiNBWe_UhmuQRwlkm-62RBsOY1EEBvnCXXPl2Ob3ajUD9MYycqTJa8YZgeqeftJFVig-ULCPJLYi8fZkTYhGr49HGFkeUOjouut7PHAr2uBiLkG_vcrvEpdf8RaofFhYPl7QP8YikM9u2Kxt-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/90997" target="_blank">📅 09:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=K1DQ4MgVPGKHtoBhcFsYpTxgTD33Q-vANRjN7jysrfM5TYPFI0JngPniVtouRtKsZQawGwkqDNR3r965xJG5SmEJhufL3uBtNdhtFh14xKl7fhGm6rkeiBZzDOQQhdUufvkAmtrYCUpsbkXMcwF9N9htTMY8KhKkDnmS1smp07bSJY0F2xyVi1LsiNRxoEZylqTcfK_eUxv-Lhx4wXbRF_rsJDWzjamethm20wie1u7XXeu-1UxMB-FfQvlgBqDzSkILPQ4NlTtdKrSF_xTml7mSwYYYjPYuh5h4wP1OawtCgMn9HHezMQGkjQ59LtlHUhQMszGl5m0X-E2Eov4fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=K1DQ4MgVPGKHtoBhcFsYpTxgTD33Q-vANRjN7jysrfM5TYPFI0JngPniVtouRtKsZQawGwkqDNR3r965xJG5SmEJhufL3uBtNdhtFh14xKl7fhGm6rkeiBZzDOQQhdUufvkAmtrYCUpsbkXMcwF9N9htTMY8KhKkDnmS1smp07bSJY0F2xyVi1LsiNRxoEZylqTcfK_eUxv-Lhx4wXbRF_rsJDWzjamethm20wie1u7XXeu-1UxMB-FfQvlgBqDzSkILPQ4NlTtdKrSF_xTml7mSwYYYjPYuh5h4wP1OawtCgMn9HHezMQGkjQ59LtlHUhQMszGl5m0X-E2Eov4fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت مردم ایران در شب‌های جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/90996" target="_blank">📅 09:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
🏆
گل‌های برتر جام‌جهانی 1998 فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90995" target="_blank">📅 09:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65885deac.mp4?token=pIH_5IRWHBA4VWdZRwHtWUTwRRhsmEyaTtycABCRMehoRzLhnlr_Eq-dkb6Rrq7P9MV5bFE8NgCc0qtw6HsVLEgtSUAayT-tBNnZG4u95OK6LC82bXCCbYkpCN8YTnXfW72WIEBSyEsiEO68pC0I65oq-Ir09FR5l4Wkgp5QwNBLX9aWRzemsVBqNZmVtlcqT7m5k4f6iYjPKXl4UJ7zUjMY6ZI0JRIQo_Uzq1BMX-UYqIDTv2WfnSk5CBF5BSQBeXsqOL9k2tcXswIIU6lOyMJSXnkO83hbKdZZRLMvlTcPLMisl63avuz5YAY5I-shWjs5GZvw9zGExVnpUMaLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65885deac.mp4?token=pIH_5IRWHBA4VWdZRwHtWUTwRRhsmEyaTtycABCRMehoRzLhnlr_Eq-dkb6Rrq7P9MV5bFE8NgCc0qtw6HsVLEgtSUAayT-tBNnZG4u95OK6LC82bXCCbYkpCN8YTnXfW72WIEBSyEsiEO68pC0I65oq-Ir09FR5l4Wkgp5QwNBLX9aWRzemsVBqNZmVtlcqT7m5k4f6iYjPKXl4UJ7zUjMY6ZI0JRIQo_Uzq1BMX-UYqIDTv2WfnSk5CBF5BSQBeXsqOL9k2tcXswIIU6lOyMJSXnkO83hbKdZZRLMvlTcPLMisl63avuz5YAY5I-shWjs5GZvw9zGExVnpUMaLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چون از پست قبلی ورزش تو خونه استفاده کردید، این ورژن‌هم ببینید خیلی خوبه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90994" target="_blank">📅 09:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzusmD8_YMox6onh8HdYTWevGnKqJmlqoFp6hDkYQ_CBUxQnbt10srKSnlKXcGngVNv9t9Xo-B7sgGMCBLvt8PAaFkgIt50tSHs82CgRuKFwZvYqI3HucOa_3xOqBPRgCgOAPy8SBEiNe0IMYstU3fKHdCNryp0bLhc7DJN6KopdXSgGfqSuFxBdq39y4CL0TSLkVS5rXY-si6iBt5-8pgjb4s-8H1JC8ZCF1bkIrAdOJ_N4hDmKGi7EgVf02zSTy9p0E_PNOuI7GlfDTdAmvM724auQDzGLcKUEchTNH7E_5EhVXYevXmympoU57YNxiiGfrMLTC4vaZIAX06jSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهتون با قلب رنگی‌رنگی شب‌بخیر میگه
😎
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90993" target="_blank">📅 02:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خوب بسه بریم بخوابیم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90992" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
خلاصه اخبار امشب اینکه الکی گولتون نزنن. خرید احتمالی پرز یکی از بین نوس و ویتینیا هست. گزینه‌های دیگه بنظر بازی رسانه‌ای جهت وایرال شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90991" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cci-p--vrmyXnzoBgWuYeXM7CSaJDNbVyzM5Gut4kkiJ8V1PiGGC5moAeh1__cvSt4DhGoT8ifRf1dy7882FSb9rV0_KFUy6_ivEb6jmxg4luU8fMM0n5rSDn692KVe7cVSwU8Xnk686l-Q4wYLr_fbIUH-Xj0VZQrwBVS1hw4EQE6Mb-p3M1kgDRkBzzqJhrmvBQM6bt6rsNAvU5w7CNT1XrPi1-ewQY4fHiZTqOkQFo0IUhXU_mFT3ETxYpfIDFAeZsc0f-LzGBsLpYWbPZkJSemGbyqLBNyTeP2r50NBMMhMwcHpPIz98zPPFfOGRgkZC8Kq1S-Bauw0TWyQujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد ازدواج آنتونیو آدان و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90990" target="_blank">📅 02:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90989" target="_blank">📅 02:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
مارکا در سال 2021 :
🔵
⚪️
دو باشگاه بارسلونا و رئال مادرید پیمان بستند که از یکدیگر بازیکن جذب نکنند، پیمانی نانوشته ولی محکم بین پرز و لاپورتا که بر این اساس هیچ‌یک از این دو باشگاه برای جذب بازیکنان تحت قرارداد، اقدامی نخواهند کرد، البته این توافق شامل حال بازیکنانی که قراردادشان در پایان فصل به اتمام می‌رسد، نمی‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90988" target="_blank">📅 02:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua6RUSG9wVEoPjBzcI8JCf0BBWsPKdZqLEtAoXvn4vEz8s2xlczX-VfoqmlNA0n1mpwbP86f1fITuBEGOA_DP_XsE7X0umFroHSHLj7t3WZSdXakmPDTf1IkBzitN47I-iZbQZNzTNV3mH-CeJ4Gf6VepMvKV7VALTSdv2pZH1cY9O70QLXSHRm23oonRwrDcaACDI7b6wQRD-IKU8YergkTanYwneMvqDS9IvozkCUHTkVyp0viCvZ3jawEmImy7a2sWlZUniVIO2cHLJ4B3uwIqUxxKb6oIRgkOdcQtoMJ2FfTehwIqumy0fE331eshNJzNWurDVcn1q7D7tVnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#رسمیییی
؛ فیفا رسماً اقدام جدیدی را قبل از بازی در جام جهانی اعلام کرد. بازیکنان اصلی و ذخیره در هنگام سرود ملی در دایره مرکزی خواهند ماند، هر تیم در نیمه زمین خود [مانند تصویر]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90987" target="_blank">📅 02:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfeO-Yzv5foe7FZYMuggyIpNMUQKMOS2gHlfbMOd2xLoN8AZX0xM38dAVLUgh__nqSk0hL9jRH4KcRVfmC022YIam-KbZ1oHRU6bo_gPzoHlE0B510lTpYa2ccugIco4DedRAP4oVoudQmBWbaaBwNCkTcVGxfVbrXcxNw1kSvcXEETGnmOWvoQOgEZjJCj23dRgNU75SAiBhy1ez2t889KWWnPOifJSzcgL2OAC4t0zHMhk_YxunXXXtbQv_bYCe9f-HViunqHlLGtCWHPfMyqyl6hHCI2JB46CwcKttjJlQd90U5oA98_dLoIXMAa_f-rXDbxLzS6DT8b42exUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😴
😴
محتوای خواب امشب رئالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90986" target="_blank">📅 02:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyK79gGNxad1VpLOTxZ9qJbProzL9kFxwkwJwipchOR2cfY0wME8LOGUm708bKkpnyeYWxswGW87W8DI8GyiHOlNtAlUzYdriNvsE1aDCHdc4HdD_n6zDR90rpKxd78xuJ-BodVUG3pzMRnnh-CG8m5WW4pT5tvbDIeLHBv3GzSgiL1Vk0WeV8AxDSlyxIqONcuwoyM4YbY0_6ZgNfxa85PsczZIu9LWiBbSjM8b20f7OxFb5lUYexylyIGRiVAzthfwU2ura-dN6JcZygh_adhScH_rRwCR0Gv50M6itTCS0Z2UzH8qRdE9QEJxijhOj92C6ZU3IHfIZzmiU8NO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90985" target="_blank">📅 02:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90984" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فووووووری
؛ رومانو: پس از جذب کوناته، رئال‌مادرید شدیدا بدنبال جذب یک مدافع دیگه رفته و حاضره رقمی نجومی پرداخت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90983" target="_blank">📅 02:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90982" target="_blank">📅 02:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXRAtXE26aUlymYS2nD570mDgZrRSxhzD9_-NaddAHMWPAkN5GQV_rFIfhyHqISCd48PRTQ0hlHchN7o_41BGVHAAkBz0NNFsP8pZIaRhafExqGb9D7pfqd9oS1b6sUkQWe9fpY8-H3UIkuhCXkINLEmcHS37pfTLqDM5c87oQiegrqRteOIB3MbNc0nuwj2MJ36-RTLhqvx1bvrQ65IOYKNyOPLgzNTfTf-7eN-Bnxwt-vxLnvdP6Lqh9mf5es0ILfSb61u5XA4Zda_Lx9mU7c34JcNM9T7yoIEJH1vNPpVi3DuCm-_3vsySJqZa9jvKCRVLbFaM5lYSXxfOi-J_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90981" target="_blank">📅 02:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فوری: خوزه فلیکس دیاز گفته گزینه‌های مدنظر پرز، اولیسه و نوس و ویتینیا ان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90980" target="_blank">📅 02:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
وعده های انریکه ریکلمه قسمت n ام  : اگه رئیس بشم دلبوسکه یه پست مهم تو رئال‌مادرید خواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90979" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90978" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تمام رئالی ها منتظرن رومانو زودتر از سه‌شنبه بازیکن مدنظر پرز رو معرفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90977" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E_uHZ9-lv2tx9CzoMJVECYsj1PgSd4fofzZgAMoyx8niUvULtYQwqA8B8cOjIweP9lTX8f95xETq5hRrirRDmTfvO4-Qkg9I7lVbFGuPWNeibgq3xnpGXnWvcvmTYEUuVElLhu8RTOBNf7D66wfvtMkc6K3rwzMgSOmrir1QCQbf-hgj5r9LubwJ4SCxHl_mShHEsEjPDgDXqF1o2D7FT3nh3HHfUf1LRaTYjX-JXjIINWKk65z7gQLhnJTY6bbHffcI-y8GocIWT24LAN7Zt864JGGFYEWqrRQIVzEhonl0VZfzwhKpKFKqmhCfakG5X00UzHu44_etfTV3l-bLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90976" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⚪️
کوپه : این 150 میلیون یورویی که پرز اعلام کرده پیشنهاد اولیه اس و در صورت رد شدن قیمت بالاتری اعلام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90975" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTaQgy_BFzfRt_5kGw01-Aa7HL7VE6pFPez_iaXDGKdSsS9I0Nf-P2lgyz-XotQlrvgp7ibUIRUqbC5ZX8o18pQcMtuldt_9PBApKEqP-1Efv7IBpcsW643wmd5iTFuNHvTRFfHkjDlFeuThOt3dTm2zgZDaRZCfG0cz7q0qdRHK1UZGc34fNKvqmWZ6QKsA5oSEjNIpSpnZV_NikiY4yl15oWyi22TI3iDlfH6B7UaWoBAmhPwbxZPJRsohBlVZ9NNEJG7jpSlBS1VNG-SHkd7OO8PfjFtFVWCZhLBFpp5jrBKA5S6lpiIkTcnfC80X8sDba_zx16Wok_VPg6bFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90974" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5cGEVfmInDKckqmQAyOusBxkNpY0qvlmPZeG9eJm6YZeU51fcgCT6WkCWEQ5A-IEJ6arffdRSKaGn1_Q7hrJPb3KZzUqM6UBttOKCXNoVrQDKZWZSGZAdI48VZWCukf1agwPOoe-jK0AOYA3U7zFlIVDSbZXZ4PaAHXMIe4T88NFeSc0NOXNLsX6S27lLCm8XsIjx8GwTigGMHcD05_II6_NfFhCWa9sW9UuvL6oLEUGfKsgp3sO5uYtAHP3zJ9El79hxaEcs-mJBpYtxLzrnJyYb98tyFLHkgAK4RKIVpVds8wh9DJ7MA1uQLUS9Ti9tGgNePQq-zegnwqWoN38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت جدید اتاق جنگ اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90973" target="_blank">📅 01:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WrQDzxMLhCBDcW011VDAHZCtR2LpXNZAi6Ywe3Xp960qUbTnmY1DP21869ZUaP0hbWzpvUJIi0ZsP_6DkR3DGBYXKB4IsfuLOfjbIH9hsFrngyzHuvIdAOS-4Pmf8zjDAPuc6GVlLmUEw6eZAT3y_FCXslCU1zIeubAAzv4AhDU5RsKN4HRudJDAAx7Hnisw4K2glNBB8J3PqbEKUpDy8pnIy1TyxOduB6tswxeqTxlSjA9NvmHMdwYz90DWBIGPXFe8jz2rHVl5jeFTnYexbMPnDN0KunonioNI1JlIPsH2wHVSn4vJpDGLy5EkF9PPp2z7YkLIoc93gX-WAKmrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90972" target="_blank">📅 01:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu6vQgti-kN1nQXnH6o3MtydlokW3y6YOB8Zq7WdILs0ug-2mz3FUUFkvgKzqCu0UC6MHCtqV7jvtm_tcoWX46AgLnY8IZ3M1eBz9icMZ8tc4usPZhtIkBhIi6RTcEuJmo8ip4np2NAhYYTzX4nm60omUaSUD3_VfUpzNv5AhOrrsmcO0Zj406rf1rsd6YC6hRucVvvyAftOz4aiW-3pdrHRKaT7KeEg4WpREXgHzAp5TTLwMAakjMNSAchKzkiEKKfvCaZduLu7xZnW73_Ny1ynNmmaiStwcLMZpEuGJV1XVjLvKIrXLXsMBx8UWK6rYUvFnQQXmNs01rJzFAcWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
پرز نسل جدید کهکشانی‌هارو استارت زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90971" target="_blank">📅 01:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ولی خودمونیم ها   پزشکیان هم موقع انتخابات ازین حرفا زیاد زده بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90970" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90969" target="_blank">📅 01:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3myYI4seBswK9XW-KcHWCVxNUBIMpaOey5g9JAU8fAnCQCCfvosEWQ_D4h_t1BHoeRLHpD4WQeHj-5js-vUuS7tWLjv6ccAuEjwCBawi9I0EY4OfgJtRtCMH_NIaKXArup5kj5LSDg0-BAa4nFw83xKmkjqa0WkwnqArPyH_0OLjLgQlAy7LJAvkqS0SIkTav2H6tRRq10Cb34DtAG1Q8Q6-wkrZSYCFK8SEU-3zBFkjaX2vWmtznvg6vGsMDE83utZ8csrYlBn-lPrQ-zBCzrp3pfIqDgv87ZSQfao4fHFKBHcVNHIGjcvsxguYNqXHdlTHLR-jhORILwfjxgOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90968" target="_blank">📅 01:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">لاشی دنبال پدری نباشه یوقت
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90967" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90966" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری
پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90965" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IMCLKyAH00VramnZH2lOUMTVKW9RyPR0ZFiZuLVO9d5yeZlahtPzamQ0N_kpIuCrNpw1gf2GYn8a6meIzBmFCjQbq85fL0D8-_yvK7KoKEim1fUaLRP9DPZuCYiEwZkyy8pY46LMk2Zro-S4mvlZlBZqZXgKodok4FIxAw-2uW6Ha2ZuI53tr7RS4g4KBkKZof8zBclvVecQCer-wspjLBdmfY9TOKZsbELSbuVnyM13QZH2CNDWUk-00MtoE3OjUQEVr8w-MNUn43jPvArNJ98zP_tNoaT9-lSCafZqcMkCvRNa0NoHbk06JN5q9nQbJk2zquvc8ufgFkk6FY4mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فووووورییییییی
بمب پرز لو رفت !!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90964" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90963">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ6FCNa6gO46kg3LTuHxzM16uPY_Kj5jZqMWHjHX1sczOx7yOPNZTXxJTjhRFXxGm--luOS5On6cn6iIUA9H3y3nzLXIsesiNmofSBCgv7_Pi56FKvBzXXcIep4-LiQnxfjDvTzBBROo4c7B0L840pRU316HRAK99gOkb84UL0es1XXRG5R0t7SJsbM-A6aT-hDdL0871wQQVNTUlneJEmS3fd4RfNsqiTO2hTJV1-rRZR2sgEQHFk5iyWwYlwt2-jUni2dhSX18fzcY42az2ngaN7c671e9sX3pC87QrZ_Y1TRmeOwly5FR_jI0ZuKxN6Nh18_OwVjtUQJZMJAPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90963" target="_blank">📅 00:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90962" target="_blank">📅 00:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90961" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90960" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90959" target="_blank">📅 00:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90958" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🇪🇸
فلورنتینو پرز: اسم آوردن از هالند یه حقه انتخاباتی هست. مورینیو حتی اگه ستاره‌هارو روی نیمکت بذاره کاملا تحت حمایته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90957" target="_blank">📅 00:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
‼️
پرز: این فصل هیچ درگیری بین بازیکنان شکل نگرفته و هرکی هرچی گفته زر زده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90956" target="_blank">📅 00:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruSQWIctaR6J10Q-kZ-VGUN-BbTS894U8gnnX2h3HYyOj80sk8FUOn8gQhEZWtZ9jC2HpELGF3Vf4gtUXwyXvlUek37iMpPQ_-mPs4-irjEmDwOJNWelvlJ79WtKu1t3Dodac5_EO4ulRuosdZ4_7ss1EZcqG7RfyFUoxDT2rZGLb9oI8kAAkMqoZeE_NefMBo1f2mkkGEz5pKccssKNWkPq701J4qC42SD_OTn-t7osXs1P1Nrkzr-GibBlwA1sxTTuk1BjbNm-3G6amBRjAFGbin1LKMMNKqA7fyT-c3XJkjID-eVpUJagcjKY8CIsioeLoTnYC5XZodB1RErbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه به ساحل‌عاج 2-1 باخت.
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90955" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">▶️
🇪🇸
🇮🇶
خلاصه بازی امشب اسپانیا و‌ عراق با گزارش فارسی خدمت شما عزیزان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90954" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90953">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
پرز: همه ستارگان مطرح دنیا آرزوی پوشیدن پیراهن رئال‌مادرید رو دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90953" target="_blank">📅 00:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90952">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=lVGcumfOEaJEB1CKRek5pwgYcbSoRTN8iouLqcmuLl4I1vf10gv1qsFRB5k7Kczlng1XT4zhsbxNPMvZZjBEKerxwGy4vJ8xSkSz3pFWC-t33obmXFNokRyQgn96xOPHNacY5WUMmVVmdbO9QpU-EPO52q9vw1R9SfohUN78VZ19opn6pf0Qh1GHyi9qCOuBpvs0KyuH-VVmc7xoLYt5wq7Ts-Ba_6IGkbYVcxDRDGcXCytMtE4QK8F_KJqEXtLOIhSIlmZwhS8OMbaJiOOWTs6UuToDrHc4cah79v6fVEzKX9nytTySXuPA-2nhdBuLP48p0zcJh5WVlKHLGMyL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff5287c9d.mp4?token=lVGcumfOEaJEB1CKRek5pwgYcbSoRTN8iouLqcmuLl4I1vf10gv1qsFRB5k7Kczlng1XT4zhsbxNPMvZZjBEKerxwGy4vJ8xSkSz3pFWC-t33obmXFNokRyQgn96xOPHNacY5WUMmVVmdbO9QpU-EPO52q9vw1R9SfohUN78VZ19opn6pf0Qh1GHyi9qCOuBpvs0KyuH-VVmc7xoLYt5wq7Ts-Ba_6IGkbYVcxDRDGcXCytMtE4QK8F_KJqEXtLOIhSIlmZwhS8OMbaJiOOWTs6UuToDrHc4cah79v6fVEzKX9nytTySXuPA-2nhdBuLP48p0zcJh5WVlKHLGMyL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇮
🇫🇷
گل‌دوم ساحل‌عاج به فرانسه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90952" target="_blank">📅 00:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90951">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90951" target="_blank">📅 00:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90950">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjwY-JXw9lQJgoINOdLsQ2sguJSUby9wFsWcEic1Ub57ASroDh8s18IXlIyw_nq8JUOk-U20a5W6FZtNucrW4Www1YKsx1iNmhYrhoZC2ndVzSuFGxi0htKcXJZ2z2tbmFQ3YblLPBMMKtTnW3h-7juSRG1jEh0ZfNICZGyWIVdU2TLXYk4JUgTWd78bAl337rmPDTkYmHgNDvsuWbdhAC-QMLjQoWmlo1jYU87vJ5Fj3Sdjkk2tzshphA0yH8q1QZaa_FhNHMsEiNyitI-ZkvS0iIh6QKRzTRdPztVplb9qfPX7tf_U7vnEfC2BH_KGV2bLonD2TFgAkhxlQLB_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پرز: ژوزه مورینیو از اومدن به رئال داره ارضا میشه و بزودی میبینیمش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90950" target="_blank">📅 00:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90949">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90949" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90948">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut2wvRE9CKdEJkbb44Twvvf1yfznb8NXOSUb3tJhRhT8yn4GSFgV1M24_CCSEpmxqSnR2fw0PTvQU4RzNf0NBRV_hkewuGu2e8XSdLJtRfjtC_908RiYwC1xyGCNrEbszlPoxEAPH-MpSiXjwfqFj3xsutkKW2YPpbZxgjZ1nEtpvJwt5muSPfcK7qCMoa8wUhYr7BAQOZy404X8-KX2X2KXW_nCtfJeHGXPy_KdD-E2ROEVY6CQLM9xR61-1n7g6Qp1sJ0YGICgi3ZJE0wsyDHAJpRvl8JuKxH2hyuq5KW5cyvv7f5bw-ZhsH8ZqAj3qZxf2wkNCJk6h4zqM76KwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فلورنتینو پرز: مردم می‌گویند من ۸۰ ساله هستم و باید به جای رفتن به انتخابات استراحت کنم؟ پدرم رئال مادرید را در وجودم کاشت وقتی که پسر کوچکی بودم، و احساس می‌کنم باید به این باشگاه کمک کنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90948" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90947">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2wckD4d0VPZ4l0OqQ0bQLLxvDj8Rqf12Hc3GwjvKX8pBZX7b9kZMifbXEiW7JZBpT80j1oiK_Ziq35qE4pA5jDL9RMLR9UZh1x6hNtBJopq33KfgrnJWpYvNKwGpdX3ER9OIaRMbw8KOn9j77YRRK-QjuocWMgYzpgJlGKmXQnNDBhzLDpRh3Z7RpbLUjN2WCEpxs1kEEKMouZuTN4gB99iaHLj2LUL3HrG6n1zj9PuS2j5I0fNKTuIRPa2YhHETCZgzsAWrBfi7bzF0U06hfr4Mg1HA-E6WXNhj3vDFlMvpzzR2qFHNWeHztKLZXSCHHkK-znM_u74FykMb5PEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پرز اومده مصاحبه انتخاباتی؛ صحبت‌های مهمش پوشش میدیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90947" target="_blank">📅 00:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW7llOM9LKK9ZLF4ULqF6mnA4uicvrYzy6agd2xr7lnWEGszuRqhvBfK7d7gisMcUEydTtXaxkMeKqfm4CNq1RtHrVhKKj_pW9YF41DdNtnup_51-MDcEoZ21A8VaM2JPq0_BWSs3RULgOmuMBk2F_YWD-X-RfWyP7bo2ab1hW7hmIKNyTWQWM52phMHS8_tUh4SfO3-lekRJ9k3nxGV83cbFlA70l-01lj6wNOIuyiFc5Hr2rig1zBHvy6w0Qp_3gfBsxF7F1VhLy6iz06PTqrAPooR2caMmI5MKXklO3mUM2LMeicbslwNFROQXxdMlnajROL0SAMxL47nCv4dwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇶
🇪🇸
تیم‌ملی عراق در بازی امشب مقابل اسپانیا به تساوی رسید! اسپانیا قرار بود با ایران بازی کنه اما بخاطر تحریم کشورهای مختلف، عراق رو جایگزین کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90946" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90945">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ایجنت منیر الحدادی:
ما هیچ نوتیسی به استقلال ندادیم. مونیر به قراردادش پایبنده و هیچ گونه مشکلی برای ادامه‌ همکاری دو طرفه وجود ندارد‌.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90945" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90944">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
😐
قیصر خواننده قدیمی آمریکایی‌نشین که امروز پس از چند دهه به ایران برگشته، در تجمعات بسیجی‌ها کنسرت گذاشته🫪🫪🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90944" target="_blank">📅 00:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90943">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=Th9x66AMLnUUtwI7ZonsmuuPc1dV6U4mzQgxKTRwRmP3e8ThL1qMfEAITuo7iKB9Lp57A7xNN3tnVD-7rARkdd5f_LC0IqrYTxbsCia_IFQgaosgfYtVW1Zn-AqIgAGl24pkO5OogegmclEBNwJ9bv0yNYwB1n_6xIR2DS84GY4kMbXJKxZn8YaK0LcwEg0-uVyotK9Sx2ChjJy--tY9fHqAl_sKOo77fAFkLFIbDQcYtDijr_8ZRPSBMT6NAZLWwrbKYVaRkPO09bhxM14uIvMOj9Ka2BT7IF-fd-c5Y6SJ8YaYY-pGcLnCctvCeBcj15Lrbbk2dRfX7nEehtJpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7dad01d.mp4?token=Th9x66AMLnUUtwI7ZonsmuuPc1dV6U4mzQgxKTRwRmP3e8ThL1qMfEAITuo7iKB9Lp57A7xNN3tnVD-7rARkdd5f_LC0IqrYTxbsCia_IFQgaosgfYtVW1Zn-AqIgAGl24pkO5OogegmclEBNwJ9bv0yNYwB1n_6xIR2DS84GY4kMbXJKxZn8YaK0LcwEg0-uVyotK9Sx2ChjJy--tY9fHqAl_sKOo77fAFkLFIbDQcYtDijr_8ZRPSBMT6NAZLWwrbKYVaRkPO09bhxM14uIvMOj9Ka2BT7IF-fd-c5Y6SJ8YaYY-pGcLnCctvCeBcj15Lrbbk2dRfX7nEehtJpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل‌تساوی ساحل‌عاج به فرانسه توسط دوئه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90943" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90942">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🙂
👀
#فکت
اگه ایران تو گروهش دوم بشه و آمریکا سوم تو یک شونزدهم میخورن بهم🫪🫪
☠
☠
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90942" target="_blank">📅 23:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=VWZYz-5jsGKuXonMNNjTz7k2jAU8DXe7D0hHUn_CDTpfRh4tmArEBgBRTvMqDrL15R8562CfhzpRC67JBsV2jR_2e73ACsahy_N3Zm2AOxp_I4BHhli-bDaWLySf6fkVSUqYmQFkrBFvM90KuaPyaW06f5xilbXB4fEJiM4d-ZW_E8I_GpH2nO2CVj1Fg5rtV_qmnajYgJbqKSpQHtITYsE0Ps8FXHm4HkdC_1RwaiqywS0WPPn9MHCA0tO-jTm9BUX84mzSt8sSuZrNxbrZEdbCu_BLuFvfjNl6ZvDlhujAekCM3OMmT4sbd2O_BfurGqmOlrew47Sx7oXvqEgFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de9f07d6e.mp4?token=VWZYz-5jsGKuXonMNNjTz7k2jAU8DXe7D0hHUn_CDTpfRh4tmArEBgBRTvMqDrL15R8562CfhzpRC67JBsV2jR_2e73ACsahy_N3Zm2AOxp_I4BHhli-bDaWLySf6fkVSUqYmQFkrBFvM90KuaPyaW06f5xilbXB4fEJiM4d-ZW_E8I_GpH2nO2CVj1Fg5rtV_qmnajYgJbqKSpQHtITYsE0Ps8FXHm4HkdC_1RwaiqywS0WPPn9MHCA0tO-jTm9BUX84mzSt8sSuZrNxbrZEdbCu_BLuFvfjNl6ZvDlhujAekCM3OMmT4sbd2O_BfurGqmOlrew47Sx7oXvqEgFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
میکاپ جالب آرایشگر خانم خلاق ایرانی با تم جام‌جهانی ۲۰۲۶؛ حتما ببینید جالبههههه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90941" target="_blank">📅 23:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=X2a_DboLdbvgq8PNqnBwKDlbLGdFbhKF57phT7HnQej9TnDjik_yVXPLRUCGH3Y_In2dLp8y533XCvGMiWEb3JEVITnSxcs4gXCh9NBbM-vVBl5awskWl9XYxO82y0Jkgcl5LO6W4mwrpuuuKH-8gzyZ5XmTDCx5c-wIhcclY3BU6D_kRc6lt8e_HkiRaFpdB1K2TgwJ825NePJyPuoblfdj8cIhBne79K9zvgZSUBODDAiV-7nHIHlOi7j-MkbLL4CdlNyCGIL05DiklCXSSZJqOgjwVPDenEav3C0uifeIrf6HzwfikkA0D5GrrxSkLOHD3UmqpjE5bjmpjCFeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c687b5ca.mp4?token=X2a_DboLdbvgq8PNqnBwKDlbLGdFbhKF57phT7HnQej9TnDjik_yVXPLRUCGH3Y_In2dLp8y533XCvGMiWEb3JEVITnSxcs4gXCh9NBbM-vVBl5awskWl9XYxO82y0Jkgcl5LO6W4mwrpuuuKH-8gzyZ5XmTDCx5c-wIhcclY3BU6D_kRc6lt8e_HkiRaFpdB1K2TgwJ825NePJyPuoblfdj8cIhBne79K9zvgZSUBODDAiV-7nHIHlOi7j-MkbLL4CdlNyCGIL05DiklCXSSZJqOgjwVPDenEav3C0uifeIrf6HzwfikkA0D5GrrxSkLOHD3UmqpjE5bjmpjCFeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشمامممممم از بازی امشب فرانسه؛ تنه عجیب فرانک کسیه به داور بازی باعث سرنگونی و مصدومیت قاضی این دیدار شد.
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90940" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=hoa_c1kKEKVWVGP57wgs0jC9Fg0ZMxq0swTAv3pERljQ4q_gmEsJXpqYVfGgFcfPduStPRchxwo5vyewojxCufVAnjwYokPvGfvmmPsu7SKApOImDgSSfXUK0ZZwDlGHxbTVd3Ja6jBYK6lHF6c2Y58i6yWpX8qoBDGrSw476eEeMjbe0Jp8P1-J_pnX5aJ_m4oHCd8WAc2uhksArviqdv705fBdnfjiy_bNKULRSvTpXayH9i7xtslfAtvovSrD58mcpD3JIGeW2fLtsfTnjbUVBNm_Nn5emeIPDpUE3L4eo8w51IugjjCl7aP9uizs6nfmuRgh-4H1-KIesXI4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cff28a7c0.mp4?token=hoa_c1kKEKVWVGP57wgs0jC9Fg0ZMxq0swTAv3pERljQ4q_gmEsJXpqYVfGgFcfPduStPRchxwo5vyewojxCufVAnjwYokPvGfvmmPsu7SKApOImDgSSfXUK0ZZwDlGHxbTVd3Ja6jBYK6lHF6c2Y58i6yWpX8qoBDGrSw476eEeMjbe0Jp8P1-J_pnX5aJ_m4oHCd8WAc2uhksArviqdv705fBdnfjiy_bNKULRSvTpXayH9i7xtslfAtvovSrD58mcpD3JIGeW2fLtsfTnjbUVBNm_Nn5emeIPDpUE3L4eo8w51IugjjCl7aP9uizs6nfmuRgh-4H1-KIesXI4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به ساحل‌عاج توسط چرکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90939" target="_blank">📅 23:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErUrPJ39K4bcL9BFeLD2UPzIf8_0Ne7_MJHniShzx_JKgpz6InzEp9mWidkVV_qwXd63jI_ga69G5rDjw4i4PhDcfZxNEdScFJ08iLeUOM2uZF3t_y4VUtwEzjaaIfroVeIdE22ZidcPPeCn9HV8EbDFqePCmQs_TpFdI_yY1g3n-0NpfUCjwbM8k9-D_mqoV53bhakxLv0VR-S6BUoxHWK-aMfAxtiy0zCh9QrREY346FBWXKxOY1Xw5wHBUjgl5aVetocJ5uaNZRdV7ZHDQOu9TvYkHUljwErZZR_ecTIs0oiIooNPbGahti37-0jrs3iVUYK5ChlvkGJ120iUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#
فوووری
از ESPN: خولیان آلوارز شدیدا از رفتارهای اتلتیکومادرید در ایام اخیر عصبانی شده و برای خروج از این تیم دست به هرکاری میزنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90938" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIbuyIulL3IYlr8WxIWV3VDLy_Ck9zgB2Gex_c5pCSgKoCoN055tM30ivFUKNUgnApZvUPoMBPzZ4dnHGXKgTXjVvkmeBGTUBYMaG4JG6reaZy9q0SLBbMzhdudSs8h2tcgXK8VIVNA176KljiTEeV7kAuRPbYmP3snU0jr-NUprzwk-5p8iCYbTtwD0Jf32y73VwKPbYWaoyx53GL-CBI9ZpvczhSWsSyuRqJ4JVHnSaIdnG6PTOcHX0VG98Pu2Mnmn8mjNMWVQMn3mdRpTP1e3iKL3iFSPeP2yUt3aIpolI5PBTvSXtGOdIX9ij7QSjFjIFkiIiK2Wu2KJxGBYMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90937" target="_blank">📅 23:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=ZZppN-RvrVFlRIWqsUfogokREyPcFH0jZwY30bp1nqNSXbFuh0S0TaF-ZPlkv0N4km2-3sEq28LpdvRvgOEKEDa9XCXcWzSlqQiLPTXEHR5meqcbepGOZ41m2opuhqTrZ4LWw8WYuP4QPPcy3O-T2hE_xt1pQdw3lFtYqR4llA-zWvZWcrTs2pPq8CYazNiipc4b52ftT4xSLJNfVgk5A_nF-6bwNFecxdJmmSmfUP329_K5dmJRg_wDcVIezkXAzRM2myv0GCqtzYPKO_2fYzZoIt_jojebUWE_dBe6pIhz8AQIlHukDckHpbib-VbHdWOCfLwVPvsRQoLFhP_KWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db661e26bc.mp4?token=ZZppN-RvrVFlRIWqsUfogokREyPcFH0jZwY30bp1nqNSXbFuh0S0TaF-ZPlkv0N4km2-3sEq28LpdvRvgOEKEDa9XCXcWzSlqQiLPTXEHR5meqcbepGOZ41m2opuhqTrZ4LWw8WYuP4QPPcy3O-T2hE_xt1pQdw3lFtYqR4llA-zWvZWcrTs2pPq8CYazNiipc4b52ftT4xSLJNfVgk5A_nF-6bwNFecxdJmmSmfUP329_K5dmJRg_wDcVIezkXAzRM2myv0GCqtzYPKO_2fYzZoIt_jojebUWE_dBe6pIhz8AQIlHukDckHpbib-VbHdWOCfLwVPvsRQoLFhP_KWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل تیم ملی عراق به اسپانیا
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90936" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فوری و رسمی |گل‌گهر با رأی انضباطی مقابل چادرملو برنده شد
🔹
کمیته‌ انضباطی فدراسیون فوتبال رای خود را در خصوص شکایت گل‌گهر سیرجان از چادرملو اردکان در خصوص استفاده از مائورو آندرس کابایرو آگوییلرا، مهاجم پاراگوئه‌ای چادرملو، صادر کرد و براساس این رای گل گهر سیرجان در این مسابقه ۳ بر صفر برنده اعلام شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/90935" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90934">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تاجرنیا:
فصل پیش هرچی اتفاق افتاد مقصرش ساپینتو بود نه رامین رضاییان و غیره
من میخواستم ساپینتو رو قبل از بازی با الحسین اخراج کنم میدونستم اگه بمونه حذف میشیم ولی تو جلسه ۳_۲ به نفع ساپینتو شد و موندگار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/90934" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90933">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDF_TxtBGWbZo8bMnR2zYAT9OFf1QALlaHkfKDqQz_jl2IslBE7dqN0YAucRPQWzMM5ojqe0RidLrr39u3gJTBAHiwmKq61WXbjGxmXeIUNGGZ-txD91UsGjsdMjZXD6cIPjvQnWWL8U3L7D4W4eYgsIUA8kPvXgZ2EveGvMavoG8RxmfFhP1gHSsdPavkkDtAozy3NomndlsVJzmBWRoJHy2BWAQN-u7eVMT7tjHx8Cfy9b_06hP8_my-RSXGQfcxsG6p7g3hILHHRTkgPSO25c_iaT2Svxfjz-kgyJJ26zu053diEVf6urklItOA9vGRLxkn5UqG9vX9tMCabjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییی و رسمییی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آندونی ایرائولا سرمربی فصل گذشته بورنموث به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/90933" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2MA45vYN9cyQ1VebuVkxnSEMM4AbfmygtqWRC5VaHp14sQIuj0ufjvkNiNxpvA46n8SW30Fx7cvjfcavMiQz-ZVKzASeeO5z42IBXoxFp8F8vXPf_O9vgGiZD0Z4XDjvDWEe_TI21ZJ5Gjq_5H3YfGT84h5d9II33F9GAgadneJBNfhrT8uyELW5kES8_zxdkyQ666SIQCkvF6l6Wn_PvIph2u8Ii8avSTCpwy-NOvPyt_un3JtJV-_rBurtJDSZ2scEni1LAah6xrpStPVZ24flnfstyXeT7ZPmGhCl8km6ty7ZE4xgslM5Qb9AqxG1h0bke9_8b3pFJvgHpWfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با پیروزی ۲ بر صفر مقابل مالی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/90932" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi3ZbFx-VDOwyPBUtmwweVwEJU8hP4rF4LwVqz3RmoWZnvkSnYLYck-Zqduym1i4ghhZiL0lJw47BX1BBtfhIxLYirSUfL6PLDjKP3Q5zJxv8-jHjmDFWXHWSSmCyK22jtuMnEr22b_kTN79lFQAonNZcfQAo8Um8xQAQrjwawjAUQr08ecbsQv7CAm6O7wlDeRWEUOeWA4Hy17aMGyw8sKfEyiFbxH_kGRWtfZGBYMJ4Be920kNCZNMOR_0S0dhuNb1dKwE2DC3Vs_GFq913Z5SJk09Fs74808iBdfIBzJQPkK8Kwh7ucOn0q9O8S2xJWDRDRL6i2fsLfDkRMiI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پرستاره فرانسه در بازی امشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/90931" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312570c50.mp4?token=b0UvBlAS1eQKipk5s0IL0rorlpG6xwAYwQg-CNPmb6mDaOQI70-kUJZ7ihU3GWdb_JfkpKS0E172ZhLMJFMliX2AemZKzehkV2s_3ZMQ__wFGXcwU6DPw4CrV-BP--Q_AmmhnEhvtoa19zjVd_2s14e5f9qHkaQmIUa5holYNp05WM8073CM_jvCv7a26UorwYG7EP6bmRu6-IrqOI4WLE3S-kCiAPk4ptsw824qBCqsgSpN85crquo63EMQlsFwRvLNjLCbAyJcevic7wqtnb4E0QKMZze480GZqIwzxbPFXGH-Oof8iPsDcEw_pWNcrxi5lbH7HzdHlNHxHkYUN1YKRiJPCfbY04h9kgsFm_gVn6B7JHSKiEjK0BRKsd794DHxZjDWDyhr6J9SFcEOZKzrcDJRjfuZieJszu1WncQPnZSfc_NLDoekb879a4nTaHwEYaMvrt2-XVzpWVV7j-yodH3Z9OLvTUFvtQeSyOcu3cPdzlAWR2_83U27rZEJ78T_YPr9g6fRv2NDcsbfSn9wJKQ9EOyoyzI8Wo7dtAcnXcmA1LjYErHRW2_B--gZyrUqvPYvit9nNFRbqmrtvtcfXSX9OkHlG5zx6i3i72xbEEGZesbXuafqY0d9SPTEzwMm3LcPXNvbBb9h5ew1e2h49wgCesTuFEWnNqrff4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312570c50.mp4?token=b0UvBlAS1eQKipk5s0IL0rorlpG6xwAYwQg-CNPmb6mDaOQI70-kUJZ7ihU3GWdb_JfkpKS0E172ZhLMJFMliX2AemZKzehkV2s_3ZMQ__wFGXcwU6DPw4CrV-BP--Q_AmmhnEhvtoa19zjVd_2s14e5f9qHkaQmIUa5holYNp05WM8073CM_jvCv7a26UorwYG7EP6bmRu6-IrqOI4WLE3S-kCiAPk4ptsw824qBCqsgSpN85crquo63EMQlsFwRvLNjLCbAyJcevic7wqtnb4E0QKMZze480GZqIwzxbPFXGH-Oof8iPsDcEw_pWNcrxi5lbH7HzdHlNHxHkYUN1YKRiJPCfbY04h9kgsFm_gVn6B7JHSKiEjK0BRKsd794DHxZjDWDyhr6J9SFcEOZKzrcDJRjfuZieJszu1WncQPnZSfc_NLDoekb879a4nTaHwEYaMvrt2-XVzpWVV7j-yodH3Z9OLvTUFvtQeSyOcu3cPdzlAWR2_83U27rZEJ78T_YPr9g6fRv2NDcsbfSn9wJKQ9EOyoyzI8Wo7dtAcnXcmA1LjYErHRW2_B--gZyrUqvPYvit9nNFRbqmrtvtcfXSX9OkHlG5zx6i3i72xbEEGZesbXuafqY0d9SPTEzwMm3LcPXNvbBb9h5ew1e2h49wgCesTuFEWnNqrff4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی دهات رفتنشونم با ما فرق داره ناموسا
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/90930" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiKFHiG5EDXXe1I7CFHgS5T0gQKFc5C4EO09Y_7eiJ0EsKO0RMxQ9PM3Wype6JlWEQ-UIujd9J1u1KkvL8LNellbzvGprTOz-3y2GtaFuKmRtTbtvfltDUIfqa26DYbnpSz2slXOJyjQOx9Lrrt7cUeUBXWRWKG6qMovBGmiDZniSnXHbt6cHLuOZw3x0xDMMp65zBYzMgl_JLmn9ksHUpGowEOUJicu6uaRnbf1xuN9lF6gjyuhGPmWGx_-RZlzpNT_evstMDP9tZZj4vHh56DObFlX4OL1AymS9fSF-R5h2kJiZxjCZy2LUe9a40zClkJKcQVdQIBAAxoTus6UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/90929" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=gUn7StqCIxbdCUE1LBhVaqQRA09M5uNEK0eCR9W1oGfTIpccwaEC6dvEzxHbIralnCr1gWOOxjRb61A1R6K2MObTSQDqqcqmXUSPkXaIyzeTPEyamU-6iDqQhKdw8AMSnjXcCz4rvT_pcoBINg81BxZgF7tqw18qQLNkMMds4bi_iMOK0sDbPuTJbJqyHfpgLl7P_eu_DJDEyE-0TAyUwgQmu_QfNhiKSdrBYkwsulTjVXHObLGktJ9JYY5f3lBsoNQnA_8jy4w5-UZ0RJL1t8PCijiR1OMAvg-Pu2XIwatxX6qNe3h_MxbxhkWISQmtW_MbSpHUGAMh-38sytE_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=gUn7StqCIxbdCUE1LBhVaqQRA09M5uNEK0eCR9W1oGfTIpccwaEC6dvEzxHbIralnCr1gWOOxjRb61A1R6K2MObTSQDqqcqmXUSPkXaIyzeTPEyamU-6iDqQhKdw8AMSnjXcCz4rvT_pcoBINg81BxZgF7tqw18qQLNkMMds4bi_iMOK0sDbPuTJbJqyHfpgLl7P_eu_DJDEyE-0TAyUwgQmu_QfNhiKSdrBYkwsulTjVXHObLGktJ9JYY5f3lBsoNQnA_8jy4w5-UZ0RJL1t8PCijiR1OMAvg-Pu2XIwatxX6qNe3h_MxbxhkWISQmtW_MbSpHUGAMh-38sytE_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
؛ علیرضا نورمحمدی دستیار مهدی تارتار اعلام کرد که سرمربی فعلی گل‌گهر به احتمال فراوان فصل‌آینده جانشین اوسمار در پرسپولیس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/90928" target="_blank">📅 21:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=o95pA_PezhXTo33eovLVDOzZhydX3ovS1RWUKU07fg9IwRq8Y1PZgU5v9Za3bXEmeiZcibZw_ZhbwL2DnlMcUAacK1IVJKSvM9YtwUoZ7p_-GV1zl8wsLEQWs2_L9ZHRyJropjkNKbkYhUkP9ItqlM8r7A8H7QLtFSnXGEmBzu8xj3X-LnZKEMG4Gi1-upmHtYbUIcxzPkVG9No5kQbrPMS2gTxIK96clOJu_JZ5_ljVVzhwb8h5jTKZiQbRf3vHEzcYL8IjUJa0FIwLuiZaeKVfIQawRBzg9cqgA-whD9VC1DDz3iUwqq_PTpvMhK0gWtG_hv6Zois8E5j-jD2WIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=o95pA_PezhXTo33eovLVDOzZhydX3ovS1RWUKU07fg9IwRq8Y1PZgU5v9Za3bXEmeiZcibZw_ZhbwL2DnlMcUAacK1IVJKSvM9YtwUoZ7p_-GV1zl8wsLEQWs2_L9ZHRyJropjkNKbkYhUkP9ItqlM8r7A8H7QLtFSnXGEmBzu8xj3X-LnZKEMG4Gi1-upmHtYbUIcxzPkVG9No5kQbrPMS2gTxIK96clOJu_JZ5_ljVVzhwb8h5jTKZiQbRf3vHEzcYL8IjUJa0FIwLuiZaeKVfIQawRBzg9cqgA-whD9VC1DDz3iUwqq_PTpvMhK0gWtG_hv6Zois8E5j-jD2WIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال چالش رفته بعد پشماش ریخته که اسم خودشو نمیتونه درست بگه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/90927" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6FEA6n-2xPAO-MIRES20gPeMH9K2uiQmkG2qyiHHPcVxiyHdvXI1acei7FyU6MzqkgjaklNjjLk6upaMHcG_rFlwYOH4sn9EFNJaedo9ybhgxM45PzRn9kgotlZUMdo_aVeL9chSdl6VZ_nYbH9y3kyHG2FsJ3qHen_VSEsFmKj-A4_569JsRxUDnTUSr-F8uOtcEh68fx4mad1OcNCxTH27b52xQ5fm0ojfyhRylxdoLDgUli5sZxOpIfQniGywTKU34Ylim70DjrxB9XA6MxEELigR4Q8WwNswevBvnEEhMVFg3EeFgjpyLyG2YN6nFX3ymK5Et-C4dg7Jx0NGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اسپانیا در بازی امشب مقابل عراق
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/90926" target="_blank">📅 20:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMoTLQDnonfk4XY24hshtVdT9-K9GJKlCrFWdaXaAp7yvYXmhb50RYvUPGHK2DZW06D-YR5j1kyO7NgXdC0Ilsm6DuhCjb0C8KKSvB9v4m9dUgFrIXoksZES4PnHOSntQ8OASQ-ZeNxKtTgPaBDCrl6OXGV-mSHOp3aNK71b9wO9M-5cBxD33lhLN8dTN_KM3u-G9PfeoD3xcfnE2_LUxUfdG2PHBSZaP1H80dLb5sAz1Edl3m6IT6IE6HxuXUDvYn5Hu_ybGtOWUD5uhzRxaAlFs5PYNTVh8exeQfuHWh2FS5vZ-tCYXZkm5HWRfM6ukjTGJtax2gIUxVtqprT1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرخه زندگی اوچوا؛ قشنگ هر جام جهانی میاد میترکونه و میره تا جام جهانی بعدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/90925" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=loGYROTMAje12NYjkFNOLb60nS7qQ0Otplrn2yRujcBV2sm4fy_vHTpTb6agzOhOGSK5Z7NbU1bs2y2ahHGc2N9CZ3SEmTaxnytnOJc-FiKZnl0TSFX3B5eA-qfbRvNJL3JUZSGDJGYQ6Xn3iNtc2ZLZK1K6M9j2Wi7opWvMbMVEUb1efwMBpJTRGq_J5_oRz2Bn5P3qt26OkGddp1CHTrovqEWz7y82BcI7EpNgUmWmKCJ6GzFZXyLZbEm4LGpEk2XYAcLaSp9CHGfzOP08W8yYJ1xEqws2-KS0I7oA_emGNZSX1-2KkhYnKOTYG2XeZEqMnITXXSIXoIsoYrgB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=loGYROTMAje12NYjkFNOLb60nS7qQ0Otplrn2yRujcBV2sm4fy_vHTpTb6agzOhOGSK5Z7NbU1bs2y2ahHGc2N9CZ3SEmTaxnytnOJc-FiKZnl0TSFX3B5eA-qfbRvNJL3JUZSGDJGYQ6Xn3iNtc2ZLZK1K6M9j2Wi7opWvMbMVEUb1efwMBpJTRGq_J5_oRz2Bn5P3qt26OkGddp1CHTrovqEWz7y82BcI7EpNgUmWmKCJ6GzFZXyLZbEm4LGpEk2XYAcLaSp9CHGfzOP08W8yYJ1xEqws2-KS0I7oA_emGNZSX1-2KkhYnKOTYG2XeZEqMnITXXSIXoIsoYrgB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جام جهانی اینبار با دنیا جهانبخش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/90924" target="_blank">📅 20:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90923">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-miXDoOL0VSqeXm9uKubFvRd0CD1Ak3ek9EQw0z-qe2aZ14jCZFWkP5YkIBnWZBhi1FPBHXAcSdQhz3-oYvde4_W-9QEAo1Z_YXX-iY-jxtw5k_slsIjen5_G-DlZrMQvJWftv3Xd0NYe7n_b4mVQoQUd7sh7raP1vUtTsHnVDtRfpzIX0GIeq3N39NHYVprhTKcx-Ud4jLKv_bq-toNTMfEkavS8aw8fSjacq-my7YfEq0nlsDQD85KkYtEEBt1IVK6AI8NseXrJTz_fRxg_xDHR2WIw_jPWp94XyKn_cjv-vjPpjYMPFSyxr46BG_Mg3r1LuEBkLXHhmDH-39NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ارزش ترین بازیکن مالی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/90923" target="_blank">📅 20:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBdVmpDFZcw_ccChARmNG9plXhL3ySYRoCc5y_GLUl-SEnT5lENhZ7ss2ww5KZI4qFY0LmruhdC6ZgfR8wXG6PcACv7tphFmEEehidlDnqaKBhcD-AMYpxh2ZakGAEP_dRD7daHLHK02zPShLZnzavp0xjKx-YtUM4-nbOxyiq962ellZ2DjZMiwGONU8Di3ivOnvAi-5visfi8lje8wGwnpq_rsNPl4soIarlHTbPqzTtqTu-KqF5O9I4nNaarl7PzOLpw3gB5DwbzCVV-zmeF4JoekTYL_jLvdcuVMeq6sVFxk3FJLKlxifF-OBiC7puUTgKjIVP0fypswL1bmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔟
بازیکن برتر زیر 21 سال دنیا در 5 لیگ معتبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/90922" target="_blank">📅 20:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN6mJ7BnpjikPWYIqoSPmLXU-VPLwYs1k89d-FBapjcwcnEj0RoY570LuDzqXB2SX5Oo4I9UVtYgVi6CJwS0a8E0aU9o_uLBTRZ6jL9e-vANpNkPULN7pPHVbP2tuaTVVWBrfP7SS7jfrAsmzH4s9rP2eWG1jYFOkTVPp5kVmGzQOuyPNjmzGRpLzWJzFtdRnsoEGszsYRi0G6Rxqa1qwqznJBJybJBFpCIQyXynU5-nlCvKAnKDs28yWJDNYysUZMuNiRv7d4a_Ja3WAGGrLG7SbwGdo15TErXQzk6YjGCxNOX5lytoeF2QduLzlHQEPiuX1pxp0hSNwPg7D7KoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم فوتبال ایران مقابل مالی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/90917" target="_blank">📅 19:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=fnUDHYB5LqTbQLQmYtqk2LuH--NVHAlPRnRKzNEe9wERvRDdOLXHZG7XgJptPIeMgvN5_ifI_pCi4whsTDyrofak-HOz97LDuduwGHTiHhGf-yL0mjKt37kITxYTEC6sQJ-lnjaH4yheNyn_1_JIsvcAh78mwi3v7gb6GsNutHlRFVt4LGzdM7P8BkzRBC6TR7mY3p-uCCoyyzVyx5IAqhYyYpBzgMMqKHqVqerr0yEo4WqjdC9vNp_zzxCjUbvf9ZJ_34hps4v6BkKInlLgo4YxVRQ3OfP80VWBqxGI152o3Vw7pizGr3gN4JV6wFuifXr6jlkbixQ8CJRjlt87_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=fnUDHYB5LqTbQLQmYtqk2LuH--NVHAlPRnRKzNEe9wERvRDdOLXHZG7XgJptPIeMgvN5_ifI_pCi4whsTDyrofak-HOz97LDuduwGHTiHhGf-yL0mjKt37kITxYTEC6sQJ-lnjaH4yheNyn_1_JIsvcAh78mwi3v7gb6GsNutHlRFVt4LGzdM7P8BkzRBC6TR7mY3p-uCCoyyzVyx5IAqhYyYpBzgMMqKHqVqerr0yEo4WqjdC9vNp_zzxCjUbvf9ZJ_34hps4v6BkKInlLgo4YxVRQ3OfP80VWBqxGI152o3Vw7pizGr3gN4JV6wFuifXr6jlkbixQ8CJRjlt87_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های فرانسوی میگن دزیره دوئه و این خانومه که از قضا بازیکن تیم ملی بانوان فرانسه هست خیلی بهم میان
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/90916" target="_blank">📅 19:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔵
✅
تایید خبر 3روز پیش فوتبال180: تاجرنیا رسما اعلام کرد که با هیچ شخصی برای سرمربیگری استقلال مذاکره نکرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/90915" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5QRLnhK1kkbJJD-9U9hlSSorM3X26swHbHfxTiCrnaLuM_WV6ABxDYCi1TOl42y2P6thxplyy2bNtYMH_SBnmjD6wm74RUxu2FNS-MK0SYuqALUktzhQCbAn4cVwOJjyNTg5HHwjo_QPps5ihTrum6cSMO3lcRLK75TpjatBMbTOFp7Gutmk1Fv0cZqkvDrMgjXFlcm9MNxKjxIi0aKgA_jZ7xmGhHh5teKioP0c3YmQnL8AwCQtk-_dukCGTvkPQsdsA6KzEk7fK3XDSEhdSRJITIEMc_bTFamETOiwFoIiTMM_qYIDIdK_OqZYEs073KdWs-6D3eOT-JoD0bAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/90914" target="_blank">📅 19:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3wQfnNvkoWd-pSSHVpLGiy8km_LNlt0f6midtV-lKLIbAu_8Vf8a4n6bWQQ20YrhTYIKnir0Y_3FHz67s2UQD5hB_kmXs0p9Ta5I2H7Ti_sPAMv0RKjqxouIdqBwS406eAXfKS2lRXEiEGmiFpjdnZ1t-ro5OdDRPPHHRRmBtN1IWVmFjsd19dgIsnzf9pkqeXjWQh5ltTCrELtxhIRiwuPuYJ_choReFc-NrHcRRK_FOTvlu7V3JY9MUqBNyoNX7DFjq2Ru4uG_l7AMkup-endt1GsY2P1e2H-HblttVAtXhEXpW8sdzG3dv8S2afQ12wiUgRAynIXxvRLYiOHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری: بنفیکا رسما تایید کرد که رئال مادرید بند فسخ 15 میلیون یورویی ژوزه مورینیو را فعال کرده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/90913" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZlcz2jkBIvym6eQsC1XcYb4pntS16nK5HMiRGrSkhbJo0woG3v0vvOfFkPKnLhZ_ndNL3_B82iKV3I6VEkpJIHWAUaU5u2REzw7hbB86H4kxNYEy28sWtNfQX4gME7Nn6uinELzotnRvO9bBGlcZMOCKFHkgLdXUwflqfiiX0STSRS6VszkW-zKnWxgC_IAvz-PwspETUmsyK3V-Ik2BEIz3KPayMbCGvsghRQ4KBqo3PcT3jsMaLe5Lx4GDXMOsg0dewy23gftRnzA4gOjebVCx2rtFGRzcKFcK5aX5sRyXv8TyOAazu2V6hTsxLJ6jpl8qVoz5Zs09i_i3gAvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکلاسیکویی که فصل بعد قراره ببینیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/90912" target="_blank">📅 18:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjBeXBETa0dLzQ6yKPBokqxBx_RaXlQ0apAVzj77n7g6HQoLKSFB-LKn7ecgdiSJP3q8UZANAXOElUk7PjHiNM9Ou8jLw2Y0RtsnOauqbvgzPXNk1Yb8aOWnaSZmk-gyPuhnM0KHP8wU8C1m3VfF8mHybGJs4X-GTM7lYsmt0uKIVWpMV5w1S_pgQQWVXVC5gk5PRlHGQaccdDV7_rbz85MJCC174Nz2r4in_pzR5z70Jb2bjE6hczUdB_F4aUHY0vb6XTtp2I0qKt-6WN8IDR4wbik1S4Gu8XXigi2-IeBLPdcVuGGY8H28XyLku-xQdU3e1HfFQXg02Cadu1pzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
🥶
وزن عکسو تریلی نمیتونه بکشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/90911" target="_blank">📅 18:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAmWnQWpFx5OQ6t4ciyk3pO1_PzuUknS3r3T2nlr1MmKShFqOzAGSAsGu-qMfI6RileXEkuXuCxc3LApfWjsqleAO8DJLmyDPvAzuvI3F7FJN_6NPs3KrGYXG_yQtDZY9r-PlchMN6hb-NDlkqyU3hM9-rRAbHf4Z0u5tLeaxiomEbS_mJ-_fIKFXcLoV3Jd0dRY_4E1uaCkFrKDf9w9AXFHRXvIgmRbpjxqjnqFV50_kJUl9XGB6EltIZXI47y0Mc3yBc-2tnYbkAscJEjnfZJUMKn45uoppu6iCB1vTWNfKj3tisxbpZNTrdiyHgRePNO_M1VW6zUzGIPV4_S7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
خوش چشم کارشناس اسطوره‌ای و حرفه‌ای صداوسیما: به نظرم جنگ تموم شده و دشمن دیگه تخم نميكنه به ما حمله كنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90910" target="_blank">📅 18:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=Jjz_yR3wMNDMjwJsZRG7cW2ozaY9UZwPF3LO3m9a7SS61skGlqrIVjw4ASBTGCivub3Lp7udK-wvn5yQ7tayXBjHCdXCImiAN1vWfIjmGNaZBG5E9OOFtZB0fxJaA1O7Sha9GFJrbAl2Bqpg7LKWZ52Kec2qL03iCdFwZFGJDQJO3aP7ekJyLPZRhKlRItqQji_Q3GKfh5jYc3dDY2hJlpbIrrpgqFCnQeHiLqTsjJEeP5TidE3vy101PEqexzZAxoDKcI4TrCq-juxLeeI9Rs9tYfdlZhIj5w493NpzxxzZBIh5ah00Yw121MMo3AqoDv7ShlG7HLAZaibaYCIeQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=Jjz_yR3wMNDMjwJsZRG7cW2ozaY9UZwPF3LO3m9a7SS61skGlqrIVjw4ASBTGCivub3Lp7udK-wvn5yQ7tayXBjHCdXCImiAN1vWfIjmGNaZBG5E9OOFtZB0fxJaA1O7Sha9GFJrbAl2Bqpg7LKWZ52Kec2qL03iCdFwZFGJDQJO3aP7ekJyLPZRhKlRItqQji_Q3GKfh5jYc3dDY2hJlpbIrrpgqFCnQeHiLqTsjJEeP5TidE3vy101PEqexzZAxoDKcI4TrCq-juxLeeI9Rs9tYfdlZhIj5w493NpzxxzZBIh5ah00Yw121MMo3AqoDv7ShlG7HLAZaibaYCIeQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو زیبای حمید سحری از اخرین جام جهانی دو گوت
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90908" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSE9mtrAkp6eDKmFibhRDcwj_eDkhM5KpjNvN5nt1VBdQ2RizurVqAZqUdhEbIGoRsPvTIIotrdlrTZSn_gQ2gGoLNhkXzfw9OaDa84ijq8Vuh6I0GXmlq1Yrkj5Aw2A9lu-BCYo8yJWBH5drvg7pn8YTYf_O0NdxudhDkCcwAbJXECAok5qIhy9mUKm1LkcigXRwLg5tvIJ0Yp5AahKNbWfdQQCsbZguOXTPafB9lTi7uZdIEd7EklZk34u9DXBXPVj9QLMRgMuwqSL1WOlabag5ZqpMg-WTq8rcdQ2q6Prb5BABtPoGs7ovcR_cU8aq0eciDmpSJvmkO5Y2zFuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرائولا رسما قراردادش رو با لیورپول بست و بزودی توسط رسانه این باشگاه اعلام میشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90907" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKZ5b50Or-H814hkUnkfKENIuMGWN7_7XGeO8wfxp81s3hsKuSHZUuhMyUGmyRCyP9Q4nj-a7N57ycIBXZEppx0JXLuMCc5IYb8Fos2O-6yzP3fBlXYV4QkBd07cx9RypJrKzCGBUQHxKc4KOLGMngC9vlhkBgItgY0aA0KbSpBBrlIfEhJaK_uBtD0Mev73PQTqZ6UCSwD3W1PeSwhABY5L_geLZXpqrt-XjkQUo_J5dDoYv53OhM44y_ZMrCsBBa3f4N8HXhY5TNsBhZjr54xN1PpK4eVI8LHZzQ0ZRo3PTRYqgvPUSxsKsrCgYl6Ph2G6iKwkwm3SaWEcuxclJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/90906" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzhtm-eJPMf9s6IRopt-JogXsjjCfRRKT5wgll1Y7nwIQJb7lI-4YBFmj3NpfkQhc8pRnADouqtpytgqvSFLI2orpya15f8mVm4ViTqX4eSOJInqv5OTDMj9A7tJV9J-Kte--Fx5VOfyypYxI68qZQ6z86_z_RPMJ3mhcpYTZYNXGEt8QSveExjps_jAq_kstPeeklpIcT1rW5nsvqZlDAzfIBdB8gGTwpYnp23FkQt5GgB5w4wu8uMY4O24e6TXi2loo59610ogSpRLnYrmpvsFtmiZMC9IxdIwQ2P-dQ22vsZhNIw-QkXjkuXdJN-wtyDfTrpF-T_sVJUomIxAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90905" target="_blank">📅 17:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=Vmra2BHEDAJ8tSxH35DCJy8nMFuPHY0bA_kh4ar9NWDmas_xmZtdgqvWqpOaWzbgEWaZC-803IggmhTT2X604ZPKiD9PBPBCUwHrTQzneO8jw84R3Vz18ZGRyupiB-VPN6vLzQFuc9vMqaU9zcP34cfMkOv7t5ey5j84AJqN6j-8cBAAa6Kq23VunhDAqguzECghDd9B-l4TADIOV_02mazZY9VQQkp4-QrqppYOREh-fDDY98Ofq_PEUtQ87RGOUFsSeXBbZ2OuwSoKu5zeMbD-BnVB9d-C9dCcGSOOxxvVnBYBs4F3vm8yWWw_7HxmfbQZxal_Yj6JsSsznDLmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=Vmra2BHEDAJ8tSxH35DCJy8nMFuPHY0bA_kh4ar9NWDmas_xmZtdgqvWqpOaWzbgEWaZC-803IggmhTT2X604ZPKiD9PBPBCUwHrTQzneO8jw84R3Vz18ZGRyupiB-VPN6vLzQFuc9vMqaU9zcP34cfMkOv7t5ey5j84AJqN6j-8cBAAa6Kq23VunhDAqguzECghDd9B-l4TADIOV_02mazZY9VQQkp4-QrqppYOREh-fDDY98Ofq_PEUtQ87RGOUFsSeXBbZ2OuwSoKu5zeMbD-BnVB9d-C9dCcGSOOxxvVnBYBs4F3vm8yWWw_7HxmfbQZxal_Yj6JsSsznDLmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای فرانسه وقتی تو جام جهانی به سنگال گل میزنن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90904" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=Heio2TaDjUtaZk5ilZs5umI43pwXZd_Qw8NsLg9YfMUq8Ha_NpYcSVvrJpIokvNSpqMB29LxYBe3KH_avInlUrcjfxkelispvpSkySe6lhP1TAfyLJOIWGuNQVOPernzWTBz0BgAfBciVPccWPly_O6lPIb53RWm2VfPQ_Zvp6F70-_OAvHv8CvuK5Is1ckf4f7TmXIj-83oAprlRZsHAycozSG1u8h9RWIP_eLWdTwytqdnaMdjls7aTl2N4sxcLb9BjgtlHDK-nIdCwNXf0--PPCzL7fYJlVNmbKpbM36Hu9stmQJlfSKApB_oqDSXnWm9dOg6NPS1lYCPaP90TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=Heio2TaDjUtaZk5ilZs5umI43pwXZd_Qw8NsLg9YfMUq8Ha_NpYcSVvrJpIokvNSpqMB29LxYBe3KH_avInlUrcjfxkelispvpSkySe6lhP1TAfyLJOIWGuNQVOPernzWTBz0BgAfBciVPccWPly_O6lPIb53RWm2VfPQ_Zvp6F70-_OAvHv8CvuK5Is1ckf4f7TmXIj-83oAprlRZsHAycozSG1u8h9RWIP_eLWdTwytqdnaMdjls7aTl2N4sxcLb9BjgtlHDK-nIdCwNXf0--PPCzL7fYJlVNmbKpbM36Hu9stmQJlfSKApB_oqDSXnWm9dOg6NPS1lYCPaP90TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع های تیم حریف مقابل فرانسه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90903" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUhKFg-6WIoS-552l0aXzDH0563EHReJzjVLnAZQhMFZMENm8wNBslxMhlQ01mcv7Gb7SAQDVRqrCe5spv9gYt6RRXDzIfVOqCRv5Yiu_FYY4fSU0VMAmYiqb3aKTe99L-NgY1RMu-UHDEo3AMweUvFHCK_khw6vtSATz-l7DA3us-4qul8SeOdzWqfx2d_2m2R9dTd77NfTFEjZXbNzzQpzXhZdbC6o1xR9iirXD_W8FNz5uuVQ-jgFcu9q50JR74WP1QB8VW6mJzUSjYuG561ykVUazRDxIVwpJ7yRpq4_sP-lWZmAyvGcbokIYoE0qbXuzWIlNfia_N1Gl-uLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90902" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
