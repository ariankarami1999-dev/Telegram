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
<img src="https://cdn4.telesco.pe/file/nOW0vlctd2TQ96OKwa3NFmsFNoQvrBhAoEosFhnUPjxNPHlrEbzkD87PA1G38ZQzVAwAb5JssDcuSFOGvzu8W-NTnbBut4RiUAr12uA6zT5nzySNxV2MucoB-x6z07O3RQpAc0xYV03DRyjsSsWFkOXrac_i3IwypK85XjQ2OEP3HNL1m5ISFVypP-_dLIIcWWDsmxzfMn_WFXrzRJlGhZk3SgxrdISQncaOl4XWtmDF9FiRtstsNiexwUI-xkqCnfIUI4OAf-ffSy91wLCd9EcjozgeUTaITERZ0s4oqPzibfmth0FSBgwaWrvh0UNJMHUx5Bzd7bbgIx8VUGsHig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 479K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-31417">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJf0hfTE0ZvZkn2Igcf_35A2JLmKDR4yFyDMm82dv2cz1zmUq8ipQPswMDLBWKf68hGXla3iwUGVPVkFmlMcQ4MMHLTPUuNQEIiucgsuynXw1k9tTFdQTTR7j8AxMkS5op-qidmQxWsP5XCePmLfSs41pT3SKdctyuZPJI-4gdJqF1So2VpVC4qGLKOBYn8Xscok2U-T5P7c9hvr9ZSY2JdNt_PyNU2x_Sqd6ty-MyfKqaxEC_-XSFar3JjWKQf0HRFhcUBw54jpGtBNSa9yJzn_KoBWabIF_UvFrTh_EpDR6VhpHWpGGbsPEH55tbdqj-VhAE3nwb9gYpPZcYw7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضابیرانوند خطاب به‌شجاع خلیل زاده: هیچ نیازی به فالوکردن بازیکنان‌تراکتور ندارم. من به تراکتور نمیومدم این‌تیم‌عمرا قهرمان لیگ برتر میشد. بعداز خدمت‌سربازی به تیمی خواهم‌رفت که قهرمان خواهد شد. ثابت میکنم هرجاباشم جام خواهم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/31417" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqURutYO-1eVYGRdWmCrrbJKv4yHgWXut7nCmZmHY2k01V969VWWuCNNYw5_Rwlwldn2p6_4hvTNXb4CA38kKHqp_7dUqfImid-RHQUsddvuk1cFw3ZdSJ7Zm4nrZ6gjx3K39L9C0x9p21VyK39csuP-__FE1rkT2TCvgChgPSUtG6WrTXUBHCVmF5v64z080Un-Jhv4F53gtjpVidAZPYbHUCEPes_siBX3pOw8qOu2tVskKqV6SaMAkwA1H4BkpRj5XcnUngl5zzEfn2kl1eHwQn5RLmoG-si0wvaD_O_yduTAk980Uqesn4irGXkFZ3eD0zNe0eAOpBFENxHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/31416" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC1rJvtNO_uXc4jNkRHzMLWWBdslAXmlDMT5NIlzP3e001gTcnVWXKuHyeZQe8E1nJsGI29f12gQC401XzQa8MxXP1wK6l8bnUppo5L9H8ODIi8xQTxJ1605mGdeAqPSIx4rjMZKI3RWvdqKZmUs8g0FrST_auxEyMNNpvC6_hLkdz1KO2lJa5EynhoYerJexZ0JQTkc1SmkMUG_K0qFji4a0S8-0VWXxRmXTVDYnv5Pg_DMsfd9C7Sv0ZwkpgjnoYa0VDJpyBDuoTeQ5vnz8i5lw_548_Trs99y4Nxz3XJGThhQYI2Da-BQxuaez-7yHQvSMbU3qvxCBl0QBaymUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده جی‌جی گابریل ستاره 15 منچستریونایتد درفصل‌گذشته:23 مسابقه، 23 گل زده، 5 پاس گل، میانگین نمره 8.6 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/31415" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGBHh0GyYxDWVW4KTtcNVcbK6u3KnEZuTujBQ6tY6wxHSmPtAztQYV7TDfw9hBGYTaFvAHrY3vlnO2-3Bnrz6UyiiqZQglhT7Vf6B8ue8Jwk7N8jpk9NMWK-gLrcuLrPIWHQ3Ge2UTnNH-Kh6SvjA4oc22jpopu71EvyrCa0KSsaCO8cZtHQqbb5gRScGBZMpw0AQ_kXwYH8VdH9mNSM7BRbMAKh6t8cdIocP_LUfH3NcqHXftGMLbPs5sVxSUt_EaC8-37FobcffFzsPTYhy6H5u2SefCohwtec2LfotzR800x4hAHf-SxRBP6oJm3r-WU1WcW4QH4l3Cjj64neIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/31414" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31413">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=Ou5zaAACWohb7UgyMFEfamCf_JW7WT5jlLBXZ5GdcfvOFE_xSPVco-HwX3wtxnppsjOueSPYqhZ-Qb1GmPNZtjJtyz_TFWo6KI0ShStxMKr7gK_z11hXGYJZDzHuBd900fLUKvKoztOFXk7WJEzCFyQR5MyTCjFJ0ZixZyEziwWMHvUIUOz8KASVQsGKc74Mc5jNv-mF15XexQETjH28BMQ69Q1TRWLBbUrMoQkGuKEKbyniCWvhKKbh8QO_OfwjAo8_ZXMAwjBZarWg82Pyo4DSIY6Yk6tQ8yAYUqICnPtyDm7yngOIk63ket2CAKa_vFDgbMNH6_VE09gg26Qx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت! زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/31413" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31412">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=q0XF5hylwtt8sMVr-LC-Vnm7Rl6RZ7UUWK6d5M9IlGyfoTsBjT3R_VEs-BeenUo-Haot3PbsFN5DN8jZkm5Bh_E66vRXZm8Oqo92y_lC-IOuwhPCZzPkL-3jOIyEH6w6qkB0ICoCNfV49LnAeeth7BUHYN0OpEybQdtwLgJz6IvB7EuqeKuZdf2af0nEnENGk9AFc8rYQqr9UeqptT8zoYeGPANhztqIYq9I6rIr27GluFfPjUcImxxjirfi-VR8dN9NxIQOPW9dAXw1U7x0z3K4ZoqcrEg3RzOfYRI9XhR6Oq3w-jumcXj6S5rLiVYlL1eMbMfjsFu3IEDAUaLbTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=q0XF5hylwtt8sMVr-LC-Vnm7Rl6RZ7UUWK6d5M9IlGyfoTsBjT3R_VEs-BeenUo-Haot3PbsFN5DN8jZkm5Bh_E66vRXZm8Oqo92y_lC-IOuwhPCZzPkL-3jOIyEH6w6qkB0ICoCNfV49LnAeeth7BUHYN0OpEybQdtwLgJz6IvB7EuqeKuZdf2af0nEnENGk9AFc8rYQqr9UeqptT8zoYeGPANhztqIYq9I6rIr27GluFfPjUcImxxjirfi-VR8dN9NxIQOPW9dAXw1U7x0z3K4ZoqcrEg3RzOfYRI9XhR6Oq3w-jumcXj6S5rLiVYlL1eMbMfjsFu3IEDAUaLbTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر قاضی‌پور نماینده سابق مجلس:
تراکتور پر طرفدارترین‌تیم‌جهانه.بالاتراز رئال مادرید و بارسلونا. درترکیه، ترکمنستان و آلمان همه طرفدار تراکتورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/31412" target="_blank">📅 09:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7024843df.mp4?token=Y69sKwxXLXogoIfmf8mSrRD407KBUXS_i-Strvvtydt5ElJj4UzjFycqdeSDa9LU3f8FGz2FZvt_9pmiXdhrEqstja4bVP6LqsPpaOZh2Rs35xbygzFUUlHAyidOKXMb864mR65sS77Yhn-cJQ4BhW5AaC7u1YYCaK2ESJo-e_xE2FsJhB4lKQEUmGddI6fXAsbs3jJirfHIX-opm_F6e8w39oCkCyjeXDvbgLcMQdv50dTOfHKVyn0PuyrIhG55NbJwfR1ANDoweH8hocshYWECC8szPhWQWaUTFio5EOlS_n6_OBAj6xc6cz480cQVGSFH8JXvMTwIYMcT9WjUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7024843df.mp4?token=Y69sKwxXLXogoIfmf8mSrRD407KBUXS_i-Strvvtydt5ElJj4UzjFycqdeSDa9LU3f8FGz2FZvt_9pmiXdhrEqstja4bVP6LqsPpaOZh2Rs35xbygzFUUlHAyidOKXMb864mR65sS77Yhn-cJQ4BhW5AaC7u1YYCaK2ESJo-e_xE2FsJhB4lKQEUmGddI6fXAsbs3jJirfHIX-opm_F6e8w39oCkCyjeXDvbgLcMQdv50dTOfHKVyn0PuyrIhG55NbJwfR1ANDoweH8hocshYWECC8szPhWQWaUTFio5EOlS_n6_OBAj6xc6cz480cQVGSFH8JXvMTwIYMcT9WjUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ذوق‌زدگی امیرحسین‌قیاسی از حضور رضا گلزار در «دور امیر»؛ پز دادن به دوستانش با حضور گلزار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/31410" target="_blank">📅 08:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rauCNWI0e1LhsCSm1t7nu9ia6_6aebVw4urWkKCzP8-9UROipPcWA0e3NZv4_hynbMoZducWJHrLosEUsMRtJ_Pi_OIfq_Lfm4g5r8nK_OGw_Qm5bRcDyGQN-nCchio4ZD5i4F7XuCRO4KlcUdKr2XvkgUzI2PHvrkZuXkhVVvy2MzK0K59ioVFfSQge01_MKXp39lwokISFA4PcEAZ-6x_RntnjSHMtCPWONOv6IJOYWhA3n05SlxbotI4ifV2nkm6S2eqO3Qlkwf6qcsAo-E2E8J5WP39s7E1t0mv4-K64YU_3rPHP9nW_i9y9cNpAkgwPMBcrHbSfXOWFGhc_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/31409" target="_blank">📅 08:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31407">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5g3MhV_1mzdt4O47P63tpxPr6JLok8Div5nWBvL-fXQBXN-v6OGZtRVUgPvT0Qte7hR2ugM_BQpv1xM5NztVHP1zBeFhXoO2M30jquyy9aWhh4CZC6rIKM8iUUwm_UkDALFqQlvP3WbrSTogDOAHrVtJJUfLSue8X4ZRqDgEnwd2LnJcj6LOLZlso0deKNJjHrIPadr4lYA1Yd22gHBGEQgLj9nm8gvw1pSe217VLoLB5cv19k-nYbqg5G2B_KIu-fJeYyXEQDLnkOhhfu3iFnAfd0ErEnEINvAh7x2KUdtr0zvSx7rDzhUXiY3QxZ638T_EhogHcChjMzZ-CdjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/31407" target="_blank">📅 08:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31406">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA7EPa6dxVEiXOw_bCWk3m-9pngt0WtAOHE8vYo5f0xNIZXLHOWREIzQtBQZtxdch03mBQYZ7UFljeVj5qf7fwTzdW6kL1JjBb1_346YIjlb6i3pLjGrRpjy4q_vxBU0icElS_edZznochNeSKco_MVn_1-b9pKFiLr3gZeJW5zgnXUP43KCFS-AiH3g8QfJcE0P023jbrwSJNfR7-B5H6uodM3CaxD0gyvXrpzeMm6a5U6xFAz8oPGvd9rzXDEwDGyqyOcjfkWl9kStZzdmmiY_B5eRMZM-zZZbtUwbYSZG5lr6KQ5XpS_PQHPqm63LMI2FG8NucmdwJYETs3h9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از پیروزی بزرگ شاگردان مارسکا در آنفیلد تا توقف روسونری برابر ساسولو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/31406" target="_blank">📅 08:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31405">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📹
هایلایتی از عملکرد درخشان محمد خدا بنده لو هافبک پرسپولیس در بازی این هفته با صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/31405" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tObAl7fWS-QtsdbWYxYuTKyBVirxZWSLwmtBGdjR3ECCIKmjtSmul8UtdgHKpYrzYkn1q-htXMJ26Y3AGRat2OtwMTvuFX9PMjf9c33aF6xoaezNr-J22_xQdSQmlinZ7dxB9YbadapSOCurCcAANDDCw1NVAZdHJz7SQ-enSkvcjfISEo-a5IDmZxCRRhHlMOTnl0J0HASBjdZJMc6yPGPwVxEkNwsr8wUEefCrishm6g2ZfrijBatpn7Quz-Ufvbf7MUS5f7ypCHlMijIRTBKB8SwifdjTEJo3AtyAei8DuZLxVbdgIqc1MMRE6A-M_4o_acCNfxNtiZ56HL0O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31404" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTwdeppBpFw45nJ4lbvdjOgScZUZPdtFT2_9ecPgqiU28bNm8dqeSuieOYzbowoHwkDcLJH9pz5JlcXNFrhqidfmrrlcXRqtiTBMl-DpqNY0zyq4pzXFk_iV1GdGFyMzC1GKk5-VMTO0wJ52ipISORhoZsdC_3j5wsZDCpC2z4htpSdYD2P17vPTTc34gCaAR7fgdvnSLLXpI05u-AvKqbCgzVIEdPaUwGUV_edXspy7XD4TtydP9d9XO5pRU1OLxgMZVbm71oxqASUfEvrb0iyZhvSN7ah76g2gSOXVyGkPtidQup2Vp2TT2TCNUanalrPZnE2WSHdmVTc5juG9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادار دوست داشتنی و ناناز باشگاه روبین کازان روسیه‌هستن‌که‌اخیرا گفته از بین بازیکنان ایرانی به سبک بازی سردار آزمون علاقمنده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/31403" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEJwMoGaE753lWkOGNLOByF7GnLbIDBEsQCngIUlMlmuxVWvW04mU6K_cdcXeHNVyu206PaLnV_dfSVW_T56vtk1bICEmk3CTp8Lya5WFS0qxsbYSzVJN_DTdBuW4KcaTYBYi7ecMey3utLJr89vLyk_UAOYPMH6Dm9KSjdI-KSm4aadvsj33Yf8i5YL2w8iyZL3dOLmX2p_E7xAbiKH9KljFTyc66lqscjjfIrjvuVCOIQ5Snsj5PCWmFZVRijmQFYOJZ_NSDtbNnBdQnZHDkBZHJaa2fbeYFJUg6Y5OpAnhWNg3bQJHa1VbFZ36y9I0UUUebsskhhUIHrHijCphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31402" target="_blank">📅 00:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGbZecKZ16HH_BlNZ26y3x-RxLrEoUCwvcVU9sbEEdj-1thbjh7NigqHuYgSEPdYpwPJ8db9uJtuC-AzD4A3PQfOm6zT341ui8kUchua37r8yZRfL7AbSAyXpkxzLfofx2zvu8X-nL_QGeTCCDqO_dsVbaAZeee9Ptah8vzNWt7Wb4eXRtOE1npa8mFO9LcoNUAgdFmSko79vuwpetv3bmluQqHz93qLYivg1Qzq4kEWqz4pIHfOiFYWBVUeO3vTD9OdKfg-4BSlZCOZUw2UZrLzUjCmsBiprQfLqY4F8Kc-YVuDn63uzznMACvM0BtBMqFx1nUAxKEdO1Pv9f-U1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31401" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwHu8SNwJUxdm1_SRVk1hN05U0wbj58m0S0xkkLzedp58WiDJPbm5_BM0ryD5PhPEJ2PgsIy8QH8nQasRtKmZoBzOiGq25eFt7O7wGRSQjwKDLSUEzjI32VP7KEpPZjrsriItGwcGfKsI93wDFqNhfv75YpJ_w1di8bhwVrq24LQUw6lnfnhvxrhInUMkP5GPNSm0CfQ3Om6_BZZd3lw11KFAInYsPdBUSyo92vblp5GnghyvjyeMyrV2Ir3M1p7vlceueJKd-JAEAY8sbmIB2mGdpxXD2tvw7AD-YnaHVyGm3yWCHRsh84HhS0ZSrdCP9jHgGVdOkvR8igjzKBV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد جام‌ های لواندوفسکی
🆚
زلاتان ابراهیموویچ درکل دوران حرفه‌ایشون؛ زلاتان فوق ستاره‌ای‌که‌هیچوقت‌نتونست قهرمانی UCL بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31400" target="_blank">📅 00:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNC0wyDQYttsjIaAp2GGRcrygPcoU_DMfqxMEL8EPMxUYwaE_xskSjz9WczSROC08Njcb5Lr8zZ5Q3x9JbGNl4pFqHbJ_9Z1rKugevAx9oppy8lehkIoBh4CXLlMnuj9StdUUSW_nuWD-pjnYjsRegs5BYSRlpIJqzMr36llxAx1Mo6WT8s4uJhb2EqXf7qh9YHDNtIMEzzyz9_oO8U0SJKqsJmJd4sJIcCBvUbTblsmpwTywHtZGuIoL1c38Mfo6Eg3xUu0BB2nJOOqjoNBT427S1M4iqfKvA_NGvhZL1GC71i_eA0NWr9AU4PQZIIKr5-qt8e7KCru52xIvyGryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/31399" target="_blank">📅 23:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtRnLwKLPrQpyEoiVq5iWC8mF0A9wCtpHTnuBKJNinV62GW_1zcWWFS-eDdYmGHHlq-9c9xtEtZNO-KUi5OBs_anCzbDtjHJiJEZRx2dKimiUQ8ijcc37Y8bt1oI5Ja6Hh00_mgn9ILMJlE0Lj6xzMB9uZJbppQyLWFfrENOvZh2IreRuaxYK0ImezvVxUBoQfLoGRmKHzEV9EBFTP1PwESSBV7jnX3Wu82EfudfOIaSVeB4iwI3DsmyJQeIrbDq9jNORutyNMzt4S1c7nblX22bEYErc_CDUOD9jCmbfB3uGYdrg2bdS93gwlibtqAMohjP-vgwukFESYsOz0NBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شباهت‌پشم‌ریزون گل دیدنی ارلینگ هالند در بازی امشب به لیورپول به گل تماشایی او به آرسنال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31398" target="_blank">📅 23:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOfLkzWNmXJrARRWA9QG6xOeI7aycgOubbevekOz4hXiNdknhf1EgVQJp4KwQ-5Yy_mZ-i7922QkDJPgwf4074A8DGliekO30vsTXyiTUP1MI4tCZEcdrLExrd616cQmhiDT1_tX51zEaDfIsvTwEofGFbzV5RTePIKfDjyTdgYRjfiP6AK8uF9eBBik8JxTEv6OMbMzlyYeoXJiUt6UndFpsUcu5KCGP3S92MMBTltbfPXCHIXlD1XYUkwUKSbssFEvEWYfX0KEcT4DFVU4Js9yzM1VxFTsr6zkHvxVffZWF85N4pVLGiZWPXorcrlU-w_AGtTikQNHvijL-ZTr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
افت‌شدید ستاره‌فصل‌گذشته تیم استقلال؛ علیرضا کوشکی وینگر 26 ساله آبی‌ها آخرین بار در تاریخ 9 آبان 1404 مقابل آلومینیوم اراک موفق به گلزنی شد. حالا درصورتیکه که علیرضا کوشکی تا 9 آبان ماه موفق به گلزنی نشود دیگه‌یک‌سال کامل از آخرین گل او با پیراهن استقلال…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/31397" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUzjr75bpB3dXcPniPsj_2lFK_egq-U2ad6h1Lpw69SVl5yRnVwox91VxZcTq7J9wmoQRUzwxUTsCzZ5d1HwL9aavK4zn6yzMI37GgM-CoTez9dx3tvG9sBAPGhwZhwVg-ySndfaqtq3PhoIoxLKHZiymp_d7IPQmwowbvGk_CPvDqD7YzjRlWcmfVsJhv7uLAFYQoS8ouUV2YPAzqYxy5XIxk-YP2uyAxXGAB9pBiIQjAWXzExZMFOoyDUVWyouEK4qkR0oCaUeVyuQrO9lbrU7dXXC5HuC2IPFE9iydyiRi5smqXSCvsSC1UWh5tAVYMOEBDsHnnYQTwiiX-krRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد رونالدو
🆚
مسی با پیراهن دو تیم النصر عربستان
🆚
اینترمیامی در رقابت‌های باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31396" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=ezO8sFc4F15Z3A26o3b2zNoG4UVQio2vsL9jTu_RPjuuPCWwFt_Sy33fNKt5zAPbXwF6bPDP_mxDqggwdRVa60vfn63Wi2-diQjM6mQexEvS8Qm2qHf_eiBTs2CJG29TAsr3Du-Y4i-u1KSnAi6cUxvK-rLc6h5LwAMa8t4EA3_1B1mj9ddYQX-mqcc4WjdsTRrQUvTDRxJOkhOxqdiBQtGd44_5wywp0_mineFfWxzq4AZFsCF-dNHryxoIZzK86VULNL51-6DXatipH23NynlW7yOdQWUKYY-NbR_KUi0lymOoi0rKI5eQCxhXn_tG9NUNCbyX-X9hrh8zowOCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=ezO8sFc4F15Z3A26o3b2zNoG4UVQio2vsL9jTu_RPjuuPCWwFt_Sy33fNKt5zAPbXwF6bPDP_mxDqggwdRVa60vfn63Wi2-diQjM6mQexEvS8Qm2qHf_eiBTs2CJG29TAsr3Du-Y4i-u1KSnAi6cUxvK-rLc6h5LwAMa8t4EA3_1B1mj9ddYQX-mqcc4WjdsTRrQUvTDRxJOkhOxqdiBQtGd44_5wywp0_mineFfWxzq4AZFsCF-dNHryxoIZzK86VULNL51-6DXatipH23NynlW7yOdQWUKYY-NbR_KUi0lymOoi0rKI5eQCxhXn_tG9NUNCbyX-X9hrh8zowOCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگاتون‌بریزه
؛ دانا جین وایلد ورزشکار ۶۱ ساله کانادایی، با ثبت یک رکورد جهانی در حرکت پلانک، نشان داد که سن مانعی برای دست یابی به قدرت و استقامت بالا نیست. او توانست حرکت پلانک را به مدت باورنکردنی ۵ ساعت حفظ‌کند و رکورد جهانی طولانی‌ترین پلانک زنان را به نام خود ثبت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31395" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0EAe_0r9BH04IxdybQqKHkc7tvSSjMV_muLqQHV_sOn9qItGc3a0fPSf4fhrcN99N8Lig189eiYPVz36EyBWazPOUI9prj4q6tsyUJIh5A1-f9WkU8Psh3XDagRZG6dSj3IiZISCWZR4ORNBn3IuLBQSa7pma3WuHcVbmxOrhwPEbh3qQ-SPX3A5TizwLlmtsJMKP-MdNHwNtZHBSO1IyVH1h6TIDh2iN_6xm1Qy26OeBilbSMTznzIu4GzuAZpFx_eF40rBBKrf4cnqipF1-1d0n-AQp4v2mQyFI5Z_JOszJXHep7DYRJC6HRTQpvToJ62Cxr7eWFs5Zn8GtgWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام رسانه‌های معتبر خارجی؛ وینیسیوس جونیور ستاره رئال مادرید بعداز چند ماه از دوست دخترش ویرجینیا جدا شد. بچسپ به فوتبالت مرد حسابی. پیر کردی رئالیارو از بس حرصشون دادی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31394" target="_blank">📅 22:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeaHxS-xd9GAAIgK2iYZlYJXSguQSvEHK-1yOJNUShCpHN7zC1t2DQifafJbzeXWa6wBw6quVzzW0NW7Bniu8RL8XdLMsFbDZxRm-aSLwCaVAkAvDuaEETL8n_IzJ94CfPFxksPB5G3DhJfpmcYYESj3WYQKKAY1mvSjuBAsL68-rTnRk6M5UkUvnwHx_JnUk2rLbLpNgSgwKggEwSPxboTAhmoyAdJgb0T68Ab5m1eIuMfRQPmeeeD7evqRgIJItOSkx5T9jKP3TH6EmOcIOVJvvAlXqPwcCobjoFX_iB-8kYtmySqOl7Bj2d0Yp5liO0JcBTstN1DS01juLv0nVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت!
زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31393" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=iGK8fr4l2Uq-UoX5iuDkm1tt1HwfN4V-Ez72e2rDQWEEClH-rmGp6c7GUc5_WPOeO6VnDEQfncrBgzKgKK78ukvh0084WzceM7TkB-gtgTCG_EKhsI-m5pBqYra20qsdI14SYPZrgA7COuY_ea3VA94RNocjzMHTAqKHYnVRpK9lv9AV-d0ZigN-B0UpcZY8H_wT_0vSIafhj9uy_Wxn69r50KeZunQ0OymMVAfTOK-3pbMPR4YrWrwKYhzS8IpixRIZT1faIdm2ZE2GsTjClHnXxgVzdfEjG-ZuIGCibee4XRBjGvdJt65JHyFcPv8-4ohWEINQpE2to6Xp2UjAlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=iGK8fr4l2Uq-UoX5iuDkm1tt1HwfN4V-Ez72e2rDQWEEClH-rmGp6c7GUc5_WPOeO6VnDEQfncrBgzKgKK78ukvh0084WzceM7TkB-gtgTCG_EKhsI-m5pBqYra20qsdI14SYPZrgA7COuY_ea3VA94RNocjzMHTAqKHYnVRpK9lv9AV-d0ZigN-B0UpcZY8H_wT_0vSIafhj9uy_Wxn69r50KeZunQ0OymMVAfTOK-3pbMPR4YrWrwKYhzS8IpixRIZT1faIdm2ZE2GsTjClHnXxgVzdfEjG-ZuIGCibee4XRBjGvdJt65JHyFcPv8-4ohWEINQpE2to6Xp2UjAlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31392" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNJf6sfpS92APfFuJS-w44BR8VP1OGNUU0HQlE23ycGVNbOdjw1t8DS3Jo2fsv6XnSv-eDmkdLiPdnfNmPNkPSuccF2EMNTO3sJ0rWX12rSmsoBh4UwiIA_EndGwer6D7Y0THdELQkC9zECJNv70BS3bzcuS2xgWnYmMyu08lTK7lKmzpFlWoz7ZZNFpk9pyQ6M5omtxkB0j1W7WcvrQVkv-H2rpe3Sur0B8kDRkJEZUMAffElbwt43xYTWbFEapW4iIK8TbKn7btir7cH7wIg2QCzTu5a3tdxel6FveIka2twVMFIKI239bDe1MDm1Enw1XpVQL2ULi5t67XMjGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYhYbUj5WY_-v3yVRjDco09ZN5SWw1MUXNoA_ulgcoXiiHAA2HMmmAmL1J4OzCTNps7aQLTKXUwoCefP9qdPa9uBkl8CaAtaqp3rksqiLeT1tKGRDtNgicN3wTu6OzeuHpZjKZ5XN6Xs6RgwpQ9YvJMC4eVPGI5G3u5Ac-GUpO3G3KsTDO4ysz0FpIhXiih-Fs7rYv-qkPuX9rVo-OIDxwRdCqUtTgty55wNe6Pmh4ytSOCQk4O6LJOIFBoNMuAjIJE5TaA_A3ITmnKxjaL8UOA5tVrm4f5Afq-yVKfZ4P7T9iePMybiGU7FGWPmXZ_Ngg7bUyW0DfQEDfVG-4ZLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDfBAZpuNzK0t43UuDox-jSqwl_m-nv5L2Mq9FBW1kPvcMAjKHnTiptzxf2YSy0FMe-59plE-8vL5WWmwhzba7UbIZrCpYweB6XpWWddd-IKq8plCxNYJXJEDuqWNBb8zrHdgnKAplvxVwGTOvwBwumyx96-iGMeL4MG5qSZvGuljX9PfEUBSxvqoQICatGyrixwW0q1GWe5HEnb97mlFhBO1WL-L0ZV2dEbanI1k-NTJBBINPfHLXjuOvL50AD3Kp7-H-CbFirhpB5_Otnb_y5qsZ1mtnVexzT_Wy9QbQvtLCFDxCwVHfNn8UiS2uHFw3XSBOUpzRUKAaBIO_t1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKq61jINopELUXGBxDTISaX9T1uV-8nambs7clmQBkGzSUpdYOUplmMv-36x1lkNoCxsmGBxIwBSeIhTesT5an4a0EKotS2bfT9xN-3EyhMrywX1qnw6z0YDiaHUskmLjXpOg1UfjU3ET_Lzi9Cc4bHEW9Yk8PB2aCHoqPrIIcGNzK-puDMX4k_PdBlKrPhiuvdk2U0RnSvECkFtcRr52sG5GfIjD_K8xam2OTu15ZOzwTU28dv_35y4Je3JYtXDeaN7EzDbzmDx-IjfrziBeczs5_90YypRT9YNyw15BQTfAnJuyInzzFrkq9Rk3MJHBT9o_l9XPu3nDc9OaAbZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C71tU2Lsos6FR-GPcli1-8541SkXNAzsPXc87NYSlPrzoa8m8HpaU0-o69l3ix4_OxJYeeo0tgoscOTyL7a28jw8gM2rV2h9sRO_c66KsGp3GYOzL-fV0bZ7-qZ22pWxGm4sWfMFQyRYewtEPUzqb0Fe_UgjWS6AbLNNAbUkFs7upiKM7xuxEk8TiZw0jrEjRlo5i2vSgnKR0IDMMiTgYTyCh7Iii2CoKYACFJ3huVHebKKRpY7DISiQUf7Oob8ZWh4lhjACEAv9QqtrgsVqhbORCcZv4T4k4O1q4dmjqQUikuS9pyoLgK7Z8KkHQbYeiguAz6Gc7bN7h_ltDwqQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31385" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdMgB2y9tfSDjYusP7FYuNa_2fzSUvz5L1jXBQpDHNzj6J0fDQVSBxNWwzXr_ktZ44zxAE3nClfCvujxkzIBs_EvcDdmO2VY9uL9g9gHHJBReqFjRIFOHE_p91BDtsb7ElQGMVSHVGlYyD8N1RxEKiWDfi8iE4dZSEOlF3h2rjM-o0K3u3V_kDEQGca06LoscOhXNBun3V9ZMupZj-KGNg3rc-2m_z6lh7NmMIcFSBJSbnv6_d4ThcQyhwF_bnCFZXa6mdyHdPbH1nDtuCT2AMWw8hL6rap5sLMNkopnc8Y-lzGP0jA_xHEiynKiU_33sgOetcAegzVwFT8E4duiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31384" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p50v5y-5Xacos4wyHivoP2uNRyfivJqyx_9cgKLWf4o1B5wfpfNB8gwCMoe2xUajyv6SdKOelbwPV2Nj6ic0t5nsXw4gdIIxenerW5nLpcUh5GTNGTQi8Y3mBeZc34hXmy5nxdt7OE0as3WhUXz3QoZ_XxmrZ5q2hGn40mMpWjK9nf6TnMkDB1QKUM4I3pmMskCQ1TcbcQYgCMXRPc7gGK1IfFPRMhi3UbKWXLFFVON1jw5WVpmyBwW8OR5xsDLnI47_JB6ECLdXsUf-2BIGiS1thiNvXch77DFR7zDdQLhza-qsX38bssLMqGUlqd8mFu8qHJsfO9Lw_T7VPQvUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31383" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkqRG-9xHptV1emuld1gs6gHQQM3FILB5BgW-dPsTt05uR_u7sOMXPvC1gbETbERlnL9c0F1hbFTfDXWPHyPfNgYmbkOYM05sYC7scGWq9_1H4j-QRyXdOk0mH1GsmcQXlmmAmt3SNkDXyxd69eT5i51olW3njV3b-ORmdahl11W6fV32L9wFgIIaP7Bs3qQdLL99IV7-cQsJEXfHp6vVhtn7I0HjlMflF4FRi0SGXVJNw683jfR-Xr8gk5tgmPLzRLurNaj6J64PnGs_ybr_cZLbhVIKDYeV2lakJEr7NXmGii1efrQDk7OwU1MUUZzJPFDTv7LSB8yTYSTasiS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ زهرا گونش ستاره تیم‌ والیبال واکیف‌ بانک ترکیه باز هم نامزد بهترین بازیکن ماه لیگ ترکیه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31381" target="_blank">📅 19:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow9zf6AOJVSanVeM9xSaYHZfhfgdIx2vfex06GxRyu7v2ckXS4j7h6_NaqG_3o1UUuaLK07CLHh3GrbLVzYwgCdm1QrsZ2Sq6lk3kbyjWNmJzk5Bd97r7kfDfMA0cU8xcQ9DAGeeTUPeOgcAOhm4o2s_97GPJA8y6hBa8AOzYSedSNaG7WKGd2nzQ9rCMlXh83MoATIu9VFGn7ibfSVmoVYeEcL7y0XHrGZKLrn3ZClRsyT9_WvXR_nKMp5LkpE1_VLGWjOi1WjAOXreAOIRrFZpcSJFFgxeDBCNxEapP90Gn6WZMRL8itWGrL6L_Y0qDFodSudI1s2WKjt_aGXZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سریع‌ترین بازیکنان تاریخ فوتبال برای رسیدن به 100 گل در5لیگ‌معتبراروپا؛ CR7 همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31380" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8eyR7FllEW5wTwPhRnhml3zSMo7DQ1VP9iO6Q0w1KJE6bPrwf1gDNl9MKMKIsIlsU1eiIiP1GQBzCd_VjDKvfyd8Ges_NN59o_fR-fwFzBx08QwbbPVe0KEY_5VDN3qBdK4dRzaVJKEYuc9QJMOLZmlZtlxkPm5zZyQ-sBKcNVGEYVDWK2BfSX-U-Rd1oGOc0BRqHS6st6fzZrgqUBJCX0Pkprh49kwLPhkSQvVnouRIU_PBYD3jjXmJCP4hmIRqqMfk6MYUWgi07FT2aXwrxKjNUAvyfamG1a_aBhMEFdDBJQtCpOOLsdpBle6iikadXaMippKDxHgnCZ254ux_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگار تیم اینترمیلان هستن که افشاگری کرده وگفته مائورو ایکاردی زمانیکه در این تیم و با وندا در رابطه‌بود دوبار درخواست.رابطه جنسی با من داشته که هر دو بار دست رد به سینه او زدم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31379" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKoaSLooqoU2oPKDRh_sbUHVxRolFzPTlBLjuuc0dMNx8EGyRt-7XhtWFw9U4aVcr83q32CW0AintqauwbXXdc9yUFOAxs0yIME2x4Q1RKXHEu2rGNTOHcF1BFeAyf5ggxQu1LSTzH4aJtxBGDW8_niHj0uR6Fx0OMpDQXf4k1cI8ioLlfmGS3oC6M8hyY_VTCRz62AY1rvxCAIDfU7PkmNRkcsIUPB7GaNxM5b6ujc-XVmIl2Mfcci5qYKx-05DMQUEbe4j0Ua_jouU6iIOhwLxON5oKVnpnCQn5bOWcK47v1G0PWNPDCVnBBCQfo_r26Sac7hi3k4TmvNtn2JwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیپ‌واستایل‌تمام"بگی"عیسی الکثیر مهاجم سابق پرسپولیس که تا آستانه یاغی شدن هم پیش رفت در اکران فیلم سینمایی ما که اخیر ساخته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31378" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP1Xv_Ak9cGnQkmrYpl4yn6V3pcDoDWte9XsUxwVX8ZoarUi-wttvQV4kDwfCToVpPrZhENkEPQTWGo-L-cULUFkNoNsgMIWYFyFOUtvq5YyU05dXXUGQIu0jNHDBsl8y6B9aZF7k5_DdjX1Ri5u2lTtvgUKZ8K208JJ0dQ4d3TyqOj_BFi8rCnugDt-qh_nLWdcl4JzY604TfdOwfNVXgDsMQPVY1yplmUtX-TCOzLzzQkorXoxXzudKb36FcthoMJQMse93juqj3GOGAJpKCny0TDpmLnyQ6PkeYDNXNCBQwo2wDGDkMa95G63wZaYxnNn2Ozf1-6M4rxND3HvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31377" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G50O3DRLtIH-HUGYFuSbcLTzY3gb1w85D5rbheuu5rplzt193AjrqacsTfrrbFbwCrxMi7-8cTJcvzy6-O8YpwA6QJfYhXCG7VeA_weOiWtFG2suFX2nd_xoOpCaPhWr9h8W9fM5XKebq4eyFE9pG7wQQfeG4jQaSryOHw7OLj4Eb9UxinyTTKKz7OLSF3cM7nhnXXuP-OD_GmpqotnTYbqhKw8pCnG28_8E8u-ojiBYp4DVqJLIRrpsxuspCEjcOJPS6fFYt1gP1eE59RHRtmc1hnG-wWSrgO_uQcpgvDHiYoVXHZ12YSE9sjprrKPuE4LWuLrn_18lk7HJ_SbumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31376" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkprrum3pXvUGRiF9l_iIbwYlpA0QczPi61CPdMI_5ivO2r7Y3yIgw8MRw72DFz8mrbUZlvQRF96K_a7cOiUxaGqK4E29tOKnhOrA-Z8mzlh4z82K4GAC865HNIl39qKK8de19pP0v_XiXhIBp8S97xnwyWjI-13s6zP6Du9zQskjbcgiUf-Z9uOnxrt0niHST67m2VO59lrQzskrPmgTlI6-IIGxEJRFpYvWA-N8cKjy61v92PUgDRzeW3gJu0c642cnZEpSA4Kkdscx3hxPkAJXmXxme5kdtBSbVyTdKs3SJGUZpnigUeasdfyFF4WuRbU6by5ASF1vH4Dq-YzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب تیم منتخب هفته‌هشتم رقابت‌های لیگ از نگاه‌سایت‌متریکا براساس بیشترین نمره در هر پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31375" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB51KmheiSB7uxT-4CIlER3YR_G6KNMbU58hOfnAeN4EJDbVtvj47KlmzdJUEtMWEoAL8e7aQhpjh8LxIgsYigaoYNPXYyy7JTiDvzLVktUKFWQZUti8R7sK6IhQoqlu3UxX9b3iMAH4HChEGFUTS7sLTAISSSLsZHtKzTyEiHmud2sL2eQIhHMPZKXuGcJHJbgn90TJXp8t2K554PYsOeO9cGS9foh04dOx6fKlJdXrlvCLmyhcXTnaCpWEx3xFKB5Fqk26z_SjWJHNvFot1vTx9nLMevWQvfZuGauhxLyjHoaz194__4RMtARiurRj54mJI6JhqIt2CK3jhvQmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwij_VzuFrPs4tjydVjJnGHUzybHFFpFs43d5dkKr3iey56FGpm82wUJWqJk4qHEVWdCTV7wSesUmO_tNDRzXG7_WC27frL7K8xz7LX76KBYe6M9vGf-PDyRS954UHH4yjf7mmbMDlExgCP2-tgr8ACBOFRwYJGp2GhXP1tTpeaQXjtIvCFJ78mtl8wYuS1u7VKI-MTdTXhXJnzOpj15QblxEdasXpAYjrpPn7zRk2IU1138aOre-ufTGF9FU8RcOK3yxs22CeJfgpXz1Jdw9xgR4i0bYrc82VFLxFzGhtuyZBLL0EZAZiIKD87s-76vOQtRia-BdmfVGrPyI74zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSw4aXtgBLqUAJrWOsacK8yPgt0vje165gHIAUhj08yOPEpf1yTQ9XSXY_qmUPQq7lTwnVYI2JFD7Maibt4nppzZbVb9UGH9-8KF0K7LNL7K-Z0zLuk5pnO9dVEPSKFrLki0WNnm8UJLqctcLDx0KnBOVRjS3k_97Z0-0MytAmljZfgK307jvZUJuScYT78tEwiLLpWRBr0zSZ_YIRxuLv9eWILNwyAyHTYCx9BH__tAyFmR_I6G2gxs9H8sDjPJBU2MV0h7K5TOGvNY_-n7p7fS0oMMy_lGySzss5rk_kk8KiGn835-yDeCqGsJfeXonXSoYty8Vw8kYk1wg63QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLwwgfTNoOrCen8PXoSV7vso5GgF9GO4BHY1aZDZcRMqcgya-zCMWqc5pVXBnSxfiVatJdvu8pgdE3_qQZEkF4PSgrht-hmniRw2JorNx9ZkKUqiNxTSZep525faXWrcK_CJB32GLuZU7vOCtCyVlKyUtG2GoZvvqeq8G_JsVrkxicq2AvV9Rzh_jEzQAPu5Q1_APjS9JxLaVyoSRXyKfvLb-3K3EIRFteHGhQa7E57vwi2MiY-KEQ5kWdSX82aZq-lDQENNZGcHSj3edvv_myc65vW29021_cl6V3jQak82vSYlZwAIsljTKFa66IPj4TYLw1vJ4OrCj4S6rJAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdXdLhTtYOnrf9veyrGXVv5wfNsOffGksphVipQCZ1GLKRwwNNTDXBTIbLmjr-ZiKSMtrB38Hwgl-e0C_yvxmVAVXfXbwIz_HcXwJPB1BffgUbUUhIDy676suKxYh1zi4z-O5uJVQeEX9eI_OoL85M0ab9hJRaxkOhjRGW5uGAM6qoUz2V-McvRwrxH0G-S_O89JFFQ2FBqahtCXchknkZ4y2fuIWMCW2_-Kj1Zp7wuBQ5-BXjZrTgxw9MaRYZODoq--NKjPgK-33NWFFB9DDav98sp8Hi6FXSTTL81fw_XzXtkhOWEbjQbAHNHAG523jTyhC0QwHeCtOAiL5FJk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3XmSRhTt7zzhuHzFPwVBXVH0chTYeQiK3JvTVc8pO1YJoAEk6US1vml3qpqGnn96xfO9jm0AJ-9c3iaDAUqwbjvdiE7K34rgJhI5Bly9tIouPM4fP3hhxExFf2zJ6dkT3QKiqb4B70q92_Zm0dccaTnzAdjKIYFfkNfSP76IamcmFIUd8LXHm2L4-zZS9jtRzXgDoHylQpeAg2wRgTyVgMCQJAC4kcOLiFcfpXi5YxqotQMxoy7IKeLsiMCI2DhTz39wTFT3XvaMMHWr24mJnA-D8T2Jag_JKCgcHa8gOryS0aE94tOYep9XK9HRSw7-mmMY4pTSvJOswlMxc9ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqS8lVc6NwANsXb1bm_kNVMDQVkoWvQ_ljtgJvab6pDcauP5Ujp2UufkdfXG4wOh4zkPhgmvlTSTz1P6_R6odWIuabCEvpqUFE9UjzpxVeFgdEwywRpdefFN6U5Mfwo5laUkfvMChnmhrgb3U6N47x-F0P_Gk3XHclbdl_D_-9q6oPyG-2WMDB-1gqhApWM3PRrDOv1B6qwtSqgkudKDIIUFkPVHrrVRxak30h8lZKbiZPmnYvFQAeWQwg-0DuNi2Mes7OnT0gaJr2kjU4bfQpfO0M3zIWw80nR_4tojGD3b0gYR_uIRtZyTWOyryxioFx3-5M26C8gjQKV7bM1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv57vaI7ZRX1aVsI1qDse5wH3U1v_2Zn7nZ06sRJ2ijcbz2Ws2DuVvZ_5hWPvqDksId6yAZ7mtQ3o_-FmkJo0Jc0vd1d7ot5tjmBTAWr5e5OBb8HTphBjTD_Eh2iG8vnRSl4c8v5Nod-wQtcuGwVKRzmtOXzFWrr702-UgugP5lm1tzk3WO3Y2bgepCfta5DKojvG_XORUM5yLYsNLwimZ8pXMv3HmaUIvyTIqMR2lgNW4H-Wjqw4n7hQNvShsap_9YA-0nbmkt4dAtRSJWQ9_oj_nGRqPTtUdvjreZuZRzNpVwkIHJ0Uyt_b5AL66JbLvK5P2ichipCFT50Xf97cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31366" target="_blank">📅 13:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31365" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31364" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31362" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=R3JHun8NyhsnH4QjMWNwG370JlxMIayNWGDgoz8dTRR_KE5SXyLHxorsTZdGQjP9XPEDUXaexHpVdq0zReSEhWxBeTcpDj-UbDvQXX7bNBaQ2eSzGJxo0-QIhO0ssoaNHdC-1DL93xTJvsgeVXhuN34Gq7paIiY2G2B4IfHqQ2k6Kr8oj3ewxCS-L6a7PeMBRfncXBFukQUx4dqHpQlkoh1Y3yhq2xVSmuWSbrf_6KpRu2EY3bWPL_dkfynDIJBaaFyhMM8xMnJWY04R1mfqkDxah6s98vyo0FZbPPfiu_ZbyG-bPDK9I--q6x43o5nAsgug_0oauB23NcSUIkOkGV_4y6pr6hiiHgRtyGgcG9pD37b4Q_Po8zjc9CvidztZPSg5yNj1Dt0KTt2C4Wx1gyOxlgXAq1FdF4UmBxK1Tjd-8HaAkocg2mjPlNlGKBQaq0YK3kFQ2KbjOUoCTSKirSqMaPJXcZeheizwm1cbVAdKAYQLaxbPmQmrYTWmsehTdvxsyev-fUAlghjbcqQUB9hdGE3jrOpTwgOc8VaQN4KsjQ25v_VVYSQy-3Rt1iD71cG3nEUR7W4O4PRNu28JQzw3UbBV7l6G5Y9vM0hBSsiK55Y_mbr4zQSZZFWXmBNxiIeR_4-HBPdNvhnvKE-GNA_4o8INLd52S1FMBxjGfAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=R3JHun8NyhsnH4QjMWNwG370JlxMIayNWGDgoz8dTRR_KE5SXyLHxorsTZdGQjP9XPEDUXaexHpVdq0zReSEhWxBeTcpDj-UbDvQXX7bNBaQ2eSzGJxo0-QIhO0ssoaNHdC-1DL93xTJvsgeVXhuN34Gq7paIiY2G2B4IfHqQ2k6Kr8oj3ewxCS-L6a7PeMBRfncXBFukQUx4dqHpQlkoh1Y3yhq2xVSmuWSbrf_6KpRu2EY3bWPL_dkfynDIJBaaFyhMM8xMnJWY04R1mfqkDxah6s98vyo0FZbPPfiu_ZbyG-bPDK9I--q6x43o5nAsgug_0oauB23NcSUIkOkGV_4y6pr6hiiHgRtyGgcG9pD37b4Q_Po8zjc9CvidztZPSg5yNj1Dt0KTt2C4Wx1gyOxlgXAq1FdF4UmBxK1Tjd-8HaAkocg2mjPlNlGKBQaq0YK3kFQ2KbjOUoCTSKirSqMaPJXcZeheizwm1cbVAdKAYQLaxbPmQmrYTWmsehTdvxsyev-fUAlghjbcqQUB9hdGE3jrOpTwgOc8VaQN4KsjQ25v_VVYSQy-3Rt1iD71cG3nEUR7W4O4PRNu28JQzw3UbBV7l6G5Y9vM0hBSsiK55Y_mbr4zQSZZFWXmBNxiIeR_4-HBPdNvhnvKE-GNA_4o8INLd52S1FMBxjGfAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌فوق‌العاده زیبا از جشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه شهر اهواز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31361" target="_blank">📅 12:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31360" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVIouCotvBvlj9l79_M33ydmjYoC8synlRPwy3v8DYBjlkLmUM4nns2kD1YAT-_9heeTrSKGYfZyTrvFgOpV1YMgvQMVAOWwib1_xiW8NB3GxjGNIeH_3JTqnYrg0xyMtkC57vy8xgBcYAENZJ9tNdvjsrekWvdFuGptIGwCN-TbvkAd5MYByFAteHNgqO6carn1mYW-619iiQOqxNKAHFzLKEpPrmCN3DP63jhjg1KGgZiOYEDmhw1JPWljdmkWGFKR2oKqOvOeD6T5UQFzaqefq3pRgMGg-4RszcvYO_SNKAnUxzoYt20gOARg0cVI7QIf4zDaEu8O0aao_81kPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس هیات‌مدیره استقلال: با علیرضا بیرانوند هیچ مذاکره‌ای نداشتیم اما درآینده هرچیزی ممکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31359" target="_blank">📅 11:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxfRESmnWXxmBftF8dmItJUDtWW71BzERs-y6f7KCVSd93O_WIy75e8fwA24A1xKO0te6h34uHb8VWh6CCrBDEoUphGUy-0ARG62DPjJFa3t3pgA20OiMothCxlDyRN2b6qsNnLDlKbKit-SBvfcSGEPsBJ9St6bg3ARuV-GGuVqQzRlJ8c6CMHK5rj00iMg9LLiRBPvk8Ny66MqtjbmtDXV8YHBHvEKBtFl90LjdS2jXZcusK58K9a5lSDfSaW3eY_jmXQq4vMa7mHky6PgEiyZTsvZort8YYKu1uicPpSNhnlrQYi_KqB3WzW7sf0c3PqENjKcwXdm_jj7-_5IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31358" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubJLn3kk9N_e-bdNa_YlZ9_F-FY21WIWv3HzK0k2i4Y4mUJHXwY0s0jIsAM7a9reMGDpc8VH4h0Ldyp5pD6RC1hcLHYQR-W3-P37SFkIUYllZF2n_xRSbZ4Jpef1b25hskFgweFmH8j3MXCGIhPc4m5YGfWYZLGM0QLCZkX3J01WeUJfbgk8WegB1_pyztWNo6rwhLi3EzkoihpTsbthwtxX1t3Wlm7HmsrEEWLbh0gMiWHMfAezsPNtSae4X7QhJsHFrz-5x-0u2FsRzH7dMEnwwYIHVZbxmZJQz_j-jT5hTu_sqDWAL9GAS1AFBVt0D7Z3OSMCb7E1GaQiXRR8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGbHjOhFeJOBKXUbCRI7SB1XRzaUARRlA-qjvyZph9a5r2kmRdrFZMy3XSA440g636BumCI8ZIk90tiK2mwXDxIoIjMUfXiNsvXTmPTUA1Lf9PoPjWQbkDmDN-hLk7lMRag8GdVS9GLsrE3xBvsrazGhcbk5TqyjcFyflFMk9i6i2C0CfRyGp3R1cslcbolHygmVzbWAKWwloyDbyw6j5Q5AkbpCwSyLGFZhVTjRuDtm8sY8PzFwKHwsqWP0Ht3MtXSGy3TqOobnc9w6uiABeFN1btk0q5aG5wU3XYgP4EqrTKF_XdTpxYaMOK5KjVpg-y9SygRTWlqGsPOP2gvPFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
دبل‌تماشایی‌ومحشر لیونل مسی فوق ستاره 39 ساله آرژانتینی اینترمیامی در بازی بامداد امروز این تیم در لیگ MLS؛ تعداد گل‌های لئو مسی در کل دوران‌حرفه‌ایش به 934 رسید و برای58امین بار از سوفااسکور نمره کامل 10 از 10 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31356" target="_blank">📅 09:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS5cO7bAJ4o47B4kGI2YeJ-Wm2H5ky4kxah9OaMbCMAixRh_7o6v-2b_UEUZS8plVOU9UR9DKiJvfXf6XJ-5maLCpjLzfkWGhybf1PSPoUB1tAyjjTDGPnVNm94x9VBFTpAUlEhDIOTAE3_DqKFVyB3PwGLoyR3cNHmC4LWwaac60b_66aTRgRTnNbzCgz_gHES3KbY8W0GQcP13KTQK57lbu5BkucxhKEMv73vRt4ekI1jPmoL4InTan1XhDk_XTT73fZSHpzVE3oDkjlONggroUKT-7jO2sY9ZdpS3HXrR_vbDz2dxXggqk2hsy1WaI3Ga7clKupjdSFSSSAQrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=VAO_u6P9aDnf1rfq_6WQUfu-0T1cOH5ssz2aZrobYP1h02VvSZu1TIPbXq-CrwdpGuEWIy-MnrlAWc2Pz8Qfg82QWDoSbLOklCFUwp2f2W19DpFWR4c52nZhLMqEqNkmed3E6U_o3i6-LEiCx0tHJi_C2v129j5jfUpme441f7rP_1HS_oRuNR4IE0wndY4h564cQ9-XlM-ZDY4SdlgRwsiwuy2YbmYYP2LXnywPVLt9z_wm6e8Ugg9WbYYrxbEsYfjgiRdTB3O9gmfNH_85uMbWwIHSgM2TQs1kNQduz6SMFGKxuN8GLREIIkSRyghJRZd4GVrCLCahE_imOialnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=VAO_u6P9aDnf1rfq_6WQUfu-0T1cOH5ssz2aZrobYP1h02VvSZu1TIPbXq-CrwdpGuEWIy-MnrlAWc2Pz8Qfg82QWDoSbLOklCFUwp2f2W19DpFWR4c52nZhLMqEqNkmed3E6U_o3i6-LEiCx0tHJi_C2v129j5jfUpme441f7rP_1HS_oRuNR4IE0wndY4h564cQ9-XlM-ZDY4SdlgRwsiwuy2YbmYYP2LXnywPVLt9z_wm6e8Ugg9WbYYrxbEsYfjgiRdTB3O9gmfNH_85uMbWwIHSgM2TQs1kNQduz6SMFGKxuN8GLREIIkSRyghJRZd4GVrCLCahE_imOialnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOpSZwFapagUjxBC7ooFlxBCuGZVuilvBXELGyDiYRZqZkPSOxnFYG5dMuPY-NthLvpyNFjr0zSGvF1KQRCnTxK8nR9MHZf_CrftYvvT3hSykxV3womazyBMZBqXmPe7R2C4Q6BM6htL6LUpBEXEdC-HZlPpbiOHELR4PvQNZzW67luQpQwhLydqGTRxqXuo5RbINORGktgH3cYdSVV-818g-gnPVEmu2CqHkqE9eHScXXmt8W-Y-1JACv6voaSc8R3jjkRHCqVpBchzA-1WH2WOrG5iNUV6qlOIHYj3AS8B3uzATL7c3hKckrjUjJODW99dZ7ivbRLkd7tdOxQjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4ddsS0gxFnjVWhhSdWYXGu14P2pSDXUEK_ofiJzGQg4lR-SgvbYW0Yasa0zQWGv87TrYnGiS_6IA8_H3moyMTUKkGsY1EvtvEiYpxXfPuylqLhSU1YefdFnyPqmVdjhlh72_VXlvBeZoZ2ubQx55B_lm5FEsuoNogeyVOvfr8EMORYBWGYjhsde8p8Rl8emd_5Np8Pwg5pwgZEVOYGWKXHKJ5UCIRZeMeqvgCC9kf5JMID3NbA8fl4qoi7JER-cqV4NELb4pUNE6ZXmQVy2M66XSuzUkjY5Zc6n4O9M2YrooBOOZaa9i-yPt_yWEzhubsd5kbUQgC8WDEwJsEL2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDaCxtgQn4Q6iT3kWfxdR5ZyWasyP6_O_8SQJp4kbCVKU269p0hvW3ftXpHuU9735QzHbZB4qlitQFMctY4cnJe5wp125FtGQXlis2wTpkq-sJyd6YDiezqfeV5yn6VHJsOI31pjm31o7qsdbCi62X9X5s2Ys3jO5rHQzpcssdrDAqgaTc2_Hl8DAFDJUSv2bogsc6GJJGh5XQ7hH4EM7SPtv5NXvDqSUirqCkB80o-DJrBeOrV32q5JRUjbfudJM80hCAcPn2Hi3jQ8PdCjMgi2gHQXJrb9rTzewaVtPABkqIfZ8v4Ywbt1PEdTMP0zRdNyJm-x4zGy9ah1Cpsqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9P_LFV4xeAnEhVHqRqUYabDStzgfWTKZZpgDU8RKaHrK-8KFgxYyowJsfP9zStbJ9XFxonsWkQGhxum1cU5ip3F0h4CvEVKvDDpRTSMIF4Kyfgj1euyzuGP3cNY69qaOpvtp0x6nbZUFjYfMgSoG1gQOnSFW1FwTtXVBnPh_eEc0dzWcxxK8W-svr8ljlF8MisilUI6yGOj5sjwU1389eCSp1YKsJdEc6gW5KbmXMWPCkjbHP4wHJRU568Nfv3sbz9JPz2MGuHDcHCI07sT-4O9wO67gvzZ-_p9RvXGCAnPN4byNNKi3rMLkbV-rEEBWXeP5sJuARnwbN9k7pXjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLrSJuW-mxLYiqh2Ele54GvNBYaskl7HsOlUCDo-PZW4AsMc1zutnPHKqg0eB7B8I2c09E6j5VaqPKfbMfygTONoQgBkSnyPdi7tzywUYVmW-HbZw00ApdJHf6lBqIA-3_9txjsPhH8k13iZ5eX15xhbc1uWlbr_h0vlIEIr1a0goOO0tXJOCp7CdIm071b81AF6PYjHlXDiO_-BB4s7Kd_uW-nV3iKSEJJiAIs5VNFR1QN-rpZORm1zIqhX4H-9vDsVC1hl7CehKLK5ZKPjY8U4BBtI8SRnL7Tc17KFFyj9oNBuE7Whmpf-svGpMBx0B5Og_b7VjJKTiTklWOahlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mw2tjgYA_PTREZhh60UokdKk7wFqmNVCNH0PmGEsnd0YWmKhWfhIci--GscjjzPK4VNHoKoBiWf3K7gMW9a3GFTChELcMr0fLw8DdWNtqHIobNSUkRmwYhgqIItTG2BnT-9gs6RHh_8ovcOTLssjrjIUYbaiP7xnK-hal03lJeNC5Jmovwxp94CE7R5FydLJxFYSaSKdjPGf8ByS2ZFhDYVgBqCqNrmb6YfjNOYR_7sZiLjlOwrB2pCeJA2iLWCsQwnxe8FYKjqyQqm3_Z7c6UDfpg0rzwarG4Gt2FQTbcrf2NQEPhTJLwVncv6N84np4QQD4P-1htZDl5vUJJG5CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS4Zm613OtQZYdA4n-jmofnLJdtVXtvq0nOAKMmFIhOfFOuN6k4YySjEnHBNhD4VZWftYAN9IbfrJHcY5I33RSI33o70fRcfnomYTiV_UaSeQBjXvqua-kUIsrFElXWPecTHKDQES75c63u90zBPKrcgWpUYhFHZGok3mSRU1JakDQRGjRFaDZfqco28UwbykO0RC4owDyEV6TD8lQZAbV0nh_QYw8CGieFaOOu4JTLQzFYgA9grn1sU-ne8Q1im43ZfTfKptwJCVnA4_0XGSHRnzNztC59v1uKKqDeBfJy2Yv7Hu5jtfHWV5TjtrndE3zKz7gTWWF-Z5VmqN1aXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNh-eanRsdAxL4gDwNjzU4clrgEldwiiZpUZRQX6q31R5DLg7lj6hhkIHCD4YN5CHe0V4U7tVnSi5Xn2TW4AYyvITTDUyYPmY6MRUKjJYTxZmb18FTPjUv66v9Wjf_TYCmChYix5EnByKcDrdRNLFKd4d5ra_hoBhB5aQTTPNg0x_1ZRTmsDXxu2hqCoIpMo1tFB1ZCdsQ0ulLQx7OFjuBxJ_Avpjmsr5hlIy6YIMvheypUYvqzwNplqA_AIE-w2TdaAMA08IVHEpDHqtZtnXLD1oyz1bb-Y3KNSKzEf2TNz93eGGMx1s4D-eds_6eFgzjZT9Ql9Tu-cbpabQTYC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPYetxtdbZXnPrPA6VS3Vkt49JMDM7NSiMli2ze4CHZedYXHkrbBU7KmyJ2TSHsSyigcBFp_1CaoI0Jzow2z1eTawZ-ymsDVPIa_YsLH7doULpeMaKjZO7DU-x-wHvUIMyC83yV_iWRzxRRQKLvJ3qr7VAMgoXKrYbkjF8JuvAshujsNnxaqQZp3tLedOUOkM63_Bn20-FLIrH2YA-t7EbXYjGQhu6DBg6dOuWTF_E4XYkU_fnh8NivxT8ljIdMcuNyTQuiLiXZHc83NgU9m8pIOwSIBqZqPswqS4TMQ87ZbT0mH1awJ7K371zXYQExKj0l_dLO1Tig31O7ziwovnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJOu-uyZofnOp0NvwzDrSE3ONnEdikttPzas74cRKM4MQztdQ6v6uLz_-xsVYxb4WfgZywJrr8HLiyvHblpE5jpsWmAZ8Pn1wSoVs2MWa8UD2K8FqYWHL30CazfZJyUPI1VAm2WRb-_dGcXrcio1vzihuJK2lFwlAcAQ37-n-x9s0Zkp39jUlhkI5HnJrUCmXWEiHkZUjUlHMlSl73NOKtO2G3M-DvZghWM7HwVTNZtBYjgwvs1s-rMNv_-e-820PJiURpqHliDf9IgVzxpddlCnRYNN9WQyNi8YJ3L5VhLlQAnR4nPMGvUos8__UiqCaAybexroYMMj-r-jFUS0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=U-gyUTbLmkRNkBJOOkNd51sCAaGmdgtjxqdqbGGTrRzwyEBxb4hynFiA2woSah1z1sojdRj1G8UHKlNH8dpL3pQftfPfjIXZ7ci_2RFT-YtYT01QosixgQ8zIBomHfj6aPBJNT7JrgffUFEP26ppx9WooUo5iG3u66apZBnBzcjJXKmR2w5RSsJCqOcR1d0hziWyQuYg4h1Qc_I9_Mw18VdGCdogWsk_1OWZigKd3_KC9TXh3xJj--CqwFxcV6GtQ1Od7XeI-fhaonVPPYFbCnb3IbiGWUonwPwHBEbVXrHSRs_wwGxCBGBxd1qy2O51HmwKPUF6XOGtnz2RH0Dmzp56jmnuLJc_wvrm6fiEeed690rZomeFQmIMjDcOK_3J_-fZMWq05lBsHjw4FIRG0qq-WKjtrH6Bv4oqOFknwpFTt7GWyJXgtyM7OaRP8jaBcMANbFYgVsuMafnSi6CA26zvmaXtvgd5nlIDZIDtsyH_LFhtIRfIm-HAC-y7wVA1inFsDklzKyVlGY6K1_X1QqdkxvPnctZ4pCoof5Q9NFPY-exMNEkMYgv2Sw4GPeJ4_gZFwE5bYUYvOcGHDKCV7zAGWaexR_yTsTbOINBoNyjIlCNv2P5VRRtCYE1h9Bvhy6W7bEbvEGbVkjA3iO7ByHnV5mTyJSBbADy6xceC4VI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=U-gyUTbLmkRNkBJOOkNd51sCAaGmdgtjxqdqbGGTrRzwyEBxb4hynFiA2woSah1z1sojdRj1G8UHKlNH8dpL3pQftfPfjIXZ7ci_2RFT-YtYT01QosixgQ8zIBomHfj6aPBJNT7JrgffUFEP26ppx9WooUo5iG3u66apZBnBzcjJXKmR2w5RSsJCqOcR1d0hziWyQuYg4h1Qc_I9_Mw18VdGCdogWsk_1OWZigKd3_KC9TXh3xJj--CqwFxcV6GtQ1Od7XeI-fhaonVPPYFbCnb3IbiGWUonwPwHBEbVXrHSRs_wwGxCBGBxd1qy2O51HmwKPUF6XOGtnz2RH0Dmzp56jmnuLJc_wvrm6fiEeed690rZomeFQmIMjDcOK_3J_-fZMWq05lBsHjw4FIRG0qq-WKjtrH6Bv4oqOFknwpFTt7GWyJXgtyM7OaRP8jaBcMANbFYgVsuMafnSi6CA26zvmaXtvgd5nlIDZIDtsyH_LFhtIRfIm-HAC-y7wVA1inFsDklzKyVlGY6K1_X1QqdkxvPnctZ4pCoof5Q9NFPY-exMNEkMYgv2Sw4GPeJ4_gZFwE5bYUYvOcGHDKCV7zAGWaexR_yTsTbOINBoNyjIlCNv2P5VRRtCYE1h9Bvhy6W7bEbvEGbVkjA3iO7ByHnV5mTyJSBbADy6xceC4VI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORR196Qy77yKDDuQneBkYBFAgohppIeAgIMgK_6cEV3rKYS45YejPQrjF2PZfSGWVNEdNhYWlt-ZHd-Vjp8F_UtvDsj8zRVxia32gtaeZUOEckgrLvyeqtWkxsdFlndHd3v37xNWtvkqRvJ1vwbU0gicJRyqdZsjttrFbkV5HJbqYNDMsJCq9dVKQdJfOIT90XGDlM2E8FBiFp4FuTo3IJIsoDOmLyJEQhXuLTZoEzHvSLy2WRfV7lmveh3ZegkGfXRofEoCt074tct79mHopNCFTvqQWUK6Xd87DXld8vUWpyaFoZqXZImsnuyDMvr_m0EMGoRANBM0yo8xAobIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pl9YZWN4id_WoOWjNP9OV4AFfWUOhlhon8LHXrzRwpaDS_x4fYfRyYEv9R4i3rvSt338CYRQD_rpMK_mvwECOxFYgHdfUnfyjwqoHxnYCO_2AYeqmHxuAl0U7vLm7r4w2EnHNUCgILICRBPBOxcR2G7_nJ1vRpHjYUL-MJnaTxSyW3RelVWd0zBcyy8nbjIxPe5mgK4zrmgIlyRc2Rr33pHMHtEWLGNXAb1DTVNnhEp-Md2HmotSgVmZxIVUL2IHQFyCUGYwDichkD7kQUP8drCHSB85CLSHMs2aVGk1RDdYdsL0RoGzE5FqeBII4RudogQf8Gmd5sUZ_T_H8f6eGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1p0OjP4iz6vvMJioSyAc48mRDskgOAeaUUtWqx0axasCkvKtkQp24lNd01vDXFibpLbbX4vq4Xj3Zfuz7keYy8X6icv_GWzznaptKg1NwPVh2rb28VCMz2xzNnYqm0XTJKNWKENNo-Xt859AkpuAT933VDjYiRBwkvBKEaWiSNYKF4o0LaqlyKV8s0NBONQ8WR-0mEDZ4KO3a3S06xQp8cwshUcIiZ0xtYR_azQjgLUBWwOGf7iTJaRvcWuyIWwmHaDHMtb9p-LSIMX8rb4XzE_KluC9Yys00DPXKfYTbUmQBLUKJ1tlbOX-9eC6_neU1quZCKmTUSFJD_deSuwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_2pDLTHCG03e6SGxU80VogcOqaxgZGRaQCVVfn3ZWvkbGcLtQsFSys69lKQuLU7g3_ojhR_o-9LBs1_mA6jK6NlrzRCApsUiGlpN7BoJ2ErjsEdt1jvrlcCo3e9JXUBlmNVAdxh7zjmlKP-7mq6Nbm6SC_RQ-V3mAyVlA9SWaTbnEJZGnyZOox-GIg_kI8-gWt-9IGlGn4KA7Y7TG0Qh1bMzlpMPa2qdkVtLKeza7O90WCvxB65SzFO-4sRZ2KGC81vKy0d6vIm7wtoaiKNrisyiQJCIPN4hs38IOsRNgZNImrIvGaYmpMXap8qiodYCuZUA5sGfedYOxZ4p8gr2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_eFf4cvYZIclRUgt3x1nDVf0U9gXhWStiz1MwoB_7mHEEtgPhm2qhtMpP-Fh1I-qsyBcf5sdi7ywyBlS-XvKXkPM8bWFPatFI4bsLzA2mKxsSeueedUQqb84Nec3-D_rKzvDaL-LMqO_2wym5YgOzzcr1zwhL5bWWbOFR-5fvhTABV0zHdA2IAoJptJPp4DljZx9yFmYuRjlXMO_PDmXl6-Dp8IK5bpSnzE2SWFYKVkXVJxOps7ckmNAD7G5lwfLqBXB7Oi0tPO1Sz_LQHUowcZ_9S5OzDAgoIptWAtzT1UJ4VhtK4sE4h1N5VlF2lQ9SXKAvL3AYMhKdfhAE2UCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJiKjodJDnN0cpEFQOnjkDuPSo0vfNNUH4H7g8FldIi3urYomSJSXMCwWyvLFo3PMVL3Zimybnk_uz0ukV8VfGJGhwQ2MP3aquxVFJD7iQVI2lW04nzP0I0kq58AxWXclcY5Y5jjuZcL0HCOguICotKzEM0Pt_YmkL88-NJn8poZjt8sOMdRyAbfeOQku8mPEhUM_VNc9gTDBAhEYQHBTRyKfRzsC2t8PntcwBZFPtW0R_jv3sLpi5hSN5korgYuknWxHk51HwyXBL1wG-pKuQwvyDGAIUOJPdKCpx8-vmbE2MFjmn6LT8N2xxoi2saWUlLhHnv_SIy0SKsngRwMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=f2ECqJfxggSlOaqh32vFw3c7FMsectGR39OiMgxXKmJ5l00jX675NR90AeWs5k2b3vz6YyzAEpz3D8LTEaOFak0KqCm0ts53EGqV0X82mq8C9vMiY4qp0VndRMThcfBc-KwFTe6fZ33DOM94v9kwKQcGRCrsdVn7mImgWjLUU2E6wm6qij4vF43HlCHbg8SO2oItN6g1Fg0lB0nBmzK84ySN7xBavjZOzLbTmeKeDKlg5MeiGglhnqNbpPy6Fun9HpKnfIsaAtL64HN5ioZ9bqC8FX15KufLrcyeprbAri_4y7Wcs5STC_w6ikymneeUo5IOLiF77YFo5MBg-511NJBkYNmEBs8XzfmkHJ57BIqPSECKgf5hi37nAjH4VVfBJMhMHoXqIf-22UuWqw8fpLU6fx5Mzxb1ngy3AZXQl8is9lUTBdjiBjJMwdVbmYPNIZdGdyS-lzGv4-dF7JrliOiYbieq4hnybi9ohEMxC490X3roVyLjgXOiAwb4sRN9Sofk_1RTie3RBKSRMRQCSgg05kEdl48YRJbNJpYSl6yLNicSp4dAFDz2FQ48KVw3e4Khkhyi5xba0HTe4X-ewUaZa7us1I7pjZBa7xhGqNy5OSyeuNOm3aS9Z-db4ykt57HTu3HgEsPUAt_suttGqA4pOyMxUuu8EjR7m72-mKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=f2ECqJfxggSlOaqh32vFw3c7FMsectGR39OiMgxXKmJ5l00jX675NR90AeWs5k2b3vz6YyzAEpz3D8LTEaOFak0KqCm0ts53EGqV0X82mq8C9vMiY4qp0VndRMThcfBc-KwFTe6fZ33DOM94v9kwKQcGRCrsdVn7mImgWjLUU2E6wm6qij4vF43HlCHbg8SO2oItN6g1Fg0lB0nBmzK84ySN7xBavjZOzLbTmeKeDKlg5MeiGglhnqNbpPy6Fun9HpKnfIsaAtL64HN5ioZ9bqC8FX15KufLrcyeprbAri_4y7Wcs5STC_w6ikymneeUo5IOLiF77YFo5MBg-511NJBkYNmEBs8XzfmkHJ57BIqPSECKgf5hi37nAjH4VVfBJMhMHoXqIf-22UuWqw8fpLU6fx5Mzxb1ngy3AZXQl8is9lUTBdjiBjJMwdVbmYPNIZdGdyS-lzGv4-dF7JrliOiYbieq4hnybi9ohEMxC490X3roVyLjgXOiAwb4sRN9Sofk_1RTie3RBKSRMRQCSgg05kEdl48YRJbNJpYSl6yLNicSp4dAFDz2FQ48KVw3e4Khkhyi5xba0HTe4X-ewUaZa7us1I7pjZBa7xhGqNy5OSyeuNOm3aS9Z-db4ykt57HTu3HgEsPUAt_suttGqA4pOyMxUuu8EjR7m72-mKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wps2VtKWkR6ah3J6b_vXtg_RHot4a0VnU8pXLOw2SQi6LDMOH48b2-s8A7O0dFp8CA6vmoaoOnBetkvCvQUzkzJCv6zwgxc92yUJAPWcLiLGSKTBOLyjc2q6kQzSlAbwvQ-Lp3JbS1OsG9Q_7q_LKgO4c-2D69uR4DfcspOFsgVJ9wsKBeZPp5dma25uCr9-zY8FUGLhbrD6BWlNG1uA9syMpjEm-dT6HkS7bVp2DfgucAfBPS7obF69c2cI0ad_d70rf6pMV-wEHXxo1YIT8LKGyLIte9ph-gJsy2OKIACGeYmGVAkHkaFrNBKelUMstxO3u9YfveeEEqMubPSKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G79IxWwLOx4ztpLMqdCugBg5TYWDkzXrD5Nri8J-Xetn_CdfpQ5tm59ow4WPc5FGa6gWaq3Xfaw8no_SuanQvrUW7OpWJrboUoP6a8OHV92Ytm0XVIualeRZeSs76KD03E0DwGGNHCpiK9m0Wl4FDRxoR9TwvWLNRrg_oI86DSu0sbKqAOBKU3j2NHsJzer3i0n1T8edwi3SpvAL8Z_yAhdUG9KNXJtFm8ktHeIeQb7t5Y-mS_Z-53XPpV9j8wH52F1Indo9FwA4YYi5N9LqgCj57AB_ovKGfQ-gPFsvqynA69_SmfCgjURIj3AxoaRW4N-rAENsKQZhqEHPcBDUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5z4u3KeE38JK1Q6rbweWPpYwFKmXyW-nj62RpjIMSZFLeXojrTJVPoOKWpxTeZtcX9drOSlolS9KiAbjV_8dVMS8n0dAKOuKwCo1lMWvGW090cDbx7uGHGtAWNaHIUAkyVBK5tDUczS_ImlpKyE3RgOw97K-Ijpc2Pm4Ogubr-nT-edV65A7kxx53VYy8Rq3ccnmBTP9mPoy1oStVUbSlXzVrEGrDrsCK3gv6oJvYW_XIJU-Gp7mnjNqHG1TSzJQFkjJ3QZJH2GNbR0_1drySg3n3KKJCJ_zPpXyr_IVksZjKgpRJJ0lKrOu37t_EbQbUSU5V42Z63HJN65a-T2UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6F6K6ik5FgoNROYbOhcZNxIh9K4Z8xNNXGI_EZqW1qyCEa2Gz6Nba10_zTF9Gtai3V3TTAv_kZfRGJ7nMHFANpCKxRQ2zm7UEatqBFcz6y-jVCRQyOEi4qAns4uYAOdt19NII9Laok_M4Wgcar_5EAqT2AnGW9OnaKMTpTBV815wwa1t6qlijZgy54BpHmp5ybaT6YtZkZgLb3V5mrCtbPLpl2kwdGy3OC8wbsPCBwsg60qtitTU_pW0OgHpajpWr9gboXj6spzbbVQgrCrXqeVrW3-KRSvlibFF2FGGYASlkm-aNwddH_Fhmkb3YmoaeLK--2zJBwyUg2_h_2kOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2kHwvaMbHNyjgzQ1uJxn0vknYKIhSfc7_FHlp5kizp8-aKXa1XGCrdjh3FAQhnqZ5S_ujrBSl8nxCg1hmw_TpYIQndPrdQU4Q3dOCisGslj4BgbRip4kqTg4BP5rtkQAXlUMtD_Nml5ABYGH2y6pTYAr9L9Qw6o00j5atIFM5I9oVJfpEDcihraZw80NXQ2iBYmNReNFA4SSoT8Z2pEcNMVyh-gvMD_JLv-lv-kMQmwuQYXhUbUJ_HnsEa4qNPOk3jRKPpu-_jKv70Fwmjp4GKrWFI9ZjnHJF5JorKehFoTWsQK4zhvpRv9wrB_7ZlLqYr-7pE7q0kxmDabXnB-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkhyRL682a-Q4xc0dUykooGlizBFJrayhQGwVdQPTNBcAs4KnJDPq3-FnGfve-KysdPFe29P0WUaRt3hxpYXgQ5A8_goUGNMxTYpd4uqDtczFIoP0-_lHn8Pd6EgvYGizc-ASvNSmPfdhmArc59_Xrk76PMYHs8LFLNmoIWU3JVocgxBkZfAn3yTMN1TqzctnJa2JNnsqBvteuGAj6QwWXjg7rrqLy1-dwt78G4S5MufVH2NHLhHun90p9d3F8Zl6FXF3rTpK7r3BWjfzjJGjkRWKtctuKE-lkMSqTcJfhaf-oq12dzrWag1nFeFiAvTVO_mZXoDDsAra1AgkbSRpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=S6y4nr6yuH2jNfsOQ6pTBQeYZABmD469TQkrHnqnoCxGozsqgWIfUgMApAmN85yo4AfhFKOEGpMuBwAnNePGylEn4q57889ABCwGQNwEhKmlDXvnZLtZSyo3TXtnES9h0xd5XPkVgnFsT0e3HxNsuQEiZx_KWoNgJkWXX8MfkMkoo9yQ4XzrMkVqroZJEH9iLF5JAFfMk2HS1bTvrd0-s0h-p1k500dtPnlUTILdhwSWlGG2VadO5mgDRMCyYESlhxuFYAc_VHYAhVQNAyBeK0xFS6vyOoH4KxGiDfa8zSG9qjswiR8ovN1E6z-lc6ROWqZPGhd7jTTEkVLy1IP6CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=S6y4nr6yuH2jNfsOQ6pTBQeYZABmD469TQkrHnqnoCxGozsqgWIfUgMApAmN85yo4AfhFKOEGpMuBwAnNePGylEn4q57889ABCwGQNwEhKmlDXvnZLtZSyo3TXtnES9h0xd5XPkVgnFsT0e3HxNsuQEiZx_KWoNgJkWXX8MfkMkoo9yQ4XzrMkVqroZJEH9iLF5JAFfMk2HS1bTvrd0-s0h-p1k500dtPnlUTILdhwSWlGG2VadO5mgDRMCyYESlhxuFYAc_VHYAhVQNAyBeK0xFS6vyOoH4KxGiDfa8zSG9qjswiR8ovN1E6z-lc6ROWqZPGhd7jTTEkVLy1IP6CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwpDCqPZfTqD1CyiSA9cwoDUyENfuWV997FW0uq6X7wPVVybhksA_Zvlx8GUnlXjgXqeS4DOEdc5hhDTJopSUF3Bkb9HC-9b7XUH6acdWQOJmcqMbdaEupMtaxeWx5EiD6eDFeiHKzYepa-C5el-7cTLxPBx4rAzH37QGYk61n2w9uaivANAv-dH-6OW8Db1G2NxN74dYmYe1THDrdbtCxV2FVhF12VY3Td41s-ui2SPTij7am4D1nCTaU5VsUPCyfvEEOtQ9Jvo3M5bIaSFvJOfZb2Uv2YEnfDlXE1x9xgvqDLS8XxmlmpCaiqqTaX_yLZ_z-y0IoXP7WScbFt6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzvtFkUVYaHBEyuElbCtbkQeOEmNKMT5RkJ_9bWYbb8LsqJX0Cby-pOD0HLy96lR1jU1NroE0WugH8JluQ6Inwi5llBPyr9q1uaLR4wAesIQ_-J8Pj-FhAA3pFyk_aH8p3z6x4MqrxEd4G1h7DfLUU9Xo1KVgOECkw_LzOCJlNoFFRA161LpWweV_8wrY7fPmbtNbVOVRQbB11q-wqumYRkVZ3Ho3O8o7IbSQkPFkDguL5wf2JzcDjGQ4xZtngjcggZI8duiM7b3FLiW0IZUo-suU70ekS2mfW0VLpwnoFQWKRQ7CXSM0tMWPyKefiZ4zjBwsMtYT0lhz5U8ugMQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=OGurQ38PDea8zP5OrDnid0ORmuOB70RFuA2H4xcHvGytILHkWTUHqG1ImlrsQILxc0PQtMak-7yOeTTwof8VMVL7uaQZgg1nG8pqpepXclaFeO3SysG56yj-zqGtgG7nBdsIyxVV1uybDLi3e7ECls02C9PySmcYCWIAm85Q6OytHIIv9PoTFD-coJlxFV8r2BSRjUWUHQkzdAZldhzq9iq6xtT5oJSx08RjLoFtah4rJBBbXyLEkFndk9dGzAnNI8-33KqhSfsiX7Y_XNknRy-mM8Jhx5ClZwZioxXDOsxBcKtEFCc6KoDYweXvM1LQ-J2_zq1agnpRsIjPqjMZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=OGurQ38PDea8zP5OrDnid0ORmuOB70RFuA2H4xcHvGytILHkWTUHqG1ImlrsQILxc0PQtMak-7yOeTTwof8VMVL7uaQZgg1nG8pqpepXclaFeO3SysG56yj-zqGtgG7nBdsIyxVV1uybDLi3e7ECls02C9PySmcYCWIAm85Q6OytHIIv9PoTFD-coJlxFV8r2BSRjUWUHQkzdAZldhzq9iq6xtT5oJSx08RjLoFtah4rJBBbXyLEkFndk9dGzAnNI8-33KqhSfsiX7Y_XNknRy-mM8Jhx5ClZwZioxXDOsxBcKtEFCc6KoDYweXvM1LQ-J2_zq1agnpRsIjPqjMZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=BZHMO0RgPjGVlT-oE6ABm62qHCnbr4Is5d8P0D8PeHyCfTT6IIhusqR9Yp2QvqKQNewpLJI1NKc3OprufQYza-Rw1MOBRChwXtLpdcehk-pS0BtZ7tkeob5ULqHoU981voQHHTVnwS5ZE0kgEjjjEuvnOmeT4WJFUeZxPKsOcGS243wjfQWm7sZEs0nxzJDeUHhV4X2FdzKBcXyJl2qEkFym4rkqRzwN5MeZAdnpX25KGFOP5jqMSwscfj-WcE_6DFJ_0gyKLfgyusPA0Cj9yAM7NaanM8M8QMXUUkZ64bl1OqwryhqfZUamKN93qWrb2hXFDxTsAP2LkBkWqEQXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=BZHMO0RgPjGVlT-oE6ABm62qHCnbr4Is5d8P0D8PeHyCfTT6IIhusqR9Yp2QvqKQNewpLJI1NKc3OprufQYza-Rw1MOBRChwXtLpdcehk-pS0BtZ7tkeob5ULqHoU981voQHHTVnwS5ZE0kgEjjjEuvnOmeT4WJFUeZxPKsOcGS243wjfQWm7sZEs0nxzJDeUHhV4X2FdzKBcXyJl2qEkFym4rkqRzwN5MeZAdnpX25KGFOP5jqMSwscfj-WcE_6DFJ_0gyKLfgyusPA0Cj9yAM7NaanM8M8QMXUUkZ64bl1OqwryhqfZUamKN93qWrb2hXFDxTsAP2LkBkWqEQXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxKUdG6joFuSF-8kfcvhP_LNSOz2tmHsX1rm9_vTqw9SYAbLgVafhvBq7eTr40rc60UBawXCxnQND_MF_E9f7uuMae3WGqC9tsC9PdruMpyJ080nEKZN2XxS02VC1e3f32aZ1Rmfjd1mzr6YQ1KeWbCBlDJC80qyhR-QUCBtBp7-SM9YBVv03WF7sdWoc-LXfmwxSMl8Z5UbQmsH4bgc160IK_yauVWQpxLmhYB9hqxZcsinQvJuX1xnHrZrapFnP5b3XAdgYH3tdJo7kuDWKAM3k-GScbGKNFP3m6GeXOkLaquS7AsCesFKDACaBzLiX7h-P8mO-2fAumvT5_YkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9K29Y9e2Ub86yLfO-Yv8b_bLfOBvAXLBqfdhb9urHKlSTYf_WqDUZehitu0DAcml1OV2K7UagT04wfS70JBUz5ouB9iubs6PeurleqKFfffJE1ItMBW6k11ftOTeT5ojiHR1UMfnhO3mOW21z06Rv6N9Rrq1Mxqcb_o9uNp0NnxW5qImrYhSZWnEfud9ZheQNV8wLU9li8eBWHzKHOSx4ByiL2LNTsHEjZs55ADt9hqyRc2ywGAB1x2s0C3ceMwn5fzppYcNgTrUZEpzKCAGfAUkXXJJFtT07R-GFs1jp7Guv8Xm1QNSVPIVWFKHs6kr2tXltymAijRZVoYo4uShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0RBT9zB90uJ7Pl86lpXmx_yMpazxPXo_6DdN0qSb-upGT7rfcYrzWunFr0U_XGwtOREmqyvgzbN0r9QKzYQ0lqyRkUxWCt6bhs0VAuAhZOasBBBI_wVEXOzodKSYWO7K7AXuEgew5aD4kh0RykOhREXaRdXlEa2oLaobvDOcDfPry5rfmapHMH56pztlRFULGYHKJveErr3ZHNYfTzpd5dnbe2tXA5F8R6yMeVf-eHpG0NGgXBZm68H5EpqqtKR5zuxP4lwqrOWyVcT3ghlTHhD6-5zjCagaoRuPzZfZ_S4rhgImoPLoz19SMsOsCtxvRBL0nkPvYzodTRdbhN84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi58F_ndYBb69Bf0qnZtKvL5A4sI8hfapOblj9gpBqy7qBlw4PGCr0TiHY_sRr_Bl8UfX8TScCZlxro_qybqn1QytxwSo-podlcZkpvLjox1rw82eVu6S-6NSfSdsljgF4GXYqElbO6pxEubyQRrrwuqdA9gfVobKbju6H_bJ6KjmQ9pzrlcAzCziJAYQ-YuO9GEAx9Dkj6nB0IdoPeAxa0RD0u78Jt2-9bTaa-ycgh8kw9OX4b0AtGCYZII0vziHtOkN3gk5h6BjZ-xLjEQ4JVBEH_qFl5R5CQmt-JMPCxTzgSN013dHp56caeiICRIAS44n810eneGkhGkYEq_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIwBZdaSvbmLhm3G4DecTR7Wdy0Uumh2xvS33XVOLn7EGdU0_kfllEqD7xKoOumqyRLpjCx9BQH_L_RdZq68fm_Tt6MOT40HcIfaA3mBbgyL23kz7dx-J2pLHLRyJex1LKgajYLDWpstq3tk5jBLS7Yj4Y5qOh1zCPbqGVIv8Qfy-iwwRJkR8l-SWMLpOHmzN8GxtaVLj6gYr7GfgsA6aNRlB1bfa7Gs4pzkYBHCXnh5O-1R5y1ad9gVO6v5u8pSRupy4RmD6XGija9qYfYE6ZZzKdwZ4kqhlOQICTIOY0fXxoj7uuZfZHN9hATIRs7LbFOZgkK8rnzjFiqodKoJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oth_HKZjWg7z2btXZ9u0FMAP4aaMRzi7yTP9_KS4GGMJPI2wRFICzP8TcFO03B9CIfSooYPdAowo73v0wSOzyw_jQ9vhn6PywKpuWSWJ6PdvoCPtO79fuD3atycLWwKxgDPCBD7SWPZPdExgRRRMCvi184r0_uPME1zCz95yqPw_NzoYvxHRU3LWPlJtB9cxOHBXEC8Pj66EwvkblQSm7ukKCvugoPhk7C4muNu-3opfWYQmtKz4paeU_jl55utzWixtz9dLKj1Acu_QvNkqtwOoGx6orY5xWIo4BGBCENs79AYlm_V9q_greCRoiXhP4dfo8jEQ0H80r4n0kqL14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlB5dstPIm1UnenHQSHhvV7ptGsZ7IcdcZh27gekuwcWCg8LBDpM8Vtm06rLb_l6Dn-u70Mm5zZE-AL758AjhX8LnCc07YM588mQE9RrtjsC0P88h1gbhCT5lAoF2EDtP-pJ5qqeem7ttTZARErLAp8INQVA5imkPTE7Pfur0L0iu_UCZd5R4ok2dmJLQ4po9JT-k-xic2_mJ-WR4nJHFRQpLRM0D7k6Tf9Yh4gzP-9QdUNcaaJ5nXVcxOSfNS-a_i3V3UzFSqztut7rlmmv746kM9idzBjI5Qg6-1-snLjYecI7crZhvhMxrkd4GYhXGeVNhOeZT0uvWE2V-_JvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItKg8qn-0qJjP3ZiWIi8jZeurcqd7mjtneiIYM65VWYnKUeFHKAKKP1H7_OADd7pBN8ySx85uWrQ4ng3Uj-JBoMWFOQYGi-fx40M4pxUcdxDkT9wHBFKrJfIU7S9jL7lhFTnvwbvgrVrlAB6jn_Ys7hvbeV-IumufNq2nH4g06p2U6hQ-1-Lgye80YfYcC2eDs8kA4aUUW980bwgKnL3T011wNEOTbaRYHJhheW9zUPjLAEi3Ge3glcc5wWmMhnl1tGgZ5rSwKbcNYmlvp1yb02WtGo2SJXwrZk1CFWSTW365WPosYT7FncDQY3_Zy4vJjRIBNBEtQ9WQ1L2zwxpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQQpRASMDik_TUM-BeyprswxcvwdAqFK3p44gKNBFMDUVg_19qlg_uZZp7wXduBF6PpFAaHgVWNAau1LU1zZ8_Vbzlc-J0DazMQ7OjZ2a8YEVZg9VAUDB-coXBourt4CdSw9tUKlXevrBvQwJ2ZLfQwqktZ7m7y6hc7xbtjDPi7uqzQMfE71y3wLmoXkYYt9VvF2yLz9tJ9bjq8X8I8MmDlotcHmKLKRMPj95oq0S_XtW3TG4xVc-gHoZGqt-muEXRDdQOGioMzD6oziY1v1E539KwnR-B255con8gcokXFvf3Ef5x_iNXIB8tf1aoYZUDcGlyxni_uN6MAXe83dsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMGYoGRRSPiDJOmex_YViuQA6K0ydoUGAcS18Gfa0RfePI02q14_HDsiY7sVokC1sgdtSj6C0lwmeM4RpjJDhcX27WEEutIQ2gEh03RavmNsUtwyOcNazdw4D7g2pn-IhDFFhKJzihnH8NmSGjSjUciFgfjavgYZQ5FZlwgBSuEyIow_jxdMmNhsvg5LQ8xcdGewfA17tF5aTJUpCi0-fxQU9gMzw3RaRAc358jld8X5rntjf5AM-xlUhBrOSOvlCfI-sm4mS2AQeG7aRDfNQCVRCv54DFQQfLVmmweQGRgkWCPmJbvUU6Mffju4aAd5auBjp9LVotEpiPzAIvYPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP2dwU0dzGX1wVZoL_z9rcuFamqXdJnQLdCVEXXwQjbMaT0TP6xdHJDnwrFLZnFH6VoS6t1zmR-7gt4GShcCalCqZi1iVOFla3A-ZmOcXYnWMKwl30o--GSWqRmm3rSRq54ft_c7lFI9zCfuqUu0M1yzxdCemt8bkfFBvhWmj7ZZvtLuEQwcO6DFx6gLDXg8gn20OmOQbl9sATsR0itOex9dWO5TX0XPsBA-qW6JUCXUiA_4LUOUv6-V701G4yubIu7nfaKWqoUoy6JcZTlitcyqwpgzfe4a3bju8Pp1jm-1J2gem9f1kYgSv6Oo4Jaw_zyQEMDu2RRJgbeRz8UH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6-HT4Pd-4VpcPGgyDnUVYiVptBEkBTGxI4gqxxSMaFAIrK_-x7GnYFtTs_srjdP8xRBykIjMzaztLz4gJMdV1qN-GlDbmpkX1a0QA-HRSlWXGaPOxq5BIavKk94NU9EFYKr0q0cbYm7Pj3gafG2M0_Vr1V-voDm6BVS4uaT48FpqlW15sJNLs2_9afm8xJv3WodZFBfZgYOLZ_J7wzxdzRtjDJM3fYgHS58WG_6DtnWtuPZSZVnwkUQmIu9BcWryp8-3guF0b96Tr3hTLLs_yllSQd4wUCL9Gm1Wt8147ON0Z-xQzOQKgp4zfNjvnXqvJxOrOpoeDA7XW-dA0MWVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTDbZV0Riu4W0M7-JZnuROb7J3D0yeG8nZghBPWwvdkRU7ifGC7Cw7lZKoB2l8kacGoO9GX0l9anRqaw-HVu4MNbZJ2XOFhW-PMOeG3HeJiqgRvNnXHY_Aa-61c76c9azEdJP1dlc4JxddpNS17iX2WO6ghmjpD4gZwcCD8jSYiYTD9FWq-YPDbBVbxtTTLQaIb3s7UAJcFVOkkvmEs2DQQe2OSVlMe6syWQP7u6YZ8McXk2SOwRYUmvUPHRb9wtYwhYFZuAF-YIF41HQDkR736c91eF3mUYxvpipq-svwBiwUvHWO2w2zGB5FqQ2ScEInSi8ugP59gXnMhozvbZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
