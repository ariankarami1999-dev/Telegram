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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oppeEoUD_9HwzRuT5lHD9hJGdJSWzR73zm421BccgbB5swGpxV3OiaYKzdIRNCk4-IfIlx5l1gL-Zz_MythWSY_wDKFwjawIpERM63KW7lA-ImXtXqV_BTJc_Myk8V_hBsQHuv7zn0Xbv0qjWmhINC7bgoV_T2pqe2hzMzr9ZqDkuhAZySSM9X2N25UEdLhR3G6qIoQmkVdKo-BHoyHzLK3d9X7tVV1R1_-TsMYJXy9dYxz8L3Kp8rjzZ6CiRm3Dm77H1608-quznIbehGIffe7WzBUB7ZM3HqyJIVD07iJx1-gKHfg-NPKUNcfS_tXaoEaLzaXrCy4at9nKB_ED8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKUB2NRc8rxuBLd9M1wY8l5CQIqddrDS9sQT2OanNkos290UvI_9sDKRIFP_NWr4dsZM4KMsYaKvphn8mYNLVWFyDd1JBzyfWPQP7uDJaKtj5_u3L3-x0tDpk-hVMej1mE0B7_2uAtH_aKmUcV1fcvsfggM9INFaSWVaRNTpsbrQ7oRMJ5--HWtT_BBCYsa1X0n8KW71-egQyjujBDctMKlD6mvABSEv82OQ_Nu2_CHJFEbhR_vQeZyRwHmIH2U43ke3zkPkjXO9uJHB8GLYV6RQg3e7m6i2G4BqU0Ftt6aMYx84zw8PGn4QCqqBq9teAFAErmb4XRT-SFbg6nzPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxqIbAOvq-PxbFw8FqpKkmHwqmIV58lpTJUoyy2ztAaAlo8oulZo5IwVp1B4OwNybq44wADWkxgu-zG06mRQdqRCrX0zyXPtkbcRYCKVgYNMy0izIwE0j-kjbHyzsFo0C9CKclkuE_TDmfwS26ruauj-KtJ2_kwJxieLsTc3Pim9C-kVJ0Bvlu8wMeAGo4S3iJlPyTNlgpG_Bo8MVAhTx-yuivh-kzTpyKILRLFQs2Sja-uZepy43cvk03njA5vB5Ijm71GTTMzUkSlqxwoJMl3PGPriaEKGxnapjL4nNHIIOJrC5A8mfmpkFf_BLkG6EhF5P2jnqHuOjGZwE3l4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=U-RBYqVrWxkWSw04YbVXLQ2_ykOF7JWXPb5BmdmaYDeHIJ24IUkWgKq_aa_jdgT-OCWf-TYFBiRXUsPWRaZpruM2qUzvIviQ6AxH9JLQh4GYxYAzMo4IzMPzXJA5VrDTzJQj_nBWsqnu52E7wYUs2fKpooisda-tlF6szolG-Ibye6QpxAAD17NLh0Df1jpD-Wr5h0P89DioijgP6kXldkWUnxkQB2e4nxk9-pxOpSuM0QCrG4V1aqOWJlMc5JxhQ4Xe5tiKfJZng6mgFaip2PKxlPfUbJGkwiODAJwm3miLJIym0ni0RD3JUgVirr03eXVqHkpx_CubcbmrgNNFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=U-RBYqVrWxkWSw04YbVXLQ2_ykOF7JWXPb5BmdmaYDeHIJ24IUkWgKq_aa_jdgT-OCWf-TYFBiRXUsPWRaZpruM2qUzvIviQ6AxH9JLQh4GYxYAzMo4IzMPzXJA5VrDTzJQj_nBWsqnu52E7wYUs2fKpooisda-tlF6szolG-Ibye6QpxAAD17NLh0Df1jpD-Wr5h0P89DioijgP6kXldkWUnxkQB2e4nxk9-pxOpSuM0QCrG4V1aqOWJlMc5JxhQ4Xe5tiKfJZng6mgFaip2PKxlPfUbJGkwiODAJwm3miLJIym0ni0RD3JUgVirr03eXVqHkpx_CubcbmrgNNFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGG0l9KCBFHR-zb-r2yrtp48ngeptT_9VjlOzNbYEr8eEKgEiZGx53dOpUkeHbyxyyH4c8NkD0QEEqYwnf_V0s2vlMZ6uKSSWXtAM-nNMm1ovd6y4YOQRmeBl3Ku2s942uv7HetseO3CC6eSnBRHtVFEhMQuEYyHMsvCQSOJOtmfS0CnWa1jg0uWKmWPG5QNNqW3d9vxnl6iu5s6a5k_aCZRvIV-YBdndYVX7patvGzdW8k-X_UmrzDthhUOu66e4c9HDWlvBeJYX2FAjQlRLptPmqDdPwvlgba3O90YmjjrlvqQ7KxpmmRscM7FPqQahxYjRMSn09J4JV-Tvni1Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUCMMAr_QgHwZQmzKcWzjj3Fg9Sfbby2ywJ-ER2_crReuN2r24U-PhUS2RbbmodQ5NeadJY-ZgA4ECc2P6EDq_29tBZCUWAuzqO0yrovtYDAB_1d0-gV9AuHw2KiAzKTaputtM75wPtY_k9clF_CRN4jI1kkYKKNgrYvGX5NInDoMSmmYYN3Yb7GPjPtt6DkrZvt2Ln0Mv_D-UomJkD5lahvYlgdq0B1Wz-Ve02J5jfKlwRK3TbFXjY2enkznwPZgacYd0KLWpVHSM8sCAIPvY24MXwBzBBGIJvL7sDGcXDDtNwdiN5qFNcBjG-EWB0COWJ0inUL0zheVC5CJDTEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwI5-G-ZuaELprKKrZxW7f7-_GlRjHLUWFO2QYfWrGinXgf04aBff3l3KyQLnFJ2WidRmj_yd74rKjlS3CXi35ipM8DaE2rqfu5GLvGkZeA-cyP90Oqv_6vHhQvoAeZr1Kz1IksNjFvdvpq9Ac4meV8YiUKfxhNTVrA_61Cw7pbq4ay2OIa5CQl82zBzuDXa8ao5ZYdk9AlkmERPNZ0u8mw4uMyiAKM2DHE8V3wHOpBmt4NJIeukvYaCbSF20da6jxGxQ21Hui3S3lAOT4KR1JCSoVQHaovucocH_v0GX5UWFEiHrhMrF96russQBx0KDhvN7itgd8d9n7ucDD31og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnlQlBQT1TCo7b-evAXJ_dhlY3VNPZ6mmwMIkj_BPdPCJ6qy6LA8w5rYT_k3gMctR1A74awV0T9IfB5dzxPAmfnVICQKh3nqJISnEWBAPKBYCmEHT-usBSEjSQXteGacdnRT1i9hBDcRziYtZoNyeGkGbCJa8A3aB-BYmLWvz4ihW_pEw0GH5Xe5J_Rt8QnNiZg-9nSSIvjW-B0aKioMKp5wYEdqyOePs31DVh1EvH3J36MqkLY2WKQBPFCgyuJ5BMq2weZTVDxTh2AgvoSgiE56huT4HbGmcSjbkq3Ovvy-dBdLbxASEEK5t_rSgGfdmLqlZd75hp1xmHDAdzPkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1LBIdbBcc1R0E_val7-OgmpcHVjL2V4_BxY7KkELEeZAjNzYks2NDger_Tfhh-T3XKZADsdUtqwpVxkl7O4FrhR09kOanCga4PzyK9HpxVQsxy5c17PSrbZceJFqOkoyHdTxxW76DtK-85VuJOqA4FLNTtCDZCT-OYO617T_8-gjTJHt4vkxm16buuS3mclui0hcOq6KsSXlALF3Fy_8rWPV9igdbHEAzQLN06ZzMD_Xj4lEgRB4KDWuHX6RvZU4D-JY4kC9OQVmTS1weyZhSq-7rxh3NysE8uyMrwlSNEWmOKbibCD83NUw59DMwnnJ2S-MbDYBpHrS9y3OEVF5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=LQnNw8u6i2VWG-1f8_JZo6Pk5Ff2mjsGFwqUmebkg088H9Cz1dxSnyo_tiqqGPAEzUbfcoRu8-uPDmGd_4-I5MFy8VLHctoEdGCzTNA_VbdKrDXhk5ZShH7rAP4oq0MmInPqfXzt1qSnkfEHXkxuH88NLAPmkq05KROpuYvIr2MaromdWCmHZaPeI4vwY8GmrcTYENMV8JbCSKzPN66bXq3zIlPa66IFdbVxLfyc8Q3A53WqUSHsxgI1sdFIrh6p0EiDa8KD7ooFoBXHxJqZrR4_6frPaGZqoCjAqSpo8qO3gFc_N6VoNy24xFzs_rrz3psW7CIYjlQcqSwcm8ZSNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=LQnNw8u6i2VWG-1f8_JZo6Pk5Ff2mjsGFwqUmebkg088H9Cz1dxSnyo_tiqqGPAEzUbfcoRu8-uPDmGd_4-I5MFy8VLHctoEdGCzTNA_VbdKrDXhk5ZShH7rAP4oq0MmInPqfXzt1qSnkfEHXkxuH88NLAPmkq05KROpuYvIr2MaromdWCmHZaPeI4vwY8GmrcTYENMV8JbCSKzPN66bXq3zIlPa66IFdbVxLfyc8Q3A53WqUSHsxgI1sdFIrh6p0EiDa8KD7ooFoBXHxJqZrR4_6frPaGZqoCjAqSpo8qO3gFc_N6VoNy24xFzs_rrz3psW7CIYjlQcqSwcm8ZSNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=lCduIr6oMrECraPXnUew1WPFQoA9lSLjgmQX8BQZzBhHgvSTpeCznzBXvEz11OlH7_N2d-tndEcbruvcSHEZeHJiTVp3vcgAK9jpkD3u1EeCZgPM74YJxSCm2MFWAjuGaJ3C46sNoqtfjYpNJWbByjm-ywUE7ebzNFr2-uZS9vpNA_httkVrs9_m06wZQYMnfL8pYRhdzGr_abSjaP_e6qo6zVxLQjevRZmWOiuKOrVCXfmz1HnVCUd0UT4XmKVUpxWzQ3kM8gJWocyHssP6jWrXyt9q1zftHLPruyYyoPVEC5bKLETDACw_Nuvd2UuIOqQG5tcTQvVm4AKjzP6Zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=lCduIr6oMrECraPXnUew1WPFQoA9lSLjgmQX8BQZzBhHgvSTpeCznzBXvEz11OlH7_N2d-tndEcbruvcSHEZeHJiTVp3vcgAK9jpkD3u1EeCZgPM74YJxSCm2MFWAjuGaJ3C46sNoqtfjYpNJWbByjm-ywUE7ebzNFr2-uZS9vpNA_httkVrs9_m06wZQYMnfL8pYRhdzGr_abSjaP_e6qo6zVxLQjevRZmWOiuKOrVCXfmz1HnVCUd0UT4XmKVUpxWzQ3kM8gJWocyHssP6jWrXyt9q1zftHLPruyYyoPVEC5bKLETDACw_Nuvd2UuIOqQG5tcTQvVm4AKjzP6Zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=WFROWb2sYz6OKRTlo0CREw2RBi7jSJ49mz2ADTtxpKUqaP1tkMIcuFrWaHftYkNOgxMV-ywyB4tEMF2Y0hUVzBnZAZgmrAimziqGsqXF1Vl9rvvHq8AEQU5hD3U4PwemadBTu7jmglhSEWnA1HtcQu5-skeRNzp1Ss7B5Xl_Ef95fEGq5oTJcQ-0oIZkkxgblns0hMvgi_lpjS_8xZwfaLwTw-EihJv4liTDBd9KGAK6Oq7TvEODkOH_rD_UOrnOEIc6eleSkns_FG5WPmCTumU9iRl69hw-3pparM3Qqm_VkioWMlB2lS47cDAQoGrZrj5YoMc7VMTA4wtRf8M6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=WFROWb2sYz6OKRTlo0CREw2RBi7jSJ49mz2ADTtxpKUqaP1tkMIcuFrWaHftYkNOgxMV-ywyB4tEMF2Y0hUVzBnZAZgmrAimziqGsqXF1Vl9rvvHq8AEQU5hD3U4PwemadBTu7jmglhSEWnA1HtcQu5-skeRNzp1Ss7B5Xl_Ef95fEGq5oTJcQ-0oIZkkxgblns0hMvgi_lpjS_8xZwfaLwTw-EihJv4liTDBd9KGAK6Oq7TvEODkOH_rD_UOrnOEIc6eleSkns_FG5WPmCTumU9iRl69hw-3pparM3Qqm_VkioWMlB2lS47cDAQoGrZrj5YoMc7VMTA4wtRf8M6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=DNn53a28HHeBFn1zE6XlYvyfhO9-2UvEsNwsOWALQ99JIrMO_TetXF5TXsJdJezf8PVCTUpuiHRAl0PZKkNEtjL4ZMH6--_dSpRnv0zcnOXFLyf7uTgMwdvp7MYaABDB4l4b_hGWV026XFRae0J8N40SHXKBCATj8kSTkk11ydPUmAuww3zI8gwfwCtuB1C9VCm8lH1ufhxg6DSBbSdfAstZYO3Fr85GhWnf0K882T513w7miWnGlJ7M3vEzS8L_JsjtGEdz3BjQN7nABJSWg9qfb9sCVcErpYWGE_x99dlEPpYdg1OzAvkLCX63z5emIsvJvsP5cw5pKO98M4asAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=DNn53a28HHeBFn1zE6XlYvyfhO9-2UvEsNwsOWALQ99JIrMO_TetXF5TXsJdJezf8PVCTUpuiHRAl0PZKkNEtjL4ZMH6--_dSpRnv0zcnOXFLyf7uTgMwdvp7MYaABDB4l4b_hGWV026XFRae0J8N40SHXKBCATj8kSTkk11ydPUmAuww3zI8gwfwCtuB1C9VCm8lH1ufhxg6DSBbSdfAstZYO3Fr85GhWnf0K882T513w7miWnGlJ7M3vEzS8L_JsjtGEdz3BjQN7nABJSWg9qfb9sCVcErpYWGE_x99dlEPpYdg1OzAvkLCX63z5emIsvJvsP5cw5pKO98M4asAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCjv6Lw_XnnZ7fOXt_mqMcjbInoaOfUhTl3PoLbMYEnjvO3-EPIV7fuw-4WvyzIqhZkS3T9IisQWKilumMQh3CvB3rGFsekr_pNVzus81hvI02vFyyIRAoy5zovXVb8DImj5EufktWOKwhww_VtJzDi1Y9VAX4yEVMmKaZIBsy3DQqfNWA-0A9xffUbradMa3S5NKzp-f19ULr4DspNNlj-AQO10316TamacN6VjhlDiCjCL3EhZnsdXc4GLae9M37QTiDwRsirL3dYNj5yIakyL7IklOuhqzsJ4Bozu2-VhLSKvGPrOZZakkwBj606Sv8J9L48g0jg-Rz7LOfbE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=FTQRk3nBF9e_Drxbh3NrjkcEnpMp4lHFjUEzfo0lOZGLnPNKsWFthWAZ3Tk_H_wwz_UC8yqCxbkgGufyfPqHqwnp8yk00g5klXRiXh9KWQu0sCWiIa7G8b1O7eO3aA9srSll9Qh8sDBo9r05SAf-Dgju8ir4qiG8BKg1fcKcSn_kR85BYBkJFC6uTn3HFdt0gGp6sc-SCqvfKIKNymMjeyT7iHJaPRF1iRUsdW8kJUpveUmdbfFCSlivueJLd8ZwrspSNQVhNZnkoTwy4qa6vDYTlc28JV96Tv8tpk_pAt2awj0yLCvrXVGHLxxRBkYqzUqSP2gDfC4YbMALtwZ41A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=FTQRk3nBF9e_Drxbh3NrjkcEnpMp4lHFjUEzfo0lOZGLnPNKsWFthWAZ3Tk_H_wwz_UC8yqCxbkgGufyfPqHqwnp8yk00g5klXRiXh9KWQu0sCWiIa7G8b1O7eO3aA9srSll9Qh8sDBo9r05SAf-Dgju8ir4qiG8BKg1fcKcSn_kR85BYBkJFC6uTn3HFdt0gGp6sc-SCqvfKIKNymMjeyT7iHJaPRF1iRUsdW8kJUpveUmdbfFCSlivueJLd8ZwrspSNQVhNZnkoTwy4qa6vDYTlc28JV96Tv8tpk_pAt2awj0yLCvrXVGHLxxRBkYqzUqSP2gDfC4YbMALtwZ41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZRxjO5-duKCUOfvlFP2AlcqBN-t_wTQu6zeHLCDeXiTDhDstg1EendbSinUsPBXQglyX0Kh6Rqv_hvMpNQcBqPqRwM-MUdmZ9feOhEsJ575HpwHT5s6E3kJhzekkEO2avi6e5kejhsl8DplNPg90yVhwqJLlE29OL_IuD-0PN2kuXkGAjNq-kHmCyIW7RqJKuvhY_IUD3c307CSFsK6FXekEe_OIfeTJoVkv5ObkJnjFUL68v1V-0anspFIr8rQU_f46WEBmu-KRHnJuFnvupl55gGWnAW0PpoHa70sIYZIaPQfoQ1vITFFFeiS9HZDze59OFUB6JDwbCxfh205uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=u6XrdkX45eWI0gbv3Tlvd7HaqJSJGNbDn4AJO-N-mzBfv_le76coC8ZE4xOz6ussfeR2PIHnc7aY5xjB6bEBYbAKx9jYSSI5PBwp8u_5PqyLelvBl-Awn7Nd728NEMIKSnj9MOI5tVjquXcYtlzK7lu1sm8fAAzXGmvCwuBSfc250dXWf-J9wwAZF1ZBhE2CliH46MCuEcqpREJ7-uLsCaF3ubZ3tmnCaE7XNrjbVRxwhrkuaSomE88znFvap8_Tk7gCJaXgcW86KIYV-oNfFha3vTOI7_7qz_1DXCkDJHWhll5h8ilg_AWDRYPzpfDCAwoDsFM2DDWfIuxfizrQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=u6XrdkX45eWI0gbv3Tlvd7HaqJSJGNbDn4AJO-N-mzBfv_le76coC8ZE4xOz6ussfeR2PIHnc7aY5xjB6bEBYbAKx9jYSSI5PBwp8u_5PqyLelvBl-Awn7Nd728NEMIKSnj9MOI5tVjquXcYtlzK7lu1sm8fAAzXGmvCwuBSfc250dXWf-J9wwAZF1ZBhE2CliH46MCuEcqpREJ7-uLsCaF3ubZ3tmnCaE7XNrjbVRxwhrkuaSomE88znFvap8_Tk7gCJaXgcW86KIYV-oNfFha3vTOI7_7qz_1DXCkDJHWhll5h8ilg_AWDRYPzpfDCAwoDsFM2DDWfIuxfizrQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=adhuLLfwAqbJ6VEA-USLsdJAASF4AAUPAsJORsvUIgMSpbbGX_jDHib6Hse72WmjEgct2CzGDRL4dj_u55LNyrO4cuZBQyvafkWxikEZOw2qp1o_dDDKh_FJotFS1KKHXN6kbzL7md5RezUiEnsBjlJmrV4mq-DesGGWOB4Jp2JXPpslsaN2DER-S7Ct64ICimZe5RrWn7G4X5IgpTMjChLy9W9pb9ot6QaWI0fc8HAw5kPUNGhuS_rxjV7pe66olTcMmCWF64m_NEvkqkWRJo0CIQBEkd-nL9RQGwBmXPEN5dvvbRv-jpgC6FSXUXyXmnU7MCC6gIID_pJmIjIqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=adhuLLfwAqbJ6VEA-USLsdJAASF4AAUPAsJORsvUIgMSpbbGX_jDHib6Hse72WmjEgct2CzGDRL4dj_u55LNyrO4cuZBQyvafkWxikEZOw2qp1o_dDDKh_FJotFS1KKHXN6kbzL7md5RezUiEnsBjlJmrV4mq-DesGGWOB4Jp2JXPpslsaN2DER-S7Ct64ICimZe5RrWn7G4X5IgpTMjChLy9W9pb9ot6QaWI0fc8HAw5kPUNGhuS_rxjV7pe66olTcMmCWF64m_NEvkqkWRJo0CIQBEkd-nL9RQGwBmXPEN5dvvbRv-jpgC6FSXUXyXmnU7MCC6gIID_pJmIjIqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=u_uquPAcFOp8oJIBnJkxBCokcE4SCPPe6fiTtHdeWlxsifhadbf3ggb3K3g7u_RCyJhOESkvivJiVotBmLfFWlk7LtqsJcpNi14EdmBNzl9rqCb0JQwSmcHzBj5K8fk0SfOSv0CBISztTGuAuMaym0eJ3fzjMEo5muxouzI9GHjzsJt1ac9Z7pDYPD1SFz8mc96hkYoVpm3-zx2ELxX1YvBor6tiscBkVbkWtDAB5-umpHMQhDNTc-dE-eaKYC44VdV227aPPJMjXdF0atcFVqZNfPNq8wxPHTILBAfZD1PDmMKdJyIjHakq9IvTf7KZmHbWOeEhl575bD6YY8Xl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=u_uquPAcFOp8oJIBnJkxBCokcE4SCPPe6fiTtHdeWlxsifhadbf3ggb3K3g7u_RCyJhOESkvivJiVotBmLfFWlk7LtqsJcpNi14EdmBNzl9rqCb0JQwSmcHzBj5K8fk0SfOSv0CBISztTGuAuMaym0eJ3fzjMEo5muxouzI9GHjzsJt1ac9Z7pDYPD1SFz8mc96hkYoVpm3-zx2ELxX1YvBor6tiscBkVbkWtDAB5-umpHMQhDNTc-dE-eaKYC44VdV227aPPJMjXdF0atcFVqZNfPNq8wxPHTILBAfZD1PDmMKdJyIjHakq9IvTf7KZmHbWOeEhl575bD6YY8Xl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=qDpDr_t7OD4i5bcN9b8EeyosO7qRHcEVDNzjT4ipdEHz8R7hsQzNqbzarlV0-U9ja-NsymAgIy0-_wtNdXkttyfbrepNzs90UqYClRpiemm3ULBmfg-FDaqhrC5yGv-n3B_MHKSvDJxo3eXMrEFhWh0u5-X7rxvT648xUrMK5dns6SEfKR3qB1DdvhihwmCc3jj1LaLxf16HkfHcgKtdlwBzG-3HGBwnBzIAW3JQuE1B5X_3u0RuLpiknqP0MBDMKumtlWZEU3xz_l_6oV9tP8N79bNOMRLSazzpU7fOShNxKv8FkuV4FwdrYgKg7uVK06b1G9FvIKtKhqJTfOmhFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=qDpDr_t7OD4i5bcN9b8EeyosO7qRHcEVDNzjT4ipdEHz8R7hsQzNqbzarlV0-U9ja-NsymAgIy0-_wtNdXkttyfbrepNzs90UqYClRpiemm3ULBmfg-FDaqhrC5yGv-n3B_MHKSvDJxo3eXMrEFhWh0u5-X7rxvT648xUrMK5dns6SEfKR3qB1DdvhihwmCc3jj1LaLxf16HkfHcgKtdlwBzG-3HGBwnBzIAW3JQuE1B5X_3u0RuLpiknqP0MBDMKumtlWZEU3xz_l_6oV9tP8N79bNOMRLSazzpU7fOShNxKv8FkuV4FwdrYgKg7uVK06b1G9FvIKtKhqJTfOmhFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=s1hSPhfV1m0zcXy5RJpYCDZVWoVOTRb-zPZLUbgWTj-TtjzfARqXcdQhr4ObsFHnCbSHT3HkmXXBFvGUeJQEcWb-LnanJEaaQIbXBq_7LLzrzhTnZ30Zw_SQdzpdf-WpNjyVWL5sXy5EmICJgrtalkastmpB9IbxOw3R51neEOOqd6G2CT4cTbnECfklk2JDpvuF-9eLKMCbv0CKGlmAanMs7cpeQxZc0YVWcvAdkkdMNgSmMWVwu61IzXQ_VHgqBlMaTFfJf1MpPtK4-5S29fK6dB_QKvrXbFFmGIQ56WhCXRSUrD8rKfR8TsA9SoFCM4SgGwQFokjl1zy348XwKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=s1hSPhfV1m0zcXy5RJpYCDZVWoVOTRb-zPZLUbgWTj-TtjzfARqXcdQhr4ObsFHnCbSHT3HkmXXBFvGUeJQEcWb-LnanJEaaQIbXBq_7LLzrzhTnZ30Zw_SQdzpdf-WpNjyVWL5sXy5EmICJgrtalkastmpB9IbxOw3R51neEOOqd6G2CT4cTbnECfklk2JDpvuF-9eLKMCbv0CKGlmAanMs7cpeQxZc0YVWcvAdkkdMNgSmMWVwu61IzXQ_VHgqBlMaTFfJf1MpPtK4-5S29fK6dB_QKvrXbFFmGIQ56WhCXRSUrD8rKfR8TsA9SoFCM4SgGwQFokjl1zy348XwKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WQIETM_Nly0KxC6G2tRr5OIPjHEUPQKapEyLfj76_CMRY8VKuQyfbVgP8sq-KuY7qhE1nLHWZK7WfxAfa1ed2k2RMANrJLYMKyCZEQI7eN8bz7YnGjGTG2tOwr8x0-LjSR8q7o4iW4mTF1JNJSbLHSTOPdLvUovt4NYiZUOzX1sXqvQga6TDsMP0Vo0Ok7JYIZDrVWzeX7liXv3ioFF1XcRTDAUNmXiM6yeujde3afQciOxQDo3AN177DCoOGpLsHK_Vmh7QzHAybSBXYvMIudCMRv8iTXkFaRZ9XwodqEYViimGf2YqY3JoFSvH9UQbgyHcSrOnlFQ-Sms17X1jOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WQIETM_Nly0KxC6G2tRr5OIPjHEUPQKapEyLfj76_CMRY8VKuQyfbVgP8sq-KuY7qhE1nLHWZK7WfxAfa1ed2k2RMANrJLYMKyCZEQI7eN8bz7YnGjGTG2tOwr8x0-LjSR8q7o4iW4mTF1JNJSbLHSTOPdLvUovt4NYiZUOzX1sXqvQga6TDsMP0Vo0Ok7JYIZDrVWzeX7liXv3ioFF1XcRTDAUNmXiM6yeujde3afQciOxQDo3AN177DCoOGpLsHK_Vmh7QzHAybSBXYvMIudCMRv8iTXkFaRZ9XwodqEYViimGf2YqY3JoFSvH9UQbgyHcSrOnlFQ-Sms17X1jOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=QSWH6wGBTCPKJ0tXK_JYDej9eRTAQRlkshHn36t_DCRYEFVHQcIjCWGm_tRLhl6WR98-ZrVt8H4EsBHoDb9QWecL6XYOGlax6YfkDGXQJnr05rBTtSRioM4jAvFmHdIJON8idzhD-eW2sj3lFUHae_tWcfhjfEBiAOTFanKo6PivP7SjPNoRtGOxuDuRl6LLWeq3qzGC54Te0mpZog3R8R6-0U3S9lEbxqOGZuDYz1TmgYdXnrzvnAQ3YQ5f_Wb553yZ2PSwTQl54dIF_nT8Tsn14WwKAICxfQk6TJZW5qCxa2i-0BwRDGcDW0pNaXkUQOxqtD4WsGGlX2K8TC74oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=QSWH6wGBTCPKJ0tXK_JYDej9eRTAQRlkshHn36t_DCRYEFVHQcIjCWGm_tRLhl6WR98-ZrVt8H4EsBHoDb9QWecL6XYOGlax6YfkDGXQJnr05rBTtSRioM4jAvFmHdIJON8idzhD-eW2sj3lFUHae_tWcfhjfEBiAOTFanKo6PivP7SjPNoRtGOxuDuRl6LLWeq3qzGC54Te0mpZog3R8R6-0U3S9lEbxqOGZuDYz1TmgYdXnrzvnAQ3YQ5f_Wb553yZ2PSwTQl54dIF_nT8Tsn14WwKAICxfQk6TJZW5qCxa2i-0BwRDGcDW0pNaXkUQOxqtD4WsGGlX2K8TC74oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCWcbehpBpHxofrXYYLGHECwy1IcmbZOkEt8OQgbMokT-o1mF1mpE1ML_TJr6Qw9bnT2wDEkjOE_uG6-ae-r5dFo0ZWqCX5uXHXhthrLn-FNZ3PlNey9cksTNak2_jXvmsVW9lJXmiKCbzS9wtIgrgjrfGd0sowP7QK16sl5CF_YFRJvnr1JuehgPygnsgTUWAWg8obJPdrCNKkN6xBxIqZDFsWAHjrX2IGILJuJU8TFjb_AG_wNV9TQVWljgudN3QNKtXfyZSGiBjOvSADSLOvP6GykBTHbjxKzwOa-wSxZYCaHLcW909jFqTlhQNC1Gffi-8y2192pWkXrzJHUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVeINsJig3AkIvYuAwM73sLH16untwbwpAs4por421xCT130D9huYUTf8NSVuG9yoJMQxAZk7FAjuEzze0zoFfnGTXLyk-u6W9urK94vo1KKf5-TMAyeOjvUzS2UzwcGeeF7bc7Q3sNMaGkFre4ksYdC22Gnit2xBjBlegZwLJfggdfzyFkD6mY5gdfO4r5LdFu8ybhaX2XRg1fKzTqGxKEo5IkafDjG7c7cASf2-Q-2gqXtQeGe1LDBgDEw8N_S-C2HDwhof5bcD2U_UlWcgVAiVdBdf6R2_7FF4Gy00YM_TAewXbU-R2mbODH3Kr3dALB8Gjf2tnq5t8sc9zKPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=cs9u5OfNVSgJkX90uHqYANDOCCgqHrglKUow4XJ1tQzG0ZOt3aEPNM6JTu7hxOAMCOs0KXVohs2tnOCoo06G7Bbzqhdnzs09x2Iom9f3y9POVYwq7tM414je7nz7n2BbOKbscadhScFe_7T77FcovsVATCdDU7c7ivNkelaj4D9G5iq_pdRFdbacnZ21Uh8JuC2uvfCIcq2xBsK4lcw3NNzYCFWT9V8PYUGEFxY_zMENtWepw4obQOXRinshwnO1KG-Ye8rlqcb3bgv9mWc8jQO9iQa9pj75u23svxlfkEcPWkHpXbFL8uHgpWv99-UAxm5YmfbUdllVbPia-F1_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=cs9u5OfNVSgJkX90uHqYANDOCCgqHrglKUow4XJ1tQzG0ZOt3aEPNM6JTu7hxOAMCOs0KXVohs2tnOCoo06G7Bbzqhdnzs09x2Iom9f3y9POVYwq7tM414je7nz7n2BbOKbscadhScFe_7T77FcovsVATCdDU7c7ivNkelaj4D9G5iq_pdRFdbacnZ21Uh8JuC2uvfCIcq2xBsK4lcw3NNzYCFWT9V8PYUGEFxY_zMENtWepw4obQOXRinshwnO1KG-Ye8rlqcb3bgv9mWc8jQO9iQa9pj75u23svxlfkEcPWkHpXbFL8uHgpWv99-UAxm5YmfbUdllVbPia-F1_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4k6xhsI0PlczBgf61eB3SKdgFFfEHZFo4YBcJhGo5Rl96Y2Mp492rXQYxJfwENiVubpaAz3SCgBnVGvRZsu_QQLlLAPRUmiGfLsg74VZadl07Ha9acLvo0F7-H_SuFc2kafm8PHVYQ6ACWLaqx8tHEeWkUH4GsvfW-t2kQlwDdMihwqC8zWeLaf96lw8SYzQ1nfp9VasBSUoR7asrRyXf2VSR93s4SsIbvBaFMMbx95Vy3abhDOd4wTx6SWoA_gZrtWZVHAsM5mgiA-XkFSeCLo6Rp_-ruimkkuU086H88-3WdKIFWj9QfrsNq-DqcfRL1nhht9loOT3UW1K-IHRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz73R-bh5c9JFy0cpgnosq4VLbXSKAvUnfVb4v2U6DTpK3jvIZakt0pDcmLdkO8wJ9Kr5j3RzFEYlRY92i6qcU9PwYY_8jHdnw-jqENTG6qQThvlOsRgfqYN0g2eliV8cSL3jFriWJTY8CvpFJCshqH9LYLhSmvXATQIj_JsLLr72TIVsH1-19Tl8W6ysviPHscTO7qStyVKCPPRAg0oJWZ9wVwn78YkQU13bqG3KMGd6KXV7Lyvf2P8xrSov3CtDPpTkYQFBO5IyF4VN1wMy2z1Ze7qiZss6v6_hFwIF_8R9dyYfFuzJS2P8QCMYMsjgxsxxlT3zMGlFYBj7mf_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=fW8RWC1rZZfzD2j8HV_4yMAUEbrl-yLAUOZe0IgdkqiOX7-iM91QtWwt2dI-FacxEEB4wbmFwtxVw13vXimZ6O5qtEYqVd3GteMnLJXROeZ2bhuKp3GFNXdlGWHd9jlKj0wxIakN5ny52TBy8-We_W9SkYII6ZXxe7rgZ9QY3hy1vtIXboYtxlgZjpV4f8dyy_8wqKbP4hlYHRPPzO_yFWtofmwjZF3D1yFNG9yFc7J8s6vlqeWks3-dmysHtal-nfSKpFaEK63eB6kQjrLQktjqmwZtJMuxVY64-1ZCdPCZz9gP9bDjD4CRx9f77mMgKrhFu1C29U82GCjJcsOpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=fW8RWC1rZZfzD2j8HV_4yMAUEbrl-yLAUOZe0IgdkqiOX7-iM91QtWwt2dI-FacxEEB4wbmFwtxVw13vXimZ6O5qtEYqVd3GteMnLJXROeZ2bhuKp3GFNXdlGWHd9jlKj0wxIakN5ny52TBy8-We_W9SkYII6ZXxe7rgZ9QY3hy1vtIXboYtxlgZjpV4f8dyy_8wqKbP4hlYHRPPzO_yFWtofmwjZF3D1yFNG9yFc7J8s6vlqeWks3-dmysHtal-nfSKpFaEK63eB6kQjrLQktjqmwZtJMuxVY64-1ZCdPCZz9gP9bDjD4CRx9f77mMgKrhFu1C29U82GCjJcsOpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=VlfkWqqWk5frDl8DodwPfvnqvr8c0qmtYqNdkkvzZs3WIxQbF0YXdkPCGG5dhhTFAxKgmC7zYiiG00Fv0-6_ZLItoQZXalS9VAvuWjYOp1JaKDmSn0gI-WDflyiHb0yf1qx-YrFGEN6zrWv09qgPtUhSPnXFVMj0fUKOjVmTv9U4ZlqDQXht2P9DOsapoNRZjyi3rsMlING8k-3rGgO7oKbo4XkPhG7o2ljDtodWuc5PaBhlt8ERSvE8Po-LiBsxSi-RGanj1kkKdSZskpt46is10BLFkrgHZ1DHdcHP-wsP_iNfdgZKbFQ6JEZIDJpgu7ma18C3OUuAjtwlCsy3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=VlfkWqqWk5frDl8DodwPfvnqvr8c0qmtYqNdkkvzZs3WIxQbF0YXdkPCGG5dhhTFAxKgmC7zYiiG00Fv0-6_ZLItoQZXalS9VAvuWjYOp1JaKDmSn0gI-WDflyiHb0yf1qx-YrFGEN6zrWv09qgPtUhSPnXFVMj0fUKOjVmTv9U4ZlqDQXht2P9DOsapoNRZjyi3rsMlING8k-3rGgO7oKbo4XkPhG7o2ljDtodWuc5PaBhlt8ERSvE8Po-LiBsxSi-RGanj1kkKdSZskpt46is10BLFkrgHZ1DHdcHP-wsP_iNfdgZKbFQ6JEZIDJpgu7ma18C3OUuAjtwlCsy3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=UprjSpgPC4PAibB_p5GS6PTPtQ4mXm5yQNWi1nCCKdNQCqZ-EnGIonQRLTJdfCuZi453kGIl4XIcKxzuRA024Z1sLXwpxBm9xkekOsB5Kk4YjTwuwprA62YUbO2vJ-nGSKZoWDg7LKrYVvZR9nURN3Ygq7oJtgKi-RSRXoY1pmcCL__nnXDhePXvU_Zy1Kbo3hVDROfudSfbBWWpr5wl5UAd_PxoucBmVsbCkiVwfkwuFR8usLzvr4DpAWWOwNxBs5gePKm1A7YK4eOxaYYNY-4mmIhhl5wmdaF_aU78jKCYqla57W0C9_U0AkHLhNjRJlJgV7RnSZS2ZLCJp0Hyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=UprjSpgPC4PAibB_p5GS6PTPtQ4mXm5yQNWi1nCCKdNQCqZ-EnGIonQRLTJdfCuZi453kGIl4XIcKxzuRA024Z1sLXwpxBm9xkekOsB5Kk4YjTwuwprA62YUbO2vJ-nGSKZoWDg7LKrYVvZR9nURN3Ygq7oJtgKi-RSRXoY1pmcCL__nnXDhePXvU_Zy1Kbo3hVDROfudSfbBWWpr5wl5UAd_PxoucBmVsbCkiVwfkwuFR8usLzvr4DpAWWOwNxBs5gePKm1A7YK4eOxaYYNY-4mmIhhl5wmdaF_aU78jKCYqla57W0C9_U0AkHLhNjRJlJgV7RnSZS2ZLCJp0Hyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcFvurJWbAeuR4noul73oRu69y64byvT4kiNd8r3nvPPmAVN0iWYZBX3UO7HYFBNgsl2LdowgMZMfzTMEDnihZPgmkqugSAuTVXzoO3uAMOYfLQyVKLF2hE-eJkfJfgMYuTPPkbipoiC-MqdZdjE-9AwqiYKI84oIogSy7k6c8yFbtQVgGFdZt8PEJmJ3CAw9qq4hXptDNxPbPX6Gjpu2xRzp7QRpK3Hg0FMTGUVfkhCWEmv2dTQEZAuS8ZirGTqImww5xm_N4FefKVi8BA2WKvMkT-mz5pKDTF9aMq5rvNwrX-RsnsPStEFWKexdgvHcLfdngv5K1AibKT2rZ6HWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltb8QkdJ75g3eZJtY73adHsK0AqlR7Z5_Vux6Q9ZoKE3b-M5-1q4PPRroRRscpJBDlEFOZH7a8in8ANTGsjKoqGvJtdKsu08Gzi7xGOvb-w1nnba7INVAwhfhTnTaqbr-di-nb_kUMmLJhilF_c5thUuFg5GxPJ0l_6ycC0Pwko7fzihrwtk8uAWzf4re9bQm-v7h73CZma1gK9qMXPZiWyOF6GoGIVSe9YccZ92l_v7oK2Hscb9prF6_Yws0StHuCNCsGZiqYt-Qm-DjLXQKnEgiPEDbiiERUkhzznhRNlz6g6h72XXHGNi6pl5hx1gkgDlhYbM_dFmxk8bvRBdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=IOJ5yIPc4ydAdzdBCt3Tefcy9EPi751i6_NSY0mihB3D3Pj_SThTSh4XoPZvnsFDqK7fODHclpLAHbv0jAzhqnln2UGNc_RvL6UH1Dese06hzMr_yJdfuCG7o2MtmvtdnsN242HmymlgwLyoLwtxpFQFbkh7PAViemfIODRCLNPMkIaDog9zzvHd9Y7Qj2WKYJzFGcLT9DOMFECVrnuV7OXqLsNWldyMxAfK6cZ5dc_rOuNOLsM-N_5ghdWxNqYK2ua576TFeYLccgpZgTzwI46pO1Qw7dYgvQZE0gIN4NxihfWeqFca-gIwZenRWNXthYr4T_Nhg44OfxJP8j_-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=IOJ5yIPc4ydAdzdBCt3Tefcy9EPi751i6_NSY0mihB3D3Pj_SThTSh4XoPZvnsFDqK7fODHclpLAHbv0jAzhqnln2UGNc_RvL6UH1Dese06hzMr_yJdfuCG7o2MtmvtdnsN242HmymlgwLyoLwtxpFQFbkh7PAViemfIODRCLNPMkIaDog9zzvHd9Y7Qj2WKYJzFGcLT9DOMFECVrnuV7OXqLsNWldyMxAfK6cZ5dc_rOuNOLsM-N_5ghdWxNqYK2ua576TFeYLccgpZgTzwI46pO1Qw7dYgvQZE0gIN4NxihfWeqFca-gIwZenRWNXthYr4T_Nhg44OfxJP8j_-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=v0EeqAbC_hQ-kIJ6Dj_qVlpYlNp1_eoJQdfeqEw67MWiOCAoarD3Mi7AQJ-ODY8c-4QCKLkyL8aQIq1W229nPxFvkwEdG7JXVqbhar6j1cHIS7-JIKPur_DRSDSSEmj9RInxhSRluEoCO4oUm72u50PhRxr7bPirmwuHsjtfSvp40p-r2FpyLwrqU9OJgrW7M9cVs_xdeqwTtLPBHu5nomK4hCTCCFORUtoVgzuvUNJEDsVZnQnrzaueMaKcapnZ6-KL2EteVawFyVNOUQkM312pQKOOX9ipeqAwnGhpbIRelYEK5vOVmVRXJ8N2THT6gPDhclABmhTOHsQXIQoZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=v0EeqAbC_hQ-kIJ6Dj_qVlpYlNp1_eoJQdfeqEw67MWiOCAoarD3Mi7AQJ-ODY8c-4QCKLkyL8aQIq1W229nPxFvkwEdG7JXVqbhar6j1cHIS7-JIKPur_DRSDSSEmj9RInxhSRluEoCO4oUm72u50PhRxr7bPirmwuHsjtfSvp40p-r2FpyLwrqU9OJgrW7M9cVs_xdeqwTtLPBHu5nomK4hCTCCFORUtoVgzuvUNJEDsVZnQnrzaueMaKcapnZ6-KL2EteVawFyVNOUQkM312pQKOOX9ipeqAwnGhpbIRelYEK5vOVmVRXJ8N2THT6gPDhclABmhTOHsQXIQoZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZFko3HIoW-sCzabbr01NLnfCKYWkwuheK5w9iIiHWRncKcO1h3K7ygaKnSRzljpGoVNP85Zn9hc-xpORlzhq1EUPuBnRLDVgECneWwj2k7CQvPb6hEOR_jq4gIeDiTnLmPb6V3VjqZXdPtFk7YSyVwV5nYqsHSomrYu3PG_vPfLpov2NRkypNZtUVZetS-5CawbfaVrwXQP9kv7MDzdmH6EW96iNwIdfzGU3UVG6j8fimHHw9j-4mpShzDiEKUFjOk_jfa9yc8JAdEipnhK2ub_ceqHXAUPK1a0yA-WYvQbxU8ix7eqmz3WRB5Bd1a1w1Spz7Bcc4jK8bON7wF8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-2CWVfIaSz-CcM0cg4LiOd3Sr6b6sLgTwHnG61SWh1akkK1r6gTSAjJ3kk8C71lC3GiQLg4M6K2l7ZbO7gbG4aBjW4Wdx4h7zAdrR4-DLPa42ihAkqKDG6NPN18XuKkC4LeX9Lz6l9gBGq96I1XhEZwFfuJj47i5VMG18IRXwlCbpCLrzpa7OohZqEyJQc6xZ9DSr1msInpWaT-8FNmI5bztXEiV6ZxhpRyXuw6HCCB0EcYmeBqBFYowF4P9LnPjNry4eYbWUFrAddnQHBvkX5NnnXEeINZHo_zR0hKVoKtPRUHprAzUAiyBNCmI7eio2Sl0E13SYsQu9JHYRAU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as1wSKhDri8Q8iJILtdLe_J2LGvtr87KQOFgpGIosnD9QU8JqPRpuat9QqgsXgTp2GjezOTkYWHpxUNGzRS_9iczEEjl3O9JYmW6-l5tmU-0yHQS4XPCdHxcyb1btehrfZdIEob8dHzwnXkOyAGKreULcmHArETW6ccdv7h0IL9Wuyb3GbsbHBFBSFyzpfCccT2mMeAko87hSABlR4bCoelmuUsqG2vfEcaEkzHC3fZNIqOuYrLsL5X6Nx2sM9dR-HRlE56gYVvZuXA0wX83onb4jdB9gcjHJ_VP8F4oKcAaepBnm9O1skSEGk9_62O0npN5ZKBGdzmUclAtaIuZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXE-G9qtWddyjYDl-7qyTYB5MXA_fSq-kV9Riel7XXd9EgF_TLAIuPfDCcKQJGEuuoqf8qtKYuTY0xgZO_rXhERr40XSlH4F_UbyfgOb5aT1v_J8PJONwy-rofbT6jyNsFiIrnrym791ElJxGUC-A6XphjumLDuykIQH2GVst5fO-wsILD8sMbNwIrjzTxTdSzn0WAKOCIDe44CggSCcPCvCx_rqSF_53q2st506YuFUHAPYRZs5zC3vcyQilOYyeSQ4e8pLLsTEjqFtqwTD4rxHDTdE_iEsCEsM9ZVEvSsYL2zYZ7Yud42TeElbcqhtL-PHaHpUuM_JEFaeQ4h5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzEsbxffj9Yv9lgHBDQvHSiKVnRgQ9Aru0cEFvx4_5g2mQTGM4VjPb6Wq_wFpiZn1Gu1aozA-OLrNUm6m3vroYYi3MwHQ2MfDjrh6GUcYBSqUJcloYouHyiUCzuzGhUkYLJeo7GJBLDkrBW64x5xphyIIpzk1EltrBrVQ1OhfczrD_eCkWiR4H0sKouZY4WU5VtV02Bx1zwB4lp7w1Qn7xspTpzYpeBEwnUfLVkONAdw5VzAKIjbDh6IeBOQEJUDAbOtlmPYio_vY0BAT57IElMBEDEBXtQhr58Jbd6m8y9tLHY2hkf2YhRXi_0QbJJ3Zzlv5imFZemILHuX_iCHnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF5axG3waCAICD6ItCiXl9NOD_WLqVgZNy4JzLVWENRnbG-3dM93X1WalnmrkxGrWMKfpjtkH88ntCvE1OCEin5igO_VuimNizDFuCccyFj1TsngtOUS-d377gDaKXQuHhp8tyFyA49VcOxyJWKUf7E8fcoHZiVtXJOu_BtxGMD83n8_gZ_ihvilj8ZoIAWzZttyyJv0L1u3LwnQZAEtTTO-rJgiyu_b1YOSz7J2Wx-5JlrpUN735zgMHHpjVBo0EtXJlXZPvlBomtdZm_lXPKZb-UOqWbu8JNaq-b6zLjBtmPfIP_gPFxV_6rLO4BHkwZIT5DJoUrnnHl_lcFzkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=GIPX7iNBfR3Y2hEg-NWKYBorw8l1OUCToyUrHxnSC_MQzX_InlRuNh2HLEkQuLoNiagYfkT0U198v9MfB04rErUchLR53HyO0cVRVS3CJe2WmD7CclswM_WVui2yZzVQveLoEyS3FCOWNJw5zFebKO7lq_QM6hWTxLWPSLL0l5faVW2nt9YUrl8U-Csrowvznez2dIrVERQlGqZrvAoUpFekCKjsgPIEauNpW4abSMPgyeQAvRSs6BJXQB5T6jTWU_kFQg_gHVQg_uyBmOGmQrZShhr1SARE7QLWFmwtcb3HzLz5WAVmVuBnCs0GDGbxCizTceGOYvy5gS7CiE6r2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=GIPX7iNBfR3Y2hEg-NWKYBorw8l1OUCToyUrHxnSC_MQzX_InlRuNh2HLEkQuLoNiagYfkT0U198v9MfB04rErUchLR53HyO0cVRVS3CJe2WmD7CclswM_WVui2yZzVQveLoEyS3FCOWNJw5zFebKO7lq_QM6hWTxLWPSLL0l5faVW2nt9YUrl8U-Csrowvznez2dIrVERQlGqZrvAoUpFekCKjsgPIEauNpW4abSMPgyeQAvRSs6BJXQB5T6jTWU_kFQg_gHVQg_uyBmOGmQrZShhr1SARE7QLWFmwtcb3HzLz5WAVmVuBnCs0GDGbxCizTceGOYvy5gS7CiE6r2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=uqczO3PPU59IMfbQKQ-jbY_RmcE04RbocGQ9YCuYmjv9gAARBm0nzhh7RsBTv1Rtv9qxF6B_AMimxq7CIno7H_Tl7ytsC7zBBLKkyBXF3ZCpdDP9o9VC74qKjyCtshVjbEU9Af97Juqw_y3nCwDEiJKbZd_TRCYbLRvV-2ILY0hYStftH31N59wPEvDOa_QC2yIIOCaKMazBHpXZH15gZ47IWiMaGryKGZ5J8jU4_I6UFcpZwaSCUuXLFCwm3OX6Rc8dftbR3SVdCvl6CiMLBUO9Lo1yG0-Ssn6NrrqvDrJXIUOXqtWKMreLyYCLbOYgy7rFtj3lcWJUKia0NBtzlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=uqczO3PPU59IMfbQKQ-jbY_RmcE04RbocGQ9YCuYmjv9gAARBm0nzhh7RsBTv1Rtv9qxF6B_AMimxq7CIno7H_Tl7ytsC7zBBLKkyBXF3ZCpdDP9o9VC74qKjyCtshVjbEU9Af97Juqw_y3nCwDEiJKbZd_TRCYbLRvV-2ILY0hYStftH31N59wPEvDOa_QC2yIIOCaKMazBHpXZH15gZ47IWiMaGryKGZ5J8jU4_I6UFcpZwaSCUuXLFCwm3OX6Rc8dftbR3SVdCvl6CiMLBUO9Lo1yG0-Ssn6NrrqvDrJXIUOXqtWKMreLyYCLbOYgy7rFtj3lcWJUKia0NBtzlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=nkXxNcBydMLO2epJw3ITZTPcEuw7QCrKiB0WXI4NgFCH_6TGkDhepW3F_YfIOdvc5ISXnuaHIQ9F_SuDNAx9lhpgWv0od1HWItXqO2fDlSflWcONziKh1H3YF3EZayIozLsJKbnuMRAwHawX2Lg-rFvl-TqimNRY_u7nJT8qYGSiUGVQfxEYhcrDPXNXcrE0UBBHkJUY7ATfT3C2OvGk_60ixA-O6n3aQOebAu1ZOGz59qJ7nqDZkGzWErPPC1wyTHEmbydzOKUfxyd5esva7PEjAxThymX7dXUtQxypM57jdr_WtkWROUXmlSi38qYAmBF5oVk1Tjz2xWhb4yrTWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=nkXxNcBydMLO2epJw3ITZTPcEuw7QCrKiB0WXI4NgFCH_6TGkDhepW3F_YfIOdvc5ISXnuaHIQ9F_SuDNAx9lhpgWv0od1HWItXqO2fDlSflWcONziKh1H3YF3EZayIozLsJKbnuMRAwHawX2Lg-rFvl-TqimNRY_u7nJT8qYGSiUGVQfxEYhcrDPXNXcrE0UBBHkJUY7ATfT3C2OvGk_60ixA-O6n3aQOebAu1ZOGz59qJ7nqDZkGzWErPPC1wyTHEmbydzOKUfxyd5esva7PEjAxThymX7dXUtQxypM57jdr_WtkWROUXmlSi38qYAmBF5oVk1Tjz2xWhb4yrTWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=sTzchrXGzOkaWF-T-pooRvR0eQQMQpKW2Jq9GmsDf7_S6U0Xjxg5OP5ltCX-39JuqX4a_G8MO1qaMgLDd5casCbT6wnK--5IWzG5I3xpIhEvAObxSMIDmKHJsceEptoggPWP820pZL8XXZ_Fjzck7YkJJWMW4E9rPj7S95PkNQ4pFWq0GIqtzEeT03Fb1y9mv78HuEaw6MelHqpRn2bEY6R0n2rhOblc2a7Byg0EhSm0-bz0gzBZnRb7zg_zpu0VU7YYi44PC4rangu-xFdgTWN3xj6p4-LDsbY2SVMPtkg-b7T4_47QgT4jPAgeEufh9YJdRPARowKTwZCu9ImJ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=sTzchrXGzOkaWF-T-pooRvR0eQQMQpKW2Jq9GmsDf7_S6U0Xjxg5OP5ltCX-39JuqX4a_G8MO1qaMgLDd5casCbT6wnK--5IWzG5I3xpIhEvAObxSMIDmKHJsceEptoggPWP820pZL8XXZ_Fjzck7YkJJWMW4E9rPj7S95PkNQ4pFWq0GIqtzEeT03Fb1y9mv78HuEaw6MelHqpRn2bEY6R0n2rhOblc2a7Byg0EhSm0-bz0gzBZnRb7zg_zpu0VU7YYi44PC4rangu-xFdgTWN3xj6p4-LDsbY2SVMPtkg-b7T4_47QgT4jPAgeEufh9YJdRPARowKTwZCu9ImJ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=f5-XJN3V-7sXqgHjXfam0N35dkYRzG9J9qnVgUaS5KnMZtaOnIlfO2CcYZwDOkvGnGxGsl57xOj1SUr-7r2DUdKtgu2H4Nj5nu_iSi3PJjO4kFwBFOr8ZeqQhCvMOsyJpAdAIbnC4cX2MSXQxskdylDeCkeTepWvfheIhDnHtAIzkdtiZC3Gw3vh_hIF2NC8fOJuVkNyrmtDAOq-YDOrkXER6pOFe8enab_oBkmuEhRQ_6-kvBBFPmY1buFSIRKM3_HiGplzlm84b5Kmp25iX-KSAD1DYQHAMwfasqyFNeAtBNExXomCpwyKo1MoksLUTV4tPWBIeYrDmjsbBdfKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=f5-XJN3V-7sXqgHjXfam0N35dkYRzG9J9qnVgUaS5KnMZtaOnIlfO2CcYZwDOkvGnGxGsl57xOj1SUr-7r2DUdKtgu2H4Nj5nu_iSi3PJjO4kFwBFOr8ZeqQhCvMOsyJpAdAIbnC4cX2MSXQxskdylDeCkeTepWvfheIhDnHtAIzkdtiZC3Gw3vh_hIF2NC8fOJuVkNyrmtDAOq-YDOrkXER6pOFe8enab_oBkmuEhRQ_6-kvBBFPmY1buFSIRKM3_HiGplzlm84b5Kmp25iX-KSAD1DYQHAMwfasqyFNeAtBNExXomCpwyKo1MoksLUTV4tPWBIeYrDmjsbBdfKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=rQ20PPAA1IF9b7CYt57q06a6aRdHdL5YArUNSm60Ja6ljWl7lHMEbNIe4WOPmwHl4jP6jyLW9A8P7Kd1jikQk_3Iq9X0kXCmChjQibvvEt3z8jd1lO8pEwnu9jdvFmEgkythOOqxz9z4rpoJgmb97gX6Q3DsPYJ1mHbe4IH1iDu8JoccEXmVwDKGdA9hzF_Aokul9b1M6NWOg0bMh1a9z0gPkRRn9DN-niT_wf9fqKftEzxzJh89WSauD-h2uYKMY2eM5pHdcyu4YpucpV7ZEvR3l7C6eDgbbINGp07afgdr5YM0MABhasP89g_sfrT1w_HvfCKurm2jq1fzW7qeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=rQ20PPAA1IF9b7CYt57q06a6aRdHdL5YArUNSm60Ja6ljWl7lHMEbNIe4WOPmwHl4jP6jyLW9A8P7Kd1jikQk_3Iq9X0kXCmChjQibvvEt3z8jd1lO8pEwnu9jdvFmEgkythOOqxz9z4rpoJgmb97gX6Q3DsPYJ1mHbe4IH1iDu8JoccEXmVwDKGdA9hzF_Aokul9b1M6NWOg0bMh1a9z0gPkRRn9DN-niT_wf9fqKftEzxzJh89WSauD-h2uYKMY2eM5pHdcyu4YpucpV7ZEvR3l7C6eDgbbINGp07afgdr5YM0MABhasP89g_sfrT1w_HvfCKurm2jq1fzW7qeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZXBV25xgvuCkiyLdYtjbmd9KEBXVoLAXFl52a8O_IAGIe8Zt8jNbzeonXhGG4gKxoKc7bb2c4x57GUUToMHtkYH8es2vcZWZV2gAdvr_0JJuDSqOkJJvSgt9zOyPi4kWO0DieVJytepryG4YJSB41maGhxUITtuSdt8DlJwQHpgpZhXQLJJekm935olnAvQoi2acXBACkS7FuOX4KpN84a9gPaVTBgtJblEiiwUzo2soApONWzkt3GV4qcl0XxZ2QyaFF2deyfdbcmKNgqbo94HEV0wy363grmBsOENvIBFwEvu22crG3RT0vc4b7kFX35-36-tvvFfebtxynZH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=UfH98VI6AQCW2Tgngg8giDqOMBu881JSKIzOi8W2HgeJvRoopAsrR1cER_SUVw1-OL9YNHqEpFdcE9h3W83NZ2n8lcodNQVzUWsnH4evJl-SOHBWneF6aoyXXXekXsJ9nIdgwesRfq-yXh88R83CO27v5L9M5ottDLU48SwS60NX6mDAbicy2T1L55BtEW9HcF94bveddNVY1lUmc11v2tbHf_V3DFkbLRcl_ZDtQblZCnZoGCfzrKijw89iOV0AlW5JGXUodJTK9zhVKRcWfM6qpKB8r_tM_zy3z9Qfoh24q85j4FqNthKywELKl7rQ7PlMlBFG-t6H9DuuinZ81w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=UfH98VI6AQCW2Tgngg8giDqOMBu881JSKIzOi8W2HgeJvRoopAsrR1cER_SUVw1-OL9YNHqEpFdcE9h3W83NZ2n8lcodNQVzUWsnH4evJl-SOHBWneF6aoyXXXekXsJ9nIdgwesRfq-yXh88R83CO27v5L9M5ottDLU48SwS60NX6mDAbicy2T1L55BtEW9HcF94bveddNVY1lUmc11v2tbHf_V3DFkbLRcl_ZDtQblZCnZoGCfzrKijw89iOV0AlW5JGXUodJTK9zhVKRcWfM6qpKB8r_tM_zy3z9Qfoh24q85j4FqNthKywELKl7rQ7PlMlBFG-t6H9DuuinZ81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=PGDMNzPW1WMtnDK4UHgWz2rn7K8aVlEpueaszAbyaGpiDuOGbITDVIL9dsf-tsD3Qc7-9nFZb0qrDPZi7AhthvT3FP2eEYcvYPsIt3erZQqLnWDv7qJEB9y2W-rWixhbutw5bxF0gYPnSMAC7AGGg7Geguc2Mjy8v6tooeS9-tL7brB00soj5iHs7l1-vZmT0KW5DqyNFhO5s5XHDysW5mEcCVFtUMF7V5Q-jQcZsZMHTKBAYNKTHeHU6d8raMWVv4i9CeU3exHzjWjkHjnGQIWJjpnaPNyTLLsSeN_w6U-d_5QM9xg7ZtmHwrLsEsnxDvQxfOL22B0zrocXLhCsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=PGDMNzPW1WMtnDK4UHgWz2rn7K8aVlEpueaszAbyaGpiDuOGbITDVIL9dsf-tsD3Qc7-9nFZb0qrDPZi7AhthvT3FP2eEYcvYPsIt3erZQqLnWDv7qJEB9y2W-rWixhbutw5bxF0gYPnSMAC7AGGg7Geguc2Mjy8v6tooeS9-tL7brB00soj5iHs7l1-vZmT0KW5DqyNFhO5s5XHDysW5mEcCVFtUMF7V5Q-jQcZsZMHTKBAYNKTHeHU6d8raMWVv4i9CeU3exHzjWjkHjnGQIWJjpnaPNyTLLsSeN_w6U-d_5QM9xg7ZtmHwrLsEsnxDvQxfOL22B0zrocXLhCsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzGTvQS1DdwL8jakdrp0itjIxVMjlwwKbpQFGJIDz1aNQ16cv-qOHLuoMu3rw0faAigKAJsOyOodFH_cUg9mBsMB618qz9oT3SncoyM1jK3f6OFx4RsKdwS_-cv6R2ESnO7BeNWpgnA5Ku3AjONc5309V6l-5hbQZoD22SmAygB4Ao_4Jwn8ZZx646COQ3tUqQdG8DyHZb8bwVltQENlIDBKdBWuZz9qLh1SB6deRFWInhjntgyI9ppYGIRI8ZR280Ek--LTLLAhLJezcUfdVnn9hsQJdcXAJgN4XkLUZsIoNY5XqkGk0458GHm6liOiYOVASAVINv8g3RvWwGbL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxXL7NSYfFKpKPl_HCFmyN-a80LGX6DDjwe1VoZXy6FGff4r9f1zEwFWArWOYrZFtXWH9fRZj42HWyz1sgrf8uBXWM9AiwDp2fCnUeZVFbRBkcp3KzzyqpQFjPv5c4moZO8eymH4SFQbJI4M8tR82tm2qG6Rv5q9JBUO1W8QZ5H9Ckb58U7T7Gj7nm3pkupyBgsF1x6jt-_KJrB1yJc8znD6HrvUFylRtrcnNNAVi7FNl4MhSW4Q_fVMYo5KS15ft7FyYeN8lD9jZ5de3fCTKQclGD9kqrVIyx4hEQ4H96l6a--cJzBtebpkrSLkDWSn8vQlY0LXROpSc-Tp61Uk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTAhR6iRO3KFcT8soXmveCxBByZk22py0o7BoY-5OU7PfVpEblh3xsSBMz_nrKRHPSs1LH_R-FJ0MQPauMPrC5dkORAgMbi5R8Denrfi_tyTYP5pl3PSUkxNpsmN5ByWfnuSVQRBtSL3ONLg31l_EUGtzZumJdCRtr-qqPEtfJsVeB8em2tVN2o3hpAufK9N6a7AUdNaR9zz2UNXOVu35l290GAbbNHyP5NFP3owefr1Xc52jquQVgG5Uk6DrkmfOZY59uBQiBVrMXiwMrCM7DFi72GitVLJeN5Hs5XbxjEkry9STyxId48QjmHV1NUbirFw7jQyruNCKVoHPN8o8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzCnQXEM7IJvuOB3s2Xqj25DcKE8yx9wq57RQX-OwPnclLA6ipo68lTO_PJTxqBxxSnGctAkl4vqOv7DtYtlB5UtjGBQJmRfI2TzLXvzw9YSBrXcmd9CqKlna7_FPLEdVQ5Hb_uTX2HnoTkz5WHPlkH6NyojMzHI0GZ8Oiggijst2crBSANcdJUVcMEeGtPIjxfzJCR2P8EZipYIssDrg15cIyeIGWMdjDOTzoOMkzfwzwmKgMj1bsKFyUNeznCtEmUNrNjD96hH33kJwLtt5HRpisimq-VQxwOcoXJT8QJ384TL6feojIgOU2WUjYKv5YV7t9aLsKxtIyt5v43zQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAY9rwGvr5ZIuhK56eKE-Nh-iqL4YSYiUG_MRYE0V9yks0i4E8UbQ70R48HJpL2xv0_gP7v_2_kG81pb0c0hQgHX7CzXXEOCtWnmfxQFJ-3NjhiNnhzhYPDE_XkEC8reKMngxoE46vm9n5quj1rUGCWCb4tVnvJoVUwRQ90elQFGt9twbwdCz6TMEy39thYhFI6a0mmsKFUx8Tr7BlyGDkY-WHTOgOLzns_loz7jUZTA4gnwVjzLcQETGryHvYfCEoLrdkD-V3SQz8aDQUMm8EkJ73O0NLOpGv56nFGH5h16e1FevBoUXZUTl1ZzxhqhrIfuwGOxaznpuU4M6nKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjBl2cSLmNjBnANG4zqxOcEeRH0ie7LFWWMKiaOROlO7MrNFoHPo5XRL0BM65WdWCga61oEGrG_SVR3qQoGoEyX4aXkRJV5unYjqDiUYaUlUlcOQGBQjxm3Tj-7XxEEfKF21ugQhoZaQpa7OxHRy7-HPIPvRd9LUT2jJ4nk7Um9h4KvPkUAOd17qKR6Q9pgkeYVhrYdBv9NaLtGjMIbqWMPCwrnvKsv0mhccTKbWpR4vju0QMoELydheUnvg-e9WmDwEoB7OFd9mAlz0pekHIjHIRsPRTLcAeInAhVVKqDbX-HTXUkCSxxTrbDiBvfU6vsE9jnegRRNCIUDuvsyEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPPdTnmFuyzKDgpeU0QPuaZNtUr2hrRfPrVsKpj1EA1cTz3oLmiHZ5qqp8MYJ6iADf_TfO4Zpo_5gyzQDy33hUU4S8VjzAvhpv7ZkJeYVFph_VWLIaz3q1uDGAGeQaWe0m-NoB6wbHEKgH0kOdI3m2s63bIhMt4_Z3VHDWf_CSE5ieaITqrAQvzNVKZE-9m92dgsmTrXQxo74mzNw8RIo9y1EcvaF7ww1BdJZut8JC_pvHe_046lWCeY70cppwHmAvgZfYmNuw2oSIN4yRlia8k-mmlOPn_DVqP7ILw9QTRoxu95s-mOSkhrw_G0E_bewb30pLrqwEK4zkx_CfyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqYePAM3uYzu3-sooy0abYdXmTmSPK0w_B6tgxy2jodXcwunvmhx8VgwBohMR5DIRMl5j5BMFcuJFQmzXSZBuXllbpikou-hzGKaSa8EO0JALvmdWdtePKM_FOfuAhP12ZRArZUG0EU9iaxhb7gYOE5w_CDylwjOnn7qJ73DWuPTXVRKlOY89BNERoWx-QTo2nKLwLjQpOYbZzwmUsmA52toqLyxI-5NmsNG2sd1hp4NoEriMhduAOHRHKGCkezsuR-0u7ZVWckilq7SwqTBnq4QKV8KxwGkG-NgnVw17vuyp7vI9dheudAE6kZFtmsPNz4KwYQyP40frRzt7l3Kog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1PHsnCKntHgLq8gJ87JugNn5WFhjRuczfTKOTDNEsIJ76WpqiuVQE4dIaq1MOM4-ErMKi-jtXq5EpHt3UhK-JbV_briBf8-cKGES1Lx6ME9Bxhcad8KXjVHpSd-hRg-OjN4BM-eIrDrTf6XrGEMLnd-fQ854shN5A1u0-fMU78Pbj5IVaKu-5kXQs7Je2T2SHFWCt8VjEjPUJC9shJ3aRniXVEQ4IgjGqiDqWoQ8beSJ6JtL1KDoPpv4mChpu3fZW9qCKWsRn0eZZyRGIhzCV9kb38uYavlrF7bV-7kZj_noxa7goyiaGwrzZZ4I-LG9cmf0VK-MgyQbuU1it_v3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP9vLJJgdT0s7JNd9tFPndc_7rPB9OdXc1PGuYDyQs5LQKkOe8bS6c_h8wLFsSstF5dKYABylV3hI5JPuINPsuJWEeYwzzMqx4iWpcs262xIqoHv5uV28642xDjyzZwTxrtTpZl3Eu_zjuoVWzOkhOfZsmOVLlAMNqEwb2GQSeQ1PIFeADgtppKlllFEnfRjgNGcgF0po0rOreC07WJXkoNDXJune2cJoNKp6HzioaoCN5iytevfae9-KEriMZa7hsl64FTGhDxk8sEke28izr2vjA6ieUxiSb5hZvVv-p05yLUnosdDlpDRAx6fyvp14sOBuFNNuAxWJkIQxlzpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds1oluq8M_fhXLCpVLLHU9-wve2eYzTWcpEnXAFeEBl6uyxNbmOg-QcQc57dhaYr6fuu5tEmVvdYrE_uy4U6fQ9CmIOHDvh27OQ63IukCrkcbczkgS7NGKZhWLUTlCHi8QZHzsjX_FUf2LV9N9bdxRTD8ZiOtnkHf51jBO3dwoe4cxY9NBJHfs7ddgD1HrN_I0HmJ8jaCKcR_GY4lE8KjhbZA0xO11yuNf5oXeINc1zTo7wsrwYnqfMc1n70vCSd73C5vUjxWhZe9IOdllfF5xfvvXpxSIQT4-b08iMO5J-krzC-1NUhEbgEBc0MDIcSqnXVytf5kiCJeFRC5MeDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmz9PQEhRt2gkC3LO1bZGwm9pOezMBLca133mFwMEnrTWBNgE3LaJfKCr5ezfmKauIp63AIw8kYJ4CJvQKb4AorqlJrhmjvxHwIbSlKhl2dM3wtYXobTCAtJh35eB0R7Ta444Ji3p2dvp7fUzXnTIdn-E28hF7ikhiF1ZgnvNs7_NiTqf9bpTIbjRys--4t7tnMYCQJqbNkf3fNnmXI3ZpQFDNRyFni6YHUGIS7JFQThaWCuBSHX2ygIvqse4FziN4N1Q1XnIQbhhWqZHF_7OVoNxxzNkKGw_bwgBjV3nxYg53hjtOJPks6XKy3VbA3RbCUkmBQt_NOPsKdj2VvSBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=K7c8poi7ukB9lcXDk_jnnA91GfTH-TYT3ImtOWIsReuZJQxrOrPPu17Bl9Zg_pUfTPj6xRwqJnWptbe5ev6RSQJTb9P0LAToM5xBiMHIxYtj9tbBQDJGoVJwKbfJT3k4bJd7nFMlhvai77PYOLNKGrPNseddEWSYEPMBVSNxpirRKUbHwCEZbw7wGv2dzGL0M9HwfPrt9tsJof5jiDfVoyrsrh9XorOC47xWj-T2R8pLmOQN3I0sbyGtFsOPRHunaR8fTy1xYzSknxjCKVMr_tFXLow6wIyuoQFVjgfdOkdQz56t5_S7Z_fe1vzxpHS9laIk7CFVtpEa0CHrHvryFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=K7c8poi7ukB9lcXDk_jnnA91GfTH-TYT3ImtOWIsReuZJQxrOrPPu17Bl9Zg_pUfTPj6xRwqJnWptbe5ev6RSQJTb9P0LAToM5xBiMHIxYtj9tbBQDJGoVJwKbfJT3k4bJd7nFMlhvai77PYOLNKGrPNseddEWSYEPMBVSNxpirRKUbHwCEZbw7wGv2dzGL0M9HwfPrt9tsJof5jiDfVoyrsrh9XorOC47xWj-T2R8pLmOQN3I0sbyGtFsOPRHunaR8fTy1xYzSknxjCKVMr_tFXLow6wIyuoQFVjgfdOkdQz56t5_S7Z_fe1vzxpHS9laIk7CFVtpEa0CHrHvryFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=asD9sMnv8zGyzYpEfyrAkQokVMLbmhQqdMkFtg4ZTCeL9jVT8ExWW8cBqhd-z2Ka4gEtAmjSsJo3qROjpyQWFLz9mHj2Mmt_JR6Y-efir1-6ylgk9JlsVmG4ADaEMXGodiFSxK-ZaaTSEt97OJ67a7woc8_DZ385TRZSaD9V1aGR0C4An-jPC6ueyL_aAHDyUX5dj6zeNb_izwwUh6W4Bi_y9z_Qr5RsLm2WrlkHOSzeBv-Lz5JYoL0xQrLoGx-j85F5Crfc8z2KbRcKtaHr16w1SVVHR7f1ovlTBJ2dTUhbL1tLGs1C47F14EZkqjw1fBihLt8Gg6UCBcOVzHh95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=asD9sMnv8zGyzYpEfyrAkQokVMLbmhQqdMkFtg4ZTCeL9jVT8ExWW8cBqhd-z2Ka4gEtAmjSsJo3qROjpyQWFLz9mHj2Mmt_JR6Y-efir1-6ylgk9JlsVmG4ADaEMXGodiFSxK-ZaaTSEt97OJ67a7woc8_DZ385TRZSaD9V1aGR0C4An-jPC6ueyL_aAHDyUX5dj6zeNb_izwwUh6W4Bi_y9z_Qr5RsLm2WrlkHOSzeBv-Lz5JYoL0xQrLoGx-j85F5Crfc8z2KbRcKtaHr16w1SVVHR7f1ovlTBJ2dTUhbL1tLGs1C47F14EZkqjw1fBihLt8Gg6UCBcOVzHh95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
