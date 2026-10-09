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
<img src="https://cdn5.telesco.pe/file/jlSAiZedoNi25chbWgZLm-dhx9nW6ZejrJPs3XaReOyfP9XbswbV6NhO6fQGe-wfkuu8FdnK0z_ib7SfEl25laCTWEZTMfOIhCI4FThEQbNEbEPMFmp8Rr612zK8GovQtDZmwfZX5oW5VUaW-I7xMJ1_omsLCqZBxuD9ytLnC5jfMpJFgOQEO6aBioytcJkqRwaXwr75pjA5PJ5PGTRYOXCTJB5RHK2607W6qFuJzfY2KbzjeO_XqRMP5kaUA_0Nss_Ns6DmBjESl3PCaDeLxGf6PvLQrC_RdGsbwuY2aa7gFaJoDH_H5ykp9-ZYY1mIx6sWrADex6Eeg732zb_gLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 387K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-108201">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=OeIq1KElmNnLha0ixUBg1UiPJrbiK0kT8Nx8DnsBCVgar1nF1pGmZjdTn60zUTq27YwewnxUo6n_W_tajQW07yHvtEGOO2oR9wIheUAQuxY6ZJVG7ITsaXLIDNeMtPhpeWpQPtWXo2mbMof1NrjHHktL7vXFSYa1pCvCcWJsVoDRawXGHGDmghgFVXOQ1qNBd3fljWhKpg4SgUWqCdEv_2rN0kLjcJGv2NM-CA4ATcO__Fz3Yy7lVo6qSEGxv-wToKwDR1wVzrgZhayNxA-3Xj-hWhRb5YODTI2-BT0r2cyPppWeZgQuhjwiexGkaKbK8VIMuenrnvD9UMlV_5HtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=OeIq1KElmNnLha0ixUBg1UiPJrbiK0kT8Nx8DnsBCVgar1nF1pGmZjdTn60zUTq27YwewnxUo6n_W_tajQW07yHvtEGOO2oR9wIheUAQuxY6ZJVG7ITsaXLIDNeMtPhpeWpQPtWXo2mbMof1NrjHHktL7vXFSYa1pCvCcWJsVoDRawXGHGDmghgFVXOQ1qNBd3fljWhKpg4SgUWqCdEv_2rN0kLjcJGv2NM-CA4ATcO__Fz3Yy7lVo6qSEGxv-wToKwDR1wVzrgZhayNxA-3Xj-hWhRb5YODTI2-BT0r2cyPppWeZgQuhjwiexGkaKbK8VIMuenrnvD9UMlV_5HtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل سوم پرسپولیس به نفت آبادان توسط اورنوف (84)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/108201" target="_blank">📅 18:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108200">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=dkA3upDnE-93uQAjaOG5SQIQ7zv6ybC6ibGrk8IVPFHOLFcdG2edjixEuJqKGY941nak8atxnu8rYDLVbeatj-qoLoas1IX2rXahJDtf63qhmVzELLHH9RVyuhFJoERwyVl67zCrT0D_d7DpdjGu9Jm1MmJinT5Z9OySwdJYqROBT-ZMEeMBRgxRzU0CtUvkRftlhTo7emH59ynV1Ybhs5OFZxwU4qgHFx-DJsRhbMHBzPzIyFeuh8yL0AkjXhgbz4BHcXzN_AW-YubqK2sPb_KwVna2rNedXO4VTELenNX7yw4mbYKc8Uh5maknM9KRfgn6T-qsgH7ioGMN28G4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=dkA3upDnE-93uQAjaOG5SQIQ7zv6ybC6ibGrk8IVPFHOLFcdG2edjixEuJqKGY941nak8atxnu8rYDLVbeatj-qoLoas1IX2rXahJDtf63qhmVzELLHH9RVyuhFJoERwyVl67zCrT0D_d7DpdjGu9Jm1MmJinT5Z9OySwdJYqROBT-ZMEeMBRgxRzU0CtUvkRftlhTo7emH59ynV1Ybhs5OFZxwU4qgHFx-DJsRhbMHBzPzIyFeuh8yL0AkjXhgbz4BHcXzN_AW-YubqK2sPb_KwVna2rNedXO4VTELenNX7yw4mbYKc8Uh5maknM9KRfgn6T-qsgH7ioGMN28G4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول صنعت نفت به پرشپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/Futball180TV/108200" target="_blank">📅 18:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108199">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=oERyq1ANngM6q34uPV-FaCX9eyaLZAiFW3aLlDu2okkEIQxG9gIobYIZiWc02KDV_oMmbVB7bcy2RVa8nIPPO3_ST-yb0GZ2LqLP0uH0D-Hk6N4VKyQk23ORDmxuja93kA5kMPrs2VM3MQ5gov-FkDfOno-RXmqqb7xX_93dPLQ5cZ72shzsBC3mORh2mIBRnWetaXptZnrNJ4wY868eUSllF1BrfNEcLjOvoIB7GEKHI5FPuk_GHiH9Z3IudjKzInYOc0wcEHBn-EZrohcynJt9FwEQkYaL7Vw_yDqgq9ge-vYEEvANJDnZ4fUym2YClcDHRiKUQss9BwC_rXnx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=oERyq1ANngM6q34uPV-FaCX9eyaLZAiFW3aLlDu2okkEIQxG9gIobYIZiWc02KDV_oMmbVB7bcy2RVa8nIPPO3_ST-yb0GZ2LqLP0uH0D-Hk6N4VKyQk23ORDmxuja93kA5kMPrs2VM3MQ5gov-FkDfOno-RXmqqb7xX_93dPLQ5cZ72shzsBC3mORh2mIBRnWetaXptZnrNJ4wY868eUSllF1BrfNEcLjOvoIB7GEKHI5FPuk_GHiH9Z3IudjKzInYOc0wcEHBn-EZrohcynJt9FwEQkYaL7Vw_yDqgq9ge-vYEEvANJDnZ4fUym2YClcDHRiKUQss9BwC_rXnx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل دوم پرسپولیس به صنعت نفت توسط علی علیپور
P53
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/108199" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108198">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PNI7LROcijfkFRwvSy4ngu2w2vpbfehHOXKnq2PdTbIcZZ6G8N7JqmCK26B_e4TlWyM65u7eAAMRUrpd4_StkWPq92fD6dlFYAw5eG0qiyrr5cekgxZ3nRNc2ibTxJisEavqfuAzD9PnW56QSW3ErMOkfJQ-wnzRoK2e7ikuTtFTru3Asx7EW8hIoXp-bO9A6ga3Q57zsP8H5aQccP3wllOwL2lYJp4jyobYq-QcxahFkVvobQw-gNcjvu4aeZN4IzHV25SWRsgHgOa9SVOtVt_6h_2ykJ-y64ekmqn3aoIEYmgpad3vLBICf73nuSOFddDHY3GWkypFg1W2grNH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PNI7LROcijfkFRwvSy4ngu2w2vpbfehHOXKnq2PdTbIcZZ6G8N7JqmCK26B_e4TlWyM65u7eAAMRUrpd4_StkWPq92fD6dlFYAw5eG0qiyrr5cekgxZ3nRNc2ibTxJisEavqfuAzD9PnW56QSW3ErMOkfJQ-wnzRoK2e7ikuTtFTru3Asx7EW8hIoXp-bO9A6ga3Q57zsP8H5aQccP3wllOwL2lYJp4jyobYq-QcxahFkVvobQw-gNcjvu4aeZN4IzHV25SWRsgHgOa9SVOtVt_6h_2ykJ-y64ekmqn3aoIEYmgpad3vLBICf73nuSOFddDHY3GWkypFg1W2grNH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض شدید تارتار به پنالتی مشکوک صنعت نفت
🔴
@Perspolis
@RedStarFc</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/108198" target="_blank">📅 17:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108197">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=l_fxWCnSGAN_pMLsqJWoDTZ1KN4Bs2d1GKnHiUm4AYX7rXx6UMfTMFNeKV1R9dSN2AztGZ_6LA_3ltemesV8wdKDivYEfnIYrXzfIQNsNSIsX18zadbUpDA6iyjrRNcLO_g8EZoJI3DY_0qIQQnHd2fiKsaGt0_nDdRXy8oNgKv70nn4d5BfHuFnxUSaStP2AmSakrfRahBKun8mZxr17cd4AvCOXTy1WHGmXt99UzTcduapf6JDxAjmry3EvMruqc1O_8eQ1Ci2Q4xlo0uoI-ds31WZSe2_HTWgwpLX4LlDPl-hTuvbroNTJfJROxc4u-aNbdILtlGaPhMqm9AeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=l_fxWCnSGAN_pMLsqJWoDTZ1KN4Bs2d1GKnHiUm4AYX7rXx6UMfTMFNeKV1R9dSN2AztGZ_6LA_3ltemesV8wdKDivYEfnIYrXzfIQNsNSIsX18zadbUpDA6iyjrRNcLO_g8EZoJI3DY_0qIQQnHd2fiKsaGt0_nDdRXy8oNgKv70nn4d5BfHuFnxUSaStP2AmSakrfRahBKun8mZxr17cd4AvCOXTy1WHGmXt99UzTcduapf6JDxAjmry3EvMruqc1O_8eQ1Ci2Q4xlo0uoI-ds31WZSe2_HTWgwpLX4LlDPl-hTuvbroNTJfJROxc4u-aNbdILtlGaPhMqm9AeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه عجیب سیروس صادقیان!
⚽️
⚪️
گل اول خیبر | امیرحسین فارسی '35
چادرملو 0 - خیبر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/108197" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108196">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108196" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/108196" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108195">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeh2yRUmyov_62oYHFEX60OsWIL8rsgmEUIigr7NeA1FgFU1k4wwi-ER-_9EtKD6APwlMQIk4HpVbgJcneYmbtt9k4GqtWR4vOxVlsBfuNj-D-Fj9TzGXU9UA9DAZuRzSPt3F455oocVRncRUah4vfkCvr08idCeGXUpiMpxE4Z0-rN7tclAXvBwY5VuzY5O_E3njpLfkD7CBf_7WoN7yqH0q6KoivfAkJgvPpNa51kcewcXbdkcNepTbTHtXszN85IFiajYe3R-A3sqBih_VWMI9TMR-LjnUBRIhHGY5lk_s46sTqJUgVEDo_RMZBNLQ4exR4CWgCWyf1cO3qDeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/108195" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108194">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/108194" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108193">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=aATxPaMJyKf6TK5ul4OAoOhXAEtguAxN-QskwWyr8dAExYwTvAER21pX8wgNbkjVrfc6LqMhG7dOw_s1_9D8xmg3YwpRSWmDDaphpdj_h_iWNhEXZqQrh5RgR0zu2qTkSjGleqFpS8VaBUYIvK_La4P6tXgPzCwjA-iepXcFiGXJZ2XB6ZdV1tZXtB_XX-PzjurZMbq7n-8Ro0IXz_d6BuoTY8-Pn3bCWY6ZIkk6LmXVyk6z5ohC1g0PqycTBugcOMYdLdTlSvk0H9-iGHCb5_xG5s1uK-d9PHVF87JDiAJo3PR3Rn8tin2jeSLGxRmnpc9hTxTtezytkImZlc58fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=aATxPaMJyKf6TK5ul4OAoOhXAEtguAxN-QskwWyr8dAExYwTvAER21pX8wgNbkjVrfc6LqMhG7dOw_s1_9D8xmg3YwpRSWmDDaphpdj_h_iWNhEXZqQrh5RgR0zu2qTkSjGleqFpS8VaBUYIvK_La4P6tXgPzCwjA-iepXcFiGXJZ2XB6ZdV1tZXtB_XX-PzjurZMbq7n-8Ro0IXz_d6BuoTY8-Pn3bCWY6ZIkk6LmXVyk6z5ohC1g0PqycTBugcOMYdLdTlSvk0H9-iGHCb5_xG5s1uK-d9PHVF87JDiAJo3PR3Rn8tin2jeSLGxRmnpc9hTxTtezytkImZlc58fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/108193" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108192">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=dXi8PjzfCSExgmJE07GxHrfk3xXyxhOW3dXA8l7CT_cOH5NcjvZNWYWAysfUO0OkiAuCObpPonscLrPZGa9NikrmhGYlf9RCkeKfPOp5APDJyiOrCT1fJQy9nmwWYqnBls1cDMLZEE0gpKdvPw9lCFFDEThsm9aBUXPYWzBLV9YIPSZB75h-Vcd9oGiFs7EDpa-DVS6XFZwaq_DG61sXeBA2iFgbXdgHPNo4lSp4C50nLegg9CCOZyc2iN9P1CXEYQcHalrqi9MVJ6DmMh5SAVqYn7Wi_r4tTJboMj2g3-BmhsIwk04HCSJUWaWBrXiSepQZUgdPGRLoGvGIZoNfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=dXi8PjzfCSExgmJE07GxHrfk3xXyxhOW3dXA8l7CT_cOH5NcjvZNWYWAysfUO0OkiAuCObpPonscLrPZGa9NikrmhGYlf9RCkeKfPOp5APDJyiOrCT1fJQy9nmwWYqnBls1cDMLZEE0gpKdvPw9lCFFDEThsm9aBUXPYWzBLV9YIPSZB75h-Vcd9oGiFs7EDpa-DVS6XFZwaq_DG61sXeBA2iFgbXdgHPNo4lSp4C50nLegg9CCOZyc2iN9P1CXEYQcHalrqi9MVJ6DmMh5SAVqYn7Wi_r4tTJboMj2g3-BmhsIwk04HCSJUWaWBrXiSepQZUgdPGRLoGvGIZoNfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به صنعت نفت توسط تیوی بیفوما در دقیقه 5
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/108192" target="_blank">📅 17:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108191">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=AVGFUxyJfqIkiLh556AiaC9jirQbpaVpVmnF-h0ohhQRnf4YlUxl4oBza3vePR8EDVDxMDqzJKtaNJ0tsP_w4mro18i9bc_FXzp7mzSG4aHHzA2RHRgeMqdTall4vy5fbd_j-Tzx3LYhsjdlPrGhx878EB7qaDtk_ZKEx7Fb57VlbqE4Isu-AKFEFukRxgAKLogFD86Jzp_oq4PcXC7481GoHdEHaC9ZAFLwy9sq5FlfwKy8acNQNFKTjqIFJI6EXKKErpLtg7KxjP3rNgrc0rUhx3l6dXgO_6cN4ZN6-tbU_Hm4zqSdDNnXPwV7HG9Ehj-NN-zSTFFvD4DyW4LgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=AVGFUxyJfqIkiLh556AiaC9jirQbpaVpVmnF-h0ohhQRnf4YlUxl4oBza3vePR8EDVDxMDqzJKtaNJ0tsP_w4mro18i9bc_FXzp7mzSG4aHHzA2RHRgeMqdTall4vy5fbd_j-Tzx3LYhsjdlPrGhx878EB7qaDtk_ZKEx7Fb57VlbqE4Isu-AKFEFukRxgAKLogFD86Jzp_oq4PcXC7481GoHdEHaC9ZAFLwy9sq5FlfwKy8acNQNFKTjqIFJI6EXKKErpLtg7KxjP3rNgrc0rUhx3l6dXgO_6cN4ZN6-tbU_Hm4zqSdDNnXPwV7HG9Ehj-NN-zSTFFvD4DyW4LgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: به عنوان یک لر بختیاری از بیرانوند متنفرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/108191" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=vqgQVNXFR8ILDvWzMASM68_wUitO1GwMjsv6nUlIUt70x_NXrvlpcUgu92xPRmH2LGrn26UrUzSspsM7ix8RPOJEeukmNrhvWMepT0XsCd46pEcSHzMO_iZjdUjQu_Ams53d6GlsBx49fHertkbSCTXcigrg8ndT61uyom7BnWsIvC3fVwk0zO1vyWHakRf9AHbOxAZC1YLmZxwWFfv5W6bSzlDT1mYI0t7y1rSN6OE1vZY37ub-YfNa6CoFT-7LcwEqt6ei28gN5kSNSOCCVDYVcwpEnyEAD-_C1xzqnlUGJ0DIfs2hH2cfdlUwJJ5uqzsje6h-J0xvQaYqyJGmvwgr9vRtrbgHH3CBUQ0COGfhbLIpOm4srTYgN807sb6jZu3PWnakudkocbeLGIYefKK-m3-XNkO_cVuxYPG3iaXzwnILBwEQJGt3bFWV9_mDQEPqhqfLVr18b6u1bw-9XtvzpZfiHYU0zrC8U5THTY0PvT9Xqx2dfIrkqxsgmLwFWzcwJIzY2lz66AeEX6voLVoZX3u-s7Z_hThfSXLTjLPZ94eJGdUHJNW6vbr5Wko5Nj0A4YzBCBNCLqlorLetKNGDaPQ6lIQZfZ3gddovz6ssacL4h6QN9Xmga7jr7td7iVUKp5z-J6Guem9XuglagkuqgCRQBvkQThO7_ZtEaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=vqgQVNXFR8ILDvWzMASM68_wUitO1GwMjsv6nUlIUt70x_NXrvlpcUgu92xPRmH2LGrn26UrUzSspsM7ix8RPOJEeukmNrhvWMepT0XsCd46pEcSHzMO_iZjdUjQu_Ams53d6GlsBx49fHertkbSCTXcigrg8ndT61uyom7BnWsIvC3fVwk0zO1vyWHakRf9AHbOxAZC1YLmZxwWFfv5W6bSzlDT1mYI0t7y1rSN6OE1vZY37ub-YfNa6CoFT-7LcwEqt6ei28gN5kSNSOCCVDYVcwpEnyEAD-_C1xzqnlUGJ0DIfs2hH2cfdlUwJJ5uqzsje6h-J0xvQaYqyJGmvwgr9vRtrbgHH3CBUQ0COGfhbLIpOm4srTYgN807sb6jZu3PWnakudkocbeLGIYefKK-m3-XNkO_cVuxYPG3iaXzwnILBwEQJGt3bFWV9_mDQEPqhqfLVr18b6u1bw-9XtvzpZfiHYU0zrC8U5THTY0PvT9Xqx2dfIrkqxsgmLwFWzcwJIzY2lz66AeEX6voLVoZX3u-s7Z_hThfSXLTjLPZ94eJGdUHJNW6vbr5Wko5Nj0A4YzBCBNCLqlorLetKNGDaPQ6lIQZfZ3gddovz6ssacL4h6QN9Xmga7jr7td7iVUKp5z-J6Guem9XuglagkuqgCRQBvkQThO7_ZtEaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های هوادار خردسال پرسپولیس: اگر یک بلیت داشتم که یک بازیکن را پرسپولیس برگردانم، آن کریم باقری بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/108190" target="_blank">📅 16:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=cuPLTPxC0C3KEamDc6EDOYuwZDvt0KOWga6IIt_e8OZooWtVubNb3A2rnl82s73KXsO1QvSrsFdKDCh0Wp1JA2TLmwllx5w0DntQYuFf2PSOktHvK43INgwcYS0Um21K6hKe7KGFCBcs-5fm4FgjyDIQXKw0jVCsgxO86g3KkIO2C1GxoKExkajSzOFe6B0PTsbT0QGLSTYv_bubzAxxenxwDcf6NjodJ1XnXypR-YyR9XPCpfV94lkMiVevKIuf49fZ50g1IupNt524Erp9qjQlrHNW7-ZTkQwx1R0xJ9blIY6y1Oca7B4TFlM9tPVNJqlU342EAucDVTxWVCVb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=cuPLTPxC0C3KEamDc6EDOYuwZDvt0KOWga6IIt_e8OZooWtVubNb3A2rnl82s73KXsO1QvSrsFdKDCh0Wp1JA2TLmwllx5w0DntQYuFf2PSOktHvK43INgwcYS0Um21K6hKe7KGFCBcs-5fm4FgjyDIQXKw0jVCsgxO86g3KkIO2C1GxoKExkajSzOFe6B0PTsbT0QGLSTYv_bubzAxxenxwDcf6NjodJ1XnXypR-YyR9XPCpfV94lkMiVevKIuf49fZ50g1IupNt524Erp9qjQlrHNW7-ZTkQwx1R0xJ9blIY6y1Oca7B4TFlM9tPVNJqlU342EAucDVTxWVCVb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بانوی پرسپولیسی: به خاطر پدرم استقلالی بودم اما زود متوجه بزرگی‌ پرسپولیس شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/108189" target="_blank">📅 16:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXxKZ8zAxQ26hyJ94R9JEzFKKH2_MunmlpgUnjsxI6AV02fyAqflFG8mi5EaURv85SIfiC1tT7yMPxzu3MqcFRbuSepcL9dPDfFJE8aL0zUCW77SOSyonYWJ4smbEAoGQdaw6QlM45PetHbx7dj2WKR3hUsxGepjTmw0T2crWy38SZ55PvZ66Ji7jMCfrWk1awTJqD6g95mdacqES7VOj5kHypbqoiTBPB3sHjiid21F58UVUCaGw5zM2_41T5NFDYP_bCmM9riM3o9P9sGiNZaqw1pKk7YENgcjknQNvsCMau_GTAApctiGCZ89O-I9XewvzxZPU7J3BaEJXOAUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/108188" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=YzgS22Ypq5z8vK4-hEdwMFzkK7_yhALjAMo3OyAvhi2FBRXTT5Wq9wipPInydhAyGR_0DgYG_VZa0vn4k3BmOL31XsWhX1U8qzoV7PwM-cZhk464hn65vmlw9CIdR8Wcb8tzfrgBCSQLPqVA-qzyqbqcBBy2Qwcq7Tl0BkYoppZQ3ahMyaZWGsjQkHHhdQUzkvfIDVeqgSlVk0d3yg1CrshpEIP4HOAapn3mjPtLigWi3Z7CWIBJRzTJgi4BIfJlUaQNue8SmvrxhzaJxIAfXQI90wfsP_Cfn-J_hSYG5_wO1FBnxAHsG218QLwn5ryczZZHwXalUQSCN46mkgJfIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=YzgS22Ypq5z8vK4-hEdwMFzkK7_yhALjAMo3OyAvhi2FBRXTT5Wq9wipPInydhAyGR_0DgYG_VZa0vn4k3BmOL31XsWhX1U8qzoV7PwM-cZhk464hn65vmlw9CIdR8Wcb8tzfrgBCSQLPqVA-qzyqbqcBBy2Qwcq7Tl0BkYoppZQ3ahMyaZWGsjQkHHhdQUzkvfIDVeqgSlVk0d3yg1CrshpEIP4HOAapn3mjPtLigWi3Z7CWIBJRzTJgi4BIfJlUaQNue8SmvrxhzaJxIAfXQI90wfsP_Cfn-J_hSYG5_wO1FBnxAHsG218QLwn5ryczZZHwXalUQSCN46mkgJfIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار اصفهانی پرسپولیس: تیم دسته سومی هم پول زیاد بدهد، بیرانوند قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/108187" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=dvIOFYhbLqMKGhRjARnvQvhN_BSV93YjpD5sy811uIa0E9gCNrfvlqWpFxZ5RzQ3bZIF3spNNbV1O9C6A4U9zRVhVD3kck6c5VvYeBy8QOe0igiLDAfzqFGkCnHVH02wKdj6ZF6dNuft63ghM8A8WPip8Cumllnds8eGBRX6IAaXTkrd4mKooydNNI7nIjb53IE3SNVThg-OgLEtJJyPf3FO0_BiRNbMf1y7zuQZSMBxJ5ANmuxhuAao2pB_tEyIMSpu97xrr2d4E9AhrygGlQoyCYfNkzXoASjdMsvj0WEYvaHQNQXSAGyBKKgZEYPvROBbtTlXQ5NO9Gu-_G1Y-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=dvIOFYhbLqMKGhRjARnvQvhN_BSV93YjpD5sy811uIa0E9gCNrfvlqWpFxZ5RzQ3bZIF3spNNbV1O9C6A4U9zRVhVD3kck6c5VvYeBy8QOe0igiLDAfzqFGkCnHVH02wKdj6ZF6dNuft63ghM8A8WPip8Cumllnds8eGBRX6IAaXTkrd4mKooydNNI7nIjb53IE3SNVThg-OgLEtJJyPf3FO0_BiRNbMf1y7zuQZSMBxJ5ANmuxhuAao2pB_tEyIMSpu97xrr2d4E9AhrygGlQoyCYfNkzXoASjdMsvj0WEYvaHQNQXSAGyBKKgZEYPvROBbtTlXQ5NO9Gu-_G1Y-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: جام فصل قبل؟ هیچ کدام لیاقتش را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/108186" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
⭕️
🇮🇷
براساس گزارشات اولیه، مصدومیت یاسر‌آسانی جدی نیست با این حال سهراب بختیاری‌زاده هیچ ریسکی روی این بازیکن نخواهد کرد و زمان بازگشت این بازیکن حداقل مقابل گل‌گهر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/108185" target="_blank">📅 16:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=resPGo94keWsj5-ySqJICJPTLTY78QKgyOFH8ZRvU4o4oupIJ01bOaXhvkcEfLZMnzptWJ1tMvLR5oSSZk7tcAJ0bXQ3xKJXKeB8-RM5G78Kv85tv9_3cl081eA06irf2rhGEYqHAsVqXkfz_qXASf6qah7PRtZTKAFOmDMWtVx3_26nV9MwCdPgov89w0ebfBK_FBjzs5IfxtKJDYJ0UmS4lKJDnGGPcBwwLHqRiH1jxHDwWXkb0FX0JTgSPLC_TLAxtprjt608j8Y03Rty3ata9j44696waQbv-oCOqBKUkLK7onRcB7sa_Gov2gTBmjxGeSZkggeXzkdlI5mqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=resPGo94keWsj5-ySqJICJPTLTY78QKgyOFH8ZRvU4o4oupIJ01bOaXhvkcEfLZMnzptWJ1tMvLR5oSSZk7tcAJ0bXQ3xKJXKeB8-RM5G78Kv85tv9_3cl081eA06irf2rhGEYqHAsVqXkfz_qXASf6qah7PRtZTKAFOmDMWtVx3_26nV9MwCdPgov89w0ebfBK_FBjzs5IfxtKJDYJ0UmS4lKJDnGGPcBwwLHqRiH1jxHDwWXkb0FX0JTgSPLC_TLAxtprjt608j8Y03Rty3ata9j44696waQbv-oCOqBKUkLK7onRcB7sa_Gov2gTBmjxGeSZkggeXzkdlI5mqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
کنایه هوادار پرسپولیس به گلر سابق: وجه اشتراک ما با تراکتوری‌ها اینه که بعد از 3 سال می‌فهمن بیرانوند چه کاره بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108184" target="_blank">📅 16:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRb9iotUMUrEYx4GMpHf8ZUKszhwhR8LGImKpuenPnar0DFzVO1PMbra91Bhv1-HYPiEy_2Lg9F5T5Z67wUHls4OeS4_c-maWJOr9W9D8nfC3OIRYCCFo5h8UEC820ER6iUQ3UjOxy9oh5MqkQXBUW3xXa_7AwjBq-pXir_WhMK2oiXn3uFGTWcEDVGkdRy1tljNuNSDJB2eUmn88k0gSmOlBwY7oC-R4hdj8qMXVVyztTn6Q1nHcc_xqBb5NRhxBoAOmRGXYVjgo1yiozjWQz_LQzb9ATJzsCMwQGcdER58MV3zqklJizVGPMhKOgkqwb8693yRME0PsX5z1_r2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام ترکیب پرسپولیس مقابل صنعت‌نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108183" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=iM6aGF0xSNpVSRjhU-mseXx3xRuQ7T900ykNz3SdrzlJQ-rVez3nwK4N-ofyCsI08mnr5fUBHGbiuSDiYc9Jn4F91uAmqXtBhv_2UX-Ct5qXCcec1UGT2VfM6iFGwIbskJaQfSRsDTElOaJiGdhKxsAd1vPb62Wb99oL24irUk2lkvmhlljB6BpJthgF_EWZ4aPJWldUumKt6KvyhQiBGHgVj5FapF6uGATjAqhfgQxL2_yjb0iqPAw-1irNjh7sRfs4pGZd3ZZ5slqMP8UQ_2y8m90KKkQioSmitOLTnKdu55CWG_mLfcFQZbGQoXaBCFyO7gSw_nYe7xhnmQxuqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=iM6aGF0xSNpVSRjhU-mseXx3xRuQ7T900ykNz3SdrzlJQ-rVez3nwK4N-ofyCsI08mnr5fUBHGbiuSDiYc9Jn4F91uAmqXtBhv_2UX-Ct5qXCcec1UGT2VfM6iFGwIbskJaQfSRsDTElOaJiGdhKxsAd1vPb62Wb99oL24irUk2lkvmhlljB6BpJthgF_EWZ4aPJWldUumKt6KvyhQiBGHgVj5FapF6uGATjAqhfgQxL2_yjb0iqPAw-1irNjh7sRfs4pGZd3ZZ5slqMP8UQ_2y8m90KKkQioSmitOLTnKdu55CWG_mLfcFQZbGQoXaBCFyO7gSw_nYe7xhnmQxuqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
کنایه تند پهلوان پنبه هادی‌چوپان به منتقدان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108182" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=aPdMEM97qNT-bf2Uplrhi0tpQOxYNLhiRu0zNZnZXQtxSd9cAyfDASp1MSVt97pMRG4yao5VslP6eDSR_13tGokMrX3QuAsQmgmjdOsDFdoQTYnwaHFKuBGsK1HhHn6wMZKRIlHYOE8V4Z6U2YaFMaCCYZYHYyIZ5nqvM8H0J5uyrwVepfqsLEeIwqB2p4CIJjQd1BmbAot2OjcMRzTRJVaiFG68BDCBG2ch5CvAJrmuBvhOso9fAtDQg2R2HKOh16CoF2qyjr28-BWEHF80GohfNDTUYEBnRFAZyHAx4_4bBNkS0XcehzBzDFyeYkX4KHsYEejCD1ChZ2YjTcGKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=aPdMEM97qNT-bf2Uplrhi0tpQOxYNLhiRu0zNZnZXQtxSd9cAyfDASp1MSVt97pMRG4yao5VslP6eDSR_13tGokMrX3QuAsQmgmjdOsDFdoQTYnwaHFKuBGsK1HhHn6wMZKRIlHYOE8V4Z6U2YaFMaCCYZYHYyIZ5nqvM8H0J5uyrwVepfqsLEeIwqB2p4CIJjQd1BmbAot2OjcMRzTRJVaiFG68BDCBG2ch5CvAJrmuBvhOso9fAtDQg2R2HKOh16CoF2qyjr28-BWEHF80GohfNDTUYEBnRFAZyHAx4_4bBNkS0XcehzBzDFyeYkX4KHsYEejCD1ChZ2YjTcGKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
همچین ذهنیتی برای همه آرزومندم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108181" target="_blank">📅 15:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=pGp6ZYm1baSS6IMoiKGl29a_wqPH-Z8RUQQVPdwi72pGjlE6ZAONdY7F6Ng1mIhNWSnTif_2B8P-Yt8RgVuxVmwkwoiU0Zz-kHsjNORConIdF2VyTyyRGvFo5080xJYFatH7GMzhWgfwKoBhUndN7_xpNcAgnVfPeDajVqpKS7KhNPdF-8eDTzzeDUgveQpAvoUC_k9AxqdoTuQboeQy6PrDHRDyvue0n3wQEbP0HI_u3WZmqJEUst6F2r_sezBieGV-yd9882chBboZyIomFZlpWAXGFD3spdMS_I4N4Tg7OARwPsmRvXkmTGQ1yTC-K3O9Wj2As0RoTiDn9m47ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=pGp6ZYm1baSS6IMoiKGl29a_wqPH-Z8RUQQVPdwi72pGjlE6ZAONdY7F6Ng1mIhNWSnTif_2B8P-Yt8RgVuxVmwkwoiU0Zz-kHsjNORConIdF2VyTyyRGvFo5080xJYFatH7GMzhWgfwKoBhUndN7_xpNcAgnVfPeDajVqpKS7KhNPdF-8eDTzzeDUgveQpAvoUC_k9AxqdoTuQboeQy6PrDHRDyvue0n3wQEbP0HI_u3WZmqJEUst6F2r_sezBieGV-yd9882chBboZyIomFZlpWAXGFD3spdMS_I4N4Tg7OARwPsmRvXkmTGQ1yTC-K3O9Wj2As0RoTiDn9m47ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ صفر زندگی یک
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108180" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1J5OKtmUaO2aUH1a51VvAvrH1ZlYk09gudCvnzrigKy8gC-MALRz7lBQfwQBVzvClCLbXVcIcUs6sMv50tRNLWCgDZi9K5ZMjiL7USUsiJjNh230k9API_t9cUx3sQdVVy6LwppfGvmfF6wGidQLOybxlkwMqodJ-TIX-tWQEm_aWR3bqL9eaps1EwQhcNj3R0ZxOEFUmUc5PelbVVlJ4AEXT4Wc1SZpBsmYhijvKvov_qiisHTfzs51nozXKIOCNaqgzPei5ccsq6x-hHl647RtxmrUFFTPV0Mw27rV6CNo-Tfj7vSzgcC3OLsJTJe19OumegdDr4SVew0AyTWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108179" target="_blank">📅 14:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrH3UfNwx_y687-SLOQbSP7mal5J52SLAIRYTQNuyeScgNhaukDZJiWvOxIAn11Krtfc-1fXkfZUAltN_nM0qmxSUwFOwYa4DVDCG7zETMTKs873UtDK-NR-Gziq8WSDAlTs3mpzDfC9CZ7zbYQeqtWIjLLnreTppVJPUIQqEeJyTcs8Mwg8O9NSs3lL9nfR9e5qVspk0rB_WGoyQqRG5VzVtWCYb8wKf_kvuvmY9BSxeSzzpZ0JfD6djAgEvNBRskp4qQFTeHoDzDLlM5Ol86g7FZ_bDHQJL26RQBydcb4Fbc5XZ1NHnd5X2uRajdSg97_qnDLzjoJ_rJYfF6TyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
هانسی‌فلیک: مشکل رافینیا جدی نیست اما محض احتیاط بازی جلو ختافه و گالاتاسرای قرار نیست به میدان بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108178" target="_blank">📅 14:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توصیف وضعیت اقتصادی ایران به زیباترین شکل ممکن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108177" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfUnqakhXd_ysHOolqUXw7O7n_l72hV_HHr_DDReF9BnP7MZTKdGGrPnFlzIwVXmIvEMcjB6DxRArSLXhrNBrf0gWZPtd3kgFolhfOA-cssbguIrUyoAWc4IH4UVwOWfJRFbrHVX2lRvrykx86kbKswUHaDWyhshl3ebkUTXp0DUdm-_GBi6Ga9iXJvAZ1tqxWUDi4gZeHK1C3tQJARynJKMzSPwZ-O15vcyg8FQKWisPyiUzy1ASgpDFDgomGqhj5b1OrnknlNAmiWDUlf5v4C30YsKlnwdAiMfmZd8VYSIpyPfEv8HRBkAO_hUfTN-HG7AelcYeCAwxNtre3m-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
استوری علیرضا بیرانوند خطاب به هواداران تراکتور: حرف‌های دیشبم از سر دلسوزی بود؛ الان زمان مناسبی برای صحبت‌های بیشتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108176" target="_blank">📅 14:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108175">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrIqzbleJotZpacUUiOPMpuCrLxP3c7LEuvipl80bgHDtEgiVIKVLzpKAkv3z1UiEvnkm-wuOo3oVLw-WUYAdoO3irjtDD5VcicesxlfyJ4GSKciZ8pnFSzt52-uX5UbGNAkyQMXjK0KNeCuTGB-PH1ez9dW4NI5585rfWEKlxn8iZpafvxZNb2EBRBjxemo-uRm0OBuu6Xs628-a8Z2M6w2pC4jphs_gTg5IVmyKTC_JswGIJvGGOYk4gyClQUtcFSxkAtBQeS8O-2VFcGLhbB2Kks2AuyvXRLZYIb37b_bgYg0bvda_4C_7plzifNzSQiUi25WeWQdwtmsPSWvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
ترنسفر مارکت: ارزشمندترین بازیکنان لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108175" target="_blank">📅 14:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601dba4230.mp4?token=NTepdJ81bMWvfcDQX-pUFo5-Vnj7Cpr1QBBbAIzhFUvXjKvy2EMM89w2vfHfBnSg2Tz-T3lkZSHz9r-T0jUlrQDtiXzWw9kJmJp-gwqvt21dd91nM5fGyXIjCCphfSHSc7MJBEUkmKZ0JZDElRizw8RQdl6jyN8EzBLjizmJyjxl4zsZFlnnwnL4Q73xADeu20WseRV9sMRzFiRXh3SP9psVc5dkvysAdZyR9o-EnVmIT0EO2ZbmHSB_YPgNMnqjpu940pvQ869ZrfSauyvlS5pdon-E7KLoGryAZ6wWZcn97v-KnphLclmHYu4w9GiJrfsYHCY5BbceZ04TjZeovA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601dba4230.mp4?token=NTepdJ81bMWvfcDQX-pUFo5-Vnj7Cpr1QBBbAIzhFUvXjKvy2EMM89w2vfHfBnSg2Tz-T3lkZSHz9r-T0jUlrQDtiXzWw9kJmJp-gwqvt21dd91nM5fGyXIjCCphfSHSc7MJBEUkmKZ0JZDElRizw8RQdl6jyN8EzBLjizmJyjxl4zsZFlnnwnL4Q73xADeu20WseRV9sMRzFiRXh3SP9psVc5dkvysAdZyR9o-EnVmIT0EO2ZbmHSB_YPgNMnqjpu940pvQ869ZrfSauyvlS5pdon-E7KLoGryAZ6wWZcn97v-KnphLclmHYu4w9GiJrfsYHCY5BbceZ04TjZeovA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
وقتی فساد سیستماتیک می‌شود، بعضی رفتارها آن‌قدر تکرار می‌شوند که دیگر حتی عجیب و غیرعادی هم به نظر نمی‌رسند؛ گاهی آنچه باید غیرطبیعی باشد، تبدیل به بخشی از زندگی روزمره می‌شود و کارهای عادی جامعه دیگر به چشم نمی‌آیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108174" target="_blank">📅 13:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koJmMIrgt9rZw25UBXRK_rsntPFvb8bXBVjPiQGajO190ZuMeo5GTWH_LkLsIrvaWl0gpRgW0nCqo-0uoxlPsv_OphcsuUHvCXy5H_xzLR47IzcHw2tgfyCBffor7iFRkg0-VQu0QpvGHeqgjRKbHxrnnXD4WgpmZug9ieNObcfzYI3Vwr-EwQCU5l4D8GOyauSFcyc7KACaHtXfTIV_WciUx3TPGyOCNQ7MYMBmCZ04z0MYWmGfGjBY3Ci_xnpBj-xRLOGPy_ENu7qxrUmQ4BlTebkI1MvfPOU1l8fnu_KNuxySSQys0i5Clt1TXv-jMY_tzvoADyW9dofHOOpY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
📊
آمار بازی روز گذشته استقلال
🆚
تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108173" target="_blank">📅 13:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
⚠️
انگار ۱۰۰ سال پیشه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108172" target="_blank">📅 13:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY8UrWeXjP2ehl0fuu1tsghkz8afe747D-rs1MuypF_aauVZeBcvET6eelSBrP01zOL8jgoWyPna1q13a6BquRVRIddWQSMsS4VXHxsIQJNudpT9jXTQ5YDh4lrYVD3fNuv4JpEFoiY9sl67TEfwdPg_NPy5Nf51eB_m9OOcp8rUvyUlsM-UL-YIt9CnxnFXwzaC-pbRnRLbg-cXIyYZxARKnTYJEMimtd9HgXEgBgO19aSKQrRJ8rEX3yfJGXlBlthLIFvhwEVoRmlMd5OBOIjF3jtDV5WPOc19uVcAwtI2b1_Bh59HQbGEDp6H87d7I962-sEa3s6DsR6Lv7zCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
عملکرد ژاوی در اولین‌فیفادی خود با هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108171" target="_blank">📅 12:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
با اعلام باشگاه تراکتور و با تصمیم جواد نکونام، علیرضا بیرانوند تا اطلاع ثانوی از این تیم کنار گذاشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108170" target="_blank">📅 12:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXuTjfmDADGiy1DwWc5IdFdwbyEOpChPScGVXK986GTb5HU_D_RStijSMiD9wqr4JffirCzDbZHImorDnjsp1_DxOdr1_WO7JI4_UVReF3vs5ikEN_QwURU3YwQbiLYP1J8_CxJnMx7eBC-4rQru2AnDO3LbyH1GXLkc6HHItm926bZ1Y98n9Q2bIAHR9wDJskDbXcTfwDtSUtUVOONaSDAWdgEDTQJNrf9s55WCCmpYljokBWKqKWInyMhjx9Fxzhj7wE_J_HJU6yuRoHLq27IjmLU5F4vjAv92UCprEMjDEmsrgw1GmbmovUISINg_ukZcJPHsXrEJphd0w9UDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری جدید یاسر‌آسانی از مراحل درمانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108169" target="_blank">📅 12:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgp7AepUVk-Ee1vWcCx-DWJnmja3iwVI6Xz6VIIRVsDJuEiF4fjxKfeBRHzBln5d6RNOL72pnxjDCPB8nE0nRrl0DrRYl4h7nzh796L3pvfFugAKdQcIXVR-ngUCKdI6caroFr6S0UR3gbOrxMsXJaWFZ1l9ATa041Rsf79J0HxGSwAfVEoJl3AmOx3CdTkLJqY5804lOPiFXz7l_vP0Gte9x4sVXP08iHSXlJF7VPNI7D9BqS8shJC72TtmS-barbMqZP5GxhS2gPa9liTx8qz57iLuOH9OS2qeBAUwIGDkEeS1s6NpzJcZeBA-IIQnmmWJeA5ENL7kr3c1R93ORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAT5SZ69eIuyzqNvzbhLGy-b08jfdt5QsAXuMfaD-TiL8Vcr7EOctb6iF9nvjpKQaV81YCQI_sum4b32BJNA3RZr6qHnwQ5Ru9uBtE44SnyFO6ePHImh6Kk7xNWM6scoVwfVtL0-iA5iC_0qekpJzM-byICxe2aAElspnJl_5l1JcBH-XxsMPf40WIp1d15tvRZSj8tg5lCEhMEB3exNTe34VOEBAhf_YGg0yFlDgAs5kl0V0wlDklJnSZw5XA1W6KssheRF5LH-jzOPjnVo4deHM6cFtYi89RIIP7ngmZAeC3AcmpqgocKmwd41Vg3PHByXfzJkQL2yib7jXubaZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108167" target="_blank">📅 12:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65716e5170.mp4?token=fh9qz7VsfL0fcLimZLohoGGJCTyZpyAzDwE-aRe1SQx05QdaoTr0osdLRnH0rQ5u9eXWRqyrgcgtFqhsA-o6KAy-N1syuP-q7CiOFV0Esi5Ej30wIOOn36hAgYb2ATSEfLwtGgMPpBn8UjqRmvnzrVEbgwyvXaLqpSHR2Uq7bcI4DLaj-Ko6Zah2RkYNz7bOtls8ryWcQV_KHqpRalt07q9G54C8uVKtMwSJ5Xp7s49OPNWZd5yMKu-nETisqZfsRy4CbEKp1T1ikVn4M5_Z3mr5zj-IiibKnptIUpjU9avXTJP-lv8p_IfdGUebOdpG3bD8TkJZwwlCmsUPvxHlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65716e5170.mp4?token=fh9qz7VsfL0fcLimZLohoGGJCTyZpyAzDwE-aRe1SQx05QdaoTr0osdLRnH0rQ5u9eXWRqyrgcgtFqhsA-o6KAy-N1syuP-q7CiOFV0Esi5Ej30wIOOn36hAgYb2ATSEfLwtGgMPpBn8UjqRmvnzrVEbgwyvXaLqpSHR2Uq7bcI4DLaj-Ko6Zah2RkYNz7bOtls8ryWcQV_KHqpRalt07q9G54C8uVKtMwSJ5Xp7s49OPNWZd5yMKu-nETisqZfsRy4CbEKp1T1ikVn4M5_Z3mr5zj-IiibKnptIUpjU9avXTJP-lv8p_IfdGUebOdpG3bD8TkJZwwlCmsUPvxHlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های نیروی امنیتی آرژانتینی برای لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108166" target="_blank">📅 11:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=mFw0XBVc3nJPWeuWDXmtqB3xmrjPpvSz8Xbb22cUlblrITLR_FK70zDcthgVKXURo7WMuOlF6coezK83lI2Ij3wc6MFVeMsL_u7b9z2kfVb4PkkM4onb5KW2CUTaF695wI2ybQuLRDNsWimJuIY4d0hgVVizvTrodsbphjeA9FN-kBOOaOV81ucHvt0q_c5YQpzdPFxKKJRxRBnAZulAT5Z38RhE_vx5unjtr8976QJ0QlH4tQ4vcgR9wXzOUlmkynBr7GqbeVOXx0zMu_P9d-zAAnZNCrWozWw7OrHVVo0pU45Fi7FKmalpxRmECDfwjhHoVbqGd5epH2NMGBbyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=mFw0XBVc3nJPWeuWDXmtqB3xmrjPpvSz8Xbb22cUlblrITLR_FK70zDcthgVKXURo7WMuOlF6coezK83lI2Ij3wc6MFVeMsL_u7b9z2kfVb4PkkM4onb5KW2CUTaF695wI2ybQuLRDNsWimJuIY4d0hgVVizvTrodsbphjeA9FN-kBOOaOV81ucHvt0q_c5YQpzdPFxKKJRxRBnAZulAT5Z38RhE_vx5unjtr8976QJ0QlH4tQ4vcgR9wXzOUlmkynBr7GqbeVOXx0zMu_P9d-zAAnZNCrWozWw7OrHVVo0pU45Fi7FKmalpxRmECDfwjhHoVbqGd5epH2NMGBbyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحنه‌گل دیروز ذوب‌آهن به نساجی که به شکل بسیار عجیب و نامشخصی توسط وار مردود و باعث اعتراض شدید شاگردان حدادی‌فر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108165" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41de558131.mp4?token=UwF0UvDALdL7Da7DTz5ZDOb2rj43pUbt86wBqh3Gin7wAnKQHPlA9yzhAUPqOBu3OFDqCiueHdQemNS7tD-lBidD5h8hE5d2Os4zhxTV40B3SLl9GszekqXSyjpEPo_Zn2q0CKuyNQioJ17IeedNKN7UKbSGg09buWKeQ0zqufJc2faatwhwD3m-eJHNPErk0MyFkFDEKSmDXHL50OAcEktUdqvhQ_kxb3Fj1Jj8fLBJ1bD_naik4k2LbakfvCWNw7fg0r9mISqCCvs5I2HuU37XF-V3W0LCktfvpu9rRlxC3k1_41b1Tw0jag9cfAL_HtDqL_sAo8XEiHLz2oM1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41de558131.mp4?token=UwF0UvDALdL7Da7DTz5ZDOb2rj43pUbt86wBqh3Gin7wAnKQHPlA9yzhAUPqOBu3OFDqCiueHdQemNS7tD-lBidD5h8hE5d2Os4zhxTV40B3SLl9GszekqXSyjpEPo_Zn2q0CKuyNQioJ17IeedNKN7UKbSGg09buWKeQ0zqufJc2faatwhwD3m-eJHNPErk0MyFkFDEKSmDXHL50OAcEktUdqvhQ_kxb3Fj1Jj8fLBJ1bD_naik4k2LbakfvCWNw7fg0r9mISqCCvs5I2HuU37XF-V3W0LCktfvpu9rRlxC3k1_41b1Tw0jag9cfAL_HtDqL_sAo8XEiHLz2oM1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
هاشم بیک‌زاده: در تایلند اتاقمان کنار استخر مختلط بود. دستیار قلعه‌نویی نیمه‌شب رفته بود لب استخر و دخترا را دید میزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108164" target="_blank">📅 11:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejkG0_eruPtbpjRIbpPhsW7mc8Z-WDudMwDY4WVpoNZKGKgnsA8dSs_U1xSiCITby6mCSoLowJcXRtKoUySQPnIxk8_v4A-FQ-PY1d8xMIm2CIuy13TD5p4tHpyjwZfXTnB1ZUzand963jhQWfouJRXXgm0nVfVlY5miz3ICq9TM4Skw5IO6ynpRdH82v9Ft-uJTI8y3pLESbBrn0slOqh21bVXRLe75xuL4pRAMeQdNHXxwGp3gK3kMpkmTAYCqgy37GGmH5oGLjxjPddzDON7OTckdVTdWEmgogzPWonKaisD_sPFxL8TmZxek82DTewRf4QLIW_4bTmNXxQZogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
علیرضا بیرانوند اعلام کرد که از کریمی مدیرعامل تراکتور بدلیل اتهام تبانی شکایت می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108163" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b39729529.mp4?token=FoB4syqV9xcIR5MrS53IRSeYkwpQz68_0DBzjlEpSrhZqh04nA1bKU-FGSHn3H8xJcoKy4RS04DyaeQ3i2gwbJzWMgG04dcyP4IBJYDdkpkU3S8Tz1u9dpZfzMQyy2TjlrruYeN7_Y4tG6jTGqU7GLKtPii-OXzD4U2CZLzo9FRuzxGcR5stEWX-MoClwASCwRuKrEov1XDmg_V_vLTesDCAT_mLtYfH3DF0wXnb6JcLuMzKw2VQzBuCOE38hs25n8eKWnYyEuYDtLiLK-oZ2OC7_GZGfmImpI_Mg8sI9_DXDrQ-qryJGJYMJHL8d4357IwRMSJJkoKWSpq4sjFxZ4nErPWvvhHs7zfi8A0mhZNvhJnv1HHJlUtf1E8F0T2mI9-I11D0dDT43D9TYkyZUJ-GAGgGzPExGON2rUjnVXnRrtDmRMxmWeSLdAaVrBPKSiqgrsrhIGYvy4ogqs-xAYo6--mMprnZwCmkYvHNEe_uzhCyjLIr9Uwj_jvaN1Qd7aXof5Nq9GnwBl8ZJEIoh3Ey-Oxsrc187-Kuz6biZ2PlurpfCcZYdqamns96x17wHxz2sqzn3jE5keHho7o3DmdU5DG6_KCSPCO2weSVsHIIxXeq0-79REpxNTLEm_Hh9qFVdZJLUVf-av1d35sM1P9gQvmOtYQlu1FgcW0npYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b39729529.mp4?token=FoB4syqV9xcIR5MrS53IRSeYkwpQz68_0DBzjlEpSrhZqh04nA1bKU-FGSHn3H8xJcoKy4RS04DyaeQ3i2gwbJzWMgG04dcyP4IBJYDdkpkU3S8Tz1u9dpZfzMQyy2TjlrruYeN7_Y4tG6jTGqU7GLKtPii-OXzD4U2CZLzo9FRuzxGcR5stEWX-MoClwASCwRuKrEov1XDmg_V_vLTesDCAT_mLtYfH3DF0wXnb6JcLuMzKw2VQzBuCOE38hs25n8eKWnYyEuYDtLiLK-oZ2OC7_GZGfmImpI_Mg8sI9_DXDrQ-qryJGJYMJHL8d4357IwRMSJJkoKWSpq4sjFxZ4nErPWvvhHs7zfi8A0mhZNvhJnv1HHJlUtf1E8F0T2mI9-I11D0dDT43D9TYkyZUJ-GAGgGzPExGON2rUjnVXnRrtDmRMxmWeSLdAaVrBPKSiqgrsrhIGYvy4ogqs-xAYo6--mMprnZwCmkYvHNEe_uzhCyjLIr9Uwj_jvaN1Qd7aXof5Nq9GnwBl8ZJEIoh3Ey-Oxsrc187-Kuz6biZ2PlurpfCcZYdqamns96x17wHxz2sqzn3jE5keHho7o3DmdU5DG6_KCSPCO2weSVsHIIxXeq0-79REpxNTLEm_Hh9qFVdZJLUVf-av1d35sM1P9gQvmOtYQlu1FgcW0npYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
صحبت‌های تامل‌برانگیز مجتبی پوربخش درباره میزبان دوره بعدی مسابقات آسیایی سال ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108162" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108161" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Pd333Wat5cebok6-ymxc30nICVjYTqfBaf9qvlH5gQfLwX_9E6DRNUyakjlInN1ietVHGeTDF3fq3V_915NcorzpwflnE7MxSu8R9_tBBmMpa5E9CzBckcm7L0fdu0WzEpUQhcn3XYE6QChEGn1RV6F9CmB5chJrSXsIf-wTjGDhPiq7RKMx0YharSOVSVMWKtYuEyI0-A83aZ2aR8g67sii5VNAgKuL-iLiRbmHySOSFbtb8_R0J6rAZUD32SdRDFuppGQZnMB5AE-ezgANlqY6C9UW2wRtp5jZZYjhuWNDUImTnse4JIveXceOWPObz-e-OB1viSf4MI1GvBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108160" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
🇮🇷
فاطمه‌احمدی ملی‌پوش تکواندو که در ناگویا مدال گرفت: شدیدا طرفدار استقلال هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108159" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hIBN49Pqc17s-DG2aC8B-qJCw8ccxifupRT03zxmSw1Y8PNEZDEkc5L9dQXYTOyUAiqv10lS33Zhii6bZ5l4HzeMYdRCOFzY7fwsN2LIWfKeuQC3FRLkK7TDpUWBD0Rt_Gff9WrTkJIhKAKRdBWIJQq1nOuHPjscgM8_yef3J_Co6sjfI7BOMkKvFcUWXBulb0gvWFllBIZoDK-5FIZTvlLQo0KryMS6wYzIgzlpFTotz-QsEDgewl9gJ5n-zTh48HlQHQI7ybq_MYIL5Xm2QC9pS8_8BXB4sPk7l-yGC5oscpk6yRizwnZXn86ZCl8hnpUFiazidqF-aIW978DULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hIBN49Pqc17s-DG2aC8B-qJCw8ccxifupRT03zxmSw1Y8PNEZDEkc5L9dQXYTOyUAiqv10lS33Zhii6bZ5l4HzeMYdRCOFzY7fwsN2LIWfKeuQC3FRLkK7TDpUWBD0Rt_Gff9WrTkJIhKAKRdBWIJQq1nOuHPjscgM8_yef3J_Co6sjfI7BOMkKvFcUWXBulb0gvWFllBIZoDK-5FIZTvlLQo0KryMS6wYzIgzlpFTotz-QsEDgewl9gJ5n-zTh48HlQHQI7ybq_MYIL5Xm2QC9pS8_8BXB4sPk7l-yGC5oscpk6yRizwnZXn86ZCl8hnpUFiazidqF-aIW978DULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
فلسفه جالب نام فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108158" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=VFExk0toVnfBXY5KbCcFJebt7H8665DCmdZIoGoyLlE142EwULd-zUMSx7_u6hGWOf3dUIpDeHYbA550vASjSeDxNOS7cIWqXrrLDFPQy9JDNGLIaPbAIRFCd8gRbwyXA2ARcJhakbaZoN9QSnDhvM9LgsBOuBndi_kiNZEpUCuKSnB_l93XVK_VXu4spKaYVR8PTp--A4AYw5DmNp6Zi9_d05-sgmYBKPm3It56cxuVcaq-pQaxxbWIuxOkPOHxd0wXDzuMuASxjaDFmzA9_2yKjwL3m4ho-ixDpYL3GrD-b68LYtTWbu0l9Glp26XiaGI0nZ7XN7XnvI2BwAXuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=VFExk0toVnfBXY5KbCcFJebt7H8665DCmdZIoGoyLlE142EwULd-zUMSx7_u6hGWOf3dUIpDeHYbA550vASjSeDxNOS7cIWqXrrLDFPQy9JDNGLIaPbAIRFCd8gRbwyXA2ARcJhakbaZoN9QSnDhvM9LgsBOuBndi_kiNZEpUCuKSnB_l93XVK_VXu4spKaYVR8PTp--A4AYw5DmNp6Zi9_d05-sgmYBKPm3It56cxuVcaq-pQaxxbWIuxOkPOHxd0wXDzuMuASxjaDFmzA9_2yKjwL3m4ho-ixDpYL3GrD-b68LYtTWbu0l9Glp26XiaGI0nZ7XN7XnvI2BwAXuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه ابوطالب به نحوه برخورد بازیکنان آرژانتین و پرتغال با لیونل‌مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108157" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=HfdXzYmddOi6vgwyq-hfMMi4DVe32rJutl9Ov3zP6BnmCA8ef4p_qSUOxyfQmVqhTKmddINaIZrnykdOMIKMkpDiAYFwk7r_uMxG04ZtLOnEO0Bhe1DG-OVsKUbBRMt7qT3lLEB3tR4rTChnGaOuqpC2oAUh1y1U1-rQ-8P6L4M_w2YhlkB82OlR4eM06x2AjDJcKSSwhmDQLyoife2t3XQyoNPXvcwM-oGOT_7d_TvtKNM8OpR3v_1plOejjYs-2MBJg3yx8zas_q325QH_VJnqcVTli-SjGI-_Ivmh6duo6jJCEk6_hcqXgcUsun9r6fnBGw6B8SyCRE1aoEoJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=HfdXzYmddOi6vgwyq-hfMMi4DVe32rJutl9Ov3zP6BnmCA8ef4p_qSUOxyfQmVqhTKmddINaIZrnykdOMIKMkpDiAYFwk7r_uMxG04ZtLOnEO0Bhe1DG-OVsKUbBRMt7qT3lLEB3tR4rTChnGaOuqpC2oAUh1y1U1-rQ-8P6L4M_w2YhlkB82OlR4eM06x2AjDJcKSSwhmDQLyoife2t3XQyoNPXvcwM-oGOT_7d_TvtKNM8OpR3v_1plOejjYs-2MBJg3yx8zas_q325QH_VJnqcVTli-SjGI-_Ivmh6duo6jJCEk6_hcqXgcUsun9r6fnBGw6B8SyCRE1aoEoJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معلوم نیست داستان چیه هرچقدر هم ببازه بازم از فدراسیون پاداش میگیره
😂
😂
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108156" target="_blank">📅 09:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
🙂
سرمربی فولاد مطهری: داریوش؟ گرشا گوش می کنم، وسعت صدای ابی را دوست دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108155" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=oMEgT_A2P-zCh7iFFG8f6mDJaUSoi8Arh5cdZhKFPk4D3beQNemqtZYNlW-Qyega7WnGWTVHpRraJnpSfoZZhZ5_az_r27BrSxd6RyiBw8CCcm70b48KPxbXj2uvXsg7vWICFSHwwGl8a7xru_q7_6nrm2AMscs73OcDE4ff1zNIoHpklxwxHlkiq7TZXHJlj242IztuB6JDdB7FnOqWdjcISK9aNFZRPw_6qdbvexUJzzIyT9ojpEEI5YVjkqUU2alabdvAh_X4bujOor7P7tRxIKhHdTYvU6udxZNiJjdKH3TBI5ysR4vN6tlNciGeNYogaJCF99JRpQPcFK8y-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=oMEgT_A2P-zCh7iFFG8f6mDJaUSoi8Arh5cdZhKFPk4D3beQNemqtZYNlW-Qyega7WnGWTVHpRraJnpSfoZZhZ5_az_r27BrSxd6RyiBw8CCcm70b48KPxbXj2uvXsg7vWICFSHwwGl8a7xru_q7_6nrm2AMscs73OcDE4ff1zNIoHpklxwxHlkiq7TZXHJlj242IztuB6JDdB7FnOqWdjcISK9aNFZRPw_6qdbvexUJzzIyT9ojpEEI5YVjkqUU2alabdvAh_X4bujOor7P7tRxIKhHdTYvU6udxZNiJjdKH3TBI5ysR4vN6tlNciGeNYogaJCF99JRpQPcFK8y-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
عاقبت تیم‌گرفتن با رانت و فشار بالادستی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108154" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108153" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXn0gG-Q6XNyo4EHgflH35smJWQgvz_gNng1G_6SvkhWyCZIweOO2rTqM1U46xMcy91P1u7gkupAvJLJjFB5M4Kwap-pOJDksXx_BfyXgVIsA1C_n9iC37-1B51XxhPG5SZYki3vMVim4JClQxQfjIvElbaqIcmGKE5PHGRBfa7r1zqavIbgyj8EnJ9xCJrVIT8arCdPVFzuhaWhSXtHGeD9xbyn0xIH8y-dq1wF4NWl9bl3wRO69hKsgf3NLN85usuKNbd3jGNdfFx_R5izCpzqG4Aag8uwYfMM3KMGOXaJJG7W_HTnT0ZkgXTSBtRMmsh1IpShv3j_tMMCvuI-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108152" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIB65Pjr3FIzcPhHc6UKUjFtHTL0DeAUobAbcp8Ex_FuDrwk1OwRSrVGawvvo_gU7AFyfCECT6NzCGRcy6xs8TAvSYPBS5dixtOnLMzoch3gtFhVWnScAlV1hMLM3Fonyxzpq-JcbooKlaeFlMkjBcnKId5Msz74ltzTyp1p7HQUZuZktMgc5au7lpQKfyecrAWvOZJ4e5Q47OX-81NG5ZM0tm1YtYca1KOO1XDoiPt-2lVyYDPnMprZsB66PHpJIqPSBo62tWwqm-CDyRowcsKiRtB5ANQvcDOSUSuMjWfIMpc1WVfuIyfTGdRuAxorVUtH5Zps4m-kBlIl_vdGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇶🇦
نتایج ۷ بازی اخیر الغرافه حریف استقلال؛ 5 باخت - 1 مساوی - 1 برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108151" target="_blank">📅 00:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=NNUBS1t9c480gT5g5IoD1MnNI9W5eAhl48EBhkJe1IvzU-oujMuDDiP72TPJA44yJag3cb9iqmJTbpOYbVMO7cBbCCw_6yS_jBDIrLcsc7Q6e5yGL_ejnm_MA2Q-u1ZdByUvCqK0ZfcUSTMGCQh9Q3BajX4mK06NBizNphi0KvOsvTiKzOdCN4lQvU3UGJzokpl-M6vM1dqcwcSk8UXHpbB-Kx2IZFe4jJnTAKdGMJ1gIliKS7NIvMq_fW9IqdooMXw93NQI80VOn07V9LUOC7ojTBQYiJbw65M_jNliv2SYLV0KKPyn57lW4h18z1zG6mY4Vgm801FeKhgwmCI3FGkOHzzNCodXhL6ehGZFmOuG-Fn9DKNXIKTMoEFbmZJwhmfTpAHcsPskxss5DypYA0_aW3JVXeOeobZvQTiRrZ0wvku_CE1Rb4rqTfmg_cNBgs_h6LmllMrYNbI3dKcC_thWLdKkX0mZfQQYSh-IlYes2a7K6S6GbtS12K6FM8Ph10ozhCJGCVNlod8tbWyape4YQqbPAU6tHjAsu5TmqKSOEiYE7C-kZz1BNgBkiLJt60SAWtUT17uI_N5-CsbyKLTuwNuOSNTaQR2g-hgA7df0uulRytFGaETscuOApYyxhgoTAiEO3tcits1HRiWfi6IqKS3Ej1mYARNabWKHhRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=NNUBS1t9c480gT5g5IoD1MnNI9W5eAhl48EBhkJe1IvzU-oujMuDDiP72TPJA44yJag3cb9iqmJTbpOYbVMO7cBbCCw_6yS_jBDIrLcsc7Q6e5yGL_ejnm_MA2Q-u1ZdByUvCqK0ZfcUSTMGCQh9Q3BajX4mK06NBizNphi0KvOsvTiKzOdCN4lQvU3UGJzokpl-M6vM1dqcwcSk8UXHpbB-Kx2IZFe4jJnTAKdGMJ1gIliKS7NIvMq_fW9IqdooMXw93NQI80VOn07V9LUOC7ojTBQYiJbw65M_jNliv2SYLV0KKPyn57lW4h18z1zG6mY4Vgm801FeKhgwmCI3FGkOHzzNCodXhL6ehGZFmOuG-Fn9DKNXIKTMoEFbmZJwhmfTpAHcsPskxss5DypYA0_aW3JVXeOeobZvQTiRrZ0wvku_CE1Rb4rqTfmg_cNBgs_h6LmllMrYNbI3dKcC_thWLdKkX0mZfQQYSh-IlYes2a7K6S6GbtS12K6FM8Ph10ozhCJGCVNlod8tbWyape4YQqbPAU6tHjAsu5TmqKSOEiYE7C-kZz1BNgBkiLJt60SAWtUT17uI_N5-CsbyKLTuwNuOSNTaQR2g-hgA7df0uulRytFGaETscuOApYyxhgoTAiEO3tcits1HRiWfi6IqKS3Ej1mYARNabWKHhRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
مارک‌کلاتنبرگ کارشناس داوری: هیچ پنالتی روی یاسر‌آسانی اتفاق نیفتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108150" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/108149" target="_blank">📅 23:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4IBCW3t78uMlnxHky7FzEnUy4u0DPAY-eog4C7ab0Emn2GfEiiZsncpnHnrA5UlRLERGmO3NyDAu-oaqCuSA2gum-4ZmD3CDqqN1AqscTUFuo1M973wPU-h0EDsOtBO3__5cmvAIa29FcIohkOgwwNdsEmzr8mMFOG1qILFbx50FC0_JryTSfVIPAw130LXVTTStenT0j_k5hM0cZBqzLkUgGby7FNzQy9UHYU1Mp5fBgb5YusxDLjyn0F1FF8Gf59_yqUhqfupOH-AmMW8N6cTKpw54UK6y8W_1UpShxfw0SPBKq_emXcwt3VCfZd7Ra4NwQrwGVl6-kTU055GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ مایکل اولیسه تنها در صورتی از بایرن جدا میشه که به رئال بره. اگر مادرید پیشنهاد جدی ارائه نده، او احتمالاً با بایرن قراردادش رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/108148" target="_blank">📅 23:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRHcuCNwhGCo6JSjycHgzK2tDWXAgToAq3Kl6kDqPqLk8e2vjkaaR48Ko7U3nDW8FWuhTsqwfHlyQXgE02A5SrhVfW5b4DP2C58-FcPhzEzRysTVDud5GgObYQ5mfG2jz9_3-AAuL5OPQILQHJEgnD3Mbqf4psJnucoG0DTQw-AUzRpSBZf0PBj6UpuVmT-Q78_L_WEHfNQjFurFeRiYe79xnfU2zQ8g_YviQ6i_-S-i82lbbVUYjc1OvGtSItlD4rccOiMJBsYJE_KhgUa3JVtFCU7f6PNWRT4ttMbon9jjm540os2VdUZeNgLs2lBdsU8n06cOfyCZ2PtOozzNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/108147" target="_blank">📅 23:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH_0xSHLpmgw611c78uHadnGYZHpQsq-gjKD1RLiGYB3SRlXl-aEv3bA3JJgWauXZt2DZQy0nLFLew4Q7m5wn-CWoPGDv-nPOsfXQ1FcSHQnpeNu-iqv6oq0n0SznqD6tpyER7ArWzJJku9rPnb2vZxs0B6v-hLC2ezzs0y697LAosZ9RhAjnZUicisf_g4EveClWCIbf0RHT7rg9JgMl-1-aVCHZK9JapNLAl3QhyqUaTQNSrmgF148Lc5js4xpyFvYmzqhw29HCSstzVqMAeipbBl8A8hv8pGorIOG-Mjl3gd9l8bFYvgWm3aGX4bk8mtSzx04TaqRzUv6u-IlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/108146" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=GiXaDrCvwuXpCutCUdPVxbLjHLsvKxFfRv_NBR7_zOG0TAQYpII71KMc07RXNt7ozYMR4d1LU5Ai_2nffclmToNQYfMjFoFMi4Din8X5T4djkrE1xkrkh8qCcJMAJAD6QaJsiSksVluOFrbTywzG-9iI3RCn7LF1Jrv0HeNHGL2Mb1TQH_N_YJJ3wrkyuePdJCtQ1YnJn_F3qOtdrVoqWWrph1vqjgJlXkEv8hjEsJ-NegQDVLIngUpe-8LqBUKW0AFV_xu18F9n0C2h7y9mbvTEfPcuXt_Lthha_8Qo9qPgOq6cndq8pFyCvb74u474H-ugxWLh6U2j8Z1th6Dkeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=GiXaDrCvwuXpCutCUdPVxbLjHLsvKxFfRv_NBR7_zOG0TAQYpII71KMc07RXNt7ozYMR4d1LU5Ai_2nffclmToNQYfMjFoFMi4Din8X5T4djkrE1xkrkh8qCcJMAJAD6QaJsiSksVluOFrbTywzG-9iI3RCn7LF1Jrv0HeNHGL2Mb1TQH_N_YJJ3wrkyuePdJCtQ1YnJn_F3qOtdrVoqWWrph1vqjgJlXkEv8hjEsJ-NegQDVLIngUpe-8LqBUKW0AFV_xu18F9n0C2h7y9mbvTEfPcuXt_Lthha_8Qo9qPgOq6cndq8pFyCvb74u474H-ugxWLh6U2j8Z1th6Dkeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
در اتفاقی جالب و زیبا جایگاه هواداران استقلال در ورزشگاه یادگار امام به صورت مختلط درآمد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/108145" target="_blank">📅 23:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlnljSMv8YRKDRopU727N5tTXBrQ_r_lfratpWoKHayocuuY-WQKPX1Jt-sPvny5Msu2-V2-li0_YxLuP3Kb8Bjw3hIagqFNPVjzkqC3Bc0GTBpJZRUXDUdcYfS937wke99MI6BBC6uM0CUN7n4zu_LBol5dVq-NIM6FuWtW8fnQi7M0tTN5WyPPc4QlobYHNb6fo-2F7jaACyoS9zMS9rtURiq81pGhnWwjDwot8BF767XDItOnBhbH033VUK3qI6kLSXwuAz9s7BvCz-_yb5rljpYYYywcpJhQ9UWFMTa4_T7LzEUGp-nBwzCSYOA7cPdR9qwKpsSAII5zmq2cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو در پاسخ به سوال درباره رابطه‌اش با داوران: فکر نمی‌کنم مشکل از من باشد. فکر می‌کنم مشکل، بدشانسی و حضور در باشگاه‌های خاص در مقاطع زمانی خاص بوده است. من در اوج دوران نگریرا به رئال مادرید آمدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108144" target="_blank">📅 23:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Habc-N40Hegy76HkIuJ6v0a6JPv_ul7kVVL4rXkfV_nYXL4OzERDMs8q6Kv94drwCoTdLJiMcJ7jLLonS7qMkdqPlno6ypQ36wqgUNM3KbOhU5ymeL1fSTDzyI5WHYZRICWsXl-7idRu3oAErBKhxJGz7k3_9RvHqm4fg3m0Q4dMRwWEUfz67PBepYpu7BYU8z4OKxb2TeWW8pYt5sX16qFcP1VJmUcuLd3m55geLIE9o2VWAPLHTKevSlLy3tGGlDzTCqp8XdWkzQ9hoxN_9ybuQ7ugck0vYaDLBETq1PNCw6-GRR6MqW0O9ZRd0TPMmdktFbVTdXVihlBjCUXoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108143" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb13pkyAT7NCTj9Ag0mI-AcAWnnlF-LAortV2FT6nU_XgPbhRIqw27Jzs9dYn1Kf_Ur6lOutusZ8-eogHtlbo5y9T-yn1-tOR6eGA5jT7Sw18nLjw3VpsEAEE85DAYU9T48SzcfP1N5pW1yJXdxRu_CqlOE4KaUz9tYf5FbHYY7EMq2f_PyPonKKNDPP0dudPMC5KgHBGagMCG9e2dxHlFeBQ4zYbPnKcX5nzgEQgeNIAfdDHQT82l-cjzqx8O8PsI-DBAV8MFjDY_AqDW1OC5qNcVzQCGrD0NIdej22hknXBmwJ2XDYq7V6fbMaJMX1YnsoFlRFfMnTJcZoVyuK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد ژاوی اسپارت ستاره جوان بارسلونا با این تیم تا سال ۲۰۳۰ تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/108142" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSK861GVWsOMwvs7KtYVuZknBw1w4o_vrBB_VdGa0Zo2d23d_D1awBI2R8_Kd4S8iolGmudxnmO6tDpRpvh7lySDWjLEI5dCYPbHhoVX4hVltjIiLwp1qsziArI5N3EOXjanZg6p293Ar36bqNLuUndwjPvtihdB0JbZx2YPdFIChHc7RofTLNw-s3QiwS8VIs79ifNHQvmbqXBymRYce-mNj6lE0c8vYRLMa4KT33vg9zgd2SP_Pu_6VXv9FC10pH-OCqDj_88Jg-WlyWgpNlrF2JSkbU4-m3571DEI43JXvzMUrfJ41Eaayd7ua-eNG_4wm6hUEx2K3bOJ4K_ZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/108141" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXMI4U8Iz2auIeKHtE--CvVNTy3uKyiPXj9wfTbIXwETGGbkWXhCyJ7UdIMpvhvzwWKz3zgH3a3Am-t59_6VZfc-w-ld_X1xF3AMH4pAsg43ka68WpIgLBC-BaxMf0I1TmVDnoY4S9lRKt1GvPj7alCzdQ0qIZuCGvQKsO448IizaVEYq-NipXVbZYVj2eRHjzawaPneMyju0t_uB9hNm4nofsd-MQQyrXM0M8SvjAw1NchA-zMegNByplyskvsf24hjV84E70GYoQeVm332ydTX-u6crrXOSURzJoWEY5o1Xkf0VKi1epPza7XNodLEtc_2ur3k1q2unQOp5wdVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108140" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14105f8264.mp4?token=U1hnR2GhBdtE6YOscL1sBBeTqnGXYj7ZSRSQSm802ybd28fGT6zqyRs8NQTzCGqlppU3-MW56dBWr4LVLPPMtdBbBy1V8OBR1J2phIXSERh2zF_7lVqPONbmkrj-OQdi60VKkNTngtDmoc8XqWRKLpWVCwCuR-k3rd3Ry0wgH8lURfZCBFUJ_Gti7fLTbsiSBz8g1YxAU8GNM4qoUt8zYF4P1jBKJ15ftyR7NBohnX0GPh3ZLoP76GiugxS-jiwUYJV5Bczw7xd0lIyRM2b_zg4SR4Zz1m1nnyamgmYdbUwd-IX5otm0VCpU6CDZ8r9FTw3V8Z1Zp-AA1xMXvshtUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14105f8264.mp4?token=U1hnR2GhBdtE6YOscL1sBBeTqnGXYj7ZSRSQSm802ybd28fGT6zqyRs8NQTzCGqlppU3-MW56dBWr4LVLPPMtdBbBy1V8OBR1J2phIXSERh2zF_7lVqPONbmkrj-OQdi60VKkNTngtDmoc8XqWRKLpWVCwCuR-k3rd3Ry0wgH8lURfZCBFUJ_Gti7fLTbsiSBz8g1YxAU8GNM4qoUt8zYF4P1jBKJ15ftyR7NBohnX0GPh3ZLoP76GiugxS-jiwUYJV5Bczw7xd0lIyRM2b_zg4SR4Zz1m1nnyamgmYdbUwd-IX5otm0VCpU6CDZ8r9FTw3V8Z1Zp-AA1xMXvshtUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/108139" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9cQppDw-DBJz6tacSLYZvRTJFTaXMypom8W1OzsCDtGRoKcGq_iqrHsiNBpuhszR-qKqs28mOEkz1V66TCoTp3_OBnhytnn1iTHHoxptE8A5sf6tLi2JDDkp7hZjYoDdPPNChJ-X87tVv5EjF_t2IXsfCYWgLtJ8Hxq58a8Va-8CvSSbfeP2hLjw8sExNJQSMOPX-xjVW5oha9pXfbSaSxhyX9rlCxSAhVs8RyHAZaBnOUrj2jYdAEIpriGkkZLTMOeeaZC017NpYndIRu8aTiKtyM69sBNAEYzI3RhUa3morITBn1w90WBNF0K5EbdSd4KNLL4cKnTkqtC7KBIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
پایان‌بازی؛ گلباران شیرازی‌ها در اصفهان؛ نویدکیا پرگل به استقبال بازی بعدی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108138" target="_blank">📅 21:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846f23996a.mp4?token=koEU_gjMlToIJNq5VzXnAeQqAr4CZtc7KCSdrkJSePWN5qvNFaIn2nCzPQyPzARzfjFnl0tZ6-aS0ZsF3yu1ye-QxPsiVf7olk_s4-4lj0eXSajOtuIvMrlYstXhSLxEncDPqW4OOwoalUuDK98E14h-Y7FSa4LG6RJKcOk-si8qNgTg-2cEnasiAbNmy9cCHlq0WRUpUNEaswEfIB3acTX5KBg5_H5AW68CwCuC2FD1U-ICYdufilxjEhSwTRq09ZABwD96GFJdfAStus_4EVV4eePioLaKAthb_qjrC5dAghwv_uYtYZFkgjkR3Vkok_b6oKNU0quVX_rFcKviAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846f23996a.mp4?token=koEU_gjMlToIJNq5VzXnAeQqAr4CZtc7KCSdrkJSePWN5qvNFaIn2nCzPQyPzARzfjFnl0tZ6-aS0ZsF3yu1ye-QxPsiVf7olk_s4-4lj0eXSajOtuIvMrlYstXhSLxEncDPqW4OOwoalUuDK98E14h-Y7FSa4LG6RJKcOk-si8qNgTg-2cEnasiAbNmy9cCHlq0WRUpUNEaswEfIB3acTX5KBg5_H5AW68CwCuC2FD1U-ICYdufilxjEhSwTRq09ZABwD96GFJdfAStus_4EVV4eePioLaKAthb_qjrC5dAghwv_uYtYZFkgjkR3Vkok_b6oKNU0quVX_rFcKviAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108137" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d21db945.mp4?token=YmK-Y7jQ8WCSTb-8lzD6ibWjkz93Gx7LaZQpWDVk-KP0z-ejO96x5jECjxN5b9gXAljX-ccqz74dKXG8xNjZL0LDE4zYU2tXs4M-AW3wGYU2-SIaq3rLqk1g2fBc28Rs__e0ncIShRSVreV9ajPPP3EPFCpddPJv2iMIGYfgLCRJ9hnk7lT_-CJalEdQCRlLE1-lrwxUI1lrka9HFBc4qEK2gpiFXZW_8_jCOmkhS7jAUoLqvJ8IW9S8ipUGhM_IASEzW3nH12I_ilB-dMXMC9TtxrjwV19vTvP5gQkg4I_v7ff8ZFL9ksADdUn9qqp3stKoqUhRySpBdPTwDUbNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d21db945.mp4?token=YmK-Y7jQ8WCSTb-8lzD6ibWjkz93Gx7LaZQpWDVk-KP0z-ejO96x5jECjxN5b9gXAljX-ccqz74dKXG8xNjZL0LDE4zYU2tXs4M-AW3wGYU2-SIaq3rLqk1g2fBc28Rs__e0ncIShRSVreV9ajPPP3EPFCpddPJv2iMIGYfgLCRJ9hnk7lT_-CJalEdQCRlLE1-lrwxUI1lrka9HFBc4qEK2gpiFXZW_8_jCOmkhS7jAUoLqvJ8IW9S8ipUGhM_IASEzW3nH12I_ilB-dMXMC9TtxrjwV19vTvP5gQkg4I_v7ff8ZFL9ksADdUn9qqp3stKoqUhRySpBdPTwDUbNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‼️
🇮🇷
واکنش نکونام به مقایسه خودش و اسکوچیچ از نظر هواداران تراکتور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108136" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDHtWbBRAYEKuk-Qg39hK_4Ma9WmILrsIYYc1iTZFuWuK_L7z8jby75EJutrpSms3mxLxImKZ5QdIabOo0tZpw_JpmGG7PztUkl1HwbdkCHQqH7yLZL-42Yuyc0gozlIkgfUeFYPxAMb3ZDUbHXGc7xjplDL3pXDtRYb1w-Lrf2OvpHwmAVUF82pAcqi0LP8hWQddNiX0eW5n67Zt0mCDlePNK5qHwNeXQ8R2aPv6pUXDifzpVnrjwG6oM16Ykui_0rX35gF9nVanE-hLU9phOZjwiGh6IHL9UcUR-GfbUwwno1boEDEWqfwGGdBdgMJy880N88ScqzGd3P8AJnArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108135" target="_blank">📅 20:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=tfbFheP1g_wNfpWs7V3MOIeJuH3PXHq9oVwhnSgUYBw0K6SWc2oWu3FLKyQfpRepcgjm_eycBc_3rDvTLDm9Dpihyd7TniSGp9hNkcq80BwogMd8xuqtDgO1wx3Xie-47PUr1jCDJw_G9qjRZcQnMQIfH9FPJoYw3srPDbRT9D2y4ahC-reBaIP2ZIPkM4Gl5X5Os9NOIoxNAV92pk7Qm1pQp1cQgcEq7NkqtdmPRLAe58W08vx3LHZ6XaKw0hHaabOa1j0Aq5ZFP8Y41YAwObTh2VgC6hECdgDjxte1AXln8_AVbnNqXgR10QWiO7LFM3VRSqpt0eoVFf6oC9qeBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=tfbFheP1g_wNfpWs7V3MOIeJuH3PXHq9oVwhnSgUYBw0K6SWc2oWu3FLKyQfpRepcgjm_eycBc_3rDvTLDm9Dpihyd7TniSGp9hNkcq80BwogMd8xuqtDgO1wx3Xie-47PUr1jCDJw_G9qjRZcQnMQIfH9FPJoYw3srPDbRT9D2y4ahC-reBaIP2ZIPkM4Gl5X5Os9NOIoxNAV92pk7Qm1pQp1cQgcEq7NkqtdmPRLAe58W08vx3LHZ6XaKw0hHaabOa1j0Aq5ZFP8Y41YAwObTh2VgC6hECdgDjxte1AXln8_AVbnNqXgR10QWiO7LFM3VRSqpt0eoVFf6oC9qeBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108134" target="_blank">📅 20:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=Xb5YetDMw-huZXO_SQAhE3RLrpCafQnRtSI5rTjJPTbDUWi5GcbGGXMmg3cTthN1aitguahqZ35Z4qJdTvpuiAG3ZXRMtqzdtrSzLSe1jl00_w87mpV_xU90cPcsXunRg16t5Wpa04SFTC0G7fLoFecwhrXVeMOlWXQobtmsmN7kS7SkHmUAZgVVJzORbLDTXAIpyIdsGauoWS7Kc1oDuaVLAT8WbPl5bXKPenqNM09yvm_8Lbg-CoYDi75BxBUf4GUBaAojhE3L0h1Po9WOxB_xprosIhHg5HuoFC_KE31ZAepnPIB3tEKUgnGH-3VEt6WcHGvwvD0ESo53ClPcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=Xb5YetDMw-huZXO_SQAhE3RLrpCafQnRtSI5rTjJPTbDUWi5GcbGGXMmg3cTthN1aitguahqZ35Z4qJdTvpuiAG3ZXRMtqzdtrSzLSe1jl00_w87mpV_xU90cPcsXunRg16t5Wpa04SFTC0G7fLoFecwhrXVeMOlWXQobtmsmN7kS7SkHmUAZgVVJzORbLDTXAIpyIdsGauoWS7Kc1oDuaVLAT8WbPl5bXKPenqNM09yvm_8Lbg-CoYDi75BxBUf4GUBaAojhE3L0h1Po9WOxB_xprosIhHg5HuoFC_KE31ZAepnPIB3tEKUgnGH-3VEt6WcHGvwvD0ESo53ClPcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌کاشته مس‌شهربابک مقابل فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108133" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
📊
🇮🇷
جدول لیگ‌برتر پس از تساوی امروز استقلال و تراکتور؛ پرسپولیس در صورت برتری در دو بازی پیش‌رو خودش به صدر جدول خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108132" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf998598.mp4?token=fbc1zpzhITNOEjs--BEUUi5TfTxa2FjEMluxkTilFyyGbhXFFCHmHGD8s2cXrxNCIpUOmkMesp0CGYdwf2naSqHuqGE8dRgWJ_b8FLiArOSRVT8Ft4DGZ8AX2qDrIsiGd5ROZpQqpGlWrHb4SMKHQmOQwgLm41gmP_lsjegLSnv61bCg5oAWfwxS0QJCvODadQVVz9or2klZlQSylsqxx6tUBZ5vbsJo6erZSpbivjVSzc-M1toDgb45bd2mCWdGnaiEoWjT_k-fVa9p1LmiCPk5xr7HNO8f_vA-a1Tm9KgvPeBQSCIXOu0WrkGLa4z9RMfJ7N2MTvtW8yUTk_hsBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf998598.mp4?token=fbc1zpzhITNOEjs--BEUUi5TfTxa2FjEMluxkTilFyyGbhXFFCHmHGD8s2cXrxNCIpUOmkMesp0CGYdwf2naSqHuqGE8dRgWJ_b8FLiArOSRVT8Ft4DGZ8AX2qDrIsiGd5ROZpQqpGlWrHb4SMKHQmOQwgLm41gmP_lsjegLSnv61bCg5oAWfwxS0QJCvODadQVVz9or2klZlQSylsqxx6tUBZ5vbsJo6erZSpbivjVSzc-M1toDgb45bd2mCWdGnaiEoWjT_k-fVa9p1LmiCPk5xr7HNO8f_vA-a1Tm9KgvPeBQSCIXOu0WrkGLa4z9RMfJ7N2MTvtW8yUTk_hsBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
💙
سعید فتاحی رئیس سازمان فوتبال باشگاه استقلال: پیشنهاد داده ایم تیم‌هایی که جزو 8 تیم برتر جام حذفی در سال گذشته بودند امسال جام حذفی را برگزار کنند. پیشنهاد خوبی هم هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108131" target="_blank">📅 20:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=XH1H4lOBqM5mtvy0rvAV1P1s4IXlzAvEEy44GTrFJ31KYAf30dV-rCG-LxIEua2LaLsloMErjthuejlURqmZ0oLk5Wiitajk0xCl1kANoglgMxy6QKMLJ1lbu8jnhHmkDPNCC8u3OpWLGsFUkGb0yVZ2urZ4P9HrIsgh-5dzZqgSzaBixcgN8-6rGmAl2lqtIEGSI05Z3gzN-zKh0IPBwNsuLG4I-oG_UmmTlEKPrJvwZn8L0vDFLLe2uQ8rj_y4PbwiNUcOrYFgOTrmMGHyplW_uEDnqvFI3PdpuuERxYFRJ7vZkCxX3TZJ8Pk7fAqjW3COfa2as1tnH-vU689ejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=XH1H4lOBqM5mtvy0rvAV1P1s4IXlzAvEEy44GTrFJ31KYAf30dV-rCG-LxIEua2LaLsloMErjthuejlURqmZ0oLk5Wiitajk0xCl1kANoglgMxy6QKMLJ1lbu8jnhHmkDPNCC8u3OpWLGsFUkGb0yVZ2urZ4P9HrIsgh-5dzZqgSzaBixcgN8-6rGmAl2lqtIEGSI05Z3gzN-zKh0IPBwNsuLG4I-oG_UmmTlEKPrJvwZn8L0vDFLLe2uQ8rj_y4PbwiNUcOrYFgOTrmMGHyplW_uEDnqvFI3PdpuuERxYFRJ7vZkCxX3TZJ8Pk7fAqjW3COfa2as1tnH-vU689ejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌پنجم سپاهان به فجرسپاسی توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108130" target="_blank">📅 20:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108129">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f44126980.mp4?token=u9FCPigCkVbwr-7BBuWuUgypaElJphsY-N6grF5IQXp3kxUHlu6VyBslglb2ktUEu2HAUV0_NgNuPHbAqzXQV_nVeBXWlohlsWYIf4YMdSW2XKUS5wS4tAFgNrzyXOTypeObPVXHqonBX4jXMUat1_lbNi75EDlCGfGeHnXVjMjE5ZCeAZnRwYpXKcmNqdTjpRWaxnYri9J-ig-5tc5hcI4yiMZQlQluO8IviacS_P4E5TQJttLqmj_3o-8ZD9VlAXjuDXkoibAoeQ8vAgDAZppjIlD4eJuOwHW_CPp1v8GFbGi3w-xZdM5K10lmjPKckBwIPYj_bkTH4r6PnAtCryCJgLAEilhLxS-YrTlEAin6o8iKwXOuo17jAR7DHd27-bmQY5aqb7w3qIYF_MMJwTJp75v9r7JuLaERGur9qujhPvE4TvgANAj11gIChFosdHJBKzWe7p-xzfGFBEEWebVhN7FfYTXDCl0O25R7GbAv8_6gUPrL47hLlFMstgirwUKsgUhurs7wTAI7IiIYj6Da7JZfoXTXKYqioYyDJkBUePeMX8k856In8SV3ETuGRUW4mTvpNHhiLWuVv3KJrtmaMsNNnZuSCZMY-bd9AaSCEq8PePslNtBdX2f7MjAH5a2geCc4ycYM4iOomb_QeMo2zSeHNW79wMRrr6SX9B4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f44126980.mp4?token=u9FCPigCkVbwr-7BBuWuUgypaElJphsY-N6grF5IQXp3kxUHlu6VyBslglb2ktUEu2HAUV0_NgNuPHbAqzXQV_nVeBXWlohlsWYIf4YMdSW2XKUS5wS4tAFgNrzyXOTypeObPVXHqonBX4jXMUat1_lbNi75EDlCGfGeHnXVjMjE5ZCeAZnRwYpXKcmNqdTjpRWaxnYri9J-ig-5tc5hcI4yiMZQlQluO8IviacS_P4E5TQJttLqmj_3o-8ZD9VlAXjuDXkoibAoeQ8vAgDAZppjIlD4eJuOwHW_CPp1v8GFbGi3w-xZdM5K10lmjPKckBwIPYj_bkTH4r6PnAtCryCJgLAEilhLxS-YrTlEAin6o8iKwXOuo17jAR7DHd27-bmQY5aqb7w3qIYF_MMJwTJp75v9r7JuLaERGur9qujhPvE4TvgANAj11gIChFosdHJBKzWe7p-xzfGFBEEWebVhN7FfYTXDCl0O25R7GbAv8_6gUPrL47hLlFMstgirwUKsgUhurs7wTAI7IiIYj6Da7JZfoXTXKYqioYyDJkBUePeMX8k856In8SV3ETuGRUW4mTvpNHhiLWuVv3KJrtmaMsNNnZuSCZMY-bd9AaSCEq8PePslNtBdX2f7MjAH5a2geCc4ycYM4iOomb_QeMo2zSeHNW79wMRrr6SX9B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇷
سوپرگل امیرحسین جولانی بازیکن فولاد خوزستان از وسط زمین به مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/108129" target="_blank">📅 20:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6h_v5QOQT1f0w4OIrIUOWQtB1vJs6VqMjTyzjJxbdKVcsu74Sw8r_R2ot5ZgyJ731h4nA8fLsPnufy51cEiblOk4TtEO9VQnnz5xegUZ9wd-RFybw13A1-m7Zx81RWp3iteI72iZvgBtCh1vRF01kNDT62QKmdFudKfiP7hi8sszxWFrtpIz3PKRcp7XWNh_7cEU3yuubJW4pE2J5Asct4cmnsctz3cH_i2c4vufxQYIwRn8qOvBpqCoRP_TjtlzmQuSiZuJRCBrrCQF5RLgUOOXrbc0hWi_9pDJsRylHcuKGaGYiDzVTUV8C2znMw__lLENsvXzjkRvnbAkd8oYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108128" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36afca847.mp4?token=ArqjHNdy9SOnCr67Kl_j9mjGHXgOERhNih1VbrS62jeHbQHsBA7ixOTdJ7XKuTvlIlbKiyUnnsblXsK11dYmhlBaA-kauc2DCFzIh41SWKt2eBT2N_QJZMbzgtv5HEovcju-XL5f3Tc3ZDjkccg9N4uI5TBE6u2wcR1Wtgsnd6Xm8iO27tD2ZvNY8OsOeWZ26IaBZ8oqPPfLuM8HEWp-nyxaniOxt2MIWqcJE6iRK5M3VKnpRGfhKVLqXZWL1fb7ctH8U7ZQ8EnAAYEmfiUvCHPTK8vN1EeyUbOhopuP7odbBBbsraJ4xRRoQgxQFHUZvIaW5ImF1WJDyHrIs_JTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36afca847.mp4?token=ArqjHNdy9SOnCr67Kl_j9mjGHXgOERhNih1VbrS62jeHbQHsBA7ixOTdJ7XKuTvlIlbKiyUnnsblXsK11dYmhlBaA-kauc2DCFzIh41SWKt2eBT2N_QJZMbzgtv5HEovcju-XL5f3Tc3ZDjkccg9N4uI5TBE6u2wcR1Wtgsnd6Xm8iO27tD2ZvNY8OsOeWZ26IaBZ8oqPPfLuM8HEWp-nyxaniOxt2MIWqcJE6iRK5M3VKnpRGfhKVLqXZWL1fb7ctH8U7ZQ8EnAAYEmfiUvCHPTK8vN1EeyUbOhopuP7odbBBbsraJ4xRRoQgxQFHUZvIaW5ImF1WJDyHrIs_JTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل چهارم سپاهان به فجرسپاسی
آریا یوسفی در دقیقه 54 دبل کرد و گل چهارم سپاهان را به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108127" target="_blank">📅 20:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=fmXGUAIyUOyihF_jUykf29oHT0cSfytIwjPhH6hVGvWmzj-bndJCyMWrnAj0aumXHy2HXwZEJA7mofH5HLVYqflV6ylxzpq0Yu13Wa8fc-hCoAQLP7az_PIY6jr1YzZyfX4_LgfU32rRMSodxjX4LZ5tdCoGM7yAFO7nbgQbsrkySTb07wSjUxwPQwDOO-75L-J3sOukeLQAb4u-FEITRBg1GYKL5QXxzRDdvUvCTo0wZCRCUS3iX8U3hnrkYSM5PoqPqKZQLrfeyovJyD_n4KH5nt3XO2R85EdnSxHCL3WX7iHUxr9qd0H0Q5sevddo3qWxSDN8lTW7aakokaB1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=fmXGUAIyUOyihF_jUykf29oHT0cSfytIwjPhH6hVGvWmzj-bndJCyMWrnAj0aumXHy2HXwZEJA7mofH5HLVYqflV6ylxzpq0Yu13Wa8fc-hCoAQLP7az_PIY6jr1YzZyfX4_LgfU32rRMSodxjX4LZ5tdCoGM7yAFO7nbgQbsrkySTb07wSjUxwPQwDOO-75L-J3sOukeLQAb4u-FEITRBg1GYKL5QXxzRDdvUvCTo0wZCRCUS3iX8U3hnrkYSM5PoqPqKZQLrfeyovJyD_n4KH5nt3XO2R85EdnSxHCL3WX7iHUxr9qd0H0Q5sevddo3qWxSDN8lTW7aakokaB1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل سوم سپاهان | احسان حاج‌صفی '47
سپاهان 3 - فجر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108126" target="_blank">📅 19:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=FrtPi0m3NEhNIkvpa0f3v-kOYFMR5mcNavLucHzb825AcYhj6kQEzsN3jIOgS6wmHeETjK3ivBL-A7alW1za7LDykj_U3HfToQ1mQx2y_hkJqc_IVipBqF9IgRI6HbzdSKExkuH5rcebTgck8gGKfDhnyUjQx_vS7p6TgIV3pIRs3hWJcDzMbENiyCrpUfUMMrLDPUwBI0z_ew0LMyCsncQxYjgnpBBC8j0M0GI0-u-fhn1nOmtVgM_Dut6nZEj-3zk2P4Dtl49jSXRScU1vmJnin2IbVhbdGB2jf3u2csEMiF3kerwOPRaJSxDj8XgkO-2f8IRbX3TZpSbf353oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=FrtPi0m3NEhNIkvpa0f3v-kOYFMR5mcNavLucHzb825AcYhj6kQEzsN3jIOgS6wmHeETjK3ivBL-A7alW1za7LDykj_U3HfToQ1mQx2y_hkJqc_IVipBqF9IgRI6HbzdSKExkuH5rcebTgck8gGKfDhnyUjQx_vS7p6TgIV3pIRs3hWJcDzMbENiyCrpUfUMMrLDPUwBI0z_ew0LMyCsncQxYjgnpBBC8j0M0GI0-u-fhn1nOmtVgM_Dut6nZEj-3zk2P4Dtl49jSXRScU1vmJnin2IbVhbdGB2jf3u2csEMiF3kerwOPRaJSxDj8XgkO-2f8IRbX3TZpSbf353oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری‌زاده : یاسر آسانی بازیکن تاثیرگذاری است/ بازیکنان تعویضی تلاش خود را کردند.
🔵
کادر پزشکی تلاش می‌کنند تا او را به الغرافه برسانند.
🔵
امیدوارم مصدومیت او جدی نباشد ولی احساس می‌کنم کارمان یک مقدار سخت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108125" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108124">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=DsylIOn3ku96frDtj-8fkygq8245_oDpKUV-uL6hDZC3fw4F4465SFlVBBWAc0R1dqZcCCI4sumCQsNISU9tdSiDwRtpuk7e69LBTV6hGpLFbX3_UzvbFrXEOop7KRqoA6dyhQSdKck72mlgzPJsEVCNJBIrO2sPQbCIiXrvHW3S3krE6E0clOCK7lgYi2jUaLxCIZeVZPLp_8UwLPgYK7LF6hRz3ndYyFpXXjLh5dZsBPJtSKdL7RMjiGjc_24bz-PTRTG6z-PIaUyIV8gPeiS_CiO4MekyAiOp5riGBAIS4cYrUZkvNkVpZQB642rnuOrzS8uJWzicd8J7foC2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=DsylIOn3ku96frDtj-8fkygq8245_oDpKUV-uL6hDZC3fw4F4465SFlVBBWAc0R1dqZcCCI4sumCQsNISU9tdSiDwRtpuk7e69LBTV6hGpLFbX3_UzvbFrXEOop7KRqoA6dyhQSdKck72mlgzPJsEVCNJBIrO2sPQbCIiXrvHW3S3krE6E0clOCK7lgYi2jUaLxCIZeVZPLp_8UwLPgYK7LF6hRz3ndYyFpXXjLh5dZsBPJtSKdL7RMjiGjc_24bz-PTRTG6z-PIaUyIV8gPeiS_CiO4MekyAiOp5riGBAIS4cYrUZkvNkVpZQB642rnuOrzS8uJWzicd8J7foC2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | احسان حاج‌صفی '38
سپاهان 2 - فجر 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108124" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108123">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=j4VmpV4DFK-iDCkldWEUJwV0Lp7IoIT5QoceSaMDVXjHmwLHs9n0jenGwD_1qLTT9AWKmomVewsI_vy21cOpeqvLvfVzSXw8XOYM1Go6f5EpiEZ8wApU5B1xFNZKDg7SYKEa-_1Ult0iesQ45vwYWF7nwQD_avJJAg-HZujCDsHrNYiL5fpiWWYa1X1BAMfXe7fKxqqxvTKjOo7VhLoI0AXNOdKSNBSNDLuKSk9VPPyZhbgnf5QdGJ1QelZl6CMEMtq4qaVAGHpNrJ6EZDd2_B8V5mgaJFVmXoQ-g7tLAr7mh1lxE1iVd_8kcbKneb8xFOXdiM7jOA7bTmqbLRmEhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=j4VmpV4DFK-iDCkldWEUJwV0Lp7IoIT5QoceSaMDVXjHmwLHs9n0jenGwD_1qLTT9AWKmomVewsI_vy21cOpeqvLvfVzSXw8XOYM1Go6f5EpiEZ8wApU5B1xFNZKDg7SYKEa-_1Ult0iesQ45vwYWF7nwQD_avJJAg-HZujCDsHrNYiL5fpiWWYa1X1BAMfXe7fKxqqxvTKjOo7VhLoI0AXNOdKSNBSNDLuKSk9VPPyZhbgnf5QdGJ1QelZl6CMEMtq4qaVAGHpNrJ6EZDd2_B8V5mgaJFVmXoQ-g7tLAr7mh1lxE1iVd_8kcbKneb8xFOXdiM7jOA7bTmqbLRmEhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108123" target="_blank">📅 19:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=bISCQ2WKw-tT6VFfjDRHwnKv_BaA01WMlqiCK8a1IsWbo-Ih_sTRElUdR5Rb2yM3FdpQgQ7KPezqOiWXdf5eETOhEc6sACaaHMeRu9FgNyIoYNqYf-C3vhjJHO3_aq_V_-VUd81QSNbpDNsL1IpQGwx8EZuJHsHO170m65CX0jt_xwSbcE1SeYWfzJTzsCatF7Ic-d8QGxZNKb0qI5Qcd28_MPpgiytvNFnjtp1bTkd7Lv1pIyYviyehhsVYW6a7EH4zpWe16iwT0MFtr7FDr_-HK-muXvMGepCfY-j8wqZaCYjK9akVixgCinrwtCqTqMYjwz9uVtBfKmyWn_B1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=bISCQ2WKw-tT6VFfjDRHwnKv_BaA01WMlqiCK8a1IsWbo-Ih_sTRElUdR5Rb2yM3FdpQgQ7KPezqOiWXdf5eETOhEc6sACaaHMeRu9FgNyIoYNqYf-C3vhjJHO3_aq_V_-VUd81QSNbpDNsL1IpQGwx8EZuJHsHO170m65CX0jt_xwSbcE1SeYWfzJTzsCatF7Ic-d8QGxZNKb0qI5Qcd28_MPpgiytvNFnjtp1bTkd7Lv1pIyYviyehhsVYW6a7EH4zpWe16iwT0MFtr7FDr_-HK-muXvMGepCfY-j8wqZaCYjK9akVixgCinrwtCqTqMYjwz9uVtBfKmyWn_B1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
شجاع خلیل زاده بعد از پایان بازی با عصبانیت بخاطر تصمیمات داور، راهی رختکن شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108122" target="_blank">📅 19:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=uYbukgQeEPbTZIYrd0eoq2v45hO2WdLNOMZRKKY0JCkusIqDekM1WKe30qaNqaSXiEAVhi4d87RGQ3WKi1DJ4r9z-AKElKMe_ImrrLF7CeTK2vLf_E2PaSLFoHxWFKT9v4q4cP6tfEnK90GrL73P_A7W3XPXkXsyNc5VnJVxJ4fqIozCQ9Fx_BofODWZRqc1yMNKzJhCGXFOCNUR0-YGO9P4m5buciqtYelwRuQS494SfBDjAfK2gcDlL_inTEFa-eqRwUjgamooRiRjMgyWbPao44n1ePqyV2xuMhL8yRaeNas2lao2SZiWtT46MoGsGc_F7Zj9kELa7vkaLIEdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=uYbukgQeEPbTZIYrd0eoq2v45hO2WdLNOMZRKKY0JCkusIqDekM1WKe30qaNqaSXiEAVhi4d87RGQ3WKi1DJ4r9z-AKElKMe_ImrrLF7CeTK2vLf_E2PaSLFoHxWFKT9v4q4cP6tfEnK90GrL73P_A7W3XPXkXsyNc5VnJVxJ4fqIozCQ9Fx_BofODWZRqc1yMNKzJhCGXFOCNUR0-YGO9P4m5buciqtYelwRuQS494SfBDjAfK2gcDlL_inTEFa-eqRwUjgamooRiRjMgyWbPao44n1ePqyV2xuMhL8yRaeNas2lao2SZiWtT46MoGsGc_F7Zj9kELa7vkaLIEdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
گل‌اول سپاهان به فجرسپاسی توسط آریا یوسفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108121" target="_blank">📅 19:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108120">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_YZspQolxCT2PijSVqwkiGaFzC0UjyLuPAdLrmmCtNcnFGek6p6grbDbjihYxIq1ef5T1adf5wmOi6blvaiNMz3U4JxFBjyf58c7Ag7MBVdW5RDgx51LfKhG_7Xvk-GajP6VxNs8N3h-UwpFqdF3-zC_rmwAZ130tdkTdtEfDyxEsCRjGNUiJAN3z6pTnZE54mkUykFxmXQ1WUSgNt8zygf5vxGh4uz0nWzz9qUUnexdOHHsflj1ZtNJ_Aa5r1reLSCs1spxx6nN5vWfqKahbPmnrItRZDXx9k1iB1G1scRFeEazH-uITcQu7tE7wAJFblCOJZ7Z1_Zn8yzJ4CDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108120" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108119">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d09wOCS_WocYr1CPdZBixyI8fRywj_cCyW8dPq8ABg39ZulKepe0NlmWlD0tn4mgSVF_xYaeG0khAzAVH_9GENVLDdQBZtKMpqbx2-IZAk56WuePpXnR0iRdIHwU7NYfgzMRzeYdJQMHlUbSbYGmWoX9I8Si_NxsNTK-oaE7nYWQTh4yj_R2kZUKskXKWg5sRJHH1sKWylaoea-DGHLnyeQ4ormjUj0KN9diRuvXI6D7vq3WsZERRpkNLJ-tfJEUUUlw_OqIRZC3j-TYeHM3riGW2tTzDnaEIoj2F9fENbsmBykxWI8OJe6NKIKMXydozDoGe3CfxQycze88DaseAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108119" target="_blank">📅 19:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108118">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndSawt3sj9kRs-9is3c9FCqGsZd-lSUlWmwpftNM48EH4nz3XfRqbC9ACfaUcz0lxVJcABRyj8jViJuUbwnXMtOd7F59QZPfV8cMJYuSKQKSbVibz4Yh-fwshA54uW2D5lgLSaMHiWbp1tPTrE0CdNbl4zzghMVM2FBFTeB4YHHqobRoOUQvSgiir5ab-n0n8UmU23aD6NnnjideLiyycbRekL7WELI65IUDfj4pp1xEHZ-LAEHj-SXCpNJZl_vAyerzIKC7piL10ExPl91eD6XDnAlwkxM9b9WuNYuZspje7QxsDfIqusTNM5GGbfuWVdK3134bHEMG8kNk8k3wUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108118" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=vjO7c4nQK9GiApZWZRG2eJPadME3wojFFS2piXzkOS5ARfT67ZuChWCSRDg90J3oWz9u3K6P1bVm6bwruVj6Ku6U6MkTpvql8w_67e9A9FMH2ZUK4hZRr7ft78Ya8gQ2yzoP9tp-EXxabeDpQJtWUp-ekwzwDvS7gLISYRqmPLINlnGVv2jvE0qcbBAGszHu0CUooAyw45mB4CnOTquzijJf3EYxzC41yfmMZLuNWbNbDa7d_J1JH9qTBFsnU1Mn_dO4RqjW-_tz2VnXfgQk9hxWWUH_kFvI3_uk1xPnpjUpEGpxxC10gMN32ezopDRN9ODWMJAbt3Ex9eFpdkCyNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=vjO7c4nQK9GiApZWZRG2eJPadME3wojFFS2piXzkOS5ARfT67ZuChWCSRDg90J3oWz9u3K6P1bVm6bwruVj6Ku6U6MkTpvql8w_67e9A9FMH2ZUK4hZRr7ft78Ya8gQ2yzoP9tp-EXxabeDpQJtWUp-ekwzwDvS7gLISYRqmPLINlnGVv2jvE0qcbBAGszHu0CUooAyw45mB4CnOTquzijJf3EYxzC41yfmMZLuNWbNbDa7d_J1JH9qTBFsnU1Mn_dO4RqjW-_tz2VnXfgQk9hxWWUH_kFvI3_uk1xPnpjUpEGpxxC10gMN32ezopDRN9ODWMJAbt3Ex9eFpdkCyNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال توسط حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108117" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سید مهدی حسینی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108116" target="_blank">📅 18:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تراکتوروور زددددد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108115" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108114" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=KAi0FJ6xWSyFmEvwbNf4IkvOCqlP4W3qsPBHHyeZg1lahswAnJ5IgA-uo-8Y-V_TnvwIxQo6niQpuRkTBmsifkQW9EP3h68R_DkuZrBzf646BJ9f8AQjc1WLR4n7q44an7mpn4xlpoj-LETnkSzPLTnRPe4ptx9Hlcq0HJfzZVWkDKccaRWQaH4FrqGF3CgVpkK6r7cVAdWb-nWgfQYomEG1ug4iU5H1rvJiqxc_E-TBI3FlrNIxT8Xyz0X7m_gjcLH6sJEHJLImKWEv3aKCgbxxY6cv0k6kQTJHCWY0YeAaTmaGqIFn82oLaL7PwL2BYzNgR8DzyoyOUe3_AUov_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=KAi0FJ6xWSyFmEvwbNf4IkvOCqlP4W3qsPBHHyeZg1lahswAnJ5IgA-uo-8Y-V_TnvwIxQo6niQpuRkTBmsifkQW9EP3h68R_DkuZrBzf646BJ9f8AQjc1WLR4n7q44an7mpn4xlpoj-LETnkSzPLTnRPe4ptx9Hlcq0HJfzZVWkDKccaRWQaH4FrqGF3CgVpkK6r7cVAdWb-nWgfQYomEG1ug4iU5H1rvJiqxc_E-TBI3FlrNIxT8Xyz0X7m_gjcLH6sJEHJLImKWEv3aKCgbxxY6cv0k6kQTJHCWY0YeAaTmaGqIFn82oLaL7PwL2BYzNgR8DzyoyOUe3_AUov_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
داور بعد از بازبینی VAR گل تراکتور را به دلیل خطای هند  بازیکن تراکتور رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108113" target="_blank">📅 18:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108112">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108112" target="_blank">📅 18:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108111">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
احتمالا خطای هند بازیکن تراکتور</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108111" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108110">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صحنه داره وار بررسی میشه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108110" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108109">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726254fc85.mp4?token=mEL1xNhq7aSKVM8mb7manMYlgmtmgm0ebyyI8kaigpZsJwPtencJgmrsg2xx6mY8UiyONx2Ki2Eyh_iOuqmRWUpgP-3OSPWpvTcwBT40o4d75tu0zC-s6yx8ngd_1T3F2BpYiTHkHlcCHVYkoto1-5XLOW57ojoQZjuZr-N0OsScRldVux-ikJa2asQPbBEmRfvrIyAaNSKEpMigdpfYg3heRa2ofxDsshfYB_WQy7Ytm7bgzszZcPRAwSNS_yPUe4ehMb3YJTJqZMd_K0bvOMWi6nLQZIN2qdWJWRtD5OZvJ1Lp2fPlTerCPi0figVW_mKpXgGDI0AVV2-GyPFRsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726254fc85.mp4?token=mEL1xNhq7aSKVM8mb7manMYlgmtmgm0ebyyI8kaigpZsJwPtencJgmrsg2xx6mY8UiyONx2Ki2Eyh_iOuqmRWUpgP-3OSPWpvTcwBT40o4d75tu0zC-s6yx8ngd_1T3F2BpYiTHkHlcCHVYkoto1-5XLOW57ojoQZjuZr-N0OsScRldVux-ikJa2asQPbBEmRfvrIyAaNSKEpMigdpfYg3heRa2ofxDsshfYB_WQy7Ytm7bgzszZcPRAwSNS_yPUe4ehMb3YJTJqZMd_K0bvOMWi6nLQZIN2qdWJWRtD5OZvJ1Lp2fPlTerCPi0figVW_mKpXgGDI0AVV2-GyPFRsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108109" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تیبوووووور هالیلووویچ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108108" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تراکتورووووو زددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108107" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108106" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">همچنان استقلال از کووووون میاره</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108105" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">استقلال از کوووون آورددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108104" target="_blank">📅 18:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEvu-q7s88zHSd19vci8mddlUedok4vRLxquf1DeHzCTo6DCbTj7j3B8im-MOrsgt0HwnbpY6WEbTwqYPhUmskNdWv83MszPJMC7xv3wKjknDYo-1Gpo4szWbxROvjhLdAE8ZyjQJMH7db_AOz4eXCki9b-iwZA6DJ72z5T8XgGI69UYefVN22rX2zUmbUPC5k6MgqOi3MazNB44ExA9brAoMrygw_gQsZf0TvauTyKI2ZrrBgSWz370X9Sq_0RTjwlK_c8ETnhdlaLH4huwks0Upniqj7w0lIxpOui6oK10ZpMKjo9GsjtIoaigx0QkxgaZN3L7NLs2fbk5Imi7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم فوتبال فولاد مبارکه سپاهان برای تقابل با فجر شهید سپاسی⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108103" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjyS4rHGDZ7hkj0BeLDPTKtI0_CeaDglCj2J4rC2R95eP7Imjtn4VkQ9QXbSuMFzFlzLOTeKN_5He9bzusnkrylH9aoBTCAfPBS4fIFj21v632QeGqHzZ6GIIwi5NAnqRHdiqLXSZ8MYsbW3qY5s7yVlZ4hLF4ariETf0KzW41mXl4hsTd7b-3FfxFUzOjF3atzqv5irCvErM5kPEcPHG_7mq45NxBvXv9yzDRzkkliaR1aWKV5v16cT1ITWRi4o4H_mSkHZg0Fnu9inYZwSqPEqtbjUvUnMv-asg14Rba9XoHD23XSZlPijFhbmP48pLvI9duN7I-rGQzlanmYVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📲
استوری منیر الحدادی درحال تماشای بازی استقلال و تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108102" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=uU2JcikRrb2tbzQjROMnSzS4jGmx6KpC0INLnwT9rQ-cI4Uxe3KUfXC0mR0v-lmhEOlVb2YhKtZbRpARAH1J9BRxbWygwiCopN5lr3fvxmb8oeED7IW5SncMLXMMjck_oAUW0qPglLGhqTrla2JBbjSkyaM5G3qzS4l4BY3smP7Nw8BQw5OAY0JpYMo7A2APHwnsTFFE9O60NEQmpwiQiwnLoMEmDkyPh9h0PIz_hzoTYdvIJ4rAt3InytCF4X3zx5raf_keV_unVn4n0C7wRA-2bCT08XeJI4z65RdS7KGEFX5YaACoQnIrlqJNmA8XaHsE1ucKqo6JDNdv2N9VKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=uU2JcikRrb2tbzQjROMnSzS4jGmx6KpC0INLnwT9rQ-cI4Uxe3KUfXC0mR0v-lmhEOlVb2YhKtZbRpARAH1J9BRxbWygwiCopN5lr3fvxmb8oeED7IW5SncMLXMMjck_oAUW0qPglLGhqTrla2JBbjSkyaM5G3qzS4l4BY3smP7Nw8BQw5OAY0JpYMo7A2APHwnsTFFE9O60NEQmpwiQiwnLoMEmDkyPh9h0PIz_hzoTYdvIJ4rAt3InytCF4X3zx5raf_keV_unVn4n0C7wRA-2bCT08XeJI4z65RdS7KGEFX5YaACoQnIrlqJNmA8XaHsE1ucKqo6JDNdv2N9VKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشک‌های یاسر‌آسانی هنگام تعویض از زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108101" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
