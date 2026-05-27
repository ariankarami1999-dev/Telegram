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
<img src="https://cdn4.telesco.pe/file/WIUSo-T3tyYpo5Dtkz1xo7xomoOCgtPrf8cZLRjcpw65SFgNmQGBZZrTitIZUau_0wdAWnqjinLwX7TvKXDyd0r3mOUKI1qgizBRe9dzaytIf-sDk-C9OzxQeDTe-a1oCPrV5FTTFXvPgNsRn2Fnm48p5V6irGkTyujWe-7a3haxWqcyo25BW1pE2LgO15Bch0YQi8XMmI3pxjs8R5zA8g4SKiW-orgT9z2kold3gsVwzvEUceHkkBs_26HwJbObfQutnd67nKGLSb2VwYkWuh6RuUuBvV92r1Sxg1KbPKC1j4XU8eyVEWRfgcrLFxK8nW7lhLlclN43RZ4aYzq0-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-438336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHaDNqGCd7sjBb-oZEvrmuLR7VAXpaxMZxuaHmzGz0FkdYTQ6BxzZNwwbnwGbAy7B7zZEZQzWqe_-MucGQNMvZDY7kQPKX43xQom5KQiK2eMO1GiNWS-yMiLumGOigV5Dbp07siOfWC0YwFAPBhdHltYGyeZoTUZD-PpR-k6EE3H1d2IErxFclODfWZKMx8rqcXFsvQdfREsm_zKTA7r_Aqk-b9in2EIhDlpsJ3c2ft7x--3-NdceCi-SmZIvNCOidPUy4gF1N013_FRDkw7XSLDKphSpVcywmRW_PAIykVVi_uDTG5PGij33KGON07HttlEtnLNmf5kuJ4qEWG10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqYlM8mASXVOXSlhCd568rM7EuscYJsjmAhVBE_G-Dk0Q80aqlQ2wPSQXH_iiN9VH4xsjQuW0qade8T036PtCCpU0ZuKOcQA88mhkyvSHnpbEPLnu3vYpEEU1WcrzbA_vUA_7CPAXs97MiBuCjF1ewU2Mo_IKXWTFOQoiB7u570sCSq8tWp0OIKXNCPN3fOV5yzPfRqgf5TU1fuhOGlqpN_z1MJyhEM02eSwcSblQtfAtacWewLJVTFZ22ulG-P9zt_so174LTwQB7BU16BtCrnNObQS3npUxu0SZ1yI7HGmN9BgzSkldAZ5lEV_K0HJppIA-XzrwKvUVUmYP3iFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wen8nngyzAhrXSXP7BsAcndg25i7V4PGx7EBfam9orERM462L9V-cxyQOsyD5VNDoci73ZE3gpT2tbZ3kaJPJDXeYpUo3kLGK6H25AjHeSR-gYcBT83UNEZVQU_3gHTVQyNMZBJwDPIirSinsus7RE1ZdUoRrNcQaeblzabxCbzZUiOFX-CmC0AUDXNRNubu-m7mJjKMafOCbVTMGzBcorYxsOKlCbXh1yNvVNFp3jqkwb25_g3tS_U_x-hUh5iChOx4LSkH0XZ_Gf1S2SK5HiOmLQ2h_50VYWSJAdtegFdncsiVV9MwoJjDZrKjM9yatNTAYNhQ4YtXYQZU-v_nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH2tD6_ks_GSH-yfSf8p1rQMslqOlO1x9hBguSkPyhEL-CIYq3GFhtGh_ZpBqkfq8TX0xmTswVD4ak9f0-IDW6ybdK3cae0yzdp77qDDzJu1ybn5gNYlpMmqgzEyeM9VTBQhr54nXWgj2ug_3Kff03TA1x67_VGNtVr25duPHvlCE7RMtHn8v1juJobouUc5FqQX0dLCu3sNaCgtUU2vZvYPKpsos9r75gPl7feDFA7oseehDVkufF8fzAMPCmQAxVXbSQW83wLSfBMz8keV-UMojlY_-pZjkEOG8h4ViLsK2RqTGPcFp8Ym8C1NYH3xq3GMgSPTd1nkOF1Y-vSSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTATaPerdj6hz6_eG642OGr2AaYN17B1dXraZyH9qn9IZy9Hv9k_KjDQAXrd7i8kWMMvs19xKu-xJG4Tnj8Ycl5rsT5dUngNN8cono8_6RCpyjjt7SgkFZpJeO-RjbQg-fT8MMq3N81pciPgz8cRpxjabekNTQU-y4asjFJ9kZDBrHboS9ZjXdx3eG6Wh0RbZ8XCKZ3XNAi339KUfRkw0Ab8MVMllq8UsUIW8HROX2eWcK1fkC-F_Rgv1-dmyQvrajgSEcll5kLoKZ0FhnPnG8eW4hWDn3Nk0WfgUE2O0gGHal14L1j30jC96yOtgmyErQLFiRk6yx3h0GSlSis_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldvguRAhlhudX8kdZO2FODO_bDMytTGfh2OLSbBv306IHk01Fm2O_xnL7e_lKwt5ENv5_dnEQA5A2Mnn49MZAYeYodXt7hJT_trTuUsGhDDaycLwkkIzzxUBS7RtRfLSKxkwwU7pNiItft7Q1zv5SOH4aARgV4r8sCI-7e3CVjZK0P9zFPPjsfEBRiE-cU8Z2zrtnhovkx4mJeJIfJA64cvfWuCSylc3jOj6BVF3ODp10mn0-LCa6Tdo4e_B7oLFIYJtBD4bARLugqCwRsJAf0sLzw-5E23GfAOvhiohqPRLImbiAEROy8PSBok7O1eoSBHY20Eef-s02INQf3njuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-X0TT1pHLbawOtzddaOVSvW6SVvwdF-vbbUOj_M5EmAWRXVsZXch7ndigCMxJ1EqU1J2t_EEAEZO3tRYpeEG3hehUNfeGPsRMWkpZEi8gCCJElMw7fbnBO7025miaB84702UteeF9ELHS_EIK_6lbIiC1OaerEdIRTPctLosQmE9lWFQMcmukUKWrR8gZ0o33kQMESd-AdtgA4WDsGMiKgSeQL6u-daEJbwILy02QOScJOhEqq9QieQ_rRb7WcR71noLiH_vGJ0h1sshOtUt940PEtY8QIsbNy65fwkIFnA6t7S0HUKsVd6VGiAo7i4h1gyLIAPivOtLyrAeP4x8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز عید قربان در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 476 · <a href="https://t.me/farsna/438336" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز تخلیه شهر بزرگ صور در پی هشدار ارتش صهیونیستی
🔹
پس از هشدار تخلیه از سوی ارتش رژیم صهیونیستی برای ساکنان شهر بندری صور، ده‌ها هزار نفر شروع به حرکت به سمت مناطق شمالی کرده‌اند.
🔸
شهر صور طبق سرشماری سال ۲۰۱۸ بیش از ۱۶۰ هزار نفر جمعیت دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/438335" target="_blank">📅 17:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بازگشت خط لوله‌های پتروشیمی‌ها به ظرفیت تولید قبل از جنگ
🔹
آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/438334" target="_blank">📅 17:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HAqinqwt6_cQzXbHlsO1fC0oYNKKBOSiUiV_X_PnpIG8CFztnYtJ-UD5RaO7uLgJ7Dx10cd9h8Sy5C3IT3ryW3ju6-iXtAqAdC_BQhKTn3bFzmM3nWisJB0pPhdyE1ccgoiN2OWd_kM-sx5bTNTX7WwlAq_xuRZ7jdHQt3QvmWa5J3LP9StMB21wCEEBg0mynHtpAOsG_iTqLdyImb3L-67zZ5CxWBc-ZgclumT4EA-CQMPvnZW_4ahknUvwwclbLfj0o7PkPp7-51vrgiF84dko7QWw_MmnqxSKJKeuqvVg3ipAfJTIp1JFnrxS6hm45Q-LuJLEJ4lZ_YGrBETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط ۱.۴۴ تریلیون یوآنی بازار سهام چین
🔹
کمیسیون نظارت بر اوراق بهادار چین امروز اقدامات تنبیهی علیه کارگزاری‌هایی که یک تریلیون دلار پول غیرمجاز از این کشور خارج کرده بودند، اجرایی کرد.
🔹
با این اقدام بازار سهام این کشور ۱.۴۴ تریلیون یوآن از ارزش خود را از دست داد.
🔹
۸ ادارهٔ دولتی جداگانه به‌طور همزمان بیانیهٔ مشترکی در حمایت از این اقدام تنبیهی صادر کردند.
🔹
این یک تصمیم هماهنگ در سطح دولت چین بوده که در بالاترین سطوح این دولت تصویب شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/438333" target="_blank">📅 17:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کشته و زخمی‌شدن ۸ نظامی اسرائیلی در جنوب لبنان
🔹
رسانه‌های عبری از کشته‌شدن یک نظامی اسرائیلی و زخمی‌شدن ۷ تن دیگر در جریان عملیات پهپادی امروز حزب‌الله در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/438332" target="_blank">📅 16:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مذاکره‌کنندهٔ ارشد پیشین آمریکا در برجام: ترامپ با یک جنگ اشتباه تنگهٔ هرمز را به‌روی خود بست
🔹
شرمن: این جنگ نه‌تنها هیچ مشکل هسته‌ای را حل نکرده، بلکه تنگهٔ هرمز را که پیش از این باز بود، به یک بحران تازه برای آمریکا تبدیل کرده است.
🔹
قبل از اینکه رئیس‌جمهور این جنگ انتخابی و نادرست را پیش ببرد، تنگهٔ هرمز باز بود؛ آزادی کشتیرانی برقرار بود.
🔹
اما حالا خود او مجبور است تمام وقتش را صرف این کند که بفهمد چطور همین تنگه را باز کند و محاصره‌ای را که خودش ایجاد کرده، بشکند.
🔹
حتی وقتی این مأموریت انجام شود، حداقل ۲ تا ۳ ماه طول می‌کشد تا قیمت بنزین پایین بیاید؛ آن هم در شرایطی که هنوز مذاکرات هسته‌ای واقعاً شروع نشده و هیچ سازوکاری برای راستی‌آزمایی یا پایش توافق، از جمله پایان محاصرهٔ تنگهٔ هرمز وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/438331" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dArlIblQ71qZe9_0EuIvTTXIxY-GRqVInqMu7RDKoqSdVFkjvP0ffAGGHDT96hc1zvzTBzZtqICRodcUn75nZwRjcf71maBFhLix9xnCdTtjkp6E9WPnzmmH31Bv1SUqRLHm0uBqN3OEDoOyymrXL0OSJ5c5mTwQgxTQX9ZdZ4mon20VRxY-Bc9fsMguMxH_2_XP5djRZRTVGPCTWf-2TcVpWqcZdWPUAGkqDyjJAAfBODZ3lFtw9hi_eQR5PjfEmc22D0Ug_eXKQoXaAH1yT-Tkl-XTQUtDDL5vA6kOgWkjnLs0__D6wRPELs4MLAQuew8SBDvc0xlJfUkLLg47dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل «سرایا السلام» و «پیوستن آن به دولت و مسئول کل تشکیلات نظامی» خبر داد.
🔹
سيد مقتدی الصدر با انتشار بیانیه‌ای خطاب به نیروهای خود اعلام کرد: «به دلیل مصلحت عمومی کشور و برای جلوگیری از خطراتی که کشور را تهدید می‌کند، بر خود لازم دانستیم که اعلام کنیم: سرایا السلام به طور کامل از جریان شیعه ملی جدا شده و به طور کامل به دولت و مسئول کل تشکیلات نظامی می‌پیوندد».
🔹
وی در ادامه تأکید کرد که بخش‌های غیرنظامی وابسته به سرایا السلام باید به «البنیان المرصوص» بپیوندند، بدون اینکه هیچ مقر، اسلحه، لباس، نشانی یا هر چیز دیگری داشته باشند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/438330" target="_blank">📅 16:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE1DY36yyYMQMzCZamy09XBAQzlo0ZqlBQplEufkafsUcVNUCi_om7njgAJSm3MrH8W4PBRYzSJtJvtwl1pBPQzR6lG5Nk3n9TfNeiMKj9bDEUupj8tq0YG_5ZTIHR3KUSHTbfImJ9wfCdmsdKF63P8EN92uznWDog1Pk2YL4IZtla4Rcy54l7Qcw7OIQKLJkOjn0IIRmMJorjH8nVWjxlx82Wj4JPudebEbJmNwclbzkg_Rhu4KjnJndLGqojHL9FL57UTkcMtV68fxHfkk5F-lCEUh590umotKpo1DCFj9zdCquPf93zHYov5GmddENL-55NUnZnFWofzIkda5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم در خالی‌کردن ذخایر راهبردی آمریکا رکورد زد
🔹
جدیدترین آمار نشان می‌دهد که دومین رکورد بی‌سابقهٔ آزادسازی ذخایر نفت راهبردی نفت آمریکا (SPR) در تاریخ اتفاق افتاده است.
🔹
هفتهٔ گذشته هم آمارها فاش کرده بودند که بزرگ‌ترین آزادسازی ذخایر راهبردی در تاریخ این کشور انجام شده است؛ در آن زمان هم ۹.۹ میلیون بشکه از این ذخایر کم شده بود.
🔹
حالا آمارها نشان می‌دهد که ۹.۱ میلیون بشکهٔ دیگر از این ذخایر کم شده و سطح آنها به کمترین میزان در ۴۳ سال گذشته رسیده است.
🔹
ذخایر راهبردی آمریکا با هدف کنترل بحران‌های نفتی ایجاد شده و از زمانی ‌که جو بایدن برای کنترل بازار در زمان جنگ اوکراین از آن برداشت کرد، واشنگتن هنوز نتوانسته این ذخایر را به سطح قابل اطمینان برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/438329" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV2pgoa8L8iB4amJuO2QMeqOijeOALWFHtA-9gi9RAR3Y0LbyRqzKXAIJFNgJ-hiNW_ccYqavk-uLk0HppcGwj74e_2DEpchopCgD8-KvKePNOqz8WzcxxmS52yVAzKrwoZbWrzVy83OJsDl80MLSR8u7HJx_QteqIYusrfdCQAs072845Teg2PvZ3Ai9FpreMSQnA9zomYrC8BGS0hJVSHX7Sdc7EU_xubzIznVCXNO14oo-H9uN-Ux3q1E0QohPNFDcyZI-G-e1GSQP6ZeHbK_CUNnoQIhbS6qCgyMzA1l17oclKCKJ-orHlOwSaJmqrjxfO9DbYWQ_uOpRcDFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام صنایع به تامین حداقل ۴ درصد برق خود از انرژی‌های تجدیدپذیر
🔹
معاون برق و انرژی وزیر نیرو: مشترکان خانگی برق که نسبت به دورهٔ مشابه قبل ۱۰ درصد زیر الگوی تعریف‌شدهٔ وزارت نیرو برق مصرف کنند، تا ۳۰ درصد قبض آنها کاهش پیدا می‌کند.
🔹
همچنین مشترکان برق اگر نیروگاه ۵ کیلوواتی خورشیدی نصب کنند ۲۰ درصد از قبض آنها کاهش پیدا می‌کند و اگر تجهیزات ذخیره‌سازی هم نصب کنند تا ۳۰ درصد از پول پرداختی قبض آنها کم می‌شود.
🔹
در سال جاری بر اساس قانون بهره‌وری تولید، صنایع مکلف شدند حداقل ۴ درصد از برق مورد نیاز خود را از طریق انرژی خورشیدی تامین کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/438328" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzmcCqWGA9dOblFQcG232lVSHcMLVzv46_E_4pSTLnd7qTIY3Qaxzog_tkb1bWtI5ZBk7vn3xEjipuQj5FWEbRU_MyQix4jDo7xu-2ZbIE5Kc78yYhPL8dIdU6TB_RxzX_oyDyTV33E2fj7dqpll3tWDQruMNN1ETMHV_UwxZsPgrZr9EKqgBTGnsxiBZGcbHc3AXie7KRKQAopzveQH6sOXdwj6mDD0F_W-jDx97kTdvUZPRFBuvIu4A7dQdj_8cdx0HyyR_2nCL39lbcJOLGdhbuEtetOIkyJ5kcTpe3osdTX88HofqSGvreClOTfp-mZaxpbFL3HcmWj3zohxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی وزش ‌باد و گردوخاک در تهران
🔹
هواشناسی تهران: امروز در برخی ساعات، وزش ‌باد شدید و گردوخاک به‌ویژه در نیمۀ جنوبی و غربی استان پیش‌بینی می‌شود.
🔹
این شرایط تا جمعه شب نیز در برخی مناطق ادامه دارد و در ارتفاعات استان احتمال رگبار و رعدوبرق پراکنده وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/438327" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک گنبد آهنین رژیم صهیونی را صید کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/438326" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBvRa9T-aBHto9i78p8gl9FbC-wrjsLECERlqvvB0P2kpefFoItGTLGS_JM_eBgDBn7J-3VcxDTeK5F6xeNwuXDkyr0k2P6O0HBHE-OKZPxkkjfmIQ6KjMJFoeXBOpjC8VvqaYLcLzGeBUkhEApq8UbhnUg07cbFwIw6xrzS6x07a0bTXvPsDRnVFyCaaheLfTTIk7lfbP37ecP9DoqdV-EKtEkxYKOb_tR_t8Hguw7wGH9gJX1gcsIM_HMC5QZB3y8eNg1dFwSTVIbqwb5REy-D-3OvjUW5zZJHsvTR76rew4-mJ6AE2danwPt76kLuCJu3FYyqd0UHyQg_4vgxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ جدید وزیر جهاد برای تسویهٔ مطالبات گندم‌کاران
🔹
وزیر جهاد کشاورزی با اشاره به تحویل حدود ۲ میلیون تن گندم به سیلوهای دولتی از ابتدای فصل برداشت، ابراز امیدواری کرد که سازمان هدفمندی یارانه‌ها در روزهای آینده روند تسویهٔ حساب‌ها را آغاز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/438325" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار فرانسوی: موقعیت ایالات متحده در برابر تمام متحدان اروپایی و آسیایی‌اش متزلزل شده است
🔹
پس از جنگ اخیر یک حس آسیب‌پذیری نسبت به ایالات متحده ایجاد شده که وضعیتی نوظهور و بی‌سابقه است؛ جهان تازه پی برد که قدرت بازدارندگی ایران تا چه حد واقعی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/438324" target="_blank">📅 15:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نیروی دریایی سپاه: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/438323" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ اصلی در میدان اقتصاد است
🔹
رئیس‌جمهور در نشست با اعضای اتاق بازرگانی تهران: هرکاری از دست ما بر بیاید انجام می‌دهیم و آماده‌ایم تا تسهیلات را اصلاح کنیم و کمک کنیم شما مبارزه کنید؛ چون اگر شما شکست بخورید مملکت شکست می‌خورد.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/438322" target="_blank">📅 14:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تردد بیش از ۲۲ هزار زائر کربلا از مرز مهران
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: در ۲۴ ساعت گذشته، ۲۲ هزار و ۷۱۲ مسافر و زائر از پایانۀ مرزی مهران تردد کردند؛ تردد زائران بدون مشکل درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/438321" target="_blank">📅 14:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438319">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=Xp6w2Z9dHmDos2qMDOx-lXjIyjMRWptZJpvFrahlMX-fkKYkzSlaZ-_UIfAgXvUbSu1Ar1gBd8CZUKsLBnLZg4NU0J6ERNq3WNNt0tbWJ1wJmgoH8KM_vy8i45HsPaJ_pGaJlnqUPhHcXfPF4PC8atfy5lAGo9UrqMtrFQOi_0q_Se9PvOwd9Z7H1WPed-yOp9TvlXxq7Faj0LlbCXUxBvY0yY-sM4gILKH2eBecNTHB8ybWT4qi3mElM-5VObPjVnbD7j0owWojw2tbHL2jyk9K4eazNIW0ab3tEPBXRwa9Ayj9TU1xEFcRvGzFLYWbn5tmF4yU70FgGJBhYHMQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=Xp6w2Z9dHmDos2qMDOx-lXjIyjMRWptZJpvFrahlMX-fkKYkzSlaZ-_UIfAgXvUbSu1Ar1gBd8CZUKsLBnLZg4NU0J6ERNq3WNNt0tbWJ1wJmgoH8KM_vy8i45HsPaJ_pGaJlnqUPhHcXfPF4PC8atfy5lAGo9UrqMtrFQOi_0q_Se9PvOwd9Z7H1WPed-yOp9TvlXxq7Faj0LlbCXUxBvY0yY-sM4gILKH2eBecNTHB8ybWT4qi3mElM-5VObPjVnbD7j0owWojw2tbHL2jyk9K4eazNIW0ab3tEPBXRwa9Ayj9TU1xEFcRvGzFLYWbn5tmF4yU70FgGJBhYHMQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷ و ۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)  @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/438319" target="_blank">📅 14:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIf4ddhPYt2Oe74-diBLiy-dAz4vzYjvSBuey6NM2WoHt5q93zgQlr_tGKr0olUwJXpL9E8oiLMncobqNTt1oCsjDsFbGJEl_1YCtJZkQy2QN5nTzOp1-Q8j2Hi0HNSdcHVNEI8_TYVdQGaATBJuzq-CyHHpFewdWq943BBIzAL4IM7eryFwwh7GP_NKrI3B1XdBk_-WgAdPckFG4F6e-eSuQJiuhKx5qet9jTy2oOw2P4LTUvjraFPFCDtg1B8GGmd4WsfXTkKnEpBK_t3V9hw_pun8V8GzHxBumLiKyiysCPoLvsTtmth1JYBNpasFu2EwMnCKLoT7bVQ0WrE5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای پزشکیان به سهمیۀ آسیایی باز شد
🔸
سه‌شنبه شب خبری مبنی‌بر ارسال نامه از سوی پرسپولیس به رئیس‌جمهور برای دستور و دخالت در مورد انتخاب سهمیۀ آسیایی منتشر شد.
🔹
امروز سرپرست مدیرعاملی استقلال در شبکۀ ایکس نوشت: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/438318" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیروهای صهیونیستی هدف موشک‌های حزب‌الله شدند
🔹
حزب‌الله: در مقابله با پیشروی ارتش دشمن اسرائیلی به‌سمت شهر زوطر شرقی، آن‌ها را در مسیر رودخانه در شهر زوطر شرقی با شلیک موشک‌ها، گلوله‌های توپخانه و موشک‌های سنگین هدف قرار دادیم.
🔹
نظامیان دشمن پس از مقابلهٔ…</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/438317" target="_blank">📅 14:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px6-czso35Hbxlvw4wvDtQpcTHDqNzKbscBjN3nA-HgRZEWlXdl2G-lg14YaKYRjpo7FuTr84UHRfgwd4S3oNbi8-guaQc7jwR15SkQ5_gVjfQ9cxEEGBjK8MREGd6yhWH1J8Bv71hVizSCupRRuk3WLQtKOBfhT__VGXokSyH9p2Y_r3siB53gxoUf05w3GP07-TXxJfrnonQf0LejQ5N_VVeRF4v1Xx1rgtOWsQzLuA46YeYrq5TuDRtPiRiKFSPZlRmX4cOAG5qLMDZpVYqb-1ndRG6PooZMDm4fCw9D54RxIrUgRP5xoZBW4-eKbcT1tHHaEd2zr_oalSiqfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۰ هزار لیتر سوخت قاچاق در لرستان
🔹
پلیس لرستان: مأموران انتظامی پل‌دختر از یک کامیون تانکردار، ۳۰ هزار لیتر گازوئیل قاچاق کشف کردند.
🔹
خودروی حامل سوخت توقیف و متهم برای طی مراحل قانونی به مراجع قضایی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/438316" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fcb5a5bf.mp4?token=LT0ENTowFMPS9ynkm99TJBhFcVdYE-o_mUQXAFPlRc9G9hiKqDf_aNFJYGw0cc1YZCeuveR3hgchiH9_AIEU3voFhiVz7DEge6arvkJ5-KwWsImPC7UDQSVDzja6YdCGtHAXdiKCUBQKdQGQsOYMuK69QHoHq_z6AJuWZ3-qGrzfPjaCuoYsBorw7Cg-zFylYJuXBLc0-b_ZalmcxLNARcMxYTtg5DRZkB13TuDGC5SXsq9aPUeoRFBZ_7NZ9fv7FrnhPsH-9pkrXHL8k-yT4sY07ij_m1GXL_zOlsQNPd_p8F2e2O2fZqUAfS8E0lVqloUFallW_KqJ8egBn_WGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fcb5a5bf.mp4?token=LT0ENTowFMPS9ynkm99TJBhFcVdYE-o_mUQXAFPlRc9G9hiKqDf_aNFJYGw0cc1YZCeuveR3hgchiH9_AIEU3voFhiVz7DEge6arvkJ5-KwWsImPC7UDQSVDzja6YdCGtHAXdiKCUBQKdQGQsOYMuK69QHoHq_z6AJuWZ3-qGrzfPjaCuoYsBorw7Cg-zFylYJuXBLc0-b_ZalmcxLNARcMxYTtg5DRZkB13TuDGC5SXsq9aPUeoRFBZ_7NZ9fv7FrnhPsH-9pkrXHL8k-yT4sY07ij_m1GXL_zOlsQNPd_p8F2e2O2fZqUAfS8E0lVqloUFallW_KqJ8egBn_WGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا رسانه‌های ضدایرانی دچار سردرگمی و بی‌برنامگی شدند؟
@Farsna
-
link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/438315" target="_blank">📅 13:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFEh-oMcKqB7d99fsP8gdk90moAYpAzs3Z-htn-iEJdVOCX1ICyEO2K0yxujxQBPjlVObLWaOrD_HI6digIZB0HFlv_X9h9hUs1TKnTI7RjdZ5Frcq8hYpeGSaigsFoI6SmBdryOLhUIskK2QkssTzLteRubodFFuSxtS6PHs3DdUkmuuXT5GaLti4ls0qS5CTCOlcU2OAOV9cX4uLVa0bdygD7PU26e4f87dsYjz3cMC9PfrvUKQjO64yvXzsQjGNqk5paRFngBDQWVMVG9Pb9sZo737FRubF7AJ40tDn6bghjZC0YYr4A0ncKisKHmWcAJQlFQjrjZiGQxBEWKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نقشه‌برداری کشور: دریای خزر کم‌آب شده است
🔹
دریای خزر به‌ویژه در ناحیهٔ شمال آن با کمبود آب مواجه شده و پهنه‌های خشکی در شمال، شرق و غرب خزر مشاهده می‌شود.
🔹
خوشبختانه ایران در جنوب خزر و در عمیق‌ترین بخش آن قرار دارد و عقب‌نشینی آب هنوز به ایران نرسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/438314" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزارت اطلاعات: دشمن پس از شکست در جنگ نظامی، جنگ ترکیبی را تشدید می‌کند
🔹
از ابتدای پیروزی انقلاب تاکنون، ۳ جنگ تحمیلی و چندین کودتای نافرجام به سرکردگی رژیم صهیونیستی و با همراهی آمریکا، انگلیس و برخی کشورهای عربی، علیه ایران طراحی شده که همگی ناکام مانده است.
🔹
با وجود شهادت رهبر، وزیر اطلاعات و جمعی از فرماندهان ارشد، کشور همچنان پایدار و استوار مانده و نیروهای اطلاعاتی ضربات مهلکی به رژیم صهیونیستی وارد کرده‌اند.
🔹
دشمن شکست‌خورده در میدان نظامی، اکنون تمرکز خود را بر جنگ نرم، جنگ شناختی و تحریکات اجتماعی با محوریت فشار اقتصادی، اختلافات قومی و مذهبی، ترور، خرابکاری، قاچاق سلاح و استارلینک، حملات سایبری و فعالیت رسانه‌های معاند معطوف کرده است.
🔹
هرگونه اغتشاش، جاسوسی، ارتباط با رسانه‌های تروریستی و اقدامات تجزیه‌طلبانه با قاطعیت پیگرد قانونی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438313" target="_blank">📅 13:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607552d2f1.mp4?token=Vg0uGiJHdduuGuZ_QOy0O23GBEvYIJ593nihOy1btroolBwyESXTsZCUNCBvB53qQCGzu_gQ2ql1gvRTKhehLGh71hB2EP0dEezK1uePbLo386TdNlaw-x0VF4s-g6bo1QO5nH54LQxOnQEgVgaCUy7el48aCYI8IfRwGKtX-pWASLCp1QiINirYYxreOSxijtiz4wpEsvqbdEzyRzi7T_7Awx-FyzSc_3sVQQY8INMd8qTMGdJI3BFhMfw-BMfLVZ4QP8Gy2brCjCcDdux2nJxNq6A63LXxjwdNBcmce92eXQfgA7OsNgCDmNuuBTGcJ1I0JoL1V_3vIDyR3GFBKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607552d2f1.mp4?token=Vg0uGiJHdduuGuZ_QOy0O23GBEvYIJ593nihOy1btroolBwyESXTsZCUNCBvB53qQCGzu_gQ2ql1gvRTKhehLGh71hB2EP0dEezK1uePbLo386TdNlaw-x0VF4s-g6bo1QO5nH54LQxOnQEgVgaCUy7el48aCYI8IfRwGKtX-pWASLCp1QiINirYYxreOSxijtiz4wpEsvqbdEzyRzi7T_7Awx-FyzSc_3sVQQY8INMd8qTMGdJI3BFhMfw-BMfLVZ4QP8Gy2brCjCcDdux2nJxNq6A63LXxjwdNBcmce92eXQfgA7OsNgCDmNuuBTGcJ1I0JoL1V_3vIDyR3GFBKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ فرزند شهید تنگسیری از روزهای منتهی به شهادت پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/438312" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_MBxzCdpTz8pxsJoQA96U3ioahp2v41a18jzFAAG7_8IeJyJbJR-FnnDyGoZURC6I-ykuo6axdfLjqd6hZe_yr7-ThkflWa_oHGvt2orLx2i3zub4Jl5xjt9vUvnQAbiHqF47Fkmr8A7Z6hZb8Gku47gV3nuVHr3yqZsEx2M7cRMOv2hBTlJaQ17B1wXIHuEByh1kTqYmjkh_f1H9w56SWCKKlfkfT8QjPW_BcalV8fhNiovJ5IKxKtjXGrOSoW5E8Asw_5_nv9AB3x5U3dSE5FHQb6Ju3DFpcMTjWHSqN432E3sBKLP3lOLtbTXMFWbmB2Ryo09TgT9Pfg8zK15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهادت فرمانده ارشد کتائب القسام تایید شد
🔹
جنبش مقاومت اسلامی حماس رسما شهادت «محمد عوده» را تایید و لحظاتی پیش، طی بیانیه‌ای اعلام کرد: در سوگ شهید قسامی، فرمانده بزرگ مجاهد محمد عوده (ابوعمرو) که استوار و سرافراز در میدان‌های جهاد به فیض شهادت نائل آمد، نشسته‌ایم.
🔹
شهدای این حمله پنج نفر اعلام شدند. محمد عوده، معروف به ابوعمرو، همسر او، ام‌عمرو و یاسر، یحیی و جمیله فرزندان آنها.
🔹
محمد عوده از فرماندهان ارشد کتائب القسام بود که از او به عنوان مرد در سایه نام برده می‌شد و پس از شهادت عزالدین حداد، فرمانده کل کتائب القسام، از بالاترین فرماندهان این کتائب به شمار می‌رفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/438311" target="_blank">📅 13:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78120c8ea1.mp4?token=jzJo13eYVeZkAxqaxErtFF_SVxJFxPbuVbcddo7zof6DSLx5f6kyNfyvJf_lpNuCdfuLlfiI_-kCb1cx7eQUUDypXMsDyM6n5n0sqJVVJ62WJp19WUTq0umz2PDrcvf5ir6j62EsnolRC81kJD_RDSu-vNJtWgmqXWora43KWJb5M0PLqYKubuSZAxluba7D5viio1JravWV6HoI8jkDQdjb4t87RGQRqsI8Hcjcpftay40lD_tu4vTkFccPlk6XAG997OyuSlgG7NJL9F8qHnxvGvl2xqd6ItQ83YmFykEcqHyr5gmHepf4KSi1lE0l00ZXS3jLALLV_xHu-AGxiF0fkeKo5OdTNxAfnyzMUA1jA-xEBAPJd78w-j4DX68hcZtIXtvVJREk0Cq8NzWntSQyugTDUMhlwney-4AzRfUWAVgFhcRN3ZA3JDXoks0Cm5TshW_K81wKQ-z8WCR9UZisspPNwqb1hcT7usIt3fUnqsyB3imAgRRdsXes-ciJU_f_Tpqw2IeVlZ8y8gcs9ZTRITiXo7lp_tbe1qwzdlroCMk37n4uTyecy0G8fjDM-RFKg2wlB4kdaDEdicqvNxfI9lTBhA455bGnnsUY0aJ89B_3MuSpsNaMuAGcyZUI0zF9rQmPmVONHw5XbXc4YWBUna3MA-cvtjtfAKs4oKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78120c8ea1.mp4?token=jzJo13eYVeZkAxqaxErtFF_SVxJFxPbuVbcddo7zof6DSLx5f6kyNfyvJf_lpNuCdfuLlfiI_-kCb1cx7eQUUDypXMsDyM6n5n0sqJVVJ62WJp19WUTq0umz2PDrcvf5ir6j62EsnolRC81kJD_RDSu-vNJtWgmqXWora43KWJb5M0PLqYKubuSZAxluba7D5viio1JravWV6HoI8jkDQdjb4t87RGQRqsI8Hcjcpftay40lD_tu4vTkFccPlk6XAG997OyuSlgG7NJL9F8qHnxvGvl2xqd6ItQ83YmFykEcqHyr5gmHepf4KSi1lE0l00ZXS3jLALLV_xHu-AGxiF0fkeKo5OdTNxAfnyzMUA1jA-xEBAPJd78w-j4DX68hcZtIXtvVJREk0Cq8NzWntSQyugTDUMhlwney-4AzRfUWAVgFhcRN3ZA3JDXoks0Cm5TshW_K81wKQ-z8WCR9UZisspPNwqb1hcT7usIt3fUnqsyB3imAgRRdsXes-ciJU_f_Tpqw2IeVlZ8y8gcs9ZTRITiXo7lp_tbe1qwzdlroCMk37n4uTyecy0G8fjDM-RFKg2wlB4kdaDEdicqvNxfI9lTBhA455bGnnsUY0aJ89B_3MuSpsNaMuAGcyZUI0zF9rQmPmVONHw5XbXc4YWBUna3MA-cvtjtfAKs4oKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک مصاحبهٔ متفاوت با همراهی یک گوسفند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/438310" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7HupVFETRicJg7D_cXIrcF9fAP6PwScPWiOC2SGTEWotMs13OzjpLudU0i4bODO_K-5r8DHjpZ7XPFq9j7gegvV1anjEZotFe6h5RGN-P8haiEHyRIe26zub9a5Ybr25L-37W8O6w4sSH2X9Lx7oeAW9Abc6qVtb_JOHoU__6wntJsCSLI3JuCQZpBestOD7bvT3lDjib72R6CvpV5q84NVBaO_isTaLJbloPCtgQnn4vsv6ao7WxGTOlqxsXqZTWlxkzSHfS6jNWXvkdKD0YRQ6vovaNSM_1Z-nZU3n4O61f-Sc63hspvAUSm_TlyLjse9pPr5NHQY7GrKrTt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کندوان به‌سمت شمال یک‌طرفه است
🔹
پلیس‌راه مازندران: جادهٔ کندوان در مسیر شمال یک‌طرفه شده است؛ این محدودیت تا زمان تخلیهٔ بار ترافیکی ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/438309" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیروهای صهیونیستی هدف موشک‌های حزب‌الله شدند
🔹
حزب‌الله: در مقابله با پیشروی ارتش دشمن اسرائیلی به‌سمت شهر زوطر شرقی، آن‌ها را در مسیر رودخانه در شهر زوطر شرقی با شلیک موشک‌ها، گلوله‌های توپخانه و موشک‌های سنگین هدف قرار دادیم.
🔹
نظامیان دشمن پس از مقابلهٔ مجاهدان با آن‌ها مجبور به عقب‌نشینی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/438308" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkF2WLKxcd-u0ekqTKmMdUHAPKwemJ88KyMEPC10ieP0miXITJjTA_1uzXm7z8kJ8nvWdTf-SRgI0KNwSgjbW6rF7Fuq-d7TTxGEezM_NDOoshNGFwTsUfHl0Vf3vtmVTbQqo6XYaBLAsLnW6nR8IPTZM8fC6I2u8YtxYbnaBxo7oHpofYckyH9rN71jj29BJ0AavMwK-Cscemd5JKpcGjjB-pzG1wu4TDJu5sKXqAE-i0kUFG78Pgt0nE61L4ukIDiD2aZn0AjYue-Jm48BGnui5EAse8vBULfaZPPEnK6E5Hkg6e3xPuEt9pYpgH0Qf8qTRmcnd88F73clt-YzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان‌وبلوچستان
🔹
هیئتی ویژه از سوی حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به عنوان نخستین مقصد استانی برای قدردانی از ایستادگی و حضور حماسی مردم سیستان‌و بلوچستان در دوران «جنگ تحمیلی سوم» به این استان…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/438307" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTCTM6myT6BIsfizM1oRX3CHlFsLZM8NSY304eZJmEun5YeYC1pQ44F4cGgtbghSdmfGc920b32c5IAKgZiT43q1zJ3czEqZdzN8G68OP4E3oVHXIWLli1udBQyhPoB7ENnx5Nvlk8JNaDfW_N7k5kTiqnm_4uSxbVwD8SIKdXX90aXKSfhf9WN9VKjFD8i9rRLrjEQhiKNWKI8HA_vGxliGFGfJGS4UsW70eBJrQxB1L5CHFQtb3sOtihaNfQwyA7Y2jKifuJPXHs4jMQDO0fiOiF8X0mGdYu3j-m6zHKoGTU7cTfuusN4yv5zO_93sk83YQ4LQp_kIi2TwPn0k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی باقری: موضوع ذخایر اورانیوم در دستور کار مذاکرات نیست
🔹
معاون سیاست خارجی و امنیت بین الملل دبیرخانه شورای عالی امنیت ملی ایران علی باقری که امروز برای شرکت در در چهاردهمین کنفرانس بین‌المللی مقامات بلندپایه امنیتی به روسیه سفر کرده، در حاشیه این نشست و در پاسخ به سؤالی درباره سرنوشت ذخایر اورانیوم غنی‌سازی‌شده ایران، به‌صراحت گفت: «این موضوع در دستور کار مذاکرات نیست.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/438306" target="_blank">📅 12:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e09b5124.mp4?token=t5vSxOUgxt3FOFo-MkouFgVFnHrKrzDdLAyU2lqTa0hVuAMA5rJ1DXFIxkgjL4_2dUi-AVRo1wM6x_cKviAvWNNnyJnDtIpIiQvJmrw1Z97jAg77wz9QXVTPqx8eggD0QH2YnUbbwiLWgJAuw0oo4ZBWOpL9Kq2vo_0v-YfhNluVTrWfBCf1MkDFCNGTGEqJFyni81NV3LPNtRHrK6Q7zxqNhj0xAJUbaSFioiZqDzL_buIsJL5swrnSJ1YBZERNNO5GPODN2Pm74xK2dfiV438KYgTK-KN-mmpZypYMkW_OsUJWuA6EtWyAPnNNTbdAcS4Cpj6yy3WXNwZiK4DTCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e09b5124.mp4?token=t5vSxOUgxt3FOFo-MkouFgVFnHrKrzDdLAyU2lqTa0hVuAMA5rJ1DXFIxkgjL4_2dUi-AVRo1wM6x_cKviAvWNNnyJnDtIpIiQvJmrw1Z97jAg77wz9QXVTPqx8eggD0QH2YnUbbwiLWgJAuw0oo4ZBWOpL9Kq2vo_0v-YfhNluVTrWfBCf1MkDFCNGTGEqJFyni81NV3LPNtRHrK6Q7zxqNhj0xAJUbaSFioiZqDzL_buIsJL5swrnSJ1YBZERNNO5GPODN2Pm74xK2dfiV438KYgTK-KN-mmpZypYMkW_OsUJWuA6EtWyAPnNNTbdAcS4Cpj6yy3WXNwZiK4DTCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی اردوغان در روز عید سعید قربان
🔹
رئیس‌جمهور ترکیه: من معتقدم که نتانیاهوی مستبد انشاء‌الله به‌زودی درسی را که شایستۀ آن است، از مسلمانان جهان، خواهد آموخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/438305" target="_blank">📅 12:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4ScGSCsaUPocpXgvt5EjP3AHaAJKNWu0tiBRlHA3gZJd3NSwlYhwmVcOKCRMLOOF3dt5JPHYF-QBIZEnZxU7DTeDejTEl5xAypjwyC-P7GeoO1H3FheITRLFw0Rc6qWYDmQZN4AAyOlpYXzlyo0OTX8boyyeas0AVEWYAnwetqsvdVp409BWrsGf4RDat8xu7JMprCwrZ-xuwilm8vEyU6RycbcjezGC9KCIiNgG1AoakVtmoMwVA8X7qFfs6LwyJ1dl91c3jQzw75r-TiZLMoBsviiLpfY3_E8q1C6kBOIBr2ytzx2dQcJe60p7XlVcHFHy1Uq6On8FZtWtj9a6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد بیش از ۲۲ هزار زائر کربلا از مرز مهران
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: در ۲۴ ساعت گذشته، ۲۲ هزار و ۷۱۲ مسافر و زائر از پایانۀ مرزی مهران تردد کردند؛ تردد زائران بدون مشکل درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/438304" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbnC4d_F5ZbW6YrxMhV_nEe_5X0tE6KqfJ-_0xfXzdclkIQPyqiVKJCt4-dndmhyR4ORzz6H92Blh45610CX8GxRnHY-9CEYJqWAqyMI4sbqLF6bQqKK2HzDZq7DTqf-jZis6SMavF64jvP7A6tkpLJkFUFCq5217wAMsBqlXhcMwtUioHCSoB6lirthhEMJTj0GVtq4dwlR9zl46wBLnS2lL5e84TpSwl7VGqFL7OaWNtiN_GjwCctPHfI7G0WLVQSNAJFaoQSBHjY0tyAyPPTSgyrNWeBaGtTSSUSLpA7nkmm53u-HVezzFqqbKbkUnjhJcV7on0KnWEsQiCCa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری فاکس‌نیوز: ترامپ به توافق با ایران نیاز دارد
🔹
تارلوف: دونالد ترامپ، بیشتر از یک توافق هسته‌ای به یک توافق برای انتخابات میان‌دوره‌ای نیاز دارد و هر اتفاقی هم که در چند روز آینده بیافتد، باید در همین چارچوب درک کرد.
🔹
دقیقاً به همین دلیل است که او در آستانهٔ آن است که برای حفظ آبروی خود، پول هنگفتی به ایران بدهد؛ آن هم درحالی‌که محبوبیت ترامپ مثل همیشه در پایین‌ترین حد خودش است.
🔹
قیمت بنزین ۴ دلار و ۵۰ سنت شده و کشاورزان ما برای تهیهٔ کود شیمیایی التماس می‌کنند.
🔹
کاملاً روشن است که ایران دیگر تهدیدهای ترامپ را باور نمی‌کند. توییت‌های زیادی زده شده و از زیر کار در رفتن‌های زیادی صورت گرفته است.
🔹
این افتضاحی است که این رئیس‌جمهور نمی‌تواند از آن خلاص شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/438303" target="_blank">📅 11:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg_cpoNx2iNQTDMhy1HTrIu3q8S6HdaFR1X5z2O7QnBLZjHAf9fjuwP-EEZjrqyFeQMIbshmO-ZM8Utkho4Q8JCipgQzlKZLhMorcj7zmrT37gQA9FURUTzgaBF-ReowIOWWV7lgWBvI2Klj5LfCIq38fOi2DNjisXGf6T-tl9fgbABa6H0ScrZGehhBNnfmvDwEngO1Zi38NYk32nDsFzGZO8TPNfSqH4hiUwcz-n67FKcvMeHFtvxQ2MUj3bGMMurgpdqxxBUCHIqcSLMlAm6nTLpF4bGLMZTLMojJ-93B-TGGBzZsmsxr0fr19dC7bmsdtIhu54mDTNJgStSBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب در امور بین‌الملل: ضامن عینی بقای توافق، تنگهٔ هرمز است
🔹
تاریخ گواهی می‌دهد، همهٔ مهاجمانی که با سودای سلطه آمدند، از اسکندر تا چنگیز و ترامپ، همگی در هاضمهٔ تمدن غنی ایران هضم شدند.
🔹
«ملت بودن» اصالتی تمدنی و ریشه‌دار است نه کالایی که با دلار نفتی بتوان خرید و یا اجاره کرد.
🔹
خط قرمز ایران روشن است؛ این بار کاغذها و امضاها تضمین نیستند؛ ضامن عینی بقای توافق، تنگهٔ هرمز است. جغرافیا دروغ نمی‌گوید و قاضیِ نهاییِ عهدنامه روی کاغذ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/438302" target="_blank">📅 11:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f32233.mp4?token=GjgBoYHOrHMDj3k7TdosU5HdQQBbe5XnJNe09dnkyJ8WT2oJfUtkDeCRNntnOCJr-tqiN_zaN8Mw2roN-HDEseasG8mOt5ryDOz_umk_K6DR4hzIuc0_RgXHRmmQuew29ecKYR0fSBPx_wBmty73g-Uh4YLbUp_c2Zg1TP6qvkXIzVx4EunLTEJppWnFsX_dOi9UlsvOlZFrYHYtROLS524RVPmouf2XYXHRTBTNUFuGW7y_MrpU5inK9dWXeOMErcWNNtj_gkHY6Tmn7mEEv0X0DjnPapXL48Vd4Y1Rxs5raJ3aHHdRmdOaa2nHzkQLSHOPnGPyP8S-Ossmux22JFTQy_iNaEuw2doeirHkLo1Xcs5NqxPUR6W5lsBB5iaRNk-P_1kkJNgUS09iPZlexjgv8p182l2L1nYdl-chaLk5HRX1WytMjkUIccugylXlojS2A3Y8AmgfAdKo017lZoHlEoGfc56Z6DGWeAvmOgV5QUf-oxnAJ8GkWkcixpuHvb__UTVgrKeRylcXUu9TOrFgUeq-5ns4yR8wlOlFE9k6fdu9CvHlvqaMlAXFcY5pKdbXkP1ESf_Ho_fdQB6mEeRLtcYu8AMPH5lQq3wkRdlRlFa1cRYgRcjkgxUowTsqdrtuPZsMS-6Eh7vF6MS9hkDN8y_yXyOB2SQamOVdZYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f32233.mp4?token=GjgBoYHOrHMDj3k7TdosU5HdQQBbe5XnJNe09dnkyJ8WT2oJfUtkDeCRNntnOCJr-tqiN_zaN8Mw2roN-HDEseasG8mOt5ryDOz_umk_K6DR4hzIuc0_RgXHRmmQuew29ecKYR0fSBPx_wBmty73g-Uh4YLbUp_c2Zg1TP6qvkXIzVx4EunLTEJppWnFsX_dOi9UlsvOlZFrYHYtROLS524RVPmouf2XYXHRTBTNUFuGW7y_MrpU5inK9dWXeOMErcWNNtj_gkHY6Tmn7mEEv0X0DjnPapXL48Vd4Y1Rxs5raJ3aHHdRmdOaa2nHzkQLSHOPnGPyP8S-Ossmux22JFTQy_iNaEuw2doeirHkLo1Xcs5NqxPUR6W5lsBB5iaRNk-P_1kkJNgUS09iPZlexjgv8p182l2L1nYdl-chaLk5HRX1WytMjkUIccugylXlojS2A3Y8AmgfAdKo017lZoHlEoGfc56Z6DGWeAvmOgV5QUf-oxnAJ8GkWkcixpuHvb__UTVgrKeRylcXUu9TOrFgUeq-5ns4yR8wlOlFE9k6fdu9CvHlvqaMlAXFcY5pKdbXkP1ESf_Ho_fdQB6mEeRLtcYu8AMPH5lQq3wkRdlRlFa1cRYgRcjkgxUowTsqdrtuPZsMS-6Eh7vF6MS9hkDN8y_yXyOB2SQamOVdZYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان نقشه‌برداری: برای نام خلیج‌فارس اسناد ۵ هزار ساله وجود دارد
🔹
واژهٔ جعلی که کشورهای حاشیۀ خلیج‌فارس ایجاد کرده‌اند به سال ۱۹۶۰ بر می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/438301" target="_blank">📅 11:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ed8c99fd.mp4?token=hCXw8vM2Pu4vL5URni7xWDy2NEvWN3AnfpAzBWT3GJsLQqnzAEM9yWH10oq2K04iaWWZXpfGtEGFTHfCcfZrQrd1gf7TeigIEy_SW10aAAt4l24EohM0Q721yzDraZoPiRChT6CwTmhudwja01hrtc_6crnb7vfBO6hUoiANyYMtAvOphNI4x5l09tG_Cr2aJHbXr02_6a1dKSKCAFdQyhJk-oSK0KQIT69h8DfkpWu4jUQOXOpqvFTxo8inHbjdMZGHeCZP21LgTiPAL0ZGUuIpnI0_bkG_Kzva1CV2CTggJsjPZCbVryJFSbJ-PZYT6Tb1WLCpMoJG7NPq_dka-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ed8c99fd.mp4?token=hCXw8vM2Pu4vL5URni7xWDy2NEvWN3AnfpAzBWT3GJsLQqnzAEM9yWH10oq2K04iaWWZXpfGtEGFTHfCcfZrQrd1gf7TeigIEy_SW10aAAt4l24EohM0Q721yzDraZoPiRChT6CwTmhudwja01hrtc_6crnb7vfBO6hUoiANyYMtAvOphNI4x5l09tG_Cr2aJHbXr02_6a1dKSKCAFdQyhJk-oSK0KQIT69h8DfkpWu4jUQOXOpqvFTxo8inHbjdMZGHeCZP21LgTiPAL0ZGUuIpnI0_bkG_Kzva1CV2CTggJsjPZCbVryJFSbJ-PZYT6Tb1WLCpMoJG7NPq_dka-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت جاسوس اوکراینی در مسکو
🔹
ماموران امنیتی فدرال روسیه امروز مردی را که مظنون به جاسوسی و ارائهٔ اطلاعات مربوط به تأسیسات وزارت دفاع روسیه به اوکراین بود، در منطقهٔ ریازان مسکو دستگیر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/438300" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
خاطره شنیدنی از حضور رهبر شهید انقلاب در خانه خانواده شهید آشوری
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438299" target="_blank">📅 11:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b86d6fa10.mp4?token=UkfHf6UO0_Lih5e02rldq5eXge7ZyURA9O5t9fjKNNsjyTLbYsGcP43Wtgh8QCGMue35zATZDOJFzC4nLq4-3ZJ9Oh50GZtduQVGmwRN6UXZTwOMcAOhA6Xo93prX0ynG4z1o5idW8ainldlKfI6VcRkJfT-IKVn76uu7yLjmNRJ4VbTHeRA7L2ElW5zP9KXP3xfGqAXgipnUNVnw8iKdf75wk7JJEHTJP9ZM90sqDX8WzKtC92jShPJGIADI7QuqAg2TQuVAlhdecKH_-79-uLv7FlDc9ERgGtU1F8RQoEQESqjfAQdxZEA_5zYR_wBcwZTL_jZo_Jr4_ivMg1csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b86d6fa10.mp4?token=UkfHf6UO0_Lih5e02rldq5eXge7ZyURA9O5t9fjKNNsjyTLbYsGcP43Wtgh8QCGMue35zATZDOJFzC4nLq4-3ZJ9Oh50GZtduQVGmwRN6UXZTwOMcAOhA6Xo93prX0ynG4z1o5idW8ainldlKfI6VcRkJfT-IKVn76uu7yLjmNRJ4VbTHeRA7L2ElW5zP9KXP3xfGqAXgipnUNVnw8iKdf75wk7JJEHTJP9ZM90sqDX8WzKtC92jShPJGIADI7QuqAg2TQuVAlhdecKH_-79-uLv7FlDc9ERgGtU1F8RQoEQESqjfAQdxZEA_5zYR_wBcwZTL_jZo_Jr4_ivMg1csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دیوان عدالت اداری دستور توقف مصوبهٔ ایجاد ستاد فضای مجازی را صادر کرد
🔹
دیوان عدالت اداری اعلام کرد: در پی طرح شکایاتی دربارهٔ ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» هیئت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438298" target="_blank">📅 10:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G05GMvbSvGPqIkKSF2uciIi8lQzOF0gRx2PncfB6KVw-CKXYc9Z96iswiry1Ps5EO0X1t1N764KmsLXIXvUOvUPAvU3wS3BvDSkNN0IcRppzHfArWS6GwR5czPk5gtqgPw69ko2SNIKMFyejWSYv0NTtcCcjD4SE5AcKqs2NL4P8i4hty7iX65h1q18MwWABezDFM_VremA_pwDMkx3rdt9qed7tpIvhSPw7QQweL4LvhtMSsix5zD1hw6SddpTp0DZ-JLAad9PzjQP8PaejPTiQTH0GkdoWHX_A1jXJuxsM0AG-L3AlV6TEA9Hx1d3JjMPuklkVe8kMu5l5g2uLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از نگاه کاربران بزرگ‌ترین تهدید علیه آزادی در آمریکا
🔹
«توماس مَسی» نماینده جمهوری‌خواه کنگره آمریکا، روز گذشته در یک نظرسنجی در فضای مجازی از کاربران پرسید: «بزرگ‌ترین تهدید علیه آزادی در آمریکا چیست؟»
🔹
بر اساس نتایج منتشرشده، ۸۵.۹ درصد از بیش از ۳۲ هزار شرکت‌کننده در این نظرسنجی، گزینه «اسرائیل» را به‌عنوان بزرگ‌ترین تهدید علیه آزادی در آمریکا انتخاب کردند.
🔹
این نماینده کنگره در ماه‌های اخیر بارها با جنگ آمریکا و اسرائیل علیه ایران و حمایت بی‌قیدوشرط واشنگتن از تل‌آویو مخالفت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/438297" target="_blank">📅 10:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf046f0904.mp4?token=u_bSEb6Vr7KNJ7UYIId1DVqx4LheJwwZLcNnBQtuREs0VbRXC7E5rhH0JRT09Hp-5LjuCeXLjleQaKwvcDVIedr4yMub9VPT0p1bPRFCVGc5yX-jfY9M0M9M8ReiQ0J8XVR0wNtCmzfOLn8vWnbfz53FNxt1TKoovSKajY2PhxP9mVxfyYH7Bwma6FOOx-XV-D5V5XnGpz3ELTYG0cBAJYnuIcCQSElQbE3U8lkF321o68SrAn0MCe4O7dc90CTtYFr_g0zJv_dt5SfLuL1na95GzetbT6kO-be7qWwh67gF6_LWdfe947iYgk2OzONQRYrUVhEf-HSHJoUUpE3Y8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf046f0904.mp4?token=u_bSEb6Vr7KNJ7UYIId1DVqx4LheJwwZLcNnBQtuREs0VbRXC7E5rhH0JRT09Hp-5LjuCeXLjleQaKwvcDVIedr4yMub9VPT0p1bPRFCVGc5yX-jfY9M0M9M8ReiQ0J8XVR0wNtCmzfOLn8vWnbfz53FNxt1TKoovSKajY2PhxP9mVxfyYH7Bwma6FOOx-XV-D5V5XnGpz3ELTYG0cBAJYnuIcCQSElQbE3U8lkF321o68SrAn0MCe4O7dc90CTtYFr_g0zJv_dt5SfLuL1na95GzetbT6kO-be7qWwh67gF6_LWdfe947iYgk2OzONQRYrUVhEf-HSHJoUUpE3Y8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک کشته در حمله جدید آمریکا به قایق در اقیانوس آرام
🔹
در حمله‌ نظامی جدید ایالات متحده به یک قایق در شرق اقیانوس آرام که واشنگتن مدعی است حامل مواد مخدر بوده است، یک نفر جان خود را از دست داد.
🔹
طبق گزارش خبرگزاری آسوشیتدپرس، فرماندهی جنوبی آمریکا (سنتکام) با انتشار ویدئویی در شبکه‌های اجتماعی، لحظه انفجار قایقی را که با سرعت در حال حرکت بود، به نمایش گذاشت. در این ویدئو، قایق ناگهان در میان شعله‌های آتش فرو می‌رود.
🔹
سنتکام در بیانیه‌ای اعلام کرد که «بلافاصله به گارد ساحلی آمریکا اطلاع داده شد تا سامانه جستجو و نجات را برای بازماندگان فعال کند.» با این حال، دو سرنشین دیگر این قایق جان سالم به در بردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/438296" target="_blank">📅 10:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ab109bd.mp4?token=HJQ9MrnwvLEdRdVaCLRdqcLnGBzmKBNzchTaOMyaIQp01OLO7mqHEbhKUspgpDQyWZ01UAcywDsNwTsyK3R4hxrNPtI864kC8qqIj4kG1dr36egBzVn6LAK1TiKci8fx_7sKthUJBGOjTfatAHNXAoKjilfYEA6L_mMY5H6GMJMXhhFtKhiaa-Jc-6x-qpx4nZp8FfVejwP_GwFanvg-KysaAez79QH5tX1U1IdnW4g4ayvXigYf7w0A5w8J4fxCxcXk5scS-EOBL-D2XE6PPfU-33Ch2nu3qcaU1PdN7iYbLvdaMUgPRv1NTa3bIy1TuPEVHwgYjdKzJtq29cRcRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ab109bd.mp4?token=HJQ9MrnwvLEdRdVaCLRdqcLnGBzmKBNzchTaOMyaIQp01OLO7mqHEbhKUspgpDQyWZ01UAcywDsNwTsyK3R4hxrNPtI864kC8qqIj4kG1dr36egBzVn6LAK1TiKci8fx_7sKthUJBGOjTfatAHNXAoKjilfYEA6L_mMY5H6GMJMXhhFtKhiaa-Jc-6x-qpx4nZp8FfVejwP_GwFanvg-KysaAez79QH5tX1U1IdnW4g4ayvXigYf7w0A5w8J4fxCxcXk5scS-EOBL-D2XE6PPfU-33Ch2nu3qcaU1PdN7iYbLvdaMUgPRv1NTa3bIy1TuPEVHwgYjdKzJtq29cRcRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ باشکوه نماز عید قربان در میدان السرایا شهر غزه
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/438295" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b5f96a2b.mp4?token=M6HBJGLUrMRLo3fH2xdnKdcZaTxJ_oS-fcIZT1pC0FvopIsoIn7Ys9ZcM8bKG0sx2KKEh6pjOwpkUIj0WGAlYvsNLRoZDpeJxGYOVpkO1PGEMdtfQuvdiLoofbbJiRrU2qsHR20P6xf7-mHPERmfDIMIZWmu8XG7AwqAaZi8g87irj7qLV1GWjGXljyHEkTYHSAjBHL3PlE-56saJNFYtFQWTqb35Avs1G69G6HQqfyceYcfHRuUg_8rtmsH9wOMyIUSMUkV8YRNZ5oJ69eKBKYlYFXoMoy7DDFJWtsjp_-5K4RYvPVLeSee0w2r2ZZm3_WQNKM7_o-8PL6x7pYB5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b5f96a2b.mp4?token=M6HBJGLUrMRLo3fH2xdnKdcZaTxJ_oS-fcIZT1pC0FvopIsoIn7Ys9ZcM8bKG0sx2KKEh6pjOwpkUIj0WGAlYvsNLRoZDpeJxGYOVpkO1PGEMdtfQuvdiLoofbbJiRrU2qsHR20P6xf7-mHPERmfDIMIZWmu8XG7AwqAaZi8g87irj7qLV1GWjGXljyHEkTYHSAjBHL3PlE-56saJNFYtFQWTqb35Avs1G69G6HQqfyceYcfHRuUg_8rtmsH9wOMyIUSMUkV8YRNZ5oJ69eKBKYlYFXoMoy7DDFJWtsjp_-5K4RYvPVLeSee0w2r2ZZm3_WQNKM7_o-8PL6x7pYB5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجاج به شیطان سنگ زدند
🔹
پس از حضور زائران در عرفات و بیتوته در مشعر، امروز هم‌زمان با روز عیدقربان با حضور در سرزمین منا راهی رمی جمرات شدند تا به شیطان نمادین سنگ بزنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/438294" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4264a298.mp4?token=jqrXRCMnPzvvPAB2exGsvMeAz0gFL8W7eCxDB9V6tfy6cm5l_AtslFoeP9V4II43LgYD1rSfS7KWqNZKhmoDQWqs6FRB_s84A2oDkxC61i-QA5gZBzn2yOB6Z2HLWKiOpPjfG7FHZIvCo5tkPxJFm-UGFuHG3C1IFnxLfxNohfH76dVYzdyC8hq6RfD6enV2CXPkxwr88xfUVX3egdoRddrIevDmol6VhLfE0u3e_giXo7TFv_STa-GFgrYZlb3NeF_uOMGF8cn7Q1NrZmdwPwjLKEKmOPzYa6UkeIW1QSE0QHZWr-37uPjFPLDTfU3QJz_fG4JpMvrVjQGbsVj3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4264a298.mp4?token=jqrXRCMnPzvvPAB2exGsvMeAz0gFL8W7eCxDB9V6tfy6cm5l_AtslFoeP9V4II43LgYD1rSfS7KWqNZKhmoDQWqs6FRB_s84A2oDkxC61i-QA5gZBzn2yOB6Z2HLWKiOpPjfG7FHZIvCo5tkPxJFm-UGFuHG3C1IFnxLfxNohfH76dVYzdyC8hq6RfD6enV2CXPkxwr88xfUVX3egdoRddrIevDmol6VhLfE0u3e_giXo7TFv_STa-GFgrYZlb3NeF_uOMGF8cn7Q1NrZmdwPwjLKEKmOPzYa6UkeIW1QSE0QHZWr-37uPjFPLDTfU3QJz_fG4JpMvrVjQGbsVj3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز عید قربان در بین‌الحرمین برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/438293" target="_blank">📅 09:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0f6c0ec7.mp4?token=UxYcuKL_3ypJZoimbAFk3EPLM3p4z8iiwHH2bJxBu9fGh1-ymay1rL9KjRp86GllO8P3YnlC4Fuq5ZVea5EE9nGkxIsbVEt1ZRhP-919MfHTmQb9EwX4TTP5QNwjJ50DhGwX0wn6VSl1Uic5n-LgPsoosPrCM30YIIN2bPDhl8gNPDznhvxJN9e2KC-JM2KJTSBUEnE6SP99lt6Hr_v14W8g2LUii2rfE2hAlf3XDhujhJ8PSwwLwE72j4ktbuqO_KBipSSkidOnM5kq2ns1CK_ARv-Gn7jPsSqCBzvXkYI61HCVdh0EX_61yMUEb3p51c8iPE7_xO3j7aLVPLaBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0f6c0ec7.mp4?token=UxYcuKL_3ypJZoimbAFk3EPLM3p4z8iiwHH2bJxBu9fGh1-ymay1rL9KjRp86GllO8P3YnlC4Fuq5ZVea5EE9nGkxIsbVEt1ZRhP-919MfHTmQb9EwX4TTP5QNwjJ50DhGwX0wn6VSl1Uic5n-LgPsoosPrCM30YIIN2bPDhl8gNPDznhvxJN9e2KC-JM2KJTSBUEnE6SP99lt6Hr_v14W8g2LUii2rfE2hAlf3XDhujhJ8PSwwLwE72j4ktbuqO_KBipSSkidOnM5kq2ns1CK_ARv-Gn7jPsSqCBzvXkYI61HCVdh0EX_61yMUEb3p51c8iPE7_xO3j7aLVPLaBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ اسرائیل به غزه هنگام جشن‌های عید قربان
🔹
به گزارش راشاتودی، حملهٔ هوایی ارتش رژیم صهیونیستی، یک ساختمان مسکونی در غرب غزه را در بحبوحهٔ جشن‌های عید قربان تخریب کرد.
🔹
به گزارش آناتولی، حملات اسرائیل در آستانهٔ عید قربان منجر به شهادت دست کم ۹ فلسطینی شده است.
🔹
این حملات یک ساختمان مسکونی شامل مغازه‌ها، سقف یک ساختمان مسکونی دیگر در شلوغ‌ترین منطقهٔ تجاری شهر غزه، یک وسیلهٔ نقلیهٔ غیرنظامی و تجمع غیرنظامیان در مرکز و جنوب غزه را هدف قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/438292" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انفجارهای کنترل‌شده تا ساعت ۱۲ در محدودهٔ شرق، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/438291" target="_blank">📅 09:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-qNG86Iviy2Ii7dAJTyN-jnX7hciguRB608LcYHP0tYXLAs8chqaoC9WOhGjdEasab8wqsaiguMjDoSG1gC6eUQ1dt65O9NU42ckwGtWNaalmK2CnkR5FfLADqWF996XmZqW431DSBpmLYcHFdz2in_G5OLZVdBOK2R87VGEQf4FM4RM58wXCjaTKmPuYNNMFHzjFLl7HGLVLndT5c0o_lOjvfKgpwZQQXcwH_sBhom9uLV9Z3Ppg1NqxfDVt3QkIiYXkOjzpdq8OdEFZnkdhFhym_bLZGR-oQ-HQbFu65m9yAPVrfKUpQuuTHLYkG9rrVsF8D74ghdTQN7tqyAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اقامهٔ نماز عید قربان در تهران به امامت آیت‌الله خاتمی  @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/438290" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a2b18b16.mp4?token=ey5Z52QR6ucfvgHpAmobyYdvHVtyG_F5Be5YRaj9_VdevE1P4XBia6wZUOczX350-e0vK3e8K51YnvVM3z1nO9j4mGemUYCSwSYnmD4jRLQzoBNVrxnmo3sFcBTproQ0HVg7b_8QDOYPZsvq3BObYIiQRi8wmnT8_0FCS8SRD_TkB9P07yaQBYRf79QIvyzh6A-LKCT3kiJ-89rZuM3nefoliqX_ZuSURRi39FxEFScD_RLIKC1ZmzU_SzI_DGVqJIYzwr8iBkWzL2Jkj0whj2mSK4g3Bkp4qXlsbgD5T4e5KkAB24EqY0A3clgbdE7c-V7lmRh_NMqioWIJQE0g4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a2b18b16.mp4?token=ey5Z52QR6ucfvgHpAmobyYdvHVtyG_F5Be5YRaj9_VdevE1P4XBia6wZUOczX350-e0vK3e8K51YnvVM3z1nO9j4mGemUYCSwSYnmD4jRLQzoBNVrxnmo3sFcBTproQ0HVg7b_8QDOYPZsvq3BObYIiQRi8wmnT8_0FCS8SRD_TkB9P07yaQBYRf79QIvyzh6A-LKCT3kiJ-89rZuM3nefoliqX_ZuSURRi39FxEFScD_RLIKC1ZmzU_SzI_DGVqJIYzwr8iBkWzL2Jkj0whj2mSK4g3Bkp4qXlsbgD5T4e5KkAB24EqY0A3clgbdE7c-V7lmRh_NMqioWIJQE0g4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز عید قربان در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/438289" target="_blank">📅 09:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM87aabJkMFUFVip1PopsNRxNrBCXwvrXnGhqUaGuIbhM4HmiqZ_Omn0ymA4TmmIvJnP0fZ5QpBBLKd3xRSliAtFpJHIGLGVMIiTySa-B-sdOsCa5vs2lVKyHEhp7AfByDXpJ3P6B0wypYKW8_q0eBbkvcKWnTugH8XJfp--YU8Fqq9IBWTTc2YnHyXDet4hJu2bTTUV3aIc_LwRYRtA2GzwKCOmpESJeOMq8kA0M8JuYsuU8hpRyCgBOdXljx6Eyu_eteGQbpDqdWUE0WnDmAJUlamaHzZWsCFNcnPDigfr8itoSNqvu6ydRbkjm7GyI-vDzbUt9XmbOiiGuR0m8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاریو: از «پیروزی تاریخی» بوی شکست راهبردی بلند شده است
🔹
در حالی که ارتش رژیم صهیونیستی با تبلیغات گسترده رسانه‌ای، عملیات زمینی در لبنان را «پیروزی قریب‌الوقوع» و «تغییری راهبردی» در معادلات منطقه معرفی می‌کرد، اکنون رسانه‌های خود این رژیم به اشتباه بودن این روند، اعتراف دارند.
🔹
روزنامه عبری معاریو امروز چهارشنبه درباره تداوم حضور نظامیان اسرائیلی در باتلاق لبنان، نوشت که آنچه در ابتدا «پیروزی تاریخی بزرگ» به نظر می‌رسید، به بن‌بستی تبدیل شده است که بوی شکست راهبردی از آن به مشام می‌رسد.
🔹
این روزنامه افزود: اقدام زمینی، تغییری راهبردی در واقعیت موجود نیست و چیزی بیش از گسترش میدان «تیراندازی به اردک‌ها» در لبنان نیست.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/438288" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/buGlLD0p9rmJ8AVvi4fg9jgVau-Z90AE4LoxsdRbkgNLfyUgdUcb5YH99R2YM2JAFpTm5ku_xXS-_kphb4ukvZkMmFTYdX0H1bwAkRxqCjIOi3R-nLNcjbxevT4YKsAq3r72oQuhtm60pDBVVGT3kvdL0DIYKfCvwG04nvt9ax0g3vTHwZJTscFGYQdKsUW0OixtPIDGLXSQ9EGkt8Wx1Fw_aqm1xqW5Ok70dfAMSP146estUL5V3aczb-jgbHWaHgTErPf8UMdJH60R7JNADvMqT1mQGUGFqd_T98hCf1KZo45GUSPvyQO-SMfknUfw3viMNpMK7v6wj4xJSFiPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hh_1AQxyQXbmjIsz58N5U5OqCNEUVcZFoADenNL1bcZ0EY4SIVxYb3KJYg4okkfCqchmgt89Tq0a6H_d1lrV3NS4OkCMys2GqLUFNDmmC1WTH-9FuT89w_RW3-IqABgO3kk_fJAgIFpjmnu00vtoEC-KtG_AS5gED1ubPTvw551CA1LvTCAFTwR7Ct2db1HHGa5n7oW4dxL9SNKkSQdLu4M4e4_sfArqH2iKTczcVt7oAFgpNIgH151Ktjm62_O4Si7tby08fTfXyyl2bLPNnrdSwV1xsYFY9r08el3FT57lpPg7ySGIWDQ4khESRLz0hBMNQX-niO9B7YxnF-HBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_ttDgTIaw8vwruWgMVc5rHvqS0Q8pPbtugPFA0CamP6OHqVnZjiTveldXIbYYK03dUfWYE-4fjFP6U8813zUl3mbdUg3cbCqbrxuV5CQ_SNmXFbbWPvb119ATpQHYFz-mfUmS5_CdCAHASJ_PrXrthdOoE4ZMXttb_O3SSRjqRw384om5NIw1JSdRttfYyoNKsuXxkDiJxlke_gDlozfaPTf54ZO-88WmasesSjBXDju_s1Y4RhfiHDfpkhwEWd2TSDKo8jfqFGhYMvJ4xN2EgmXo2q4MDUSrDSeLNdnSRAIa7w2Z98PKSvq8MN2F0ltmwhjR22e8AYL1XHeBKi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or64d5LjwAI2ZeYfn-oiiENSdcUboFWuql6u-TIIDm_HG_2fc9EVs-t_6mnTExxRbWeAAzZTuOruTjoonxuivp5jPVGOF7t4SU9yQG9KOmIQjbo3zWcIhi-SiDev184Bs4Wz7_xMBzyHACPSgvWI2bUZHpxCQDnlv2S5ANPszWhalvl-IC4No8k7mGQGMC5IYmIchFc7Zj5N12vN7bXV3nt_GK9n6Qu7ZFEunRbemyI8oh-a0lkIPV11qYrdNP5Sov44YIzQSqriJdqZgvbpLOXA1tzzdJ_o6MUbgXEjOOJYBWNZkLRMuCYAd1UzPMlhLXWbcup3UUz31qJRKg8rJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMbSMft1rS4Lvl4ic6kooSpvuKNKnRXE1AXPfgN7pQYQkE6U9qOvAcVGUHxuQA19qwZxQHRe5s6cTjfUdBT7bKRmQ_2dGtvuwimjoPY1H1eKdBwmTvFA1htM1_Kcd3BAgtzSFeG-u7LjGPVgYsrjMSY3pXEtWJq_m7h4xN5UOKH4-Mnu4fNHJhPgU6ByBEdjMiMYzJodKkvl9I4ERKBXicA0aLcdfLhGLHoqXQpYPKhLGhU41jPiYn9aa0Vmj5vIT_K_j8sJZugynYrGMmhaZAOoSlF1nQDaol2DERFOzAa-ZgFq3imG1KXGDZwJR3bS1dv_pCEStOPKEFztX3wofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3AGHHU0kA-6JE_RGjK6k7uHaEEp63BK5142-nDVEhRDkTJp332awW26_ojZh-YrTQGMcbvsxYaEhZEmH_oxL8dl0JF8S7aQiXKGR8lKbihxYE65DZ4mEHMn-hIJjzmfgIujEETRxsv1PbSeq84xOkRjK8RHvgVx0etZihrzt4KnOtKo7Gcmj89LbuV_0FAIG4p0N21O6SKenBGefMvbNTgQWVWQqnUSuYXM4LF-kcjBiAK8FqHJRGyQqR6DQ076q3_uuVLZbeChceptm0SowppUtjLourwzregJD_NtCOF7UkyVDtM2A2z8O-zzR2k0vrlvAJrd3Vz8mWpr6AzRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf1HYns5ItGeNEyedb9BnN-gVvOG9NM7Ka2DKV6WXo6OIXhPMaA2ysssRzyt5qniFAZsYKZ0kDrzv8idPLeGY2wrEDuJ7E9s4Kc96NXU5FW2zAqbmgZrDSzAnwzoKxBN2xDYU7DzG3lMRuYZxx64hFfLFnFkiis0zKYwp33TkiZvmUZ5snJRqQ7m3uvOMyvh0t3YzvYSxKIeD09LIllnFVbjLdiCqmI3syL0vXMkSAQt0zvFvscmJ6tGWNkVkdLwdeh4etRaWAwoZSoZyt-r5O1KL4cXLw8BqFEvOrgvS0ic06qp-qwtQN-_PqsjbevHCgTZ-Ior1punPgGRIWXduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLTzPe-nbbhJCJUbp9qFeFtomBktTrYWac-bi0PXeHaQ-D3PRlB1MkAORdPXbGGC5E0Ovauqb24kHvsGJqCsuhBMDG0b7-B5LbZ0-WYptoTzXt4sovRgldKIb4FZeDi-uNUZkYyze3wKH090Y_Zsofn4CCZ5cOpBBiBDg40IyRndIwWmQzVMa8Fme1RRB6ZvHQ8HnHp9ZTFoq5b3wHSsHN367So8XqIzs2lDH2rO4rAmOnNbA_uKmjMLj_rSmLTc3NZNRvfTbRRSCY1uZeHAGImdwslHl4i9_Qer15txY41rrd1Txqu0gCospsS5fAsCdoKrH0TGJhWJGJ6L455Pwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gof9ygHhN4mH-h5nLvQ10X8BG_62qsA5qbY6orEj1oj_5a0P5W1LVhF8YZDrqhaDOon4tcB7t4jaurAEnmK4Hp9L1VOuVpD0v1BmqlKX1U_GHQ2tA9berZIFP_6p6hPBq0sv9W4L_q1Qs3qZPUNH1qism01fdPc84aKyiQf6EBElCQWplac5StC3AikRu6Iy4CWgYWIYsxfHwaVYV3hNZiR9omEsPd6SJy-mn7vkNHKdHVM3elfq-IoEMBIoRSQuBhKmAXOmVUhUs-bUQ0s0J0bZcKq7aJuEr6eKGgn3cJu38PZJ9MbOfQu2CLr5Y_1lP4P-XT-S_ly0fAkyoFSYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FePGmf5RC1_r0jiRBVi20o3iXnSH-_LuIL9RwA2it4aSwGlW6CHjhXezxn6z9cg8giSdAomTHB7ExYoSeodblk3-JY40XB-YSLNo7HhEhJKAklVFURpQ1996VzbF4hwJht08Or05G-PAkeN0vq6eE771F0ufxQ5xa6DWqLuGFz9FmXf0aqiJE99eS0Oq7IdY8-vnaGH2tpBXTFyhLDpUPypwEozVgRiW_RujE5EqvUuQOjNNouqFyg0o54QTjdP3rSaIb1RKMFaaO6-LVbzEq0sUPUecMZQ3ZqDUkHQndvlDe1vFvqEp7DV3zeGoBA5fuDvqzThlqtN818gHCvHI3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کربلای معلی میزبان خیل عظیم زائران در آیین معنوی روز عرفه
عکس:
امیرحسین رستم‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/438278" target="_blank">📅 08:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14e9918b4.mp4?token=o0g_l-ZHJwFWOyhlHpWEf_oFnaivJk1HOirkTXLrA7xVlJHLh2b1Ad-oKsXpA5l960wjZFy1XU5JQvsRQAfO7N_IdECMY-nbcHfABy0CHrB_9Heqoz2cErYu1a1KDMmSLZOcVMOrmu2OltQadEJdwsCwmhImcAurUiCvGsqns5HRmE9jXX3Gr1QOjnkjGZQpBe9skaYF2WXCCLWqrkZjoIBeu9oqRlaU0QbgZx0qtki-dznftLPoP51_2KRwUjt5MEKTys5vj46pNCm63ahT8AKrcBJqIZU3lkWPvPS8OQC_zlIVWj6nITd0a0QX5zuJKPkPhCVkeapKvn142tTbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14e9918b4.mp4?token=o0g_l-ZHJwFWOyhlHpWEf_oFnaivJk1HOirkTXLrA7xVlJHLh2b1Ad-oKsXpA5l960wjZFy1XU5JQvsRQAfO7N_IdECMY-nbcHfABy0CHrB_9Heqoz2cErYu1a1KDMmSLZOcVMOrmu2OltQadEJdwsCwmhImcAurUiCvGsqns5HRmE9jXX3Gr1QOjnkjGZQpBe9skaYF2WXCCLWqrkZjoIBeu9oqRlaU0QbgZx0qtki-dznftLPoP51_2KRwUjt5MEKTys5vj46pNCm63ahT8AKrcBJqIZU3lkWPvPS8OQC_zlIVWj6nITd0a0QX5zuJKPkPhCVkeapKvn142tTbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز عید قربان در تهران به امامت آیت‌الله خاتمی
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/438277" target="_blank">📅 08:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5e17c79e.mp4?token=Y3POOmQ_5F4bHnZExAGUSTRmvH40E3waGumA5i6JidrXSrn4WwowaloX01fak6TZ42G9dRi6skw_dFvJvGnsyrzwpbV3JxgKSztR6ICrVzO0ym-iAVWzTO47ShUbhnTAOl8ezwY3_TsqB_GdwdhtjRMLQ1kmyV9p7flDAOxCxTAavVpU6FpBTpGWxmZJTzOe8RP3tQaQsrfrQeCsNJfllHjAFelS-7IHDcrsC2MF7ghWwWtjcPZSLGL6S1FNyA8zF6XPCwWmNcioOAxmuJ2k1IJFwnqTe91iBxRAbU5emGRm15dj7mPw99YOYGwyBpr-V69gg0JxDQlWQfa5KYdLaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5e17c79e.mp4?token=Y3POOmQ_5F4bHnZExAGUSTRmvH40E3waGumA5i6JidrXSrn4WwowaloX01fak6TZ42G9dRi6skw_dFvJvGnsyrzwpbV3JxgKSztR6ICrVzO0ym-iAVWzTO47ShUbhnTAOl8ezwY3_TsqB_GdwdhtjRMLQ1kmyV9p7flDAOxCxTAavVpU6FpBTpGWxmZJTzOe8RP3tQaQsrfrQeCsNJfllHjAFelS-7IHDcrsC2MF7ghWwWtjcPZSLGL6S1FNyA8zF6XPCwWmNcioOAxmuJ2k1IJFwnqTe91iBxRAbU5emGRm15dj7mPw99YOYGwyBpr-V69gg0JxDQlWQfa5KYdLaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز عید قربان در  مسجد مقدس جمکران اقامه شد
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/438276" target="_blank">📅 08:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438274">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6350bea7d1.mp4?token=Mp0OcwGkCkclv15pruSH8zFpQBDVdxY9XRgAkMLk2S-DN-xhYUkrUFUljJyTuUNuBuvEpluoRvj1nIYyuuT3AYN0TZ5LWq-8QDfw8y4NIgy-nlb-0SFw1Mn4W4On5Fbng6z5Q2eMgqx6DxHYNqKEsnwKrn3xicPQYbuyIURYSYnXiirBKcdjjoL-Ua32TWa2Q16L28KfU4rZG0xoNVTRVVbkYfsnuTyjnsnH5xz6lThdj_qEL51d-Ng7GCLLLdxuKAbRy6NsQlTODUITVKPk6cECKd_6YemApX_HoKzHEZ6050tKy5NnMlMQQRQlywXp0lp9L5CsrLCCBWd93U6JzXxbDc6VDeme7GOy0Sl_A2yXadzJpWMqcdD76LeWVXbRQ4abN_FiT8pChNYXTXIB9iisKjo3hvXVmMClrLtrkUW6Wegp1KYrCU4AT52Bsirpdw_cieHZXR3ki2KyQkZmsFh9yjZCF6nrEk9IFU4TH7Fgqp0vAolDKILNkAJDfN_BvIjfL8_DeLbZ_WPRyf992wIejYmAxUC8S0fejPNSK5sbxJlnV2vCEiOiAtEZugWPKXJCbyzc_7xuFksqDlp8cvn1lfR_CwsUiLgE2OEQDeUqbbZnWZShdmq3lwr5IU9y1oKHjxOD4zjH6xK3V-agyYEslgktKbDDVPn8XAzY8VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6350bea7d1.mp4?token=Mp0OcwGkCkclv15pruSH8zFpQBDVdxY9XRgAkMLk2S-DN-xhYUkrUFUljJyTuUNuBuvEpluoRvj1nIYyuuT3AYN0TZ5LWq-8QDfw8y4NIgy-nlb-0SFw1Mn4W4On5Fbng6z5Q2eMgqx6DxHYNqKEsnwKrn3xicPQYbuyIURYSYnXiirBKcdjjoL-Ua32TWa2Q16L28KfU4rZG0xoNVTRVVbkYfsnuTyjnsnH5xz6lThdj_qEL51d-Ng7GCLLLdxuKAbRy6NsQlTODUITVKPk6cECKd_6YemApX_HoKzHEZ6050tKy5NnMlMQQRQlywXp0lp9L5CsrLCCBWd93U6JzXxbDc6VDeme7GOy0Sl_A2yXadzJpWMqcdD76LeWVXbRQ4abN_FiT8pChNYXTXIB9iisKjo3hvXVmMClrLtrkUW6Wegp1KYrCU4AT52Bsirpdw_cieHZXR3ki2KyQkZmsFh9yjZCF6nrEk9IFU4TH7Fgqp0vAolDKILNkAJDfN_BvIjfL8_DeLbZ_WPRyf992wIejYmAxUC8S0fejPNSK5sbxJlnV2vCEiOiAtEZugWPKXJCbyzc_7xuFksqDlp8cvn1lfR_CwsUiLgE2OEQDeUqbbZnWZShdmq3lwr5IU9y1oKHjxOD4zjH6xK3V-agyYEslgktKbDDVPn8XAzY8VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح تشدید نظارت بر عرضۀ دام زنده و ضوابط بهداشتی ویژۀ عید قربان
🔸
قیمت مصوب تمام‌شدۀ هر کیلو دام زنده در تهران، ۷۴۰ هزار تومان تعیین شده است.
🔹
امروز ۷ جایگاه ثابت و سیار فروش بهداشتی دام زنده در تهران فعال است.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/438274" target="_blank">📅 07:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIIM0tOtIaN0KByysgRhjWgVL-JcIpNXvyg6gH7UqOxt2Os1A6G86FtJ5Ga-26k6q1C-jDDyVOaQIMDzqBoe5888IYKJSdkgNP5QQfImgrllJv4VYWXtA5vLrVkdC-uvphhEDIoIga-nkSgd8BJ7V6Zb-RQ9g8k4S_Eih1QkdH3WFU1iBELNEJY-LautsBhvP47ebJczW6ZFOUpGCic6YM-B2qXHHLa37eRyNzxF2g0tZwM4G_c5qz36kpEP3F0qd-h3yDKhxoJxf0seM3ocPRnaXyTfqcMniRS3X8L6y1wKj70cHjPXaGx4IZCWvppEnS10FVpY6-VqHoRAivD5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD1gbaTfYxjQ1SE4XwnyOi-FwcHHqIZkEgdGegjI6It2byx3dv5laie4g0UWkJcyVhWAqlKQQ4WxlmPfAM7pnFgy65lVNLWFExCU3MSZpSZoO7LOmV3q1kLKeM3XGsI1qPSTkJi_fMQomzBy8Yik4eVe4N-xJR8Ebv1G13AahpZYGY_hhHSmqqUqprdaZZAm5kRdKivDf3lrFF9KLwLkszaoYoZEXM5Nrz-zBGD_l55CuuAaNyOJ33fFfzpnm1UPhCHCKczfz9hJ3OCdCjXerbyg0ujZToj2B5StgL_QYj2Llx2511AVMLXkoNxyiT4rUI1NVBCGKgDVhp6hUgdUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rq0E3nMoCBB3SepHpvyF5am-XTz96D941Fw8hUDxSsX3t-KEJNk4RTQ88Tes9l2OjK_dc5ii9CaOihCo0pRI27s4NXogrOlg73qiVFUl1PU_eMoY9exD5BJeYDwNg5nf0fevB5hnLwQ0r-OZ4AOYRtzxBVyNCDNZMhhY1QsvALyKvBQkoXJUwaeatE-waZxXV4KCDY_kQlOgbnFrY5vD9-_y38tVq9g_5FIGgceK3nGM1o0gr2eO--sp9iTjBI6xWvitoR_SyKUDzvlQeFrOUDFtlKQiitHQWHk8fH-PvFApM_nAYW1PxkyGdrD3ub9k64jJ8Z7pmuNQMepngAYZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyzPA4rJVChNMluVCi5OfVzlaAdLWw5LP519Go2cnA3cRvn1uiOPFz93eKnjvp4RBrCD2mHsf7ajEbjPeuLKqSWwMhGDWiINAvgmDeQrPVXsGmavvHmiJoXjjMfKMT2I_Rs0Nt0MwL1s-BK2vWjAyAQKzwpf0hEULWJQ3o17XWP4dVaBXEgRjswB3lmJm9qus6kSekoMB6QrDYOtkZiINGByE78-GTOmz2vuEUrK22X8V2P87x_Fd8OUQ_pxZmSUzTyryPeQpAgEqKIogdMmDnB1ctWD7JixM1virx42Kf0RiQa3ete36mZMk9oWcNrcAqe2jPRjUz0hm7GBxkAp-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامۀ نماز عید قربان در حرم مطهر حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/438268" target="_blank">📅 07:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa37bce4.mp4?token=VJHKgK19n2IOWqxbdg_tOHnGHQguWYW7HoIfD6DAVagq2hg-CkjJjaFMiN2yWyI4c6gH-k04T54GfyTbn8z95PAl6CMVMdR11Z-D1OA-3evnUwVUiTPeZcGelYE1W72t_hRfuLKKDX6PtWpb5IfWEyisWI9NQTS4qeeUJDqbWhUmI9tAw2tI0I6TUo9cfulOOMDqDJMZU8P1DR_0oGZHOKlskIzmIxwUMFJ8vZzWAo4CWvJ3Yfvn9Y41S8YLcXf3FXm0xeXUDvZbjzAbcoLmouRC_kQyCGTfr586ltIHgwaJqtMWs0ZQOiVVWbuQ-37p98nDMdRYiIsmLOG5MDZwFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa37bce4.mp4?token=VJHKgK19n2IOWqxbdg_tOHnGHQguWYW7HoIfD6DAVagq2hg-CkjJjaFMiN2yWyI4c6gH-k04T54GfyTbn8z95PAl6CMVMdR11Z-D1OA-3evnUwVUiTPeZcGelYE1W72t_hRfuLKKDX6PtWpb5IfWEyisWI9NQTS4qeeUJDqbWhUmI9tAw2tI0I6TUo9cfulOOMDqDJMZU8P1DR_0oGZHOKlskIzmIxwUMFJ8vZzWAo4CWvJ3Yfvn9Y41S8YLcXf3FXm0xeXUDvZbjzAbcoLmouRC_kQyCGTfr586ltIHgwaJqtMWs0ZQOiVVWbuQ-37p98nDMdRYiIsmLOG5MDZwFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز عید قربان در حرم مطهر حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/438267" target="_blank">📅 07:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeVtKzskl8x55ancK-s4rKoRVxYEFodsKYYatkJJG4OzXZIne0PaF0bp8Jern4y3iAwQBnUPgDJXGfbFG8Vpxrbb1mo_Gsx3sp9wk_gEboeJ4C3Xx7H13yf4PiE1oSWeeKpDOYnPy9gWcEgUakN22gbMcuCRZH6EUGuoTHdhWYJvX7c7gd_TZdsY2xxP1snIbY8N4tmMMumyeitq4e86SQgeJMcvGP3txW7NO5DDKUKczpc3GiaJVwmg-dLwT8KDFh4uWNFYqZFU4-oYTsvongcGjcw2FUQE6bPAo4ckXSYGiijgby7B4t4udCbDBSGvJus7D8xucNswa8_buUQMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تنگۀ هرمز را رها کرده است؟
🔹
با پذیرش قواعد و کسب مجوز از نیروی دریایی ایران، بیش از ۲۰۰ فروند کشتی در یک‌هفتۀ گذشته از تنگۀهرمز عبور کرده‌اند.
🔹
درحالی‌که فرماندهی مرکزی آمریکا (سنتکام) اعلام کرده بود کشتی‌هایی که قواعد ایران را بپذیرند حق عبور از محاصرۀ آمریکا را ندارند اما حالا کشتی‌هایی که از تنگه عبور کرده‌اند، یک‌به‌یک به مقاصد خود می‌رسند و کسب اجازه از ایران برای عبور از این آبراه حیاتی به نودمین روز خود نزدیک می‌شود.
🔹
از نظر واقعیت ژئوپلیتیک و توازن قدرت، بسیاری از تحلیلگران غربی پذیرفته‌اند که ایران در عمل به سطحی از کنترل رسیده که بدون هماهنگی یا تحمل ایران، عبور امن از این آبراه بسیار سخت شده است.
🔹
گزارش ویژۀ رویترز تایید می‌کند که ایران با شبکه‌ای از اقدامات میدانی و حتی هزینه‌های عبوری، به‌صورت عملی کنترل تنگۀهرمز را تثبیت کرده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/438266" target="_blank">📅 06:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6aGXLnp0taJ4bMVC1B17QgJuqqyZ0Vn7zLSpTCye8hJixUacin_7vaSfWDPGbNidE4B4CDFzjS4VkUA9YCIMBsrHgy5VzDwQV1KS_xdU1HzipfrWuC9Nt4ITVyoZ_JRmDoAmPFWNF4pKyox4ovfppWAbRoAHmtLRDuXHSIrjGxv5o7_NO95D1_MdMjiQbY-3uhFJyGdiHeKQmfUNFhbcknic71TCZZm5GhH56PxHmPSHTIcikuHaLgOXUy-vRtJexaQCHsymsVa9VX_OaF2-IcOMflHSY0-XAUWj_ZP4Ic0CKW18mGxuowORVaZ_aIn-rJ3B4tYwppPiQh6rV3VrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزخی‌های سردرگم
🔹
حالا که مردم ایران دست در دست هم یک پله بالا آمده و به تعبیر «رهبر شهید» به بعثت رسیده‌اند، برخی از خواص نیز با این جریان همراه شده‌اند؛ اما برخی دیگر، سردرگم در برزخ مانده‌اند؛ برزخی که در آن نه نشانه‌ای از مردم هست و نه غیرِ مردم.
🔹
در این ۸۴ شب، هرکسی با هر هنری که داشت تلاش کرد تا از قطار انقلاب عقب نماند. نقاشان با طرح و قلم‌مو در میان مردم پای کار آمدند. بازیگران و کارگردانان نیز با بلیتی از جنس تئاتر و سینما همراه شدند
🔹
اما در این میان، کسانی هم بودند که در مسیر رسیدن به ایستگاه، خود را گم کردند. آن‌ها در این ۸۴ شب حتی تلاشی نکردند تا به خیابان‌ها بیایند و حرف مردم را بشنوند؛ کسانی که حتی در فضای مجازی نیز به چشم‌های منتظر کودکان میناب واکنشی نشان ندادند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/438265" target="_blank">📅 06:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روسیه اتهام حمله به اهداف غیرنظامی در اوکراین را رد کرد
🔹
سرگئی نچایف، سفیر مسکو در برلین، ادعاهای حمله به اهداف غیرنظامی در اوکراین را بی‌اساس خواند و رد کرد.
🔹
او گفت: نیروهای مسلح روسیه هرگز عامدانه به زیرساخت‌های غیرنظامی، مأموریت‌های دیپلماتیک خارجی، مؤسسات فرهنگی یا دفاتر روزنامه‌نگاری حمله نمی‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/438264" target="_blank">📅 06:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در پایتخت لبنان
🔹
منابع عربی از وقوع انفجارهایی در بیروت و حومۀ آن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/438263" target="_blank">📅 05:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxb1ej1JX6_aC_0AcREWbMGrJ3kLkqccwkLTT_WXvPY7mTpDplEkCmc871JyDIHD0uXzt3GH_mfiVM_v9P7Cuz7Hva1TPWHrLzHpVtU2C08jjlZbdhKQcuG8BPUk6PGQ6elXAR2KKs1VWbPXklVXnYJ7z7udxvrjyNFo1ZhcfN9-pfLhEqPnFI79El15pLlTirQ8zFmv1_X0jWWKHWxbm7VQdTs9Fsmizr8_5GkTN04mPBjbMtdcdbI7u7lhpxItyJZg4jeZ4TILYru_Oipl93aaLsXVgJK-i74mC38S45QJ7-BHGSKGEph4ESynATAdyiwso2RfaH8EOcokhrkhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازها در ۱۰ فرودگاه کشور شبانه‌روزی شد
🔹
با تصمیم سازمان هواپیمایی کشوری، فرودگاه‌های بین‌المللی امام خمینی (ره) و مهرآباد تهران، همچنین فرودگاه‌های ساری، بیرجند، گرگان، بجنورد، کرمان، زاهدان، سبزوار و مشهد از این پس به‌صورت شبانه‌روزی فعالیت خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/438262" target="_blank">📅 05:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJxmmaDpaFTIGmx1DbKixh8wCsnerBl_H2G7hwU2RRo5NCVFiNcpHEiqAI--BMt9VDuA8EQYpoofJtZYAmoaFRXW5j9Oqw5LtADz8VxZkBlsgRfTdFErZfF0athNBtVKzDxbFqkd9wrSW5Kk50yJVv3JT_Etmsb8D1j7o2MH8tfUDlihdSgmzOzNpfwXgP0T1fA7iXnAPrmpC54oYSPyi9w63F6mS66y_CWiqmrLoDpPziQWRVLQrPEw6kJB2UgQW_ocHZAhJZTuEvcVMHm8bR7kbtZqL2IwVDt0DXe9s0JSPwbVeRApvYlgkchnHgz-H8SQKHEu8mw1KkQnPSpuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ واگن ملی امسال وارد خطوط مترو می‌شود
🔹
مدیر عامل شرکت متروی تهران: سال گذشته ۱۴ واگن قطار ملی وارد خطوط ۴ و ۶ مترو شد، که پس از آزمایش‌های مربوطه استاندارهای لازم را به دست آورد.
🔹
امسال نیز ۱۴ واگن قطار جدید وارد خط ۲ و ۴ خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/438261" target="_blank">📅 05:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرودگاه بین‌المللی تبریز بازگشایی شد
🔹
سخنگوی سازمان هواپیمایی: فرودگاه تبریز که در ایام جنگ اخیر مورد حمله قرار گرفته بود، حالا به‌دست متخصصان ایرانی به مدار فعالیت برگشته و چهارشنبه، ۶ خرداد بازگشایی می‌شود.
🔹
این فرودگاه، سومین فرودگاه پرتردد بین‎‌المللی ایران است که به ۹ مقصد خارجی پرواز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/438260" target="_blank">📅 04:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ces2z0sFtAOqbpCnI8tTP_vEMRqjfdc_Ju5AslFkGYM1IUDb8tRtRuZuLJ-8d3iZGzhoc0suZjO-qHl_fko0ASLUxGx5vJDZTNID6XrLp2zVIPXopje271WPK8wOMk0kjPVoxgUv4sUwPc9S8yJt80SCOSoRLxF3HuFhd_1vInFicE4KDtZ5CBP7zEzbZ01rLJjpvp6py58XFfRCImyU0FQcViRLIds7p0-zQ27xBvUHTpEGg2TC3LxLAuMYelePQkPOeCfOI0j_iMvVFBrak5qX0up4uZNf8F8xkNmr6hbhDO7LebSH00HRSSpfYhhhg2bnuXxYSB97N8zKTLOS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از جنوب لبنان به شمال فلسطین اشغالی
🔹
منابع صهیونیستی می‌‌گویند که در پی شلیک موجی از موشک‌ها توسط جنبش مقاومت «حزب‌الله»، آژیرهای هشدار در شهرک‌های صهیونیست‌نشین شمال فلسطین اشغالی فعال شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/438259" target="_blank">📅 04:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
میدان‌داری مشهدی‌ها در شب هشتادوهفتم
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/438258" target="_blank">📅 03:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قطع برق ۱۰۰ اداره در تهران به‌دلیل عدم‌رعایت الگوی مصرف
🔹
مدیرعامل شرکت برق تهران: همۀ ادارات پایتخت به کنتور‌های هوشمند مجهز شده، و مصرف برق آنان رصد مستمر و مدیریت می‌شود.
🔹
طی روز‌های اخیر حدود ۱۰۰ اداره و بانک به‌دلیل رعایت نکردن الگوی مصرف، مشمول محدودیت برق شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/438257" target="_blank">📅 03:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbIVrsobTI_TiRmOI0XdQxfaMBI3MVtXNINiIj5golK4R0O1qtPSOfo09jvQV9FkywUx2MsWsKmX-U4LbMIPLBqIfCSdxlxCqfUmYROcQ1cXOef9AUzFsBcpKJMnzY-VHicWcUPnUH5p8ewB42pme_O8Q4wmbiaMg2i44POFOaFpLVd_uu8vnyg3-pSTF3k66mveWv-GI8g_RI5cvJQrR7gW6dfr_aZ8Ac-iauVnJRQtaoQHG4MSxarLK2DEf3--nHQrTfX8bHp-UrGKPvvWXRN8ozTe_gNLmJTy4XHtiPqXHO1t7P3uqTkzsoLeSX2xf1U-gTkrx6Kb0nYKgzWsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آشفتگی در آمارهای پنتاگون از تلفات نظامیان در جنگ
🔹
تحقیقات اینترسپت نشان می‌دهد که آمار و ارقام ارائه‌شده از سوی پنتاگون درباره تلفات جنگ علیه ایران بدون ارائه هیچ توضیح مشخصی کم و زیاد شده است.
🔹
اینترسپت می‌گوید مقام‌های آمریکایی تاکنون به درخواست این رسانه درباره آشفتگی‌ها در ارائه آمارها پاسخی نداده‌اند.
🔹
این رسانه نوشته که وزارت جنگ آمریکا در حال پنهان کردن آمار نظامیان کشته و زخمی‌شده در جنگ علیه ایران است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/438256" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzR4fuTLLqxruzH4CpZq4QLitmqXwOvenUOimu8uZdzvvnhu5NBpi4B6qwBKQ4wH6ejqJ2S6VnTz39ZMXcBx6ARF7MHzJdYunVBgye0YlQfHMa_EGFSGJiaAItIE1U605dAR3g-esK9vWvs42xVGt3RHuQiBwl4tsEQBbnns27E3qDspi19SHCDSGItg8dhnbeLiaOQe_XeQ-jLRWitszXoRtvedRPrszRg-A8DcsqO-Kt8AvlmYSZaIp_hqeAwdGZX4JwWHRM2823d7bF1-zAeKKCqxYDAorYlqexRYgL6nxoUHp29ah9-7KqlZVlfLfHFg3g5_b7i0SBkx0CI8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشک کروز مجهز به هوش‌مصنوعی در کرۀشمالی
🔹
دولت کرۀشمالی اعلام کرد، روز گذشته سامانۀ موشکی کروز مجهز به هوش‌مصنوعی برای حملات دقیق را آزمایش کرده است.
🔹
این سامانۀ موشکی از ناوبری تطبیقی با ناهمواری‌های زمین برای هدف قرار دادن اهداف تا فاصله ۱۰۰ کیلومتری با دقت «فوق‌العاده» استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438255" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438253">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791f29930.mp4?token=rxqL_CIu5HlbOCzJILWlAdd0XcSGSDi-xBNyzB_qM3n8_P5ktORN4NAbrRqAgIsiHuoLAaWeLIYGkU-Af6yhuAH4_9nvEQZC3GHUpJeLb2ToH1jNE54o0GNkFXcsZCCJ26coBteWQMltK0MkX1HiC1LnBSpl8CXDdcP_5kRRLD36g3MVlkV-QNhLjnTho7Irv_xisy1Z63s0Kz_oO0lNjh9EGo_7b_2UFQp3NnMFtPwe04RmxdLWlmcSvL9O5cZq8yzrs7VdAojR1BJCSaau6Z8a_ywUPaKaSvxcPx_bBzcay4k2-k1eSlc0iz0MqoU-KdHX1Jwf_Bpylgm1_fXW5nvRt3hnMlSOY0BVw0tYo2f8FKc3igpZTeSw-jaS_VutWdIaGBkHSwvn4f0J8TK8WwIcaaKzfpONBSr9vW6fUwAvK7IPb9CkjFZVVQlixw5t7DiwihkohFOr2UkO8GuF5fhZIrq7mrtkUqbhTdeTkpPbMAw3WukrahslfbKI0w892PHp0pKXWCIK03GMUUgjZ2Am_42JajA9Y1x-SaRC91uwKMjuRdYh1KhH9NfiVgF6ha58kdKuGbs4lyrV5SYC0YnRw1q_ZGCZkdjFVkjr8BVq7EO_r2fz3DnCfYo27rKTyg2O_ePI9nhKk358tSff7POOJwaIOCui2Zy4_IyDXG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791f29930.mp4?token=rxqL_CIu5HlbOCzJILWlAdd0XcSGSDi-xBNyzB_qM3n8_P5ktORN4NAbrRqAgIsiHuoLAaWeLIYGkU-Af6yhuAH4_9nvEQZC3GHUpJeLb2ToH1jNE54o0GNkFXcsZCCJ26coBteWQMltK0MkX1HiC1LnBSpl8CXDdcP_5kRRLD36g3MVlkV-QNhLjnTho7Irv_xisy1Z63s0Kz_oO0lNjh9EGo_7b_2UFQp3NnMFtPwe04RmxdLWlmcSvL9O5cZq8yzrs7VdAojR1BJCSaau6Z8a_ywUPaKaSvxcPx_bBzcay4k2-k1eSlc0iz0MqoU-KdHX1Jwf_Bpylgm1_fXW5nvRt3hnMlSOY0BVw0tYo2f8FKc3igpZTeSw-jaS_VutWdIaGBkHSwvn4f0J8TK8WwIcaaKzfpONBSr9vW6fUwAvK7IPb9CkjFZVVQlixw5t7DiwihkohFOr2UkO8GuF5fhZIrq7mrtkUqbhTdeTkpPbMAw3WukrahslfbKI0w892PHp0pKXWCIK03GMUUgjZ2Am_42JajA9Y1x-SaRC91uwKMjuRdYh1KhH9NfiVgF6ha58kdKuGbs4lyrV5SYC0YnRw1q_ZGCZkdjFVkjr8BVq7EO_r2fz3DnCfYo27rKTyg2O_ePI9nhKk358tSff7POOJwaIOCui2Zy4_IyDXG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هشتاد‌وهفتم کرمانی‌ها در میدان اقتدار ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/438253" target="_blank">📅 02:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRqHT7gt6FbrGg6ZF7SPG3aCe4ijJkHlgTVdkDG7LQAKMH94qnHD2KSb3qm37HAj9QL_3P1eYiXn3ca2mjk2BL2JXuXyewYKez6Mllie9lu9JuMkWes0buGn3-UBvJh9MOjvKnsa0-UvMo3JEFti_thBEO5f-btE_QtIbUxg0s9dcOF-TXpGg4cEJi6gw4IrwYa4uJrM9Ht9C-hC8abk-Fcb4RNLErnqWP-9uDC8-5K6-SgbRLo6ZdRzvV2VPUhc4pzbE97Q4Wom_ucX-ZIdPPyOgSvkSjesFN7CJgyCLOK2Pvpx5Lcshl7vO5zI4t-MeYSbZ5HQWfm13GZj7RagxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعه‌بندی گوشت مرغ ممنوع شد
🔹
وزارت جهادکشاورزی از ممنوعیت قطعه‌بندی گوشت مرغ در مراکز غیرقانونی قطعه‌بندی خبر داد، و اعلام کرد محموله‌هایی که در شبکه‌های غیررسمی توزیع و قطعه‌بندی شده‌اند، توقیف و به شبکه‌های رسمی استان‌ها برای عرضه ارسال می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438252" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e4776e5c.mp4?token=kXLQtWnw1tM1SYBRf_yGZ2-rIqMZkC3JshR2ihNrZ8qgyPuzznjP6Ya0m7nf-VB_7kx3oEdAFKekPENfEH-2vZKvG29Y7hswCjDbedaTKUqCuejgpyaQaTBSkr3F6xqrS6bLmoVKxAwIqP61BC-OrkbG0pY13NhRMDZWvVcwy43xSlgOJhesrSSpVPIU5W2lrK5D4BQi3GVlRiJowNiag55iZtF6dsOxX6AccrwL9VRgCqM8VIwVTrn-Sj0yWbXemufaGgrUklc_BcG8OvIQ14bqcZTz-6fcw9U5kGSj-fzmi0iz6Wvdu4Pp236bFtW450xq3hMZYLReKznEEiYjbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e4776e5c.mp4?token=kXLQtWnw1tM1SYBRf_yGZ2-rIqMZkC3JshR2ihNrZ8qgyPuzznjP6Ya0m7nf-VB_7kx3oEdAFKekPENfEH-2vZKvG29Y7hswCjDbedaTKUqCuejgpyaQaTBSkr3F6xqrS6bLmoVKxAwIqP61BC-OrkbG0pY13NhRMDZWvVcwy43xSlgOJhesrSSpVPIU5W2lrK5D4BQi3GVlRiJowNiag55iZtF6dsOxX6AccrwL9VRgCqM8VIwVTrn-Sj0yWbXemufaGgrUklc_BcG8OvIQ14bqcZTz-6fcw9U5kGSj-fzmi0iz6Wvdu4Pp236bFtW450xq3hMZYLReKznEEiYjbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۳۱ شهید و ۴۰ مجروح در حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم صهیونیستی به مناطق مختلفی از جنوب لبنان خبر دادند.
🔹
وزارت بهداشت لبنان اعلام کرد: طی حملات چندساعت اخیر رژیم صهیونیستی به جنوب لبنان، ۳۱ نفر…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438251" target="_blank">📅 02:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
۳۱ شهید و ۴۰ مجروح در حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات هوایی و توپخانه‌ای متعدد ارتش رژیم صهیونیستی به مناطق مختلفی از جنوب لبنان خبر دادند.
🔹
وزارت بهداشت لبنان اعلام کرد: طی حملات چندساعت اخیر رژیم صهیونیستی به جنوب لبنان، ۳۱ نفر شهید و ۴۰ تن زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438250" target="_blank">📅 02:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwSd8mN3bUCLroP2A8cnuwcLIh8-6MBotzkI56G18jDW4QHEZp8h7-qRA0M5RPo9u6ot7KlubxpPw6D5IO3YIzMRB8a7aca8QRKLz5eRGskqEecvnoleuykJ8RiP9Z4uXc2BpeqepAXT1ML17svtGDjo9YUsYhkZVoqp-PRrxacxglgjJ2bGhe2L7cKjw0y5hfMQW6puz-ygMNpuA-HCSrEjgRf92B_QTtpQ6j2SkAs2-Mx9V2NLpryrZWEcBeHs1mKUOyCmLvqfx7s8Neh3-nKa4CO0pDhaib9_LwBMKpseF3SKvbXBJ0RlFA-jl1jp1paHSR29_W9qkD0ddYAojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام مسکن ملی افزایش یافت
🔹
در بیست‌وچهارمین جلسۀ شورای‌عالی مسکن، افزایش سقف تسهیلات مسکن ملی از ۶۵۰ به ۸۵۰ میلیون تومان به تصویب رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438249" target="_blank">📅 01:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ce2af54a.mp4?token=rZIG_-WhL12erGoWNcsMMdIaBSp2Wm76i9taPhKg8mNA9r7cfFXItanpTH3Dl10a0tZxNgGyco0R6ZZNkmTKLlgLEKe4K6Dwv_OzBBcttomP6jXpwrSnrGJnjs9IwoYxO8q-93FZP6gaQTRAIE6RY3KgYq5gZ3n_svpcgxkeCpwMTdhQZNGuDDFWig6jLZlGO0yWxKPql73zDHBn0356832e0LyxKN_HIHRvEUn0OiceffYspcLBGRo1TXTONUFMUOTlKxjV_BrvLZI1JAQHy-G8Pbtg6_pdLbS22Vz5Qd8D8PGXfD_MVUdnmySl-MwfdBUy0Q8HYDtv8f2z-r0XKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ce2af54a.mp4?token=rZIG_-WhL12erGoWNcsMMdIaBSp2Wm76i9taPhKg8mNA9r7cfFXItanpTH3Dl10a0tZxNgGyco0R6ZZNkmTKLlgLEKe4K6Dwv_OzBBcttomP6jXpwrSnrGJnjs9IwoYxO8q-93FZP6gaQTRAIE6RY3KgYq5gZ3n_svpcgxkeCpwMTdhQZNGuDDFWig6jLZlGO0yWxKPql73zDHBn0356832e0LyxKN_HIHRvEUn0OiceffYspcLBGRo1TXTONUFMUOTlKxjV_BrvLZI1JAQHy-G8Pbtg6_pdLbS22Vz5Qd8D8PGXfD_MVUdnmySl-MwfdBUy0Q8HYDtv8f2z-r0XKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار روسیه به کشورهای حاشیۀ خلیج‌فارس دربارۀ پیروی از آمریکا علیه ایران
🔹
نمایندۀ روسیه در سازمان ملل خطاب به کشورهای حاشیۀ خلیج‌فارس: ما مدت‌ها پیش می‌گفتیم که اگر چنین اتفاقی (تجاوز نظامی علیه ایران) بیافتد، چه بخواهید و چه نخواهید، ناگزیر وارد این بحران خواهید شد.
🔹
به آنها می‌گویم، شما گروگان سیاست آمریکا در خاورمیانه هستید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438248" target="_blank">📅 01:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61e8aa2590.mp4?token=pL2gjqL7Qqv-1hj0JdVGiKcKt9EvvQPdkjM3eiQ0ZiAIBuY36bRC04f3UP_D8n1c0F_bHHvDCYRcx3COP1Z4bNzY3xc1Nfn9b1ocprZvGP7mFaBcAWWv0coaYPpzluMRCjTxoW-Za1WQXYLvT5Gs6XvWKJefhYVOdaQ4j9HwCEdvtMglZit9OyFVmkhmerpIIUvoYKvGrJa87_t6l57T3A8j-Z0QHB5C7SivxC1AmxpP3rr-41B6qwCDTNNVj94MBtvShlCmyYwh7gJxFRz_LC7lbb3OEei-OXKQmezXvxNgV1BqZrIR0I-3KgJKUzJNU6vj5F6vev3Izs_FiJYJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61e8aa2590.mp4?token=pL2gjqL7Qqv-1hj0JdVGiKcKt9EvvQPdkjM3eiQ0ZiAIBuY36bRC04f3UP_D8n1c0F_bHHvDCYRcx3COP1Z4bNzY3xc1Nfn9b1ocprZvGP7mFaBcAWWv0coaYPpzluMRCjTxoW-Za1WQXYLvT5Gs6XvWKJefhYVOdaQ4j9HwCEdvtMglZit9OyFVmkhmerpIIUvoYKvGrJa87_t6l57T3A8j-Z0QHB5C7SivxC1AmxpP3rr-41B6qwCDTNNVj94MBtvShlCmyYwh7gJxFRz_LC7lbb3OEei-OXKQmezXvxNgV1BqZrIR0I-3KgJKUzJNU6vj5F6vev3Izs_FiJYJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعقیب‌وگریز پهپاد حزب‌الله با نظامیان صهیونیست
🔹
رسانه‌های رژیم صهیونیستی گزارش دادند، یک پهپاد در شمال فلسطین‌اشغالی سربازی را تعقیب می‌کرده، و سربازان دیگر وحشت‌زده سعی بر پیدا کردن محل آن داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438247" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تشریح فعالیت ناوگان اتوبوسرانی تهران برای مراسم نماز عید قربان
🔹
روابط‌عمومی اتوبوسرانی تهران: خدمات حمل‌ونقلی این شرکت، با تخصیص ناوگان ویژه و تقویت خطوط عبوری منتهی به محل‌های برگزاری مراسم، از ساعت ۵:۳۰ صبح فعال می‌باشد.
🔹
پس از پایان مراسم نیز، شرکت‌کنندگان به مبادی و میادین اصلی سطح شهر، بازگردانده خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438246" target="_blank">📅 01:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQTh-EqtoU5JzoFKYLor2yyM5eWX7d0A7KeEl4lExtC4eHaucW8LxK4ZR63FYwIfpHMhLLjlYvjEhGKov0J4LnINPfU-A2pBLzxHYmCJfoX37JPcMTWN3hVeymS5r0Atl1vDXQRLAMOPnfAQYI6q69i5T8zfHt2pH_72PngnP0DEyY32P6hEe0nBmuPCwiqwBCbHXoHwvFqiueqlvB7pUq_hqcWYn4llXUXmcKetSdy9_eZF7eIshOT8fhlL3-AG5yqrgZBdBds-b_WyK9YGWU-x-FxtK8GdTranjhi7KuDCQQMcUsw97Z9A4iO9cGS8pOnnAWv5C-JCPzpkatEChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مرگبار مواد شیمیایی در آمریکا
🔹
وقوع انفجار در یک کارخانۀ بسته‌بندی در ایالت واشینگتن آمریکا، منجر به کشته‌شدن، و مصدومیت تعدادی نامعلوم با سوختگی شیمیایی شده است.
🔹
به گزارش گاردین، آتش‌نشانی لانگ‌ویو اعلام کرد که این حادثه پس از ترکیدن مخزن محلول شیمیایی «لیکور سفید» که در صنعت کاغذ استفاده می‌شود، رخ داده است.
🔹
به گفتۀ مقامات ایالت، این مجتمع تقریباً ۱۰۰۰ نیرو دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/438245" target="_blank">📅 00:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شکار بزرگ حزب‌الله در روزی که گذشت؛ ۸ خودروی نظامی و ۷ مرکاوا
🔹
حزب‌الله طی سی‌ودو عملیات خود در روز گذشته، علاوه بر حملات راکتی، توپخانه‌ای و پهپادی به محل تجمع نظامیان صهیونیست در جنوب لبنان، از هدف گرفتن ۸ خودروی نظامی و ۷ تانک مرکاوا به‌همراه ساقط کردن دو کوادکوپتر اسرائیلی و انهدام یک سکوی گنبد آهنین خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438244" target="_blank">📅 00:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ_-l0JlIM5T0brFBZxMjYs9I7QGcc2KYytKxS0fMNp8qW82-ovFRRP_ew0-eiDYGm22amej5ucGZRgeWAIev7RjswPwZfP2EvHeGCK36Kmxw1arPdLsz8A-t8RstjcGAobidbm36gfC1c5Dfswhl7dsh6N7gEd43cjflSscheIlgd7oMuqYVRiu05MkBYsLXiLagAAaKdPe_ZoIKN-7ZpsmRvM7mX0nsWHpgJUyF9OMy_MutEkMHMKCyFzFh4i6OQ0qo2i64_NHy9YmvdNJX1z0fM9Myboo5bzk19P_fWrFrXjEAvBSIYzOfIdp4FqJ-2ecmYtSZotTowDoNxl5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهانهٔ اسبی
🔹
شخصی نزد دوستی رفت و از او خواست که اسبش را برای کاری به او امانت بدهد.
🔹
صاحب اسب که تمایلی به این کار نداشت، گفت: «اسب دارم، اما رنگش سیاه است!»
🔹
مرد با تعجب پرسید: «مگر بر اسب سیاه نمی‌توان سوار شد و کار را راه انداخت؟»
🔹
صاحب اسب با صراحت و خون‌سردی پاسخ داد: «وقتی دلم نمی‌خواهد اسبم را به تو بدهم، همین‌قدر بهانه هم کافی است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438241" target="_blank">📅 00:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d45e25a0c.mp4?token=EtURQkFkShVS1Ab56Fht7-9kMLS0xSpRytwhmOk9hw44bWwEtD_eUgcUSVHXh4eSfcBkP9PR8ZHeTjqVRhyf7ZbHMLY5w28YfI1dtifAnhTaWnz0gyc6amTNW6bTasHIuVfolOiBjEkYG4YGtsuaVErRfv6uMEKXMJ2JGl7w0M3C9-Zdhhvm1IXKEGdiy6Eun_u9P4uCTCGxYrz-LTXkD-gU0W-26w36lmb46llstTv2qsQPFGASAyqgNdxlJMhpcRjogVKlkoO8NFZiyxk-lDtFKGA2nGgZoEkVh-k5TAraTrXqLNw_jf8Xw5USv_ZNuWHlzu3gB2SjK7jqeyQMpy2dPRrKhrDOEiJ0h1p1wWWs-l5MnEg6WjfI6rorC_q8IPafgBidy_Qsd2U0Ingc-S60VH_ER3y1kGbJX8TNFY4tp8eWCKJRIamKJNtArW3KbzaG0Y4BrstzzE_VDIK_dEgO_OWv-Ph077iVqDkSedb-XCY5forK2caRKFZmR5zmB2cX39Ec0Eb0IPzNnBX40E7wHtcE0RXUnwnXHjuePqCwNxjXnwid6gqTuGm2PfCPHvjWGGUMnwqtZJ3v_RnG0Pf3rfztx4wnvcUIlvQL6-SnvQYdNts8IxkAi_De3aIy6f3BNWJCsQAoG2wb1ithb7PlzS7XRdl2tEFTcBWQ3So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d45e25a0c.mp4?token=EtURQkFkShVS1Ab56Fht7-9kMLS0xSpRytwhmOk9hw44bWwEtD_eUgcUSVHXh4eSfcBkP9PR8ZHeTjqVRhyf7ZbHMLY5w28YfI1dtifAnhTaWnz0gyc6amTNW6bTasHIuVfolOiBjEkYG4YGtsuaVErRfv6uMEKXMJ2JGl7w0M3C9-Zdhhvm1IXKEGdiy6Eun_u9P4uCTCGxYrz-LTXkD-gU0W-26w36lmb46llstTv2qsQPFGASAyqgNdxlJMhpcRjogVKlkoO8NFZiyxk-lDtFKGA2nGgZoEkVh-k5TAraTrXqLNw_jf8Xw5USv_ZNuWHlzu3gB2SjK7jqeyQMpy2dPRrKhrDOEiJ0h1p1wWWs-l5MnEg6WjfI6rorC_q8IPafgBidy_Qsd2U0Ingc-S60VH_ER3y1kGbJX8TNFY4tp8eWCKJRIamKJNtArW3KbzaG0Y4BrstzzE_VDIK_dEgO_OWv-Ph077iVqDkSedb-XCY5forK2caRKFZmR5zmB2cX39Ec0Eb0IPzNnBX40E7wHtcE0RXUnwnXHjuePqCwNxjXnwid6gqTuGm2PfCPHvjWGGUMnwqtZJ3v_RnG0Pf3rfztx4wnvcUIlvQL6-SnvQYdNts8IxkAi_De3aIy6f3BNWJCsQAoG2wb1ithb7PlzS7XRdl2tEFTcBWQ3So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفاوت شب ۸۷ تجمعات نحن منتقمون کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438240" target="_blank">📅 23:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
موج ۸۷ از ایستادگی بروجردی‌ها در خیابان‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438239" target="_blank">📅 23:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d69293677.mp4?token=E-jFIbCG4jM0K6lmS3blwTZD0X6sTBtzVfm79ktGTkZlfrwL_QQWSaC_KWnqnFmAdUuLkgFia_e8PSqYwkZz80Ho8cvLWWyXgeGjYWqdf_72tihjGVFUeoVNkk9xK9Mktmrksxjgkyd36fhG5GTAXXsqJUHl990Rmo_68HXzf7LtyOYnggOqTv3aRwNUw5cuxQtN7Q7_bDGezmZWOmS15-NIZXlYCK0f02qcpwxb2l6Z6M5fIyewg8fB9qyproW2CY6Xn5wUanXcj_Y1cqQgn_FaHhYZhlbmRMhNu9eOoOO7BiGMktF-aUGAaKDJ3cpE0xbeFI3ESMqEdT5RFyfYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d69293677.mp4?token=E-jFIbCG4jM0K6lmS3blwTZD0X6sTBtzVfm79ktGTkZlfrwL_QQWSaC_KWnqnFmAdUuLkgFia_e8PSqYwkZz80Ho8cvLWWyXgeGjYWqdf_72tihjGVFUeoVNkk9xK9Mktmrksxjgkyd36fhG5GTAXXsqJUHl990Rmo_68HXzf7LtyOYnggOqTv3aRwNUw5cuxQtN7Q7_bDGezmZWOmS15-NIZXlYCK0f02qcpwxb2l6Z6M5fIyewg8fB9qyproW2CY6Xn5wUanXcj_Y1cqQgn_FaHhYZhlbmRMhNu9eOoOO7BiGMktF-aUGAaKDJ3cpE0xbeFI3ESMqEdT5RFyfYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای خواستگاری تلفنی رهبر انقلاب برای پسر یک شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438238" target="_blank">📅 23:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e83c8266.mp4?token=nD77I9zCTnXPn2KQQGgFMf2ky8_58DRv2M1kSZK8Kwdt67h4bFQWp93S3OgKeCYs3ZdS4YVid1nzcLGTflRmVz0jBU0YAhH9E8M_zttCBPNNQhUr2RJtjwUXYUM4t3GQ_IPMs7CII1IwYnBoZOe3ZlCmry4WhpyCoMVxnBXScr--KPcn2g3Z25PbNNXnjIBH26U6hMbxqZCqV4I7DSradlQK8Ou-hHFWw-eeNpD_bMaSGm6IOGnDzXsEpNMyK0ESlOF1SVmrm3a8sDzuyqvR85BGJKHO_jP5O6VIDfhIdUoVdB6REbpWz1y-BnraGLl5znPrEk7O_BpiXVmX4ZfwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e83c8266.mp4?token=nD77I9zCTnXPn2KQQGgFMf2ky8_58DRv2M1kSZK8Kwdt67h4bFQWp93S3OgKeCYs3ZdS4YVid1nzcLGTflRmVz0jBU0YAhH9E8M_zttCBPNNQhUr2RJtjwUXYUM4t3GQ_IPMs7CII1IwYnBoZOe3ZlCmry4WhpyCoMVxnBXScr--KPcn2g3Z25PbNNXnjIBH26U6hMbxqZCqV4I7DSradlQK8Ou-hHFWw-eeNpD_bMaSGm6IOGnDzXsEpNMyK0ESlOF1SVmrm3a8sDzuyqvR85BGJKHO_jP5O6VIDfhIdUoVdB6REbpWz1y-BnraGLl5znPrEk7O_BpiXVmX4ZfwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ الله‌اکبر در جوار رواق کشوردوست در جمع عاشقان رهبر شهید انقلاب رضوان‌الله‌علیه در شب عید قربان.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438237" target="_blank">📅 23:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419cee0e82.mp4?token=GCVm3uO93vDoZUSn4ViqA_rFf6Nvdi2v1ZQ1h223rWQ3JqMh5So0Yi-ixyJwROwpmDyEVKoXhxXPyCWefp9jRIMu_Zi_sN1awUSRZEgQEXvgDwCvlTSy6Q0lTCzhzTWQOReDeO1kuGiQ3ce8tDd11_wF4tqpXZ4z1f0oZXwWk4mugMmohLCQDtDUmH16dAyr7IuHzw95yjGZwMgBWCedGI5-5q2N286u7ce9xKg3BAtV_OPBA1GEYrVxz_KnIqQxpSNrQ_tdxu9InX76E7lZbUNU4N_KXCREtTdEuu6RxeMeET-uVt4NNVs8QCqchP-YHcCQMwIKevaDHc1iiKL0DW01CX97WFvikaCpCDQFFTTclyYRT8AaaIikodTi1rAVo0xqXWfFbhVGcFpw3nIRvfqIZ2_yvpJDQpYcLZuTAyXJelenfdJgLIqI2t91FU8j4V1ZNqxJNbsnR4tUJ3WV5p5Cv4urCa6LIqMLMCQE_zRhIPwl0oDRXqiro6DHZF3Jj9Fe-VM6W_Zkh7cnY97YfQhsc9b52pSVs5tco93IoPEPOBvjYTtyToLoL14qo2EwYBszD18dSJwxbBus26D2tjS2E2LLf47VTBCEmQJQ2CSQJAmX3FXH2LEFVE2PJgPjGhOrA5edS-SZQJSUSLDU-AkwMK6bU0z4Azu_x4h6YxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419cee0e82.mp4?token=GCVm3uO93vDoZUSn4ViqA_rFf6Nvdi2v1ZQ1h223rWQ3JqMh5So0Yi-ixyJwROwpmDyEVKoXhxXPyCWefp9jRIMu_Zi_sN1awUSRZEgQEXvgDwCvlTSy6Q0lTCzhzTWQOReDeO1kuGiQ3ce8tDd11_wF4tqpXZ4z1f0oZXwWk4mugMmohLCQDtDUmH16dAyr7IuHzw95yjGZwMgBWCedGI5-5q2N286u7ce9xKg3BAtV_OPBA1GEYrVxz_KnIqQxpSNrQ_tdxu9InX76E7lZbUNU4N_KXCREtTdEuu6RxeMeET-uVt4NNVs8QCqchP-YHcCQMwIKevaDHc1iiKL0DW01CX97WFvikaCpCDQFFTTclyYRT8AaaIikodTi1rAVo0xqXWfFbhVGcFpw3nIRvfqIZ2_yvpJDQpYcLZuTAyXJelenfdJgLIqI2t91FU8j4V1ZNqxJNbsnR4tUJ3WV5p5Cv4urCa6LIqMLMCQE_zRhIPwl0oDRXqiro6DHZF3Jj9Fe-VM6W_Zkh7cnY97YfQhsc9b52pSVs5tco93IoPEPOBvjYTtyToLoL14qo2EwYBszD18dSJwxbBus26D2tjS2E2LLf47VTBCEmQJQ2CSQJAmX3FXH2LEFVE2PJgPjGhOrA5edS-SZQJSUSLDU-AkwMK6bU0z4Azu_x4h6YxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندرعباسی‌ها امشب مسلح به الله اکبر شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438236" target="_blank">📅 23:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cac6a41c.mp4?token=XTMpDmpotm_Z29nflLiDoOH1mGNdwZuUspxnevQDohffSZiWhhPj6J3vW-vi63P9CzrzBTHTR0cRwIT0HjTCTcpKf2XtduBwuyd_C5Tn_Z47g3ySIEKFDIbNJg_Qj0lXVMn7FxvkIHZlJCKn4hK3YJGU4XAIhRuEP_-0BzLrDt_o0z3rlWjuS7KrIRiAwL1hjgZsv_uN-eZ1-ZENvy2qM8GDead_sToud98ASiVfCy8vRzuaGP6PqOwj-X3jVv1k16_zB-c6Sxv2HRVMsBXEZ45vdCbph0QFBjyZ7A_dh8OiZDxluAPXdbvhoKdAj2IqQY6aidTZsWSjJqqm9_5qvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cac6a41c.mp4?token=XTMpDmpotm_Z29nflLiDoOH1mGNdwZuUspxnevQDohffSZiWhhPj6J3vW-vi63P9CzrzBTHTR0cRwIT0HjTCTcpKf2XtduBwuyd_C5Tn_Z47g3ySIEKFDIbNJg_Qj0lXVMn7FxvkIHZlJCKn4hK3YJGU4XAIhRuEP_-0BzLrDt_o0z3rlWjuS7KrIRiAwL1hjgZsv_uN-eZ1-ZENvy2qM8GDead_sToud98ASiVfCy8vRzuaGP6PqOwj-X3jVv1k16_zB-c6Sxv2HRVMsBXEZ45vdCbph0QFBjyZ7A_dh8OiZDxluAPXdbvhoKdAj2IqQY6aidTZsWSjJqqm9_5qvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری گرگانی‌ها به شب ۸۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438234" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400a0b30cb.mp4?token=qIpUPhQ41Y5CZ8R1kQh4UnrQTef3OAJu1qqu-5GbFEEOAed3K_WEfDBipnA2gMLRttyQWERSFANzpqhVgGuwtTeWFf81r7ifu85eDx8M8xVrpeWy24IMZnfvV-PwreRvaPvNib79QsWGq3ES_O58pRvB2fZnmwvLcRzFvPrFZFKllqC9puAW038vFFj2hI-UV5lWuXq201pIEjJL-IU0oKvi-x_bWN6qd8h-UBSHYfRhulg8ZmD2OyDPrgHiJj_nhdmQ3jjheYONjNX5fFN8_7RMdkyT147Dj_Pf9uRP4FcWKIPzIvH2hiJ-hmqSWfWxo_VL1j-NzKof3pPtEdTNIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400a0b30cb.mp4?token=qIpUPhQ41Y5CZ8R1kQh4UnrQTef3OAJu1qqu-5GbFEEOAed3K_WEfDBipnA2gMLRttyQWERSFANzpqhVgGuwtTeWFf81r7ifu85eDx8M8xVrpeWy24IMZnfvV-PwreRvaPvNib79QsWGq3ES_O58pRvB2fZnmwvLcRzFvPrFZFKllqC9puAW038vFFj2hI-UV5lWuXq201pIEjJL-IU0oKvi-x_bWN6qd8h-UBSHYfRhulg8ZmD2OyDPrgHiJj_nhdmQ3jjheYONjNX5fFN8_7RMdkyT147Dj_Pf9uRP4FcWKIPzIvH2hiJ-hmqSWfWxo_VL1j-NzKof3pPtEdTNIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«الله‌اکبر» در بام ایران
🔹
طنین شعارهای مردم شهرکرد در شب ۸۷ تجمعات ملی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438233" target="_blank">📅 22:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ef25ab28.mp4?token=X4xFJ9jl26iOQhbIVBV0X-nebMWDMUqGnJZrHk_qxazLimgQ_R6Ms5KvlSjOYvSiCIvrRD_zO06UTWI7nQGhfDVLM4nQL1q4VD7B99lzVU0rPW-n9Y5lZ2WyJSL4GEjOWtnLjmnkhSEhrm1FSfEvXOnc-YHK5y2VAKIg4uE05c5AFGZVbTaZxX3lOUfIDPT6xiSwsdW6z9Jvb4F5_Rz2huiLaaevy8pMQMe7xiGfE3Ib1UVj9gRmrHkL9UyLM9xwm1s3jktBPaIWbToRbxzeU74FZSUe0MYmT9tz_TbqmGyl2LkrMeI-2ECWknGDmdt1WT3g2J3tIfxrgYC6AOFDDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ef25ab28.mp4?token=X4xFJ9jl26iOQhbIVBV0X-nebMWDMUqGnJZrHk_qxazLimgQ_R6Ms5KvlSjOYvSiCIvrRD_zO06UTWI7nQGhfDVLM4nQL1q4VD7B99lzVU0rPW-n9Y5lZ2WyJSL4GEjOWtnLjmnkhSEhrm1FSfEvXOnc-YHK5y2VAKIg4uE05c5AFGZVbTaZxX3lOUfIDPT6xiSwsdW6z9Jvb4F5_Rz2huiLaaevy8pMQMe7xiGfE3Ib1UVj9gRmrHkL9UyLM9xwm1s3jktBPaIWbToRbxzeU74FZSUe0MYmT9tz_TbqmGyl2LkrMeI-2ECWknGDmdt1WT3g2J3tIfxrgYC6AOFDDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ رهگیری دوباره یک جنگنده F35 توسط سپاه در بامداد امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438232" target="_blank">📅 22:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1281a6896b.mp4?token=h0Tdnmw7TbZM_EBLPT5AR80Sdf0ba9wZ5x91eqg-4vBONzUSb7-ZPM7uf2hDHkjm4IjnaDoPPph9kh85KltoDD7o3rT8cxBtIolg7t6nyO3D--I5KZ5ZzEbeWKcqdDkfQzrEEEnnHu5olQ2eyFkKKlz6fMY2XbBGwFO9tmzoXa4guA-GmPWVAbFLGa5K0iem9g2eBsMcMqFbufB8La_5oKYcEUdyX9yKPaXPyB8KvVt2M45WB5OxCBvufbAyRztYW7pjNMxXzCE4m5RIn3d-taLndHKScuXeG1OBCR3Tra3VypJY-nXzVPHZTY-8Si7UX4R5h1E74Yc-nW7JXRtZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1281a6896b.mp4?token=h0Tdnmw7TbZM_EBLPT5AR80Sdf0ba9wZ5x91eqg-4vBONzUSb7-ZPM7uf2hDHkjm4IjnaDoPPph9kh85KltoDD7o3rT8cxBtIolg7t6nyO3D--I5KZ5ZzEbeWKcqdDkfQzrEEEnnHu5olQ2eyFkKKlz6fMY2XbBGwFO9tmzoXa4guA-GmPWVAbFLGa5K0iem9g2eBsMcMqFbufB8La_5oKYcEUdyX9yKPaXPyB8KvVt2M45WB5OxCBvufbAyRztYW7pjNMxXzCE4m5RIn3d-taLndHKScuXeG1OBCR3Tra3VypJY-nXzVPHZTY-8Si7UX4R5h1E74Yc-nW7JXRtZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات اولیۀ حملۀ رژیم صهیونی-آمریکایی به مناطق مسکونی لامرد
🔹
در حملۀ رژیم صهیونی-آمریکایی به چند واحد مسکونی و یک سالن ورزشی در شهرستان لامرد در استان فارس ۲۱ نفر به شهادت رسیدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438231" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e134e5633.mp4?token=clQzfwDjwIPVE61PqIZmkDIqMFTeEFPeGv-Vyc-SIJsJbhfne2gzKYKxDwL1FWJhFmY30XDGiCWQEDH7nxubgDWvOtHBqaBL5PDBVWSdXBqRMY2GqD-qsglFZRirtoPccxkPyU1eCO7LT8OGNgDaJhtbPEuvHIINWysGPlfFV9GAizKS85A1Wq82YM-Cm35RUq-N-fXcNLSJLQ5Oa1iswbvGXyBorqip7yOQYPWoQwJg8aMVtxqB2CkDQJxGAUkVYnVJaS6649do7M1lCCrKVWf2OZqKp1a5uooFli0G4UxkqRN3otEGTWOOvp9lewUcmw-ss58VrhquqWlmX7PX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e134e5633.mp4?token=clQzfwDjwIPVE61PqIZmkDIqMFTeEFPeGv-Vyc-SIJsJbhfne2gzKYKxDwL1FWJhFmY30XDGiCWQEDH7nxubgDWvOtHBqaBL5PDBVWSdXBqRMY2GqD-qsglFZRirtoPccxkPyU1eCO7LT8OGNgDaJhtbPEuvHIINWysGPlfFV9GAizKS85A1Wq82YM-Cm35RUq-N-fXcNLSJLQ5Oa1iswbvGXyBorqip7yOQYPWoQwJg8aMVtxqB2CkDQJxGAUkVYnVJaS6649do7M1lCCrKVWf2OZqKp1a5uooFli0G4UxkqRN3otEGTWOOvp9lewUcmw-ss58VrhquqWlmX7PX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: یک پهپاد آمریکایی را سرنگون و پهپاد و جنگندهٔ آمریکایی را فراری دادیم
🔹
ارتش تروریستی آمریکا در ادامهٔ ماجراجویی‌های مداخله‌گرایانه در منطقه و رفتارهای متجاوزانه، در منطقه خلیج فارس وارد حریم هوایی ایران شد و یگان‌های پدافندی سپاه پاسداران در راستای…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438229" target="_blank">📅 22:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
مردم دنیا در مورد مردم ایران چه می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438228" target="_blank">📅 22:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438227" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6-rj1TECp0TDUMiZoVtNywdEVyvuJ_Z-26B5RtWdBhDlML4jwlpuVIaP-uta4jqWCzDqYWoj38kMBokfxxHVXh_vv4G_UGLrTAGfnjBFVL-QaANtuWaf5jhuFD9DuRaTnia1dKRFQ0rq74ilZz-jWwvHkTDoRjOQFs6bci6kiStyJB35j-A2KEKloXRRimuxzuXGJ_Xi5xUCppCSD49wjc26FKGjoGssSkl-W2mywAPhwShzsVJkesg5xlYfeCc7AMubfGmMAQQ_igUBHFWti2T1G6rhlFGbuaaAodlJ8D-ItrxPOmlZ19BgHZDSvtD1ITByV0IaP3sebg4gOg2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔹
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438226" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438225">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عبور ۲۵ کشتی از تنگهٔ هرمز با هماهنگی نیروی دریایی سپاه
🔹
نیروی دریایی سپاه: طی شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز  با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/438225" target="_blank">📅 21:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438224">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">شمس‌الواعظین: وحدت فرماندهی ایران در آکادمی‌های نظامی تدریس خواهد شد
🔹
ماشاالله شمس‌الواعظین عضو شورای اطلاع رسانی دولت گفت: در جریان جنگ ۱۲ روزه علیه ایران، دشمنان گمان می‌کردند ساختار سیاسی ایران متکی به فرد است. با ترور رهبر انقلاب و حلقه اولیه فرماندهان در ساعت ۹:۲۰ صبح، انتظار داشتند تا ساعت ۱۱ صبح کشور کاملاً فرو بریزد.
🔹
برخلاف تصور دشمن، ایران تنها یک تا دو ساعت پس از ضربه اولیه، از جا برخاست و واکنشی ویرانگر علیه نیروهای مهاجم نشان داد. به گفته او، ایران مفهوم «روز دوم جنگ» را به «ساعت دوم جنگ» تبدیل کرد.
🔹
این تجربه که چگونه وحدت فرماندهی و انسجام نهادی در کوتاه‌ترین زمان پس از یک ضربه سنگین در ایران شکل گرفت، به‌زودی در دانشکده‌ها و آکادمی‌های نظامی جهان تدریس خواهد شد.
@Farspolitics
_link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/438224" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438223">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عبور ۲۵ کشتی از تنگهٔ هرمز با هماهنگی نیروی دریایی سپاه
🔹
نیروی دریایی سپاه: طی شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز  با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/438223" target="_blank">📅 21:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlYpQKgH-CcmBwDqdQ7mrFyK_QSH8Ec-gCNxmSS5-nEDh97Yc2W9ktgx7OHBKPtoD6nHRKY7QE97FAyVaRiaDXVZXuBfPU77tfykWekJm-Kt_zKlO24kJzzjg0Eb3wRaFlmkDGgCkh06WeiplwGx0odYnaZ5kaKHQ1uxmPAFs5G56bMz8VEzS7Iw186ksW0mwZH-eE02RSTL78FKCNTjdPBJ4_6Kgw1It2UOZ4O06dTepD3dp06WzY-rmU8wHL1LKOcCMeudl8xPjS_BRF_4XdGRdkGKaxe6sBUCrmZX0nDhFI1j5kF4zIkDWksvQQ6NOH9BnBzObz5QlFPrRMHYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6uqhzWyDl-0RPDJGQPbg44JAe0mvIltVUvkXDiM_lHyC6pcibMvH43AyFYYmnwU580KwVADwqM4CgGDWseZlbuO5DJ1tq2MmwtG7phJc3FzW_o1LYgMvEw8bsZRsoeymqFSmwqhh6j1n-cpr9lgXhYHhAU7GV44HSXABf940-e2_x90NwO0S_KnVQZsHW6QN8h4GU79D-PSOQqtIN3MdfPBsspm68HycT7oGPS5E8L40g2smMVdC9uzAb9-RmSxgTeQnRG1IVLjd3hp5b5NAukli1dB8z8_0Z3NjU1X3dB0qOkFnVIFMNonRIo0DAzMBW2KCzoZ_FAIl1yGUJDo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAW_uTPZoyfSYx6d2-DgHp0m4xjXER29WCkSeJzVul-EKqSBlGGTBYXezeqo3ajJljseDca8lZqP3WrXi1Z0tLCAyXsV9EZgAc2IhdRNhlxEaBL3CSEjRIrfEDTnwMs4oXeCm3uoA2uS7wtWya-rWZJfDgUhus0WOZgA22JJKbHmM2_hcHKvifVQ4EcUt3JUHl_cVYPP4ZWZ8Vadcmsv3GPiOciyOATOnWCiQ9feSPZCE1BOast6EiaR8OXqtIz2Mna-R2sTgoIH_4XQzuOgWlP5kGFgUEtIokBSOmbQ9jb7Drshp4GmeUxxaHzXHc8qawI-4ag7qLTYwULAIX3wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhi72qsBeJ1JytNrs6dkni0qUhvEu3iQWTG4LyIvX23pK-VhPEPQtrDdZx64mm-t6-LyJbTT7UZvG-dblY5p0LaAyD-hH0R-hR2nXIir1wM7J_FHrCwwjfDukaj1OkiJ8mpLQhRZXsiI8c6d85Dh5CW4nZG12I5sOdFyDrAOeaEolHHjazY5SKV8f6J7fmmx-O3rsdx7cD6h6cl1YyLXm16CTYWxvh78-7C-XGdLIiajbd8r2c0aY_UiauOrwX-nx7dS6_mGlhZdjZx7gYWV7vtZFhCdBSZZXzq3rlGOWJrO1wvfuJIRyxI7Q_dPO5MfDsppt40Ob_JU92Jao0Dixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njumMbEF_OMulgCP89GqTxlC0NJ2987ydFfTOWSdn8xRh-QMu8JDDk45TGaNP8KhqO6zLbXGvWCTCxKZPYXxXgjk89nJ5EZ--0oXl4YA56RhZZ7UbIEE7FhpLU7M-rOhy6gx7nPMlFPHfeR-eXXjHkx5ujQcpSog0mIGL-bkHvlHO2CHC1JZDSS5XKSxn57P6n6x1Qivh_hW7baSdpLlKWNfYcduK-Gms9bdTrA9-cfnUp21xtkh78Cf_9VrSWwE6T-lhG_iN0j1mX-__RNrYFAlgeqs00QoFc70zGyGvuUbyTe53lTHRqXBvbglSaqmUGWN7e8NgMCt0FX5AaNcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFjz4j8tNAG_iYBWD2J4AitkSMinYswThxCPeztBL1CyHOr3BhtAFL54bSxCRAMBSXujhySVtGCPSq8I34ZQXmfGpD0W1yfvA9-046U68yJchGc5FEkfR8r2CV1fBmhFOf0w5R8QSATHJRSg46sQd9XinZf6T5qswTUz-c3PosNFJVXHVN6PXq5uh8CttJCL-9SepYGtF_gjB43LIrt-jkNWY1hqJRh_tzk34xxVzK6KHfJfZc4bi-IqsBmlToq8ZC3u_WA7YoqCY1_DPHE29lrtBdYozOiEs4qOZJ4R-jHdPHfzO9uBR43WkW7smmliKolX4SbY_0gdr3v5_-bgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ud3gu__bYfLmBIGCoU-obYX2gUWX9dC9AWEVIvGn0LHYM7UGu997zPQgoqygCT_tvME9led8ixJsK9BrWiqYiAElOL5zqcP_Y1s0GR7Qg4iGGJgg4EBPwgibH_AeiDhPRz7C4gPGJVUsdevK8BZ3a_wVTmp9SS9ylg6VLtbRviOiB5xSIcGiass7KgH7QOKSGikngKAneMqZs-7JJpgKywwFcI3wF4BgniBlhzXx7ZSZhPgV66_e3fqcwELK1V4OqeO8L6O8uLn9i0VBv4DfKj6ogW-Ci9wVmqJJxlznudiip7a-hCj6MivXhoLh_xmW-MorzwW3DgnJyv1-c4ZK6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم دعای عرفه در قزوین
عکس:
میثم‌ملکی
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/438216" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb40dc0aff.mp4?token=T_KzCiiYKj1v4EOWY6NNCcjlEU43zO79zqDDHNJOrRD5pWJYjjB1xAEPN98e63nEf3ImI9kzswVVrOrR5YPw8NyeWY3MBELDP4QaDeGdV9zPV6utAoqQDk17DfaA9ZAfUfu2AoFzKCgZxVPNJt4xsNfMX63hzXQ08JaYngili9zEGQcEt-xr0xPWK82M9pHtuWeb84E6UPZyFI9k6hQiqkNewaxJdHSKwGAWcAt9Rg-sqjJCGwjGnrgEFwIIXY1yKOCqi66h3n6kDKOEAH3MMmgd4516B0-9DNgeWmXSUjnUlci4OmH_FtkOkEHHFVgXdbRfIwS3th-poRlBXRZQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb40dc0aff.mp4?token=T_KzCiiYKj1v4EOWY6NNCcjlEU43zO79zqDDHNJOrRD5pWJYjjB1xAEPN98e63nEf3ImI9kzswVVrOrR5YPw8NyeWY3MBELDP4QaDeGdV9zPV6utAoqQDk17DfaA9ZAfUfu2AoFzKCgZxVPNJt4xsNfMX63hzXQ08JaYngili9zEGQcEt-xr0xPWK82M9pHtuWeb84E6UPZyFI9k6hQiqkNewaxJdHSKwGAWcAt9Rg-sqjJCGwjGnrgEFwIIXY1yKOCqi66h3n6kDKOEAH3MMmgd4516B0-9DNgeWmXSUjnUlci4OmH_FtkOkEHHFVgXdbRfIwS3th-poRlBXRZQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کشورهای منطقه فهمیده‌اند که اگر میزبان پایگاه‌های آمریکا باشند به‌شدت صدمه می‌بینند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/438215" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106bb1fc7c.mp4?token=Qodj7dkFNXkrwtDkatw5FjuL3mU0g2Z-lmH1PX-ojShOANzBYnKLKKee89jN7RJmw6bDRX4v1JQGFy-uOGMVt_jyG4cACb81bs_mctsBqaHD9Za5d4Wb-N5Y1_NHwl8rOWo0ea76m2WRc7kOqmboPQQxOjt-nT_KEf96L_VFAbX_S18_gP6Sq3vxcIQeNxhyoGw7DMk6777ihNrldUtQi6EnRh4XPZlDRBKJfqKiFFPguYPiNejwMongrpOwZCKy0aZm4Dguo29_7jNCDOHBcoGM7b1z8Iam4XJypWxchs_wN6yp3pnHj8aOBGA-f1GKiVl3fJeJnF9MB8-1UbGwPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106bb1fc7c.mp4?token=Qodj7dkFNXkrwtDkatw5FjuL3mU0g2Z-lmH1PX-ojShOANzBYnKLKKee89jN7RJmw6bDRX4v1JQGFy-uOGMVt_jyG4cACb81bs_mctsBqaHD9Za5d4Wb-N5Y1_NHwl8rOWo0ea76m2WRc7kOqmboPQQxOjt-nT_KEf96L_VFAbX_S18_gP6Sq3vxcIQeNxhyoGw7DMk6777ihNrldUtQi6EnRh4XPZlDRBKJfqKiFFPguYPiNejwMongrpOwZCKy0aZm4Dguo29_7jNCDOHBcoGM7b1z8Iam4XJypWxchs_wN6yp3pnHj8aOBGA-f1GKiVl3fJeJnF9MB8-1UbGwPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام کودکان مشهدی به ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/438214" target="_blank">📅 21:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-TxFWJcO7IRnANYV_LhKnunj-taoblveIHlsG_T4Aq-CqOyRP9CEav0B2n36nMysda5onchXtEruAThTNGOvokLtJQ5NkNuNN7yzWZlWsUWw00uihc4u36c6-uWmdkuMaOVuZubhcPc10hsP5-rsz9mqaTJIxRcEINkK3loebBSGrTmSWxcQ9oqMTfl-H1RgPdt5q_Jl2g-ywwtmdFs87LJHwd7htURvfQ0OBpFE8-ilJM8yTDPJi5oM-47265zcYpn-yErg7SudydGGA2oFI13ysfQLBZv_njpk2XCgcEj2EfZlnDPARj-J67m94AWFJFlBx9vP0yK_U8qGAIywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: در گفت‌وگو با رهبران ۸ کشور مسلمان اظهار امیدواری کردم که خداوند قلوب ما مسلمانان را به‌هم نزدیک‌تر کند و شاهد گسترش همکاری‌ها در همهٔ عرصه‌ها و حمایت همه‌جانبه از هم در مقابل تهدیدها باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/438212" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbac7ff3b2.mp4?token=eLS21nZ06JzRIh7uD6w9Kcrrd2aiq2WJNEVQ6CJWR9ooGXI8uJ9TObj8w6ElRE8LP2Y7SVXv0BBueFhOXmPJU2gNUv19ZImJjJ4BRTNcIjj3TUsufPek19qvb5MNjwIQrbT26HBk3fS61JTarc6cwhn-njC4dh9PQ9utStHAnRLuk9xir_RZCFfvvKCABGItcM1aOij1o7Osx6ZUx5IJium3Iks3tfVD3N3uB1H1ldNDxOEpQUXwXFpxElTgkYisxZUqojd4UwJdyrNFTWuBmSL5XlObaOh7svBD1sZhh8UqUgcIApcWkemkeDTr293CvW43177baUzaip2vt5EmUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbac7ff3b2.mp4?token=eLS21nZ06JzRIh7uD6w9Kcrrd2aiq2WJNEVQ6CJWR9ooGXI8uJ9TObj8w6ElRE8LP2Y7SVXv0BBueFhOXmPJU2gNUv19ZImJjJ4BRTNcIjj3TUsufPek19qvb5MNjwIQrbT26HBk3fS61JTarc6cwhn-njC4dh9PQ9utStHAnRLuk9xir_RZCFfvvKCABGItcM1aOij1o7Osx6ZUx5IJium3Iks3tfVD3N3uB1H1ldNDxOEpQUXwXFpxElTgkYisxZUqojd4UwJdyrNFTWuBmSL5XlObaOh7svBD1sZhh8UqUgcIApcWkemkeDTr293CvW43177baUzaip2vt5EmUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحقیر وزیر خارجهٔ ترامپ در هند
🔹
به گزارش اسپرینتر پرس، هیچ مقام دولتی هندی برای استقبال از مارکو روبیو در فرودگاه دهلی‌نو حاضر نبود و تنها فرمانده هواپیمای شخصی‌اش به پیشواز او آمد.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/438211" target="_blank">📅 21:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82dcfef5b1.mp4?token=aaEt6FRBOTTXnoYiPj1dEK32Lpa8lVYiC4AfmQiIHdCHymtmo6WnT2e_1wUZfL28Plkoh1tToL262sUqH7aJbVdl9nyeYR5plM-i1Tme1aXz5l--0tP7km-Z4H9Cf1Xn6eogbH8VLFnwf4wKT5pKJygLWHJ8MNAGjk-hO0O5TK7NAfDKTERsdDsR-FQx-1Lq758lJzt1L642JKWmDT2CwyH0eZh3BACcWihl-jPtuhdFRlavrOg-IqiN5BRKNhiapTbB7ck9C1dcEsTuXdkeNxIULB5SeGn-302FFDOr4jR6svNjlBVNsRQVYT3JySJQUcW_9cnH6qAYJuDLspYuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82dcfef5b1.mp4?token=aaEt6FRBOTTXnoYiPj1dEK32Lpa8lVYiC4AfmQiIHdCHymtmo6WnT2e_1wUZfL28Plkoh1tToL262sUqH7aJbVdl9nyeYR5plM-i1Tme1aXz5l--0tP7km-Z4H9Cf1Xn6eogbH8VLFnwf4wKT5pKJygLWHJ8MNAGjk-hO0O5TK7NAfDKTERsdDsR-FQx-1Lq758lJzt1L642JKWmDT2CwyH0eZh3BACcWihl-jPtuhdFRlavrOg-IqiN5BRKNhiapTbB7ck9C1dcEsTuXdkeNxIULB5SeGn-302FFDOr4jR6svNjlBVNsRQVYT3JySJQUcW_9cnH6qAYJuDLspYuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار یک خودرو در حیفا
🔹
منابع عبری از آتش‌‌گرفتن و انفجار یک خودرو در منطقهٔ «اور عقیبا» در حیفا خبر می‌دهند. یک جسد از درون خودرو کشف شده و هویت او هنوز معلوم نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/438210" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8fb760f2.mp4?token=r8lsCjqqG6JsgPexcT5juY0F_0euhNw4UW6iAFPJW-i60Q2WMR_EFBCrGQZ1Rgt4lBNmWXJWGVDI122fzTNC_DbUEF_urAOa-Ig4U_NvrftODWn9CMGMyPEafwPeYzmCrj-9c7hgmluHaYItxJcP8jsbaMzl3JTxWM1jae4_1YULg6kWYAtbm0WLTWH3sgU_Wupq8Tt1v0exNGLJhvdY35qqYt8Kj5UYGyFJsW0akSXbItBx48wEHhFQBov2CMo02akEBlvQHZUYUlLQBtCPwO1fUwx_74Lu6VPjQ7QbQQ44m92R35gOx52H365cUDYl-zu1PWQeJgTg0kB3MzrwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8fb760f2.mp4?token=r8lsCjqqG6JsgPexcT5juY0F_0euhNw4UW6iAFPJW-i60Q2WMR_EFBCrGQZ1Rgt4lBNmWXJWGVDI122fzTNC_DbUEF_urAOa-Ig4U_NvrftODWn9CMGMyPEafwPeYzmCrj-9c7hgmluHaYItxJcP8jsbaMzl3JTxWM1jae4_1YULg6kWYAtbm0WLTWH3sgU_Wupq8Tt1v0exNGLJhvdY35qqYt8Kj5UYGyFJsW0akSXbItBx48wEHhFQBov2CMo02akEBlvQHZUYUlLQBtCPwO1fUwx_74Lu6VPjQ7QbQQ44m92R35gOx52H365cUDYl-zu1PWQeJgTg0kB3MzrwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور و انرژی پرواز همای هنگام خواندن سرود تیم ملی  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/438209" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
