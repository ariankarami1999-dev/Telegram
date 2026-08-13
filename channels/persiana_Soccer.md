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
<img src="https://cdn4.telesco.pe/file/PZCHdZ7JwV1hCeruZ_KRGAZPiN9-BRZ18wsiVT-A4_X5b7aQo47VCK0OtaFF_gPiei7LhQ6TUWQ3v5xUHHwTtJLKJf_g8ZHX71zT7SSwaseoAJOKbXMmKLJ1cjSb9C8x_otTbepEBWcL5JUF-e6IEmIG9VUG48ZsWVGZH_31ize4S2VSzb6t7vszVF50nZnnuEi6VxK2dSCRX-8Zv2M50FVNodkIwTuGAkNmt0q7Lcg4L8hXwi2tfFc19hU4lHVXKHAuo7v3C3JfBgiH6ivaG6jbsdp_U_NL3x_AaoEbVNQ3bcXnKHWbEf_sQnCMys4WsMwPfDQwFkgpSxRWpTZoBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 640K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 18:58:28</div>
<hr>

<div class="tg-post" id="msg-27652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxG6dj3beASdCYE7rpXFF5ZE_ew6ZQ7FXQM9cR-Jc95zy5b_TskkBAGFH06eqYOu2Aq5a2HcPZCKuFYZ1Ub9is4FZYc0xQmSVUXV2LjEqwhtbIZfSXXuqpFqdMcNvhsPbVAnW1R7qDWVT-bd_60BSeHd-fxjMo-IrpTwYlooXlEZYS8eGhjwvoBdIuCT8D6QLGtXJnrULjysM-UbnCPehmL_twDY8DZ_2iTPVNr9fz3-JWu0BceF5GQa7PkapnWQpuvk4jTBmT4OrgBrQGBqNO0EoPgWpUfOAXd1pmSfVrWqmxVD6XenclriYml1WHnErzd95AcBHhErvjtAmHIzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سزار لوئیز مرلو:منچسترسیتی‌پیشنهادی 120 میلیون یورویی به چلسی برای جذب انزو فرناندز ارائه کرده! انزو مارسکا اصرار زیادی داره که این بازیکن رو به هر قیمتی به خدمت بگیره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/27652" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPrXwspJjOuSaBeuTA11bkU9hT6ZOJNE1qKJsZF8ke-alimKNexe7guloFERaJWwGeJFrR8QeV2wjM-FZBCktPAaq1LyOJ3AM_a5jpF5W754kbc5n2dzlZ9WkQOj1kAGKnA_XwXs3_ilYTtEU4mITv7Fu-SzXJAQ_PkA40qpElI6xfyh3i54OEpcB6SQMcILeZGUWMVKFStZ2EIWeCtXxdRq5J439I_RoUipyw5jaNqIjNiqM_7hJ0zjpGUaMaNA99r9quAhzfO7pVzg9elPZDJbbH39JHQQd2ORb5PiMtA0iVHvwTSK12EnENV0Lk7VmPmuJTQ158YvhdA4j6KKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/27651" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8DzldtRrFIa8dgYtX8iVzEV2lGvncd_PQ_ofWAmj6yDhQHNflmABW4fLFfzGcRHluhyaYAK8ZoY7v2ZaE4nVlAPa9adbiKHL5xgpG2WmQLhtFIkS2B-hmZvVDzxhJAi2hpULR8KcbuQ4zzEk3KSoAs88M402FoHDoUQ22tws0L8B5dBa4TUJdEw29OdJWhIhsD5P9pvwvaWZ9gH8eKpIGAhWTiy-swVPWMjip0w8wREbM6bDdMki3z9Yc95aoZP-K9jzlkzMDzAqa3dNBXG8JjtOpiHkO1Tqg95Axv39lfJH2anADTMNGI9IT4DTArwYkHEjA8fKNsVNYZGABjicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرکت یوسف جامه به‌عنوان اسپانسر فصل جدید باشگاه پرسپولیس انتخاب شد. طبق توافقات انجام شده قرار شده این شرکت در سه مرحله 550 میلیاردتومان‌به‌حساب باشگاه‌پرسپولیس واریز کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/27650" target="_blank">📅 17:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27649">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nci9eVcE7zX63PitpOqdPdVHrvgYSqqi4upB6npR5hFfHduQ6q1itbT9keSGukbT-T3eQAkKNqfI5YAYFaVGXHJmivCtbCJfp5d0UkJ7D5vJMnQVaKjqxMu13aFpkMYiVt6oVYzGrEEjTBr5O0ZK2oIHdMQf8STN_mms_zew0UUVm-qTB3nmn4dNl-wLQE9_oIl_E7lbW498Ti8MftJrFw_Zv3Sx6K-C6CJ0EO1kmP3Jkm-cY_Z5vqSSQ_Y_51NlYAPB6U6w8BjbCGLCEMN9d-ZOW-eF42O6Ns4G00bMoJKvwp4SnjlNsBF4G1an1yaBrWooOw9200F8D46g4yDytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
دوست دختر هکتور فورت ستاره 19 ساله  باشگاه بارسلونا در ورزشگاه سانتیاگو برنابئو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/27649" target="_blank">📅 17:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27648">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5X0WAualvu-as-1cmu6l1g3iAnv1doDHPoNFmrJSOO7vdqKHWnriyYMvITccV2VV6-rp7fYxNGeikYDQU2QWPNXuBTJyyPAlxgN3Jn1EzPoJkNvoFZseyTkkcw2UEkk12_roY-S6SlV8KrNgWkakE-ApvN6u53drFuM8CgwZFVaMuKfYeP68mzGsP1zJ4iFu7nhr1W7YyFxe6x7hgVpFXCgHAHdGgR00m1qwXLQxReJ31CgkwPgeVs8wNtsJ3fngvVredKDC_e6D3sWj4q6fsx72WPYTrN6QI_4Iu_U6OGoRIxEiyXgSEebiR3lxWs3XG1_i3LxeIS8UVgVDl3TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/27648" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27647">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOL3GAfVRFU6jofPoH3SxfOacmoeN_G_HvsjrWZA1w7WNEV1W2U6JWdtAdoEdb0HUWvVdq5tYHyWJWXJ_43SLszqQ9EevpFX9m0qBD5rFi9VqYpM-Lx9_ugQ-N-b8wFOSdvHWbC0426VWOPAbcG36qZjKtkKF7mr5cB8RcjGfJwS1n_lKL8VnyHv4tPDNPahpvf7mtIC9cExf7CVoOOIYyFi2wQX-rtozW5MOw5m3jDFCrO_LG-GugRAnRvz4zahpNepGar709Mz1VW_a9NRC5EFOpBG4aymvZsFddb9SUA75CCF05mK_Lyo1ip2LOcb-Liu_DuBylQDQneO8Pbu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/27647" target="_blank">📅 16:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItkbPw8FdaN8bJRCqe2Jc5YDNy3DlOJ2uEHWy0vZ_JRfp6eHXZzfhF8SyQlDFbT5jKj6yU-iSni9V9KsQx-6u0A0xfUyf4qAnw5-4uaLi9945wosHYGcQLFwAtaUFMT2Azxwgw-GsV4xCsKObP3NVgHvHOXJIPOm-ZXX51VjTqDJTS73WPYU49ifgxned-7guxyWtVog9mIUY9vpTKO5-KhDU6ek6OobG_Bs-L0S62zHzam_nSQrg3geuzACDdNU67jvuUriyzYNyO-z98IDO3A9qwwJvMftkfc3fBOQTbTlQRfUeQfIbcX47OXkLNj1TefGBvrmF6aoDYGra5a9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/27646" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27645">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHsOsCSLL_Nc4e7KT0YN54tRN4OoHEmnoau8GenEhVBxnUcURBdQmX-6WbDjGzaOIZQErvneqG6R6PfT-kl7PT-0ZjoaVvXHjrZE9RzoJGuaQvIWC5hxzJKRc0rD635yOIwt7pbk3Ez-OeACoiQJV6i7i6U5W734yzZfkmfr3T-PlltsZA2n0AwajYQPxgaqkRxcEfDRXusUjAcCkG2StTXQ5agdIk5xjD5_6sPfen3jiiqfl1utIFkxudN6aBnyS4JvpiiRKMPinZlGm7VOI6xW-CqnMzporPDJlvKyJgTBK9TLDpboeulccN8ny3PnpJTbdZxEuQfkI7ci9Xstig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/27645" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOIzxUaF1K5g3XAz2CqUixx8qYxFTOvx6ms3gHyMomUJ3UIL59TZvoPiw9efWpJTgixPcETsHHoUSqpKiqKwAlj_j91tTtyBVypx82pJPGSD0VOvqsHvpFM-xC9CgtygFra2N0pDBHWYwwetWsUGnSZDOWdtN2GIvevPm2mdblruB0djYpxqCXpk-z1sTxG4diAkPyj8_N695WLEVkGc_MqkSfiDAGBNR7g1fNas2CycGXUmEzLLf2OTIj19pw9TcOgbm4Lmb3EHNC7f3u_gsvhjNIo0ez3Wb-nD3P-FkoWqVCqkI1gTvtCBfKviRmUD9vOESAGmuye725neAthCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود رضا بابایی ملقب به "بچه" با لابی‌هایی که داشت نذاشت باشگاه‌های ذوب آهن، مس، پیکان و صنعت‌نفت با نکونام قرارداد ببندند اما نمیدونست که زنوزی و حجت کریمی به یه ورشون هم حسابش نمیکنند و تو جلسه یه ساعته با جواد نکونام بستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/27644" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUh9VhvlBRj6cg0yD5VuM5e1Ws8Ua4zNM7gjqWhE2IURyKsXSMiLBRkxoFvtwokBnnMNcLeqx9geMBuTjnFUEb3dxSTOmE9GQkLaPJO1d5gR_Orj_GaLUq_L872ZTD0VGsMPPxHujAZPYO65-G_fRWTKQ76gQ7ijJ7-eR_HvKIjvz8OukuYyhWHr32blU6ti5N0nMWAFksOj13u8GRSDIbw_4NQl8vZ7UPbmDP5YaQBUcQViuJeTnLY1z9ivTtrY8IoE4Y6RNTbBQkJ9AaTG2uVIcWndJDf81VRH4Rbi1zfX4wmaKeJmRn35uxtHS0en6UorqTbgCQZsF5osvJ4rZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/27643" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27642">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDPbviQXoZA9V_lcrEgjP3eAm5VbkQQ-iJFe2u2691M8-0DksQ01RRdeZWEHDB3KivW2xG2Zrx5ifCWeJ15raLut2C0iCmnoIVnPIb38KdDRLC3UWFpVGDHR3k0bpDTU3792kO-3rfI-RcLs40Xllmdau5yYC9r_iqBySY9smbJ7Cz233Dhw0nSv31G9q0LTLIj6-LmWvAuaSpCflY-yWq2qT3lttGqtvZ1MEYXGzq7HckCswIQ9VEvH-Cxsc8n0d4x0jtt0_lMA2IURnPmk8rd3U42p-ufXU3ichZGXIhNfyuWgykdq3laxzSeJLNJts06ViNBczbgvmdktD97bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
لیگ حرفه ای عربستان
🗡️
الدرعیه
🆚
الاهلی
🇸🇦
🗓
پنج ‌شنبه ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27642" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27641">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnFPPNxV8OGGfrZ1HgMALmRd_wkBDPXlyHoXhJ0a74IgaUhNH8olUH3HBkDWVV1ayztNSaM4bSrvufAEAXG3pDYWDRX6XVvuOYYsua20HjMBQnpMQzPe8ErhI2yjOQvNP3-m7lsNBM44TUmC-0do7PHHEws0ho01LfbRqhpWOvCHUdXOfMaHcdCQ4BQyxflw_nncMHQH6ccZ-RPyqngc4PCvQBO5J3z8zzjnoOKui65pvcDDY7BSbS--4eVrLUq7BLAJeCuZ8-aQTH6YoNoQvqNls1VNos0aHsIaE2aPOTvuTY0-L8MhK33SD1DcNY2JIRwNWyNq2dIuLFmUEQ-3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد وینیسیوس‌جونیور، عثمان‌دمبله، رافینیا دیاز و کواراتسخلیا در بهترین فصل فوتبالیشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/27641" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27640">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kygKyc_wjw9-uhMFLtJ9jIVJV-u2FlZ50uxDHrwMvUruZzmx3MK2gSzr7K9t7teMhs6uFy1CTFVlo5j5gGynbFJkY59UUNQX0t8DPk8_3R72gvOGExtWtOZcmpB3_BYt_j1U0s13w_69c7jMmGTARBvQwMzFJ6qOXIthakERd-QO7Rq76HZYee-J5Ll2RjLr_01rLMcNcjGChzzjtZbGNUtsBiOpFkWjEJQ7Gv_OaW80dgrHPODZuaAJi2H4f0rMG66XgDvf22C5W8AcyZwcdCJVb-lMO3JlD1P0I7i7WOvsxoOE4u6VmDHSAgKfqPrSPsvgHOKv1GVmtMMInhXbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ طبق اطلاعات به‌ دست آمده؛ باشگاه تراکتور در روزهای اخیر تلاش‌زیادی‌کرد تا محمد محبی ستاره تیم ملی ایران که بازیکن آزاد است رو به خدمت بگیره و از مدیربرنامه‌های‌او که رابطه اش با زنوزی خوب شده آفرمالی بسیار بالایی رو به او داد که…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27640" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27639">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTH2yDTSL4cx1ar_AYUl8YYdjiwJC8iKJn7Xn8YjpVEaoNmKwrYyq1bTPaXOvlFoLAknTuBKqn0pqDQ8IsqfsEplhjHwoukBCB0_rBs50NqAlKhSRuc5P8_PsktVBoI3IPK2EII8GT0lAotgGo1qI7AwmYwj7MoKuM_hkS1BKutYMy9hB6AMsaqC8x6pg4UKxwtxh7M_nHMvZJpS0k_2eANTjuTh52mEpSO5rNXli_sz0yzwobnx_5icBBNvUzO12txbmsmlb_HkTIXTT4UVi8R0e7YBqRslRPKK-Vk-QHvh8l8YglA0yd8bSMZwx-aPM5P2YDpFrM7DlFSMrCWWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/27639" target="_blank">📅 14:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27638">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxPI1amraCwr_eNKvQNzq-47I6P7Awa5xbT7V8A27xQ8ZJaDV6wDGSkxs9C225TMlLM7E_J6iY8w3xdX0DAKee9M816YoYvIMrY-igM8LZhUSdP9bdhKuC3fsnphzB4NZOIdHU2N3cONgTQ1qAcZ1ZXy81PVfBWZto3-p88pcRCt2vqgENfaeuh9PW4CSYJlwvHuUgLn9Ow8hAnpx67EYNutHUD76i8QmQB3lpdR6O7iudovLD8JRrRIMoBKudDMh_AB0lE_FnroDI6UVwyE8Z1PieTv5ua7NhSEoujTH2WSS7qPBI2QITxwKd48cfVA1AxzXXPFUQQij8aK5BGk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/27638" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27637">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmiAdwAqO1eAluUX9Flw7RuIPbPJBsvtgVS-78WxZXEX1Pva3YaxauqVzu2unLFyL8t0yeA5K5PrLVD2X3AOZYdKKpa4_pmtZL1Tso3Q9mkd5CJpfhXhTgki2UXZUPNkAYvRQvFDBvbIO0Z6zhDdSOwsUZ-O4eLt4u0bzeSpM68CUkXfTpBZ0jsgUoUuemSUG_R0Q_VOKOfbK1R-mOr2nO266Rgwg0r7QIn2rHaDsrtkoYQfYQhQCH2pqrd8icWapmoJATSHDx4i9RJV2qjHuKQDDqhiu4kyOKBLez1wGtrZ4z7G9yO2Sjr0DizritN3IvefywBTYm5hY8_m5wUc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/27637" target="_blank">📅 13:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27636">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBbynJz3Zxsr8ASW17E6iRf7bJQYTnEKuXVGGJlbRSA0_BUU5MXKVS17Q4c_a3aIzi3NZelDuzyZfzJm0l7udGg0gXzN83s3MTGGcT-mnTVwS9yTe6sF8pE_96ZbuaoqV7DI0XSZ_ODCZYE3RHm3yIGI-QZJ4tzOVmwAJBvCBoyn-aa9HArw2aWA_hpZ2TiL1LXqifGUp2TOJCvEiz7gukBLidFJOpS-fuDlGvok06R0Sd2rRORRiCNeFDJV0anGH5FgZJ7QlbRwFwn6YvdInOyGbkOpRjge64WjKqiGe0g7JluPuVzOl8-leDhI2HB_gMSefR6J1gYPKVrY3YQ-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درحالی باشگاه استقلال تمام کارهای اداری مربوط‌به‌اومدن خواکین گیل به ایران رو انجام داده بود و حتی برای ایشون بلیط تهیه کرده بود شب گذشته‌ناگهان به باشگاه پیغام میده و میگه تا زمانیکه آرامش کامل درمنطقه‌شکل‌نگیره به ایران نمیاد. بدین ترتیب حضور…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27636" target="_blank">📅 13:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428e46d461.mp4?token=rAUKMLFfNKYr9zYen2N6lFRPXg3V08gUgw-rTPrpT9HkHIPSOxCMs2RLHKtf2fYXaIpa7vJWSIkOEWIeOgFD_n8LY2iBYaEREj966XLhCkIBi3UBNdb-T98KTBigdj-yZjMj8ngv8mO1GaAZdGzPUjGfsDuS86-ESPMAjBYuLLRGBMw5QkWoRj6zitfJc_sgh-Uy_T4ls8ryDQZNVx3ZAPgpmoR8EGHVY98VjffmjQomR3LZbAfiy2qGxSqAIB9LYNM_Wnk0vbRcUS3u841NiK7k8f_DJ_KQ-LPsJiMTveaMoZ7UNMZG1R2erkV1Dq_1Q-JSeKTinUIFj4uAld6XVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428e46d461.mp4?token=rAUKMLFfNKYr9zYen2N6lFRPXg3V08gUgw-rTPrpT9HkHIPSOxCMs2RLHKtf2fYXaIpa7vJWSIkOEWIeOgFD_n8LY2iBYaEREj966XLhCkIBi3UBNdb-T98KTBigdj-yZjMj8ngv8mO1GaAZdGzPUjGfsDuS86-ESPMAjBYuLLRGBMw5QkWoRj6zitfJc_sgh-Uy_T4ls8ryDQZNVx3ZAPgpmoR8EGHVY98VjffmjQomR3LZbAfiy2qGxSqAIB9LYNM_Wnk0vbRcUS3u841NiK7k8f_DJ_KQ-LPsJiMTveaMoZ7UNMZG1R2erkV1Dq_1Q-JSeKTinUIFj4uAld6XVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27634" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9rSX26HxQZBkOTzWEjHk-SsgivZoTOCVw07ObpZrYoivwFFTpFh69WcYppMP3DTkMDQlEY8gieOmmNm4hMdCiZdGhDY30kz0UsEYuI2aStqFy7GgQ1Ad_EN5w73P-F5oXhkc3YilU6Dd2yXIuZBfBJS_fMlQJJmLjc1zVI-sdm6OTA0e_JyoSRVe1JY0sLf8ejaS5dDJPxmC3k4ExUl1rZwXD8RAZWhKtiDdvyTR2ktViteG9wnnrvR3BEQwVlzQOYdF7_IWlnhFVw8HS_GeDI4iH2Q-0qrhiAH8V1_G9dC6TPIwxnNAWtmIww5Xx5BSA4FCYk1lWEI9zxGnkR_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی‌از کیت‌اول تراکتور در فصل جدید رقابت های لیگ برتر ایران به سبک باشگاه‌های اروپایی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27633" target="_blank">📅 12:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2kmlNc0h1WAqhsyP7M7tsdvN2kj91mFhh4rcLCzlfWlstvsesdwIB8RYuuR4jgkOgldhqXrXQ0qnmiRUv1pPdNU4ymfFudA4PnrtFxODaahXytoq6Zz_yq2JhbtZEaHE7VvYBC_elTPhi6Xmu_D2G7JuFOS8uxjI7IoknYj9kdJfmbkhsFBxhDLjkDtmcblxtk9_pltqsjbHBLthSltGNSzx5Ywe92LK9Ml4eBtMgf7XUoMsxpdZFM766mizry0HbuPCfT39GILGiAP5pnq0TTwPIzbTMQZnAp7r9yKY3SXHMh3B41sLs2D0gi3PgbGJwXL7rxk7MocSAYFLd89zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27632" target="_blank">📅 12:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdD17D9s8aUjIp7SI0yZBn3-pL1-NFXkNuOJZ8lordBUsLJcxMw8sR97DP-qIwuxkjqLswXnV6A2NnTMvffmjz2fru4UvThrN0QozMq3hQM7JW1IR_Zkm-PJ-KUdpHQoLcnbPEkCtUm8yjmuRcwDzMbzttaIxJ2H9K9Isq1fxF9K6fcUVggflK8ikRtbKlyX77MwpYJtNZdVG35lB2BwtgicJbQWbYKTkNH1QBCX49f4kj7y0FNguM_4htnk5t-H3a9Tldu9O8_8cfERMZrfyO2bxCJUZYlbNmPQlIh40pScLLyuQ1GT2ZGnk_tn2QKbcEhjo-_DBO3-ElgeykuWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27631" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNoxsJmN7bquMm9FVVtWSo6F0-dYB6wJD2cMrHT3QWSwR7_6obNJZ54IGo4yMAbSES3MVxU1GhQ8SwVifphG_-BHkl6M42ubm_W_-wmw5gB6U7ZI-GYMMSwwV2AmAKBXTphaQ2Evf7cg_Vm7z620vDAY1nx9mL3kX1UOgARnueZm8GwY3Q1OrBnM_EPE0WJlHfiTnFKzmslBp6qNDBN6dbTTWG2fC3Q7XA0B3kWpnr7vHQOhSwBjyMPYHbrBa_YJaeIKw8I-M7KakY1BEN-PQY6vrdmfOkI5C4NZ4dRqxpoPXY6WEGSEwqG47rjz2ofZD6V1ASlwUZjc2Q8ZgaRi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27630" target="_blank">📅 11:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgEpbJuqvD7e-flQVOOchSkM9l-iIZpTnbOQlXuVZi7xLe6PjwOxbO2YcBPLVBMqIIzv3wqVhCHmwvrwFNO_y0bz8DMrkXDdnGkZeve-_Jt9G7AtXeLHHkPgTW4FCeVOXtrl7zsWXFLdP6LQuyRpUiO6mutHlWNbWw8gLbdx6IXdJ3-x5a1-ShgmfsNJhtviCwlKNmm2dTiffZLXHIvJokr-kQYqBFZ7Ahinc-g24RJVaRwvuvvzird9f4whiNt6Ke5Q9w_t7HNV4AxOqLP5D7zK4yYv0sfgWU4cJQDliaJ_UQYaJNrLLq6pyVquG_8ft9O1hayxwZlrIflKgwAAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27629" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd2-5N-_zUInyPdiVzqXVfzoK6EaYVFaqEcIhvNFCfaMW-2_pxy-eiCBMnOaiBsFVpNpjxlKCpGEO8y8Kw_q9jBuDvFwFpQLpLspzimr1S8jQjijuEoslHWknN5jnn2rxqBXNCWUfpEobOQlgJsrzYnhsmV0no32SMBU43bt3O6sK7wpCQgdBEBqF4Z996aBiouWWNzU5ryHkLUf9jJtR_W2Xdnd2hnMatDtEax5y1m_kTwsGJmR524OwCzZq6Gji_5sAmpLo9UqeHp1M8X5e8NjplDNdX53WxPXD27kfPADh3o8iCf_GwSfFWlbBsoifYmCpBo57_0eyyAxJWaBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوپا آمریکا هر چهار سال یکبار
شد
؛ با اعلام کونمبول، جام ملتهای آمریکای جنوبی به روال قبلی خود بازگشته و به جای هر 2 سال، هر 4 سال یکبار برگزار خواهد شد؛ دوره بعدی سال 2028
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27628" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxx7hVZwMLFGJSnNcbKVhZiNZc7_5dlxW3pjIXJcxXD9XBuaPrylJh9Ma37DQxQ8g8o4_65InDdDzNhfkWP5WMww9dzbKOnhm8xQYOXjRaWd3N57-O2HB1Htp5vsyux-2YGGAGvV8picXz1BJmbfBWzFqx1ogL15_HisESlQvN8SR--A5JEVLBkVnCOwlGkyTS7XJ0JiZFARi1TsqVKWkBu6SACn6kHqSvAXG43NqFGfk_owxjLZmDq5Z0XoeLkRLJ2krFYq-wTYfYzINdFFVF2_BcpR046QlIaHPZfgwYp8QSjPi0NKC5ty5mWt8__GOnWKLBgDSzqHMyd3EDoorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر دروینرو شارژشو
🎁
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن وینرو
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr22
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27627" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE2ekcm6VsTFzuKA1zoq2za2dFZKRmxTrw4anjyUmbcdxKDOfeAVBSJpbhf1lqOCZCfliTZWOhRTQxWDpol6dkqii6mAshVYgAORLVZV7R7IIqOh17q-6KnRjbudeuK2RdrVoNXNZ9DY9DleEWUnckb1RVrfY_lvMs2P78qoxOWIwk2viz7PPdzaoIwTVmsh92kiWanuMZbS6nb37VMMZVwPmtDGxUj8MNA-nXD_eT3lvxgfxOC4k7DFVRWVnE1Qf85KHHinnDUTMRwt7sGeXALP57XwBd2YDMgOlgjoZMPwuxRLKAMaSxxqSj9AsocSswbKkBrmRgS3RA9iUyd4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای‌اخیر گفتیم؛ دنیل گرا در لیست مازاد مهدی تارتار قرار گرفته و مدیریت باشگاه پرسپولیس در تلاشه ظرف 48 ساعت آینده توافقی با پرداخت مبلغی با این بازیکن فسخ کنه. توجه داشته باشید اگه رضاییان تا قبل از فسخ گرا با تیمی نبندد احتمال بازگشت او به…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27626" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIXuLuWc0IzOSIJVPRAFMT67QjqjIF-f5WcaJXu99HQudZnEb3o6MvmTrxsRqi4WZHNbt6ViCLg6tkSDdVWLowWr9TJsTH3Gtc-v2v2cnMUxmKKUn3Y2--vSbeuOTO22kmLjPepK9rSDBpdXRKSjpx1ilr2ebBSJfCGpjQmeLgpx8QA1yRM5skARHj-WDmQ3wX7ApYT9hu8xQR_bjPn_ykbG_tPsa9Ina_7oOmvC2fJYtQiVOujUHdXR4IIAjRl9FOSmztIHyp1i12DIeBIrsJJ12K_bfaYp8kCjvS7aZJ7wa1WXcNOaErYm7thYmTi6vX9W4NjRDaLzDD1z108B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27625" target="_blank">📅 10:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27624" target="_blank">📅 10:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=M8NNDm2y69RdHipBwqMupMdDh-FO2TjFueQyxAnn4luJE5_am9e8suSGF0JfUxdDkwNCPCDww4PsnW9aGbkkUYIGgYb6zIgRjaIxbq-hHAUzDrs-dZBOOIe_HRXdzVNUbVmlcKcMAm4ouZhzVns54s_iRVrqDVYO3D4HLTFzp0_Abs4QrohlgIl780465LUCrj-Nspvbj7vjvhvGq0pxEblWWsKRdzunvOVQ1qicupVvPtqxF4j7Rs5kXFv02jGbg5xej8SuE4wTCRqq1fTi2HdB7xrP8LPFjNsTQbdt__2piTwl4NucrjzlMFY-duMR6GRq-AKgJfda1FC7_3f7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=M8NNDm2y69RdHipBwqMupMdDh-FO2TjFueQyxAnn4luJE5_am9e8suSGF0JfUxdDkwNCPCDww4PsnW9aGbkkUYIGgYb6zIgRjaIxbq-hHAUzDrs-dZBOOIe_HRXdzVNUbVmlcKcMAm4ouZhzVns54s_iRVrqDVYO3D4HLTFzp0_Abs4QrohlgIl780465LUCrj-Nspvbj7vjvhvGq0pxEblWWsKRdzunvOVQ1qicupVvPtqxF4j7Rs5kXFv02jGbg5xej8SuE4wTCRqq1fTi2HdB7xrP8LPFjNsTQbdt__2piTwl4NucrjzlMFY-duMR6GRq-AKgJfda1FC7_3f7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پیام لیونل مسی به مناسبت درگذشت پدرش: بابای عزیزم راستش باورم‌ نمیشه که دیگه پیشمون نیستی. درواقع من‌نمیخوام باور کنم که تو رو دیگه ندارم. لطفا از اون بالاها مراقب خودم و خانواده‌ام باش. مراقب نوه‌هات باش که راه پدرشون رو برند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27623" target="_blank">📅 10:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=RtjldEr-vGRx5YCZTcmaiQJ1LxE-hBGz2RJatpbmy4OOuE3hQcecAfpPdR61vnZdL9H7GKJcy5TePJK_K7wIfUx64-9Wqk9JsoS-mFc0-SnI8-qPWxESsDThvVaxDU2gS4d3cl4FQCbmLDFP-OBDhcgVxLqYvpMJgmJDy4AJgV4Ca0pivITRojZkKSvC5J7k46tmw25g9V5e25lime6aMWuoecYDKww4-63y63yPAsSIJdj4TCV6ISNIAYozzuQn_huLBR6MuBvtd38vH7CHoer6nHR09hM3S5bVuWZCLK_a_O5iW7fkrCv9YdCia784TyTss4t_JKusIo_yxga50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=RtjldEr-vGRx5YCZTcmaiQJ1LxE-hBGz2RJatpbmy4OOuE3hQcecAfpPdR61vnZdL9H7GKJcy5TePJK_K7wIfUx64-9Wqk9JsoS-mFc0-SnI8-qPWxESsDThvVaxDU2gS4d3cl4FQCbmLDFP-OBDhcgVxLqYvpMJgmJDy4AJgV4Ca0pivITRojZkKSvC5J7k46tmw25g9V5e25lime6aMWuoecYDKww4-63y63yPAsSIJdj4TCV6ISNIAYozzuQn_huLBR6MuBvtd38vH7CHoer6nHR09hM3S5bVuWZCLK_a_O5iW7fkrCv9YdCia784TyTss4t_JKusIo_yxga50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
#تقویم
؛ 9 سال پیش در چنین روزی؛
در سوپرجام‌اسپانیا، کریس رونالدو بعنوان یار تعویضی برای رئال‌مادرید به‌زمین اومد و این کل استثنایی رو به بارسا زد و زمینه ساز قهرمانی کهگشانی‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27622" target="_blank">📅 09:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA89Z4HRk6e-pyNiRXHk3M0s3_vwLSv8NoRnqWmfhzvLgurmuqJ1IY3pfL4EiBssywduys_uEGUKCQ13uxt9fXMeGSbJp4RKdy3f5cH2xN9YRP6mqFzMbuSNFvpfNneHOmPsgx9xvFV6KQKGXBQOC1H28xCqCpWoHQvOdLLckfZ47Wvzui6ro_eFHFbFtf7mrQyKCECViiBmqGAOz89hUHO4fd4n-nEysTsJSxuZFJmULi2P16ucyTPgqzMCVT27oAUuzXuhJLwx9DXb5uboLfKuZkKL-NNHhT2GaCeL_vsr_5DnbC3rUIkBq-EtvWJlVC6OMeZUyaL-9zhOPgNp_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیرو خبر شب گذشته پرشیانا؛ امروز صبح مدیریت‌ باشگاه‌استقلال 50 هزار دلار به آلمدین زیلیکیچ بوسنیایی روپرداخت کرد و پرونده‌او قبل از شکایت در فیفا بسته شد. مورد بعدیم طلب 25 هزار دلاری جوئل کوجو هست که‌طبق‌گفته مدیریت آبی‌ها فردا پرداخت‌میشه. باساپینتو،…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27621" target="_blank">📅 02:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzleGhx9O9uwhXBkplRms71HwDJkm-YNqA5gtxchVn74bda6Z_twXXVngF0iF2YKYnlaYGe38QXir0TBsPpksKkXt3y3xQmpmqPaFlcTWJTJzz6WSxy1MKGoBHShlre6pWlgfSVoVVM_8jX900TvYOWk-GCyZO3ruRB4XvPGbQb8um-9IzKPLCNPpObgv911KWiecm5B4uhRNMqqwal1P3PQoeM0utsYqwpSPasErqYR2AQz46cDzPDpiclwaasj9ILZ5Dz-q_taTfkrQPyukIyMdc0geGhGMvqoIy_f85ORp3qlENPWIuqIkQNeLL4_cFe2_tSs7EG9zxeqSuziOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27619" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27618">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnfs_zruQ5-zW2oi6Wq-qFdOFCC18cDNchDAxfXj27-4LwxrjUhOvWG8hgGk4HLOIcznjAJHlymqN57kWSitBiMVr8vAW0ikTvJPC-5Nme3bwrsX7HBdfInhuHmNDc4_35YX1uO3H5W_JwINRDNGOhnzYMhf9nkNN_qQXgx7r9SC4rl80HpY3lz2AEpTtuV9bHLJ7bgtmuh9i6M_hiMgJqdlp7TcQthskb4wwhjLeN-ra8Scb8QjqRQ3YmqDc_-RrEWdkVsT7t_GvH6pzstkxGfzuFv7JvQ6x8dte0qqujXAxFTiiSAg9VRTtD4Govcagm8zbDPK6wR3rNEEPV271w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
هواداران‌پرسپولیس‌وتراکتور در زیر پست‌های این دو باشگاه اینستاگرام بشدت فشار اورده‌اند که محمد قربانی فوق ستاره 25 ساله الوحده رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27618" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTYO4bUheuBGAJZk0sLcEX9hur1V3psVx5z_-psK6JAQEQzK36E6ZToHRv2XJcAbw243bMWoEmB28TIQ5Ufs7Ev_5675WKhHQ0c9EC_Q_LC1QXp93Om_7mV-Lcwbp-Y5gplQs2B_sIRn_FQlTqzh58GIF7Mlpm1947rutsEYTJkk4xYStFlh2DXcQhfnDW4gp0FE_nBw6hd65A4TEzvd3KOmFehHvnwm744-8HR1OzdCz6IQ8q2ajJseAwHsK-nx9Dl93EbvY_HIb8Fx5xl9Mf0Ack1a2UkeZ6fyjLQD729umM_1h1nkd6XxeOlkM6vX5ZqFTtePURghd4dpjnOlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌بازی‌های‌امروز؛
ازبازی‌اینترمیامی در غیاب مسی تا بازی برگشت پلی‌اف لیگ اروپا برای اللهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27617" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FwdaDFakyEg6DX2lI_GivHifSMiAG4lidfNniDRKW5I1vnbGzmZNPFiJFe-8Tc7c026YuIbQ-HyhNOy6YnsmoOz3xUQrroPy6hJHarcIW_mPkPkHTPigVZhRAunV2x2pviwz_0pcpo4xjZhYAsJcbXUMlb_q2usw4p0lsxadu7JdmYwo874pSrEDJLOZru3wcJ6Gs-0pRq8HzzsfOeurddgPuJhXuvJJsBBF_syq1KO7ALPbI8CeICzKIhRB7COYaqUAFTY2fUC5zMs9nUvxCVSQd7ltcB1wqozXprFSaR6bTw50Dl1ByjKMsBz617HM7Q2KGtC7LO6U52fjV7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
‌دومین‌قهرمانی پیاپی یاران انریکه در سوپرکاپ اروپا و برد رئال با پاس‌گل لونین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27616" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFsf-hT0zTz1BKKst0jYIUZ5nTOW-ZOrTrzSeQJmTt2coVuJg7NlvQVF3WaPykqdcXL9B64l23FJh8zymmHW1-gLGg6U_1lJnefnSJg1k9grW2bgdUhDwAz_1FusyQGcJnipKExY4Px6p38OEP_2fSB0joQ2oWY7zA0zeoyQjyJBwKpx2gyBwMoLNvoWh8upZeV79KtpfKqVxWHvSl4Kos72pXj-0qoXEX6sKQh-DmZUCWo3rfdJFmXvhgLowXvsea09zs6oNIgZePEOTJlSsTjPaUO2pV7ZoPBnsPyWT_nC65GVXER3cJudpQDiQCNTbO1wZVB8kDyN9h1kxQ8hLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27614" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc0eflkawxTxqaJgd8fdxgmxIfxtXuJP8Ss-aZVGUqtQHUKRB3TBASzE8OaGVBBzGh-y3sSY3V4q81vWKI1ybslobooi0SSxpvR9pWy0THrKCA_4pkVC2HfQMDRp1MjogjMf8C8KOF_fg39em6okmKE18irCfx3cPpwHjJLxQFYxVSAuKqYOF9Bh_8pSVap1m_YESIjnn7HyuSxlZUfh8Yzv5qMeHPkFPGQY1DZQsxkh9yQPiq6n2KCnXeLVq3zBemKKR8qsFBdRPdog8tAoyqwqA0r-d14RSti8XmIeOWHRw5vPlae8X5NtpIoTZ1aPzRCVNcmaDe9ABv1HRvraBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان لوئیز انریکه امشب با برتری دو بر یک مقابل آستون ویلا قهرمان سوپرکاپ اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27613" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaOk1Q-pq3B2KW5jTFMJu2pth7OhiV06xW3AkaZanIYFs60uE4e1I6hJuIZYSCZI8ZFa_GeC2_Qv2mHlpz3FVwEV930fNBPus39oR9JmGepkCMv9YWNHnwOuftuRkO8qhUb7LbHqpdnu6OAqnzl-HJ2F6Mv950Jjlu9UQ40XoTdPbUVqbqfkAZD-4gt344jLAibbQmByFEGfbmQSR9FEQd9A1p0OOQ_iU9E8UemUvMoLvNCmz7NmKPlnWH1VW2wqf8WjYvu8bNcs1QaCoTIFvd1esxfmJ5MlBLjFr9uQ5KrS-z0qNShfYYUTyySCbDfsV4Z7jFoFLGDbzubaE43ONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27612" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml28weRl7_ERhwxhDj6mBW6-Co-wQf28q6nenOiumQ6E3htMvlzRZ0vVMlxEj67Q6MtNEfrpaT2QbP8ngAZYDDo6m4SsD78b6-L4fSYq8l-Ok32lJpPR9_Me2n0gEUqHdGLZU9auEFewYcf9nGTklfHGGTSfOQXrn9B7Ygenylw75rUQ_NMfa1rSEd4w1qfFt8m8OEU-U1_I8fhfoPA2VjsMT7v6FV4qtja4cAa_-n7BIk7kBpsajpFLcCgwHdSC0Auz2QKA6PZVgfQsU0bhJ3-ni1Z8vt4ZN-YGrHnksb83253bdFMzKhpVq3-78T2GRfxPAj9ihN-Pn3bImyMosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27611" target="_blank">📅 00:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbGlvt7895fE74nVLsM9XOufEVQYOZK8lu0r8sPQ0oiErQsZSzQQF1wUcFyMSTC5NkttVJwsqsbEBSInUnOM9kCMyRb45B2HVMEAquFlxciYOvBGGSkNEeZIc3EO3z2ahzMxNN43ipTDQgQ5DA-dz6S0mgvXTJT9apPfS3b7qDbBpvGmxL4HqzHMqGEZIK-9GLc6tHLH--IacTIC1FWRm4wJvYTbULEMmBqpV4NzO5I63awLuNJwiL6Gdf2PvsBC60xwDGENvbipQOV5qCTCz_gegn4aXBcEUX5avPRPTIM24yN337j67hyYwvPrgQ3uTu00-j6oT_BCk2GCFLUmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با اعلام باشگاه پرسپولیس؛ کارت بازی تموم بازیکنان این تیم از سوی سازمان لیگ صادر شدند و سرخ‌ها با تموم نفرات به مصاف شمس آذر میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27610" target="_blank">📅 00:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEnYb2L0QF8Y8fJ3sk0ZRVi8VW6Za73HksDb-JLFAXc1ShEQtFJn5EAxWED6zbqgk0nz58kTv7rnz4wTelEOR-xsmE5JfXYcWtKHEgeFXYzeSH8lJF7_ty2_bKIWulkhG6M8oRcsadBD_tXtHd9GG9AX7p0S73YQZkBh-suYgkbO5CuBWYGMH6SKdNJcqhAqAXalx9g4--L8yYPyOkA8b_sTUPcaDexVTa2n7dYwwQcVEqXoEak2ZUlivSO8Oc1tc2gZyK9PTCFC5eP2iawQzOsKJFT_J60S57O47wjIf331Sr64V7Tn73BmaDvK4MI30_xAHYmyV39dTh7RZkcKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو اسطوره پرتغالی تاریخ:
🔴
اگه من جای امباپه بودم، می‌ رفتم و ویدئو های کریستیانو رونالدویِ مهاجم رو نگاه میکردم، میدیدم چیکارمیکنه و همون‌کارهارو انجام میدادم، کریس رو الگو قرارمیدادم و سعی میکردم چیزی مشابه به اون در پست مهاجم نوک ارائه بدم تا بی نقص باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27609" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcE0VuB1aLHufP7DLq393l7n4-PuPCjUiw_jglVnLOH2Pby1RSe15kmliQlrQD0hf5X38BYr8BrIWUmSiSj4X2Pccl_q-ys5vyWomU2NJZbtHyE-3uFwcRX2-UHYsHeLeIkqdeECF4olHTu9xGnOiKtApbUerM2YenFpNHYK2XNnmrys9Ka1RLtSOgRRjCeAO6e5MRxF4nEyq6Wx1lMYy_fq4dZ-4GD36r62JdSmTrrjTyDRIZPy5U1EuwNjXY3uzL6LjdzA1ETeHYva3wRQSjc_pgj-9stdt952YnAoWVaFgScwgtBXYcot99Qj5LOOEY0LRSHOjwfmQ50XizateA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه شروع فصل جدید؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27608" target="_blank">📅 23:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27606">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEI1eXeFSgDiNmGg5M-sJwOniUunbfn2LPjC4HO6Dcy2vbTS0SLmFa02ELSQFRjhb9vLqNTJd-J1I5GX8DgS7LXRpmffMR1ExJD2srWOBIaSHBU-F-IUJ-ytEsxL2fXpitGV63SWkWZKe8ur-dEybuHiH4YQII9A74LtGIF7rOKjd96FcsPJl_C-Cfc1dRaLndf0nZENel6aDE17LGWSQ-uTrXaG53bATSGAvlKzrM6hvZwGKgznjW81yiQuU5HPUONEa06SbI8Pyro_TrhF8iAGd0VbCdU0wUMp8kvvmNwEu-ow5HPKKh9QTJOAOT0caOY8YmMdNcODqfZr50nV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyXQ9mC89b3ItdDa_f0mXNfXGN7xQpLPS20qYHxVuHEls42tXgPBruVvKS_x77bRXNG82oSYxkhYmB24WHz9mVuljOOLAzX438oq9uArA9BjwvlVzVpZ8suA4hsYstl-fQcdz3m8OWRU4tb0vUz-UdwPijDNi44xHsNTsSohWebyoUCkLGmB5QzZDx-ERlEMnJuCpyFIRuFgr6QnhItrXGgRIYrCKBHl3m7Yz8V7TyDRNvAT109G0JG-vTGAEe5-e77rvAqpr6he06vgoHYtjRrlqBxcY7lrbPojRA1E6dFwXXAriO_WOl9jKdUnm_MUUkiIjQj5ayvzDYFsq7M3XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به بهانه شروع فصل جدید
؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27606" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27605">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQVtCRKi2YJlglJknbvvlqehkiDamp6wXx-5K3LrFOcgAfhTwMWfCQdyF2Mwj9u6gLTGSO3ZK-B0MMuoCheWpqc8OAbJuZB8VXu_ESNBJ_suUzGP_E_0OSTkxXUhLY3RzXF1cuzPmX8Zh7_7HoEVJLyR7rh18ZjG5xkD4eoMhSvsjcOM21608kfc2UIqRGC85yDaNe-GvZZrSelBEVr25s4dvJx1p_0uJITl7vD15twVZ-CSc9AqeVIVuu3JuoBlUHZCSlJCN1G9OWC4ztQyw4_JTte3P_c4rHOXHVw63QkLku_Wk6oshSDZlAsH5tTH6YCiqcBY5-pfTbjH5OKq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛ برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27605" target="_blank">📅 23:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27604">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=pnEfC7tz-WwB6GPwLURPnjuKn8C5qdIpznsha_IpTqxgYvXbivUVUMVKIouBbPiBBjwj2QXOhe6Q-h4y7YtetPpXzXqCnD9u9tmQQCTyIWJAl36u5bspURZaUaxlpgtMyHEUzsOl8MCgrofq4lW8-llnDU3bRtEDFERWFMSOQpPlltCVlCEKhC_NHDdBV0WhmjUb-X2OEQSGP1W5kkWl3frvrO5l2rBTl1r5fFdgPa2eyB5XU_QgxdMrqp3wztYFFVeJhGg0uhrouOd6na42cWXusLDoW2FdNc9VgZeE6DEwPrF367JKaOSoA_PiDpMCPf_JPQT3HiS-PzN8Vo02Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=pnEfC7tz-WwB6GPwLURPnjuKn8C5qdIpznsha_IpTqxgYvXbivUVUMVKIouBbPiBBjwj2QXOhe6Q-h4y7YtetPpXzXqCnD9u9tmQQCTyIWJAl36u5bspURZaUaxlpgtMyHEUzsOl8MCgrofq4lW8-llnDU3bRtEDFERWFMSOQpPlltCVlCEKhC_NHDdBV0WhmjUb-X2OEQSGP1W5kkWl3frvrO5l2rBTl1r5fFdgPa2eyB5XU_QgxdMrqp3wztYFFVeJhGg0uhrouOd6na42cWXusLDoW2FdNc9VgZeE6DEwPrF367JKaOSoA_PiDpMCPf_JPQT3HiS-PzN8Vo02Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27604" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27603">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVTAr4YH0Ba0h8JUq6AUleT9CbPu9mTO5Gl34mr_TavncVGPdn32s1ty3fs2OefehFvO21qyTDJur-TeIZbqPPEiBlklIymv27i_Znj08rUNedihjqUtknm4lKcL7D1Ql0729iYkppmuKjDcQi-f7vCZsFvtk7BKBCAJuYUYdIGJH9fyiixxJ4kGmBszw-ya9SvE8NDa6vpd24N3eWLgdAwyCbKWXlac6tHT2vWmAAA8KAMAQ-EAVR7lQTtZl5DvNGbPQlTESrA850QRWN8OGzPxcIdLulZfXO-yLSLKDWr4H_jg3q8WrPKapaJM1vAhz52IBfbW0oA6LevUb2Ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27603" target="_blank">📅 22:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27602">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=dtnVMlZTaJwgpehK1BGJIFKM7xHtnwHWpM37gSKtqInQu76zk7Nik0x29mfARGfKpSZQm81RIMhFcF7qzfFC-wGvjXZGqTWzgL-ipEhQF2-7FeyMRiDorG75c639Js298czMr6jtg1LsTKwCOAuqTAOXMi3ZaIZvKL2gTYCHpbbrCVHSuSPHzbirc90HXL4jvdhjSKCzNQez1s-vZ6Ijocc_qe2KfHJYMjezfHTYN2MctW3q6yMcaM1h8wnCSdN2CIkqrH5sp1b80rNZRDidAZvDUv5KMzSsxsBwqvskFjAn32hhyTiN9ncVN1M3BeruqQuNmHcgEaXLvtJLXiIUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=dtnVMlZTaJwgpehK1BGJIFKM7xHtnwHWpM37gSKtqInQu76zk7Nik0x29mfARGfKpSZQm81RIMhFcF7qzfFC-wGvjXZGqTWzgL-ipEhQF2-7FeyMRiDorG75c639Js298czMr6jtg1LsTKwCOAuqTAOXMi3ZaIZvKL2gTYCHpbbrCVHSuSPHzbirc90HXL4jvdhjSKCzNQez1s-vZ6Ijocc_qe2KfHJYMjezfHTYN2MctW3q6yMcaM1h8wnCSdN2CIkqrH5sp1b80rNZRDidAZvDUv5KMzSsxsBwqvskFjAn32hhyTiN9ncVN1M3BeruqQuNmHcgEaXLvtJLXiIUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27602" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvJNVmLU1mdD_N1-twwjblZIRzFrYf9aRmYdVMx6pOfNwHzM7389pgDQ1snPMYn3XgGQWbNa1BFnj5CxjpI9XyA8tWSqrkaB0MYKDy5INVejOSNkQcK_exWO8BAFXKeDeph_7wEB2xCC7URU3mVeIKz6DxqEEbQ8Uh8yHRTMYVDMzYo0n1E-JAAJbewvtpWrAeDLxFZm8yfPjnN2nqJHb562XjkHs_9YnM51YQa20UAMBF0zpuOEGfbdORuwAozzUBPRCc8XcX6HpRJ1vQzGdx5q_H-liAPCrILujCifZ5B-E49fnVD0AyASUJGyvLNkX46gcVGvBySH4y8wvxQ0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
باشگاه‌الوحده‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27601" target="_blank">📅 21:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip1hYLJCDnRvoIjTkQz54OfW1St9N8U_JCraFyJc9jgZP9L7WETjscmqKyrOspVV606IywM7zzmifxWjg26Xhr79dsavOmmXnL5mQObqlproZu6Z4QRb5XYwUuPxDafn5HxqI-xRpVXuShWj2tH9dPEsYrlc2FpG3_t2ucFmDKVKTplssDdX6iBZlSIJVRj5gYYeXojroQMvqLrOgpcKizrWpd7mgxok5J3TS1r2HmnXqA6uFF1S7QXooH7Y_qUlJaQn1EDQAvu1taGSN_vu8yR9V2kMCTNHEp-V6P4SGMlEudPvojGiTyJBKAFg9xBvCPAmjrVUbAHSYHiN5n5Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا
؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27600" target="_blank">📅 21:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzUGofjCFMbmvcPIWTPfAMdFbntX6XXYpAEKgLxBdefQkE8q_bXPjbWhu-h70qbZIwgr_Rk6I_-v17PxIxqBfpyw6sdEz7pF5y1Jc0NbntYPQFplEo2sFfS2xVXVeHaWp9Qr5_4eUhfwgJJTZCjpbvqvwRCX2fl3-2QCHnV2Wkxp3gUDbnG9mUB5iO9FoVeHbMN8BaxH8eiCgkm6IlTvWmFgiapuD1NwccVYLGLVowEwPbbmC0KikcaVfIbEgE-BZnLlhi4ut2vetDOc1RVdfJGxUdMKyFYtuX0rfy77Ow4CUl573MFAOi2HR3cJ6mZ45r9DNMIgc6riUUMhPw5new.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
حمایت‌قاطعانه‌عادل‌فردوسی‌پور از سعید کریمی کاپیتان ملوان درباره‌اتفاقات اخیر مراسم ازدواجش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27599" target="_blank">📅 21:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeX19VRkLMbCNv1jBG6cMMss54wzfyYwDXJR0s0IUSsw0QF4XkRCf3FX0dFxTeGLhZdXjb6_HkpK31p9yoK8bIDd3Afn_rj91fpq20rcLYVJQbwyxpZv1vKFLUuOWVx7Q8eL9-nlJV_aiSi-SdNkI561U6jTJYhSvFN87nCOXbZ0mgclHr4gYAZD9Eba7KCZgMA6H3Fb0ZkhdmdtpNv2--Q8l0m8TSvfkoEjdDRt-faB83mbVoFWByXgtkSa4arg6sqMDqPK2S9K52Qdxh82Brey-bjg5RzzVPEs3FFuk1ARKO3aPoX8SC0_R82ZKt8KtpgrOeBximypbLNXWhZb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ طبق‌پیگیری‌ها؛ تا روز یکشنبه هفته آینده تکلیف‌نهایی‌باشگاه‌ جدید محمد قربانی مشخص میشود. قربانی بار ها اعلام کرده میخواد جایی باشه که‌فیکس بازی کنه. هرکدوم‌از دوتیم رضایت نامه‌اش رو پرداخت کنند میتونند با قربانی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27598" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaZ_ly8MBRZMChzK72ILR1C7uRRiPcVxmP0geav6D-CiJMeVnK-d1BLH61TQI2kRnfWFQPF-Yh010PAZtlA5Hslf5LvQyuXdETSACUyLd9_tsiDYuvfUl2ujZmdrMJLMISHySmWrjJOHA9APsm-MHMpS6f3A2ItNG6ClLERJSWpV5K1BpiqYMRXEGoY7LV5xUodh2klQdwzGtJVo_Oo0iwCsFVaCgaOgl6-R-RMnlfpO0BBRtrW0uYyIHmiK378V4c69rCa7KJkCh92ol30-fTo-ENkqbYMxIkdP0_wq0cMGyf3GJZrL4UPTXRqu81e5ClMip_d4RM4deWqYxT352Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ تکلیف محمد جواد حسین نژاد و باشگاه‌جدیدش تا پایان این هفته مشخص میشود. طبق‌گفته ایجنت این بازیکن حسین نژاد حداقل تا پایان نیم فصل به ایران نخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27597" target="_blank">📅 20:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDdce4CiOKGY6GayEiVSduhiPYlDW7Xdk20GYHjQkNKf3iUxuN64CVz2RxJJo0Zrgt8dc5zlsjnBYqzoQfN8Oli7Jzp7S4WuhsJnWThoQeneNi5XbKGJS9c6EZsuKt4smUPQBBxTYPxk1sET310cK8Y78CGt-5oE6FcradTogtKkUy10HITwE6XFvoZVmkcbsb_QEU4EfqSDdsyDAB8n4l4kU89ssLFazPcIQLuoBOYEKuNPMiBvrFxXzKfNbHaZJFus66NhWxf8AjV4BMFD59DrjzaIz0wmX82pZM04NZS9mGKsPg7zP1jRA5eADkk-_nkSuSj5DueQdGhTnsaa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27596" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27595" target="_blank">📅 19:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9yYhomOai1RFJ1EuxTonIuGCIvAKO0EW1h7Jia43r1-cJ7RP4yjpqpX7SDGHdfon7EQQsKyrxpnJiaxCsnkLAhZOWrpKIQ3zTH6tf7jZOg51XCjZvEXRb_1IveE24oRQVX-z_-htiE58x7N1ARK0IBTV_TO-HRF8lsJ9xy85x_p4k2BSzIlwZarpC3WX9ACatu_eR3xrpcH0M4M9i6pwB87NFg0XQd81NV5htVmftOppZTkVQiwLUVWX_5nr2Lvn2GmMdMQNdSTEnOZO03B5gOfbP_p-12WsDWIk8iPmv39T78taZh3mlATUMiqWis31msIUuMqfnNe0QlhLLWgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27594" target="_blank">📅 19:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTABUpNg4ujIr2-PaAKQTcqQAZDFGV2Wl8cqXVS5R61FaOWDi1MpwHXFg_UcAjKaUru2HV1LZWAIXFDLAyEzAgRDHWcsAWg7lyRC2KHOBjHKw4plWlSdHULl8Xo3FWclFwBDW2HkdlK_VnbaKHKT1GaoiwCmZF0WMy6EpHerD4NZJbI_TZNdAv5CNWfJAhd70wLTyW67hzz6lX2MOyjcFeQD7saNN5m3YbRTWkJFcU8HS9MVnPcX6unn1loclDHOaOdrE7vWf7vQARCeUdrEq5sibi6oHVu3QknQEKarUgopnPAXpTDW77_7AIojBmEl_YDW2YD6uhUF36G2fWl6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛
برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27593" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZMuYq8OiobfzVRr7VOPVZtvjghh43af3TC-SU5HdWG5tDgD6oDV9PgcWUaQOgCm2W_WlPud6pkAw2w9plzb2GMe8tO4HW7QOVOohtkvw3XAH6mIfF3ly14KPwVwYz6oppCvywjMW3UgXsBtyXLF_3FCBajoG6rm6TMNIUteQCkjfgEfAMlazmqURHrg9escxuuaLgI6JsjPNgMWjGCCRidnz43r-uIfQzW89MwM_40X8LFKEOELC34_VQT9iOtaVbnllFfltdic7hsFR6VnQsBD_kRaKSHHvX459oMsp2Ke3nL6dCFQNbgRtiXuFvHBovK3wigcESIPh6cDzS8CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شانس‌باشگاه‌‌های‌بزرگ اروپایی برای قهرمانی در فصل جدید رقابت‌های لیگ قهرمانان اروپا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27592" target="_blank">📅 19:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAg3O4fu3fXirBHdJz14SrI84OjC-j_e9w8A6mmEPtqLQvC-ApT5KYSvuvNe4wE-dUi0rqSgDnMqjzFcpJjRQisXgpR0lzfDffDRSFvKIMmoBcrfomGtamnbDpMx_dsOOr929DxQZnsXg3D6YMfhrkRxXOyD5GbaYTlB8tRaZuMdJsoFuAJ-CJAGDHNrx_jJscoOWeqdVnHL9K4JW7DJwOZyKqgoYq6ZEk1Vr3dGbLnDVkHfdLXfzM_J1qc9UXNIl8FfYKGcwCTvFY3xlcZPBP5QKxOMG6_FpV8MarurP7hRzEKEPy9po_fUVosd8wVufXbbiZIJhqKNEkiPBZEsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27591" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLq6WtgZEsAwm0SDeM_StSqLEY8J3CuBQMGzgHNwkmv4rQ__AeQGSD8JKKax_D9CTKfF-RN3K6uC3FbiIMxzdPniqQ8FU6ufIyUkAq9p_mXv4tQBmHdhcVXGWN1MUGXeJWbuw-CkabRseJ1CFBuPQTh5PHEmuoL-YTmIHRF0M04iy-ihutrDGnj3tTHXhC11H26dZ-gv1y2y5gRpj6yfucGguo3A9NGi93UV2xaocypQUByq6E2Dz8y3S9RnnH_O4tgB9m2bcFBaeFhah0qddazXZaZTrH5cWeBhfRn2UokTL_hES6VmRqrU9eS30SLVS7N6e-gTXM3T06cnEfj5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27590" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq61NsEFK2XnMD9-GsJoIaq1kBWWd80J3BnLE_Kfhg4p3FI4rUwY8i-3fCC8eSW9HigocMzMc0gVoDXtqdVHvMF4WFWi2OV06BDszflKOuNgTnaEYPCctUvErJb7kWLp7Sa-He3-xEJwrZVyXndgpMeziFaQ2TAfvtMpBwWxYaNK2UPU6iJI3O7RB6yM-IjpCL1rboFgCGeCtknhzywjAk3yxO-1ZK3VSCjy6bdC1qF0XqXYKOZDltoPfenAjBATZSZmgeHzet0AQaX_f2o1YYTIEbVW6q-9PthbpWwsclC6dVDBBQd6jnf-S1snTwhVhoHymvwCwXiJFrXxpFxBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سوپر کاپ اروپا
🔵
پاری سن ژرمن
🆚
استون ویلا
🔴
بیش از ۴۰۰ آپشن متنوع برای این بازی در بتگرام
⏰
چهارشنبه ۲۱ مرداد - ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27589" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijVE2R-PW7t0YerVcH2d0z33gsVjKFfNdx4MiWV02ogHOYOURxzWQ236Hyowce00YSSXPCBQR-QAqxoNDUcZTTcZtqxlB9_UpGLI9CJRTCrUyvLWHTG3_49OSRfayhDKdhYj9PLgxubqwPPHoP5hKH2hoxC-vO5lkkrb082U4aAnKowykrwuwHPWyKfT5stlwQCiLjb6V2dmhl5S2eEotTkrsNutDcUt-1w_uFteX1ykxb6Qef5PM2IQsBgy3fVJplNm-ogEaP8L7c9kii0DKwwq2HsTw2a2FeTImSRGmRh8pmcYQwMPWu9Lf3tJxBMISD5zXkPAI8hp-O3-NohvEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغام سعداوی برای‌خدمت‌سربازی راهی ملوان شد‌.</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27588" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK3szXKG3xbIsfI1HRkiJTDZpcjL9s6hkFe31O7cMHAwSoyf3YosgOpbocANulPDxr5TPGYJwTrvi8OEfLe985RVIHcKiNQ2JbRSraXE_IG1s0856m71eLumfLzM0kkb_KgGFpcESjeCwBfgYXCPOn6erT4bZWYEBVkznw465tgrbu0m4YLh_EDfCrAIo64NvoX3Scrc37b2h9zUO9hyhhAYS2aK3ZrYk2iktcww6yi7ihN0EBWl-0m6d98f-5A5HFSgitm_8BRGpnXOuOlqaAjZ-rVmNaNW9cnNvDbe5Rdkg0wLF8Uw43xx3SuWuUC9cy6y1yPsbYOAyG_QDI6zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27587" target="_blank">📅 17:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27586">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnnHKUumAstesFmWSa_9dloZfRM5hkIDdmJ3tqMzTVkBRbGdWKCb8ygbmq1yjLo9zRsWgrVRI0YtGoTVE_WhfjpKDbAM83BqDuKQtNzYRdyl4tnneCztoY2ZYwWI_4y_hcSs-7QdGC_PcDheCqJcT7pTstWDOXuogAOXxHNZQiPG8ApT3RcZYexb_ExAv_kzBLBGd-DwrF1zPcAfVePck0DmLpe57yr21epV0vfg4UxTTprALUKX0sxC8hVLKp3cPgXYymT5HuSRaAWwPrXlw_mcr8n_P320vwo4b1fPDMPaXwgAdYQH7hRnTFfe8bcyo-ns-E4X0l72AYT5Fb5I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27586" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgE_CO-WecOlXkHCw4LNOX81fE1-xvbRWUuUiyDL_nwZqFfyQc3dZL5TooJ7WjcPB6WFyFCwCWIIZM9E1ZpyF_tkMb6ElGdoFQ2HKbOJCvZlV114tbrWh2fIAmYaLlA3scDN9b2x2GqZAzRARhufRSbiNK98gRjI3hZ-lGXtc0R7XdgRxWgtJbNkx1C4sWTJOOIqjttum9168bi5D8lfSzfGZYOB5Cn0nduurgM66DlrZhFSkbMw6gV7SPEZzhuiDrziOwP6ts2kdgjkd1KYeLxEnIifhNRG8Gy-qei8dAnUyKEf0sQbiyPaWxwTZQ-U4KQXnYEY-dl227D669nKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه اینترمیلان برای جانشینی دنزل دامفریس هلندی؛ جِد اسپنس مدافع‌راست26 ساله‌تاتنهام رو به خدمت‌گرفت. هزینه‌این انتقال 31 میلیون یورو شد. اسپنس انگلیسی فصل گذشته 44 مسابقه برای تیم تاتنهام به میدان رفت نه گلی زد نه پاس گلی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27585" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7TWYaAEx75oxisMrtmKwlH8AwBGcdjEOOClIUv0nHwQ2wzrAyLqJZA_sU2O_6FW-q-iLLXeiWrqAeSDSJ1ZMkYDHVl7x9M0-lMnCYKEIcZz3tlhmxXqDCKCw7u7e3mXSlK1CnLnXChTwhAqvLL7Tc3YIYidztf4rR41ABsPMk1vfpFy_HvUMNkZwHRue4VjORAzqP3xqhx_39eApfF0Wqz4h6S-azgmA70K__VGrD8N4dqkcBMRZ33dxdghMqwseRrkkI08mTidQD4fsvsXGtt5CHCqUZsox-8YUz3TbVnuhyDe-8uAXnlGH7Az2nazGBg1i6S0ngSpocgfP6DPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27584" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27583">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7ta5aeCWNDCDBwuppn-zHJ3NL5-j2fOQYKCZr1XmziSQar6IEgt6Am1YjkEualJXGnbgPmANjaSZYHxPMQ_aKi_zl7aTZvA8AMi1O39ax38o0eDfjJIZXgBLjcp2n4ZLTp2p2WxjEJiTy1yKLcCn8sWwhyFIYLl5X6xYKZoCZzACFEYza0lOQurcs-9qKefZ4FM30a6hexhXFClL8ni9Mcq2yI2VFsRDi3x791RBjYTqdJlEMTqMVbiZua0-K9ycfU9Qnse2OT8B-EEVKo_P_kW5aEwhD6JeFB6UrPWeu4TiFf7RHUa8A8F5vqbjKDaytV8jz263BiZI-i2-rVxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت:
«در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27583" target="_blank">📅 17:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUT3yNrRjbatcH2e8-M8MraylqLFBZ_Be6h-cn0RwuLTyI7WVD8gRse2lls6ktl6ovFFLPru-ITwJ6RpeuFi3ey8PAuc6tTCCTCqE3VBuGYd2el-y6B-FToGlXEbzLycgYq8kj2_5y87hiALPdG6JVidkiIwawfMJ4cg5FKymZGs3khljSyWofmuehi8kI2B8ISnzJkt-mS5wQxUbSOoxEs5GnZ9rwuVfkY_IOj2C435rz0-1rA1aHurTTQGnhshKzyvjAlcJgxIIL8JJfZC3yB-Ixau-RjHiPIV09x_Le589KLAm8OSpLPESZ15Cb2ZrUG3Fp-QEsa63OQ_rkSSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فیفا کارت‌بازی یاسر آسانی ستاره استقلال رو برای فصل جدید صادرکرد و به مدیریت باشگاه اعلام کرده هیچ مشکلی برای همراهی آسانی وجود ندارد؛ باشگاه بزودی نامه فیفا رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27582" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27581">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ERMWgJ2gFxlajcq5Rbmd3bLx-JOXTg1eXGy5bWqOBc9wHQkJh2dTjh2Wibh-fAZSrJ9jotXZTt8-mliNSSvApsHyNUI9fFcdvhkvdxaacZwFYxRp1rpZDToP6uy8vh7MDRIACGQJBRvFBaxRH6plfzvaJTQJKVH2BcYVORv9zWbK0UwiFrLXcwyv8KqWsZ9EkVSUMpPBBTtkZ1yqJmdV3OafuBVbe6LxqUxKgxRFZeRw--Xoz9aQ5Q0kCLJWc18M1IKZ5ahjk2Py9R6WYk40RKP46azfGVhFrhvT4WQGDpSaDxvGRZD6diCcmDGGLq3Xo7gCVFpB4jYys2Z295cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
درآستانه شروع فصل جدید رقابت‌ها؛ از کیت سوم دو باشگاه بارسلونا
🆚
رئال مادرید رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27581" target="_blank">📅 16:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGFIkoe22L3jVmFRXF9U5TdS9uocmgF-B3kdMZ-g5_VFwAaLwahgS5Ng5Fu1-o-UfJER_KmY5vkLVQCOltVm3rAxG6SRCixGfm7mrAIIzf03ZaS2zncoTR05p6mPh7Gx5dJbpImRbpaAFi2p38JNEQUOgc7ALfdfc7xR23GvPmmb7mt-u6NYmb3IjhbTDqiHbeJheyD1WkX0PtkhVVqiOfmjaHaqjvFOJ4-0kKHt8L5Ji_ul093HIL04i3LaQqI-v1W-KE-BWsMA0ahNCgIUqvqYoGc6Acg4FsVNKapzF42bTS4Dg7ymLFRHccgaepDAIuSzGz63Rrw7lgRgbts5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOaevlLIDABPH-F9EgnyTvLG73CB62ZSeLY52aUzopZv0q72BTBWHMTiJDY_dwZcaIREMBdmCpGQLImY2Y6Es20rHGErcMWu-MHPaJWVdRzlXZXFVpNMTBnmnMGsjChoL5OFV8vCjqj30bYtZt2WWmgbXVnhidEKUPy0IBtftB6qaeJbLbI2QEnQgpM9bLsK-oh77ZR3noMRq5Hu_U7mBLipzxzdija8Bjm1ya9rsihtm4Is-5bOHS-bX8-twinj1lh-6koNCF8-_za-bHU7Y9DD8MlK8dr58-JNzfZ6vPPO6dxY5mnZoyhnDrSfoDJ3O9G_qeM8KoTD5YJefItq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj-PybByvxtIfSLqOCMYB6L4tWgKzemu4Ncw3X8lEBWt6o1JnjM95NMEIYo6dZGKcExkvsgD_0CsULENi7MraQKyhZMz2dQKP8JSBBmW75vRuo91b3lLYJvKkEJVWHufh__Sq8Ha5Uh3ZWPh_zFE7oqkXIAEbZapdtPraAe72tNbfTqT7oEXYzTOfuMluvh6dA2OHZ1TKWHmjfyqX5kAyg7FfDeJf7eE3jYZg9JOxe0C7lysj9osuF9Y6nwWBJjwA8Qs-FBp4w7AvA90qSwTKleYM106ohzp9Dckz-u_ZfUFmTndL282TEXdu3TM_j5C_x4kUXgxj-hUXE7emCc7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTg7XFtB7nCbCI1XwpXqJSdddjKB1iyL0Ay9KIJkkHarKKQWe3r2y-Hoomxdt5wDwVAmJJl2Z2HZ7kZBCeIZBqP-9NweiaavWskZ0sb_qSrN_O1uI5Say_2oqerEyiN-eq1kjNRH9RPBcpZk8Jicf4l2tnLVysWItag_IiFW5Av9780aO9oDygX4mj2giHC8-useOpRqa-OWd5dbqMGl8aRQs8-ZJ7bNjNQfljo49jxwo8pUJ7cVXHgpt6LzFeIhIUmzWS08WDLg0MTwKEe9PkiIS4qS_phY8gU2j1aoAhvKhbzAKYn_U6nY3uL2YhQRe9_OoWhiY-hKl43wldHg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbvWJrOHmGC5YwARkxQY2UsN2-KoGZaszPpSomEFlA6w3i01zr2hmLxjtytGMmRcHwNVxWWo0cR3H6O8VvvXSR4RBzCDhu3zpznM-C1b5KtLJcyZ2xUDk_vhtw1Sd8dBS1ohdtdaiXHGWJrmEBMFqV2CEnsMbvLejFFJ8t0gWv2wI_1dRT9cuTpDI9ko3oXpjnHsYDUPK3p4u8yMaZsR18PYQ1_Tnwd81vKbAaiGZQw-U5M42kZpOK-wM6FZLzCbLpi8iP9RxWAuNRwMlf0rtTN4HHKxgG3oZczF5broNA-aPedosag4Azb1vOElDs0j00GsRM0_d3u9BEi27JQjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya8orXWVa2nmHR_aSSkdfWZRFz_8GtzRIwNIDHbD2_x-jYHiOOikupuaccZ0GHz9dKJui2PWFLO7sbd4NLGWF6noQ5_ervtcLiQXTLShqY3ypoWHlVvmXxZ0GzINLNylywwtid_SC9rGDVb84I5rtar8CMSQGOVxhcBnMJ6IfzJKz5QTcQTkBFnoN92qiWvriWGxqvv4OcFk6NyBWQO_jU5FXeXPLuv3PlxFxFlPW0DUya0qwUqGiWnVu9jrU6ijhHUXfyEcRaPk5pp4EqE230GHWSYoe6oIe7-RSfSDN4uehzxEU99RJJaODxom5ImgekP5YpxcvDcdDMPugludoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLEgu3NbqOP8aonYHyMq1RXuXqkYy-7Scqz2xa0TfJLDC44oYupVUrgX0Wrt4EZmMgMeLF36Eyc5h6A14zB1PECp94XQGszSwQtd7qOtSLBm7QUUL8ooF7hUveeHS5PNHzZndMJ22rOp4UoGKoKQ3X9jBPBB6Uj8CwhO1cq_yzsY-s5fXJ9X_TKT1j7gn1vR8SYMR3zgT5G8fOkAD9OJr8umRcB4peHYd-n6QgGV82fq_4-NKpl3Vk4xjdtupjUkust7XlLwIfxIFdthRAoZBTnI7nbVGy1GnE26BLIFF3XWs38mg-nRTs1cI8-qus7IxalqqmQ_uGMfAR2WP_HIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2atq5RNYLzUIxOijebk0hk4DVoIonwd2ReFvwhqMNoU9NGk5CxhMZoB5KAflQuIH5rAWUaatSEK6O2-ptdCUURLf6vlRp_p9QSsskF2F10Or_oB1tf-qJutH0rH1TlxQ6mj1cmTLkSlIap7mfd2EqOuLkDNnJfT5vmiKKbwTNy3SXot3DwzYNM_-xL6P2DS9Jbh8sgas1zbZBgiIjuj-JG2PLtY0bvEttF4JFXJpX8gg9UVFSmLPjHIWBL0iHjqh44T_5m8YpcKAozP77MK9OTLdIB6hc8S55WmKGJ4F1X8J058Uozxcpx9paZx-gkO2WEkX7clWwB2bxqq8NFlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPa-YhWFRt-HW2bPPktx10GGLwQLAgQQsIU6gA2v-We75b-T-1IGGPB9EnK0s2jkU63lRxs8DpF-RYhAsVeqSx_jY7qZLXv9VWyXErRAH336naSdzMkXtaxPOMaTLqcKErepO7nmEIZY_06sHUDnNk5IiI1qbn9h4YxamJtITK-edud6uM4x-2lA1JlDgjSmvGkJrIAMqFxDDEQBvNMkIf8EWjP7yLtKaQH6lt7QcGMX1EHnxwe9XOAch7znIi4HeWaTsFs2DFSKUyd5Tg4ko0wathYWhk4tw5raoXPFJ1dmWD6hE1jnafCtBKSSifhxKk5qdU5oLPHJooIyM3T0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyStne_NqJma9jY2Qlt63aBn8I0r7qnrw93519XQZQYx8ibS0fj3ozjAD-0LTFWU0I1dPttKGxWLsY13eXYnwKD9eKvfZtujPUxydlu8siavG2EakwIgx2-XxwvTzcmI14TNfpn0wiChfKG0Lg_ASWZX8tw9n0_v0ijJdPFeGYpgG_0GdswzutzwQ_FSg9B2BBw_xSNVMQpN42lqQavRbZHevV0yfRZSONGVlyMSQZyhQoCvaU1VOJcO2D3tAw_grS5qi_maTWxAX5DGEfrxPftG4m5S-tY72HOwftakE-ZaB4XqbeN6jBPTeysHHvCc2kqmA1TaaILkpMLvyKcRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elpXWldrsVqDtIQ1y1bQJz3JWNyMe2usXLjCGkqqwhbsHIV1aqKb1S_UtTrbrVZeUWqd74BnaZzFYESkmROnuG_2FGiqJMpaja7Gy3E5Y4-fO0mIWzBB_1Rn-6B9nl6tudIuJYw0QRL9W7edK9Ln2zizlvDzN9KKuMZxcyvXkcV9j-wwDwaH6n3NUFjGSExG8HxmLXJZqEs5GSb1tVYUSntNsfmzkZZstHrt-ZANI8x166vUk25B1Sxf0PH_SpWeJ1GQ-FcerzXFaGn6X1dThWZsNlfBfr-qmzsF_y0ZR_9x3CWw2UCZuEpOj2DBfEj1TRHQEAsfuDtIO_Qxe9dppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0zSFAvFwKaFHnHS4H28z2KUH1CupGJddTQHnT3-YpyDO7kqhYdIi7_z92LHu9U3e-N5nguSUyL-KF_ShZ0ZYeYlG6UBi2tnuD9E_eCBUd5pFmeymcC2PcxQUvkeEm6wLDeqhoPgWPzRn34aWIYHJDEHYKnVnMvKshZkHMEl-nucllnLcQOltifyqW0ZBGC9f2u44kCCtp4YW5QqygZGXY6CK4iFmw_XDJQosc68RrCaffAZPqD8I5g5zzhhtwPkF3zG86wIg2twW6sH1AKyN5CR500tS_DIWt5j7XQw5D_ZPQQqHaaNpgpONkyLSNuqTkQ8YnBaJ5c4piLhK8Gk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjz1zhE748vhCi5Xm2aaMK6HTaZtPoOKzXPUs6fRS2BX1hkj_H0or1KBNWEVRHDTZ8nfD56k_Bj3C6jOteEulTMle0txvljM3v8Dfk_0GYILZwkopzd4e1t9pcwio7MaTmwTSbP-XkhRMeQAhtsSnH9-OCH5bW7kYCAay-QggHyP6EkUPz2B6kJ4ZNXiFR4M9SAyXi49uUjYH12NxloHUSrpwx3rxvk6dLPL4_fsw3A8-istEjFTgYwLilyF58_Sg3rbELUZJKlnw2Xgffc08Ug1Nhch4kVEpJVsO3UpSXA9bxh_VMULDj2--U9uxE92r7DQRC_5fk_sQsYD1lvugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5dNVw2poi5b_-WxUiUI6HaEQ5wEffB6ZqLmTKfmYw93cPZeWCXZoA3SUa37uluYus2akP_SL7uja9_3UfZ-yAKQlZcf3yjUnJfKpYwguf58OiptYc3PtPyvNq8oNXghTkurCGJtcIPRPFGER93ZI1aoQB3lRLj4nIjGTo_Yia-eKv1Uir9W342D18hqSa4Lk3YZdAdETwHJY4bI4YUFccL6bc4m2MDUuqZPNmqJDC696VmQoL7J2dOwqExdTNckpqlYwy8HldMbv7Eqqw7vrtskFc5aIS8nQQo84uZ4FSpVFhoJSCOzL8Ou8L4GveaDQ24gvwEuwGXCIHpFdv4UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYfBxxQhakmOHYntDkm7O10t9nfQvZ67iEDkJHgZKNWTzt09bEaUMkOJ88HWukGfPjxL8ixwFo89YCNiHXxa6g_WOi2hTKub1CpV929T-_dfCnUt2Vqbpk2N3NodNYjDLsjfvQsBh3uKOCHuAEnZ9KrflVO72XgauO8j6yRa-vBCyQv0m53PQ1cUvwjxPf5L2RISjV2pvlG8mg0r-kNPu2y1294C6d_ueGtcoQb0H6CEF4yMjYdMbdsrcJKQ-0jV3g6_LOgNraSWz44YSKUtdfJUfePWQ3Zff0i_K0G6Ojs1cr8BXlak-Bx2lDeaw3BOR33hnj9i1on_2NK495wu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBEYEr2lnYPjspT4QMfq68wJ5Z7Z1r-cWqyqhZeM-wJLA5PoUPUwT3oeQDUaYAkXnN-Wm3bQOzJp-DN45a3tSUSTgHeqfi3NqOw3MF1_XJD-EuHv1lJUtBYa-2_VeKBJSM2dEuGItfMt_r0sxVdNOuiW_hsJwZsGZHC3le7X_5AI9o7mSiBlQxH5kcRJJhJj_O70ymzYckDNstFCPSGdDEXVTno8ddNgTQiMSYNutCzG97TuV0JVIcZ8GYr7Tt3_enmZinE0sfv73ghUC5k76sDgZyNwz6w_sfC5QuU1oFh343maSit_odiP8AVqcHw28bQWNYwIycur_YBpqkNFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxjjWjn8QMonliIzbbij2A9Dfl0luTlXIO-Su3cynG8DCUFeDbYGIYq3LWQ7AEsfEoNol1mgaHncq7-Ta8OyZOUBfYiepQWniRad5SesCBBC-Ye7QAhD3Gt6b6-YEocMOwK75w4Z-MKfHH6OQJTSZSGzOnonZBXouY00DMTfpvobTb49Q0d-aP70tbuPdqYH-oWrW0jXE0NjCkcOqquMfJeyYy2zwItGYq0vedCfTPLPXD4jiD4TErLOq2caMISCbuKopzayitp-7bG9vNiP5ulXOKKpyWXpxPnw9UlajLC-tHR7V1-lLAdCsBEUV6OzIiBgm1Fs_9lZEftQp1n8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXUcifydmOzjJq0__LDJ6_sDSsg6sRG0EWTqrBssC7MQPclVeKy_MfYAJf_PP_UIiedfFTCTeMBdyfCjEHSOce904I6yQchi-W8shy-yAsiVpMoc_KD9ps6kGH3Pb3VhVaYQPcn00cXj88r04EINuryhzVQn0dVpkC3IK0fr-uVRTJVkteVomZbZZf3htn1iQRBE_8qEHvTIwLgVxQPUTK0saQ9U1_Yh8NuR69dTeAgjs1si4qQUkQNJZO8a4MZCQOOpW0yCAhuVbQBwyrl6dWraVZz_PZkeQjOxHM9VSmJx4-cGdNyTm8NJwju_E_XlbMaebqTuTSptwpsvGSq71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=I2mYtN2UWmujNYZGZ19axOJ8XIMLnyNciSyZ531xqtLYuftHdBvg1tYgzJDyfnOf_Yr9jiQxX62v90u2BszOIXWuafcJq6dkQYgGWosKMJWrStWuTNUMeaFnBeQd4buUl9dcUFEGdoZZ1rWBuiOLPRfaWbl_y7pd6qiX9Wd7WFutqiLby-cYW2XRh2LWf1EEaqiy7o6VtL8LRkatxz-hSVCj2Ldg2kOx8wRbCqhe4nqIv0BLLSOxTDsPcifx5ftCf87DcpOJWxFM-8yB5WT8I4M74S3ixIuGSSWOuNXfGqzhoUurTGoN2kniW5zzpo3Isug10OxLyTXUrFqGkKpLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=I2mYtN2UWmujNYZGZ19axOJ8XIMLnyNciSyZ531xqtLYuftHdBvg1tYgzJDyfnOf_Yr9jiQxX62v90u2BszOIXWuafcJq6dkQYgGWosKMJWrStWuTNUMeaFnBeQd4buUl9dcUFEGdoZZ1rWBuiOLPRfaWbl_y7pd6qiX9Wd7WFutqiLby-cYW2XRh2LWf1EEaqiy7o6VtL8LRkatxz-hSVCj2Ldg2kOx8wRbCqhe4nqIv0BLLSOxTDsPcifx5ftCf87DcpOJWxFM-8yB5WT8I4M74S3ixIuGSSWOuNXfGqzhoUurTGoN2kniW5zzpo3Isug10OxLyTXUrFqGkKpLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=LVZpGc_LXXpejJoJQlTqWDal87y3B1jCzaTRNMw03OgESryZ9X-PNQhZOXttE1d8LdB18s0aMqxcDM3nI6JWZhjOCGJRF6XkCz_RFM5MGSyVrruUPsSBzrEIF3z7CDPCw8hPCK0AjNI2uKOKlrwIsGPfK0ekYTf04QL41wxoxuaC-wty9z_cAH77zgFEeloYnDJq7dN2zyYmh7xJrljGpixCI2oinS7bGqt0xrr_LO72nGE72ExC7WCe6oiBgQTwxxgIWUMHOpMU6JGdZl8_MGChGMWMBuXJ2vDNSoZiKhiGYSm0842QL61viG0o1R7b11OFbtCTjEaZs8S2KCTnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=LVZpGc_LXXpejJoJQlTqWDal87y3B1jCzaTRNMw03OgESryZ9X-PNQhZOXttE1d8LdB18s0aMqxcDM3nI6JWZhjOCGJRF6XkCz_RFM5MGSyVrruUPsSBzrEIF3z7CDPCw8hPCK0AjNI2uKOKlrwIsGPfK0ekYTf04QL41wxoxuaC-wty9z_cAH77zgFEeloYnDJq7dN2zyYmh7xJrljGpixCI2oinS7bGqt0xrr_LO72nGE72ExC7WCe6oiBgQTwxxgIWUMHOpMU6JGdZl8_MGChGMWMBuXJ2vDNSoZiKhiGYSm0842QL61viG0o1R7b11OFbtCTjEaZs8S2KCTnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK1ROcnQQPHzEzAu8IB-VvYrppQFBHmv-gsXhijuylb6fbBD8OE0dvQtfZ3zsRWr5ijPV4z70IPzR5CKqrRTSn8p5CK2cQFF2-G6NyQXHjI8vSeC086--ke19Skf1mzKF5BDYV_FkWCa82AyXM6EqZWf7u-3McDiibqT87U9c4EBmu_dj6AUwtpmB7MEYX0h86YXRNEmNyC-ijiduWXM7f0o6tx0PILMc_SVopra-qIlanV24-l72z37Be6-1MbwCwYto4bDMKPJ77ZMD9hC67zO4NELUsNqN4-fwEutQUhf6BChwuyRwPnqIpx6DQwY01BlvhSztljoRuighoTHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1n23JPeOFcBrtEXcsKJycT1jmAfnIs396SQGoR8kE3xgCuk22JAxxgEVba-UzmjXpXShUTQ-kqz0DjIEpg-XNSUa2-M-EJq2bq0OTSDCgK-zi-M3ioaPKCakuUGZNasuUkZnjiyp8MHicigu7dFmG2gr0HSp006o2Qtj-6WOGoSadW7ZsTnSILlYypSpgLyJjIGd-9xPzlsrlOfjHoDJhcZvPmz5O_38l-dMsP9M7xq6OzPbnSWV7doa5XHl1r8D4inaa4bqRUsC4zcSq_Oo7tDjmk5nnw0sDizgD8iZXSt0c8eaqEgPecLzB-LYvsrDC6nE-czU93_9fKVOb1wSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhMt1gz2qLauoU3ClFIEYfp9xoh5WXCYBMMtIgy5oQUhR_fCoiyJGAhT80pdU8BPhp4cmdzOk4lQeGOpLRaG8lQApdFUfVQE630r0yDrBP8hCXtdied1Fz4Levi0m9D5389kVu3mkrgALwqa9u-BhvLN0yO9aj1_hw3QQi-cV82-Bb8awwXc2eNvtBGEZV2eYBBbaZNvD9L11lzU_9Sjb-uXD2MXqAn0L8mVtzrm2g2-1xfP800qD_BT49PkXumchP80OSPIQ9nbgtntNnox-4TZ0utSMDZ0RTdsJVyiZaPFs_FxeGeMz4cjDCpct0I04iVZDPKMu0KMrWgH-db-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx4dV6S2NgzdoLvxyerOljDMG8M4qdwNB_mJExAbQ3GNPnbwbEVMZs3eCMD7NECmYpVwIhvUCLq3U0Wz9fuCFe0XXzBnk6WGUORzXC7LISciuehlVPxm4P6zfsk8HUp9iaayw__MVfIc8Ppcvjn7LnAjfl_1kdATMzUHksAiYoIKtCRK-aQMQLp4BKIVJxUCaXjlwYS5uIgLodQX4bXCLBVOXsnnnoZY5aijf7nx8G_8PFFwcuaTNIiFyurBdlhr71i63-dZU-IcMK8xJf-eEb5GI4C7U3p6C8I56hzcK2bq-tKWPDuiWqC5yujPU8sbenJljuvELg17Qu1j1VpW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQpTza_KSP5l3Z-X0O53tVSJqP5CRBuM8po4YRHrMfIqm_CKbA9KV5dCcakLMPIql9_x-e0OOub8gwHUfHS6gucRkABPL7niC8VdKQw2QHuyRPQzVR8MYx6PucON0oSQjaq143vgqTcLRd2Pi9GWLTCnTqjXtpVvO0TvYqSCdtVJ8FzWb_U6xiPqyBBYtuI1_nPjrkC4JG6zBkyXxiMryJaQXGZWWaiS47fUqf24EhqDwva7YY7-2JLQOCS9nY2qW-0CaG_syuQBLk640BGhh8q0bP7WuwNWo6uByNAlQHHOen7mW09tj0MJ4idlYSyYKjr3oMOUlRQ8r198j5ySjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgBSY3P9nB7V2uBMdtwI8RKvCkJAXnWkjge2X5nvfVadRIgUiM9zLj1FeVmWW5craA9YmrJFDLEzsF0fOocrmBhVAdUPXu0Y40BQ3uE0kqBIbqCQLdRpcrsl1Gk1fXeg65jEfnDv0omnWF7TI1fEfFtg5a4Cv1Nh8sFo6bSGox0ifQPxeu7QclHqT1Qk3vWOmybUVYm0w8UIKjxjUYbR_al179njfu2kkNUDKkRR9lZ9CAWUnqtiCZ-TPDjzr35zwPvfOlR2h4tPT9p5n7lT4Wb0B9ZHcfF1xNYGXvbdjDIB-b78WzN6xGQK0vJtpO22X3s5AIdRTAaOQb0hQGO6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u76x0GrUhiWI5OvIWx67g2TUMnh1J4F-IY8mxbKvhxyM-WvAIKfb0eQoRw6kFYpeDPFAz0fN2I_fzAMdu_5CNY49Wnc6tcCZEIU8DfBcTcZ6UdMRYdYrTsJnBDfadeIcWBoEuzyxyoW-dxzKuZ_H_GJmNqHETBgi39_h6K8N3SNOPJN1MfkDiur4xeWIFClRSoBCw6o57DWX9eDvyaGzyxNeBPYtWxUtXUTLU9jcwn3wP768wFc0s5ewKLgzT3jrNWJByBkSX4fo_qKXOX92wvUjRBWqQNPF_O21B0MnNhO_FqjIlCjmVxXS_TJjMTEHffWTbTEIo3KR4FtIpnONvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYo6acMDVsaOTRn9wVP5ATrD0wr-RL_WXC0FsZx_WL2nKRMR_w8vKGCxaqVsTZHeE6S5VSTC-7H6GeKvd_wVpEKkNPZG08FMpQ7uPD0wqpBd4Yeg0Lleb1KPjtN80Vz5sXZam_Os2R-waMbsuhamwgvsIOw1P-kvp3ndbAB-OrmaT8e_08eklkFWJFxq8AAxkOUTp9fSpyBmm545I_FIToaXvIoyf3TThHDoaU5UVUmxN3wolOlL6xldgMSYqJ-9k3q6o2u1teSoal4NELLzhY1ExTWos5bvsqeJ4Tpz2joKxLrlqOtvurX5tfzDaNQzrX0OTCM6fVDstBaxM5pOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8-yjpukvCmus2VnP_Ibo6BaDzVhd_lana48XivAKwu8gw3E0_8no5Ea1wst5N603N4JBDi0TMko6oSg0S923PxbX1djgdM9st4lN9WYhrXDh693icr3JlRCZGd4dZhhe-EAjuo7LSKpq30pkFOaDlUVHwL0hNWYfWd72VfFZdGd2LNt2v--FyCp-T2iVNlkQDR8dyfQ3wFTn9VlPLG__gJus5n1MukoIBPbwBG6lKJOBm6djhah26cCA6TaoxeQtw4TYDp8DGoyqIn1_54ARLitzFN4ADvOC7lnlV9Fn0lew6-cpW4uvdtrCtxcYbpgCb_s-utICOcX3Axnikqoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM3VxeoWuI7n3HvOAF__p8pLlijC5n_Gi5UlsT_pj3jCA9AZjxEJjDZRcCQZavlKIJHj8aG8jHovRNzB2LidVU06M-OYK060lZhtrLAdKpIJJ3Cx4dDzQz1VVYHsW0hkrKeFcbDJjPfzm_DqvGFwAorN2xsadw-cGtk9y8SuAsCx7A5eN34RYSCsqzTL20JUeGpCQpnD5dD_DoRSsB721_5jgZOhc6-jAz_XoM0qCOY17vAJXf8fOhK7OoKy62jnN3NQNTu24T6rs1gUfdhObqU6Jm343ec85UkUwR-nWxIak_PXYHTCKHQ23Yb9Lb0VG15FF6iEc-Hh5NxLzuwlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
