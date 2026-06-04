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
<img src="https://cdn4.telesco.pe/file/X8NG3rU_VPDH4CQ8f8kwC71K2QnnyQN67trcyFtZwgo_RqpdHEOn9hjksb_PHK0m89suYa3t0TN9O585AMzNXfMAHoAiApcTlkWlRd8zUn8Osi6VJO0Ak8W8HwsGcxLsJP6_NjTe9mQzFmqdrPFw9QiRniDYEEtlPSN-hW08tSpB8HwNT0t95WbskzwyYs70iyuEBhzs8OuMb-692oq1eyAwjcsTVRwx8aT5s92qxA_1d4eRQUFSHP0uPy95vhrNYIU9LWYQFYKQ0qRn1m44RWmuatPrv8eDD3PiHHkOVY6DeFYy5WhXoNrtg1jpgDzNHktzfixmVJU9yx1kwM2Q_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 229K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gngehLb536bd5d7zN4l0GqiWdfwLwLV_DvB5zfnH3S3gbLR6gyEg0jg_GYz-2Vv8BEGSQhRs-TXzUI9RWUpYdiYkctPpCWBODGab0jPQPw6P5zGotcrB2cGdrF2vEPavdP0_qCLtwBW0Lo3zlhseq3BIGgDl6yBtGxN74gSh1thAGPHOKxygE62wfbTF8Tny4Um1QrWUDCn8VbvhBcOVIu5QskHkPw_27RRV4BsTZigb6O8EbCwT0gYNVyIxPL8pedVn_fd4BkI02IsOsWQpk4mRvLRL_wGyyMq_mKH1lysVPyefTOYtPeiE4fXnbLCEciVONk00LUB-GFTEjCp0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce5X2rIXdp0Ty3x6kiXL9QQelw70iE6pjNynlEBWJ6hZFyWPHpf8KRkqyGfMV1FRwBCtCufvgiRP63PbII_fHPjcznroR_OSrTBRKCbtkBaBf-EAirTPLwkYzyLU7tDDm4LYVHLryMUAl8a5aUoZBxITXp8vhoBmmab0qRHlFVz9v4sVijBk0Ds3RDQHsLyx0JrW-jLW8-HID4RNgeS6VaYOEtHxfozi5gP6CrN5J6dLSwk0SeTgco9INXWgeVDhccHb3V5r5_oORbYmwQ4HulJam3Ri_21XETDZNb503vg_T3j6Teb6UvlSLlyEFfr5m_P6EgslktJd3rMsNWT6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCB05YnHxNSzcIynJW2Od0o5FOhqEQ_n14IQ78JV3cWcvBakTopEpY64MKBb_qMEOWRFaMmCNTc3QgIvo-fJlSOXsgindcU05pJkx9yOaxT4Bfv93B_c9CneehY23UjLVVrOpfapyZJ_rUPiXEj3er31RgVnNLvzCU1nMa7Hg3BvkUW7iIsgvQp2N55PeczO7_rYynSqdKWvY65BkcBEmcWQ-ZL1SPO-ZKosqx5BF_HDBLpoSLKazYEo4CTYGS-jrMW4ZulHbramJV0tS7v2nDcuJpkhTtiTxApU-BsUXCv19aG_DvtUa7IirfPv14vhQYyORyoVglTFEUdcEYR_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fapL9i97oPPcxuF7b_ULQTDmnEz1ZTYDj1u6USZri8Kj6a5MkgpCKzNqP6klmYm_HtZOzEzSx9XlTC4S1m3Q7IHVAistgRXiJJkdI1Z4JsKueg8-O3G9gnFbkyA18WzvGIM16tOkDWUOGDE4JGafR-BRw35-GOxFsc895-VIaji00jB1-z9i8zL5wp6uiAgkWXyD5NDr0KkeTo60_DMeaWGot3sW3KtALBBTLWBZM1O_874nkEyuV7xY84K323lHCfpleSQS4Wfj40dW-crV6ItyrrY2VfAVNT2bP9mrYovhVervww5HVpD9sMvLB7RkUIX5S_DdFj2vmEDDd6iJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB76IeXPa1lGkgHpHQxLsJB2QTSRHyEqj5_3XW33SeHClwtHQetTF9Y8rLEw30udtq_7DL1AxjqIKSLoTjTZYnbX80FaWbqA9xO6uIAEKvhqD-KFTdufnOv_OVwN88c1UrvH02ajbIbyIVJkfrSRpSoQw612xKOqdCUtd6tdfkaAubYhJUy7AsARQA29FLUJ0ObTN37ZGVBWTBjG_a6gz7AdZ7Gc9YwTymZBXc3yzx-LvyzqZty4Yj_xbWc-baijckmT-xJ5ZuGcno6CHJC6ThCHG2d50KWD4h79KCBBAUpsef56-A0cf-fZrRnZPe-im6Zn_kJngMU_Eph2xds_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=EF4I39g5mtf5jS95KN4PQrCo56r_y6FOrByTeuP-AfGTiKNcwJrM-vYn5YM3xukZCguVCOpfWVh7StFHRld36v2g8xwRNK4DFLIhd-h3rPXSjabxGA9DWluRUcXwx-h8GfSONSvj0b-IizaESls6lQo5y52ui9yo-bePlc6HRN-wcMdtUL-pOF7HBeLrznF5YFVgrjB-q96GY-EciRLJ3PUAALQf1C8qGQl3Cb51korgvnI-ZnamW_4A5-NprQtW4NprlhN8gEwfeOew_nsdduBiDconcQ0M5vGOTeXeZ4Hl-1Qn6loBUkvhkiF65QcVK4mbIWKSlq_Aj78bO3clZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=EF4I39g5mtf5jS95KN4PQrCo56r_y6FOrByTeuP-AfGTiKNcwJrM-vYn5YM3xukZCguVCOpfWVh7StFHRld36v2g8xwRNK4DFLIhd-h3rPXSjabxGA9DWluRUcXwx-h8GfSONSvj0b-IizaESls6lQo5y52ui9yo-bePlc6HRN-wcMdtUL-pOF7HBeLrznF5YFVgrjB-q96GY-EciRLJ3PUAALQf1C8qGQl3Cb51korgvnI-ZnamW_4A5-NprQtW4NprlhN8gEwfeOew_nsdduBiDconcQ0M5vGOTeXeZ4Hl-1Qn6loBUkvhkiF65QcVK4mbIWKSlq_Aj78bO3clZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpB7sMmOLO4CH7FWoBct2NNnCHZYSwJBif1s2WT9tOG74J79tjxYywOoMP2Iw6glYG9zJgplfyvKJ0qGteGmMyNjVz7ZHllqhJKyec5z5uXecIojX4iDCUHVNJb5LVqVoKKFSN1FOXMO_vRN2JFUk_E4NSgCpC9JCgmTJiyN0qLqteeXGtenKECP4HYwmVzmEwlDT7SRerULYeYhCMWMhIHQO9K881FKdJBLSpBvon2Zh65FmtThIRhonvxjCT4mWcQI-yjSJQMAsaFlr_3dKpp3y-4x4Wwtr0Ajk60scg0Oi93IhPgj8chrCQ6Wa-P6NNNNbpcWq7Ho7EOSjrItSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FS4RH_D4ZoY6lIyzUBr57ZzmF9OsYT9FYOZgI8If98ddGAN1bRoFJkUL8S-3f_CFoLpRPz1KJpCXgiiY0TO3EBvoik3YUsmAXzIWZ-dXQ-uUM5jBKFAv0qOebwpqqLtA4oZhBgdQuJwZJ_A5uw9ZCwwi8C0swfy58eWFvetP6b5xuZCA9Nwpj6sH19gnwlCBO8g0CnXgE6UBb5ra7XgMAdiH7f8YMo-CtF_YyvtU4AchOVPyFna2QiblWmVWkHROMDC88kqMo2RKpTh0mZr06cmGYhyYUWbe5ONQozekMHoRRHI7TwlFCykArQT_nA1hE9DZyVTI-iRVJipIzq0RWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFonwSfenbLuJAB5sZSkpbFkDA1jK8rbUslwBed0zVrQSP4-PXpnxF_sn286eULzUfLR2a5LKPnUOFz6e14LaOoqlwL8psE-2d4IGUCWQig7aW3C5AEHpNMb9ye3EAI_a2Cuy9Qp_jfAcN4Vf0WgnSpgy1finUY0rUT1M7hGyu0uiWVg_ixHj_sJCLHtVAVuSxS285Dqc7ATrwTSQ3quf6xSA3SIY8MLE_h9Xk7mtPfL3GzcgrVVPZVySsPC5OOB9o1_RcOn__VRdHVLU_Q2nszon5IRygrPhTlhQEvboOlfu8IC1HfeAsgNXtndbZmu303PPzGtyL6P-7nFevv40g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gleWuGShM-LRWHNph-tUXAS8D-7ypqzRlgZ267Cei9LmrjmkL3PP_AQp1qM5RrAdDiJ-zKTrZwjtjvMiPO3uDY5LSAG2wTMGJ8WynBgR89E19SWq1dQAAz1PrO2nsHhp4RxWcq5QzM9jAVqoungxFgDz3GF6W9oZWwp4ekoDY5cXuC0l0GR1nxSVWdtTD8_RZ3FCHsfkDd_nqDxILL-iQ46KpVhdxQko9_8UOuQUJynlDnEcqhdxYUivFUXHbD32mlOyT-SLVnuUlpNTAxJ1zmZJnHark5evajxbPqvCqaSGepuJzSiNXFe8IO2IIAsFSoNwpWbx8zESJLdDKXK5kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-C_FOHc1dp3DjbJUw3t0Ha9undlSyd7Truvjpug02HAMuwSJHKf4aAYEbWLY4pncfK5JiJntia7EA8pcIcfMZxYMGypMcnDOYMxNz0fDzVUaW_yC5qEDLIUqx65pOfb-cV1_x-MBrDQ6OkVS_47DecT9cGKLRRUbHy2TfK5Fr1Q70DkVCEZLICxOPiRlaqfgzlHfzHZMnrvZ2VEsuPAgGnBYp_LakaqKlLfVLzDqcLlbriXFMhfTnj2fXSLLO4cRt3iZE0XhMR4Jcis9fXHdj4RuHUpOrZFmyXBP8sUnzEL3Kc__uYnGqJ6RD2x3Z6Yv3h-fxgS6gvY0ih9biySWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=KzctxnV1GuQ1iL0VSjaF9UVDOrujlKDgNDVSFF79Af-pOPrpRLCZbqtC6Gm0lubtjbOFv5K2JLarVWTnIYAyzhemTEwjIKEyMFvwn9aZnn5K26V6bnq-9mdWtg7rPcC-dC8oofT76UNJQs4WxrnWa-oOcIRcpHzPwceydAR4Rg6ehMJdQSOM4xqH8_jT1cnLi0wxbjPlCQswOj-mJ8gK--S3l1WGUlWCDLF0wUeZuD35CrQPxNp3pZ0ROzbBsuESILrKyedhDPXl632qZxZlN3S1gvS9yAyZRjh6nW5CgwWC5KPULBxv7S1Qcg1PfoxiW2qT6bDBojQ-jpDCpdjUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=KzctxnV1GuQ1iL0VSjaF9UVDOrujlKDgNDVSFF79Af-pOPrpRLCZbqtC6Gm0lubtjbOFv5K2JLarVWTnIYAyzhemTEwjIKEyMFvwn9aZnn5K26V6bnq-9mdWtg7rPcC-dC8oofT76UNJQs4WxrnWa-oOcIRcpHzPwceydAR4Rg6ehMJdQSOM4xqH8_jT1cnLi0wxbjPlCQswOj-mJ8gK--S3l1WGUlWCDLF0wUeZuD35CrQPxNp3pZ0ROzbBsuESILrKyedhDPXl632qZxZlN3S1gvS9yAyZRjh6nW5CgwWC5KPULBxv7S1Qcg1PfoxiW2qT6bDBojQ-jpDCpdjUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ollgdOhhObQknNmfvziin_TmEvvAlYDsg-0OZEtyP6jO2tQ1Vx15jNh0kJRfskGOSMD_l-mckBOMZRlcfnAXlyMsagr7WDvp_g4NJS-YtIWFG-US56lKzYiYvdqv3oAmEZ2QGiEdtbz5SYhK9SOOnA7bDM9PdpdmDH3fL1JEMz_0bOqUokRYuN-v4BU1K3TrOqGH6R9dDo_Bq4-bC_D4WckIl-YwpKrCo4gzrwT_cFliSLa-ZvJKG4W-6ACRP00ftMmhL5Uek4bF-DUYchmB8gVz8-nyqt2aQLgRKcM4PMGoPjHsQq8uNTEASGjQpzDonJHYfFQ0Cbu3D3hvTR_Nzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTMJ3eXLn0jC172UogXR0FMaBTZT6vBIyHeWKdzM6pmIiDNIosaj1dTGcu94ZenUw8bXQoEZTPlTGAdM06KjJwvLJTrRqpvGF6NKL8vCj3qnfNLqFV_4get0--RnHoCcytNnn-EqYHp1TTv_xp33uV-VwhXQc-rAAqZsGhgZLEwGrFnsRk6LPXSF0fQzae1kpQEVLqJvTf4quCWs98vIqAy4s7IByK1VvmGdVRueuWoi1cgAf7lEUvWEYDEMVZFG9dyO-xED7LSHA0HfulabAQCp__Pws1LUhqvwZfpJozLAGhfmtiT7DO0FwXO6ca0tNCAGtfPLqZ4IHhahBnUq_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwEET47YdECgc6O9YbTkTs2EG8uFiqn_YHxMqodgE77Ul5qJXkzt0fJHFOxRlwZct4jG2SwcRoSFvqeLp-qu2sJZeyF7erCLrMTadUa8ZvLogLzrB5UTv06W0YDceplVoeZoFHlU3AhKiq3fYhc-Mbbvu2O4FKqcZVFLh9x9XDsZkPkVs7dbzMHxMAzmMVthbs_kZXKcdeh1cB4b7MO8ed1XHqSE3q-swXm8-I5DBKJodEsvSuGWXomLVDBlyunXqRmr-EABl0JBNkKkIeaTB3HsxY9v2G8aUJhrJMVBqEn7imsFWQ8iY2LZrqD7Vm6UTF9MIxUsI3NSroimfxoKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYPCY2GdNEd2BXv10TQ7th7SCKkLyi9QNX-vdg15fN5SIwWViz3tJ3DzGlWRH9v4UH3cO_1VarxlCZNzQPFHTwcg-5Ne3exBRPuuXQ4TMdva3t0Z9Nn3YuDok6ctFO_sAVjbu7C5B7h1g6NHE1C6z1wF6GMeTGulZb88sGSOsa2lblOHfBBqEzVxOD0Qt3dyQarcqN2fai0fSknYwIZjKJ2LmdKbHE39LKbVkI0m1Q4ONGHGRfG2jlF6AUqZRNDj8uB75MSkbW9PTPH0aXGZJiIg7HbIDyodJ8EXKvTkTrx_Kq6QMxVXpxQncs3N6NGFXhGSjehuTD21CejB0YqrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsrM6r5ixtA8F-0vayUosI_ZLCwinhcT6HKtIUZuj0CTGJGjQIfizfvXwQRCjowtVWVqLk2mwq9v3WhHBwV3L0hmJuM02L3tHJrS-g-7o3daPPOR-ArH7MeIMmPTMbeZCOtcrgEdJ7FpxMzK7S9x97dcAFinqKnGjEKCQ5GgZ4zwW5YX88eBiHZVLwvDHq7PDAVHHKI7rzUlDOM_Znn47XDJFHoyM30kS_oc_1PDThKSVflWjngqSLnRVxcd2BVAlz9otyx5zEvgIs1-fTDPi-Fx3UVwa3nRjsfHJaiX5PydVdp4eO28YwnkZIQZ3Ie_GhMe-qjUviGooi7rvrJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2sJTkcHkOnAnpUM65cV4-atZlXiYLJoUje01xJX4ylYpaUbnoKo1k7WIOVHCtpfMlXgVCYnpUu9bwWLXCU68IRLVubD6yEnI149rxfCkw9Of6Vhjydexhs4JBsv3e5-hJA--_LXrEhLLLZPnqZO-m09bqZI3I6ToZ-3uYn2kTICAIEk-e6RUnJBlx3CSBZdwyRp-eqTaMLb6h7ZB4z-q0qLjxe8IoNjCCm0wwkkc2ujGYR-O7w4zRXJu4YvNz4dwo67KKfDr44oIXd19iOfmSXcnsSx8J7qt93r3SGL-8MuejI5luKikRANxWUJTxb6n07n38CExS7Tb--OjCRLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=g7dV80XuEPW4sdZD02Blwunyri_B8AnuLJB4RHtLS11BHcx-r61wv2UTzyeNg9mxWa4agAzu3JB98kzbGzodGGppKba4hs9wTXMyEdLWFvk4pT0wKUpn0XajJjx4HzNp9xP_OedW0Ls8hadDiFT_RJD3HeRidRHHJ16a_wzwh_OXmqcg4BZ7IjCBuL2ru2nd7LrDvuHzUL5V3nSDg383yMvjn454rdMArXI06D86ggN0cT3TGy9YBjVt8oZQEgUBKoWnnn5s5ThDFKrwYBI2jq9iTSqEZCfFgS1O7VQa9aXQAvPcMZUXDAZQXuf8rrR__CvLB6w-jpWEJA-eLfxEYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=g7dV80XuEPW4sdZD02Blwunyri_B8AnuLJB4RHtLS11BHcx-r61wv2UTzyeNg9mxWa4agAzu3JB98kzbGzodGGppKba4hs9wTXMyEdLWFvk4pT0wKUpn0XajJjx4HzNp9xP_OedW0Ls8hadDiFT_RJD3HeRidRHHJ16a_wzwh_OXmqcg4BZ7IjCBuL2ru2nd7LrDvuHzUL5V3nSDg383yMvjn454rdMArXI06D86ggN0cT3TGy9YBjVt8oZQEgUBKoWnnn5s5ThDFKrwYBI2jq9iTSqEZCfFgS1O7VQa9aXQAvPcMZUXDAZQXuf8rrR__CvLB6w-jpWEJA-eLfxEYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=GhmRoQRXHcg_jzWd-Zc48E3La4j9nvYkRs-UOGMUTSIUzSyOPV8DvWcCDjBCT2ry2Ju1baX0dRDCUHtzxof9OyJWB4qjdBik_iiPqTOUmDUhNmYDDzqYkmzfJlbS0PK43J7710FRrj_E8kvjzGU0JTy8JpeYiK17Iss8wqgeXF852KyE71IlXYQrcEPT2U1JqU95zf2OT69ITL-kGUZ4ZsJC51kYpFqBpNXRKRuNp2mEweIIqs9F6fiev4tztIK5gmxS6-HMW88iOKavQOx2edBOQPabpo10zfkg4n7C1CuIf2Oz7NKwVK4ZZbblGmilb494id6DyT0dY4uWEy1bIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=GhmRoQRXHcg_jzWd-Zc48E3La4j9nvYkRs-UOGMUTSIUzSyOPV8DvWcCDjBCT2ry2Ju1baX0dRDCUHtzxof9OyJWB4qjdBik_iiPqTOUmDUhNmYDDzqYkmzfJlbS0PK43J7710FRrj_E8kvjzGU0JTy8JpeYiK17Iss8wqgeXF852KyE71IlXYQrcEPT2U1JqU95zf2OT69ITL-kGUZ4ZsJC51kYpFqBpNXRKRuNp2mEweIIqs9F6fiev4tztIK5gmxS6-HMW88iOKavQOx2edBOQPabpo10zfkg4n7C1CuIf2Oz7NKwVK4ZZbblGmilb494id6DyT0dY4uWEy1bIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=msORPn5oYgW5lrt7EboYY8OEpNYvN4EjhdeLRwF3T_VqsPcFfgPiCOXIY0RZtcnmMxCtFpZRBcx_HVUZFY-AeHcjMD-zzkV-RgN7DurMTU06Lkx2BKuwS-Ube52Wpx2luhsX8-IdRdGw0iHWPBGaEeupgkCZzlvY9LXZkuaO0_Yxng-gghbwUD08yIzOiiVwoPHTUsnPHkWyT67iYJ1Jt4NNJYRiESg1tRvhvKPmgLsMTWBBjLyRN7L5w185sgkIPiKj7EJ17ESXckL4buqBfgSXDBB2fIY5GKCFrCcsZ3ZjPUTCyvHNM7JRJSAcYNing9XV5QlCrR3LQENkgLquqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=msORPn5oYgW5lrt7EboYY8OEpNYvN4EjhdeLRwF3T_VqsPcFfgPiCOXIY0RZtcnmMxCtFpZRBcx_HVUZFY-AeHcjMD-zzkV-RgN7DurMTU06Lkx2BKuwS-Ube52Wpx2luhsX8-IdRdGw0iHWPBGaEeupgkCZzlvY9LXZkuaO0_Yxng-gghbwUD08yIzOiiVwoPHTUsnPHkWyT67iYJ1Jt4NNJYRiESg1tRvhvKPmgLsMTWBBjLyRN7L5w185sgkIPiKj7EJ17ESXckL4buqBfgSXDBB2fIY5GKCFrCcsZ3ZjPUTCyvHNM7JRJSAcYNing9XV5QlCrR3LQENkgLquqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go89qTY9dazAxoOftoIdDnNk8Msra200spkop9D4p_f0g6TyZFUO1kSdOPreBzoTLq0monIhrNa6O-bQB7YGTSXpI9ML8chNEmco6cbsFm9n33Fw9kTvg6IZhG--x52ajv91yCYayF5ccYn-mZxluEsyDP-mhoWd0ISYXFXwmKXO6nMi9mAmR5iMZ-sox_DWDbl4iNTIsK5D04zhI4LaEEEAseBCwAXmZ9Re9MIBM03OabJipa_5Eky3XHm1eQIBj5Lpxuhvl417rU8Mxf7y2GFQFnARf67Dc6WRlpkBRCRYnzNInGo2tAPpKu-pXk4k2bApmDa-CJEnqQjuRT215Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=Uqy5SObH1402aA6f-ZEYaxoADU_-ei6Iv-ecQi0xq_01I-_Hfi6v3dfa8HcXafGIDQexPfkV5UJ36tPcClCfuCy8AwWH8TqeozXXtzZBXnfyaxwgb6kU31SDKAjpgImojhWuVjIV7xwG8c6w04EmN8V_4m1fgZBRkKNUuhtX2_Cbg7PNPVet0QKHwMeBlZ-CF3Blb18BWmEbE3iNuzRbhXWgbUVfh9fmZ3jHMAgBMVNUZ7VqY-w5aXEIihYRKvmG7IZnPRStQ0Bo62sBuVT2N4eflH_mJ4GL23-niCaNGVUm1RZuqE9q8Ll_4i-msz3oYNrULSOYfowDqBQu8zJ9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=Uqy5SObH1402aA6f-ZEYaxoADU_-ei6Iv-ecQi0xq_01I-_Hfi6v3dfa8HcXafGIDQexPfkV5UJ36tPcClCfuCy8AwWH8TqeozXXtzZBXnfyaxwgb6kU31SDKAjpgImojhWuVjIV7xwG8c6w04EmN8V_4m1fgZBRkKNUuhtX2_Cbg7PNPVet0QKHwMeBlZ-CF3Blb18BWmEbE3iNuzRbhXWgbUVfh9fmZ3jHMAgBMVNUZ7VqY-w5aXEIihYRKvmG7IZnPRStQ0Bo62sBuVT2N4eflH_mJ4GL23-niCaNGVUm1RZuqE9q8Ll_4i-msz3oYNrULSOYfowDqBQu8zJ9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=rvIpyGhHJPXrB9cYbUESW3hCp2VQuW1E9CDXr2c0fm6KDJ4dj8wMb40fiZ_m8wpVByeg9nT_0r5UKK9iuqdlgoax3xEFZkBOsv87MoeAtbKg-vBE5Di8LqiYHylX6GC5dL6gwBOe5okzlotzSDCcI2KEsOmZQ3ZkATcnNR3vR4jjwh9xfeFjByzL5SzfT_McNjBr_U584foOi_VTsktrroah2VsGWTc7YkeDXlGv99h-BcdiK5VtbxxutVuLRZy1-kBXe5xJpEwSn1msmhtnzbRvKutE_REQnARyGODHhm1lACkzujHChu4zybl0MX2YGPYV93O3fXG2CpY--60XkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=rvIpyGhHJPXrB9cYbUESW3hCp2VQuW1E9CDXr2c0fm6KDJ4dj8wMb40fiZ_m8wpVByeg9nT_0r5UKK9iuqdlgoax3xEFZkBOsv87MoeAtbKg-vBE5Di8LqiYHylX6GC5dL6gwBOe5okzlotzSDCcI2KEsOmZQ3ZkATcnNR3vR4jjwh9xfeFjByzL5SzfT_McNjBr_U584foOi_VTsktrroah2VsGWTc7YkeDXlGv99h-BcdiK5VtbxxutVuLRZy1-kBXe5xJpEwSn1msmhtnzbRvKutE_REQnARyGODHhm1lACkzujHChu4zybl0MX2YGPYV93O3fXG2CpY--60XkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=CGg2wqp0ftNl6kGrAnHcRl4LLA-704mM4Lyeu-uf3yt4VSrsA-oPxASme3uS67R5Cet1yzP3F9Jb1XAZcO5D6f3Oog86mlJpZ8VbqtfOWJl6w4-IorqDLAeqnC0Ld0UK9xIUJFFNXVmU_OCpHxUaRwdKBLPCN4FEbLiNIwdaU9Az8Ehe6rA9YVYod0e13yey7I-s7quZh2s0uQ21SbCX6OC7wM90Rt18x-IJ80mXoowv9_A-vr5ft6xisJkOYCBl8wPYQpW34IeWHuZlWMDdwltzU_RqBY6lG6uedNeJQX6Y1qQmvdOHjlRiwBuvCizKar0-tUq-2PNP3YQZFUgcng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=CGg2wqp0ftNl6kGrAnHcRl4LLA-704mM4Lyeu-uf3yt4VSrsA-oPxASme3uS67R5Cet1yzP3F9Jb1XAZcO5D6f3Oog86mlJpZ8VbqtfOWJl6w4-IorqDLAeqnC0Ld0UK9xIUJFFNXVmU_OCpHxUaRwdKBLPCN4FEbLiNIwdaU9Az8Ehe6rA9YVYod0e13yey7I-s7quZh2s0uQ21SbCX6OC7wM90Rt18x-IJ80mXoowv9_A-vr5ft6xisJkOYCBl8wPYQpW34IeWHuZlWMDdwltzU_RqBY6lG6uedNeJQX6Y1qQmvdOHjlRiwBuvCizKar0-tUq-2PNP3YQZFUgcng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=L19fQsdVhzolWBFFZsmY2y-7-ui7Hh2eERkVpGo8NVpc-EJKStogFnuzkSeuCM8q0A5kN757W4o8cgCrg5VhCyNhlCLMrsCjGkJQsmPEEQL2UNedgKlGN3akrVDxLGXar9nRfiP6izRmd5gl9vWKGthaRCoq-iq2k8iMUez5U0-0fe3JpPzbf4lTJfoxf02bSe4okRhMfEHwXXtiVDHiWpsgUNwRItjHf_6JI2X8l8U9ec9tzAZuIhPaTGkTRVFUSkwXeZLFMKlRUQEHZhjaggCWYohmx1ysTuOcJbeiverRvsErpzwhhCbaePqDseVIn2Eo19ik6yeYk9su5-_Teg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=L19fQsdVhzolWBFFZsmY2y-7-ui7Hh2eERkVpGo8NVpc-EJKStogFnuzkSeuCM8q0A5kN757W4o8cgCrg5VhCyNhlCLMrsCjGkJQsmPEEQL2UNedgKlGN3akrVDxLGXar9nRfiP6izRmd5gl9vWKGthaRCoq-iq2k8iMUez5U0-0fe3JpPzbf4lTJfoxf02bSe4okRhMfEHwXXtiVDHiWpsgUNwRItjHf_6JI2X8l8U9ec9tzAZuIhPaTGkTRVFUSkwXeZLFMKlRUQEHZhjaggCWYohmx1ysTuOcJbeiverRvsErpzwhhCbaePqDseVIn2Eo19ik6yeYk9su5-_Teg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1FnA3LcPf6SlbrvegPtnmSiUOShymJNM4fWYASi3W1BwzP0TEmfnXDmdr25cPog09iteUHe2HjZ-WDKHyNSzbAYkTs5Sive2yA_nu5PPb8c4z0xihK4tOdVOZ6PDkCzVTgbaVTIUC365U2ooAOFpTfSoGXNGfLkBwsYRX8j3L6E2uv-qOO9E8EShd4IOqm98T45ec99q3YMqiLX_dZsi2dXQZhwofoHvBJUzYPs-RZ-ujOwSNLT84TBrIXysCUh-mgZFfWFMaRFGZuCZ6NAfa7j7ZwVuLQeUJFRzzIsTYZFos-BQHVo7G8fgzJtJsAaX9ZJymWVNfOTApEeGYcnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_Kdy6i8BSff5fT4RyLReoG7htpxohMGmhMyxSZkc106Hn10GHIhggqqhq6VJqvJQe0fqtbrR1GCw4nVg5lIig5ALnDZ-CfN64wpCnp6DQu7vGhthSchP9Lugll_xhni03NXAiaZLmJclfQlwwf6YbGumemLewlWTBaAi-SaXYR-9qgosF-MFlDN9JtQj7Y2XrzTYkGCm3I8FP5cHZTZkXuJhELUgKg-HIPv05vLgRwZwjV4crxpXbX0TYw1p2InQfxUxkCXbU1oPR3CVXKfoSzlglGY3iuGYbi_fCFwun6AEZkXNjQ8mSdfOMReSdri6vfW-1t3Wi7kieAmaWY_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIXCqVRUFuInDdEsTVOrLDpj3h6tKhAzWv38aUmgOX1Bw6kWBvrd2b32WkqHVWE3e_f1xPw5Hp75CDwE_VzjcHwV_Qi6PbDrNJsljgkKAX7-Pc6V_HK0BBiVIXwHKv6nEtdVKNwB4ZfrSZzNZJoTqrvvrvOfAa-0f_7qy1s8BMG4lgkrbWQt5fQg2sJiYwwRwO8mxZKIZbJ309N26pYB4C9QbqXuVkWpBhLkGIBIE1HW2UxAXDuteMG8OHXOfCZKMis2TYTckQMam9Ii4W7OJsricgBsMnwrTDPspJ3v7IZYN4eY3NCCxRGftCi-5mjZMBw_kMpeJKbXB2NiZhOYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pRxGNB1Z-3kot1Qofi583rjd6dus41pPDGY747Jlx5oa31fgYfSqfT2rXuhwjgDPYrFU2gEf888g3aHLW40kKzTgh5eNDXutsY7D8vao-oPmaV7FF-qmBmGKpUPNUBBkcyGn4pDAw3m6oNBvp-x7iedTFWV5l9cFTtOZF-PEyPd2de42B_DXpKnCXTmw4ag4DSrI0BMbhoFwTnFizp9luCsBnVEZcheTeU56EoYaEvi7sovmfJVX9i8EI0WMkat0eCB99LH5qlIRunK89a77YP9hbgjnat-csksrpQfeduud2jZILY9YsuMIaLmdwvJ83xnh0CvcjNafX6aaof7NvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9_17IhChvYI9mmDUCQ5lmdXKUQxzi5tjaDIwsf8Zh_IXYbU8sLaOkEwKpQKA3s9xKJwxVQXOWEo9jkHnEC2pFhLsQHQB8xi1pSlDQL-UMDUwyZQterWL7Hk8IM-X95PfTMVsbhyiEhpRlYs9fiElSlhGl8vnb9hZZghbDhVOFMYFj2EjWbf1PrGgCOxgg87Tb2L2uPYTLlCsfihUGMltkEnUjmeERwZJdSzar52GFqs6IEMywvwzA2PO1LlpgEFXM1Q3bhOakeskNg6ksh6GggreJG9XeJGhHObG4dEooTmJJ_470o8zc9CtAyWN4iLQMzKPBmqWpP4AZwsInRjGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMpcbkIW7N1wrarpVfPSsBHpqubLpK7oLpcEr2bbgmeVx4mEywVGk49pJPTDM8wXcKGHlem5aQno_N1s3TU03mw7bmiw9SjnzpHFpPihijMFu7-RbWUtXK3_fMVbDEQLfhkU286-b-t_ymm0diZepZqaxyuK_DN-m2O6dD_PWwxqiT9Dr30RwWW5ozmoF72ehtKXNETRTmEQ2CdjWZJSJYv8Eqfei28sHv_lERNJ_1HS5-xADHl7YzXY-Vy7AfgHGOyEB95JWUlLR2CjE3JNjabZ8uuxtgm0O9UNBZAbHV4cSYUUxe8edfRpX2dZsP8ChlriSQJcQrO8X5bZHkXE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnBvQKFo21vES2FEtQDUGZLeDvy8HvZE9KbJyYn4-6JVE_ht143Dz3mHnrDA5GnNKM8ayeV1cGE_M60BLUiyLdpUd9m2Ka5n5bK0fMFIxm8UT1qVua_Sz_vOHxvjgSDhUYoZOhDaehYiJt_0BoJDlxLSCV1bMDJOLU9uD4RR8Z2KyXltchj4CRaISI2F2_yZZ9JyhT440KByy8euNfBnCIkWs9XFEP4sCNWksTP-xTPgx7bQS-7gA9clnCHda5l-forM33zlT8QJa7gEN8l6tLzTQMdF1yuOaK80x5g9Y2SRYIdoRfPdcRi9_rmegpcGpUjg9NKg5AlWPFrucxo7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm3kR2jHlI_vJE3N0b3x_7uyNx-1ms0hc4SAEMnL5sTRHHSDtHW6r1Hj01MgXrZeLKSZDXHNKCbSD1J6fPpHh_2SjxsvYhc-Y6hO01qmL6nK8XxvDfZZta82k68lpukVsSkoCfzgtYGuW3PhNRyxvQyXPaf3Jws-Su6I-w6cDvfUa97-vKrPwQ6f6ky4zIczeRqynlnmjFo-A9NsL5-7PcRh-t1bBsQqzihUaayUF1CmDGeHotYJjnKItCmgKtMLuHGi3G95Mo8jNR7QMNikaHK0m6IWxSYB3qyLnS_RdZu0hj6uMvrV0yn4qJqhhq5WgLKZzPTLmNZ02olntUZ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiFWhLkIuumwsAY8CFMRcH20vPmgomcLztEgYCUhPnNNQo4jZMynJVw7xrP0n9Agq5S_ohBe92IRO4Dm9sHCIBxlDMAbyQtjvezcLWQB6YsVha28BpulYzMcTbZHkurZ0-5eQfmf1DkgWf4euVxuwpoRbv8FKB3uGMUqYNSFpp1QfBYyD6HVC3MouM33Tf7gNzTz9N9v_JHRo81deZ6lgup-H9W4WXYi-8InUUyBj2stIGSay-1sVWPTdUl4-wdrFHsWMSx8cOKgyOL3_Kw9HKzDYzw6BEP8cQiMPhyFfHnGGTwMsB6AVZCKtkDnQemCa894cST_Y5ciemIgCuKwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=c3bFW5LZ6uL97NDaT2uiwZT2yr2hJPOp1H46rHq3uqQDNxVayOp69bLdUteuASQ3pVu_tqsM9yeblvhIDs6lReXuRffm2sM2S0eZDMyEk0ZB1Dcl38mWXXIbF-_iWcUACqJ3jfpK1NwiyrAcyP3w1V2RGKKq8OPnqpyWiy1CaH2pbkPqOYXG0yFZFW8J0WJ1x-0xXZ7zhFwxko0MKp9cjkvrYb3UoahFhveMHiQseR4fpwcssuGuNq37wwRQ1O0ChpgGMFqJXSAd6uhineSVhMwTiSrDUO-Eacmqam1R7vy6MOsxHyoMJkQDqMkEoKSi7ifLYhM15YajAgjbFvSyUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=c3bFW5LZ6uL97NDaT2uiwZT2yr2hJPOp1H46rHq3uqQDNxVayOp69bLdUteuASQ3pVu_tqsM9yeblvhIDs6lReXuRffm2sM2S0eZDMyEk0ZB1Dcl38mWXXIbF-_iWcUACqJ3jfpK1NwiyrAcyP3w1V2RGKKq8OPnqpyWiy1CaH2pbkPqOYXG0yFZFW8J0WJ1x-0xXZ7zhFwxko0MKp9cjkvrYb3UoahFhveMHiQseR4fpwcssuGuNq37wwRQ1O0ChpgGMFqJXSAd6uhineSVhMwTiSrDUO-Eacmqam1R7vy6MOsxHyoMJkQDqMkEoKSi7ifLYhM15YajAgjbFvSyUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS9Xs3nDdAHj7uJIPuMV6hn9lI2l5LaPfH9YFxAuh2H_hn-1NXdRrmGRyfyI1XhRLkiz6L9o6Nu3Vs0GnFBSagigG9xy7ghF4zu9xddPSoCZZgLUANTVc1UKsS2eqScWJ_EpfRXjU-0ObJpH2S9QfDFb-KlDCeXfslLBt9dy-dfDF8vRDYViMzgGd9H9TR_p3773F-58ww3uAckpyacInwC9CgeFQYFzPBMiWJbZnXxQ5UQGckoq7OKjcUHpxOm7QTR3sErWE6APE64tcPBmA6-gTi-PTa1sIhqtA7e6eP7EI5qhreDiN4VvXnR_fak18z4LMkiDvhDr1jOyUhdX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEXbXjWKlhCp-s9yIvqOGirfDp12n8jdStszN39h40uXcOsUc9Uy3AlCKRy65976jtdUjiC8jdrqhkX2KWxbG-TswdPpyHkKj5f0zuUEBdjNlWhdoBJuqI8YJ5oMV3QoK6tIAwrraAZ2y7-nZnrmxc3p9QryEkGzNZ0RTXxThA8GfeDmGoL9P2PE64X39xcuACbziVkqo70Lr3YoPaJL9xIGPaFIlb7QWrAk9g6BcQyO0zbmAYXkOQ2tz-u1rAQ-fFoSvcmuvPTG-wBxXFwTnJjnEBfyIDPPer342jFPrSj4M8VhEt2lR0bKi_qci-4GWv-Zp0WlXHFzYBV2890Amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICPryZPkiK-iLvmjj6RnsSFs3oiosnRQDMvE9X-yqdxrRhLb3c-nZ2Mxo_SG_JmXVO7vZX54VOeaH9Jk6loUpiSesSoOwcc8PbSbS_I3n87lnwxNglU2BfDQbPUUucMePyDD3TOhYFDPihpEvuGQq_0UXZ4ePb9gY1-HjMueb4vNYW1v0HeU5rpHMtsexQm9qPpDmOTEw0eZ_9uw2Rl_S5zwDtr1HRQZaH--aAUKzPojC_s9Tu1BZAAyH6eXwW39ZwFkYI-JWDX8MNKngZ2JcK1-wQnTiOY6gQcy_vizJr3bhqrwEbLJHel8At9ZRoCTgDbqGbJqsPrV6LON6Lrxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LinCVbW4jiy-9aa0gSJkcbHl4Ew0YhsznQlCbLrOs3ot_uApjaYEe-TTEVWJPyznde4PkmBUVHg-tXL_aYeLsllprOYWJPbG6lNi922h1JUhay32F9PWexLK9sOuFyZsSWtep4K2wgOJ1XtCBYVhexpAiu5O09dC7uwrTnvRCiividIcZRnn2WzAq5eV4Nkz6GGanggEpo78nWl1jvWZY4Z4LqATIo_RSE2Yzb7k8pkICnvmaJ2vB2z0Sa97gvhzYCR_bD3axzFsUyAJY33SgJgayXjvFvHWCgxofSvrfRQbcR1ZsHvD8pz8zvVyh0D6FjUaJBji3UMDBJC_rbUS1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=BnVFn95SdQm5TOLYEHq0yjrQBILix8ZmO3GoOgV6Fp8AwemkkYVxslDF9bHXgGJ6igqr59JheTfqaVw56d4AOxgtewg-9RRQkVRPIC2FYtQVEiFmQP8AuMwrIHwWnDgUgDq2Kfd97sltk1jYt5iB7Oo6VD0Ltp4q119HlAah-7uZe5R7zx4d33JGcxjHTwHRvC2xJCgbzVox1qstGHiE5KuPpRcAeMM7rc4UIORsp0zimsfc6mDGSiHLbceZzAlgTr1vSEaQX8N_AkQa_jsVnnMUKoca6oNnGlMrVK3ZdCozMo9RzKf1P6r5T7xGRBnVMnz0NyBMz0GqopIMnCn1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=BnVFn95SdQm5TOLYEHq0yjrQBILix8ZmO3GoOgV6Fp8AwemkkYVxslDF9bHXgGJ6igqr59JheTfqaVw56d4AOxgtewg-9RRQkVRPIC2FYtQVEiFmQP8AuMwrIHwWnDgUgDq2Kfd97sltk1jYt5iB7Oo6VD0Ltp4q119HlAah-7uZe5R7zx4d33JGcxjHTwHRvC2xJCgbzVox1qstGHiE5KuPpRcAeMM7rc4UIORsp0zimsfc6mDGSiHLbceZzAlgTr1vSEaQX8N_AkQa_jsVnnMUKoca6oNnGlMrVK3ZdCozMo9RzKf1P6r5T7xGRBnVMnz0NyBMz0GqopIMnCn1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvSSIvaOLVHAKmV68gd1N_cM3Cluwviidui7bMCXFOfVXmzyWL_AkfZtW0aHWJ27kUSvC9ryivbHTsY4gVd4n-gIlbGMF5fFzDmkL-Piw-RWj0oosrKkyg1xTG4QNkNH7l2ym47Wi1DfkfV2Rhpdiv2Gf3OyDkVvU2FFvhXCsJClcwLotpNV06U2OeyI5vBGnnNiNN1xIgaXssEoyySMOsKR_ede89pH-RIszr2TruV80kjRgWFDFJYD7YnqbM2ESDpmzVltY5iXoFgWthWXTvIzc1GEnLLEtEELsBgJ_PHChluAAxaiMmxm3q4Y2Vfuz74pdD5E0I_YyMe8pxHHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=jDyD9G-600QIdNOmcp8z3BQugTJ7t7hZ6-4LmlYNq_PzZajfZ2S8fxtxRNZSKBt0XInwepEi4fmQyQNY2-yEWa48IieiJbJgDL2_dedOEl-330n_ZGHuTu_0ZO1e5kgs94cXOm2KukuQ2GnY3XXe1RAJcs2M8Mpny0l4P8IelFZv2ZFfDW_ah0rE9mMkAjTkp1mlFgExZjYm6X35YeypxKrqTjcttQIWLDCGbqwRZ84-7ILKEoBLwAZGXUEymvuK8_V7XU83KMGa0o5GK6gz8MziwVuDvV6VXC5UpYCrzJHCju-UCKSCHG7hr2-lwacmicN4ppCFrLK3ujJNf78bUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=jDyD9G-600QIdNOmcp8z3BQugTJ7t7hZ6-4LmlYNq_PzZajfZ2S8fxtxRNZSKBt0XInwepEi4fmQyQNY2-yEWa48IieiJbJgDL2_dedOEl-330n_ZGHuTu_0ZO1e5kgs94cXOm2KukuQ2GnY3XXe1RAJcs2M8Mpny0l4P8IelFZv2ZFfDW_ah0rE9mMkAjTkp1mlFgExZjYm6X35YeypxKrqTjcttQIWLDCGbqwRZ84-7ILKEoBLwAZGXUEymvuK8_V7XU83KMGa0o5GK6gz8MziwVuDvV6VXC5UpYCrzJHCju-UCKSCHG7hr2-lwacmicN4ppCFrLK3ujJNf78bUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEuFGLETQf7AzRtmDuSVSv3xvg4fT7kvSghA2pCbi3qB2v8V8tVlaWScOoKwLb37dkJuqANiTPqG_5bMPENWN0sZZVRnEJ6fHvlXQ_YoZE7v7JBVMC4dzmQ8ImBVxLV6ao6RphBc6KQPEJwmfi7_Xb-qMwquDVVhj1ML-eVU7a7fmwMdx3yXA0FN0lB7wo74ADnwSYMPJAnawBZ3jGce1a1p_cr0kiTKYNM_yYxJ_TfL1QHPoPpSW5vZ9LU2G0-Mcv4wKBnmIY7QeeYTrLHxuGZFnuo6-ddg_dq17uRCtc8ZBoCZDd1vq7G4J1BBOuk9x14wrd73c5l6BeQ4ln4iwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=dl492TBO-IHWcCq6o2YPzQ0AKIW7KlfL72IJOPN-Ojl-bxtqp_iKDPt5V9475DO0is3Gb0oXhi0Ka98eEVEgjCPlyVZ0aixf4nnil-V-548S-MJARextLdvM6xK_k7xUZDuSjsi_b_zubixT-wwjyKFEKHzeX6z98XAb_vIvh3d3iZ3Jruu5qbgLTk_yJ79xiY3eEr3SNSnPwL6uyCc-k-fYal6F7Rg0rW0ZHuO_89mhFk8YSZv9FaYQEJos-fs01Ber4lx5-rQ0yzQ4gmCQxSTN-9oxECLnnekaNP_ZiuRGFlCzbrnRw1irg08Y5Lr8IVt10Wn4uPUFPExvTlMHtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=dl492TBO-IHWcCq6o2YPzQ0AKIW7KlfL72IJOPN-Ojl-bxtqp_iKDPt5V9475DO0is3Gb0oXhi0Ka98eEVEgjCPlyVZ0aixf4nnil-V-548S-MJARextLdvM6xK_k7xUZDuSjsi_b_zubixT-wwjyKFEKHzeX6z98XAb_vIvh3d3iZ3Jruu5qbgLTk_yJ79xiY3eEr3SNSnPwL6uyCc-k-fYal6F7Rg0rW0ZHuO_89mhFk8YSZv9FaYQEJos-fs01Ber4lx5-rQ0yzQ4gmCQxSTN-9oxECLnnekaNP_ZiuRGFlCzbrnRw1irg08Y5Lr8IVt10Wn4uPUFPExvTlMHtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=mt-L0FsJrQ2SPUdlA4AkyFbx-OIZaRsGlvwexkTZbFgjEQPNP_HHl5Yiyo9eV_zSyRkVFGbIQTisrdI5uocOhxfbPfYaMHdcfegQ_lM5R1fNubAX-alnNTC4rLxnVk_KhjismVTAVZKojvypmnlPJ_eNZjQxa2ZtBa2rcAGabY9kK64v26eXpIfh6nGNEgGOk1RnggdVZb9jJ7nNuzQfqhN9y2eFm4phF-OmugCa_3WV7oALlPOa-PZpDdt-owZaY4M6hZyVbkZF7vU2pGyduDyjB3rQikJuxcYXyXhbSJ44tViQOe-w_aXCydJd6PWDQB0a3QeFVcYrcYem9JyeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=mt-L0FsJrQ2SPUdlA4AkyFbx-OIZaRsGlvwexkTZbFgjEQPNP_HHl5Yiyo9eV_zSyRkVFGbIQTisrdI5uocOhxfbPfYaMHdcfegQ_lM5R1fNubAX-alnNTC4rLxnVk_KhjismVTAVZKojvypmnlPJ_eNZjQxa2ZtBa2rcAGabY9kK64v26eXpIfh6nGNEgGOk1RnggdVZb9jJ7nNuzQfqhN9y2eFm4phF-OmugCa_3WV7oALlPOa-PZpDdt-owZaY4M6hZyVbkZF7vU2pGyduDyjB3rQikJuxcYXyXhbSJ44tViQOe-w_aXCydJd6PWDQB0a3QeFVcYrcYem9JyeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=HqlPhc--wMpqgLV9Gla7ekOydKXhovvk58yvp0lU0Z7ne7ZoYKG-9OONLRJDFfHPOz1lBMpryeu3yJTzaf0EnVjcBmzESji29OJFev1I9fWmA1lDJg7AScbv0Sb1Vxikv5rq9COYcDVCbjyxcoub3zE7WpKpZ0InVjVzk-hfV4k2LLzsM9S2j4PwxQDMyH_3u50tAXGDmQzPH2bhmFhTu1qFzAXvtZcsF9tqb6WYghJZVoJh1WzDRk2pg68Tp9rCvY79MB6IL7Zx4LFqQDpQedE8d2tvfcWMGuSm-HmIa-kANwIHijTuefZ0s3dKxmD3IsMC2WLpSaCPcVoR_Gimaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=HqlPhc--wMpqgLV9Gla7ekOydKXhovvk58yvp0lU0Z7ne7ZoYKG-9OONLRJDFfHPOz1lBMpryeu3yJTzaf0EnVjcBmzESji29OJFev1I9fWmA1lDJg7AScbv0Sb1Vxikv5rq9COYcDVCbjyxcoub3zE7WpKpZ0InVjVzk-hfV4k2LLzsM9S2j4PwxQDMyH_3u50tAXGDmQzPH2bhmFhTu1qFzAXvtZcsF9tqb6WYghJZVoJh1WzDRk2pg68Tp9rCvY79MB6IL7Zx4LFqQDpQedE8d2tvfcWMGuSm-HmIa-kANwIHijTuefZ0s3dKxmD3IsMC2WLpSaCPcVoR_Gimaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ct-TK4raxxNioDYoj6nS6ACuyXsH-hUfMjgIffXkLoNj2-ddG1m3LT09Da3gt_PlHmRZIgwFpTPGqAVuDRkawXCLvH5UmmVJg5WesJvf4Ry2JntHe8G5P819xHGtncuQx0TPjc6aes6KuRWKeIhs5NPCFq1DT7oVwTzXCBCwGfLo28MnhFg_ClJomJmxXR6zsxzyODOs_U0zxY_-FzXmZCBIOd3jSlHW_u63o8kjRc7Zvc67ew5RVkiruoj8fnPU1cqvGLmgBemRKPqierUMpE-1jB5dfBcQoOrswPpgWVgnX6yqXidmpfddP_-XVFudj7X6HUJm3cZ6lfQcMphvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V05vn7KILAMiXe-LKrxLioRwD24WeiuILqJkm-2Kd3_0gyARFALF5kUywkm9VkZji82Bya3ndCwoI2TLBpTlXzxmv9NBQ73a8lGF_cWVt_zjAMPxsq4WAMSXqpmgqChcPSUft_2KgkXTAPLrJdPjodBmjYG0iBy6WqbHkhEoy32OqChMl1kkTFeTspcvAbizyqWGUgefbc46e5WiWE3_Poy-vq5zqksKcxr8-_vE_all_rHoWG6VUqDdNPpGbrn61V1Fo0hHx3RAF5pED8kbXEUUOAduT7VUJoyY_DOMluvnEOcjwJ67nwEgHSD0Wae2_EjnfhQFVcuUfNS18jIx5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=pk9iwgf_EjRu-9PC7j47rjBRJlnW3e_hurNp_o69-_XfM8i6AEx8gms3c0IZeLeJ_3xuHEpWgOkJ1m5jK0Z5QhY6e9cS5ckFZkzY18Hc_KtLaabr1Tw8tV8O419PA_m2ydC2igwsjmUQjBzm-Bj-syPjlgogGuJRgaj1JPge-o15JznMxJrAX2s0gTyenOPajxqGhFFsYDVWIlesvTNPR_ggdN7iN6ndL5PcBwPtkVxtNiuAfMay2Y1Gn51F3SyXXISRzN_0acaMMPIzwOLULieA9XGWsEcTb6g_IX8wRTcNKT5DDktUv16aMoFx_1iJgjpJUn4rMVwYdlBd1A4tSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=pk9iwgf_EjRu-9PC7j47rjBRJlnW3e_hurNp_o69-_XfM8i6AEx8gms3c0IZeLeJ_3xuHEpWgOkJ1m5jK0Z5QhY6e9cS5ckFZkzY18Hc_KtLaabr1Tw8tV8O419PA_m2ydC2igwsjmUQjBzm-Bj-syPjlgogGuJRgaj1JPge-o15JznMxJrAX2s0gTyenOPajxqGhFFsYDVWIlesvTNPR_ggdN7iN6ndL5PcBwPtkVxtNiuAfMay2Y1Gn51F3SyXXISRzN_0acaMMPIzwOLULieA9XGWsEcTb6g_IX8wRTcNKT5DDktUv16aMoFx_1iJgjpJUn4rMVwYdlBd1A4tSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=c8d-jQn_nxZYbMN72ZCbqJablqpKanOPAWKovLb9Rri6W-374sxXO_6YT0YzFVIDWdqm6DGJ35M10aiKvprGlccVTfv6PdIA6-rBfFdxOTo0HpxLszAtf7_nxaLYVwo613ml8HG1Mz3s5Kj7h-1qaw3EYW4UuWDZM7lFzkeHn34W6ug7aU0VKzA4b7uOIEo2sxLCiiN73FJ9UWjehpEn8yVWuPaK4nHthx-pOuk3eu7xYhYJm4ieptB8w5oEkeeil-mpLniWC5s3ujf0XJt2hxNbbiGi123wWsymrs347QItOsnARH1aPUM6bcSsrKfPCvdYoNGIy9TnrTsQeon5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=c8d-jQn_nxZYbMN72ZCbqJablqpKanOPAWKovLb9Rri6W-374sxXO_6YT0YzFVIDWdqm6DGJ35M10aiKvprGlccVTfv6PdIA6-rBfFdxOTo0HpxLszAtf7_nxaLYVwo613ml8HG1Mz3s5Kj7h-1qaw3EYW4UuWDZM7lFzkeHn34W6ug7aU0VKzA4b7uOIEo2sxLCiiN73FJ9UWjehpEn8yVWuPaK4nHthx-pOuk3eu7xYhYJm4ieptB8w5oEkeeil-mpLniWC5s3ujf0XJt2hxNbbiGi123wWsymrs347QItOsnARH1aPUM6bcSsrKfPCvdYoNGIy9TnrTsQeon5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HquEAiSoR7A-Dvt9GmIIhnrdB37JtBFLCGPiIyZbr3YZDw3E_P16jqaCgmZPX7sQ_XSUGi3oVDVzWC296NAbUpwnn9AbIvISZ1RhiH-z3zkVf_VkezepfE1zNX6_rf3f9ocydZikITDo3gVjpYnZro-xNjRPYQczZFjrfnu4aZzqimURbjty6VAqhXA1YxxyrWd2Dme6ordbClvGJtV0YUcWaB0ZEMr0l1G5R5wpAjzOP7enUUAXzLwPt6jsPaYNk980Uil71XOkpeADZTLVmtdlFVfkoOoeEc_R7fOQ7gDhSYrDwpLYmvd8bLqzOHtvKx_zoc3aBUbzAicmPAIw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmnktwklZiHGd5G0JBZ1eDHOu8mXb5PyjNvdYvcbLy4XNSWKthyUQXMMxPySclgAByRQyGfZVe_4k1F9EjPEgfNfQESZqpti72kNdOD27dEuFR8q_mMN053S0B1GlzVTNRcbptU68RgMwQfjltzD-malECHd2YnZlJse-I32q6pvXdc7ivl1NUNBDN8CVOdAvyW-iPLde-x2pBKIH6PHiD6btlki2B5Qbhd01jmOBvEX7Zhs2Fr4HfrSsUxk1WYqgpkSddW92SdbymdlYQ5cIrMr8SGZQIpYxyBoKSxFsnifATfzPJEbfg2mN_8D6dyhkUZ_yU_Y-QFujD4I2l7L7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPCoUNXd56gOqq19Zx2yUF2a8exgBfY5xvRlnBIJqmNi81GESnW43NP_OmbuljYXsOtkSeAId_epOQHbcNBXBxxHLefby_I9NXJKSmZdKZKbZo5wjVjRyiOhXx3d4eXNO3DX9BtiUASM5KxsUo2-lPO7RoL4RWdDylTVq0A1ZGide_vCKiOwvZukQRgMnX6OhR5tg47A8FpLXEPAJzNBqAFQTWc1f-5uVcexx-Q4cNfm7mHLVZsh0-wyJD2Q6ae4rTUgkCMsN4veBI5mRB76uQ5j7C1yQkOcOxrrvPvcTMiw5_XfWhdxrpdN3whQR9yW7gpBzIjOpghKApieWDoxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoJnfAodwwBkBh_UkXXcL_RY_lCB5QuoqOqoKu9Tm9xX8iw-NQq1aJ_VYEmtnQ-7AFw3NyiTKKqN-W32sjPO-NrSm_buQOuh1gL3g1jcFCg9iD7VCbVtTz7fJPMCu5cj8Ziku9y135D45lWZHIqeNQFCv6NQJXArcw9wzDeDjv30EPBAIzsXC2hHsLbm1yHGp9QFsnAiVGocuBVibGYartU72lnSE2Ja4601e4Yaf8zJwh4qdoMRZJoTvmu6UDWFTZnvZelc-jiNmzy0aZQpF1HOMdZU5S91Zvw32K_kL1yJfwKvP-BqgTf8xmXUjsEqV3KjhSH5CaRxZ67Tua3G0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G32vrstVktu6tMxA62UhgpLsDVdtednduOzRyyxpIYldw4CoZlM5FlXqPYk08WfXQwS3m0NYjuaGFZ5CPttX8Lx00K2G5-d6WwoXKdPdurpkRDklTj41ERKXAsz_pEJm4ujyPiP5hG0QjKyBC5HL8mfogQnuBNUAE343AMdzKtXp4DJb1gMV1P462YX813mF7YBUMso0XaaB68XczhGvaAQtPUsbdKvKoywomHz4I6egBWe1jxbC_1Hz3fZf4yJREQEODSyO6p7tnFOVyCzjoC2ZbBCiZNAy7Eqzp0I-p8ctRxi6GK7KyASNKIMovGtzXv1XvV9UXwxEap708g9fMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhHULdfi1ydq8T-9QwzBv4osKgeMy898c4Gqg5OXZQnI2kTHcaTWVAFGD2QknJjgrKAiGjTtbv1STLE0hVJX5r_EldsflnmBNi5BdKhTy-08Dg5maQz546ydnONMKcReMRVUQBr43J2mtA2bnmuFgluSovhA-xJwpDa1GyQ8iJtUC9hTZGFTxPZs9u-2XF6mgY1QzZtRNhYVPyOH60ftxb8rPByEv4d6NdMTKluXEK3Rwhj8FPn5L-coQdvUM22qBeDivPM5VBs2sd-0cG29l3bBQ_SOHSObghZM290aH7udeNM3cT6uLSp8h3gKBF9Iok_rEpKCF2M3xxN-KHszGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vNyV5ycu9T6jXozUrFu3am6i6MgGX8aZMFcQZ-05nAGFtJWq34hRjjyr2RupJMXeBe-86FPUdnfoDho7Ux7ggDWtiKR7KunEJQoqgGonOopr1HN7O6-AqxKDnZYIdf9AvjEQQEz7FEOZkhQ9LUbWVaCJT2s3bjJjrQIrdubsqEGY_3A3lxDuS9qmyNya8NlhdnyapM3BOy86ZN9PuJMpHrD4B4RgNEmi-vAypad-5-pUEB-LY7OSVcfMUrgjaHQuHIsORckEP924G6E0zVfkX0QED5_jToA38yuOTejLuKLX5zFdhNeOiykuw36XlUCWZqcZeX3GqDba2MhPg_XZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vNyV5ycu9T6jXozUrFu3am6i6MgGX8aZMFcQZ-05nAGFtJWq34hRjjyr2RupJMXeBe-86FPUdnfoDho7Ux7ggDWtiKR7KunEJQoqgGonOopr1HN7O6-AqxKDnZYIdf9AvjEQQEz7FEOZkhQ9LUbWVaCJT2s3bjJjrQIrdubsqEGY_3A3lxDuS9qmyNya8NlhdnyapM3BOy86ZN9PuJMpHrD4B4RgNEmi-vAypad-5-pUEB-LY7OSVcfMUrgjaHQuHIsORckEP924G6E0zVfkX0QED5_jToA38yuOTejLuKLX5zFdhNeOiykuw36XlUCWZqcZeX3GqDba2MhPg_XZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQPsieoUIzycq0Y2eSYFpQ9PqpuNpFkC0KdeRAsGllRUztayJ_Uw4LBGizxRLqSaaDFN0oNxXSh7kKngvkaprlBApViJxr2qWYRC_mEWfWExwZ0_6keINhRm6HXzDANSe5_XwNuYUpJClT_oPX1u0jLZz8ZRXuuN09gD1KdmFI3HNTTZOty2k97ye8EjFHS6zjFAQ2OQYbbTG-lnoEAf8hGb0p6KWm8NrLDPpfAgFfAvJHf5CRKkFh4Bt6rjNOKitnHjXjV01_ta8BSrNmyALXP-F--YWxtgBPoPG-p2hG2J8hXZofv0L0GFUhRll_RD8ocRgytE2S-L5FK4ehMqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNJ-wcVtRX_bYX2tgnc_bmmYYeoHVWaO9Ds_3pENj9qQRey9CaepyaugL9NKhPXeOYNIVLPIz-Oi3buJ7V2seWQ7xva9nzZ0Wl1onLlG0E_JNGSX_LGhaA9yRSjpz2bFcP1vKYM9Q7umdVWF2iPv26zdX5jy5Vk78N4tjz6qPpPw1qNKR9WBXfkheMAqRpru5cbCzbKKKEJmDLYNQeWeDW7Ho6DgqyAP9g3o5iSUXoFiBvyTZd0eR0cYrOZaflY2M9OAMmhEwhYNuMgl-ogFcYmM0BsR3Ret0-sYAz5IOozdTOAVPeDz1Q56ZeNx2mvtCUorcFy4YvFWC4NJ3yJiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
