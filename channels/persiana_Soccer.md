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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 04:59:13</div>
<hr>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b512fOGI-5V7KbPwI72KeBdgI-u-VWldwKSUuXmHcjqbL_MXPNLg-P7wB_LJgDjn44qpYSo_R7lSWan6hvqQc4GnbqBsexfmo9w4zxZ7XLdmT1ZOXL-HzktSq_HOulvdcZ8keIEntM97lxQxugTjRYLRgWmMT37rp7FEpLrvntArAs4hgyOilAvltbe71Om5Jr-VfeVb6YrjMsY9KCSxq5dEz4gO3RJDiNfShr2BUo1uJr9OIZ1TvEhleaH0f16tbwodpWLYOJwSfI79gezKIyAiPNXgt2_gHaEcQ9Tk8HQuQEog0KGDwz6IEWO6fU9hgc8Au1OAzTeDBkSAP6m_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oem9qpJOtXsdSezFGb1gw2DJXjfo-xTc4HGH_Ot7rODoD3hDquVFPUT38cR3uqQi0MGa3Et7sgyh4e9kIG1VZQMVpM3NCIR9J5Cgj1etlj5_AJXYY9ZEwmcDW1dbs508ih0SGrdQQQYbqC3OeNwpJfT_Q6zvVnOWxW6U2c0ywUFkFDpmUyYUGQR8wTr7WmzDDOdnXLc36DkbFjdO0QvoudZRUxDHWhx3e1HjOQ3t8mV904Jmisx8iGsG9gfVDnCl_rkjklt_neTCpVsqI7x3czgrtrl7wJwz6aSrxkeovmH6W6iWAorZ8UZpXcav3zwBD9laj1DqMVJObi2TiGUlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpxoPMK5xe93eWcMpICWYARTqa73n8hxxVpaL5QRu96qAjDP4LEQ5thHCcxKhFjmTBwngrrAyH9nEl2ATQKa7PYMe8NWGnkKqn77D0IgcqQDMS3vElkMrQjrdUsPhwA1tS18bXek5urmolJ_3QNaJBeuk59C-C0fhSvFV_1KqoJez7__4O6Vu6oosv5q5sdDsVpbxT2EPv3_LsOLZT-f4KPBldV40aJn70FBTHvECAcNVqs5Hc5Vkub-Sg5ShaU-qBEc5a5iBw0o7SoqUSa0N8GcfSWrz3zfG_Q82JR5XSgeQWMyjA5mVEbFayNQA0GdzxQ-ZGfhApXfRYFRWviZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJQ34acsS189yaWTHx1mOYY5gJbhu5nxxHGQ1NDsFAeqzLCgK99lNjcZgz0jeIep-xdg8cxT-XWrvt4CTOCwHlZqHL0SWDwLaWEedMpoBb_krfX9Z-_QGG2E5QqjVihbxg3GKt9Se844HUknXYjfBekDwdkRjRw2HxhsNIyIVTHotR59NQgwneP2gE6DhNxl5dUN19nugel_gF4afNhuV2f3VloYt-lxqIeXTkcksGeunV4j_SFkNscHuBTO0HDl8U7p53_ktmxyD8f6XDnNTywFnbKeCyVBa6su-ff-V3xl4lTvjKbLQHSjc9pYCkaYqmcxYcCfCtmxcPOPWVYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMHT60lXFwxiJ6BYiC1U7KnpCUBUHQ3uUocKZwRAqo63O9LcQt7C28suwii0CiXl0d_hVCzWOV7Gm3uQue0yW8g-LAh8OYvNjN3xMErt38HpCB_uvuefiNOIiO_xLiKIcgJ-NO0ZzzThe9Skk6e9dcp-tWM9L-ucJ_cDFNwqk359lTgG4EyKrs9c4BZ-53IgE0LMBvGQaP40nIM8rNr9fvai1emU95vHA69TEK1ApqMP2Is1h39BkytJhaFWjYYoGwAfWD9-E3-OW2DzReS9HJgv5oprSJI9PJlc9g30nSFJr2RrwByZKukR51KCMQ7JnyV_AFILKawd023uZ13hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8mBkTBzs-Cgph1A_WzXP4LuBYWeaPnq1S9wNDz-CgU0vPf61iK_sVAFxp2RYWOoq_R75ft-9C-I_5i7wHmIzqR53AL0lPkBOeR4nfgLrP5-id-h9hxWfMxxGYjynjegs-ODaGSzjTBqzbgoIo5RLrEqsTPjSCtvKGvsBNG3KknxNVkdMaVm1samDfAWJwEV2hLZmyR_h3er9zOn9gMwugbFCyKUpDk_CEAjwDcho-zReZaBVxyRCmdD9-iwcuXhuvv6c15b_U_IMgejRGPnSsadExUAg0Jda1VUeBnUVP7rU25t9NCQ4YZpvITo8slWLTmN0fnNyb5SvEf2zREzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlEekSHKfllcM7yk4G1FZ8wN4BFLc7nFVTfOZZhsMu9khEMXp6infbqSbISxpISqYgHfMI_lGxLi_9Bi6xAY6fcG4tXYTeKc3blr5aickVrXUvZ95ZW1gZWaUVxMCObpkxvJq1fVrUCAiwfIXrro580WuEwQbTmr16zm3acoT7K2NbOaEJej21ebWGcElnKYbGEXulam_KMhge7u1CNJPVWI79EQ0eLSpx12d_B3vo20StLScfgu9BX6n54zyQeM_ntz8ftkdPXg6JneFNIWtL1OitJ3PGSVjnd6q0QX9FV3hDBvtRKEluj8-azN6QpsSk9p1u1mXukDlovj_Y2zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dH-oJtKIele4S4cI4AmUOh9ocUZ_ZO0orx2rYKJ33cmli87SBbT3-QaBqlXJNiyvKQNncCUp-2qqLsZNeVT3Dcl3vun-qH7jldQ0SIVXUAwhgGSZWLTHs0tIeh4lBqND35AL9xu0_jaa2tj59rKg4azG_4Zq4oxthp6cwVBtgGormAY4B5s8sAhe8C5SYbYd4n83-Viks4OiL88u17pyX634SSmpwBIp7jLdsZC7iqliTeXY3GZ1OmDnwoZ9OCIdRM8Y9LO-CDJMsw9qfdZ2CMuQYiRFNhtVonASPeIoAqyUJB5umKe5SRDryyIMrew3a7xZ8Twk517EcmNqzmjvNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R61qpiPap0R-u2vpbNVVcAZY3pmuak5_4-Pdph3F6LgbKexJgigLMGT5qkwchXF2UEsf9S2x5yegCuthhFXid-ngJUaWDmPvhVBTRAJwbe74ieW5FnA9iGzHbvzdwv4qdS44gFQoRJMnZYRCFWGVJNDxXGp383hYgTi55N834vk0qTpmXRo5TCYieAuuyslVJU0HYbmmUBxmYIdCzEpExa-kNO3Ho_lc8NzccIo86surYJXAOIdqZuPNul_C6XojkoeQILr8JPJSGjiiJe8RUA3eu954nLCtifP7kw32MlbxDgva_kcOuBysyAw02eam9iRWOpTH4sKBgaBlAv_-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt3LIVuUh3ZsjB1Dw6_8ldm3JhYeeXhgrbh_ps2UZNZc8P9Ixlpj1JB8HkKM2Sz05iLStMHecFsFTniy9YUOiboB3bM_-zz4oTUW3Sf5H7HzmEySQ0GerAE2Hb8pMNu5YzztPEw9rD1hHnRxIBaNHdHt3h9Nu6wDXeirsHcyuZav8EuB1uPodOH81kIEb3oLWEeD4jKmFExyyc2oTWPAYwdrAKcom7zVHLXPjDjXI5lwBCj3QxQrE571ggTin9nNtZvg8gmWWI4GFMpqi98hwbqrSAhUupyyVFjeDogh_LA1YKVRe9GdJMs0fghwYcx3klJPLhqU3jfNB2BPDwavEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcyB35bvZu9XHV1vhMX_fAiy4K4h-NWllhkx9Qx5Nd-fS2vcqAph8rtcNgjrmDHxf1nb9aUVfHxvhKmSMiPQSqG4i7lw4KY066B7rYtosQQSd23n_2zpmWCIdt6jHMRoiAckqfjcbwSOYVulmYZzyNyx6vFWaWCdTgU_kjUiuRykD4A3pHBFD2ZM6Xw262veA3sRiDOubULrK5mqBMjewq9HX_d7xAt2iK6BXgOInTKQ8AYGctlwsUqputT2SZOCvFUqU4SVfQqsheF58yFs7XNP5rCAjDiLXwqqqvYiVdfvB8CkUHlwnboA1sOg_C76SuMdIedPGP6x02_FNlmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiKVeqflHnqx6S_JyknpwZnblAolpZ_IMm4LWD5nC9ZB6U1ViZzpfPtoCuARES2whKSG7xkvHupoWJJ7nngqOWtes86q4iaHqpSK3n48OvjWmnHiz8N-u1ZzrnFtXi14lUsafrTfrqCN7K3SJ-rXJD2p8_eTbkVQXTkQNXAYmRpGkb-vyaPUQvimyIn94m4Wp8sQgsfr43Cgf6Xpe3wdO089pxZUUATqgB40Gvah7O2MOy4n-DQrLp6uv4g2zU1raLMTFTHrA0f0D7_iLHEhjmkCc3BjJjyB8m7PSzZlHvceBqktxKJ6SDHkDaUUkOTpXqS4rCCJr285NtkON5KuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG0ySUQPDFlXak4x5S0Yore-8E57wvc5oz4Y2nzEXjsc0dUHmlG5L87KdgOicIDckR4otl4fL1G9LEXB0V4JuBoru3hywGV_9h7ytUlWxS_rXYJLU0PQuGYRcIW7veiAfBWZDOWuT3x9i8fn0XUK6fUsZ9gKZ92EpiZyR67x46yGMCLK93Tk_WZ0z2aG4mA352l3WcwmzgfbokItmDJ8U71eRsItqGC1NTojWlmb75IyvFSD1PAX32ejIXDSAqRcX-KFBroR-i75KHJ1e-dTSLLJBQd8oNSTBkV20EE9CIC4k6vSOcazr-jFYke83Hgar-6v5ICl2JsF8r5Vxuur3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8cdOqqxHgPT4CqNs01bxwU2J7mfRk842DFPuSUTUS8F95-InmHCmV_D9IFEgyK8Upfnj7yMdgjlcu3NY7iE5su3xZ-GNYhhZKIhoV3LyaCTUQPgvBSXIENpAnWLPrBUXvO0Tnih9MxOkUvRvIcfK7slCfnCOuu_RgoZ-Ms4rFdVwHOnUxD3TiJQ28emZ4dxMvwzRzxTE1aXNIRzs5is4z49a95Uvhh0xxINzh0C8_kdP0M-RyeTjXJ0YMQr4RHKBJUjWBTLL_aEGkva6AbhcLR9x4m678_Hxa2jvOCZEqbW8tXTO3EqabyfpiHIohcq7Ihi23gSdCuRnRUba-vx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQTBZbd_BrxGpQkzRm8JLY6Boy67c6UK0DFRn3OYcMwzsneouqGD2JDXfWwc58RFm0l422hR4KWQB5eycrZQh1-sCuExvt5pOI6vSLbetmiUV-pR1v1RWrrvdWSePZTyzx7vVYf52Odh_oihiu9wN6atWMiBvoiHfXLXArn1l-vGxtkRHeoZSuWEJe9WvED8lqXQLKyp4vGi8MkaUGopYEqySMyec8OiD_KPAk4afk_O-oSYvCFFvTghiwjnGfhzEuBTFeHdFsPLk9Oqkh0AeT1YPh2zFq-jPQvspmsSQED7nn-sAw4qmVfGTLSV555pwSqyiF7WtPmJLrgu0qvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7CdIG7FtWFB-sgKlXwG_deBgO7XBCaZvUFjKwWOooxYWtcLm1wPWhjHH9RkyaOgBDpBYDuxcfC8LUN1eoklXyCZa3hNOzJykNrJnUOp9cZWaeDzTDB65AW-9G7hYElCQARgGS3g3KmUGMabsTNkY5TPIqggrXrC5SrDvEH1C507hWTGPJr5sEXWF9Oa77Y25UQ7APEwDp53bgTxhQAtiP937hqlKE2gks9ZtYWPmuvW6f9tdRAQicXygwPslXcU14KPGnuS_z0OZrZLPL6vM1uhoFGlpbSzEMoLRGYn_6V2-xuTieEVoy9TwQYfNPt34SBBVQ0mTgIvoXto-9ZJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVCnBdSGyfz9SBe1g70_UQJ7vvYNpo_6nalvnGozjj8YHZQwYWJJdfQj4VRgwv2g_0bcc1GIp_AGUsI0GEqkK__n61tHtEfzt5LjnW3Sy9Uaf3iK2BHyAxRdN3CMFqAjx0rOhT4GFHBPpivfDOOc_a8pvododuvzjuBcsMhfvgledkqlSeRJ0DqAT4S2fSGMjKRyA-51fxeOY8L00u4cJTpdggMYbpljzK7YUFgeBW8ArYm5uF1n8bdZzPuC2BsqMfvNvcVUT1LsscmJQuuq015hG5mafkCClT0uhA2y2znaRAQLVCZNrzyNl2bhAfupv0VzOgVwVS37dbb5FVNRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct-i5wFP8bD2Z_lRkGsP0EwnTss3ur7snb6IWMc-Oq2Tk3MpHE-71MjZJrA9thVyN-NbmCAoTVcfDtdSSZ2Agfjnio9YDeFPLlbuZGeuevO-1ff9K7wcOzDA4TLqBJxNQLpTf1kR_a_PWzXykazeb2p0HkXxr8iCCEstRuBmhbrUzuRMwCRqp-qW_1QudNbHRMM_gQm_hVAWKj3qGDgmaW9hS2aA4IMnN_Oxe0TSgHYnoVd643VyiII0N3URuyYgZr9b_YDtuiDXQLq39hPxf_WC1YPj2eR-NSrs1g_8kUxm0KNpUvwtNwn6IZlwiQjKhS51R8IrMxTiPsQUXp0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI4_h7lSGAvgX2ctnn6sbtbWrkaSydQR1lt-dmdHMXiOb6gzfEquYSvSykT6btRqTHmGWcBfyl08LPLYcS5BfTaFZ3ELRqBTcXiIwtTjG5TB6rjFcvWLJljtAs2iQ7lRokYlTsPJiworUB8LR-L2c8LR7xl1ok6tXs-qsROVTLWuWSEG89RfFFOjU0QVjnXT4M_9LofuAkmDNWdCW_TDPNDn1-wUmK-mY34sXUhSJ7PygWpKQY7KoxIPT7DUH3dXv3vsd4YRFcuwPSzW5tzPaCNlbwvaG8_GhaE5SDKr5wz-iXrZt8M0k77aDuTUSK6m9aAi-jbBRR4K2yX4-Ut0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpyfazw90cjJiHPDbB3M1XEyx7JANPaBWdIvrN8y60Vw2RguV8okAaWx6Ootwyaxi9i35A6If1W3WtELRzPiPB3vW0GRfum-BTUKcHsbjRaEo2h1bI_zX2Sz2puasvtqs-LCLde-0-UIQKCmIA0aP9iOWHfbCb5YlOi3yVWj1fSWjQ7eRDnt3mgN7a6i40JhMFqIWHLwb02EQfQkMH5GOasF2PeXnwS3tPUmRY9wlnwCz_mhz4RNBc__vVAnzpeNaiyKyFSBlZLgx9CwnNT9GdE7e9MDhFU9S4xF7J9znmcu7RTYA6nfO7I9ajnv-WhPhf9XQ0iFrpt0jxFHL0QMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKPx_JngBhysLCwTpTzHbHytCDdVfAiJF9ST6ClMoY8dZ6GhRD0FOcGGXNU9x9AI5EgEzYTnoLlFfpR1Y8XgNJiPdBvhDtQqXXGKk6dsVGSs0UciTaLeuhdSwy8yr42FiKTrBrfVUJ8YGIEthk_Vrbljnmmr9NxQzM-mYwVN4aaG3TrQji-ClpNXmIATLLvFaGXxfPXLm5AbviuI4q7f2yAor5yp3G5iGPYfGLF0jShAgB76KbLOSvOeSfb3ao5vv56xnWCCxBI4kFXy6Bi7Wq3MJxflPVUzk5BYZU88YzTiD_qJgXI1GQc0wHxYZxFxzDU8K3CuqQrYULCUQYXvpEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKPx_JngBhysLCwTpTzHbHytCDdVfAiJF9ST6ClMoY8dZ6GhRD0FOcGGXNU9x9AI5EgEzYTnoLlFfpR1Y8XgNJiPdBvhDtQqXXGKk6dsVGSs0UciTaLeuhdSwy8yr42FiKTrBrfVUJ8YGIEthk_Vrbljnmmr9NxQzM-mYwVN4aaG3TrQji-ClpNXmIATLLvFaGXxfPXLm5AbviuI4q7f2yAor5yp3G5iGPYfGLF0jShAgB76KbLOSvOeSfb3ao5vv56xnWCCxBI4kFXy6Bi7Wq3MJxflPVUzk5BYZU88YzTiD_qJgXI1GQc0wHxYZxFxzDU8K3CuqQrYULCUQYXvpEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=EqCgSJJL_R_ifA17vZnZrAP43MKpnVEP0Nq6ZxKWcLitDXEBmd10nZK7yWyg19674tIl56w3463XR-kNkmmCbHdoQK1wwaKzPJb26Y6nsvduRc0PWzUgKOykMPW3lJggGlxyWZMQrxnVhNP253-aMU0F0jbXREoS3GZPD_QmuY3El3I9K4yX-R0Y33T-USheHKxknqqvE-5NHvdUxunjIX4BURJ00sjWwhWdV8ZJFL1KJWmAVSu9XFGiZzCq-Zzlfm4tNOVVQ-V4iAeofnmUvQbaF2QEjywaYjyQc3f4eWHut7zgE6aiKLPKPEoNQN3zDbwOIdkTXchFysgRW82-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=EqCgSJJL_R_ifA17vZnZrAP43MKpnVEP0Nq6ZxKWcLitDXEBmd10nZK7yWyg19674tIl56w3463XR-kNkmmCbHdoQK1wwaKzPJb26Y6nsvduRc0PWzUgKOykMPW3lJggGlxyWZMQrxnVhNP253-aMU0F0jbXREoS3GZPD_QmuY3El3I9K4yX-R0Y33T-USheHKxknqqvE-5NHvdUxunjIX4BURJ00sjWwhWdV8ZJFL1KJWmAVSu9XFGiZzCq-Zzlfm4tNOVVQ-V4iAeofnmUvQbaF2QEjywaYjyQc3f4eWHut7zgE6aiKLPKPEoNQN3zDbwOIdkTXchFysgRW82-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u59DIGH5jfYOFKVbSD7FlithfWTbaVn89eDHhrsG_VbFXaiHYDhlk2E1IeXPyi4WRkC0kqLkbl-5Ve9cGOPDs8A5L51uvKVZ1Ut680dqyCkwef2T-bZ6phsgH7_BIEvq43y53oku0icAANAGQmnfprDi97USiMyRJDx0f-xxSMlNwI64T5XbB4mEuBaUG2fkQlwjW8TvsA1BS_6eEFvFiQsLkBVtjBCvAxr2VTlzeoAYrlCdNxYwZhUI9uf-X_c2YWFeuZvK47vJcmwnS6U0hSybzU5P4PmMRWEFH8OJfHxcQbAkXi_ILj-_w1-k14PXLg6e9i-OH03Jh8ZWxhNe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqESK59AIQSqGUQlvn0YCu1GMQWYzhIoTi4PW48LXRtUNsHMQFPPhhpqxbY0jbOFskRKvQbiVk20WmbURFY1TxTShytTtrfTb4rr2oLQszf5oolDuaM-TFuT6YtRX_rrFbDAMwRCa8dyeTb4NnN_kmgQb_FUCjAWMxC-qz3hh2UogE0X3tD69v-OlO6ahyiVZHuN-3oJVUUdJGHyEwFG13e_6doNl7BTOA645WRm6tPLdMxghRmNemmOWbZvUISzBGeg81KswnYdzO8EKCMYufXY8Sg5fo6s6GrPfXLP7e-fXOyAHEwxVm-khNXeC7-22Nj4nn7SY0TA8QISfBBVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrVw6FjPV_GUkuK4wGuOiaR3gK46Pq-Hx3NuI2PhmSuByFddfXL3VP9Qd_vzFXg0HwwT4g77s0azjyh6lPqWsD8DV9VTOKYZPVmTi28QnXHug6ecTJsVi5-_KUV4ntpWSxgtWM1XFzWcLd-kahnEsDBvACeq86ZSo893sG2ImDpnnd67_WPcOBIm-1Co8dKtfEur095hZ8piQMDnCsy8hFJ1cDnetxBcCUWmo7l3FfmoJSXqD4vwbuWqjlarGK02R-3RhdjtaFfi-wAExT0y4DLrEb1qE6IKc3vNnF-wLDiZMvwUr02DemS8YVRq2qAX2Uhmi38DzqmMB2Y-r4NFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-zgPegZARH6DWVgXz9UbRTG_Hx_kCKPlYZUmHTit8HDBUQ13vOTztPtlCYVg4tHiYB9Na458Bfwxetacnw2_Ee3-VdnteyRmnG2yX57vxGqiv1EMfU6aTFWPTLWPSFM2uzRz3ntiobWwIbEcMiJhrWygYRh6pFkQPGPRsWWg9_3vXT9VcvK7dZA-il8SqK3_hjGmgo1emeiAdikSXPbYBxY6HpCEPWW7M2vy-zHhMzu8WCFaR4WraVAdieRkQvxk0O6FRgvPW0uwfCtzLm2UudNgN8qK8Qs68T0pw86IOUxkIMgkg1jhEXjm_7YfkPYXooddsh7SOdSHpmLL4aMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpQ0aEmAcPgq4-5xhU8gMVmP2XCtC4fN863Zx_HyBbPW66OFnvucLzA3M6bTB4SdVFTkia9XFSuRbhHZPX-XAaKHhwjtNHlBCTqpSTFQz7SR9bFlwBL34Hslx8mghc88hd73t-l2wJIk1il5FpWNJ9AbLguTopk1kW9QC2q2AJYhvig1k0ob9oUqxkYB3swqwJJtx03jFBDZiLBIBycMn-zcHxzgvcdnUobZMwRk1maALqap3hV8-76X83qpg81ujQTRrFyppToqiYo3rZxYGEskNg1UT7CutZ8TrCSaIiS83yY-GeyJZnkUzSPMx6bI_tN1kwN4dDVOrHYVcXOkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMEXgwPCPw7O-ZskfCZVD8mBLyyd8keHGf7uJp2qp_A6wpHFHaYQ5D9OHpJeCOjSpDKHFwUOkIHAsz-pljjyqJUDqd4LGjy9nP1f-P_aTTMA2zqHhS2ZD3nX5BipTUKitfi-cN1oXFmJdk10nnTSvDDGd5SqbsALHwpVVmJSDzlYNiQ3yvL6zuqW742ctsSumvVzTjYV_eM2pVbqRdI8zvdXLZcwktgwYVXUyKPvHVxupzQjBbCOfMYbDCBgusKjBngTsk_Ag29FdF-mE5P5MhHlqulx07OX0YZsSFvQ6_kCvbvLQhHP6jM8jWNB72XM89XObu2Pt3lOEvSUrOa_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRXlTxKkcBYkWXPZYM35G9Uxhk_hq2_0_P0oECSQRC0tnBZmuvEd9Env7igLOg-1DRIJeY4N22wcZiY8K-4Q3qa7YZcm-PZS662uipMtNkzrNUs5RAwgzAtl5tVkic3Aa4Ket4_Y02qJMYjYi4vWQoFmGySnyWxaB6cjKjbBfyvuh3DMOqMbp94Wf2OJnNAsQZH_ob264i6lGakkzBJlxOithL5DzEmHZM4bIrmoSqqqseDSqvOYzjfZ_pxulGqurRF8TwAFI8l63IIlDwndBiPpZt13_deQXzpATrIzrI7kxo_1E3OevkbweTk2fs4Jip0qcack5BOl8M4aQmUniw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbtYseLdWufDRwclDg9ra3j5GDIia5JlODC-NA4B1PU28PLmCLchbNsbPzmMof37kGTm--0LtoIABlZm7Ob6GcpKBX7FS2ekZSSCk8UwZhDgxuA-SrMLDAn8qRDgnIVg9I95DAAGx2nsmHvhFS4yQjLE2fk0q0P64AWO2JcdaZWHDqcCoLxbDAwWe4orUylDwal6pc95RniFlzp5ZIkAPTJhP0G3shZZrteMIhpcqOG5L8xW4kBWSTDXDj7_bXD0-HnXu8nBDhUFzW_A5D5pQ-3u7155_OzSRuJlxoB4iwMbroFErXa1fP3p0FxBxWng5ZZ5ZV4qNMgs5seL8olsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVhN7eUFirKynwpzlxVYTajPrwU7zoQygdYkvLERLfju3tJAXLvnbSUZHPuaE8wsNN_kgnqLXcmwWZYFRAnQhb1N-hUAg5D02cCWEInPbFUI0d4s03S_4pXxHUCMUBoxgREimY-GidUw5CPVwcSbwLE0XEStL83vWJxXhSddGsC-fq_-u47IiXe69SGNBUvdvuZcfcQWqGoTO7_OE0Mehwcv_MNXdJNTPRgQmGQfE8npHSDv2eZ7tJ23m85_DE8J_RBr0kFmjTm4rgXvmTejnnvXhidvaoSN1dgsn12OE1oAQ0vIcLWOXjxedYaoNkg629oYxYSr2kg8rk7gwHT5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PipkfCB69lms6JTPn3-3Rs3GrdtprDN0FRTePGzhkiZm5IdkXjPiSw4iI7PKQp8fgDL94FKvVEwQyJr9aAAh2AqDHg0nGeGLEpvpjRJE1xYnP2VK_QHEp7kIxGuX6_YDS2l4bjBoBrbJA03_uPcJ706CRfTXX_cJVbcML1RWeYbRjHoWduwwoLim1mG9lc1Mlx5izEtyD9vq6SR78pLxh8WJvYvKu5j7znJ3viF3iW9LZ3kDwOeGVGaVgrfevAVt79NVAlWODrEQHkhcjNz24XD-T7imLhzOeVthlyWEn4gexpq7_HuCaHar5kCmhy4EqBpXq769TqY2zUM9Mt9_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ius6dyI5YG4Kma4kEDRt8KHKgToBb0WlLz2ZX1alrtR8G7iz48lf38qooosznVM2kRr0iSr5GUkVVkTKmBK9fPtPa4ScMyWSyMl71pAz0ICMDkiem9We3U-Iaupr7rIJ8w3wG2bxsW_Qt7msUvHURzLv8F7wDyxdwnbia5fFB3YzFII1-joyxto0Ff3sXkR8k8BuAxvFWSXuMsK8xIjmztnl7ssdcTtp5t7x5c4MSuhab-fsCvTrP4SreJ11H-q8rIXUBYiHktSK9k0QIBiCMZI6Ql6DjgEJ-7tzYHvuCtjIw7_mlPqvImBsp_pp07c7Isfd9ETkNiu2ai5uZ8s67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obzQKmNs1eJ4LbI0Q4o0S3ybfDKY79dzELtiXC3nQw-km5B3AO_3Ov57iV-VS3mEIwpH_4GDXYGpzpNCI4jd-kd4Vg7h5jH6dALlaIaU-lvD_VcUye4XVSRcZx2F76hL3zxw0q8Bp5ivz0fztf1J2PTFIOV7JQAQNsc2r8a2BwRVOjodT9NMeRuYhMOdp9gY-UAHyYANc7csJMk-absBkRuJ7bpHcvC1quo-IHou8jZwr1t_KnZFT0q-QzJZ6eguiPLX6VuEnptaY8NNKZb11D0Jgr2xLK3bC8ykObpsvsTbMuU9Tm2VSsp4hw17wz-_3633WJvu9A_hsoF0wOryxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH48wKDkQvtoQ6g5k3YM5XGypYCiPRfk2UuX8lVDMvIskCFY8_L-sgu9JflJkQMd6H2C6lOLSftFgr4O2iLzRcNFW0Q0b9NA4wqZI5aA8x6oeOaQb4sIzCqA57aiVqmIsEioexDUGJ57DIxuQFJvI7-zw7zNUZYCAK_TChPuoUX8OmJbJuL1gVlz75bxFnGhwIy_KtapkWdR0JDqMPN3kd4gJ6N9HqMxS0eeep1o1HpV1SZq1PlwOc7BOgO1wSIdnYVJ2g7-E4ILoEDFkbdwdzdTjo51EodqQcaapxZRn9uaZvrg7VBnEwBEovXpf55ZWfUpREg9D8OosCHXrcyfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh951LdfyGgH_bVXE2_IT8jfRngrt9IxEQE_ml5z7TWXf7Fo19NWUJ19e9LzbgmKiY6erJxmkip5ctU3892Ms6D74Lqr8ekUfoGb3Z-ba8TNAnBytBHjoNsUCBxwvTWprZfcfz2gubVvLYO8aoncfpDkcnvxJSjn2aWXrKvNAiCcRBRb-mH89X1UF1vc96OOo-vYkXOIxsOpZ9edTU5ElcuuvjdvRvYB-wTsuVaRCv9LCHyU6k4tmVOsYmleEPgbVhdNfi5bcfsPhejOVkK_0UBvevuQTp9pzLqahNw76RYgGI-MmWjgHbPhJDSQ8zVxDZfH0UjJezGkeR9WpuNaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4VuuJX86IZnwDx_gNlrVNs8XwWlCiDQbnydpKTYslzDNBv34gFa5_s7LilvIvrIPYzJIXgDdzDms4oVO0yb8eeb_sa-ed57pxgNwt44vz44y613YnBrnGfHSHNzMk8l0VsHHRoRxJt9068PgwQlG6yZDM4Ef4wRyx7iOsIxQrwu2HxZI3gIzZ3XNo-iMfl_TeFdbRfaFWcmZvTnSmHp4MeY4YhePHl4zWY68yOMMuli4lR-TpnyV7-LjfON6y3-_CHB6Vsv90UDkddo2TCcvYXMheclzstW34uq3KKrHqiDwy7h5qioZYtN2m2sK6_2fWTXtcIzT5ByCPQDzlK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eimQIYOmGkepOjYDH3rSdreqrhsnP52Ag3Eue66moK8nbioYst21x4daNXJ1pawMFpP2TBKrpGTsKrdqiljmrC-yJszobOlPrmH06r38whEUT6X9bB0uHVJoqeLd1F2g70LjiXnnb4rzWVr3bUi8EwVvlXM1Fw81MCMCQpQxWIBp-x7GZsFiWmaSjT8WPb9W1uo4lUBjVGAiSPQ3P5FAzUbf-FZ6u9VYGgum6oyXrymGrY0jI9IUw5P7mFPDN6WVe_5J9BkB7_QjBayGoYA2j7KdCdhPmLb9Y1Kj9nV3scsg8AY-uDSjwjl6DCkw9jk9Wu34EUv6m3gGheQmSlmLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-sfXlVuZQoodC7-z6i8qlQtP9DC-eu1k_VUW1R7wCEFtlvd-vFuyDJfUnRminFJq9osPTBGFUPiw8lJLqzC5pKBAZJrzgk3g6pgn_gdobCzTNPaaJA_JlalrDYe0cnvbh9yJICiMuW0Kh6q4sjldEKJXijE6W0nIDEcclNp5beDou3R_VDrV-93t3jlq16-rdGGSOoPfnJXwb5kDck2PzUcejiIt9T9QQuZ8Dr9eV0yWzwmnqnmbLFX-UyKx62gUBx-Lp9Fwpc8rDD16qbBsy0i5yqfIw9-1nuUIUJGKqpCiGpTmdMMD51YvhJTRKdx5HRH-PrZFuuc4UDro_mPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAqpsYOtATHNO_827NeugGBupsR5O4CTmrQgo1G-hyCUyKj0gJPZW8Au0xytNEodIsYplY2UxzWnLfeH1Ro5ulKi9aELG037kEhOIMocWi6vVGyzr6EYZD0qs8bWE2Lz2bvMCC_so3t3rZ0-2oRJju_a1rtZwROvzGOE6Em7g5opGE6efinfbX15VEZ2piDS_F4AUQV-WLfdJLbESqHEdBz9vbNmQExQ87m_MgTfqyT-7LvtJEhox7mZVUHCRKDnlc_10lSl2hIg9SV_I5d6f8vJgyYanIgRyURokr_n7Wc7d44tehg_gJF1buDZB07yBDjNKN5SWkj1WKYcTcIT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fclk5eTo_vO9IWpS1fsGQpOWfyRss9uIGOh2VWeUhNSHcF_9Ao6cXwPxbr4z5oTm7oFML2KDpIpWvZ1cXx9CL4qBbFgZyYkBQI8VUlBGmKauy_osO-i6xqvI9JJ2Ba78dNJ5DNBI_3Ct-f7tJ65Gf1TqmFe3J-UlT6jUquOpnrjvzrR_7dOIpkkfh_J4XruoN7eIF4g4AnEyB5jnxuT-8SG55OApvThi_iCzhfwIGgQvFKh2DoLr6LpIJH62XsDwsCRVUgB608oa_N74Bz45w-n-mrRlXNF3rL6wyg3u3WWJNe8Uo0OmB3jyuzRjDHlg3c_tmDYOHvVlgmVdFVgTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Muywc2SplhDS8u1EeYHrN5TezsJtEU273ggnEXPSx_B59VKMDF6deI8l2yNpbuetaatGa4wHQiTGd5VcQKnBR1xXueLW8Qx27Oh6kHTV_RxaZIjl9OUWAceyqXT_cda6UpuCLi0PcWrVsaLfaTWJLvQBHJsquHYazTbI02dH-uGGae3HiMrA2rqtxIyoacGZJrqKBJSTDJhEUJhGH_KX0rXIs93b2CnSrcvZASSqnKMEA2-lRrrXanVFjHoJIgw0ZbCAJkKp88UyhjEv7lS3xi4tOY4nj8XMJuhLgq7rN0jjfJ3mGKIQGS6DDeYqbtkt6G9NpXZeZAihwafVrRe97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0XOAzQlXUSpm1ZAUR4DmHGoZeNpa8rKadqlFH-9-1G9bnNWiQfS1xy0LM75-az41b9ER3HsRA26BuFUc7wREu2dfpZCyQ69AcBmSKf5xgIgU3pbxdY2X6-w46RjRzwbQKJr7ISCORhQ9I2TKpzMpBAiKWVxJRC4Wmflsr8ldDfmLicgrDqq3Thbr9w1qNZDHAXPM4taqt7p89FLhKeHK4pPWHw1FelevX3Sr-Mpbn4pnfVsKi2ZA93oFC84H7-4eLj1gcf0JULquILokPY946ryAH0Yy8RorjcmenQf7b31muTjFKgUB_r61YT0pd7I73-txhvPyO5TSP6En6mY_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEGSA4pS1oT9c9RcMDAXA9p6nKOQUKlzwE1ISKVOjp6O8N1NZ7afmJTHd4pl5QscnloOfHZ2xPU4grk_lgMmiNEo-g_dLk6S9ItX9jlwLywEDM7_r0xftuWc_zuH6BAjlXuxVCgBkzEaxFTLUY4XhWWH557DqTv93_MydHSLvu-QTQqs5qxzqV6ZeifzE3FV_041uFB32QohyxWiRUMY342ZHSc_snvG-Pf-MtHHVgGpXzU0Tw3T-IbYklWid7-dpqoC3S17pBG04cl_n-iyjX2I7Q9wGlJhOoQyBTNLUvxNQbyLUjrwHKZ9ejKeG-Tih8DGBBj-kNJ0wbRk3xFbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3nAkhBmr3VAovE90MCx567n92djLUaEHfe2c_aOKo1n8HVIjg4jIZ4R5mgztSYh78hyWUb13sJ2S72fvOkrX_jVgKxKBs7AUROJpW9bh0bIHml-fvEi9CNIYiO3uaxyflphSm20i_dlqVyyNFq55-SFj6FEqgdmsngX-wBB0j3BYGr2DpiUxkWdYMZX1Mt4jfooVp_djEV7OdsEaoFHa94ptkf0YOc4w2RsCr0aOGOEmq4iExfehy0nTmfgjHiy4rGdrpigx0nFiTDy3_CWOCeAYI1Ad2ScIWsxDIS0uTT3ybRFYUJj2VZQUIVJ0nms3YA1d_h4gO5MlRM3jD8_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTRIQ1PWwkQiZLZvGPKYFRIX088iFAc9dddrJSzpF-hpjZfzM0gjd3q2-ZiWrEPkD2xzXFTOnYsiVvAiNqqQh9yaeQPAMovOn66mcizlNKk7BroImwfMOLGgQ_eNRrYecRlVmdwYWJZFUEc5lra92jypDVqcEoEqK82SQ6wgrW7A7e5OA6jw0HvgdPtGwHJM5DXSkHcbzptG6OKZtGlHa75YbyrC399UeCIH3bceCOAOIRDqUh_3vdKfMSoOWlmf23iueT1rjpvI7fmlNu0ICHkvs7Ii9RFSK_s0OXkeXXQu2Oi2coYZot2jdVSQvIOMnqBArCItseN5mQmFay1roA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgXsmfcLjHUNmx7a0Ukd75E6koatQxOilYNMAyIcdeEh1HORPc73d8IObhw7qYuAsIuIKkpM5RjkBIhIYGbswpwon7Y2XAEQDiPfzEo1giKjrTo42E1vTjpF3h-Kr2VH9_l43bPDaLpvwLn7yjkRHiNMWn7fXH8hpgdoM0uBOJuGl_A2p96ZBUgAFg34l9iI8cb5TdMDEk2_SX9B3Tpm-WUe4_CHBRoAvOsoBd5-wcnHC5nUju2E3wwLC2FX91S4yRe-uFh2R4waCWIZovAbf9YMVVW4jWu1XSK6Ov2RsCEaoEhq3s8cdBbAb-pyQu3jPOhicJRbpWVBD4LMmPXPiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU93bueojIzH9WopigVAG8hLWImvRbuak2wWnbf1FdoVZUi8oBoUHKSlhXs6ok13o_1Q7EgU-OTgeI-H9GuZUmVqqBBziS1HMA5IFJY-erUDgS59wiLGUK7UligTCV7UbzHJ_MxFKun7-PqNVNRGdVKBZRckLuhn5yc3O7lUaYAz0WlOHJL0DGaycnIAr90ZZywly6lIGsBVLPMZasyIVuQQjpCq7pmzYvBLxoYrsxOAk0dgXw2qqa0Jn0e60kL62S5eX-gnFDS9XmqemxB2DH2AErThgmIkwUx8cRsqMKofKZoIDOpe6delHX8rfc5wgFFI8GhcaoYmQNkj7sBWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km4NDOKYuMZtikq5LTWwg9xxH32vH8i_1LB8HWCTZ5OVeqx9k84-AKbSdZC_DiGE_PYMJGjQXeM3Q5SC5uH7zBUPvHZRQaANsNDxYVqtYKtqpK_qA463SPf-pKY7M0Tzvm0R1EQ-LXZvpSkoGrqUxlBB0yOZ0ScRiv1-pChiuIauaJXRy0zHWSDrWjwMzBhSBnvNLkLhvVxB733uWrVojkW07YibOFQJxpAVLwmxBevL-ON9P3C1vvOqGSCiDcCiDjCjNYaLhmO7YVtWMGceANTqn_kJvHsrGPmxsch6OUhm9b304397dEvHEXN27wvQVJG00T-sniKHzDMKByAIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOZO6rFo4ifIdl1e9sP42YtWXSRS7L6Bpbnq-srQGl-M8RoqogZ4F8_BaqAh9a3QY9ZRsUyPY0PmC1mR9Ytd6U9KQx96gqm1XLeSdfimcZtmTrfh5PMJcSjOK38r_91lBtRdKWincwogZYErAAWs9cHjD30WK6iufVwNKIfDtf5lCHmWW0NzT1_mnRJwuZGJHMrigYucIVQaJdlSQjQGUOOLGIzZ3dXNnQRe9DvoPpyK0pA2KrYraNZxmk_mDDrUeOi-GfCAFDauXT6W0-E_2rMxtp229PdLL40or5qfw1PU1RKbRpXlOKSu_kGcxgqvPP8nWrv0yjq06ur98n6pBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoxD2EvHgGKIkzVYLVzcWKNhJ1MPOlPKypEiK2WKXH_HYHGXIqAHjP2xKJPNt3yaMVUQIlvXl4qme53kWq8VPYN-M4aKBhs3Z58sdLyf-MWEcbtK3q_jtLQlVHkIJooNhjJI4o1ZaXOtLmqubJdOKXOvS18rwpnM3H61TZMI7IyleaQS2DYmkgmbCMVZYX6Kb4ZupxOQQunLw43NCz5QHFG2iDueGwvK-zfIhCDWNm30ne-9xBnS3bJi5qtXdo33-ThKxt8udIR-KXSb-QpOUDNWbsnuF9hZEDKL5CULf5ARiMQVbLy6IXaGHRDE51nXfEZVM_Rix6T9jmjWJS-LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3V37_eb2rA2VFp4FBps3dEfXKMi3PO_bcjtE4cEYjb3AT2jcmUD2DVa0DjycKdig0c2VAZF1mxMLWgyFozYZE0z50K79GQihdtriBjnEi7bmSNFeFh0HRnC7uzf0zIr_LVRfGHlDOu573b2c7x7d5SIJLaHXjO4oTxyqqeD3Y5p2AzxlYUo1xhaOQHx07clAJ10Q4G5yLXMahZdloMdIe5XqaL5cbW1zwiSnIkT2BWZ5HqYLzyERRXR8dDhF6aLYa8e5_iz0JLVR9tM4XgZjYNrg-Ta2AJh-8bpIPVZeBGLr3XOAvPJF-Ww3EeJi-C_Ae8cRZ77Nq67Lgl1lK4bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ_xpLuQ58dDzCq_Flo6KyoMooU0TBbrZAavv7CXDDG2s37OKosGB5-OhhP6sGCxKIsDRzDMLZQJQpBLdM8KamjOHmVatYQ6ROQn44ksuspWgmKsIMYX1zjOQpBc2kq9QaLaKio2WlT9dQpTcRNmtRkIQ8f9nOns6TNDwlMDuwPDBjvdS_9wlAjG-p221pXjuq3gtTOpeoPRmxdv--FWeAcNSl6S32IXeFTR8M__ZUk3HCcuJJppI0ZHhQMSZoFzmLjTSV4H8FnHljy0aX6cjDR8l1Rqz9oFxLsDvhPGKvT_LddX5pwXp3pSiQmVQjXSH-pC6XbLX3Ieoochwcq36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb8PdyixY8ivUJUFkGK66d3DGAmQF-eX1ZQhV6IrNWp7nKUXH2vTLW63hNGG06IeDvMtFVf0f2NO7VdzyjdqvEwNrwyNQ_UNEW-Ufk0eARpLzBcn5VzBVewf8tWqO7TyutVh66jR4ZX1bjbzhs0zP6zSKcTlUdgMdCaqJlf686RtDduZFLmbEu6TkAajZYTvbKFQoOKH-Lqk0iilIy_NEtGt2nKH4oKnR6WEhOKqdjNADljKuU0bPvt6sogmYgaL5ihvMS0m9Gd11QMMDLnvEuNhRyUfCIPZHNl5o93I2urkbO8gPHefd8vfzcPCK0cpIVEkNvIP70hO1JCVX4wJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-4nfE57PzwxrEXW-fZCBUsLWlIRqzPjHq4A0_EjzUxTrWZvug4mBnKQFlksmKwWtYg4YszRYlJSHsU8bgF3F5j-AZC7TP5SJ1kDRq_Fz7fKd1SXL7XWYvSo9_gxxM9d1XNLrP3U6BX99uq_-tl4X7mij46mg8vZuqNajZerA6kOgBpVnNe5s_m0x4-auvxjTVKDHgPKffOLyVdKaiU_YMaCyLtG6IDQSAB5l00YwoPask2u5vVTgtAGDfgxRXI_dfWB5avpmsKWpykniAz7V6p6fK_4B045wkXdxRw_u87BEwriJbzJVyEE0QNQi0Yru7T1XOV7w_CHCy-NTOXZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=uW8RaQbjHX5g9NzjLaExpqjvaHPno3QAgpsGnv3KAx9k_i97GFd7WphPrz4cCZHqXiHwMPccvAAOnle3qAeNaYF1HhyIoqJbgHzjoVoAmXLS8nQyn5P4QS7CtJv1PvCFV68nLHkvQo_IfH4IjUUAeSvTTVqOMwKPRh9oJ6n_kZ2GgtHqVo5AE0Rb_pPQIA0BRwXpJCU647unG85zPbUqvncV9qimX74JBcmD-Y2uaAI8UZ7t-ptG5wPQIBSCm3EqR4aRAkG3yxxk_MFfAjk9KflF2DtMvN6EdzyyTNDnQ_m6WdjFVd5RNwp_rebP6V5Lgf3PbLVBVLatvCX7Sh1jfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=uW8RaQbjHX5g9NzjLaExpqjvaHPno3QAgpsGnv3KAx9k_i97GFd7WphPrz4cCZHqXiHwMPccvAAOnle3qAeNaYF1HhyIoqJbgHzjoVoAmXLS8nQyn5P4QS7CtJv1PvCFV68nLHkvQo_IfH4IjUUAeSvTTVqOMwKPRh9oJ6n_kZ2GgtHqVo5AE0Rb_pPQIA0BRwXpJCU647unG85zPbUqvncV9qimX74JBcmD-Y2uaAI8UZ7t-ptG5wPQIBSCm3EqR4aRAkG3yxxk_MFfAjk9KflF2DtMvN6EdzyyTNDnQ_m6WdjFVd5RNwp_rebP6V5Lgf3PbLVBVLatvCX7Sh1jfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1DQZYv1GAetKdNJ0zoxnFZxV1LkCVXK0BiIgsd0bDN5iYA-7ucxIxw9qdtAPzexEPtxLlJP_flkaUwiGMHt5jTHcWq-LosTTuBHh7rV0jZT4Hb5bhxB3bKEJkVRbuL5NY__brLvJ7OKv0Ab34nfwNAFLDdwj2_MB05czWMn2gAAw5m5zp_NpUGqXEsx4JGYloUGAv8JgXMBkwvVdnjCZP9n32mFsoMyoHdd84yRYF9Gtv1vy8ngUhcebEDKw6kbswCkJfyPYdY5lsB75Sqrx2nxxXdLLuD--6_QWsLtvQT1_J1dyjPXwe7_QZ1MiKtATnmrXTrGRqmhyjqUmC4U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=RSxpNDJ1GKZk2GlljsiV9sOqRrWuaXvBj_UYWSJlxiWLAKWxH4G4U7FvY0edwzZY7iCMn3tLf4ZRR2Z3FuiVl02M1GYoQtj5y3F6-laNZCa9jNaDWRZKRXbp_pdOs8xS3jLp2MUTMBUuBAeSQsqWod3MjiNW35z7J0Om_JoCibEJWNWLbvJaSevNbemsfs63o40IlUPcjeBNLqc3fYXzJZzuQjXuL_PWuMBxBKfkTVMPIkIu9tU-RD-mlMX6SeJ8-15L6CBoy7-yBurhXmlAPUGpCuLuFjcJMHdzV90o9YhM86VI4c8htdTiiZnO3IOO60a7V0C5FMl6RPyeiZXCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=RSxpNDJ1GKZk2GlljsiV9sOqRrWuaXvBj_UYWSJlxiWLAKWxH4G4U7FvY0edwzZY7iCMn3tLf4ZRR2Z3FuiVl02M1GYoQtj5y3F6-laNZCa9jNaDWRZKRXbp_pdOs8xS3jLp2MUTMBUuBAeSQsqWod3MjiNW35z7J0Om_JoCibEJWNWLbvJaSevNbemsfs63o40IlUPcjeBNLqc3fYXzJZzuQjXuL_PWuMBxBKfkTVMPIkIu9tU-RD-mlMX6SeJ8-15L6CBoy7-yBurhXmlAPUGpCuLuFjcJMHdzV90o9YhM86VI4c8htdTiiZnO3IOO60a7V0C5FMl6RPyeiZXCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=nTco3q1sTN3SyZO52txWpJp4BeYibKRTfkuT_F9daMfuu-fKUxZZqR7dYoLMICsJ-TGr36_FmoFRcaPQkQebBaO-FWjdDxqvHx-pAo3FtEMLGjIvP37AOlt5D2Fa5lNTeEg6MYxxGJWYdtYs4AMAUee4fVZMdc2soB9iOP6jJk17klwJmLyDcgvVihDah-HpHCsQUP4ztBRTqTQfwPCT7LJP2GSEykfP2n1rSu_O4WQvU1ILCSzhjiaN8dtSEcNbVypCLcDAEAdzfZmpj-GJwhl8Wku2PFXwC6GwHzgnd3e1cFwLD_6mtWw0M2zg5wCMiN9iV6UUspB6CFjEgGzn4WzzHwXHvWO4cHx4hWprBunkTHolpiNcYfB81jYDy_8WUmtZgIiCHAG9LUJT24VdASXIUXNbIKQYknliggFjWA6k-M_bbL0wtSedKOoPpKT7Se3kDxddLYy0h-OAZKWH6Ik6cpKMScod6FdEj3KdGrEYy7a85hJlknNTkFKNBrW6tAvLqoYxaFyZ1TDMAgDUpin5Rt2PuiMfkG6bfMzdAoioW-GQRpbI3KvdmPLs6z3mlCEoh0DqxnTmQ5zMTWQUM9JU2B4OXRnOL-HlgoPh4e36VtdbYWRg6dl1nE9n8UyghPkGRR93MQRdU5D2-WVJ9E1vf7-SkCT3u5DOETtv3fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=nTco3q1sTN3SyZO52txWpJp4BeYibKRTfkuT_F9daMfuu-fKUxZZqR7dYoLMICsJ-TGr36_FmoFRcaPQkQebBaO-FWjdDxqvHx-pAo3FtEMLGjIvP37AOlt5D2Fa5lNTeEg6MYxxGJWYdtYs4AMAUee4fVZMdc2soB9iOP6jJk17klwJmLyDcgvVihDah-HpHCsQUP4ztBRTqTQfwPCT7LJP2GSEykfP2n1rSu_O4WQvU1ILCSzhjiaN8dtSEcNbVypCLcDAEAdzfZmpj-GJwhl8Wku2PFXwC6GwHzgnd3e1cFwLD_6mtWw0M2zg5wCMiN9iV6UUspB6CFjEgGzn4WzzHwXHvWO4cHx4hWprBunkTHolpiNcYfB81jYDy_8WUmtZgIiCHAG9LUJT24VdASXIUXNbIKQYknliggFjWA6k-M_bbL0wtSedKOoPpKT7Se3kDxddLYy0h-OAZKWH6Ik6cpKMScod6FdEj3KdGrEYy7a85hJlknNTkFKNBrW6tAvLqoYxaFyZ1TDMAgDUpin5Rt2PuiMfkG6bfMzdAoioW-GQRpbI3KvdmPLs6z3mlCEoh0DqxnTmQ5zMTWQUM9JU2B4OXRnOL-HlgoPh4e36VtdbYWRg6dl1nE9n8UyghPkGRR93MQRdU5D2-WVJ9E1vf7-SkCT3u5DOETtv3fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLcouGpFhHYo400XQclUmmXgfDiO2M3wSIexvDOxAeTbRtjdCJRJp7t-2waTJE2Cviilr3RDAnW4O1BgPWMKX1OuHNz6lvAuJfVHTanZavvYpx7vcMBU6ToTJBN9H2QFm6cnkg80FPHUM8zctAwB3XkSzdCPdRZLBqXC1SLrGBwtV1k1RKhk2j-zWfjK2ZI5rKT43R-TnTC3qP3dJF3wYTFOOeXJjY01nOxkcfzZblKA1fW1TiLVutgH5SxyjEo7rTSFShrglEV-1H0O60OA7O45BdNEqUnLqMW9XgOBf1xcQYxWSqwim8T5rUb7gnU59oado3oqdSGJoXEuDs0O4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=TQzSfxttrwBfrIdmvq2e6InyuU6j5N7cLkZ10EAgglcUMfvJwpcMfuzIFA5Je3cJ7QVPnbZyibWXiGa5YQBkjvGZkq4U18alNGU8TjQXg_nfIMLD8tlY1hLrLRepnXvAZNDmx3CzC418jW5Mc4HBIa24Oy007YlEu3fGOz4GQKmQfgh7_Wbnavpb7IyaGWhv18Pt4UehMRG3p9WoWQ08Pog-IvjoTuXzfQMVgZHz8z8ARys2UFzCNvfCrqKwmaM6sQsiKjLPoYyKsDrSK6m9AFUIQtJeOnvy-UkeiyPsHwX_ROM0NDRNTH_VS6RBj7Bkf3jnPRVWuuQBmAVoGSg-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=TQzSfxttrwBfrIdmvq2e6InyuU6j5N7cLkZ10EAgglcUMfvJwpcMfuzIFA5Je3cJ7QVPnbZyibWXiGa5YQBkjvGZkq4U18alNGU8TjQXg_nfIMLD8tlY1hLrLRepnXvAZNDmx3CzC418jW5Mc4HBIa24Oy007YlEu3fGOz4GQKmQfgh7_Wbnavpb7IyaGWhv18Pt4UehMRG3p9WoWQ08Pog-IvjoTuXzfQMVgZHz8z8ARys2UFzCNvfCrqKwmaM6sQsiKjLPoYyKsDrSK6m9AFUIQtJeOnvy-UkeiyPsHwX_ROM0NDRNTH_VS6RBj7Bkf3jnPRVWuuQBmAVoGSg-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=Qp99cLIco1M_85kmxI05Ae5W2mns_zJ83WesvkNnuW8OoRAsmQmVS9pDn-zutfAN6UIeCAWUQdJgWie08OpBV4OhgnqarM60HxPUB6OFqT6VM8WkdAfKXJo8izVWAHOYCuCxRZXpmMQEjwCnxKS9pLfDS9ndjCfNwm0tNgu0YXnF-9_3OGSEFpWY0Uoyhvcuacd7tojUOGITfR47WX_yC6q51wkvgLbHFukq_OJHSW6vzTlHId4rselGBTclUc4ITN9SyrScalHK-f9XFWyRpWXVM7AHPC0IZG81LIsacTMfTP4MCGZ-aN3938E04eGVB9CQhD9BFA1JXoyWciv3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=Qp99cLIco1M_85kmxI05Ae5W2mns_zJ83WesvkNnuW8OoRAsmQmVS9pDn-zutfAN6UIeCAWUQdJgWie08OpBV4OhgnqarM60HxPUB6OFqT6VM8WkdAfKXJo8izVWAHOYCuCxRZXpmMQEjwCnxKS9pLfDS9ndjCfNwm0tNgu0YXnF-9_3OGSEFpWY0Uoyhvcuacd7tojUOGITfR47WX_yC6q51wkvgLbHFukq_OJHSW6vzTlHId4rselGBTclUc4ITN9SyrScalHK-f9XFWyRpWXVM7AHPC0IZG81LIsacTMfTP4MCGZ-aN3938E04eGVB9CQhD9BFA1JXoyWciv3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=cSG9A8wDmzeEAAuVcClEZ30UeUVI_95npJQCLbcDGT5OW1zSK-s-6RWfQM3K1M7x7IA24w73cGWDLkpPMqjhyrVNlZ82TmqJhPoAigsJ-Os_PY4kLPfb9pBkHQsYtZoxGTtkmvR8U729QOpT2zho-8NcdP46lQgJnVyYbqeMXvR8RQRxEsa3gyi6LYTFW2jiCorDRXe_pFGUYZK-yx-vNS8whtEpIgkZa_iIaoiHt8E5xjGp7ROCua8Iibx0pIQsIzCpsgkASLWAX1vDKLDhrd1Uu6jFJuWSjmY7LsShthhTKt6P6SjPYxvyrmNu6LUJGjgKA5pCmssQQE4jlcmPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=cSG9A8wDmzeEAAuVcClEZ30UeUVI_95npJQCLbcDGT5OW1zSK-s-6RWfQM3K1M7x7IA24w73cGWDLkpPMqjhyrVNlZ82TmqJhPoAigsJ-Os_PY4kLPfb9pBkHQsYtZoxGTtkmvR8U729QOpT2zho-8NcdP46lQgJnVyYbqeMXvR8RQRxEsa3gyi6LYTFW2jiCorDRXe_pFGUYZK-yx-vNS8whtEpIgkZa_iIaoiHt8E5xjGp7ROCua8Iibx0pIQsIzCpsgkASLWAX1vDKLDhrd1Uu6jFJuWSjmY7LsShthhTKt6P6SjPYxvyrmNu6LUJGjgKA5pCmssQQE4jlcmPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuO8OHnswvUTfVnqENdz4khJb23nmBgxuaGrMmPHp6V1t2mSowPwDLqRGHfIft9um1VwnpqDpi_rvCXTLVKu35x7O1Er1cP5-ro4_6z65VgTTYMDBw2Jdv5JFSDQGQVqECAqxuMCgG8TdxSm78ke9-Dc_xC-ttHUeSz73wz7Xv5Trt-AejUz1hJpbYP4YhlULxBkwPpIKaoVBhQ1KoPUluUkXnBMduzh3FxMezmCWV5HKGldITXA3Vt-6cs2ekbFQIdAV-_Vlosmrfshk3UFbXnBi-fAgGn4oJ9c_ZYna-K3NqMF2RjzPVRY710sxq6IA6VxiU3y5zpXkvKvu6a90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=lKoJNpbV-fjdaOMMgO4mVnKswS_xpPmp-yLGA4ZMBCqPIRxdlJht3xHM9kVz2NSBCFF9MFy9zJJYlUptTbYqUfG-7xUnvMVk2O3G9EFejmi-807PtW6jYF3gowUwFTnN231YkuXpiOvsK7Bnk_8YeVtNvtnRrqh4RBpBVQ29F0ruG7sEvndb_uoRk7qhsiw9tU5-A3FqWLCSnpiW6mCjh3kKbocmMSLfgZIC6e9b6IzIT7HkMtczSxrF5ZVgq9QEQT64yaG9vNzpj3Bk94wazSwPiZABHjSE1Qm7_KSzgxeHznl-JjAm1ADxxzesk0g9j8mVSE3-WZiZkyKOHWUfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=lKoJNpbV-fjdaOMMgO4mVnKswS_xpPmp-yLGA4ZMBCqPIRxdlJht3xHM9kVz2NSBCFF9MFy9zJJYlUptTbYqUfG-7xUnvMVk2O3G9EFejmi-807PtW6jYF3gowUwFTnN231YkuXpiOvsK7Bnk_8YeVtNvtnRrqh4RBpBVQ29F0ruG7sEvndb_uoRk7qhsiw9tU5-A3FqWLCSnpiW6mCjh3kKbocmMSLfgZIC6e9b6IzIT7HkMtczSxrF5ZVgq9QEQT64yaG9vNzpj3Bk94wazSwPiZABHjSE1Qm7_KSzgxeHznl-JjAm1ADxxzesk0g9j8mVSE3-WZiZkyKOHWUfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-GjYZJzWg59o1C1RGoGZrxmU310jPrvcQ0_vtwSsTXJiQ9GRbaLOPP9EJoE9F67C7ioP1qlNUOXHazVc8cGTQUaqyWzcTe7jMO5UHfteGkReLleUQ3GSxyWLjFbSxLQTaGygNzOQ7-2ih8ffHYIUX7dOe861_nFFbxZHzMi78bHLXCoGMfyVBvAfixKHO1ZHWd76pdBymKG1MflnGCiPexdY8JSAO5_UBnEWuPwfq9hbVP-Zo9RYnd9fMmnWuwescgoXE4UfF5XNoAWIVV982ijNzP3Tuce6RMw9zurUhBzucMAtLQ0bqEWoeljpubuMefN3-0z-f9dHmPVQ0MmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkWuExDl37xQWF2nr_dH_tSrTSSwR-0fHaZWrThAFRRMPDoMToyzqbEbvKrjybI1yJgp1A3dbotahJhArFs9aMi7QtPGjDwG7zOzzQyA-Eo4DkCT8jVRCYvIA1q9CqJH4jy4qAf_4NMfQkuPUn5QtWqBADWWVgp-6AR2l7zwjzcQXzSrAhIvdhijOez4USM6WVeeKghGp9GKNR1CdfdXUcxT944ii16N_4-s6D3eTEDrapdwAJpWSAdpoXEMkzqslY9eh8iFsFxtWKlDkujOyD-63wBclC5wfQuzPHkAX8l4eDYafWEekLxg91fRNcjR9AbvLw2fkLxSfs_jjR5Jgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsHzjcHu7GPNG89PeDztBl9rvr14eYP4XkwrX4wnJyCC7Ljndc7h4ewJVwtYKiWtAUYtZBd7xRvd5sBe5HXtcw0p5x0u0RABBq9Jk2FEyJHNujusJ-5yGHNBDF5lz_irvEL8VUZiHtCXoAwnYXtu_7dLFJ7p14Cvnik7LsokaaBH8ItlzfTKrk7vKYsK21c-gbc-d2JWK0RlNpziMUvqbmpNHvPwWMjI1PJZwsUA6cgstDmZAKZbL4t-AQxFnw1YBW6Yb_6LzZV2O5NOgi6WDBu_6gH5EoT9SaCFQZBz0x5hxCbKzYepEVwuzUVk8crjBD_jA2S_Y0KSoCpUsaXwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_BuCT40CWNDL22Xwat8mmDcBsyz0AFe6eLCEjXKBWfRjtLeSYQHw_qbRXrok2qk7KgqMDonxITQd_r9b6woLCZTCgebxqSvqZZ1T-in16VJocV1BJZE_lnRiNkOBYBafDbtZKASaTLccDOPt-Tv1gy2G1w6pWH8Wxa1hsYUfS_n-VivY5jKVx0bvs-kiXoZvupjj8k29d5p8cSyiQk3IcvKSyohfQ8xyD2Y23euz8NFJusPu4jm4p9Z8B1rv8QixB0CAIcZIDbqbiyOTpcSEYo1l_vc8QbtvwSPwjJyGaASx1Fbn91GXhVZsgG1jOhHIJqQRw6-5Sj_FgRIF2UE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=cwIie8ObVc-TVURk-H7kLP1g7k-uBEh4IPsYkQlxZ1AIUbpvJRRImcQ0lR-yi4OImFZcOg2x3NX2elMLV9t6tqEZJNuomqtIH_euiwANwg4CbEoyCwBmazw2Iq-iv76ZX5m92u75oGpdqHagIARpE66vh-7AmoZd6BoAEj4D3zCzbR93Ci5pBmpwXTkNBezFecjBFAvx4mw_d7z2VYP_IB7SHI5ZhIQjpiM2MhFmZvMBReM1pOoIvwzhRT3pGABIq5WvbaLtsNKxldeTlBTVtu3JPi9gldWjwYb9CH0RWMbTDkMkIbV9Ty-p0VNlF19f-Woh-AzDhBz9hzQNDL7Lfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=cwIie8ObVc-TVURk-H7kLP1g7k-uBEh4IPsYkQlxZ1AIUbpvJRRImcQ0lR-yi4OImFZcOg2x3NX2elMLV9t6tqEZJNuomqtIH_euiwANwg4CbEoyCwBmazw2Iq-iv76ZX5m92u75oGpdqHagIARpE66vh-7AmoZd6BoAEj4D3zCzbR93Ci5pBmpwXTkNBezFecjBFAvx4mw_d7z2VYP_IB7SHI5ZhIQjpiM2MhFmZvMBReM1pOoIvwzhRT3pGABIq5WvbaLtsNKxldeTlBTVtu3JPi9gldWjwYb9CH0RWMbTDkMkIbV9Ty-p0VNlF19f-Woh-AzDhBz9hzQNDL7Lfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=hJkBdEhwNrDmRtwJ4hUuqXi-CKjY218Ml83daDMn_fqplI9bfxzTSSVmS4YvnVznI9XNAvwLYIZAq_yIZOqoQp9NnuD7cpmvJV0uMkWOOE6Xxh46m0uraEWkbFrw5USml4UPlkOGYIPig60zPjYIGuK5BuxjarKu2GBm26xO2CYhs5bj8YT7ABMrFpPpAo_gDFEnhUfms4m3OhVziR5mKlb8p8RRJy2nRrb7iG2UO19dggtdyQaOQGH8KAfTIZw1ordXQGTbMJA066X-OlB8tpCe0HsC6l3XmWCJvPnyuNK2ZfXy5he7ac_sMInjqvem4jrh2dRiyUOXRrUvZyQDoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=hJkBdEhwNrDmRtwJ4hUuqXi-CKjY218Ml83daDMn_fqplI9bfxzTSSVmS4YvnVznI9XNAvwLYIZAq_yIZOqoQp9NnuD7cpmvJV0uMkWOOE6Xxh46m0uraEWkbFrw5USml4UPlkOGYIPig60zPjYIGuK5BuxjarKu2GBm26xO2CYhs5bj8YT7ABMrFpPpAo_gDFEnhUfms4m3OhVziR5mKlb8p8RRJy2nRrb7iG2UO19dggtdyQaOQGH8KAfTIZw1ordXQGTbMJA066X-OlB8tpCe0HsC6l3XmWCJvPnyuNK2ZfXy5he7ac_sMInjqvem4jrh2dRiyUOXRrUvZyQDoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCZoaxdsfKWirr-3VxNkVTuci6WQE6yrngy75o3XWF3RNSzMeL6MDnLG0zuDfzhbv9eXisT6mdUiJWHMBrSEHcsNaSOhDeQNllkQFF9UHvsrYROiy8p1gAeDTwO2oQISW_sDghbz84Iui2WTI5cwI2a-Zn1--q1bIhKPYjXOukSwt16MeXBIB0HndgWIst4YmD2GI3GzEw7c7hXwQZz8aL-FX7-scf70eSlPH0MLB-D48OGi7dkxL9g-3if1EWYzFOTsls6BupL-X4tAA5aZhJnMmHZYm2Qqds7n6WBWaA1MXQwdz3mlRADSmlN23tThUnfmf4olAx1v1elvyFPHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=OvArqsLK62z7iYf2x1bAlRbkNtoJHgLXNNvsDh-cZ1revIWfBDRHrZa4m2xVVBnGEWCRzL7ccK0Z7zXOgoX8l9GL4noGPWO6pxGRowVP2GCD1Qxb5PbgMnm_g6XotHCBAfpbh_HC6nrk_5ewD18ka_42tgqtD6t-ZmWtNRkWweh8AJ-TVGasJGQ9wxDo6aA1Uzo4mVCvcG5n4DkmwNhKwFJp0hwd80EK_BsdGDRRofOW7RGk43EaVOK7qsMz86rO-eRrAgXpvV_9lLi2NyC43iglxFTUKeEcaWhmahWLbj-Nf_nhWFccwzUUiavtg-tEEBvfKrreItANEa4h8TXvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=OvArqsLK62z7iYf2x1bAlRbkNtoJHgLXNNvsDh-cZ1revIWfBDRHrZa4m2xVVBnGEWCRzL7ccK0Z7zXOgoX8l9GL4noGPWO6pxGRowVP2GCD1Qxb5PbgMnm_g6XotHCBAfpbh_HC6nrk_5ewD18ka_42tgqtD6t-ZmWtNRkWweh8AJ-TVGasJGQ9wxDo6aA1Uzo4mVCvcG5n4DkmwNhKwFJp0hwd80EK_BsdGDRRofOW7RGk43EaVOK7qsMz86rO-eRrAgXpvV_9lLi2NyC43iglxFTUKeEcaWhmahWLbj-Nf_nhWFccwzUUiavtg-tEEBvfKrreItANEa4h8TXvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=KBypWDRfz28bDGDpoah0WkkYRZrNj0yJXMABjMsE6yy7nNnEfAOQcj9KOMkMDAPKpAWcZH9L3vbTQiR7ZA3o7oIcHrOgkBiTxovJIWNODDahxIMy6SRroSNywbpHU_TUvF5mGb5BWLStnVwZpKDHxcQg5scNcMF1oqJaqxeByHXqG1AXQxzzi6tycy-2IGDKTtw90Gfh3KGX7bG3VLdwJBHUk7mw8kQhkt3K4R1SVrFpqJIhTiK7fRoVroGPmqEuv1mtSDR6hy_yDuRPafhQv9jMF5hb4YuoKBHjW3JC3mgHNj1zYtVNn_ESqdEHJxZgYRr8CJQlkfT9_OViyk2leQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=KBypWDRfz28bDGDpoah0WkkYRZrNj0yJXMABjMsE6yy7nNnEfAOQcj9KOMkMDAPKpAWcZH9L3vbTQiR7ZA3o7oIcHrOgkBiTxovJIWNODDahxIMy6SRroSNywbpHU_TUvF5mGb5BWLStnVwZpKDHxcQg5scNcMF1oqJaqxeByHXqG1AXQxzzi6tycy-2IGDKTtw90Gfh3KGX7bG3VLdwJBHUk7mw8kQhkt3K4R1SVrFpqJIhTiK7fRoVroGPmqEuv1mtSDR6hy_yDuRPafhQv9jMF5hb4YuoKBHjW3JC3mgHNj1zYtVNn_ESqdEHJxZgYRr8CJQlkfT9_OViyk2leQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=dKNOa0ON1Pjn4RtHi1Elsl0grlP4wlQqigiQBKERxmnP_cFhQyzlUEVT5yEoi9E7yVSRA6W6evPzUXmHeyySPiuCFmUtLIVgjgQsha97-tKJifroPzMNPaJdJiABXDwzFU9SIJ3Zfhic0MAqwsQHok7nSfBxYrRrzSL41m-KVziYbw3QktLMYjHqyq-jayo8pZq1_k_tndrEkLb4l6vzVN3CPxxxgdepPfbEGYZS_cuF-dHflZQJ1bTkNr9uXTDbz681vzWBqFisKGhbvosZiYmgnwrJCjThTXwMmntBfeqAEBWBOZNOUTOz5FteCNUqmbxvNZ8Wio42tLrKa09LEbdlf3oPf7ZHgg_Bq-koxOVpP0NJP262mtJyvtNlPTJpFQekoOJqlljJzyc_z-yiWiMaXfDJ6T0eO1Gspz3nXL-I1gvNd7aojInuw69dHRezPsqgZNzBlZBUMcMid62oFJH0x37OZKOQ4W6F3_wdw6jGykt2PZRg8oy0lCuW1iunHBV4BHo7J3ZeJ9mS29Y3uxBCXdvm8Bp7QEzLwWo7S5hwll_Pwk7zqkbCpnW8QY6NdSi88h_njveQaP8VxmUvoqPg3ZxKlXSMj9x4wq2N8FqI3xECpS8RbrCDe-4zS8vBBfsY8HWIflMI_rYciPm2mmXsOtjb7C4vg7ov6SmTzdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=dKNOa0ON1Pjn4RtHi1Elsl0grlP4wlQqigiQBKERxmnP_cFhQyzlUEVT5yEoi9E7yVSRA6W6evPzUXmHeyySPiuCFmUtLIVgjgQsha97-tKJifroPzMNPaJdJiABXDwzFU9SIJ3Zfhic0MAqwsQHok7nSfBxYrRrzSL41m-KVziYbw3QktLMYjHqyq-jayo8pZq1_k_tndrEkLb4l6vzVN3CPxxxgdepPfbEGYZS_cuF-dHflZQJ1bTkNr9uXTDbz681vzWBqFisKGhbvosZiYmgnwrJCjThTXwMmntBfeqAEBWBOZNOUTOz5FteCNUqmbxvNZ8Wio42tLrKa09LEbdlf3oPf7ZHgg_Bq-koxOVpP0NJP262mtJyvtNlPTJpFQekoOJqlljJzyc_z-yiWiMaXfDJ6T0eO1Gspz3nXL-I1gvNd7aojInuw69dHRezPsqgZNzBlZBUMcMid62oFJH0x37OZKOQ4W6F3_wdw6jGykt2PZRg8oy0lCuW1iunHBV4BHo7J3ZeJ9mS29Y3uxBCXdvm8Bp7QEzLwWo7S5hwll_Pwk7zqkbCpnW8QY6NdSi88h_njveQaP8VxmUvoqPg3ZxKlXSMj9x4wq2N8FqI3xECpS8RbrCDe-4zS8vBBfsY8HWIflMI_rYciPm2mmXsOtjb7C4vg7ov6SmTzdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gas1Xj_p78rBoOTOhkj2rZiROiJDLP8abs_WfI6NvR3vTKSrJWaccbT-17KGqaBNPjxhBYpIdNoX3pW3F5iAaDIepesvyBSskfaQAj26fNzahqsc0H5IEQpUCW1ReLNtxDkEfNSsa5K2zYzZk-nqkZIBhoUPCAwg4ogSnsMqv5Rf1HjNjwECEZ39rJRv9Et8SIL9sGXQV-FDJDJuXOBlhw5nMS3Qk1NuAfTHBL7icQBY-UP0Z2kMW_TXIJSzQHyy1ZKwhbKpenNkKxin9XgcUxMjZ6lnVg4p8xvSKyduM241N8vxAcGOJ5MAfimYdw1n7ranMGg46PqPmvGeWxMyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=bPBKlWGh1B7dFpNWNqASkQAqPhAYqsENxRWtLK_RHHrs1wSHW4hwnGSsn_uV6BwMdTSmafs0_uQGIs2xx6Guzikeb_d8Pl4Qb0Lm_J8KdaVfti2jl3ycc7MDHMVmJaDS7zztv1iNcydIsBqj8oY5ZCIXahOwLVxtg-5ql3NnfLy_OkJ8Q0wiF7e2qZRUyfBdafoiNnTBclHW8W6Pg66q9AdqnMDiAW9xY3RdPIBll9JXLgxV7x8po2LRqCBE5hsGKxxrkF1x5aJCfOYeFWWf2a7a9uZVoQ8lsjXZuX3Pu0IbZ_KnXOU-vfppnhgAht9fifxnESh6JQTj9Xta2Q2L9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=bPBKlWGh1B7dFpNWNqASkQAqPhAYqsENxRWtLK_RHHrs1wSHW4hwnGSsn_uV6BwMdTSmafs0_uQGIs2xx6Guzikeb_d8Pl4Qb0Lm_J8KdaVfti2jl3ycc7MDHMVmJaDS7zztv1iNcydIsBqj8oY5ZCIXahOwLVxtg-5ql3NnfLy_OkJ8Q0wiF7e2qZRUyfBdafoiNnTBclHW8W6Pg66q9AdqnMDiAW9xY3RdPIBll9JXLgxV7x8po2LRqCBE5hsGKxxrkF1x5aJCfOYeFWWf2a7a9uZVoQ8lsjXZuX3Pu0IbZ_KnXOU-vfppnhgAht9fifxnESh6JQTj9Xta2Q2L9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIc0PLZXdl74G2ieiwP5L-1zUTwNsI4RAgqu7j_GVEOIgaSaqM5kXhyX5CSvRW63F2_2aKYVy01Zt8XdU2OiPyKh070MgCl890XoUGj5nPB1gd-t9XrltU2HkAe6Z9ZOsNJjqVFiK3QwP9aPMnntzZJKWqjvCcsP1d_B5-xXoGEXz1UnDRH1KYzkIQaDQUQXU5CGffciWEbL1Tyck-cfikfUf7OJypF-O9kPKcVWJJYLbXb3WS7P_uyA1ZZrololUNn_v0G833JzLQFx8NXq-r2u3tVEZxZBQnnOIITfEK0WEG8CPIcglsdEBWMxpU9nwrfPuOQ-bdbqNNCAyTlebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7v5q1SJ37mIqdNAqSkBO4ckDbrp7LD6eWH7gfpyfT7VIUT4hC2OXRhzgMYw8s88uxs6HGq08ryQnwvvWkT4il5oSm2ncogsS0G9LoBJ1ONIVlNVQbN3vP2LozQtg71rTYo9gbaZbUx5aEyiefgEDKx4Lz2g6ky-f0C_PzwCJJhhquItcKeUXNqFQQUEZ4HzDM1yNBlIkr7ykmjKtjr-CqzMMSf7ToZuGIZztQ2KWCS7U5hIf-A-Q36USfZdweTBseqqQyRoTfkv5GtqN8qDpFmNs2X9Y7-9vG2VcDJzI-eJqYqWjihlDREBO7lJ0Lrli-kAHoBySu1EVZvp7K3CmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=Bph9c9R1nx4JlrNNDGJDPJDm6W40_80pY__5zyxr8Gwh19Wd_WdUTVUwnPaV2xRf-C-bImZmBOVHoaciTBJd5GgP1oOlWdA3G7Ct2sD6w0oDHEx4NunOvha9WOsVmmcepyHVoP6dc0QPxwm9-mp1F0EJSLIHyqokvj2oCvgQSi_r7brwi_s8mWcK17_WIFe2lX1UORYzMYHBPzX4Tzvniah8KGbRbX5ddImfdK3-fXcm9Nvlu5QzSmj8crIbqg9mOK47OiXSsuI5kV_lOls4NZ1lXIS0P2O0O74Z0ZB74NV-Ua_-ZAw3oQs5FpQPszdbea-g5C9OiFUmie93PZPQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=Bph9c9R1nx4JlrNNDGJDPJDm6W40_80pY__5zyxr8Gwh19Wd_WdUTVUwnPaV2xRf-C-bImZmBOVHoaciTBJd5GgP1oOlWdA3G7Ct2sD6w0oDHEx4NunOvha9WOsVmmcepyHVoP6dc0QPxwm9-mp1F0EJSLIHyqokvj2oCvgQSi_r7brwi_s8mWcK17_WIFe2lX1UORYzMYHBPzX4Tzvniah8KGbRbX5ddImfdK3-fXcm9Nvlu5QzSmj8crIbqg9mOK47OiXSsuI5kV_lOls4NZ1lXIS0P2O0O74Z0ZB74NV-Ua_-ZAw3oQs5FpQPszdbea-g5C9OiFUmie93PZPQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWuy6gHmSoEshuIsHtt1UagcZ-LYv2xhm62CjB24Duzym6ARuyKj1u6cSZgL7zK26pcfT5HVGuzT__bhG3qQP5HNoMxCELkYgXXAZE8kAy6a1K9qO-rJvcSGdFW22Fk0DmcXEC4RCkjYZhFRl9bOJjxCtvDhbPWN7AZ87i0l10kFZ4j85qvVVWKRN0neaw5LFS1Bvi2meSOrbkvxqh3FL67XRWVdSUIL-OcHznQhZzM8jhMSZou-zbgrkNBq69wqMF4lRKU3kFvNHp6DxyRVZ8MKSoRmyq-qQJQc_YcWBCjIQo2_f0t3Vo0REb8KvLgtWCfTnl8lH_cYm-1v1M42Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=syv69s75FJr9AUZbqP5u6Y4ZD7tGjs7x3TjPe9uhbPYqk4v1rVt8Ac7WEqLW6JppXbx6rT_2YAtyl-zBkw2utNSPoYIsb0_Tz3bp-EMT4e2L8Onizv5n5UOS2VHgqnOWknvooL1_eixcxNjypMYcPIMIg7IeFeIpiSxMeg9UKqPWq84v81_UFvc9K9PBz8136wNzlN7OXp5sACFLu5jWs3JEWyLsEvNJfkQunnhA24NwDZeteTPlzV0ZMK9ULBhuCYroatq7eNhX9Q_etCN3u-WOWMJqqBNMP0ZPFvHn6YNw1QN8fzm-Ihfc6qVBDTCPMHVzG1OMDeEyWXOZu1Rq3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=syv69s75FJr9AUZbqP5u6Y4ZD7tGjs7x3TjPe9uhbPYqk4v1rVt8Ac7WEqLW6JppXbx6rT_2YAtyl-zBkw2utNSPoYIsb0_Tz3bp-EMT4e2L8Onizv5n5UOS2VHgqnOWknvooL1_eixcxNjypMYcPIMIg7IeFeIpiSxMeg9UKqPWq84v81_UFvc9K9PBz8136wNzlN7OXp5sACFLu5jWs3JEWyLsEvNJfkQunnhA24NwDZeteTPlzV0ZMK9ULBhuCYroatq7eNhX9Q_etCN3u-WOWMJqqBNMP0ZPFvHn6YNw1QN8fzm-Ihfc6qVBDTCPMHVzG1OMDeEyWXOZu1Rq3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=B8UQSOXNzHoQ6OVwPFESZ0LLdLH9kxE94PS2AYAx72iOEe3JJkbHlLAzGmG1AgdVSs4EElMiYh20DgTJqQI5e3AYewu1q1RLdtiJ393PU-1uhP1KWdsS8-T2IURqfiXLtnjDt2PxKS7l0tS3PADF1pdAA0E-uAwqZZFTpr-o8iCKIK2jigeqr1Rd4exJruoMl5fK2ZVCpw4PApdcE9PtEayZ_QjFKIwXnc0Lmx115nWQkz7ETZaulyl6lYoreigM8R_rcQp7VR4VIEqgMXbBDQ-w7eL_GtmoJgYju-Ano0-FVY96D_oqXCHZM90H1uihvTLLW8Ty8rNo91DsaPv9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=B8UQSOXNzHoQ6OVwPFESZ0LLdLH9kxE94PS2AYAx72iOEe3JJkbHlLAzGmG1AgdVSs4EElMiYh20DgTJqQI5e3AYewu1q1RLdtiJ393PU-1uhP1KWdsS8-T2IURqfiXLtnjDt2PxKS7l0tS3PADF1pdAA0E-uAwqZZFTpr-o8iCKIK2jigeqr1Rd4exJruoMl5fK2ZVCpw4PApdcE9PtEayZ_QjFKIwXnc0Lmx115nWQkz7ETZaulyl6lYoreigM8R_rcQp7VR4VIEqgMXbBDQ-w7eL_GtmoJgYju-Ano0-FVY96D_oqXCHZM90H1uihvTLLW8Ty8rNo91DsaPv9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK4uS252tavQgAEMR_Z29qPx-16dvZnOUdXgHLKNt28ahu11udS4BnBREi1LRUTx6ofCSJRGPwbjNGomMhCSnL7aE8vkam3TYpZylQ5Hc5ePiixfavBWicrEBSCm1I6RJOhIeMGuaB5HXzzNJH4vzOxaXBEAPReXwsmZkFKbn7YjmZXnhYKmbYc5rzcl-GFVFRDbLslqNHXqyS8ste3ERNCmd9y2XZ_1NqkdiF3C6OHUq3WjTF01H3u3yXvOtIMI_Xz4V7oRz7DdmUTmy4alTwCSwk2x8e4ROL9pVwmeJdRjq9IbnE64KEozA4DlI14eBq7PABX7vnW3WnPWhE6YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7aCfg6NmU50oimFJxStCGBfySn8YUgh3vwZdX2d37TWJs4fcvyjZCoVFFOW9Wzyw-Uz3T3yK3OUtgvgN_sdujeqm6ygm5Ie_uvFIoUzlNl_dVOKBU05eZ93i_jf5NTQHbtEfktXnXYbyOSY4vqd5eaZaMOPzmfU0KcoCdqq8Yx4L1wdPPyitxhFvjcbYuOXEW3fKQ3w5dGeQGonanKOumW16d8gM-7J8VajRjxGhko8_fp09cx7Ung1SCUDbcFuOFSIerjiR7oWWLPhRwCkYpOImgsXy0r0GIgjEthep0kasPgxxVlweXasIwbYDVtin1-UdJyiCWj2--yMLBBRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5UxX_fg52FvTda7CWTkLZ_JOM5bcPdvuoBdynp_cA7ScqpKHsR88ZG_baEVzoKf3EbmWdGtHWZxCOmcxhEDZvD4GIGPIbb1DgLtFqCMgkJjJrU5go107nEJv9jCiIJbWa5P3RmYUrIITMKaoKChbGvtZWhysctii7-q2N8V4guXY9hAfJg2bZo800h1gi9ijct8uwAn7r3XxiCh941UsaEJ6t7oNTSFiKm3S5udUIg1WXLl0xl2JePUMtzxWvdGca6CctIx6mZpZWLKMjXl1UVuXKCKuisSCgbjrvg8XtOWGOp2mCPyMVZXFrlovtFOKS2ZFFvWPKofpWxmMjCuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=INTVii704h4pBIY-5YpbzRnpx1SuJDujQv1vXt_CJqj-e_gG3hdZnkKsw_vuP1iAG2Ere5wVOc2GarkjdZDQDYnE7moJY84_QF606aAlt3IOecXgMl-vcAu2ysdkX7sFFtS2Hg-VEjKNWnPNvcIbnhZzXzjpGLAr2I_zlOyx-NWe9ujgrSZud0qiI8z9qgAinhOFdHwkOjCAj_6reR9WXrc-xAtQxGvOfJQm7OgI37_72nQXmmZZAi64nUoGejadWtMFscdzZ01an9JtVxOquFb9ztKFSlJ_94iXznYtPPlgvhVYm5pZs3_xhYdcGjrGM70LBqv7X2aMNv9b77zDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=INTVii704h4pBIY-5YpbzRnpx1SuJDujQv1vXt_CJqj-e_gG3hdZnkKsw_vuP1iAG2Ere5wVOc2GarkjdZDQDYnE7moJY84_QF606aAlt3IOecXgMl-vcAu2ysdkX7sFFtS2Hg-VEjKNWnPNvcIbnhZzXzjpGLAr2I_zlOyx-NWe9ujgrSZud0qiI8z9qgAinhOFdHwkOjCAj_6reR9WXrc-xAtQxGvOfJQm7OgI37_72nQXmmZZAi64nUoGejadWtMFscdzZ01an9JtVxOquFb9ztKFSlJ_94iXznYtPPlgvhVYm5pZs3_xhYdcGjrGM70LBqv7X2aMNv9b77zDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=c1LUsoEbg7BWsupHQkpsGv4RtOWmm8vACp953hpfJiDxg2aEweBIE01RnDGkxET_6KWkpYWBNzTt3VVRt7SAvbO01gJCFKWtN_VCgOkmxeVhGylsRAp0dzesGzj8Utt70F3h4Z_5sRmAknef3XswvK4A8mbylBAqtV1MsqRLgU0KAdjkuxtqywISgg6S-uswyoWEdsUaZKoM-r9EO7YbNCtNudemMEC-nYT_0Nlw015Nm07xocyb4gMg2NyF3OCDzfqKyFlBluJviLL5hPrjBcHh68HWlPjTs0iMpM0QsByfd_f1kX7Fo4DjnB9WPkntwx3TIh7eSSqC89GV_mCG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=c1LUsoEbg7BWsupHQkpsGv4RtOWmm8vACp953hpfJiDxg2aEweBIE01RnDGkxET_6KWkpYWBNzTt3VVRt7SAvbO01gJCFKWtN_VCgOkmxeVhGylsRAp0dzesGzj8Utt70F3h4Z_5sRmAknef3XswvK4A8mbylBAqtV1MsqRLgU0KAdjkuxtqywISgg6S-uswyoWEdsUaZKoM-r9EO7YbNCtNudemMEC-nYT_0Nlw015Nm07xocyb4gMg2NyF3OCDzfqKyFlBluJviLL5hPrjBcHh68HWlPjTs0iMpM0QsByfd_f1kX7Fo4DjnB9WPkntwx3TIh7eSSqC89GV_mCG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDdkTWIZrzDyC8fGlOfWg6rwvZHdMj1BRtIVDcpjeZSSCRux2wiIOVWNj-VmW5WttBAcwzAZ5jga_rfjudnNLct8y3S3Y5yRxaW82G3Tsebokv3kl1k1P_Ci0u86JQQIcVQx-_7yXkco3ELcq7CDUHuorVoBEMsx_5LD86By1ZlObMqe8VqlyBMtuS35HC7JSTkKTX2ZLdGUW3IHRIFYomx3XRDbe9rZnvMj17Z75W4jgxhQMWR-DZaQpWA3sA0tExJuD_2aJ_KRO0r02FwFQa8XtWcb9WeArKyGx51POWeffYASLrJte1KvIT8i6TSLnJsEyMdNJgwtbTsBNkPzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku_PgEPCVmvGtQincyajy8mwDj4lTY4vgw6i2KPRJoIHLM4-L3PmYR8Zz4LViC6160rLzI5n2-wyBj90R8l0BwBMA3FkuIrIFwRFKSeC8I2yp6LB7-NCHVHx3FBYXVE6ZQD0DrefqEOHEUoXvH4AbCTn3kAg5fS4K9GKULgYzR5d-dlzoao14Zvfk1aVSXQ2ywS-bPqt3uveeRL__UdWEIY-l1ojXz_JkIZ1ayt-nzf9gD7_7KpM6xgIZgMFACVu8bscppXz6gAAQK96OzyXJihcJD_UZI4Cqr5Ffd99yvwGWFd-dSmRF3YjRrKtDHf5TrcwOvBKfv5qkgEB7fR7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-tK8_-76Xvss9psgfjm_UJFwN3B-4Vlk5NzlcgbZyLIWWj2V5jyIYwyqqu-fYT3QzP7ep7B7OqDwEJ3TsjqS05wtz6-6gd68-hAN67gzXAf-JXRsuXYVWSouT7_mfBbcKRxLU8ZMboXPLxQCKCeB7kgp2hNDw0Jv133jk5itc2Waw9fpoCv1pSE5DvS3Xqhul5BYK2lrszXh604aGVtHdmQ076ubZ-EmpfYiKRID3IqYPE5dr0U7VXp331iDyDPLwffiZ7yQTiwy9qvWR8TMdNQA-iZ_JgPpweI0hai18G2uHdHbRDvJwin-dlOcrgOE-E33_v6EsnNtNSyqjmoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvXOadSCyYlAAtqtlo1UVE01k1KtdNp2EoHMuHIFz-16Yloe-X0HtsSbxvdJBugncjdVHahXV-VSCqa8ANl2goCHRlemMNzAWGDyVBkd9X9-zIx3DkS_EFOuOwiXTwTC-qi_JGRNlg0MVMjs_AlRkB8sx4mj4ZNo-fhkRi6EA4rbSJVCJQSHKyY7BAb_rTZwG3XTf5Pa-4TyBXUnclK8XDDp3hAiUt5RABhnSJXsmW0KwXnV6tvOZDAJuJYHJpqn8cL7v-WY28mXKIPkv3gBOLgGEh8Yv6spMfnxEv7zRgWmvEuuyVwRZwJ3cw23MbjqLWE9OqSdhaJrkIsBQUtS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=Nd0cf4qRIRQ9gP-9003w37TFph_Y4gqMk12_Pk5iMeuV1LMai0toqSafcit_nrlKw-JMI6Lw-A9ADern_Y95l_ixxGGPJAgqxEcZ9lV2Fnnl5vhUkfhA5pLVCmnjz2nTOi0H4iireFqgaQpahAmQyrU9Csc8QzyMYGESKPccQ6jWlG12j3d87b9C_HyQ0UaIZr9VMnYvsocL0Sqs3aw2fmYodqV6LhD21dpvto67eotiTw1x3ojwstTuaQXNAAbtA-VCWhZGtiUw9BxtZDZSl1qc7XolPd701rG9iigMfTGF45I03NKc4KlKEWgzMYah5AP4kQxQl_AcDqzmT2ZvJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=Nd0cf4qRIRQ9gP-9003w37TFph_Y4gqMk12_Pk5iMeuV1LMai0toqSafcit_nrlKw-JMI6Lw-A9ADern_Y95l_ixxGGPJAgqxEcZ9lV2Fnnl5vhUkfhA5pLVCmnjz2nTOi0H4iireFqgaQpahAmQyrU9Csc8QzyMYGESKPccQ6jWlG12j3d87b9C_HyQ0UaIZr9VMnYvsocL0Sqs3aw2fmYodqV6LhD21dpvto67eotiTw1x3ojwstTuaQXNAAbtA-VCWhZGtiUw9BxtZDZSl1qc7XolPd701rG9iigMfTGF45I03NKc4KlKEWgzMYah5AP4kQxQl_AcDqzmT2ZvJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhzLDFAMNgEzh--KL6QkP_2g13OSqEucDk0bv2wrCOdUdn0SKpQ_5BT9Ja_mMOCgY1cGi78wlwMj7XUWNP96M7yWSKrbr3oFWsvIONJjuFIm6EnG-SbMsuAlIQ_TazMZSGh-XmWsbfgisP4zKKxdxVMkBdXrxSLXJuCiq8LZBwHtu7fSyyKzTTyNtab7Hc_FRj612fN60Ap0-ZYRFL9BM_VPmPF1b48XnvVrlVUJjC7d5P1HV0WnOuGHykQUViC2Vf2yP4gLoPQ1n31IfHYe1_R1xOinHXOPZz1TmBPRPSQm-Du9zmKaJCRKGkaR6IGV4Bf9XzcEeXnK4OE6iKrn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUi9w4-XiUyJ-VoiGZbYAmTL4q0RuSQPk-ol6MI1mmMhf9fpN855bENOAxsc0-qBorSJhy4u4TSn5EwkuT3R_qoH6N17JYdmC3Wyalc7v_WXuFhBjys3dL4pG5kAnjS_A2SacLXUSL2PLJS3Qa6aZQVc4ct8ZqzVY-FSUc1jeRSb-RmDAH33GnTFLWzdQp4N2TD1Os5o_zQkqJjsKyYNm-7Icu71431zsfiN54m6i1EegkbHaSxv4Y8N9XkbOTNnq9C0LA3cn8ANI_IWxzMUL5KrX8v_vQXASyM3UIXOnyAw2mcFYkFwqxbxzHWvpGFR6JCtKoMJE8TiIDulTZe0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv2b9koGV6DwSFpwBm7Wqhta2ZsCTYTF2KwqtBfzN0jOHHBX1764RDGaOppZFp9XppEgAhj6qXO2x4u3CYuqX89ek7KoSY1LyBjVLbdfzwQ3VXZUQmNUY_Dx76WQQw4deVFvxnQU2xqUXI6RY8gMPcXi11bkAjH4up8fHUN0mXCp7p2iaWTLvkpJpJ_06A6qpPqSt3oINtCHcBJ-UCr2M98TELLIpc8L0fiL9ykQ-XMgakww-OSZrEUkU9nKQM7K8Fee4A667J8L-kWDtQKq__WYnc5zQTVGocItCah5EwISlDi_cPBA_3h6P5H5Hxj4_lTx_r5wZJJCfQD3c6SkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBKslvfHk4RYYZSelxImw8wnKJwTupesivXJIFwTi5WMV0-pWU4ek5gC5HB9WfH3PD7MtwdvNSId3w4Ow-7zp20OLZh8Rzavf-aUhfTRudNbz-gJi6iyGbMnV9KE8s4CPJUSW7Z7yBxJ5zz80auFwSmsGrsEzVBFkVUBEOldk7Oxz7-o657czYbc1pKuSpPE7DpF5H9zvvHYSmLvXYBERxE-_o2PyYFQ3DtIcZ4SZNx-xyNJrYvvw5jg07Ebpfw35uYlnZRC3xbPpi6L23CVaBBc-CdjwIxKsqRYbfy5yRPCXIURksxnn7foBWj7dXEiQmIC53vLoQKeGT7qZMxdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd0dHjvE-n3QWT_qTZ1uG9Y-g2L2F94Kt763W6Q9wkWzhC3kStzl9yxL-1Y4IekZe2QqDeJXg9eA4P1bsdV0sN8GU15Cj9thxEV5LaVRMaN8azJ2XKwUF41xO_mMMhO3zk5AlVOQ9AoUqfK9UWz5haJSBp7tTZIA2sZrawPmLtSMEZfLwp6xE2p0f63m2Y-9RRv_yQxToOTe2tbZja3naO4vNzuVHso_vOBylevbQoPj-I2sluzbEe7JA3bQfKuuHdHnBcn5W1e9yvOwPH-O2rcFqTVRLNFPts0T0vb6_StT0a89qIp6faHtHueb2iLpAzgnzeHl23027bXOzBtPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdi8sJttSGpgidHS7Pbxczr1rpUi0KfnkZwFUApV69BMXWrpRIk25UiVdAr2-BJ9vSZ6MQvqHmJSdH6t6_iCqUAya8j-6R65UHZuZf-RRT3VvbmqlhnE6bH8jVgsfdaJFMu4X3EPmSKt0JABHeAMbbo63Ap5OP5hRFgRXEU1ZVeRV9nzfn_e4zLNpEugOdgxlvHuBXLDUc9O0PLufDVCf3FmI4SQR6KQ8JloOxSVoq2AVxsy2qoPD_nbzfVvv3u6CvnQHIMx3Cd5hMf2ZxHxg_9IdPo4rkOrDw2cOKzAzOQcx25kxJ1tZxoWsT4RZv6qsfehC8gpjCc4I2Tw3qFL5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUpmZhRb49_ZkL08XsKaJGg8K-j_hsP7o4Fq4YFn1w3SO0tSVZ0an_28GQjeZ2L-h91sji1nZJ_S8f6iWgGIn-u-10lUFckJZ8tIurgNecttKcNdV5I-7KhWbcrJ84nfQNc1e4I62Pb0q6rzPmt6tynQwjRjYB3jIYO05AZ_t1pXZQIiaUdeCtdxd3BNTfINRXTqTIc8mWiI_rpkzvzhc-81x74DZu5Eg81fMOIk3V7usO6rlFIJtdr3rjQrRW5hbNfAH0G0rWFB4aYsZs2w8t5Jj9us5qJ-5vORKaiReNatftX3ulISVg_PcbKF0OOd4EwdtjTkqOCEHxbbl8GG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG7AS7j4hNe_Az4nBa4FzN-1Vk6yZcPbmGcYRAYAYboCQEF3hCDWM7zQquolVleCxD3S2lPiqzMQ2ciLWBwsOqnYbgPm5sMI0cqrRNkQvIVs10VuRyn_jV6oG6vP-yVVuutCho79SmKWNqGRNlxu8tCkJTTxuHxOPZjFKFKaWI3NorHllweT2CyXsMtJbXWrhTdTniIGLHeF9cssEG012vvM5dlca3aPUEAhzoVABd25Me2RMMW2d2HyZHOjkKSTOV43RBL_ezbeo_ijqyUWg_QrbhEvlDx2hNywjvic-k0nAY1Y5SpWtqRFGY6cUAAAfp6jHnpGwcxrjg0X9X8NFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyDmuYR_T6feMNTB8W0bi_HsktC9EeD-wgrMEYnewbCwfMPUsW8fkutQ_cu8EUGgRWcUXRreFeiJ5DWaqgfEglXIXCFupEUwueTkSP0_zjR2r2Tznu73zizWdipn1NFXzXyVs0cJX2jd1KqnpsHuihBKdhsz53TuQQwd8Ip9WiWJ1UMSwvwEYUo9TAH1vdHe7xBM_TR_CAXOk8areFQaqtU9lZ-vMnPQD50wkX9OuAdgUshzzFnkku68veb40YyfuKTDHIGGJOPx9bTxDNT0YF6ducHcugmf0myiy-dqMDZ9CN8Gn2gwwLzI1-seNHmW6yMd7m4WgTdJFzdAYAhUqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhGpQrRjnTLE55HDFdQgisPkKDYa8j4cY83P2kQrIOGki6gIW-q-LTEayydh0Vn34X1XJYb8RekqjYpyFAd3y1JNxOn2T9XXsgPmTPL3swFeMekO1ooldBCjLV83AztV_zt0dwN4L-v6-Pa3nTJJzaHbdRVHye8mT45Ny0mef7W6dJu73pmcllL_lJfVF7NFEXvLM8h1XXV30Mu78sBYDatlCoxeD1JS9Z8QnsxlruQUq48XHqocX3lUhF5zsp8EAu9utt9EXq880d8bD_bXX19s9DiKPftErlFPoGPfoVNuWMzwAtN4I2kr05xuPU-iPQfmbfp3E4-vmd1VAvdGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE5D0qpclFY40_aWeEbkWq9E1u6BrjyAgBSkSipP1CRoOFYR0sIND70Dk8MPzbpTxW1LqQS89L1JO9NccN28e2K9kCgEB2O8O9RgVy81SD7E1_XpwzK6gGg7qa1S6gmGj43Xyyxml1yfWnPiJWbYyOQZrpirREkP6zFkOGOJ8IOGEvkl5_J2pAQ-jVVcP1bkKVVnphwTYvWh9B5cb8WMJRRt7fhdO4ZHu0lGCZizP1ed0E7IcyPeNZEFBW3WNo9h6NUIEDS4Pu52qyzzOKr7ZC8XiZKVTsc-aKWnx8Nyw5enIcOyxWaUJ6v3KnaYUFh-GFg1DnFjo0_AaOiQHfAjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
