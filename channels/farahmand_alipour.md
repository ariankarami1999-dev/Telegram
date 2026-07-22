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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IFPpLYLD6EYUN64DvswImvVuhq91JoClI4-zw8rXJL3hvZbiuuRpfrYhBkOcxG2gYwl_ZU98LSTH7aRgDZHGqRxss0axx1fOPPFkc5dDJmB6PDsXEypN8ZtjI06GRrYxyLmJJxUIEI79rCcF-W-rT-Ub-FVCMMUtfjn1pYy-LCkqST4dgCam6bchoovX97ste-e1CO_UAeXXH0X8YAZ0v3E5Nj2YssQ9_C0pyFGkFnXgbwcaoEfGnQH2LFzdZAeNqpyeBDd66oFW2rD01tkdAGX8isYX46qrKh-fZwxQH4CWyT9dCfgMQm96rCDmCyhJ6otkrwAYIvzRNhX_mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=uxSzPGWeV031CsAcPgsdHDvB5_YwRILjEvSOTeMSI3HRc-H1eLmnsNfDXhYK0vqOgQQBJHrEoj7dtX5TnDRSaSJFQwV3coa_Il_qTDhyS7vQKMfR1vhwuVV3VmQFNYo4bxYAAUXapOvkeEOXBZkcO4KIDxSTjApjbBkA5fRcLHXxDas3QmRs-nmm-Z5JH_6mX5KWXtJmY9lfDyTacsBoyc68UOMlYAQGca7wGINxQHDiNEG8hK8zXAxoCDPbuTv-eEBg-nx6SQSLCaqGi-l0jMlDx5l6KpANu5pNCt3O1nx8hhp-vQUy76CEyucZ8YHId6OsX1Fq381kjfAY0zt2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=uxSzPGWeV031CsAcPgsdHDvB5_YwRILjEvSOTeMSI3HRc-H1eLmnsNfDXhYK0vqOgQQBJHrEoj7dtX5TnDRSaSJFQwV3coa_Il_qTDhyS7vQKMfR1vhwuVV3VmQFNYo4bxYAAUXapOvkeEOXBZkcO4KIDxSTjApjbBkA5fRcLHXxDas3QmRs-nmm-Z5JH_6mX5KWXtJmY9lfDyTacsBoyc68UOMlYAQGca7wGINxQHDiNEG8hK8zXAxoCDPbuTv-eEBg-nx6SQSLCaqGi-l0jMlDx5l6KpANu5pNCt3O1nx8hhp-vQUy76CEyucZ8YHId6OsX1Fq381kjfAY0zt2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlcX-0ElyrBvzU7DZEGouNRKQ3p_YT_djnAuLQkLBBAhuE8kXNI3J_cL69VdeMcHp5a6Dc05Vm0P57wvlQGYy35Al8eWDCLyq7aQzUleKHLNda4lJZ74-wOsmyucUihgRVmWIJUyEQuB7YDb7MUNHlu1UxlFiGuZJAbfww1VX_SyFnD4skVpeboIE60tvljbZcmDRe9TspHAoW6v1iG9dhjPfBu5C76ZevInDudjdA2RmUVQ0RQpKmj9IPc2yWKj2-99dw38TnhrZgVRHnSZIPOgtG4bT8q_PKltXx_5xYw4XBJpj4OzxIZIWrCTqQrgk94yZjfA8wdqfh7BhcUUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l632PjQcyrmR8xEGrMtGBGUYL6OoxWu3neeFiWXDK1LJS9X45xDbusV5zae0dFx9CCTgXzMUtPOKrycuDIvuEg5k3vBZe1DhVga8rAF840LrzgZe-ktgyEQPyjaqlkG1sHUlP3LQANoFyxmq30SjSSqCMEr_Ctgph9te8tlUfyyslodb8yJVm7FT07tC_L51ujIZBaLdWqtGVghH2ZofVZEbchWXooBKf3oS_PbXF4P8dew_XRJXPCwDSEW1pH3t54b9ml_7800uDfiUiK2nNMvTxIvOEoAibmFHUJ4IhG_e-2xLsUKjzp90EPRuWIjWOB_XfyM1xDEEGPDEmcARTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=nNURiISPyFRx0stuZpzMLEN7jv6P6YxtTN8lwADjO2o5hVTuSEIOd3FWNLKuFO_Uz_VIqqkuZHR6fVbKfcm8za_IaWdA1iSI_w9oDcNw2DWtrRM7cBz1GULcRIz9T9ESSseZLoHoNYpcVgUzFME1eGuXkS1met9ES6axTwZu3kxRMiTZmtVSzvVJrgJkz-kP1W_-GZZpFcjT3iZG9Y6v5eSTbJxTX8iDdXY4uap2Rpk2dOTDHiJitOS7RhCxM9VefuO9B46Pt5uwknhVq25RvoBS_8TCSDnFiOm54iIA0E3IRIy1UUxXEp7m6_JWr4O9j6sOMvDMtqhZlvmviE7xOCOGUjBHVIG_bnYot41emD5LHaiZYe8ROxvz7wgCA1svudfhUFXTw7Eb823DC1OPUkigjoKIzjxQKRw2ARiAgBzxSwn-JrOweoVHg1vM1BZPBRg7XRydozuqwF43b_7yEhPCD1fQutoOi6dV0pluYm7GgXaGkAHcO1RVEuXE0KcsMbzLYrl1BuBEMXJ6uw9f-LzheMGcComiEe2CHkSPfTMKY3xwdIMIuRoT30lVhFPqhKNIx1yyspRYrt45eIqTGTNE2sregWrWmHHNHZUHwBTvDy49_EyFGaCAACOo5g1FqhzwUWTrr7cpC0kv6gorZMZiyoELP8mm9OYm4-HA5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=nNURiISPyFRx0stuZpzMLEN7jv6P6YxtTN8lwADjO2o5hVTuSEIOd3FWNLKuFO_Uz_VIqqkuZHR6fVbKfcm8za_IaWdA1iSI_w9oDcNw2DWtrRM7cBz1GULcRIz9T9ESSseZLoHoNYpcVgUzFME1eGuXkS1met9ES6axTwZu3kxRMiTZmtVSzvVJrgJkz-kP1W_-GZZpFcjT3iZG9Y6v5eSTbJxTX8iDdXY4uap2Rpk2dOTDHiJitOS7RhCxM9VefuO9B46Pt5uwknhVq25RvoBS_8TCSDnFiOm54iIA0E3IRIy1UUxXEp7m6_JWr4O9j6sOMvDMtqhZlvmviE7xOCOGUjBHVIG_bnYot41emD5LHaiZYe8ROxvz7wgCA1svudfhUFXTw7Eb823DC1OPUkigjoKIzjxQKRw2ARiAgBzxSwn-JrOweoVHg1vM1BZPBRg7XRydozuqwF43b_7yEhPCD1fQutoOi6dV0pluYm7GgXaGkAHcO1RVEuXE0KcsMbzLYrl1BuBEMXJ6uw9f-LzheMGcComiEe2CHkSPfTMKY3xwdIMIuRoT30lVhFPqhKNIx1yyspRYrt45eIqTGTNE2sregWrWmHHNHZUHwBTvDy49_EyFGaCAACOo5g1FqhzwUWTrr7cpC0kv6gorZMZiyoELP8mm9OYm4-HA5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjchkzEUXXtGSIcDeBLhF0JInluSsEToP2FplK4NjgAhyWoGrUmIZ5RQl4psyz1DNlfQkzEEGQjBWr0gwcbFq9jFpLggljG7QfuJifLvFAnhXKaJwl7fKbaKQuflIjVH_bEqt07bFrYWrymG_YurM0EFy6Z_UTL2JLdhioIxGMLPrL6JSnN8UaU7_Bj-ZX35CI0rNWNdeUKBVsuJaLNhaZGJCzO1watMebn1TpZEwGHM32qPr_u3vxD7WujUVGTnog5UlrnAlDNfGBzVE1IuoBaEkkM5MeHowpqSoCBVgSxr8oMBg-Hdx6fyvGfeDcPKWkCk-37C9PyGNIOZhqBR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enryAPfZ9x2MxUz1bCqWHGN04Fz5U0eqMWyaRV5raz6RwuR-_Wokzdeh7yncA_eFQq3iDUFnmnwIV48QZWyy4HyMLxol_BZfB5Psib4euSQfY27xeSK3Z2LzgaJnzp9Uz8YBKXS7xo-rVpOrahIfXYAzVPCVqP5t-S7KQw0kzBNpez-cRU9Hp1meLmvZ-DjtYgkca_eeNnshhynBZDuEKaEoMyYox8xz16ZWUr9pFBCRN0DTs7BFTgl3O8eBRiOllFqKuSlsxK9N2vxojsSdJEXPVHru8LeOFpP6gz3xiSZFulRNUrzXa83TwocyG2FmOw5ZG5esg6dK66OG_3xhPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjuOtMqGOb1AYAPuiOUC_yH9n1SatrJrPEhEAMTZ9mbsJkNbR8EfFL4rYXeKOjTC8JteULJZ07qCx-Vrwyf98rY8Iut0nK1gEPartZ7zvCfSXB0ougojP3ZKFhkmROu48lIPWswK10qMMJIwAFzUrAL1X2EnLUZzWE3VIdP4risrib5YTuSnObeoBV--VlxGME8GQAmyRnylyXqwiyDcHqn53Lshe2bam4qz85KtQfM0t8lq7sFWYDN2wNW2-0Xk0OZOOwK6C6iVhIqOxfqbLaP2TEpS1KJSCYP8agvxHvSTCwFHSI58V32r84gvy-DCa3wTCGZpfVuGvPj_sHltjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK1u0ruA10eK2Pd0naiilIRNz6VgTV5zKYn12OKlbFtiy1EBGLnDP3_9cPj556gV8Nr1KPnHIZQ268AVf6EFu2zdXrNU4KdyYGi1cyCftXNMsoaBk_lhVkKaOPLDec6TDg0h2MBG4AWk9Fjble1XFDRHdm0Hz_BC9CB0eplvwx8Mmmn9GjElo1UVZwn18HCSveXkHxxY4hRj03AQh3Z3r2N9WZsaRKI5NR1wvRnSPkcx1pXiEWBsS426TKcNJN-Un50MrSM6twYvkSqBlxpvtcXkIyHE3IVamQxYU7uyOLa3aVBf26SPUN33mzlE5Yy04V2sx5WO7EC-AkwqyRGAUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=h90k9yNY4-6yYWf2_hw8oIVepipV2Uf5BVVIkCPVfg34aJm7tKxnjzERHQTYRnDB1OsCB8dE3IBTR7rzxHmG8KtinPghRKx6g96c14-dfNEiu6KwIZojAnT4aGvG3SfI1Zit2zwL-S8KBvZ22X9N2a0aCvIHxgXraSj7qkD7xojEUoZnSF-fvcBLZvDA8Vchm8dndHsnYd7hG2Dh_l6fzfjvQ_8uID0A7QZNBimOl-VtZzybCW9GwYKE2Hjho8jxqVpkAwwh90UEYPZj0RYbym5Mictj6va-lp73sIbct0bqhf2iE3tBfOKmZcTKqApw-47j63tJKGUmwD6hwesjIEplPLV_v_P8rT2Zli7Gr-1NZ_d3UUgCO7HW0qk89LpimdEt2RFBpIuEwJBWmFrE-bHQ1c1HTiSelJd3dZOzRd9YgReS0FlnMHtKUdsvPX4kwWHstGAOBN-CnHbYotllNtrz0GVjGotuCc7pAvkzgWKHH8oQqtfqV2rqDy0M32ouma5pfx-kakgbtco1U6GO28CvjXMmcU50nlBZvC3o1w9GxlGjI9PaihYyVCZWb_4UUJJZu_u6MeeOrPoBeua6vF5_mQlLvJf2HJnjh8uPxEUe21f8-QU8XApT5X3qlsIgtWukkAjWEkGoAMaHx9KGV7xJzuqGyi_Oe3PuqjLM2TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=h90k9yNY4-6yYWf2_hw8oIVepipV2Uf5BVVIkCPVfg34aJm7tKxnjzERHQTYRnDB1OsCB8dE3IBTR7rzxHmG8KtinPghRKx6g96c14-dfNEiu6KwIZojAnT4aGvG3SfI1Zit2zwL-S8KBvZ22X9N2a0aCvIHxgXraSj7qkD7xojEUoZnSF-fvcBLZvDA8Vchm8dndHsnYd7hG2Dh_l6fzfjvQ_8uID0A7QZNBimOl-VtZzybCW9GwYKE2Hjho8jxqVpkAwwh90UEYPZj0RYbym5Mictj6va-lp73sIbct0bqhf2iE3tBfOKmZcTKqApw-47j63tJKGUmwD6hwesjIEplPLV_v_P8rT2Zli7Gr-1NZ_d3UUgCO7HW0qk89LpimdEt2RFBpIuEwJBWmFrE-bHQ1c1HTiSelJd3dZOzRd9YgReS0FlnMHtKUdsvPX4kwWHstGAOBN-CnHbYotllNtrz0GVjGotuCc7pAvkzgWKHH8oQqtfqV2rqDy0M32ouma5pfx-kakgbtco1U6GO28CvjXMmcU50nlBZvC3o1w9GxlGjI9PaihYyVCZWb_4UUJJZu_u6MeeOrPoBeua6vF5_mQlLvJf2HJnjh8uPxEUe21f8-QU8XApT5X3qlsIgtWukkAjWEkGoAMaHx9KGV7xJzuqGyi_Oe3PuqjLM2TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=hwEC8ZYtfzJDopUpGLoKfc7m8_UKdlmjcogzCqgFBmoiEJZIRP11QOVXO3dlIZ05NyV2h8UihAT3RoKR0kjEYG25_IFHCQmWRTBbZYwD8UNPrgOIpunlZ8pGoAR0BKc6U5ROkriTVPSHMcEsvmMQ8caS0Pprf82bgJUIdCa9NQiJLLWHFHb8QdMBPUNsmaLVBP3BqIXjFB5VWIwHKEfVUWQOxEKF2n57w5yezdocpQHNmHCb253VaxpSIBoKH88V7Ull9M15SptbepSpGXJ0yfP6sMu_pCwpoP2tqzvIVJ1R9Z-jNpnoY89I0a_PdUexEgehnZ5vFk5j-akohj3RGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=hwEC8ZYtfzJDopUpGLoKfc7m8_UKdlmjcogzCqgFBmoiEJZIRP11QOVXO3dlIZ05NyV2h8UihAT3RoKR0kjEYG25_IFHCQmWRTBbZYwD8UNPrgOIpunlZ8pGoAR0BKc6U5ROkriTVPSHMcEsvmMQ8caS0Pprf82bgJUIdCa9NQiJLLWHFHb8QdMBPUNsmaLVBP3BqIXjFB5VWIwHKEfVUWQOxEKF2n57w5yezdocpQHNmHCb253VaxpSIBoKH88V7Ull9M15SptbepSpGXJ0yfP6sMu_pCwpoP2tqzvIVJ1R9Z-jNpnoY89I0a_PdUexEgehnZ5vFk5j-akohj3RGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzTx08XIedQjkAhro_eBg4aWHMgz5B3eGYTQ-Zl7T0vAFxTVFFUiSgn0thdgLEG8mi3RRVmiNp132JHZr4X14wAH79klmX9SBUeypYNdkELHmtkkrDw1kYlQ7KXg3yQCQjWOwNrRP1MDMBDsCVp34fgDdaRcSyeWhKbTwh6xTNhHXXO_k6PfAGk3dKoKfMvVDVAPnlEOutHL4NnqR307-KgQg9AZRl1oH0FbyMMlJN58c_rfFhzY4jWCr9twMS2CVmmMFJ0UlXkiknGbHH21ZrXwubZ-goYn56dJma9NBXlLJUm7--AGp5a5Y6eaHlipz0sRmWa411gluCU0LEPGig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZKQlKhj_d8G4d5c1KCowspmc2BPWu8ink79fqIV1mj5jzhES6WdzVQAEPagnnS46AOZ-Wq1stBcCNW5FKJWcGWHB030rckPIsu5rBZZvYogPpMIxiBwOYZso9bNbMxzeNf373nWPLHl7Fa5nI9v5Qf4EQEb7dXdcunLopaNJgg3pW9KMXTv76TAkeZvr9bWkgXfLv6s_NXoVLlUXBXjisikiXpmxTeqNBeSZA19pz9Hl6xtZBAZQWWPy6OUdJYt_lqQAxEkm22KXVZDx2SIj0OTGStOppsSFg4K6YB1j1AXE7aFI2e6ZZ9S-5nTWo4N0d0HYGNZ2GsX0AFNQNJkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyNVzoGHfL5orwVAVq3ygc3833M6o5tmYEr4_LNoYBiOKKUVxMEEIKj_CZGuTGpIyoYKs7sTp01T30rWW8r9BsToBGIXl0Kr91Ku8_klA-YqeO4n3pawZNan-yXRXfGgxpz5SKyoCTDUzL-4Zs9JQ3vpWMM1JO56WxlukpyfBjl9Z2TLtUukoqs9HGZ4N80RYqWwFqfelecK3UxH8egfm5-d2x4mktZapjWNMHrCCT0V0C6wTF-aVgFcjMk-aoWhwyuBrRq89exH7QK4vB_L6BTH8Zy63pmduYRDM7FVjun7O0XWcUhRXE3bgsZCln5GxefubFSAzolswqWDGIgiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yo00ij_6LTPI63TM8dqFcNFEsUMEoiFd8hB2BFcdtzDH41H5Mzvi26lWxvKd_tODxtkKqT_NYRyYbGReWbel8ffxtzE0F2v3P7PEauFlQvKJvsekDsvfq2Ast0Qdo8O5lDA7-lJoO1kFhbMBS7LTBEGFUDzVC1CjwYz0-htfT2DlPKpRZ1v-w_PnbAGa7RVZInWYuLWBOl-xgu8aJSnp4Ip97NovI2w2bZp72u9MRtoBvNTH4Vv2l3xddSCpwpqWcG4SP8vT0eD4v5o_k1T4SBPoPju6Y_gu8pyugMNqtCoWkMeCygzsezQ7EdTQ7eAhQgB7auxe7pZsGkOzAMGp_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaZwMUzPMHTNLl9C44OCjJzgIXZO4-TAqEFsnpn3ChgfwvX4isYNQ4YVik6xuKxN21pavgCanl1cqluYEPbtkOKqm_dAT5Gb0U4cQnkGxlSn-Gt5R8_HDkMLGAlO5K1N6M6sJWDBjOTvn_gap2_AekmqDIfxb0NvbjiLHm2ISvDLw-PAAi0s340jX9U5Z4mLu0x-PYnUfUp8cbbJj73DZoGl6SvLptUarw9jTwOetbOvHA7yqn94mE2kze7RwICJnbCL7exAnQjzdgdnBEyL0Ht5D3dYCap_T3T-Eg6UbyXHDrnuccf_UAsM4waqDQ2F7_afQ2QoHUS7RYdE89Z26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqPvKHjsON5i2Q1-DVeZyBDKUeqEMMEziMD0yNPNWJcYVyXwfe5pbtkyHpQKQARri5EwfczDjRQCetp16wPSzpaKBXfsOTGSR6maa3ELqtWBdTVSGFOsbeS0MiNpx-_q9xbwDUxzEXyzz-6S1_KsEcpHbkGWmKIP3Ya_TTLYAAqRp7Agdfl1Paxi5_Ax1dTCH7Z1g7qZKK_JThk5lsEK6FZCFbcq95OPY7P_WEB1hopg6lfROMOvm6FeF6B0eE32CqsIyNEyl8YyF6a8LD-TvsTo14luJGjgUY2GF8MuwzKfeE3MHd6xCFlt9Hq4Lwm-AwrCv1E-DuseeDIgAXS_8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOCwa-Ph10SidsHT360i4TvJTHZPWhQU-_IQNCs8ysJXtYlmiPdolTzccbpGnTz5Y8v9Eh7IGbTwAw_QWGHThShHlgYEheUulgWJuPgfuKgNzmhEXK7_2xIfnNzkcPFEWFj4MRxJjyfzAWiZbplkknAXEFjbjKyQVvl_LSDBcGrYGGKAqOCBWmAd4xQ6FjHnSSm93sXCl1diKsQ_yESlY2CL30tzTmM4Q6VecpPU_Z2Uamy3aTSL15Yi-ALg3Z13yX-2_9cgX-t1zRPFzTvze62Zfj7_6_-v1SYOYY8FMZG0YEA21Gbr9SiGwee9Fj2jVfosf8Ip7bVCgs_KDhmMLQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=pSQ8VxNqIH--4GEZr551KD902fjsVOZmzkSuQ2J12aSwnmm6Mh4bQfmeZTxcHJ_yP-xvqLwMFL-zVokNvaNq_-2JCW8WwaA96PmD6KymxXVgWSwmuduKBzMzhh9iOr049IO91ZZZGgFDdU5a0Toh2ZrGCpll9upCvJMPUfPGTDH4wc3SbFylzD0omSYHC2H9orL1Xhqy3O9OuHB8szPOfqAQCklzKy_fDgFsjxDiYtC7J7uwj6TamMsrDKi080heCf_WbtxlHqL2iyqY1yOTeFXfjsSF_tMzoMcpUMFVPJ2QlQjrXoyM8-cqjkFI0l6nWnzTIg42z0EqOeotxPogoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=pSQ8VxNqIH--4GEZr551KD902fjsVOZmzkSuQ2J12aSwnmm6Mh4bQfmeZTxcHJ_yP-xvqLwMFL-zVokNvaNq_-2JCW8WwaA96PmD6KymxXVgWSwmuduKBzMzhh9iOr049IO91ZZZGgFDdU5a0Toh2ZrGCpll9upCvJMPUfPGTDH4wc3SbFylzD0omSYHC2H9orL1Xhqy3O9OuHB8szPOfqAQCklzKy_fDgFsjxDiYtC7J7uwj6TamMsrDKi080heCf_WbtxlHqL2iyqY1yOTeFXfjsSF_tMzoMcpUMFVPJ2QlQjrXoyM8-cqjkFI0l6nWnzTIg42z0EqOeotxPogoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l38If7zPlgf66mZpeUpZ67y1dBTSPNj0Z-Z6pbTXodXV7Z40A2JGyOQ5EUonJXCizI8gVhGqw5sS3WkneIE1rHGD82TlzuHT1laKogkLbr7A7wTWqLbW6LziFoc6GJCVsVQqK_aYmlZSOPhe0yjn02pTNGEZHpV_p5zsteFATJwzHd-4GiQarBj0UCISjpnCjYZPEa01X_5yNS9gKW2bgFm-lDkiDRKyUHtMK8S5Yc2QmtswwmLBlnnYa7h0-5FqDUlu6nDhXe9JPXXYJiSWjlUVHsfZsNxt1_bB0GmQHrqmVdLtVOxbqCgbhhqSEyMREXhbMA4Qlf8_aaKNX-CxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=NHr-U98ZGaZRqZO0jpqQLuwgnjUVf9j0cfJ0tiL_fPWlf9a9V86Hb3GFzVt5d_dm36gv75DECsU0mEEoesjtqwuyhb8L3lf598JgPw2tRSaf_VALNSWGKDiWiYe6IpkpC6syN0bwUXMApALOr8YAxGb8qfioj7vKtkKfIOonikCOMWZ_HovgE4X4UbVKt6qUriBU2II4ZWSo59oRF3fFrNEK634IXcrj4lDFYoiliUOeBFdTn5pJyYTRsccs6vUp8CO07s0s-lwCdKLoJlMtIflH2pKoM0TZmNwvFjJqYu3KlLHwfTmjs7XDolbahKjVr4Tdb9HieBVinn4pxKAlrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=NHr-U98ZGaZRqZO0jpqQLuwgnjUVf9j0cfJ0tiL_fPWlf9a9V86Hb3GFzVt5d_dm36gv75DECsU0mEEoesjtqwuyhb8L3lf598JgPw2tRSaf_VALNSWGKDiWiYe6IpkpC6syN0bwUXMApALOr8YAxGb8qfioj7vKtkKfIOonikCOMWZ_HovgE4X4UbVKt6qUriBU2II4ZWSo59oRF3fFrNEK634IXcrj4lDFYoiliUOeBFdTn5pJyYTRsccs6vUp8CO07s0s-lwCdKLoJlMtIflH2pKoM0TZmNwvFjJqYu3KlLHwfTmjs7XDolbahKjVr4Tdb9HieBVinn4pxKAlrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBj5DQm4_5-r_HkKW-GkSwlUcdrWl5oDILSOtycuyqpwCo9VrfddKQNU14aoK9TJKX3Qr8Rawqr32uc4d2tmOM0I9gja1KZybLQQXxwkQ4De6zYUhdcU1Ov0S6rkQjQVxwoBCIl7N_MFAM0ogU_UQr6qsNYAECqxKXlo0oCERy_ZLIcAmEFCMqZCIqJij29dwr2478GIiIMLkmGQ732NJlIjMwr1dA_u_WlmJfVVuUVl3B4mApOvgoXOEpxhJFSwvveVg4eNE9GI-ziInrzc8UZu49fx9ow4jVlSvZ0EIZQh4gfesapfonvGQUaDnDnrCnBFdIbESvlwPdEoAGr-XA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFPl052NQXuesdF8CkcEYIBxlzQrxHz7h6ew31z4tGaMBauhb2AdT2Ab3dbdIEcBWgiQp7Jpfvj2d3ryzuI4X17-gSXsitDWTT6CtRNiE1vGvcxuFMfedxrygT5VI1MFaLO_u1nVnj2aXroBAdRFw0xhy6t1oQQf_fkg4Kes1ELIEfaJjAHw-wOhNcZd78vN6gT0dXLy4JKt_EDhwhW28PsnjgRheQsiC4AMAbx4XTd83hxwC4Q1i89Jxe_JT-D8Ai5a_9JuS9lTUU6jNJYGBexVpTNTVdFWC6TU13FODqp6pYeRfRC64sHxKqsS3JqMMIZlady41Hiac6Pbonc5pMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFPl052NQXuesdF8CkcEYIBxlzQrxHz7h6ew31z4tGaMBauhb2AdT2Ab3dbdIEcBWgiQp7Jpfvj2d3ryzuI4X17-gSXsitDWTT6CtRNiE1vGvcxuFMfedxrygT5VI1MFaLO_u1nVnj2aXroBAdRFw0xhy6t1oQQf_fkg4Kes1ELIEfaJjAHw-wOhNcZd78vN6gT0dXLy4JKt_EDhwhW28PsnjgRheQsiC4AMAbx4XTd83hxwC4Q1i89Jxe_JT-D8Ai5a_9JuS9lTUU6jNJYGBexVpTNTVdFWC6TU13FODqp6pYeRfRC64sHxKqsS3JqMMIZlady41Hiac6Pbonc5pMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Kr7WnyVYk1oiG_5HlYySzD_orCo5QoywDUvjOTuPgsGVrx2HUdhuaP_YiNRXGOz0Y99Y48wMANsA50SXeWFSYRTGwC9oGpH6hYmAZdnmjF7qRFxQ9IdwlrT1BftffZUQQJVHxvIe9L_vHbhvR4VqYBWF3h8ljXUolHoZRrsn5tosiho60ZNzDJGOmuUjIKj8rSQlH4Obj4j8Ur2UdJhUgTJDQ3i1RHhRGoqO64kUvaLryB8W_0pGdtYSy5326EmE_hPBRMEMLPuQPfIyeLfn-NJp-wo02iR-EdFupousEUpg92vW6XVAr3Vrf6nL7y4oU2Kq8nAeVIakz0QKuEXHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Kr7WnyVYk1oiG_5HlYySzD_orCo5QoywDUvjOTuPgsGVrx2HUdhuaP_YiNRXGOz0Y99Y48wMANsA50SXeWFSYRTGwC9oGpH6hYmAZdnmjF7qRFxQ9IdwlrT1BftffZUQQJVHxvIe9L_vHbhvR4VqYBWF3h8ljXUolHoZRrsn5tosiho60ZNzDJGOmuUjIKj8rSQlH4Obj4j8Ur2UdJhUgTJDQ3i1RHhRGoqO64kUvaLryB8W_0pGdtYSy5326EmE_hPBRMEMLPuQPfIyeLfn-NJp-wo02iR-EdFupousEUpg92vW6XVAr3Vrf6nL7y4oU2Kq8nAeVIakz0QKuEXHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbSxSy7c7NUWyJrAd2y6kRjSF06zOq9SbEit9Jxbn6Ox2nYcXFchcRfn9OGTFFcPv8PEpavrifo_oeB0pD4sPyKEsCQZQthc6TnPIasVmCXxI7kZPtPgjm8_lTQnOLKmtQ-ivZi2qAfSTwRKgZ5qb0TaJQzAwQDTCE3SYeDb1Z4YHF6zJ_734ag2i4q-Q1OB9NRKO_ttV0WJdb3WvmF4lViV3wduT71Fu71EODT6ZB6y_8LpFQjio0DdMeGv09lTp6dPlu-P_m9ICrxEY8EBGTBFlrFMGQoxU5l9bTZW6bX73jXPG5ylPNocXVJax3BlakvHlGsVBgThMXzPjcvxg_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbSxSy7c7NUWyJrAd2y6kRjSF06zOq9SbEit9Jxbn6Ox2nYcXFchcRfn9OGTFFcPv8PEpavrifo_oeB0pD4sPyKEsCQZQthc6TnPIasVmCXxI7kZPtPgjm8_lTQnOLKmtQ-ivZi2qAfSTwRKgZ5qb0TaJQzAwQDTCE3SYeDb1Z4YHF6zJ_734ag2i4q-Q1OB9NRKO_ttV0WJdb3WvmF4lViV3wduT71Fu71EODT6ZB6y_8LpFQjio0DdMeGv09lTp6dPlu-P_m9ICrxEY8EBGTBFlrFMGQoxU5l9bTZW6bX73jXPG5ylPNocXVJax3BlakvHlGsVBgThMXzPjcvxg_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJgH3GrSm2jdzcUNeqBjfM1EutM3yM-MxsL1dhSjy_96A1r6zm4y-u4iWK_SV9mzDsSo-OIxkALra9glR2C-GsmbiKyxDFv-yr603x7F6hM_i6hU6qZUBtJ7eff-DOGvOUSWKZU61hzjDMb31Q_E7QmfkCobAPOXb2UVbcZ3phT3TdFRDjZLLfWPYkHLN3VbJiCtnLtvyer0YfZT6J3f5mPxT8S7z1tpItTxm-maPKSkmtzGllT5uLMPKv4ig07lxbfRBM8yLoICPYk5oYxK6EFrpkH78tAgOpFm96znzLLOivjpUnkgZo4hQ165vzg-PNjRaelzAM6h-HXSA-331A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eky1cpR1xLvXMb1YfM8hCPIvjoWXm6nhWtAJ4Q06NeWbBHin1j2YC_iFI14sj5Jb4S5asabg5CG1wez0QUOuEPVRQQzz1M_Dpl1vfVtWJiJARLg1goX5r_rA3OILV4QM3qytEo-S1TdCKOLjXEWJ5oHryLMM6Uq3WlelzO0Kw6njt7BieCKuY2ubCjceZex1kN8YIMO3ivFykEcIKUfWLq0YJ2HPhOqZx4AVxrL2mooeO8uvH2Z4FL0_jbyf0vddlPfPVPfAoLiIl2NebqKUvk23WOFP8T64xoHZnACd-89qwWhm7g-Bj8kfdwzKdlaNwTujqwgOUPh_UUaeSjUM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbqJF84AQHRTwokU4NXs-toMpF3nm27JjBV2RqV_4r1RgB1ySQ2lXxII3iGUke8SxoKmSZVUWyzue2rbJPsxy3w6pwua8diDrBsnXikn7B-o57iBhYySQ5WHoxLHpx9-CcngYgOGXP-IRhDIwnq_t38RK-pmtpV2uLENDDfW7L2noKGKxVP0krH_EaapfxfLOYRv_3LdtXP17IBAMP-_6t-7hlqZ8tsFewHd9sZVEdbRyDtJw-gEyZ3u8Uvta2pBN4wjy64D6B_h4Tn-JgWjTeugwOKwmVzy_ZFwKFSjv5loclj0cO2FtKUv9lrJnPRuavyRtNadsxdi8eQ5qi61Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gobmQCRUwYxG5NMTXrZShVgOs7eaT9E7g9pZjbgv6vpJ0BEFod6kOAQbFLCqAq6NPOr5Uiryfyr2yi_Lz2x9pISr9lZFHE6tL93RW7RrY5c2aPpfwLRsTUR-RVwdL1gKZQBTQEqonAXsCaoTyF7NrARXVZ8oEjAFcIx4Xk1oEXQVmmgUPVidBU90wtkVLRZPAGjQjh8NK1jFCl9iZOmvPdZJL9enqEl8RYHJnnxuQmO8_nUBcnl3uaYmB3wIgoIoqoCMI8O7e6BPjGxxFh67kt6rf3VQkGOaVf5UAWNfNtuFOujJscSTqXpYIiEDwH0mcrrkRoqcrsPjcFOZt7MErg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oymPDzfrta0jXgVOVSSBgaaOr-A9w5KdBA0y-nkkx5iyKFb46nJtWIpER5ix77M7k0cO5eSjwbtwJLilpwZIzffxHHsURxNYH_kbmpHjUZy4cyehK_kRAyWs_OI8gLcNShGMu029f-Qd0cHLQfYASTJazX4OTb80diAs3bAfZthm2xjTM2SKfgW4lMV61DCGk6__TZQvWoK0Dwe8aFDCikWM0PP04STLceLzbLPFOKJAxR59UXmyRs1NG7h36Qh5buqdpY5CTCBDfrA3ag6Tzq-8mJg9k3hgiutWE1uDH3QERoYbPynOPbOQe1PUO_l6pAS5fTZoJ1ciizxneSY4OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYSUebdcZ_i6awqYXjDgqpxBnrSF0A-KS1x8BPgatedKvdFnpcA7SJTnecM_rH5ZPZ3Tsg6528Trl6tNJG57GEW1H-tWpcIaNf68mYvcgXrgpgxFn4E0ffHDjbxsAPBmFNQ0ScZB9LKFWneHkC8tfaDp3yWKyIOthx3oictWTZtoH6ZugWHka6YnQwWYsSEDeHp0uHqCvuT1V5w8JEaRqnr6L5rEKnP4ug2Of3T_wUIErDa2PQsKjgmzpvOpcFo8oBCddBTVNGD7GtmFzUJBSoZ2G3gzkfb30CZfItQ366pFOs1d3_qTT3P_MvnqiFwPV4P6oPVOrwd0NJ-YuergKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjOF9X2J_XKklOdVinws-HAuR-Ekcv2mnbLmdUAahJ_xt48JUmYGAPWnBiW0PTXpv4-C4bUKel8mqV3ExpLucpa5ZARB_1AgL1UK8Tx_-e6mYFaaZK_MHYzlmzRwkGwF7WPLxesL2Utb3RT6ah0aaTwtQf-DrknCtwZtscWbROxf0QcDs2rM643M-DPl_d_L55o06EEjLXCG2FCxUBn8OCVc_94WGfgjfVCkMWtTlUNWgJrjltR9uvdB1REw8ltbgVc7lEsPoEgvDcnCTBK95k0jmLc3P7TUxvOqzkG2Raiw2qCmwCHyVvooksGpab8rTxrZ8ey34B0NbH6xWu_6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTgAWcZd65wFdKqkh6_91iT6AGiKQHQzZCT0PKBr4ibMGEhRGxHoEYSVdDy1je7cywtgUet7EitIQx_kjEbjit0KisvwmlRmX8G7JzFiK4SzgkQmbkVEOiPmgao6PdIo3hJhWsprEewwHfQPUJ93Pm7oNrNeTCd78nXAjk5nmzCLy0FADMn3KzZRxluY5SLetO7gg_ta68AJW-tgE5ukDZy6CU7syh0am7ydni9xsH_MyLLXMI_b7LSAFYgJ_TTKtERVEIaGZYcS-Ven1Bmy96U2XDaedKN6j00xtikrxfbs38pX54cKhRmA0RlpMEY6KIr6APxbBADmW_ryvsqE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0VcYs0VszxWQH1mKHxJQGD43Tr304ushXRHQ6qjlLGGzX2u1ASUu9sW1xash8qWAewRnIknLoMtu9TvwvdMg-FjbxBTRYMb57MCDtfgLYVfomh6k5gvldEc8OLsZNeVgndbznOALrGmOXiAVV3iGLbGGjZyxomvfvvqUGJuZf9fCAj1Xc8ol0MxVklF5cp429Dj_J64Qy005YVOreazBZ5b_Q1bKowqqpecbBS5ZMSRNH6WWwU62JR0j0JL6q6WTNfb-3ZJoexvSg4KOOJLRDpAuy5FKvD0uGtgawObGGn-tq0140ApiFzSawzAzPCTNBqUePkjm40JzunfzvpKJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy_rq7IdoTfbhVobd4sCAg7MnFENgetdDHRcwnJDX3wvbp7HyukWpUtuxsqm0p7VtMvXxSHoApVAOk46wf0JnW7Bq5oO2Pk6UKbrO480awA9X2uHP5zIzUsm8hCpuVbDsGv2s5hvTGbMm7HkCrlgfRXQJu5QZtdZHkrPv2olRGvJoH2JBqeMWFcDRz3e6kJ82PO9UzSKM9BfsiJX0gc3sawbdpv9Gs8miHWfr7V5UmxUUyV8iNXqp8SkeIWNV8rliX_4-ucwA77BNmIMpxx3NfTcvVOeLZircf4m8o5h8Iy95Sduf8RgOzROtRQnYa49K7nF7SCPIu9UwdCZi_5JSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B30VhuktRYqjpIQtbYPVNeDOp-XeS8DmKaXKTwmZOu0Db1iNlGSHedcrWt_K_8-0wFYXPlNofbn8y2JIMcdT9IxpLSL10LcDRrXZYYGvbWeQqfjrxc3hMbzpuazwKz0xnDTUwoqFKgNsCBy57TKpt8aQMy7O-jdcEjoygNQ0mgwWGq9DQ7NQXPzsGjiiEnJUYISoWOdriNuXTJosRWBf0bGkiLG70Mk6-TBSkwaY7ES4S8fa_HW4Q_uUiTk5UzGmB5VwXgI9kcl2jndzoJH9uom1imVnlDRvHELgLATUGlGDdeZAnwY8vPVcdODWrwCbsDg7gLop1vekz_ObEutfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amOIxzrhJKJHCGqfb2G8SaCeAhBOGGbjXBkFkvE05bD2QHAUNZiUF514mTmbqw50duyZimGAblzSKjrGlwr0tjHvD8pfRpHJnPBhXrb0EdpP-3O7Fa9dKQ4FGuXCid5UVesuG_MfTfK1Xobi_fHX1KcW1cnXqOiseQb6cPS88gBoY8nE1DAcGnq_DzNvz1RT-ZReJn6XHElfHTJgwuK95kCohjHFdj8IK_WbIdy9EiFNMy42MnkTtVF7SKJCNAYBK6aarWzCc2XpQhmbBNIOBcmj1sdPuAJ-b1-rmCkk609YHzzywlv0UIi2m1Tsrrsjs3OBV-CFUI-ygnlAHzMX5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBMjtMzN9wYkw522sjg2f9BU5KGqG9F64rK7Yhd2j_8zcID9hONqg2glTXH0Ar7DFYvv_jkhj8GDNUfBVWUalWt9UaOcnAu30Noi-1OUP-y0miiGNyweSBQiiOWBwLUZp6ysDAgQ13MijH_ugwJAJBcfb1xaEMuDwWndWy2XVW6QhPW21rcOLf5lYaqHtiKa5Eu3iNZtYHn9X5g-eyajyDQBNeT9KRjXp7Dg7Y4DLb5E4r7fzXwZNNgBxfndTvnr5yyRPdws9i9_WS-y8-7vtyGVrmOBRp6jTOZN6yAX1gnFamlkHzZ5i7O6aDxtZYQWsZQg44c_5sdexbTVkk0KNy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBMjtMzN9wYkw522sjg2f9BU5KGqG9F64rK7Yhd2j_8zcID9hONqg2glTXH0Ar7DFYvv_jkhj8GDNUfBVWUalWt9UaOcnAu30Noi-1OUP-y0miiGNyweSBQiiOWBwLUZp6ysDAgQ13MijH_ugwJAJBcfb1xaEMuDwWndWy2XVW6QhPW21rcOLf5lYaqHtiKa5Eu3iNZtYHn9X5g-eyajyDQBNeT9KRjXp7Dg7Y4DLb5E4r7fzXwZNNgBxfndTvnr5yyRPdws9i9_WS-y8-7vtyGVrmOBRp6jTOZN6yAX1gnFamlkHzZ5i7O6aDxtZYQWsZQg44c_5sdexbTVkk0KNy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=CRLv_J3UEo3pk3r8eqPJaxiPG9YO7pQmo4ubSVxVaqH9nzzdSHxhPAQrpkzrkSvqFvmpv1ivlAslMHPTH5WIdHoW6DZ2YDjE6DOVgE4FJuC7CBvICzcZc5mawt_opW55ohjDV6N-AbEc5nY7hNhIVudkBfyJdJ3duox1GyDZNRZlXl38dgB_VK7Lelw3qa8jqly-g3Bg-8i73DzW5LvR8xxxzzCN0DAOsUSoVVm2HCBSsEXgG2UmhNpHXqSpNop5d78Mm1PQwFiCk8jfUaT3TNPc59KsQXjLLp54bZRnWbNgGCRPblXKtliXyW2f1hw9ANuJniM1h55kbCDbc7AFyhkCnC2iYwuXfMcuou9bE7s50e0Joi8VfVpu0WMaOLfFxXwKa8pH81U4grRkXc7nwPtXH6t-t0kKga76zs9QOWGRA-wlA8wgJsfacKGZNPO1MLM_LQ_FPPuOZ9G8MkruU3pNUpnQKwa_5ezGjcLcTUNEgMVg3FB1WQqlHawfLu86MOCODeF9SthH8B4nISIqvXbVs-RdJjuv4GDuB0CgxAEG7VAcxvSnTNhZ5a_k7Rw4FLO-S60y85PiNf_s08BBrOtDAOYCKpTY1saSW3b1bUZiTBEWJbVqzLvVg3iAy4AyZQmk3A62a8xRvJp95tRDV-gEFvDlQ7aKzg_gPlvk8RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=CRLv_J3UEo3pk3r8eqPJaxiPG9YO7pQmo4ubSVxVaqH9nzzdSHxhPAQrpkzrkSvqFvmpv1ivlAslMHPTH5WIdHoW6DZ2YDjE6DOVgE4FJuC7CBvICzcZc5mawt_opW55ohjDV6N-AbEc5nY7hNhIVudkBfyJdJ3duox1GyDZNRZlXl38dgB_VK7Lelw3qa8jqly-g3Bg-8i73DzW5LvR8xxxzzCN0DAOsUSoVVm2HCBSsEXgG2UmhNpHXqSpNop5d78Mm1PQwFiCk8jfUaT3TNPc59KsQXjLLp54bZRnWbNgGCRPblXKtliXyW2f1hw9ANuJniM1h55kbCDbc7AFyhkCnC2iYwuXfMcuou9bE7s50e0Joi8VfVpu0WMaOLfFxXwKa8pH81U4grRkXc7nwPtXH6t-t0kKga76zs9QOWGRA-wlA8wgJsfacKGZNPO1MLM_LQ_FPPuOZ9G8MkruU3pNUpnQKwa_5ezGjcLcTUNEgMVg3FB1WQqlHawfLu86MOCODeF9SthH8B4nISIqvXbVs-RdJjuv4GDuB0CgxAEG7VAcxvSnTNhZ5a_k7Rw4FLO-S60y85PiNf_s08BBrOtDAOYCKpTY1saSW3b1bUZiTBEWJbVqzLvVg3iAy4AyZQmk3A62a8xRvJp95tRDV-gEFvDlQ7aKzg_gPlvk8RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5jk-GMEkHnuH9jEmwXxq2YHzMY7FqO711NRQbXvgZWWFkDOb2rQXsPBkf_39dM0Gl8W6GTcm25bki5IsurwFKkZl35oHi1RjBgQOOue_lfrMeGAM-geK-PfWXtj57DUzrW2IaE1cfEiI85LfIeqA6RLGU69n1eUOZYbMFusKeIxIEQRfr2aaxDkvEYpmbZvPtuPZCD9_jZI1yqNYOMH83VfYrnq3vOEXAsuNwHRBz5P955U-XMPagC7NPXyc7yhxkvZowOfa_CQbF2wGnCCG_orscFHe5ZsJ_rKbR72Meq3FPXXuF91cMOSKbf237RQpxvmCWMm_GG0AHnM-2HkrA.jpg" alt="photo" loading="lazy"/></div>
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
