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
<img src="https://cdn4.telesco.pe/file/Y3N9kcrxboJjhxYax6XGfhlmQepLgyWgx_UZYObj66yVGaVDmin3X7unHjOHsdYmxsXl0065g8564OMykK7iHHFZ1OKTK30tw0Bm2U4I_F_y49mmmnYkv2BV_QSjD6i1lLyBWUUD9bDE7-AGRQADfwaArgAK9BqlAfIpfkN0cPhDiM9wobXTYz_7-AMJgaBQXAzO8IHKusQDGgvUAAbGDxLy1ZHTQNOi4rTKvl1kIGHnNyUwR7eL5PhXPb5AxzWxlhZtjW1-VnyZcTqSuOYWMk8sSENgXGFQYmXg_lR-P9AdeiOeR2hnf_F2KTQ0ISHhFrIoKce1Gjw69AxUrFDe6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 21:59:09</div>
<hr>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmwPpVG61psAtQdwMHDeiVYAASq9Mi6tK3OXSI9ho5OTpAgLvBX8LpMbZgmBFPdCbGFMiT0Jb8dw6rUfe9iWWnlymXvftvCyK4vJuUiBdt8KbT2B3XHl3pc64mrEHOjo6r04Su0k_T3OR-KWaURUFZGBxGVwiUUBA5YWz64UV0eXJ5w-0xU2lqfyYLpYARO5J_I6xRWkmc6q7_VmR6nHucx8Kkp-VPeRQ8KyAfMhlXUyBPn1tJfvNSXUq_hp4G18t4DGRT55nULY7Ln5qKAs0iPsaBUWxTZNZFImlL41hQUjoj1ldVchxnjYPI7qTmeGdK_V43UI3UWK_sndc73k4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpdsq2fOFGZxYah_QBzHv1ejr8ZdyXBLr_CIwoN-u_sNUl4fL2a6Z70vmyaXrQ-yiO8SUqy-Ol9MWZOSdFG8dGxyujiz3mlUP6lBL9hXczW44ilonpBxvFNnY07VguKYGt8UDOAAESxtMewkNNC9HY1GzF8ZxpvCtQLxIVfcDdSpei7iRRDmXWpDg1CtzNSYzT86yE3nBDV0Vkzic5JZbzaybdK36SCoZzJplGai8YiQOnVksBdEQFTfOPlef2qJc9n0tWFIsedRtBn7hm6R00SDKzmGUknMCJAhPvqTLlx9LJgeqKaOWUIgQhgzBsGpMg2R2gNrycESweucsefUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCrCyluWT5t7TBl-8swQwSiu-_MnIH-86lRDrS3xrJDc6jbWzsgqoBlBtly3YhG0cA4yixBWW1QbM7gzpUBalWyky2UHv9k90632lNjBar35zQUF9TpTzy-dnssTXCmLyEolKKYQXdf7pKZG8QsSB_NdxEYsfJeN7YNS3tGPYFGcSh-GKwWSUy2AaYKKLOXKZSi3CcNN6kyttq7xQHOpwI4KSmnzX2W81jVOiZ9QHt9DL53rsrttMjme7dpCtRk-HYJrZVk493Nwi7j-ysVSzHZxxnxHpSAhg9zNKhvBezfmzA4tpHqL-oZWvkZuwFOzjLFB0OQcRuxlrSXQFbYJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS0R82oWZ_7rf481K9WB1kQ0r9PduUOUAEn1dfdbrhyh1Xsf7L49dY9plurOiAZTGm4ak__zLPH_7F2leRRv2cspGdmCwhMIrMjE3zwqQkADb_YQnKJc9MV8wdtRbBoxL8Nsa5l_LSmHVrEAekVBt-BrHXvEmb8UA93alOR2ihAhsRurKoEVNEdR3ouWzqLNPL7LeKIuzmK2XR-FPOBS4akkuMfrc7vsjm44k68dWBNqn19GzudcUcx52FripM7cpWGa8RVizWpeheN99gufGh9ibkqmpiK1LKSNkPsGyFPKIa6-KK2FC4cGsZ9nE4f8Tb-ppZyUD8uTZIRp1AXsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIc5ABrHhs6VsQM64JSIYwsUD0hOer6dfRgNTpRcaHTUMmwC5m-dt2GR8wjye69AOkAhqr7Mx1qtxacBh7qYdY3wvH2psylktOgoIU7EJaGfMiw2n0Ijfn9fuwvS4XgKHWS-cL-_KYeJI_BXKc6asWbDAUbCVbpj_mLwIsBuN-S57aY1I8hQEvZMuLHlV2QHDQ6N_BlK_YXa5vGddNm1GXd_zmAWk-rk988DgIi6JiHI-IfZiroLJQDrqycz6Bn1vDzSKW7QPINkQkd_iLYyoFKWSKvusZZg6-9UBYIpsrByX57R1H5QHxo1VDCjwi1w0Bs-ZOHYE8Lb4FpWX2xcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ9beUCwEbTtOeg9DSW2Tqiuokj7C5jaz6mokWpQhzpLdUAlGumSq6-PqoYg30yRz4kRVAKVj_u96d_EHE_zJNr7vF4vHkn0YisEMwp-Akdx8jUunAI83nLH_Gw3GwmxPnv4M1J7X8sqf-XMA7QrIRBCa3dhZnzIpiE6v2unqWfUFrJI8ohwSsmQkuE-nQ_uV11sIn1V_VxXvjzSO96PQBIgIWtkZO7jWEB84LsuP2Kv9seryFhC6ol7gGz9pXvRh_QkzF-Ucx5Nu2xqRWJxVCscC31-H1nZrg0ncPlM6T4SRzUgPVcjbF_BKhhNx6WyiNFjMDigyKEbYKctothaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr_ANOOK34TYghfd--lTORI-R5WvEbrdx1L8SRuldj7HN2DdnCz_fqKb2HfuHnYTlw6wqqnipJ7yeIjnj8Jk4vpnAqHA0si2lRxRfedw8PjJyTOsjLLlW5vwz-ok8-Bcc773ibHucQfI6fU_-1om_UmNFyyLt-GMV4lWSZBvwTh5Z7M0ev9ewBMXzOMbZlTdwp5d5qUpR1pi0fCaDUumouNUzy6wwnZpN0ozaRh_tDPcwr_fu0qQqTZIrcMV4l34IqdsMSOmRgEGM3b8VOO_LwjQo8EgMQLXJlVIX5ql1fLikUMf3KRJM6Zl7b17y_xy4NNZ5Bq9pQavMMxGqZBu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-klQo3qACxx1H13IAFWJ_8cjOTFe71sW-CUrkquYaWN2WIgsN-tlxbm-4hVj_4g9ppwwmwp1nuyX7vI7W7MKeOCdrSCbE5s1ceEiL9FYdQ91PAhY_Dp3K8OU4_EGJXrrdmvarVenqMAlvXYcAp-9UCJ8yQ4Qp3PXXQ-4CKjALLPyCDu-pNtvjlCo_Bt5IaaNIzF0ahHOIuQ0VYUrtBJKJv9sc4JUI0bMK-cnCSY3Vc8zPvC_9ks8amQxm4DSco3mkjBTGlh0rcOz3cKaLX0Rdm8SescFdCu9khNP6jT-G8cE5Sb1gHCNMNYicmviwonbGJrye9OEgPy50bUOIF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
Claude Fable 5.1 API
⚡️
20
میلیون توکن بدون محدودیت زمانی
✅
ویژگی‌های ویژه:
✅
تضمین
اصالت و پایداری ۱۰۰٪
✅
بدون
محدودیت زمانی (No Expiration)
✅
عالی برای
برنامه‌نویسی،
تحلیل متون و پرامپت‌های سنگین
‼️
قیمت: 12 دلار
💵
📌
سایر مدل‌های هوش مصنوعی ها(
🤖
🤖
⚡️
⚡️
⚡️
🤖
,...) با توکن دلخواه شما نیز موجود می‌باشد.
🛡
جهت مشاوره و خرید:
@Configvortex</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7641" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7640" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=CnFUNv8fkoH0VjJr3wh-bS3N4j0du4La874ytqMzuwg16flUOeCwNj9F1mcCIfHchTADFQp-fR1TGs4a-4KJsA8C2rPnrYt6sDe4aVw7Mffaex8xAOCFC6o04wAU-YW8ENlj6SH5LGx9bIIGyAUDsdeDdy_rGTDqZjv6Q2VmSgsIWWkpu08Lz1pieCbmSiA52oRz3ZQIuRjJbCcXk8Zpg_19a8KwvHe3QFXVmDk7EeFFz421qmbWXl8229UmiR5gpezsuVTkeSdLXWH98LKGFxwXlpqE387v5BFpWmnpPhB1q9xUp4Hf1B1hjed1HFsbhvMaihFn8qRcgfo0gqsIlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=CnFUNv8fkoH0VjJr3wh-bS3N4j0du4La874ytqMzuwg16flUOeCwNj9F1mcCIfHchTADFQp-fR1TGs4a-4KJsA8C2rPnrYt6sDe4aVw7Mffaex8xAOCFC6o04wAU-YW8ENlj6SH5LGx9bIIGyAUDsdeDdy_rGTDqZjv6Q2VmSgsIWWkpu08Lz1pieCbmSiA52oRz3ZQIuRjJbCcXk8Zpg_19a8KwvHe3QFXVmDk7EeFFz421qmbWXl8229UmiR5gpezsuVTkeSdLXWH98LKGFxwXlpqE387v5BFpWmnpPhB1q9xUp4Hf1B1hjed1HFsbhvMaihFn8qRcgfo0gqsIlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2SvA4bxe4A5KNkfg9v53Cf0bOWJVmdTttKzTrW3wQ4k-KAEryf7C9vo-QilCiquRvfMMt2ZgNTduN9X3ZLS8gkyc29lsujgxY8htmm7u1H1vuLq7LgA3su-YZeWbpEM8nC_vwYR29TVMt5720FMBX__IqcQRDIwHrcIpcueBRgVgUtuvWytHYvtWdrwTRBxoJ-_XjxykTDZmed14E2KY202nivvMyhuwLVy7pu76p_t7t3gSZcTSIvGHm1PmTlvXlBYxi4UokoPE-IU4KtAmqNJ-8XYhXHzuXOToD45guI3X85aiGVqVSisomiIHcaOgHjz5Am-y13dAn4LQ7y_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtf31SVIUF_skd-sIbjS_sc_mMj0vARByJ8iZTIdc4RLJUJ7q64iD5xkMbXQfPZXtQYzkkwm-RY8BRcKedfUlowxITAf8lV_BTEGebXO0-V4-ywLxGJinSfouwWPr26bNhyMqjsqyG07O0jv24IO7meXhrBrGe6_0HVN1-OJYTU6T24Px_EThqOu8ySs1gVlV415tEc_yPzGm91Wr2JT3WhNVqH0LoLzNa7tOO1rdxpwlyXnzNv2hFYslD1aNSO3MmieckU1-CxPdFlqZV3nlYRI_BOvP3ARAeCijXyM1EvMQElsVywdgrbL2dhbfSfuUZihIxmppSOUUc4PeQsOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=GZ2jb38D6Rmys2NOqaDvwS5kpoh1Apj67A8c062hNWIEroRtVwgqFHbGLuRH15WvTPf1vFJlht8j2XvYHGZLvecQ8UeRRdAHKyVinNKaDzRqY6GdflnLNPtV7jl4OUsxZ0lzXmGFORqmu2t_NcPGd5Vzl2z4Zp1chD9VOVueUQPULqVsWJnJIhb3gbTgSk7kNkx6a77lCMB_jGP2gq2Pd2yIibhN2vVYlSkT_S-eWhJMRprxdWnaKqMwYWX3O7nM8NKbBlxk7OGF-aOHlFa5vSO4JfSWKybPJMpy6CBEbcn5HRdXQr-27TaSc0nBgjy7LaNXbRBIBAf3Tmg6Ftw8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=GZ2jb38D6Rmys2NOqaDvwS5kpoh1Apj67A8c062hNWIEroRtVwgqFHbGLuRH15WvTPf1vFJlht8j2XvYHGZLvecQ8UeRRdAHKyVinNKaDzRqY6GdflnLNPtV7jl4OUsxZ0lzXmGFORqmu2t_NcPGd5Vzl2z4Zp1chD9VOVueUQPULqVsWJnJIhb3gbTgSk7kNkx6a77lCMB_jGP2gq2Pd2yIibhN2vVYlSkT_S-eWhJMRprxdWnaKqMwYWX3O7nM8NKbBlxk7OGF-aOHlFa5vSO4JfSWKybPJMpy6CBEbcn5HRdXQr-27TaSc0nBgjy7LaNXbRBIBAf3Tmg6Ftw8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=qEkjn_AHB3jBPpgwr1vYJJuE7KCZoZuws-DAuKKI9dC7pHZghgRzTV8QwJLq2MIFOro-eMAS6UikSqxxkaEpllWpwWeuQmyS71h_SrvsRhL4Aiw2KueHdDMO8g82DuPRiQYmJchSeAbndvi6DVHWDlVAeubHJMiQwiZrdDuWRQKFHmSF7tGnEIaNp5Y8PuqcdWjCFq87KvI0mSxMR4VrFCLkGJIEjJuE29FLzSw2GqCulfVk3jh_9Gat-fY3FJlFPC_20klBEa-hlGy3xFu0WwI6Nk2G68q0e7RxGonOFQ8AOP5oRzc1gM8ojOG4FNR0zHFRWmIRlqmfbXNFgxq9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=qEkjn_AHB3jBPpgwr1vYJJuE7KCZoZuws-DAuKKI9dC7pHZghgRzTV8QwJLq2MIFOro-eMAS6UikSqxxkaEpllWpwWeuQmyS71h_SrvsRhL4Aiw2KueHdDMO8g82DuPRiQYmJchSeAbndvi6DVHWDlVAeubHJMiQwiZrdDuWRQKFHmSF7tGnEIaNp5Y8PuqcdWjCFq87KvI0mSxMR4VrFCLkGJIEjJuE29FLzSw2GqCulfVk3jh_9Gat-fY3FJlFPC_20klBEa-hlGy3xFu0WwI6Nk2G68q0e7RxGonOFQ8AOP5oRzc1gM8ojOG4FNR0zHFRWmIRlqmfbXNFgxq9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=qzmnTA5uImGJwgZw1FYVnKfwI6FjjrYfijv_D3XhtlMJ-_UjeGx3Vpj0ZHmaUB5rHRbRU9Czdc5zGOEQuYAh4I1xiay87bnQk7LjGE71LDLfpaqH0UOwe03tzPFOGrbkj4r3fxJqIa74y-sq3sp7CFmZijuJb_ySwk2LkQtD6tmONF96I7BwjmgiKAv668v18g2qi0oeALRoEDKQovbG-hF8i9idPs8D4jyb_Tp08-FU4MwVAwm910ryrM6lIFZwPZjIdhsM7Eryj14mkJdaQulQZvEWp5KoIBtQhwfYmod8yjjx8vRmI1QWTh_15B1jMbs21m2biFNkymkNtzAyFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=qzmnTA5uImGJwgZw1FYVnKfwI6FjjrYfijv_D3XhtlMJ-_UjeGx3Vpj0ZHmaUB5rHRbRU9Czdc5zGOEQuYAh4I1xiay87bnQk7LjGE71LDLfpaqH0UOwe03tzPFOGrbkj4r3fxJqIa74y-sq3sp7CFmZijuJb_ySwk2LkQtD6tmONF96I7BwjmgiKAv668v18g2qi0oeALRoEDKQovbG-hF8i9idPs8D4jyb_Tp08-FU4MwVAwm910ryrM6lIFZwPZjIdhsM7Eryj14mkJdaQulQZvEWp5KoIBtQhwfYmod8yjjx8vRmI1QWTh_15B1jMbs21m2biFNkymkNtzAyFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhvu0oK7vd00sChNiVsLABpnWIJgQgv9nVqmmzALtRg9X4V4oVELJ5M4YQxd05N-GwDgpP4UBEdh9rno3XjbM2M36vbYPMDq8D9JVersYevecj3h9VIp_lb9A__SYe9MC4ToDeUkjEgk4uKijdd2jbPaDwfgGVm-MQ1H3wyx6nFGkAPszgsTldnhIUWHnTvJcFF4wp0M6aMb7q6oiiKNc0U9cPk9uAbES8Hb1hz5mlnMr3IRFnZAlDldLJnu5BfbeWbWAD4P8ObfChqE51MPeUh59OWGLdfme6igZCGcqlBT_g5iPeTqjQx4EmsN7y2h4DpOFs9Py0y0PHkYo52V7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=LIoIbUJGtsu0zmNND_9JSLr1lLT1RyFbzMYYG9q8IPAuuA8zPL_z_EvUv0CRWSOcvuRxzOhFmqbM6N2jIX_Wcd9wpt9k4X9a9DjHq-pqU5-V_6I7X3fUq2A0E1M2D60i5LluTpIifnN2060dPRh0xA3ZCYf2_VDZet3qojiaGqH28xkFkCbzMIEJwnZWY8C5FvU9rtwPZ_31Qo-_nAF8AVdpKe3EhF1piuounXq4D9EtoEKDGdc5HI1i_cH1FpFp1KHQApD0dJ9RdJY3vS0z_ag9OOq7dxpQuyQoxWP4zfQpgOq9kVycq5wIuIabsymL94wR86kuxjdHaDkUWKa0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=LIoIbUJGtsu0zmNND_9JSLr1lLT1RyFbzMYYG9q8IPAuuA8zPL_z_EvUv0CRWSOcvuRxzOhFmqbM6N2jIX_Wcd9wpt9k4X9a9DjHq-pqU5-V_6I7X3fUq2A0E1M2D60i5LluTpIifnN2060dPRh0xA3ZCYf2_VDZet3qojiaGqH28xkFkCbzMIEJwnZWY8C5FvU9rtwPZ_31Qo-_nAF8AVdpKe3EhF1piuounXq4D9EtoEKDGdc5HI1i_cH1FpFp1KHQApD0dJ9RdJY3vS0z_ag9OOq7dxpQuyQoxWP4zfQpgOq9kVycq5wIuIabsymL94wR86kuxjdHaDkUWKa0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbhR3m-dLW_LGFBLzdJUJEwUYshq1QJHcx7yroP7xWGAA3-TZEzTk58_vidScCTNfwSKXq-vpOs2u4EhrwldRFrkRnQsnt3ouq1nu9CbywUd1x1uSxqudLlGJT8l0j32XkKWaoqCIr64CLzB4EAPpALlAwt9ZXEtuDnVVBhDWoFcGeqICPiOv3ZpPj6yq9-dtypFcWN--sOpqZdBRoAg6N8Xymu1eX2btx_t4HlXTmnK5C0T3CBvDwdCqFovvbPdwfAveI6NJZahshuc5RNWrT1QUuCwNf2jcbBsGTUMXRGeKoE30NFWrH-JNL5CRgFVTBSRTguoHw8uPASAInIc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOQo10lEb_TS70u8plPjWerO9jUpXYjS7W_CHJSsbAZyaPEa7z9Y_LaBgOVsTUkVetXJVvxpRLRq9m_niQocFhYved3gs_HPBE0WmWITe0Cbkh1ME9FH9aVhrO9NU3xHxcjPWyfGRrH7F8XYVN-gfqg-tjK38nzv8h4TI09tLSM_BoRxDyGKEHndQPDy66fZKVqDOi75dbNyCpbwOHf8mxboowlTYbdkaravpJn17ATyETLS0Pha7DpE_2ze0ZjzrMW9cEt0Q-SFdcANaDuSHIme1tASoXVRCvcxzlKelW_OTHJjWTgaSsoKgqwbdTb2X-eKOsxZjdOaRoK-CSpoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAKxQ8UyYIz1q9KPV0XFqJTbti6UvAmWwEnNDr_980Q3zfoHk_wFXGmzE8O8XrpQO4Yt2SR_PU2JTDykIjIBGIDREpX-0bdv9mzxgnRwDHgyxpzpbHcsr__kZzy1fVx7NVJGBgPlOtWRHkkTE7DGQlraFDI0btmDTWc5WsHxZIBplN9de12qI0iVcI3N9KzVRQWgWj9Rck9jihaZRrP1QG9NSWOXsuWZG1VqJA2YxxK4eBQ5azE-3w3OoxsuLNaMRliJ9ZDBEaqLNMBE_o8aPcstjYrJ54av1BHkjVYHNNTS4wfeABRi5NQO7wLZdw4fVdyGYI8VkPl81IbE-h0iQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwnn-vuw1fPr9053tL37lnrumykwCMOQCpn2cCfEkcvX-k3K_Z2sDCz2FONMAcWd9Hg4Ce1p8nw_ROhGLWZIbCdVxPTNpJZBgss3xmKt21xhqTaTwWGMOtEjZr9UvnRBJrU6SYfI3-aHq4D2h4TYTPgumTqfbMf26jLABwzRsLnTF4W4kZghgq9_gDvNHNJa7b9B9ULlmMdnGuVyq_qOd9IVA5w-QirUg-cOs172yz_D5ZB_x_qRegU8Lp-3Ir58EbV77Mfr5atDhBTxdfG5U0CdflCSXwu01paF-wjDIRMqKE1Tkp66Fbtm21mSfzBvnnBF1bA84MLBf0rWYD_Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX0npswgZn-Kb8V8_H1nV-12e-1All8KkBiGwCFwSw5DYGkx_A-KfgHsA2OH02oflzgLh0qWE5edpfhVUfM-PLhe9gTi4AtU9ESDs-mtCkeobeXamF-DDQKpTu8eldz2jAHkkENo5quTZeXi9fiqcwVVo9f4EqW_MK5o3wyIxcwnT-zgHoT3WCvza4Wb0cKcDAqXhzmOEy78AxEZtTizFOjVFwe1IhNHBuvOkUNMzxWJL5r2Fda9xDcimyaZUXZuFSV_mn7tT_AJmX9JqCAWV5kUJHkuvEiAVX8TQq1i1rNQq0Tky6g-qafWwPH0qLdUpezz02kc7TyToe9hC5vmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5AlLlzwPTjGRJrXTEXTyQHfGSXUQjf-VGtueafFx4fdEUkprahPHeMcLJaoBJjwldpnYQCRF9hdEZ51rbs7ZRikSrGB6bc3QyHLt4GbL_exODghZzNfCmmzE3e_BSTGt6JojqDS4Op2BnOWlanXPWxVrPa5RrCSqMCWViU3aPDmq1k9rU8nbpEeJu9z1lWcTTAIxYfn0P86zjyf3pUxtPsaSat1skaA6UO5N4TA9CelHh_2wmYWE8upTEl1p7_nfdp_g42cfF4rquh-vINGVHApakdzTR9DYz6_g0YjTAeS2jJXGqqhVFe4sGn9Ij0w1-Ph5Tb0i9_ga8u5dCGq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEsoJi_199WJ9aT3aBYFFjpQNCUZoQfswNMsmSIB7UTQUOr6__OYZyxTK1qkJTRiKn5I6vezHYTi47wWKdHC-cuvNYc_Xd-oHeTykxplEiF5-vTfidxyStm89qmk1329UeOPfvAnRGIaqZk0VH8xKJpxq_Mruh9u9BdZycU0XMOno2fUqiPzhAXAdf8JExJhSIAv--2r8kkPk8P9m_Avr17syIXGs9CB2g7wo9BqycfCQbtKLaJduya5WiLe0aEz61Z1K0IKBTinxnY-s0hA1XNqVRIIUHVWg3u9KDjejQm2zaJucTSE7-tW6coyWoWulFuSUqgczoeSO3a6uVPEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXH2U1J4aQSLTyawM4uaBJxkJD-G4bXj8_jfbEN1X5A0d1-MoSPIEFxvgjHbjNOKuzkc5WCDPBM4n5CkGgsGlHagAtOTrsNAg-u4sQGMt7LRG4_QhhOGhHPul9E4L0f0nOU6Q5V6Gb6OsaD45AW4EfE2R6shXFwPF65X1ecDec4VH7R0pzHyp9H3IUF7QIZmg1D5vt29RijMNhf7HhVLv8wEtf6S3MLliIFMZs0iOMJksIziLbE4GwTEzuhG_JbERxvESyQR7nI1sATIB0XGsIAif8FF-StDy0MPnNtthRPZqMRWma8tOTsZ9cqgJ2CUG1AhPa8i52A9ytBr31TXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWQcZHvPVLuNSjB34XjagA4xZxbxeauVLe5VcA8c63Ued0PXqjwJzObrJOhofHdGePXn7yG1Qs0f6bpNvclpOs17dS30qrWsZ0YRfkjERzVrX-8R25T9pok8Zd6exWKzyFzgnibc2x4rrTZvWxqqnMK3JLdSTAr00oUS6uhF7zxlWdz6bZ88CQrPg86K-TllnGzVM56u3_CJMmcdSdG_9BeNQqqhnjPBP5Wq01UzGOVjUH5E_KfwAxyu8v_TdAXqWxGih_gf_sg_cyqIAbiE-SqkmMlAJm7pSASPdmPw3l-J6wk_YoAu2BG68LDPjVb_rsbWOgvfQBprpOpACV2sjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT182vSFlp5R7iPWbkOf9qYSlO1z_22uHlcyW2yJcsL9gA3a8VDfCo-CLoKF06EO1sXN7veRPfrWJ0MXY97HP-37DPr_gqobyhESSxEi3Fze7zWE39BzdvZqnxcUvhaIeDpw6cVf3MnuSlaqWAvQWHIwOMBd7gV4vAjpavOewhML7WOxhyKmr_L36gn09BusHxdqqAhW9iMo_gZiY9fjfoypCGPYRO5cSlmvOpJS1KFkyc_wDJIqMKWbW9rVslnFRlfHDo6aGb9wDNsCVsCTr1S1JHo71jAqtsaqr6IXnTVv4aKBQ2DXCAZTrQmR51-FmwKJhQnFq-lr9eEL9beATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGFeahPqcnFjXRAldqxRxGYpEc2lgzWJHy5BTo-Ilpdk_90MLHCGettvgzERu_S366homx-WazwLD-kcKScPlkuDZ_77TMHWPH4DPamwOSrh4-oL46jdZHEXxQhg1ff7vjYvLTH1uMk6zfD_hRWGBkxbu_RwUPJpK-8feU0ItS-eiqpllhCPzPVe44ve-RekdkTR5pWihoPejYIC1FE4P2dPXukMekZj7hcDoK6soHoPPr1aY0QH_rZlHzZvpWNO43zUrFn4yAD-Z_Ir40X0Zn--DkRndeUwVy0kE0aAi78WpQtn0nUWjPjqDJIHTIpn_WQGnhmsoz3TBO-1fZSMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjqvC15JPa1tf3BGwalmEkU-Cep6sIYlV3y_7SZmCv-lYEPwyc3PzCk9PcJlVdeyxPh3D8Wv4ACZC4Qzu3q5z0ekBAVh5m9GAWO9oKeqBGhhboFpsV3kGd7PnIA-aqGpe_kfa9MNJkU224sPCPzTL5yKzQ5HuhfRs2ANmRO79mMMbMcBfaIkdv7klqw9u-z8fwTmG0eoQ367IJXcxBg2Q3Gg_fYjtysw4XVWYKsICAleL22it5NVjzA5n48kYZb_g6nO5JQFYvh9ni29a1E3YzSlvvxloTDz-droc7S50RRPLqs_g3sC83jfatgQmHHHYGY5_tfgn_m4jzwsjGGsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgpIwoz36vXA0sBP0QcAhlHvdFwY9wshC9Xv3pvx4FhnUx5bzA5oczJyyiv8blkqK56LIc14ifqCiGdvBlpb9WU9LqFb3F8mxOIfyiCsgrsWScqNw-MGOegQxXlF19auxO5aE6aBJEgzpBBXvKjuPA0I2jrMrdHXhyaci-bM5hGlu9pinJ82Qpk0ha_uA4ODypVib87TLDrkNmZ1AX6VBibxj0x4t1kO9yyCNNPvAKp9h77WY-Qok6idHGraJSM1KiljEKIS93bPoRC94Oop6OunB9Jf2rF96SCJfdpKgmANtwZDGbHva64txXot3EU0mgR2Qvh65h3qNlhbpQFUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uci3S-9FxXP0wwT_cObU9zG0FZnlhrhjf1A2OVZrrrM-C5X7cCINJ98ZmtGUJFDcUxmBdvTnZ45QfyfVCvDzfDJzE-FzDks5iemnG0l1BMUbQ1px0l7nZc0z0uVEpZKG5O12IgIIvY7xtjydu290p3gkbqzabqyarYc_tApL3KOFjfLbjkCwXQyD_CWj3k13q3241vMNd3qJjQFMzNt5NCWTlf4PM3YKwgufWOzUN0Tqo0wCp3h3XJZr9mQMWgq6fDs3suH0wqT7eFFaxAOJU8dVgD_PhdfYnd8Jw1x35PSZ0RFh75r5a-tRR9usttqkQPdF3LuiC5P8zoiYpdoqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGPqueC-JBjan00LWC4Lg0ryWWFShjddbke8kuhxNdcoytkFzH42RDM2wfgV3FFdGxvQQo_kCDTbzzngGsiyhRwACytz8t8ZKAmCSgQg4wLZLTu26QjVrOlEPG0Mi4HnV4gzmkv-59KjQXfP_4aLtJW5nRK-pbKSL868u_b6s2Mu4NQ1bjHuZW21ZKjp7UsbUpjgAhwEZFiFCG7audCyi0b12PMZ0bRGMozVCz8w9lJpl8jJ76dyZR99IZ0QEb93GYJ56USEOimv4RwhdZUTg2if358Z0hk0evaOTSi9J3wBRlF3OrlITEDzbsjc-Em9RKg5q6JfwWAnhjEA1KnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMGBognTZjgEy5Q850dPwU6Zo8GKjHICrDsTjApgHCKgOEM2rJtU4FwLxpCCscYpnYFJ_fjbPROgSlBaeJgiWO-2BS7-vkJhGf1pFVHfz4GCd6L4feRTNscKQnOM-mT10_QwXywuJ43mhwgI4Pf9XxTKCMp5AqWHXz-SrDxwAfw_B4fa9uEy3Ml0HhrUJMoX0UMBr2Xf6q3n1mWQEMP2rHJ2lil7POH_BR0ZpEV2EdcQ6rFXpIiEK5yFBxScjxeRtYbB309R7J5-l0zWeVKZKMUdHRYrMII3DFbhiFATvMmnIrGGD6ankCZT33QLXuSCC3ZDwco6ATcBCsm5qBcksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcW-jY1i03tupqBftG_SAoJNe2aNXJi5w1OJQboeJhMffWAOfatAedhe-9aDM7ZfTM4PWO-YopQuUoqQhp0oPtduaMKo6N0QwP44k3X-EzInRcKvJXOV2cizeWn-dabt5b0HAA03M75AI9Z8lnP-6ze65haf9iNTLbORSwysUsi-hbQXW8oMXPrzXQf_IbDfyy8Tltfgs9ESmlE4cIT62sQMo4xcNrkV_yhOABKIrM7mHVGZBo6VcDp4LPE2-ACqC8sQLr9fZi-bo40A6Iaz3BI4G75MsP_EAnHaKi3T2MrovHDxkQzXVUvz0bQh7QqNkT3QXVBqP7_pRrm0v7AqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzhrIfw0_8fxTfp8Rk9T4sH0XGXCz9XteKPqfH1BnSTc5DZfvf01oLMeMiD0X1tO6AuvIO_LzzIZAWFvBkncWR-S2sx7kyRYev10K5ivJMQAh1_GmuVJhK5niNXP2Adu02FdoqgvgeCaWOePzLvIsITgIO2l0fsz9AXOK4e9tMUopr-u1NSRIDFzOgdcdsGaSk1geXdGYViJwnHSPcPezMGH1UuIyqGWG70RWHAkyTrLhKau_7LhmuKJdh2tjUm3I0sV3MQAg91zhDwDraLFm48mAIvTsJhs7zUfMTGWZOA1RmEOfHqFBW-VuFbfVI1v0J1rf93DqVgjU8nrbDcSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=fkObU2uhwdvB5yDQGhAR6r3asyijVAKyesJA3DGxT5XfIIYQMe__laLcnXchHBWK97syXI0StAYh2AmtxG22cjWJP4Gj2P2eAAlB9tLCyYGV6P_bRPWIHOpzSZMEU6tlmRL3eT4ugJuQpRcMgMAzrkL0VknBAacM3MAeKNSeBje-vp2CLMxvOpmhUxCCC_wCbI1efz38QGpTAw8ULZSth2tzoTsI_1LmWpVo-0yEwRJAi99VDVrV501CtyClqMc04chdKY_IU-fScWPblCipxJupqnglsqzICLaUWSwOygx218L61ghSEvCjqQZ2Hg9iZ-hIZe3FP7wb4auwS8Lwdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=fkObU2uhwdvB5yDQGhAR6r3asyijVAKyesJA3DGxT5XfIIYQMe__laLcnXchHBWK97syXI0StAYh2AmtxG22cjWJP4Gj2P2eAAlB9tLCyYGV6P_bRPWIHOpzSZMEU6tlmRL3eT4ugJuQpRcMgMAzrkL0VknBAacM3MAeKNSeBje-vp2CLMxvOpmhUxCCC_wCbI1efz38QGpTAw8ULZSth2tzoTsI_1LmWpVo-0yEwRJAi99VDVrV501CtyClqMc04chdKY_IU-fScWPblCipxJupqnglsqzICLaUWSwOygx218L61ghSEvCjqQZ2Hg9iZ-hIZe3FP7wb4auwS8Lwdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd_ckYbsUc33quwh9Z9-0MnSsuGqtQ5W75evN-JQPHyfDIBsu6UDbQKx7pw-tq9QKD-Va8DpeCjdMz2OI_Mu8pUES053a_vWegGxDGpuMpAMdfIwDtjmIec38DzFG6UXMFeY4G2q2o0Kv9jmJPYFc3hQAw5GepNqpTXAa99E4DYYChlhyoA8mH2eKCG3YL6rhhRvR0swAk_E_KRNuopkRGfp1XAC3WyMZ1JAAALBYcGdRy-S692or4tkJi52kchQQqGTuDnB2PVCH6Pc53QUs8JInA_SoLDAlZyok5zxiBHA4Wc9YcWlPT40L-CX0d-cHgFPFiIgVLsCkj9SEj1j-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=l3lJj2FbbL8mCx2s54p3RtLNtq7GtX7Y_E90wbEW0Bq7SEruaPEHHCm1g-w50P8y67u7ScJ9_t_PW956G7Dii7UZZTF38oM9jeXoOCyzrqDJRM6BDfh0qf5Urb4EOktWkMUCEQWHFJOHVrk8HWQxBRc5MGL8oBgq72teJ8gMhd9s4194OOBIkJtzlZFl5W0ZBlw2iWwplgg5XFM96mzqpHQPtSGuKwx2z8nieQte3SHA8XNCB5mhALas5qngDjUoXeuqu-ha7IWseCPrwT-6WmK_of2l2YOb0o_7heo22kWo9LnK79bvtsZIdapLy6P0Jtnz47ncikv5SBATFm2rZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=l3lJj2FbbL8mCx2s54p3RtLNtq7GtX7Y_E90wbEW0Bq7SEruaPEHHCm1g-w50P8y67u7ScJ9_t_PW956G7Dii7UZZTF38oM9jeXoOCyzrqDJRM6BDfh0qf5Urb4EOktWkMUCEQWHFJOHVrk8HWQxBRc5MGL8oBgq72teJ8gMhd9s4194OOBIkJtzlZFl5W0ZBlw2iWwplgg5XFM96mzqpHQPtSGuKwx2z8nieQte3SHA8XNCB5mhALas5qngDjUoXeuqu-ha7IWseCPrwT-6WmK_of2l2YOb0o_7heo22kWo9LnK79bvtsZIdapLy6P0Jtnz47ncikv5SBATFm2rZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fizr24Llq7MkFEUGqHe2dUYXC7PvZXxrpxX0H_n43PgOMSHA0xWvhulOVto1U-w7aAiPWV-UG2ol2B7E-0yGqg4KM1ewFqz80f5DbdLAhvID9jjR0h8xp7j6f81o2PdgAezR6qm4tMuGqPJMZMx2ZllkUSXH1DNkJ-Cupunw6mES3wfy9YHWM64i_Q8b37n-lB5BW4yjKllZW7uD2b6Dfn0aCt08xIekkXhDYrAD8gAsccgPVsR3hMgWSf6eJczU_NwZ62AHtnQeoeRK8v8gQ6zEH0UrFIZVlSR8PxZiwyw2dpTZrpV2YEPslTZ9t-W280heHs_2EVMgAB76bCchKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIiVME4VdZSq3QvDYV-DsDfa-FyoBrMogvzHzQIRx8ociBL4xzcc9Szk9AZs0NHSB3_QExw0neZD4nHKfoEaOWl0w9IytoFJK-8s8OSfy3ZBmYR9Hwd-Se8h9bAsJFMAUb1_hvozHAN4K_2EOAzvw4uE1VpZbEI6pRIsTbDPPokSb-n67ZwOIHBpZjjcaMd5DxArHvTE_QeUUFrWAC2Dj-0aIO2U4pDRMOr2ziQGVw-zzZT1I6uTCuIjg8h88VmtxUucBnrmgQzVrZYexaYVCjG4LXn7XIkxg_GU-qgMNG-SL3R6-fg7EG7K8exwTQeVRzhUzjvG-lACQ31BfIyanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1oFbxWtxtuhW1hv5j0PgS6xszd0DPOBQjwmVmVwhh0VgprEjOjCw7PKH-a_-xe3B2-fZfiMxH2c4gyhHqyjnp-6To33rEUCvNivMY8TH4-QnYsb27GUPXamnPqnLxhjU9lmuw_Kp3CKJs41Y4yrEzncl9bpuanolLt99STf5ZBU6Uvsl5AwqLJsmUs-6urmawrDe5WT4HsSneG0GchWvCYeqaF-fpqFdK5D1xKOVoqFzMq20t3HbYIdWLo0dxRK4RBcYIdGtqVPtq6ZE1NGi-BLqFhWS7sMvUbGaVPJ21x-iLSSaU3YiZbywlufM3WwZjtSEq2tDBvvlSVPaJcYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkHRvSDk0eo_SfPt3QRJ78Xjh8jY5REEwGYH4hMddGAzP9_bKut2LtlUIbPADty-cHTcvlX7yterXHTlodyCovEzLWV0afvWp_nH4sn4kR9gqxsa9XhL8uMur8z01zMQkuLn3x8c1GCBgU3dDzoOYmlPaxaYCt48QGM38_Qx88Nur3iLTkjiGPG_4Ju2mb-vTXLezj_GuNH7uwtQ-Oz8jq00aOzgc02rbFPErLbwCUobPwoCBb4XHBzoHGrd57WlKpTGkNMYo-lUR15Uj35VZc25Rj8diOpOmx7RhMKYQu3Z6_-ct2unSneh7Gp2EI3nuq4_6nAeEvu7ZlkbV1TEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFFCDakPa44UvZ5PzTxuWGrNhegkh_wR6s9l212NbuMw17PYHs0ODIDBjGQtIR2ScufiVvbLbWEbYutVa5veElQpt0IayiHGAcDSbRPQzg4izrg9EMcGISffqNeflWWAn2zvRMQlhWhnrmkDKymroy5SiV7qnJvcMRoQN78-fLQLPgWHvTxPsvPKlOvnoLLVuZA_eByFJqQKtZXTf_eTGUBn9q2bs34yIWxftRr4RIPHiN149kNzMHiiJskwLZ4lyKfF195bzPcH2HNpZOljFsXF7rBkUCIKC2z6Lp9BuMchbKRIx0tuadRa8C9_8nb0ASNVrMIVbqDX3Of-ZhYnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7pZdzgTjF-iR7TFa9NHgOuqD6GsmeJUrLV3MwrUjr1YUHm6Aawtg-YFxl4Q1yuYWPJZfrvXk7tVZlc71sVQRH04LWhtykmY7pGUU2R9yDFpihqD-feY-YEi5WGAXIisP_Je2C-m71YOVGwvMHy_dPKd7eepvI4EouBlSCxiIR41Oi1v9lTqeS2HjiKGzuUXwSlvQgjsFUN5h9XqsXlRJ9oAhjQja7bOo8jl6MQXQznzqo6J4zT2VgFumfTNBjr-UtUYKVovk2DyIWPg78vQ_cXM5WKM7In1CXWUlF1tVEcNZk01rlnHtZL8N93hobHQbvJPt2IOt0F_HhTt27GQGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFDIrBKiMguDvr5K3rhgur9YxNmZeB13fev9IHCwC25VHTkiOafcozX7IdAKNMUh94GqwMwLNAZWHnPBlB6DJO1rlRz989hkzcILgPyBBmJcJKBISNWe4PMSL-TA88Y0_0F3KwvN9C_FqR2jOGCg_mP40rHh40Uc9agHCisRYTg3ueX37gblTeAn_Z3vDcu-uSc8cEMdTkmq34n5_DsUmznVU2ToBHCh-6kbpXLKkXOFPKdOg-Umb8wSAD_QRNpsQxJcRyFSLW5TJ8qqDll9BTP03srVTO11DGP6YClw1q0HgzuyDvfZEf7fDz-xguQuGn8vzlEjAiB0p6ERQ0HydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ7dpPo2Hq7eQQ2HO6AsZSIWeZbqOt0RnntFvWIMIghSBmM7RV-8azq5vOWnu2yw1KBWAeL7OBBQb_jLVw3-RkrxZE3O3CDlk-_GFCF3AYd7EuFDMvrxyHDzKLytSw1Rlc6GZDxFrmZcqZvqubJj5-0pO-6A4fGiUmJzuUr1HHI9L5cX04N1Ux4I2ZlLc3OeoCPHb1j8gS6gNUUgK9QKu3d4BaAdCslc9C7KvjHfHop6_2eqBm7W5Lwb6ko5OqgTw_HiP8zi71BHuKDDGexYjwhPp8r2mf44oGyW656LRAP0fLxIT0t8RX8JVHyRMlaR4bSYL1ubf3THgy4w9P0SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOfbm8pxMCQ89hvrKgRKF9PuNpHLmnnlyDG0Veo4Jvr8uLOtBzHqdRmYLMneM35GJ9w4YYihnQlEKMIPo0K66G5IieqpW19oaHroyxIvIaQDeIO089jHgIbFYssnHpdfkmn0oVw0Lb62ajyE46pR7IRXUtfnK2UDRPCplCCX6KGWGt4m4Iz6SdSGSvsxraMlx0CA0WMHvI1zOrLRI9pIg-K7j34C_lEg7P5VID_ijh3l341ailzimp83lan65lvIycJoxL7MeljoIcIpBjBkwO_0MDO2LGLAGlPeeGJBVHEsx4j8wzyD-ZrmafkjAokaLc4dEUVy6Im2z2teeQUoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJneKdHtvBJ8B4M1MapIjnmQTI4_k-bqox0Cmx5HreOUkJlYFxdwd0QNqbVsYgQ2H5QlRT4AcYPVwbg4LRli0cCi_IrbyYxcjykwhaxlyc2iaMd2xEkcn8zAtP7J_xIJYfWgzEX1RySlRTFyJ50xXjIvTskHY3gaXlaTU18hHnS0eWsPaoqIi-IFESgnbDLTX-LaD275_lpKh9NPxbQmXW94BVGdXsPjLoTqtsKFbIdk3qIXfV65EIRGIk0T6eUZLKkiLOVkEm0I8ZI4H8EO-IHkXKttVNv-fkfXLUwx7V_irwiMNXJTt8bHfbPTu8Lw_8uaB57owL9KapnOlj-KJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG1OaP3WdcVpDs4V5TUciCW7CX0jUJHQKjq-OMvRBTekCC5iZqqHTYHesilrytGlFIQMb4iNup0cxo5xCh9ZsTPpDutDjrXlFXvTzIOMlGHljM3Dw-t3M4nnhaEuPrc3VIdeNXk4X2c1jsopkQRYnCbr_T0-DCMg7IsQUjoosIutEjzbaKz8DmkMa-JDd9ntMKrPPazvJ89d39g7IycT8dVFSck74QZRNpwDync5W81kloCvoNRavTG5R_PlPyI5ZnTGzy9ZRG0kQZB6AvymqiVWS0rEbdGTGOcC1FIOQu3uRW_QVLaj_tgmqBt9WbqcWLCgeOghLrk33Z2RYziC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-8L3RARy9ETWMPJpjGvcJO73jYtE3b_rnAZ6V8UmO76cynfU2tk5Rr00PiYfINeLFE8rHuqa7-bx-ce-5UMxwdy0Bvgzfo0KkNMc1QYrcdwHrlh77UajxRmWpfsBB7pm7c0Reo-dEm7GLoaiZCeTaOpmvLH43zADvgyPt5HhWxIj2AZpZ2q6y1tjYoa24LYOZuRpdmTYDfk2QjaDnFFOTo9b6J20wcm5Zz0rduys-2DnvhcNRFSGtFp-DGT_CPuxFDePOgNiX7iZGS8xFtSfwU5ZKQ83_E1ODMjKFctlTGQGjXujzn8dSzSoIu1afsRk-9MeLZOKMqRTDPQkhd3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMTSFzKrKQxDbbAMY_IkB6Ajcjlc-kCa_j2cq0wdI5HJXa7kvELYJUGvXbPdS1mygyNOcLa6sBN_1VfCEcQ0h0joP1vIKqIW-N-s8PEzqXpanOUQIm1aMebDyCP9LU1fdhrurm81dLBO4hVYs0e6OGHPP9_dZlJ0Y26zyn52UX9a-9Wo6gzktKqsiYBKkXX21HpMe4_DB9EL0M8e9Krb3rtn8Wyek0TSwUuzKfiRPqXqMayS75hNh16F-z9pLFoK8nOoucj2gMaHa_eo29UK0zEvXUVLkzYv7cW2xnAix6nnw1RvJMut1hHBQ9rjekxClaDgiMwP1oV5K8gVcVAUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=h25bxfC27YuvsFKXylD9JArkFumahWmLI2jAPGRH58uFfibgTmVstGvfMbP0yBrSIjLvhE17G50riIAkBB2Zo24qIboRGDt9GJ9zgd-tzS_1uZUHO1-iZZyvVroaKdo6GofNHmzSFoy7gzw_W1EUv9OW3CZG9LCOkyhIrSRdJNP3tbUBYYjtsb7kCAthhl1oyMWktnLm7wQd16CfDa6kBV9dwX0un98uczyIqkGVUOePQ1ZbFcDkKy_HjhsWVYPVlH0Z3GJ1P1AB44XH3kIUj78gioDYin-97EPZG1o7CzpKCLzQyr6SHsFfZ2QT_VA7T5-r6FOWn8UxMuJc3KbqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=h25bxfC27YuvsFKXylD9JArkFumahWmLI2jAPGRH58uFfibgTmVstGvfMbP0yBrSIjLvhE17G50riIAkBB2Zo24qIboRGDt9GJ9zgd-tzS_1uZUHO1-iZZyvVroaKdo6GofNHmzSFoy7gzw_W1EUv9OW3CZG9LCOkyhIrSRdJNP3tbUBYYjtsb7kCAthhl1oyMWktnLm7wQd16CfDa6kBV9dwX0un98uczyIqkGVUOePQ1ZbFcDkKy_HjhsWVYPVlH0Z3GJ1P1AB44XH3kIUj78gioDYin-97EPZG1o7CzpKCLzQyr6SHsFfZ2QT_VA7T5-r6FOWn8UxMuJc3KbqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=Mah1mslfrvljtCBNoZNC5aWXGpxAY3XPpQ8NfxSZkE948nXKcvBkNKr3-C4LncD0IFW-ng8oaAuWL3i_wNQfk3tSVn1_DZhkSENLSKCnkhiOZITs2YSZAf-5_jH6aeVQ6uonZ_KJlUI4U0dINAsrtGFzVwSnFHwp5YCY3_LZpQAIiEoGzRAjlJdKvRaw7_XFP3LS9DR1fLkLQyXD4OEaq7409VYVaL6G9grcJM4aIyZsKgT2ysa1DwOGvweqp2uy7SxpE-u-BLuDSbJUdGH6ixOHtrepTOXs3vm647oZmVon6drZu9G-x8q0GHWxR9EDId9U9Uo5uHaWohXf2rxilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=Mah1mslfrvljtCBNoZNC5aWXGpxAY3XPpQ8NfxSZkE948nXKcvBkNKr3-C4LncD0IFW-ng8oaAuWL3i_wNQfk3tSVn1_DZhkSENLSKCnkhiOZITs2YSZAf-5_jH6aeVQ6uonZ_KJlUI4U0dINAsrtGFzVwSnFHwp5YCY3_LZpQAIiEoGzRAjlJdKvRaw7_XFP3LS9DR1fLkLQyXD4OEaq7409VYVaL6G9grcJM4aIyZsKgT2ysa1DwOGvweqp2uy7SxpE-u-BLuDSbJUdGH6ixOHtrepTOXs3vm647oZmVon6drZu9G-x8q0GHWxR9EDId9U9Uo5uHaWohXf2rxilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq09UYlr5608OCJlM2p0LrGS_N9n2iahbAuJCTYVxljTmD4jf2J8NSMGSaq1YU_YsA6Iz69ya_WGwHrK6gkfmUlGfdZJE99wD8Hs4wQ9B1lqCwzB-YYfa2pDlPR7XFSlFhHJ5qBIC91QpzoL1eVJ7tVPgldUIwQgfH18Z6lToLefIi_h0vLtXPpRd8PN5_ntqPrEMYfKjaPuWXfk1ceCfKnAJTDQXQ_6hwLbSFHjXnegdMtEhI01e3fGrKNVYmeZjitfMAR2PiViutPTVy6Fc3N8QIZMiSkiCxmmhRW9Eb2V5FgseyVzN1NTYednWwzZrfIQfRj2DrD7kn3BoJYU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvMAryQjYxmzNHSj2rrFyj4BWd-NBDk32AhYL7ZyFlUQ7s1gYaboIbuwu9embkqki1_9ymoMTIRZaCogmyhzV2xv8WKTxMTPcBfPF3Siik4xB5xV_k5fQ72tt8Z8ILHb2heXtKAD2nYLPZ9QQJ0J5DMx00NIhldmJdxfb2Ox0keVXhxAFB_c9FmJiz36c98pnHZ8eFmQfrlACQyvqhq_E5D45esXGroapAQHnm1OSn85FlGpp6jVj38DPAYFVJ3dFVcVy80LlnbK38ksDd06CA3C1rVuRlb1LizUSFhHIeT0mgpy-Kj0dNYvTVMX9njqOMkBSB1eNbRan8fVRgrA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA-o0IaEXU0FOU9jLgNsX3Kx1PnqpQX462Iryl8BR7Dq962CRpA-GEIaoPJ3GUV82XtA4yeAhLqbZCrCnienKK-Axb84eE7F1IhuzZFpMMUYj0KbXbrn-f-g5XDZTyteKHigZjlBQjte9VAWguxQg1nUJfpT2YkSldwZ4PjtUACaJT4n-rJwVzgUKlE4iA10M9njOza0JFsxjfnT2aJOrWazJ-ZQ-QL49iEKEqBDZRF0QkXHXJFl7YaP6wpZ-XsxSmA85tZgTTMbqBfYmqYh045QwZ33GGklRj6PJmXl_rvUY9ItwOsdNHwy-lKxOQnefxA94OTsCtM9Jeu-ESzOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=R5KUITYcb_sQ2aH2_6ZnW6TqOyL9znNhqMFZcWsjCaDye-AL9ViiYS2BPouanFEROHtRNvWu5tAk-chFwBqPud4ROyhy6q2ogpwTUwlbR5tXDqlf6QkAhs7nshwXXY8NrH2zVXcj1CXeLJxF1C9C964dAnBQXS2p9CQyEQDlDD4ztFFn4hA_1UvPFhR9jSv-8AAABCyNg0Lr9vx6i7QVHgrywwJy5yl-lvOdplvoDu3cntLOTYa6DgFrhObSUbbsK1mTA3ri157lcdypFbU7GtKA2POsMMZpxLfn__GcLTix6E_eAaNn1VSChWv8ifBGSwHGfww_27-_FKtkBSJzmVGRLC_W0ipRJfrejhu2e01ajorZ8_KvMNuZblzrjvHDsZAY9szPRudtQ-nHcU0CNxht86YLa44Sm8s_yBXExlUiqQrsjLgFC699KPBuladIGH96NIxI6CKIn0h7mDH1j1Nx2v0eGeSy8BP2dP1_ZZnFiJWhoTBdWd3oPrQRQ9kGo83y9VO6FSHBRPCS5guQsoOS_cAnHr-vqdDTh01CtiTBUKeZeku_xHD0PY1Dlih7ZT3UURzDcERgtV98UWrjz1eQFC74_94ojlcS5ysX2HJJWdILzzxiWSkCClBbeaP_pQRPrzff6--aWk8vhzDujLxtnnlGYoNnKH5-TGmB0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=R5KUITYcb_sQ2aH2_6ZnW6TqOyL9znNhqMFZcWsjCaDye-AL9ViiYS2BPouanFEROHtRNvWu5tAk-chFwBqPud4ROyhy6q2ogpwTUwlbR5tXDqlf6QkAhs7nshwXXY8NrH2zVXcj1CXeLJxF1C9C964dAnBQXS2p9CQyEQDlDD4ztFFn4hA_1UvPFhR9jSv-8AAABCyNg0Lr9vx6i7QVHgrywwJy5yl-lvOdplvoDu3cntLOTYa6DgFrhObSUbbsK1mTA3ri157lcdypFbU7GtKA2POsMMZpxLfn__GcLTix6E_eAaNn1VSChWv8ifBGSwHGfww_27-_FKtkBSJzmVGRLC_W0ipRJfrejhu2e01ajorZ8_KvMNuZblzrjvHDsZAY9szPRudtQ-nHcU0CNxht86YLa44Sm8s_yBXExlUiqQrsjLgFC699KPBuladIGH96NIxI6CKIn0h7mDH1j1Nx2v0eGeSy8BP2dP1_ZZnFiJWhoTBdWd3oPrQRQ9kGo83y9VO6FSHBRPCS5guQsoOS_cAnHr-vqdDTh01CtiTBUKeZeku_xHD0PY1Dlih7ZT3UURzDcERgtV98UWrjz1eQFC74_94ojlcS5ysX2HJJWdILzzxiWSkCClBbeaP_pQRPrzff6--aWk8vhzDujLxtnnlGYoNnKH5-TGmB0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXvK0n_whmVUUGVbBHWGgYAPGWpMzBtFztM9-ZURCzuLOF12WS4gDHLB1q19g77QJ8YdT9xfRAY5bpx7_1kYY04Kpi2txys3CggM99gYqhlSq0amKdhIfNiXW-hHXKhjwaqfXafcuV_P_53FLuM7TumBNMvq7N7Azmc8PlRf4oUM9MZwlgxFRiAPhz9cCGtCTjbgcxWIFeC4B3Zd3NPBi1fCiEnhw4anOd4KTQWXsZ8e588cEFa1Dyrsx2oUcQtZnPZStp37cl8qizf1iD5-YkXgfKlfwVz-n2ZtBvngzrI7doKc14rPIb4vjBVY6MB011oliBWV7ZLJGrE-zoT36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBriDVtmTg9VRrGtp0QQGuw_JHxe6BhmaqNoIwjOmJ1-jgJvEbyEUmhMwOrX9s1yjlSBPJZJYk8Z71E2Vm1kvQP1a3_sXuiaNjL2UgTevwqBthi_WtqXC6n0w2lz-vJMsDHov2C7lIYhJhCnbcX7VYCt8_fCOrnuRxJvHcj7mUVWC2GDuSUpS0QqCqRGVQ7FkqvnH4iy-HAN-LETJXEFfAHqRCERnx2uMhJgzYZwtvP2MwnOw5msFTxbNoRJSSet1cibadX7W6Dk7pLKp4Y2RQOtTf86t_ABoGQ0SGX6HDxom3KU1a1ZgRWuyM1QxUAtTKDJ_uyAPKyzEmpjwer9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5cziTnmKM5HiNdhjmEOm6TazOvtisyW7AtnILzLPMGEaI5Ynsp0Gwq5mcqelULu7mdHfqn64zC4aSa98z1s2eYKI50vuinRiBiKt_C9CfiOCh8lBrmjtWzRGqYiw8rV6JWYXxBiJhq-wmyJPnjnY9X4x9g3UCN6T5IPwlbyI5Pbprb0RSnlPSWILvXYJXM-_aGf6tZ9Lywh7wIeo01SEG950LsR2c_YkIbKnnW9QHuznLnRpc35s1oWwnKAWJRJ3VJsgLYExHUEl2mS77RJ5xIv3sa_jTIu52q5AUJ7Tz1NS__fU5tNYWkuLhPUfTx9_u7p1QmRWtFFQKtvPSgpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsSzTD3pmV8p7PVHr0YSJqHF3ODFu0bx69EkG6l-r-fWQxKuw3qqeXvE09V76m6tcyHv7hQD-9Z1I6LBa3WJnrygR2KN25jVN-eBBrngBTxLdFSPjBP7_kzVVGnDMB0ZARF9LEmdj-a00DjqVNP0GqrI7d0ObJmLu_LPS1SZ7qNzFizoSmZvQdMm_STHRKUuy1L0jcW1diK2n_2JjIn1FJudL6FC_wkV8OV88Lj5oXy-1Dzt8tiLj4F_c85GX6jfwDkohXvkVj80uxosZAF0Y53Zo8finHlm1KAZHBQhqkvCHC2fMwCaWe2jVk8-E69v6ukW_ussdNUUWKHlzPEUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGbx_83Z86nE6d9cWHD0Xy2OZgRQrl-Ndxy8RbVmmwj7XYBAodxlOyRD9u_-CXhOcVF1v4R3CM3U73WevLjji_Qvd-_oxN-HaEKo0L79N5AwT1ud93ye9A8b7xQL2UGKvJZj9h8TBx469-nrsXqQKAWngvuEliSjC7ZLF-6_yVgv2daxucCsKd9_mT92fU5GP9DNCptkWxkVq2aCVOgLyyAY7bOkwLtM_zU7FXLXdxsT9J3JLJsfXGfV_hgzaGW5pH2AwjhTq41hTivtLY6YdZgT_wz9LpdjnUXas40TnL2LXptczRp-zGP4sqB77X7gP4LUxi8MjD0aZUvdZzcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGn4dO7roq-gl3musLqSgW3CYkQwABAyH3Er53d7AG8mdv7soxHZALjB-DU5kLQhXwcRUlZqhUF-bB0dTXaUsmGVfXx33tZIUsFETt5RyFvdUy-ahOK5qR_axBgOxawiW9bA2_ztNH1kz-ijdJDQcO8BtNiFKXwEuvVvnHPNSfybk1ao_svmJOzD4GYdFYG8d2weWTaZwp6xEqrklwoMFPU57-IJWQeQ5xnAb_H-icZ9T_F4OdusGYesg_LhQotTbB6Mm5KtpVZn-jmR6CcTu667VUzhzLsg5FRIVkRqXPAj40DuoqNhOtGrrb93wXA-41GjZjkEds6nFQXq254l4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vXZQKu39oQ65X3yNhWvaICsaHr02zK1Qy_Rob2PV2c9Tvu4GNlxp2DYBH06VwVCyNyyb5TYt5XSlOSmWO-swmhkY3vgNCHnsgXeGWGyPYgh2zzmLRGclgKyNEjg4tVJZ4Ta_d-KC2TuEKxW2ayPI6lw67GF2qc0wo5Vwhr84LI4iSavA_O8pPT_RmkJM_JgABNO3X98Kj3o8WpgihnjFPl6h79ZN9SgBdTjJ1t3T6wc07ThDRcgwb6aIWplIcrbq7qKke25TnHuaxiodKMpuvmaWx_xhkUvB59fZmhsqM9-tru0Yti8V1qbMxenb7ExFM6rZcmLASNQI6JTbX--kCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=vXZQKu39oQ65X3yNhWvaICsaHr02zK1Qy_Rob2PV2c9Tvu4GNlxp2DYBH06VwVCyNyyb5TYt5XSlOSmWO-swmhkY3vgNCHnsgXeGWGyPYgh2zzmLRGclgKyNEjg4tVJZ4Ta_d-KC2TuEKxW2ayPI6lw67GF2qc0wo5Vwhr84LI4iSavA_O8pPT_RmkJM_JgABNO3X98Kj3o8WpgihnjFPl6h79ZN9SgBdTjJ1t3T6wc07ThDRcgwb6aIWplIcrbq7qKke25TnHuaxiodKMpuvmaWx_xhkUvB59fZmhsqM9-tru0Yti8V1qbMxenb7ExFM6rZcmLASNQI6JTbX--kCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVwJqtI6eVkXlYT2uegX5OTcemiqofF0kw-v3eY45g092VSIMEyQfXu4lDIP_TFBrs4wJuu46wLx_FmlCxGi5lv7kaMy2QB77jki1YEytzKzl436RFezWtVtBFRfclLGISTKRTbkILLzOZwqMj9cME0_XLQzxs8ap22wAWzvX-RlXXYB0zBqNnXU1p3g2ss4DvvlLpiyxWsiiEwsr8rhcztapsSjC8yjUpUW4u1MXU4f3Bn3iwgrl5cZnrhvEy8SsoV99WQ-z23mQ_8g2cLwj4mNhfJqoSHNmlcZ-CHoAR9sZAclUzsVmoGIsN0Lc6lSr7mSh-bN1iRMIOcIAyY2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUzP7kkUNHfQ1ZrMHWOt7PNQJTvIKiizah5mydl-yt1dxx_DeNaIx6-PQFB4JIsNemHnxGSsKHjKcVB-XURDSkGWEPv0j4XugzMCr-WEB2QURMgNK3zdthOeIjDy6CAABgo4P_sxfhKsC-l9jJOzXiznJeC6FSXskv3eJ1fqIGutCA2hFV3fx7NYfQZQhXgYTUkPLZ28zsAuGLdNeeE86xXFWi-AnFATUIscyhUkLwyobOk-GGHbtwWqCBKHZvjLxvKm-65eUaJx5Tcs0J45uta7vNzlXOgMz80P-s8ynoCmmRnrB5tC5gkDLuA-_p9gP-B2Nl9TA7KGqYdL-PzEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AovjrTuqVDh2sFxiNptMvC65r2A0ewUqB249J8YYG1OzgTyETQxJzsW05yfqts2ScB3efJR3YV4OMwW2IrFToxWubqDq0Me5Vmeiptm5ZGgjmE89s8gEHNDcG-ArcO7l52cArCO9XdZZOmmlSrXaEpC2otrVY1d8UxVlhiPQhMfm6X0Sjys8GFdQK7XPMR0ANqP2k6-49xDmRY_mSXgXrkSi_7PaHDSq3l0BHgelVUfpGjZPbt1XnqqeaQCrAv1KXK_jGPEB4JLLwOJWExCWrtw8u27tVrX0O-jGI6IVLAuD-OraqTm8rgJcbx9L2DWjdDsHlpRf59scuBVoI9fBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXHt8-g7zSm6AHAEjHpC2sfqQnQiCxxDmgNufQYRE4iQ7Sf2Fzy0Rnjz8eCOi1Vfc01gYdLA8eerBzTCW4gJgdJwEcioS2M9312wxIU8EASux7ocXCzTImNU6wB05SRhujxQZCEYrrB3Cq3PV_8ZFRiZtEs5eQ67SwQLMs0SUsYm9XUU86l4nEz_gWMS8J39hgxJ0hCwUIv_a3M9hCulN3jKNDbpGIujukkWcUUmtZkpjnsl0ZuPUQv_OgIpFFJoaArPV5kUbqkaeh1a1u4Mnas1kmV-oWMnBNB1vLAQtV9JSrOMeQSPG1qLeGnOtmnkcFPN7d2z6oXErnch0a6pRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Duawv3V6qNKURsYu6l3SGVU808poCS4gUhOirrONxdrTrCQX_5hsugZ0X_FI52l5xFqeKQxX1DVkcelWcAdGBewPnHdDpE1kGcXkiwJHjc2nkKmb8zWu0co_IhrUkqA8x6Q4yTnuFIBhPlGobMNnVVzTpBS47xm8ShbVq7tN5s1NtzzdXz6X99fE91fCBwiSEtt_qgejMOQ-73El_DyygCapwtvvBsViJF4OH2oqHBbneO1bwGGLlpqvnELQi6V_2s6DhMcZvwvH81ibFNKXnWnPzNCXIYO4Vuopn88MQ5k6IHNNwDjvKgtye66DxNwr8LdXH_O2pWjmuPFsWiP62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4KDvZftKdxCUyOkuTJEp-uviBGs7hoRvVXMnoQY9kgOjkAkRP1_3WOUOtfU5OZ6oYiCr3l9bbTP25iYQCYN3XECgNODTYPaVsjzRBJGs7XIhgWK40grcY5s0KVHWlcalyEz44hrIqlQ1FpqU63K5tnVU7Vuv6gs7m_cu1SENOpxfhXP5DUHdrSr-R7LuR9fOpV-nov9I89TkclQJ03Rif8QqGNTUDy19zBaV2TpPMc6KEe-X0Q8aDrZaHsxuupSuJeiDcY8yK6N4B1m1vlwAjCtNzVo2nRUFi6XjqTSQY7FdwmRnX4v2_TXy67e7Hrgz_fWoBSq1grUAQ4527x8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRU0CmDW_WZkEi7mEMEcxHMrxTHwC2sYZU92hKYVglUbWsAXjWwvL7MTeaWfCJ_peXAJecXonEOJoTLis0lrmYAb5oyI_zQiLSsX6uy_sFjWlt5C48lG_EgXEzhnZRYiGk0iLTp8mcYdVJLAllOh-hlHuNFxf3-NGm55UkFoTpHIFMQC29Lbzy0xOUo7099QaydwBwhT2bIvvTQLHj7ffIG2IrFTjLchHV7d25CT35S74U_8YNRQ16118ORjB2ehv0Gacn8JXTqQW3ZeZ2MQmkQR0gzrzvMty1KlpGp4Cl8rgk4f7ABRSJ_lbCfDzMZMB_nqsU9czMvYnKheNhtx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDiQJDgEVEgq-d7B9KNRhqJG6xNIIK_zvTirJ3hD0HMWvA3Z13SE409kQweNahgxwuw0AcPHXI1ZCKn_hQZtuasDVTT4S7oPgakYhCWGYmPfB83zNdvcvqWwP-bhev4Frz-YzwOXwXtZrMT_1SaVrnl4JfF-WIR9qRwW2ZHu6nSgMOuUvhGk2jCcYhcXdH52zVSEjq3NTYCRWbZT2Yt4mV7hFKdLeWnlu6Boc8sxsUwTgDIm878QAH40SdBC6B8UEtzZMz9mn3tcr8398AeyABuPyjVUDh8f5plekCpcnmzh9lmkhjx43Mm9ZYVvumS0MiffALQGS5a2DpzRJTwk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4swdxCcTW6eKPd8alXhopZ8FYxAnOIAFDXSO_KR07lIGOXtP5hsdcQxllABvLUkOOLKXm2B4FSBwE2mcOvYAoFv7IWXivrjG5sDdZAse92J-wPGcXtQfOehE-GHWdO5Jop-Hqshlge9sW-ZZKJ4oSsJTY4V6c-RgWjZYY-mHnAWp6jsVxixE0i9qxLOPCsY3bQTu74TJpUscOAk-BNzsfHP03QwbR18GITFcJR2M1ERDzN_1UN7csdCH7FvGlAu7Wt8RfkH--lIUjntlaNpyzIgbr2OJ444SXiMZrFXnK7HKwa2VQRD706zGTaetq51yEdmmqQ-9F1TtuKMGf64JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
