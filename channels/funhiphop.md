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
<img src="https://cdn4.telesco.pe/file/J-t9bJpmSx3B2bof_IF6KZ8w2f9o7kcZnmcO3vKYGFT5HEBt6RAEf3Jb8e47fR2EAISNVKSE2cYdzS_O_9brXAWM72PH-6ItyZZ-tFZfB6ents7nEY8Ae_ba2jEVgCZUHetaj7ySqoL1T_Gc4ME78EzIgrhJ5m2ec6hdkoZqPTFYst1wVt9bEc3c4j7GOb1JzuMIOI4W-izcskadf9CTlFSgiWmq87MwaPQXzkTY9Rm8v9mKSEx--68y24T0QjSkVJH7vFU3WCtY7BQKC5cl_BIU5TL980SHAfNJrPJWEAXtxuRl2JMzRqzgBK-FtpFxnb6b8DwXvp0LoDXeocjokw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 239K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پولدار شدی ایرانی
کالابرگ قراره ۳۰۰ هزارتومن بیشتر بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/funhiphop/83541" target="_blank">📅 13:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa__aaEuwC1QZo7vDwBvfXGw9NKF4rHuep9RbUWWbcTHDC8yfXu9aZyubCt98EvO_wnMLb3g6__MprWI2iH2WDgslkVSvekg8QCtnih_rKRKvmnWRyuzqt192WOTg_Z6AbdxMGnuY0xE-jmmXTbG4Vb832pQ8O-V33IHByLwCkEAIL764BlccYrS4PUdQcK00n6PwPaiInXb0Ptl71ZfDrsny7laz7CagT7ryL2Mn3MYe6lcTPgnon2Inf3db4qcWKYTTo6m4AMBiI1IGY-ah210xM3npDyJqyirC1nJJrIrhr-ADji-legnP9MsN8sqbrU6IJhF0eAkKuena3balA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی منتظرم ببینم کصکش نبودنشو چطوری قراره ثابت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/83540" target="_blank">📅 13:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEdxh7DKAa8GMgfVM4DZL6tHbO-Um-FcYUwv2bBhb5yIdLo5j4HWDl8Zf3mPJFTJYODR0BNvzUVT6NjcDDLF5HzTarpgiph5zL5kXLilG0ccCYmkj8XZYiDZj548iXS3QgpKWZrFhLfjcaInK8mu6wgsRrgdDF8PAkvp4LBeypNwbgTADpciBBwKYvDvJvGWEZJuC3alARQ2kjBs4BdoQKmQR6ywpHBfKk9JPNl0PV4_A4XMpzSsqwznJA8uJrG-HxAfQRKdLPeld0pLGcDeNVH9cuUTglzGruVGutCrkv55lNEmy5EDHD9vilefn-vIS-SoZgmym10sDDzITDxMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک الان در همچین شرایطی با آرتا قرار داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/83539" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spinner</div>
  <div class="tg-doc-extra">KVIRO</div>
</div>
<a href="https://t.me/funhiphop/83538" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/83538" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGzoP1p_PvieU4WtTBlAPVk0rdwTi-0DUQ-9IY8U5rqqZU33lX0DrlFHS7PREiVn93hXPUEjXEptA4Oybp3EwRtIhbCbM_EMPrHVZwmEU1IFQpb7ncUfXOxIROg-XcNJDE3DaNFvBLc2rTrEGQCHCio6UxqkE21YKlV8gz0C-LAoZh3HrSnPA_jaxSy4KRz5lUsCtOW2CAun76nhD8ILlOJmIyxtQdd7gFqZBAgCzO_-00BhKlYA0ddXSsD7QUZ0gFvdjSnMabEEmadNDC9W2RxeIXNZXDyTjfmB0BeO_Mp862YuuggbOSA7ql-qC7u62yZA3XqBMjWNnM5xuDAxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "کای‌رو" به نام "Spinner" منتشر شد
SoundCloud</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/83537" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/83536" target="_blank">📅 12:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfGGuRz3PsxxebeqEoYg4KON2kPwECsMmKKQrXPT2oMyHYCFOHq9688Dp4wfxjhCPZLtBF5yHR7H5IqmZ1EjsRQtZdnfqcl3m7pc4BfoBEVRQE6K7M-uUDSf5SKczYApoGa2SfXUvKPWxqD5t0UiyAMvnY7l8fzKlSSxqEIz9Zf93EzjNasjHdsdy7xQ8PCftMR-5aE3G6SC9CLIv0UQ9QtNdGP_qyokwWU4Hw9jIhVtye7tYOGB3Otdr6fMia30T7iJ8baa-oMX1gpP-9JYUzXAlJj8WhoXqYqEDRjEUU4YATbKQdmtF78I4lS2MpKsP2LHk8IBmoi0jeB7dwHjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/83535" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83534" target="_blank">📅 11:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83533" target="_blank">📅 10:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTsy4MD-q3k2eg_BljQ_9P2DCdXTTqZgdshkVAPep4hCB6ERxZz8MtSw7Gn85fJpJN2_jELQX4LpihXsJW-8g1zYI8gDdcwgKEl8JSPbyoQv6vRQpns-M14QmisaFmYYqIAcGHhuavPl-0xv7FStC0bY4MFTalMby_b2c0cklrqnQOvtZmQwqkhUMc9uy_YEs5iRpkKMIc7LLX6TolQsCJkjWVFPbXRsrLVWHPpFKtqMhKBKtH4kONeig28CFUoUMDXS7Sv2VNBw4gBqCTg5z-RXVXXZFJTxhG-nDPiwf0vlSKF-9eOtqmcfs8pCox3utpY-Ggld4BwWQ4mYdppfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرینج بازیو بس کنید ندید پدیدا بعد از سال ها یکی دیستون کرد حالا گاییدید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/83532" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با من از صبر صحبت نکن من برا هر شوت سوباسا ۵ هفته صبر میکردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/83531" target="_blank">📅 10:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4HoVoTq9iIj6jlRIU1eibFM9qSyhqn58KEOlwUtKppFl9VYXoaKYHL0x2g6L_X27-tGDABHUXd5Bl04qHUg8j8lve0KN8PJzaQihVQxNv6fTrFR6Y_flKCVx9BJUIlxK3obCdHOW8j7WDl--eui0C5afXC1bYV9Hm3xiu5OZVF3RONox3gSMWaLYfL4SFOjUjUBDvO0efAvNzNCvfHmzUCOPWzpcEBdrpf4pnpfdm2mj0Wm9mlPdwRkBWsQb4CV8Vp05ewT08wbX6cijj8PR3QCTm4WZ8i36y2k0mc9r4qT6FR9vJyCPk85Xr16ac8uE01Yd8zdQ5IJ0_uSi3gUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkAxAl0HiLi_OLt1QWrbVb4qHn6IC5rdxhesxcLMSzMx9bhAEXVDJTB2QjJrJZ8StZqhAZ_OZFOYqsO8NVZhi5fyWb-nYjUsa1kph0-hV6CCAbZXg-IsjaqErJVt_LwQ-Fv2WZxlqDEOE6swPK5iyd1cBT6Gr9aJZIFxAfS1PQPE_JZl_ZggueomqnwHwAXx08HS1Y44pKqb64HesXcWk0SCYNcEPZVKe64-Ngsb8v9PwuRNxLSJUl-z-8ajoBfhon2hgwalxANH7NpP26vZxxuq6wdajPr7gx633OGboUEbeUcEdCkHEaqzTeBWiSBukOqderXBxnNIFNBVu76LzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKhEzsd63l390sKFHmPec4fIn1oa9lwnbGsTOr21ll0BOvuvr-HupOhqF1sao7ddh_XxO8a50EeVLrDplZH_lxBp4j893EOCxSA3gMS-U00JBrAWW2s7i23qu73nJ7OZJJzADMRUKdVxadnqrvyyclJOjaBYouEC4O4gPq58VEdyPaJIFtriSLC2fJKVCOdcK8xkHscAU3tDMTpeXHvVsRLAJW_EI9jhZkHkKomQmtyG5wAQjcsrNgyJwZhJldyDOjEa53tIbYya1Kk0CoxwB4JgeFMxGTuVm6spkjwzxoc4Pnl6dVTMWRrBcaVOHi89ktUyEDx4YKIs1PjU22vrEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید شکیرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83528" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3OWrp0ysCUX-5pZ6EoYr9f9hq1h9Gheh6z8Tve2BxnzBgLbx4MXEbeQ4MurmwumliotM2mMeTv19gIzH1ytAk02_odmS_VVO69pUkAgJYBON-Z_YCS4W_I0DZk1ora-r5Mbv_jLebTCbdQAEOuFilyjg9EwuI58gc6_uopKPfS_Y20g6iFm_3LNoGxJ-ziXK0_puyeQsOHBXDFvl4V1dUpbNyEZfxiM2D7jzFdS8PLWnRWOM36dGzOzd1Q1nZATP8WmnIjm5C1Xw5rsmpDvd6PtwaGXw339Yi9sDOt-ASXcnyX6cXYEYS2TvaqYb3Xywfryw8TnIrLn0CFa_s9DDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اتلتیکو مادرید - اوساسونا
⏰
ساعت ۲۰:۳۰
🌎
📲
لوانته - اتلتیک بیلبائو
😀
ساعت ۲۳:۰۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R25
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83527" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این قیمتا هودی، سویشرت و دورس جدیه؟ یا دارن شوخی ای چیزی میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83526" target="_blank">📅 08:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ددی آرتا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83525" target="_blank">📅 07:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ببینید دوستان بیف تو رپ طبیعیه، حالا یا ایکس(وانتونز) یا ایگرگ(پوتک) میزنه ولی تقسیم(کچی بیتز) حرومزاده اس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83523" target="_blank">📅 06:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لاشی دو دقیقه دیس داده ۱ دقیقه و ۵۰ ثانیه اش رو داره حرف میزنه ۱۰ ثانیه هم خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83522" target="_blank">📅 05:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83521" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo5NZ0CGi0J6lrzuzqgXVo_5quzEJPmGkY09Gi-hEefpt4tQKizAHxCNga-R89LVR6tZI_HjwLOUITtBTWZXYRGxzW5jcYdbveyhkKBGjtHvCj27kEFghHhCDKnE2QHM9dqVmSA29-NHP5KY1KQusC03sEdjpgX7DROOPUVgGf7pDGu8ZQUMWX0JHUji5qv-DO5AL3gspYettVelUZUFre-GIOcmV3N5XbR_P7GjmOW-VsLNIBdCMguxA3yCgKjzt9ylWLemuaRYYwxvAQCL0k738qK7DZ7JyjmCizCA2L202j2WPgN3WiN95IrojyBdR6CRSE7T2L7C8pnPwIpvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/83520" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgBqdxGqrvMqWhC3zXETJxqfawO8ArA0sjfKjr5_Op0D2jkvarcuxsxhVITu94V3Vy0Kts6QyaBjHaARCxniRdIIDuZtTJoZ0RlY7nS_WYy5783ehfn_S-YuAjl3Ui7Wy7Butku9rPJckb7usjWokQeelTaQ9_Jnx-P_emdcQqdtqNst8CFbcmrpSSVOcGsvG6Nquvb6zBJzvo1ygUd9sVfdRgzlrYECcAGb1-xSEvl8aKhNu14aup7N771bnnYwm-4FW4fQIGciM080hzPV8uCy0XNQi8iQV7JZG8ZEtp5KCCs7n9bJlgWrPDEj1h4QFTIKwhWeM4-ru7FKxL8lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری و ویناک رفتن تو جلد آرتا، جواب دیس قبلی رو نگرفته میخواد بعدیو بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83519" target="_blank">📅 05:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=VqkGktvqdS2V2QaOAUUTYAdnqDRSWIaNiYBoxQr2xB18KAhCyapZGD02T39-CLO8Z3LR4nNzeHjqhww74cQ4gLlegJakQSeFaLfMS8Qt1ZHl7MMe2nBNnrTYk3rFZn6Jnhr6dEH97cRWLxt8RRiA7xRlyzpMte-KKIsb839caWmJjfSMlSa4CoC3imd77VX4VSjMEC0hofgp0InI9L9bQo09UP27ENl3hAI6ZXNGmQKD9AW1qYilqlCptRETdVpsdVcsxXrEgOBXTw_jf5_rlMJNfhVGDdqpqZMKjN4mxyP496S7eR_XdiJJGmDXBUMeWYBZbd1mOYjgzQZ_JkaTHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=VqkGktvqdS2V2QaOAUUTYAdnqDRSWIaNiYBoxQr2xB18KAhCyapZGD02T39-CLO8Z3LR4nNzeHjqhww74cQ4gLlegJakQSeFaLfMS8Qt1ZHl7MMe2nBNnrTYk3rFZn6Jnhr6dEH97cRWLxt8RRiA7xRlyzpMte-KKIsb839caWmJjfSMlSa4CoC3imd77VX4VSjMEC0hofgp0InI9L9bQo09UP27ENl3hAI6ZXNGmQKD9AW1qYilqlCptRETdVpsdVcsxXrEgOBXTw_jf5_rlMJNfhVGDdqpqZMKjN4mxyP496S7eR_XdiJJGmDXBUMeWYBZbd1mOYjgzQZ_JkaTHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو قدیمی‌ای که آرتا میرحسینی از پوریا عرب بازنشر کرده و ویس‌های جدیدش خطاب به وی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83517" target="_blank">📅 04:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جنگنده های اسرائیلی امروز چندین بار تمرین‌های شبیه‌سازی‌شده‌ای را بر فراز ایران انجام دادند، و در برخی مواقع حتی وارد فضای هوایی شمال غربی ایران شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83516" target="_blank">📅 02:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmiZ8YKeYdE8wbddu3joQltm_B2JezAyFrt5zYxvSauH74d4j5MOwIXKJTNAVeGfsU4r8yLI2-cn8BIdfFEVlh_kNdPzIikmsrkpRzzXsUhrgbBi1Z4c-AzJ39Z37Cmy9poe9QA7w0KrkjiQktFa7b1HBV8drej7Zx2Ag3jJw_gcoMAr_6wlN2RS1P-_-rOHdNPzSMJMvVTY1jCfgdMUMS3uD-a44M0sL60UbE1YxLRJo5I2vCL9lJ23XJuHcu4jR53x2Pdn8Mc__RDFm1e2bo0oh55rvzWjt-Dwrj_7xLfWpOpoof2mXFHNQTzgMQgQJk7tDiMajnqRwycrWKYaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد رپرایی که تو این کنسرت حسین تی ام، بیگ شگی، تیم بکس و... حضور داشتن بیشتر از شنونده هاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83515" target="_blank">📅 02:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسام سهرابی بلاگر شده و ۸۱۹۲۹۹۱ بار از جاهایی که کونش گذاشتن ریلز طنز دراورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83514" target="_blank">📅 01:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، ۷ گل زده اش تو بازی هم حتی ضریب خوبی نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83513" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز:
🔴
1.49
🟢
1.78
🔴
2
🟢
2
🟢
1.8
🟢
1.34
🟢
3.89
🟢
1.67
🟢
1.44
🟢
1.35
🟢
1.4
🟢
1.6
🔴
1.9
🔴
1.46
🟢
1.24
🟢
1.8
🟢
1.2
🟢
1.3
🟢
1.3
🟢
1.3
🔴
1.3
🟢
1.41
🟢
1.85
🟢
1.5
🟢
1.3
🟢
1.5
22وین
5لوز
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83512" target="_blank">📅 01:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بخواب بارسایی رئال برد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83511" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huefKTYYK54k-9kvWaZQuHKB0s7APoBT3Cip_nsVwAoHUVCvTMdFpCotjaEkajq0gENeVDw52xiuDd_LETHoz75IyEzCpC_H1fXDorNNCm55XNYO-WGZ_M3AvCNPl0wZK76AIf1FnHAaKQYd1BnypeYKMP5Hn1COGmo3FBxzGHDXDG-JUILcPuy-rnsoBPcsZpJYwqFAIPcUnXqDuhZC3TBFVAzuF7nOQi9cybLBN8h0yOzWc3cgVdqf1c0Dr0u6CGGvbh3sfbuz-E1D6AzApAcUbB7UvCWTNF7p3gaqc-itpUmfwv5ep2ztkb6kf3iVC6RaUKZTvM_7ucIcE0UbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت خداحافظی با بارساس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83510" target="_blank">📅 00:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgoDmkLJfKRUGHjQWmxoKjQp9SqTfF4DmYVXm-qwx4ys9IPv463mCLHcnRIfPZ_-oTDsd4k4-uTAXAS_pYw2lLoubV54Zib7CHeZbKgQbYTL1ELFLMY0obsXy6fJdFfePmxc9E328g9-S3pyVhKEH3xSZBJCdwUMfm3BjQoh-BGEn46JMrMecoIvDR_WHboHuIN_trtkq0GP6oRdoXWszUKaGTXvYHuW3-FEBifRnjUa1t3ZEQtenCh3Tbfi-HgdVy1n0lx6oTka2Rd0pCEF8HXJVlr4419FXiohgr3d4yCWxpWoN7pbEQV2Z5VIuolQ71bGn6bgP2wHA9vdSeAbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83509" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83508" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپشتیبانی تندر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzRNcBcsAlU0SqVzAeez8vGIiptvYdxnmQXLyY18vN5REysrWIeDvotsKNsrMEbijq-dEoPHxvtr626HsvNQUvqkcJoZzY6YNuBSDaD6S1drqMWCAlOv0eTlVI9ZutlXePdmLvSckn_qS0yinyPN14kGV5JXNjXY0YaKi7LLAP-93M461PHe1Xd-lFoFYcizqgvcsgLABgzvC99NuuMB1j9QCyCy-q9PHxsqeEMDa5BR8AUlz9NQ2HkfMJVZ7-nPuRdNSEWmtCb3dp9dfY4swwyuV_s7EyB0eya-YizZirCF5cWvQusyINV36kqkhlro8_UpSPIzmgBNSnGva3XIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83506" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69179260d.mp4?token=a-E1a4aFONCp9-DAEdu6tErJtDrV7f6AehEDiI5oBP_b3E3lKTzhjLob44DRH1j6oicdHyGuIqqMxKb4INM9O7lJS3zhXgL6woOLMOfqKtTQYS0jrPPsN80-0cThyTcnvcl1mX6HqGSCxMmMi2PEl8aXtpHcRn0QB4lq3p4FUmZdRPJg_Ij1155AMB34WZn8KiJFepgDePspYA0cql74oLb57Zj3YAIlZnKLx6Ijk-DQgWJDP1vfDJNp_llbDrAv5q_SgCMgO5PTnP6P4Elt7wOgThun5NAgKRESc6rjHkpMzEox7BtSIOby1nSHPsTyqxHNTUQjHlsOq0Tg1WCMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69179260d.mp4?token=a-E1a4aFONCp9-DAEdu6tErJtDrV7f6AehEDiI5oBP_b3E3lKTzhjLob44DRH1j6oicdHyGuIqqMxKb4INM9O7lJS3zhXgL6woOLMOfqKtTQYS0jrPPsN80-0cThyTcnvcl1mX6HqGSCxMmMi2PEl8aXtpHcRn0QB4lq3p4FUmZdRPJg_Ij1155AMB34WZn8KiJFepgDePspYA0cql74oLb57Zj3YAIlZnKLx6Ijk-DQgWJDP1vfDJNp_llbDrAv5q_SgCMgO5PTnP6P4Elt7wOgThun5NAgKRESc6rjHkpMzEox7BtSIOby1nSHPsTyqxHNTUQjHlsOq0Tg1WCMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی ایران حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83505" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیف اصلی شروع شد باز
تو تنگه هرمز صدای انفجار گزارش شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83504" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خدایا گوه خوردیم درگیری بین پوتکو آرتا رو پوشش دادیم بس کنید توروخدا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83503" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انقد نگید چرا بازی پرسپولیس شروع نمیشه کصنمکا
با تایم تیمای شرق آسیا بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83502" target="_blank">📅 20:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تیمای عربستانی تو لیگ قهرمانان آسیا جنده شدن</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83501" target="_blank">📅 20:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p64STA5gFJha8VwOiaEfQbTWK_hVsYpcpt18o6ZQaCf6Az-1VbEWcNyCO5PrBf8eoV0Fqu7tWoPueKtbNniEXqnDDvwe2ITr_UWFJpYuv4R-0YISFJ6IydKH_U8-3qYbCdvtdZtxB-SXzLhrRsmZrE1tqcJJZidwGand5DZ0ik1yluQsiXauhonTf4WGthaVePQjUKI1py8QYf5ciaTEpFv2Ryg913kxkkq9vJcF5Wnmyb-rFdB7uPwQD0T1r4wJ-bXFtTqG4TRZBmCGcaqtHHQ2z3KVIhtlqAopu6MX4uBbRGGyvfzl74o4ilMgdUZ4OyH9lPOc1cgtu_mt9FTC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83500" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83499" target="_blank">📅 19:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij5UJQBp989nvMHvl-rH76a7MNL5gORDl0uH1ghZI2436_JbiGQ3b3ibbvDI0xohFn6rI-hddt8YavRNqSyPcdysKjAyz6dzZVPjgi4AAqHPHhHLfkkCUezzHXQ8VPSdDjcEuTrOatliWf4fDPvnUYDyH_eSX4sHiQGPmHFl78W-56RjZ78lTvZGiln0_3InyHYb3kX-hpN7ih0BCYx7VLWvQxQo2uekDC5x3J8csIla9qTilYUIhY6Y1sZwK1sW5qKjvjUcXm1tR25l-gzRb-x14w2ev7nM72Yi7gjNKiqJmJq49PGlS5k42yF1KnW_0huM9yHkaO3c9o8rJTtfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا هیچ کصخلی از دید به قیمت دلار نگاه نکرده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83498" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83497" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLZS0mp-xDBhZRLzcL2vVZ1C8B8GGDkWkYJKqC7-1YXC647ORpoZ7K3fL_ROxduBHFS9VzXaRe582kdaAcVGhZJlUXC474UXwkw7QLR6CuPq1CfIgExAChL7IOWL4vXEDXz2LONhz6Q2nTtxKiXGJR0z8rTqbdnoY0qnmK-hkbarAEmIn7lGyjjy4vriDYvCLOaUarKhVEs3RQqUSmBSzbcEUWGfkI42HUMqQWzaWySNTLborqaulJzLrC8Yj03kioTnsKomRdzi2vJ40SOH9RlMAPXCd72osRRTbjBjrskehOAaFLG0OUbRq0PAVxOZ8mAWlgf7azBmiZ7JZ2mQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
24g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83496" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsDU9SpVeSfLausIARnag0hG2iwh_bTeITPKhbj5z9Z5WiyFnXli-jZXVEuKm5hZ2em6zjXABKGWa9bvpzofHrD91dc6xOLas-biTQZ3B3X8hepWw0JVh9aGCjvSl09sU1Ox7R4ZdZbKnMoQjgN4Az5KtQAYNr5QRp5AfsiTKBzUFOcgAHI_cefWAUqawljLYSYX3OZK8UQeqxlq7eDVi4uxvG5Zk_s6sL-sYEeV7q8hLAR9qW1Tq5yZ8S9fxCnFq9uKhq5ozB_6elpSSnCVAMWo9kwPFAWNL6mB-gdA0ORXZfLl8UwBVUS3ZhgZlGiIG9FaGULqD0H7uvAZaxHqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی که از ایران نجات پیدا کرد پرسیدن چی بهت انگیزه داد که با دست و کمر شکسته؛ ۲ کیلومتر راه بری و خودتو به بالای کوه برسونی تا نجات پیدا کنی؟! گفته تنها انگیزم بود که نمیخواستم سر از صداوسیمای ایران در بیارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83495" target="_blank">📅 17:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/959d87b013.mp4?token=gwFUlPdDii5zGjx_acSkiNfEdL7OR52STiz0gSaxPNObPgRRig4eKV5fS7p0ROJf-xtG3SdDm6A2K5No-SLBc1bupgXk5jdhDhJu4BBH2WHCpSWIyoCU0YhLkg5zPEBHqZf_uyL5ayiAYWsPinqyR4i3VeZjw40RkLDLfPsXjRc2omGLZnI8XhgIIm_tnhCqu3hQvb2UXJDiNzvGxTMxIwe_-eB8-YnXRVEw8-nBOhmXg0t2AwI5dGoY_fkHUdghDNGiMgnNZ4zJdqJqF6TcVgUMBFpgV1ogUsxNL7V0-kd-1NTd9_fPnVwET0I9CRg8hSSU8ZlYOnIj91-lIHWgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/959d87b013.mp4?token=gwFUlPdDii5zGjx_acSkiNfEdL7OR52STiz0gSaxPNObPgRRig4eKV5fS7p0ROJf-xtG3SdDm6A2K5No-SLBc1bupgXk5jdhDhJu4BBH2WHCpSWIyoCU0YhLkg5zPEBHqZf_uyL5ayiAYWsPinqyR4i3VeZjw40RkLDLfPsXjRc2omGLZnI8XhgIIm_tnhCqu3hQvb2UXJDiNzvGxTMxIwe_-eB8-YnXRVEw8-nBOhmXg0t2AwI5dGoY_fkHUdghDNGiMgnNZ4zJdqJqF6TcVgUMBFpgV1ogUsxNL7V0-kd-1NTd9_fPnVwET0I9CRg8hSSU8ZlYOnIj91-lIHWgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیپ‌هاپولوژیست بالاخره ترک کرده.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83494" target="_blank">📅 17:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j241kGQJeGl4N1Qz-qJbWfwxooxjn-pwayeuPyM8tVxIk592GJfvt5wi5z06MWVBl4lcF5ED75fpO7YJHyrTScWCsNyIE9JJ0Nkc6-YJrqHaTLqKfWOLvClu6GRDZSinXZQy4mrs1lN-kqyf1QKw0nfbxYnWvsmeSV2saVsGVj0puWeXFHA7-ZQ-7U8NaqdMiL3g388ybLyvt_-xd9netvH_2zT8d_WVQ_g1W6VMqrgej-LrRFj8wMpM8-Wk_GWJkK2nBR7I_P0gYUpCgUultWxUOA6LFzdUDxj56AbJTFIBwW-hILg9P66CmpvNN-OCybPK_jQM_SJi6_WCrupFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83493" target="_blank">📅 15:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فینال سی ال ۲۰۲۹ قراره تو نیوکمپ برگزار بشه و بلاخره بعد چندین سال بارسایی ها قراره جام رو ببینن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83492" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خداروشکر حداقل وسط این همه بدبختی طرفدار دنیای کشتی‌کج نیستم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83491" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqqkkucc-wnieaNANbx-q0GAhbfut5JF420ZFtPwl4rjxdEjxsGAqZPs2HW3yK8cKeDNAcoTi7P4xMMSB82YIs7bcWNw8oUQOqC9cU5roXEcomiLnVQpaS20MIAF-52da1ZjkBw5U5MLFzPfkpnnbL4HnDpK_EUJWJcUEjy5wBazPOb27ZGLSXnLWgKTYlGwRwBmjJfDkyWdt31kDuCq60-wLbhxXja-rWZN677QwTWf8N8pOgSwYuymKuGbulsNVHvAWWN8ncss3-r21xaN5p9Rrxi5Naz5QIglaK37v_mu9i6W_-GiiJDoSYIg5t0qts1RqA7VAcys7ajezOwfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادش بخیر دهه هشتاد حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83489" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هشدار شلیک موشک تو مکه به صدا درومده، فکر کنم حوثی ها یادشون رفته خودشونم مسلمونن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83488" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قشنگ دارن زمینه سازی میکنن بزنن بعد بندازن گردن هوش مصنوعی
ایلان ماسک درباره هوش مصنوعی: «اگر هوش مصنوعی بتواند کنترل سامانه‌های نظامی را در دست بگیرد و مثلاً یک سلاح هسته‌ای پرتاب کند… این اتفاق بدی خواهد بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83487" target="_blank">📅 12:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2FwQW3xXBtJk1G19A64ezSGCFL3P7h0Z6F8BJlv1umpABMSewGHhqRiOD6LIT6kRogree_9s2omIJ38MUH55IsalwP3Scihx53srehtSwEq6bP5CawIjB020H9GoSJe_EPlQhgzA0M6KncWUzn0AnKO990AhvEL0VMl6BZP9mu-9hAiD6pLFsXQVUd1aDnttnlieusms-fHQJ7Wmb7o0LvgLQmZKjstz5OOs6y9xyRyaA4mmS2-aFsebxMSzx2Lbfd34fOUjD64vgmt_PEqt6pzYpY9JIO_lqSCkvbULcwuHtlFCMJzbfMh2iea_Fm6RxEtDgxFVyqf8heSN8ZMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک اگه ۱ میلیارد پول داشته باشید تو حسابتون بهتون کارت سفید میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83486" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83485" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa6xo5zV6nWDgvcFL5ShOw05XQ-XgUjXs8p1ktP5F8qa9A6tMezHEojTuXH_3odjieEXj7Ze2vBlA_57ONLWo9h-ReZVphK2_eMyTle30HMCIeoTVRAZtz0LefDsh1tp_uLSRd9Ic6ogSOhHYrL12v3L4UeGPMw24n6y5L8ZVJ7MOQ45MAZuFV1obDVLdpTnKgavYFlRAB8TtxHPN6eyfN1uxqoki_faj8NXVaFPW9TGCP0AoSoPTgWy09pQc2PcPsrzDYKPTzCtg9OVAWnWAa3F1Ul28TZIhp8ZsfDjc0WnNcyRJ-RckJD0w7kp2Xzh-XBOV4K4z-ZCbyGMdapaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
آژاکس آمستردام - ویلم دوم
⏰
ساعت ۲۱:۳۰
🌎
📲
الچه - رئال مادرید
😀
ساعت ۲۳:۰۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R23
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83484" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">لیست برندگان امی 2026
بهترین سریال درام
The Pitt
بهترین سریال کمدی
Widow's Bay
بهترین مینی‌سریال یا سریال آنتولوژی
DTF St. Louis
بهترین برنامه تاک‌شو / ترکیبی (Variety Series)
The Late Show With Stephen Colbert
بهترین مسابقه ریلیتی
The Traitors
بهترین فیلم تلویزیونی
Remarkably Bright Creatures
بهترین بازیگر مرد نقش اول در یک سریال درام
Noah Wyle – The Pitt
بهترین بازیگر زن نقش اول در یک سریال درام
Rhea Seehorn – Pluribus
بهترین بازیگر مرد نقش اول در یک سریال کمدی
Matthew Rhys – Widow's Bay
بهترین بازیگر زن نقش اول در یک سریال کمدی
Jean Smart – Hacks
بهترین بازیگر مرد نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Matthew Rhys – The Beast in Me
بهترین بازیگر زن نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Sally Field – Remarkably Bright Creatures
بهترین بازیگر زن نقش مکمل در یک سریال درام
Allison Janney – The Diplomat
بهترین بازیگر مرد نقش مکمل در یک سریال درام
Tom Pelphrey – Task
بهترین بازیگر زن نقش مکمل در یک سریال کمدی
Kate O'Flynn – Widow's Bay
بهترین بازیگر مرد نقش مکمل در یک سریال کمدی
Stephen Root – Widow's Bay
بهترین بازیگر زن نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
Linda Cardellini – DTF St. Louis
بهترین بازیگر مرد نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
David Harbour – DTF St. Louis
بهترین بازیگر مرد مهمان در یک سریال کمدی
Rob Reiner – The Bear
بهترین بازیگر زن مهمان در یک سریال کمدی
Betty Gilpin – Widow's Bay
بهترین بازیگر مرد مهمان در یک سریال درام
Ernest Harden, Jr. – The Pitt
بهترین بازیگر زن مهمان در یک سریال درام
Shailene Woodley – Paradise
بهترین کارگردانی یک سریال درام
Saul Metzstein – Slow Horses
بهترین کارگردانی یک سریال کمدی
Hiro Murai – Widow's Bay
بهترین کارگردانی یک مینی‌سریال یا فیلم تلویزیونی
Steve Conrad – DTF St. Louis
بهترین نویسندگی یک سریال درام
Vince Gilligan – Pluribus
بهترین نویسندگی یک سریال کمدی
Katie Dippold – Widow's Bay
بهترین نویسندگی یک مینی‌سریال یا فیلم تلویزیونی
DTF St. Louis
بهترین نویسندگی یک ویژه برنامه / سریال ترکیبی
The Late Show with Stephen Colbert
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83483" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بامداد امروز، یک فروند پهپاد پیشرفته از نوع MQ-1 توسط سامانه پدافند هوایی پیشرفته نیروی هوافضای سپاه، تحت کنترل شبکه یکپارچه پدافند هوایی کشور، شناسایی، رهگیری و در آسمان غرب تنگه هرمز منهدم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83482" target="_blank">📅 09:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=cRBQAlywo4IGI3BuOmTaCv3WtnY1fxccpygbyh8d27B-soeWqWxTvfC8sKnCi433k7sh9HI9lmKgTfU2QyLWpjwXZew7x8RmntDySSQlhfvyPMsK3QcEUjBAbVD4k1xIpYRbUb416IiyTmmvS6q1W9ro1Tz3fWJ1sMgGAwYpFES6YSWXbEMD-JZIM1sMPFxBunC_JufTpW1T-KeNgM0O6Oeu18rEQ6OTVdPu6VfU3CQKWloLv_xY1q0_4htyHK1_IE_n_JwQ_lLttak-vHCUbOMDHeGpGer9ibpdhUbFZ2khFRBHkrtMcs_p4Kn3drp2eJGkcPWBmeItFsniKBuSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=cRBQAlywo4IGI3BuOmTaCv3WtnY1fxccpygbyh8d27B-soeWqWxTvfC8sKnCi433k7sh9HI9lmKgTfU2QyLWpjwXZew7x8RmntDySSQlhfvyPMsK3QcEUjBAbVD4k1xIpYRbUb416IiyTmmvS6q1W9ro1Tz3fWJ1sMgGAwYpFES6YSWXbEMD-JZIM1sMPFxBunC_JufTpW1T-KeNgM0O6Oeu18rEQ6OTVdPu6VfU3CQKWloLv_xY1q0_4htyHK1_IE_n_JwQ_lLttak-vHCUbOMDHeGpGer9ibpdhUbFZ2khFRBHkrtMcs_p4Kn3drp2eJGkcPWBmeItFsniKBuSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83481" target="_blank">📅 09:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ساعت ۲ تا ۶ صب فوق‌العاده اس واقعا، ملت میخوابن سرعت اینترنت رو آسموناس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83480" target="_blank">📅 06:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3YN3o0sK7Rh1z_qaYAWZAqc26CjyBWPY734I9Vjv-Eq7sdfj90KDbHfjMH5H8dAOW7jh5JBbohw7phnlfv6ekIA-MZm9yCV636pMXleQjl8So44KFmDyBptJKRkFCaM6sN8JNTLJg8XxKrEK6j9nD_ArOzT73uvvMcyhcEQBcsWCn9A5mChkEELEMXFku1E4oOlNcQ0cWoHz2jFeSIULleWFa8xXCUWx_zXVEjJLyH9CczautgN6nQlBmfVlO5ctM4KTC-fo9WZFr6rVBhYHybBUQnrTkBRuE9Bj07aRJBnVBvVrN25iXG_ZxafuUIgayDS7fvRr-0T5iE8QqNJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOSCKVu5x-SUMpWJkwFIZGZNZkuWsHNZIDQ6XDoiQW3ije793Id1X6J36JK7eJiauXcgJ90cOapjvjzNRYtuBSGzi2BkA2jUAg6f9cctf1JsAUPRDK3CGLj_-k0aEJqxtgTuvu3oMvBLtD-IFEGx-ToImgk1KQTRKIk15ne6MxOxjiK3IzZkUP1cCy6LFSEet3h9bWNKF4la_TNYMHZs4Hc0ItRMrNuNgWZxDhtL601jzZ0YSBihQQndpca4RjJeDsa-GQZVZW-f3Jp2KHFS2fNxNPbvX2UcVgYFim52wOpQEACgFf7zPvsb4Tn9xMYYxsqxRBGZBs64KNg_yRHH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOg7NxrJgFDlSOmPbXQn3A__5nRxThtpqg_9lpiaZmGVf_nf01aHjF2yYVEPud5XGDHCxrNkplbGJL0PVKpCkCL8L2iSI8qJZOHoKIAUdGNu5XlnRwHgiAganLmEwFC4BEAiOyVMJEa7KH0uWIueM3rkdazjWEDYwHHbjbVMZ_xNMVrMjTvcD4WxxoRwPRrmHX7fLV4GMqTkKb-AYgrlE-dSjlHOCu3s8mEbyVHj1feRzsDsozzIYletT2hBXbcQgY2rLgA3aQyu4sJV0hLcGBowDuOV8_ixPhtjJ3amIxbLGRly2cx3J5i9rkpdMr_9Dlot1rfqqUazO8KbZ2bmeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تام هالند از زندایا خوشگل تره</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83476" target="_blank">📅 04:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KizuvKBTIPHDqRzV_IAW5oMx-Bvx6T_oPEv0XHol6cqRx8udjSkDoZPvWSWc2nBXRGmhVv_RkZXi5ESQRGJ_byoJpX5fymE9PNT8JejKNEPk95nRfk9woTf0n1GAU6gYbw4LWNhs8_ZwQjUA8YfTMR8VUwPc3J0LtImNj3IIDJqCxzJvLRNmcf6vjhjlkzvHx0RAPB_DD92jhUr_yqKs0gTPUui29tMweMjU2fIbz8d1WsNYnXmw8YESkL6LbAYn3ygNcfeZzJZNxqaoGVLOjCpbtJTFA6em-TUtAmK3S5m1OYHvFt3krWT4YG91NSdsDmwqxVSZhWCWD0iEK47ahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآ وای‌لی برای سریال "The Pitt" برنده جایزه بهترین بازیگر نقش اول مرد در یک سریال درام در مراسم امی 2026 شد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83475" target="_blank">📅 04:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bpj4cqsGS_X9i7CQ-KPU1dFSk0-KjdXDqVQWtUUpN8zv4tNlBjp01nT-ukQ1_0KHXeLvD6urzxMeGMRsu_B4rb3Co8i7NNv0T7EBWl0wVyna7UpGqbKy7M-JgyLz5lgCL-0ZNJzfMzBb4ZbWwrCK691Xcpgij78YCSd4VdjH0zPy7lGyQTfJEZ-oHFWhY4GxvZ77FlTFNpIQQBJbcixW7KjXBwzFyb9IvYP3aU7in8U95ltbVEIny-K24TEOQcmVxTHyWOoPqRZrkbZlZGmoQizScGGgARuWXO3g6Au7QrRSWsdy0216u30HN8II4ItZZfrO24fp6J-LRIsmySf6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ujl7OL1JxWPmi7EtfMCtZghOkTkk7cOUdICfDrqAxuWK_EuNl05_4DxLmZwT7zNiw77tu1Oa3AmlC9ZmZ7KKNsiBvQqbanq5FNoIwWLRkLTzdstKoyxg3IO7KXRf9FTrGOmi2hvbBLGo4HRBj7gROmlQk5sELwoskYLFY0nr0Pw8ZtGZ_XoW3zH6LbzNYfvjTqZLuQNnHeOkaaN9bevWlrNQ5cqecaSptS3Eh4y-GUqUi00SVCF_cVoYk5bZu_tk8cmfZV9xTpgg6l-rbl5PYL3zVUbFHRpiCa48cHXuONO9SVuBJd4Kfv6O1CUipdsGQZmU2WnOk3_d8NUqByHShA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سارا پیجون</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83473" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83470">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwTgcavvSSRkU_IjoZ1Xh0z7cH8g5kW2nDCtbQy7d5Yzz8ZOfX9av-yMnFmmLQf4exq_orlP2dny1iwdRMSaAWi1zhS__PTW1lZzNsc6hPRPJSIH2Pxxcm0We9sHEBU8wAEyChYFN6QkJ0x1XMLZx1BQS9Kiu7BTlnltzJs0wtu5Z3pCQeZTl2IQkjBbuiHSIVJUFbakpzn39sXV9tRue9jNviISxj1EmNHaLgJBNVsqKTYxQAzgw8OfNNQHgVPH8xFdqt77R739AiamVyOyLtBo2Wf5_tyoQpwYorxThjEcrqbIsDPy4_H2UqEkhxyrGLlJpxIe_KNOlYGvCpuQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-okIw6LbBtTAQZKM3AD4qGL0tKAUYOuRowHjAYKAImV97QZkb1GmW1uD-DqLZjkYKNUzY9x4CwBnVpOY1HokAmRCw0PHN0Zo4dyJacqSgJe8b0i-NCcB--1Crb8nvl4SqzwmkRC0ptGAGAR-oPdU_uvk5_PlwEx-6a7dARv-u9DsVqluDg1RWrh31CxfGdzxmUtmuFtpjkmZhjDDE2jfDtoC44SKpPiyt8imvu_jDA3Z5UxTI_pNHd7V36IVYG27onv6ztugGNXzfKzd3Ox28uhZTzhTj-E0klcqSXQq1jG5JqjBleliBKVPKCmN05fNdrQK6HocBqfmFXNT14dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا اینجا کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)  جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)  متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)  آلیسون…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83470" target="_blank">📅 04:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqB2DqxeJRTCX5nwvquJUk93O-0vCQmJCGacpUNHMrJgk5Yrp6oOwUTYmMk287yw0cUUWAGR0Zmf5ixsiV4gJUsPyReEfWek0fRtqgXuKY63P7T_GnHwURAJe2Lhj9O1WlN-k9fr53RugdcMP3ID9_wrqCHaz7KOex_1ALVSafxRkIDikmXTKsW6kpQp41v3oGeYqLai5ujMI0aVUahNgn73ahbRO8g2945HmmJ1pnXGmkSqvmgn5f0ogE1LzScnmWqX0NUJYI-jC2HiCADRven7FDhjPotbOI7uEdZeDlDT58OegTaamHTtTRB9itGo1W7DTSy81X_Y_sBhKeuNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsQDnjUeg0o9Ks6kArNGBtvc6M0IM1BmfBsncrWeUAu_0c8Z348UH1N4geKnBdYhzsnG5Eji8vl-Qn48LDSxLqBJPA1lsEA2t8ttNaUGIDuR61_HwC6tdKPIez_Jw70kHqquc66_d75JEuvZ38iaZlSfCgnXCnS1fbkWGawMoAof1tT0_5HJKZLvdkt5nWazcXAukBac2AlV5VosMGUnTux-2bAysyjIaF_ng5lCqpjrQdUBk5ciddRwYinuHclaiMlZ0AnBQhqe7EGLhR3nw0d2QnkoRAjCVlr-E1N3odSPk01vOz6lpXFlxLWpUeYLuD6qBMF2t3-MqbAcLbpbvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما درخواست پستون داریم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83468" target="_blank">📅 04:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تا اینجا
کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)
جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)
متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)
آلیسون جنی بهترین بازیگر نقش مکمل زن در یک سریال درام (The Diplomat)</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83467" target="_blank">📅 04:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCqvazrmMslgzWL2kmfmw3LdkDKHSkfRtzkR9t82oEV2Tcy2h0LsBdga-PPFsmcuKTldMq-HOl-mtX0uaUSo8z9iQ0SLWBi9_sLYzBlEOthAjytAuQvshWKRpCu1Kf6zt5x9a_Go1j_8wdtRMuznzqvCm5Szsb3JYiyfQOidqrcHW8rXqZw3Qjl_duH06yrPYzeaV2uRq2RtsI08Ljl_76TMcvXGIw3mQSp-1ef8qz6UCNu6NRggMCKC7t25VeBlMLAPmBKmeHJx0AY677Wyzfs5DX1rufqrjxbDe1PcLC-lvgujTVSPTj4tYeCC1E0XAUwgjZ7FTQJmj3WlCo1xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMewSrghewyMmAB35PEmfHltHc5m2XG2nC8G6jxX0hyqgx4qkwbuUL_rCMnN4RT0JaeuI_iJ6tI_MAW-EE8bffBAKelGSivAB5MYq11Uzw2MhNEuVGvR8jL7c-iS1_WAaVPCFqn5MrfzMGAI6HLLnPXwfPBeC0tz1d4Piu7B_JZKjziWU5b2paJqo-m2HIpNXmC-sd4Pbx-yf5gWev2jdA9Rb2sr0rADf21k1bCW3jZIKXUZZ831IA9IDYCyIerfXPRyIZuixj-fBiz6r9v7MgZKGpn6p5r6VZ3MLku1TRRCyZcldZZY4UJGXZJxr8D5Odr1lN39X5m38EQpsAL-Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اما دارسی هم با استایل تام بوی های دبیرستانی ایران حضور داره</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83465" target="_blank">📅 03:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83460">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKzWm7r8zguMax6-KygqC9n9oE576uYJKKNtjlcn7hR0aksg9GPbGpP7FXKAj2mOyMmDU29u7Xn8WDbohICrjK0rymOi5R8x8xzkv7VMKG_f6MiMjR44xmsuSzGJ9fOTiT7RjK_vtPiBRCRNgVtwvVLp0oXT4yhtH-tZvG3YHk4KIXSPN55bkod23zn7yJHRbkXlI2deu27g4sdEFnc2myoUNO7vjgYrOXUcLWg4WopqTGfnKLrNFivWiDd2LOlbDWkmhi-iQZWtjc2ubvc3KjxPQWh__7ESIonAgll68Qq5cDaBZUcxUvTivMA_084NRyOEWOjDcXbuz6ymLHU0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB-q4A7bBJljQ2kWC4Pk2v6pRj2ecO-Gag0luITz1xfuvuP7nnH8wTAv_HRjkXwutlPuluYAe3feLhrQWv8OcGfGRrifMTmGEUske00zpVGAvyEb1e1gCRRtGQnMFd0_BfGmiknLOHuaNAD9k8m_z4-VQYqgaDeMJSghhRXvCOFCbqcXYOsXE2pCpmg1ODfPjrBV0-Eu7HXRgXC87_T6Jm-TJJ2iOHIWF3ZK8qt8baLLBA_v6tBKdYpnpbazhHOYjUVKycXEYjQpQWBZed3RAiX3l431Xxw8Sf1pOyh5MUrN-tn5G2ZKoOw_NQ5vjSDGyOkc71w7moZxnnCy4_czYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FedvzxwR87tfv-5u5eYIOX5l6tDA-Kgp6FGVMzw50hF3QaYtyIXWeyajSudad3edS9mgsFZ8Uy5oA7klmqwCRwzCAI297aXwFC8P-l0BWa8R0ZeT5qVHq9xlvMgv4iF4hSEDEgodH4Xo1NTUJFpiEuEYCR3cC0Rnt5NoSVFQOa8jOhtCPsIGbuJhif0_hD4pZCDq5md4WIfW4GejeyUvrgZC0EEb-2xnJiHAnkHxQbs8A0nEZbXhjtVbRVmSt6sq4cx7CGl6trhfbX1x93V9iQMNmwk5X6DK1_dyJhyyVkO9Pvaxq6brMVT0S0yyfggGr8CUG84XyQLUsMNXwvjVnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپیده خانوم معافی هم هستن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83460" target="_blank">📅 03:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83459">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5zJsKY-2JlfrAcyUNuilRF5FVoP2qTv4GlCGKz5bj-rZ_eHw5yTga2rRfgD3WUDtoJrfHi5g1eGOUX71VtJO_Kyv5ItC_OvW9pWvD3XnnQxCD3dRexP4h_e4JsZA6PtNaB7XHxsGfoox1b25nDoqPI9mXI9RhgnzqyS99U5Fs08Iim4x3mNmcq7nDD1BaC16KX2Dn_v-ppMP24EtzMP4ny_3Q9Dv929l-baXgXf-lk_O5ASyuqAHjrksZ3Jj7MrpiL9v5IiPDzZDKKkMODDV3E17QnphqwJhCe4xF_6r933e8D6a-FxsHNTq-0maUolHi9WHJ6vempsRc0Y3QGfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولیا گارنر هم برا خاص پسندا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83459" target="_blank">📅 03:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83458">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaQGy7Ls66jJkQyb3Jayx-EiavxLGvNLE1az1__WMznJ_uuVnH3lTMihQAnzBcdn0uhQ0XMM8cuKbHY7DuMTd3ic1d_AlgNV4D7h3oTWnR2sm-J4FYpvg-KMUka_TuTcQQu9UDNhJo7q0fRutPTMuQU93v6dKEgA5X7Ctyfxr9s4jiJPyYh5mbLFbsiNg2Q68W5QZ5hetqs8jXm1RJzjyXPrE0FkBxm4cQtLBCG0CtVyYmO1M34y4oOWraYumty2Y1bnTW17NwQLz2WyNGtjlFOjGNTAdY28L5Cu7TtbWs53OG43AFNToptdLaT70EScuJCRdLb9DYcCd7ach_m1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلورتس پیو رو پیدا کنی و نزاری ناراحت میشم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83458" target="_blank">📅 03:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83457">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c06_RnDKAsRw1yswq7wuFjNjyJL8w65KefECHYceaH7MPEQQGpIFTxhKe-1U0lJicTiw5gCj-lEy8Mc5Yt0CkuJPozx8KptW1m9g1qLF42YMYqkkDOt9PO3By9bQwhuMjXziwUPNWjPampxXvJ9WEHwSnNSGTVS7WwXfkJXmHRXbbJPZ-5pWLCwOJZ4JzmTVjYm8JQoXvm6K8TRNNvjSwcJR0WqiqHo744A54PiRMOgMOgpn2pBtLCAmfVu_fPjZuPsnAczeeNdlVYbSrThmNIU7ZFjAup-zx7oz5OOydKGbIH3AUDkd4z-IMXxD1aiNMlsPvXEcQKFwnKe15QVFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهرنگ خبرنگار اعزامی فان هیپ هاپ تو مراسم امی حضور داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83457" target="_blank">📅 03:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83456">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Artb3UjgOAeGZgxeRssl-TqL_ksse1iSHHln9Jdu43xJGMtBVuLz3ASUpfk9ytWNMG88mvB_is-pwY_-r5lmT51ECvcX-qrH71YJNmyaUdC3fkNye3-4gqEclYB3KulyCsPi8SocILPGgr7GTTshF6NA59uCoVk_VhX8475IWzOe2GfHYvNznspC49x8UhGllj8pRs9M1eYmCiI3Yk6Do_HhlTmlc-8XzOKS5UherazG84Hr4E6CIMWTPx6s2rCrYUxz5seb-43mblhx_nqts_sCBWwxWEYlo8EVQ-KsaU4Gxpr8a1HrWGax0LV2xysvjiFpohlhdN0sEM16xdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندایا رو خودم نیستم ولی شما ببینید</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83456" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7xh0YetJBS2XRB6BpIQGzb3QFbU-ymFY7g0CNB-j7u7UlSXh8nr7Cti8jG7yzprMdgRL1I7ZkUmtB10Wc63QcUDQB1vRTMeiY1RvKNXBc5LEt2PRKJP-FNjBh8m-yA772IQhsErXCu6knYxhbWuxmKDx5fozFVjdYOpYd9sWZg7je9P3Pn28yuPZjo2fgdjbzlcFoUFAs1xVHCo7KoLtYQ-HyUtmxGvpllwKxVYXJSXKoOJj_6WuTl3BmNIfGFZLfktDdYVJzC9NVNafilbqmGYFx7Ijn6vQI4jqakUOnRj2l8nQgb3w02fhooLfEfHXy9fQtCMjLMRf40CarGTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای ال فنینگو بزار زود</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83455" target="_blank">📅 03:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ببخشید مردا رو تو چنلای دیگه دنبال کنید از مردا بدم میاد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83454" target="_blank">📅 03:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxO_dta7zFS3qwe54qj0bPLReDtPyKT-iWs_FWDoORYzSL16QuG4zy16Bmsm-rRvNDdMmlY2bIbS_3pYI0IdxOflFUEhlPYEZUShoIGXJuYEV0WweRzBr1xFLhhhX-MDH4CS2pnl4s3c1u0d3bU8jqs15j_sdCAagIr4VmQegVDKbfKYQNQE1sgeXGRHpFbykP2WfTLSonGNBM7gQdqcZ8VCivZgXZJ_XZByky97lkUOoHEWhp_0m6vN1q6S9HfdEi6nqsP2p_kUUhO7r7Z4gmYMf8I_Lzp1TN-5uR0kgAzeGDzCZGblzGowmp6JuS_0CRng5nkUcCWUTxJS3mVpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83453" target="_blank">📅 03:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83452" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvkwc69gnHbnLR5CixRZvRUa8kzc32wcN5ZHjDY-H6afGzZtDBCcy4xtEj3ltR6tqnQdHBoNWZHY_N0JeY_nd3cqPFUiGXKcLK7tQSqgIaHtloksvniRxWe4Drf0_zBFGIhu4A0FkUvxriFbpU5k4s8VfTkVMzh7uoFqiWB7otsweSXRQt1mANGkgAaO_c72bpAxH7eNIeqjUs3L84eQG3O4x4uA5eZIrJGbq8THA1pcdLwB5MxMa2K1EJP3opFkf6p0Qsiq_tMrQRyjE806Qdho7lrSaRpDwy_TEHuMuqnXxtfKJsa36WNtB5X8fwgKqLU5yYX-h-Y4A17cC4gM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83451" target="_blank">📅 03:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwqPusWRtPsKGCQ3WEU-jP8fpW1_5cQ8G3w1-yCMjr56kKMMlzyTYMeZIvse9Ac16BfrPkZaArPXYt58SI6fFB1LdQKHqyyRjd2R-jRCbTacYtUQJkKGYTQPZcobuvI2NOyWSYt4-8s6VKPBb5NZNM-dJ_81rG1ThRwdSQRXiFgcZBD7I85-WRRp-geZc8MZaEAYGwWT_q4D4T188YGi4fKTn51zZmEvTaII6cmuAqCAvLcThgiL-TOPFWD2e-Dog1qWNUwjz8gveoCRi-j04Nka5QoHP3PsqHGtRhABGje10J_dg8vKvgSaYmZa-oQ4x5SZwKeMQg8mjjKkniKRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GC-v-ujHNhNmf5p4XB_QgsmHX5qQpe_1MtB6-SVPwpWydOAmKCowZMLovnevKFtN6dSgg8QPgWoZv2GprTBBk8yhqfuojLc2heoYmUQYDVQgc75ewfXSEIwd4xVAmcDdGH8OM9ytBx3IPEZnUWBje8EGxI7hd47kYZpK9gG9-hmvBdKalMIKAA2dbJTS9Ne-90T-pgRqwF3Y0pZ6RqQKgIe5O3OlQAERfcgyei9yxEFxdWQe_uRCWr3verH3FzvIHT7T05Ab-ZpMIQF0vb6nqqjqysDRrrMF3SxEZ5TbnLdNL6HEVlaUDo47li2Iv2ZH0v1HttLhQO32E_ckaAO4tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو کیدمن و داداشم چارلی هونامم هستن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83449" target="_blank">📅 03:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0pULmupVQEd55fvXpYWw4RJr4MCxIVRb1JZ-tXfXll0US0onXFtYY6LehqVv7M81qiTbRxcYnGByWtYdOA0nezLlEiXOnFdPg88uEAZyTFiP-tfddKFQI_b6peOtJDotFBD0lHzK9pAweu9COF9p4-WApDYH4emHXrc5l9pdtO0cNQxsmXS53eHvaevJgYYYcUp7IWtt9I-PzAwiwJv0NBlwE_oWK7Ai-p9bvrMhs9MPSWa4vQW2OmtrhbYvM2lf12pEfYHjtzqPnvvjUA-4UeplYr9X9HLPik_X06xtEr9ySwctRzdhUBpAE_a5NLkqqcDgdLcZjRyVdqGh4NYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83448" target="_blank">📅 03:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83447" target="_blank">📅 03:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY87vZ2Dc3vPC3y0Na2qknq8pY0mErfWLClP8d5-FQOMQLrYVmlAvAnAAgSva_El94tOguEVDMtfvqEq8M3JGxfCQthb0EyPHqESWmuWewnR7-qUmGObeDZCoODm6RNNHWSvDevHNc31dLmICCle5KXS66gqaFiFVqwzXSt3UiUjADz8ntoWvJkbVYK_1zXFVmpZlPmwS9VAhSlujVgeG_ty3GexztW4CXTicJexyZSMqKAGZpPH4KrHz2hNe0b-6zIXmuhpTXJmrLKBnxsP-FotceQO2zHlPiANwnYkzis1RRIfDUHynmCGLfKBoC7KESDqY7K6NXkVmwt2jZGOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی زشت شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83446" target="_blank">📅 02:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=n9z7e-HBHqJngt8icQ05l9gW4In1prBALH_09o36PWDXsBdxuAGLV1jwPOUx94MpdyXwKJ6_5YwR7P1DywlBbUkg99uwYL4GvousErVBnLmiJTnivo0wev0UOQVQhJl51K1LO52QZj1e92BxdlEUeNR1uOC1KXIT4IzchTloifxINCChtBKzXuP71AzFtZxVvJ6anvuOsbonuPuRFYcSYaGCwqBK_onjX-5zNCfweTZ_XCbuNMOzCcJlYZoy9pYmc-DNHpETGk8GBKsmFVyuUlywP0DtlZlwIeNAU261IsKPuo6MH00-AwdfgGfDIa5jfDXnhVDevqIBYc4fRevG0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=n9z7e-HBHqJngt8icQ05l9gW4In1prBALH_09o36PWDXsBdxuAGLV1jwPOUx94MpdyXwKJ6_5YwR7P1DywlBbUkg99uwYL4GvousErVBnLmiJTnivo0wev0UOQVQhJl51K1LO52QZj1e92BxdlEUeNR1uOC1KXIT4IzchTloifxINCChtBKzXuP71AzFtZxVvJ6anvuOsbonuPuRFYcSYaGCwqBK_onjX-5zNCfweTZ_XCbuNMOzCcJlYZoy9pYmc-DNHpETGk8GBKsmFVyuUlywP0DtlZlwIeNAU261IsKPuo6MH00-AwdfgGfDIa5jfDXnhVDevqIBYc4fRevG0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یعنی جدی تو یه رفیق نداری ببره درمانت کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83445" target="_blank">📅 02:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این چه مسخره بازی ایه ۷ نفر شانس توپ طلا دارن، قدیما قبل مراسم همه میدونستن میرسه به مسی فکرمون راحت بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83444" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=KWfkGVTFBCkJSfl7pq3aIUM7p767_Upz2grWhy8phpW4ENU-WVytg5DSY2UG2WNL8jfg9xZBy4v_75-MbyHwIdA2oziyKDO10OmnafkyaWMKpFcW-ipFE1584xfsi-cUHpLG4-3yOvyIok5jBtO2fTvXJ-pa59OWsiRZME_Npxe2dLt0UyAsd2M1BcCHtD6fM--n9GX1DUOplGk41-B0H3-2gDt3m8JGxbmeBAA13vaVxLHTfZRzc3S_ERF4tOb1kaIMBLjA1-hm-P_B5ar1xbvmdq-5ojoxPx0lGd0QPgKPcQNt-zwsK7bBxjyYZZDbevP-8G7ge1Xa2t0fq1s_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=KWfkGVTFBCkJSfl7pq3aIUM7p767_Upz2grWhy8phpW4ENU-WVytg5DSY2UG2WNL8jfg9xZBy4v_75-MbyHwIdA2oziyKDO10OmnafkyaWMKpFcW-ipFE1584xfsi-cUHpLG4-3yOvyIok5jBtO2fTvXJ-pa59OWsiRZME_Npxe2dLt0UyAsd2M1BcCHtD6fM--n9GX1DUOplGk41-B0H3-2gDt3m8JGxbmeBAA13vaVxLHTfZRzc3S_ERF4tOb1kaIMBLjA1-hm-P_B5ar1xbvmdq-5ojoxPx0lGd0QPgKPcQNt-zwsK7bBxjyYZZDbevP-8G7ge1Xa2t0fq1s_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83443" target="_blank">📅 01:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTO_RTm8yvtlx1awjw0B2HthJ1JHNkctYvII_jChmKxN5jAYn9mvipGG-UL1vmH-nLTzr3r-gkhdzLofbTtnFBvd1cuwYhIaNKm68ATmrMRElF2ap1DJyHHfsm1Wfgf51qMSDTVOEUuMNXm45BN161y58XtdCU7zCUHWk3QTqL3TjhdM4adkZMzWLCbQGJpDWm2LEiqhxSmgJd7GLZx0KWGa7e1IPL3talVU6aa7EnkOcSnvN_ycnKvReTP8JkA_LjrLP3TuRigAUJU7Hb6d8-G-nSE0MYIUyrjQ_-sxoJbxG9r9QdwhWiVA3za7WWs1FGM8LTmwCQvntKXtAHXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد میگن ایرانی فراموش کاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83442" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">واقعا بامزه ان پوتک و آرتا
پوتک یچی میندازه دو دقیقه بعد پاک می‌کنه، آرتا راجب همون ۲۰ تا ویس میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83441" target="_blank">📅 00:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixO_F2yYgZX44IRwcYpl0E-WPaBoKLo8jbzXu_K3EVrwgXrjz2ClScFg2Se-JG-smVVazcl_Kh24EtTNdNT9Kfj0jBUADOYPexSvtL0RUKflF1JB3t_WguslDE2razhSKbvTuaVm5g4lNW3fBfBfpOKSBb5_qyJJaz2cNr1mTkp0wkgNh_neiSuYwoyBIsczC6IBplEFq6txqFwAO4tuPSK-5JUTmQNQDFLwX_JvAr3v5ZUtsnVBT_58xaBqRuDNvtFoZo-c6BOlEHRK7Vj9LDJA88h8wYCGQxpPsxfRVa4l4BQeise_KMXOlUaaYRFaqhSL1Pcn1r1n24XiCuv0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک بعد از کلی ویس و فحش کشی با آرتا اینو پست کرد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83440" target="_blank">📅 00:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOi7v8dVyKmk5iFN51uQuBsaFITiuxnU2ENc3JkES6Qfuns_PH30xfcz695VhyUMBCgFf6Cc_92b5Xbrd-AlXaTIOS3VmRk346so8tJmFtqETPThELrVBUl6_BnZ5TMSactqVgg5b5hDG0skdil1dZHzULoaS0rpo2eCUtPdG6xCeWlNB75RTec1mWFyntn2GqkWCVQWWHP7ybPQDGnBDpAtNc51t5pXQSbqXVieRYkrNGEiP67fBfwhjFjz60VFHmSPvQnjQGAflaXk23ga-3U5DvxRfKhT3IPz4JyUROhYS9aGirj7__KY9MrvRPuOzY8mUEdTt_QZFdh7BGds_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم سهرابورینیو با 137تا پاس صحیح 3 تا گل به السد زد و برنده شد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83439" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حقیقتا هرچی پول بگا دادم فدا سر استقلال با این بازی
مساوی میشد فشار میخوردم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83438" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برید بگید ال نمیدونم هرچی که دوس دارید بیاد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83437" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McjQ1nThASdiHURft26KJ8-tG2rXuy76KnaHROQVIG-Xi07h2_CoSr4SI2z5zn_WRQKQhg8VUKnW7FFSAJiHHTargh-Kc9jabhDgOCkRdR_pjFV2XSh3TXlKdvUql-TUmnVAhS-liOyPmMdJ_4GAv5iKNNLz2NEaOtMMz1QlqundVJQo_AeGr2geUrMk03wEBp6-xVJQ6QQ7HzYv9x3P2WtR1SA_-s12G9ZPPlFyWXdQ0Zmrdu1g8t_j_Te_GDERq57MM4HkBqqMcwysMAxpG0fXqDgTj5c7NyaFfKMCEPR591V07cRTQs9Y3vtm16qT1U0tcnz2AG4JNoDaKvxlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداد عادل، برادر همسر مجتبی خامنه‌ای:
آقای مجتبی خامنه‌ای عاشق سریال فرار از زندان و فیلم‌های کریستوفر نولان هستند و به من گفتن چجوری تو کریستوفر نولان و موسیقی شاهکار فیلماش رو نمی‌شناسی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83436" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ویس‌های آرتا در جواب به
پوریا پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83435" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رد شد گل السد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83434" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه سعادتی بالاتر از گل خوردن از فرمینو</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83431" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یچیزی بگم نخندید، السد از جام های داخلی انصراف داد که تمرکزشو بزاره رو آسیا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83430" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">استقلالو</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83429" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از بازی استقلال کاملا معلومه بهشون اطلاع دادن من رو السد زدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83428" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83427">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سحر خیزان
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83427" target="_blank">📅 22:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استقلال یکی زد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83423" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83422" target="_blank">📅 21:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اوه اوه دختر بچه ها دارن فایت میکنن
ویس پوتک خطاب به آرتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83420" target="_blank">📅 21:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N85PasrumB6cYoYcj1Km8uFTXbpk4Ty-Dfb6US0MjUAQyCXDJR_0Pj0CbwMFFAx4N8iRYDGB2MnnUNL6VLgL8vLy_MyFOZiAcQgs8H3Bz0vypC7M6A63cSZ37ueW7rClOCxQnkr1izrAYmQ_StcmV0wZonWilZMJNdCD-VLWOXLeD9oJVPPf7xXSjsQRu9oiUnSofQCPbGJc7ELwpAWYdU-AaXeMzhF9YAbg_xp77Rbx0xS08KnKV5UChCK72mhaTUqkvhmrLS1qh353hDElrTfHtROClXwB2EVC0DRABo1Fd-www78JS_QR68VTw1Ci7GhQTykVV4h5E_z1kYPfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها این پیامک چیه برا من اومده؟
ممکنه منظورش این باشه که یعنی تعویق؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83419" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=Zmsm1Xy74PPFvxFQrqKfD-39HfL3J44C60ACHgN7k7Jb3ah6OpnnkuJFIVgMuA8fB6TByI-z-XXJvKNNp3WOYT3Z8RhfdToYpdgJMzWP05-coKbTWYgTjUXunx9xZZGTIBoybNcTBiHwTl_4qtEJWoFHp78td_0KExI-toDzzPtxE92J7-eF6QENJZep-noT5qFy95dVPzC7AdLdr2nzTlxdP5HeUEQMiFZ70odGZ6efXyqEbALvqoiyylm8SWGZ5DTERFSGD3tukIaA34j8DvXyt2m6ZSw0PLseW2Uq_LC8xUULQsPPW24JZcJ3W7hg6WJ1XJyOJ3gdNWgVAVLEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=Zmsm1Xy74PPFvxFQrqKfD-39HfL3J44C60ACHgN7k7Jb3ah6OpnnkuJFIVgMuA8fB6TByI-z-XXJvKNNp3WOYT3Z8RhfdToYpdgJMzWP05-coKbTWYgTjUXunx9xZZGTIBoybNcTBiHwTl_4qtEJWoFHp78td_0KExI-toDzzPtxE92J7-eF6QENJZep-noT5qFy95dVPzC7AdLdr2nzTlxdP5HeUEQMiFZ70odGZ6efXyqEbALvqoiyylm8SWGZ5DTERFSGD3tukIaA34j8DvXyt2m6ZSw0PLseW2Uq_LC8xUULQsPPW24JZcJ3W7hg6WJ1XJyOJ3gdNWgVAVLEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هیچ عنوان قصد جسارت ندارم اما حقیقتا بنده احساس می‌کنم این رفتار و محتوا در شأن همسر آینده بنده نیست؛
امیدوارم محتواهای بهتری رو برای ساخت تیک‌تاک‌های آیندتون انتخاب کنید لنا خانوم، وَ مِنٔ اَللّهِ تُوفیقْ
🙏
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83418" target="_blank">📅 20:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آخرین باری که پرسپولیس رفت آسیا دلار 70 تومن بود</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83417" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
