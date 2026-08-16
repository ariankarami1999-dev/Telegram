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
<img src="https://cdn1.telesco.pe/file/FxwLM6eYhhkPQFnDVH3_dtQ_vCTW_0F3onQPDSP9SwEApUdvYcgefvU6vfVB3ZfDsDHgh-zqgH44ozl7iDV-YFqsNUQhNq7TYXZ7VcLp22pIW0vrLB7z7Kn_nod6yRlY16C2NAd7kNbc1dQ54-vQjBO1zAKd_LbngNh7cHlLjTztfFv0aqehTIzqA-wYYJ0rAY-4h0XsBTUZ-sC-Hx466YXSTYLpyRkDFYyvcuUU2zh840EbebwhgQdGKVAG_ix2-TKGGxrhPgmMi9B6coAGwlGDNPirnk9j_Cze-bz_KIobgiB5BKhryirtKP2vQ3gX6E1imeR2_iBigeTCjY2-jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 09:54:26</div>
<hr>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/H4m84MfuwndS5JMf2opLDP-0E9EO4MMlzpmbqrOVL73ZUHWy23NCFHQ5aDsaZ7CJ2z53Oij7NAANNuAKfcXGr5mbsJ1xW0DagRV8s0bf2rZovZWUYiwm3rkYaN85mDnCA84_sbOCt7omDN1g0qdX91DLRrW2Oj7eLH3wan4EoHmzgDJ78IbSjtJnJs6javXSg8FGI4qemK7NZJzvl5ROsZ-NeEn88CeEGeJtT_o_3FR9Gu0FNXnf90OcEcBmqjVkdVzzimGUsFCNz_EHaeKMtMvBUa0ipGjJvFV0R8lLQY6qi1a3y36DNN0qALvgUs8XCbgUpISiwEN1pCHDdj2Z7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-jHUTjKQsgvx-fqiKpXyje0Rbs5ZDODZ1V5jV1zRKaVJA1e-yJpsfviWFdgSjN6VyJ7AoDROD5mk7VQ_u5_Uagb50fGdz9uJxYNT_ELw6HGVFTS5dROAEJ7FIcDH0RJAGFctAAvChabXTF_dOfGTpJP1iZBmdO3LnnGv1uP87UeJB0mKRySaTSZ6HEhh326t2GofSbxhy7lcC5E1FzTZgsmliUJBIOBzfr-GKpLrVkN0vVVI6bFoaErjJ1d3aWJr26f5B-nihwh0ijF9s5CNMvh5OJFjdh8bLTQB777wS5i2Wb25E0w9pAHHWqkGDgQwiaDYIPVUwrbSlGpbCGAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ID6so-Ik8C7WySauZK3NXOTWJz1jsWuTMBy9LIeVxo2QNbEtwXv50yCkfklCGDJ0hi-SfiIKXWXk8B15EYXgkP6dMStZWMu3g7Ud4yxyysT3y0EAjuXRseRWv1Ybdb-qPubY-htgkKtypKn3URsZZ4YkGWgpMpMIIy2ij2MvhwUaBeyY9f599EaNQ4oSHzAp6ETTuhxys8QFHlfg626t1uraB-ulNJYDPD8onr-TBM4-nYwsDSs6SifK9NLY_nZJYGJAKN3PouYmTAV0s7Dd7Zyj92u9st9aD-Pmg0GBVn46lT_O3Su9wvLErg5rKb-kEjnAFaLPBiSm7OzUouG7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBEkIm5-0enFgj91MIoE7QrZq9OmD44GKFPiQXTYCyBxRBSZxX0miZVaehrTQknmkk6vEcEgvYFywH8h-eVHvaOe0iCZ2LMAoPlq5idAiTegB8UUznW1QkIV4fqRMSVFKBu8M40MIUIXHZOA6l_HhGH52zhfLD1_ml8_XvFIo1quBrt3tA5lOazEHbEIl7fHrr3AE7dt5xXE4jSQ9KwewOQonBnIKq5DdkAy1_uYS9aFLtPtTITgntxVo8xOR9mdXvXur_XwKhtLzxZOpTyKdl3gMuFsUHqHqh0s9U2JPiX-fc0aT5zNCqLLsJWvDkkr-pnNHzwVjKt2ej4eUkkqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=FKYB0WMmeGxx4hkXYVFw_byf9SnQvvKUgxAmuFFY5JALQnkg2UN6nSvZtbWy61zSMex54_fSxYIBzL9ae3trxu3_E-lSxuTr5d_CoqHHBMpEWA472lt0C2oMSyOMThtfEWhLFj1MBbmeqPWUgc8AyrYylDLROOez_t0VLPhtldIRzF3MentAcvP9H3SF1k8s8hjlXnXDrKALjUCdBpzjU_3QYm9gN1LRZZ-Js2A6Y4iaw7vZr2zLt2iljD1pvav-cMNFpy8tr9YAu2LuxHerz07pitfMB9q2hKvGGz2HYfNSIIX84uFPnhiDmyPSl_5pTvXyXfmceeqr9QywfNyj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=FKYB0WMmeGxx4hkXYVFw_byf9SnQvvKUgxAmuFFY5JALQnkg2UN6nSvZtbWy61zSMex54_fSxYIBzL9ae3trxu3_E-lSxuTr5d_CoqHHBMpEWA472lt0C2oMSyOMThtfEWhLFj1MBbmeqPWUgc8AyrYylDLROOez_t0VLPhtldIRzF3MentAcvP9H3SF1k8s8hjlXnXDrKALjUCdBpzjU_3QYm9gN1LRZZ-Js2A6Y4iaw7vZr2zLt2iljD1pvav-cMNFpy8tr9YAu2LuxHerz07pitfMB9q2hKvGGz2HYfNSIIX84uFPnhiDmyPSl_5pTvXyXfmceeqr9QywfNyj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtDHvNGmNyatInKM_ZJ26pXv3tjyHv308O92BZtWoUdVVhGVshvvee7W7JWCTY0rhMzBM_9b640V477hHG2ZkAnh3zg3_Wd1_hMcnyEQhBsb739Lkx4QF2kLCdlEcyT1oolSYVjcEDOLnx7qioXUHD7cIEwhZAboblaYuVfplFiLHMvAVYDljL0MvxNZpt22tw2qkgEb-B5w3rh0F_ablPkWH1JkO6AQA20uNxdUQToGW3DpurdQ_YjZnfsBAgEkKMzyKvCk1_er3JF3rD4fqZYRdHcERVV5xqUr95ouBduGQyZ_h86rGyTREd9O_cUDgfz3rICY0CYxF2twUrlJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsvCN2VxTom2cixIBWrDuHUskRH0j7VSGya0ptgg2yJy5pqfrs4cEoaFSsb0V8gxNq851rAy4YziMUzmGG-1yx7Pfy1V0dhuROn9A6A7eUdUNEQfHRLgpgVO3tekez_E-iM1x3igEGq-yFybtEs3EV9jsEljQF-ImL8Zb9BY8q3tXXi4kWGxgQ6qde828FLJoJMNqokQWqfj4cnuO43KBAGBZph2SFkV23NF6FmKP40uCIjdKn7KTHVMDE0EFuKylpCpDpaTzYpvICtGXPJdXr550cYNyetiQD7zNI2K6dwAM3s0zywngpD2V3o-UOyv8NYRoK4OfiHj3kicrVDM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PU-XAZJtM3fniVfe3s9Jutg7eaGn9dCcgwOttzSMsbXR661WoSau2D48f11yfXa3FDYRJ6SjZaJbj_peZzdc9icN_4M3OkUbeaGfG4gFmfiZdt6TAv3-wj4-8p5DzLDN2EqmGXS2BJ4Tf7Zd4GhwHWR8CseIbYtUmhR2sliZ9hozaXhQ3SpfWa0jGtVc0Ut6fc34gKdzYUcJxQ-_v7uXhONoIT8Z77liVhcHZJGm48WBOPB40xprtue61xhYQdByxQlPv6hH7DBE-s1JEMrqlwhjFN2BJ726JHfyXb6cJDKeB26VauXUwQVV-eq8p8kopFrBEfNHPb62pau66CmO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m8so8dHC1yC5axlczNCtN-Nk0-BwJDwk4eYh8-1QgcGrWu_R0qm_d-LTKBozupKeCG2-gxIdJDfum3w5x3zT3dKHKfXb36-OfvNzrxtjrt4mnfpwukKgxtfyeQC9n7O53DOV0UKpZ3gC5h7VZmtyqQOV4YDPlIlbz13vFmxfvNFuc-cdTCtbjLSOVotGjag81xTdER_kBqXqo6Fcmwc6KjZzPG9AzAK9VJQb5UwTDa1BYfQs0ljsW2ekTglh4eDhjWFslFjx0NKtcbPHrfuP1eG21lDcgU3JiI9ubQxp56m3AaDeOk21iQ1MwHwMMzX81CDxXsnkRh6aVHcLIExPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/meqJrav5GDHV05wHvX9ud0EL7V0ICgCd0bWwTnFGKkML9Vm1r-0Ag4ZLNehKETuetncnqBgUsFXf9Jw8n_5R_0pFNYs1EC-dWAZWEDb0LE-XEkmehf4PYXkyoe9g5O8jutPnMeFcoyqtfq56RjQHin1GNPN99KEYS-bb8F_H8SM7qXVw-YEV3tydNSyr0D22Aon5FVXfmkW3tpAv_i8mkVDvsGDre2Hmrz-WuEpSbWeFoCSnuq-RTuVeedigoeWEILC_7qRr4Ck_3hPcSF9ktnbiXQrkuCUesh5dvAs84ZPLUStFaMTwfj4CEfElyNkAW2HfJ5T_pO1PFu8joEuuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ztn_dZPdXB76b7r0U-OzAnc7GNtNUFnYvFz0yJLri_w2ZeUIQ2CRTDjX7ProXNfSO81PB7tZWK2u0IDntRkxmRoN4TjgXB_i3tU6yEsxzid_y1UCYxKWV4_5qodio9cgb_jYMb1OSY8GEdiBLt5ZeMUoCqPP7NRWfdnq0XndcqX7Ltq_ex8UwO4O7IpczoXHy6oR0cNwBksfza9ZENFgU0WoPADtjIvp97WDIFhiW-qIOJxcYqLROZNVBa_63lz3FfsC867wJjw8AWHrfNDqQXPdrgi9Z2kNwvv1RjqdAvOIezXNY6YoP0z4G-brKbXvz_kT51ZQ8ktola-_G45O_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/An8hUw6sWAchy8DvyoepaE8sFo8tOeXG7MLi7-uHZObgcKBP5f9Pxu-S8Ce0aXOHARGc7fnPDsCSCX0MMGZ8MyXYTPbIvRHytxUD5DXR_DQp_lQjtnCKfuIes3kiyKPQRHDd9MaRPPHBA1pYBQcKMOY8oVkXAPLMVUFO-a6q3VH1CUhbB_UZN5YFRTG_wVgfGPoEXJ1iKKf_asNS5pJn-98keU1JxGj3d7DQ2FfgYLKN7W1ihRMSTOhjLhWV_bitp6uNPEQgVNhoqB2ET_I_C39O8_lZg4Pb_zWmNE6AEQ5Ev1QpzZoBUEeYSRRCgyL1c0VSIYIQ1plD4LsOxxjqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWPx1bQ2oi0pdPUCYFopNIAgVKrS_0dEsV6JMR01-KcnaFYAkDWLXTe7DP00y4_ZVOC-BARLcFfh_5q0rXpV5xnWNK2RcuOLU1mq5PqOTnLoLVuxUG_yrdBJo-vnnSYJdoq_nmXFafFGwUGGGvk6IKE1ZObRWJU1uiwEIdAko__T879Ava6F3WJDEMvwcN3mV4JvBs1XGtJN4Pl8MIdrumx5LMDz31hvE6OMyvGbOCZzwAoRlorApmnrHrosU8akzEkfmHwCOK_h6eQ9EXWyGiOtA_DNX6TVLgIiwxe2Qqx79tXTh3Fdrh9LyYWS1DvDwfPD_cjlpO7BA6pn5b9n6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wq206DgFCXs4TndDlgFIwC0EmY1T6p54RJPtS38dma2OzlkOzP5TnTQaXglYrb_-BdslZP0Cr0M6nf1eZGxClWX7KoxS0cPTO-SPaAyjycc1XN8CnPDQOERK5syKOTp_9smeFaFffH80wURW1s0ZFIchZBTsGZoi6cizv2vngMR2pZZA3tHHUCjO6wX9eub5lIo7tq515zSGIu36L9J9noV7sN4etj3uYwZElqn9z351U_Qo3TnHrQGOpgC_bZ78GWrm3pDrekhV02_cm1yWD3lW6X5OghCdSZPn6ZlgbyvCZd8BlG1YnBHbucoaUtQBwLuI0-VWfS6AAW6HelHA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tNLhXup5OyG5MPS-1s2gw0bPgVJySmpZfeTJ4YQ_0SEEZDRd2ubvl_sQvfuSZiJbk4J_eVq0kbaLfABIwIjHOChN1sNqwVPyKF1fNozqYdWd7XbcVWjK3p_oj2hS-5FZwxI3wHwW1y7C-BQeJydsIFgPGzDZ7qTb4U979VynxxOv5rjIhM91W4y4CeCP7AkIDOLNLS53xblam__tZye8GB0_UHcUg3e9dSwU_a1MhYKw7diqIqJn_bEK2-RXQ6XcSWzspeb5zAc0ixaLfP1N84NXy6RkHil89LOjft9-nSotyW0CmF6Z-gwNnDYqpBf61j88NnMi2KHHr01g9Jd2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWUjq8bOw7W8UmMghamwWrrinGqKV1dYEnSpoprQmT1luabQzafwN6AUNss4nNCHK5zi3N8o2Z59bsDjSfv97xJo_TDgbXwmAZXqF9tTPeJljPjEkAXPcpTO7veHTcUbL2O55ZQmVME-YNAdeyF8pNoCQgfwhmD2BHCReUI2l2t0IRw-8OBBqSZvISENR0wAIkcgTwJnCalfwCOUdPTIgq354WECZXVSmcn9pcikWUCKkvtnvGTLv7pvOvBq6ba31xISV1ozifS10y-aGPLB5J8vT519C8sDsY0qT7aOspH7AZ0Hp0mAp4HCF4agqkE67a0URFmffZU4LomfWybk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJirm4-yxk-Iif3pXxrodbdm5M0xGO9fsxCiVm411OQp6osgBK8msb6HWxCSWJ6RxYiANJgzklQmncfyOBhJYwlQ8v2n41bG8PwysJwEdSq6B96Xb-XwDLnoY4VTaL3o4NqLqjoL9ALrojAxvFw8DWktd0YLjogDE6ud5LhBeBCUDBoL_kmyhybOGIKKeO8OgPci38nh9d8-wLzEOBQGUBPiuRh4snw3UUeBJqUb7jrm3CEFWtLiW4nTubZQ-W_tfCZpUWbfzotPSlSnwFbsDTNiC93w1Y7QeaAH-3aZg4apF8QaSCNxGk6FHE49ciHM4oGbNdjtAExdKMzsi6Pmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-oojeTR_LuwnJfRpFHwL5JmWR2Z-1zDDGLEEq6Xc5uZ5NM4xgVeLc0oWUnN0KOSPLdbSGx_OS3yV-4CVrIoZd1t4yvmczmHx3-TeZ3LbKuaXMavezavTOyxaoT0w9fIbcd6MSFc5gI9Y3S-1VbL7MpPUyDSKO10prj5rDtsGA6a3QDhkBIPvcVM5BfRQmZYSoX-OcBfHaM_LGkDKM6vl3DYuS98lFdWjhm5OSrRxUAv8F6UGBg_tHowDU7HJcEu5I_FsNeaAIKNy7UVrgmMgcRNOE-ZSf7JKtqboNSS9qZ0xTe8f95KkUgAmnc_CvmYrlq-SrqHJqQ2A40Cs6gEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fdze1MGvzmQDXZIVvgbrQDmQCM5bTK4Cp3yHVwuEqq8vgPWC26LdW105MdbUeuDKuRUJVz6slU2FnqdYx2ZtYT1AjtfTIjMkct3cseDl3IR8w2WKnNkMZ1cgX5zV3aVMmSh5bhGC4IuYTDQm5LxxNOWZ8UKn4we39UZG46B8X3Q_D0OYxMSD4PhMa1gd_09kCzr81mRGvHMc9uAooYXkEtAkS4f9h7jz_O6MuP1otNIygqvYEGCmpQcqbNX4hKSqohkgAL92IK_dck0BO90d6Q_eibF6J5gO8glycWc5WHQLCwv0Gw4yNx3UKpplHNqQjWkOQV-ineb9wmsG8tsZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gpm97ROQbCO5JdqdCJcqdWgu0bgJPSUAr1KEUPmJZzgwHQ_pl6Pd4sUJw-ZTtk246pVjTRbQJ_OUnnmyL9DJ84CD9iA8pdjDfXWTOcV1_jhiAgbMuPiuGdG58caAq5jLRm09YS5UuMZWN__WXtCxMHwJQ0KVCDB0SZFp4tNfyYieduXD1-BKCXpRTOU4-IcdLEelfcuXoEv8rd1CU3N1bm87R9ZN_ScwPDlLBaq3Z5ECIJksr5l_unZeZ3shZ2DO8YjjZ8tj9XQ2dl2NjHETwH7NRXS6Di6vrhEXxjM5pst8cO5t6JFVy1L8nkilxkdV1HBwsXWcZ0gP3jH4m6w0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oo5DFqbM7zBoq9tVPb0ssUveSQBM_Yorgej_7dA4iixCJu3HEybkt2TBlinagz-zcGxHLp87gktOnckQElP_HGciMmwznKfxFp88rMM2mx13UjLaFjohhI8j92IgvYz7SCOC60AteswecwB71Cr9RkEltioSKUGf4WGnmU00cNQRPP5vnPA_zIxJaKnKFN8Uwp2If_QwcEkpgA-DuEhzTgDtP9YH5RGKAIytZKQnuoHMKD_N5p3Xk9ymrTtDS4mVKqU323y6KCPZ4LzGK0WTn_VviEkQdegxvNq_KEurkhwoFePBzwiRDSQeB0uaO-Pfv3M7KhU3nsfnDIliLsWgsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU4MgrpQKBiLGEMlfOBE2UfCj_eu8jGMRvKr1GmMCnoo0hvl9vGkDDbtQhk2fhB0hOvPEv9bLXAufsuHdTvmSBbECpLBFNEA34XmmiuW_EX7Yub0vZbbFhPyTEb_7wW5RADwYZQ-hLRSFGC8k1YwSFAvlKV-eQeo9AGFuel7Y1j0GJV9pCQpwpaVJJQbEMttXqhb6kSF79Wni4TfofTh_c-V0xNfArfS4s2weQfuC0xOeyZTokjVuo_x34D-akXctCRkULD5AWW52N-gfmujqkQA9t5-dPAiEkfmanUrOSMFprWfHcsmS62AS4rExodbJeCQL6KkhoZOYBAZyEBPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uV0iqPwXF787B_42vIzPPs759MrIIwjCNx2l16D9xis40x_kgYcJOHs-c8BEOXc78noK_GYgFHPTYoeTFEUgExDv39w_s6wnr8U9VF8PJE0CHrvgtu0nSDefTmLSKCAnZxdivrjx3lKq6fK6sP42ImHRZ7YLDabOf_2u7UE6RAw42QQfYf0h2-DMR56XSYSylX8eyGGPSDNvMCaCAK9WPDTI0a1_sOA02lhqrZ5n3RFW1-elPyf5m-EqbjwV9nkPCQAkeI1QyoR_pVqzdmquZyea07-KADU9g6eJZ9oii6aW2XjfdzWsXx3GaWZbz7nWmghmJE2KR1IQ34zxE2Guww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYupNYCCg2iR6vBlTSZGFr5ZmtCrTPZqtk-YOYvF7El7AO-EE94PbQ9ZakS2ssVAikH0B2PReY_ewWDYLHNpRUkXt57MfZ3iRJEKbUp1Qz7gBc0eCFZx7-7o0-PmvOQXADwwfFZW90N_Iu5aY3taSRjklWLTQvWAjFDrO-HpAf7HnSgqK9u4E0EpKkSdeLf94cvPZsZhw8CXnizCYxOxv2rS6q3EXTaYNHrGVOVEQnmfpel8FAYHdGIHLtT4qndyQe_wvntOLJWnnkFsqTMEDS5euGhCbici1CBPL9HW_E0n4K-m1kyTtSrjrv8qXYS7kfBcB9x4zk8nASpHHYFYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PHr4oO0ySDH351OULXrVtxSSatvzNvT1v8xvEtxtnkNG6JPmgnfJSowDsPBhZphjAZyQh_hLBJ8pxORkevxSW2qpPnu5qrI_tzP6THawCqDHQUx2cd-FHpohmpcP0UDQV-2BMxioZfjBFh5ud8ar1R_xKhySe_FMpzV-2c3hdLiH5JYx2aK77VYqaCWuc-uI1ObqwrH6yVE3j496C4YxCEd7G3u7MePsQdSltAvx84ZUfQcVQa-2a3xsqN3gXZeX6kKOuG-RmsSkQlm5asLZg8YjHf-lueTaVG0TePKYejuH9gwLXhEYEnDYzj1Zgtl0NEms2Cq2nI9VgMu8cXLvxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lp0JUulh_eKsAX6txh0UQobdOeR5i_ESzwD2PbDoeXaqsx_KOKIGN7GtZTd_nBFEAAqyr2ZvZRg7U8KNmwz-U8y_3kejL32z4cDyz5G_6vfoLENo_VqpXQnkzL09ZAYR-rNLYmiIPI-wbkO9bzpU9exShXzo6MjYMR_hqQYzIZJcy_fw2LaiH-c7q1223qEbXhmNKE85LLgJkFqO2WrIoAubRPsb59CP5y2UHPPuEjbS1lo2tYJVz9x2WUVXl183ubijmnZoYYlby9nPKBTGxZan6J8wfPgwWR98ev16GrDvPmf-wR8_BLUp91sdeAxEmcrhiYbIl95dHGJOKessnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxxwJ0qlLyOpExXD4Kv7hndJSkQyU2KA1AjPBxb2c6ExeHfWDVbsFId3IA0W3PVWK4as2FeYxBMLAzzFCx_7YPpFWl2RduyEoGrX7AI62CRsmnJm-XCu97yogHgInQ_YRvcGQ-xqBBHgT9lq6DxIa4h0BvsxZMZKBcV4qLNp8_bbZf8QgheOeHLOmvN2uEEWx-X7SQWFpthZrUpqngXWh7FFfDqKkbGh6wc6y_B1qViA_gOc2IJnt-fU68Wr9XMs10j7f5kZGM87EIX7RAoKaDHfooY-rG8NB697lDvZrfwVNNBFwqH7mkP0UgFdB3sE3zReTI5i79O7peka-agL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8uO5Z-92dCyJedeJ3zxhw1s4OHlxVzq3I8XwATYWZWgYin8TPlbw5Q7CoQa0oNg3FJ9rHhNYDBcYPMKF3orXrulOR9AnxgCgJFcbgkBJMeG-ffYE0QxXKHH5DA-GfiG-1mTWJfx7Vuhe7WX58kgknkYlcvsQhgRa9mptTymbVYIObP4M0p2aygt6UGAFoPtDE1opidAbqoxhVe1Olg5D180MNIcuPq6V3-EW5MlNuOTvjUWJXlaube9gBpFXURk5K7QEUk_BZgjT-m5vi0U1OiGp6eFNsrM0--Vt88IXezOrfskzOgygbgcMo8qE9tqmPzb_zSFUfpvblPbOLZ5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rltugww2dZKtOE7y9uPW297oFNTisO_2YowDKo0e4fSXRReSMG99s7347Nw1Wpr2T2EsnX5OEppYUnFESGaB8zdSm5Oh6kY9npX4fFS1XVWcvLVZ8cXFxgCoC0QPHa4lGtEYntjoKlPWswdA86VXOf-ZZO8FKTCGnqzyvHd1cx3t4hBonUmXdR4aj5EngsIcHncddcB10SgUlnJo3rGrDAioPdRxTM_KSONcgHAL7VzztWt0ik5YaAvm2XeRflqezdqgRoQy66xEA_h14wGwckz4CuzvsJRr6tmaSPc2GfWnXJRu3k_zhEtEHin-208pZS8mlPNYW5FBs1FmpsNYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JGJjqGkjGpXkmog7XR3dB4T_3CW2Jg9v_1trHx8AR6-WFvuMAyudedEz-BNkxoWZik0bETx5IcdY3ZQwWSEw_8M7ZgvxOBNb7j4bFuUxxbJEhnfFl1nRQn2_yYJWz31vHprITUoKP5E6MB4w2-FWPkPAAt12pgNxIgCyhhhUp6uxNUcsFMwyNEsUM2lC5p44Piq9Wo8fis5oTT65weBWQyy544JQwZx0Bt9Xzjtbfz5BS7CsbOf6lAmPNbB9kDgUbvbvXNTiVolZjhcQKi__6sJi65rho0VJYz6YYC-TiSRdPfDQjTtimwrw9jh7sqdZ9EwHPMn3V9I5jCjZMpwBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpl_yNYbkfzPIlDqk7IwsFrViOjwt0Mn_WfvxG21S2OhPrjH0IhqDjPVOGRNlfAoLeBORHRP9IVI9vCyQpPhQZ4KTuQHxMQbNS3SF0n68e3594g0-JFLro4x9o8omt9lulpYegOTPV8EsE0n0no2TawjgtBrfJAfARcjqwiEqz3osiKOjwBxYydZLj3AarmYciT7tr2_is78I1ZO1bZbcdwfXKSAsB0yaoAVfgIQktOUTNz913K8mtxzxmKsYQVwbtF2dngE2PU8jw2pBclCQzMnf1bfCJmCpYTv8Km5Nb4VTIfYqj0ExyCjtNzA_VUr0bhUI6TTU2eO6FZqTvCAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V6DJMb4GkSiTECtOKQbKYmnouGWBeFYdVaTh4ZBHKR6T0RF1wahIGqgM7gWuv-0NIVKLNcgHfhEsRKkxmmrqSIc_rfqDk7vmPWYS66yfWMX0zE6oYagFEHWJhhrUiUVCGH0MQBKEmktJLHMwxLZZA7flSQfBSAR76gubUSDEZm2VXD1AF706e1m7OPViXz9SFDl2CffojZy3Ha1r2CXR47CdACnZ74q2Hto9XExd8EP6th9W5G2gGNNrBCNpZfMqB0R7omYDlQAPVBTRxCt_F2wLafJ8IBlJ7i_dkobzQgtkCQvv_E6gicyTuhqdwxXGyb487wi6cJF2r5WyquBSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJqUASXg9ufdHe3nKGagQPYIp5vaHvETpfiUr2mRMTGGZfVLApw9MEQ4-9c8nNaStm2yQbpsMXYfJYtsXR2FdqclTg6HGgJmaU4ZAMMO5ZA-28fD8hUnjs2shNWpPXNNjx3GgnHWF-lWQ5dDYOyAFx02LSLBBJUQa097M5z8XnLqTMIjJrPV_cWk8WyJEwTFxyNRFoLR4iOZY-5AhhfH_CjRLanqcOhYBVvzAWH3-xOvjhr2YBTst39t7iXPVYEyxJ-mbk6nL2Hk8YPfTXW6PGoe3kxBmiXJDW5t9KCfgS52K575QXcMn7p7prcRmA4dVKoP5HRnfi7_SeEmHyy4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6x_RlA2uypq08n0a2HeAvramkD63ueCAsMjEpBS8O2Uw7UeZ3qcgqhxKxAJV3k57VI_RDDtYG6ve4Lx2C8i5juMlO9RSmx7gSj73MW7EIY1Ihg7f9HfUPMkYmMuTUJeOko6IKgW0XSFRxqNco7Y1KkJROQlB07FBOT0MTGEFVGHxpj3V8NzvW_xgKaOkYFsgerx5lfpoFl3-sIhKssDQGB64apv7sIk-NOg5VGMoqAIRqHy-6ezaMMkzRkxA50t-b7VQst7nUjmABA2_dWR2JZh5ZBkxLJH-xcYiFBKJVLAcrRRVl-W4BhFsclpzALijdHdu8CgpCIjFhHiKBPSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iygeK7ibjm1rc6l3J-zYcK28dWYg2wtp9ZgEJLTPTL2MWn_tI0TDL9sZ9Pp-9CNkUqmds5vi1kVR9Vr9_WiZhOpMW9E9jP6IB9BIUjPQAwUm7C2KLHcAFJirdgGkwaiPtdBUx7QPreCJKEX9-VF-PaFL7ZFgeM05z-FDf3HMQfDNIOMsuW1fso627-2a1H6mcX73tdrg8l48H9LykrdziBsLfzbxMBSNktpfduQG-rgOqcuxM7nOJ6FOpsgMkTLGrASyQVKifR-OuvguWstmEVYt1XgPi1ObAF9sorJk8fNhIJw9tJ7l-nLisWwEqW69-Ly_38clc3_ZnBwRIj1nqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=iygeK7ibjm1rc6l3J-zYcK28dWYg2wtp9ZgEJLTPTL2MWn_tI0TDL9sZ9Pp-9CNkUqmds5vi1kVR9Vr9_WiZhOpMW9E9jP6IB9BIUjPQAwUm7C2KLHcAFJirdgGkwaiPtdBUx7QPreCJKEX9-VF-PaFL7ZFgeM05z-FDf3HMQfDNIOMsuW1fso627-2a1H6mcX73tdrg8l48H9LykrdziBsLfzbxMBSNktpfduQG-rgOqcuxM7nOJ6FOpsgMkTLGrASyQVKifR-OuvguWstmEVYt1XgPi1ObAF9sorJk8fNhIJw9tJ7l-nLisWwEqW69-Ly_38clc3_ZnBwRIj1nqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REJ1r1IwK8oryS3tjVv3NOdFJuHx0GMstRVEZ3Zjwa5CfYKdNmxPCsjbAQ3LgYOElZwYSSaRKrzZgzbRYt6aqo4pxZHwdopn2SysWa3VyMMmA0QGSFOMaKuKe0FNl5ANyMNNRme-tvBgNxc191BfjDYYzH_BU_5kiXqfUIqiMN-H-IJXYlCA4RiDNs4M0PyH46JIPbeBrZjclI9DX1G16Up-xMdk1RwDE0OGbwPLBHBAEXLi9DGnqUbpa1WF3p5Ff7mIOGwgfGtuegEqFakylbS3OHBhQqJ3-TZ2XjSFxeck4P7txUzmtDfGJidJuFcYvNzL4in0Yi_rxQsT_ZidpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VU5DJzPEA93lZXSIX1qUkSxKZ9OoK7MTc3mpc_bsxJMyg4Xd_-QDtPu8eyCzCG21He1N1mpBWnQiDSOLdeofJTNT5GphaU0llabSNa_07o2JxSAInp2nnnbAPOCUhEwZVIxJ8lvG-hSDsKxLiYmRb1ETfd9gg3ccvPBZRQV4J7Fd1TotPIyT3LDhn9iRuZGtu6VWujo7h0MPBDtv_y4TqEDLLGr4xNsNlgRHM7592qrp7rI6b3yq-fPUA9_5QANe-tcLBzBMOVivJaqiBW6UxfMZvoCy1jcHofYagfsGKBdY1lh-8JZIWVnqcAQlfoC-bAvPRj72jUX969nP-CO08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TE78pCAnNRroWrJ3XWvbqVUWUxIZ1aq5wpaw1Zs6ZutzVQ3AAYtGfO8oIdxBsxRlOZJ1s9C9fRnIJd87EzMgOZ0Xx7UkylDf5urUY7O_pQPdG5YlrAbIbpuCsLNZGJAvKeby5sRij-Afb-BmW1tCorN_WrLqIAAcVBfpe3JE8cBapq-b123oM_ukcwTI8v1gYxs9mwcD2O17XViH5oQHGDfhD5wyvAsNioklMf646GAqOCPO3FmtyFQYLecQlqF7qhb4DX66ZEspUi1wTEjKvG6DjkwX4LmzNy9Nr7kj4QliOTa7PWpZE2ZONh3R-IIO-F8cvSzpS2R8bUOKIH1SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k7iRyeexmAnDv9X3LyPxJgzHb2PMCnxCuJa1896rV2H0L6StbSBl9zECuNUZBs3Gd1Fb22YRjFFFs22ED3uJWAxIk-OLxZpLNsV6kxczLCWnKyNtsxGCUYsV88pDFE2VraOMrHixPqwUvispF-B1Dd-hRjz-dnwqbKZv1_Fj4AFrbYEIIgQdn7q2mRJHCt-BG3QZmm0G7ehabtB4XNkiyEvJfebJtd4n3di6qgur5bWma50xeuqp9DLfZrrssIXl6JmaUgCdhbfBO9ELpaVw5iUAW5jD1tJvv_PXdejGwULIYckolI9asg3_bJOvbLMvFzOldCeThCVfAQaQo70NTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q4TDVnOb4AaxCpUBmuX0tcFIb8SZ8IgF_R0SZ38mUAMPgKQZao1zO8lNRiIlAoczN1aY6aS7X-BUy-QpU7qYjJ5XXJSwBLlRLFon9KZC2XFnVsB_NAogtIJVdUPt0emaWcs0ovz0Oalg5ONQ7MQo5IHyvTI7ZVLALCGn9lQzzve5JjKn2i1n9jgxSzvpVovZFp2hfMWXKDoy0UHbZ4TMQKKBPT_nFh-F_AuYO5S5VBekyWNWdn14KMk-3RLy2qqVE7paQH15nKEcrllj9ZkS6lumgLvAhxxobySZI8qjhzvA7_D5nDg_Nr-AEJVWpE8DqOvStSu77_l6yjxZfWwg4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMEHJWV1mFX37m706IJQjX4fMcM2kDPFyxB7cAK-UXaR2DmS5WTFBDlGDbi_MmKi8pvZjDldJcK5qZI-81fBLr4hwzfw_af9xnt4qBIH85uhTJ41_WW5b_HPBSyclnWFXPObpG8ApRPWmcZH2-maHGCmShboIA9K3sw0BuLDL06MeV0J0rwV7VAxpnD0-28UBpW9fitLr31wy0g2npX2oZa_dbizLC8C6fAiHYU3VmOZhrVbTWckg_xvXFW1OvepIMGT1HFK3k9PNBLMNxs9WLR4_wxyApl46pEfd4baH0Wj8keDEhH83w7-2V-kdIv9Zb6AvDB4t-aew0Dit1t77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=YcAMwTpiOaXBe50SYvlAIXAi-cxJxF7622luFYdw7mP9pDdIx3ErpdVZ-paFixjgYwTO8EcgP7NkF03gFXv0blNf-FlGK5RbQpoO-9nNjV8jcqaTqc427c7Sn8lqGLE_bsF5LOn3prAC4xMlmY-b9Kp4F-o2xRtEN0jMrLFZjPXXnxis_w05JScddGXee7-ALft0akZY0pYPQbSyrEOxKaWFY3Ue88Q5RCTKrIWW7MV_E3K_yoArxv0EUx5_J3WhN1uyobo6TU381jUtQ26vuu2ccsZi_cbkzjFZDoDxT_46QGt3lv43huWsyG4XvL7WDxXKhZUmIWvwjsuWnSjenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=YcAMwTpiOaXBe50SYvlAIXAi-cxJxF7622luFYdw7mP9pDdIx3ErpdVZ-paFixjgYwTO8EcgP7NkF03gFXv0blNf-FlGK5RbQpoO-9nNjV8jcqaTqc427c7Sn8lqGLE_bsF5LOn3prAC4xMlmY-b9Kp4F-o2xRtEN0jMrLFZjPXXnxis_w05JScddGXee7-ALft0akZY0pYPQbSyrEOxKaWFY3Ue88Q5RCTKrIWW7MV_E3K_yoArxv0EUx5_J3WhN1uyobo6TU381jUtQ26vuu2ccsZi_cbkzjFZDoDxT_46QGt3lv43huWsyG4XvL7WDxXKhZUmIWvwjsuWnSjenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=q6TOZhsTtFrOiY-uf9UfyLcU1i_ddf2UcQS7nRpjtBTVP8Ki4lWhNQk4OMLQtAiT_-Jt0EBsR38_PdrArCcNmDLZANAc5MwzD05o3Vm4aDzZbTjNKfBXW7zuNigLXFyMkXCg-F-JdJKa2Bn0j9ah8n5O5YxQTHzn4xAx8Jn9MGGf-f8NpZgVpXk8zScrCBaJNEcrEBDLELLMcNMf7qaNEZ_PHF0HGmaOsM5BSvxaavgJBBQskeIYkxhyJS5GbWbBvO_KIky-qYSR4xR4JK_CFggHwslzWUPFWb1pVN6MTAOofdJ9zfjkM2_7-MQivA4yOFDz7ysk12g8QBKoZYsVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=q6TOZhsTtFrOiY-uf9UfyLcU1i_ddf2UcQS7nRpjtBTVP8Ki4lWhNQk4OMLQtAiT_-Jt0EBsR38_PdrArCcNmDLZANAc5MwzD05o3Vm4aDzZbTjNKfBXW7zuNigLXFyMkXCg-F-JdJKa2Bn0j9ah8n5O5YxQTHzn4xAx8Jn9MGGf-f8NpZgVpXk8zScrCBaJNEcrEBDLELLMcNMf7qaNEZ_PHF0HGmaOsM5BSvxaavgJBBQskeIYkxhyJS5GbWbBvO_KIky-qYSR4xR4JK_CFggHwslzWUPFWb1pVN6MTAOofdJ9zfjkM2_7-MQivA4yOFDz7ysk12g8QBKoZYsVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAEg9gRYeGyWL-KDPmkq0q8JdUcg8dks9ZpFBJO6MTJyaKcUSvKiShCCfwAHZaRnoF0kBsBGuT8mxVBw4sj3DFxN8Cf_QuOPNQnhETlLp3eMIt_KIDLZBIjxmB1iTK-d3UVg0d1d8GGlIj4ItwJgZzxbXKnmx1qvcxv7g78m9jXPTMySJm-pHoHUSYUVFkHaSS4WoOU8fnQ3DfMqti5XwfrpmL_mXFavj737XbNq9QNUbNYIl5liTOQYOwA1jYxazzD7IgNcDRwQezi1Ox1ns_hAwsISiIdjBXLLrIk7PhfjgjlHYEDO4Iv9rqXwADalf3emO_vomwB6ok6mRwlwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xzp1aZMU5oNl2i_W76r3UA97aMSrTwQ55UCHe0cKipPzd-CUmQht0BQIaEVqOl8M3C79MvEbnr3Ise5F0Rcau9ekjmbybC24GTeRFq1VOVIlVmQU4C8J-HGtqqTkatgkc_8ILT7vPMKZeXzVtP4edjds89M5yfWtgQXoLnf4YzobLki3KqlhwnSdWcgMd2B71_LmzqPjG7RjZwZ4Nc3j1lX_aCPpib5HS_2jsWPwJV-PcXvMQUtPYptIIBOLebxJBL5FtEGQJGRQ8fApgSHgvuraUg7XqSAhGrd5WPHXC84Ysacq2uv-NZ6_3zrmyH9JjFSmBtGlPupAfjkO24RiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FJdZaScEw669MzdQcAJLhF_DfKBWjuWqYY8JElpwNzV5cj1JtApSdcKuRXluz60jLpXQYaJGMmFOy7Qns4OlSXF3fvPdoqMBsudntxCIyBY6Kq3jXmU3nsiboKmqZofeVsSCs23mNZL5wSVKfESEKND5U5f-kN5exYLZZMEbvupOQPHu27RJJfvX68Wm9hbNx5ug07BrsH6RvfPpZzWSqV-cQ9K_K8-ezxUczhsL3TayQ_kHpUmAtG5hvhpCSkAD1utOevGBz_jYMQPoS8Ujx6WdfiNs9Hz4C1eELCVQV2ySm6Wxs6EkWl0KpZ84gKoMBkVqhxjWWj_OhHvRLE8dHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q469c3055TM7XPSbs3A7ZeWSR3U80iu-QMinXUI6HHIkMuWnB4Haue_6W8a_yYx_0rS1QzTcU3h_qv99U1HmIIuCQulvzasGmpUzWA3z7ZgEzf9Ui1Wu80imCWTaYTyYdYdHixr6IsyZ8-KsXuoAaEiQCw4XZ4EIKeF0SMA8soJupzKDn0A65Oe953OTN20tERnvgbcy1PpA4TB9IAX6Pm-kKOANVCyFLyzgAWXHvWzO1to047srRq4RwvL9EBzu1td1kx5INeEDd0xOlNOkM-OKI1I47ozCIGEuXlhjmnHskm3vpyhqNo_wXckhjGlpQm1i3HwxeQPbrpgB0Zmqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
