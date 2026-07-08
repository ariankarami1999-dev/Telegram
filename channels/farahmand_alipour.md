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
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRccgvoabv-wGNxNoN2OpDPp9JgmnkW531srP9oI687kUU_RNwZUgc5Y8U35yfLb-YH-6d5N74l_w0Su0fGhXhoDuvdhZO4kYA-jzSaCas80pejAkUanuJ7Ya6gRCXif06sSBH3mrgqbDUAOSyJJHlDvPE6YpJpS467Tgxkc2XGxk7l9t34b7jRQMpSqMANnnlEJNx5_laqWiW7IPEffR-3IVVSxAWG_xJvpjQLwE7aJbhDoriKErOioVDIQYzzbJcfwEpWHiF_NKUUsyUCTxDWypac8Ftm_sGuednOskdFna0XLY8Ko5JYI1spSGs4Z9YWeEL-YHk5_WqCBj3l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEweKgsR7xpOgJ3vg1aBlLpdXLheCw7cGYaFhQ6pkJvjLxI5fxgDJommlivuTRBw5BcZi4EX7UjuSuRR6Pg48xwpuC0l1hAALrEHAK8KWU14fvM8UoF7YMiRKxZgh5fATjGuKeChb01r-IjUT8z--s2-7jRsXtdlf5S_cg8g09u9ztiOpctLvjV3jtES7_sBpLpc7xtz03SeS6UPFF0bLk-qf-QAyDILgtPucUHfb8O7nE-zowLoXl0S9emekFpuHEHE2K9mYRgqEYOAPbMgMJjcsv17hHkAVfrGMJtA_m22QMa-9GpZh0GKUyEjhF4Vv20r4fn3M5iYt1yDGD7LIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-b0jHr_NJTir_ysr_B0SAXAIhuSlkOy6O8cBM4Ppa56gkUAvthkTwmRGHLnTVtnl-Ej6BOTE3nCACIj9K2wNQC77w331XwnAv_SAfuDhWPWk6il8j4e6dWxXLXHBhraRyg_7fOAalVgYktL-3vW86mQmCaHPD_dfXWO9YSXpGVhNGXLN7Q1z6gBklG4EGLFx8McjgPr2euZLDKKrSflf3xU1Yz6wdiG1Se9UkfOj_q3OWh8EDydxTMT5LG-G-wtcQU7S9r5Oresy6iBLBGe8IJYzyy8qlZjrNqI6AE0TFZk_GcLU2MRiui_rSSOTotnFP8_HWHFZ5NoPEvJyvUe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=S3S8PSSFVtzDLPPLwiMdLTFkFSFBstRaS-AatLZxPkdC8_VvfVzp0UD68aS9xed258qRLYdOpXrkASkRXdM310Ae3_UaYvQ0YAS_AsXYq31YTtb64QlU1TqGk0BLDZC9NC4TRlNdx2JZp5KeSTC1pfy1Oglvb9c37-hEV_vtQTodLtMsxJVIsBZxheu1IWFCddLmt0mygcZfb2mxDnLcUnJec8DferHxWeWTd0pkrCzXoZaNS2hFy9Iz6Pr1QyFjIfyHVqzKhMBaPLn_-6D5b9kEJiCZHlzFPoYzYR5f-qi1vsVLo1C6l5H9SsxX1apyjfwbi50CNEJItR0jOqXHLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=S3S8PSSFVtzDLPPLwiMdLTFkFSFBstRaS-AatLZxPkdC8_VvfVzp0UD68aS9xed258qRLYdOpXrkASkRXdM310Ae3_UaYvQ0YAS_AsXYq31YTtb64QlU1TqGk0BLDZC9NC4TRlNdx2JZp5KeSTC1pfy1Oglvb9c37-hEV_vtQTodLtMsxJVIsBZxheu1IWFCddLmt0mygcZfb2mxDnLcUnJec8DferHxWeWTd0pkrCzXoZaNS2hFy9Iz6Pr1QyFjIfyHVqzKhMBaPLn_-6D5b9kEJiCZHlzFPoYzYR5f-qi1vsVLo1C6l5H9SsxX1apyjfwbi50CNEJItR0jOqXHLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGtCvp3gZLfi3XFylHa-zC91OPUSC3aoV6s2SM02W4TIk403vCmZdXVMiIJtsmwO9Br7TouqVPfl49Jq2sSSrazi3BmtiA-8dr3TI46-WYpLtJYXu7Kn92_XKf8dNru8p0Jmktbd4k3wN5JbIJ7AEML3YSRXWVzpBDFhqTQJuOMCFDEFxAKEjgWHM_Kb66Bx5WQA7bqyrCJvHhjykhoM5MlDYQijk6Da1YAzJTyUA2JqU0-pLLkv3KFmhfjzqW2NXMlWsgNBvAeFSWaen7Q6evZ859cn8zWrnG597xhvyfwC7F6n4QGQiVE_mB7xFH3PUuvYh-WquvnE69tzHmVA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=tOAtlDJyfEFBMKgHbmNOyWfcI7HbGUy0zh-GuZnJlKYzGqXi4u_dcAZubGB95boJ739wS80u9vPdkfu39oJS_wHxP8KwjaRPJo3hSVbn1qMDtQw44v2LULmrOfhdd9I44aenGI2rt0ID7CO3wFZlZNzvmPIr9YqXl46aOW-qrVz7cWOu1PDeDni8Dny7ijLcSV0N27bDLa-TH0ltPABjvxWjL_TnDEfx3SUzVdCPCZBfC5SF6Xqx5VrbeD4F8CS5ZGpHo6eKcmLfCusoVugMqQ1v40224HncQYbp-TXblzzgqSoh7YtrQFZAHKei-V8hfwA1_R0TYNLYOpBAUnPXJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=tOAtlDJyfEFBMKgHbmNOyWfcI7HbGUy0zh-GuZnJlKYzGqXi4u_dcAZubGB95boJ739wS80u9vPdkfu39oJS_wHxP8KwjaRPJo3hSVbn1qMDtQw44v2LULmrOfhdd9I44aenGI2rt0ID7CO3wFZlZNzvmPIr9YqXl46aOW-qrVz7cWOu1PDeDni8Dny7ijLcSV0N27bDLa-TH0ltPABjvxWjL_TnDEfx3SUzVdCPCZBfC5SF6Xqx5VrbeD4F8CS5ZGpHo6eKcmLfCusoVugMqQ1v40224HncQYbp-TXblzzgqSoh7YtrQFZAHKei-V8hfwA1_R0TYNLYOpBAUnPXJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH1o5a6Q7sEF8K_1WMwiM9PjmKSoMavcDDE-vgg8CQPL7x6kv-IeHLIITSZ0afu9SPmGwZhamC0EwO_7yb26hoGRR7-xK1--tZ1TxAHQ03w47bOFydzj1hK1Pr_UOglBoSwJysfuw6Ac8SvgOg6nkMyU4-eZdaEVi9w0UNXyUnkcxLrDVpA_gyCQdYskCzRpV-P9on2Ocogag7mSmu5-WmMUcAht1S4LiCsh4_KSp9NpUVwF7mbN0PzStpYRqSObiqoKl3ciYe7ouHouOMaV3AyN2oFWWC_tlXGfGdU32jSfk_y7JnY8eD4gKdrrNUKOcw-iIsoEHwjFBzdXQcr5zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCfVJWDfLqXMRckkHZu9GLtdiBOl6GJTMgVxHvNeMelebw8Pvk9LtPX_6a-OF_DHoAvt7hZ8mAKo6Gdx8todnHrSK5RIb7pYpURpvNe-BTvof5F8BwHYu3PvOcMHgRVtzYbAwjXCK53NKRUyV179Te6IzCQVMVQhAGQNeptTKghD9ifOP7XK6UdJtT7ji2NH414_NefG7D9sfs4jK44ICeHFY_B2eIdFYmLKtT_MrZs51ztH37JDLK7sSbdklgwdpUaepB1NzlyippbanBdDmq1DAiuE8yeFAEYpxK_cF3gvk72MupSEpUyvIMQGzohjbq7bacZnIVeouZ7wunGCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk2zGK2lSpjkAA1FpIFXysr21V1zpw0PPBVzRFqSHY3UTWivrEGSneRGYLL3czy6LU7kkjCiU9mPQMVDe5gAoZdHCdrxS3HZp-7TN4hw9QPpBtdZfv-JxJTonz5kuHtdJZwj8gzC73VLyQblLhu5sgbAx3MonwipX3RYqMTUuH6VpBKMJfwMqXwwHc9ppIF_--C7Uqv_HF7xf4loyxP6F3Wg_Bhd6pWExZBEmxiisBiGDH8jWcnkJV5IZjpKkqO1zRrhp2bmoBlsFxM8MJc3NeoWr0W88-240Xw0a473y8Z-3WYhuu_P76ef0fWuARQInnp9_BAB_1nuDuDgiq85yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKOgK1ow42PnYBCgb5B8Nx2H3q_tyG2aZwiiSag6PcLG1x-LyVonnOZlDMNWKpB92PHV0WkshpWGCZMtfNp7s_GcWeOfQaGqug_z2SZZ5R6AT0544O2_dfXsvbHuRBBhNPUHRo7CyjFrlQyk6wENVb6jkenSKgVJ6M86Y2qzWDdWIm0uZ-UK2QLSO-2Tg1j7bYsCSgFbm4Mg0Gri4lyn0xZzJm0eJ9voueSnJMW_IuVP8WS7k0bgTdJbb9bRb2-1vm_eBT2712ply_G2381EY8zirJG1kUXgmU03JPOM7XhmDM9OgxKhLLf5T6RPi_QihHxVhJCoNCQxfno9GyiS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_9tshyVe9Q0FJ0JuHt9n1lZ6y_2JtieIZvW9cTOryq0zx0pVrTWTMT75C-557YAdFDWSWfjZxxzfjtxVfyT8iJsm2Ghya44ybowE_kkDWY8dw6SGd4rDUIoLGmeHKVVxxI1YCL21f7-PiXllQLz6eyywQwOQvEItVXsO_M3lNVww1BuE23EWVOEa9scrB8ea8GCaDT6KTMLEjpi1oMMZ1ZrOPA5enzxYhQGhMjF68iLnDcT104kMOmBS9T-ayZ0v3Zy3R3EfWWBKv4GmF0INrDa1BE-I5f9x5fmc8KBM4zJnMh9TqSHnOOJfWqaTQWzst9hvtpKDjpk6tbPAZ4CPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=aSuqgOl8OuECCr8mK4evP1scUxM3oiYVEbtzWEj0wvDPe_SvMPYHG0oo6WpEdL3cssaP0-ZqhRdkoAC_WweTlv0PwMs6-cZLVIMGtEpM6lAjtXTKmj_dhHm9vkGf9LLcqxC9RS0SzD5TP62QvoiulCuU_BDts4J9MuyH7RplwYfIPhRWq-Ef6JPOMIDjeTG9rVAjhtsNQfRmhU0y-mIaRe3-VQEQbmL4-080Ok7lID3686sTEqtVyRdV46Mcp03EL-9WU9t96xAg8B1SDQhBjnIfQSiQKk8SjvZtbBZrDV24EbTTcQRpx48xRUAq1ce0VKjXoG8DX3s6VYdVVE_e8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=aSuqgOl8OuECCr8mK4evP1scUxM3oiYVEbtzWEj0wvDPe_SvMPYHG0oo6WpEdL3cssaP0-ZqhRdkoAC_WweTlv0PwMs6-cZLVIMGtEpM6lAjtXTKmj_dhHm9vkGf9LLcqxC9RS0SzD5TP62QvoiulCuU_BDts4J9MuyH7RplwYfIPhRWq-Ef6JPOMIDjeTG9rVAjhtsNQfRmhU0y-mIaRe3-VQEQbmL4-080Ok7lID3686sTEqtVyRdV46Mcp03EL-9WU9t96xAg8B1SDQhBjnIfQSiQKk8SjvZtbBZrDV24EbTTcQRpx48xRUAq1ce0VKjXoG8DX3s6VYdVVE_e8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=NwmGQGoYgoFaqIN6FrvGAqeDf6-1MNJ8v8TYnAFnSGp-WPuXwNDXIsGZ_L2RFE6ssVaCyA2OK0Z-zvZEot_58I3qspz7pXaoT8Q7rk60yrIV6maDFoBTM6ruubsy12shrp9gFKF4u5vLKaXahBojxVUD17bz4UC5cdTBlUh6GOkuwv3EHrPxh_fD2y7ewV_0Bn3EhPWwIk6oHkrTIx_5VeS6O49YnKW7QLdfg79HCaA84ggOevXpxYRiwkt5R7hmbxnVsRhbPo4PbZv_84iZlVw8D86WHvxCsVRWC-Dqj-srHWw8SArGs1zEcyNkKPyrA5cUgJy8vbYDib9Vt2NxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=NwmGQGoYgoFaqIN6FrvGAqeDf6-1MNJ8v8TYnAFnSGp-WPuXwNDXIsGZ_L2RFE6ssVaCyA2OK0Z-zvZEot_58I3qspz7pXaoT8Q7rk60yrIV6maDFoBTM6ruubsy12shrp9gFKF4u5vLKaXahBojxVUD17bz4UC5cdTBlUh6GOkuwv3EHrPxh_fD2y7ewV_0Bn3EhPWwIk6oHkrTIx_5VeS6O49YnKW7QLdfg79HCaA84ggOevXpxYRiwkt5R7hmbxnVsRhbPo4PbZv_84iZlVw8D86WHvxCsVRWC-Dqj-srHWw8SArGs1zEcyNkKPyrA5cUgJy8vbYDib9Vt2NxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=fU5VGWsg2WDa030whjw0YaCyBikg9WVm_2Qtd8VJIR09RG3J7tE4aUeB9_4kMphrbg_wi8IjGY0bgzMYlB0p1rmLiiDajy7KrYo9yXpyQBk_n33PSSIy5z7IH-GwTdmPld4sifu3knQc9h9yC5nLRJdAzFueMZPt2qAP-ZZtZujgmHMYKlnvdqVW1iX_tKK8r-5H7xhfL3W8pImDsfjlke14jHYzdDJjakk_-xqfDvAZzH-kpg6n-X9-PK70FfkfvohBEi2tMKec_Qi9EDlOL3N9K42Qtr_Sd43GktkxVe5IS0iB77rB1iqhTIzxmV9EFubmmWUfpwSzTtM13tNQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=fU5VGWsg2WDa030whjw0YaCyBikg9WVm_2Qtd8VJIR09RG3J7tE4aUeB9_4kMphrbg_wi8IjGY0bgzMYlB0p1rmLiiDajy7KrYo9yXpyQBk_n33PSSIy5z7IH-GwTdmPld4sifu3knQc9h9yC5nLRJdAzFueMZPt2qAP-ZZtZujgmHMYKlnvdqVW1iX_tKK8r-5H7xhfL3W8pImDsfjlke14jHYzdDJjakk_-xqfDvAZzH-kpg6n-X9-PK70FfkfvohBEi2tMKec_Qi9EDlOL3N9K42Qtr_Sd43GktkxVe5IS0iB77rB1iqhTIzxmV9EFubmmWUfpwSzTtM13tNQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=sTQdUtYEKV2qmrb_dfHbF6sG3_rJXD4ExKgFoup-ZI7LiQF6IbHpbHup6eVR2L7vLcVCD2ofrJ8ecpxfoz11RuLuuTTc3-deGvk1FvvfKsAxvL3KaK_NPeOyTfWHfQ0JY6MbHmT6yCWNP3KlGKxvmOECxj76Mb5zs-Kh31IduLRYxVARVMpH2vb5sQSlFe7pZCewgL5shYb6BlIFJIlZZsvlIxT3Xkj5P2GqL-uBBb0og5lj8eGkvBwP-o7D4aKvuKbg8M5iTBjNk-nHSO98AOWulb6pfWJZ3Qz3NXkPMoE8knWygCYtFHM7ujbBVtqL8LCV1cmu-KR0yXIogTROJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=sTQdUtYEKV2qmrb_dfHbF6sG3_rJXD4ExKgFoup-ZI7LiQF6IbHpbHup6eVR2L7vLcVCD2ofrJ8ecpxfoz11RuLuuTTc3-deGvk1FvvfKsAxvL3KaK_NPeOyTfWHfQ0JY6MbHmT6yCWNP3KlGKxvmOECxj76Mb5zs-Kh31IduLRYxVARVMpH2vb5sQSlFe7pZCewgL5shYb6BlIFJIlZZsvlIxT3Xkj5P2GqL-uBBb0og5lj8eGkvBwP-o7D4aKvuKbg8M5iTBjNk-nHSO98AOWulb6pfWJZ3Qz3NXkPMoE8knWygCYtFHM7ujbBVtqL8LCV1cmu-KR0yXIogTROJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCVFhzsSHxgwf9ZxpBz7iMW7hWkGKGfsy8cXLrP48qmpjXWnsvy-Lns-rEHDG0bOKYJxElxIpLm6RbWrVAuxW5jkYnpnwWgMwHD3ew0G7mxrkidnPbSL5lU38Ev5ZBW4xNk9mlsNo9PcpJIpT-JbGmSG5GL5A9ZIHl7U3qtkr8JVoassRQoNWQ19AN33HAjvDXm_5X28WRRO5xzzjX2AsqqDDHI1E9Hza_D5XlpzCfLaKIrBycLsdYVjpxoxNwMLe02W2wzzbHF_xY12_Q9vYOr_2iPgeqqsB5tE6muNQWfC-ioJ6H2wCVAB3ObmRMoGdNEjhgdMkmSH1QIepUHRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=iVS_f45B3_y2gP0H11dnLyM7bBFh9WJgCfngVNVvTNZEFYi1JPwFSrDRm9hx0ZzbmJoQjhCyVK3TlGUi1ijii-i6T_RnfzERDq4b_Wkb3yJKi1emJDQda555xAuP2FUBQWM0y_VtlseeChMPxfZ959l5VNJhZY1dzYiXczAdHlptxucxlHsb_IpH2FFs5s51A9UPtMqtlgrjNWEhLEumop-3nL-NSNAbzb8n_llIfZDyRbjr5wNd0Yug2vcVkZ3ig0flrmdNIWIbPyV2j47VnR8w8CXANNewMDDP2NuMq-cCJlDZeiBj1asyXRIN_MR9kfGk3pG4pidg2pJohH2e_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=iVS_f45B3_y2gP0H11dnLyM7bBFh9WJgCfngVNVvTNZEFYi1JPwFSrDRm9hx0ZzbmJoQjhCyVK3TlGUi1ijii-i6T_RnfzERDq4b_Wkb3yJKi1emJDQda555xAuP2FUBQWM0y_VtlseeChMPxfZ959l5VNJhZY1dzYiXczAdHlptxucxlHsb_IpH2FFs5s51A9UPtMqtlgrjNWEhLEumop-3nL-NSNAbzb8n_llIfZDyRbjr5wNd0Yug2vcVkZ3ig0flrmdNIWIbPyV2j47VnR8w8CXANNewMDDP2NuMq-cCJlDZeiBj1asyXRIN_MR9kfGk3pG4pidg2pJohH2e_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmGNDYx1UALvKs7RTey2eMFTxD_koal1ZHkb1WvbLW5KFOdfYXJ-msQFe5e_b0sJ3Ju0tn_sUdwyzan8CDnxL7hTwgwQPFoOWuXreZQG0Capq06ZZtZ6JJb0tVW8tObXZkpyLq4v9pp9nr_jINxiYLYCv0s98fjAKzLRAZiBlXUakctE562fy-_6ks7Lu2o7eMoJKBfB1sWYwI6NVg1jUHlU_DXta9J2XvJJBXxC1FQ45T_97Guekal5MG1rXPHKhLo-Z4Ni4KME0Vigj6c2xLm2ltWo4YQK468mRSfSbNcg8y8hR2bCGZVwzfpkK4RB-iJWnumjowLuFqYo_P-jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=NEE9om1e6eg3HTeXYy5b0q4154Oarygo3Dti4TzqHDp7iffph9l7CqMQVT5TN72ox2RI7FlDRscVPZtNmmWdNUAA14Uspgo_9YJ-Jug4kFJt8kQ44WyHN1mMfHntGq-LfFzxJpgVS_sKI6BHFtUUjwKBqMkA-Z7LVv04_NgkzRHKfsBf2yg7WxX8Bw8-qgv38Wqw4zrZi-IGYpLrW49Zcl9M-GHDtbHtePCXxpV9ycTRReQzX5CYp5uDd4Mbc-AMsLRFOXjzu_uMbFvsbZCRWtHSkpdtpZ5np899uCpHP_a9Gv7KePP1eL8PIn77zmzRyngmI64PFHizdUOcufiF9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=NEE9om1e6eg3HTeXYy5b0q4154Oarygo3Dti4TzqHDp7iffph9l7CqMQVT5TN72ox2RI7FlDRscVPZtNmmWdNUAA14Uspgo_9YJ-Jug4kFJt8kQ44WyHN1mMfHntGq-LfFzxJpgVS_sKI6BHFtUUjwKBqMkA-Z7LVv04_NgkzRHKfsBf2yg7WxX8Bw8-qgv38Wqw4zrZi-IGYpLrW49Zcl9M-GHDtbHtePCXxpV9ycTRReQzX5CYp5uDd4Mbc-AMsLRFOXjzu_uMbFvsbZCRWtHSkpdtpZ5np899uCpHP_a9Gv7KePP1eL8PIn77zmzRyngmI64PFHizdUOcufiF9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=rOvH-QhDQ5PDbhB26mP2PmWUp9g9oWt0duHknZgEVzyi_7hHLZrYA27VZomTQLhOrDd0kc34qpmgRZ7jWssUm1p4LxgrhKf9o92woow5Ul9Mv81458h3hkluqzfCpgDtUIOFZW34zLP5JtrRni9mLq0YDXDd6ubx_FFU9el5f-bIz1opdenKVM2c6gl20JmtVoffTgPz8qaAK4Y4vt4oQt_8TjIVz-oXVwZycY0D7rsMahgabK-YNwFBLtcv7YMFonPWddTnhao8Io1tt_izbGDPrX9AVTq09lJspgKMcrO2punLfFs6SZ68mnRpURVsmFXCCgxuJahjaw2b7F5jgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=rOvH-QhDQ5PDbhB26mP2PmWUp9g9oWt0duHknZgEVzyi_7hHLZrYA27VZomTQLhOrDd0kc34qpmgRZ7jWssUm1p4LxgrhKf9o92woow5Ul9Mv81458h3hkluqzfCpgDtUIOFZW34zLP5JtrRni9mLq0YDXDd6ubx_FFU9el5f-bIz1opdenKVM2c6gl20JmtVoffTgPz8qaAK4Y4vt4oQt_8TjIVz-oXVwZycY0D7rsMahgabK-YNwFBLtcv7YMFonPWddTnhao8Io1tt_izbGDPrX9AVTq09lJspgKMcrO2punLfFs6SZ68mnRpURVsmFXCCgxuJahjaw2b7F5jgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=K3TSStB_catJEORHiqB5LdK9CoFoHSoiWFUNnHyWEbvn4Nxw1bejbSqkh2WPlG1DDA96l7fxjvaIOJphr4NTbwU_HiTWzw4c_RlKh20FDbihCiE8aAwDLEf4NNr6o-kVc7QSmQ3fNA8gOUxoG_L_GHuAp6vuk_D2u5Zg8UJWCBi3r4dmAPBY6Qljiai1f_kNFq_0vW0zl7IQ1qgcmiKyDGdru_u2jNp8Ee157xwPdx9e7MjGQkX3Txfr4PHzkkRi3srIQ_mDdrtyDr1PRJGLRMiokdP_oiPbIaOtYhklhFXrmalHuq1LdUgQWN90n0JsO79SAntBP7TN0i6Ml5Emfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=K3TSStB_catJEORHiqB5LdK9CoFoHSoiWFUNnHyWEbvn4Nxw1bejbSqkh2WPlG1DDA96l7fxjvaIOJphr4NTbwU_HiTWzw4c_RlKh20FDbihCiE8aAwDLEf4NNr6o-kVc7QSmQ3fNA8gOUxoG_L_GHuAp6vuk_D2u5Zg8UJWCBi3r4dmAPBY6Qljiai1f_kNFq_0vW0zl7IQ1qgcmiKyDGdru_u2jNp8Ee157xwPdx9e7MjGQkX3Txfr4PHzkkRi3srIQ_mDdrtyDr1PRJGLRMiokdP_oiPbIaOtYhklhFXrmalHuq1LdUgQWN90n0JsO79SAntBP7TN0i6Ml5Emfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=IdozijQ9huR714P_51BuHFLw26XGyzDweo-NkiwhMtOKoi91ROPkjMYivg55Udjh-N0-u_VHkPSNDqRo2jNY9VoeK-PQsqC7dYvqHyjJ6fgT5PJxBfEG_r0ymjz8TET6RWFGGInFBh1scchw_bj61gMh8Eru2S_66ev1eyWQ1w8KyBetth4cVf6VH585E5_ePRxCo4Mq_yrqosvlWeWV9ajcSLkmkjB8FxjTOPmT7IL9FwW5OO-gOjoDu_dlmwVpSeghkZLnm2RaM_AkOV6O-gui07OV-zW5cp3BopGjCoXgZ73OyFzadTwjEQmG-j1IGohk0_7b-sBWBaw1TkH5Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=IdozijQ9huR714P_51BuHFLw26XGyzDweo-NkiwhMtOKoi91ROPkjMYivg55Udjh-N0-u_VHkPSNDqRo2jNY9VoeK-PQsqC7dYvqHyjJ6fgT5PJxBfEG_r0ymjz8TET6RWFGGInFBh1scchw_bj61gMh8Eru2S_66ev1eyWQ1w8KyBetth4cVf6VH585E5_ePRxCo4Mq_yrqosvlWeWV9ajcSLkmkjB8FxjTOPmT7IL9FwW5OO-gOjoDu_dlmwVpSeghkZLnm2RaM_AkOV6O-gui07OV-zW5cp3BopGjCoXgZ73OyFzadTwjEQmG-j1IGohk0_7b-sBWBaw1TkH5Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=lPkgoOysS9Ylanrr3dIe2GEGrIaNU0hkykiy1eDKfdRPdLm0XOlzuFungNCTE8VO-8JJTgMMYytQOXksYNdCzLwYb7n0IByRJlJUu0nO4pGBJ97rvJDT8k2L2_BAYYjurRE94JzqjR2NvtYHUNyE0KCLxEpxRghCyaEoKrKtcsUeWikLQIBjjj6Cdyckjhrpugt45QBsyjXNIhf_2LLHUN5VLH77_4Z2yMs_svRJo8XHO34FWlWa9bsF9VTC1FSf9RQtG2xAeT22nryPg1HSxjBUcAAX4LeWRHQw6NeYAwkNHVAAQUAHgq5aA9Hw4lT31ZbaAbHZctMWdQEVE-YIrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=lPkgoOysS9Ylanrr3dIe2GEGrIaNU0hkykiy1eDKfdRPdLm0XOlzuFungNCTE8VO-8JJTgMMYytQOXksYNdCzLwYb7n0IByRJlJUu0nO4pGBJ97rvJDT8k2L2_BAYYjurRE94JzqjR2NvtYHUNyE0KCLxEpxRghCyaEoKrKtcsUeWikLQIBjjj6Cdyckjhrpugt45QBsyjXNIhf_2LLHUN5VLH77_4Z2yMs_svRJo8XHO34FWlWa9bsF9VTC1FSf9RQtG2xAeT22nryPg1HSxjBUcAAX4LeWRHQw6NeYAwkNHVAAQUAHgq5aA9Hw4lT31ZbaAbHZctMWdQEVE-YIrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=OQSu7O81JnYbjoVko9-H8OYBWDeyfqaSjD_QBVz80vvuf2fnQUEsGucAOe6LnFX0BM9ds1CupXtC78UCvqNRdVAzqLjQPKfY6iDg1XwhZcvFJIJJVVbOJL2yQGKrY42eZG90Jj-U6b7i1PkwloGS9yFVUnlisSZmcC-wDI6q3m9tb_cnx3dkGSgJEamMAzo09RBViXxcKD8IlPf2bUQGASfupxhHjJhhOB5gw5NkIcEmNYjXkVk16W-eF9KARlRHIrya3BOTyozOb3nApVasNpX9mkS4zJ9yt2A_wTBclVqlULI2iPPVwnaNJZ6bcIO-WrobmvnXFV6-F2h383ZO_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=OQSu7O81JnYbjoVko9-H8OYBWDeyfqaSjD_QBVz80vvuf2fnQUEsGucAOe6LnFX0BM9ds1CupXtC78UCvqNRdVAzqLjQPKfY6iDg1XwhZcvFJIJJVVbOJL2yQGKrY42eZG90Jj-U6b7i1PkwloGS9yFVUnlisSZmcC-wDI6q3m9tb_cnx3dkGSgJEamMAzo09RBViXxcKD8IlPf2bUQGASfupxhHjJhhOB5gw5NkIcEmNYjXkVk16W-eF9KARlRHIrya3BOTyozOb3nApVasNpX9mkS4zJ9yt2A_wTBclVqlULI2iPPVwnaNJZ6bcIO-WrobmvnXFV6-F2h383ZO_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Z5Gm6odHjv8al5_d0wA9C8xcdWym7w17tLpBS3rNYwmkJedaBRrnGsbxtSGCehGhmb3Bmr0j9rsZJjsiKItMdcTCOwu6z10VU9KjVRS4Os2p4AFRFLhENfmK1mtpw59MEpF-cQIXseKyDEPn4r5wygCHF9eB6vT5ze799wbcFMUkxAvlY74uTHYiJj68WuOVTh4h_sGQkucMUZlzFDu5V8MYDVZv2LIV3bxwbhHDZo7cahl8ZuN4tk8O7iDgISsquIYXFBuUdZK9u7IY_zTjfy2kSU6KvFk-x95l8Xtm9mBGYp8_TsojESkvD4xJ_Y1WgvJCawBUx4Fmfx4JYmQxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Z5Gm6odHjv8al5_d0wA9C8xcdWym7w17tLpBS3rNYwmkJedaBRrnGsbxtSGCehGhmb3Bmr0j9rsZJjsiKItMdcTCOwu6z10VU9KjVRS4Os2p4AFRFLhENfmK1mtpw59MEpF-cQIXseKyDEPn4r5wygCHF9eB6vT5ze799wbcFMUkxAvlY74uTHYiJj68WuOVTh4h_sGQkucMUZlzFDu5V8MYDVZv2LIV3bxwbhHDZo7cahl8ZuN4tk8O7iDgISsquIYXFBuUdZK9u7IY_zTjfy2kSU6KvFk-x95l8Xtm9mBGYp8_TsojESkvD4xJ_Y1WgvJCawBUx4Fmfx4JYmQxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQwKR8d5KsjfVh1ReMOmb9sdmNvgbXY2vZjXTvdakjykyTk1LKbKJsUS2p4FBCHpDjMrSw6yrtfdLezZfw3ggDTa6x8cL-IzFR8W8OG-8S8_QpHDXmfp_IiQcf3i3AYGe7jgBs4aGvT_VLVc68U8eiueqjw4VvsO2nhesMphgIH8m62ScswbsIl9RsJHJw1X6aP9604Vc7-TsVlIsbzGkPOhXRJWuUK2IMR41yFlRiJ3m1RjsuW_AyZXFIAzD6TJncfKn29Q2CeR3I0TTyhXMpPODgqABB7bf-dSbT2XchCIZ4KYWqI84bbjCEey0TW8fK-UIRfiA1aSqbP7jSlVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4z_J8dNcPm38XTUvIroSbcPj2ECl0n2-raaJBJXacA1MXQfRqDS617D18ZParLaQUdbR4wtjaihY3n-3PgEG6kHwZYMJN47YvFWKMBmgfuh3Eb77QMLyp3on4g3K1dXT9JCmDoyRrMEaxuphTf1iTiJCvEFZmj0P0iiOGtszLTOOxl0RdRXxWf0TW9B8XZ-zQDQMROJVgUhDeCNSWwg7a12tvdIvv0sns6WsImYlxvvHz0GZ8vMS_KVba09_UmyklqCtoZNXksI3yDhmaWoDQAhDnqYaQNiL4A3veWqARtc0masaxKJVbs53QzR8ejadwowwajhvMkCP3C3eyHgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=vm3jBRJlwKtGv3f6_oLRXT0T-mMNsQOWxJcUm09vUwHysyRzHdzYn9eo_oR_yJ-ZNEB5Lldfh0OTrm10VDQpfexYZ2B0hLQtIUjV-Ahpq06lVYhypqW1GN0i6i4bG0PGxVP2zVsXJ1FLr9yoLWLS55ijS3Eb9rflYelaDfiI-Lua-XwXehBhtnu2xwwZ2twIVx01JiovNqArSSPSig9m1u2UMwcM3O3WNyC5jSa4yENl6By4ZQNFRL0SlMYxdGcrbWILMYG4-wPN3fqzbEHdF7n3vacJUjXzmb8lz66ANhiba2H2Mxv-UFbWppp_ybI7sRejlyTQclnplf0ZPMMLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=vm3jBRJlwKtGv3f6_oLRXT0T-mMNsQOWxJcUm09vUwHysyRzHdzYn9eo_oR_yJ-ZNEB5Lldfh0OTrm10VDQpfexYZ2B0hLQtIUjV-Ahpq06lVYhypqW1GN0i6i4bG0PGxVP2zVsXJ1FLr9yoLWLS55ijS3Eb9rflYelaDfiI-Lua-XwXehBhtnu2xwwZ2twIVx01JiovNqArSSPSig9m1u2UMwcM3O3WNyC5jSa4yENl6By4ZQNFRL0SlMYxdGcrbWILMYG4-wPN3fqzbEHdF7n3vacJUjXzmb8lz66ANhiba2H2Mxv-UFbWppp_ybI7sRejlyTQclnplf0ZPMMLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBnx4fLIbW14BVBeGr0K6jbRdSzl5RxoqYgJ-y6k5lpYqIgbgX4kGPfsLIWuoT1WBreYGlit3LIPd2fGsAuafoP43lmfpbiL0mJIK4tfhVhxdMiQ-FNR52iPVUK1Vh1b9Kw5ae4y1xfBKKPSwA7lKOEGGTB2OanISATkSgmB7UW6QZ-QVyn8LZ28fyxhDKqU_hw-jpUjBVC_Zd9a-KXdEdN86-OkUi4A7CfBMUY3NmO0S1whcbqRvtihqSgFuDrkJUTpbUf35n7g76nGa-HXwNPQOdjmK-Si9AqK7ohOJFsSHy_OR23thDKymlDNTR7tZRUFf4g_pG6IXsxqHfTIoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXKnZ4qUG5GXTpu8b0T3Rc2UtRAIahmX-mzhCI94zkgHEvVWJ1O9-ToWpwn1GY94xwYSLgdzK1im1hjS9sakNXjoLrWQQBuh15i303XEdt-ch8bszBgto8AWTlARla6ClMIHVLQmWnzRoRff3-iQDp4Lj8j6LCOZFwXU1hvomLb48EJ1E_GL21OSaXgsVZrKSGvaeczWdf26btwnW5GGbMYmVU6iYN8OjPjlsT_8aafJHLXA3u2SAWw7ZmJZgBTMuJsNBRtJVoW4nJiRNNO8lcOxkyq7d2YrnEh0HyMgb7osnYVtXlI4u7wiKttaZSoIxQ7urWSGaW7Gl2nxY8gXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=QuYfg2nYA1Z-dhP_CQPg9GwbOXvOqldzyIsS2Zyeayyw9uLtBwmJ_1YiIJ-xE57hLnlCKYh5Mr2rGALBn6MNTe8YfPjOS1WuFh4yfQzrmJisYlb0BtLHExfYHODEW3OaOVJX60CsvElkSVS2okIlWutwM4ejiVWN4pnSBk2jNTy219dWRIIsBlbDyXhivZ21efs6k3Q6owgbnERweS7K4B2YcrOVwZagZuCJefK8dzDLDqqcIy7-JfsQ3PVb2V1pviwLKXPQ4YLZZr50hQExXh1jk_8Dir0C6AyJuG-bgSvUlcxXYSlLQsI9kP29D2kdU6DNWSPcoO8htur3jXGXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=QuYfg2nYA1Z-dhP_CQPg9GwbOXvOqldzyIsS2Zyeayyw9uLtBwmJ_1YiIJ-xE57hLnlCKYh5Mr2rGALBn6MNTe8YfPjOS1WuFh4yfQzrmJisYlb0BtLHExfYHODEW3OaOVJX60CsvElkSVS2okIlWutwM4ejiVWN4pnSBk2jNTy219dWRIIsBlbDyXhivZ21efs6k3Q6owgbnERweS7K4B2YcrOVwZagZuCJefK8dzDLDqqcIy7-JfsQ3PVb2V1pviwLKXPQ4YLZZr50hQExXh1jk_8Dir0C6AyJuG-bgSvUlcxXYSlLQsI9kP29D2kdU6DNWSPcoO8htur3jXGXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=M4Fo2vdt9Dc8tQqtBVir5EjLJaSXqBAj5rsBY4TjmlU8QAhF-3GV_gEQtFWOhKXv2LzXM3rhhypT7Og5MIHDHUBw48oZSURXFySJ-Qnb1EKAf__yJh1Wvw-9iNx-UP1bajcrOWO9uHxGSEKajtIbYEiles63Q82_i9yBIUePvKJ4iR9sjlsXzmDWRc_UY8SrqHF1MjTa6pigrtrRzqXaMjslZTrWYVK79g5i0DrW5d4ct-KrvZdIzSyzwcsNO4VfG4O1sHMr7YjGZSdvQYpop85la5TaHpjnu5QewvEJTcFhPeDFpvKf9h-7wf5-nWfNQbwlKRCYMu_LHxJUTGuCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=M4Fo2vdt9Dc8tQqtBVir5EjLJaSXqBAj5rsBY4TjmlU8QAhF-3GV_gEQtFWOhKXv2LzXM3rhhypT7Og5MIHDHUBw48oZSURXFySJ-Qnb1EKAf__yJh1Wvw-9iNx-UP1bajcrOWO9uHxGSEKajtIbYEiles63Q82_i9yBIUePvKJ4iR9sjlsXzmDWRc_UY8SrqHF1MjTa6pigrtrRzqXaMjslZTrWYVK79g5i0DrW5d4ct-KrvZdIzSyzwcsNO4VfG4O1sHMr7YjGZSdvQYpop85la5TaHpjnu5QewvEJTcFhPeDFpvKf9h-7wf5-nWfNQbwlKRCYMu_LHxJUTGuCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=S7pq_wXZhgRs5yvBb8djdWG0hYlpFJEyTcTGnZn3jgfo_HALt9rCzXX2AC9UTKzMFrRaA-SO7pJ8jc3V_qksWS0B8Xft17YpI8AU_qnSiJLN1xWV4sAQiT_saXV26Fy4kDyVbq7ojL__X6hh-BQBYuKrBn7FIrikEd1lPFFvV9nzlhkiOs-iVMCKoC4jwxIm1-zEirdvMppJpjwdBBWJXGhIJrXHS4OidvIY4F87TMdS48n6jNwio21OcefDdCa9OQ1X_DtjOqF4Uj0Sl7dNHONLsl5jyIWXVUSVrMowFvSgMxY8nwkAGwLeP5rO9C2hwEZnhKW6qUI1pE_coyN2qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=S7pq_wXZhgRs5yvBb8djdWG0hYlpFJEyTcTGnZn3jgfo_HALt9rCzXX2AC9UTKzMFrRaA-SO7pJ8jc3V_qksWS0B8Xft17YpI8AU_qnSiJLN1xWV4sAQiT_saXV26Fy4kDyVbq7ojL__X6hh-BQBYuKrBn7FIrikEd1lPFFvV9nzlhkiOs-iVMCKoC4jwxIm1-zEirdvMppJpjwdBBWJXGhIJrXHS4OidvIY4F87TMdS48n6jNwio21OcefDdCa9OQ1X_DtjOqF4Uj0Sl7dNHONLsl5jyIWXVUSVrMowFvSgMxY8nwkAGwLeP5rO9C2hwEZnhKW6qUI1pE_coyN2qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv_zHnl28BOH6vlgAZD5VVBH2NE7dfolJfc57AQQMjZ36mU6fmD--JHD3mPqVy33uSSiUcXdDPtzq0GkKx0TI-FpyN95CEOQOX0w8LzRFHleOYjrN_nU3qSAg0jzV0BCKu5-Vwpx5YVcDXavbi4v78sglfn5ALPz7ymS1kXcknUx3ai9tE2hU8hwMyKX9iC9atvmm-MSy_lTBxxL2dKe1scfEZQzGkOMQ5E0_k-NR9oyw0nqDIr_9tELKlYg3u4mzoM9KAoMBKFpfUK_RXpN86FiUWGwaEY9xDcnjzM2hpKRax0LCGBvp4lM1LVdACFaTFWIhkNiMRehbXfBBjXA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdaqW2pEFIPfKOrUF9knAJRtFqRJ0bYvxCx3ZHMW62Cz-7GD-VLxK4CaeIY_w4QLJBOzyxFabqfb9cn6Xz4z75E-TzM1d6WNLpX5agqH_bgYCUeqmCt2mTwcyGUnf-AxfljXEkVxmKcmrsfXpXi6xY_qo4Dq3AAAXSX_NAdxv9tXkuHn1HN1hgcI8AUXsLNOoJSeUb4djEif91vIkK8LRkpZLCm82DIpAIjPC1Z37dCYckdEx1ftYbH-ZCsXv0uTkM6m0Ii2GYis1DhzUpLehsLbTV52CnANsVK53f8a-zl_qWlv2VFxDC0ED9AEwSJiiRO8mT4RdDEwsGFdhJWosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=pIyZzCRF5Y06wyaRBjdCOFzEnWlNIQVeXuwtniozklnZtbOjJDZNXSLEEHu2UswlIOsdAPvpa1yQXOpldb-_zrcKrLih6sKqnTPBd7TomW5eND3ySPKUfuEyENLNRqWdJWBOr5QWImBXFQ7tIV6ugWyzOjkcbmk2x8kg4r9TIncPSj4s5PkqnCfT6Jw8y8Ub9G6lX11qT3W9Ea8xArNmW4y-mLstMhlbDM2HiURs7gmAGn1Iej4ZR1nb8DOzn8ZNxBN6qlPBat_zQ0QfgKlM3N0a8_6cWat-tiFTIkRDiAVuJcL2ZVP6A0BS2ahJQxZubfv6mC9BMFSxnuVB52zD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=pIyZzCRF5Y06wyaRBjdCOFzEnWlNIQVeXuwtniozklnZtbOjJDZNXSLEEHu2UswlIOsdAPvpa1yQXOpldb-_zrcKrLih6sKqnTPBd7TomW5eND3ySPKUfuEyENLNRqWdJWBOr5QWImBXFQ7tIV6ugWyzOjkcbmk2x8kg4r9TIncPSj4s5PkqnCfT6Jw8y8Ub9G6lX11qT3W9Ea8xArNmW4y-mLstMhlbDM2HiURs7gmAGn1Iej4ZR1nb8DOzn8ZNxBN6qlPBat_zQ0QfgKlM3N0a8_6cWat-tiFTIkRDiAVuJcL2ZVP6A0BS2ahJQxZubfv6mC9BMFSxnuVB52zD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=eXt84q-FaqU_4EgRj-mmWEINtY8B0Qvi6XSNSseGP6bp5pYDzFO3XXsgsikLtClgWWizU-BlKGr_qh8qYXzEJRCag3E5bExzeMRNSt1qykzQtOAYBklJLIE2fk1iE6dbzqu_8lpZv19Dve4WV5iL9ikjdDSYs611_tx6jzBM0rpIpmKqoD-qTbcrtkDhs4R1cs-Pg5UfTeI3FwvRlkTbNSeC6-Ea2PSDE1sqGVN1LyQppKqB8tNLUTSH-axrnJnTq20EoTAiqcm7yDfkuCeM6aLSurskbRxCQb70ti3oypb1jcseixYAO2rxur_CzAMf8um5ET4wS0cuLTx0Iy0iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=eXt84q-FaqU_4EgRj-mmWEINtY8B0Qvi6XSNSseGP6bp5pYDzFO3XXsgsikLtClgWWizU-BlKGr_qh8qYXzEJRCag3E5bExzeMRNSt1qykzQtOAYBklJLIE2fk1iE6dbzqu_8lpZv19Dve4WV5iL9ikjdDSYs611_tx6jzBM0rpIpmKqoD-qTbcrtkDhs4R1cs-Pg5UfTeI3FwvRlkTbNSeC6-Ea2PSDE1sqGVN1LyQppKqB8tNLUTSH-axrnJnTq20EoTAiqcm7yDfkuCeM6aLSurskbRxCQb70ti3oypb1jcseixYAO2rxur_CzAMf8um5ET4wS0cuLTx0Iy0iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWAFAOdOpNE_rVX6wrC1rar6nlg7yPRH65Am-cbrFnQ0pl0WlY1q9A_FEy9g95MwH_15voByTHeTdIINStZLY6bHXpR42k_mL1Vpc3091xxTdLQtyy074fSZKxDdeyxXULpiuu6tz7ChgQLGaRSDQRNwidSHIJjNjwVmcIaXoP6MsqKb4f82a1ujXBjeGdmraDRK1D6gx8paJvTA9PqIEL2Zns43OEreuZ9j2lx7iPh5JOwENkMW0oj2-rNBaiUrXd3Miu7TzbOGy1h4B6vCKMx1XebI01ooK6Yk2mepB3XciwgsDeyTLiepMZk0_smb2uJteDBuoWs3HuNTnFtdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZRfVZrR6OV2Re0Q23xfQJbMK8_3MDJDVNWR6tled4kiI-svOVv7czX0MuLBtNFyAQMy8ksi9CraE4KlYvtrQ5Mo8UTKnjT-TQ60e2PgLcfzLfwjWq1iFnDvia5RIqhsxWR_uR2v1xYG-N9bKjkbj9SIa-AHJtvbBYVhn7fJF7OWhfFsBOR8P5A0U4_vqGc9a5-Da8XgyaWRhkDe-a3sCL0QlbyP4otAkw3kvtPa0ZUC1q2gDa7N4OgV5VF7pBpieA3gzwsrk-VcudKeJ1YQo375SUxVIXTJaUsNiVG-rw6fUdUMBssagePP-Vir5BkPF15o0MvhEyK6rHvvhTHSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9pDaMlB-unNy3O6oq7euqF-AF7vWfkhIhbJryICOp0qJ3kHz1oZG9wy8C999ZsoiG5aYFpaQ1gAoB7JuamO6thWs-x52lXkXMAy4aJkb54Fsl_I0A9hKolcQMQNGqhj5zeJCx4qypi7eHQpegj9ASJn1dGixJdqIP_ql3SJcbUBOIsEuk3piLGh6PTX5nGkMRTM5zt0IqF05dx13OrlPTguX5wnGFJu9NKWu-k_esmViYZ6qvVlmWHFnap2QqQJBga66a4LOa9ATSayNLjHFS7nqJyfR8cATZpu5Kl5P4Mhefou336TVWFoGKeqTn8tLuIZRY9HdSeCEZtzF5wASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyyGpZ8ELkTBekjbAnG7uIVixKui7siLwrCvO1G1ttHAT8dWB9d9pIFPTiUXadj-MGptP2veArmrRfvZumeKXkrU1LLh_cRh6NayP63Q9yrzW9A2uDQGooSoqjoROw8A2_saHPB9qxKsJwuqOAOJEAW4Xm1t5j1Vg5y2kM83_pWOlIvCd01btJg-FkQ9OROhYDY3vx3nM5f60UziUex4j1YGw-kfg2bB_xYyYh9pjpLvwaNUBRXKRQQpepqlraeCgz4_0a4Zly4TC-q9WiTo-M35qK0CBjS4Vd4At903z4tvXLV2-qLfHYdOlz1SYSCyg1cHQWzFDSIqihnrOTwNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEMK_v9ONFiXU52a0dVfbi13I-JM5H4060ZnpvWhq_tc8jFeDxEX0ds5BuBHD9Ymt8jWUzxpmUK3Jdp-1o5QKBb9h_pMWAfAL7ac1oJwLrP-bU-9G1jp66L0UmtgSXqTjllPuq_ZrWyjQTri93yCt2Svppcv93fLF8TF0K9WdkfAVi3rmS71WZuJZTShJUC0ywVs5He5jqZXXiSDR2TjCrHILiKseDpmw6pemoLRBgiDcK5PkhNEghB5HClSvrUW9KA-l0BNGaaJqGBQMGocSQbFK2yYo8PaBQ_ciO7xYFcjXhT_edW3WhNBCGcJy9r9sl356KsuFeogZZ7i1WPIBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY4mg4XAJSPnanE72JxHin7uRAQxB2qZYec4wqqwJJLXO-UVBY3ftiH_OVTYOiWC-HmJVTPyXonNpLT_vRfFn1YAFFcP4AlX4Onc6TrQg7xM7ZrNAl7CSXwmMCjXK-TF4CshlW7ZoxkjHTeJRENrhmsMqBuiKWF-mS-ltA2JV7p6HlBC_J3OT4tThw3O2blihYdONYDnvKZxZVnDG6DEeyOuLObOIq0Slj1MP0DHydj0kYdOcROzOyc3EcPasbO9h3Eq13wCJT9jhVnBiLuAVml3bdrPKUSWl-or1vS-LvVrlW7jwarQqRtZwf6JNukPyGiIV1R_lZFSz46_rs9jLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ovi9oHZbclIsqj8meM1KOAOhHGCQLQ43udX0B8LA52hEyMybICx5Mw0vcI4jnypVM1IwzKoFQSCUNtX8mayVHTXUMhb0G2417ULohowkSChzvCGLfEVaX1gwRouzeduEq_BTrrnUEK3l8i4RiMgqh7PJEsuhQ5lPIwIRPP8OerV-nvQ8V6djhWzjeewKgMzcFGHsi5nNhUtKbNvuqEcDHX2xiOxyhSIgaDfOBB_SeqjZ-9ppmOMyIfZcdY09ywjTIawcWSpy8p6jnS8ap7CLukgqrl0QLKR4rF7540wdpPcyo4Zv5aja-7DflWNbNLXOEU7V8j0u9JIP8edblmSu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ovi9oHZbclIsqj8meM1KOAOhHGCQLQ43udX0B8LA52hEyMybICx5Mw0vcI4jnypVM1IwzKoFQSCUNtX8mayVHTXUMhb0G2417ULohowkSChzvCGLfEVaX1gwRouzeduEq_BTrrnUEK3l8i4RiMgqh7PJEsuhQ5lPIwIRPP8OerV-nvQ8V6djhWzjeewKgMzcFGHsi5nNhUtKbNvuqEcDHX2xiOxyhSIgaDfOBB_SeqjZ-9ppmOMyIfZcdY09ywjTIawcWSpy8p6jnS8ap7CLukgqrl0QLKR4rF7540wdpPcyo4Zv5aja-7DflWNbNLXOEU7V8j0u9JIP8edblmSu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=e0d_mCBvVKAQ41iN_UpYvoKixXv3GruRpTWoVr2AMkr2noI-lEd77c-hHXwegbIh5K4BpeWJ3EhfYdK2N2UMOVp2FYs_KOQ4lsuXjWPpmecAAh82WdaAHfh0DFJBBfPnagVijFCHOp2kVgVjEAx_FVT4aK_jx8iwYMr4VMGLKmoEg9gYQWlM5nKEFoPpUbydDX-3woyd5_4cQG4xtqPyck5llWYh7rgy4WW6q6-hPIaHF-8zNxMe8sA41fMlGq39zg6XvospERwO-Ix0ObIQDgsFKELB3xX7a7ZrjFzkv8W9P3-ZBSEevUkB8vmQDPNfNsPeSFuKVjaXGHX2vPm0wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=e0d_mCBvVKAQ41iN_UpYvoKixXv3GruRpTWoVr2AMkr2noI-lEd77c-hHXwegbIh5K4BpeWJ3EhfYdK2N2UMOVp2FYs_KOQ4lsuXjWPpmecAAh82WdaAHfh0DFJBBfPnagVijFCHOp2kVgVjEAx_FVT4aK_jx8iwYMr4VMGLKmoEg9gYQWlM5nKEFoPpUbydDX-3woyd5_4cQG4xtqPyck5llWYh7rgy4WW6q6-hPIaHF-8zNxMe8sA41fMlGq39zg6XvospERwO-Ix0ObIQDgsFKELB3xX7a7ZrjFzkv8W9P3-ZBSEevUkB8vmQDPNfNsPeSFuKVjaXGHX2vPm0wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=DTPdvqsn9XGbn4M0Rsmlu9loaudnZkbszH9pQVvydkmO0_Dgr1w3fQxd4gDXXafs7hTgmaJelKOkcAnJcdQl0KIf5Qr3_lvF_w0BGLzrjDVZNO5bDqXiCS_F6iyWEH_oJ0PdGoYMaBhb4zBsbqqA-uHPCr12sJ0KUMHdp8gb_WTmXUU5xWD2t3To88JnTYK_TYQxivgxFHLXpWkx1htXhfueWqjDamvyXtC5yb3gmM2FkYCZYTaTZuvCldeQvzzvck8Hy--APPDLDZ0wtriklzSwcglK5umrUzZ6AsX6lxcxZsCoaLDtazfQJuGxi9RTSBhza-5qB-IgUF3qL4MTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=DTPdvqsn9XGbn4M0Rsmlu9loaudnZkbszH9pQVvydkmO0_Dgr1w3fQxd4gDXXafs7hTgmaJelKOkcAnJcdQl0KIf5Qr3_lvF_w0BGLzrjDVZNO5bDqXiCS_F6iyWEH_oJ0PdGoYMaBhb4zBsbqqA-uHPCr12sJ0KUMHdp8gb_WTmXUU5xWD2t3To88JnTYK_TYQxivgxFHLXpWkx1htXhfueWqjDamvyXtC5yb3gmM2FkYCZYTaTZuvCldeQvzzvck8Hy--APPDLDZ0wtriklzSwcglK5umrUzZ6AsX6lxcxZsCoaLDtazfQJuGxi9RTSBhza-5qB-IgUF3qL4MTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=FlmDYiSGJfn4-D6WPPKN0-pQ45dsPMu5_2uYpJ6wifDxv8cCY_BKaGQPIBOM7SnSUeRCnj0N63iRSe6CfB8S2IMyF2JvPg_nSDMdpbEsq_ARFs9UzFQnGR2Lkk1eqWzrgSStphAteThp2nHOSOO_5WWLRHWsZJ9uT5aMoj3i2LidU18Csn32BJNJQoPtUmzJMWzq4jWJvy25onKOW_wfN7ldsL99JtSXEstEQRpqxjrOEHHYQyVxCXyM4dbhuwH-IKuzjGn_oN6tWahFplMn7YdlPWdz0FWXMExB_VUxZ6wkdrDaiDtZc2RaMPz1uXSua_vS2lwDI55AJgELV3ynVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=FlmDYiSGJfn4-D6WPPKN0-pQ45dsPMu5_2uYpJ6wifDxv8cCY_BKaGQPIBOM7SnSUeRCnj0N63iRSe6CfB8S2IMyF2JvPg_nSDMdpbEsq_ARFs9UzFQnGR2Lkk1eqWzrgSStphAteThp2nHOSOO_5WWLRHWsZJ9uT5aMoj3i2LidU18Csn32BJNJQoPtUmzJMWzq4jWJvy25onKOW_wfN7ldsL99JtSXEstEQRpqxjrOEHHYQyVxCXyM4dbhuwH-IKuzjGn_oN6tWahFplMn7YdlPWdz0FWXMExB_VUxZ6wkdrDaiDtZc2RaMPz1uXSua_vS2lwDI55AJgELV3ynVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=T5a9ya_P5DfE2DYjsKd4dtw-Hug86J89JVT2RwZ5UmmFh3zIhutblre5w2hF5jIrf_DSpHFy81PmkTWXdViegbGmRG6UeaPRgVnFxDuRNX4JY-4_lhwqjxdkjcQXMxzZbp6zPhV4-7xeGG6ao5hroWvYj8b1SbYzmKpbyfSIrB7w5RdXGBd_I7WRAATq2qMKM2bJIsReoco7lkL58bFaypHjsdfbuGLH32Os2aBx4_b2FTlFep2ynVRL0Ul2H6ymlouiSSrdxmzweQzxSEXahZrn0Ig6QorMkvRmFURhORkGODRU9X4zPguw6gxSkHzT6Zn5R9-acUi2Ki9w9WzlLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=T5a9ya_P5DfE2DYjsKd4dtw-Hug86J89JVT2RwZ5UmmFh3zIhutblre5w2hF5jIrf_DSpHFy81PmkTWXdViegbGmRG6UeaPRgVnFxDuRNX4JY-4_lhwqjxdkjcQXMxzZbp6zPhV4-7xeGG6ao5hroWvYj8b1SbYzmKpbyfSIrB7w5RdXGBd_I7WRAATq2qMKM2bJIsReoco7lkL58bFaypHjsdfbuGLH32Os2aBx4_b2FTlFep2ynVRL0Ul2H6ymlouiSSrdxmzweQzxSEXahZrn0Ig6QorMkvRmFURhORkGODRU9X4zPguw6gxSkHzT6Zn5R9-acUi2Ki9w9WzlLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dBkNrXG_spcTYwiq0DdvJRvBTms6K5yD-knn9zLOV3fhpSNuFr1MYmd4OYQ8cky2c7uhHnu5TNCGBkjQgwGlN12fv4hyeqI7hQ9oXgt4wrFYlzoO6_ESWGkvxMITTYahNHCnskBzTVFz8T5O2hsAPbGmnVlbAdX8NasgkKvBXw750SwGCiTrPJXZbTitd4N0ABKdRm0_KCW04yOe0cPNB9cYI8161h_2mU5JXYogimjsh1bQEqPXB21wuofsCBtgre68jVOAKSKIXYmO1fU1xpkbgvoaM2x92SR_q6P3fTLi67mt2K6yoGyPuO-VJAne66vvquX13HXDgk12vIADbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dBkNrXG_spcTYwiq0DdvJRvBTms6K5yD-knn9zLOV3fhpSNuFr1MYmd4OYQ8cky2c7uhHnu5TNCGBkjQgwGlN12fv4hyeqI7hQ9oXgt4wrFYlzoO6_ESWGkvxMITTYahNHCnskBzTVFz8T5O2hsAPbGmnVlbAdX8NasgkKvBXw750SwGCiTrPJXZbTitd4N0ABKdRm0_KCW04yOe0cPNB9cYI8161h_2mU5JXYogimjsh1bQEqPXB21wuofsCBtgre68jVOAKSKIXYmO1fU1xpkbgvoaM2x92SR_q6P3fTLi67mt2K6yoGyPuO-VJAne66vvquX13HXDgk12vIADbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqpxhlUepW0knekM91oZwG7KBLJHPEgUsUTG0y4O7a38EUmGpqQKLreknrm_xm1aAEMtsiRQffZ6HXtZ5Sh5xhY5IXLO89MJJT2XbO07cggMcZdKqmqjZ1OFDlKZxalrIKusn3cYVDg57IV3GcJyqFmsPYF0bTQqb2pkjPE6W4KEbg-bIBzlYZc1zpbYsRmHUnx65-pOoPnCrPdqovcYBuNlxY5HnLv-qLhi9m6JoFMgq56mUwzdB3uFbY9EuYy41LnfEee5w0zBAZxgiaA16O3pPzBsh9I26ZdRTQ9QHCoYKMXYuq2LUtRmTPRIIU40glpyIq7gm7-d2-1GXxbDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=S3KFJBGksrLmVJADTfwjlFwLV1dRI9bHckDpGZg4bmvka1KaUB3I990ubIE7EHdjN965ZLpRv-CdLRh52u0cS9W5BeQbTPB_vG-_miAc_AZbDakWTDfzWussg0vVMxRw3QFDlNi4GOxtRCK3T87Di_foaiEsdGHVWb2d_DrD2WxnjjWXyk5HZ4DjXN12aAEGbsMsYg8sxQHgbsHperL2BYQtbxCUw9G70nlUYA0vmiTBJWqudDvk-2IgOkbh8JS2cSsAF_QND4YoyKLAc3Uh9dh86-TQpDXJc3OCTfkfUhhp3MMAYSBOD6fF65SsHPyFvW_zA30hGopWr4GaE69Mjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=S3KFJBGksrLmVJADTfwjlFwLV1dRI9bHckDpGZg4bmvka1KaUB3I990ubIE7EHdjN965ZLpRv-CdLRh52u0cS9W5BeQbTPB_vG-_miAc_AZbDakWTDfzWussg0vVMxRw3QFDlNi4GOxtRCK3T87Di_foaiEsdGHVWb2d_DrD2WxnjjWXyk5HZ4DjXN12aAEGbsMsYg8sxQHgbsHperL2BYQtbxCUw9G70nlUYA0vmiTBJWqudDvk-2IgOkbh8JS2cSsAF_QND4YoyKLAc3Uh9dh86-TQpDXJc3OCTfkfUhhp3MMAYSBOD6fF65SsHPyFvW_zA30hGopWr4GaE69Mjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Eux_HpPV5X8cVTHk-Ny3NpF5R_p0c0BFTRkTzWPCWOPteuKH76IFo1G-1SiRQj86ZuTIkpLprPsJlgTqYYhxbNwmg8tMEccK3BpucMffHewpW46btO2uPuOb77_dlMoxYRUPQqd2XevTx3xeTSy6r9LAv2jn0PZXUY1hQ2OoUgHqjk2_nhK3TeSDZ0w-7dbYM_yp9d1eXPcyu1jiPhxtqGtOSEhD44SK-CDbDxv3ClIn_ZVG67zM96UyUhux6F_6W6JdJyz_aUtUSQfArIYR1xoM6dfBrcF4oQobpWeXfQVkP1UYXgHyaFDAofAOjtt7UyYMhVi2R_ZmesB8rEcpVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Eux_HpPV5X8cVTHk-Ny3NpF5R_p0c0BFTRkTzWPCWOPteuKH76IFo1G-1SiRQj86ZuTIkpLprPsJlgTqYYhxbNwmg8tMEccK3BpucMffHewpW46btO2uPuOb77_dlMoxYRUPQqd2XevTx3xeTSy6r9LAv2jn0PZXUY1hQ2OoUgHqjk2_nhK3TeSDZ0w-7dbYM_yp9d1eXPcyu1jiPhxtqGtOSEhD44SK-CDbDxv3ClIn_ZVG67zM96UyUhux6F_6W6JdJyz_aUtUSQfArIYR1xoM6dfBrcF4oQobpWeXfQVkP1UYXgHyaFDAofAOjtt7UyYMhVi2R_ZmesB8rEcpVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLQlt8MQdCM3UMgROADXV2-ELOE2DAzkFP-mdXueUzwIHExKXoObyuKZwwi32C11QfMzjc0Ysvr9-rZ9Q6DJwVmu7zx6WtK9DKHzsg26POqBSHKa7ZGG-MItSBGfjxfLBI3KASs44YURSRP2MZR-rsP02yWK2AP37Wkwx43_h_KKb7fMA5dfS_T-m3rcv0tczi6i3deFJ5w1ut7WPNl1I9SynaWkpqZk9vrbe0DMs1UCx7ymOzb2VUtv7C_apbUVcgAX8B-7TYCf0JK1Cv4gJ-GWyDFxcWMwy7ZeDD8sEiTlTHwDmObnQkqRQa1LLb5QLRf2YLWnrC6zyh17HzgAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phHTUGWBtLF_IAAXDUDpqkAYbX456mEZQRhIQmv8OmOahfxSjKHUfcbRHN_zNxBabyRqZGJ6ebqnfm6q-27PQWXVnsMAC_kfnq9zlp5Muui9kEgnhjbjCnmE2TVmqsPfFSX4vOdP3BbstH2j9dO30Jq2rk7OmV6FpV-oRuHI-JV4A_-yjKnTa1G9H0KQWezeZA_B6PbSEN5LSq_qhS5hhyZ2SH1fKJnAy0zfGGuxj5tKyS-XTUP3Kat43EwYK3c87d2LFj51aC0l4DaARELr7u6Z9AlcgGu6CPB6QdKhJWSLB0DAmhu_66Y8UFEAO-xDZsK6bR0yYQdinACn7nEwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJwg0kkvioHg9Ew9mmJ6NXD_Jkh4-N5OoOenATT0tET4o2gfq4ptg8h1Kf1gJv2Tg_NOxgmqxF5xj6lq4GdBjdkGdBytNarJ35ebDX7_Mw7NhDqSUZlxhXQjp8VZqCd8XnACf9h_RUnZLBMxmGORpVddNHlD6yLawprW7hDI1jHEidtdJUCxObBz6NCvpKpJ1kXOlXHgSohjwEKMwI4mrP7vYmrhXLS29GwDQ5GCzVgxSC3hCckuRXJua7lwoNPariqI_DNeitZTA_2uJJzNALIpuWENMEHtPPKhIopMz9Mf6zz4mFBJGdUenLrhmRbMDwdDif8aF3IcyiEfAnQC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMkBi08o5eMW3ifPNrHja2o3f7jphuoPJVvbOg3W3qbRik6vuEMm2wjmzn6hFa6GA-EfHEp-mbfOfvAst_rtSt5uk20PaQprnl6Lz3nF9SMDfsm4oEWu81K4Mb5sOhfrkhb-9b9wguVQFEeeyEJpZqMChgNC68LJKzt3-s3Umrh4aUInlGvibjgDTMZH4PKADBUl2KCrCG50HebRW7h0JXEVRrR66Nb9ICbg-NMm_btdLOMbGI80YtePvguiiSNqAHBMvxra-Occ2Eqd9hFVnPuw6aIs50VIqcYSS9hvj8b9g5w4C9WDKuuB9tFRm990U_2tL2EFJJMpJ2IeXhKwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQzrIxXC-e1dYqp0jV0Fzgl4TKCEqTT3U8u4msgpno5Lx8U8ky3E77utK6S365OX6ogOs6nHJaoUpvDxMBeGWVDYknSdhY3tZl6kKzwQlMcPIad8WQm_dQYT3a4AxSOkGfbk_V2mOY8QHDB13k9w-XRTcVC7i6obOBkkcAHZ4cUrfpN1u3e_2cK8B4UGTRLOYKruSLQl-9ECOoqIpuo184RnbrfDud8ngGzfBacYJqIfAO8Kt1scqcHzQ92eXASrMmvoVHfMmTSERDwkT_-XYHe3L0tqXQgDyDCvC9VzDGGeNFswUhLRuPW67IMo5xF6LYoy2wZZoaVQ_YJ9114Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-gzQBBhG9A4uQ2Ox1hnLjJbj-017PSj99PhEu1c1KAMZk_PA86aK_LrfXdxLUm6gkvXr3wm_diftcJGzEro1mMpeDtZlpkCQNPEF_I7KIw3Nu-pAXMDxU-jijZu047PgCChcen_rerWYU48cn5PCc-5FfuwmGjjyz-H98jL7zGrwOHKu5liJitmLRjfW_wKiFVIc2dasJbXl-tWp9eRsFvP-W0Y-YB68V4lGMppaIp5zCop30-nn_Q7MHf_EwWddNVlPPpfvU_Ei1AYldYf9RyL2FWHD7AlnMem877Ae-6Vo3W6GqRchGZ5rwzyToZq6F2tLjwo1H_ZdpSR-vHEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPPdTnmFuyzKDgpeU0QPuaZNtUr2hrRfPrVsKpj1EA1cTz3oLmiHZ5qqp8MYJ6iADf_TfO4Zpo_5gyzQDy33hUU4S8VjzAvhpv7ZkJeYVFph_VWLIaz3q1uDGAGeQaWe0m-NoB6wbHEKgH0kOdI3m2s63bIhMt4_Z3VHDWf_CSE5ieaITqrAQvzNVKZE-9m92dgsmTrXQxo74mzNw8RIo9y1EcvaF7ww1BdJZut8JC_pvHe_046lWCeY70cppwHmAvgZfYmNuw2oSIN4yRlia8k-mmlOPn_DVqP7ILw9QTRoxu95s-mOSkhrw_G0E_bewb30pLrqwEK4zkx_CfyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vB4v9qptnBAvo09i1JjpvcBDv97k6hrPrSUpqO6UlpPyOhISI-ZIYo2y_QATdOJXjszlUj6vumur_V6g_2I_TAv9z1rejC2xYMKc5nhGQ6-u5R6yiF3KHXm-q8CMwroCzgRIWOAdbCu1AuVtLbyTSRk9zIc4VTWtzC8aZCGNj8ruw4MY4sdmLMOT6dQaaFmAoOTnF_Pb7XpuhbYTn1i3e9ParaN08opISBPsmtRHbdRkfa6PdgzfpabHhB2yecSLlV03ry4rY22rfO2zDITHVHkpVbqVR6RTQZK4wRjsi_3rnCtOIHsQbY67Ny0x1RkV4vodC6khVNgFoK3AF8eLWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRUFcIL-vxLVbj1jP9uZ5wf3sc3Ldnbok0TwdmyGZT1P4F78qTNSfk3ac1EcVw1-7mpwslK-YsC6iugUD7PrxYgz0eYUTd3V8h-zZYSklX_OsWpeOyaNpVyeg0cJNOLNTzDell_k0xw5I9_WAAwkLQ-PsUJd8q_kiKJ0OYwM1lLm6BQpZK27-Zs-zb85ZKlmtDhWwGZTpvHspDjDXM6UicV9AFdTRiWtYiW4qGZkI0SophH3HQ9S8_rjpv9rxmVnHQlTTdmKT20-Ej-2AxfUPukhDjWeJ3FdVlhlp8o4L2114b92h6UxyzbpPXAsJgzsZrru9Gei1Sgl6F8RPVLADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob1ADXsvepR_5ZmGwnzCKjwfYOy4IZbwkERz3kmkiT9s9DfRgDkiamHpYgzndx2oKdF1X3peRg0w67jyVp4624jT86nyhzCkHuF5GauXW38M4ORqaMVHaM5PLXhc4BinTSi5tD7rgAAAv4BVHFwGfRS9Cyr65fSgQkjkc7iPgmbSiUthKEWXJAGf63OZplwK2BAprAL2tKkIHN8Yg-skVkwQOb074X3zZKTWj2d6Cex3eS__Jv2f28-FBTCQWNwEkOMVbCrbxECtuEFybPydUg8rBxYoPi0O7bzxLcnkMPKzgqM8_VR9i5eYDP_sNPxCsoPHWnRsOtBWZbIx43X_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5X-du5JG8CzWac7OsYXGg2yuSNCa7HB6h5emn6B4Fah-eKdW5_ecwxiVc8qrmtTpmfyWZDWGhvkozd_XmaMUgEYVPUv0gf2SEFxYIJSkWbv3YHE7i5IvAjTL99azE9dqf1Tv2ngD0DN6XmqjyUvgNS8A8ww8DdtcthidJVxcmHLq9BMmH3vrZjAOTsOMa9CheJunrTMNIQOuC5tejkdJJXlwclcaYqzyBlvrMW9c8OlJW2s0QI8m-312dySpkCpK73ztzWDT0A_vVcnRC1Vr50FN5N4sqkSNkuquVD_wn2nAcB89oxHHSKOizrdjDUIE_Jk_ji5P3qRQkUDSgHCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQuyuHTm2zFGxpgz666j8S8kwnxmpi4PZ1pwOWYFT2l1KvLW-_DyZMNlsJell7PtNhocGxSIXS-1OJTe8iV8qxLeKAO_i-uu804sZl1azMfDXX3vrR2rxqsVudJNt-BJmXX-73XrmjhqeQomMUOVr5K4DcHyfaWW7QBZgzd_QokElCcKOkX4GYCWOEGG48alHkpfYhdsXoUgkRHVLyODKSvF6duPhjrM5X7R9IwX_IMLFmlJybUiqJi6owu6nOOPu8CG32UYtobI0kTvCeWoqaVb2GIC-YpIGFR90fmMCR5Gk04QnumvLznbjGzLwpLwWX0qlep8wD2pKQnkxyrRBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=oR2o-NGx1ws8ZK9pK--ptPHpvERnPnGBr0-gBteJI1zkoNihreb6NRwkSZihjqyI5p1DYxPA6Va5ssK3xsalmEoqr6RpNsnPy8Z0BY7gm0LA5EZylwBJAKxvuf8I9i0Cftnwrc99sfriRGcZRyVQ2Cdyp575NfBLBdb7QOowSg-rsKmzaODhJR7pk-q0Ufg3oOwvYGQI2EhY5lZ8q_36EcDu4TjVGRef4Hh3aAbWrNcKJ1bhBboLsIYFeDF8y8zt5pxyj-yotpDDYtVDSzatuKSGT1YySmA_pJWMVx5J-nBL6kk-KGneydpcLfcE5XCYr0atCbBZnD12vra_EPkL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=oR2o-NGx1ws8ZK9pK--ptPHpvERnPnGBr0-gBteJI1zkoNihreb6NRwkSZihjqyI5p1DYxPA6Va5ssK3xsalmEoqr6RpNsnPy8Z0BY7gm0LA5EZylwBJAKxvuf8I9i0Cftnwrc99sfriRGcZRyVQ2Cdyp575NfBLBdb7QOowSg-rsKmzaODhJR7pk-q0Ufg3oOwvYGQI2EhY5lZ8q_36EcDu4TjVGRef4Hh3aAbWrNcKJ1bhBboLsIYFeDF8y8zt5pxyj-yotpDDYtVDSzatuKSGT1YySmA_pJWMVx5J-nBL6kk-KGneydpcLfcE5XCYr0atCbBZnD12vra_EPkL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Gv9SIpHYaxTV8i3KkQP555zdzPn1cdjKGNaljL3jujMwkba2e8TEUm7Hpe3jMcBByQg9ELUUnCUwkdQLVOAmS02X1es08cbvkor4IVFo5FBY08IiPb9nTOg_HFaStIZ0h3vRMgYUbKrxdbSZMSx2rAHJudM25MellUl98AjsSJnguf0oBAWd7Sc8PoX_P3D4kKJYZ0QzC7KsYHpyaiyu4jWrRoL40ylGn_i-7Z7pTRpea8PS1P6U39rkJRNhZGjVYLettVX_PXF5LO-Ks0z44uGt6lhQ1VzlDPONPpYcKel4e5XgVgcDRI2ys9jOf9U6CUlnsbl3p74b0362hJJtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Gv9SIpHYaxTV8i3KkQP555zdzPn1cdjKGNaljL3jujMwkba2e8TEUm7Hpe3jMcBByQg9ELUUnCUwkdQLVOAmS02X1es08cbvkor4IVFo5FBY08IiPb9nTOg_HFaStIZ0h3vRMgYUbKrxdbSZMSx2rAHJudM25MellUl98AjsSJnguf0oBAWd7Sc8PoX_P3D4kKJYZ0QzC7KsYHpyaiyu4jWrRoL40ylGn_i-7Z7pTRpea8PS1P6U39rkJRNhZGjVYLettVX_PXF5LO-Ks0z44uGt6lhQ1VzlDPONPpYcKel4e5XgVgcDRI2ys9jOf9U6CUlnsbl3p74b0362hJJtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=Vz4Q8eDSo0gpcn_u4pSKOK-PFDobwnhl00GZn2eJrDTba9tPfKhKmt9XnPZi2kQh8CAHRFrc_n_Gj5GDYisJpmoBIOHva0Y36RH-IoDncIKavX-XqK5hQ3d7PDJXbvtWBF2IYNiP6H72P7OvSSWSPrIImWq47LIlXkxWGz83xQn8gMhgpkTKpg98DdNsPpu7WXBktpdh6aA2sMJOBwLwOG-tMGh01QhsMyijiSCcJp73C3KPwqRFP3UPDHVMwBMcqn3886TCIe_eoICcijLwt4O7wgCQ_PTWr8SnAbUAhlzsWYclffboDOf2B26ft_bgTcJOA55oX83-2rAzmZ1ulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=Vz4Q8eDSo0gpcn_u4pSKOK-PFDobwnhl00GZn2eJrDTba9tPfKhKmt9XnPZi2kQh8CAHRFrc_n_Gj5GDYisJpmoBIOHva0Y36RH-IoDncIKavX-XqK5hQ3d7PDJXbvtWBF2IYNiP6H72P7OvSSWSPrIImWq47LIlXkxWGz83xQn8gMhgpkTKpg98DdNsPpu7WXBktpdh6aA2sMJOBwLwOG-tMGh01QhsMyijiSCcJp73C3KPwqRFP3UPDHVMwBMcqn3886TCIe_eoICcijLwt4O7wgCQ_PTWr8SnAbUAhlzsWYclffboDOf2B26ft_bgTcJOA55oX83-2rAzmZ1ulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Ff5XBffgNPuZTDuuqBSMF9suubEiFUnJOWu17MQoTB61_JVY_WRKC6gI3rPMLhYNKreYUVknVVQJau7Zzum2gQ650nO61aVAUK2VklI_8hy1kBEYPDpSMAnjbSA-g42xOlO6SofgW5enWa7pxZ0pIsu6TMu--1x3XjXFliTJJu4aEN3TUZvMm5wxx5h2JD_TXpju4h5082CAlSlVd09CM_Tfzpa7PfldKvbsK3WkB401mCcjS5EbnWqGsZGTn0jjIPulv6p9xXKe9oWIdYyKSzLTmqT-azQorSnnEg5FVdXLMtkHxo4xFnZYRTn4-X9PNKL_YkMTPozmVnjSsXI_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Ff5XBffgNPuZTDuuqBSMF9suubEiFUnJOWu17MQoTB61_JVY_WRKC6gI3rPMLhYNKreYUVknVVQJau7Zzum2gQ650nO61aVAUK2VklI_8hy1kBEYPDpSMAnjbSA-g42xOlO6SofgW5enWa7pxZ0pIsu6TMu--1x3XjXFliTJJu4aEN3TUZvMm5wxx5h2JD_TXpju4h5082CAlSlVd09CM_Tfzpa7PfldKvbsK3WkB401mCcjS5EbnWqGsZGTn0jjIPulv6p9xXKe9oWIdYyKSzLTmqT-azQorSnnEg5FVdXLMtkHxo4xFnZYRTn4-X9PNKL_YkMTPozmVnjSsXI_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=SYynAOVU7fPzS1YKGTWDQgPV9n45y3eGusv059KwFHJ0ejujxKruFQZ1QE8HNTQ6qD8aZQFRg9wJLMDm6QqUDRr6prw2OZog5uwCZRbR-YgVAzFBnmS5w_gGi56eKbpHQGq-EWssRe9Rm2CMNUwE7Gm8mjawEWptSzkGk6pB2zOWJz-TYeYYmDgMkJSBNRU2OdxotHq92EYVBPPehRW1xv1iIJ9DuQiHVqcboJVQJCVLXCBWVmWKYRzT60LsxqIkKnWtTpLhacqQoNmM3zjuvIkcqeRDsuO6Pm_jjI-BlMWJLylFN_XGXx67IL12DOvKMKoqvITXlgDuhqSc3TTGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=SYynAOVU7fPzS1YKGTWDQgPV9n45y3eGusv059KwFHJ0ejujxKruFQZ1QE8HNTQ6qD8aZQFRg9wJLMDm6QqUDRr6prw2OZog5uwCZRbR-YgVAzFBnmS5w_gGi56eKbpHQGq-EWssRe9Rm2CMNUwE7Gm8mjawEWptSzkGk6pB2zOWJz-TYeYYmDgMkJSBNRU2OdxotHq92EYVBPPehRW1xv1iIJ9DuQiHVqcboJVQJCVLXCBWVmWKYRzT60LsxqIkKnWtTpLhacqQoNmM3zjuvIkcqeRDsuO6Pm_jjI-BlMWJLylFN_XGXx67IL12DOvKMKoqvITXlgDuhqSc3TTGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=fANySFgyvRuJI6GCFjsVacitk46HpTg373ZXfDTh9bqQ8Rfbon2sBny4PJbGyJKeT-kFS7ua2PgvjW-GbvoY6N8_ZafnVlPQlVhPP9vOzhz_L7AMnRncet8F7Kcn8_Y9HyIYJh21fILr8uFMie4FAlms8av4Z8YONA-9mBGrKBTXHOB-hheLeXmxNlp-7XPCnDC4TO_idgifraIrU7gWVxEmD_eerlCMt_1FGU2CL6lJW9zc-PpUSR2FtMR7sd-2Idje--n6aGuDAdO7aTXSNSPOIQfEVxv4BMGmf02aVLnaU6NOUrRe0k-zX8pFCmiHgFlTF0OVJETl24p4uAm4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=fANySFgyvRuJI6GCFjsVacitk46HpTg373ZXfDTh9bqQ8Rfbon2sBny4PJbGyJKeT-kFS7ua2PgvjW-GbvoY6N8_ZafnVlPQlVhPP9vOzhz_L7AMnRncet8F7Kcn8_Y9HyIYJh21fILr8uFMie4FAlms8av4Z8YONA-9mBGrKBTXHOB-hheLeXmxNlp-7XPCnDC4TO_idgifraIrU7gWVxEmD_eerlCMt_1FGU2CL6lJW9zc-PpUSR2FtMR7sd-2Idje--n6aGuDAdO7aTXSNSPOIQfEVxv4BMGmf02aVLnaU6NOUrRe0k-zX8pFCmiHgFlTF0OVJETl24p4uAm4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
