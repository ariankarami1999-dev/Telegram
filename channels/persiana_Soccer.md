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
<img src="https://cdn4.telesco.pe/file/peoXE9vanxvysLb0_stXpi1BlvuRyLxwVF5e7TR_N3vGE1ytQtS3Exn0n58MdQa3yb4HRbjdO2Ts_aH51m7bdHrB6oZG5ZMyxnR3H3EgHK7guApVMjeQRrZFEmJ2f_1R1H5U0fKQlUHm62WTq4PiNKlXfL271Tn9ZzSKIe6IBztl75_LaHFIpEa6dPA57UPuz6yCzaRhsQBJMabDBn15lxVSjwmTVu8Xy573AhqlYr3qhoUimX7_UPIzcQ2Y1U91YLScDXOuf3vq2OsRAWFcNhw52CAjRytfL-TC5SKesMN1SQRML-YhNdWc-jS8oh5fQ11uf7AV4Upo-sYzT-0BRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 444K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKG35SrmdICwSLgiUMbkrljNtOzJT9vjlklxOP8xAw7HzKvLnWa59ptTMUq-kVU2ZfIiTCY1nELAtloUBpMTd5t5erJEzBlwrVJ0o2MJr5q-QSnsE3pBJ4DTt4SYjsNadIrHiqfb8d98ebtmw3ziC-mjXTOdbtaldhtniA2wuZUoxGIQI2CUqEppkbk2WNdu3_HMRXmO_JefavPiFOp2pQ_Mw_1Odiai8F8h7JF29eJ60cy8hD9G9u-CvwJ-2HijscX0GnTpfQaRuA3hzoP1uUycrlTAO8Q1NmAQr8XsxCU_P7O8YXUueHxHZFViJZG2fsfvn6LjOYZOgiHXtMhyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_-JrhjHNh1vE7_gW156N1EspejFr5k6RDcAG-OECnxQdq0cp3cjegnFDlAS-XI4kcHbYfJKS8bpn0uPhlTrVfwaPQpfXpCleUvk6Wap2YP_6KpSgunjjbOqvx6bO_J3amZCQr6PmI0OsedB-pGJOW00Ca27rbEZCaH6cCmUVJ2JRnkCKS1hfOvu31ccopl9vD35zQpiI2lh4ZDzF19pdMex5JlmQvI1bg4lfxjsD2NfIja-ODDytmYby4FjYkHy5t94vf_3kyotSjEa2EqG8cECUQEKyKQSnqtzUJleJRHRxNgDoF30o1kVr6SQQIamKW0_IMO-iepLllNXnu1i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu0B7qIuSfILTXBQogkfMRwZ39lymYWHMIEb-Gs-J96G2fW1y_QKP3D6_C10cYGBcsK70q4AEnVhwZ21HKhDyhr3xOEpSrZ9-okgcKz3U54tRox5jpFLsKauUihOEkiTOQY8rRZc663QH3EopQfjX_boMvtuFswSz2FJHd5_fAb-nWGnz1YmPRaP5ZswejTETDJVmFzUVnJJ-OUClenSvrTRtAjmvFUEIELeQQH01N1GxB-TZbazC4A3YXKkI4UUNQyvJpsILlelqKs5l5o-lpLqV5V7I7eV3cZMW5m45HtRHeeRFwo-aI_5xhhjkseYTxnnm4X16CEg4DVGVhikhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ppwF4MkgaKtFjo1r9nY8gVylUYmRwqzLVc_h-zvKLXoCfGRGfhwe2KmcIdgELQCLSt2MtxIt3o0wnWiRUlMdhbrbJTy0WryqyRigfuwzvhKT1AJlr0sAozmGZnvjw5Cg87EZb4FY3ZyrPnRusr7R_uLbGqrI776gmfHrGcPt3XfQ9QjnjTaz4BR5qQRxvrAaLSMGi7Vq-VxJeAH25ZSXdpSrcGPDZ5Zb8l09AVxPf1Zm0xNUatlY_BEK3M50cp0zx2aajpZ2Ty5IZ7sYHVckwTsuL_RoH7XfHVojdIZGI96rLdrBL6xp3Dg7oF5jk_pjCOhwvWw-4D5gv-ZIMyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshsGo2JGDTWH_J6Ch6kaVLjCoJUjsKHSC6U611QGw5fEidHv02uHmM67TV_LuiGqlzvqVEtXAdobM5-UrlyjRGwVNHdP3oiqBdKYowcFewxYo3ouHOePBsLBgWDvWPSbmQng2K76ectYl_W_Y6-GwHGQhOuRSV7K8bnCoPUdA-9jwNTzpUWDb0pnDGpwpMYFU45uMPatw2goL6kxTwWYYVDebD3h1MZ3HkRhMu045Lu1oWEgyve44a1K1powMgFEvmfv_mWv8YYZcSLn3ylUqcdIACWFaQA8xcCJXGlq2cq9fRsSy-mb_LcL3JQzR8qZLCEnOkG7lyFbdu8CrjNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCtDP6Wgsu1tvFm3e7skmxg_WwVTrF3cMLZ3UHDEUBmwCbb_pL-4bTY2mQXsBOKlKot8Sl46_NcXdw9qyaIaQTpYQRDU6uY6_e4zsORRa2H0GIUt0Ru8QeuRX1p5flZ1cSenaTrNKVgtZ0wfvkb9dSN_dp4QxOlfDlk1aSWgLGAjQ4Jp6NMe1SInDDlYL15ShT-kMcoukNM2Q7VbF1D5OZBPNQFt77dNKUCw-qZZtr8wwY4nhNmpuLLwiWy2LrmYpzUENn6nvSvk1wx0T1jYlwixtu27P4m-YEUpDsRdf_d68Upl7BO6bmyBsDsMoS-qCaIu6pwnOUNdaVT3Mvo8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34X4MzV2B_I-olf9lVisXADiU79WmSSFWdWu6BvkQQsrdfh50Bji1g-4Lj8oV-lNwsyvX6PhqICb7GuqfjLnKsYQi43_ysJqufCEWDVVUFhcETuquAePYN1K-D7R81JAzwBub0I0E8yJJaIM9N80vtX2gvjE-Vl_JB9qQJ9Sw8yfoeujkvl0vupZjBINfrFPBYV2yIK7kU_YjEjzST2lDH5hAji5G4MkcP43WyRVjKTkiGZBtv7VOHP3BXlpfEMmJuauvwkI7uLSFtI87P6z7tuzV0S7tcGlEu20kcqTLnizIlz8JczpYA4hr6cNG7Rqoc4yk1HstIrvKh9JJdhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQD0aBEcrI-1gKNS-IkrrmnsZFNl9WGpSQqxWoS1kLRCsWkqjgTTk-1U7wCsFpWixoSCMZOPqCvzqwZEBXZ4_IBJ3x0l1WCSICDzHZwuptm3jHsLUqKUQKxr-E_z4ZyVH8_pSWkXtV2nbwB3vllts_qWQxKtQ7stRI88kqX0xEAo4EWNG_zXUmWTynqtLBxH0Tuic9obqo5kCJATX262r4Op24fBDPnBuecgioyloiAX5wZizVcTtlPZnLhjbrO1SY4-1p6y_f0U0Feo7gV7zey3oSaS4YA4Q_0BPhM70xLPZdx34886Utmz-YdsTWmMdvVU8VZMdzH0RIxeUdPo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
فرم Vip امشب با
ضریب 2.
0 بصورت رایگان قرار گرفت, برای مشاهده بقیه فرم ها وارد لینک زیر بشو
👇
https://t.me/+laf8I3RIuq42MDk8
💵
فوتبال های اروپا شروع شدن و هروز فرم های ضریب بالا وین میکنیم
میگی نه؟ فقط یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و با گوشی تو دستت سود کنی این چنلو گم نکن
⬇️
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq00gD8DfgBuf3-Yy4i1hP27Q10H8EC9XmnlXcB9kvkapYLlt7N81dU1lhmcQrhnREwVLHukBIpa9BIXivy0xaDnGPF4pycmrh9HzDa_ovZS0kqpvc9UIUEVUSV6sgSnoHdeAQbgdJjz6dA9wt3hxqSuPkQI_b4p6QS6Ha1e4pR6rkIYC4qEitLxH_5cqInRspISwYrCTivLpTphudUTl17AEFde41RItqY7LgMJOtwI5GPKB3fEbb1ez5ILRP_KtVCg1V6ENV-bxskbuh3JrFbNM81kd-uugYCxw8twQ_9p9GWA5bAjMwNupUb4cp9xz3lHuFMbBN-iYxqmDqsTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQV3rdXksS8gAPous77XHNtlEY_k7xuID13ewmGJ7rTyVlY-Q2lqH51UMKUwXs5imU7ltxWQQKXTkCW7noKpZk3hMoZkZiJj4jem4AWUmGYb4298JHowDp7P3akj4Jjy8BMaeSax83OWnSGHtDa2kgI5k8uG_q-JAFE2Q2BE_OBdyP-jMtGeMDFbROVtuQMFh57gdW3V8Ti5Osys14-JyCyRb15_CrhmwlgtDerixbbNy87QEnSjuuqdg6bCnnKA4PK4yMDYGPXtJGYR1_jflpA_0KsXTrAasRfka-5f44_lt83JoEnTsZmmvijv4nV-I0TPgx3NVXZPF7B62epXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYNjHkdGJRtHMAWKxjZ_Ur3S-VDj0B5dwpc5yVDslNWSN5J9E7Yt_euXFM6rdSLRtyGEroN26No6typx28bND-FzNdM7gzRPUq1AZD7o5zR9UJsMVYWHw7tVeBCR2ST1MWUDuwwucuXoUrkGLNZ-G-S3dvUCkV3twAi1UtT2tnlld6BBrGJ2has3vmm6DTFDYj2jHHhhcXilRsLKQ3JP62Ai271Cpp6yYhapeKmvxwJYjd0PxLIKOY7spG8g7JCVkWfQ7XV3FVYI6oAAntp-XkC2ds6DJUnYfeEIFGxSmnSjqTwZgpd7efeGC7vllP_FVrkjMmEvY7jCQjZoQJ2aOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxFVB4vIaP1pggD2JtmRIBrxplV_LsDrIUi44_I7jdO2V1K3gAvZiVV_lS-gtesMV-gLsdmZGmOeP9TshGE_Nq5PxyakMNaZxqf4IjzW_NxvA9TuNRcRYC-ah2O3_6UUDw3WOam8DfIg3-L7LFLqkXHrTxyrklhmFJ4CUxBpU6KuYRcpwT9TntT1Kx0kgv6r6i6qUnoh2dKoan7KAEg_vyMVaq1RNriRoIQHyYpvNNNNmB8Ck1ScM-u4jqRMcjSM7t9ggWwaBxrnCsqYNT6x-D4bRw0zKBlRjHQHRR64B2nD63gHgkUhwDddUFm__18v7QCoxyRNRQZGRIlSmB5LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVoNXAh7QIYC9wciXON4eQW1N56uG7tuDMTt1MvKZlqyQ6_Fevoi_91QCpwfih-4QCL7KD7AW4Ms5n3ZEPyfXzjUdw496QwySKqDhe7EZVy1xolP5TaAgUxXz7v99WT3EkcZ8cYjPsPdOisM02wi46OhWjh7Y14O2YvIPLYkKDeGdjB3cRM0xYZWhUG8JzsEtucFUG0zYZrZV0Ujq-Av-mYVY7gNFvDqlc3-nUDXiyWXP5gdbg2-bph7j9oH2uJ-z3DheetylH6fZGosRXFLmgdm44eQINjykzQa0hksLzxacL1D9asyxzI38CNygCLbexjG3WiKxvl0KvV8A14iUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krncJDph2zQU3402ZGIFYg9av82j6DIx5i3sOnQM5-Z4zrXpX7j2ffOT3uqHNVgE02rONSWaUsh3ithcaAwyvSVMCsup7fbkTTvQ2HsamYmdvUVUuPJVDgoCun3dPky82hGxDkrQXldRtAQViFynFKIWBLk0qvc_Ocn9cWYRLbAHXjJJv5s_K94Ckc5E04NPhsetH47kh2r_rZxJv_uY1Fx3SUL6pka8fnZsIydwQxnZV3sQB1fHn1a-jmuDB32mcyVXUkEIwDq4XFEV8EZKOWOndseTsgYbINM7ic4MlqyhSZ-C_l9CgFxjSffatQCfO-jQ5AHohKDWejtdampFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs35xb2OKsvMFPGuYvM0S7uYiM_3qzWWzlBFX05xIMqNSK-MrAsmpn50TV9H5Y2Siz965C6VQ9uAQLe2q0iAlyb7MjdQeAn2o4fQVnztEr2uXrac7-Ljt-hCyuvpilkTvbULloi8fzCFYZHkv3SQI7FOIFlLUci1puKTSgq9HX1Af9Yl-1zWqUs6t5VVgaQWZ2KQYmR5LSlAZZPKgJJ3K6I7W-tm3_b8D7UwiOvJStGnGtgOpizZci9M9fSEoJhTHXfF-V4HpRjasTuelmdg0Tv25HXmXka0NeoYuG1V3L5tHLK3GiD-CMsSnNVsmUPL-lHo-SrsLX2jyJpj96FcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFNY816gG9GwlA4koRwSRO3wl1l6rVoUqNqDtnT5v5fET_CgoS8fWfukE04WcKBszrJFKvur9i7QFuaXCPa_bTlAFgt3RHW0XSxbaJlyq00SM3MDL5pb7GfUpQ9syuuu_wyTEnWBs11-IUwy_FHRRsZUZE24oODPsS8rN14_GDrhHT7E1AXXS1yE233GEIDQUtPCa0LMbnfxlbrpD3VSBWDBla-2qlnKfv0J6NXk4_yu9OF4xV9MALE82yjr50VjzXE5tibOdH0jwlJtMSisObEmHKp2o7mQRXYOqNygIgPfSLIimcSdYzlzKqdgFV8T5B3fGplJehaAunaQ6Tx8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIjWO6nnW0odS0FHaouc5_06G8t9Jyn2ctvKkpJk-WQuCpS3i7TFWXyuQBJI16VqJWz5jJI7fcs37yLh2-OBCjj52VhMim5ZxXtdRnMZXSyk7_jYU3eZ2_Hor3KvE12CFhmbZuC9QCkIu68Qr4XejKLSBFV9wq1yc2lpq0q_oN0TJ6WceYjl7lb4P1lQfKZGNTGGrsrXe0eMF0sdHrshz-Q1K4gepBjFkS0lT5o3Il4bWEikfTxT0mKEJnmGzPlh8aBb_jCVMp9kB8Pb3j7cwk7XyRFOOmQJf3F2__hAKkcyn0KpGQZDXXWOLGkMuvju_OTV6G6bGtuE8amSAgJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnvjytxZ8GFREhe0-l9mJTAM_MNWpzCi-V647q2B50YsFv8_7v7KfG-heS-y1EVmpAnwnlBEuJYwmcOTLIdsqkKpsgkZrreZPiJ61HTz3A8-tlACZJq0DYu8ryEi67urr01XWHOve2cV63P3-sMTStBuSRVrdhCTNsJ9lBlZ0b1HGzmBiJwE6fW0j10yrRIy8joHLncEt_iYPKsGqUwF-zw264rwOyEyzJQzCMWdgYSuYkswqemiXDMzNdnqkQNaIlQh10cCJ4jiRI5gXxenWMWH5sedM_qZ1TxlA0jHhJDPT8plDN5O0u78NhFUqh0BRwn0XRfZp6G-PbpW1XsT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8PxtsqpRS_dR7vuX6E_B23qVM6Y0VYUiEmV2YUhXQZFEJ8SxOPT9DYRIznpni-OEuzV-7YG_ZvS1bmlHqbST5lxTVBVUN7T76b8mcvfeC0qihOrTEuoyoDqTPo-WxUMsOlybfLyXLycXaObsYl7fxoL0xd181sjfN6POkyR8rhUC7aZbVeq3f07HOgjJt9L47iBfjp0MbEURIbK6i4Q8UbuufJTlPwVdOktCoFpEtgyhu7MXS4jxJuzd23geP55C0EhZb-IXItJzC9F7Ysj_vucyMTMds-Ms1Z54ik_rz_J6gpoFMH7u8GD9b83A9acnD1Meeyt3-alT8XfvxzvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRpZ-ur5LnOz18IByL_VbDmnnuRhYPad0kqbSCC2RYJH3PMF9iD3Q8Afh0Mcc1jb7Wj0VQ9cVCYS-FE38SITjrHvMP0XLJgkFxAM14UYHdJGx3GZ3jJGlSVtyXHwMjl_ggSLU4qWs0XwzOOpYOPeLp9aLJg9k23HyrL9RquUlDiYgCjc5myolbUNGsmUsDLj2VdjAufMYoiLKo8_LP_SXmidN46PQ4Ih-I1vRf4BhSMjrcPwu_E63Mo0F0P_ln36_WxJGi4IltILJaR2qx9T26IpU-ywL7ELwxiiIPu1GAjxsvANPZsuXVHyuOlL_UCURwrE2Y8LHYPeKJWG_Rpuxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C53bDhRV_1G0eZDsxSU43AxMYTt-zkrePN4a2Qo3L3aP-m7BQKuMGHjApy0P3GxDm3eWiZTCnTu7S37thmnCbKkrax4wZOvNrc87Y5-cmz42CcWvg8NrXt_Z_-A9dgDEroFUMj7cHqiNNXlqDtPLVGxn92oBHlgJ393JF0SXbQ20RsNIhLLcEl74VjNFOjD0XTaHnI-jBjN1QKVERYhmSI04ZNJOmD1GsaR_ZqOxz3cFHP3BNaetwIhOeinfjlof6oEf8gf5MPILsjG8s_FaXotzVgQi1ZeYJn463Epk6850WAwX7HLufyGMliQfgxkVCb998no4QnPIDx8wEzKkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKB16l8LtLenIQfSxpmQvtrzHyL59LPleTC1h_yVuXo1jdlN3wGqhasdSzBZ4DAvjRy40F3rxjI-B9cISEcAQu_KlnGRBloGlKcMEv6tA7H5HMNKDLUKJcB4LoKOxVQI_jxZTZWS2Mw0MJnvNGQXf_X26E2X8BhbkfZrPgm0WMNVT23S5_vu4K97kTGoRKmhLqsI_LsgBBqTOsVRqVds6RA5uCwEgoJFFqFepDUMGk3LvTRG4Mg5RZxx7k2IS2LaBGHtWJiqc8A9Jm8XE-dOFrrJ8PKIT5HT1bXd7GJ4JuhC0SGAfKZI-QSNUq5hEc3C-IhhbvyWFtBsnNppbagEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5d8oqfWu-ixP-vhsNRSSR0jJo1xG3ZGDST7EJ7s4wLDqPTZPZe0EdaE9xkMFXhFDs3b7wk3Jdo7oq1Aft20oKo46b_65Iq_r4pa_oShMtR-D7LTfxu6mbohEYGSB1nIDwFdYi2MTqtuVCelzNq-ehi8PRKraSBfWL6I8yaUzEPNzo-7Nn2VASVV-v8O1EuvcR9SKD8VbecxsqhgO0dGx-WEJgrInOAxkffQyJqb61dX_AqktiefvzaFImDMBif2sif2O_MZOknIsso6NBABmQkgUTsAjgF3ixiWYn_gt0ZeJRBZz23FfOyDnfi5Ri3pbCUBaJ9rOo3E94cPpqrCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR0gPiP027PM5-3tmKaE54fw20t2WbIKLvIJPNXyfARfKJb8tf0peyqUipve2CW2wOn4EJeW264TuxvGvd6LeYXaOQVxb_c7hwujPbr456BbgqnQcf-A39dL1yCsIW7fRh-qXPhXRFyYCEp4T2nagH8WOSPwGSjczfNWOlLKL0hhX-r9K5aVhYckEL8Xx57rvF-hkOqwq8zFQOXmqkirk9ZFBVfF8kOoDbmrIPhc_R_68D8PwtNXj_MQ-xfBMO5njhs0uyo6vTR5bDWSLqdUDyZpFo8BEIeo0VqvltKxqx-iGB7hqavdFothG0-6jC0elykQtQ8DNzFf650-7nTBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای بین دومجری زن‌ومرد تلویزیون روی آنتن زنده: دفعه آخرت باشه که اینجوری صحبت میکنی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30539" target="_blank">📅 12:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U55gWnKBg2vrdwJkFg5WQB5w7g6iCr4hbapusRv5SXjyY-pNPtCHExgRBsFcKx8l0iwxvkKCgw24LAUTHYvcqLdGZEdKujuuptSj1_Fu-sqOK4KHYtYM7_jasMZbSmMU7kMv5KwAABfWgWh1-32xRo4PehgWnzOQzHBe3bfv1vWlcx7xXZ1O-bjG_-dKCmMwYWxWVrkdoeeC18cgqZLQDceZ_h4Uxnzp_WrALhHpmI-0sWhZX6zwm-8-bmYe-en9g7e-6c4EAIhzLP52rf1mn8pFFY2ALwNM8O6OU_5dcMFb6crMsoYfC9LRtl8MZiPUfds6j5I9jhIdDEBlR7SDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30538" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU6J7Sm612wVK7mqa9sfcDGDGZhYhfvZg0X2lCOgpicozCfKA_Xvbpt8YDSlohefM4HpVG9wlH6twX62VlZil1hmMenZ5PfO85QWCo2qsTpST6X9JodphYe02XiFoIKu2W48I4tvsPUtbAmCKgPkszuhM2A8DE4Gl7jd2mGHT6QndJRG1IOkOrM70KSBBL7cB1g6pmowk3YetrGikIhHgMLMDhPPMyQT36uaIW6_Bne4LhzsrDBnjYQWhoT8i5zlPKHspqpdsecd0QiEHXnf0bZ9zKvxBp6wfkKFCnQYxBuGdnYKT6nCuGJ2vI4dt3tHVxOOeZnsPrTggzVCopkerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حاشیه دیدار دوستانه امروز؛ کنعانی زادگان و ابوالفضل جلالی دو بازیکن اصلی پرسپولیس دچار مصدومیت‌شدند و اززمین مسابقه تعویض شد. هنوز میزان مصدومیت و دوری این دو از میادین مشخص نیست. فردا بعد از MRI مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30537" target="_blank">📅 12:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30536" target="_blank">📅 12:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6zhj9JnKE4kjhz0Dy4A9Z2ugvdzPm2PSdbC0hroBOoyI4PQFXGcnMqEZETaZzEYosAlcO71glcbVlIN9essXI8NV1h29bDAiCQZnRlpkcc7TFeme3cuVGlZqScT6AU6C9BK3qwWmarJo3lCXnqECdKPuN6fZljXObMFV_V5leVRQaHSjrFtqX6-XwaommHrn-DCYFR4gGvIFDDZm549BmVpNeKUj7-zvn1SwYRxLyeQFhnhD8VJl1VjBTok2yNRBbssSI0njgHnhuszk59zruxKASzEXdJSQlVn2FX4sI-zdj2ymfLl652j5OEO0ofXNZ_xpqH3X_LmZU7ZX1-SJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
درصورتیکه سهراب بختیاری زاده تاییدیه رو به‌مدیریت باشگاه استقلال بدهد؛ سید مجید حسینی مدافع میانی 29 ساله تیم ملی با عقد قرار دادی سه ساله به جمع آبی پوشان پایتخت باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30535" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCn0qokIowxW8fVRkgXo_0gMWZAI_cgYLnuIBT5C0dMFXW1t0xnZNJvduJgDELUFd6b8u-VEwBlFhbT7E9RT3wT3mqyM6uxCeCUfGUUSMeF9w7jjG70mY7eGDpm8OyxLUUJFySXl9V8VUbbAlApSpZxMLr5KYditkbryMUMACkvfGGTrX8vWat7Z6C9Jrgf3B2iptx2GyZQkUYPLH7ALcRR4gY-a646MUIclVtnh4FQtEzaX0cidR-y_r5405tRsTuf7nJlfC7N7VSQnVxl6-y8nKefPvxd1dcBjgeILIhHwEhiOXkYsjwsFYmGDbh9sfTK_MdFHF03FDoGfzxinKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو بازیکن تیم فوتبال پلی استیشن ایران که مدال طلای بازی‌های آسیایی روکسب کردند به‌ عنوان سرباز قهرمان از رفتن به خدمت سربازی کامل معاف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30534" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdZwbntPlEQFJr60Bzzlvx1TFtRSATl2IkWzJw0QW21p7DhZ6VJt_NteGIN2hJtANiHSOIHxtnPlS57__Hyal5AuqLDJAyyUJfSMZlSwwkl4_WQz4P0pqcs9SsJHl4oDYHnMojkYa3UukOoODIFueBYT_k9dOFySuaVv2jgBSN1bGy4pJAL8Cx_TBK0MJohfi4pg5uF0nw6A5GnNj_ypkkBr0zuewbB8fEz3etQNsJOyP4smSJD8rSfczWrOL-NuOi3RWdOOvtmfAJ-UXkjhmNoxxrMEuFh75lxF1-Hv4MRRuBofVRR1ueDnaUW3DnAS20AePdNIUOpMcIzsurZG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30533" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIDJm4iE7rmeJBx_vvOfIoNaaRfWCJo-mysxp02vkBIfi5Qw1uaFFZ0l0P7IR8J3XWDAr_V5_pvaHiqAeYf6YBorysxJRtd8NyPcyHYQvbXh4vylbYaY_aeJJqTDubx0f78AznnWG6Lw_n3c-5-11jrByLH2OOvIWsUpnUzhQV_6ThaagCYdAFcECDYzIzEwGmmGOpShanl2mqGglBAkETY-oY-gFPoWPJjqfB83EGV2cT9egZJ5esfY4x5XIsw857gcNUhx60PtNK1MCYFiJlpOfZr3KQB7xZo6VJqMKxcdFLYjiACt5vK-Doi4MXLKNjRNnYwvLB2y3wkp7fDgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os_TQkfStR-grFn_xguWlyWZf_4hQZVUg56lRtls9Qw3alc48iJ9O0JI_By8AdHqyOtKaCFWDxVRQ88qjPH7oqKqd7dS60uq83HKG4xv_Yam_aAsOOKCkFKn7cPR1Hey6qPjQNAAFvUqCinb0i_QngiN3E31nOz4HCel6IrrD41o-4FsqMF2G19Cp1G0NGZ099oYy0lB-LEli8l4TxXcnsPrQAQNBfDZsQdWFHJIBG4yhrwYR1MMshiyN0iKtz5a3rPwD6hOFuKfVZ3laIFaud28_65ek1aCv5DynZLl5T-NxLZIr1_BMGMa4hc7B3JCVg91mS2t3ACV0WUaOe58ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30530" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30530" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmznZY5iiRTj90u1mGZXxGY4AWOEa4xAQbBPAyc8ttL7L40wIkqfMK6n1-WOBjqrUHUsD1vGyJkd8x7AdL5VkL1xup5ezwXmBmc-U0OwLQgAXNlpYpf7KBlRQE-bJVrO16bzT5kAGSuQodkHjkG7-5WMU6C_fa8j5bB7v7nh6IVNcjzz_keywJhym6FviyI8aJl9I9COf46obEwEiWbWieMQV754ChNdQKdVzNXf8yxnmpr-YrMSp_vea-OVkDyNvUR2OzLM4ygE8_hUUtMtC6Cdvnx--JsTifrsc83FFJjnGWPAgUUsmxiS5WFltXlKskLIx6GKrCFx8lbaN2-viQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یوووچرپرمیوم ووچر ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30529" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYPMGGlYOBFaaU8_ZzidyrWCft-jWRviFvj1Y-6WzvHCAvDPYeorAT-8XcD-a3Mdq0zG3wp0diZYb7A-vKRqJ_Ie07okYdYJdKpT1xC2hMlIqGwe-ipnBg-8ReF-xrMTB12Q8vchYP5UgCbKd5jq9qE_2sTATrIBf_xELTbtvpmYAqrkajTRWwXiarzRlPg7P6O-Ykpj8gbV1gsgE6TciACQXxj2CG_zQ9YdhZ5fk441rBXW9kUzRR2SkThtbfZR3738Ttf0CfkrUDFizJZeBcRfLxczGx87EkrjgXLvt6OSuDYIHvsgQzyXbFxfcV5XPUfBFn7LV0JRBj-5p_QmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifkhEDkexTeFRgOagTFF890cfO37qlPcmfhJGn-WmV8qO3nBiwB39i-8wqksClMdWP7RE1EZsTP4eEEUUV811q7yM67CXhUdbhKrJKqIjjR8LRQ-mM9apgg7gPd7e3J1CDVFBYISRFOgL76UqhA0R6Qxl5fysSBgZuFQcS7be3cwYmhWJyrB4wUXdIMN5PHWQIgF5B8QlZWpOWdznE0l2f2WvqAJ0CbI2aKCn0e74SyQTuMFiyk86w4eMzQt5KT3Kg0AY1waLLyZbjUY2QZ9UtgiAmfu-D1GWwx28tGNmJqbRC_RxTrv-Xosvb8IttJwfRSOSr9NSdaNT9TqJLvEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_3Qh-rxZJz0vdR9dWXaKwZCTqDuYZtWa9aUNgGdlOQ8qXeRTJIblI40_GNwyGE4bnq_2CpOwpE75xlqyn7rTBkRlKl_RW4xwKzXtdox_0gAF2HazCe5wB15TR1Ec30MLyJdDzD43Sc8WMVbLOPicaDWN16_RIv9du4itMOmIKyxWc9TCV4y3mziEjuqI2ckfvEx8jzK58S5ceXDaXzxM3oq8jQSEsNeqgScXozvs3RbkeqDPrIIppgGjEnwaMuik7ndtCTRqjDtHtFUvCPuilnpfU5Jxi3GxF2EEEckaQO5eFaiv6BgofleAfK8VlyL5BMsWOfpkKGyWzDjkF4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAtiXx-twKRGBWc8XHi4iuLlFfbXw_dDscS1rvhyqFwRHgcbE0SFKCZHr8HUMSJM9oK3jwFoZMAJ2im11-iwaXCCDqqpYs2zY7znUKJe9XMnVJP2soLnY1SrzROkJSphLIymy3GWCIwny8C9eoKMC635oQq-a1ijn2tWZY-o8zQll9ZFjc_BAnN45VbmWtFmgvAuZclg_je9dUsJrLc0yQ9fmUrSx8a8nDqlOFzOafD_VzUmA8EP3OlsXDf8yF6Vs-ANCoMuBoLzoPzPQEOPJFDlDYEXkNvFJTKDCSn4SmfAsTMJXg3F6wSUZKIwAQ5yr6iuid5J7n27dU9MJyheGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDD4pAtpUgNx-UVXplRwMSMe85IdzYFt7vhpEbjIg7gRpox9vLHSgmT28Vt2Y7t8od4J-Af-kt128-rCLaTyO1cucK6loC7kCHd2ffQ2JU9tYoo6C0SY4W3p0rIVlnyH6YQovS4Y02NPCbdmYFykIAEOJ8Kiix6gmZfc0MlB5HsPLndRxwBHtepI0HYjH5fxkIJ-YWIx3XqQhiqa7PoVB9pN-OpK6Byjvwrc_K2Vg2YyJECL852xs7z9YDjxTAcPW7pGDkzvxXzStne2wHvGOxFqTRELRSKpNdHahk1IRNNCwxOML4zhWI5LsTkr3OQnzI1J6-GaKmAJjc2xPOGSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPVRNmTH6brIPYKPOg70xGaaMJwsUDfJaGV7yWCjMOT8bCitPlwh7plnk-2NFCaUSCIgR3w-DrrPAGJola8R01XCrgU7Q8QJMZLovYYnzna8iLL-qpPoeStpUm5tW-hiPvC7f8aiWT6kiKxoSDGh0OaYBtTvQ4xJhgw247wXpf2SbaTWYOMXsnYJXbpTkRIHSLJoOcu3f_skVuc7-z_RCxkQI9rqBXhjUW8ClDGvYX0nnHAL5Nc_M6ryVt1o8JjglhZnGmIWud999ndqqlBIT2zszXE_s-lgRyzDfmGbMsbMNcb40IQJcScN5RCpHK0Cy8nzrljZroIbwr5UAn3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ZfW52Es0Vyez2n99DqIt_PfZDpzNVAoVOywUg7yG0oYYti2Eu3yMx_xObFJzmaE5D8M5eLOfm1B44CVfmylkW_d_UmtWM9gCUM6QT3O39oVB3UGscsM6r51sfrl99lW5BUsLEKwm6eJCZ_AcG_DAeqLDEbYONdkfqjLp0UsLQZ0VbN-Bq0L6ZoHTfhiBdrn5Ltyl41UFAdVUjTX4fzufER6xPiBEBroqasD_7JCPH9xuQ28IJiIp55QtAqPAZ2pRzAudJmEtRH15f5TVuyJCd149iig2EOZmipZAj21F2-73LXPAJrnEPALlQl5iEHov74wyuw9rEcr7LTd0Hh9z0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ZfW52Es0Vyez2n99DqIt_PfZDpzNVAoVOywUg7yG0oYYti2Eu3yMx_xObFJzmaE5D8M5eLOfm1B44CVfmylkW_d_UmtWM9gCUM6QT3O39oVB3UGscsM6r51sfrl99lW5BUsLEKwm6eJCZ_AcG_DAeqLDEbYONdkfqjLp0UsLQZ0VbN-Bq0L6ZoHTfhiBdrn5Ltyl41UFAdVUjTX4fzufER6xPiBEBroqasD_7JCPH9xuQ28IJiIp55QtAqPAZ2pRzAudJmEtRH15f5TVuyJCd149iig2EOZmipZAj21F2-73LXPAJrnEPALlQl5iEHov74wyuw9rEcr7LTd0Hh9z0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5NfZeaNRNaMgEJd5nCKQFMfFei-wgpHwUxU4lhGvrqVLL5LlGyMebzuTY5odBy72cscFaPgvj8G1YFmRORxLlVANzXk2i3MswnbtyCcwkTvs9rvXhkhxqtmi1VkooEg6SVbgB0GJ8Ch0krs3nZM6Urmtqbjp0aVsHgwwKrPPIMK9qbZSJFTwX0ZqmBJmvC2DwFUZkggAtnXqggVecfMZNBQaX0AzNQydkKSjNVQ24G4NSZsd4IVdKiemslmjxtUvYNwt5ntnGlxDccneWXQ7aqpSw3MGEam5WTNCZPvnhF8-1ksOPja6d6Ofo2iOgsHTBYEVaLTsiVirIBb9241Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6XWJUtxJ2TFfmjoCQ2-14xkuD7OkIH8fB3BiXmJLCGLdZBvPJQuwFERSWDs1zEUyE-dsqF1Wtty0nOTRntsatrJLffS4o5k9SU9nBXR_NvRMYh2aMn8USvEk87cDLJdNEtIaccmijT7QRXRhU9DMGMaO2lp8LT4Xw6psLCNy82m9nj9Lqh17sIBg2AuaU7ChDBrU75T2tehhY7TcchXggl6qC8oXGEbQAGkke18cX6Ta9M0DpVBijgVa4XHNmEMX5qaULS-ewOdr3pyOBrkG9vrYJbWiziHnpI2594CaU54ngdGo-kZu6qykBmRZ5qLBiYAWjAqt8OrGBlyUVm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVSCnzPtMfwxXPcBOtqS5g5SCLo8GS3jYvZpXn2tuChj18IBs9dXMev8CPRMnR5UD5Bv8fFvG9kQqiO7qOopXuNnwSZNK8NOBltgbKtketLe1qlZinRR6y0zN8BQ06zPI7wuQ4j8gFfsiNk6SjEmrsM2V1IMqnUmhuBPmx5R9WEzfWZKMjg4elwKTKpe69sWmxuwfxV_nNwaNjfpBj39gp8KMW2B1BXQI4gNQag23QUXDncJIaEnJ0PmxP7UM8MYHDzEEFXeCdMEX88lIZUVtmYhbgsj7NA0G7dR7jCZ09WrRc3pa7PNQnR9VArTKju1XnYKCyx2u5c1-TkLvIXkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30514" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amwIAfFXcrtp6M1PYz2xDqgoJv1AVmDr4MsWPWBD4Kaqh3Ld_uO8kTLc_nrZYD03HT55pUYHUCKImoBKnk_yx0aieljBcRz6t1nJ5KvjsEJQkR32xSSFsxJ_NddRynU2DbEQUbQB4UYtHBtBnrgTsHk-gEX0N7MM5e2NifdQFcKFjvUd0UUKSJFhfdAra_5Lk1dH-v-vBxJb1NDpeFVc_sxa2jTlD1cQGiD-KbtxTG3C1AYqnUuD9KfwEJFwDCJQ55sYpapD9Qg91QTK7bl26im5331O1gfFRGbZgwAHILWx5IDLjHqHlf-4qJo7p37vBUA0Bsm-4GJ6lxuPj8l33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛جام‌‌ملت‌های‌‌آسیا آخرین‌‌تورنمنت‌ حضور قلعه‌نویی درتیم‌ملی‌خواهدبود و بلافاصله بعداز اتمام این رقابت‌هااز تیم‌ملی ایران کنارگذاشته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30513" target="_blank">📅 00:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPV70P31YhA-4dw1HI5Objp34rfhwdFJR8q9ODknePr89BRisyzyO-6SJlLCbSB-gmcx2gIwP7sJtCA6pKjSP3X0tquUeR9Mxv6wlxuPaoXZu0VImUTJpOn2vD7XhLbr9-PczIFS0R8IGjMX8blF6NKS4yy3iWQa2ENh2x5l_HRypro5g0cnJHbn15OHdv4kAS9ZxJTPNzZ2ygGiItx5Y-cpVVD0hk54IGnbq3dqrJNbHZEncZY8vRa594gWoiW45rnt5cGDio4ln1NG3OVkTrxc7IrAQNCJMppRXtUMbSi2QvtsXRQFOKgAyR73-JCXukDB8ZWqWOITF4ih-wCLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30512" target="_blank">📅 23:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqLV51EM_mPABfIvcrcXvzdgjvUgGCMgxgmARICFBufXbR2LM393KHtm0b2ac_Q5CDIGySN7KNQ5tCe3540wZfgrSi5ctNpZgnWpYeN4A-N5cDg-KsIjjyeAdZSnNbMhHAKFDVYw8iNEbTZxrzW8YhmrqvQnQ-_abrL_1tiCQRi-43yK89_IWOpCwBTAQeRgKRwCrIY2e3slFVffml4WkTRcdIJow0JAzFKsgiiPoojvGBropiOis9p46-01llyydURBAZq-Zj03hma6MTM_gvbsrVJODWx7P9ZzM2IpQdyq26_qVdFbMG5U4wtpm9_tGc-ea5lt5QccQuaXhy4e6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#تکمیلی؛نشریه‌کوپه: بعد از آزمایشات گرفته شده روی‌زانوی‌مصدوم کیلیان امباپه مشخص‌شده که مصدومیت این‌‌ فوق ستاره حاد نیست و امباپه بعد از دو هفته استراحت به تمرینات رئال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30511" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxMbmqe1ea3lXra72CpU0eUp508zdAbG0zyxeQCg-j_2CPNAHqb5WhW7ZDlVldFqayhYBocb_qNJXqD5EttY9VfRLX1lrlzA_vH4GwvnSxccxkMP5mmymcA-yDOgpjH-Gb1WlhkECTdx7UgoW0uPmLw3ZaHdOfTAiV0fmbeopqaJvHlZX1GPJ0AJYuuziGAiuy4ns4AURgiolb55-19FBCgJ8PK5RWks-BW8zadncKqURqS5tTbMwYv1CkwTXdrgjck_k42Ap0R8amTYr7HxV5LlwUIxRIIk2VqnzhNFc178aD-cQ923lzn61myQ4Snjuij6wxcTQ22qgKCmkrhBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYthuvvuXh1epom7eoiRQmsovZn4EmH4QuMPQ1B_kz4FUCCgBkYakKa2ey5z6m3pFPZEhA1u1Motx1sQY89XJkBRXWrBrfzyW3PuU-FUhwkWQ4AISxv3JXiJv5DXEttRdSqq0wFL3oF4JC7Fb6qxYOjbiKtxP-NEMzS2-Zs3S3LvmXieyM1LAqGmKaBePF5ZD0hMwn_aH3hvABTGgFtmhBK1ZsXVNCNojdJWk1hBLBXRv0qhrvpqe2vIyVm3SovlGvt2vhxSo7lyHImSJIPvWyLLZkbI9kfcnfiSYI7ea7z3ffzOrsHmpF_obmXuzEhAU7utiWMhvqCinEe9gOPxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKOBxhH49PmRvJTlMbq4eWf-xBpP984nKAC2nE-HDwBx8FbuSWqzKjEONXnIdkMLzILJy-K12ihJoe49HDx82Sv7Kcqc1qwEpuMO58Hm1dCAEhsuQq6isw5bvoISwUQtDozU4dn4deAtnhgA8ywMsBf4t25M0sAfWd4XsgFun3enC_LJX0G73VD7fAfU128mGVO7bVOyqt5os-acUB4o0oJJtMKk9GWlosp2gVT8iTygVAW84dyKP2CRLQHG939TKLEVCzGs358Be7uUcyf2HCLaioql_3ymrI1TKS_QDE3nApq9xGjJPge5pMNTixHe5xOsauSpKLQ_7uKzClSo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDAwpfhtutDkBp3qS5CJB_7pMg6qDZ90n6AaQqIGeTrLuW0hBBs-lz6_nBQ5yVIAMzJDsVWhD_xXA0u8KI1PbW3JDsBo6d-bCTixvnHN01ovNw0V8VmAbjdY6oTQ9t6EP7zyvpNfoU5eZstcQD2L8PmEtN6CFg92XhkdD_hr21AhW25qB10im9fMVThiAIbZeXjonhdGrTfxn2JMiTZ0Qm7fvbo9S5hgmJ7AWdwFuF-ID0Jyx9GACtPCmXBq2w5ZicwjMgSiiIQLuwx7CFTsuncZxY79dSViHmynoR5L9DNullcXJKxa-X_BeoiXW2XuX5Xy7C2vgr6ZVlpI14qGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msC5HxoKvSA723pIDzWIyht1KiEiokZT-defbH1k-jBw9dSND7FCPcEJTIymLy1sZOUwo0Hc0cPHVsSCayBaw-KWd1T27ONPBeawfinTJTD5f3TQTyY9Xd1Z_j85-4mPCZYrH6ThSEiTU9EhvgfHdEdtEdgqXfQNLFQmq-OnuL0saIRFe_MJ2NSVwava2WypVSBe1LUXStPOX00fHvX9tgqyi4AXJ2k-qfetZcPzLH9CAtFsX4P8hnx_sH4OdJub-6gvB6IIdaDWx1pvjW1uRGjr_SADf2lKVbBUgVXvOUceDE4OED4bW3b9jDgeSvGBowLzrCtW_bXpqNqM8ep6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9FJni-pgsO_iy6SoGHzy1JKUR91M5fib9l7bdmETSQuMjnK187nSIKElfSwiL1vcohcq_rOky87wCXosaigOeEHu_2M7nntNW6-NIh1rY72AUdgxJliuvNqywGABJTvCKPannBk1vwz_Paj1Z-BfCnqqwUrRfpOz1FJWe4Rv3XTuhQi9VXFsKE1vczH-VMN4TXVnokw5gQm6B_emeIML1igs6-m6X1QQjg2DyFwR6zjv4YP8IGevev06ZjTrg723ntN_qnhIqLdFIeK7L-G6zVM1wKaEz7j4H8BF30tUADYjP79qH68lUSEXHF3PrzVRdh7QjoZNM5GTRmUFTYUEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YykhU9syy3-Whp1elKu-yAvQw1mr67c7iH43Lu10sJQg6ONVac0GtSy8gxEkhCXG5pRO97RRQbskcl0VgZ-T6KfaOBf6clX5w2q2fx8MxnJlCPm3BQSSek31KhkQmSgZXnrMxnnU2ll4R10bZB7QM4mem3wQcxnkgtZg24b1-ptWkpNzhNRIRt3z27K008PXi6n5f2-OEG-dhi-hyW14o6JPUKreuqAh7D8cYxS1O9xFbPPJ6qUdzka7YZ7v6_5c-7RdYPhgw3UqSGPB1ygGKw9kbgei28OMlokHYLQOE0htkls71e4wxn6W7N9hsFvIuPbIADfD1hOX5LR3OdJl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_LC9bSaoxO9zQb3cduIK7io1JRszqZTvaGLoIUt6y5yTDede3JOUmResAtaYtZG8sdGrXkvMKqZCqg3I919N5xkiMAbdSaf8N7KzG-DQulKFjsu70I0FadZHEJ08p0vLS3PTyWvvskYU2bhTg_CpPEg27HovCNN3r7xfQg2uoX-ti79qBJRlL_ATiZiJ4MIcFM3wEISHMqo37Nf_nXHunZxe8KmqStPLTYfa_uShYYi9UCNFRRQB6MTJTXTk-60jfiaVx8tCCCjIsGR02L0bm0ngcF6pp-0DIunho2aAx9-s7Bz3JemaHSsCJqXoOA4W1fLyC387Cu6RaGH3k2ZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=EGOg1kG_Nq6vOzzGyusNzNwkGfA7IsDZmiBhKcUXwB3Pq_YloeOH6tWuM7zjZ_JAJFiGCoM-4WTWI0nKvyN-UzdQ8oHIghOGLjHPXmxX85k2j1QEFQZDSIEnIdztsfmipyKZGuyMGaf__gLREh5OE1_G3d5k1vkV71vhfxQG4umEHV9MrQnEJeJNhJgX8zARldE5oC41rK4pc2x0Kzw3goL2yBXn31FeML_Yu8D9LCxkvTYSmPOvQRH8_e0QCR74X8oOC9PhDU4mPltHjSqKRsYTgrIlZmVlv99xFfmKbzN_v4LjfGBIN2p8m8JISu5_nVDXNXaObwTmvMFW1UBFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=EGOg1kG_Nq6vOzzGyusNzNwkGfA7IsDZmiBhKcUXwB3Pq_YloeOH6tWuM7zjZ_JAJFiGCoM-4WTWI0nKvyN-UzdQ8oHIghOGLjHPXmxX85k2j1QEFQZDSIEnIdztsfmipyKZGuyMGaf__gLREh5OE1_G3d5k1vkV71vhfxQG4umEHV9MrQnEJeJNhJgX8zARldE5oC41rK4pc2x0Kzw3goL2yBXn31FeML_Yu8D9LCxkvTYSmPOvQRH8_e0QCR74X8oOC9PhDU4mPltHjSqKRsYTgrIlZmVlv99xFfmKbzN_v4LjfGBIN2p8m8JISu5_nVDXNXaObwTmvMFW1UBFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kazf-J3rMN_b89sLzBm6dJaATpcb3-cQrPy7hkSx2ekN29lnFGSIRgV9OEjfE-0ReEHRBuTSKOETuouR4t4RZi20F7Qag4aQ8SpoKGg4dDc-ogssuJLHtt1vwmYel9s2ZUWnMGMGwhAdyijbgeLhk8Op72IuX7VZ2hJC6B67TpHS9_p-3G0v_0KnsBb1EJTX7kmIdhfIurYijtTgME1GK9PYdQYkBBK2ViaHybhL4qPQp0Xv3zV2Ten1u8-auL0hgyylTH-w4u4OL4fdUXDwanM__t28e_id6DNp_mSVJs-xlHqeLfsMq-XAEJ4AbWHDdtSVgbLteOyeK3N1feyujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKnFbUEQcnO0Ku8e4zr-j1j6S_aM16ZFe4nLvpv29XJZxkDaAbaUaPt0bquqjVDDBxeqhp3Uj_-bs3ZBDyWVrvpLurv45C4FUCvhvv6RjMAtaxi7jsM7kkwjhjB-NiFb5NyMBT2ptkcEU0znOD_-oPCckG3kqZcnEblvN_vBuWm2XZJWkv_D_V660cnrFj70QyO2vdak_wwCRCjy-ADJpzuQb9--9RaYfprMpQvRDGX7Hscej5Jkr9w0asal9bNLbgbtaMssdgjDQwba3A0u7cipcN4ND1g8jvatjE5ypoTte2EGi5b8-DI3YA3KrIyf-6pn86ZDG7BKN7pAR_g6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK-1hP52YE8Ae4pmnB9Ca__8gA47j3L1OePW9gJGk9P5Oa9B5dv8ctPKqrLZkZAZhywCwLxt5UAUU9QtVFHXDlb6RXmGXjrP8zrWB4AIGZhyRP-lDtz6dZZfxn-FI376lQWiUXJjOzNVrLiKuUlDeEZ5JiRTa5BQXltyQDu42yzp5-T9pEUVmBKSKNFJAIjHzNHVALXKsSm-uONqmJNyknbi_wYizoION2tb9317w_b9uLl4LnKZpeBqJF9rQJU-zAma6D7zTmy8B7FqHVnMbUxAvqnUbNM0x271t6r6b4eMn0Cj3llGoowW3Sleg7FuKTbNEfEabqvKlx8bhE-72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUiirk2LD81tcM6SpaUmSLfngvEtExlOcvdOsU5LayeT_hnOnDYuD_svE2DIN93acbWIMfH50iUQOhl0bqYB3MJHn0OqsrU-GO5ublUBzrlW6ZOTDB9ebCRhQRBK2lpk3Bl2PJ3xvJ_csodGPAJq9JO2m5KmWWhc70YcaQLSW65mz-xkCBmVTdUO5nt5UaqCMRDOPC69wmaVl1BvYcdyxiEcWUaYMx4ah8gtzgQv-BkW4PSAINoG4fNwBDmefn_HiXhsvNMelv9FQvXuzxxZxdMak4oTJF55vlYiRN1VKemq4kpZh8miYwb78RleTU3rmlwemSNCwc0sOQATNbRvGQxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUiirk2LD81tcM6SpaUmSLfngvEtExlOcvdOsU5LayeT_hnOnDYuD_svE2DIN93acbWIMfH50iUQOhl0bqYB3MJHn0OqsrU-GO5ublUBzrlW6ZOTDB9ebCRhQRBK2lpk3Bl2PJ3xvJ_csodGPAJq9JO2m5KmWWhc70YcaQLSW65mz-xkCBmVTdUO5nt5UaqCMRDOPC69wmaVl1BvYcdyxiEcWUaYMx4ah8gtzgQv-BkW4PSAINoG4fNwBDmefn_HiXhsvNMelv9FQvXuzxxZxdMak4oTJF55vlYiRN1VKemq4kpZh8miYwb78RleTU3rmlwemSNCwc0sOQATNbRvGQxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=JfEd7f7mKcDqSaBr6xA_MJoTJeTLLZBGt-t65LQgOrn_oh0epWM_vzPgILb4IF6Ry9wQJ1XZdkRiLYtvGzkVBsfVsnxRea8rKyPiMSfvDYYdGSOZYrdZ-e6Aolotb5J7VvITWAfiainDFRAdYGpYQ4viir-Gwr4-RG1gaSSTMnLaQWjGaHHbQFDqALXSZns6qLSkSQuzvH3tjhi19E2inRMlztCzywMUuhC5xxJmmY4XRrYT0o6Eo2fIFfTRJqYM9Tr8-H6h2nG46-VJLwFeRRpXBFrwrO4vDjL2Bf0IZ9pQ_nYKwEYz_dlqoFY6XnoUVbDB5IEAwM9GgxOeDBNJHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=JfEd7f7mKcDqSaBr6xA_MJoTJeTLLZBGt-t65LQgOrn_oh0epWM_vzPgILb4IF6Ry9wQJ1XZdkRiLYtvGzkVBsfVsnxRea8rKyPiMSfvDYYdGSOZYrdZ-e6Aolotb5J7VvITWAfiainDFRAdYGpYQ4viir-Gwr4-RG1gaSSTMnLaQWjGaHHbQFDqALXSZns6qLSkSQuzvH3tjhi19E2inRMlztCzywMUuhC5xxJmmY4XRrYT0o6Eo2fIFfTRJqYM9Tr8-H6h2nG46-VJLwFeRRpXBFrwrO4vDjL2Bf0IZ9pQ_nYKwEYz_dlqoFY6XnoUVbDB5IEAwM9GgxOeDBNJHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZOVbj7qZ9IiTcmcl6sTsgVemAnV07R-iWT_OwYLDLWC4eupDy-3rXssULCLgcL9NwJEjCersIExEPS8hHJZAJv3jc27kP4_y3hTPhaEhtN9cuD3qFhJ6Nru-BnDV2FcLeKfcPzwKorHKn4I7vGzZpk7RNjLQ05ZwjurdcR2v9cm-BZeQ_E7jsX_J7Au0UcsSM2ND_RH-_jD3mAOfiOyoZmNDpvFiuXrtvkqn2vAU3utuGUsnPbTZypgbtsfMkQEi6oHygIXFajNADLTMrvgzjvC2VdwgIxvP7ZgIU2YY7WHTY0YiGHG0XcN2Mh3FRAfcH1wpWkjP1CIxefQv--_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Besc-mNrAun_si5J0XEnnrKDyZC38TNDU8pe_zvPssddUpaO_wj1P-lD34fv9qrR4Cd_BM_MUdA0jQOqfkjZlM2OOjaieotFkUDu3yMR9FfLrG6bHm_-8W70_VMZy-dERcJiWBLG1ME_BuiEwYVGyrERaXfWNxtBPLpJqNPVk4zb_a1hadPpczBAFzIpwyl61akwG8yMndnEoG9L-OnuvcnInymkFhRaOW3vqfetWbgasOfQRyeHR5q1E7hYzACUqQd2LRPpZuVbfMxR6OeIU3bvy-M_PhdVR7Sjm39_04tGU7UzZAJ_hGnutSc62sJ5FbRnOpOLCCCpeH20eDo1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpzMbUZkUUzFg1BPBfB9B6zmj-p9dnY3LxvJJ7EZP0kmYhvVjbt3TUhIIbqAdZLZeKAwmdKfsuNiTSSlMtNwWsXzAAB0Yz2JcqxNeNzXY0GAtobnTcicodmiSZjutCwucHnlVsHotBOgxqqYcnQqCkRugaaM8OAuPBZkk3FpUanOBf2Dmc-iYpGe4YuwTOoISToISZyW6t0Dnq3J40ZAnsBZFG_qSWDDjvp7o5feHn6AbyiwYHbXKOUrwOQBnG3pQWW6e2DLIeN2iqV4Of1zNzSrEVaYk0W5mCKFJ_0MlqO1kq3aKiA15JJdWRNvAzSklga-8UlPH3rnGtvQckxNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2HBjCi4UrgxVZLraX1vNUV09gvorpreTu3b7T1cGhmJ5aB_ukZn4v31lUSCGyNMWk0WqoZ5HcvC4nttgRTrKsoR-TWhfsg2Qvevb_aVve95voPma7f62d-sdlcENc-AQ3OyqXBQ_6xMjpebjy5RPR8oez1RVB4jGGHqQHzV6lLhhQkUS36ik0KzOhO1VgjfKcZyGNq1LW9snpApiz_bDMDnIEUdKHOZeKknzq70JzzTfg-xQYk06evu6lfdUXeolL-H2uyS6w0ylFlJ_kgpmJJrcHRKSVGvN-4xzAcBmtMj0rWobD9S4-X0SG_vAHPSQZ2puUE_E6b4o1K8TNnLQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOADXxOAFIxVP1s9gn89dBTtQ7rrXM4MgOtm3kFDn3eqG0SeEbINRFj6KAcnHbNxnotKkjh3-oPJDj3_oiG8wrUkoalShWLF4aEb6T_dVH2sm-D2vBwo44BcrkvCBLxBkM18S_M5RE2D6s_434xg9gfz_ZazeG_kLsXf_Xhsw8oH-VbUTK20FhSJQi9iAu2qvK4yKOu7SMCD3RtCoOEiuE9Zl0ZyWqLFoHc9GhP4UzrR00_kyq6kov1bvZywjd8gKUR_Q1NlQ6GwBNIGhaltbVzACWLqJnMYxGvcrDtC3mFTAmmz2Ya5lfN1oTBW4VyXI6zjQXP0UJ3Qxko9iEpJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0607m9_Yg1riFMVSibEA3LQUCQgDclTOkDdm8wLQdLlb6xZE34OL_uFIxuhhe6VZCaJj11dwgtLWubMrwdBU2LnWPdroFbTPctHlHWHxN3sSN9qZGL0xThmt0-k2n3d3SYK_gXK3z1PphL_WU19CV8wef-_YAIyXr8CGEULHkVtbJoSe-AHqxVd8qvzli_Yd1_EZkZW6FJbFFTTu-9JaUJwN9ZbEnIZ4rmNN3qx7z49fE8sHFVLVEDwSUshN-1q3qP6oPrzb2xMXykFea8ImJiNj_4dmOyShxwEW4T00LxZ2GOvXQtCsmshsal4d1vPOzC66aSQNFQ0jAX8fnwzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMdfgNFdbga3eXbJYuH-JjJRKVx9ai4qWDSwH2P39TSjvabc5zl9xTiyUmjlys3ApCKJq2zAJLMzowGJ6a-tftWQUuynwlS8PjhD_Yp-Jp2PaBMFKC1gx-ZVMbi_iFPDBrdRT9O1vFXy69tZjEBxyTQSrWLZhvtu3-VE11OIK1_-6X3FtFhGYE8Yy-WQL2bXT1Hb94iByuz-pHprLb2TQzRnx5nDry1zxTgTSdESKZJrsNZT1jQd1a0w5_tohcRire9EcQKV8cweFtzr-t-vaesA9GccgGKBFhqeizCEzhm90CTvgRZEdPPNxiStKTeH9NZW3SVGuYLOBVBnEnzsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peiQVynPMkQBsacCSczboARsajMrC-hfMQK4Rqapcc9Ht5y6M7HFT7OUmoFPXHFIdV540Bwrzh7DucUr2XQ5pT81GENMRPCK_rBm0bYN8D68S6uEi1KeTzdCkcCKAgZsTgpGrS8iAlNfNpWrWLiDyiUpmbypAZ5ClE0UQQeHFFO-aj-UtyUuOcakGeKJNBBiltGDpCpOyEKzVYZygVfW_vj2e6oUajsZZjZ79N36-2Ab9gu0I1c3CWBbQGZYT0-pUqoaoN51rOC5dvPX9dGNuMR4NUKaJEEX_tE-B54CuBQGdsObJDV3PhAxS_F6g9uiFFxkir1oAWcFBfxX6BWHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYhV0HbJcC0kkr0ZkrnBFoSsa-LLZKMp7tEwtX6zcsIkB4Por_ZL5DKq4fbRKtT7F_FeqP_JTJi_Njejpm2icYwB_B7dFn9IbhckfYwY_irmKN-M-QELohfXlZYNhLvuesSUW-AAVy2kyTJRBFe25h2LfmEdtonu3u8GMu8HR2KxvdbCCezq0LCeDZQXLdfmYOK73qSCh8OqWXHbKDt3Bs17AfOFiFWiD4w7XMsbyDCTnO9Aim8yNOa4qhLjTlCrCLM9bKn402Z2kmUSiml0YjDvpZVKXZSpmRcqzq9GYbtfLRCJNP7JKqKdUU9W0Fu9Q4HXeYXeUmBgTEcDPPmgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCJEp0dXEsXlFkDGpcwenLN4axscsYUJQhmDwEEMU-Tc0h38Jfccc72NQ3G9s_xlEqvaqwQcHyT_u_b4l2uj-XIjAwpKWn-1JcA08VKPsbG5J6YK8WxOuq858cWZEjQ4PAsV3g1LuDa36GFUVIz_CDirGFffXnEjMlXgV0RpXuAgLtjC6BF2LDJqEQvr_vL7GmBYLE5FbVQJKeb2LzjZbWZK0K5YRNPoRIJ7EYs0R5fgZFv57_Nl92mvWzXNFTBYbK2Z3l6M8otfY_v1fAH15N5ptNklWDCMT2x7cIbDkWAhN-UhuQcW9PQLHTzXwd6AnDIOj30DQ5BQXYtbDlh_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXzFRlz_Fc_ertRaVoqIXOM_oE-BtQX8Rg_DNcLlDAfoh_fX13BuO82zNeuCIw4gvfbJlobjBm8xJFtPDJ9cwQlrzKxUpDHhq3vXORhgGfi-UOtXhnWyiH2C4-PhKguYskW7VNei1WRgyHs8lXhaIcExUKvPWZu2HlSJ3nGAM5NnUzpofDv2NxO8RB5KFiTR3lE-UtDPC2S73u5xhPQt_DV4zPxuID_JkecbZPBt3PcTpRpSOSgk_xkoPx2ckWCJJYv5LfSLWTHPj8tE5eB1JRza2shhhd9u8pO26FVsrfokJbz_hVdDm7H2PmvvK1N2UkfG5BJNxKZtgU4ciKG6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px-RpAwbCvPU1sx9zmO4PDTeqUdJknkGipOUaBrX3jD0OEDF12T1xYmEQT1yocWsfG3IIlwZsQ-iCEZSEuSF-xtoFGeX_asg4rJyeVvFwMbKKg0yl3pA7A8hOwuDQdTi3OEqZygfqW7X-f08ee03Xt7ovg--vymaduBNOVY7p1Bhl3kDOchPr2hhoHlsKauJk95HFXIxIcaN_vH-bYsKN9WZWFihUOwwTV-d8YB7b3sydm3SZi0G28NhYM1VmI8ciPxgkbm7Znpw9W2jDhpuFMzaxEB9FlAPl4uOQ5I7S39hqBATpLyWSiBKHfg8T4utzfKalLZPpgS0ifqqPEpmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALsDqM04TPO4Jb7mcbEPhQpNjww17WZFWnPOcekWw5LYpd1deOiEo_zCqHw9IU2usm6s0MFcLRIvB5GsglCGk1QWxAyoWbDV7OI5LgKW95DkVpdV-Ax57iIL6W8S1Ummt8cttRxJySV1B6GIsEiqJCLkkAFm5e7khePhrJmEGPGCbFRR4ODLeThJMOVb0kxwkzFbGqpjp30eF2i870R9dfwMSi9dIKs11oe_6UEmZjdF1l3AZU190_w57FnGlYRozhNHpY8fZUcM0sN4t302h07GGaPIBF2dkX8Fz5uNuUrpG8bY8ysjEoXMsB70u2nF45cKfmZVoiC0Hye3kVEcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMdNqPaifYQGqnwKFKm_5owluBmiE_UbwYgtelS5Cosafqt77FkGs_oSVEdjAP72ltFqZMNjxGm2O1qaTRJbhKpaTI0SkPHQYkDOUOScFg6KELDukWihN86zeysCycr21hsvgOwXG8Of7myTZ9YdLQawhXBnYEW6lprlEX_zGPSCJxi88LevrtkIIzmEUq9x7pP2DbS6JH9pHWAsVuR_eK51Mr0xai-d3KH37pRy3TdCH7lNGTss9FFclcA525gcpqYoRbe48EadyH_JT77oQQ43Sjv0OL1E-zcDSFULqIWCOPG2e_u49gt0oD0XSNYkwa7GdrPIiA_y4TL-pdjtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4miDQnLyWiHe-fdAVN3COvni3_EiJttWjSGRMwP445oaFxhbY90qIUZWelzUXNE1DP3rg7mBJ24yrYAUZdVibYZtEWJqkJBzuLeqUsZ7qSOPblTUoLiatC2517CNV8Xv-8HAKg0daTb4vng9T4FjWGgsGZn6yZSqwiFIUMn4WZV_znYbGeutHUCwe5yaYmr0D3UlbtJBXN--7ixeqGSfrWZxejS_vB3LwSpgR7oyVDfAOHn66m2TrnlHhd5OQ0OVASJOvRyQ1pn-I1jI3iPrTfHQ1nAXzM4A-oeAkvGI0K8WrxNiivB_bt9vmEaWeyr0-ZU_zD9gddclXhABWgz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOjLIOUgH6TRIxcETT9xkxDoxIr9kFeL4Wz-7waj170Q7pvNMSRCgxVv5eqrw3JJZb1nYz5-IGnRrewX_c1dZN7RCVSFKMZjGyquh4yBLaHJeDTE5cIUz30GWzTlzexrGROpX0PlZv7HGMOst6NK-zA6MzhZN1CvymhtYgCaFT28T0s4H63_fXawPQ5UOWp7np8Hw3xFiloomfGt5CzfBytGX4SrvNqMdv_hNJ4sE7ZQF03UHIuS1l4gm18TvgNIjmSjUhdna21g1o9ElPgVQaj6KpLbVKLhObT7znt80vJEDQka2x4MkYp1KF4eTolH5uBnutlvvIWs2saPBoudyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmxdF019p-YFjMtYiShD6_E0H4tuoA5TlbZWmp1ivycTdaT5bmR8z1s_8ra0S3Y5bhg5ExcC4vGje8bam0qQPsDRhTtx8Pnk8AXr6lDOgZcoNXA3wkw136L1YE9curzVS8yaKouCVmz8tfbT8bd55gW4Y3XbxFaE7E9pVQ88__PIIB2zb0y7QdJVGch4zCxb_JeYQS7FTRhP3Oz1XyHFMAYgSNdVtuHty_P8WW2mRuMkL_Y9GOT2WOmdB8D8j-70gpZiaAlqxBdOfMbhu1L4BhX0YKEqxRTKuH16tzZC811Ksp5z-5iqofRO0UqWr0vyjALzucNUtfGsw6xI42Pz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6eNykA0l5tzVwFbow8PWaIwCBVi75wlW7lhBwi01X2bXG5dHHHk_oj-p9DHI7rYuWParrV0Fp3kDQbA4eED3fHqdSX2LSYHNoWEkVFxTB1ev5xALEgIjc6yA0jtqGocrgIgYvFtEkyrhYwAmqTTuGYhwClk6kTAfSAll1kOAdfnO_zQ2zvekg9mR2KSjqmIhCpqKje0YCsFy0UvbWgrMHsw40q0qBUmrdQtlU-svdVIjOGDBbZHJC8DD_5sllmrIZHD7dAMQ5Ge-GK22T_w7UmKBNXsmFExmBmIBVTLm8Vx8owuUEm0vGt7ao1BGFaLz0IGSaBEVA0E5_DXITuyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en4Va5q0LmwB-YzMbnB0uaP5-CzX7Rg1DKIz_4pV0ANH9ycUD6qULRsARx4XtE8Yz8Nbcxj-VxFU7to9bkFeUO76ViU8PfISWrjKxMTQftiEyiRP7cEukUVJX2fLEgRgcjCUhP4snur626P7_3d-EcQi-aTKaD3uui52iYto-WgYk6BMKBcp-NwypAG7Sm0CiLY8VePjev3pqe0xkPBPFOntWDvehD65Bsw5k6Jrtv5zAYZeo7jC6j1J4G0_hz8XLt_CXuAn0b3L6dw8PE6tmG3h0ENmIVp9Y89f4kNo24UFU4dPf_gArb6PDWKMO8ArLXJgoP9DsoZq0epms1w7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=YTlz99CUF14STTXd5yyJRT8BO1xwpnCkoKxuotu948_Z-tZMV1wWevBi2VaAO-64T6GXFwB3YEE8D1U20YrGRGfWhm55JFcXlqs5tOmj5ZOafEryeFOipqX6-ST3FIXEAJuAGORtKag2sMStw6MTbwKC6goemiKhJOIh2mtZHpmbBAcJ6V2IZCP0C-OfmId6HdRj9iGpZrs0Y9oZvJ6vVmBbs631E-t3nv10TTj4Rlw0oOlIbZkGnmDdOtkn5QgpcN7cdLk6ErC8GsraHKNnKDDDiV6G6amErK3R2SSAumWC9nDbZNFD5u7MAjjop_jOnzixcO6spJWMQvDQueFZ9lDh6xb-XsjG3b8FTRczdrTc650y9Qgx_VWHm4J5aTIwm3Qs_YUMrfQCBQJLi9TLYZSvE-FV4mroC0gn2HVnkXjUb9yAifSjfKWuZ9qtT_ZqMffvtTlvFOAj9ZUufeMqkzm4KCLDleN31IQrw_qpJrBJQ_SVyilxppOZb-zDiACAPR2x0m3EQEkkahTod-OaTBuIgGXcSCPr_aWE5xKlmmz3pDFrW1dJLrFeS3QPC-x6VGQAXapomk35P6_XdqpwFA_kMc_rEEzuM1i5d383RPS1-R2GHqUzgdDebrxtYlofoWSFv9CvPUiTGnM-ls1JlcL7rvjU3V7senFtpx5CrlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=YTlz99CUF14STTXd5yyJRT8BO1xwpnCkoKxuotu948_Z-tZMV1wWevBi2VaAO-64T6GXFwB3YEE8D1U20YrGRGfWhm55JFcXlqs5tOmj5ZOafEryeFOipqX6-ST3FIXEAJuAGORtKag2sMStw6MTbwKC6goemiKhJOIh2mtZHpmbBAcJ6V2IZCP0C-OfmId6HdRj9iGpZrs0Y9oZvJ6vVmBbs631E-t3nv10TTj4Rlw0oOlIbZkGnmDdOtkn5QgpcN7cdLk6ErC8GsraHKNnKDDDiV6G6amErK3R2SSAumWC9nDbZNFD5u7MAjjop_jOnzixcO6spJWMQvDQueFZ9lDh6xb-XsjG3b8FTRczdrTc650y9Qgx_VWHm4J5aTIwm3Qs_YUMrfQCBQJLi9TLYZSvE-FV4mroC0gn2HVnkXjUb9yAifSjfKWuZ9qtT_ZqMffvtTlvFOAj9ZUufeMqkzm4KCLDleN31IQrw_qpJrBJQ_SVyilxppOZb-zDiACAPR2x0m3EQEkkahTod-OaTBuIgGXcSCPr_aWE5xKlmmz3pDFrW1dJLrFeS3QPC-x6VGQAXapomk35P6_XdqpwFA_kMc_rEEzuM1i5d383RPS1-R2GHqUzgdDebrxtYlofoWSFv9CvPUiTGnM-ls1JlcL7rvjU3V7senFtpx5CrlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFNQpbhUgL3fj85MrW3z5K7hLQX1VhsJXT4xBmxiCuZjipdcO2TRV6Rxl4ZdVh0nrotkMfzopAfFFawkgPrn9IJYEggUXCwFkDHz_e0CGb7EnXT9CZ5Sa8un_SZle5JgnjSdUEKg6bo75WOZXzWtmBQpcRj20hVtPRqDF7KZ56M4sISv8K5o_6mj8rFPRNohnnqplm91RaayNcFJJ0abIdqR9KLBAwxoh5oPDWS1fTws3YqZHBZ5_u3_OBiHV50NrlZAW0Fv1BhT-f_RARS62_ZfOcA0EQ92imgbN56L_MVX0ILfyq4e1bLLYBFpZtndP-njjjZPx4uXHwlw1jvxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbQzRClSgwAF9Sq-V5bbdMeYC46qYW0yvV4m6cnmvZuJMZ5LqcArQXQ3QjmpU8QQW9vjO0wdEWjnpjTEJW_cFpkW39N41QcME_Sfku4Stu72kgtk_tKb7FfE-UBNxdb3kXj5pOYsvXZh79GrhzkYWaAmFoGBG1m91odREUc7Pbz5tfqUDcnFyhLc0t5mLu6PbKT5HD3ouCKTR4l_evIrfK9ahvxO5TdxcYw6GAWioKMbjFCcg6UoryB_ytXQnl55OLZd0qIUIMayVRoDnMJZFvcNEX3RQV5pLprUQm27YMbuiNDa3OuuJ09qWRfWD448U9WgT2dLK7tjVfvqNPj8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSWPWNMUVbemJS8dwAThpY1Ogw4KOpuO0uHILQa7Mvs6P_ANl9GNkv4fS1howKBtEvSd3PyfMHJ6ApV3u9BLHYGd0d2kad2MRVp17Mjntq7ZDoOvobqBpLsORw9y11G6Bo4_pzmrSCW0JcCxny7NKo2gdg5L3NQLzsCs_GP1VoncjOBMleoNAFmc4vnR_RC57vqiHNei7TEEoxokvQBYnfy4NH2tWvHVgLQ33lfQGkmPw9PvsNIQ9gDj27XLxVa4e3sU6Y0ts0WqDLfzPf4H-4I-BjMFKpEG2CHYvWvL0xptys3hYtHJg6bBIUQIgrJFrICdvy1am22C51vBaJp2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=Tpd-8MNYpaQc7_l5kogu0ZyV8fFCzuM-dXpY0cZ6MT_FWyjgaS258aCuOUyGEGfXOQUZz9YQHGIBwAqCXu5PRweoupJYs0vR5FIfD1etpjwX1VHoWXlgies5TjQuZ38KdKf3ojLrGtBNBYPuLhkTM87mND5Tj4mzXnfH3fitvCF6ARQ-FT1sELefSMCtj8HB70ARKmON--CqLwAKcOfQgrm1xOeV3Dcy6G-MNz728KfPewvcifkrcScQEtH6CcZcvNKjYSW-f1v9M5iOEW75wu26f5iinzna8R_fgS15kQNmwz-BB5nyLbxyx_ouJtB6A1jSWkLODOcDUbSxiG_4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=Tpd-8MNYpaQc7_l5kogu0ZyV8fFCzuM-dXpY0cZ6MT_FWyjgaS258aCuOUyGEGfXOQUZz9YQHGIBwAqCXu5PRweoupJYs0vR5FIfD1etpjwX1VHoWXlgies5TjQuZ38KdKf3ojLrGtBNBYPuLhkTM87mND5Tj4mzXnfH3fitvCF6ARQ-FT1sELefSMCtj8HB70ARKmON--CqLwAKcOfQgrm1xOeV3Dcy6G-MNz728KfPewvcifkrcScQEtH6CcZcvNKjYSW-f1v9M5iOEW75wu26f5iinzna8R_fgS15kQNmwz-BB5nyLbxyx_ouJtB6A1jSWkLODOcDUbSxiG_4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=Q6qCKEjpS9qh-IsqbjnYiQxYETXjdfcIg0XegZ7es9e31jHX8I426PZrC8s4MabAoRdpQdG0jeFwiiU-Sub_IMg8w3B2yYzI95Mf7azHjlN7bYcMagyMj9VX54TSqa32ZRpvJiYi9tEn9C-r826yydN4oueYsLcf7KLhzQdPSJ95ZTa7kGzV3SSGDilkSIMzP2cRVBHbfqPrZ3QrYiivYzqfTAVTNBuyjblYNqev30rC5InOPGcdRRfmQ9QqGyZZazaJ0iNlfFK_TVoRD4pVHuBqPKNX7FakVLJzRX3-nkmllClxqYQS0g1tQ14UM-ngxEl2MRSqwpxXRyIPeguL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=Q6qCKEjpS9qh-IsqbjnYiQxYETXjdfcIg0XegZ7es9e31jHX8I426PZrC8s4MabAoRdpQdG0jeFwiiU-Sub_IMg8w3B2yYzI95Mf7azHjlN7bYcMagyMj9VX54TSqa32ZRpvJiYi9tEn9C-r826yydN4oueYsLcf7KLhzQdPSJ95ZTa7kGzV3SSGDilkSIMzP2cRVBHbfqPrZ3QrYiivYzqfTAVTNBuyjblYNqev30rC5InOPGcdRRfmQ9QqGyZZazaJ0iNlfFK_TVoRD4pVHuBqPKNX7FakVLJzRX3-nkmllClxqYQS0g1tQ14UM-ngxEl2MRSqwpxXRyIPeguL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSQmVVfR5ePxopXE68R3GW8eecIgMo8tktTq_96Pb7hiI-ds4rTv4OzwNtp44pCWhWxZHaLj1AA3Su_S0Ig1lro8p5AAxhK0d8WZpjueXgLikVZLM74zNQ4Kh5p-YWnvlrSmO8kji_soNqaLqRDAEAFWyAiuvGt_kgWy5a27HVMmHKLPimkh4Vzq7dtoAulPqQ6NXlJFW7EhyZd82I_tABMz2z8wZlpL9EP5yhE78WVgFVYl8uxwHFh4ILApAewsv5-SbnFWzzVKQvbQ9AWU_CHbF_o9KIzgYB9BMeBQLuUaGyveBJyxGqg1YOfF89syTfMfYe1jbclArIaovo_Jso8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSQmVVfR5ePxopXE68R3GW8eecIgMo8tktTq_96Pb7hiI-ds4rTv4OzwNtp44pCWhWxZHaLj1AA3Su_S0Ig1lro8p5AAxhK0d8WZpjueXgLikVZLM74zNQ4Kh5p-YWnvlrSmO8kji_soNqaLqRDAEAFWyAiuvGt_kgWy5a27HVMmHKLPimkh4Vzq7dtoAulPqQ6NXlJFW7EhyZd82I_tABMz2z8wZlpL9EP5yhE78WVgFVYl8uxwHFh4ILApAewsv5-SbnFWzzVKQvbQ9AWU_CHbF_o9KIzgYB9BMeBQLuUaGyveBJyxGqg1YOfF89syTfMfYe1jbclArIaovo_Jso8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3S2YjuKyhBtsDKfktJONcSWhlsr6sr04qOZtguAWav-MS5tmnnuICz85xYoRDOOKnna_qUb3NOIUo0zRozrm3Ja6CZYxplyzoh6rzSMkCOXBil_t3Jz5EhsCQGu4d4phzWXelA57-rbDcAYb7waTLB0zvwhOIR6SSAC9p4a8zc3gqQEfEQbiOnfHXJAzpgrvo4MQhyrAFn4xR-008jyphdADHEoEjiexcsW52wBKvwTNPYC5hRlT_O5prjPIRism5YdvPjenaN1r_c9BEizX3lHHWoDTkzOF0chzYgejHOCv2n7yG7r0t7UMH-GZSYj0k5gsPn-OL1A5272JXtnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxO2yPqiTPwecGIDWxB2mT2bXccZ93CPrBiHUPsj_2L8p9IugwN0ckjL_ZUcfBK6zMXehixVPOa4xOSLdSslRvzvQS_qDRf-N_UD9WkvwsFc0RAokUofB1rrlKF8XQ6u-WhARO5WYyOSBU04Z3NdwJch9kHE1J4NeJc-XB4jbcgzcCq-EBGIKCIziScTTMFhwDZQKhh1SMttsBUn-1nzPScltKhrKqdfJd6gtqrYaN6OOlHKqO9RGlYs1ZL667e1DzmTo-g3y2bDoq4Mpg68roYRNZ1vQLFIKTudOYu9pgpbzPxPUWr5XA4Zm70Zr996flw9tp9khi7Jm4ASGpvSmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=HpUjN6IWh3c9MZa3uUOv0_nn-PdGJcOGcJdLrGwPbw8_nqId-_S2p7gHBjEH197UZ_wxtOPBf5QK2vzb12l3AbGe2861OV78u7Zv4uTIG9hg5cRjXs0QE5pUZyfbJx4DOrsXSNGu0JW2QcB-7rtaw9IE0FlzXwWbm1h-aLFlOv_uLJqRKjofSbxvtsBXVTrO4Df3nWRT6Tso1-dvkNc6KygCv1EMcCRovqTCeE2P2yHdu2WOehoywAFYQ25VAlYUg5c0-4sBDP7QS0PIw3d_mHdTpVo4CdJaFkOz9fWGPBDhY7VrYD52-NaplVsricWe1zik2u61MCA5kpLM5PSXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=HpUjN6IWh3c9MZa3uUOv0_nn-PdGJcOGcJdLrGwPbw8_nqId-_S2p7gHBjEH197UZ_wxtOPBf5QK2vzb12l3AbGe2861OV78u7Zv4uTIG9hg5cRjXs0QE5pUZyfbJx4DOrsXSNGu0JW2QcB-7rtaw9IE0FlzXwWbm1h-aLFlOv_uLJqRKjofSbxvtsBXVTrO4Df3nWRT6Tso1-dvkNc6KygCv1EMcCRovqTCeE2P2yHdu2WOehoywAFYQ25VAlYUg5c0-4sBDP7QS0PIw3d_mHdTpVo4CdJaFkOz9fWGPBDhY7VrYD52-NaplVsricWe1zik2u61MCA5kpLM5PSXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Ezyls4lY9rKGgOlAxo7X_j0UnFffvx8xy8Jkpz73bSjEZV5bMro-V1MOP0jqPi0LDbC2hA2WpSgAVg3CgAECkzzMpdOUwsaH42Jbf0YPqi9d4UthoYELUtIM1U8wIfUEwLVfVzjk8BeylHyRK7cqCEVsP53UMYRiGN08r4Rq7iUMGJHuq1by4T50Py3POGrIfldtTDV3W4eAWZMjG-HKBnhz1a5AxydC54Rw0eXL4lrieMK-WSLVJYM6oZtrRez9At5eX4BYne9DvPNttdzuMm76c0Xi9FcJ3RbsEp1hePL3_aMwKy7z5OQYjyuxJs3U9nJDhyTgd4uw_4Mav2OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS183EEbPWpemuLPRPl00u7ijrAWIcRIcfPRKZSYbUwH-xPh44SLeS1k4dH382f2muZc8U2RFcFfZFdoEXBAhZI-OFqXF8vdx_SCuVfIS1jT17rchVEV58gtyKoxuiQzJqBC1QYOiQdHwaSBib72Uh_V8JHzdGzoKu4zbywXGWzuPzfURiaiF9F2x3QAHwz7SenjagB2zxKI9eJfcGfXMy97sqpD3RJQJk6lwjpjUpdjHkSQ4xeYBP-mqBvKCnha3ByrW_titaSIEtjX3hSwHiydPrYuFim8tfjXNqPU4-QON4NenVKZpnCYRunT1CDe3jw-9txyJLfHdU6LQ3pbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=fbEGJ4Gli6ZBCnTkEOqhwKR5SGVWYXTqYjg6l6LNhAkIp4mHIHgIUwBESZ1-iPo4IkywTXgFJYcafqQXUzxH43Qik0OIvgQahSagceWkugZDtBnRB8Pk2m8rAnz9-Rwe5Mt2E_j4DAWVa9PScu49hOi0bn51O7Zr0Qclf7aDm1dEc0LVWHDD3g0jXUyv_uoSH7yd04gGGqHqg0hTfwtc_dgHc0iCglNhdpp1qaC6ZiiFYNyTq83TCEHZ0xqMZT_pGvHmzJAXHbIkgNbNIzYgKcfUE_svbT3CSPjYuLaHhY6qXcQrhIhEiB1cleJjx_GRme3jpZjt2FJFUlQEFdoCjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=fbEGJ4Gli6ZBCnTkEOqhwKR5SGVWYXTqYjg6l6LNhAkIp4mHIHgIUwBESZ1-iPo4IkywTXgFJYcafqQXUzxH43Qik0OIvgQahSagceWkugZDtBnRB8Pk2m8rAnz9-Rwe5Mt2E_j4DAWVa9PScu49hOi0bn51O7Zr0Qclf7aDm1dEc0LVWHDD3g0jXUyv_uoSH7yd04gGGqHqg0hTfwtc_dgHc0iCglNhdpp1qaC6ZiiFYNyTq83TCEHZ0xqMZT_pGvHmzJAXHbIkgNbNIzYgKcfUE_svbT3CSPjYuLaHhY6qXcQrhIhEiB1cleJjx_GRme3jpZjt2FJFUlQEFdoCjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=P1HHx1Etqh2DcAF9bICRx_F0s4JR-rsE-r81gNtGbogNwacIMyiiVkmhTMNA0DY8f_RsxwtJSzFM9YFxXOfKwXlq699gkQGGXZeYczfApBTfVwDsy8-1wRDp3rG17OiPvvnQeKL6wnZSTBTACbKSNQf5cVQ2bzw8dTNGo19Q4er5tCY_6xrOlyC_bEIFYYFEh2pBW8TwVpQIw29T8bY_WUZN15CROwUF3p1QM-vOcnqaP6d8GrJJeofqyG0bSH25kK0efoiwARNqHUP0fbWx6bGJ-6nkra4cMOYfaeJpWpwg2xNjtZRRnTDIoh66OrRpwtq8L0D6N7owRG15nm6HqqP5TbZs9BjGo_yky5DktBbmua1dM9s1Ui7KEiJtoWHsGYtXFIRG-uUglN9XYZUzuJ8BXeVGqKZeKg7Y495_m1xY3ytcSkiozGVt4nvwwhcela6gjXlET5DnOhuibXcLKNPaP9BD-qwrRZlQw0SpBnd3FQUyevRwC7k9ahykCyU1TZ_QYhYO9E03tRe00eyX_DNtNrvx0UCRbiwi_a6RSVprjCQC3t0xm0znudkN7K8GA0yonFfRyIjkt8z_9OGEo7GQsDA_Vpk8rNBVnSS_hdosCLM1LMjRrJ8QTXXCbxbQOvwJWFx29T1MaZreQkzvKbhyTfi8g9N0_ujzg9OyLSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=P1HHx1Etqh2DcAF9bICRx_F0s4JR-rsE-r81gNtGbogNwacIMyiiVkmhTMNA0DY8f_RsxwtJSzFM9YFxXOfKwXlq699gkQGGXZeYczfApBTfVwDsy8-1wRDp3rG17OiPvvnQeKL6wnZSTBTACbKSNQf5cVQ2bzw8dTNGo19Q4er5tCY_6xrOlyC_bEIFYYFEh2pBW8TwVpQIw29T8bY_WUZN15CROwUF3p1QM-vOcnqaP6d8GrJJeofqyG0bSH25kK0efoiwARNqHUP0fbWx6bGJ-6nkra4cMOYfaeJpWpwg2xNjtZRRnTDIoh66OrRpwtq8L0D6N7owRG15nm6HqqP5TbZs9BjGo_yky5DktBbmua1dM9s1Ui7KEiJtoWHsGYtXFIRG-uUglN9XYZUzuJ8BXeVGqKZeKg7Y495_m1xY3ytcSkiozGVt4nvwwhcela6gjXlET5DnOhuibXcLKNPaP9BD-qwrRZlQw0SpBnd3FQUyevRwC7k9ahykCyU1TZ_QYhYO9E03tRe00eyX_DNtNrvx0UCRbiwi_a6RSVprjCQC3t0xm0znudkN7K8GA0yonFfRyIjkt8z_9OGEo7GQsDA_Vpk8rNBVnSS_hdosCLM1LMjRrJ8QTXXCbxbQOvwJWFx29T1MaZreQkzvKbhyTfi8g9N0_ujzg9OyLSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
