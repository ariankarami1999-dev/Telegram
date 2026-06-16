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
<img src="https://cdn4.telesco.pe/file/S9peqB7avsPA_Ca37i3PZ5VcdK1h5ou3Mf9zIIHOeyp-3Dwnz-sRBxuDYjhLgA4WNLdeTYf1NCa5vg28x6Xuu4xsl_FQfwLXRCs39k0-HzZQgCObm98tyvjHBv1cnfijj61PJZtF6Kl0XIp1OpUcqfs1yrCxisGNj50t0YOnCJpkxcyTeqkFeYwkNAD5VCnmJLoqN2U5tLwWyDMp8oWzgS_-sRTOctiF2CoMeqfG2pvF1RhGQwWW7yUHYuPa60bTwGzWSH0EMUNAZUiL9bsbOFgRCG9NZ3osg4AR9ODUbq31uw5j3PPuZIg1QCZkEi70soXCztaNoMN1wPBBCzZCQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftR0bYpplsw_nYxrx4JCf3IOHaDWI3xTUrzI3r2xiftoW6OHIKmhSdPej8ojhczKoGk5cyxI9O_qye-VphtyhKEbLC0ax-TVTr84KDGmKzXZ6OI9YonJwvFeGTvYRlLFhTtGHh0xfLb3LFnfn8zqVhBocLPh3nk_Lqq7onTUpzpMl-ObqujCRd5tvjtzT2RiXBSQKjfTq3shM9XU3VPTqpXnVQBdYYctMVQmKLoZ1stAEhMBV-yALUu3CimufYrjX9wKO5qLVi2o2Jh9-oc8UaPii5cNSMORGwW1hEKZm_52CZgSWZVwkzjpdbWPWdDhMHnpe72cJCQ2nAw-L2tcz_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftR0bYpplsw_nYxrx4JCf3IOHaDWI3xTUrzI3r2xiftoW6OHIKmhSdPej8ojhczKoGk5cyxI9O_qye-VphtyhKEbLC0ax-TVTr84KDGmKzXZ6OI9YonJwvFeGTvYRlLFhTtGHh0xfLb3LFnfn8zqVhBocLPh3nk_Lqq7onTUpzpMl-ObqujCRd5tvjtzT2RiXBSQKjfTq3shM9XU3VPTqpXnVQBdYYctMVQmKLoZ1stAEhMBV-yALUu3CimufYrjX9wKO5qLVi2o2Jh9-oc8UaPii5cNSMORGwW1hEKZm_52CZgSWZVwkzjpdbWPWdDhMHnpe72cJCQ2nAw-L2tcz_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOhHQbP1NmSoNA7LOu16_mgeEFxN1xmUekzUbmNqFCkaRxPaXuvXK8r2U5jA817xaC8BFjhLHJJQDrfSAx_4G8PGGEtupw2C0uQHkoHiaMqBsIUKIaoMMfcUhOBaPSSpubleLswM6QeLoNNUpHa0T_toBpLOkErCkauP8UX8A3niKHmgNCEvzUPC5b74-zDRuU81gZizvtAkGHFab7JtepV44sXES2WWbZLN8Bh-bm4z9yvf7_vwpraHXwkMJkV6QSjrHoqb0JelpLTHwrTwNcda1avusrnuTootnlYn2NMmqTbxI10ixuqh_Nn1_QQ0zXm2CVJFS9_ERT6s3oyaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXPNd-sjAK6k0FHjbEUDhvF1E6vdscgOFSJbeTN7yZuVUV-0KxyLKq1qOWkqexFwk-8uukZVbXrW0-m4ElApBznnLTNFTngMxO9ex6FVcg_BKQA9A2zK6H6strq0Zk6o9YPvJCvirBtcT0JN72ga7DTwgPg_h1ISOFoMT4zCdLxKtgAxdXL4UiSMX2cSR203d58Wh7FWlv2HtK7FchT2zQhM-kwO79Tx584swtoTWVuj-SbeDb2nA3DMuYal3WLb02tojAHUNIic672lJ7gG7sFp4b_ij0_WzZc4wkClfJzFdGu-UYfgg3NwGDDnCvu5duseOthqSl2SpURMVVAGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYhOO-R2LUKnhklu74Id45BTDEudSbOxk-7gL-KOCxQkyR8qEy_Ez-QuzOpLMpwC42OCS6v8NNhaCRbUi5pRQKbGOlp9eJWQz3jiGZ7LR5ss_7t4zuGYBjuijWpkjLld5KcDnnmyT9tRbeVSS8KR66zMzfGdkanvuglAjlb5R8eqTxaIslbejMCerhT1bhfOeiq1rn-gVIbwk8JSwwfK3vGamkmqXw0NbHIepgNvAVuToVf4X6QN6qBb7pPDS4t9ER0MNvlCqknelaaTaTwaNAG8H6wfqCcaRMXMgEXu_SR0dZYlasx53n0uRZgq3u470hTExviIqLdWGd5DaN4WDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc1LlD3zqCuGprnmnrbgLpLgnd1mFCu7FK-LL4ySrdE9IHUI6uJ0MkBzb_DSWhuUjvgPQKs_LIEsHEwro6Zy1wom71RiXAhFjZmhYZPs--uXV2A7AwLCrH8xmihGbDHN3RDcmYyDg55mutiL-daY3hWFO1wjfwUOOQ0BslsVzBGckSDS8Vvv0j3pMtI_JJNm3945FOFfbf5qTdh1XVrJb4GXDBmYV5EaulAJ6DczYf6lu3RRfCfN8q10Z6wa2cK-sr0-MDtuB_ejqUSoLyaFwDGhPYPvsNLjeLKy43UufybMif-KgstjzwiO-tWWbdQAx4NiGZTiYOwouruKzJX9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBw_GIV4sJgbtRCH48QSCYxpQxAsL6fxtWCMaPz4hl-pvcKsjZTbmk9Q8FhqkJEG0-pEpsRWDeMAECpLCAA25s8HpuMsVLWZEpuAsF8R806XYkgdJOcyaOzIh7KcqGafUu3WchyTlXPhcch9S5gmXu-bRquGo31C85WBYAwn1EZSGxFc8ZbukmzklAeveudC6beCY0luHzs-Koaeawr0ywhCWXJz56C8qsDg6hAvo5tPwK55xTzP-xLPV2eS7GZI68rcrOWM6SoRO35eTvt4AjMlVjvJdC1H3dnxYcAADodsaAIBT3MmomVanAcpEJaAxy_vzP5sT-76b6B8_5hV5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo-EVKpONwjyirABFjizyI1SGde-jdHRD27BfKm48QMMal63n5oHUdtEmmhHRtltgeoAogBHaFgVZxsF9iKXbjiSk0KC3a17fws0EQfjaK4BPwghKY3FZn1fJ3LYCnwqCGZRBCgWw0uAybSdQiMQZ0LRjM6WgLj6fchvQJFxgyv5Jk8eQRkEhOS8eppHQht2aXcOkWOjwYiLki_SXoyFqWWXaHBzZH3w6QgJfv-f6wpB4kF3KEgmYiarLicGoKDT_p-YmrL44Ixc1hwsL69n8nGXy3vcZcFo8qX-AC2SJeK-jVtzBzUexMuB2mEj-3tgdrbcdG6aqAMpOQr8OWV73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3y0TZQ7CJDRUoEWhQibPYZ0lIsaALmMn2oL0nm9wzzr1FvgzhkxakrdzL1Yf0tSTzwCw0Oz4ypBxtsB3mdXGiZJ-g_8m5b4e0j4PAUzudQo7b8CZhfXmeXulJfMhOTkD-q4UjeQgRQnvbzKTeJOnF4AN3EkSbt7UmUrhU1P4uwWEGDxSkmFUkl3BgYzcdRs-bWAMA6NJdbCcLgEp5a18cMMa6D5bDqLiCXbj261XLjMAn295jm3bxcNveTZm7QHqhuqrGBtGQ8dE91rIBTAWlCFVTkqaMLKDXmDjSlEA_sz3LoL_e5J0b9tOiDG9hoL8pMZnanGI91b_xB0ovLrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qADh49vJ2SgCVxb_SBa9v6cLWQ295CcnKXGsfJlALxEo5jYV_G72yNreTb-4TgJV7bqcIU8ZcNc8hb6EiJGyIrqv42d1iN7oa6HoncFhR1NU7a5zusAClNb7qJ_y5-N0P9PYDiUGCU43Io4xfA52n202kpgi6gI5l6aci1cTHVcMtLWaDnd37iz0g2tqwSqcTA870zxXAIHC-a1wo_boDrKa8zyjK1ZvapBIgbpmqqSQVzKRdilIq8n7_c2zVr18fV9d_uvPBQ8Ab6SvqWJforRZNql1Hq0stsPNJEgZbBqRuCMnlZwQXOOg2CznJovd7Zp8eJruk9Cn7cBbwVpN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=elPnzjFKI2BxP0WHD_pFRu1IhrxSKDjDMSwWsmNjgAiqS-FVzNwulx3qCgirZGS3AwZu-biIW3KeVMoXYZsAOjNpjEovzaZU30L9VPgc0wsqbckxF2NZOHAHUQycoEX-JQ_jHIjhF4R06pVmV8bdNSRLl9dn8HoI3D1WKVd_U9-V4w3V9jxqh90ngJrgnE5PuZ8RyKH4iDCFtc8JNooAauVV0cMBXM80BGeKJ27rduwv70uIi1nVVMGYi2NoYKOvzXMA_BBGreqnyJeKsHBH_1oXapvJUhxYVSsddxgk40XWhmEL-7m1ueqrOyhnwX9pPBOz26IMu6Yb6R8XJRIdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=elPnzjFKI2BxP0WHD_pFRu1IhrxSKDjDMSwWsmNjgAiqS-FVzNwulx3qCgirZGS3AwZu-biIW3KeVMoXYZsAOjNpjEovzaZU30L9VPgc0wsqbckxF2NZOHAHUQycoEX-JQ_jHIjhF4R06pVmV8bdNSRLl9dn8HoI3D1WKVd_U9-V4w3V9jxqh90ngJrgnE5PuZ8RyKH4iDCFtc8JNooAauVV0cMBXM80BGeKJ27rduwv70uIi1nVVMGYi2NoYKOvzXMA_BBGreqnyJeKsHBH_1oXapvJUhxYVSsddxgk40XWhmEL-7m1ueqrOyhnwX9pPBOz26IMu6Yb6R8XJRIdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InTHFji6gKtKee6DnXAP0B69xAXsqPqsf4M8nvwamaiwO94ox6InHU1ElHr1iDSQRCr9jk2HPf0RmmMVDW1Hq_8UI74Td6kkg-lQZmARe0ttUQMBiPD6mdF3wCmyf4pXnjwsYl-4xyuIkhTe2ZrlCX1V6ORG2YaJlRiJZKzYrX32JOLMbdXGi-3kbLfBJVs6UA-v9FJdnaMTMfqIC6SJyXYC90k31ST4hKjhwbZNWszU98SqwEliPWZ6F1C8bEwDEFtrKfXohXF4_pTeR5_Z4NJRFXU1hdKjycCsyzlnHhWXCHr_4tcURcQc6YRQU_ebx403S2L4Q33dtT2VbQ1OVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSbpJQugd9mg2jl5GzPeSTFGs0heymTbYyLTFg6QPRn3nhNgbR8QGHTymDrTIBkecWP_bJjoaz6xc2Wubo8wjdlDWD_gKHPDxdsbTEVwP746pHPTOtMSGuzreHH0HM8QZLnUispO9OojhTLXpsOiCFn-skISSOMQ45oKZEk3rnRF7rFtSoamPbX_4lQUE7DuV7YaO6_EIaiNMq0gGq5JvIvWOM4l0XdGTTarJ2QjPIalQtzAI6NYBA9lJCdenhRQq9HAOBPVU5T_8aO4FgGYn-1SUBpICgfyMRZUjKoASJ77D0t0lyxO5UvuZ3IOybp1Zmh8wNgGjMtsqmfEJZ938w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbGwRcyhYYTGAIxeMONNEc1eLkdxGSSgZoIPNHNdgK9lmY4jOpZzLwTQQl9DkCEON1Ao49nXcNLBkjiIgNHDHyG5ZXKJuhhqGcSibbaaJPRSmNcmrhFdSBLg64FGz2epszYJBaiofqMjfn3lC_Jc5XIdw6DfNVrmz6raT1827FYQJjwA-XEDD2vwyOY0Pd2kV9Y2X-_Hg__oyJTQnqbMn6BWnJPRUHydHf0dAGlAgCNwu3sICwIj_GZzntZOVsn8BozvGYyS95FdKJ55MqPOlXmADK-HpQMnlX-UY0fFAzh0FqrO2voElgB5sMJs7pGuRI6RaTz5icXl5ox95tuGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN7kDWrBMTaqK8Wv3Q3f7uUDutB5Q2-AI3pTInsYkPKZwY7Qp0tTw9CubRaYbw0at_k6ZSPVzIm7ixKt6Lir2QP_gxQbtsK2Vibrxbvu03DzUw3pjSOUx2Dq2j7tHyF8Kw2mzWHx1kCHv_lp8mwm0k4pyhhtr-FPr7D7eOUbWqkUPN3vGETgW6JTGvNsl2nSPQOXbG2bequASPXuCthJMQiPQs-p34_uurYEg80wEm2krJ6D5agAOAz4AOUOdln3YFcVnXNCKMmt1x2OU33tz3puofqIIY5UJCy8IMBfJ791aFen3YoMmAXOWdtQSI-wZHv_7bLQB_4NaMuAfsStVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPQR2Osquzp51gKjuUHLlitQn6w6-1STPpR66C5SiWpZYTatIgTouqiYCtc0LueBEtva5NNlD6sMj3I7qZXMtNLVToxOLWLnS8_pdubic3pIESmgPx1fKr8H-gf6XIaPgahyWxbjW8uPBbJQZJiRmhWmwyXwlKzBkQZqYniTv3wFzPnrFUGSP8hYM2zXiShjvPNkxz6OFAeFYnBtP_3WBv1EXDfBZxkuaotyDNeIW6kld645DpGlVOMBh87rLzQ4mlUEb300if3TLYnjzJHQ_hZDsdSminjGkl1BrUH0tBnZL_vYzzGGUfMmYviTjNmVwGos42Rd02iLb7OuEY39lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXKovvUpDBoKVlntz43A7y2IvelE1KMmkP32IT8wp7uI_pTrylGwmeiEMipE6FypfGXENRnWF1Z_mUEIZqCA7CG0HBzR6u2Xy5UHM-v6oXPKipD4ziG1dp6ghsRFDgDi-7PM4InqmvMVp2f1005h7U6BgxTsZxScAoqs8qpKQeqr2gkLBN2-10nis2xKQ_caCUZW_gsjV9ZJ6F55acW1-UnPo6U6rW4t2KOLBKc0B_DlTJ-OplQlEwmmNwvr3aeaGXQG0LS8hgIHV-g4mqYLCdQFEyPlxS2kMknX-jCze5LNwpGKmahy0JNsAQfvPpskkw1LyXYYeyJGCbh7O0KVDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qV1q9WfZfUDJ7dOq-9LQmBGUvq4_98SrPP6CMcM2QNuhgybSLBzTFIwKJQUKN5VTyc6WbsuIjREkww27KeGL5vphpfAD729q6n1Xaoug-aUuXwPcJcp7xjm9q26K8y_Pw7nXyjZx84xfRu13idDzqlzI5aTPmGx_kpd9J50rNiZL9YgMgz8jLQRiyzgygtFa-UMNR4nRh1-TdpruowIi8TDEYR9UD5O1zBLcsdJ7vHK7N36wa2WVGwulKIgAKNx8QR6_FVETC4o_7NDG0KPf9CRdmnriWQ2b1lrQg7oyMKSk3PZvATFn2us6YG_0Gl_Pkkj7NVU2JOQ1etbwmvyb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czrq0nR4IX_vOSYkokzIOcZZIvxskRk6YvEsIMztegBOmNgeHiSSMl-RoRNtxjjOuORi-E1JrxFTr_CDBmgai3PqPkx06OOtnNiwFtIUUo-mo_TFoyyziOKi4r-DgK-EAXfzahFA8FM6RqGfrWh12xrIvagS8wFJSjaiJgqLTJ5KWR6_nFXUXNP8tKXHri5OZsuHAg4FUUtNMqY6UuZhHOSntxrl6npkSzc7NWBD3NFd6IkkrXVHZRq303noKLxshxj-mwRKqix71dugduWVp7l9b_uYkM_XEMnbo_nKFeJBJaJ4JH8CXg9P_u4wJtxjj_bi5ww_NRG7rIawe-hrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=FrsBWH3gyUegpft6vqxDGxQQJ2z_p1zCvQ-VAMO-xry0vhk-RVueiMdRIh1OX3Mj0PrtIn5jwc6CEpXpC3cr5VQvGVYW7NTOR0Fy7ekHi3yEdve6PjBjngI9AIAUowcce2IZcwAevxACcCcptHcsibXduA31XtxBrf3bhyLqoCs9wAWQmtQx47UO6_UfuizyD_ifog9HXtCDQaaF8ua8OJ0MOvtZtqD-R9sxUNdhFavnODYtqcDPI4oyTHMod4-JKBBdHKpfZB2LITZnXSCnnQmjfub_nLymmy3NQNk1dgteiON_0ZSqVcPdAKcO5D2fLsNu72TEQIKfzaS9BzL_mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=FrsBWH3gyUegpft6vqxDGxQQJ2z_p1zCvQ-VAMO-xry0vhk-RVueiMdRIh1OX3Mj0PrtIn5jwc6CEpXpC3cr5VQvGVYW7NTOR0Fy7ekHi3yEdve6PjBjngI9AIAUowcce2IZcwAevxACcCcptHcsibXduA31XtxBrf3bhyLqoCs9wAWQmtQx47UO6_UfuizyD_ifog9HXtCDQaaF8ua8OJ0MOvtZtqD-R9sxUNdhFavnODYtqcDPI4oyTHMod4-JKBBdHKpfZB2LITZnXSCnnQmjfub_nLymmy3NQNk1dgteiON_0ZSqVcPdAKcO5D2fLsNu72TEQIKfzaS9BzL_mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=jbLY9Nk61cTfe2iCWz2gayiNe1RkSyoUOhQXunHByVp6TegYemmyDGH5I92XZ6IisvZzF99kjNFmO2hohvOXYcn1q6Q5Szw1Dne_QvS5OvTWpECtThyVZHvWWE2vC9PgPY8i9_3vICSIBWSKEuKa3p1OaHa2rPjTZSKEVGM0EEZLw_pTbYxw75LJUVX6Pwdh0aujiPlIUFExOweeSN36GZHZSd3qXjTA2mKVrYDY4VuqkcmMDlFkJ4TZZlmJu4Uxwdv1KmOF-AjONa-tkFzYOHZdoa3fBtLifhGuQsar8DLOIbAwvkwHN0mtWHX5yvRj7F96bAlPLfsI_g1Ka3rpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=jbLY9Nk61cTfe2iCWz2gayiNe1RkSyoUOhQXunHByVp6TegYemmyDGH5I92XZ6IisvZzF99kjNFmO2hohvOXYcn1q6Q5Szw1Dne_QvS5OvTWpECtThyVZHvWWE2vC9PgPY8i9_3vICSIBWSKEuKa3p1OaHa2rPjTZSKEVGM0EEZLw_pTbYxw75LJUVX6Pwdh0aujiPlIUFExOweeSN36GZHZSd3qXjTA2mKVrYDY4VuqkcmMDlFkJ4TZZlmJu4Uxwdv1KmOF-AjONa-tkFzYOHZdoa3fBtLifhGuQsar8DLOIbAwvkwHN0mtWHX5yvRj7F96bAlPLfsI_g1Ka3rpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Sw3-meG5rBm5WwtYJhm3mxxCrR8IKn09ku06m_9h3zQRSY1wRCrvMRKWS8skN-cseHqEEzQhPl5Quw9Y9Uq2L5aO5T9bUOq6EvKCikg_9D2azk4DcGLgbLqHHn6HZV88EZlVko3JNt3g2XB0B1U9nrDUWrKUlDC8Zc7K86aC4L2ipGxaEG_az0f4SdlAgbzAlEqv3Prme8DO7AimwS1XZ8cIyokWxp25Teb61q6X4UwAXiDkyFDBPL4rSkCNl-J2GXZWrnG6MGzFQRkvpHLW12bP6On_yXfrV7PdfehKv9WvJChmR6OyHEvifcEdAwcFrq3gNyvQKMac66wnIUhcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Sw3-meG5rBm5WwtYJhm3mxxCrR8IKn09ku06m_9h3zQRSY1wRCrvMRKWS8skN-cseHqEEzQhPl5Quw9Y9Uq2L5aO5T9bUOq6EvKCikg_9D2azk4DcGLgbLqHHn6HZV88EZlVko3JNt3g2XB0B1U9nrDUWrKUlDC8Zc7K86aC4L2ipGxaEG_az0f4SdlAgbzAlEqv3Prme8DO7AimwS1XZ8cIyokWxp25Teb61q6X4UwAXiDkyFDBPL4rSkCNl-J2GXZWrnG6MGzFQRkvpHLW12bP6On_yXfrV7PdfehKv9WvJChmR6OyHEvifcEdAwcFrq3gNyvQKMac66wnIUhcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=Y9Zwe3mFze3hPmoJ5KIoXuxzPX4JdGlDyJdkchRtUzxLmg5Yt_5xgGpamrCw5ZkS2ntMUBpMiUl-OMO37XNKboe_1h6m-vfBH7ktFIbaa3qR5RtCk_hN-4MGH99-1WCGZuGmpgBrAqRDsMgESPJM8WxVYvJoU4OSYyWyGDLXQRClQ4Phn_V-SO6PB7WKHix3TdVsQ2EtJHWrAXfxTi-1WEqZFvStvQ5CW4uayaLk0vcrozU3ncBJ43Ou-UWv4u34bCTEueszcjpjLzrTHp-PUHdyFK_EdOXpsgodlRW-LWNgoIwO3sscBEwZoQ2tVAdocexgm4dN2vIMFgihiZB--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=Y9Zwe3mFze3hPmoJ5KIoXuxzPX4JdGlDyJdkchRtUzxLmg5Yt_5xgGpamrCw5ZkS2ntMUBpMiUl-OMO37XNKboe_1h6m-vfBH7ktFIbaa3qR5RtCk_hN-4MGH99-1WCGZuGmpgBrAqRDsMgESPJM8WxVYvJoU4OSYyWyGDLXQRClQ4Phn_V-SO6PB7WKHix3TdVsQ2EtJHWrAXfxTi-1WEqZFvStvQ5CW4uayaLk0vcrozU3ncBJ43Ou-UWv4u34bCTEueszcjpjLzrTHp-PUHdyFK_EdOXpsgodlRW-LWNgoIwO3sscBEwZoQ2tVAdocexgm4dN2vIMFgihiZB--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=TP751y0burAdmpoC8mMw5EZmpUuIXInVPXZUNiRTf34OQNhxQmrtPcwWiR7kPML1td3QNR3KZV4hYKGWJwOWi5oCDpkCqy41smOJLi5vDPilSig8bGSDqiG1mUCMH-QtEfWGB4ef6eOsFkZylK-WFSqA4ruidQsl12bV7mxP0txi9q0gIOMERzUUUT_UAvbclczIVyLOt-nxSCHXmnN4dd5tcEkGHBKxGIuIO5t90Q5K7q4Ro2Id1werJDd-5tT6YDPziOFpQ-48gnJyNooMrz3wQmcBRu-tc4ApQ7JjrgdcqPIJMp3bGZfdMQL3Kyvz0VANQJt6D-_hWwt2nzKKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=TP751y0burAdmpoC8mMw5EZmpUuIXInVPXZUNiRTf34OQNhxQmrtPcwWiR7kPML1td3QNR3KZV4hYKGWJwOWi5oCDpkCqy41smOJLi5vDPilSig8bGSDqiG1mUCMH-QtEfWGB4ef6eOsFkZylK-WFSqA4ruidQsl12bV7mxP0txi9q0gIOMERzUUUT_UAvbclczIVyLOt-nxSCHXmnN4dd5tcEkGHBKxGIuIO5t90Q5K7q4Ro2Id1werJDd-5tT6YDPziOFpQ-48gnJyNooMrz3wQmcBRu-tc4ApQ7JjrgdcqPIJMp3bGZfdMQL3Kyvz0VANQJt6D-_hWwt2nzKKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=jkQ7f-qCpDnq83q4rrwf2h9Vg1Sky7CWWFKbmCxkpgopYa6T-JZtgKj-uMhsuxIXWsllVl9CPbL9KVOEjeCXenvd265yxET68fAh87Ndr5DmAu8fBnzSwnlMdNmcP_Nquc6S_NW6qiFM6zl4jp2JE1PpVG0soTMTH5KOSVOC_ZQXy1ztT_xSQfbN1HXpgfwllbOk-UN8uVQTQJ0sckTKGPatj6FxG9RZAfP4V5ymp8tY3WjjNF8dR4QsNIe2n8iio_JKszqPz9YJp6WJI8XKbevjsK2GXsyX1VD1mBdScxLikLyJvh38IBbckfWjRSNIFsKOl-gdEoiV-JxrAI67wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=jkQ7f-qCpDnq83q4rrwf2h9Vg1Sky7CWWFKbmCxkpgopYa6T-JZtgKj-uMhsuxIXWsllVl9CPbL9KVOEjeCXenvd265yxET68fAh87Ndr5DmAu8fBnzSwnlMdNmcP_Nquc6S_NW6qiFM6zl4jp2JE1PpVG0soTMTH5KOSVOC_ZQXy1ztT_xSQfbN1HXpgfwllbOk-UN8uVQTQJ0sckTKGPatj6FxG9RZAfP4V5ymp8tY3WjjNF8dR4QsNIe2n8iio_JKszqPz9YJp6WJI8XKbevjsK2GXsyX1VD1mBdScxLikLyJvh38IBbckfWjRSNIFsKOl-gdEoiV-JxrAI67wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9zg4XuubFZ9KAEcEglBHArxsIUQ47OvFDu2bH9hRBfwaIv8xSCtjZOukn4pjhbzjHSv5_2B44wQNGUx6DQ-YP5AU8gf1HCGWPw-vw6IRnrReAsBV7MjL8NlJZeArjJ0EuZWe6D0RSmfAhxMS8c_17Ojb7oLlKUBxLzJVOdsKnkp1FB81HTnmjpAF5ODjLyJfqPxwgOZWBXJRFQbGMpCDoq4gCJUdRrY6Xr3OMj0LZixwj-1p0hXjBS2Ws9i8RqKiYwZX0-p75ov1br5xAcabbi2x6rFlgK6P4zFN3TcFYzNHvl6gTOtcrtlA6jePQG1jrbC4DUhhPLl6v_xlz8OzxEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9zg4XuubFZ9KAEcEglBHArxsIUQ47OvFDu2bH9hRBfwaIv8xSCtjZOukn4pjhbzjHSv5_2B44wQNGUx6DQ-YP5AU8gf1HCGWPw-vw6IRnrReAsBV7MjL8NlJZeArjJ0EuZWe6D0RSmfAhxMS8c_17Ojb7oLlKUBxLzJVOdsKnkp1FB81HTnmjpAF5ODjLyJfqPxwgOZWBXJRFQbGMpCDoq4gCJUdRrY6Xr3OMj0LZixwj-1p0hXjBS2Ws9i8RqKiYwZX0-p75ov1br5xAcabbi2x6rFlgK6P4zFN3TcFYzNHvl6gTOtcrtlA6jePQG1jrbC4DUhhPLl6v_xlz8OzxEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC0ZYFdrAPsh1ZoBJUhM8d4Cz3O_OasT0v7eImHDBETcFrGT0iqzr7XMCufSVA2tLReYdtrfzcImCbt-z4vpb1oZS1TBsmJGdekIduKGwl18wh8bxZI_6Jz0y7WlRQgt5FLVaOe_-1V2yeNFN0J5YIHPcsmCsz0pxCjJEpt1wsqRekRpORgS8rpzRN1LR6sdm7quGk1KD5nAwlyAmJNmK9hYilrYXnqQKokAdqG4J-PA8Uiqc07zPLmzURNpBMA0VcrTYTUsh89UYicJ8Maj68DTOHAMrXwvue1HIPfjdq2ZKQ5BzaZTb3-gFogoyXeTXfCxNZ0afFOA5n_W_NYCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Onm5_jzI7SKD8OY3XVxJx5FxaY7B8M14II6FDODgoXDxkDqx1bkbiSPe-LX-DBsEDcfoU0mJWKg-CakrNPQiCIMEK8b9rOEeb0nFHC9gr1a0viWUcsm9lsbWjdQ5wU9XpdvnRory1t6e8IXT8h9iLV5Y3Y34vBRlKhNMRqvkgEG3aQ1eENydHH-s7ZChyoWcaI7Hy6z9024kJlpGyWHdfM_IvX1hjhqTSLkTzJb_6dYYA8yqPW-Zj5ApiC38_HAVfbqVDPGBZRz-4Ax6zkI6ArVomR58ETPoKssC9d5oNI19NNo2CtDSTs-Ra4qw44SFGtSxi8qA607TybBlvefVDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Onm5_jzI7SKD8OY3XVxJx5FxaY7B8M14II6FDODgoXDxkDqx1bkbiSPe-LX-DBsEDcfoU0mJWKg-CakrNPQiCIMEK8b9rOEeb0nFHC9gr1a0viWUcsm9lsbWjdQ5wU9XpdvnRory1t6e8IXT8h9iLV5Y3Y34vBRlKhNMRqvkgEG3aQ1eENydHH-s7ZChyoWcaI7Hy6z9024kJlpGyWHdfM_IvX1hjhqTSLkTzJb_6dYYA8yqPW-Zj5ApiC38_HAVfbqVDPGBZRz-4Ax6zkI6ArVomR58ETPoKssC9d5oNI19NNo2CtDSTs-Ra4qw44SFGtSxi8qA607TybBlvefVDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgLSM1V4SLLkMtX-O0TrAy1oPUpEyJdSFJ957myR666VZRbJ2Q1bM-1KNw1P3FmsGbRxsRJG6Nwq-UwS336sQuTALgHje9v2x66wKSKgNXMiysdLFTVceDoWZYHtkvYEU-C1O8j4eOFthkyGQavoMZICQCepnITGN81pcFzuz3YZvwdQcTxfaPQv__-UblfmzlKP7kkzVe_2ldG0ah6GLnH9lNyRCiEYuidb5EDcVPMjTEnFlSizMrtOzkN9_DK-N7T21zw53A5s7NcPSOd7u2sRsup13AMW2hWZ7R9IAemHYZlug-Ib2HKfnLvb4uFxFcsBGxJjJ1JyddKD0v8maA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITZe03VBrFSThX2VQUeWf6VwV_x1hqtLAlxBODqKOUh94ZxwEf6nh-FRqJD1etUiwJ_jYzuz_Z4oM0JiJ1m0VDL8gtUQAqBjDsXlOqf2ueZCJAWZKEDfjSoOpwK49zZq5PBuzktt_e-veJNInH7YbIcHMTvBWm7wmrRzRfbVsxV9_Vda1Ac88SHFYUXlvppLX0HC57UpVN8qd8WedRD4jFebx05dFBlB4Oz5yTlXsz32eBVj4BQrHWTnyrxGxaQ_yAu5FTZTFrLVXTRHwNvcU-oT_vPNDpfIJj26uHpqJc4MxJ1JjdHi_LudlDEpi4y09-_6P7_U_NJaM5REYz8lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5c_qWW_0AbnN6zXZa5PgiW-gJR0W0XR6fvwd6G1mK3ZonktUi2Ti2oGK3y-MYF-K026z1ena8Uz81MKsIDfjKAPx5NpSMPwvK6xIz7mBN22vBShc8D5Q-tVP8eLMpxjDgWRe9J7c-vb025nBDW0Q7rO2yUYmQUJGfWFUxR_FQjNzQebAfZ0l83aK6LL3xR5kj8KvgWiDoh3HgXrgBWCvG3FFb08_iashfvaGKxaKZO8a09uzVCkkn3whAAXwyCLUN0ZhbkFr0kZM30KzrPC487ASx-JyQX_t3otdSWTHf1dIAepd9xhJtqqOEfoII3d-uYFBjAISo6HA2NrorVJRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=ZKaH6rytiv2rle5FLSay6g-WS1PWbVbvr1Pdz06qE0cSBe4sGclnG3EMg0i9pN0Fm1ZUHJ5A2bDEf8BiAMuNL4auybdTAAQVzW75XuanZkAUJReiOukPkw-9LHopqUJFsI5mSPnPNDEw28KEr2GUR9qsnO-mPJpSvVhqu3BUFoi-EU4EsEY-NkvkMbeRPz_qDtYM4RbEWRB8ONJroIDHJ0PDyJlvkBDUGSo558FpP7xeIQVKN8LCIThLA9UG9bEMvCJjbp9UFzEQIJdG58_02Ye2GrmbJqHYDs9sEzO1KBU89O6zjrYx-vUe0sakaU5cEgDlZcBq4fD9HK5wVn1wRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=ZKaH6rytiv2rle5FLSay6g-WS1PWbVbvr1Pdz06qE0cSBe4sGclnG3EMg0i9pN0Fm1ZUHJ5A2bDEf8BiAMuNL4auybdTAAQVzW75XuanZkAUJReiOukPkw-9LHopqUJFsI5mSPnPNDEw28KEr2GUR9qsnO-mPJpSvVhqu3BUFoi-EU4EsEY-NkvkMbeRPz_qDtYM4RbEWRB8ONJroIDHJ0PDyJlvkBDUGSo558FpP7xeIQVKN8LCIThLA9UG9bEMvCJjbp9UFzEQIJdG58_02Ye2GrmbJqHYDs9sEzO1KBU89O6zjrYx-vUe0sakaU5cEgDlZcBq4fD9HK5wVn1wRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAJjJZkQfV6jKg03NTWMIJ_x0w41upzqIMO2DTu_hv4ASuVzuyUeWUUSBMkRPiSaYCJ03xRxB-zOEbnBcJa8PIwRtYPw13DSr3v8UdhXlNvsb9pln94YcOaIqQ8DKiC8vAJhKkGnCQMS6Z4fsG5J0w5Ex1tqKk_rpCVvTL-u7QtafWDpYBZY9zakbpXavTfC9P1VjehPYHsKC6oKp1DSKklFCQhn6_BKiBILvpvlGxgS77vroGG5bdITHLop2CCbFX-z7ZsXl9hkjWJrj-PAAbCBBKhtrtNgX3IpW0oWVun07I8KyXOVeHsAC3LJl_dkRxzFwzWeLdpgPRvKICf5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgF2gFNZMOKOQ6GDvMe1VdCQlMNo5aLsB440DF9PwXkYT9VJmks9_dnIoqMqQziq-6Dwf21kwZPRMRvZyLZ7fK-fz2q4nwMIlyXrhNDYal-nXwjCmbdFFsQ2Z7MpI0tj_DoXv5MDv9TWigp64Z2ssuueVCbyXgd2-ho7Nj3dV7dfO8EW9CrgcCN3t2JDFH7eYEiNNi5vKeJF32mVFqR2US0wEIkB8EIIpZX62j_-FXZap8SAtBYT_vUB_fkqYLtFSzLzxUUeGa1awyq4t3YU95UvT_3gugiCZtvDmznNjeU4G8HY2AEEbFxLYkbJQFmqmnhGsgCWiKwmuaICZlcaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaMYy6KFt0sg8xux0dlzpuzhSDh-StnBcKb7Un13WiCxAxQmy9Zbs_Ae9RQrB9G8e0odggqz25_ukwFOBz5V_rWkeuhh62KP0IR9OfpgWpnMVp8ZAQxi73UagG-2U22AZMOwRqzbBHQr3dw0ngW7hgTuqXudciYLfhP9iSxGfDGFf2uVc9KzyAPq0qC1a36qKQG3E_ajZ2OSJEX032Orte9-gw4-J8K4pnUJWra4l7GdLmiehet3EFIYlmA1sxkc4W6nJAIp1z7AtFdMwb3JwU9ZJZnq4v0crQt8WrIYOOB_N-YtTENvOs5j1hXqpcuVI5dayNxEoR2tIJNlDN_VXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX6t5MHuER3MiqngAqc2LqZJG56GOQC9zU-kjX7va5eSBlydUEQNX8jueE-D1Vyzlz3Jc6hqLQzXTBL2lQ7Vk6sIes8jzxC1wSDsJKCIDmESaUaoIQDY0pXmJaS20_1TTxeh7OLZayUH12Wl5HbLOTbawbORDwa6tgsRKjFiNbEPBzoiINgdpSBXNvqCYOLrS0RsQmccuGCiLWCss11Z0PNnD6HjXv7ojEqHwkyDbLUyI0u9MTj9SIHye1aDzhTWL4mk3mEBiKf6lfc5L48-pegdjBGH76RuMEb_JbS0ZKOjjxtWhvauETP7E19Z9QYWomwZ-4Zxxf4K15ftIiRqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=dd2fyZcBNPT0CYW7K6kGtll7H_B7_o447C_rgykpmMBK7WJvn5T9_9zoWnFp3cZibsvOcTh0dq_mvig4zVVEdF1wx_Sj-N8K_0zSxVbtp2GFNp09JoKd_ZkrlkTgDe9px_MxvHgIyi6YhN15gQZkxuMKkb2qRdIf_EqfFpSyeK_vWpW7DKYqn5vdHzRM24HfOVBOXQqhmlX5_jYDbVXEV8jDywdsGJVSeTBgfyPS020ijpV3Lr8BGuTCydHEpAcGTVmnGn_UkYedbldH2NiO-QTxzpFSF8Jell4SB9jc82pJeECanpf6sO4Zgz4YvuBlXLfSxU4kUbumzFiFWwYU9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=dd2fyZcBNPT0CYW7K6kGtll7H_B7_o447C_rgykpmMBK7WJvn5T9_9zoWnFp3cZibsvOcTh0dq_mvig4zVVEdF1wx_Sj-N8K_0zSxVbtp2GFNp09JoKd_ZkrlkTgDe9px_MxvHgIyi6YhN15gQZkxuMKkb2qRdIf_EqfFpSyeK_vWpW7DKYqn5vdHzRM24HfOVBOXQqhmlX5_jYDbVXEV8jDywdsGJVSeTBgfyPS020ijpV3Lr8BGuTCydHEpAcGTVmnGn_UkYedbldH2NiO-QTxzpFSF8Jell4SB9jc82pJeECanpf6sO4Zgz4YvuBlXLfSxU4kUbumzFiFWwYU9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clSLh9t4BPRqbKicCj0gkXc8gHQQ3Med5_HcnDwfCzaknFbdj9vZCbDPj4A91cIzUvsBKI_EkxzKcXZQ_WLnE3alqt3lA2OaOuzpJQSuU7GSWm-1mcqVXrpnBHcTrfjOCznMQKKd70D_pvabVuzMzn22x-eaGMijrHP02S8XSaWWPfpthHAofLhB09TPyCVGlAvoKvNJRS8_YiVrfvYTLsKPvYwrxi-lgusy3aOiLznnPP68NIGjun7iGGlJZWaUFKv1_8UCMRGL4gZioVLvOxvyvLVW4ZC0B9YVbFrS0BOTMo8pwmeAF6w6ZgbWqPHeo-0tCO5Sy97AFdfNkA_GHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAKTNrqzivibA7IzSvBRq3gIE72slUhO_BQLTBNftpdjiPWGq6bay5d2GgFQ9QAO8YSOKdqU1hCiFg6dVKq259k1OEY975KA3ph4a8HY9kBlnqNQiAwxWt5MtMxdEfqUDGVEEIhxkXp1rNsYjDmxcZ1tBt5s0Fim80uWnmX-i839PtVcaMWRVHjXH_hg765WXasRfatb7mFsdnJlxWuunzqAysrRqR4vFKIoBtNHrkR8CDuz5hJFmz7LwffwOsHpuNcWAvfQoy049pWUNyfREqKVCXpNXiCdoK4f5jMGLNEizG2-Ff8a7nvBTXhUtkRg8PuHAAaFK80hv5zXvcV0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=FODgst18mlqC9eHp8NQDw1h0IuL9zv-d_JI8RZ-p9h4CVIUuga-nkvvFiw5T8RYPbNwmxloGX5cEBCRtYzcIHgaEbsNIjNBCsffbNsKLnZCbybtZcs-bCp0tyJA0CXruub_ojREtojVEYT5iJ3egMl7s7fsHxSGxa5JSkC8Gpvum0tnqUEyqsArutF7jeOUPQj-9TUNPo3K9Ig-suSUPLnCU682-1f0B-X1FsIiMqxUyDK1lfpvP56YYDMgNptd-kwRoBtmIO1MOzoeaXT_hc4KfSOfgAKumzSZrZvfstZY9m-FLdVKUjnTkpasII9j46Aoltu7y2VB2R9sRMNzOU7fRSvvHf-G1ElTuWUzFDtVWl9z5yfuOmHtw90uFksgqwPf2Gysplsn1nBavkhTuBoHbHXq7tYtbYrRa_CnWrCLkGITHHEwKgZ9Z5254Z6Q1en8GYMIJdG1VjWF1dMfB-yHmlYncvQyX7djg97Kst5l1tlWOggUuVCihzuiT2Kuzm2qqsP2cNuXt3b3fzBFrjHW1VH3cyPa3p_FU8BjoJxZwK2G8rfCoQYRBmedZ1gakLWYWcejDXhN5-MMBix8xpPKgCt8x_sFuU0486Pq12EmDZaeqSp6TM52nO-6hW-kq55wtYsfJAUgbJbJbpuWR8zKLeCwJJEaz_1n2QDhpw-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=FODgst18mlqC9eHp8NQDw1h0IuL9zv-d_JI8RZ-p9h4CVIUuga-nkvvFiw5T8RYPbNwmxloGX5cEBCRtYzcIHgaEbsNIjNBCsffbNsKLnZCbybtZcs-bCp0tyJA0CXruub_ojREtojVEYT5iJ3egMl7s7fsHxSGxa5JSkC8Gpvum0tnqUEyqsArutF7jeOUPQj-9TUNPo3K9Ig-suSUPLnCU682-1f0B-X1FsIiMqxUyDK1lfpvP56YYDMgNptd-kwRoBtmIO1MOzoeaXT_hc4KfSOfgAKumzSZrZvfstZY9m-FLdVKUjnTkpasII9j46Aoltu7y2VB2R9sRMNzOU7fRSvvHf-G1ElTuWUzFDtVWl9z5yfuOmHtw90uFksgqwPf2Gysplsn1nBavkhTuBoHbHXq7tYtbYrRa_CnWrCLkGITHHEwKgZ9Z5254Z6Q1en8GYMIJdG1VjWF1dMfB-yHmlYncvQyX7djg97Kst5l1tlWOggUuVCihzuiT2Kuzm2qqsP2cNuXt3b3fzBFrjHW1VH3cyPa3p_FU8BjoJxZwK2G8rfCoQYRBmedZ1gakLWYWcejDXhN5-MMBix8xpPKgCt8x_sFuU0486Pq12EmDZaeqSp6TM52nO-6hW-kq55wtYsfJAUgbJbJbpuWR8zKLeCwJJEaz_1n2QDhpw-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ebiLE9me_qRrA7Q0SFNjwSjBMbCL-2Mo957TmfvjBKGxdRCsJFBXp2-0PznhjX9-2vXlorSHB6Cy2o9JtWLUIx-Y6An0ZzwaEKi5NeTr8xwLh6SpVJF8vKD4ThjBD0zDC2Fui8m_4BWmQlCtPi4hqcaUtYZ85GZ0_FaLBJQJrFWhjXiLLf-cv5wiNod8stkNF5Sbi8nZEIzUUEgJ5zd3bjhlm50ikgFoxy3eWX5TX8dPPqnDcWGdWmkwnVAidVYc-Nt9Pq7FO_cXbDE2wwHSf-owNxaHfBXC6MTYVi552jKJC2fL0zp_dZe9FnOWGlKqC89jfqW8nLCjXGd1t5Utxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=ebiLE9me_qRrA7Q0SFNjwSjBMbCL-2Mo957TmfvjBKGxdRCsJFBXp2-0PznhjX9-2vXlorSHB6Cy2o9JtWLUIx-Y6An0ZzwaEKi5NeTr8xwLh6SpVJF8vKD4ThjBD0zDC2Fui8m_4BWmQlCtPi4hqcaUtYZ85GZ0_FaLBJQJrFWhjXiLLf-cv5wiNod8stkNF5Sbi8nZEIzUUEgJ5zd3bjhlm50ikgFoxy3eWX5TX8dPPqnDcWGdWmkwnVAidVYc-Nt9Pq7FO_cXbDE2wwHSf-owNxaHfBXC6MTYVi552jKJC2fL0zp_dZe9FnOWGlKqC89jfqW8nLCjXGd1t5Utxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFu0TAvfhZf8gp0fphBcCCf2vyf2MFDWP1U3oa8dwmc2OG8FctFrd7Rs8xYWbusu5jeZ3dANSGSCiwD7BhClvWVBnXPLxsjCmzlBqKezN0i4Ao8qr1Cr5A9eI5j533HTWQ9jE7iqsm5TBG7VNsZuuphAH_P0e-aQAV-lVlo01MtPNMzW0BEeO8n4_KVVz6efwdWH9-aLtnOXOoI3ql2W0sa4sToEUWnLZu3uwqKqoXAbZGQk2o_rPD0Bx1OdWQ-ZPdd-k1Nkb_TqYSiBqV7_dW549w1r6458usBHCcFuw8LvCLEDGC0ni4-x8UmwJ0eQCn2p_tz7E5ZVX6N5MJwsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=vv7pj-gcngBFcVnezMiR2n78mC2AkYdoRGIBJ05vAIgPAzDvCrob4cjqKiPZhx1sJem_mBnZu9fdEw0hVDexj9-5ledtZChO6XwPSqkunIRGywWVmL-kwQOODDtmiGInX7Eyn-92G40WXXHIgdSB5tIUdPo4WGOzKz0KmvRXax7GajBlJl6EpwobwfWudwwVVMT2EFkhuag_Rxi1EXkVpffHOZWAvFGuKF_BKFs889OYqq16NRY4m7jWu4z82rF1EeGHrTD-PLcH-n_uLCj2uoIcklAndABBcTTjAghcafzEBbig5mkaIbN_14oFFuP-aUTD-m-N-rbgD7SZmZJhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=vv7pj-gcngBFcVnezMiR2n78mC2AkYdoRGIBJ05vAIgPAzDvCrob4cjqKiPZhx1sJem_mBnZu9fdEw0hVDexj9-5ledtZChO6XwPSqkunIRGywWVmL-kwQOODDtmiGInX7Eyn-92G40WXXHIgdSB5tIUdPo4WGOzKz0KmvRXax7GajBlJl6EpwobwfWudwwVVMT2EFkhuag_Rxi1EXkVpffHOZWAvFGuKF_BKFs889OYqq16NRY4m7jWu4z82rF1EeGHrTD-PLcH-n_uLCj2uoIcklAndABBcTTjAghcafzEBbig5mkaIbN_14oFFuP-aUTD-m-N-rbgD7SZmZJhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzTRA-IsSBj1kGD6sbqU7wxopDviSyPmSbD5HSbc9kOdAqCOtSkx3cEpHmnLYOySbGckbAlVNjm651GVcPZn2FiSVKMSi4epcwguAESjg6vAfRYKb7idR7Sa7PsVq3Xz4Xciuln6xD6sKo7JZ1n4WCHNYSBS_uaKc12b2DFEOXQ4zRCdBOYOZUyNoUFyc-2mMEuj5bJ8bhyJUVrGLpfamhJ6kc55HYip6duAwDyv4pKc5cwymYReizfiV9cD9ZqUTWagmnWQqnl7HHFVfarc_Wo_T2-DuMN1ED4E5WnHPvdUhAJHxkmu9R-1Cxx-c1zlII5VIfpIOOBvJX9x9d7TSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=PaovzXaMX-5DSVN_mi1EZSkZaEBt5ASfAXMh-wuGEAnCKodrCp8mACH_DdFUIoy-57l1UCnbwFlXRlijN0cRssjcZ_iejZSqNJ4vJfGsDSg-tNxU3o0tY7Xq8p_NDRaX9zQDDFOmsWsrLJfRLJsM-Ziqjb-7FG1MyJEHIpE4v6NR7lQZXl1Slk5u9OztSYNMFOBT1Vu_POLQJRa8jAL5OV6yOD_Yz7fW1SDTsbaZrEe69ilBAAEyLNe_2Jcl1SO2awLRa5jPU9gpCgkVoKE7Y33ZfF7yRgGbmfPxQx6tN5aAbsWp4aE9HpF4RwvhH8DGSHHH7dFGmvN5bTYUHiNpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=PaovzXaMX-5DSVN_mi1EZSkZaEBt5ASfAXMh-wuGEAnCKodrCp8mACH_DdFUIoy-57l1UCnbwFlXRlijN0cRssjcZ_iejZSqNJ4vJfGsDSg-tNxU3o0tY7Xq8p_NDRaX9zQDDFOmsWsrLJfRLJsM-Ziqjb-7FG1MyJEHIpE4v6NR7lQZXl1Slk5u9OztSYNMFOBT1Vu_POLQJRa8jAL5OV6yOD_Yz7fW1SDTsbaZrEe69ilBAAEyLNe_2Jcl1SO2awLRa5jPU9gpCgkVoKE7Y33ZfF7yRgGbmfPxQx6tN5aAbsWp4aE9HpF4RwvhH8DGSHHH7dFGmvN5bTYUHiNpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=Uau-y8F9qCT03F3nqGGFZP5Dylx4AI8pN_BGEt9mhRlXqGL1Q4bJdDFjWAzgx-ZTxhOPpDwjQX5RhhRLZ8jCLlqS13Av2-2vqV4OrMi0WMMEeWGV7L0IT7BQ5zZX0Rvkqb1VmFJVUcXPZXcR9HO3BV2D9gwC_WjsR_L9W6QC_2E8c6FoKaFcTK-rbcj_Iu9N_In4_FDGvbxpmnARJpMux5ISDR7GGI6RBGbebgsXAI4T2jN-lrfu7IEhP91YSZEzqyVGeAH4j96gd5aXjOh51dXYFg1iR6-bNAqN4ZLWE1eY9VrJfM4ViH6QuyVPEbYWVlHqs6ibiBdonclU4LjFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=Uau-y8F9qCT03F3nqGGFZP5Dylx4AI8pN_BGEt9mhRlXqGL1Q4bJdDFjWAzgx-ZTxhOPpDwjQX5RhhRLZ8jCLlqS13Av2-2vqV4OrMi0WMMEeWGV7L0IT7BQ5zZX0Rvkqb1VmFJVUcXPZXcR9HO3BV2D9gwC_WjsR_L9W6QC_2E8c6FoKaFcTK-rbcj_Iu9N_In4_FDGvbxpmnARJpMux5ISDR7GGI6RBGbebgsXAI4T2jN-lrfu7IEhP91YSZEzqyVGeAH4j96gd5aXjOh51dXYFg1iR6-bNAqN4ZLWE1eY9VrJfM4ViH6QuyVPEbYWVlHqs6ibiBdonclU4LjFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnRJnF6AImRfmiP-KpehqqGf60ZAN3Op0srL9hbn8OSc0d37-e7dSEzssiVZ2CyVgYaAH4BH85JJR7Z6TFY9puky3ZIOMFW_tPEIvkJIriPihgU2LCLE-8eQ5tjpattFPnSLjRVBZ-YamUn3Kggxm7PkUc70U2FLHPB1YJxzJNco6zvLWkf87Gqb8iIN0ed_1QzpJehEliz2EBjpn0vqyRYxZlNWPixXVh-ATlISqUQ9ZftgWav2tJVBeP3_W-lX25xhZEczrk5xB_Sm1eajzoe-OKX38u9uI5GvO-wpoHFKz2BxQuYwRSGShtYN6htKKS3TwIQPccPRlW_uOK3Exw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=n9PhCqeDyF0c3Z0QEg_vK4a5j2mEXXK1QX3lulVrlMJMHOjvBjPqZra-cAnVLpza0SuNBj8cHQMV0MlkR46r-V8RVswLlDxXyWmsg_hicLlGqrFKuN3QR9H3U01Cjta5F7cXs-2mX1yiSdnecNENvryJQgnsHQFr6Zy6Lw1w9jU8EdAKh-r_oTfnoMb_Oew6mt0koyxh79O2G9NaBE0U6ef0flenP93dMDH7HX95yGwfWua_3yJUx768v5G5hieuKzQQX04x6QMNhPT_vVnz6YAve-fzhGJafJ_EmWpIAvsroDOO5ILcOeCyGpuf3ae46sKgLT4v7wIYrgJcfNnNyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=n9PhCqeDyF0c3Z0QEg_vK4a5j2mEXXK1QX3lulVrlMJMHOjvBjPqZra-cAnVLpza0SuNBj8cHQMV0MlkR46r-V8RVswLlDxXyWmsg_hicLlGqrFKuN3QR9H3U01Cjta5F7cXs-2mX1yiSdnecNENvryJQgnsHQFr6Zy6Lw1w9jU8EdAKh-r_oTfnoMb_Oew6mt0koyxh79O2G9NaBE0U6ef0flenP93dMDH7HX95yGwfWua_3yJUx768v5G5hieuKzQQX04x6QMNhPT_vVnz6YAve-fzhGJafJ_EmWpIAvsroDOO5ILcOeCyGpuf3ae46sKgLT4v7wIYrgJcfNnNyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHNs8IKZrLjnSb33uBzZX0oS7QRFWQVHfa8zVsMaF2W4qUyi4xLYRq6S0DkSGmpNbJcLs8gZEkAv69Yv24ixZCXG1WtnteDciCiFcRs3b26g2inF-d4NFykwjk_fAxtGBHJxoDaPtbjsrsuhq9C97HtowyfWqJwNsHHq-MRSCn_OqAREiEjiGo_skqp23iEXuzkuSODWIs-2NuoBNjvj5AeGvRZjY95atF3ZN-vwk2CzkHRDtyM7e1upruKDZMH36EfHZxlLu24vAGRb8DtzuIFMOScbYHA7_F9ohuslLxp5zCaWz0Zgxqw4RrjUY7Qc82ZW-OkMG3tvS9e_ZLiUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbLmpiVRPT1KZBhWVI7k85JOAru-8tBE5EHXoiLdLnevK5FjL5LOCewz5PZYAarU4cLBLLzj1M70NiMQwKZCWLb7qxTL4O8u_9Az8mwwOlbZhaZiE_0Pru_jSmwwWyChxhubb0Eh616DK1fXUasqd5AkKa5X62KXxxLQ4hoV9V5ekef3tReM5uP87g5b1_2tLimJXLzZ-7YGsaZBMSOBfJzona-wsfsIeiNcF3Iwho2UR3xHwYq-2exv8aKYmh1U-tZqJVDwXX9lTDlVdMGIPIa6hRR3QmSbZIz_od0DiqYKhL_ok1Q49Ml1ws5Lgzw3KtKco8qD8f7snioGo4O-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5RoaKP-S_w9DqzKKM_sj40JkrYzsO6hSWRvPt-GZN_dfNFvlmEkz3IEDjN1Gv9NjchbxnxuS9wIy40LNssPtNn02_Zz9dNzNyP9kkrBlL25YbSJW2RSt66oH_3Jc3PYRMiJW7k8N47lNdwymXHchm1FkOSqCDGIHA0n6eqcpjcFAIhu9bbZ1vI0T1mzemnz0Uqb59dFZtJyy9u2h1dVOVcTbzEZ3sZ66aLmNtK2xQl-Dzr0eo_uwWfae9J4jOiWOa7bDcmI-EmLdYbl9KIO_Dm1c0QluLrYeDBUmATCCBzCCYLHATy9hUa8kIID-XkWyJbKmL0gNGnVjABpRumakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAPd6ZP6LkUWWZVsG5j-OvzZV8QCjwIsEndTbmVFIrfjuPOYXGzot8mapr8b0r7vWmScg2r6iLNrmEbBKAXjossoEHKT4XmBKE5ZaYbmnCrpFW9ufGcBIW39EnI84_PeSDuGMSyNqBbINnJMx_c3GaA5q4GgMdRAu6Co6n0mWKSPKqt6Z6pUPhhgp0y43ZUS4K0Jl56_jOjYATboZg_PyqORWPRdYLoZJ0OBVEvXqpcBDsjnJkjOWswpTM1-b5SWj5EzrrwnzcIZHFdNmntoqOhJgW5BsZ6JsRBv5tKCY3RUADye69gJ924hzVroxv1jUIO1Bl47OAuyndkqLZ3Bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMFoIBMHb-DEY0rHE3JNOhxVS55MFs9UHnOmtUUC7iT885lFlO_EeivvV3uiMcC4kRdGdQWIXRbwqru7BeeeOYCTBThS3WOYb7hsUt3kVEBz-q5iyQFgeshJnbXVYZ9jbxgTckvAhRwRNLD8dfFdHUOMCqjptCvc6_aYTIlgDG79QTSE2MFHKiXLXyaRMdQQOHhe9BWYHCH8KdmUi5BaAb1GRrC3T9_knBpCOmvLJ0s0djmInGHkVE1mPweU5laQ3ADyHwdciXPzmsJ_kFrbFD4lvJrNoArXCPy_TCal7zivj_TQr_OvNSCuxNmCaiUGl6yjHr5_kwfRhhwVALDCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA8jW63PRbCRQiDf5B7o9ZssJwR6wSgeqh3YlasA4VAS1QLELNv5wzLEjbi2h9ky0iHdzZGZX44_BAT6hm2lQlVX_W3XvSZcevyrkrsY4AAlmc8pEC_DpTEDDbvLXZcY2StANACe_3KBza_dtCkUR1gn4oGAPFlWh4clSMWv96DtAt_6dQBVR0RdpB3Z1DZnAaJHaf3wopeno5xud2jmxdAtlKZQflaQmHpPYMtg6mVBLmcXVKW6RR7BaV5AgQQ4a3P6LG2Ue3M00_KMGxS0cDnJotSms9XDLQsJvltWi-AMG767FwdIbhNRVYeIgLB3KI6bn-CxxqTGTI5clgCTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=FMP9OAUrsix7GUMUueGwopfxvD3qXvs3jC9lWJTqPG7vJTUH513q7NCTE0cN_fm48gjp2Ffa2qLayyVJ_odyAQwczaS6Fo1ln3zP2XLYdNv20StPzk6UigOZuBSJKkEk2I9dBEXcnbxNj-dU3G-uc0um5HPalXdKxf0TOYJ05juj7TsW3gfaRfFEKGzl56cT0TyMcw_9s-bde5zPynMpTyMyinowkyzUUVOnkcWbo_LnhlSw4uAVREixD4_ilm6ds4vEqcQnq8hHHTfdYrwg5B3C9oof0gx8vHAseu9zS2s7B_kEGElEUeVetNJsMbImAVtsx58GXpxAR-FvvFYZ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=FMP9OAUrsix7GUMUueGwopfxvD3qXvs3jC9lWJTqPG7vJTUH513q7NCTE0cN_fm48gjp2Ffa2qLayyVJ_odyAQwczaS6Fo1ln3zP2XLYdNv20StPzk6UigOZuBSJKkEk2I9dBEXcnbxNj-dU3G-uc0um5HPalXdKxf0TOYJ05juj7TsW3gfaRfFEKGzl56cT0TyMcw_9s-bde5zPynMpTyMyinowkyzUUVOnkcWbo_LnhlSw4uAVREixD4_ilm6ds4vEqcQnq8hHHTfdYrwg5B3C9oof0gx8vHAseu9zS2s7B_kEGElEUeVetNJsMbImAVtsx58GXpxAR-FvvFYZ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHoAAEEVtx76kUfBXyJ8PzYgzPvbAWf4CjXDSiVTzQzRwR3eMqB7XG6MvRjfS8VBXyT2X4sTNejNGlxEClfn01YW_FTMSVI2EeWNI05-N8p29O2kP5SWyHfCu0DI4iGSF7PeCVM2X6_YAq4mYubNKrcbn09vf6J9498NopV4taeeNMhwePpQyiMqxiZeVUJgPr8UMQdEkxAdK3PEr05W0zUU0C175F04geTQ7GdA9g4vNqXJsBekEEXkAgpA43FCXQo32UuNkLydrqOnEvUMXXh35_NK9S2e3MmZy9-PmCPE9NcuI-sqW2CB-1ETtl2O8k2NIhKbe914Bf00aH6m8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKWk33wBxiX3lxnGRQyuv2z3gqtVFjS6jAWABgN_3HJNo8qOqY-nCIV2hMmDdTSrlfMyvGHxWB1DeLQ0lekOOz4-148HdpBY5nid9HpxGNgYac-buu0dZwOQNz1kXEE1-gKAa3hOoGkpPSQXxq096ULtNsQCLSAwwBQCwQB3prPFGAKLti0-yL0-NlbXZpNf2BIBkWoL2fSnRyaZ2Qn_BGeZ1LQAsqVgnQAfHx0w4NqrTt8RxcaVrJJHoCEuEtBzqvpcZDCPIzoShvTuqafbw1k47cxp8PUe4m1_zXRhyvx2X9FJD4U1kRjNYGOEpwjJkdt4gHnZDtuEGEYh6i0f0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9AWAmewmZsrYqxOHtlblbpAJu_GxB9ABngtZQKJRcdclmslyFV6E8NTkhWxS9IgQV5czVxahFtWTqBj3G8Dev6shQPJ2Ucd-4X4p0UGUrhUHTnzQZnjiVOPSVbmN-72dTy3R4Lry6Rf9stvPIQZNjpWZe9pDsthxAFo38O6U5s5Kkr3yFJPyV60d0u-mhj3Wkc2fKDl3FTBEM41MDJFSEVAtis8xmIdf9iJfMOkpUL4ljCd3b3d5-xGszfBL9lH3JBDLfGalIL8DVqKZ_N04zuIdNPjG2IREvX4E2st7mTGi88kM1gpXbTMuarScN2LIyV_B9imMJzg2NuuXj19Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
