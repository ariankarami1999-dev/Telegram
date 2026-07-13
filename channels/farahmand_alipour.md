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
<img src="https://cdn4.telesco.pe/file/Ra8fXhCG8Sx112UG1xK3ndbrPnrnlubteoA9kIX9bFCitPWBxuv9cu6DytwQy2z8m-m3WNpb5WZmMEU0HziPmwP1uAKW1IlDWeGRqcpfUjuSTqt07kZ4HjnXb-rRYQnn754XMSN1Y9qZjjExYrNsZLkn-t5Tx5yIaCvvwo7ZtkYS7KxumhecxLydi19D5uSFn7M6kw1sUXq5eAHju0OoRumG3wDNdLJKWZxMjMQ4MJNAhHkuW-gxh13zfArSfowCLSbfUq1ouZkcgSKoOOEDVEmVXd4U5ewhYLYRZugAJgSLNSQuV1sNLZaXKOmK4jeHzGbgxWXHh5EeAriwWhEYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=JeejeAdMdS_Rk3rLM9C5RPUsWcc9tyQw0tsQmnUr8owU1DjOmJ93yihGy_IhwFqtKFz1JqZ6vcfhE27FZZrPOtdhXtYXF91jmpMJdO4XupTC4KCqGhMFK5O08y8UchbFl1nWRiXKMK8a86BZYCIjBs4wHp-6LOe7J-B6nW_gQ0MvdF7JQJ3WzNLSxSv9QfuuOUC87GGafr4exMenpZ_tZO10xQRtkzwflypnj5ychppOYcjnRu93ttrunUOhsWeZIUk1rbzsB7tVoELUb8QYXDSFcp8BT3pZ3l7xyrfKDEBP9Qph_wn28-NRpg3wRyBcCz70MIoMMEytUS17L59seZRRkX-nLao518hIVkHZOqrdnU3rKf4uHJlYoLnl6GWyOSrLLcRBwo8_OEJY0IadGHgbCHcjxzOVYQLvE2gS42tFFnsR5esq0b4pjpTbZ8-AIH9JKDSu_zgOjFSDAZg7vO_cdQK11aBAzkSf1AsIP3nN5dxkrSdlWbkZUfLbIOMVSH3qK1ANjSq0YbmdAfsmbX4llkzks1EI1dsNxbgxL399q2mcTUbEKyTY1DkJ51Pcd9hGxqvvI7LqRA-cXD_XGPgtcmYDKQD8eCilszgJP-pGw-VfsHFDd_nEHOlpdFND38_HHYAicJ8qwuf5MrKDOqTqIEqRXLJWXLSyvi3TgXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=JeejeAdMdS_Rk3rLM9C5RPUsWcc9tyQw0tsQmnUr8owU1DjOmJ93yihGy_IhwFqtKFz1JqZ6vcfhE27FZZrPOtdhXtYXF91jmpMJdO4XupTC4KCqGhMFK5O08y8UchbFl1nWRiXKMK8a86BZYCIjBs4wHp-6LOe7J-B6nW_gQ0MvdF7JQJ3WzNLSxSv9QfuuOUC87GGafr4exMenpZ_tZO10xQRtkzwflypnj5ychppOYcjnRu93ttrunUOhsWeZIUk1rbzsB7tVoELUb8QYXDSFcp8BT3pZ3l7xyrfKDEBP9Qph_wn28-NRpg3wRyBcCz70MIoMMEytUS17L59seZRRkX-nLao518hIVkHZOqrdnU3rKf4uHJlYoLnl6GWyOSrLLcRBwo8_OEJY0IadGHgbCHcjxzOVYQLvE2gS42tFFnsR5esq0b4pjpTbZ8-AIH9JKDSu_zgOjFSDAZg7vO_cdQK11aBAzkSf1AsIP3nN5dxkrSdlWbkZUfLbIOMVSH3qK1ANjSq0YbmdAfsmbX4llkzks1EI1dsNxbgxL399q2mcTUbEKyTY1DkJ51Pcd9hGxqvvI7LqRA-cXD_XGPgtcmYDKQD8eCilszgJP-pGw-VfsHFDd_nEHOlpdFND38_HHYAicJ8qwuf5MrKDOqTqIEqRXLJWXLSyvi3TgXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_FEgegbTtDmpOG-h1cl0tLFdIH2zI0RfyqmLTR-MCNVB9KuDHpnxGOazS-XwQTUgubIqH3mT_AgFeRni3g6H_7yiuMF1yL-nlJbotxfdeQ4aSZs1LR1diCLTSLoGOE9PahxL0VwXh6cdeq0PShg2ekRIwQjtto5dlRpqY0tm5SWFJeyuPV-L817yU5fdpYajUFf8vD_eBB_OszeqqAk38JSWy-FWWWRY9ov90rC1dHcvRBDl8jgqRWa7ELCan50r3KUvGXJlsZRXwIRa1Jedd44vBooWx7dq6zV66hnDdm7KB-Q7ohe0Yzrxs21V56fynDmC6TA3I_el1WfhmcV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gidsmNEnzGcmQ0wpDx0bugY_bOnuxSUlelKEpWvIH9k3urdUSo8KQb_ruYe41N82F7ZVRBCK4wWyNeFSyJIomt4ByZE2Dsv0ucsOVzEKydSS610NigwIB8u9ZH_DzUz30LIxiDYKF1v7uVCJNnIPYtXtXLqaTWbckLjeyL5b9ZJDUV8_K1kU2NA9mi_SQ_G7u2rDF_fQo4xd4yyCUQ7HBKWTsZe5jPWa6hoqGIXeKZ-pzVZZZQdc6fWdZTgqFDw9Fj-oNdBhtLzU3W8vBkYTCt1rc5eiq_BfHrcPoBWVuDoH6iJGM170h5z0utxXr8ITMOlvZfbqaNcHCn59a2FH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WodYqipS_f4drNmmCLsdRxnfGxzGkE9AkTJYlt6iYnbfZzpcem_vZa9XsBaKEOvSAaJS_9P4agq_4HDGsFuhpDnKDi4f_yl20g4i4VnX5VRvRwZjsqeI3k0hYFcBkl_50ci6CaCiwoK5eQSFlUdWVlEC9_fmWzJJII_fcD1Xm4Hli08-szxeI5M5cofnOrv7sczl_plveVieSIP0-SPlVyGO5B6KDtQXtIgIIdS0307oZLj9XGchYE1ovAEvBCtvr7ED8F3pTX_OQ7Mfe51nSWXxp5-fo8oRAYQ8eatbkykGSa_ID3sxuAT6UwfcnPmEOCzsTTm56gLFDpK8GOlyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD0muKxU0borg_9FS17lI2uS3pFJOmdZgTUXKOH4mgL5D1JKPW7LGGs7XfOhpMtI-BLUbVARHuzkYAkTg4CzTjgBW-5x-rSN4zDlUVDUgZiI2Ql1iSYgKay_dPS6LltmSMBniJQ_Tz1ZIjnhG6eNRDALVFD-MUlRSrlvRhM_qb-3cYff-jjF1tvDNtoSwlDBB5d5BIoW3eQeVm9s82l60cmdPU6-4Gh-3a7Ne46hWDDhdjLURqcGEhxoAE1BGCRLC0sk7gTAc_mJBEerbJou-nxKaoUICqsWiBJeZ2yW7hkD7njAlP8KSzKe5HoRkqKzFm8NeoXEQTc--ZpQI-dDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFm_pvl2dRzeWo1nYU2vlAXkzIKSDiHGpsHh_ejdOgH6qhZajZ5n9vcbXbM_n5Bvzq7waf5xUaqRFUs0dyD_w55Vn537Er1apNb8at2yVwpgODAIq01ndlbHYy03U1l3P_7Jl28tbRmTRgVBGxCsp8DpInjUMAonLJBzKiXn8Nu_JA-oXtf10Q9eOH9eUQH_6qrpCzS4Iwei5IKIutnwL4hfkYf-lOdVXvXnWyVLxEilYycXesgeq8JTmkjiIZG9LAv3m2WYRmRK7G8fz4tprRObbYV_HgQjy2IVlFX9HqVKDXu1nc6Ekehh-9l-pCT5JiBhdqN_F24Dz_U_R-f7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZy_T-3OfghHmboNPupBrtUINwJxIJ7jPjwSm9mpKvcc-YzW4UYns1St5dJ4T1JxOkyEAld0vx-ITtvKgYS1eJbsdYfC8J3BrdkAaEL-YhJxft4SlFhxNVhDNWtgIlDSK5EFLYB2lFbO12DEOtOyJfK5RlNjvJwooL7KvlIUM92d0Ds8raaSBQmn5Vw1uN_hTLOCHvOFBuAVIpbGzE49oP0t9D_Ny0KvgNzu83E4qjFwG8KvPXb8uibtSsq3BG0dUWZJBwsuy0gW8F2m1PmFNAMhOXPzlJGM12F4w3LQsE0oBmmvAdwFrF1WxSVe67NU-GNUZCO6A8miUCgZnbWymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=OtoCKRbhoBoLPmR1f7j2LCukFs-XFoc3veRuC6UKxesea0S4C-4A5Jp7vlprHs7enIMtlxXrE5jRK4HrEbo0mRNLTEj1F5FCDb2lMK6iILkH4bLn3KMBMIMk3qaG7aAyglPJ1SDDFUIMFttm8czNpSV0HSMsg6jhkw_auzmYXQX1JPh6VpYwG2aH7a0pGYogCJzFMFJFlSBphA2QPrR3KOIr5Y04XNH1yi8-0E_rOd9nZU0lga1odAEtgNOSLD9Q-QGr0fN4z9g_SRNDglXqi5_Jn5B7gzkmxp5Pl0MurLtGB1e--X-Y4xvLbKjjaBBCsqcOLrRu2zPEoFSIT6MbAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=OtoCKRbhoBoLPmR1f7j2LCukFs-XFoc3veRuC6UKxesea0S4C-4A5Jp7vlprHs7enIMtlxXrE5jRK4HrEbo0mRNLTEj1F5FCDb2lMK6iILkH4bLn3KMBMIMk3qaG7aAyglPJ1SDDFUIMFttm8czNpSV0HSMsg6jhkw_auzmYXQX1JPh6VpYwG2aH7a0pGYogCJzFMFJFlSBphA2QPrR3KOIr5Y04XNH1yi8-0E_rOd9nZU0lga1odAEtgNOSLD9Q-QGr0fN4z9g_SRNDglXqi5_Jn5B7gzkmxp5Pl0MurLtGB1e--X-Y4xvLbKjjaBBCsqcOLrRu2zPEoFSIT6MbAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=ZJ3Xvs8V5czeKJkOH8uC5-Rv1a5c1oiX2bWXkRzztBBahFQgni8yIpfZM8k_rLRyGrAKtAtBiLyFDkYiQSpp9lgA6gTQYyX-DgF2y4qSBLdifu7AvFGqYQJH8Db2ROd32AEuHaqatgoz6-Y1ff-m21zPI7tCO_8DBBDJA3JDE_8n9ccis626i8yvPKfZ_whDUrZF_HOHMjHEPTKBFX-EDVrMYosXIq_V4HISEP39QrtZhZRNo5QFC3PFoe6JK0KSZK1YA7k0DeCBeP8xoKswPwu-OwUmplFJjmp5HEcR6XRuYA0PB_2qm8WJmT1F-ax3pI-jAhoaa3FAEV3ZfujgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=ZJ3Xvs8V5czeKJkOH8uC5-Rv1a5c1oiX2bWXkRzztBBahFQgni8yIpfZM8k_rLRyGrAKtAtBiLyFDkYiQSpp9lgA6gTQYyX-DgF2y4qSBLdifu7AvFGqYQJH8Db2ROd32AEuHaqatgoz6-Y1ff-m21zPI7tCO_8DBBDJA3JDE_8n9ccis626i8yvPKfZ_whDUrZF_HOHMjHEPTKBFX-EDVrMYosXIq_V4HISEP39QrtZhZRNo5QFC3PFoe6JK0KSZK1YA7k0DeCBeP8xoKswPwu-OwUmplFJjmp5HEcR6XRuYA0PB_2qm8WJmT1F-ax3pI-jAhoaa3FAEV3ZfujgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=AzGoERdBVncGoDK8kcPooZ6q3k8VpriI0KTaJFuYm_N8hitx_KWtG2kYxl8lruAKxBGSwnqY6Tn6MhiSVh7Zz9ygOTo-5TA2f59eOc62B3SzNP3xyXFKRtR1foBVeFN8DH0qOhrwfI5z3KyVmkNSUOD-Ne2Whld7ss8MG9XRL2RNrnwInoHbuEqbUJ3hZQRz0Dnrprx9eeqGKLm7m7c_rx_XGPVuNRL8GWyjw9bwpfzuES2o6rF0XFknZ2bdVOZ3Lw7vbUzs1eisRvQ0_HrXQs6sWBEnejd7_bGEPLBieOx-tLzQaCgN7mtwB4O_M_hC8PE_IeFb9Sqf7HL3Ynm5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=AzGoERdBVncGoDK8kcPooZ6q3k8VpriI0KTaJFuYm_N8hitx_KWtG2kYxl8lruAKxBGSwnqY6Tn6MhiSVh7Zz9ygOTo-5TA2f59eOc62B3SzNP3xyXFKRtR1foBVeFN8DH0qOhrwfI5z3KyVmkNSUOD-Ne2Whld7ss8MG9XRL2RNrnwInoHbuEqbUJ3hZQRz0Dnrprx9eeqGKLm7m7c_rx_XGPVuNRL8GWyjw9bwpfzuES2o6rF0XFknZ2bdVOZ3Lw7vbUzs1eisRvQ0_HrXQs6sWBEnejd7_bGEPLBieOx-tLzQaCgN7mtwB4O_M_hC8PE_IeFb9Sqf7HL3Ynm5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=flJ5pA29efft5HAvoIn0n0vNTl-E90m2XpRKv0VKEqIxiBsgnLepfg8JEEUZnIMtRxjMhMtJM59RMAOEXY_cFQjaUU1N6hkyUBiwjT85RFCZzHBQbjqG0IdAjELpf3kPpJ7JVeR8H7mbxn0_-AbiFJ4mJpib_h_2EppSrB3K0DQ37tvVPNE4B6jbWenVBdFiC8CYGMXRIXWSqbCvtBtgnzADuXezP-Gp3S49dGibSn_RX9Aay7HNjr_RsnUJGW4xtdXEdKOpC-4zvGlPHs2E2RSebWPWB-Uv1-3mPuid9D_qFY3OHIYBpYwEYCl2Bsb_ubisnqfVGpYJ1-kNjBn31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=flJ5pA29efft5HAvoIn0n0vNTl-E90m2XpRKv0VKEqIxiBsgnLepfg8JEEUZnIMtRxjMhMtJM59RMAOEXY_cFQjaUU1N6hkyUBiwjT85RFCZzHBQbjqG0IdAjELpf3kPpJ7JVeR8H7mbxn0_-AbiFJ4mJpib_h_2EppSrB3K0DQ37tvVPNE4B6jbWenVBdFiC8CYGMXRIXWSqbCvtBtgnzADuXezP-Gp3S49dGibSn_RX9Aay7HNjr_RsnUJGW4xtdXEdKOpC-4zvGlPHs2E2RSebWPWB-Uv1-3mPuid9D_qFY3OHIYBpYwEYCl2Bsb_ubisnqfVGpYJ1-kNjBn31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs-XK4K4YAawv_idYm_nSQwA6-HEVhqUZL4mEUouidXpUu-V44CWw4ueozAYP-jBuHI-zQL4qX3scC_aXtG3SwCheWc9d5TaNqJuA83EpUsvGaIfAMFwJcQxvD-ySQUlFP5K_9DUK9rfzgen0dXpXv-IDZtsfzeiY2z06lEPfZs5szY1Epow1vtIYgWNMYBGXrnJ5D_xos2PqqG8M-YT4tmIZWA-okKT0tVEd-btiQF-Cj0_Jec4AMKfc4e9RKzwrnA5XnYJKNyKHnIYGiZQdhLnw2aQZjsjXw91jpCLtxo6eY2-RhMQH0OxtOwgEPayvbFTZZ3S4ioIDdQGeJMIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAq6ifYHW-aMp4qYTNfeQ43GR0zsyvy5saZoUVSiFo8fG3MvZVpa78nZJ9olfNBSZBO31V36DwKr66kNRLH-_PCzK5lOFtQ36lJZn0LDht2Mid5_n_RGi3ufmeak45Vy9cAV3NpH_Uj2KzIxCrt1IIMJsqzpwVrbkXhTgImS77ez01bRccLNtkW73L-c8Nbw4MiQTyIwrrErv0nS5_7XfF78NystPAPI8ry1dHw5ig0rltabRaDFLisjYDYlYQCq9nJnehCwD636eAV3c8ajvrB-rCgF1_YGNMqcBYQZZPvW95C7AjgCPKQBAUDdhwNTw9Fcf7Ftpr-HEgbRn6DPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=OMme6D_RRhR7UnMRdSQeYZDrhTlqWPJui1jNJjFiUJxA-jje-nq4jjjhZorrabJs0kAhT3uLXbQqWE4vd7GKuSmWE-mggeDQ__PY3QsKBH6vXb3ngdy8gZ0r-ywYtVESMjNUOjuBHnZcNVXP8VCrpKHHgGdRg1hpi1pfF-dQG0oPA72HFNdk27jsRMuU79OpxfBRu-RUabDPl59JGWi-Rc-Sa4GOZvenKtVESmx6XGos0K2t3YySj1LIu49N7X5wCNmGaxzWWRvZqGoakBwzwgk6c71eXgJQUmmXrTShht5Q7mce6PJawR40-TW6a1NjAwHn4QIZZTJBFewOrkPyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=OMme6D_RRhR7UnMRdSQeYZDrhTlqWPJui1jNJjFiUJxA-jje-nq4jjjhZorrabJs0kAhT3uLXbQqWE4vd7GKuSmWE-mggeDQ__PY3QsKBH6vXb3ngdy8gZ0r-ywYtVESMjNUOjuBHnZcNVXP8VCrpKHHgGdRg1hpi1pfF-dQG0oPA72HFNdk27jsRMuU79OpxfBRu-RUabDPl59JGWi-Rc-Sa4GOZvenKtVESmx6XGos0K2t3YySj1LIu49N7X5wCNmGaxzWWRvZqGoakBwzwgk6c71eXgJQUmmXrTShht5Q7mce6PJawR40-TW6a1NjAwHn4QIZZTJBFewOrkPyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQNcMnsaLJe3SshXE9L7Sj5rjbzs3izlpFESD11nsUu3K6ym6UJRDNkBZW5X9AburCg3BUwo8Sy96NhKCz4YTBH9txUj8GFYsaCYRCCzyeOZlocQjX6ovJIEhcB_6HrQnr4qjiiEpqj6igDAllaeeeV4jKrl-Bs-LTF9CvHUDpaE3NVU6c5MSqfOBUPZydQBZ5l1IA1LQ36mFlGNRM4N62OJUpUcA0BIAjfaWQJuGzaldukGfZafoUcJ5_UvPpwZaUuZ4PRERq6bT1AHyCZRn6tcft1VMcnO03fqwUK67W8ux7xPebPrx_un6o63JrcV5Qv4DHws02PnUZbgr1ko3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=D4THnIN89ZZ_sj7DX1uOUtzFdW8B-Gt75Osx3r34wh6LhPQOhkVdctxgrCOXKzRhXx_EreNN2wRucI1bkEfjqxeHNCcF2ED3Uimn0Sau3fNNOZt3zcADxf44jGJxxJU7OekHBMwB_4WQemGxIwE719CmFWng4CoPoeU9M2tebKxwH26dhVpwbWbC8HX9b3ZEWn4iN_IqqU7p5Q5EzCvEKqAyq-xyBFYNODHsxO2UYfqnCO_D63gdCIAoER6GESgR3YlXtDin4X0Yq_6_SVyGVrzHya0qKCspXBPujj8o58Z9r_adcimOZsPAEsHaCCtcJgOCtpcG1rP9UIU1_rcWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=D4THnIN89ZZ_sj7DX1uOUtzFdW8B-Gt75Osx3r34wh6LhPQOhkVdctxgrCOXKzRhXx_EreNN2wRucI1bkEfjqxeHNCcF2ED3Uimn0Sau3fNNOZt3zcADxf44jGJxxJU7OekHBMwB_4WQemGxIwE719CmFWng4CoPoeU9M2tebKxwH26dhVpwbWbC8HX9b3ZEWn4iN_IqqU7p5Q5EzCvEKqAyq-xyBFYNODHsxO2UYfqnCO_D63gdCIAoER6GESgR3YlXtDin4X0Yq_6_SVyGVrzHya0qKCspXBPujj8o58Z9r_adcimOZsPAEsHaCCtcJgOCtpcG1rP9UIU1_rcWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDS8csHKLKXa0hvVNxH58An4Nu9Ph_dimocvyy0BuajlCQCikkTFIX7eNdIieQInBfSEes970eLUBT4pp6LJZ3Jz4B09IkkYyXyPkaxE6-dB4FmX3xcg6EWn_oOQbZmY5nVhedDG3SxNrPcCGkaL-FYPUBvGLHM2tfan2Ij4624B0Dev8t2N9NUAUHhERoSdstXgxl5W3KTHAyylAewEJCIJFlgGZg1Hv6h3Pfidm3w9DjCqdiE-M8iK91TZVFwrc6rNzaAJuPi2ceeEwyda3s5AR7ZsDE7TwRuIZXUEUkqR6ZEE1xYDzSvvEiJBpMcN9Y3nFN69PdBONou6zxZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXafd_ccREJ_sZLo_GTngE7_XMMhvR6dTTpQhQxHhDa5wa1zS3rOCUnGITukqC2nVAZvfL4UwYEJDSCPaUH8M01Ya0vi6tGXWwSuz7tLC-6g6dKaBTRbV7B1paiF2XFLgowVCLdlAMyiauaaZAYlM4zlUltqgey_uhG27aKl464h3Wki34SLWxwhPypVDDgUY60TBoobY2gvqgbk2YL1bLIC7ra1sxKCde4UODmKAB9Rne0klTMgxXImLQd22SbsEuSSsVyZHMEEQIi5JNCFinxNJn1ajZTrFNILgslXmWC4kczhf6Vjre4v8011_C7vxoJWL8eLwjZOb6_n7OxvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWRIzRdNrRw4G5D7xWZoj-j5fuRBKTUJwjGcgkX_sPdvJS5h0S4qbHEtDKlje44p1IrrozAEgg5LYrohgrxhmafAKGb96LI2VIMJ5dibFesh73bbwUWzlkNval2rpNcOZi8juDHnI-27ZkLr5PmLFZuJ2s3QjgMTKXUAxUm6SBgrxlREyV9f5KyNfncyvfNXJYibnd5nd1qld6XVfxSaBNoC40dtwnuS-2K18ePI8sfDXdhM-xoSdxY55aK3i2GXyaxt0zqlbTud5fiyOLjTRB1YS3q2SfNJsOQFhcvL-LZAG6EgF-OjC99cpLgcpvHkuknI_wCL7s-40wMEN-6o3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUa-KqOt0dYcNzWafvXLGP1fPt5Ysreg_zx584RadsEYu6o0dzaZQO3izXlvROb9kQmhYCDEq0A4s0WKa0q0H-JxBrlv_8sy2uTMzC25NC1ezwkMUH4Ztfl8PeXcBM2frg4J4jJh7yiv_e_UsoLqgyhRL6OIv3iXp3ntP72VG7TFkJ19KyA8J0qk_mncu1Uw1g6Lc8wLJ2RFRuECpiNFbMlYibstjttB6Bk24V87zyFoiwcx76t_urESJ20wn26UTNFeFIqmK2ig4syEnGKIeCBnVL4cpEQ6CgKXqp4ABb57F6tyMfrBjHduavpwx6Qja21UM2eBhma__RbLymWjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIt5URff70xGs9s48cHqNRwy4Qx_ZWrJzbgJPRFSoAk_l5zrVSJDmtEmpLgCfQ3xHcZ5IOu17TeQ3xisjqp9UOp0KYLJcnqYmUDvw-3vLF3VQCoBtl4YYUIMHgKO195x77gWy6hUG95U1cfz1mrZ9Jk0DU6qX4cDamWaXi8ae84bb0c0kphddSpJBlKUoL6ieiWk8NijbKUXT6gXoe51FQWVEDRQmED7lutS0s8iS8oHfwr-tIpHCUM45zvwpSLI0Mid8yrIuOTX_g5x0AbDDdVpwtPTQcl1LsKvNlQxx0BtnFWArD5pQ-8g_8jQAfVGYIk8HDNF1MCoj8zFOqUZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIgV30k-xyM9cV8itiIdzJOny3byJach_PbZmAQrhlsPY_mOwARtqiRQjz2-ensoi-XOWow3gdZQxB8fNmv4cL6CjTUE4tNlsvL7oyP_Bopwwh8P6S5uPaU_cgohNhGvhAKVVloK09uWre0xkCGtAuKfLqALRc3ULOXRxIrNst6OXyYq1LB1v9fJxQn-M4j2rLijeYnKLy4HB0P9wUo_Wh3jWsmHB-vgbdPhhIqnx0pqFR3iEqGHe1KCqchhwCAOEO9ykIid-ZaG0WLg8XI6BEkdIOSwvx_nzE431U_ZWrqAEU4AOAVsOjFWyg12OAniHr53RVO2B4FhWhplrUJFvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX_kwK-oj2mVC1aKTLlQKnmSi2-Uyg7v5d06alhS2n6eHtVlwzdC8ljx9W0mN2jzP3c20aeVW5brcHEfEEDxyRrq6mq-OadOfoQ4AuJaTOfd3pFGYQvPvLP0-w0RWqEuABUaLs-u-Pp04saBhJbxrktsDTpEyILMXWdivW7QuFeUEckMPlic-dSDpOjPOkFD06mL5aO8UtGXdlX1Iqxby0XLb5JKBhlAclkK1nWA3taOrnJlimtSFvG9fuTT1Gc0uNNi9Si9uPjEcg9915RgmYS3R1h-QQFVza_BSeoVJUtCRIfSNMfJT5fzQ-sIMvYaIHckGhc4izhqB06-KwpWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0Tt3H8zm9HOUNjLbbgiswLsintFN53aRBIf-ToAbe3aKfDeQBEHgc3BKAYizylVOp_RkPvF2kp6S434D2IrQL_t-BCsvb4LB-Qxx2IgEZHT_GtpPniaCUiDHqXixTu1KmzyDlHIhj1xH0qfcAiC6yhZQTWQhBQn042BB67pDEL9N-tIMEBqVVA-BorCSW3Rul1jgg7n_A_tvocVa-9VGHRvIOYyZQa9jFC3QpoLRwXaKtDLtxnClTEckB7MN5ZlPQNvGDQsj6wbuDpzPzIW9_JYPW2o-A4aq0skg19T06xo4STY2C4Oy7AtO2mWUb1cD00kIF3uQ38qVmKuozsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtI-ARe7AOBOQCDcv54PsXLC7WxHhuwUFhqA-H-DIkFUf3sZsrryR3nbbee0bobVJe6KBxLn4ow_b9g4Mp0sPiRbNm-QV3kndJUuZBjZElo49Wr9_fx_usR_cVRhlUah1aF1q1ze7CkQharE1z4lqbvka8b9CyT4PV1RpZCXwlulU5n9Mqr1mIGP4ona0u3f0ZCZM2KQxIVJ0aphQk5LEVYreHzIVXn_9-OZo9Lwor_MV6Sj0Jsd5QpuaJ8c1VtlKwhuJSe0BUyHZdMjRf4hsNtCAq75dwxpNmoK3Ff8xkyK_UYCcY0Ol6Y-9u4d23haHG-liZYB7DedielH80MqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uynBLXELqWnXI-i8Zs2NZokF472D2h4erBT6LZQZkt6bYg7niglxMEAzkmd4KzO3jQthDx0bCeNymt5wfrR9wyiPF73lGQcEEBdci5chGyZFB5j4IShpCLX2jTE0SgjSeBF4pvSmqkp9zW7M1JqUoymjGjhzOWlgsLNae0VTX8ixQlXIakSqjsnOC7HTLOEKO0HnISqUR1Q-huNRaSQTElT09E-ZjY63RMO55fQtgX1j-toJpu0sTN9bOXhWWCS6i5aaDC_JvYs_Xgpfs2pLfIf3c4nrkcQGKVr-UrwV_aeP01R3DhBPu2oPSYJhZjHTLR3rkJB7NnDr0fsHL1_anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdunZ76HRriMhkoKimFECdCSBfi7EgX2V8HXUC6YAdvjHObM-EUPvsFc0INdfTrNx95vm8KUhg6UVh0Ngl-RY0t9k1IrbXNuvoMiIjDPXQzEDGuQBzpCmwEY3jBVRQbxJaHYylQso68vhm4XkMqPBq1E_fXDVctgUkHidsjB4W_Rerw4OwmMbhzHa83-dJa4Pw4Y_ztUdqqE9Y3n0dN5C6Z5WLmQTTwcQ47qFPGBdPWomL8bth7xZ5RE3oyMhDC4xK6FiU4oTwM2x1iiytbnNvS4ez-bn8S3Mw5XrilmbpmKs6FX2CFsCllUOzn08mxKoN7u-Rw2wg_utdHAYOnwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=e2e7sPWc0S1RgwW_467kA_P27pU6AIgYcw3ZtIsNmUsUpgW4nlr2B2oLVpN4q6me-uuoRwXEye-CoMaXO3qw_k2PbWpV6ZQWSAkGFPJkpqpWcE8ZJUcMUC3c_YJ6BdlH4rLRhIkOZ06kh3a2ht7QAPu8wGeA7slSe7zBYIDAIxzJ3iwzHJ5c_sYwGbeanhVoItE3yqpJCUAqX4CNCBiBJC6eEKY3IxAiwZEWtnqHQ8GaVGKsmdiaMz37LmHeWocTVJVL20y4A-Fr0cELwRNBloXncZ1yHugmmVIBTmRqGFFj1booONvs651xgNRytSsZYQQI5hJFtm8_24prucYrqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=e2e7sPWc0S1RgwW_467kA_P27pU6AIgYcw3ZtIsNmUsUpgW4nlr2B2oLVpN4q6me-uuoRwXEye-CoMaXO3qw_k2PbWpV6ZQWSAkGFPJkpqpWcE8ZJUcMUC3c_YJ6BdlH4rLRhIkOZ06kh3a2ht7QAPu8wGeA7slSe7zBYIDAIxzJ3iwzHJ5c_sYwGbeanhVoItE3yqpJCUAqX4CNCBiBJC6eEKY3IxAiwZEWtnqHQ8GaVGKsmdiaMz37LmHeWocTVJVL20y4A-Fr0cELwRNBloXncZ1yHugmmVIBTmRqGFFj1booONvs651xgNRytSsZYQQI5hJFtm8_24prucYrqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4RWLLpGb31TmRGQNFodu2bXfaubPNRMA3bghMmsDzFZfZTIIQQbH9yjpF4GpvAdEi1Tz8mi48Wg1FIT_6HjzU0t3y0nt3qulAQVwIZJ8-qvRUIw_gPpIZskOH1h9UeCV1E677pFsLJbm9FFyq2Uwwgc8NL7JL8uuXJ3qhGZ_RUamwfFkeSvQ76P14uYeCXJzSZ_dWny-UcH5ZN0OVLv8-OumSxClnfyd8MK3uGTvM5GeeuoHc3XRW-PbLoD-sDp3uoGVDL4NwMIGmt2on4iUhgWRfzdLGVHI9y2UWEdn9jA2XTzhUQIhAU-L1OGy3eakg2IdIa1O9s6oXIVBBCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=llrFjhz_T8Zt6-fvixkWxSWojVoC_5QLhhamEoD8ZsqiGy8wcQlNiFTs4gu4ecMBZenp5cLQ7Rhd49GT-G811WGG75eLfQt8BQgTQic89_vWFZBsB6pK-bEKXL_BejdvmzDdYU7adfv5ElmGB3YgrlTzsKK4qEip9QwJIcGA9Qf56dpVV5NomEzzvANU9PV1wK9VPZ65nQigG-DFeMkoI8x5LGm5KlxNDBLPk5JT7c_-pLukyFffrSFhqyteIT0ipupK06uZOmohDRmaZJqvXsSsOsMvvbGeQb_seLLsBi3OV9p-yaA1K485o052MGR5ZJpnB4HjLzikGgbdyy9cSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=llrFjhz_T8Zt6-fvixkWxSWojVoC_5QLhhamEoD8ZsqiGy8wcQlNiFTs4gu4ecMBZenp5cLQ7Rhd49GT-G811WGG75eLfQt8BQgTQic89_vWFZBsB6pK-bEKXL_BejdvmzDdYU7adfv5ElmGB3YgrlTzsKK4qEip9QwJIcGA9Qf56dpVV5NomEzzvANU9PV1wK9VPZ65nQigG-DFeMkoI8x5LGm5KlxNDBLPk5JT7c_-pLukyFffrSFhqyteIT0ipupK06uZOmohDRmaZJqvXsSsOsMvvbGeQb_seLLsBi3OV9p-yaA1K485o052MGR5ZJpnB4HjLzikGgbdyy9cSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJARcLaUnlEjoIDiFdOpBXGn08rspk3FuqjvhxzehUMzgJQJgNXxLkOAVXbPMDbU-mgthfdJAf918_TfHV4UhAINZzGA8GtNuCOA93RxalAJZwZLnoh20A_XOi7_J9lrAbbH9xddwFW53Evj8AEQI8EtFQ12wwvF_mT7lf46CS_3tI6NLlri7RrTq_NpBR2NqgYysgYXJDw9RE6YLItMVWewR1T_gCuD612II5VXQs5TtQ90fF9bMhG-RVYACvfRvYupmFu1WXhS29bCoVu9vP6DRmngVJ43WfpErM65TFIqPC949gMTJdW4uuNffdLjjnsR1IvmwSm96uA1LzgipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HszcwpLYD5RktXfogIHxuvKJabrVYaESYyfBRkFTI3RXZN7RV750bw1TZOL-YiknOceiphko1YSG-0NdeES2Czm-Zby85SBs_Q0_xxLgZsOM8VpJVA0Icf6nhwFv3UdrCXODgk--jPuBZVEwpOBwVtG8XU0gnQ_KI0hbHQxSvv-2KoEQO3qHDVoKpKQ-5NFCurFBXQl5LCxqEdQhX8AmoFT9AZiD5ArMRz_Fwot9jMehM3cqZBnVOxh8LMlkeh-Uesh_MZJzhuoK5JYpBTuDwbq2nvAjtqqvgyjl0fTKreew51aqXTt_HvfH8N-lFS6MOQxB90edjC82XI5FF2obUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=RumgtmBAkGllBtKjoaIl3tPxOHppXI6vAQNThRFjVc5ibX6eKqADqRaewueJ-4mTQF5X4Lh9w9A6kLbAaMqT-1uUIwquloXu9tXMlS5K6Huv4fb4H5j0_WGmxKo1JkIiX5KIgRwc0jzPCi0OZm8X05A8_qTrFry7__1JWfMDAlO6_i29Vukw4csLlZwKEdpI2CtOeTZbXXm7C5XUtBIYt36kyLbmOT7SaHjjvMIokhiTIYJSc9WMlXuO_Xzi9pOVfSQiS2Rd6LSnlvgPvQPQ9xMcplRmrF7d_GM-lnMq_EtWGFfv9kfPQmqJdyVeWaqLq3NSCEfLjx4O0uetURG_1iqvMcCuqMraqdX-oInWb96XVJZGdzUCkhvypz6FXgsV-GGCpBEis2h8Lb5mzb5NvK_m0_a9j2iiVu_KLmXp0w_-Va3AtnAqfz5TnFnzw-0jKypNwYJHQirG3BRR8NzPXQwTkPY6ANBeEMeQPUH9QG3GQbkLsm6iXUKUcOjS4cLbM8Pmhzlj29bHt47WxhyImSU9-x9L9A_d4q5jLWH8gHRH8JJntvUSMagHUE2ncnhi4Vmw32WfFwvtO3Y0eYOduEjZS5eO2Y7MhBYVoMVownuu4bfoLvAYj5cZs4qhQLqkrbm-3JP_YdsQ3ApwiyidEtirrc9tqD4ASF-gydi9DV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=RumgtmBAkGllBtKjoaIl3tPxOHppXI6vAQNThRFjVc5ibX6eKqADqRaewueJ-4mTQF5X4Lh9w9A6kLbAaMqT-1uUIwquloXu9tXMlS5K6Huv4fb4H5j0_WGmxKo1JkIiX5KIgRwc0jzPCi0OZm8X05A8_qTrFry7__1JWfMDAlO6_i29Vukw4csLlZwKEdpI2CtOeTZbXXm7C5XUtBIYt36kyLbmOT7SaHjjvMIokhiTIYJSc9WMlXuO_Xzi9pOVfSQiS2Rd6LSnlvgPvQPQ9xMcplRmrF7d_GM-lnMq_EtWGFfv9kfPQmqJdyVeWaqLq3NSCEfLjx4O0uetURG_1iqvMcCuqMraqdX-oInWb96XVJZGdzUCkhvypz6FXgsV-GGCpBEis2h8Lb5mzb5NvK_m0_a9j2iiVu_KLmXp0w_-Va3AtnAqfz5TnFnzw-0jKypNwYJHQirG3BRR8NzPXQwTkPY6ANBeEMeQPUH9QG3GQbkLsm6iXUKUcOjS4cLbM8Pmhzlj29bHt47WxhyImSU9-x9L9A_d4q5jLWH8gHRH8JJntvUSMagHUE2ncnhi4Vmw32WfFwvtO3Y0eYOduEjZS5eO2Y7MhBYVoMVownuu4bfoLvAYj5cZs4qhQLqkrbm-3JP_YdsQ3ApwiyidEtirrc9tqD4ASF-gydi9DV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-2cDuSMXvZLoCM1NMdWXpjRWNQLRLFo6HlsR1_VF7zmJPBprArElrAvp2gTkPVVTed-EDqAir2zw_VKZmxNlI0zn-xut886SV23rwMFdgXtLi2LTxiJeyQD-0IZ8ir2NkqP1QERfuBSCgd-dbHnAPAQ3BXOJQic-ZzxzMdVeo5cwfXZ4pXWMfTZIADohj-IvkxKDwMuzRAmYH32aLImUuHZT-3MGdAs2eYjtnM5BKSpPMiv3hWDFA7VQX6SrksWmHV6-R7BCXE4jFaERYZaiztau_E7J4Z-f43h2v7qMVzHQ_Fmf9dyPGYQV4NIN97o01XikwuTpgEDIFLs1eKefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUVPYGHIQ4w7hVauRSR4Rzkbq2keZWLGYwdTHo1DA1TCECRvq2keKtJ8sOKJ5Fjtuuuo9p7ret0gIc-oboagaMMXvKdyZqoUF-XXhVVjCpzvQeSbm5uz5sTvacKf4uDWwvO0C_nhhU8qRylOPGrGCmdNsriIVvL93ZrGpUNddcMJQ7CL65b7G9vN3hlLZhnGBp1hAIFcAulfR2IBv7qZPEGV4vH8NoVgUTcfJLszf6upzqgyNNr-wHfLPdIW0EycyT4mcNlnEKMOEGpBPHPwtSbcp_4TANr1qdSQZP2ALDh0Rx0Q276W1IhO_sUv7fJHN8_8U_yqWIhikwZjMnrHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUmHLV2EcvVw4GyLAAlMtEglH0l8hlPxEx2shD6UPObFoAMoJaR-MCOd99alqbWNHK0WNl0M-r4EYNANtNcdI2KQlLxrw4l1Sbg-78FrzLXGnRUErcRgRL6GIKmGX0xuo7sBnBRE2uHcsTC2-e8p2y_1vydKgPWYwWt0SAEKwrH_hI-HUScy91mpa0Oqj8l87CZG10Ad-fkZM7U0FUJ9r0LewEN7RBuQz3QOWILpcSWMxWryTCJI5VgUFKS3ouDbqU_c6sguJT8GNvqNkN-f9-Yj2a1weWT3GyPkAKyKdZHmsdn2R_hiOvRC-Ov21OL5X1ghVkc12MoeR_70V9xH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=l_MUFX8SpFnhWrC1pXUGfU1tqBAZMS3C0VFHWecOZ92WrxNajfXWNxXPRne5qGiUJvVhNWZ0vxnUHtlmmuC9kqzqz_b2T7XINBMzFhqlo8Vr79CIQ2kLgVzvn6FYB1MWZ48V3FC_OZIBY7zHude-qCnWlaXia7ttSubepYtNwDa8ocuT4qCXHDbuCPUjiFUSMSYIK-J2OkfSkxfZ8wb4gINS1u87RAPqAIl9dyGdd2QsWMFVSKXHTquoQRZCbUmAqJ5X3RUfTz0MOZk5CpkFV3vYyQJ_1ZPJd3UxJR0Td-Z-DyOYsy-i17wVqW-kWZHPLWvojfmM392zBjIT2amHww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=l_MUFX8SpFnhWrC1pXUGfU1tqBAZMS3C0VFHWecOZ92WrxNajfXWNxXPRne5qGiUJvVhNWZ0vxnUHtlmmuC9kqzqz_b2T7XINBMzFhqlo8Vr79CIQ2kLgVzvn6FYB1MWZ48V3FC_OZIBY7zHude-qCnWlaXia7ttSubepYtNwDa8ocuT4qCXHDbuCPUjiFUSMSYIK-J2OkfSkxfZ8wb4gINS1u87RAPqAIl9dyGdd2QsWMFVSKXHTquoQRZCbUmAqJ5X3RUfTz0MOZk5CpkFV3vYyQJ_1ZPJd3UxJR0Td-Z-DyOYsy-i17wVqW-kWZHPLWvojfmM392zBjIT2amHww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_aD52A1RWJCWPCIzvNUeUl1X6dBNehbwm3h91LBv02tpypoKe0waCkMASb_tPbI8DCrls_y1PBK7fze4R1hjrKRh3tO3FwUGZrkjHsDzkXi_CkS86OvfHK9vj_09_45JcYByfyYpnmvGpDaxG-JL9q_17sWNv-LAxVD4hfBwJCp9yfxS3Z4d-KW7eqKarrD0TyF5ONGxWjtCicRBVphRpZIC5c8_AwZX583MuySkgWM-WC4jl3n795ctMmutoIjKXFviEccj_PBTO4quzCWq4cVqEpj_uYW8w6UCy4SiM5S3y7xEztCeJHwSF2f71-FDTWgKShj4HLVduomKNavyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaCo6iK1c-tSIkOYEf0FDvfrZvDvUj9SDdHW-6c8DfvoFV-aYIOTRy_gAy-VLmLDRDERHz6gJ9j_jeyjtPVZJV77llTDVCfma-mZzKNK_PYh92c1HDpattFdw1Eaqul78uRr6elVeXqHaPs9Hkmgm6ieIM4DXUlUtuqNGC5ceNe_gRAXVkOORa7s1u7xzY56yTXKz3p_dvZPoXZ5resipTQY7jxbjc1W37gpssIfOqNjd-bs2sKXilXkJQWgIEXYItrALOjolhlCGGbv7-ZDAc0_U87D5EbGAMSE-_wZuwaMJY9KyWTYzpHC9TK0NfhMBQqOZFHkRqtfA_au5pwHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZfbZw57_BlNj6Jb2w2AQqo2HKLyAIqPm99NUzewZ085noutXI_VbhF3NyNCRXV3KZCFYl7gtTJ6dpUhFN_l5NlaPHnp_6Av_L0PugK1rxzIF-iKwgX4yYVl85K07SVixDLWiqCWRXi3MC5q-ckDSuG3OjtAu2WmUcCdubX3tsBN4O4kUiCgPmeQl_HjA4FXSWmnGRvUww-XcIGerwgeaUAefBRYV-WE7B7GeHYLOBxFtDaSRRYNoNzt1v42MjiFp2u0TR6pKgCnCrFPWCxtOQQ_7aaHzecdfiLD5gk9ISttqF-eObinYXFX-xyAHbMxx-uyVXA_qCJRjqbFIIJj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuR6CFMs3KGyAB1lXLNBn-cgBhn0b1sKsGZWJMQfRZ7aRPelfrZCEa23cKtK2_LF6Saa9ia5s69JpjfEmUd4b66t-2QycntyanLtAgtGYx3kxlQ0XfsXczddkayn9JqPCxLpNGdliwrPLKGrEOyiyVCy1MsGN-sU03CpYzGX4fzpD_iQYezOYVyHS_qjjhwvC799aJjEvLbawC2hpOSiibq1fkfVM10wpyQMRd6WmtE91qZP_yakcJYzQi--OvOZEJubsWHXaZYHBFTpOx51rCxS9ecv3uERFSEzaQTuzWD0HBblOW9gFASBE2bmjHbjg3ArUVHXxlVHkXFj1gKkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvTqStj05KxS-RcOgzEJ5jT2jweBBqEN74x2yRhqlTS8ElwXvDBGiKcEv9WfGpxYavnAPZe4QphUXWptqDaAYq_k37BYXJOTx4dq05ZkBSmBHmb5oYizGPlGdmAB-vjfgDte8caw9B-SKZ_t2OB5zttq2rilBkVOke8ZQ98756ujroN92w85DVD_Ppa-symM2_xwIkL2p-gC9EkXaTyHyFkd9IFV9jLPHyR6R3fC6Y-SDSYvcmhf6rzjE9TK7wvWc1NJjRZpKfeh17OdoMWqXMP_YRiz3njx6ACDdv1dx4PIXt3nqE4N1XTJIp5OAKswTihk2Z3WAgN2RGgjV9zgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRdSt0KxQTyppbDw9ZNTSspMLooBT8CDV2NX6_uXnYLzNKeZyN1SmiKxTFDpyhg2makLgBbeTzbK7QX-ibRS-1DJZFbPqBU3KkyBDB0h5utfjLmgAS8EIKBra7GrxE32Zr8c5bmzhYnbdWND3ifllI9ha1cCGdTU9tMnWehV4ut9B-cozpmve8j2wwfd1-ZV70IIPzzJbvMJkJPfxaD0UUrLyOWA63nkt6TelVPJr0cqu20wXfsEwprCicgYpxvJZUIXDK-XBtRhtinLPPl_gwC58F3LKQKhspkRmMBIZ0zosMXNawbx0bYmfMA7n2eUypJNOw1BMO3DBlR8KtGklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii2ejlxsY7RvNHVtICM0p4HNaxPyEhsGbrV5i3HiuPj_TtN4XsC1Qa17MWmZeSUL5nl0s2Ha8mPQ-328kjPI-0LcbkBWeRj7NuUVegd5ATp8X5PUzOH0LcA4XPnUaT51-gxxz29b4hsD_3n1Zi2j0kgJzO75BYCgNyiQUoj_zCfgmpOZydFFMbGFAjHFG4mpjs81z3KrPXKV_dMZISSGhqcur2VYweyKR71rXd54hlaRRZnlUvN9sODPmvcSdipcCsvSuTnHSjrs2HvNVVA2ErlZnFaETTQ77Wcj1tpZIgrFcYTVS4bo-pEXLq0gZoBXcATcQnL2-URb_rDV8yJAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dseAgsGE4VC5xdrTgjEVX50Y1-g0zqv0uRWqfb1J0mg0e1bcWKEbYVuifYvnj3K-Wd5ChH54XFRoQXFdYwPTNZ2FI49LyyuPycHaWRG6Z4l7SB-a1N8bZBwiSyJYe1FQBAOvTGC3Ofnw5A7ejV73mZP3Y_PYPyzzo_lS7j2WkRg_dEWjos49w8EPuvBAmYWPy0kJEU04a-drXbMLJxkN_R4Gh01GdhqnZefAqRUZ2Js3LZbaQNH-g9yZCqOgTtMcxSLxTzEJwZw9w5kAHoR_RcTfYeAUmOVVzvar9NDCA6T2Yy_kUnpvu16_2u5E6tvUHnnbTgyw513VjugkIr_2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JImXK2W8jFauAGwFcQaszNxolb1kJVtrRT_Of-Ft1e9E5lpcbmzNMYWezNnqUL61AxZ_HAepDqC4DrsKwXyk8pxpsalXPvqeHuWqMnwzJgzJrfFCjBWxhaSJ3RPJgbolcLw8biY_Z70gHF1rRGgd47AytpUhxfjFPJfKpVMCDXl4qN8_u0C9NV1NcSo3nU1PQgaml6e5UXzOs8-KEhW3am0Bn3EsSHPv_bF3M9FfqyGwoFkoLaCzkpRmlmGMZ4Dp30s-qDkGhWV5iIc2D4KrNLXZKGhu7DjQBGFvPdylT-KKcZ0jJss-pHPhIzEEkezQGDMYxw_-TPZ9xuN6EVuqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lI1ZtHW9P32n7riPpT6i56SK5uWLr1kI1rTPlyaqbqnYZbCxayDk2_ymPk2SHuNEPCn1GwGsxRPV_WQo3_NXj1aGq0uBQch9-uhRJwUEhNL1AToPPVg9QCfH8yL40kjIl--q3ZYIXsnnD9gliJ2UbNnmopxqpaNL8o6N3fTxlwWUYGZlzUh3-TWVazj9pdQNlmR62FQ7fI03vWbsinDJIc_8v5jMHC9GOkXZD_YKA67lH4K4kwQf0m0oQbycz33HeeILoHn9474EmacFkaQej0_KS6twmnlUUXYnWn5fqh7qj6OawNzjhC4b-6KWZumCW0WTZ60A9drq3ZpMqJEmKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=c2y46bYrSZUdfNfUyXkjzp02DueADrwjdRGdv3YnPCwbn3T4noC6UcFbGT9BRW4fyBpRLqXP9uPFJG0qd2nPfvPHvqwfhRde3OEkueGxh3C5KC7HY6nBGaMzCXCBFbla-3XoldipoVJzXe3gRrzggEtkAl7B9HWO-21rFaaUHr5zUN4sWXm0mMRQh-8Vj2j5tMSvI_3IZ6BDuYH1I9jdJnT1dr_UsbtTUVxSYZLebGlp1--lDEc4w1o0Glu5QuFRKqPhwzGv4cNaEKATJ7lpncOwOKvtAeWKOEBJwJ7Su4Y7S2WiNR2cyGCoEgTS3RrM9MIs5RWXRMjrbuumwNO28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=c2y46bYrSZUdfNfUyXkjzp02DueADrwjdRGdv3YnPCwbn3T4noC6UcFbGT9BRW4fyBpRLqXP9uPFJG0qd2nPfvPHvqwfhRde3OEkueGxh3C5KC7HY6nBGaMzCXCBFbla-3XoldipoVJzXe3gRrzggEtkAl7B9HWO-21rFaaUHr5zUN4sWXm0mMRQh-8Vj2j5tMSvI_3IZ6BDuYH1I9jdJnT1dr_UsbtTUVxSYZLebGlp1--lDEc4w1o0Glu5QuFRKqPhwzGv4cNaEKATJ7lpncOwOKvtAeWKOEBJwJ7Su4Y7S2WiNR2cyGCoEgTS3RrM9MIs5RWXRMjrbuumwNO28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=I3_a74lYxiDaX33kAXKRPsuEv4_HEooN_Xwz_26GGy0mDjAyWr4XyHfrd5hlzMq3uTrnC13OxKczfN4d4BWsVkiB_u2__cjOp2UvgirLh4ntPcrVmeX1oWfa3HslDT2qlFNgo4evwFnfbxjIvvMAmBLfTnPHmpINxxsMMNc2Bm8ZwXVW78z6aIbFNsjeCTkgwOzcKKCG06piHkgWVFKULHA_N52yd2um1R9ujtTD3mNY_UYOlNNL4ZkYr7dSkmgaBuby9IqNpjs30d5Lm5rivHbUz20ugjVi2ff14IY7V2FYfq1M-hiVrspY1DGd-6AIFD3VFSfeJlOWeZ9_M0PjEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=I3_a74lYxiDaX33kAXKRPsuEv4_HEooN_Xwz_26GGy0mDjAyWr4XyHfrd5hlzMq3uTrnC13OxKczfN4d4BWsVkiB_u2__cjOp2UvgirLh4ntPcrVmeX1oWfa3HslDT2qlFNgo4evwFnfbxjIvvMAmBLfTnPHmpINxxsMMNc2Bm8ZwXVW78z6aIbFNsjeCTkgwOzcKKCG06piHkgWVFKULHA_N52yd2um1R9ujtTD3mNY_UYOlNNL4ZkYr7dSkmgaBuby9IqNpjs30d5Lm5rivHbUz20ugjVi2ff14IY7V2FYfq1M-hiVrspY1DGd-6AIFD3VFSfeJlOWeZ9_M0PjEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHKoyFHalG7vmz9zgv8dUBQCQ9_KLkxSTpJCFqclHn6qbTS9qe8Jtrjg5kISqwBb_I_Dy5dMuZ3sBZZk0TY5vqWQb0zR-9MsOKXjfaJ3U6U-nKYFZmbp8ubuD1MGwcey19ag19MetLB6PWbufa1mHwMsTec8vl-kgznHt5dOn5AUJiXRngG4agXOOayJJpa8i1PjS30RqmCo9kEzWvMjj4MythMs6MTxcJRj3FrErVYygpF9X1396LSPSu2gMU5VYR5GapwI5D2JgKg9osA-EAggkdJ9QwLt8lanKWxR6v3x13fqbts88-A0-R1mo8lcN1MM90ehlucRbNMZ0BU2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdzFpM40nv9a4f5bd-NPUY97f2g-xJ8cHDYTUhzKHJpAto-uKMXWJU64tikGlAnQN8vWcb0n_xSw73bmGLlxfSJ1ssSmiANyl_bcrlchlhVpx0HzkeR93B9BBeO-tJRv3M9iDxfid2yOWKgICfTg2Miq1KpajNczY9QzozIFoY2SeiMBVzYmd9_RRb3cRMLbz8WQjp63feFXUnr1Ycv2VyGrk67ASDrwiBEZftayBYzviL9XNFJEib3UzyJjvq02b5StQgEilt04taYakUilog5p47KJUbSrhlJBp92izOM7j4gDUWv529cACavhmlNhebp2lkezqvnPSPIGzbL1Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdn2TqPr9hRnIi4KJLkEHmhw2hgEzbduxvfg7-xL3j5ci1p48bPVQMpFBmU_NsNsZhkzv77ixZaQsH6SPS3OEqZEuSmzAU-YsyPNvlu4qoSzgjL4-GUStt0-JXBUIUGr4UqZ4J2gdXVltSfVVLJSHdamDIoC5Lc7TxIQ9SKzL6Nd8G6CjRBnEjaQcK-Cnadksc3MX3xHwH7oRveohNTGvw_G-ymW9zu5f2ivOQnBOkBQOQ-Yq4vdo9X5OSlTDKIyI1MqaUE019oRIW8tjYyoFldglHKI2QT2H99ADveUuGDAeyFoBdGzezmIAkFNBRuYLYcJNM_56oxfJNdYnHD70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=HCupAr5xXjukO9gUtgYEdtacEMfgh0xAUlgrloVBfsEzNhvZOqmpg-KmaBk29QTRODTntpXOZcPcmMcNti0Ki0JjfKueh9BiPgLnc1wx512YKts-MJ1G4KvdsMxCAfUuhJ1wbj98tX3OLJ-Q7Ja-ywHRq9Rm1ORn_auw8-FeJ22XPOP4hcn92JzpawDeHrxsIamPABGydFV4s92sNoHYX6aCafrtl8xZWQf2Itj3iSaqbsa6TIbmg3cP6VhPmgPueIOJqlWan7DxdLZg75Kx8ETQwXna0GuBeo8Q5ZSA91bsKSjYw5YePMhhgvcBg8o6PkG0kyMj-cZJBg8Yp-1hpDwvrqkhYb8mQfjPrCwVFxxaJwf6cAlHeTyhP_q0Iwhk06Mj2RoNTqRg2C4m4MqMjd_SU9md9GWwQtGCesnWumorHCAHgrlmxN_CqVF0E3PJGLoILAitV2XGah3A4Us4JqgyIIGBU49AkD7FBSOJJ4qBZ-qEIzxWDrijQT0Ude8BD7WYerDyhKp8ZidtnyL-jRxEfOMRlwkyvM6DwD8dRXZq1iGMNPcqE0xyDQPbZ7IxiEPmYcYKRQZ8IXcJPGUqvBSrmDwIej2jJZQ6TKYaa4Ke_lbBshawvq44LOMYHF1-n4EuU5VbLp4TkDyh70RpA1ZwrTxkJbkiGUF4Iy6dX8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=HCupAr5xXjukO9gUtgYEdtacEMfgh0xAUlgrloVBfsEzNhvZOqmpg-KmaBk29QTRODTntpXOZcPcmMcNti0Ki0JjfKueh9BiPgLnc1wx512YKts-MJ1G4KvdsMxCAfUuhJ1wbj98tX3OLJ-Q7Ja-ywHRq9Rm1ORn_auw8-FeJ22XPOP4hcn92JzpawDeHrxsIamPABGydFV4s92sNoHYX6aCafrtl8xZWQf2Itj3iSaqbsa6TIbmg3cP6VhPmgPueIOJqlWan7DxdLZg75Kx8ETQwXna0GuBeo8Q5ZSA91bsKSjYw5YePMhhgvcBg8o6PkG0kyMj-cZJBg8Yp-1hpDwvrqkhYb8mQfjPrCwVFxxaJwf6cAlHeTyhP_q0Iwhk06Mj2RoNTqRg2C4m4MqMjd_SU9md9GWwQtGCesnWumorHCAHgrlmxN_CqVF0E3PJGLoILAitV2XGah3A4Us4JqgyIIGBU49AkD7FBSOJJ4qBZ-qEIzxWDrijQT0Ude8BD7WYerDyhKp8ZidtnyL-jRxEfOMRlwkyvM6DwD8dRXZq1iGMNPcqE0xyDQPbZ7IxiEPmYcYKRQZ8IXcJPGUqvBSrmDwIej2jJZQ6TKYaa4Ke_lbBshawvq44LOMYHF1-n4EuU5VbLp4TkDyh70RpA1ZwrTxkJbkiGUF4Iy6dX8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=YZDHwnowJeePf3B6_qlaq379ok6JUhoDDqqaXgxlzSgO1-Iy6_6xc5PZqeJ3dq-hsV30nbWtYogg0YbCbRoU64gi5AIRGET5Gq63sQ3uO57gZjjGqrTbhXYC_p2OH-_DWz2-IYyy2YCxE7feD7MORKqJ6RYTmiC7SaAUPKOfzjujXeWbH55_Vuk3JIFZmaIY2mOgov5yyKKUTFPdy-quxOWf4-f3HxymgqhfE0b4t8NHa2YJsKcGVDZ_2KDKf82guYTC_aH0NaD7qXkoNwq5XbQvXuhYxmwZw1CFGt-levt39xqtYUKtGb5LEmAD3VAvB_cA9jFCQTRjdxgcn4uOJza1Da7_uWB8m5pGqINvrAQXiti8UuTZsx28C8MWm3lxWs_Gctdzb-NxAUCkSnp9MXOtGQPuqi6z7maK9tsJ1BDz_zGhKkPa0tlP00b9sBngwSjdsxheLI704NDTcm33VhnALVX7jDUIwAox71yMosnz8BFc77Y9hV4T8MkSBPawoEhSOm6PasCHAwGRVTsAxhJxbYj0dmCGGOmk_ZfgJx7pbxv7bTAv21PZgi4wTXqVkml4MU7mhJE90rMTLIHNi3hbUenVwJgulzhe66vbTPn2wTAw9U4j2GPaLqrGiD4-_xjzCP7a-TERPHm3hXbBj4DxtIRLaepUvGNjOOBoXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=YZDHwnowJeePf3B6_qlaq379ok6JUhoDDqqaXgxlzSgO1-Iy6_6xc5PZqeJ3dq-hsV30nbWtYogg0YbCbRoU64gi5AIRGET5Gq63sQ3uO57gZjjGqrTbhXYC_p2OH-_DWz2-IYyy2YCxE7feD7MORKqJ6RYTmiC7SaAUPKOfzjujXeWbH55_Vuk3JIFZmaIY2mOgov5yyKKUTFPdy-quxOWf4-f3HxymgqhfE0b4t8NHa2YJsKcGVDZ_2KDKf82guYTC_aH0NaD7qXkoNwq5XbQvXuhYxmwZw1CFGt-levt39xqtYUKtGb5LEmAD3VAvB_cA9jFCQTRjdxgcn4uOJza1Da7_uWB8m5pGqINvrAQXiti8UuTZsx28C8MWm3lxWs_Gctdzb-NxAUCkSnp9MXOtGQPuqi6z7maK9tsJ1BDz_zGhKkPa0tlP00b9sBngwSjdsxheLI704NDTcm33VhnALVX7jDUIwAox71yMosnz8BFc77Y9hV4T8MkSBPawoEhSOm6PasCHAwGRVTsAxhJxbYj0dmCGGOmk_ZfgJx7pbxv7bTAv21PZgi4wTXqVkml4MU7mhJE90rMTLIHNi3hbUenVwJgulzhe66vbTPn2wTAw9U4j2GPaLqrGiD4-_xjzCP7a-TERPHm3hXbBj4DxtIRLaepUvGNjOOBoXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my8lF_Po1IKI2iwcDdxHX7j9d3SJOdSPkcOO_MdA1VI4Hauu6G_H_APlhCgyseQzhpkYUXPrCAcEQFw4uXRjzjBE6NZWSeOHeVGpQsmRdBJ9ZVdHXzJLg25cacg_oZIJxc88DVzteXK_li2k4-WcOQCFLyrz3qJNuFgSRq2-re87RoYzlTR5Ny0BRvEXSirz7UH8K_xWblrra6kb75YG5udh3LP2mEY7RpV1JFR-tAI3L8ZGwOYeq0LOopciGyf-UkJXq2tZmRXVbtUKYfWajOVN91448Zt4sxROoOp0g3EP7zbkZZMsSWFMIB2y8SF5DZbh4M4IPxld_oMDEgDlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPEbT7YZA-tM3ACJKLWlVuk8wLyfFiBZdyXBU1vEir011m-fm_dnflT_kBE77IoWo_9ESxGrWY8LcRoSbwYGSlT9VNAMZT8x2rEs-ouYfHQ0cxv7IcFdaEqSaX8mAvcU5JPlxbV9FYfSlxDfpgvfLjY9qHmVcOsZnnjRWevCeXgn9TEFSeDNwGryKvYs0XfrP23NkosVG6-J4SFuZALjDtG0e44c9KQofxQmg-rH2x_Al5sQEBDNMQZWj9ODtm8w_w8hS0KLMcZUGhmPXBhbqVslmR9fOuW-vnn780hB-59UXt-Mv5SMc0Sw9e0dvhwz3vV2i_CNIIJOrBdb0AAmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNtJ8soez4OWolriTLfvHu-tscU-Eqja7yQO4muWjhTqLdfVAbKT-ppb9JorsCdOMgUPI04x591sZ_-f69UQBOzLNP420Wm4XCm2vKcReU1KXRAy3p3R1AiRIsMXpVS6lam-WXT43lDTJuyIJDqV-JLpjd7axqegQUnFhBAjndFWwRyCowq7DsdeK_6gCJfP0fBhQVUBaZKH9X2UhU4Ud_DFpwLpGa-MkjkcZMUQoRHwFNg_gvDhpV39lVh6TuFzODzg4gJyIb27ZOE8KQs85hHXlUk3YGkFVFfh6WFkLvqXwC2yYExOv11og8oNkSLrAnj6tiPJ7IZxrMxZdMbhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=ob5c6OnaHwwEjc9tOFJ_lx_FZ0z3K4DAtHSrXZbwiadfxlcKRtgpsE3Dpio9ha0eVpltSGbGIuCObVPZesIWEa04ScCda2mq0H032EyKiWBd_5SyS4S6YEgj1LsPeKmzJiG_fyysyq-ptQTKqqyQuxBpVs2DW6bcFBQog_MFIh0PECaD7nWGBWHhA45GCKMk249GGoT1L08uxYunmEh2sw8gn0mXp2FJ8aiYwSmSNCFrO1kvtcpXCg5xbqmJgPASdpJ9ZIJbFYkqTpTewwFi8W-TG0YNR2CBiRcqItTX7YO711wOGn4y6JI7WeJwXjHv8xCcEnHLtzlIuDbM1ic95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=ob5c6OnaHwwEjc9tOFJ_lx_FZ0z3K4DAtHSrXZbwiadfxlcKRtgpsE3Dpio9ha0eVpltSGbGIuCObVPZesIWEa04ScCda2mq0H032EyKiWBd_5SyS4S6YEgj1LsPeKmzJiG_fyysyq-ptQTKqqyQuxBpVs2DW6bcFBQog_MFIh0PECaD7nWGBWHhA45GCKMk249GGoT1L08uxYunmEh2sw8gn0mXp2FJ8aiYwSmSNCFrO1kvtcpXCg5xbqmJgPASdpJ9ZIJbFYkqTpTewwFi8W-TG0YNR2CBiRcqItTX7YO711wOGn4y6JI7WeJwXjHv8xCcEnHLtzlIuDbM1ic95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzUNqQa-X0YPIACj7kX71mGK66H7DETZvC-CyigqW7POXhSW1s3Uu5eYIO3qjA94nPSelCBYcWvdmUqeZ0uWnddroTELUshKDu69LfXaOmaPC3YuyCbCHTMo1YSWXCJtiQ8gGLOnFyezCGctCqMJ8XCq3NwvxkHJOIlDCFyDD8YjW-8h24AEkZTM_osI26qC2m6YwhUaT3DcOvaOve_-o_9Ou_7WMpvbiFiPPRUd9LHtMYPynilI6XnBs2ZfeidWVM5UwSdCYXM0jAO0BY7kFHY3q8Y3alJb_CIofMfbKbtFKEQB_tyxb7_W8mqk1uqZ1hYBJGXr6rq8eU_Ga-2J1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=L1MvxEX-8X02ECh-iXrEBPk31SmrPssOj5UoI-rPa3ZBdv3VqDCI1nNEV4qB-GF5T03GWnDZuWN8zD4ksw2LT6W4vwD6s8Rx6rioqbnNC3m0twXAPMiO5vgUSFCiugahiNgqxMAHZjPn9qFPBTwYcsR6rHBXWR9LneTOaZ1N3WZfGZfYWSsGG77zcjRh3cywJZjqKbqRbiE6Nw3cvpxONXKuL1x_yyRfCZV753PobITr1KD8SDTCxlkqZ6Px6912J9zW52H5ztALyJN-su8lAb25A2Q8NOeJbF5FnN8AVO62a8b5CysQ9-3aTztQbVCMrgBYTQocUnEAoMLkFyqE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=L1MvxEX-8X02ECh-iXrEBPk31SmrPssOj5UoI-rPa3ZBdv3VqDCI1nNEV4qB-GF5T03GWnDZuWN8zD4ksw2LT6W4vwD6s8Rx6rioqbnNC3m0twXAPMiO5vgUSFCiugahiNgqxMAHZjPn9qFPBTwYcsR6rHBXWR9LneTOaZ1N3WZfGZfYWSsGG77zcjRh3cywJZjqKbqRbiE6Nw3cvpxONXKuL1x_yyRfCZV753PobITr1KD8SDTCxlkqZ6Px6912J9zW52H5ztALyJN-su8lAb25A2Q8NOeJbF5FnN8AVO62a8b5CysQ9-3aTztQbVCMrgBYTQocUnEAoMLkFyqE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RorsIzCi05Fpp4XiXAmXGi4_bqGEOv6KGREHqfdfy7WCwsghd86UpMvPvj1bKE8t2dmCx3OT5p9FsCSGiixvwISKyddqDO7PlQc_OR0Sq1FxMRQtY-Bypqvsp_FjV2se0DgzNAXA4JG2RW4TYbThFWjnDfQwxPGacM8SFUgVU_wuRfhh3UvviM4KYs3gIFIQ_h_nE76B4jtKzcEUuoxFwnz2_dRz46odtfNvb8O83SgLkONP_yINsjCsbC2w70wMtfM6eZj2B9ITS6Q0aRXsdvctt9pc602eviILK7iEX5K-6Doy8VPTlELoUG22i2cKd8N1JJ0sl_i9x0Jzb-HIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADuXfBylo_tzApx_kaqv_kqwBVM0PEgzRrtjxtwwI--_AOLxM8IXZRiNupQPh6DdWE5_FSuaqG_VpCcUhqfA9osTmnZuQ29vIcsDqaWH86w9CT_eORLWVFxsRVdRlZ1AwsLtFoFFaoc7ZZ7t--AR28ovBFfKSy_r0AsQDyN5dYGvLfCea0UGGooGOVQmKZkaF0mv3voCHXuRxr8js2hka_Tq4eCPan7NbBdkFjKvTrJ3VLsVYTwT7TG0h5QrbiwEnb6z-pEqEM7n6qncxScMEbHL_dFL9JjfIxDclCHKqbbKah6FYE5I6WHvWWk0LeZjcOnA5gFYxjBa5uAtDxkADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WzxFQH9KKVtw-t4wGVc-2Ofufp2rbpc83Oa2r8eITIiG2jJHPnC0WSV_T1-tsNJUqwgAV-v5FPAp3qLseC8DS3hEkhVJqmydevsAP7vrsn2dL_IfJ9BDN13FBK5CPf7jCbrA2bQiptyntP5Q7gL_FbebBS60YmppeQleURZZK8el0rgvneGDSXtEygWCXvLrXAgNT860i7rriKS1DCWH4I-dHwgPk_Wvvgf70As50J3vQ81ER6vIS3H9f7DTYEa9N2OE2-c0yJZplo2MDOZXW-Nj4evzlI11RgH16ZvRQQHbwyPQx2tXs0z40hP4LZTZY6se8_N_V46fNVt7tU3EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WzxFQH9KKVtw-t4wGVc-2Ofufp2rbpc83Oa2r8eITIiG2jJHPnC0WSV_T1-tsNJUqwgAV-v5FPAp3qLseC8DS3hEkhVJqmydevsAP7vrsn2dL_IfJ9BDN13FBK5CPf7jCbrA2bQiptyntP5Q7gL_FbebBS60YmppeQleURZZK8el0rgvneGDSXtEygWCXvLrXAgNT860i7rriKS1DCWH4I-dHwgPk_Wvvgf70As50J3vQ81ER6vIS3H9f7DTYEa9N2OE2-c0yJZplo2MDOZXW-Nj4evzlI11RgH16ZvRQQHbwyPQx2tXs0z40hP4LZTZY6se8_N_V46fNVt7tU3EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=DVqIx7Ihs01CMUgD87PFocy-JsQmne6r6WKUKItc3iI344Tujf-bLkUSLJdgiI8UqqJXIjL-d0f-ZEl4l8Wo7jVIF77IeR5pARBhxQYWL3rDkZqA7NT4B4Zaj_Yt-fluK_HZO4Os9t2Bya-zjiVuLc1g5IAKZqqqwxKCUtHBCrSWc1KX2syu4GoSkYanUDrxipI4KYpfDBu0tBuo0aHMUZ2_BICiCKLIQLW_tG7aZouFYbK3k-avwEVGsGTeyGuBuSxK3ijF2UU9mizTs9sJRBagN7f6aS5ETKDUo40R7nyWhzxg5eAUcr1G6CmSQsw7iY-pXL2LkCjT4cXakDY_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=DVqIx7Ihs01CMUgD87PFocy-JsQmne6r6WKUKItc3iI344Tujf-bLkUSLJdgiI8UqqJXIjL-d0f-ZEl4l8Wo7jVIF77IeR5pARBhxQYWL3rDkZqA7NT4B4Zaj_Yt-fluK_HZO4Os9t2Bya-zjiVuLc1g5IAKZqqqwxKCUtHBCrSWc1KX2syu4GoSkYanUDrxipI4KYpfDBu0tBuo0aHMUZ2_BICiCKLIQLW_tG7aZouFYbK3k-avwEVGsGTeyGuBuSxK3ijF2UU9mizTs9sJRBagN7f6aS5ETKDUo40R7nyWhzxg5eAUcr1G6CmSQsw7iY-pXL2LkCjT4cXakDY_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=M5nkC1Dxe1PQ-YcWxTuw3fW7buGJfhKzaozXTNaWx8MMpHgxOl3UglumgTgniHEGpRuS9Df3FvCSzje-TDZpefDuWmtbLfjZN0OE-A4dBBR-x6Kg0MQACrCKigMtrvRgWQ1UiTlRYku0E9ksHFmEW-Cwwe1gmu8YCpx9DAvlQRJy8c9f_A6Z7D3rrfR3xcAsj9DzXj6BrjluI-7c89YZjS2BxBqkSiAwebU4kl7ZMYC-7PKoqtKOgdoLw01RZjulCeAkjTsHlJ90Oo9jUAs-xnPTUXM7_2U0bJ3zAi7ET2hGeq_jSn8TXaXDYGjdGhxuuak8HC66w7V9QwJKB5u5LE1FXQ2W-AaPVhp8ONBidNVhGfe9mPteaaNYK5aNL7T-WwAfbIWg8zDsZvWAy0FJkinhflyzrpS_wdClShrhQl3_T4Vet-srNo_45rliWht_OaXaYM_jYhPG_zve2sK3ti4PiQdCadlbnmDul03axqxHnE8RZrG1xgzb6qQdNTugNNFR0y0fW37LYRTo4vEV_fd1tzluh0H7u2Dnkl6m5KqUqwntNa9Oz_6UNoi3pcRgRfa-kDGX1l05Iur7t9u5BEn40hAu9LvI8SL5qs058-imIZn2VMTgRiVYVttN1uQQadYoJNt3RbCnKVP5pskzBo1A1oXTNxrkaenMXrVeMPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=M5nkC1Dxe1PQ-YcWxTuw3fW7buGJfhKzaozXTNaWx8MMpHgxOl3UglumgTgniHEGpRuS9Df3FvCSzje-TDZpefDuWmtbLfjZN0OE-A4dBBR-x6Kg0MQACrCKigMtrvRgWQ1UiTlRYku0E9ksHFmEW-Cwwe1gmu8YCpx9DAvlQRJy8c9f_A6Z7D3rrfR3xcAsj9DzXj6BrjluI-7c89YZjS2BxBqkSiAwebU4kl7ZMYC-7PKoqtKOgdoLw01RZjulCeAkjTsHlJ90Oo9jUAs-xnPTUXM7_2U0bJ3zAi7ET2hGeq_jSn8TXaXDYGjdGhxuuak8HC66w7V9QwJKB5u5LE1FXQ2W-AaPVhp8ONBidNVhGfe9mPteaaNYK5aNL7T-WwAfbIWg8zDsZvWAy0FJkinhflyzrpS_wdClShrhQl3_T4Vet-srNo_45rliWht_OaXaYM_jYhPG_zve2sK3ti4PiQdCadlbnmDul03axqxHnE8RZrG1xgzb6qQdNTugNNFR0y0fW37LYRTo4vEV_fd1tzluh0H7u2Dnkl6m5KqUqwntNa9Oz_6UNoi3pcRgRfa-kDGX1l05Iur7t9u5BEn40hAu9LvI8SL5qs058-imIZn2VMTgRiVYVttN1uQQadYoJNt3RbCnKVP5pskzBo1A1oXTNxrkaenMXrVeMPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
