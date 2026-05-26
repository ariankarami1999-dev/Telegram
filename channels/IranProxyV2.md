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
<img src="https://cdn4.telesco.pe/file/et1gtQISz72pKtT7VhEx2934eZkRn91129GfMv2PgI5nqiVUuPrWA1vp5n-uu7PJrASxwUQKgH8oV9ldQDqNtXqP-DQSVrZU7b1bJ1mkQIwe0fNe7upV5qv32V2UGDA9b3Y5JdhKxDyMpMHkhaNPRDF3GvK3qEeA4mLUoZxQakgKlafnumaEQQMV6wM6Ttoq87S5F5Qy39-u4Jb0CcTn-zyAGBnWogeSBJVS3ypXi2EAhU0qttw04iHHPXGoNaAKNuLtEsMcMhkx5s2wxg-yYp_9ycnnlbmO7QgbkY_BOGnbw4XkAV7sq7w3dfc7Ctl5L_60jd9-jSwKbJCmk5wYJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.9K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-8555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/IranProxyV2/8555" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH-zRRtRhqrYk6hZENDMi6apS3ABLkdXjfcwGZj0F2QYqkTtg9rVzgMq76-q0y2apEz_83VMakSqqcwtcfmkZZZoP3-Fxr36qIMWFmOyV0YrDZfFDQb96vs_co5YqPOPLY4koA3abloOB7MD_XGybSyyEmBXBapkyNL-yS9Xv2h0nG7jCIjBbjAwoi8WmESto15UZDUlXCVp95-MDThpBrjJ170a1mJgVxJUCS1VtJamnLtebrZtK_PhiKUM5yEBM-3U0KB45-rIG9-jXOc8zdK-q01xjuwUKgxsvROejcJB8kLQK67DFnj_0-Sg5WbiFEdtyfCMW_hrbVbO_tfIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/IranProxyV2/8554" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8553" target="_blank">📅 00:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
https://t.me/proxy?server=178.105.241.184&port=443&secret=99902e5742bd34a3f26434fadf88cde3
سرور وارد کنید، و بعد به پروکسی متصل بشید بصورت ترکیبی، رو همه اپراتور ها اوکیه، فور کنید دوستاتونم استفاده کنن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8552" target="_blank">📅 00:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📣
دوستان، سرعت جوریه که نت قطع بود، سرعت بهتر بود
😐
😂
📌
درضمن، اینکه سرعت سرورهای تانل ربات پایینه نگران نباشید، برای همه به همین صورته و اختلاله کلا تو کل کشور ، حل میشه ، ولی خب پایداره و وصله، خواستین تهیه کنید تو ربات سفارشتونو ثبت کنید
🏅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8551" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8550" target="_blank">📅 23:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">vless://b64ced11-143e-4ded-a985-a8de25461061@3.27.234.120:51808?security=reality&encryption=none&pbk=XHnwfyEySdx57QT_8P_7vDVFzdLHO4tO9BQOsHxxlEk&headerType=none&fp=firefox&type=tcp&flow=xtls-rprx-vision&sni=yahoo.com&sid=8810c789eea55c28#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل به همه اپراتور ها، بفرستین واسه دوستاتون هم اونا وصل شن، هم از ما حمایت ریزی بشه
❤️
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8549" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">vless://28154b7e-afc2-449b-8a78-bf1eba31bd05@a.darafiq.ir:8880?path=%2F&security=none&encryption=none&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل با همه اپراتور ها، فور نکنید حمایت نشه حلال نیستا
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8548" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۲ تا کانفیگ دیگ هم ساختم، رو یکی نباشین مختلف بزنید که سرعتشون نیاد پایین یا قطع نشن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8547" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">vless://abe09a99-7346-4c5b-9476-16774c032ae7@104.16.89.120:443?path=%2FTelegram-%40IranianMinds&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=1&fp=chrome&type=ws&allowInsecure=1&sni=mcia.po2pco.top#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رایگان جدید رو همه اپراتور ها وصله، استفاده کنید بزنید، فور کنید برای دوستاتون چنلو داشته باشن، حمایتتتت
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8546" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8545" target="_blank">📅 22:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8544" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=nt8c8X6NZY018NLVdVPoxjPzn2QhBGAwuMd0mk_9KR_gti_lpVeZtc5p1U4EOfHYeuQYneBq8x5Fwhx5G-f4GCyu9QD2JNoqD0yR_gYpeWcWzexlt3fWI2ZBzn9Q11SI9KXYIcymzapPNU0TR9dwMhF2SFOLXgotKnbjnE15gqhO-MCwzSVPIwzYju2_REDfzw2BU-8XF8C5RQ1amchhB1Pqzi7bWj7ToIlBL5JB06ZO0pg74aIyviqhsD2PZz7tVjrAATPw-e51RzIQV1i29A_D1b_k8MmYKce_nRAJg8BzFSh6QDVc08CThrTlx0Swy7yroTstt4Ryc3TU7VO3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=nt8c8X6NZY018NLVdVPoxjPzn2QhBGAwuMd0mk_9KR_gti_lpVeZtc5p1U4EOfHYeuQYneBq8x5Fwhx5G-f4GCyu9QD2JNoqD0yR_gYpeWcWzexlt3fWI2ZBzn9Q11SI9KXYIcymzapPNU0TR9dwMhF2SFOLXgotKnbjnE15gqhO-MCwzSVPIwzYju2_REDfzw2BU-8XF8C5RQ1amchhB1Pqzi7bWj7ToIlBL5JB06ZO0pg74aIyviqhsD2PZz7tVjrAATPw-e51RzIQV1i29A_D1b_k8MmYKce_nRAJg8BzFSh6QDVc08CThrTlx0Swy7yroTstt4Ryc3TU7VO3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ، خداحافظ
👋
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8543" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید، خوشتون اومد فور کنید
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8542" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?path=%2F&security=tls&encryption=none&insecure=1&host=sni.111000.indevs.in&type=ws&allowInsecure=1&sni=sni.111000.indevs.in#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
کانفیگ با پورت های متفاوت براتون میسازم، سعی کنید همرو تست کنید، ببینید با کدوم راحت تر هستین، حتما برای دوستاتونم بفرستید
✅
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8541" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@104.16.7.70:443?mode=stream-one&path=%2Fde&security=tls&encryption=none&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=de.xn--q9jyb4c.online#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
چند ثانیه صبرکنید وصل بشه، هنوز پهنای باند اونقدری زیاد نیست که پرسرعت وصل بشه، یادتون نره فور کنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8540" target="_blank">📅 20:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">vless://8b84b146-3405-44f2-98e4-f0ac7dbad0c0@104.17.147.22:80?mode=auto&path=%2FTelegram%40SoonTeam&security=none&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=uk.im-eb.cc.&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
سرعت عالی، رو همه اپراتورها، بفرستید واسه دوستاتون وصل بشن، حجم نامحدودههههه
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8539" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همه اپراتور ها متصله، وصل شین لذت ببرید
✅
حجمممم نامحدودددد
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8538" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@172.64.152.23:443?path=%2F222.167.202.31%3A7443&security=tls&encryption=none&insecure=1&host=2026.hhhhh.eu.org&type=ws&allowInsecure=1&sni=2026.hhhhh.eu.org#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو تمامی اپراتور و نت های همراه وصله
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8537" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👑
اینترنت ایرانسل و همراه اوکی شد و باید فیلترشکن های رایگان برایتون وصل شده باشه
❤️
🛜
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8536" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول متصله
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8535" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
اینترنت بین الملل روی خطوط همراه اول هم وصل شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8534" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانفیگ رایگان برای وایفا
✅
vless://4493268e-2083-4a18-9c24-72c1f8f604d5@92.42.203.168:443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=dl-server1.tpchat.ir&fp=chrome&type=ws&allowInsecure=0&sni=dl-server1.tpchat.ir#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8533" target="_blank">📅 20:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8532" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8531" target="_blank">📅 20:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پروکسی وصل
✅
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8530" target="_blank">📅 19:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">vless://fe23b0d9-ab91-4f7b-a5a4-89e4ae9b094e@www.speedtest.net:443?security=tls&sni=broken-mud-0a9a.rigacihir69.workers.dev&alpn=http/1.1&fp=chrome&type=ws&path=/eyJqdW5rIjoiZEFtaFJ6RlAiLCJwcm90b2NvbCI6InZsIiwibW9kZSI6InByb3h5aXAiLCJwYW5lbElQcyI6W119?ed%3D2560&host=broken-mud-0a9a.rigacihir69.workers.dev&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله، رو وایفاها
✅
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/IranProxyV2/8529" target="_blank">📅 19:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر ارتباطات:
اینترنت همراه تا امشب وصل میشه، تا فردا اینترنت به قبل از دی برمیگرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8528" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📌
بزنید تو نپستر با ایرانسل تست کنید
🛜
ss://YWVzLTI1Ni1nY206WldZeVlUVTBZV1k0T0dNME5EUmhabU0xWkRRMFpqRTNNR0l5Wmpneg@ir.npvnot.com:10112#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8527" target="_blank">📅 18:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔸
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8526" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
آمار لحظه‌ای وصل اینترنت کشور
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
‌پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
‌افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
‌همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8525" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8524" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از اونایی که پرو خریدن چه خبر
😂</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8522" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✈️
دوستان اگه در راستای قطع شدن بودین و وایفا نداشتین میتونید از ربات ثبت سفارش انجام بدین، آنی تایید خواهیم کرد و اینکه درنظر داشته باشین،
اطلاعیه
رو حتما مشاهده کنید.
📌
در صورتی که نت بین الملل بازگشایی شد، تمامی کاربران که از ما سفارش فعال دارند، به دیتاسنتر خارج منتقل خواهند شد و به ازای هر 1 گیگی که خریداری کرده بودند، 3 گیگ اضافه خواهد شد
❤️
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8520" target="_blank">📅 17:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">😼👊🏻.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8519" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تست کنید، منطقه ای وایفا
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8519" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این پروکسی های تلگرام هم داشته باشید فعلا با مخابرات و برخی اینترنت های خانگی متصلن:
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
ممکنه منطقه ای باشه، بهتره تست کنید.
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8518" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎁
بفرستید واسه دوستاتون
❤️
vless://27d6de57-240b-400e-a036-192608ae0459@mbv.followern.ir:443?encryption=none&security=tls&sni=tino.protag.ir&fp=chrome&insecure=0&allowInsecure=0&type=ws&host=tino.protag.ir&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله رو وایفاها، قلب بزنید ببینیم چندنفرید، برا دوستاتون بفرستید که وصل نیستن تک خوری نکنیدا
😶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8517" target="_blank">📅 17:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">درنظر داشته باشین که فعلا درحال حاضر تنها وایفاها وصل شدن مث مخابرات و آسیاتک، شاتل و... اونم بصورت منطقه ای، مشخص نیست اینم اختلال باشه یا اپدیت فایروال باشه، پس صبور کنید تا همچی مشخص بشع، فعلا اپراتور های همراه مث ایرانسل، همراه اول و رایتل و... وصل نشدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8516" target="_blank">📅 17:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8515">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
پروکسی متصله، رو وایفا و مخابرات منطقه ای دوستان عزیز، اگه وصل نشد تو منطقتون ذخیره کنید داشته باشینش، صبور باشید شایدم اپدیت فایروال مشخص نیست هیچی
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8515" target="_blank">📅 16:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو وایفا و مخابرات وصله
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8514" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجدد بستن پهنای باندو
😐</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8512" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNZMOZUf75tPODIDVL4pqf0uDHRa1i941OziSEn6rZuikzeYSwt7XMdA3QudEnNbKwfL7seyAaWtb7cwHdyyIO-N_-ivzoqinVX9EdIXJRJMyMtB4_RHgcDoQzkXKzVCOAn3-aTyyqHAXjTUeg4MZVBZ0ZHKpvQcLlY71Tdy98YCp1UpBS54DKYFpQ1Pr4M16yOv8bj0u5opfJreUJhbAHb4KNktXdl_1k2xcMZ91_Vbkmk_h6VqXKanwSxcyz8WT6KH4Oq4Wqk8SVLgn4qTRuhGtXykobwEDhRLZZni8DHpoD9cW5Rmxx4DXLkEtCwA0QA8gxVECMF32EIFf_fApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8503" target="_blank">📅 14:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روح و روانمون بگا رفت، از بس حرفای چرت و پرت تحویلمون دادن، رسما دارن مردم خر فرض میکنن و پاسکاریمون میکنن، من یکی که دیگه مخم نمیکشه حرفای اینارو باور کنم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8502" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjyq9wxQZyFiC8fnIHjdkqf3kxgE-j0Ks9z14UwmA6M7cdItw5rTZv7gHK41yiwRLcPyuo-UKKHoYq0nCPgFxTXbQilqhsl7mMIvAUTCxMwsHkO8UOpUQB9MzlqGRCsEN7gd8t0J4Oe0D8Qerqs0CrwZwYh6yj2um6plNjcyUqiI9gvIF7UITZYVLvHGvdR7DR_vBfaTGeH6OAN-aViqtlghVNTBXbRq12gQThgMhRqg8-yjjsMZ-2bhdlYOq24d8EIEd6l6-BgoS9efjcVpA4kLUY8WtqSmufqm6AKYOK-rsBkfKO1MMgBB07Myb3uJkpdKflsEP-8L1-BrD16bYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا حتی ذره ای تکنولوژی سردرنمیارن با اون کلشون
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8501" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8500" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس جمهور کشور اگه تا آخر هفته اینترنتارو باز کرد که کرد اگه نتونست بنظرم استعفا بده بهتره چون نه اونوریا حسابش میکنن که ترورش کنن حتی نه اینوریا حسابش میکنن
اونور دنیا رئیس جمهور یه کشور ناو میفرسته یه دنیارو بگا داده بعد اینجا رئیس جمهورش اینترنتم نمیتونه وصل کنه
جدی اگه نتونستین وصل کنید خودت و کل کابینت بنظرم استعفا بدید یه موز بزارید رو صندلی بجای خودتون حداقل فایده اش اینه موزه پتاسیم داره ولی شما همونم ندارید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8499" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فارس: چندین نماینده مجلس که عضو جبهه پایداری و تندرو هستند درمورد مصوبه شورای فضای مجازی شکایت کردند و دیوان اداری دستور داد اجرای بازگشایی اینترنت متوقف شه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8498" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان داداش نقش تو چیه دقیقا تو کشور</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8497" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii7TFqzdTHu6fyXU03Ie-H72gm4jFuEk2psGC6IG9ZmS6OsDru2h_8epS6JKzIkREnUWZVQAsNcwgv09RoImmxMOsvKr0pX0VuVeGhbfoAFu9rfVCJV642xU3blD2Yfse_PtqDmdyYcBgYqgNepypvx9djU_sHgGKm0y8PrN3hq4miQ18cmAsLQHLYeHb22ENpWKrLxjB7_Ava9Vt7PFF-xol5QTiWbClmqwP4DRJ3K4ykrIQunB0-eYUBEUrK4PUXesHOPT-6a2kxQO38aSAszf4diEQ_9Uzu9xmQsVx3oGV-k7pJLaSpg4vLfzz0C1KpXefPHMiJE3faAviIZrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8496" target="_blank">📅 13:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8495" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی با خواسته ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» مصوب ۱۴۰۵/۲/۲۲ رئیس‌جمهور، هیأت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت مطروحه صادر کرد.
حرومزاده ها یعنی چی، هی پاسکاریمون میکنید، بخدا خسته شدم دیگه
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8494" target="_blank">📅 13:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzoeQb9vtG_cfZyzZBMRNaDgk8gvv-JKr20QpSr2YdT9WTntXcPdS5yeSe2QJv3xieD-rv1DNFIToTniLMCA6keCgVYrvset7ARsUZZ7FeMYh7FSZGWMlHQ4hF1LbME6PB7UUTwhq9xjxuczhifWtnv0KsteUDU_eOoIEclsF9p13WPZaB_2MjEK-3Q_f1ar376RsxoHJ2j4ErZKiwqtqy6u5Ntfw6kA8DztJqamt_X3bJo53Ui2YRdgQ0xo1IEFXVd_HrnThDU05YGuZTDjSgPE4K8S063tiXXFGflM4aVaSJFlckY4Aov57qqSVHLcjV-xNyrUMkzvwhIH5H10vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8493" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚠️
اطلاعیه، درصورتی که نت بین الملل بازگشایی شد، مجموعه روسیه پروکسی تصمیمی گرفته که به همه دوستانی که از مجموعه ما خرید داشتند به ازای هر 1 گیگی که خریداری کردین، 3 گیگ بصورت خودکار به کانفیگ هاتون اضافه خواهد کرد، پس حتما لینک ساب هاتون یا سروراتون رو یه جایی ذخیره کنید داشته باشید حتما
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8491" target="_blank">📅 12:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان درصورت باز شدن و در دسترس گرفتن نت بین المللی و برگشتن نت به حالت عادی، حواستون به چنل باشه سرورای عمومی و رایگان براتون میزاریم حتما برای دسترسی راحتتر
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8490" target="_blank">📅 12:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده  منبع:سایت رسمی نت بلاکس  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8489" target="_blank">📅 11:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOFae89Bwd0avESpjJ_vdQ4PQ2ytaDfi7mh8pCIbarOucc7v8ahQiRnHBN4fDqXlAMkM5RIxTZ1jt3Qog1lJvUDIxFXn4BTlSl1283TpA-2uY5zt1qpoda45Swjj0MBw9nNPi0jgda9P9E9Chcii6EKF0R0k92bdBjapb8vhM9U37UVdO3JeRAA3L6YVfTBmzuJkhhT_3kz0RhiaKyoNcVzayUxKMhvcdCARQXgRj5a9rGcUOOkFE4lxNuQV_PZwz_CCL0zBf7bB1ZgKiVP0mmXmVtMhf8ZOy_BFr-sXD4zc85KPBGyzc3TBtFNZs57IRWMspOykFOYu_IXk_i3inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده
منبع:سایت رسمی نت بلاکس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8488" target="_blank">📅 11:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادرس
mail.google.com
باز شده ولی
gmail.com
باز نیست ، اینطوری قراره نت باز بشه؟
😐
اینکه وایت لیستو دارن ادامه میدن اسمش نت باز کردن نیست عجبا
😐
!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8487" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/IranProxyV2/8486" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaKSgTrYq6hH2Hm968ufH_3ltNT5jDsIL-PKyAl8YkZNY-8AYw0fu41CPCvTfSNo1k2CJwwbfXGqo-AqXVH81JSyS4I6_5hvp-9othS6L1gp59T9jfHOXwYaB7Q3yz8zXm1rEeHd0MZ1hLY81ilZvDy_6pqkq4etJNzGypZew4HH-3aIlHXfqPYfBLqmTkqy2hQLLHwHXw8Vp7I1V7WtIDvFl1TjsBSV6lmjAoERHOHR0D54DCQqeDjSq6i3dYrADVcRq6bnA_6T0nLefE2vuIVbdfYeBzKPsCfu9vU7jgblhwSp9BlqRe_i6D8kMPuHiiXQRJIZ3bxdQbtE61qpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXaXWL1SOjrVikLMZcRIxK_xGif0KH6kyyyPQfq0lKiMckSI7zxW0Vy0j_homS0mx_qz5C0jdM8f0fz6b9tiBEs9Irfn5X3DEVIgsxIHuvxlMGn5nybYgqJBUZ8Iu7ahMSF4K-Ih9hplRG8BBnEJkLUkYlUfrCLTeDfXXND0jnVmN-vKs47L6llAUcMF52s4zFGFzOMoaACclobdSk6VWDfPCPInzEux9lCJ9sFbDdfKFaFpfoeyaWPk9cy-810h6D0wU2GW9BsedBGDRVOPxauJzQPTbmneR63NWuz9WhHueodC9OeZaSIqb3OXS_1unNgXEJhSr1jIXIs-aM-eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md9YoNIv5qSDY_ElyIG5bxyY1W1PvPgNSxvMLmxszeWwM8g01SpiZoYQo8uzbRtQSRv2EPzxXTjYtkVE4lqCyfXOJSUiVSw5GvOyihuRJO5tDde3BVsRVA7CpTEBnbn-8-r2f9bVAxfUqQthOIqgay-960O3wz64Iw1pC2xOgFeJ1YwDCj8bQELPaIvPYRpBo6DK4_qkZojz_Qjd6Chps9ZpJ5VfA0kS2EyitjSlZnrMNND0oFpz8aYokvhHZNOmXo3Rhc2vmjUbR_z99DkgRh1RYRpOYh_2cQWXA_dAjGUHsc8mqaghih71KCOjEeKewy1aeCvrB4PZ2NxWBLkAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxbNKYW1FWUh01gr6Jll9ZBy3Z0ANNjHotMVswdsh_9t8sbRVSxlnwUOPc-YIa2OYepwKvkWw6Q1h8nLLIBbrWyvenblfo52AQEiBwjiINp69KWoFB2gmfZdX_DUX4O1uYH8sCvoPnsorVK2Ywt9-daZF_5ZQ2u5kj3xvfQjfly5FxtUvbOHlJ-Z1KKkjkwMvgEJVpegGY5BYO98pRW02PlPKL5Qc597KgVzhfkq3n1lr34jcD0y_NR0Oq_kAAtQeEd9WO16zIH0Lw1_4CoMKtRep1nqJdNYJ_MVMnrPCHjQEqJQSijtYywcbAi0rVPwOpKpPTNU9uHOSFeiFnKRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZnwtsEv23gyhmAyVnS60RWetbDSkJ9VXaWXjqtVVAEKzlv5RLftWuTTNkN9mfmjt0R_GTgtZh_fTKZ-m306foDd2Zu4Gb-gYoJ9IMFnjzzroWwRx-eA3GeSjS_UmL9jX94f_x_nUZB4ef7KKv98fwsmeEZq0OLFeKm5f44IDpj-HKMDMPAT1j0PO70T8XuQnnePKltxDP9L3DcvlSidxr7naV7HfIKQTG0G9wY9e-uEKmh0k7IdRa2qGOXwkvfI85rIR9B2yRN4YUu1IOJw1c2h222VpfyUN7FidEFaLkqjCK-B6xMa8e74E6osPkJwa8gqvGEyDfhsRvCCclyuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvLUSMUIVTdu5lWvwP0s8HdniDDcmyicRTJoG1vhI32iO6h2_c2UT8PkXrbtx0QcBlmHKZqxDC8HDhPmZYeJUMv_BXevDV7dyrCF1KXdx0wCGmSCMaHC8x-h_cVXAGaPtU_FGh0KAeX1kzxYgQc_3oZC3d2zqr7OdBfuzbsap3gIc1dCg8oDRsiO3lL0pFXnoSGzQEutfLkWCjqIttxPxhnujyHYM1hHN_1oI4JAMNRfuqwv21wQHflsk0WZ5A6fm7fWmWv999Bz4TvVdFKO9cZ7peGS0SXhVy8nPMu4c6zy7B2wB6-PmP9yNeO8eKpYgrR0i18JB_xWpAdBmCVTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFU5LO8D3JJ6c6Uts1AAXO5dqfvIRCfmz7HrkQk_fzHPgWqNvLxoKvM3sSHVmHjyh7k-42ejhi8UnsJ-JuP8BieIVsmIRsu4YgtX9GaMiAeRb2lnKbnMpUsa5kOG-cL750hVD_UjsPbj3pTvwwekjy5KzXqpEsir2aDPJKO5mWTyCzOojAopwZ8do9jgDx7Qih3idgIcR-tTRwZH1ZpfvVk1L_l9Ip3W0iTSM29jIwWoPQq4des2EeCrWk1-va9zhZLGylervEreeCZL94a5jRC4TSFJyTFdpQl-zFjmdDawFsloEL1D7FIVaJaHCs-pXIV6gmNw7u8DInI6FHTxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzFn6OgclVbHNkEyivy0KatIvnzPJ624f-1q8mEN1cdJXTBo9iRlNQVRh4keyo-LLJZ3NJVp8q6RtpiUT0Oyx1VJA93OGL3H2cKQz38aMfDQZrt0Ua_3FfhCa2eeWQg5_kaUhyGZdEduX9FKM8gZ8oEEfPWrSy_XbNWQgOI_b7OhbYC0rxtNd7MO3aRG9kJuqzA5qQWNCFM-R7egJucD4ArIORw1Tt6o9kUpDoaTfCK2iLtBKZgqJojNFrYQcazdfAoYIK0HHyJ1JCEe5HCGSEzhzLmGMOtoXEyYFZnO4fPiAJz9G06xfhO-V3ka4PKhQ4iiVKKgZIPecBt5a6qCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTOimI8-HkTon7Z3RXEPEm33Twm2j5mfstNYi_QbtDG36ziGKmTyiYoZSd7QyndybP77XaMImFw42VerHRSKKZehl3XzN832SRajqDAYH8YqP12zywRBRImIMyK3saeqnjRgYIIB9Q2d8Fv2hUwwy5Lktej-d4DJoBkB0-8i6gwWEfzm8AgmCzGyTDA-DaRchUdbDaXTK4ucX2vn7ebocApyPRFgC6_eh0miVWnJSNEIYZcNNYXQJziL6iUpZBbKVg7f-r3-XtvVHi2-89wDFs7QXPLgOC7K-pwon9_carHwDeEKxogIvdVgB7OCznHuHElsRfiqBK3VfsNRSbo2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhgAeapDdeDjcL-Kd4gX6FNE1Apf3QngZ_oCn5brQcjDU5wL-cxOuGTzHiwtChSlVUsIg_rbVNi0XM5hwHyLoDyyAHQgK-jFy5Eg9XlZSfUD6W7To1SPwuoeeAOfzO5wf9vgQ23DWE3OTpBkfNhnJtuvovpn-s6gyswUReyglWrScGF1MVSBE3V19apb7Dg72W-XpYeafaatp74zeF6LTj7uJqubPuf7E-fzzf2ccSm3mxi9Ojuv0zf7na_efJOond6iuTn8ymvKlTa0NVI5oh2Z-ixRb_BBg26bdfeeZQi9UXQLGPj8A9-wIlwSHTfsYLF8-4g8L1wZyFReO75YLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6AnqAhVcaz-0AJ7CFjtQQLy5Shqy0M-FXEFFO8gy-IUiccl6THop_WRwNUe3Jg-mg7s_cB81ogRslTMQXWrAitXbogX_zTYFpLiwg6fz9IoWctsdCkXzVI4f3K6Bp06VZIfCWo-GgK0ndhOcbqy3Xa8sxkAQVo9sj2FB_fVwKMDFjeB1b3M1Ri9qP5nv3PElqGDTwfQKsGjY5H2cRZ2aITYOefs1yXBH2xzvgXd5e_1vpRxHOOeFSJuLTif2zNLYEHcYbUK60wtvU7fzu05chSLw7JNyWAnhNnMnFfFHg-NunClcsoOJRLjrLl6-SoZq8DzmTz_5MTyJraKpuztNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5Dod-bVnlQLGo59do_l7ejZXgfBYZUE3Yy5cngihzjADpgfV8daTYlJsB_46EPksSYHQs_BnJ7vWZm1E34LPIKWyRbm8xVhELh8K_3FxOdSy6_V4fUncCebfpxieLtpLklpw-lQ9z_2MMr7NYi1W7bp6NZcZ8Z0t3UV6PMq_nrsoIV0qwOCep-_tRr3LpSq84P5KpCZgFWNskXJ036HwG2PRGNyAc9nVmoCyh6nqL24OhX41unj1eNpzMNtNR138Dk4TndpzlmZUiL6bicYn3bSGUWOlZ0oj7nFN9AmOPGmLJKZkS4oGEbdrr1Ofw2sW6ekmmA1kS3QD0PPvt2WMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA9t2tu62F69J8YpNODD0KA4odoMNDio8yAmBLvnIYBFfC-qPCjJJ7Vk6CvzrDhhod0H03bueuT1Cb6T5CB_VsXs0oMgWLLj2RrGAXuBOWEUUduYbaHkqf-BgyeXlir0m5wVTo5B7lvzT_cYD-okyvkeGMdIE_tqDmdS5mzDpAtJX_BXiKc4_s4rdDJC8w7TMK_UXMRbID2_Q2lq-HlonZnCds_gDrDoERSNVfIxvCiJkw2IXumNclWkNUhrH2urR6_uiX1tayTJc1eUhYxfNb5c1fV3dcSaJtpgzoxlhF_7xe74ln_lcbjWw9ZmHcxY-GFRaCalDXio4hTUnzDq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=uhuCC6shcTJeDfSHGy6mieP-9nUSe3L8ESe-Q346CpYZeAM_mzfTM2GUHuGfYRCnzTrH1VgslFRUdPQIcAciO4Ac-vIpI-6BHu6TuGODmFw12WVOnzjYdbF4DBwhhdtHBbsLN0lH37IAzBVrBUkyTVOikT9b3x4EzYwEVVCiiPFkm009HfRqZOzjCKS0G4dajsVXjl2dwa8tjtAZnZzewWqe5dpJfNm5CuBFQZmb2GIsa7CQn3SAcjAHsHa5fYnj2YOd6OUeFVf4xISI96gqERk7jASN85jrihHU9y57RvRh-_5d0WVz6V2k_9-Pho_VBbVFi7vxuBC-JPbS7YphI48rSUrKWdCRm2ofJiE9S3juX_uQ5SWoXI1_cgi9GmtNLhbb97LS30EGc_kS8ei19zAQuqItB2IqOeSxEmKyb3QMBKfCqy7Qg9Y-YYvM_g3o9rjpWyA7vJHBnXJXbzDf6reQf2K0Lo8ugJUWQhXdM26ck2aJ51rudyrqLbtHKFBBwxCbwJvLYJJ3gCiDEKcU7ekyM6VnCuKOZQMhBGG7UfQbI5pBIRGU-warkF2OnPC954HOZQYiAKYE38y8bseKAx1BIQj3hy-HqtsgzJ62e_V-CjGdI8tWF7kR14uZ042pHV4KJf45k9cSO12COAQ4WkXtxb_R_8XX3_FmV73-nJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=uhuCC6shcTJeDfSHGy6mieP-9nUSe3L8ESe-Q346CpYZeAM_mzfTM2GUHuGfYRCnzTrH1VgslFRUdPQIcAciO4Ac-vIpI-6BHu6TuGODmFw12WVOnzjYdbF4DBwhhdtHBbsLN0lH37IAzBVrBUkyTVOikT9b3x4EzYwEVVCiiPFkm009HfRqZOzjCKS0G4dajsVXjl2dwa8tjtAZnZzewWqe5dpJfNm5CuBFQZmb2GIsa7CQn3SAcjAHsHa5fYnj2YOd6OUeFVf4xISI96gqERk7jASN85jrihHU9y57RvRh-_5d0WVz6V2k_9-Pho_VBbVFi7vxuBC-JPbS7YphI48rSUrKWdCRm2ofJiE9S3juX_uQ5SWoXI1_cgi9GmtNLhbb97LS30EGc_kS8ei19zAQuqItB2IqOeSxEmKyb3QMBKfCqy7Qg9Y-YYvM_g3o9rjpWyA7vJHBnXJXbzDf6reQf2K0Lo8ugJUWQhXdM26ck2aJ51rudyrqLbtHKFBBwxCbwJvLYJJ3gCiDEKcU7ekyM6VnCuKOZQMhBGG7UfQbI5pBIRGU-warkF2OnPC954HOZQYiAKYE38y8bseKAx1BIQj3hy-HqtsgzJ62e_V-CjGdI8tWF7kR14uZ042pHV4KJf45k9cSO12COAQ4WkXtxb_R_8XX3_FmV73-nJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFXMHKm9fcp0tFSED9hx11J1lQMaeLAFKG2uFNSioYnbikJ5J3-IZyC5KG9ky7pTl5Uz4UJM5MyGrkN6iXtk7QFjPQ79je5xmFFSmQNJ2x75qaMaGv6i5zGiTwzjNIOhV3V0rOEkmXOet3U241uGvqtcuefN1KEEjlEuHvx6pxlqUEd8BRLT9PTS-Okd8yWMzU8OIGzN9Tp_YngYI5_SnyQBNcFc_PdUWuDd3e4kBpA5xYNSt_jndiOOJqtOj5cKQdeUr2JcUj7W_50LIgAu-OxUW_kQYXuoKmUnzSyG9zqekiFBWjxrt-BPVAO17fD_h1oBWSJsmoEmHgQAiPeeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
