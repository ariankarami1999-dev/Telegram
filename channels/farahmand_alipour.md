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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 18:01:49</div>
<hr>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbqRS81I6dl_3R8TOESEgEtB_rCrtsKUtwXDFVV73iDIslQZxUyIf4G0wCD9TGWicMj5q5sU4zEYBFFgzI8_xahUghv8BhJB8LH-DFXQJiggGCJHJwzC3oRHVE0B8we9V-I4ldEs4IHtAqkXb_mL7HCkbfuteJGbq6LZPaerZix1QI0XcOuS51ttGllNE22LKZaKeVrQRnlK2pymDzIwkdPGeYVergoSrfis3khPYj-6hvMnGl3r4eHRmGTmNiph2HRKbvczAtsZdl2XJKK1bIJ3wJoXsa5hwHJSLYU7TzEtlQ_ptj4JVexp4DIrOPR4EpOSKwWi_ORx9OV2Lw83Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCifBJcmvWNzkkHO9bP26HCXu905TdnULK3CVRW5o1ir4phaa8OrmAhAPHtC4nqP1M63iL23yVWPVZ-tlbq8T-C0Jul5Jz6AKXEiyZugBJXWoNoFI8btuFlECWD4tNop4aOi8eoXhBtEp64qp3ZOlDWxoSeDO6XnUl_1F7T-D9Yc_P_hYpCJ6iNQ2CTYfRdTTUN_Q3lZ-ujUm86bLL8gyYBodr_lOg2JPxhUqc6VvRQP8dA0sjMDTIDaaQSJhI3Ccz9VAz93iPEkBwKV47cc_KTDnaXp90j3-zKCxENZdmBowXsoHBOhsmvk4B1e1kd7Zd5dym2-l1-6Nn0GSCdi6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhspRjEojEV8PG2r8UxMAe2vctmlZ72-y0HqNMrydiGPwS8jZbSILED-odMqbiqSYhU297aANDUvknewmSHgpYV9ksrjYx80DEOOdoYzNnhdUK8HVjYHRk9YYb3XqXXl_3-J5s45HeUSH4I039dX5mxYVwpYIMMH8JStzkpuzYkDkAIBVsVFcNFOs_v3m3jk2xkkgr_a6LtMDE-WMQWsOaljOKIX9q07NCDY9ISvTLGfIR2n8kadQSxY_lq6PKOFn3QVamM56tlCszZJtcuEU3_xU57L2fTYoE83VBkKY_XeoyfCzR4WYcrljdeReExgzcC7K71tD-kwNAmB-WjQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=VUBaNPv5Ok6O2UlPhZNq-g6RD4xCfwi__mMnl8FaR-iB314Ss4SYIULYhrBZqjAX1B3HzugZe6GHHaW1kx0QKCCDmjz888snGkcdVgXrLK1ztoVQIbtYisY0EyHYflnYAE8P0ZaVjbWeggSOnLJAS4-qYL52LmHHdu7BQ0k-ADWU9o6AzpFS3wnu_x0UPUBQCDdWVB7ZzMQ0i2rWhsvivJH8YFHPmCin2jzjk3hORW-TBrc0QnKjCCVGyOVkVBDrIuVDlwVVVq3QpLlhI5w2i5iE6ZKsB9MkK8vlgm5---xuyJnNa_Qj_SVAd4d3jX6YOjXUoEz9Z1RHnSV3KhCicw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=VUBaNPv5Ok6O2UlPhZNq-g6RD4xCfwi__mMnl8FaR-iB314Ss4SYIULYhrBZqjAX1B3HzugZe6GHHaW1kx0QKCCDmjz888snGkcdVgXrLK1ztoVQIbtYisY0EyHYflnYAE8P0ZaVjbWeggSOnLJAS4-qYL52LmHHdu7BQ0k-ADWU9o6AzpFS3wnu_x0UPUBQCDdWVB7ZzMQ0i2rWhsvivJH8YFHPmCin2jzjk3hORW-TBrc0QnKjCCVGyOVkVBDrIuVDlwVVVq3QpLlhI5w2i5iE6ZKsB9MkK8vlgm5---xuyJnNa_Qj_SVAd4d3jX6YOjXUoEz9Z1RHnSV3KhCicw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7Ot7KDdQNsqg-CYOa5lCveelacQ_XZd3jZJ5U3UTZIPivghX4CHZtB9uh5kptPiTGiyeY__NhEsf-fU62Sqaw9miBv7i7MCeh2OyXkAkL05MDTlqkACo3roN-skXx22usz_CM41gDLw0Q0e9eKE615ceXiH5jn0mMFx3VexhYyP54Ot1QEk_kK6Cq9MowDjQrqvMnL9sbvfnN2rRJ2Jk0yXmTaRF8jwTxbuPp5ZLSe0IOx_VWblKvm2zodQxJKW7HV5prjFhC-b0IbmrjrkS7qnT4dAAaSAzMrCt6ZqySnjKb5_eMubP0uCFCHizFgVVyXRe94Mr2KMmsNr_gmI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFY7dco4X_uGOBk9wGkRKgb96VQuvPWLXRn07eUcLrGV95KhISzsjkD5gubZS1LH5SI97EnOMv8VmxINL3_6rgwHpnouVS0VZHwyxmabweS1VOXYO9TzwwRzlTNmX2azx7j4FkP74JwL7RRaImu3CUAT9j35ZNq1Y5xkBHyYG_sigGEL4bwDCpUrCBjS_r36-3FGbctki5GsaU8st1oUE4cIKLsF4uQHk0nM8VRQNOhrwT_yYn3be9621T8i_DF9SOs35rEmWdYUqnMkFhXW2mmd8QF_gNz_hhB3nZBicCEQjTWB9jOl5k0KWl78H0mWVZcQp0-SGuOSvsEJX4Bimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=V4byA6kBYdGjrX7ZLxJo4KMeUWTfwWJ6vqekKbR0fgm08v_gR1iQUe4j8vRj73gmfEJWwjCcNqeEF__Jxd0E9gzUsdmlpaJxqO8aUiL-zONCsI0HB_LxPkPNcjVP81gqwS8z7xQVGUz1F_w1o1yWCvpZZwk1cxWj088fNE3x--zzHaWf8qPU-dMxBK6E5uug1ZFjYY7iG5WH-KRodjCH_1vPfZa9c-5adAjfncTWPSHeUZK-jK_mOAAUZTcVqzGXQIHlHr4bFzgjkii8tPOxY8IKZc01b7czFspxQhDuJ51pOLHHAO81Pg-aQjEMgLc2FMwBbnoniZMGagjxDxbVOFQMFurvAVetkaeeuXAt6mBQ2Qtz740H8DN0cMKoajRl3OKAoJzmj6Gwu4iG8uqm6kWtmsPlJSJ0dE5uOrdRkCBEXKLPRDDkliJjX4Z3v4my-BwFXKcgoT_9Bboyy7Q9D5g8SdFlwoDHpoyFqMBjGDE3yPy9C-79DbYzg7SiBVgwBQczayRrTrMgZQKiBSgugKxsu70VNz_WVoREKbxFhL_Jiz00cCCM7SEw-iu6yjXI_YhCpu-_4wCjPCKZjheM-yM47hRfUxRQa0Q19Zas4hYHklf-2CQ215rTTYl9NLrKsD1eUAqpWim2R2g10OLXAOcHK1n08vhTyxDhpleQ0x8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=V4byA6kBYdGjrX7ZLxJo4KMeUWTfwWJ6vqekKbR0fgm08v_gR1iQUe4j8vRj73gmfEJWwjCcNqeEF__Jxd0E9gzUsdmlpaJxqO8aUiL-zONCsI0HB_LxPkPNcjVP81gqwS8z7xQVGUz1F_w1o1yWCvpZZwk1cxWj088fNE3x--zzHaWf8qPU-dMxBK6E5uug1ZFjYY7iG5WH-KRodjCH_1vPfZa9c-5adAjfncTWPSHeUZK-jK_mOAAUZTcVqzGXQIHlHr4bFzgjkii8tPOxY8IKZc01b7czFspxQhDuJ51pOLHHAO81Pg-aQjEMgLc2FMwBbnoniZMGagjxDxbVOFQMFurvAVetkaeeuXAt6mBQ2Qtz740H8DN0cMKoajRl3OKAoJzmj6Gwu4iG8uqm6kWtmsPlJSJ0dE5uOrdRkCBEXKLPRDDkliJjX4Z3v4my-BwFXKcgoT_9Bboyy7Q9D5g8SdFlwoDHpoyFqMBjGDE3yPy9C-79DbYzg7SiBVgwBQczayRrTrMgZQKiBSgugKxsu70VNz_WVoREKbxFhL_Jiz00cCCM7SEw-iu6yjXI_YhCpu-_4wCjPCKZjheM-yM47hRfUxRQa0Q19Zas4hYHklf-2CQ215rTTYl9NLrKsD1eUAqpWim2R2g10OLXAOcHK1n08vhTyxDhpleQ0x8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBjHLq2I_bTZp1Z53C0LPECMlAWvE_ob8oCAu813OOFfvXIZfCmoJJ_BnsraNNh04qlkAflVenYLIiAm1rp_5tfSpPEYz425UsqgL_-_epnqJ3GE1LJXdTIM7i_ZBuNZ-sv96XUE5cq01hasPvyy6gF7NIdRWiBFK0CLlmbPxG4R6go25sXcenQpT8q-_NrXZQJF8HbFTNJA7-I21F4BfnL3WB3u7L3SPgmwrj9Np6q91RkpPlbATNAFls4XDn0IdjQVxJzct6DwODCGKDYlPo0jlBGJalyM0hVlzriyuPULHrBoA6yhORGHDP9_6npuao2HV2KJlZw-Xua8L-_1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JazgJx7v0qdV3jTEHo-lMcyHOLxitpF6ty9oC7ZV-qxCR9azCjs09hrs7pii5oc2hhX9-DBFRyo0lm7OLOzgreL0ZS7pC4s49sflXs7Lynl_PRtGeSgVCtuL6DRlEYsJnwDYN5I2B4pW_hdo4b-61vy_wMXXCfyiAiDbxp5TsRuNhZETUblxxTw88vjwwSKjmzTMDjm_6mwzC5V1tKuvT57E1oxPfOchbOO0rDaBbiQA7N72BjEuNpylKLJBFHZxSajxgvffkeFox3psJq-m5320zKZ8fQfSLMUuquQD6OiWyxySAkGslHuu6NktSaR1OqkG0hmDKEKAAV3NN9J89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBYKjY0zDgOHNGLXdGrIYOsgYGjvW5DfHKi0-Yxgt8h3ZloFYr759CRWkS2Nj-J4GAxGElY8a8QOXe1A6P40BgsB7sfoQYBuCJvXjuBk7Sziec5kMvgQQ9wMUBP3hJKD4RP7o29k2kIGa-NEHuOa1nug7IQpuqRKp68JZO0bp55B-HxDlRYh-YClhpELfAwO-5TYb8Mp7VEgnD-q39h_WMm157fYxl9EH6KI9uEUft_MFdzCFtkETFwGNEO20ywaODD1dPTmFSgutLszx_LJqLeI8xgt590-v_3RostP_ekVpu1GY95pFLKZjXqh4PmDloItoGzudWX17N8jIx-XZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuVErMl0wD67RpHSKWKzBTto2oGAG0t923kW8VbFSyCOHXqUDrpMZT7AJQuTHlaL3nBiV6_ZMDYTyFJCfq2eK-4kwPBSJpk04KAq0_2uAs-0syl7wZX4m-9BJsNl_BBIZoAO1zy-NJyT45vtqtDpk5r8t_VMcaGerRqHVi8kPSbzNZgT77FYJh1aR0rbxMt_L59or0hXEf7J7qJ94k-q8YVh43AV7rkGIkAVE99eEu10tC75qQNgtOTK7UW6DeDnIA1v4vY27juhK0VKkxkAaJPhGKXqbntInmDNWqlml2vvYHEuMCd9JwSisAY0peeTeVWXXP-PMWbC1F_ga1xiHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JAKpSCpOMHHGsz2cTa1HPpaNNzOon415sWfkVo9__S3MbAKgcqArg1W84a7qf4jc4SMy0eL9xCriDFwWBS6J7qAAAqftdNz8bcjXmqV1lXtaPEGl6mMHFLAJo9FadZg4ei8oJXZQoyZzpo5fE3eU2zVyir3Ye-MrPC7ws1j9mBz2iIKLsUhSj8zM6tJwWUBu1Q04y1CKNfX9i2Vncmyl--IfFRhnUZlVpN-QqPYf0CYSQWBz-hmTAWFdicg2QDEzsZ_2E-FkVVDfxUjsscwzFaWYS9DbhD2pMVy-seS5lUpcysHvvxYYvqSWzmTmYchGLPhh2dKuXMHAZr5RbQaUSJYXlw3DrwIQe9Px_uIzvuNMHVIe1WVQ6uF99U1MpCQ7lKD8WgipXScn0FX6wbNFIAwb661S9UQtyi6bSUo_6JIgXceD3NnhOYK5sV5XnSXvJu8EFujSpMCoASelss8VQ473Wzbmq0DtV8Yc7-3UuuaSSsomj1LDYD7BKxKSyJAdhOAOzHV1lCPDGRCNTZOYpMkySnXt-no0qFa7-JidYmHV04r6IjbMUEId-gR1jKjaGP4VElpHX2ROZjOwr_1GzMhOhFL-EdH8_B822SAQrRlHMvbESwONOW7ze3Cb2K-iZE7QM8lbWJozlF4Uh8ZhQt1ngSEyxTDj8OBUg8OA7CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JAKpSCpOMHHGsz2cTa1HPpaNNzOon415sWfkVo9__S3MbAKgcqArg1W84a7qf4jc4SMy0eL9xCriDFwWBS6J7qAAAqftdNz8bcjXmqV1lXtaPEGl6mMHFLAJo9FadZg4ei8oJXZQoyZzpo5fE3eU2zVyir3Ye-MrPC7ws1j9mBz2iIKLsUhSj8zM6tJwWUBu1Q04y1CKNfX9i2Vncmyl--IfFRhnUZlVpN-QqPYf0CYSQWBz-hmTAWFdicg2QDEzsZ_2E-FkVVDfxUjsscwzFaWYS9DbhD2pMVy-seS5lUpcysHvvxYYvqSWzmTmYchGLPhh2dKuXMHAZr5RbQaUSJYXlw3DrwIQe9Px_uIzvuNMHVIe1WVQ6uF99U1MpCQ7lKD8WgipXScn0FX6wbNFIAwb661S9UQtyi6bSUo_6JIgXceD3NnhOYK5sV5XnSXvJu8EFujSpMCoASelss8VQ473Wzbmq0DtV8Yc7-3UuuaSSsomj1LDYD7BKxKSyJAdhOAOzHV1lCPDGRCNTZOYpMkySnXt-no0qFa7-JidYmHV04r6IjbMUEId-gR1jKjaGP4VElpHX2ROZjOwr_1GzMhOhFL-EdH8_B822SAQrRlHMvbESwONOW7ze3Cb2K-iZE7QM8lbWJozlF4Uh8ZhQt1ngSEyxTDj8OBUg8OA7CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TiLU2r6RWTK8EJg-zZmneC2btEHcSfrt8HAvX5iLl8UAG3Ee4DR0cIYv2o2UKEvjN6dERtf0J48aQ3hnPE4SYFFZWTAxNgQ-thnCNOnqTo18Ymyh1PJIKhQI4b3FOxMRH98ll47zMTxIh8YNTBDHWsFKHEcbzlAKu6Z2ayWX1d4-NePrMpvDR5lYpFe-b3_AiRWErUeJ3Z-PIery7yWrL_pvc3KRJBm-VbEjQcYvbeUNO2E0NXP_odgsbAOzE6QI3zGeXPE8EHlMKIdHfORyCaNgR94iv0BVSfKFrPybqCSuV3iYVxyYaTJ0P8Dns3Gn4Z5L4hiYY9D4UNOFPE7h8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=TiLU2r6RWTK8EJg-zZmneC2btEHcSfrt8HAvX5iLl8UAG3Ee4DR0cIYv2o2UKEvjN6dERtf0J48aQ3hnPE4SYFFZWTAxNgQ-thnCNOnqTo18Ymyh1PJIKhQI4b3FOxMRH98ll47zMTxIh8YNTBDHWsFKHEcbzlAKu6Z2ayWX1d4-NePrMpvDR5lYpFe-b3_AiRWErUeJ3Z-PIery7yWrL_pvc3KRJBm-VbEjQcYvbeUNO2E0NXP_odgsbAOzE6QI3zGeXPE8EHlMKIdHfORyCaNgR94iv0BVSfKFrPybqCSuV3iYVxyYaTJ0P8Dns3Gn4Z5L4hiYY9D4UNOFPE7h8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYkTfZ7LO-H4F1HiGSKXJdiw-Im8iGdrs9CmlQP7m2PjAJfs64v0aMZvLNo58HT1IKzBe-iAt_Ij5zKuc4g3fhVoO6l9dO1Nt56HLAiWj6b4EkbHRJ_bLpMg_GwRfGhILJdaHg_AiQf_qhnr6smacMCTmBs2USH4zvDhd9mDOoY2Y6A8vAJBIsQw5ZeRdn2q9jeo_yk-U_0zLWR9Ct_2KLApVvG12VDryfTKgpBlJiAX96TxSgMsvVjhUFiP4uoQvGfreYdnE5WLKjjrS87wiDs5Yfuq1LmRi1eYA06V0fBBSVq0i5wcA8unRAdKSZH78SUK_rukxZEwcfquVMuVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsIbc50cdhPs54ka8F0nmmNiGmgSo885ShR4hFziKyRP5bR2q0l85C845tPg-42uQD7yxk7EEMSQNw8EuBdlKbqObNRvbz_ne0cvm7ZZ4dtbYArC-qrTH5X3nlaGsKQo9xSbX-pp8iH8GlQFQUVod6cZ8Fi0C-D9c5GkfQr6k_m6OtHU7hTZCw7k_Xz6zMvHaFmFkUqhISL-sq-Dd6uPgvjUn9BHfTy0oLUAKD0PtUEdIhR-TcENHXqh4xDgvwo9Nx2UQPondb00Aub4ueDNlxYBrBTStIK8Jz3_8XmkgbDmJWOIxyacJiMu8786Lnil81BxP75iuXLUc7EeatB-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0jXUDr3DIVXyv6v_YErk5Kw2qYIwtrNmm4PqRCsUCxrO9JdR3uolKREpUCwy8Ih-9NzWEajrigx4et6oE8XT0fFLC9jAqgNtf58C_ledEfC_9anp5gLO2yxMLPnfkKFHvjBOHs8EKJVDOM_P3WISfxb0ELKxHo73ZaDfIOFtyQEcCwa8f15Iooma38u-11rR-sFjaA2K5EYyLxlTo2o93OSMLSZ1iGoVpXTidb6bUavG2o6S7dTqf7-lAbdAxfLHsGRQ7zTXV8ubdqIX3JrpneOrfEfRW55cbWvdBviuCNDPmrROx7xTThpvLcmtmV7-ee_whLLO_V4cSVuw38N4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vq1Fo7OME2LfTJAaEiATDlKW6OgHc7R3BQ5jgUw_Q_zyZqJ5882o4zpSlaZkfBIvU5UXeyarhEIa6E4F0ud3PpuZHqKe4E-V079fELIIHYU0Dk7vMpaafoJdptkxbmA0Us8q-q08HCz2Mn9IL_QDY_SoVvL9shJsOzXiieqseMzs3ZRsR-5OsU_PHbF1f2ifatMabMxTEIbfjtadoUU2phmt5Ti4prUbrD4SEBSz83DHgfWoblIUtcokPL5_R3DBdIWxybrzH7fYBnt1SxG3-VeFrlcrL24oQK2maDC9hVHWBM5V0QA3DBlRz80Gk3TzfY1EkfH9GnYSAq1j2jhERA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYZgYmlULCO1bHOaLlCZh2bLq-nihsiut5IHwqA6VHKpir-8PYyswOjomC2PFe6BNGKkRn6MBM79UjLmk4fusUX8csI_PvrvwY1bLht8UZ6xEyQe9DujJD3MR_ZzlBzeGB1OOpxxeAfCIyVvVGb1VrG9MmsXy9NBHbJGQSrB1kRjxK1A2R79EhZW9rhxDk8kS0rU5KqXRSZEfwXC6FHlXpmgEL096G0_sOYmOBLr50zZZKlUjVOR3Tk6ypJRuCfr2vfw8AKnOXOtTNyQIvRGZHO8WDwlCCVzJXBMsFzbZlOxFzx-DDJp1WL7pLVnSsK-mQovPynUYTnq2pFRnRUiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ0vm1aCGSB6Yc-NwWWUGhg9Ol_9edvEV502r9yHW6GODvYNEfU0BuSVimiVM7wFvVKhf8n_3EJCp7yoo4NinL0fwCQAakIUtqPFVaDrRz2RXnQ0rcNVNr94obSAM3-4uAavk7Ikxk11y3r1M_bLD2ZOVm4I9-dJxYexdU9l8E9DZrC9xvoDbtlxs0TvAmXcGmRyP4WI7X5VwUBHK5FrdOj2bvgh2mMpibhXlows9MdM18WysDnuphWwLJq67qAl021ibkYeIHcrEcgVG_kJv5nzaCy7n5iLzuOh2n0pDc5lQelQPOK0B5OPt8lc_6Bo3cJRb7HjA86AiD0HK7RswQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kopm_SHepe1vfnRv4yfDRuQKIAtqAzfMS5l8ITaBIGkk6AyNofGt81N4jC3qQPXTHwOclgEfXq4pQCMYg6oEI2e_zej-khRyWfHCwltpluy2UzS3ZxrHihcOEXDZJXTBZKIUSDPaET1ka6Tln6krIserNS_BFzainU-KGglUxcU0XAVaq-ZquGMV0pkwwFbwo-78pFanHS_OotQJaqxT3gs0MBWwvKGZwrgyMQAdkqGYtxQt_uZatx55SBlsqnTWfE43U-tqZUl6WUNd3i_9xlXGYiZtjx5PuJNkSymkeZvfmzNTkTuRfjHfupMzbGW0Flqmgp5o765FUvYJS2iZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=h_PGMAEp5nhhMrxad7icTZHYdXIpK1vsF-a936U2DHDXpemxM7L9romNE0v0YXZIXv1MpSNKWTNz1slmeD6JjTv2KIuDo2xYqlTN6ReNuh_U-j5DDEAl6uUiGCrpdoItJ_gbNDPs35GbYkoO5sdbta7oUsSp9FC4xQYfQ8TCLqmkScsnUke65ApFTXe742zY7fWp8srWCpH7ZVdN5podiu3rE7r3N-ArVncKIT8Uq4crE8TzZkgYEzqgtvdaxNmB5_918v4bh35B7XF11WjMQSoYa66azj-VjGLjKA4aWN79wlc8l_-a92s-5iTwT3buahUm2XTwmt8cSYmfWY8s1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=h_PGMAEp5nhhMrxad7icTZHYdXIpK1vsF-a936U2DHDXpemxM7L9romNE0v0YXZIXv1MpSNKWTNz1slmeD6JjTv2KIuDo2xYqlTN6ReNuh_U-j5DDEAl6uUiGCrpdoItJ_gbNDPs35GbYkoO5sdbta7oUsSp9FC4xQYfQ8TCLqmkScsnUke65ApFTXe742zY7fWp8srWCpH7ZVdN5podiu3rE7r3N-ArVncKIT8Uq4crE8TzZkgYEzqgtvdaxNmB5_918v4bh35B7XF11WjMQSoYa66azj-VjGLjKA4aWN79wlc8l_-a92s-5iTwT3buahUm2XTwmt8cSYmfWY8s1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMCUgYfhhWe02eD4HNOI7UkAkrVVnMc-0_RyhdM6qi4rYoHJWctao42e1OqkdAloCoLk-cZGBD5NV-7gBWK5hwDXnSBtWfPjl9C0YcNSv1aLXbSH597XlFJUrRAvt093yAnmkKKEMiKcnYqpdA8f9a3hbzP6uUDJTGXLnZP6_mj7xoLKI23Sa16nCZTPWWid1-v2mGhPffTDfTP6KBri1ECyrXaiMZnU3Mz6DA20W-Q0wLT87_iDRNE4T7a4CAdoVBT0om08HbC-me7KyW296QacrrgbWZ4iu6jJbjrzmJsL9WOdyCmXDpMmYQVHjUMq6qKqovS2BlJC9XAT3UTeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=s8_fJX3TWa_Bj63rBYUxBTRIoOK_kkuqSKvvhAeTQJ_IQvkJOigWItASPpGj94_wH0p_wVrdIxNM4TX_-1gXMts48B9cltE7WoECMR9og4uAECDjHvHFfDDk0szea8J0NFrPwcKegtaNaLAIsRkx7bZrV9x0JE4-r-ETDCqC2wXB0GByyQ4EQO98Lc5A0W5NzLT6QQ-gUMijXqQMQsNUYh7y7tBd3ixM6xzlOmoc4isd3yp_vxd_gecNS1vjcvo_7P5F_z_g1T9KT6PDxSnHziCI45_rtihIQl3IzbogPq63plu_Zi0N_KsyCOGQu6R44YsNNzJMOxmlreIRiGoE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=s8_fJX3TWa_Bj63rBYUxBTRIoOK_kkuqSKvvhAeTQJ_IQvkJOigWItASPpGj94_wH0p_wVrdIxNM4TX_-1gXMts48B9cltE7WoECMR9og4uAECDjHvHFfDDk0szea8J0NFrPwcKegtaNaLAIsRkx7bZrV9x0JE4-r-ETDCqC2wXB0GByyQ4EQO98Lc5A0W5NzLT6QQ-gUMijXqQMQsNUYh7y7tBd3ixM6xzlOmoc4isd3yp_vxd_gecNS1vjcvo_7P5F_z_g1T9KT6PDxSnHziCI45_rtihIQl3IzbogPq63plu_Zi0N_KsyCOGQu6R44YsNNzJMOxmlreIRiGoE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUv9kpuElhgOVWpeYBgsyCwHhfUA9mMn9HhKRf89m1Bd1uFEwNB1dNXlk8d9jejDgtL0L4R4vm_zQf4YrNofxhTVuZRnikU4Dl7QK89u4mYhQ_PJEleQyq-487fAcRFgDvBz7hEPDBhGkvPh_I6oYQ83jUWo_ajkv1tT8HeAPK8ixgEYtw8DSxg5IR7VquY30wxzAKwat4lu91ZQyPMaASizCVNr6fbENF4ndTdJgmjMtPD1IjOcU-DqA2agj-9VgV2BpPSqhAm9kxzsD64mtAemHq-xbehiF_Fn7IlaereTAKeN4eB03we3yRp4Z7yN1297p6QPfv8FPGP52DO9nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGLbn9OPK4F2CloG8OvzCt44OezSuG4wAI_xaU-gxA-Z19tCBscCRCs7waIKYAQIKLn9jEyYGwQQ9qYMY2sWkbk9YHiUtM83nPjJkA6xSICKrApji3TTpgxuCjNhDk6FpIdO8wilYTAZtYLhu0NllzlAB-PXjWyvU1Kh0FjoHCQN8kVsidkPo06VcdIPH2CH0M2hluLD4x0pIa9wK4d86NCk3u6Kb-IH_mbW8v7pDjMFujC9WmQIrLiNE4RLCFBiTj7y6bEuoHnufT90GrWtK1ZIIX-zGvPYcHRXQBHGS_eV1AQ6hY3VHSrIQJoIzi60zz9tR7CF1q6LNmkpPotlWEEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGLbn9OPK4F2CloG8OvzCt44OezSuG4wAI_xaU-gxA-Z19tCBscCRCs7waIKYAQIKLn9jEyYGwQQ9qYMY2sWkbk9YHiUtM83nPjJkA6xSICKrApji3TTpgxuCjNhDk6FpIdO8wilYTAZtYLhu0NllzlAB-PXjWyvU1Kh0FjoHCQN8kVsidkPo06VcdIPH2CH0M2hluLD4x0pIa9wK4d86NCk3u6Kb-IH_mbW8v7pDjMFujC9WmQIrLiNE4RLCFBiTj7y6bEuoHnufT90GrWtK1ZIIX-zGvPYcHRXQBHGS_eV1AQ6hY3VHSrIQJoIzi60zz9tR7CF1q6LNmkpPotlWEEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=SIvdrzES5KpnrARz1JNznI30fwTv7OIqgeHN7oqUcPGNr3Rrf-KoAUIWbepedLPVMk9bC4octd3-ifVrEcT9Zci1MTllN9yLlWD-FZ3MhYByRHuxRsagg5u1NMfeY8tfz96Lu-oIADxArdKhaIZuARfX1ljCgZMZn5IYwq8PPa0x7vfo0c8hNW-1Zpks6FZJsBpWySvPdF7wdsb5-4bFoTEhpSrt8bdN2GjZhJQZ5yCuWqaGUlb-BLVG9SrFmsQ8-M0bpLQtQRiOrAGSjeEmyRljzOuppxP32OqdC7nuoWCdrcHASkYYB13sP3wToiaR-wIyM22l6E-pD8XNA0EmBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=SIvdrzES5KpnrARz1JNznI30fwTv7OIqgeHN7oqUcPGNr3Rrf-KoAUIWbepedLPVMk9bC4octd3-ifVrEcT9Zci1MTllN9yLlWD-FZ3MhYByRHuxRsagg5u1NMfeY8tfz96Lu-oIADxArdKhaIZuARfX1ljCgZMZn5IYwq8PPa0x7vfo0c8hNW-1Zpks6FZJsBpWySvPdF7wdsb5-4bFoTEhpSrt8bdN2GjZhJQZ5yCuWqaGUlb-BLVG9SrFmsQ8-M0bpLQtQRiOrAGSjeEmyRljzOuppxP32OqdC7nuoWCdrcHASkYYB13sP3wToiaR-wIyM22l6E-pD8XNA0EmBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=p4FORe7koS_A540hbGFajgtqvG3EHVQlTguR7KT6FyPGHj79-Y1MFsIv8ghtS94Fw5SmraFpGsOezrBmrQUg_SPsTvWkkJJMfq37w2tLoxOxIBV4OEJqecUbh90tg3kOG8OjowP98l0Lih6BX86TaMq2vpFyUU4_Rn7rn9BIB0nJXWWo4Z1cArHD7Gbtw8UU80DJwKUZ8G2HPPeTK8BZzotF27wJBThO0DffLoAH6ZQo4sajO5yrgMPdY6dgENPCzTIwcwIHoD0L-yuJaJmNeo56mUuCXXGTN8VUvRmepPXDoHqn3jLqZx303i00vJnXPd3cVc3Hta5FyM8gCgn0ammrkrBXiK7L5mFvOBMiSwH-BZNU2o1UklNpjJgHXQ4JBqgh7qs2kyb4TsHuZigLHpNPo6i41_PDGPBz9XfntWYVlaQ_mIFfrhUPQPJhybENErr459uOcbzXbl3PWesSYOo2EqQDcUeM6Y0e7q_ax4ZEf7-sSzLC6Cbid_6ySsdUz9I1df7c_y1aXq2EUwo3wYYEODg--dWjCbt5lypSHBb43T0ny9ISCf3IcJpQGHKQr4u3WRCYLyg6ewjlT95d7j0rZjyR68RFi_MBXCM262n8VNRAFEUyCNH4zvFM6FcmtkeJFYyzDG5C5kVzWkj8IL2NwM5Hi1Rr1LPxCaHqZuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=p4FORe7koS_A540hbGFajgtqvG3EHVQlTguR7KT6FyPGHj79-Y1MFsIv8ghtS94Fw5SmraFpGsOezrBmrQUg_SPsTvWkkJJMfq37w2tLoxOxIBV4OEJqecUbh90tg3kOG8OjowP98l0Lih6BX86TaMq2vpFyUU4_Rn7rn9BIB0nJXWWo4Z1cArHD7Gbtw8UU80DJwKUZ8G2HPPeTK8BZzotF27wJBThO0DffLoAH6ZQo4sajO5yrgMPdY6dgENPCzTIwcwIHoD0L-yuJaJmNeo56mUuCXXGTN8VUvRmepPXDoHqn3jLqZx303i00vJnXPd3cVc3Hta5FyM8gCgn0ammrkrBXiK7L5mFvOBMiSwH-BZNU2o1UklNpjJgHXQ4JBqgh7qs2kyb4TsHuZigLHpNPo6i41_PDGPBz9XfntWYVlaQ_mIFfrhUPQPJhybENErr459uOcbzXbl3PWesSYOo2EqQDcUeM6Y0e7q_ax4ZEf7-sSzLC6Cbid_6ySsdUz9I1df7c_y1aXq2EUwo3wYYEODg--dWjCbt5lypSHBb43T0ny9ISCf3IcJpQGHKQr4u3WRCYLyg6ewjlT95d7j0rZjyR68RFi_MBXCM262n8VNRAFEUyCNH4zvFM6FcmtkeJFYyzDG5C5kVzWkj8IL2NwM5Hi1Rr1LPxCaHqZuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbb0iZahZhW02P3gi89c2QQKTBMPjN7Gg9q6UZSZzChRW_tL3xL3kDHi4DOBIqJkP24HX0x5oP0A5vEJdC_P6YWjmZEoy_mCLqHnOJG3Q1Ml0zNl9rFXH-AW6DObIQFxie_zDhRiBfxxq9e78Im98h_Q4TB__6-ci51qy70v-FjPBa1Wu31hvMyTiIJ85sf_2zaXeBuIEx5NzBpePmar-zGjm9w4OVfeA2eJTAnIxyRgvYbYxEFMb_dZGe6jWOK4wxGIMRnY1L4uI_xL1ISwwcWqlC2hASINkHizOG3uAj4dVm7hdj1a5CGTXoy8CGGkasHAkrefLBjYmtldwFP6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNz0xjrtAKKZokhK2_A2t0oUXPqCfQJrfcsLTNC6vejili4wvuJOpXzH3jFjmPQkka6g4CaT11ya5qey1bfsbsQfnpfKcYmVAUhtJ679lE9-3DaZ2zjZhU0csSfCVEPi_ny2ZVLvkscMsedehLYjnr81gYeLIDvNc8c06WgQk2o5LdDHR8cO3UW7HtQk6WE4Lq-Qj8R9Wdq9PH-zUcFpGCeD11_6q8od1P_uqgkaPfA1NAIDmTtRzjViJtAVkX7H0PScpyBHbj1rtRxPwdyTDNzSrU8ten930Du7-xT485kjrvXVSQsbelFe1u1P_v6m1NUdyPdteUgCPnOm5I-vhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPXF8SYDeXloMAi45m5BICwMzdCXzxTKu-VpPUtroA-bsZd7fN9GNXrth8o2FWEYesUExi4v3NqgVHe7FPzs86w7y_kcYQOGH2z6eivpV28lA50jDcFUAWRoSP2robXiH7pJWnMerz9KlihDz9e7fOpyjgulenm6q85_cXkc9FoHNwy5V56rdsNuB0Enl201N3sO3K6e8b7DUWQgcPJCUDPWoBLfghy8uFaAz3bxw8PzAF6RjgAuQVv00O-mwP2FF-7JXZ0asAu2auedtu2djqh3xfsEZPuOptcfuyqmfFR6mtze-6uV3Hv3CrRShNiRNv8EP4_5yv3l8zgTFRHWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXVUx5zY-ZZxdsrmSCR-ujr6G-c9au9l0GUYAgAu_aWcobtPVeFiDWZXXginYDeHFWFeVZXgZw6UlYIi1TzwYhOFPjUinnx8P2KdbY0NmznY-c_QXkhGci0g2wNOAzxx9KHJix6HEc0okXW0dJBxKVtQgmd8W55tdQVfrOtrXxtzS74iguDyxukSYbRvtNRXLzBB8kyNb1lisKAt9-WmcDT9-PBFS3oxejs8Em6s0WukzwTkEF5ECSl6c5S2mAxcarS2Jyd4HYOxv6jFtP_xMARf8yBOYdxAkJFHRmPwedJqztj_hJcKSVwCsMTe0zkOsek8b37-Y1Ns50res7uN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Nqdp2CY-JMnJU27ydZ6hO4drHAgKh_ktxTGUZLtGNpbsGRLR1rZ7aydPtRq2EeMnNqkJjx6KSTOnBGpNXbLlWZ50UmK5XTgQ-K3AFbQMg94I7gJjZPRiPFAMtVadgNH7hl5C66cj_l_xv-DE4Hv--9GkEAdfqdRJ_wm8OlRr4FCQ0uA4PXvvGvAdTAgojUWLze48-ZV024LqYRHdGH3R4Mk0g6_HeUvMMaI1nEkKH9EssZFqnco3RgrRcCt0o2OVOYFWcD0Z6H3eQn1Axt8zS0RRcvTfzcu687L6q_QWC1sTBhbHoeMYxUHhD6MJexgb2OLhtWNjZUdov4uRIc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju8VyAaTbgwSeKLvvqSQvfk_S6ssCClVZYHzu7HMCuR2L3gtO7WNJX0G6HVUuxkTOi9trNqgPh7ipr4nz2GOY0Scrg0R-Py8ipm2_DSER3r2G4q0cC-iJ_rW3guWWiH1MFWsx4wJhadlq08kE2mDnwFiKxoLeeWiwcCcxT8fzXhRAVxQ4oSHkjf-HGs1MbXkB2y-JGnGQfym1nzJ9eN0hmgLu461QEhThQ7Mw7Mef9P7NhBdHtHyVH29Pg0cAlyOupoaHAWJfEMCrNIXUQLDh79-GGQmBk48PQyABZL07mZVbg1aurKCN2EDrV8ioG9YvaiblzDQplUGFGnv2FdCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDyi9F8Hz_3ABbcf5lqeZPXk4CFtXvIRj5-7s9p2yYDIvJKVduHjC2B-nUVhSGU_tr-Wezhp5_-LmD4kQFTiyElbXXeM0OD6IzOBz39Kz8MYFkUQYlbY9d_kR91AzHddkr1U57DXIgASlcPcDaXHRjrb-cqf8U1ud8TC9Jg5ev5jukPDd2rtGzy9_qEtq7dHTtC4VgHiE8AfiS2TJ6neochzPz4UW7jxQwkFjTdp6HDZTg9Ipx6D5593c2rNtc1XO6GHNqvjjAvIwlij3f7rM1ggdXlgGl6aJEV_9STnDNidEv2LgtrcbjerjXnXvoLdDlQcgeI2qk7wajpvL8JI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6zd8G_SjqUOgR5loVjebHZ1MHYX_eU8z6Ye3CuPRtoMLZfoT7eD-7V4-twA6jv_lm_qTyML07T11y8Vio1Gmdhvi-ejsAws9zNyxTCab0fwjlmVRLCYPWJoV8Rpg_nezb8GCsccAaqT9Fpsm8NerUmfkRnBFGqFxDdrZPfCYykgBdeq5ZOEPJRib7T4gqV8GBgZ_U84CACbHsx31InUKneFwytKTRWpiuSJccDKPB9pYCZL1Y7kCPe8rJH3GigKyWUqijUjQd2VPm98evOasKNknvPQ_iQ7qE_aN-Sl0fhqrXPlSMbe2nuwqOsH5QI0Zvl5vL-G0PXA5DzFlgKtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXyUsP9331TlNRJs4PC2rSZBROKFECEbkTBJq0M1FWM0LEdtoEUJSJ7RSyC6MciDI8zP-gVVRCdUIo_Zt6VtNVh-BKznZHkoqolPevooR2glFct0Viqeh2FLHNI2SVwxwx4DyJMrndOGVqwlKX9jHZG7MfvS6vP3BXPrTan6wzQStPvz3fBPdZAzpG0o4P7_h6glUa3DYHv0Q6Ubz2EjrGgzD8PDMcjTubdjwbDNMiuHYbQEbb_HEqB8ajJKny79b2Ek2EMGQAVcp2EKt2clMVT4cMdu6HWx6OcreK8HyaE5X_KdEr8G1XGLlfAPeiqz5KPWMtgRHRyD3Hr6h-EK9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ__Neu8olAu_h4DeCyBpQBV1aGIy4Ynfl1SOREYyEpbDnr-IoLd6QjWzphMyD2omLlROfwZ9YedPeO8biLjptE1qyYTEGKSN8HyDqvmazAA33Vuzudyha4qrCubxmiYkDOUDPqMrIxpd3sEMn8S1WODHaSm4bTNSJ2ly3zMGk8mnKbxdf_eJGlBsTvzpGvMzoN1oJ4wGeasW7Ku936aDwyy_SOql9u_CyQu-ExrcOZ_Z2soPLP-69mRE5EPh5BMtC9cSqRPKW5_sjS0Nco3x4tFay_sT2--C0BdNowKrDccuhfFkf6Zs1WZ3fSWSlNQSb37A6tw_QQXt9FtarjWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTzxr8bxcbMJzt-1NEbmYdFa9O6Jwzp_oL2ESvor-86LmvVAurw9fvDCYUjHEan2fnjcKWStGS42K_UkfjzaNnK0pILi4BmbjYgE-N-Bf6qrpBA0BwM579LWllAv0wNZucVXeRwo-LoILxRKJ7C7F7X8XMVvnpqNUR_qQ_SEis_G7YaCqFmk--3MlJJux1t1j0T_V4Pknm55B1JE5JBFJh5e8vt1hMRja_qIZ1ZLxaDsyWgAjK3W56sHF-up55hGAKLf3vEBXMtZ5-BJ0PIJ59IPJcAkQM7sSzCZWyXNZhy0ddsN0lacaSznIFVdSbYiFf7SCRV6txql12xNhEfWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m70yuY-pIlppd0CG5mI1XbNpi7g-itB0kDYHHJkUirJ8sH0HMZtYBYCj8kNPwJZLw6gjxrQYHp-QI8t0BDcyDYhgYw1tvl0glOgzIOyPRqQqPU7YoXQczeXa_9zaAxDAZ6AhEtgmFqqsKVfOgXOUR80GYWgTE4r_i-aYchUsc29yV5QcV_z37Lkz31womOLjAeXmRZ8FOx6YnU6UAkM6OrohR3JfqXi-iuTKDbRSdtG0Do_10QwVQP0f3xh0Y0rsJNiO4MoS4_f7sa-Nnt-wPlHRjVrYU7RJzGvdiU0vJMMtTzfJiD5OVs5x1UpAXrx7dZx3G1SdKlAQcQ6_cwOyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=v2gowxLidAJEViKn4-SoQN2jz96oVmmJ7p6pOr4O5jJg5VCp2lkeL4Qz_7BqUDdmL0iChMkAFYp8GU40aNnwr4SUEQvxADNO4ZmayS9sKkDWu2KpeyyINw8NdlTvQtnQ-kejaaxUVw7ctBWX6N5yHflq9-9v3m5grU-8UqlIv3iH5FthaUsnsXccUvOYvq6jPyNCOlRjo5U3UdDSh7ag_KLAFJy2Tis7qjS30gFBpRRswtsEJsYBTFCG_1GiUIVCK1KMwy-NRcxJ5P35btWJqIX2Q6Vbpr21Yk9ZuG7W94s0b7lcnjGYdGu_lUMGopOlP8stDxkcSLzwJSblwgy84LROEIlZ3uyNlb8ABZFWQdRLozTODnILxXdikJrlN7L2ViezAPSoJZzF58wv05-tvFZxkyoTFUt4c6ASbxIVhjUQHMLb4zrDlBKQuUp046O7gUj3jZOf8zrVf0A3HyLqcF3Ga_9Y2K-hubeXH4JK6azxQFRpdMT4PwpJ0GgFcMvnZ8z8MjEsBJAEO_rjym07C8vQzX4wLhFH4UubKHxnzFYjYAwbgpzrquJvkJ8ilcX7hmowP1Ni0UXR_xOB4KiTS9a8LXPiq0HBg4bRnPlgAGwcqErH8AYkviOww5mjLXOV2iEYwcOOSRshkg8ygY3SLCVxO4kU2FXwckdwRHB5uiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=v2gowxLidAJEViKn4-SoQN2jz96oVmmJ7p6pOr4O5jJg5VCp2lkeL4Qz_7BqUDdmL0iChMkAFYp8GU40aNnwr4SUEQvxADNO4ZmayS9sKkDWu2KpeyyINw8NdlTvQtnQ-kejaaxUVw7ctBWX6N5yHflq9-9v3m5grU-8UqlIv3iH5FthaUsnsXccUvOYvq6jPyNCOlRjo5U3UdDSh7ag_KLAFJy2Tis7qjS30gFBpRRswtsEJsYBTFCG_1GiUIVCK1KMwy-NRcxJ5P35btWJqIX2Q6Vbpr21Yk9ZuG7W94s0b7lcnjGYdGu_lUMGopOlP8stDxkcSLzwJSblwgy84LROEIlZ3uyNlb8ABZFWQdRLozTODnILxXdikJrlN7L2ViezAPSoJZzF58wv05-tvFZxkyoTFUt4c6ASbxIVhjUQHMLb4zrDlBKQuUp046O7gUj3jZOf8zrVf0A3HyLqcF3Ga_9Y2K-hubeXH4JK6azxQFRpdMT4PwpJ0GgFcMvnZ8z8MjEsBJAEO_rjym07C8vQzX4wLhFH4UubKHxnzFYjYAwbgpzrquJvkJ8ilcX7hmowP1Ni0UXR_xOB4KiTS9a8LXPiq0HBg4bRnPlgAGwcqErH8AYkviOww5mjLXOV2iEYwcOOSRshkg8ygY3SLCVxO4kU2FXwckdwRHB5uiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=gfLIL3bit4dDWXCWAVF-4WZkEXYFJEV7DFBXrmiziJUzyAwAQaeV3OYq_HwCs3dDC0QFjy5_0WqHC0khXxvMwP46_S8gJWYFZpOTGDACTwtrx9PxLf1_uf_FexIGaW_9pq3O-vZC_gryqM8cbpQu101z3yR_oPgstih2LPSDG3EOdrLllmnMq09OH3YlKoXgutwI8sF16AvPl3vnunv3XxkcbMB5fxNpSOqf8PA2OqcHMEVtJv8_z6A7YmfWiVD8Yfg7I89Yl5pnGZuHylMs_-yCkQqA0BLGtyTFRex8L91djvvEdN4fwKTusjHQXC9ms7X7WFnNTRgGxCJmqKOK0hclIn5wvk9RNndurcTeWp6vQLkClq4pzcAeF10Zn7LEem5ixWkxPI1avx4ZpJ9BNxLxCxBPcTSU92KWTeEdei76gSCHcL3_XjzXpe2OPxOBGgT-AXWOHBulW9zJLW5h0gvq0LSQjq9lFw0X08N3NUuqGE2M1eXtPB5fRQv0iT6phaISBFrcxVX4GgGf44yo6aeIAtped4v4D5XDa4FKm1f-_l5Gppraka05wsxeMFV4YUQfPp0iBBkY5FdNb_SZCq8h4TcYIKbMFIK0WSMcWLa06euqwNGnC28rXjKZU2a1rHSt50y8JNkWaZ28af4e-xKD40GY6wcjAuHxI7E9zOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=gfLIL3bit4dDWXCWAVF-4WZkEXYFJEV7DFBXrmiziJUzyAwAQaeV3OYq_HwCs3dDC0QFjy5_0WqHC0khXxvMwP46_S8gJWYFZpOTGDACTwtrx9PxLf1_uf_FexIGaW_9pq3O-vZC_gryqM8cbpQu101z3yR_oPgstih2LPSDG3EOdrLllmnMq09OH3YlKoXgutwI8sF16AvPl3vnunv3XxkcbMB5fxNpSOqf8PA2OqcHMEVtJv8_z6A7YmfWiVD8Yfg7I89Yl5pnGZuHylMs_-yCkQqA0BLGtyTFRex8L91djvvEdN4fwKTusjHQXC9ms7X7WFnNTRgGxCJmqKOK0hclIn5wvk9RNndurcTeWp6vQLkClq4pzcAeF10Zn7LEem5ixWkxPI1avx4ZpJ9BNxLxCxBPcTSU92KWTeEdei76gSCHcL3_XjzXpe2OPxOBGgT-AXWOHBulW9zJLW5h0gvq0LSQjq9lFw0X08N3NUuqGE2M1eXtPB5fRQv0iT6phaISBFrcxVX4GgGf44yo6aeIAtped4v4D5XDa4FKm1f-_l5Gppraka05wsxeMFV4YUQfPp0iBBkY5FdNb_SZCq8h4TcYIKbMFIK0WSMcWLa06euqwNGnC28rXjKZU2a1rHSt50y8JNkWaZ28af4e-xKD40GY6wcjAuHxI7E9zOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIygHKwswmTnJOb8UtbFPh8BwZyZQPwzMt6mhN9-UvgY3-xaJK0PoNHi33kP7Up6Rcqt7PbzZ0xA9-sM1NGYDDM1ZaYzZcdD7GgGsJMXKqV8RnJ36-156uNiQHYhIoEByIecvZL354cmN6UWoS1-wbiy90x6VB7dVav4SRzDMv0ku_Qdw7O2Fj5MWgBtgKp9UnqQExNwfVHThPRVHDB0_VrMVPrLSiWBAYC2XOPu3X73ylbsNA3p6QsUS0fdZ_RXrW4kr0x-obzaTVUR5sAqwrdpsFnRWmJVvOU_21fi5tzA72mq6SILy7nbMFDedKu7XcfhsFU1L1H5lLXBnlXQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
