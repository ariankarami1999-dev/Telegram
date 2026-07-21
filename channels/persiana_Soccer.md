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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Ov1K8U2sr_vkMmvgYCmWDt8QNS86cO17HmZwtozmbbS_zztZDBF7B0ZBpe9XOcEM_fJt2QlpAkRpBPc2lQ_gaaHlVeLhpVnZrP6-MValRrtM7RGNhcUtJfCDHAT6YXoUwta5YwA6eUHFihuqNe-Ga1oGJudo9acEa3lJ0cOziA1ENmKYf20BnSf1Vgm1sq1x9y4Zi5n-Gk8WoOr7wMW41lxUPw0n7zV9y-w0BrtjpWVI8N6pYljy33xQ5sDmfhteiBMOUFOInF2jiLS-wRLDJhiVOUJK-ibfR8GsNZUSZNpEsFX4gm15yL5Hrp6XKpm_hAsYWj3OuDuGlZhT3gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jht8nLq_RcXzCut9ZBoTnEPrK7l3K4HIcbHeNEbGgHqx59IVyiqK1YwqvM_3x0G6KeavW2rjPpCv-Ayk7S2UOL_bmuBoWUhFjTo5_1Ay0zTz0AO2C0u-j4KPaCUHX1q7Meb9kotsPtNALr9RIXlabIJjzppNazcOSTSWy4ThfQdlpN4Jc1xhgyXfhe1Gs_F_rKEGr2tCAFCHRYzjTJjJ_ueYuk2in7__aI62gYQNbsJRQKLmTs9NPzu9AKW-VQ71Bf7NqG5ft747eZysHfolBJf4pwtF4u_v0ViLvZkp5Fs5IxkWA-L30xNA6gU3OrhalLoFNaaZytzU1MWAzSnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26197">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKU2tLFziWPQPDbyzWYfC1x_TVYCZ-SEq9LvGwjpyYficBpt8Zton6ns0UskOQc6uxHZIkEBj4w9oFRJfozJ5pOrkRnTaHRvwC1Irn0xIDCGPDJ1BmwatUixy8D94sV_9KnCGoIG7mHXYyHms2Kq4tQHAuW-_exoVfGHGJtVPBv88aiAlYyioIu1l7Xc5IMfZf_JJNWp23eGQsj-yVJwXgQ4XloX2IRdkddMlosrkEnYCtmqS89MSiNTovIZM77YTrPzIjfHQoR-MKnf5Q23fHT-lHv7O95AYz32qApPM59kDpzOKUcFwNB6WGU5evcG-9PqNzqRLDiMWSF4TYqcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r30
📩
@winro_io</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26197" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=I5tLRp9pbDfdXMRUfNuOOkS69HCYNJuEu2pqB_o-to3_wNRiopccDpl9Bs9W4Tbwpe26j1EdT039a2j_sJfjw6DHIqaexEKO2O1WpSqy4g7ZYVpQx6DkWj37N8ZJfx61zC3WS72W_oe4JRpmp_mBJfVUtbKN5Xps5_iw8SoMlAu3zxLNPwsOveCsvsdYVDgq_ZT6E-1biGGAOWoUb10AugVoX6llBUr8qexjX8fDEOhyWdcsSTfcKr7wW1jl2dTvoarEGoXGX1Dc56kR1Hzu3brxheFAR-EriMOv5MCn_Qf_IhiYL-4JTDl_H0Yl2GmqTWX6sUENPOy-IYXIhJgDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=I5tLRp9pbDfdXMRUfNuOOkS69HCYNJuEu2pqB_o-to3_wNRiopccDpl9Bs9W4Tbwpe26j1EdT039a2j_sJfjw6DHIqaexEKO2O1WpSqy4g7ZYVpQx6DkWj37N8ZJfx61zC3WS72W_oe4JRpmp_mBJfVUtbKN5Xps5_iw8SoMlAu3zxLNPwsOveCsvsdYVDgq_ZT6E-1biGGAOWoUb10AugVoX6llBUr8qexjX8fDEOhyWdcsSTfcKr7wW1jl2dTvoarEGoXGX1Dc56kR1Hzu3brxheFAR-EriMOv5MCn_Qf_IhiYL-4JTDl_H0Yl2GmqTWX6sUENPOy-IYXIhJgDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgE1B2K4jRhI-I3Uazx8lqbYXR_oL_zmUfkQnTDLeSbkat2PohzUAZWfIKcNbwrfh7r9jMFJd2ZJsfbhNiQI5qlfM2Cx6BDcs3dMCu6hWzetONFjYlaM-Yk-C3xojAstQ0f_sRcoXgHjdfeIuQoCloHkKc9iVQMvFqJirnxpa3exFd1RiAGfo32pPS8t3ET-hW7GCucQ5CrbbgW9U8AoPGGk3L89O6VPRy7NtqBwB692nSQ3DGue8AONarV1Y5uGdbJcPjQdjiZBgWj3vMe-wbzNzD347A6lBM1QQR3HdXEPZ5gheFrs9BNqbdCZYf8eqSWu1FNrV_tW4FW2JUIetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXvrIbvtEfR_MxshQhDWRAIsMcgAy3lzwZn9LGLpvVf9Vuqo2pZW55z3JvNedm4kykWW_NiTxQlL_W1IC67UxlXgRNKFtb2tm-2xzFP8MKuDS0v34vSaPcrGoYVrn9cVlsy_xrFo_ZUSBYMs9vCiErqiz-9mRvoPRF4MoTzJqplaUWCA-iEYjWfOFNF5KtXSDFlKW9r7Qn6z3wKjczuieuguslVEms09xTe-JL7DFTOh7Fma-5ja0KgaSIGY7TH2Eq_Dwn1Qsi6xPytzBBp86_-3R9ouZ1Aa1b2fSQfQlz5ioYRy7Au41lduAdD_xxknOY_OPicG6IZFf9-rWbZQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luzSWFY2JG0z_Nt_BgwJET15XzIBfju75CoHj2huMW6nFJm3oCKDAyyP0_Dy7ShvflcfhIGsD2LTliPhy9N_Bx1t1veQD6C-gTncjRZ0ipzxUqs25Mr3y9MQXkq7MRrbGMjtdZNDwcBeMX3fu2JPdzvZJB85egUeMrv9xsI4Ae9ZXqIVOHgqo3KqwmebYcz9wnxlBfim6vUwmAMsjx1x78G3VtGRprn_H2SJw4jBVDbKWcgaaxnrblY7O_U2_4V9_Rwha6o6ZZtOXgcbjasnWtht6HZcExQ8CZlh5XmeJ1qbQm7XdVdAx4RDBgqkAjlQHoFXE2aZJSEw6xITH3MHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=TNXxm74ADis0l-ayyRHVj96-jmh_Qzc-0RR0PgPtgBAhB3PPVUAZFGPem2BXfBqTXvdYA2jGptcVgpN0FVmwsUx58DHAaKnDaBbtknn-KqdfXDWyAeodfFYAajD1tUCXw3FjENQYWM2PBfuznshvz-9mDo2mwjpD8Mfl4joBpD3bX0h0t8QLE6ohpbo5im9oB-Lu0uzWoFSBcaXIPZSsbQernl8M-KNybz2N1LK6WHC9Ot5bzw_WcRLZDLA2KLQAVi7BDvcbwQMS9Nkh0ckisrMGxFzj0fniZyX0ExzWWnDhVw61L63_lpEZ3lQ2SlBpULhvn7pgAZYWvg73vx056w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=TNXxm74ADis0l-ayyRHVj96-jmh_Qzc-0RR0PgPtgBAhB3PPVUAZFGPem2BXfBqTXvdYA2jGptcVgpN0FVmwsUx58DHAaKnDaBbtknn-KqdfXDWyAeodfFYAajD1tUCXw3FjENQYWM2PBfuznshvz-9mDo2mwjpD8Mfl4joBpD3bX0h0t8QLE6ohpbo5im9oB-Lu0uzWoFSBcaXIPZSsbQernl8M-KNybz2N1LK6WHC9Ot5bzw_WcRLZDLA2KLQAVi7BDvcbwQMS9Nkh0ckisrMGxFzj0fniZyX0ExzWWnDhVw61L63_lpEZ3lQ2SlBpULhvn7pgAZYWvg73vx056w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=NUMt8PIPUdjqkCheSIIk593_ltlAYZyH-8ziz1Fq_E6o9Llvvuq_ZVNT0Zwa7WSRrhOouXmQjOk0023xVuxVpzUk5RwmDLuOnrD7XpopGLmMgpTmB58GbB46ck-rdxfKl2hfmPRo9ko18Eag5rDge1CVWpNvIUBfuMV5VXIC8rx8oeVql1svVCHhiX9qok_9bUuKAVizQ2Ukrgo5bkz6aBYcNR2-YTrufX3GCHBtEUiy_JlCqTYTrhlPP5sfjwkafIxaiooJB7CSUbBhO73v3JbAjGID5C6ZqcfWJ2R_5lUnD8ZVdacCD_r13U7gVyo1CEwxi2U3I9r9SfChJqoOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=NUMt8PIPUdjqkCheSIIk593_ltlAYZyH-8ziz1Fq_E6o9Llvvuq_ZVNT0Zwa7WSRrhOouXmQjOk0023xVuxVpzUk5RwmDLuOnrD7XpopGLmMgpTmB58GbB46ck-rdxfKl2hfmPRo9ko18Eag5rDge1CVWpNvIUBfuMV5VXIC8rx8oeVql1svVCHhiX9qok_9bUuKAVizQ2Ukrgo5bkz6aBYcNR2-YTrufX3GCHBtEUiy_JlCqTYTrhlPP5sfjwkafIxaiooJB7CSUbBhO73v3JbAjGID5C6ZqcfWJ2R_5lUnD8ZVdacCD_r13U7gVyo1CEwxi2U3I9r9SfChJqoOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26183">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26183" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSH-weX1okAfvwDYUnJNTsTGABon821ptqRPm2fD6fdx1cLLsi_dDZsBU35LV3d9vr3tZZQmtrDHQAgngq6_l4piJEaqxtDUH0p9LoyKZ-_GICuCrAK0nf3tnjQItwxf_rv0q72WD28i5E3bTunXA0IlCAE5Kpg_LCVRCZ5TqMk3uVpsVQ4rSdrXAsS7rkIVK8_kLJH4oHQdE_erxnmPx6uuG3SRvUfJBXkCuBd3JT0uylfRoXq9BNT_cyRVc29-CC0y_uWoa5FT7jdYrUV9eqdLfFeyF5cFMtTdsUtGpll8kN9BuCmhJP3WppZag-EEG5HvT3pKCQnoxbn6BR2-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XihLpvqfgyx6ev2gL9MZQCDKvpxEI2J5u_8yfPZ4COYj5u6s8kKsK5grUnoN-jF4UeUimwKyPnLlgPoWlXGGFAku0w1ZpUamUVRN-DgE61pVOJ2TNeqmT_4_e0nanstsUVfuqpTqOB1-vZvdKJ7VmAuCA2o79Z_pcz66RcH5-j4WQdnBLCWOf8opYfeWVBGJixPVJF6qRiMdvMyxjs6o5jf014PU_KPesCgjvI2FjFTpiSrrjsv3gAsa4bCYtVrph6wCK4uEilJ8eaV-dg73GbiZeqB1vEs9pJHBtE5o-nscpL2qBX7hEno9Jx_SRNv9eVVQwoArcmKwUc7_UDNwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc3fTur2v9XL1cNaHTZYx9NsMA0RzXlFYdJaP91RuAqL43Q2cMCfKmfMHSlvmcnUTZscTmYUXYdnIEGL7RoBfmhATT8roTmZm7vGirjatCD16hddRYBllaIpRz0pYMZMpMfSfuciTYx9Na66xOq9us84ncm7rEa6Us4tGJgMxzoz6ejgZrXicbz2GbwFaQs7uBUWKkJlCCAUORF3cRnCncujVpj7apdeCa_gXwrin7i4wYsmzKr-jEZkRaYo-e6JcW4ox1CeHkoiMivY724LVGyBRd0Vj2qY1zeNEBuEeW-DTBpYLYR3yHHoh2qrNQFH1AUrP8JNFPuA4SWK5zxyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlrglLG8qoyOSLXvunmfm8KG2ADR3IJVfZMyLHA46Biw3xcXtqIekwTVuCiW5fEfeg05bWVLkhjRE8QLOtJgaBqOikZpp-eKyEPppjzAy91qUNGknjLiUpgdrL8R3EN0zBrNbHOvC2fqC9eNvG90tFMycZ-rYwSJXrs9kEFdgMM72wDpn0M8drq2g8ZZEEdGUeJlrU47dJwZ4iBGC0JWYeuIN0L0NkfGztW_x5r5CZ_HOD_AVUU6NU2wsknG7_gNwYQrQq5pabqK_l9AEbBwH_TKkLLuJZaOK7HrZPNlewdQtPssE2gHF_govjgV75W2qb0qBawNeliyIdVEbVpDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nij57szZSS_wfrN3GmkLbdDEdcCxJNtBN3Qsa0Dis5mAufuaNk0btVC0zvc51JlW84r1XHvgg46iAJhsVVaao46jPXGWQf0RU81buuxbf7KYX4U2ULM29VbIPZoBNldBInBaq3VebPOalPqkihxI_G_pXNdd9IhHiaC-mAasIDrMdYpVoR2DIg9kijLdmavWLA_b595P6IROkLapmJ4C5OiNzBLOsimvSfNbpBQcsxSAE5JJK429rNFFnvkf01pAPPXBS2nfYG-EkuVcAd4EwRh9eJsHlGF6rBuhMGLOWfHkDMXGfzWJNUXUEZroN5bBVfJNXPhidxx5wO6tW_-2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1L9CQqfd4KKVxWto8gwiunoFcCfoVIHwwor-_7Iw_yQNN4ogCuRyUOTM3dgY6YdYW0BlJGT4cDXNAxNgPceCAjkZuxAaFbb8cyCD0gnWVvPeoVxYNC-jA0N67n9VA9HbaiKES2o6h0_yblnL5QglRNKld7YPSwaVfwP0o5kzl9G36ClslXvAFAq3j6Uo9f32RMBjQVPlrCO5sOnljG5eX2O2EO6iXVV0MCQqAb9NCYTBx4jlZyj9sgMLq5ja3eEqLQatw2HlcrVr7QUc6iAExP0nImGnNLQvFgpMDxG0o3PsGuvCxTpby6CGacVKih7j9Rruo-PN3xY-vktLaugpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT5wport7fUSbDG9z7r2y8C4IJ50wYHv9zgcFj4ty2cgHjpPIdzi0ggNtxW8IMFXEqGz8oZ83IdVAYLR439dV4-lVpDzqholPZN-wQV0svh3bNhOgI_kDuCyWrL20BW8IWQ1u27GbJa9ymW7us_X_R9vJ0F9nU11eMSdrPBGeXDfeliVpbnTbGaj6uni70SGc9OPdazAAhr2S7mDKk4Hz1E2wfFUaDIQUwlgeg4zoJhidqF2NNkS8-olefTpJizkk6x8KKQ-_WjI49SU555kPwGYguG74EPdBPK_Bf0QhkDGSgIRq2v1EWqy4_SqQXPMrbcbYtfGJ_aLfyrFpMETHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4HeFeBtzhQBAWW2mfKv5TM3hhhN_keeUPeN-z_8DBci-6O8CuVBK6CZnEJ0WUt6QBatQFVUP2Lrby7QBAG7kgxXbNXU3WClEzpL1InDb_xvXTmHZ3hiFEGtU-V91w6VrerA_DbWnSK1s3nPsV_DZ8P3DoEHSBISw5-wvAwxPqhjIDke-NAN3pGYWa18syEPBAIUezn2FoSZMMbhm-z6rMscIxBwPq6l1iXpKAraaKk4vd_SyraJyx77aUNGTrvsaGmj1WqHUrroM1PA0abvrD1K7RGphdcUYlhYU3CC--6CY2z2F79bYMmqb_yG4GVtuaf7pOy1_l00WZt67Td2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3nPBqRLKkDrRhzERt6cnlq0-UV-obnQOPIG8cAfvFNJFw1ZDjbvBe45IMcNSZhFyhSGDaCEtqq59aJv0lOrj2T8uNHpZEkfxz2xbgitH-ri6ynZc6fefSaKYhhlZ5K3N1Wxr-fOwJ9-3X-lc5iYYBuyux--odidCcrY2Py1yrLMD7p4WuPeWkGy2YyzRd8T_9R3mNvBT2WRdgWZN2ozMXnDREOSkLUnzt7TNu9wbqjYqhBaV0IPog6Rl4lQTrCkTOVe_6tl4Om1yc2e1RgQnYEmLg4KCiaAaYTr0nP15jm53ADqokuHJHsjS7-_tZenVc7dSGxBpjADXQv23ezzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQTd8nzTeFJKKTO9bEg1s1Ep9XYQSjNUfEyjbolD0l-9WvlyBzcZd9MLLypU31xXN-I_ToL4TtS7d6eDoQjCXj2x-I2XVwRUQYNHCsVjZghprTaCKQzUYiMbrgBBskGVD5sTYp6-5RrOZWcEdisUAOfAEzC9jxdPVaVDX89iKQ1IDbqIu1aWXYO5rt5TuDBvn68-KLqMoLYH1pTTaVMEbUSNI2nxFUWRbequu4SJqo3xaD_gvnVzVtg1A80mEQya9sKOnVgng6o2rwnB-W_5AcXekBuldY4uYMGU_re2D1_Uii1VwXEhmicowiELsmVg1XgParHMVG8F05Qb-iueUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=CV915CT29M7TeX72LMPm5HBX-Ej9MVRKGyZnLynMDL-xVkM471c7I_9_moLVOa-nCrSHWqy9lj8La-pnLw2dz_vibqs06UbEEy0I-Ij5DFrufvk5r0muOUdvHysHPcFxRmmZCLACpb7PpSUoehMG4OG2QOFpZEx9lkiLdaTZUmwmfg-yRvx1lkdWRP0s31nXLsLd4PnCnohiAIYrnbllDabC_cM0pzrZV1nEoKNE1UrMmrN_Kc8wXMS91iBMde54z53rKdyCbe4w8V-aijFsVuijLLAeuUOUy48teC6GU4T3-4slpczt-52Cs_mEeS3m92FnHw9QXmcjfeCLi9C0-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=CV915CT29M7TeX72LMPm5HBX-Ej9MVRKGyZnLynMDL-xVkM471c7I_9_moLVOa-nCrSHWqy9lj8La-pnLw2dz_vibqs06UbEEy0I-Ij5DFrufvk5r0muOUdvHysHPcFxRmmZCLACpb7PpSUoehMG4OG2QOFpZEx9lkiLdaTZUmwmfg-yRvx1lkdWRP0s31nXLsLd4PnCnohiAIYrnbllDabC_cM0pzrZV1nEoKNE1UrMmrN_Kc8wXMS91iBMde54z53rKdyCbe4w8V-aijFsVuijLLAeuUOUy48teC6GU4T3-4slpczt-52Cs_mEeS3m92FnHw9QXmcjfeCLi9C0-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZCnqZytlgnq1TgJVwxNk0sl7beS1CzPsPDO2y0liKGKK3yZYk8Z6UN_EFhQLKobdptve_ovWJaa2AqYPAXN0EVwv2_vhF2mU7OCNDWcj9wjP3F02GCZuhSKdrFh8STt_5cZyX4JNk20OQDCcJ5WsmWBryiBLVmarTJFGZu79YE5aOSXF_PfSFzS0CNFF4wczcnZNpbn9vSMy-WcFLXqzJprnGcVpTjiF3V3ki9dbMCezk5NWgnJMFzBEzqPlrUWU9Lnk6DM56Ff-8h0eiptNHAvV6SEJqWXTrbytHtYM5ukumuIEg4nAEUdPpVBG_aM16G_6UI88h5kFf3uULp8L0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZCnqZytlgnq1TgJVwxNk0sl7beS1CzPsPDO2y0liKGKK3yZYk8Z6UN_EFhQLKobdptve_ovWJaa2AqYPAXN0EVwv2_vhF2mU7OCNDWcj9wjP3F02GCZuhSKdrFh8STt_5cZyX4JNk20OQDCcJ5WsmWBryiBLVmarTJFGZu79YE5aOSXF_PfSFzS0CNFF4wczcnZNpbn9vSMy-WcFLXqzJprnGcVpTjiF3V3ki9dbMCezk5NWgnJMFzBEzqPlrUWU9Lnk6DM56Ff-8h0eiptNHAvV6SEJqWXTrbytHtYM5ukumuIEg4nAEUdPpVBG_aM16G_6UI88h5kFf3uULp8L0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSIr5Taqrse8_hGhwUi4_EBLTOJc_Gji5CV1ax2xb1GWP14zCVB1x_fd_didY7DxKzVay4k5vSsu4gmpOq_fFRJli28gkNTySGtF9DBbniYKUIu_8XCoh5zqZ0WVckX6AX9t0JhCN8CpMoueOhcMvIPpEmw45vEwMQHQJC9begWJDRS1pAi-f1UR7BaT8b1MJRhZPVRdH0I7BWG2wDg-teZ4j5IydCItaJ4Jo7idHrsmw4j4GCIKyAQhIF6JEwo1mkde0JGcgcTOG9MPofeEPK1CKURcmpMIX3pFoFIKH4kqbx_rorSFwv34dr1RDMfXVu8o19BadlIPnlLZDikz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUWHLeID3djlJTyrnZVoUkTcVowK3XXfgwzuABQC1rIZ3y2fhvuZMilS_qsykqO80zX8oBIcOtfmx25KZmGGWfgRuxrA9nm0fs4_N5_h9jwfRWTnlWDDf7pd282ZmA_xUFDUxPL2tdYlzSZ5RUABRmhqYioQ58Ufy3ki3npDMdwY87UCZbxDV1n5ZuTuSa-WYciRmFbdwHrKGAXROkhcgxYFS4cNyK4-Fpkr0LdIwQKdTh4PSmr7SaFTZSeHl2xs9UKuDiD19YOUU2jEGhw62X4ROtCPVmkDU0kHB8U9RHMIfJ6mAQaRMYyPehWjvNACbqPQZmJc5jIZ-WqvardnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=h93Zs4pzL8eLPIl0gOs1Ao6h98SVuQtnQLXujYbRP-_O-bGEBVMFYbLmsodeuLZTd7cBCG8LoTvnY6A2buD5x8vNgmEGRcimKDlv8KhdN1GyRkio3zUbYtBosmCX0C5hypEqlBAKn4d-VKgYDFP4KrlaR-JHS2ZEhlOTA9IHzxG9F4IfqCpRxTQtBvvzmB33Z1q5Ik2YnpFsQzU_IniWepCA1DehdZJdivVg_9QmdoOeRCYFLhmcQFRBmVW9UhhgcxAL5lKP9J2kNcGVhL_vcB9G-qtRtqEqxJmAv6o1_BvCgt1BgvXeTj5HQu4JrD1WYM0UXPGlRn2Ku-j1Mdtt3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=h93Zs4pzL8eLPIl0gOs1Ao6h98SVuQtnQLXujYbRP-_O-bGEBVMFYbLmsodeuLZTd7cBCG8LoTvnY6A2buD5x8vNgmEGRcimKDlv8KhdN1GyRkio3zUbYtBosmCX0C5hypEqlBAKn4d-VKgYDFP4KrlaR-JHS2ZEhlOTA9IHzxG9F4IfqCpRxTQtBvvzmB33Z1q5Ik2YnpFsQzU_IniWepCA1DehdZJdivVg_9QmdoOeRCYFLhmcQFRBmVW9UhhgcxAL5lKP9J2kNcGVhL_vcB9G-qtRtqEqxJmAv6o1_BvCgt1BgvXeTj5HQu4JrD1WYM0UXPGlRn2Ku-j1Mdtt3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbSnw80Fk3h-7Hli3nzgDhqrI7IZMEQIeL3a5I2A5ttoEpurEO_FeMIh8a6N4X5MhSZfNX-TNYRZ8Al8JuBxAuKH_zn-mNq50_mUlkkxrKOGDHGO3pAX4Lx9sWKWx00bJo0MLl66d3EEe5bH_NTwzIWea42pfTgCpJb5q47KNNdSoaLWxpmaRIIe3QigfvCDzmUZR3JUCgTsjMc4bQ6CpURfS1fg8kiLhWVk1-5_TZY2RdXxNHVUZyTWVG5PNsTf93cOwSzixIOXvdannjY6eEdx2Np2UnO4oy6hlkYDtt-0uchqkKSIUOKSHFSFAfVTQpN8C0cRBMIZyyNrGzb0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJ7y9Ox4Tt2XjW03ecKxnZaUilwWZTk2iSaDIeWJTxozpwsv_cTM_FD5PXRAMLP6kQJsuznb021-k7ugfGaCjdki23LYtOqxYQNYFixfefHtwitYCcsMbpJMJnsbzDR5xEh-t0aPOgU2nx1ZQz9iD2wgbnAOJKk08xBXYD5XIMZspGSw8AaxEoML7lhBVLMrPFTYyGmjEvzLgLJyDPjC6z-AASDf3-OSNXwgBgE6rOB8RPO-5q6hHThj3kcwdLncsBvM8mkMV6fHM35Sj_pLf66dt1AvjTqcZGZlnYizbs9WLgCNLlnfLMlUGG-Ud7xaiLTLDjg8er5KigGHXczuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM3NiN103GjNxnq7n1adBb1nb3BPtfrh-hwGsQ1W4gioqQ_uOeWcYYOMnckj7P_RaBduF3ZMR-53hlK-Sa_2sw7IZKdk4RoaJNr7dD1oTfbXoUbtI8udWuUDVFaHqNF6XXNb-8DUC4g9uYkZEzMOj3Hjq9afwNcX1AwpReoVoRAU9gUVrXZQA5yLvVuT66_PprEn5yRjsQNccA43_hiwEbJzo1p8kLVVl61FnqscWrfDWDh2233tSsX4-jjCYq_UAw2VUV0wA4TeFLPskyZUb1SF_j2TSEHn6JlQdPRHlCcDaTrIRImVE5KwitXt7hew4MeoWtXJhVJY-YJoOVhazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7V44d58_8duo6ggGvYrtP9VijlWQuDeWvoGjqdW8zLWIViwsbknKrxW--rnxzMqMM5k8IIMWcDL0MZOzmAlT3F-GOGO8ORXGYqQvZQaOh2kWATISGfxYF5Bi8QdM0eCFqpsgMHDxQnP_Dqf89z8rlMY_m21IiXneU0NfhH8-fhurIYNgQ3H9uDL5kL3-WL-oaj2JnpsqLTiIkPA_LIG39S7orLuAIDnLNLOqpC6NOJV5a4R3hnlc_TNAXYkCfp7JHmm3sFk9zaweFIey19pzYRhwJNSZBa_hYQAEwFj7ibSulDDHolxFUYENDNW9gvhKziZbr-OQYpFLAnEQmXFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXqmkNCklZ9zM_pN5wSB6kLC_RgKaTlUhbHuavu-fZm7pl46zybW5JWAq8Vt6yj4E8v5x23L94Z0HstKenXn2TYs4BGeb7I_rNKyer9Ge-Xcb2_7bgsU0VPvP7WsCF2tM6PId9v3H5NBnPz0aD4qms5UB0INjOuCStsfhJr-jyRS_Jfss58V9xCv0XEx2KFwuBOYFDI1ojPzB2oU1SSv1WmZ2JSdpyXiQ3E4NnpIZAqrmnmrZ0SwsnWDzX6m8aEHY2S5Ucsaug5yv5gQG2bqG2mEwR6_XG7TmTPFBWSEUWh5xvrfxJoSFJxloambJ1r7Z-rzJRopMGaqWVXGc0hMTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aldZbzGVmjAJbsZ7ASmc4bIyzVPuSLpB3FTNoILPLgzFsGTQUDG5O_9ybDtdKozkMVKMMsvUtxCH08mdX8MX7txQ3D4s_wx2fLgeSq2DRQ_7v7HfIgWwZkK3vbaXrrst9B8PkqIafpfuusYC_or74Yfu-qoXaBJW6VteenSn9WjfclB7r81HpMIqQcHU1iU7CeNBSHNtdruCpBI67lotJOho7DqqP_esJOi5MtSCbQaGa3x_Ws4_25dBLXelDemkSicL6UWlq3WsnxW7BJBiNNRDpvMOiPNidhOhew2iww4rIMsvWVFERCiC4NUx5yhqrqbxuUvN8RWeJ9UrCNV6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeOGulNiQ9XSHHHeZh8SUPXOuAhuMUVeYHkv6Fsh_AOTU4RDwr8wGDlTI1cCbGi3XregA0y5gVicx4SalB_vvPXSBL5KQZkiiUL-3AY7qoHuZahjlYHh7LkgTKIQ8EnoxCTiJ_wyxd3_blMI9mU6MB5DoAxlAHaFH0ZAFB2ZlhoOH5pxvt5wBS1igYitH3MJHydzTtPWPFeks-36ac9DTk7-dQbmv3eI4DahadcJs-pxqpFikNDeA1XD5yi7YVQnY9aNcLM3vuD-A_gN4rtcQp0c_v_fym1E5nfa7ZW3PS-H2mNegLmQOuOBrM8v1SCPOXXGWYWgu4GMlrKzIe7ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U95fk_1FU6SiHKZyD5oiNGOatHGxPwop208BBGKuiBzWX7bpW4eIEuifpMqhZH1GUNjerFzWgzDZdhTIHjJk8QN_SsigvEzgnAldPyTIoBE5k165bruXmWIbfKxkaYXjQOJES25c5ho_UlToaQrozrysUHUC99ux6wMP6RJArURklTFpYE_bS-d2uzpkWZTuTihXoji1SCzcsuiqf8QwS6UmBF0cMSABstLCqlRGBNN3QChGItV5-K3PDuhm3Giu-MnxkPP78UdBNyNbmr5TNMRIZsnCV5cJiYHJ8vlS33VsDf96MqUy1VJ3Lad-Cm0s_bZ8iELpptNmEjyJ82PLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=PEGBfactbCM56VFtPfXc5rEBZhR_vNo2MHOSz3dVvFIrjTjwF0mPqDakseBwDeI9WE9a5APaHoJW7cbWIs-bsfE6WY0Nxkp2WZASC3OZeYvBOmej1TY-wQsgE-AlB5AZBenGfG5oTUEVkcncGHdzUC68qKsSUgo4xoshrTkApYm5eF2ZBQkR9C-wfhn7fpAf8AH2JrAycFiQbj-yoL1HtbPxZ94nmiZd47nW_QV5umF5VVRCEGlHGgDDTDb7h-hHz0DbwJq5khC8CDitNZgkm7q_v6zn12pT1RtIlWXS2KXcuMfWFglRZz-ellzuoSpXFtzkKvdipLsIIitzJkQ5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=PEGBfactbCM56VFtPfXc5rEBZhR_vNo2MHOSz3dVvFIrjTjwF0mPqDakseBwDeI9WE9a5APaHoJW7cbWIs-bsfE6WY0Nxkp2WZASC3OZeYvBOmej1TY-wQsgE-AlB5AZBenGfG5oTUEVkcncGHdzUC68qKsSUgo4xoshrTkApYm5eF2ZBQkR9C-wfhn7fpAf8AH2JrAycFiQbj-yoL1HtbPxZ94nmiZd47nW_QV5umF5VVRCEGlHGgDDTDb7h-hHz0DbwJq5khC8CDitNZgkm7q_v6zn12pT1RtIlWXS2KXcuMfWFglRZz-ellzuoSpXFtzkKvdipLsIIitzJkQ5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN7UwKjbJ9H_HEC5JyDAg8aKH5WuTMFkGlLPzKHJYuZitnCiao3cDTnm5H8CJbvXzkLjOGFMYdgJx09XEK_-M-aUbh5iw6-Jha0c01O2ItagjmMOaeQpiykRHbuT04YXdIh63ITwBGOerzRwXOc-fg2HhrLd68XQGDZzVgtCayf5Qjr3kuAYQruw1RTRw9bh70hDsA9PBcZssS2QAyAfKUvgtNQEHjFPPZAYXRpUIE21XjYr0onlMayQAAzIVtlHo5L-L2IZK0Oi0suYB7pAMArvRT-jN-0YZt4oQ3NH3FoO3hmk_5yRe2Avu-j6g_0Ig0FZ1NPLmNMu5FzKobSDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWGTh9cpGZ4U-dlfHgisv76aBEv5kYavur5Yvjluv-l-_ob9TuaaBzftK9HanoMklzaY0G1CfuJRRQmaxbWkYwdvC98rWyn1cn9ZgwKgEF6iBWyKHyLERtc2a5c1CIlVCQMIigryt9OJzXLcBWTUdiiNFcX3xSvc_nFI6ZA4Yw0laHKu3-GcdvGakv2kgPu16DTcsRqt8zAL0y446_VbA9tpL71ebJYq5XD400-XHupskxT-mhDNwIMzQwc307hviyb9fx8yui7nDmbq9yIM3n352FDOSWxtRBWPw4zHYdUZy3gnSCW8m-ar1L4jJKfIDAo7sxPxjCL0fU8zXyzeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDyoOkPHsg3Twp-MN-vg3UVfZZ3dIEisrIsdsPxY3XeDHBqODiE5ZPY4FR_jx98FRM5oI8hwIDS9mUtlsTXxAbMdW-UGuEqcE7a5oh34nfp-JTUaT_vTs-MH0uw_WNp_fzbTNZPUXnj6FNcOJ8RcDe0UBE5K5Q06yHVpkSDwn4IJxkbCtRDB5humcCTkNfL3RUz0eOo4RnNngqwVpMlNnqU1g_FRT8UZR50NrVUgX7iYTltZTzFvigCSM0ICDpKn8WLOOt7ywK2JTyVmTYqS2b9voooZaMs5fH5g35e55-Rqw3EEkYAkKy1rt726tQkBFJu4B21zfDQokFqk-gBiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4BElZJZmsPdz4NMINFOxj2WQjoWGmkVyxF_k39bTxCct4oXvweF_IEJXoqZ1GEXLiTkRCaxR9o_XHOQBAqTT0F4C9WkR3ZYFT5wI7gOmcESHIkl_xHXohBBfI2kJc60bmc4UefsVfvwdl298vnSU77ChLDTxzGY2NlkhfpAAEsi9PlY4pk0x4Sidr6NTQqK-RfWLixMeg2aGXWoPZN43Di51myzKzRnoEdCfiTrjWFBQrMF8zY7899cs6is2nXSe-YeTZTLXeKQX-YCG8v-bGTQJDErI_pgMZb8IJsqO3CS5zvl-fEVD2d-ktaYP0RrcySir482rlQU1g-IkEOzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6tCD6v2GYqh8x-SpfbbbL0XugTpLr-1BMAgS4iEt0n2botPTT27CUD02OIzq_0SCREyjQv1zYt_JnBUX6beXAiUfmDTPkdp-1qoFCzdWDp7IRZDl5Rfd5oDdEYCYbZ6Xs_OuZ2PgPxrXneCS-o1_uPKIEKrK4Al1n-rVS9V5ECAV6X1vHw772oaVoulslMbGkkPFnCw1U5doSpXV9akw8jeq-uET600IgzWXbamdTkh1l6Wp5-M__nxjLMIHkVuoqX5kMio40b2tGPnZAXK37bVIbsVjpFjYim6T2SsKjFCBg1grtkq3d8zHE4_LKCbhIk-p8C9VvAQZDWUE_LmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnDPMOj4PH-5Gv38HKUi-5Ar4zh6dhPtCMaLf5TLyIr9QY0-lGosTcW7vg6-HTumrVS9dIbAoPE-OEi_WKqAQc73ZOrGxbRUXly6dos6b0vpC1IEzGLDgTrIolSKCqsA1qtDbsFq5C0Zi-EyOTKAe9RNHD_83KeJhI3rMPrUoTqz-YEl0lbsjuT-_k1DwRJvv88GUS3Fs_V5z0-iqS60KJHUW1DJZmY68p4HubToVpGX513t4ehIDLORCMVVQwlwuabEIqCK6vZ6VYWlhNRoZzSESqUChkAZUhUanN9AFtXZbl2J8KSr6pK-Ghy6cf-hU3ZaH8m_4ZxjqpSzWKYrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIE6TlS-Ja4i08PHYh0aM1qpG41NZJKlmwrGxJ0SP4CoWT8Laz0P-wMIyNvLD12YWodG4MfbD826XG04HWqo3PD_40RhmHB81uRxCTGaBQ-H7xVnqF7tDQDznNLtXUThTnuoKl7fSzEwyHIWSKJ4KIUn-NhGV7DZHJjBOi8kx-Em3jKZDH-fhuecYtk08H2FOx_hjartSPb4VKaLihn4e5v-FX2r2B6q_IAqW-3gMREyl1tYMOQEe2lq8iHQ0bbwlZu-MjtGcelEDlkmOmfdwcKjj_OZsjnvKNvLAYuKZGfvuUzZ7AxBLAseHlDwUrVxUGOHBP8l8HHukRfe2nJQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUqPjZFA4DoVeHRoYqtVaGZMmzhVTKrOE0a4BS8t_89WNMUQZfYquiOPzT3mM7OUU4bolCEJNdQ0137sR4N9nKGFFo-ieNZfwctrnkYSz6_uraLwF847ppxyuwpQiCVGuHHvIGvnaGKAvChEyc5qTCuaZI_2V6b56VGJ0SSwAOkd2_CmGB9zdKCJUofpCF4n-N8gTKTi5wLMjcxfBMwKuRuyqe57A0C0HNZYdnde2E880-Ax9SnummFCeZ_J60J6HuJff7azdDhTQVhw9vwABxS8Xsx2VCKG1xkQEoykGpObKuBGj_XBVS5K9trT78zwiHXsbq0V4NaxfpU_gUMbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4uOiTGNvqdWxekLP3FR_QsZ9Wbbv4XSwwNn5uH_ghG3Vnzb0HtK08IWcJgcWmBd84dRFEHkzCLyQZj6x7qESeg4oRkgikzUII2hEX4uLQ4-YRgTPfXPzicXzjafgLE3um5W_VR5ZjBK5TuhcSMCl7r3g2i-2BFfJnnDqR5sFq4vKcc9Qh5UX0h_UGSqwu4EnTW_6kveo14jveToF-Gc9c2Cjn1X9EFCoSDrPJz-XyjrosdKE7bEdjL2oxQdaiVK6nxW1sUaoZ5ZstwEvIPBAtrIu8jBmNQ3ouG_80_tyaxXi4yEUTqt9qyJIx_17syJaaW98bGwJx9neij3irberg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764SiyEoKQ7-NeaI2k50hepVCubpvAVXNXInY-dGfmV0BFf4HX4YggMR84bxW-Zh_ZAHvzjUuXxRBEWLigRhP7a2k9moIDNJlGVgPP_zTqWeS6SwWprbv_GeJUu_hdqzarQQwVYLQRCSYH8ckykdnmzEkkPm6mJVLBiFS7Rj1aU8OFjSSoQ_NKvDMcdLtLfbnYPEwdwo1-juSqhpNt8EJNuzpK_yHylzfIu49IjEgbTJnRZxtYPaBRtVFJcHdJlJmOgBmjncipp4GmX-JxXns0r5G-h94OoXHWYOAYv8fGIQlCSh7fcdTyqXv4ofR1g1bgjwOgsrQ59BBchX88oBSku4fvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764SiyEoKQ7-NeaI2k50hepVCubpvAVXNXInY-dGfmV0BFf4HX4YggMR84bxW-Zh_ZAHvzjUuXxRBEWLigRhP7a2k9moIDNJlGVgPP_zTqWeS6SwWprbv_GeJUu_hdqzarQQwVYLQRCSYH8ckykdnmzEkkPm6mJVLBiFS7Rj1aU8OFjSSoQ_NKvDMcdLtLfbnYPEwdwo1-juSqhpNt8EJNuzpK_yHylzfIu49IjEgbTJnRZxtYPaBRtVFJcHdJlJmOgBmjncipp4GmX-JxXns0r5G-h94OoXHWYOAYv8fGIQlCSh7fcdTyqXv4ofR1g1bgjwOgsrQ59BBchX88oBSku4fvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToOKMJ_zUzZONYIRYJu4Up0NzSnCiePsvymDpfFo463dRNIgxOUc_Tp9_V5P32Dha6X210_MEI_6dacvLC_f2QmBAF4x0c_I2gX6YmuLiQvzZJJqQsoa0nsHu9GSEJbiezlhTOVoK8BAMoUT9CE4-0zOjzNUi0tThM4DY5S6S_IRG_4wbTOMHfg9-ItPkToaWkN-sBxtyp5_Xg_-PJAFQrNCAQYpSk21xrCUt62r9WzNuhv8BaTlTtb5GWCyJ9IHIm6RWedRO3JgWfyt4ZaEXmxJP8fsjL7B2Ghzg6aD-LIVX4SokIeXk7ZUOmFngp_apcp70U0kkJ7UETz4pMGppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=tHQ4yDG5kOWHAr56x9ZWoQ9U5bimWCcRYdeJ_nP2ftW-jWdC30A6EkhDxmc0Je25Lc1VRWYbSJ-rR4DLXr5dcgV76xsr66xogZY822H_GrVNbryonAsk7S_2NVCTvhMICwMOGdIyE6iGk4qpGvjbDMN65lh7NXltcIYb4PsOyjZIUqDd858vREC9QfKqlFFTtHdt7UCg_2K4hyVBRdU0I8aRnG_h0R_mfjiCutNVZxH6-yQZFGKG-GlzKPGL2Ahs4Q6VGETlyHVMrRFjgRpE7mf-qHTo5wSd_yzEKFRhj5NJ29Itzlnsml83oAWxxIkm5fFcbR8plzBVmDnQWwxlDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=tHQ4yDG5kOWHAr56x9ZWoQ9U5bimWCcRYdeJ_nP2ftW-jWdC30A6EkhDxmc0Je25Lc1VRWYbSJ-rR4DLXr5dcgV76xsr66xogZY822H_GrVNbryonAsk7S_2NVCTvhMICwMOGdIyE6iGk4qpGvjbDMN65lh7NXltcIYb4PsOyjZIUqDd858vREC9QfKqlFFTtHdt7UCg_2K4hyVBRdU0I8aRnG_h0R_mfjiCutNVZxH6-yQZFGKG-GlzKPGL2Ahs4Q6VGETlyHVMrRFjgRpE7mf-qHTo5wSd_yzEKFRhj5NJ29Itzlnsml83oAWxxIkm5fFcbR8plzBVmDnQWwxlDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=mHGRhmuF0EPib-3ikLaIaNnTkRfgi8bThM36btzI99D0zf2NSrar3cX_iKEg24OMRphUqyv2VAJ58BaHk99WIWOh0RcCTop7d1wFwEEc9o4bDFWE_mVN7yv2L1-j-9uqIiVikGw250Lz7GeC9wDq6grygGBZb72Hkgxcb7-6NVvE6HWiV-20NEBOOSr03UK__jKt83Vsj4zOggOUZmGb2V9qiV2A3KMiSC2I34ZZQ0lSLyL4F716Emeez2nhwrBO1967m-YbMZo98wisefGZL8xX_maVUSq0jnEpJkF8LlQ4MWOK2cX57u7d7phGdFrc76hntUSCGjTpQX_jj_8iWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=mHGRhmuF0EPib-3ikLaIaNnTkRfgi8bThM36btzI99D0zf2NSrar3cX_iKEg24OMRphUqyv2VAJ58BaHk99WIWOh0RcCTop7d1wFwEEc9o4bDFWE_mVN7yv2L1-j-9uqIiVikGw250Lz7GeC9wDq6grygGBZb72Hkgxcb7-6NVvE6HWiV-20NEBOOSr03UK__jKt83Vsj4zOggOUZmGb2V9qiV2A3KMiSC2I34ZZQ0lSLyL4F716Emeez2nhwrBO1967m-YbMZo98wisefGZL8xX_maVUSq0jnEpJkF8LlQ4MWOK2cX57u7d7phGdFrc76hntUSCGjTpQX_jj_8iWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=pcHa8yCc6Hu3f3ygixJF6zrG62KfklddXiYa2swp67guEXEq_sb3kqohfr4GRx9RswLbSXbKUlUTlA9sPvd01JTJ3mEUbhUn9rux942IUzRu5Jir8duDZsFbzXzNNdnKcAzH0hvowCnNpzWkNPssGP6i8S3mX7AYyiClOUymzimVsJFxI6qzmPn4et942K3ixk8nnjUBK4KUTNOqd9_A-PMghYaLaiofgfdVXjhZPTnqcuDSyerDejSgt8frO0u9MDW3Jk5QYh3-dcWXa3kjnI71l9XvZbrn2JnsA_PvcfkG07msKwsTeeo6PhDxYNUorR2eHQlkN4LIkMWvWPLAGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=pcHa8yCc6Hu3f3ygixJF6zrG62KfklddXiYa2swp67guEXEq_sb3kqohfr4GRx9RswLbSXbKUlUTlA9sPvd01JTJ3mEUbhUn9rux942IUzRu5Jir8duDZsFbzXzNNdnKcAzH0hvowCnNpzWkNPssGP6i8S3mX7AYyiClOUymzimVsJFxI6qzmPn4et942K3ixk8nnjUBK4KUTNOqd9_A-PMghYaLaiofgfdVXjhZPTnqcuDSyerDejSgt8frO0u9MDW3Jk5QYh3-dcWXa3kjnI71l9XvZbrn2JnsA_PvcfkG07msKwsTeeo6PhDxYNUorR2eHQlkN4LIkMWvWPLAGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lu3M1lOV8N-HUHOybe3F8hLsszlpuv1qpR9QPN7aUpszm8KToujk_Fr7TohBowRGBMmktFPGGPRbeoYNpjopuraCXqb7tT0N1MrFxWHsayAR2zO8HcGmE2CRpIRX2FQNYhoVFWrDs--aKZgY5RrTqJB9_0MRwmk_8t_fbxVPLXcrJoQDunV9JetHkQZ-pSNj0JGE_hT4Lm9VrKUf93Zts7XFUPCsOfdKdyx7YMIY0BeKZ0StO4rzOtsQaR8TE56Er34jFRUCnDENv5JxWtAxfursBbl3gjV7M_69gxiAkvQ1J8xrDTgjUcEMMeuBo1OGWcGmroDNC8yyJ94E2yGAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2MRY7bZtB9pQMeAohM7qvQmTu5lh7eitfbM2YcG4Mlf9AAPQIMEAf2pPX15xIVs_PbAG7ySpLMgDdO2Eq0uNplVJ7auCCE05mgm5UTSqFefmVFOktmmFqKt5wrGTtv3NcpElR5zsaH9kQrWJeB6z6Rg_iReIYgNyz-t-MdEvnlwwrgxSghtmmaGqFw3_G7vdDCD7kLIVH8nTR1wm4Ykxx-SnAVBUsn7fAHceGFKSn7mlHA11dGwowHf474on0Cy7YYDYtIWEPfQbxa5lIzT8w9ZlEmNmdNmpdHu0x1XmFFdaEaLfgtNMe34JfO4sILlxm-lRv6MIGkFU0nivPBdGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=V6e6rZBgdWpSW49L5Hi3eOPq5ny8s3SV0wuyMNuyK7iiFXcvJj9kYYhXcAyujoPgaXTpAONQ2Fk6kl9tv6SrcV5xrfPljhn6vl7DSJlDR1gvugTocdBviLL-ErsP5_3xKa5xIb1cZ_nALiQJteilVRKSV-h_dGhj22zrZA30_o-oe2J7OwrpaiiCkalQsO9JPJ6rt2f2FyPtUIThgy78FCO4IRNc1UOCfaQMwib3VmEGb_CxAeRptwHsdQNf3BA-fT92iS5Im0ngTzr8MIq5aflEi5c6HGHMmwS2MENzt-1QmyXIzgR9eFTow7MOpxSf2scjj9WiLcCc48U7z62V5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=V6e6rZBgdWpSW49L5Hi3eOPq5ny8s3SV0wuyMNuyK7iiFXcvJj9kYYhXcAyujoPgaXTpAONQ2Fk6kl9tv6SrcV5xrfPljhn6vl7DSJlDR1gvugTocdBviLL-ErsP5_3xKa5xIb1cZ_nALiQJteilVRKSV-h_dGhj22zrZA30_o-oe2J7OwrpaiiCkalQsO9JPJ6rt2f2FyPtUIThgy78FCO4IRNc1UOCfaQMwib3VmEGb_CxAeRptwHsdQNf3BA-fT92iS5Im0ngTzr8MIq5aflEi5c6HGHMmwS2MENzt-1QmyXIzgR9eFTow7MOpxSf2scjj9WiLcCc48U7z62V5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=e5ij3pDEBAO6zvuQeRAn18CPFNML2ORkV7caQQHhgWAn6cnNvODCMGSFskVS0z_kshmj0HbaKCCZrg1MfzJe-5hejHYtLdFJL_zfRry3OCnbRAh74YkLoPznrsGlpTAii373m85E8Gw2e6GMeG2Y9PlRFglofj4uYLjWwNwYTApZuJCVT_wvZBdMwGVwyHhp8jvybDX2XrKAnkb2SghSzvffSJ49xFeUy11X2UGUIWFbAHug-cqZmM5EQf9-vA3WvATexMOEWPjOJelxeFXUgC61XfbA2-CemUuf6W4PrdoCHFDyM-CqmFNQYaQwOnMozl8xg9-loC3yY23zyOYFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=e5ij3pDEBAO6zvuQeRAn18CPFNML2ORkV7caQQHhgWAn6cnNvODCMGSFskVS0z_kshmj0HbaKCCZrg1MfzJe-5hejHYtLdFJL_zfRry3OCnbRAh74YkLoPznrsGlpTAii373m85E8Gw2e6GMeG2Y9PlRFglofj4uYLjWwNwYTApZuJCVT_wvZBdMwGVwyHhp8jvybDX2XrKAnkb2SghSzvffSJ49xFeUy11X2UGUIWFbAHug-cqZmM5EQf9-vA3WvATexMOEWPjOJelxeFXUgC61XfbA2-CemUuf6W4PrdoCHFDyM-CqmFNQYaQwOnMozl8xg9-loC3yY23zyOYFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=fSjn4VkVJamzsoeAf-1QHJOA1K-OjVRttW4E2e6oGuYLHluVBZ-FTFDRDwdzx1Ab34Pmr_34v314UOx_yiJtfiFhIEg37VGi0Qi-8HysRy5ZqJAjl3vMpwsRmIOyNmDA2mZL2-CsrTwALbbldBnC-b5iRca6edExBYkU3T_LCUotRMpaJtDmarkaUzCpU4eHBP7ZEpLZsk3Pqm2CbbVPSrJq6oPXsB0tZDaUWMbK-bvVs1sBMmbzrbhQjVEPTl4vw--7SftiTOt7OdDNkiCvLRCFY2qpiKeEAKVlEFW0eeJ6baXVNjpG0QAJgksx2jJOwe_AmLX8vyOKVWqnSpUi2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=fSjn4VkVJamzsoeAf-1QHJOA1K-OjVRttW4E2e6oGuYLHluVBZ-FTFDRDwdzx1Ab34Pmr_34v314UOx_yiJtfiFhIEg37VGi0Qi-8HysRy5ZqJAjl3vMpwsRmIOyNmDA2mZL2-CsrTwALbbldBnC-b5iRca6edExBYkU3T_LCUotRMpaJtDmarkaUzCpU4eHBP7ZEpLZsk3Pqm2CbbVPSrJq6oPXsB0tZDaUWMbK-bvVs1sBMmbzrbhQjVEPTl4vw--7SftiTOt7OdDNkiCvLRCFY2qpiKeEAKVlEFW0eeJ6baXVNjpG0QAJgksx2jJOwe_AmLX8vyOKVWqnSpUi2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=IdmElZS3mMUf1duRaxwpKHm-AkkZyTe62_haCaZZfXKWzmlonO65F2I6zcIJJ8Tw1l-TDludl9sV5gfbiPm6bS-nAyO5AOMgCu-dALIDbX3t_VaTeLeEeF9xTwoZSYUu5aAY7v0ubeDkKjvZpDr7E2rXT90uMPV8NB1EmB_pVdxMlTYnOQAyZdsa8mhhS8L46h0hURtTVxD_hbXlE96xdS7qF-FemsgRQ_QQY_MgaLJOZQuKMIA-Pl7ROzGDsUwlu6TfNVJ0o_hQfmfY1m0yJ-SKQlxHtAMV5sc97MVeOTZwb66r6IC1ZjkLpfn_l6CJD_P5Hog_CCuLfRYhgy6gtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=IdmElZS3mMUf1duRaxwpKHm-AkkZyTe62_haCaZZfXKWzmlonO65F2I6zcIJJ8Tw1l-TDludl9sV5gfbiPm6bS-nAyO5AOMgCu-dALIDbX3t_VaTeLeEeF9xTwoZSYUu5aAY7v0ubeDkKjvZpDr7E2rXT90uMPV8NB1EmB_pVdxMlTYnOQAyZdsa8mhhS8L46h0hURtTVxD_hbXlE96xdS7qF-FemsgRQ_QQY_MgaLJOZQuKMIA-Pl7ROzGDsUwlu6TfNVJ0o_hQfmfY1m0yJ-SKQlxHtAMV5sc97MVeOTZwb66r6IC1ZjkLpfn_l6CJD_P5Hog_CCuLfRYhgy6gtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=DlM1X1BEKUEYOZPAXSk5UZWYazELW1KnUQj6kZZv1u3RzddtSfGa7h_Z3RNpSD02Ry1owllXSqXoX-3H_lCjnC2r5jUVBEjAqlUBtvIvXNGFGDdYB_tT4WFJHOmd8PVuZgbm-OhxDAr27wqPVO0fjHtnGNL861r10MhhkefospD_Bs1LXAbeS3m2e_ltsAx5RdvACucszEQhsLHxefYnpyOCBi7qqYa-e0D_yBb50WB4G0hPAeQ0KA2BmnbMUD4eBjm_aAUt7pikKXI24YoC3hb2gfHtbriN3w22ugGFVTs_J4XW5W-y1lCODkHiNrlFg0RY4Yy-wsAOX1oXgwGxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=DlM1X1BEKUEYOZPAXSk5UZWYazELW1KnUQj6kZZv1u3RzddtSfGa7h_Z3RNpSD02Ry1owllXSqXoX-3H_lCjnC2r5jUVBEjAqlUBtvIvXNGFGDdYB_tT4WFJHOmd8PVuZgbm-OhxDAr27wqPVO0fjHtnGNL861r10MhhkefospD_Bs1LXAbeS3m2e_ltsAx5RdvACucszEQhsLHxefYnpyOCBi7qqYa-e0D_yBb50WB4G0hPAeQ0KA2BmnbMUD4eBjm_aAUt7pikKXI24YoC3hb2gfHtbriN3w22ugGFVTs_J4XW5W-y1lCODkHiNrlFg0RY4Yy-wsAOX1oXgwGxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=KJnwrHzQJXGVgwRsxoSmB630yY_BtbHDeMucOIJfdZQXW9LEVUSRIztYAr8nN93uKjSmFcpl1jZEUluas-cRgRMOAqXmrDvfvHB0wd1r70-gQ-P5v5D0rgxPOnNuquvOgVjbrkww7xro4_WYS8fp6m0Xc5gPVR0YIdrlS51VoQULmx7iL4RSrRSMvtqTuMzF7nekeXMS052XAJaE5mfmoKr7PhRfnNuSLMG9PNJUZHqhQnPSVAHktQ6QjE_--Dmox_8oZ249icK18c1oAcU-3qZXPxgO34RQbgijg_omUbilOArfpfv9PoKhke9hJIwH9IrTTXmEH61LDxCsfrwTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=KJnwrHzQJXGVgwRsxoSmB630yY_BtbHDeMucOIJfdZQXW9LEVUSRIztYAr8nN93uKjSmFcpl1jZEUluas-cRgRMOAqXmrDvfvHB0wd1r70-gQ-P5v5D0rgxPOnNuquvOgVjbrkww7xro4_WYS8fp6m0Xc5gPVR0YIdrlS51VoQULmx7iL4RSrRSMvtqTuMzF7nekeXMS052XAJaE5mfmoKr7PhRfnNuSLMG9PNJUZHqhQnPSVAHktQ6QjE_--Dmox_8oZ249icK18c1oAcU-3qZXPxgO34RQbgijg_omUbilOArfpfv9PoKhke9hJIwH9IrTTXmEH61LDxCsfrwTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGQrH2UIgakMIISuOzql6DuWqkq6eGM30Xd1_kYUlmhVqld9VSxNLrF0K5JZCtL4YTzuGXojbOJXYuJW1FTC-viwUPkhy4YIvMpvAA9hv2JBQFlEi-LNi9dwypM6rctYUD5vzkvyONFmhHB3wO9X1_OzhdPr7Rewt0_fvxx3VNvOnxweHEtBvZCLJVuL58jP7VdU89VxNKTlyWm3MbyiN3RTjn0D5XFjGFa8lDYygmzXNGI9swkC08rH8GpjPwOdG2UCDw2xZrhSU2jEETmru4UbEQ1Onf7AFfMMZB2DJVOnTyf9hU6aSF9D2Kktghj69QukKCjmThqOH8s1dAaWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru6sSq_HsgMwCXZqaJO9bJV9PvIyL65OteooM5t4FCil12NQ_RvJFwyK4--LgLNOz2QVYaiBU3MMnO0XcJIzxfsI3fjBeQ4FvVU3kltHV9kg9qqEKKt-N3Iwy9MnQKwRFWwg0uuyXQa9lwjGX8aKxdy9cVcGmYEPaBRiKDk0B8i1WRdEuG9WMaGdxekA3vlqfk2nglUfZAdiU01AdyRkQUqstlE7ObmtM0xiyCz0nSknuSKCqbkzUkM8mLp8DLhQvfkj389SvDlpXwtusKCab8bqpRj6BvG799xJxtjS_s4QKNcbexG5JnyvAnziUrKnQDqAMQOU3Lj7IDLkCybXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTGthew4CIjIiivpu2S9i1Ale4vAYeWEtPjI00yBMDFkQ2gb1wRnhhCqvS4yGz5HSjRCOom-NG9D4kWDgUD5tE3EcGIHruMzJG9vskd6s1GKKLrzAq-oa7uILEdtfpd6abfJhgCgbrCT8UOJwrjCu5XfY0R1WnihYxwDkpKRTyNWcjuWDsCDrJFVKUUvstdaOR1xtLi4O64JC-w2SrsDR_mV-UNveO3EQm_ikgZ8avhO0lZxL7aI_c_GY3Vjdr50DaOtpAT-BZIZX0TdJ60_Uy5QbFAGX_JZ8ayr6a6jxEsjRiXmPKh37le0LoYE2bZhNQ8RCP80OlsKQC7q5tmh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe7h9wLs_nIbs38r1bw3jhGAu-n5hCpVS8icl8bhA2hTKn3-XVhRrtmsbVpMcvZBht431ToJTdGwfXe9oNMc4y4NcECQHxZ-pr-ziyBGCNiu2inqDqDbQY6mtNdf-gOAd4vSowun7nc-2yoSySGqxr7o8OlI9N6FezVPvUvSYOoMH1YztE0pgW1oUNNL_CtDYyV8kZxyVq6xM2aH0MvMxKDT0SdL2fO6wxJDmwaYrxNhPXBx_9rW114p7Lx6EpGYIhRpOETv3WV3LTcTd4KN4JBlBjEGGSVg12Qm1l_LgLZZ6GPaQde9nWZDHpQg_Xau_z71cpXG7zUSUNDkZTUKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt5VOqHZAzCU-MDwuqtXmH9KGWt1D2Fffp2_uW1XfvYS3rA4KA51lBxNtuBCPqPpI4E498uXP6cmkJx9eSGJ1CvVHqXIaHVhdj7e_rPwdRTDMTbZ5MHGNo1GiC1odEIvNFsEiQPKi2s4bHzVM88RkboDNaawYGmMp8laglIp6OWgo0j1x1HKPexFK9xASvf9UraD4bTuKgBsHNTDozqtpUXFb8X4fMXcnUZ5JxokQeQl31Xp2x7ivqGq9tJFyqBLJu-aq7INyWSae4GJqp7EDOs1Amv48yEUsAWvrBxJNpa4v7FnLJQA--IEzZIfPgLwajMrXSBmw0yG4D2lezoMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl-JPGiG4op7yAeI7dYNhInA6FqrjVNYR3gPaT4nrKLtBZuuD-OzKJDKazOiwEL39sOpvTxGmy2eb8FT6OUOiM0C9fde1uG7q6mKBqh7DkQvkZiQ3epTMSX-Ex-oTNvm0j4wc0tfFvt6QqnV5pEQsClpbl8NBfrBo9XBVUxNg5Sdcsyp_LMiVjcgXuW-nrfb6EZlJkn6nKgkxje5YkhiNF9zysagytG9kjT-4BIL9a7_gxliCnviUTOU9ITz51uDz_P6Em7msRKnIBQT6yvwFotVOyQXIpB2R9wFyshUQmpWdz2hajK2XEsewslAcZBwkq4E_VU73sx6lNrGf6mHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiWG0ZzKNLDVWCKC2kekf0ESuHFZ9yfwH8zq8rW14y6LoNhYz6HrkCTwryTzoCVQZN1Lw7YO3fk6fyvcXb_pPVKzhRBeh441QwrGRdGwj75pEdOa6S_Wnl1IaQfS9jTBzHQpPbq9E4XFN1CsWaJZD9txfu_RX_8QQn3Qn6Ep1r2_d8Kgpai_83RSm0oGOKB7BnTZ-1bqzeUdHs9wY8yM_uLJqChcf4ZQ0fZmU1eZmjxnrbIq3Crn4JlgEYZymfEIkvQYy69Z3F23G6r0eAxId2oFQAoJLYfodpM27lBqpds7CxwyJiLPwDKRp7GBNv_M19B3GIEoJGSgnvNNCHbFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ32_DGYIXe7vQNzXM2utS--8iBUgPpnMU246TKhdWYhr440a09ppJZp848KvjnuS9Jd1IYrC9e-f5s6K6lQePNfxD0B3i7HKKYsxm6AU4CSFtqBT-D-j8TO0Nr6h2PqPBdFRLt3-H5eWxgkcTPou0hF7Xd9XEAu_R7VSGrxjKZLcMVCqB8bgpAzfZeq5AivV2QcykljCjDJOjy-35BgpYeprjnb-x-RIvYeUGap1eRko5atVVx-0sTATcf0Yu3to0U2DY7VM_ErnJ7YjBhD0fdn1HGcUbPMIcxJMmnmPxjVNJ7TrhDFruH8ZFGYzyRHCtl0ZmpJRO4Uh0GhJrj3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns8g0ug-VPZ-VJnDnRyhbBkuIHDqXBHzo-U0ubtIvNuzuQUAfPLstbnfOjh-MBtfAlcadY0Rd0T9NZLiegoN3t5Eptdzma5dnjG3OFAN0_HMWHE57Obb-0SJ25W6-3k0faX3iSQatxNSe-n_0QDE1OgOJpx9ejLZJVjlkFMkkYokaoQlBizKJTSJd7D3w-S0wyjL1mkdfrsfSnxIRkFG5ScAEvwAGraPZGwLJK_z3KO0zzMk76yQBuP8zrmUJWwd6QIP04DGqyZS_ju8ncPXiiyqk4t-F3-iXGbhqI9jNmIR9PRJ33Zg2SF6fUiVH6hRHI-Z9PsGBWRMZmwf3viphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK2CG_nkItVsoKDOvCywscLfcTgkMJzWu8PF-8ZK-5wVEaMoByLd37YXZib7J-z2eqzCYuv_MPhK2As8NcxjV3TuUoprUovv9247Mk9qUeIM383kV9stI72mgUYouu6-P3r2KQ0H1n2XmUG-Xy0hMzkIgf_QV1U_BD_-doTCyXcOVUrRweWV6Ff-uOiUCuV8jP_GPyk1gF0xKb8dLFGy3eptXngRr8ZohZjpiQd0iAcCRoITCzxonD1CjYfVw_TaPDLqfGbVXSLfzsm-NJw1F3Z8RfQR6XjWffwG4niRJfg1kBDbCMEo3QNvyz-dgF88wKLAQRRumZ25_XISteahnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Zf8cJLa-51ePTnJLoOKj7t7DyTwtLsGDA1Bdx5tS6NkPbEsW9E21bllD2b7BU3hm1lnuHhZ4aXXFIYJdze58hSULSEafMZvwfb0c9GCj_qbIKwwkFNqx1MksA64nQoutNfj-aJtg6Wuqtz0H0gq8UzwRU8-wS3HGxhDF28NVmfXhjTsnOf-cf_vveYd5IdvA-UHgifrL4O44oh-LL6BmIxPEqsY96LNBAHfrzK-NAGbzqzXgenj7mARfFRDGjHP9b1AhvyIqYsKxHSAroN4bloNy9ZWiWxylarzWD0eW2AP987LcU9hhjkFBZuR43BUdZC9Nye9Gb5WPlHGHljZ3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Zf8cJLa-51ePTnJLoOKj7t7DyTwtLsGDA1Bdx5tS6NkPbEsW9E21bllD2b7BU3hm1lnuHhZ4aXXFIYJdze58hSULSEafMZvwfb0c9GCj_qbIKwwkFNqx1MksA64nQoutNfj-aJtg6Wuqtz0H0gq8UzwRU8-wS3HGxhDF28NVmfXhjTsnOf-cf_vveYd5IdvA-UHgifrL4O44oh-LL6BmIxPEqsY96LNBAHfrzK-NAGbzqzXgenj7mARfFRDGjHP9b1AhvyIqYsKxHSAroN4bloNy9ZWiWxylarzWD0eW2AP987LcU9hhjkFBZuR43BUdZC9Nye9Gb5WPlHGHljZ3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJCkfkg6XNT353QKGYkr2QIvor63BcM710lO0wox4elYqb5LHYLFwqAkVQnHMDAL6_e-3gBKr_CIW0G8MCmlMtZB2Us8XoMjTY3-13V7gCTr_dntwskxxHwDBpof2GWmN9MAABAaRqQZ0obrqLDMty4S3iTrzfqt7yaEXQ3DdVT6FCRi7qWU0zBpuFs7wLi7Lu-Wx7VXNyvS2jPIeHsITk3N-AvTgm-mxlWCT9yEX80SyCVhERYr1x87d_h3L5svNYaGSiIRbt1mTSdm2PEN4gW9TpVKS6fKQLLGAmMKRi7sKRNaWjDjIEzv0IqwjIcNNl4ubMgOZrweUum2wCF6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6Pp6P_i4cipjvkPRR_ct_FwlUmiH7sF7O3QO3L4AXdtzdO-b2haalbtykrd7wSXArpfc3o9G5VUjf582Um9vjq1-4DfJV-7fkY0cXCNLE4ByCDMbm80jelkruriPYA_QLsNSUK02eRQwIIJrzoiqr0lK2F1tUODj73zlKVNCGmxQMttaTN9y-x5xDm57cO4xgzCbjt8Gbjs4dVxtycy-HW51RbolcvW6AFttwb1FKhfV3dyOGWLMIemBi7ylqBLJISTcidbSczDJ0kxTZWMEpKw4j3fft09M_QFBFo9sKWNxDyJ747IhHmNvMRBkqzWYbkd_dbzxyePc9BV-z2yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZ83qLZ5XtXhqIWEDKOm5UIit2ud9O-TytiUXunSbtdFYucdEHIICjHwYzR1LIcrKNGSRQZkKkxOlMrT02cISztcyLkZHwszYmCnv7C3WtSg_D9HNogMrej5UII2rG3WJQPjQOjO94oM8EghOQStLuG6w6owS_GkcOeP_R_S0KbirJIP2H_JNCVNl1ynawjwa4AxMwdwZPc7vDc-MEQXpLs2ikrctKWk2NBp16wlbJOY0KNmaJjYwM7JvdJcR-S7Q61RlvvoQNrkVSZODTdEmIC8PCqk7IWL9m11BnfgD2U09vGsys0-VOBq5n8NLH5CfMPyrXds9_jJVKLTNuFQEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8ZiirBQrcgk61ndsEv3kXzjFZ49fInX7Xu63cK256gky0REtUievtiEGK_S7XWBITYPEw2yghNR7Q0Y1NDx2uajMRROF_DWIuE6BkE9Qxk0x_9Cjooa7AMpy2HLKchvaRvrt-lRu27YNdkYO7oulj4HadOAuNscAFcM4S1v9hjJIEyROTs-LuLRTvHIrQZF0o18f1FnclNfpa5yu8Faa_3v2f50j5otcNKYEErhQ-hugAHNPlucemZwo3WshA51Q-Js70x7Eom21fHks1GdD8it1DZyQwZiOg0W6oCTfpBGJhfN8h207V5vPJpF3rbUSW8xBYhCJm2zu-fnR_H4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POUUJruiswjrH-Ddx00laSP2JzMW3ci4axWS9N5ImMhwfbCeiTTDwpiXecC0dPHnqPOfkrG1BqSDSv8ddDQKlgAQMCeFm6iidRpQ07OTQQeY_nLEG3JbE4ScmeE1IxS8VPFDoXotI7Z4-Juzwyp9ln1NlK3lxELu-wn2OEvVYzuacfUW5BA0_xGHTYgQ1mNw3xejepygqUrw5-uISRYkaLdU5WNIugPfslz8_emPE1nPP4fbZDUJyGLwZx4f7qU3shL1wH1S9sviEIg_g_PpMSphI2Aizd3NEZ8yPUzfsASj87lHUKPSsG86EV1mZcwlaQybYv_5h4OGEPNNpG7aRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrZnd0yvkZiWqg_AZjwnEawb3zUSKiBGh2VQbC6T6_gjvTRy48VhIZSJujPbPGo_0weG2b6-yMeSixH5wn7mYEjZP1PT71Qn7Bsie_0eGORnCHYlnff7_IljVNpRwUSgq4yR_DFFdL-NRiM3tzKZ39cEFTScmCJE9ReqyPhPGw8HdYRGVoWck42qZuGAk5FNL4qJiPFvZn9-h1dPjm-oOgvzgpqzXnOIuRYJ_bckWFI-yUgIJbZCpo3eLKgByBmze-fIv8ylKPa5gBN7RexvSw-bbl9XWOVncCtYsYs1rO7pUPY-NNj_BaXq1bvM0ckx2eo3HAObPEu4XwNxvAvZsJN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrZnd0yvkZiWqg_AZjwnEawb3zUSKiBGh2VQbC6T6_gjvTRy48VhIZSJujPbPGo_0weG2b6-yMeSixH5wn7mYEjZP1PT71Qn7Bsie_0eGORnCHYlnff7_IljVNpRwUSgq4yR_DFFdL-NRiM3tzKZ39cEFTScmCJE9ReqyPhPGw8HdYRGVoWck42qZuGAk5FNL4qJiPFvZn9-h1dPjm-oOgvzgpqzXnOIuRYJ_bckWFI-yUgIJbZCpo3eLKgByBmze-fIv8ylKPa5gBN7RexvSw-bbl9XWOVncCtYsYs1rO7pUPY-NNj_BaXq1bvM0ckx2eo3HAObPEu4XwNxvAvZsJN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Pzw7fCpGcOopmzTHcyA2L2fRm0UhLba3cfgWhkbi7kI42p-CP2vncgoBzfaFfuKUVcCAUC1q8Numd-sr6_ICJIwKDSR9oJtKj-XwLWpkr2PASuMHBbOXvs-E7cwS53FM3OmseTry_BQy8BYi0k52LKDSiAx0PLaWry_D44msQ_Uvn7N6eSvNZuExGgZfrJHDyV5hlB-WGlUEOMEgHL3lY2EClK_aiPXWrxExrTaeHYOnaQK4DDauVz1ETskmX7iqSecqrWFR6W-FF8n_V-35_TednmcKpcxGk-GCtCZRaneJ07yAUSouHPlFZ9MXZVVe0TNQp29hkdnfjQpsUZ-RHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Pzw7fCpGcOopmzTHcyA2L2fRm0UhLba3cfgWhkbi7kI42p-CP2vncgoBzfaFfuKUVcCAUC1q8Numd-sr6_ICJIwKDSR9oJtKj-XwLWpkr2PASuMHBbOXvs-E7cwS53FM3OmseTry_BQy8BYi0k52LKDSiAx0PLaWry_D44msQ_Uvn7N6eSvNZuExGgZfrJHDyV5hlB-WGlUEOMEgHL3lY2EClK_aiPXWrxExrTaeHYOnaQK4DDauVz1ETskmX7iqSecqrWFR6W-FF8n_V-35_TednmcKpcxGk-GCtCZRaneJ07yAUSouHPlFZ9MXZVVe0TNQp29hkdnfjQpsUZ-RHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPOfFJs_NDtDwSptYAFHuvr2Mq5tSO5fPNlG94yiUuR4dg8xuttNVnjk1Ml6E-2Fo6pkGJ2JlhNe0x7zbPFklOB7pKhMjdKghkACm7DPOzzB5BzlNNkIXo6fqgtateeX4no9V2SFbvDuWWJNeN6sh8ma5jaxZdBhw1Dn2iW3_fX1JXrVKKFbJpYvch1A_LIDcLSlNN1JH0pJp1wPxt_QHo2fF81J-kMQhZrKGGYEjRaCLXVY0paYrp0Nk4VgMR0jjP_0_acAoPdoWBZKER7WIHZ5nseLJAcNIbsSa-RgguuhDjAU0EESQUBUjEaSdXONUgBHfdnA8cvgr0c7YPI9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=rr_0EQP_sSsbez5BCxpbPaYRjLK0Ux2ObH_W5XK7jqIzWHaylW4pq6zTVHYCYU5gLPolzOpxzMYFwE_iWqsEupU3cBr6gtpJ02Hg0z1WWlZmI1dP4gwAwis7amvAIJQX76tsM1oRSOZIDz5tZS9eiMgNxsw3P2DoH2THpgxjgnY-EGkGuNK6FEFOyHoOavux_4guARS6e622zVrNzWhiIbqVcncrPyIp53s_L4jzQMMPLPKipbhM-5_OxHQaHHRw50adoOxKAk8zo8pT6o52Q-QR8ZH5jkTXa5dZWEnV7xCasGBoHUP6tBwfwsl0V6DeKccwthhSohKRPGtMEasEew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=rr_0EQP_sSsbez5BCxpbPaYRjLK0Ux2ObH_W5XK7jqIzWHaylW4pq6zTVHYCYU5gLPolzOpxzMYFwE_iWqsEupU3cBr6gtpJ02Hg0z1WWlZmI1dP4gwAwis7amvAIJQX76tsM1oRSOZIDz5tZS9eiMgNxsw3P2DoH2THpgxjgnY-EGkGuNK6FEFOyHoOavux_4guARS6e622zVrNzWhiIbqVcncrPyIp53s_L4jzQMMPLPKipbhM-5_OxHQaHHRw50adoOxKAk8zo8pT6o52Q-QR8ZH5jkTXa5dZWEnV7xCasGBoHUP6tBwfwsl0V6DeKccwthhSohKRPGtMEasEew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwhMkZawslFhyECeBEVuYTsFtGDtD5BejY2jTWqayMEWwcLDjKvJQlPLDwHXjNTlPu5hBR8V26ZmiIKUGmT80XIVT03Ih9dLEkMaTuZWhmrVz7Hk7dF0jGeV9fJzMUwLpP0EQgvNYBuJ3CaVZcvl0aMj1E0aQ2VCT5Vaz2IqJsqpL98sUNRxfW9lF4FYptwLOkWS2Rcfq1K8Y5pCKwbT3uYhZHD2TBJ7pB_YK3bxR8DE5ZygvS_tTTn5P5P458TZcp2dWX7s0mzvgoA68YeeTQSkzZRpr_ZyVizTIbXhcP_MokQHdgzRfE6V-9PKtU9oN8udqiSCVCEn2vuebagtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2dOL7Tu7-WABK3WEytfCmyWXLgdKwto_BD7_3qwP4z20P8ICvfzJ0ktD11ByRufrkE0UGp1jt47cuqJWpJ7WtnXr_peTK0iRutBI6OG1-oWfmudnKYr2VxxQvjTSDMRdpzJrEWiBeIrLu6hJoS5w911v1FiCp11waHLqZiQaOMrjghf18iM3sFqCMXnoEaGw771-tPBNAly8RcGOoownx9nmFLKlIkykmSCwNHDl2Y-_IAmmwGHDOyzqwrnZpMiA_SE6IfYQgF_A9SvDieetylkHL7bu5DlhhqGyld75GKY2n3SxqJY1mgjNLteYUsOoEaZklGy5Ld3gOf9ko57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
