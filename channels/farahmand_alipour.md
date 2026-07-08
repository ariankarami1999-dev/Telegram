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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRccgvoabv-wGNxNoN2OpDPp9JgmnkW531srP9oI687kUU_RNwZUgc5Y8U35yfLb-YH-6d5N74l_w0Su0fGhXhoDuvdhZO4kYA-jzSaCas80pejAkUanuJ7Ya6gRCXif06sSBH3mrgqbDUAOSyJJHlDvPE6YpJpS467Tgxkc2XGxk7l9t34b7jRQMpSqMANnnlEJNx5_laqWiW7IPEffR-3IVVSxAWG_xJvpjQLwE7aJbhDoriKErOioVDIQYzzbJcfwEpWHiF_NKUUsyUCTxDWypac8Ftm_sGuednOskdFna0XLY8Ko5JYI1spSGs4Z9YWeEL-YHk5_WqCBj3l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKUB2NRc8rxuBLd9M1wY8l5CQIqddrDS9sQT2OanNkos290UvI_9sDKRIFP_NWr4dsZM4KMsYaKvphn8mYNLVWFyDd1JBzyfWPQP7uDJaKtj5_u3L3-x0tDpk-hVMej1mE0B7_2uAtH_aKmUcV1fcvsfggM9INFaSWVaRNTpsbrQ7oRMJ5--HWtT_BBCYsa1X0n8KW71-egQyjujBDctMKlD6mvABSEv82OQ_Nu2_CHJFEbhR_vQeZyRwHmIH2U43ke3zkPkjXO9uJHB8GLYV6RQg3e7m6i2G4BqU0Ftt6aMYx84zw8PGn4QCqqBq9teAFAErmb4XRT-SFbg6nzPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vZ_kVblSneE17pJgfQwXfNlzx3jWmeHWzAan_Fq14Br9YYRI9_MAVIMB8jn8MfMVMHI_FCA_edDKPJWl8pACx8UG1A2Ynu45abKCzxV8AS5Ccif5PXrTU-2kDMMhXqDaOF6h-_KzaLHgAoD9tNTH5wdnMsFYoJcZk7S4MFbOMtU8_mM6pg9GLf4r7dWZPZFtNHNv9W_LlA-uVtRx6beT4scvjui8_dU2kFN531DR1RZ7SAInV8oqrQ_sP-SPOL_V-rzwC6WFFYGdnpL5qsSrCZnehYYI5kui15ZJf7THZWwgM2OpWUIqQbxXH4Ad5Sy6hVIjFkwq3eqZJDYghkOUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vZ_kVblSneE17pJgfQwXfNlzx3jWmeHWzAan_Fq14Br9YYRI9_MAVIMB8jn8MfMVMHI_FCA_edDKPJWl8pACx8UG1A2Ynu45abKCzxV8AS5Ccif5PXrTU-2kDMMhXqDaOF6h-_KzaLHgAoD9tNTH5wdnMsFYoJcZk7S4MFbOMtU8_mM6pg9GLf4r7dWZPZFtNHNv9W_LlA-uVtRx6beT4scvjui8_dU2kFN531DR1RZ7SAInV8oqrQ_sP-SPOL_V-rzwC6WFFYGdnpL5qsSrCZnehYYI5kui15ZJf7THZWwgM2OpWUIqQbxXH4Ad5Sy6hVIjFkwq3eqZJDYghkOUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=NcRuYIR4wg1FciM74v40E4c3RamTRMUOlvSbYjJbKVaJUXBtMoWukB8uNUrTqsUGBByXZ6tEUYfCvHrrh3wBcePU6gCwt4bwQh28AhvsdQrq0gn9unmKzJNN0XXZ42AzXcet7kxB7NpaY2X1o5VqFyim-GTKm07-obdTw7n-vONoCq4di2-TMj2P2oSp4f69V-aGsoy1M7lsp2lL-oqFw1UMrqzYosrQ76GywgP8XddU6_RV84uvM9upoV6pRErODV0I_H0eNkuE8ftuwWAOQgP5Fon6ZW8pSkz0XOLOU52CBUHcIigPLgwGVnsrCjdhP6fE5WfGGSih4TL_3TYr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=NcRuYIR4wg1FciM74v40E4c3RamTRMUOlvSbYjJbKVaJUXBtMoWukB8uNUrTqsUGBByXZ6tEUYfCvHrrh3wBcePU6gCwt4bwQh28AhvsdQrq0gn9unmKzJNN0XXZ42AzXcet7kxB7NpaY2X1o5VqFyim-GTKm07-obdTw7n-vONoCq4di2-TMj2P2oSp4f69V-aGsoy1M7lsp2lL-oqFw1UMrqzYosrQ76GywgP8XddU6_RV84uvM9upoV6pRErODV0I_H0eNkuE8ftuwWAOQgP5Fon6ZW8pSkz0XOLOU52CBUHcIigPLgwGVnsrCjdhP6fE5WfGGSih4TL_3TYr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyiFQ4eoub_RiBxEAp1N2knoVCdpFMThD5QOMP-YjIq_vNRheXl4TmHBW9-DKV90aMFvOletyo-XB7MJHTnFoa6Rf8X4zYjK1sruEibBLhHrK-ecbDJrO0KgRbyYnBpP0pajVIX-tC4wEzbZ1r78ZRwCFNeMTxeAASxyGjxHizh5q0pKkJLfvuSpSN_D6GvtsB9t64mOIZIhfLt4EG0lGXf_92jYHpFK5pPw2EIrvcowzdyWERootXt_V3PfIyWQTZyGqsIYWBTbcgmc3zXyYj82SwdVriw1EpAZyIJYD3SmsSEi_Hm1iEq5RrkBOTXHelr2kFo8qbGmb6b7BwstWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Y5XJNVF-60UU5V9UUgQhd1onfGSsVBDKaFVSR7QB1pXczkdGO4uJNCfOLH8GBKJqeDak-DyjOR9tMg60CvnSkyAZKABc5MBLuyRurexgRsQ9KYHq-32fJvcf4ZZnmpdCHsOEwjArA-GB83SIs5XHCKA-62foVCAY9AArb6dguM3vabFm6hssRoO6Q-9pNGZGWG1RwgBNkZdIIsVVa8sQsnzpeYZtfMQNLINAxUDS3sirHpdQky88_lE7vNpXWK1HXUA3ZSmdWjlslBuU2Af26xrKcCiKy996qzOqDj7GiscO4uhQFwi0qdrIcQNabYI9NKjvphGh1zOi_OsL48uX5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Y5XJNVF-60UU5V9UUgQhd1onfGSsVBDKaFVSR7QB1pXczkdGO4uJNCfOLH8GBKJqeDak-DyjOR9tMg60CvnSkyAZKABc5MBLuyRurexgRsQ9KYHq-32fJvcf4ZZnmpdCHsOEwjArA-GB83SIs5XHCKA-62foVCAY9AArb6dguM3vabFm6hssRoO6Q-9pNGZGWG1RwgBNkZdIIsVVa8sQsnzpeYZtfMQNLINAxUDS3sirHpdQky88_lE7vNpXWK1HXUA3ZSmdWjlslBuU2Af26xrKcCiKy996qzOqDj7GiscO4uhQFwi0qdrIcQNabYI9NKjvphGh1zOi_OsL48uX5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5qVs8ikPoTYWuT0aTDsj2l-BQGMXUj_QI3M2q_xZcLB95S3W1KalRIUQ0NqDBCWav5NF1BCXXZy85U1OsgZ6hDkd3yMRoCVfrS_ih0OdS3p3_Qy8YOgl6sD-PWSya_qodPR1XvVzMsFxslZpLPfiFAbjszYsKjko9qoR6nBcIdVn_djvseeJcnDqg8MLNPV0nAW8fQtE_X8Tl3o5o_rPaaAmb1w0oV9vCO3Q1vTuTcvuss-dI40WVSaAWO_fh9NdHwAceD-VmixRodAwqeKYIEHuU-7iuVP2EsyJk2OSNVe44UuMBNaRGU-wamKZEXw-QwKnwnwhcf4SZtuzdReWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUCMMAr_QgHwZQmzKcWzjj3Fg9Sfbby2ywJ-ER2_crReuN2r24U-PhUS2RbbmodQ5NeadJY-ZgA4ECc2P6EDq_29tBZCUWAuzqO0yrovtYDAB_1d0-gV9AuHw2KiAzKTaputtM75wPtY_k9clF_CRN4jI1kkYKKNgrYvGX5NInDoMSmmYYN3Yb7GPjPtt6DkrZvt2Ln0Mv_D-UomJkD5lahvYlgdq0B1Wz-Ve02J5jfKlwRK3TbFXjY2enkznwPZgacYd0KLWpVHSM8sCAIPvY24MXwBzBBGIJvL7sDGcXDDtNwdiN5qFNcBjG-EWB0COWJ0inUL0zheVC5CJDTEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAk2-5Xt1Y4glpxWHFw24k5X0CLkvKVf7yXkIvzeIWsDcIT4rQJszK0I7gkdEQmrccFHMgeXcFOZCN5oHz9SZpIXacWdCl_JMnHOkMHSGXsEVMCDH2qMdiN_rZOUtw9p1swGpkgRmhZBUFYaZbmROo2nWmINbTnnvgyZHjUGGAQBh2EBcfM_hJARavG0r0j0TfsecDMJovHjEGK0tHVOHmxbk_5KhlP0dT2adKwjEcfMV5lilrfKp1Yuiwy105H1Qtjiy34cZZDNGFjH4IIfDey4arB3CXRyA-8OfSf-4QBJ2foNjAi271CY-uSwjFpSg8ZR0mdvwooLq1hmTaP7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz2jZtijf7QtLJR28-33QVscX7XfZVX41H9IF5df1Cp_O9iSRFyCBAqt7r3q3Z02DueOQs_Px-WDhwbmQ3YTDmqrmP_C54jKPaL44g-Mg-hEOwcw2iLn99DyjzKyBs-G3_4FaQfMWb_QSU5B8f4WfZYQpPVdvKTyFb4bbsWt048Q85fU4MRT0HeYVx73ITy2mi5cW87U8TfDPv_Y4ZMpX7iyf-n_1uQqZKKCSdWM8oy13x1DN_SL_o2298_qJnuDmDZb2hKeqXCVuBUyKA-Rw_8uBW5jyhc3I-Zu3ZXINoR8Fi82U6fjdojjKH5pqXsBGa8tOVV8eH7UEeLC43vAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAUImggxIBQHZrp8-LIq4MwUSLqArbIfAeveWpqKRW77WiO_BaEImgSgVFmg5bkwJPDyKSQNFnsmWBbsXPAl4jQYgbE_AZntWxS6JaWrc0FYPEPogEJ_k5kFevMNg2TIsrxj2Ffvk7UmBQMhBeIGDW9Kqf74Gv5AnLA6eEXV5tdLj87bda2J_jguNwNgSqsU_KxnLA4WkKmKVis_jHX9SOPIwYLHnPpu6CBKX-_Y3ZVVqxyNJNnPtCon6Qxg1LYGOlPlnmxtc9c7-f04bkBqJC1aI5w9VSFoZW7jA2TeraW1z-xGwVhbOfGcUHYvKAdAFEWB1mALVO2qxBfXJUzOEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ZVPMB_dFOz-CLe5zxtqT2KSOq8B_EqFltq5BLQ5vyT_z3Q-aRRA3Y5dWjcX-7goCuGcjKrcCtH59-R-f6GrIFUJwPlC2BrzWKL1xe79JvKeIJvCjvBmEGADRYDkloiVCLEd1bjOH0wkafOwmWy8EGNu3_5Tx1C8s29RrpXiHUQ9D7ybEwF6BgnfVj2ODbLCdJ5vJbXK0nfUvZMnUmlEPlnrBPVlrxA-XDDnAVTKJXnCJZK9QE9MGfJU6OagZAc6hRwgk45VNmZXua2LxjCh7qtLM2BWPSNcbE7zNAqLqX8FrJ5XcYrrJCE9K4LMXI28437DFLkR28qQ9hXb9BFGtUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ZVPMB_dFOz-CLe5zxtqT2KSOq8B_EqFltq5BLQ5vyT_z3Q-aRRA3Y5dWjcX-7goCuGcjKrcCtH59-R-f6GrIFUJwPlC2BrzWKL1xe79JvKeIJvCjvBmEGADRYDkloiVCLEd1bjOH0wkafOwmWy8EGNu3_5Tx1C8s29RrpXiHUQ9D7ybEwF6BgnfVj2ODbLCdJ5vJbXK0nfUvZMnUmlEPlnrBPVlrxA-XDDnAVTKJXnCJZK9QE9MGfJU6OagZAc6hRwgk45VNmZXua2LxjCh7qtLM2BWPSNcbE7zNAqLqX8FrJ5XcYrrJCE9K4LMXI28437DFLkR28qQ9hXb9BFGtUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=pg9HQNxS0tXE-mLeKU82X5-L5ZjVahHNfb5IVZZeTBJG64gnVv-3ZP5kBBtYXAeRFIt_VeWUbcfSwhhEXxQG7FRJsa9CGwM6cFKLSNfl0CM6rdn42ZcqHzUUc2D9huxsqslFhjI1GIQxxRtsfTH7fmw2EiAUk1KlXwJlN1fHfOQKiqkbGUaLPwQFg4nF8g2aBZsCid6NllISuEk88G54AR7iwOIfYhblxe9n5OcFOGKAsECJMMYYJFZ7X7Bc56uRMvunmUQyNGF-AlXHBn5JJpx0iSfPj355rAgGiiPfhVqmSDAXjr56Zoyt-cyR8HXJZEiXJCZtptHhVjutfYpNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=pg9HQNxS0tXE-mLeKU82X5-L5ZjVahHNfb5IVZZeTBJG64gnVv-3ZP5kBBtYXAeRFIt_VeWUbcfSwhhEXxQG7FRJsa9CGwM6cFKLSNfl0CM6rdn42ZcqHzUUc2D9huxsqslFhjI1GIQxxRtsfTH7fmw2EiAUk1KlXwJlN1fHfOQKiqkbGUaLPwQFg4nF8g2aBZsCid6NllISuEk88G54AR7iwOIfYhblxe9n5OcFOGKAsECJMMYYJFZ7X7Bc56uRMvunmUQyNGF-AlXHBn5JJpx0iSfPj355rAgGiiPfhVqmSDAXjr56Zoyt-cyR8HXJZEiXJCZtptHhVjutfYpNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=WFROWb2sYz6OKRTlo0CREw2RBi7jSJ49mz2ADTtxpKUqaP1tkMIcuFrWaHftYkNOgxMV-ywyB4tEMF2Y0hUVzBnZAZgmrAimziqGsqXF1Vl9rvvHq8AEQU5hD3U4PwemadBTu7jmglhSEWnA1HtcQu5-skeRNzp1Ss7B5Xl_Ef95fEGq5oTJcQ-0oIZkkxgblns0hMvgi_lpjS_8xZwfaLwTw-EihJv4liTDBd9KGAK6Oq7TvEODkOH_rD_UOrnOEIc6eleSkns_FG5WPmCTumU9iRl69hw-3pparM3Qqm_VkioWMlB2lS47cDAQoGrZrj5YoMc7VMTA4wtRf8M6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=WFROWb2sYz6OKRTlo0CREw2RBi7jSJ49mz2ADTtxpKUqaP1tkMIcuFrWaHftYkNOgxMV-ywyB4tEMF2Y0hUVzBnZAZgmrAimziqGsqXF1Vl9rvvHq8AEQU5hD3U4PwemadBTu7jmglhSEWnA1HtcQu5-skeRNzp1Ss7B5Xl_Ef95fEGq5oTJcQ-0oIZkkxgblns0hMvgi_lpjS_8xZwfaLwTw-EihJv4liTDBd9KGAK6Oq7TvEODkOH_rD_UOrnOEIc6eleSkns_FG5WPmCTumU9iRl69hw-3pparM3Qqm_VkioWMlB2lS47cDAQoGrZrj5YoMc7VMTA4wtRf8M6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=ghs_lmKdK5WkPzcWo9Y-vrHRneJgHpSDATJa0xbFTZ3WDs7PHA6pnRZOJJPynBnLfOHI5QLn0rp-Yr0onjHa23T4Se16HK6GTUH_2qS6ANUqD2paLIYPa5UQ39iOXkAxO_XTkMXJjfa-NnMsWgznnZmAZ4CDm-w_eP22oFMmkZEAuiQBAcIiOT2-JOtWQTxkOG7D46_b66woX6RF7mLv3lCj06NWbqtm8tSlaRNRyTnzem-GlkfSiM_lHs3eIJq6HRQEvT7pMzdU-7YjT280Z2XgOUt1GWG9mnyqGGiQB9Vm5y7WEjNWv1NncEjcwBa2qatkLnt8MQ_1vu4YiP8vVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=ghs_lmKdK5WkPzcWo9Y-vrHRneJgHpSDATJa0xbFTZ3WDs7PHA6pnRZOJJPynBnLfOHI5QLn0rp-Yr0onjHa23T4Se16HK6GTUH_2qS6ANUqD2paLIYPa5UQ39iOXkAxO_XTkMXJjfa-NnMsWgznnZmAZ4CDm-w_eP22oFMmkZEAuiQBAcIiOT2-JOtWQTxkOG7D46_b66woX6RF7mLv3lCj06NWbqtm8tSlaRNRyTnzem-GlkfSiM_lHs3eIJq6HRQEvT7pMzdU-7YjT280Z2XgOUt1GWG9mnyqGGiQB9Vm5y7WEjNWv1NncEjcwBa2qatkLnt8MQ_1vu4YiP8vVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpLfWVnTpSJXt5PIvEuFav-lgxntSGybLVFHs_T6bmX4yGwxEmbiil98TQmOp6Vavjl1CAeiklWWk7Gxh94WHpQQj_U6TFdGDHeunlNQ_-M8qESeejRqB_CFqdR7PNfcvQ-OUFkzsfcRdcxBe_gf3_P09yKy9mYWJjpz3OlMx8n2mmonDOJGJz0iNememDyVpSmiNA_7AWurDDuozFuvRRxbKQ9aJ6_PD6KL-E91K16CP1OWiSsop9M95Qg0ho5LGWcG04cYngyJeO-03moGjIPKQ7SbTObyK72WwIoXRnIrNVeGOo2Wz1iuFG-x-zUwnBV0h6Yk-RHCdAHsKWvsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=DWIGf1uwcsbGmlfv3VPqvvnPO3AlBGpTcsbL--3zay72iUdEev-9eSdr-mlLkr2I91EIr1uLlu1_6c53zsHFrvHXyjiOwiQ2_LBQq20szgiviT3rbwq2IzGuNLNEZiYBq0VpLAdf6FWJcQ-BRUjvvbGTeMPoDtcC7-k6smK6vAtYHDoMmjqJVXxHxCT2XbjMyBYUCFZwzJU2Me4euIpSCGhXUs8jfeinf6yjrhAutUKbv8Ps5zCvlwDjUs_tcM_bgI3BygLbe90OIK51vB7KnFViMKQ3HRcWj9Fg2fRRmtPvBGRCD3BMtxBAuIkiMq1kugHCUrDSG9vcNy29Kq4UWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=DWIGf1uwcsbGmlfv3VPqvvnPO3AlBGpTcsbL--3zay72iUdEev-9eSdr-mlLkr2I91EIr1uLlu1_6c53zsHFrvHXyjiOwiQ2_LBQq20szgiviT3rbwq2IzGuNLNEZiYBq0VpLAdf6FWJcQ-BRUjvvbGTeMPoDtcC7-k6smK6vAtYHDoMmjqJVXxHxCT2XbjMyBYUCFZwzJU2Me4euIpSCGhXUs8jfeinf6yjrhAutUKbv8Ps5zCvlwDjUs_tcM_bgI3BygLbe90OIK51vB7KnFViMKQ3HRcWj9Fg2fRRmtPvBGRCD3BMtxBAuIkiMq1kugHCUrDSG9vcNy29Kq4UWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZRxjO5-duKCUOfvlFP2AlcqBN-t_wTQu6zeHLCDeXiTDhDstg1EendbSinUsPBXQglyX0Kh6Rqv_hvMpNQcBqPqRwM-MUdmZ9feOhEsJ575HpwHT5s6E3kJhzekkEO2avi6e5kejhsl8DplNPg90yVhwqJLlE29OL_IuD-0PN2kuXkGAjNq-kHmCyIW7RqJKuvhY_IUD3c307CSFsK6FXekEe_OIfeTJoVkv5ObkJnjFUL68v1V-0anspFIr8rQU_f46WEBmu-KRHnJuFnvupl55gGWnAW0PpoHa70sIYZIaPQfoQ1vITFFFeiS9HZDze59OFUB6JDwbCxfh205uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=lvhUZNz4eeeAf8cDHjrH4qLX14rY4ib4KmtPnKgs-CCuI0C8VI9HH_Wtc7gSh1iJ5lVYwuqJ6PYfUYjks1rDQeCsIB-mJS-OG5vhQrbkDY5yplLm4bYsPdpQR003ep2itP5UVnbY8vqd0uqcV4moqyIrVi8yNDBuRo10p6vnS1v2ItGcTBk074CCjcUqkBX9LYWpoXkbRSOgUNKi--OEKljLkslGo6JkOmeirmcNmQvrB-6Nn5m_fO-H8FNfSPLWM0j-ZnVpmD-8qSAYzqEiEInIt3gb4SFPsh-G5r2Azc0BddO58gwp_PPPDIHxNGnPRD6usxshTSpJaAS1qr-BLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=lvhUZNz4eeeAf8cDHjrH4qLX14rY4ib4KmtPnKgs-CCuI0C8VI9HH_Wtc7gSh1iJ5lVYwuqJ6PYfUYjks1rDQeCsIB-mJS-OG5vhQrbkDY5yplLm4bYsPdpQR003ep2itP5UVnbY8vqd0uqcV4moqyIrVi8yNDBuRo10p6vnS1v2ItGcTBk074CCjcUqkBX9LYWpoXkbRSOgUNKi--OEKljLkslGo6JkOmeirmcNmQvrB-6Nn5m_fO-H8FNfSPLWM0j-ZnVpmD-8qSAYzqEiEInIt3gb4SFPsh-G5r2Azc0BddO58gwp_PPPDIHxNGnPRD6usxshTSpJaAS1qr-BLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=ZFOIo170--xrWaIAE6seiRVQsB8E1Iws8Qm2UdpUXAB4NMNtHcemJvDxZ_zvIJP5dAeL9YJ-6oDwqotrV-b9rLUkoxnd2-XAFIeFucPiMi9SO-fUnz-iJY5MDVnhymU16aOLCvo_x0lh8WVuhBCI1opEnl17YAF1MBGZCU6zTXFOOlORB9ihzQgNHDnawM3cqW0wRJDoYgjdCQRwke8QidHRimJQ-rfznVjXvCTXRnpX9JhW3CKvRNKyUCUlqZF6jpgEg-3atofzuFCN_ennWJkhWkMGaN_HIUYjXgoqQgCp4tIybuMbq9qGx8eIexrErSoYfj-ZnidTGhY3D6RoTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=ZFOIo170--xrWaIAE6seiRVQsB8E1Iws8Qm2UdpUXAB4NMNtHcemJvDxZ_zvIJP5dAeL9YJ-6oDwqotrV-b9rLUkoxnd2-XAFIeFucPiMi9SO-fUnz-iJY5MDVnhymU16aOLCvo_x0lh8WVuhBCI1opEnl17YAF1MBGZCU6zTXFOOlORB9ihzQgNHDnawM3cqW0wRJDoYgjdCQRwke8QidHRimJQ-rfznVjXvCTXRnpX9JhW3CKvRNKyUCUlqZF6jpgEg-3atofzuFCN_ennWJkhWkMGaN_HIUYjXgoqQgCp4tIybuMbq9qGx8eIexrErSoYfj-ZnidTGhY3D6RoTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=RqFCw31O8Ume5KEdTwqqJcwpZ-BMWxBTYeopnoqoeD7igDiHFo7hbwXYFbqMu_3csO_tHFqvrQ1QyFj_Fuj-Y-A4gc4S1icCr9OeOaiunM1uW2n3-6fO07XleOWC5VUJ3iEA9gs-uL51VhadodY3Fi6MUgOKaO5k_cj110GAxzKxdYN2bF28guJys_OXwGO5ivjeCqnVvww8YrpWI9rYoTpgw86QUGwp5te1KClUlm54Q6buAMPnztezmqPhglHtImNQ2Grfqms3QF90JOVGXELSUAskYC_GTE1ffHHux43JTJQdB_tdSbQt1eRxmSAtc95KNsaJ8zxPG0hh98xONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=RqFCw31O8Ume5KEdTwqqJcwpZ-BMWxBTYeopnoqoeD7igDiHFo7hbwXYFbqMu_3csO_tHFqvrQ1QyFj_Fuj-Y-A4gc4S1icCr9OeOaiunM1uW2n3-6fO07XleOWC5VUJ3iEA9gs-uL51VhadodY3Fi6MUgOKaO5k_cj110GAxzKxdYN2bF28guJys_OXwGO5ivjeCqnVvww8YrpWI9rYoTpgw86QUGwp5te1KClUlm54Q6buAMPnztezmqPhglHtImNQ2Grfqms3QF90JOVGXELSUAskYC_GTE1ffHHux43JTJQdB_tdSbQt1eRxmSAtc95KNsaJ8zxPG0hh98xONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=ZEkeMNRvE9czaFuW9z__VehzyqxPwG3VYoG9t18MdSo5eqoRksvW1T_EHrKaxw5WC93uCKiElMFsfm4Wom8ZOhw5OdK5gDIHb-uA0ibF34eWxMEnf_VK2OgozdvnltV8z4PEUI6cRn2Q0QrKQvi80cM2fyZGYPIxX06439q37X6KE9YVGPCiEnrf3M_O5cL34vcpnAZR1VtSX1SaAjzZLzX_jHBHlqdFG3e0DVcbojqNEcxgjDbwYJldqn3pyAFK0uaNaMxlAKQfXD2mciTVVGt9sr_Ncms8J5uzut2frroU5UFgI4BHqx63vW27jO3guZEsenI88B_WO1_tpUWymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=ZEkeMNRvE9czaFuW9z__VehzyqxPwG3VYoG9t18MdSo5eqoRksvW1T_EHrKaxw5WC93uCKiElMFsfm4Wom8ZOhw5OdK5gDIHb-uA0ibF34eWxMEnf_VK2OgozdvnltV8z4PEUI6cRn2Q0QrKQvi80cM2fyZGYPIxX06439q37X6KE9YVGPCiEnrf3M_O5cL34vcpnAZR1VtSX1SaAjzZLzX_jHBHlqdFG3e0DVcbojqNEcxgjDbwYJldqn3pyAFK0uaNaMxlAKQfXD2mciTVVGt9sr_Ncms8J5uzut2frroU5UFgI4BHqx63vW27jO3guZEsenI88B_WO1_tpUWymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=LG8D9855Z9Wmw_nm3yiuLG-LFT5d-2f5l2LDs5zXNmhX4uKzOGOGnqVELHz_L_tW7gSrIu5BmlNT5Jt9y8CIbKfJ_EfKR-KGPs3FBeh50_Zr-nk4gis5FmTAnXJoGhOQ1qb-gQqSaY2LPc-STv1PjMZ_faSUCrPGEn7AeVjHg7ZdHyy18AhCC2FyXEVxuF68gTiLda1fq_RtMMMip5D4JbPqIfHQJ4x1iJWJRGommzUxpdaWQfafZtWU7uw0yfwFFDiWGzrv57lUysaXCVmc9M97CG_sEG6Cv8EU9uJu3q2mTXYQd9UB3BeG-Ei64OfBTc_-fG9_fFyvDEUWrW7faQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=LG8D9855Z9Wmw_nm3yiuLG-LFT5d-2f5l2LDs5zXNmhX4uKzOGOGnqVELHz_L_tW7gSrIu5BmlNT5Jt9y8CIbKfJ_EfKR-KGPs3FBeh50_Zr-nk4gis5FmTAnXJoGhOQ1qb-gQqSaY2LPc-STv1PjMZ_faSUCrPGEn7AeVjHg7ZdHyy18AhCC2FyXEVxuF68gTiLda1fq_RtMMMip5D4JbPqIfHQJ4x1iJWJRGommzUxpdaWQfafZtWU7uw0yfwFFDiWGzrv57lUysaXCVmc9M97CG_sEG6Cv8EU9uJu3q2mTXYQd9UB3BeG-Ei64OfBTc_-fG9_fFyvDEUWrW7faQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=vUNfMx5RsIpDxo_Fd0UcpoBwWjUWESq1_R2foQAvmZxmBoNItCH9q6qO3GZq2RE_PW4-YuEA9xvFqdkw4ddU60M8SW-hBG22EuFOmexOWh_O7xt2Of46su0KmEme5HgLrhT1FMHjuvl7BUFsnTPhk0LlJOZ9D1OR8AFPV-EfG-CbYmqsZ4VnXjXd0VgaOhmCzMUN8p6cd_5rc4upUhJ5yMJk2wlkBDfr0_9mFO-HKVTSBB7oFovY9UGJ5tbMfmYx6I6Wx0_UUOm1aBB1j04e14Nutmz5eB75uAU3syOW2_ZGvP3yyI2SGWJPr3Ns7QgvHu1G1W2WYS7O4djkfWL4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=vUNfMx5RsIpDxo_Fd0UcpoBwWjUWESq1_R2foQAvmZxmBoNItCH9q6qO3GZq2RE_PW4-YuEA9xvFqdkw4ddU60M8SW-hBG22EuFOmexOWh_O7xt2Of46su0KmEme5HgLrhT1FMHjuvl7BUFsnTPhk0LlJOZ9D1OR8AFPV-EfG-CbYmqsZ4VnXjXd0VgaOhmCzMUN8p6cd_5rc4upUhJ5yMJk2wlkBDfr0_9mFO-HKVTSBB7oFovY9UGJ5tbMfmYx6I6Wx0_UUOm1aBB1j04e14Nutmz5eB75uAU3syOW2_ZGvP3yyI2SGWJPr3Ns7QgvHu1G1W2WYS7O4djkfWL4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=iRMmgDZAwhpa7TnaRKDWLighgdabgU-Eq1GNKimu81XeNn8DkNJuJ4z8NeNpEJP-M40o_HGekoIGcKLvXRxiBLe2r9SYa-dHZej2zjFDEohH3MI4EEoPlokJ3UlsS3rOdh3einMDcXa-8ojKeqDriHpqbrVUPY_B50sNeFIhCyinxkuzo4wrBFMnIIDuvHclXJ1dheorZJ6mMUFe7SLmORlhOVNTaNFKxMoF98KvPbnWCY2zOCCaYKENROD7vuhfIpD-As7H0gdsm-o-fc4xcpjfvYV_sQMTTCc16lPQmsIIu2s06CgJzO4OxbEjnPk0Uxe49qVod5rG4ry8g4EbMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=iRMmgDZAwhpa7TnaRKDWLighgdabgU-Eq1GNKimu81XeNn8DkNJuJ4z8NeNpEJP-M40o_HGekoIGcKLvXRxiBLe2r9SYa-dHZej2zjFDEohH3MI4EEoPlokJ3UlsS3rOdh3einMDcXa-8ojKeqDriHpqbrVUPY_B50sNeFIhCyinxkuzo4wrBFMnIIDuvHclXJ1dheorZJ6mMUFe7SLmORlhOVNTaNFKxMoF98KvPbnWCY2zOCCaYKENROD7vuhfIpD-As7H0gdsm-o-fc4xcpjfvYV_sQMTTCc16lPQmsIIu2s06CgJzO4OxbEjnPk0Uxe49qVod5rG4ry8g4EbMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJvSJzOVYV1ToKCqsCWyO3aUfWf-wnPJzZ28jWBtdrzeayXvi-aMY1PndJCcWpVij3-K2Sx-zFEkOl7JncbQ3zo7dMICHekauuvuEHNtDWphP9hmNlhSPxaBEJYs9TlubkIP5DZBU2ngQWhm-P0HSrBl6oURb0hLjDeZosPUaj7LzL5NyR1H-WJPy6naXxE8nHxtVBW6xIbXa4tGMuT9s1KIS9PF0dHueRS0AAnnC1S3YRi12XGhPEEXWuzWp-hzNMfV_sp6GqY1X63rQ2hN7wyYOozmrnHer7NxwYgZPl8v-VDR9gPXbA6twba7Hqsp3dv21h1EqEJgIHe2vLmXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVeINsJig3AkIvYuAwM73sLH16untwbwpAs4por421xCT130D9huYUTf8NSVuG9yoJMQxAZk7FAjuEzze0zoFfnGTXLyk-u6W9urK94vo1KKf5-TMAyeOjvUzS2UzwcGeeF7bc7Q3sNMaGkFre4ksYdC22Gnit2xBjBlegZwLJfggdfzyFkD6mY5gdfO4r5LdFu8ybhaX2XRg1fKzTqGxKEo5IkafDjG7c7cASf2-Q-2gqXtQeGe1LDBgDEw8N_S-C2HDwhof5bcD2U_UlWcgVAiVdBdf6R2_7FF4Gy00YM_TAewXbU-R2mbODH3Kr3dALB8Gjf2tnq5t8sc9zKPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Errp_0tIkucsOXj0Rk3Tu_jQrE9VxX8jxtDFWhJNfyrqYhHop0kBdFitgbCn1h7DJ_G5RzrOxSGfIxeUc_MDOIy5e7WSsDpkjBlLarhIyYBBrdnbOjpJ9NWFP8sa6RjW79GeC7pLQLAfvCtz6z4zC_YgnumeI15KocnF1-cvjXxH5I07RdxA3qrQ8pFut3b0r69YVgiydPBzQbcJNjSJcEzjoxYv9nFbbsqdp0mrk-XZ-o6KeB-u4cPG0pZn71Zacg9DOBGB3aNGXkRyJufmxAQQpSlVg8I1AJhrCnkq6heydKwm4PIEV9jlZvb7xZ85KIy5j-xmWcup2XaUcsZ4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Errp_0tIkucsOXj0Rk3Tu_jQrE9VxX8jxtDFWhJNfyrqYhHop0kBdFitgbCn1h7DJ_G5RzrOxSGfIxeUc_MDOIy5e7WSsDpkjBlLarhIyYBBrdnbOjpJ9NWFP8sa6RjW79GeC7pLQLAfvCtz6z4zC_YgnumeI15KocnF1-cvjXxH5I07RdxA3qrQ8pFut3b0r69YVgiydPBzQbcJNjSJcEzjoxYv9nFbbsqdp0mrk-XZ-o6KeB-u4cPG0pZn71Zacg9DOBGB3aNGXkRyJufmxAQQpSlVg8I1AJhrCnkq6heydKwm4PIEV9jlZvb7xZ85KIy5j-xmWcup2XaUcsZ4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz73R-bh5c9JFy0cpgnosq4VLbXSKAvUnfVb4v2U6DTpK3jvIZakt0pDcmLdkO8wJ9Kr5j3RzFEYlRY92i6qcU9PwYY_8jHdnw-jqENTG6qQThvlOsRgfqYN0g2eliV8cSL3jFriWJTY8CvpFJCshqH9LYLhSmvXATQIj_JsLLr72TIVsH1-19Tl8W6ysviPHscTO7qStyVKCPPRAg0oJWZ9wVwn78YkQU13bqG3KMGd6KXV7Lyvf2P8xrSov3CtDPpTkYQFBO5IyF4VN1wMy2z1Ze7qiZss6v6_hFwIF_8R9dyYfFuzJS2P8QCMYMsjgxsxxlT3zMGlFYBj7mf_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=WkrYlOAr4s5CV21Eji9wtvOBLrqX6ks9ZErkQxsmhQDNqeYw8KeN5PZiacCBplcWlMDlxrS14sNwmEVP58KSJPADf_IuOqCV-8G_FSRwHfOsefobdL1NCBniqjnKR2rW-grFCgBA4DInrIJCRl0cv5X0Rg_11z-Ytcf9JNMk--CKVnZICa35fbvuM-yxg22DF4jVB6U6wcw6Ew57RQdi7RcWGX6du-rwbbUuvL06DTwJ0Kx2QdSX7J04QrVbmjHTADg7IswHVQ0xgKTlCHIaSJ1EfqwzH4Udy11PJ1V0LJ3rQP1Vp2oiR-sOYW9GGYaRy1cpdimwhYUtel8kk-0ikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=WkrYlOAr4s5CV21Eji9wtvOBLrqX6ks9ZErkQxsmhQDNqeYw8KeN5PZiacCBplcWlMDlxrS14sNwmEVP58KSJPADf_IuOqCV-8G_FSRwHfOsefobdL1NCBniqjnKR2rW-grFCgBA4DInrIJCRl0cv5X0Rg_11z-Ytcf9JNMk--CKVnZICa35fbvuM-yxg22DF4jVB6U6wcw6Ew57RQdi7RcWGX6du-rwbbUuvL06DTwJ0Kx2QdSX7J04QrVbmjHTADg7IswHVQ0xgKTlCHIaSJ1EfqwzH4Udy11PJ1V0LJ3rQP1Vp2oiR-sOYW9GGYaRy1cpdimwhYUtel8kk-0ikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=p_vgr0QY2-ahkSXViT8Ah_O8FH-VseuuFF9JQrXk2Pwh-4HGsUUqa-heNaFcVBsAqlqbpOABG2EtwibHqETviTk1qM10fngiienNhVp5pBl8lIIEIGEObX6RsSu3DIb1KY_UBqqrtWHkS7ONCY9COt6Biz38ZpBwjqEtxliY8mRjufZmDrdCv5NLXE4RclVbM8aADR49yvTbreiDjVej_dCFBiDw_t4aL6Ok3IeDmcM7MDEZuOORMRHhN69zL7zDgJzBur0aVNKp4WFwNoMtWUf8Yj2fd-WCagn0EDAb5EJO401UNHmrlUyfngqcNoYz7RVdKXfqIQ1Xv0deW-MsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=p_vgr0QY2-ahkSXViT8Ah_O8FH-VseuuFF9JQrXk2Pwh-4HGsUUqa-heNaFcVBsAqlqbpOABG2EtwibHqETviTk1qM10fngiienNhVp5pBl8lIIEIGEObX6RsSu3DIb1KY_UBqqrtWHkS7ONCY9COt6Biz38ZpBwjqEtxliY8mRjufZmDrdCv5NLXE4RclVbM8aADR49yvTbreiDjVej_dCFBiDw_t4aL6Ok3IeDmcM7MDEZuOORMRHhN69zL7zDgJzBur0aVNKp4WFwNoMtWUf8Yj2fd-WCagn0EDAb5EJO401UNHmrlUyfngqcNoYz7RVdKXfqIQ1Xv0deW-MsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=eXvH4XQhV7X7um1znChdQnBdq6IdQ56tfISaYlWk3C5ufoj7cBE1MuAOknxNn3KhwFp7hWSV3cYKcgOcHKghiWNZN2Um_3rs6wflY25lscfaj0Do4nNMGYG32jhQgu4J0umjKOUa3kgumBdHcWaSGMIbsQpvLH6_e1v5b_2DEiJkCxfwI-kSFOt-4wqrqvfoo_m1OC6svyToiy_aexmirg0IIfdczweDGQdXD6SuIyyL4zPzn0y1Cuy5eVDyeAwM04SbnyyP8NvWvKqIsjUzbOX5CMmmLf-0dFHAKiydaNmt3oFaFSyKqiMmb5OiD7tTW6H4ipsY0dSscFBL7cYKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=eXvH4XQhV7X7um1znChdQnBdq6IdQ56tfISaYlWk3C5ufoj7cBE1MuAOknxNn3KhwFp7hWSV3cYKcgOcHKghiWNZN2Um_3rs6wflY25lscfaj0Do4nNMGYG32jhQgu4J0umjKOUa3kgumBdHcWaSGMIbsQpvLH6_e1v5b_2DEiJkCxfwI-kSFOt-4wqrqvfoo_m1OC6svyToiy_aexmirg0IIfdczweDGQdXD6SuIyyL4zPzn0y1Cuy5eVDyeAwM04SbnyyP8NvWvKqIsjUzbOX5CMmmLf-0dFHAKiydaNmt3oFaFSyKqiMmb5OiD7tTW6H4ipsY0dSscFBL7cYKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1E0UI91EgpVA12L_ExV1h5158nA7giwfFyWgVIimU10XDZh1a_jC9gNG0NqiVVEIGgh80ktruu03hxpMSDl4BlALAyAAlFBRh2iSzdgfnGZuDzlblfO53YnGIuql-5I5DcWB_4gWcxM-UEtbS3cSemEyyTzApSkZu918EwUqkFt8i3ohT83UReOeN_pT3J073dBAinHb2o5oqk4-aFVt6h3zmsx2xn18LAB_fIrDbnTZhv3oGsuhWvumUS_-LfrdLG4A5db99UzwjfDojUmMG_betJiAWi04ROsm5DNsmV_O5hCeBBrOVUczTPohxi1uGAOzn1N-OR7L7eQrPm1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCCNT2FgFQ3z8UNaNNOMrO3ltpakO8ko69a_pP8YEcKwPoaT19bVsI0E4FM8cMGSd1e3v6hIJhfx7uP27ujj5Bh2Xjv90QaWkY8hoAlh7WvaAx6tCM9VVEZuHCnAUCJQ0inB_ut310HEmcS-RsLnyE9fpBpkGbXp0tNahPNA_PoTRCcQQaf-_fLMMGfc8A3qAWfiWR48eZFtvEW5carhOfoYUa9zSnXZVAxb9ZH4sgKx9QWi20IhlFo6u6bGLse2KFSOrAtDk4FcYIDINaRGzB8hVzTkihnLfxlEWi92-GJ_hIOMVEEDha6BL1Q04R2gMpHBkTJz8Ednth2HUFbLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=dC8TX9vBVME-rkLtk8-L-OmpvhdF4QF8rDUrwJeIaIYM1G9uxQoL8BL-pdd5SRaq3Sva0E_QcbL_gl3WvPmj3I47E9Zw1vcwywiYwvm0im3_TVAN6A9LWBl6pgVizrVydhDmExqkaausK5B65v7ESLLDe6OxtR4l6DalOUFfiG9vVAgtPNsPfknREBeoDtTd4RT4VMV4VApad7j--2Sy_5BDj5CKI63LQn_wkxwmnvsxrrw30Fus_pTcEqWLuPN1E25CSr2c6OKyDEDJ7vo4U4uTdpVwAc-WdfHusBIyGx1PtbGSvahevdsE-cBoeBcyOfsBYFpGRcnnmImRX4XIKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=dC8TX9vBVME-rkLtk8-L-OmpvhdF4QF8rDUrwJeIaIYM1G9uxQoL8BL-pdd5SRaq3Sva0E_QcbL_gl3WvPmj3I47E9Zw1vcwywiYwvm0im3_TVAN6A9LWBl6pgVizrVydhDmExqkaausK5B65v7ESLLDe6OxtR4l6DalOUFfiG9vVAgtPNsPfknREBeoDtTd4RT4VMV4VApad7j--2Sy_5BDj5CKI63LQn_wkxwmnvsxrrw30Fus_pTcEqWLuPN1E25CSr2c6OKyDEDJ7vo4U4uTdpVwAc-WdfHusBIyGx1PtbGSvahevdsE-cBoeBcyOfsBYFpGRcnnmImRX4XIKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=syLJ8LVdnJabrvVriLLwJCnLDKb__s8y4MH2S9HT8BLlBOraXWVrAYDHFsleDheEeWSVQUKzwjcu28CJrKGvfpydpPXMn8EOAuvKIeHFBWqPQaS7y_TH1eqZ_VOnNgKWUMyPdCf6w0BT-oQ-bXNvSAOHgz9DI8S4oGx0DNK-DB27lzFPvXaD9n4lSuxk89BOem1nAfzDlBj18wdEri7OvlaiqkAlwCqvCn7DeAWQv1Dr9sY7tk9VD9sn-wth48kDuSAVyNMp7Asu2R_nOjQRSmHu5QPsaQwxL8enCIg42jI13v2BPUJ-a_Q0XePTABcVZJbUyIIrsIFD7s0rcIXl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=syLJ8LVdnJabrvVriLLwJCnLDKb__s8y4MH2S9HT8BLlBOraXWVrAYDHFsleDheEeWSVQUKzwjcu28CJrKGvfpydpPXMn8EOAuvKIeHFBWqPQaS7y_TH1eqZ_VOnNgKWUMyPdCf6w0BT-oQ-bXNvSAOHgz9DI8S4oGx0DNK-DB27lzFPvXaD9n4lSuxk89BOem1nAfzDlBj18wdEri7OvlaiqkAlwCqvCn7DeAWQv1Dr9sY7tk9VD9sn-wth48kDuSAVyNMp7Asu2R_nOjQRSmHu5QPsaQwxL8enCIg42jI13v2BPUJ-a_Q0XePTABcVZJbUyIIrsIFD7s0rcIXl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtihwP2b_2OyYhlk2WkwfnLJNn_kj3Lr-g8n9Jt4NFg_eoverKm0Qm8PPA0AldH1cg-OVv236ddNFFhGLPxEQXQ6504xedz4EkYmFStUwK1abbLMbJeKGV3cgd3GO2YIiaQuW7UPbW1u9oNGFSsDC2n6DPVacvYLd-Jj--MjpNl-PmBQ3jERZmHzL-Irs6ptfkVVP8zC1QeKfnaSEyUYOhNGZzSxzs-e8FLuprrBroyvG-1jmELzOMj8pOw-9S0WcaAVfoaKQy21Dh21MP78qLPj3w_1M8lRJWK28OEtt2jKVn7OMVQ1DHce0xk2qeKHWA0BEZfDBk7j7kN7Gy8pcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnJl0YjPSYsT-XhjNmLU_ht10XKe99T7TK2Nn6Qg_-FTgnh831iUHuC_KyCyTFvBtSDfwCKO5zLM2zNQdVOTeY9Rp5hyVf-Rcl2TtKRPB6kba_xioxm93h00IjJE4Cxh5knq_P9Mg21SoI5_BjNFaE_bAfUqHCJVPUBi-EyhmmFYodNmQX8twXL66UHJlHgTmeKfDw2eSc2l4ubcM4lM84PAOAbk3g4mhc4o9zfuMyZE5i0jQUCOY-8oesSX_TNqEL-qrvYjq-9V_YwUlinyb4vU1CF_ugHg_l5Pma_kgfNedi89ANw64cbI0DJHS8PnDz6EN5aQkG07WK0M9I71eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH-DkTaAaOZJQ_Hdq1X9mwZ8gvuVYb51-pYvaGbp-xGhh5SMHnYOCIj8TriVSNi37U56ZkoLDt-LSKbhBoqG97nyQbIzGV66YKiQEGwcV0ANkmgjmt_GO2CUd42EP8uWtE1KiDX3FCO8SkEzrlnxUyknFoS8kD_-RvJ5OgWvPo1UeAQzPO56UBaP-kRCWeqnaU7lZ1RcnEaOtcKpfi_-oDxsGH2zOjFJpuuc1FUGpWCyQbu07mnL0zq-jfLHGBQX1RDPy0BntNBpCfiUhIip6DeZq0fUMiMS5IQaQ7xzHZUR6RDGPPrZHBF9mz-cUguhTtTNz7b-9tc4N42otzjVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQS3P0niOi5rE_u9nlXun41ZJilLQZNEDIDudjyqlS2UiltzMw-eZ1pS_Gab0eugaU0h8KMYnfgOTkFTVaW1t-9H_PSzq3Kmyk56CGOtBrkYf0VNSKUKba8IxYGdYDKmmvpWyMpFt_3uNiNDnozz1_TWbInKP6BOj_Rqo_RuP3L5ulDOjHBbcWu8x4nW81PCEMnTVD0mefSkacI0Mwn2YbAspEUqksOdnvZGch0KI67v4CZnREc9KWRgoB4Z6TSKzdA4ftR-76mFkNeKUaGRCZKj55mqIhMZ5VtBAxE1OAQtZEQisiMH51cd68GZdi9BU6k-0JboySMShViwIUTnFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMFHj8B6Pl11SJum8ngpl9qSfZk2CPrM-v3LtBdWYTxlDHylz5-3cpwxeL6rBeAFbxprEiVXnbjYozGAilGzDfqf-fnbbXejwFbSF5VpzBtYcM5TeGwt2FrbpeCwrg7e32v6AurszgCUUbHlpjF6Z-0yfSN_vkqA6qci9UhXV87nhcM9mM1f9L-P3Q7x7KpzkA2UL-20nbRQFgJUGcSy8RPxTXN47MCIYICAMPZ3HVjAl2Eh_s7WzKUmbHTU_k3AhSqeuqh4MFU3eefWUmxnCLHiG9WkHEQX5_k3Inkp2nSTzLOyYRCZrh2BTUxwrNrqNNgFMYG1dXYKFCdB6REOkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMKYMMNETCIg3swWxsByWBgBg7ukfOEQ-_3PKnO8Ig7QuJU96CD-lApJbuteoRp4I5UojEf8SJO_3eyBSAOrozGKS3MKAmMrmEWGJjvTv-OvWy01ygiGTwcMVLQGiP9b6jYY6eSWv3amSsaeBnUNr0ATOr__YhJvblNyAo7tl3C7ZNud49UJ5fAN10drAPxbTV2xKPkC14GMDlTHy1ccrwofvs8kEWSutv9O5qnPTjiJDvsuc0_iNIruozmi-nxLzihnxa93bYdsIK2y0iMgbn_7ESuzb6c1Re1qmx3Zsuu9ggntGQK-7ooL48KGBWpsQ1_9eIZxX5cSLAs4ejWbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=tVYdVO20_fa0v24Dr0hGaNeHxq4ydR66hGKNNl_sHSx9P5nDy5hhU0PnJFzgD1q_elYqS9yRLm5laiAVa-bvXsT8HBkfVIneHwpyDTIb2Obw-ScWliJEEs6z1wz9c5aum_iawloJaVRFfTQRFH6jZkCA2-2O0NuOOjWuyeKuJ2dcJQRaZ-o-pGTQQr9LlClr3kpwqJr8gIOcXAEOeHQlG6VW0CGOqJypjOHm102J-h0puH01lvt4Hi9DBlSwAoj8Yov-oVNwwZyr_7vPOSKL0cQFi6l83Qym4VseFtc5MZVKEc0Z4456lhyR7eX-IYi8On12_Q2c4U_w02HzBaQCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=tVYdVO20_fa0v24Dr0hGaNeHxq4ydR66hGKNNl_sHSx9P5nDy5hhU0PnJFzgD1q_elYqS9yRLm5laiAVa-bvXsT8HBkfVIneHwpyDTIb2Obw-ScWliJEEs6z1wz9c5aum_iawloJaVRFfTQRFH6jZkCA2-2O0NuOOjWuyeKuJ2dcJQRaZ-o-pGTQQr9LlClr3kpwqJr8gIOcXAEOeHQlG6VW0CGOqJypjOHm102J-h0puH01lvt4Hi9DBlSwAoj8Yov-oVNwwZyr_7vPOSKL0cQFi6l83Qym4VseFtc5MZVKEc0Z4456lhyR7eX-IYi8On12_Q2c4U_w02HzBaQCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=J-iEQJohqv-ghcol4ku_1EmlaANVDjAhNuDwMCisFJyZlN7HuQ2Gki7o0DMg2abEzS4lVLhzjVT3hIb8rFFztopzWipLd6-X3OS5tO-csnaFFW2eLAz1vI_ytMrtzJC3rTX1wNJ7TbPFzdNmAAci-FyMruB9F7pMKhQKM8OlnY0FBWaPRAsFdKOU87lTbyUTkPoHjN0kVFzs5-78yj6pVvu2dySmj-FSZjqLYz5u6COU2wSldb7vRuXufKesRvky8BpU7Z8vnNGOsblnbh_mL4uRPibwUccIAXemk1ki3NuSgUDD1jXbpQT2tnS1Yf7BvJWPNvIyUkRaBgjWa1cAcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=J-iEQJohqv-ghcol4ku_1EmlaANVDjAhNuDwMCisFJyZlN7HuQ2Gki7o0DMg2abEzS4lVLhzjVT3hIb8rFFztopzWipLd6-X3OS5tO-csnaFFW2eLAz1vI_ytMrtzJC3rTX1wNJ7TbPFzdNmAAci-FyMruB9F7pMKhQKM8OlnY0FBWaPRAsFdKOU87lTbyUTkPoHjN0kVFzs5-78yj6pVvu2dySmj-FSZjqLYz5u6COU2wSldb7vRuXufKesRvky8BpU7Z8vnNGOsblnbh_mL4uRPibwUccIAXemk1ki3NuSgUDD1jXbpQT2tnS1Yf7BvJWPNvIyUkRaBgjWa1cAcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=gkATl-Xc_IiGI46YuwMkzdhu_THL_dYEZ2d2Y_8T0vnOdDjLDuZJSIKHuqaoc7KuDpjW6upmP7Sq2r6Dr52URCnPftJ8sRDLbB6b_AOtDlTPtcqUUmf9J4icU9tbanZ6G54jq2wh61QoyCf8hROILXDrJu9dp-zPLAa9oJNGdPlmS4AMgRTIwg4ttM5T_l0uvXF58TibvHt97sOtbHkiQn0xOL4VonkOdv2hzyVk_nsCwX52vkVACGiMqYD0BJiPifPBJesJxnxO0ANHYyGmsQtJ71sBCsptaz0KYQl4YphAof1PMxFe9e_Qs36xYckt67FLy5IS221VbjeYJebSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=gkATl-Xc_IiGI46YuwMkzdhu_THL_dYEZ2d2Y_8T0vnOdDjLDuZJSIKHuqaoc7KuDpjW6upmP7Sq2r6Dr52URCnPftJ8sRDLbB6b_AOtDlTPtcqUUmf9J4icU9tbanZ6G54jq2wh61QoyCf8hROILXDrJu9dp-zPLAa9oJNGdPlmS4AMgRTIwg4ttM5T_l0uvXF58TibvHt97sOtbHkiQn0xOL4VonkOdv2hzyVk_nsCwX52vkVACGiMqYD0BJiPifPBJesJxnxO0ANHYyGmsQtJ71sBCsptaz0KYQl4YphAof1PMxFe9e_Qs36xYckt67FLy5IS221VbjeYJebSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=VMopnls5Rll0ulq7XEdlIXQnT4BdQWVwFS52X2SbjZHtfp1ozPD-4f6Kk6AWn5Ej6Zy6XQQ2rRnnoPLoA8FX60xT7V9SxByR8DNlOR6XxINqm49CLDXPcJ6aZut7UpBRwBMnIUAjDIqR7vpxo1rfcGAYVlSWs67JgXRWLBpAYbdWkq7Vp2C72hfSfnjsYN4Sj9knXfJ3RsUYgc0h7YD8rcH5iwwEG7dQwuPDzl8VhRkyMqJWrrvo9wZGjx7ZDZ2MXZFbV9xRstDRG7HU34NPyENwN1UNmfTzutRz0PBP35jvfg6fYdcV7PJPilo_9y1d0zLkdpi_ktoiRNcJfGaStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=VMopnls5Rll0ulq7XEdlIXQnT4BdQWVwFS52X2SbjZHtfp1ozPD-4f6Kk6AWn5Ej6Zy6XQQ2rRnnoPLoA8FX60xT7V9SxByR8DNlOR6XxINqm49CLDXPcJ6aZut7UpBRwBMnIUAjDIqR7vpxo1rfcGAYVlSWs67JgXRWLBpAYbdWkq7Vp2C72hfSfnjsYN4Sj9knXfJ3RsUYgc0h7YD8rcH5iwwEG7dQwuPDzl8VhRkyMqJWrrvo9wZGjx7ZDZ2MXZFbV9xRstDRG7HU34NPyENwN1UNmfTzutRz0PBP35jvfg6fYdcV7PJPilo_9y1d0zLkdpi_ktoiRNcJfGaStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pLqy6gGSpEfhk7JJN59Rmr_FF_1rORh4r9g9WA3WaH-0weRSsniQTGeam_lefeLOmhJ6X_5WhpwTOLhDWoXxC9T5LTiUqUHs41JFG6moBaStg5CYDstUIY0AfTWO_-R_bBKMHHX17TK5AlCXTCU4eZ3X30fZZfp_GdRn7JXBgzRz76vuJuwBsizZ_sF2q-2kiRsPdBZK1TiUQiHSiYEnPQFaBEr9UgW0hvZoisT5fIo1Ryvg_hY7ptf39haBpY6_LC13q2t6gChL5VW4ZMQd5IR4OuIoYJp0JECeGNUifdW5Km1H5N5KZIPwxDkoXDnOUMedfpfdA4_JAUl_ZbdHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pLqy6gGSpEfhk7JJN59Rmr_FF_1rORh4r9g9WA3WaH-0weRSsniQTGeam_lefeLOmhJ6X_5WhpwTOLhDWoXxC9T5LTiUqUHs41JFG6moBaStg5CYDstUIY0AfTWO_-R_bBKMHHX17TK5AlCXTCU4eZ3X30fZZfp_GdRn7JXBgzRz76vuJuwBsizZ_sF2q-2kiRsPdBZK1TiUQiHSiYEnPQFaBEr9UgW0hvZoisT5fIo1Ryvg_hY7ptf39haBpY6_LC13q2t6gChL5VW4ZMQd5IR4OuIoYJp0JECeGNUifdW5Km1H5N5KZIPwxDkoXDnOUMedfpfdA4_JAUl_ZbdHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=lxsfBT936L0UP2uxvPW6u2v_9zLJBju2Ft3zT6xet7zFa7j-L1yWuk7mtMZyNd3B19S92h0cQiekajpUn6v6ZudujhVc9wcwnu0D-8XYn_RekWUFtxurm6F4gCJziRnve_RhwUWlBItj6kc6kjUDu40kIreh2CKtF2zPA-QNCErPya3vNM9JFxGyfc1FQZWbMp2f1eb3PR0bvdgEKH3GWxCpKh_3Shr0L1CPHLOMDPdFLmUl5JDfcosPq96xjiNq74HjYIT2_ir0wyfylgiBygv8x1pl0h_lSrCiJfMp8j4lpOntVw2T8eL8DGvmgc2suQNFkqwQb7zDf2tPwGxb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=lxsfBT936L0UP2uxvPW6u2v_9zLJBju2Ft3zT6xet7zFa7j-L1yWuk7mtMZyNd3B19S92h0cQiekajpUn6v6ZudujhVc9wcwnu0D-8XYn_RekWUFtxurm6F4gCJziRnve_RhwUWlBItj6kc6kjUDu40kIreh2CKtF2zPA-QNCErPya3vNM9JFxGyfc1FQZWbMp2f1eb3PR0bvdgEKH3GWxCpKh_3Shr0L1CPHLOMDPdFLmUl5JDfcosPq96xjiNq74HjYIT2_ir0wyfylgiBygv8x1pl0h_lSrCiJfMp8j4lpOntVw2T8eL8DGvmgc2suQNFkqwQb7zDf2tPwGxb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE90Q-N_PUCH3R89495iVD8837vbw6MtLirFGEMhbFNolgdcRIChABntMmkj657D14Ax322BWEXr6pC7LNHq8TJ8pg65pNayJ19DN33v9Nht-cQQRxWUNfwtdlq5fJ2qte_y2bc3tqCjpS4fkWVcynoWIICNVbUgOu2ieAS9t6ZFBeANWssu9T8LxjVyEJSXQOtj3MaflGp03aX9FimiZK9GRl1MTSLJlmYZkAes1Qew888sJ4ALSJMmIaeAZjLuCQfuI_fPWwZJpG82Qca8tTU7_wG-M82ic68jT1LX5_wciaPliWYhSbC-IgH7BqmHO4PcIbOXlMKswHnPTuIe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=fiiRtA8mcbnjmQgOx7VUIk2wercTKbT7CON4qiy2p9L_xpy8yg7Y7M5asj7F9kC3KauUIgBKr_3m7wz7MejaTRjAjj4wdtGmpSj-sV5S5NVtmXFG6yfu3ggU9Vog45kZANS3ND3-XFUOlXLPpthaW_b9tqx_fG5BJPzhpQn42Sp_gPumX1EGf3G-CHQPa3lIcwWsY8uxcDDY0Aag64vziPQmIUP7GpefE6qeHjpLA0renftFrXz71ibjNnmg8TsNmXPbQnq2eRtayOuY9egBjRm_dZTc1eLTCeW85Py24SytS5ftGX4tV7-Q_6AOq_s0mZvkRrsbwenp329Ec-NQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=fiiRtA8mcbnjmQgOx7VUIk2wercTKbT7CON4qiy2p9L_xpy8yg7Y7M5asj7F9kC3KauUIgBKr_3m7wz7MejaTRjAjj4wdtGmpSj-sV5S5NVtmXFG6yfu3ggU9Vog45kZANS3ND3-XFUOlXLPpthaW_b9tqx_fG5BJPzhpQn42Sp_gPumX1EGf3G-CHQPa3lIcwWsY8uxcDDY0Aag64vziPQmIUP7GpefE6qeHjpLA0renftFrXz71ibjNnmg8TsNmXPbQnq2eRtayOuY9egBjRm_dZTc1eLTCeW85Py24SytS5ftGX4tV7-Q_6AOq_s0mZvkRrsbwenp329Ec-NQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=cpYtpXXUziPxG3U5JNXkpq6VBZnR7eCuRS_LpbkuZVf9SCxd7sWVTvhM9xd3t5FT54JvVt3VvEi7nGiF1MtMZ5b_sT3frLpmJUBZOWDBnWuM6JNGHaV3l2MPqEcHeKyCFIR8peIz74uqNHi93ilP8EhNa6XnZRR2ZaXDeXGZgK4HdRgPZjS4aI4qghxxh2NVMpqsAZQxhsr2X2StSAyVJJKq5ZF-G9mbrCytGUHGVcgTCXT2dMVsXOv_Rc6rCLqbc6eOGEvs-sfDU2nJqRrr0HCwP8DdRU3DdgeRzoLvzacObtyK0j46AQ8DRixItW1peg8of4sHzmW6OxqHWjNfdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=cpYtpXXUziPxG3U5JNXkpq6VBZnR7eCuRS_LpbkuZVf9SCxd7sWVTvhM9xd3t5FT54JvVt3VvEi7nGiF1MtMZ5b_sT3frLpmJUBZOWDBnWuM6JNGHaV3l2MPqEcHeKyCFIR8peIz74uqNHi93ilP8EhNa6XnZRR2ZaXDeXGZgK4HdRgPZjS4aI4qghxxh2NVMpqsAZQxhsr2X2StSAyVJJKq5ZF-G9mbrCytGUHGVcgTCXT2dMVsXOv_Rc6rCLqbc6eOGEvs-sfDU2nJqRrr0HCwP8DdRU3DdgeRzoLvzacObtyK0j46AQ8DRixItW1peg8of4sHzmW6OxqHWjNfdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQn5p1hUnfNeRJ6XrYhLO_Ric31JLUXXBO0kL_nJM_pYuEUm05Iet8A-yEL35OPlhIxNQn3ZLaO0Q4wGDKjasMJAVr0d0ELKTtz89tIkN44SwBarSTIP8Oheqg0uilaIPy9x6oBV-ybNBY1S2FN_o2yseiafQJTEf-j6tx6ExGrrocTBYDKFOceFIMNyJeL1ScE4_80OSpLsZjALwoY9xYwCn4gkLjkVTyPRRjmH2Be3IhKgsU1gG0rtB2KHO-hOZ06h_7cNxjzGHvtoazGUts-mk7OHrSAL24UT6enit9Mk18F7TweNn5e6PiemZJoDv8oApeQVns8qnq4U3AdvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1giH829DBjzbkMKds-Pm2ZX83wICGRYCDGwUbDhGhAY-3dasd2W_PMICCrNmM_GIKOQWEBI-VWK8hCns7wm9SJPOeSbl1Q2VjSSIPssB94dPUo7o1Bh-Y5m8oxrFZ4rhI1h0S6bcTotzaUxS1tV90DEf_zodhA1xNUutI5as6AD20x9abtmc3-GEkcaIIKTHDqfjtsVZznKnlRxgj7fdUeHyYll0utP_iXKTjcMf7nyXZOSEcCiMcAo28zugKWAbLrbStOCX3MovQjz-whQ0pxPDjIVei3sHQd5FyiwqZWh4dWeBrVDXloX8-0WtWhFniSel2XmPcmL1FMfxoIRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiF1R0phrrxUZYrYSpA1tT0o-QH8ALyckaOpxI3NBTqYUNa4zi077Fy2NpkcD5qhLadygS3A-FlWs-dbBocOKa2-UyabTRDW0l-RNkeJuIjsSgREkWpinbR88-IlI0niBO8b-yjkgi0ohXfFPzeg_SNCKnl-CsN08P-wHQUYmC0akOixLM0ON6BUPol4TZt2ycZi05idqsudXR1Pl1u_Wk4gQ-MCvgINaMXSmRiNBBz07W7ElM3ZTZQYsr-cKEU5Alj68P4qLvubMy0tH-CH44Dt-G9-8ZgdYYPN1ba6jgLA0PAUDo-U94M3pWQlQWaZoELCl5Xqej0xeAT99vlFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahax3DDLevKi2K_ezQxemcY5V7Y2pFhAEpG7aHXi5hugdKQnHKbRTKWp5O-8IYCHYKXU49NI3BySKnK5A_vZK8hV6SKmSO8Qufv3d61OLwLp52rNemMXdJfaZtmL-8k4v6ixa7XRpBAjteRYfUSsXMPfJvZVn1uNkwoEpgTkbP5WdjMdIfzRLbg6ylHeWQu1B3YvAZjhYb0c54Q5mOtIzkdwxPsSnmf4VkHNxb_2-VYot6R3hVcOkk6bVWZyI06_tjsQ1-CuFIvPemR6hXfYSx1UPNwymse7E84iW2b_EzvlDKnfsfn10GA0K8ozBSZiy8w2q24W2YZNlII6a24idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca3TYKxA55jkmJgiTx6YshgaEkYOFu3fo_hXP897wjuuQ_yZw_a4bRfDFbaZUXs7zhZIaR8L_8jSp_hRfRwNSjq0vJn6LCD7DFswAsyxC3ec9hnoRBtdv9TiPscHKK3sUu_thxIJGlVxtH6T3KEe4kWH6uqt6Om_Qa_RQ3t2fr3FCSYq0ogdYoLK_oLWu-s9-jbaIen4u-k4Os0MgNrmnyo_gysUGTQyNcGzatZEdK5B_enQteygVMPB_NrWqBjWv-_i8nKHFxPYQQOP3d3M7T8z_n_YnBtwr7sHbvZ87XhrfmupYfc_iL2bbu1PNGcMnzgp5QVrkVZCthqo-Hr34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDnOTCxzs_t1XtXrMLABd2AU1MT28aRJjQ1dEnZPxLGRBSQuN0p5nA98Lrq0FCU9wH0-5Z8MNXEGaFjAJ41Hqz1FvM7TLORUT5RQ9XSoZFvb414tNTsu7pC4U2AH2yXVvM6Jln-0-bY3X2lDFc3vCHIxPB5s87OinzmNr91jygjMs1fR3Dnoho5mxeGB8XeyFjhmc8G7xB2vRezHu3DGTc7l4o-Ly8f9lkv5Z3QZizayU6ItlaHwNh-0TVGaIKnghx1UsZzQW71VoIS_eG7-ODqAP0cPHy5bv_D5IajVlMmH_61_hXb5aGbvURkbejVQ_icn1VTt4D0qyKb4NXQoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPPdTnmFuyzKDgpeU0QPuaZNtUr2hrRfPrVsKpj1EA1cTz3oLmiHZ5qqp8MYJ6iADf_TfO4Zpo_5gyzQDy33hUU4S8VjzAvhpv7ZkJeYVFph_VWLIaz3q1uDGAGeQaWe0m-NoB6wbHEKgH0kOdI3m2s63bIhMt4_Z3VHDWf_CSE5ieaITqrAQvzNVKZE-9m92dgsmTrXQxo74mzNw8RIo9y1EcvaF7ww1BdJZut8JC_pvHe_046lWCeY70cppwHmAvgZfYmNuw2oSIN4yRlia8k-mmlOPn_DVqP7ILw9QTRoxu95s-mOSkhrw_G0E_bewb30pLrqwEK4zkx_CfyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTAShgezL9YDP8P6KPPPhiExxjloMB1jV0ZIHkxt3B2yL0wuM_iZC3_iqpZx_9F4oCOC84K4CZIyZKo30tkjFQ8FGn0iJtyXlcXVHODhHQcQlK4s6EpOUNOCJWgTlzZxMAQWMTibMcB0JGzv2SdeBLNKiFHwbT8E_annYtdG0oZTblxUkd7HbIdM5a2WlWprZPwHnZEH7omWMAWFrFczTtrNdVc-lsN6ONyGXIupx1Ip636WEbXPCEd_KvwPzJXARwDYGU7wdcFgL2JZBmAE_oaUjMIyFaGqSMNU9DAVRZHXBjeldMaH2T30v8gubRHW8BMr00FRtmNbH_-MysTQUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB4rHvVy-Z84WGKW3EbHKYiY8E6jjhwC74_894MS9iG0S_kWOYzsIbOGwmNOljFelDsmJ_fZ3PVmMI3Qpow0lmETwlLOPVIi-X8l_zd3u5vV5bd5QiZJeVPU6giTUxLRVtvfSBNKoMQ9TEXGwG13-KT7CXw_U8B2_VaZ5DPVb4S7q24G0HXldIybhFDTmcbNdXuJV6ApXUKA3qY0_iHcQPoBnzEc4_zdvYlobUa5rTqtnvDqge20FKNdfPjIZsYZ9F1MpFguBkGv69PcMl2RZ5j5q7mw-oGFwr6P6ZutcfzACyAAgfLb24C6pPIz69zSltuG4E36IP9d6TctDxvTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT4qaebHFNLq55bFHMirv0am4WVSzCZlkrY-WDuNGGVfgRX07oFxk1lkUg3L6AGMfYwCM6RKz-DLYe0hiVdSpV3zOpl1mVBmDOFl9pHkaTc9oQqRbgHXdnmkFsadUzIdtytNKnc5pQ4owKTwZ28wDe_Vl4BRzTUA-xfBN8F17w5BJNuD0IgcvJwxBRL8dT6ECU-vp3IMy5ynFcHvdBSGSFYXcl-I3_7mm4n-Lxs9Sy8iq9p-kylG83td8tS8jaUZiEic64Zr2qUGts97DIe7zwdwFKFcDigqAttfh3I9-AwSZI2sjVH1L77hd5FHBGtpbeymHQwTeD0O7ijmqe1vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWXMmyNlAD8AuZIE_p6wABTuF9dmHEIGFCr74Tw2Ez9Fe9qyOgHTtoj--BjWRfwI2fHvOC-boGBb1SFCp87Zs70_4AvNre0Ss952tTvReE6fnRcAjTYRsDoK4IEB-sjRaVQ4O932X2FyjmH8MdMtm7h08DwQXjvWYZcyNZ-T4o-xdZbtMtrmXC4GZiB5il1M7FG-xHK8E-1-Y1JdEPJ4wMFYBYduofxbY9xqtI5XSWZOE175z8BnIgfqIqVt_SuSMP0Gb6LqegIu3f--tbMgyqXXKuEqiYaQ4nPLm-RHTC9NrEzQB7g0ujtxagJXhIJCVBN76l8rSacZEALvkrFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9EgwNF70rkqNgIppFfa_YQ9Im-Kgaz-c1tfXRd2hK7EhRpMhQdf7vMax3RE_smmTk0fvlTaVsOH3cd7GmSgagShdWzl8EiGlteB-gMPZqlW5ZELC2NzICssVgOGAjC8Q7le5hkw8e2idl7EiSjpjCp8fnSQpNHDHFVQPpWOudPtpHREHLPrhgGI1ktzUu-pxukZXyqTCeVZUaCNe8JN347wO4fBNC42b443EqphZEcmVgEG18oZNvgSs1r2tYqpKyjtIdZwn4XSsH_5K7ukNXNCimXHQwEV2du9W-h45naLSwoO3BwCKaLWu6AR_Pwl3shtCalhzdB6Q0RWyVT22w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=XIDzuqfrMZkG-slmdLXM7c9ryCCSj7SRQLGU0kYE-S69MMlcL1jM2IbBmS38LmS6isVNk6hI74YlmddslRDDckGlxdCnn7YvyZzjmKoPQblFLA7SR4XXTEtGjPVpYhtytN5diI-99Yakk98PeHI6FOEjdJNID43ISHujDrd_8112FH2t1xBRXXFcedopZlN0-1ZT85auTpWG0lv9-_BVpTcnkR2tMiWz6seiUv17d_m9MRbdNKucs3QGK8NRzQh-SoA6AcNG2-SJUvbeRHzvoxq9824JJw6Kn-ERxTB1RkB-0ccYreFFTNb9lcKNnQUE23sDFL5BwTL-q9YOOsY8Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=XIDzuqfrMZkG-slmdLXM7c9ryCCSj7SRQLGU0kYE-S69MMlcL1jM2IbBmS38LmS6isVNk6hI74YlmddslRDDckGlxdCnn7YvyZzjmKoPQblFLA7SR4XXTEtGjPVpYhtytN5diI-99Yakk98PeHI6FOEjdJNID43ISHujDrd_8112FH2t1xBRXXFcedopZlN0-1ZT85auTpWG0lv9-_BVpTcnkR2tMiWz6seiUv17d_m9MRbdNKucs3QGK8NRzQh-SoA6AcNG2-SJUvbeRHzvoxq9824JJw6Kn-ERxTB1RkB-0ccYreFFTNb9lcKNnQUE23sDFL5BwTL-q9YOOsY8Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=gKMRY5zz_mmsz07Qtk9L65Qww0FFBcJB6ablmuuFeXlaU_MhyVf9p5UuuDuFMqdQesxj1l_537KVSttff8g42DuGCGpVHuVbNqEvNo9bJkbXG4ZMBr_lZCXlHn0YZXJOzJZiSK1nEBYcGcvGahX3gjisVxJg0OoWKd02RZ0AEwqm4ZzSOwsm_rc2iMfb5ZizcdYFWUlVTvKYcdnUkrqSSDESBHWPRp5G_PilpoQ7la3nw1TsAWdCmWnFfYRlikgd2UOCj8u3vetAJ1exfoHoWfWdK3fPYRMkdRx8ZiSvt3-lSf8g6acQ2p8a-c-n2r8OjedNalObMnlMUkUA2JRG-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=gKMRY5zz_mmsz07Qtk9L65Qww0FFBcJB6ablmuuFeXlaU_MhyVf9p5UuuDuFMqdQesxj1l_537KVSttff8g42DuGCGpVHuVbNqEvNo9bJkbXG4ZMBr_lZCXlHn0YZXJOzJZiSK1nEBYcGcvGahX3gjisVxJg0OoWKd02RZ0AEwqm4ZzSOwsm_rc2iMfb5ZizcdYFWUlVTvKYcdnUkrqSSDESBHWPRp5G_PilpoQ7la3nw1TsAWdCmWnFfYRlikgd2UOCj8u3vetAJ1exfoHoWfWdK3fPYRMkdRx8ZiSvt3-lSf8g6acQ2p8a-c-n2r8OjedNalObMnlMUkUA2JRG-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=sM4n0D2zDbhsJGkkAFeIXiGDe9c3QkqdRw-3Kn0VDklELsFTgpzpnI_hq5AFVgNEaEQRuxhfkYcXXb0n8LVAgtXfuyhX5WfvapgBn6PM1JOmiAil2LtBjbftjtwnX1-e5xt4N1532JUIHvq8NbQxrz6pxXjXCRLpub6t1AfQHO03-ar9MIP1hR3xlyqnG16neHJJ2Ffa2CZkrpk44a4czEWQbA9s6STdK_cWPtP7UXS_LsqjC45RgjQwpn5tV4gCo1KpPW30bcvMAYuf5Gv9HvJ3C4zQeoETUbQ6r4oLUVRaiHCMrFwOsIUTebupvGsJjcFjSigobAGogItbeEmJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=sM4n0D2zDbhsJGkkAFeIXiGDe9c3QkqdRw-3Kn0VDklELsFTgpzpnI_hq5AFVgNEaEQRuxhfkYcXXb0n8LVAgtXfuyhX5WfvapgBn6PM1JOmiAil2LtBjbftjtwnX1-e5xt4N1532JUIHvq8NbQxrz6pxXjXCRLpub6t1AfQHO03-ar9MIP1hR3xlyqnG16neHJJ2Ffa2CZkrpk44a4czEWQbA9s6STdK_cWPtP7UXS_LsqjC45RgjQwpn5tV4gCo1KpPW30bcvMAYuf5Gv9HvJ3C4zQeoETUbQ6r4oLUVRaiHCMrFwOsIUTebupvGsJjcFjSigobAGogItbeEmJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=bR3k8A09uUp_wmSP0i5nvIt60gcM0abMWLVSLSeLn8oDBIobXcx-plilr_b0UsAOVHGi9LFzRAg18wKlrU04DKri2iCy2Y_pvsHDSga5edLeuANMdMhMO7JlLS8A7jR8x7sXvZT9og73Zxa-r9DoYPLCT3VnplDcEyj0voYCdfB2KqH8DLWd2kfx6cxA77yYrI3VKtgoNgA2kOx9GrypUURuwBgCdZJG4l1FWI73U9LFdIWMCO2cpbpMj2BsIVTs1GbfdyarRPA5F3FWMJsu2Uiq8dDOa8BL3O1bdj_IcI5FvXROtvxsLXqjjcEoyVciM_-4AmTlBQSI7hJWsIdInw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=bR3k8A09uUp_wmSP0i5nvIt60gcM0abMWLVSLSeLn8oDBIobXcx-plilr_b0UsAOVHGi9LFzRAg18wKlrU04DKri2iCy2Y_pvsHDSga5edLeuANMdMhMO7JlLS8A7jR8x7sXvZT9og73Zxa-r9DoYPLCT3VnplDcEyj0voYCdfB2KqH8DLWd2kfx6cxA77yYrI3VKtgoNgA2kOx9GrypUURuwBgCdZJG4l1FWI73U9LFdIWMCO2cpbpMj2BsIVTs1GbfdyarRPA5F3FWMJsu2Uiq8dDOa8BL3O1bdj_IcI5FvXROtvxsLXqjjcEoyVciM_-4AmTlBQSI7hJWsIdInw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=tfR7EiYXtaJFmuNF2mAfyt5FDFrU5e23pO2ACOtBn5Uf0jqWNALqeOEE4YyBb6W-eH-hA6X-5QrcdrmN66PeMVjzJjpuRu2iz6xPtEknI0Iyuj53CVwesdK0d6_uB_lepZ3VJmyxzF21j8Woc1bURGfPcXcF17qJPmT6IJWVORzOFQJEV4CXcNxo1jVFSNn11cCbXyp54HwQBv5DKKvBtY-83RUeXtj6r3VBNdMGR5f8FnHxvaaynyiZxrW0-sJjVoPrNuIjy3xW3hoiRqDaNrugIieDWhgUl7AJmBQET1C8t6XGyq2TjRgW85fqYi3VggtRhPI2EJVXuxzACZRA7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=tfR7EiYXtaJFmuNF2mAfyt5FDFrU5e23pO2ACOtBn5Uf0jqWNALqeOEE4YyBb6W-eH-hA6X-5QrcdrmN66PeMVjzJjpuRu2iz6xPtEknI0Iyuj53CVwesdK0d6_uB_lepZ3VJmyxzF21j8Woc1bURGfPcXcF17qJPmT6IJWVORzOFQJEV4CXcNxo1jVFSNn11cCbXyp54HwQBv5DKKvBtY-83RUeXtj6r3VBNdMGR5f8FnHxvaaynyiZxrW0-sJjVoPrNuIjy3xW3hoiRqDaNrugIieDWhgUl7AJmBQET1C8t6XGyq2TjRgW85fqYi3VggtRhPI2EJVXuxzACZRA7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
