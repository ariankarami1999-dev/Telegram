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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #100</div>
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
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی.
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
<div class="tg-footer">👁️ 187 · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 796 · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 871 · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIc5ABrHhs6VsQM64JSIYwsUD0hOer6dfRgNTpRcaHTUMmwC5m-dt2GR8wjye69AOkAhqr7Mx1qtxacBh7qYdY3wvH2psylktOgoIU7EJaGfMiw2n0Ijfn9fuwvS4XgKHWS-cL-_KYeJI_BXKc6asWbDAUbCVbpj_mLwIsBuN-S57aY1I8hQEvZMuLHlV2QHDQ6N_BlK_YXa5vGddNm1GXd_zmAWk-rk988DgIi6JiHI-IfZiroLJQDrqycz6Bn1vDzSKW7QPINkQkd_iLYyoFKWSKvusZZg6-9UBYIpsrByX57R1H5QHxo1VDCjwi1w0Bs-ZOHYE8Lb4FpWX2xcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr_ANOOK34TYghfd--lTORI-R5WvEbrdx1L8SRuldj7HN2DdnCz_fqKb2HfuHnYTlw6wqqnipJ7yeIjnj8Jk4vpnAqHA0si2lRxRfedw8PjJyTOsjLLlW5vwz-ok8-Bcc773ibHucQfI6fU_-1om_UmNFyyLt-GMV4lWSZBvwTh5Z7M0ev9ewBMXzOMbZlTdwp5d5qUpR1pi0fCaDUumouNUzy6wwnZpN0ozaRh_tDPcwr_fu0qQqTZIrcMV4l34IqdsMSOmRgEGM3b8VOO_LwjQo8EgMQLXJlVIX5ql1fLikUMf3KRJM6Zl7b17y_xy4NNZ5Bq9pQavMMxGqZBu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7641">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CirL0Lo64gaN7BP1dA_xnbTIMbODhB87Kt1xvbUmSERwJCUm5wSMGvjYlcPBUJpt66DrApqq3MW5rwexCZl1NJccVAe4eMA7O7VkFJL966QuENtD6I5ZsG3HZHk91YwcxGn8QAT5_7DKtiMMa6DxQ7Tfh6HeR0qskMtBWicjo85DkFBXvRKPTAQ4HQk-nPgV91PwNuz8sKdJ0rG6azuFrfqB5PeIBq-jssnOcAmMSas0lDVwpmyONHjvzce6247e1VDrdMzuRViW4GtarKvI0Qy6wvxJMvg46TNiiZAKDWq732B_Xy3i6ZPsoQdm1GqiSh5sy-Jvzn906e7BtevuGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7641" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7640">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7640" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=cezzpr6vktNLrlubx5vHAjaflWa5PH6HGOaR_RRBqDkFtjwXvRit_ulFrVebZGejJxRnn9eL1DflHVZauLK3b12O-A5fE8rzFahS98FJFndRsfFhJdlMK1gmtT3JHCXImMddFyrAKKcrXn4hCndljA0DnztRV_6ZMYBYL07wrXF9lpgnXixoSii3vZEHTqHJZzERf0MNI_QrB-m18V8tOUtZ470oaLM3KB4UOwiaMB-vx5yYJJZSBHH-YoL140T8U7Tk9sah8hOsfAHYobpnH5EampXr7r_OTzVrH5YJ4pSJmGEATtL1ALTWiWCLC_pBnaAGuBUBJnB_G4uvBuo1Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=cezzpr6vktNLrlubx5vHAjaflWa5PH6HGOaR_RRBqDkFtjwXvRit_ulFrVebZGejJxRnn9eL1DflHVZauLK3b12O-A5fE8rzFahS98FJFndRsfFhJdlMK1gmtT3JHCXImMddFyrAKKcrXn4hCndljA0DnztRV_6ZMYBYL07wrXF9lpgnXixoSii3vZEHTqHJZzERf0MNI_QrB-m18V8tOUtZ470oaLM3KB4UOwiaMB-vx5yYJJZSBHH-YoL140T8U7Tk9sah8hOsfAHYobpnH5EampXr7r_OTzVrH5YJ4pSJmGEATtL1ALTWiWCLC_pBnaAGuBUBJnB_G4uvBuo1Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7zh07g96yOduQ3a4uHtiDH4Jtmo5CLhdFdN0j1CDL8opnEEecRj3Fp2q_8GAQxC9qLGqDzBq_9jmxCJNZCs9yYXhRyXfeIwCgUTlyRD2buPygZios8ZT92hhbzahQhrY5NtvT5YXayIv9n9YoBCH59IGB4Orhx4jxVCNIF57V1MdArZCVJFLg72LRKHAPY8fsEC110nLu7iF02CndXcSkPuTEu9SU5NaX0bg0EXpcdtfaICWJaDHjyeCvlJYsv9CiRa7wO1E4YTGnAKsgVk-N3oKSBnsx0WDduVpYK3IESSKJxjAoKMkrf4-rJyU--pa_BHkQZ-QrzSz_iQfEKMVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJZsscoRjfSgfgtvIJq9lqKFJZZkXYEsRHahukapMQKYyttelAMh6EpCVUCSHAchRvzxqHBZO3kMcKjckxDSQWZ8nd7RbSwzD7GX72432A4O1lrz2_lOar-J80k5fhiWryu5svGStIUuuABaiiqfiX03uq20eSxJsS_Ve4I-QLfM_oXiipNQhwvrwE9G_ul61_W2i2NAJm-_GMafziut3cIPv98RNbukU2iQyhYVjg0g9NmoH5uUH_eVCZGf1O1c1Jw6RLhODoFGhVhY5UAc3NhJwAU9mr2ZiBldpl9puJIiBqnu5asKEG3saFjKhEfeC6IwR-rfNWrCMYzonHQfiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksMmVaKnXaq6rC-YeLEDWCzE-7Z71ITMxQo52ErMn8fJ516mAcWIit5ZUHx0HQOV3mH2S27z3pEeid6LANNor-8O7Vw5Coxr-m9rLPNTVVOtPCzFgn8-Iz58tDSLHtDd6zTG4XawKporZFBgb2CojUtwpCWPPVOttqai2sp8gzNdATJtoGEYlPtBdHOM5GYDlZtvo2b0t7K20lzalurp0KNhBVjNV6lsQLp_O1BC6_oeA76DDp1dc1PKcoVbV7rNRq6XnQPqF9_qSHIPvr7ca6y5reNSP1Oi59Qa_liSoO_kK4awDIVlRX54sZgPiKcKIq-r8G5rNnYSIHPGOupKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiaMpErZvdBeHc6hHqBmeE7PR-dYVh9XFuC5pqtlGJlHZ1_tUJDjubNQx0Xw9RbqlWQDPaksMlmZoQzzBIZGTOjE7k5vawClBUcRWt0WB6Q09UanTtOMrl-ZrhjOmRXWR1QcYfY8VGDvzDBL7uIeGlFUhmayA-SaxFJjQWwpFaAdgtw8RKkq4wT5BvRfwEMG3oMZSgmEA2_JHFMJ0XMiHKmyGnpklDr1UbVFW-8gAw9jYeObcTl0vhJTyfj79psFSqjEQZzItd9Tgc86VHg2tFvhA8kBzdxeIVIRmlFH7iOG-VZRhQ4NKb8Rp4ngQ8zWpke_kARSqoBEFATIHvSIKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Lvez_7wnwD08SOrwRUcr8ILDyUBu1faqp1y5geLJ1kWp2MnNGWaR2ygGnPrUuD4zV_jxQPTXiiQmMJorEQ7QYQN-019gexfTbUW6bJLOxWRz8Q2MlLjt2NbzGIeNXMyGnodO9iMZlpShEPOoXSBRII42LFbETrE_CP7wj0iCAv4GgAPNJXWjmGKxAYvvgxo1EDGF0lwBakSqFUnmjXI10MUoTrvAxvMwykDgxkZsmwtwLioZwgG31xKewVl90MmpM9OhvKhibjFDKOAxOXJfcgjiFpmWDSPzysI4dGXXy2PYhh2DX_2uWK5qADUxy5giAy-QLwg8soalkbiTky6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLdc04lB9eYwqGaJD9lC78ZdEchTAnccPRHBrBKAuN7CaR9TpIwvB1s54UI9y58cBMeJ4lVw58KU2yDyjSYM2ecijWo9oRGI5FBxFbjKmJ5zkQa2ZvUfJFNVWI7z2z0jD_-u_oae0KzLdOx_3L4HlVmT_cSzNh8dx0VxYAKEDPgOItWKL89ZFCuV3Px_78-tjHj73dkgzmCb99oFNonGS_eZ5zBlo6p8OZPpaR4LVJQw9UH_4mQVYopIDRjxdK3a57EvSQh3LG_OGn6OfSZlsoNEJpmRSOS53IuaUeepO3Uj5Gk7oNbME4D9Gq-c5zhkB5GuHN99SpeWoTcaCceH8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx2RNNN9XC_Y0lTRFluJWnDX6ZiN767D4nF_ewMkM8vKSWK7518JSmQIKpE74BcW7XvCyZzvEfFLBIa7txEtwvyyw55Sq2TFYnpz0fSMZ7_BdvFutXh3p088T9MciLMbTANnL687NTd0tmRqGqIMs7VxYZM75eClO-5aJfQsvflAaBIIKGAt3qG2njS2z0BDeu799EGBN2BLRJW3onEyfzLaMiu-ni91scGSVEMdBeFzQvj7fLtfXI5BWmLODP4qPZCtoOoh5UJ395porAUe8g1p0Dv6FnPk2kdJOoFKfW3nnI_plSnjcO6R_mJyxfNZpaKr9-KhkPeoFE1HerC4aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4u8CXwqzlYYW_ilNjRQDhXpOsubncSc0gNRbjzFI5UfHBcX3Gbqf_KSl1DvHFM7_UtekialagC7DrZoCFeP6gCNnRyYJITtfcugDeYbBydCCOEpo1gt_ONjQzvm7xCTUbkoSXM6ha26oBmp5Ph4aeWzoalIcRC3bJjEf1thdzrqE_wRP8arx56sjsFs8orUYky1dS232L3Dg4vVQW-E8sj77eSa3ZbbeWpN4W_tp7jbmXy8xlNOusnNPN9U8GgO-kZAVio-mI9_0Bv_ZWNr87OGCCIPVMi_sYBRczo3Yfu94_TOKFB0a3YaMEkKL1pLIgE81cRR3I9ZoZ9IH14x_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcF5wMnRRLKQzUhWLZn6cGr-CqOB-XDTe1ajOtB6SzMdVYpDUEOcEqj3w0aW6cbvutS6MUb6FAOK8VOMb_GYIOq3onksZnfTHPZIeUiyYdg72V23xdAj7cPBbQwaps-KQHZK9X7APtOUDCh289dytb4quimN2tkK7oA3S45ntWM3HdnldUpa0rYi9bY8uRzkK2UYIRTYAlEIhcVf_oG58ol81kaptgTRBT4RKL0fM9bX1WIoO162TQkrhVwJWIUT9OU1Ig-HyOa-ie_lqrqhjD6awOclUq-Vv5cko6IaWHIN8zuIiSTtIVWdfh6pQg281yeC56oC51KPDWLLMpxwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeQnRdB-w4SHgnlnh26wb2GKvdKkb3k3IbK3uibIKDz2qoq8gegsN4EsAxPXelRoTD8Ni7XOKqcnR3f-Gww3p87VKfjvwe-UlMP1-mvYk1ZfjTXZChgim8-HHvdb5FiOXOEekfocjAtBPKqTOfz0KOvlhBRdRKFGjza_GFlSne9HJ5pUpGjmJ_LndzdNE5opRbXk83yVTRzjBBH8tU928AndTufo6LEELDEl-c0qx4MhqaQEm4A9ZrHfMKCmZIlcP8-ucTePLK8s9BYMJGdjfxT6pmLVVYCQXPZ7OdqtERlVzuc-TGtDX_a4DcdpBUE3nm20nsUCWmDjnYXhYirU_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq5l23s6IwDjpc3iyglDOnlqXc67yj9eZnAEvfplfpk2u8ombh8msijB0uP5T0X6AE_e9Jh9hHSm7h9_MXMYpT7tFf4IwRtxvPwkaqhoJ2n8TwkkcJ-PjjXAR6NoZT7LSnpg1zBe600z37eplS9xMuhpvh0YPyRL_hUolV-Q-iFJ4IaZcLh9iK9zUVz63UX-ZQn5-zmAqEsUWjd4pcKWPy15bhECMS-37PNu_eVE3MvzfAL9kCIf1GHykMGdidbmB9U6Wm0ZPOlSYeFxLcPsb1j0vtumD23ONA6W_cznoHwQRepwme_Kv0zeruOkSboZHtPv0Vznw51aDcSrBQlr2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVVuopZEz-crpRlMePZB3fnkF4YSZfQ1V5Dkdq-O_f9obFrqTLrAgqqMsJaYZEnI77LQhEMqaQGjhfphbbzZsP12pmTyHWDIfbD1mo0QNpCR8MS-0sZjAIxnytrFY3qGezC9vLWIV6E12WYsJRLTqOU2mTU2av0ay8lnMAlvQyyUQ8RDqXFUCWnBl7O_K7-gqQNWEy9AZuz_yJiihsDxrUp1QiYDN2ncVHrg5O6p_IJad9TESEmigAVZ8vTLlUPjbld5-VYdGEdHhTdHfWg-NNnKgQSIVmGNm8KxAAh5C2a-tkG4GMIWdBz-shZ0zy4YE2XTjgtJ66iCclyPl0EThg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJYHYTB9HYNP7pZ1WieqtLlmBZZ1OEQIMBQk_Qyqy8XzD7ZLFPdU0y2maVhROQwq_eYcl1pye3WJR9cqs2CGkCXAtPAu2-fsvAN6Utwr1TdH1Vt8vdtAQFb-9XWmk0imV3GOHtm43TIMCPmXtZne3v7eM9qbrJa0e1ks8mX2kUBspzxHebulCI4Vveesw5pNbztPH5kdp1GijEQpRlG77kM4lfPqbPxl3TlppYXvBJcuxZLDZkFq81g6lGMOwRL1yNVMb8pjDImRIMCxligRj_QaezolEa4S3sCH5xPt70Ioh1bDaz67q0rvpPxrnLk6GEy5maXsSmCD3hmeHUABJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChDRO_q3jHeyYWI1B8oNTcv-2niAGQUONxiFUVLi_uDnuXhsiIXErGKoglnA1O2vtwcuc1wvZ176Z4YnJNI8vAsgGjbs1qVFWKrTSWZi3BiBlavEJhA4JIuPbjPzxUH0P5c8HE6t1LE6BhK1oo305xUYdat4_KvNI0wR0TbF_Op-gjFq7dQu3uQFw6ozFcbvXFphkOjpX1dY3lrcvL5LA6nL9D9bNheV-2AIkeduclyjZr0Y-8ccfGFq1uvyTdP0G4ukdwUL5K17KW3nr_VVjMyPTx6O-rrkeDIWkzgbfVz1Uf0bQi4Ev4_MwfEvgLKDa9lAMX9RQcYrVegtqTc6ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaZo-BDBj6uxk-yy6rD_gvLwVlgZSkBc2wPiYcfgZzn_eE7-52HbH4s9aB3P5MtNx51vOqn72DKTRzmBmaqXAxa4gO4fhOY0_wuvgw__zK4rpYGpc65VpiAE4Qw0ytaQnxMcB_9bv32DhbX-W3iq7ztoJcAqaLjYTMWkgjGQEc6NqmVDtFyX9hZEUyDE6NNISp19WuOTblea8RIRoHZqV_FnB1CiT2Nm1WbCLbp5BzDxz8MUecju31_EV4Cmv5GUiv7Jx-FeZzi5KXCRSOS7WvblYzPVDEzz_4YpU5VWDGeeKEKNZdEUEL9jL4qHV77irS0v5XFeVLCe4RLEmGyjXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLBGB9EV4mjjDl3EhAJq8eD_S2kM8wF-LgBoY6yqrEB9h9wyWtOc6YH4yqhSTjNvhuV4NoVM9yDkzwAtl6huOTI28-xtp9zDB4ZyqKrSVnmMo8aBWI4NhYtwDiQQzh4D5pP2V6P35vfanLQIcSLRKrsDuFn3omyeC6_tq7ppk3TQj8U5DuDNBrqg-l5KtycNMGepYpN4isoXiHdtEC4Nu4Lg5KIHUdDn2ocJL2V8Uzjh-RcrbiJKY13HPffMZEoH0SeIg7iFaAKrMnsSYhssTSqjqv0UI4Ukfy80pu_HlbateXFG9kTebHZrWRDnbbO8ZP3dG0sjVbdy1XM-Y4UeGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBg-v3P8EkI4YKvMB35-sc4fE5OGYnDQc3U8XQdYrYW7fokxXljwlD4Wq1w5xM14CD7UaCEZnci5ptFrwS4KOBxfHhc6-WmVLlx59z16BMCoz-rSKu6RMouJ7zvtgH9bRCo4aTe-HvEsPFRrk4IdCHygVLDO5jKYWSlbYXM7aH464tCtw3thdiZwtwp2gLHT3_r3_wY903MEXCux0OTF69GS6x4vkJ5u14ao9AP0ZKtAKQfTHPbp6o2Slpy1pYOz4V6YpIUii_gVmSoKXZ4tsd4uVOShfjrqThJbCFWGlYEMht_JN2PCcysBtdI-JctLMPM7N2EeHSGcplKhXpRA_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLE7WYqhv1FTVDuYx9N-VxhuIZzXCLkeIJ3L06i5P_C1PCt6zmYAAc0ZGudAlbBPPgoU1YF9VgyENWPhNVM_yXxpQF98pm2J8DSFFXetAhppJ1nufh_JP1fB0w2Mo-Id46LazPgDwgh_7EUnl-SQ4nwqsW-zDMTruE1oftZczOubwct6V8jlPrf_u_lx5A3jKZqh66V-WpFJgxqi3D6Pab3g51yoa1-cN1jhv-1pO3qZfv3ijryzm7r2HV5Bg5VEg_5idPTXKnxUJac4v5UPLbrFqtA-xQd51DAQE515SxErVbmjVPDWkYezaKnHM3UWhsQIH11qN0LdDTs5d6irZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=kETI9xT-rViSpN7lKxFAWMGdBdZavuSrQhTmzEdE57sjjtPyg1jBRVkQcr6tJViRDrKY_nS6PmKHdljiZvghiISeG-SCggQlhoIswI3jcjMzpL-a82VGVh4ayDDnVLyjKBodCOZX_raEAc-xCY3RnAXMQNHflSQFonZPSitOcMnnaXl3bpcsg8XgLmxHWeHsUDmh0LPuZATe2ZIyJ_2MTaW2rWTgSDodE3DYjMynZMj7lDjIZhl86tewPpZzoZhEJw1vejcobYAgXC5pGMNRrWSUY-rLE5psUYQCByY-HMij2r6wcSXKZeCmEk2slHWLmVgSZrac9HbwCSBsSsd-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=kETI9xT-rViSpN7lKxFAWMGdBdZavuSrQhTmzEdE57sjjtPyg1jBRVkQcr6tJViRDrKY_nS6PmKHdljiZvghiISeG-SCggQlhoIswI3jcjMzpL-a82VGVh4ayDDnVLyjKBodCOZX_raEAc-xCY3RnAXMQNHflSQFonZPSitOcMnnaXl3bpcsg8XgLmxHWeHsUDmh0LPuZATe2ZIyJ_2MTaW2rWTgSDodE3DYjMynZMj7lDjIZhl86tewPpZzoZhEJw1vejcobYAgXC5pGMNRrWSUY-rLE5psUYQCByY-HMij2r6wcSXKZeCmEk2slHWLmVgSZrac9HbwCSBsSsd-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON3OH2jxMa7xGflmMNLoioKqw_GtGwIsYdVpqJBorATnehS5c9yst6Aux8QuaIK0z5MOm5_ElIctoIHIxcTJEjdBtVe5ejQ2Oo5EqIQFZ7iCABgcCAJO6HFePgk-a7yDozCgFzA5g_DUvyM27FALAuWUV8r6WTEqhvaXbJ4mB-m4NKbxKn6tFU6eWl9rbesTwrIaUXH5rUl-Fm2xlPkiPqcq021t3ULJmxNPCtfcDflG4jZRYcBydNMyRa2zm-NQ52MYP69x67MYO9hAkV4_USkctegnBXNazifAAzShzAWvL4E27gbO3QOblcNwYh3IKwZkL5OOU9QEYz_NLfxZHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=dBH2EU-fdOhHyqTu-L-kZO1b84cGpJo-O7y6rXJsBckDxcn52MnpXz4Fl9LvOy_tR8kUSsRd1Dz_j9BJLJvjV9UYsgkSsxVUemJi4oIl6L0p_y4MLfNkAWRTCo6-iUtG1hZ4nRitPtXPRp4zdWLsI37inFEHAuMBXe5J5MmICFPQDTD_gxmO1zkSPsiVQlN1xY7l4VCVy0_Uqa5v_SiQltDUbRfeCIEqTt6iF5X-dUJQaETlpMwAQH6_bzIy-FPDokskRhAPBXtcnNc1lMlWdW-ZJwaCF2Z2B9Q10SgXesqDxvuNuvGebsFFNR9rVNTbUZCnGgyLQa37s2SUwiJ8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=dBH2EU-fdOhHyqTu-L-kZO1b84cGpJo-O7y6rXJsBckDxcn52MnpXz4Fl9LvOy_tR8kUSsRd1Dz_j9BJLJvjV9UYsgkSsxVUemJi4oIl6L0p_y4MLfNkAWRTCo6-iUtG1hZ4nRitPtXPRp4zdWLsI37inFEHAuMBXe5J5MmICFPQDTD_gxmO1zkSPsiVQlN1xY7l4VCVy0_Uqa5v_SiQltDUbRfeCIEqTt6iF5X-dUJQaETlpMwAQH6_bzIy-FPDokskRhAPBXtcnNc1lMlWdW-ZJwaCF2Z2B9Q10SgXesqDxvuNuvGebsFFNR9rVNTbUZCnGgyLQa37s2SUwiJ8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwBPGpgb1lSBB5eCFd8Q8v-SLfh0SPhv09PIYpw7TKnobTeZHM0q_bI4cmyWz1-l54uM1RTve_lm2UJcQBJobkwfmDjDyvxpaaV6QGxGSeJsa_8nnWGxrSy_huVgbcKooBMrYRQgxvTV_-blsOAxji-rSOUd6x4o1UO-Eh48VgbadlIhDqY2zKZ4-tiME1Ut8PeZwjiyL0v9Pn2-D9ow0ubGWaULYozn8fH-YenoGAGKNhEpGeMgwJ0noBSRbPCzCafG-Tl8hQIMLNPY1Z272_J3HP8BehnOxytFtbiidgbEPpcv8KhWkVLL8V3nVh-AEZDMz2QfsmZIy63OF9w95Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET0RaCGra4-FjO694oSAxy8bheRS563JmuV-Az2Y-QQPORZo1_2ZNQ4OQAMaYlpSwbZf_b_uvhmMII8ZDEMK2sw8acleRDhr0igfJy7ZKEFvnrmOnnoBJC8A5dHv9RXWtrXU6R77GIN-SJoxVVw8NHD9isQbZKn502LeI0rJv-4YYqrfz2oVyd_o_iyth6G5Du3MId4fEj3HaDHK7jlSPaygRfk_f4_SGFz8IXl3NiMToSz2PVfn-hXaJibr1RkJ3VTSqWJJXMB-EEtK62gd2RQvQTy7e5zC4UyYoQNkNicDwmCIpjTaToeO75P7jybovEDKBnPzNcqmgS3XW8j_Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKbVS-aU9f2Ok7qLMsCVVojsLirtVbdr65Mds2cVshYF8YTrZI-ftIf3VCKo9V902_UNOA7j6qz1uTxmWQOEh4RVgxow0vCC8r9FaE4C-cN_wGtlOrRyODJBMr5VNxzxh_yusP3AafY8hh4c_4LAc5SZUtz9j4lBtxVu9oFrmtcQblIVW1ZfxmOB2Z7CTn0-SPw0DrqgbErzKnM49sefQC0I5PyDgg-jubxNgoaiiiCSnlckmmcYGHjWCdBndm2LWa_AAKugHmsgFgAXDNC6K6LsnDSExVQWJCC1fZmyBKkU10oT_4jyY21BoPSUe29t3Br5irEZiouIuHYFrg0doQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBNtiDZvsbzO3ThFGJ-riHFfLjfSTDV-aKUbsWk0tR1aM_dEVG-bnL6d3o6N_WyFb7w6ixGd6ZqiTCR5U6QVbm_L7XfMT6NCFnD4PcztfGW8ceuOhEE1oL-P77ITHWrCQWIVexTcQPXZgPraZertIZBo1jVVZfTqUpnCn3NvJinci-cCTu7zTUK8lPXM902cozKeKA5nrkRbHEBgXhgTbRd5MJHlsc_6BiFwGV9FAYDKUoo0UF2Rgw8bXic7aFLUCvIxJaxfKZoso0Ds4dtBQdzoi25IQjZZlYRf6qwqxeGlglSk4JnIqjGjEn_xEnyRgyxpexxtRDPUQAtGkDUcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr4eePoCc7F0G6Kyx1y5tl7TvH4t0aKfIUrxwkn6sxejJPhEQqCvlwSJv1G3klLo3fH3C4u4fjD1ut2ChO3N1w_NsETQW2Er2irpCJ0Rh4u-oTjDTEihNIqhyAjH7OFF5qrdaQ1sTcYSn3o_Yd1krszdn2A57RPPb5dKrLDq3-SV63FR6PSqDd6q2g4b0NkJHHwKPb7KzMIE_E-wqFWsCw4ycO6xQ0YDFcZ7MfDfzeKcdm_VmFiUXDSYN6MX_k7630K7HMoSnknPvVT3zRtddgUi8PJQ89Y59J6leL1RD-dpgUNtIhqrBD4dF9QVfosELr-LLDnhE_LDPfTv8A0B9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3RnImj_sHfKmfb4B11KHTabbE-gSaNzIhGImxzKfoyJsMleGlVMdnJxUIwuUD_jc7o9645XChURVUyXfS3LP9Zi17Hn6FDhwDTDaaBW4gWjXL3CQDf0Dc4bCgj6zZAdaJDbkPecnEk4o2cP55MOjVsoUo6enm1S93TBTzgLwfUN1fNFjDwM9TT5O_VBtwS85oN8GaFIyZJZRqq2JP1FBBDLXRQocLUIfTzLoYpM4QaITMCx-uk8cfzTpdGXj2hsYcoCXzLnPUpNRpLd-XMmfOZVW_o1ULcNfz9iONq4dTAavBHWOdJjT_qRoCEbVhVi1ZdxDqpZUVGW45p_5N2ptQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7BiutFEYvPj8KRCo-qAisqjtiirzcbbVVX0z_pQ_4MzPvBd03CKv0M9z8F2MnhQ79wByqd2nkGOjKgD4RJNBXuWYF4RSBvqNOSFrD1lqne5ZBxftmv2ztjAFUm2n0xSs5xtIfxqmb-eLIzvVYjiYMBdHYi9XkObdL8xatYgJigGfq1TGsgrkOPF4JV4awCHdIZOaeF_6p5BTxvBHqDatGX6AcI2BFi9sr1pYGkHDub3i16iZCDgngt4PQFh4onlAPyh6l8NDm0So43alPAb-VAJYCk9DK0Bin-o7oWp9ZIftBZcB4Kgx-LhY7XowOKGTBHDbUKZ07U4WNTnfC77yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5K21HkVYJL_9ivVi-XbxAYaMt5mL87NmWz8wqepFxtzd2WODCh0KIBWL8h5lR46dMKdbMSpS_imm1_oqFQVOz4ZmpPt3L96uRuuaoq1WH2OS2vDAwIH2mXNxPCwYXA5Y_dn-n8OSpS75wOyGl2bgHSWkXvCT52kSRI_hr5614KsKqAeGpeflIHwHDFMxi3J0IPy_NSWyJ67Yz8E-uH8qIQhxRTPrlQFS2wA9eFeCf7T7ABIG6j_rQx7KLRaPlYmlRH6vAbSNYMMlL09WPKhXHhuaWBl9xZa6025ZDD_tzxLLmjSPdm1zCW-s4oacDtVgbeZjZqraItgfeeLzeAfpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZBnb3eboSHNdV_q0OrwKyIWEh5iO8sPqa4ONKLU3552XYD_C5cezJP3lIEexdn0zRTNpYs8ayAtmABoe8GrzLpg37z-_dKLWMJPIBMtbK3vqrjAzdLEI2cZQ8Oj7rYp1bHlJA-Z6IiFi4s6nsU8VoK02c8ZaevgnOCSMnmo2E77YQpkDOUT-ZgI1eypX--F1JPdnDVAMTTAYq2N9GyQWfyz6oSrA-cVaL6ybI4XGNCn7J4m09RSyrA3Reiol2QoTVcmt36wl9uMekKUxVsr-AO3ZYIZTTsdufkQR3KPeKE4JRf04c8qZh19L7hzmYL28IcvWKT6xe9vcufc8WVQmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3gYf97xdA1k7CCCM0z3cV3Omemq9rTHKg8kNcIR8v2gxcnxKlLQKCZLJGVW7xGtEZlJMWOGO4yNMuIJSXF3XyR1fTCG02f35SWVM0FOx2Sk3uadxNk2zs4RvvXv0RYNvtjuPDIRbAZsWKzwWvyhp3ccxqCEdJyrATZnRfecdLIQAlhJXDnv9lYFa-7kwakMPgOJeiYXuU1Lkl5iNWhv7-50_xj-MTrXyijdpNdFw_Hby-7uqqCR4kJmNa1NXDw95MaUCHXYZRff9Xxt-F9uX8ZP132yJ4nzHJAWdMwT-_szyYGYrd9Ok8IUyQyZj_UQWK6AEL7frtOU2jsmsEhoHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBFnl2YWIx3JVU5uShHS2EIivtyXldrSwoZC-FrrN47u_yVTv3uOFLC9bHg5ZzZzNuQK4H2pUCld4uzzzLhVbkJkxNA7g3l7eau7_RRlcqJUNjIjF2Og8Z5jsaeeNSEbOoMwZEjgOHJZHvfQxozO4D96TBHxpcG6QbFAiCHAfbq4d-p7Uh8j9zBKGna9v4iDPj5wurJkTy24O6gX1mi440cBXDCzPN_EtEPFUUEOKMqMYyYSIG2jrVHtxOmcrssKVFzAgKf-96SrfV6UUNfsBk6r--tfuM147HloHseZddEZDNOjbpqs9N8agssYT7gmMy_uEf9YGFZM0hB58H5sEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_dWcOX_zAwDh3xuLoFO2Xl6MMM0dc7gd-SpcNWVxMZhrzGnOL-u4D1wKDGrSn8VkOWCt2gXcYo80mQUThuDkL-oFrzSEFCew6CGEiwJPZoTFZ5g2oGleEYOznUTwcmwE_WPxTsfV4W5rNMCLihIDcwb1zZMxmq1pESGS2DrGohXxUEo9uIMBiNUN4rdlX7b5baeanFB4HF-3x56Ibe8HVDUKlcokc9j4cbyaLsU6KkiMJRmzXI14Xl0u5nADgmlOh92Zxc4jkCnuS2bRlmYlEpQBKd6Kx1yTmbwZeGoOAWD_rFk4gJqsATKJJcpr5pXbxrK4zdaU1o1a87HRCiRCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf7aHe5luQdb-sRHy6pbpbfZYiEASQjvpBA9xfxz5qjSYH3B4yONKIsrJx-3vWxBrQS9FbBmpANdc6Z0GXaUCUzivY4iX1n8wl9PU5RCKDmh2NggNqQhkRxtzmU5b4eJbtFymBccMBS5n-yx0aYknEzk99IMPa0YxVE9jevuLV-obdboFDxl9xx8TBj6azO7M7OHr2UEniMIcUpkxK0HdE3J9bxhUP-qH39CqZUbrXcciTLGrx0eLKz6F6CnhfyziZ3zQK7xDOTV5xOoy1SGDtkgvyLRXbmWqUIECPtmWoT8uU2YiR5GaFNqO8ocElrxmf7HJrt5EekT0ZZ-w1ZbtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=YFD4c2TgGFsF_M5WFwvy1_BD7Hd7nyywk7im3j4HJvpEHOWDOdWccPUmNHVoopw4WEYroTmt2dWASiJ7XriQ2LRbK1ogubpkjyVdpNOaHrqXrjqQKEueIXaoOjBXJ9hD1wglzyoTJX3Qdn3Gr7l6x2f8OotOF_3fmiCdYwsLQshznfnBuGVI-Yr67hseOEYQus3ypCxo7HUh8kOU5237oTPuW1mxwv-Wv_pRimzwRncJBUHq3DAKkPQfcKy7YNAU9z9LA1SxY5qZf9wmPdvXiqwkMXeRQD6JUWozB7kAwUPBY-9XLvC-WYvK4j6Voov9eLB4x6GAE5bpEGIoCpZL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=YFD4c2TgGFsF_M5WFwvy1_BD7Hd7nyywk7im3j4HJvpEHOWDOdWccPUmNHVoopw4WEYroTmt2dWASiJ7XriQ2LRbK1ogubpkjyVdpNOaHrqXrjqQKEueIXaoOjBXJ9hD1wglzyoTJX3Qdn3Gr7l6x2f8OotOF_3fmiCdYwsLQshznfnBuGVI-Yr67hseOEYQus3ypCxo7HUh8kOU5237oTPuW1mxwv-Wv_pRimzwRncJBUHq3DAKkPQfcKy7YNAU9z9LA1SxY5qZf9wmPdvXiqwkMXeRQD6JUWozB7kAwUPBY-9XLvC-WYvK4j6Voov9eLB4x6GAE5bpEGIoCpZL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=QYLJ7YHnVs6-r1E1RU7wZgx2yTIsVwjBwCEHoSObjV7VxDWMiQmmsg1i0Nld9ydlZEn5EquurXIRgYqBVFBSaF5XbPZokZlLi4fzw3XyP8CZCc3IysIzqcyV5wI95FCKpQn9uNqiBgKy4YaZBBuNfR29DxAXV0Nnx3WGfiRZtDmtE15gVZrxw9mnMUO1ZJBui6S_Of8jznqKQFRWGN0dCvyv_MSoUq3MuHJePQk7vf1y6HZ51gpHzCbu05E09DWUW09GQQ10m0MoNuTtxnYbM34mg_Zn1Yem3_Ke3y8eSc87NRhDUSGx6kUXsuC4aUrPQuNVxmPtu1sKURpIR8-qaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=QYLJ7YHnVs6-r1E1RU7wZgx2yTIsVwjBwCEHoSObjV7VxDWMiQmmsg1i0Nld9ydlZEn5EquurXIRgYqBVFBSaF5XbPZokZlLi4fzw3XyP8CZCc3IysIzqcyV5wI95FCKpQn9uNqiBgKy4YaZBBuNfR29DxAXV0Nnx3WGfiRZtDmtE15gVZrxw9mnMUO1ZJBui6S_Of8jznqKQFRWGN0dCvyv_MSoUq3MuHJePQk7vf1y6HZ51gpHzCbu05E09DWUW09GQQ10m0MoNuTtxnYbM34mg_Zn1Yem3_Ke3y8eSc87NRhDUSGx6kUXsuC4aUrPQuNVxmPtu1sKURpIR8-qaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht4HlCUDkL-eDXdIyCS4Jn_yJRE2-6RHTtclkFw0Z-lPYHvaGvoy712oJ8N_OeXzxW-MS19l7W5Q-4DK9c2y6B87lA5WyHA_DqU73QovYO_uNzVPZbhGxeUYBJUCwvgqXYWSMJN0Va-wnhAqGTjXgwv1DvY0zkL946xzpzOD0jYzIcyf2oZ-Z9hWiw6Jzn1udIL--EhfYrkDrpkFiqyevusAplCSHHdch0uI-WVTKKfMhE2sBVU7K5FEtjNzXf1jsYKlhSS9V_4-fx55Y-RR_qpes5QBobvtswbxq0JL3r2aP_npsMq17EHk9JxhcpRkt00qhhZeuxQGida-pEFCUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_6YDEJYNoUVXdaHXAXJMMFGlIPfCgyu84Sv0_56OGvqGzgQe_ORN83OFiqSQiap42ufnOWy6afRgcgLDdAyKoP4-jXvtGTaEwhNILOF9My9koMAe726YIHsydErRTXaDQOFbfngGDpPucKZsd0wd_kNd4RUK5U_gtG4wny-yEKKtAimpkgI72uImMKunO3KWmeXj7p2YA4Koac99l3O9s2Cw_UbvdT_FXbZ5AULdFdPpl8pRVDNiOlHMRnh2LDiWu4ym-IHX2JtVCLh6z2Fy2op9L6bIIVNU6ynCnZoMaCEM1UBs72fBVvPFERtitdFAHP6HPrRWr_WerQETPJ7wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3vWoDneZpNzgFcKXrlm1BJTZSykH_u1DefU6kUzV22T6g_2NI8Ug_2klzF9A6KxNlEWMIXOumkkYLghJu0idziwocOZklDZAPYBFJSVYm0Q6VWOYPMuY25Icw0SigWzCvMNIwq9GwBeBXw_-D_UKFyy0u_A5wxKXekko3d3B-rLSfWip7piQk5y4CcrOEgO7l00TZRZfezjCAqTzPpWo0KZcKvF3iq0EIndBVjmy0faP37PyOk3CQ-U2JNjQTPCwW9wuE2_Zx1yxjDSOwe_0XMYL7XdoiQt5r48pyOmAQLjNeEziHhzVj0_tQOQWsDPmFwwzJKY8e3SdJ0etdqRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=W6F6GyXVlWJxVulcfubd4y4u5yXLOAsKjpLHED2sh1skR_GCc50APlXipFvII4DnVAlrSRZodaeujdr0uzoXFvEERhhkJQAfzM0cQvxzyHko0m6yvmJFvNJFWkOb3_OZ4mbL9eGvTicG7Hm1bxXL2VSI17X3VR5v0-SkHGJxxLOa8O8U4BOT17WjSZiOuzV6CLMy8kPeCkere4zKSKjyUsVynEli8qFW-_duHF0tcaQZazI-EsDe0_9mQEbBw1Q6nPpTdNGrJvRl67CzpLLly8hhmtw1-GpndpZWrX3jEi_SAXWL4gppVrY9NnR-4yQAE6IzjloM-u376B2CVA16E49fafHAs61ECF7-2HyXpE3KCoE22_NuDMd1BvfRV3jrI2lARnvr0nUifSIKIC-CvCFCn6RYaVpZUVlIhiwBBBdF6P1Ttz9_5didQQ9srshft8R6krvpS_LTcF8MrE71LDgMTb4Lo6v3JxhOuCwJfy8W7vZUOFL4NnDmfndOx7XSTzM9VP1uJNnA8Y4Zie36znj_BVa97DAvhvWArZYiZ7sF01odD5PKH_8Pk8h1VJ4yIkMkXlEMW1fMnpfhhta-nAVPi-pDBvvvNhCdkn0nsQWzzJ4Rz5Gy_k5isCv7q6e3rF8ddPR8YY9DQBY1y2H9mF2qDDiu6mdJJDE_YFU59Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=W6F6GyXVlWJxVulcfubd4y4u5yXLOAsKjpLHED2sh1skR_GCc50APlXipFvII4DnVAlrSRZodaeujdr0uzoXFvEERhhkJQAfzM0cQvxzyHko0m6yvmJFvNJFWkOb3_OZ4mbL9eGvTicG7Hm1bxXL2VSI17X3VR5v0-SkHGJxxLOa8O8U4BOT17WjSZiOuzV6CLMy8kPeCkere4zKSKjyUsVynEli8qFW-_duHF0tcaQZazI-EsDe0_9mQEbBw1Q6nPpTdNGrJvRl67CzpLLly8hhmtw1-GpndpZWrX3jEi_SAXWL4gppVrY9NnR-4yQAE6IzjloM-u376B2CVA16E49fafHAs61ECF7-2HyXpE3KCoE22_NuDMd1BvfRV3jrI2lARnvr0nUifSIKIC-CvCFCn6RYaVpZUVlIhiwBBBdF6P1Ttz9_5didQQ9srshft8R6krvpS_LTcF8MrE71LDgMTb4Lo6v3JxhOuCwJfy8W7vZUOFL4NnDmfndOx7XSTzM9VP1uJNnA8Y4Zie36znj_BVa97DAvhvWArZYiZ7sF01odD5PKH_8Pk8h1VJ4yIkMkXlEMW1fMnpfhhta-nAVPi-pDBvvvNhCdkn0nsQWzzJ4Rz5Gy_k5isCv7q6e3rF8ddPR8YY9DQBY1y2H9mF2qDDiu6mdJJDE_YFU59Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFhGV1Vara6MxYUDh61DSkEjScwe6Lmp-guJ2Q4mlCrGkVrOmKgbIB0UCGCjoYctf6j7VsNH7vzLvC_zNjSur3eTg-4FgnsX2ZFno_9n09bD272ai3t7j9_ejRYjOCyuj0gQZ-sCbitRHiHZDe8qsM-fjiCRpu2_Uxzq9jEavxPToMBTtBC-ZURp9QxaDmypCUDDFz6UiBTk_LKCeDR4BKUHwWper4_PTUJoWD8ELErbQiwCWjNH4xHWDZUN6swordX2p6iCxKX5JPnMdrBH2o7rHnhAhkcVEKX9VmVfTcNy2jBPj4_sYJ9ec_WOn7XKPN4u3QW5mNsO0ixqcanfZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpDK2dhx0KwEXZLRMaPAHt_Cj-6M36Pi5DMrB5vZ6bSCP-Mb6xmjHnW8TOGLhfVQb_9_YEayYckB8mI_A4W27tFtFbo91UYnxaR0nOVDHhfYyQi2-vN4yHzBFLa0xdlgCeKNc7RaZyGEzpti-u8NaKxWV1YB2RBBAh-MtMseZ079VmlEiQw_6niRQOLkI39Nl4zSlwauLPy-SE7zmS2AmWSARMY0nOZ4Qj9IkyghSVTZ7bz-6yXYZbS6P7yEX4B0_rGQpfq4DtRl7wRXKoTHhfwNgHZ3C3BnQi02tLYlnEmW7HTtUgDlSa1GBkk7gu5V6W-x7rSuU_gF0HgaqbFPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E64osHxUKCJNECqhFqHicSAGJsCCxNLgDZxW43gt2HY2eVj5COaMSr5I9G1WzL0PGO7QBUbgR7Bn7gfRDh06A6R1yzL5lfJePhKsay3FaR1iyUYsO2YXDIx3IawEiFF8PDPIo2RX30CBf653wbP-7YOMguP03fpRxbI6Y8QyHtOkxe7uJEbC1OIsY6nh-nKDx6dO9AqAukhwcFniaiGel9-kzcr5O3E1F4q2CRDQMw2Q9r8UtkznIwhraD-DxQyRyMJ59qS2u5Vm-jOl6gskpAaL9aAe4ThvaNOIFOK2Lpi7nOH9bT0oQqLznyjt0JAV_CezKd4nq-gtE_uCDW01ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjdsp8RdL0YL_zzEc_9LILLDvukiP3tXRwQkKh5ExGY-Mth8vbRLatSW_W7x6NUS6P9JbH6sKbHXF-5bShuRgai12WJOyFJ3auMxmPhF_WWYC0zAJJoM4dJNpqX4y9R2dKyX3vqOq5QC3B68NyJE7-oFf7bbqXUl52ExPx9MDyK23ZjWoHa94lPWMZmmTp8qgCyZdiwgx1sZiSmVMsLveWQb4lvWKSUk7BsnXLLDKVlba0UaYTFNw-mSWbCu8175RZTsdC4rba5a5c1ouFw85Y5t18RnUOaPP5ksRCQjhRv0wyruEgq-bsYN9LFwYPt9b_0eAJ7noHyB3YSlcBbawA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eksz314Y4syetJfxzrATuhitmTn25TWuyx0N_s7DAVqw9fDDndNGz_-7mMcOe3ZGJev9PLzod3TkTWRkBYv9dxleU_MR8fZwam57thyV4OsFBgaYyumYBJEMgTzQL9EvrijFxCna9vuiMFHSzOpwa2ZRSWl-Vsy3emvJepLfVWhpOfLKPGKY_3u_hPp_t0CAx3rONQrFLz3GH8f5huYIH3uOY_-nmfvjRcqgkljQT9zsJR_uFfUuw9UgvTcNOkd7AlgPXmpnh7WYZGJ-xModIzQnLIG63g3_KQ-ZoSHINx-w0B5jiOTW1R8tgjiR67EDqFxJuCDbC7cOj7ecx-2cOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCAR0EsL4B9DIaBk30Gf9Gmrxfffr_umQC66P79YAuqmMugCfhuxBoFMR-3noK6GObdq4zEpez4vtaw_C3IqmV20ZKNnge4SHCiaE6SFqDkBtqITFOHgqMNuNRs3MAOqbQpCrDEsMXmRufBjdivxE8lgjVV8yWOlQNBC4Uq-0CMqw1BO3qvMLWG4CV0Bs7ctfLd7TALSQTohCk73AF1sISeLUakjtZZRBj6GEPl5ieY3zslkc9gRsmXMyq9AebpMEsE_GM6b1-RQPGWxLEB385prsUKD8el9XKpo7bzg0hRkEVu4tYJvim2N9-DkY97f0kRM2Rl_jZbLtE_MgCGSwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=qaHJcSa7yiEXmM4TtgeSRlUkM18Kf0WrW4vddZLARyVj3iy7aTNBWjBcmsMNsD--1dgAa40426ymdpEXtHjPk3U39YnPB60-mJbFOfy_hF4y_NNMtAVw49BOdDnj2IyhQD4u7_j5ZutR8dPTdHwUvyis4lLnFMaooJuWP3o8IsBSIm_chl0E34Qlh98IrESXIPlo30m-P7hPgjdqMOI-gW5QjymrKkravJU6z-w2dSYlGErjcAydyBiCWoNIhW-0jqVuczAW4D8WOep54vJcYGLjyqdDm9BT_K-_5OdtGY1UEjXRF9Yfzcx9PxmsFGfhXTYYtsUxyj2cnR5Bb76fDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=qaHJcSa7yiEXmM4TtgeSRlUkM18Kf0WrW4vddZLARyVj3iy7aTNBWjBcmsMNsD--1dgAa40426ymdpEXtHjPk3U39YnPB60-mJbFOfy_hF4y_NNMtAVw49BOdDnj2IyhQD4u7_j5ZutR8dPTdHwUvyis4lLnFMaooJuWP3o8IsBSIm_chl0E34Qlh98IrESXIPlo30m-P7hPgjdqMOI-gW5QjymrKkravJU6z-w2dSYlGErjcAydyBiCWoNIhW-0jqVuczAW4D8WOep54vJcYGLjyqdDm9BT_K-_5OdtGY1UEjXRF9Yfzcx9PxmsFGfhXTYYtsUxyj2cnR5Bb76fDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUQLWyaAeRiCp-Asq32tgtstC05qpqG0HDvvAq0ipSjP77ctbXuqij15chfMBHbkH0ySAw3gn2QDshN-_pKy5hsLEdLb9i5ijOEidsqDwU23FmfzteZ2OCu41tZw-FBK360RxzxKQ4EVuvQq3eMz58WpWKUtPZSdycEwtwfdda1Ztf5ZR7LOE7N54iNm1uMTsgeHKjAaKwk2Pqd2XsFUCnF4CjmeC08JzU7foYrMDNnST2QdB4meqN3SK_azAQGQH9YbtpeN1gqGG3i8vqN0N9IpxMTi0me-g2IqO7mjdpO15anW94cvi8t44ZV7aQONKx4FWi_12xUV-hMGcaGVNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7pMWjlP6CIjTylSJjDWgend1PFlDzQTtYhi7voYKuiZjOqZC7bspxgAP5j2eGThV9FxZXLmefZC-Xj4Sw4jtt7GS9WxpoDs5_iWXvvQCdDhzVKmsGG0BEDmiBOechFQ2CMJ0ckHiLq49WwbXLMyLdCx1agCV26K38MH3v4HiCkNogBMZvjokeY99hIK8rv0kZXBb669WcQTwzN5dR5YgbtPCECNRGHGbnjSj9oPTj0SirY5uilJiCVWTsR-VqHjS4x0cHQiJNRasZm0-r3GVHGjR1YcN_u-07GRSzbVBlZLchLtIf6vYGnI_0YRtxu9gWcrmkWoZHujkSNzChjjHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMjnS6swWcQ0FGpVBt8l1BKE0QcEE5qJl1Y-Bh44hczld-KMAKLEPgTGFBiQbC5TQ7weKEuYjLU9iCDcGCe5WHa4TDJUFjZtWeAqlFNFb6giym87af4ipY8IihOQaDV67nNGM4rKg6caZRDevofSw2AaQ1UV19JdAdXgXF6MHPvCMBC8W7obQAOr6lAVU3XIdUG0sycBmRqr9Vm91D1b5wurt9Gs-erDEQH-TgiUlw7sYijevb85c6NjNecY2dT9uVxVEcp7Xi73PSRu4lfdjD8lnndky16mPsakoCa9l7rLI5iApoVNiffXr2Dor3IdFn1e0IC877Ro01Am16tR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awPMhNPr0cL7-DbKXIV46HFP2fYYZnHrVIqd72i4ZaSvNyvhCbx-0ood3lGQFqM4FG17XN4SV5TCDEs9KOJ9RSgiGT-r8d3X_5ua9PzGl4RH72Oj6x1U717NUhfmgvAgD28EEfM9WeYx6iVdq8DqYamdnhUvIKW3QBkxZ59-A5MOJS1hF4a7u2ZzWoyTfxFOMu26ZLf33e0ISCfydGfkVAKeu_i_NLbMqh1P3xXENubgqYO_eqtin6OTcYcWqkZVjAtFIjF6Oa9gwFZ0S2qXThbKyoh3l0nQ_V_z2NuIILJJaWQeXpPisaZwedAPEltd8SgkG44a6EeT58OcndWsQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikwgkto2LiQDEoEwQqMeROMPvFuqK-JEBD2_-ZO69Q6UsMhG7OzREiaJQv4-_s3g-9if2k5ZDaURx7mQJkwaVy6DoK5GV3pDpLZGQS03jIZiZYqZZLXkHfywn4oyai8lxUMqC3NSIzSyuTwJGdEAHjf4nbwKBK8urnmpL-mAEjVaOM57HOlcfz-yMG7BxuuvPlvkLnLp5hiwGMGwdKOcxmCWq753DJYkSK5eMkY28Tq8zez_Jmp8Meg4PoDkpF3bWJaIOgmMayy6Vi2VoiiIDgjrNiueQbbHHriuRxZHLbXQ_LBY1bfuWNCgeCi4qYCIqPZSSwv5FxECvTYkCEUZ1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdjwUAaPSbk-t8e4Y-_zv99c7jxvREfNFijaNtJFkj0T2B5c4fK32iGH7rA-lT36aspghaMw9Bv-dE44Nmt6m_IzO4Zr1wIBVHWIG3BwtBNKOfc1pVviGNd1MuZjR3R23DVnE1YFQZUjjk8vkpUJ-DMlHDE45Rxy0xlJO_-UOHY8Bwu5B67LSfgNMwyLeoJDRr579aY_qmAf09qbPIvz_4aepPt2rJzzbK5DnTRzqGrrPrxZRpTyl-z6tg3LShZGISAvivpzOoVIvfcYK-2msv6c08bU9Y8QBaaDEMsgRMSlwKng6_Ek6WKZn_MS8i-vr_Phu7ryrMtdpnO2iLLo9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLOHItcOINfGefnMmu4kWMb16DUU1zXXex-iH6gAucOBxtH6ejGAcw6B3gXLBCCxUtILX4mLGzfBRlp1wcmHKOkiMgfyHJGuPkpXLz7321ldlf-RWZAHKd099OkUMXAhVjM-t7clSld2B8IcvwFjHgvA1EFeKFeFgdaodKmO1jKjzt3O2Odz8IHjo8WHFa_kpK3XRB019RwZYVefcF-gDP7vvdScHYFCdpk3_s5hgxOUYdfbt24el46afkjp3T886LaYKADOMXRbjUqYYQGoZvew8TPvV-Ywr6Whx_lgngOteLdX4T_Nplac0uoeMBgJPR5IGLe1nhkRvqrCF6_sBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS5HsIs4BgtPcDf6ThxjxpEYtxtZkD0Uu35F2tu2kGcXs0YFu_oUehsJPPrjrBOzN_f3x4nTA6WGOamEoDX3Mbwua6EOS-Pfskts53nR76PaBd42fHRfl5PQAYHprp9LN8Jx5y2-dc2-IqqXhl5pUtjleild8lfIw2s_G1_XphdkRD23PM3JMCBpu4d9hXqsCEzDAJYA0JsFLP7jm00AZ1-wrH9HM-D8ICtFYnqEQgrkzuzWtLwfaV8rmGJSFu8L60YCjEGvNrTBQRyAvxquZOukNZhFdRLKwnwe9wlxsZYoFpKWx3bolLfM-5lzvCwuiyN1Se6rEAVdBq-xsa17Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWxrWSuajU_RimvFuYgP2xOgf1k4_RUy2J96vcw1LKuVdik2oPQ2Hlhx3AfuS47XDJ0rxqXVJuyudOYl5Mr_33ip1u4NayW-p7geA3LZDH2UZXWs3W4LFGGToFq7X-gLE2ogeBOg7UX_JizyvmZBcpgDr1YcSaT21j8N2r1FPw1_VtzlYRcdEn-XUwVxVdA-AY7GHor9hc7YdKQKXKLiUtx0W6T9hbfAhuRKuv1WK4fp_K2gKQh6BrOLFATyXoanCdtwS1LIwyZFDJpGQkIu3iegbEJ0iW2jWzZHNZN4NtCjUnhnwIIHYqd44QNf-ocWHvSltva0h6sHNP5oXOm5ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=FomSIZJ5JGGsCz9ICh2oBLPPGSlh8cHPmg6zyv7IEv5z8DPiI80lU3aSPbf6MeKqpsYSkprM78sbktbcjMN7esz_QCH3PlkEOFR7_qdwoOIIaT8BCELXzcBvyarMRZJepW5F3aLnRA-5zlXB9NaeIUQnfTMaLsFFZ8xMdCjCgVZKCXvJb0eO718Ibao0cPp-Qrc0Q-bBCep5eUR2ZxSdJW5Gdag_burCGee07XjDH15szooijZELhH_ZuAlAoePjhnZVBLaVPcd1kSNKczfRPGst7XM4PhhwbaKtF-A1eMDLoBl-btq9vimDgnSDJUCsUC2SBqQVmdnQ9KROe2D9Q4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=FomSIZJ5JGGsCz9ICh2oBLPPGSlh8cHPmg6zyv7IEv5z8DPiI80lU3aSPbf6MeKqpsYSkprM78sbktbcjMN7esz_QCH3PlkEOFR7_qdwoOIIaT8BCELXzcBvyarMRZJepW5F3aLnRA-5zlXB9NaeIUQnfTMaLsFFZ8xMdCjCgVZKCXvJb0eO718Ibao0cPp-Qrc0Q-bBCep5eUR2ZxSdJW5Gdag_burCGee07XjDH15szooijZELhH_ZuAlAoePjhnZVBLaVPcd1kSNKczfRPGst7XM4PhhwbaKtF-A1eMDLoBl-btq9vimDgnSDJUCsUC2SBqQVmdnQ9KROe2D9Q4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
