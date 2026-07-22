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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1-APUG1CuqUSpwje_NFhmGe6NtCqsogjSRqjraKND90VuA4caUrRNel7Gq7EG3PkPIeKOtxPyoahqdZCmW2rb1djsSsd9VKNiKmlZ9UL6xb1Z4Dejurty2sF6iEMKQo2Op0e55Xr5En4xqAWKc0PBnZTt_8iTCNmW67-8VJY_rb655_q-W52XHzPs-DcQuVgQ8EtpPSXIdGKHT76RrSiSyn2SSgZAWa_CLz19xjpZygsJUJRXbVKGNjBhp6Ltw4qkyeHODDtRAeLDKz5LOiRR1iXEvNu291hGLcskzxa-j7hkswhG4MJuzMLASmnZaKHs-2WO-Z0Mq8KN6hVTCkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbqRS81I6dl_3R8TOESEgEtB_rCrtsKUtwXDFVV73iDIslQZxUyIf4G0wCD9TGWicMj5q5sU4zEYBFFgzI8_xahUghv8BhJB8LH-DFXQJiggGCJHJwzC3oRHVE0B8we9V-I4ldEs4IHtAqkXb_mL7HCkbfuteJGbq6LZPaerZix1QI0XcOuS51ttGllNE22LKZaKeVrQRnlK2pymDzIwkdPGeYVergoSrfis3khPYj-6hvMnGl3r4eHRmGTmNiph2HRKbvczAtsZdl2XJKK1bIJ3wJoXsa5hwHJSLYU7TzEtlQ_ptj4JVexp4DIrOPR4EpOSKwWi_ORx9OV2Lw83Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCifBJcmvWNzkkHO9bP26HCXu905TdnULK3CVRW5o1ir4phaa8OrmAhAPHtC4nqP1M63iL23yVWPVZ-tlbq8T-C0Jul5Jz6AKXEiyZugBJXWoNoFI8btuFlECWD4tNop4aOi8eoXhBtEp64qp3ZOlDWxoSeDO6XnUl_1F7T-D9Yc_P_hYpCJ6iNQ2CTYfRdTTUN_Q3lZ-ujUm86bLL8gyYBodr_lOg2JPxhUqc6VvRQP8dA0sjMDTIDaaQSJhI3Ccz9VAz93iPEkBwKV47cc_KTDnaXp90j3-zKCxENZdmBowXsoHBOhsmvk4B1e1kd7Zd5dym2-l1-6Nn0GSCdi6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=iBjPYP0URPrKZ1JcOluBUzaQ_7S0Scp2Au7zY0OV7b91KqHRF-1k_HuI0pLk9U-Zy5lnDl10bS8rW8XW0pSTQPxENnHJEZMyEDmhPfBGH_R-CVpIXA0bYjmcnq0ds2N3nTtJKoZ5Gjlnoj_DTS2_dHDF0UXu1NDWD_wjRb1kDW-3azOSsbbBPdYLNm4sc4Rw33RQK962GCILyI99BzGXEjALEmHnAdd2kttLVGZIS93MSMOrbbzEFloku2Yr_0nrhHGhJwjpRcePw4ucPpOMEBy3pzq1YDMkO_T26EuWDYWSrDCZYQxtld8N3s3g0QLIU93BsgSMQ36KRtS2Ombs7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=iBjPYP0URPrKZ1JcOluBUzaQ_7S0Scp2Au7zY0OV7b91KqHRF-1k_HuI0pLk9U-Zy5lnDl10bS8rW8XW0pSTQPxENnHJEZMyEDmhPfBGH_R-CVpIXA0bYjmcnq0ds2N3nTtJKoZ5Gjlnoj_DTS2_dHDF0UXu1NDWD_wjRb1kDW-3azOSsbbBPdYLNm4sc4Rw33RQK962GCILyI99BzGXEjALEmHnAdd2kttLVGZIS93MSMOrbbzEFloku2Yr_0nrhHGhJwjpRcePw4ucPpOMEBy3pzq1YDMkO_T26EuWDYWSrDCZYQxtld8N3s3g0QLIU93BsgSMQ36KRtS2Ombs7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=B5BwTY_vmvGhV0yNyI2nPPouF6Fp1jB9IdNN0nN3dOmlvBTRjvph3IaqHUA4ymtzPRM7YAkQXABPZHNTut-GauqQLfC3XFcVAKQlnPVQtDMwJRqloBQPcPBibE4UCHP1cA_gp63xsiFHDQ8bLN53DTd3eBpXtPMBwbOaTXDNHQ7m79BMgi3F5yZMNaQR3TvvhV08dm7jJcPkqRh-w1afR-VuyCoCwu3Ou5G9AjC6LAEy1Th7kEu7O314mqdRDwcdL2Ifu6Lu0sYEkk21qr_7ENjiB5KPrFyaLicHB230x661NtStJ6hd0L56JkOe762bO-IbTU07Agqj8fUQx_SIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=B5BwTY_vmvGhV0yNyI2nPPouF6Fp1jB9IdNN0nN3dOmlvBTRjvph3IaqHUA4ymtzPRM7YAkQXABPZHNTut-GauqQLfC3XFcVAKQlnPVQtDMwJRqloBQPcPBibE4UCHP1cA_gp63xsiFHDQ8bLN53DTd3eBpXtPMBwbOaTXDNHQ7m79BMgi3F5yZMNaQR3TvvhV08dm7jJcPkqRh-w1afR-VuyCoCwu3Ou5G9AjC6LAEy1Th7kEu7O314mqdRDwcdL2Ifu6Lu0sYEkk21qr_7ENjiB5KPrFyaLicHB230x661NtStJ6hd0L56JkOe762bO-IbTU07Agqj8fUQx_SIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=PwVIZeCuwabU8Gic8DBEQ-yzclXtpr9c6pBmDATeAgfSPrs8hwtD90kXcv3urWDOuIx3X1cx8BR29ep2BnjAZFevljaw4a_kBjaTEQoAMgjHAa9xIyIP6HQ1kmnrAE2gaDYIZNYkYQBB0deBCSYNnu4rW0T1YJrlCwkLyQuE22liIAw5ErGhABfPAdmTSvSNcCybDEJFanc76D6ifkfn4HKQ-t0CUswDBAjhqewb2wXln9fljr5T2ENeAddAI2wVw5PhXzlLyS6D_ANF4mcKIIZ4vd_rQX3rYilVs1iVWIaOAoAwz46-jOX3aC_DPZa_L2v3AyZ9rBHrmHhuykM4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=PwVIZeCuwabU8Gic8DBEQ-yzclXtpr9c6pBmDATeAgfSPrs8hwtD90kXcv3urWDOuIx3X1cx8BR29ep2BnjAZFevljaw4a_kBjaTEQoAMgjHAa9xIyIP6HQ1kmnrAE2gaDYIZNYkYQBB0deBCSYNnu4rW0T1YJrlCwkLyQuE22liIAw5ErGhABfPAdmTSvSNcCybDEJFanc76D6ifkfn4HKQ-t0CUswDBAjhqewb2wXln9fljr5T2ENeAddAI2wVw5PhXzlLyS6D_ANF4mcKIIZ4vd_rQX3rYilVs1iVWIaOAoAwz46-jOX3aC_DPZa_L2v3AyZ9rBHrmHhuykM4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6kWUQQFxtbyUTA9LcP7u09R_yf4130RP_WcEPyTLY2E71FA46qcJ7yyAfY5QX-1Up7cF4hXpIDr9b_Mr3UZ4pm8fFynFshIACXYgA2wYWWTu6rHu0b-x-lIarCpl65ApvGAbMC2UoSSpPG3EuOKL8wEQSbcFqrcr7-s4lxubGM_WO2pg_agZ85TSXd0HIUO5tN9pbeAqbW0Us4uSyjISl2b9U9jGQb5Wn4M35yyx54fcdPNdpBLUbePxXyQj1dYo194cICPtk2jEq4spOOdWQKwDOllcufsZh81pc_g2nAcjFI3mTGFsW2VwDMSUFrNKO15GHMldm7Q7EI9XX4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=s2ELUiVkksmRDGZVsgkzTdq84Gfj0sqi2NxVSROPEarVbD7ZucImPWNYAbXCcv7l32_xyTV_N7r1D7dwCMdgfZfbd3I-uCLGBvTFUeA7alaWpQzvAq297W3hNxD2VcMSi8T3PHSXYXEYSte_gi7S-PJ_WWuPbLDZU2v_MuR0zArGCyE8LhX8MmxWM7CjbPEN6_XbJgt4yQlLlB_N3tSQl2wFdJ4TgGLNUhBY2SiT5YeTA2nyVTv9bJVpoRau7ymuA6bXqYYSzj853QSVf936aUurwd3kSFo3oFfppnstImK2pkEyb-zZRgISC32o2HWCyNzPxnyyy7SDAQ4sAXtJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=BVXeKVXuv0DKoOnb1d0I_qQEX4reB3r72OQY17_-g1WAOAPFV-2D7nd5E8ODt00N-Ca2b1PDWtGk1MqSyPC1Euvu8jpAhZZtonWiXTMzLe2TkBFoNw5NzfvlfEePisrI7AIb58DH0JWYcXDg3VjIIyRsxeoKScz_qLH_hoI7rsQTevn1K_ZPPAU3qsGDfDx5s1vDjLGiig01vFw-YvCLCFu1iPReKIsUWa3o5aT-h83MUynpQJCDJaOLuFuHRIFk6pVfM4jl-ofz8q5X2zIU4PVqwN5vDS4Ug68n1vR-YZzXdjqBJLNJAZydonr0tbV2QWHg84pNaG0GuHGDAQy79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=BVXeKVXuv0DKoOnb1d0I_qQEX4reB3r72OQY17_-g1WAOAPFV-2D7nd5E8ODt00N-Ca2b1PDWtGk1MqSyPC1Euvu8jpAhZZtonWiXTMzLe2TkBFoNw5NzfvlfEePisrI7AIb58DH0JWYcXDg3VjIIyRsxeoKScz_qLH_hoI7rsQTevn1K_ZPPAU3qsGDfDx5s1vDjLGiig01vFw-YvCLCFu1iPReKIsUWa3o5aT-h83MUynpQJCDJaOLuFuHRIFk6pVfM4jl-ofz8q5X2zIU4PVqwN5vDS4Ug68n1vR-YZzXdjqBJLNJAZydonr0tbV2QWHg84pNaG0GuHGDAQy79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s89ebKDcp76oMXgG9_vZQLvJ5mqa9WvPskX8elt1ydedxxxXEuFDck0dbpAuxRyVG3S1Akh7CSfV2jv0DuTFw4aNr1vfKgw0lV-OPYp8F7D2tSNSHukEu0E2JTi-Jj7Xjbo3AXioxTSJVG7xBtgUWF6GV5hrcKVw5Un9M43881CJKYOgG-oLzaClAaY39uLwvBIxcTYukLP7S_flsKXVIM1rNln2bGawR_KTC0dO4SpkvGnJEcd5Cx1W4EYlw0bUkHYONjYRjeJjgy-PNyL3OjGXcPHgoCgnaeCfD061kBvpNx5KKHV-dUXLxtgPolAQS4uRw8u01rgEuqqKwof7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujXq3SrrQISOZetHIihCddqaNsDAkk4fZCxwP6JUBpeU0WFiO38O2C7SjrA_DO6OhRPctrlytlncp2sFiGISqko9VZjOd9LEWTco3D1WXxAgJ0PWIL8_wB_2dCGP-nSWuPDt9LqmChYiHSruvnDGJoCJIppId6YTqhh6_kCLSEBhTXKlDgiJF2pCsloAyI85PkPVki_igzlnzB7gAg8qTxEQbHQgJFhbbPwrAKziA5bzy6jXwtUN_4H5tvtWLF1hE6q84mqwV2em3T9y1qKVHkuBHY1bYwDm82tXV1NAVONoYjL7mgWTmXOC7zU6l-CGe7TlLsYYZxBnwngNrrHnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=tPgf9fryRLJwYFsx5AR5Y4s5YHPciZKq89e-1d5ufpPxm_E8MZIbl8C8KDbPr48971tdhGxvJFm2G3dEwW3IyrSXxwFUz_K0q7GS0IUmYXbPvCQ17GinncNJx4kIv31PMa-Lzs2TLTef_k0PcTV3XFOVz7_IMisFsY8HLfzmDUsRmSnRcLGjm0PMhb_LYVsx_f6D0fo-dHBBOoc44eHATnSQ7RT32I0txUdNBVvsnhpMEX_yvhOGkMvC1v2Zkul_2NU2HjACqUpB9bbGicRv1p54rQ9HYuenXVAgYPSm4SC5sn5jo0sZuO_M5VwmflQCUq_s2UE3oiNrNubFuKKflKRNpnXhnAutvMOp0dqL_xWNe9HwIg5JLkawc1f6P7BKkrcbh9UJeYIA0Lybl8GVfzD6cctXDgK63B1NSjFvnBBGm9V6FGu2aLBq_l3v2-da4tUtucxA-KUrrjQUwZ8gGhddRmOEbidzYi5PnliTBnnxkRSX4rB03GrqYzjYED8haCnEblQsZdqkwKI62cEJxFNrJ7ZZb39FTQnDOxSoNyybNp083FiMcOj7t6a5mVzz7Au8vfH2Vu3PFhwYu3xsCDVVEOeUIXVYeSO5l3FrnwFvna6CPb1Rgviqg3hOOmifXAaDzQDBupXY_FVpBXt4bI9j7izxYCRpQhsxYmhi7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=tPgf9fryRLJwYFsx5AR5Y4s5YHPciZKq89e-1d5ufpPxm_E8MZIbl8C8KDbPr48971tdhGxvJFm2G3dEwW3IyrSXxwFUz_K0q7GS0IUmYXbPvCQ17GinncNJx4kIv31PMa-Lzs2TLTef_k0PcTV3XFOVz7_IMisFsY8HLfzmDUsRmSnRcLGjm0PMhb_LYVsx_f6D0fo-dHBBOoc44eHATnSQ7RT32I0txUdNBVvsnhpMEX_yvhOGkMvC1v2Zkul_2NU2HjACqUpB9bbGicRv1p54rQ9HYuenXVAgYPSm4SC5sn5jo0sZuO_M5VwmflQCUq_s2UE3oiNrNubFuKKflKRNpnXhnAutvMOp0dqL_xWNe9HwIg5JLkawc1f6P7BKkrcbh9UJeYIA0Lybl8GVfzD6cctXDgK63B1NSjFvnBBGm9V6FGu2aLBq_l3v2-da4tUtucxA-KUrrjQUwZ8gGhddRmOEbidzYi5PnliTBnnxkRSX4rB03GrqYzjYED8haCnEblQsZdqkwKI62cEJxFNrJ7ZZb39FTQnDOxSoNyybNp083FiMcOj7t6a5mVzz7Au8vfH2Vu3PFhwYu3xsCDVVEOeUIXVYeSO5l3FrnwFvna6CPb1Rgviqg3hOOmifXAaDzQDBupXY_FVpBXt4bI9j7izxYCRpQhsxYmhi7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBjHLq2I_bTZp1Z53C0LPECMlAWvE_ob8oCAu813OOFfvXIZfCmoJJ_BnsraNNh04qlkAflVenYLIiAm1rp_5tfSpPEYz425UsqgL_-_epnqJ3GE1LJXdTIM7i_ZBuNZ-sv96XUE5cq01hasPvyy6gF7NIdRWiBFK0CLlmbPxG4R6go25sXcenQpT8q-_NrXZQJF8HbFTNJA7-I21F4BfnL3WB3u7L3SPgmwrj9Np6q91RkpPlbATNAFls4XDn0IdjQVxJzct6DwODCGKDYlPo0jlBGJalyM0hVlzriyuPULHrBoA6yhORGHDP9_6npuao2HV2KJlZw-Xua8L-_1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JazgJx7v0qdV3jTEHo-lMcyHOLxitpF6ty9oC7ZV-qxCR9azCjs09hrs7pii5oc2hhX9-DBFRyo0lm7OLOzgreL0ZS7pC4s49sflXs7Lynl_PRtGeSgVCtuL6DRlEYsJnwDYN5I2B4pW_hdo4b-61vy_wMXXCfyiAiDbxp5TsRuNhZETUblxxTw88vjwwSKjmzTMDjm_6mwzC5V1tKuvT57E1oxPfOchbOO0rDaBbiQA7N72BjEuNpylKLJBFHZxSajxgvffkeFox3psJq-m5320zKZ8fQfSLMUuquQD6OiWyxySAkGslHuu6NktSaR1OqkG0hmDKEKAAV3NN9J89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al674wTtbE9uPvD7g-DAlXW8JC9chJBxR0iy82Alhc7ezGi2-0PdizKgorWVWBxXWCGm-sDINQvB_nbJSal5cG9EoGmiOCHu_ktXD7AqpiD3ajfRzcFCaXIMddZMs2_NAnRhU89oky0GDd6OzBAqXdkSzoPjlDezc25FTDmlMvtv2RnRWPU62_zWA_0atIbRiNJo1fQAI16IuvT4ZWObgHptBvesH8lL4iGq1zzmBzfzYUaw3PbCWXKbhtN3cEzdE4Yw8bTbJbXeGIKOEHjQ74tvkJhRuLs399ljMcCdFGs0jzb_sMlJl8yHpvkA_Wg7LaKuC-kDYl0VHCndUi4lZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmqEKrP7Qdfb0VDpUvE_QztqBVavOgeURphG4XxP8S56ZG9WXlLM0EdesfV8jk1envwIsDoKccPMnCXH1mN_RH7sdP7EtMPdEEqHzng3jvKUv72Gxu2iKakiGlUKWHoPVoCNOwQ4yiBMVkC5GmcusrsI_hcsklCguQgro2woluxEFrvxvhSsa29ghLvLwZUJwEyDjOSwvQ9mZ16gteco0dfCn4wtiwj42axsElcBUZF1daJT1TuTcxSezK653m2U7wonaelcFmukqK5BMRnFGUoT9DKkqLksyBFEODuS7IWk2SB_KM_E-t4k87Om1G2c2pUkuwag-i1zSaMRAbP-4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=fE6qDwyUJV3pkFHm_YkEik3GSPIUuIYcz6G1LKvU-ZOcG9Eh_u0xDX2XrLNlp874qzhdUSkpjFR4fZ1bEmZX0oLcvQX7jTKWOmc6w7DMwWCmnix8KqkoPe9guU36llvmOX0Qzl20w6Bw3enZkFCw7fGVMD_GEscDIwXO59Tis10VOEOgSQkiFYwBwCcUSVlQCOzvvCVXdSBVsRDBBd-ZdwYScIdk8nKZxQAx7GVNubQVVJXSkWBcWU-4Vu4MI6yPR8Qy5JQVRWxOlIkvgsySCWQAn62aG9wnFetcLACTXsBE88yawZZ1T2GBatAn8j5nBhNH_UPEk9qnFPak34OIRUDfFXX3nt4pSCEVZhc6xLDsU0l_BsugcaDyazPa6cy29TqYEtkKex7w3-vGSEnHmRLCThF0dzZiVRTdcXDtCDajzd5Uj4Ucfe_WzIcrVddnVRqj-CKDbOaUuIDuhQM17ykZUTwjmlHN2hksdBWqjmdPrqRuR-j-QpZZofNQOm1_Penv4_3wda98psBpGfPMrF6IX1aHtQivAnQXtvjYVaiqaOofBvT2JF-qGr217CL9ZFbphudYUReXzx9y45zoi2XOyW6Kpo-vHSyp6KsWWHQAKSyZrBxgCI6aa1ZVKcz2ut3AS6mKJxORyuZxufsR7_K-pD85di5iGDZMVJOXXIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=fE6qDwyUJV3pkFHm_YkEik3GSPIUuIYcz6G1LKvU-ZOcG9Eh_u0xDX2XrLNlp874qzhdUSkpjFR4fZ1bEmZX0oLcvQX7jTKWOmc6w7DMwWCmnix8KqkoPe9guU36llvmOX0Qzl20w6Bw3enZkFCw7fGVMD_GEscDIwXO59Tis10VOEOgSQkiFYwBwCcUSVlQCOzvvCVXdSBVsRDBBd-ZdwYScIdk8nKZxQAx7GVNubQVVJXSkWBcWU-4Vu4MI6yPR8Qy5JQVRWxOlIkvgsySCWQAn62aG9wnFetcLACTXsBE88yawZZ1T2GBatAn8j5nBhNH_UPEk9qnFPak34OIRUDfFXX3nt4pSCEVZhc6xLDsU0l_BsugcaDyazPa6cy29TqYEtkKex7w3-vGSEnHmRLCThF0dzZiVRTdcXDtCDajzd5Uj4Ucfe_WzIcrVddnVRqj-CKDbOaUuIDuhQM17ykZUTwjmlHN2hksdBWqjmdPrqRuR-j-QpZZofNQOm1_Penv4_3wda98psBpGfPMrF6IX1aHtQivAnQXtvjYVaiqaOofBvT2JF-qGr217CL9ZFbphudYUReXzx9y45zoi2XOyW6Kpo-vHSyp6KsWWHQAKSyZrBxgCI6aa1ZVKcz2ut3AS6mKJxORyuZxufsR7_K-pD85di5iGDZMVJOXXIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=a9nMke21okPGiQUmgr_y8Q6ZmP6z_mWquvOFAeyu8XKDYHVweFO4zosWATfjVGGCO5Xtczm9xtrNPjucI1NEr7htODZR_rg2J5lszBpBlT6H8yqGV_mOqRqMdDeGOiVvAmBoI1A_OEZbSxPL9ZGqM5cCvOYnKJY6W3EFS1Fi5Iqa8FW57SV4zqJIzkrcwNX8aIfjvJ8S_2l6t82oMMg2o_-fZjsZ0V0FdpuQidiiMtdkhCqmzv3dddmXbwwHg1YFW3nNdStCx7ga2Qa6eQmow5oFhyPPDedhwq8MusnlLDSJEsGMPIn6R-F82D0FpmGWuffrb2IkOG6JVRsD47wY0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=a9nMke21okPGiQUmgr_y8Q6ZmP6z_mWquvOFAeyu8XKDYHVweFO4zosWATfjVGGCO5Xtczm9xtrNPjucI1NEr7htODZR_rg2J5lszBpBlT6H8yqGV_mOqRqMdDeGOiVvAmBoI1A_OEZbSxPL9ZGqM5cCvOYnKJY6W3EFS1Fi5Iqa8FW57SV4zqJIzkrcwNX8aIfjvJ8S_2l6t82oMMg2o_-fZjsZ0V0FdpuQidiiMtdkhCqmzv3dddmXbwwHg1YFW3nNdStCx7ga2Qa6eQmow5oFhyPPDedhwq8MusnlLDSJEsGMPIn6R-F82D0FpmGWuffrb2IkOG6JVRsD47wY0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0gySWFPVyLvhgj2sRSXqWKD5O92LRGr1Y8eIzsESGEV67sr0LWYPTy4_FxYMiB24dNqLrn7Ebve5Bs16RH8T9njdwuBK42nEGlf1pu0f2b1WULwMjunrvlfOffoOmbFqjlL2VgAYirS0sE48vf_kl9CWvLnAZPkjXFnL8Ibv8SizhVQgj-Hxdsfh3RuDTJW7aNU4V7NVdgZMqQcMzUejm13-qY4wNagfRtoGdQ8CwE_2z8HCpgdxObPjMDay2fOH0Tg00Dp6UdJ4lYCxKKzfLTOnSP-hpboYj8sUFzx0AxmRJ0e7NBVCiqnDlz5hqbSlDI4AaW4txwAJlcBKkVqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djpj7AL3b1PYh4Vhuw-4YU4_hKw9XFXdO1bznBuFryG0Q-FvZf-XUgaIWsGBBGGuT3fBZJdOatla9O5FWHTgMjlnF7a4GHfSESLUStAkRWx2OoJ6-kPCn2o-9cxU7TM6DKelno7_FSQ5wZyQAiS_2RY_5AQyGyljHENwHsgnJNeUh7bJS54OrVNcf-U1bTUV-jZG_2crDy26DmmzxL03Ewf_YSc7Xe8_w-duCasJf_kQy4I3uF_PkgZxLoTANgn5im2YYM7GlOiZsAmKfayVxRh3KPW7KJXUpJaEtyybMUUC3oZR9fcEGBX0_YdeLu7TugG20GdOIFPMZZwxYDRWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kROtIyNN2JtNtiRo1cH-UUyXTxiiK86L6jhYNauGGG_6opwTYjcGts3jTqaHh1pL9E1d_YrYpH8v9GkOibRFCKAWrewQqOKnVKSLZokNgbxIeUkUvH3XsqwDy43HKpaZ-dYHlI2NtNsAe_KyqhUAngq8KV215DPdGMC4gZfYIut-sh0ja_v6gdq30nc50_gtfyjtR6uW3jQYEx_RVCHTT2OIhWNVTsaciaz5oUkRSJupqx7iGTuYt5eghmwKzvryL5IkWfWhessoVcmko_zetZwrtqLZZ6hhdLl32y7GFALNJOl_Ig_UHkU7qOa_rDjTPg_jS8T99ZacpPbC59_gng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmHEZBai7oUbZL-dprWjmu4osxoPCserZ2nP7IV_hk46QQacJvoYlIVtvKpBVDp3LKZ_8dJRU4blMOaIswUf9Z30g8S-Bgm2wY0Eq3pDc1hB8K1d41UUFlLQ4n5AV2WhA3hSi0k9fWePfxrgLBMMni4EgdgvcwybwmBGDnALD2BBEN1n7KfOah0qN3dMoYN76JutXGVmTdSaZpsQqyJWRrBMlbIMJxspA3phJrRjKO53pUA7XXWmRgHWBsOfm_O7N--UqDFOI3sCHszqBwC9W06QBb5m-UjWJl2VyPr1UKwjLTVPn_cgD5Kv8Gtyn-LHE2n2anO04Q6113LrJAHJAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYZgYmlULCO1bHOaLlCZh2bLq-nihsiut5IHwqA6VHKpir-8PYyswOjomC2PFe6BNGKkRn6MBM79UjLmk4fusUX8csI_PvrvwY1bLht8UZ6xEyQe9DujJD3MR_ZzlBzeGB1OOpxxeAfCIyVvVGb1VrG9MmsXy9NBHbJGQSrB1kRjxK1A2R79EhZW9rhxDk8kS0rU5KqXRSZEfwXC6FHlXpmgEL096G0_sOYmOBLr50zZZKlUjVOR3Tk6ypJRuCfr2vfw8AKnOXOtTNyQIvRGZHO8WDwlCCVzJXBMsFzbZlOxFzx-DDJp1WL7pLVnSsK-mQovPynUYTnq2pFRnRUiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCz4fdajhBwcJxOSwXHEZlefgH9qAAHrZNP74dd1Jyd6TmzrNWie1Qyb7smHM1Fuod-idF6LwaXy8eaE1V5jW2OIOw8PxiNaMFbJl3N73HkL4fix85gcFs4HsBp5wNzzbUcZ2ngvr_8g9q039xEcx7LuO6XFC_YgUtY02DxupETZ5C6BkFRjk41NSCcKMFze9jnKYwlC31uyCLxdlr-kO_-fAdcrLKlfpsOFM0gpxhj-e3bG-0cyjP7W1IcQsHZCa1EGR9C3kFvBGKzYfqx7HFdCukIiuCMG2iOfPviFkjBhYO_4qeTEDyM1VV5s5HoxNyweS7_CZqLuMpC6r6yZOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMCUgYfhhWe02eD4HNOI7UkAkrVVnMc-0_RyhdM6qi4rYoHJWctao42e1OqkdAloCoLk-cZGBD5NV-7gBWK5hwDXnSBtWfPjl9C0YcNSv1aLXbSH597XlFJUrRAvt093yAnmkKKEMiKcnYqpdA8f9a3hbzP6uUDJTGXLnZP6_mj7xoLKI23Sa16nCZTPWWid1-v2mGhPffTDfTP6KBri1ECyrXaiMZnU3Mz6DA20W-Q0wLT87_iDRNE4T7a4CAdoVBT0om08HbC-me7KyW296QacrrgbWZ4iu6jJbjrzmJsL9WOdyCmXDpMmYQVHjUMq6qKqovS2BlJC9XAT3UTeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=mpq2yk4dAkXo-KtdjAMHYnkWmCyd0xAzFPwVmlHLmSNgMeWJIEvRzAkxG02wtwsT8yF5EErt3I2mTgbHkOZU731LjBgh-FaL9TYzroryJ4U4OpGOn31zMJnPKyoJH5CdqCzCL2jTsD2SheLU6GhXNHWlWpMbYd50yUDr0XcQeBXRZLnpI8_3DQiF18QOntez6nCqwa87SwA-MnnIodPRUntRBTb8ATyiSQlVge1I6Z1_7xFGwIDLztm4Y_S7GLZGWb2MUPBbASg-3F_xtym1b7ZU9f7--AgkfSou6iSfNSvzpSlXA72baVFfxuzPlR5sgxUOQSc_Rx4BETAwkF0jsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=mpq2yk4dAkXo-KtdjAMHYnkWmCyd0xAzFPwVmlHLmSNgMeWJIEvRzAkxG02wtwsT8yF5EErt3I2mTgbHkOZU731LjBgh-FaL9TYzroryJ4U4OpGOn31zMJnPKyoJH5CdqCzCL2jTsD2SheLU6GhXNHWlWpMbYd50yUDr0XcQeBXRZLnpI8_3DQiF18QOntez6nCqwa87SwA-MnnIodPRUntRBTb8ATyiSQlVge1I6Z1_7xFGwIDLztm4Y_S7GLZGWb2MUPBbASg-3F_xtym1b7ZU9f7--AgkfSou6iSfNSvzpSlXA72baVFfxuzPlR5sgxUOQSc_Rx4BETAwkF0jsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLOp6vjv4qut4OjYNXJEJG4FEomS8X8jWjv3XXqkSy_1DRC3zTEYZ0a5bt8RJ6TBHzZSnoPV0KgkG_8KL1YCaCVEzdmZMSq3MyFGD61cRQgd6hVD81Veu6rrquYKiegkmxJknnx8hgZkhW5h0VK9dXbLw-sKRwBf-xSQ16xU0N2ScVpKB4myqnVUi3ZW6uOhnI_o4Gzg-8AA55UHcETkVI2Nvbn2he2_11mnjhkePIG-nGTIB5Mfsp48A4A8V8x2abq4mYQOnlKFNG0N-jfFIYCIp86GuqBAVEHo-hKszlIQMSDHjLtp3mWapoe31GaxQO1clrfH0YEdQwYMuPZ-Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFSvzpP3wjNfKZgARPCA1Segifd2LI3-G9noC6TV0051JY5cBS9w-hvPCanZHOjM9iY1pap9buO89Qo5xaQDiEm50pQCfEfQSG3unni75PBqsciOBKDL___cufOddLJXjrb-V1GRLMp3VEdOdj7HpM197z6lY_U6jtyBI3CasOPuxYOXphH3QLfqq8QV7yDuQf3d5XFeK_SNhx0FA40EjnsQI4fWkB-OH5nYVsc8QPopGHu_RSkgRbOOl5QyywefrHNqrpllE1TKZO7HZQd3P5IunG0Oq90GpNHq-HEyMr6aOcbWqz_92cj0c52hftCK2dbCMxFdtTQLDy_oHenFKGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFSvzpP3wjNfKZgARPCA1Segifd2LI3-G9noC6TV0051JY5cBS9w-hvPCanZHOjM9iY1pap9buO89Qo5xaQDiEm50pQCfEfQSG3unni75PBqsciOBKDL___cufOddLJXjrb-V1GRLMp3VEdOdj7HpM197z6lY_U6jtyBI3CasOPuxYOXphH3QLfqq8QV7yDuQf3d5XFeK_SNhx0FA40EjnsQI4fWkB-OH5nYVsc8QPopGHu_RSkgRbOOl5QyywefrHNqrpllE1TKZO7HZQd3P5IunG0Oq90GpNHq-HEyMr6aOcbWqz_92cj0c52hftCK2dbCMxFdtTQLDy_oHenFKGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vdjYCN60Gbechx_uYuGVDijB2Db_wHXKHCFczhl82AYslQH8ECJp2n1vtzvJ5lO_2ts8jua6qzU77FC4vweGFcll3yF1hPonBqp00HjrPbBUAIFiEExiipR-XTxdPzeNANiJzwKuUupjlh-7sTDcgYpXbE8MdfMNtIbSgrKMPB2hpKfZHRqwW8we7ai5XmAWkgNtHRofGS0P3pGuvdB875E25T7_BUEZfXu541ekckZh3iFPKtoZ2bRSHfgF4OTpXf2e25YWMun09Q7eA-2mpNbOuza5WqTVZ9dXZn5TGV-P-8FddsUXVoLhab82LrumYhA2J0CZJSeHyosnDeA-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vdjYCN60Gbechx_uYuGVDijB2Db_wHXKHCFczhl82AYslQH8ECJp2n1vtzvJ5lO_2ts8jua6qzU77FC4vweGFcll3yF1hPonBqp00HjrPbBUAIFiEExiipR-XTxdPzeNANiJzwKuUupjlh-7sTDcgYpXbE8MdfMNtIbSgrKMPB2hpKfZHRqwW8we7ai5XmAWkgNtHRofGS0P3pGuvdB875E25T7_BUEZfXu541ekckZh3iFPKtoZ2bRSHfgF4OTpXf2e25YWMun09Q7eA-2mpNbOuza5WqTVZ9dXZn5TGV-P-8FddsUXVoLhab82LrumYhA2J0CZJSeHyosnDeA-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BWfIjRgXAhsxhVJ--aZYrl9I5mV3oW2uhgEXv2MX4fI1F16sT3I8S1N0yOv4fZjivJJ9yMRiVTOJU7erlJsYWoYgbo-QRpTo1nz2_hr0glojTS8FTWm9x7qofeA4n00lpF04Bijg-OGBHZXnii8-YMrZ7EZ1g9wgiw-LYzwscOB1w1K_405EhJfDHqXFe5p1Fom53t0OMIWrrPBUAzeI4zKiNudYVV8oppKXtPnHnEk4WiFmLADPngOyn1Cp5qwzJ79NpSyNTLkmAEPz9FG3WQjem87T_gOOcSgFvx0EHKdgm5bsWMKf3HP0WEEutNqgqrXvrCM9voRSfSquJxuu-7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BWfIjRgXAhsxhVJ--aZYrl9I5mV3oW2uhgEXv2MX4fI1F16sT3I8S1N0yOv4fZjivJJ9yMRiVTOJU7erlJsYWoYgbo-QRpTo1nz2_hr0glojTS8FTWm9x7qofeA4n00lpF04Bijg-OGBHZXnii8-YMrZ7EZ1g9wgiw-LYzwscOB1w1K_405EhJfDHqXFe5p1Fom53t0OMIWrrPBUAzeI4zKiNudYVV8oppKXtPnHnEk4WiFmLADPngOyn1Cp5qwzJ79NpSyNTLkmAEPz9FG3WQjem87T_gOOcSgFvx0EHKdgm5bsWMKf3HP0WEEutNqgqrXvrCM9voRSfSquJxuu-7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1JOYuYT0lgYzRGzewgjocGhv8AYxuj0-eUS-FTdPL5TkaLc8KbMRuclhNGk4hbqOANFPwoUNU6BH1hDkqt3tvOZauu8wymKFOc7m-6oJR0z4xJ8IVUHKNNS_A3j7tSs5LZjXwd_7YZDuiSg8jQgU1zWr6vzGQLmz6xvOmqiYrXdMsuK0L56kXA2tfLKWEQsT8yMQeflhthKR4yLldiTiWREsSbPjihmlSvC1ClPi6tfwflyonk6UFppGCMWKcL6RIz-uevEkibPYUzC550UVKI_2LYZeh1uqJA63QM0IdbtinfDjJIqLXxGKKE5V_KamzPRToXlqDDIaIk48Zx84Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZwIchU49U2Hs6DHaz5vOaycLj14VGoDD8C0zl1f21ncSSJlGXXA1RIiNo3JAaveU1rKFc-exzAjAxB7SBYr7BfhmHPbBCI4HxFVoJv_aEW4YK5Lw7eCUAfkwe8IOD3yYPmKCN3MuBHtdmlsQzcQnPp7AHasFForN0FeJlIDm3wXYN11UrsME6MOfi1trfT9pVg9Ly2mlkD-HmtTawLd4S-zhhxzXc-cdQykyl4S8_qdGdecPn3QRjobsivCSDJr3P-K2FQ3RPt6VH37m9aOcW7wn5anutPa0rLcDCipV6QeUecklR24DicKvgtD9bG4zurUuqyDAxDsxTMZDIehMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYwRravn-0uq9kuCWaeTT8I2DFTB0OAwFXNNWPOa5Rhk0kgO_3G60lHC8ZaxOXeCbEcY--ugwwANRmz_z3oSeOMp49QdHWjPMGwvmoIK42wPgQMZf-Ilgt5B3Tidzsr3xgniFS7XH5xR2IAJwiXkOxD8v7nIjEtouCaDGTh2NloCona4dz0c_E3WTZs-B1Oarq97--WyELLRYKq9VlTOUQIZuEx-DaUsrZmYBsWjRkMlUsAv87uT-5zCOuLdBj0-gG5r8ToYNZMbxI8ezbuav8KimvluUt3jXXstk-Hs3w3WadMi6hQmA5tqaBhlOtlI-9YmK4cwZ4DWD5gmuwE_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2YpLOHIqgjg2XIm9AIkXTGEvVn-mx8mHF-O4bSPs4kD-PkKNl0NpS-_SnIMP0mUF8YkZ0MgMkdFHqzcHW6GgnYhQcdz-OGIIgBnSOKYeD50bTIgJhBDs1ZabljMmJPgVzdxPKGQ-27ktinvLDbHGIv88aVcPS8pX1DFBYhJqXBTSc0HcSFoaTlpGvqoJif4VxWpAdzYpizRzL6DZxYxyV5a8dAJ9MXAV46Ksmp5CYcqbhXhDV48A2vPuoAl5hqON_sHvrRofg2iHQ2foBlDo-9xCIRLtlhNLsZdbD-pXtAwJ6LGj4pGoHntMW3RCMdu1lD36wVmKxcxtWLsVhNkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPFJ6p6o9FfNputguzvKq5A7Pkx-QjXlLJm14jB7ykzB0bmNbGYzIJhjuarRaI0uLbH5QHAF-Hl4DydgtZkPG3P-i86hQWDBfpLwvVRu063Drv7HiISwSDbIYGwDV6yzExJtPmbUzcaOX_HTMZBivWd_4NqYh2NYwiN9BUsKxdcdsFk1naJlv4vQVCHeeB4IEtmD667XX2CPNQRUdOBO_-lw6X5Arl88x-br49BfRoH-Wr9TJDk8yjh-rRRoJFBBUXuZV_QLzhSw2wMFt2-bulAg1jSJmsiSvnIxuv2sN8vVasjP6gqexZt8dI43nIMpC8aI5DpExXHCxRFYmcWedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXa4fOHunOOYKnvVZ95dClvXPcZEaPjxgSokX3YBc0GoebZ4MTQChFKDAphsGAotDt3xKbMPwNW8vXs6Oi8ACNsyFMtc_RKT4diysJO70JSHAyTxPkamPdf6XZkjFxRURsZwLlZJCcHmBCA9E610XkOn6vxTg9hXyVuIZAe9a_2FRZGLbXdxHNyv8luv8jEjEZiDhs2crO_19zmnRG4qbHNnuV0HDc-LQs3cfTbUtzVxRhCVQse1hGeIB0uZT1TZ8xvYtND2PCqef0uGTUGbmjePTXFwbhUxFwcWwTp7K_mRpE_m5oNbH3VLqTlpjvTvaPiJ8HnnbwXsxoDrWMnbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POfiJ3dcU5zui3d9pr5aIZf9aJ-feCo2E-1cxYQL-tn9moIR2RXE31ulk7EvwM_WZvu5ZAvCxEGJt_2J6fddz42_7T5-BDSXudgwUiTxhNvTKxBujCDBcSf21r1fEijooF2KMCb4kXAXinIS8_vhxh6K6DPS81R49aRZiVEcoibbKxSfzbfVYfKL6WUXLkgUy55DZaBXdY4AOOdvM5G6dZQ06SfpUobFvvu_SCjcBrUo8FtrwTFFjlNyhxP0VJOmM1xgzY7EOA8uKGAdzUlFVIstVIP-U5Rs7TN1yELfEJkAMX1vKVxRHjnxVji9z6EaweZ5RAJPH00xMl0rkgSA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_Ftw3482Ttg8q8ISXzO-R_lCXXW4z8NBfk5Mjf6JQptfWWSNhMyIgmps7MTTxiFPXG543EJVGMMnMG6wGlFGAu_HTI0wT2xxNX5oZWOw3v45QyT1iQujKJqnYNiHhUSGABgkUyDIT1f4PtD_0tQZWQlrtyipLIuKNkSgYGVYGYQ1pCzeq3-UtDAnfZ2Loq2xYRyKN6FQI_1wKYgoHq6LFP39ErEzzrWg2vBDNnvKp6ZkXfa2JGq1Ael7Sgc747PVBgHczX8NDD6g7DQ9SoH7p4abwMniaxLG6THfa2h4M-qeqiDEjGLsf_It9nkkijIR4vfh0G7SM2PkzgMUrzBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgB8Hj557LinztmO_ymTg6D0Ez3pQ0bLjLy7PHFvbWoRF4XMl-2oKJjYg2LW5PZ9e7e6CQvBaOJJ8t4nbQcSGISvOVLiwXRxbpEH59N50kBMUhdYR9cBz3AULJn3wVa-XZcdwuPAhYgkUnkSoQvYf3S7zqGTDxky6zTP8P38p25r3cYPXG7Eo2vDcTgIzZ-S5yBUA5UrrVc11KJivkNBsGTqJ9T_FC6ENNp7t3-xuaKdhMZ9I8eLuZfIxDpBmISEvtdeEtRug8axrLCUKeY09cW_BbSCtd-NpgUbpwlmrbBXiX9Zt8V0RcchNfmC7UeVv12hwL8w0jEsIDR6S6vqpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwND7_LKMOTInA1JOdKpppfQK2Q4WSicw7A9nPyNWRQ3c3XOrJCypFbUQwYQxO5hRrnzvTBrSt4YDSD5vxKiYhkAGNE0CUV1cdPpkCP0t2LLwDAwsq6qAXAo-1Wu7ssTjLxvK3etOPAZTDa24_ouFDskGYjZNVDOG8whvIYOijRgPml-YcclhJ3cMzvnPCi7UzREjQg0n5ac6ott_EoUGgjj9Q6BsKYPQVyTVNIK6dEFNK2ndbm8oitbi0mJexOl5VTGAhz4UiA0peDQ3Pn-5cGU21KVtshLB_UK0LooIrLiO6QLWi7gRmGiGIm-LEKZHIdp-z8tDD902hLKE8NFuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5nuuQVxX1v3PUc92Sriyeltji2JcW6HqzBaoH-vjuFqvZpiSphoR0uakJNCp8oiOl9VACBs3gRf-w9K9HigYyrDTK1wXFV-T1a3_Ti8pyolmIPbZXthoz3wdhFkIS7ORMMSMaNrIOVSTLOqYWRrR-UtPLoidPOuwpBvkWEgskrTZUiHEQNk2taQKRm8b9pVToQYl7dKm2SQmjCy0M_Nz-DGMd2UDsK6QMubiMn4eKCaAO2Dk3y8gslRAXrW5tZlfkNLbOI9rbXzikUdyQIvD8_S604N7vIc2QbKAhg77zpBMmubp5KlGPR2_K4EXptf6EPfxLH_PoCPApSyUk9Hig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLiJX1osaDsqNu9zS4AvDisCmEuxyGrelMXRCoIljdbd7Rb-GeqUiLo71WGvfr77UXE_44_vnuwWdOA6e4cYLWutBKoz7xdPjLfQcebHHafaKU2LDNg7wo09RqZNBQWThQvhN1MUyDGFMCBxKph170w07foVdX82VOQWLYGBR4SElyo2OsXJFgeieKNTXxE55-oBM9tvVwcbxBY5T6BUyHJtMAnAin-kFVSUd9VRPlg5g19U1w_ykQr48ga5JHkmHJy5BcMU1PcMP1B1x_4p5zfO_WqDMAIxP7yViEBkVP3A9-DuQY6PbZc6Um6UUQIfU22XtfzT0nou9tKqUk1iHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p4Rcf-VixBupKuTH4xz1bIj_8WRtRu890k2pX6tFSKXPMDI65kZlXYtxPcMoPXlkPQvPZj5fhdm_pyEvxBD652DxpQnfmknQeE7ofxII363wlRky9CMoVOi2RDGhgfY1vnvF0Tpk-ezT5wnBwvdCOVeGLEU6jp5vyAvXyAhnq3BC5RZUJa3X54Q_gmujJ3jlSgPesnTOm8oEuaqR42814ifv0zkFeFqJJ2_9vCr5OXhd1sw61m6Jjg4WF_z0hPLJyniyVJ-qMhDp4zjDTz8iamKelipCS9RJ3mhzLCbTb2eYkQNBEVqQANZeq6Ql0liREwrTT4E55BtgYEmcR1ckhzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p4Rcf-VixBupKuTH4xz1bIj_8WRtRu890k2pX6tFSKXPMDI65kZlXYtxPcMoPXlkPQvPZj5fhdm_pyEvxBD652DxpQnfmknQeE7ofxII363wlRky9CMoVOi2RDGhgfY1vnvF0Tpk-ezT5wnBwvdCOVeGLEU6jp5vyAvXyAhnq3BC5RZUJa3X54Q_gmujJ3jlSgPesnTOm8oEuaqR42814ifv0zkFeFqJJ2_9vCr5OXhd1sw61m6Jjg4WF_z0hPLJyniyVJ-qMhDp4zjDTz8iamKelipCS9RJ3mhzLCbTb2eYkQNBEVqQANZeq6Ql0liREwrTT4E55BtgYEmcR1ckhzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Y1u-saiMWybMVHHkIAsKdRpXftgcZ93ZqxvVQBlow1sNeW3TOmUaAsQs8tvmoVYPUfXQ98Czz6Xzo-IAoZKapQUUcoWd4IEtRSrkdRxUHkeTXf7wr84BnJPjgdrq79lkhfWU9eZU37RJLPfbHXdt_4uZuVmKgB6yB68C9T5Ct2E_J6IuLLP1A3HQpZYCIJNYqdzSSqmq4xzQm8KEYE6mqGqZyTKDBARKXnKlve58g6eygM07P2UrlrCtx0vaMbCfKfiKhAi81TXLdNQp5rc1f3yy9gIf7YEp8evqsr1BSJ8IEgOadsguZWismEPMRiquZiS1VBSy9EawK6j3QuY-SI7gG7b1JqQZuGcbNq53eMSyhs5KDU8hfo3k605ZZWZhgWd6t9USk7Z8h8QaSnUHAfcK-HpHBArH5NNyxaePEsqpN5rJDFb17bp3Zpw6i6bi7WRPy0DEt4p1tUEw0WhcFLOcAt9ZIugcgRambmFiJGT_K2u3UMrcSDz4fkmdjUevlS5PaAekvikO6aY7AGoPrV8c15zO0onxMTiwOumTDopvKGcRMIHDnJU-F1H1aqjN0R7SHIN9htiHj9OU4Cxx-lYDrndki9iPfMh0y2-7miAbpO5ZpdHR1Q-3hImcRxDNstot15CjvcqdUkNwXJDMIpXnuXSpbMUKIwIaO9fkqoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Y1u-saiMWybMVHHkIAsKdRpXftgcZ93ZqxvVQBlow1sNeW3TOmUaAsQs8tvmoVYPUfXQ98Czz6Xzo-IAoZKapQUUcoWd4IEtRSrkdRxUHkeTXf7wr84BnJPjgdrq79lkhfWU9eZU37RJLPfbHXdt_4uZuVmKgB6yB68C9T5Ct2E_J6IuLLP1A3HQpZYCIJNYqdzSSqmq4xzQm8KEYE6mqGqZyTKDBARKXnKlve58g6eygM07P2UrlrCtx0vaMbCfKfiKhAi81TXLdNQp5rc1f3yy9gIf7YEp8evqsr1BSJ8IEgOadsguZWismEPMRiquZiS1VBSy9EawK6j3QuY-SI7gG7b1JqQZuGcbNq53eMSyhs5KDU8hfo3k605ZZWZhgWd6t9USk7Z8h8QaSnUHAfcK-HpHBArH5NNyxaePEsqpN5rJDFb17bp3Zpw6i6bi7WRPy0DEt4p1tUEw0WhcFLOcAt9ZIugcgRambmFiJGT_K2u3UMrcSDz4fkmdjUevlS5PaAekvikO6aY7AGoPrV8c15zO0onxMTiwOumTDopvKGcRMIHDnJU-F1H1aqjN0R7SHIN9htiHj9OU4Cxx-lYDrndki9iPfMh0y2-7miAbpO5ZpdHR1Q-3hImcRxDNstot15CjvcqdUkNwXJDMIpXnuXSpbMUKIwIaO9fkqoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2PaQQ1njjMJsKN7P3OGP1Waslc7iYj27SyHJdyyeUNnoEoogIY_UuhA0coIRzEsfM_0utfstFZ3F3ueFLWiMaSCmLmWEjiYUBZXO8dSGnrIIe0I2GFpeywnJovs4DMFqut32Dx6XACYBnTh9QcSWs-hQs5ahe7H12wT85h0FxQMAmFwRNDo4ySUvyBAtEbuasG2vSDB7YHv1lPLQrDT6P6XGhOmqOu-WetrtVU9SNp06f6oQ4Tj8MX5X3AL-4-7bALtKUEKgBx5_txzOIdeYms7w9m8yUAwsESLOkMowIo71sA5FjDBaeEefBR_X21svdYy6chLwKpBPnVltu3ORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
