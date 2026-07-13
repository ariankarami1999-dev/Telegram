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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_FEgegbTtDmpOG-h1cl0tLFdIH2zI0RfyqmLTR-MCNVB9KuDHpnxGOazS-XwQTUgubIqH3mT_AgFeRni3g6H_7yiuMF1yL-nlJbotxfdeQ4aSZs1LR1diCLTSLoGOE9PahxL0VwXh6cdeq0PShg2ekRIwQjtto5dlRpqY0tm5SWFJeyuPV-L817yU5fdpYajUFf8vD_eBB_OszeqqAk38JSWy-FWWWRY9ov90rC1dHcvRBDl8jgqRWa7ELCan50r3KUvGXJlsZRXwIRa1Jedd44vBooWx7dq6zV66hnDdm7KB-Q7ohe0Yzrxs21V56fynDmC6TA3I_el1WfhmcV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gidsmNEnzGcmQ0wpDx0bugY_bOnuxSUlelKEpWvIH9k3urdUSo8KQb_ruYe41N82F7ZVRBCK4wWyNeFSyJIomt4ByZE2Dsv0ucsOVzEKydSS610NigwIB8u9ZH_DzUz30LIxiDYKF1v7uVCJNnIPYtXtXLqaTWbckLjeyL5b9ZJDUV8_K1kU2NA9mi_SQ_G7u2rDF_fQo4xd4yyCUQ7HBKWTsZe5jPWa6hoqGIXeKZ-pzVZZZQdc6fWdZTgqFDw9Fj-oNdBhtLzU3W8vBkYTCt1rc5eiq_BfHrcPoBWVuDoH6iJGM170h5z0utxXr8ITMOlvZfbqaNcHCn59a2FH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WodYqipS_f4drNmmCLsdRxnfGxzGkE9AkTJYlt6iYnbfZzpcem_vZa9XsBaKEOvSAaJS_9P4agq_4HDGsFuhpDnKDi4f_yl20g4i4VnX5VRvRwZjsqeI3k0hYFcBkl_50ci6CaCiwoK5eQSFlUdWVlEC9_fmWzJJII_fcD1Xm4Hli08-szxeI5M5cofnOrv7sczl_plveVieSIP0-SPlVyGO5B6KDtQXtIgIIdS0307oZLj9XGchYE1ovAEvBCtvr7ED8F3pTX_OQ7Mfe51nSWXxp5-fo8oRAYQ8eatbkykGSa_ID3sxuAT6UwfcnPmEOCzsTTm56gLFDpK8GOlyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD0muKxU0borg_9FS17lI2uS3pFJOmdZgTUXKOH4mgL5D1JKPW7LGGs7XfOhpMtI-BLUbVARHuzkYAkTg4CzTjgBW-5x-rSN4zDlUVDUgZiI2Ql1iSYgKay_dPS6LltmSMBniJQ_Tz1ZIjnhG6eNRDALVFD-MUlRSrlvRhM_qb-3cYff-jjF1tvDNtoSwlDBB5d5BIoW3eQeVm9s82l60cmdPU6-4Gh-3a7Ne46hWDDhdjLURqcGEhxoAE1BGCRLC0sk7gTAc_mJBEerbJou-nxKaoUICqsWiBJeZ2yW7hkD7njAlP8KSzKe5HoRkqKzFm8NeoXEQTc--ZpQI-dDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=OtoCKRbhoBoLPmR1f7j2LCukFs-XFoc3veRuC6UKxesea0S4C-4A5Jp7vlprHs7enIMtlxXrE5jRK4HrEbo0mRNLTEj1F5FCDb2lMK6iILkH4bLn3KMBMIMk3qaG7aAyglPJ1SDDFUIMFttm8czNpSV0HSMsg6jhkw_auzmYXQX1JPh6VpYwG2aH7a0pGYogCJzFMFJFlSBphA2QPrR3KOIr5Y04XNH1yi8-0E_rOd9nZU0lga1odAEtgNOSLD9Q-QGr0fN4z9g_SRNDglXqi5_Jn5B7gzkmxp5Pl0MurLtGB1e--X-Y4xvLbKjjaBBCsqcOLrRu2zPEoFSIT6MbAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=OtoCKRbhoBoLPmR1f7j2LCukFs-XFoc3veRuC6UKxesea0S4C-4A5Jp7vlprHs7enIMtlxXrE5jRK4HrEbo0mRNLTEj1F5FCDb2lMK6iILkH4bLn3KMBMIMk3qaG7aAyglPJ1SDDFUIMFttm8czNpSV0HSMsg6jhkw_auzmYXQX1JPh6VpYwG2aH7a0pGYogCJzFMFJFlSBphA2QPrR3KOIr5Y04XNH1yi8-0E_rOd9nZU0lga1odAEtgNOSLD9Q-QGr0fN4z9g_SRNDglXqi5_Jn5B7gzkmxp5Pl0MurLtGB1e--X-Y4xvLbKjjaBBCsqcOLrRu2zPEoFSIT6MbAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=ZJ3Xvs8V5czeKJkOH8uC5-Rv1a5c1oiX2bWXkRzztBBahFQgni8yIpfZM8k_rLRyGrAKtAtBiLyFDkYiQSpp9lgA6gTQYyX-DgF2y4qSBLdifu7AvFGqYQJH8Db2ROd32AEuHaqatgoz6-Y1ff-m21zPI7tCO_8DBBDJA3JDE_8n9ccis626i8yvPKfZ_whDUrZF_HOHMjHEPTKBFX-EDVrMYosXIq_V4HISEP39QrtZhZRNo5QFC3PFoe6JK0KSZK1YA7k0DeCBeP8xoKswPwu-OwUmplFJjmp5HEcR6XRuYA0PB_2qm8WJmT1F-ax3pI-jAhoaa3FAEV3ZfujgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=ZJ3Xvs8V5czeKJkOH8uC5-Rv1a5c1oiX2bWXkRzztBBahFQgni8yIpfZM8k_rLRyGrAKtAtBiLyFDkYiQSpp9lgA6gTQYyX-DgF2y4qSBLdifu7AvFGqYQJH8Db2ROd32AEuHaqatgoz6-Y1ff-m21zPI7tCO_8DBBDJA3JDE_8n9ccis626i8yvPKfZ_whDUrZF_HOHMjHEPTKBFX-EDVrMYosXIq_V4HISEP39QrtZhZRNo5QFC3PFoe6JK0KSZK1YA7k0DeCBeP8xoKswPwu-OwUmplFJjmp5HEcR6XRuYA0PB_2qm8WJmT1F-ax3pI-jAhoaa3FAEV3ZfujgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=AzGoERdBVncGoDK8kcPooZ6q3k8VpriI0KTaJFuYm_N8hitx_KWtG2kYxl8lruAKxBGSwnqY6Tn6MhiSVh7Zz9ygOTo-5TA2f59eOc62B3SzNP3xyXFKRtR1foBVeFN8DH0qOhrwfI5z3KyVmkNSUOD-Ne2Whld7ss8MG9XRL2RNrnwInoHbuEqbUJ3hZQRz0Dnrprx9eeqGKLm7m7c_rx_XGPVuNRL8GWyjw9bwpfzuES2o6rF0XFknZ2bdVOZ3Lw7vbUzs1eisRvQ0_HrXQs6sWBEnejd7_bGEPLBieOx-tLzQaCgN7mtwB4O_M_hC8PE_IeFb9Sqf7HL3Ynm5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=AzGoERdBVncGoDK8kcPooZ6q3k8VpriI0KTaJFuYm_N8hitx_KWtG2kYxl8lruAKxBGSwnqY6Tn6MhiSVh7Zz9ygOTo-5TA2f59eOc62B3SzNP3xyXFKRtR1foBVeFN8DH0qOhrwfI5z3KyVmkNSUOD-Ne2Whld7ss8MG9XRL2RNrnwInoHbuEqbUJ3hZQRz0Dnrprx9eeqGKLm7m7c_rx_XGPVuNRL8GWyjw9bwpfzuES2o6rF0XFknZ2bdVOZ3Lw7vbUzs1eisRvQ0_HrXQs6sWBEnejd7_bGEPLBieOx-tLzQaCgN7mtwB4O_M_hC8PE_IeFb9Sqf7HL3Ynm5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=flJ5pA29efft5HAvoIn0n0vNTl-E90m2XpRKv0VKEqIxiBsgnLepfg8JEEUZnIMtRxjMhMtJM59RMAOEXY_cFQjaUU1N6hkyUBiwjT85RFCZzHBQbjqG0IdAjELpf3kPpJ7JVeR8H7mbxn0_-AbiFJ4mJpib_h_2EppSrB3K0DQ37tvVPNE4B6jbWenVBdFiC8CYGMXRIXWSqbCvtBtgnzADuXezP-Gp3S49dGibSn_RX9Aay7HNjr_RsnUJGW4xtdXEdKOpC-4zvGlPHs2E2RSebWPWB-Uv1-3mPuid9D_qFY3OHIYBpYwEYCl2Bsb_ubisnqfVGpYJ1-kNjBn31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=flJ5pA29efft5HAvoIn0n0vNTl-E90m2XpRKv0VKEqIxiBsgnLepfg8JEEUZnIMtRxjMhMtJM59RMAOEXY_cFQjaUU1N6hkyUBiwjT85RFCZzHBQbjqG0IdAjELpf3kPpJ7JVeR8H7mbxn0_-AbiFJ4mJpib_h_2EppSrB3K0DQ37tvVPNE4B6jbWenVBdFiC8CYGMXRIXWSqbCvtBtgnzADuXezP-Gp3S49dGibSn_RX9Aay7HNjr_RsnUJGW4xtdXEdKOpC-4zvGlPHs2E2RSebWPWB-Uv1-3mPuid9D_qFY3OHIYBpYwEYCl2Bsb_ubisnqfVGpYJ1-kNjBn31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs-XK4K4YAawv_idYm_nSQwA6-HEVhqUZL4mEUouidXpUu-V44CWw4ueozAYP-jBuHI-zQL4qX3scC_aXtG3SwCheWc9d5TaNqJuA83EpUsvGaIfAMFwJcQxvD-ySQUlFP5K_9DUK9rfzgen0dXpXv-IDZtsfzeiY2z06lEPfZs5szY1Epow1vtIYgWNMYBGXrnJ5D_xos2PqqG8M-YT4tmIZWA-okKT0tVEd-btiQF-Cj0_Jec4AMKfc4e9RKzwrnA5XnYJKNyKHnIYGiZQdhLnw2aQZjsjXw91jpCLtxo6eY2-RhMQH0OxtOwgEPayvbFTZZ3S4ioIDdQGeJMIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAq6ifYHW-aMp4qYTNfeQ43GR0zsyvy5saZoUVSiFo8fG3MvZVpa78nZJ9olfNBSZBO31V36DwKr66kNRLH-_PCzK5lOFtQ36lJZn0LDht2Mid5_n_RGi3ufmeak45Vy9cAV3NpH_Uj2KzIxCrt1IIMJsqzpwVrbkXhTgImS77ez01bRccLNtkW73L-c8Nbw4MiQTyIwrrErv0nS5_7XfF78NystPAPI8ry1dHw5ig0rltabRaDFLisjYDYlYQCq9nJnehCwD636eAV3c8ajvrB-rCgF1_YGNMqcBYQZZPvW95C7AjgCPKQBAUDdhwNTw9Fcf7Ftpr-HEgbRn6DPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDS8csHKLKXa0hvVNxH58An4Nu9Ph_dimocvyy0BuajlCQCikkTFIX7eNdIieQInBfSEes970eLUBT4pp6LJZ3Jz4B09IkkYyXyPkaxE6-dB4FmX3xcg6EWn_oOQbZmY5nVhedDG3SxNrPcCGkaL-FYPUBvGLHM2tfan2Ij4624B0Dev8t2N9NUAUHhERoSdstXgxl5W3KTHAyylAewEJCIJFlgGZg1Hv6h3Pfidm3w9DjCqdiE-M8iK91TZVFwrc6rNzaAJuPi2ceeEwyda3s5AR7ZsDE7TwRuIZXUEUkqR6ZEE1xYDzSvvEiJBpMcN9Y3nFN69PdBONou6zxZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXafd_ccREJ_sZLo_GTngE7_XMMhvR6dTTpQhQxHhDa5wa1zS3rOCUnGITukqC2nVAZvfL4UwYEJDSCPaUH8M01Ya0vi6tGXWwSuz7tLC-6g6dKaBTRbV7B1paiF2XFLgowVCLdlAMyiauaaZAYlM4zlUltqgey_uhG27aKl464h3Wki34SLWxwhPypVDDgUY60TBoobY2gvqgbk2YL1bLIC7ra1sxKCde4UODmKAB9Rne0klTMgxXImLQd22SbsEuSSsVyZHMEEQIi5JNCFinxNJn1ajZTrFNILgslXmWC4kczhf6Vjre4v8011_C7vxoJWL8eLwjZOb6_n7OxvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWRIzRdNrRw4G5D7xWZoj-j5fuRBKTUJwjGcgkX_sPdvJS5h0S4qbHEtDKlje44p1IrrozAEgg5LYrohgrxhmafAKGb96LI2VIMJ5dibFesh73bbwUWzlkNval2rpNcOZi8juDHnI-27ZkLr5PmLFZuJ2s3QjgMTKXUAxUm6SBgrxlREyV9f5KyNfncyvfNXJYibnd5nd1qld6XVfxSaBNoC40dtwnuS-2K18ePI8sfDXdhM-xoSdxY55aK3i2GXyaxt0zqlbTud5fiyOLjTRB1YS3q2SfNJsOQFhcvL-LZAG6EgF-OjC99cpLgcpvHkuknI_wCL7s-40wMEN-6o3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUa-KqOt0dYcNzWafvXLGP1fPt5Ysreg_zx584RadsEYu6o0dzaZQO3izXlvROb9kQmhYCDEq0A4s0WKa0q0H-JxBrlv_8sy2uTMzC25NC1ezwkMUH4Ztfl8PeXcBM2frg4J4jJh7yiv_e_UsoLqgyhRL6OIv3iXp3ntP72VG7TFkJ19KyA8J0qk_mncu1Uw1g6Lc8wLJ2RFRuECpiNFbMlYibstjttB6Bk24V87zyFoiwcx76t_urESJ20wn26UTNFeFIqmK2ig4syEnGKIeCBnVL4cpEQ6CgKXqp4ABb57F6tyMfrBjHduavpwx6Qja21UM2eBhma__RbLymWjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIt5URff70xGs9s48cHqNRwy4Qx_ZWrJzbgJPRFSoAk_l5zrVSJDmtEmpLgCfQ3xHcZ5IOu17TeQ3xisjqp9UOp0KYLJcnqYmUDvw-3vLF3VQCoBtl4YYUIMHgKO195x77gWy6hUG95U1cfz1mrZ9Jk0DU6qX4cDamWaXi8ae84bb0c0kphddSpJBlKUoL6ieiWk8NijbKUXT6gXoe51FQWVEDRQmED7lutS0s8iS8oHfwr-tIpHCUM45zvwpSLI0Mid8yrIuOTX_g5x0AbDDdVpwtPTQcl1LsKvNlQxx0BtnFWArD5pQ-8g_8jQAfVGYIk8HDNF1MCoj8zFOqUZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIgV30k-xyM9cV8itiIdzJOny3byJach_PbZmAQrhlsPY_mOwARtqiRQjz2-ensoi-XOWow3gdZQxB8fNmv4cL6CjTUE4tNlsvL7oyP_Bopwwh8P6S5uPaU_cgohNhGvhAKVVloK09uWre0xkCGtAuKfLqALRc3ULOXRxIrNst6OXyYq1LB1v9fJxQn-M4j2rLijeYnKLy4HB0P9wUo_Wh3jWsmHB-vgbdPhhIqnx0pqFR3iEqGHe1KCqchhwCAOEO9ykIid-ZaG0WLg8XI6BEkdIOSwvx_nzE431U_ZWrqAEU4AOAVsOjFWyg12OAniHr53RVO2B4FhWhplrUJFvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX_kwK-oj2mVC1aKTLlQKnmSi2-Uyg7v5d06alhS2n6eHtVlwzdC8ljx9W0mN2jzP3c20aeVW5brcHEfEEDxyRrq6mq-OadOfoQ4AuJaTOfd3pFGYQvPvLP0-w0RWqEuABUaLs-u-Pp04saBhJbxrktsDTpEyILMXWdivW7QuFeUEckMPlic-dSDpOjPOkFD06mL5aO8UtGXdlX1Iqxby0XLb5JKBhlAclkK1nWA3taOrnJlimtSFvG9fuTT1Gc0uNNi9Si9uPjEcg9915RgmYS3R1h-QQFVza_BSeoVJUtCRIfSNMfJT5fzQ-sIMvYaIHckGhc4izhqB06-KwpWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0Tt3H8zm9HOUNjLbbgiswLsintFN53aRBIf-ToAbe3aKfDeQBEHgc3BKAYizylVOp_RkPvF2kp6S434D2IrQL_t-BCsvb4LB-Qxx2IgEZHT_GtpPniaCUiDHqXixTu1KmzyDlHIhj1xH0qfcAiC6yhZQTWQhBQn042BB67pDEL9N-tIMEBqVVA-BorCSW3Rul1jgg7n_A_tvocVa-9VGHRvIOYyZQa9jFC3QpoLRwXaKtDLtxnClTEckB7MN5ZlPQNvGDQsj6wbuDpzPzIW9_JYPW2o-A4aq0skg19T06xo4STY2C4Oy7AtO2mWUb1cD00kIF3uQ38qVmKuozsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uynBLXELqWnXI-i8Zs2NZokF472D2h4erBT6LZQZkt6bYg7niglxMEAzkmd4KzO3jQthDx0bCeNymt5wfrR9wyiPF73lGQcEEBdci5chGyZFB5j4IShpCLX2jTE0SgjSeBF4pvSmqkp9zW7M1JqUoymjGjhzOWlgsLNae0VTX8ixQlXIakSqjsnOC7HTLOEKO0HnISqUR1Q-huNRaSQTElT09E-ZjY63RMO55fQtgX1j-toJpu0sTN9bOXhWWCS6i5aaDC_JvYs_Xgpfs2pLfIf3c4nrkcQGKVr-UrwV_aeP01R3DhBPu2oPSYJhZjHTLR3rkJB7NnDr0fsHL1_anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh5YzxgS3onHtMN_dKrbAklsziXRrjoylcPV_cg4rnUjYWSbazgYVrEwYj_bpKQhpXo8u8K1m9DNPmM4GhG7rOdEJftqZbNqFg_WR1ruKSpSd8NI9XTFlVdXPFmSIC3rf0e-UsfJv9XhduzMQe_YWOOfxyQ84yKO5uLlb9lb9quAJqsmrAKfuSGKlnEW4ODvPgZeZL2q5fv5kZ7E8Yw1ZH67qm6aMj8ZB51EJNimfPjmlrMHnkpNlJ9AY54swR4ohg9PDaWMm6zCrW1zp12JQZAQBLOPEhaJWyt5l4qH-ip9E3E2O9zjQIKnKV1pFHDwHgFIByczXcKofju3luRvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=J9mINPjhiLiwOETnHqAQukIQ5QETeCQS2bpJWf8S59Qn-ifSpNw-AgRjktIyO9s-wlsC67cLeMohUUh6JjNDlOYGC43DtE07NbabH-bdn6NbTmICSy3Mzs7bZICMDA4RpCMWJx6fu1GiTN8kn9D04b2v6o8o_l8zKrWGNhtBD9_xdySW5UbUniieXs0TKulj_cOChwHZXShzaq5QRogtYI3gKbo0mkCYUV7gX2Fqz3Scil9NLC1A79LgjiydFvV1JnWTxc8q7phNCYv4PjmvfwJyjD6kQSkADc6n4cVipJM5ej2DIT_0xby9uz4HbDWa6jwa_jVhx6EFV358cCoFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=J9mINPjhiLiwOETnHqAQukIQ5QETeCQS2bpJWf8S59Qn-ifSpNw-AgRjktIyO9s-wlsC67cLeMohUUh6JjNDlOYGC43DtE07NbabH-bdn6NbTmICSy3Mzs7bZICMDA4RpCMWJx6fu1GiTN8kn9D04b2v6o8o_l8zKrWGNhtBD9_xdySW5UbUniieXs0TKulj_cOChwHZXShzaq5QRogtYI3gKbo0mkCYUV7gX2Fqz3Scil9NLC1A79LgjiydFvV1JnWTxc8q7phNCYv4PjmvfwJyjD6kQSkADc6n4cVipJM5ej2DIT_0xby9uz4HbDWa6jwa_jVhx6EFV358cCoFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4RWLLpGb31TmRGQNFodu2bXfaubPNRMA3bghMmsDzFZfZTIIQQbH9yjpF4GpvAdEi1Tz8mi48Wg1FIT_6HjzU0t3y0nt3qulAQVwIZJ8-qvRUIw_gPpIZskOH1h9UeCV1E677pFsLJbm9FFyq2Uwwgc8NL7JL8uuXJ3qhGZ_RUamwfFkeSvQ76P14uYeCXJzSZ_dWny-UcH5ZN0OVLv8-OumSxClnfyd8MK3uGTvM5GeeuoHc3XRW-PbLoD-sDp3uoGVDL4NwMIGmt2on4iUhgWRfzdLGVHI9y2UWEdn9jA2XTzhUQIhAU-L1OGy3eakg2IdIa1O9s6oXIVBBCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=llrFjhz_T8Zt6-fvixkWxSWojVoC_5QLhhamEoD8ZsqiGy8wcQlNiFTs4gu4ecMBZenp5cLQ7Rhd49GT-G811WGG75eLfQt8BQgTQic89_vWFZBsB6pK-bEKXL_BejdvmzDdYU7adfv5ElmGB3YgrlTzsKK4qEip9QwJIcGA9Qf56dpVV5NomEzzvANU9PV1wK9VPZ65nQigG-DFeMkoI8x5LGm5KlxNDBLPk5JT7c_-pLukyFffrSFhqyteIT0ipupK06uZOmohDRmaZJqvXsSsOsMvvbGeQb_seLLsBi3OV9p-yaA1K485o052MGR5ZJpnB4HjLzikGgbdyy9cSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=llrFjhz_T8Zt6-fvixkWxSWojVoC_5QLhhamEoD8ZsqiGy8wcQlNiFTs4gu4ecMBZenp5cLQ7Rhd49GT-G811WGG75eLfQt8BQgTQic89_vWFZBsB6pK-bEKXL_BejdvmzDdYU7adfv5ElmGB3YgrlTzsKK4qEip9QwJIcGA9Qf56dpVV5NomEzzvANU9PV1wK9VPZ65nQigG-DFeMkoI8x5LGm5KlxNDBLPk5JT7c_-pLukyFffrSFhqyteIT0ipupK06uZOmohDRmaZJqvXsSsOsMvvbGeQb_seLLsBi3OV9p-yaA1K485o052MGR5ZJpnB4HjLzikGgbdyy9cSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJARcLaUnlEjoIDiFdOpBXGn08rspk3FuqjvhxzehUMzgJQJgNXxLkOAVXbPMDbU-mgthfdJAf918_TfHV4UhAINZzGA8GtNuCOA93RxalAJZwZLnoh20A_XOi7_J9lrAbbH9xddwFW53Evj8AEQI8EtFQ12wwvF_mT7lf46CS_3tI6NLlri7RrTq_NpBR2NqgYysgYXJDw9RE6YLItMVWewR1T_gCuD612II5VXQs5TtQ90fF9bMhG-RVYACvfRvYupmFu1WXhS29bCoVu9vP6DRmngVJ43WfpErM65TFIqPC949gMTJdW4uuNffdLjjnsR1IvmwSm96uA1LzgipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2IWjXsFW-LntxEJkpzrqgg6nq0UPmGneHdkO4787AY6LdKwdJaM4rG5eFSliBDkN_OJq8Kc3UCu461-bDBvwvMGO78BpjpVSMXlzSysy-rddNEI7mThGPXCzjW7-VK4LFI7Cu68xMLTR9Cppb_54o-eN6xVVjqctwWLuEOSe7evsDMGsyiPE3vnV8J7WIi8A8w5ofs5Ob8NEWv9YBC1zKxmksbV2S4pQxUQbAcUrYbGDcNYjG5a4_fh2AIKM6Z85mQKM96rQvashYxen16FmaCvwuWK8yTrfLN_DxlwVidFoSsEDaaLz_E5l-TdOdEXXAU7Ib7kVs3wTmNbyRkToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUVPYGHIQ4w7hVauRSR4Rzkbq2keZWLGYwdTHo1DA1TCECRvq2keKtJ8sOKJ5Fjtuuuo9p7ret0gIc-oboagaMMXvKdyZqoUF-XXhVVjCpzvQeSbm5uz5sTvacKf4uDWwvO0C_nhhU8qRylOPGrGCmdNsriIVvL93ZrGpUNddcMJQ7CL65b7G9vN3hlLZhnGBp1hAIFcAulfR2IBv7qZPEGV4vH8NoVgUTcfJLszf6upzqgyNNr-wHfLPdIW0EycyT4mcNlnEKMOEGpBPHPwtSbcp_4TANr1qdSQZP2ALDh0Rx0Q276W1IhO_sUv7fJHN8_8U_yqWIhikwZjMnrHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUmHLV2EcvVw4GyLAAlMtEglH0l8hlPxEx2shD6UPObFoAMoJaR-MCOd99alqbWNHK0WNl0M-r4EYNANtNcdI2KQlLxrw4l1Sbg-78FrzLXGnRUErcRgRL6GIKmGX0xuo7sBnBRE2uHcsTC2-e8p2y_1vydKgPWYwWt0SAEKwrH_hI-HUScy91mpa0Oqj8l87CZG10Ad-fkZM7U0FUJ9r0LewEN7RBuQz3QOWILpcSWMxWryTCJI5VgUFKS3ouDbqU_c6sguJT8GNvqNkN-f9-Yj2a1weWT3GyPkAKyKdZHmsdn2R_hiOvRC-Ov21OL5X1ghVkc12MoeR_70V9xH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=VQnmDqX77zziUHCyf3PWXlJftuXhKJ0EMvjiiiWxVS2Yzm-yuoxhDOC7akpNsobImj7OBQi9YCcl9tuPuyCxXhNIThKxTdqphcZvNmMFPW4GknLzObVbJGW2_EYQs-29ip90vvEbTx2VRxzlzR5h3fNDJShLh5ULWO2k6p6heYXbm_B72UI2Mp0lIA6dl_UOKE7f7IZjqHxIhZjJhgQ3dhIRoSozD83TM4HyN3QumxA6Qw8qClXNVydmz1m8TB9L-wpqZInhz8_Ng4b_FoYYafmbbopT-RmAwWMClahOcG4SsyfebZbLSpY1utc2h_U23C3RY0B2MnKLFAKRFiS3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=VQnmDqX77zziUHCyf3PWXlJftuXhKJ0EMvjiiiWxVS2Yzm-yuoxhDOC7akpNsobImj7OBQi9YCcl9tuPuyCxXhNIThKxTdqphcZvNmMFPW4GknLzObVbJGW2_EYQs-29ip90vvEbTx2VRxzlzR5h3fNDJShLh5ULWO2k6p6heYXbm_B72UI2Mp0lIA6dl_UOKE7f7IZjqHxIhZjJhgQ3dhIRoSozD83TM4HyN3QumxA6Qw8qClXNVydmz1m8TB9L-wpqZInhz8_Ng4b_FoYYafmbbopT-RmAwWMClahOcG4SsyfebZbLSpY1utc2h_U23C3RY0B2MnKLFAKRFiS3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_aD52A1RWJCWPCIzvNUeUl1X6dBNehbwm3h91LBv02tpypoKe0waCkMASb_tPbI8DCrls_y1PBK7fze4R1hjrKRh3tO3FwUGZrkjHsDzkXi_CkS86OvfHK9vj_09_45JcYByfyYpnmvGpDaxG-JL9q_17sWNv-LAxVD4hfBwJCp9yfxS3Z4d-KW7eqKarrD0TyF5ONGxWjtCicRBVphRpZIC5c8_AwZX583MuySkgWM-WC4jl3n795ctMmutoIjKXFviEccj_PBTO4quzCWq4cVqEpj_uYW8w6UCy4SiM5S3y7xEztCeJHwSF2f71-FDTWgKShj4HLVduomKNavyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il6aZLmohs-xGehBLO7hNecC70vorNS97oGU7RIPsQFg7QpUxE3Y-k86RjgS0dSNIjFtgLz1bbLxWu7EJyTavzcIyaw98sLPmyIKBdC7Gayl_SxzCXxW3HbBAjDpnGQ7eXUSL3348mUORXgqczZjjLe5XOIruj8V2yvBYoolmVYl1SLt02TMoRFPyQ5tArJuBoXVk7IlER5sAgNkJNDxQs0kX2Kt2ksnDUjb0pfDg3fyRhpMHr2zqDsGQ3bbHoYuw0oJpLXrAMxKvPcJ0YtgzwzVlnFm2LuNpOS5Hc4aNvx1Y9wZiDAYzVsqPeTw6xWaq1-1NthJrB3HEcelfjWvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZfbZw57_BlNj6Jb2w2AQqo2HKLyAIqPm99NUzewZ085noutXI_VbhF3NyNCRXV3KZCFYl7gtTJ6dpUhFN_l5NlaPHnp_6Av_L0PugK1rxzIF-iKwgX4yYVl85K07SVixDLWiqCWRXi3MC5q-ckDSuG3OjtAu2WmUcCdubX3tsBN4O4kUiCgPmeQl_HjA4FXSWmnGRvUww-XcIGerwgeaUAefBRYV-WE7B7GeHYLOBxFtDaSRRYNoNzt1v42MjiFp2u0TR6pKgCnCrFPWCxtOQQ_7aaHzecdfiLD5gk9ISttqF-eObinYXFX-xyAHbMxx-uyVXA_qCJRjqbFIIJj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkWbl5jdZJuboj42L55BPttoKE4dwhJBY59370YkeXeefqx2wBDPU-L2vs3llrrZWrAYlJd2WvcR-FYFC-CQkHIueq6ApPk-CYcmgpL3XqIVa9Alm_YATn7of9cwSkRZGcSnsxfgEsmJ4uongzqMcLI7iK-UbTs5zN2SQZMgtKqFsf0xC-BHfAOdYddjed3M1ViwaFYeLtBH7pJuvFgLyKnGpm_g_DnUhjooEBcenQmWjrKsJLzi7qWDGf1m-zoKUCmpAvTXPDIC1RZ8-1JAnG2HGp5ReotHIFwJPEfjLBLHtOrKG1r9AlMxlf_AxZQRs4fcIYonxgr8OXIPipAtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvTqStj05KxS-RcOgzEJ5jT2jweBBqEN74x2yRhqlTS8ElwXvDBGiKcEv9WfGpxYavnAPZe4QphUXWptqDaAYq_k37BYXJOTx4dq05ZkBSmBHmb5oYizGPlGdmAB-vjfgDte8caw9B-SKZ_t2OB5zttq2rilBkVOke8ZQ98756ujroN92w85DVD_Ppa-symM2_xwIkL2p-gC9EkXaTyHyFkd9IFV9jLPHyR6R3fC6Y-SDSYvcmhf6rzjE9TK7wvWc1NJjRZpKfeh17OdoMWqXMP_YRiz3njx6ACDdv1dx4PIXt3nqE4N1XTJIp5OAKswTihk2Z3WAgN2RGgjV9zgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrKDxsWWWHX85OlCQx-yVAPkveND44ljazWrtNAEZcLOsTDxWuzoPbSsHSrfwpnFbc3mo1LDBbDKmN39HlflTym71xLhzhIOhB0sS-W3YTSQ2a_Wv8abBBdSca6bowhErx66Ewj_5Z7pxjXHqikLvrzYAnMD4k_qUke6nbTMFEoKcF1DcgWOskBuHrkSil8mBEajEYg6pN_bKro7E6tBVMY_hZtXN-UoYKtwRlMDgTrkhmv9_f1HEoQJkGdEaIBuM84xIhV1FxuUdmIpBXY19CMCMlkEYEt_L7jmfpeAD7FKaICbRHMW6I0X1Quo5U278WuQj7BXEaFh7YvifOj5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVxRtbi9si_NFk4dOrWiH_n4XLZ337iyBIS3hRrbOzicKbUbkzeZNoJVcQI5UUkJx6oT5p2F8A6f0lRB2TfsrfekBEcJ3X0YcR905ZyKH683wS_LyIU0csksu7R7C3wrHZG8cO1x2OixQYS9cwQj97A4xfJ4x9cLSI2q9dSF-KvKOFHEATMnP8QzfNsWaPgVAqYW9K5TSuChVNSBrdtzXZuYyVptDQ6-rpQZX9sAMS6Q_L-Gn7r-1841xnviyk__9XxGXC9e1Pj_TbguiNZzmbxC2Bta8PG3B_dbsVIBq6GWDBDR2IBU5atV2zF5OVPb-HlIP4njDF6r9RMVGXEfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlEbi42_aPn2v3Q9RFHRrS_rLPI_rX6niFP_BKFbaqtbqGveJFvUg01XoJXxn2KdkeFwEaL59rqEmxjQBrFpSyignYPzNppXsywAhq6A_fa55E425B5Fwssd3kUtdjzO-wElHewpPfr42e2h5S5cQC2oCdpk9W4NCzpRFiwBwgL5NpgpOUepWPv8TLIn5K_QFJ2K9VtMyway9rfeWZRcwucA8YhuWwllRhLuqYKYiTj_N780ufspMlMiwSLUVciWNH22xgKW_wqbS-FKx2w8yj4L90hmbkkO5GbKV1L4GJYBtmwZuChHZ3MYcxFOnGx1L9UZxAdXusjc8gW-N3GwkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reRcsAOOdaa_pNwRI_ajKT-5vaG5SqI5hDyqORKoyV86M7oo06IsIYAKXEE98TN_z7pZ2wUsiSFuUW__884txygZ5BeMtp_ZU0UxCFBXtJy3G7ajQ3tsp2smE32tK3YU2MhImcJ5byHTh-G_dNh07udGBS2VvaNrHg6Ko7sUTGG7KfLonTxUQF6xUR8R9B8X04MAm-oQALmmIwdB3S_aopbNDlpkCPOngmp6WthpPW71Aa-jzYsfm5QbAi1x-IMeq4W-emzE2MFgoGWIIIzWgHk0DGSRk9dblWHlIO_tsL-osW88357zi6Li48ILfPU6YcMAjCEKO9_h81D6s0Igiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZ6A7MF16djfrVMlpKaiIYsNzW9CxVTpzpIUob0ThODR7dSseUnvH5_IHnFOhkDAPAUa4BLjTb-pw20haLdmTl2F0j6NTxdDVZWdfzgjCw77N48B7Hx4AR-J-5fQSGHs_H_hbSKfA3vKoN6Rrgd82X0nFfNadToqQ57RAlecyFNEJ-Lg8ZoOpxRbz01jF4QA0J1823gjhbYesCyjVZgKstY54I1p7WTwK0l96KzWhmHxCkgraTXvQipmjr30QGeOuONru_8iEX1GadsifTyzU5E2VO-gCLHMFKpZUF3X7dnpwV4rpsCQvFm6U-6OY_xZqfDAt88cn08P10f892MNsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=aLiieungxNlG_m58Ap60YWpIxY4PvpD0_gQTfBZrZGhll5iQR6XKmG-3A--kCehRIV8covKtYH8sXU4LcWkSCzwTzDeXZimfLBV7en6ZeiltAKysXby5JeeYiarU7YG3_wkQBiqzbb-pCnGboFS-00k0syj4UNo_xtT3cx52F5C8VJhHzoB_ataTQNbvKQ0cLOGbtOVSt9Oo47sC8ixPGX9VDUwl9kg_aEa-2r_iyz2wfQ6muaMQ6Y1pqEb7CUhTEYraH8UjGj_iEn6_SSxyvhrYREyzIZAUxDInseKg2TGUdpCquUvkR5vHLhgZGqMnuqyp9UoVgD4ix7tFkTxjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=aLiieungxNlG_m58Ap60YWpIxY4PvpD0_gQTfBZrZGhll5iQR6XKmG-3A--kCehRIV8covKtYH8sXU4LcWkSCzwTzDeXZimfLBV7en6ZeiltAKysXby5JeeYiarU7YG3_wkQBiqzbb-pCnGboFS-00k0syj4UNo_xtT3cx52F5C8VJhHzoB_ataTQNbvKQ0cLOGbtOVSt9Oo47sC8ixPGX9VDUwl9kg_aEa-2r_iyz2wfQ6muaMQ6Y1pqEb7CUhTEYraH8UjGj_iEn6_SSxyvhrYREyzIZAUxDInseKg2TGUdpCquUvkR5vHLhgZGqMnuqyp9UoVgD4ix7tFkTxjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=QhfVB4aYx37GRsbVYV5oKg3MwxvlqKV6c6gp111dj_PynJ0fTY0bEA61iGyq8mtaMk9J7s7raZZECYEHctgWRoXp7jVXKWTYyvtM1DRC4ugV84RUw2kR-KXUn2UvnQABtc0Gas4k8lYPL3m730duwFMOuCiA5GQcQ3TKDZaU42MuWtWJ8sy5tDmrB07mI_MSkMn5gnhFoHAs8yvB9NZ8q9lUGDBiJ_IiSSNqo640weKY1Zy414eOxkPKpcnzwSQHXnnC4BmfMmY8zP3eV1xh8VpmUq7JLJBTDeSLq5G8O_9PXNVzCyEFwZTXnkQ9de4HsTJQ_4SYgUziPyqI6NcLh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=QhfVB4aYx37GRsbVYV5oKg3MwxvlqKV6c6gp111dj_PynJ0fTY0bEA61iGyq8mtaMk9J7s7raZZECYEHctgWRoXp7jVXKWTYyvtM1DRC4ugV84RUw2kR-KXUn2UvnQABtc0Gas4k8lYPL3m730duwFMOuCiA5GQcQ3TKDZaU42MuWtWJ8sy5tDmrB07mI_MSkMn5gnhFoHAs8yvB9NZ8q9lUGDBiJ_IiSSNqo640weKY1Zy414eOxkPKpcnzwSQHXnnC4BmfMmY8zP3eV1xh8VpmUq7JLJBTDeSLq5G8O_9PXNVzCyEFwZTXnkQ9de4HsTJQ_4SYgUziPyqI6NcLh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAOJUgKC6Xl2-ObJLGy056YFZMJksk0ZI4RfjoV9U_7xIageYIbPUdsOUvDnebuEIDqPkTB2Yp9l2zA-AZSvF2TE9G39N62-K_W5BPp0-Fb3FYBWfkNzt_9hh_Opj5S8rTo9kOcZlJyVm0PrO6o1PpqZP06moJXh1BRN3Oa1_OPPAO1I31otBv1Mx3vuwduJ-gR-A2bAd6S3xNtsOdYCN06-e1lFahvz9szTsWULRoAAEVSTfoORisCHnvQ0NUaDlWyPYjl7Yc1LgaNkXbATMX86CrWFijdvchPk02NWhRb8l_LaxdWmHlhzpbxtUTRfrK0F31ZaW3wLpn1b_LBzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knUD8WGxykE8LXCicACGaNamSW1dqK_hkIIaQtI64f7Il2X_3n1B0aJNGtBZbyISLodDf7BbbhGzXWFhjRgQfh3PYv4txweOIX3eG_rWrf10WuLP9kpGRdeJc1KLaelLElOvLjkHXniwl4apxDQNtCXl9T6x0HUwPFvyL1vbYrQTtWRCXBU6DI7_pt5f_p1NIW-NTwR3tesQ-M9eDXK2PfEzTqCAzET5Cs6cQUgTwzzbABBwjQZUNWwFXA_sBjjZcCRh8T6HvwvNaVvgociNz_ptxr5xMj_qY1_YSZ3L8GfJrhOeWi-RlD1YsAtw3pv1CS0vMmD0jRzI-zJBhtl7bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkWnHE-Az0eqh6ERnAqnzYwQ-yMUYsdNP2IkPeLxQ9da8wsCTZRyWAXvzKgkXPxy9XinB5w8yxBWxUyLav_KrBR-vM5fWcQ-V2-IBV63ao0y1vxrhRhTvuN_xA9LDetygCm39LJI6YZLa9t7Eba_KYwSW9KrNAjUcl9uFb5l4yYfcO-YfPeOv7rHT2yXQJoRUZnimhoGqveuYlpyKX0D7qA78SL6ol4EfQwTiy620s_iAxXJt_T9-9hLnjcmaVKl-rAucFx8zXXx6D-SwITYEe9wVIeO46CRRfdL0T2EQ47FYYNI6cYptEZHXyo2oJbCAidPAaJ_YpmgjpCZiQhw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lbSiTvEKB0ObJjwcLEjNKQLmBzea8Z5Ltnx8A_PyUJu_xwTmibujn7H4V_RIyEKR2_qeQHnicc7EXBdxtSaKurmU2sZsAtGdDYIINhTx6bBcv5r9BWXrO6alb_D6CoBqWtN8X4L1FqOojr3Uq17m60LkTz5U1tDVvsOART2vtWJnoT_Pa5SyvHteBkTRtrFdXNLvPwzwDbmmAPs_NoV3nNQLeKlfa9DhbEUfTr4uiNLA8trJ1k9l-khd7OFk6kDTTRxI5KIsc4L3X9bbXpN9kfrSOk2eYKW6BorXobAyy7lYG6KDcmx_j0djI_9EqsmnSPTkoTNeAzt4YW71Kf5gKeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lbSiTvEKB0ObJjwcLEjNKQLmBzea8Z5Ltnx8A_PyUJu_xwTmibujn7H4V_RIyEKR2_qeQHnicc7EXBdxtSaKurmU2sZsAtGdDYIINhTx6bBcv5r9BWXrO6alb_D6CoBqWtN8X4L1FqOojr3Uq17m60LkTz5U1tDVvsOART2vtWJnoT_Pa5SyvHteBkTRtrFdXNLvPwzwDbmmAPs_NoV3nNQLeKlfa9DhbEUfTr4uiNLA8trJ1k9l-khd7OFk6kDTTRxI5KIsc4L3X9bbXpN9kfrSOk2eYKW6BorXobAyy7lYG6KDcmx_j0djI_9EqsmnSPTkoTNeAzt4YW71Kf5gKeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Ds9tlhC_DMP2jWRCqIGc4TtDtoLzYcXKz2-WmYKXUIJsNireNTvtglURRMtnDHmILpKHfp0U-ZDhw2UQLDuBK4nFo0LXiUc51nD49ibsb7M5hiuvvSlBdXHj2QMNszQDZl8dC3TfUJBdikQk0hwk1aKpmiwTzVJVe92iX6w8ojwlMsxzxPK-Yi5slSUmMPvHDhS3zPwZczSazxy8Ns0DWRtjK3hbjw91nqhVsTPbbx1Lb-9qY-NR8pfsqrdal1H3F-Yf8zXgmSOuebAvr9Lm5Vx8ohXCvWYccGKPZDt8aPgJwRq9U3Sd2rN70pkeeRkP0JxNYT57nqHKM7RHRSspsXFyCwGoJpmCit0SsfkRcXyaI5Cy-BgvkCRmjvVlu_gkdZD8eGfvKj1km2NqeBdqLr8YASgE0a5YlAVeTq4YKRE3ziky1facsh1ku_OWxicYsF2ULvlkz_MV8aQAB8kc2Rq6VlRFahVqDKRWlS3tdc9i6C2nPKOH1ckUrQAtLCKP2bNjN7UEHy4TW8P-ZJR56BtV2rbzoTLFXQl9zTuSc0OsG290lOav5_OmFg7zYybkvCR8JEnfNBGeChc5-LBoycTrMieYoN5z-ahLo0cSUXQxMuCau9BtqQlFxV8eBrbhVfxBuCAJWVBuOzS9yfkfuDFxV18yRIkXxfMVTjLsXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Ds9tlhC_DMP2jWRCqIGc4TtDtoLzYcXKz2-WmYKXUIJsNireNTvtglURRMtnDHmILpKHfp0U-ZDhw2UQLDuBK4nFo0LXiUc51nD49ibsb7M5hiuvvSlBdXHj2QMNszQDZl8dC3TfUJBdikQk0hwk1aKpmiwTzVJVe92iX6w8ojwlMsxzxPK-Yi5slSUmMPvHDhS3zPwZczSazxy8Ns0DWRtjK3hbjw91nqhVsTPbbx1Lb-9qY-NR8pfsqrdal1H3F-Yf8zXgmSOuebAvr9Lm5Vx8ohXCvWYccGKPZDt8aPgJwRq9U3Sd2rN70pkeeRkP0JxNYT57nqHKM7RHRSspsXFyCwGoJpmCit0SsfkRcXyaI5Cy-BgvkCRmjvVlu_gkdZD8eGfvKj1km2NqeBdqLr8YASgE0a5YlAVeTq4YKRE3ziky1facsh1ku_OWxicYsF2ULvlkz_MV8aQAB8kc2Rq6VlRFahVqDKRWlS3tdc9i6C2nPKOH1ckUrQAtLCKP2bNjN7UEHy4TW8P-ZJR56BtV2rbzoTLFXQl9zTuSc0OsG290lOav5_OmFg7zYybkvCR8JEnfNBGeChc5-LBoycTrMieYoN5z-ahLo0cSUXQxMuCau9BtqQlFxV8eBrbhVfxBuCAJWVBuOzS9yfkfuDFxV18yRIkXxfMVTjLsXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGd4kvJ6Fl_fgL8pZgEGoejw5MnY4z0JspQAZznk9B76e_bZWJEcJToU9HKaxb3kmGzcJQh5eEGMyqiLFGGR0S9-tg_ryz1dBRoIgrKio3UxL4O7OwTRfDo8_WGzi_wCbABj5ATq6YwpAPJyLx_L4ZevStpTKaNB3sSm7oJKKyLg1ia-lHy__Q5jHkc1smxyLbQYWAePPD6JHF1wqgwPf7CSp_Y7g8UwpfYoy5HcU3oG7W5-q7Mm4IqOCCImkLuhjwj8lXDwG-RcBDpKa2TGa5qLYCf6mAKp4xD9QjRlq-sH8eacS2CNOMwIYGg_cJYp0BTa0nbE4Lan8bi8Owf6bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Udc5JNIMe_ipCIHORKRgroZcjh3ZHKo9JBBCTGx9BMqXXHfulueCNK4X0PPQCja91d68I4cXnnYXL-R_3rCANFt2UrvdRpjt2lVE4x5rVS0uyziZfhBfgCB8-1NdkQY3vTZh3QuFH5EKsthmpERnooCAhIb43GotOBEG7Ep9Yx305QI5r9ftksf_56TQEbS7QWV4EHum0f-Lmos2B8qFqMgOBR0X9cpkI0GvNcMR-ijTzQ6kX2p0D-0Fn286XnaBAyNOEV4zsBnM5ooMFO0xo_gC6LzxFIN2YWbS1kWMb023f296jDniB3wHoMfKqdkClmEW2tjwZYa3RbD58DgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3g3VXLzRgWJEPlAUQ3Zjhtctn_mnBSaUN-7v5uHv3Ht7BcdOsX3UzDyZybupLMT5HwqHO3dgaA_rw7qsAJRDMqsupJghGFUj-65ZR9FOiw3aO3AesaM8itCv0ZlX87afwLRJl9nZKNEBvpr3nJZFpVmsI4MKQNeOEdYtqP0W6Fp573Y99dg3Dr5bcc3-wXD2fKWKc6S20l_KjuMsloTnOET5wsvL5NZCNjK8y5L9Z5B23Q-9a8j4Modn786VTAKvSr5dtXvMLLsLDRuvsWkAv9KO4_4wPB-1dHhBlWm4DHeqXJ0KwACjgIDME6DsrKyq25azPiv8KWsCAtZ1g2GrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=lGr1DnLuiWiM-qrPoVi9PyO1DcyhnTiyW1Zj1Uy3jxkbSX9jorKiJ2Nbd60clzcRlpJiTfGwxE_DxlJdHwfF3pqvZvSG2S0x5Nf119lGWdEAOh5hiXIE6ZQVRJi021KYOFtORJ5KBD_NlnpT9pt_Cq_jBJWwLA91pDymRJTDrwlnZWT-JiT-T4RMzZG-P_xRzdhB_cpfNzuthXIYGKD3m38xz2vaJBGhbxE0hMa_CYjTh5n3fjOKnH7ITV_drRYk9Uc9C8jzykge1hwiaO0XnKjSIm8m7t6vUPJioAZgjuYFCJ-fkai79R87ukmAVCFfonES5tagVym1bcYYV2-Kvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=lGr1DnLuiWiM-qrPoVi9PyO1DcyhnTiyW1Zj1Uy3jxkbSX9jorKiJ2Nbd60clzcRlpJiTfGwxE_DxlJdHwfF3pqvZvSG2S0x5Nf119lGWdEAOh5hiXIE6ZQVRJi021KYOFtORJ5KBD_NlnpT9pt_Cq_jBJWwLA91pDymRJTDrwlnZWT-JiT-T4RMzZG-P_xRzdhB_cpfNzuthXIYGKD3m38xz2vaJBGhbxE0hMa_CYjTh5n3fjOKnH7ITV_drRYk9Uc9C8jzykge1hwiaO0XnKjSIm8m7t6vUPJioAZgjuYFCJ-fkai79R87ukmAVCFfonES5tagVym1bcYYV2-Kvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCPh9OKdg9AUr1fwpOwnT7yXdUdns_of4P4Zy7GQYrmm0EJxIAdYwXtN-gu7B7MBZMdIi6CYq17_wqZBIiwVRd0p0MYe44b43Q9uvgQtctnAHjPZvsvvmVsmjhAFE5v2ibVCjQypoTOy8YXjX0xGzdhVBg9mbdol-C3uGptow_o4I_Xsn38buL6KMeZxXv5STBhTDJf5C6xFyiK_sj-pUYIoK56GHx-SYtbPgF2Kbheqp3QDwreiyi6fPCdafpC8pqPFFumFkiUDPwo-IVpaO5wa-zgoRY50NUdTPa2FUpaGUwKDnSNKi18_szn7IwH5Ugzoahic-RwusxjwxQESpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=eDnGDIYZtDWJiIPT1NWTl9Pb2fzmJlh3HmS3-hxZ1Y7T_Kbk-bEeIt7zIDbKzi-VKUbu_M3afxTgBmIziOWTxd5attEh1tepF4_nEgUw69_k1BDcdPRb8zRa9K_hvw2lxtMkQNe6bui5isbaVXm9QQXx4yFpz1ZYs8ld5hRu216KXYspgLe6OfRLlyg1ZwM3vdMaQAjX_nmBjaW4_4qZ9IPlYSr-mCVvqaXVKnHT6kyIUQQai1SdKl2krB1Ovhfv_kC4XLm9I2aOLje3tp4f6PxWOvuV3fAnyNq5dWtb_HbjCupBZ5bPDd4xhJFXjxfKhu3oxhDcR4DTI2pothYTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=eDnGDIYZtDWJiIPT1NWTl9Pb2fzmJlh3HmS3-hxZ1Y7T_Kbk-bEeIt7zIDbKzi-VKUbu_M3afxTgBmIziOWTxd5attEh1tepF4_nEgUw69_k1BDcdPRb8zRa9K_hvw2lxtMkQNe6bui5isbaVXm9QQXx4yFpz1ZYs8ld5hRu216KXYspgLe6OfRLlyg1ZwM3vdMaQAjX_nmBjaW4_4qZ9IPlYSr-mCVvqaXVKnHT6kyIUQQai1SdKl2krB1Ovhfv_kC4XLm9I2aOLje3tp4f6PxWOvuV3fAnyNq5dWtb_HbjCupBZ5bPDd4xhJFXjxfKhu3oxhDcR4DTI2pothYTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyrx_8aTI12STqfWoJM9FIedRcPmFBZTJhbirJjQPj8Hg9MfKTCSdlciGP-58M60R48aWF5tiTb8TVdHor47FsgRIkw-vPXtyscfjUs-GlMtX7x6ToTWHyyUgERrrCk75HONo-tF8sX-lmb-ua4tew62Q0yhih8y8uK5H1nlmKRVjA1uTe6fgAj2I8oXJXeyc5hLfmYfE_E7cLTdI2zMK3hTzI9N-bKTSDMPGf86FAge_1n9IzdAPb-xlr_1ARUyJS2ow_AOCqKxPN9ofNe1AapibpPz3NHHtacQ3AHvynjVH1Jb_xAgfVvKeCxoFZTBNt3CWDgBhqmO6uzk78rh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJiNXuqacxCl03MKdxRPBXw0RkF7adwbXT_diETXnzJOgf6H1u4uq1rzWpraOK_1VK7txRp6Uafuj4I5fBFWE_PIzlqyiLM9Sbw1eBGNDMHl0fVVizp2cVgURLtYF-trUrwizKC_lDjmIu4pRrudQWlcmZGEU8PLesuFNVXVlP4Uhi5GRgpIbntjlKlhxABhO8NL4PdexgvWXUQfv5GXVp1YQfAwpn_ruyGczmTaq9gGkfrLCh36dvmamupnru8cOIUeSqtB2npwjSw5bQN_1RGcZghitFpRA_E0axCHmPpqFfv2KK5cl3UceDLvvsqV5CBVeX8iAbPZ5IAQNAxQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=uPOQpfEk23Aa01K4_9qFdGIjZHseQlu78ZQmREBACGytuDp1vYrisnbY6Q749rgMCIV7vT8LewGPgmm3e5kneV26rjCu9aJbuLnZ_4BLKKQfuipSRrzrKH7cVXu1nNVbp5ie8wjgQ2p1DdJOpj6xQ86EvZWDp8wTSeFJ-tXAlsTtChNHlEDyCL316PIlbJK3nqztp1uy9YlEqxQjl9yaPTd7tmXXniFVQDJ5nP6amNjcWmQOKvpUTyfvs2-cIlC4SM1YCGZszLm6ONScGYjeecsyPm6J30HlqnShwTaT0yisFCKvVV_ErLAcu5cr5G8CucEskRjRUET7mUfl-2ptwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=uPOQpfEk23Aa01K4_9qFdGIjZHseQlu78ZQmREBACGytuDp1vYrisnbY6Q749rgMCIV7vT8LewGPgmm3e5kneV26rjCu9aJbuLnZ_4BLKKQfuipSRrzrKH7cVXu1nNVbp5ie8wjgQ2p1DdJOpj6xQ86EvZWDp8wTSeFJ-tXAlsTtChNHlEDyCL316PIlbJK3nqztp1uy9YlEqxQjl9yaPTd7tmXXniFVQDJ5nP6amNjcWmQOKvpUTyfvs2-cIlC4SM1YCGZszLm6ONScGYjeecsyPm6J30HlqnShwTaT0yisFCKvVV_ErLAcu5cr5G8CucEskRjRUET7mUfl-2ptwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UlPyP_f4ouzxsC9QjC6wrq19dgZZcL7XZe-8Xqb-sQi7eR3-wii5e_GG5s9Qd7AOXYaRGe1N9MNtlIUIWKQEQpUM1BmuTv8fb3xqoxVEkqFmI7FNJ8C_-m1hJ2FnVFWqHHvkhWqBeZw_y39BSvG46H35sRXqfmRGOFxBGzAaLD4Zgh_6_NnwPcllsUTKqHVYJqFCCTYPNjaPGCER-4iEI4Cs7rSTyQMoNFUakNK43pYrt8hneKgjrSmzAiuBrQ3tNq25QMU1-9Y3W-48fhb4rAh-fiwnlcCTbtW6PiwKW2kyg6dmoYEzycPTcOjY0B6vcIe48P770grTVj1be1nefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UlPyP_f4ouzxsC9QjC6wrq19dgZZcL7XZe-8Xqb-sQi7eR3-wii5e_GG5s9Qd7AOXYaRGe1N9MNtlIUIWKQEQpUM1BmuTv8fb3xqoxVEkqFmI7FNJ8C_-m1hJ2FnVFWqHHvkhWqBeZw_y39BSvG46H35sRXqfmRGOFxBGzAaLD4Zgh_6_NnwPcllsUTKqHVYJqFCCTYPNjaPGCER-4iEI4Cs7rSTyQMoNFUakNK43pYrt8hneKgjrSmzAiuBrQ3tNq25QMU1-9Y3W-48fhb4rAh-fiwnlcCTbtW6PiwKW2kyg6dmoYEzycPTcOjY0B6vcIe48P770grTVj1be1nefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=DnFRPhVPKxHhoa_qKAwpE61iop6hh-QjpLxOD9586Pa1f4plfXQp3orvGaUEYJj5YTN0VljpMrzX_OiZNdocUvzeuBG2Bsc7RkWOldc1liXuS_zdJG6jyWN26_l4RFsy5sU6Wvi0ctOAbFMTagPA-Pktrepe7-Ziaxcvn-F0iLQvUDfUGBro-i_S2lvjoQdMva2BSkTw5b0jHP-pLSnyX197rCWztvhAxIT1m_t9HErkyVUWKk-ZBr4Y4KzJqcW-ejovFNsmRSEl2xtSgXxSsk9meGGopN-K3Ego1PxUMERaVALspjvBInLp7m85If7HX3k9coXVPKGNHEUs_HUGxI8ipkBXUS9Y9H2jXLv3TI4lxqLCQnzwtNKfouD6xPEIQCROx3pNPVBJHTa_EZuua6Ffw3JEoYT3KsDt_7o76c0nr76timLBxcS3DNrsX348QpBodtizZTmlE292aK126kNTsn3-VZ8O6MWxw_kKjPsVfgkx9noQuG4SfpU1H_NFVCgG3R4Nino5X_LDtEEpcMATABggS2VGTPIKe6E6XtmqZenvmM2MSjZ7T_8ouFo_jFJ_XfWnpUgBEQ21LlPgn5-PREJnDPWbJnTSkHfzc93CFCbpn3bOOe0lT3YK82xo4PCiFK1T5ih9In3vGGpoUA5eP58yMNVRAICKGe0_UjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=DnFRPhVPKxHhoa_qKAwpE61iop6hh-QjpLxOD9586Pa1f4plfXQp3orvGaUEYJj5YTN0VljpMrzX_OiZNdocUvzeuBG2Bsc7RkWOldc1liXuS_zdJG6jyWN26_l4RFsy5sU6Wvi0ctOAbFMTagPA-Pktrepe7-Ziaxcvn-F0iLQvUDfUGBro-i_S2lvjoQdMva2BSkTw5b0jHP-pLSnyX197rCWztvhAxIT1m_t9HErkyVUWKk-ZBr4Y4KzJqcW-ejovFNsmRSEl2xtSgXxSsk9meGGopN-K3Ego1PxUMERaVALspjvBInLp7m85If7HX3k9coXVPKGNHEUs_HUGxI8ipkBXUS9Y9H2jXLv3TI4lxqLCQnzwtNKfouD6xPEIQCROx3pNPVBJHTa_EZuua6Ffw3JEoYT3KsDt_7o76c0nr76timLBxcS3DNrsX348QpBodtizZTmlE292aK126kNTsn3-VZ8O6MWxw_kKjPsVfgkx9noQuG4SfpU1H_NFVCgG3R4Nino5X_LDtEEpcMATABggS2VGTPIKe6E6XtmqZenvmM2MSjZ7T_8ouFo_jFJ_XfWnpUgBEQ21LlPgn5-PREJnDPWbJnTSkHfzc93CFCbpn3bOOe0lT3YK82xo4PCiFK1T5ih9In3vGGpoUA5eP58yMNVRAICKGe0_UjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqH5Zk2am6-WRXFzlkUnA5YWgbcJA36GsKe1Ok7sRf2yNqsN8LBR85tFhQH51yUIvDUEB-fldnSpu12h-H-HeeLdDzzxJZ8uLzQf-vggdHgXBzE7sXslvkAtza6k1bQ9ZM1UE8KM2SvHkgHORK2ssq78pg1aoryXu3Ej4AjQOl138Qc4Xv-1qngRFeld1y9dSJUJc5_LomprPzQ-XXsv0whaJwSQAZXxWDV-HsLOpOzCt0JKWHOvv_woMc5vY81CvceGxWJoF5sEI3UY1XTJjCJ1-8boEbPJj21ys3rmIs-Zzbw_zZvcEUrGe0AzXcpZWlYVq1C_tSEjeneAPD7eEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
