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
<img src="https://cdn4.telesco.pe/file/YuffSiIJRxPQnemTXBhjKPPqlMtnMA7U45lbFksn5CRG5gkVF0l4Y0VMLzlLAzPjiLdAQdBLsRltrVDGyo6-X6j0KkDNJpm8O4XzLghknrILqVJbGDnVyFcbyPYfloji8m700-7jr-JH1R3v6Im5rpJIIpuYEgr1eMSvZ2iCadru761i_DLWDs9gf4_PgbTQajwy_BGkxUygrWokWfsyBJP6oOPaCNMggJFcoMovsSVpXvglycB7BWlXlOJiPLTjtSIZeXFuzBxoVN2KFtxHGWD3AfcbHR-PzKjKm0WvXRXO2myhGX9CzLDufetpoWVJqberjcMrulRy3rIW-eUQAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=fxY3sYIQnUGitJz9GluPireU255L2NQ1NQah29966T2l06jqbQZfJh1q_oItAyAxgonLs3lXzVnSuE2frDcV0C-0FnQEv6mgLcgjrBhzbWFenauE8CIh23Gl5KGx8Wwp7lBn3WbVINDcD2LC-RSMgXgCLABCoXAYCQ1bYn-Ub6WJrFwE-jzXaNK3I-dRa-nm7OyRjFeu5CKZOa-USszjuElSk_TFLTQVin648u9WDeS93Py5gOhISuQ6ClMBLCMChNRTC8Q9KsuejtvZ2EBoJFz24fmhpprl6-uIK-vEOAVLFuBjKE4-ERe2ZhMvDCdE6XC3pAlwvLqqUnS0Ch28IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=fxY3sYIQnUGitJz9GluPireU255L2NQ1NQah29966T2l06jqbQZfJh1q_oItAyAxgonLs3lXzVnSuE2frDcV0C-0FnQEv6mgLcgjrBhzbWFenauE8CIh23Gl5KGx8Wwp7lBn3WbVINDcD2LC-RSMgXgCLABCoXAYCQ1bYn-Ub6WJrFwE-jzXaNK3I-dRa-nm7OyRjFeu5CKZOa-USszjuElSk_TFLTQVin648u9WDeS93Py5gOhISuQ6ClMBLCMChNRTC8Q9KsuejtvZ2EBoJFz24fmhpprl6-uIK-vEOAVLFuBjKE4-ERe2ZhMvDCdE6XC3pAlwvLqqUnS0Ch28IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbqRS81I6dl_3R8TOESEgEtB_rCrtsKUtwXDFVV73iDIslQZxUyIf4G0wCD9TGWicMj5q5sU4zEYBFFgzI8_xahUghv8BhJB8LH-DFXQJiggGCJHJwzC3oRHVE0B8we9V-I4ldEs4IHtAqkXb_mL7HCkbfuteJGbq6LZPaerZix1QI0XcOuS51ttGllNE22LKZaKeVrQRnlK2pymDzIwkdPGeYVergoSrfis3khPYj-6hvMnGl3r4eHRmGTmNiph2HRKbvczAtsZdl2XJKK1bIJ3wJoXsa5hwHJSLYU7TzEtlQ_ptj4JVexp4DIrOPR4EpOSKwWi_ORx9OV2Lw83Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCifBJcmvWNzkkHO9bP26HCXu905TdnULK3CVRW5o1ir4phaa8OrmAhAPHtC4nqP1M63iL23yVWPVZ-tlbq8T-C0Jul5Jz6AKXEiyZugBJXWoNoFI8btuFlECWD4tNop4aOi8eoXhBtEp64qp3ZOlDWxoSeDO6XnUl_1F7T-D9Yc_P_hYpCJ6iNQ2CTYfRdTTUN_Q3lZ-ujUm86bLL8gyYBodr_lOg2JPxhUqc6VvRQP8dA0sjMDTIDaaQSJhI3Ccz9VAz93iPEkBwKV47cc_KTDnaXp90j3-zKCxENZdmBowXsoHBOhsmvk4B1e1kd7Zd5dym2-l1-6Nn0GSCdi6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhspRjEojEV8PG2r8UxMAe2vctmlZ72-y0HqNMrydiGPwS8jZbSILED-odMqbiqSYhU297aANDUvknewmSHgpYV9ksrjYx80DEOOdoYzNnhdUK8HVjYHRk9YYb3XqXXl_3-J5s45HeUSH4I039dX5mxYVwpYIMMH8JStzkpuzYkDkAIBVsVFcNFOs_v3m3jk2xkkgr_a6LtMDE-WMQWsOaljOKIX9q07NCDY9ISvTLGfIR2n8kadQSxY_lq6PKOFn3QVamM56tlCszZJtcuEU3_xU57L2fTYoE83VBkKY_XeoyfCzR4WYcrljdeReExgzcC7K71tD-kwNAmB-WjQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KIMUmB1VUCi0TCeFG3UkijWn6YAQYy_31sC9h54jnJU8rwRoV2zQfinq_ljTD4GNu9wn886evp8BXY9bYTkXX7jGdWos74I78FK3dh2G6-ky7ndMLWrjCOnlQ8JmOxcobV2JExf2PkQz0YRxsbpR7kMJNt4VmjWcR9XrdYJ83A4f6MnFctHLkT7w8jVgrmlSfspLNIp0RTSVZtOpnzEInkkgG40b0mgw_6rxlmmNbxHQDNRS5KsA37sbuPLbn-07vJM72MdMVLAB3Qlc3wivLZfGWQppFWoi05_4mkfGqAleHAjJUo9a531JKqTa8LxjXt8mHp-4Ihb5jgS--fslwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KIMUmB1VUCi0TCeFG3UkijWn6YAQYy_31sC9h54jnJU8rwRoV2zQfinq_ljTD4GNu9wn886evp8BXY9bYTkXX7jGdWos74I78FK3dh2G6-ky7ndMLWrjCOnlQ8JmOxcobV2JExf2PkQz0YRxsbpR7kMJNt4VmjWcR9XrdYJ83A4f6MnFctHLkT7w8jVgrmlSfspLNIp0RTSVZtOpnzEInkkgG40b0mgw_6rxlmmNbxHQDNRS5KsA37sbuPLbn-07vJM72MdMVLAB3Qlc3wivLZfGWQppFWoi05_4mkfGqAleHAjJUo9a531JKqTa8LxjXt8mHp-4Ihb5jgS--fslwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=mdfQz1fW1OAcXpjG_eKBEyFU8uOhPX8bc5f7NXAGcugJR22rT_kJA3djHf6fUYyfLZBovknggf3HGxoT1rnaGRIDp0MQEir8MhK0aToaok0th5xG5iKjpxXTsCqWtv4NC2aqPVDq_u0tCmyXJCl1NCWTzlNJkWx4mVPyJupypfD4A_jgXzdhBZZOcjq1FDACArOlqx8JaN0MzZs6B5qnhVvgm2ODKH8RzULJhj1vBtzSdKdaDDW1TwIBovcMWQwGBJECVnaq0Gr7CfVP_jJAXpyORCdTn-zYk2RB8j4CAVbL2m8eeojFtgbU7iTtOsOb9FGURaB-gcZsAHcRvtx9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=mdfQz1fW1OAcXpjG_eKBEyFU8uOhPX8bc5f7NXAGcugJR22rT_kJA3djHf6fUYyfLZBovknggf3HGxoT1rnaGRIDp0MQEir8MhK0aToaok0th5xG5iKjpxXTsCqWtv4NC2aqPVDq_u0tCmyXJCl1NCWTzlNJkWx4mVPyJupypfD4A_jgXzdhBZZOcjq1FDACArOlqx8JaN0MzZs6B5qnhVvgm2ODKH8RzULJhj1vBtzSdKdaDDW1TwIBovcMWQwGBJECVnaq0Gr7CfVP_jJAXpyORCdTn-zYk2RB8j4CAVbL2m8eeojFtgbU7iTtOsOb9FGURaB-gcZsAHcRvtx9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=QJGLOtRqEQeXAGr0zyoWO1H1CJUONR_E-nl6cJbDVvthsYAZ5ZR8GUULzMWNTbxJfI_MkSFmBDXnWiLOrijZKNMqaCOInB9rYVUwqJ2ae7qEs02vRry1zIPRgB2FgqazdeGNv3ZpV33k3rzJOLZTsPDbfAFi9Rq2wsZhapNttyb0SraRvQOugHzuvqnNfocOZj1TJJL1WGVwrwBfVcLQCmTvB8GLPh8_PjgKJYARwoxBTGQj6LCP2qHk93SVQmpgDtGxioyHB-KUBmaTT1ebgvUKAqQC5kAIr1ZwkUM5aGyUZ0XETInG7AxeCVXWHB7FdD_gGotl4J7armZPdQ-Mhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=QJGLOtRqEQeXAGr0zyoWO1H1CJUONR_E-nl6cJbDVvthsYAZ5ZR8GUULzMWNTbxJfI_MkSFmBDXnWiLOrijZKNMqaCOInB9rYVUwqJ2ae7qEs02vRry1zIPRgB2FgqazdeGNv3ZpV33k3rzJOLZTsPDbfAFi9Rq2wsZhapNttyb0SraRvQOugHzuvqnNfocOZj1TJJL1WGVwrwBfVcLQCmTvB8GLPh8_PjgKJYARwoxBTGQj6LCP2qHk93SVQmpgDtGxioyHB-KUBmaTT1ebgvUKAqQC5kAIr1ZwkUM5aGyUZ0XETInG7AxeCVXWHB7FdD_gGotl4J7armZPdQ-Mhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=m42MWXHAEWCHTqS2cF2gNOGt3uHT3URjGsGSXttOE2Chx_n5nCGnDJlMabVD2d-0SAJdZFeRIsQai8fxSKxE1N9mXHoNkD-0pOuOM0alm6IwsnJoWXb9TW5ZfcuJkzG4o8ieCQg4Wcq2QcyIpsAbrU9lXbEdTZcwT8HEbbxYrBluptcBUn5FMh0QNBnuQZwO2wVTihegIIHCz220rQG3br3GPcOHZE8KsrGzqaIyzrMsqyezGeW__0vK9NnNQUFel-12_6QkwtSuUYTUSvmj7PiMMGlnZg4Or9AQAiLZMk8YhLKqINarNWdvvnCJCnWGDCNI-5VPOpPUDyGbU6rquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=f7fLfgYFlJalowTZgWZcTJZN-sSTZ5sESgQHdCeGg4tNiENL-XkIRvA6B6uEd7efehGU6ICJCJ4oO_HPvjf_Rr_OP7vMuNkzTYhg8ch68cnT7Bs7o1unjDDvJVHK3gmZXWB92q0PujfdBUubJNak2pLpqwRwpRnp7WUYjtB3zvOAD6g78Bfuc8Vd4-P5WMG-7rV7dlCxSei4QLs5dKTbPtnFUudWm7Z-NV6bNKHWbXdM48cnJR9_OoXbu-8qXSmDxWQaV0qUeeL8rNPPjRAI10yBLyz9i88VMfejb_4lqx52kmf_aYLh21FaR9Lh8EhSJX7u3esrh0B2S3XzlHTgww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Q8xfu240ZYM2JnmVRsVlb9oTvu9BkYcxJvoDVUc3w0mz7YUrqZETZtK3PHvz4dxzrz_Iq93-V1thC8_ksQJEjO3IztcL4qAlw9187f-7RIhia5bqzB7Gd31ZNagNodW_lxUbZHCEDEo_ThYJ857AAzgS7pihuqbU_6ZgiFMptwvPRwL2ylTMxUHvaUxo6ZyvIgVYEb098AqdblCfT6xNbF8IofeIMjL9JoHlCBC_-ETVy7qexl4QehsuEpLAyb3oT3SA7uR7gXAr7SCqH6w4cFvUC6P3URLFPpViNFnF7OrfcmndxyPI06li_EcVhypR9b3QFBIAKF9hs9DT5zdmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Q8xfu240ZYM2JnmVRsVlb9oTvu9BkYcxJvoDVUc3w0mz7YUrqZETZtK3PHvz4dxzrz_Iq93-V1thC8_ksQJEjO3IztcL4qAlw9187f-7RIhia5bqzB7Gd31ZNagNodW_lxUbZHCEDEo_ThYJ857AAzgS7pihuqbU_6ZgiFMptwvPRwL2ylTMxUHvaUxo6ZyvIgVYEb098AqdblCfT6xNbF8IofeIMjL9JoHlCBC_-ETVy7qexl4QehsuEpLAyb3oT3SA7uR7gXAr7SCqH6w4cFvUC6P3URLFPpViNFnF7OrfcmndxyPI06li_EcVhypR9b3QFBIAKF9hs9DT5zdmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R0Jtn8D8_5ueJPvtptqQP4CN1Z-DTJDvCzKitQ3PzSgb2lcm9Ug9WFjG2YlGx3kenvg1BHCy9rFBqPrt8aS-iEwp5HL2kvyqgWvBo0534haR6g1GIiJFhJJ1yL9hzJiebyzOZe-D_KyTK-0vWkOHVkJGKF3grnGvegVCu1VrNHFZfFr__iQteMTVN8_ptVB-lQOIR6s84Kl6i6rKTQJbjgAA_uNV8c6Q9D_eKt4CMCa5SofMl7gWokou_sx9GfKW2J2PaXjB5ZI04g7D_zK30WyGRJBBgkHhhO2GBUsWHgBDD2KeAswV_xAeHg7YoHGI3ZpkcIsSmTYwRuVMVMv_dH4EVJ2rf8MVmLW6DUSmAhTQXAJTsrNi8yCyfPDm3RGnwdPZOpCo0YSHXvLuQKoVICUL3NRabfKXRlefRw2n47scq_YddRPyqudz3xfTk2JZtOuRtvzTLalPO9NGfvTEAOw9IoBPnpwU7GoVvNEZNgFHqRa46c6auOktk9SYMaRXpAkOYTsCXKBZ7c7e_9ays6rb6Jn35HMQnjtiBs5wqrpHjq87r_MWm0oO8eN53fcPAh0Z5jaYw2Sd_w3DL4Xt15352xP3muegHNqOM4VtXWMe_Dg_KsxZzZlN1OzYrL7cHeA14ncjj_hncw0KmN-fugR35pb0QWhb9wKoHuRpjNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R0Jtn8D8_5ueJPvtptqQP4CN1Z-DTJDvCzKitQ3PzSgb2lcm9Ug9WFjG2YlGx3kenvg1BHCy9rFBqPrt8aS-iEwp5HL2kvyqgWvBo0534haR6g1GIiJFhJJ1yL9hzJiebyzOZe-D_KyTK-0vWkOHVkJGKF3grnGvegVCu1VrNHFZfFr__iQteMTVN8_ptVB-lQOIR6s84Kl6i6rKTQJbjgAA_uNV8c6Q9D_eKt4CMCa5SofMl7gWokou_sx9GfKW2J2PaXjB5ZI04g7D_zK30WyGRJBBgkHhhO2GBUsWHgBDD2KeAswV_xAeHg7YoHGI3ZpkcIsSmTYwRuVMVMv_dH4EVJ2rf8MVmLW6DUSmAhTQXAJTsrNi8yCyfPDm3RGnwdPZOpCo0YSHXvLuQKoVICUL3NRabfKXRlefRw2n47scq_YddRPyqudz3xfTk2JZtOuRtvzTLalPO9NGfvTEAOw9IoBPnpwU7GoVvNEZNgFHqRa46c6auOktk9SYMaRXpAkOYTsCXKBZ7c7e_9ays6rb6Jn35HMQnjtiBs5wqrpHjq87r_MWm0oO8eN53fcPAh0Z5jaYw2Sd_w3DL4Xt15352xP3muegHNqOM4VtXWMe_Dg_KsxZzZlN1OzYrL7cHeA14ncjj_hncw0KmN-fugR35pb0QWhb9wKoHuRpjNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bClxBJXAG5-SFMLw9Uf5xK9D9B9VuE-_1KdezEjCi3kwfTPeqqyF1bO0ucmtpRXNcWecDqAAXm7uNcvaeaUT3BhGfbbpwrMVQcoXTGPVGEeFzgmx-nC1EjRhvr0_SfpqTfjiF8HwKh72L7D8DtdY73lguSzMGFX4eSnElk00tqhhDC2ghmzCQFJe6AE2oLPdWJZ7SZvLX9xOisahAb3BePje_MBJKfV_H1SQBUtsBLzqO3d1ZYvhoB_p7vYcPn-TIaNWeavp2TGlp9vN6SWARDbvQ_mAtdS3teXal6Hf8AT64_67Xk059EOMgnuTf6Kj9qCpc7QVsxebL2nyzIdhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bClxBJXAG5-SFMLw9Uf5xK9D9B9VuE-_1KdezEjCi3kwfTPeqqyF1bO0ucmtpRXNcWecDqAAXm7uNcvaeaUT3BhGfbbpwrMVQcoXTGPVGEeFzgmx-nC1EjRhvr0_SfpqTfjiF8HwKh72L7D8DtdY73lguSzMGFX4eSnElk00tqhhDC2ghmzCQFJe6AE2oLPdWJZ7SZvLX9xOisahAb3BePje_MBJKfV_H1SQBUtsBLzqO3d1ZYvhoB_p7vYcPn-TIaNWeavp2TGlp9vN6SWARDbvQ_mAtdS3teXal6Hf8AT64_67Xk059EOMgnuTf6Kj9qCpc7QVsxebL2nyzIdhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=dIL_gSXTa3o4zYUarfruRWayttFG0wwt0SFVH-_WANuRQ3rmEeAq2mofFLurizMCqekHBlpEFWgdtJHq47rGXoOcRgM794Cp2fvmnaXqIzuu3qHYMvHi1jRKbMzUf0uYVgETMegrZXm9DaSg5aZof5YN2_NkxIeKhqr8puDg-SoKWxntZEVyMBBQcBGnRdTMvCsEg8z2IPUXf-DoCx92vQpymKgGcZEA6nIYrLo8bVFMtOa1Hfmk8dBbyY14_kpM3yMcbSmJ1w9qhkhBoxo7qvMDeemklO85qTVKEdYOBJoIVPfdO1vDav8V5hfKUYblp-AtboirHLma0CmxtGWzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=dIL_gSXTa3o4zYUarfruRWayttFG0wwt0SFVH-_WANuRQ3rmEeAq2mofFLurizMCqekHBlpEFWgdtJHq47rGXoOcRgM794Cp2fvmnaXqIzuu3qHYMvHi1jRKbMzUf0uYVgETMegrZXm9DaSg5aZof5YN2_NkxIeKhqr8puDg-SoKWxntZEVyMBBQcBGnRdTMvCsEg8z2IPUXf-DoCx92vQpymKgGcZEA6nIYrLo8bVFMtOa1Hfmk8dBbyY14_kpM3yMcbSmJ1w9qhkhBoxo7qvMDeemklO85qTVKEdYOBJoIVPfdO1vDav8V5hfKUYblp-AtboirHLma0CmxtGWzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClXvFoskpuOTkJDCUBwMx7pXbbdlRg3ZMtuNIIcj6QEUTfs1NT2i-wkGnGQGnuH-NlRGiWuRphugCZSUUNjzyxy9GOdP0_QcJUucg1pzMUpJ5ZOXpVsNEQ5aRnp2q-CLWEf_qohMhGX1EWcKeytkyZruiuYml-H4ZM-9bZeitsfVBmCZ4JSYV2ripOL4tbApMzpGxTD6M5uVZTRYX221-mkcX6lQW9T5b-e9T20u-JLXVmEtAEtYNShWBj3OG7a1H3TnsZcWJa3GMtf06hddR6wM0TxJy0JsnTCv7lIEqZqM432Bn_r4RYZfnlK350jlEznNo9W_k7Djy3fa1Of-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8rQXp81tHYrdQOiW7ApndKvpQLmwJd0FBkHjqxLS9M7eHDn25BZaUF3qt1OIdj3knxo1tn7B56LcnqpyO6eSBFYtlwRVy1OnDcw2CJ7FYQQIrzZtvHZp1jvYs_q0SszUlhdgu_H2pSh3g_He-Kc7cRctupx8BRGJW1dvAXGIe_H_0sUyo9NjTHCv42cwCDUM39ACu14GiZrfcIAKh31aQZufrhHbuLHMRdv-02niq0SEeH8idQEHNC9gjRmdCptvwhK9lBL_CuMUs41aRhK3_f2UP6Gr1ZdfN9G7430DKJ354nCuP5rAJnpszlRp7Nwrw_8iGk8lN_JKUAd-si7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=RrctmVzwwUOGI7SwHiEcVT6DBV_1XmMYpnfMJuH4cQ14aWtImJMXmXoyamuilqtR_JpkrKAR49f0b626reNjon1ugqNV1JPaJd-IV6fk_pU4Sdzbt00EW5gtLNBonOllII9KOufDzPu6nTPEVjv7v4Ey4Nd6qaowaAVVyZ9RloMRtVYIOY7v8bb2qOr7jEcWifafZYuGg2YNyaJQqJ6-Y7A4k-HKkeI_BnBrQWMQ-8N2BqSC1SWYiMqGoRw3phr73_4bGwlknrsgO0JRLG6PYVA1X9JFYLLXb74ob3p1Dj8j_T4e_bytnva36NsCTEjBsUS_9sBTAjf4333mLaqqMq_Pab1ttEg0vxfHGnMJMUSV9VJPCAh9fc2g-o7HxAv8E8eFyEgptTlQC9g0kLAvHhyDQZWb1Z5FCNWCelad0Z8cD3Nt0OT8xCzWWQF68iG134-5bDXH-duA-AcyYJJJhebSTdaKGH-7Cs_h2m2WEAXXhvB-vDjvVWF8G36qmMV-zfhBCiIPdDVy-ThJ4AntNLlsYX8XvJonWJy-8f03GxMOpe_twFgZJF9i8YlEkB-_xChLP13qCah-XsuYJtpmVeY52I6R-HJ6Pawy8zYz9ovO4dKRhz57IEL-CwQD4cjSkmfv075UK0u75h_v438pf7LPfwziRqG3v7O8E889F-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=RrctmVzwwUOGI7SwHiEcVT6DBV_1XmMYpnfMJuH4cQ14aWtImJMXmXoyamuilqtR_JpkrKAR49f0b626reNjon1ugqNV1JPaJd-IV6fk_pU4Sdzbt00EW5gtLNBonOllII9KOufDzPu6nTPEVjv7v4Ey4Nd6qaowaAVVyZ9RloMRtVYIOY7v8bb2qOr7jEcWifafZYuGg2YNyaJQqJ6-Y7A4k-HKkeI_BnBrQWMQ-8N2BqSC1SWYiMqGoRw3phr73_4bGwlknrsgO0JRLG6PYVA1X9JFYLLXb74ob3p1Dj8j_T4e_bytnva36NsCTEjBsUS_9sBTAjf4333mLaqqMq_Pab1ttEg0vxfHGnMJMUSV9VJPCAh9fc2g-o7HxAv8E8eFyEgptTlQC9g0kLAvHhyDQZWb1Z5FCNWCelad0Z8cD3Nt0OT8xCzWWQF68iG134-5bDXH-duA-AcyYJJJhebSTdaKGH-7Cs_h2m2WEAXXhvB-vDjvVWF8G36qmMV-zfhBCiIPdDVy-ThJ4AntNLlsYX8XvJonWJy-8f03GxMOpe_twFgZJF9i8YlEkB-_xChLP13qCah-XsuYJtpmVeY52I6R-HJ6Pawy8zYz9ovO4dKRhz57IEL-CwQD4cjSkmfv075UK0u75h_v438pf7LPfwziRqG3v7O8E889F-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoiPCLKkDOSTPZo4vh-ED3ydxHjhDuAifaMyOLdCmkSBHAE3jDMCpFYpCZ9ondPNoCoyoZ1GwiZveRmbt6vxG1MMBPD19vlW1_Bayawoqp99MpXROOejlFQPUJ8Il6e0GfhzixLOaQjaRmuuEPOSn26p0YWsoXNPhRCUbT5vYa49ItC11_TyNIyVTKU2v5gm0U9TNysEKVs3T1_fWMwLMrWR3hUYDLXZYLoglMtverVvSmdZsTAuapQJrgcl00rdWuLcGI8-Dol4v3R8oMFIMXuyTIzWR-qwufYEoxPT2Rw8qQSQr0oohtGzzlPPMkgxzrTfnLMy1M_c5UxU2WG7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ryqhz39raPROjeAXZ0VWSXYlGBYmle_lWwQc1ZzJuwyteRJgT2FjMFCBN60t6oRbnW20TV45VgI2vVhWzVbOh8hc2bkMNJIbr2ttQijJGGkKI3iN_vXOc3k5ND5yw1zGsVOnYjqphB1SfXIZzimnqum2vRaBcCabQrfqx1OhdPd09XOK22Fus3ZNr6NQ0oYMlL5wp79coTH_6z6c44nSNuXBbXBs89jNRNYLdswUv0dtbPTdV3BFGtGyPHT-DsvT6MixilufxrRACSu7ukRlRwwGgurljvVu9_Ie393VRZ-Nyj-YOxAmQwN5R-xZNIzaQt19MJFI0ugqwUpq4KuvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLMrdm4xNwg0x0qdWwexUCuEukUq9MaPdykhUMJOEQ46ucz_1vnVuZolo0QmbPLoTXrH_cTB06uQ0RoggezrBfKluWriXhCnvUzajPDxNkET6YDIMZyMA9zAJCe2Uwgh79yBjBsbdBz5Ap__X8kV6tS4Z-dUnlADCorBNIWpXU1Q0T74z9k7BLr2hufdzBPqR-81bdBM1378qf9cJ3PxruYgs4ycioe0y6syl9faR9W3gkbkIVAuK2W41FVfciO_gGrSCsIzXCWiWjYxKNNdF3TXCWat1s2TCJAkuWiXPPeE5cIz6B9zs30igz483SfsWJLaDaXngWfJY3cuuqIa5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpSBsjwDx7JbTFepzU4abjrWB4dZ_d5ei0gkJH4gl8pk4NReEsf4EhUfp6etGvStolQzjABB33V2uYois4IpzDBccRy2OnE7-B10j6C-SaFhk6FcvUhxH42kmAenUty_J2GokeN-S5NPy0w-65eFflF2XunQOZ3uJ3AN0-mAHGrVHw_NIBx8gYwYkw0-xWySp6QTXhv2ET0ZU7EqAZxt-D6r66uReL77g-YOKKVkuKHGqsNOdpViAcDcQuGdhGtg0zKLjiJz0bXrxIqiKO_siYd_DwBe2IEHv8HofoEttcJu9fwMEPch4yODX67Ltp_FJq9xfBWfs39bdivcZ6E0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=bvciCqdpEyiF-hm9VThQ2aEurL-143EVJmeFC6D7cd_gbK6hWvxc9-YayPA7y62djadGQX9Y8bb2pyhOJmKixqOOVrml6ACu2vIGkZd-4JQsUH8J-ftscxiObdw1HImL9yrwMSdpxN498yaeoEu8PEJAkEr5xdgvADi_pJLWL83wsgZSTKrElsN_G30gYPvBw4JNWD9tiAzlsWIfigkYNVx3XhueWWJCGYDw-89T2mg5oRys5q_-b9Ui_T4Y5rD_tHX2PbhyVh2PGKha3Xp5-_Wt5T9M2Ec-njbkZXbH9R-AQ2H7A5QgwklzpBz8OxNDVThvrMi-l-D5QjfFyH4rKFebBHVRC-XWjws99uSAum79WCqhUWI7iy3dxNOy5FFUtEtqbwlqDSkqDZM4OMrlR4_gcwxhoFUA5zAXsc7y2KDL_4gaQxU5NezXZoWEz6RcMC9Y6Ls_CejGpJWw88TlD_yFcZuV8GPTxUfIDQKXYvepGEny8Q60HMygYrxKEBMLQTiNOtI_aTpNVOXrDgNJMjzHybOA8A3lsLLg1hzH6wPlCgn2Vd0nKfd3i-7_Vt8BMAptn9DbbiYzNsBXLumBhRtt3RagukquXzJA8zcqXDL1nbW11wqq4vYc9xeugq32qx0YyfVJaRKKH4KcEQi4FhdGpVEnGuX8wkRgTdfMMbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=bvciCqdpEyiF-hm9VThQ2aEurL-143EVJmeFC6D7cd_gbK6hWvxc9-YayPA7y62djadGQX9Y8bb2pyhOJmKixqOOVrml6ACu2vIGkZd-4JQsUH8J-ftscxiObdw1HImL9yrwMSdpxN498yaeoEu8PEJAkEr5xdgvADi_pJLWL83wsgZSTKrElsN_G30gYPvBw4JNWD9tiAzlsWIfigkYNVx3XhueWWJCGYDw-89T2mg5oRys5q_-b9Ui_T4Y5rD_tHX2PbhyVh2PGKha3Xp5-_Wt5T9M2Ec-njbkZXbH9R-AQ2H7A5QgwklzpBz8OxNDVThvrMi-l-D5QjfFyH4rKFebBHVRC-XWjws99uSAum79WCqhUWI7iy3dxNOy5FFUtEtqbwlqDSkqDZM4OMrlR4_gcwxhoFUA5zAXsc7y2KDL_4gaQxU5NezXZoWEz6RcMC9Y6Ls_CejGpJWw88TlD_yFcZuV8GPTxUfIDQKXYvepGEny8Q60HMygYrxKEBMLQTiNOtI_aTpNVOXrDgNJMjzHybOA8A3lsLLg1hzH6wPlCgn2Vd0nKfd3i-7_Vt8BMAptn9DbbiYzNsBXLumBhRtt3RagukquXzJA8zcqXDL1nbW11wqq4vYc9xeugq32qx0YyfVJaRKKH4KcEQi4FhdGpVEnGuX8wkRgTdfMMbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=rH7SxckkDY5MdPlLFytAnCZNqkbsRvk9CqjE7jFE7cs1XPo0oqget7y6XfehBkIVI19PGfUXUJ5yP-c2jffHF-BcK6V5edLqd2rIaeayAp1a07GFkMcXyoXOor7KhseqPv7tNvRDD0fhtwESFtNsyE9mmwaVSOutK_gaBcOWdnK31br9RU3LYkxX4IFY4MJNvAVJCBCJY6UiJHRfR1A88YipmGTfeLNXp8RWVUTuxpWBcUCUR67FKoLoIn9REQV3gYEONy2ccpAHKu7KfQW4QC46dzfcY9pxqj2QQTrbDgAMzFmgWPGTkg0KdURFOem1kurlDbIBh8SKFmt_F2X53w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=rH7SxckkDY5MdPlLFytAnCZNqkbsRvk9CqjE7jFE7cs1XPo0oqget7y6XfehBkIVI19PGfUXUJ5yP-c2jffHF-BcK6V5edLqd2rIaeayAp1a07GFkMcXyoXOor7KhseqPv7tNvRDD0fhtwESFtNsyE9mmwaVSOutK_gaBcOWdnK31br9RU3LYkxX4IFY4MJNvAVJCBCJY6UiJHRfR1A88YipmGTfeLNXp8RWVUTuxpWBcUCUR67FKoLoIn9REQV3gYEONy2ccpAHKu7KfQW4QC46dzfcY9pxqj2QQTrbDgAMzFmgWPGTkg0KdURFOem1kurlDbIBh8SKFmt_F2X53w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIE5c-g9eNlRHAZ-VyR1_YjnDkXA35Vqx-rAQ-ALT9PMG8lQD1poSCAlXiNEwNJS3SiQqQZ2J8S5bp7ItirAH_66JGhSYCcDIy0TqJriBB1zRUlH-0OEF50Ccwkw8dTtHXtLLYWeZ-HSig_aQtWb9R42Vga7H7mvM7ayK3kq57isNQxBgMkkACBiSzJtPa8jSryDeNmA63DiOez8WaC9OB-nSRFzythW5mnSvk5dqw-4C8RfOUd4aCMbZ5-kcNTY050TP-tHcWBVip49zgV2dPHKbvOBCENmpYj78hSbFRQtGM1R9ixLx8bo_O9V5j5STukirvT0__f1OfII9epdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kejdhzxUN7Nzbr__uaCjuRDOQi-QRR6Roo0its2tMCQllh1M6oCd-MD5HTWW1E0ofx8X8NHO7zgzHcR8Cq5tIcPPg72Sm5w_MWoV0H5wGIe4VJ9ldleLzA89yhrlu7EKUsU9TCRgJNtu25M866gvc4au3Q3weN0b9r60xwzKelyFarqIpMBDMjwzq_PMJVE3yWP2178Fz_nCE4P3ZhQDZpZ6WyXkDMod56AEMpM31KvORjbRNF8_O2KKN4uZUOVuSQPVbchTkZi3T6OV5LZmXd9gsoQtu6OpAKE4Jv39xaCHh-A-GQ9qTBTAFp6XxBki__U28TFkxR74N5bQm9K0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kL48w56X4HGIUAsJD0FwiS8HX9nDmYZtx1HyHz5qkIM-uKJ58f3rjYVrlv_UAW0wSMb7vKFNyTFBMwPe3-D8Ly9A_OvlffrgWA1m-EHctzCL4HvSDMPqm9FFkW2iRKCC5MXlFfI8St-dGfdLLTOg7OOYuQdYn-B28cfpON_Dhxpko1qRceh7s_AbfU73Na7PYlk8ZTQNzONZ3Roipa9Tr5WrZwZwJPRKzxAv67DCr30TrgheJmFefDHHEHMfoq_aI9W3PWLc13khVEdWP6x9ti4VfCPVAPItLEBEFiTW-FdOFlDjKEF04d7EY7p_qqOZ4IqqD4QkYcttSAOi2Soq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nITvSreWGFkcrBRORYaBZ05NRQ9Q_nkIM_tXvZhqoEPr4Jbn9kN4AHYwm3rWVzUU3lHjVeDlVJiTnq4nTVeAavL3TZmwZyn7ZBsfzPEIm0vN1ttU_zfF20ffbTXemXWg5jUrLVzbJ4lh60fCISfqqDebzb65QyAJQ3pwHpW0LOK5y4HywVP1MDTwsah4JSlHcFywCpJN5fq4C15ofHs4QkyVqaLkGmWV72l8asyDQM5lT9M6YQV7zQqarOnODw_rTNsTWhbdb3uCBBawxvntJ78eELO5-EeC2q8GIfpyYbznfj5x4bhfvj2lXe4yrO0vCrCgcA-zgEZjGOXfQaukhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie5eslxr_xz2GPF7DqXARKICHscUGUukHaD2SQwVhQs0-z27XnVpCW1g24FFmZl2cUS9iJSDNv4AoCu71AE1QnUKBw90822Wu3MXgzVsPacn5Zilyh0bnTtOhlGBYNXwEzRSn035p3nfcafY7BarnraG7B5pFItWE1AG6ECdtSHqHmrsERvIM7I9t3SPo_6IAei05G2X3aVIGlXvSqcru2jpGktdzducCbs7VAenMeoQDfODuhYRaHnp2p55sLy2mswWKGZAaIHlT-3bbXnddyvneDQAgKD3pGF67HsjSB8U1QEv2GAJQPImtZofW1RNecHAi6IkU7CoeseySOlYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skMYadTGFfbdcepiSiCbtJqTdZ39mq64JOemdMIcyLxwbXe815Obi390iX-FgXZEJXcROjjP19GPnucN0Yuc9Ab3gcTlC99xRC3MGNJp6fIJ8XbIv0fxLBQtrMsj0uWO8YK9HQrEsFFzbjIMDzsl59MCdO0BbsDIE7OJONpwwOWSemw_-msZxDD2MZxX8kuQvM0IpYdkvO7koEkiI-j0ooCtalmBFbf-ZR7MvxkvD1tgqKzvjVrhprR4N7nWWJFSvoRThgfhOg0hdPjPUaSU7wOCdJ4QZtHldS9ogFLNcz7MlSY5uBDt2FpCrP3-IgCrZUSAddNv4PtEoJV1aysyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNMRNoamwMqPwMOWs8PfH89NevOLMKpxTR6C6P57FSEgC-N_UX62hcFPpbiK94LPojBKO7iDAQzPy99iNxtf_faZEbRs4jHpIf5fovUYesoEo8jrMQ8zSACCx_r99xD8qRymEtvbREANmQy2Qiu7P56b4F_5aGLs04DObltzjqu-Uzf9lJgR8hxLO43A4UdP4q0gYjjAQT1K9PdxDayyBTPjBHzfoSycBwef0uRPZO_PCrXoDGiGkfMSBsIA53caTQBurZMeeY2lVRSBgJG-w4oTwzg5cTky-ixWM5hUDNhqzJPYwgQE5HljVNipKX5x9b-KQaj6FeHv9XQcefFGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=cSpKnvBxSuGTOeO6g3H72kFrvVx3anGYeXGzPup8X9d9TnrBsDcggN2Gq5HDtbjekOt6sZbVNVLiCMPIl__gtalrE-50d-_mMp9w0bSaQcuHv8F21l0ErAySDZVF3chorTzUPV13T8F-zmy9JPIn-x-qKerQSNTtXDyCdM0llRIMmWqjd326lE425ZqI4TLJWmuSShj1trZW2XSDTNxo6p_jhcdB0bUJ1ikFr_Dqf0aoFlm-uM6ujgGe-6JBrxCQazkqOySovCr7vapEkM7poKbZSHJp9T8QkmgEjqA69ExPOybyoV-XmEEB0MlLdi4ss3yExHgKmZuIUgrTdiI6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=cSpKnvBxSuGTOeO6g3H72kFrvVx3anGYeXGzPup8X9d9TnrBsDcggN2Gq5HDtbjekOt6sZbVNVLiCMPIl__gtalrE-50d-_mMp9w0bSaQcuHv8F21l0ErAySDZVF3chorTzUPV13T8F-zmy9JPIn-x-qKerQSNTtXDyCdM0llRIMmWqjd326lE425ZqI4TLJWmuSShj1trZW2XSDTNxo6p_jhcdB0bUJ1ikFr_Dqf0aoFlm-uM6ujgGe-6JBrxCQazkqOySovCr7vapEkM7poKbZSHJp9T8QkmgEjqA69ExPOybyoV-XmEEB0MlLdi4ss3yExHgKmZuIUgrTdiI6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT7eBcNG5sAj-m8t88Vyv8VXRZekhjTGMyXj6iB86Zw3f4T4gv0PT3SNWCA7WWvo3kd_td4QwI2uygUE0cIlF7oP_ccsNI_CYuj-MwRAXfc825Dwb_1uta4SuETCx0vEgZGL07CJvgZ8O80wDpKZUTg1y9g1bGF89hwMyY0M0epx_TZBlIN6ZKrI1fAPLIV9dPuRB2KSIetNLXIJ47kamKpCnqAnwTbCE0k9Ckx-FPOTxtfGhSxNz7AyCniR0K0FFDhw9ZBhu4Dj1NUsjyPPVB5KlltyoNmYs3cosU1Lk1YDlvhXzqmTi1Y3y0TbpdACRVJCF70oIqujaon4sv11Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=WrXsjobPbIh-Q59FiDTV2XH67b94YaI0d-HrdIzKy84r3YVzXjMkbvdcPkVDw48CeQjPk2FbdNNfd3QLNNosNMwKbgNQBe5RvEvjDS-guMY7RshDHmQKb8zZaY2iOCUJwBkxIxC_iw7mdFINmeRKw8bPxml-sWREDF1DvuGC1yHq9WRMiH7HECX2Eh2RuBji6GZF1J46Hykgjcz6my7deiEjSHGN-ALDrrSWKhNgv56zDZFrArQ7xS-dDhnuw4AZKlRsoyr3RWK4vofon7UxLRPIg9PbTZhXmyOHpTvx1ya0GsJt8hPzB6okWbCOZYzjM3f6-uKcSoPkF-ifb0408g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=WrXsjobPbIh-Q59FiDTV2XH67b94YaI0d-HrdIzKy84r3YVzXjMkbvdcPkVDw48CeQjPk2FbdNNfd3QLNNosNMwKbgNQBe5RvEvjDS-guMY7RshDHmQKb8zZaY2iOCUJwBkxIxC_iw7mdFINmeRKw8bPxml-sWREDF1DvuGC1yHq9WRMiH7HECX2Eh2RuBji6GZF1J46Hykgjcz6my7deiEjSHGN-ALDrrSWKhNgv56zDZFrArQ7xS-dDhnuw4AZKlRsoyr3RWK4vofon7UxLRPIg9PbTZhXmyOHpTvx1ya0GsJt8hPzB6okWbCOZYzjM3f6-uKcSoPkF-ifb0408g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_Oc520eIP2w8rNoIEMPIBzcWRiSzEwiHUXMr2UyaeVb3JhTJJn8Tg1OYN5lmKWEAeGlxlnactTeX-OTdPd_yZsZ3jzKr4A_6JWqw-PE_3tpOl039rTdsIpGBWDcilYl1UgtxgaOO9e8tW7Ls3s_ogJNR5O0okm1RdQEAFNzBr8aGGEPXsjrWLc2ZctoomBRDdVZBiZPWH9ZWOl6mN4vnKw9V4nBMiPzqWQO4OitFN3c7Lqp6A_o-4WILmaxD7PUICnXdmCnd5aygsTyHlCe-XWAG6EdwE3XE1GEgkUx_All8gc8WKW1c-tOD6bYv-qGsYelConx5x9nVSTlyINjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGISiCIUIMj7fssACu-llY_9oU8P2WXiI7h6SpDf2Oa1V84j65BnKU1PAO4uX7hQuKVjQ8kEWjz3xKrHf57_UWkVYA9QTXkdYsRb7aFLdeOOdf4GM2PQw4NExaSu-Kjea68n0pN95OpgCLhNwDHe7KUr40EpptRnnOtYH4PDxvKEH1Yi2fKNIUVkOV5SDhXGyYalwzFtR-HiMcIUBEt1MSLYwWi_qd6HePDs-jxPEmtNlR4Iv2mL3gFmFrXnRM1Rlir4SNNoLDEBuZIN5yELGBD-Tt99f5mvIPIDdaVIDEpOysHgZd_MK8Y1QFbwUgWwKIbddeSOkupRJSkqJTkHUxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGISiCIUIMj7fssACu-llY_9oU8P2WXiI7h6SpDf2Oa1V84j65BnKU1PAO4uX7hQuKVjQ8kEWjz3xKrHf57_UWkVYA9QTXkdYsRb7aFLdeOOdf4GM2PQw4NExaSu-Kjea68n0pN95OpgCLhNwDHe7KUr40EpptRnnOtYH4PDxvKEH1Yi2fKNIUVkOV5SDhXGyYalwzFtR-HiMcIUBEt1MSLYwWi_qd6HePDs-jxPEmtNlR4Iv2mL3gFmFrXnRM1Rlir4SNNoLDEBuZIN5yELGBD-Tt99f5mvIPIDdaVIDEpOysHgZd_MK8Y1QFbwUgWwKIbddeSOkupRJSkqJTkHUxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=lZPPy-Wj4yk21nMZwxRUIMp2wO6QShj2BRjVzu65XZ6dd5nEiUs8zTEN5suIQ_qEo1R8GQTZ2S2MjNKLQJlZEvXHPqs6jsLvwfRZdo1JkGnWemnSHdtyg9W6gnHeo841KuWlEPDSQPscorYlE7o5Y-ojaar0mLH1x2R4NH8jmExdyWasRdoTJQZWD7hAV-jy30iSPLEIG2Jab5wnXol2z_luublxOAMQTGzaDXjRs24d41prr90ldVrdHnO7v3eXJyd-iBVMcafh4y7ltLO2ru3S5NU2bhClVt7fWieaKz4AWqhMLn_Ff2EJ9DEycMqrkYYo_dDB0LCP_Y_ouXLXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=lZPPy-Wj4yk21nMZwxRUIMp2wO6QShj2BRjVzu65XZ6dd5nEiUs8zTEN5suIQ_qEo1R8GQTZ2S2MjNKLQJlZEvXHPqs6jsLvwfRZdo1JkGnWemnSHdtyg9W6gnHeo841KuWlEPDSQPscorYlE7o5Y-ojaar0mLH1x2R4NH8jmExdyWasRdoTJQZWD7hAV-jy30iSPLEIG2Jab5wnXol2z_luublxOAMQTGzaDXjRs24d41prr90ldVrdHnO7v3eXJyd-iBVMcafh4y7ltLO2ru3S5NU2bhClVt7fWieaKz4AWqhMLn_Ff2EJ9DEycMqrkYYo_dDB0LCP_Y_ouXLXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYn_GZ_u1abjQCDyUPdIcoEjsScfRKAHbVGeo_pae6vr28arPXHtPqtGSjuwgVxqM2roULhJDV7B_UnypNBo9xqntluWQkR0A37S0sHgIbHp1cTb5r6GS2Xg5Pfu8CwcjiiMgPqGzWCBJNMrgD20bvoOh9NhZirCc5lme3Cg7G2PrtLlVIeSUDYWJaN9Dfxp7ZKZ0mhxcPp-v9QI8PsMQ4ancnCdFrrv0I-tUGuUuEyY7BFfsmpJ-QbcggG-kwOLsyz8FLl8SJS0P4tI_LIKPx_SFr905photuH53ECfhFXCOpuBq1ldactLyLwe76_mfQyZXuuLaRYRy9EuxYiakWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYn_GZ_u1abjQCDyUPdIcoEjsScfRKAHbVGeo_pae6vr28arPXHtPqtGSjuwgVxqM2roULhJDV7B_UnypNBo9xqntluWQkR0A37S0sHgIbHp1cTb5r6GS2Xg5Pfu8CwcjiiMgPqGzWCBJNMrgD20bvoOh9NhZirCc5lme3Cg7G2PrtLlVIeSUDYWJaN9Dfxp7ZKZ0mhxcPp-v9QI8PsMQ4ancnCdFrrv0I-tUGuUuEyY7BFfsmpJ-QbcggG-kwOLsyz8FLl8SJS0P4tI_LIKPx_SFr905photuH53ECfhFXCOpuBq1ldactLyLwe76_mfQyZXuuLaRYRy9EuxYiakWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_J2LoFUqOb9WqIJg0_1pSZp4ce2iOoHzcTULeDxuUUCkolSMRKWKSxP8UTYTRAqSXjqOa4zM7p-CYvn4B2bXDFVBbwYOSHN_bNmuJvts9-9ueF-0qGcJkIkOLj7bcJll9mt-LA8IKB7ER19BTxGw8o3izu53cpjNDeLT3D8f5CXopmIVdwuAkw0D2W5IDSYmnqNKjunWKQ_O3tx9LW-T5PupaDW9yLN1rfyQW1S-4cMvHHiii6BvUtrkTuWnRpb_CRmWKtRE7qwLFvE1AVpm4jnpMfk_XpaBfl5UniQ1aO2XCsPQ5f2jKOZE5eqy3p8D_XmpTh-QO1RtXwKJjAFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxFHzfxHyn_ARll8wfpcQ1FliyG6dROgwlVSS3AiEyokikO8B698fu4yId0Guk1rFCSzPps8agtd-s0eUD3zhxcnRKwUaSVWhtbW2iUQmqlhJPaF7ob19cfgv4IM7ratpLkr4B8xUKMnbnUNPS2hAwACx222gchoykFq9q6gyjU_S--o64PBX8JIT3dYsDdVgdWU5uN2COeSn-cEyhe6mMqBUr3Si6jzm1jO0w2ufQ-VEMm6YIg08-21o1NnAWO8c0636-qgQYAiEAKUFXpMGwmCWk3eJ_qslTJbMB4W4YZ-5vyQrBuZlnOSjsIlfYN0HmDZ4AYNJStKEKUJiYmKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sczs9ojWysZLUizA3h1MFdgMNIyh6O9um6Lis0wFa4pU-qLOQBCT1I-XgMDa3qEX4noMJY7sRNPOF2NMuZRInwqGxeSz5bCIlfiTujyAqzxsVwxUcGvoMBlF_K4NaCh6RUszJOOwRtPpYYt7suf5pnYlIDSwY8aRbuI2iM98zOaAXqhY_rN-54-C3XKrT7njJBy0IY3y6kiAohBHvoljyUDzwphyogmUWLVxhbGRdHtkP-BCrn-L50rlDoz4bIRG4RlS8wYSwteE1OjJaDx9NNnxGWDdXroYjrpWNHeHGalfncUKzpJeGDa8Ybhf7SeXh94_aZO7ey6mOMcLRNn--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFfY6WRyubje8cgQwBOZRj4PFmCJqOS5uB71wbcsffphAQ10ck-vh-VJdByG98n09vmlia80uFZT8gLgGSt0YrDRbVUvQOsG50H5uJo61rjWZfhctf9MYbaGWvHf8OjHP6OE4m6dtrJA8VDl0lzeOsc3X7VDGfhW_zhazDaVZtmfqj1aRVQ4OG9oJ9neQz-IdIvse29Qq1TYP7pZvYqPM1n6dLIzGjRB8Eaxpudt0voLsxJKoyNTFdqz0aUeyr9bxBxkbjOlNkiuaMk5sL-EHl_GkVaJYVIVMtBC9MewFCWJChIbmimeOH6DVB6FVabDamHAQo0HXyLzQPrY2BBPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPCFxNOEhwHLSn7O4FgkOV3ZmhPwm6V40YhvCa0LxtwyDq5tYDuEjUKh4tlg0miRcAJMhZ-I45-Y9NjrwXFpyZ3dd35Tx_YzjOGw-xadVRK4zinnvRb0Aqs8hyCl6xKjfUsdo05U2ad1DkEI9-r9zrDrhewbsj7nVtTC1DvXttVQY3eWrXa55brovVzork-iIrPx3aPp8joJ5lOM96wrdhXNLIUAI1NjzW7ZG4nZeyyoM25NonLXFcXLNvwp6hVAU5DSKHBF1vUKHJPbSJIHAEk05jXywImrl1R4xF4ROU3EPLs59fqCMc_YE5FD3qwSS4k1dcVBvMRD609blUdGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICc6jy0N_CBR0dZF2l5C3Jp_dSJjb3R5NRVAXEz17Q4r-GSRr08R9_0oniFtYtCMp3wq-1dU3ARdwBhjlbcprLHMc7vwGJXt9vB4DWqGvwwikc2ZYyRscrs8pIrDwZ8kTt_fnYGOjjYjD9kLiqTntL332e2i3I_H2QboEMR6HgcCEZtvrDCd1hhTZr2_lj2Xk-SYDdfkkU5aug8XY4k8W7WXvKw5ba5VTnpyuGsvsPK96kxPkQ8aWhdLPzLSSNIp0BuJsh0BZ6j5eEXS1SYkMc1o01ilEWXIghs0GJZiSHN0wOgXX9kdGrr6rDN7yU-ryOfkCHhpmbHul6VqtHQiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7IcRZuNnLGC15x328AyqPCfgjwvkLOZKakqwVInjydRKAME2jG3g6xszKz_00UpvqgyK8V5vcWSloohoahCR6dnu38udzcE1aPYfRVZ94RJOiylLoJSTm9nmfHYnFcrFIK4JT94eBXltFSrKN1g2E-ZJ5q8oeWakwWKFChX67JVL-9OLq6kzV2OfjQPNbk2CD0op3ohUzPslv5yfp217VU4l5lqdYqnJBwv-cMThUC9tAASzs8VCgDEHaWi1EFEJ-umSXWdqr1zw16xrDF1cwSdYDFfK-I4ejZ5tIfXVGIJEEmpjDai70iNIv0OCSxb2u7BJe646OC1Co5rRjZR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxmkP6hHMfCu3V105D6QT5RjryF6LiLJ2h_1ImA0bjUw4GVNCpUvB29wehE6WO_iapqCydrQUj4FQA-OxFj-OiemM6_w_4Mj5QJFAzZc0Da0-RCChc-ksSFf18LsuogxFBGm4a6Cz_f1cnjHz3sqZUUaEn2oYxCF6NFvbEEXotqmwpMYkesdktbyeNBnNZf_r6HSHdiclvWKo2AGYNho7OoMkTkRC7xQFwyxVT09NPEpmChpd6bKmIXrFL4JrQOmZ3kZlQdFD1byIInU4RFAGWMVFppyOBkoJS3wVXBxEjJZDGacGRdvMk3pMQJWRPuPnMfkU8GZuqwAnBbTcg6euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGN-iwHkFS9OH2Cq0DVXNmb-P0iuE1tlaufYA2oJ1152rc9h2-2iHuLT0d1af_F6_PKGXmVRVPW8MKlGQnclZWIbykqEpkwVHf851W-S5AFRF1YyQclRIWL8nQTuxEuk4vwfusja4kY34JMPRvYLz9Iponx2g9SedDTvITpEp_lCEi4ajt-qxA98J5mzFtkNhM4nKc5IajIxItfIJUmTc4oB4eAJdFyuasWkYAWt-9p_O_nu62fYF6qhDWqUyxcrHuklVogV2zsh4rH4oCRaC4_3Y90YUWcbztk-I7ukIkr99MvbsEIHkej722fb7O2zvMUhMwpTieKROCj1w673og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtpqRKPSlf8TaR9s1TPcTQRHsDsYUk-d3AvPZ7vYXCDi-WuUhGwwyU7tvN326P3oitDkSozaMSb4OSWIcNHHfggcx0fT-OPMljgQXqhZ4nu4H5JBVTe33YTW0HAnkOl4J--vjXBFdlHhergZgWQ9-u7G84a3vL6j_dYMCNsnDT8GaQhHFa6BqQoC2bSnA6R6NP99cmTfzKfNaMC7iUzCRSz87YM5ptKcez9nZ21q2RK3aU5gDoh3uK0oNvr5QIA-L3qLzpSAYUgzzx0z4lmUyZc7hu2hUy9HcUyqzMIoAnQ6BLurw_cFZtfqKmpwFIiV9QAPFAcqK_gPFYMx9SXCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC75YQwwSpJ3lM1t93A9uhb_vXBqJ2YNEchKdXZUq9COvzI4TM-AQCq5hclzU7d5Sw4sZsTQv_1WY4SoVmgwtmqrXILWLdiIQs5kpjypGd1GXBuK5z0KasIiy72Ahlglf3wwIECl1_VvbD_fVCcTEODG9hMbNh05hViu9IqsmiNh2nFGIpA_EA3-G4YGIxImvfN0SlGxRgUlHy-Aj9muylqoFd_9qOIek_RCS5XCvkElgIuhoOprN_uX4tDU0czED82WRNWOQ4Isvr2hnnvD33Pxdg2xnOAVXWeGqgVLpSTMXB-aQBthe3gckxMlGGo1Pw1gMnr9IDW5Kls6aLJnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT7UeHQxJuY61UckpjjTDzVtZIyekPfGWCFzMhid58rFF0lO2XhzSLvDl-hNfiaRcY2w51Ad7FPFGbWJJtXcgCDukgcaxgLOs5G_bp70cmmLN0q2Srx4APihoHm8IMaPWzSAQfff4kKisiQu2mBhzD_Ur1HYGUQhr9QCSUIVBjs42dj0gs_O2GGVq9CSKay7gZfZXB3RPVUUM4Xdx90kg5cx1yCkUc5GwJOjJA5i_4qCg6rqrUQKYc_XHZvayf5tp_pRAAxmq0CvScmLrokpVPKUK4d9hsonRiEItk0j7tZrchWdBlsWYWYDE818EycbI0KEdsdEf5XvpvBaIflLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMK-4sfS5XeloNubUmhpyMreCi2jRpSzvP6aYbFizQ9LBNoEAMRKDJxNZ2PsftEERJuVqqgMZWSuAa-XXNT2GtnGftWkSXucETPlowVqOCju3ofienVKBlC4umznUIoaOLL7-hpdX977jhhBn3optSeRIM05yHx1WfnaK-i7pklQR1NWOw5BF2DV3qkhlz-mgWRENVgSO5gHnztxuOnuAXhLVjW55b9EhmFHTqFWc3-ki_rI4NKNwBLomFkhhs0_lq8SrAikirLGZVy_Y_1K6FlVkR6QY-7bDQuI0o9GKAjvIZX-PIuSBGBgcAW6VW63C4C8X3B-flsMXYfULQddyD4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMK-4sfS5XeloNubUmhpyMreCi2jRpSzvP6aYbFizQ9LBNoEAMRKDJxNZ2PsftEERJuVqqgMZWSuAa-XXNT2GtnGftWkSXucETPlowVqOCju3ofienVKBlC4umznUIoaOLL7-hpdX977jhhBn3optSeRIM05yHx1WfnaK-i7pklQR1NWOw5BF2DV3qkhlz-mgWRENVgSO5gHnztxuOnuAXhLVjW55b9EhmFHTqFWc3-ki_rI4NKNwBLomFkhhs0_lq8SrAikirLGZVy_Y_1K6FlVkR6QY-7bDQuI0o9GKAjvIZX-PIuSBGBgcAW6VW63C4C8X3B-flsMXYfULQddyD4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Kkwfy-MDbXylnNpiNGRVz6Zf12zqIfCEh5uNQPnF6SxslbOw37Gy6I5jSRVhIWAzkGVGQ2CV8Lexv4W4Xjsna3AhI6SCsCQvldafrevXQoadAQF1VflyhQ6wSVNr_bWC8IC7hsEsqgpKCwcCPQnqA2IiL17vOmyS6KmjKknZb8kIzYBkhfQj8xH3iitOc0TZdxpDgolmO9H-Rccy3boqq_-Bou5_ogFQb2DjIp1BXFbUQ_M5CB5hF6Nl_CLndgJYJWQ4OcurXAz_I_DZzJfT9wRBW5fFQz1RN4px-2L39nhVavlhMmhI39paPrkn0Th_VVfWkoj3IMORCexyuJpLjAdotr-NpKsCGRbWYo1AjB9TH9pNxJot-W99fruuwlXGSdW3eE2T9AMrabxlm0mnazuVpbjGanrlVNvlfpUW_vNPaVSRKM2zgEOwO9rK5qmoy2WyqNC4q1zbbMrEqGw_x7xJZX5yhj4xhvBiJVWL2i8kszieCL7rkjy1otrniitfm_oKJRjvh5RExT6QUogfgrC7hcgATx9-rlmtiwHoxRXhUS1zfk8p3xUr81Kp0NB83FX4ZM95sOhiHJoqAHFj9fPbD4ZTaSkhu26VsqmHNIpq1G7ytXtFJVdtO9mf8U3ueb7oTeKQ_zHl-3D4WP7IyomCH8sIzIIMWcRriBARxBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Kkwfy-MDbXylnNpiNGRVz6Zf12zqIfCEh5uNQPnF6SxslbOw37Gy6I5jSRVhIWAzkGVGQ2CV8Lexv4W4Xjsna3AhI6SCsCQvldafrevXQoadAQF1VflyhQ6wSVNr_bWC8IC7hsEsqgpKCwcCPQnqA2IiL17vOmyS6KmjKknZb8kIzYBkhfQj8xH3iitOc0TZdxpDgolmO9H-Rccy3boqq_-Bou5_ogFQb2DjIp1BXFbUQ_M5CB5hF6Nl_CLndgJYJWQ4OcurXAz_I_DZzJfT9wRBW5fFQz1RN4px-2L39nhVavlhMmhI39paPrkn0Th_VVfWkoj3IMORCexyuJpLjAdotr-NpKsCGRbWYo1AjB9TH9pNxJot-W99fruuwlXGSdW3eE2T9AMrabxlm0mnazuVpbjGanrlVNvlfpUW_vNPaVSRKM2zgEOwO9rK5qmoy2WyqNC4q1zbbMrEqGw_x7xJZX5yhj4xhvBiJVWL2i8kszieCL7rkjy1otrniitfm_oKJRjvh5RExT6QUogfgrC7hcgATx9-rlmtiwHoxRXhUS1zfk8p3xUr81Kp0NB83FX4ZM95sOhiHJoqAHFj9fPbD4ZTaSkhu26VsqmHNIpq1G7ytXtFJVdtO9mf8U3ueb7oTeKQ_zHl-3D4WP7IyomCH8sIzIIMWcRriBARxBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqQiOecbdtSFf8U91Fc4WX2_j2Ym6s1dAhhFVXp3vceHpY4vUkArFbzxBoZ8ImaX1FpkqvHuxsDLyVR265d0WJBp1v1Xw77ic61c1oTY3wCOtIoJn1Sh6tHaitqzq9VGQfRwhES-GHvvQKxfsvJhVaej2fDQJUacx5glguAOON7UadRrnwDrvpB4SgPc90I2PoLKfyMhG7Ns_HkFiybRH_7wQG88LLmyp1INp2LTLGqO4rp4OdBHBV-UqB3AEqM4k9lion_4B-jOG4W6R69hOFmn990bI5D9xSUS-mWlf0ZQavoGgpJzKRr5AQmYkBIodjAwH7DSHmmBOZmVP10znw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
