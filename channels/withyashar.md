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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 352K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/17035" target="_blank">📅 04:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/17034" target="_blank">📅 04:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq_EXiUq0rjEObLsta3yF0yiZ9LcFgwSm9r6ne-Z_BlwJ_u6UrQRp2OT2g5188Ym8hYbIS8z0YYI_TI-KJuAZK3AhYAr0mM_cD6i7f4Ae8bP1A_-Nx5uvOi75v2B8W_oL4mYSydh6hp2R-rleNsUbQwPSsVeOwpBIiHfRuCxq4CP1ACIPLFqG8f7FsV03ZWyiPqbKZypVDtYUNsc3YoIMTmwRG2O1-1JP2JNPeypglvjIHhdM_Sujwnl3TXsQk_nhKffsjeEQevx4q9iALmoGWYcJwWE9KA8_ZAu7hlkbcScnY3aCRmVjnAZDhvjhCidE5MzijJDAvRrRbJrdhyxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک ۷ تا موشک از سایت موشکی خورموج بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/17033" target="_blank">📅 04:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG01WlyL9YxIF01sojQX6z9-h7xbCxbZph18NwTH-C-REbzPJFflgF881hMuIfTqp2WEhiaGHRyIADQxLDXIKKtBMd_-yeTsBPHVLjRZA2Xn0hsn_SEM-0-LmJA-LKmeQ6fo1WigFqwUqEYYWrjkhd7eNjxxrHGLCmuAD19pGhARp45XAgQQvdK2dlchpryQ70gf2Hdg7zhTBkU_3yPizG8Zw6MWo_nM0js887uMhJBh3d-miouEGUWSOeP8paqRF9mj20PNFDmNg8LFyi6dS_Xnf7apjImBwrsEeb_4FaUsDa-_1WWl2AHLrQvlSvZkk40-U6isywad9R7VcysDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از شروع حمله ۳پا و شلیک موشک بالستیک از بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/17032" target="_blank">📅 04:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اتاق جنگ با یاشار : ۳پا یک پا هم قرض کرد و حمله رو شروع کرد
😂
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/17031" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بوشهر دو انفجار دیگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/17030" target="_blank">📅 03:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">از زاویه دیگه آق قلا @withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/17029" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=Adn832l3xlOBYWvAzv4Eo4MQg7FtpTzRkTF8WM-6m1vmAJnNGH59mn2oevaTp7l3jKpVxgEw8QlcxjpVaOpuV-eXc3pEfX9PqObyzO07ocClZ3ilHH5ToxE6-wh28OjXlVoqcjVhpdPMupgSYcmb2taqQ5bpFMEhL0_zNUbFy_trkFya0d5uvqDCDeqjluP_7wE-M3kXU2VEuV9w3gtTfBwDxF9Yh_Zo38mJdszkZSUjhxFMD0XQS62LkbqiqcD0M8JE6e-E2x1PVyiRmHktEU03a7zJeK-cRcR5AfSYyEK1YyFHi7bpDGF5cqb1KC4t7ENO2qLz_CM8R8Y0Pi487A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=Adn832l3xlOBYWvAzv4Eo4MQg7FtpTzRkTF8WM-6m1vmAJnNGH59mn2oevaTp7l3jKpVxgEw8QlcxjpVaOpuV-eXc3pEfX9PqObyzO07ocClZ3ilHH5ToxE6-wh28OjXlVoqcjVhpdPMupgSYcmb2taqQ5bpFMEhL0_zNUbFy_trkFya0d5uvqDCDeqjluP_7wE-M3kXU2VEuV9w3gtTfBwDxF9Yh_Zo38mJdszkZSUjhxFMD0XQS62LkbqiqcD0M8JE6e-E2x1PVyiRmHktEU03a7zJeK-cRcR5AfSYyEK1YyFHi7bpDGF5cqb1KC4t7ENO2qLz_CM8R8Y0Pi487A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان هوا فضای شهر چغادک ، بوشهر رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/17028" target="_blank">📅 03:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">همین الان شهر چغادک رو زدند
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/17027" target="_blank">📅 03:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/17025" target="_blank">📅 03:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724fff2286.mp4?token=IDy-97_JQnQB8rS6cCNNQOJ9AIhBPPvdmwg75EB_YV_MgH2_RvuLdg2n9dFxWduQx5FK8LhK4dSLsSL5RAR69YoZuS_gN7f-sbrP3gejxzMS46f3XvKepOXPVZuNgfWM14ux8Zwc60THoH-ucMyDmN-8i0goHUqS_pQVSjHk8oAcrQnnjiCl5o1wnUUVDLP29Qs_MD2NH6-IsJySFDmKrNrlauTWCbtZzveLuIH8b1U65iZzIjS0VkfDP-oaBYzT4lMzotnOhDy6aXDn37W478mZ12jExW6UpcgtCHJk5Cr-ZXXJU4mY7VIe_Z0gPj-1BzUbLA3HZb5i2Y85HWz9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724fff2286.mp4?token=IDy-97_JQnQB8rS6cCNNQOJ9AIhBPPvdmwg75EB_YV_MgH2_RvuLdg2n9dFxWduQx5FK8LhK4dSLsSL5RAR69YoZuS_gN7f-sbrP3gejxzMS46f3XvKepOXPVZuNgfWM14ux8Zwc60THoH-ucMyDmN-8i0goHUqS_pQVSjHk8oAcrQnnjiCl5o1wnUUVDLP29Qs_MD2NH6-IsJySFDmKrNrlauTWCbtZzveLuIH8b1U65iZzIjS0VkfDP-oaBYzT4lMzotnOhDy6aXDn37W478mZ12jExW6UpcgtCHJk5Cr-ZXXJU4mY7VIe_Z0gPj-1BzUbLA3HZb5i2Y85HWz9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل ریلی کنار پل دوگونچی آق قلا استان گلستان @withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/17024" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سنتکام همچنان بیانیه پایان عملیات امشب رو نداده
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/17023" target="_blank">📅 03:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFpm2ka8Sc2md5bTl878GsT6GxABq-Jav16Lt1PATAJ_4oqivxR-r9yJfVW2Si9-QE1IVLTH-eJq6ND9D124ztuHXwpO3rf2BvhtquhnT4nqseE6OCcSVAA3uFMFKDr_KAYUGFJgwSCNehgAGnF9kxpINbHI5PSfKd1A2x6AOGhAW-FgsGa-Sag1hQKDOhMhxJdMIlDtPJ8_-khU3F4qBVE9n4liUij-mmuFi7saGv0DRMUDVq77Wvh60C9Sv-qMLE-Su7FbcOOT5h2jfLm5q_ZvFO8go_7O3ZSaFKx0zPHfFfeLFoBcOxKcaTZIq0_TlPMtu1D5cNpSKUII9zFoYO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFpm2ka8Sc2md5bTl878GsT6GxABq-Jav16Lt1PATAJ_4oqivxR-r9yJfVW2Si9-QE1IVLTH-eJq6ND9D124ztuHXwpO3rf2BvhtquhnT4nqseE6OCcSVAA3uFMFKDr_KAYUGFJgwSCNehgAGnF9kxpINbHI5PSfKd1A2x6AOGhAW-FgsGa-Sag1hQKDOhMhxJdMIlDtPJ8_-khU3F4qBVE9n4liUij-mmuFi7saGv0DRMUDVq77Wvh60C9Sv-qMLE-Su7FbcOOT5h2jfLm5q_ZvFO8go_7O3ZSaFKx0zPHfFfeLFoBcOxKcaTZIq0_TlPMtu1D5cNpSKUII9zFoYO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل
ریلی کنار پل دوگونچی آق قلا استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/17022" target="_blank">📅 03:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUR3YxeZO_F-1hLnX50Ql_MXn-ehet7t4NaJkU-CiSArG-mAXz9-gQhhweojaP2bUz7b-XJWdmnyPiAou4upc5grT5RkFR2zo8gu04lIvCPse1sv16RuTwzdNKcNNk-aqAiwSiFCB010EEUKgq-QYzM_u5vBWENluCCzp0ADz-CrkUzkilJIwkRbpFC4yUbh1gmgdf0etQSphH6LGXwXWEiwiSCJGRnpQNckrHVEwPPHiEXP3m__mewMJQRVr1hKIWlZtGd6RI1KOJGt-Ud3TUJVxedizqWUqbzJEqbz-8vKOEw5AooO_h-7dvF8kfWr53lqEn5A8zPGGcfklH9pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsvwn-NFZAtrBV3zDgNeHaBlfjH1rbrGCgHP73Um_YN-3bhorqlujMN_nHC0HhVqFJmjnlfxqaMUMN20tP05NfhGmqui6TVViaf02ozPSd-X3zERmkGpuprbi9mn7hGpqoAir2VrcuNzQwnEICZoVKHebqYgdmPRtxk5Ph-yG8wGAuffbxM2HsL3gwlWa719-RdDj97BN6tBFgFZCR4ioCGi8fZV038gibwA8HQQtER6xN_b8eSxqp-LRJabEscB3jzmGr1vP3hrkfPypd34ZcU49GZoBWyz_Rk4YNfySTb90qKm3TsDb9GRJzirkwHFHp-VrFur3mH3yPej8vZoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJjfs7pcgNKSr6zRaE3svc0mlhZ8KBpgGS4rpOzc5-O8JPuMYrtpgQmwV3hgY8efy-MlphGYIPE4zvXnvroMLwPHWzZK4h4AS4mRJjaL-yh5tuDEC_90WncpUUhm74DWtUms1U6CM2oxPwt3TZ-In71XNeUS3EKyk9hQrk86z-NlPury8SVAzFoqup5LTU53F9avt4ysiNXdkGHHoGVDoZ0OyqiZiocvazUdd8daxSfrWIKMdANPEVbQCcTIttUXoQWqb_qQUk9MLUQprhj-Z7VkQa-UM_7kl_v0UsTlNZPiWmFu1WM5WkpA2r37_tX2N_i3wu1_lpkvHV3ee1tdIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های حمله به راه آهن آق‌قلا در‌ استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/17018" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=NGyoPCPJXRpZuevyRFH2RGzI185D3TVC8cdsfu5_9GBEHG_1XQQQnlmaSJ__DeMcBNqo0Vjlm3uEVSMjw7LwdGs_aJEIqxW9ceBuXL4k5l6suY5ibLOE2f1rQQE8AYQH1CGpUytT7xBGUPRNfk0-NTynkhkpj9H_uULq7YPZcmVydiJNkgG9Fp_KM4O57lZ6sj6_ksj4tAvYCCw-26B-pdciklLlrvUIYOZUkXaau62JFjTTHbM_81WRMyNNFXK_dq_St0-f2KpEchNA3jnqvqUHWWC7GlDPBN_yBhGLez74EJ2lA_F5MgRS6zEG7DimR4wqMP504VOjSEVmUeAVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=NGyoPCPJXRpZuevyRFH2RGzI185D3TVC8cdsfu5_9GBEHG_1XQQQnlmaSJ__DeMcBNqo0Vjlm3uEVSMjw7LwdGs_aJEIqxW9ceBuXL4k5l6suY5ibLOE2f1rQQE8AYQH1CGpUytT7xBGUPRNfk0-NTynkhkpj9H_uULq7YPZcmVydiJNkgG9Fp_KM4O57lZ6sj6_ksj4tAvYCCw-26B-pdciklLlrvUIYOZUkXaau62JFjTTHbM_81WRMyNNFXK_dq_St0-f2KpEchNA3jnqvqUHWWC7GlDPBN_yBhGLez74EJ2lA_F5MgRS6zEG7DimR4wqMP504VOjSEVmUeAVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود !
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/17017" target="_blank">📅 02:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان میگین که راه آهن رو در آق قلا زدن
! کسی نمیدونه چرا ولی من فکر میکنم بدونم ۲-۳ روز پیش ویدیویی برام ارسال شده بود از ساری که یک قطار بزرگ پر از کانتینر هایی چینی اومده بود !!! خوب الان به نظرم پازل رو حل کردم ! ویدیو رو ااان پیدا میکنیم میزارم ! موسیو یاشار از مثلث جنایی
😁
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/17016" target="_blank">📅 02:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارشهای زیاد میگین که موج چندین انفجار در آق‌ قلا پنجره ها رو هم لرزونده ! آیا تررور هدفمند بوده ؟! هالیودی‌زدن ؟ همه سرگرم جنوب بودن هدف اصلی اونجا بوده ؟ خواهیم دید چه خواهد شد ! @withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17015" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17014" target="_blank">📅 02:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ، درباره ایران: ما به آن‌ها ضربه بسیار سنگینی وارد کردیم و من می‌گویم که ما به نسبت ۲۰ به ۱ به آن‌ها ضربه زدیم.
هر بار که آن‌ها به ما ضربه می‌زنند، ما ۲۰ برابر آن‌ها ضربه خواهیم زد.
وقتی آن‌ها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ خواهیم داد.
ما از نظر نظامی، پیروز شده‌ایم.
چند وقت پیش با ما تماس گرفتند. آن‌ها چقدر مشتاق به امضای یک توافق هستند. اما من نمی‌دانم که آیا آن‌ها شایسته امضای توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17013" target="_blank">📅 02:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9jyd80YcIi34QGMezKgJYaHOHXJC8WwJJEHkAnO-Kz6-QXR7lDuJPxrKa9l69LdMbHv-SC_LisygJpfBU90mgLhR7qte9Wn--50fut-MSUY78BevBq-ge5y74vL-C629_q1z0vFCqGvEqm_N8PErQvzU9zOqX0Py0wSIIAE4a69At_MBZMqyGDbeBWs05OUR8oin8PL4tdfL5CUyZGlmhbzZCpIM3RAgEsm-WQnA9vrypvbaPQVlSzL23l3oafPryLd37C5tWLqxoPYIKZ1VajKGnagwDOi10EtyPyAdSVAZVlnngvIIopj21j6mOFVNkgYxWUyxym0MVXqUrZcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، آق قلا ، ۲۰ کیلومتری گرگان استان گلستان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17012" target="_blank">📅 02:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شاید باور نکنید ولی ده ها پیغام دارم استان گلستان در شمال کشور ۳ انفجار انجام گرفته !!!
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/17011" target="_blank">📅 02:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجار در‌بندر لنگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/17010" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afa943f35.mp4?token=avtiPEpFLV6By8pRw-z40R8anYhjINYHiCXKiQwqZ719JJuVmMlQxU5ftqjVjZuL0r9X_iWYDlnaQJUsuzu7lgnxZUZA9yTKTsA0td5gRnhAvA0Sre1DlIJrIlfpTBEDInreN2Pb3McKs7gH02e49oys3yZx9VQHHuJci8agDcLgi1zWZMrrinknspww4uK4vq3S0hhNSpLfjslqBsaBKgVXZTvdhYvlMCx3CEiNLZz-jSfh2xSUq_G7gbcZseTCnf17bFB7GJw6c4JYVvXDdeXmUezk-yflv-dL5I0Ml6T9_LT26JuW5TEApIrK6_nj0vWBZlAoxqHXKJ6WZCROIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانشهر
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17009" target="_blank">📅 02:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند @withyashar کاره موساده</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/17008" target="_blank">📅 01:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سپاه چرا انتقام نمیگیره
😾
🤣
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17007" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajCGf8HGmRoBneepA817pCjDVy2oPG1kuVu1wcZSLroQBV1OHsrUxdUpBj8rr9RiDsFyoA3XMZ4_8EerP02Po8KY_r-cGf2hT5OZRs4H6b4LvOmJAlmlUoYKcCSfwzqtyOE6WCMulsYo_y5kMMaC2I4yYMadF9rBpu860fJ3rAYk-FvdKrgRG4FeXyZF--HO1UdWPFzBELgON-Z6PDDEJ5xXKynRhtn2RCbeG-xOWuNNPQAc-TkPEhdvdEOemJXSA8iifjO_14k9tuKR1XfSVEfZndlKLIVugmyEyNeC00fZ2h4UExIuDE0Pd_0xOgL9n9dhHDufg9U53g3HXAknug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ما تازه فرود آمدیم (انگلیس)و با هواپیمای جدید نیروی هوایی خود که قبلا به پایگاه نیروی هوایی سلطنتی میلدنهال بریتانیا فرستاده شده بود، ملاقات کردیم.
در مسیر بازگشت ما از ترکیه به ایالات متحده عملاً هیچ انحرافی در مسیر پرواز وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/17006" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با لبخند وارد شوید
😁</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/17005" target="_blank">📅 01:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش دو انفجار‌ جدید بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17004" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b2994811.mp4?token=K8Th_oZOfjqGB602heKreg97IOwC1WNQ1ExAZHeF4kADJbH8MkptZNnpG61eUZI8LY7apohBSUvI_oG3JsHh3oXSCV1wTNzBQdZgWWXdR4HSDtBM2mdfp64AUceUG0nW2rkmE7mDs5Od9jpgmX-73sHj1rvKPNTGLUGvGJ_6Wuyv5-3BpWMuynD6hIg2S8UdYVfQS5kjGy6fCMUAdpMnAfe5kksIyLLCkY3LQTUf2gZx9qsnTEFeQCfvsR0tNx8DFVDkK812d3nGLuiqzifmIhX2I3QE3iNr8zdobxRcg6q7PrBxMczAqJ0MXjAWmZ_3Yzlnc4nrEbksG7mDTHy_vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ظاهرا یکی از تابوت‌های خانواده خامنه ای رو تو عراق دزدیدند
@withyashar
کاره موساده</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17003" target="_blank">📅 01:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17002" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فاکس نی
وز به نقل از مقام کاخ سفید:
مرا
سم امضای رسمی تفاهم‌نامه که قرار بود در ژنو انجام شود، پس از امضای آن توسط ترامپ و پزشکیان، لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17001" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاهورا</strong></div>
<div class="tg-text">یه جوری عکس و خبر میفرستی که یه وقتایی میگم نکنه رباته
🤭</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17000" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHN3_D78NXngwAFGBfP7NEtMr7U4bJruQMx0GgfO1CwLBfO4dZumJjhokfoubjHHLGhOxEqQmPMoyb2n2lDEOFGeyUzlud2TkaidfbSbsbrAGzUn4CuNMwl_mCgyzbCskVMo2oAcdyJPxW0hcxarlKLbnXJiipyjCnVR_T3emSh9M3atjomAcCnsWWJpy7i1AaGINNpRbunG3ip433ribDUR4AhLmh1GXVK9c3FKlT4T3bs_A_G3wT4dvhm9hsPGWj2i7GDXE7ar4v_YnWL2hLKeDxa4rSIghvTsLakpg4n7k2QGBpgdeUdWHpeGd2DjEG7yWFTC14V1ElOY1x1Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاطی که امشب
تا این لحظه
مورد حملات امریکا بود :
از چابهار در شرق تا بوشهر در غرب، خط ساحلی جنوب ایران + جزایر
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16999" target="_blank">📅 01:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/16998" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک مقام آمریکایی به شبکه سی‌ان‌ان گفت که "توافق آتش‌بس با ایران، حداقل به صورت موقت، متوقف شده است."
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16997" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا و سیما : اسرائیل در این حملات به جنوب ایران دست داشته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16996" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3v7-L5x21GKQhfkbu9S87Uhcr57fMaQcwVk9cJnWqOVV0O4JeqZlZ5smbkVKaToLCmk1pHCgkYF2hoJvcKIS6hTyBX5OXSBAp2o5ELsTFcmPqL0-BG-6GhkYxP9-l30n8nlugi5enoQo64XofjSPIIOCNDB7cBZMH0U1OBh-JUXFJ_klOHBMypN6yzW5iTWEdnYOBM5XUZrDcuDZKbVqG0oZ2xKimuNmp-GbUsl6yQ98vBrO2rfzxPyjwco_juM9pOPIa5oi1YiBlH73fwG153Jr6t2AwcnLVsS5ZLAOd3WNoHOSvqrRL7fSpPrzDbaKEECzWHDEK8TabCe6EZ96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر وقتی سیستان و بلوچستان ، فرودگاه ایرانشهر رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16995" target="_blank">📅 01:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق‌ جنگ با یاشار : هر کسی دستشویی‌‌ داره بره بین دو نیمست
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16994" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تکمیلی : وقتی ستاد امنیتی بوشهر نمیدونه کی‌زده و میگه دشمن نمیگه امریکا یعنی‌ ممکنه این حملات از سمت کویت یا بحرین یا جای دیگه باشه ! در نتیجه من از‌کجا بدونم کی‌زده !!!! وقتی اینا به کشور های دیگه حمله میکنند آنها هم متقابلا جواب میدهند خیلی ساده است ! @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16993" target="_blank">📅 01:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : این یک انتقام برای بمباران کشتی‌های ایرانی دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد! @withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16992" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ7k5I1IEwN1FKObYp0avbCWtZkHBQUbG50ovvcFXoWvYiqqpdv31DgnYz0Jad9pnpc1ZJCYCKqCM2sunyZoXgcAB4XWY64IT5xGi69v74zC_sElpQC3bK120nrVhxN-YH9PFIZ94OLLUZ9kzbbYgKZcdu6cwKZPUyWwzGacO5niu2JBzSI7YIDKb7LV0Gkb6sLv_CFhLh2i046F0PR2ZWcixqFea6w2gWMkgOPog-AAh_haAVbX9TeMaY-yp9bKmd9RXGnu1Mm7dKrrrs2I8HkKMMJuNs06874Ds9tuGq-m_aT0AJz2jsxd3tUGpRSI6fecJ7HL79iOwuZJtq9Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار  @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16991" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فاکس‌نیوز: ناو گروه باکسر از ساعتی قبل وارد نبرد شده!
این ناو پس از چند هفته وقفه، روز گذشته به حوزه فعالیت سنتکام در شمال دریای عرب رسید و اکنون در حال پشتیبانی حمله به ایران است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16990" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a052382f.mp4?token=klODfaBZ2PvdQnKflhbjIO0avasmXqig2hRgWWfvCypEtSl93UsNIk0YDJlvqMxCfBLquVc-NFJUmlbhrzAuKHOYENUmFyJex97oW3TSeRah3kK9Rrdj7AOgQJYusRGubdEpFZ-inxlX4_JZPY-bJi-SQdHvQTnoQ2HBboqTDVZ9wAWtB_cf3ckOsLT7BR9m72Qj-j8r0F4LlAmgT-gFw55WGuVe5VtGPKdQ2-HCSmxxXcdaPPGZNAXXJc5myExL7SCGNlhqOT6kKAP_7B2mmRgQgqBViM6lOLTNcE_taFUIX47U_2V8UFtWOWIU4xH4fBtCxIW79OVMU0ftUjgppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a052382f.mp4?token=klODfaBZ2PvdQnKflhbjIO0avasmXqig2hRgWWfvCypEtSl93UsNIk0YDJlvqMxCfBLquVc-NFJUmlbhrzAuKHOYENUmFyJex97oW3TSeRah3kK9Rrdj7AOgQJYusRGubdEpFZ-inxlX4_JZPY-bJi-SQdHvQTnoQ2HBboqTDVZ9wAWtB_cf3ckOsLT7BR9m72Qj-j8r0F4LlAmgT-gFw55WGuVe5VtGPKdQ2-HCSmxxXcdaPPGZNAXXJc5myExL7SCGNlhqOT6kKAP_7B2mmRgQgqBViM6lOLTNcE_taFUIX47U_2V8UFtWOWIU4xH4fBtCxIW79OVMU0ftUjgppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج کنترل دریایی اسکله کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16988" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایرانشهر بلوچستان زدن الان ۳ انفجار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16987" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16986">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvkW3GoK9Ee0OM9LCH0afpUCT4AGuj0VyBaHDa8IJnE1asX6oa3Wy7Mpz2gQ8YizT2ol-CEC0S9en1MLm0CfWLI18Q_lKiCqd8viRX8bB9XM74NcEs15bQQY4NH7hgQx2bCHNrIuwvgvB0j45kg1Nh0YljOLpXK6A-pu13szOM4dFbTWZiQpv4Aa89bnFWpzQsa4oHjqcweXoVSZWeZHRNIrApfsztG2lP909Z0XzaFLApeRw6X1urtFds_PoNF8KY8q8viKGY_Pw4m_ECrqf_-Uq7l2jl6TTddPmWHlDHBvOO9iwXJTSo6dRRps_5bFcTnG4DzP0-6QT8xtXsehjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت : ۱۰ سوخترسان و یک هواپیمای آواکس هم اکنون در منطقه، چهار سوخترسان از تل آویو بلند شده و به سمت منطقه خلیج فارس میاید.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16986" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه های رژیم : رهگیری و انهدام دو موشک کروز در آسمان بوشهر توسط پدافند ایران
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16985" target="_blank">📅 00:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای انفجار کنگان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16984" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چند سوخت رسان جدید آمریکایی  از تل آویو بلند شدن ، امشب شب دراززززززه و قلندر بیدار
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16983" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16982" target="_blank">📅 00:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16981" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16980" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستانی که نمیتونن جوین بشن، این پست رو سیو کنن، فردا عضو بشن یا با یک VPN دیگه امتحان کنن. جریانش رو قبلاً برای بچه ها در وویس گفتم، به خاطر امنیت شما و چنل هست. من از شماره ایران استفاده نکردم و محدودیت عضو میخوریم
🥹
🙌🏾</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16979" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارشات رسانه های رژیم از کشته شدن چندتن از نیروهای سپاه پاسداران در چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16978" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVBAhmSQ-J__I7_RfGB3U_IaKgRa1q9-0OKgDidpvPbaJWPHYf-6gDwaJAKrFp9e34Q6V4ppQFqTw630Dv7YCVftuAbWvKwPzoAL_lT3dK5Gh7-H2X8DC38GS_XPQooK17mTs8ula0e6w2fv9QwrSzEef2Gi9GT9SKIuzpAEJkYfECbkvhpKLl7I57u_g5c-iw4t3NqIo7uzyAdph8AOkp1_xHEr6krUawHaBOvTR0rVFkhw_jktWQTw6cU419fHBwWh_VIWN9V9x9nyK4qENKmz9NwMMHduOdr96jZkQm52h14oy42dI9LtHpaBhCyUQpkWBptl58EV9qwVnuEWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16977" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اطراف بندرلنگه چهار انفجار
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16976" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZifUO8sMvcGYawGQ89tTojMuRe0m3sq2ftEDj5K31CrtAfffcQmy8tCbcXQXg8a6mvuMozjzLxxJNAqHV7c2XYRS_weSEE0c20YmWZU4kv9vWqg9Eq-Dw00WrRf7Xc4S-3TqkmZxiKB9o1RhNrq1Ttaf8ofXwMQ_gU0ZlUDbYlzsrgRrfVCyahdECbfNPIy-GFnuNF6lmEQoQePJkdIeyA8nx6jmLx25FVHtJownWAFHQBCDFUvVS5ZKeWGqnv8KYiOW5ydTzPFJaVeEQU3zGtxfM7UWWFPsxb98hqNuA-EH68w6IfZXAhV16OYrh2KXJopHlVBsbgfrAIJiRwDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16975" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tebLZDkg4J-q1J2zhykDpqevqzwsWJ_G1dkjTWrHVhNhyCtCjmQj27Pyuovdlo1-H6bUm9GEtJf_sRmSgW-4CuspLMbOSzBOwLoSiZc4_t-7GycBVhRPdRGYtkgBeAbleadrvAEomK-yXoEMIflO51loRTfjqTjHTN7gXf_pUr7rxAf25T8BdQN9V0LIuKPsXvNPUgzwbZxrAn0SIoBjnWkE4aDenXRPqneGUuJYxjtpfC16NbvZnx3mKrMSl_1_Lrhol4aQy0YrlAKnWN_3f66FNdRDyP2AUaqF6CX81cykatbaWkNc2EcUPgnAr4u5WbiKiR5061OM-2AQv1P6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16974" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدای انفجار در‌ جاسک
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16973" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوموسی
‎
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16972" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار صدا و سیما:
در پی حمله آمریکا به مناطقی از بندر چابهار، ترکش‌هایی از این پرتابه‌ها به بیمارستان امام علی این شهر اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16971" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=uGAj933s7E9BYCVIz-aKNK34Xg1Wp844ek07d5996st4NBUVPRYUSbBxvaddoRHGnxhc3Z-jDGgX0SYf7S-XavdTTQJZXNj841L4g-nsWd7ej7r5iVcRGepY8RaQBMubc9ExLyw2C_K-lUtL-nwgG4YqVi6M5g-nHL7Scy8piIj9gIdBR8bPCBkdu2YsYvhELlhWAoHZFlsvgStpp0P6uN93udaOUB8k4xJl05a6gV0ys4vEtrzbjxNxQsGfgw7qAOSmbLxJ3Ea7Z-OBUTsE1qRdysMFU5nwlg8u0GCTkL5bR3X4KkNaVEQdZss4R-69M5Llx0yRtmN9pFs5ZdZxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa18193a.mp4?token=uGAj933s7E9BYCVIz-aKNK34Xg1Wp844ek07d5996st4NBUVPRYUSbBxvaddoRHGnxhc3Z-jDGgX0SYf7S-XavdTTQJZXNj841L4g-nsWd7ej7r5iVcRGepY8RaQBMubc9ExLyw2C_K-lUtL-nwgG4YqVi6M5g-nHL7Scy8piIj9gIdBR8bPCBkdu2YsYvhELlhWAoHZFlsvgStpp0P6uN93udaOUB8k4xJl05a6gV0ys4vEtrzbjxNxQsGfgw7qAOSmbLxJ3Ea7Z-OBUTsE1qRdysMFU5nwlg8u0GCTkL5bR3X4KkNaVEQdZss4R-69M5Llx0yRtmN9pFs5ZdZxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16970" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=QVj1VIXHvWa2cbQZQ-k-jBmgJ36Hr77l2TJ1MYCsCvJjrVTvWfe0deqPM7Elt1kWiAcuKCx_fTgItETHEyI85NVFafBrlf9XWppxusTfNe449hD0EXSSkHWwrs4h8XaVwRDrhF2VcHMCs7SmnFDp3ytxAvNqIUJA0XkwJflg9Av7iC-yQi85GsNZT-Xnj4BMHcFVSHjxCBeSC6RdpNJvcdZ7x2L3KqlupGM7qLT8H7VoDDBrkSj89ohXV9yNx3kAKp5BWV34UKDQzBUAW_TFBNe05kvL2faRjh70JhCOMe283G_L2T7N3u_qZp0GgvzZf3s9smq9xwqi-5ON9aLk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24619f26e6.mp4?token=QVj1VIXHvWa2cbQZQ-k-jBmgJ36Hr77l2TJ1MYCsCvJjrVTvWfe0deqPM7Elt1kWiAcuKCx_fTgItETHEyI85NVFafBrlf9XWppxusTfNe449hD0EXSSkHWwrs4h8XaVwRDrhF2VcHMCs7SmnFDp3ytxAvNqIUJA0XkwJflg9Av7iC-yQi85GsNZT-Xnj4BMHcFVSHjxCBeSC6RdpNJvcdZ7x2L3KqlupGM7qLT8H7VoDDBrkSj89ohXV9yNx3kAKp5BWV34UKDQzBUAW_TFBNe05kvL2faRjh70JhCOMe283G_L2T7N3u_qZp0GgvzZf3s9smq9xwqi-5ON9aLk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16969" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=GG4kiFWbi7tmdLbYWqQNKepboryNb-8J5Lctd2n7KJhQTKbf9pT1gPCdE4w0-2EdE_63FOPNd9XnIp9eZICFJzrKqGZOEOaNT5q77Sul253ps_MER6x7hsWpviGAiN4e-qziZqM6cXDpyexYBzoO4x8zhUmxc8zr4CB6RI73-AtvpvN98U0VgcEHC7f2anHiHqqn9beukx2_gMiIOSj7MqJBeUO3jumkMtm49WpzBVnok7zNlyXArI2qyCUxBZ11T22fmDHYAUigiJCxJC8y1OO0toRWvUthN6amhgfkx4uYh7qplXYE-qwR-XoS8hMvDLTPe1x_1p5QSNP4LwJ5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e29a349ef.mp4?token=GG4kiFWbi7tmdLbYWqQNKepboryNb-8J5Lctd2n7KJhQTKbf9pT1gPCdE4w0-2EdE_63FOPNd9XnIp9eZICFJzrKqGZOEOaNT5q77Sul253ps_MER6x7hsWpviGAiN4e-qziZqM6cXDpyexYBzoO4x8zhUmxc8zr4CB6RI73-AtvpvN98U0VgcEHC7f2anHiHqqn9beukx2_gMiIOSj7MqJBeUO3jumkMtm49WpzBVnok7zNlyXArI2qyCUxBZ11T22fmDHYAUigiJCxJC8y1OO0toRWvUthN6amhgfkx4uYh7qplXYE-qwR-XoS8hMvDLTPe1x_1p5QSNP4LwJ5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به اسکله شهید کلانتری چابهار
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16968" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش انفجار بندر جاسک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16967" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ-ByeJFtFtRyL6A1FKhDyxNg43qoZOUWaIsuYczltHpzrkonrkDPw3YLGOX-ZQy-q8RN7PY7WetSkuK4KHruhr8OCi4m0VWQDfjG9POZ9ztJ_66CZ4bhb3-KCvRohA-CMnGCKc29N9F8355ZaFgBMwJQq8FZ9ElEaPDQwexKArDHAfc8exHXTqMtqy2n2MCbX9Ie0zJi93j_5mnGr1iAi4WPQzV7ZOLySbMBpy87YZ4fX-NcLAOHT8fPxJ92VW0vdQE0m1Mfm1kj1y5uBwqb0JOg8MbtaHxNIxvLzTbyOGcO5bhmV9EpX4H3TWOtyhZewlMV1PmB2NONJZrGuZ4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkewytTX2TNYNrXIPhtegS2Ixs84YqOF1zeSZkJmFGLMkwydGgvPnzKC0nJrTp1kCXt5EdS1AOQXwOK1IfgSIIgvB_X8P2BMA2-0ZzJE_xHf20jpeEyrPM8r5shAQfRutRp0kxOl9OOZsmihv0JaWFQ7yDEOanZ5MMIwx05XkPGcpoIyucn-MqvL9ffS68bgvGMutJv9to7BTK1FMu8zFwHQLMNTHQNh_00dBp1Ny-SJNgnwn-i3r8nWpDHjQ8IZNEEjnJxRpDJcUhJgK7zF_R_knEeUqC_YwM-oCct-79LqOSVt-pV-Ubp3Mo6NMVH7ovdubdrj2cqzF-gX-8nixQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16965" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های رژیم :  شروع حملات موشکی ایران به مواضع امریکا
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16964" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB6Dv3548Ri7dj2eyB6UfXYunu1doDgN3LTCuRuJxtSbsC79r5OWUAPe3PyGjOWN5Qb_AjfOyPkXk-QyFb3rUAbKpy2eonMCVt-qateRrnZb-c13CMgVFPMarCZGn0_uFyOJrNO7LijKhPFrij2zswl94AQ3iVrwfZVo6bQie40RLnk9P2wrnj4qYg6-2OYyEkO5Ooa6-coNag2oj_-0gAzXiULYUwN8w0FZfSigsTKGrPyX1ebNPDWfVyp_wq6lnGeCBN0GPRGD02VH5EYZHuJdpumFjKt5cDD5Hm3CoI3RE8SMhTBodH3LV04r5mVnsMQIgdRnI2HU8vsCwX5ByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به نیروگاه برق پایگاه نداسا در چابهار
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16963" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=tWK6TFBLlO30yXcvHMbtyrKU2vhlireFuoQazGEyz_oj06ibiW8IkKgAfkQvjkXba7J3AJhJY7RCy9i1bMU74kN_FXo-PVPwdRKXOZHbGj686R-hS7yt6yuJU5zcwMJ2PFuA4Uq2LzdOFN0Ti_IJIxYysZ64wT-jPKSds46GGJoJEJecLAzjo-89uRA5LLy6dIDuRU53uPuQUuzzDh6P-osblTKpabkxk_--Ll9AOe689Y19q8kx7iRvHsyW-ye5jiMnhzvtB4r0upKNOpuzeD15B9obvGHgFdy5U43d9VefUqbUhXZqlY0Qv1rOEPeLp_lMNGMHFTy1g2z7T1_BTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=tWK6TFBLlO30yXcvHMbtyrKU2vhlireFuoQazGEyz_oj06ibiW8IkKgAfkQvjkXba7J3AJhJY7RCy9i1bMU74kN_FXo-PVPwdRKXOZHbGj686R-hS7yt6yuJU5zcwMJ2PFuA4Uq2LzdOFN0Ti_IJIxYysZ64wT-jPKSds46GGJoJEJecLAzjo-89uRA5LLy6dIDuRU53uPuQUuzzDh6P-osblTKpabkxk_--Ll9AOe689Y19q8kx7iRvHsyW-ye5jiMnhzvtB4r0upKNOpuzeD15B9obvGHgFdy5U43d9VefUqbUhXZqlY0Qv1rOEPeLp_lMNGMHFTy1g2z7T1_BTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16962" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=UCmrCXMkeITnV5Qg9G0dLfI46Ry699mvecJop182jcjTKJcmY4Ki4nD0yGJ55X-Wh59t-WbVwVpyXfkOrU-jZbZdLVkk5dCNhw_B9QGSzuKk-XVt3wyoXyT3gzFnUAUnztHGv4W0QXlIq94UuPgp9Ay9X2aXtfYdjtiskXVa6HOWhEN_K3KrUr4t_yFjBESorPc1wfB2X7W7l5nCnSgZKW5_qI5aDJocODyllAngo-_UFvcWyLgqUxC-nvAf_ZSvLv1oR2xeFZkkqxmqXij63SqqCtj6L2-kYwifuPhvHNYtrDTcNp_dywys2igganwsgE7U6PyI5FPL6V2-e-pfBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=UCmrCXMkeITnV5Qg9G0dLfI46Ry699mvecJop182jcjTKJcmY4Ki4nD0yGJ55X-Wh59t-WbVwVpyXfkOrU-jZbZdLVkk5dCNhw_B9QGSzuKk-XVt3wyoXyT3gzFnUAUnztHGv4W0QXlIq94UuPgp9Ay9X2aXtfYdjtiskXVa6HOWhEN_K3KrUr4t_yFjBESorPc1wfB2X7W7l5nCnSgZKW5_qI5aDJocODyllAngo-_UFvcWyLgqUxC-nvAf_ZSvLv1oR2xeFZkkqxmqXij63SqqCtj6L2-kYwifuPhvHNYtrDTcNp_dywys2igganwsgE7U6PyI5FPL6V2-e-pfBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16961" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJIUzBtxOVj_nEhcxgqlxS7WH2dWn2xgDRk5NBpeaNU-5bTKtMjQrxXQtlPc2s6hsSmA0RN737MWlYT5M89bh351-ASiDk4DPnsHEdarGo6VuLr8U9eEtfnQ4TV3hzVsHa3ymiSCoI9-7e05Kpuc7CJ4IpZPj5cA4ULJGkRhjBf_viO90lWtPtFVXP-jlE86ENPQtsZLXQf7QHFYPmEeeOgLseEH7lW_vypxONsz66twwH3jY3LK671HMVx4p9LkkGlSTva-OEDFOGWV8ITA8UWxwKgwt4oNY6tiyD-uyxvpq1MDDsOu_2n16ISPV9x11uicdVsKaO1I7jTzjN4Vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی سازی سمت اسکله باهنر بندرعباس رو دارن میزنن
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16960" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16959" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرودگاه بندر چابهار مورد هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16958" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=Wh1haXfp_uO_FTTAIQIRcSb2pfGwl3RVJnIiaZroKnlLEM2ivNpuB-zi7kNz-RQ5eYXVAwgmhFDMMCta35j6afeCm4ViQxKlxwYuaiQ4G92AfcD9mPNCROV9mPav80QiYAbd2cVA1xGOupVUs_0F9_9wMAnCtHaXaRBbmvmCyTHBryafK4GOb_fNlSfFFRlOv5zGR7MPRADPMLszo0m8cvfqCfWK3eM3NPnj1eybgvOzNWjwxxQXNxecWQ8UWJN0RUgV_9AiPwKMV5HbKLS78yDqf_NpMGra66LHG3zC8MGXhBvB3IKiDX48qdOtGUc5l9Eov829fg90SGXnye3OHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=Wh1haXfp_uO_FTTAIQIRcSb2pfGwl3RVJnIiaZroKnlLEM2ivNpuB-zi7kNz-RQ5eYXVAwgmhFDMMCta35j6afeCm4ViQxKlxwYuaiQ4G92AfcD9mPNCROV9mPav80QiYAbd2cVA1xGOupVUs_0F9_9wMAnCtHaXaRBbmvmCyTHBryafK4GOb_fNlSfFFRlOv5zGR7MPRADPMLszo0m8cvfqCfWK3eM3NPnj1eybgvOzNWjwxxQXNxecWQ8UWJN0RUgV_9AiPwKMV5HbKLS78yDqf_NpMGra66LHG3zC8MGXhBvB3IKiDX48qdOtGUc5l9Eov829fg90SGXnye3OHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16957" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16956" target="_blank">📅 00:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صدای ‌جنگنده در‌آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16955" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۶ انفجار سیریک
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16954" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16953" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش
بیش از ۲۰ انفجار در چابهار و امتداد ساحل
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16952" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg9IR-HfnqfBkyAHKQ9JTm1xRuc8SAuwdZOFEqjqriohHDL1mv2i47C7ccfCs_PPnw1nUWs8sjXV9dmlCt-6XkJXLE9C1YnPsz-OKqQC1i4RGl2ByB0y2z-V-i1vs5tuEiKFmow-xoww3v7ZBNzeYRraDLdJCgn6rYiHJXnfjtUVrobK4nJhiSH1Fo8T1r9fAKaAN_aKH5Xz1HuMkWEFTAdXZftqhLdcdsbzqrDruZMxLuKzurpqDRvy_rAM8o0Xp4c-8Z8uaMzP7Z7_OgMkiPL9wlNty5F6KPKgobsryOX6r5mgFOcK6ARww6oSol_ypWPGyhF3ooY59sR-3GxKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16951" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5ebJVjocwSfh3CFHfaS4-nMANyQUfjwJIp7MRlOckAIYcJ6x6V_SzDoZuMYw9Q0rWV2_rCgcJZD2vCybY2kighFZw2151PQPrMB3pAlEZNRKF82_BAhzQoHkU32IVT3XZFOBBw6bPPntfHcPlD3kKToS6871083Qir_rBDtmSd3wh4eR9xq-vUvGmaRnUd5SuAi-iIAZQrqbBe8wq_MZDcbm40aj8WSf3fDgQIqrY0vuvIcoL71FF56IB7nZ321YledJ31Pioh8J3wsv6A1WLw-L5ZNOhNp0vWkg1PrFiRCzaw4I74C8KXaNoXgz2CTIGNi7zbyZKdVYGtAgLfHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام: به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16950" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دو انفجار الان بوشهر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16949" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش انفجار‌ از‌ بوشهر و خارک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16948" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ_PvHX_13N-FE8jXRygP_T6PLn1z8VHOB1vCpDHoxnC9dPcISfkVs5kABJb-GRd2FjP0PujBcOfZnINXwyhxasB-hnoDm3H50A8X_hK4sghWXUy1m5Ac2DGp3QYm9K39OE13ka2718SlWZYVYVc9tcOecZNFh2fBzrPwBES532qtrE-klyPP9jVKLMpp5VSz7g8MiF7qX_JolaAc-jE6ETpHu7SdqJJoaXFQZVTz5oDQlHhDnnNmFk36oOU9A1Y0JoXD5_eDJM4jaV5jBG2CdcQ9OswaF0JxL7gUBgO3mlJ7GHz4nECTuON7kDkdSwVxKYl4PeewzbGXvCbI-ND-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله چابهار الان
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16947" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش پالایشگاه لاوان رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16946" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بندر عباس دوباره زددددد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16945" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=Q9ZVDmaCrrSRYkvWnJ3aMqgG9KVnvexImlYAMnRnNiJHDEHoGtxerJ8faapGZbnG3i8P88LhW07k6QIGsDtl7-q0sBElNk15NgpSAX5XIloo_APo7Lvn08W0yPa10YEhbUpxgkUd3SFvlNLmX-oIENso9lYKFlLgXZs_wQLzTwwjgP41jRjKPLkCO2NDzT_lpvK_UUlXHZ0Vj9NlYUnjfNGPuY-dyGzNriJieCvCbs4fV7UG-_eC3xT9JGRky_eVA85oSAaeggj76i_hnDfdM5X2vym05wEiSKqdfyo5n-yi3_n4F5dh5OKrY5SBJD8QyRX1OOYaEOcLCAPJxQxwXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=Q9ZVDmaCrrSRYkvWnJ3aMqgG9KVnvexImlYAMnRnNiJHDEHoGtxerJ8faapGZbnG3i8P88LhW07k6QIGsDtl7-q0sBElNk15NgpSAX5XIloo_APo7Lvn08W0yPa10YEhbUpxgkUd3SFvlNLmX-oIENso9lYKFlLgXZs_wQLzTwwjgP41jRjKPLkCO2NDzT_lpvK_UUlXHZ0Vj9NlYUnjfNGPuY-dyGzNriJieCvCbs4fV7UG-_eC3xT9JGRky_eVA85oSAaeggj76i_hnDfdM5X2vym05wEiSKqdfyo5n-yi3_n4F5dh5OKrY5SBJD8QyRX1OOYaEOcLCAPJxQxwXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فیلم چابهار گویا پایگاه امام علی بوده
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16944" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش انفجار‌‌ پادگان ارتش در‌کنارک
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16943" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16942" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش انفجار لا‌وان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16941" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۳ انفجار دیگه چابهار / اسکله چابهار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16940" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار بندر کنارک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16939" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16938" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۳ انفجار چابهار
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16937" target="_blank">📅 23:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چابهار رو زددددد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16936" target="_blank">📅 23:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16935" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">منابع محلی از مقابله پدافند هوایی با یک پهپاد متخاصم در آسمان جنوب کشور خبر می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16934" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک پایگاه دریایی سپاه پاسداران در سیریک مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16933" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای جنگنده ها  در نوار ساحلی خلیج فارس به سمت ایران شنیده میشود</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16932" target="_blank">📅 23:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارشات از تحرکات موشکی سپاه در مناطقی از کشور</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16931" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار‌ سیریک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/16930" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
