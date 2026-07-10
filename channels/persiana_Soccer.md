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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYVXS4fMFz1AFX5QM1qn7LNjVoZDQdqj_kiatFo-fGQWM285A4oCUJNdI2xBurXQ5QmA8nNxb86CQp6ljWJdy-BTPvrT7pVgLFAipfmKoIUs9-6dYJsNBzYxIlLcZJNyxF09N6ZYjLLeHCrK4T58wAy2NzDeEsOpMs2kX7PqvxiiPxMJUcJS_Apa3ZNSUcRnHHldR8kKtiLiCNYn8pGK1AKj2CT9jWxWIfpFphIGeNZUDy3fMnWcdK5H6zBKRIJq2BzlRHok9r9ageGaQnrn0beV2djEaSdcdxPj4P8dgKr1iLYsejzA2jDVqGxp6M7o-8cj9O75pV3Jpyd7ggQYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU7USQhs9DgwAR1gvU5AmJovxxNaXORFlP-mLPs9xRkqz1gY8OycTTcwMC2ZdBOFgbTMlWxEsBt_-Oexp9FQChndH7syRrKEJGQ9YAS5jv2Oupg-_sy3DlRg51OovME2G0rPsbgYYYwTA2wCJX9Yp97rqEM68L4k1DSQ5KAaVWw3NFEE7T3Pmw_PQXXlIrCQNloH3DHkFt_hgKlb2nnFrKMPy-uA56wH_Ahz3bNSCpsKiF461zCnwEIeETXRZz9_nWzRIaM8RA5qbAtz5MQ1IZdy9u2nqLjSqXtkKpxR-ZrL4qcRzSNTyLXgWT1t5z3hOP2lyl95A-fifRCIdRWMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYMA4ds9Q7SjJTuO7IgiF5b1gJwNG-OpM995NZ3BHIYY4RatspaayET2BJ-b65QsYuw_Fga7ATNuJG0iGKpp95rWwwtVP2b_68enurr_Llwyg3SeAygn_y_KVAfuy8xkgEdWM6dxE6E3zxJ7Ozqop4Qs5ugnXU-tVPNnXdThwYgoio9yzErdtGXlvnLg5jK0BNQqTjS-2BzHfVMa5UMHbagpubTCSfAk4VG6Rf2p4cwZNlHMSH0xSEwIWYBboqv9K5x5J4MHOX5symyi3ng5nkLPpZ83NzRz9A9fPkRIWPK4u7jZtSDSO0DxDBauxNKT_u0gVZ74YxBI6S480U1vFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5bqdA_Js9YTEeCN38IaVkLLh0ajfhD6dCgdtTbEazchLckXfnkFxgiiO7eKbJxA6zUuJju8HQ3vSBImjZrAtXjW1Gp1bih2-nYKGz8j3dmPprfxHg6_YlbH_weZqnpW2PnPxM-gJwgjKYEo_Trr5vcaBDODgJiTGFdTYLI2a0R5kMETmPW_ET7I4iaHvSyjZNT8VD50hFP1203FgqoCnFgbL-5Cj59XzVqzmqLSRlavu11vVcYIyM9-lQQly3SFH-KrrUvakpfXqG2p4wMidp0xVp-j142Oi2Ua9_P1lpeWibkCMfSPLq--v__8iJdQ_BVZnfWJqf82phhNQ5Xa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnfxXkoLGZ_1viGHlgDt7hrRPqm6a_o2lwWWMxw8b_WiwTMWWMNdfxifM_jWF2MJs5DnCFLZUyZt7br4_0aJ8zBaDK6jFI4dzicI0M__yctoisb8uW5MqCL32Uec9oE0JGUDJMs4ltjzvFcWADo45AhmZCwVRlwnyGjUmpVCDXIOvUbSatojkdZzeo-tzQhTbqAYkwKqq64J6DF7wqVWcYd7esrY-hEkfcsVXtwIXn-FkDpxHO2eXH_B4Z4b7oqyIKrguXGjy8vPGk-hxZm2p2BVpSMjV3YDCPZDDD60IYha2eb_s0udIzyW3FWNBe3juoNMSBlY0I50xu48fp_mQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5DXgNDqSkA_utCkV2wHaeg4GTzYlnyynSAmYh2gevMQhxgHwXPHIOv0R-IArE1Yl9MMiMehM_6An95jE2OYvySpx3478HyEZqDHrDAoNwQFRIJOfADC9F_XjJR6XXNTcBs2EiR2P0c2jkPuFXT7gRZF1JIYECdwQ3ruHyoBrjNxmL5Zs2EP3ff-g-V_DPvPg3Ec5My2FrOCbrraLsE3ZAyvDp3By2BYzEMq9zLaCFL4qxfvfiXAmM6ePcgd42XzqtwsNQERu4tdcPZOXr_-3pCljKtg4maCv_dI2Qgz-kK_c8Sq3SuDAORXjdT5AnRNQUohJevLvP3pTt28aEvAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=YlU0xiQj8_TlpjTK7QZ3mcJNgIgkWPXspQ0UiSljj15NiP5aP8SSjJU7L9Gm4_5Lr_slGPfEKRtOTbPmYc9gPxKz430M0COE3FkUL0SxyNLQkb-qOCzYoSCIPN4C5xX3w22cCMj0DADxp68y9wGN1gDz_h5It90GG1GPdKNrJNR15poGpLUjGsg7H62jd0C0w4hBm4QIGB1oeuYPckl6VAVRwRKlVJRKHUqEOxS82QIOcckBz1oMOUkG_TV3Ckou_s_wQhfpsNjQGEnR3QH__QQzNC4Pxe3g98jQnE7cSXhyGqk7gO1eZz2icfu0A--9jA1qqvpiBJ0zhR1q7JZ65Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=YlU0xiQj8_TlpjTK7QZ3mcJNgIgkWPXspQ0UiSljj15NiP5aP8SSjJU7L9Gm4_5Lr_slGPfEKRtOTbPmYc9gPxKz430M0COE3FkUL0SxyNLQkb-qOCzYoSCIPN4C5xX3w22cCMj0DADxp68y9wGN1gDz_h5It90GG1GPdKNrJNR15poGpLUjGsg7H62jd0C0w4hBm4QIGB1oeuYPckl6VAVRwRKlVJRKHUqEOxS82QIOcckBz1oMOUkG_TV3Ckou_s_wQhfpsNjQGEnR3QH__QQzNC4Pxe3g98jQnE7cSXhyGqk7gO1eZz2icfu0A--9jA1qqvpiBJ0zhR1q7JZ65Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6CI1n5HzvC6VMzUvkWoK7v9GtM3m9XZ1oZNlYu39v387CMOYYGJsIUjWz69T3E3b7ErlyLhrBveqHimYmV6qEQ0mosBRkF3-tnxo6WY61nBU1vWswRdACKAIzcI9RUz3v18o73R-Oi3xq-da3D-5QPmcfYzHJwpu4et8RDysrjDvXWmqVRH3eC833MMjQTh2ZND7jamAReu10bCdGbnoZSSLRMsTq2OX1yL704EaOpkVV1XndYAcJMHC0VpQ7otu4MFyowA7zK-1DbdizzS-sXyRSNpsYmQUElBhtyi_ZBPMtCpOf905PeMbPF7jsF29VKw4mJqYzZ64POMf97qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXwN6hgWZFhSTWPN20AzxPkvNGG3kzxZRyQQIdbnz8Dd2RtkRTstFw4gKFAOuWOwQf3JGCERoV02wvCx7ImH6nCL-rB9b6CfyhHAPqT4NNMOkWWOHGX3t1dYRqaoQ2MLzBEUqdBBwwocY4M_sxUk3BufZ-f0QV-Y9VXQT-pgqJgfs2EEIk5yk0YEZlP2cehapjEVM7iToYr1o2V_dG-vhHPT5_R01BX4h0ssT7oFO9x3IoctzUPc2PD5vF4y9PN8GKm8KBgdg4AGx6t4ghShA4FPAMo0fPIibwwxkpk9t5Up5xZ4au6XEQBHblJYsV0EJx1whnCz1tz1enP9e_GiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9gj53_q5yyry9-fN3nN0ico5zvDajE4eIKxfAMX9l-B02YZm1-2Lzz_d-fbysdAEAtT1ZoKWidqCAR71t-wVtcYXeXtQfbdqIg-UY5aAi0eiud8TfWZ738v3-rbNmup95J-1Fe6JgPA8l9CrKBtG1RGlVk2Lx-yUf9cZRMjzIyDX4iAOmW84CHx8ZIXSH_7BDj6PWGAUa7X_WcStPLOG92QZRGh1qri_Z1hAmDFYRVWi8t4FgXBKsxv2FgOlf6VWG2MFXUm0C6C_qJMCczbbZZdwZX0lsLs4x6xuiUZRsx31AEw1Kv6ZONmHpLx7F_U7LNiW19UM6mPULFVePbluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHHRdTIFgR71E9FumqwYrqK55ctAUq3QZxqYYKB_0AX7hwL6BaPY_dNiLigMaTx9SmTngIC_-rpEO1GY9as9KbU2HGKna93vSRiyq70TrXN1vYmQ0kjgrXeJc3qnH-i8P2pgJ8I4btnDmwD5Ta3xkyuk7ItzxT08XrSaABaMEGIQv9cvqQHrS9LL5kibMHg83A8GEZg7vgcgVcKvAkLywH__4OuJonqZqTGdDZiHEcdKbh15u6Y3euC0X_BGFIeYG-VU7DlwFAOIanaHMH3PyDb_5xEI4x8nBMrVr3QnYHhpI_xVrlX8BxnWBK9n_y1FUhr4ktzbaAhsUp7TsPBJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqpBT0rwS8c8zYrJfRD0RetmB1LQBjIA3_7ZosRw5ZB-kHqoWFnbVhp2FMo7VYWC9gQIWb1xWXeIl46a1Kc-5NbD9_ne_RGVso2y6ImLNXxNLpirP0QPjrm12LC9gbv97Pwik66GMpUnNaHMPvmB_TV0bJ_jQO2O_gl2MmDibpieoq_0opyBW4-MFCCqF4HoFpfXD9S2TL3Bz5jt2Ih_iVaZyA_4Xw1Vu8GfQxJ7g1momgK4oti4563ElAl-bwQ4VqWHl8cxzXbK_CBb0cgQvnussE6einqkQj0ewr6dkRpvbfXUWqML-eHlwa7aw0oDX2hX_xcFYe5W3FdDnF-yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVYl2LQl9KmD63vP5ikxA2_cauwvK-o-L1zyUBJ4409QJ9E32_2LexFOdjsY6SnTGXo24Ssm6mUdRF9oQ56ikePyVFIRziY0HpPb5DJvGY10bEXCFTC0E9udRzG6-dr_zntyy9RQGtzRgmtOklY3h3CWdkltpXj1iYe02Re8_Cj_H7A_EYBY7eqgDxkYyFh3j-Pb39vcrFLvMnwm7RxnliF7nfRGvKGhYTFTU56X_WCzhvIHjz2LBlJCBv0AzNVz64zBVoIn2indbqrXhpNJu_1-A1lpYXJSE61RfFgNWxmuoYHdBW9cBoOVqow7jPhQ6eayeWnIQH5LFPlk8b4qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdCvWLbE1sf7jeIynz_YbPUCd7dj0UwAlCk09pHPw1KlzApYWsQRPuHHwVUEuBuIVg0BVByKwVIezhXPMYpA7vOVRmq00MDST-1FO7dUp9nqKkJwzFV_ctLUnVVugBk5GFJGWh1oX85dboZplUZt90TCCWMeeGQ9StgBl8TAGr2j9kMnv2rf8tsiTJsUAxUMUkEGF73tvplia3CwKDkEQFaEkaQfy1v9ZyV3AU6zFBf0FIEbvYc0IIXe5ATrxTq_r3DmV7kgiLXLTHwC5UnVKvZYwX2W4-RTJ6ixwHPc3XsrVX_3WYvASuZxbjUiuLtls-EqYXL7iZ-S0RS9MaS4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnRXMh42vrZyUHVzHslSQvW-gTrbf6eg41Sq1CHUVa-ydnSSwnvlDU2qxkkroNLI5NUE2nWnDMrLoq6G9Ar4YlHLZBbkFAOtWP27Fv09_RdzNOPgoTG2LsC-mg2QAhb53SIPqyaFv2zklxr4-hgZvAX_ku-75KULH8fietMDur9F26lM9DB9HyFHQXNckqnfYeCmKwA8YrqdOt9HWdhwreNckwOr_LkKfMTypAL_RBLmYVwooRh4zR9-OA3Z-vKNSUXWUnk4BJmXha1i7kE-4cHKM_rPWFK75uC99SsEZcaV5zfeTfBETagMzMAwpABiXJb9qWHB9-9KTk3LX3TPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohnPCYgumw_Euy8KoA8Yj0tsfmD0vbhQEB-PClghLSg4lqPCyDsjGeDcOTARTs7G-d-Hq-5lek9ZScM274aeHCX2LAGeuqR5BMVyARCvqZjITVI0WYpWlNBQ4sy3jNOI8ShRzlDW7PpqxvRs24T-tXtwxmsJwPpm78t6qGEgPFlRJnExICddY9LN0R_h0exSVZhS7dHfWuycxFa8HM27s3N-hwF2VYszMy4twr-RHWMqu58i7MiFoE70sdcdLLzAHHLRh18CWot3FGwnD7qnqAG_xvRZp1t4-3q3DeeIlqqP2aMMu7knIx1QrZBAuxwLnUxLkq2D1Egg7KTOdglDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوق‌حساااس
اسپانیا
و
بلژیک
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAaVZwZp7iLZj7TCkO9PsWZ3ehw4ibxPe8ek_WjqpJU_Bao1ODSuAkNqayM_sMUk-CDsv_8NptwacT3rG8GNbHFCScigHKEQu5g29SWnWjhUu6k0SSDar2QhOJcXRgwjWef7_T9LGspZkDoXxxiIRGuSFXeL3eGEA06l4oawz6gdos8iXKmXc3qKMjzvcbslZdsHTtJ5MSt0Y44TgLiUHXITx63p7RjqptrQvTqp_dBWWnxrolxnGn5HJFKplM1CrFIAFmwjDYidjhkeJP9ZVyuiG6aDJqb3sMB815dIphs8IvkB-xoz2D-XuL2CV1xHV0kCopfsGHK6t49Uj6uDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Pw97BBplcLHo85UCDtSwd-aEFpGcY4bDD-Vu6efnjCrxg5oNz-cxeFgGz_P0w1h7ZhEFKfh4AeAydGWqecZ5hxX8EWuP9a8piz2cQL2n8vIV_mrPn60VshSC7QslFf-ONq0QYjPwxiG8tv0FKmIhsCCL8Ph-S95CAMUWmG77mWK_WUcvJMFlC_wcg8tfYfxif7CLBI5_WS4q2UWEfyGDcUGWaiIFc8HTEoeSycNsKogSy0uZ1KiRwyOlhyU59Q5f0xUHxRP9GCnyN5MTzglXqBjfkqYZ0tQ1ZZ5HRXH8sm0SLfdmBd6WUx_oLjRK2fZjxZGJWIFuu-Q-CKxJD29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDt6snOSzH1kQ4wi8smsJGwbBYWrG6rEvBvJS-1c1bvF5uSA3ch_PhxUGjUzktlZ9O97RZxsHGUiS-XsrXrY5deOv5szzjuiVDm6C6YP0smbdg_T8VdzcxjP7nd9cJlzhgag5pK5Hn_XkNhR4cru664fm6y-DgCKCmMGwbOdZf1OGLo5EpqAxpSoIF8tZe-3md-s06I5YInw04F4pj6q2CwKZ6ZLctzp-7N5U027vbYS-CFrHvtLkCgL6oGPzeXok9HKKv6q2a9EQ7s1ebRr04aPQ74bg_e_wMWJ3JsHU_aBSpQrXcUzf3_uX1h6fYryafbmecj08z6kMFMNMzk1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqvNrUWa9zLCqijb1p_4nQM_9R41WWLgxVGo9zW98KWNcBgmFy8xtiUUiR2pHUQylFV89O0nW8R7SmcpTcVkF0ybrxxXcNTrvPUBUyR37pCpNIGQ0zGjjMfBNb3-B2qzoXV4EMWoEJ_4P0VyXj1la_yomAkxh_spDPPCbpX3Isq4j9Ocv2jcXKZW-twEaZgRVNu_4YTdaHmMuYpWcJtb55kZ2rs4Ci_qA-uBbNHfRTc_AbVfaaQ-yRhFHG7ICpgB22NUtNBFnOzO2rdgUVyITNY9oFAvTgvGXAMNsH8ektobksvOaONNFCrrPq6MWYFBT_t4hUNfaPx7RlfTYuvnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGdpjqhm0a3mztTx5vdxE5UTOtx-bvJ4ZCcDm8DQmhxRvRcfVEZMjxaWN1hZ1vkN2edWjLUGXi-9Aqwqh2beuvi2ZShyuqvD5K4oErF08IczvfE44qykW9hUqbPHNPEICC8HAALDTRyfOZT-QxQ45vKRHYH-CHud_kBE4hLKw_UVU6_tDX1UjC6oClSbAk9kRk0F-d1D-qANqg06hKGRalPZi-ARYCFFt3Sh68iB3iJ3-y4LwB-e_xpV5mC8ClpChzXTL7u6ZaPUeMDaRfLNPlG1wdi9L2VL6-PwlICkqVpjGAt7K_ZCkNkqxqgH-P90L60VwG82BYDMzglh-DTHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-XymLA0rXiPAqJw6Vs_eXKndH0rUpsSsqZseVgMAwSYUUA2aH3JqHlejbZ3ihRUuGBX7xs58FMDZTpAqwZjKRPcAsM-k-kb6wZEFrkvpLvFbKtDWAk3P5mt4R-fg32fVmWS4I7vSkvnsE7Ro_c9uaWHOAP6cR_MZAKslb6o0SR3bDX3aqdjt4inr_414p5jHYJ8-__vgP0MDEykCMD4FXnmxIn6ehqIa8agPINHPGuvBawW5VodYZILFJS-_CstjoSO7EIffaESzG8ws_Zm2fqZ0mH5nTpwONrlUw2MSdmu6zknV6xHDHYOflA6SDqzTMKwMFaaL56SnoeKINljFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoohAQJP7iP0aPAl9IBVAb2cO35qWPYby6QELzDjcktNxS8_M60T3SmOKeuOr2V_9JAmLPht7ugoItQn1Cry8ceTaaOBlge2tcLuv5NzO-JnQoPWSVaP93038JJcBHbuAoN1e2kCULv4Gz92AnBAI_mnLZ9k2CG2c21rdsjemM_dIoKVGgwyWANDrHPxDK7PMRRQUkeQ3PKdYJGDexyQDfJESU8iy5GwfeINLQ60IPkNGZO-yp6E5TNQofNRz5EUqVB26dHB43ad9v_UmXZouD-QRAx-it3U9u6vcG9ofkhrFnliaYvk72kX-1P7gkYu8xkd1ohXjjI1sgxg8B9ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPBhKxB4NgTedrBcBDAqyOYGnrosZFtGQddPBxg5ww4iHq-V8PgZXFY7sgI_FYG8afiDMlBV9ddyeweWpw3kxe8X2FOfaW199hn2ejEWoNaGkTvxPUXg9kqN2XVbScxcXuTZkh8zidFueBYrWpB-1VLBOOPGJDz8duyZl1kz2urNdE__FN4oUD2kKIJ-xVP0mMlhb0UP1fMFI9n3csev2Wz7fbN-IBCnzFP7RIPktKONGJPNsTr5vW9TApEGN335m_SXQ7q0ZqdjRxLyz5zfJSRVoB1V0Gwz7XjJtj1UUSLhofapUtE46akDhTyagTUvdEavr3KEXtR_qGrMNFBveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS8kqGmCGSFitjq2PkYKZbAcXsx-KFVvbvdzKABHEcNDfH_eg81AzXtap7HC7mHNvCqurIZvZeg2u2N2H1shRZRwW0ElqMszqgEQ9ocmy4u81PRVZYK6qxDugZSoplQ3ye5FUHQKVU1xls6mWiG-24G0fiUpQdlomzIE8vgI1ZeCYJthxWSqaqNyKUDCiAux3Eykm_hbeAXIq-RKm0LCnzM5zdl1Nc21xAzk0po-3voJiu-cDglfR4bx9izChG5q--AoP-gHLisiyHw68wGcmQ2h_DVE2GmMCgFa4clxl4kzYH_zx_LnuCv8VzaAlg4haFShYmEfrwDLXkleYOEzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHH-3N7JxFnx3c1cKVykcH9XXqTWQoYiotF93VnSMwlIsIyvnP0pIG1W1l_WpvfKUcBOteeYha6FHG1O_HvoWxLuBkdRdwL-FTg2tzDw1PyyzruOhimbkrk6ZGVaFqhcp2KpPuw1itC5PSeWM4uTWbzXQOSaTiYcBn15yjLWDv65-bGc6wHoIv16M7yaI7FsS9eDsB-DwkHAEg_FF0LXBR8R9XcQtdfQgb0Kjv_ru0tZ5NculkAY4Prch6StkORuW92GuEleW_d0LunQcvHscWPLYsz8GpKVJlvIqyCnYF2Ux1fSyPYJTBC6QiPH4Dhja_HN4kuHpqUySD_hr_jv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g252YRA5bAfHj7b4UNnl8cuMncJo97DDhK-PpHV801CN0XU5FJ86s9fxDXdY1hBCUhdNZ2UNsFCHjF8JtnKYEj2xVVgjt6iOdIOEiq77ojSL3lHuLZbQH7c9rlDXvLz-DFagqqxF03R1pSeRkAIW8q7B5vW0fZZunNo-WebOvsSz4AScKls30l5rsX04CBjT6RMAOvzMmKBlkWHlDY2pD6uzGO0RZRB3eqnxtAiGws4ec4z2bSUC_PR9NrpSE1xhKjj5EPtFcb34gf_CedFe8YYRT4NyZFViz1c37CnpMw0cqeMrcBjPY_w4g0QPrOd8B7y6u7mcABf8vCGhi0YuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgOc5tH7uUg9FDS70h_eB628niSvF0HiOROYJIjweehZZqnWbkCE8mmz_oGN9GvQ3GL6Ie8ACT9C8TjIWiFzaQmgCQ-0XFSK_00A_sQP8St5jWZfwpVVOckdfF8wh0RfTOe8exg2MhvE_yiEyOofrpng04PSdaa06XsSRFghLcxDQHI5osWu93ADEUz9YO3fUOYFJ90-1GqB_VeAF6yQ2WJBYz3FSg5bMJdJuV4goFMcirLpYl1-qkUJT4ZujFiHDnIweRB7k9LLYf5Puc5roJgtI5tLQvoav0f0hHeHxmJMONZVkxuw-zJ0JNZRD24E0C-gSTUCt_Ng6xsBzN0Tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-6AQokar_56slU3tcP6jwmU3eqMHAQwFNoXQiWDYe66ZsfIPZ2xLo44deHR2U0ER-kqNZYHhPLBv8IF90uy63BI0b19wmefWQw2d0IjcUWsSh8csv6ZGxHc1dU6b6wy5OLeVO2WN-187oT59YkE908tVjCKoykYWMk0MopCg11Nn1hAw9HpXbVPZ2aFkQWvinYlbFdeFLOLbgsM6Z9zDc9YuOV1uxugVrweMkyIttndyGBdtCopdWoDADAEFAvX06pjyUIcX28GPPcJJEL2nJJZwZafD6s0RGvkplSHtQOgK8QaUVGR02d0T84m_QA5zBTzre1DFNgrcDWmaFeDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eir5WP78SLV66KqKmPLlKjCb-2chd4QeNQUbWLLkBRh9ddDjuAFc5NH9Dr_w91sASmQILLbYtPCvB4UgRz9i5cPcjOpJulGD5FwHaZ09_3HG6LldyEzHNUap6eu3VJhw0iBJEUpHOZIB7AFQyEUPx2QeJWp0j1CE42zr7VLe02IVKeHhJmRRgg3Ms7qUYPeNzJd52rtS_PsjOkuvAPxlZuOL1YkrLjBVwQPNh-H-nwKTb0stXzcAkwnzHWLyaf4i10QA02nvgtla8Y4LZc41EgGT74SO0XbTX5vsZZqD5maKdXM5g8qrcwy5zKeRd-UL0Y9rRMoGaByu6CBos07PSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEsMDTCOvHB0IiVDJQUrQYDBHHDQSuNM94AIU9ltORnmGETvimdMNZ7eEEfZ4SlUA_7jG9DLf03PKbZIpmcsS-U4Lbx7iwVVFiqNspfq_EUq3oNaZPU3zPEU0UkSgbT-3bHZ_yXe-Rl4_x5rm0SGE_g0cAH39LrAsIfs1bHSGQOzhhUX5fzSeqd5iFhW-Tg0_zlbfvhlCaZ4Njbvwb253u8tHR-KKsxrQf9hzxKe3ksK4-qyrSKaO8CRKmmh45pNksHmBTUgPzk3QuTNIQhUURwceP0RHCG04rH1sK5vtFrqN82KcD7-pi8GDpA4Ul4e7D85izw08nOfTIDImcyVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=XVBUj_BTI5a1stuCJcNhMfH2kFlOXHC8HKnN369Fd0rPUIZtv_kpaMbyxf798zpK4ueOKDIIE9bZ6uyxdLoPsOY8NoxZg_PdLE3YMx2KyWjA-3Zs2XTP81pLCDBaykCSFaqxgv-DLhgZ63y5u1_bvO0GvJtJIp_dLj1uq4eq1tDcUk_C38tAltnG7xqNqHiBeQUYw5d2fVB1S2n_u-U13pRxcz9ptyP0aKt_xc1-xYdpKQqzNv1h7K_qW19L8eHjKjDwupb7W1ij5WsCZuEFqMvkLNF_rQIdA667DTn_GRpvEvwejcLokqXqM81aJpB4n0s22_T5rzG_0lSxeAWa7V999WOtcIy--1cgbMvFLkq9TQhQ9e0WCquz47zvT3vkYzUvm5x8WB5V_NF_tZ7ZOFNyBKJI0Vuc0R_DHmQPtyU4w14P_chFyDpxoZKgEr9kgKIFh5zX44EDTrybD-2cum3Q2CRzAKHcjwH7pvh50iNsn_P_qxrd6ZnikaJuiDmzrOEqza53F6akTN65M6436WYfeXS49bx8TkN4yKxF3_Jo0jlfr0a14jJJ92EmD2yooreUmnzKcxBjyvQUnBCoxkBn8oPRy8vIp1LzjkE3rijSVSTFwFVFaAbpUNvshR3WdTo-QEUm8OGQl-OhXkUj3XEHBpVVg40odzBQew3TXgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=XVBUj_BTI5a1stuCJcNhMfH2kFlOXHC8HKnN369Fd0rPUIZtv_kpaMbyxf798zpK4ueOKDIIE9bZ6uyxdLoPsOY8NoxZg_PdLE3YMx2KyWjA-3Zs2XTP81pLCDBaykCSFaqxgv-DLhgZ63y5u1_bvO0GvJtJIp_dLj1uq4eq1tDcUk_C38tAltnG7xqNqHiBeQUYw5d2fVB1S2n_u-U13pRxcz9ptyP0aKt_xc1-xYdpKQqzNv1h7K_qW19L8eHjKjDwupb7W1ij5WsCZuEFqMvkLNF_rQIdA667DTn_GRpvEvwejcLokqXqM81aJpB4n0s22_T5rzG_0lSxeAWa7V999WOtcIy--1cgbMvFLkq9TQhQ9e0WCquz47zvT3vkYzUvm5x8WB5V_NF_tZ7ZOFNyBKJI0Vuc0R_DHmQPtyU4w14P_chFyDpxoZKgEr9kgKIFh5zX44EDTrybD-2cum3Q2CRzAKHcjwH7pvh50iNsn_P_qxrd6ZnikaJuiDmzrOEqza53F6akTN65M6436WYfeXS49bx8TkN4yKxF3_Jo0jlfr0a14jJJ92EmD2yooreUmnzKcxBjyvQUnBCoxkBn8oPRy8vIp1LzjkE3rijSVSTFwFVFaAbpUNvshR3WdTo-QEUm8OGQl-OhXkUj3XEHBpVVg40odzBQew3TXgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suv52guRzzrHTZJ3q000nmxn318F8I7Lfp1E0QRiTggNPpkAFR5Iv0IEpHlsRGwxDB1zuknfjIyzj-tEXb4kMnrP2j_SnOORs622kHTQI2q-9cScjOdlDGoqx6lGRWoRxbH_4Efgi9HiwBQPr40DQRqaaOm6ItGngXAIWLdrT12hkPT52jd9DB8QsTRuROPOeJ0w_vAg1CajaFkwgoVAben3B2SjH-8W0egt8neqSKaZ9e_CNoLGwecOTVXh-wKnmcL4qCVxLXAV3J_A3Zi_sULxb3bzqkX-NNkKUmONCBZDeEXQImNdwP1AkpfWVLXS-iZaCbWl3tBbovT0rIjevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY2zGWwDsJ699hCuKlq_vtY8J3lScA4WD5WBIRfPe7iatgF4xLMxoxCF3RRQX9q29e612fqfWy5SRO77aEpT1Sxje8QmemQeqsjtYT8W29D0iBhtAjKE-hIWLqOGxVT1RPCXCI9DT5UPoO4BFlojHZgsHEeZLTnah8XL4Igetl_1gAYjQ1oNCFaYEDYSeOO-E1M61_BbpGO49VeIoWffsuFaRPyz69jdS2LgWusVjwvYAlKq_2AvHQ3NtyBF_JCCE7ayV1QETG_Hf1tWj3VyNb4m0lK7eX6uJys8W13xU0_4KXRAedm_4Hb6UVxQxPO9QMzW0KZKMdxEoEF6jVCyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3gGjSJ6arHUL9-PRVYJE7ZuKIMUGbnOX5mT_IwB5AUdnOe4gCMEL7yRMd8jr_etPbdvjcmBgYDFA7i0qdblZT9slcX7cR3PbRtXj7p7sswRv7thG2NXnHP185_SqPvB4LruZz8afziy7LmI6QZYuY1agxgNCgoPxTTf1BvrNINOPRQQhD6z8kFXuLkWAjKAnOUt9Lw0jvktcLFOq1ZYWSqfNtbqZjiwS9QmAX2g8UGZorT_XcRblDs8mOh26DShPlZOWynwzoPu0t1q7wkVC1Z2Qde6on24qe0sFbEDN4Q8Mvdr19_M_by_Hbwg1tMMYl4izZ3TE637oOccPEktGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=niwRqF_o7wA_bRbNJ7Zv4KepJqyMzt6P7IB6Zl6dXhlvhleZwKLaorL7M2iRvPGAWw8-UlXe1_ZgOLCqW6rEJM7_qmc_69Fgx9MD-m7PlCMr_BWU-e-o7yN685C2ZQO2J1aJMoDzC0xAA-ep9YBw3RMTBz5-p071pSNhwM1Cd0gtxEGfPbpSJEA7TajIIYM7Ug3ZkSIQWfbdPhFHzWTFp8-tpn1EPRbWm_J4O0Ezh6aqDADrLmLrD61pcIC3FgSSowgTWztsYGkssQRq33n0vS2hp5DHaTEL5hJdMiVMdxQmiBkSCYHkswNzJ-uNZlKktjLqjLyHVyHBB2bZ1ktEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=niwRqF_o7wA_bRbNJ7Zv4KepJqyMzt6P7IB6Zl6dXhlvhleZwKLaorL7M2iRvPGAWw8-UlXe1_ZgOLCqW6rEJM7_qmc_69Fgx9MD-m7PlCMr_BWU-e-o7yN685C2ZQO2J1aJMoDzC0xAA-ep9YBw3RMTBz5-p071pSNhwM1Cd0gtxEGfPbpSJEA7TajIIYM7Ug3ZkSIQWfbdPhFHzWTFp8-tpn1EPRbWm_J4O0Ezh6aqDADrLmLrD61pcIC3FgSSowgTWztsYGkssQRq33n0vS2hp5DHaTEL5hJdMiVMdxQmiBkSCYHkswNzJ-uNZlKktjLqjLyHVyHBB2bZ1ktEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkewx0iFZ-WtvNQ6Yb6pq4Hp0UZHQf7ZWsocEeZ9apAgvjkIps7DrsigyW5D9Pxjtu3exE7NqTteJEL0Tfy2tFMzZPFpAAO-0RO7YAxzizhj5FtWkWtOkpvplUQle-fyLKtWRmX60ypt17l5iP4DRdpQcsVsrB0GW2dxEKwyPNZ9pL-OGjOGnRGp1eGWEmF6uLnuC-iSuch-DuenKjXV9giVf9n4KsjvWXJdxVoLDoKQmHmf2EkVFE5GxEfcBCun9ws7p4oD21KCWi6x7I9fLEHifCLYJDFIhqwCeCwYjv8dtMPTFbWoSf7HMyd-RZjGdrqJuPyIoX8W6i2Cjirwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIAVdBrG-OFGnMKVSKcD-pfMe9ubLJBo7FcDycvs3cxbdKEM8rwgsMR7nRn_v6rGzSGrMxRVmragoKAB2_Qh_E0JJHh0w4KKd7bl2ktumC2InVQCwX3j5ImwcaQx0UXNpOmp-Dab9lDI4og3eHclmBtn4tLndwM39171_TtoQ3S0PePWyzhkGlqlYiMmDg9UD_P8cmB5SQgoYrUuMfInEGwuk7gkqOmhiQbQUjf-ZWkO_WLKu96tkEOMADKAq8zqdl23MPv5AIH0GEHi7A1c_l3--2x0AGJ6xG1g-tk60pc8bstNwjjXYxAGWidq2Qmly3jMOtwLPeU7nMwsNhuBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HE7EI7aMnAhkoe3YOoxrI7UfrT6R6TfMLbdNGADC2GOBX2Au60fPUoemRpRQpQCB7FbLzxwi4sDmC6R-FegiBFlcgRcvm71v9XTwz3SSBGVj56f57Oo8WcjZl6hzFSM-EezRerAKeTdCyW6tFW67xVWxZpO20JWwdKOFWXly6-c6x62rI21oBA-5owJHAGehoQv8UrpPjc3hQVAH_mAbxAwkV14KhYnhs2mQLZUJShPqvkCmG1rUTNsNCMpHl-3lijzsJf4mLGwiI0bx5RzZ2XqSm5oajRZJ4_W3-d3dQrdTFygCTUM6vmwyI4Bog-oNHOQwvcj5QS27wpYAcss5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_kcvjCw6cUYmVQGBwHnYi3y2aN-RilrXW90JFsNRV5gch2DY36eWk0mRCosn-K1_w8qDcmZ6z89JHwGxRQg2Ealj3fak1MwVFuZboGQzlhvka1cvTYGIOjvkkduU6Shn_eNeyLOkGDLmHUiOTQLCeU6Ukqcwcxhs46svVIOt4ZavSyAW_QxDFuphZdBogjg4XUkaoSrADyam7261ktF52GneF5HHGi-IxTFtaWse8aQx2KuL0deLXH7Z-MtmS3x15tTeedz8jeHsdhoeXT_5Qb3KrnzJnWpez8q4BcqFeIIcb6drRDHB5NXs-jCw2yUBc16B-xDtQmnN4c2rHkUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONwHgwZRbqePlwUjVICJfe2ydxODGv9sGFITgBFjfiHofbkmhQ_q1kVnQPKJeEZKZ0jC96vZtAnr1dpSitBR346WNHUlDmBgAB1_IVd3E2htBP8HLhRSXfAWp68dDOKIph33yHds5ekT_-SM0dHjkNrKHA6zn79_xHII6NMTR08eIeQlRO1PSDB9imTOoObtnLKETjPkQoMagj7c4LEQhJmya2V7Yy-GovJzHMHrIEnrX7f3jq9ww-TavFmrioKtRJE0rwaGV1qfW3_PgsnCES_ahF11ZL9yqqv2Cr4XU12sYZnru6qH6lK5NcD6wR_6Bvh1m6Mrqo2JuKNcNmyR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRvucNMttN1Du--kODlSg1ZJppshSX8BZLZn12cxUs3P2HY5pVxacemJelxfjJlwKkNjF86uCo_RUFFYa9P5mxydnJaFwvRHvPC6hjD5xb-iZ1OHcQ6DviP-VLoox2sS_-wrUtd91Mx5frWiaSTITyQ_1FAydQcywfucj_Cs_h3FsD5YgPSyAW47NOQ_Ho7ZJMy1oM3jFapbmsBIR6JnAhxzDdesgMfO9lmuREDAKHDa6MD9goBpCVjMNaCNqy2n9EncN1MU-7uI3Q5BPI2gqg0_kmKXr3V0r92ClWgXpCLj5td9kWa4D1LxTl2WSOzZS8dVUwLFjTNiKcNq8YrukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYAxdMYgpUArxU1BjkQgyaDVmsrhdNrHZnMVDRShwIHAROeaUvsBkfav_oILYqQOafZOC6aBRTlNv-4AwdKrlmEeQAY52boLfVdpkd_DDAUlm9PHv2UC9v6P5Lui2TbvoN8xFaYV_cotyJNftbBGGiCE_KVao5X3S8SZWM3s0rLS2yku3oAfOFCcnEplRsnKAMzX6hF_0LZwGpxFD-mS4_12QG5msM3WxQLKilLZaInS7pbq0LF6PQwUETXwTWY_Bw9HeeFa300_zCTu3DtjllSCquhnvXVJFYjkFNVGSpyMDhLgYD6VMGjH5gCiJwMVZ6_nhDkuOYclbvj-p_LVLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od8HOpiwAE4nzSYGn5aln0VNiWjuNIdBjNszJVm2alyio8bHQPrwOWj4tcDRYUy-EbVVerOzZN73pb6RukyoumGpB7muIg453G1_H3HxPs5QpB8SrfPhD6EAfKsTooXniQDh1HtIVcnXlTcEZq2FmWMkXlvnkcCltGRdagB6gIcr3FVBO9KJ0akGQPuE7uD-dlVHUPVtY9_RaNE1PKyLev-m_N-x8A-xrsNosU97RlR0McOJrD9I9XhFPtnmdi6sOb8EVV2QzMZbK4afM7KkmcmcvXPnicVzxqVzZdjzR31WCz4HkFL5wLt7bHQL8QIPZBkKj6nnfY7S0tfdOgo_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0zyAAb_5oJZiEYXskJ8GrCeNhaWnj3GgGjibTPGiTcZzGGRJrGfYM6Mm_1UAlNWiQ06GvnNuzAPrhqdQ7B3e2bAO8z-enaaXw4X1YbM_b-kCwwkD7Eic4PjZjB2IXDbIykSSo5l9m0mD3JNkHL8RA5TamFOdwrrSRciez5ravhckO1VV5aQWg6PIPYMk4gcA9ljK8otttLpdgajD6zCSZ6a-9WtR7GE7iA8Vyda4p6FiwmjS1uZkPulPbHQl8TPSL8ltruA96WmtQmVXgcWIs6tU7AW-JdOW2vXLKjwkRVHtQ_B6psJAe_8YvCDsyYouTzXwGhkNnegnldVcxULJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUWdC4sTqmvgnlo5UnWq3dvDvLNCCIprA-zf_AL8LkeGM1a4AfNOHvRQ8B0p2iOLHynfOfUoDrAdwdFlNUGGSNkCMiDZGdYXH7YReC_RlkEgDs7TB4GnAuhhIkfKn77_UG5BZYOuSg-4a2wS5x6sQl7qhiRdQnXoKOhpQZFQEK641G-_FdEVEm0jPhqs6T0hMRQ6R4bXJV6Z20rRpykLX54_2JzdPo679BAHrAcZXtqJyWtVrR8PBu-BKvGkPaMp1FmThaIk7olAs0hpzJqijanc8X2zMPSTWoFDehCulifVxlWYHbFTUneMLf3IGaAvbSIP9PQkmlqFOvUwiNC8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAdYW3-_tKlZ4319V2mfu3fzwp1H92CtmUfd06-Mcp1xhXeHZ2PtxJ6nZdKla0r92sfDXVhvnTyE1Blj8RQUC16eYZyekwIvFq35rxO6c_sdIF23t3E1pn-ihEkeh2Gzzm9XHE_FWsb9bJibRAcwIzksQvpYL-gHqCu0Ki-Bc26JcHyby9SB3axt_tAVyOaJo9pseXTTP5_jDWsge6D5I_hKfd0E5cbYWUZVTQtjqBrsVInZqnco1TAOu7mZGPXnSnriSo5m9QuKlT-Fu2-r4UZcb-KDAMrRhJsPKCKK1X4p41qyrVHZd0p_d7aMMEViWetxjtwx9EuBnx1Fwy3lzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjjPjoP54hjERPxCoTE4CRA6UAqAFVvUMFLIGAOEu_zqik7Vg98UZusPARyANuqnn4gywfAy50bBl77NBmbMJGfMGo20vtT1GjZoWa3EUQvLZngAclmpYTjOfiTLOqA2vK8nwIA6ArS_5uMUEGmmbmDh9ztaqKbAyclENov9Wpg7A-eBFmWB78VDxzPMpMf5zydlRVn3FycQkXDyC4J5U_yqyl08rUJk8s__8G-3jiJSacFv5EHT_5jghraA00iXdTUjcTdyAwz4iTfe5UY9SNKBdCcGkmxhVlVR3zs47ywBoo-mWnRkFhszXcHlcPx5XjeSdF97MO-wArDQXOMaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWWk-Gc35qccvj76yVTwJtMAAhjdtpJkyrlUDDnNoBEyN5USVylGatsQ2aXrOntQuWdfp74H1EUJnJDE7CMD_l-odAMjyYr9xzvBSBwsi-AwfXrSpgG76aqzIWGRQ0VzduqJ3snhV6huVdtGm2gps1pNl7Ec97Qf6nAHdiRB39fnzZSt5L59BejiGalIlSVsZ2jB9xTpKs2Wzp8LgHytZNzetA2D2LmUvn-P5y5jIuk84U50AvJvhYCHeRsj7raswuOOy3xlJz_cC1PBeBD5ue1oqiDcA9UjMZJqKOP93yquBfs8hOXNLMPfJ6yEspm8V__faTaRmyYZP9v0rXnx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVBaz-dAYjY3H2VDK7kjCkNu3x1-EG4TdU0wdHYqJM0z_Z18ba0-CwXQNC6VBBHjNCpfXFB1LQaPMjtvpeEfeKGfO50uUzzXHRZUsLPB9o9DPOysmev1OMwGuqUgCa-rwj_sg2OiqvXCVReSqKZxCwAhK7JruKTQVTTZ5cKBAjZApJtGg4Kqhis5YBfumMLn7jwncMrcBhwTrv5cpZQovuKB--V8XVtBYH426ckIVsW7jpIkoEpMu-WOLULzmpVa5nrojy042pi7Oy13EoKd8PCThU0H7gJ7ezqN5SssppCny5dQLsuis7g81H5YYqbulw0MTFY6JT76Y2EfnmkyCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEz2ijwBNqWlwki3jsX5mS6ksflzGU3YQzztgyxWUld6N6smG7w5fmhIgDE3EJFGwGa46ODoKlyiiSmfKFKLlQRvFX3Ee3Zocb2r-5rkgKDCQpsQSQ9WM7CnUN6pYBgGpV6q9hcbn-3KEV_MqEFlaboV3qMLYKYcVMN9pBZReZuGNuSWXw6zPAB8W5g8zybT4M4JxWk4navBYi5TCTlCMlac5Pf3H6eKITwZ3MEbMECxdOjpFv4BTVr3KEJNIMYF07waTF4dZhC8MI9LIVMmKsiW6bPc9_-dHcd6snnqx4sINrbz0WJtL7sjTH1ja-ZDLyWpc4mTJfKF6feo9sT_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GysA4M_ntdmxLXxMh1TGA2io_2-JvDMVH6omFsnueRlncUJgvfzAWNKql5BxX7G2JJkVf4DypLzZi9ilePZihtbpVwB9KBQnjSUhShQt7yRjrBvXn9vottb7ojrp8MRTIIzx7JoIPINgutJpJcusKvu1AayKWaeE73YIlBCLO2ImXVwsNfvyzWTudePqHzPIz16sl21gMHBE7p3-9PTXz7fFkpgNFZvxw_EE1-S5DrVMkZj8pH4zcvatJ5MvZSQ8xYc2ahhtJtFYmj4Euvb5fUIT6mR9LWWG1SL_5POqSh1Q4YPy4zp7WwfG4KlSGCiAMSQx5sPc9l-XrOVRyFEhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSX5MZdqzvbUp_6zfKSiLxXSV41cWDAs8eQDjTvRf58Uv7hz1kELzOMI4_IGJaUHmyqmAma1m5xaZD3TPvLxxPR_VBXQb2EbSR15n0FH6G3SNQ9TQfHm6sdKRJT4_0yufbh-O7qvgsh17N--P6Qr4JzXiJ2al8FYfPXZzOOITnux5Y0DDkdCTrWRW7Kv6MIzCf9ZoA634lYQcnPFFEC7aO4Q89ZA6e-uP_FRwfTvD4xPE_eKyoAiGEQjmcZUIl0qn6okNc0F0BQA-Ty1MQRPfwVki_0eYCqgFBOFWBOAGy4qxNxlwocNkalOzc3k9DyIwRjummszlgbAITnAGSryxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulr-PzR150QG-1ypBuA_kB5jy4tVhKny9UA4ATAxK7MVc5wT8x55hcHMS4axWhhvQ4EYrTgHmloMex0iD5Z29F_lxlpVlPhzsjWT5eVauL7XGLlNUxDQEBy-fxfpYzEQb8W6-6StOX9GjkMM1MQk4wHvbwJgP9yLem91KgfxY1Sj00nIH3ro7xQU4tB4iSqqXoNs5Y0GYT0dPRHAGhR0gvfeZqCNkQsr-gd1TWCssumR_QMIvKJ3FEJO6zQHr0VUDeT1YMnYjiN7nCGDl-uYd4dhEk-E8VZGgAPPUvTdBeYLiseJKahjHc0aECvwu2DTjqPvn1yq3Ox3Wkd10nQv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLgRGpRAS5mI2259wa1r6UT35yycTdMF3S5AtCJ1js1rdChWQ0h6UngnjQ9fKUzkJyvAmdZU-dzf6E2animWmNc5OD3kATVJGCMrljk7cEQ2q2mnP1w6d-iAU1xFB95RYzEuZ0A1lVSK8UrHNfOJ_8XRrgMoyaCUCztqzo70fxKG8aQ6H81_8mggG0ELp8qMMDhMajX1EA29e0ZsZFwQqnxr2fzDacug844dJ5liGL6Ci06W2bMV3G9JWWnYRJTuYc_KdfZyaS1BGAwwdfyYqCXwyWUOlv1i1-AysPbvwgioEr_urYFw2tFibCP9j4mgAO9iYNHibVR7SCN4m5ruwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=KchJiMB6J1RPcSv6mSNXTTPbbI24VxZ7bEUC9DZeSv7T-Oc548D5t7EoKeDW2dlmKLsAcKmPYXTEXSzg8MDnPmzinmM9Fr-9EwguDiXx87fuhbnaND3kdFJJpTE4IZpoBmeYagfuG-iBBt0gavIqq_kYX7kvnQnDnU4dGSOdm5_N4fUi2_BC7IgCOIYG5_dkW9GSnuOlJrFbv4_RMdo6kXqyDEyH_Wct3LhNL7_iJZszjsNKzYdUzhNudds_d90ZUoneqZH0sDbKnqzKqOK2CAUXKdOdM2d-4bCftBIHCo_fYei7WKyLa_uJ_wD1lHnOEyCuhH0EHmRAdT66CPR3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=KchJiMB6J1RPcSv6mSNXTTPbbI24VxZ7bEUC9DZeSv7T-Oc548D5t7EoKeDW2dlmKLsAcKmPYXTEXSzg8MDnPmzinmM9Fr-9EwguDiXx87fuhbnaND3kdFJJpTE4IZpoBmeYagfuG-iBBt0gavIqq_kYX7kvnQnDnU4dGSOdm5_N4fUi2_BC7IgCOIYG5_dkW9GSnuOlJrFbv4_RMdo6kXqyDEyH_Wct3LhNL7_iJZszjsNKzYdUzhNudds_d90ZUoneqZH0sDbKnqzKqOK2CAUXKdOdM2d-4bCftBIHCo_fYei7WKyLa_uJ_wD1lHnOEyCuhH0EHmRAdT66CPR3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=Kdtzdm9LIdXNrwT7KOD1sN0p7L26e2TY9hctw4rAeZzZiKXcSeEcsFHt0KUvqgnuFnQCa--I6AzuBYQq1v2aQ0Fv2gdHedWDbpnx3qS3Gc6hCv2sZ511sO8K-o06LgJoOvXe6857pQ-lW3axf_1roDkLBdAdQLjPNcZm4cEy5HSgEZ5Aoh0xAPHd8RNxixlMXZkfdJKd2yzWgFIQ28mVZKedY1VeY7WMY2velscvtrcaTXcyMLsId5k499w_wfy4TbFuw3SDD8NMtIO8PuAodxXU6hc_mxer1SsovrmT6GHwqXYA0MMcNorypL-bSGk9jkozPmG-1K35vxdnMirgbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=Kdtzdm9LIdXNrwT7KOD1sN0p7L26e2TY9hctw4rAeZzZiKXcSeEcsFHt0KUvqgnuFnQCa--I6AzuBYQq1v2aQ0Fv2gdHedWDbpnx3qS3Gc6hCv2sZ511sO8K-o06LgJoOvXe6857pQ-lW3axf_1roDkLBdAdQLjPNcZm4cEy5HSgEZ5Aoh0xAPHd8RNxixlMXZkfdJKd2yzWgFIQ28mVZKedY1VeY7WMY2velscvtrcaTXcyMLsId5k499w_wfy4TbFuw3SDD8NMtIO8PuAodxXU6hc_mxer1SsovrmT6GHwqXYA0MMcNorypL-bSGk9jkozPmG-1K35vxdnMirgbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=O1bD3OSTu6-8uddFZ1RIRInJ9ZcHH18a1d3Cz0pnnZuAc2MBsPgYX2yI-wSWSIfniZ8BuW7BZE5k4esW-YmUfPWJQpbvTxAneTS2Bhn-PvX7AKDNoBLsVEAy4oFsXYeJAij63wVklT1XxEG-5UNW5uTNTReSEfhwSGNld9DKVCusBTx-qpLe-v9xu12HNALyGPPjot_2JwxEVoqUIo1pTLJDkUvzvATseyTsmneXg0yiJP-VlFgHRkrfTwadLtg6FSFyIFapSAX1r2KtWOdj4-7Dht05tuLDfMgEUMQBy7ZQboAXPm1SFl-2wvgdk8RYhTh030YkAN_6ilGVtbXC_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=O1bD3OSTu6-8uddFZ1RIRInJ9ZcHH18a1d3Cz0pnnZuAc2MBsPgYX2yI-wSWSIfniZ8BuW7BZE5k4esW-YmUfPWJQpbvTxAneTS2Bhn-PvX7AKDNoBLsVEAy4oFsXYeJAij63wVklT1XxEG-5UNW5uTNTReSEfhwSGNld9DKVCusBTx-qpLe-v9xu12HNALyGPPjot_2JwxEVoqUIo1pTLJDkUvzvATseyTsmneXg0yiJP-VlFgHRkrfTwadLtg6FSFyIFapSAX1r2KtWOdj4-7Dht05tuLDfMgEUMQBy7ZQboAXPm1SFl-2wvgdk8RYhTh030YkAN_6ilGVtbXC_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq22wfFuj_UmYQMI-sGfsVyEe5xzvHtPnsxTAZ2oijZrRHGptIB77XzzwqwuskB0uqjFXDaPabaRjV9y1wx3aEWG88HzHJNX162RvCbLJTRDfCd9gqOLefVtZ95gACcDwKNKE70zgiSqJyzQFKxtDrvFUi5LjZvJV15efO-7LuNU5g4SfQlm-dZ90J6IK1MXM4JEM_iz2H2Eor2-s0LP87-KFGhkOboIComGymukYwMfXm6782C_9RN0Lg8d1qaR6BmH5oAZ53PpX6G5QBZpW-tS1GyxjZjrmOKsWfjYop68VvvKjFu7JdFzybp3y6214FEI74Ddfu7tGbIV0bPvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS7w40y0csEAaeLkgwmmX49gF_RQJR8Gq7mtBeH8a1DUH71Tr8dVOWt4pl90kRmT1r8d2mLpgxov-wUJuWvksMVefetYsI3iZNiELJoVvLWCLB_4KVLaEWuDwlGpFAu59IVCzpCQxMmqkdVS3i-08cwjNdmWx18zKFdiixEc5EOgvxeak32GJZeVUCFyH7Lu3pWA8yQUtkYRDi3F4w_hgXaZlA2IvJlwkbH-V-lzsQdF42DUZBP70B7Zemijj0RO6QPCOds3fy_dL_yJ-cDcUFJ-9713aRwsrS4bTiy1O28F4C6CqFzTKX-QOv10niN-gY8baBHesrd2N1tL0u5Opw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=mg2ONLJkrms0Dj1sDKng5E-Jz5qa1FkW7s7I1aY4SlNm3FtxolBwu34vfAw1uCjJRI5HfRqhloVrmmoJli66oRx4U-JmkMK8_AQtu5dAJnNz3BQkxxJk7L5pd31fCUY0Eqb20cc2_GVHGYseNErWh8Z7ZnUDF4reAW9VjLHLo7G3cjN35r81lwwttaXnDJifZP_47bz80d1YdwLOzjIOsorfPZ90RTCmFmoNgWyy80yAQaYW8LPPcJNoPkl1XtzJZwRrci9mLR0R2194d12REVrfs8U7X5SoHoQR_DOx_WZD8n6bw6OtjOYvO0YF5nkjTiypbXiunBxeCJe2MTM_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=mg2ONLJkrms0Dj1sDKng5E-Jz5qa1FkW7s7I1aY4SlNm3FtxolBwu34vfAw1uCjJRI5HfRqhloVrmmoJli66oRx4U-JmkMK8_AQtu5dAJnNz3BQkxxJk7L5pd31fCUY0Eqb20cc2_GVHGYseNErWh8Z7ZnUDF4reAW9VjLHLo7G3cjN35r81lwwttaXnDJifZP_47bz80d1YdwLOzjIOsorfPZ90RTCmFmoNgWyy80yAQaYW8LPPcJNoPkl1XtzJZwRrci9mLR0R2194d12REVrfs8U7X5SoHoQR_DOx_WZD8n6bw6OtjOYvO0YF5nkjTiypbXiunBxeCJe2MTM_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNQyl2y4hO5GttTTPTplbWDrmCy9h03Gy15GVnkqqIWjHLOkcc0-wfmEqeLcyYXP5pjcYpKQQK7bsVWochtilyYzwFX_0-V6ibrYNbvhp1zqxv0TjfcSW61TfKqvklApBebdLTKK-rmkhhYXTWGrNkw02L6UkvUlXtAtJcc9QTZEe1gY8GeWJ2S1QJQ1Ur0aONLpJRV0MoGGqbdtDSkyhV9sP_dFSrTblo5SZ4aOb7LCWdnmzmfCUtVI6wNnHmGy4Vlk6IXSeBu9Ua_MMNyyepU3Mm4dh3hGiVsvlcpl2vi2dMh0yZXsa55oGQdOEnHq-FyLcjrtQk9whbfrFiL3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3d5XNuyV3ubsgLOiAAJuGyOqEj7gEvP0FhpngR-z3WqGEeiiLyDqC0xHAuiJZFb0Rlmj5PCeb3BtJ_6EEXKMJGGtsi4XrK5k2jOriZ-1DZHbmHU0lurk7rGAKe69kyeeNtTgiEWT5YZ57QWcMPy4_wRGZ2QdvAfWnE4BtqmbwGGx6KX1NC9WASKBI_Hk-SqGuNYIhGUmY22qUBrsbNR9hCjDFmkOGVkiLVJ_9Xdaekf-uzBzZpf6w2pXMyH5T4JzhYavRXJrv9U4ntMS__zPYqi92kVBa3Tv0FI9cfGhrlIL5kK3Np7hP58WdOWxrVuyXz0WBgvfTAAr8NSfvjYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2pncAOTT9B1e_UWKwbtQQe8E27wopzXtWh04OVs1kfYzd1JB6mf9ivH2Q_aKCG4bC3qGrC_RHA8eHgtLOSDCv4gvdldo-C6hbbn_gGUvUqFcITrqeg1AVraPrrWQv53mgs2YhCHSN1A2WxHa_LpHSLrdGXZvY38yEfHIRCfSZesaSKgFFASAEkAw3MQoDuaWGNqALSD045GIC0nPH2O0H59F14HZq5WjDVQ7s4U1d5iSt459jCTIASIYFjTpJlRYfWfOlYZrd9aDSIwlFRSOFNEf2zXHUKUW-AF_tEh7EKsAduNwDENPZ4JZledoybi-mOie24Afk5wk1eafzZlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiPUzQpTxijpNl2IHZ7Y4zudFKGBKW7jfPQWU4OIMfEPbgiFc3PxgGrBMHt5RgQpDd7qpJYD5vxcnUD0prTjKValJHspE2RDO3UDQZdjOnaLzaIgLGv9onsHfLyhEbadfs9nXWjBcEMLzk2WyrkeNN5QuPEyBV8r1HFZF-dIZG4Hg0RTcMYmJd4Ur1lnvgrRMuoy_G4453S6rVH4LmI2iayXPFQ7mSGu7vtVtO1ZWtXG2cLP6FI3u93paT3GP_MpH3tG7W0cLP2XUaLrh-3Rwirv9HRqSqbghX_nAfPheWjBxL_jFGgO1FPjNI69-Wxwgwk597QtASrk42TOXwqAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maSLezVX_3eZN2iTZjYnrd41qZYHVKIXa_gCJc7SvNvu1boZIQAWZHyMwvirBYmAgFoPNkh87WWknBnm8lmOJRn7RevSGzXKMmm4mikvAf_yIW1Uj3NoGr0ZJltD_XfW08fR4kb_dcVgLAnS5i1_wrTFAbiJG2_kNq4cL8HC1sc6FJBaZk_ENqLahOC0cXKE7wrmBGO5MYsC8ZQKQ8bMOtMKysPaV6_Mp1MHL0Gt5WkoTlseT58hDpssF9ikmhAyN7ONWnmaefFLI2fvp57I-2KlJZLitnB1W6ClRuC8ChEwy2wPrmtjGE42vX8681Ee3COMeDewTTWUNWrHUmf-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q00lZydjgTJrLLfjo5kLg9B1Z8iVKaF1wTRQ5iOj8pOoK8lngxBjrOPmXOIvh15TqYSkXPf_THvVveCeTLjUdeD91Clubst3Q_-pj1uXU2Rdg6T2ql5IaH6L_SpbCQkATMA20eegixVLu6mIRQrfS0xE8pWSu46A9QHBzFtpKYxIzViDfq88fPq1Ra1PakcwNT8RsND9QHUO9VN4-A4nUyuEQU_nrAF4Eze1_0YNlaBCV3WqJxK6kz4QgQEmG6knP5z50bcBWIZSdgUt-IUSj6wIuLqbvbFbMl4IfX01yTV0NktptQF8U5VZaHHWzEw_8Zx6itsl1ynvQOcnWExUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIcyYY9hBtdF5ARarPpNO6zjhAQ-_cYrrD5NCubVrFMT2hewHjBUepYnSa6O_RPG76w4CfH9nHqRFnJTsPpPDWtsr0ctbOV8KzdmuzF1NW7FsEGnLsxFO2VRXx3Pz6aRYWorTrBv_3p1ruw9QDnu72BYNBVP5tN6603TVc0KsdjhiSRyvZtF-Em34GfU_v4R-wtgz5Ra2nS3XCdOLxkowj-R1k32HFSA7yGUL6WyQorCw7GK-wdUhMzIslxTxdx7F1MCText0-oiaOl9RrQB9Yl3iMos4kO9QwvbC8VNKWrIc40sCPS_Lxsa-FOZSmg1rgjje3mXaVJhui5nuSMJMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4qA0tjsDdmkQcqPASyJRp0jgvil0MPT7-st22pdkuDECCAEnxGrvwnydiMN9cTlwixld5ApwyvV3o850c7BSy2wK2LNmtfyHASM_8KA33Cp_wafuaz629LAqLuVb71PtTPAphkNlKHmu_b34SUYPOU9S97facVY_m-8USTsOoO7bejANwh-FVBcHWsEyQ7NnipmzL1Eocy3umMDn5Bjr0Z0HO7LXNIwnIzF30OrGSzLzMMzgz-lJqawZ8KU2BFNlGUfdKEijx71SlMXNNcHw6pdurwHa-z1v1zi-SQcuZarNsR4FInoMd2GgXtQcdGSN3ULZcsb3e42WeR1S1jpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EocHbHkMnvMaN1Aq9A_LmdAxa3IP_WLoozJuvudVvXHDfcXCw9C4Tg9gugzipC1TMt7BevZxeEDvJsAS-td6R0TUHBQoQln6wotVgWGzi-uzyLr4v65IZ-EOarjbpm5jJD8dSmnNlCsO_pMenbLcSgGckbJycLEGuwJBcNg_bt8sCRIHX4X5QdGtfY4WxsiJOH9-7wC7HoBy7RLuNCVH3i5GiQtnujw96YiFmbcijVGYUqF0jDH0KfUdNidLL5GgHAvRpQIBRQ2vXHLY9bEZgoDFCWq2ypegxrkWCSOrUB3gE2GxBCcpBA-xhhCezwEig7oRA0wtLYyl-QY2reRjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOxl73V0ApMnyXl_q9W4aVzPlmldp-o5BfDBskdec7hbODY8-29A3GD6F6JpkCy1Mx_IOwA6_7-QFyYyt_uShmZIHQCODPXOBQCdNMAdxh8Yf2QVux4ydvQb0b2IqipdhEinMO9B9l-jeZ-ZgtFv-HVdorlcMvX45lFz7fWAPOdB4HpsXVe5zH7kt-zRk4zVAOK2kOZNiA27F8nXd0p-fnyGK19ZNAdhf3HaOxZAbmvub_hfZWHzhdYe_DEgDRvb5weFkaKcT2aow9ui10spmm04L2AWZ47gx2a5wIu4Ez4o5CA_phZePTSTNV1CQcNTNnOeBRHZxC7FNv9CnsTjQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqCw4yDcAOw-WxnZ2eoPA1uradUkqvceUzIdwepiSlCh7FVDeKieacqoNnQezn0QTpZSuCPLw1CqZAO9k3690istuIlikBDGVeXKlwxCjExttI9Y3ZYeNtUIlyCVg5WQ9FYjW2fJhTJ98rs2cFgE-Ze1ZUXiKIuh62il4jIIF-zZMXtg-Tt1W0UsWswHwFY1AEdXtTPNIABbY5i-9cKQNBe29ClMYuRCCYhBR8SQ-Jim45k3FBIwqsvVERUO4dQ4xrK6Pv_DIFLDHlqDLySAa29iHI8LfL44Bt1cK_BoaUueh--Kr3QCKwHc-yd0IKxKUCkwZJJPgGEpD4WepjjRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSA44e9dAA_pVsUmJnm4sw7KMvlXuXrjKlclStwbJmB_mgyBWFePVX64_ebR3P6HYb7jzkh6ynNGJePdxrj37N7CcRYl_OEMC0WF6LEbCOs2-62gVe92d3zhSlL5wyZlx6VKMdkMoTTxZmOUOMs7GJayXCLSObFcJdXfuuhGyUUrcnig05alijf9fSvX8JDN7BsSdWNfg1p9LX3oD2DcFlNgc2GGNiASGMLFxTMHfikYX2fWE86lBSqk9G-KQK2DM6xyrlzR3rcnCbe2IdAkCegtWLU-gqUAE18PEfVj3i2TNd75I3Ta5H20JDxEwFAkzCnLRbyUWbQm6R-vqXz-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7p3c6Sf5U2HKjzEYf3z9HYo6i3Ms3e0sPMvLJjRewshfOkBfK5-P4WCOW5qKnAcsMhVQcdZUMdqdb_Sc2XeiWyHCmEiVx8srMhZjq8sUuFxxeSjep3IZloaZBzocF2HX3Y2-U520-O9Cdxhq1GmcBo69hHcFSN5LbMt_GqmP6YCSFRqjY0mn3Z4W5Wlpqm9v1UbtECAXdxu5l3pHPOiSqquYvUghH7Sva1mLQHGZYcLxE6RavcuOw4r_GFl3D9gb3VX94NMJ38WPZhlp-DZW6o_215_0NIGI9bv35FdIhECNuOWJ0t1k44_kS-9EBkRmFBJE-DDUUysoG-sWcA13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wp5vPiitCM7bbRnn_2QTlZxGUbrS98lk3ojPTdwX_gLUI7oDBmj3ZS378v-vxhiKgDi76oShJ5-jsyyYQYWsiKgrb1m6Guh76yC5cZoMHIp1C1UzUlbkm5lyUt73LcZLppJ6Bw_0B3svHcMGFATqonzL2omgYVnlwbzYgZyJrOV0d_JDjEX_C40ZTbyR7_-3N7HduKqnFT7moq-JanzMgVzm1EFcCiWq9tie3GRT_yjZPC-3F7CYQFiTrBuG4XonDDEFWe3l6VE5TXhcS_arzE45w_VzTUU0DZ4kwub-JF0q_1TCJSeropuwcXNMJ6BqIYf5yYQrIqlB8fFOdlUDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJT9DL5fyjnhIue95D0eeI1gG0CYSp2LWxUfLSl47ERkoBbDa50uwvEqzH-d41eFqGp79vi-vn2VIjwVw9YNaJ2LN6-7uwiSS5-t2lre3uScPtDYLWp3ldHyFkKLB_HkjNFIT8XcI5o4kumxvYylqx-RTpvPibGUXkGVvQsq88gvcKHI0Z635weo7nz2sfIaUN03LFyZr4CoXm2J-wE_ItaU1iK4MHPc_IiYHZ8_d_CaieTIVTi-sryUvZO92ZudFCKLFYIO8aFAsoYZomsW51gg1JJNNlr5DpREAyGaMtSoyFMIWtB5FURCMi0hY1xtXE5tvTkptKyybtRhRGQ35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXAfgWBFZBQQf-qD0wH0bzM6X6MG4UBQVVj5tTHcfBZeWjJ5k2QMsiOICk5gQrNiAh3VlBq773hPaic5ggr0PLvUx4FYzdKmgnvXRR6hzzxvDtZqMkVjCu33rTiKn_Oujn9CypsCywLY86zob8Ozxs8H0O1P3sIZdyeJQy-B39T6qrwivqVYvMBG22YvK-yjMg1fI1U7gcg6AbPxUybkMY5v4klhJFAFcK1Wp6hbLdrJbcuUVRKTVqqpJNKu40eXfHEZWFw7nc0pxb1UnmuMukT8lYmr3FHS0MHYPcy-JRgUarGxXOiXOL6ugOLrvyC9NCOO3Lw3rrKX-qH5aHtIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe3pcmnMIfpX0aHj_LZrXvQw0y-6AxUqmCmTnc8lTjEKXyavr-4kgqutDurEahJRcva6D_JXtPZYokxB-QH3WZ6YQVxrj0QrhV2H-iCi3NLfk-Pga_zznSXfhN9eHzhwSWZkvrOozWphiCA1WqNfgEroqTSQPjzkpyeUSonu6hnaOb6njhwi_--C6V8vX53cpVWFHeqSFmREjqeRSk_-VutLvlt39Q59GFyJoV1V3lHWlyyOOoDMaQz9mxwjzgZjl-Pg8b1r4OJ4k73LTSoUDWU_rNMjRgcWqHcdOUaV6JJ79gTSI4yPaeDTg5D6nSpEGRKWRpZMx2SN0FrLLs7IpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptmmz1PMyXOXw_MLfKn232YCfwCt-kyIyq09JKwdgyIFTl_k9Zt6KqGFkjBPQV1Nzdi2rEkT9oerXbpTYyoGaxPMkm39mdK6WLPFYImIbCouwiR37oyZGDxXqUSNYBqDQUjzGXXzD10sSAtnTFdIJlOUAOHwG8xIsZHgaqvtt_QvtjN_JWRAE5XtSCER9ZQQIXmSiHdE4Vep7GVHb0dUVMItVDoNWtA3hKHv19EBP9PlA3sgjgZ3F6drpgAzDeXJCMeoEsAO5uSBlaH_Vbjc0dxuj-_80Cfdy8bB7GaojHQXta9VsGUxpPDcuEZP2XwgYTNZUT-FWQEBCj3wmjjdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRbJUbBMHsd40r6pL-n6g5fywVf5f5lIk0azIP-RCwa1r6beZPFpq0FgNsb02wdFwBZBqKG34rG529M8IS3XM8qP-kq8eIW_ogTH9RpT7Xm2TSZgIWybmKRyIX1GCrxrdigvjzPrcGU1ZB3LMlYEogGJmnY9Ec7D2TM7i1zr_w0qflrHJqCrDc2fochlp0J-f8trTYmUcQD_pS7v2wpC3DsbseA0O-e44ZHpdB249ZCirbHnE6Ke9Hqe-xFCmACx9Wr0iki2AGWARjPiHIv0I8G0utOMewizeROLzxHbFyn5sWSGtgq8glwCK8poUk6KR0myC6GR3aPhpQqUoNxHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q__7QbB8n0ak-jgGu2r0iEu__O_S78tGAkQkZJ0Xm9We6wxsqRtAKt54gcZ82Eky8Kbt5Lglg15Z2em3vSkuvEXgvxdDUaJdl-ceMu7ELdInAb5GJdjyTnEqy3O1dT-eD6-aK7tpX0S2NMP45g5kMTp5elmhBUU9sg7UrVHOrGtINOqEtvy-4iyqf9FXKIjwyXJYLRB2IPfsCeSzC7WFcmQoUpxSUZ0X-GRdJuvTxoVsFzKyShvcnQe8W1Q0RlBu6EPam78SXxW4vzW4CXMJRgDcdo1eSXBmJAxp8ovKY-6CkwQqq-tFD6DcAdu0BuEMa8eusuYJZGu4g5kafOFrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvmnJcflaNLolw6W4QP3Q3gqln12Zq3zYgbLaUfa9dekiRa8aD4s-XAQbwUJHP3QAnSzzc272KfpsviN55sOuxbNCQir20Z-EJfV3RbD6OMzDY0ykyv6HQctlhubhdWHev7DR88hjMdOqRTKGpp_J9yyzadpuuvWlpas331uYbRi7-HMx5HHK83cGzpo9dhXvcyEGca4LozwdMNUwtfvfIvwqIdOp9IC0qNzIqccR64rPhED56LhSGlCqfMXhVZYLFX4h0Qr_zeH_TByYlrhGLhJlIHqGsTzvwzz7n9Z3LdLn371vhjTNHWrC0A7QSO4_n6-N8PW-v20GDGNhZuB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSmyD6Ai3LzmKqz6j_H9AEmpkuMG-ZQo3GenPIF6FIaoMJc409M2QOawLPcqmMvjbkXh4jyWDoQj0ijo3v1Lhg8Z-nrG0FRel_gV_gnFX_lbw4n5PzfQoMnEkL3JrI191inK0hwxYvQ2sF1x4KTFnYB9ypj4fLlWdiuD37dB_N2E0SjxedyJo1SBGO8ehvKlWBV-AvLTjsaMba4pOhO9D1AZn0cwnaAeXIlPyDHJJxHub3rEfzAHh8Th-FaG1UhiawCA9g1fw9n9P6Ymq9cKzpod7STvWsKPUeKKupADnif4QdAXSDYhDT_9SEVgQpnYz8ocICyGdJev81LcecGysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe6gwxSYbB4DYth1xeBPFNS2LUfup7MzUGUOkK8Cx6pdVr4TFpLOqfJTbLFuI8eH2mWT-rD1AkgmYlw-1NEIfcnnqxGJ4T8ZUvI6JcWZktLLRYGH1ygljZXSiHmprIjotJ-SWKQYY0Ev89QAwO2dkzIC1N-JONq2R3coFmAxYlRSX7FBzK5B3rpBFLvGOmaKJtKS1E5EN1Y3cx0fZINotc61X0VGxZJkWgIP2ZBuamu6cZ1XxElseUKqNrRiBp2pCZNnfe-ACYxzZc1ynrAS7gJ7AMGmJzcvug3FmQ95Rm6s1TMkjoHdhldtPMxMXozPK_bsanwXkDLEkUPWsamSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxcXTvTJgMrZeTvrzzuDINPcL6CzKVHxLTVIkfGQDTx0JBQwruQCbyNZDLoepvqfAvv7urONl2XdBv0C7_stQfiutVTsaQEx8DDngVTn8G7y60xiHGt5GAbvLHCp1orjcoL7qwmzBaUIFJeVD20gTUfdyfqRP4CDAYVYgk5Og_2faOXYfeFu4_82FWGuZdEbxP3mXldWQHZ-Wohg9jVWbN4Fu8jvJGKjxP4AVF72WftNHZd9O1C_U4G2yR_3XXf8r8Sqqrq272_-gQtkjn1y8pRQpC4SXMFB79hoF_EHkZr_TnMKO-Spe8l6B7SvTcMowwvVn9_lCcw57mG0MxtyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXN9fzInwQgs6tJuNDPGr1eLWR7XeIGKdOLlCRVMGcWrvEUmA8YNWgwHdGRzmmBdXkl4tQkkGPAi09itrWPYhgs79ddM2fq1qzfrZYfHZqPxIDU_2K6waQgb61jKU4Vu9Z1uznNC1ftRGAonxzeZzOzg7XTGJ7XG-ZTVPWGGvcdnngJkA_wDzBYDwTF4hZ4ak6bSYuVfsIHZy3M6pqBFGoVehGPb5nOzWDBv7a1xvj701CURXqxP2dZ0i3XGW7yB7kvHTwzjv_SdCPT5uz9vRs89Z1BRBBfp6vf1r2kKr5_JM16WmxKUzVr94E2sYA-sMPguslXF4JXauuw87JOvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrRiOIVm2WY_YipI8SbTbJoFjaP8JyszazlFXO_OOiRJbBwN1WcIgzd74T2LqGpYqGnByt1CmKN2spEWkq4rx6GqtVmwUV4SJplvvvxZr3XVLCWa6-BcJSEj44svA7YgerhQQJO6LmAl5Wgr5oU129YlT_4wWGnZU3QN8fGTi69olVyQRl2BYqGnkxgZ9YyV4idoC5wXj3OQ0kVAlzO-WkkO6Zw0OWtA8JzcJZqZaeBhMhO-IsaPr2Lf2_OM_edlHH_UFqR04NI_Et8APSz1w-yA0nqTC2wJJU3-szXV95wpNBNV4lRZ1Qp_SEK5oJUui3H0IO_GjCsEh6SbKOVSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIQ8XPjk8p7mkf3Jw3RIqRvQbKz4xrBftsTm0BOVY5onvlver0yyUHBJozu6XL9EbqwSN-Xcqp_uCOU8zSvM2Z7YiKBhqkmzT-Pn8xyzLYR9v9R_tieZ3d7lAJ0np532rg4HvIv0GSmkDLQeBGSU7axkftj4afIhZxV66Kb380Bh2A_A7hYsAxCywQz1MIVGVBDBQJzUaIFHeJ5hgp2Zq-YTsIFJhSD-qQMpY7xEzkRKtSI2r12_G-aOawzfOxiTRDSB0xlFghsFdsnt_ufW5NCyfoHDJYS91dKTkywPriWYn80fuUjLaQ9LuEFlcVne4E7_X4sAYKebQ7osmizY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1qVAPbwKKCikgz6JwbEYa5RU2ACvTSJfWuytzGuo0QRLZnF3sVh-h2AKJtSSkgmHCz0MElPcC-EsrKEdd3EHvoY-wpVlwRCBud9Jhg_tUHQoN8FGcDMGNhb9TF_H6IEkMql2BEJxGjp1a7ZbLVG22lj-OMpmUhoW-M-AW40o0IslyseVy3PfCSPKiV4EJZSAn416vuBT_Zc132XyIMUGycw9u3oOOte2i1vZWsILhibFCF2Dnn9Xot-yFkv8v0kEtrLsjVH1cE_JXMni9IXHEhfXaDpNmnbz6L0ZuP-QexCB68bbBgABdbdk3gkv3p7R2POopnQDEgs4iEaJWouVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PipMLOmVyjWtBv4e2t5dvJbdHLyFnE_NmRagJGzUPhGRcFgoLazD3cAxpcuAL_t0uJaC6UsRg5VcILpNAxzJ3AJ3UreorrWRDnfqkm5wSKhm24JRqAjO4kqxetfkTBo_gW89wDT0SVmSBs7SMS4q9P8a2DvGE8i7nCxC_Ha1aM_Uv2TGrRAHoqSEWQdxfsGQI4jsS96Abpb9L0rsig0TwGeVmEQXNaZDT93XHOVXGnRP_IOMokSAQV9-4ywlpHh4_4YnLm19vTdaoiBVHdR7xd2BTrIcIUIcmikVrtJ7WTJQPJFsqfyfA_4yR8AbiV0hU-EjkgYtcf2THtKBRwF86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5BXGq0SgTieMwXFiBRvUYjGHvgSIIZSRD6S_gTwLVJWwcGc1MMLHjlvgmHu2w-kfzUwacwcn3RJXs353AYj_RyR8jaq5bMdb6SvC41FaF98uPbuK9_vxpNZ2pnanSXR35C8LwxrNF8zLpoT6fM5ur62bftbSS_kPBtq4OnB4-Hu_5ES0LdELNx_UiQ_lmKEOiur1RV8Ezndz6tqyIm-kzVDhXytj6JGidgSHjN4VWOEmOsWxVCrIoA9h771lPiUywKZhnVqpnt7Myo6vegCiKbjTkiuSFKxjcCc0i64F2dcHHNU1eWpCgF2qcqZooLBXt0IUw4OXoCpFfisBMmc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhsuyFcWFJv_VuTdtX3N_H-cZA-X50_yolAbogdbZJZbcUT0zDVFZPBCALW1eR78B3NsjaiX8FgWFbUm-KpFobuic4_N8zVfLdly8QkbYPZJF_cqyKjXoCjLtjIPLWWBiJguLfT6VLzPKKvxUXWXT-2NCpku4LigKxKxFmuF8W9INiNEXivAX7l4c9dk8qMGhzxGWXVSmFJxNaO7FAt-XTDHDD86C-J9f8Pq49Tia_J2NEtX5MD4bDzHjcFARXrhBThRQK0yZU8dKuxuS4hw1W79bMNl8ZyuAOACAzfDbGFihrskH0S2XtzwIBTBo3n8yBASWeGQS3FEF58PTo24dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaReOyR79QUvOMw_ZJVbQUqc5yqrR2r4PyowQMfv0CY5WhWYCJtqGBpj8Fijn8MKta8JdLCMl23gopAiuL8ovq8eoAxP2DuyLGZdjtqO8n0dGOwKpWvdwwlh58PBDRw5d27UTdNs3FC_RU8kfqKapsnAHWaQMcK1UrepmfnFJpIVjhIeJ_UThiJkRuGlfLGfW3mWMBI2nJu7gGGC9jdxy8o8l7W_b_Zy7AWkTNNTXGI7v06lDN2ulTlDO1G_V904peNIssH7iON79e2K0fKDyqYAqh8AnNbU2uE4Rh_SyrPEPXGW-CsN75KCHZs_vpFgYneXmn5AF5_C5tkdW-SB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOBPppFDwGXUM-IKguBmiXq-MWQVmKZbLaW2ubVEclICED5xLkiru2Q3ryjgkS3VuC6nrnqCiXY5CWRPLt_Vggn6DnlM_uB7uweMQdDQ2uzcRsJ9_f5j0YnQqT9plJrOJRKlsV3HvTQko8Rl8DuDzKiKlQoHyCSgvgh5--kAXsut9GIjfZOsXQulwkI8uADNeQIqHjd3O0PiEQbsPlzJcKFAqZX_HjvG7zlSrnKLitBj4q9JhVWbgXYgiRKM3PXx1ChuMKk_WS05gqgThfvsNYB7WfNtVeoQlyj4TpikntPKum6zAN6J6iq5glYPo5oRZiOhdEf3ODwojGCjrl-i-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT9zsmpXLXF3m-eawuX-edtFO3iPUVdTrlQM3MpmSZ-9C5o78MAICbRpuUUeUadR64wQ84e6H9fDG6Xs6u4LSGuowChud-ruJ4KBJxXXIJ8lMJkLVi3sF4rdTFGnlvboIRCXAVg7BjpCAgJ74UV9c5OchUpu5Aa6_Oj2t2teZX1ZV4DjpltMb34ll20LTJJUBqbHcYVLwWKX_dda2URoQTKFCY4xNZrUaqOMHD_1jGpfxDPRq7Ejq0EaWna7R4Qi7LQ2JmiCh9LvQH8tbEVUMMi0trJekDV48dvCyUTgCiyynGeKMxuRAkbC3gXELM1oYEUcldwLyOwzFuaq2qiTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpFwkS7X2m99B7UjGJziSpuuXiG0o5CX9wMfSoQ8mr2pc3tMt0-PX53UMYjAabbWxxpsl7noejoBrLsGW6VwhaezDMbLqrCb_gbr2RxkFPUWrI1aMNnsQAYHug_J2GzHydifToLCvJMXUPgLdTTyBmXAF4K7-KpwZBqHCOmxwDn7gEChxVKqMhu-sUhtfGeLXGOo4HdlS0jAo6HUwqrl5qDDDNsskErzuDT0YQWdjH7W6hJ508PatxKyg9h99BsDICgQ8U_Dh4UU2toSUn94wv94sysyX071zXzxuUsjIydCo0KFv4zSXMIgkL08XTjEsI0PNBD3rqNw1i0Jprli1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjnZXGxyeWuL1OQKsy-bwrEZVAKrLECKsAefn5dk0OjBYIGc4a3QZclP2AkC8Gw5yLWJgF6-z-cRVpZW1Sd3G03jCCtGRuqubHo4rTEW_K6jYGy872P7XVLWurCGqXDwwHwqz-2LDy_QiP-kzZW7g8v4uTxxZY96uSwE3hK5-3zmHGt03Ddm1slHuXX6DpjQB5sCuJsrEa8WJgDaRAi2b9oe1d5gN4QwvugXeZmScIKvdwwMc8tiEDNtB3wl7tK4OI7u7YCQnM643vSaJ-ubhL8j4Xt0qIMQoj7OXOX6f_5nBfa8Mrk8d7ZwH0rrD2jPJDq1YnK2pNpsHeBFrlTTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoTgWm_MPNtDnH-fFsw8e89aj0ftD-DhvWlVxQ1yo6pyOlok7J9ecGY8IyVBvU9LN70zjz5mHiELZmJHp4kBV-DE65iMdMqT9sXgSAW3DAA7pJ2NDSkCWEGYZ270d42OhUiLREcwr84TplTtOGVn4F3Q4R_XM9ZBcZ21c6lMLt0EIu76chtdhx5h8q-e9sMY3Ie2hjbMOFdyzuLXWpi-7DL2k084FGQN_x2EV1a0BeG1z74DRPWKtZcqOkHI0LkrwHKdF1x3M2qKeXcpZkDR8Ep_aVWM3XJmpyPzW6bfr3kBFhdrM5RTWr3I9oxzWuW8tcIuYbIjaPnLZ0pSyCZ3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKvMAMGcNr35WkzEuIY8b7Tas7y4u4CDHh1O5aCIn75XoyVc3bvagBXxF8nc4Lf-XF1RW5a8FIxuz-FdDG86DRMOMwdTFvLwEWLdny05iI209dAJIffPY2H9ghqHPDA4HrcEN6JlsZ9rCA6_VzeilY89CMTCZ5w04r_C0Oz2srLNtzFrDiNkARZm5sPCMzx9mENXRSI2VjiJ8jkjy468Igdx-AUDJ1GlXaswH9kbauucVzCtDVFvh_m3r-rA3misLfWXA8Cm2ym1tA_OLhuVIjriO_YaUr8UlyFqHx9zCck9nC9y58Amk1ylvPvn3v9LXJ0LXfJLg4LgmYYvpntmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
