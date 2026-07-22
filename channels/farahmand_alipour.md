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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KRkG0QcucR0MIfIjVoWjQZL4ea64ZU_RITlhcwtJwxus1NxfQo_eGShdZzbYGP3u-Cbdttcpgy9w-Of1b6wDUAjyy9Rg2VoO1uxWKSSq9mCRNl5lemMUtqjNqqxt2UExu0hb569orYJ3LPJBykmVOvDlAakkfBjHIxAZ8ba2TbHrClUzSr3RuuA23-prABlrfScad5U4wvkmrD2ZyH0np7nixKjltl6JLjkUUnKqdpAUKhi43tKUQI1XqRD6_4tWNrvFzgaxoCD5VXFZSlxxXuorCOakbb-W4DiOxvGP_QxDAIJ5ETXDfIkLmjN5EbmPsKnfEqbe3tqs3sTqu-Xcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=KRkG0QcucR0MIfIjVoWjQZL4ea64ZU_RITlhcwtJwxus1NxfQo_eGShdZzbYGP3u-Cbdttcpgy9w-Of1b6wDUAjyy9Rg2VoO1uxWKSSq9mCRNl5lemMUtqjNqqxt2UExu0hb569orYJ3LPJBykmVOvDlAakkfBjHIxAZ8ba2TbHrClUzSr3RuuA23-prABlrfScad5U4wvkmrD2ZyH0np7nixKjltl6JLjkUUnKqdpAUKhi43tKUQI1XqRD6_4tWNrvFzgaxoCD5VXFZSlxxXuorCOakbb-W4DiOxvGP_QxDAIJ5ETXDfIkLmjN5EbmPsKnfEqbe3tqs3sTqu-Xcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tXp6fL9k1bv-MGyvlSL4QNHShYmStIejDTXCJXX6mqXHPHGVDKpYuJBFxP3orvc3K96ezsRCqjB69zsEkq4KmTJ6u35rHxwgrkPlyl_A-Xu6_c5D8KKUB_ZpJCGIwPcSaZ1y-hVa9WJ7uph9r-yqIVHBON34ZCwD8uZBhGkv31qAzbZdvLq8vTnE-Kz_li5IEGa8RJNgrfOPWzjAIEcqSP2LypfGvv-4_Hk7VDy2Fottqu0TjJO5gCdSwNl5R9HucAOBcvrwdN3odzE3fYAnRTurJI3PvQNSaAMvmNpAmaQT_UmnfiwYz9DxWCuj9jzlsyR3JQvxMSXMhtvV9qE1_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=tXp6fL9k1bv-MGyvlSL4QNHShYmStIejDTXCJXX6mqXHPHGVDKpYuJBFxP3orvc3K96ezsRCqjB69zsEkq4KmTJ6u35rHxwgrkPlyl_A-Xu6_c5D8KKUB_ZpJCGIwPcSaZ1y-hVa9WJ7uph9r-yqIVHBON34ZCwD8uZBhGkv31qAzbZdvLq8vTnE-Kz_li5IEGa8RJNgrfOPWzjAIEcqSP2LypfGvv-4_Hk7VDy2Fottqu0TjJO5gCdSwNl5R9HucAOBcvrwdN3odzE3fYAnRTurJI3PvQNSaAMvmNpAmaQT_UmnfiwYz9DxWCuj9jzlsyR3JQvxMSXMhtvV9qE1_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1uiYWDDqunijg_0uc_PIUMpzslMAVzYwYWHB6UPJPsMkdhyRfqz5KfA-Dm6MosPasv9sEzGUOkM4TPKha7MN-Jjn4LUVy2IPZi7RKNKf6Y1WqJ1_XTav59hOapEbuOG-KxjWy4PFiMg_3OYvVzfZC68P3d8MJNSon30RBmXqRhTozzq-FZpFofep2vcyPiZ_ryePZbDTidYOryTEV_KmGV2lRIgW2bO7JQJqd5-YO7JkcNi73OSDEF_LnSf9tldJej7aMNDGAlX8ep2wgvhYkKuyGCZHNWKCXVbFWN56iadLfjVYQFesIHJnPj2EPJQbaeA6D6wI2qZG3OdlrVCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgVEE8H4Kg0S5ayVk3ky3kZxPyk8T4zJT-qg6NlLnnsfOwBjDcjXjfT1h11PZ3Q1ZjIdLYWNF9D9q6qIo1u5CizBHdAjkwxVcUfc9tYSN8K8-EKWnWF6A3OGs1aGORDLIDWTC4xVbWJAZw48gbUzD79Wj6xl1tSV9hU09W4GrMuvzDeFvoZwdRwL77Fafl2_2hhRIUdJyskzhJ19pKPfnHnBdufXqMXx9Asa6e-Rg2FA6i1flpnYqiZXqQgrgkpdL_p-kXiEhJtR9eYsf3_1vMmR4MCQvRV7Ce6hN7JzPXXTKw33dgKFURYFRefyvIQFvOLoe8qGwBXv_jcuTm2snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=tmF0uYWfOl6rQjLnXc1ergljWV65ypojENK2pMuIUwOZRZv_c3Xuz-cpSbiNbxCAxLuGRwDmnQdYFstOLckmVQv_4k-sIw13Zd7ARtP6OzbNTPrrNf9V4ieIWOe5rpz3wNmv1zVK4KF34DTnbYE1fY1rhk32Nwd-I0va1pA5AN5De3EG012e7cRvpV2WbWna4h74uGxe6licmI_cAhsCJ2FxRtd8O2NF1APMdydlUTVvly8cU0exrmR-779BvQS2xep4nXRnyFJTekjsYgdFOKrXnRJUbFp5lWScWL4Js1DADgKpgqOXgvg-wfuAg08aEgJAh-2Y4rIGQTVyXa_hFG0uK6byAkMp1wqiMT5OAJ1IRQPo8aaEejrsFqK3pP_AtUlubBk83UU0KpiJZGrafBkih-m_m60YT3dFYdBFHMAT5VMheqDZm306UiIkLeVC8wMOEMBb8Odi1ljY-cZDUy5OocQflnBJH9qK5RWtylhAO5dCYuCVWT-FQCZP0FNIUP2rTJXN5wUECBEgemwqSdHbnRGiwtU6eWqJyJ3Z-w5o_Iyl4hzNH8kHL7gkmjvlpfRjILtl1FclD-bOprP2zySLwN8pTuB2sB7WWqy47RgsFkhUTQhq9hD9_rJvDJdlVJwy6QQwmQmwyXIEgSuvfrpLPOJeFuhSey_hJMToRis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=tmF0uYWfOl6rQjLnXc1ergljWV65ypojENK2pMuIUwOZRZv_c3Xuz-cpSbiNbxCAxLuGRwDmnQdYFstOLckmVQv_4k-sIw13Zd7ARtP6OzbNTPrrNf9V4ieIWOe5rpz3wNmv1zVK4KF34DTnbYE1fY1rhk32Nwd-I0va1pA5AN5De3EG012e7cRvpV2WbWna4h74uGxe6licmI_cAhsCJ2FxRtd8O2NF1APMdydlUTVvly8cU0exrmR-779BvQS2xep4nXRnyFJTekjsYgdFOKrXnRJUbFp5lWScWL4Js1DADgKpgqOXgvg-wfuAg08aEgJAh-2Y4rIGQTVyXa_hFG0uK6byAkMp1wqiMT5OAJ1IRQPo8aaEejrsFqK3pP_AtUlubBk83UU0KpiJZGrafBkih-m_m60YT3dFYdBFHMAT5VMheqDZm306UiIkLeVC8wMOEMBb8Odi1ljY-cZDUy5OocQflnBJH9qK5RWtylhAO5dCYuCVWT-FQCZP0FNIUP2rTJXN5wUECBEgemwqSdHbnRGiwtU6eWqJyJ3Z-w5o_Iyl4hzNH8kHL7gkmjvlpfRjILtl1FclD-bOprP2zySLwN8pTuB2sB7WWqy47RgsFkhUTQhq9hD9_rJvDJdlVJwy6QQwmQmwyXIEgSuvfrpLPOJeFuhSey_hJMToRis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buCCNJjxiRpBkrL-rcF3WJSLXGRKmph4G-kChYIS_KZMi4o5Ybj-UhjkhZLSg6sNq6vfnSXD75JeDS1G0SxsexlTbs2XZjjXWjD1AdjpeEtgr5Fktr_2mRrJqaMpNck6DKVTbcAyeR7X-_tKUORtZNXpqNZM_Yg1nrx3ql1FREoxBNRHBEtVdt6MfQzLlOOHrBDtEgvjN7VrzcUgG3hrxMJkxO1vRxLileojapj7FZQP9txwj2jpnkKfbMus2Q4KMV-6RCR24ifqLdPXuJ52x7E7LLv58ywEXbXETu1g5bczECWqVJa_wWRy85Bs_7tWD24nKheHij15PcNfohINqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhKwiT0-kGhdoiCAwd9xMFGdC4dkJjm5P43lP-nEzNjwmEoNoJoMZdzSeemvNnWBaUQDAghpV3jWRxPpIZuUd-UFMQwaDM8qKV5Z4uyoNbXRWx3MaSjmhIxsWxpo8MVnppRvrmdxipOmkgIHv3K-GG8PonAC4Sywe1YVBUoKkJOQ1hDMn5RKy81d4gfeV0yT4LCfNL6Kym7wdlD6JVbVnvCXzmUVgpkelPqeDUUiePveYmomFyzWVoHjOmorfxdAMI_wnM7SkaQ8YJPDI9RO05slkQirX8qaSsFwoTVRi1BFKc3fjvR5YHASltLKU62Sro3djSvA-lNrKl3nYfj1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRhbuGLm0yOHqshFqJS6ysbXa8Dwv2ufIb1urgjABi-9XOz_Gs1IHiIP8DIQ3FObyfB2BqCvR0FthKblGhWpcbkuq8tdBmpeRLEfDuYyvmXTevyfQ2y6PZDKkvtg1mlC8qopSX7H-odNg7bQ8ZHBbittWU0_jBFF-8lrTPGQCu2NnEMG-E6IDPvgViBX1e2R-5GusHHB2e_1ffDo40mq0gOAMo36NbQ-o51mNu2D0VO0NGfW7_LNnqXj0PJKZGr9oR6IcP4eAvtQ5pJqqOZQoY9b63LhvXUiFug0PCeRkSs9Z_79vDdp_XwYtpP7pY7Mtw4KT2Zal_E-CBTnKkST5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7Uuky3kEFSI6sw3Tt85bPkmTUavIOV-8f6YkEiYGSlzv3zu6XTKsB_BRd5I9cARrO4LLR5Pe_z_oIN08DXY5RQ246f4ozkCGpQQcgrtmd6mWqgWTTVlN2PnxOEBwkmp-N666KGIBYkVHDObXo6wAtityvPEGrkQvwN3g2Dvk-r_Av5RBUh56uleFezpicDf15TcuHvAeYYbeImiIHf0s78tQFQlyoVkoABpkZUhdc23-Z5c5UgFhrMj2zd1Dq1WB7VuSJE7cgOboBluPGTCKZFGwZQ1d4L-Bfqd2-dTDe339CU_J9xrLQ8NhbapQHypqWOE1bX2YaZOesrw-X2zyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=O5eQbDONEkTKL6wwGZB_iA1YMk1dLgNCtF1POUcPiGf3zD-kV2g_26K-jih3T-ZE-RwuiyTC5ZIarjO0tf2aqZ3L9L4On7R-RaUivUfHDGLDeSjK1yhZhlzJgCG3k8tWWjoiswDaVL-UnbYZiOzwKmPij9BIchBB3kzulC50PKD9062MN9i3UnxKs2EnuKoznPMm4azqnzapLymDf0A0tA7XQPl7p0hiU_DpprE1WuRBRplBg0uCMw07fgxqKRF6hbtJQbn_r-7_ewgCgdX289y1WRVPVK6XzGdWQuqXueLD5hdFi3S-4WiiENRZmzrxWyETd59MDq6aMMulCodmpHaltxga0r_THixtjzctJVtmME-o7CpyWNdjKDyGLP2PaIIQCEa5XBWfOTk38atGhGVqbZc2uYBMQ8RcezfrOASzd-4SE03_RiOKH8BklPfjTMDeTKbYFQReA5pXwik0tc4V2RWdbTX6FRpkq26PxNw01tr2ilXx401rcSAK8Wv3kgzeC6Hd8T2IwjzKoOfxsbxt-RIL13ic2K8r3RMDrZWw4Ni_dToo_SzMcCH--U8cEdfydjksxjSO-Sf0DNsZcMw6x-xdIjZS3BiRc4wseHxk9JK91PCPyGXPl8jN7q0CSKltOtl-kjnpB3WzO_5Th6OeTsKsoDe9B4c9hK5qSIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=O5eQbDONEkTKL6wwGZB_iA1YMk1dLgNCtF1POUcPiGf3zD-kV2g_26K-jih3T-ZE-RwuiyTC5ZIarjO0tf2aqZ3L9L4On7R-RaUivUfHDGLDeSjK1yhZhlzJgCG3k8tWWjoiswDaVL-UnbYZiOzwKmPij9BIchBB3kzulC50PKD9062MN9i3UnxKs2EnuKoznPMm4azqnzapLymDf0A0tA7XQPl7p0hiU_DpprE1WuRBRplBg0uCMw07fgxqKRF6hbtJQbn_r-7_ewgCgdX289y1WRVPVK6XzGdWQuqXueLD5hdFi3S-4WiiENRZmzrxWyETd59MDq6aMMulCodmpHaltxga0r_THixtjzctJVtmME-o7CpyWNdjKDyGLP2PaIIQCEa5XBWfOTk38atGhGVqbZc2uYBMQ8RcezfrOASzd-4SE03_RiOKH8BklPfjTMDeTKbYFQReA5pXwik0tc4V2RWdbTX6FRpkq26PxNw01tr2ilXx401rcSAK8Wv3kgzeC6Hd8T2IwjzKoOfxsbxt-RIL13ic2K8r3RMDrZWw4Ni_dToo_SzMcCH--U8cEdfydjksxjSO-Sf0DNsZcMw6x-xdIjZS3BiRc4wseHxk9JK91PCPyGXPl8jN7q0CSKltOtl-kjnpB3WzO_5Th6OeTsKsoDe9B4c9hK5qSIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=K1YVm-CbmiMM3zn_r8TAxXRt_UYZauptLrZ_j_0xxukS4KWLJqvN-DDf2zS2JN9Tb0tSuwWm8F602gUEP_cNjqEbbKBKejdpLObXVmFDujGzGi3flE0IFEz8D-LyAZ71CtcMgqfymPk1td2MEO5GQ6JNILXdNWLfV1Zpenb0bWSCY5qnIAHS3I3dXKpoIq7luaVvPop96uZDsg1TqNId5qiQUADM2S6-53VRyX1JHGsm_rLDEQnDKIYSWEO1o4NtcC7exjhcksYswPFtO_diBbxjrx_7m4vw04VhIfl4YF2fRPjdfVWcKgByX1FvxWm06rdiaCXTOumPRIQnSi4Q9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=K1YVm-CbmiMM3zn_r8TAxXRt_UYZauptLrZ_j_0xxukS4KWLJqvN-DDf2zS2JN9Tb0tSuwWm8F602gUEP_cNjqEbbKBKejdpLObXVmFDujGzGi3flE0IFEz8D-LyAZ71CtcMgqfymPk1td2MEO5GQ6JNILXdNWLfV1Zpenb0bWSCY5qnIAHS3I3dXKpoIq7luaVvPop96uZDsg1TqNId5qiQUADM2S6-53VRyX1JHGsm_rLDEQnDKIYSWEO1o4NtcC7exjhcksYswPFtO_diBbxjrx_7m4vw04VhIfl4YF2fRPjdfVWcKgByX1FvxWm06rdiaCXTOumPRIQnSi4Q9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc0VK0qau2ih9J8QSRNtYTiobB02Ye7yguFd_OYN7t8qaIQOB2HodQaU34o1bDHTfTxgmz1lpFg9COzwEy_J49AQyjKrNX5Qp14Ze1HbMo-VD5Gt_PDDGZQx_9nAqIKBFKwrLB502On1AmrDb1yojO3ig-l4QxX4NhTv4hR59oKr3HAUbFSLlRTcjjX7XOYCT8ilSGlW4WNwxYfuZgPpT1VVEfjhDnqYNG6GPCArmx-BS76REkgXqh-UOcN6tbu_hhP4jek9qwBYE8olk2YU5zww0UWsIF25QWiMEryO9hfcycwvDh2LkeOFASmUK8b9ZhJYZp1PEKJsdLMEPAAuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXwFWdJh1MlCvIcVFtirVbQ6klr_qyzCAh_8V5N-JTzn1DfYSEJsR1z0OF6FuZ-wKuMAezlB5FooGaJ32VSnfNb3BGHTlFd9pMbdmh1KSZdL1MppWptGJ3SwTtUrr_wp2r6kZybfmH3UzPVEcxjib8BdnaCKn2itN-GFLs6RJqgF6J1oMt-rTF5MxEnH0afjJ3moEb19xUcd_4ZaGaL458T1nEDrbB78cGhuwYGjCD8WLAyvTysC2r-w_N7HtlRc3gyV7OLyss2pRIQ_ynsdn55jHyB97oO0mg9fSOPoFnjrIOq1wb0mPWUzvC5sMAPhgoHJSs65pZU85mQmPyd_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijwV-ZvA-wiagw65qfYLHGmjB8NmbQCaRY8sNT9eDp6ktIPby33MW6_eXFIYPu5hmcx_8r3JoBct5bXRpkAZZDchKjsw8QDd5dCxEBv3CTzAcL_bW_tnQoE2HEChAQBfL8KQ2kxBkDEYBlVN1IArSPoQFtn0hBS9EJp6BPEIodYTA65Gp2LAJzjh4wXlwssBkLCqo8pPCNdh2XFwkcOl1sSAEP9DdnPnJuld-pHJQzPwQuw5iSOUg1M5wGzuNkt3qomGAkak8jqxXuJUVK7pd4tqcZxAScLk9GoNeDkXjcex9WqGbn2jZJmwuiquqwNgK-Tdt3QvNyZoTw6gbifUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvHEeBo5EaUEH8SXfnFTmMdzeEJAiXtvIxbHoYLskz3JaJTack4y4ndl_BxfGlij0RsZMqQNQOLJGQgPBfz06dXgno29w2MtmBDSN6Xel7L1tFyo9KxtLvHZZ1T53WoEfeNegeh72nVtqAjkwUGMEwvCSw9exVKtQmQACK5HXLnyqA4I0wPENP4KEtJ_rzQ87o26oITfH2Ekl18u3j0rCgvGlWnzJZLKSDGrrIyV-N3z4GcgQpWpcNkdAfQP3UXvUbfjrqfQaVANeN0rrw3y2siodM1EIAWoeIzRw8Ue9yP2vsKfS6vt8ROCghfBe_f7t4wNV3l08JCzdvQ722a6eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiyY_6I5orauyhHWxRtHS4qtZpD9eo4VH_ul3n5-OTu3XxdgNpCouHt4T__h52ISAgTaXyco0OLplMsnlpau6eWTzdthUxb9FoebA-wUr4BGC3yf55aI6_ZulDg8L5dNUVbwhEhFi6EHQWsqjKW5xyhTtWHDFxqGJnAun7chFyJvZZuB-yoTgKRBzav78ys1g5o1fweJbWFK8IKTuTsvndPl-kAwprvI8eauIeHewOa9Jb14VnCy1EHjUub3xkV7i4qE-YaTpDjyAb12SALxLd0nsmm-ut8F7_VuVpep0rSfBWs-akzXS83VEow_0vv9YDBSpWYEOWpldXwnTgZWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5nM4hKatbowepenteZigeLgx3qEojnJS_uozF15RIKw8ZypLFCkuX5Cq9Jog5j9YymfBhdQ75DLnkhcwKkwK9LppFSJub_YGsP4XEFpk2UMIvWoYi-M2neulA1uKNTEoLvaFEXUdaSoB6SMrVQ6J7TJB27gIpXOwKF3xLwy-QbwTd1X4tlHhTRswjnKHcbupr7pQDknSCXlhKKuhkGZdQmvlo2H0bsfStJ42qBZ-sEPv30aKrrPEXH9NK-wGoZLOcNJwWNSouoI1E9mcIzbaFs1Pv04rc42d2G26tkpoG0GbmjpLOd8id82JmxJAzFxEiQMJmFIac4UIGVhHGTlQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6WJYXCU5AdX5Qnt6tc0dMxUmT-GlYuM-fYXou1shtCyk40PtDOVqW8YLXcJGTRc0kr3j_-fqM3AsyO44wJI2pIt22OAkmXDEco8z6Egi5EXGONhHmGIciwNeQXNN0COYsoahg04BGFeAaLrxgMRA-JUH3JxNvO7K30EaP_4ENvBLs6Gto7Y-li-x5RtKKYylaQYFEU58EqPPcptx3ABJEabiRFVO_zfH2NLNUWfhJ8Sg3F18CRLU3QWlw2FZfYXbMurOKVQv2AwxIQNDePN2_2Bsk0jtSVi3XJx4vokPpA0SNZtSdPlkKez1FhlQb3ObipmlTn6HuIPL4UoCNQuRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=lgRnho1ItjuIbTfJj8oxCgpoXz0SBtTSJ36V6D2Z_xOh5GDsruJUzyEc75JdhsgYz3aN4rRWRioxZPKe57pHmHKyw9yNks4ZOAIb-GfNvX6XK2i8esOZadZEfd4jKMhgp74sxg3tj5aZJ80rI2918jTqJfBRFo037Wykzp5dhBjM7_mEVTNReksd6N3DT0pHgRDoH-moDOi-zPKyXAzdpUoxj-cEHR_2Krg_p1zG8a6g8XkW13Uz_MPS7_ompLqd-xqP6_WsJjiOA6X83KsUCagehICzEeb5vENH5d9s2kFZvkGNVdlbrColV1ezR14-PM18ZzIQwm4ZUfJIO97XWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=lgRnho1ItjuIbTfJj8oxCgpoXz0SBtTSJ36V6D2Z_xOh5GDsruJUzyEc75JdhsgYz3aN4rRWRioxZPKe57pHmHKyw9yNks4ZOAIb-GfNvX6XK2i8esOZadZEfd4jKMhgp74sxg3tj5aZJ80rI2918jTqJfBRFo037Wykzp5dhBjM7_mEVTNReksd6N3DT0pHgRDoH-moDOi-zPKyXAzdpUoxj-cEHR_2Krg_p1zG8a6g8XkW13Uz_MPS7_ompLqd-xqP6_WsJjiOA6X83KsUCagehICzEeb5vENH5d9s2kFZvkGNVdlbrColV1ezR14-PM18ZzIQwm4ZUfJIO97XWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrLRtUiZJy4ROSOlVLUU61PSNYTYuknem8FWy-YVOx64PjGArGG3sZeBBVIWz1glogHxBo7IXjcKfMclStSTrfWCTK84wKZEmbtw3rGC8rvHD8nR2xGXmA5DE9BRXLRQBWluJNnFIKC0hQRjC82PX_xdPBKCKT54MDpN-kKUzMKRSsd4MdkXcvbCCCrBa3f7F7m-CSyM28WVCodWHQ09sDz5NfVyBQQ69LRnMdBbX7rL0UyTFItbe_OyIp7Sugtj_Zt-xfttE9zYfKWqvfujIY7jb_67dvy1Pqf1l6aNVVgHCckuJEhh31Af-wanRt6f95_OPABP_d3-9baBYe8CvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=FWVKE4eoCTzKoQ6r0X3RTo0Iox9GqMjZHU5BsoXUk-CyG832F6nxFvlgeo7nLq8uNzCvxEftGSpbYXdEzo2HVbKxk3bWyR-I_DDDf-SSiMnaYMF5q6yv2h3fClJ7H71j8WMFf92XBsEn-zEQeb_Jtyu6N9Cpr3wdeDkelrkUU9In7HP1UFh0WcsNR272tYGUT_Vjxx6hnKIZeNQM0OgOWfN_82ZrT_zrFlBDYCYEatMZD8GGZCuDGXCs3ZB7LdzIXGL5eMfgWJ5QvoRm74hvt-IpeM3RxjmpLaDF1y8jFUt3DmKU9fp0MyvoKQ1KYoXX68_NsgnXW0V4HCbv4KbfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=FWVKE4eoCTzKoQ6r0X3RTo0Iox9GqMjZHU5BsoXUk-CyG832F6nxFvlgeo7nLq8uNzCvxEftGSpbYXdEzo2HVbKxk3bWyR-I_DDDf-SSiMnaYMF5q6yv2h3fClJ7H71j8WMFf92XBsEn-zEQeb_Jtyu6N9Cpr3wdeDkelrkUU9In7HP1UFh0WcsNR272tYGUT_Vjxx6hnKIZeNQM0OgOWfN_82ZrT_zrFlBDYCYEatMZD8GGZCuDGXCs3ZB7LdzIXGL5eMfgWJ5QvoRm74hvt-IpeM3RxjmpLaDF1y8jFUt3DmKU9fp0MyvoKQ1KYoXX68_NsgnXW0V4HCbv4KbfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZgav6V3KxEY1yL9R4hk1JZxsdiqnEk1Aav-PxY4b1CTEDLNYiQl7DbrfE7T35gAouo5cISZCXNds5HTV6WUFTW2cLWbH0yqAmyj1iv6r9oldHERYOo24j_3OJ-obuaAWjvby7RTsfCdKQEthVa2xy01dIbbK-QG5PeHKL7q2JivZClwAI3S7ViSTBuFytuoaXDqQreaKPSMvCiDZroc2if4tbufNJtqLDdPjp7NQm0Cvf2GyYurl2dzOC0aptxyRCVQiq1O4poCTTjzRylMJfVYWKC190ia-ys1L9HhH-8bXtOWTgrL9fIK_xXIurV1LInlnZinsaNfyfj1_3Mxww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBd2nKDY5PrdLp2UMbbpcAHiLnTzQu_Cx91M9PagJh2KLjQHmeiFnGZi1XlwvwBJ3aNe83HR_8PudHptfyJU2HbNIzpskkEJEXsJtIXmf76hsoHFmRIJom6puFNt1Ld0s36IEubS65cJwQM7-BlRcZn2OHIq2kuJnus1052PVnAo4ck8We0E_4HAmqTniMkBQz1mauevDU5Gm9gbDlq9H0eI-L5ULm2ES25LwvegCO08H95cdsMtyyuo8jnAZl44VZUIirbF9-36kgeTbXX2FHbsMpc452cZzlkrtR9QdECGtzElcYx6VJG1Yf9czGyM_WJ5lmyd-g9fKoN-gCXAAjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBd2nKDY5PrdLp2UMbbpcAHiLnTzQu_Cx91M9PagJh2KLjQHmeiFnGZi1XlwvwBJ3aNe83HR_8PudHptfyJU2HbNIzpskkEJEXsJtIXmf76hsoHFmRIJom6puFNt1Ld0s36IEubS65cJwQM7-BlRcZn2OHIq2kuJnus1052PVnAo4ck8We0E_4HAmqTniMkBQz1mauevDU5Gm9gbDlq9H0eI-L5ULm2ES25LwvegCO08H95cdsMtyyuo8jnAZl44VZUIirbF9-36kgeTbXX2FHbsMpc452cZzlkrtR9QdECGtzElcYx6VJG1Yf9czGyM_WJ5lmyd-g9fKoN-gCXAAjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qTuIAr-x6rflbtk5mUmqCEp0zRxqrgd85C1_1ioZBUk6vWwxu8hhatukXc5c82NpRRvIA4psZL1_djQsPVDuvpPmaK9bFmndeeUokIL4dn0jpNXL7ewBRjkknHMcngtWT2kia_z9pV1eeP4V2vJ2AwYDgi0PnC22OOYz3KVTQRijzX_KqpR-VrnUtNsnlpwlKUW1yqhiHrdyAJsJS8IpNDELvkBg_Fhi3Flpkw1LsHIYbN6eccpeZ7ZXsBqiaXnCZC3tJkIlm7kSG7PSmumGt84XgxydDlhnZ6QPFQUCSIfSSqkeXPAeOGu9GeNuqWVmcKd-5MztsaoivoPjfBbUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qTuIAr-x6rflbtk5mUmqCEp0zRxqrgd85C1_1ioZBUk6vWwxu8hhatukXc5c82NpRRvIA4psZL1_djQsPVDuvpPmaK9bFmndeeUokIL4dn0jpNXL7ewBRjkknHMcngtWT2kia_z9pV1eeP4V2vJ2AwYDgi0PnC22OOYz3KVTQRijzX_KqpR-VrnUtNsnlpwlKUW1yqhiHrdyAJsJS8IpNDELvkBg_Fhi3Flpkw1LsHIYbN6eccpeZ7ZXsBqiaXnCZC3tJkIlm7kSG7PSmumGt84XgxydDlhnZ6QPFQUCSIfSSqkeXPAeOGu9GeNuqWVmcKd-5MztsaoivoPjfBbUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXbWb6RCE-iy7rr_UTMPjfFYGGPH-oRIFGHBThbiX59UOgO_z9Mo059nIQjMK-Wh8tufC_lDTcGm-GnTvbWFGykR_wB717nYkzZxa7XxmAfq_g6JpmQCaVimxMY3zzuoQDOAZ3YrA_MIbI_c2KpQODku2RpHr7AzTAgBzAx8aWmyS-mhub873_GzJ3FsMSVdQ2hRdHNOm42ou3fbLOoHYKp_12QhyfgDvC2WEm9-NC1SNHOQIja9_ePY3Rc_A2WuBEpU0nvKmakivEOBMHvFXW05cN-rrUwWMBvWLJqVqArt0R-_fuvBpyNWbuuPaQnRqoI3T0Yyth5iwhIHvgMUnLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXbWb6RCE-iy7rr_UTMPjfFYGGPH-oRIFGHBThbiX59UOgO_z9Mo059nIQjMK-Wh8tufC_lDTcGm-GnTvbWFGykR_wB717nYkzZxa7XxmAfq_g6JpmQCaVimxMY3zzuoQDOAZ3YrA_MIbI_c2KpQODku2RpHr7AzTAgBzAx8aWmyS-mhub873_GzJ3FsMSVdQ2hRdHNOm42ou3fbLOoHYKp_12QhyfgDvC2WEm9-NC1SNHOQIja9_ePY3Rc_A2WuBEpU0nvKmakivEOBMHvFXW05cN-rrUwWMBvWLJqVqArt0R-_fuvBpyNWbuuPaQnRqoI3T0Yyth5iwhIHvgMUnLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NArYAePhTw3Qf-S4k14pnAmZ8jFlYD-am_e6ozx2_fXoxhaVy6bkbLz-SuL5E7mgUCb70NNTFyTuEAmXV6KbEP_Qe800OfMOqQBAmUUZOkzIZvWZIP21rXcTgeTSd2H-5Cm1GTjkoFu1E1Yybx2YDDKs5C6y3zTvkExk-XWj0c9DcVieU4lAr4CF3JPIetiMf6wKVSpJdSO4qtoHdq3i_WgiQfuUk7mZWHREJMQ47A6Ypox12-OYEmthZEW8hhVyuwpGPj9TQ5cQrwbBfqWr3gE3ApCjKJpheddYEb5sbEuI40M1JbxpXetGntEbA10YJSxOBW1xCdpZBAr8NSrwVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9RB_B0SGs8gqdk1I_cbyjoF1-flOr-jgTgp-XSrL4v9md9PYnZjSnFFsitV48k2I9iYzzFeoQpkHAxGrV8HNvQSB5QfOWMYnhFQG0AQ6DX0wwvQgh-Q6kwCgCJtmLHc4iqv4SqU21tBAgJLLKu1PFrxDHEto-yGEFbYehgndOfWPDykcQ9DYj_4rm5PAwPbXJtZd6TY8u2wHO6EHiq4nf3toY3IMrgwVoh3Kif1g5S7zoKDdQyGoX3x2Z8XHSz20Ha7uiH63fTNg_OxYkGLlmICVs7YezG54oFNTN4_T_JH1aCOHgjvoIPLIVmh-9gb6aXXl4gsnUKC0RLJpBEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmGo4meuIogi4ucve4ap6dRJfOYIV8ZltIur8eugmJ2EKAKFjj-znjpdU1gnEEC3kKGkin2i3k1i1nlqaNOTBlEV0ptkl7wgrwFK66in5hqEOYXWXmgRGYUQWJABVVe3jvJp-kbcrey2CWLEvQmRX6PlflkIaOc2I-Ha5UCwi0fed3wu3Ww4yvCnSfKqDMmw4wqMxtTpmFWPel9EOwOgmtKK93s7kzBKA7bUC91h0WlZZ8nLEfPBFIlcDBkjWBZUBWhDXAfVkUqbQlBi35s8IIgzR7CWhxhU5QQNcQmZ8WGAxd-Qpvps8p3S2khdukRmUuq9Vo3sVl0p9IRM98bd_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnt_0SfVECCatlTyftKY_AONoujBlYwZijdKYw38ZLB3pg55WTnlwGHXjZecIf4Xa_stWc_tEFPm9OwGwSSHATTqOanZJquc3ZobRA6ROF13xEvkTpr3Mj08VFwPvF4Q7YJIR5ImdF75db2goZ5r3WtMCYCNUQYUtvuiKP8GGPSSga-kp6Pt1fcMDOyVhdb9-mKlJWXyWW-w-3Du5Ermt1t9MQj4EkK-35Ms7WBVPWhHj9JKSKtqQusXqaoOyvPvHqXQ8Kc5AdFIGlwoyxgnz6tIlgjC8DyjRi1SZjieDgjJWM3I6a9u61JUUda67u_Y56x-6hZ0aTyOpWIjbQBZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJae96_MdxdLe8QoDpYG4vj6k5P1KFVyq8zNe4gZZ7E0KyqiJzAZAIjNedfthKDpykGKMAoqG3v8CH0Xa0cEQUsE_T9EJICT4wvgOZLbxlt3dyAqBjA9guM22b_VVHtg_z9gxFiWBNf2SWGxMdyVH4FwgOdB_Ara8fDq08WoJ63HrCO7PwGz4Umru8Fg_P6-vWsGoH7hKzu6O_qGTvPdJtIQW74VMEo_bFLG9WSCIFhdPZVE4xPJsTu51wmHNekSCLVknZW5-l13DcKS2omGRdlO7YCjLEq56RjYujp_wW5XbiyWSE6iGRjF1XfrR3YTgVU9lDCl9lK0dtjPB3LIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCAAdey6X0kNaArUTvRRn50Tgu2tcPjBjBjM1x9HJp7nspzaQjMmF9oUFGmbUxfqpaotDhSFtHD2QblPZTx4AG4wotYoyM2AVJ3lSuqGBwwxMU7mjVjHbkZ0hNozkhtAY17qIKDBmBcFBD4215eFOyiQDOsiSosK1Jg859GI3brENhuQQChbs30COAaGFHPL14AtTpRGwM6VXghlPHq78P3zLagMTMcq2Vtc3JMGk9P7-sRmPFMuqjaBLThUXrRJ5k8l_kMdRUgEUdIEJIFJZ6BNpDsBT5mpWy8pzRaoIkgUVuUoL4q5CJO5WrKSVch5bJ1v4nGn0EBkW261m5o0yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdybLbJsaRB1SzJGPOsLXiB8NqlcxOkD3RRKSfdankh6lwV114eVa-XsL5dEst-CmPiNTgiOrRW98nAofmwfh_G1638yUdchGXal25G5FpW7aiOqS212aFvhPyetNCRZNuugDDCuK8rIjcIQ8J8UFH8gmGFtgfKx5xrkiehYNI7mhm1BFuhYRl9pWFkyeChHJmlePdIt6yaHu_k5NbG4mSYRZKQ72M-dCnak06jZQPgNyc-e5kaQwQNM3PFLXm19xHVoq4Cv4jEAHFWBSqHmHsdgOwgamsaPSc14xwS9ndvqg7iSstzLSaH6qVpeJkGHT8xRhncCMPu9ladH3HG6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjip_Oi_7xSvnUldK0oQL9MNc2dNt_u7fzyZn9H9jWYFOXk93D_5tAvmuGFg00jyqZFHiJ9nS6BCwAzEZLfBMxso_9B00_6xnbrc90lJPm7f7yrGHBmzWmp5PaeE2hOjAh5gSweO0FzOL6QvG3JSRZdNQftDQrJZHNQd_0X-w7M91KzmLo5D3b-AdIxgAXWGsOwT9zZjUuYgRCAu-bdGmhAP50pPOTJ2Ymz1tYi59nOTZWZZUchXrnOsJL4YNCJBoVVasWdx4EatHd3PKWWyAW8ZE4ajNsbkZ8_pypCWhJ7vmwOmWPdNjEICoxff4qow04nkUQiFe3gJ8ObGKYNjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoSRbPapn3JZjlfBvIzu5uzsloTG9_GaeLztZHirqNxltbTshjdWTRqlJ2vQEi7Nc_9ALr5G4VdgQQ5ubAFgjck_oRGVAQnyuF1UcKrINGwuDa9doCKe9A3IjNDGA5D95mGfOfG44FH5nuMVPPsjuuTvlXwmCPRdkAKhJtQVmW7hOE5R--GBRuHHTw7-M2D8y3y5NZm5FmCs7dVN_yMBxkMLsRpgdtaWEaQ_GrvvpPoB69zY7yYyArUfHef7AloHrQ-ESD77DscCmvbIETzNuT5XurPW51JnnOg5P7AFzHUVjPp2RcDKwQ_kmmF9-FbeokrkzQdlbECi8OsVB5cnNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYDllcw_Ne8nLSEQ3P90yC1XK4jKKILS2tHDkafwSaGQRvkSH6CXO4zkjaQWg9sp2vyQwId8HrhelGVzmRAY5XaGTvKpFzJ3QQUbK5WMAe8KzypwEmtKPbZGon5BfjOtDXXz-PP0MEovQalQJua3ADz_Mri-vj77YesfP-3qrrXKDQdIOtcJXC3XjK5C4STnLng2zkxUWTY51yYLgGSVAmRKRud-y-HYzyxRAujkhmYdkWxSNhVy-oTK__x7W7rcrAHsCkCWUnv0NfRgh_FqQzwy-B_dsFT3t8M72pX7ukeJplA4_cu1SBjxyd-J1yu18kbgF37bqN7quaOjU7KuVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLtxzglmriJ4Roag7WkIT0CUY7vEErQ1vO-j3gUIt8e1hAky9qK5Z1FRrwwCqSaSZ6N1xegDKUtPNL3J60l2NeqJwnPcuMdqdZdWan52vsBio4smer-hddoytH3s3CgB2f3oxgWWpcrMrpt-tD5BTks22uKIZgnDdYiaiILWVPk43Gp3BaWFsyowDHSALUUvPa3lxkk7NQb5fg3UJI5zzyf0ryWuU__dWDHILbBT_zhFckx8E6zf0Av4jlKzdpbosF0V1jMB5tBfLaaB5VqVkKu7p0ykOWF_wn8HW7WEYYw2mUBhxKQbD8sd_GwaEgoWDd_XAWnD3NLMcr3U1iMpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utcpcekwxmk0taPpbUSmAxqBLToPsiNZ1RK_nLrZ7rffmCBJSth9QqU9T0OsPckkngFV-5xff3ss27Bg2GhLGzskWqDSPO-dxuTqJW6ROWZENOR_ZQTnFcW4S-8LTBSYtiG4XIP-xzT2Y2WZD6FagWptZto7X-KPlQ2wNBXz8ouu10Dy9BNd3Hap6zmXUuW3DbwDYFLQ3LY0RlsC5Pt2HDEVAVab7-1MNn1t2Z_uWlf-xIdGaZ1hc2qLZv7It1gIeOdLXOHyu_AQrlO7vxvldnOaMxz7QyYB22VRLwtNVlSyjgGcf2Qg1y0fm4fZ8NVgL6FYFyK3CyMH_xCZY8zibA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p6wNlH5CMrUTb2mRaMhUYK5pGHPeHN31zfk1ufHxnE-WtMYHqKgAnoTOhxyGTjv2i87E6Ogzp5qRAwh_Dgi0YV8Cnr1gB3ZNizaexjdzxHAEgrb4ue1zcPqN6g2Y6HrLrQDb0tzMN_FPvobcpo3ytT5BnqpWieccrS9qYwICi0m26eLH7hfASYuXBP1WPAZqFULtS0oh-OtHWsMT3iHr0KfexQVSvjK7CXrVYZyuQtrnGz3HjGHRVwVhIRbRDH6_mmxQHlwmYPYVU9oQTBgqCiCJsAxrKF-ys70STY-oE2lzYwqUqXFNcwBnXooC0gjPOzod83Nv3jrYDneml2IvODE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p6wNlH5CMrUTb2mRaMhUYK5pGHPeHN31zfk1ufHxnE-WtMYHqKgAnoTOhxyGTjv2i87E6Ogzp5qRAwh_Dgi0YV8Cnr1gB3ZNizaexjdzxHAEgrb4ue1zcPqN6g2Y6HrLrQDb0tzMN_FPvobcpo3ytT5BnqpWieccrS9qYwICi0m26eLH7hfASYuXBP1WPAZqFULtS0oh-OtHWsMT3iHr0KfexQVSvjK7CXrVYZyuQtrnGz3HjGHRVwVhIRbRDH6_mmxQHlwmYPYVU9oQTBgqCiCJsAxrKF-ys70STY-oE2lzYwqUqXFNcwBnXooC0gjPOzod83Nv3jrYDneml2IvODE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=VZnllIuhEfkChfdbvCvBkoii4e_2jZ3v71-xKERpwUHHPjRIFrqs_DPAFEqZVF9xZxKtefV3Jm0WzfIopcc6RZmK05VzRJDigMaF76qsNXd3nadUmWv10rhWBb1NV9I5ST7mg8XrGW9vw7PB6muoO8nAIURdvxCZAwl68y29GBmMeytZxOS9mLVBtQ8jOu5yBCeYCQbRuStgIl1XhM48xVKTZOFVjpVAFHv7kuuLRHjnCA-jpk--sbyWRBMGYRky6RlxmP9go2oHybbA3OY3kV91JCkT2cjxSrREcY2-HxssTNqLeagPcP-_c-0fEDCL2k415MTSRz79gFCTexY4fmOhD0BBxQoVi3Dfk2t2AV8Je1y73QUWDkwXbA-NjThGA-nQtGLB0gJ_N-AZvrOpzi4wFgkZUgs5_Jx0v_57npQhaeKo26lSnZI5_xLCH4JBxrVJ7JwbRu5RPNwle47wbx5Fv9mlITh7tFqW7BrY_gMy8f0eHAY0VxdP-yVa-_Ni2i2YPMTN-_dZQIk2aVFKcPHDgbedfGg4EoMy9frvuQr6K8uazWriLVMQ2DA75PcgTzA4O33xYdH-PuI7NeP57P8H7rMihASjnAYF0AcPuMnKAmaonSPvQZ4FunGd-iI8kdgAkW6mxD9b12ov1Rxk3jLHOh-WkBOdyulAD9hUul4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=VZnllIuhEfkChfdbvCvBkoii4e_2jZ3v71-xKERpwUHHPjRIFrqs_DPAFEqZVF9xZxKtefV3Jm0WzfIopcc6RZmK05VzRJDigMaF76qsNXd3nadUmWv10rhWBb1NV9I5ST7mg8XrGW9vw7PB6muoO8nAIURdvxCZAwl68y29GBmMeytZxOS9mLVBtQ8jOu5yBCeYCQbRuStgIl1XhM48xVKTZOFVjpVAFHv7kuuLRHjnCA-jpk--sbyWRBMGYRky6RlxmP9go2oHybbA3OY3kV91JCkT2cjxSrREcY2-HxssTNqLeagPcP-_c-0fEDCL2k415MTSRz79gFCTexY4fmOhD0BBxQoVi3Dfk2t2AV8Je1y73QUWDkwXbA-NjThGA-nQtGLB0gJ_N-AZvrOpzi4wFgkZUgs5_Jx0v_57npQhaeKo26lSnZI5_xLCH4JBxrVJ7JwbRu5RPNwle47wbx5Fv9mlITh7tFqW7BrY_gMy8f0eHAY0VxdP-yVa-_Ni2i2YPMTN-_dZQIk2aVFKcPHDgbedfGg4EoMy9frvuQr6K8uazWriLVMQ2DA75PcgTzA4O33xYdH-PuI7NeP57P8H7rMihASjnAYF0AcPuMnKAmaonSPvQZ4FunGd-iI8kdgAkW6mxD9b12ov1Rxk3jLHOh-WkBOdyulAD9hUul4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft5xrTKxutIlXs8Th2H7IHXON_V0knLay2panwF_k1Ao67egV9GHURCNNvEhtaiLti_n7a9ALiT6bZOuXdiM8klkiSK5AVX-YkBu67xV_p6v51IF-oXq8hOYN2ZTEzr_rF1iHZvToCzp7ov_vweeuBKrYjeC1eqmfnn3dUljX03LrI2gUwXw5XzHGijOT_hc0CQYtMpoETFB94KtG61ckJvPvbh_0vPcsUPj7pSYSqQHw7PLsHih4zl2faQZLtzEOCI5FhsoTp1dVn1DAVezUicXZPiT6mRu6aQjE_coIHrknAS4vwQnJlQuOsFg51CPVWtXIDhrQifoLfMZGjaBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
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
