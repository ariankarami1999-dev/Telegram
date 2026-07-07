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
<img src="https://cdn4.telesco.pe/file/vgx5oraikqM_9-MbJruknH2f-YxSaAUZaL1sKvjkuI64aMtoaGfwEdwARppnsnGlGfPmatTn91jLERqR7hyyuZeMUeLoUCqamu61WqL7UAqr2mF1hmkqyt7DtP4LzSF8Kkt6UASxjdk81UQCgAy4ghMUnf9OTuDvtREU5uEi9SYnT_drcnNTq9PUnFV9TDNiknXFca5-SrRViS1sefJiAt7J2_Gbksrh0J4MDp6VkuetZfpHzFLvhr9nGCegjHhDKurOWYM0tn5UENJ6Fm5AeviuCLDl1ANVwZirGl_al4eg5yRS0MD9xMEFsaJUllTg256rofMwW3OfllSkHdr3Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 02:22:15</div>
<hr>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRccgvoabv-wGNxNoN2OpDPp9JgmnkW531srP9oI687kUU_RNwZUgc5Y8U35yfLb-YH-6d5N74l_w0Su0fGhXhoDuvdhZO4kYA-jzSaCas80pejAkUanuJ7Ya6gRCXif06sSBH3mrgqbDUAOSyJJHlDvPE6YpJpS467Tgxkc2XGxk7l9t34b7jRQMpSqMANnnlEJNx5_laqWiW7IPEffR-3IVVSxAWG_xJvpjQLwE7aJbhDoriKErOioVDIQYzzbJcfwEpWHiF_NKUUsyUCTxDWypac8Ftm_sGuednOskdFna0XLY8Ko5JYI1spSGs4Z9YWeEL-YHk5_WqCBj3l9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSu4X7feg3BPs-kWR4gpnmsqBCvS3EkFTLddT0wJLBzhwyOaDmrSYYTP-jHHRj6AYv9y1nnn6ltJkyjewYr9ljU7C1X-fY8bcqtiO5fEJQgG-mCDP01tUJ-nTBpjR3q9ZB2sLKAADp_5s4OyvS5E0X0q4_uteasjok0I_bElwgUdBzj5b9pX1WlLDiTudR2CV9qZHHz1MMu9O2koMGPktgimzQm66D5Gh50vYYt5s5AmaozcDcy4SjNYiqXdx4sc-JmlexDtW74rjHk6-X9bsIIee21SSiW7dFxZra2XdmTvxDyA76qG9iuxJweSTUauZpZU0BwyH5YO880ynThQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmCJ3-FVh4KXEuF3XgtwFp_DH0d8S2po5zTonuxGdyOurHWLh9971maKMYTyf7PJqbb44r1XFC6po5eyIhTquNmFYWOB4_xUW8FYhlVNeJH1GVAKzDwhWs2DoQztxLv0pmj3K4oKq1Rgn3XqiFmhdWQpkzkRK7iyTu_m7rpzr6ozLjrOTMvhFJ2vsRXzf12ao5QY7IUq0a3cjvVcfa-ED7P2mDCaCnBWX_nJq0IQBtOlZYPxXwm8MtoX7Mw4hrt5YCXmkw0gPiDZxuQAZ36WgVS5upwg8JXfg7jJNruJvUl6QGW-CnKXsk9lPy3gRrOMjp7DmfztiVR7lm0ZpEWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-b0jHr_NJTir_ysr_B0SAXAIhuSlkOy6O8cBM4Ppa56gkUAvthkTwmRGHLnTVtnl-Ej6BOTE3nCACIj9K2wNQC77w331XwnAv_SAfuDhWPWk6il8j4e6dWxXLXHBhraRyg_7fOAalVgYktL-3vW86mQmCaHPD_dfXWO9YSXpGVhNGXLN7Q1z6gBklG4EGLFx8McjgPr2euZLDKKrSflf3xU1Yz6wdiG1Se9UkfOj_q3OWh8EDydxTMT5LG-G-wtcQU7S9r5Oresy6iBLBGe8IJYzyy8qlZjrNqI6AE0TFZk_GcLU2MRiui_rSSOTotnFP8_HWHFZ5NoPEvJyvUe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BujRTDtFq6zHFwha7QuQIrLZ2RyrlnALedCLhpGVXTQrfd-AfZKnNScmgRrcmOPMM84kizAi9bJxcHFbsrLwajM9fXww1Q_Cx7B1f5Mx1wohriqYg9ibw8ISvKfspe2E6UWLlf5DZc3lx82FNEImZ_gny3EcBlY-f5ZOkDbp-JllMBJW-KQU5hb3F3KPJ25DQV2rg0_widHqGi_IRqKZzGxkUS8g2kAM9f3czQ4ZMnrin62HBZ4nGMVT0wT2ssg5dYJaYzk9XtIOKUR-m1wYnd5sca7OjrG3DtwNMyv2L99GqHgL_6EWnogm5wUyoRMMOnVOuNCp9PpnFoPXRqcOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoxNKsDbZjxzKAUi8sNmPus15qFPEvWi1l_nNyA449ajA0ug7oHLmIpX_6tCEc4nw-8-J5cp2Dnp0YZng8TbbxfAyRbVtiKIMeTcPZ4Sq38-LwCLwVDSW77uAKeYk89hnuw2biYFPniATMlzaHVkf-EHmfXaW0eY38HxhBU5qyrxchhGPO0-pflzJCifhsJS5mFEjGQkNOocH2i9kQ7yGGHBnRiP-ii2veyHKujeXvDXADdVPc9XbVRT1ZScGvylCRjrkiaca5fv49ubbOuFmsYCRU_d4mdZoX8pyfN3uWvz_XbzD9MGB3FW5d3UySVuZhE79XWM7pnH_sSVI3TxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKNQe97Od1oYvPJRtOd7KNBsk2JU96HzgwMVozLV8RnUGBKxdxYTh8GXuo6VrF7t0dn-VsqvVuu1ucbpf33HkL96gMgptnmNxzwkQmhIMGZK2tTQ65PYGJbz8afDzCXdA69iQmYAQA7XWzf07smH8_LJvTX-7LQCCuQvMvSfGxowuCW4yPvoP4hG-Jf6lLRjnBak0nGcrewRWZC3T5SjsWPdUOPUdGCk1coCl1ig2UP1eJyEPTlalxjfa3mK2pKy4yMTsBKcmy5FG2ffWvCsl9l8ccbM2jb1xb1D2KKizTJfruqkOt8cwE4FbgmxpeKDVaAnMGIl3oHVeIEywQHw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIWv_hd4gjwQngvdPefxV8eOxWDox9kvtlfV9B0HxWyfnNSo5cctKlfhXTwL9drQV4v7YfcCFxGvYM6xRlTOkEKRtKk4X9k9NCCsusIliplX9odqHO_lidmm7LOBDo_Ev5wC2J2T5OpddAp-6lWpp9C5a1rl7tbon5LoaCsgHI1L0yVSrKinVvvDegNpizL-_CSTtRdX2B-FbKY_IYSVEVoKAu_WvQnDOJka46t4RTEm7P7UguXiXE8eWmBoheAzBg-cDgjrwJYYfjTx2_cEvXMwln_anjsw-Iq-s2TuZqjtkbybNBHkRRlfPh4bCgW3aDfDQew2HDioLn41k-YbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGWq9hYxk9dJsv0FqsCmLrGLAP4k9rPn-hv0f5_g_qEfdbC8kcaKOpJvibj7qkOhUaH5NXLpyPSxhozcmqs8p2tbfojfW0v0qEKve3TxBXbsgWd1OaALjHUPvm_26cl6URSTw_LqcCpQBe74dyu2PKkRTudDzGSGcwwhKvUPst-vWWOyNDb8oBPeHGwuoE-pw4d1QNsMcpULMwErpHOs8fFJMJX-DUa1RktyLC7oxPo2i8aMbnZf_ZZkXN1Sk0ZXPrLlFaVbE5rnjO4CIF6XBxU3qZ_fxdMf7n2CWv9j4ybdgViQsmyAiI_rv1CUjyfU0Hv23cjDtoKZ049OmJVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK3ZrVzWY__2d_UD_aPuLMbRm3kMbvmGuxZOVW9c0Tu2NYs_7JYSfFjekH3XRIFwvcz0qbHBQaDAkKKWVm99ydVHkMcCiWTFr-kftwlH1zPCchuQPbgTpJnX4DBNVpgcCziZuye3R495s9npgYh12QVWkNa2R2fBMKbIoNbyCi0ahEzTlPwipH947daPFLpcceGGUIDlcfOJy4R2xxX_3cq-tZtPNEXxmvYDJ_lNs1SkmjX3UeJsrJbxnbHcbxnkfIKUbhXvtvYlL-Jwy8TLf_NJNrZw5FN01_8NCiv8nHNTNWmFXU1fR3nL8n2UqfcLOmdwL3Tzlh7RbOiXYDRXDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=RzEFy5YWNf_AKKPv_ROkHAaqYstObqSx9DM58UQp_QzwkyN7DH29jweQRLZTDJDeYA_Zd5x_NdO8dGYFgl1gwRDXZh05l-ifS642n_D_NWXpRyFB6XAxf3R4If-4WvtSksFdyyyPoByzC5y-qp4Qve_V-f1DNtrLKDz-uAeRKLJp7xh2ZRmu0r6XO-5bdc_feiVarLWpv3hVCYnAQJGgFofYuCFs1O8pco46j6Nu-PQb5NrLudjBKe6-zq_B3jqb74TFNGMbb1JqJtgukrE0VrXh6zU5GGdsN_zaO3dBmvYQswJ0raugBdRVi_TGrRs_3GHwrSLB4icIKdnMf6BIfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=RzEFy5YWNf_AKKPv_ROkHAaqYstObqSx9DM58UQp_QzwkyN7DH29jweQRLZTDJDeYA_Zd5x_NdO8dGYFgl1gwRDXZh05l-ifS642n_D_NWXpRyFB6XAxf3R4If-4WvtSksFdyyyPoByzC5y-qp4Qve_V-f1DNtrLKDz-uAeRKLJp7xh2ZRmu0r6XO-5bdc_feiVarLWpv3hVCYnAQJGgFofYuCFs1O8pco46j6Nu-PQb5NrLudjBKe6-zq_B3jqb74TFNGMbb1JqJtgukrE0VrXh6zU5GGdsN_zaO3dBmvYQswJ0raugBdRVi_TGrRs_3GHwrSLB4icIKdnMf6BIfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FI6BAkvRY0_jDR_5LrTcjrC1kybbqWRO_3eu5vFFdkibCydNwUUqIaUGtgo_NcfN1i5b-zdEdatKz625J2Sr1ZPcttNpYL4WHwHTgij3jyIiJKY9bjbyiGVtnetwR_zYjhjeMjCGbAqDYZY1fhB2yolkppkdvW1xVV-0ONMzZa8pP9EIOwvgw5EgAYxhQLwRtPjvFCFRY121XaM-xOvnZty2htpESnaKVxHo7ZTAn39JZ1VVkIidCPq5Es-AQ8n6hx8UiicvT_UVRjZzM7GrAySJ7_DhX7EhxB1IUm41aYweC9vDNlEIjXke_wAGRoaFwPwqP64h92u9Yu3j2Ansqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FI6BAkvRY0_jDR_5LrTcjrC1kybbqWRO_3eu5vFFdkibCydNwUUqIaUGtgo_NcfN1i5b-zdEdatKz625J2Sr1ZPcttNpYL4WHwHTgij3jyIiJKY9bjbyiGVtnetwR_zYjhjeMjCGbAqDYZY1fhB2yolkppkdvW1xVV-0ONMzZa8pP9EIOwvgw5EgAYxhQLwRtPjvFCFRY121XaM-xOvnZty2htpESnaKVxHo7ZTAn39JZ1VVkIidCPq5Es-AQ8n6hx8UiicvT_UVRjZzM7GrAySJ7_DhX7EhxB1IUm41aYweC9vDNlEIjXke_wAGRoaFwPwqP64h92u9Yu3j2Ansqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=m8QSvGpdc507OYMSZH5FDcADmazIoq8VBSjAg52RtikaE0uk5xYcoN2HH6PQqJofH5W-EmOw-A9Co9sx8iSUn7d6u2ETf7_qbukI3-CHrbIdegdJwPQHh4NwIiEOueh2i2PV_7y153Uni_5qBIqxeS87swayvWWZC3c6lnNReP6oW_KRQMAnkc9TtYTRy5f1_6fEo9be1RNQ-bimSdjcWFIbkUaCDnQPbziId5Ouyt1sSBV0K0XqaaQkYxjafIZP_7iN2OHqU-4Vf4tqmak5p1Frk5AqwwNlDUdi9FOiacw2aq-Q-MVzhxlJGzeccFGWNRfS1bfujFjit4e4l4B3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=m8QSvGpdc507OYMSZH5FDcADmazIoq8VBSjAg52RtikaE0uk5xYcoN2HH6PQqJofH5W-EmOw-A9Co9sx8iSUn7d6u2ETf7_qbukI3-CHrbIdegdJwPQHh4NwIiEOueh2i2PV_7y153Uni_5qBIqxeS87swayvWWZC3c6lnNReP6oW_KRQMAnkc9TtYTRy5f1_6fEo9be1RNQ-bimSdjcWFIbkUaCDnQPbziId5Ouyt1sSBV0K0XqaaQkYxjafIZP_7iN2OHqU-4Vf4tqmak5p1Frk5AqwwNlDUdi9FOiacw2aq-Q-MVzhxlJGzeccFGWNRfS1bfujFjit4e4l4B3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=e700OdroctKTzk0BzKudLbuBfxBhh2kIdip4U2xGhQTrYT-MVxAHEaWIhysfhmNUy5YJ46Jc_pXcgdEaouGHRJzHclxTJ__DcY8MTcyz_tWxbh7lUmdckYExx6FTvSlILkDw1ezdYpzfgklwww_GtUPshQEF-k6LEV8i72jFJu4J8tnGPoj9MXUR4yIkKfmc8o2mDxAFk7JtZx0kYhC-iAUufzv0Zm_WvYcCzZnIqNib7J-ZvArm3MK2psaWxAsdMtX9ADOja3Z4LwnmvgQ4xWKQlEDpoEVkmqYOcKBBXIX1t5aNK9OyMLVSQO3EQrIrcSd0GQQQ4roEcaIFl44MjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=e700OdroctKTzk0BzKudLbuBfxBhh2kIdip4U2xGhQTrYT-MVxAHEaWIhysfhmNUy5YJ46Jc_pXcgdEaouGHRJzHclxTJ__DcY8MTcyz_tWxbh7lUmdckYExx6FTvSlILkDw1ezdYpzfgklwww_GtUPshQEF-k6LEV8i72jFJu4J8tnGPoj9MXUR4yIkKfmc8o2mDxAFk7JtZx0kYhC-iAUufzv0Zm_WvYcCzZnIqNib7J-ZvArm3MK2psaWxAsdMtX9ADOja3Z4LwnmvgQ4xWKQlEDpoEVkmqYOcKBBXIX1t5aNK9OyMLVSQO3EQrIrcSd0GQQQ4roEcaIFl44MjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8os8ZvrzZ80YomZNTydt8hXWzxYBzbwhsM-3qSgkBPjBaAicVHpBo2YCvtaUnRTxhWEnOXzazMHH32LV5lopxarXNTatIrtGLAldgiC6FT4sfl9WpJvG2B00amd3yjuXvkjyPvG6rv7monfJuZRwH1jo99hIkk_Ag3qW_CmfwoHEKOHfyx3BcstqoNjBX-0qrtXKXHwr_RnM8LXOy00pqojdb_crQe-1cm1ETEdsboZohy5ACTkGP90NM3Lbf9ZpZltiiDjuXPL1J5qqmTUBg50Qg4KNg8a1APB9kAgutrHAhF0j3IZk5hGHK25vwW7NNuIxlNjO-MRyslDXBZjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=peVf9MCovkk623Drg8VuHksI0XBPGtGgRIaNslp9m6kX3L4_1tZlpt-L-KMzXtm3zOg9_RcAO_1SVk64Sg31s3TUenJXD2O4aBikiE93VCGHfKDM6irsV8SUdfWq2UOHKkM7hndOx6_jew7LtKG9t3XjK9tdsfZl40tQZmkH_CVOIXprPMaTvTwQgP91rHQdXlmeL6wddWdlj_xIoiqoli7z81RleYcOD_oNJVefEAA3owRL0M8b1Ya3PKoYxDnrm7MRv7khsv41z48-vGTe36vWJvVZPdm4o54gar90FheJiCdObnCMec2hHZdpize7x48YX0LG9NOTnpU0vPXa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=peVf9MCovkk623Drg8VuHksI0XBPGtGgRIaNslp9m6kX3L4_1tZlpt-L-KMzXtm3zOg9_RcAO_1SVk64Sg31s3TUenJXD2O4aBikiE93VCGHfKDM6irsV8SUdfWq2UOHKkM7hndOx6_jew7LtKG9t3XjK9tdsfZl40tQZmkH_CVOIXprPMaTvTwQgP91rHQdXlmeL6wddWdlj_xIoiqoli7z81RleYcOD_oNJVefEAA3owRL0M8b1Ya3PKoYxDnrm7MRv7khsv41z48-vGTe36vWJvVZPdm4o54gar90FheJiCdObnCMec2hHZdpize7x48YX0LG9NOTnpU0vPXa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3lEbR6olm4TGPZ0yMzAoFt35fT-MJdfa1n4Nk6WjYNuYbwY9Q_lvhpoMAzp4l0fnr1yERgFugsv1EtJCYuMx_UTnZJkUimz1EdoxL28Jz50Gxc-ZqJcZb2iKvjss3wJtATZjAxTvpbonWao9PDTc3nBeQ4lvmCg5g3aK0otwHUTh_hnz52A0PddB-F0YbX8oA2giQyJAq9joakG1vwKsa-e20qE9cwvHPkWAT1Vb1W4XOPSvCZfXchORz8coedzJTz2_FJ0U9fUsqmINMjCDqGXboQWxGR2bXrq1T1xV2DI3GCkxpN_MvElWqW1HmwJfKfUFcRF8gzmIHRW70LuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=q0C_pK57p0-dcTXaa9VW_2mrq6yPMYJN7mReBS496p4xrZzst-qnxOBGjt9KNtLsnSAUVSrfSe4Y2xxSgNi1W7rP9VQIiyHyqQZkhLD7Ic7A953wrgeBT9bOCB44lPS645D5gA4Yh4vYue6vzIJSUbCDWiFl4csVoqKKlyqLwlxwPGb8l09E4nN_MUHVF_TRpMd2uEQ3M4VXGGTLrO0lZavdBoetMi8kulD1qkXFrRQE3Y5YzdP6Zd3d5VoR591ymcFUry1wZ6c-SS3gLoYIg8hCYb3MkpvTMOK-e4G6ggEDun1ptevfMF8pFfN3LKQHpEEvZA5UJxs7zksXJmeYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=q0C_pK57p0-dcTXaa9VW_2mrq6yPMYJN7mReBS496p4xrZzst-qnxOBGjt9KNtLsnSAUVSrfSe4Y2xxSgNi1W7rP9VQIiyHyqQZkhLD7Ic7A953wrgeBT9bOCB44lPS645D5gA4Yh4vYue6vzIJSUbCDWiFl4csVoqKKlyqLwlxwPGb8l09E4nN_MUHVF_TRpMd2uEQ3M4VXGGTLrO0lZavdBoetMi8kulD1qkXFrRQE3Y5YzdP6Zd3d5VoR591ymcFUry1wZ6c-SS3gLoYIg8hCYb3MkpvTMOK-e4G6ggEDun1ptevfMF8pFfN3LKQHpEEvZA5UJxs7zksXJmeYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=tuFF0ozB3Emm0D4QFgfP2BmJOyyEQNR4cTc27WIB4tg88abCNxMejloC9CCKVs9MGZP4nKsEeZN0hg0txQKCEG8wIm0X1f5M5ECazGoGqixAUOpl7EzW09PEDSdMwJ85o65QHA5Isfzn2JUqP8F8JZG2BNrHEKWxCZ42n6N7YimTtj4RZnAGoZsObegmTNKWWxzh5uwOo9JPqOn5Rq3vijAnIe3rga4Kx5LfBSjptJvm8dUsc4h41WvJ9BcBiSbR0fNrTde4BE6xz-59dI6bRuxSgYP39EZfH2kaELX4hCCAne968WstHNLzyBk0tKJrLt_xo5JnRr_URo0ZglU2Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=tuFF0ozB3Emm0D4QFgfP2BmJOyyEQNR4cTc27WIB4tg88abCNxMejloC9CCKVs9MGZP4nKsEeZN0hg0txQKCEG8wIm0X1f5M5ECazGoGqixAUOpl7EzW09PEDSdMwJ85o65QHA5Isfzn2JUqP8F8JZG2BNrHEKWxCZ42n6N7YimTtj4RZnAGoZsObegmTNKWWxzh5uwOo9JPqOn5Rq3vijAnIe3rga4Kx5LfBSjptJvm8dUsc4h41WvJ9BcBiSbR0fNrTde4BE6xz-59dI6bRuxSgYP39EZfH2kaELX4hCCAne968WstHNLzyBk0tKJrLt_xo5JnRr_URo0ZglU2Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=GeoS-IqiCy8nWPlHzaNRxkh-22R1MBO2SYMP979rUg2mmVvbBZ38hdm7CBQmRM4C60WuxOGP-MqNfpgZEAu-aizk56zXogTL6vAcJJcJxDpmmwZ2yILkunz3-OmxuVkF95Qus-tD0MUqAcV6cPpCm_C5OXXB7gmkzFi03-9NVxkoz2vYbWAdNdoy-bInsB71Tc0yYfCfyxPtjsMGSSqfEKfccGQv50D6EnlHs--7dDJcF10liKWVwr4jtB7p5VpNlzMwv2UyeugQxLvvM0PPFOgGMh5T10YZFdJxLNuHOyjXO1ygB1Sup0DLmYyIo3TxauzRbQQKOA-G0u_yhtJGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=GeoS-IqiCy8nWPlHzaNRxkh-22R1MBO2SYMP979rUg2mmVvbBZ38hdm7CBQmRM4C60WuxOGP-MqNfpgZEAu-aizk56zXogTL6vAcJJcJxDpmmwZ2yILkunz3-OmxuVkF95Qus-tD0MUqAcV6cPpCm_C5OXXB7gmkzFi03-9NVxkoz2vYbWAdNdoy-bInsB71Tc0yYfCfyxPtjsMGSSqfEKfccGQv50D6EnlHs--7dDJcF10liKWVwr4jtB7p5VpNlzMwv2UyeugQxLvvM0PPFOgGMh5T10YZFdJxLNuHOyjXO1ygB1Sup0DLmYyIo3TxauzRbQQKOA-G0u_yhtJGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=mCz8KVv3P98JOP8G-QbKaJytbSA9DWWHj4hFzelVioDftFpYac4CwKPE6Dy4vAG-my_lT7fy7863EjfJVD8XwcYhwr5WwDd4hHQD08ZC4N04hO3GqsX-MdljjmjNFvq4oJRYMi7ga1bnMUQc6aXFMFSN-rbCk_bmN797hLC8E-whh4-nenF5_vPw-lnJJ_SyEzF3JsZPZptf3doC1H1tGIv4MQywlDOGMvWp3FBoaI6ZJyDTQ7sgG74UGBoI479SO0HiU3_EFwB2MB356rB2PhwZB1m-c9IVoZsdfLi_XA7k9Kj4m3Wk3y5U7305Xfm56hj-yhyOe1kpmXgGLrdiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=mCz8KVv3P98JOP8G-QbKaJytbSA9DWWHj4hFzelVioDftFpYac4CwKPE6Dy4vAG-my_lT7fy7863EjfJVD8XwcYhwr5WwDd4hHQD08ZC4N04hO3GqsX-MdljjmjNFvq4oJRYMi7ga1bnMUQc6aXFMFSN-rbCk_bmN797hLC8E-whh4-nenF5_vPw-lnJJ_SyEzF3JsZPZptf3doC1H1tGIv4MQywlDOGMvWp3FBoaI6ZJyDTQ7sgG74UGBoI479SO0HiU3_EFwB2MB356rB2PhwZB1m-c9IVoZsdfLi_XA7k9Kj4m3Wk3y5U7305Xfm56hj-yhyOe1kpmXgGLrdiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=UMmxqGdcUmqJKPrf7jFkFzVuvi4iqK-7xN6wD1SU8J6qQtoZOFfeVIhi9cX-JZwH-TWYrLqJjEkebktUK-IoDCZRA-4x2us1WOwaSBt_UTKfZGecANNJblwyKrLfRhjXAoUsFMWrkTympBMudUg_WP0V1OzmJEZYgdH5M_sr_bkcdc0RSUuXEbBhXuhTsDpudKDPYQD9ypM9gQ4ExN5R9blYm7AyCTzLt1Yu8rDjqCWSo2iVMch61WqcXsmW-KLNDuFsWSd2v-R6pTYsOsn_UrsuNRjdaY4pAnr_yONlEsNnhvBqbT38eyG7Z1n0XOwTDv4spWSuqMEzyon546pWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=UMmxqGdcUmqJKPrf7jFkFzVuvi4iqK-7xN6wD1SU8J6qQtoZOFfeVIhi9cX-JZwH-TWYrLqJjEkebktUK-IoDCZRA-4x2us1WOwaSBt_UTKfZGecANNJblwyKrLfRhjXAoUsFMWrkTympBMudUg_WP0V1OzmJEZYgdH5M_sr_bkcdc0RSUuXEbBhXuhTsDpudKDPYQD9ypM9gQ4ExN5R9blYm7AyCTzLt1Yu8rDjqCWSo2iVMch61WqcXsmW-KLNDuFsWSd2v-R6pTYsOsn_UrsuNRjdaY4pAnr_yONlEsNnhvBqbT38eyG7Z1n0XOwTDv4spWSuqMEzyon546pWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=BWuKqsm4z36m3ebP3DeCbnTezNqlR6xhxWtUAxHByAeq2Q1EyLItDXovbT_0sE6JABSL9v02BwdfZiO_fTHOT4Jsgz94Bcm4VQlf-pUl0FPAPSxn3dm0l_iMyXgIzNmdC48D0DT055I1bkTKEEMHgile2QqCnjSjpf_ww61OzMQGardLOGiJus5sQOeyWZ8eZtYa1KQFXAaKoluqSrgkpx0PNUdT1LTMRM8ZJzI_TcAe1_qffxXI-EzGzho3m1PMZN-PGFaSslb_J6u8ban0YtIm7bvfU4Rm6rRB-_TQV3ztAA35OkvmZrS-NZThWK--8CAfhjdkFaGmvkKvgt3uGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=BWuKqsm4z36m3ebP3DeCbnTezNqlR6xhxWtUAxHByAeq2Q1EyLItDXovbT_0sE6JABSL9v02BwdfZiO_fTHOT4Jsgz94Bcm4VQlf-pUl0FPAPSxn3dm0l_iMyXgIzNmdC48D0DT055I1bkTKEEMHgile2QqCnjSjpf_ww61OzMQGardLOGiJus5sQOeyWZ8eZtYa1KQFXAaKoluqSrgkpx0PNUdT1LTMRM8ZJzI_TcAe1_qffxXI-EzGzho3m1PMZN-PGFaSslb_J6u8ban0YtIm7bvfU4Rm6rRB-_TQV3ztAA35OkvmZrS-NZThWK--8CAfhjdkFaGmvkKvgt3uGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Nt2FLOCiPp0KOzLRU6rf9SVvpSUChja4OSpSPWqlAAeDNxNy2vIL0lxqcJN_N0vG8XESJbPqVCap13aILHDTi-BQyVwETmrGr3Fp48rnpHRrfZI9snzEqLoqE5MNeRkFjWYCMUtUKLRzl3Mq7htgTkK0MVzQxeRRUkjbVAaPuzLFfL2U0YLcky7ILgxoJhnXzL43-ye8HJO-0xcJzx81OW3X0dq7g97p5yF3unFqCzZqIRUKq8xHv-kLB6UT8VrUPCYDstYUR_WTOQwh8U7Pij6lmNdQCKw_W9LGeG95hb8T2Mc3Myv9P1Jf2a3fzyMxRgL8QUp8WwfG_cURsQe4_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Nt2FLOCiPp0KOzLRU6rf9SVvpSUChja4OSpSPWqlAAeDNxNy2vIL0lxqcJN_N0vG8XESJbPqVCap13aILHDTi-BQyVwETmrGr3Fp48rnpHRrfZI9snzEqLoqE5MNeRkFjWYCMUtUKLRzl3Mq7htgTkK0MVzQxeRRUkjbVAaPuzLFfL2U0YLcky7ILgxoJhnXzL43-ye8HJO-0xcJzx81OW3X0dq7g97p5yF3unFqCzZqIRUKq8xHv-kLB6UT8VrUPCYDstYUR_WTOQwh8U7Pij6lmNdQCKw_W9LGeG95hb8T2Mc3Myv9P1Jf2a3fzyMxRgL8QUp8WwfG_cURsQe4_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh3vz3mFfRbXItIQrQXpy1eyljAk1hkgxRau2DtsUqPv4_F_j-xEsFs3JKXqk8q1Hy8SllgXAuK9VIssZiVq4z8TaWZILrSn-8Lb_-zgRcVSGOa5aQ8kLTWjF5n_3W1Ffp1g5WUSQ0sdFhp4ZG3zjy2AKL6zPvJM3gbabgyr5vxXIp4qDgP4w3H0rPPS-SqPe1wy8sESAhtElUlwnA5D1I0EPnekTfcPMhaZcK2mlU4NCSxJXb4w_5RcSzksoXuMhB3vTHVyS-A5UKgSOxJW-R0bhfwcXWNf7ii-rFMVfEauCpQi-WLUKj3PeRKOmP1Qs9batFuoIpKk3CXc5Jmf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKWYdVFk-fhWdl0k717sXSXw7mFfbELqUHYk_Qo8yT595jd8KLNXKhEfz9Bes02lQbvka-jQaLcQhzqKBAAfrBQM1aYXljP7LtH8nbXT6B0Y7OJ2aIhVHBW89mx-ORpptqerJDNKiMwD6z6XK6fYY7a-c8XZEHL5459dzaKtI0Jo6o7L0kwkAE4zik7wmahVudLfaF2xxOjJp1xXrJgoVNW0L1CXH20mOTdH_msFxZyszKIpb8VIKeAoCacImtQzCMCF3YtBhjnyz08NEGNxWBDIXxhmEMu-8gD_GBAO5Zz9Gc3aeLqMuyRJCPRyu9RxFDCgBhKBiYu4MMDvb2TT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=DN0iqDtQsxy4k2yn7vrQF6IQwlUUP8EBlL34KhYxTUJPG3UkAQdWp5ychtwYpq-TLRvUh0Z-S8ew-Kzhi5iusUyIeQAZmIbA2T3qd2ZDkEVhuxMkUqXRu2gaNxDp0LcwdD_451mlmtFGTPMjqP5kUsjlNTVXE4VLrF5M9gkZiM8aZIuTX5gf3NsV38QJlYbP9sUHpdocJ7ifCigUFvoPHh2dyhXGLgxpm67qVyz8v7hhqcFNm430KIf6ACu22UyD-DJ1vLkiT2t16G0Awf0V--tukMiVYQhDxRMj2bmv2-ZF4WOqUPw-mE3oQQyBYJ0DFsaroCVA1J28VgZyiyrpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=DN0iqDtQsxy4k2yn7vrQF6IQwlUUP8EBlL34KhYxTUJPG3UkAQdWp5ychtwYpq-TLRvUh0Z-S8ew-Kzhi5iusUyIeQAZmIbA2T3qd2ZDkEVhuxMkUqXRu2gaNxDp0LcwdD_451mlmtFGTPMjqP5kUsjlNTVXE4VLrF5M9gkZiM8aZIuTX5gf3NsV38QJlYbP9sUHpdocJ7ifCigUFvoPHh2dyhXGLgxpm67qVyz8v7hhqcFNm430KIf6ACu22UyD-DJ1vLkiT2t16G0Awf0V--tukMiVYQhDxRMj2bmv2-ZF4WOqUPw-mE3oQQyBYJ0DFsaroCVA1J28VgZyiyrpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSLfps8gwpdrRDgZrImP2kPBmADYL6dG5agKinXlRDuMgOOLyIO67F61u11KV_0Vb3uYIRugKbPXX_j8pVGoDF__LAn5SX53S9blCN40d60dS_A3CC0nD9EjlcY3iwErlpzp5qHD-o1_D6jmMsn57aei8jyYTQmuv97gDj2gCgGZv5ynFL8wY3nkmgMr_WAJfNrvYqjg3WeGR5CaY8x2IURXbFgtIqNIJoAPwaBnsry3tbvhJdBBPtxQnMYAi7YXEe9w3U9ae1hmStWrMUI3H0cekQYl832Dz_c_x4CIWxC9YvdMibrcalYe97_glDPRDEkFKsBdSeT1hl-5R1XmTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXgfQ0lUB_vh09REYLdu2_y3O8EdF4kleUTlgXdO8Lh8tmVysZ-UzSBzuOQ4mLqZYDckY4zp7klZMHb7vcGeHqJGX5paf8oNfCjku443npA2GvPOa8XZYsyUUirs43NrI-qjopslAZ-bV-n6bwVQC8lQkxa2_PfO3QJ6sn63BZO0hReI4cWpWlt0kB7WXJwiuHegl393zpbmGtMMysS9MRQXQ-TH4fYqJodrCS9MFlxnMgavyYX5TcZaGjhJeZScEXVeqyvk-i10z9fVyua_s3V_LDTE_XrG_4GFTJBVt_-BqmJ8eQaeoof_ZyIKrJ4sjD_NdvkrG9U-tD02l255pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=GdiMK0ezvIv5aHFsHyy0wncG5CNK6ykXAChTB5y012kwSmRHg1YdPc_N3LpZvaEvAhIePrJLODt5mkXz-jLnmXzvuaWQ9Ch6gEN6TtYW8ShP_-Ergk7TnW_EA45TMXSLPkAVvrqzd7iu-zlkwaFYPbsoEFZnCTfCvSITbXcG-8eawYA-9_ATb2ba0xdonvCjuISE2JDbCM5CqmLBJcs4YOr1OauworZsyQh_stoU4Uhx-C6VQCTi8XGCavMzSJ5w1NoztaLQbU_8TM8Fb826st9wdNXuL4retkzbVvreGac_5Tl6_XLc6CNitWZ52Ai7kuFuLbfKGkVTR_mEpZg6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=GdiMK0ezvIv5aHFsHyy0wncG5CNK6ykXAChTB5y012kwSmRHg1YdPc_N3LpZvaEvAhIePrJLODt5mkXz-jLnmXzvuaWQ9Ch6gEN6TtYW8ShP_-Ergk7TnW_EA45TMXSLPkAVvrqzd7iu-zlkwaFYPbsoEFZnCTfCvSITbXcG-8eawYA-9_ATb2ba0xdonvCjuISE2JDbCM5CqmLBJcs4YOr1OauworZsyQh_stoU4Uhx-C6VQCTi8XGCavMzSJ5w1NoztaLQbU_8TM8Fb826st9wdNXuL4retkzbVvreGac_5Tl6_XLc6CNitWZ52Ai7kuFuLbfKGkVTR_mEpZg6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=cGIHUXkafx1kWTaCnYGo99pqvKmlltpYoFQlWqiOXWCkA8CQzX_Msp_xRYCDNS5CyQCXHAtZgLe0Eaf62F3VcuYu7pm-DAaTrnSWZHpujdJPBDb-bj8d0Cw-j7-SFyZe0WA7aUgzNu8fqGNG4dnpr3sibJDG2nDBn2m3Jgih-5nXpJy717P1QDoTFKJW_tBZQsIBZUKUmIhvuYFjMefTgd7wk4gDb_CtestM6y0El7THPVdTeEoOG5aguBiwSyG0XAWcGbAlpq8UzDu8bL7cmJeFxpPyqDl5RYvPpyGoUlwSXVWqlEbyMS5fvRVjwQrfFcsphGKlrZb2iHVaVTOOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=cGIHUXkafx1kWTaCnYGo99pqvKmlltpYoFQlWqiOXWCkA8CQzX_Msp_xRYCDNS5CyQCXHAtZgLe0Eaf62F3VcuYu7pm-DAaTrnSWZHpujdJPBDb-bj8d0Cw-j7-SFyZe0WA7aUgzNu8fqGNG4dnpr3sibJDG2nDBn2m3Jgih-5nXpJy717P1QDoTFKJW_tBZQsIBZUKUmIhvuYFjMefTgd7wk4gDb_CtestM6y0El7THPVdTeEoOG5aguBiwSyG0XAWcGbAlpq8UzDu8bL7cmJeFxpPyqDl5RYvPpyGoUlwSXVWqlEbyMS5fvRVjwQrfFcsphGKlrZb2iHVaVTOOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=jzjClIErm-Awd0Zrq-DJo-B8As5gatV62heUSEoDdss1QQYEvhkUCsSvVRIW2NfRC0FdTMLq8kj6TWzm_56W6-Sfm3l4Q3qMDab0dXJzr_zJueV4uP8i3QOBsw5c1MNUEBB5eZxUuzmQFmzOwLLwLEoRKvVuN3fkBvbBvzuNC54F6HsfqoMHAk64jIRuLUJ0oBwwGuQV28OqJQkbg3GI4hzkcAG0zFtcexPHbohRH3QmjZYYacdbaLB4PxNmlhn6ku7ArLgFeyGul2usOE4Gny5-wwKRMHQm62m3TbN45R_nILaoj-tkKbKGhaL6GrjjD47IwzQ0UJ9IF1Jk4xZnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=jzjClIErm-Awd0Zrq-DJo-B8As5gatV62heUSEoDdss1QQYEvhkUCsSvVRIW2NfRC0FdTMLq8kj6TWzm_56W6-Sfm3l4Q3qMDab0dXJzr_zJueV4uP8i3QOBsw5c1MNUEBB5eZxUuzmQFmzOwLLwLEoRKvVuN3fkBvbBvzuNC54F6HsfqoMHAk64jIRuLUJ0oBwwGuQV28OqJQkbg3GI4hzkcAG0zFtcexPHbohRH3QmjZYYacdbaLB4PxNmlhn6ku7ArLgFeyGul2usOE4Gny5-wwKRMHQm62m3TbN45R_nILaoj-tkKbKGhaL6GrjjD47IwzQ0UJ9IF1Jk4xZnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osXHFxZuhH2TnhbwTw5VdrtgSvPCFkTiTwaT7BwRcPUE0YSNS2BohvqxSRrzsFBz62bL3gBYqFMfovCq_kmOLxrhziiu5uwrOj2kfJU03zIzBEcOV-iaIQM-TyK6RMbXrdEivFszicGTm17iLKMmJoXDU6y3XyALKFmM2tMSV9csC1dZoGfC-L2vCMaL6QDZivQDIV1cEFNB5wUcy_JkaHYm9rahSQ-CInB56s7RgPii87bBKKzD05O5HlvtNPt4K1Fj2zP6Jfkv_RDP5XOv1NXTBuMZ7Y_d-LByPuaToO7fzcWyInbPDFu2jEjBkgpZQWcNrRxtBwiOR7vszunM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL6UHSsh5lAMNgWCSdNd5hJcz9NplfLbrIqURelZr10z5oMErlNb9K9pVj2cjHjTkDOFnoOsicIkHAGy-6bHXitlZwGqe_hr9Rq5A_D0sVMOGKsY90jV9SrjpnIIXGt3md-n-aizw82z-1YOaLwbEB0ZifwVmnErT6vnT_q8Xslz7xA6JAoGV2hwWGlVqC8Wnxgritpf_PO3otmSw9-mTqvjaWayk63cdI5iDYEMaIzZ5TqvXJUIdaPDttslsvu5H2WgwHO-QO8Rn3rcME0kKGfLIP1cD4o9SQxWgCUwDaP-MxufegoWfHLWah8GG70uhBqOG0UjQbG9Oh6qkSfolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=GoP4jswbUoYFBWbOCLMwyV7Ui1T5CXoEhQa3rwwLqi7kIG0jU0Uveb1O_GXhJWCltqP8UWP40PnilGFeti_edzo4KojWIVJOVACxOxNHBDk08RMn9h1L5Zjs26BVUKJRhCLkpnZUvv06XdWEkiKDLtd1UdAwEux5Dwnzr7IkYtRN6g0h96_szxA8SM9ks5qsU4GQMWrVBXmcM4V8md-kSsfnDGmDvTMJlfUVYpOb0itipMs91z2pCKhKfEpGCZJZIlEgP_QvqlBBMjFv07by7jp7LlMAs3yEDhe088ePCzagopHL5DzYGvl_Bhs2B5YQaPOE4zVL-v0EDlPCoRrWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=GoP4jswbUoYFBWbOCLMwyV7Ui1T5CXoEhQa3rwwLqi7kIG0jU0Uveb1O_GXhJWCltqP8UWP40PnilGFeti_edzo4KojWIVJOVACxOxNHBDk08RMn9h1L5Zjs26BVUKJRhCLkpnZUvv06XdWEkiKDLtd1UdAwEux5Dwnzr7IkYtRN6g0h96_szxA8SM9ks5qsU4GQMWrVBXmcM4V8md-kSsfnDGmDvTMJlfUVYpOb0itipMs91z2pCKhKfEpGCZJZIlEgP_QvqlBBMjFv07by7jp7LlMAs3yEDhe088ePCzagopHL5DzYGvl_Bhs2B5YQaPOE4zVL-v0EDlPCoRrWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=KU3QTViUp6FTb0-68urwGI7vEaiZtsiUZSn0m2hzIXHaGVITqqxl4QmCqjGdiRwubZKSrbxIuPDwEDSKm6A3CZwFKofC9n00GBgQBHHTQlgzGUNWAGN-c4jxeI8I-gTXPYBiI2WhAbqFfXEpg28CvcyoWePUuN9hq_cv0azoqHyBdtZwDbG4qmFSQG-qIoOX2ea5g3xcPcYPORerpPtNpf5PmYt3_68gODqCszJDA2_h-i86BpY2Hx8l6KcThiXNvvupNEyovnoXAF7i-TJy7TesuOylwzv7S_di0LS1Jp-aTO6iGdMsHtcdFB-YXUEexu-53zkgn81IyycKffeKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=KU3QTViUp6FTb0-68urwGI7vEaiZtsiUZSn0m2hzIXHaGVITqqxl4QmCqjGdiRwubZKSrbxIuPDwEDSKm6A3CZwFKofC9n00GBgQBHHTQlgzGUNWAGN-c4jxeI8I-gTXPYBiI2WhAbqFfXEpg28CvcyoWePUuN9hq_cv0azoqHyBdtZwDbG4qmFSQG-qIoOX2ea5g3xcPcYPORerpPtNpf5PmYt3_68gODqCszJDA2_h-i86BpY2Hx8l6KcThiXNvvupNEyovnoXAF7i-TJy7TesuOylwzv7S_di0LS1Jp-aTO6iGdMsHtcdFB-YXUEexu-53zkgn81IyycKffeKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDbDsU_BwMscApdqxxN2D9ZvAT89LR59vU36pfEd316Qej6u_n6SvpSwEp5l5oxKFSXiDqdo0woN8zlxTkjXfgAp5-qgepz7eMLGPszP3u9vVsJD6n9ZRWgr2Grb3swWvIjJ2jNBCcgSpBcGxzGy6bKl_2__gdP-g4Lmx7V24fAgOSzSbfU-0s8caZkAYM9Sfz-hhD8uPvC0RgTyanCO9Sl6IdzCD27E9FfjvO2pSV8jJeYmMvPyJpYmp_3oA7gQoWRtLTxIXTnTREUMjAci6oI1Rg_NG25ZbD-CftryP3sa_4CerK9FqDdr-gDP_cPSUOcBnqEmoVeXj5R-sHk4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irOn-jbUtWcm2SlzikdBdxEQ-HeDDgV2YErtmUZU1WzAbqRtHYZzUSKbkVOlzIlRm1fZDCPb8tlzt2taDoZCPGkBODjGcsFYSabHYbhXVW-g3qn0c0S-AWiW8Y-0njAFgxI8uMeFRreGaD4X3W8PmpYc2EdVgPpMDzr3M0RDzLQuBZMyMyXjSNFX_Ro8bb8w1rI25059WzmkVI4KPGA7gxILduF9foHttuPqbfs3Qsmz2fpis6bLE5RG81M9N5XjJx2AEt02KiEXp9qGxT87Vbu3546zD6iyUP3WQXkZ6q9CJ8-gSCgGc2HVoBCOq6Sre2ZkZsHNtdeRkH8rW_yRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPnY4wkfvfSDhLi91oPFPSTkuj7PBtUL8V5HLWonaqa3xtUrON3awROu7hqvcv5pI99A6MvfLYe3vhJr68A8JP5qOIZiDYAG4EKT7n3ZvnvwCG6BAeObeeH4hZ2wUPehGHuTP8x5XmqfPv9_TdJx1ew3iP77vRirXKiCj2-aBrUkIBlH5C1frO5ea2jqN0-RCq4J7y62fROJG_Cbn5hYnU-MorVVCPlCqjlIp09Ej88Irmp3IQgbt93kEjGuis-wsVz2g5XJCMoDi64WRPUZMFC_ALIu9KR66v9SZ4Vi6QUTdSFTNLBbNmGAllUkkrxsnSY8uFGLrVpgMBZDrNSg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv-WaWcgVSSViNFxSf9uoeWZHsUhxK8Y4IXe6UwUJs-9Sn9oXXH8XapuI3o6Ub7VRGeiCoZK2y2epHNp3pLPeqpMqt5dhCQD3R_9x6BDc2rkzytPfBLcTnM8oSAOh02OeuRk5TDtyPF0vY_aYVdP2pitTZkKRtltRxpGVKbD2Dnowu6ARELnuc6ocPbV60h5xl_apL4jaJojoenWcndoKjZ0RQzUNuHaMUwgb6YTrDAfQDBtOVPI6JgT8SAeDte-BiIpaU58Fss1S4SfUftYinCD1EQpffg_mH1WOV9zX98AuBEwkyRwmS-M161oBAf3kqZhKCQLnHzWdvWw8B7trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXP1rbwV1tbp2Ra5g5Iw5QgzNS5MKKDL21ol6K2sbgtGp2b4qNVxfCY_vD52k8moP3HnOxZrmbuPAtOX62GwINjBEfyIzc2habMjpHmAUQzXxBEFayFuKeHYYxUTBOmivyEadmW6UgzwJ0c4rmIn8Baf6t1t2MpjF_L4Ko1FBU5Eyw7Tk9XDBMzXQt5JJOWeU5CyCOsTqOCg6uyDszAyagQ373DWX2UyINYRz8Qf8gV5cuzG4dHFu4oaSacmBrFYt0QG5OcVxdjLo99EMrqlla4wp6Vk3zJMXUOLGFGNx0DRO5SNaxAIlOVzgHvRHu7r2kvnxRfORSaA_QlSNylFUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN2prwqz3QsFrIuVXXaNZAzAwppG4Hm3-mjjFEKIzp_nuA0bNjhZvw0MccYihWbj-lMwsFpPxdzl9mD0XT8rw6Sa1Ry-Q7UTsuozxhdg2PbTpQbUYYGVMiI2Cs6MFoJilcfrlt7EfR-YYDPAwfn_ckV5LKnqr4OrBT1pdvVh4oi55m9B1OvIXvoniFTiWVPEvLO-kLhi_EV5T4SzxQPqEHIoBbGeDN3VXGOiiVnaCj4JvOZRZ4HsZ8nz8lHEpIgUoFuyBSFMQ_lxrrbPfKfC7hnNSe0EkFJz27eb_on9aL2ZJdI6bcfwMHPpdfhMrCUUZ3bNvLnMSOfKE_Rmx1Xt_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=sz8lAYCxVrlp5yAsm6uEry1oH8O7kTp9gPKXqI-1hcH5aYfmXAMxH0shncIKNFCF0O6AMM_OcPf8b9V4pjHhfRglKfHh5pNNt84Z0Iya--OD9bEVsiyj0CBKImlfTi7qI1VL447CsrPY6uVFlTRnq_Ai6H1U9lCox7KB3hoEtjP32o0wp0CivpOWkoHZFSUwXk9qsGq3VbC4wP-PNuHHwAgUibPL2Z_bIOY74OmA_eEPxwEu2o6-6RL36sB84tJJ-caHhHQmA0fBt8-2MKVjWTOYfAC1oec4sit1s1pu7jbV1Fp7HKhr6V56jC_R18K1xqHkUilwxtkLCzCnq5t7bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=sz8lAYCxVrlp5yAsm6uEry1oH8O7kTp9gPKXqI-1hcH5aYfmXAMxH0shncIKNFCF0O6AMM_OcPf8b9V4pjHhfRglKfHh5pNNt84Z0Iya--OD9bEVsiyj0CBKImlfTi7qI1VL447CsrPY6uVFlTRnq_Ai6H1U9lCox7KB3hoEtjP32o0wp0CivpOWkoHZFSUwXk9qsGq3VbC4wP-PNuHHwAgUibPL2Z_bIOY74OmA_eEPxwEu2o6-6RL36sB84tJJ-caHhHQmA0fBt8-2MKVjWTOYfAC1oec4sit1s1pu7jbV1Fp7HKhr6V56jC_R18K1xqHkUilwxtkLCzCnq5t7bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=sYbUXIhKefimQDjWMB_rvmLk-f5zdpMIdvX2ghWe8m7AMDJSUoxuCR0chjqaIbHW2Q6DMuX7OXO-8wlVc4XUgKqqMWyXl1KgFSC5H7CjLxMvSdDdR8HbYEn8p3HFLoEKVaucq3sDI4VSWGkAjZwVfBn1xvYNpRSrST0YzGm1qy-FBD3pKxmUDE_EmVaECwbtzZA_6bIbNE1q4BuwOHm17JbvMLuTFdxDFc_hVas5rkvjSTo7y6WhkyKyKZZZoFSLQIrpvMcko83l4okb5VN2gdTs9hbdCST_wm4Q0PW1R7IzHbq9SPPIpSy6EBrhsyrYQ0aKMETjJdLbdcOKBphEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=sYbUXIhKefimQDjWMB_rvmLk-f5zdpMIdvX2ghWe8m7AMDJSUoxuCR0chjqaIbHW2Q6DMuX7OXO-8wlVc4XUgKqqMWyXl1KgFSC5H7CjLxMvSdDdR8HbYEn8p3HFLoEKVaucq3sDI4VSWGkAjZwVfBn1xvYNpRSrST0YzGm1qy-FBD3pKxmUDE_EmVaECwbtzZA_6bIbNE1q4BuwOHm17JbvMLuTFdxDFc_hVas5rkvjSTo7y6WhkyKyKZZZoFSLQIrpvMcko83l4okb5VN2gdTs9hbdCST_wm4Q0PW1R7IzHbq9SPPIpSy6EBrhsyrYQ0aKMETjJdLbdcOKBphEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=aFSWxrSkGwTE0DwJlfu0RhxgFQDPQV27mLO9EEBk-3R91ci3EWVd4Vls7SN7Q3DevgaiatPbKea0lLuO3l8Ir3fWRFIuhnMDTSGhK-HSq7EO1iebTPH_7L-mOXhgCFlXwKFG3KXJjBJGppR0lZNS0qdo8_gJganKvuCFGBg8xkwX2eJBx9XkyxYop1YYWzIr7RsNFM9hhIc-zsqtLWHOv6w2OWYPrF7LZNIqXxbPTvk9odWx2mqf9lRlMJmRqe8Ft_4tMwtbrIYpfreYYEwvEHlPjzhkNfRbN-cK5EIVc2bR4U2oH3YyCyt_8gxJpD-GfAi3-cemaANxVZNcc5ih5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=aFSWxrSkGwTE0DwJlfu0RhxgFQDPQV27mLO9EEBk-3R91ci3EWVd4Vls7SN7Q3DevgaiatPbKea0lLuO3l8Ir3fWRFIuhnMDTSGhK-HSq7EO1iebTPH_7L-mOXhgCFlXwKFG3KXJjBJGppR0lZNS0qdo8_gJganKvuCFGBg8xkwX2eJBx9XkyxYop1YYWzIr7RsNFM9hhIc-zsqtLWHOv6w2OWYPrF7LZNIqXxbPTvk9odWx2mqf9lRlMJmRqe8Ft_4tMwtbrIYpfreYYEwvEHlPjzhkNfRbN-cK5EIVc2bR4U2oH3YyCyt_8gxJpD-GfAi3-cemaANxVZNcc5ih5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=MHkK2g_oGyl_J1xchNhqPICo-9d9v67yyMgXDQ3OaSzl3LRVTOwUT6D3X3YOO2poh8zinXSeOWn7ToNTqIleCfTO0PT43hLs12KTLF5dxv_aAAIGIX8aaaN5M1zTISQcM0o9YD5wNc39WWhS3C3o3wrkhgQc9JyGAd2sdEZDpY5WpvcdMS3Ab9GYtXl8taca39n5cbmgXF4vBZdk9GjIA9wf7bHCLojqHWq79nLGbrwDPwQhwaiKBGED3d5nINh6ZiLm2DCoUSmyLyzgaK4T7p_oDHIPvb0SOiYQFq5GaWOMuNc8hDjEJ33l_ATorf6GuZ_NMzQOvdF_HxjT5ktkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=MHkK2g_oGyl_J1xchNhqPICo-9d9v67yyMgXDQ3OaSzl3LRVTOwUT6D3X3YOO2poh8zinXSeOWn7ToNTqIleCfTO0PT43hLs12KTLF5dxv_aAAIGIX8aaaN5M1zTISQcM0o9YD5wNc39WWhS3C3o3wrkhgQc9JyGAd2sdEZDpY5WpvcdMS3Ab9GYtXl8taca39n5cbmgXF4vBZdk9GjIA9wf7bHCLojqHWq79nLGbrwDPwQhwaiKBGED3d5nINh6ZiLm2DCoUSmyLyzgaK4T7p_oDHIPvb0SOiYQFq5GaWOMuNc8hDjEJ33l_ATorf6GuZ_NMzQOvdF_HxjT5ktkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=iJK5shqaEtgbjKXt1Mf7dg9zpolTl4PPumGsMdFOyHB7JbSPtO9gSrbOAul0TAW_MhlTwtRQccel5Qgl0jGD4JJLk9SeKl8LgG2APJE2QDynOxoIxhpzjxzrA5ObaET-HpVNC4MM6bVkL0e6PIqAIOpu2Zamg4qD0gy0SSFOg3dsbxgHoJyav4j2B3b2QTi7LJJI6W5X9lPgaRcyFH9zqZTaEzXzn-LXAyhqK61R6stlUWOz3BYLWpCQhNu9RQEalSgjP8BNW05e2U9ecwfcy_SRk0ZgLeEcaoTtRl4ZUQaxuskZ7v3dRhVbMloGGW2g5xKuoRznm1WVd16-y9FMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=iJK5shqaEtgbjKXt1Mf7dg9zpolTl4PPumGsMdFOyHB7JbSPtO9gSrbOAul0TAW_MhlTwtRQccel5Qgl0jGD4JJLk9SeKl8LgG2APJE2QDynOxoIxhpzjxzrA5ObaET-HpVNC4MM6bVkL0e6PIqAIOpu2Zamg4qD0gy0SSFOg3dsbxgHoJyav4j2B3b2QTi7LJJI6W5X9lPgaRcyFH9zqZTaEzXzn-LXAyhqK61R6stlUWOz3BYLWpCQhNu9RQEalSgjP8BNW05e2U9ecwfcy_SRk0ZgLeEcaoTtRl4ZUQaxuskZ7v3dRhVbMloGGW2g5xKuoRznm1WVd16-y9FMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=oe7sQNrAhfLvLCrZKq5tuNd8No6dtSd7HoytaTdNeenKSno_Y44KWvIPhTvmsXhOyoZBe5cCHfpTZzG-1gvMVUaN0yp69qiARQ-yHk8dXLARpAA-sWy1s3itQQxaX_b7Dwgsm32JxCrQ_f9KIk9ZHanUaJTnmHbdp-F71IIVbHHhA7_dUIhbNGip1HOo5hD73ZELEbpWnK4PVZdkqhu86OTrf60NBNdEg_CoqPwdhb-tjZ6mAOgvENbaanY8-jjdKAAD8mVb7Oq4engvxO7WNdnahHKgVeVfAZYyi3EHMsb6xFwYnlPBHa7UecaqNeXXjeCcwi-LzECn4lze7yfDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=oe7sQNrAhfLvLCrZKq5tuNd8No6dtSd7HoytaTdNeenKSno_Y44KWvIPhTvmsXhOyoZBe5cCHfpTZzG-1gvMVUaN0yp69qiARQ-yHk8dXLARpAA-sWy1s3itQQxaX_b7Dwgsm32JxCrQ_f9KIk9ZHanUaJTnmHbdp-F71IIVbHHhA7_dUIhbNGip1HOo5hD73ZELEbpWnK4PVZdkqhu86OTrf60NBNdEg_CoqPwdhb-tjZ6mAOgvENbaanY8-jjdKAAD8mVb7Oq4engvxO7WNdnahHKgVeVfAZYyi3EHMsb6xFwYnlPBHa7UecaqNeXXjeCcwi-LzECn4lze7yfDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmcYLcF4helLJk0ol5h9vOhUIdYpRk6xpg9qY0-orwictHurNoxmWcnxBuiQhmnneyUnzBkRyWQjy-NE-zGnhCIDO-24R5dCkIR0AhggXfIdQDE2097w6gCe2VgsxAwvfsClLJ8Qv2oqSreCJCsxwfsHPE5VUVBESXcPYCLIrQ8D7uGPVgTPr3RMIrdWKOtNN-7nKTiI6VYTukut-5NwlO2cZQbbdtaNkzUaubLN-9qglY6rQxro46IFlnGjJxl_OSom9GIgqHSOcH2kJnQs-YglpYgy-RKyO07GaZtr1RdVC5s7jhlEv7MyNkifusa_e_hmGmhwXs4yozpLjSNu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=U8bAuZNEL1U72oLNwucaGB53OJOdPCiOhlZWDH0cA09Xd7SF4sM_6l74D40WfhQxWuoOPE09UJFfTb_et6PVgbqVd23WsHZR54FCD6p0snZggKPwYuSXMC3jKNuaWg6y-Zdq2olRAsfE8zg7z7cTev0VPa4dMhn9_zKLA6gw8PhOtKQFmSTT4aLozTFJD_y_BR5sCpVAYBWEZENNuw-dQLZ80dDt5UKtF5s94rFY9rYur3zyB3jLBkWQTr6i50lA4OQ3FRk0I-hmQtk2AOAcoU1NQh74YMP8Diuu0smjPALIwcvEEkfWnmqXZhyo3r-ve3laifHlASVaF4mh-txIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=U8bAuZNEL1U72oLNwucaGB53OJOdPCiOhlZWDH0cA09Xd7SF4sM_6l74D40WfhQxWuoOPE09UJFfTb_et6PVgbqVd23WsHZR54FCD6p0snZggKPwYuSXMC3jKNuaWg6y-Zdq2olRAsfE8zg7z7cTev0VPa4dMhn9_zKLA6gw8PhOtKQFmSTT4aLozTFJD_y_BR5sCpVAYBWEZENNuw-dQLZ80dDt5UKtF5s94rFY9rYur3zyB3jLBkWQTr6i50lA4OQ3FRk0I-hmQtk2AOAcoU1NQh74YMP8Diuu0smjPALIwcvEEkfWnmqXZhyo3r-ve3laifHlASVaF4mh-txIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=c-dmK4d1H5AoNnXJLuUd-I-xIgilfa_83tm0OFogsH3RHXQ_N4L4ctQ-awXYBOk_NKjgeYs-KWb06XaHc-vLuLfXT9ndqbE3Z68U4j0wQ6QdwyhvTWqDz71mEaRxi0q2UwlbKSGSJ1Dm2_Ea8nXtpF86yQIMAQ1hpRZ8LRuzZHT_K7QIO55-QIQ7n3MOGuqwgo5xfxksdXz28GZ8nGJLovUu2Vl6MCUSzL6tYMUbWlOI1sbhtFlh4AnGn5gOmQa0FG46HLmsjnvf3E1USwc0DjZlziiiHuqRbfLn5zo5JyZnLt6IhSG1ZiMGstekX9Fsxu5CgfpPJL_8FoJ8pQTtrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=c-dmK4d1H5AoNnXJLuUd-I-xIgilfa_83tm0OFogsH3RHXQ_N4L4ctQ-awXYBOk_NKjgeYs-KWb06XaHc-vLuLfXT9ndqbE3Z68U4j0wQ6QdwyhvTWqDz71mEaRxi0q2UwlbKSGSJ1Dm2_Ea8nXtpF86yQIMAQ1hpRZ8LRuzZHT_K7QIO55-QIQ7n3MOGuqwgo5xfxksdXz28GZ8nGJLovUu2Vl6MCUSzL6tYMUbWlOI1sbhtFlh4AnGn5gOmQa0FG46HLmsjnvf3E1USwc0DjZlziiiHuqRbfLn5zo5JyZnLt6IhSG1ZiMGstekX9Fsxu5CgfpPJL_8FoJ8pQTtrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B18G2wE8qhGhbn_A-0zj0Ih_keZoqsA5ni0xjaUOKI1G9tpmPkj6mrXj6A48cO520G7WDvXp_Yew3502SNQ_eHJfIpnZsIj-LSTt7njQE6nb8DeE4XbtXu5SuTQVTrZUiO2QoRhRI3JPVluU2RT0UMg2GHZyY4mS80k0edTMYNOVxzwTFB990ZCJSoXi_JQOBw1sj_HVKHqf2TbRuhJaO8NyN--SveQGB3icuL8DiS3-JOV4sQboIZQ80o6aU95AqKhqpuFO_cTsYkUwyzKj2t79Zuh6tFUWFk1bnOvX_MAnuCQqK_gnruPUbLUiWSPSPnfvJAsxQfowJz2asQCGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0whSwa_95xa4fU4AQDV4rTmw87U4EXpqXYAs9K6yQ3GGVjx09lxHug_mykzq5kEeD2oH0ySK6oncOYIwVBnv4icVTFZD-k8cAiUsrzTdlP4tiCcrnQrlXE1b1ikPKTy97mPM8FQrmbGo3Mf4H87FtGjyobuajK-5MZHTQbC2wGCVw9s3rcsbQIvJ4XkVJqYkFBTAieeZFRWxj5IclucNq4VDa4_0IQ85c9A7iFu3f8CpVLBpcPA_-KBX1iy06j6_in0Ps7rf-lE5Y0vRvtW87CTQCoOeEehVds5UcsvPlphFldPyj8aDFWBHOBLIys8CsyJj7sAfRn4BAQg2H8JNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTbemO-QIcfpS9vfbRZ9ZYoLIl5r1w9aNr1Bfpjoe4NEdyG1VwQyIQzTbAW6mI2Ue1Y4aoJXMoxq6ismRMCxC1adT2ltqazGz5t6ByhKlKnbLSPv3tnCH0L00qVyuXjfPuIYrIQmo36y3DHKLxRrm92JG_yIdnpqzmDSnL0FKYtVSl1XG72M4f2-jAt0Foy_U-covkt2ECUSzZG7wCRDMf2AHd2UQ9FryYQkUC46iM2LXwI98CAMk3vFWROuSVn_OU7PKsg05imc5T0dibnjXSopkmWA2FnwVvcrrMbWi91gHTp9JmUGzH-HRElsJhxY33uK0IKsk7T3cit7C0b9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etc10eoMTts_FYG5FX0sc8Zhqc6fjMZ1IUn0XK4kywDgonHXGZj4KsR_RoMF3ztA7Ri3JqGJIBf2ybwOqih7FLEyKbMKZi_224h7SPXdCuiplsN0BtyrNKPCgHimmq8Y3ZiLt32Q5rB8p-Fu_fZCTsW0bTD_Kp3fE6-0KcL8XEt1Ji7VYub85D9DPSepyeCkUo280Lw6GdK5Aq2JhuYUREC6W1WjrADumHAdGQ4ZnJVjn1bu38sbgYugYg7fxFeskckVW7yxGYGzuwsui0Xo7iywWy75s4I7MA9zYLRTok23o6G0ovNpLEHhxQwWz5V4ZzzqMtkG-Jdyq0WNy-T_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN7WQEso_khZOJWOVQyyWrLhXhFhHgAF84mwTojMi7owLds2S0bkOd72jFNDYVzs5CuRMdcad7d0uJnpwoX4Q3VRpRCUihuJbU7EAxmEuRLgq6b1uuln0R7oQ3nidq9XuzzCDw_NXt1J0Y314yJlXhCPzvEwZp1WOD9epqcUye-WHhID__x50qau_RNATUCg2s5X-YgVHZK-bRnPuJJDgYw8xxbxUnJ5-yWn4AGn_sBuEtBk0dKSueH6PqZ5plwBrL-whPK2TRETC5VzpDhpwqReI6NzodzlugRHM3-9m3PFic5caJznl_DdP6MIkoCgHTs3183-XrJC13KZmAPj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dddc0r-GgEElbubo9KzgK7QpngLk5b215wXKw-j60cCHnd13YC7fS6WGwQjlYNcNOat7qgeXXt9lON4t5uskGKHTEX34fRhRF7psk1Q6betj2KuH2EPtWEOvMM8YnO1mqeXAP9oZaMQsaR6v_AEpNHpWBtNYhUeXueFSClLZYlJEJFsMaG11g4pw-LxdcQxzdMG09sOu8FAY4ui18RDu9ZJSlO2H5hqD4ALwUR8UIV7zM15-Nijjk_k4911Yb4ijay6eMCgB-VilR5IYl3xo3YbpnMut8SjS2UKHCRKrKvO7iwy316Bg7u_Mbt18l_ltvZzXIHyt5wm9VJz2UT2EXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPPdTnmFuyzKDgpeU0QPuaZNtUr2hrRfPrVsKpj1EA1cTz3oLmiHZ5qqp8MYJ6iADf_TfO4Zpo_5gyzQDy33hUU4S8VjzAvhpv7ZkJeYVFph_VWLIaz3q1uDGAGeQaWe0m-NoB6wbHEKgH0kOdI3m2s63bIhMt4_Z3VHDWf_CSE5ieaITqrAQvzNVKZE-9m92dgsmTrXQxo74mzNw8RIo9y1EcvaF7ww1BdJZut8JC_pvHe_046lWCeY70cppwHmAvgZfYmNuw2oSIN4yRlia8k-mmlOPn_DVqP7ILw9QTRoxu95s-mOSkhrw_G0E_bewb30pLrqwEK4zkx_CfyfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZ4ipf2jsZuLWltwkp_YLd_eonM6M2bHJRAEZi4eOXT7Wuo3EPvsfLNieawRw_Itc5fiWcTJxuF3F3O8EP7gmjcaHMty4pRpjEMDmI3dJdyTganunal6eTJQcMK4pLhEu8E8dJlN3itFVuusGtsAo3BtqN2ZcJvhCXAqvzM48Ky51wC3qEtb0TgV6zNMOlU0RiLFTG-13p4jyDjF0kAOKKTXDbWO5La7wqa00AIyOjhUY4LLGM3ck1LNpCSkBkD0tmLF8cdO5CKSVz9-dBcRc1190m0Pr0AL-izI1_oIJW5s_jePIwE5QdKgzniBwNWpjsXNQYWaGRvtTdCgbOv7rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF_g2K7w0qRDU5Q7R1pJ8tKiRGXGhfP5Yg3xZHkf2G0WGhCxf3orD1MGXT4HbSk6w1ji_2AF8AAwyuwX4eEdRNhgUz7ZS0NXDkp09cG2Xs98bwfSEvh9C244BBiXbbOmEMvVcavy7a4PVJPiwM1uVOB2AzsbY7p5KuvMC0-qEvG4DkLTmIgbqNjKJxWWVhrJAqNErvsLieeyS7HHBYovrKjvunTScJDwCDwU375-HuNImpY2wWZoMmehJSiQ2SXxcbrrFt-i6nhQ6OF-Y4EKjMz03vkgIB5_rh0Q-Tf-CDTdbuRDLwvnKjU9yrnQAJKkmJSI__q7pR0YkL5UAHuzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G40ofVHQgcQ8Pj2bX1PQ5n8YPdIOWNxm-a4UY9gPZxKqBtUxt44dayEO4FbCIRUb3PviF_NUf9TdrX3YhVjVa6rUU8VfpuRPPgq1zghkBS-fFT5kE3HNNNCKPxDvoNqs94_5HvPGFlRKwV0F1n-cENx9NovbYCEb52B-8FD4TcaBgaVnSg6zPh_w_YICvqXtj0XEFXv9tKyCa_E4cZz7tqca__0gXLnwEqoxaCzbs09RtmeJDsRxRpn2cupk9zAmDZgpU56EXPRFEynmxl0rMNtPWNTvPWQknmHl-Vwx0gM8Zqdog0ZvW8vgdC_d8uQUrUnyOizTF_ff4QleTgLbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjqCBQZOnqiG6aMSfGacLqyoS7S9tH-bwkke4dozkX2MGw3JDPYntpiv9-N1D7ot9EmAZ0SeS52zkNNgf459u9afUHUnNp3wrzO7jFlPQXY3St_eHXXVASj4r5KfJ4uJEPKu9Y8g24llgO4vmdr7g0WoNvJCfwFb2COD_yYSrSvMXpuFr_gLX35SyYJStAhmcXwbG-g3249NdiQLxiQL0LKW0V2s8wohn2ZvLQQK-XP5vcVgrPGbQeYgWP0iqUV9tWG73nseExDp_UHGKBnVdlHMjlKQBbEr71lThkTF6PLhWosEd0yvk7Hui9OEwxkS0uBt-3MewPG0nf9X_vEFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhtbFLfiUMbztBTk-9is0_kwvo2YvNFssyKKmrn_zc32vY_gUhgvTo7mzptL_QVwHL5cSS_c562V9T-WpsmhUacj649uYiQRibH9XWCo7fPN25iU0Crj1XlQsOYR8qly5hY4yVz-UnxONlL9J1qQEkMemCDQ83bUbd-odZlqR0N53NRunP2SXbgsk21v2efJyHMzD8L8uSs7uzEJf8Mf6VShFZiN0nahPx_Uw06RA1WlQykGxpNxIXDpXIKRFcMmXc2DwXsjSKVym2-gDldwvPSS0CcNRDryUam9PjoZn92xBa6jU2TqZxj0jwwAdggo925wjgfm0JbcblgwDPbwiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Geftp4vy-VtNPQnyDraVlsT5H1SDVG6YHPQhgRpcG_1tfQTD-GBtQWJy38saCONK4IA-yGWoyXpSp7Rz1SLQkdcDYpzp0belftio54Y_EwGVcTm6CBPV0pCTRj-BfhGeUA74XD7Lzc2Jj1v7nB60FOXWTT1yvYX0DMGWioFZIxTcAQKJauw_4WtQQX-QKDsaIyu58V1PQHaBGzjVSsvHhys4bI8n81h1NN-FcdSyJvCu200UtERcqtYUSDUnaVvw6DGtw99RaWyQ4aRtYs9fsZvLQkO1k_6Y5n7Ls0QGvzpDghzJ10zBNj5xjSETUC6HXqNs-Vmf-LY6lyhciSETHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Geftp4vy-VtNPQnyDraVlsT5H1SDVG6YHPQhgRpcG_1tfQTD-GBtQWJy38saCONK4IA-yGWoyXpSp7Rz1SLQkdcDYpzp0belftio54Y_EwGVcTm6CBPV0pCTRj-BfhGeUA74XD7Lzc2Jj1v7nB60FOXWTT1yvYX0DMGWioFZIxTcAQKJauw_4WtQQX-QKDsaIyu58V1PQHaBGzjVSsvHhys4bI8n81h1NN-FcdSyJvCu200UtERcqtYUSDUnaVvw6DGtw99RaWyQ4aRtYs9fsZvLQkO1k_6Y5n7Ls0QGvzpDghzJ10zBNj5xjSETUC6HXqNs-Vmf-LY6lyhciSETHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=VlIEr3DwxmPStEvpPVSHDMDMxUmOFMX9z1qAmGOL9Rhj5RO2zz9y4eTBY_ZTLW2NFOSeEjaYs_x0mWT66uqO4vRGk5QHNR1osx4LMHb-HX_BiAbjqPZ2P69xZPkEVNBMPeZlRWLZDY3eZtiyLTQ5thVfVENP5R3NmnDvwN-rRfTvGeSjoYTHvO9Y4cAleTxOtsJD4CqmuXrNXnkb_CAIBCYxbOiuy6HEG_qR1ShOTYWrJa6Pq_TsCMVsGT0tYTd4jc9-ZtfcopAMz3ogX2DVKO6q5gx9joOTTis_JNQdlpGLtgn4PEK1nrAq6hnTkHcBAK_Q5YXQSazE-abWCOw8-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=VlIEr3DwxmPStEvpPVSHDMDMxUmOFMX9z1qAmGOL9Rhj5RO2zz9y4eTBY_ZTLW2NFOSeEjaYs_x0mWT66uqO4vRGk5QHNR1osx4LMHb-HX_BiAbjqPZ2P69xZPkEVNBMPeZlRWLZDY3eZtiyLTQ5thVfVENP5R3NmnDvwN-rRfTvGeSjoYTHvO9Y4cAleTxOtsJD4CqmuXrNXnkb_CAIBCYxbOiuy6HEG_qR1ShOTYWrJa6Pq_TsCMVsGT0tYTd4jc9-ZtfcopAMz3ogX2DVKO6q5gx9joOTTis_JNQdlpGLtgn4PEK1nrAq6hnTkHcBAK_Q5YXQSazE-abWCOw8-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=gYGOQq4RzMqZ1DrpRhCHMxT3FrR-BsYhE6tNngFGqv96kXFj9lFDjIgA5K6NyNHqVNC-1UeXQ9OaVTyoRabHa3OfNQFOo03yBcdBQcjw-_y8yPF6SGFTkOCoy4uMFUCJZPKpV9OE3djt96zLOX2wuXvxiqWbrzyiatCuhLjfDN1Wtae4WqL0g891TaAZBX38LOdUcWNN1iSkQ6udWNJUPdWux27rQa1nYuuZPfC10P7iHEN4Sw_RPh-L-LdQgbPGr-qVeQXfqDgrpu8pSdhKsWVJijkY7TXnpCHxzYzmkpm2uQO55WQP6WjnJLqi4tHMJWEsibAgwy0XHqP9ej39GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=gYGOQq4RzMqZ1DrpRhCHMxT3FrR-BsYhE6tNngFGqv96kXFj9lFDjIgA5K6NyNHqVNC-1UeXQ9OaVTyoRabHa3OfNQFOo03yBcdBQcjw-_y8yPF6SGFTkOCoy4uMFUCJZPKpV9OE3djt96zLOX2wuXvxiqWbrzyiatCuhLjfDN1Wtae4WqL0g891TaAZBX38LOdUcWNN1iSkQ6udWNJUPdWux27rQa1nYuuZPfC10P7iHEN4Sw_RPh-L-LdQgbPGr-qVeQXfqDgrpu8pSdhKsWVJijkY7TXnpCHxzYzmkpm2uQO55WQP6WjnJLqi4tHMJWEsibAgwy0XHqP9ej39GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=PVN48ZL6NrP_Wj9Mm0CwjFUCMppPECOC640b4ulg6_n9SG4qMViCMcBe7rCwtalYQx8QMWv-ckc5rGcARvDM7p7nOy2gmTzNwPJpeX5xwsR5sCfeDc4thL8GVZF9UuJwvTbpym8SDG-Ia8xJP1PYIEYMDnSCdOn3ci5qpnQxzdtqe7BgOq0dlqTMCh1_rc5eudlNSnnAn4oV09MilK6AqAvWb00F5UYA45bTh2SmWudM9if0BnHi9cQKio-7WtU3sR6s-CItmH9sgSvJawI-vbN98EXYLqdXzIwXtUfkfpR9JWs-yLbyMDXwp3sad5mPSalZRPZ_dEY34moOOhPsdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=PVN48ZL6NrP_Wj9Mm0CwjFUCMppPECOC640b4ulg6_n9SG4qMViCMcBe7rCwtalYQx8QMWv-ckc5rGcARvDM7p7nOy2gmTzNwPJpeX5xwsR5sCfeDc4thL8GVZF9UuJwvTbpym8SDG-Ia8xJP1PYIEYMDnSCdOn3ci5qpnQxzdtqe7BgOq0dlqTMCh1_rc5eudlNSnnAn4oV09MilK6AqAvWb00F5UYA45bTh2SmWudM9if0BnHi9cQKio-7WtU3sR6s-CItmH9sgSvJawI-vbN98EXYLqdXzIwXtUfkfpR9JWs-yLbyMDXwp3sad5mPSalZRPZ_dEY34moOOhPsdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=s9o_yjc-QKSGfI_U5535hlmVdNRUrr1yjHyr94DZlttdsGLuhchhqXLBZsVtGTWRhTD_JEp6H44JTIldqXaxIaA0NBD-YKvJsCnPlvwGVuqKnaQsKe2eiptoodHhJ0OtB1eEnx2uT6IKxrpyzn9kDyNvnh7krDAIOlpTDeXzGlWguBzAU8u1kwkmhcIoKKX082_-EIGg0kBaKfD5ey-hO997DTKntf8hyhdcR93saUkKBwxNN4tvWIGY7_UUt_A0EYqk52Lgz8hYuspGAK920uVFd6NscayB6pHeq7TuJ7i_L6ewxakOwqsqueREYPLj0ghZ2glCQE1sVNAvxIYH1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=s9o_yjc-QKSGfI_U5535hlmVdNRUrr1yjHyr94DZlttdsGLuhchhqXLBZsVtGTWRhTD_JEp6H44JTIldqXaxIaA0NBD-YKvJsCnPlvwGVuqKnaQsKe2eiptoodHhJ0OtB1eEnx2uT6IKxrpyzn9kDyNvnh7krDAIOlpTDeXzGlWguBzAU8u1kwkmhcIoKKX082_-EIGg0kBaKfD5ey-hO997DTKntf8hyhdcR93saUkKBwxNN4tvWIGY7_UUt_A0EYqk52Lgz8hYuspGAK920uVFd6NscayB6pHeq7TuJ7i_L6ewxakOwqsqueREYPLj0ghZ2glCQE1sVNAvxIYH1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=XW88n46GMvPIO50pae2TTpLyf7s2nWWqMCu1jhLhDrjaA9gBMoFeE4UE4ZM4C_SAMgzNiUDZ95SAp5WzrsrkSVEZNV9yDUJV1z01GmaSebJysOH2mTbCN5Zc7TXHm5lI95Uc6loHZSrROjkPIbPS-ztGKbcK5nMcS6t56u13ahWFCkBQjlENfLAU1d3iDqGqPpY1-P2F83n5WP-NZUkbGL-GyFdepNO6tpjoZhFv4OuDM9qlfT97bNxTlg8ujWpYvd5beUx5QbG1EecWXSUe_3W28-Ae_A7n6JTUEeOCU8G7GG4gKyzPLdCreAyswu9WfLdJ-d7G8oWXqZw9u_HXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=XW88n46GMvPIO50pae2TTpLyf7s2nWWqMCu1jhLhDrjaA9gBMoFeE4UE4ZM4C_SAMgzNiUDZ95SAp5WzrsrkSVEZNV9yDUJV1z01GmaSebJysOH2mTbCN5Zc7TXHm5lI95Uc6loHZSrROjkPIbPS-ztGKbcK5nMcS6t56u13ahWFCkBQjlENfLAU1d3iDqGqPpY1-P2F83n5WP-NZUkbGL-GyFdepNO6tpjoZhFv4OuDM9qlfT97bNxTlg8ujWpYvd5beUx5QbG1EecWXSUe_3W28-Ae_A7n6JTUEeOCU8G7GG4gKyzPLdCreAyswu9WfLdJ-d7G8oWXqZw9u_HXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=MXpMWSyNZLWbeLxspLVtNKgOa-wwKUFnIV8MNA_ADs3-1AANrPT-TCEpygc0_ocNdnnM7vGtMwpiN88BeAQi_O4c42xfwGC58Skl_RYd0p33xp1KsG9dGIG2cWbAYblTlArinkvu1Al2hhGw_dHpUWbPRyFFsqQamp_aJ-MmT1B6BU3vAOmnZOnJiOkdAGb-U93H6IXBOrrQF7NImde1oeQGJiW2iI2zkcJ8_l5pV9ZC0fG73oHVbzFtAtDgo4hT-dKsLQIp5WJcuqlj1zvHTef0LERAcJrVPn9yPT_lcospyJyIcjUdBBcN7df1qIrCJQdlruP_kxEtVjJbYoB6VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=MXpMWSyNZLWbeLxspLVtNKgOa-wwKUFnIV8MNA_ADs3-1AANrPT-TCEpygc0_ocNdnnM7vGtMwpiN88BeAQi_O4c42xfwGC58Skl_RYd0p33xp1KsG9dGIG2cWbAYblTlArinkvu1Al2hhGw_dHpUWbPRyFFsqQamp_aJ-MmT1B6BU3vAOmnZOnJiOkdAGb-U93H6IXBOrrQF7NImde1oeQGJiW2iI2zkcJ8_l5pV9ZC0fG73oHVbzFtAtDgo4hT-dKsLQIp5WJcuqlj1zvHTef0LERAcJrVPn9yPT_lcospyJyIcjUdBBcN7df1qIrCJQdlruP_kxEtVjJbYoB6VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajIWhPlBIjlcMtVxdGJNvO4Y_6kgHEJaYDxrmjJ_yStswnLJz4EB7rUpKTeAQo1h0l4N6Kgi9In0oMGDTDGkX5ziMHbq_m-Yy1dFr4f8p34MztIUTv59nl-bwlkTxk24HwXnVNj6x5ithG8jMREZjo-2w3A-GKeVoBi4KmQNiNk1n4U0XL37BBflXH8MQigJ3sM9b0UlOQzGi36lCeGke2tIw82twD5zwPsn2blzUZGGci52DVpM6ZQA0X_hDt1bmntsM79eZL4i3z4SyZ8_-H6AFC7FrQNl1LRMfyJ9hoJmzvm79mTfTfhGe0B8yKJ_kr0EWDm2aADZdYN0O_cV1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=fsB93DWgyk2WHOnkYawvt1_VvVxXrkVJVCSmqDswdCiQ6laXJrGScB5kblpiVKfw3fg9G_XWYTAHe0cXDnX2jjf0B1h6x4hybeQdPZJXFCwPmsJm2D5b0Luxnn7tp_pOI0pMP4DdMAR0fL5hwiexeIdneUQz1rlzLcMI889ZwDz-a6ev93Wet36Z4D4brnqNFZx6osuho9PRd5veUZxK86G8v3VUMNpVI0cZev4rh9iGwcM2QUVnYeoY0uf6RjOo_pYpxljEtJ1xoWRFVIN8lqaYpGy-7v7y-H9vEtPniYOjYdqwsETACaZCTMR2WGj811rnmRttJ99ihEFuBg_YMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=fsB93DWgyk2WHOnkYawvt1_VvVxXrkVJVCSmqDswdCiQ6laXJrGScB5kblpiVKfw3fg9G_XWYTAHe0cXDnX2jjf0B1h6x4hybeQdPZJXFCwPmsJm2D5b0Luxnn7tp_pOI0pMP4DdMAR0fL5hwiexeIdneUQz1rlzLcMI889ZwDz-a6ev93Wet36Z4D4brnqNFZx6osuho9PRd5veUZxK86G8v3VUMNpVI0cZev4rh9iGwcM2QUVnYeoY0uf6RjOo_pYpxljEtJ1xoWRFVIN8lqaYpGy-7v7y-H9vEtPniYOjYdqwsETACaZCTMR2WGj811rnmRttJ99ihEFuBg_YMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
