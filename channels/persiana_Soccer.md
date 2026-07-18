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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 14:57:31</div>
<hr>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxb19mj_Ive4DUdSsZfjcOaqOoIhSO98PrqLsM471ECXC8uXehtSzBMamuQtTRRAc3F86isAV3skG6ZvAmEytcsqdqAt8Ru8GwVFZpk5XcQ6kpaBz6d8yfiMOmXesrNDa9iQ0dy23ByGOHOS-0BMfDwI3aEIRKOT-SYQtyF_uinaPppNFalge2tMizF1aWBatYjSlGZhDO47G1d5u2lVscpbBQ6utl_BKDSAZ-3rqUjnFWxcqmMnNaUdCweDTs32T9-qLXaDuIOhYWhg7fG3oFiPK6ivcCcPYAcaBWCtUoDqt-d3QIflfuLJagDa0YDWAuFsB0Sc7w-HsUMl-fTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp5DHZdLk7b4hnn7zRpL51RkFFyo0i-gIHOUe4Bo8Q6x5BXtcjf_rC7jye-an5jTVpFT4zMUeL2SaV-sC9wpd3B2fRFZ8WoqGcyi-lOFoDbVKeu76fXNGhlLFqLAciGlbY1FqHPUndGx4mNNtK1jsULa2HUeBgz0UChvaf_7pUudT9LTICcKu076gRIcI7jMDcfpTRCOR212NVqbrGUY3jP-yxyE5SCGdtaPxFAOpy834JT5B-fyXT1hL9sXTLkRek20IxrhKLtcbLO8nFtJ4QWj70R4HS1i9OtupS630qIpV0wY1Qks1ePBO-RlWwr8-AW2_ThTK5Fpd82CWCYLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFab79s20IHbcdme0YcNP1wzFTGcQ3-4SNVFoxCovKDm8jDv04a1Z7Y9UsWUIBJ0Fw8Rih5JTyn53lS4Wja2vipheLNIPtkpE6nx2I4xz00xv-Dl53ieqoKWT5wXpjQwKr-4BVCz-vbLOsKd010gjpsC1OD_CP3LBGYKFlw2k9ifOtP806sAaZn3XsRbcvsoepMdolLD1VTxCRMbHgTr2pHhWsFD31Ie6Uffc3SiXFnsakl7QvhJjfTN7Ur0_EAgfalBYCnyOA0IY0QMPd-gqBb4qjEDS9u977g3KWmuJvK5Tc-83j2wDU4dwR7wIF_BjsYJXdnDMVZYMuorGQq9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl5rvXXabkvRgJvwWLmDlR5RYgqu9jGToSKDh_JJdmgWf1KabqdLdRb3L387T9P3sRZEXBKJrgdDeYu-QLY4kjystEOjpusoF8ePC_auteCFhJlrstGo5QlP-IJQgUylTkg4uA8N1SEStMVV8h78uY4VnReYAMf1zxkPmoRoSuG0Nk8sDe7AxhDcDc5fawknYSEwBhZzPOZdCrrz1iW22sAdt-fQFe8mSPOyFxrBFve-e-kwGogYo7-sL9-9lWPxDcAA8A2eXxf4JvpARkUjz_NIg6EaHDECQ6dTUPjPHvNafHTSSyFMIUogrklOVF8Qyuvm0xsSa_SMwtwGdrGBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB5SqCnaWBlgH3PVcuI5iI8Xx1Bq8AKtjA42bXQfGZmrvKwXHl0oRn_1IUosPN5r_kAR5qitf_LakcfZ40JNleQ1758u13JZ0fhrDVPUxgXqQQ517z4byUy5RCPSKcm6DdZAP52YP52iGSYqDWvVTc1l2tYp-y4-WJ9D9kJP7THPxCLh7to-uoSGzzOw8s5ioWt9RJu0U8RsBxtlNVXB22PrA7y06Wim5sksj5ru4Ylzi9Zo9kOaaKkoAdoJwuid500XZvG-oTUkqYD-H3gTBlF6n5kDFybSpnju97FNzLmwcYFwPqPP95D6Mk6WIcgS_NeIJBWRxnN52S7dd7NjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce_57n8xP8fj6w8xEnnhaD8iWEYuRCp0E-WCZ3XidBPWcYE9A4KO5DzTj2kMp3RmlRGVhdLWOg69kaRJaFC9E2MlY2lntAJUWOnr04Y5OKRFQo5H8_43XzCaDT_ZK1GJLb6UBShOxp_tRxWlg_O0zWSrOEo1p7RV4qmwXepkfaRI6Lka-9g66qdRK0q5aIdlqCS8p1MU9aNAeXa6IlQlvDqMAjOHVFGw6vu7RDnvSnna9SqSqZpWHvpvYgDCQkbyZT5GIYWsxukJvxDZlhabWmQQG9HV-vjeTIlO4RG2KOwpv03xlULwUYhRbNTx1lyKwLTdZMTQWJazerOHBTjhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPfZ-4_YgjAumi9rYQ19hCSJ0NnRQSrOCPOrNPCep_t2FggqLUSFDyorZm3dvcB5jP3ZOjkm-gqUgg_o21Ohl9dh8Iw_3NuRmcRe5EHs-_7MzGYBDrwD9Xyc9REerbMdS357OPlVMtEedMRTUyUMfvYo48HIRyGq5szyEvyvgLZoM_Bqfd-Q_qk2Fjc1dohk54c7xqqlnu9QQudcHdV-zMsFLtqbHQuyh19Z8jcMu31FgqQBRVFUXP8K4LOuy_ULpkzUJ5LsDBGuAkZBNXxi5dA1lmmMByLF6Yz39JGEKxiwp1zC12gahQpPbUjNdBQbgtRD1fcrH2j-t9UuAO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVc5TroZW3eTXjs9abQ-L1EszDL47znjY3hazgu2Pj_z30GcXB52lX8OrSydC9LVVXtq2XILvlKp5vsAz-VM-wWG76DF0l2STcbuA5AAx3_6xvQJSoloroHnaamyNDKb-KeTtbZJTErDcDyD8IYi6m8sqwEW8CLz-tdqgZsv8fnJJCsYxEa6xBVCC-qURAvMyqdyXvxk4IZo86KZ1fj_Fc1_O6YQ4cFaIp4aoLyirG44qUP-TSuq2DudbXM72_5n3dpzHKRCTJG-7g3jegWB_kXkc03WAw_3bZtZ-V-9O7lqE9lhEpVMAujUlPwPYu-GHBi2wp59gZ-fpPhI7YtVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnN1IQg1SXn8tC4h0MKvxcb0qkmzXNtqLFeHQ2333Wtz71zUz1m36Ohjjlovv3kWqIPaAcXogjaQAcxM9ghUxIIRy0ah6sL_RU09I3SdcddhLwOSD5YJz-y0W86zOqQq8MqXyS53DwzUUIHNpec9DvMt-M-OUIoSSUtNCYE9WXoSXoMuUosiFiG8XKBL9MMcA3XRg388hQBRHnXNkR7e9YrZHxsY3_EHujxxgmliu4AjtehlY33RRFuElrZPqzSnjElJcnmXbTBNRJIhfcpxv_UvxmIrYAC00IZf9tZOKi9-2pVeceLFuAkvntWYIYXc7-lNyWCWnaQh4BTPPGuRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e239GC4BC3IjqDOipMysJQt39GxZ-wY5LVRx195e2iGyp30O7C_eOVEv5D3GmSR69GAkvIcDTeTYmEJaFu-nZ8bXRiO-E33Ka-3X9ZF2EzNYUFRIXi8V7rq-WvufrJltm8mQlilCDPz805TI-R40qNhzh6y7VJ_wP5UBLBdb3_TjMRT9fCwlQQDpoT4aNBODPwhfeY6Chtye9o-V-vi0rxsfQKunRba5kPnNXIXuB9BFVdQtM4D08BkQU3zp2M1DuQRkzaXafHAGovApQGuVZPs-yzRn5kEMJ-6H0h06sc7NPITJ-sXtQR1a9IKorBLnZUmwRKTGkU4esl0PvWChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6mHlD_svdZJkjH_OHuGoU6DCKql7aqP1PM451Rm2VvyDq0VW2_0Pij2vsdtDF-Hq_HVz5ip45eHSatvzffEkQ9u53ywOVxsPjIQThqFKIjjw-gYnS7WvImC4xND1-x4TgYxwG8yCX7UUVhpLoE0hoabVSdrOv9y8I7Sty7WbyWxf8rSaSFldfFNpG_SuBBkGJDgn6mM-9UBVjEUPYd9XiCoxpqVqQH6RXGldN645FU0lf1hVWduFKqIqWD59lfES-djn-1LN9Qm_8WJ2e9FaRN53YX86EEQWS7ouVA7jPPlraamMC9iLFXZu4OzqDWiIqXmu0iUMLo60bg1CnSixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwI6XqoeL7xi0vk-ZAW687-dWSIRw-2WWjV__ft3hg7anvDhz02JHZQirZsVDV2CgAL47iNU3OTYFodOuyjo7QLju5CjvxffpmXHwkBK7w754dB0yBuzwxfAnATRjUr4qSjHRzgdh_EwjIl5kFiPKZQfG7_RGZpywJS6FB8HRzdtjjY8rBAGUFVJLkLOpdZfH6TM2GqGklTfi1mh7Zq_R5NPYIjsauQj9vxOk8X7nQb0nCpSUBg0nbQcG7HCeP_VgG-7LSbGNb9o2e1KTLnmm1YUNGn2iTu6tZlTey-Nentpdvl96RKuF3nKm5B0qmzuQKNhKjfJ7BjNVdS4JCLamQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZVuuOr7fEuWh-p5WCn4C705BhE5pcz0iAJ_RmR0HK5sgLxgJgBIlw1Lj46Qg_YFAB-2I-_jCxWtvpZMrBDQsXozmMLob9NCL8lAor2K2RVGn-49Is_MQHfm_ynBz3mTpurXbc-LY_hT9CN6eMN55MIUyBBUwnI20GU94Rzq1165dortjoS_dcxgYxJa2IUsaiT8fvHnb41npD3DuCsl6gnDW5wo303hn9Rc6EQNcqA2xZanjOlAvgVPa3z2XUNLot1MsCkwmC-0D_WHFbLsPrnEKAd3XIDHGr29cP3NUUYzVFI8xGBApQ7VJcvWXZJ5mD4xYT8RI796OryVNJgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdCv-1SYJvM-X9-VWHQWkAh7iDBcwMQcZz2iVNsksP9Cx8ssg9Ez6H_Ol5Ebv1K1bDoz--55Oxe5gzdrCE9z9ZuCXb7KvUUGLzbgDv9-kQl9nBytLwg7Qs8ozz_c9pb0HMRs0QXBgGHvbuxTBMfA-Ai1xIwA6kFMV8ypvm3lVppQrMnPidfRTJCfOqw4WFu2KkmMtSM_BOS7NTZ6SrTUyZMPdyh2sFYI62TilhTaGrDezrScOO_rkPO3HP9tDvwb8rf2t4y7wnu3dbok-VhBsrpDMY7MLhFsBQqEdk4XiOzsd1Mw5Wxtc3EQinzS0wVPcv0fjo1bYUKxTxrDq8s1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGNyUBPLP50kfBtnMzTpuImekYJen1q3J7RScCP7mcgnstCRFprR9nAYR8R3IK10yRebufCsS2dNi5SILG0jKQPwaC5IYX49OkuM05hPak5ktbG0ZdgF9Nu67NZsvtkCAPASQSA95pXHeaHZ45XntZ9UQcdB_InczFGLOpWcHbhrHIY37EW-hMR0ZNBNkOjiy6oReYVzXT6yM4POVIfpdJy3IlttMxu0cu0wI_FKSBqC_DeiHIu3XAULGKcvn0lJJThm3XQmfIb6Qdvknaw0x3sj-Hy37s5fzPpN-HZeTONwBBqtIPZH06mGI4400ocSm7AAz6eJrBGdi-mUGGKd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=lYgVwGGNZ0TbO26RB8ChTRfY-e3H7s21FYCY3cJKNmxKp4GClBYK_u3BX2vZlyfG7Yv3rZmG9ubW5NfNZjsm9P9SGNHWzZcjs-ZWqi1njD8mT5Hb8Jw4hik9ihAtGBYjbgFO_1TT4vUShh6o0Zet1MJwTFANlkhYnAopMXnED4iJQSnvNzX8ER1mykOf6UEm7iDzFUox47q56MqsMS9M9SnwB2p0CWUSBvQg91WrBbSO2bZUpZQhJ6swrlREI8useAtTS5dwiqi-ahLxa_mQo69bj5-sTQaajUO1anixdZFnEziPuAyrmu5QMhzriKXcZJ0wKdniWxSRkKmVEmnEig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=lYgVwGGNZ0TbO26RB8ChTRfY-e3H7s21FYCY3cJKNmxKp4GClBYK_u3BX2vZlyfG7Yv3rZmG9ubW5NfNZjsm9P9SGNHWzZcjs-ZWqi1njD8mT5Hb8Jw4hik9ihAtGBYjbgFO_1TT4vUShh6o0Zet1MJwTFANlkhYnAopMXnED4iJQSnvNzX8ER1mykOf6UEm7iDzFUox47q56MqsMS9M9SnwB2p0CWUSBvQg91WrBbSO2bZUpZQhJ6swrlREI8useAtTS5dwiqi-ahLxa_mQo69bj5-sTQaajUO1anixdZFnEziPuAyrmu5QMhzriKXcZJ0wKdniWxSRkKmVEmnEig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZz7LTCxOoPh-FBOkWmE_ILss53q_hCqrJCZaOUo9mZ8zTDHlAH7Q1x810H8fNI7ED4wv36-jXPai9oilyElNZ1Yx0ke8vZG8pM6N2qBohLgf45WnWwEl5USEgTZroEPR1QphYrYmzlE26xYXtCK-Srz3fRpfnvKrSw7bSfvuZT9a5GXQVIqRZqeDDJJmkDw8ya7L5trlcAQDnuxalSuCGQSU7DlI9d6Q50833AQxb8rufVrskaVGAk10_3XlZZa4voOcZfTDIxCeN3lwPEyDqljCgbkOugPSx28l1mSQO7civWKc2lGJAaYAwI6PKEjn_4O71TX2ji4ZsgC-Eeffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr27
📩
@winro_io</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-BnDUvRqosati5qeGkQYx2Gpy8JlXTRxG-7lv0eKKB8iLXAygK2tUaBioCDA3WagbpaAjPcyDaaHA7qPFu3elV75hyIHw_b81rIP1RZtiiDK-rBPHCxlfnxLPw14_Pl3bHmCBUy2EeLpeAQj12TcJvlTwkBwnyoOSpohY3XacpBurFWtEjT3more-gB7_3TCWHL8njOAtzeOBLarmNtCNd8t4feuakHsh18stH7kvvUaL16R2oqQrVtHAmXo7KTJ0YcIWXRghSDQ6xumRK-5MtFKGWBLAxYWifserP2xM_n1vFnWCD3r1HsKIgv__CUWCa6LCsL44YtGw1iB-TUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlYlHb8XzvaIxsL9w2Va7XnpRwbTrw4q6AsgE35qKQQu0dczO4guMhDa8h7DxsflH_va7TKlbKuLCCrgTSYG84dsie90KJTC6zHe-3nUD9LU7xHDOYjR5Uc2o5YSL1te9H7eGp5i_dxqaO9hNtIRFzFQf4KRlsEKgZLIne-b-RVKPgC2Dv-GBE1_ZDpOY7naE_sloQjf7T8AxVLYhTqBkvLSNJ1cbQoDS9YJD2p7ZyhEC8rF5PtYmmdO6VLmOyPbBhjIW2eBDqG0rv_a9d1xbvNbMQS9ZIBRHOPBArrPSLB4E4WbdzVKQRNbK2kLg-asGOWWL5OOjaZjnxyajBmLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR5gai1hTYJeZ_I4cj948nsmRGLoxiUgFfqEjt2m1sxSu2q4lHho9IOtCoQNRhM4fkKxNlKv0eG9JQM_x2C8pKwkAgIpgXza_EqDV2-hOJEWBhSlEVU__XE48as8mhw4JVvyhYI-ccoE46XUfSEI0Y0SiumI3T1gxZ-s3E1vf_El0GCqm5t2DYuC5CCvXRSHa6k1NhzfXRASaKkzai8PpNPpQVy1JUDwVxOYITIEjEiQB1xpPgDumaNzTHSClt-LUveZREltZOteViQD32S9mw_w7NdHizMjLqU9MsF9qLImErIJJ8pCzGJKFwg4Uox7hrACywWgsEQ64BNtgFKVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui8_R_KVkR8b7OyOC5Rq397-Xi6IrS46Kkr__9GpV8mmkNZ_JbfD9XMLAE27ma77O2JvlSz-4FHZv6FZ8UC9guB9YBFFYJOnYeC4Ap1TrMpNlpe5tckjm9sJfkgZh7vkSmqUElyuLlAhV_E7im0SC_CIKjByqd7P5KWK8KGRI8IJAw-7v2l2Nm84u_vL0qOTvQPX3PxtXpM8jehJy099hKLVItFiv29e4dtr7i1z2MJBYa4jBohdLauvpEuzw1wFKuVufsZcc41gnKTIaAbjBK1UMYmhXYCqfjlTgB-qoAYG1pGXhP0K7yKkYiQ93D2uhvyUmINUR21D__vZpDpGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwuYRNa6cnT9zFQIrLlPMUbGR9nuDDTM9lJ5WYB6glM8Zjuazz0LggCb9OLlUtlsqBD-yvXsrWk3ywlqxRQb0EnLWihjQcD3CjLyqI8IpaNxVPcx3JnnnBPug15LW_dEHTyK9u4oVrYF05eCA6d0vg4owAp45f5fLJy4PHeGJjD0wdL54wQm7tw5-K-HLc0yblApF6OG1quM7ykHGl9yx5MHd2Xyoc55ym77ViBK5wmm25-4gJALHWe-Trq_z7ro6BCbyaYFyq_sL67tFqhbYMa8Dz9MLKACYqKHrQHDwB8wUt2In56K_xBLZTD5CK7GLi2IpwX7gphAlW5ytLd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-p75RkpeshXIgRwnFibdqKjSKEaMpyqdr1sYoh1uf0KKj-4kKRl7Lvaa5vBKZYzAORxLSJFX_TT3uX6Dv9o6qbZCeMVJqi4uoVDSOfBW_09gjDOZBD9VowE-58bgh4oWfEhXf3WzbHn68dGtCievgOC8knJLsfvFuZXuUEC3lYI29yCLTZ5F5rX29BW1dzRu-AhYIm8CfHsefCyiiYRyjWm-3WOOIyoIcc3Wz7B6XqS01bQcgrGc8C9udjft1mGlsTTK-hPbAh91M9hJ8CH71cqZDGWvqMWEKoLiDS8BbJzLklKnG82fO4jqYePcX2nib6M4kGBsbJjewNMxPlw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXZVcM6POZolmrDd9b7HeQx3TZnG_s6iZfOjvDpyUdtIkMbje4hhnMRUy_VYCtq3ijWKAZlXX64pqXtom62X7wIfrliJONLPjz8tC-c5iMv9uqzHS-Drcm9m4-qUMAVKXys_UvAfPBfSk9DhAuQssT3Y0A3QSzV8jbjZqdOly_JELig1PEU47Q7_sfEb13vPUMEurxWqqUBEQgo1ced4BqIKPBOQ75Ro-4dm8vAudRQgFZGvjQIHt-bTAKd3v0hkdd-3jB0l6PRd3q9w-tnIDMs-RuLbTaJkfPnKzofwlTuCCL19XJ7jsLKYWbufafo3ErcZwRuJ0B8cmLEPSRgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eke00M23YA83nOZLmZT_azxkg5sl1IlOf1GGszyzysK_EHrIjhrBuajxt1e5jaSrb6Si4hctkMr7fB9iQNQFlGqNCzYCzexXivWxh7kDE_Z9iA3I9IwxCNDPQLCrP7mCpRnLBo6nLhxTDY1XXZ6tjSERauYf4ng95rL6mTQj8_GFN9o4PH7qnWbV_OE-GQ7TVUWmI-GdrjHfi_b7uSexMEfkm3Q5Ak-mguYqCgtBV1eB5G9Qb50FRyOFUcVMIQZFzRUGkYS0u3Dcm5SPChZHRl-dq8AA1AGdMuCZwmlbLcY23xAx7sHCXWIGkaJbNX6HIv01mjkca8gPV1j6vyvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBdYO6xkIu0S9-9hoGCl1iSbuk-8ELDB1f3eXTmk0b7HbsUzvjaYh7VMbnJnvo5JDI_PVnwPg7BAgf-rSjJ_oai_dl5TezvVomr--Nw3pBH9EOoAM82af4zykWLRu7cTcIrrZ9mXo9rdaUCtT_QObg-V4Yxn-F1RJbtedjHoe83RRY4_T2UqHdRwKihY8se2HsEEnjQI0y3X6MnatkPd7zu_YknYVMNI89d0iDDCjXxnvg44-79KVUEF-98HhamoSZiLXiJWUdAvYHeyBGFZen92oNep-faYfWwkeYKN7HRsaUixScXCwYKFj4gPxNkhuDcw2LKLcLMlCLTwxegmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=rWy9SBtw6Og25Wnf06PtIRRc3Ncb34763HG2KFqd0aj5vsSKE4zp-S1biMSgeofAXLnO2Jfajul2Nh5UFNsXurPkHTLrt_xWeTO0EEgGryRHLqWdOu3Mp-mGiHXKvF0QXHPlcClBX-VPy_WXGo8cGYfBlweeGyxLg4VjjGVlQKq41N61n3IrNoZfZ2DwsiZb6YC41XrOwk9F0Arqto2rgJ0fjWQ1HEm3ypXHXJn22Un0nF3Cpm3tGiVph4aNw1KqZVjjUyf-hpWKLYlywQbWnFS5JtYCefdPVAaQJibLanVtUgqPgS3Lb2c9dJ9kEwMqAW9NwOznyVo-MRulMppAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=rWy9SBtw6Og25Wnf06PtIRRc3Ncb34763HG2KFqd0aj5vsSKE4zp-S1biMSgeofAXLnO2Jfajul2Nh5UFNsXurPkHTLrt_xWeTO0EEgGryRHLqWdOu3Mp-mGiHXKvF0QXHPlcClBX-VPy_WXGo8cGYfBlweeGyxLg4VjjGVlQKq41N61n3IrNoZfZ2DwsiZb6YC41XrOwk9F0Arqto2rgJ0fjWQ1HEm3ypXHXJn22Un0nF3Cpm3tGiVph4aNw1KqZVjjUyf-hpWKLYlywQbWnFS5JtYCefdPVAaQJibLanVtUgqPgS3Lb2c9dJ9kEwMqAW9NwOznyVo-MRulMppAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMjhljuRqavQoh4h0qkuQmrfkfZMHFEhq-mj2jGvczhrD7SHOYBcbsEfEEST9TkyG14sSwiZ_XJKPt_itvYCbHtHsXmCYyDlpqzGVpBSe6NMYl0PpNva55rNozystNncz1Xh5Pc1nmTiTFZz5nIubs08BdFD6AAJHdHW7A1yMAGhKbx_5KpyvUQSl05iVQLY6-nCln4m8eWxiuEBiFji2eqgmb1y6S7Y4Ec7eyUSEwM-j3nIy8SxnPmqkR6yTcmr18m8ifr-PITgp6eaYhi6WwPWscHyhsOFVFu1oS12nHrjkZZbYGq4GKWJjbAmTfTygPiJcypbMPFqfBz-al6bLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPT6FV5Z4zf6mzSX40tP-wLNgnuX_2aMfac6lKOrXYFpqxjg0awThJm1MwOk-LSi8gFoELVlcMINlzg31c_Pl4tkpfIIxL5kX2yg8JuNtss4ceQyGh5ySM_rdRueZFjFikS3HMnKkC_vOEq8EIomKG7j-JtCdDUomCAeyhNb_VHIjtwelAkxihyvuSYohY0EBIJX6DJv2I_DxEDccP4W_-mjTJCMrJx-dofstdkA2b06u5SR6MDl6-D0wTo5HdMLDqcr1ELH_PJuuYasBnvplJJjmKqIAt69Ujh8fmhkITxOoLMdl80gjTJzB-UwcZFQygd-mEAYnvsvZzWNxWmYTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=qZXVQJbUFYbzreu-V3Yi5q4eyrgC68g1otyjkYbaJ7Tn3CUd6ORh-3dHLQ62Id6TIx4W6t4dc3I5LIZrN2UKESgnqd_fFFPwX0DtB01xiHWQZz09VxrFTJPlY59b3B-Um5bYhc3Lth0z1nTXNg9LR-gvZnuv1ucbv10SNV6L1A2Ys9Zcytf21h8t6os6MnBKGOOjy72DxD11LQNT3GA0fpKHyiloSAT7tI50j2exhvzUe8vYRxrzTp5tK18K7G76OO_i3d_RKbgNFAAAbtQKWH7RiJHt4o2nSTyNkq2pFg8OSVW_VGOhp0SXsGsPNZJSWgVmxXyks56t13I9cKcyxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=qZXVQJbUFYbzreu-V3Yi5q4eyrgC68g1otyjkYbaJ7Tn3CUd6ORh-3dHLQ62Id6TIx4W6t4dc3I5LIZrN2UKESgnqd_fFFPwX0DtB01xiHWQZz09VxrFTJPlY59b3B-Um5bYhc3Lth0z1nTXNg9LR-gvZnuv1ucbv10SNV6L1A2Ys9Zcytf21h8t6os6MnBKGOOjy72DxD11LQNT3GA0fpKHyiloSAT7tI50j2exhvzUe8vYRxrzTp5tK18K7G76OO_i3d_RKbgNFAAAbtQKWH7RiJHt4o2nSTyNkq2pFg8OSVW_VGOhp0SXsGsPNZJSWgVmxXyks56t13I9cKcyxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=MGmWFx5LAFPYoQXJEGUHyfWpTlk2XUQURyvwPfmYf3JQgvWAqZKb-2CqHKVoq0GqTPc8_K5LhNUDHgF5TDY0XHHGfIo1k98VHFHX5HkYhyVpuqO0J4YytdEhbnSTx5L9YdMnrl7-Ubn7hVwhrkl_pzAba7WjO9k9ivP5lTZn4pnc7kWZbFZt7XhhziMAEHLMfYLlH_FImYpoMr1pwUC7VC5yF5Lbt7XZscx4YpjCmhBbKAAgA3uDguiIWwm50Gw0elueu-6Xcj6DN8ePTvWKY-xHJmKmHURrDd91C_5hD8AixMp3CyYIEAzceuS31U2rYGosqP1ofGPvdUYOiEI9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=MGmWFx5LAFPYoQXJEGUHyfWpTlk2XUQURyvwPfmYf3JQgvWAqZKb-2CqHKVoq0GqTPc8_K5LhNUDHgF5TDY0XHHGfIo1k98VHFHX5HkYhyVpuqO0J4YytdEhbnSTx5L9YdMnrl7-Ubn7hVwhrkl_pzAba7WjO9k9ivP5lTZn4pnc7kWZbFZt7XhhziMAEHLMfYLlH_FImYpoMr1pwUC7VC5yF5Lbt7XZscx4YpjCmhBbKAAgA3uDguiIWwm50Gw0elueu-6Xcj6DN8ePTvWKY-xHJmKmHURrDd91C_5hD8AixMp3CyYIEAzceuS31U2rYGosqP1ofGPvdUYOiEI9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTLqBR022Eeh5vuiLEAMb_gIqyrA2UxUJT74zY8yGUZtf24EnKiuK-xb9g9e7EKH5yI2S1igkhTKRj_IIgBhzHFiV3TQ_QpTEF-JWx-SSp1tLJNcwwwrac8Gzh_jL00r4L7BR_UabLCalefKo3xAg3VKjvNRX_aNz8miuKPBL-ViDJBlNIe7K4lAG09InbqFuHzDgBcq9kMuy1J2oG79hkhYv0PeuUqj_fvdSS0xFqPcCukEFW15lXJf8IBhBfXuqu6R1-KMEiGOx_IbwG9kqxZdwUKcSs9TFcYyzX5M-out0MaIJo1H0W82R3yNCIu9McsSCdi5uNw-Wze_jlD1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=h9UJ4IIbZNOHLe3sWilPsmiwKWeY_TWnAOa-ZgooLj7-e2D5cEksD6Sr_0YzM_sDNiC5M59uQiKXrhIpgdxBYFfizDhonhSQJmjTR5_xLQ0YWwV583B3SeIS8XdSxXbEEXX7Ga4TXuFGdMIiJRqmL2z71kDgOYcd9-ViwBPpVd88AmSuhywMdp9wzpNHK8Qr1iR-Y4hZoiX5OJ6VkqiT3cW7gx-XAq2JXOw1_NXxN_4kxnKKj8YsqrQENKHxgY8X6arbjn5iwhgwj1BQkt72rPJEqpCLeFuHU4y_QFAwJf9w5xU139ClrhppRNdNFNQaMJDjNNLTz0QS904_5NTMOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=h9UJ4IIbZNOHLe3sWilPsmiwKWeY_TWnAOa-ZgooLj7-e2D5cEksD6Sr_0YzM_sDNiC5M59uQiKXrhIpgdxBYFfizDhonhSQJmjTR5_xLQ0YWwV583B3SeIS8XdSxXbEEXX7Ga4TXuFGdMIiJRqmL2z71kDgOYcd9-ViwBPpVd88AmSuhywMdp9wzpNHK8Qr1iR-Y4hZoiX5OJ6VkqiT3cW7gx-XAq2JXOw1_NXxN_4kxnKKj8YsqrQENKHxgY8X6arbjn5iwhgwj1BQkt72rPJEqpCLeFuHU4y_QFAwJf9w5xU139ClrhppRNdNFNQaMJDjNNLTz0QS904_5NTMOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rya9NTaKge8MVGoesn4h6ulCPVupQmRtVqotvr2oNLrOfow-HuXqM312iP77qHOlxbOQIUe0Y2TmidA6DYnRa3X8F55CjU3wwrWU32l6yo5iWi13WcO_vay_Y_TzJWgzvM-9dtsQkOrFMD9xVDERWA9rEPBzTN9qN1snz42c69tjrvY-3ZghIFAgzCUWR5oGKnswgh3qWSRNEgZS5PJa1Zr84bdZlhRFTgEAnn4lYca-shDPstlMOyvUMZf4-S6tPamuW7j_yncUmihBbG59u_gcoLbqJx_vao918K8_cnzT-PQsKY3uGvwI0NN3VSCvcBRbTbklyPwIHjDI_HuUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj08noLstPkJnNlGIwPP6-ArMMyF0L5H7-pAZOL63yViJplsFsj4maFcTy_Ewo8nbmAXeZ90bMsqptxz-vTwCKKHofB4YyUep916dHZqKzC-HDNpQjzxBm6ybrS_5S5AE74CxPUxK-PYbu2mgiTTXum7_zUivsLiw9AZ6hS8J7U6tT-a-u2yycXvkX6W1pfDH6NoxPMJoGikT2ftwXLkpv9CtQRG50WpClhUVlxbm183WjxASpKEq02CU3yeNvBoLgQGWhYt1wBweYyuNjj-4kgi9BPMh7sW6Hhd0EqO2E7mH3WFReGwf_FWo0QV1lVtJYLIH3CJfUrR_EtdOP1jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAvZiWb8jd5WTS-gsu0V43UQzusVAEOeGKeCOpSssNFYe5C9AdmO2iBYL3GR7D-Qp40W35CrpnUpEMcbG325AA08hwck0UNOcmDbBhMj9d2Gr5nLUBDZ_m01HSIr4VgFCrqqFoRinH_lpB9QNe8jLUJPgRLhoPDwAYc9MixnhrirAawVQaLtCr5JrqI3k1AjUS1N3Oc-wt9BwMnTWD9rBet2vCpQYwOI1e8CVqiQEeNu32-ZMnDrJQGwlPLe1VDLyU2Is0FRpKUsswEYxU0WSp82iAtXG87tJsIzVSs-ZW3vY1J1bflmwM-EAOoizqEutJ9aq69ftS2TzyQ0lFoHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7G5bUQNiI7d8_09fQhsq8QecYpDczUoJdz_VOuF5Tk0qVOVXKI_aXO2cqUtWJ4MalZHilTXUbTwlY1IsaCW-NvL9LLlI2_PNsbAESnzvZLo7lboVhRAueOv3_WktJ7TzzEQ4R2O-p7dxGib5gE68QOD5St0JElL5TgBc99ZYedUP--ZbgMcpDqC60znGKF87itMn-TRT68sSUjQ1Z9cpwSzF4wzixMifeD6ftHkPlhuSPgghDO7I4EMJarb5oqNQiyBh8VFcu3Pmxe36flLLBQ9E7s5fgQc620LLtofE4zcEMK0EBY1hjmiE13-Z4z1cZMNEx6ZT4MYPMosXCQfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGnt3IWZFmitYkbkTtHnWGby2cgb4iiclspS1WPE5rUBmclJB6CD0oynhGP4v8Xn6eRho8Ed0So4Xt_46ZVMW2PJeHR1XHpD-KibaEO1yqrf0spywbxyj1J-2WWcbU3-Ov8ZoKhmuhGw8g-0nxRTcSdM3xIiHQQPtJjl6-3Ma6eVxwqzze2b8ji9JoNishgTNC2jKkjy5nv9XgV7v3_fNPC6GRm8yrwxIm5mYrjxL2IF1LcgxHN8Z8psnWVWFyEodgY6Xdu13pU63R4O26ZTXiBv8tDgeivcB_CBBmtVKxwKPDFyLItEPzseAQc3k-LYuq2aiZMwtNHcP2hC8WElfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElWXvdkOTrqshP-Za7j5LN0WUwMsusY-Rlh690-fCIpHBq60MK8skGpM-4HU9-Wk_hiZt444JxgeXAE4felqqJR4NGM5rl2DdpIaeyLMetTtxb3xMLExx_hHUTUdUxKyGxatAGbtXDt94HOyZu36aV8PpDKtdjPT9UhFbs-GOIMUj_mgvNRWY6OGcRR0qW7c6incqQKHtL_SScka2pOR_VspsSQmZH5J33mTyoi-pqU2-8cVNazZ_5K1rl8u8s9LfIKrJJ8eilx5tSztEff8QLC_jn2Y7iK0BLAf9BqprTa2xmjWso_5xbQlA-zA7THkMG5IJhLKTNXiQ98hJ45v8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=fOlEYhiXbgXpY_H7QtPKTVu5m20JsVv_brR77lEv7cngL0xTiVGXHdPH8iyA3kaVmiZitxgrOyyQHTNa4ZeO_jnVoZvHsVKc-x9jDA7ATuCJZItjwk3BrBeNMhtUjCNwD15Hu0mCWzVth_LZkqpTFtZfCR3FzT1eeYUfkooYC9RA-Or2SY87SEIH6pbLuy1dIZgH6-LuaYnQkL-xgkHjuPP48Oc13nsdFs-djirReEeR4_O5DLmN3XxYSyvAtu1GfR69xnkp0zSX3avMSLK7fEka82_3lVVe04UiTMAENCWz2mvZ1cA6krm1t08xPiQsCtgsLkkm2pNwHMaY8VsQCEhrHU7LoJrDULMF6-zwDKY2ewYEDwU8khVn8c465ojIA0vVUX3MgL5fIUlhCahVXFmEOuXjblXOFbo2HKSneKsYQ9thSDnDh58FdDlZoYGGn1DLEAMfjkV8-LeKGFYekOESWAuKIBHVZWEQPX7wPxtKSJpwOWJ1zVz9KfysAXbuNB_eeya2dzbUbqlnmOuVeh7R3abq7KOs0xlIUprGpVLCLAi8BNN9hJPRqO6rriOTs28tYJqKcNlGKBcKTFSdcx8Qkr6mKTsPI8fnh3Cs0QC_8q1ywdXSUmyl3G3tZ6Uw78QQ12N24o-S7kACP_NIvMHEm0OIz6WEY11CRiJ3UHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=fOlEYhiXbgXpY_H7QtPKTVu5m20JsVv_brR77lEv7cngL0xTiVGXHdPH8iyA3kaVmiZitxgrOyyQHTNa4ZeO_jnVoZvHsVKc-x9jDA7ATuCJZItjwk3BrBeNMhtUjCNwD15Hu0mCWzVth_LZkqpTFtZfCR3FzT1eeYUfkooYC9RA-Or2SY87SEIH6pbLuy1dIZgH6-LuaYnQkL-xgkHjuPP48Oc13nsdFs-djirReEeR4_O5DLmN3XxYSyvAtu1GfR69xnkp0zSX3avMSLK7fEka82_3lVVe04UiTMAENCWz2mvZ1cA6krm1t08xPiQsCtgsLkkm2pNwHMaY8VsQCEhrHU7LoJrDULMF6-zwDKY2ewYEDwU8khVn8c465ojIA0vVUX3MgL5fIUlhCahVXFmEOuXjblXOFbo2HKSneKsYQ9thSDnDh58FdDlZoYGGn1DLEAMfjkV8-LeKGFYekOESWAuKIBHVZWEQPX7wPxtKSJpwOWJ1zVz9KfysAXbuNB_eeya2dzbUbqlnmOuVeh7R3abq7KOs0xlIUprGpVLCLAi8BNN9hJPRqO6rriOTs28tYJqKcNlGKBcKTFSdcx8Qkr6mKTsPI8fnh3Cs0QC_8q1ywdXSUmyl3G3tZ6Uw78QQ12N24o-S7kACP_NIvMHEm0OIz6WEY11CRiJ3UHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2McktNWjVNZ_cDX4dlkFe3u76dPh5E2JhqMfhVcvcW35w3eLr8RgnOV6mscgFGF0WvsMvAg9SIl7e5bUnj4xAA15EUTDlVs4JymTf2Gn8lYgn4WsM6TfpsKM0OBqx-KsXXqRC-uNxP1pM184tiXcnNKL-eiFrE1S70kSY0R9T7DO4F18sKi2STnJgdFRkDGB4KddObdc-_tSy7WLdIDjdIW24iy7rUVlKe4U84_6yXAyX0i0GlCJQqpEevQY3NObC6u7JQMyjump4rP9oStVPGtSqKCuGn24BuF_Wxwo3_7LTwd1kL6mWHMx_Fp0-zRejC29sm8croRM-NX9eTzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr8vQyOudK117FZfJuwa76EWeIiiE9ZBnaRAbBREfmNVkd0rP_jvu8BfoOUv7G_mmPrcdP_DiGP9PClTtA5BxtbhgBdu_KtsVSezM_11-U8WpaoCOIaCmF2WI_NC41LhRlyN7uN2pvqsuv-L03CLlPnNNf5d7Ga3UjmZ-0yY2Id54O3-Ntzkfw-7QhyDG-tYdUqJDQEKcu-xQ7slcnbGlwn6WDbGAVU_2bNNfJlYmtE8coCnx-gb52Dpm2dm14dRC2bntAxknCg07xN9JY2lJl0BEk87oA3WFGkEno4zK08VBxOt2d8TNDoy-qrGpAoUa5vc07u95toHQrN8R-j8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJaHI-F2mRWMigi706s3LRyc8CncMBJEmwNCSEHD5rRY00fBLseI26U5_gvw38nOHCm44quXVF1BBYpgWrNjXwFbPFFkjyejXw1TUsrPd9Qrv7C1qaWV1iHo8tIiz-WI4WmHkrNeR41CSOmF2bXjjr0MJ2otvO2QkdfetSg8EGrVwz-PagngY5hzWjcGQwPsBwynjGk4j5zghyYuwDLiroIPQUD2coglbS8zHBpg5EM9OrU_2krNfrtX13qnWrhQJiIjTlNlJ3A_ukwKUqfcv-FFKn9hQCHtFpkyRKKm0dYSQfGP-VFopKiwPUTNHpxXWbtyYZpnXiRbg3teTshfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOTvYi0WYa_-f60AslIQP_wBAIEEnCNjwE2fFcU9I48B8jQr3cBR0mRSxlqVkg81OuSuoP1WCVoFYO1GwYb_V-aZgWFx5qzOIBl7U7w7SQfPpGaUQdkbM4n6wE0s5pY3NeIVVbKpH9k2aODJzBLOBUsHbmPEMVdezMnOdyNhR4kZOnsdZXctVGf-mXx3vf1bm7Mn9VtM8dJXFfsdJNhygyteS7siscO9k3zIsJbLXI2HEcAfDA5vKNrz9vqBQrdAAayoLKMTQ_Zj2iSQTnWw9Yx3XPo07sbMegyb2-qIEiBpb-eFU4n0LXQkkD4LNvwhZe-bZBEv_CF9eKfeJc2BaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvzX75f5oFRB9fsiU4nhjTD15_Y2b6dXDG0hfy1mcjx4uIqnaVqm9FzJ8XV7-U7RWi3MTuXIilEOO8KqV70mP-Me84F4JT8JsYYAf0wJZAzcdtGGFNPniPTmPUKglYlH3xzmGyeBwtv6fBUKVl9fMZpu931mGpi_U6KREmIOd1kxFgAcKmxRIugC6HL1Xc8nnBi6DXNLEdj9oLaKbOzjr90ZNtVrzhKEtUo1Rx7k1DvfzumrvodwXWfzAAZ4phPtUa6NrjIZeD_pNfdo_8uJSLBf_JglcG1BcKja6Lac214FiPJZZP_ZEQeaAJkvMA77yef9OlMu9xo2anTwcSkJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zor3GnhIV3nBmm9QssJ_Mf5XJfuCewjjH9y_MnJFk56njV-UtO6biyoVn4cloZPza_RW1tSZ5PNYVfyFxCKOeHlOqpL6AFU8svtr04N0wQiApvFgyHDiI1rWfKtKFtX1Q4XTHfU-1ymV2veecmOQ6vVmMpPC9G4q1a_aKO38KYrVNiw6uuTLI5qsvIBOPT61R9O7lm8lWQMRPRHgsK3DcYZ-AKVBPDYRMJZppYnO9aRGqDXKu5tvzL9vRLc5wsO3rj112FHugfdQj2YQKEjoEDb1AL1fiXNv9XWFB1_wsa64hRjdNXMjFL_hpZkfWRnLDXsLMTYzWx8QwC7-3pLdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVWoRo6sU-mSzJ-uMkh1PesUOV9wuaDRKtYe-NXo22q8EyHkEKpM-v7kgGkNjAXMplX_13K63mMGXnqspO5-knvf2JYVNACkgiMe_kYBIsYS5PWoiYKRa8JoKTb7E37akFWKsGdmLolYCPODV2wmw66hgQfhqw4fsXLoOc9lJQ8NDWrjvLLcLZyicLajwEO-o0vHN84Hvjz_jpiZLiCky-JBN76hRMnXjDBn5-tD7ySKllosVvK6Zs73FCoWKYhlfV4Haqu4-GECSu2lfLhGRD3DJf0rgHoOVAp_r2YVgTeeg0RQ9UsVS2PggvdhOD6DXWOcbLisy3q0jKQHAAdTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=Tn2MRoAZg3Fiv8vXam1qhxXr04v__dZCKiFc6Kh-cpJGOGr3nc1lUj5PSxzP8khE52vgk2hyWF_H9S72DnXgZZ4IXIffj4QogFz_amE_h7b_Cg36KjxAs9AVQtaduBups_DVOufrDSssDZU9iVLl85mZex7IvU0Mu2m2_Hgt1Slvv_Bpw_EaW81EvMFc7Lpk17QmQdVuQLagwaFZv-gMG42GzoNV6RzCIRinDPYK338UCv1v0jf5Cz568dLlDrUoUiJu3fo_NYS2lSuluOB7jetSipQohouVP4hnSgRDq9fTspPGZNZy2y2XaCcusii_O-h_IT1ndkt7NldwbO06Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=Tn2MRoAZg3Fiv8vXam1qhxXr04v__dZCKiFc6Kh-cpJGOGr3nc1lUj5PSxzP8khE52vgk2hyWF_H9S72DnXgZZ4IXIffj4QogFz_amE_h7b_Cg36KjxAs9AVQtaduBups_DVOufrDSssDZU9iVLl85mZex7IvU0Mu2m2_Hgt1Slvv_Bpw_EaW81EvMFc7Lpk17QmQdVuQLagwaFZv-gMG42GzoNV6RzCIRinDPYK338UCv1v0jf5Cz568dLlDrUoUiJu3fo_NYS2lSuluOB7jetSipQohouVP4hnSgRDq9fTspPGZNZy2y2XaCcusii_O-h_IT1ndkt7NldwbO06Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up60vPfGKEpLSpYWSrfP2sYqzYi3BI090JNOXAjpHJ7FwRmrwxTgH0R-t5Y4oiHQ1JFfHm-6Sp6OHsAxcNyLIJ_-fAdQBIYtizL3rB7hgQGaZ0cm2L_1xOsYB94PAHl4HBwnOwHYX7iMsJhKbT4DXL_M16PZyR4sYG-f-PVuOWW45i7YmZsrB5Zu7Y_dJYYTuSuVAUjky_ydIzR4AbKQzFlccyecOaiAwO7hHbxk8PxbuZA2ZQsT8Y1YTyFrNYL18VScLRvqimi7ngF_Sx5ZmJ7GWXpbqo65C5z2dPSuwe0D3giGidD1Q-ceQUXKjyIVFgaM0YTk3Xk1hQdY1NawYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=VD1JA_jrybCtBXuk305j_9Nwnk7PB7Kmn924gYrR4AWQnmxYAPw89VYGk-qWL2sOrbn-oq_tWRA-CphECUja4h_yCqVaLl2Kc6n436woS78pLmmenVHaudn3krl0_2XdfJpQqBOVbvJfOk8Emq0G0dsjMgc34KZqcgSUYc9gETWKM4-UxOejSP_KJ6J3hQlwe-33SIi1a-5CZlZnmCBytfI2XLWdwT4w-QgCOgg9MPVx4X_c9tZvefH_VJ0qHotK43JHmTDNVGMU9D_ZHD4zwUIdwp4TtTDYJhtRPPURXxthw_ZOOYTZd3HFiykwwqv39yTeaM1Ir5YYiXMS3KPm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=VD1JA_jrybCtBXuk305j_9Nwnk7PB7Kmn924gYrR4AWQnmxYAPw89VYGk-qWL2sOrbn-oq_tWRA-CphECUja4h_yCqVaLl2Kc6n436woS78pLmmenVHaudn3krl0_2XdfJpQqBOVbvJfOk8Emq0G0dsjMgc34KZqcgSUYc9gETWKM4-UxOejSP_KJ6J3hQlwe-33SIi1a-5CZlZnmCBytfI2XLWdwT4w-QgCOgg9MPVx4X_c9tZvefH_VJ0qHotK43JHmTDNVGMU9D_ZHD4zwUIdwp4TtTDYJhtRPPURXxthw_ZOOYTZd3HFiykwwqv39yTeaM1Ir5YYiXMS3KPm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB7pvxUr1JKuutrrVfxMP4tdmd9Y2v0KuJE5_hMuBYDUbg8KdCPExZjBS1rkaLtY_IYLGnxK42Y4vKz78hII6hDJbMZEu-O3xwkwbhEBdmFX9hxE-envAt4Jv1R77d1h57Ot9x6ZQB7vgkvIC2RE5_PUkQGMcv8Yta-fFTN8Xbmd98Cwi4duGvj2zsYDgxfDFJIiHlJ5xpSMwGBRefoxLGAfko4UwmAiZgNkFdhIle6O6h-Ossknnw93VBM68MEHxuO_jn4lOzJLqKtx5XOsuahOeaH8IyJ8DHfZlEEUY5Qau9cKMfj6CrIdNdcbuW64aEvRAOPU-ypi2LOBVq2cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaB5H-mhAqF90lsruJzV7M6CAyQeJ-MSTpUHm7-dAj3IkcK1nLa0UA6bOlZxOXBypcqV2SC5bdfcr1sKLv_OfCtCBK4zSlSV74IQSGzbOmTS9YPiiyCN4itYZwnCrS6UxYBzj8b1dI85h7SqMTIZfZAUOJnY8XlK00fEX84D6wgWhm3kgCi5E1CczZHIlBK8NCdXlWBcgYPy6wIjWiatWc1IuuP8H1Ps89MmosrloyaOLt3mBJjghnj_r2je_FK1GNjo_-ne8vK6f7V6S25JGx_qBUK_gAz1b6oKU6W5Qt8CSpaxguv_jxaxYPCghfhlHtYFGk9EjtmJvWReZ77ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTIpFL-9Pjh4SfkECRrsmyp_Xem1Dyr_npIQv4hjrbouc_p6eyoBOOi6yQGMSRTWEmSX9rlcD-6MK314N-I9e7oc3cU07NZJl053w9oheuDB6omkILCctDQppebZpxjRlV6eDVvdGXMYh8EfGLJii73QpZVljOar8w_3lfxC4old0bkx-mfDPPBiQKtDTxysXh5t1GYoTtDLKEZgWvdfOlj7dLt1xVqY3UZR8xMJrlWhCNOFwL7lAI1aUnUDeq6RRDbfhtELXDXQTcc1CMo8Exl5lKqcqDgfHUgIkQpuY8pEqxq7WZ5U7ya4bzEGMUEA_s_U7YJxNJnc79DP32PJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b48ylX2QSNHinYXnGqXaaKp30E9IfcOzyKZi4_1usGL_JJbB7MAqCeT8lakXkmFgujI_9ORhVfnDNCRTb9WFvRCoDI-b5jiPmD7LHAzbMsrYkcX4HTLeOjRdAamBDL7XB30EXosm-5Io_wvA0rb8uy5SPxxuLUtk1MFNPYqbf2GcyBM6N5lgLSI4MzedQI04vf6fUd559IqrZ5uBwWiGWLBPnRU8VqJFMtxFvZrK7oYRyYXKdqHsQNOj_EUMoGw_R4efLS2fGLVOtn3YYn6vCbRdH2BLnn3PZIe-wKg92mx7ujJaIOTsWaTOOWfAuprUZ3pHtAg8LlaYrfRVmOEzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkSoOnDMOrMU40A4jEG04uIsCw9pXQb5oVLmZ8XvdNMZmBcmh3XXkYR_uLfjAFPQrNANuKvUeo4QUwlE3Eo3BEUm5hzX9-ePMq3YrrG2XTg_VddcLt4KZOv2ouCD6EsblnCXci60m0ZLGe__J7maJewxyVEYRiu6-AK1oZ4Cr3xokGIWtVYGm2YS64SNZWkQtHqUn38sBoyIsqbXLhVHXK2_Cs1g_OhGo4Us70Sb2DvmwoH5_KRMerlP4Ad7miZSq5ULus3KMHN5Yef9BpETmAvC19ycDhkRvDr284eRUSkDzYmYMVDYX2ViEhyNmLf47B6swE9iM1K12nWaLfezeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=AINqKn4jc60qHeL5xGED9vVkexUCxkySg6XBcaFrb0wcyQ0ps9OJm6lrsKJJTN3bCrhFAmnvy4FVlBLEOggDdjQcrKA_cQQWDPOgTgzhXmzxlx86EsJ9tB_eo5J2cad4-Ze4nimdVv0sD6zxHBevR40xSdQaM6UNIqXObIAMBhXRYRO9y8cd-rlhWa8akU2ym1iGXz6CBADmDp02lAQZ_9l8Ibi0ss9yELgZ4CbVCyDfY7Y305bo55BhAY31JPS2OW-UmeBE2fDl4-1aQlkLFO9kDv8dtJ-P0Zj93WEhv3Imdeyl_bcFtcdEfOpndgZaaBOfXBtSDqGv0a-s5fzUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=AINqKn4jc60qHeL5xGED9vVkexUCxkySg6XBcaFrb0wcyQ0ps9OJm6lrsKJJTN3bCrhFAmnvy4FVlBLEOggDdjQcrKA_cQQWDPOgTgzhXmzxlx86EsJ9tB_eo5J2cad4-Ze4nimdVv0sD6zxHBevR40xSdQaM6UNIqXObIAMBhXRYRO9y8cd-rlhWa8akU2ym1iGXz6CBADmDp02lAQZ_9l8Ibi0ss9yELgZ4CbVCyDfY7Y305bo55BhAY31JPS2OW-UmeBE2fDl4-1aQlkLFO9kDv8dtJ-P0Zj93WEhv3Imdeyl_bcFtcdEfOpndgZaaBOfXBtSDqGv0a-s5fzUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L0CZeeD3TlbL8orDRhpRoNm0S1yGj8tt-Zbea87IVeZe5nR-dnvFhv9otl0S4-Dsjv_mOCxQ7pGb0lMvn74MXif6YkbioR_ytkH1YpqYY-jLzf2PORDMeTdAYu4UaCzOQoN_n0Dws4E4TV7ppKa1BLsG3JWjrXTFPskJu4atq-bKP9h5v3eAjDYKrXZf2HmwY9HjIcnuyKbrQM6g22fAHzqpbG0aD8Yya00KdGDsci4xQ3B84aPAs5yYftX-OWYJhQNIABZDafF8zu9T0KHvK-D2zB5d08B65M8AdUMK0jOwgq38uBHTmnftsgK8Qc2DVF2_98W-7xsuwcFTUl_Wxqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L0CZeeD3TlbL8orDRhpRoNm0S1yGj8tt-Zbea87IVeZe5nR-dnvFhv9otl0S4-Dsjv_mOCxQ7pGb0lMvn74MXif6YkbioR_ytkH1YpqYY-jLzf2PORDMeTdAYu4UaCzOQoN_n0Dws4E4TV7ppKa1BLsG3JWjrXTFPskJu4atq-bKP9h5v3eAjDYKrXZf2HmwY9HjIcnuyKbrQM6g22fAHzqpbG0aD8Yya00KdGDsci4xQ3B84aPAs5yYftX-OWYJhQNIABZDafF8zu9T0KHvK-D2zB5d08B65M8AdUMK0jOwgq38uBHTmnftsgK8Qc2DVF2_98W-7xsuwcFTUl_Wxqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-jo_MNwMz8tTmES3pog4w8hJvE_9suZdXvTAKmYs5m48AS7DTaYSy2S7jAdZIbJ3CuOZXpZnBxePFujrL1naQaP-0S7VHRLh4tPs3MqUtFET1BMuZ5D5zupqtMcdsO-sINq0suBC07f9SEKRkYUL3xijevXnQGXi-p0Xqa5VG5_eUyj-_BlnaM5IUI8LM0R8zfgSakhihLJVQew8aBOaU28lKZ0Q1S2aoJtPOr2lZBinFqVKR6bvXOvjSRQsorkyxgXYwBvjZgkGw8iIW5pAB0T7Afhk2ves4sPvrlN7OCkmkPZAu7q_343FWyN4HivLQEWg621hB1kIUwcHyzLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=QotayLaKslAGNaKk6bGT-pci5m6SWdyqpyxoLNSU9Vz8CcJB8CxFCszdHaFkHAsltsiMepTPoVRhAx-8HSOCGJe4OzkI7VU104FnHhvm1_rnRMFMeaw3EEjwfnChlF565XP785mldqh_0PY07iap-ctbjL08yy1m4JrM8OHbMI8IqCovVK5jV3NKW5BIh7WOR-tf16OwrgAYVoNh24xB01NfmPvpKIkcfF5zEpjJGzAdXGnqVbM3Sw-_ZvZoI0LjN9kUrZEufOVAbcWlxdVpYC18Wtj0aDkN3UylTrXLuSZezI0vLLAJAY4FMJCNS2O4KTp2Iq4I1DypEwOnCZ5Zlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=QotayLaKslAGNaKk6bGT-pci5m6SWdyqpyxoLNSU9Vz8CcJB8CxFCszdHaFkHAsltsiMepTPoVRhAx-8HSOCGJe4OzkI7VU104FnHhvm1_rnRMFMeaw3EEjwfnChlF565XP785mldqh_0PY07iap-ctbjL08yy1m4JrM8OHbMI8IqCovVK5jV3NKW5BIh7WOR-tf16OwrgAYVoNh24xB01NfmPvpKIkcfF5zEpjJGzAdXGnqVbM3Sw-_ZvZoI0LjN9kUrZEufOVAbcWlxdVpYC18Wtj0aDkN3UylTrXLuSZezI0vLLAJAY4FMJCNS2O4KTp2Iq4I1DypEwOnCZ5Zlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=dbTBhJsP6_QmBSOIWvxrc9Rkpu-SNoiY1DQhG9DMxzEgv_GreuC0gWmfoSpa-2QE3NT3F5qi6HznIH7AYtzEN-pipdlu4IPzwfu2LVWPEOTcWLE76-SKBbVI1WlwE-kiKbL2nNmkexfFW9Q7AtV2vahkv5hRVN_FZi1od5f4QjOwxouBUHXq0RVPCdbqke86HZVvn-n-LhjS3iLgCHWB7TGlTUEsFEwZxDPK3v5GrMyPbr6URv490QDuIIlnjNU20UOoJwsOcLZho0XKpm-B9bv8sZz4t6-04BHaf3LqAwMOcgeGjagA9eHjN1Fkoqy4soNBXkr_ks6lJlGlDLSnJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=dbTBhJsP6_QmBSOIWvxrc9Rkpu-SNoiY1DQhG9DMxzEgv_GreuC0gWmfoSpa-2QE3NT3F5qi6HznIH7AYtzEN-pipdlu4IPzwfu2LVWPEOTcWLE76-SKBbVI1WlwE-kiKbL2nNmkexfFW9Q7AtV2vahkv5hRVN_FZi1od5f4QjOwxouBUHXq0RVPCdbqke86HZVvn-n-LhjS3iLgCHWB7TGlTUEsFEwZxDPK3v5GrMyPbr6URv490QDuIIlnjNU20UOoJwsOcLZho0XKpm-B9bv8sZz4t6-04BHaf3LqAwMOcgeGjagA9eHjN1Fkoqy4soNBXkr_ks6lJlGlDLSnJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=CNNik5V9c2Or3rD_eUv3N4b5paARAMEzRovvUPYQIrDxRX1DHSRk_5WeSG6BmF4kOFZnM40iUdu5-b7e0aJLNUgA2dA6eFyE6GwULseDUYz-Bvj_WRDXILT0glLOANkKJa36i1n-bmZUG7E1c_N2foNNipXaJ-JyK37wUh_QquAj6nyybqdFks8YWuf_eDUcfcvRZL26qjE1D8_g1IylBZnv3iT2bAV_t9YqN_u13reCsS-sTY6J_B-tbBRie36tqDxQqKNgUmaUDyGZ-DSU6--KclXZOUtUJxS-ME9v9JPR6w7kKi9zFoVR6x-ezyTHqQ4H1DfFWW8RGiIDU4-6QR8etAeu0JnLfK_UoRmwpnfRPWpTEo23n4HSV-qIczO1AJcxPknaWUTmvL-xgKvYrke5fjbZ8tF4D64vKj28nqrcxQaCQQZ4JZA0UdrsYX7-XOzIZILgh5rTUElwKHW9PEKR2q5WtW1HpqzpjqCqbp78TxUcsU-ibh0ypVCWR841VUMGMUyT5SLB31wsTVHOGTj7MtEAszEbP1Zh1F81cz8vEyjWfBZeubnR-vUwHfqNq9v6m-SVDIL_8_H4fCgPLJrPcQsi3Ql3ycMBiQwEwCjZ2FwIi-BXDxv8NZPw1eAcFfyGrnK9B-BthrQMbQLYAzfMkCP6Bd3WGgYjP5Ubv44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=CNNik5V9c2Or3rD_eUv3N4b5paARAMEzRovvUPYQIrDxRX1DHSRk_5WeSG6BmF4kOFZnM40iUdu5-b7e0aJLNUgA2dA6eFyE6GwULseDUYz-Bvj_WRDXILT0glLOANkKJa36i1n-bmZUG7E1c_N2foNNipXaJ-JyK37wUh_QquAj6nyybqdFks8YWuf_eDUcfcvRZL26qjE1D8_g1IylBZnv3iT2bAV_t9YqN_u13reCsS-sTY6J_B-tbBRie36tqDxQqKNgUmaUDyGZ-DSU6--KclXZOUtUJxS-ME9v9JPR6w7kKi9zFoVR6x-ezyTHqQ4H1DfFWW8RGiIDU4-6QR8etAeu0JnLfK_UoRmwpnfRPWpTEo23n4HSV-qIczO1AJcxPknaWUTmvL-xgKvYrke5fjbZ8tF4D64vKj28nqrcxQaCQQZ4JZA0UdrsYX7-XOzIZILgh5rTUElwKHW9PEKR2q5WtW1HpqzpjqCqbp78TxUcsU-ibh0ypVCWR841VUMGMUyT5SLB31wsTVHOGTj7MtEAszEbP1Zh1F81cz8vEyjWfBZeubnR-vUwHfqNq9v6m-SVDIL_8_H4fCgPLJrPcQsi3Ql3ycMBiQwEwCjZ2FwIi-BXDxv8NZPw1eAcFfyGrnK9B-BthrQMbQLYAzfMkCP6Bd3WGgYjP5Ubv44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzc2MG_a9iVy13SvJSqpbKJv039Ty82EgApq19QHR9E8KefMAbGFKRIkPyjlnpD1651lI87uSiv4ZulUPjsX_2bGbRotPEmwoUeopcM2M6gyI4zKqKVLAKzYlMr_wm0ts4LQXKhUrrUFGGX2awLnL7O9d7f9mSIbNgFI8k951FH0bIU46TBwa74f_VCB4gKfmQ_2Opmou7zD4zWhnPshta15W0xuGl-pG7eBvsuE1nEEsin_YT7eV2IR8-L6dg2F3MdRB_rG1JIEbTEiMg6t0XV6IvPh_xQvzb_av0RfFE9OMhNpxBJjkw3XqJvVp9vKLGycRFvGElTOj4G9_Cp9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=is476ghSKq7fuEsHsa8VfoQOtwhqY4zhKYFZHo60S0H5SNc0wGmCV9csW3ioH5Iz9XzUD_DSP1rtRaPqMdl5-TagyRn_vkMCCD1mUSy-cMhEFxDuTWuD9T8BlvAl9tvye9qC4wVDsWHhe02RHWdBBEcSGZB8hOEiNt9PpGY8LafBGTDorbFC0Lld4bjQ30n3bF4SpWixUC-EgUPFgEZbNH13AWmHsfgD-sBzpLY28fIeIyB1yv_Jvjdq7FA3RKMEp0Xd2RGcd2vnpH-FIYSagopgAUA8QmXbRm9Hvi678XH3traOh69Z6SFnnthJcR9Z58MADfMMyEWONke11Gig5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=is476ghSKq7fuEsHsa8VfoQOtwhqY4zhKYFZHo60S0H5SNc0wGmCV9csW3ioH5Iz9XzUD_DSP1rtRaPqMdl5-TagyRn_vkMCCD1mUSy-cMhEFxDuTWuD9T8BlvAl9tvye9qC4wVDsWHhe02RHWdBBEcSGZB8hOEiNt9PpGY8LafBGTDorbFC0Lld4bjQ30n3bF4SpWixUC-EgUPFgEZbNH13AWmHsfgD-sBzpLY28fIeIyB1yv_Jvjdq7FA3RKMEp0Xd2RGcd2vnpH-FIYSagopgAUA8QmXbRm9Hvi678XH3traOh69Z6SFnnthJcR9Z58MADfMMyEWONke11Gig5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=GTeKrQKt69keDR6KIuEpb6zAP7zcAsFxcml4hSODx_2N5YukECLxyI5yHZyEr0llWc7x2B2O5otBOh4-l-xRcf3z9IolGreo9C7zYfTTVW9JKCk7KUEvJtS2OGHJnRYOGGSGe3sztCDmh6wbTXycbg0J9b_rIraIe6YNp41BBIECFiqQSt8_6DxU9u4ZNQdLUnBsyY_kWJsl2e5ALrH1faDJt7-0ZqW97Cme9LM52P-pLLecSEQJalnCgyx2gi_aipTD3Y326FN1TZDGhx_TWvwfJlBOW3_0M0ruR5jjM5bKDdbQZLyXuIP7qnnpUmuhTW52YbVDN4trjd66cP1nUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=GTeKrQKt69keDR6KIuEpb6zAP7zcAsFxcml4hSODx_2N5YukECLxyI5yHZyEr0llWc7x2B2O5otBOh4-l-xRcf3z9IolGreo9C7zYfTTVW9JKCk7KUEvJtS2OGHJnRYOGGSGe3sztCDmh6wbTXycbg0J9b_rIraIe6YNp41BBIECFiqQSt8_6DxU9u4ZNQdLUnBsyY_kWJsl2e5ALrH1faDJt7-0ZqW97Cme9LM52P-pLLecSEQJalnCgyx2gi_aipTD3Y326FN1TZDGhx_TWvwfJlBOW3_0M0ruR5jjM5bKDdbQZLyXuIP7qnnpUmuhTW52YbVDN4trjd66cP1nUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0J1hbt7JozqgTPkgAW_11-zmLuazrsyWXCgn4_AASNHRvkacGx362F9k6cQ0DN5buMfyzfZhSO6v1jQfphV_AoGAHHhl-y9e2NN0Jp3tcoCdpfFm8dAX_7-gsHRQlYq8QWCdKrDGVMZrbMJB8xbbIB3lIVfoqlDOgw9SgVX410yKgeFLUlkbg_GW-h8smtdYU_ADcE0nnT6lmOHtutGE3sGsHYMOjvMIVwKL80n9bkQmVgw0_gqGgL15_eVLFoUqJUEy5eEP8b_8s1VvXXC6q_ex3HgwsyRF3aKvY5KWzaxzWdwzw7x0E53v5MrGIam90ePF8HE8tijzxlnpRrQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzEkgq9hoxEchx0VBf_B_G_P0p-lgpk9maykQYR6SmAmAPRgO32RIMKSpQUO_vt_Jme79dEd1M8WBQ0oTo60kv0c4l1XI5tzWdH80QzcjcoIZqAOrChJorlCeT7KG9wBiFYmC6uHppV1LflUyY_Nw2G-qqU2WAuca9vqQm77KMw23l9LPibxOYCrN1maCwtFykXkKEf-GiyvhWEkD_OcloG18djz_AOz5xOh1LV3Vp8xLtCcDjBtJIkpTiTvUHztdEHZsKtNUSOdXhAld5KjgL8ev4Y-AUtRcDBS7Gcsp39pgLfJqrNqPG1nQ85XjAt04fXPSpxxcgNMFNh9IGso6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbB9wjr9P5WvqYy_HP_NDn2PI9e8M281usnz2-JKOeEffKdiyQgYGH5-WRFHCkl4UGXERBKpgSnu9Jq4M1gjTE3TIaQoBm4hkNR5JvwKWx2ROihiApRatzn1r1fgiWoQby-xtnIb4BBgNe6ToRiJJ_mV5dHxMg1LWnNKBrM64P1vkeMeXOQVX7WNlzRi1CabXZDzmRU-j68Gn3VDnqKDUJrwuUvyOS3r7iu55gYXPolz1tBMn0b24mIVxW6dpW9QnJDN8uAgm-vnBvAzsV3xmmNMdk-xIPuazRru58Pzm1SduoUsFYQIfgFN6UgP7xO5eyS6R1WgSEdgg-nGecxXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5j-4PVAJSSzOWNWduZ5VK378D0piR0tcREzPXX7OpnhZmXZoXL5y5KC-tuxBWY2XSQO64368twdm2xprIXpbl-Z93-RQAXFeNaFAfm522XH2QJhz35e4N_wfLy6F4pQsNvNElivRfyDagWIVEJRG2NGcpOF_U_52IpNnrDhvtt7b5nDWDCkEWjIkqwIHFEmFtNOxZ1mibBRsH9-LuUioR9mw4kCRaJCFQdnWvIa0nxQXLU14n9STxlxv0Ma8rMFIAhUQzHkFYIfokroPy1F03bz4E5W8yaYdEIuEXmTAP91b_XrNyLS1-HBOjpgost99T3KFY1jO5FKK6H_WZRfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFqwXSjwWNnPIuYOBRaJC0GxP_ZNpNxISSNU-1ItSX1UhAqaK6sIBwXZ3dwuK3eJ-Pqyo2yV1XQEEOGZjezKAWcRjZEFTCBkP7UVZckp8ZqXjQJq0jI5mkCUreG9DOKKaaZi-ZcsvZR8i5LhYn_Elu0zJ-1V16C9nzfrLMYdwECHyCz9kA0wlFq1lPgt3-_Rne6LFRohERIaMCuIgTbYpFALfuJDtx19oWbQHMhHd2G_KYaSifpo_kG-CjOM4jyyNkl9pcZGkQggxONL4RUmqtxCrgeExs2k4QBvK7y_nCHOgSnNF1Mwh07MiH6jLssuoBdHB0sDMgbeTd1yDDVIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0z3FX0bzNXnOTP2IDuMz0bnBS0eQ6uni7Pk9gfuWX_2Rm1Dh89otQCR1_G6prCJkBDHcFmghYuS6U-Kc-cKtt9VgNIAKiBBr7LsNOsRe3WZwqDRxaFFfBoxxcPLVIRxzy2O6nri1_e7oUXLvq8XvvGD2AQkw1TT1A0KkR_HwrNGfPaR25qgDnnJ9wLy-4knMGodY2YpJ2UMoM9H2Uk0s-I3dDti02vV9i1L6GetH9uqLqLgRST3NP5M5r25UkH6nOJEMHhneKtjywo2IjrTWqsCuXLNlqWCTaxkaRo6B0ZTboF5wymOdF3-if-3-KHGeXWsyIX2dlV8VFpGSNyYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=m5_Zop0cPtwsC491ZkCriikvs35OI3mGf3fc3xVmTyc6Z7jofWxqPiZyOkbsT0fuGxHUaxIixsvzg9pA-o8qPiOornUsOQyhF1nMvzDZQkFfU-xoGt3JjqMLOmIiEF_Dlo3_HzKTi6w7Yqrp7MvDtIhDJVQzqDMd-DzvH9Q5DW5fJ1Lx46I8s6IcHymxAV6iIgjpoUogwauLIIaTf9AarHmQ4FINv0bwZVcivw6akQ1Kf9U_YE3K7CF9EeKyrozjNAIapw5LO3jXrfhJjxWPr0aIX_qhRXo_HLnIQQ_wQD0Opo0fhK9xhhL91Htr82grrN7cfrWAXoVa_6embVzLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=m5_Zop0cPtwsC491ZkCriikvs35OI3mGf3fc3xVmTyc6Z7jofWxqPiZyOkbsT0fuGxHUaxIixsvzg9pA-o8qPiOornUsOQyhF1nMvzDZQkFfU-xoGt3JjqMLOmIiEF_Dlo3_HzKTi6w7Yqrp7MvDtIhDJVQzqDMd-DzvH9Q5DW5fJ1Lx46I8s6IcHymxAV6iIgjpoUogwauLIIaTf9AarHmQ4FINv0bwZVcivw6akQ1Kf9U_YE3K7CF9EeKyrozjNAIapw5LO3jXrfhJjxWPr0aIX_qhRXo_HLnIQQ_wQD0Opo0fhK9xhhL91Htr82grrN7cfrWAXoVa_6embVzLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky-qwyW0ah94RCwNZNaZzsYi_IK5Id1XvyfbkMaApBTNA2sTf3uLs7AGQhhHPrGjzEUISJYyEoTqGTsUlITsgbJT2lyiLU_wZi2kmP62Ye39SrpVs1ZdeavBhChL_S9epy4HMfq0c1D0cIObh6RgLZYLEa-v8EVeTdDm38R2v2bg0aGQ93n6eKyP1i_kN-SB2WCa-jo7wEdLSIfgKdOP2eYd9-MMecHL2YJct0OBIIG2cWbzlHkIPlYMBFFtXVz7mZCw7t55CaQ2l6RNs5v4ohsRND_VgeM5r4UDfsObnzNEP-Lzy7hrJvzni3b0f11UD0nMH_ekCJ-OL5Oa7PDCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjsPlmPh3dVTjuib0vmlooIG-jPxN5Fx2Dt-8JV9oeTn0MjMnk6rQvIzOoFRWx3HNdpzs4BnMsP9OyZOCqrdBibHskk8Z-I1d8CnTa0cBQtQHNzEe_N1mSdYbDFUXyxdXeYVsLv0iNwi_5JzTHKV_y6bGMudBzt2E-OAHFqvD8oI1Wp_mtLmtJ69AZA7ANiO1rlB45yQEXkw1RqgP5g-ttUnRFnP1j2GyGYvm9WUAeeO6JG8ZPddrPxWXSbjvANckSOhdnbCMDkQXilKAsorVp6TaLciI7Y2tjdYeMI44GfUMVsDhFjQGJt7-s5Z50dk8b0fflsSm-FAzImkqgrwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCPX20bY-MgwCuZs6J04HwP-4BU96WykKJl-SBcf1UiqlCS2VpLqTpybeQK1OtF6Hq-cWi79dDi8jJY8i3tiaQWRX-Kvcyy9O12eFvXkyui0pWoeZTQQMEHsPfJ_sU_fE8vhapTTrTH2-02_HLQ-aam2Ybc0PRRLfN6LKayDhcFH0JG_0MaDkfgEIVz-nfRF1aPKBIhHORqWEnArhIuNTQWRwTs8RBT-KpLp4ppJEPMonkmq8Ifex5-BZPr9qMhKRAaNsEmk4RLmzhhdUyntP4mK72pqhLHPpWVYVoM48uETUJ9FsQrr51zyHQ6Oug1COJRKZBwpT91_ZtYp9fZvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ-mLBxqFquMgSeyKdmpw-OLtbDbu88Wwq65bEssRwNQFZvYejUkvRyXda5xDVO-LT0hE5pBQtqkI_SIupAg71hmKVI5ONViyLngmZDzoIXY74GGM39JoXQRaUx6VfS3_QZa72yLU62G0K5QOxI63h1WpXTlGBmkWr13GKdwjEEEuxxO85gTMFoP6ndR3morAU1iMn-cKGgIPLczOQqoRgYLZU5BmEnfktbFzQl_YC4cyTmuFdtevC9p_wKxibFXGqSmfDdxvIKBw9kliCpPeWP2bBbitCmc1cmcaDkeSgTUheOiT2R5d1XbqOciNpcTCeCYJ_mn4TDPWLwmZ1w59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOhvKFl39qAkrWoUiP43K7l2c9mPQU22DfeuuD2LfW6g1RpmA2J91plTWuLhT5PAflE19th73SYEMLZtKY13UPt_7jHq64F1QaaQx2L_HqOLLPju44qrPiZco9AObhEfkcmp8eqh_5sN--f5ZZn-nxH8gqLAgVff5ps5Nqn1_LRwI6JZsaTJuzUiGg2eORh-Ei5buPgHCBl_BTUiF5r5mDu2_CVxTLP8fVR88i4miUUVztHVfwAqRGFD5v54RV4nHFFUwZCJeeUE0GmCagqRfZ2-4IcWE7DhUAR4VEgCro6MpFZgZV3zlqZhYm9RbPlWkdVPIJZLlRbbaFUXQ0jgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQmnZPXZZfuOp5TA1ruF21TU-VI7TC-3_V5ViitOnzP2zpz5mv-mbtbzd06ouxl3SjcVulS-gq8tNO6ffhRUH2sfp8zF6Et1QN0fkjN2q1i5W-xO6MpQ58SK7y13U-5tcU-MLTRm3KVy6fK9_lVUWo_MnIi2_h1XCVKFi5teAvmlDi8WGaPpt7zDc4PlKG4Re_pfzquW3cRZAU1lefGhqvGrPCjOeS9W3oEulHzzHxTWpz2ffuc5X8BhT9vMawwBUkNf70qM7BPFfvjbUfhA_lfvZ8Yx9g1JAkXhC_9rZn1b8wdYJabOzrofYwyEjjy8PviiFSwjNhixv0uKzwQ7_Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQmnZPXZZfuOp5TA1ruF21TU-VI7TC-3_V5ViitOnzP2zpz5mv-mbtbzd06ouxl3SjcVulS-gq8tNO6ffhRUH2sfp8zF6Et1QN0fkjN2q1i5W-xO6MpQ58SK7y13U-5tcU-MLTRm3KVy6fK9_lVUWo_MnIi2_h1XCVKFi5teAvmlDi8WGaPpt7zDc4PlKG4Re_pfzquW3cRZAU1lefGhqvGrPCjOeS9W3oEulHzzHxTWpz2ffuc5X8BhT9vMawwBUkNf70qM7BPFfvjbUfhA_lfvZ8Yx9g1JAkXhC_9rZn1b8wdYJabOzrofYwyEjjy8PviiFSwjNhixv0uKzwQ7_Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKLwa5bC1xF7m1iMyMI62CE_s0JkstHahPrQ91PSmkr5PhWYGF1oOrZaT7tMPCTlhU40AhpzUAk9pm7yOQAnxpq8QbF4mD_axGft7LRHKZg79ME6M2IS_xdSCr-rIybp-YaZrqfDOthH0tv22PYceHvTBmNAJMwH2QcB2lrHf9SRhrprW2BHaQ0SjShPlMHQlcbhWyyq9Q2EA2Mwx82vyD2PY8w1mjmpPLI_FcJrRP7sM56va9-68buQqJFzs030YYm0kiCKTwFZ2ntSg-BLFq7gxG5LpDMJqkLM_vRuxkqe784PH3KSa-0effX6hj9iSJ6sqGv_E_pqE-KVMN0QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYMnuubd3n5p7cip_hF4cI06dlN-enYubGg9jD0DdDea6eils0UnFavxq4TtQOc-27OVS903HoWn5B-Y8J8dhdTM1wWRLi_ur9_TMyJM44WNjjmwTQC2VRD5UB0wJ9Fu--vgFbyFWkJ7Ug3VsdDAX195KminN7fQV5bu9Cpb8bCL1a9ZAq4x9bAJfCMhbatx1iyNq_LAtRIbnejTbaejv7kVOgbTEVYNdK19XE48XEI1dlb5Y7ox1UUvybqtsOC8TIermp3nKBw85JT7TNOdTbPOOV7Z8zFfhoCqIFTlc8CTPSxPC5XsGS101Oync_ijcVzbSn3srP3LWDe1tv2Sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=XKtWOnckXQBVGaOWMV5yMI9Mhczg9hfR8yQHVj4_TLH0tBejukxLcLG720ztVkxxUv3vEgz12OUoniDl3jEBNj1NnHT0NgLcIEwLQh4CWWSz_KyNNdipKK0tJMB03Uol2fsIKmYUk0sTbQOf-GRGq2ZtJXJVGzOGnKS6xNgSoETOQH0sqRFt6ue2Jif2SN_7frx5YPHLBfrLTXmfCcHi3PKRlWYn2C5nroMrvOKxJ9knWXxL9i8IeggFqqhr8--eCXwkaZEOYl4L0111Zh6Pf4PdGJDO49-A_BkDdmOzhOsxRPZp6aTgw_oNDGnTnk6_ffDcYMeYH-jnS11E-ywujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=XKtWOnckXQBVGaOWMV5yMI9Mhczg9hfR8yQHVj4_TLH0tBejukxLcLG720ztVkxxUv3vEgz12OUoniDl3jEBNj1NnHT0NgLcIEwLQh4CWWSz_KyNNdipKK0tJMB03Uol2fsIKmYUk0sTbQOf-GRGq2ZtJXJVGzOGnKS6xNgSoETOQH0sqRFt6ue2Jif2SN_7frx5YPHLBfrLTXmfCcHi3PKRlWYn2C5nroMrvOKxJ9knWXxL9i8IeggFqqhr8--eCXwkaZEOYl4L0111Zh6Pf4PdGJDO49-A_BkDdmOzhOsxRPZp6aTgw_oNDGnTnk6_ffDcYMeYH-jnS11E-ywujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hePWBFqIXqrOkSMcQVBKLvA9vlL96TK2Pjkcv6vKGc8d_X4FncGmHBsr7EANF3jQjmHw12j-1CToghfdVSoDmU2H92c_dA69WGEiclMIg82XNnfpSzRyYZ7tbz4L3ha5ZbiAzV_eJwi6NjJ3UCKVu-wPtam1pqPchEsmBNkXtxQc5ZXcIIgv9uzr03HGRb5NJrb2H2mwqB7J_3ZkcVOyl3jdRPqYYc6sAp1I3ixO4c3S140M8Nm0JjO5tuEi7If_n_nqf4eqpgHYP4Ud_22SFlVB6ClW3oLu-rIPuW5SZMv04Biy7C6Z08hbvZMOSKRq0E7Skea5bbR5GbTL_tUaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=A--nBCgjfHySVv1yegjYMWfC4vHa56cuZuOI2q27rmXriHR2SDoruLLxOfT6HmHbySLYlSZyevlpTAAJXk4TFuo55H-6GtpSExyDvmiORVQQSfiTkmDKQNVjWvVzi8t4dyX0nyI0Xx-qwh9hK6ygHl9k0y9LOGqp6_TpG4Y5coaJTcv04UgOO-eMlGOEXTsQPVEcwtoYDOcXMRnM9AwmprspTMwDpmg1vGolr2ekGpL3y53rfZ9uwLM2gk8b4K-LOfefFsNwJaPlmBpOBIwX5MWYuPUeD-2fRil31xSiKJdWwPoaz_-Ub5mMzzXvVH0eRz6lA-bKa1C_rUVXmlvu1kHG7xF16WTXCRNOnIn8gk1kumB8YZL2Bm9iYEP3iYQLYbpjJiyfjuz0fcQtXzNaKExFqaeOCJXnsLwXQI1IVIQ4hdLsQNmssOGyj0IumxbKHRKVOaQwnVocehdoxw1N8TzBfp1ncgop5q5jzAd3VhdBSepQUHWoXDoFS8jA-RkdgNch8OXqBCZQ5T3kyYdSyyrB-vTQzgwiFztMtPeS0Gl14VN96wByGynwHU3zR3HbtsAJ-jpbuwmpRNAD0oHnFwHF5-XUx9qkad84CT7L7g6Ouk0UXVhx6-XBjtkj48dnadoyH3b0XendN_5J6sXvIJ2UetEPBCugHkBW2iIJ6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=A--nBCgjfHySVv1yegjYMWfC4vHa56cuZuOI2q27rmXriHR2SDoruLLxOfT6HmHbySLYlSZyevlpTAAJXk4TFuo55H-6GtpSExyDvmiORVQQSfiTkmDKQNVjWvVzi8t4dyX0nyI0Xx-qwh9hK6ygHl9k0y9LOGqp6_TpG4Y5coaJTcv04UgOO-eMlGOEXTsQPVEcwtoYDOcXMRnM9AwmprspTMwDpmg1vGolr2ekGpL3y53rfZ9uwLM2gk8b4K-LOfefFsNwJaPlmBpOBIwX5MWYuPUeD-2fRil31xSiKJdWwPoaz_-Ub5mMzzXvVH0eRz6lA-bKa1C_rUVXmlvu1kHG7xF16WTXCRNOnIn8gk1kumB8YZL2Bm9iYEP3iYQLYbpjJiyfjuz0fcQtXzNaKExFqaeOCJXnsLwXQI1IVIQ4hdLsQNmssOGyj0IumxbKHRKVOaQwnVocehdoxw1N8TzBfp1ncgop5q5jzAd3VhdBSepQUHWoXDoFS8jA-RkdgNch8OXqBCZQ5T3kyYdSyyrB-vTQzgwiFztMtPeS0Gl14VN96wByGynwHU3zR3HbtsAJ-jpbuwmpRNAD0oHnFwHF5-XUx9qkad84CT7L7g6Ouk0UXVhx6-XBjtkj48dnadoyH3b0XendN_5J6sXvIJ2UetEPBCugHkBW2iIJ6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqCI8C3yhvXnglHbugZcHhRtHzQyu7kAZzuQ_wsvFgK5ZrTWK7iaB20e1FxfoX4MWss-OK0DCrOE8ELKFtPMCgFPAiAZRN06zYgBkKvmUDkRrZ-gucsbeqDVFPxaLjMih8zfhDZpf2aQiGlWm-4LTIzF9k_U2iM-PHQBdCFXhLr-XVrWierGCGvRlWks1fn_9vDgtjvduTPjHXZcc4xiqMHs6R3ylQOxpVqyfHbJg6t67cvOkRXHPzCCz9ae_EMrUIwmq03BOaZa0HVUf2irLT1zCZX2ZiA52idSMN6rc2pk_k8jlQv7BAt_Ib9lHxpnbmoXojL0Ko1T40bICnXUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS6Zrea2FgV4q4-nw5mkNDuv0hXrRqXYO3qOVf9Q8RmLUx0AgRnXSogsZHNC1vrMxGEiTKMejj_MKtYmBQPa3V2Ss29HBfeOY64rMnwJnsgm_A3Q5Zcr2oBsaL-Kw8ePv_7_er7dL9WDnH3rlEPmZRFCBdzG2z2j1eg94pDDHpHh6sX_jSWOggYCAzsClegjW8fS-2zMG6cZRk6IjfGGZO-Jz0Oo5uZSVFrcPRXbUJaUiKrV5jINE3iw_fubHCJGdxYQCOyKkX5ZGA1m-F7Ww8_EKZzMDbdKj037CyB9NoPPAxnlEPfTF7Dbb_8e8F9zNkYSc552C2StV5joGQOq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_um1cC9iY9AIiY_0sYdQF66OgsCZUpAinQn8QIQZRbAcnCNBgk5jwssOa_FhU1njTLWjAPI8TsOKXEONEHoc4PyIi2JUCN1IQkwzWc6n0Fz-YdsCuEERw3uK2G0c7UTdlGPEqLqx_MXuyw682hgWmsJl8wqzxMmwneE9-KPZ57vxq9hWcBj8ocy4zxnj2FGRe-ZjFCYxIcw1AS01lmu_ZflBX34u5BC95uwcSbBlXowTrAgxPpEDeh3RdziLLdoOWo6M5neQ-7FfQalnElnl0QA_3PlRurip514TjWFQopva71pArpnXUGPnZBMS9ipW5HVgYlb32pkqSG43mw24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=nNzRvUtyacdARVFzYZTxqJ2vxXgQI99y02p84qxXq4v3FTByxJjy_IJEq5w515lZXCd4K9gWq2kreO6b6gLYA6Lze5rO5o_3iQ0g5mZrWR0kVq7KKXaSyFuI7qvqE8WLNxfrHRt4xNuSSzwK0CvMBiTJh-ZSErVdPxeHJdG1ThGe0NNiY4A7Y4X_Pwh_q8k9yr5IF_GiqICBbZnoER4X_XZgkzkyuD4lU7E7IklZ8F-uwZWLOO3wiJvCgEQ2g1TyA3wYfCsgwl4Z2teRUHzo0UI5eyiT0QIrRt-La4DUZIG-n3Mz6Z3v9aCGTlmHiq7xxXd5ZWpNeF6cVhYz26sVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=nNzRvUtyacdARVFzYZTxqJ2vxXgQI99y02p84qxXq4v3FTByxJjy_IJEq5w515lZXCd4K9gWq2kreO6b6gLYA6Lze5rO5o_3iQ0g5mZrWR0kVq7KKXaSyFuI7qvqE8WLNxfrHRt4xNuSSzwK0CvMBiTJh-ZSErVdPxeHJdG1ThGe0NNiY4A7Y4X_Pwh_q8k9yr5IF_GiqICBbZnoER4X_XZgkzkyuD4lU7E7IklZ8F-uwZWLOO3wiJvCgEQ2g1TyA3wYfCsgwl4Z2teRUHzo0UI5eyiT0QIrRt-La4DUZIG-n3Mz6Z3v9aCGTlmHiq7xxXd5ZWpNeF6cVhYz26sVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTbUAsz2Oa_ECHCMqlbRM1Bnu4guN_QyZ63q1ClBhyEVJwH-MNHMCI0MmuIiAcnz2BPwguRHDDMrWypZZUsfTbsFiLHBomwBW0h2IR-v4-KzrFZftsS-tha91lS5AefZCcCAv1D-lPwYQYK74J9GK6RYsioPzMnHsqJEeSEo02ITHD9EtKP9XIAeKb4zdYaIjEPs_A23CNK4QmrH5v2LUjzOHj5hrrb8odwMp7_ciEppD-eo9xm6YeVm_hyxwU8snJHYTgpDY9yIMAonLuEfpthU3Gz5ebdW49kpjZVFmpZJUP0pZsgnI7VadC69fTz7HbbtLGH3lQa8xGkJIauCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
