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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 578K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-100084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXLFKU7LkU9d_Nv4UHTIDZpMT31p1tEFt6bJpkZ6AUcqI7ojUCy8atY_BiPcoNPLXzNE4OasstTzeV8e4eixowKClgvGMaipJPhS6Q54z9UcO44MjEaz2ih0KqPGUotXQeibZztpHHf3aPCtXmXCji66uws_T_lc52UGz8ohYVcGGhxSrxVzGPRGCaoHaAA4bsoNdhSBb86197wr1L5KKEUrf9WbMkRtGsIK2ep1YCDvZrQBSi_lf72N5x1mL2TWWJaw6i1SnOgJOusX3GpHPe91lUpIk5zUWejDuQ7rqx_MaYybomVgIgn05iK5WfuFKsi3DlteObMS0NSuRqPqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/100084" target="_blank">📅 21:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZTiCzCgFMs7DdkR76W5anxcXU8L3i2oNVSxCgdcV22f1ZYLJjyFbRXIUPqg8fEUm21ojiUHC904LCGt5v3VZSZPsA-9hyNt3DgvZq559OuE5ZynOjVjuh1VPQTWGFyK9iPlmamnD-h5MZ_u2xdbyXi1iFJj6xG0ns25gb7jbl7Bi1r_-JX8w6DuMMILaSGi7QhaQJNNZL1kkTBap4uxpljW687qxSMEs5Q1tmo1s5C_DfaAz8wHEJ_YoxdWOEeKDsi1tS_ycXRPfsx6Db-KQ2-dRDZ_D3dHOYH4tWesYw4tkefL1WTEJhNoCpoh5CwLyXAjuylSa4i3R6O2YDga5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
#رسمی
|
تیلمانس هافبک بلژیکی استون ویلا به منچستر یونایتد پیوست.
💰
مبلغ قرارداد: 35 میلیون پوند و تا سال 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/100083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇫🇷
ترکیببببب تیم ملی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/100082" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCiSLIj1fAKC1XDuSNhUiAd3-J31M9gWVq9I4Gjravv9cK18nYrnrrsUKXOqX19ValUs-qg71qbhiNZrNbXOFOUwthja-hbs0JCfJYpaUtXSaNprzxUHFUDC3wokUg1xAeTX2yo6sUNEaZLuZr90uFo5vE7uYvlLNmOv2v5zSJwgFdxU7Wutn8NfNwIOSwGaHE-12gk8m1RP8CA2-Tc3Gq2epG_7CuMeaFPu82XuoDnVpZKv3fL25475BtXnN-HtJwP78aA5TA-ynaiEAUzPOfavlCdi1Wcza5xvjIdlcTBLuiRuFFbnoZk7y4-W9poUgml8hJxOOiuAxwGNzOoqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/100081" target="_blank">📅 20:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-VnezVsd0Q-ABSwQFpLfkI3TSND9PnYLofDYGgMhbwtURRhRsWu5MIZ2pM9srTPrxxqvsjvo_UeoG9EJ5nQcqORVNoak-nVyfViHRVxWjAwfJDCda-mbDgK1snpAH2ypryshQJ5RP06Ik3xmYfQkkQu3daaibPk5C3FuyLh0ggd77-bygLCIFmAeDpfdOb4Bk7DkxuYRwDkzupXeMHkDfFIWyK5_YaMIqUcuc8XDhQ7IdLzAf4tAWvSIttHvQGUHoHmbMZUsvW1hvhY5OJYoVkUit7E6Mcq6WBUoXaYInURyOU5-udnhs_xS3gnBnpUUeB-IOupWy5ReIzqxL-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/100080" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1J6DWgGjSJz6K0kTc_0-nFLlJZ4lcj55OkQWImsQv5cqOCx-g9fX76ZyN9W6P-o3byTuAbmLxi16QyN3DKD6lZDOzYe2C5_mHP0wihz1flVvuXfERxhg0sho1NQKXCUAL-pTsDvsMulT2GSA5bLr4BZZ0C6kIpiHt_-TnMQIFrGr33r4DQSPRD-ljYl4pdiwyYw509bE-t1UQcx1uoJQrCj5B-PR5MLhNXJL8ElG9tVGOiOpWXrFMCDt49c5khBsan0W57Ii-2-pQAdt8UQJXPBKVFIfhXz6s8rFcg7TSx-iufrH2ihjuKmMdO2Xsh93vhmfGrlPU1xZzGQubBpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/Futball180TV/100079" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjmYcrCjXOmEUeOrAOK7JOKmWvXT5LCvo3HTXZhHyZct66H1aLVYlxxeUEpr9hueJ_KezFboe6RCIkvqG9VMkOl1zMmVn479T4IJ8UtPiFaVIJ0LfZxqTFVgqa-s-ZFM6w_S0qFVW0yXy1AiUASaCVPH1Lrqk0rJJZ4XUBaOWd2i96RNShgzejyr5qfXID1oo-bVgDXFLNA0-2tbeMUyr03B1hvZcXxA5S3TeYBZd4nRYeKutrDgZypSJhNxRara-xnP825Gj5Cv1JlMKrNNWc7D2fXIR8USzbBfFeby7xVGMx1FmMpdTWcHdPWP1Ls4bVo6z2B6VwtqocGF5P8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/100078" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Axruy9oYBv02HA9Z8liztEMepWD75HQhZT1QPaNvkhzEeXPWkkaGn-foV9jk54xyDS460Ss_JJ9FVe1P-yPMnIz041mhGDDyS7WyL4VWuEPrCBGXL07Ic5PbI7VcwUsPDLtqb-8j78QOwOf0_zoORC_2wISCxHg-lRFIjCDmKFL_eoWWvbvdZ7O4gPsOuOtujqJ351H2uSrSc701mwuIuVkVDo0iyt6cK5WXrHsXU_0TIVZ9m2iUsqGcR8W2c1o6EQ2e2bWIAsZ5p2SPN6Ol85lj7P2XpMjkRMonvzbRgur9fSw9KGOqL4i_oUCqg_Y29jHNqLmy8GOqkWDGio_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در نیمه‌نهایی مسابقات بزرگ، هیچ بازی‌ای را تا به حال نباخته است:
‏
✅
برنده نیمه‌نهایی یورو ۱۹۶۴
‏
✅
برنده نیمه‌نهایی یورو ۱۹۸۴
‏
✅
برنده نیمه‌نهایی المپیک ۱۹۹۲
‏
✅
برنده نیمه‌نهایی المپیک ۲۰۰۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۰۸
‏
✅
برنده نیمه‌نهایی جام جهانی ۲۰۱۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۱۲
‏
➖
تساوی و حذف در ضربات پنالتی، "یورو ۲۰۲۰"
‏
✅
برنده نیمه‌نهایی یورو ۲۰۲۴
‏
✅
برنده نیمه‌نهایی المپیک پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/100076" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km5Yf8oRS3UKFA_jzQAt98VZSx-nGnyiLaXRYLMJ5YYU-eDyXsB-8aO1AqWGI8WZNevON386mwTstvHX0eNaV2qNtx56vATQ_BIa0PiS75lASthGPE5lwJSQh8mcn6d1vTy8-9aEjx2tev3nv47citI7mT-TFqpwh5L27ba-zOTj5y3osrqqyinWSi3slwLjnzdPuyh7OFgmebVG4Ctgkttjp5wFg-auqM0FixuVdk8F8NSMni7sRN6ih8i6qh8i_nQUpcdVKm6zAmu8NRCMD2l311aOJ7jGjg2Q4d9QJnPvEHklMyQb2cWR2T9530VgOC0u-PoQ2YYQz4qy91nX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwUObnvLFI3DxbVBgfSLMseE9Kx3gZyqLpD9lWEuECPXDfphfT6CPN_VEHb8RcYCTzHxaHQzQx1Wfto7Jxz4JA-K-ZbJN2RSMvVgZCaNhNdRr14HvpZkGHw18YhOXx34tgJdYfY8RRHyWfFqZe3GbttLPW-r-ftgvJtpUp6bo2M7LbSYT1QkBXZ6HLlKwe5Ei4WCb9HUwS-3ZvS2zT6KLTsuR9ItacyQGU5DANTt5WXzD18bhhNe9EJJqLaMOMxSSgUrnBBhxIYmiKlMuF9VrA80MnfmwrXYSvuFNoNJs3NZKosHsOFAqcMi2zkwKolvQJ_lX4wb2nHawWOqi8O_Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🔥
کری‌خونی‌های لامین‌یامال شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/100074" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnjdARtXdKhkjK5F9J4ycfrhFNpqAP2n-jF-i5xbqt1CBriaLoTZDjfKmZfo3qga0ZA6BsHU6nJUfYMkYL8WPKKH4SGWRy577LkPAfAYgNTgJ5Pawp1XLt6622GkQsBvKiTFauua4wPJ9cZHmcFlAHzJmKCgIahsmytgEUfj76KunkryWZUSm6RfNgNylaAZRtpge_4lDMhtRbHK1CdCZtgv6PK-BNkWxlYQ9bBZoT92g0kTY0nyB8TF7c1TkSNk-VLigVGnKwWonpVLyCU9GfLiBd0fB4X_mRJ1tCD2KJTC5xmgZT6K__du71ABr7ryPAFDvcSNkIR84MskS4sjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیکومادرید در تماس با فران‌تورس از این بازیکن درخواست کرده که فصل‌آینده قراردادش را تمدید نکند و به صورت رایگان راهی مادرید شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100073" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7DtwBQhFB8lT2mc5opGfyXBKFPGYHKK4AsXN6rXxAbzdnBX3JmmKpk5Io1SZKx3hsQMt85NGML1gD1G48Vtg2oiroYTZ04MpxHUZs7EsNOILWa4TCf2FLqhZlHRQjtxcHXy1JvgYM_5Sg3dAASAGIKeuxVpnlADDjSrfX96_zv5OQDt-nMooeJBKrABFUt3FoxbYvKgr9C_O6i4ZnMUp_nPW7kBlGWO6iVzBwUkrsvDlpo2nJvpNSDlQhmDEYhienRpXW8oLoCgzMOJR49FidKD2CV6h_NPDbCHjpGkFsxUQBx-STAl6Er9brVEdgBuT4NVDbHfiPPG5x6ZM2n4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100072" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔥
🇫🇷
🇪🇸
آخرین تقابل فرانسه و اسپانیا در لیگ‌ ملت‌های اروپا که با نتیجه پرگل به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100071" target="_blank">📅 19:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=vb_yUdio6imkDizaqSNnTSSBp1MSnQ8Uj7SddivOdusutDffuQqu59oEQA7zf5ioz8JGU1jT3gSIJFugq0-uUjiBCY8HPusDW8xjwx0EHmR-lRUfVYuR38Lc_lBHqFHmy85i_-C1edQPxj9WVbCupZ9aoVENrXrkD2REcy_NkP5JE0b7sPS1S3zPrCNyB24E4hqmwSDf8yjQJti0pu5OlgdZ3r0jeOIUeOV5aZ12rWTS6ezc0PBAnrzugx8sgrxTUCnVQ2VaDWVRQcHVynRWzAQpdxF68XLJ85qQHDZJHOPSIMg09H8p5GAqyg2XbxWO5k6CMludxoCbMWoDU_NhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=vb_yUdio6imkDizaqSNnTSSBp1MSnQ8Uj7SddivOdusutDffuQqu59oEQA7zf5ioz8JGU1jT3gSIJFugq0-uUjiBCY8HPusDW8xjwx0EHmR-lRUfVYuR38Lc_lBHqFHmy85i_-C1edQPxj9WVbCupZ9aoVENrXrkD2REcy_NkP5JE0b7sPS1S3zPrCNyB24E4hqmwSDf8yjQJti0pu5OlgdZ3r0jeOIUeOV5aZ12rWTS6ezc0PBAnrzugx8sgrxTUCnVQ2VaDWVRQcHVynRWzAQpdxF68XLJ85qQHDZJHOPSIMg09H8p5GAqyg2XbxWO5k6CMludxoCbMWoDU_NhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇪🇸
مروری بر نیمه‌نهایی یورو ۲۰۲۴ و سوپرگل فوق‌العاده لامین‌یامال مقابل تیم‌ملی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100070" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PycWjF_ffZ3T_0btWxk9RFkvNOKcS2BFSTjawKqWr_huazvQv9-xfvEmt-t6Y-pLPkbPLshtYQSJOIZczWR8rheAEnnULx03yb0DvnmpFfBnoQmmHCEpgiEILowpIa7on1uJfD6jh7hZghbufB1oIWGW1XooOX7LbQ3_lM7rWOvdB4nurpVuHnGsvE4VaxYGaoYdV3heeswuKLCFd_LfSa51SQDHjrgVbAyhYhhkTM4CimEI9_nXILfUfnVbyqcb7Lf1urZOWuQw5-LHazj-CJx8BvFIzvoVlJsxUiVsLSluDY_VaD_eqVG6_wleJ5E-DYkviuSR_csv5_Bnr5zYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
فیفا از هنرمندان حاضر در مراسم اختتامیه فینال جام‌جهانی پرده برداشت. این هنرمندان عبارتند از: تام کروز، جنیفر هدسون، لورا باوسینی، نیکول شرزینگر، آی شو اسپید و روبی ویلیامز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100069" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
⏳
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100068" target="_blank">📅 18:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
نبرد حساس امشب میان فرانسه و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100067" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWieucLQUljovNC8Py4zpQuCWlY8f8V9Av9Ioo1-w8rgAg4M0jCmT9cwVZ0f7CdVp5btHbW4rK8GF8eSMgAhpbCJmcw7rVJsjiD3vLsVMh161XYYTjWUR0kwXWZF0efDfV6_ytbQewSagRVYOz-JIclfpwvSS3InVlP5N-TwRdaFGymcZGbFO87rcvAUmEowJJzsAfPnY3VgrWkY1-JE5TH4BVx-qtQN3qvPdX1mn36DJ5fE1-H04iECtRsAQ_Llf_yK_-d_KSORhgVQWmeSxpRPvBaE0KWVME7UfN6wGmWAp2mnKYN4l-hSMu4XMM3gsbiDi8MgWMuhWqsssxekLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
فرزند کریستیانو رونالدو واجد شرایط انتخاب یکی از کشورهای زیر برای بازی‌های ملی‌است:
🇵🇹
پرتغال – به دلیل ملیت پدرش
🇺🇸
ایالات متحده آمریکا – به دلیل تولد در آنجا
🇪🇸
اسپانیا – به دلیل زندگی کردن در آنجا به مدت سه سال قبل از رسیدن به سن 10 سالگی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس – به دلیل زندگی کردن در آنجا به مدت بیش از 5 سال
🇨🇻
کیپ ورد – به دلیل ریشه خانوادگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100066" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
🇪🇸
بازگشت بارسلونا به تمرینات برای فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100065" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
اسکورت و استقبال از کاروان تیم‌ملی نروژ توسط جنگنده‌های این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100064" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMv2GqZ9An3W6OTBujKd_Yy0x4qMOmtXleCUQdCfKIvE-8mbZAEkMLHuzHmkdxkAqhQdNitjyEfmvjLzBZgY2QU-ENolV9eh5jn-RilB5UAYhql2MqGAylrcmFtbZ9Jbq1R-o7MguBa-GNvxuyte8ALbEe9YTtDreG93hLpbjCrAdibVGm_a4ccKn6J93iAwk7USjmhDK9Pd0oYYSe4rApQcXfkTZfOscP8EyiLZCgF_QzXFKiJP4czSeOuIBCOno4eKxB7wWxSM549ilUfk-q-JxrxL32LNqcojbSBonWjXisXPYAd3qxWur6Ab2q1mxWIAz-YcQNCYVxEADdm1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100063" target="_blank">📅 17:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند ساعت تا تقابل خونین اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100062" target="_blank">📅 17:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1C0NET5S5Q3dWjqxT_HrPBEiU9If2-Ilp9g733TbSqjDOV1jcJHHfqaedNPPuvu_lDkV5kjgBjAffy_-bRGkJNgGxPtosEFDS95MFTcDYaMRWmr500Cs7bBRmj95no2rYiLF7j9ZMZOW-ZXQ1Unf2hzUOk-zkE4nQNiB_kdxXi-GMR3cWJGFelzjuL4OPLl6SDShFKMHsUbGhvWu8fCPsWXQNrjd-kw5pdBvq6R3FVjw3nyarEmdhALlDfD0YcCMp2I0-xefTMdW9Z1LSH4_niWc9iOTw3A1XU8Pnh9VyzTOddTpQZ6qnnnQFGacNFDMppJ7jncnpbkbejt9rKHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری
از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100061" target="_blank">📅 16:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارو زدن 150 هزار نفری نروژی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100060" target="_blank">📅 16:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله‌روا و ابوطالب آبروی قیاسی رو بردن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100059" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_AEa1crOK9KUYpzSAL9nJdi2XGOfDCcACnogwq9WAKQg1DksH-OCY4jd-sJ8wrkn3ErI63SCQm4o9QSoitHWBcyYKoJRCKWTlMaXDo4WGsa7iKHunxSBQDUgsgiB9ZvfirfsPIZuQtYh4kk0oW3QfyF3Hm9KeyE4Up0Lagm0cflrRVnnmtaAgsWcXOKpe4AGtDx6puMlmo4NMqRL3N6aYr3pXJnEc7ZT4Ag6MArKxIwK_MWGm8w8YupAOYtn_u3ZySj0XTG7whLjwOQpVvzQSNPZEv764V4BecUIKgA6HWabs9Pnroh-r7lvllqAJDrLP5bXSUhe7UsLJKHj50bFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100058" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx2D5Fxnmf0ltr0Ej_FDFEGTdF3cBxD5KjK3tSIwb9JUg0UKgqDOCmoEdbK-d-V8bqhJkgo123FX905r1Ajy71U1V5aDETEX2821CF62mtanWPe7qgdhkfEIu2wHqvHj1vzp5pihzjrext6YlNmg4PQc5DKgvCZV5vj8a3cu5f9qX2xFEKaF7SyQOb26HI9ZewVRhV-qTMoINu97UfbW-XYR-MGfxRyV0cMhaIHWrNsIKVluz9qom2hb_WmK4nvnqpD6m_qy9HNyuARrk2Lzj46A0PFV43-xXKlVWR3k0p-8J_iQzI1Bpr90CreBFcjcmRJxVE5X3SF3OXEWSIHaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دیوید اورنشتین:
لیورپول به شدت به بارکولا علاقه‌منده، پاریس میخواد اونو نگه داره، اما این یک گزینه واقع‌بینانه است. تنها دو سال از قراردادش باقی مونده، و اون به طور منظم بازی نمیکنه و فیکس نیست، در حالی که او میخواد اینطور باشه. بارکولا در صورت  وجود فرصت مناسب، از انتقال استقبال میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100057" target="_blank">📅 16:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محدودیت‌های عجیب هاجر دباغ ستاره فوتبال بانوان کشور برای انجام یک‌تمرین ساده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100055" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
همچنان از احترام مردم روزاریو به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100054" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط مصاحبه عادل فردوسی‌پور با هاجر دباغ یه لحظه روسریش میفته عادل پشماش میریزه
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100053" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
در انتخابِ دوس دختر خیلی دقت کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100052" target="_blank">📅 15:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxcgB8nsPxxFx01At-T-qbPaWbyEVEIJDvP_svPi4wil1GfaLnuWQCO7xIGQQye0bkfQvJQF023KI6XyL4jTcNrmz_Fpiav0dUEb_QmHEvWz3zLKGFYskHONcriUIwnziqkW58NB-i3yQ_U6FTuh7mAdBgIGJq0gf0rXEb1IlNH-zbwnen10mtacdbxasA69WffdJNtAbqevyBRfMH210k6gfQxZD0c--WMpDZ9c-5qeKUMAx8cu8a2Udoujj4-VcGGx0y6S800AudCKXVp8RzeVmlABYR7XsdfPOfsApNf8tsPXBsBmanUY8rq3QDoTza5BR60V9sFaUz2fuwYlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
یامال در این فصل، در تمامی مسابقات، 55 بازی رسمی را به انجام رسانده است و در مجموع 25 گل به ثمر رسانده و 18 پاس گل داده است (در مجموع 43 مشارکت مستقیم در گلزنی) و 3711 دقیقه بازی کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100051" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
جو فوق‌العاده تختی انزلی از زبان مریم ایراندوست؛ جایی که زنان هم در بهترین جای ورزشگاه، فوتبال می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100050" target="_blank">📅 15:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تنها سوغاتی ارلینگ‌هالند از آمریکا
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100049" target="_blank">📅 14:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKD7GZjGhHwWccrU2Xh8Vif6Sf6ZQ8rjYtrZ5dC1zvRfP66ix4Qml5aRxL09Oe6CdL5qOgrZzrDwWfDmqZL-RySHXBaYE838vEO_CeGR9JmZyDr3fuaXcO_SeGE-ftZ0f3Ck-jS0ihFXp8bO9QNi-TkOYJ8KUzrQ6nzuvQjxJyUAwzqgFrkq_aQ0WMm-D03wnhj-NbzcDNfH2WBPKD9x6sBvlMv50p4lZcua2n3LnMZUcZxT6hbhlE1iMyTuoypBA_YTnN9pnxggOOu6iLqWA5awSjrRepA3tQ8fsyGk_CvJb39z19vPOqU6ZwQq8dBEXjBVXi3O3VSblH0aEuJkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
فرانسه برای دومین بار در تاریخ، در جام جهانی با اسپانیا روبرو خواهد شد. اولین بار این اتفاق در مرحله یک‌هشتم نهایی جام جهانی 2006 رخ داد و فرانسه با نتیجه 3 بر 1 به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100048" target="_blank">📅 14:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t95N5IBBt39kLy21sztBfaeXCezWhcRa9BfBCxDranTa60VsPhlWgOYScVY-0IDxsvjFRYyZvki70Gxu5ioKNM1-OUECL7ClRuDw_5LO5tX-GG1sPk1pPERFrhcQyJityfOCEB16AOffGJmIWhgs1d8RulmbSNhWHrTxnV6DRgQXAjIBeLKw4DL_oxPbyN6sFyn3fJog0FICORDLSM_G7aL7BQIrjGUh27f-6zk8mujDMwaoyC-hiybXJNShUQetHS8nj4BCYwsITJzzB4iNYJKuHwGtW6gq3EGBvaxEH3o7SE4tp87RKIt2J8ayKSw-V43F8q9pnsMGrRQR4UV2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۲ و فعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100047" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBlrru3acpDuA3ZKUt0KJg2tIIBd0pmVVrch-b5NdMvmSsAJxYNvjiqRVg3RADHWQrLWCGEyOpzNgvfoolULfLmQVR3PqPAy_ecv3o79f7VAvTWegQmiXtTwqnLP0Q4LdTpanJJiBhvJ4ZKIOdtlI7ySBGckCATiY9tWl642k9YNXSUSp2dU-KUbtpbzOyL-wkFRaGCAmSfef9mVD5LnVQkeMzj8gu-ML8E90mLkTko4hfgFO5I3mQrBdcg5ub3OwPxglo1GgmsPfhdZBeCouZtjutpQt0UEGIJGQtaV8z8Ek0ArMOAJQXsusO96NMkAclIUoBr-IOdor65UjFKcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسپورت:
خولیان آلوارز با وجود پیشنهاداتی از پریمرلیگ انگلیس، علاقه‌ای به رفتن به این لیگ نداره، خولیان فقط بارسا رو میخواد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100046" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD8YF3XU9cRtVEhXvMmSoh-mLzlGRu63R30rhymlBqGeAeUp8qCic2PAyv0VeC9cqA4aMmRpy-T7gnVs-vo6_fC0X5NmkHVWvqDMUh-pBaytplbXQ7QbOpze1IKVPIlFu39hYOJOvc9bNdvXGAYvKqIAbz88-NeiWRaqTex32eEV5BSyYULr-yRDOkwSTmwRc9RjNNZF5P81PEoURxMHg0ERjzz4eIpFx9hvN-8nFH1H8c4DQNibYfCa5lpyf3Dbb1TZKrWoUnNmP6nZndl0uklTmLhij9Clh2KtVfKDlXXY2xctHWfpAis7e8O0PDrKQPlx5tTcOhGvtkiiJ99iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ساشا تاولری:
الهلال برای جذب سامرویل وارد رقابت شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100045" target="_blank">📅 14:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
نظر فابیو جانواریو ستاره سابق لیگ‌برتر ایران درباره عملکرد امیر قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100044" target="_blank">📅 14:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2OkSvZkN3nsnJPrLgPlibOXBQ5l4zhFhmG5umljwUx65qARX0tCAnF2NnlwkNgwAi-2OwPfM8D_2CthL3jmA7j15j8QW-pSyNvqShHWdAOV5DM_b51xBqvQJNwcVgpMVUN9AFb2cM53Mr-pcOur-KF3UGwFMdL49lunIwTadv_2weQ7oe9e0hw0PmapSEcu1jjHReL4-w1n4-W3jf3QVS6DZxVqF5wtiArmlfPvAKeqF7p5zv4MaxTcRVcwIpBCWepVgz6wpozV6V4u96zH_UQw6VM1f-DYJqoIZgASKqGnzek47xDhi_FIgr4UrTU12TUXs8xWNsTVlQGgQnFYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
ترکیب احتمالی تیم‌های ملی اسپانیا و فرانسه برای بازی با یکدیگر، طبق گزارش مارکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100043" target="_blank">📅 13:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تماشای فوتبال در کافه‌ای وسط استادیوم؛ دیدن بازی فرانسه - مراکش در یک کافه که نزدیک‌ترین تجربه به حضور واقعی در ورزشگاه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100042" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
موزیکی‌که بیژن‌مرتضوی بین دو نیمه فینال جام‌جهانی قراره برامون بخونه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100041" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پیش‌بینی قهرمان جام‌جهانی توسط گابریل کالدرون سرمربی سابق پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100040" target="_blank">📅 13:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای مردم مظلوم جنوب ایران
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100039" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIF4HJp7B7ig0nQdpHEnmADMtypaVLJ6yS8yaH5ffYautWbUXHRctES4gegaoYFFZN-YcdIsyOBRrQjXNSxyahR2qBd7HVR2Kh8ogywR9TdPrOpPwhprYDnfMo3C58u44x-tR6ghUsDHaty2CVJHor2m24rCBS4SdDI4ox3GeQbiGOtVQgNL6W_6gX00wphTCB6gqLGOeHQN0ZO-Oq-rF__WWl-b-7PTYsXsjbVxMKY8DFJsQY4mqYZTunNhopzWhEtrYjVJd1gI1bl42gbQBEFtVe79Psc1Qv2iHWQEoyNvy8zRWrUbcJlQNUAQyazcjkDZLr0i5PfV-bC5uNPjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
قرارداد امید نورافکن با سپاهان تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100038" target="_blank">📅 12:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
برای درک‌صحیح خط‌حمله تیم‌ملی فرانسه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100037" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm-upj4bm-d_c4OF2UFaPmDMXNnMx_D0826Ik0YQ4zSQvqydT4pu8xRqywIz0kJ59XrNBuvV39KK0yyshTis08Sws31nAOAhWet67aUH_Em9stxoZ0dqpP6JN3iyJXdt0gnXflk6NwegerYImAh19nvmc24Ue4rTvR8lrtTTSPht7yg98pQfbeo4Mt5gbHNF-AeK75mb7TEPYanwNh70f9AaqhCV8gssHtnRipBav0MpgJ4p9gApuInNzC1uGO2WWt5WUU07rO09Y7o9ScLI6CW40Sw6z7xTE3KL-mmQlMp7KsLi90MnDhIm2f6GEjkX0y9_DCm2tszedv-P3mL5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
قرارداد فابیان‌رویز با پاری‌سن‌ژرمن پس از جام‌جهانی به مدت یک‌فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100036" target="_blank">📅 12:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZANI70LVUjDCqNmso27XTOW-UeGn4PzhfjvXzdcu3-D9B5HvPBo8NYsRwQs_ZJT6S6HQcYyTx9qtSe9TIWfPleUPSnEHYXnTjnZSloHIAQkUvkKyTrU2fx6vfvGFs0xxxGeloRnvrugjHH-sMrIalrk9VADTDF0nAnZXsQSW1XFKd5cVE1X3q_ehbtYFvfbJlt3vcP1L2-UjKW9a_kZQGO6Si35kYULE1JxlgonfXs8B6v5vqIE8u6R37GLLV8AXv8rbOVeLaUmk9AviVltHjRwh0DyGoggWuUittfXnxngEsnCRy_RjvPTnO722i90HUzjtMKzuzGTTqffA6ijiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100035" target="_blank">📅 12:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mssrCEQrmsle3mItVnvGiBPLbzP7ViqR0mqOcjkOveYNY1aYf9lWh78MiAB_mowa3RbofobH89KkKb7hxpW9pUoPlBBos_lz3_P0oC1mqRIzof1rCYOEqlAimEUC02i1l87xaheyMPH3VQCC1T5oEqocmK1nmlfI1_tH3PEQ9E3BRddru7XfGgv43nCHVJNxzjbQIKVi8QUUwCLJeSg2IUO-T7QelSo3FbpC6NztuzUVGBVXcb6Ip2ioOdvM5L2D6Y2wLo_V8trY0ugdpta5dTkQk9-p8BAzKVjbCRBp0X_QAgjlhHYmv7xMJXVbkB4WAtX4mU0iaxByVq-_vmrGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: باشگاه منچسترسیتی بدنبال عقد قرارداد با ایوب بوعدی ستاره جوان مراکش و باشگاه لیل هست. این بازیکن ۱۸ساله ترجیح میده یه فصل دیگه در لیل بمونه اما پیشنهاد ۱۰۰ میلیون یورویی سیتیزن‌ها ظاهرا لیل رو وسوسه کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100034" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
🏆
🇦🇷
ویدیو جالب و جذاب از نمره‌گرفتن لیونل‌ مسی در بازی اخیر مقابل تیم‌ملی سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100033" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیش و مات شدن استاد کسب‌و‌کار مقابل ابوطالب
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100032" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیزر جذاب از بازی فرداشب انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100031" target="_blank">📅 11:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🙂
تفاوت پنالتی زدن در زمان فعلی و گذشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100030" target="_blank">📅 10:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxuh9feT9LfTlleklj0wF6-pXVioA1G3UY_sOCcjF-xT1GH0vgsuMS4Kn8q6XoQ_QRiUAedNy7TCN9Ab8icKCb2A1oX1FsYRI_C_EPsH7_LE1tZLN2vv3CyB4llr1e0hAlFIaDJYs8kB7dGlm9jDA79BOb97Sef1omKNkheHOKHkKX67n65ahjSn1vA9y7IkLL37wEke8uBtotiSevB0rZ8ONR9BVv2urpE7oz3cdJkDe8vUW5IAIuECOqqy5iEUiKV7hFmqlevKnel4_3IhLrn55cKKBE7hxnY7pBhsqf5-Enws040xKIw5Untpr4xP5XUduLxRIf6cH_-OIgs0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسماعیل‌الفتح آمریکایی داور بازی آرژانتین و انگلیس در نیمه‌نهایی شد. ماریانی از شانس‌های اصلی فینال هم داور VAR این بازی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100029" target="_blank">📅 10:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=YEFvs7R_cZs8I17nKUsFihQqwWeMMA40RUF926bkNPnscDctRdxUBQcFBYEo1g2sD6Q8cllcO16BW8T-trBkiVjPh2UxKWq4QjgSE14oPLmnFFh_9D_43GoSfDlr_-UqkYvm7_ZEMtHi3p6j861pYw_xmHrrSjvtYNE_wOfPVH81yUJ1QLr7YefcssBymfVxfWnKY-NhOBnRCr8u4Nw8wOtsXZnzPuInVzUyI0P1Mt3j25aKTaoqaXeVg1Ysbe1XQHG2cRloWPd7P4FGwmeZcPjpT3FsoB7lvs2FYn72rweuIjrN3VNOPnm7qyBUQ2UDHM_p4EWchVMzi2IPPBmBsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=YEFvs7R_cZs8I17nKUsFihQqwWeMMA40RUF926bkNPnscDctRdxUBQcFBYEo1g2sD6Q8cllcO16BW8T-trBkiVjPh2UxKWq4QjgSE14oPLmnFFh_9D_43GoSfDlr_-UqkYvm7_ZEMtHi3p6j861pYw_xmHrrSjvtYNE_wOfPVH81yUJ1QLr7YefcssBymfVxfWnKY-NhOBnRCr8u4Nw8wOtsXZnzPuInVzUyI0P1Mt3j25aKTaoqaXeVg1Ysbe1XQHG2cRloWPd7P4FGwmeZcPjpT3FsoB7lvs2FYn72rweuIjrN3VNOPnm7qyBUQ2UDHM_p4EWchVMzi2IPPBmBsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
وقتی عمو رشید میخواد سرمربی باشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100028" target="_blank">📅 10:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5hEUCpyfsLGV70DL9ZCNHOmmF5SEHFk5vo9T44ve8CnJ6o2aJ_sYvF0jkZzI1Maa3eCAqguD1TX_4afoavPCikSF2PWSdMXRf_LOyNHMGB-4xttnvIRXuDh2Ehf1e4hG75Y-HKl7tzSOP_qv_KsuSdtGj2c-W3pIrHyMgfEV34G5FQW6KDxJGoB74T6rVf4oP4g6NcUOjc9dOnvoAfpstN_lQV4inMdA3okgyHjhFPDj5fTC9a6awaD33n4yelKpvQLHsReunJOq0GjqN_GFlrb8RncZmNzsE4OaZwvuXjcwIcxFzRluvDe8MqGj6YgI5X2TXVbADvWyR9wEA2pCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100027" target="_blank">📅 10:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=BeZ_WA23hYs38oZ32DXQvi0Lt0f_9QOh6gYuz1h8aJ12SBi0f5g_JYxKdycJz0HBgOnA9jj2h30uT-23iPvnwHxyqvflt_A612JU09bFwrPffHK2zFQE-2HWaG6yK7lhh8LtskpwisguErk79FqPJn2QFVvCm2iB3bUu_7JMsyZY5ofZdBvUY3we_34G5PBfwsXAD9D3W7pq4NPb_pPlH6sLJ0LwKcIUAmIulgaKUeS1PhqXHHACSgd8r8RHUKSeJMf3C2pr7PvLIcdrfkNV5AFFeEUnVYNn61j7QRnBXebwczNrNlKz-TFK4AFNJY8iAbdYb08tNgoGK203J4b2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=BeZ_WA23hYs38oZ32DXQvi0Lt0f_9QOh6gYuz1h8aJ12SBi0f5g_JYxKdycJz0HBgOnA9jj2h30uT-23iPvnwHxyqvflt_A612JU09bFwrPffHK2zFQE-2HWaG6yK7lhh8LtskpwisguErk79FqPJn2QFVvCm2iB3bUu_7JMsyZY5ofZdBvUY3we_34G5PBfwsXAD9D3W7pq4NPb_pPlH6sLJ0LwKcIUAmIulgaKUeS1PhqXHHACSgd8r8RHUKSeJMf3C2pr7PvLIcdrfkNV5AFFeEUnVYNn61j7QRnBXebwczNrNlKz-TFK4AFNJY8iAbdYb08tNgoGK203J4b2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که رسانه‌ها از داوری فیفا برای آرژانتین میگن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100026" target="_blank">📅 10:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk6UK4t4ZPIvOpQb8Y9Hqqo93kFzsfCKkjrbbB-X1_fBZV_9xeHXbiDNfAqXWs0vsaKNPbb1fdFxx89sDDuDeymr5cWa5ab9MKwPfSHqgh2tS5_OUM0vM8KDHdanE-VFufEQy8-n20XBZ2A4Ej4Xf7Vso41pFpYRKj9GpISlIg2rXOyKWrsSxWDczKB1m-Nba5Ep0mJDAy7ZYkz9thgeMI5l0DdPlmVTH6TkugtuyNpLT7VjUmAbe9IFMQXBbD0PD6f2ji-u6P8OLIN2baOREP0ZgwkLdAsuDGNTIUP6iJ7mQLMWLzfajOv0b2nz-JW55nALoUnD6FHe1WlITm3Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عزیزم ولی این نیمه نهایی جام جهانیه من که نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100025" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=Q4xPI7a0f_P0SZZOih_mKhb8qaWUiaywV7wGKpvT91hKhi5EFri8YsgjscCWPyz2S2L5-k3YzKPgcTmMcZLHTLHJgyQXc6VVgMtVW6z-xjYzPk8khjrLZe_Mqb5VRlkFoTZEhPuNdQQJEFsezJEjvknJFOy_5bbWVJm02N__n0zGBrWKje5walQoCZ287ChieEiVUdTVK4l8s3cpnqeWh2E-hTDpIH3XbrBDzeBYGMVd6pYolSXcJ5Qfm0xFKoBO12zlkfkWT_kNqQjDT5F5E2SgrllWO_jZFskfEnWFKErCRetf4b-aLmDQTMKHIaUDvMGC5YwlRn_tmbFZveYnq533W8UotLWFYFQCvmJCNQyuwWU0bJNlMoTbCgaLwvhoQnCDa00CYxhp7POBLB0VFhrkNkh3_h7CzvjJCS4D-SKHkrivJzar6TwU1etXi-rJ_kB-_oiPoIXXUtlTQisOV_olG4rOquKkMRdgTStgVBIkMw_e-Jq4wQ9MT_7In8LmnecR9hQ2dc3bxH0o-ydrEE3kj0jcdjH78Y4r9jW3mWlzKU3JSHGIUI1MM5lGiq9FHlYs-SNUFhkEyxba4sVOidhy8RE52oZgEssuetFLmdG-0sBTPDw4Eudd8vM4Wvq6Z_kRq0TsAXo6z-v6fJBtCOXJfDAs3WuJi3849R5cjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=Q4xPI7a0f_P0SZZOih_mKhb8qaWUiaywV7wGKpvT91hKhi5EFri8YsgjscCWPyz2S2L5-k3YzKPgcTmMcZLHTLHJgyQXc6VVgMtVW6z-xjYzPk8khjrLZe_Mqb5VRlkFoTZEhPuNdQQJEFsezJEjvknJFOy_5bbWVJm02N__n0zGBrWKje5walQoCZ287ChieEiVUdTVK4l8s3cpnqeWh2E-hTDpIH3XbrBDzeBYGMVd6pYolSXcJ5Qfm0xFKoBO12zlkfkWT_kNqQjDT5F5E2SgrllWO_jZFskfEnWFKErCRetf4b-aLmDQTMKHIaUDvMGC5YwlRn_tmbFZveYnq533W8UotLWFYFQCvmJCNQyuwWU0bJNlMoTbCgaLwvhoQnCDa00CYxhp7POBLB0VFhrkNkh3_h7CzvjJCS4D-SKHkrivJzar6TwU1etXi-rJ_kB-_oiPoIXXUtlTQisOV_olG4rOquKkMRdgTStgVBIkMw_e-Jq4wQ9MT_7In8LmnecR9hQ2dc3bxH0o-ydrEE3kj0jcdjH78Y4r9jW3mWlzKU3JSHGIUI1MM5lGiq9FHlYs-SNUFhkEyxba4sVOidhy8RE52oZgEssuetFLmdG-0sBTPDw4Eudd8vM4Wvq6Z_kRq0TsAXo6z-v6fJBtCOXJfDAs3WuJi3849R5cjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده نروژ دیروز در مراسم استقبال از هالند و رفقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100024" target="_blank">📅 09:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f18097782.mp4?token=k4RJ-pBsIdQ7Ay8Qm4o7HAHb3ycxL54VMEBhf55FssPFv2A_anCokHOBA8BT0R2AEm71iNWRMIzmQWFILeBX3rdACxdTMQffOm8rMYyAA1wTDiR9qahNuS83P2G7dzhnSLeCQH_14cXsY_IuYHFMe42NreHvyJa71vjTJCkXyoNjXZC90Y3HfUHZg3U3IsNu1eBQR_7nrPAZ-4vd9KNpHIZeirfSs0hhmcvqVrea4JGjvlQthvk-QtRBuwmv9l1KHyHoRITEPUafmC1tA94C4JzIuOC0TUirsc4r4hRViVTSRAIZV-L7FqPoWHQp22Foumsf-XogLkxeLy5qefvHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f18097782.mp4?token=k4RJ-pBsIdQ7Ay8Qm4o7HAHb3ycxL54VMEBhf55FssPFv2A_anCokHOBA8BT0R2AEm71iNWRMIzmQWFILeBX3rdACxdTMQffOm8rMYyAA1wTDiR9qahNuS83P2G7dzhnSLeCQH_14cXsY_IuYHFMe42NreHvyJa71vjTJCkXyoNjXZC90Y3HfUHZg3U3IsNu1eBQR_7nrPAZ-4vd9KNpHIZeirfSs0hhmcvqVrea4JGjvlQthvk-QtRBuwmv9l1KHyHoRITEPUafmC1tA94C4JzIuOC0TUirsc4r4hRViVTSRAIZV-L7FqPoWHQp22Foumsf-XogLkxeLy5qefvHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
عذرخواهی دختر علیرضا بیرانوند به زبان انگلیسی از رونالدو بابت پنالتی‌ای که پدرش مهار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100023" target="_blank">📅 09:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇫🇷
🏆
🇪🇸
تیزر فوق‌العاده از تقابل حساس و دیدنی امشب میان فرانسه
🆚
اسپانیا
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100022" target="_blank">📅 09:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRFI-Y5e1efwygxH_701XAOmkfYLD80itrS2UJEs9NpnBidloWwf2RBpct-KdZ-fnOqmUpW7A_J9en-7gY5Q-1eKpoperh4PhxMhku7kdUysanL7xMCw0YmK0ymbD_HL-25tJnQiM_iD-v85oTyi5FNogeN_ksnAq6hx9uOnUbvKChZdQo0c3Wb7r1EmVBIUKa6nYloYXy3--HnJ7PDsg_K2PRfwT4qK-JZa1N-ceiRcsHUdtb1krJ5NEgwCjeXQXzCk1g8Zd2bXlozYYwXVlHgug-SkZG65AxHEpcRTA632Fl-DVy250mBrbQ-JRorkouV4g-0jZ3kIFz39mbvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100021" target="_blank">📅 05:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141052eae9.mp4?token=lS7s43x2RTNQeXphXddV39GM9i3YOZNDl02QLnYyyJZ7N2zBntw5bVQGQqvJBtRqoyRKBii9fDzSu1xiE7weKaXwy8QhvRlWi3HHZfFXkyeAB20nBmtQJEoqD8Wmkmjj0RLAKQwgOYIuzggsqi5Pv51AY5OoDDOPwtw3JoymVm9RL5R1Ukgiyr77EBUFcFQoRzbFR75mSMBWkbPjDdsyIpGiKReWIk8fEDgIRK9OMvSi5ILl_Lr1Vi84_gA_aOO1q5mUzqZiCCrpUrbZS_jmLZBd0RKO4ZJciCv0UTZUml9klPnnbtguaO0OYTNY6j47oABYDSnCEdARHMKJ9OQPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141052eae9.mp4?token=lS7s43x2RTNQeXphXddV39GM9i3YOZNDl02QLnYyyJZ7N2zBntw5bVQGQqvJBtRqoyRKBii9fDzSu1xiE7weKaXwy8QhvRlWi3HHZfFXkyeAB20nBmtQJEoqD8Wmkmjj0RLAKQwgOYIuzggsqi5Pv51AY5OoDDOPwtw3JoymVm9RL5R1Ukgiyr77EBUFcFQoRzbFR75mSMBWkbPjDdsyIpGiKReWIk8fEDgIRK9OMvSi5ILl_Lr1Vi84_gA_aOO1q5mUzqZiCCrpUrbZS_jmLZBd0RKO4ZJciCv0UTZUml9klPnnbtguaO0OYTNY6j47oABYDSnCEdARHMKJ9OQPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال گرم‌مردم نروژ از بازیکنان کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100020" target="_blank">📅 04:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=RQo-UWDEI4WT5kjg9LmtyBsOYu2vA8BwFhVjm3a13vErgNQ0LvYMOWsMVd15MarH8i4DQymrtQmVuNciwY3S7wVrPNZVn1BF-GgcqGTyCOQpB99wrxzzipcg-NDpfVjfFEkmuIR_B8BxPGcEnLJR0kOvhgcyQGafiOGOV2sWJ1ZkBNASDJREoeL7g-h8IuFy32dS9H0U2hxBOx_CfPV6POYlK2V-IjCRbZe1nyQ2fDAgA6MmzYOA78H7NUox_61G4oCbGB6Mt46Rx9bepMu2B680RclGYLsfNFtIv-TbjvjLunpRfHW8MoLzCyYUXj3G7MbZ26FGZTSgiNE7A2HU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=RQo-UWDEI4WT5kjg9LmtyBsOYu2vA8BwFhVjm3a13vErgNQ0LvYMOWsMVd15MarH8i4DQymrtQmVuNciwY3S7wVrPNZVn1BF-GgcqGTyCOQpB99wrxzzipcg-NDpfVjfFEkmuIR_B8BxPGcEnLJR0kOvhgcyQGafiOGOV2sWJ1ZkBNASDJREoeL7g-h8IuFy32dS9H0U2hxBOx_CfPV6POYlK2V-IjCRbZe1nyQ2fDAgA6MmzYOA78H7NUox_61G4oCbGB6Mt46Rx9bepMu2B680RclGYLsfNFtIv-TbjvjLunpRfHW8MoLzCyYUXj3G7MbZ26FGZTSgiNE7A2HU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تولد لامین‌یامال در‌ اردوی تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100019" target="_blank">📅 03:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=Joxsp_OfFKPxugbaQToeFtQQHGWcUp23V_1nwob5fZ8Evzx5WG5axvib--FqeXKtQe_IOUolckNacFi7T6QMnHm4CCZ5np-7AOiXTBBIEalpS7s0NVcmhg4t6SQhAS39AFaKtBAnq7A0OJgJVJzg_rA2iON0om_RfCCU_3gg56aPkjXI5sZaON9tn9xJjFOI6NXInA7ZRi_ghsocx7brFgNLsDx61P3sbDB9A35mzJA_Da5yp26fuDGEaMby1G6Tq0JrEERsKJNW_gJhedqp2KoakAWe8RR94eovyvBfHINnU8KXtOTjLKqAfqIzvYSTmq-KayWf2pQ0Ccube5wPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=Joxsp_OfFKPxugbaQToeFtQQHGWcUp23V_1nwob5fZ8Evzx5WG5axvib--FqeXKtQe_IOUolckNacFi7T6QMnHm4CCZ5np-7AOiXTBBIEalpS7s0NVcmhg4t6SQhAS39AFaKtBAnq7A0OJgJVJzg_rA2iON0om_RfCCU_3gg56aPkjXI5sZaON9tn9xJjFOI6NXInA7ZRi_ghsocx7brFgNLsDx61P3sbDB9A35mzJA_Da5yp26fuDGEaMby1G6Tq0JrEERsKJNW_gJhedqp2KoakAWe8RR94eovyvBfHINnU8KXtOTjLKqAfqIzvYSTmq-KayWf2pQ0Ccube5wPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوب براش خوردی علیرضا جان
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100018" target="_blank">📅 03:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyBKrrTxR6JrxhOgZZv0yyny9zcak6caI3WDKX_YQB1GllksgTKI_qk5LgtQUD58W7eUdxYHpz2DgmNXac9fXm1SGxC_qeiW-e8zf3sYDZHoUFK-wi9c2RrYj02r2Bvb6JGP_S05X0xmGONvLIs3pelMAqqq8RJuKOD-ubnAvKX9O8KV8Hq3kptSHEZrvM7yYXPH5jNdQch2EBke13qw_W6sZBslM8V_7ZzDIIbG0RSfPw_pmonE3cLfRWRTeHsCn0fINfzESOWyUj7ysm-6vC7Mp8mfGcjIj3Y7yVHrJqQgHCf8tZQ6PhMYweqzvQLX1jWKHfXGSaJc43BOaRH6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
لامین‌یامال: ما قهرمان اروپا هستیم و طبیعتا تیمی که باید بترسد اسپانیا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100017" target="_blank">📅 02:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUHwIXZmh6pqJhDs4nozAPe4U3rKNGD5z8z_WcvW3mtdPOPVxVEJO9fYaYzeDNfuAYJiezE9SsqB8s0Wz1T7eXaojshkAAMnGP5or6NqduAAoy9PqwoATgW6sQoHHQf_QDC1IxNEgKKFdNZGv1MflHIUPYvXf8Lww9kvMi8aovs29jOtLsTyN6_JIc1xYH0QIYETHUUFOei0LHtFkcTpx-5XGAnvfI_d0k3Lyn2T6_tkdLK3ZCH8O0fU9r5gdiwc9TnzzPbsQaxOOfTXzh8rHOTdHMaoHVtI3bpOpaFQ7pUtP0d0_Teb9Sqt5qPeTgCGbRu5JlLGBvegqGK9HOK_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
دلافوئنته سرمربی اسپانیا: لامین‌ یامال ۱۹ سالشه و بهش اجازه بدید خودشو نشون بده. مطمئنم فردا روز شگفت‌انگیزی ازش خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100016" target="_blank">📅 02:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRfHSIUqGO9Rx55c1uBF2cFpez5Ys-MvejGNJXUMb80w_ezlMQpYlnFljoLuwnXeqQMaN_UKtWOvkXSVbpAL3FjJEvRi-p2opOHaU_WpvBGIqsH19qpImm4A7EF2f1Ax3zS6Fy85FbWb8DGT4LG6N_57QXTvGg9nXo4QuSpHwEcrODyoIlhNzUT48ZbBPUQ5SX2TMwvWL3yWSQbK3Z3numuzv7RCpY94WmNxCycnWLNg-reFkd34QRqMP0-D5mtUiqT5U3RtUAYdmDNb3gbRpgbmOyp77RhpVk-bxCSVqqmACJEwvYwYN6WwYq3VRx3mFdLhq8o3G2S56AIzi4oHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
داوران منتخب باقیمانده برای بازی فینال:
علیرضا فغانی، ایوان بارتون، اسماعیل الفتح، اسپن اسکاس، جلال جید، اَدهم مخادمه، سیمون مارسینیاک، مائوریتزیو ماریانی، گلن نایبرگ، ژائو پینهِیرو، ویلتون سامپایو، خسوس والنزوئلا، اسلاوکو وینچیچ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100015" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=r30rsl-gYZD6xn9itjSqIhq7bsWekkvo8rV9k8cQL2oaiJngfTZA94WyKnFPWrUe4BOSGtGU0mJ31LQ08yCXIIkeEXmJEO6Ql8a17tQbko00fXW9_QCPX8b97qUlaoLnCNhtYACna5hEXoEYlQJ2Pa9Mc-6JjQRHDRvopI0Uhb3JSyzdH9GLHNuU2VqscExpKRFAWEreZyN-vIgUpw7F8OcVQ6XyPUeWHfrbBFheQykiDFxhzUqTd0seWbUODXAPpegbCqSShek_bqYTD2Dt2ZW5_wwkOnEILVVWpncwS7IWt0R2X2-entfkNWqUQ_PqERD0HJIn9WiAaD9lR3xuhzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=r30rsl-gYZD6xn9itjSqIhq7bsWekkvo8rV9k8cQL2oaiJngfTZA94WyKnFPWrUe4BOSGtGU0mJ31LQ08yCXIIkeEXmJEO6Ql8a17tQbko00fXW9_QCPX8b97qUlaoLnCNhtYACna5hEXoEYlQJ2Pa9Mc-6JjQRHDRvopI0Uhb3JSyzdH9GLHNuU2VqscExpKRFAWEreZyN-vIgUpw7F8OcVQ6XyPUeWHfrbBFheQykiDFxhzUqTd0seWbUODXAPpegbCqSShek_bqYTD2Dt2ZW5_wwkOnEILVVWpncwS7IWt0R2X2-entfkNWqUQ_PqERD0HJIn9WiAaD9lR3xuhzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇳🇴
استقبال فوق‌العاده از وایکینگ‌ها شگفتی‌ساز جام‌جهانی در بدو ورود به نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100014" target="_blank">📅 01:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Fs0P1cow3fA2a0bFsZc3i9oo6x-DNbTpaSTzt0T6JCqAsFJNvE_Je84xaPxaQMHsZZ_aFp2S31C9muRUxsHs7TTdUvdVIoj350nrOO66s1K-WrYWv04TPAg_MidiaQYPpouBiHgcdw-OnHWCOkkzQRF9E7sB-Kf_hHDtJltFh7Wb2c0eNpc3PROwZ1g8wnwfy2OWKNIEcbceCelU3pIduiinJwwE-v-uDQhf90DHaqnBW3LI18g4Y2lPt-r2dxoHP86dGZU-XMTCTORKcqqN_J85W4999cCQyci7Vm0W9rW7DcZiaaesgxW2jl3KuyGU8rJi2GA63a29TAgmSeu7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100013" target="_blank">📅 01:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100012" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/100011" target="_blank">📅 01:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
دیدیه‌دشان: کیلیان امباپه صدردصد آماده هست و فرداشب بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/100010" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ_L7RPbQ4zGBUG5iKSWnEDezn54NWyrO3w_EkkyuUMWLBCpTrK1udhQ6jGOjAk6yLWclsme8qWq8nSXOR1TYU0UXMyTOOagcu2dS65WGGSNw1YoAs4kIatC0Gwej9AMAKQYlNPuEJz2UAgXv229IimKJiEYAAW9JsCEIpoJPFvfa9PPBpdSHMbbLbWsv92VjdZ3MsSuy0psNQQ7wr8ENIcZt3IA-9uSVz_APtLQVFJ20ZeU45LWJZMsqkLtxrcs0k7xG5YKdhwWmI99NbvWGhuz4aJWcd0OZ3XDoX_54LcZayiSHeeZVjc3c0TdiYA8jRrU_QDMA8H9llfyhb4hCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
‼️
گزارش جنجالی روزنامه نیویورک تایمز:
موساد در برنامه‌ای چندساله تلاش کرد تا احمدی‌نژاد را بعنوان عامل اطلاعاتی جذب کند. هدف این طرح، انتصاب او در رأس هرم سیاسی کشور پس از سرنگونی جمهوری اسلامی بود. مأموران موساد در سفرهای خارجی با احمدی‌نژاد دیدار کردند و هزینه‌های او را پوشش دادند. دیوید بارنیا رئیس وقت موساد شخصا برای ملاقات با او به بوداپست نیز سفر کرد! در پی حمله اسرائیل به محل اقامت احمدی‌نژاد در ۹ اسفند، یک مأمور موساد او را از صحنه نجات داد و به خانه امن در ایران منتقل کرد. با این حال، این همکاری در نهایت به دلیل نارضایتی احمدی‌نژاد و دلسردی او از برنامه‌های اسرائیل ناکام ماند. وی سرانجام خانه امن را ترک کرد و برای مدتی طولانی ناپدید شد. احمدی‌نژاد پس از غیبت طولانی، هفته گذشته تحت تدابیر شدید امنیتی در مراسم تشییع خامنه‌ای ظاهر شد. به گفته چهار مقام ارشد ایرانی، وی اکنون به دلیل کشف بخش عمده‌ای از ارتباطاتش با اسرائیل توسط نهادهای امنیتی ایران، در بازداشت به سر می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100009" target="_blank">📅 01:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100007">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100007" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100006">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100006" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp4gn3pVHwGbxHxc17RLuwVl-79YbDJL1ltD5SaVlky8hh-tvT3vM_SzEISPA0JMlm6vw8JKIsGKcFlEqvVHR_2FJF1SKP7Wzi28qYO04eR3hiMkDqQM2CmQ0igdzxBj4qIANzmNB7NmOLpRAbiNYCWdV4SB8vziQ8DV7bqeCJJZwrD4z4TW2t4hUa2CNbsIRsB9pI6TmXScCSkHKHHyoT65hnNfZKo30alLqpm02PmRJbZbweFNR3xhmDH-ZWlMFrSIIJvu4XTl1FiT_LsS53IWLauTEh74vfZ6xfk0KPvRnDp6wooaUBDeZ1JMfjdYrGlYhs-tG5jJb3ANDYAROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇫🇷
امری بازیکن فرانسه قبل از تقابل با اسپانیا: راجب صحبت‌های یامال حرفی نمی‌زنم. فوتبال با فضای مجازی فرق داره و فرداشب بهشون نشون میدیم که کت تن کیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100005" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fem0vz-sJ-0IaVxfn5czeQHQKf7DDLQwm3eIGYRU7d8cHMOpMvQOhBWGfONRa9steqsyGTEDrZLR5AP9qbVGPljYwnQl5ns1Fzyx5Au1io5cofVj4-e-hGrmJ1j4WkLltkZGKa3bEZONjuXfMS51bfSBQY9Z_iadWyq9HxDWh40EQms8Zs_xCmi3a2Hki0qIVeMY8j3tqUkBzYo9ycCqk3SaWvYkypWAlyGo5yEeAuBtq3NC1tolqDP2TTZ_ZQOfgKD157E09Zf9UrnrD9AGk1tYHn2TK_KP6JeyZR-ecGEeqGmte8Jq7UUieB7VJpGBhEJaprA-GgbtmhVLwUgWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100004" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100003">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100003" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100002">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
⭕️
شلیک‌موشک‌های سپاه و ارتش به سمت ناوهای آمریکایی در تنگه‌هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100002" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100001">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
⭕️
فارس: پرواز جنگنده‌ها بر فراز تهران برای تامین امنیت صورت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100001" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100000">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv7O3YE7vGOKkmLdhMSnCPf6Jkgk9XQEdHFVkOe-ltD_C-7IXJuNPgLMv4T2OZKO_9MizJh7w16xPt3jMiehV0dfvpcynX45Y7Fj984uy3fNskyCpxmzxfE0w5Bi9Sz0SOD98NBsoOnGxwDSZDQ7MkVpngeKofJzw5mwYUn07iW5vt8mnTSQDN3vmCsFVEjlhoGbY36GIaVEoQPuqTsl2vS-LovigMw6BVEhpm-81PTD1eLIV4cSxiMcYEJLC329bX6ipqNmYDlXNPbwZLxqeX-5l56Gjc0IEOWxUN1fmenZ9pC8WYg4uprA4RcMQnjhUrPNEmcVmK51EDpWRX2hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: مایکل‌اولیسه گزینه این فصل رئال‌مادرید نیست و اگه موفق به جذبش نشن، در فصول آینده برای جذبش اقدام میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100000" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1g782_c4kaPqKLyUAYfKP4zASHru0P8KLsO_nhN6TKhKhJ9qxjYu5xACpEQT4ziuXHdpNmi0yETizgY912Q804oepANlBtHrPuAcM8AYIiqqITTmNjpWuwMidLwynDOy62m_hMefsOxx3qn-e-UIidKrdeZ7_U4tWFmYgrlgBb7g_uBPd4izaYm9ZLzMqD4KTzFuBX7JGtcFY-tDvPddSN82HZaFy2n16hu-QOiyv_TZvpGR7fdkytasq7A41ngHKP_rR9RHCQoP9YZKpi_QKjV646JruQUZW1tPmAMnzed9xSwNjI3txbvYQE9BMHx3IV_Bb1vY4eSWrs1JQtCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌ماریزیو: باشگاه آاس‌رم با ارائه پیشنهادی بدنبال قرض‌گرفتن گارناچو از چلسی هست. چلسی البته خواهان فروش قطعی این بازیکن شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99999" target="_blank">📅 00:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=mmi1ApQG11ANUkDRxKGQAU5UUKU3JYdnnBulQSSnlKomAByNo2WBxwI1NUHFskC9G5svS33tqT79sBnFOD-Y30jRGvKHTd_-hNjiiVEDFZkVf6afBaY3h3YNgdanERbdBYOaZgac0rkUwBd11JHH49qZ_RUFZkLPRmICaobYM-g29VThzD0d9_OaOEEWluzfPtoWNPe-79eG-7NmHuQAiaapULR0avyPWMORFFQ6SgPFtglJXEqYNn8in5EGTbCBbtLlGvMCBWCPdWMW5wMDZspp1gcpsTw1x6dHP3wyiyuXjtzlR-kMOOLzSyvFOHikTROrPONu2GP5tMxzSfCwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=mmi1ApQG11ANUkDRxKGQAU5UUKU3JYdnnBulQSSnlKomAByNo2WBxwI1NUHFskC9G5svS33tqT79sBnFOD-Y30jRGvKHTd_-hNjiiVEDFZkVf6afBaY3h3YNgdanERbdBYOaZgac0rkUwBd11JHH49qZ_RUFZkLPRmICaobYM-g29VThzD0d9_OaOEEWluzfPtoWNPe-79eG-7NmHuQAiaapULR0avyPWMORFFQ6SgPFtglJXEqYNn8in5EGTbCBbtLlGvMCBWCPdWMW5wMDZspp1gcpsTw1x6dHP3wyiyuXjtzlR-kMOOLzSyvFOHikTROrPONu2GP5tMxzSfCwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو منتشر شده از حمله به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99998" target="_blank">📅 00:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
شنیده شدن صدای انفجارهای متعدد در کیش، بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99996" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgRY1J_vEaEaIRw7McDeeuVkCiMAXNbpKnIJzprDlBohyoXmHYpQ0J7UxmupUZBu1iRyOjMpQL2syAfkycIN-J_HYX8BJM2YIyd1Vxm8e7RjcY2PimTeGVLmK-KIasm4ZHkNv1-F9_aOAUOSFIT9fcbPV8XWbsouAr03ZwqwTa3vYpcpd2l0sfhfIBt3gVflC-JoS7AEo-skp0B5alO8fSWbSYvngpjt-i1fG5zxHllo1iuLfpx2QLRHnG1e0F92H2I-fL5Ne8gYHQN_wJ3d0amBhZLgOZ7R2wkQ4YpKGr1MUtppQuxpBNno3MnZgReDGz0YydhoauUScvcILVLN9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: میسون گرینوود ستاره مارسی به فنرباغچه ترکیه Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99995" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igq6chXytl7vQaH-Ck6bKgKcQHkkhgk6L5biOFQK-s45Qc7OVDHd0vQPu0i-9iTyRXCL548VD0PR6oAejVRTIWncujPkbsG0fSDlavGQqb3z5sd1CgoB9do4cOec49xxM8gUxpMDiP0uty-9pZ3bfeLhrYutHyk-_I49XTLvxnx6oxYXY8zdeZV81sNw7n4JLsL-LIzs1qjzkNe69v0MTWvK0tMWnYktQK2ZOB0B2_kEPgj1HhL4VRiHpNeNyUa7M7Ac8lWYRhAPK6hE819jo-1w_TTD6xGbHDhfugOxNr-T7JHFEajLzX1keTLQ7U9PXoiMUX8LpZ-eEBxD9roGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام مربیان فصل جدید پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99994" target="_blank">📅 00:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
ترامپ: ایران نباید به سلاح هسته‌ای دست پیدا کند. ایران می‌تواند تعدادی از موشک‌های خود را، مانند سایر کشورها، حفظ کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99993" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
ترامپ: عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99992" target="_blank">📅 23:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99991">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99991" target="_blank">📅 23:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99990">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/99990" target="_blank">📅 23:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99989">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSI-NBpMQxU86RDEPF0c3LxqOd-VmcMqTzr71fpChv8mALMutSsGhHjCUUHPLwpWWvpCMSDznWRmOiYV6uyvfKc7_3eTXW_7qZgCy9yM0fjCNcJTCEIi9CLayWILidqoJsJT9E2u6eyBFpUfQGQ9DV4OmfSM-xjY3AQUFP84u7mMIOCXr8prS47orTzJJguL-Xd3e6-p9B6_pJHk6V_QN33t3a7uJlPBrcz-EFqHhcxRLRj21u0RZey7-fqVW5c8VI8eUdutO6iPP2bIEs3OBm9q2_IYSNC9c4FAfFY8TWV99GjxW6S7NHZcUH4dHJNjbGuRvK8_V0b5KwvlPVv-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین روز کاری ایرائولا سرمربی جدید لیورپول.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99989" target="_blank">📅 23:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99988">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
#فوووووری
؛ فرناندو پولو: چندین باشگاه سعودی، از جمله الهلال، پیشنهادات رسمی به بارسلونا برای جذب کاسادو ارائه داده‌اند؛ لاپورتا قیمت را بین 30 تا 40 میلیون یورو تعیین کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99988" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99987">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWJ4wb9csRxRSp8Cw1da_Ce2-5vGKv7-JI7XN47IIVGQIdr46no0qh6_mjWplqHgSqj22LEhgR4vjgJbAvUJivwUkdYNbwkybnScJbKQb8_ultQ-DdWU8IqrOaJJ3XpyN_qlZ0a6xR4N9k3n7BkCHniUWTh_c6tsMbkBsNhZtpispW4qzdB3LYrx1Y44Ub3UeL_PvZHBW58RPCZ08f23T8aR6S6IqoIn8zPToF81dokmSt-ZjmhXl4ZWw_PPgpBM_Do8X8U-L3fgCP5hqmofISSccKKIWFQdmLe7XkpAuLPZghwlV1npmPd_f8uHV-UlMz1mKyqEevWWRPNVDqCTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومفریز تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99987" target="_blank">📅 23:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99986">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC31033MZMO8PPWVVRayGtJL1Q9tt7hG5efFI13HzXTPKqKc6rlKMMO9qzOY5dxxTZhVlilkWL-Lx5egGGc8G4Vok87YffO-419T3K3JTIxueyLqwbVoNIA-BuZvbelMkqVaQOjtzeDP_F3Qj1U791gj7nIjzSEFAR7rMEqr-uQuOmoNaWu9eHpsOBYScBEl6MDPYxAZmCFnZ52k4R7G0XY1qpqluQZgZpgn1aYw9h54ZCLfFXp834KZjYtka0c6iKxxPiIU80XVO4A5V9NlclIAjV2Rgxz6El2dCxV8Sghhh_fSUXGpRUbvLEcjiYh5EYy6mNWAf0vrHve29SaSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بین دو نیمه فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99986" target="_blank">📅 22:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99985">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAY_WYWnEXqRf3eWwePeTZx3TlAao55LgdKfEEmubnjsDSjx07pvI1MRYW0xIeY9yw3zJB5YuoOgnBOT2UXMGfu5IDght41ti-ss2CtKnxT2ELD8k6CKNMEtiHf7ufULeOC0VERj-qbkboj9BaJIYAYVmsMqslr7WSgSholbJZynkLyS04qDAmuyuInBuFSx168_d1-oGPLxCQtFV1CJr7URoZoPe1coIeW55hEj38M_HwfmkrOUWsborqRll9OdvPUN0D2tjFEaJ0KAhkutt7Kq2Aap2FJmdFN0PHBVvSxxmZ3hi_B2mXVqv2T4YCWfGTVoklRldh2xaGf_EoQV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز و اصفهان هم خبرش اومد
اونجا هم دارن اعلامیه پخش می‌کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99985" target="_blank">📅 22:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99984">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9I7IBMKHh2LO0W6UuCf1ZDyQ6SjPZKDarRH_r0T9PMUDaZ2kxPnZ5LG_sn1d1h7nP43jQW9Uae87yrN1E9N0MzrHhKRuJkHPjCmOaVPZjRR3WbOlJLt3B6tIHRp0HhEucBjFcL_9itJIJT-RNqsN-eAJWqzlCATIeZp3aiL5abJwFllIqlNUA27-Mo6bFwSzNBhoD3_w_No3b6GqvVxyWsdZcuJNxfnaZhwiMUBs8hsj6KZu4x_4E2ILGEP9DVy05o0W5p-gF4IrqHUDyvywWprIGpELEdmWjeY9Sq_7jDqVinXNibqvTkb-QsZdJexuPszgTbEW7h464vwHqGzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمه نهایی جام جهانی
❌
الکلاسیکوی بارسلونا - رئال مادرید
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99984" target="_blank">📅 22:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99983">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6407669b7.mp4?token=KUriJkIdM90bo8_40JRidvWk-lJikHf4H3ysCdbe43PTJdVyJCX5UtTTmjNVut0Z44QIuC7PWRvrVUv8J8Mue_qcGyJJfiN9NotIPJj-vzPmuaPFhqfobZEvKh3S0lyrQ7uhd4GMqR9Pdd0MuTZPae4HHxPZbVvgZaogLEYp6wPbt_Hb38Zag5xKRDsbfpNMKjg-k6oxrGT9ALWKRguL9Tcsg8cNC4Q-BjRYb35fF_X6KX56yGH1L9rxgN1069lQSyAZ9w0NkNlZa6Wa3aKztnctHjs66vkuduWCM9y_jMfG9AsD9zxa6veYw_CIDH-n470m2ua-MBk0B6umACoRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6407669b7.mp4?token=KUriJkIdM90bo8_40JRidvWk-lJikHf4H3ysCdbe43PTJdVyJCX5UtTTmjNVut0Z44QIuC7PWRvrVUv8J8Mue_qcGyJJfiN9NotIPJj-vzPmuaPFhqfobZEvKh3S0lyrQ7uhd4GMqR9Pdd0MuTZPae4HHxPZbVvgZaogLEYp6wPbt_Hb38Zag5xKRDsbfpNMKjg-k6oxrGT9ALWKRguL9Tcsg8cNC4Q-BjRYb35fF_X6KX56yGH1L9rxgN1069lQSyAZ9w0NkNlZa6Wa3aKztnctHjs66vkuduWCM9y_jMfG9AsD9zxa6veYw_CIDH-n470m2ua-MBk0B6umACoRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
بازیکنای فرانسه اگه تو تیم‌ملی اجدادیشون بازی میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99983" target="_blank">📅 22:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99982">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOKl5BdyeiBMU8e4_DAlwaztt1W0v0TQCWfbgdQLdLcLFEHPWIlBP6lD85phn7ORaciAPgxboFQ8Qe_SGAI-I_vbQGiRk5F9LMNWnZyxxY-kTzbZmnMF8oV03tXAXeTJMklsZ4dVf3cnrYUqRd9wjKEbcRtcmjFgA50vjpi-Xs4NCWh2JVe2JjZQjnMZgEVV_vYQrlArNoY3ufdu03FdwpOqikC2KBcUhwF2KdB4nC7U50pS4kmyD29smG9oCfrwXQ6ZyRrRAzT0g08wnO_IN8_O8AY0LGohb0-ojNkx7OisdCJOV8BCRuor-74JM-ffuovRQd7cRc-5KlXSwARB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
کیم‌مین‌جائه مدافع کره‌ای بایرن‌مونیخ فصل‌آینده نیز در جمع باواریایی‌ها خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99982" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99981">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=uKIeZc__pVso-VyFh-7DVE12p93bos0uMdWHSFmxDEHALXCVAQZx-_4iHJGUqdtAMKwq7M84zrtZ9Ndwj6C91Jfnex9jCttHbrXZY7LKsae3urXdDmCeiCPHOerspMZUeHAJRevIKKmoCsPd1lfM9P9NEupLV34fnzaRSQM5_AN5J0FguCVx598uVdL-6MvcRWzfTy9DHeD9Q0ogf4mrh9WpA0PFrAy1Toh3AXn-FGGulnSDNmMAPlLdTrg03SOqgb7Rr5LmpJDTdXS9cuVYZt4Qz5uZSjUbaPdyMt8EqVU9F_5MwGM3J5FIWUntnnWe-kUOXQyHVoXfQ3kdGYB3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=uKIeZc__pVso-VyFh-7DVE12p93bos0uMdWHSFmxDEHALXCVAQZx-_4iHJGUqdtAMKwq7M84zrtZ9Ndwj6C91Jfnex9jCttHbrXZY7LKsae3urXdDmCeiCPHOerspMZUeHAJRevIKKmoCsPd1lfM9P9NEupLV34fnzaRSQM5_AN5J0FguCVx598uVdL-6MvcRWzfTy9DHeD9Q0ogf4mrh9WpA0PFrAy1Toh3AXn-FGGulnSDNmMAPlLdTrg03SOqgb7Rr5LmpJDTdXS9cuVYZt4Qz5uZSjUbaPdyMt8EqVU9F_5MwGM3J5FIWUntnnWe-kUOXQyHVoXfQ3kdGYB3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
مقایسه آرژانتین با دوره قبلی از نگاه گابریل کالدرون سرمربی سابق پرسپولیس که اعتقاد دارد در مرحله حذفی، هیچ حریفی آسان نیست
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99981" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99980">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEc07yrK7C3gsPSBGE6WlitOYgPlbypbMYm5x7tlRhA5XQABcDoQb764sCTota3RcVl7iH0LPwOSpnF9hFhiRnnKlYWdN0ZQ4Yis-Ygf8nNVXaPevIvksndeUJ1IOfxM9ez-A5vYitcixTlgpZ-OTjnjk2fz5XWUEHlWuvig3oHeBTAGgZCQQJvJeFR2I3VVHF5llQgxcdtPJVcYsYarTHgd3df0DqQJjxk7n10RNuae6x7kWv6r-UCjzsA8qLecHsVS-c55CJb04pqbfbeJA0vVRyJ1Hos27QpjiPxfO2qx-LRaa94ylf9vPLuIRedcaR_zOjFRy2RvAPhqlGuryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تب پیش‌بینی جام جهانی بالا گرفت
مشارکت ۵.۵ میلیون کاربر در جام «همراه من»
🔹
تب جام جهانی بالا گرفته و لیگ پیش‌بینی جام جهانی «همراه من» به میدان اصلی رقابت‌ها تبدیل شده است. تا پایان مرحله یک‌چهارم نهایی، بیش از ۵.۵ میلیون کاربر وارد این لیگ شدند تا شانس خود را برای حدس زدن نتایج امتحان کنند.
🔹
اعداد مشارکت خیره‌کننده است؛ کاربران تا اینجا نتایج ۹۸ مسابقه را پیش‌بینی کرده‌اند. فقط در ۳۰ روز نخست کمپین، بیش از ۹۰ میلیون پیش‌بینی ثبت شده که نشان‌دهنده فعالیت بی‌وقفه شرکت کننده‌هاست.
🔹
حالا با رسیدن به مراحل نیمه‌نهایی و فینال، این آمار باز هم قرار هست جابه‌جا شود.
پویش «همراه من
» دیگر فقط یک بخش جانبی نیست؛ کانون اصلی هیجان برای هواداران است که پا‌به‌پای بازی‌ها، در فضای دیجیتال به رقابت با یکدیگر می‌پردازند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99980" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
