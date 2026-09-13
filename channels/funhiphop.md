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
<img src="https://cdn4.telesco.pe/file/BFal71OjZxRK_NAfPX7pe1hhSDaomDI_hSdzBOWi8JBmY5FrvJVIxEH7tQn3oU4k0C9eIUFMFE3Say_Fb7U_UuVsZsJwao2UOvCpLIkrNbXSz6nLXsqMGVGt3kYLLaKEXv1blm6FIXMddkjYMzwnGc1wVLcTfOqLsF2LiMboTAhhphn_AMgNd0U-DIVPjMsxmTLM_7K5mX5XdnPzPjP1Q9UJMZDbeEG3bp4sMiP5qVG9D_djmi4IXPj1Lw7nkGH3uDD_4eZ6bb0cwDTsSiVedubwaS3_laBbWBgyQECgbwgPKab8tQ100brNTfQRJgGSu9s59AZrin39MFQC0Iw4cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-83355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بخدا من با استایل اولدمانی مشکلی ندارم، ولی استایلی که لباساشو قسطی از اسنپ پی خریدی با اسم این استایل در تضاده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/funhiphop/83355" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کریم چی زد ۱۰۰ میلیون اومد رو قیمتش</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/83354" target="_blank">📅 19:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترشتگن برگرد گارسیا گاییدمون</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/83353" target="_blank">📅 19:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c3b572b.mp4?token=VEmcCgnanCV7JCkIzdbV14UKtZWGe8r-LMur-fCjN7I6kxkSHug1H3SmN54h75UzaJlb--TRp89xrwknT8T2NSooRF4oSHpNTV6EseQJac3he2tBeBaZa67obHZx0O6T96BpEQIFCsmVqywNeNU6fE36a3qlfWmxoL4B39A4VZJE-iUCJjwnbYz5w-_qShjP6TRpjIinDHV6Zsq1wh_hy26jMHJuf-Dv8x0LFBGi0iZynR0e_kBr1-4lvVCb-202SbY76TemOM9oMqvz2eBWdp1AVOunFdZZyESZw6FBcxZ5N_Cx0MmUR84U-asjEIlJ30xcAjctFvIyTTLt2qbROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c3b572b.mp4?token=VEmcCgnanCV7JCkIzdbV14UKtZWGe8r-LMur-fCjN7I6kxkSHug1H3SmN54h75UzaJlb--TRp89xrwknT8T2NSooRF4oSHpNTV6EseQJac3he2tBeBaZa67obHZx0O6T96BpEQIFCsmVqywNeNU6fE36a3qlfWmxoL4B39A4VZJE-iUCJjwnbYz5w-_qShjP6TRpjIinDHV6Zsq1wh_hy26jMHJuf-Dv8x0LFBGi0iZynR0e_kBr1-4lvVCb-202SbY76TemOM9oMqvz2eBWdp1AVOunFdZZyESZw6FBcxZ5N_Cx0MmUR84U-asjEIlJ30xcAjctFvIyTTLt2qbROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای یوسف تیموریه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/83352" target="_blank">📅 18:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65680f7b4.mp4?token=N4I0gYustyZxZWEtDXYVlr5AQkhBFvC3QQPwEAzHZotyy7yhlHm1MCFH_qZfr2PPjnrozSWvD0YK3_EoGst0q3nGDO9Yt58v3jTjZuOLutighE-MogLbWn62wx_iiDCindFet4MZRjBNJwjd0uUSaPBZ9nkd9phnaK8codR3vdkTmJ_XNhentz55mjt6uThxV7UecHh28B8lMGbgRmGuwBce1ZssemsK23cCcfic_C0QLn0DCOgoznOwl9Z2fGgVZTiceWyW5W1DM2BQGQ-FD3rglcH3ZE9VdfAzkRWbJCRhbz82iLH4cwwI6u4HeERNdpzwmLG_PwGrxxQAyYC1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65680f7b4.mp4?token=N4I0gYustyZxZWEtDXYVlr5AQkhBFvC3QQPwEAzHZotyy7yhlHm1MCFH_qZfr2PPjnrozSWvD0YK3_EoGst0q3nGDO9Yt58v3jTjZuOLutighE-MogLbWn62wx_iiDCindFet4MZRjBNJwjd0uUSaPBZ9nkd9phnaK8codR3vdkTmJ_XNhentz55mjt6uThxV7UecHh28B8lMGbgRmGuwBce1ZssemsK23cCcfic_C0QLn0DCOgoznOwl9Z2fGgVZTiceWyW5W1DM2BQGQ-FD3rglcH3ZE9VdfAzkRWbJCRhbz82iLH4cwwI6u4HeERNdpzwmLG_PwGrxxQAyYC1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای یوسف تیموریه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/83351" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=Zvo92nTQBDaaioBdeSdEezWsecIoAUn9gQE8BNmvLF7dAJ5VCynmPuv4M7_1jFDJItX9yRB-Ggf4caxQc__RxXwvZd5FPQYshSIU3wRspWAf_O8u2GfyCLcBP9aGZjNhEKGwyyFrdO3a3cuZvG0o-H5eLqd046DBrZuaKf2qjbhrYjgXYGP6sideFFXr39Byj6pijXMsM2kmTl3dsibqaZpGoE7lfoeyIQcCFlV_E2tEo592mN_tyknbYxLe4O4_0BChNFHtac2ZIDzebmxsfMJiOnmuxAj2bkyVzijLc-HjkpWONSmjEd-IPZDTh1ADREoIrz1cwexb6zT7bnfbVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=Zvo92nTQBDaaioBdeSdEezWsecIoAUn9gQE8BNmvLF7dAJ5VCynmPuv4M7_1jFDJItX9yRB-Ggf4caxQc__RxXwvZd5FPQYshSIU3wRspWAf_O8u2GfyCLcBP9aGZjNhEKGwyyFrdO3a3cuZvG0o-H5eLqd046DBrZuaKf2qjbhrYjgXYGP6sideFFXr39Byj6pijXMsM2kmTl3dsibqaZpGoE7lfoeyIQcCFlV_E2tEo592mN_tyknbYxLe4O4_0BChNFHtac2ZIDzebmxsfMJiOnmuxAj2bkyVzijLc-HjkpWONSmjEd-IPZDTh1ADREoIrz1cwexb6zT7bnfbVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g22
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/83350" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqjj3FDDhAyEk77HEYpXldu9MdfdvGZrb3x1OkrOajNxjDJhs2MUaGLwLgHd4WnwOHU_UUjTHX6ZwOagyJSkKsUoP4zSG8WG7p30YWL8AXwrrIK_0zDEOG09XUV1lTkbMAEfcfJebu6DKx3afKMXea4YypL6Shes_oqfurR6YbAkqKGNTP-O7jROivB7jSoiwWPXIdG4xmduZOQtZ7uvj-i_IvccIVeqJ4Q0PdZc9R2wkQK0VbUKa1WIQTCdY6R-WkK3pVGsbjr0jbhL_a-Qa-eM8eC4JQ5gab2DA3q9EbE4qO0VRSeCFJVojWHAFa9wBzPnadnn6yQDOc5KElXjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
مجتبی خامنه‌ای تو چند وقت گذشته بین یه دو راهی بزرگ گیر کرده و سرو نه یعنی ذهنشون به شدت درگیر و مشغوله چون وحیدی می‌گه بیا کل منطقه رو بفرستیم هوا آمریکا تسلیم می‌شه ولی پزشکیان می‌گه یکم اوضاع خوب نیست بیا مذاکره بازی لطفا و حضرت آقا برا همین نمی‌تونن بین این دو راهی تصمیم بگیرن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/83349" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قوه قضائيه :
علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/83348" target="_blank">📅 18:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=XOnXtwBOkSi7Iaw6uAfmXinX7foeuFxjxlg8UU10EqLC1mGOHTztYEiEOrXajULwXxeYvymyaPV1rHEYUh0ixIyfeaZtzVH1tRXpTHbombU4RGmwr2YIc9YHd_vcje5sGcTbapAn_XvwM1xz3DYMRco9xHIcp8z4A4X7BqnHjkMOA0_CRbjtMFBJn1vXolF55fkOM0XRSGl-bQL9SnSLMKiXgAUBNcWtYhRGUcvbmM46P_U6DdSmzXXgphBs_-W9ZkdX20qW1l-P9g-RIxbPdfskbWfnuvVG7HqI68M03rGo7QOBF4y9fZueySUh1mgwrWTliJ8gbzK3n8mDTFbA2BQgSFgcUO42mfTFEyChA0vs1Yneqv4ff0DnGJNGH0weiYjqE579ljW7AgINe7ocS7v79tAGlfLIIspgOhiKOSTIqagdqKUMQcapGPWw3pS67d3JSeTu2TFXpTYaj63MZVJJlUNxc0iwsi4z2bdz_6md6tEDzsTvP-zy7BMrn7O7Xh4sYt_cgIVb793mGd8suCGtKTB2DyXQj9LplCMruqoigE-nrwTJrIkyvKjM8J0f8xW3lCtE4ZSfRbw_fEoA8IUrWQ6H55eXRjlZBxilP2KO58hpkQWnm6HqRgALbwq3U9O_AdsagNtgaOS6_fNVEPjipxlV0o_Q7KrGCySgs5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=XOnXtwBOkSi7Iaw6uAfmXinX7foeuFxjxlg8UU10EqLC1mGOHTztYEiEOrXajULwXxeYvymyaPV1rHEYUh0ixIyfeaZtzVH1tRXpTHbombU4RGmwr2YIc9YHd_vcje5sGcTbapAn_XvwM1xz3DYMRco9xHIcp8z4A4X7BqnHjkMOA0_CRbjtMFBJn1vXolF55fkOM0XRSGl-bQL9SnSLMKiXgAUBNcWtYhRGUcvbmM46P_U6DdSmzXXgphBs_-W9ZkdX20qW1l-P9g-RIxbPdfskbWfnuvVG7HqI68M03rGo7QOBF4y9fZueySUh1mgwrWTliJ8gbzK3n8mDTFbA2BQgSFgcUO42mfTFEyChA0vs1Yneqv4ff0DnGJNGH0weiYjqE579ljW7AgINe7ocS7v79tAGlfLIIspgOhiKOSTIqagdqKUMQcapGPWw3pS67d3JSeTu2TFXpTYaj63MZVJJlUNxc0iwsi4z2bdz_6md6tEDzsTvP-zy7BMrn7O7Xh4sYt_cgIVb793mGd8suCGtKTB2DyXQj9LplCMruqoigE-nrwTJrIkyvKjM8J0f8xW3lCtE4ZSfRbw_fEoA8IUrWQ6H55eXRjlZBxilP2KO58hpkQWnm6HqRgALbwq3U9O_AdsagNtgaOS6_fNVEPjipxlV0o_Q7KrGCySgs5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوباره شروع کردی که شیر
ترامپ:
ایران با شدت بسیار زیادی مشتاق به دستیابی به یک توافق است. آن‌ها مدام و بدون توقف تماس می‌گیرند.
من توافقی را که سودمند نباشد، نخواهم بست.
ما باید توافقی درست را به دست آوریم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/83347" target="_blank">📅 18:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=JX-jcPhqmNpEzwgEUH3BabS7KYy0LBdRmsjQWYjss3EpbTwvUbNc7nSQfZ_TzvucYSY7651sDDRjWBuX50TmeJVtT-2HR2UHWaEd4Cw7Dj3FzdkBtDu6xJdsuVMKDx0_tzGlAdcYNR14d9iLExI08SpJmMlvHu0sX9IIed88vTKskW_90ABq1dqlJN2huR5CmvQBtJwLdeimf99O_tbdJ8vYLRcW5uGGWmzQuLFphRohCifAbbmPy-9DFGuK7Ka21xZ6hCNyD9V-qKjwRFBTzRiVELwPm2AcrbrWen0BHthmO6tMeyrMY4R9RuZNuoinXUDNu-eheWOJ-M7llqWo4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=JX-jcPhqmNpEzwgEUH3BabS7KYy0LBdRmsjQWYjss3EpbTwvUbNc7nSQfZ_TzvucYSY7651sDDRjWBuX50TmeJVtT-2HR2UHWaEd4Cw7Dj3FzdkBtDu6xJdsuVMKDx0_tzGlAdcYNR14d9iLExI08SpJmMlvHu0sX9IIed88vTKskW_90ABq1dqlJN2huR5CmvQBtJwLdeimf99O_tbdJ8vYLRcW5uGGWmzQuLFphRohCifAbbmPy-9DFGuK7Ka21xZ6hCNyD9V-qKjwRFBTzRiVELwPm2AcrbrWen0BHthmO6tMeyrMY4R9RuZNuoinXUDNu-eheWOJ-M7llqWo4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش کانسلو که کون خودشو پاره کرد برگرده بارسا و الان نیمکت نشین یه کون بچه ۱۸ ساله شده و طرف هر بازی میگاد:</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/83346" target="_blank">📅 17:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پوری دوساله داره آلبوم تمساحو هایپ میکنه، کاش بعد ریلیز باز چارتا دیس بخوره فلاپ شه مثل فیل بخندیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/83345" target="_blank">📅 17:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترکوندی شیر باهوش
مدیر سامانه هوشمند سوخت:
خودروهای نو شماره بالای یک میلیارد تومان مشمول بنزین ۳ و ۵ هزار تومانی نمی‌شوند و تنها ۱۱۰ لیتر بنزین با نرخ ۱۰ هزارتومان در کارت سوختشان شارژ می‌شود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83344" target="_blank">📅 16:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83343" target="_blank">📅 16:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/83342" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83341" target="_blank">📅 16:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmTC0ope4a4gtIqnhcDrZgUg3LDoQG1BEsqknE-5jrgiGLdsZv7hgD0Wq100evo37RrTLBB0giu3GuoujTeJrDgmyG44VI6Ngwwh5MzNB4ZkAkwXsSO9cNItx5Se5EO-mysoda494F-UFPzV1n5hqCE0TtdqNdCzwcFsNRttY_urWK94yhrHUrKjJL-LKdlQA0oQcsOStNiBn7NqURSY2kWax2HoplR2dmX-cWu4Gmz8pnY7JO0CezCNqPFCYuauoyJvSxSoo2-U4f0rKC1sE1BUNqIBnkkU1a94mbWVPv2jTpwZHMhNcQhGbF0svzZTHKeDR0b4g9LqGdqr3Vwq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/83340" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چرا بس نمیکنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/83339" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQplEcNqH9UKbtcOGxBnMXz0eLRjcf1-VrS3ROsL7zy-4Pi7txUoSOumOT3-lJAppzVerlZV_r2lAVpVfhMtyFXoLTp0BM-51Khxae9T8vvMCL_nzyP-uTtNrOVMTA8gzGKVoUnyx3F5hQT0_itYtHj51xeC7Fh3rQR_C8thJapMZ-8G259yS1AAxn6jkoBEDEpIA8cCDJeozxyvQQmvtiUczTIdu2r-zv5nhcmgzo0v_Qa1T2S74QpWcBRuT3AnYnbPziFSoSa8xJ_hYRl1AL6DsloeQrHwjtg9_ESWilBBAS79pzHQ-ub1oP0BeSarggfokg6wwm6_jB6N17Dagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا بس نمیکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/83338" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeKs9jzqUzd1cfMo495mLk7c9DvBFEGq4HWpOMLGckuz8kwhyww-3-MuIsoGedUXtpAMe9XVEu5IPz_fvMSHRr3VS5ATVfBZ5EJjKh4iyo4RCKUYcw6lPTYJDVspPfihrP3jiEugLiZBKKGiUZKRmhlORCc1lNkNMpLVyL889vNAzCWNNCXpkbda__Seq5fSzzEmnijvy6QISaN9B1iXo7xjzBAmeBfCUa6PgvZ1NmTBXO-ESkpC96aInPkCbK1KyaYWM90F9Au8p8VaUSjyrvYOAkc6HfY_LEwKAgSBCRstMsfcZ-e5Iv5us4h8FM23ENYtyMnrrFianOMWnZDc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم حالم خوب بود تا نوتیف اومد</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/83337" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این یارو کیکستی چرا اینطوریه، میدونی داره چرت و پرت میخونه ولی کیف میده گوش دادنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83336" target="_blank">📅 15:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJaYDNRa7diA6mv9GsqX9VKd0T2rtsf-j48lrjPwWrWAe4022U1tsbWljPsndVqoMw1cqZZm5Tlr0Dc2Wz1io0XjA6Iz3caqgzEuVxVbo6RBszZLrsaGim12GHmuDyHd7aKI3pBr06eSiLe8dFkZsTqUlV3ISZZwT1pOjdIbwwSX7lIxh80xuowuTWVtESfhqyga19dgoBegm6chEBEdHQQnIZzwmcQE8TBeoKPjqlBJRpf5fUsqHF68if_7tqTFDbKZq6pG6v1hgUkKGLVdlL4ayhJCF3jUDy6lNvGme9IB_g1iyamzsY4pgTYxB-P52ctcc4AZnj7UqBsI4Yv30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/83335" target="_blank">📅 15:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83334">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83334" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83333">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FARov-VDuCalKoCEUzI4QDFV-Fiz5bKg4ou4MyRZhAVfnVBeQVvljZJZ7EVhwoU5AIWtK1wMZyoSTXCKyusgH9j5qYEl0DQ2s27M7LPjof2Lys5vGfyDSJSJUxvE-7lS9Vt_CDzjSMkuB4tQ098Yq27o5z1TcWgtBLdF_5ecFADA9vURFb0X8HotDv49mvQLyxi3Ba-670GYcIDGiV0REfMMo2xOiCGOXS1v2O9ybK6WG9UBo9MoCuLzKSQCvyP3tldA2mwexWspspO56DnMLgdn4kxlKLVdm652V87AYpjPuGfhw-C-5ZjySiWqpONw7IV2kTwhM4pjvJK7D_gocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:  "نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83333" target="_blank">📅 14:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83332">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=sdvnlpKiH71ZZ7X4iczBTiG0iqQNRe2-H4_j7y4ppABVCKk8jj8R-kORD-FdbIpZzIAO3NfyZIaypuTn0hQ_8YBEqrFGsDH5Iab9FKhfdrMw_S4T01JnzgsMOiJ4AYGh-vm8qksQxOU2NfpIW22lUX6jZ42O3dtHQ_t-pTLWbRhIf7DmqMQ74NsITB1ZucnB18mIQGK30wwOMoDpfnd05q5vrYuNC6EmS9Ou5fLLGLA0jVhAtuzTVJSneeipuFJI0Xq5w8dFS6ntaKxZR2vIuAH1DnVBfM3xpNZuh2YJnYCMkXwz8uwu5ujpHT8vrcNMiOyLdXUy0voFwaRSQzYRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=sdvnlpKiH71ZZ7X4iczBTiG0iqQNRe2-H4_j7y4ppABVCKk8jj8R-kORD-FdbIpZzIAO3NfyZIaypuTn0hQ_8YBEqrFGsDH5Iab9FKhfdrMw_S4T01JnzgsMOiJ4AYGh-vm8qksQxOU2NfpIW22lUX6jZ42O3dtHQ_t-pTLWbRhIf7DmqMQ74NsITB1ZucnB18mIQGK30wwOMoDpfnd05q5vrYuNC6EmS9Ou5fLLGLA0jVhAtuzTVJSneeipuFJI0Xq5w8dFS6ntaKxZR2vIuAH1DnVBfM3xpNZuh2YJnYCMkXwz8uwu5ujpHT8vrcNMiOyLdXUy0voFwaRSQzYRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:
"نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83332" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83331">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/83331" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83330">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83330" target="_blank">📅 13:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83329">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71116434dc.mp4?token=MgDUaqTNR5j3sjs521HKy8a7WujmbGzaUpzpSUxJKI8NQO7d16oAyltWWpOYZLu4kDRoklqjppa_9z0u_AOFXA-etKjhCmEKgHahmjwdjkOUJveE_4dpiEeVLRQBsk-Kf4h6kxO_EZoQrCQOgcZRIw8_dv3QSSrqzfT0kMBe8mm6wI6ZmXmrtzW8AcqBgUsm8V6N2_xqeCcLmtW15W4Hb05Gwi-rrm_TSTA1sjNFHb2QV4sLJn_TLkDxVKnmAtTqOsfY3uttSvHFYyH1jHg77a9fm7iDYjom67QUYOFXBwV9O0be-VOxXJOiOE0StxS39nThRWlMYfCsQpH8fYKuU3_U9IEBRIjbshb5RAHGpZS9g_v1pCKNsobJBJbwJUHibtUy3CBsv7O1BUJ9KoCV96MMCYHWWy-KRdJFQUjGELazPxNMnM2FOrBBMVYj0qHRyW55Uy5Q0bjjYOu2DkfLy2gpyyqNkQ7rGmHbv3W_USmc0ghNkJGKAglq6fax51MKlsOsgPIVKRRLSfkSP-IWS6dEp2aWPqDJDkefm0QAdZiU5tsleARElMDI8H2GTgl5yRHiUkW0rnfjo1DH3I56hqzUXFDcLmX50RXVasW8OrQQyYWwAYebbMh7a5ouAMQDnia1Wd449DrFngyfyumgTDL8Q6RDL0ygrymJyMMNrNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71116434dc.mp4?token=MgDUaqTNR5j3sjs521HKy8a7WujmbGzaUpzpSUxJKI8NQO7d16oAyltWWpOYZLu4kDRoklqjppa_9z0u_AOFXA-etKjhCmEKgHahmjwdjkOUJveE_4dpiEeVLRQBsk-Kf4h6kxO_EZoQrCQOgcZRIw8_dv3QSSrqzfT0kMBe8mm6wI6ZmXmrtzW8AcqBgUsm8V6N2_xqeCcLmtW15W4Hb05Gwi-rrm_TSTA1sjNFHb2QV4sLJn_TLkDxVKnmAtTqOsfY3uttSvHFYyH1jHg77a9fm7iDYjom67QUYOFXBwV9O0be-VOxXJOiOE0StxS39nThRWlMYfCsQpH8fYKuU3_U9IEBRIjbshb5RAHGpZS9g_v1pCKNsobJBJbwJUHibtUy3CBsv7O1BUJ9KoCV96MMCYHWWy-KRdJFQUjGELazPxNMnM2FOrBBMVYj0qHRyW55Uy5Q0bjjYOu2DkfLy2gpyyqNkQ7rGmHbv3W_USmc0ghNkJGKAglq6fax51MKlsOsgPIVKRRLSfkSP-IWS6dEp2aWPqDJDkefm0QAdZiU5tsleARElMDI8H2GTgl5yRHiUkW0rnfjo1DH3I56hqzUXFDcLmX50RXVasW8OrQQyYWwAYebbMh7a5ouAMQDnia1Wd449DrFngyfyumgTDL8Q6RDL0ygrymJyMMNrNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83329" target="_blank">📅 13:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83328">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=NYBxMRvT_dWnrFPCAPpNkDMUPmw0UmU1BD1vwW2ZlPcHEyTw_VvID5wzrB4ouhxy2lv04FAnnSTTKwRXcFIgg98QmuJ0TKU7B80D1YDt7x08Kmjsf0YV_c3vVDo9xi3OjwwgcrLhjgKiZUObb1HVoRNA6ycgDejFxA7CT4bh_bj_6f93fDfDGDfxUirSZMNSSwn27Iubj96UOc-i6tJNNvjErsdK33hHkxaxCaGA_efs5Jh-znU2MW-3QcK_PhkpFotRZT7-YGF9-o9ovlxwKVd_3ZG5KMRSd0wuY-ZyDSocmAJlhx2Pv9WFr1Sf_ePDqwDlAA_7sWWaLN-3CHclLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=NYBxMRvT_dWnrFPCAPpNkDMUPmw0UmU1BD1vwW2ZlPcHEyTw_VvID5wzrB4ouhxy2lv04FAnnSTTKwRXcFIgg98QmuJ0TKU7B80D1YDt7x08Kmjsf0YV_c3vVDo9xi3OjwwgcrLhjgKiZUObb1HVoRNA6ycgDejFxA7CT4bh_bj_6f93fDfDGDfxUirSZMNSSwn27Iubj96UOc-i6tJNNvjErsdK33hHkxaxCaGA_efs5Jh-znU2MW-3QcK_PhkpFotRZT7-YGF9-o9ovlxwKVd_3ZG5KMRSd0wuY-ZyDSocmAJlhx2Pv9WFr1Sf_ePDqwDlAA_7sWWaLN-3CHclLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران داره هر روز ۱۵۰۰ سال نوری میوفته جلو از دنیا
یه پزشک زنان طی گزارشی گفته دختری ۱۳ ساله رو برای ورم شکم به مطب آوردن، اما معاینه نشون داده که او هشت‌ ماهه بارداره و ماه آینده باید زایمان کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83328" target="_blank">📅 12:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فایننشال تایمز: حوثی ها با کمک هوش مصنوعی تونستن موشک بسازن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83327" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de166635f8.mp4?token=GUcWmC5GkgQ2d-BCPVaRFnqbGB1GMDMw9z3YQeMVZWJ7VhrK6_fHyVJqr8rFfT8yEuXxZb4DFYzBvczEsM7sj7_3rHDXRy7DkTZCRds0ATogSBGmCtUN7fSMmKQu3yQ3IyxDVBsS4uwAegcWSyKN1g9w351paNIuvDqaBddBv3Hm4aYJB14PcYH7QEUbrLa_J-O93qaYIBSqt6PbjP8e2FpjwmBT8ljmO-NvqOaUSkkJNvepXDFNTS15ld92evCTe5rG_8HffnSg4A4AzrQftvaHdEUKQGnr5QJSJqf5TBdEHWHfGl-FuK93gP4p9HjYFUDjI1VHSV1yBOTkFIkSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de166635f8.mp4?token=GUcWmC5GkgQ2d-BCPVaRFnqbGB1GMDMw9z3YQeMVZWJ7VhrK6_fHyVJqr8rFfT8yEuXxZb4DFYzBvczEsM7sj7_3rHDXRy7DkTZCRds0ATogSBGmCtUN7fSMmKQu3yQ3IyxDVBsS4uwAegcWSyKN1g9w351paNIuvDqaBddBv3Hm4aYJB14PcYH7QEUbrLa_J-O93qaYIBSqt6PbjP8e2FpjwmBT8ljmO-NvqOaUSkkJNvepXDFNTS15ld92evCTe5rG_8HffnSg4A4AzrQftvaHdEUKQGnr5QJSJqf5TBdEHWHfGl-FuK93gP4p9HjYFUDjI1VHSV1yBOTkFIkSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی دیشب زئوس به مازندران حمله کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83326" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJDtqhxFihYdXMDzwFh0nP63eGgF2dgOsEpEFRAnH5Njdz-Pnna3IqGQubhxjiVj8Fn07Kc0AsNKYdtdcBpuy59Sw9LIWQgIbb9Rd5Paj3A-vAGOOJh7UncDylq5Cxg-Xt8IXzxQSUp27G5btoleIA9CGKPQx9HFtFFUr2BTHxxT3GBkTyALOqgv7Ryo2aSw4-mbrfrJOgLM5et6dBynb-Z797v196dW42sc7MDZohTBZlFBy6_H8q6sCoEyAQ-TAhu5_azIgYfda1EFSAiTTwl4_Dhq0GS0ptdrEGHIskq2BV6CqjQ0L3F0XQNvC1vrIFocsB_6v2B4Aw1BBNOrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه حملات پهپادی به عربستان رو محکوم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83325" target="_blank">📅 10:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gySUyzBI5cWHDjNFqQPzm-HskOJd40kBynZWcfJAPo7EkSz_bzmH9RzYlALrWN0Cm_j8yk42U3Taw14bGGrbmuwv429_aqkXE7E7SNimu98aTr5oCtvI4tVgX1pfUyYExCB6VlgtDm2GAZrag7kpoS6mNdm7dEToNYT8baY-dL2uPzGO9JbeBUIW-6W6Y56oKdaVm89d4Dxl_L19zI6cH6mNmG5I6pnmrYrywdGWCFh8gdRT-paF5WGIMQwV3X8utV4oFeDgCIVf11h3tLgD9GpmDj8t8CbWV-ad_JMpC7diQSID2qkvoIKKz-vEM3R2KuzICk5yGPzbs9UeDCMxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا تا چند ساعت دیگه مجبوریم یه چیزایی گوش کنیم که دلمون نمیخواد دوستان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83324" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP4xQqoP-ZuWKANNHqmGMtm6_2Pb9y95LDfS6n9xs4fdZfgCc0j7AutZuaIH5G3iDVTrX_6S71Z6JWJfud2ouNs7KoipvM3yXTwSi6k7WdtQ2Ipqz5dXRgfAqXlCt4OCAlHexMjMj26ULJsN02-yEfaKvxXsRbNyJCHtdUgg2Wj8b2vfdoSrcP-l-9mHMpJX-4sH-G4Bw0T7Ci8f3Qh9XLviBEeE7pH9SXzBy9UzL4remNgWLDHtYRgXBL-8c2BPqQsLPPQBLQGF2LWcIP19fuHPjhD3ppehYbF4gx_fUiWc-0cky72Va94AbZDdlcPf5avLrWda8LvidqRndc86xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
منچستر سیتی
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 -
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد
🏆
لیگ برتر انگلیس
⚽️
🕔
ساعت ۱۹:۰۰
📍
ورزشگاه اتحاد
✅
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
💥
دو غول شهر منچستر در یک دیدار حساس و تماشایی مقابل هم قرار می‌گیرند!
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر سیتی؛ مدعی همیشگی قهرمانی با سبک بازی هجومی و ستاره‌های بزرگ
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد؛ شیاطین سرخ با انگیزه بالا برای یک پیروزی مهم در دربی
🎯
انواع آپشن‌های پیش‌بینی مسابقه
📊
ضرایب متنوع برای انتخاب‌های مختلف
🔥
هیجان دربی منچستر را از دست نده!
🌹
کازینو رامسر؛ جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
R22
🅰
🗣️
@C_ramsar</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83323" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83322" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83321" target="_blank">📅 01:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ناموسا این آرسنالو منحل کنید، کیر زده به فوتبال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83320" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83318">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز چنل:
🟢
1.32
🔴
1.26
🟢
1.5
🟢
1.3
🟢
1.34
🟢
1.53
🟢
5.1
🔴
2.4
🟢
1.41
🔄
1.86
🟢
1.54
🔄
2.52
🔴
1.52
🟢
1.58
🟢
1.41
🟢
1.83
🟢
1.4
🔄
1.8
🔴
2.8
🟢
2.32
🟢
1.5
🟢
1.5
🟢
1.925
🔴
2.4
🟢
1.4
🔴
1.4
🟢
2
🟢
2.8
🔴
1.8
۲۰ تا وین
۶ تا لوز
۳ تا ریفاند
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یعنی تو دنیا کسی خیلی جدی علی گرامی گوش بده و باهاش حال کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83317" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83316">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqjn_DiPCuI_NZnTxk0pC_Jbg-xGifdNV_GffIafuAMolhKOMz8OHa5xg6vpsJg676hYSF9201wskUNfpHR2r_zOTRrBBb7QYB2nYiMtzuWuHf9sPhcbjt0TCFAEDvz6cwjz5zqe9vZ3MtCbdboGX4Q7AtZIRIXLOrSLtp1ff1CLrooJpMobzZL9rB3mq9OS2lFu9JUw4IegL_urUxbXyuAZ_BNMxxcXgemFc48penMXOIVwnUCk21-prYXjIjAPzn5LI1eeKP-hwMGTFvqpG-LrQawlzK1tmdEVneTv4DBECgKhaPeNzVGSWOgYqfRLrmO3WgsO-DaohgLeP7puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این استوری هایی که از علی کریمی پخش میشه ۹۹ درصدش فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83316" target="_blank">📅 21:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBtOsowJO14JaN6Ww4O3OfR6Y6F3a5Q3oYW84NVom8k0w62dPwcVH6AmnAM1hOorPCyqPZNUpJVevhYzKiKwJNHlkYkbog7v5rcQn_Htn2NHn5sXxRMsqBnfykaHkkfxlBBdDH8q3KXAIhJhSLtLgjAmeJRjHiDqZaO2_KRWgdXnrSAODnm5XRRH95TOR1svou1qersU56ld4ry9ZqlfBlpaEJrdMP6SpC9tbW6IfnCNhXl9Oc4Hy9PD52rfD0x2Zh2xcqvtME3PbIzEhQzjn-dpa6Ln8Kwg95RWaOf6ietFD6BQOdSp2FFd201Z5oT2CW1TKstNgD4R5fq4eeZtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83315" target="_blank">📅 20:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=QaLV5jJRjf1Z9p749BbLk4wn-xWjbcB02D2h5dJ2Iym8G30VwGyUq2dwhS_tabFRoRH2BgeOLXgVpqVcS1DwENDzg3z6Z9MpIS5IaJJbRwpf3MBR8u8ZAUlG4bl3FV5aFb2F6bkXjb1tvZc7gqiQkb6aXilv3xvUQYz057tyA7JN3sTLlgv0fm55jauY8JNnGIt41_NIhxaKMjEvb3epmi3Avohw_RexEo7kKAck8Cx0ansfhQ3V6yjSewC0bCGr7mp2Bltdp8OpdkoqgAFpar4wh7Q5-kfYGf5miiVjMeG6bAZnjHTDo3yAB_U3hQUOmo0IYD-LZ4d2HA8rCTPP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=QaLV5jJRjf1Z9p749BbLk4wn-xWjbcB02D2h5dJ2Iym8G30VwGyUq2dwhS_tabFRoRH2BgeOLXgVpqVcS1DwENDzg3z6Z9MpIS5IaJJbRwpf3MBR8u8ZAUlG4bl3FV5aFb2F6bkXjb1tvZc7gqiQkb6aXilv3xvUQYz057tyA7JN3sTLlgv0fm55jauY8JNnGIt41_NIhxaKMjEvb3epmi3Avohw_RexEo7kKAck8Cx0ansfhQ3V6yjSewC0bCGr7mp2Bltdp8OpdkoqgAFpar4wh7Q5-kfYGf5miiVjMeG6bAZnjHTDo3yAB_U3hQUOmo0IYD-LZ4d2HA8rCTPP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک:
حادثه ۱۱ سپتامبر واقعا وحشتناک بود چون عمه‌م بعد از اون حادثه دیگه نتونست با خیال راحت با حجابش از مترو استفاده کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83314" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83313">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVdDPjhW9ayBkcZp-FI11HknyM-_uqhGnBvteHSxgK6evZY4u9mpLEFSssqzSCUCGl4miq4EvNxg4E8giBM_MzW6bnWhjSvVFOUtH9KikY-pK6X8dN12UIBhAemm0pdcPpRA4GBUVVZjnnGJxU9AodYSHTLhdt7QpXHrkV6ialnNYmI2YBJ_X6E_-IVb28DP6clwius2gAgYncz_4c8ZYLPeW_gjRz_SHGtWqZTsLWnCfBMygogBBIcINa18WMmki5OQdZ7WsOMBCnt67w00_ttu46TGEk7gvYVuZuUrWlap3GSNeTXf9IuFnCA_LR1JFIa0h1HeXpCSomfIS6yDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرو و هیچکس کال کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83313" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83312">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXs2KWSeLd7tHwoORokh1nD-JVDfnQVYN5-P72S9tmkewJpYGpRcP6JdQdf3RMFmidjitwGMZyeGoACJ4Nrj9ffZR0VFG6CRwn1Ijeh9n_So4Yt3XklKOon4Z_WlcIK_6PYg4JNkR-EsTTUrtvjJmQshYSGUAfYXsiuPRO7XGcmYKS-UMPnL7It88bhohtyqFqV-wX8ALVav6bsaMob4jHSsIC1JJuGoorks-u3KzHkNiIcXy2k4nG4jLpmeLWmBFjmJE_P3GbUKuUZWLU4n5audXMjBDSZgcDORY5_79I77h5UwcuXWq3u9fo1ZI1_7wgxQpvg7-fQ6BjbS8Smccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تعویض طلایی بت‌فوروارد
🔥
🔥
با قابلیت «تعویض طلایی» بت‌فوروارد، پیش‌بینی خود را در مارکت‌های مربوط به زننده گل روی بازیکن مورد نظر ثبت کنید. در صورت موفقیت پیش‌بینی مارکت انتخابی، برنده خواهید شد. همچنین اگر بازیکن انتخابی شما پیش از پایان وقت قانونی مسابقه تعویض شود، پیش‌بینی شما همچنان ادامه خواهد داشت و به‌صورت خودکار به بازیکنی که به‌جای او وارد زمین شده منتقل خواهد شد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SUBO
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83312" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83311">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e048011808.mp4?token=lgW81F6hQhnmW_Rquuw4y_b4xWM6CRE3PLFg85G2qCOPyMi5vOv2ERlh7TGrqrlmsI0xd-T_hUx3Zp1LfuilbS5P0oy5IGJI0XLqhGIJbdhfEbCn0r5qTv9GkJOwgqX_cWsTDYVdyj1GNt-UTI7mMjk8hc203fmNJcKzD9LKSdBAXui29a5ZDMP8aB8BcB_1vOBvMgo3L3K7btwJhqegmFpEhhPPP6gTq5Wx1LH2e45KiNU5Lp9F28Luq6mlbAHAvbUmoI3rVsGtyvPoVpVIcLTWiqQPSG-ivVSuq4AYDZXHDUxlrjJVNwHd1Bz8kQmJ__ISCjsXTCFSOYs5dzSCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e048011808.mp4?token=lgW81F6hQhnmW_Rquuw4y_b4xWM6CRE3PLFg85G2qCOPyMi5vOv2ERlh7TGrqrlmsI0xd-T_hUx3Zp1LfuilbS5P0oy5IGJI0XLqhGIJbdhfEbCn0r5qTv9GkJOwgqX_cWsTDYVdyj1GNt-UTI7mMjk8hc203fmNJcKzD9LKSdBAXui29a5ZDMP8aB8BcB_1vOBvMgo3L3K7btwJhqegmFpEhhPPP6gTq5Wx1LH2e45KiNU5Lp9F28Luq6mlbAHAvbUmoI3rVsGtyvPoVpVIcLTWiqQPSG-ivVSuq4AYDZXHDUxlrjJVNwHd1Bz8kQmJ__ISCjsXTCFSOYs5dzSCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چی بود
تو سراوان نیروهای سپاه و مسلحین درگیرن بعد اهالی کوچه دارن تماشا میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83311" target="_blank">📅 18:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83310">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu4Hsvshr1UfTh3DUfiUcxsI67trD1Ji3GAYR3OaYbyhNDkfUOe4Fl9XN0oWK4IRTlFbg5nMbzjF_CPZnECarBBgtPfnNVi3v0MKjOKzSQRIAz-Nq9fnFX19flfUcZSlR95CpYGlIdzOlWZuRbAKdcVQ57t-r_N0Gys6MadHPfs7TfSfCX8VRP8SO5qEskW5vn8ZC4a2v4_ntvjegG4ZM4BFRf8Wmo-odDjQdQ1EabYTynXs89OepzVyyrYD-saGnguf15ZJSAVPfFxVpmDWVHHJYLI869ljXoqJX1EdBSpiayAo2BRrKBBiaZeg7j1PG5x_t7Qqv7rjUE5ORQFOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیت مپ این فصل دیومانده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83310" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83309">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AND1qDygyOIhrLEPQpUJPyB3wIhatqobA4vwLT673lUESaIaq5qcioTMQhpb5WJWD4x2I2eAkH4wugE8PMYvQp6Ou0BdUNvaUqtK-SoMtz97muN6rQXXHoLwnJG2Zsu6nLgKMGhao1hwwmWSJHePJWOQqeirYMLmgTYsJQkWXo6Zt4jhX9FNoT0dCQaIocfl5hiM_-8_9nEo_pPTjHjL09qhrQL8XckPn81188l0lPpzDzizMXdk3MVayq5KP5vJ38DoUttTWNwORoZ-WhjomiK5AgicB9ynWJiI75AgIkywx_4gUu_GjxZiHmxQPsPcIkohF6aNc3BCLbuIqsbrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83309" target="_blank">📅 18:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83308">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1II4LK5_xpMYdTsEKlXkfnau1GlO0bjYqIkELzOZSS4vFtATMaMv89uk7R9_Z9uUm_evnTLJpW1_8Zb7VSX9_Idoac2hway58i24st_0QVZ0ozlwGn20iHS2hSYUbStkWhXmx60uTF4Hq6d4AQ6E2P6DwzjgvIfn3etom_DFCBvhK5Rb3iY9rCktXHSTLmwInJzgpMUDNiMLcc9KVRIDazJwrDGh5S5npGzZ38qBkgeqXv4EnqBZYksSv8sx5kjfDZRDsSpuEQXLvrL6z3qez1ACKgQDJe52w01MZLFlA9BJyuxvfINNfBchb-3vbNXREt1XoWnHvFq81A6HEMUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83308" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJF68dtRufnQhSZBob3z7iUdnL-Muisk6GBgy0KYzPWu_hH5eneeQlqYbAj_gp9IT0uVFOs-htv2f3pxyXDdniiKtifLCz9a1upfb_15JO2YJJSauXa35OH82EWvyhN4QO1Ynm98XDREjo82aVrHT37MPPsqBARWCNRhlsItYbYdnAKp_X5zzwfK0WSEVXxdEYk6TKQEzzD5n6iQ3vibm6gDmEOvUyE_IP6nGF-X8cXJr4fvCnLfF-P_5Armh1o8-p3wP8PMFR5qtjmhPPCEek4mCUbhJPt8wt7P-61tLNBSAAm9ZUkkPITCKJa-Lbl8a4dzTAoDaFzzZq2ZD8QhGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJF68dtRufnQhSZBob3z7iUdnL-Muisk6GBgy0KYzPWu_hH5eneeQlqYbAj_gp9IT0uVFOs-htv2f3pxyXDdniiKtifLCz9a1upfb_15JO2YJJSauXa35OH82EWvyhN4QO1Ynm98XDREjo82aVrHT37MPPsqBARWCNRhlsItYbYdnAKp_X5zzwfK0WSEVXxdEYk6TKQEzzD5n6iQ3vibm6gDmEOvUyE_IP6nGF-X8cXJr4fvCnLfF-P_5Armh1o8-p3wP8PMFR5qtjmhPPCEek4mCUbhJPt8wt7P-61tLNBSAAm9ZUkkPITCKJa-Lbl8a4dzTAoDaFzzZq2ZD8QhGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله بلاخره یکی فهمید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83307" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پسر یه بار نشد توییترو باز کنم چهارتا آدم تحصیل کرده و سیاست مدار در حال دعوا کردن سر مسائل سیاسی باهم دیگه باشن، هرچی آرتیستو ورزشکارو بلاگر تاریخ مصرف گذشته اس افتادن به جون هم دارن از طرف ملت باهم جرو بحث میکنن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83306" target="_blank">📅 16:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83305">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f927888.mp4?token=uFHx2K3gXNgAtv7unHXX0CFEUZTXOSJ9Z5-331Yx0efSDlQ71ES-XRYev--BTeFVn5jlaoFbXhjZglfqXrALaYcGQ_HF0pbI_n2BsUHCPVVclEcUeoP3tveqILvSy-fY09X6dF-5K7uo31TD9Zze-m4B0PULoBjiUtMVZ4Mz_s2LQWhcEkhQhNhj_Gu1nj15cYN7TVPyVUn5hU6MMgfwYIxewld4U48I-HNi5PNZflT-2a4mK7ELpChFVWourKk81aiFtdq4FSSrtQC4bsF0SmdfeW4I17K1oUYf2wZaQG0qK4XZJ4BrUAgV92ydlAhF00-8t-FZkZe90Rt9PuDtcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f927888.mp4?token=uFHx2K3gXNgAtv7unHXX0CFEUZTXOSJ9Z5-331Yx0efSDlQ71ES-XRYev--BTeFVn5jlaoFbXhjZglfqXrALaYcGQ_HF0pbI_n2BsUHCPVVclEcUeoP3tveqILvSy-fY09X6dF-5K7uo31TD9Zze-m4B0PULoBjiUtMVZ4Mz_s2LQWhcEkhQhNhj_Gu1nj15cYN7TVPyVUn5hU6MMgfwYIxewld4U48I-HNi5PNZflT-2a4mK7ELpChFVWourKk81aiFtdq4FSSrtQC4bsF0SmdfeW4I17K1oUYf2wZaQG0qK4XZJ4BrUAgV92ydlAhF00-8t-FZkZe90Rt9PuDtcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی اینارو حاجی
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83305" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=v8zZMNVttx6DnKppC9qW6bEwpOiatximnuJ0b5Sqk2FP9BilloDFfaWLbSrspQv5sQ2dPbS91PlEcQQPl4WmHqt9XMoPanx6myPSfYY6pCzEZuOINRWvGBH8OmcZ_PYRzyD2lIs7qcyy4LgH2b8Xq47DFEBs09tweaLHxDEmeXW2aSpXNc1xGk2ahYjJjhB3d2juWK2ilprmE6GIMQPqiQEXjJALraUI2tUmKjcncFf1j_-dVPJI1zRwpzYCidgpGMvQTrwntADXHMbHohsIv4zzBa0dhh6K9OqMT6Jmp7ZHri4XHas2sDSHeQCORvnfzxu9l7b6n3aI4Z73WxM3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=v8zZMNVttx6DnKppC9qW6bEwpOiatximnuJ0b5Sqk2FP9BilloDFfaWLbSrspQv5sQ2dPbS91PlEcQQPl4WmHqt9XMoPanx6myPSfYY6pCzEZuOINRWvGBH8OmcZ_PYRzyD2lIs7qcyy4LgH2b8Xq47DFEBs09tweaLHxDEmeXW2aSpXNc1xGk2ahYjJjhB3d2juWK2ilprmE6GIMQPqiQEXjJALraUI2tUmKjcncFf1j_-dVPJI1zRwpzYCidgpGMvQTrwntADXHMbHohsIv4zzBa0dhh6K9OqMT6Jmp7ZHri4XHas2sDSHeQCORvnfzxu9l7b6n3aI4Z73WxM3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر پیر اومد دست این دختره رو بوس کنه نزاشت بی لیاقت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83304" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ درباره حمله به خط لوله نفتی عربستان:
ایران به احتمال زیاد مسئول این حمله است!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83303" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=AKN-yoZH1laLC-kUla5-yKsXSj3laUPCcHd-yGPmd_gMAQFa899p5wIp7uW2JI6lZgGhI2tG9B5NN026TECOup1fcaFAnQtuCpLMO--Fl5m01NMuUFPSqaQLQIxPAQJ6HwrDUGJfzGKQX-wHf2ox2pn4xTKI9XEbrRTHZlfzEzAY-6bku-ZXImGilxHXa0Tuq4ek6-Nh9_dV5s6CmEDA3WmXzQwzZSwY8dEk0LivYosPbfEWrT_bw1XD_hlC1kdXm9geUj4l2c3-0Rf--L13BA0M-vF282fqzRfnWztexPzJQSU7m3kUc5T1etJmEA2nwcwGq3cMA2Ts5vgSe7pdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=AKN-yoZH1laLC-kUla5-yKsXSj3laUPCcHd-yGPmd_gMAQFa899p5wIp7uW2JI6lZgGhI2tG9B5NN026TECOup1fcaFAnQtuCpLMO--Fl5m01NMuUFPSqaQLQIxPAQJ6HwrDUGJfzGKQX-wHf2ox2pn4xTKI9XEbrRTHZlfzEzAY-6bku-ZXImGilxHXa0Tuq4ek6-Nh9_dV5s6CmEDA3WmXzQwzZSwY8dEk0LivYosPbfEWrT_bw1XD_hlC1kdXm9geUj4l2c3-0Rf--L13BA0M-vF282fqzRfnWztexPzJQSU7m3kUc5T1etJmEA2nwcwGq3cMA2Ts5vgSe7pdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه اکسپلوریه من دارم آخه
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83302" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83300" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده جواب هاشون رو ببینید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83299" target="_blank">📅 11:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=Rj1RKMxg7z8Y_BnEOr_qIkr0R4QPF_6vDput9mOflTR6X9QFKb04iMAjnp7yOss1bjcdZ3kuAwttBsI1XvCR0NokPqO8zV-sTsmQHEENId0cAhLuKRiBmM4NGR1GI4N_GF3cVWY0icLH91YCf1JMSLHVQSQ7nxbjAUWf5n_PfBWx7EVTaw6gbE76OYhjz5Ct1zN2iH8uLvnzMmVkzKCQb3td70ZWypLpPu9flHbespJYE4JBTgqA8I6dxhO3SOSFUuJB51SR4EvCTTb1sOab0Ox8q2Lrcaph6LPh5srYFuK2AA9l1mUPky2CcuFt-rxdChHjZNm0pfm8qXkZ-JulLqjog1kIYdObXmTeq6bFT3iTOWy566h0-UqOZkuf4B6s_vbNzRbjZMQd0e54sNIowHXsOILOWlwCozlADlauJ7bdAG9xPrB8ggffJzZbHtiZsKmxw4ebPNJMAYBXib92JVKYlo2CUEo_vvZRYUrN_tBtB6ReXkpsw1a4kFTV6LYGFo6xLKAjdXElle_wdQnjL9mY3UsYz3PD8Ll7SGlJ7t1eNrMnneFH7Ei5EWyn7sYZbOmwDj8_23t8uNRtWlGfU73BGZYsTVm5gvhI-py37HyczgV2ZUfOh1FGKIsAFIvR1ab1ltkIH_8vgpwCyNe4YuWLTveaJGNjJFHs4hWO2O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=Rj1RKMxg7z8Y_BnEOr_qIkr0R4QPF_6vDput9mOflTR6X9QFKb04iMAjnp7yOss1bjcdZ3kuAwttBsI1XvCR0NokPqO8zV-sTsmQHEENId0cAhLuKRiBmM4NGR1GI4N_GF3cVWY0icLH91YCf1JMSLHVQSQ7nxbjAUWf5n_PfBWx7EVTaw6gbE76OYhjz5Ct1zN2iH8uLvnzMmVkzKCQb3td70ZWypLpPu9flHbespJYE4JBTgqA8I6dxhO3SOSFUuJB51SR4EvCTTb1sOab0Ox8q2Lrcaph6LPh5srYFuK2AA9l1mUPky2CcuFt-rxdChHjZNm0pfm8qXkZ-JulLqjog1kIYdObXmTeq6bFT3iTOWy566h0-UqOZkuf4B6s_vbNzRbjZMQd0e54sNIowHXsOILOWlwCozlADlauJ7bdAG9xPrB8ggffJzZbHtiZsKmxw4ebPNJMAYBXib92JVKYlo2CUEo_vvZRYUrN_tBtB6ReXkpsw1a4kFTV6LYGFo6xLKAjdXElle_wdQnjL9mY3UsYz3PD8Ll7SGlJ7t1eNrMnneFH7Ei5EWyn7sYZbOmwDj8_23t8uNRtWlGfU73BGZYsTVm5gvhI-py37HyczgV2ZUfOh1FGKIsAFIvR1ab1ltkIH_8vgpwCyNe4YuWLTveaJGNjJFHs4hWO2O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده
جواب هاشون رو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83298" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiRc4h138JADidu0SbFcPd-czxMZRBQCEaGyvbkIr7opTvwe6u9dl5a2xLaWBNORFvqTVHdjuULrsHjJL4G8TY4Aii3J8of9aqHOvg14Di2r3oT6HAi_TafYbR89c58AYp3DEA4Nh0Zqu3McxhLLNt59yvKuNsUu3nNBGa9J3Z_nDadV4IK5ZO_iSU_1_edX2-UmeTC-9N1Mqfqa1LRBoFQUcXBMWDqaENhbgEyHmos0kQSUCKWxgmvRZ22z946MDxAGiXD5uOrmxogD1D_Xd80xXgx-89N0Ph3p9Vac-HEfmDRplQcG-WWaqy51KaBZjLMG9QjmC5vwBF9a8wjy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
شارژ کن، هدیه بگیر! بونوس فوق‌العاده ۴درصد
⭐️
💰
۴٪ بونوس نقدی روی تمام شارژهای حساب دلاری!
💰
🚀
می‌خواهی با سرمایه بیشتری وارد بازی شوی و شانس برد خود را چند برابر کنی؟
🚀
از همین حالا، با هر بار شارژ حساب کاربری‌ات، ۴ درصد بونوس نقدی هدیه بگیر! این یعنی پول بیشتر برای شرط‌بندی، هیجان بالاتر و شانس بیشتر برای پیروزی در بازی‌ها و پیش‌بینی‌ها.
🎯
💥
چرا این بونوس را نباید از دست بدهی؟
✅
اعمال خودکار روی تمامی واریزی‌ها و شارژها
✅
سرمایه بیشتر برای ثبت فرم‌ها و بازی‌های کازینو
✅
فرصتی بی‌نظیر برای چند برابر کردن سود
🃏
همین حالا حسابت را شارژ کن، بونوس‌ات را بگیر و شانس خود را امتحان کن!
🌹
کازینو رامسر جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
🅰
r21
🔗
ورود به سایت و شارژ حساب:
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
💻
@C_ramsar</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83297" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">همینجوری پیش بره ایران میشه نیرو نیابتی یمن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83296" target="_blank">📅 11:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صبح بخیر
مرز شلمچه بین ایران و عراق توسط عراق بسته شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83295" target="_blank">📅 10:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شلتون ست اولو که باخت اومدم ۶ بزنم رو بردش، اشتباهی زدم رو تیافو</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83294" target="_blank">📅 05:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7W2ic-CWxFE0ReToMPLYxkYg1VrR2sG33HffwcvQ5nf1Tbc066k8OIL46McPtqm1KJ9IG70A094KvUke5GrOrUp5tB8urEV5o8Jda9T4dU0nWSU8D8aIg-iIC4MAPlpX3ye9pxQSh8x-v3edz7fhRUDiXsIkvWYuK6r0wu0cNFBsxAiz0YEVuua9-zjLWesRI1Wa_MUZ4qPU1iFuyMx64yrCQV9ABmZfcPAbs8K7KRJoxPByZg0fe6nfjH3JfQx_myBP56jqR_6N0N2BO2HcYozWzsVc69vNZ-Wx0uoR13ntoT0kXV08Azyd0vvGczdleT3nhsGkndzuIymY7topQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلکسیون نمایش زوال عقل با هوش مصنوعی توسط جهان پهلوان کامل شد.
❤️‍🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83293" target="_blank">📅 02:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmndvYNJJPufH04m6qgcg5PQFWN6dbart-V8ZK6b7cRd1PCfdpr5bmBmeniz2WWBbC1CsgcW0AuPmNDtRXiH16Rl4R2hu_BmLXP3K9SdDUkrAnc22NgI_KRyiUV-aJfrf9_GgoGhusmLWKI_zaNBjdm9Ubdt5h298bzwaH045g3Ll2gK9fFBwJpRAGO-J2sW-EhspOCjUhhDKrC97iKs1u3EFnDvChQs-YnNIqCYkoH35T58mlGT1iC8t12chCrM8oU6MEfBlvC8uljrtuq3Llod0403XfPsRSq4UB_L8h1uPcgHNDeKabYZ13XDokiAzLQKUZfYRTYQ8UV9Wi-q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83292" target="_blank">📅 00:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njYuqXBMIlWtFHd47mCHmFRzwLHTHyWxUeQx6oEZym0Tu6pUFu8ojxIJoVbxCqlhR3SVjuGjYyHjW-op1M5WvRa2w2LBF3_8GPtGr0GUxTFFU-fks_Xp7pHC6FyKTPs4Fa-Sm3tmsuQYNxPXByIpl5SOhkDKfi8fMfvmLFpYrDBhWUsmevnL-OUcQHMr71XyAmBcoUxoQeObDfIZBNzBc1Lr-6IaapYt-jrtMq_SzV6CHWXL5YxG-U217wVi95XnpFPj5M9KaGwQ2mGg5L3ULDjUUHhUPuISwDGpyVvuYCR_ibstYrEF_zSe4AnQ1x2dR8BdTg5J_6gHoT2riENZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83291" target="_blank">📅 00:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شرکت آنتروپیک، سازنده‌ی کلاد اومده یه گزارش مفصل از عملکرد و تهدیدات و اقدامات هوش مصنوعی کلاد منتشر کرده که توش یه بخش راجع‌به حکومت حاکم بر ایران خیلی جالبه؛
این شرکت ادعا کرده که این حکومت با کمک مستقیم نهادهای چینی، به استفاده گسترده از این هوش مصنوعی برای رصد و شناسایی مخالفانش در فضای مجازی پرداخته و تعداد زیادی از مخالفانش در داخل و خارج از ایران رو دقیقا با همین روش طبقه‌بندی و شناسایی کرده.
همچنین این شرکت ادعا کرده که این حکومت، از طریق همین هوش مصنوعی، برای طراحی طرح‌ها، سایت‌ها و بدافزارهایی که تهدید یا استخراج اطلاعات و به دام انداختن مخالفانش رو در پی دارن، تلاش‌های زیادی کرده.
ادعای دیگر این شرکت این است که این حکومت، با استفاده از این هوش مصنوعی صفحات مجازی غیرواقعی زیادی ایجاد کرده و از این طریق پروپاگاندای عظیمی را برای خود رقم زده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83287" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زندگیتونو بزارید رو برد کارن خوسانوف</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83286" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83285" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83284" target="_blank">📅 22:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: هانی رامبد رو من گنده کردم، قبل من هیچکس نمیشناختش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83283" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83282" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3D0OzzRoekvaqCAMoU7tNv0udmVey-1lOcUCsLEkgwPXv393DjAmoNSflcSCOPY4UZcG9nGz3CRIzIgbJ_6O5ONVeknhiyCTuVZ1h-uLBNw958Td_H5XEaN4OqtzdkPVLCUexaBMb9DJb2MFBkoWY4Oa7t-nMVIHyPBfzlWfHAJSqKRg2sseKeTQg2Ubzdm3tZDx95UJEm0t88sBOsULQOr2sKSqj-9-awLZztsG_twPtiO-LH43Hy7WDnIKEsAEkf7XjehEPUCDL4RxhRqBl_2wPKjdZ-E_zBWYjV2eXDt8d9UETRJU4Fw509lY3-iflwvuzjSBFjUwqGy8UZcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83281" target="_blank">📅 21:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جدی این وضعیت دیگه داره تکراری و حوصله سربر می‌شه، به نظرتون سیزن بعد از کی شروع میشه یکم پشت کامیونای سازمان ملل بدویم یه ذره هیجان زندگی بالا بره؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83280" target="_blank">📅 20:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سعی کنید تو این دوره زمونه درامد دلاری داشته باشید
من خودم درامدم دلاریه، دلاری بت میزنم و میبازم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83279" target="_blank">📅 19:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه سریالی هم هست Special Lioness یجوری توش ایرانو گنده کردن منم کم کم داره باورم میشه ایران ابرقدرته.
- مثلا ایرانیا رفتن افسر ارشد اطلاعاتی CIA رو تو خاک خود آمریکا دزدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83278" target="_blank">📅 19:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=o6gxhjgOvdRHL5CZDhpPd8bJzCxFTWv9d2KT5k1or6KEQBR7_YwgJW1kPFRAIv8eXWE1Q_56VUpmbIYJ9P-W-PNAUFq14-AmLPegdX9r_KAzyKtAgrbH1NmmlNbjRdwvxOJ0f5ifxirr4xq9oI0-ZkIfLyflG6vwo7LiO3ijiutDNuW-_QPtRTufqwkA7OVu_Qlp_zZcXXOLLrwfkqr6SzjXL6wCCDT2g1jVzA1kadK_0NF48Mw8s1IWro0I-DVCrFPjM-PKsRXRO7L-WR4mnfY0fNxCFcEyTeAoX5UbHXxKt7-s8aoJJ532sPqxnPQApxZgYnKSbR8f9j2QPqyQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=o6gxhjgOvdRHL5CZDhpPd8bJzCxFTWv9d2KT5k1or6KEQBR7_YwgJW1kPFRAIv8eXWE1Q_56VUpmbIYJ9P-W-PNAUFq14-AmLPegdX9r_KAzyKtAgrbH1NmmlNbjRdwvxOJ0f5ifxirr4xq9oI0-ZkIfLyflG6vwo7LiO3ijiutDNuW-_QPtRTufqwkA7OVu_Qlp_zZcXXOLLrwfkqr6SzjXL6wCCDT2g1jVzA1kadK_0NF48Mw8s1IWro0I-DVCrFPjM-PKsRXRO7L-WR4mnfY0fNxCFcEyTeAoX5UbHXxKt7-s8aoJJ532sPqxnPQApxZgYnKSbR8f9j2QPqyQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تجربه شخصی ۹۰ درصد فیلم هایی که تو اینستاگرام معرفی میکنن کصشره و بعد دیدنشون پشیمون میشید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83277" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9mTs5Dw-JYZLFGkSq-kan1vk_vX8HnFAZ9jiZ8fwBPhkP4A9R9h-Ryuyv6f3wZAqKY5bbiGoQJSdDkYFQjfKL37Qnd9sPlLaopU-i5xwhIudbn2us_gIszEPveHzgMsveggaJrZPpC0V3TzVb-kpt8sBVeX32tBo7uQt1qlxUQVuCnjGV_LnvjZz66I5lZBYftg6HCutsidA3A14JvqF0hIKdQPYVjLQQukQFsE6oc_kTmnsXZ1Hgaqnv7tzn7WM6U_xg6hQUmZM1xHIUWDgA2vM74fgrA4jO9Y9MnfnIdkJDtbzH34L67xIjZ1hqc5BUkyOvv13A5MoOu61cMTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس چند هفته از تمام دنیا جلوایم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83275" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=PHmlwXCpGsApRm0c1Ej5_appfVo0_YpKn4H34NLDRvGRg6vEZRyjfSqd2wd0jvpEz6V6EQELOkRVXFt7rKoTYc-Xod6s2EjjZyTj7zFGdS9lKk8kQPEDqFrXqSsaBxvUjVmBo_AbToLgDLeZDtPBFHRuY1u_Tubja1Qte8PPiinMrLoPolC-fGBS85h83eAk2sKuuYX8OYsVdqdjI0aisKOiBaT5d7zjkh1lLKyHGwWrmAj_plSb6P_iplTdFhO8wsjVzjOX-fn0oh2rUlbzkVdM3P0Tzknty9HGNp0SlpLfAap8JmQlU8Y9-_ubh0Nz6WF45fd4BQI2nmzq27ZTBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=PHmlwXCpGsApRm0c1Ej5_appfVo0_YpKn4H34NLDRvGRg6vEZRyjfSqd2wd0jvpEz6V6EQELOkRVXFt7rKoTYc-Xod6s2EjjZyTj7zFGdS9lKk8kQPEDqFrXqSsaBxvUjVmBo_AbToLgDLeZDtPBFHRuY1u_Tubja1Qte8PPiinMrLoPolC-fGBS85h83eAk2sKuuYX8OYsVdqdjI0aisKOiBaT5d7zjkh1lLKyHGwWrmAj_plSb6P_iplTdFhO8wsjVzjOX-fn0oh2rUlbzkVdM3P0Tzknty9HGNp0SlpLfAap8JmQlU8Y9-_ubh0Nz6WF45fd4BQI2nmzq27ZTBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی این بچه چه گناهی داشت که پوتک باباشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83274" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ و‌ آمریکاییا بفهمن با ۱۱ سپتامبر همچین شوخیایی میکنیم همین امشب با اتم ایرانو نابود میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83273" target="_blank">📅 17:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تصویری از فاجعه ۱۱ سپتامبر:
🛬
🏢
🏢
🏢
🏢
🏢
🏢
🛫
🏢
🏢
🏢
🏢
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83272" target="_blank">📅 17:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان رئالی شما برا اولیسه بمالید مالک بایرن نمیگه اینا خوب مالیدن پس اولیسه رو بدیم بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83271" target="_blank">📅 16:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۵
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83270" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83269" target="_blank">📅 15:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2xQatGzKL2yotUrLhkY9l3aJR-wKRo0szIFK6s7NHjtjKwc6qsyxgjfTjtqgFzXOGJxnfPUpEwEXfSucKSUMOtDf1-Z9fG4lqoeyLCmhtXkxDsbSrFdf9_CaM5aqeQZv6Eo3W43IFNGXEAW5tyeYz4Tm4orwIQwe-2_MnZLsCcFajqElnPXzlaWJQMRbnA9mVcya3c1c5eocoTb7Om0wejKky0uFwWqsCVpDa6W_Z3fnvydm2d96B424T9y29g_MOLS15BvbktxPYOJTanEdISz2YHExvrX6HwLDHi8Ql4UWRSwyGPF5NSqcXvWGbMVJArpaVDRF2N7t8a1PFfLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5yNdhyrVIYwbFj5gEqRzW7drOuSvN9xZdhUl1KcQtA9lefXuziul8YkA_0ezxVuCQBtcQnRmkjra3_MUKU2o_OHjnG9TIemHti4BhQ9iPTv2M6EZ9op6dCz-vgH04eW_IlxW9djFJR2g4um2UM5bTLcl7vW2yypM2marbjvgySlH6dU87y5qwT9oNcOEV4bflYddChuPWEe5h1mLq_oxi5Hmlgyx1ovePj0q737qprIk1r_LIsW_p25X5ngZtQTkZNTOR6JRp4HQTERKKo7vSv0bUjz_f3LszJ0qjQuXU2SOP3LhUG9h-165jFzyIO3aAwlJ--0f4lEhyCnuqwWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=QuX7KimwQZW0GJ-KOshhxzKW8MxXHSXdNZB1ETyPztLiySoVAuApktcRSZflI1EXDaaLih8rwjNYnHvLSALQIh_8IhKcRaeOShs29KkIbIa7B-mf7-xwuPQyTORyVNYHNmEMj9h0HGcgbZYiIs2j-Nh46n8m1SX76aP7cHHJJYg2rqPj0lBfoWwVbn4r-x28DcJm-H0FcLjpOE5JR2UKS2w4z3MCWAI2iTj8URv69QKZKuN_wm4DlidCLX86ByMZpdqYiQnGsXw9Ik2MKz67bOhEzgrhg8muZ1FRALEu-j-ZWcFe4j_Y2aT4KCg456xX8hnW04Aur_JKoXAlr1TbZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=QuX7KimwQZW0GJ-KOshhxzKW8MxXHSXdNZB1ETyPztLiySoVAuApktcRSZflI1EXDaaLih8rwjNYnHvLSALQIh_8IhKcRaeOShs29KkIbIa7B-mf7-xwuPQyTORyVNYHNmEMj9h0HGcgbZYiIs2j-Nh46n8m1SX76aP7cHHJJYg2rqPj0lBfoWwVbn4r-x28DcJm-H0FcLjpOE5JR2UKS2w4z3MCWAI2iTj8URv69QKZKuN_wm4DlidCLX86ByMZpdqYiQnGsXw9Ik2MKz67bOhEzgrhg8muZ1FRALEu-j-ZWcFe4j_Y2aT4KCg456xX8hnW04Aur_JKoXAlr1TbZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=NbMUxXOM99S9_lWXu7gn_BO_OU8Efnbzefd_pNfs4vhxnKp5wGy_J2gdEfG1JS0jUFGmAJN4iF9yIYYEuM0GUJXi0ImxzKMpxJFNIMr_wGZbNJrd4PvbKHKwVDbxGfig0zeYJznaJZakmgbGo_wLAZdddRYfWmJvABErbtNWut1aYhDspijb5rK_NWmtg312T7UNIb72f-RdthDvSiLl3dK9qi6gZ7O-X9yypPXwrGIjORPSEQXT-bRDQmdoGpIRb63ewaLlT7bzW_boOUF7QDB4k_jmR61CZBbEvH1r6NkBXGd9eKE9W1d4fwWEuORgOm3Qsgqua8GV7gqtDGxaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=NbMUxXOM99S9_lWXu7gn_BO_OU8Efnbzefd_pNfs4vhxnKp5wGy_J2gdEfG1JS0jUFGmAJN4iF9yIYYEuM0GUJXi0ImxzKMpxJFNIMr_wGZbNJrd4PvbKHKwVDbxGfig0zeYJznaJZakmgbGo_wLAZdddRYfWmJvABErbtNWut1aYhDspijb5rK_NWmtg312T7UNIb72f-RdthDvSiLl3dK9qi6gZ7O-X9yypPXwrGIjORPSEQXT-bRDQmdoGpIRb63ewaLlT7bzW_boOUF7QDB4k_jmR61CZBbEvH1r6NkBXGd9eKE9W1d4fwWEuORgOm3Qsgqua8GV7gqtDGxaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=qEkgWu4R1yrbnkL9Dxipe3gsMWjsY94NuY8MlpVl7KeyNHQxVzyN_QgFymGkMhtqdu6fw2lylMn9fFrxWiWRx4oJuEhwonTz3otahCSZQNi5HHGyhIkjV3R4SJVA1mtEuCjmmOwbFctSCngDYmJZGiHl6pmPp9Bz7dhh0goB_W2ZzNFuOnIQrM5UOyB04VBfCHuOqdGV8NV3katIeqGjpOkU_gVeZquJdeGYZkOFuCsDj8EJr53xDxUFT2CYH7D_bTe2RiJlvwJeQgcCtSYnr19yNF-olPkkDptE_yKeOILJ9c8q08EvfeyEzHGMJAaKHClg_SmQLoHDWshfD_pzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=qEkgWu4R1yrbnkL9Dxipe3gsMWjsY94NuY8MlpVl7KeyNHQxVzyN_QgFymGkMhtqdu6fw2lylMn9fFrxWiWRx4oJuEhwonTz3otahCSZQNi5HHGyhIkjV3R4SJVA1mtEuCjmmOwbFctSCngDYmJZGiHl6pmPp9Bz7dhh0goB_W2ZzNFuOnIQrM5UOyB04VBfCHuOqdGV8NV3katIeqGjpOkU_gVeZquJdeGYZkOFuCsDj8EJr53xDxUFT2CYH7D_bTe2RiJlvwJeQgcCtSYnr19yNF-olPkkDptE_yKeOILJ9c8q08EvfeyEzHGMJAaKHClg_SmQLoHDWshfD_pzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV6SftnHryJsX7ZoZaXTe2Bfo_vvEWcD2iw3o0YFV4RaCvzlYvhGI09XX81nOjgT85-FA6l_-d9cGiHNxp8b3qSfKgiEoPnjc8_m2x2kOzlYuh3czFGP3BWl8hXjgKrlvqJfYW1PHULb1XQkltztGpfArlyA632yZ0ZB5ffizVfcKqpq3z2kldusCpItLhVsHEgFz-ZyGTyHDdfNLpQPOa_ul0_fZfO4alQHBN-hwkPHanCQSDgJfhjNId9-Y5kJ_JniIuT_X8QnBIvWSpuyZhoTGf_63BzRwE0lN3iEzFrQ2g6YiKMLdtWbVqnO07Yjn7bUSVCj3cdEg7ycsK-GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RADc_uYfcXD4h3uDshHSm1WJInRBOvGtlXjdC0sdJu3skZRwAzLTmoAVszTMbeMowedoGzVE4wWlKt6Mohb7BLHCm060hOsMgY88cMwGfgtuxh8RxUXnorl5iCYWkQmtYOdicxwm5ziqI0RHChm_fzW02Bx4nfRr5IgonrV2ILK9kieNJIgXnqU1ZufeRKlKHWPWL1UzQ0Y7xz3mxGAyvIqH0FDALbuu2NjjV5Jvl0B65imIT22OdBfcENA8oeK1iHikB24W1_INb-v_bZkMOWDknjVpYv5HUH5OaxzHxy-fQ0o2ikqY9Np5bYBoOgzilY99lBQ3ir5xUUgRxginiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=UMFhzXp0hYHVDO7yHuUZ9wfL_mrWy0w1RjRvauJ7I24wXkvFJO8l-vOZ9fEJT1BO1bl91ryGx4W5wUomZvvMSmdzn_fKvYVqSw0oITYtJOHFEebiB8Eq3g8Ml3E4tQ1JPMVCRnhUBWByTMw7gujSFz0H4n0FaSZ0WrJsPLaqBEoLelbsDPdinKmFYyuRVueAfDrdtBM_OetLivu0gFp1hbbeSXtPNTrtdgCuRRC4Fgdv_NLJaW6QSAZxFNTLOgQrxw5HYXL1mpWzztQKEZztTZ4isMwp9D91TfIzrNciQs6Y8HeBivg25hqaWriPuI8PUuXZ2An47IdZqzHrHw1QOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=UMFhzXp0hYHVDO7yHuUZ9wfL_mrWy0w1RjRvauJ7I24wXkvFJO8l-vOZ9fEJT1BO1bl91ryGx4W5wUomZvvMSmdzn_fKvYVqSw0oITYtJOHFEebiB8Eq3g8Ml3E4tQ1JPMVCRnhUBWByTMw7gujSFz0H4n0FaSZ0WrJsPLaqBEoLelbsDPdinKmFYyuRVueAfDrdtBM_OetLivu0gFp1hbbeSXtPNTrtdgCuRRC4Fgdv_NLJaW6QSAZxFNTLOgQrxw5HYXL1mpWzztQKEZztTZ4isMwp9D91TfIzrNciQs6Y8HeBivg25hqaWriPuI8PUuXZ2An47IdZqzHrHw1QOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxKXRvaVeMuALay6XBuGE7dF9MnnnTnOD3f38Y73Eiv7kXXfWA99dxbCjlLJkE26n1llieeWiRG6bg4FqmZCZH4Z3LHe5vV-Zvo_V7EMf5MjDeKxPX4hylCmmc0Mnd6NSw2LCKFu_E6XwaKqyTErSG26CENeFWRF1UEZT5rSgiPdEG4-F5dIa6jrh2jz7-1Qz6IIPK-QluweNyWwY_a_-NNdDqWarTNJ5yHwaLIQEOmR7QZsBe324JguCF_oZQHfEJ_WhQXUdiKY-8S15ti4L49pGL__YvUX5x4X1NBD4k5W51hGOluqcyRaE7MFkr5VwckIMnZVlyMjtShwb-jfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXc_PvOX4JdexbhnBN_yTkQllbqQ6hO1jQLcBCHvp7EqKJQRTzU-oZqtFNttVVEfAG1WuLZILw-_W26icyJ4QpCEBl6UFj5TSHYzVzY0PoqXttVK-QNtHgUIID8sUoLBNH1BYa_pQKjMA7uGWq9DWmxfXv_1mITW1PsP_708ZD-f4A8ORyW6xpYzFLPuQG476Z1kg2ZPah62V1CK33BQ7mLmYsEOCkc2z3MDIsgoLU-Z2TjYqr8Eespp9sQUvtrKV4tpAU4DSzCqNj8rGxiVmAtKI9LuI3UyG_pMe7pFrBur9avAvRgv6BvhuIsOBF1HmY8b-TXLZTw8in65V8KWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQCEK87Yp_QhJx_njACGjXI9VNtWvZ9R2_MyTKcPdxQ4gu7bjiiBjtHEvLM65y5_hm_dhMX6FRQETmyQ6b9rLvS4qnuhGYLOUVoeQNr8uuZIF4Emnh3JMj6-HaEKFQQ0nK5n_ujNapw2vaz5s-suIihzZ3N4t_a5zShupOP6PFkxAOb3-ht5zdstjzsHvTcLi8Bwsd0_l6vGLbmlsW5zg8nTZ_-KsHZb2TrOV8LQnc7BY8XxVlYaRQT7caCQ_8_PPp50xlceMY-6axc3pcsNKgqIYmewbkeYoxTxYrIf3nDd8Mzrq1KIN8FRCR0Cd6--AtcwwfsHT7KWzAVSkk53qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fk9OrNX64lQ46dS__zSk5cxtAz1jyIZYv8mXfuOGMPue_Tvhbor8be6DEj0-zitFbqQ-zB0AwLeCwpvnItSwP5agJD2jH5yu8j3eVfKD_CXYAos5BBmwIcDoxCNuy6JD2z6tbLzAtH3b2D1xlmNE8xVewWl-vQ2UFTkSKIGYG85cVXTpfFXokzGCPO_npKTMOgNtkloOjtNIUx3hi0t60cnghKssAiGrRwYE-BSd3oXxeD7wvXAVtfHyiqxWeA0so6jXGOS79ti-cGpg5plbGPpsqhbEqHtalblqZF2MmKN3xQ1W3_rntwz-InmhYG9o78IhcDhODHIVO_iV7O7hTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phlN8J4UULAW3NOhCRrBvhsJyNVnwoCl89nzBTFUq33TY_xh_Ffjt86hY3LhGA5x675eNuBuXH93zVqh4YeSOXr1nlIv2rcy8pjuup_18SGO_Qkji08c6ydhGy7mN8nojgkTj1tHYeyvhhvxtYImnWVZk9BpOwwzDIlxQYfXcT2Sun7Fs-L52CLrn-PlKBryURkBzePV7YPCkhAyr2Y5TNXwXa_3qA38sKvib3S0e3OC6PeiS1pjrH58PzPE5NW6UdlpmzMrf2WROytAC1jbnXCH_kFAKgmi9cFBtz3rNJyzwa5sHBI_ybxkXjsUulCLWTCW2ZVKMSV4_C2hD8_NFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqeUsukHxHSgNyXU7PadIE9_zGq6yNFMvju2SNTQPJiKyYazLfXB4g2K4cODsmv8jtE85p35p8JeM5vr9q5BnUEmfp-5eKX-ME_wUgFlc7T2DayLy_k9VEkgUK689Zdn11Gg9OVEJJswYTa0HAthmFt6Pil8DfnZD5JLV3TZVhqZYsCNVOe4z_LgQ8Zps9EyxE6Cj9z-Ehh4w30En4rwriIYtwx27N3ML-A9M8lYjupnzmwr7wJdYCIqNMF8oHcM9eI8Y3OY7PMObyrCBEgemAZ6vMAKKWBtE_5w7At6KMGHllVVEtMIRAlEQaU5Ja7fl0ao0-SgrF7Yb0CevrYccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
