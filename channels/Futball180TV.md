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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 562K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 08:10:41</div>
<hr>

<div class="tg-post" id="msg-100709">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnmwHvnpohJVVqL87NrZeaLN9jCEAU3TG-9XcohHQOieMaL6My-K4FlIosuqIPihsaqLxOjioSxKaBlSY0788bojHbFMj7wGBbEshJ9myD2sXhifZDVSqgQgM18RxbK63pKD-rkC4IfexnP9e4g3ksEmYmkqOQnN7A20uOY3sW2VJ_vZaKEpeFHHbVUvXEll-XiqeeDE2xUGLxmA76-_92NLBsNSWqHwKMCBQxEL-IoWdDLSWBbEiSxVpHrspJZNjC3TzqbXS15JmnLVuZC_zdA16idlCrM9WtUlf1KKVh2MJrm9n3HvH8RhmCOYwYnqlLp5_Z67DE75qHStI7JCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
⚡
تو این مراسم همچین قابیم خلق شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/100709" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100708">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور بی خیال آناهیتا درگاهی نمیشه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/Futball180TV/100708" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100707">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htk9Ew4rmr4lN92Z1zvJcMg2WHcPuXzIm83Oh5uCdv3wxglgH3jnA0zNMMkyJLE4-OEbhs7ULxTVzuatxZiN1VBQGaxwMlbGzXfOiHA6mEJoRgdClGBErQhXS-YWmaNbglrtcGMkyAm7L6G7isckFdSWAuFsVt8eI98BOJAzYvk8MP3ttOY8vvD5JQiQJbMDF-PBa_PMdU9jU41WRnTSPc-yhYNfGaBxhKytW57yF22wIKtxXzD1nPjmiIrori20SiHXydsUbDGRJpbHue3RQ14y90xgwhlgF5qnp9_gboAaGnQohhqs1hTOenamRUHkwLwHj7kOScttipi1E7B5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لیونل مسی: از بچگی یاد گرفتم و فهمیدم که آدم بیشتر از اون چیزی که می‌بره، می‌بازه و فکر می‌کنم همینم بهم کمک کرد تا چه به عنوان یه آدم و چه به عنوان یه بازیکن بزرگ بشم و جا بیفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100707" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100706">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdiJk6manYethXKxADFM4MbPpjheKQTNrH171chwR7MO4d_U82pQbNmvxAcS5iA6PMXbDZZeXNAkJC7WYHFbxhhuhNdc6_Mmjl3JCvThTd2fBs-yj8jchLEq26VrAVQMCyWJFlf8S4u2WNbeBY9w76oBwos79wwk2waIjhgHWUQKwrlELbx0yEcu7YbZnEEy8vH-KalKT2HsEpaD95ThQvIsWZ-nmDEurzORDEZx3S22Aar252SculPwP3hVcmWgC668P2OgE5wCkyGmrbB2CL3HDMAzhhcWXVnO1fuJlr90ttxFzwOMkkH57Nw-TpO-zOjAhQJOl62T1aFs8XV6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🎙
اسطوره لیونل‌مسی: بدون‌شک لامین‌یامال یکی از بهترین بازیکنان فعلی دنیا است. برای او آرزوی موفقیت دارم زیرا باعث پیشرفت بارسلونا نیز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100706" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100705">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:  ‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100705" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100701">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnKkiBSr6_RIzl8aGoae0qjn6rVm57jiSeeagIlvCbEP1ZAdb31zFGcH4dr4Wf4-2SGOezE8aDn_WW-7XldjHESXj4GSH8OJDFON7tNkoPPS8kcfC7BoLGRFZ0ASUMfaAgmOOte0Gl4XKQheC6c8d9NdDlhXn90MMHVejOUJ1Fwc04JYeA0DGfk9_i8qtNJis4KuwL7FjRqwY-gCy6YambapEOCxk-GauJrrEMQJo_Wuj-9bi_mnL7XqqKq9g57JE4AikicC30JPPjzLHrR3UsFf_ffo05qhzX6gfks81K7OeCBkfFb_8mx9CvzBvrhM6elLs8QRCIr5dGtKBjlq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2O9MFBSX3pljuFvQpqo5gWtZI6oH2cSQ6koD8ZiJzZs9PXY2-KmzFJpw2H5C2Fl-RAVbnecaiPuPeiqkyzTYAUDQVHAVsZaR56nSvfbwfCDgLSTxyO6Jhhw57BhoG0DhifkkuLRswkaDTYI6aHRSbAcYAsO4fauzI3y9rzWRbjUXd1rSh_y7OK4U7x8ED6MoOESPzOSPSgFkxIevC1psWymF6aUJWcLPBAYazH4iPL1BCV_HWuHAxnn-x0qa_JIQFBMW-iIiWDJKj0cxAqeuv_0_8QvJt5_2_M1l8NpgsMahGywibgPAbZYuVapj3wG6eVQKZY8wFLcMjZcZftCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5-1QYXStW5VQ94ihoWt3wkAP76aQnE4mSOaEl0oGy2qTEe6cEb9O1abWwS5h8NiSRf1rPWLd9bPM0Qp2XQC01hBpo0AKSr0V4MpcK6nhmn-Xhxeky9ZLZvBNkLna--7r9FzrxLJt0pxjgOKbxYtB2paszFKkaSBj5zOK52O7uDf9H84jgK9110pLLyNfdrdA5AQv7BRPJA-lULJ8sipSzkVjY32MNcV6klRj_NAJ-sFc-OTklgzBAECzLRKqUxofsjCkfpjYzun5iqUr4a_VZi4Izvv4abBnu_50OIvsMFl_HM06zXh6nzEnIEW7UY_mj6kHb32Ecz1tMM2bArd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpg8accI27MAIqqOcr8Nf2VhqIdQ-UUnMsBisjnRMOG2WClcpyjkETL--FGgpu7OgFi7bNmDZcSD-kl_iywcH_Rj3O7TiIAVx7b1lObXO0Vt1AKAZPTPMqbYmKeLCi4ocFVQkB0KoGYY1x7V-FYcLjMuRg9IlKxCm1TAMVsJFHV76cjFciRiyXME1UD_rDIfrUStSJ06Au82Yo-9Yfi4tn9qxSFJVvoehiMI2-VuwoTcVhcumUX5-tgxOUenA6OV3KO60-j83pq9oL4T37KH11rl1agUGeKvl0110pUnnKyPnhmn0Bx3ratQnTwrm_5_jvz-DahHLSHTy_2QyzNmaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇺🇸
📸
|
تصاویری از مراسم استقبال اعضای فیفا از دونالد ترامپ در نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100701" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100700">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ0S0iDbNaVv39AjIi8_OX5fbzrjCD8Ulw7QSHU_R1oj76ouK90KHk8lVsyez8-VPLvxmNXAiN6j5gTBgBZHxj0C_7FMDqzOa0dnZez08ZptcoFIFk5MmtSr0JveuaQUSR8Nd6ahy-_DCQDlfXTJxopvfnER8Sd3GTZGw7fDBvWDdJ3vBMmKJihlpy-GVwyubLX8zBhlwwL7xmwxqb-jLO_OJiuA6I-6bYhQKh1T7tExUkHJQLQg9lDl6pN8sFdeDBlefRmWAzJhelQFugymrEsdnoHNH2hEEQ7nCGs1BsaGIVS7VmMd59AqyuzZUNiNizzTGNW0tex_1WDy24qJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100700" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100699">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DylVg28ohggpDcs0firuiHix8dT4zog7mcyKg4gxAlD82DNelpOZKzS6uNYFLZvBzfjwNnHj0wW0XPAzC7W01D8LDgHKf4lCnPoCrU2e5ohb5J9pjV4Zh9FnEkQcIucBUNFCxADV6yUsaB2ToDclRT2jr3nFuRrxednmE_eod1qUEinl55Smpj4z0aCaHjEA-tCAIVZ5f9X8W8-ruDMg1jIR-W0WqS7uvEvLrvGY4RKwb8VLu_jIPANBrtbZbs4XC6xiJT3mqf6myCrzfdXLrS5grinDm3fo12le_uYRaMcrfnmAap5NDAs5Q1KfyMRGzjUbzCmc6c-Uqkh6BVnmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:
‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100699" target="_blank">📅 02:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100698">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_W5HhW0rHi72Ctr6_8cICkyYFhusrUIiUNOL8VzfkxZlfKby_DqCpDLKMKpe-hn4XiIgdwr6yam5k-vEmYw_Igw4s2jdRg0R_DOJ8SZTFeLYkVynlhsTVY0Utns69KLUnLW8BQYulJmH6Byffftb1MfAWzqUK7kyERVKv_B0JKg8ElphBE53UwfohEU22NuxRwgYMMSemRL470p9wFVObAyP522I35nCZVL-U85kwMQRstF9uVONTABBR6aD0R4F1wh24fGfi57tISCFcgVQfaS2uPtXMwpwsincHpqrAu7pfyEroqVFPk9Gj-6qG1xoClvvhTgGJmit24pmGSa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اینفانتینو: بنظرم جام‌جهانی ۲۰۲۶ بهترین دوره در تاریخ مسابقات فوتبال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100698" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100697">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100697" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM_N5s4l7_Aj_mhmPZNbmRPzr_34cGZQdsTFTjihxTkkHF2aUGcnAoJI2MiY_hEe7j2whcX03MoK5EsxgWSVlcrRFiV1yLbPrQY6Fks_NG1POFGtzAglunxVChIa3RtfrahmcF75Bv5KkHRwTV1UXfJAOby40Q9KSclh2sVFCvFSWPjxGojEQ2aLS0gnoQ027r4IdIkBdtRGbLmTbQX8GF_Rfpj92bA1u1OaauiAYNCNSIkz1vQWuaw8eQYPmOaF0Mdf6_Cxc4SCYIkqmo5A0Wux1xvyhESv5l8dWWp4ZGmFSRllkuBWkHMuIMB95CTYSQYr1I1e8O6Pk5bFuF4GIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
🇺🇸
ترامپ: دموکرات‌های احمق در انتخابات تقلب کردن اما من در نهایت برنده شدم و میزبانی جام‌جهانی و‌ المپیک رو برای کشور گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100696" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🏆
🇺🇸
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه. چون فکر می‌کنم بازیکنا از مسافت پروازی که طی میکنن کونشون پاره میشه و جذابه برام
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100695" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=EAQO1Zz-5iPvgWYzwVKKHd0llOtJZWhB0NmRB_HsT31iXXg9ioL8PRKEDktUgZ9THiEoFIB1je0C7mZMvSl3IqeFqehN6BsocQhNeMWVFRJODje0PjGb8Ef06KB2WIYzWAdAKaDuEo9l3GiuCm_9OnG4ucvNZHqcLUY0eZte737LEW2_HzaNkA_aNacOybbcn16_uTVM6YYnPQ1K8gpiXAA5ORdB5_9mc5c8OB4CMLeeD-OGKG3N_5Mr7xrJBHjaIel6QIqhMuJtH83jOyJrJlw-ghI4gDEm4cL4N4hHcbTWZVT-JxCwK9xsHfUR1WNjgpSwGO7Ua3SLiDPLlIlkujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=EAQO1Zz-5iPvgWYzwVKKHd0llOtJZWhB0NmRB_HsT31iXXg9ioL8PRKEDktUgZ9THiEoFIB1je0C7mZMvSl3IqeFqehN6BsocQhNeMWVFRJODje0PjGb8Ef06KB2WIYzWAdAKaDuEo9l3GiuCm_9OnG4ucvNZHqcLUY0eZte737LEW2_HzaNkA_aNacOybbcn16_uTVM6YYnPQ1K8gpiXAA5ORdB5_9mc5c8OB4CMLeeD-OGKG3N_5Mr7xrJBHjaIel6QIqhMuJtH83jOyJrJlw-ghI4gDEm4cL4N4hHcbTWZVT-JxCwK9xsHfUR1WNjgpSwGO7Ua3SLiDPLlIlkujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترامپ: هری کین بازیکن فوق‌العاده‌ای است، اما شاید در پست اشتباهی بازی کرده است
به نظر من، شاید آن‌ها (اشاره به تیم ملی انگلیس یا بایرن مونیخ) اشتباهی مرتکب شدند وقتی او را به عنوان یک بازیکن دفاعی انتخاب کردند. آن‌ها بهترین بازیکن خود را گرفتند و او را در خط دفاع قرار دادند. این موضوع کمی غیرمعمول بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100694" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=StQODu9NrYHaZEWHqbb2BIehozp1RBLGJ3c6MYGx2Mv1W9_5qen_OA8KBsREgG7yARXL-xQe8ID0Hf_U5On0P6GP1-O5_cSeDFiAKzwrVwFibuq7wX6UotZNYZu4V8gdXWvWcKf1pj9FU1DuCAV1vhyhkVvpaZRi7tY2f0Tnex3l8xnyYZZPs3hS2NCeRvg87HRzkjzHBDUiahcnCsTgKf8TCL9MhcuwITlaEFZh-U8Il-P58o4HyH9KnOEngPed47hNNpYCaDCSLjBAN1lZS1Ud3szJx94R37NYp7n1CgiKxJnKxUL4c9glI0XzRmiZ4HsEbHokpb7FRJ5iKzC8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=StQODu9NrYHaZEWHqbb2BIehozp1RBLGJ3c6MYGx2Mv1W9_5qen_OA8KBsREgG7yARXL-xQe8ID0Hf_U5On0P6GP1-O5_cSeDFiAKzwrVwFibuq7wX6UotZNYZu4V8gdXWvWcKf1pj9FU1DuCAV1vhyhkVvpaZRi7tY2f0Tnex3l8xnyYZZPs3hS2NCeRvg87HRzkjzHBDUiahcnCsTgKf8TCL9MhcuwITlaEFZh-U8Il-P58o4HyH9KnOEngPed47hNNpYCaDCSLjBAN1lZS1Ud3szJx94R37NYp7n1CgiKxJnKxUL4c9glI0XzRmiZ4HsEbHokpb7FRJ5iKzC8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100693" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=NKaGjjPiCKVZ_1KwcLH8ZDACrYyyfJ7LGRVZK89cgDXThwU4_6Q9pH1iUcjZfkjAP7eXO-v8yIHoFiZ_R6tMKfm0i_1cLQJQvivtzGS43C16WFGYeqkEDbDId_KW9RZCHhq5LNtdVnjjeDYjoWLqRCNK4mHMvKYZTuKdt0uiXW9rmLTPwf5DSxGC2JXCsaXaK3VBWa3r6W-5R4iIwRohri6GXd-w0dcNhr5rjc0G26CpOzhCMz0z2Hz51hkH-kABoCkuRbGY9RKe6Th0vb8c8MIEVrxfY1x4ZI0O2aiMJwykFsuFpdN4pm6QB2ja9M289hJPj4roMf6ZEoVx5MkNyTfK3_KilNWeS9ILt2LSXuXaTAg1oTnEFAWjGEF6qd657ekbD-5VPl7lL7qzAf7clldL4pSLoVBBfwxZFtJ9IaDdF0sX28-DXHP37n67xt_IF_JnrF8Y5Ns2uw8ycfP5PcOyNS-ThxDmQLATyE3830TWPLrNgJ6Xfk1LEfZHW4579lfWCtZF1MrDC2TEdZBEABN58Z_flRa7g1bJUu0KxVRst7ACYzKq8E4hW5p1Lp0LCoW61s8Kq-20PYWwIsnDRl9WLRXMTYRIiByzgIdfV57mYi0qxbbVEgbZAbDpH0cjJVppmV2BADkQoq8ZTXtrx5a2SBbQc7sCsJ70YFwXQ-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=NKaGjjPiCKVZ_1KwcLH8ZDACrYyyfJ7LGRVZK89cgDXThwU4_6Q9pH1iUcjZfkjAP7eXO-v8yIHoFiZ_R6tMKfm0i_1cLQJQvivtzGS43C16WFGYeqkEDbDId_KW9RZCHhq5LNtdVnjjeDYjoWLqRCNK4mHMvKYZTuKdt0uiXW9rmLTPwf5DSxGC2JXCsaXaK3VBWa3r6W-5R4iIwRohri6GXd-w0dcNhr5rjc0G26CpOzhCMz0z2Hz51hkH-kABoCkuRbGY9RKe6Th0vb8c8MIEVrxfY1x4ZI0O2aiMJwykFsuFpdN4pm6QB2ja9M289hJPj4roMf6ZEoVx5MkNyTfK3_KilNWeS9ILt2LSXuXaTAg1oTnEFAWjGEF6qd657ekbD-5VPl7lL7qzAf7clldL4pSLoVBBfwxZFtJ9IaDdF0sX28-DXHP37n67xt_IF_JnrF8Y5Ns2uw8ycfP5PcOyNS-ThxDmQLATyE3830TWPLrNgJ6Xfk1LEfZHW4579lfWCtZF1MrDC2TEdZBEABN58Z_flRa7g1bJUu0KxVRst7ACYzKq8E4hW5p1Lp0LCoW61s8Kq-20PYWwIsnDRl9WLRXMTYRIiByzgIdfV57mYi0qxbbVEgbZAbDpH0cjJVppmV2BADkQoq8ZTXtrx5a2SBbQc7sCsJ70YFwXQ-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇦🇷
ترامپ درباره مسی:
مسی به خوبی تحت مراقبت بود، و ناگهان او در سمت راست ایستاده بود در حالی که بازیکن بزرگ که او را تحت مراقبت قرار داده بود فقط آنجا ایستاده بود. مسی شوت زد، و آن پایان بازی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100692" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=OSLsuoyTvqaB8i6D6c1MSjW20QCC1JdYWoRpZUvlyoz2EdHNkT-XLpqSgrCT9QMr4nudR_cqcuKKdWQnQ0i5oxndb44JgekPBMoptMFSueXU6j89MGe6lftuN2-TYjNRXLGoFoP0bTy10T8YVcEU3OmJpFRERluvNmcNU--4X8zoxdp8LG90sBq31ngumyLr18ZdMbdb4F9DDWpNKY1bb5KS_14EJCf-TEuZC10MShA_omBKmbOGq2Zug6leViX3ECNX60bML1AwsJZzebVR-WCIhS70RGcGS7EHjp0ImoUbEChBIsfPZdnwK5qKhnjugwVOHYx4yEppC8_KJWZIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=OSLsuoyTvqaB8i6D6c1MSjW20QCC1JdYWoRpZUvlyoz2EdHNkT-XLpqSgrCT9QMr4nudR_cqcuKKdWQnQ0i5oxndb44JgekPBMoptMFSueXU6j89MGe6lftuN2-TYjNRXLGoFoP0bTy10T8YVcEU3OmJpFRERluvNmcNU--4X8zoxdp8LG90sBq31ngumyLr18ZdMbdb4F9DDWpNKY1bb5KS_14EJCf-TEuZC10MShA_omBKmbOGq2Zug6leViX3ECNX60bML1AwsJZzebVR-WCIhS70RGcGS7EHjp0ImoUbEChBIsfPZdnwK5qKhnjugwVOHYx4yEppC8_KJWZIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇵🇹
ترامپ درباره رونالدو: من رونالدو را شناختم، و او مرد بزرگی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100691" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIhnwbjmS4RzoS_0h7z6k_5PoEnotC3VplowTbTXfMQQPk3SXSwDsxKP5GJX-qlIc8F2j9p9QWibJZa2aJ8mEiQfKd9mYzP8s4hb68Nz8JkMusnggwPnH7vDyCpwIvGTui4FNjU6KmTwN3uBCZ5D-vnmeO10SuVYjt8T8X4tpp3ak5FUR2JJ30w2DUxr8GcLTJhLIE8QmCpxRtQFIw6YUbMwa_0cxWlg0LUWo7PD5LtATD3mB7UUC0wRaNZG9anLjGpDaPfvwY5r_vu8kVORd6ELjqvfgcNPn_4ceQx7i4A6HemdLt1510vt2tubhUzVK1Iz-mXNV4u6m0vcbHY3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوه اوه ترامپ و اینفانتینو نشست خبری گذاشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100690" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dns4c_95Q5wRhyV-Cm78DVTRTBjQIGss2yS-xeX9K3LS26Q13-0BGEtNHvVwoQqrsbBcia5KU51x0LtG6sq7dPmQgJMxbFIp-EecYIditRRDDfAUgLROD-W-T3pgCnqELyp9vEt_qwLpWzZVeOAK-n_NNB_0VJmC7cPn5FaN_MRmXvS_ukE89vhERQZpLED34uQXrK4I0kFCYNkrSiu4f_pumDIC0O1-vmNRxKJ04JxbWBaOdObYWXCSRphKdQC3OIwa9oCSnvXUrjRrb5WNlUOO-GAcpH3FM78LwK6iV64S2gClOMQbYyanfZDhiQa9sWAr3goHAkN6r_64mw1nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
رودری کاپیتان تیم‌ملی اسپانیا: لیونل‌مسی بهترین بازیکن تاریخ فوتبال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100689" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100688" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6Z2mbM1dYU7Zt8ycRvYrqaVEwFdNHuDuvsPw1VMfSlimcHIllu3TgVymLoBV4EJWX6QWPEK40M-0cPGPbo5GB3res2oC0o8l97wQ1XtWosXFauz8KTl_StX0fsChpJMfl385dSlKtPHsuGurS0OqO2vYZWhBjkqWkH4WSJC0vor4QNI5CHju4FrjafcwR_I7retCWx0ZuQbT9jZRHEZBeJ-sQa18pCSNQAx30sxgZ8DGpE3odgmoR7dtTV4ddDQ0ke_tlANI0wcEK0qBjmjKjvIBGloo5Ffd2OU2DVRbT4EEenvmeLo6Ih8COhl5r1jQDOwSDv6vPvWZKpp9OxfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100687" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdXzkzWvSKxhR0hsI32jA3yZw2gS1ki4M628p2LwHv47TRHxwe6nWuEIiGiyhGQ4Eyrc1TYgtIs5HCdbFvieosZydThWOJ84pT4eoa8-_Dkw7u3xYbCLC_ZBcOzpeuVXdB30thDoxfLgLvXmb5eTxhZbNgxpz4E-hdeFIWYb9GpSXgxgysQhfyW_bKGwAFskRfYC_mDC2vQoBI2WkNTK02Wkxl_T0Yw9cRrcwt1e0phy-GYbOqR8G5G7Jyi7AOKOHSh0Fumxbni5rTHRQn5gcDS5_TW35mXVvTE7FaHZd2UPB2xZqB1MNey3yHN0XLhbd6rPu-oSEPOgXmU40B6uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب‌احتمالی فرانسه مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100686" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=QkgsH-p4emj7DU7sWzs-XffIoqLCvVkzhzcs_kagMUBnIk702NTnIJMkESNk6JdUIX-kVYrDRvFoomDnza3_Ys0nPA_2jXU1k_zG1miC6Ik_VXZLul50u_m2YZitSHpD4ThTEoi4NKS-ucRpYLwFKPNemjmaQJqzbQuz9yWic26Z1kInCXidUoc5D7AzonfwGwmwtLt77MfessMSv8DBC3oZmxj2YzkwPoFWHCfHMbBB8UN3UYc6NA-0caSZZb8VTKptqp2zxM-Bu0IDPEKVnnxlYGqHMUg1Dmj5EAXklCT1rrHc87-JO0ziF7xsD2lmMN8WZRQTFv_apQvCnawLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=QkgsH-p4emj7DU7sWzs-XffIoqLCvVkzhzcs_kagMUBnIk702NTnIJMkESNk6JdUIX-kVYrDRvFoomDnza3_Ys0nPA_2jXU1k_zG1miC6Ik_VXZLul50u_m2YZitSHpD4ThTEoi4NKS-ucRpYLwFKPNemjmaQJqzbQuz9yWic26Z1kInCXidUoc5D7AzonfwGwmwtLt77MfessMSv8DBC3oZmxj2YzkwPoFWHCfHMbBB8UN3UYc6NA-0caSZZb8VTKptqp2zxM-Bu0IDPEKVnnxlYGqHMUg1Dmj5EAXklCT1rrHc87-JO0ziF7xsD2lmMN8WZRQTFv_apQvCnawLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حملات موشکی به اطراف شهر یزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100685" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4pqtYAHPqb_CxX93c5PnAdejmZzhOPMxpMash9q9QE-4ReSGWdP-ERxtrQFkJmMLyGHDEc4lmO89N6dbKPsx2P8Cjqj7TCBOHFP7HiXzwrSLkkDLL9tQcj5CA8JaM9GAe2YeYRuhlzqcUlQ64g3MG8xsNgfi4SWUvo4Kzn5iB34JicpvkX8hQSsA9rpcOcV0aWRrnVgJrmAZSuTp2wl4g4-XJKPB5ie8EWEeoMtv8jZGWjrg6kJVSQc2532Ml6AMuEnY0F0dmSj8oUb1orWgY-4qWVGSX3RY9lGJILoUdkaN568k9mun4LqGx57s4uMmIARs96pXMQmibfbvw3CWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
آیمریک‌لاپورت مدافع تیم‌ملی اسپانیا
:
از رفتار فیفا با بازیکنان آرژانتین تعجب میکنم‌. چطور ممکنه یک تیمی اینقدر حاشیه داشته باشه و‌ مجازات نشه؟ امیدوارم در بازی فینال هیچ مماشاتی با این تیم صورت نگیره و در زمین فوتبال قهرمان جهان مشخص بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100684" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدئویی منتسب به حملات دقایقی‌پیش به شهر موشکی لارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100683" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100682">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100682" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100681">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5hu-b7jVNAqSFwr7p5RhPMx8tGDTrKLSLWdV259Snng2tr_aLnDQo0byhNEnJrgecMZfmcUxA-1IZ2tY0PCscuAs5FrHaMgPQEgujlg7jlckS5F5Fzgpr7OwN3dFtNrPQujVXwnauPSd7zM3WmqNeCeJ_EDezwVENXynwZ8Nx8ygEsYsZpZ07EnxmSdY1v8bv2f2DPdeTV3nFcZic8kiV6nNJRVywCjbnV9HtWtVJj0nNvokaAq7urhqLM3v8f8eBJMizhWVa_0KwlI1Ek3Uv9u6pQAJe097AMYDZYE1bhb7X7Bl3LGZDHWpG_JHt-bcwOBQp4su4CoffrSkJKOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100681" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKCPV7R14mbYAGFinzjgEP4V9OAyS1qAdAZo9HA62znnI09VWgpJuxctQvA34vpJQLc90gkQL2insFBjFhBdIlRmD8aCIEv0sHy1XR6y7KcPI0xCBf24piVvduugx-r92O9rf-HI23wnoVVj42qCeEVmHwRH8jHtsS_62WEidUDX9w-kjAx5cQ4BuJ2GZgO88znlw1WkLyoxw_7YKw0oiGzb52OzGguJTRY1F48XisI3BEgyajPTq5O5fkPu0tBmfhaKm3LEhksu2UupARJFP5CJqBBkNW0zJBuMrMILgpVXSqeTgN2LT1Hkl0NOmDy8pEwvokNDM2NYm0u7r2kC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚬
🙂
شرکت تروث سوشال متعلق به ترامپ به مشتریان خود اعلام کرده که میتونن با پرداخت ۱۰۰ هزار دلار ماهیانه،توئیت ها و حرف های مهم ترامپ رو قبل از انتشار چند دقیقه زودتر دریافت کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100680" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100679">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلد مارشال رضایی
با نظریه جدیدش دنیا رو شوکه کرد :
اگر فرضاً دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100679" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100678">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMWlookjNMlJivcJxcN1YqjE2EtbCTmlJpukNau_45lrhoqG6I0PF_hRNGvMqKZqCWE85iaE97QsdUqGPB7gxatRlfL7HxzfQY0XufCjTCqjzgK9PZSDompgT5HGZapKKhRVTub8tXjm6H2OoXBBWZi5fjTh6lSklPDUl1CvoAZpTzyL7p_zK9Z6xd3CLtWTV6YJooJ3m6TasaiXnKcXzaSWMJ68uOJS6yBO1Wc6hkcGjuPDuTDeBHOBlCA5BNdVIBltjCibHPiOxNdqHhWSBBHNdLpYvcq1cGwebCVYiH04qYHMeYlVbAaSK9pi61a3P7mbtrHU5y8fIOuCg0R8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
😍
یادی کنیم از استوری رونالدو سال 2021 برای علی دایی: یک قهرمان واقعی همیشه قهرمان می‌ماند. افتخار می‌کنم که این جملات مهرآمیز را از الگوی بزرگی چون تو می‌خوانم. ممنون علی دایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100678" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100677">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8e7Gk5unhz7kaSFf5CKGCWmUxCUV-3G79y4-O5s7BQw-pXLgmBIJ_spkL_ShqC0WdiqI1NYpUo4IEkiG2r-7zdWwkcPjzbVgVPea_RV4rT71AYWy8Im1yAa0PUUx0MG0QtuC2xyWHwyXV-3hv0v4bizvQ4JlNEqT2yVPGHgF0NQxn6jMybfA4p9vZgtpk-447naGG12MKuOrrnRUV97iEBXkx5WNRF8ilyVPpXw2EaMIaKnxGARY72NK7NODzOZoTBsKrdo_ZZskiz4soRzNxvbEqCstsVHtgORniaGy-e5WhqKBK_8hOYtIdWGeWfDk1I1TeDFni_JlcdvoT_MoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100677" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100676">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP4ym5rwPEFVjIfGSEYcmPULdmHy6LAWcRmcVSbFX8EOfK4ZYsmVS4E9LetlFa90hIAq-XkSvKeljMlXiYE4ce3BghVhv0JeuOJg7Cm8YRPX3IMV426G_6k3yd7x9TqmuaSCIMP4By5IEkBKAPF73bSylEyGh8u3I0RlgnJDnOEP4Ntq7TxHnFm-dDclMHMVKm19qnwlod2RML21RaS9IOwTIadl1L0nLijmm3IDs0944c9OtXyyqyHARBjQ9fN5xHKQ78U1c_q5U5d0Nxe8KbRnCAFGm1hDfniYtUzP_9nuJzbz3QdiWn-H_WUgj4phgvNEkQzeePndidYkSFgwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
رونمایی رسمی لاکرونیا از اوبامیانگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100676" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100675">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100675" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRi3AR2VDIpbWXVwZxKQUvk64ELxz47PRbY7J9l5veEaa8q6wFp7fV_64EdiHApNDd8viQgtndmN-ox5-hhfQE2aTxpuVo5msusv4vW_S36NLm4UWN-RP5LPI8C6kkq-iDQ-WYbYlRfqK5bKA1O_GI3ui7M5KQYm1Ntfq_LA6Zs15d7XTiM6Qi50-T5rhDeVgiF3ToJ0dWO82lFTzpfNuYK5FW_Qfdw20mXt6_mo2Uk0QfSe1e3gJ3OstyQHykS6KygYMXIFAHTuFtOfbBs1RTglz_BOsSTOMr5aGdFLymoMh9b0Yfz5-vCk5yp1j6EcfpPyi4O02LfXk0BXCuLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INVUjjRydUedMw0JzhYpiZtRDNGawHQ2YEyEsueIUMoEGcmbYZLE3ddMadx3z6uNz0Ikwt2Lv9MiGlyQUzqsUxv0eTdFbf4bNJSwPyngWMQRACHG4psAfg1H7TDP4OPU19VyKX97elDdGeeIGZY5QCwSs9WsUuFaQYGDY_JzDnFHIePLPN7JDNDH3FaUJqU0KNeW0Xzs3NcQFuQqU7JyEWrcOAhOKB5vIb3j4-6nbFWntXBPzmZDhK3d-0Xw77GJTL02sxxDHraHbJ3WgGmWazJswHXRlYtPjCqA73cMz5tcOWXMgBuzFJmxeWAHOuM5r8hVQiSRs6HtDfBIkuZUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpheum3ChsKGSI-tS3JEh3PSAWdrstpInEhdkxfCQyD6BvWxu0R3Z3pK3S9HQwNBI7YS1yra1YPp0D2XXlwBcSXMQTDJUUzGRqGJjfMU1fnjvp-UI9Smq0U6FZP4cwYIrLxbAsmMenn3Wi1HimNHs75U7-AyeWduC2nuxMlAqqOv1X6GccarXa9FZAdch-Hgq50mQitEFkioMU--_0_oxPMpYK2hSmdTbLSVlsGsoQK0dUtKjn_q6zI3sQWfRccqZV7YTOi2kTw1XMOKoLWuEiQHz_j6dto4ycGwpP6mDZvEHsMXUtV2N3O2hgP3kaiOITYyvMtAnHb5QbY6vW_kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZnuI5IU1lEQEABw1rGDgtT0GAaWT_DCctzEX-KMpPXtWPLba-X2gr3fjku9DTXzhFuXrih7drfqLlXvbbg16Ua0xWanpSMOU7Wz--qRoiIu_CqNbmP9MlDSG27ZbyooELzrUQ1mw7FjJB1Gk67yQOUXO-AszZrm2YhmNi3N-9tzmUKNXPrasV-mtCoLT6EXGtdnBrpqtelkHxiGEJ9IsGELHpcwGF9wxdaYw9UKqD55pm72fDGPYu1NQCLf9jhTRMR24UIoNvlgUcvQksgfdK9Vkd1UT6SiTgivITWs7-YjaUCopSWOQ9AfWMnnyAN8iYFkLh1TSMHnwTHMRABlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6PBJSN6EwwT1C8zOrEFmrGaq1xC_DfDGcLhTAGF-UJ73ixMh10AtKfFcnO83V6wXWSublgaKrN4qa9ahjSsCutErIlMCGYGHRGppZgrWyotfmho5gbLEIaoU0BbzwdQ77j0oet3DDAUCNO_yiMZ9EwGM7HB7oMYdoK1bjw6ona2ShQLlZ5OW6U5GKKCyEPH9jyOhrp14WhsyJWmtDHwM-rlVHisRqnx2qGgH_RvMKnXpnHfQxpF_o1VoIlArA3-bL29SvVF7tAkHTXakK4rFEN8bufmpEpy39iaFfPBEzk0BT07S6JOzv2BnhfKvpAZAHMYi8w50yMitNOfNkeBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxjaV3ykxL9I69ys1j2mAfUekLmoaooiV65gjYBB2gkl97yhbquSlAkbKSZxWMk5G3jlfu6FNMaOk_MtDvevv2h-vqdH7PZx_rLGzY3AgchZn25sOT2mqr2CM_OwSUQjem-ul1NJYpF7DI4X3YzamXhXsMIdRJoBv-IMTTGoDoxZd8rMxeaEoj-2arwvCcci5rH6Ips8PHhEojoR2atyVpf8W5T911HJqn1OwfUFkFQbkokUpe9D6RW35InvCV6PGyQ7g0T7PfKPfb7Z8H6HXsRCX0zAqzEAOOR0qaGboeWZbY9rJkrDFitkwpEIYgvo865lle9KG1l7pSwoHT75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
والیبال ایران مقابل اسلوونی هم لنگارو هوا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100666" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLb2htvBtjoHoLIwLTlBlAKr0TQgxJknr59P9YwLRyLDudtuU2Vs6CLWXhn_GP3r4nZTlzTDU8J16L4qV1dPU08W_phPkAFnYoAoCEAFF9n5Jeylv3G9EX8jx9mrDoZ1hH_ypS86_FFN91yjYIPhGm3jcq_a9wpMnrTS4bNSca0hdxeWpvFujv47YiYjZkR3VS3wdxPWRWD7FBFE9b-dkzSMylQQJeDkwXiQsD7-PwwRIwDugjyjprWIeX25aJUC8vvkMQVMZz2YDG1dshLAOn6gHRv1fgS46Z4DJlaT_CmdkTOwQWNO2I8C67fn2eb3qbDy_2W73nTlyBPt6Iuoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wp7OCrW_boBG5MWmy_PvgQKp_uf0EwpUxJTsvE_Fge8WXtFsNNUe1tgjl8v0LQ9ictIbW3jGlmsfTkCFp-7AQEcbaejtsYPfepBmhAPNHcUo6EyllnFg6b7cFvjKPcxnusjdlPOpgtozjgFmxCOWW0nweq3TCeEaVdUjsFSjFQ5Rmg2A1Nm0ovd7Em8y913Fuy_FB70F-TfaKb9SuTFuTJga4nS_JLeYJblkXdzHBQ8dm0AiAAzAvgT9Y8mXqtFgJCAVSnWaqXHTCLAiZ98IdfThnpVS6gq-iYac6UNVWzT4yT7RKjpF3rpjrwIWuE-VSw0WuldT7u885ttCjB5e2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زیبایی کاپ‌قهرمانی جام‌جهانی فوتبال
🏆
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100664" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu0n4Tla3eFKsoXqk2DxmCJcCdGSd6Y4Dd0En3H3t_hzxvAECsne_-Wkog4FDd2Bw5SOVb2Ly3k1Bn30gi-L4Nx85e4Md958jYGwZxvYGRxJMmAUsqv2rAIHUYkCrjSmCTfG8G-6PWA4cXW8i96W_vSTdSFkhmZjZwV0Ucrq5X2JK3VGiRhgmoWzwVQ4L1QTdIjAVoP1jJKUTSba1BPwDAYoGMawchU4rxOW5BU4OTX05T-yJwnQYwHxVXnC8CJe9bT1UnINRnsa_rB1HWdHgbs6kPTeDG--vufCLY6N4EffItDVkpI_2doGQq7f4diVVf5UaKuyqmRW-34ut15Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حمله تند و بیشرمانه بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100663" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGyN4QD0ClYdTquyeXUMxfGBTjtiHSO6EtHq2RgSGyz9na6YXgi97nWrp9fKrXAKI_JsTkLn1-5GvFxjzVBHdk7Jfju-R7Vl6mQGaw6hd4lgj05scs4LzMcuNMMpPRfx58dk_63TK3I8BmT9G6swrFXXHqC2AT-hVeciTVj4pfd_YYNUZq7s-yhZQ3M8uE-dkiBjpGGkmwKTyoGq0bSKBDbq89QQKjLSuac5rro6DlaY0hcb9Pp6lAsGoM0jZ7EiUEHhcXSa3zfUD6t2gaEvo0mEOWGxuUVaJZpNOZ-VHsEmewumihAsBGSdflvs4xhQuiikoWzOQUfOieq9bG_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
بازیکنان انگلیس هم قبل بازی فرداشب رده بندی تمرین رو دایورت کردن و به خوردن فست‌فود سپری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100662" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100661">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGSWMV1TwFrwxZVT3F1HkGLRIwebQvdeChSaJHiTakKvsBWfLd-MOSwSLsyHBvc4IWxagsIpFkhblk7hgIRVSAFsTLO6nuyjKQniZAudFrjrvJIC0Rx5waUpYDwUSDs_TnlYVYEHCdK_7sdjmZNEqNwP41td3Jftq5gYzPmeauB8v6VSwDn6G4EmKeaGIPaWfxklogm-qPjsX7ZD-GXkp7BI50vSoWL-xev18D0ZlA7fuHYTA_ElQrXfaz0XvrdaJlEC0o0rSKHlYsNkEKGrk-TYpjWIsGVYsDzhwzUdCTDx0dY5nEidq9RW9F_kNMPOPf09jkeAE47pHNRMzrH43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلور ناواس:
من فکر میکنم آرژانتین فینال رو میبره چون واقعا داشتنِ مسی یه برگ برندست و همین تفاوت مهمی رو در یه همچین بازی مهمی ایجاد میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100661" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100660">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L52VF8MIIaAd1DaqMV7kDQAjNgdFYpSCuj1wMkYhtcJfLA_g1LWAQwvStcR4srYvkX_gBiD6UH9kb1wHSaFifsVVAvNSvu6ku9ZLi8qlmcn4e2WV6oShCVyY4rsd3jbLn0h6jCblshtowo4KQ1Jk-3k0ddTizlX9F2WD0Mk730RMywplwfx9Q13JD-Y7t7QqKtKC-R-aqzRtiQm93A7gcoW2n_cJOyOUDP8p2dU2bbRO-6QbNosxYyuMBJPtQZvr_esDtHm3LfePl8DWFpqOWF9-_EHO8E_EGAtHZQhHdF_JMIRfI_EeEZXMHj2WQ4HbgiLcytnXSgwDG_4cuvtUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
دلافوئنته:
مسی و یامال
هر دو بازیکنان فوق‌العاده‌ای هستند، اما در حال حاضر هیچ مقایسه‌ای بین آن‌ها وجود ندارد. چون مسی سابقه بی‌نظیری دارد که هیچ بازیکنی در تاریخ فوتبال تا به حال به آن دست نیافته است، در حالی که لامین هنوز در ابتدای مسیر خود قرار دارد. امیدوارم مسی یکی از بازی‌های درخشان همیشگی خود را ارائه دهد. اما لامین هم می‌تواند یک بازی فوق‌العاده داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100660" target="_blank">📅 21:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100659">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu4A3P2k0PIkoWEPJbrxMbscUz8nKpwm6fSfSwwyQUQ3CiwIxGCLbfKIhvMJRs3eiEvOtW1LIKCG-2_iDS7iA0pJyj13-Vwzkg8LZtCY5_k0WdZaQMyZGHhUS9D9Kq_x0FnnU8Qv1kinK_mbp776WmlDCKng_gA9Lfhnpyw3IGPRbGjdoHHK1u5BYR4e5TwuJ1tTTN1QZEPKhpoL3Aq8P-jicx69lMF3URm3JeiZ2jEovyOk-OfnioUGsMXl2yYAjvL4xhMyecr2n3mHhPFirShOoCOpbvj6d1RzfaP4u5UL6kjr1sQ3VXa5jrCJWcr4cPKoJDykvfiiEBdfzvVs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بارسلونا در یک تورنمنت دوستانه سه جانبه با تیم‌های ناتینگهام فارست و اودینزه به میدان خواهد رفت. این تورنمنت در تاریخ 8 آگوست در ایتالیا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100659" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100658">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz38XR9vkjyr2KGsWjMJHMhjR7QA4NaNugY_VVSWP1sSH87wNonPWAMVLL4q2tQfZ_f6Vc4fhdV-G3SgUs6xbgQZpruZtBuMCoaOpFO4JQqmufVSNjG-d3h5jZpYJNVkFCOmdYwuS_g4hZpjnqJOYlVGpxYAB0wky6baxiGClE6Y9i03H4bZxJjqUk89YOohw_NaP5mrZi7XfKO7sP-j2AlVagE91u9GrKdLM00FAiRUVVmNKYbCymoPHyDDOjolPCMA0AEUCrwt9ebkJe-f1ttsWgCKKDGs1jphzuWUwHrKYkg5SU-D2uepOqQ_XwmOZfnqRRC8_m5--hnbQFYS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
؛ لکیپ: اولین پیشنهاد رئال‌مادرید برای جذب اولیسه رقم ۲۰۰ میلیون است که تا ۲۵۰ میلیون یورو نیز قابل افزایش خواهد بود و هفته‌آینده تقدیم باواریایی‌ها می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100658" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2KFWHUovQsGKTytz0yY9mAyeIrTLnmoP10wGVBiHdToLaY28kIyKCbEjep1F9gUVY0VMCBUnZGuhlz5pmVB8c9rLodv08vTT-IvuIRtnWL65vOKbX-aIoqNp02GEHaoJS2rNSXCi_qx4slJQD4VkuUoUFiBS1kWhmPxzxwo256e5N9vEaWVGdK1cD15WYKoktxkrq1BbH1bn6Wr11oRik1Agklmt9EHYMT_WWB6uzknL9kXyQyLc67Q5ocKMmYwst4dhrDp8FlTMnAcDAS0pNBPMsheqfA8tSf7Zj9UectooBxL4IO-12qqlhmFe6Oz14I4pwljlglpQc01aTsayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح برای عقد قرارداد با بشیکتاش ترکیه به توافق اولیه رسید. دستمزد ستاره مصری حدود ۱۰ میلیون دلار خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100657" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEP2tVekCUGDpt116UqOJQRjR0HAc4glW1hnI_fL86s2Mw9WorUsn_GTliPYkGJKV4Gmgv63kL4raj5dj-GcIdvIWNve4DN2rkMWavYVZFz0zgphQwzboeChOThFbLEHxZL6pdYBshc1zf67zBKs2uWJ-d_s0v9KxrHACQ1y0SDy5W-0L8xez2jmGU0T1JoZKWUoLPWaegccpM5mUkPNbnoGJkOW_UCZc8VA9CzHBUx3U_nwqcub8QvKZ8kowKd6PT4q4y5s54Ldrk8D9CmZifxfPb1SOSYSIB8X2hc-Sq89WqGX6gluvnpcfhdhFoECJ1J1zfvqIBwsD2xRazN-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
قرارداد ادرسون برزیلی با آتالانتا پس از عدم انتقالش به شياطين‌سرخ، تا سال ۲۰۳۱ تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100656" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1mW2AsOXEPJ53696ivlIcbxgaYyldOvdeEKwQ0fXdSalfus6fXKzIMTNf8pB8zrRvqyNbW7Rq9cUNgfRZruglqPv_NzBgIPrIRR7u3MhZD1fWn1DgD8SiUkGyFbGPjPLLPut9uoCY129GDThosXNNMOD4dSDEdGPdRAQ3v0ndqJbRFf4zHzvwFnYY-iQixJWVBICqJPKGpCgk2lzfRac0wn5Z_nQeEI-ZgLANkq2P0XwBo-Y1XzrW9WKXjDa-RfFPiHLw7D0P8z0MuVZtexhn-NOFhIJj0YLT52Jx6DLIhFKCT20FL4FS0rBWKwbfC7Tf_zTXDlWkZfYLMWNA9pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
طبق قرارداد زین‌الدین زیدان با فرانسه، این سرمربی در یورو ۲۰۲۸ و جام‌جهانی ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100655" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7DR4Wbw86Kq1poFZZOFqsrJp5ifpcWNhZPnhX6Qd1UDGY9SFhLZ249NuIGTF8JcHNmLJZ8DOuDYng6HC4_eYBdvC5t9Z1IGIJjhsc_xqINI5_oPSTT_ZoSU8NBJ51KqEgaNgM6g04zH6DV2AMPVHUH92UkL9bfchn66OQCjlg-95-rp2TZPxaK_ZuOi7duaJrXobYiE8kZwNvFH9pBWHRj3W-PUfEg16Ea_Sfz6vOLbIw4gRULWZiB65UQhiCQO1UKmwHRLD7IZ_d_lM09pbgPJvA0jDbqPSUIOQxcNyIRZ4uAUzytdpmO7mtVKjDXk60Qz0cW89ZoVyqCwSS6rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100654" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15sksOK_Aa-cSLwgRIXGFy6CzSz0kA5Za1IWT2ZTEGYlCkxqOx39dwWgjykrnTnye1nTurGWVoWC8dG_ehawfCOkxVQTJbb8DBCJrC7P1BnJbAUkNDjUN21Eh59k5Vni7TeQDc3Faju1cnEshJVRIybCz1FKEkhc0BB7cpI0XBMy8vQ17r5v0NoKkFcWHZqJI3xccZT39IrVwS9IMtXdQABDhkNHxj7Oh0DNqjhHKxb1roLoXaJM2CQT95HfNT6HzgYjBuZrcXOu8mS9c3kkeIBfvddK5uTtA_xOrwpdOyQba3W6nLh4bwhuXItQaHsxYympMOMIzvHozNl5rzKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک‌خوردن انگلیس فقط به این جام‌جهانی خلاصه نمیشه؛ تو چند سال اخیر انگلیسیای لوزر تا میتونستن کامبک خوردن
😐
🔺
2018: 1-0 مقابل کرواسی
🔺
2020: 1-0 مقابل ایتالیا
🔺
2024: 1-1 مقابل اسپانیا
🔺
2026: 1-0 مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100653" target="_blank">📅 20:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100652">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o01iWjMqcFYTWNX-b2xGYlmemMttL-a-IE9tKgvM97Dve5_aPZvchtID_pdUF6mxa4hpT4ZTk7jB7TIXMeb494tO1ccedkk3FyxzGkIp3C7e-aRzyU7Jjn6W2HcTorrM1jQxr7cLGlOkdDA3J5VyAOINKgtpCcpoP9m-Fwfn1jcU8s9jNKFe5aw2th6P5uxLSIGerZ7FJaUyqQliHmYVtB4eIPvMXrXCFoHg11qq6tCGqSRDK_bUPeMXxS2vs4JMG5jDry2QqLbiQ45kq-QY0RfLUy1rvMYF_xI3v36VsUT1R7E7yZsZTb7arWpIIe-KV7TPxAoUwxOEabn4pVXCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جیانی اینفانتینو در انتخابات سال ۲۰۲۷ فیفا آرا قاطعی داشته و به احتمال بسیار زیاد در سمت ریاست فیفا ابقا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100652" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fttlorP7P-Opy6iDB9BJghG22Kq1Irno1j8PYlRE_QpV86d03gfg0a9cCKIJDi06jtnUJnaUX8j0WflvYwwxPiX4qLCCZm1Y5tD6rkjrrvlBzasJxejpu2w5GjF7meCYp-vZst_xlQ2g5opsesFZGA3a299JMkGFVoF7UwexiUa5JriKP3fPFdTBnmoR2DXjC1v9S44trowBQOILt07boVQML4QSq-qD4kRRa6dEFd1iiblAqoFkvddg9MN8HhhpD8x6_Qj-vJft5BuncUDkvhScxdJDsyEE1ioYcxiIvrOiXBMJZL9AzXNJ-DKQaqfwP_tEJK698UXnRE_tG0-mVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLg3p-EQ4rqBF4tkWrxcd5lehL0RbNZKPzewTlK00r-mT-j9TK6YCJ--awV-V9XngwTz9iGEzO3FtbuYkckIYcZI255V4CuKIuUuBpypuJOkfTqS3KUTq00TcGl2RvMTSRETMdHcw9eQDe3SJkBwGbfxWQikcslqQkbfUeB7xRN6pb9P7Zh4OESrvmgB2AWwLQEvrPIwZbJ6LAEZ42Jb0mbY5ZvJ1IiLkGiCNG4HKqzojIVM6Vl-V-dcHOEUEDI2lLERQnLtHY4-7O1yhhW2yByEd5dGi3WCx-JyDI5TTQcx77HkV5vKEYehyd9qXfVodcaIx3mdqimEAavVEBOew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🏟
جام‌قهرمانی جهان در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100650" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYQPnh9gWP6EmoFSHryCJoWL1F-bVtEnchHB5jNy1siWGp7_LO_vyXKQbKlJ9jgWQPCXMC8uEgYLCTviYDeFcjdsypI53z2H1hBGqLhsiDseOnwgFSY84fLpgYNrEKND3JQTFz5fTfQqyuRVofbvPfzFpVUy9GVQUKNMeuQ6XU0Vri5Nm6_IyBGjTbqORoLDOVrjikw8hGBR8m5DJpIQe0_CtfSiODWvDXKl-awxpcITR704i8-M-5MQFEQF11jeLqF-yrf68xrJIOKWuoMsxC0zpGnkf4q4tu2j7frIVgR3nm9EM8s6gNsaknfMyF4TpmK1FY8j9CfAPqUlmZ4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یکی از جالب‌ترین اتفاقات در فوتبال:
- آخرین بازی که دیدیه دشان به عنوان بازیکن برای تیم ملی فرانسه انجام داد، مقابل تیم ملی انگلیس در ۲ سپتامبر ۲۰۰۰ بود، و آخرین بازی او به عنوان مربی نیز مقابل تیم ملی انگلیس خواهد بود، در ۱۸ جولای ۲۰۲۶. بعد از ۲۶ سال، این چرخه کامل می‌شود.
✅
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100649" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100648" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR_1Q9VZWjGZiPiyxn5hUz6qpfesOUfWd2v_z-xD-GPKzDoINkdniEjIE8xVpsOOJl-2ztrINN4OM99HzghMxgPrJ0xiE4buD3mFZwLeiZYVJHkA2JOITuv4tgeyKIpzCajieqprDUxgw4b9o1Qs7yXawcEXPGbw98fm6pNZIX35VBP7YjP706JkGMupFw-9l9VlLl8DtPiNiAWxyZRnFrHmUVL0dYkpvJ3oitcX-Q4ptW0hcnmITpiltrGJlN0Gfm6Knx0iUQeTEHcRD-35ZROnGzbGhyOG__IkkWCCS352ldswg_-xre_XqNfrjxWgzb8hxTFnEoumn_DEZynDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100647" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbOtOE4kTncDUXVt8lYwisL0egQCBU7pmgQ_KNAMBeV_Te8tjqSj2vekcb5LWP3DCedfLi8wrMp6kfqbW23L_T2E-c5OAKHxs4s2W0ivO5hc_CW1yGXKqpOsyK6_oszZ31CCYqMa73GAYPJhLxtkUC3AWBKnuJ81YP5U1h4qRtNXoCX0w_IuMf4iA0T_OQIl_oLv-A20GeNez90CDB7cjSzXWodOr5M9Yjk28Rk0i9v1rJMFY9uQpL3q_WSlEQEvqcszhYanf_FtQ8-kir6ZQzX-O4-swipdwf5u5i9QjZ9yQNP13ZRGACnRiVB5NT2h7FM3HWt0ht8o3PP_as5DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا رسما اعلام کرد نمایش بین دو نیمه فینال جام جهانی 17 دقیقه طول میکشه و نه 30 دقیقه! خود نمایش 11 دقیقه است و باقی زمان هم صرف جابجا کردن وسایل میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100646" target="_blank">📅 19:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بهترین جایگاه برای تماشای شادی هواداران آرژانتین پس از صعود به فینال جام جهانی فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100645" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoJXjKx1IvAwWDvn7BVe1P6yliIuDdVxu_0ASfWsqQoqC_mhN5VkNZBFGLZapO8THvVTS9AkjJz7O0AR6Bw3cRk7az32jIZMl7UhxBKnXcNBl1KCSfsORivLJFyZeOHNTeDgw6ci26zvro2YlRRMC47VGFZZ2lHSbMY6TZUCGlmr-clMzwzSUCL59IqeDzo1hmzsVGXB2s_seLaBCjGat1wyfHlmNjJTHx3NOOca4-Vqb60l04Wlg9e_HR9RumqvxJLDaWXkeCWxim-TWtY02GEEkesljMTwxj8JV1163U6x3fBuE6b9gRQzQOWuZetLxRQQNwMOaHYKguqE2wIkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آرسنال به دنبال جذب مورگان راجرز،  پیش‌بینی می‌شود ارزش انتقال راجرز به آرسنال حدود 100 میلیون یورو باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100644" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
در سال 2020 جناب وینچیچ داور فینال جام‌جهانی توسط پلیس بوسنی و هرزگوین به اتهام قاچاق سلاح و مواد مخدر بازداشت میشه و پس از تحقیقات گسترده و یکسال ممنوع‌الکاری مشخص شد که این داور بی‌گناه بوده و تبرئه میشه. حالا پس از  ۶ سال این داور با انتخاب فیفا قراره مهمترین بازی عمرش رو سوت بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100643" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100641">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4imvLFp-76BEb_M42Tm464rbb83DrD411nhXAgZqnED7mcGGqeuJLbwiksHsgZoBXBfDjfSybbuXmwrx2eXwoYMaOkvJ3ABdHlPqVyKoFp1KfN1hT3ZUeK6BrbvcMtjZLzf4yU9ecHvUqdjbL_gtCzPLucKCGxSjYveCGaRlq-TufM6EDrccpSfFcgQxH8JSXfPGtFUR30-WP0xHwbmfsBlo3e9mTTB6P6qDsHUdw-v8FMbvK0Slv_doNF97d_jnbw6RS3Hn5JifXyORt__mk-QV0uM3jLoT5GkNwlvq_BmOZawuNcrCEAd7Ct087Lc-Z-YEyr-PPGy4mj7aElrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b318kRO3RipP-GB4kBG6NDxCvKLu-bCCDFNPCKa9sFRctME5XGDjS9wrFG6GVRIt-A0oHNH3XF6xGxp1brKBXHHTwiFiPF00cme81Gs71OA3Ygkn3a88jK3io84smdeLX7axhP9F0MFWM8Q-ViK1DlZnyt9zwNTIaonQ8Uzs1xuF5Ufm-FpNk7fAhbPZ0EoUM1yDsy1AEcV4JZeeJ19xvjE9yZI3Zw86TQ2fj7ith3UD-tcEMxA04T5GZ9I0rM0ol-QJlZ5mieLz43IhdThjVEgwYLf_-VKvqjwyFhF5vYQQURoTbTSTSBSyjoC0K0nW_4ch3B3kFQ3b8weKaebeYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ووزینیا: من معتقدم که در آینده لامینه یامال، مسیِ نسل بعدی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100641" target="_blank">📅 19:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100640">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzYRtwNmBBagbRa99vst8bkoajwYIJDO0_9KTFXarDlNGtwM4xLMsNUMDV4FHJjA7Qd6lMCtNhRgMO42pEWmxF00kWKTGMW--z6CEsKebk9dzcUOEU_iLNzLa6xhi_F7MyrYjHg4SbaERxbFMe7qz72EOd1ca9MP-ORrZ3nO0gGchTyKb2_eWlI_OMU6T5EaYmsmjpI_CFs8h--8u3bLEZZhq58fyIVtYfus3fvkmAMKvCHsAtxi_hxd7EkjKNzyJ0t85OaynqmskZxY-Vnm56LM-7MZvHM4R7aSc3soYh2D103_GDuRoNGzQ0y_hZYWBIpQKz22CB_BIXWmwU3Whw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌‌های‌ملی اسپانیا و آرژانتین در فینال جام‌جهانی با لباس اصلی خود بازی خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100640" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v949Uf2s4rdMSwzX1_NpC9vVbBvbBa6oKpLttD_2S6qOa6UfA8wMw55y0L0yqcF6HXNwQ2uG22n9aNqjW3i_hz0BWncECZ_152q_8O-zZJzktuz04bausx7g-hzfdq-HWTzdFDV9P9HIN58LhD0zN_tV5hg7jFuGKmJTa8KHDEc5LbG-PCklmay0ZkJ04FO-MZHhxgwtGBqrGiYAYtioz7_J370HWzUUauw2hVPD_N21D44sKal_0v6-4FAcQGqtLWPIKhBEt6JGo0a-IKORhoRG-c9Qe0otPdshwiAs3zZrOyCU-kZMrBTZayxYsbOeoIQwFHsScI8YPVQonVeNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل Marc Cucurella رو سرچ کنید یه گربه با مدل موهای کوکوریا تو صفحه ظاهر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100639" target="_blank">📅 18:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1ERBAeoTODbj7S4a4OlRSiVNhyYzNSaCZy3LemKTKQkOkamfgK0s1XviJbVQWHmiqrfyhIKMfDsZORUAYEmXVznK-cLUFLSuIF4ExlAl2cxrHx305NjGIM_vTm2vWTlkXTNiTQYf77150oyvc71VDQhCon0bBBZdbL8kBB_7wpaA3XbcNAsM7X05pDLciCTEYMTvG54WTnKOSA6s89vc32i0iX41NfNnldsY9C-tUgrvccBouPBdZJoOyUzRwWvABQVHJgQh8oQ-HQ6h8UPq0usV746CeJnLFIjiSA1ezf1ofAWUq-DYqUGf8uS2V8ohifjAmmSQSb5KfROBF78UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
• خبرگزاری فرانسه
🤩
:
🇪🇸
نخست‌وزیر اسپانیا، پدرو سانچز، که در جنگ اخیر بدلیل مواضع مخالف ترامپ اختلافاتی جدی با رئیس‌جمهور آمریکا، دونالد ترامپ دارد، در فینال جام جهانی 2026 بین اسپانیا و آرژانتین شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100638" target="_blank">📅 18:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
❌
ورزشگاه آتالانتا هم به خاطرات پیوست و زمین چمن این استادیوم برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100637" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
🇪🇸
تیزر دیدنی از بازی آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100636" target="_blank">📅 18:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=KW_gMhwteK_gJOBT2kKZEwgtWBjPzlPvo6LHMWOpOl0lem7rwl7v6IOVMDefIx3Y8VJOX25WYMJQ1mGWVTYyu5SSL-NeuGSpsm7UzaKeilCBBbMo9G3PW4hOUoyqMADW9TJKd9DeA6rqhSHsAILDmf7p5RJOZ_RUnPDFZTrEH2efr6T408lOoHOnA1kNfw6-Cj-LwW67PZr5wyjHh6rDwg2S8KKwcc8yzsJ609wcTDQ00B4dfArhq3QZrMqoNJNZmbumWHRtfb9Iotike7dXQJFNcgRV7cfIvXwsMraydVy5f1UaYvxDUoyiYOGgv0ByeYdeuDOQBPVopmkQ8yyReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=KW_gMhwteK_gJOBT2kKZEwgtWBjPzlPvo6LHMWOpOl0lem7rwl7v6IOVMDefIx3Y8VJOX25WYMJQ1mGWVTYyu5SSL-NeuGSpsm7UzaKeilCBBbMo9G3PW4hOUoyqMADW9TJKd9DeA6rqhSHsAILDmf7p5RJOZ_RUnPDFZTrEH2efr6T408lOoHOnA1kNfw6-Cj-LwW67PZr5wyjHh6rDwg2S8KKwcc8yzsJ609wcTDQ00B4dfArhq3QZrMqoNJNZmbumWHRtfb9Iotike7dXQJFNcgRV7cfIvXwsMraydVy5f1UaYvxDUoyiYOGgv0ByeYdeuDOQBPVopmkQ8yyReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند پیروز قربانی خطاب به علیرضا جهانبخش: من چندین سال داخل باشگاه بزرگ استقلال بودم و نیازی به دیده شدن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100635" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=btpn3FV_pci5zjT3sQkCDhkuxOfYi2i7205C9DuR5MSkKiRusFdRJTME5QAQ1H8DNDATNo_dsw-q-g24NZj2Pd-8qjeRrLNVlsqPEOw4d6f8k_IJ8pBBZVUTHiYQwdYBPJCPgTrJdxdigSeGI0uUJyEtZ-PnoAzCUfoBp9mrsIJs3zFZ5V8oIgTVhc9qZ0TadUddbSk_r38NpUbKhprqs3qj7i6wf76CFhrL08-wF-kIfsZciRasyZ83_BfhULWm0HlbkPGr2-0dTT9_jZieEFm0AMHVXtVYxowpEIhSv6yvnIt_QCLLUcDXOwuJij63tVhMrB3MM6DdX6N7vuk4og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=btpn3FV_pci5zjT3sQkCDhkuxOfYi2i7205C9DuR5MSkKiRusFdRJTME5QAQ1H8DNDATNo_dsw-q-g24NZj2Pd-8qjeRrLNVlsqPEOw4d6f8k_IJ8pBBZVUTHiYQwdYBPJCPgTrJdxdigSeGI0uUJyEtZ-PnoAzCUfoBp9mrsIJs3zFZ5V8oIgTVhc9qZ0TadUddbSk_r38NpUbKhprqs3qj7i6wf76CFhrL08-wF-kIfsZciRasyZ83_BfhULWm0HlbkPGr2-0dTT9_jZieEFm0AMHVXtVYxowpEIhSv6yvnIt_QCLLUcDXOwuJij63tVhMrB3MM6DdX6N7vuk4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=ts2vDbmP6pKUibh-t26yyMvVrPlkaHCQo5PlFSG5GIKX8kHgqqcl6tusOf63vZqS1YB8oz4l0SSPiQOVfcCkeCxcp8btttVj3LTpRhpPEnG1YkC4DOxxcNOhuOW3B8y09kx3xlXkUrjQnCPOCS6pr6dOvB2OxP-wAAYnYTCghM3zdNdcCkjlZOsKo__-kD0IPB7OJByIh5B84ptkCP9dEb6C0MjSizoUdFnJa_gcb101gNDt6XJ-cT3wGSo9OhodA7UFsFy98x1WOLzl_ijkErcDR07vSssHUWGrEsriwwuNxKJ1pSfPN5Faw_3xwF7JV1PcCtWkt49iNnBCyoh55A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=ts2vDbmP6pKUibh-t26yyMvVrPlkaHCQo5PlFSG5GIKX8kHgqqcl6tusOf63vZqS1YB8oz4l0SSPiQOVfcCkeCxcp8btttVj3LTpRhpPEnG1YkC4DOxxcNOhuOW3B8y09kx3xlXkUrjQnCPOCS6pr6dOvB2OxP-wAAYnYTCghM3zdNdcCkjlZOsKo__-kD0IPB7OJByIh5B84ptkCP9dEb6C0MjSizoUdFnJa_gcb101gNDt6XJ-cT3wGSo9OhodA7UFsFy98x1WOLzl_ijkErcDR07vSssHUWGrEsriwwuNxKJ1pSfPN5Faw_3xwF7JV1PcCtWkt49iNnBCyoh55A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=uF7Faewtvx02JguGcM3VVDy_wYO7QhdAewo2knU6m1vlv_kTFZWarGzdy-jP9MI_Gh6mMzar52uorqvtNdlNQsQ2qAiP38PkF1m0DeCzdlxGcomDmheR6medm5cinCq2wlfUxQpMEYdMNuxdIAHb38i3YoaLB0wMqcprQ96wQFuel-rsZw9ipZ3w4P4_ECB0Y9YaIhF5aFO011GMLphnvQ1o8BULXrD0gOS9qPraxhkxeYmDCE4dwZ30bsGc13djW-DWLipRJ6XiI4uMEn1rhPiT23XimS6LWF9CIn09R10ayYvcUvVNfHGjuUq12b53tXuV9Hca0YbNMGPFu8paIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=uF7Faewtvx02JguGcM3VVDy_wYO7QhdAewo2knU6m1vlv_kTFZWarGzdy-jP9MI_Gh6mMzar52uorqvtNdlNQsQ2qAiP38PkF1m0DeCzdlxGcomDmheR6medm5cinCq2wlfUxQpMEYdMNuxdIAHb38i3YoaLB0wMqcprQ96wQFuel-rsZw9ipZ3w4P4_ECB0Y9YaIhF5aFO011GMLphnvQ1o8BULXrD0gOS9qPraxhkxeYmDCE4dwZ30bsGc13djW-DWLipRJ6XiI4uMEn1rhPiT23XimS6LWF9CIn09R10ayYvcUvVNfHGjuUq12b53tXuV9Hca0YbNMGPFu8paIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=QhTuom8MbZCIbokB3Zunu0eKS2blz0FygOtU96PSn9lyluMfd5SUlS38ugqnz-MGbI9zIsCQ1Hshhoh1Yydm2SmBzcKZw-MrPC6dy4qD1EmFnFOvHohkORI4fx9LjFPnVSzqAyKEAwQ0XPsroh87aYNmz8feGN6hc5NQc-Lchmwosr1nd8kBECc7-IfVk79a4Snb2TtUxsSEsyWykAHPD72uRz5b9uNxnqSiEWPWq-0eApls-oTAMZHD9Up_06TExaX2P91M3bGNqhK2DUOnuWfms8Wn9efzJdJlMu58tkVfqS8sNspv25gQa0lTLyHBHkbLxBOWHeTvWwaMxHORLxQwWFdBr2A3JHtqXZ6ITK3ykmkprHxP5AW1PxmoT9vMdZLQ9I6JOv4qZfn8lTICO1zJF7Uc7w7Y8WC3XoPtryDJqZlrSExUecTBBeE0-16jnRkqwtTwq2Nov1ZdBoDWkqLx5mo_ObeTTjqeDdQffLAW1vRFZRBMcUiBnwhkKHEUybOomFE9p-dzc_MZED9dhn2qbp0BFgPaD28qfxN-sP3HUinHuIOdzJ5I0tOhMUCo918NtUECV9X98ayhDiuI2tQxDaZrZrs2eKjo3iZ-au3pBFL-SnFerPxYbj3S73dlX-pvs_aM8Ms49lwySN0kDGz9wCeu-XbPoF8NeBc9dBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=QhTuom8MbZCIbokB3Zunu0eKS2blz0FygOtU96PSn9lyluMfd5SUlS38ugqnz-MGbI9zIsCQ1Hshhoh1Yydm2SmBzcKZw-MrPC6dy4qD1EmFnFOvHohkORI4fx9LjFPnVSzqAyKEAwQ0XPsroh87aYNmz8feGN6hc5NQc-Lchmwosr1nd8kBECc7-IfVk79a4Snb2TtUxsSEsyWykAHPD72uRz5b9uNxnqSiEWPWq-0eApls-oTAMZHD9Up_06TExaX2P91M3bGNqhK2DUOnuWfms8Wn9efzJdJlMu58tkVfqS8sNspv25gQa0lTLyHBHkbLxBOWHeTvWwaMxHORLxQwWFdBr2A3JHtqXZ6ITK3ykmkprHxP5AW1PxmoT9vMdZLQ9I6JOv4qZfn8lTICO1zJF7Uc7w7Y8WC3XoPtryDJqZlrSExUecTBBeE0-16jnRkqwtTwq2Nov1ZdBoDWkqLx5mo_ObeTTjqeDdQffLAW1vRFZRBMcUiBnwhkKHEUybOomFE9p-dzc_MZED9dhn2qbp0BFgPaD28qfxN-sP3HUinHuIOdzJ5I0tOhMUCo918NtUECV9X98ayhDiuI2tQxDaZrZrs2eKjo3iZ-au3pBFL-SnFerPxYbj3S73dlX-pvs_aM8Ms49lwySN0kDGz9wCeu-XbPoF8NeBc9dBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=F1hxJCCwtalH4iZ_iLXP-fB4z0jjvaPJMpEAbcFmOza6r6sdn3Q9-uFCgrSGBy6xXnhm2Srn6DZSw7jvoxn8d1-kg4FiyCR3EaoNrsXhFkkP4nDmrCTnpO1CeLSBCkGBhRCeM1o5kvOoHTXySU9NtcDs7aMZ05v3Dt-Lc_CM_BmF8xQRSeVVcRUm5QvHKCjEc7LLCPmfV-kCD5iL3YBt1Zi4Zw_sErhkQDcGsAO4_Gfl4ihI70Q-w5AFbjTyUh-_HYrxXBGPpiRQ0evm63xTCn4GKJ4tleApA-gAUua03YyOb6mLSfIzQF4rB0u4nx1206YNwZ6w-8grasellWLVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=F1hxJCCwtalH4iZ_iLXP-fB4z0jjvaPJMpEAbcFmOza6r6sdn3Q9-uFCgrSGBy6xXnhm2Srn6DZSw7jvoxn8d1-kg4FiyCR3EaoNrsXhFkkP4nDmrCTnpO1CeLSBCkGBhRCeM1o5kvOoHTXySU9NtcDs7aMZ05v3Dt-Lc_CM_BmF8xQRSeVVcRUm5QvHKCjEc7LLCPmfV-kCD5iL3YBt1Zi4Zw_sErhkQDcGsAO4_Gfl4ihI70Q-w5AFbjTyUh-_HYrxXBGPpiRQ0evm63xTCn4GKJ4tleApA-gAUua03YyOb6mLSfIzQF4rB0u4nx1206YNwZ6w-8grasellWLVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUueBuZ1eHj5vKO75Q2PUyzmyTIbGCZoDIYHWQoyA7WyiBxWadJIi8BDNw1UkkWe9nI5kBA5vQDeIdPPWViGvOyFNiHCOZOh296kCC7f0oH0LsvPnV1UXWZ7W8o56tfyGf0we_eItdG69W28OiPEA_RnJIgDOWcWs9Hb_hmA3RKBuaJu4qLTzkZiWYT0XNFmLzqgRegjCQrXLhRLKJ2aP2hiQE5zzZZK4GaXJkQfiafI-7VgY4L86tYAq86f27Rp2pfIPQhBBLri50h7yGiW0MQUfDPlAAS1wil-tHpDxrpihNBsywZl62e3AXjIh0v6J0wUug2nr0koZrgSPBtHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF580fGrkRq85iBYqAVRYbq8sWpi03vKkbneh5PJSeA2Xb26jIqXbd6nEPceM8LRO1CaM9QzIjPTqLXlN6bU1MdOiNQtNa7gD_ega0MM36nnvC-s3ZhDPYmIcyPZiFKE2H-7MaJSTpDtKa5vsuutRqBQkRLMfGlqKI1P6tfaZiAISNP0N2EyXSQFZcChOfvz5kCu_a6MaDtCGs6GS0IT5R0RkCorobhcxXF1791m8YHaR9s4kUKXB5GTJWXHpw-w1WsaCsa40wN2vjWDIfXBk_0xFfohzN2460z8tBg2ut4T-9aX3PkuV3nvkOHk3BJJc8iWFeZlBdTvFjUETeS7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=Ge3xmksm1M2i7v7yWrUv2Yz-smyeuc4khNw_kw8O5uoT2zp21yjljOINT9Dv1Fv9faFsDNk9ejW-Oy3cyEVpOCuzKl1grNepoCsnhXtRENYmJW_A28KU8aEecb07KK49eTc4nd1e4BQ-Nw25-g5FwMmvmNZa5yNDbFT87zke6bu-6_rhHQpQM-Elnbxouy8hcmO1sN9cZquh6BfZg_J-Sh21N71MO-1HrnAf3CMxR142FPn7k8PzXqtu66gPvBqCELRKCq7Y2Y8WbrPYDxLrkWU8dpI6fYl_5Mg2ToVXcW6wpExn41FnE3zE6W60KdKXF6Ep5mrQoz-f3VV37NA9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=Ge3xmksm1M2i7v7yWrUv2Yz-smyeuc4khNw_kw8O5uoT2zp21yjljOINT9Dv1Fv9faFsDNk9ejW-Oy3cyEVpOCuzKl1grNepoCsnhXtRENYmJW_A28KU8aEecb07KK49eTc4nd1e4BQ-Nw25-g5FwMmvmNZa5yNDbFT87zke6bu-6_rhHQpQM-Elnbxouy8hcmO1sN9cZquh6BfZg_J-Sh21N71MO-1HrnAf3CMxR142FPn7k8PzXqtu66gPvBqCELRKCq7Y2Y8WbrPYDxLrkWU8dpI6fYl_5Mg2ToVXcW6wpExn41FnE3zE6W60KdKXF6Ep5mrQoz-f3VV37NA9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=PB6PEqkfxxIxaUOB_GDVT4QJYYVM_kkYYH639use85FKOaj9uW9UOnLr7wUeyz_a9rHBB8AcCZCvL8ybRZUVsELjV7UTmGxgDXgU5FfqHZn2Yngz9MezaSWSoJ3uO1kxDjEziXo_M6jVozL0ARNIyxWPpAaOrE6h-I92OV5vzxGN83n_JaXIqs13gqVsVf-GUcq97enypJunJ2A7UozGwnWFpZaCu4WL6a1MYtd4mTxu8UK-34zg2DnmFtgVsMdWxGBo7RoEiqfm2NsPe4z1hhV6zIzJBrmPfH2S-n-hhGE_N4Jcjnm52lyMrltSkGX-rGl9uxOlB1AsaeUPiASKhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=PB6PEqkfxxIxaUOB_GDVT4QJYYVM_kkYYH639use85FKOaj9uW9UOnLr7wUeyz_a9rHBB8AcCZCvL8ybRZUVsELjV7UTmGxgDXgU5FfqHZn2Yngz9MezaSWSoJ3uO1kxDjEziXo_M6jVozL0ARNIyxWPpAaOrE6h-I92OV5vzxGN83n_JaXIqs13gqVsVf-GUcq97enypJunJ2A7UozGwnWFpZaCu4WL6a1MYtd4mTxu8UK-34zg2DnmFtgVsMdWxGBo7RoEiqfm2NsPe4z1hhV6zIzJBrmPfH2S-n-hhGE_N4Jcjnm52lyMrltSkGX-rGl9uxOlB1AsaeUPiASKhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=o3sfK8XHKHafANdXj_nPpvKKjmJeagedipA18zphxVXq6Jp3J1KK82URHYGaaKve1mjE9c2Q7VYx92Hyg-MQZiaCFgtyKGF55JvfjOMtIRdYLw3DZD-m3HsDO9wQe7gObIVcaZSVYWHlZ5z32cB7yXXR7CXLs2VJAiKatWd5copWKi4ym5OHCNqqNnkHWHtpiITsBVIF7CTX0-RXb8ZGi72ZrfX_WJx0vGku1CHfGiSPO3lOF7S1nKBmyDhCmMpC03ycP1k1EPAJn_n1IEp8hQo8QIDjkiXB2Ssxa93WTcdJIuuRdoiahCHI227mOb7CxHMruD5ing8Gt0pDVdq--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=o3sfK8XHKHafANdXj_nPpvKKjmJeagedipA18zphxVXq6Jp3J1KK82URHYGaaKve1mjE9c2Q7VYx92Hyg-MQZiaCFgtyKGF55JvfjOMtIRdYLw3DZD-m3HsDO9wQe7gObIVcaZSVYWHlZ5z32cB7yXXR7CXLs2VJAiKatWd5copWKi4ym5OHCNqqNnkHWHtpiITsBVIF7CTX0-RXb8ZGi72ZrfX_WJx0vGku1CHfGiSPO3lOF7S1nKBmyDhCmMpC03ycP1k1EPAJn_n1IEp8hQo8QIDjkiXB2Ssxa93WTcdJIuuRdoiahCHI227mOb7CxHMruD5ing8Gt0pDVdq--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=PmS4uhgbFqi7mG1gdOeOwoNANDc22L3667pk6METj23lsGhzriNgYkaxdQ_c4RFwm5YnZVz4HZEodXBf2iSI52CnLwjHlOQ3E-AUo_bNFupygyo49VS9laDKjl71MREsBxRZeX-cPxWzRvigyNg_IcJDuGNyzIFTrQ7ZVIBfgJnH8CnoXcMhUYflpUXpGCi8P8fcQD5zfInfy1mMZh6M-FCnpIB8YBoJB_VgUSJ71gcO3Cvk9ehQjhOuFgLS1-xQeuTncBrWABDmm2dq1gZp2tPOzWb7qVQI3geXLSfluYUYJXj9GauKiblth-1TkYK9Am_9xzRKDXGpH0g__RWZcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=PmS4uhgbFqi7mG1gdOeOwoNANDc22L3667pk6METj23lsGhzriNgYkaxdQ_c4RFwm5YnZVz4HZEodXBf2iSI52CnLwjHlOQ3E-AUo_bNFupygyo49VS9laDKjl71MREsBxRZeX-cPxWzRvigyNg_IcJDuGNyzIFTrQ7ZVIBfgJnH8CnoXcMhUYflpUXpGCi8P8fcQD5zfInfy1mMZh6M-FCnpIB8YBoJB_VgUSJ71gcO3Cvk9ehQjhOuFgLS1-xQeuTncBrWABDmm2dq1gZp2tPOzWb7qVQI3geXLSfluYUYJXj9GauKiblth-1TkYK9Am_9xzRKDXGpH0g__RWZcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=PRaAsx-bxI0TsL9drZBNXH5qtSfDMpGsGexbKSD_2U0HWHx2ljuOum7bKBWq4rxHy89WX0chY2LjTH8aZBpBbrGFMzpehXZM3-v_0kgMi7eM0dgFRR6j1UM_2L3cTujXGBuiq_oefNRIgh-TXqEDo8timIUzvYiaU81gtib1E4xUDRpZKNAXwr_l3bOwkmtk3wOcPuEx4PYlhF3vc99wn7uDifvpsNFb2Ujp54q9E3l1S7UazQ0K_6RJdR49saKT7VOfWrPYvWKBEGLxJ-6F-GjArj6HzleYGXmOADZ2I78NREZnlmrTGRpLP91zU2Cy5ODg_nGR188x8aJ74W4V4qeVEXl-GJYGzwUex_l5MomFeIA09FwNX45hBtbM4Z32cmeab67phxruqxMurWl_wzwfv7-QO4sLkmgfK_4oWY4Bx5I1z_26p9x3TbNg4LNltahkJtmQfMM4GPZiX18Dak1pk3wh6d9ItGw763w2lD_WbSFbQ_qTxy-v42L27ePv-VGJVz3wadAtodDC-XHrXdghg2m-goPxXzymX_AaacO0VeclZAuXJbhMkl1jDgM_CwTkTz21zHAX-cftGJeo32MarmFokOHWGAWVCjxfQSAdyN6eT8z4uhwgL1b6xPF4yt_Iy1tuRM6nuE2ZgvwmbJZKNQeaUAOxKMHbFiE4ak8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=PRaAsx-bxI0TsL9drZBNXH5qtSfDMpGsGexbKSD_2U0HWHx2ljuOum7bKBWq4rxHy89WX0chY2LjTH8aZBpBbrGFMzpehXZM3-v_0kgMi7eM0dgFRR6j1UM_2L3cTujXGBuiq_oefNRIgh-TXqEDo8timIUzvYiaU81gtib1E4xUDRpZKNAXwr_l3bOwkmtk3wOcPuEx4PYlhF3vc99wn7uDifvpsNFb2Ujp54q9E3l1S7UazQ0K_6RJdR49saKT7VOfWrPYvWKBEGLxJ-6F-GjArj6HzleYGXmOADZ2I78NREZnlmrTGRpLP91zU2Cy5ODg_nGR188x8aJ74W4V4qeVEXl-GJYGzwUex_l5MomFeIA09FwNX45hBtbM4Z32cmeab67phxruqxMurWl_wzwfv7-QO4sLkmgfK_4oWY4Bx5I1z_26p9x3TbNg4LNltahkJtmQfMM4GPZiX18Dak1pk3wh6d9ItGw763w2lD_WbSFbQ_qTxy-v42L27ePv-VGJVz3wadAtodDC-XHrXdghg2m-goPxXzymX_AaacO0VeclZAuXJbhMkl1jDgM_CwTkTz21zHAX-cftGJeo32MarmFokOHWGAWVCjxfQSAdyN6eT8z4uhwgL1b6xPF4yt_Iy1tuRM6nuE2ZgvwmbJZKNQeaUAOxKMHbFiE4ak8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=fU8lguLhdR0hTcKSxp5kPboEwEjKp6MILwjCtTEMArck3h2TpI56CvKIGT6Qwqc8J36c3dBwBXLuRGeEmhzT85i7n3x1UXs8NU9p0Rf6Koj4KKBxqH1u6DE-l8X2z8oy_4mJUb5z8wEgX1z--mYTlO_1XbpkvQn_sCB_fQV7FbjIOxcSojH05-8EnyPLySldFn4jGMiwAdl4UavL52nWREKuY4SDcQhh9uqT0NCxKp60EuAkPq0pfEI8FXA5l53lPOAKMyNi9BaYRg8Rfh-F_zrnNRFxS-MsrJxecGPe89J7cPPnQMJzfiGfKyLoGueyR8O0GMEkEpHebMNw4nXF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=fU8lguLhdR0hTcKSxp5kPboEwEjKp6MILwjCtTEMArck3h2TpI56CvKIGT6Qwqc8J36c3dBwBXLuRGeEmhzT85i7n3x1UXs8NU9p0Rf6Koj4KKBxqH1u6DE-l8X2z8oy_4mJUb5z8wEgX1z--mYTlO_1XbpkvQn_sCB_fQV7FbjIOxcSojH05-8EnyPLySldFn4jGMiwAdl4UavL52nWREKuY4SDcQhh9uqT0NCxKp60EuAkPq0pfEI8FXA5l53lPOAKMyNi9BaYRg8Rfh-F_zrnNRFxS-MsrJxecGPe89J7cPPnQMJzfiGfKyLoGueyR8O0GMEkEpHebMNw4nXF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8ra-oNvE-wbimI7B3GspidOneOdsN1seXZnNDDCECUG9fbQeV4FO2k96GFYxBErS_6gA9bFCAzSBNgWJhsFfCYs9_9iY3Loc08NqUNzwAa-RHMs7uMJwI15vqTHl0qhWKChfl7C_SYah6sKGhPPjt_2Mm5lRuSIEZq0FHJXyyWQB5wBuJq6NboXDXgRexEMcanyuPHCvJOVHUelmS7-rkqpF1LMallJ3Wy_45t4uD0CNeYBwv0bz6mpLgTqUNJ9XPqQ7vBZ_I_S43kfMTgZ5KOwQXxkydaSthckPiafDV-B4p7yMop3HwH0pLq4DfQZ8N9lUwe5fl2shbwKSA5jsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=Wf3rTinVfcVJsPzvDK4EXMoeiPHYI5mIX78lUFA4ZE_Sibo-QsugsUT3USu0XSS2DTi-jCSAWL_A-3i95T9Lx1gXfRX7yiLjaIKorK4dCRJBNF4VmnWkjtyI1GjKeRjRSbtc-QjvedRcUDsLxjEgUw29Rxb5Cxcadg7yLXDWkt3xAzkRzomXjKFYDWKp1WTPr9dZASwCf0yP4n_GkTzepzFmaExpdMSn34uG9RF01wiPam1l9dILkpzIHGJsvkc9o7MwGUbpW5MEJgPnNojfRaPwuZPX-iXkzhZG7DWlLB1eHeg2jW4u8iMDo3VKmWBOa7ehvRuCmKknXdqxkOs9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=Wf3rTinVfcVJsPzvDK4EXMoeiPHYI5mIX78lUFA4ZE_Sibo-QsugsUT3USu0XSS2DTi-jCSAWL_A-3i95T9Lx1gXfRX7yiLjaIKorK4dCRJBNF4VmnWkjtyI1GjKeRjRSbtc-QjvedRcUDsLxjEgUw29Rxb5Cxcadg7yLXDWkt3xAzkRzomXjKFYDWKp1WTPr9dZASwCf0yP4n_GkTzepzFmaExpdMSn34uG9RF01wiPam1l9dILkpzIHGJsvkc9o7MwGUbpW5MEJgPnNojfRaPwuZPX-iXkzhZG7DWlLB1eHeg2jW4u8iMDo3VKmWBOa7ehvRuCmKknXdqxkOs9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=NjB6iT0V94sDdnywXnupK-BYWXDEgksGDh5YurM-wa4U2zHo6SUKWKCSEjBjjNgP4VyovZVkq0B73cwFYE6miIjay53fOCl064y8HOfMjoqYcUb5pSx2ivHAGLjC3ax7R52YS0Yp2trMqLYIJhQH8jw7OqLpC4F6IP6a5vcOs70KFyUVOdfrL3uE27bYIXtA5hF1Av4owWFuNArIfHaH5XWrz7SmlolNK4six4Q1kzanVdlouSZY8RtY49CSzGoG4CMUkYv--mMrKgou3fCiMN8PSHwCgOiSNmFHNyTMiuE3iPIBK0BD5c_M0uwNqf_UnF2WA9ORHdahBkM0kYFHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=NjB6iT0V94sDdnywXnupK-BYWXDEgksGDh5YurM-wa4U2zHo6SUKWKCSEjBjjNgP4VyovZVkq0B73cwFYE6miIjay53fOCl064y8HOfMjoqYcUb5pSx2ivHAGLjC3ax7R52YS0Yp2trMqLYIJhQH8jw7OqLpC4F6IP6a5vcOs70KFyUVOdfrL3uE27bYIXtA5hF1Av4owWFuNArIfHaH5XWrz7SmlolNK4six4Q1kzanVdlouSZY8RtY49CSzGoG4CMUkYv--mMrKgou3fCiMN8PSHwCgOiSNmFHNyTMiuE3iPIBK0BD5c_M0uwNqf_UnF2WA9ORHdahBkM0kYFHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=hDoO_0SN3ZJDR4R6tlaVvj1O0GgJTrU5QxVzc9YLEsA-oPabKqeLnS3w8OY4BfKHBuRQFFqf5VpSSE3SOZeEEyPMJ2B8gY2noMad4fwu-jIhGWlgxTr6gfN-K59msNuzgXCRdkbbLhUnCKI99NmS-SDDP87Bj4HuOMnpQRnNF-OIf7T92ngUfDHyioOwn49cS7_DRsm1eaPA1rFE4xUkrFm8eBp0F1RvItM0iN4pFBkcOBf9SeDtjEQDFlCqVrlGswd1mEe6sr3rsJJFpj6Y4pWMopbD4Emdmf9mVxHp-rrCNjHKLqMIUvzuabz2HaWjUKmM4rbQaOTpB5z1rNzihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=hDoO_0SN3ZJDR4R6tlaVvj1O0GgJTrU5QxVzc9YLEsA-oPabKqeLnS3w8OY4BfKHBuRQFFqf5VpSSE3SOZeEEyPMJ2B8gY2noMad4fwu-jIhGWlgxTr6gfN-K59msNuzgXCRdkbbLhUnCKI99NmS-SDDP87Bj4HuOMnpQRnNF-OIf7T92ngUfDHyioOwn49cS7_DRsm1eaPA1rFE4xUkrFm8eBp0F1RvItM0iN4pFBkcOBf9SeDtjEQDFlCqVrlGswd1mEe6sr3rsJJFpj6Y4pWMopbD4Emdmf9mVxHp-rrCNjHKLqMIUvzuabz2HaWjUKmM4rbQaOTpB5z1rNzihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=hUFXmNez0Rs7QBHGoOoytRao2y7voynelaZvhSErowYexa5h6-sjPbpp4Qvhzipsa3xuHmRGlrPvQl7IflGlVXawjakcol3afr2CI0kNrZxjkdd2thwbvEZEFzobsX3E7rjn0RCaX0f8uAddZcFrZxZVD87bFh2RSbRy_fM8tfE3obLsNI_NdkPy1zYDvkmYVAWkRjSuUb1pU_eVDh0vtxwFuukrc2kzIz6DmMBxkC3inl8N9-j01TpqNwnf6S2zNaXZY8LRP19FPSZrTroklbkS8ZMe5sSJ_T7erXsJKrcQF-8xFwnl7BKiu0c2Awm3QArx5u5xP-jQ31qupm_voQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=hUFXmNez0Rs7QBHGoOoytRao2y7voynelaZvhSErowYexa5h6-sjPbpp4Qvhzipsa3xuHmRGlrPvQl7IflGlVXawjakcol3afr2CI0kNrZxjkdd2thwbvEZEFzobsX3E7rjn0RCaX0f8uAddZcFrZxZVD87bFh2RSbRy_fM8tfE3obLsNI_NdkPy1zYDvkmYVAWkRjSuUb1pU_eVDh0vtxwFuukrc2kzIz6DmMBxkC3inl8N9-j01TpqNwnf6S2zNaXZY8LRP19FPSZrTroklbkS8ZMe5sSJ_T7erXsJKrcQF-8xFwnl7BKiu0c2Awm3QArx5u5xP-jQ31qupm_voQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=XqlUxajrwOVPrsNsLMq3xrEKA4vBBPy-jKwppJmfO-bJ3gfn0uvg1qTB5hEOxaGMu4PbFcLWNTx4SIi8JXI5g97obWWQ3qAZ5iqa-uTTOPDID_ykQjH-iUyD9_-lCxywJRaWyRlVVY1Ct0biFH7gVsmYqsf2EZIVOIa8-rmKaf4j6IouFqdkS3LleSvduTn5i7HVcslRSBNDHAb0BYg6tAgoiE2VYPTQMsHhRu9F3Z8-I3hjk_nrp6rGvfMe78Y_Xv7XHUVRRsHGHCuvFpFt06QAEqCYTkfgqlCCS02f48GIBKQM9K_aiAuRQmN89OHVeAvoQoiNdB8pNz3u3TqIn3AiW3uHU6wn8m6ORcXCrlyZ3-2bPOhPtdBYRSi6o_tKSVdCaPVWZJGQ8p1nItBTmGGVqLhpXH9wzm47FcPCkkeIoiIvMkmcYX1TZ0k1suKQALLfk5yEAYZQmMhrNP3PcvhVJNP9MYHqY-z42S66PWcflzGVBumZ-86iUjL96SusIrr90ga4hCJOgppbvZ7fcmR0pNPV-aEN4gpnx1yHNpHxNt1Tre6LUSnDcECGP5gcogGFOi90mLpVR680Dha4pFNwrStqFljB5jPLmUCuPOWXIbRSNHZRTqxwg2Z4aceD4sOfcZAHeDqHQZLQz_8tM-7QlzJsFj1EqpVP6478ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=XqlUxajrwOVPrsNsLMq3xrEKA4vBBPy-jKwppJmfO-bJ3gfn0uvg1qTB5hEOxaGMu4PbFcLWNTx4SIi8JXI5g97obWWQ3qAZ5iqa-uTTOPDID_ykQjH-iUyD9_-lCxywJRaWyRlVVY1Ct0biFH7gVsmYqsf2EZIVOIa8-rmKaf4j6IouFqdkS3LleSvduTn5i7HVcslRSBNDHAb0BYg6tAgoiE2VYPTQMsHhRu9F3Z8-I3hjk_nrp6rGvfMe78Y_Xv7XHUVRRsHGHCuvFpFt06QAEqCYTkfgqlCCS02f48GIBKQM9K_aiAuRQmN89OHVeAvoQoiNdB8pNz3u3TqIn3AiW3uHU6wn8m6ORcXCrlyZ3-2bPOhPtdBYRSi6o_tKSVdCaPVWZJGQ8p1nItBTmGGVqLhpXH9wzm47FcPCkkeIoiIvMkmcYX1TZ0k1suKQALLfk5yEAYZQmMhrNP3PcvhVJNP9MYHqY-z42S66PWcflzGVBumZ-86iUjL96SusIrr90ga4hCJOgppbvZ7fcmR0pNPV-aEN4gpnx1yHNpHxNt1Tre6LUSnDcECGP5gcogGFOi90mLpVR680Dha4pFNwrStqFljB5jPLmUCuPOWXIbRSNHZRTqxwg2Z4aceD4sOfcZAHeDqHQZLQz_8tM-7QlzJsFj1EqpVP6478ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
