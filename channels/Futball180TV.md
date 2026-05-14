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
<img src="https://cdn4.telesco.pe/file/iPpBdl_bGmElwYHNK8VdTT7fX5uqFapEExHEu6Ob3WlsXHXfG53Y0eKpnuYRZNA32f7FI1PNKolYjX1s04Y7djVUGXqa1GMvpdIybzSJDztU8FQxTwCzmjZPXFcycaKzECMPxhFPJBfmqjskgBT0q9bfGOSFLM2pzLbzWvI5L5zEP6X1L7nqUNI9Oi_Gy6Yhj5tFmcC4I3Ida61sXCTIWRI6TaqkEDHkJ_HBwpjP2AkQ7GONPQ5Yztal5KNHESuTgfV_qjruY0yC9DIco0mnfGDl2APeJasIaAqj1M8ccTqPL7EsOovxi83A1u1a7pZI1_29orNrXqvATM7YEmEBrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 136K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 10:11:36</div>
<hr>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf-rbjOePQ5XCaZCpRo_NvGbcfZEvslFyzOhbi3wmZ0dHi0Dba-a7zBOMh8jAMDktm2VeEZ3Jx976Lnrc8VMmbtIP2JVroxoc9na3Bos5udiYxbcXilxXI1Mryy2LUXIIwOs0vdA0-M54hN9L-XGCq-0uSwqUIQnPujP4TXmDDiMy4E6p-CFpiiSTJU-17Un51OR4wjx26i4u8qt0T9wJu5m6gD3Gnf9_5QpZ_SggvnvjVcFXDN3WQiGzke9WMmfsAz2OCc94nLpXTv-V_0Y2aLffk0QK1Q_QnVelExvP4AlH1y5xQXGrjjjs3cqdm2aFlKj1tyxg9kmiLjoeIBcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/89937" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqszfrTzkKApcBBKIRe2RkXucZjFRm2JefTDKY7hBLe_S6riBkzJdphKZPzM_JuAICbDcklS0ZlfPslD5vCnxPg8a7p0ytFX--6ZyRA3rHqaUQ_qPVaUoMWziOtqCLCorIALfxQwMiubC7T1JnSG7jPZQRX0hQlbzDDoieAfbofiW4a2mRSxXGwTo0OkHT-5zFe9p-SIsW6zqT9rVGkOSmO39frZ_6EQfcoRXA0OthsPNVyXU9pkNFTqLL5dADaiGhmx0PToxo4gTifC-_xW5rME7DQY34tlQu-4Tlfyv3aVfaFr9Dq2irBe-5NflRMi_rlTLbt2g4ljW1U1Njn0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/89936" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqA83AqyPjvJUwrgoa34TQUL3UwkwUwIVfUv_TLr8KoCemp_eTkQBoK-FPXGnjA2dyrjqqjAvjBQFubj1xpr6cQX8mhM0UYpLxgbRr6wJRA_JrxyzH-7GvXkpCuPQBGoPI1a1WfqJHLW-D6GBEuyFp4pTFKmOVFdCWcxEr4huyEw3IdR9ffmrKXUfU5-s9X8RAo2_4xPTijyR22ca6BOev7sByzUnOGHjqBdmW8nS75wSV11qGarMa1wdNjzpzglrfcJ8ebNm2itN5Dy92i0thcrdIlpQgH9CIf9dnPX2o6yXRZEMfAlAfgMozH5HCj5JvgbD8pyApeLzIh27LqUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuE5fZqt-gjm7fB2UXTbs7wPKXK_jAhfBckdx3QXLtBwmC79DP1KCZTPEz3PUxaBWQ3H3JycLVM6xn7wgXOMGGT1iQCoLfGIcLyNmjk2Y_viAWlNwpM-12b7cC91-1_lbkztarXo4p1NEAa78HniAbN4PKlu2wAVdiJy41u-ZH9qEL0NPPRnapFZD-ZbmMAbIWygY3yYd2JIjKM0ovyp4R2UeldWIXa9IDyZBTgiCdFZ4nvhoGVTKPfGOJb-vUWpo8Zb0-5vRVeiYFvbd3Id0_sIyyib55Rd4XN5AO2vvEADUpahmGv_rFlsbFR97dg6vPwULFvdwIRkk3R4U3CUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjKiv69BTdp0MGXxBIzpOOOqnDThi0nAkJjZ4IMQKIV7FI-H7sHzRtAZxJxJ8L-BxrAmwY_D1NCEHRoV6Q4gdkohoN4kM5ySpXCk9irxghZKW_OkYFvw3wXBw_DX5rZaCelzpIhOC2xKSo9vGth0aoolrGAz8mPeJ5BBnxah6Xh4eGXrDD9v3yOyAukhDMr33EkS8P0yOF-3-OfL-AEMAVbKODm4XRieR2extlZ1hcjSO6FYsdyAtgh7RLv0UExtBmkjY9oGUZ4DadDOAtfYDUSU2oQcYxvMnv_PoAky2qgJWJuglBvNfkYbmhdXoAO6bKKe6irdgCeYdLpQBNyajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDVevZ16bGzU4qMQ_JwTr6hizJzAUrXsDIVR3k52t--cLhlTLFRYZRwVHS9rwYmALqwDscaT6WiRkqxapob4Lx8SquoH9RDg7Fd8c_9U_FwiL5XmFYazGD1_r2r_Llc1xgYabR2Cv5Q6yZGZyCqlj5qiLaGnnNTPC2ddw-X79wgEpePTX4fhb8avwoc0F5wjnzb0P8FJZ1-JCyHPZ1WBAUsPLHYCjrGFwdeF42hdIlrBT8lp70jBgII7VDVOMGpDIEK-P8c8_AIcQer6z6c1J-csOH90E_wq0HE7L7lqvs0Jkhe1VmiGcgeZ-D7Km2Dacg-o4yygIN80OIf_fau6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/Futball180TV/89931" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmwLKVAi9D-rOCnQpT26tAz5lTXYlV3RdSFt-Lw4468IVzWmV_jO73aK2UpVbPNWAVXi1i92RNsEsN79lXA0-XUXOApPRKgGbMsniDR1MFFi5-uMXodLUc1A6JdDtLZXYoYjdzItmLShtZ89HVkkd25rhMNhYSCAMEXjG_lCBhzeoo5FOeQ8CYSg3vah1DYPQVWQn26LQA2Z5qm0fsIQZjmxEEMQE8xXrpbWuNPHvRGuoZvzMoXB7rYk6LVKXt3EYaoaz5rFw3J8YHndSeg03jRQCJ0tDeeKpi5mv3qaDH-yLIHfml4NdjqB2UVpKP577qf4GUmPud5yGYRyw1FewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/89930" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZeHbhCal58avDcggu3Cs1YXXMoWoAuOhVhZ8FzyQlr2eOM0UXJH_JNQUeB1ub0iwb_V2oWd_hg6dz49U7owiFK1FuSSBErDETtOAEI7djK85AVWnLigXI5apjm4J6QlOQhMo9Y96_KBXx64OiQkdZGpxsOg0PldKMMTNdZyCAozz1M2HJoaDgLVWspIew0y88nHCDGmOcVhL9ikpvkSNBDjKXi52YyDb5CqOwNRPIOAe1xGgwrDKs5Pg87GY8-RlTjKzYp8XzBcqhg8vSZK0WfqBdztN5A3su5QbPWjvijelhqn8EgPwvkITpBlgRptf6F5_GgoUufdAvjIpXTqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJq6bFKIgeR0KFpeYkYOM2oUo3WzQJw-KgHgOyYeoiCiMqiixxQ7gSyx5RU3p367lLoQlZzcyiIPyLPuVpwVKZ5_B7znmBLVxBCTni2uySeMhSsXr4yIvCM1Arnt95ztP08xEmCHbjM52knjp0RH19dOyTbSjihd7Hsn-WypPQA0rBm8q5B9HRny6SZOkRob2WkQoB6WbnUZQm-QjpOsHnlXPNobQ06oeUAh9D2fS5L2HK7I5TlZTSH1xPmtNJYY8DWyrW1eWRu13NJilFUvJ2HQOU4T8n-eQG1xOQueGSe8Un5CpF1LomZtCesi_G2ijFNbIGEEe9DvdMsB3pEw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=AsvJOXO0wI1jCIfPbqmcdstf-RVcxNN9I35Jaeo9ulZ_BCJJUa2z2B4Eqq-K_h6wgZzjbZkhpcfJMwja0xIt04s1jjbmBjSIcgjoxQ3dr-gkljNkQDThKQKH-We78BVYn5Sk514Xr40FDIgZ-S45HyRAyYqKu6LuUREDiFMk6xi0x9oxH_aLgfTbLQ60cUXbyZyAcN_Pwr8Mq-Lf-TsmIrDeCKbzLH_zECjBs3Nw23DKkqjmXFXBZ0hpN8yPxT4G_VSz5LmVZOAEtEtbidgskYv7dFGl7_BFgWg1WL9B-EDrM-AkoZta7EqJYuWw546T9z8JA33IMppUOkCX9jh52g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=AsvJOXO0wI1jCIfPbqmcdstf-RVcxNN9I35Jaeo9ulZ_BCJJUa2z2B4Eqq-K_h6wgZzjbZkhpcfJMwja0xIt04s1jjbmBjSIcgjoxQ3dr-gkljNkQDThKQKH-We78BVYn5Sk514Xr40FDIgZ-S45HyRAyYqKu6LuUREDiFMk6xi0x9oxH_aLgfTbLQ60cUXbyZyAcN_Pwr8Mq-Lf-TsmIrDeCKbzLH_zECjBs3Nw23DKkqjmXFXBZ0hpN8yPxT4G_VSz5LmVZOAEtEtbidgskYv7dFGl7_BFgWg1WL9B-EDrM-AkoZta7EqJYuWw546T9z8JA33IMppUOkCX9jh52g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smx0FgO4i6sONhXdSTdOPGDSIqUK1rBeyUkTOXuvQPAIRJsdkrUk0mrQLNL2ufi-FUTUf2FSYj6gq3F9j0R6qGTG24Z-N9JwcTP58QUJcJXY1zDv4q4c3sVhlDGplxNILIz_8wouULtc3hAGggm9TltAsV8wGY_Wp-q8OlnKt212vx-_wpay68Op4rg4vpqUbJ6mQPAe4wkTJsUrht5oY3jGHFeEWyM7EMo2QolaZ6pBDJi4OOKFizPUDS76MhWPWovAMmzaOnC_f_x9BQpFlHjvXJ2z83APgSwUnFH3dV2HUyk-7tNdxkZEepoDIFymfl5HJJhplEwG-e1z6VMeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Oq0AOyCWuLKOLbQNu2KCHQV8B_KI1413NdsW4p4a77eZMly9dUxDM1Yox67IGA6-OwAmrFMRjxHoYau4ABWVrCoy6Zzgv7eHhBBI4-1lNgrD_55TrQVh2p7iKYg08APMh4sZ6098LKhh6FZGXRaS8GNWkrlWJLbXmhxQtvTt177ano21vhXv9apTHFj2w-8XwYOFrUcFV0J_vCejWliSOieADZRyEbDjGWg2SJ8bapqJS8I2PMKve9F-I154r7J1xbtXZYwukvzawVEnCiD_ShAGddknNnwg8he090SDGk1uEKbWYNHem1p7pOF0teYuR4UjCFDUyCsQv_OUrGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvCo1UfIFQt0a_0cCFAgkeMCENwiRg5-LnrfW8GtOk1ktoegdNDyKBUzhEfecj6LlkWqmfaHDeia8-RY-dFuYGYqsgSKONdkz2v6ywdBkWn3YQOfwk4ijz7kZzpyhO3O6q-N_kGM4hWVv2EtvRT3yhfs_6P1eSJu4GoNtrIC6YVuvlqviSlFm7gxv7C3o2Ef00IEXlZdh1oLcgyN9O6sX_9UbY_2VQ31ZpS5NA3sPsLpHia41_GuJWCprBrjA8wPw9KzaEVmmmVsBtQ9N3o3rSsnXT0KZrcChh5o1DYa92kUOMw22mcUq5rfk46O8DZTgSstpGKhXm2i6t2HM2wVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3mj4DX1C1VpT5QFzTfp-HakpEI54BXZG1eEWTDb-hN1C-ZDTJ_TI4Da-r1-XYBd3_bFQLnoHUihuUz1HyB9yfXud5Oi_PWRM0MJHCd_9LsziRhAxmNn_xKxnverCNQsJnpi7lLfi9JKyMNosMPEE55Ceq08b9N7Pa4BWWVjnGT3O-itbE68SOEsp5lHFX6v-cE_Q7cl-jNgJbaRzeSUO-niEOlkD-z9HWC26hlOcaIx5qY6o8pXOQE4ctH-gO5NdCX9OybaKPJN--5QqVh71JmM6QZ-SobivajIVLhxj1FSGO7i7gzFcFqbzbLFtrDCMqA5ZTLCb5HKGs04kgjoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9dcuKYa3rbhQPQZMBTqH-oIY8uz8dcS9P-2sFdu6WaB7B7-kmDy4B1Ku_cz9jbfvlHLo14IdwBuWTHbnjaIPJepMz6AQwMlXWrbtvHfaT9QO0D8maWhf5GscBBBO8_K8XukQI9zaiwHAZ-jgLR-hmHjeRzUCCSJlaXe0Y6NlZ5C9Wn5akNugPKnyTAWriF3Xq8fnV8Rwc93ruUUDfyeewmYOfEmHj_VW7uHPf53-edT24RUCTgQIjSNLACzg4yUfATvl6IYZoQU-xuf7dIxPC8ZP2TCxA9DElzMhsW-k9EIBDo9Ri8xTuyJTzjqmsCnyPVkQHxbmOumJDFpHsv5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aguEQQTae_ozx-L8_VKIEMw3MvSGw7jOXaY9lJpli8e-E0LCyNnm41Etz1kd1jPr21czJS9Oc36QCsk9Onx7j02LXdUg-P0yT04UhyOdn4Fa-Em13_QpRrwez0rQ_HXI2vSVtQpThllN9JYpmuNKLnbtmHyKBdpliF5ktryvtNo4bYSW9S8Ri6h2Ia5O-5DXF6pqP4rp-r9ifFDP3aEISZ1tl4ry_FAVg1SshCm6eOHasw_WC27-McuTKdscuZuYj1vpcpifX_hFuIJoREE2zcvXJ26MP-4HxHG4wfd_kWIKFTOKwUAoQg8jH9PykWpG_wzv19YoGiifOZHCJtQVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWiCgDLEL2Mrl0bWqL04ZwoLC1qIKd40_8FZs8zMun8lZPBLDqYop5PlpF8D1oys1xrQTMdhxaw_M7ZymECG0viLO9WcFrizPk1NMnjVGo0jnn20h_k9xwp9upn-bfvMMrmRJFjUDQWbaVeomtIzsc2cuNTiKyp6Z2Di4eDSnj3u9NIC1JAMHsE_eJU0pX1klZcZ0SR34KFXob3H_sFgVo96kCq_8EljbmTkXUgnUeXaSg9o7rBSdFxsgw7IEAs21XEQMtnvEJJEM47NmCP7oSgeg2DypqviVGPmk3JNS_GUFle7BED-UFQ459KVztFK6RJHw-UFwtmJCEAFEbuXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=WYes3syVnuxICe9KUw5HFx28pPofM8tn1bfY0v0RGWbQ_xvZ4L56G96QZ6zn6rVdg2Rp8f2GkQeHTQuGWU7YSMbohJ_uzJlIAuETfWVvOAkuv3VfvQiQEfsCjvknQwG84hsjt0IlAN8Mq5Vm_lMyY_AGtqm5atG7vL7YL3MF8GrRIxISN6uKztaZy2p4uZGdYKFZCidOLV27wxWaVR-tAYE62HSaXFTgLSxlxvZ9n2XyHlBscM-Z8u8XIX9lVIO0vqZm0KfhA1zrqb3_C-ajfrYNqVM7XhJl3kyA1qUp-J_5hIKYkUOEIoBVLJgVWXYpJv0M7n3vI4ZVyWe3TYvBSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=WYes3syVnuxICe9KUw5HFx28pPofM8tn1bfY0v0RGWbQ_xvZ4L56G96QZ6zn6rVdg2Rp8f2GkQeHTQuGWU7YSMbohJ_uzJlIAuETfWVvOAkuv3VfvQiQEfsCjvknQwG84hsjt0IlAN8Mq5Vm_lMyY_AGtqm5atG7vL7YL3MF8GrRIxISN6uKztaZy2p4uZGdYKFZCidOLV27wxWaVR-tAYE62HSaXFTgLSxlxvZ9n2XyHlBscM-Z8u8XIX9lVIO0vqZm0KfhA1zrqb3_C-ajfrYNqVM7XhJl3kyA1qUp-J_5hIKYkUOEIoBVLJgVWXYpJv0M7n3vI4ZVyWe3TYvBSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJzwCFTdhiZNg8BQv2STimQ2jrWVefQbUDTY3cphLnngDbtqwhN7Pezd59AzL1Si3aYlYkeZddcBUGzN5ACOzfwwJ2xwbcmx5INv-kWv8Zuimy8gP2mAzhfDUKd3fbBMuQv3scUKdd794T4pvpeZzKdO-u8PhyXaVHpdOELllbElm4MIIU7J1g61qGEH8UQNagMyOuLrLswZ3htUc1k5H7kpC5jS5hZVxV2dpXxcyzbyzIlZ6ht6BDchdYVRqrfTRNIbmwzH_snKKS_DH3zOjrPA_Sew704OBsQGR_yR7tISrOlTVC9EFg0FHQf2_pMd38zE1AnDBBA7LaVTLw3elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3JZWSkj82J2cJhEZc1yVlh4K6JxfcOqI4d40KZfzDhE1VojOvpNvCR-Xphl7liCUEiYLSb6KdTkg8qfYIQ4pREbbfladNkt95tefY7_rcTxVB4fgxBULAZ7J0YFVIIxv2jzjJGaGcsRdAtWdCMLDT7Uty4BuhQRtCxnYBaC4B8A6JWpdMmYNY25zsIDy5YSrXpm5-iGi0TR_ztI4cPBdW_JERxravEAfmvHsmuShiTwFeaO3OZaGmY2MXr9rOTdGmAjdgArNX1OIIOS_OYpe9VWc1x8cRPbeGdC7HcIshs-3zxAIB-DEKfAhBJlgIqE9if-PYpduKzWEWvu4QOo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpqjjMr6U6dJOGjp0Zrl4aeqa3Fyo2aq-mFm01bAUt595Eh18My95_UkaFjfMyju-GmHbGgM9WYaS_cY9mBvfB5cNrrErEoBNbzluN7RxQZKCB6wi7Nvkx-4cpbbJeP0ji2NIbHXDEf1CmTpafkaM0YSsPaP0mCxPVgW9q9imMfuoNaq9eEt9xW1NLZPH7zpAEYEKYnWdDkPIygMoOZ8TRRcMphjZ7xumJ4lhmlKDxnhxRdJ7FlSlO72iKM2hp6WPalkBhGetpS7-dpXcJ3NVL6XOW_SsmsnEd_u6OCd9j4kYyKViaIVoeAymXWjcYLfBz0e2RdDnQgOz5SrQCpbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKF77wqZEaOQRsdqrG0ghxwsWDOjt_f0trLKVpkAPuEA-LWyK7Y2p0kkre0rVtUSCtv5cdVslIU6FNw-J0q39O2i-UpHkDk1_SzHwrH_k6KTS3_0kQhF5Z1xxTDzIdOSNoCpUCHNTOHZEzmftefmHZi2ieUOJ0YpNJxneZFgBfXqnxCkhzbI-12L7qpMwxKfsF03T6Ue93CTZAVYKKH17cgSquCegk80jKXV2Qs-AMyH9Nk3P53bARlgovf8586OhWaZFdTYyZTqKDjDfrNqnswfs7WzD0PlQqrblQeGv2ADyIRIZYCmVKsBYTGjpS02iHw2lbPp6pkwBTsJXRsBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byDoCChs77t3LAGyd87kW6WiI79jlMfFLZeEjduTCMS6Rr1ENLYDTx-SZaCCP8TgN5_wIMDwdIpM3LQMDT-G7H6MNrGUMe7hzLez3Q3likZisyualgf7LPQc7l-eJLI7AX_ZAjW4i6AJZSXtAsf3bE1S_AEPVxC4ZUYPwK10qGOMCWaM98zQVMYoic8j0ezmKrRu1Ohq-gC9sjM3zpaB96RD03rIsArHF8bS1BH1uiNFQJ_To8kU3u0zTzrlkZCkKF_slCgZqBt_8whLx3Yv_ypLD-a67GnKcvru9ESEvXk0i8161sWj-yQZs--Fqxp3bMzMY2LXCHBGzFGLzsIBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jldYrxxp93pYOQCkTQ3zz9S_us1FhYuSYTUVkHBRY2ZnYfSPzU0-D8lvU3tueiRGSjcICTgb1a9Xy780yoyFa-SkWy_f25Ke6mkyfDHtcnQUCq-F6dkJUt6kZsoeloAZxeurwKH6Tdatg2kbcxgxw2ZyJNE1vkJN0hFoumWeNHG6F1RweLyLEhQqUNjb7q9sAo0NkEx8XAaFy0xMQr7GNz8cmoBSJMhLtQpP3CfvLu_W0JRQ_92Ko1cjVGM3MXwaWLUjzEorFUmmQi0z9TS5BgNPg4b03PBzv8JT3Vpy5Y7uwYv9iwFYtIb3aNS_ekgaQbdL01sp7DbK7eDrN4DuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Voxz5KUVhse25HD3FipBx0tmA0DdltZQHXEpHARBB6gEhXxVkvcwwQIN5Jr-1n4_ySCvYo-jvTkCwQr8RPAw8_zkUuOyjl2diEUZQ08JM0S-pfRJh4QTTalLEEI8m1DCqsR2g2UtHd24f0lR4Qd52elZq79QtT1LTtQAL4Cx4A55h-DrQEg2BwzrWKBe2VCxIrvgBjUtRdaWfJVsDvjnAw0WDY-Qf3JdEA2pj230Bf21OjjnqnOXq-ki5DZT9mLC_8-MSOAOfPrGbTNryTiy-7d5lDD-38-0PaHbFsGKM7L9y0Li5_MQmnXUZ-HQhSWQNuBkHvhjrNwuQfjfcDQJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvM3Ktmj3kY5pZZGw4Q5d2-PwIuQXpYI2OBj1z0hXJv61KC8a0pwlZpJWofdpNIyNKSnjLBbxgiwACSmWX7pIVSyRwtkMfiYm7SmoSkfd8vT-M48YR3vGF3JY2prR1-4nMZ7O52Qcjgdaqk0HO_EHc6WdIO-lCuRaPFjrVHTSO15ceUplErnVn5Gg_85ij2CMHtccwEC9vJdO3qc0CYYsD116t3w0_M21Cc5ThdoZJ-J65rgcp0AIF4ZA9qnc99wlcgO4XddsWvGhqTpHEDsEB-UcNX0lBula9aLL2fEXaFf4CveffxW0y57SihcnqRA85GFQdps1hptmOtCoMUA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0SgB1N-S4Eqg8OOcrV_GftGvQZQz5Dth8CIEwo8Y14Aq1PmpfpYTUTXf-qeo0WgbZUd0XqPsg36_yzMlczDY8OY0WB4u98Lzp9BM4O7QknuGQtIzs8zXeIEK82sj3vKop60QBf0HJs-9CJoKZ_To95IBElrABqIFC3UrTqT2ceemh9rkaWaHKjbQwmzxzii0dD4vbeYqKXeSPpqpxmOOk5XhwXDUSQJG9KQukNL_mZL-uWkLclr5TpzNr0HVdcrcn0eF9NA9rR6mFzYHGkMiG5JwF71VHhuCH-FDnFOZe3I1q1ab8vYuM7Q3v6BE9IeIQqyakGH7A4FuX0xmV5oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=ScEGb_vRd89KS0mkuh6yuyiJNAN6zSIkLARwBGk2koExmUiM8DpXwS-WlIrhwD0iKAT33SMwbvArCegHNev71Xv89MjvoMRzjN6pm-Q8txSBFS3H9UuH-t6eCg65babSRyLka-HWgVM7CJr7aUfxehLqrCfiI1c63RHjNqJrrl6vnFv2piw6Xs6iZG6gGVKxjZsSBVQ3QMMCTgjYnTvXL1I2jVOOHAhA3E8SpBRiB6SG4q_DNIHDpi0YYWuGQEM79-6sneHCyUPOnwMQMbx0JhjJOm1kcQZ7zN8_dO0SaiL_ksOTQITWypwMcwJJq3euwxg0_vQI7tPhYQ8E17pN2kAVrGJVzNeTW91Ni8nOx6JtdQx_FGhx7CEC3OlhY9I59u3ZtU2H4WHoFPM-v9RI3vbmBOZhgQk6WbX1rEFc80QujcFEY4yj2XYv-0FK1QTX7mi2Qc1IegZEiI_L-YhUIAzGs-hRRA4TZ8tniQQ2witVESXG4bAuJaYh_IK6vVicgWuNsRoCu-hKfg_59mTzKOXxp8OAjSmEeLwcL35deyqU_ZTXct8P7-DR5VGTReWfi4oNAGch8dM-bLF5od3KZ3jAHpfzmezrxnX69vpK5uZK9ZDfKC3k8-Ler7ItrrgsAh24T2_nWh5iaUhoVSwWTEFmQ3AnVWJE8aBIfHR0hMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=ScEGb_vRd89KS0mkuh6yuyiJNAN6zSIkLARwBGk2koExmUiM8DpXwS-WlIrhwD0iKAT33SMwbvArCegHNev71Xv89MjvoMRzjN6pm-Q8txSBFS3H9UuH-t6eCg65babSRyLka-HWgVM7CJr7aUfxehLqrCfiI1c63RHjNqJrrl6vnFv2piw6Xs6iZG6gGVKxjZsSBVQ3QMMCTgjYnTvXL1I2jVOOHAhA3E8SpBRiB6SG4q_DNIHDpi0YYWuGQEM79-6sneHCyUPOnwMQMbx0JhjJOm1kcQZ7zN8_dO0SaiL_ksOTQITWypwMcwJJq3euwxg0_vQI7tPhYQ8E17pN2kAVrGJVzNeTW91Ni8nOx6JtdQx_FGhx7CEC3OlhY9I59u3ZtU2H4WHoFPM-v9RI3vbmBOZhgQk6WbX1rEFc80QujcFEY4yj2XYv-0FK1QTX7mi2Qc1IegZEiI_L-YhUIAzGs-hRRA4TZ8tniQQ2witVESXG4bAuJaYh_IK6vVicgWuNsRoCu-hKfg_59mTzKOXxp8OAjSmEeLwcL35deyqU_ZTXct8P7-DR5VGTReWfi4oNAGch8dM-bLF5od3KZ3jAHpfzmezrxnX69vpK5uZK9ZDfKC3k8-Ler7ItrrgsAh24T2_nWh5iaUhoVSwWTEFmQ3AnVWJE8aBIfHR0hMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=cl4vhukuwWGFxTV1EHS2O_h7Wr_7myJES9Ml9-zoxMDlK3HxxfbrVeR7SA3pt9ezxWQ_ncdB2990GvDhv49YphfnpNr5IZCY9nJe0a2YZUdLDSsd6o5iTQ8F2hEAsHbcs4IWM-Uf9fucAHEsdfeO3BHcCvEYKIYW1hcFK5dSxXcYZkUCthhgWNcVD_bzJ36stXiRrxbKEh9NFnLkF-aXvNmPssjXyRImv3VaEMA6TvKug1F1rMbof7mqhrTqVJDUsJKpNM3nflpSmPNSa21iLFZnddG59lhjYZXRH3Aohf7o3pY15rFCkfeHEgq4PEL-nElOcXy4wlbNnbqeQi46sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=cl4vhukuwWGFxTV1EHS2O_h7Wr_7myJES9Ml9-zoxMDlK3HxxfbrVeR7SA3pt9ezxWQ_ncdB2990GvDhv49YphfnpNr5IZCY9nJe0a2YZUdLDSsd6o5iTQ8F2hEAsHbcs4IWM-Uf9fucAHEsdfeO3BHcCvEYKIYW1hcFK5dSxXcYZkUCthhgWNcVD_bzJ36stXiRrxbKEh9NFnLkF-aXvNmPssjXyRImv3VaEMA6TvKug1F1rMbof7mqhrTqVJDUsJKpNM3nflpSmPNSa21iLFZnddG59lhjYZXRH3Aohf7o3pY15rFCkfeHEgq4PEL-nElOcXy4wlbNnbqeQi46sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksID7Jva6BS-pwRuziKTxVSEVWTYlPHBOcztt9LZR2US_FgSwRqPqdTD5a2ExlKKm5TEv9387Ifw8z4CqCauFqeW1DuwjIeOBQCbOFdhz0viLHgG0aZHLdXZ3GFdnjYX-4-ZQBsUpVnVq5U_NhHV0PBes2m08bJLS4S1AWSwQFY0MCbu_EnYkcodP0iVobE-ZS4-h8nc_XsiEWYjDgrL8HRqEsiM6222X0Ti6GisqRwNvF-zSCc4wU2eD-XA07WoujpNiRn_PpcG4omXe6lYzCghU_Nt0E2jh4JeidyJXHjMbL0VIbkiS_fKF7yAFUeEIxwhlXwJ_8IchqPnjZW-kIm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksID7Jva6BS-pwRuziKTxVSEVWTYlPHBOcztt9LZR2US_FgSwRqPqdTD5a2ExlKKm5TEv9387Ifw8z4CqCauFqeW1DuwjIeOBQCbOFdhz0viLHgG0aZHLdXZ3GFdnjYX-4-ZQBsUpVnVq5U_NhHV0PBes2m08bJLS4S1AWSwQFY0MCbu_EnYkcodP0iVobE-ZS4-h8nc_XsiEWYjDgrL8HRqEsiM6222X0Ti6GisqRwNvF-zSCc4wU2eD-XA07WoujpNiRn_PpcG4omXe6lYzCghU_Nt0E2jh4JeidyJXHjMbL0VIbkiS_fKF7yAFUeEIxwhlXwJ_8IchqPnjZW-kIm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=LygHFZqWOg75U4eGfG8qSnguPK6hMVERTCPczKIOQ7e456x3YLMAzwXIK9jQgBt3V7i652KVYTgBZch0SzPeXvUi2dVnYP2-Ofv8Xfij3UgZvhuMd_HxY5MlUmVAhNlY9ptU0TizTNlz-zIlZQroKdd4W-W_9Tj1G-wRBhcg4RdPICEeEfY0n0pGsMG33lCW6WZ_hiHMswTrsmvOWBLBa2IMHyyHMWDxdgu1f-YNGjczBDi2bzlScEqjOrwwkXKV7zrasN_j0QJQfftotEQ-eqz82GGQM11c2f-wYZH28-JnEt0_b590knNdro259mj19H7NKiuEv0hF9Ytpi18M5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=LygHFZqWOg75U4eGfG8qSnguPK6hMVERTCPczKIOQ7e456x3YLMAzwXIK9jQgBt3V7i652KVYTgBZch0SzPeXvUi2dVnYP2-Ofv8Xfij3UgZvhuMd_HxY5MlUmVAhNlY9ptU0TizTNlz-zIlZQroKdd4W-W_9Tj1G-wRBhcg4RdPICEeEfY0n0pGsMG33lCW6WZ_hiHMswTrsmvOWBLBa2IMHyyHMWDxdgu1f-YNGjczBDi2bzlScEqjOrwwkXKV7zrasN_j0QJQfftotEQ-eqz82GGQM11c2f-wYZH28-JnEt0_b590knNdro259mj19H7NKiuEv0hF9Ytpi18M5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS5Dst0T6nLPmSTO-76SbxB7Qhe3tQSkViyRfzLRaqghnEFCdn1B2ygyXWEMbxQ8CHU1w-N0NnQ7A53dNx_o5U0bduDSf9p64Z9uYwlkIsTZLpbl4P4tFzhuXtZ-lnMK5GclsrtPeF2H-5ilYddyR-RXcy8VHSkbmTpUok3ARZ1FNBpOrmgsKP68rwInVmhGdUX3OsDM3kFrr8Ma76Zi-jVxcRUifH4Z5zCQgQANb3lvqhJDJyUC5kjpSLv-EuYl-TNskkzGQeg-UcVLV6nMShFEJ5bkvZX001EmQ_pYxEMBz9L62bY5MJpGSpSczhiLS_SXuyO0aASnG8tx5I2lQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvh_N6qD22EL6F1GjueGiQ54XkJEHqwFhyc9eXq08uLPlLx2roy1SDCjCRJffVw_3uE1cow8Eotkrd4sI2YqK7ohCY46Ozo9sJIg6vFQf7xpWuaPGE73QGKziQFbOJy3gxxzOcmAr7fnkYGr9Y1yCyEvAHXDI4SSJR2xQyET0l9Kg5fO21WHXL4OTvijdODHO7BCWSLdkax8GblJ4sFX_nmWs9XRvom8Gx7kjPfiFMmhK7lLjskJKMFoCNFojtJFBNnywb0E0Op1uBvvYT4212yF7z0LswRL_pMTwhymUJy07p_dnvr7ZNJsFQFdHJOZljAxn7N7ZvJ1iozEBTxpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNceR-wzbYmCyiVIV34ABBrUoR-v4tsGeOWZM0KWn8Bd2tKJenAHzv_OiDQCYAOasYXtXKeJzQAgRIu5jC-xDOSl_8kBvbVzqBU3yk-A-MqQK3Na90bMO59bDzF48cnr2fE2IBPsKNB-HdDjzznY0t0719C6B-q5Ni6LORCux-PSa599ehfjkJYYtMy6uMoGQQbRcPfSgnzKXNJBPsFFF7etpeQyfC8lEIH1LEiGaY3Bmb_s6SPsCTTyRMKHH5S2ZSGH3dFP2YYYManZO0yzgCpywAIpgw1fOGkEu6cr-7tV0C7D4xkFE1fAEKaSTcCoXQDYScflNfo5xeugyhHOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAVR2qr0si4SUDvGf8MGEytf3GLwiH-nQhePwBRoQ0YX66E8WzMylBLFF87WhFCk587hPFcnX965ll0OjOyEY70LUON0VxniYQM4RjVpkg_VSagYUHyHKvlqFt4posZ8hDUEJl-sXQmNNd20AiWivHkit1DhsNzLOK6qtPgMAba43mYY05_pos_1cxwhn5YmAVEzIrogaN1zfTiZBKkpZLA44dHb4JN-ELyCaktsU8xrsrdZDrHEysm23q6h4HxrUoMHXsOKuf-3pCv3yq-Co2JwmA96PZA73trdvjkSn9kk_wLgO3xIHV1Zbi_Y7Ibaihowc4GJf0LvSfao_Bp30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4CUlrLSSpq_rjrhJ1rurEPt0MnoaNHt7aOpReF4lLMUcU5-69OwiPWYvbiLVS4e3jmejzBzytPAebhC1el1oIZ54d-vBiV3G0ZbpNa-1ZgQMRnPUmhRcK3hxLYd1054BQE8nNuJca343DzpzNRfaVjyuZNQt0vfx-jxyIwc8CLekbioH3XboCZroM218ON5FZXo0XYGozqa8RXi9lU4XPT5TtwZjgWxqHt7-3z6yYP9WFrZzkc1YFNVXqC9ln5hEPZFUl3QtG7TunENDywDwJDE4SGjTNAU9aqLBRl37-7fgNSBi5iHzrgS-Q8CDBbofoVjqUGsGT9TUKrbW4EZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJPDBwWMN9XaLmx3ajiZKTa7FJp1oGKlrUccdDJNu2Jl6e1UNxp_fxFUdOGneEjPmxhcGlpbNFqBtneCsn2bjQsMCn4iCAaBFPaEuIX3RgzWE-YJhFuLu3y7jvzLBwINO5O8asqieGNdIvhOgxtAiv_G-JHU7LlX9igDjXhqQUmgBny6xznpt2zjtMz26KaZtVS5VyRdTSerAdhoT_u8v5ogcOHvrKqOt6jmPkfxRmy-9nraVz5FqX73ZL0ri8alw5unPERDSHS4rk1DAZe4M9uLnh9KGPjROBIKSNlL_MsbtI50X8btt2u_4uxiQvw6VHarkA73ToLYQUiWJJsimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-gXXk9PgOIsA8HVcmoY3oAO0lvtvHenNGuzH61Rsp8v2Ms1-WMTM0J1qsv9FHzQvJIR9Qjxz34yk96Eww3Y_Sc2Y5MoLaTqi53LonYQSY23xNqSO6a7ctCPnf9Qdzv4FrQn8FIp5nYBaCLxjbqsWznyKQjBAs90Q_uY_95pNP2udhkW1ccaZnz6AL3G-XeXIIzUTaoue9Ia1KOJukG9_ySlsopjuVjLFJwA7UUL48kdpKSmEcbQaFOwOX80iQRjOyj2ECp0L1DiW__ZjUSvVJFmKtskKPd_YqHfw-dcMJQYMxhfzpJf3_bBcZx-Vv0_UDr0rqcAQIodQ-w9ELuBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klyboOqUL3FMdgpblny6SkHjCkswMufNuC50voOY8Aj6eOwWncODOwOyhRXdCD0geL29kU9DqFVTgNKsd_I0uyv_kJbit6_mQepKudqQ5b-_ZGUDGM9YEEgP2uWD1FldlRTDm8dxefqorBcSxcGSq5i3vXXK5PocYxZbvTUU7LLz26cZVVS2yv-HJoUVPQqoibS3e6aJUsgRljDWRi0jvNYFCOmqZ2OCF8TjBdt8BQJtX--72lEubaOiXMPOR6Unx5YxXqUaR4erSnvF5hl8te-zWI5eQnRc0CFuinhEYo8wXCy0tILSzHfzFW9aX6Q3oN4DF293sQV0CgnCzhpBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7fq0TzG3aKgmLnhsaerlpiQB66KdPN8pTsh6Aqd8IZdOT-VmEykKhE2pYUEqGE147Dc8tBD2eA3NSbaazBaTpjnhZcmXkO5A9SIKSW9I-x7hLNV6q4RecHE3QbOQZrj4RGVD1oMcWr0scy1N8yBW-ml3F0Xr4kS4Eym03km1VtWvPHI_caaP7ZeuVb13ufENmrQUzmVWjLj9pQKfQi0xfxN54N5zjWtCgJKduRjZcAIwc6UsFNLAAqzU7dr2mIXbB8ZdH3_gsSB2_nrw-ORC4djVG_Ze7rlIxAlfiW1qZNRmvSRglg_zJscravraD_C4rxrJeTC9o5x7k862gkerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwBFs80DOqDdBK4763mAakayPqH941EzD_9AKt_H7UBJgCM5Ouknn8kuqvTwIbgOxvnVbPRXdKbsEV519I4FtnT-B53TNaiheP0hF_CEhNB20gSk_s_ceqXO7FLNujup2TuSzu_cX3FhAA67JF9-ddTGS9_w2Cawm2N0kXqKOiLpSXbuW4jZw8zthdZ7oem3rfs4Q2bNqgLlFWT6EPnQb3fbfSd44w1a_8EqBtuAThHYq96DsO9MUn9N1FVC47j1CZ7-geN9GcyX7_WsgYgVs8jcn10zZqZW5W-qCDAt2Z-KidALVYpOqpLTQb_msbnbqlAZu5p06WSx7KG_BVnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=LTbMD3UFr7FKkTTqPKG8q9B-H-MiwwDttpeqH1wdZk7glONzkZTTHAgIM2gC-lgh31mAK9Xw8GEKDc-jAo6TTbLNZv2v_kleMYkvuMrrg2VJug5eGBkyVMs_9x9_4rl8fE3TFJpYHlS8bTt2mP77ayyb0_AoeSFZ-8yBOEysxVUBB012NHAln2YySIZmb8R6huKnvcN5L5zp5J4jssOpK517sEfVZsX8wrN_obyrItFXMDMWdePbsXxXGspIB_-e6VnVzXnWVI8O_T80eJD1qA8XmWzKJcnKbKPDsq_FoiYqf-JOu2G7Cw5CvCKjRWhYacrOASdk3n3EN-GQLquYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=LTbMD3UFr7FKkTTqPKG8q9B-H-MiwwDttpeqH1wdZk7glONzkZTTHAgIM2gC-lgh31mAK9Xw8GEKDc-jAo6TTbLNZv2v_kleMYkvuMrrg2VJug5eGBkyVMs_9x9_4rl8fE3TFJpYHlS8bTt2mP77ayyb0_AoeSFZ-8yBOEysxVUBB012NHAln2YySIZmb8R6huKnvcN5L5zp5J4jssOpK517sEfVZsX8wrN_obyrItFXMDMWdePbsXxXGspIB_-e6VnVzXnWVI8O_T80eJD1qA8XmWzKJcnKbKPDsq_FoiYqf-JOu2G7Cw5CvCKjRWhYacrOASdk3n3EN-GQLquYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN5YlpXjVHc7hL3pU97TG4JwV6e7lPJEf71htFZMPVsfxgSlHiTHoCB9hlWHzRxj6Q7D11tKZNyny7qEltXX9rTIZ9MJPaiX1-mtJYcLPajNErU3L-MMNWnuAeNeG_603FNfGY9LA5Kp4Au1ArEQmN-w_rfu0RXmOyQxmiQUC8Xyo48RGfjs0XlWOZ3AWO95LcmUbQ8HCcmLq6t-xle6VcT4ZJjZwYW4vfBkNFG2pYdTqehjk7O3_Q6UL4I6SzwP41ad9dEDEWDJh6WKVVwiT7_yyqaY8fjhkx0KZ8rS83Z9-72uCZmuaVtlVfQFqakLPl75-S7ntWUhuIQA305fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZG8Z4gQybXhW0Id7utW6hyEBsx75q8RodrZPoRuGYNONiyGqTcaCWDzTvC8zzpl5pLs2GeapXjnrFbIkff1ummiiVYYg3ZQun0GPV_ZVXDJhGpQO4Wpv9Xbr_hZ2YJi5-CkBFW03k_p6zRb0bgnEX2oVLcNl_XEJchiCwLnD_MAOycwuqIhsATzl_HFAF0rFUhI8hmaDBjy97nFX3_4J7Nj_CNJDzagu4y-WQgD2PXxHELJ9Ur_lnIXBt6GnbUJrASilCTwcmCBrcjgKVfOsVYodqYdA0fpVcy-ubggwQFSYR1HxYC7U50__HCvzH8NpweU78bCNPguFuZmNQcuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEvbFoingc2-lvz7MuuDe-ONUldtvxt4-bBnQVJotxGEDXpMm_KYW-6DDLZ2INcznqGBUfjh8-xkAVSevD0z3hYH867vdM727Ihnn_YLUJf8H-852SKxjeenWnEzC39ePSI8a2oOz7WJ5L8n3OJVVJ8mpsKgpr244JsKIyld2XsDaf01fSZ5IX6pIBqF_hOr2ub5vo96_EYWC14lDzQ7FO2tYXXc8pGbWXfYl5yQt5m-LoW9XL8Ot8yQaWa3HsyDvot68-Id1eBFztjX0G6wgttCTmK-wMi_ozM2mEouNQpK3DnRSeJim4P46tjMZeV5-DoP0S_BYIxXmuEBSb31Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHqGe98bu921Hi2YaXWgFIWZ2KeL6M0z3UJT69_0aPKpjzp-AOIRLbPLtfKozY3XCJa7mw3dONuf7dxWMWyEwGA1YflXV49Cs4s1wROHO79dxOSBRlEasWfTYs3omx2VEs3LsbTg5ahgLbf02zcJsikt1Dy7aKAIraAi1NsoZULnmVGvMzESLBkQH5xNB740rsn8hKsHH2wBhiM2C3ZsvnH6-TIo4-k2Wu_oqmzBsDofB5Sny3e3emwN8JfR1Djm6BAWEZGyc3kOamkK7XARizVCfOVcIO43PzT4P9OsTwjtlBcnlvav9wupE_Pima-Z9_2iTJwnYAASauYM9wGk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_qwkbBGXCGysVSgd9Soxl3oc_4GecNwB8CrWS2u1HmN7TXUPc6q5fLnsnE3CTOA9PAHM1JBcahlRhxt4jAB_18XcDiinMvnrKIKIBgShxZFCBmvcBhrAN90T0e-hTJtxzp_3YYLiP4jSO7MyloXU1SnCjJgh-8pKs9UG7gtySWnFt1FM7k1IT_Rokubr9k3VQUk523pUUJSwcMP4DqrsALuX_jP0vdvKsJSHLHTaHzK6utYdma1K8Lz9z1BRZrcVZItXi61agEIY_Iq6yqKeZaRdLaxVsq7xxCn1yhXNBaxCwDveIyTK5bXx6RunOWq4Pl5xBnrQdE5yVvjzShaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLeI33u21DRPmzA7d3EOIzBaVYBveIVbWXuldrElzwJrz7RpEq9oISgylqhawujUzBFI0O-0RV86Qa3RoPupawDV6yr6hWE1D9b6gtI7lROJ38dbMeYiW9Z3wfiBBKkrEIrolgPrWla4wr4edTFd8POG5z-RjWEn9pGLXa1KVUgl7ZwwEAPCDM6EreCihht442JGJjPHRl8AsuK-HHXzo70dx8mYRa_oSkv-sIBaCywlyBLCMBxcphUa97nTLORE-4kXBxZQJ2VwJT25C4IFMPUpWDjP1MMV2mXyI6IDFk1_iMOBP7QZ7E0vrE_qrv79ooL30u1Xiz3mfjmQ8KhGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksRXv4DJ3vo9BFsAmEgnZ9tqSdziO4HjTvnlX0vuIgj6KIbSNaBr2DLLd73RmXNNYGpNHmag83GrpEZHvzMnVo7kMmAwyknz9uDLhbWPOaoyLcMcT2Axt2-WUuo5T41UjGOjd33XxNLAbz4If-v5058z804dPxk3TA5oVYto_O4DmdSxZRRf-Zxv2docng4s1_kDnEkC1p61y4RxeyttHp5wKLBh_4yzeFQFdreDqogawC4UUHsRoYbPZrNKY5HyAqg4qAxOsnVSflgvl1-ar2iKybwaaeDDxqIriGpbb4jY_kCXUt6cM_2JWIEZXKoWtIDRDOtQ_kY19fQr_EohOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZw1VvD9Ai4-nYrRJ5eC-pg99ifQlACYX68XfYQ41K0NhtfkVMem_4eC4AmFbmQJ1whxlOGunw_fsEYxZlUaOLPvM7u7cD75CI8LwInUMta8BEGEBB4jJwVnMnRbSTIZ8E-lRlGEUOBGsko9psT-r-Z9W_Z8LqdIrFPkdg5w0mPn4Y07HsqMbhcuNUHqc8HzdZXqfxl1TC6NfYmTahavrcSx-d2YJ7Bhi5ZYIRlI0zSiotksddo5LoRk1Qb5bc9Tnkn0IGCNMa6T7aSk-lPNYAYcDilMWC2XYFtCAb6Wo_ipwNoP7GvvoYE7nq6lqadNER3oGeTx0w6pnQlFloALLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEGEbSOAcL3xingd4U9mXOiDBhO8nHf-xVhaBY_cNRlemnrtKvZmmjl1q-aj0X6KnFefZCyKoMK6nT_9Z2-6wtUuvdEuF9yO-fuc220fViLB0lcxYjAPYVV4G8-_NjJvl7k2jNpxNmhU09jh_zeiDZHlWCe-7MHv7IoyrFi1QacZNLQ1JiDIfaZXfmKnSMuKjfw5bhgLRxKbCLtiYMHAbVTdpD-bK075WsI8U5sJUfAzrr5_qMZYNvQOSxuDs-y37s6OxbosF591LaRihXEsIu__XsorPV_XrlsR4H5bQyfBH9r2HVJeFdAEM_vqFEm9f680SlpAFg89wqtUcgKAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AymkbmFDTLDUmA21uwJT1uJUwwZNsvOSsjS7TkSQkgP1V7laRWLPcfawelgrDmzcdpAiJdujmq0Co5EQ3YiwSAkdKid0M3mMwO1WZIRgKYyTeiSMxxZ_eK8OxiYTy_q1WIeJEAmPcIxfOgEBrZVqid2bLpGvEdCi9Z3Y6-v1PqQHEau4lJtdpDVAKSDyZ8wT4pWmmlls9wy3--VnbTWgdQ46FsruqhiQG9u9ByKvvlocYYXBwMHnKf_SSOYa62TX-xmnngbt0bf-ul6dFlBjj8PiH97RjRFkEe5jFWJdtfwd35J3irAVkarb8pUSsWAgrETwNP0AeNNF2GR0UEzXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4NyW-Z3VYcBHK4mXhksueEbXbzQqy86NBdYJmMGHPYEnjwokvIdE4APyIcyCRs3XTp_w1q73xLksuQguQb--FtAlpFfrm--0rftQAs1fajTSXDH-v0gCl0ovid3i3N0PUBVxuV4O6nHxcErFLI3OfhDnfCRWb1quOztg6EJ61djb4fk795sU_75pU_E5SkX9MvZYcMxBzRrUuDIgcgM8OplcfVas53hHp0unlaa5KIeOdIMFMeZz7CXWYMPxDV7gYvrGojv7xnhEJ_JuuJrrnPVD8sPpXcmTiVziQHuW8N3zpHSRiQbjl2qoaSCMx8Dda7QC-OObuZhATsyx8awLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=LRZMKPcMvNp0KuC6aL8zDyNML6OG9MHegDUPCIuVsEkto27ir7HOEzC7Y2eqT4eKBOtJFYJXlJ19pnjmjlxODAbUSiNJ67FFkzeaCz8onY9V7SWZ15A8Krc3fKDEhrT4ZXwSeUEZV-dpfpBR8c6kRyHSuPs9Viq4Ltx81LNW6zn05Eo3lXZsNKjAIKA3hpF-GhC2vPiHixXJ8bXF5B3wdnZy5-qqyInfX8wqZQeCGuAwCzHbLNYn8-ArYdt9H39Vewl2D1JCs0qUEJmTj8vTmqk8jZ0y-qSEC5jGC554IKlm3pssfARrI2n6IYDckb2ZlwTCXKWAGwxfTqJofY0g1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=LRZMKPcMvNp0KuC6aL8zDyNML6OG9MHegDUPCIuVsEkto27ir7HOEzC7Y2eqT4eKBOtJFYJXlJ19pnjmjlxODAbUSiNJ67FFkzeaCz8onY9V7SWZ15A8Krc3fKDEhrT4ZXwSeUEZV-dpfpBR8c6kRyHSuPs9Viq4Ltx81LNW6zn05Eo3lXZsNKjAIKA3hpF-GhC2vPiHixXJ8bXF5B3wdnZy5-qqyInfX8wqZQeCGuAwCzHbLNYn8-ArYdt9H39Vewl2D1JCs0qUEJmTj8vTmqk8jZ0y-qSEC5jGC554IKlm3pssfARrI2n6IYDckb2ZlwTCXKWAGwxfTqJofY0g1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوممممم بارساااااا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=qA-SDviApmwgY8iA3PfsNWe6yRXqNYm6XI3ULVwEJesRyxpY16bOZMxb24XdYQ6Ax7vSaRCL4jF8N5L4psBmapGH45_ETJ0dOIAkbVs_JVihITMmDtXZn0kqlxfpALThZ5lpEDTEJzTqLBcgPIUtoUF8uo5YHZoQqh6DM2ADvzUuUTiH6frRxAO5gycoYNA-Rz52qHYauxqdFCCIHevR_vX4tauoEaeULaakShYVWSQt2iRQZh2r8xaCqRlFNk4b6015bDa-6LykuiqKRfeUCgKsrYCSmSLlpg9SAyCMkd1wTJ7fnDZ6dRW3VJN9-HMkp--Jg5WwwCHOCYGQcjEq1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=qA-SDviApmwgY8iA3PfsNWe6yRXqNYm6XI3ULVwEJesRyxpY16bOZMxb24XdYQ6Ax7vSaRCL4jF8N5L4psBmapGH45_ETJ0dOIAkbVs_JVihITMmDtXZn0kqlxfpALThZ5lpEDTEJzTqLBcgPIUtoUF8uo5YHZoQqh6DM2ADvzUuUTiH6frRxAO5gycoYNA-Rz52qHYauxqdFCCIHevR_vX4tauoEaeULaakShYVWSQt2iRQZh2r8xaCqRlFNk4b6015bDa-6LykuiqKRfeUCgKsrYCSmSLlpg9SAyCMkd1wTJ7fnDZ6dRW3VJN9-HMkp--Jg5WwwCHOCYGQcjEq1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گل اول بارسلونا توسط رشفورد در دقیقه
9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWlkMDjZ4N2z1ZvE5oSl_3aSIAH9xvAQRcTQ8Ng-4wlmeMmRN2qBWtQfPv-bzHS0U2OC3M97u3NcP9mlYnD70qkj3D2Dw-X3qrLlquUjrkcC6Efzzvji3DRgmNiyY0wPS2hJ4gCSMM601tZGksvMKRg7lI05rDo26bfaux3jSQYxqH6TilEXjlgEQjvMpVCqC18X_xbnImBh3uaZS0tV_ARXyBWDIqK_q1LTF190VAPBy6wtF414A6qrcQZ3OwtuGwieTwDJqA0-lTLxf8t9IvnSC8RMYyg1g_Dkv6yPplRzVq7utmpE4cH4cY_vNoQgdXenRda8tXYoWXWSmuhEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزيدنت ترامپ
: ایران ۴۷ ساله داره با آمریکا و بقیه دنیا بازی درمیاره و هی وقت‌کشی می‌کنه!
تا اینکه اوباما اومد. او فقط با ایران خوب نبود، خیلی هم بهشون حال داد، متحدای ما مثل اسرائیل رو ول کرد و به ایران یه فرصت بزرگ داد.
اون ۱.۷ میلیارد دلار پول نقد هم با هواپیما فرستادن براشون، کلی پول هم در کل بهشون رسید
انقدر پول بود که خودشون هم موندن باهاش چیکار کنن! ایرانی‌ها قبلاً همچین چیزی ندیده بودن.
اون موقع عملاً احمق‌ترین معامله تاریخ رو انجام دادن، چون یه رئیس‌جمهور ضعیف و بی‌عرضه داشتیم. بعدش هم اوضاع از اونم بدتر شد با بایدن خواب‌آلود!
۴۷ ساله ایران داره ما رو اذیت می‌کنه، آدم‌هامونو می‌کشه، اعتراضات رو خراب می‌کنه و تو منطقه مشکل درست می‌کنه، ولی دیگه اون دوران تموم شده. دیگه نمی‌خندن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGz5Tiy0myKWTi9rmHo8y2Etn008kzJmMmZUf7M15m06LKb0m-pmc5ecrAYqrA_jJxcXkYS_0oWQCbbfFruRZ7ExlbxgdJOPF7RAx0GaX-uF80Fok9towY3oC3Sh4jxC-55LyJPJLuJKVtr5zyXapXA3Bn9Y2lTzeyQmcDXyNHMfut9e88F9nT685azb9gzfPKbOd1iN5HRZtf4gryjLeZK0ahshJjkiiro_knfJCeMql-dawSCN7BgoTLF_MjPbVFUsd1CMD4rLWhHmv_4S9BoP601HnT6_bphP59qS8sYOu4YFPJ-hXOlEXg-ab7krA5oMv0dihUr8YZDaWCjVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89852" target="_blank">📅 21:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrtGZXTpW0UrGxypmqk7TghfeUEzx6TpfVqnIZB1uS_aU3s_njNXNkeibQ2nrVyP83vj7k03Op_WO1yekfRzv-w78MbuHS2Xu9v6ksaAMdKtRiyM85moy7XGylnvdGfT3laPuh3e9SKJg2dmzoFPAepRBGdwAeQuQ6BskPkAAYy6DI3X-jmL0cp9DzimrNxBStIHTJ1DJTKDhBUaFpaYsxflNnlLZqB1Fyk8JtPRE_6Hxw5WZg1VkUUBs2HJXd0ksEo79dUcNcfkVJYjDm9p91YYjQ7Ys30F1iRb5pq1bHLmZEzHhOia480C15HElSJhGu3QNLq94Z7bsZD37VAL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترکیب رئال‌مادرید مقابل بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/89851" target="_blank">📅 21:06 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
آرسنال با برتری مقابل وستهم صدر جدول رو حفظ کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/89850" target="_blank">📅 21:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=Obg-QbriEPQkwJro4agIEGbMwtnKmbl5GE93jqWvO6C5gVX_e65cncWqW_okfaVZovYlyxhrT85o2-ujBOyEFye7G0CofVMQ1sz6PCAKcHr5L1ew-rnf2ET5ZhJrM1RCrk44JbxLqbLXi6290JZElds1sPgdet3X6sENtB0genT1tuibFTUFYUCAfEKWaY1EVJDxKfPpoBuCQCvfMzAV0XDyELL8njRc8lC3f13-tm0GJrMmXX6oBZF-mEEz2D9T7t_88Chw9zfp7MZRRgUBFT_nGDHgy3goGX9eHJiuKG9rQowQgYGM4V2q_0wX7lMHJMukIl7KC-pYHc2m6YDsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b416a65c.mp4?token=Obg-QbriEPQkwJro4agIEGbMwtnKmbl5GE93jqWvO6C5gVX_e65cncWqW_okfaVZovYlyxhrT85o2-ujBOyEFye7G0CofVMQ1sz6PCAKcHr5L1ew-rnf2ET5ZhJrM1RCrk44JbxLqbLXi6290JZElds1sPgdet3X6sENtB0genT1tuibFTUFYUCAfEKWaY1EVJDxKfPpoBuCQCvfMzAV0XDyELL8njRc8lC3f13-tm0GJrMmXX6oBZF-mEEz2D9T7t_88Chw9zfp7MZRRgUBFT_nGDHgy3goGX9eHJiuKG9rQowQgYGM4V2q_0wX7lMHJMukIl7KC-pYHc2m6YDsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
هوادار گالاتاسرای در بازی دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89849" target="_blank">📅 20:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57353990a9.mp4?token=Sy35JOHY6LJYaPfUvckMiTgFP72wkhcm-ZAz29-KEMmOQOem76hxb-tUg1HOGwrjjxzZPEwXNxFpMagn23_4ebFibUHG0CTW8i11HMuXnp9B0cKU0qNQMxds05DY50NBv6aRuxwT2NxQRNP3p80qfaXjlsL29jkRUTdAoUdrqavaPbzhCCkoG24iZK91m6iX18ZSr1lpIG6d2s61sUceNOVeKM22Hy1x6A16EuS3vqhLtVJGG0ohpmNmq-PXgB__hqc3pZ_5CNKfcL2DDd14pybG3ZcJCrZxkgymjhzvmkf2nuaxbn_xKWpZNDVDDQVQbmsCWm9PhpysUwm8dE1oJJvvXh-sJT8hNB3Gt4cF0zjHAMQgxIaRNTs3nFxHkOn6vQgIULMncj_jawOee-KkeW_Z3ro_bdlLIxGQS5WyLnnmWlv56qUWfNlHxcpWoZXL2SLFeeSFcK3AQjgtWqaZ_xtyZlaR-JWnlOY2sfeHapHxr6fMP8qIbLZi3jpoiwPm6n0teor8PDF9VkiyDZsb7FT8f6xQbgeje8koVUNgzpc3-H5ePbBkrCYodR-FPx_1JhC5wDLvZtGd1pJk-2HkZR8dSEMiVQJ07b0BKOdbiwihCGlQs1uJNbLHLMPLpzZ9181CFmLwaSrzz8wPziJ7seRxUjpkRZMQ5RV_rb8mhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57353990a9.mp4?token=Sy35JOHY6LJYaPfUvckMiTgFP72wkhcm-ZAz29-KEMmOQOem76hxb-tUg1HOGwrjjxzZPEwXNxFpMagn23_4ebFibUHG0CTW8i11HMuXnp9B0cKU0qNQMxds05DY50NBv6aRuxwT2NxQRNP3p80qfaXjlsL29jkRUTdAoUdrqavaPbzhCCkoG24iZK91m6iX18ZSr1lpIG6d2s61sUceNOVeKM22Hy1x6A16EuS3vqhLtVJGG0ohpmNmq-PXgB__hqc3pZ_5CNKfcL2DDd14pybG3ZcJCrZxkgymjhzvmkf2nuaxbn_xKWpZNDVDDQVQbmsCWm9PhpysUwm8dE1oJJvvXh-sJT8hNB3Gt4cF0zjHAMQgxIaRNTs3nFxHkOn6vQgIULMncj_jawOee-KkeW_Z3ro_bdlLIxGQS5WyLnnmWlv56qUWfNlHxcpWoZXL2SLFeeSFcK3AQjgtWqaZ_xtyZlaR-JWnlOY2sfeHapHxr6fMP8qIbLZi3jpoiwPm6n0teor8PDF9VkiyDZsb7FT8f6xQbgeje8koVUNgzpc3-H5ePbBkrCYodR-FPx_1JhC5wDLvZtGd1pJk-2HkZR8dSEMiVQJ07b0BKOdbiwihCGlQs1uJNbLHLMPLpzZ9181CFmLwaSrzz8wPziJ7seRxUjpkRZMQ5RV_rb8mhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جو اطراف استادیوم نیوکمپ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/89848" target="_blank">📅 20:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89847" target="_blank">📅 17:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ: بالاخره به اورانیوم دفن شده ایران زیر زمین خواهیم رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/89846" target="_blank">📅 17:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saml34MyuTJ77qu6N8q5V2DhHGMTtGy2k51HQv9AvEkza8tcm8HwtIvjRdW00v1SEbKg4DjeXf2N9W3o4ArYmVPZsvZ1Hq2dL6gJqjeue7DWsPNwTKcGWORHyn0nZ_t00pD4Mt5wbCNER3l08l8oTDOe2zQSuk1Rq_x49HN4D8RGmhCVqUOT0jXEoWMxCToH2ob96YGLfu4L4sIsw-mZ2lO0jvneap7z00ATrMvc7PzBtHUjbtAwcQCKT2TZ1kU6duWVDT4EXgrK4ubWUoOCy3KNQuITqashz_S-VSoXEwPgi-YDct-VarWt8UAj9oiAQY_sHK-vBfr6wnb6z75ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
منتخب این‌فصل رئال‌مادرید و بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89845" target="_blank">📅 16:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWJoX7nTVXdK3K5c6ldK3JgE0uxH8-Hfvy70rpkaur_DhLYyAqbtIIMpu9lgvQKPzrP6IRTW7U1Ixp8-BFu9d8plbpOa2hnNVkJLTeOLv-QvI6Q2tCswgCmkKr-9OBjzORRqo7S3ShAmqpgEDCDqVFOUwpDGg8vzr4fOW9SVbaLo09x5y8zW0Nv6AnQqlSNgQnA3z_Vye8jqrzrcAeiOk5IW6jl5-ds7_fBjQxN9OAujZk1qCpwSBMd793fkjMZmX-PE03h4NBc5LvJgoWjJPjll0JVTnMaEhp1RfZGK7FnvwzZDrKdofJWDcfArGPvElnrVgmwb7ChwzYqL--dLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
هانسی فلیک در الکلاسیکو:
‏۶ بازی‌ها، ۵ پیروزی‌، ۱ شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89844" target="_blank">📅 15:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utkbWVPExJrhehq959fR4Fh_zCCDfDcKtMivFuF3M2Qj7md1Xn1DxqUMUkAZf24XcfULnc5jJoDg4sx_iwhkgvujTjCrNaLR7IuXRSymTnkkcOS6RAmCoGLWGkWGblq3rxxcgmxjlJd_jqPVYcC4koBazEtXjSGdbjl0WuAhwMBRkk_IIyCoHNgyPqkUx8BjEuN46czQqD8KxU6u-8vAhpVHPgrpRY5FIXpbDK4QvVAYDHEQQ5JqI4AVBAb4fyvVMjfHru6d-K_wlXk6wVuyrP_uNKc_zjUYXQU0i2nCm-Sob4GAVhe99e5KIgZ5Vckj-A4DwAD5LTNV5zNEyp4hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89843" target="_blank">📅 14:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
امارات اعلام کرد که با دو پهپاد مورد حمله قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89842" target="_blank">📅 14:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNGvzGT9l1YTVzNg8WazPWt-tvyw_buw0ZNuN6oqm0dM8_rTzK_3wAvphy_c4FfhxcHqwYkAMsTeGKghpC6z_ippyDg5D3hL1rKj_B9Mq3E2LMt70BwnBcXashonqWJG4cRPPG6ZYDqkGxHQbAFV4qGfJ3qmmc1f4j5-GdE9jdHTvCUB7-Tlw73m-ZJ7qdgw2ibpQuL5j8iqZ2klzMKt0wjjhqg2ud3ZuJDNnzu1UQyNSVyPcXRMu9N87QJAiyG6ZaxwQbtIDc_XQxeevEHAgF6phUNuV-2kKmFleCcygr0wkEGy9kCp1ENkyQuRu8XK0e44BFWRSS0nIumB73g_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پرگل‌ترین‌پیروزی تاریخ رئال‌مادرید در الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/89841" target="_blank">📅 14:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89840">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXIInpIOaPhkJnnOYp3eE6rZG-YKVL2mHZy-GqIZM9OQcMk6VANrMEEcgwmGBUecS-aBH_1u__n7wQiOmXu0F6nTxl3nH4V9naMn9kdUo4tFqQuQdAP7qbh_C-W1xqRgROccZA7pK9tRDaYMMd2Y_8KyDOaBPJ57reNH1GkVtBTb8kD_Zb2G8i92UZZGKjf_o-mjpMomHZZx5xMQzdX0ovDLzR08UD3RLXMTA_h1Grn_WIjq9nlLdL3cMXspSkVL9H5LNMDeC0_Lk08QsR7HueSUyu50tU1B5dYON8qH1TBQUB2HNF-098pP5Ilg_6_LnZ8ZA-9XCE950-Lg6Eq8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
در الکلاسیکو:
- بیشترین گل زده: مسی.
- بیشترین پاس گل: مسی.
- بیشترین تاثیر گذاری: مسی.
- بیشترین پاس گل در یک فصل: مسی.
- بیشترین گل از ضربات آزاد: مسی.
- بیشترین هت‌تریک: مسی.
- بیشترین دریبل موفق: مسی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89840" target="_blank">📅 13:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89839">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Mmi1P6NR5X6NFCsvNu7WVJfUZA3-jihh7W_sT-NcYUpISs9-BRfFsoCxAP7P2M7TLjQ3S_GLbHJTzP8aInlQiM6BrRLonAUamgDdJR6aPWMzpwK6DsSN9-8DtH0OkdWHxAinKLKGcLAVUPlTH5qvb5Xg9xryS0B0jdYErKXwN4-bjA-m9zhVqItzznY04s6-jngzwtXA97wuFKAK3gbjoR8XScJaVvU_JdYLHpZ9aylmGPtepGztJgBCvtiMdjUdzjh8RO83WhWWZqBONxXf5x7joYrCqlCEHv-gOoQdP9K4dJW5sRgMVTBIlcZopEGzEq0HXB2nVVPK0hM6qoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست رئال‌مادرید برای الکلاسیکو و غیبت امباپه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89839" target="_blank">📅 13:24 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89838">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiGp5vX4yl2mlD2-VeG7xwX_2khRoBt7Zft_7bEgV9UvthPDio9V-gzTKYterJg33elE9FciCdSL0zRpAH9I3mjAX4F-bxWRg0Zthx0KPt8HXKJVKxkXObfsMobcQ_yyBFqW_2gQsBL0jWOO24jGxjRIrjBMgtQYdvYiAv7CJy-4iHjVRDoPvoBcxhgCuv2t3xBF3jdb63-ZCc2PlR8HdtbWp5yWndAHq3wiWPtvaf0U54aqypqm0NryK-oYHS6h-mmuD4g0DvrKI_kbO-pndkZMUxUxQPY4EagLbpxi7ffjh3YEfVzUuEx6tYq3bvBq7TawP911_SX2QrgINxRJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین گلزنان تاریخ الکلاسیکو:
لیونل‌مسی ۲۶ گل
كريستيانو رونالدو ۱۸ گل
آلفردو دی‌استفانو ۱۸ گل
كريم بنزما ۱۶ گل
رائول گونزالس، ۱۵ گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89838" target="_blank">📅 12:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89837">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=XObF0Z_HeqsNbTcBHuhF6L7cvaC-BN5JxctirWBeDcGwFT7YZOFkdDMJBoqJy9W1QzIA4FGWUKvT_Lut6GcFXGwQr_diFOBgvIaDz7wF4cnzMTmOQDNHzjf7JJA7bpiuIn3JNpKAoCzWXFkgM_T3As2z_7xZd_a21eB8wGmazj7y8HQQ7CFcbg1ReX7hMEVjfADwueEtFWb9bz3VJ1ehJx9WBlqEOwg3Wyv3tfduKNHq2qcTg2-fdxEUTwm3H9nafdLcZFZJD5tG87B6UumohIqLYZbPrr-neFDECfS_pDNZOoFaPbnqSfQoZlJ4Xcd8NWOqXYe9WmQLONpRc3KAXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b811ef34c.mp4?token=XObF0Z_HeqsNbTcBHuhF6L7cvaC-BN5JxctirWBeDcGwFT7YZOFkdDMJBoqJy9W1QzIA4FGWUKvT_Lut6GcFXGwQr_diFOBgvIaDz7wF4cnzMTmOQDNHzjf7JJA7bpiuIn3JNpKAoCzWXFkgM_T3As2z_7xZd_a21eB8wGmazj7y8HQQ7CFcbg1ReX7hMEVjfADwueEtFWb9bz3VJ1ehJx9WBlqEOwg3Wyv3tfduKNHq2qcTg2-fdxEUTwm3H9nafdLcZFZJD5tG87B6UumohIqLYZbPrr-neFDECfS_pDNZOoFaPbnqSfQoZlJ4Xcd8NWOqXYe9WmQLONpRc3KAXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آخرین تمرینات بارسا و رئال پیش از الکلاسیکو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89837" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89836">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re21CgGS7ytcMTJySGq5dL7_wnUYaa95sD1QiFmSth7EBCAvXaLWFtbhVbQjs1JYnx2A15AfyHjtcqUAezsNvIYJqC99gourgE1zRlP09L7Uy0RYizbdurr42YIJ0_vhWu9wA-DKbdchxaOtIx3g0neaU4jg_7ZlBaMzSVZlYk7-Se3egvtwt_Kcryz1jOoCduQWyp9K9-GaM-e7G03I9Xml765CinlLV3NZ91NgFyzkXti2-_ToGi8JDVovdjWrG_eVfnCR5YEFb7C9yE7oUgDQhItUFfeBByf4HVOArzqcZnwNFE04eHllCeUdAnHflfXzqyqlzqeeq5H8Sk89Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رسانه‌های فرانسوی: اکسپوزیتو از کیلیان امباپه حامله شده و دلیل ارتباطات زیاد اخیر این دو نفر همین موضوعه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89836" target="_blank">📅 10:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89835">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSJ3URzyhgwKtIerwnMaPBM4CIWrYZEgdpyDd-r2Zgy4a2K1zQArYtU7k8DZU1G8pkvxEMUVID5wxuLvbzYTbxYEVx2KRIQHn-Uif4pT6rffePWIMtAnesw0J1IaYK24uGYqOhO0jUM4b9GctT8oM9tycVVRMZuchYCe8wxfvSTjRFd8u2TLC24_G8hl6VRgbw9vqAXUvsdZ7L9FtyyOPIYYQnJM16B8_KSvtFoNi6BUuoGPG-9CgXuGOTVGdYUv215PMpzaF9EV2pu0R_OqDVbYeX2qprXSzbR2f9W0Zmlr8smbJoycuszJyBDpUvkk3j3TXqczpjYWYBbALA958Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوتین: پیشنهاد روسیه برای خارج کردن اورانیوم غنی‌شده ایران روی میز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89835" target="_blank">📅 10:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89834">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetUnblock</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDwkcYaCBh7Dv2SLbyLhnC_7A5kLlOzX5rCjOhPDtO-PjbuCsa9Ke8gnBAJ7xDBYOTgxSiH9d_EUXUi3K3_4BhSNmnlvi7AoYaEwnEVOK-ozpeR3DZzVT4zeKRGJNBA67en1w-Ml79KjWIUyfGJkBtJU75zZQqGwPVLqN7cHTCKhkJF6mGJOlXIkFxi0fKTnqWmt8ckoe8mZ1_btppPU3LfcYg2T1IVKYJKR-2EUvD4GH0CxiWvTuWcDYPK2l6v31QdLYDtKHDNddDGGoXGdT2Z4FD2xep15EpbDjXSwvDD4ilbZwifG8Jnn_MrOWFxPBQ3D0luX2Z5Ly4aWeQNE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">[
⭕️
]  سرویس ها با تضمین کامل ارائه میشن، بدون قطعی و با سرعت بالا همراه با پشتیبانی کامل تا اخرین لحظه
✅
امکان مشاهده حجم به صورت انی
✅
تضمین بازگشت وجه درصورت قطعی
✅
تضمین کیفیت ، سرعت و پایداری
🆒
با توجه به کیفیتی که ارائه می‌دیم قیمت‌ها جزو اقتصادی‌ترین گزینه‌های بازار هست .
برای خرید و مشاوره پیام بده
👇
✅
@NetUnblock_Support
کانال مجموعه
👇
📣
@NetUnblockVPN
🤝
همکاری و فروش عمده پذیرفته می‌شود
.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89834" target="_blank">📅 00:27 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89833">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: ارتش اسرائیل طرحی به ترامپ داده که ظرف ۲۴ ساعت تمام زیرساخت حیاتی انرژی در ایران رو نابود میکنه و جمهوری اسلامی از پا در میاد و وارد مذاکرات میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/89833" target="_blank">📅 00:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89832">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez-IjgMQ9pzUm_N0SGnRtdQSGYRif10wc__Zm3BgUyZonnX418vE7lkb1kHNi5_31g1KPAd-n6sH7w5D0r3DlBwFfxTZ9VjwcRjJrlvHDJP3dPQJe8lh_LNMqlzVIqTlgNlL2xqI1YwwbynQQmsuS7bRj4qqDVXoM4aNy9l6or4BsadqmhzjzbxFNXtjP9ITmFw4pPX67bGB8blfxrBkKvf58HCFO7cQKD5lPxrvU6Ig2IQChf9fbByUUQ2e9kvP7_6CajnMls62MdTeq5HAFIVP--3_wVNa_whFHvmFmHlyghD7sSOIPFkALRlD0LptH9gETZAy3JNXOdQtp5EZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آخرین رده‌بندی توپ‌طلا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/89832" target="_blank">📅 22:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800   برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/89831" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/89830" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
