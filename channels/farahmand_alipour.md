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
<img src="https://cdn4.telesco.pe/file/N4ARMjTvPSJ_uKgvLx1nkySQF9pTAHRU59lMqOi_eED1HRegE_aw4_fwxR5FfRWVabv23mCmB5VBTKwiSxLIEKfyAYn-fX3D01xJLzOSbecP4ms9Ax3xJ6uQ9dxfYdSl4O2zD21NQ0sK02ed5QDd90pDfN7HpV9hKrzkWsr4zV8AUQKWreWHOSF6yUs3zMyNLcc3rRco8eDSdxFdjif3s2dkYmJGJ4iqDLOO7-agT5tCez0N3sy6x6v5TLnK-3d3XTya4gn_uRGBqO4aBgHRW9Dk8J0ajwo7ixO3Psa52ZphEiPkjIyX2yiRwreqTKFNZvbfAlsttOVgvY__GAX3Gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRccgvoabv-wGNxNoN2OpDPp9JgmnkW531srP9oI687kUU_RNwZUgc5Y8U35yfLb-YH-6d5N74l_w0Su0fGhXhoDuvdhZO4kYA-jzSaCas80pejAkUanuJ7Ya6gRCXif06sSBH3mrgqbDUAOSyJJHlDvPE6YpJpS467Tgxkc2XGxk7l9t34b7jRQMpSqMANnnlEJNx5_laqWiW7IPEffR-3IVVSxAWG_xJvpjQLwE7aJbhDoriKErOioVDIQYzzbJcfwEpWHiF_NKUUsyUCTxDWypac8Ftm_sGuednOskdFna0XLY8Ko5JYI1spSGs4Z9YWeEL-YHk5_WqCBj3l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV3pGjpnHzpEnvTsGDUQEUZ64nQwZyRVj5L2qIc5stek_oCZtFGZVfFdVOJtij4zBd2dF6xFqoSnMgQcveWLett5aWYzH43IVId397WD3vDz18d8S-V2ChBt_jdNbekmaQaz5n-BeH03NqFwIDO8q9IA_EL1SgIJRwBWOSHQPsfw40LBzKPLs5U7EPT9Xq9c-fnjzQZDg7Tk8tUyrDt2tHV1meoqtuPoONzVj7fdoX4zKo2y-CS4MEYBMNZNkAWHnDOE6UgANl8qsnJrGGrrBkocsWbHjlpiwxrxo3FPx6JZw2r20CUKZXD8tERX7iPotKwpeOqANuCkLBwcynPr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=hsK-WSduPyVKUIVGLrIAwLvHVW_LjRvcJBXUndZQiudkuIGUJBKyR-ImRoSo3f8qICKQBOBOs72y6-ADWbYoQb6_oEpRWV0bLQzYqKpxOyhgYG88ueOIiYVeVzxbxFtLl7_qMNvNee2p7-tPIVwp2_1UvE0QaGaRPA7gHqZ3fhHvyKmbBSaCcRaBpnPayGHOwXTpJILSm1pR1F2gY5YjsR6wV3uqr9FD5e0wsyk2dQZFuiOPgKtuJOlcEaMqVU78YlUfZTBsB1QcDug1XN7s7cipNy476CUjeCrO_kmV8PaRGf25VwEm2j5p_w1icm93vcaPa52Pb8ya3SPbXsKbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=hsK-WSduPyVKUIVGLrIAwLvHVW_LjRvcJBXUndZQiudkuIGUJBKyR-ImRoSo3f8qICKQBOBOs72y6-ADWbYoQb6_oEpRWV0bLQzYqKpxOyhgYG88ueOIiYVeVzxbxFtLl7_qMNvNee2p7-tPIVwp2_1UvE0QaGaRPA7gHqZ3fhHvyKmbBSaCcRaBpnPayGHOwXTpJILSm1pR1F2gY5YjsR6wV3uqr9FD5e0wsyk2dQZFuiOPgKtuJOlcEaMqVU78YlUfZTBsB1QcDug1XN7s7cipNy476CUjeCrO_kmV8PaRGf25VwEm2j5p_w1icm93vcaPa52Pb8ya3SPbXsKbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKUB2NRc8rxuBLd9M1wY8l5CQIqddrDS9sQT2OanNkos290UvI_9sDKRIFP_NWr4dsZM4KMsYaKvphn8mYNLVWFyDd1JBzyfWPQP7uDJaKtj5_u3L3-x0tDpk-hVMej1mE0B7_2uAtH_aKmUcV1fcvsfggM9INFaSWVaRNTpsbrQ7oRMJ5--HWtT_BBCYsa1X0n8KW71-egQyjujBDctMKlD6mvABSEv82OQ_Nu2_CHJFEbhR_vQeZyRwHmIH2U43ke3zkPkjXO9uJHB8GLYV6RQg3e7m6i2G4BqU0Ftt6aMYx84zw8PGn4QCqqBq9teAFAErmb4XRT-SFbg6nzPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vZ_kVblSneE17pJgfQwXfNlzx3jWmeHWzAan_Fq14Br9YYRI9_MAVIMB8jn8MfMVMHI_FCA_edDKPJWl8pACx8UG1A2Ynu45abKCzxV8AS5Ccif5PXrTU-2kDMMhXqDaOF6h-_KzaLHgAoD9tNTH5wdnMsFYoJcZk7S4MFbOMtU8_mM6pg9GLf4r7dWZPZFtNHNv9W_LlA-uVtRx6beT4scvjui8_dU2kFN531DR1RZ7SAInV8oqrQ_sP-SPOL_V-rzwC6WFFYGdnpL5qsSrCZnehYYI5kui15ZJf7THZWwgM2OpWUIqQbxXH4Ad5Sy6hVIjFkwq3eqZJDYghkOUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vZ_kVblSneE17pJgfQwXfNlzx3jWmeHWzAan_Fq14Br9YYRI9_MAVIMB8jn8MfMVMHI_FCA_edDKPJWl8pACx8UG1A2Ynu45abKCzxV8AS5Ccif5PXrTU-2kDMMhXqDaOF6h-_KzaLHgAoD9tNTH5wdnMsFYoJcZk7S4MFbOMtU8_mM6pg9GLf4r7dWZPZFtNHNv9W_LlA-uVtRx6beT4scvjui8_dU2kFN531DR1RZ7SAInV8oqrQ_sP-SPOL_V-rzwC6WFFYGdnpL5qsSrCZnehYYI5kui15ZJf7THZWwgM2OpWUIqQbxXH4Ad5Sy6hVIjFkwq3eqZJDYghkOUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=NcRuYIR4wg1FciM74v40E4c3RamTRMUOlvSbYjJbKVaJUXBtMoWukB8uNUrTqsUGBByXZ6tEUYfCvHrrh3wBcePU6gCwt4bwQh28AhvsdQrq0gn9unmKzJNN0XXZ42AzXcet7kxB7NpaY2X1o5VqFyim-GTKm07-obdTw7n-vONoCq4di2-TMj2P2oSp4f69V-aGsoy1M7lsp2lL-oqFw1UMrqzYosrQ76GywgP8XddU6_RV84uvM9upoV6pRErODV0I_H0eNkuE8ftuwWAOQgP5Fon6ZW8pSkz0XOLOU52CBUHcIigPLgwGVnsrCjdhP6fE5WfGGSih4TL_3TYr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=NcRuYIR4wg1FciM74v40E4c3RamTRMUOlvSbYjJbKVaJUXBtMoWukB8uNUrTqsUGBByXZ6tEUYfCvHrrh3wBcePU6gCwt4bwQh28AhvsdQrq0gn9unmKzJNN0XXZ42AzXcet7kxB7NpaY2X1o5VqFyim-GTKm07-obdTw7n-vONoCq4di2-TMj2P2oSp4f69V-aGsoy1M7lsp2lL-oqFw1UMrqzYosrQ76GywgP8XddU6_RV84uvM9upoV6pRErODV0I_H0eNkuE8ftuwWAOQgP5Fon6ZW8pSkz0XOLOU52CBUHcIigPLgwGVnsrCjdhP6fE5WfGGSih4TL_3TYr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbXKnF9LP5phBGZiLsSHm0c-M88go6h6PSmmB8446pv399BzJq2T-OUJpQB1W0kgS3FRRfyWUZyVG2QANNcD7p9Anf7eQnwIsq1-9nijFZJZE9pm3tBZ30jW7v3gq7UcoUUIyrIqwEtHlCJUWBvY405Xi1YAd4yuojYkSghbuPF2U5mP_QKWoehm2tAXTancpOC2jbBwzExBJpdBRujjpJ-6dKJrZuXkjX5CAEIQOrdj3zTqg2KEBjrI2xNnTt5n_XeACYI0abgAyhKVDDBUJaOAvvUVpxjHNX2T45d80V0SaAg69CTDzaf9Gf3-rI9ZtWzaDskNJJd4M49Mlw4Axw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=E2217XTVXg43RcHcq80_fGWA2OZCEALsPJbo1dWYYg-GYQtjTO2sQBrFpL64fIY9lnqinXPeTXUnZUyrki1qT8L3YCeyFppJ4_U71J9pkYNLNPoNCndyi1O__pn6csgIt9sZsHGURz7IywPKk-yFuoeutHWkAU_1u3t2TtskF8THA1iepTDYO6vq6sF03F7QXxP7deP2Zw3guxI6adr3wroTJlpxXCexmWNymCUKW2oFxwDeV35Jzy_K7835Oc6gCYp0q2E7QHpSiuo1F3-Q_cqRr-1FFMm_w_p7aYQYcYwTMbDbp9JxOW_RGv-ubd1F-ppkiso7B4Q1T2rs7xpghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=E2217XTVXg43RcHcq80_fGWA2OZCEALsPJbo1dWYYg-GYQtjTO2sQBrFpL64fIY9lnqinXPeTXUnZUyrki1qT8L3YCeyFppJ4_U71J9pkYNLNPoNCndyi1O__pn6csgIt9sZsHGURz7IywPKk-yFuoeutHWkAU_1u3t2TtskF8THA1iepTDYO6vq6sF03F7QXxP7deP2Zw3guxI6adr3wroTJlpxXCexmWNymCUKW2oFxwDeV35Jzy_K7835Oc6gCYp0q2E7QHpSiuo1F3-Q_cqRr-1FFMm_w_p7aYQYcYwTMbDbp9JxOW_RGv-ubd1F-ppkiso7B4Q1T2rs7xpghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9yWJZ5DyJgEYHXk9WSo87BEFvXmsL4X5gzz4KiA48TYfR9LYF8tJFO89UOm3ImZpZ0WqWVVRrUuxagyRrcRrAvEIYGJqHb4wiTRYgg-w_X6PPk9JL1t7j7cvcd-zmbq9FJkcCGZI6-QDe5NjbsXukL6sb-0r6IS4J1jz6iWgtIGk4arGUC3Qwa7CYj-NtsVEcYZtUtYHqT8IY1C7ufUVpDP2opKNsherBWPDx_aM3Fkq5XBS_1nsiRnt0iGQqKZnxQbFJoJPgu67XaFXG7pmXwpEY4EHDrrdHSZCG1lzGk9SExY9OBIcPZbJYM8I2ZpxOqpcu3hQuK2A9tL-Jg0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUCMMAr_QgHwZQmzKcWzjj3Fg9Sfbby2ywJ-ER2_crReuN2r24U-PhUS2RbbmodQ5NeadJY-ZgA4ECc2P6EDq_29tBZCUWAuzqO0yrovtYDAB_1d0-gV9AuHw2KiAzKTaputtM75wPtY_k9clF_CRN4jI1kkYKKNgrYvGX5NInDoMSmmYYN3Yb7GPjPtt6DkrZvt2Ln0Mv_D-UomJkD5lahvYlgdq0B1Wz-Ve02J5jfKlwRK3TbFXjY2enkznwPZgacYd0KLWpVHSM8sCAIPvY24MXwBzBBGIJvL7sDGcXDDtNwdiN5qFNcBjG-EWB0COWJ0inUL0zheVC5CJDTEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwI5-G-ZuaELprKKrZxW7f7-_GlRjHLUWFO2QYfWrGinXgf04aBff3l3KyQLnFJ2WidRmj_yd74rKjlS3CXi35ipM8DaE2rqfu5GLvGkZeA-cyP90Oqv_6vHhQvoAeZr1Kz1IksNjFvdvpq9Ac4meV8YiUKfxhNTVrA_61Cw7pbq4ay2OIa5CQl82zBzuDXa8ao5ZYdk9AlkmERPNZ0u8mw4uMyiAKM2DHE8V3wHOpBmt4NJIeukvYaCbSF20da6jxGxQ21Hui3S3lAOT4KR1JCSoVQHaovucocH_v0GX5UWFEiHrhMrF96russQBx0KDhvN7itgd8d9n7ucDD31og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPvaytoztExt3jvReZMK5_er0Q4c2vq4TRhXXAjdgvfrgnedR2dB9qRLQm7i_4ayUoxxVgix7tIWtXDjf8NyN2tSLlZEgPhvvWFEo_lVWS4AVKnNjntw_nWUbnrZlRJv8M12SflOiTytCZuuVIPMGQXGEJJQJp41mH51w7wzdUi3AcY8F3-nLQyTXXyGkD6RtpaPErdHimMCWZ9UY31XT_lDXVodrCva7uHAzrqfM4bHTV_A6m0CgQEv2byMs-GJ3-3Ya_rgj4yBlO17wbwzu5Rydi7kElZYmCP9u6Is15jRrvdA-7bUa-CfiGjfDH8UjReC25ZegQSOEZ8xXCCmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThscCGFYTYGM76CFObMI5NVMv1xDrP6Akh68ElmAHJAEmCHwiQem8gKyLAIF48jfr1Q3E_csnwpkpvdsrrYyY12JfclO2Lc3k_Lb4vPw4pbvFckboskJWLA3-fBbwSdKMjSOdHKywWjVStm9n_GiWmMkhD1YRRr0huAya_N0COBEywhi5Kwc6ukQH4AFoagN_utVoGhmWWLvvvQcqzdzzM5CyT4XI90XR_Dnh5aIdHcupGm-qmXp4Z_NhplzmN2gX9Y7oz2_tJdBshy9i-Dh75X15qwEkbwl2ku-xEnzkOQyddD_ktsE4QA6wR7fRjGt6YHvCGOjUVSmx3ig1MUo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vskieIgn44WrXqh77764ivb7jLRmUkWVhG-x7PzeXOBUD_eph6a_p1mIlQ1fydECkTcxRMqFiDmq4xvKjKV6N8Xz3FZkAVjauLCwAddwc8B25Ol_ny1u8c5yjB1TyIez5QMVviyPbFVUO2-gUNQHikSlzy3wkeSshON8zyS7EwT0ledE05VFri2JEk-6TEPVygUEyiiIPqyJvKsiuM78Jl_XdneY9ITSWL-yAsJRq1GLfyrLbKuODae2yiygYlDagM51MlWEVpIOrGJq_GToYnFAKaCT-Y-dPutoy_myFALU1kQeozecaH4pkVjg4ZqhZ5NyJ-qSmB8Qw0D8qEmtDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vskieIgn44WrXqh77764ivb7jLRmUkWVhG-x7PzeXOBUD_eph6a_p1mIlQ1fydECkTcxRMqFiDmq4xvKjKV6N8Xz3FZkAVjauLCwAddwc8B25Ol_ny1u8c5yjB1TyIez5QMVviyPbFVUO2-gUNQHikSlzy3wkeSshON8zyS7EwT0ledE05VFri2JEk-6TEPVygUEyiiIPqyJvKsiuM78Jl_XdneY9ITSWL-yAsJRq1GLfyrLbKuODae2yiygYlDagM51MlWEVpIOrGJq_GToYnFAKaCT-Y-dPutoy_myFALU1kQeozecaH4pkVjg4ZqhZ5NyJ-qSmB8Qw0D8qEmtDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=vaWc9IrfPrCrHQc6iMXZCh5urIi2jGQklObYQqAdXloB_2POssiuqSAOm31c0yIFX6FNmT9rA8Wpl0h7p-wrkKwBqh0UMLHi1-EU2RvrM7lQynw1JiNoJsN7Eszom7yvrgy7s6uBT1C-Y_z4htgrRQER6Z62U2-IQljo0zrk5jqlXD27SgfgWVvhv2ygbIUkgNE5FTs1kMt357fHUDCQL39GlP_Os1wIf1C7WIeVpiwzDeBuSTUW8LFbyiDjxVzN75zdYhhpwYMGuGRz_RQDMTzt5ZEiEvVGE9JzwUlb_qO3kuWT1YBSPsE2Ti5dxURpHOipojEAPepcX3lj4wsjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=vaWc9IrfPrCrHQc6iMXZCh5urIi2jGQklObYQqAdXloB_2POssiuqSAOm31c0yIFX6FNmT9rA8Wpl0h7p-wrkKwBqh0UMLHi1-EU2RvrM7lQynw1JiNoJsN7Eszom7yvrgy7s6uBT1C-Y_z4htgrRQER6Z62U2-IQljo0zrk5jqlXD27SgfgWVvhv2ygbIUkgNE5FTs1kMt357fHUDCQL39GlP_Os1wIf1C7WIeVpiwzDeBuSTUW8LFbyiDjxVzN75zdYhhpwYMGuGRz_RQDMTzt5ZEiEvVGE9JzwUlb_qO3kuWT1YBSPsE2Ti5dxURpHOipojEAPepcX3lj4wsjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=F1i67oSFL31coYblUNmFzDoxTn0Y2ZQamsHXgquWaW_ELLqWb_8l0KCQT9ocGdZ0gL3EuwFSn82MZeCxk760XANK_BLEXNe3IT6iTfgV6CCiY8BmNR32EY8-P9AU85BY1gN8yYMoE-iU8p_GQ63g27FCoN2S6GztqxBpzzpdAxGw4664JeO7OjTwrtseMbVk2ixwjpdN8jOeHjqFd8Hpm4wTp07ZpxAerTjR6kZWccNPC89fq7o4NqENgy0GwQK7WHKb4MySelBGQvVGBYVScpUXL7xonIuCT5NF7mWsg4RvekGDNkg-F1EVI7NjLWF-zMkS3lYExu1gMsAlzwhPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=F1i67oSFL31coYblUNmFzDoxTn0Y2ZQamsHXgquWaW_ELLqWb_8l0KCQT9ocGdZ0gL3EuwFSn82MZeCxk760XANK_BLEXNe3IT6iTfgV6CCiY8BmNR32EY8-P9AU85BY1gN8yYMoE-iU8p_GQ63g27FCoN2S6GztqxBpzzpdAxGw4664JeO7OjTwrtseMbVk2ixwjpdN8jOeHjqFd8Hpm4wTp07ZpxAerTjR6kZWccNPC89fq7o4NqENgy0GwQK7WHKb4MySelBGQvVGBYVScpUXL7xonIuCT5NF7mWsg4RvekGDNkg-F1EVI7NjLWF-zMkS3lYExu1gMsAlzwhPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=KNuz1TlqvVBR7pQk4bb8xefmNeFz9bZw63QBIbzAVNsmmgAab9aGfQaN6NIqxjOsV3P9JW0zwwdWcindwzyHjcXQ7APoKpJEHOYwffz7vCxhraoH8-LGbEZVW4mIWq_yzoIcmhdXhceFMa5GhmL0d3ZIjB6d1w5msAD4H36PHp-yu6l6O6S3pYPlsjcO8lf6GHBn8LTrR_UCexqxoSWjF_uJ2T-0OEpsfiGMpXJzdqKJZaCrHSDBTrblOCSb8WsKceqkwxThvi-VqdUfZ5Nw69e8MBc_78X5_TbrczlCI8TUmyZ9kTYsjI9pzs9emRgIYxe4ppA6O_JTSeURg592zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=KNuz1TlqvVBR7pQk4bb8xefmNeFz9bZw63QBIbzAVNsmmgAab9aGfQaN6NIqxjOsV3P9JW0zwwdWcindwzyHjcXQ7APoKpJEHOYwffz7vCxhraoH8-LGbEZVW4mIWq_yzoIcmhdXhceFMa5GhmL0d3ZIjB6d1w5msAD4H36PHp-yu6l6O6S3pYPlsjcO8lf6GHBn8LTrR_UCexqxoSWjF_uJ2T-0OEpsfiGMpXJzdqKJZaCrHSDBTrblOCSb8WsKceqkwxThvi-VqdUfZ5Nw69e8MBc_78X5_TbrczlCI8TUmyZ9kTYsjI9pzs9emRgIYxe4ppA6O_JTSeURg592zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSMoeT9G9lAWhvk0k0L_woEYLbLj5JQBpIzHn1AvPtjAM0va28IUXygatv8SX2CwMq8eFd3-ji9doQU2NqP8BJxV5ffhGz2I6gW8J1j22XVcFGGl5jFEXw4wbqE0ATXC1gIk9OUhSoxr537EJL9kWY4FNyxdxd5vb3pwCaNL2Q9KczkIv41IhDma6Lh2tIfqF4_0QSNO3UF7koC87Itl5kUz3eQNaGs9R1XDxzp1O4CUKdIbdDpL2lRb1tBauxcX7p16I92YluxogNdUuQtMts19bZiKEmsxVmKqBc4DWqm-sao8kQ8C7XLp9z658f0RyW7hNhpEXgDpfYayApjKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=l3zp5kFSJgHEjTlGPCW87fKsCZey2SbQ2pljGVhhDrTgbF_I1zBZcrShTBLFq5qAirrqCH-uVC1bK1POLtnBEnk6V9fJ9_Vbo4s-T6CpaX0P8YIJU2ssllsKmVSRqaD7JvX8InsHgXA2HOadm4WIQ348fo23m78S-rWzWASnvr0sUFdaQaLvysnvHgfKy3sNGaXWXzb6hrbS6t9X3LN5XWxUswQM-yuGq7zlf5UWSgXyBdjKXtuCNpNUS--xwZ3kNkkBDvaABv8DXJGaQQrmyRWPdSwbuiBqb-aysLHyDLxpvz3jACiOfAyA-ftiYheoBqmNb4nkk1sKBZ4gnJEfIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=l3zp5kFSJgHEjTlGPCW87fKsCZey2SbQ2pljGVhhDrTgbF_I1zBZcrShTBLFq5qAirrqCH-uVC1bK1POLtnBEnk6V9fJ9_Vbo4s-T6CpaX0P8YIJU2ssllsKmVSRqaD7JvX8InsHgXA2HOadm4WIQ348fo23m78S-rWzWASnvr0sUFdaQaLvysnvHgfKy3sNGaXWXzb6hrbS6t9X3LN5XWxUswQM-yuGq7zlf5UWSgXyBdjKXtuCNpNUS--xwZ3kNkkBDvaABv8DXJGaQQrmyRWPdSwbuiBqb-aysLHyDLxpvz3jACiOfAyA-ftiYheoBqmNb4nkk1sKBZ4gnJEfIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAjKfH15F4ul22tu-vscnmlmb34rUAwCMVjgwEBnNuCztPqtXUmHggQzSOjA8wvdhK1zEdME2JPICOHfKC2I54gKwF9pwcKcPf4b6r5jTxteuxbC_Wg94cQj1fVWhUzuYq9DIAe0vUCJ6U6evb9wnH630YkN0LBmVDKKqbUcCgK6YxBrDsWHOiSnzgGvHKANvubDsl3rVPvMPMw7SwirosPwWLGgRIvD7G_G6ICz3ogHPKMzi9KtVNWffLGZkOmtUN-ZKqccvAvx-aJUanYHImgHUklyBt3kPqinLdnE3o5ZmZ2jktfGQda4ajGhG6mE3c83MTg7Z4L9zY1eKV_i1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=cjzb9xfkCNktX6eVzYKbP4DjC-U45L-YqvBUkvZVGJ6zV5BUOyaWSqBekyygjsvoj1he1aVSjv7oigAAlZgu6knuEuB2r-WXe4_a5eyylIvyI-nm1RBvVYrbsFFUK3v5fQLi3XmFTp5NfDW9fKXFHdyaRuPPvvUGXuIDxS8UfK6eVM57xy9UAwH44EZt_RrxhBBDDYgI8ceGTDRPyrnePglLf_ImWfPUmjjsfkNbqREb_279l1CgtqItfQcmI3ZCW0ur33ZUvbZHoh-9eujHJI4RsqSf7YlOPi7dtc5h5gwlAbQzs1ubEprgwPoHAwM_xdyP7fCv2Pwcqr7AbmMU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=cjzb9xfkCNktX6eVzYKbP4DjC-U45L-YqvBUkvZVGJ6zV5BUOyaWSqBekyygjsvoj1he1aVSjv7oigAAlZgu6knuEuB2r-WXe4_a5eyylIvyI-nm1RBvVYrbsFFUK3v5fQLi3XmFTp5NfDW9fKXFHdyaRuPPvvUGXuIDxS8UfK6eVM57xy9UAwH44EZt_RrxhBBDDYgI8ceGTDRPyrnePglLf_ImWfPUmjjsfkNbqREb_279l1CgtqItfQcmI3ZCW0ur33ZUvbZHoh-9eujHJI4RsqSf7YlOPi7dtc5h5gwlAbQzs1ubEprgwPoHAwM_xdyP7fCv2Pwcqr7AbmMU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=e1hBJZ0NeAiIN6EO6N9HsR0Tvipkm2OpR_sRMkqEG1miC7APTeqr2tWHp7QZRk14f45tQx6PkEXA6viSx0pqOQM8ROnCQDl_ocWiSuYnlWjUcMSPbHf5NcuM9sIrgERY7SI-eYW737wdN7zedxSapM9m2DWgpUznn_yF8C5mEsUIGWbVWVCv5xgH8LqWRKYi5rZlFrUZZEhD_oLE0802PD3NfehPQ9ldMJdRWFk6TVph0bDqNLVou_3Vn9oFlcuZBd_Twz8K2gArW-jw8at2JX1a1YcQJzVu2fQB-zX1XUREXBfSotujYWKzPkHH_HPlegYJn3P-ZlG9bcbRuPV1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=e1hBJZ0NeAiIN6EO6N9HsR0Tvipkm2OpR_sRMkqEG1miC7APTeqr2tWHp7QZRk14f45tQx6PkEXA6viSx0pqOQM8ROnCQDl_ocWiSuYnlWjUcMSPbHf5NcuM9sIrgERY7SI-eYW737wdN7zedxSapM9m2DWgpUznn_yF8C5mEsUIGWbVWVCv5xgH8LqWRKYi5rZlFrUZZEhD_oLE0802PD3NfehPQ9ldMJdRWFk6TVph0bDqNLVou_3Vn9oFlcuZBd_Twz8K2gArW-jw8at2JX1a1YcQJzVu2fQB-zX1XUREXBfSotujYWKzPkHH_HPlegYJn3P-ZlG9bcbRuPV1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=qTF8QCrvgjo6mvYrLskMaYYjqHUocUtYmk6MchF3f5DzADWAZj0SGPYC7oX5JMF_xVo9AozOIUHgbnx42gfnuNN94XQqlif7lBQPl46VRsawlTeziquxW7WC9v4aF_Jk7ogzNLT6hmLH_1fvEGjNYtCeaX7noHMDMWZjbc92YHQXDJ3EUCpTJxdmmURKBa_ZDySZVrtxNUPPfkXnUuEPx07eLY-vXUMqtLo_kTZSDJCIk67RDbFxNwhLbgTg5p7cNKwl_yXO8GvEq5yKaC9lK7HdP4Wk0VKMGvymGVCNC4nlpJm-P1q68t8QjCUj9G489Ue95_B3OIdFw50p0Ob_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=qTF8QCrvgjo6mvYrLskMaYYjqHUocUtYmk6MchF3f5DzADWAZj0SGPYC7oX5JMF_xVo9AozOIUHgbnx42gfnuNN94XQqlif7lBQPl46VRsawlTeziquxW7WC9v4aF_Jk7ogzNLT6hmLH_1fvEGjNYtCeaX7noHMDMWZjbc92YHQXDJ3EUCpTJxdmmURKBa_ZDySZVrtxNUPPfkXnUuEPx07eLY-vXUMqtLo_kTZSDJCIk67RDbFxNwhLbgTg5p7cNKwl_yXO8GvEq5yKaC9lK7HdP4Wk0VKMGvymGVCNC4nlpJm-P1q68t8QjCUj9G489Ue95_B3OIdFw50p0Ob_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=uJS5Td009ohrgVcFh5V_GnjTtafD7AAzWuPOsNS6kpZ9coQt0NFdxqN9q911KmRVLNwNTRhBf6oLxIfCz3LAIaYTq0cA4Sfe1dcEtMba_gED__-DTqqiM9CmIFvCZYVITz1-qTaA9jRiiHlSX_qN_xPBcV9040b7c7CXyfa-aKWKU-2aSK8dUSeX26o3sc6MdrSvgs03Un9xeOyUlMwidOBXTw7-mmm68GVFVyO7uDMp5nENJ5wdmvFG_utckoUr4Nsikfg1RCRgEmveJS2ssgpt5637P5kdlzzkguoTU9sknglADIrrzu9wHU84EzF0HBH5eJgRmto1juQxUofe8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=uJS5Td009ohrgVcFh5V_GnjTtafD7AAzWuPOsNS6kpZ9coQt0NFdxqN9q911KmRVLNwNTRhBf6oLxIfCz3LAIaYTq0cA4Sfe1dcEtMba_gED__-DTqqiM9CmIFvCZYVITz1-qTaA9jRiiHlSX_qN_xPBcV9040b7c7CXyfa-aKWKU-2aSK8dUSeX26o3sc6MdrSvgs03Un9xeOyUlMwidOBXTw7-mmm68GVFVyO7uDMp5nENJ5wdmvFG_utckoUr4Nsikfg1RCRgEmveJS2ssgpt5637P5kdlzzkguoTU9sknglADIrrzu9wHU84EzF0HBH5eJgRmto1juQxUofe8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=SOK3Ni-vTKzNQaR-mw12Zm7echKHS98i0eYuGVxzzrm4mKLMEw9zi7vsdaKR7W9lLpx4mHBvcJJmbaRzzyTSHvyMzNMwiL9A5s0DEF3Eqc7XgaZ1tv8lnIoXHSzOZDFmk7tgO7m-6PkBkmP9H7WAh6vb_YHdFHFgM3a2XkmokYvzhE-k91qVrWN_LxYj5ZY-KPn95rmEcL_hIaWXrkqhxT0uAThLG4D3dccmZfMbBmIpN1ld_9hc4pEwbWZJqXfcz-bDrUBgGHiBRqth54c3Nk_gkdlpEpS6gf43wd-apMIIfXO3cn91k0ckhI06yDqkuLoDql1FDykCYa93Yse8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=SOK3Ni-vTKzNQaR-mw12Zm7echKHS98i0eYuGVxzzrm4mKLMEw9zi7vsdaKR7W9lLpx4mHBvcJJmbaRzzyTSHvyMzNMwiL9A5s0DEF3Eqc7XgaZ1tv8lnIoXHSzOZDFmk7tgO7m-6PkBkmP9H7WAh6vb_YHdFHFgM3a2XkmokYvzhE-k91qVrWN_LxYj5ZY-KPn95rmEcL_hIaWXrkqhxT0uAThLG4D3dccmZfMbBmIpN1ld_9hc4pEwbWZJqXfcz-bDrUBgGHiBRqth54c3Nk_gkdlpEpS6gf43wd-apMIIfXO3cn91k0ckhI06yDqkuLoDql1FDykCYa93Yse8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=niG6qqcs0yFNuggqx69lawW4C2yTBh_eCKRQGtsu2Z24XKSI-KAKgdrjur6fbCq-L5OhpogW2H3NVKVVMw37rJmNkFdTi_d5vED6fzgYa0vp3lMuA5TiryVvxiIomdR4XCc6-qanZufPKFm-FSTJanyuC0DFy92XDZF4ZyU6iaWWtgUF_qQ21MM3FHroT4Y2d9F1O1tWN5upUoMevNHPVo1uNE7GFGCplq_nJ9Wz-PRlrC3mWpjOO_q95sRDvwBzfW6yYLK4s2EreeXbvIgAFF1GQvfvzmYx7JDIkwsQyLXHTCxtC7ZcIeJV_wQWINz1GuhYc2Zbsx8BqG1uuoExcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=niG6qqcs0yFNuggqx69lawW4C2yTBh_eCKRQGtsu2Z24XKSI-KAKgdrjur6fbCq-L5OhpogW2H3NVKVVMw37rJmNkFdTi_d5vED6fzgYa0vp3lMuA5TiryVvxiIomdR4XCc6-qanZufPKFm-FSTJanyuC0DFy92XDZF4ZyU6iaWWtgUF_qQ21MM3FHroT4Y2d9F1O1tWN5upUoMevNHPVo1uNE7GFGCplq_nJ9Wz-PRlrC3mWpjOO_q95sRDvwBzfW6yYLK4s2EreeXbvIgAFF1GQvfvzmYx7JDIkwsQyLXHTCxtC7ZcIeJV_wQWINz1GuhYc2Zbsx8BqG1uuoExcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=CTsP4zYkbdEI-C2y4WPs4gkqjVugPLAs4GYVQsDnmqvNudBCsNtL1t5w5zmrFQVyFb-YXWFZr8rDZlfVpVf6uB7w6ww1LKFv92SkPIg9oJcoGgayWOJQMkcxa8VTqDEFZQXB3poUIRLjTg5-_GEGsYmnxqh5w8NLDJ7tBY8KId-Bdm_i6FcY4qwAspRnk5_fqpMhQMRoOmgdZ58qdU9a7AzZvX2crY7HDYk6pww207-sMfYEJs082iAgzpxHWwB8IK1c46CR4H9SU3WILJssnbZyIj31bnxXAKneaCk-762piExT9f0FSre8TwXpy_XfqhPCUy7nXsLM1ZCsTjt-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=CTsP4zYkbdEI-C2y4WPs4gkqjVugPLAs4GYVQsDnmqvNudBCsNtL1t5w5zmrFQVyFb-YXWFZr8rDZlfVpVf6uB7w6ww1LKFv92SkPIg9oJcoGgayWOJQMkcxa8VTqDEFZQXB3poUIRLjTg5-_GEGsYmnxqh5w8NLDJ7tBY8KId-Bdm_i6FcY4qwAspRnk5_fqpMhQMRoOmgdZ58qdU9a7AzZvX2crY7HDYk6pww207-sMfYEJs082iAgzpxHWwB8IK1c46CR4H9SU3WILJssnbZyIj31bnxXAKneaCk-762piExT9f0FSre8TwXpy_XfqhPCUy7nXsLM1ZCsTjt-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_d1aM8iKjFAA31qNtWmytf8iUFA46EYRQj0uMC9amPdhOvb3eSvVeTGcNwwK4YzQk1Dfhi65TJJnINz-pIm6cPBUOQwt5Pxgk5Q3Hl7RYZjm2OfE3RzK5tXfXqrze7VhAXnSsfcNilH_fXYOgEetcTxJSKz7xC0vmRPwqZ3GGJ5kSB1VBdxev8ha5VYogx8c-YMCzTtBsLVhzsU-W0PIBjTlm9dVvOQxxOk8WzBykLLyik0izwllO7xbpFpUyRLLj6RDnhVX7btIMeOH0yTOSBcgf-07DT0UyRFqmqugBef1FyJ7pq_0V-zvKYiB74-8P_tSGzU9kkpXo1QTqeJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvfkoeQWninFbxyXmQKIVWpJHJsoOR9aXRLC4U6vUZ84AV-mnJQN20b0KOzPSU-xb5OFz0g6mIXV0ioiQSUc9BPlmO0WkN1GFhb7DhD4WSMDFg_tIby2IZUjnh8iucvfZsFDbE1Mf8C-tqNSv7P0VKEEegm6a7zRK7hnVDwz4lIXCnOHzawxvCqHMDe-qEcpsQIAukGeq569cD8GABWDwoOy_siluIjw_2s8RKmW-PdrgrU6sYAfZ_CiQtEwAg636kc7nxLMbZE6NLzg7kS-RQcE7RrNJAkwwRR6PqZE5cK0UfC1aS4hvZjJZUyXhhslAGOhqrWde7MJOw4crt1r6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=JxoVFShbFSEee3djOAJKmw9Y_o_bTTyL6Ew3pbNnwE3sCjByPeohhHy6E298AFqTIxg4xsbI31mkMmSvpMV7ZVAIVpaco6APW0ltmVY3k37eArlHc1Zgf5PF73oIt9r6IsAcryr-8OX4ahOzWUjN96w0uVbsyoQucm86h_y1XvRzIgjCBsorw25dbXRuHHipxkCB7tcjeUhgw4G9ITyMc1CfhO5OEfycQ1v971UpBccTs7RS1kxRoiXxUGVmLMTNc6GimxL68ZBPO6_6Os5Fa7tyPhsqJT76WYgU_5buo-FeaI79g3lNZjs0npDrCxsxF4lyQQPADelzDy-UQt2-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=JxoVFShbFSEee3djOAJKmw9Y_o_bTTyL6Ew3pbNnwE3sCjByPeohhHy6E298AFqTIxg4xsbI31mkMmSvpMV7ZVAIVpaco6APW0ltmVY3k37eArlHc1Zgf5PF73oIt9r6IsAcryr-8OX4ahOzWUjN96w0uVbsyoQucm86h_y1XvRzIgjCBsorw25dbXRuHHipxkCB7tcjeUhgw4G9ITyMc1CfhO5OEfycQ1v971UpBccTs7RS1kxRoiXxUGVmLMTNc6GimxL68ZBPO6_6Os5Fa7tyPhsqJT76WYgU_5buo-FeaI79g3lNZjs0npDrCxsxF4lyQQPADelzDy-UQt2-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_je-cwbDM_a2Hv5s-wxEaWF1WzIG83rI7eFZSsr3PZ6PGar_F4mBGBYT2bS5oQ7tJJ7NRVQk-DK4jwn5ZyW0TJK-2sRwJ3N82Z30NtZcF2wH-ef41yhrAUmF6IMcjiMWJavPDfWdNlVUhg_OWKvVTw1H4I-2vjcPMH84J8NWEhtXKtDGyKZIiwTxZ39kgEqNHgTnfjASo05TLbNypTNcNS8nt43sXVi5dw6Ez1U6YJLIvlWvKGupKPBMVnJy3oGSbVI8iOY4Y_9pbIOs8NVNGuoBQASs3OgNp_C-aPBAkXgJp23QobxFBp7Mn-WA3AFY3sW5P0EIjYvb_dQ26Ov0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKDi0V6VtnZrM4D-Etv_xMpNyWszH9AwQuI38MTOW0lTTkpvJbAZmGdNuhpBaVi9hDy36yI7cFIz47XYBKf-4NkuUa5bwi6Q5iLSugXghZ7fFBCM2p5VEh1pc0qDLz65y_554uRzXrtxkZ96yWTPlwjGiagYM9UziRgwh9NLWJE-lZb5rT2urHlKY1LG2s7OIUO11fKTXHTPTi18NxaR0vDghZ4SMAdukiEgYuMdeBtotdg6FntxLQglREyxKxJBPVfthlBI57-MHbqiPziSm_8CvLu8wStmtY_psuuGfQhT8k2qQcMXL_nPm3pD7_D1zVEKMGn-zUrxwmWGSc59bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=OC8u-F1pm62pwcu_Dj8dhnOJtLJrN1_XTilezzQWql5IcNY2EgIHQn9vURyakLVxs-QsLKo7VY7RlPn75rO88l7FSUp-495vIlKwSHktzxrYhibSHfrNiJ9AlWiN79SJYHR7CPNc_GsUIcOiGo4cffmx08TypR0KlHTzv2RjrRWRXaE04JWuz1EAgvn3RFDGKhPPhbCQh8MzINadyximtCWXZEtMhVPqp5kgoTSbdFNBGi09QLZVL-1vn648nMM9hY_YL7ZdQFw_vmViIp1kADRB4vC3aBw8RIYg4QPwNCaABZBCnxgkWLHOoogM_B3PHi725sx-wMxcW96M8EI5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=OC8u-F1pm62pwcu_Dj8dhnOJtLJrN1_XTilezzQWql5IcNY2EgIHQn9vURyakLVxs-QsLKo7VY7RlPn75rO88l7FSUp-495vIlKwSHktzxrYhibSHfrNiJ9AlWiN79SJYHR7CPNc_GsUIcOiGo4cffmx08TypR0KlHTzv2RjrRWRXaE04JWuz1EAgvn3RFDGKhPPhbCQh8MzINadyximtCWXZEtMhVPqp5kgoTSbdFNBGi09QLZVL-1vn648nMM9hY_YL7ZdQFw_vmViIp1kADRB4vC3aBw8RIYg4QPwNCaABZBCnxgkWLHOoogM_B3PHi725sx-wMxcW96M8EI5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=NZDYO4Xre7YJC9fR1LTRCyI9wQpELb6ZsyYRurJ5fCetFT1rsMa6ehAOBUT-ZcZASyKF0m8SqEe-dxQx_cztERpjARY-ZkXDFMDqn8Gb6ez6x_jk102Vsnja3WFR_HUbjk-pzqUDGSmPmG-0hbOIgmUZW4q4gmoEIOJJ_jLjgXkzdlSkIl5s8DGJU9_rKicZJhfmz-Hsrve4Snkq0mWPIUoRzUYyeiamVhP4S95-5wOL3brGt9WryvsiE6TsoXmQBCHNU1dQ_CxXeojvAa9jLnr9TvjFE2I3CbrR0uc1myvgN8xQHjizCYJ5yPNSG3hb4Wu8TbIounxv4KwOS5L8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=NZDYO4Xre7YJC9fR1LTRCyI9wQpELb6ZsyYRurJ5fCetFT1rsMa6ehAOBUT-ZcZASyKF0m8SqEe-dxQx_cztERpjARY-ZkXDFMDqn8Gb6ez6x_jk102Vsnja3WFR_HUbjk-pzqUDGSmPmG-0hbOIgmUZW4q4gmoEIOJJ_jLjgXkzdlSkIl5s8DGJU9_rKicZJhfmz-Hsrve4Snkq0mWPIUoRzUYyeiamVhP4S95-5wOL3brGt9WryvsiE6TsoXmQBCHNU1dQ_CxXeojvAa9jLnr9TvjFE2I3CbrR0uc1myvgN8xQHjizCYJ5yPNSG3hb4Wu8TbIounxv4KwOS5L8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=X_8qCzibpMKNkithKg7y1JZKdu9_Gvt3hEY_sY5-sKcaaxzT7MJbkmB0KVUHo9gJo16T1HzvkvifJfLmYbfv9g-l5XCA7lGmOvYLCqXd6b_lgxd-kPlbs3NXqOirDwBd7Ga2wJOzoMpAx00ubFlwY4L7DBu3bdeNhCCJdbTqzZizgUXJI-fP8DXvsz2wS6GspxRm6xirovPptEiG3BHZWP3seUNZv7WIsI12Rfvxq5LTdxFEWmo0fanDrSPJTEtGJuh_53L_cujHeCrzMiZKLcyPx5m5DKD7yCMDan_l89GCuAR5WPoo3A9fPzAkGuQckXFJ_t4OiweuZr2oMl3KPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=X_8qCzibpMKNkithKg7y1JZKdu9_Gvt3hEY_sY5-sKcaaxzT7MJbkmB0KVUHo9gJo16T1HzvkvifJfLmYbfv9g-l5XCA7lGmOvYLCqXd6b_lgxd-kPlbs3NXqOirDwBd7Ga2wJOzoMpAx00ubFlwY4L7DBu3bdeNhCCJdbTqzZizgUXJI-fP8DXvsz2wS6GspxRm6xirovPptEiG3BHZWP3seUNZv7WIsI12Rfvxq5LTdxFEWmo0fanDrSPJTEtGJuh_53L_cujHeCrzMiZKLcyPx5m5DKD7yCMDan_l89GCuAR5WPoo3A9fPzAkGuQckXFJ_t4OiweuZr2oMl3KPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCQqaOq51MS6Gs1km3Ewv8FHwmTml7Mp7n3CkEd7uAPQxDX4LbyK2VC-R2zQz4RVT2d_QgTACQy5HAlHxMI9O3zIdL0ktOUevj_ue40QKl98Vritjz-tuJjpp8wZVGgBeevFDMP57wMG0crpQp70KzSsYylX0yvkdla9rMxgmky3kNbCbPnVYhYxDQT5dqORkoqiAjcRtvgXXmDrs0foRHbLn80I08BBCxZWbW8EZpueIrtKf_alNgy0csD_CDCqzy0cYIzJSoDP-63ys08JokDNXCl4xTLA4TcAFHUpmFQH1_Wq9Qq83jZTenpGxMZjq_u4rB6PkpRI-t7dPjH1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnjTBKImQ3QzuV8F5DEZzQGIKh5YL2yrJm8Y0hHDaLngUOVZagXtk6qTTw_y9gKUvOzW4Tn9qvkLOxlVwqCBlOmiqUfhp25GX2_C4-hWd-69Ot-MOOu31M4slhtbv9A5enO_zr-dAP_KiEkIipqIYHcpffndbuKVW2LLKQgTbv7_tyruUjyL54-MwkE4CMNbbYDIY6KXHoAAu3GYWjvIiVLH-MOTKwiaWxu35bdBEhDbTsl0Ky68TikGel7bNRyHwpMEcXYRBdvka7s4eJFH-Iei6gSYB52wjTJHSTaXqyx4xCesrcUIr5zxI9mASv7QC5pp4Ke_Cy99XGkyZ8feVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=t0BN8AKTi2aDUskcIihU8-sWkqh14AXVcLfcfUH15SgQFWnuOJYMaGnUBqSM5pMeU-I5-xzVB3Nzzuxz98ncvf_vm4IlzKp676Q-nV4bAIdRVwhghyzRhw_L1v9fx7s4gwxp6MyCL73yhWOct4MBjB7Aun_lHCZEnvf3C1kfIZ7DkniSWMBvLtvmg-DcrtIns_AD3L76TXQcazGH2LCFkulqA6ZgqLO8oNmc7dQLB0glxsLfvSJRXJprSvz7gDN2VpFO3TfpVNntQhmQaZB2Y2KOWnanTVatA3xCLRoOYg9tKdVFiTifNkH2FJb3z9jnuNufk7fN1_4I7ngVM4sbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=t0BN8AKTi2aDUskcIihU8-sWkqh14AXVcLfcfUH15SgQFWnuOJYMaGnUBqSM5pMeU-I5-xzVB3Nzzuxz98ncvf_vm4IlzKp676Q-nV4bAIdRVwhghyzRhw_L1v9fx7s4gwxp6MyCL73yhWOct4MBjB7Aun_lHCZEnvf3C1kfIZ7DkniSWMBvLtvmg-DcrtIns_AD3L76TXQcazGH2LCFkulqA6ZgqLO8oNmc7dQLB0glxsLfvSJRXJprSvz7gDN2VpFO3TfpVNntQhmQaZB2Y2KOWnanTVatA3xCLRoOYg9tKdVFiTifNkH2FJb3z9jnuNufk7fN1_4I7ngVM4sbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=jkc5hEfDJ97AYioxmi0ifE54VP-z5tUfbP3db--T0UK6J3qcCw3_SDIKsH-H0zwlCzVVymz2dIOAAZzKZ4S5CTqhHqDPuy43atXhz93GJ4woUrXy4ynbt8bF6FbfZQ_lBO8WiWNzkuiGbOnca53Zav9_mhZ6eNo6tbkXNYRVDy7MXrRbcyFV-B0XBg-O5x8qqJ7rpjpPids6sF3TGrpCMrL2ZZ-CoM229nW7Or2-a-CaNRJFOP7IaZmiBFlXRJ42CvFmI7mQTMFC3RLqd5Z--GxX_-vIYsQX377d-CsQLvcjRgzYC12PdCftJw_EfQ6tMj-jTuRU7ukxsVNqLanupg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=jkc5hEfDJ97AYioxmi0ifE54VP-z5tUfbP3db--T0UK6J3qcCw3_SDIKsH-H0zwlCzVVymz2dIOAAZzKZ4S5CTqhHqDPuy43atXhz93GJ4woUrXy4ynbt8bF6FbfZQ_lBO8WiWNzkuiGbOnca53Zav9_mhZ6eNo6tbkXNYRVDy7MXrRbcyFV-B0XBg-O5x8qqJ7rpjpPids6sF3TGrpCMrL2ZZ-CoM229nW7Or2-a-CaNRJFOP7IaZmiBFlXRJ42CvFmI7mQTMFC3RLqd5Z--GxX_-vIYsQX377d-CsQLvcjRgzYC12PdCftJw_EfQ6tMj-jTuRU7ukxsVNqLanupg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpBcL-oA_dKb4q40le2fjKPcPQez2WNxYp3s98_Qk4UR68I_CzD34SwfGy6UrQy6o9vvTCvKZOhnnP0UHRwLVfTUvxF6XQ8cEq0N8h-1aZuU-xTTdSSCeAoLhOqLBTKBH-zhkidkOiC_2dS5eLf-2F-xlRCbPxIQXDgBAMfb1divuLABMLbWaCjH6xJ-p9LFx5IQABr0Ai7QarwmPtwUq7TR-GGnuYDa_k5Twjq2pUE2l-cakXDKCWoeGyhAbyvlQ4lR9UsFLe-fOup1jFCxV4sKQ0CDvOC9zbpLOXpGsoZdL42aBLD8h3S1GetadwhXYT_rEHR_j8Hc3jLcowHQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIv_w5hupqMJ0PCzEeCr0viDZMwMUVemk2LcBb7PX2-Ar-tzPjDNkkbMqf1PNNWqKwu6RQbNu7kWl-Pbt1HT7rUAG4FNEeJjKxsfHp64LkYUQZcPRtWDchI2j1-H0-wSmxpycuj1fyJypg6QNzyv_yhPwaVdCT76pbEg972ScjePJmSG1b6G3Tvwxz1OnIresHxpY-TJtohtV9PCMymPKUO7sWYXjsu6zMdOpV8hDOWcASGxIs5Imd6n4OiWKda-ehH3dRP4ZrG8bME5gpCeUm7M8mANkBiYN_NpDbu9F8MGiOMVdaTDswhTXbwwvYM3f4hbMurgYuHrGax5hs8umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMTzRMPngFbWTmsGuNf1HCClFVWlmTf2hlRiJo2R4N7NKuWV7DZZCBV2HU9TpnP2IvIExiXeEc78x9EQqEcsleEeBTXHhWCRROiFes7B8khNQKt7PdYSZxGPio3rDe4z7vOuoKWSfjMp0A_u5CkbswS8a9v-tfHlY90-Osw6b0deUX2FLQf0MRxyfL8Tvjl8NsR8n2n8jEZS453ucdVWoOXHqfs0IMmJSFT11oUNnn9t4yw_JtMfye4TpdUEX93xOpZhiaqMK0vOodqPs-K37qB8MJLz14XYMXqtQVaWZswl0I5bgOus2m0a2WFx2P4WNrB171qGhT7qKFPE1nI5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7aLbvRZdQnYKHanJwgv7hQfHkM6Acj-CwfVRpLg2Tkyzvl5RLOZeVJf09FzPdHHtwGDPKcdhSoN3pjE-GJP3BYe1pUEtcxB1PN0VHUH5CJpXS0wOBqnnxLVp_5UkBjgwJvjhWeM5vAambbzePV4s2aJYsaFh7THExo8pcI4bSGU8oaqZFeNUTZ8moLYW_XTE6iL8oLQgER5gWfaeu6s_2J2BVsKcVG_DQ-DNBJjiw5r4DzIsW0HFBbVoPodA45aZJwej-znWL0nG5jKpc3oU_jKaWcAA3mGSyzbuGMBdHLUs8hBGKwUMyDBCWAzOIrahE0ZIT-v3vS_LEAcKhmmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJTzIkAbkta5Z5T29PfJsUarUqOXKrsfoNjT5ltfg3DN69LzcPl-25taFFaSVHiSDBvCtMqc9PPlubbbLzFhRbp9rr0o1gvCI8_ffSWYDiyJS2Md4fnqvKAct8g5E5qiOtlPJrQdDM3pNq2QFikv28EfbgY1I3OBTdNBcONJf-6GO6ZHDlLa6DUM9SpOZ1-EHfGQ9e1R36NSQq1aUrbP1QClLdGW--jAq6ys2do8fHwkY_U_TTSvkKssDjsLsHS-e6kd0ze0xIi_BVBwOSPzDY7yMEhEpU0I8zU27Pu2SJxKvyVmeAb-HpedPsU5OSgidfO-63l5FdrbMlTjsHmeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWEuWh_h3Yqw5IwKVZm4QJv3JxZjqhbBR1LdlEk49wMHavBZ9IkgaTWyk_110rPMF_F-6IMDNZmcyHqiSpDWoWCuSkMSzi7zf_SjWDUuPsO2T6B7SM2sH5gLSH5u0X6IhQG7GIiZ-BdoHfzc444lQaQjnmHW7nSE6O731qedrctMC00IvdVFOr8AlAFdvMOJd8QLo_J1TnjxvxhHwtcVUVHKszvy5zp4gSLQp0laTL_f4u2RbbihVNaLOStxELt38z4xGwGu8vYFO0LNGVLAFssuecl46ufz3j15AbS2bTHq_wVD9oh11Q71CLN-Uxlkc1TjNNlqcDnG4WKvIg1eyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ey0riTs9p4Y0JgDkfUXHyjV8vbtyiwYnk_uu6yzqPqxB4uK7o5sEPp5uEr_e4PofhjlIz8yZiiAu8xRrc7OrNa6hR2zqMH_kp5xfEWFUy7PYF7wMnW0upOM5IZ8arrqwovAilW7V_dDMYrY4XTL1SzThqzjofEpGFVR-xpd-1i4E0DaLf7Js1X82VmAV7zh_s6HisG1dfSu2FKnT_byvTbQ8PM0mv_yNGJX1QT_yjmx5rL9xJ4fhb_QXQezt4NXzaeJ1_IKRUiaxqBpgdr04rAzkKE-n25jgABZxlWb85t38AkJR0Xtkd_0h5oc8sLjWH6HtE7gAyV-QwRT-1fZXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ey0riTs9p4Y0JgDkfUXHyjV8vbtyiwYnk_uu6yzqPqxB4uK7o5sEPp5uEr_e4PofhjlIz8yZiiAu8xRrc7OrNa6hR2zqMH_kp5xfEWFUy7PYF7wMnW0upOM5IZ8arrqwovAilW7V_dDMYrY4XTL1SzThqzjofEpGFVR-xpd-1i4E0DaLf7Js1X82VmAV7zh_s6HisG1dfSu2FKnT_byvTbQ8PM0mv_yNGJX1QT_yjmx5rL9xJ4fhb_QXQezt4NXzaeJ1_IKRUiaxqBpgdr04rAzkKE-n25jgABZxlWb85t38AkJR0Xtkd_0h5oc8sLjWH6HtE7gAyV-QwRT-1fZXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=vmx_zNzayelZtyFQ-SKfgJHxWm3NxV1DbxKsgCIbh67PLFoDc_EgcNxhoG3MDm7bzmiDHXKCk6yhUTDb5FGYvPG4238W0Oyhtj__nKx6E_AgInZnE94m27NN536r9sDkL8aCMMObkJCh92cDxZPNUuyxddEzeUJnyoDDBwec9BKOKKmaTeebCwLAAKEOzmfK5vBr_NIHyXB7mSwo_n443Ryiu1JAUi6ff5l7Y7U05hfSqtuMlOUg1Ra1bXRpD1LJCIDtnGp3xTwX1xFuEwEG27SFr_uccf-In8QIZaij1bL3Ozuno5DB1nUaB97YZSkLgxd1qvHkFMrNAO9qcMz3BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=vmx_zNzayelZtyFQ-SKfgJHxWm3NxV1DbxKsgCIbh67PLFoDc_EgcNxhoG3MDm7bzmiDHXKCk6yhUTDb5FGYvPG4238W0Oyhtj__nKx6E_AgInZnE94m27NN536r9sDkL8aCMMObkJCh92cDxZPNUuyxddEzeUJnyoDDBwec9BKOKKmaTeebCwLAAKEOzmfK5vBr_NIHyXB7mSwo_n443Ryiu1JAUi6ff5l7Y7U05hfSqtuMlOUg1Ra1bXRpD1LJCIDtnGp3xTwX1xFuEwEG27SFr_uccf-In8QIZaij1bL3Ozuno5DB1nUaB97YZSkLgxd1qvHkFMrNAO9qcMz3BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=RxdZZZ-i6Jemjfo1GULRrYQ_bj6lbK5M093F1873_fGFDESG9O3kMQWlEhIgQGzCB9xOxfKaKVglGYon6v-cS-hlsQYknjIxVu6z8sWrIY0xBx-WV65ggQSOFk-vwY_24BY_CBsl-S09ywqaMDmZs8m7la3iwGD7RMPpBkTIW-rGXJkAlPc_dlI1P6RvCRT4R00fh9p4VVSPgfVxgqv2oxxsJK0TALbC5IWhoRE8CEV7wbHx_060l2_Q9fDu8mLi4-NDIAFZufofPeTIcTFJUifXTFFe13K9Ys5uUck3OglG0s3za66y3-AuU-OcNK2sNmEk7P_QQDflg8u3d-ydUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=RxdZZZ-i6Jemjfo1GULRrYQ_bj6lbK5M093F1873_fGFDESG9O3kMQWlEhIgQGzCB9xOxfKaKVglGYon6v-cS-hlsQYknjIxVu6z8sWrIY0xBx-WV65ggQSOFk-vwY_24BY_CBsl-S09ywqaMDmZs8m7la3iwGD7RMPpBkTIW-rGXJkAlPc_dlI1P6RvCRT4R00fh9p4VVSPgfVxgqv2oxxsJK0TALbC5IWhoRE8CEV7wbHx_060l2_Q9fDu8mLi4-NDIAFZufofPeTIcTFJUifXTFFe13K9Ys5uUck3OglG0s3za66y3-AuU-OcNK2sNmEk7P_QQDflg8u3d-ydUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=SeUozobdwc4wXtrf8zoCWUxlLasfQigPXxZ-PYN6bayQF1D5DzQEKsq2Ds1Uv9pv7zLgu4EFKdhNy4SDXsLfxt62m8wQEYGwYlALrxhufMy7_0LGnjxi9qgMv5WKkhMQhbSnFXScl9qcDoe81XPq8kM3lIae19uqrZIbqx55A607Iu0ddq2KhVKd-0TvpDbXJdwcG2ilRPkq6ImvJHNyX0wgaPc9ENSqQ_N11FgdGT_MD_avYcKwuAXu3cWSX5x9tUyEc_foxj2ImUuvUxCyf7Nofflyg59xPTmzkXokU1y4Ni7-4lLpIHutz736_jgEaRoCkyu6qwJsZdT56YGsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=SeUozobdwc4wXtrf8zoCWUxlLasfQigPXxZ-PYN6bayQF1D5DzQEKsq2Ds1Uv9pv7zLgu4EFKdhNy4SDXsLfxt62m8wQEYGwYlALrxhufMy7_0LGnjxi9qgMv5WKkhMQhbSnFXScl9qcDoe81XPq8kM3lIae19uqrZIbqx55A607Iu0ddq2KhVKd-0TvpDbXJdwcG2ilRPkq6ImvJHNyX0wgaPc9ENSqQ_N11FgdGT_MD_avYcKwuAXu3cWSX5x9tUyEc_foxj2ImUuvUxCyf7Nofflyg59xPTmzkXokU1y4Ni7-4lLpIHutz736_jgEaRoCkyu6qwJsZdT56YGsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=uL3P4eMqP5aIqLLiLdpMI8Zzr-Uok7NWB8H-0GGmvHcMMtPZC560pfhvqgzpqaWgbvMKz16mYbsVAMR2Bw7qOyg8dtisXqRkUl4KYmTs1T_6tBIFySmJOLKwU6NNmqpsqRu5-PYgkLAOtu3fwiGwgRSyUc0nGtc8duKp-1IPxKSS4IfZWOadFVrjnhxZvxrPHEkyINuPXVUxzygDdzy7PqQlrZWsxXaaOkQuldxDtzbpahKHdBRqR0aZ9HNKiJLa26rRtlvavVHVmI7MlmZN5GmQDLx5EizBXpcod0dEjmXUwbLlS7vhz_tJyMyem1t94SNohFyMcR7njB89UNTanw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=uL3P4eMqP5aIqLLiLdpMI8Zzr-Uok7NWB8H-0GGmvHcMMtPZC560pfhvqgzpqaWgbvMKz16mYbsVAMR2Bw7qOyg8dtisXqRkUl4KYmTs1T_6tBIFySmJOLKwU6NNmqpsqRu5-PYgkLAOtu3fwiGwgRSyUc0nGtc8duKp-1IPxKSS4IfZWOadFVrjnhxZvxrPHEkyINuPXVUxzygDdzy7PqQlrZWsxXaaOkQuldxDtzbpahKHdBRqR0aZ9HNKiJLa26rRtlvavVHVmI7MlmZN5GmQDLx5EizBXpcod0dEjmXUwbLlS7vhz_tJyMyem1t94SNohFyMcR7njB89UNTanw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dSh9qUz4w0meKUJaLbqcFo7JiRv-5pajA2Vayh-9Onhu9d-8dveGIoaGt91oA44QZrEKqRDbYJQ0c4K_owm6IQBxOBkoEd_AXA1dVly12fPWUt4tyNojUmvXCO201jnigHCtYQ2kD_yGQsnuspZAfen5_2pVMHPQoFieeGMPeQAd04RHAPjHB3iqMjpS0QD7Ve6jqAZUyoclBcWtMDn9P28iIk2go1IGN5hgK9An6bWu7b6Mnk76uR_jC4bAiI8URVGPRLJYPX3bIFKf0aRQ8f-EJlH-EidR3mxr-kCKYFfeMFaIO9h0KP1STqVMak8QpVHIZn4be4giuRWWBv2Wew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dSh9qUz4w0meKUJaLbqcFo7JiRv-5pajA2Vayh-9Onhu9d-8dveGIoaGt91oA44QZrEKqRDbYJQ0c4K_owm6IQBxOBkoEd_AXA1dVly12fPWUt4tyNojUmvXCO201jnigHCtYQ2kD_yGQsnuspZAfen5_2pVMHPQoFieeGMPeQAd04RHAPjHB3iqMjpS0QD7Ve6jqAZUyoclBcWtMDn9P28iIk2go1IGN5hgK9An6bWu7b6Mnk76uR_jC4bAiI8URVGPRLJYPX3bIFKf0aRQ8f-EJlH-EidR3mxr-kCKYFfeMFaIO9h0KP1STqVMak8QpVHIZn4be4giuRWWBv2Wew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWE9NYvN55ZKSgf3qSWXZ8AAI5uF2rIMIrv9_K8Q4KHv7dx-9zuJAgDpgDPH9ZAQW_1QOpg5au97219kXSA8e1vtUOWPKfrHXmKYN_PzYMzYXw7b0rDrUlmePwipch4yuQA8Vwoo-F-Du9D7U78DTt6dZK4VIkD2McFPq-L_zKjw1TOXmhWfR9P9iq7bis7itDvksD6wZYRo7ufDYYa6l1XO83XITgKCkHbdkQIbWUFU_J7rb79Y9dpIeBD2ff90JTefivHbOn9jSzag8-xxQNTHMhjM8LRciq-3MnU_3F3AoXvY6Mo02BresY2jr--szOjp52iUzGmKcNteGZZR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=ideSGis2HCeBskGevg-8Tuq6EVxVrM0PLKLXjd6hbuH6tOfxO89NbD3xxu7F05xezpPJ5x7gvJasJIB1pXb7qYYIRSCetH1MuhIOc10eeNf25HkfGVRUTaHkT0ml2BOhG7LtUfIfEnOKlkfd7xuvg2BYA2v9UoI3jmRiYZoU6-FYjyd-0xAr567cfSxt_FAxMmW9PQX2zPcxefCSNBcT3ucYRgfbFw7lPS9iICHuf32m-FBKPUpG--yuh7hrGS4L_KxsUgYn_kAjvGWGUXcmZ2sHUv2wqjOhmBLvDI-10b2MVVVtFZ2Dyxf0yuhwZgzUjSxKTzeaZfCVD9MZfRFIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=ideSGis2HCeBskGevg-8Tuq6EVxVrM0PLKLXjd6hbuH6tOfxO89NbD3xxu7F05xezpPJ5x7gvJasJIB1pXb7qYYIRSCetH1MuhIOc10eeNf25HkfGVRUTaHkT0ml2BOhG7LtUfIfEnOKlkfd7xuvg2BYA2v9UoI3jmRiYZoU6-FYjyd-0xAr567cfSxt_FAxMmW9PQX2zPcxefCSNBcT3ucYRgfbFw7lPS9iICHuf32m-FBKPUpG--yuh7hrGS4L_KxsUgYn_kAjvGWGUXcmZ2sHUv2wqjOhmBLvDI-10b2MVVVtFZ2Dyxf0yuhwZgzUjSxKTzeaZfCVD9MZfRFIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=l1LQIJUQ6dRqxQlxPa2Ccwqqu_pGbLlSNc77dPJelWF_Eg6UcCEkQM9ZXWjCA2zjkrvbp_R2-3rR8n9fpNYLgIyBDx3mDy8xD8FbLTA3mkHZ1pq0QK8mV2DC827PJl8gXQ8EBFaNBoZr_w_EJKxg4uXHce3F280G72gjR5SaULMrXgCSq9KrZ-5bt1vPJoUEYGXLTE6WB3RV_yjghGjTZAgdyIwlM_B2uk-xHC7b1wprQN1r2vL6TzqzIRR7DvWkcZGO7f7_kf1I413LhRFwvm3usbgmeQmSZWcYFGWwHqtb_aHmjLusktjbl1sS5hBKm2l0FWzbjU4N7beUpzzXlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=l1LQIJUQ6dRqxQlxPa2Ccwqqu_pGbLlSNc77dPJelWF_Eg6UcCEkQM9ZXWjCA2zjkrvbp_R2-3rR8n9fpNYLgIyBDx3mDy8xD8FbLTA3mkHZ1pq0QK8mV2DC827PJl8gXQ8EBFaNBoZr_w_EJKxg4uXHce3F280G72gjR5SaULMrXgCSq9KrZ-5bt1vPJoUEYGXLTE6WB3RV_yjghGjTZAgdyIwlM_B2uk-xHC7b1wprQN1r2vL6TzqzIRR7DvWkcZGO7f7_kf1I413LhRFwvm3usbgmeQmSZWcYFGWwHqtb_aHmjLusktjbl1sS5hBKm2l0FWzbjU4N7beUpzzXlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIzapdwmgjmBuQafh0JwgpAsQyFcxeGRG0QNRjr76osUreIdC8BiHGEelQS4ZKporRvEnFFMrSAkHvsxSHHM7Ad5djQbjeGgCIKo9Cm2uKWHuWk1Sf_3Fk51ba9vOv_NljF_u6YAGUUoQNhvnyJXw3a6TprIR5Yur8aapTOmqV9bRg-K8JleA_kVNcJZHsQTCxetCGRv07NJxP8tFiq6SGs8LCoi3nS9DE29Sg6SxCNwuhz7MPS5-6rKCFwIsB129GBT9sUkqLJa_80cKQsUHLy69EhTpXxoGp56oottNbqzY2SRgznaTBQkmxEZilPextrWMqruQXoxYaPB4PuA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3alMNHnxA3RfpCbBbanALo1myMvwPMs5-bLJP5CVaVtIcCwZ6roKYkfUHBMcDu4hfP62pUSEXohIB0jy7O4BuM9c0-8BrQgV0Q_9U7veP4ITWdYp0Q8ADCH5omoe6VRkBWwD6O1Xr7IXqLiWXJG5UqsAkG28kY33Gq2PuX9xMQS5EUrrmyyBgfr3evQvCxG-In-rdt2YkyQLYEsCGkG9foCsh9CHnwEmOW-NOuygZV6D_dFwwZRURqJ8HZmUotj2Fb-GJNq-x_MZIpYFQd3IEVd7ggAHUDBUlCEMrKGMT8X7RdmLhf8G4UqRQxnKSZkXW7zJYlDBfHceUAUHp33Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHJqRLDL9qGlakVvKNgzFUIjU4q7f3PKcBD80PKJ-gqJgERzRlSu-9A9unY7Lef-wIycoPrbCYDX86p2EiU8Hb8d3u4ds1mYqaZrJ7eans7N1Ef4d-dbmToq946cP7ECtXMEoSJ4xC3Ciw2ex4tgyXuevTelLCzukj_lX3h3gQ1OpilbcjwnjkJXAkZpD0obY_-qzwrC4NTnczp36tY2X0DAp-py2K8Kx4-733J94OXk_ZlfuR26np-j02BFbBZ1-oEiNfrhx5yQdE_mLHOitsLoWuc7AICtWgzFk7FWwRV8VW1kLu_W-OES80MsMB3ccYHY6fbG5ld2vPNNlbpf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPkX-cU737ddDQAkiyi-oqlXV_zlQcfaOiguCaTKEAyI7TEfQFHjd2sS6jma4y7syZJybpinji7zoPYLuA3OUvOV_TpoWn23LfiuGtv3zJmTYdlfxO-fj34LE2W681OEGbV9VmHehB86Wh1GRycH144OAMBA1iMVPzy4AqqmOXcgCE2SR9-5ZCKRgrmNyi6dATNRzvgsg7O9RLqKy6lVLHIjrGH479HUy1v1tYqeWteReGUsJ9nXQ9gEFalDWO8AEzKBoz9x0a6Lt1BpjkJxo1k_ovVfDGhHL3EMCM6aQ_Z3xCmbuiwu1Rxb0pA22CUAUgRaCSVJVmY1YnnAnvc89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9qS7Sxo-9VuqORlrGPvMwmlBq94TVTYK-pUkQLS_HPttNnxodjv4UnxgZ5lcf6hSw4jnzJCPZqOIbRndYpI4l1J_TXXmS2iYHn5jlaG7J40dYvtWq1l37mXbsR_24kCKR-4_kl48RrP0pHBc8CVppEgAjEL5mmri_e-3l2rggA_lEML2i8-sfK5C__WS9gI_M_NxO11Rv-QEc7B7NMFe3AUk_U8ovlNugxOijjJybNPoQNP1tfslDFQmWYdymfRQHD--dugGoGlVNixticaIoLKW_nYYae-YtlhyFAoRjco86NQL-jsUIhjvXUNI4t5Jav9omKYC8-XnoV2lFwDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2YL2nKSbNzmXChEZox2EovrnLJ89164b3f_vDBc7rlct82cUcFuljkHvIDZsvKP7SZugG69kdzWmduWGn98Wb78N2R6WHFWak2mR6HUsuDmH9juvfr3CxGrtzuYB5af-_ftI3euo0j2GDa7e2Cv9JGZT0rEwrusKGAxuYTfofIooYmgSbGRCrPt-evhAcnKt0EOjlq0U5e0e2TRFSLPHzF4hRorhq_mNfM8nfkXNXZJa-LDpY8M1CmC6FJGgdn-k1VXjt3ZVV0OC35wW0hVk5-WO1oE4U2ZF_v4jbiGlWraA3bE9OG2tqXRfrxA_P3rEKq72CtWCO-Z3fZhdxY_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmVGrrbTeN0C5yrPa3pS6YoZ-GFFSq1gcXQEbLf_J7s9HzVGHSZbd5ZrvuJZkey1Qamk1Guk2IbYDVoFN3Sun7IobiBlsNFPI_SsQo_tIKHwIdmg7VMYI5XI_H3BZVXg2kiCp3ecxNk7axocy_Hc1sMKssU9vXe-8mW4_BHrSx3ikpXmigoAiJjhK1iXexj5ZhMk-uLiMI9aecCQ89RztlthH4XNZaDCyxUwUTutbe6HYGSz8XF4e1N0zZWB8XtP0i4b6RqmEeW7aJr9aVU1ec4KduqDpBvK98WM3dT1ISmiUZATTVf5B2qkj6AhsVxjcCDNX4Srvd_a_Fi4E8BJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLIaEyy0LMEovMQ_6XoAfmvmEzFlO_94bEzeF_SnsXTST9NALxuH_MFmWVAbMQjwFl-_um1wLMQRQJVEVer2Wc5Wl97Q2sxLxKJcZI-P0hYr0qMKAz2oL7GHBAeuqukHkbE64cKKaogOdl3fvgcYKfxHdcQde1Fm5C-XfGKie1stDMnKY2U1_x90vMAMMIKwBSJ2Ze-aTQ5sT7wFKiSaej8j2NKzlzStLZZMVthULJ1tVm7vDpehf7LHBilOm4V9cKuv6HJMoIspDrgQG-puy7QZ4pTRWUU9L4ybMvu_kWsvWBuzP0EiF3MuJbqkqo832i2Zi6s7iRdwXv8EzU0RVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSKi17HRNFZhmJZIMWrSjN0VakwU1R7WenlpwLUA3Wm4qz4FXKadcrbzboPPC9kTswrnwwSAH4cWxir62_CgNv9r2czbSKorlwU3NCQb0W24g-PU0M6z1HApNjbQCwu-X40L_jak7Dbrd9mpOa4pLldTuAx-REHVbf_vVZC_5x0FTtCWM9KCRfU0FWQI6U3VdAtTbAHpKxGJTB4KGj9-qvXRouhbvK89uu2dA42AnVARiPsyZr0Om2o8BYf7Q6fMDjZ6_QbT39fX4qwmI62sHwlAnkO3jD2vdTOzzBnJhdBpiqru1_ri9YXRP0MHcI6ekdJ1LG8-SjDMbPOvJofsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifnz5s8njJhsfwZG7uRB1wWmikQ_5tNFDZ68DwbKb0CprMe_cW_QeZDySJqY2LQlK8E43efiKVClE3Av_eA-a1VRMpzBBIiv6vIP-1kS1KSK6gqzlTTtyeCkfKbU4m7Y7fV8D7pKSc-ttDrMusa_JY_FrXKJRN2-LPJ_qGJwee3l6QcPaY6vQ2hjgKcdLJ9IcA1aoIkIs1JfE0QgBdS4MP_r3orjCKldPeCWdmZfC4OowIWyIKUzL80EIiuLtVOqUUKRexvgw6ekZ9-Z1yg6UVzQ1MKGP3ChosHv5wm5S6ybe5k_be2CEHbko0oaxa3rYL1l1a06NzBlN4h9Dd6BjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rThG-9ENnqYevpTBrucjsvkoGEcEvS5w3tVeUItZxHBHys1hirTVr0CqeTSJRt4gJcZkKZxqIQJAjKhAEUgwhes_BRgIrMf-13LDxVPd9f-1muT-5VHe_FuoxMPaGe38_XfRduI72KzF1ld6MHgCri5sOJjrnM5xMZjfrZw3e3oDBpQM5Zegof9l6rdoq1YykV8Shg5mJy5q1Dnmp1SgOHMPtAB5KdpGzoKi3i_PS9sLTro7876AgErQ1NyBbvoVvVVY3a7ffY7hjzbaebkRKl7YMSQjuDLbKCSQfmY0GtPgv3ip5fgtK67mj5mePDOL_BPD8O7Wk-eqYMNI7YK8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fysMwPuSA1WB1e0Y1sI_u1pTQpGEiOxiIneULgAejZ72dv3u_5_0ueUE67wte0_S_oU7XAWhCPYyl5PzI3SOVQlnWFEttUXJNCTklSfoe_kcSiOT6BO6cm_xZN7PRzwd31qE9WJLGbUZS9tIpOJ8XPONJjz6NvapPETsJJ1BeuyV0L1_m28b3irAvtsmDZeE_wMZJ7HGnhJmIQvpx4w7f3ZZI6dNTE7KqnlFCkDoGV8abLMvCieNh__hAWXzzwI2DzfzYH6UbaHp-NZv-9NDLnCW1VnkIa6BsNwKx8H5UfT_JWzb88oiJgXm0z8j4X5ND9ZKqQh7cXH_VRCYInMZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ScNqawqCAoRQYOGaDp8NNvE4Lw51qh5JlCAo2TglByr59naP8l8AGzTCSafFKDr_DRi_KlmUIVWia25ObRYcCelgsjNRVQto6nrSg7LvYeeAxvmIpcGu3g3Hpu4nMOti0t6DzoYTa02mzopnGXkunybkwV_M2OHpfcxfuq_eoQzhqrsAYF_exP2EFZErt41y2vfgKwND7tUVaqwrAAjhpCapP3H0KaR2p4uY-NKRdsQPClP_NXMpvfCjFvWIQPbaSwAzd9Gi3Gs9XRR2c_v2mfr2FUhZ_SN2Vcq06UZHCr1CgNUSSSPp1AI6r-NDfOySuk2pbT8T-iQYonN_pkaBvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ScNqawqCAoRQYOGaDp8NNvE4Lw51qh5JlCAo2TglByr59naP8l8AGzTCSafFKDr_DRi_KlmUIVWia25ObRYcCelgsjNRVQto6nrSg7LvYeeAxvmIpcGu3g3Hpu4nMOti0t6DzoYTa02mzopnGXkunybkwV_M2OHpfcxfuq_eoQzhqrsAYF_exP2EFZErt41y2vfgKwND7tUVaqwrAAjhpCapP3H0KaR2p4uY-NKRdsQPClP_NXMpvfCjFvWIQPbaSwAzd9Gi3Gs9XRR2c_v2mfr2FUhZ_SN2Vcq06UZHCr1CgNUSSSPp1AI6r-NDfOySuk2pbT8T-iQYonN_pkaBvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=DCWPEN6G0gv5R_dIXz_sa0w66CAVxQZ6a909yojyaISEUEksFNMLrc9aaWitOZJT4gr85Kf8bvvDPpzhTvVnwxmgW_QYX1-e-uu3hWJuAWN68O7vkLMhyhe4SWZzgVFlNvicwTsyWekhXiXSy7c4Rfwgr33utWs6lz6V12nQsj71gMKNC5f0sholhNXaYFEXeIvtSHylX2t9NuLejrzXNEoWSGrzp_LqLMyotb2-bQ9qmBcprI-AdPwHuAtXYVKJ0PCjjLFvZDr_M8zO6e-YLb6IhGeRV4ekyztwBpFvsbutqVBnhN3umJPUokYTVTdo9GLof2suXhUXexQ68B5VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=DCWPEN6G0gv5R_dIXz_sa0w66CAVxQZ6a909yojyaISEUEksFNMLrc9aaWitOZJT4gr85Kf8bvvDPpzhTvVnwxmgW_QYX1-e-uu3hWJuAWN68O7vkLMhyhe4SWZzgVFlNvicwTsyWekhXiXSy7c4Rfwgr33utWs6lz6V12nQsj71gMKNC5f0sholhNXaYFEXeIvtSHylX2t9NuLejrzXNEoWSGrzp_LqLMyotb2-bQ9qmBcprI-AdPwHuAtXYVKJ0PCjjLFvZDr_M8zO6e-YLb6IhGeRV4ekyztwBpFvsbutqVBnhN3umJPUokYTVTdo9GLof2suXhUXexQ68B5VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
