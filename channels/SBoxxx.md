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
<img src="https://cdn4.telesco.pe/file/gIvpIJSgRxlr4ykGs00TtXAsW1GhjgP6xMHa4fJtbnqSsp56i5Et-UUtdU_d_3qSvRNazznWT58l2E1ruXm39NuqbJH0nGB6iMsS8gDnABBsYi8JyabwAfYvL4sDAU-_QuHYo8Yzu3w0MZcAAqK8QYq7qRGwJqU1N8W9B4PZUnzor99k25OBzNtLVxFNdNm54esQmFgNNy3Cm6vHBO18V1c8UINDmgOzKI1IuJ4qBWX4IE9rRSmCtO1RNYqC8QbcVf4CTMGtM2tlg1EZeyg5IEdDu-Kcih6svojlkpoE_SEuTzLuZ1IXCEn_WepAB7gf1Qh9JTQrAtEe3bukyMC_hQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBXP14-j5tGD5fJcWP_syTAeI1Hb1VqN7YcQRKl4cQlWzTwaCHIMBYa-CYewgVKb_CKlKF78sq_FuBkG2UWjXmmYak23jADZWbX6l6MOHhbNszYw_GkCG76s2RQKFVfWjJu-JzjmhJy9-Io8INtYeGpKzcbDo3RwmZm_VNWj00tKCL-fejbbqhqxWLdmd4ohJcYpQuVYBS0U3fp8VEcmKjnX0LmTvizRdoP3RANgClj35fmah2P23KaScRU6UuVRNF83wnBofnrOBJvo2JGN8gAIsVT3y6V87G9xG_4PtsC1PYARpuZP_0uWXtvbnKFmbW__JBRPD4FBV-JcvyE_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYjntyEq0Snag305RZOi4bDcrkru_InEMHXnjhLU9VtneuB8epQtYYQh3WDFjDTgxG2FxxeTNOWEk0BzwhYpzKGq_rp3gI1hKohRofG3R443p3WWAR_E6AyOeaPrxEkFJMhFiDk6XOGYe-sa0MZ2UFLfpyFoydivjnBe496tscBO4UpLXytEcVKJ66mFxPmz6vitfTrDecFfMokU6Qf-xuAmSwGAFeoL2zXWylUUMmcmcZ5oEX0HUiz4s7p-GPK0O4ckKpAUSaVGk31LNWqLSWLlXfAMYiLNyORDXnPsLJO4oclcQpfCYcFGkb58EYnIJArMnj9aB0WdTVrYWj7ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOEQz3_ZSjKz__23xHVUL_w_nE6Aa61eLU887sUBX6fY4VdhO0DTpnJInanY_pHRdpNZWt7h2UDEJk368sfoLskjsPkv5LMsir6WfHuE3mntlL2dfR9a5mkKaMkGB5uWDlYQKOsiqOZi4Lu6ReYrQirv1aIJzcZWy5TKgUm2BrpvirQd4WR5SEhnt5rocBFNKFxLFOzEOrSie1ubIv63vbPg7jvLgEg_3LnrE7qn20SGk8-HPjacVOcTKOrkgn7JGAdqz3v5PjkVxsJRiz-A6KbipJU2mARiATrruWpSgvyPINVWtrOsfySDdo1Dw4OLeHbw8J2Mn5hJebnCfxHlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5yo6Gbyf8-MReQhfOqf1SqxZooGBnKsHcWBCcPTjMZCm3PzscBwT4TMEOc1xa6RsJg6hrDGLOYIDyvyY0SpOXzP__kxnBlthWiCOV3weMPlUGEEaYc97AVWUkFB8cMPGsHRp8CU7VaQtoLphVxRVZPY4KHZZeQ5HMy3DgpNp3uR8F9DH0Xdf7aPVtlHVDUAOO6LREF7OO-Ti7Bze36Pz6qK8Y6z7l8odCIiGsswBwRSoB_bwThhJ5rPfIkGhO__lwBaSH08umQz-r8tCK1meNoafxdsGE3YgKuZ7SZ-qXy9_UomnmrH4-1orcC2B_1sXK82kE7JDj94xT0EA-EGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=PslfkAlgsaU1yylZbgrUef1sDNQo1yT1artlZkBE6vh24mVKYvHhkM516U_QWiY36kVwJ0aD3Nedt7hoGF-H91kuu7ZKRqVMS8K5WMLvN89Bxlk77viHNb-ph38p07JqEtAGCzfJJVABuMq2wecvCTZA3d0vm2bi1Hmxm3afNXSBsynFjfL8vgrYmjMfFJDoNhMOILzZOcA8oiJS1KV01Ujhynn-RF5Cm80rqHXCTfcPjCx2QzckzLOSEeETnxw4zDdxOb7pNLWV_uy3bpZmBHcr90I1awa5ms8BEG3Tv2Rj6DX40kpEPQHN9QbFO6onWmpTZiJoBMeUHF1ftgdHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=PslfkAlgsaU1yylZbgrUef1sDNQo1yT1artlZkBE6vh24mVKYvHhkM516U_QWiY36kVwJ0aD3Nedt7hoGF-H91kuu7ZKRqVMS8K5WMLvN89Bxlk77viHNb-ph38p07JqEtAGCzfJJVABuMq2wecvCTZA3d0vm2bi1Hmxm3afNXSBsynFjfL8vgrYmjMfFJDoNhMOILzZOcA8oiJS1KV01Ujhynn-RF5Cm80rqHXCTfcPjCx2QzckzLOSEeETnxw4zDdxOb7pNLWV_uy3bpZmBHcr90I1awa5ms8BEG3Tv2Rj6DX40kpEPQHN9QbFO6onWmpTZiJoBMeUHF1ftgdHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9Vv1KrzWCOkI35rpBPhZzXnASzNOVVPOim4cryMnh0x5wSwDOaHxxHteyE2x-F0If1Ifxx9Y0fbW6-qGSHtUQ_RwLiz-aXxpADXvRc56Lytty-_YwDQ53I6OhmtQd4gDgSCS53MbRAqJtgQASPv09F8cKG6PetYn4jREUHCpHFtPqub8IMhrTUGU4uYfgq5mCofmOtyui-w5s1SD8iDVxFOHNbESWASq5PtYvhT1aPv1JFZOpUG2dJ4MwgEVu2pzt90iL624G833_PVel8Mh0CEXxOrPd5hyTIg31UomRPuR_nsBhm5YfY9GseZ0E6YXdapRNu1QfikFjjmNSRp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
مواضع هاوکیش کوین وارش در نشست جکسون هول
مواضع هاوکیش کوین وارش در جکسون هول نشان داد اگر تورم با سرعت کافی به هدف ۲٪ نرسد، افزایش نرخ بهره همچنان روی میز است و فدرال رزرو لزوماً مسیر کاهش نرخ را ادامه نمی‌دهد.
بازار نیز این پیام را جدی گرفت؛ احتمال افزایش نرخ در سپتامبر از ۳۵٪ به ۵۶٪ رسید که می‌تواند به رشد بازده اوراق و دلار و افزایش فشار بر طلا و دارایی‌های پرریسک منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpytBOGdSrNVW8kZ1WRo1KivSekL1ztsuhJkHC25i1y1qC8a5g6UY06gWdr319E5uik2bst3zRtPmXDWY2ntnndbS7Z9Dtj4w7A9T7VYRQm7_-gqJ85ASOihO_RKLyZMZNOEJVjqXlYXiVXMLz306p7_g2Cp8u_ZOT2aAgs8BPwnDbPpEpyEcQ1ZXZW-wYnt-bo_cQtLU1S5jrG0dIVcr4AISI6oD2cjJ7wnr7S5eNpufV0O6PGX-M7w5lNAAvRuarrQEcCAD0oNsur6SWBV5mOcyp1_3051W_PbyMCYhoJraQYYCPggGkWuTNFdH_Afg9Qa0cbafg8lf0vHgzmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1DsLoUhWXuALBRXOEqDOPiELzXtmCuNkOAyo0QaGZabOTH-uxp2VEhATQC41L7V19roi2tGMGk5vQ2HnQdnYseJ9ymGarpwYRZiQi7WE3jFXc-3AsHm9MBWwlqbCOqCc1gOuOgNkXsjFaiONUwQUv52faLDUQh7HPAXPQFWoRzidaeKRkrqQc-8IYFBpfDDrcDciwxqszsaNUR8_OIJk6E7tAbZTXZGaQ7LuThl_vgIKx8s6uBXFW5sWak-AQpjQTiUFr8SHTVFlAu8YY9ud9aXMmCaLyi69tblGs5VW_9Agyo5_EK6flqOt1Kdbx7XeA1itniXTWKF7qe6MCWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GByalCC2I6qan7hymYebTxJJ8UtH7gdwLTjzdGyNGKkTW3r7bFE1PsBrcMOGUkApC4hIXvvXnt6h7vKT678FpeJcigwR1tIDNq89OPYtaRF98BdULN2Ukdp2gdR-oLpeMDFhpA3Nir3l-1QJO86sHl2lfJEB7mwwBoN8cvVXQIy3cPyjUd5v251mHA6r31-LdGrI6cyLLvUuLvlHf7qn4hl_9nb4Bg07_2GJBDhDzaX6LPBE_ppOn5d1KfLE1IQfm2kCAfWE3bQZC_pP0qJ7SB6yMOFgs6fd3xxO-47mB6EAKKcZasZ9odSyQKNSbJCnHtG-VcfKdIHWXvVdPcDkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az_OeWrNOdKo852y4dOjiMApgd3SHbplc1gbIjVxP4AaRRBI58j47WKZ7idKXiE_EneC95SQA0H_osdZyE48WZExr0PHr3O8flvDz-iVoC6HnTfIEzrfl4XpTAJjwdyXGo5gC4T32mEkM5NzLfUpm1Ngs5sFWFdnZZWUJithkgtLf-yZKUbt01MoTua5rciOxyb01S75KTGrAjgiksDQHQ3oj68fy_pXPyU3uEyvE9VIeRrN92mAGhAuAFWXbpwAMtOWwCEyAWXjk40YmmiMM0odGnnzhZGMfbwm7d8GUFc-xPJ3PK6-1YRNswiqyxF-R56W5-dXcr2LcnsrAZ6aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3IQLYddEj3TiPEXZuQrcLc7MwPpTqhfw_RN46ywDrq43nUj-8ZyrAlAOFdCFytBHU6w3pMH0PFjmsku1irxaCvJ7woPTVb755fmMQxykgfDpf7GkJ1y0U898guCvPOgTixs5iVhaOxjzRs7CtKMAQ0ZU9lTfiFGpmT1TjGp7aIv8Ch_xet9iR-khLPOUsy5-CqJTDFzuIM4fn_M6HI3UEVALrm41rs3rB9hK75jNUpXekFEtqCzv5jTV3XNlxFy0Dhz1vvSBay2mkxeeobzyaShdwMPinUKc6EODF7z4Liht_CF0-sk7VgnVtcC9X7a-eHjVFcG9WvlQ1SsYGpRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNZq8gS4WFa6bwww7XpEqlSS8wvO_0i5SgjFDDjUYtQH43zuhkvUDxpvLN0S2zaHqILFWg91606tEAkHUSxdKerciFB-Iielqp3t30R7G8-udE8k4p6rG-Cjy_YyltM2aT9PqftVICJdxQEHCEP8-dEhmvduvAu9jTRNpLlKFNR2GaNR1k_l6LeKqvH9jlfJcM2YacPnxfgi2plNvQHWsbfEn-rG83aINmKFHvrtOpW49-EplurFVJx9FCkMk7vZqmfX_5qumR-ov6ooWUUyS2XTEU1RKHupgL1PXhkmR_UxQISZvB5YXnJPCLA1gyvPS_pmug6CNq0boiNR-GUMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM6kBoJIxQjaYDqF-ewMGcXY2i9Lw5MYH-0qefu0esXK1cqy0W0HnJU0ZN22WM92v79honeCAH-2Hhqcvr0xu3UW72WfNT6LGZCxXvLfbXVOdm8mCeTrKYo-9vKlOSrU0SiqR2zjwuxyou8Y2OFQRmZKMQSqR3UVI_Sg0Os-BGYmds2OlW3G0XVg_KRi8S-D7zHywMidVQAb4yO7t3gdYReqlXNgWwl9WJeta2yEjWPCmy-9XE6-aHPVmB-IyCpsXdtfLczaayJ6J-SMgOQF5Q97gUlYk8KCxrtxJhnxNY6zJilg_jQYzXJtr1oPXCWHPSa_b96x1C69QAfKf9CLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWr0SDFGiVYuDW3ub0_5k_M8hPrrTbIvzik8DufqDWpfPRgzJvJUgYSdaCKuyYdmGAtypRiQXv4Mubxd6ufqDVmiQuW1PT7edkZParylQsCqub9OU7byW6RhPP4qSh_07vOp2F1taIpP3-cSYiLEy20txvIGCwAxFkyOT8TxWuNRtW-LUnaxQZOApcKa4zZHFoj9rzSNHTka5cYD4ExLVG-gWgq4hwW5XHIcvZJh3Y7TgL-apB3_GNHpP6egd-kiPUTrGNX91PwYtPL3t4_6BXfu4-CWX288hyVr1KRIZFtVjdABjPA02CjRaq0bm5DrArPbuspffXQDG2JdKdf_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7OIlozkM7kFUzZ4A_rXhBa1e4tmEpMfSTAjOQUgBifgNSIjqQdGqDHwKqrYUleUUvqIycNTg8dY8GIUkrWEKS2bcvipANTRY-bT3U31kYbZe5mUqB-7082cvXCYCQbslqKF_4UB9tPYFsK-VqG5a-69KOJGldAXKRjOGnCh-MuNclMXcm4J5dv7nVLrjZihAr40tz2c-DnXEZvYZAmKoKocoRgjBmanVHgA6UJDtqkvTng2zpExzGtkLC_l-i_btfBVOApVYhHslOn0wtYwRL-p3AFN6kxnQP7A6s57oeYdrsNdX08wVY-UwgHqZq7DuCsYI1OlaLt5lIwKaup0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSpTls0qCSpw-tuQlkfBAoBWQhOqiEYV-6_5kxfYLrOKpsPUKu_DkFU-SCbPQeXYiQdtp5V9mZJ3XqQ0FETjco30aBcSshNwpXZ31QA56Ok5SMcHIgQyXlQynEjNQpg2fW9AhouRWWAMM9h-xmIp72ns8BNNW52PSIAqUAIWQoSU5k5KP2KzpSNA4RrmDwOVkam0oAS1ViB_5BMlebhwGanljA7Rn9FiSdDeXuFB6eGTwcJaka71xOZyD3OkFl6qjQ1lTRmrzvt7Xjblj1R5qJsAbsWMenReROuOY5o1kz05iEyaJ4loT6kcVNKYjHLhqnoPLbMYwEMLOax3HUa9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDNrP2EedbtWk3akqFt_plapLq0J59xk7cLyMMXVxP2b66Dpz2iVW_RfkbZ0_SIpcmO2DTVaLRzllGl-YYk6BCnEHOETm3Xs272Ghqu0MQuUN10seyEYDG38goHQ9UJECz68VtEWKC-uctRiwnnm6BSHzgEALnPuwCuKIO6xBlkGSiiXlR4XfzMQdp0zU3DTYh6zlWyZfrrYJdyVQKAF_LW5mkNGVCmbOdvEyucec8rhFuOV5GzFQiFHeFVNLcFsrjXgLlZ2Sn7AJT4YuMPASFTEakbkVNpo-PMkvSLhUwJIGSCzP3WYe1D3VglrO6X-qaBK2ha5lr1zrPmKs74u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cikO2SuPtlvwxdlsBXAQBkAfmpO8_p3vLuK2nXtxfovEXtMx3_1n-9y-mREZTdfTmNbLzarbjk5CKr5oRGLdqf5E3yvGv1pXVyozrbR98ZpxZj7zvWiHJ6bhZ3puLFt8hzJCfah2Cs6j89xgBynkrz7jX08vxaKhsVLhrvyPd3Vtkmw61XQ3-JPy9Rgtguo0HNZAIqt-RoVHvM4c1RCEsDSwdfFsxYsNGZZ9eB-9aqNq8E9gt2Yxy8B3Y_vDq8XjuU8U7CwaRHmSJ35uTlQJzE1-dUsNGrmf1RATiQQ6PDg5ze2_kCJ4kkAGhZuhcMU_5HYsdb0764C02gjX6nek7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXvcR18B1EemtKiRu8t1cYuXE956MBJJrtlJIAw1BjzZw3DQcXZbnKhZnlzzM5JTPyycDWAoZp3SBV5-0gTPi3jZ5od81ch3WiPylOGsmx1-pD0a_t1vA4olAR438JXta0PIsxolJekMkvlnswekdaOGDkFEgGCN4UQUBQ6sYf4gx8rb8fz_d9Ev2hz-h7HRfAMCY4NyLl7bZyw7P_kXHOujrE59-XUe_rEAR86hqt4pjP-8Q_--knSemkeUnFpmvySyiFxip1kyJ4KwtyfUn7B-3exiOeLwUbj-ILgpuYb0_WdhVfWJ0pwl6D05wgCG2WtFQowSe2x6rz-ssiH3Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q36kHVzpHEOyPPzMgjo5Krsj0wBM3dR0Zrksyw8ccfMaZuvTosoaSQ2TMRMy0YwES_5BACxgWR2cv1YJedy5AQAfwamE0IQcd1Jan6wsR8P4FuTJtiaFw5ybDgL0w8ZqdnXdq4xdy_HcdiUZ1HDDE2taHMiVioQJar59yh1Sz42GQdGiAOsO-MZvFBlT0B0wbIfGC90eWAS1hza9yNNpdwRhJsYJVzzh0lJH55j7xVjK3lQVC4jW6ZCop5F2nB-_YyYuLGxqCsjzNzEIT5WUmJNptJZ3q6hzo3WHmBcykZeOvKymtaKKeZl318dh0ZWAfRySM9XyeOvzgyhMJOSUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUszyFHnTv_t3sSYEmKLb2PloqRu5afqqQ1thLBRJmu0wV9FawXIR0xgrGjUCW2dyQtWC-R4Ai0yHPZhHw-IBYkSoLnVZ3_L0i6ZY5g-8LkcVgQwqh9XRXi0AsdBdXcTzvnEs85D5hyf01QTK2UYq9Z-o69WDHmYWEWLzNnfhWeO_htN4tvulOSiP3kdzeDUWUE7s1NuM3WexabSn8wNM8SjxAGTRcr8XrX390BOq45y0nENsvvWE_EPCis-MmPxfSlZFKg3dMOhnCgcXPMZze35IdZtdmtrHIs-2-OAAYuiHvYuGs7GNBjCQj-gDrGeS92pHt7dySVRKW4jSx_vAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCezrKs0BQv_c7EQwUQOOS1t-TvNp1UdWLnYVOq-FLuVobUx-7u-nL77Rq5hVIYmUkl87qMANAbiLctGEBOEu_WNxaxbXQJ0ywcNmr5zYG7_o66LFtgQf1AO3nIjcKRa1gllL2gkxWpW_ZKWJOWJkBi_Yaku5XEvJRmwWFEFWaaj3vShCaQ2J3OvRU4mmwUd0HKx5PItc0Hf4bhHd-oshxq2GqpiE7fsKZN2CD91CuRjoVUXrspX_btvBBnF68pqmEwgBlnPiDKZuVDoc8DQed4hVQ57NS0LbOnpzqU2a8NhMnLiMYaCCkH-EQOeWUBo5UuZyF_m9Tgwt5aw26yg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=WB1FvtqzqWItnW12Q4J7IKbPBhGYENYwGguIxd1O-mMH_clcb7MQTLx0sXJbVRFtYPaW2K-cYDCKNiawLm88xGKHx-c7zn7l9gmR5chEdZwiMJ-hnWRQFCpHNKioE4SpUmGoUMkEBA5AnEzRx8eRZ-TctGnN8I4uM3RCvH4X5WWsjBAs-i00ZxhUxZ0huBF9xlJmGjbuqes82EvtPexNN0xhjtFuh-ZHj0Y4ja0MlnZQYzW4-Ih3eKKF-8oHZd57KwS7tDZ65Esmu8lO8JFvPmOnhRoW9O9JKfO9Axohb0oXkDNCfvSpbrB7F-iIe0Fe9vNF9oPtLSGdANh3efNoog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=WB1FvtqzqWItnW12Q4J7IKbPBhGYENYwGguIxd1O-mMH_clcb7MQTLx0sXJbVRFtYPaW2K-cYDCKNiawLm88xGKHx-c7zn7l9gmR5chEdZwiMJ-hnWRQFCpHNKioE4SpUmGoUMkEBA5AnEzRx8eRZ-TctGnN8I4uM3RCvH4X5WWsjBAs-i00ZxhUxZ0huBF9xlJmGjbuqes82EvtPexNN0xhjtFuh-ZHj0Y4ja0MlnZQYzW4-Ih3eKKF-8oHZd57KwS7tDZ65Esmu8lO8JFvPmOnhRoW9O9JKfO9Axohb0oXkDNCfvSpbrB7F-iIe0Fe9vNF9oPtLSGdANh3efNoog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX9lIKQv2lUtrOg3oKIRurgjKyp1IhEBJLLnOE9lqbDtTXZUsapQwSZs-49xw--yV6XJjOcb-8tVGisplu1cBrnnwKde4RFHA8lxL6E16elS8O1TgCtb82XZ3hEwqDcdwXmV5caJ_hGNbBWQbXFC6BGKeqJY0MicN7akfX0jpVQk6IXJkwMr_dqQyHYyYVia38-EHBNLjz0Dk0LzeW1mssNmO41o6tPcrqudItdPLQDvKs7Ep6CkbDRFTexQZM-r8y9qA8KhdDmD2nrhCG65ZStGgrJVT5sHUVWs7fDVV4Rsrmjn3SlbacjvA_lkZ6E3F5QhDCSrEFAiqo-soaTY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHLF4uyuheNVoofTMVJ9o_3i2ZzPwNuB9rNakSMM2AYq7DpHVhxkzNeDm-bm1aMdPyDXkAHYt3NIKYA8bngFKRSPYRdrNNud72YeBxc5OyVCcj3Ps_zwDmmnHqTN2WUo01g28rsj1XIKOHN0_jN7n67T0W7H4UbzgH_LCc0oVWJbE80vqZt4PM_u7wzfwJB2nBGVIVoXeSYFR0NlPbUeMkCVydSJj2-nSdZLMtRAB7Z_8lsPv9GBaCBMfePiD1AM43zksxpkyMYcF0y_f3JMfWvuxSzEp3RlpzQz18mmLTOXPZHwfJHrk_rcanrVpgO7b6FskTHWhJrzsGCmpKQmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT56J5i0m8rlYWM3HRTDxRitWwaZyIvOXB5YRJKIIv6OO06d3RJWZGu2m4gYc7MqzULXbnLfZSoLFCfJWuQupFzfaqUrrQd5rBMjCX6Wm1xnJmu9eD7VdhkH3RQadimMiQBfga0IkmvnfrjPD_-gW44jJjX2rCehoGvnRmJRg1Sa8qi7_4g6AJHAD2meZ2_D7Nnkhz1NhtJCFAgHeRbsGdCV56EmYH1I94sTs4ADpCFxGCloCjQcOptQyjWk8D7aKbty9Vub62LdRVjS33wNS4qh-EiC0zvZoKXa3AIttOqsgBrFe-EYFb3dRr9PaW8--lFL_J-V367-HLOmdq_D5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtPkQFlzuTQx98Nd4npFTfZzyX3KC5Tct-RxMxnO_TGPomIj8i-0ZiNB1wtlXgUaL6JY-SXsY4VxB8_L_wDO2foMXSwNaLxWLfTqYIPXJShie3HcLGJoDxcnRgUn5tp4XsSFzbQjIUoHhUfo_eDfm8iO8CdDEzHmQa1YXp8cpy3A_mAg-Vb0IOpyJTNCNlgUiioHDCcCNR9sTws62ErGTrqpoH7xQ31pO8JL73Fr5w9KUECCNF5jMN0wlF1BinJIhYFllkzs7ahRsLYD-x9wz4g4Nm-b0oSsL-9iPoHOMAb99gpb2Jq6E-4DSJom7atUqmA8eOyAIXqQYY7UPVF9Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9RgffkNq-Wo_puADxil77tVpUQ3tUNawvhy1rhmELMBStKPp6NqKlrsK81XRNsrshEFnInfl7XyAbGUFUpGSPcfAVcK5OJomzDa3XOxWjBmAfBFLjhoKezT9sEcs1fWm052NryYYSPTexTQi1jkF3DUwRbzGI-SHX9kBgArmHkwLrJwVGu5gA7ua6kKmmLfHYb_hFGC04rZr1IMraejGGO8POHKmJdK9nHCQ395rMY0LxcjiBf3UpNwWKAxPANa_4AE-tSngVuE8TYrK-bwSfOWeMiR5BVrDXwvewS2kPJOLASQNvfMDa_cqs8F-s-mYrHFRwfSjRrUTjjdx1UHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpafRL4YkoBe7RdVw5hhOCV_h3P19fh0Ludk3Sk9x7GJg-_xpozfe-M1uwByCVP6803YD_PzDZtyTgFFsbQ3xlubM3bp_aGbPiv3XXG6aycXvBZ5i77IvLQ_db3gKbU0pI9O1kWWjggp-ZmkI4LFaXGJAVnvb00K0poTZyG-bUsRZ9cfeP_Y6KL93JFOVCc02g4pimQr-DoNt08hRLSZFc1_O4YIv4aVd0P5_3JGidy3s9vI8WLkeExav-wt7FEjtoALkGTmcpTnKCFo2rvy9bXQ584CcEsU11HHA3fuFZ6eCVbntVwOlWOY8lILZ6dJbYBgSv1jNXBQ-IlMoJDGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvT7-M10MN2lxkrw0CyPSItQfhjCtp2vnHPNCcvgEAYC3xt4NaN1HhqzmXp7kWDC4cJFmXSEyxBLW4YcZvWVPTkmEmGGkx3a791JPx5nJDDg7Kc5W9s1zmqN4nP55SoTFyjxXchFBT74vJpqUHoKtbYs3kdlbnt2jmpQ_f2tGXpxS-SQHitAwI4mWE4ApJ44L_UQDpG8Zlag-erbuqPvrHw8JrMbMG-_mS4-veChmSOgVsSb8EdEpwWMBO55ktKdtMIk2bynIJz9tMjwtxeVAoMD_oPnj0mYw7hddAU-4LhOKEO-H0RPWYw6bg4bpgpEK_k_9CdoT2b9qYTL35l-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=alKcyjakUgZg9qGy-wjnLfApj7BrGQ8rxurN1LuikboeaHEnZJKRa6N0jNGTzBTXAgm6Q8z3vquP9JPAfkwbEHz8fqSU_7aRFPixnLXdfMtdhg4-TK29r0V0wUhCI9_SRdfl0wl7bxsVVGhPNeIKW_2HwFpfFtP6u1fiiO6v575HJTeTNC2e97g2Q4U_w9x8TAJqGM6phqNx0S42keDxcM89SlzsEzxZDzJpeL5qvCz5bLt1xj9ZaiJD7gKZnt_x2rGho8IQA350P8iob0HmQlOhCPexyWb8HRXMjmaXGusNWt0lqzJPH6RS6W8_QOuE63c6XDDOs8UW1DFHIPOF6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=alKcyjakUgZg9qGy-wjnLfApj7BrGQ8rxurN1LuikboeaHEnZJKRa6N0jNGTzBTXAgm6Q8z3vquP9JPAfkwbEHz8fqSU_7aRFPixnLXdfMtdhg4-TK29r0V0wUhCI9_SRdfl0wl7bxsVVGhPNeIKW_2HwFpfFtP6u1fiiO6v575HJTeTNC2e97g2Q4U_w9x8TAJqGM6phqNx0S42keDxcM89SlzsEzxZDzJpeL5qvCz5bLt1xj9ZaiJD7gKZnt_x2rGho8IQA350P8iob0HmQlOhCPexyWb8HRXMjmaXGusNWt0lqzJPH6RS6W8_QOuE63c6XDDOs8UW1DFHIPOF6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=HPL2GuBUW9YZH-G0PfnIj7i39kYDnPwUHUTvlfmV1b6PWnglwJNc-Yq6QtuNIQVF9AkXyDbUhmaeAXmqQFN-7_BQJ9oax4Yoshxftjt4JmFJ8yXk5pP5AWjzG7G3L2tiYIQEUHEHajBrMcVp1gbasmNFC3LliwSoxLtzaWk2-zZahojRdyAJFcRtNwJZzBPFEbYnk454rYThykq2ttRj78xFDT1CebrjNUmvdgYQyaqnOFyfNAFdlJlN46lU9dzYVjvPJhHnaGhsX9LHe6xznNQRgtSQQIq8QQG0vmcum3P7Oumdn8NccqSXWq2xRnftaJI2KwTWysVH8M--_oO4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=HPL2GuBUW9YZH-G0PfnIj7i39kYDnPwUHUTvlfmV1b6PWnglwJNc-Yq6QtuNIQVF9AkXyDbUhmaeAXmqQFN-7_BQJ9oax4Yoshxftjt4JmFJ8yXk5pP5AWjzG7G3L2tiYIQEUHEHajBrMcVp1gbasmNFC3LliwSoxLtzaWk2-zZahojRdyAJFcRtNwJZzBPFEbYnk454rYThykq2ttRj78xFDT1CebrjNUmvdgYQyaqnOFyfNAFdlJlN46lU9dzYVjvPJhHnaGhsX9LHe6xznNQRgtSQQIq8QQG0vmcum3P7Oumdn8NccqSXWq2xRnftaJI2KwTWysVH8M--_oO4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ05VhBIi_nSWlQ97LrnZtK2ECmDZzLqYqMdvn9ntNngWcLoXMElp7UU_tSw-WgC_BJF8MsjHnYd9aruwahs9nw1bEOQjdOEpBHEB5vDuKGksqn_DXxS0gtNYQhjOtiZV6XIqTDMejPMMbPyT4mLUAKvUbx-Him0zQLvry1CwsIfTdwww1tJtU4A7WUKJLLzG5ApQZ27GJT-iv3y8PzaC1VIr8Jw6tMv7ouRRLLuM5R9uhLCMzx_LvuVsg7g2OPkRd5AZ8cyxsBhjs8ACbFOzKvz-NxnTqbBYFNWzxfujk9egNNPrTjmazzbzG9oY6ysoXnBb0lJVK2L3UjsKYGYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLMSPqp_iLZo9o_J_SFpyAosco1BpHJTZ5bXowdXKcqI1kjd4vpIOUJc-OfykKDDzmPYUKtqaJ3BJ7ZDXVB7kw3Ca0ClQY2-R6yCRaH-v3tPfZyQPcxDvgkAjnQ7Iar0RvvrzA5J2ZQK0i6qq80p4-t9hV4uk47f1CO7dcPI9ATdwEq89bcfhZFgm6J7S1fQ5jXf6lWnupYl1fqI8o6PSux5JjUGZOq0EmRzD1BJmKtrttphiOJP1WZGMFG6neqc8qPM4fn0hUGsP99uIdoJzU5tr22dQzOPxUsnhNEaooNRqTIftgfEDC9N4spg3GVxP0gqZigcmfVP9gw8Orvhng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9PBoGBgXNXlLFWrSnUKifp4k8CNI0M27cyUfKg0AZgHybr8tAxqLmvU23_gtVYu7hc5q15b1lxW9BlEl8OtBIK_Hp0YufVdD8HgH8CC2GQvsO9_wtCScLJxtHhcotL6YZI0RoKWrUq2zE0IiSNEYe2x4vZVUPfzWp7KHaFGf6hK9ckJDv9gHS-uBIkLHcOt1YJhYbWQhD_-XJqxbEFTBwFIawcQu7Q8Y95RAeOnukC8lTop2qLGQc8Uoh5na_kKt0o_i0jxG_NEcr8jDdiSbhvwBbmc6RuHDBpW9W5MQh36vKpGvcy1JWIRG6E3UmwZi6zQLR2VuS0YE-hUDIdS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
