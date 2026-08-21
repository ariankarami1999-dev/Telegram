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
<img src="https://cdn4.telesco.pe/file/FOd6Ks00NBy4K-RoR05pw_-KjXS_qHoaW6tCPfyZZgj79BTPDXI1-92q0mjO3S8fS4D1I2EZNOuCVtKRmvzIihhJ4QfozNN5uD6DfP0myxSE49Tt1TbL7JTs2t7m0hNnLnkrhRSWQ0oi42s_RH6FqZVGKEgTeD1MRC9pR8_GevxBq7T-AlAwtJNIMpDUznSi4AIsPjUTvgQV5-fS469_OW-twZHUwhA-dvAjZYON9alTD3OvdIOeOa83C2k1K3RSoTdttz_pdpfFby5R84z655fOmPIXR_X_TBL7okCsceFBZ4_2PLRNX5dz4xtOc__I6z3c6Mu1_Po2-TSIPpiloA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 15:58:15</div>
<hr>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moWg_UMfYn_-p3qEgdHOKFb1FpzLlZXnLKG9GV-qNGUeAAlctAjKtPzrZnJexLjb9IZXF43Spj21oMD82vRhIuG8npvZkuFeMruMdtYZJjcUihc304b-WmcGUb4PEjzhhKu5StX9HRcbdsoGsJpeTk3ON0O4neh5I3HNNsAxd3wg7jxOkKGI6rAhbs-ZTLVZXbCHxqahKCGEd8SMUuKp2XQCPhTPprkgNm79LofgisCFMB2xjZ1KtUz3lfkO2dmeqDiAk4Srb8kLE_zXHiI84T_9vtGyLmVyMRQIf44lOrkqeaD-2-ndMMA50QQOBNrir8D_C2RKGP4V0z0qPChrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1tNOZB6c-MoQ3XQMu7mUtgF-BQk8BMsZvsHZp8EYCDv_zpKIBZeahvjQdEf4RgZ7zIoEWNj6nP_D0RHGtp-tLA8u8D9Gf_tAf-LuisnUl33KjquBkubl4EAybwzC7_v1V7ZDU3sp2DkwBmL7BWsm6XZzbeGe5Uy_cRNia0ZJjQspMSAE-y9Ed5NMYNYgxoWd4sVy2HvYEOLEfidb2RzHubd1Ck58F7e7MZWMXLx5Vo7qkqzwYwcuH7OAz66P371ddS8pQihuvL2xWKQTXIG7eOpEPEvPM3TWGQLxLLxc4R9w6GsON6xoFqJ5H-Gz0dtblGYamEKuPrYk1X_EoLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZRyw0iU2VFhAMFp2m_a_3-SSRdkA5AV6S9loQG-kbaiVi-QUqeNWTNoKr-73zhFnVkbPziBP0BhMVM2vKCDW3mQCrQXqTfmpsLgGbwe6SasjzfbJnHeTs-Js-HabNbNdtPkgmCTWxVUnheyTDAwU1bCKHsYKQRN4sOmc4-zk1gb7-CtNb6emhLO56nMPzyzTFR8K_Hwz0gqed5RLJq6-x1-WHzgk_f6aIZtAJgHTWqIkeUZdzFGywjdZnx_LiPulKoWNujHM_5uk1BiS_UbA_D_4_8mxtipg82w8KcpIN3Y0ywAF7IML_SX3GItVibRpNLxwyUimP2udxbgv4xtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0ohILSPW2O_SOe1NkBErJEIPThX09VhvtcXHmXbCIBFRzoYpIjdImQ1uTAjvO9VGOg88kDcNbPLnbBPqh-SQ7riC_M4ARMNoK0fuv5gJQx5aQvZV_l1XkN2PdLiO4zpHitRdGMAfGr8LREZK3DwBWODCcSQyyQ2a89QYJ4eubPDvX0XbAyxgGM0A8DNWB135UGxS006tUwSCkH_OtWNiaNxWS4W1tDykwgZPVd-FteeFIE3KfNfo0eXn3hhU5wRq7iVxl6PdsJf3X4C_bJoH4bQr9DAtMB0hGtSZq4nGZq4f2E4TTkVQOwGS7KQiLm-8rIoM2LkEx5D9asQsI8YXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHtpWwHZyVHW2lU_mwtMNMYpcAet42p9zbh5LNkNfcjgWxC4vuS_54RU8irkW9Oa5Gk9FZ4h5VG3F25VZlzKjD3sp_l1rWoXJ9ky3blOz4bCoA7L8NM6Y-nM5NKU-2Fbo3eRWedEPylIlLj_lgLFewsArzbHKA0vO24smst1YYsFpB5mCjBXS9ClE4lKV3hw_mi79NMAkATsZBPs0UsPYOveq2P7s1d8iM97tuA2anMEW-cuLT63IMWZEBNWes76gnL1xGhlaPzTlsjGHIJYPX0CzZD5tfCqkfXZlT_x8lE00bvHJrwJRMK_14CGx3xmMAAfB2YTpAj-ealFvQoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVwOmj27ZXolV-KHP8L2D4Pahm8zRA8AB_-G7fikzdtlJ7jhbtBuL0WDe8xxF9RswR2T8tnFWJtpwq4V9gw0yGV5nVDoZyXWDE20mX8jiFYr__iFZTTmctUqMzSajNX6q-Is9lJBXHyUz2Ias9_0N8TAFw4pevRzXDELdoz8xuFJJrS77hH-zV8fz5P_UHwOMBGHMAbrFj3qIiUKL4ZSPQ64mLEVPhA0s5dlfjp5bsSH-_3dmo0OK2faekZvbmUsmxy2vmGRUfY6HJG4rP3CbgnCCVj_47CYxM69BBGiUqCJcr4OvzlWcxy2VYmq-PUiTVV2DjqYUk05tcQLaP-t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXgeorvbzMcJVImjKjaXB4uyk8ECq1GLm0ESAwB7LuzMk3LJXY05dPU-OXiby5kfCsh7j9COMIN8FqpVelK7qo_WOPggrSXcXzxW-UMYJfPPVBKXscU6dnPRf63EyiHT3wu3ifboNGs1k1l21EISablwR3E0E2ZTr6Tm8E8UESl_kxPEL6aMmxkIeNhnGogBP7SRiIfSo22hkQrhW4EYis-3VOmnxnFccAI-4UHbhAqQR4_kSOo9wCIEZuo0R2Phfe1OLhtMqah4Ka1BGe5w156bhwyvAeOdlRorQPjsnh0Sfy1tFMIIMu2KSAPljQSuXLyrxBooJUs6ZtOVbFWf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUV8tqbpjf6Ou4EqcITPPxoKhXfyNVkUmYpYakIc84YZ71_PiayVL0U5cjsfXsxo_T6oyC6q_1eu08QjJIT61m7MSZ3sDfsK41efZt_UCRonz24JbnixXDOpTP08GxP72_YHxnLeswNfJs9vh-s5IuP0LCsG4O8NdYuUpjfk45zk_2A_AZuGrKcbTRmiHT_AjmUpi8tJpvo7_ia1fRhFRMF4rDcgLK45tHfjW3lZXHpqY2NDlDGe0tPiy4qqr4Lh6G0poiPK7rgOetRCkdR5iRmpm0nCJuvCpLB-OJ-M1yzbOX9SpIdTVA3znQ8aldrrNFyBnXCtzO-PgvaSHW6-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEDCjD4Kupo-S6dTI9EDlV6idagOB1B8cq0VulXNIIe86ZVKLFJYjMz2FXtFpO9D6fG7nZVN2YBpdXDgExWYqaq8WXyBtRjH4LdovqDH9lYVKp-CKuJX-7_9NzrGdWgUx5skiLD5Fftv0RKCiGor7MOuONEHbbcUe5BBk72TyEEpnoIcq07i9kdwEAr0o6TntSFrc3AwXirQQgO7WMu5MHuewvNqyybkPhUdPhzcQQQ_usyX-Vu8wjtovHXQjgkZLktQpBBkZaALI8VZJTaGHrMlyaGE3k-TXVQ0Efd_7YiBd_Mnif_a--UrRCLp-ZPH5obkh0HOFCz6X-KW2tbwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcdF61RsgxMpZ3GbUYWqGRdS3ba-YOuvEI3siEBOjzpUBPWBTbovoJ8H8OAlqXeuye7hL2JRqdWVINqpLzhG7MhE8YflOf-8OB1rpHwlullwPs3hnW3VT-D7VCH7EGZXpAV8rRU68r8p6VTRSKteoC2-0HP6Ya7gvyt5G3zZqSF3mmmBySKLgIT5cXlZWFtb08l3qoy8u8QHEv1jTLASDsGFQdcn06zRNgthoSNYEReEkEIWYhiJI7833YyUnGE8OfH_kAvrOlyK9xhdRPmU7CLOFEvu2cclqKlgtUXMQwuAHDat5ywruqwBilmPouRXKh3QvHOeIGKiDcJlq7pMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljGh5mN-R3-vTA0KuuW_BT7tWAQRwNPi3EaAdffQqOkKvwAzYLwMsThJwZLZp4-GyqzNqKQfftsZT-wnXefjcEvvp4HbOeBH04EF85V7qYNLKtXNgacDPx3XlpWOGmTmDaE9m-kpALEL4IFxcobrHv3gnOi4DGYSZqClWfaP1jrBMtcHw-FO-6FkdwWXrUlJ8_bFT6igsCN6eoogZucOo0e778lxEuPAR5qeMQEbOd9_uZg4tvvy30L2I4PZ_qLEcju5xSeEFsO979MKMkUSiNk4_mxi7a-JEkW48FD4Nxgph93JT4C3jyl7bi7EwaMSfRyfpx9PVDNeKM2ELpH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAlXwum122IIjgsVqKb9bPea1uSnkODhVOKxtFT5xk0AlnGf-Zy8D6P7Yu75TFAwnvIuwgzoyo2X7uJRc-wlzMWPLYvXMDyz99XzpRQKl7TVnQAXJ47rL6KqwzXp8BfUsYdMYPp_MiBM94WOUzDwI2UtmtmxQ8JRGDcwaplPn4foIU9INBoQ0jHQW2h91k_NazmckaMoP3R6IkY8_m_wqJRqwf9HQooY96T-7IVgMwcj_HpiiXu6rxvlWX7lOabnnmE_t9gKHvpYqZLf1z7HsF8cwibx7TdRDs4YOtWbdMd6x9Qj5hN4gt7ZtfsSfDXcDPDuJXjx0IF7M75VZhPLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5SwFPkD62G1BqX80w0yxGr4Xn6Igf3xU85zMSC-psBCmFCw0e4Nls0zeGRyn6WFEUNl8NBnio75MkQH_4ZYzC85sYTFr5gmtSudASJYk508qk12eD0TQkVhavn79E5t8jK4-x4xOupoF6JS9EqCOUd04cuKPkXkdh3dnDab-7SwR1su2HdoDo-zixP6tmQJ0KH64DKbX_Gkws8VeXdG9COQIca2TV_hh9n7S8bF9xARH7K71dPjXtdua5KGAO3ZuxB_7Dx4x7O-rEMM9kRgUUMo8NTINqD7DqzNC1AcZ0Dgbkp3d4HKnE-EGNSWtxHiFPJj1iS1SLZ0PCPjw8Hn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3sVcriqOuZfabeG_IQiXFMW4mrXXTOCpI3XlWbvclzPJ6zfPgmD286WDijhldMKGsygzfYz09QhfW7BJuvASUOoA_PNcWRjaM9TeZeZtBegxxCRXjMpwhu7_SYYv9An43lXumNiognDZQmYpw5I0oI1I2rwrSPBPzkQxLZheKRUZPGnlxr7UtBW4T3FHq3Lg2DqZ8VHK4qUSNC-wwRV9d-L8HSlEZFI0ISnrUlh5Pq0Gfh0DQZjPsUWIVCuAtl2ti3yRYx7Pu24YUN5Mm6obS_tRyXvwXyFjGpO3YaY5GDE2M5M0hk8dKrFzdHbVZAGn7xGfVwJ9EbZ1hRnZa8qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW6my_cp7Rxy9PDQMmz2LMl_FJEt1iAEvv5jyok3YFmSohY8zfCrgxdHRuZqN-OYu35hONRD4fUy3bDXE7tiIpbeLWVwhNiR-yIaOFqaaCuVdScGna0vv0SaEAJA0vryeB3-aPiYl17wyp61x25-Ua56j4QhfcXC8dBUyjki1ZebdHqfzb0H17sp0al36kzpTbtf5aQZhXx5rVzv3VXZ1C6QjznXhtejN4I4Gl9ttVR8cpIVW66i-FV_QMYwnannMMcnkeNdsZtmM18Y-ag5g9u5w18T6TZJ2T8sEylNeLrOfkACgjBAr5sOpKrg458WIWIQVslPwnxLo7AxWl_-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5-SdCeCDaPg0kroiH7J1iGfOVuLC5DlLoOv1qVsSXZb9wvaHDInozYQpEc29gmixf7QGA3L3nmhxsIs6cxF2DRnmQs3OCtiN3Jyy-IPIdBpzs7szXK3ZZTUdjfkf1GUoZdXGfL-mDC1eqqMGaZiNlflSLuQBz7W2VWr0osSacQp0LgBJgPXRCUgmM7sffi1zd-dwWweM7gh-8BPgVoePTmFN28IX3C6y51pF28g33I9mUtYH1_w0dMARq4kXky5wXnHsJWlBliBWLe4_qyqpM0V4-vKC3Vd5CUGow75o49dWJ-DyTRQ-_ONtNUXTDS_1BS6XQiU2l5VaO7qSLBuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5dB9AkoScs3TBBlGrPQ_2DDHXBVwnqCPW0-YyQSzqGLWVTTq783sxmVq-_DpJENqVfoce7tlquwiTyStQcaWlGvFqPx0HgO2OPm8LTRJW9vjtgS0-rQ7lklOAR78SypVDaYz7wlSoLHdGK8MjxE6tZdeKFAxtEILCdmJYB8v_nSWiYy9BDfDyTb-0dv7Gi6_hS9ZnvW6Z0V5RXmx74NSLZnHbYjp1mpfiRZf_Immgu3xjaT78s4ZvEEaRDz_dTfWTfGOo0GdYLforZMx8clNUur_cjI-cU9jGUno2n8vw3Pd6qG7JEZdnKTaDsfPvRcw-r8eLTS8qql3FkkIKKycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4uxwxDn6usD6tP-7vc0kGOV-4lklFuIjxauLqPOTWPPN27ibSvJJjYrZ5WGJa9V1VzPi_buiTwtylVtGO9CgDj3jgDiW36cKOUW7R7KdWuQE0E9NQctj0Op8SCC8CHetO7pJ0OFZP45Bp4jHjVeCpnyZquXJXBcjKQgp3hbC2g2lWGamvwTtyDzBvuscHJiKaRj42C5fP_89LIZOMv0ZoTUwAeV4zwaFU_n74WyP02aPDOW8nyvJaaU76of1LDMNOuiIbiUHftWD5cjjitbyTsmEvOs1evxenSYMw6ApuG4ZVI1FCJ2gQ9nTtT9gJxnH51wNPTpVF_5yfmLTrSDcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV9BzkjaH2x4CbOwKVVJWmkAa8sQzSC1tfSHTtk9kXjmKaESlThfkgwCOwcXRa2P2ckR3gV3HZCk5a-w4GX8iVRqsQGBNJKuGIkfhlXyy4UqWAWD9JXgUnOwKt9yGxwuu6a0UdazncsebAIMxP1l7KFN2kdfo4_pc_Uow5kar5D1Brcw2cyLSEn40Dv6DIzbM0azmbuaucwpg8jqX4-aYXr5enjAPphEtb26IbE2o24RXR6ONhLpwfpDdNuhbl-ECP_o1FsH1PnZD100ooqBR5L7ege2PDr8irI2Qnw58VMdj-ZL9IVx9odiObo1OJ0dpAnWbQDfy_tucR1jIfsuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enzQtcWdjhl4rMaiRajVMUB2lL8D2xsgExiRzs0z8KiFEMUK4VvNgs-KoWzoNKZLRrAVWSWGXOtseOBJjXKc-OCZ6UO4xxrMH0JiV8adQHU9JCYWSFvTO1x4gV7inBD9FJbP2EY65thNwsTzlC3UAG5KMkH_GtScJtlA9FdRyfqE6oblZMkbhvOjA5rLFPtT_Xl1q8oHcML5HLiQlisn2J6tfnXiVPfy_i5lsIBxAuttC2QI1AnQNVQKh5sNMCUqPkavXHk_dynOXtBsXCeF2b2DFB-GdVLzL9mM4YWcgHMKJ5fb_vmHX2zuZwOFPpJYD3r9Tt30MBDieVIw0Ol-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoibvlWiKCoeXs7QniEppGn9LlY-P7uejoOus3ImB4PTLIhW6XdYjrPApptnXFuNd7kWatA0hG9zPRKEP4mPhMroRkn8gaP4Ls8lLClrp-p5Og1MuwxAwrI0XsV9pD5mbWDUTNIe_iLHVAQbxm-v2MNwh9XTcKDAk7kd21FcDD4yetJnMZmG7XfyNWV1LjeV3sslnnkH8C_qx7n75Z-V0SNPyabhIQjXJpylnrE0kOkJCegNULXe1Xm8AV4U2g4pRJQ44iSmNMz9MaBxB5yK2Zuytp59fIT-Njii2KC8vs7FWe3FOPe9kTXZPoPnILxAmyOo2GlhVi467aRj-h7DOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMyjRJvEH6XlOas_cRRwGpxaPa6LtqDBBiazwBoKdIZQ3MhDkTop3VcZe_RDS0WAEVQ4tbWlxn7nagPSRFWTNl53EpXKWtLiZ2NbPtTBISByB3O1gxXAuyTrIj0PUp80RRaMPojQf1GrjrsriEAYfHgGeYoR53ULbPePDPnUihzKtpo7zkbAEoxQVTEeOBk1KBJSpLXWkT7miafOm6tagQkcbvtlnFObW8BZeFnDYwjJDPEQHoysZPLvQWg9lrIawUH17beQ3KAqIZuh6_ml4-_I5f56_anTX-P_pRsjKATz32aDh4PrTgVe1sguqHH3jUkTh02gHg24ggZ318lnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0JgdENI6elMjow-YcdSwoILFGV1Gb_BjmH8DVkJ910QMsxQB9kSZS-LU-zysg1uEGf45znvEqaOSd6YZm3961935rFK8VyRMRNbug7oAnEmMAHGC2er3kbaT4CJ-tftbaWodiZrUfBk1y8pVdzl7lsTreCL33T7RmkWk7PFv_PAOd3s3GCIxEAxGMt40ASL3luXKD9es1WHoHHgbbr_VXUBGsDmeS5XGblPM3mu8oLPNns8h5PSwYjqEe5Bfw1vrJ9jIFWp0xHaN4gbPqCXVfH3fwiYQBGbSutaSe7jUDeNQqS1ZxZWzNjDvwMw4YKcfHJjdUQYtyX3DAf_PSk5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD8xGVWTH-EPLCKFrdIBQyDv9N69-2uTEdR57zhEQmZhGCJRlBmDIzSGt8HIZwtq7z-QMFv4VUt58e6PJjtdP15XZIx2V_rQ6ZBxHOxJ-BfcGVL3K3CsXP7ah5_ZG3AcN9WfBHRZLWMin1h2pDtE0x_SqeJjq2TJuu7RAcWjttcjGybRscgkHkRyztfcj00VCdh0QoCONfpC0-C1GvfByjDr83pKJckbltEHik03B7Kmzwle9SmqX7B4yDxTg7I38NbtPhHtTcOww74ZWQseu6VPRNMrfFF2kEZl2d1Jc4hs6xXTefBmZZIU_trIfiDGl7SkQ7q4SW-IWE6M5xNf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDmkewnzy5iw1sSTFPpPAekogAjmTjfdzNMcllqhEqy45X40jTNJFBlWWf1a33fsUb0Fdg9GgU558GhGY49qDlM7pitu9ut18HxYLJaa6nZQd9k3J0dh934bo1FB-nBHsapKTfsRr-agyfhpTHqs7OsdsJTBoUjhP6MSoBtyFGcJJAsTGZgD2GI2H-beQr5SmjjG11M_3Cxj2qGCsR1btKrEFUuSFSsiVD5OZ8A5LIsQsjpSeljU3PrJ6vfrwinh8V-F_qzhyk4ecfT9gNyuVsgqTjG7EhpdATnSSuFNQkxrIGnbRj9Gf2mx-ovzc0KGjGSh2eIegL1U17m9Jx66Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0N-YZtabmfyaodx3f9I0wk2_CX44fYiwH5TZ1e5mQVRaq3PlnPIhf8BFILJz_4S8j2X_kPNk8TWp9HaK4VDgDtAf8TgxQcz1UGb3x_XAdBHnldfikA9NfPlsrZHtGukI5nX5ZWGkPSaBB2Q4h_gMhFwOF3SJzOqtl37dAvbwIeWLMQBngaPvfFYQBbTVNePFN2BvOusjVbZG7StltNDZaVl9JVZp_3MXibuBYTAIehjlxIil2TiqK325jz5A10YneSaNS7UP2TX6_JOmyrWx7a3rPGPP-dilHcTUxwmn1tOfxIGMsdEOdr6uXkteyA7IVD1ZiTaRejMKvzKuKw7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BACgeb0wXi5sshQZGommFS_R2x63rTibEnlzf--MBJNFxnwdWQA7Yij65DInfSFgKnv4WzsCM2PGQK_lUItRSLzeRZXTnHuxx0nH9eND4O2SQWNZ0OiqkoDlr8bkaqrOSBg9gq6tk3XoUpsj9iJnWzfubnod3T9XGcZrpRDjpDAZj6wiWdRFv-EqyJ7jApo_Eo4BrVLMynU7VmXmYhknTxIzglA6l5KgqVjMbMZl8mFgRf4z_K3pCt_NxclGK5DtUpGlGwpqjf4d15I6dK3grG8kh6skZ7eESpwknyIDPQ9EGQMLlG5sV9c9IP9YP6VmPluELxKkYY4XzuxL8KkTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpFbsgb2eD5Aq_6uVaqTCD11URJtHlI_986ZbnPo2iNhttyfLkKppiitgItsJT_PmRXUVAwFVOZ1y6_qsgMs4FmXX9mg_uA-Wr-U4ZH55nGmUUE9xaMZuxKknkhamfdYpUTXk6kPIPEQ0e9GqiElaIchmsiv1LY-55fmhxPYka67yFRbXmMO0WOAFseMmybw1KR1e62Y8e3M-LboJU239PXz8q4OHSvgnuR5Ym8CgI7yHBAOb4Q3PTuEqeXDRUSE2TlkaV9jcGmOO-BJp5oyKHxQYctp4kafU12SaPPlysMCWFo5yHJ7aBuW1i4UXVSimVLu5neYhhjwb2hdwaaG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUQj7n89eaFEt-rSQYkEFb03_3ALZFKAzc87vA4Bw1THZZ0vYbeFC3MhhXJ9ShupJecraUVDTFj6R3nBHU7tyskH4GrolpEUfWoWwUTuFxxDHMRZ7WzdDbKutz_LFKF_ktciqCwXQZuAuXSe8bPBRAdzzLRJvTwq_rB6pjMkJkqUQRPOS_2iDLauxO1kubdXop9bo-3KD6YMmG0iCtJ7bBIvBIkYD2wt0ATaTTsJGM7N40goxQbPv2gt2ATyphvL53IK2TCefkpa6UIWdPlGwzzX5yYfGWHJg9KZnZfWO2dcG52l6LTDFlCdT79af6lnMTsnUhD3jXGNggXna3ip0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnkgUQcqQosqUDQnRxtagSXEUGRLVmJ2zfTAiJW9cp0eySaUx9O14Xb15LaT_sqC8qeGEirFcTyUkZnstlHGuCVfxcaTrlVhXj5ZjIrKasuyDmmDzNRrXk47EqwcjAmLbcytYmySbKb0Q7V_PDUyPpVVWzmujm6pzYett7yNQigNmwwT30xGBCJZlMZJzZHkE1U2NAerFM2YBASJ7QV5EQ7dNptPXvpAKOQhOAR7YZBf7vZeGlLTVl70Wxpzyf64QRSrQe7tZ-6QVS-kg1nnr4jpv4dWDmlHKs4nVOwT3M_s2CrOaEWiIpzageHAtHKQXi-GcxkYX-kVJmsONphdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0-QwXFMEQJriBWyIfP7xe3PZ897KP5AXdvNewTkqn6P4BF5brXyTDVxL_sT34sKUEauTKwXsex77RXLXXE4LclzK79_OeN1du0a5BhSZNeQY1-_NwNoAALPeI8XjPIeHDJ3joYuwDg3MpeL7hnsEXU6OVptdko09binjYOnJgKZfIEw3njDd9b-u5LoP0X8XsT3qobVp2Yu9gAgHa9u2tB4D8bb6HBPY76ACN3CY9EGepLrm0WG9BtLMg14BoPSm67LtodcmTZ3Xr_KG8kSJWrcFfef-mMyibe9bB4FZEz_QQsj0wmzChE-7rNH7B-AXVQLeJaxCYxzCBs2-koiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ0blVJYVxUOLzjVXGYH0s1OAf1V0PpM5ZGNwNxsPPkBkTNtcYUUWCXgv39I3MD5MibPhgTxQqlBCMGFi4jsZ8hNIhGjRKa7pRDQ-CM_TWbLMKYCDlB2yd4g70UhPvk4kxX8FKM8O5yhsB5M0kI6QMu03_4vj2ILbnqRiM-wLL_gUGHMCKRZARnMKgGVbQNkmoIptT6CHBp1kmVwIO4lWkkrvhJdNxmsOjRdb-xslqo8Z-6h4ES18pN1GUW5IeeGhr61HJGFb2Y3VZU6p_oSE5Pmk3LUnsbVgV-6kttCrWatqeINYSmWKne-GstE74ll-xVL94S-1ZdBRzdl6zG-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2UdgjuYHrU0sDWO2MbFaiyIYttNIwJDLfj_aMTTzXkGJ5MfKoez6Oe07Sf-GmTlwTpu0tXtqZDAIKE8lW6C9NHI3PuRcJmGSISC6GiAGhObnguJVVZcaX34xTQCzQGVUxK4WJRMSdnzvd9sF68Hii2Fj4TsgCg6iO8C2tRRTyKvY7t9HMScjeysZ8-RPVjM9hcoTWFf93coNCwlvssP3GZhhh1QTEDLgPgENztYIW_AT5VJ2j6iwGYQ6WEeYLojRBgavKEeg3Kh3JZFapq8MCnQXFHOclH1XXi_0dvxPlSJfHyacU95UoHgnBXFi6oAW4ua9bqLgoY-pPI8ij5rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDgTO9JLepja-vYozDrZqiEEWvfnrKvk1mIBndSuJMPzbCn3C5Q0mImtsFu0xPvzybON8gmF_PDfRu7E20IP7TQ0wo8EJr5mod_5mpYUAJ7MZc2-SCmRS2B_PfRCbQVl7KGxpNATE38UyGSFb8gTtaGchXyqhfhejYyfYAsFb88vpYnkzrjSUrNcVU-x0HdSHaqq73MKB7-FYhiNVl6slXpKQ-7Xz9V_LCXc6RSorQ2TQzHJzNkkZO6jglBV6f7wMPznGSkuaVbrVlUbJEOwKKZlNu64Ag4C4hrPMwcVCCDwIFf4fVOHZ-9uuWVd9DS8bV_uwiitcARxBB0oqkss5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PyieLqyQlvyKatpbhpdM4tPC2qSbxunOo9FxTg-89Sflp971D5BCBWWBTktOZs5G217olZASNUPYZrC-Ni3BrZO3FyyeJIYSHArk3phxzGbuseaM4IDhXfXS9xyZO3FjUr71cZzB5GotN6tG2KMQgvQxHl_3EknuY7eb3kUtUCXfVtceRADEBe961EBFNihRS4qVPfg4w9YZ6eEdt20NyHBUC3UJfK5rn-VMSElbhFiOlAIynMgqtNoCy-dz6UzoHtu-rSAdn7wLy42lRAA_VGIoWwN1ly2XE_hKLRmBowsIcqCJus0FDA2IQmBbDAs7o9xHqJLbOYgXNxB_boC4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PyieLqyQlvyKatpbhpdM4tPC2qSbxunOo9FxTg-89Sflp971D5BCBWWBTktOZs5G217olZASNUPYZrC-Ni3BrZO3FyyeJIYSHArk3phxzGbuseaM4IDhXfXS9xyZO3FjUr71cZzB5GotN6tG2KMQgvQxHl_3EknuY7eb3kUtUCXfVtceRADEBe961EBFNihRS4qVPfg4w9YZ6eEdt20NyHBUC3UJfK5rn-VMSElbhFiOlAIynMgqtNoCy-dz6UzoHtu-rSAdn7wLy42lRAA_VGIoWwN1ly2XE_hKLRmBowsIcqCJus0FDA2IQmBbDAs7o9xHqJLbOYgXNxB_boC4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdkDl0A5Ned6cnMkZ4KLJEYOzRoGB-I3FRAwgjaNrAFP2y1fhUXoOj_5ajOUQp1jWlSCNmgxTO4lqcvb2MW7Qel2pBc2SNqywXdGufbhuVIixUaQXAkDDV7GJa6uwkpYwmlWu7SA-66G-lSPJrvbHpc1aL5YFR2KVEtexy_l-weRdVMp-gKlM_MRsZs9vpHC43RQpVtKjI-Jzf_HSsf04PRWwkE1ZQTE6w6qb5lPPZFPEz2hL5gJSvhkKtidrfxpXK4DKHXYsnP7DHUyqCtE87YHZKOX0Dvy7CFztw8-6CKa2VWSCuLrgSGcNcVWYaSvOudu4c9sLgBO9oRKsqIgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cp3U6eSy5tzmjwigzAERODIDfAE9Gnqy6p3BcwA2hhX5DKGsg7dBtNzB5RE1jW-7OTzKQggPGaZkLObmbOJa_Ly-GR2KuK3z6YkmHeo5clSI7DzpdobV3C7ibJyrD07Mh9VJL6sYVnyJAej95vyBvjKOmo8SMwDKD40sZs54jBymL1EFm_eup9UUX4_4XkiTLUmMfjUWw4oLmWhftfmpTy5GQo7ig-aXIxmi5dAeczeHhjCm0w-YKosYJqQRS5G5zKoMqLk1BUs6du1c8N53O9mqI6hPf8ksXVWuWXUwTJffVekV41OGVAbc9ruOcDPZc3JXJTM94DKPEicduPfJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cp3U6eSy5tzmjwigzAERODIDfAE9Gnqy6p3BcwA2hhX5DKGsg7dBtNzB5RE1jW-7OTzKQggPGaZkLObmbOJa_Ly-GR2KuK3z6YkmHeo5clSI7DzpdobV3C7ibJyrD07Mh9VJL6sYVnyJAej95vyBvjKOmo8SMwDKD40sZs54jBymL1EFm_eup9UUX4_4XkiTLUmMfjUWw4oLmWhftfmpTy5GQo7ig-aXIxmi5dAeczeHhjCm0w-YKosYJqQRS5G5zKoMqLk1BUs6du1c8N53O9mqI6hPf8ksXVWuWXUwTJffVekV41OGVAbc9ruOcDPZc3JXJTM94DKPEicduPfJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxZ-gfcCgXSBddgVm8S156FoccjHQ0zrBi3R0p35Ntl_qSq1L13TepFfOOGPOWh0WkwKJkRjdII7XezJpcawvIsVxfDxdn2G2P5kEqegGzvQqbrbALQKT6Vm6aCq0-ZX53iZlAXT18Gvmxqb-EjPbPT4FgnGgiViMU6_pU3ijXHPXyvYQrw72oja3QAegIr1OGhPlVSTBZP2oZWylGFy3a8de8vLk-cu9XRN96F0YDm5QrUBO9LQeqn60mqSzWW5Ereq05m_QhUAPKxZurSQusmjtbCzgqsj7NVX2sKLOvoq8qWETkXahT2U36VykkQ3ssfi__O5TVDUpF0L49FNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmKhO06ip8h5eNsBhqCBvf9dI4FudMWMq526_gOw4BBy7Ej5at87wzc9vA0x2zCzIWHXON6yVNZcnc862wvuX8kW7lNTC_FtirQ_bcLN6LIkoqSO-iOKMUuDd5L0UCg2awO7N1lAWdkiVOti9yRXWPA-wTgRlyoFVsZ0Md0AVPszqYzf23qSQRaCqCBzXgFYBHdk0qhUAaAMr0elBJxyEiOHH-0OeBFJv7Dg37xBhaO_B7AMvGdu7CbEH5MDCYyVq4jCvP7C18YH32RjhkLge6bq-lfuCSfTJP9-OuL0ZbVw4C-wrKH_qaWQUaUVlqJa6GYyaNrPPsAOK6tmJLfAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=XANDlhyC7rsXdToTU6cGfdMKJ2fGjfmctZR_eWICVFHDz-jONTUphfz5ouQAkDAdyiJLCb4EjrMxwzKZ1eIv9vufd2Tr2ZlJMGY1YjypiKvtHyrn737Q3-pu5qAvQ_vaQxWGAUcSOQ2WuneOQuszu58E0yPV171asnDzcUVZIenw_i59F59yfqN6kU9vDNhmJxb-36OTuOEil-Zsa2QdxYM0Htuecrl3JXh6blqOQIgCtY-3TZTM00HkQ7mrI2Km7Y6KqDxy9CYVPZcKhtGu-MnePRZwXaICbo92Yr8AqRoBFmCXpr-1VOPzlMh6msEIhAt2dgVCBC6msc9YE_hy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=XANDlhyC7rsXdToTU6cGfdMKJ2fGjfmctZR_eWICVFHDz-jONTUphfz5ouQAkDAdyiJLCb4EjrMxwzKZ1eIv9vufd2Tr2ZlJMGY1YjypiKvtHyrn737Q3-pu5qAvQ_vaQxWGAUcSOQ2WuneOQuszu58E0yPV171asnDzcUVZIenw_i59F59yfqN6kU9vDNhmJxb-36OTuOEil-Zsa2QdxYM0Htuecrl3JXh6blqOQIgCtY-3TZTM00HkQ7mrI2Km7Y6KqDxy9CYVPZcKhtGu-MnePRZwXaICbo92Yr8AqRoBFmCXpr-1VOPzlMh6msEIhAt2dgVCBC6msc9YE_hy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKP5LRBktnqSntNKQS489foLyqDb5DeWzqLJ9AQuJ-p7Qhs0p45XWgsk1aHTBiBwgqe5M8np2BnSmUQNiuLuCQOmibmCc4NJT6KSoB_rg_URxfH1fsPz9zg_eT_YPN4Ejx_d9FcpiG4QLXYcMXuTRvU2W3muKPDUgXMochFDQd-sKYmhEszL0_77TCOZKUUD9GhYmlUfwzORbbpQpwPJ_HQ9rxbpkhz93Z5QCcCKhzCRLfnJMajSLN_88z2iwlpIkozk7PaIsQr9mxiIVpdu0wmpxTCiabzCRBhG2PqCSyJ7lo0COsROtfhaR5IHV6BsOWpogWTWJj4r4js0TVCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkghfB3cQPrS_PK46QqAugBKPeI61j0xAXnzcpAC5hNEU7g1bDfu4FlhxoczlTn6aMIqE5KysOtdz8JmruQopI9poNUqUL406mUSkGwMmIlyXbFYydZD4sAzmj2QVejmUvOe2NDmis6mn0rARTSLvinFGZsaOu1_83XEQXB3CY7oAyv6RcxNooMa0FU68XPPbt7mYucopFZeEJUuhoF-mq3ji8_jNVQv8E6vOcL9bqRWsjhqIQrOvvil23o3DEvmWnUsoUsy9xdDrFLSAS_b4T0yCXuUL26GD6WB6MzYGi_PJ6rQAIK-2xwssId89vagF-eYk1mQOQygyRUEknz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUvNQkR0HrporZbNL44xyGv0PrHn7LU9oeYkm3c_JVm4uP3gpsLdkKSux1fJgCjWm4Haxe-6KvvXpCkuTNrpgn3NjBM7ZFO3dmt_WJ5duhQT6n8YRmb8OZgm-wi4WuLCemgC6snm446VN1DA4rEjCyOqgP151CwIufD00h8AKPIH6vl4IRolvX7-OzCK3wVJJYN2om8vrG-H0I3MieuMpToANzX1xYXQp6Adabhc3dnMhwPMP1W8YXkX4aDezRPuR9RH08mBeNcNkoTslw73gIngOohirRzyFnVlBzyDHgUY-NwgiaPsWzs5FvjKmwM1HcAUHVeZa5pwdZNqIw7dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=U8jelYqLxMXUinI8CVMS61VxHx1iBRiibVoI-71KkJiQwegZb6Xs7aMmQz3o76G-D_BLAt3SZK4Z1JRTTkbYcIPimd1fGlxR-G4L75DIvWl0ZvuPO-KJsS-yxZThS5CVvEcx6CQXipsc5n4NF66JVkQsRpW5xfbRDJ0OK6nNLf3UlBdxMu_FOOVH6UJ4fc4kpEiSKkSFz7MoEKQr6Jy3QSbm-yQ6R-a-PEF0EKH3UTM1kbyV-QI_cIOUzMGhT7CZmHVCYsQkmRR556lA07WlfgYAo56vqigJ1_Mu_DAJ_3XqjwiSG96NieWntcGEsEZpuldPyoiYJiAlBUG3wumOmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=U8jelYqLxMXUinI8CVMS61VxHx1iBRiibVoI-71KkJiQwegZb6Xs7aMmQz3o76G-D_BLAt3SZK4Z1JRTTkbYcIPimd1fGlxR-G4L75DIvWl0ZvuPO-KJsS-yxZThS5CVvEcx6CQXipsc5n4NF66JVkQsRpW5xfbRDJ0OK6nNLf3UlBdxMu_FOOVH6UJ4fc4kpEiSKkSFz7MoEKQr6Jy3QSbm-yQ6R-a-PEF0EKH3UTM1kbyV-QI_cIOUzMGhT7CZmHVCYsQkmRR556lA07WlfgYAo56vqigJ1_Mu_DAJ_3XqjwiSG96NieWntcGEsEZpuldPyoiYJiAlBUG3wumOmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=MkWgamTRSlebnTkYrzeIeB8qy5HgcT1Vc-sr8ZAG7xaUtNBtRwyHSwqzrbNcidyhMbLt4Md8ctaNb6u1k7kWa6jYpS4y9ZjXRhsayeNoNzChY7qtN-NvYZPBcZAjnCrpl3lRXMFNWtGWdiQ4eLBuce46pDxDeZxv0xQq1EVmvbx8gEAfZmowSNu8XsjH6w4qKd2IjpLo-2hqgNEKvXk0vMsC9EyW8ONZ2al8sKCmTMEy02FLZ79Fbg2VuY4y3DNlVJHnfr5bNnojVfrjz-YAHh4_-UgYTGBi_27P3WIfPTQfs-4z83cQ95sUE5HsOECL7dPGTiyivvjXmo8wzpa66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=MkWgamTRSlebnTkYrzeIeB8qy5HgcT1Vc-sr8ZAG7xaUtNBtRwyHSwqzrbNcidyhMbLt4Md8ctaNb6u1k7kWa6jYpS4y9ZjXRhsayeNoNzChY7qtN-NvYZPBcZAjnCrpl3lRXMFNWtGWdiQ4eLBuce46pDxDeZxv0xQq1EVmvbx8gEAfZmowSNu8XsjH6w4qKd2IjpLo-2hqgNEKvXk0vMsC9EyW8ONZ2al8sKCmTMEy02FLZ79Fbg2VuY4y3DNlVJHnfr5bNnojVfrjz-YAHh4_-UgYTGBi_27P3WIfPTQfs-4z83cQ95sUE5HsOECL7dPGTiyivvjXmo8wzpa66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLyuMPrbNU2Om9RCwRePIxvBgZ_nBgO0vY6vCVEi1jt_1DYAqifWXwxkgUi8Q3XVXv6T_gy1639E4ayXVjnauvp1XD6Z0MCKS9-FcZRqyfrDBDtLuO6UBxQfwpBgTWv-t7qwW_j5KiDwuNUMGybG3wDxCIZ6e3zGIAN1SYzHFBEDigufW6HNkCqaBPxjtxE19hl1zcsH2eF9BBBu9Sx--pkiSCeH3WRv06RvtDePKB_3g4sMdPAnmUXKMSDs3Uglu-U4w0GyVNGPXVsLYmGhw4ODPtlJUQZj-ecEd2jFy6UqPntw27BogtULCDNh9jA7UuRP7HMyxYIOhdkaC8xZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqKMihdepCOLf9fgbyf-aRb08p_kcrbFn4AUgaXz5BbydBL6Opn5Ll7tpamo6_QgyCx-bFgNOolFElex1nRHcPew_fH5oQiruuwIZBlc7Eew16OiY26GnFw9ib3T2zlFzpBtClAfZ-46dcwfoqVpPMYpTUyKkorQ2hX-8rtuuZOIokekgeG8SV9vJoaWukB-Q_5NCz-k7D7J6NIJnP0ju8pNtXOgitvlWwFl7DASqB_quUOqYfJA3R6F2NRwNQrkikRBWMzIyetqNTSK77BJQr1jc2kGqaTpa8JypkQBGOdlDHZ7a5ylB1UWXPigPftec7dNIC8b4_Qru0t7GLwEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQMXQjE6f7DO9bWg8PqnXvEYZLGmTHix500G3J0pfd45CZOy85ToInUCihqBf8RK317Rzaqa5wRwe7M8yOgfSFVEupvAZ335LF62f3XDEDY1YpqZJ4X4WhNo3rTj9FkAwPg_89LPBvabDCk0iTov1motLv8VphZfqp3owSgy3-z4q5KXYf5ySXlrPtAsNnBJeKyrA_D6s3Bk4gi70e_dIkux9ZvnChgKrmo-mDh8yodJ97KqueKA8e_WaMU7hgDz_mfiWnSGP1x-rj0AoSV_dloxntzko6iKlb1tmdSwGNZoLJgfqrJaIGux4UB6MEMF4IHnfRgcKu69cGeQbu7B6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwriN4Z7beQf0BeOSMoWBvKJWiFqspb0kC9YvNAHjrplwfO7aYwxzt3CqcxIGxhOezEPT40IFzL-weDEAN28tTn-A9-sAPFL8xGyUcGu-T9JGZvjeHyFKdumOLza0EdNesedmPNHD3vVqUZpP1oRyogt5gO5d89xxnu7sTFszex4X2D37yEGUbBSGEDokhhpUmcja-9s-Bo0wuwzrb7pWFqrabyINPvIhIOeZmPxLz9i4qfjOg4MIRLArrEiIhBJt4FlPSxMVkDIJrf1TZHjgtPZmHBuIpqIUCfvSKiA0H9BA-juAQBzBvTw-f1Env0f-tQ2PzBet6lTPo4EqBFqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1k3jNV4Q20HYU3jnKNskaYek7_f8jv6DaPc3hZ-Igx8Kxw1l8sIcdtSm-EcyOK8IViOlYu_JE6v59DVZs6e5do1c4kWrkP1PtyPK9vUN4dEH7aNCcCU0K3iyc_Oi9NPOYtL9XbNESYNDhSM2u6FNiO9FdxUV32bAkvkiES7NxiUsDzotxwpyQH4cb91BsD0QR5b5pg6iQ3sla82ZPFLa-Z10qLeZ3UsGr5ihe7rQEyjRDl0XQ9DgRmGKgPttUCMIECr8m4aA8cQyYZKwF-EkE38bb8kckzZU0QSR2VrMdcvNptNnZWTBpi-rf2-lXJXevjRQT2Nk6EZQy9Pb38zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7znj0xHdijINe5WxR4n91CWy5MLLQs_CanFR8Swveztmr7vljbsYLSlSO7c1h_WvTYRBtOOEruuYFVN9Bb3ClnjkNbaA1XeryvJ-5omyg9dQrgCn-arRCUG5sfLkHv-ErFU3Q6gpazyHOoKxCsGIk10xyHJ41BPgyEa2Nq4L9GW0pKT1TkVjr1lyjnCXkXb9tDAX3Kw91lswTpkNZintukt6yUNZ47rZsR_s-O_tdoEMIUAQmQFG8pe2LXEUHfh-w5wbQLCZcQcaPJgdIXbsN85-a891bhJGB3DqTsoAvP_Q5Nlnysga9r6124X2EmPzGLVCbdzQ5wselBnUSDOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIQqHOpvlyxcO6t-1CYPeAmMja7e7IzyZLF-oaDA17gsLhI40o9IPH_ahX6LUdLkSJO-lFAj2I4HSziWMbVhWQpHMuVvD8RUXMZKwGrds_YoB3ovbw8ofFHUisKvAArz7DuBIuQQ8vHA_mLy-XqabOoZ-G3_xiMcnXzydz124BttOuV_qY-TNeKipzMlDR5EA5zjSJ3kv8QEFv2Z9wBFMeadkGzVboYpkSkZuAq_udtdPYwoigNiST6zw9Sj8IYfACE7qwqWN3VZukp50SCN56Utf-oFBnbGK3xkpbTSfF-v5E1cBChK2Rwbqow-BUIQvhFZGWFdkKIVp_9KSrBP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=NDpITd-eIxRdbAQbo1MmzV916rmnWP_o9sQs6o2iblpfS8pdYcNBbZ3QefXhdEc8PmbGa5wvnuXpNUsXUkFQbCEzoUNlOFvKtv8qPJGKmubZKPDi1zmJmiyIsaWOHLPSHIeWw3alcqSrPn-OyKZYz71DCvfK5X-Ze8nvKBjVc0RiRNvnlQHwnepn1BEcvZ_OlprcMhxtBzAI3LwLAMA5hDTc5Q3XloqRYGEuIxQZiQOCjMIYXEAaRhXJ64WFb7zev935KNy8CUie2zUaC62ATP1wEBZvvtlVrxQ9tXPOM8gtJjUut9m6SV6dvjb_gZjUhrCb5B5OK79ZL9I4n44B4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=NDpITd-eIxRdbAQbo1MmzV916rmnWP_o9sQs6o2iblpfS8pdYcNBbZ3QefXhdEc8PmbGa5wvnuXpNUsXUkFQbCEzoUNlOFvKtv8qPJGKmubZKPDi1zmJmiyIsaWOHLPSHIeWw3alcqSrPn-OyKZYz71DCvfK5X-Ze8nvKBjVc0RiRNvnlQHwnepn1BEcvZ_OlprcMhxtBzAI3LwLAMA5hDTc5Q3XloqRYGEuIxQZiQOCjMIYXEAaRhXJ64WFb7zev935KNy8CUie2zUaC62ATP1wEBZvvtlVrxQ9tXPOM8gtJjUut9m6SV6dvjb_gZjUhrCb5B5OK79ZL9I4n44B4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=UsafrRVYJRimnw0CdBlwh3sAhBl8HJNUW2_sgDjgh_YBqI_cbpE_Y-Rc0Sf5zTg9MacMUyM-wh-B1UddHSCZQroNCkbZUXSy7FP2dvfAgQ9LTVCob1FvVaOHulR00NhkmMBRSAFR_srlSGQoyvqKBiovSLeT-BOxUOr1YW-a35qcqDrwW9CIeoqzYjAY64_WTXML_UZANElS6KvBQTSGgKrwWdb85nxGEXwn3TNfP5RNACbB-mH3Y7ZnRgc6mFnu--98-5gM9KPjtduG7pKz9REZDdDrk1-KQ_t_1bmDQkFThQQuv9vdARpLAiPiWbQlZutrTZJ-VrPyZPCfIUl25A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=UsafrRVYJRimnw0CdBlwh3sAhBl8HJNUW2_sgDjgh_YBqI_cbpE_Y-Rc0Sf5zTg9MacMUyM-wh-B1UddHSCZQroNCkbZUXSy7FP2dvfAgQ9LTVCob1FvVaOHulR00NhkmMBRSAFR_srlSGQoyvqKBiovSLeT-BOxUOr1YW-a35qcqDrwW9CIeoqzYjAY64_WTXML_UZANElS6KvBQTSGgKrwWdb85nxGEXwn3TNfP5RNACbB-mH3Y7ZnRgc6mFnu--98-5gM9KPjtduG7pKz9REZDdDrk1-KQ_t_1bmDQkFThQQuv9vdARpLAiPiWbQlZutrTZJ-VrPyZPCfIUl25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=H6nRJxr5S3Qptq2ipGs6S_3ZrKNePg4_0gKBo0gvoe-GdZc9xRLDizqrOoTUF4VzkZaPJNrXCz7sHcUAjFqX0jGlFF8C29WTNTYJ6_MvSRT67TNMRhcos4Qu-s3EXn6nZUuwt2EQ3nNf-GnhCYQx2b73qCjjQ7hdI8-4WWjC3WXPZ5UZGVSJpup33-FpncE6pwrOWtUGajQSJ05irDkKGGpjc46EkHtILBpod-7wbmgolYYmyVcGAPRkquqQqUHC3x5mQDPJjR_fBVfVY1qES07cDREziWdKg71cZ9zRcHIuVKgZwfcm4gFmB2VsyyvUGCZMdAohjawi-z8ZEJkcfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=H6nRJxr5S3Qptq2ipGs6S_3ZrKNePg4_0gKBo0gvoe-GdZc9xRLDizqrOoTUF4VzkZaPJNrXCz7sHcUAjFqX0jGlFF8C29WTNTYJ6_MvSRT67TNMRhcos4Qu-s3EXn6nZUuwt2EQ3nNf-GnhCYQx2b73qCjjQ7hdI8-4WWjC3WXPZ5UZGVSJpup33-FpncE6pwrOWtUGajQSJ05irDkKGGpjc46EkHtILBpod-7wbmgolYYmyVcGAPRkquqQqUHC3x5mQDPJjR_fBVfVY1qES07cDREziWdKg71cZ9zRcHIuVKgZwfcm4gFmB2VsyyvUGCZMdAohjawi-z8ZEJkcfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Hnfwcwnh95nDeVpDbp40pSKNq8PvWZ2s84Jt2P8tAI7wi1h3Zgm3vxTMkb7srlVz1pXJBkJQSrwDAQFBr-yP_KvDvNx7iw8GvqtpDMDjciRccVXmdYnPwHwne4VxHW_YXf8Dh7Rc57mF3Zm2WaGKfy7Rl8H6HBceLbLY6lNhjLOsG2PKZKUn9Gzq4R4PMVkm-zsJGOSWNoUbx7IZd8KgSHfZY86sUG1FNIHosDYM9Vy-MoTIMtE25jkYV6TlHwpv7ov_cqWjmDpZ2LAY5QkpfAcJ-Yy53lHM6LsQGryQmLWFLXP_DxNXYV-B1MQqaxaBi8leey_BmcvykGI4g42o1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Hnfwcwnh95nDeVpDbp40pSKNq8PvWZ2s84Jt2P8tAI7wi1h3Zgm3vxTMkb7srlVz1pXJBkJQSrwDAQFBr-yP_KvDvNx7iw8GvqtpDMDjciRccVXmdYnPwHwne4VxHW_YXf8Dh7Rc57mF3Zm2WaGKfy7Rl8H6HBceLbLY6lNhjLOsG2PKZKUn9Gzq4R4PMVkm-zsJGOSWNoUbx7IZd8KgSHfZY86sUG1FNIHosDYM9Vy-MoTIMtE25jkYV6TlHwpv7ov_cqWjmDpZ2LAY5QkpfAcJ-Yy53lHM6LsQGryQmLWFLXP_DxNXYV-B1MQqaxaBi8leey_BmcvykGI4g42o1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=EPyNd5EQUJ9kISIvVAVgE7kTzElTkWRcaqvdevlTV-hiT3EPZ9gTiszFa1LW6nXCAjOnrxw8pr6eZS7DWIRfg0Fk_4JvtHQ3kWaYwL6ZoKOVsrezra0x5tbAhfY-ns5H33qAPbuStDd5P5q1glKUrrql3UbMWR3yYJXa1esbiFpIX-KuShGtLo1b0klX6ymrOE8_AT93oVbKvcXthPSkEZl0F5lOaIPbRF66yLkN7MZK3TOknQUHTKKO0B8yrRa_LN9uTWB_EZyx5nhgQ3Q_g9iuj_QyEZ5ObcaoyDp83Rw1Le-aNHGqSUW8Q1F643b0EZ42PYftw4YreXmN1N5lXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=EPyNd5EQUJ9kISIvVAVgE7kTzElTkWRcaqvdevlTV-hiT3EPZ9gTiszFa1LW6nXCAjOnrxw8pr6eZS7DWIRfg0Fk_4JvtHQ3kWaYwL6ZoKOVsrezra0x5tbAhfY-ns5H33qAPbuStDd5P5q1glKUrrql3UbMWR3yYJXa1esbiFpIX-KuShGtLo1b0klX6ymrOE8_AT93oVbKvcXthPSkEZl0F5lOaIPbRF66yLkN7MZK3TOknQUHTKKO0B8yrRa_LN9uTWB_EZyx5nhgQ3Q_g9iuj_QyEZ5ObcaoyDp83Rw1Le-aNHGqSUW8Q1F643b0EZ42PYftw4YreXmN1N5lXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgvtS-tz4sDaIK0ZwDcZQwogYn3hL1ImyNykjJWtf37ty4I5tEc_36egJbPu1mS_GiHH8vVlv_zxKrxU-gaQR_6Ozj9kfdwfMxWsjDEguJ2F-80VUoRCGAl7wZEVmn2gWJIY2DCK0DoEnVbAunuh_B0192eGYvCzUN6F1NKUXnYN5XlJZdun4HUf-iHWVIsCTqlTzzBEL0oOIeQ0bvrjp4-QwRTsr7af-OycnTINKy_E67YKO8klSyhuEEYjw9BpAIXx8L-dW-kTbBcHefOmryf0PP_umTj4TVkcuQQVBjpJ_FMp68d1lWxySFwKPqTtO7zTK7o9ycJrL2cEw7sYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=SbEb_n3TlsZMIXutEXE7CAG_g-0nW8VozgPtUIqMaiyZXpuEnXPP1jrKXrFcI7Sxcvcev2HMVfCS-4L3TZKIDw_YEzOlWg6_9BDbZt3ThFEWC4OVqDAIQCbhZZoSuwTsg9-olCXlHs958HX8nmCTtE-T4r7ApyyQqadPKr5nGOkrLEywn0r4eYn97dtrw0f1lfwnbB_QACrLujUH1TtciQYogThn94qwAkI4yVV8IEUDPxuQKqNOzhkEi_rZtRVJ42PZ2RlSpTj6FL_h0GEoC8207ecK9Gq8cmzK_42uPbobF-DYdVx0HpAgmxSXfjYGjltGs5LVyWnMkiXqWu-5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=SbEb_n3TlsZMIXutEXE7CAG_g-0nW8VozgPtUIqMaiyZXpuEnXPP1jrKXrFcI7Sxcvcev2HMVfCS-4L3TZKIDw_YEzOlWg6_9BDbZt3ThFEWC4OVqDAIQCbhZZoSuwTsg9-olCXlHs958HX8nmCTtE-T4r7ApyyQqadPKr5nGOkrLEywn0r4eYn97dtrw0f1lfwnbB_QACrLujUH1TtciQYogThn94qwAkI4yVV8IEUDPxuQKqNOzhkEi_rZtRVJ42PZ2RlSpTj6FL_h0GEoC8207ecK9Gq8cmzK_42uPbobF-DYdVx0HpAgmxSXfjYGjltGs5LVyWnMkiXqWu-5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZLhsv9EBbh9Ss8GjWdYZDPKF3GsorQFb8qjSegV9Nd5bRmuAacr3zxAmLFnj5JsB1evgaWQBWVQJJffOdS7Po13Ww9vxH3cTYNr3nKkMhCQaD8SICAwpufXdDbnwNXycnXzo9wm_UgApiF7VsH8Af2qDHv2-CRGFbrmt58ILj3lCFONcS7Cw7crCP8MBsrEvjnQhUGxrg9NhCw3-LEjLU8oaq6DGJajp1K_WRrj8mF4USWckMHtgE8avBQ3U7bix1nNDwQ4hXmzmrpsMAv2NizhKBYgQxgcjy2q5LB47K76Mb93DVF-sgFqJdofWCg04sZRc16u9GB09A_o6Iw0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZDwepRvjiUGyfSIIXWLaLTh_oHbvgy6Dq0XMgJFRUt37srxr5RijLjkEZEw339sWmREZjXnekrDSRmVTJIcqBDhEPmZPo1xsqJV1nGrmxg0O1UQNYSIXgUPmKGLVAKNqEKpexb1E8JMbTavSWvq8MsGw6zn_vsEexf-uw_1u8e9aC1D8p9SLXefzjzpco-xtruYPC_Q8cEh_jWXxe9Q6Ets_sxh3gnYY5hXy98-YLPFQrgt0BZ6DU09XMcQsJu4O4SxHGnNTd2UP_DJ6j3b9M4QBfIGhfQrqzyMiVW5Fj1eJyyOKf-3-vEyeWQffPlucLwSPJedyuI_UTSL02V-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFKgw27XiEw3yHcvBrnGXNZVGh4Z8Ge0zWCVUKwL45Y-MGL9fV6fgQj1KCWFx7IsX_GUDPUwQa9e1hV5EIPrsmXnRprwTMfixytIOPItr-B3f49qg3aGVMCyBE6szW3MecAu2LyHVt8FMy18efXkphAANStj2qM_e9PQUnEXWPiuSpxKzmLSZ-X7TyCH4JHcgzYwYttIpulhjTHJqJp_5LmudoLRWRqkdYKzXBKNCRK8fWw2kE_DiPjII0don_SxsNTg1kmSJeJJ0Xx0hQI-jaLPXB3vwj60j5G8GzUh_Ofq9ZAI_D_ElqBtJB9hpY0zMH814iBmWgT0QMxTXZ2-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGbHAMYw293MMDuAp98F7Bai32mrF6Iww7ry0RQVUbkSCuTCY7sUnupfN5NkKqNrw74iGiiL65wnc57X3sLfKA4odLtqZ28zuwcwO83R8hQSAh_kYxc-TniCboeleiGXoWI1cH0o5TlsS4o3_KQcjmaYwaTiKxz05i2D8TQaew_mfziz-a6cO5zFCq4CtO58EHR2hhiM9WiGVmh3mrcXq4y_BYL6y7H5N0g5HPAfy3La2vtLq3LFaOYP81E2ZAjlEL4vZnFvEhfNBW9KjPpGchtZoSZTt8zRq9zQpg0ICVjSjoUjQ5wY6XpSJ0esOBSarNsKj6EJQqtwqCP0sMAZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=oZRJdhPWDE9hjy1945QBBYN_PwMz6XJeKF-Q8lp2MVZIvr0sUURGFxaKC8fIyPBErtx4pfE29KiQob1OcQCspYGS092MttygsS6vKbJd9aH03VyvEXkjy9irIYP2SAKISc8-qX6c22_JwAAI2KGguPLNB8aReeg4MluVkSgK3ox7e6-5oXDvXfzQK6x3nA063vDlF4W2t0EB2tkODRGjkuo3i35MXvoWTL4dpJlh0sSfNbqCvu2eabW43mDJcvTxSdCRadpPzHxubIaVPBZ5IJY9uuAD4NEi7RoyAhPq6_6Z2WUpA_Siy82f4Qwc_Oo_QjKEQyOnDGMWCI7a8PdhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=oZRJdhPWDE9hjy1945QBBYN_PwMz6XJeKF-Q8lp2MVZIvr0sUURGFxaKC8fIyPBErtx4pfE29KiQob1OcQCspYGS092MttygsS6vKbJd9aH03VyvEXkjy9irIYP2SAKISc8-qX6c22_JwAAI2KGguPLNB8aReeg4MluVkSgK3ox7e6-5oXDvXfzQK6x3nA063vDlF4W2t0EB2tkODRGjkuo3i35MXvoWTL4dpJlh0sSfNbqCvu2eabW43mDJcvTxSdCRadpPzHxubIaVPBZ5IJY9uuAD4NEi7RoyAhPq6_6Z2WUpA_Siy82f4Qwc_Oo_QjKEQyOnDGMWCI7a8PdhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVEL7rAGEuRjpqfqxhJY1-xwsbq-aPfxUbZ_Z0iHMzuF0NgIs6hJUs40rkH_EsOv41CH7HAlltOuZ2hrK28K723Ey3SrQZ9hzgJgtrjWZoFMJY6WrstkjBOyxC4VGSryVhgx_3pc9xaKgghdQELoAlNhFV_O7kTUNB2CoOuuAayaQz3vTKVfUYdcAwK55Ywy64HHWOTWCWStdKK-rJk3WkD1o8q6lQ7wl540VlpoNcP2rY2xIKXqS8RhhbUnkhnOQtYTAH4xgv9ULWXwjQczUY1egqgFuNkvSJi2-Axmv_Yg1wjZA1mJoVnE0VPxm67TjPW_780qNJNOFY1PMx7JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=tK4ouzkj47sQ22l-nSrXEQVpINgcUE3G5Uddo80lpQ0wFvVrUovvIkNCn0vtqnJLmIbG6nHeC1PY1c5OV1Ro9DZvp7L1dJwq8ZWzEF4Fp9EztXzE8U97Zd3h6lHOyO51lblWdhKpIzYf2h67nUOlGIBwCyCfB9egeT1uT8GvNLDm_G_r2CqWQeiJ4wT9A_hRqjYxxpPR_t_iBLgOYPws8JfdOrC-aqgi4EhJ7bWFKGb4Nl3ldLbyYS6hsFyLkRYLaoBVW-uqCP6f9eZeeoUDbA7QQCD7N8PdMQc4Rz2r-mHwhVAKLZqIVARnlDnZbYtSf9y58WwResO6XLQxxp5rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=tK4ouzkj47sQ22l-nSrXEQVpINgcUE3G5Uddo80lpQ0wFvVrUovvIkNCn0vtqnJLmIbG6nHeC1PY1c5OV1Ro9DZvp7L1dJwq8ZWzEF4Fp9EztXzE8U97Zd3h6lHOyO51lblWdhKpIzYf2h67nUOlGIBwCyCfB9egeT1uT8GvNLDm_G_r2CqWQeiJ4wT9A_hRqjYxxpPR_t_iBLgOYPws8JfdOrC-aqgi4EhJ7bWFKGb4Nl3ldLbyYS6hsFyLkRYLaoBVW-uqCP6f9eZeeoUDbA7QQCD7N8PdMQc4Rz2r-mHwhVAKLZqIVARnlDnZbYtSf9y58WwResO6XLQxxp5rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=nHtusmmQohlUYhSn9m4h8nSl59nhf_kWjT778xfOtvTNnsgedn4XaeGt21uG9PhRRJvngpRknRiL7Gz7SMBUYCo1G9wUSsFuDMtNBL-bhllD5xPvgN2rRlCBMZ4fhgc30AQ9XO-eHsuQI2FhNlZsRZ_qhu-boj1kr2TF8CcV9qsevW8AmaHoLIZLLfmL6ilduC79uKpw2T2f_t8bMDnakW2ndZg7aCNIg9u1U-K6VZ4Kj_kuyKiGDlMKQ7bzLqeRu9qSmguBogxvzchxJ0T7lbdkzoZ7CnMKafRw3xeU2AExKWHoNlwuxSR39Adk8wHhuGjGUAp8Dcz-g8rbdXNMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=nHtusmmQohlUYhSn9m4h8nSl59nhf_kWjT778xfOtvTNnsgedn4XaeGt21uG9PhRRJvngpRknRiL7Gz7SMBUYCo1G9wUSsFuDMtNBL-bhllD5xPvgN2rRlCBMZ4fhgc30AQ9XO-eHsuQI2FhNlZsRZ_qhu-boj1kr2TF8CcV9qsevW8AmaHoLIZLLfmL6ilduC79uKpw2T2f_t8bMDnakW2ndZg7aCNIg9u1U-K6VZ4Kj_kuyKiGDlMKQ7bzLqeRu9qSmguBogxvzchxJ0T7lbdkzoZ7CnMKafRw3xeU2AExKWHoNlwuxSR39Adk8wHhuGjGUAp8Dcz-g8rbdXNMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzg11khL7Uxo1t7rkfI1pFC5UhHhitTr0TtLFAdLUNm_HYgRZF4R5GX6O7jtX7wxyeGy3bQQHnNyzoK5VTqn6IPz75NSj655LltKxB32NIafygy3IXeNF4V8DqjcVV8kSczmCnAQR_IaKYOYWR3FjIzkrACf5LgdX6mXbsq6CWJhgcWPjmj2jwDv-93YE9B1M8armJVzZq_n9zIuOs5feaTCMBKTCvEVZ5PF7RbdF73mJC86xA_gNuOrxSUC2vLO-quefbjcJykZPhTXYM5D4N7x3_VRh6lmfFXztaqqBoKptDXSTv9RLd5T6ywfpSDeqzsEwGF5vOy9X6Sx0rbmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMGpi75LVSDoguELbF02YLVQ6LVzsB1dGLoJpXWbWS3a4BIdpIDzEy-KXbAvzouThUud5r1IPhqaFvRJRCRx1tFP8wz43KjwrooJZxa3exygNAlLRGYmZ0A9cRExDu9Sxlv3oVGPhElmNGjsfRikL5Ihn43QzJ5PqfaZA05NQNxDg05VdKdhJvGqMOmn87W42CQYma9KDVMMtW2Orc1jj3i9yF-qy6CchNQP4JwZjChnpJkrOPw3DkynPjyt803lwA_lkCuIjL_3elTT1WlsldoeR2hPr2My0O2c_pswZ-m3GLLEOiKcdTxFh2JDEo0n1iL1d3sFw7Ju6XfbffzLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjPpW8K0Vs1Lh1Pc_o46AwqDzTHknKC12fX27_1S1VXLeFZkL_A_KQxKqoQ8CEWmic1eSC_t5hS04R5kwqzzVfAZwNuAyBWve9uROFCTUw4cUtLIrWm2qBYUbg86Ec8NClohiiBlY_lPXPGN53izaCEamTCKRQBznNdiS6I9KXspvZvgGOBE3KylbI3b2kFfniLbwYCE-RZpe0uXhCMwJyGvCetogq1AMAmQK9nU5P9tdLORpgaFZxfSbYNB8yID0YPCYtYy4WndxWUqavgSo6yhx9lmQlaJr1LsWElrSPttagLH5ULq-yGe0YL8O6mHRxRa4m_6TbH9QHitCCqH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=LWCJLOjyT91RKqRoLlsxfW9n7ltOqmKafYymBHsXzFPIFrjwyaj5XjeFZP3pZ-Lwwdz6PcZWOXiEfw_0clb9kreH2ifKNJmjJhQ9dv2d7bo1iJRilVDtyTtdcQvtQ6qOnDaF_9jEQI9_uYVj0hnVqVe8FbX4nEj7PcSi5k9VhcoNb1JUVGgS7rP_jUc280srn996sxoOSfhjMgNw7L3ALn5y8AfN2VPnvwjtru_ARx37olWRZMfreAe_DnAfW-ZslU9hjS5H2ywz8tGdygG-H4j_ZjZx6JszmMQQA6EKnnmLrZaShWpIjQxIpjXCkTKCWVt5dShZNS3arR51jonmyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=LWCJLOjyT91RKqRoLlsxfW9n7ltOqmKafYymBHsXzFPIFrjwyaj5XjeFZP3pZ-Lwwdz6PcZWOXiEfw_0clb9kreH2ifKNJmjJhQ9dv2d7bo1iJRilVDtyTtdcQvtQ6qOnDaF_9jEQI9_uYVj0hnVqVe8FbX4nEj7PcSi5k9VhcoNb1JUVGgS7rP_jUc280srn996sxoOSfhjMgNw7L3ALn5y8AfN2VPnvwjtru_ARx37olWRZMfreAe_DnAfW-ZslU9hjS5H2ywz8tGdygG-H4j_ZjZx6JszmMQQA6EKnnmLrZaShWpIjQxIpjXCkTKCWVt5dShZNS3arR51jonmyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=sXOKxrp3XkkK-vKPlCyEB3gP5003WJfS7rBzfXEtPrPQt4_NK2SNca-v-0rZlVhM-wonCb1PPC_vIU_w6DORJPRUakuyfi2lUaa08yB0-gC6wkT_SEsP410Gk_fipkGeFPjowFcONbspojWXi47p4FLAUfHszjyZuOIRm_ipHvf3DmGW33t6arvrVDkPQob0Pzx-I8Mk-QXqAv4vV0Rz1HHHdCTax25fkK6uvMUCPR4gdv8dw1Ux1b7qSr8Ca4isi8cawPZr04VrBbUsmqHJyXk8okxWDndYVytRFM66OkAN7j18zwZMQXF1glCoX9GzsDckNumaNgbuP17B4iUFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=sXOKxrp3XkkK-vKPlCyEB3gP5003WJfS7rBzfXEtPrPQt4_NK2SNca-v-0rZlVhM-wonCb1PPC_vIU_w6DORJPRUakuyfi2lUaa08yB0-gC6wkT_SEsP410Gk_fipkGeFPjowFcONbspojWXi47p4FLAUfHszjyZuOIRm_ipHvf3DmGW33t6arvrVDkPQob0Pzx-I8Mk-QXqAv4vV0Rz1HHHdCTax25fkK6uvMUCPR4gdv8dw1Ux1b7qSr8Ca4isi8cawPZr04VrBbUsmqHJyXk8okxWDndYVytRFM66OkAN7j18zwZMQXF1glCoX9GzsDckNumaNgbuP17B4iUFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6YHMgz0TTJbGSfYDl8QRNUVeq11jTeJohoFO9kKtY_nZtKpyDwn_57hmj2QFrOF86DM74J08Mh5r-MVkwVVEiWEXy7NhZMjrB0wjEYGm1Vco3SDJA0RSKK6kICe35ob2Gf_blyDhHNgKbhXCy7KRvVdo3B1ZpZk8V0InhMCsccNpOmczHX8zzlDuT292YrsZ_7jEzVYdbKtAqpFaQ87PFR6oWUl_Q8yF85-fQWL4-hIR4zd5vU-6XZXwswNUXkUi3rdO66Tmxz-eZo8Fmf8_im8uzTxmjscrAcoMVlLKUQq4wOkgiTLAOc8P3YnESFWiLNGxwWccyHLaaYxVvFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkIo-QOnYScKP45m3XG0I7qvgVbMGe1NU6WBRdO9JV5PxadJPKB6xgj39GQQ9Wi05zuowheL2nXDciHCeOZlEw1PO923evHoJBSCGp-3p4ZQJ-HQ1_JKkYVDVnd-W8Gh1havbqIdiqvs-nDZ0f-e-TBb6OshSdrQeZCSEarUMDnwtavpWjw_ySqUMhx6dJFMx3xG9020CxD1WIMY3xHMitIay4Gt0-Wj1T6-TZRNvs-cCMwRjmA-nMFgP5YBibXd1w89Y8oN83j4pDsQcm3DE0gPaPj0jwrsK6KNKLvdD60oduROscCG4y1AVfuqO3dlUhiInjwHqaPCpcCggM8Z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kueKy6-lsPHAMGQKHVRvlJFqt_oNt-8iAFc9JFVRBoXfMBKlBLKA2hopfH16dSkr2aVsA4ON_qIm1Myx1zAcRw-iXDSxsocuz3QtFlgn9Q-S27nP2D-OJRBZ8gsO6qxtmEGFyX_f597MVQtA7-ixReIH3ebHT1vEdwjLlXVJVCFClnOlstQ-pDbl-uY8e8R1KVVWbTLcKtX7eUp4Jht9JOLklRHxm0G7s10ilUHeFXAuySOcXvD4ByM91dFu9CIWSNpuQWAGc8CgCI0HBX-1uA6kQJvMSRLpOsq3oI-mRh__BB1RYeUhXq-9R9v8DmELebR5keRHdEhnADW9vct_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc2cF-389DZDnogwgW9xSP1gb61qR-b3DKZqpa_zFoXyGydd9kMJcd_43TZa9vINmLEt-kJwFGQOBfsJLbdeKB1WU1WTFDj_B_qtDL_newrXsvaTbU3HFS5Ki1E5gspUbiVekiJePWiRgY242AQs06OXzZ_5scHQjep9Gn4cRxLLyhtPk5auen2FUFGUKcN3j9dA13jxUwQ9WA5qwFrOiHQuhqqCzGk2Nub2jcKuJCEjcFzKFACABQUPVvMFZTJmFb3brTMjP8Ie8Ebchm3IWpueNafbD4uujGu_cRQhpGcC2Tsmq4sgbjgcwsvQfoyOyd73lmRCSLyiQkM6n29VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjEQgLVIvk6aaEhAeIK1HzRba_iGI-f3NKNQcLUVTf7eQU0WoclIff7BVi-4Iqlb6QB21EKz6IKEn3JwBgGxT6r-v9ruPViW9XD7MyfD5UfSmQ1tr2lbT-NVZI1bM5AjN09qQNPx7Uk0UT__I8ffTqkSK4p7ee5NgrgJqnxuBbWX100QUlCaHGUgN65P7mNVsNASccB1mwYvr7fkh5uH1v6xmlLs72kPscOm9-2wmbEIaxCGVukcwpvKV5y-4iFdpZwyzCj1SQ22rNplMVaLDdOs7RQ5WpTdcUaolhfhYQFXepORTU_lsFraY-0Af8Tk_VXtpZnhmEdR-jzuGnTjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
