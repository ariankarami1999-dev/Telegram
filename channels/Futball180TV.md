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
<img src="https://cdn5.telesco.pe/file/Yaaioy3-UDqBCk7s4tO3E9ewiMdgWfCc9iQxWU9z7MHKIUiN-AVimL0JU4zJQqxw2yzYACJUeucjostgr_PkYt-zmzoJxbP9pIDFtVtNp7Dotzl4TiCCbaxpY_HSEKfbeB7zu0WO5u0DKTZGc9tD65EWBXepATbPcvtMmIjAsYPolVHa0eCn7XH_DyxPkl_UAgwEHRU1JlKD9GGOLqUTYYF3qgUBoSKIHGVUEVkv0cbX_Db6TF7UanQEN46O6haNaAbteKs5AOjA9sU7deAehfR4LJNvZSehtvGRfXo8QMKXEbRQoA6DxkjCrJWhPuPbSZVlVR0VBQT-lEaUlZqxXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 423K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-105831">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های سخنگوی باشگاه گل‌گهر در خصوص فایل صوتی جنجالی خداداد عزیزی؛ با صدای بلند فحش می‌داد اما کسی از رختکن گل‌گهر بیرون نیامد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/105831" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105830">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
آدم عارش میاد بگه به فوتبال علاقه‌منده!
مقدمه عادل فردوسی‌پور قبل از مرور پرونده بازی جنجالی ترا‌کتور - گل‌گهر؛ این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/105830" target="_blank">📅 23:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105829">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
فولاد خوزستان با گل دقیقه ۹۲ احسان محروقی مقابل فجرسپاسی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/105829" target="_blank">📅 22:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105828">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
واکنش کنعانی زادگان، بازیکن پرسپولیس در مورد حواشی دربی و ضربه اش به عارف آقاسی:
در فوتبال اتفاقات زیاد می افتد/ نمی خواهم به کسی توهین کنم و یا ضربه بزنم/ شما دنبال این هستید که حرفی زده شود/ هیچ کسی مشکلی ندارد و همه را دوست داریم و به همه احترام می گذاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105828" target="_blank">📅 21:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105827">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
❤️
کنعانی زادگان: بازی امروز خیلی سخت تر از بازی با استقلال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105827" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105826">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😢
🇮🇷
واکنش جالب هوادار پرسپولیس به عملکرد تیم
:
بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل می زنیم 3 تا به رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105826" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پیمان حدادی، مدیرعامل پرسپولیس:
🔴
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105825" target="_blank">📅 21:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQYGPyAiIHUojxRgAi-_U5JKltmlt79ikgmW3z_eVTkYuI5DNSoJTjYO--a9ZIV562P1QCcxUJdwS42nVTsYIKLFDLdA5d557KvN8tqsagJ4RSBP8RtgWsLUQhNJs5hr_DKN9SqvN8YQP7RJKoKnKIHU2LPN9mL1kvIu73t3E0-3wwWD0Sq29y1Tl9e8yiU9XueeY0ewoDmxbcZD3A2dD7QsLshQoczu4okNo0WRl4bztSBaG2N-HtneZ-7wiP9JocNYkFMvYaTO4DZAKwtxwQT1ek2f4kB8o3goZpCpOlycdYcZouQhaCHh2XJYzLP__4NoDefRbtBjmVxfelRSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
عبدالله ویسی، سرمربی ذوب‌آهن پس از دیدار امروز مقابل پرسپولیس از سمت خود استعفا کرد. ذوب‌آهن با کسب ۶ امتیاز از ۶ بازی در رده سیزدهم جدول لیگ برتر قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105824" target="_blank">📅 21:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105823">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRS_D6YPhEiOYZN_Vc2NwDUaAYq8gQW5-cGIQffjN2Iil9UDXK-EBBqdEVnKTznk2GqTCJgrlQCkwYdT2LkXFeBW079LAHg6VGz_FxIgmymS9n4Kn8rYEaUVS64cvdwYhO1nAMcmYQlagTDN-Q9s1APXRqYeLAmriMhCiO4IZCYMa9G2AoZCEIeneYg0jB3ae1zHTI5O0tW02Dhq3Eg9kmf7Ju0M7c0JhLlyefGQHDXujKRppA1HGfmUdQm7gN9jvEcDlhQrA8UJbCSWKpaka0OGQva3VfBKCv2tesDvPilS18bvEltf1wgwWZwdhRhLtZGni_GsZdKKgsAhGX47bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105823" target="_blank">📅 21:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105822">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjLZmDXrDd8Sn8vPVCtvGeZUO-RdIzDUzcdAF78UFVvExbm_JgKMx5OyEjIn8OuQ1gMO0HUkpp_wsIy1ynx6Uu9ePaLuGpogK7w0XS_2l35qY5VEbktzt9nDB85hyg_hqd4HzsgFMYeSn8DZeEpvgGLLyzuNZ1ilJF9ZtOO0xe_jfLI5qIGm_BpP0DRGz6E5J4w_iPYr0jRxQipfGpIh7tVelcNphThEySqeFTefg8SfsitEDHZUTxJzUTyM1z185Gh2yxU79GLuvcdPKiMwGG-9CL-oZM_X121vPRVmIvrx-jl3kk_wXquRGqehSDPTcD9RoELZb6Qb6Wl59-_7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105822" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105821">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از مشخص شدن محرومیت 4 ماهه خداداد عزیزی، پرسپولیسیا این شکلی عالیشاه رو تشویق کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105821" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105820">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی
64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105820" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105819">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105819" target="_blank">📅 20:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105818">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbll0s23YWJGK0bh0waaToW5xaxgSgNDLwiXKuA3m4CS8I-4okLLUY16mKueTfHecnaRm79NV-Elz1-5WcblOP5BKw2XDEFe_tMfoOKFBuhZP_zHrmlCtwXLNhuROSzotJSVPj7S7wBIecLEuktLh2A6mZaARF5ABzJBxEL7iWcgH1H7GXYZuQy3wmgVProQNlJ-mSHLI3EcZwosGaFoqHsY4KpXtH_h4Hx4rsmj97u5DBOlIw8WYynDzk9Sh_E2ZlkpdPSxLLdzX8iYTeHBQgoIlsUSWEYM1rRl7M51hQexrpeUhW475afWe9szcAjjzisZ5DMxbKhNZadoHAm7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105818" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0Gh6rzJWFxxT5u5qYT-JsFEsesnjqmWlVypnGSr1UjoG5Kb-eKm50TwnwVeC6h1XMADROBtvpwl39TDB_Z2JR-OBl_YMm4NgkUxN73BxuozC2enz0Z34T43KmWLHD2xur2ttZGveB7qy6btvcDqttrBoObDXAtwfR3ywmDzlLeVKeVh75EoX5C77_YFsH0EaX-ZaLl3AtbKx_jI3p87lgmjV3eXZwlXJ_tpBvTn26FASiyySQrxV1cO3QUZSVcPiPyy597y_lw3g626RgnS3T9o8RDJKBYyLBeMSOyIom53brLQBuWkBmKEox8bJ2EN9PMZh6GERbRUjdL4m02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105810" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ7sDUS6sKJuCjo_harl7wGl-eVae0kvM0RizmpbhhQ2NC34ou_ZeStF6p-1LbS8h_4rQjMpLflqGv9raD5rl8vP8q9uYZkXFLuM2D0X6YEacEeX-ODo6gCte5J-ENnePNRmdxXv2BCSa1NQ-DbQkMx9pne-gpO0YCnoxwE9rxCuKz7iYT2pj5mecDldPunEEe3OCFQZDe9Pq5VO9M4tHNxiiTtUuxL6m6kf4QzmIGBUTUhyqNO54NEUEOzxiy8zqlm0AXAk_ojEqbJai-n_oH82Bxggd1QZLKMTeMb6E2I7eOmGeTyS0cONreb1fnxvA4jvvAiD-EEIWqX77j49lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105806" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4au16FRUIpVzLDDVRZRo9WrPuJnRDq2OGDzUD_54dWENce3dYgjtQaVY5L85g-yYgqwtA8a6iMWkt3C5otJNdD6Hrijs7jcl8BsDXrYCWq7h9B8SNYUyUtUlhZYmtHQKg4M7JSkAG6ULWZ9B8dwf6yDLatEgpHAc7FlL1w_zIXQcjYhHIsSWZukajQlEOd16JFJYMlZvsjAe-rm2uzjHdrifxjISd4jk6iMGyGT1xEDv9cm2BEaY0tq0J54bakdhLeX1LefCoCgrq6infbdkWfYTb8XCYMghvfRqjNaEn2iFh2T4r8eMifJ3zWOlausina6VUWCsDsukeT-A-qxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105805" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAIjcaPSDb4z7Sx1d_0bdEl3GazV1_yWbWT2qkUxsdYdXyspSXrQ2A-gORq6B3IQj4kO07aD8eQ_dSFJ4mYtRFphGUiZ33f8cu9o1v6YqcZDL4yYDZjtjKmiOHibTl2l1TH6UVv647Ja5-0Oj1mSah68R93NNr6WYPusqPeidGCl8WO-5k-LsvymeFnyFyMnY9ziZQJDb6wa9qK96E5FWK8hu3rexXTtnpMKBJcmTEoJ1NoQFXEAmENUczBiPEzanoy-v2KeuEiMyuCTl5AXZVPUhXfafP5c197cTlezPmfmjkk4Ick9C78hNQu5PPbz6sx1wAeE3o6jnwuA0QCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQZx0rB_GiOVv7QTerBdYRFekvD8exGvxg1KQPkXrqj7d2PIHlEK5sqjB1A9hL9f7PBBKedHIZZxiTD-KFreTtAAkPAQpZaLqlnzAk4fhRlbcN9XURnKhopxN8ZvUURcLU2qnSunaweAVaIzK5qp6bfur-A0LRoKuEx8PdXuKiJdtT5r_wss0SzghvOTBTVRIYtGIK6SfXSoG8012F_mg3yKcKEchY_3Nzd4DILkOY8KX6eV2lxCZLyY-oznsiRwimD9HMMikisPIJksEIna9My5ph8HjutivKLP5wg7Z7nGs07F0tEYpbb2as1q2jhksCSimxc1SD9DbzbQeQ2sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
جوری که دیشب هواداران والنسیا هنگام تعویض شدن پدری ستاره بارسلونا تشویقش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105793" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
وضعیت شاهکار این‌هفته بارساییا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105792" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEeP5VKMc2hPVC6IabNwvAlYVQlivA7SmmQWPunl8EvHE5hjAWkjPQ8rrSc0jYDNg39oYm8lrKKRc2tuDuL1yO0iKCZt4vzhR2EChVjgn02VxFnj3tve3_Q_WMZI869kUzgEmLSWBifmOdTrAhQKDKS-0KYpHwu1e9vPfXk_Nj-gah4KUniFAPrRqnLSm42qK0r7uIcxlUPp0VDvY1fwi2Nocp2qP5O-GWSCKRoDIV2BdcJARUSZNm0Cx4OH2LSNCki1bToy6jO67WdQS2gdmXFkEcCTBuDTNKzqXR_lGxzwCtU5PiDieNMWladgC089AB-qb-HD1aqoqMNjT_t_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد بازی‌های لازم برای رسیدن به 300 گل
:
🇦🇷
مسی: 365 بازی، 300 گل
🇳🇴
هالاند: 384 بازی، 300 گل
🇫🇷
امباپه: 398 بازی، 300 گل
🇵🇹
رونالدو: 499 بازی، 300 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105791" target="_blank">📅 14:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7j1rB590KW0zz2ODRRTCdLfEjrpL1un8u_d7NcHsX0Fm5HrANGHqBQz13vZaLK0tGwY5YVNKpJLAYC0ct_e3vo2RXw5MbRHOtdV5ZT71-XaYVEnc6k-kxjKNENtyMiQ2sawZ46BTEvuLnB00wkoF5Qs6dnr-7t5iYuSLVpud5YqLMUkpUD122Mx57e6ZxPQnqNU2DIfO2Uf36T-BQRakhZOseHeUyz6g3ZtXH3zLqBLrk38sZjQaWHHYoZddS0gP6ayxE479QwHSZmFWrt-mRrQGixOScLPWi0vCgbJBfeB9nm-Jn9wDIqbWVOlLvhQnwS7-MHR2-yK-NFdHqJk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY4WNgi4sIDFAE9O4OEJLneMFN7s0UIie-FHjcXa5nAngaZc3twKDM4H7aYvKvJC-2rrcC6m1SsAFNHlCi6nPAhSsvWe22PwautemaeRH-QVdbqiqVEAPWVwXIYpS3whtdJOsTBtz8XwamJ-vJ6LHt9hWGYupITe24fqzfk_pWi9kFj8PLx1g85L_Ix4w2XFljv2FpN2kS3y4YZT505Mbx0Ay0hH9ecS_3fz516GwamHTjEEjCXCpqeG1xmzC3jDdpcYe7ox2z1yzE2EGS3FuTKQHd_WUl2l3H8fzcXAz9jD_02dQbKQmhtr7A328I3F8srCfLlni31S25GjFVUlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeYUhOH3D2BQ2VH3hOb2PdzzkKbGrfFLrGb5AVjrEDB3tUDDGlz5YYTBXfH_-XYSDnKK9CsMXUBrA4wk7Z12fgK5U2Ph_kMxvlJ11d_pxvz5vpLHhdG3tsINo1e0M8mVJEZxpmw2juldHKghXhwhVl5vMPSPv9KLX9IHa-Ify8pJm8m47f5ijEU0wOSYxgEZqiMwhl2goKLuxwe3vg1ndNTD1Yn8sc2YMGcdADL3aRa1ppQ9nKAfO1S3CYPXrgS2Mc7WTfqonXOt6GrK1h03lBeGNaTKGaED8GDLf5R5isM2HOys47YvH9-B7qxvgrTgMeotPt5V9G3p6KXSUIM9yAdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeYUhOH3D2BQ2VH3hOb2PdzzkKbGrfFLrGb5AVjrEDB3tUDDGlz5YYTBXfH_-XYSDnKK9CsMXUBrA4wk7Z12fgK5U2Ph_kMxvlJ11d_pxvz5vpLHhdG3tsINo1e0M8mVJEZxpmw2juldHKghXhwhVl5vMPSPv9KLX9IHa-Ify8pJm8m47f5ijEU0wOSYxgEZqiMwhl2goKLuxwe3vg1ndNTD1Yn8sc2YMGcdADL3aRa1ppQ9nKAfO1S3CYPXrgS2Mc7WTfqonXOt6GrK1h03lBeGNaTKGaED8GDLf5R5isM2HOys47YvH9-B7qxvgrTgMeotPt5V9G3p6KXSUIM9yAdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZataCB-NXxPzs080VhekdxbfOFkR1aT6vQcGGjMSza2KdeB8eeUrMB7FbNdMmZXMhqfWSGKajRGIYiHYWdKdss4xs-8pw1RdHKYzFrMs2hOfuv5WaI7brt688MASbjCpOnz1XPGZUOYiw8pr-hapXCKYCCdx1wKXQ0xdO8YkTFUoiXaVbyBaxMeBnAjYmG1ZoaYOqz3VTaAMB2RcwotU7s5WsPLj9ci5_hoA3iJUJnLCGoT8ihpL8JTqU8j62Qn2de4duQlR69-8egonQQctEYxePXuE6-3SxAywWpGY-R7mW5l1RpYcBbXHeQEJm1dakM04jknS76WQNRkMenHcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=P2lsUxXBWt-Uw_r5Od3u6p2G55etdwrhnAs7nD4JZ0DMhkxhD31aDoTI8ufXaWz-rWlW1tzwAYT-mTNVRIdmglBznjUgGGB7knMVjxkPp5LVixjXy1EHa2UsDxWe2VnZzUXLcjxNiUdxZmlJQIWmo5mkgvpLMmcI0BbC58Gb0A3C57MAxtgvFBPY2dJKRbFnMxmhFKkm7G2zUKykVzWoCu-nQyWzhTyJkFLAecxoElr3Hqhmbw4vWYrAVIVtpdVadapprg4eiJd9tN_Xl6hMJRqeiLxDOL1WDe9i9FKQTkgYjfpCsZNqTPmW3sZc4TD-V5E2F9Wt-XNqaQgEWIcKjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=P2lsUxXBWt-Uw_r5Od3u6p2G55etdwrhnAs7nD4JZ0DMhkxhD31aDoTI8ufXaWz-rWlW1tzwAYT-mTNVRIdmglBznjUgGGB7knMVjxkPp5LVixjXy1EHa2UsDxWe2VnZzUXLcjxNiUdxZmlJQIWmo5mkgvpLMmcI0BbC58Gb0A3C57MAxtgvFBPY2dJKRbFnMxmhFKkm7G2zUKykVzWoCu-nQyWzhTyJkFLAecxoElr3Hqhmbw4vWYrAVIVtpdVadapprg4eiJd9tN_Xl6hMJRqeiLxDOL1WDe9i9FKQTkgYjfpCsZNqTPmW3sZc4TD-V5E2F9Wt-XNqaQgEWIcKjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncLzYKXSELUGDffKfePQ7uS-9gglwHsr6K27_SGmIAihJLpwwzrLLjhQfvQUU8cHZyMAn-GF3zNz8OEepQbzfxG3zedK2zB8TygRFXSO6JXZL4KLfMD-j8cs887RTFNKPEIQnhr7Uzq05zhjNCD6CX9VaYYoPzuFQx0owDOiidsgPc0c2Ni2lvcOIe30yzYVRRhrZm-9gVdIb4uR6Wm8z-G2PPJLBj0sDdv5AplC7_WnXbT6joLXgzefc7qlppK2VYkDl0dO_kIzIlpekPkmnOaQH8MwyqqbLMa6qPXJQcXqdc1K_XW4kr0L0lXs_0bPdB8X24lh-aTgdQDa_AxhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105778">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هایلایت‌درخشش دیشب لامین‌یامال برای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105778" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105777">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPfrjXxbofT79vJ53oxvbME7glzuo6BrY-qk0BuGUBGkM6cS3F-6aRvri54rlBHRCYXkHtH1q-cOUVkhb_TccROViEyvZBoom3RYpYxA7mzj1YJzGT4SBmeZkiCFRwOuDV_OXwxMDoe0ODOE_MOU9Hj6v0PHefbnluf0vbyIShorx_2jr6UE1AFMNjirMPKQ0Y_qmV3e9drgkGB-uKIkeXc5vlOX4k-17I57b4Tqk5OUTsXOb1FBkWay0yE-XT3MT6VhWSeSdo8gbNg9codtUNTFad2yagbybyJ7PiLJisvXkjOE54xDk-A6fIcp7M6Ro5ANsP-gF28_Hq483j-KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
بالاترین میزان حقوق در بین سرمربیان جهان؛ هانسی‌فلیک بهترین سرمربی فعلی جهان در بین ۱۵ مربی اول لیست قرار نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105777" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105776">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
⭕️
با اعلام سازمان‌لیگ ایران، فصل‌گذشته لیگ‌برتر بدون معرفی قهرمان به پایان رسیده و جامی به استقلال تعلق نمی‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105776" target="_blank">📅 10:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105775">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=PtbESKO-RjlK0ux-bdW8kBU7sql5k2dMiHQcPbmK4ajoUnHAAoPzqCI9-GJgNjBYZL_Q8E1008nm3vrXWo6cqHxKra6c2Y4uYDblJTFgUOeALXjoXDuIFcXzkDWvKpyIWiFpJh7qp2m6GdSYTLmleWmWjDUcqKvM41EsKxI9yfSVO3GzXFM3DVDCs7t_xvh6tMiboHo_k2a2feciCl8qfHLSTymoS5-dYuyGgEH_FoZIoiftfPFzGDcnPIdkROadHvpq4qSOyGMzSBp1BcUaNZimsr4LLdYpIJj-aRU3ANvMclXsTVJl5jOJWcFGyORG9c9LP3D6LBzewsT3KjwYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=PtbESKO-RjlK0ux-bdW8kBU7sql5k2dMiHQcPbmK4ajoUnHAAoPzqCI9-GJgNjBYZL_Q8E1008nm3vrXWo6cqHxKra6c2Y4uYDblJTFgUOeALXjoXDuIFcXzkDWvKpyIWiFpJh7qp2m6GdSYTLmleWmWjDUcqKvM41EsKxI9yfSVO3GzXFM3DVDCs7t_xvh6tMiboHo_k2a2feciCl8qfHLSTymoS5-dYuyGgEH_FoZIoiftfPFzGDcnPIdkROadHvpq4qSOyGMzSBp1BcUaNZimsr4LLdYpIJj-aRU3ANvMclXsTVJl5jOJWcFGyORG9c9LP3D6LBzewsT3KjwYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
هوادار روشن‌دل تراکتور خطاب به شجاع خلیل‌زاده: به قرآن خیلی جدی میگم راموس ناخن پاته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105775" target="_blank">📅 10:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105774">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=I4R50W0U9s6ILu6X-L7Y_ZG6w4TABNlpUpq07I01tVOvaP-Ot91JyKMzSc6nl9wOK2PsvOMuQ2gFRAkm59nccNBKY1DuV4XKeyWMFRYLj6TPILOyhcZ0DqOzqbHuN9pWNzThkKbM64H7J9MztS-FsGIvnThsjBaZRmxKNu_LPEQe-L-F1hGNbHYbCPAMcUTt5McT6YCED_iLps394j-oTFjzwrALyeiuCj28Rglz25hJv2Gz01SGgY4v_BjyCWeUE-60eN49tml0NUuQyXRUq1rD_qBWW53zKEHHlSXXUMjWoKz1Zf5XKjUdwGilG7IxyoY0mIZOmYXnKZChkIievA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=I4R50W0U9s6ILu6X-L7Y_ZG6w4TABNlpUpq07I01tVOvaP-Ot91JyKMzSc6nl9wOK2PsvOMuQ2gFRAkm59nccNBKY1DuV4XKeyWMFRYLj6TPILOyhcZ0DqOzqbHuN9pWNzThkKbM64H7J9MztS-FsGIvnThsjBaZRmxKNu_LPEQe-L-F1hGNbHYbCPAMcUTt5McT6YCED_iLps394j-oTFjzwrALyeiuCj28Rglz25hJv2Gz01SGgY4v_BjyCWeUE-60eN49tml0NUuQyXRUq1rD_qBWW53zKEHHlSXXUMjWoKz1Zf5XKjUdwGilG7IxyoY0mIZOmYXnKZChkIievA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه تند رسول مجیدی به فحاشی خداداد عزیزی: والله اینطوریا هم نیست که همه جامعه فحاشی کنن
…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105774" target="_blank">📅 09:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=oAntxmG-z4ObS5-NBFTfP5-pp3AMiJdQ_N7HR9pbBTuFV5xtgWS3QPE-cBMhcVl1uTCOh5tL0CAMQB8cWrx8r_SasFVr7XiKlU8GtK_1ykZ7IjnCg7U2RzsPhqcFDCVik2mt0lLiN8-rjwDMDP7vGNcTsFhHvhcZcf-vdYFqsLaKSUrhdJc_jw0innjabe_5yHO1ntWtVANO4XrNS6L4mnt69YQcpinb5x3oniq5IgbPl4Q7FkFGrC4Zi2fwAUN1mfrfDrlq0vHxahxtJDYU16QouAtdocb5bJDmE7eBgpVVT0tEGHow9q-80ZLjlPkgIaaBr7b46ajGvfPBREeNkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=oAntxmG-z4ObS5-NBFTfP5-pp3AMiJdQ_N7HR9pbBTuFV5xtgWS3QPE-cBMhcVl1uTCOh5tL0CAMQB8cWrx8r_SasFVr7XiKlU8GtK_1ykZ7IjnCg7U2RzsPhqcFDCVik2mt0lLiN8-rjwDMDP7vGNcTsFhHvhcZcf-vdYFqsLaKSUrhdJc_jw0innjabe_5yHO1ntWtVANO4XrNS6L4mnt69YQcpinb5x3oniq5IgbPl4Q7FkFGrC4Zi2fwAUN1mfrfDrlq0vHxahxtJDYU16QouAtdocb5bJDmE7eBgpVVT0tEGHow9q-80ZLjlPkgIaaBr7b46ajGvfPBREeNkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تماشایی دیشب رودری در بازی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105773" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXDhxDVNy_9wpcI8cH1-S5UWaIIaq3PU-kHBln9XyjAWYneQILZzzdzv7xm8urPJXq6rre0Uf4kadXqYJLd8pJPBxTN1Y5Nx_bKbalfBCvytz4kC8_Cwpyg7HgHDY9jwgLHB96z7xC6IBRwoqnueLMX4EMveMAdCNQGYW88ViBnPC8cmqxiHuaWqSMuDPqkzgzhGyODtE8ywzzLKuy3Jqtnhyt8iY5Hdtsfch7W60JjYZPq6I3xh6iyXoNwQrIrCovg1KDNtggSV8POY9nbWXgZaPWgARPKa_1LT14tCpp5ZcjIJyV-bHQineFZc_mZjH8YgFlNsD5KjfYcskV_uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105772" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=mL-kxWTNAV_nRtFxUYMyi8uFMFx5Sdv7Bq7F_BwRp3YuuKj_jWorgClrGIPnAZalIslbII3s81HyYVI04DT3pdJTXcKet7bSfJAitmsrtlLeQrIjL9gdMBlSVe-nOzuCO2nktK48BshsOCAGCBvwhMOeOA18X_FxJ2fMt0jhZHOvw3nFO-bHlkIT8GyvF-lS25_C24WMGv4Lj6chgOekmE1QY0Q3usTXbHceDA_5COiujO2BwwbzX8vbZI_dQ8QIt1yR3yflK7PXeDzCm5eDx5LRdRLJCMBFGlIMYhKyqEXP5tOQ2o6N0csMWlu65P4KC_i_uimAcoRmi1kElBTn9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=mL-kxWTNAV_nRtFxUYMyi8uFMFx5Sdv7Bq7F_BwRp3YuuKj_jWorgClrGIPnAZalIslbII3s81HyYVI04DT3pdJTXcKet7bSfJAitmsrtlLeQrIjL9gdMBlSVe-nOzuCO2nktK48BshsOCAGCBvwhMOeOA18X_FxJ2fMt0jhZHOvw3nFO-bHlkIT8GyvF-lS25_C24WMGv4Lj6chgOekmE1QY0Q3usTXbHceDA_5COiujO2BwwbzX8vbZI_dQ8QIt1yR3yflK7PXeDzCm5eDx5LRdRLJCMBFGlIMYhKyqEXP5tOQ2o6N0csMWlu65P4KC_i_uimAcoRmi1kElBTn9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران آرسنال دیشب حسابی از خجالت مورگان راجرز بابت عقد قرارداد با چلسی بجای آرسنال دراومدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105771" target="_blank">📅 09:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=vNUdKWzf2R0-gupIX4ItfqESDfmkNDaGKQz4VmIaNnxI7OPW4wgafaM2yH_E2LzvGHj56yi3DRXDoTg1JkL2r-XHMpYFtY9B9U-tDk5UOB0s9opaGp-ZKUEyTXeuHOEcxO1p90zTu_-d2TOtnvQwZTSGkuK6hHrhQy5e121B6UU3O6ys1_ctN6NMH5IpQi7-LGKDbJdbx9hbKYkuDceAh9AT4Gc9fCH9tOa83lTLKUyLMHR71L3PxeY_odbO9bUigENa23ZaOv0_wvBhX5xFTnRZcKWjQAPMXUlHF9t5qLe90i-0qZ5lLkh_-sTIVN8T17zI6ZPuGaTym89HAz9ilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=vNUdKWzf2R0-gupIX4ItfqESDfmkNDaGKQz4VmIaNnxI7OPW4wgafaM2yH_E2LzvGHj56yi3DRXDoTg1JkL2r-XHMpYFtY9B9U-tDk5UOB0s9opaGp-ZKUEyTXeuHOEcxO1p90zTu_-d2TOtnvQwZTSGkuK6hHrhQy5e121B6UU3O6ys1_ctN6NMH5IpQi7-LGKDbJdbx9hbKYkuDceAh9AT4Gc9fCH9tOa83lTLKUyLMHR71L3PxeY_odbO9bUigENa23ZaOv0_wvBhX5xFTnRZcKWjQAPMXUlHF9t5qLe90i-0qZ5lLkh_-sTIVN8T17zI6ZPuGaTym89HAz9ilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله شدید وحید قلیچ به خداداد عزیزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105770" target="_blank">📅 08:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105769" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwwRFUd8BkkKTCEGe88BEUXO11l4Iv9EVFM4rcDw3NOXyTzthxSCc6VhWkI-xpQmm02GxwI0U8lnbbLqeFQN-M28pMnqghG5Ew6ngQJTqbDS3P7zUD4juZRf5MO9RYumzinej4FDuYr2bV1e7wmvEqpTX5heoZRnEI5sAzwiOnDb_Uox6fMVJv1CUPasxqMnmiDwyshGOR5apl28JKhRnFB8Bsr96aeq_WlUav6mV8wYxqBIhMGdrVBBXJDzqzDpSYYQxAOUCRV8UTtQEebou97PeBkPEgfbTBu8077cCDEXbUUmkFceVTxqhURjMlL4ZTSlDPK4aHQjcWCWFDGdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105768" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=RneZP1SUW5tITRIVVK36BkK-v2MaCyPn4XVRNHT3uvX_dnf7tycNrsCZLnRpAxFxQXnka3dQggEIGSglclFVxUVBVo07XBMAMvp1uKKm5G8UR2X6TPabwHiWlLmlFu4xPOIDSDXulh6z1ZGjSUx-zKzMcI9P5i7VU1ioZ1Fo-npy8L-aeecuiGvLflK2WYycSmWAROigUY_xtOAmA2uKwqkANOwtzqOCmOiyw8V7PKsQpqF1YW4y3ilLoNX2TXMM6g3inbmO2yC1cwlbWyYlIOuNFjtM5gbf7VGMX1608Qacrdbu1ncXGGfeGDE36w7wNnZNBRl-ZDntFecrttuETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=RneZP1SUW5tITRIVVK36BkK-v2MaCyPn4XVRNHT3uvX_dnf7tycNrsCZLnRpAxFxQXnka3dQggEIGSglclFVxUVBVo07XBMAMvp1uKKm5G8UR2X6TPabwHiWlLmlFu4xPOIDSDXulh6z1ZGjSUx-zKzMcI9P5i7VU1ioZ1Fo-npy8L-aeecuiGvLflK2WYycSmWAROigUY_xtOAmA2uKwqkANOwtzqOCmOiyw8V7PKsQpqF1YW4y3ilLoNX2TXMM6g3inbmO2yC1cwlbWyYlIOuNFjtM5gbf7VGMX1608Qacrdbu1ncXGGfeGDE36w7wNnZNBRl-ZDntFecrttuETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lroZVgwgFFmYB4v4ykz1bD7BmaUFxskgCSQv3r5bzz_H3A5y-y93ZCFCyBsbzFpTcmevEzi48sipJuVF5TnmbKt86vaZkO9rGVGNu6aclyITAL9Jx6dlYoE8NU6weO4OI8w_OyAlBL4xbueKcMxhBhFuLpqoeBBT3W_LXNzLEm7SYrQzpv4H9tD1JNvyNxCdABafOKDQNXH5T5q0arsiBvxls5Vt5iOJLWtXkcPVDMVNFowkxRizkaG1w8nyMdgKrNLIIRs5asbz9mv16F9sZKM8edPpY8is_nUGLmVifZCXpSzb24I2GjXL_aXWZ10OVkefuVuRiOvUBVu4VuidaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووه لحظات آخر مساویو زدددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105764" target="_blank">📅 00:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=btto2eKUc0jXf3YlbgKx3vUf0EKFUs3Wtv_1zbPXjfuIP6VGq6REL3QGuKkX4HNPV4HWH99WDMU5BfVFiii40WyZn-TXDmO2MVoEkS-kbqKKqqf3NcjtWgPGqQXxb7zr9DNCCC_kB-SW_Bt6WqF_UpjF7Zm0GAMpUxO1ILNRTvroAIYbBPQzJH2IwuIfHH4szqi5WrY6F5MysE1s50CrCOFTyiG0pRGYK_wnNHZ153w0HgtVrCA6_dwOsBM-ApoRgmnfP4C5P9nr0oza0UTFMU44B99NjeYczzTtfiCnkFn9A0LG_WR29JTVgRygysfvYWm-JbrAKYqMUoAzLKs5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=btto2eKUc0jXf3YlbgKx3vUf0EKFUs3Wtv_1zbPXjfuIP6VGq6REL3QGuKkX4HNPV4HWH99WDMU5BfVFiii40WyZn-TXDmO2MVoEkS-kbqKKqqf3NcjtWgPGqQXxb7zr9DNCCC_kB-SW_Bt6WqF_UpjF7Zm0GAMpUxO1ILNRTvroAIYbBPQzJH2IwuIfHH4szqi5WrY6F5MysE1s50CrCOFTyiG0pRGYK_wnNHZ153w0HgtVrCA6_dwOsBM-ApoRgmnfP4C5P9nr0oza0UTFMU44B99NjeYczzTtfiCnkFn9A0LG_WR29JTVgRygysfvYWm-JbrAKYqMUoAzLKs5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105763" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=OL19vg19ETj1yMSe8az6SlNNpqQWlOY63cq-z5__8bX81OCBRhpmztAHFb-P2F6lwQSNKcuD4Gwq4vrQjE7roO1Q8JTtU3C7JwcSPHlYhUeRhjV4Yi9ARAIgtHFgnnhUKR1_C5PW_fWWlfLzNlkaWcZ38AWBGqERb4IrOVz3UVGu_Pr6U4Te5CcdLR8u3vDOngRQuw3UXJ_GZElZLL1LhfbhUK5DTcMXs971ZfSC8u5A-_2rJEVExKEZCTDTSAHE7wD6-oh4FGTSztbL7JVwyuW_CnbyKRiULlWNCFU2ik_PqCLirliGiUX6RCflanQE3iTMcfsmL1yz1lsD5uA4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=OL19vg19ETj1yMSe8az6SlNNpqQWlOY63cq-z5__8bX81OCBRhpmztAHFb-P2F6lwQSNKcuD4Gwq4vrQjE7roO1Q8JTtU3C7JwcSPHlYhUeRhjV4Yi9ARAIgtHFgnnhUKR1_C5PW_fWWlfLzNlkaWcZ38AWBGqERb4IrOVz3UVGu_Pr6U4Te5CcdLR8u3vDOngRQuw3UXJ_GZElZLL1LhfbhUK5DTcMXs971ZfSC8u5A-_2rJEVExKEZCTDTSAHE7wD6-oh4FGTSztbL7JVwyuW_CnbyKRiULlWNCFU2ik_PqCLirliGiUX6RCflanQE3iTMcfsmL1yz1lsD5uA4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
واکنش عارف حاجی‌عیدی به جنجال در بازی با استقلال: والا یه ۱۰ نفر بهم فوش ناموسی دادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105761" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=u8YjFOFFPOaRV_i6nF6-DxzGg_R57jljjv9ckPWobVk6CyukBmu29GELscg4dE-0_Yh2HbKP7VGR2lntk2439gM2tAvUEIV5k7hIFElxyWXtvRO_IQIGzGChjwF7urmIw0YH_50ROKarAgtOpGkdS-02t9BJgb4zTm6n_4iD-CIgJ0jN0hjRarQXf4MigmTho8Pey8jJ2PAei5NrI7VpGAY3-i9OVEr1TAEmozx4BbKGTk5IbKOsZ2ajEYCEpsTvAuZwu-LFRltzFSMhTzzrEmcF0TQzMglL60uhj6wjO8gI6PbAwT3Imylfw2ZrcFfxBe2QGRDTKgNZRvfT0ClXwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=u8YjFOFFPOaRV_i6nF6-DxzGg_R57jljjv9ckPWobVk6CyukBmu29GELscg4dE-0_Yh2HbKP7VGR2lntk2439gM2tAvUEIV5k7hIFElxyWXtvRO_IQIGzGChjwF7urmIw0YH_50ROKarAgtOpGkdS-02t9BJgb4zTm6n_4iD-CIgJ0jN0hjRarQXf4MigmTho8Pey8jJ2PAei5NrI7VpGAY3-i9OVEr1TAEmozx4BbKGTk5IbKOsZ2ajEYCEpsTvAuZwu-LFRltzFSMhTzzrEmcF0TQzMglL60uhj6wjO8gI6PbAwT3Imylfw2ZrcFfxBe2QGRDTKgNZRvfT0ClXwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش پیروز قربانی به پخش آهنگ "نصرالله معین" در نشست خبری بعد از بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105760" target="_blank">📅 23:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
🚨
🇮🇷
🇮🇷
محمد خلیفه: تفاهم‌نامه بین استقلال و آلومینیوم خیلی صددرصد نیست چون ممکن است استقلال مرا نخواهد یا یکسری اتفاقات بیفتد. حتی اگر قرار شد بیرانوند به استقلال بیاید، با او رقابت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/105759" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=OIiYTFnZ7yttcWgj4Q3x2W7dbclEXCyCdiK1iiv7_hsConaeotcDBT2M8SAlJ8eEjwIlTlOcBWRwHastF23PI-czhiHwKPj_M5VynJjewkVMa4EaECbePeqzh-M9rp6MIKy6-Zqtc-5iHYmNRQ_Wtj_9ZkMqN9aravpasvXgDFwvYyYCUPlqWhg7fXLltdputVtl00Dugq9cdKOvJ_1B5h4nEKcX0w2Sdhf9L6QJ_3KLFiQC6-wrGLtJr5pkUI6k0zg9Lstibb0Ms5q1On1cL2dy5ABBZ3drtEd-8JIskHu4jBVjMkkEA7MGp2F9qVGwCcQlepLIEhdQDeY60JH_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=OIiYTFnZ7yttcWgj4Q3x2W7dbclEXCyCdiK1iiv7_hsConaeotcDBT2M8SAlJ8eEjwIlTlOcBWRwHastF23PI-czhiHwKPj_M5VynJjewkVMa4EaECbePeqzh-M9rp6MIKy6-Zqtc-5iHYmNRQ_Wtj_9ZkMqN9aravpasvXgDFwvYyYCUPlqWhg7fXLltdputVtl00Dugq9cdKOvJ_1B5h4nEKcX0w2Sdhf9L6QJ_3KLFiQC6-wrGLtJr5pkUI6k0zg9Lstibb0Ms5q1On1cL2dy5ABBZ3drtEd-8JIskHu4jBVjMkkEA7MGp2F9qVGwCcQlepLIEhdQDeY60JH_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105758" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNciYGtXIZMfHnWh5kgP7t99_MIEjK8LScoc4dTBlUz7zowM376ww0ujI6H-xABkEI8vVR7gQlTk1i2sXAzwa5VtyKARIrZqqnKHyFvW_GEhYPmVI0jKNoEVap8eOU5eFkb7rGLFLRB40Z6ULqgZYixqPyMBOLZXyhn9eoiBhnB7xwI3w7TnTjAl8hTf04z5Ovd9xBkq026_RTtZLcheXaKaDrztSunY0MXeaoLVpXYbhgcolIu1UWWAUM8hHO9bm0Q4nAnOg0FZVgW8brfw82N0zjCVQeL8wrfNvWy0dn9gt-lG4QBSypnOZWYXIPFO3XZz2REouwZfPed44gn1LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فکت
؛ آرسنال در ده بازی متوالی لیگ‌برتر مقابل چلسی شکست‌ناپذیر بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105757" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
🚨
💙
بیزاتی مربی استقلال: ما هم از نتیجه خوشحال نیستیم. قطعا مشکل گلزنی را حل می‌کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105756" target="_blank">📅 21:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=VuEwBZg0oVgnPf1XazJfvdbPJeYE2UmRzp1VIt0zBmWghGk8vCrkowOfc0x0QvApar5OVVLw5ocl-Ec1DfJ2zI5a24LlsCajnEcJbEQ62h3Xv386tBcHor4YvX1B8jiSgPfE1sNKR8W8jaxCWs_SSLjLur2MhC_K1O44SoN6moIZ8PsD_M683CzGGXGVmo9nhim3LFIQJ3ldR2FMGgI3YkaDWKf-AbPkKBl-Lm31O_fFMUt70XhQ5ds1UizZoXm9bkwzKcrTFJcCoTwVuT-onDoCNYmNmkgUxQ4yZ1Nylfpf2ORKUsK0Y3JUQMs9MAOCR4Ggf_uGEalmMyL6ShCPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=VuEwBZg0oVgnPf1XazJfvdbPJeYE2UmRzp1VIt0zBmWghGk8vCrkowOfc0x0QvApar5OVVLw5ocl-Ec1DfJ2zI5a24LlsCajnEcJbEQ62h3Xv386tBcHor4YvX1B8jiSgPfE1sNKR8W8jaxCWs_SSLjLur2MhC_K1O44SoN6moIZ8PsD_M683CzGGXGVmo9nhim3LFIQJ3ldR2FMGgI3YkaDWKf-AbPkKBl-Lm31O_fFMUt70XhQ5ds1UizZoXm9bkwzKcrTFJcCoTwVuT-onDoCNYmNmkgUxQ4yZ1Nylfpf2ORKUsK0Y3JUQMs9MAOCR4Ggf_uGEalmMyL6ShCPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
⭕️
نرخ سوم بنزین به مبلغ 10 هزار تومان تغییر کرد؛ سهمیه اول و دوم بدون تغییر
سخنگوی دولت جمهوری اسلامی: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105754" target="_blank">📅 21:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPlVy_m2ccHFA6x7h2r18Wa1JfpTeBIwyhHlkBqdMNAhoLx9KRot4Oxpmz4bTqGAa9YpcOhRISoqGnup0lgivHo55EbRfOL-dLlpFVwwi_jIxIBR4Ff7yY-f9x9ahtvS8zOqGskCUkg_aU3_a6_dfEROpzvKg0R9Q7HsLOESoLlmiUl55wREjpeGW_Mx7oXT7wcFhFKvgzWw4JpeNpkijtvTHok0e7gvu7HvZfevPDGCDSWTk8YjhKwbJCJ6JFH3hOr5Iux579xexvroMxF5n6ogsmP9yMhez1okw8c_rmeWgNHPnsg_U9fc_bHeT3U4je4H5rOuVI7kTQQORuBfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105753" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuETsWoO2aWsMAAGY_UkIFdqJ6U2UQf5bXhfqdVr1MlFdspiEndL6PmloWDpd0geMUlOPbGkoP1JkvTQ8Q1sysK4avwpfXYg6YhIXM8GtBhZzadFjr_DRmgR1qerNY00ukC5Gi9gRg_d0uoSLaWZ3Bm9uE25l0D-A__wAqUaAPS7VmSnRKS3qRYQS2yfF0I9RaDyucT3QW4cv3TymfoSJSwhkA8HvwV0jp7qg6tPMMoU_hl6pg5vzYItI0-uqmJwE0tgbOkhlRvh-UuEDWEvN29hKJbbB6JXzyX7FZscuUsJdqsqMMDuZiHVqyenwMlyd_nb5DHqOJClDPVEJYuPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105752" target="_blank">📅 20:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105751" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105750" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=shxo5uaYHmV0DkvnLs_mUI4cFt92qOpZQvb16LyKQWPtov6mhlIp6DCrkl3kcfmZXlFTAxktkIjoqOHsukq_6AE0gQQq_AKaBGcWFn95vCsZ9jXXzu72OJD0NsQyNLX0a6fxkY0VV0gAm5qvSp0y72fVWmxWM1T7mcOSiKrmk2pzDGZ7Cc8yute4_wzcV8_4qUqz1kedqcMand--yGYMv4Ml_xXMkluPMAGT83pSFv9-MdckRIwGVYb3T4X1xYdvr4OZwWT_m0GdnxY0JH4A47Jf7xAPWFAIocyqiNNPGw8qfKzvlKXZpMKNVTKCbIijeMdepTMGbMqigyn_8ZcZzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=shxo5uaYHmV0DkvnLs_mUI4cFt92qOpZQvb16LyKQWPtov6mhlIp6DCrkl3kcfmZXlFTAxktkIjoqOHsukq_6AE0gQQq_AKaBGcWFn95vCsZ9jXXzu72OJD0NsQyNLX0a6fxkY0VV0gAm5qvSp0y72fVWmxWM1T7mcOSiKrmk2pzDGZ7Cc8yute4_wzcV8_4qUqz1kedqcMand--yGYMv4Ml_xXMkluPMAGT83pSFv9-MdckRIwGVYb3T4X1xYdvr4OZwWT_m0GdnxY0JH4A47Jf7xAPWFAIocyqiNNPGw8qfKzvlKXZpMKNVTKCbIijeMdepTMGbMqigyn_8ZcZzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
گزارشگر اراک: محمد خلیفه ما رو یاد جوانی‌های مانوئل نویر میندازه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105749" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d287258445.mp4?token=l2vxhMUyxwI04dAkRnGbwQPPvVST-BemhWmwZb2tRqDYtQ0-zz8mj7IJy6XfKg59mMkY8fOZfLz8_fBBKTptl0xkvQrCtKiQlmR_7w_tObLzYhglJ_myi1G0TOtwfELeLSgYhk0YWxcuhDXjfeSAoQKZ12pySZjfBMQIDwjmtZPE6bw2K5yeZc2ruICWbtJ2Ida8U7u7zISGbb4kV16lolBr9VkT0YNt3G5fLRVioeHPQ3kqaAOuhRUoppICMdev7841BRyBqhFbyM-g6bCA8YHZ51ZasnlVRdIgSp1ihpg6iKKnz5Q-OjaEdIvLmPq2bG8mN5EmdGWR12HIw-Liqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d287258445.mp4?token=l2vxhMUyxwI04dAkRnGbwQPPvVST-BemhWmwZb2tRqDYtQ0-zz8mj7IJy6XfKg59mMkY8fOZfLz8_fBBKTptl0xkvQrCtKiQlmR_7w_tObLzYhglJ_myi1G0TOtwfELeLSgYhk0YWxcuhDXjfeSAoQKZ12pySZjfBMQIDwjmtZPE6bw2K5yeZc2ruICWbtJ2Ida8U7u7zISGbb4kV16lolBr9VkT0YNt3G5fLRVioeHPQ3kqaAOuhRUoppICMdev7841BRyBqhFbyM-g6bCA8YHZ51ZasnlVRdIgSp1ihpg6iKKnz5Q-OjaEdIvLmPq2bG8mN5EmdGWR12HIw-Liqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
استقلال از کوووووون آورد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105748" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استقلال داشت سوپرگل میخورد
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105747" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105746" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=OuqH17AjyvoOlSK5rlp8rOj8Z5hVbSsfWO6mgn0ArpUD0WOV6od0K2P52dmCKrxk7aGv4sjLHgylzeTbJQclm4WOSB9TlFaRQI8-LUV2xVabOt0lDcvTfJ2qAtTkgdiMttrsSNqhtRguweNwBko_0IR4uO-ABgdpB3R9Wq6CM3w-KfWAVT5wa7INuhNstxW8UEPgMep_hz9aepGeAqii02yp9aDOhmU4fjrlyBv2fhrLlEvsOTh5Ov-Ty9tV9fPtjlKzPZVXPw666fGZb9s16CTKZCEHsQkOaWYd_aG1iQ6qh8vJ97uQV9SVFsp9rlp1pky0crunLDBKJTvKq98BhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=OuqH17AjyvoOlSK5rlp8rOj8Z5hVbSsfWO6mgn0ArpUD0WOV6od0K2P52dmCKrxk7aGv4sjLHgylzeTbJQclm4WOSB9TlFaRQI8-LUV2xVabOt0lDcvTfJ2qAtTkgdiMttrsSNqhtRguweNwBko_0IR4uO-ABgdpB3R9Wq6CM3w-KfWAVT5wa7INuhNstxW8UEPgMep_hz9aepGeAqii02yp9aDOhmU4fjrlyBv2fhrLlEvsOTh5Ov-Ty9tV9fPtjlKzPZVXPw666fGZb9s16CTKZCEHsQkOaWYd_aG1iQ6qh8vJ97uQV9SVFsp9rlp1pky0crunLDBKJTvKq98BhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌اول سپاهان به استقلال خوزستان توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105745" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=ft5He80Q683vQWZwUeE8Ljz_eU7gKFrVwlwCs7bgJINMHINRbw4eeMDvO2q34zGPAx22uc2dKFmWcOZrSZJnYcDbYFysTWhNOiEYQHaKbhq0XtEz6ZxeTHVkkCGA_ICVAlE0rsTaGHOlbVnyAnJUIJkA3ZqRTSasUVPIIZXDfiEOZ1cAnDdLr9fRXtBg6Yawkp3n9jTsdAri14XLZY1iAZhuzCqIa3-NxvUxTYmxzylEx9HHgnCnl793SPlQvmnNWXOERfURli9f03hNomm8i6zGSoneOCsFNlG6EA1Sf7BN6kDsQCTrUHCgE_wcBCn390xvhwSeL5NwBe448wQiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=ft5He80Q683vQWZwUeE8Ljz_eU7gKFrVwlwCs7bgJINMHINRbw4eeMDvO2q34zGPAx22uc2dKFmWcOZrSZJnYcDbYFysTWhNOiEYQHaKbhq0XtEz6ZxeTHVkkCGA_ICVAlE0rsTaGHOlbVnyAnJUIJkA3ZqRTSasUVPIIZXDfiEOZ1cAnDdLr9fRXtBg6Yawkp3n9jTsdAri14XLZY1iAZhuzCqIa3-NxvUxTYmxzylEx9HHgnCnl793SPlQvmnNWXOERfURli9f03hNomm8i6zGSoneOCsFNlG6EA1Sf7BN6kDsQCTrUHCgE_wcBCn390xvhwSeL5NwBe448wQiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال به چلسی توسط مارتین اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105744" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اودگارد گل دوم آرسنال رو زدددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105743" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spd3gw20qQHayaQeKa1pREwtwM4bEU3cspuL9DuOh5Z6ogbMnwbwspS0Xk5lakFLqDSQ_ZSMo6MMQhM95jn1tAksNHqyfoPPHoywwdij5sIA7HXMuLy1iV2HSMZ2bVM9L6bMzBQCjYDMZavJROpmepvEsDLyYmmVxekViIQVqKJfmBqdurgxVgiaXKTWvnkQuwgMbrA2O3VDtqP_TW1SzMYcD0G0uIpGW45epM3_X32rY_w01bWwspHJ7VziZ_6qBEotlFmkIdSGlLm1eXRxvJcYGw4RwXcXTnoAG0eE39Q3m83vK4ZX6jgtBcM1goKrhflP6Gr3eKtn2b5IVADQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🌟
مربیانی که بیشترین تعداد پیروزی را در بارسلونا کسب کرده‌اند، پس از انجام 80 بازی در لیگ:
🥇
1- فلیک (63)
🥈
2- انریکه (62)
🥉
3- گواردیولا (61)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105742" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVhbWkpp1exP8YvudAHeE3x-2JRGJnsFM3HJ6x0lnJ_za_3sBghk2zKoMlEpWuUubBQKEJdIWSwYapYXIN6GxrRkytfoSyAtAFsYZbEERZQYfEs7oYWa3aeiNtNkbwSGbHomQV-wQ_C1Ss3Bz3D1g2887tG_el8CvMAoLXlRRVaWZBUUVvrVdkqVqhdZTB_TddzisMDFwq1oyH0bfkqdq6F0GuV_NJp0CZ_hEFnmp7ZFRVDUbUg7f90IDBJzth3XSld2Fz6HJV788HrGR0n5tPBy3e_MqK1w2LOpxdYf2m2FHfE9O5mTLQKLltuPehwHzEnzjT7k0eABc2MAzkAtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌چهارم
لالیگا| خفاش‌ها اسیر درخشش فرمین و یامال شدند؛ نمایش فوق‌العاده شاگردان فلیک در مستایا
🇪🇸
والنسیا صفر - بارسلونا پنج
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105741" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=StPZICAjJXKeGJQNPDyPJRxHzDD88gCvZDdEXQUJ7j--ktL8HukvcZ00SH83aXk9m0JRf0SROoDXcXXce1Szjb4qjbOMqF9GMtFAm8YAcvDAGAIg2HLctwdxGbzF51TS9yS0bjShOqjrBQf8jX6kPA6CHHDJXBtUZ8Y5w92MQJygcC4xApHDgkGYzpQ0LMTCnYUGEWxoec_izyy6hh_tlNLlPPoSVlNqH9XvW9yTmIGN8Ib4Ro5zhfszuUf1xnix7EKkuRVq6a0YrOi3Cs1s4Sg-dj5NekjJVpEuUO3InkyLa7KnE0tsmCO-1iVo7DTLjVhymCwHzhjwinCL8-FY2o95wcgYLE9g3MiHfYIQZ5ANlRHsQ-sJaNmdTtj2jdSehAmeNm-OoCbg0TM54J60XfnBDCywPgNvLMJ2yZPtjz82Qeaqt8PnDDAg5RG93vmJfZG2P1I5zp-GTO494g_hKCvCbQt3bwa6jF8FuPiqnHhW3QWA5jOHHYSOc6W33YazBqlBsPoshPYP5kJl0tILepfSLQLRHrxnqk1NX9wmE5gjAlgY9E8FX0Pon8GJCWc3BYf_CbAl4bO6IrtOb2m3nr1VL7T3KXlAJ_nE9NaRM7_CITcSF91VSC-32n599LHNLMIbfCehayRt55x3eQsgTcT-jwx9zLxEbbNBAoyRghw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=StPZICAjJXKeGJQNPDyPJRxHzDD88gCvZDdEXQUJ7j--ktL8HukvcZ00SH83aXk9m0JRf0SROoDXcXXce1Szjb4qjbOMqF9GMtFAm8YAcvDAGAIg2HLctwdxGbzF51TS9yS0bjShOqjrBQf8jX6kPA6CHHDJXBtUZ8Y5w92MQJygcC4xApHDgkGYzpQ0LMTCnYUGEWxoec_izyy6hh_tlNLlPPoSVlNqH9XvW9yTmIGN8Ib4Ro5zhfszuUf1xnix7EKkuRVq6a0YrOi3Cs1s4Sg-dj5NekjJVpEuUO3InkyLa7KnE0tsmCO-1iVo7DTLjVhymCwHzhjwinCL8-FY2o95wcgYLE9g3MiHfYIQZ5ANlRHsQ-sJaNmdTtj2jdSehAmeNm-OoCbg0TM54J60XfnBDCywPgNvLMJ2yZPtjz82Qeaqt8PnDDAg5RG93vmJfZG2P1I5zp-GTO494g_hKCvCbQt3bwa6jF8FuPiqnHhW3QWA5jOHHYSOc6W33YazBqlBsPoshPYP5kJl0tILepfSLQLRHrxnqk1NX9wmE5gjAlgY9E8FX0Pon8GJCWc3BYf_CbAl4bO6IrtOb2m3nr1VL7T3KXlAJ_nE9NaRM7_CITcSF91VSC-32n599LHNLMIbfCehayRt55x3eQsgTcT-jwx9zLxEbbNBAoyRghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌پنجم بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105740" target="_blank">📅 19:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kio_V-K5lZgakyjKA_CbmG91kX70LxexdESaN-JRqy7wu7fvngJlQ1r-Bwf2E373gmXV9MEOtgwnJvyZWQ9sLMsBAyu7piDo_zt16UwUApxe8vly-qF439Mta6QO9NPsdQA3Wr6kEB0HH82zMC_2TuqqvrGIaVnz3IOhUGXNA5wN9Fp_YXGIn34V6n6IsPIqo0OqHrtFLHOdFfAyjS1Mzh2jaf1Q9XwHLFFQlbd4Af0wP_4lEfsUCGbiT31uhdqYZkbDoKjkn4D_Ck8hlLqItLkvuBAEuTt5R9JPGSsIDWfkESdJEtM1dWrCcL9EAtZNqhLsVUnShfGjPHGc6Wfbrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لامین یامال به صدمین گل یا پاس گل خود با پیراهن باشگاه بارسلونا رسید.
فقط در 19 سالگی!
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105739" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">لامین‌یامال زدددد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105738" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بارساااا ۵۵۵۵۵</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105737" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105736" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=BZ_U0fq27dZz-w3K0PUS3T6ivrZySE149Ehtu-jOFKCQADAHhnW3e1FLxUnMLwwYuTJuyQ4gp_afUJ1_sd2NVaUFD8fU8zuejVBbsrikGdaO0nCbgQbXa73dz5sfxQtri2_Lg9dTH3tgRokYz1-8cvLv4l67e1F57gs6Z4daA-NcH2tqVAR2bX9_g0_itNIggrt1BvpoCHZkcoUi0iuLMtAhcaLO4maavFW_rbu1TfjhvENqJ7IOLLsDo03j6y02geh05YjcfnaZ6qWnx8rjRyw45bkRwzJS10Y-8Qxb6MniTsCo_XSMAXZViCb2mgwQqTNssHxQtcRBWBv8EjdtNW8nN8QGx9Ub4m6xcT_eHs7wHxWfUxV2VJ3K9zLdom-UCo7P3jAAghVY1RmlKCplTIaRLzW7L7EBsul41cXpRAV4JWXXEbSrkzM1HKHVZy8UQEy0Ey8VT5nq1T0LafFyTxDCI48nTOiS-IkaiG45EfOkv7MS8LoqfdnThBX-Fy_mjhqtG8Q5foA3UTqQ4z37-YKdceDELCIHn0fi-wtjy0EDp6weLK-BjDn-3vLJbmWa-c39pbgUw3A7yoMvfje8iz9YgoL0KnFLScDbHGFLs-4fFrFoS5Zl7dFcbr3H49FSGzCW9f8zZOim00eyoHjEQsKo9ByBGlnIKpdXBs2M1ns" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=BZ_U0fq27dZz-w3K0PUS3T6ivrZySE149Ehtu-jOFKCQADAHhnW3e1FLxUnMLwwYuTJuyQ4gp_afUJ1_sd2NVaUFD8fU8zuejVBbsrikGdaO0nCbgQbXa73dz5sfxQtri2_Lg9dTH3tgRokYz1-8cvLv4l67e1F57gs6Z4daA-NcH2tqVAR2bX9_g0_itNIggrt1BvpoCHZkcoUi0iuLMtAhcaLO4maavFW_rbu1TfjhvENqJ7IOLLsDo03j6y02geh05YjcfnaZ6qWnx8rjRyw45bkRwzJS10Y-8Qxb6MniTsCo_XSMAXZViCb2mgwQqTNssHxQtcRBWBv8EjdtNW8nN8QGx9Ub4m6xcT_eHs7wHxWfUxV2VJ3K9zLdom-UCo7P3jAAghVY1RmlKCplTIaRLzW7L7EBsul41cXpRAV4JWXXEbSrkzM1HKHVZy8UQEy0Ey8VT5nq1T0LafFyTxDCI48nTOiS-IkaiG45EfOkv7MS8LoqfdnThBX-Fy_mjhqtG8Q5foA3UTqQ4z37-YKdceDELCIHn0fi-wtjy0EDp6weLK-BjDn-3vLJbmWa-c39pbgUw3A7yoMvfje8iz9YgoL0KnFLScDbHGFLs-4fFrFoS5Zl7dFcbr3H49FSGzCW9f8zZOim00eyoHjEQsKo9ByBGlnIKpdXBs2M1ns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌چهارم بارسلونا توسط پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105735" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105734">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=BK6UstyXV-lNxgrItcn6zLPFMPWDraCz2oCSOYakiRiHj9QqoS04jAuDP_9uNYNvymQoCDVwLFePk1PSkS7lI8IpISvc_9lTWEM_onMMrGoq0A3f9jUxxausZaO9NciNzFEmtccGc8rE8b-hmIagLUx2C6z1WUBXgKedAl1mtC8g-xFs1M4zLU9poMmPqI0eOaDArXA9DBFx3hLatxxHfB3vOW2Wmy62VEUYDZxVkmKzms6noelk8Fm93FqBK3NDcK_QW8DZ1L7giivF6OKEFWisCaKHluBNVfIUiCvzXRJesfD8h7rcSDP7hifpDA5L2WbGd2FrzvoRBJOD6H3mxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=BK6UstyXV-lNxgrItcn6zLPFMPWDraCz2oCSOYakiRiHj9QqoS04jAuDP_9uNYNvymQoCDVwLFePk1PSkS7lI8IpISvc_9lTWEM_onMMrGoq0A3f9jUxxausZaO9NciNzFEmtccGc8rE8b-hmIagLUx2C6z1WUBXgKedAl1mtC8g-xFs1M4zLU9poMmPqI0eOaDArXA9DBFx3hLatxxHfB3vOW2Wmy62VEUYDZxVkmKzms6noelk8Fm93FqBK3NDcK_QW8DZ1L7giivF6OKEFWisCaKHluBNVfIUiCvzXRJesfD8h7rcSDP7hifpDA5L2WbGd2FrzvoRBJOD6H3mxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت محمد خلیفه
😐
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105734" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105733">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یا حضرت عباس پشمامممم ریختتتتت
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105733" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محمد خلیفه چه توپی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105732" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پشمامممممممم
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105731" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
