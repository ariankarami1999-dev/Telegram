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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 13:40:51</div>
<hr>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce_57n8xP8fj6w8xEnnhaD8iWEYuRCp0E-WCZ3XidBPWcYE9A4KO5DzTj2kMp3RmlRGVhdLWOg69kaRJaFC9E2MlY2lntAJUWOnr04Y5OKRFQo5H8_43XzCaDT_ZK1GJLb6UBShOxp_tRxWlg_O0zWSrOEo1p7RV4qmwXepkfaRI6Lka-9g66qdRK0q5aIdlqCS8p1MU9aNAeXa6IlQlvDqMAjOHVFGw6vu7RDnvSnna9SqSqZpWHvpvYgDCQkbyZT5GIYWsxukJvxDZlhabWmQQG9HV-vjeTIlO4RG2KOwpv03xlULwUYhRbNTx1lyKwLTdZMTQWJazerOHBTjhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPfZ-4_YgjAumi9rYQ19hCSJ0NnRQSrOCPOrNPCep_t2FggqLUSFDyorZm3dvcB5jP3ZOjkm-gqUgg_o21Ohl9dh8Iw_3NuRmcRe5EHs-_7MzGYBDrwD9Xyc9REerbMdS357OPlVMtEedMRTUyUMfvYo48HIRyGq5szyEvyvgLZoM_Bqfd-Q_qk2Fjc1dohk54c7xqqlnu9QQudcHdV-zMsFLtqbHQuyh19Z8jcMu31FgqQBRVFUXP8K4LOuy_ULpkzUJ5LsDBGuAkZBNXxi5dA1lmmMByLF6Yz39JGEKxiwp1zC12gahQpPbUjNdBQbgtRD1fcrH2j-t9UuAO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVc5TroZW3eTXjs9abQ-L1EszDL47znjY3hazgu2Pj_z30GcXB52lX8OrSydC9LVVXtq2XILvlKp5vsAz-VM-wWG76DF0l2STcbuA5AAx3_6xvQJSoloroHnaamyNDKb-KeTtbZJTErDcDyD8IYi6m8sqwEW8CLz-tdqgZsv8fnJJCsYxEa6xBVCC-qURAvMyqdyXvxk4IZo86KZ1fj_Fc1_O6YQ4cFaIp4aoLyirG44qUP-TSuq2DudbXM72_5n3dpzHKRCTJG-7g3jegWB_kXkc03WAw_3bZtZ-V-9O7lqE9lhEpVMAujUlPwPYu-GHBi2wp59gZ-fpPhI7YtVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnN1IQg1SXn8tC4h0MKvxcb0qkmzXNtqLFeHQ2333Wtz71zUz1m36Ohjjlovv3kWqIPaAcXogjaQAcxM9ghUxIIRy0ah6sL_RU09I3SdcddhLwOSD5YJz-y0W86zOqQq8MqXyS53DwzUUIHNpec9DvMt-M-OUIoSSUtNCYE9WXoSXoMuUosiFiG8XKBL9MMcA3XRg388hQBRHnXNkR7e9YrZHxsY3_EHujxxgmliu4AjtehlY33RRFuElrZPqzSnjElJcnmXbTBNRJIhfcpxv_UvxmIrYAC00IZf9tZOKi9-2pVeceLFuAkvntWYIYXc7-lNyWCWnaQh4BTPPGuRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e239GC4BC3IjqDOipMysJQt39GxZ-wY5LVRx195e2iGyp30O7C_eOVEv5D3GmSR69GAkvIcDTeTYmEJaFu-nZ8bXRiO-E33Ka-3X9ZF2EzNYUFRIXi8V7rq-WvufrJltm8mQlilCDPz805TI-R40qNhzh6y7VJ_wP5UBLBdb3_TjMRT9fCwlQQDpoT4aNBODPwhfeY6Chtye9o-V-vi0rxsfQKunRba5kPnNXIXuB9BFVdQtM4D08BkQU3zp2M1DuQRkzaXafHAGovApQGuVZPs-yzRn5kEMJ-6H0h06sc7NPITJ-sXtQR1a9IKorBLnZUmwRKTGkU4esl0PvWChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6mHlD_svdZJkjH_OHuGoU6DCKql7aqP1PM451Rm2VvyDq0VW2_0Pij2vsdtDF-Hq_HVz5ip45eHSatvzffEkQ9u53ywOVxsPjIQThqFKIjjw-gYnS7WvImC4xND1-x4TgYxwG8yCX7UUVhpLoE0hoabVSdrOv9y8I7Sty7WbyWxf8rSaSFldfFNpG_SuBBkGJDgn6mM-9UBVjEUPYd9XiCoxpqVqQH6RXGldN645FU0lf1hVWduFKqIqWD59lfES-djn-1LN9Qm_8WJ2e9FaRN53YX86EEQWS7ouVA7jPPlraamMC9iLFXZu4OzqDWiIqXmu0iUMLo60bg1CnSixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwI6XqoeL7xi0vk-ZAW687-dWSIRw-2WWjV__ft3hg7anvDhz02JHZQirZsVDV2CgAL47iNU3OTYFodOuyjo7QLju5CjvxffpmXHwkBK7w754dB0yBuzwxfAnATRjUr4qSjHRzgdh_EwjIl5kFiPKZQfG7_RGZpywJS6FB8HRzdtjjY8rBAGUFVJLkLOpdZfH6TM2GqGklTfi1mh7Zq_R5NPYIjsauQj9vxOk8X7nQb0nCpSUBg0nbQcG7HCeP_VgG-7LSbGNb9o2e1KTLnmm1YUNGn2iTu6tZlTey-Nentpdvl96RKuF3nKm5B0qmzuQKNhKjfJ7BjNVdS4JCLamQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZVuuOr7fEuWh-p5WCn4C705BhE5pcz0iAJ_RmR0HK5sgLxgJgBIlw1Lj46Qg_YFAB-2I-_jCxWtvpZMrBDQsXozmMLob9NCL8lAor2K2RVGn-49Is_MQHfm_ynBz3mTpurXbc-LY_hT9CN6eMN55MIUyBBUwnI20GU94Rzq1165dortjoS_dcxgYxJa2IUsaiT8fvHnb41npD3DuCsl6gnDW5wo303hn9Rc6EQNcqA2xZanjOlAvgVPa3z2XUNLot1MsCkwmC-0D_WHFbLsPrnEKAd3XIDHGr29cP3NUUYzVFI8xGBApQ7VJcvWXZJ5mD4xYT8RI796OryVNJgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdCv-1SYJvM-X9-VWHQWkAh7iDBcwMQcZz2iVNsksP9Cx8ssg9Ez6H_Ol5Ebv1K1bDoz--55Oxe5gzdrCE9z9ZuCXb7KvUUGLzbgDv9-kQl9nBytLwg7Qs8ozz_c9pb0HMRs0QXBgGHvbuxTBMfA-Ai1xIwA6kFMV8ypvm3lVppQrMnPidfRTJCfOqw4WFu2KkmMtSM_BOS7NTZ6SrTUyZMPdyh2sFYI62TilhTaGrDezrScOO_rkPO3HP9tDvwb8rf2t4y7wnu3dbok-VhBsrpDMY7MLhFsBQqEdk4XiOzsd1Mw5Wxtc3EQinzS0wVPcv0fjo1bYUKxTxrDq8s1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGNyUBPLP50kfBtnMzTpuImekYJen1q3J7RScCP7mcgnstCRFprR9nAYR8R3IK10yRebufCsS2dNi5SILG0jKQPwaC5IYX49OkuM05hPak5ktbG0ZdgF9Nu67NZsvtkCAPASQSA95pXHeaHZ45XntZ9UQcdB_InczFGLOpWcHbhrHIY37EW-hMR0ZNBNkOjiy6oReYVzXT6yM4POVIfpdJy3IlttMxu0cu0wI_FKSBqC_DeiHIu3XAULGKcvn0lJJThm3XQmfIb6Qdvknaw0x3sj-Hy37s5fzPpN-HZeTONwBBqtIPZH06mGI4400ocSm7AAz6eJrBGdi-mUGGKd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-BnDUvRqosati5qeGkQYx2Gpy8JlXTRxG-7lv0eKKB8iLXAygK2tUaBioCDA3WagbpaAjPcyDaaHA7qPFu3elV75hyIHw_b81rIP1RZtiiDK-rBPHCxlfnxLPw14_Pl3bHmCBUy2EeLpeAQj12TcJvlTwkBwnyoOSpohY3XacpBurFWtEjT3more-gB7_3TCWHL8njOAtzeOBLarmNtCNd8t4feuakHsh18stH7kvvUaL16R2oqQrVtHAmXo7KTJ0YcIWXRghSDQ6xumRK-5MtFKGWBLAxYWifserP2xM_n1vFnWCD3r1HsKIgv__CUWCa6LCsL44YtGw1iB-TUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlYlHb8XzvaIxsL9w2Va7XnpRwbTrw4q6AsgE35qKQQu0dczO4guMhDa8h7DxsflH_va7TKlbKuLCCrgTSYG84dsie90KJTC6zHe-3nUD9LU7xHDOYjR5Uc2o5YSL1te9H7eGp5i_dxqaO9hNtIRFzFQf4KRlsEKgZLIne-b-RVKPgC2Dv-GBE1_ZDpOY7naE_sloQjf7T8AxVLYhTqBkvLSNJ1cbQoDS9YJD2p7ZyhEC8rF5PtYmmdO6VLmOyPbBhjIW2eBDqG0rv_a9d1xbvNbMQS9ZIBRHOPBArrPSLB4E4WbdzVKQRNbK2kLg-asGOWWL5OOjaZjnxyajBmLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR5gai1hTYJeZ_I4cj948nsmRGLoxiUgFfqEjt2m1sxSu2q4lHho9IOtCoQNRhM4fkKxNlKv0eG9JQM_x2C8pKwkAgIpgXza_EqDV2-hOJEWBhSlEVU__XE48as8mhw4JVvyhYI-ccoE46XUfSEI0Y0SiumI3T1gxZ-s3E1vf_El0GCqm5t2DYuC5CCvXRSHa6k1NhzfXRASaKkzai8PpNPpQVy1JUDwVxOYITIEjEiQB1xpPgDumaNzTHSClt-LUveZREltZOteViQD32S9mw_w7NdHizMjLqU9MsF9qLImErIJJ8pCzGJKFwg4Uox7hrACywWgsEQ64BNtgFKVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui8_R_KVkR8b7OyOC5Rq397-Xi6IrS46Kkr__9GpV8mmkNZ_JbfD9XMLAE27ma77O2JvlSz-4FHZv6FZ8UC9guB9YBFFYJOnYeC4Ap1TrMpNlpe5tckjm9sJfkgZh7vkSmqUElyuLlAhV_E7im0SC_CIKjByqd7P5KWK8KGRI8IJAw-7v2l2Nm84u_vL0qOTvQPX3PxtXpM8jehJy099hKLVItFiv29e4dtr7i1z2MJBYa4jBohdLauvpEuzw1wFKuVufsZcc41gnKTIaAbjBK1UMYmhXYCqfjlTgB-qoAYG1pGXhP0K7yKkYiQ93D2uhvyUmINUR21D__vZpDpGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwuYRNa6cnT9zFQIrLlPMUbGR9nuDDTM9lJ5WYB6glM8Zjuazz0LggCb9OLlUtlsqBD-yvXsrWk3ywlqxRQb0EnLWihjQcD3CjLyqI8IpaNxVPcx3JnnnBPug15LW_dEHTyK9u4oVrYF05eCA6d0vg4owAp45f5fLJy4PHeGJjD0wdL54wQm7tw5-K-HLc0yblApF6OG1quM7ykHGl9yx5MHd2Xyoc55ym77ViBK5wmm25-4gJALHWe-Trq_z7ro6BCbyaYFyq_sL67tFqhbYMa8Dz9MLKACYqKHrQHDwB8wUt2In56K_xBLZTD5CK7GLi2IpwX7gphAlW5ytLd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-p75RkpeshXIgRwnFibdqKjSKEaMpyqdr1sYoh1uf0KKj-4kKRl7Lvaa5vBKZYzAORxLSJFX_TT3uX6Dv9o6qbZCeMVJqi4uoVDSOfBW_09gjDOZBD9VowE-58bgh4oWfEhXf3WzbHn68dGtCievgOC8knJLsfvFuZXuUEC3lYI29yCLTZ5F5rX29BW1dzRu-AhYIm8CfHsefCyiiYRyjWm-3WOOIyoIcc3Wz7B6XqS01bQcgrGc8C9udjft1mGlsTTK-hPbAh91M9hJ8CH71cqZDGWvqMWEKoLiDS8BbJzLklKnG82fO4jqYePcX2nib6M4kGBsbJjewNMxPlw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXZVcM6POZolmrDd9b7HeQx3TZnG_s6iZfOjvDpyUdtIkMbje4hhnMRUy_VYCtq3ijWKAZlXX64pqXtom62X7wIfrliJONLPjz8tC-c5iMv9uqzHS-Drcm9m4-qUMAVKXys_UvAfPBfSk9DhAuQssT3Y0A3QSzV8jbjZqdOly_JELig1PEU47Q7_sfEb13vPUMEurxWqqUBEQgo1ced4BqIKPBOQ75Ro-4dm8vAudRQgFZGvjQIHt-bTAKd3v0hkdd-3jB0l6PRd3q9w-tnIDMs-RuLbTaJkfPnKzofwlTuCCL19XJ7jsLKYWbufafo3ErcZwRuJ0B8cmLEPSRgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eke00M23YA83nOZLmZT_azxkg5sl1IlOf1GGszyzysK_EHrIjhrBuajxt1e5jaSrb6Si4hctkMr7fB9iQNQFlGqNCzYCzexXivWxh7kDE_Z9iA3I9IwxCNDPQLCrP7mCpRnLBo6nLhxTDY1XXZ6tjSERauYf4ng95rL6mTQj8_GFN9o4PH7qnWbV_OE-GQ7TVUWmI-GdrjHfi_b7uSexMEfkm3Q5Ak-mguYqCgtBV1eB5G9Qb50FRyOFUcVMIQZFzRUGkYS0u3Dcm5SPChZHRl-dq8AA1AGdMuCZwmlbLcY23xAx7sHCXWIGkaJbNX6HIv01mjkca8gPV1j6vyvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBdYO6xkIu0S9-9hoGCl1iSbuk-8ELDB1f3eXTmk0b7HbsUzvjaYh7VMbnJnvo5JDI_PVnwPg7BAgf-rSjJ_oai_dl5TezvVomr--Nw3pBH9EOoAM82af4zykWLRu7cTcIrrZ9mXo9rdaUCtT_QObg-V4Yxn-F1RJbtedjHoe83RRY4_T2UqHdRwKihY8se2HsEEnjQI0y3X6MnatkPd7zu_YknYVMNI89d0iDDCjXxnvg44-79KVUEF-98HhamoSZiLXiJWUdAvYHeyBGFZen92oNep-faYfWwkeYKN7HRsaUixScXCwYKFj4gPxNkhuDcw2LKLcLMlCLTwxegmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMjhljuRqavQoh4h0qkuQmrfkfZMHFEhq-mj2jGvczhrD7SHOYBcbsEfEEST9TkyG14sSwiZ_XJKPt_itvYCbHtHsXmCYyDlpqzGVpBSe6NMYl0PpNva55rNozystNncz1Xh5Pc1nmTiTFZz5nIubs08BdFD6AAJHdHW7A1yMAGhKbx_5KpyvUQSl05iVQLY6-nCln4m8eWxiuEBiFji2eqgmb1y6S7Y4Ec7eyUSEwM-j3nIy8SxnPmqkR6yTcmr18m8ifr-PITgp6eaYhi6WwPWscHyhsOFVFu1oS12nHrjkZZbYGq4GKWJjbAmTfTygPiJcypbMPFqfBz-al6bLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4GR775Lf9IvKuBnYXUVrd0kmwe1Wg3P9SH6QgH0ftxiWxBwgivzygaRanQ4kXnDdQgOpbzbpGO1T9KjEhBEmphn1KFSW24jRrelpcsFMRtyrDDw1IeR8e7yYFO71CnHw5Nd_hfjn-wnVvQOq_odFTRrLDgwHB64UpSKzEIkjSxzQ6aqwFSswKyj-t4dkWIQfldfedmUOuyxJuuOAowxqnih-zG88hzIdnq18IZc6alFl837bghChZ-VWinvZO9Sld827yZmjd7PSqyPo_faTsgpIKyMFHaSLvCzisYvcGSRiGQcGIhwdlLwFyrFG-xamFACa6BzIDsXqNgeuEZnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=JQPzVQHer6HW-w5flkxaWxfwHd3tso5w94kBoNCpwXudJyVGb2j1h-a8jV_iijPoeM25W_E378YM7idhrSLuOINyovRryTvTi8U6zxkZH6dalY4NGylBJQqMlx3Px99XOTBG3lNuB9x4KAKhNvQjbP5QLo6s9MynmgwLc-6iMrNe95UNNqvqnPiVh8kGz53ntGO-cMtltOilWce_aBKBCr6lpTSgz_ofl9bFFv_du0T8qm78g5LZx4fb679sNg-FT4GGypgusS0mYQUsBlVwERvaJsoMm603u79mhGArOKuK9-9qOSU68BsMm0-3_h16V29pmLJca4NNNF1aqLIBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=JQPzVQHer6HW-w5flkxaWxfwHd3tso5w94kBoNCpwXudJyVGb2j1h-a8jV_iijPoeM25W_E378YM7idhrSLuOINyovRryTvTi8U6zxkZH6dalY4NGylBJQqMlx3Px99XOTBG3lNuB9x4KAKhNvQjbP5QLo6s9MynmgwLc-6iMrNe95UNNqvqnPiVh8kGz53ntGO-cMtltOilWce_aBKBCr6lpTSgz_ofl9bFFv_du0T8qm78g5LZx4fb679sNg-FT4GGypgusS0mYQUsBlVwERvaJsoMm603u79mhGArOKuK9-9qOSU68BsMm0-3_h16V29pmLJca4NNNF1aqLIBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alGRWVYmul9sl1JYPSbTelcIFebyte3XqVP1yRg1LiYzahXATGMfunxtXQkorDLPVcR0Cg-KAmFZLSle8MSLV0JP9ee41qLzIevhlxxPzL-8ngvgzhXdmyE4OTA9GNYGgofb0syarORTp8hj3dQDhqHmhXk707f0OcfeEcbBy98Bs01IW56WosPUMbD2dYJitWcDNf93dIRVU8f46wGLXhGKqCTMXF5ptirf7ZhnmkyM-6OwWdWdELN8Rqo9Xki98IEnyHOEI3o4pz0p_pJVsonPsnLDw-HNLcX4_L3dga5KURnCMO1H80C1G5bzzhtapwSHS3DWJSqLEWKavlCQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd-9nBupw4w2BspoCvtWvDzqeRPInKyPdnFevF1oolzjspFXl1aJvRFDbRIMyWh8FuiIOH59KRmDPPuFcXd90LKHV2Q54-ocxoeKA2NwwwgbpHyBJXJ1BGbteaM9YH_g21kd2aDhwf4o7SWqq8aEvJGyul_upZFR-ywonWr2sEWRrgZeJcIp2P4PP6nbbF7fossg6rWKHOpEzUef4ARIIU_jWZcrMMuDNXWvBPO_b3Ck5GBSUG6zB9BzE2KbA5N73aBVKHtZm9l8SdwAzM28qpfZ-ud6-Bx95Q0JuZ0kHaRdSZ6IaXsPw76nLXg5wI0cp6yeYVH0rZ7cXlTmLlag0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbX4HpqSPxc-OnWGBSPelJXCCMnDaWnmAwWCV_DPfBCYflhjh7u5znyyP6UlrFK6J5Bwb71yLCtBGmKqVc-Z6SUB-9xT-0Vipl6RoIRcacDojdcbFDkmUqQOeimkKHDasEQNXNBsoy58_H6dhpBkD_SJeFrqH_2CnVKZhbaZTMyrY5Q91R4esrwSnWJVDzF9HRSAs38OR7cb6Dc8uDlVR3qK9qkSYgFxSGhamZ3R-Qf1kZvuns1Yo6RVakVcG5VF2T39FGR2XYLq9Tu7qyWO3Rn9kRVquQ6YcIREUOAB6SpKyPV7HyWErbkcEsgfgbANntYXPT4t9K8lvPxp0Fj8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtqUAzrimWCOgDu04bQa8rVBCeXsFWbCbzzpOXER80jMVM9OjHQUT8UVriuK6XVxhaiahSczubenxSoBI4OrmM3KPIUfHpQazTCVswmSTRPUNgc_-RKqDAy9csYdGk0InU2D3iSMZiFTM8jlnlc5MPJwWMd9gEjZ4XrFuh7Tq49PTxgu8HLoAvIpGZIjTLcMIqlEl34zXbS2J9Tlx42y8x0-Q_1IQ1T7MUhi8lEFrw4wuzdAMgypYCbO1PQ081x9aZkvVIAYby3br5fT1d90GSfPn1y4zrFHgd0Lr_gMHoTrDNFARygMCYSo9lwGhQBboYZarNuYklq6PqwKq3dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaelsO_O6jb0TIfWAAqHYkxxyBrweDHOCpvigSXr4zuz7483EyjLmtNJvIsYwV_I6vEJcxYIICVQ1YpzXp47X-sjOopSplPOWkWAcB3mSVeBpKzuCcE6vddCSwsRRxwX4fvIwGsYczMhsBN0-wpv6pbzs6DeDNK_2ZQA20WBFSENCH1pzRumB4tlndp1JDz862oWY0MzWzkbP-uOoBUSC-Lujq1xsHYYN-Iqz7vERv8LXzyekmQxdxgrYlvdZzX_EFCX0e8VnBwdGdPk3jL0FfmvF8BHI2BSQzzb496rlo3Enwe__EywrWkvKf1r6H3zLuyVBlTaQHhC3DWdQLlSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWVUUvLbx2SQSR2mpvKcuSqVNPjpIbKw2JioCBImLT9Wl1gFiCrtdYKwNaPgohk6gWrdx30ZZuZCWyMNdJLu_17_VAWoMbPSppP-nh2OgwUax8TU9D8k3GtCeYgP1wnKMIQ15JLus34UDowPaO7MJySggj3zE7kZbcWeNBI8vxH4QqNKMxeS4H7BjAbpAdP7Q1eGVB1RLIe7NTWJbmCUZnSZJgpBiok5elqKIb3zsQp5Zg20WlvgpjFNeWMQDpexD7pjX2URZ3f6AbfrHhZgwps8F2nlLv-HEiuKdDihmgOiYh_6L6qomqo-tt80aHQvlgNUo7yIobs_YB_b4Ww-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3QcgY2DZ_skouNKOTkx33t8RXbk5t9f53sB6q_NLJhGaUOeyYIo6Aczc5ikqGAEE2go_q5cbCdGxOuUXeOrJkoHBYRQo1Jg6yJzCqFwXsX5q7-1UVEMPPACSlNEwd683Hk2myfwliqhczmGIplIbPkGQBft98YYvIvD6k3Hr8ZMZVqcEMD-g9z-cOidCi9P0uM8cKV3H7kwCOgKw_PXbtnDLz2fWl6ly0qPlFpddEVrYqa_iklh0figY3GFOyOf6p8a4Ypgs5CLbEYqosievzwmMQ3o1bMPxeIbV5ZI9TbRkNFDjGlNOiTD-Mq2ewpEbw0XOPl2iVlPFNJ1aCgDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=dygh49HM_R2mN2mtQy7KOp0Es0ctEvf3IwJbpvO9yYLeqI5yZWVtzLbCK7sZIoVRaAnn1we5AW2nRgnivyoV6lBpyqin4DYqsxAajVVWXpnH5EtLrUc8vgcJFn1HoUQ3qoSbp4fLBhIiE7ghGr5ZiTpWUJCRM1c52_sHDoidiikXorubryv9JKMebfArTmhl4klR5YH7fx-OoHwEsXvVwbgexjPDASHQWAlX_-eGsXTTEyVDsDs9pAku3849E4SJ2ZnHMbCz_QjyucURX_J0aa7Q1_KOgvtOWTGu9PsAoee0x11sO9KS69NKH7dEEmf2l7_u5KZr_eig4H0b-hr14YLLbgOslANhbe1gBJSxtZJr3YrZET6CFknj6WFFu-7fwTJzxO9V9lYEQnJxRW8vQhsXsHcfMuWk6J5hGGet86OtBbxCHVb_ZtbPI2S6mjKSQ9QDeZeraq9Dg2JHCOzOYN9-4x86W9uZCgUmBxP6evH1_EqNdk8R5sJkfiKxBCdxZSS73zQevyq_HMBlRQ-GeAsu3TC8gI7-Vu0_IylBkh6ueBs2ciSN4azvPLY4FgT_bDAqoroxZSYKij1Br7QesdVUfn97Sy9jDGt_Eo2Ge0OyeUt5entDOGzo3HCWRO5PU3ABezDA8QLCwNpvf_V9Gy4sInXDsGotVcdTL5uMSzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=dygh49HM_R2mN2mtQy7KOp0Es0ctEvf3IwJbpvO9yYLeqI5yZWVtzLbCK7sZIoVRaAnn1we5AW2nRgnivyoV6lBpyqin4DYqsxAajVVWXpnH5EtLrUc8vgcJFn1HoUQ3qoSbp4fLBhIiE7ghGr5ZiTpWUJCRM1c52_sHDoidiikXorubryv9JKMebfArTmhl4klR5YH7fx-OoHwEsXvVwbgexjPDASHQWAlX_-eGsXTTEyVDsDs9pAku3849E4SJ2ZnHMbCz_QjyucURX_J0aa7Q1_KOgvtOWTGu9PsAoee0x11sO9KS69NKH7dEEmf2l7_u5KZr_eig4H0b-hr14YLLbgOslANhbe1gBJSxtZJr3YrZET6CFknj6WFFu-7fwTJzxO9V9lYEQnJxRW8vQhsXsHcfMuWk6J5hGGet86OtBbxCHVb_ZtbPI2S6mjKSQ9QDeZeraq9Dg2JHCOzOYN9-4x86W9uZCgUmBxP6evH1_EqNdk8R5sJkfiKxBCdxZSS73zQevyq_HMBlRQ-GeAsu3TC8gI7-Vu0_IylBkh6ueBs2ciSN4azvPLY4FgT_bDAqoroxZSYKij1Br7QesdVUfn97Sy9jDGt_Eo2Ge0OyeUt5entDOGzo3HCWRO5PU3ABezDA8QLCwNpvf_V9Gy4sInXDsGotVcdTL5uMSzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAiytFlId3K8pZzQBBO_0CXU-vfHPXPaBRIt579pFnf85ps0Fn9Xx41nzWqPXFTY97yZYxFpHUjlJO13Z1l5MXxPHj07NACRSA4mFukabBLj84TeInd-N0DOFxZFjAESOetodA18kBqN6nMWHRu4cNZNNOISVH49IgpSSfERl09-3kCbqiHxn5zBj0dkbZGh1CEHG6ZfE13qLXXy0cotShBF8WXf-TBbzXHruxg7flLuYNcKZJsA7wilRnvf1xUqIETBzAv2rX5V_miU9vf36LlUtG4MPuc93YMYX8BAhp2OjlQTduhFIJkp_lsAOCLFZ59tOAjyTTJO8WabmER_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3AWYEBlDOGJXuWuAwPPIjBr7Yia6XH_r3DwAqNb7TiDEXGeE5GR5iF03T54rmKGFiWIyuFHdzWm9LW_X29VQwpu7s7pvBMEAjphxA0lESqgBJgehaJunE05jn7NVUqtSyo49LlJh5rt0mUOU_dvoqjrgfsvz0WDkbektUCZoyg9B2DCLf8jStW9vjxxDjF6aaTifFkAmyoCWVPbcIb8s16Lae1MFYtQSK5Do8siCDn-cXSVqQZ0fXiuVTMYsQPtx_EWYJ7siSz82tgk-HNNoHF0Yj7mnQPlnYz37e0lFkFjmvMg_0WPve1gl4_Rhm7Y2AGHKNMCg-0EQqa_UXLvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzXeJ-9rCSrL7z4ZdVt6LB-BA53X794s_ewHz3aaJKeyfxxPgFCuQohYLWvneYqESh8i3jyIjUvhUkm9jUDyImR3K2cVnfDLQkpcLkTT2voqDpbrU38jMLXZ4hRKdbglVV7kUKR3QXJhi3u_KFeaf9Dia-ZsPZ6Fci57B5aq_wzuTJhTOETowkOuN_gV1LtDQpT_4xYXVV47BU4qwwHMx2DX3jeKwfLBROjxdmf1O2CZgfRqVexM-7gmDNWZ8nALBMbZ20K22gjYRRLLseCZjrI8BOnWfIyO1AEtyEghErWLOn9A3XBx6tkRsoz2Uz-_d3Q_H48jYjSwB-EumPVWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbQk5LT_Vm1PDloWr4VG6mIgjtfDKJqThU6EfjBhD-fiD2cTocOySre38uR88mRnZxuoujfcX5ytYlhvrlnRz7m4OjVCLa8LwIb3MFJwi4a7ChibgS97wRVncedXcqaYUUJ3BY3NFpYYyXKOtUeuWg7BeKz_c-uWb84eRf3eDW8Z1SsXLXylYDyTfY0lM4mPCYrke9iy61578lBqTbAvQEC4zLGjkrHzx1qX-TCTRv5nsN7YStEcZ2klUIRkZ0CLxf9C4rgjqo32iV8aeo0duSesq0gZzFRyCS_QMtNohvQx9XCFGxtnSYWPnYtVpAPiauYlLvdf3fd8efh20MihtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLWYFaT6kQIp5zg8ir30MvLh4AQb1VcGzeY6OCkgXNIQA7gu3l8132V_GwLjUfz13dW5ehKcxWA0PV0dQyhU_nvOi0-qv7Xv4n2VITzFg6YKYwBsnelpgvfSlRbeUuNgXr9tcC1Y63AI52NwCLN3VU2WuzOM5TYP1EEL3cDUQi7pjBsp0sVlUHQpP-9BlfjXxPHbYsaouS134RQdaz02yT5cTqg-JFCxTmDEQr54konRLGqvbFIpApoFq69xx8vadoYift48cG6TxZQ_Lu0tif-XCi6diXHpmEXV3uKPscLxT_-ION3qe3tSX6RPI32pwCvSKFsD7Bc_QhwX1NYRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqRnWVIR-sjUTnjraZ4SWGLMjt1wkxut47csv2p083HFPWAzgz9epuXj2qojytgRUAhKLcV0jgkRb1Dpt-I-NU_D7BMcDaP3Zj-1t9gCVhy8crSB5Xz8qISXKWQb28zSYr9mNkJBgJuQNVzMBe1dhLGHiACixhdkrNLxFQDVX8dvXXaTmfChMEWEt-Wref1WH8Sz_a-GoTzqRFigSYTmcL_cIRTZrPN2dmPbvMy61Uh8GLYeKBYzBPBt_ZSblMOmT4Nb1vDAfed8VMCt4Gzl3mbpWP3iDZxlJU_V0o5EKuPzaVjsznVq9_y2M-F89q9Mz1vX_eXFTqLNFzZs4Y7RgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiH7LpdBS41l0rbDncuvrRICaTQp_ZWaN71XNSxSiOkHplSSa-qHneJwxaT9BrWtKDxVeDqRK7-rLg1NLxv3Q6UUjkRJBwD6GjsNtuHyfhqKF8rNDl5YoGxgBxKRGKAFyXU9X_5T8NhlwhbED5MjaDL2MQFCeKHSJdU52Uc6kA-PFmhb9LYVz8VpEqYddUArVlE5SoKl73r9E-Ax1LDlyaVdP0A8hOdpfpkGVKVC6dyVazWqVyJ-P9vpmKiaKaxI1Wyb38rvbv24E2BdWi9QQfr7YL7zQxKlSsGroKHPvbKzhKqUlTBhyNeK-u7GEW8ZM-tVhLOQLrUx6Qol0nV53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=rzg3b-wOYELRaZ3YADtsBsy3RfU4JYsVDNQCNImbfT5wAMmMXya07x6uJPPEsDKu_NpF7vlFgLUtzDfgNUyYqHS_6d9_nTOw25MXaYEqfde-4_hlCkrmAad4QbiuuYgTKSE19oKmgC0_jcQAix0MxV90QNlyLeG_KJ4d7iRFISeZQwfP8cl17AUdx8ogODUt99rVPOTea1osjk4gbLNlDIMkEso0G2FzJBZ00d_0xqAcsmJwrD3cHyvYvSosU_Agspgh0i5Yq23Seig0cVKNf-E3wv25zzistT0MlX4Xvn7L-LGCNtKl46aJ4W2JQEC9yHKVZn-FU4HYuoNZB3pIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=rzg3b-wOYELRaZ3YADtsBsy3RfU4JYsVDNQCNImbfT5wAMmMXya07x6uJPPEsDKu_NpF7vlFgLUtzDfgNUyYqHS_6d9_nTOw25MXaYEqfde-4_hlCkrmAad4QbiuuYgTKSE19oKmgC0_jcQAix0MxV90QNlyLeG_KJ4d7iRFISeZQwfP8cl17AUdx8ogODUt99rVPOTea1osjk4gbLNlDIMkEso0G2FzJBZ00d_0xqAcsmJwrD3cHyvYvSosU_Agspgh0i5Yq23Seig0cVKNf-E3wv25zzistT0MlX4Xvn7L-LGCNtKl46aJ4W2JQEC9yHKVZn-FU4HYuoNZB3pIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXDHMfKGDOL2rmctqamwfSk9fkGCQ4OA7HT6LxkHOpk8I9UgX-uzlPVzRSkYFEqJP5bKhGiWY84GFP4RDGdqECCf3oicKuiWGxepVsu0dSdivVFTPAfMbxByQs7cS6Pnf1YGsUDMSkOHanJVSOqEa9mgQ5lAWnQEBCmki7UwRRsMiBoFpaP6LxrzUq9V-RwgiN98MLyeMTLRC_TP_-obearoIfUafa4c4SJjVPxYkWBQaGyAGVBoqpdlgc8ryUwcNqXBfRRCRVfi0t8Z8KkjahbhuJkS73xyTGm44Nl6_d9jP9BYrMoVClS1WMczWwW8bl_XlPpbXt_RSVZCJxy6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=UNZdgcBozVo5ATrn2V9My_6OQS1zIwgoeNc4f6cFDU5kvIbOITZSY0E6ffYNnAL3QIQEPgTCXn5S10CqyjBNM6g8uFSreT2frWumN_fM23mtvqJ-c6CGSsSl-qPE6ssQB8f3SP6WSuAQZmsH1fnEISX5KS6IGohqecq7IOU5VZVSJF7eN3gROi5uvMjgJSD6Mp_9AWDMLP8rN2hhtfceoYoCjgwc0vpsywhyjp5mUKXGraQQm3GXjlmom-N87ujYfu3WWwYrTxDANN7VqlC-KucX8fZTiQkgN7OYpnfM9e3q3aPJ8KrpYFzt5DCLIBdANSn-XBsFxkyM5nESvq9N6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=UNZdgcBozVo5ATrn2V9My_6OQS1zIwgoeNc4f6cFDU5kvIbOITZSY0E6ffYNnAL3QIQEPgTCXn5S10CqyjBNM6g8uFSreT2frWumN_fM23mtvqJ-c6CGSsSl-qPE6ssQB8f3SP6WSuAQZmsH1fnEISX5KS6IGohqecq7IOU5VZVSJF7eN3gROi5uvMjgJSD6Mp_9AWDMLP8rN2hhtfceoYoCjgwc0vpsywhyjp5mUKXGraQQm3GXjlmom-N87ujYfu3WWwYrTxDANN7VqlC-KucX8fZTiQkgN7OYpnfM9e3q3aPJ8KrpYFzt5DCLIBdANSn-XBsFxkyM5nESvq9N6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9vfZhaW5AbD54c1Aa2eeE8Zj1VU4mjzHQSuF8dmj29ygPsCisqtjAJT7C4OnzDLVcqD0jTQ7XkCRXEzxPcL9SUpFBcy_NJmLmUCjWloIUM5RV0VS9zfCNmPzVwdVIuro5JEAJPvli06APgeL6ZiDWa2g16vuwJOSuYVZXDk1PY2WI_05qySnrvv0ZtSrZw-JPcw2-k8ogpkQ_0q-Ae9daKEaA9cAxw16ZaXZaCJeQsMfBJxfF2PWykTt-fFnlbd2ybWEO8T0cGLjrhCdO01LBD0i4PTPuf7rrUfYp1lU84bXTPRrMb1kIcoo7sa1ul0v2_P5yzG84663zXL2xjZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukj3TnIeP8-lmcVh-BJ0Ij71xTAlRW3KT1Vzi_N3bKoFlBlg6nWRnt1EhNt2cL67GkIg8U63mjLRt0_-X4qqfGLpzeCw-1Nj2awLWJEiASYpHwjLSWyjXAx6PpH_WshyjnSlkl3fXuAkLvcjE1iVLklq6An2oXjTfzpItD7LQnqCLLyy9EBaBcWG1e-9cHouNxV99LXOkSF44pDDHLSPmC9_nRccqwBOPUPsJGqnCTYzXqNtQeBy7GNGBOrMcTVEPJWGMsk5JIdSPpNVt4Z1RLkdcJ005i9NdhpItzIPIcxN9eFSW_G17aiV2ta6CBMKoBLhuzZDySggTmFzsp8rsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG8tKzRqU1wMYFoanlehXKejPnrPZZJU06MTyGABr4UzrLGCi2ehXGX9pxvi6jof9kk8HIW4p3nebWtCI9uv1rlTnM1JktgJ-ZBnWIMiBjxTj2xF0nobQ3nbFeJtKQUW5A_UklofkHmditcTFrOM4IRycVg7cE02Jway-Yyk0pMte71YsFrOaijiDcmiIM86N5sTwLxWglPnGcQkFE9XwV5G4koYMTgT9Hh9JnyA7ZIbF6yJIpTMgNIspabktfw4Dcm5IzzYEnF2ab9cwHOOnqORjDpRrrZRCGi2YLK4MQbi5Au4_mcuJ5Q3xMuQQU_Coz-ARpV-tAEGkMQ195welQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SROPGX9yqKMKUFfiJa8nY13SFPwAtfdLlPiXC63An8qFF0vxiqiPISHhS-I7xWpavdD8k5ibsVMfBUgeXVL57Hf0Mux5Fn2CGqcbR2QcbnoDyl-W2iZWwUqokjRwPE8-jOhBTNZ5XyUlRA2_kR46oDwCMxHTKN1jFuJ6gVEA_H5RURVLiVhvp83mmySOUEsJCEStqEobS9BqRs4wOtxqh5ffPDB-7-5MxxRQPtbp0RlD_BlqTOd9dhwFw5Dt-hhAUy4NSwaAu_qJQdIEdkKOpIMx7LDEwohqI60Kas-0gBy9KgqaW0KyJJPKpNW1QGgzIDbNVzyoevND54G5_IqxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHEkkRRb-BOrXRhQoUByouWZjco2Xy6zmzftZ5qNkVlV1wot3--rUPL0po9w2MvorNqQ7l6RLsMTxTUBRSb3vha_-C5MATxIEysUAaO1XJ8KKfV7bf41VWx_FZPerjqU-EIxoglwVyTxMByjKRTqBgewz-_Bjc9_e1V6HiV0Vo1xQZhWswq0HxoVbbwpvkVSXRTalwtRsydl3LWYf_QChe9m3tkAOGcRDuN8_2a4TbNaA6ofAgv0zEa4sWWvyo-YNwko72kTpXj07nbq4IzBh2otk79LgJ8Lk0W9pK2aguB06AN2kJT03uJhXpFlx4NRRIIqDWfxFnpzUdvTwzm3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=BaUvictwWg-sSuOphOsXpEYBtj8MqFGKxhVSEbPt_zSD666ZxuntobMDUGgpQBcD4xwZSEjkxlJoY3WS0siJq84NMnuGEDvbynrW0FZE1dx5umOr-hsFGBwehhR-kpHnFSrpmIOhzg_-EexsXQexJE5B320_xn6mgvgtKtLmyGMmYr6_OR8y56dMaEJ454WHvi9121wXu3pAOZYkDrP7NRBw3OLpgxDwjPf4UI4F_6_CMOJbPCU3ZZGv8qmvuI7n1Uzyi_WQBYD0CA-xK34KWk9UMeBibL5osyGSpMnTvm-X-eeooxQDbXlGE1C7jifhVdg_9r7GvJJGSmeIU8owmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=BaUvictwWg-sSuOphOsXpEYBtj8MqFGKxhVSEbPt_zSD666ZxuntobMDUGgpQBcD4xwZSEjkxlJoY3WS0siJq84NMnuGEDvbynrW0FZE1dx5umOr-hsFGBwehhR-kpHnFSrpmIOhzg_-EexsXQexJE5B320_xn6mgvgtKtLmyGMmYr6_OR8y56dMaEJ454WHvi9121wXu3pAOZYkDrP7NRBw3OLpgxDwjPf4UI4F_6_CMOJbPCU3ZZGv8qmvuI7n1Uzyi_WQBYD0CA-xK34KWk9UMeBibL5osyGSpMnTvm-X-eeooxQDbXlGE1C7jifhVdg_9r7GvJJGSmeIU8owmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=GUa5wmBhv93k03JuB2mh1_3kINfSiUt3sKLTB5eFjbU-GUQXDC0KkbE1IMq6gzMnwTbre-NZo4l74OsHI5gQcc9so3kBKcT62Fi0jfWnggbr2T0vvqbRHnv-HCQoX5cwPBSSDN2nSEsrYhVyF8HXCOWbmzfH-sniI_rMxdMb2YL6TP8PzSqMGrayHornvRaOI_eTXog1HltzatPsbrYJPAzdqytOAEkmBgyG0LhX65hg4OeeUANu-_wn1OLkVgWJCck0bP7g0EsGTHDc2BkcqC3mTx0RSHLlPP31FsXsNSXOu3zZoWYR1PttNcilJuxaDpyiWzvIQLQIprx3L7PnP3OwqPciAd5aygifGxWFIELEcchoRwIMWuI2haFQPa0g0izHH-zvyC4GOI_Gy_2dZ_tFDgosASDl4dGqedZzadHUnZdoQxqqvEm94tx6mIFJF4ds92TMXloN4JkoFl9kshsenrW43vOplNJTDBvWi_tYqYP7JWTz12UQ6orABMp6A6e9YSK_ShKlwGygmtprAmQo93tFapF7JpPf_1GUtOxpgsJB4bigUqhrnnUT8RjqSvK2PbMWooB25w91Ca00-OaYWkP2QV_daaj5YWTfjIwKT77TVUax6gHoFP5b_JjC4cSaRlMAb850-ywv0neyoBnU3ejXYxSvHOgypDdUIjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=GUa5wmBhv93k03JuB2mh1_3kINfSiUt3sKLTB5eFjbU-GUQXDC0KkbE1IMq6gzMnwTbre-NZo4l74OsHI5gQcc9so3kBKcT62Fi0jfWnggbr2T0vvqbRHnv-HCQoX5cwPBSSDN2nSEsrYhVyF8HXCOWbmzfH-sniI_rMxdMb2YL6TP8PzSqMGrayHornvRaOI_eTXog1HltzatPsbrYJPAzdqytOAEkmBgyG0LhX65hg4OeeUANu-_wn1OLkVgWJCck0bP7g0EsGTHDc2BkcqC3mTx0RSHLlPP31FsXsNSXOu3zZoWYR1PttNcilJuxaDpyiWzvIQLQIprx3L7PnP3OwqPciAd5aygifGxWFIELEcchoRwIMWuI2haFQPa0g0izHH-zvyC4GOI_Gy_2dZ_tFDgosASDl4dGqedZzadHUnZdoQxqqvEm94tx6mIFJF4ds92TMXloN4JkoFl9kshsenrW43vOplNJTDBvWi_tYqYP7JWTz12UQ6orABMp6A6e9YSK_ShKlwGygmtprAmQo93tFapF7JpPf_1GUtOxpgsJB4bigUqhrnnUT8RjqSvK2PbMWooB25w91Ca00-OaYWkP2QV_daaj5YWTfjIwKT77TVUax6gHoFP5b_JjC4cSaRlMAb850-ywv0neyoBnU3ejXYxSvHOgypDdUIjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVvo88DWZG5oEhOd0GxUAkUfA5vZl0M6nWeuLLFqmyCzYSbUFt_Z59VfaEauL9i90pVL3RvS3zBd5imMgyRfuSGYxt8dUGYpAWS0__yZvB4oPebx-RR7iv4UemSxTgwZ6HaU59ad87ntocW2h9M7KZ6na6HFZYmIR_XUJadYSH1FYK7SAX3i-WXU7BmoK3NyAcdYOcPmJgPS7GdF8RdJnNua0i4S2Fzn725mhRAqsxl1kzzwDCBiCZqMpOkYgZ370v1y3vptz6my1sj-kWMrogqGp9iYsZhUVJ_2aPxIGVPP2CrRVN0Cm3ePM9x1-YJF8qao7HSx2Pr_iy_G5ptwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=d8H2d5MgR0zSj7sdjoVzdFMwHvaY5SEZ9QqcQPmM8v3CJdr1_exzuWn0L1UztHNpJO7VUmQ1F_TFWhWuQPs_GzZ0avizHX-wjVFDU3WDfmk3LUqJVBK2dmAFnb0cSMHbIfByUqAnRyZMz0u6D8z7zl85MqjE9LWPaNGQLkN8aZHjwVH2BI75NSyhM5XEnCf18cG6nyCs40jFkNO--9w4iJFN3dyLuT2aYEr1yu2b9RIMAnay32nJ4Mu9kYaxyblRuoNdOZCalGryLM3eWx4X20XxonLBOcm-jFoNW3SOXhyNEp23w-2M313md_0pGAPBU0ASpquewr-Yp9DOR6cBzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=d8H2d5MgR0zSj7sdjoVzdFMwHvaY5SEZ9QqcQPmM8v3CJdr1_exzuWn0L1UztHNpJO7VUmQ1F_TFWhWuQPs_GzZ0avizHX-wjVFDU3WDfmk3LUqJVBK2dmAFnb0cSMHbIfByUqAnRyZMz0u6D8z7zl85MqjE9LWPaNGQLkN8aZHjwVH2BI75NSyhM5XEnCf18cG6nyCs40jFkNO--9w4iJFN3dyLuT2aYEr1yu2b9RIMAnay32nJ4Mu9kYaxyblRuoNdOZCalGryLM3eWx4X20XxonLBOcm-jFoNW3SOXhyNEp23w-2M313md_0pGAPBU0ASpquewr-Yp9DOR6cBzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=bfPL4lat12ezO5Zben62iqsCYqLUnNKVqp1ah-VF85GoCWMyijKBzvLq1ZEvsBSh-xk-InuSQx5L2rMVrlO3PrkXL4em1FmUR50qraFnYOm59P85Dyh_uPUqttexomfIlMvdwJ4INIpnxkLQenaE-maUxfZkjBCaVyu-qh8FxVwpQwt2EGTbGSlw2fWEwK06zaMqeiO89thJjXlkj-w6gZXmKWcy26YBUvZ-_1GvZ8gGyKCq8IgxWjtjzP0sF02zw1TH7M396KALMF91MrdG-Hp9Rr4nKiRr6-iRuvO7o9sMLBlb1-toMjGWTB-Hr_0g9eVCMKLZYUafNNXj-rViZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=bfPL4lat12ezO5Zben62iqsCYqLUnNKVqp1ah-VF85GoCWMyijKBzvLq1ZEvsBSh-xk-InuSQx5L2rMVrlO3PrkXL4em1FmUR50qraFnYOm59P85Dyh_uPUqttexomfIlMvdwJ4INIpnxkLQenaE-maUxfZkjBCaVyu-qh8FxVwpQwt2EGTbGSlw2fWEwK06zaMqeiO89thJjXlkj-w6gZXmKWcy26YBUvZ-_1GvZ8gGyKCq8IgxWjtjzP0sF02zw1TH7M396KALMF91MrdG-Hp9Rr4nKiRr6-iRuvO7o9sMLBlb1-toMjGWTB-Hr_0g9eVCMKLZYUafNNXj-rViZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=md66zZU_1htLBw1KfrqFzcZY0q8VGRyReD-Ujq_s6YDRH2-dSrKYJZhS-JJ4N0Sgk6sM3mgPS2wDo9yeo-OAntE74ug11FL3nOrg1tqw5DlKWOaN3kUwNZFC5qsAcdgj3Wi58u0urVuwdOK_RSW2g1qdi2g8nPlAwVkUPk3dyTGl7QhkquRcQJAm2zGc9K2_CJrByisTCUnInhOdHOmx7vvYafe5gk8ZH8f6IeXi9w-mYyqK3HUnj1OHqVnlH0mUxQvhDvFgzJqW_JgrdOBCxroROs5noMx4YD0g70VDssbBdYU8iFuyAti_2NDibz3ikqFIvuWC9h72otlldvtYAp-U07i3WrOTf9hfQj5is1G4zfXtnFoCcKXPyrU0mKg1N8k8kO1wXTib4mVSu73TUWyyPvTkk0jw3FgnfD_7P0J_wShHpIQnAJzKZ1R8FS9zCEVVgDbTTZvV_XVWH_-C6hXs2h_reoC4EWg7rjlfqPXoXTgKKx7jxUyL3jQ-4nhrjVEj3TEfS8DuAaIkWdaUD6012lPyYjYWLpcmdh1LeMAK5f7-MUPWaELUhkbO_6RvBW93mofUwg1snSiUSp0-czJx5X_dKGBNCuGmZyIEqOuZvJ64bJ2iBnd4adXS8_0tWuNU_hpm84FnSmqL7KyIjO6Ju8p1sIdX4tojtac9QnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=md66zZU_1htLBw1KfrqFzcZY0q8VGRyReD-Ujq_s6YDRH2-dSrKYJZhS-JJ4N0Sgk6sM3mgPS2wDo9yeo-OAntE74ug11FL3nOrg1tqw5DlKWOaN3kUwNZFC5qsAcdgj3Wi58u0urVuwdOK_RSW2g1qdi2g8nPlAwVkUPk3dyTGl7QhkquRcQJAm2zGc9K2_CJrByisTCUnInhOdHOmx7vvYafe5gk8ZH8f6IeXi9w-mYyqK3HUnj1OHqVnlH0mUxQvhDvFgzJqW_JgrdOBCxroROs5noMx4YD0g70VDssbBdYU8iFuyAti_2NDibz3ikqFIvuWC9h72otlldvtYAp-U07i3WrOTf9hfQj5is1G4zfXtnFoCcKXPyrU0mKg1N8k8kO1wXTib4mVSu73TUWyyPvTkk0jw3FgnfD_7P0J_wShHpIQnAJzKZ1R8FS9zCEVVgDbTTZvV_XVWH_-C6hXs2h_reoC4EWg7rjlfqPXoXTgKKx7jxUyL3jQ-4nhrjVEj3TEfS8DuAaIkWdaUD6012lPyYjYWLpcmdh1LeMAK5f7-MUPWaELUhkbO_6RvBW93mofUwg1snSiUSp0-czJx5X_dKGBNCuGmZyIEqOuZvJ64bJ2iBnd4adXS8_0tWuNU_hpm84FnSmqL7KyIjO6Ju8p1sIdX4tojtac9QnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2dfGo6YD20R2oeM0d66MoQZEL9lLsXCJ5TYyGhwtJ5it11MUWscFD_y0gQ3l8ZRHQ-tuB0uAaX3IY43j5VOqXSuMxF0iiZRIjvPQkQOBFrE-shnjms7w3iiVukGBmME1jRu1iSyQm8PEXEc30tijGM__l4D31Rjy8h6rDRqr1YhbHvqGPE4aRT-zUsdGLo6yw9issI9AP4zfywFV2nFIMQL8gCegHK8EUd4sz9Z9Y6OV-sQ_iA-TABRGIAzs_BBVrmIec0hteUHIn-QCPlJW8ExpzH3L3BjZbkIcYHFiEGO1r1_s3SKhT51dWHFHcAGX6gzpFRHfHl2NhLSGau6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=H1M3lHwMYkZlE2EJ9elsRFi88yc-VF__DAFeG1nsqkTWPmEho2RFoKrcOVn_vyCA3NC4g98nCDRS4nCvz8FgiG-4MGBNMTzH_xlVTRCVBylSBNSW5aw_IwrqMHqALjibdc2fzg8wJpXK3hieEEmvaL5uEjmS63I5ftK5pLQEN27MK90M88ZfCED2p35nvmBNRu-Ys0sQXFvz6XzpJyJT9Q-O4P4EJlHAa_4K1BRZ_F74ZFqi1fhxVD4MfGpCkCbMLFxOcxVPj_drsXQlW-dJAEEwD67ithHREikZzA85JnonGBuYhvM4dLMqQ020awXeK7dedcBhf0OQ4REzkeWFjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=H1M3lHwMYkZlE2EJ9elsRFi88yc-VF__DAFeG1nsqkTWPmEho2RFoKrcOVn_vyCA3NC4g98nCDRS4nCvz8FgiG-4MGBNMTzH_xlVTRCVBylSBNSW5aw_IwrqMHqALjibdc2fzg8wJpXK3hieEEmvaL5uEjmS63I5ftK5pLQEN27MK90M88ZfCED2p35nvmBNRu-Ys0sQXFvz6XzpJyJT9Q-O4P4EJlHAa_4K1BRZ_F74ZFqi1fhxVD4MfGpCkCbMLFxOcxVPj_drsXQlW-dJAEEwD67ithHREikZzA85JnonGBuYhvM4dLMqQ020awXeK7dedcBhf0OQ4REzkeWFjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=FRLzQuo8BzzX__cYLzyMaotKtPPVRwMiCwPoPrHU3_NWFXiU59tE7a0E5COt52RXDQa9y4-6FswcnPKvf1OS3TdhJfylRxyqW1USn_qOUnIDcZgbVR63vTU6zIKEVzsO6cjnPfQSdZMN-VaDoech_EsqgCQTviyMEapaptaC8Ozt-x-nbvj59EVC4Vo_LF7NSfYo2QkhWbJxQaDxe5hmZqiPIptCyVnFgiMIs1J0Xb7oZv5t369pb0OdG03lqpZIYyHOqgSovLzpJ0543-AM_Z7Uf6ybXiQZ_9gZktul2Gw1Dp6VW2ldcN9dBb5wqjJjPTny4vqI3bvRTIKcGULm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=FRLzQuo8BzzX__cYLzyMaotKtPPVRwMiCwPoPrHU3_NWFXiU59tE7a0E5COt52RXDQa9y4-6FswcnPKvf1OS3TdhJfylRxyqW1USn_qOUnIDcZgbVR63vTU6zIKEVzsO6cjnPfQSdZMN-VaDoech_EsqgCQTviyMEapaptaC8Ozt-x-nbvj59EVC4Vo_LF7NSfYo2QkhWbJxQaDxe5hmZqiPIptCyVnFgiMIs1J0Xb7oZv5t369pb0OdG03lqpZIYyHOqgSovLzpJ0543-AM_Z7Uf6ybXiQZ_9gZktul2Gw1Dp6VW2ldcN9dBb5wqjJjPTny4vqI3bvRTIKcGULm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T47k_WXCYlAy88qR9fgvD4QYQTm52EuA-bX0SKLXTJjaBLBNY5bjfkCjtH_6i2Si3_pUI-eA_FLSpPWA7PyEx6i0MuHqhPjk0L8cP-hs37RKCIWSvAYvtLTBh8VS0sNLbb43Da8BHZbO4GzhcIfzNalBZYDiL53mTDKbh4lWAux87czSW8ls1QYBiImf-RjdDE7JRRRkvBy5cD01kiBhsIWqWAWzEzUk1WjjjrpDXYfMo4J530mdz5mZiPhDMXdBvLfC0gIYMuggTnagrqXp53wyjxuauyh5IGJoK6CePFXvPHeYqagy4lLRqolnKoLXpULE118w8zp8EwZTMsLLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGgoeelbLyooaFDsap7QKUhdkLMsQDF022SfvwZ81Dth9r9eJkAzSqNFhXMcNpQQ59OIrDnwiH-InsLdUb2e3Avy-J2I7jKMZgQPPSmzppfF1CzhUwn9xQLRr5aWGj4apGpTYd1Lq4fG5GmMAVndL3zMOLU40vNJx1tmMSt3lieGPIy3XNvS_Cz4cHpJ3hh7hbHJxxV7-Y613gQhiyUJMYPGOb5ayA58r2gnj1fRx8JxwXGAfp-IMXVV0lUE64-j44GMV-H82hK0TXFmwfDYsEwd_W31X4lYPd_xhD728xQc9VkAUYRQz01SN7gp8rdqPObMfx7RPv1iZ3PUZC1yhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0qFZLSkCCbnrwbICtGQn60Iel1nmTWspavxxc_1_WDZqiGVrzZK20jRMxTDOe-L0k19gYvmXQBHNrZ2V3LZrRG6wf9qJngK84z_nwvxmuWEexyqpxTX3KnZpzUEapKTWPMlWB7RZSeW-y-dSSmX2GOI6zQ_m2NHkAqSOSBk5UumQ8y5SpvrQkJ66tboVotr9xNroMwoW_SuCHY4w6P5RHNQYbOQOcTOnGzk2IGfmY8GGHgbQtzppbXcn0_MiwKMnaU4NQxRTeKFs-rwYrSRLc1JLVQTJM_-hyuep19t4RqTXsiiqOnYYjccdvZ1YGpp5mZuGr_SApc7pgvin9mlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH7gSPJ28vOKtUEBbgAFS11dfH6b-dcyi31EkQZMVPxBTqzLAN3ErXF87N30Nq4MaL-rmTfXPk21E-sv9llXHpViPI6kBVDWMpkf5oYqGzw4_GR5myLbSocLaLDeFUYQmwLT5lPkkqQI1EPuZoY8kiOoDEBpLnNFl0RZ2FPwJw9Wej-YDLkUMfJCLm2KB_gy7yqIiY5VpPpMVL-mFskEhdqMNyxeBfe1UT_VfBKxdZMvH9gT6d24FfGgRY-lSM7nGIqIeYcIu9gVUXTsQRQwmbXBYVTvQ0WXQTod1pfLfdy5HOlbhu5KkM3Kun9JUXyAcgyalyKh5e3FaxtuPBTJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnnV4pcqd3DzXq76t6ficYZqtvcFcc2zGFS-VHsVg99SqcyPFFgW7d8Rrrrf8PgFNuie728CODwKfrLC8ux8TH4AqX2TnIC57qnpeW7ZmuANetLcu9k5znv4xoijZB_7cIaxFtuV7biHi3i1i--EMocgpzwY6cVkiATxF0EB__187owofht7ezEma07C5YdImPnFYsi_CFDktl-ZvU0x2rDGhmzLAxgP5saQC0BrvXu9i6zAPsdlPunOqq6BOF1lxEqSI2w5xHyxNl7iyL58TiXiEGEa-wGLpdy0vWmmKaI6IGxJEu2WLdUgGG2vte5Iq39Qwzvp6i1gW1muSq7Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PksS-Urs0642UsIQcaeo5vkvSIatcCHxXlrrE-emLh3SxKPd0-7F7cgOrm2Bi73SswikTVRHvatOO8uDbfZr7c4oZ9FQM7geQzR1l6V6hJqgDlIxH050Gku3feOkRKb1PjHSho4OesQIrbaVkRNEYlqrQ7lkeGugw7N34jwihilQ-vsywk70yFSWU1u5jd9s3wXEg2GIavkObQpnn8ZmCxAckv6K4ZqzErLolJKFdHsHiTFSnLUc5ZFhcfOwsjpctao7nbq3zIRjjZ_nUtMVHYhY1iKwYdMUFyuWTKpicETojvihtAL8gUR8jRY-jHXcGZbdDJqKFoS2UXWrwgxgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=ntNcR2RlQYV8hhdsF7hZ27TULcU5wgRtAobqKp0YoFGBG97PSEpj6EfDqYUfJBTkLXpgn1LNhAAaW7FAXu-VylwSj_S8CfzeX5LsEAd0njv64FIWfDshmQgpamI7uCuO2DHslv7r64-LVK6AbvzGNl96ybAq_-QVr_UHBDAOsSPBIoKByiiJEVdhT-09-VV_vw8KIAwxpOb5ctxSASYn2ltjRw7cR_nC2EVRGQQOPwZpDl2b1RMQbjJ5vCZQRr5444gURdXbvymNgweTm3dwQmkqkA97x1jD1xDVXK4FVCEuwLzJBRRjvAvFRqqyrlN_JPwITienjnc86giVRiBXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=ntNcR2RlQYV8hhdsF7hZ27TULcU5wgRtAobqKp0YoFGBG97PSEpj6EfDqYUfJBTkLXpgn1LNhAAaW7FAXu-VylwSj_S8CfzeX5LsEAd0njv64FIWfDshmQgpamI7uCuO2DHslv7r64-LVK6AbvzGNl96ybAq_-QVr_UHBDAOsSPBIoKByiiJEVdhT-09-VV_vw8KIAwxpOb5ctxSASYn2ltjRw7cR_nC2EVRGQQOPwZpDl2b1RMQbjJ5vCZQRr5444gURdXbvymNgweTm3dwQmkqkA97x1jD1xDVXK4FVCEuwLzJBRRjvAvFRqqyrlN_JPwITienjnc86giVRiBXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRc9c3jNTjyjSbdiJzBO3pvLrI_3ZX_IUIM6xHVQ9gSovFA-nX4bcRyJyijNbLlWOSpS4ryQkuokn7WAfL19pwzc2Uf5ZWlwfK-DFsfl3Vs0mdL461QpgY0jS2Z3GN-VxXvnSd0S0va7Pham6CBfCdvSSlq_Qivpl5tWoOGNiq_UoIU8b-RoiPmFFdE-CBYoEw6SJWH8EvMU-K3joRzdijlJHy5ksm8B85EPrd44oOHF5TmmEJVRphjAt6unPw9T2cC9XYc2OC4ir-Wmrz-JGXX3nyKXOMxIVYWYRggVskIN4gTnCC5Z0Hzsh1ro-I3GZ7f3UbgOdiBLBOV77AG_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-Z3IB8efL3KrAfh6EcU2A4gciknCVqEfhvnHG2OR_I217UQ3xvWo7LkQh7ltKKRibF2ZzqTjvAOU0e2FwFLZCuyKhCzlu7x0KqyGXlPp9KIR21YQCKqTwsFD7Lx1gVED1ZloPGrBxDNwDJK8taqh5inPmt2WBRqYDaPqtxsSi0UdcuRetYMaWwo8R1Ilte-HDlSS7FjCdcP2qSoUZ4RcP8e3mi5wnta3pau_N9UnD8jRDwzSEd39jGkfyZm0s0-u4RGM-tEKANRpKr8nkOeNRtlCoJkoW3PvjAEhhlL2wIsk5V-2hoAmcR67FD1YvbKZf-RvPbT4eVR64AjtXiPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBaownIkpsMyKs428o7bfNyyVeTO3JW6LaYxEwLlLVxBO7vyT2xW-H_94R_iNEM8-7N6hteKksewicd5E7lq8hODYXcDaN3_6vgYAYvJyDjaaUae2VyAE9_Mmam8ab5FsI8IsfV1cHO8jNnA_28lEBgaKXhpohZJ_iYufKVs9ixT9b1rdYAOVLEfywQde5TDtmESjw5X_RQc1u09hEJtyrfI80I4HIq4xDqARa897i_e5PWY_cOWx556sx45cYdunLjI-snKS7HSTADvGHJLO4DDmZC4h4EsLVw9d3jonH5_7etDk7MDD1IuUTDd8tY3thzFiqmw6X4uHO03XUvZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsP4JAl94tfTT0veerT2WltgoFpv-cVA_-K5ooje-xgNs7U4H3RKWRS3Lkf7QjYOqFyuypf4bI1pih5yFK0vNztUvKLs6iUd4hQsc2HjWlR9odUYc8N64EJDA09fJkkXydAiKjG_NQvbcaHVRgHbCNNHFN89xNc5Y8Gpoc7b6O_-817ynM5MOTdOCH4148RODZiSkAUmcYnZeGqb-glUug2L_l9fdKhRzOuxCDIdaMEcibNkcd5BHwBYoQUPdommsIpmcHrVYqr8aoYdR8Nb6q-0HQgIs0A2EWlpvbwPEPcy1XfUH8zRZ7pzcAeUmz8-JE4Sm4MmJ3bbZArjFzi16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPZgp8Vfbn_rKsWVNL6wttx7DHCbO3WMTa90_sKzuijgJmSpO8PkRW4jVsei84lv2yZw-YHZoB7yckB1TmJbatxEXf1FsEm9W_9vA0ATN-zh5bhpJuzqrEP6Z7qAf-m500x-LoAQVLwOqKtO-NdSPKFtbwk8_Trsqe06eBnXOBF0p_m47tAui3eLhcFTxZWW7ZIB-aYZbwh_mYZZV1jawJUYTeZWF17WsaRZoXuIKsPHFW-jbwq4WlI2oumlpj_FND9zfoFUg5rHotlIGEpCGSGEFFkUeTs0gG1Z1jmwzxEXX-6jM73AdnocXqokkHM7DQUD4VFRqbeT55hk_ezIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQJEGq78cJs1FRL6rkonkSbzxDLm5bC7p6bnogLn_NrlvXmqSXL-RpaPzVbzsI_XYLmPKXcXr-X7Hp93xVJIkAoc9ElAfGd789JqU_p52JGe3PP9ZbdccRVNpW6oEPc3bT04-lALg7D51g5RscBKCaWmw7JGAocLiEZmLYMgZfrj1k8vh3UXZ8OC6wkZb73wL2YAaHbPogunWUoprh6MtTPyB-F8IB-RHGXCX_oxJAxGg63EJhOOmRcj88ZNQfBK1FMwouc4x2b1eHqB45_7glo2i0RRQ0DKxAljS-lscp7h91x9L9MvYeZwYeL2ri0R2gQ5BQ--ejzalq6_Pw66Wlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=SE7_Cnkl7giMZ4PiQ8JQZnqpL1M8OK_ZMcPl7ut4O2_0vcfPzjg73ICN5CkFLN7WF4Cpqkb6-o-r7fQkz7wmZlPErVs7y9YlyENWh3_70oemKdlOJuLnaZ9bZOFSi91QFFiEFhjo3V6DK0jM_3noOfZKvr6S6nDH94nSZWS0WGUh2hT0uGDsUwaXhVWvbRE6eo_I_nu75se3s5IZ51ktkjuIcdO-OPa6Py_jD3vNi76S3XhYrFQP_CY3DE-P1xpzyXw6FPr8MdWdPHVO5XlbwpzswNCWzefyCKGCDJFiiYU4wCdTBHKgzOlJc09pNaC0stQJuFRb20XK_zxol95DcQJEGq78cJs1FRL6rkonkSbzxDLm5bC7p6bnogLn_NrlvXmqSXL-RpaPzVbzsI_XYLmPKXcXr-X7Hp93xVJIkAoc9ElAfGd789JqU_p52JGe3PP9ZbdccRVNpW6oEPc3bT04-lALg7D51g5RscBKCaWmw7JGAocLiEZmLYMgZfrj1k8vh3UXZ8OC6wkZb73wL2YAaHbPogunWUoprh6MtTPyB-F8IB-RHGXCX_oxJAxGg63EJhOOmRcj88ZNQfBK1FMwouc4x2b1eHqB45_7glo2i0RRQ0DKxAljS-lscp7h91x9L9MvYeZwYeL2ri0R2gQ5BQ--ejzalq6_Pw66Wlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcSUhZQ_88SrtyL638Q48jV82634wdXZeE0ccLtlB6ZuAaMDz0qSOFnVwmhBY3bZ3_HFHUkg0oIm6KwhIl40PrwUU2Xl9PZi295clgeTvWs114PIx06lqTju0YbnM8uQK4q8ImN26nV-WAdrYA3_A96C0Huu_2qYXuXFsVm4E2-PmMpnzWPjODy6ZbjbrRKxKKcUpXa6bPWvl-i_cwV1b6oj4qZPK94xoskeKCk36Nldi-gvJVkOHBssx6iplz4az0mF_VMT1Jt0n97AnnHUF2dkgVC5UYadzA6ZCUvkQeyoDSRknVAAb1jaspSU0Gh2x4I2MwnG7J0IJ-_4FkRj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq0NxrUADgMiBDYfcLhyKIg3_azFArIaSeKnb-r72MOoZdvctdhqqOjZDP3ReZDQtVifCx55aOz7gscGovnjaGpM3yj4rGticknPOmbXp2VUnLAiEmahlPDJh63MffRkyAuHTfe88OsKFwbnBxTV-XBbGLSzr2Sy2Zs3hg6jnI30Z1gUvPqv8oOdEauO7lz_Tjm7wKnqwe2uWNwqDFTA4uBGrFIBzSMP8DTSXHpT2s22HkFxe3rYFZKEXBPRROdIx5F-LskBEJebI0TPkQuaageSd3qTjbd7YWuLVI5qzuSHQPMapwRtHC6BV23c3zAeyCcu6E8HYDZWEX7kde8dsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=GrIWeKBSDNh7sQftT9svyecMm95LmjdX-nLaaIeaez1vB_de-T1oOP42GroAzcjJGmiKvyqHMf05Zvwjh4MrwFJLwEsFLleT7HaNOZXYXK8nmJfXXqIxzOHlE0yw8dn0skRumwXtLcKTuUlDzQfbBQjdW_CQEhZtbQkV8DL9mlt1a3S08foctr4ruUhaQcHQcsHW0-PV7OdwUOh5hujrg7OVC8tsuiyQCUdGn31gi3fNWb01jA0dzg2c7cgZB-IL_cNgngKkELqFXIVTPghLlSnE-4S1pT24j-FQMTqUhzQTT0Nk1_3qj2kS7BSjR-zTljjFJK1zYCScR--fwfLA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=GrIWeKBSDNh7sQftT9svyecMm95LmjdX-nLaaIeaez1vB_de-T1oOP42GroAzcjJGmiKvyqHMf05Zvwjh4MrwFJLwEsFLleT7HaNOZXYXK8nmJfXXqIxzOHlE0yw8dn0skRumwXtLcKTuUlDzQfbBQjdW_CQEhZtbQkV8DL9mlt1a3S08foctr4ruUhaQcHQcsHW0-PV7OdwUOh5hujrg7OVC8tsuiyQCUdGn31gi3fNWb01jA0dzg2c7cgZB-IL_cNgngKkELqFXIVTPghLlSnE-4S1pT24j-FQMTqUhzQTT0Nk1_3qj2kS7BSjR-zTljjFJK1zYCScR--fwfLA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_V2t3k5mBpOplfbN9mqgaTl_GqgVBo0iouDJAmsxeflqH-onBlHEQASKDvza3BBVCZ070sxNApexhy-ZyDipRHyEUZnVRYfqn1IzKJj-mNHBhF4pATZKNvMNWi5ByU_ljOqtuih8V-edzaawdP_b9Bo229S-F9TVqAcLGVYOzqOgXa7XY_2EsXL5CQ3o4o76bNml4chgzh6WwIlsE5qBZG_7_kDkVHIRNBIUQbNg8sC_0uVFNDHPBad1WHUOjV0X-9WZjeLBBUp2owhi3DE2k3wSiOn4w2Gxn6TGtqCoAOrtS7FBbxi8U66SOgjlPWHiPOKsvldUjEvkgjZoQM3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=ZVDPfkQCg4COMXtxTbZyg4CPPwzRja8RL5meHJNZ5OPr4lMLQFRtGUhxG4lmmop7SUzonjM2wRG21wlNXPWf9BJbDcHEtOxzBNpPPGbgk9dluSoZDbwXw0ae29B7urQxc58pAKf8QJQLCB4J-YaRW16sWEUh_nBCLpe6QkPJXwUzz2JU2THXkCZtNEo-LQcMNd7BpgY228RlaXhzgqom0a_GsrIefFuv3gSHUkgTX3s_yErmzIT778fDGmOGNrGCVN2WCZ90ARHUJWPIjShlktwzRFYAyH-c_D2SOEffXrlXNj1a2muTwbSQ07Bvc864xkwOmh_e3NELGeZPAFvfykPjjlH_mOacBGKwC-v-0TyocPXRMZCQA3JIWPFes2Rtvt8QwadMwHwFWBUzItdthOYf6udlKTKQVJIU02TzT0ckhtJJlmwm7LgaBe7Q6qEpdVETYkpp874m20VwWxQPT8lR4z5b_UnRfqokoGCKAwHeilmco4q8bpKNo_3WhBYmq6jDaunhSU1iFMidkCa8RXcJ1Hl9UR5A0vplyOzT7MwOezzI1NJZvBIlXdHEvEUzlPrq4SqkbJgstcgSPWUehv9Cl8XaeiZMIhWrZtUTLhSLJQJbZk4ORDUy0aPQ02xq_LpX3HJfN4FHdRA3m83ALjfo8IYxee2oiQwyy-gEl_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=ZVDPfkQCg4COMXtxTbZyg4CPPwzRja8RL5meHJNZ5OPr4lMLQFRtGUhxG4lmmop7SUzonjM2wRG21wlNXPWf9BJbDcHEtOxzBNpPPGbgk9dluSoZDbwXw0ae29B7urQxc58pAKf8QJQLCB4J-YaRW16sWEUh_nBCLpe6QkPJXwUzz2JU2THXkCZtNEo-LQcMNd7BpgY228RlaXhzgqom0a_GsrIefFuv3gSHUkgTX3s_yErmzIT778fDGmOGNrGCVN2WCZ90ARHUJWPIjShlktwzRFYAyH-c_D2SOEffXrlXNj1a2muTwbSQ07Bvc864xkwOmh_e3NELGeZPAFvfykPjjlH_mOacBGKwC-v-0TyocPXRMZCQA3JIWPFes2Rtvt8QwadMwHwFWBUzItdthOYf6udlKTKQVJIU02TzT0ckhtJJlmwm7LgaBe7Q6qEpdVETYkpp874m20VwWxQPT8lR4z5b_UnRfqokoGCKAwHeilmco4q8bpKNo_3WhBYmq6jDaunhSU1iFMidkCa8RXcJ1Hl9UR5A0vplyOzT7MwOezzI1NJZvBIlXdHEvEUzlPrq4SqkbJgstcgSPWUehv9Cl8XaeiZMIhWrZtUTLhSLJQJbZk4ORDUy0aPQ02xq_LpX3HJfN4FHdRA3m83ALjfo8IYxee2oiQwyy-gEl_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfO35-QDGxBNrF3ZMg1Z6H4N5PaCDSCYOGC0d0DO6uDTIvoSS0OFnfvLsw96yOoMEyDwZRbICplJAuGXEDCgOMl0wNsHMwvpsJmznofRs59jHeOWEd0hzOY08jRO9mztLsy6zbrP8ubUZXYEDI5gVVT052wX9T2UBJstNn4PvLQ3hIeFWFOVqXRBAwdbJMu59ElJiIly-C6R7Lq_PvQPIzgZd468V5GS9vBjMOqxjOvIN6dzNV9P1SWAg0uTJzaLXVM7JLc15S1uEMSoygo44p8Em6yIac3rmwVOV0TbG_aYpBu5gqmJXfxc7o39OmgNvdAAugXpykEz2hzQdJfMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVB-hpcghCnMe83x9DPsi-e5yX27nJ98nBwT7r2jN9dnLHN6wJMMVqD2y9HkaPd1onrESVFKRFQi9kwubQnurlOi3Jc7fhZDhPmgprnzFGWStW2dP31BiwgdP3yrIPgeaw_yoiOTVBmVNw4vFeTmvlpfP33sirmysoTU6YiEAJM4ePw-jn_rRWLrYIexIhIAdT2sSnMVo3vSjBnOaGSkawzTe2vgeqEStUae_gtTCS8zpPFM_q_cvfo7-uvl7_BEkmor4oLrQGFOW53-aD24aD7mzMUP4aD1xEboGpYLlXGC5XgQDpbE-OG8xiYT-LtiMlak8k5F6GBH9pqZTkNEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DljLtCQIeslmnF5e3jhlo1Cgr1jx1m2hk-JBb2DhpJdRpJ6XxjFovJD1P7i8CRSc98dBivLpkRUEC6ZkZbmJBqs1dQR7bodpIWasM2gk9r69BqEQv0JdR8HtR7eeViYJO-vLsv71eLlXDoRGjMW1_w76ZM1ck8PnXQ4Z4kv1xDquKRBRoUwoviKHk4emK888wvR3gHYt8JcsL8FKp2DpICQM_vvaXIUfNSPeQJ0YBljMUGcGvRkYeCLRX5sHKUuDLPRzkJ2kvU6jztW957MHaekpKD59xnhouLTPviGzEiTswbxLcqt-CkOYpAVJzXGR-mBImvjOFy6jaUzcEcLxyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=ZkhxWUsCV2vaypGwSR7knqyn6aK07mfog9cISPRFDxQAwVmiSyPYsQQJWGglfXLhzGLthGpzR6ufh8HdRA8A_Ca0kN6ZOe7HdK3aTqoB7agNnZK4f--ZoMVGs8xeguoxKByiMfjflSFU4bel6cc_e_91ilyACtozUdLuiGLWE54CEBuNd3V7KfSUmue-Qg_I5ORnl63o2Bn90jt1nP3ny62SfUU57_BL7rDgwgSA2DMgOibAhJIksC_rh32HL43BXPZAzgoboadscezybqtjHaViiNMqsfEPUHp7IOCYUO6tCnpM-2NhQyWr5CGyO-cVfjOeOVvWc5do4L9P4dXM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=ZkhxWUsCV2vaypGwSR7knqyn6aK07mfog9cISPRFDxQAwVmiSyPYsQQJWGglfXLhzGLthGpzR6ufh8HdRA8A_Ca0kN6ZOe7HdK3aTqoB7agNnZK4f--ZoMVGs8xeguoxKByiMfjflSFU4bel6cc_e_91ilyACtozUdLuiGLWE54CEBuNd3V7KfSUmue-Qg_I5ORnl63o2Bn90jt1nP3ny62SfUU57_BL7rDgwgSA2DMgOibAhJIksC_rh32HL43BXPZAzgoboadscezybqtjHaViiNMqsfEPUHp7IOCYUO6tCnpM-2NhQyWr5CGyO-cVfjOeOVvWc5do4L9P4dXM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvam35VyNqHfg61dbKOjXdx0VGW_dGHO-4JjYXvcUvEPN9SKAQERsh8_jibi0twdeyUMS5hqKtkEWkWw9LQ41-Or44XR05rcLn0hPZ-7TKdmK55d8aYIEV0gnshqUzQAhlLs-jrHbZoumoW9xduK8wjyzbISjRAuPHPtU_MNkPlNjtMfo91RXpbxzN6C3963Sz05uFFiZu9KOrxl_EFI5MyPv_-k1MWBMrC0SZMa4mB_THLHEhVq1vJ3rVxSDWCIlsu9SqHFvovdBqOEmBkrdMLCJYW2XH2NIC8mzjSmCkM0gKH7_Ogo_UsKu3d_-e0iZ9bdtjic4t-tt6cEzPsp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcp1TiSp8HjK0tjPLIFV7P1ZN7djxBKC1T7HOwBtsWwZBo1OWImpvNc-wTPcQo9yMgJHnwO6jV08gFXtPyn3SidhV85LxV-aHwraiNsd3KSBsJqY5Hx1POAY3UB91ouJz7_qzh77p8TulquhWozBjMqQ2ZcE044ly8YgKXt2R17UOAjgXw6YrY1QM2uhKpSha_H1e7aZbK7ZskJe6uiJEYGKE5O65emk3F399Mwr9VC_Z3_Rz2B13Q91cS7UsT2o4QrT2XOMi0gPJF2UMMkSRdeQJ81_oA27TDvT9gvIS_Th__kYuFlqNoiRU_daDxpKZXhw9itIkdsKBH0WQbZNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_uJJTdxXwVWmPbo8RLuerokGWa6qg0LlKudl3C78UXf9M6OZiOc5CFP7VQkvMGvPj9-7Zo6DqK8pl9dnXDBj7UijS1yoChsaiK8dcTjMwnaOO7UujEjXbqWHk-Huf9l_Dz9yeZTvylxL2MSWRvk2pkOUXsOzv9BljZsNfy1YVXfbGKV12zbVTGqfCTexpjFOzud_ASnuuKIWZJMzqbiWay1LfTXUtKqtr_CoOqrAUTY2d5zIwxY6sY4VpPIDU3lZXj_-ZVBmVmQ23SqA6LiiVHNfLmgPuhDSHzWjhjFw6KArm8Mf8rsyi6OdsFFyp3rnH1N_8QbTAd3F14Jc3ebrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=raF1awjReDznFVt5GSEd60bzeiKnbACpE6qoNFQ5kSYe99qm2fgZWNWaJ9CRGwzbXGcJYHXhkaq8MlctFPjgxB366OgRqIV6cfAtRrUWMLWJZJuMhms1m0A3773VDWGvkGc10HsgoHiC_KOj4HQe3QJ15UP6QPf4__b5ZMsfBnPnrxLSpcTc_u5rj3T3n-vZmbBY6InE-rCiH7_HVYrjxiRwwMobLwHouXcAwdZw-eTZzfRnPLU1JlWC_1CupEF7sZqugZ3lvmwDMP5noIYH9PiCjUKtVBAwh_9ZzpmemFlMOVvbILJgy472acQAEVFH5dZRCsoeO_53FqL7-BfMww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=raF1awjReDznFVt5GSEd60bzeiKnbACpE6qoNFQ5kSYe99qm2fgZWNWaJ9CRGwzbXGcJYHXhkaq8MlctFPjgxB366OgRqIV6cfAtRrUWMLWJZJuMhms1m0A3773VDWGvkGc10HsgoHiC_KOj4HQe3QJ15UP6QPf4__b5ZMsfBnPnrxLSpcTc_u5rj3T3n-vZmbBY6InE-rCiH7_HVYrjxiRwwMobLwHouXcAwdZw-eTZzfRnPLU1JlWC_1CupEF7sZqugZ3lvmwDMP5noIYH9PiCjUKtVBAwh_9ZzpmemFlMOVvbILJgy472acQAEVFH5dZRCsoeO_53FqL7-BfMww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl3Et1cdiNSHkUZvwtzl7CzKj4W4GDZC00eBxkNrMBU4_mCvVsCGsw_sJ2hYIFhD_kRCSRIw3ZrHDx9uezlAB3vmT1cOa7GcE4ZP3yRiZSYlHUSHbKpjGnkQP9DxsWIfMdzlhxJH4B3V-gwPBHdJ5r94tT-y78VTBlCKzyAkiwAo1hSruigtHbTxGnvoW1W4_vqEdiF4rmJtRAZUWXdaKcS6g2obPMI0WCuC2fQiEyBo-5FASbt2bul93W21-kZSgFqnjOlcgWB4s8nNyrW6Lz1LrPGcOnfIdKz1U-XXtWok9VwzStu5rLK40ybSd0xOV3ZBPbeJwb0ImVog_VfQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYnd1Jskj2IvB-uk-78Y_RWMqw_IMyRpGopuo4ThBzIgfiUspiw8F0piuHK6qiiyBV5I4rO1ng1exFSbb6HcKAj8uA4qa2b3UCxgkfnavVCTiilhJGoTI0CoA6feZXHV7tq7wHhLoLdJBAH4bWWLZt-SJeDqmA7nRYrkspe7gmt2dPviaplI3Zyhk1da0WO3BgnW_6eawlzhgPqVowxPp4yySgEMoWWmhMoIw8IVs2_0id6oj2TYGzoqe9WvxAEgtCUUYdj_ITxysg5HSBD1gBB0JQyRi7TTsSXzPQYZIOrskeo2GwAqwymdZumMSonMS1r2dva6mkMDrqmOu-hrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
