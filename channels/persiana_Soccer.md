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
<img src="https://cdn4.telesco.pe/file/K0qX30OC7phT48fjn7687RXAAkWzZ5LKuOEqJIEpCmAfdIUlc4TihmqTWyXaq2zxDKMtgiysQVxvbv3GY0TNS8lTU048qiWxy3APzN0ASFkr8vN8u9FO9xqNifZzTpT4sB410sFEQ5L27rP4z1Wu9VV__hikT3MInoTZp0vxQPFcEG69L_W2rJmzMAHrUyUa1YtXeAFPDdXeaGhTjZbLq5ZIdSQmGshYjwykIMBfCQnHhVZGRJIT8CI8leXoUffyYAmPwpGfoGvwM555n1HMHBIKks51_g9nDWMLlrUErFwaTdFlyDibr30ka3uSTGz_i1hQFp_6pRdDD5Yrr5MlkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 479K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
<hr>

<div class="tg-post" id="msg-31405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📹
هایلایتی از عملکرد درخشان محمد خدا بنده لو هافبک پرسپولیس در بازی این هفته با صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/31405" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tObAl7fWS-QtsdbWYxYuTKyBVirxZWSLwmtBGdjR3ECCIKmjtSmul8UtdgHKpYrzYkn1q-htXMJ26Y3AGRat2OtwMTvuFX9PMjf9c33aF6xoaezNr-J22_xQdSQmlinZ7dxB9YbadapSOCurCcAANDDCw1NVAZdHJz7SQ-enSkvcjfISEo-a5IDmZxCRRhHlMOTnl0J0HASBjdZJMc6yPGPwVxEkNwsr8wUEefCrishm6g2ZfrijBatpn7Quz-Ufvbf7MUS5f7ypCHlMijIRTBKB8SwifdjTEJo3AtyAei8DuZLxVbdgIqc1MMRE6A-M_4o_acCNfxNtiZ56HL0O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/31404" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTwdeppBpFw45nJ4lbvdjOgScZUZPdtFT2_9ecPgqiU28bNm8dqeSuieOYzbowoHwkDcLJH9pz5JlcXNFrhqidfmrrlcXRqtiTBMl-DpqNY0zyq4pzXFk_iV1GdGFyMzC1GKk5-VMTO0wJ52ipISORhoZsdC_3j5wsZDCpC2z4htpSdYD2P17vPTTc34gCaAR7fgdvnSLLXpI05u-AvKqbCgzVIEdPaUwGUV_edXspy7XD4TtydP9d9XO5pRU1OLxgMZVbm71oxqASUfEvrb0iyZhvSN7ah76g2gSOXVyGkPtidQup2Vp2TT2TCNUanalrPZnE2WSHdmVTc5juG9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادار دوست داشتنی و ناناز باشگاه روبین کازان روسیه‌هستن‌که‌اخیرا گفته از بین بازیکنان ایرانی به سبک بازی سردار آزمون علاقمنده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/31403" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEJwMoGaE753lWkOGNLOByF7GnLbIDBEsQCngIUlMlmuxVWvW04mU6K_cdcXeHNVyu206PaLnV_dfSVW_T56vtk1bICEmk3CTp8Lya5WFS0qxsbYSzVJN_DTdBuW4KcaTYBYi7ecMey3utLJr89vLyk_UAOYPMH6Dm9KSjdI-KSm4aadvsj33Yf8i5YL2w8iyZL3dOLmX2p_E7xAbiKH9KljFTyc66lqscjjfIrjvuVCOIQ5Snsj5PCWmFZVRijmQFYOJZ_NSDtbNnBdQnZHDkBZHJaa2fbeYFJUg6Y5OpAnhWNg3bQJHa1VbFZ36y9I0UUUebsskhhUIHrHijCphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/31402" target="_blank">📅 00:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGbZecKZ16HH_BlNZ26y3x-RxLrEoUCwvcVU9sbEEdj-1thbjh7NigqHuYgSEPdYpwPJ8db9uJtuC-AzD4A3PQfOm6zT341ui8kUchua37r8yZRfL7AbSAyXpkxzLfofx2zvu8X-nL_QGeTCCDqO_dsVbaAZeee9Ptah8vzNWt7Wb4eXRtOE1npa8mFO9LcoNUAgdFmSko79vuwpetv3bmluQqHz93qLYivg1Qzq4kEWqz4pIHfOiFYWBVUeO3vTD9OdKfg-4BSlZCOZUw2UZrLzUjCmsBiprQfLqY4F8Kc-YVuDn63uzznMACvM0BtBMqFx1nUAxKEdO1Pv9f-U1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/31401" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwHu8SNwJUxdm1_SRVk1hN05U0wbj58m0S0xkkLzedp58WiDJPbm5_BM0ryD5PhPEJ2PgsIy8QH8nQasRtKmZoBzOiGq25eFt7O7wGRSQjwKDLSUEzjI32VP7KEpPZjrsriItGwcGfKsI93wDFqNhfv75YpJ_w1di8bhwVrq24LQUw6lnfnhvxrhInUMkP5GPNSm0CfQ3Om6_BZZd3lw11KFAInYsPdBUSyo92vblp5GnghyvjyeMyrV2Ir3M1p7vlceueJKd-JAEAY8sbmIB2mGdpxXD2tvw7AD-YnaHVyGm3yWCHRsh84HhS0ZSrdCP9jHgGVdOkvR8igjzKBV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد جام‌ های لواندوفسکی
🆚
زلاتان ابراهیموویچ درکل دوران حرفه‌ایشون؛ زلاتان فوق ستاره‌ای‌که‌هیچوقت‌نتونست قهرمانی UCL بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/31400" target="_blank">📅 00:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNC0wyDQYttsjIaAp2GGRcrygPcoU_DMfqxMEL8EPMxUYwaE_xskSjz9WczSROC08Njcb5Lr8zZ5Q3x9JbGNl4pFqHbJ_9Z1rKugevAx9oppy8lehkIoBh4CXLlMnuj9StdUUSW_nuWD-pjnYjsRegs5BYSRlpIJqzMr36llxAx1Mo6WT8s4uJhb2EqXf7qh9YHDNtIMEzzyz9_oO8U0SJKqsJmJd4sJIcCBvUbTblsmpwTywHtZGuIoL1c38Mfo6Eg3xUu0BB2nJOOqjoNBT427S1M4iqfKvA_NGvhZL1GC71i_eA0NWr9AU4PQZIIKr5-qt8e7KCru52xIvyGryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/31399" target="_blank">📅 23:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtRnLwKLPrQpyEoiVq5iWC8mF0A9wCtpHTnuBKJNinV62GW_1zcWWFS-eDdYmGHHlq-9c9xtEtZNO-KUi5OBs_anCzbDtjHJiJEZRx2dKimiUQ8ijcc37Y8bt1oI5Ja6Hh00_mgn9ILMJlE0Lj6xzMB9uZJbppQyLWFfrENOvZh2IreRuaxYK0ImezvVxUBoQfLoGRmKHzEV9EBFTP1PwESSBV7jnX3Wu82EfudfOIaSVeB4iwI3DsmyJQeIrbDq9jNORutyNMzt4S1c7nblX22bEYErc_CDUOD9jCmbfB3uGYdrg2bdS93gwlibtqAMohjP-vgwukFESYsOz0NBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شباهت‌پشم‌ریزون گل دیدنی ارلینگ هالند در بازی امشب به لیورپول به گل تماشایی او به آرسنال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/31398" target="_blank">📅 23:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOfLkzWNmXJrARRWA9QG6xOeI7aycgOubbevekOz4hXiNdknhf1EgVQJp4KwQ-5Yy_mZ-i7922QkDJPgwf4074A8DGliekO30vsTXyiTUP1MI4tCZEcdrLExrd616cQmhiDT1_tX51zEaDfIsvTwEofGFbzV5RTePIKfDjyTdgYRjfiP6AK8uF9eBBik8JxTEv6OMbMzlyYeoXJiUt6UndFpsUcu5KCGP3S92MMBTltbfPXCHIXlD1XYUkwUKSbssFEvEWYfX0KEcT4DFVU4Js9yzM1VxFTsr6zkHvxVffZWF85N4pVLGiZWPXorcrlU-w_AGtTikQNHvijL-ZTr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
افت‌شدید ستاره‌فصل‌گذشته تیم استقلال؛ علیرضا کوشکی وینگر 26 ساله آبی‌ها آخرین بار در تاریخ 9 آبان 1404 مقابل آلومینیوم اراک موفق به گلزنی شد. حالا درصورتیکه که علیرضا کوشکی تا 9 آبان ماه موفق به گلزنی نشود دیگه‌یک‌سال کامل از آخرین گل او با پیراهن استقلال…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/31397" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUzjr75bpB3dXcPniPsj_2lFK_egq-U2ad6h1Lpw69SVl5yRnVwox91VxZcTq7J9wmoQRUzwxUTsCzZ5d1HwL9aavK4zn6yzMI37GgM-CoTez9dx3tvG9sBAPGhwZhwVg-ySndfaqtq3PhoIoxLKHZiymp_d7IPQmwowbvGk_CPvDqD7YzjRlWcmfVsJhv7uLAFYQoS8ouUV2YPAzqYxy5XIxk-YP2uyAxXGAB9pBiIQjAWXzExZMFOoyDUVWyouEK4qkR0oCaUeVyuQrO9lbrU7dXXC5HuC2IPFE9iydyiRi5smqXSCvsSC1UWh5tAVYMOEBDsHnnYQTwiiX-krRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد رونالدو
🆚
مسی با پیراهن دو تیم النصر عربستان
🆚
اینترمیامی در رقابت‌های باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/31396" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=ezO8sFc4F15Z3A26o3b2zNoG4UVQio2vsL9jTu_RPjuuPCWwFt_Sy33fNKt5zAPbXwF6bPDP_mxDqggwdRVa60vfn63Wi2-diQjM6mQexEvS8Qm2qHf_eiBTs2CJG29TAsr3Du-Y4i-u1KSnAi6cUxvK-rLc6h5LwAMa8t4EA3_1B1mj9ddYQX-mqcc4WjdsTRrQUvTDRxJOkhOxqdiBQtGd44_5wywp0_mineFfWxzq4AZFsCF-dNHryxoIZzK86VULNL51-6DXatipH23NynlW7yOdQWUKYY-NbR_KUi0lymOoi0rKI5eQCxhXn_tG9NUNCbyX-X9hrh8zowOCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=ezO8sFc4F15Z3A26o3b2zNoG4UVQio2vsL9jTu_RPjuuPCWwFt_Sy33fNKt5zAPbXwF6bPDP_mxDqggwdRVa60vfn63Wi2-diQjM6mQexEvS8Qm2qHf_eiBTs2CJG29TAsr3Du-Y4i-u1KSnAi6cUxvK-rLc6h5LwAMa8t4EA3_1B1mj9ddYQX-mqcc4WjdsTRrQUvTDRxJOkhOxqdiBQtGd44_5wywp0_mineFfWxzq4AZFsCF-dNHryxoIZzK86VULNL51-6DXatipH23NynlW7yOdQWUKYY-NbR_KUi0lymOoi0rKI5eQCxhXn_tG9NUNCbyX-X9hrh8zowOCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگاتون‌بریزه
؛ دانا جین وایلد ورزشکار ۶۱ ساله کانادایی، با ثبت یک رکورد جهانی در حرکت پلانک، نشان داد که سن مانعی برای دست یابی به قدرت و استقامت بالا نیست. او توانست حرکت پلانک را به مدت باورنکردنی ۵ ساعت حفظ‌کند و رکورد جهانی طولانی‌ترین پلانک زنان را به نام خود ثبت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31395" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0EAe_0r9BH04IxdybQqKHkc7tvSSjMV_muLqQHV_sOn9qItGc3a0fPSf4fhrcN99N8Lig189eiYPVz36EyBWazPOUI9prj4q6tsyUJIh5A1-f9WkU8Psh3XDagRZG6dSj3IiZISCWZR4ORNBn3IuLBQSa7pma3WuHcVbmxOrhwPEbh3qQ-SPX3A5TizwLlmtsJMKP-MdNHwNtZHBSO1IyVH1h6TIDh2iN_6xm1Qy26OeBilbSMTznzIu4GzuAZpFx_eF40rBBKrf4cnqipF1-1d0n-AQp4v2mQyFI5Z_JOszJXHep7DYRJC6HRTQpvToJ62Cxr7eWFs5Zn8GtgWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام رسانه‌های معتبر خارجی؛ وینیسیوس جونیور ستاره رئال مادرید بعداز چند ماه از دوست دخترش ویرجینیا جدا شد. بچسپ به فوتبالت مرد حسابی. پیر کردی رئالیارو از بس حرصشون دادی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/31394" target="_blank">📅 22:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeaHxS-xd9GAAIgK2iYZlYJXSguQSvEHK-1yOJNUShCpHN7zC1t2DQifafJbzeXWa6wBw6quVzzW0NW7Bniu8RL8XdLMsFbDZxRm-aSLwCaVAkAvDuaEETL8n_IzJ94CfPFxksPB5G3DhJfpmcYYESj3WYQKKAY1mvSjuBAsL68-rTnRk6M5UkUvnwHx_JnUk2rLbLpNgSgwKggEwSPxboTAhmoyAdJgb0T68Ab5m1eIuMfRQPmeeeD7evqRgIJItOSkx5T9jKP3TH6EmOcIOVJvvAlXqPwcCobjoFX_iB-8kYtmySqOl7Bj2d0Yp5liO0JcBTstN1DS01juLv0nVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت!
زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/31393" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=iGK8fr4l2Uq-UoX5iuDkm1tt1HwfN4V-Ez72e2rDQWEEClH-rmGp6c7GUc5_WPOeO6VnDEQfncrBgzKgKK78ukvh0084WzceM7TkB-gtgTCG_EKhsI-m5pBqYra20qsdI14SYPZrgA7COuY_ea3VA94RNocjzMHTAqKHYnVRpK9lv9AV-d0ZigN-B0UpcZY8H_wT_0vSIafhj9uy_Wxn69r50KeZunQ0OymMVAfTOK-3pbMPR4YrWrwKYhzS8IpixRIZT1faIdm2ZE2GsTjClHnXxgVzdfEjG-ZuIGCibee4XRBjGvdJt65JHyFcPv8-4ohWEINQpE2to6Xp2UjAlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=iGK8fr4l2Uq-UoX5iuDkm1tt1HwfN4V-Ez72e2rDQWEEClH-rmGp6c7GUc5_WPOeO6VnDEQfncrBgzKgKK78ukvh0084WzceM7TkB-gtgTCG_EKhsI-m5pBqYra20qsdI14SYPZrgA7COuY_ea3VA94RNocjzMHTAqKHYnVRpK9lv9AV-d0ZigN-B0UpcZY8H_wT_0vSIafhj9uy_Wxn69r50KeZunQ0OymMVAfTOK-3pbMPR4YrWrwKYhzS8IpixRIZT1faIdm2ZE2GsTjClHnXxgVzdfEjG-ZuIGCibee4XRBjGvdJt65JHyFcPv8-4ohWEINQpE2to6Xp2UjAlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31392" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNJf6sfpS92APfFuJS-w44BR8VP1OGNUU0HQlE23ycGVNbOdjw1t8DS3Jo2fsv6XnSv-eDmkdLiPdnfNmPNkPSuccF2EMNTO3sJ0rWX12rSmsoBh4UwiIA_EndGwer6D7Y0THdELQkC9zECJNv70BS3bzcuS2xgWnYmMyu08lTK7lKmzpFlWoz7ZZNFpk9pyQ6M5omtxkB0j1W7WcvrQVkv-H2rpe3Sur0B8kDRkJEZUMAffElbwt43xYTWbFEapW4iIK8TbKn7btir7cH7wIg2QCzTu5a3tdxel6FveIka2twVMFIKI239bDe1MDm1Enw1XpVQL2ULi5t67XMjGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYhYbUj5WY_-v3yVRjDco09ZN5SWw1MUXNoA_ulgcoXiiHAA2HMmmAmL1J4OzCTNps7aQLTKXUwoCefP9qdPa9uBkl8CaAtaqp3rksqiLeT1tKGRDtNgicN3wTu6OzeuHpZjKZ5XN6Xs6RgwpQ9YvJMC4eVPGI5G3u5Ac-GUpO3G3KsTDO4ysz0FpIhXiih-Fs7rYv-qkPuX9rVo-OIDxwRdCqUtTgty55wNe6Pmh4ytSOCQk4O6LJOIFBoNMuAjIJE5TaA_A3ITmnKxjaL8UOA5tVrm4f5Afq-yVKfZ4P7T9iePMybiGU7FGWPmXZ_Ngg7bUyW0DfQEDfVG-4ZLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDfBAZpuNzK0t43UuDox-jSqwl_m-nv5L2Mq9FBW1kPvcMAjKHnTiptzxf2YSy0FMe-59plE-8vL5WWmwhzba7UbIZrCpYweB6XpWWddd-IKq8plCxNYJXJEDuqWNBb8zrHdgnKAplvxVwGTOvwBwumyx96-iGMeL4MG5qSZvGuljX9PfEUBSxvqoQICatGyrixwW0q1GWe5HEnb97mlFhBO1WL-L0ZV2dEbanI1k-NTJBBINPfHLXjuOvL50AD3Kp7-H-CbFirhpB5_Otnb_y5qsZ1mtnVexzT_Wy9QbQvtLCFDxCwVHfNn8UiS2uHFw3XSBOUpzRUKAaBIO_t1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKq61jINopELUXGBxDTISaX9T1uV-8nambs7clmQBkGzSUpdYOUplmMv-36x1lkNoCxsmGBxIwBSeIhTesT5an4a0EKotS2bfT9xN-3EyhMrywX1qnw6z0YDiaHUskmLjXpOg1UfjU3ET_Lzi9Cc4bHEW9Yk8PB2aCHoqPrIIcGNzK-puDMX4k_PdBlKrPhiuvdk2U0RnSvECkFtcRr52sG5GfIjD_K8xam2OTu15ZOzwTU28dv_35y4Je3JYtXDeaN7EzDbzmDx-IjfrziBeczs5_90YypRT9YNyw15BQTfAnJuyInzzFrkq9Rk3MJHBT9o_l9XPu3nDc9OaAbZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=gFTxqvLjIT22sqdWcLERu1EQ-mN5I4uqWPyGnc8OeXWs6I4iy-XrPereSnX2pXfXmN2iAjfk3OLjkLLhP16-3d5uW7b62VmEYSDgBWU1xshf2DXDJAVCnWg92aZAcCAhQpnWtzbTtrqvgfGccDIcWpMJtZ0dqFPcwDxoyyXyFa0hGd4i6LquUN_GrUzeLZXAOsKratfb-YqsmGd-LZgu2Ec5J_7DcKE7Qx9ajIp4I3MSCDA41wNhkFRXRkV8SrQIThUr8gtge0wae6wB4ppITkuKrL-79VAgqcwR1Gm8ymsRT2Uq4zhyfcsem2KW6tJjTjifYi5wUYLoQPWxN1Ohs48R66y7c5CsSQX829PV1HphKH_5iBqnqIsdAW26mt8frmFX9XRMGLrBcrFNeusw6nA77boLAcirKVEMYxu7T44cW4gIbhDaGNrCkwaZPzuzi46AXeYLGmdwwEOMpbHcDFwFuxng59GuyQJ6LFzUPUYNEEby7Nckqd5LaEupXc7NV8zOsbdpW7PEAFLVMqk5F83SMEEav5bnoTCfNcNxTw589zmj_3gbDniyrWnztQwhVCJPb0ICtIzkwRmEySCZt0ffNzAYQUC7ZmXyEANqxznkyXgTKYi-eIc6HANh8WIf7OpbHI46Dl54bXSMb8bO9ju9OS8VZmPNa0UhcaNmCs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEbEa-DKVmmBv1PmRmnWFwWOHWl94OiKTB0_yIXatFpUKkhduUc_MO_TplA6NCMJyg2681vCzQEAabnPeLUceF5M9PrMZTzaz7emYrbhOmxlnJCtZJCkKdEt3tkHHXfQGym3tISN_v_TfE4msdLXGO6Cy7qMqQxGDSPfEw7HrYqQ588uVn1TpWZHMfMY-UV5B0_LllXHM-TgaV87S1auKJHcxwAmcmfDyttnYwfsBP6jxLOtHdcmR-WdRA_pxHoD3PsAQeZ5PuQF4uNpkCBYInA-ci_qFAxCpqtuCH6IuB0Ax_-nHgLyZ5v4fKfrdcdIh7Ref9QyJKvT1FZYGhxigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/31385" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdMgB2y9tfSDjYusP7FYuNa_2fzSUvz5L1jXBQpDHNzj6J0fDQVSBxNWwzXr_ktZ44zxAE3nClfCvujxkzIBs_EvcDdmO2VY9uL9g9gHHJBReqFjRIFOHE_p91BDtsb7ElQGMVSHVGlYyD8N1RxEKiWDfi8iE4dZSEOlF3h2rjM-o0K3u3V_kDEQGca06LoscOhXNBun3V9ZMupZj-KGNg3rc-2m_z6lh7NmMIcFSBJSbnv6_d4ThcQyhwF_bnCFZXa6mdyHdPbH1nDtuCT2AMWw8hL6rap5sLMNkopnc8Y-lzGP0jA_xHEiynKiU_33sgOetcAegzVwFT8E4duiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/31384" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p50v5y-5Xacos4wyHivoP2uNRyfivJqyx_9cgKLWf4o1B5wfpfNB8gwCMoe2xUajyv6SdKOelbwPV2Nj6ic0t5nsXw4gdIIxenerW5nLpcUh5GTNGTQi8Y3mBeZc34hXmy5nxdt7OE0as3WhUXz3QoZ_XxmrZ5q2hGn40mMpWjK9nf6TnMkDB1QKUM4I3pmMskCQ1TcbcQYgCMXRPc7gGK1IfFPRMhi3UbKWXLFFVON1jw5WVpmyBwW8OR5xsDLnI47_JB6ECLdXsUf-2BIGiS1thiNvXch77DFR7zDdQLhza-qsX38bssLMqGUlqd8mFu8qHJsfO9Lw_T7VPQvUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31383" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAj3zkHFHSdgMlbqGMHRGGJ71gqvzyiBNJIwIifJLxLQKknql0aWdd97SX8wxMRVujcU1Nc4UGsryvC7VBSitlGY5ROBuuirL94Jsq9CDdTxFZdUmlYXjrEd2xL9XZRBCu4c357pxj8KO8sgYBZEmJd6YC4XUzqC3qq_DpdqWcqvxP5iq8cbM9WQtt2XQt83_gqAQBXRl_mUQvN2ScemUQEonwIMkQGYv9EfbdzN-9-wIlQRbQSoXIq_q13Iok5opBJzxzRWHD5ObCs3a8CBpfc3xq0DqBHusAKu_roVeB1KGnYIso5jIgBzCvuPYNr1RRaDCW8BRFKcz2rtzZrgEryM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGAj3zkHFHSdgMlbqGMHRGGJ71gqvzyiBNJIwIifJLxLQKknql0aWdd97SX8wxMRVujcU1Nc4UGsryvC7VBSitlGY5ROBuuirL94Jsq9CDdTxFZdUmlYXjrEd2xL9XZRBCu4c357pxj8KO8sgYBZEmJd6YC4XUzqC3qq_DpdqWcqvxP5iq8cbM9WQtt2XQt83_gqAQBXRl_mUQvN2ScemUQEonwIMkQGYv9EfbdzN-9-wIlQRbQSoXIq_q13Iok5opBJzxzRWHD5ObCs3a8CBpfc3xq0DqBHusAKu_roVeB1KGnYIso5jIgBzCvuPYNr1RRaDCW8BRFKcz2rtzZrgEryM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31382" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkqRG-9xHptV1emuld1gs6gHQQM3FILB5BgW-dPsTt05uR_u7sOMXPvC1gbETbERlnL9c0F1hbFTfDXWPHyPfNgYmbkOYM05sYC7scGWq9_1H4j-QRyXdOk0mH1GsmcQXlmmAmt3SNkDXyxd69eT5i51olW3njV3b-ORmdahl11W6fV32L9wFgIIaP7Bs3qQdLL99IV7-cQsJEXfHp6vVhtn7I0HjlMflF4FRi0SGXVJNw683jfR-Xr8gk5tgmPLzRLurNaj6J64PnGs_ybr_cZLbhVIKDYeV2lakJEr7NXmGii1efrQDk7OwU1MUUZzJPFDTv7LSB8yTYSTasiS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ زهرا گونش ستاره تیم‌ والیبال واکیف‌ بانک ترکیه باز هم نامزد بهترین بازیکن ماه لیگ ترکیه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31381" target="_blank">📅 19:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaGEWJdkCEJDGytyD1L3voFeQl-gT1f5xIAVEhtD9Bqz9ncLr4LqIPN0-Tc0vKAE4fAmoK9HbJeLRwvy4zYxoU4ei6VIlCF4ywsl1SoX2zcauLQbez4bRaxO3hnLYwtpq0gE170sfaIo45jfZKciKwi8v2VNe97k7QaxDF4lOrV4DcvizZaHMqdj9J07bJHWVoz3zIe28lIejkxiqMNogF8_VxhYLdfghU3nuKhXBnDJe8IsCpbdUODo9uclfu2uiUdeW9Ql0zpDpggOOnjKHXH3bTnJsEiXWb3EvtOXTkmATVZdX-yVGFxeilFTLn1EqrBHwoH6W8RAj1eu4BjVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سریع‌ترین بازیکنان تاریخ فوتبال برای رسیدن به 100 گل در5لیگ‌معتبراروپا؛ CR7 همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31380" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8eyR7FllEW5wTwPhRnhml3zSMo7DQ1VP9iO6Q0w1KJE6bPrwf1gDNl9MKMKIsIlsU1eiIiP1GQBzCd_VjDKvfyd8Ges_NN59o_fR-fwFzBx08QwbbPVe0KEY_5VDN3qBdK4dRzaVJKEYuc9QJMOLZmlZtlxkPm5zZyQ-sBKcNVGEYVDWK2BfSX-U-Rd1oGOc0BRqHS6st6fzZrgqUBJCX0Pkprh49kwLPhkSQvVnouRIU_PBYD3jjXmJCP4hmIRqqMfk6MYUWgi07FT2aXwrxKjNUAvyfamG1a_aBhMEFdDBJQtCpOOLsdpBle6iikadXaMippKDxHgnCZ254ux_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگار تیم اینترمیلان هستن که افشاگری کرده وگفته مائورو ایکاردی زمانیکه در این تیم و با وندا در رابطه‌بود دوبار درخواست.رابطه جنسی با من داشته که هر دو بار دست رد به سینه او زدم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31379" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKoaSLooqoU2oPKDRh_sbUHVxRolFzPTlBLjuuc0dMNx8EGyRt-7XhtWFw9U4aVcr83q32CW0AintqauwbXXdc9yUFOAxs0yIME2x4Q1RKXHEu2rGNTOHcF1BFeAyf5ggxQu1LSTzH4aJtxBGDW8_niHj0uR6Fx0OMpDQXf4k1cI8ioLlfmGS3oC6M8hyY_VTCRz62AY1rvxCAIDfU7PkmNRkcsIUPB7GaNxM5b6ujc-XVmIl2Mfcci5qYKx-05DMQUEbe4j0Ua_jouU6iIOhwLxON5oKVnpnCQn5bOWcK47v1G0PWNPDCVnBBCQfo_r26Sac7hi3k4TmvNtn2JwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیپ‌واستایل‌تمام"بگی"عیسی الکثیر مهاجم سابق پرسپولیس که تا آستانه یاغی شدن هم پیش رفت در اکران فیلم سینمایی ما که اخیر ساخته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31378" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP1Xv_Ak9cGnQkmrYpl4yn6V3pcDoDWte9XsUxwVX8ZoarUi-wttvQV4kDwfCToVpPrZhENkEPQTWGo-L-cULUFkNoNsgMIWYFyFOUtvq5YyU05dXXUGQIu0jNHDBsl8y6B9aZF7k5_DdjX1Ri5u2lTtvgUKZ8K208JJ0dQ4d3TyqOj_BFi8rCnugDt-qh_nLWdcl4JzY604TfdOwfNVXgDsMQPVY1yplmUtX-TCOzLzzQkorXoxXzudKb36FcthoMJQMse93juqj3GOGAJpKCny0TDpmLnyQ6PkeYDNXNCBQwo2wDGDkMa95G63wZaYxnNn2Ozf1-6M4rxND3HvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31377" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G50O3DRLtIH-HUGYFuSbcLTzY3gb1w85D5rbheuu5rplzt193AjrqacsTfrrbFbwCrxMi7-8cTJcvzy6-O8YpwA6QJfYhXCG7VeA_weOiWtFG2suFX2nd_xoOpCaPhWr9h8W9fM5XKebq4eyFE9pG7wQQfeG4jQaSryOHw7OLj4Eb9UxinyTTKKz7OLSF3cM7nhnXXuP-OD_GmpqotnTYbqhKw8pCnG28_8E8u-ojiBYp4DVqJLIRrpsxuspCEjcOJPS6fFYt1gP1eE59RHRtmc1hnG-wWSrgO_uQcpgvDHiYoVXHZ12YSE9sjprrKPuE4LWuLrn_18lk7HJ_SbumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31376" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkprrum3pXvUGRiF9l_iIbwYlpA0QczPi61CPdMI_5ivO2r7Y3yIgw8MRw72DFz8mrbUZlvQRF96K_a7cOiUxaGqK4E29tOKnhOrA-Z8mzlh4z82K4GAC865HNIl39qKK8de19pP0v_XiXhIBp8S97xnwyWjI-13s6zP6Du9zQskjbcgiUf-Z9uOnxrt0niHST67m2VO59lrQzskrPmgTlI6-IIGxEJRFpYvWA-N8cKjy61v92PUgDRzeW3gJu0c642cnZEpSA4Kkdscx3hxPkAJXmXxme5kdtBSbVyTdKs3SJGUZpnigUeasdfyFF4WuRbU6by5ASF1vH4Dq-YzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب تیم منتخب هفته‌هشتم رقابت‌های لیگ از نگاه‌سایت‌متریکا براساس بیشترین نمره در هر پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31375" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB51KmheiSB7uxT-4CIlER3YR_G6KNMbU58hOfnAeN4EJDbVtvj47KlmzdJUEtMWEoAL8e7aQhpjh8LxIgsYigaoYNPXYyy7JTiDvzLVktUKFWQZUti8R7sK6IhQoqlu3UxX9b3iMAH4HChEGFUTS7sLTAISSSLsZHtKzTyEiHmud2sL2eQIhHMPZKXuGcJHJbgn90TJXp8t2K554PYsOeO9cGS9foh04dOx6fKlJdXrlvCLmyhcXTnaCpWEx3xFKB5Fqk26z_SjWJHNvFot1vTx9nLMevWQvfZuGauhxLyjHoaz194__4RMtARiurRj54mJI6JhqIt2CK3jhvQmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته ششم سری‌آ؛
تقابل شاگردان گاسپرینی و سسک فابرگاس در ایستگاه ششم برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31374" target="_blank">📅 16:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwij_VzuFrPs4tjydVjJnGHUzybHFFpFs43d5dkKr3iey56FGpm82wUJWqJk4qHEVWdCTV7wSesUmO_tNDRzXG7_WC27frL7K8xz7LX76KBYe6M9vGf-PDyRS954UHH4yjf7mmbMDlExgCP2-tgr8ACBOFRwYJGp2GhXP1tTpeaQXjtIvCFJ78mtl8wYuS1u7VKI-MTdTXhXJnzOpj15QblxEdasXpAYjrpPn7zRk2IU1138aOre-ufTGF9FU8RcOK3yxs22CeJfgpXz1Jdw9xgR4i0bYrc82VFLxFzGhtuyZBLL0EZAZiIKD87s-76vOQtRia-BdmfVGrPyI74zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهراب بختیاری زاده پیشنهاد حضور در کادرفنی استقلال رو به پژمان‌منتظری کاپیتان‌سابق‌آبی‌ها داده. منتظری گفته بزودی جواب این پیشنهاد رو میده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31373" target="_blank">📅 15:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSw4aXtgBLqUAJrWOsacK8yPgt0vje165gHIAUhj08yOPEpf1yTQ9XSXY_qmUPQq7lTwnVYI2JFD7Maibt4nppzZbVb9UGH9-8KF0K7LNL7K-Z0zLuk5pnO9dVEPSKFrLki0WNnm8UJLqctcLDx0KnBOVRjS3k_97Z0-0MytAmljZfgK307jvZUJuScYT78tEwiLLpWRBr0zSZ_YIRxuLv9eWILNwyAyHTYCx9BH__tAyFmR_I6G2gxs9H8sDjPJBU2MV0h7K5TOGvNY_-n7p7fS0oMMy_lGySzss5rk_kk8KiGn835-yDeCqGsJfeXonXSoYty8Vw8kYk1wg63QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31372" target="_blank">📅 15:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLwwgfTNoOrCen8PXoSV7vso5GgF9GO4BHY1aZDZcRMqcgya-zCMWqc5pVXBnSxfiVatJdvu8pgdE3_qQZEkF4PSgrht-hmniRw2JorNx9ZkKUqiNxTSZep525faXWrcK_CJB32GLuZU7vOCtCyVlKyUtG2GoZvvqeq8G_JsVrkxicq2AvV9Rzh_jEzQAPu5Q1_APjS9JxLaVyoSRXyKfvLb-3K3EIRFteHGhQa7E57vwi2MiY-KEQ5kWdSX82aZq-lDQENNZGcHSj3edvv_myc65vW29021_cl6V3jQak82vSYlZwAIsljTKFa66IPj4TYLw1vJ4OrCj4S6rJAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31371" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85d440852.mp4?token=Hi7mVSfRVqKDohsjKcao-AIB2cclGFEP03QfBDn2DJX5NAMiHx7tijYgKC4JfqkbGV5W3v5j5MuA9ss9ogMFoYC8irPxnRgQUds2FzozFhd8PD8vlTzmNvsXMYM3rBHx2pP20Qp-HHj9-I5kaZFiRFcdt306nQh3VNbkWURt4EiVCCXSDwKfxIdYao-F8H312KM6nfkBgwiQnTH_qWGCArlSBdAP_mzMnNQD7iWBks01UN6BJ9MB0uQLkxvMxeUCQmt-x9O1XLi1jYr710T_YUavOWBPHEBeXrNBsdQjqLNzmchwhUmU7RidfoNh8rU1bZEuwyiXSG3nXZZGHtYxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
ویدیویی از پاس‌ های تماشایی پل پوگبا در مستطیل‌سبزکه‌منجر به گلزنی هم‌تیمی هاش میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31370" target="_blank">📅 14:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdXdLhTtYOnrf9veyrGXVv5wfNsOffGksphVipQCZ1GLKRwwNNTDXBTIbLmjr-ZiKSMtrB38Hwgl-e0C_yvxmVAVXfXbwIz_HcXwJPB1BffgUbUUhIDy676suKxYh1zi4z-O5uJVQeEX9eI_OoL85M0ab9hJRaxkOhjRGW5uGAM6qoUz2V-McvRwrxH0G-S_O89JFFQ2FBqahtCXchknkZ4y2fuIWMCW2_-Kj1Zp7wuBQ5-BXjZrTgxw9MaRYZODoq--NKjPgK-33NWFFB9DDav98sp8Hi6FXSTTL81fw_XzXtkhOWEbjQbAHNHAG523jTyhC0QwHeCtOAiL5FJk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31369" target="_blank">📅 14:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3XmSRhTt7zzhuHzFPwVBXVH0chTYeQiK3JvTVc8pO1YJoAEk6US1vml3qpqGnn96xfO9jm0AJ-9c3iaDAUqwbjvdiE7K34rgJhI5Bly9tIouPM4fP3hhxExFf2zJ6dkT3QKiqb4B70q92_Zm0dccaTnzAdjKIYFfkNfSP76IamcmFIUd8LXHm2L4-zZS9jtRzXgDoHylQpeAg2wRgTyVgMCQJAC4kcOLiFcfpXi5YxqotQMxoy7IKeLsiMCI2DhTz39wTFT3XvaMMHWr24mJnA-D8T2Jag_JKCgcHa8gOryS0aE94tOYep9XK9HRSw7-mmMY4pTSvJOswlMxc9ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار شبکه DAZN ایتالیا و از طرفداران تیم آث میلان که گفته روسونری با روبن آموریم به جایی نخواهد رسید و باید او رو از این تیم کنار بزارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31368" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqS8lVc6NwANsXb1bm_kNVMDQVkoWvQ_ljtgJvab6pDcauP5Ujp2UufkdfXG4wOh4zkPhgmvlTSTz1P6_R6odWIuabCEvpqUFE9UjzpxVeFgdEwywRpdefFN6U5Mfwo5laUkfvMChnmhrgb3U6N47x-F0P_Gk3XHclbdl_D_-9q6oPyG-2WMDB-1gqhApWM3PRrDOv1B6qwtSqgkudKDIIUFkPVHrrVRxak30h8lZKbiZPmnYvFQAeWQwg-0DuNi2Mes7OnT0gaJr2kjU4bfQpfO0M3zIWw80nR_4tojGD3b0gYR_uIRtZyTWOyryxioFx3-5M26C8gjQKV7bM1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ساکت الهامی سرمربی پیکان قبل بازی با شمس آذر: من‌دیگه‌اون‌ادم‌سابق نیست و دیگه دست به زن ندارم. ساکت الهامی در بازی دیروز با شمس آذر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31367" target="_blank">📅 13:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv57vaI7ZRX1aVsI1qDse5wH3U1v_2Zn7nZ06sRJ2ijcbz2Ws2DuVvZ_5hWPvqDksId6yAZ7mtQ3o_-FmkJo0Jc0vd1d7ot5tjmBTAWr5e5OBb8HTphBjTD_Eh2iG8vnRSl4c8v5Nod-wQtcuGwVKRzmtOXzFWrr702-UgugP5lm1tzk3WO3Y2bgepCfta5DKojvG_XORUM5yLYsNLwimZ8pXMv3HmaUIvyTIqMR2lgNW4H-Wjqw4n7hQNvShsap_9YA-0nbmkt4dAtRSJWQ9_oj_nGRqPTtUdvjreZuZRzNpVwkIHJ0Uyt_b5AL66JbLvK5P2ichipCFT50Xf97cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31366" target="_blank">📅 13:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9b16df533.mp4?token=ugK86nQ-vyPdk7UVYmp5NKc2scdB_XRfv8T9H-dV8L808Vh95Zdm8g7zcMUytWvD-CDq-blOpMU1fj8kJ140FHnlIuIRgYLHSx_vONRwvllbuKeFpa_xfoazJppVM66eZePVsB1ILw3prXs3oTyDrgGjl6c1UKzhkGEr8PaUuqrAFv2bwGcWqDbhSohDGUwX37cPyskPg7zQWYHeeSAq0FQY7Ne1UgDjLL75SYsTyMig5UmBza_YVvxPZZmgPolvZ4kewb0ZI_OLVnN_RnfYxiZUmgvA8rJBDc9X5TDqUxcVN79NRVSrcBJ6GEAGSs6pX5g3SrdZbZKetWbbkFGkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31365" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b580b78a1.mp4?token=RUOdZMQDpyQpezmLRbQ1uj840Sjxkx3XY67avgDHDPSPyZ-eoSxxAUyU0idtx_N-ah8HBlJsEdQlV7TmpX0TnVKcr67Yw7ZDIa4vfiHjJTSrYPiegSb-XYh-NfW2FDaLtnMSDwrkoInwE1PUBNMPKuHb-reHc8kYKeiSZifG9TfJ8LZFJrtRyrsmODFMBOQL7gAyFqfOC0Af-j8FlUaUGWkAde3X2a4XrTDzDcFM5AV3Rv6DqNTkma07EVPGOv7YQ8ZdSxglPEXGWuqBrVSgestKmkoQmxPxXsbBMLIIuxcPu95y2fKPyeZE8_VRF5qyRgP9X__GwsyUtKe65v-4_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه سانسورشده از مصاحبه چند روزپیش رضا گلزار سوپر استار سینما و تلویریون با امیر قیاسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31364" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqsQ8PANR2B4wn7P69A3NJdK1IFtzvE6pWvMA2IOQj3lK4N3o8RbwkiZ9G4uXcF-rpAPncXzlvGs_50hGMfOXMRgzBn-kmgBCOMfm1CxLu0uP5Qff49CGIYFJbH4bjiIu74REQeN8F3eDyHTpCgc9PY0QSW3jTiDpZBxKsfz6StHNmveS98uR1RefXZCxzyWyBNTs9PR6yqbZBO5bYjM7IOUjkD2QvBFblReU3xJavNJ9dx3GDf-C0LPPllt8CHhjskb5Vb9mN2uqqo8v0Q4gc493KMW48CzkDY5thjua4v_6T20PBI13ikzZMM_av6qFe9yB15_HauRL626jH3B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31363" target="_blank">📅 12:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124cde064.mp4?token=eH-ZWdAIm2SrcE00NifBBXL6Af4Yhejt5JiWjxxQ8Li9skZvosnvTRrvB-CKgIuJ16MjmDavYYS8u44pmBz3HqzqjybEZ9IpDfCl_f_lrMHT3PUsqArXq_LmVVRHwfrCKJ-59FEEraA6Mc7CLrET54j1G2ISpLuhF907Z4J3N9Q8SsRwVGloFgVIPVy-YYFnUnPTrybrsuhtlmgHFxuPAtxGgkubBMsPAYFZEOCMRoJEnpjoOArTcks7uZPReDCsT8hUl4nOynZm5R6ihTCCjB5KisQ4AFAj1GcIlL33O7nKqRgpk_l7LzxevTnPFkcRCz1y8D9MYkV16wf8Kp8TBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31362" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=dqADlM70cR1OS56_3M_Vcunjq-fdrUHdD-YNIlOokj4r3VkGZHJB3zYlDzHrhws0GVWUwzASy_9p-jBa5oUeQO5NktTPhCpREADWpHDRGL4ebbmmWL7DikbJHwhxLub-LCJ9QZPOWrIXnZGCe-PO4_8WGn33ubP5pNHj6uWbSwE7hf6n6oI5h5wap0HLsLN0oX678xewIm3b__n86ozRSUKSIVvRHucLfVVF7xOeCfSxUS-4h65HPuUz2v93H5sJ7hK3BSuGm0hIY0qAOAi1cz8ipc1hZERR1fcq_EUSw9B96vDSPJ1EuM4T3V_Cw1-j6boHxyypwOsCHVPkDedtSFAnWteAkCI1F6NIC82WGxL5OdA2gcGglxyL4XLRK39t89TFdvEzrlV4QAoBt8sOYAsxhcvqA-0aeLnKPvSg0QrfxjcZYc89aHpbpEEm2GMbkEi9YaDTyib88yBoa3rWJ6avmAef87sHDNqO5SI-YT3fsHkdfPIlESCOf9YUwSc0xbSuUxAHA0-Gg9LWB5BAspfIkNwzY_o2Yv9k1aBkNuzkzzzP0zFnjww5fT6cDwlyvUEbwlHmpKFRFFNJmAfbGJLU93GrPyLL3ZNwczvf75hCsQYbhPM6VhINGtKrwHlhShiCP89-QNYYJZL7BqNikg0ys-JW1IF3kBsLYa8mGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230f3b6f7c.mp4?token=dqADlM70cR1OS56_3M_Vcunjq-fdrUHdD-YNIlOokj4r3VkGZHJB3zYlDzHrhws0GVWUwzASy_9p-jBa5oUeQO5NktTPhCpREADWpHDRGL4ebbmmWL7DikbJHwhxLub-LCJ9QZPOWrIXnZGCe-PO4_8WGn33ubP5pNHj6uWbSwE7hf6n6oI5h5wap0HLsLN0oX678xewIm3b__n86ozRSUKSIVvRHucLfVVF7xOeCfSxUS-4h65HPuUz2v93H5sJ7hK3BSuGm0hIY0qAOAi1cz8ipc1hZERR1fcq_EUSw9B96vDSPJ1EuM4T3V_Cw1-j6boHxyypwOsCHVPkDedtSFAnWteAkCI1F6NIC82WGxL5OdA2gcGglxyL4XLRK39t89TFdvEzrlV4QAoBt8sOYAsxhcvqA-0aeLnKPvSg0QrfxjcZYc89aHpbpEEm2GMbkEi9YaDTyib88yBoa3rWJ6avmAef87sHDNqO5SI-YT3fsHkdfPIlESCOf9YUwSc0xbSuUxAHA0-Gg9LWB5BAspfIkNwzY_o2Yv9k1aBkNuzkzzzP0zFnjww5fT6cDwlyvUEbwlHmpKFRFFNJmAfbGJLU93GrPyLL3ZNwczvf75hCsQYbhPM6VhINGtKrwHlhShiCP89-QNYYJZL7BqNikg0ys-JW1IF3kBsLYa8mGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌فوق‌العاده زیبا از جشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه شهر اهواز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31361" target="_blank">📅 12:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31360" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFGSjjgQYPQJa30EAR1mhtxrVlK2Hm4qH_veOhEZEltw6GhgY00MmJibk3NNNqYjmIAGJbYCzOMJpTw9exggze1ZAHvLFKCHKJsNazgiu6wXTQPz6Cxdxqx2eYhYN-w1F7xYD8wxLoUnvhQhCGiaF99BvUXFiN6qzIxX6c9UaPvLMHU6Hvt-wduucil6Ql4VxAQXshcDdfl3pkY7p7FGa2l863qL2-Td_s1jPByYP06Wnbc_ryx2PvTYrmIvrFk2zTQEJm7Fb8XvrFF7mBFQWgWM77xwS-JQIICQ56Mtt-_Wj9aLTB-xDViZ20u3BKsBAoau3qmf10LWCtCDMPXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس هیات‌مدیره استقلال: با علیرضا بیرانوند هیچ مذاکره‌ای نداشتیم اما درآینده هرچیزی ممکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31359" target="_blank">📅 11:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brqjCc11o80F6rrZQnIXIRB6T7gaoDAafn4WwmaGMrGBEdWL-_gXbq37kLmAjGH3dYLoHZvbFq5b1STcUXBFPsEHPNOJ52S62iBs747BbEH-DIx6xGnQya0nPLJi4ZK2lRClZXo-o9dO-hG-AI9jUQ8Em6x_M6KcyPPW5vqF0QE897OgAlLoUT8ETShZRDIx6dgxwrIXZOUyVxd0jWNcC-VnIzoUGjDotfiZq1mqZ8VXhGddVsofKg3eDLxG_l6GA47AK0GtsvVUdt__n3cpYP7eEfA9KhLmJoZcPRaMoE7LLij6Pt77HJXKssT2I-ChAb854Dmes_-LTWMSzk8Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31358" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz-R4MT0Zmdcx_0a4mmjYB08kZXyRlzUpPOJATEEcFkvI2jX1412DXcQBX-qIqDekgEBSSSHweTjfUDyZRxFPSFpwo5fsjhHZDCbCBMLOSQrdCBFrsravDy-TmA5uIP0LZpN_pjUKLVE1Ui0NCRZPwXpmyRo8TF4zCTNcrQDcxuKU05dwpoa516-f7qh_Bsyg-xS2LYWy-JZ0sQhZz3d5sCIPwoLwo_CEFFXO-asxGXS6ID6n2HbUoz-pJVNZs1GpsvX5vShiMlEhTZxenU2ruj4uryfjcP5DAVPTSeQ3CeKJZ-HktcFjSf5Yq--KYTIxEORTL9nlBpw_JapLvXJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSGVwhhNtISP6TA_Yv9saJyK00G6BDazDvV_d8YlUrEpIUd2-JCRJlpATtYEUfkCgHjWYE0ZtYxc6KiCrKhuG4tzCqVRHMI1F54p8TV7jjTaMomuOUiE3GARhlIC7LX-_Ic_WunNPoKIcXWdFXBkaRHhan0pQK2IkiCuL51s6S-p8e8B6m88a4X6I1DCzea4QMENRAN_yFqeVmAdtjRqMUkNdQ2HDERmtRZDDc0NZJV0jezNlPsu5Az5PgLF70CuXugYP7bTSBGVPrDafUmXoZS1asDF6cQy33Hgw1ItwdqjJdGbpzQ41g6B6x4FTy3L-jn5fP_q08liwTMcdm7crA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
دبل‌تماشایی‌ومحشر لیونل مسی فوق ستاره 39 ساله آرژانتینی اینترمیامی در بازی بامداد امروز این تیم در لیگ MLS؛ تعداد گل‌های لئو مسی در کل دوران‌حرفه‌ایش به 934 رسید و برای58امین بار از سوفااسکور نمره کامل 10 از 10 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31356" target="_blank">📅 09:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8qvwqYyEGgzLL26QWkzDPwCqy52WZ6-7tWw7TPVlsu97AS3VwTsEFq4A1JtWieVKj9CHLlsv_C3yhizYCD607qLSStIz9NM8VabEWyExtrVKLsw_m-zRDd49QlvgDrqW44X211t486cpfvJKwLKa1rnpHgiVwCOmWcBJKI7OSZ0leuiBT76n3X4HpbMXZwcW8aaUuX6pht7qJ7-ubgPKt0Ow_yC4JaXARP4J_sPs50QYtaw2Up5EDChSNF7fVit_esieBWlMxlmLpWuhxn40LlIAHkF21mktGyFSXwanfF1bd-B87A8wtmaAP6auj5OwVDBgmc6-tW-1UIDbyNvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بارسا فلیک تو این‌فصل: 9 بازی. 0 مساوی. 0 باخت. 9 برد. 39 گل زده. میانگین 4.3 گل در هر بازی. بهترین خط حمله دنیا. صدر جدول لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31355" target="_blank">📅 09:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa22c27bfb.mp4?token=aDr2jm2U-Gqg8Eu5GLPYGsGWgWXJXWtgM7HMhZ0gBTSjiWOx_vEbsNZwH1csLHc88X6Scp7SeEkcVCp3dTlgCbEpEBznsPiX4VWODH-d9h8bI-b7Ixog36IkjV6LUK3TB1IN-oPEoC3T-3Qe5pu8VmByyVXywEiCy40VoSIuNUovakMVYZMlixnqTJYrGrYgAPV_75RU0YfeqNCxxzAWKpMvqkWIa2Cmc4rJpICMhMoFp21ycynzlwoGolijT-hODbdpvCBkoSP9K0zJxtpPbEysgDJvWhSTBjGqmMyyVN8WC3UP4kmk64vaTA7mszG5n0BtyXMOUPKR_nPxSe1dUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31353" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uARpoEdfT2TN-2vn-E8TpA7VufnDdAAXGa1ixWEzBIQnTKSgsF93D66uaYqvHWoU3w6s2fxLym-N4VBi194RdvH6oa_gyAmrrT7F_kxWyWCO61y12Fj5Ep2bjrsGngqxYNphd3hrR3nSfN_JR-qnqo3yYPAA4rJ5RipS9slYRsyY9tSQqydf5QVi7y54Jpw1a6JtbqCv7JST218y3JVva0asYpF-Zn20m3tyhn9aV4XRXdWM9tVpGbO_oTgHGUEeFd1VqmouWLR9yRzdkF3aj8mQqm_TjDYgB1PKKgviRXLaVVBnEQunx--fixk18urqZFcmQIaI1ZWtImT1A8SB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31352" target="_blank">📅 08:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8zj70A_6nWf_2HyZzCpOuwZv6ZJhYJWOln2gK_Q1Y8UgqWalr_ytOHCHNihqQVQjNipaQqgkD7Vj6VyX-VxhC6Sw5grfmuaSPzLSiNgbhROI3_A69zp4JHbTpNsMYxMXdSLyWBGBJrpprbVwv3ICC2dU3U0q9JnnehEsmtmyXL3ItvLMDmNMzSaBhMkCCdfLUV-IcewLEQf1QGO9jPI3Ru4bVVHk8OhphEK6vwWPexrWDfIqHJJM-0CQGrcCJG5Lm5ktB00btf4pBGWzwFWRsxczWcmJVuHkZShkyR5FjChT23AnElguMc7ZlnQmck1KClk3OA9a80f_GLvnsYD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد خانگی بارسلونا و رئال مادرید تا دومین تساوی بایرنی‌ها در این فصل
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31351" target="_blank">📅 08:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOw5ihv2tbZ3LRVRNlij5Afspm5NCvvJUqKXjGlg_fxeZWI74QDbEwVsPdg0SgT7qV2ZeeZ5AzTR552zdrG5rHyffjqgbI1Cbdj4dzALORQeYxwdlXO0gUHx_7HYqIRSLeRLDMordM92FTliV0U863embXRlU7vXXMbOrSO7qBFcDtwEMYWUA2grM3_6mOAdQb0zV1nmG1lswFaaLUckWjcy2hgvDH2CaShI1CvbBRTr6av12n4L0H2zJvitUOuQz9hLJA6bQvHlpov4OXRkiYS_iOR479sIp1xXrQ80Z9Og-ugWsQzXz5xdycW18pKOPymA47so0d9JrmsW4rztfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31350" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjlswvNJA08FMHvKiV2hC5W2Wwrsr--7k2BioRlrR83UYnoXIDf5bOo7yJVKEkSEzYduaiyig76MFEQUs5isIYzMlsfff39JMP0-Ms3U9k8ilzvnDT1Ntq7ul6FYX3AlPv745UpipQAs-OgINwQheg7SH5JtEChqud3-cF92YtrdpPTTxljLs-NXNqy5au2ztRtIgaE3z1jd-XPNczi1xPtHb0wyEUzoteL2LMCzEP0PiXX19GQ6hILF8d830yNZ4a1Cno9u-kN561jf5sWaR7XGjth27F3kbgZJPmDxNse-n-V6aQ1q41l27O-RHTJZC2BqxY0QoUIUWCMDzQ1evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ پیروزی سخت شاگردان مورینیو در برنابئو با تک گل دیومانده؛ اختلااف 6 امتیازی با صدر حفظ شد. وینیسیوس ممکنه به خاطر کشیدن موی بازیکن ویارئال دو جلسه محروم بشه و الکلاسیکو رو از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31349" target="_blank">📅 00:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31347">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBSl0aridxtgGJ61Tp6kpwEVRkJgKq2akRGJOAc5X_y-aSEbYi_0ly3kLNAa2w39IUHzWPHHZq_1rfPND7eskHS26Jh8J55eItITY_-hlAMUc40MKolqrVusRjHFkQfxCetJU6sImcKSlsFA58iOXi738U0YGqi7Parn68iRCv6fuD4vZuwPafKAteyEPfOUO9uqeOb1TO4Bkpp4P64MvEYTm-09ij0Sxl_tq52KaI51DtHcZ9DpovvA2vvfC7kiAunqlLlcdDR-QFJsVzBDdkzv1JJG4CaqHtKroOQ7iD_PeZgLbymRJb_REL8eJD9qJgU_pejkGl3x_QeVNNDW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJe0hbjQOyCljhsJl0EMxrTjBIZv9gKegQagUNKyYXO6AhNqViMu6HY7Otf4eLmr57GayGFIERo3RjK898mIHoKYEAduLaiCpqQDpk7A9Li51E7OiuAS0brTKjQ-jwpCiu642E6F1eT7kEc7sVda5s50Yhsc_wtI6wKppv1RAH2eDlGtQ0okaJwJgQa9a-pWlNfVECRzpWRzn8cHiJl8_PFl7b30Z2pC9hrIIQ89c2PFZXZogA75UVmn87XFZuSEznDKDs2uXM9cH-TH6J9yAPpIxczQfK7djuzBH9wnpiovrGQUTkqQgsWW1sgkutbmbfXbpOpbLyLhpRxyYY9Kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
این‌بازیکن آدم بشو نیست؟! اخراج وینیسیوس به دلیل‌کشیدن مو سر بازیکن حریف؛ وینیسیوس که توانسته‌بود دروازه ویارئال رابازکنه با بازبینی صحنه به‌ثمررسیدن گل، ستاره رئال مادرید به‌دلیل کشیدن موی بازیکن حریف از زمین مسابقه اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31347" target="_blank">📅 00:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31346">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPYc5wEgA8pyr1AzLxStS_xFKdQVrcxM7-wNAXZAIcbLUqBsabVyc8gJVMTkAJ_D6d8vWQ-nmh4vxCu37zoh7hD4dppjFFOeDG-lXFDNVXv5L2z2bc-c39HyV7zHEACN3qKsROunnS265ZcfJk0PAqZeKwee1EFhr6kmf0Y6bzouGbk4qc-zbek4N1q0cDIPPwnY-43NEpZpLihiBwtIrZKS5sEXuYYQRUc0Ec9olemsyCNYLKpPAlcIs4yWzoeraFG1zDmVBLI7gzacFGom47ezjjo2--fGadF9WRaZs5oUs3IRVA6HNxucRvOdU4yYi-Eg1C5O4TmQ78dky-E1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31346" target="_blank">📅 00:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31345">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7d_8F873D22FTR5MsjGScirmierkq-x-seShaTJCbn2y4uGif2LAF_lJ6iq5K-tAGkSok0AB88SQVcl3wEJmsUOQTssM1pHmBdi5V84nX_yz2mSuUIxuYn7_XsLX32MkMTldoh22vsSvWw71drBG48b1SA_5lrhtmYHn_aZw0Nal2MtujjKE5Kx3wl9DJrO_NCGtNfoyPXzWP_BtAzZoHGPwek7boYpZn5gHmamC-gUPbieXV8AB2MDtTeUKiYqzcRVYBFFTU61Kmxzj4y-N6QDgxC55ZHiVBe1tVBQza-TYsn2f5mZMEx0ioGQwYFsT3x2DO8cLwPep4Q-zwr5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31345" target="_blank">📅 00:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31344">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNzj9ZOPvwWNnBoTATxzksWN0rkZe0odskkVtx4ru3i9oyf0MFRRH5PMcnCVe3TVl0Q7YkszfiuBoFaRHYO36ju3fzdF-3lQ9_cRds-PAzYr_PCbTC-zhmgiXADTCLHC62eCosTBZh7lkzIsDsrne8IjE6108tkL0f3kI13bIn_bg6aeGlgsqqLly1zcYnYCbESQmg5qfmhJLSbUcLPWzbppnboqCpHGDN8wzg2h4fJ-t6K9qUgq6wUsrH3iImnvm-YftCKz4_y3y5LBsy174kc_D--SITrdD7xULk0DM-54GUDjyt0XmGAH-Xch82-Hpy7gd5FxjADKmoxWWkmvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31344" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31343">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
👤
برسی عملکرد پرسپولیسِ مهدی تارتار بعد از انجام هفت مسابقه در فصل جدید: پنج پیروزی، یک مساوی، یک‌شکست، پانزده گل‌زده، چهار گل‌خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31343" target="_blank">📅 23:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31342">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zps2fYD8w0o6QA3d6wV7AL3aCTj3g6PwWg3lmriHoY0hF-digFNnTeNvtpKdBJVfEwQ8TS1bB5u8p1kiSOVOfRUT5WaYyMB83H-KZhNQMuHBicYfnbFYxCrtAZ3cTffTicMT-XcOpUWki4D7z3-_Ugn01SAHNPPS6Es4wdOOjj-fGniJopdidYv8dpS8VBRtbR5zdsSgFV5XdV68UK9-Nb28_zwp8iJ1C0DPGWJ9VQWuFrsrX6_DotZ5kn7cMNZv2GjyUP9JAy_h9M_vJz9wslXghkW9FQENO_QNuzeBfCh4YaJeBSeely7URzPGacOdDOMq1R2cSiAHPyPxTOhsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31342" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=ZDyLb8jieMSPxqA_TuLSRNxgrnH6jn97nghdLN5Ya5Lu7f08HWGIOkAvoMKoRZPyrrQW-mkwTwlAM-LlK1t01WcaJo8V-ebl-hPGi_ZaIYsx5I0nPBXu7-YIjMr_8fDlXXR0aXzLdtsuOrjMoXJqRZTBcPpDP4l4XSKDCvqemxNT2o3Rz5msvEx9EvlKIbEGri5RfIJUTv0TNyzDPtKnCQLPfWYwZQxOo3EfkWN6Av1EpPSoXZEeP55DUAMcQ1aZRnA7tE8FbXIyv0d-New36ugaqwpEvUPVvNnlireTL2ZFPqQf8Pbz6B-bAVOrbs7FSZ4jg38-W0tHOEa9kaabRD2eg7iszWQRMZ9dLR4k2IsA8EAa13H6wOAra_xeZFTBfTKnGIIF-aJHUnE1xlnRtoYGD9MAAu3Sp680BUkzhtHvwOv3MzhKfCLAwtBHgYwwlBhaGNZjNz8BLdnmotDv3QQh3T_i34wMSC22Bid-WdJzUl2Jewh3dpQe74UkVbmF0d5cyx-qodVVgPjmHhnM3pIVHn3FAy9n14q693Dp5UOyv2te97Mqomln7fNVnXId2D7vk-HpsbFG6x1OxlQd78nJIyC47Ay1K3Ely-wQ1SYpVULmSR6GvzfHadAR6pnD0PMJUoIW739eLZ6rjy7RVh_0kTFNbehaQ33peMeP2fU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ece2dc9b.mp4?token=ZDyLb8jieMSPxqA_TuLSRNxgrnH6jn97nghdLN5Ya5Lu7f08HWGIOkAvoMKoRZPyrrQW-mkwTwlAM-LlK1t01WcaJo8V-ebl-hPGi_ZaIYsx5I0nPBXu7-YIjMr_8fDlXXR0aXzLdtsuOrjMoXJqRZTBcPpDP4l4XSKDCvqemxNT2o3Rz5msvEx9EvlKIbEGri5RfIJUTv0TNyzDPtKnCQLPfWYwZQxOo3EfkWN6Av1EpPSoXZEeP55DUAMcQ1aZRnA7tE8FbXIyv0d-New36ugaqwpEvUPVvNnlireTL2ZFPqQf8Pbz6B-bAVOrbs7FSZ4jg38-W0tHOEa9kaabRD2eg7iszWQRMZ9dLR4k2IsA8EAa13H6wOAra_xeZFTBfTKnGIIF-aJHUnE1xlnRtoYGD9MAAu3Sp680BUkzhtHvwOv3MzhKfCLAwtBHgYwwlBhaGNZjNz8BLdnmotDv3QQh3T_i34wMSC22Bid-WdJzUl2Jewh3dpQe74UkVbmF0d5cyx-qodVVgPjmHhnM3pIVHn3FAy9n14q693Dp5UOyv2te97Mqomln7fNVnXId2D7vk-HpsbFG6x1OxlQd78nJIyC47Ay1K3Ely-wQ1SYpVULmSR6GvzfHadAR6pnD0PMJUoIW739eLZ6rjy7RVh_0kTFNbehaQ33peMeP2fU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31341" target="_blank">📅 22:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31340">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇪🇸
👤
نتیجه دو مسابقه مهم امشب؛ هشتمین پیروزی پیاپی و ارزشمند شاگردان هانسی فلیک در لالیگا و تثبیت صدر نشینی و توقف شیاطین سرخ مقابل شاگردان دی‌زربی. مایکل کریک در آستانه برکناری از هدایت منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31340" target="_blank">📅 22:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOvdQETtxE9cDN8lJcAJLLGha64zmb-D1nFFH0u57khkQshhs-efD8YUoYhAQ-altnYHIeB8oZhsMwmutPwGIptv2D2exBMlfpbvPqRiafLCKi2dn_DQj2Fd65nX5crsjGznNOEqjy-DeLSiCD38L_oM8YOW3n6UuRJ4mz0Ul0qbH5Ow_C3lalMHED9quVwZjLwibZAVGMqiTVIM6nqxf-LhUvptjMrRF7DAcit1xdhcdHEKwO8Kc_WAaXC4sQ8oQmIWhuk0jO0cvnSSEg_IlW08ujtM5N_vsCBVeQLHkhRv6mPRVhveNS7_yAnehCIDOmk2H1XEQgAxJbOv3p67MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vv4alKHNZBumTTJnhbWH0f5ZbontEpMi45glwiDr2ChAG7WqhDi49YWUpH6OAcWerxM6yHKPb6samI9cnhKXpVKkbXK-IcqqZa62CI64hztjOmWDUhQ2m-0VSGlhRrTNjyhuoEPUhuAvDzjlZiDC9dmc-Z-5GZ5Vczj3IuMekTPFOl0VN0ft8i9q8EyPQ3zBc1abZUTHr9Wmoqrjv0iDlt4shd4aXhuUbXYnQV7swpiXkPfq2K-znRd1dYR45GtvBUZl4js-p9PJg183K26Ntq1sAocfVN9R6HLrpwnJix3tKQ2D1GgoudskqTAa7ZIChpfnJHvrgkgbRTft3YZOFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امشب مقابل ختافه؛ ساعت 20:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31338" target="_blank">📅 22:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31334">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2WvhytNfkklNmlDuBMESoG_iVqXYcIdO36CNnuNTF7KP4QSeTrIvDM8-uqDX6AaZ9VNVQHz4Y9GFrlYzYKCDm3rtW481ZD1cReepxLJGD-wrKY-BW7tix6bnRy61CbgL21Ws_wcE08VBCPiSE8rU4RIt6vNlj7mPCnJzgoxj4MQWlCcqEg47KE3Ifs_EH9j0bRs_UihoXCPjrmA7wlxLpvZE5kVkP64rU83onuyYlsPIza8_B11HYMDAMs_8nWKsCuATIHAMSe36w9bDIqt8TDUBJRwcBm3zrpPoUyzklg-kb3NBJmTw06Gjj05BcVg_NGe3vbLaiHfZXmSLxFuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfmhdcWFyapLyOn5HVEYMYNg-b3J6QhsWQ3ASSgpip_u-PUkKjfBdYB10F-nIp-g20Bi4A0Gyu5nSPPnOqfq-ArNRwPcISLfjo1vSNqmTd-BOsiVbhZGII6rDljtHHHtdp16nCIkwLqRi_xPuv78dANmEY1Ki7mGChGjfmTJGGKFuZizzjwgYERdqq6fTTpaYIuT2Qa-j7K6scUy3XunG5pWEef9X3wJX-4uoVFbRVvIymaNOQ6m3qiIKHuTABFCm6gPDNcOzyx8NT1NPiJGQ9F3V1KJ4aWIf7cycrJCjXcYNb0SNAGickrNsm7ES_yLoTIELVVwvRfP9GXFrYAFRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته هشتم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31334" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf77-Lj6BxgkoBmJdtpqXwWuQWIjnXaL2LsC7u6pBKSuEaXcyjyVj1NzhWxtQ6-iK22L4LrjZk4e_KsggprEzSCPyFeGL4MYnyjClxSIbfP99EXor9AAvN2l1HXuHFTaXy5fWCZwvsL3zejF5Sjr34bdSqEYrO_gDVeTNw1ZLjydHkhkw8Ypcy0ryErgTYeHKDGoevHP3wn43zUeDficEsstEZgvlDGSxuwGsPeStA4mXotrIkfm_1V1L4bDje1qxM87YNFXUhWhYHBI4mrlU7ikD00Rc6hs3QE3r7Yk2-PiVtRVTDATp0XJMtBcEMRs1xtCBNeSLbCvhWwwvrXT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسول‌خطیبی‌سومین‌سرمربی اخراجی فصل جدید؛ بعدِ شکست‌سنگین فجر مقابل سپاهان مدیران این باشگاه با رسول خطیبی قطع همکاری کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31333" target="_blank">📅 21:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUAq37h8I-COeNHiC8Sj2qzb8ekq6JXB_Hw0LhfRWd4_7wUQRCxIq6P6AWSygGfAUPLSIr94L1YMHl1e6lS1QCBiUjvLOYt2cKL8CZmlkHZCOsi4AenL8_3z5QmSSe0GIYMvdIi4IZ_paTzI0IpvyX0ivzALOeYaBFj41bBcm8dKj_4cvr9CuWNIaWb_lzn5WRosDRGqlXbS5Z0OTEAkWmDBLhEkrybqX7aEGUNQQPMELYSiT3YQk4Ew-blTJapQtcIZCQdbx1WCyDInDDDex9S_l9uy51lceUf2B04Fgn-dkoStKBK1R168tL3PbIOyumz3ynTY_gd8DweHbj90IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هشتم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل ویارئال؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31332" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=C8r6os4CE2LXtacymEmByCAbLnIPAFbaoe0UVhx7nGYuuN-vdXlxh0r2Mhdu4fiP1jZ-Ky9g8uzzmc0JJ_q0rh7q9ZYiaLfayPY74XOE6T33PGkDWLbxkzeWeYJnfvXPGQBaUSTVW_j3YfiWUU-JTToc0Qw8ltoWkejxIfcAlU72vVQ5rc7pA1MAtlVE-m7Lrf-1zKWbTw_8ReWzIBIVU_oC7kJiue-AsGtw4HZiGKEcQ48Cd_OGSLbuzcfDQpdIj3S-a2nPfUZIR_t84HwZXmKGSy0LrnEHsi-avkTNlo9zB-xU-kaQVrhsQdpI0MsCKSAmT7FlMTTr2HZj3_gcwyRyNMXKhlLWtmag_L517Kv5L1axOLnUrfWn8idkaA8UEf7RlcKGyksIgX3tf65-Tf4pOteZ5qKRLt5smP1YoOkdqmGeVUJeIiALRYC2himzoZEly44Bm5iJAM1RlYZ3irj58NbUpr1LdRy6PQsrgAUOY79TbxBAg-DP5drW3IRSg4Pl6i2fZr5z0W6jNmY-2hXPUHkjznFrMUhwHz1i-eVAlBMb3Eqkic_BDh8Ezwak2UdJa11v_HrXX3jukqNOfwJfZ3HZwtD9Ek4UsrGZD_RNoYnIBX7HzpvYN3qNOEcepVNq_6l8nG5UXq4kKjhjOJffCb7U9NwH67T1brY35l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd28a51cb.mp4?token=C8r6os4CE2LXtacymEmByCAbLnIPAFbaoe0UVhx7nGYuuN-vdXlxh0r2Mhdu4fiP1jZ-Ky9g8uzzmc0JJ_q0rh7q9ZYiaLfayPY74XOE6T33PGkDWLbxkzeWeYJnfvXPGQBaUSTVW_j3YfiWUU-JTToc0Qw8ltoWkejxIfcAlU72vVQ5rc7pA1MAtlVE-m7Lrf-1zKWbTw_8ReWzIBIVU_oC7kJiue-AsGtw4HZiGKEcQ48Cd_OGSLbuzcfDQpdIj3S-a2nPfUZIR_t84HwZXmKGSy0LrnEHsi-avkTNlo9zB-xU-kaQVrhsQdpI0MsCKSAmT7FlMTTr2HZj3_gcwyRyNMXKhlLWtmag_L517Kv5L1axOLnUrfWn8idkaA8UEf7RlcKGyksIgX3tf65-Tf4pOteZ5qKRLt5smP1YoOkdqmGeVUJeIiALRYC2himzoZEly44Bm5iJAM1RlYZ3irj58NbUpr1LdRy6PQsrgAUOY79TbxBAg-DP5drW3IRSg4Pl6i2fZr5z0W6jNmY-2hXPUHkjznFrMUhwHz1i-eVAlBMb3Eqkic_BDh8Ezwak2UdJa11v_HrXX3jukqNOfwJfZ3HZwtD9Ek4UsrGZD_RNoYnIBX7HzpvYN3qNOEcepVNq_6l8nG5UXq4kKjhjOJffCb7U9NwH67T1brY35l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت مؤدب‌ترین و باشخصیت ترین مرد تاریخ فوتبال ایران ازسفر۱۸ساعته کاروان تراکتور از تبریز به عمان به دلیل محاصره هوایی ایران: پنج بار فقط سگ ما رو گشته. اینجا هم فک کنم صف روغنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31331" target="_blank">📅 21:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAcs6O2DKS9H2QiuedigjigK3i2k5W9hrfA7iXnHVw0W0WY-ptT7T9945ch-0_p6OMl0PVKaDosJpHtVRAixBTMZEYe6zKuQJDdFoxXzE-9jclmsmR0WxSh7bxxacYbPCCY4vdGgx-RbXy_-P31xXUZYJeZWoaKaIGiqbyUojm29KrszaKf0_UQPJwD7tophNfQhWujbEHHKmzkb4jTsNvIWjKK_thNvek3KTSRrU8KYTswpVenyuDHqdWPcpI6BCAKfvmAIBRWoYyDMtE5n7K48CU25iTnZ-yC0LOej1jpLHs_FjUgzUiOiYAHNsj6WPoy9K7WtoSuuYsTwryCEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-zQP8VT8JjP2vfl5w58pQfWaygFuAZP4NEleKOen-hVAKS0vzbmF91j-p2I1xjTI3ylSPqRqYJBeyG1-jGTXhe9iACYZt0MFSBbCZccKyYvWUrFPiO7_Ykhs7uhueAbroYIBw6qtVyePU11rhyLdZTy7PaG4-kIG_qb7e0JjANaV8asHPoTv8j12bVVMXknsNIus74p0Bw-cPaM9IyrcwQQcj6YcIr3WfRSfLeey-UKw0LI2mZu2nf1YAssJD3bimQQI9eD9nfsDfXXytEPdASKnSp8iOUimxRSJRSACCT9ZPwNLFFN3BP-WRTlqECGwfkUxPc4jmesYgBIq1knlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kw7T75zGyR7oZ0aJmiCHpNFe9j8ajc-b9vEY15dff7XtONrA6WeUswKKsj0yRHC336XWVsZ91FvkTYJ9TP4DFvAgzWrTAzo4DsqCkbvy_NyiGBFwX8u_xVU7fmT2z4aDIkBRH4ifrYktrexcVXNxGCnjWww9A3bBSFpzL-PpEdBSm42NGoUF5GoVG3seCPD5rBR0pQOyOJSJsxLOHjiiTacHsxU899oGkJm90D0jZC_sSMswm5tecy06G2fu0opCSvMnD6E7zyrYhBNzCc2ykjKJe2KX9UGT2kqwBfGaF1uq-qGNsxsskBhlpvSyqxrG0yxcjk9BYfgMkT-a1p_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGZx19T0BIgRvpK6kVlH333ahpUjcVWKJA1iHZU5YZGB1yuY1MV3zcvZemWNRJCia_rUPiJS4eMCvHToMsX987Q7K_9ra0msN2lhG4yBAk_kZuo6fyGzDFfKYkB73JoivF4S1TF38XP6S8tiBLhXV_QoiO2Dkxtf2KEMbRAjigdK9PxjWswVCPchz6fBIEdX1TnZC_U7uV30B1wYurxdTB4OvRwahzM8YeirKpDxjHKohW1LAA136V7GHeiirrrINwNNQjVsKxvuOPgntjVsTrWKzw-6wstN32bXLkE11Kdnez0VgqdPy6vjrC2F8IxtV8a7WhJLUCkTCAbX6TbfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU83SQu5K8hf_4f9ouB_XKeQznKckFqVUkioPdvy3_91t-YgbknAMIz-wKJWektz-_wBtvbFYPxPGD-TOW7Owmr4asyQtS2_g0GvhL9rOWN7MbeAwQy5LEZzkRrLN-OC4p579l_h3fW1PDx52L0dP9U1MfePSlRHX-czLCYEfwLBZWkQESYowS7oI7eg4Y4k9C-YLIU13OIJAS6sNWDbifCFRRgmxd-kKnBMqfjSNOdr4qBXfUTim9C9a2tftpTFKt7YIWz9kRMlBlzrliYG7eGK712kSC6g6FWhVIurSGXqnaEuESDaOe5GLsrZQu1PEV11gw_ZI322Gt9ulH5VSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOpl3WKDOUXLSlNFLDz4YfiCTMC_RGoy_fF_xAWWzJuCE6DIqP_Z1Ub8GsYnkfyKt5IBO-p0FJRDqCJf33lp9EYLM_a6PgTdmndyZP2lymAB1P6t9f_MIp054vZ9Iq1FGPy7fKqV4o0QFsgVBlTJaDBPqCxh5nnbwzs7JqGrkAjQHvNDHX0mW4Oy-oarimp_FUT8jn7MYtrhQN49RRbvT_G3MwRz_kadnszAr9D_Mp3E9qzcoRmBiv3EXI_pJ5UbUxpB7RYxxbwbE6F6_VMhn7sByCj_fnDzPjfI1m_HqXyh58xj3vXLPyANM2zLDrSLzCpA8PGHszrqXOT3apwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=oIzoyfZx6GCtsTpWz4P86HFl8YvfsdYHk19cpiZkUReSDOKHu6EMKamWaeLuHDlqI6B45iAv0ipLUp5fleOrhaWz7JIqwCb5rUoZyk6BG1-TlsN7zkwzJBll6qmAFus1bSpzxy18AnI0CnqGYrNpL-GCDkv8TfBWKV_4gn0opk6jMmpJ8PlwXQZEFtJYevJ25nnEb0Zkjl8B1C_VcKFYqvPtW0XH1dP0-Qrde9RFO-thlpP5xbw_oje1lFmP3GkEroo2dn4fL7_1v3rOzfFckeitWyk8-Ibf1tgYZZIo0TdHvUJp_eCu9mogZ03X4eW2gqWMNODp-PNjwN_0_6_rqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=oIzoyfZx6GCtsTpWz4P86HFl8YvfsdYHk19cpiZkUReSDOKHu6EMKamWaeLuHDlqI6B45iAv0ipLUp5fleOrhaWz7JIqwCb5rUoZyk6BG1-TlsN7zkwzJBll6qmAFus1bSpzxy18AnI0CnqGYrNpL-GCDkv8TfBWKV_4gn0opk6jMmpJ8PlwXQZEFtJYevJ25nnEb0Zkjl8B1C_VcKFYqvPtW0XH1dP0-Qrde9RFO-thlpP5xbw_oje1lFmP3GkEroo2dn4fL7_1v3rOzfFckeitWyk8-Ibf1tgYZZIo0TdHvUJp_eCu9mogZ03X4eW2gqWMNODp-PNjwN_0_6_rqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiyguPnSvMQBp1sOl7QYh1eDRtFfqzbZZ4_VRZ2_6XzByQeQAgMObTE6C_1wJykQePyxww4Mf-N9Ps7GXSu0OiMWzmyE7X3X6JnvN3Qle9-KdUfQfwkOB4QgSod9XrvcYRUvJ5cOTn3NvB-u4BuCnYZ83ks3G6mCpln4r1PEg5RkE2rDXRf8SJ_EmgC5Ae6cttqznPGkWi7yugRNMz7zS-MAQn3bUlulCBQ4Do2UYk0gj2F6lVeusCJ9l-iDik5byfaDkspZiv1SnpJVpYIwn3S49l4ZOalnk6IYiEj_w3F5oKZUEMicp8-czGYL-0HLmvE3Ot4ffnDAyo2mXXbEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCfjXBfzOqEfgpOYG30TM4ExTfUZHd260IQ7dY72-vTj5_1m1zdP1Lbbep90onGYjA0ijTk4Xxqs-mnAp6SByN_2vw7J7QDZ7FK1y61iSwqz-KqXm-D4fDrbv8DVegiDjL-wGaqkothHp3vVIe5mnML6S5y55-wOirnFdP2mYbnt7RmVTKth_oWfvj-MjJlWYDj_S0Rkl-aqWOPn6VGfckydG4dek96Uc6tZksViHEXciy7gRbb-ungMx33fkS0jDfEHnUkhRPtHqpiO61zieNxcVuSzRGmF663fkW9Jdyblv2E-_8YZzvzx1i5YUNQzwXfrfeCe6T0Bci1SzgChBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=gFedebBb0oFEwEPjbZoB8RQcnoNet9wqPcaBe4XYv2aMPPV1pQ31kfF0fkD1Qs0-vTh1JlSkJHlMTuRZIxx4jswikIKqoCuHMo_hSO87aNPHoZIc87Z17aLS_cMwb3K3Qq6NA5z5b-ZUvZFV-h4pQAESCQXGXZC9YTArgRgH4n_cQ5rm3tsLM4eyV5WWAZX4leUJGNKTtowdaranzJHs8hmAidzNi7XnOO48RLNZpcksN5imz6xegVA0MY_hGKapgFHvpIBtJsMUjUv60F7adB1_zskIMddbiCVLEbQJIjmschAWHN8b0Q_neClAbfIPGjLjO1M1Yq54pxa3y_ZAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=gFedebBb0oFEwEPjbZoB8RQcnoNet9wqPcaBe4XYv2aMPPV1pQ31kfF0fkD1Qs0-vTh1JlSkJHlMTuRZIxx4jswikIKqoCuHMo_hSO87aNPHoZIc87Z17aLS_cMwb3K3Qq6NA5z5b-ZUvZFV-h4pQAESCQXGXZC9YTArgRgH4n_cQ5rm3tsLM4eyV5WWAZX4leUJGNKTtowdaranzJHs8hmAidzNi7XnOO48RLNZpcksN5imz6xegVA0MY_hGKapgFHvpIBtJsMUjUv60F7adB1_zskIMddbiCVLEbQJIjmschAWHN8b0Q_neClAbfIPGjLjO1M1Yq54pxa3y_ZAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=Asr6i41r9pyCB5XO5fCzxV0DTfVGY_D0UanPVn3kJGXB5wzqV4gxiMp5OVLj3ChXz-Yy-S2v4nFdcC5LEIC3p2SiSdp7TDWJUIcUKmQ8-ZMLEm-gI-EVwKY3dQMmKh_hKraLPIZ20uf1ATJxjtvOkVw475B40wR2_XjjYpJ6cXOTwjzMC_naOM8H4JgjDhkHOFcFSKA2Rx47xganzr1Rb724rFTvUtux87Jq-i0zl5k34KL4axTbS3FXrMYb13SfI2EMAFmcLTM90wX_GxyG9JKZuuVi-pPni_BwMLRWxCVXqLPHShA51imsm9s5Fx3ET_HcGkNnLLRc79rTtQ3h5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=Asr6i41r9pyCB5XO5fCzxV0DTfVGY_D0UanPVn3kJGXB5wzqV4gxiMp5OVLj3ChXz-Yy-S2v4nFdcC5LEIC3p2SiSdp7TDWJUIcUKmQ8-ZMLEm-gI-EVwKY3dQMmKh_hKraLPIZ20uf1ATJxjtvOkVw475B40wR2_XjjYpJ6cXOTwjzMC_naOM8H4JgjDhkHOFcFSKA2Rx47xganzr1Rb724rFTvUtux87Jq-i0zl5k34KL4axTbS3FXrMYb13SfI2EMAFmcLTM90wX_GxyG9JKZuuVi-pPni_BwMLRWxCVXqLPHShA51imsm9s5Fx3ET_HcGkNnLLRc79rTtQ3h5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMASR5b1_bWcALLWqNQp9fML98EX7Ee0g3l63AGds1EVY2IYBo6JZA2E6OZXSqV5TbyfJNbSf9qkrL8J8r6fp9QmtHJLFwi4oNpjPqrIF4b1EH0hMfWlv27fQPzpl0HSbIj2CuE5Yk8qC5UCTKPbN1qWpdosA4ThcncmUKSu3KkLFv8hrKII5RPZzdUJI2Dw3qUnAe0dHvGP1pNenz_QoIQjjC4_6oOKhIAqalYrYuR0yUY0IsPktP5WgUAIF1bUFojufBd8Jx0pwoHLldepaB3PXW7VpBfEkPDTczKaihTvA5CPLzakoy1lvAviFU9-_B1EnpfSRinD0dpvLG28rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgFXHKTdPuo72Ip7-b6AyAAWbqcD7o_JpkpZ76jPt6CLdTapCBQFAd5q-ZfhlwMPPaw_KKX7ZUMIy4h05lZ5SfP-uxGqKbNpgMwsB5XcNpUTSQx-0CSkss3w4o0uCMelSvtTiuhzyIYQ-lJ4y43-iu_-uUgyxGojC1amqY8dB2vdqoOGBbCWcoqUcZBMqf7xspQoPqyzsdUIlV9BrjfjR20xhoeCcLcFKHF4yaVon3gGMpnJTKFNL6_FDYby6VDDfLMtMMip7HR4s8pjMHlJ7hN5yP62DY3Ws6jFgOAi1CuYQ49SN3t2S2qPs3ZlRbF0HJpjsmcAMLrfTcJNBQkIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJFQxRfzfxqwt3TEm_R0zhDgwfHOlGeCvQbmKLMoWssZw4Yemm2x9M19Fn5dCpTqeSeklwyWlM-uGpRQkUNmdOFJ0xAZHdYoqJNaWKgQiPv-Ts89lN_60hyqD-WX7N0b6cSVXRAn1_fJ6Al5xvzjkT7zNBxgf2oW2iRi7hyDCYREthmkLLUWl4UfSx_oPlCyBZa-84_epllWTNFfq8JQMyLN-xdJJwBxWkrUvo2UIq0qK4TY1eaRqLXKGgkxGkNzbPq-ljRWqyzxiOooZYhmC1zG1iFA0rieGgu3wxk7d6-u6oGNhBqi6h1Zv-Ml9WmG3e88MQE8BEyXzbM6Hb0BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqVaT0cHJ7TFn0GmYX1dIK2mI7Oy4yt_Sjmf9-DNDP2qgnJNhpN64HL-qyfAYuZ2cHMXrVKd-ei1M5LWXSabuaPQuTUGgkz8xv0DEsIWfIamBhckXQruDzs8T3T0SZQSOhCOUtc_5VKjBoTBGaYGvASfM2jnPo7Voklefdwd437m0X1VYYV0ARkvPeAvXyyE6uLYdkdmedZ2sVCMSbbKY6dFwjOEoM7rSO6IXpgTbOprRT93Lg87x8QzqVC7kvIMocGHmPCEbgzPLbOn7W8FOBV1PKE8qTQoD2jTLCiLRG7Qp0suA2u4LzOU1wVltAuwvT3f_syPu1lJPr9r8a4oEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN5mn86ZzBzaYqOP6FnvSYIiPTk36eB16Y3diuNArehF_GN64NHeqlIDyQqrTAbhxE-RrPrfb7z8NFSMbRBmBonPFyjruGYpVryugItbrDlZermZoOYfkbZDlM68CpHmvtE0QzUgZN-nw3bPL0fPyDcphsPyHL7QN3H8lfU9kxfwMqq2Xl0S2ELCbc5MHGlm84eqOMTMFwUqihmNjZGdX4Yxbb_OPIyHKCecOCXbzIbS6PxwsWrsCP75A23CCCjwgXeoGrdUmz0sLjo7pjw-JM7u5uc8PObWnwQGUgZwEK7KsjRcVh5PluDXT_qF5TajbXR7RxUqy2M1t6FTlW-Kaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZllcpRrpOhJr2h-QYEcztVRYnGqMBEGOqbQ-GOmok1zByF_dr0MnGL_brZK3HoJEoxdofJiXt7ftZGIgGDnRYcmBWZu93Hy6b_v67kCjA2H0bFyP_3-jC1j4q5Bh5GdVz_Hiq02hIuRPVIwVVw4COnEQxQBung1CkDXhV4nDJpYsMKjpjeIaxEq_mLFqESPTIV43Ch1dOKrXRho5LHjwDjjCuyzfMbmZxr5MN2baS6rkthjykIbVq7xPEKa5l17LEHcCOMfMUBDfPpwKNXV6qqbc_4YUQYUWwH0xSahUBOLwxHhLAZTBHPn8jYj0XXOi0BtuCc-n31yPfJhbL6nc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uerSx3c02RAbPnbQeumzy8cVS5PBRvF_Ynb26r9mYhlcvK5BSzLXdy7LENHozkiMeL8EG9NLdTx1mABgfGsuKj8dSEGzQinMynqmJklNYG1ST0U3Vycjjms73taZsVN3nPrenHyHHUkIubiSKJx4h9mkDeRB-X8dFGN6ykg4kKEDkmr-Z6by6W6Bz_PhzMUOb0DKBAYrq5sZq7mf_M_h7LCgic3218E-yJjmiItZ32AwA1pWWF7EoLyJXBnuVBM0uf2YAGk_GlJIFrfpLUKSNMSD5PH7WhzcYceSAi8j0TjBj78brpAfOSnkMrR0WU_7r4Kv8CE7_MOGIoi2F5zlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsdtWRucPRScphFjPjc9pFzqwso6M4DBnKFbxcT6ZovMY0mbr91x_2ZLKrTt9UOvk3JNXsZSE_xfXv3PuPxX1UCCgtBXLAeYwgoJ0n8TNKfKGNcXNLsDt-k_0zuWBiS7t99E1me_765IiEjf5X_vibQinPB7fPXzsspTqJLIS0Pc-lPyGk7bKBcqDRoKP-briN9giw0OMCS-07pcEjfnwM4bvPBs2buIpSg_Sp943PHgnVGDCY2-WoBxbAX_r2Koxd5uO5yZz_mH57kxtyvhB8L3lz9cXEs7S4UNpl4BE8xpXyqIGCrT2JfVBn-ZEA-7SBj_FJxinL4kGYr6xvSK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6sOWxOzYwyYuwz2_vasMmCFy21zrtq44UPgkS3VY6noPk5J6892cg5VLigoa7r_sn2hFhwnGkDZkUmBS2lGK4iRZZHvYgYcSJaSc6wgzMPZ2L5bNkdzOFOyitEEowTD_FkJQd-i7fTjUupKUtycn_nFru2-5f56WitCMSIE_CqYlqmMm2I3aIMbdlLhmx6eQT4wuwow1IvSs48zPKJXH24-IuOWiNrRYprrV-dlE_xy_XaiB3kfXLt8BN5-mlZt6zxDigZGLcbf3KpD9GXu6U0EK0ho_tia5R-iBNsmRVOgcIsZdm9omlScTHULhOt1xDqH7qF66pyTAeUPLGNoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvqLmfX2LvJYIQjw0Nlfei07n-9KQgdgmIG47FXE4x53f6U2DXRDkcdECZYb4papGGYBxG7hSlrUJJLDSWc17Oy_C4rDZPlnEZYKThtmRgQYWOko5E_LXgOUjGXsEJY45ODI0W6YbuVHtD5TcF607eG-H39i2A1Vzq2JVwQkEDx3Px6eA3DjO5jSWaoOMYu_0D6sFMWviocT-N92J5RoTUbv8mG9_K0dx4bK-aMmKNLdrMtsKybdJ7UsXR1axRbKWvnL_ub-YLsfs9_u6rWpV0E5iqOcxcE__x94yS28yXA_rTDaA1JGo1A-peLa8NVUQ3BHBQZoc9IhjNQ7XLFTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATXAJoQ9ZaZRWWBaQ2LpCf1QMi-pNpD-ddC2-7aX3QVjO43rFEZfIMaEnDSy1o8ba-vIRo-2znepqdwjBFZuDfW2x0Hj83sc4Ru_7jwgRn9keTQlztkRhWAEGQ88xU708fl6nNI56rrJ4zYoao8qsEYYO_zBcYhUjoR-UvVQ9BK7kpABu8rV7vcv4QhwE4HanBO3HXEw_sTiuF-s5UuUK5TtsY-sgLulbWNjGfFp7OI4zBFKlnTSz-vqhj8TOOsXlQVZTrZEd2tvsKEIayg6Jfpwf4UAjUBzD9W7j2WGFNND8uhe9Uo1_WJVDQg32XmnrA3SGUpANsjhHpGa5NTXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inHuoOEEj6pMdxjEFMfH-LMqukf1-RGE3w0w6uFjKjmPHhYuHRzIFReSqr_2BAgKx3Qib-vJH_MMG9JNxPkfyPWQ0r-NYHIZiXlSPB27CY6vxtosV3hgKSj01j6p6dAGU5bZz0EYm3Mqu0pv4Epm1-FkEx60NItT2zMiVqerbiuDE3HS7zh4VjQxN45Rgr0AXc6zln0IOdreBR1AtLkusDJPbXHxVaBkR5LSeguHMFvcyKT7EPlwMuvOwJNmm8DbGgeLkABIMfE7v_ibg5n4M7n-G50qn9ZnmZdlnwwJnlBbScZKZu7LzPU8QIbN1n_2x782Lk7eYpL2Tlk64cv4_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6pLpLMxevTaVhfX0l9E1_H_lSz1JEDLdbzyCSNoRxLLlT4r86vIKSWAJJNoHtWzCYHiQjBlqhSpXPN2hbvIXgJwMgxhNAkB9NdvQ2Z4SaBZzTBjP9jybHEGsyrVOC9X-nZ4ux922CaxEL3JBtUMBOU-XEo4gVlIbdAb1ACGYQ-ZyArhtqCNrwmwJWCgcb7zdo29vSAVdoT7BAnSRQpm-GcUWmvmWoX4N3ijSRgyvOCFGlBW-luBCKsntEQwm0V02b_NMrMvyG0M7xipabuoxOPOblHYJqXBzbV4argYA7_D0dz9cjqFkVxyEYMPM9MmNNmKkz1I6BWZMKfB7LpPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bATTgoWWzSvirzPjxTKMHzl54JZZG4_6MG7SPOvrbwSuoxiaz9eW_DXMyxLpMNHfi7XBr0YPoBTK8-Q6ZH6XPNPfdiHkVdNNwnBcYktuLRgiO44O64FpcYbeqvurt7CIdy-OVzJBzu6euUvKKYjOztjcnqvC34waH-A05918HrPQFV0_m9batV8NQ_cDJ0w0cJ1qxC_hNGVN2TO0cJXsk9_AqX42hU6x1Kn89HAhfMChgOsqsKx67U0RxGht5hVWZcUqJyF-6aOJAmyRow3MqrxzB0_WiqeCO2xkz-fK_tgVyFpH-0sv9Gs8fxuLLJg6EaHDxrDLMsMzlY_zhVUlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAIgIeHWv6-qciAxsGvP1kzIwwavT-fmXFuBXhAQUGwdZLN1X70hF2zcXC0J6_-5FdGfpCjq2nQw4XDgLAZQ-7wcr1CHR6p9-Yus3VdNbCR6fMqCnwLyrfr0GHZjkH6vVsEGJ4uAQc01NKYwQwPnnAOD_NBkx5oTafi8U7QE69paKgeJY6qKuUwJtZV6nA6q7CqxYMgTmhfKxo7AExrltWflSFT-TDffjOqeqWcvMHGRA3HIisvkqa_q1WD8kw-3csjtBJYQFsYDyN_Re63aofW8Bi-dBhcO9itjWroR5Iiu8x0DmcQqVI42T0ckXGb8dcos8HWgaaMAWIj4lH-Wlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1WNrkZgEdv475dHkhOJbdAil_m5VlNiOnOQwOeAWtyBstZY20kJHzBhlUAJR7kGy0aPA9R1Jb8IqU5TYpE89EcbQUqD06L2HEgUiIQMsvrNJGWNV0rhT5Qc4C03JEou4lp1uVPAkn45fFSw6F_rK8oTZaEt-wjY4_jpW-ygn5LeHQ-33jvKXM-n7Y7UZ_nSEi6fEJ89Y070Lc1Qmyhpi7j0S06HuIUwBMuz2gHPSTXdRT3heDdZNCoYSjXcc-r4CvarBM7P61kqdhQzhEouAQfbUSA11kKm0GiV3IukAoLpyiXaINCAAY1wLVSvqzV8mJRaqGo1vMvlHDx4QXA2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAo2DnmHn87h4Zu6EsSMwi_Pe2Fye7-NBPT43ioWMq0cXoWCSildq1jMRxk8A1IwuMc4zH8lNTehev7y382VoEVx0AtaNRBfCV0B5fssDUmKHFVTYHew3xTNFsZOKrvC2ozGuutmVugYzXkbEQFVL14WyY0pqF7WXnTUOT0e8kqwVp18DNrZnR5ZnYg4ST1yOjyi2Oym4G6SEJN-JkfYwg2YWQqRLwIYMTYVI_b-c-9S0y5Kdyv8-t4xRyh-nFCGtUvnzhKrMGfzMXAFIjhffShW-t1g5fnSTd_B1xD0uWg8Hd6t8FIl2YO2uv71hm53gN3LBsanuPogIrAKrJdCA_fM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAo2DnmHn87h4Zu6EsSMwi_Pe2Fye7-NBPT43ioWMq0cXoWCSildq1jMRxk8A1IwuMc4zH8lNTehev7y382VoEVx0AtaNRBfCV0B5fssDUmKHFVTYHew3xTNFsZOKrvC2ozGuutmVugYzXkbEQFVL14WyY0pqF7WXnTUOT0e8kqwVp18DNrZnR5ZnYg4ST1yOjyi2Oym4G6SEJN-JkfYwg2YWQqRLwIYMTYVI_b-c-9S0y5Kdyv8-t4xRyh-nFCGtUvnzhKrMGfzMXAFIjhffShW-t1g5fnSTd_B1xD0uWg8Hd6t8FIl2YO2uv71hm53gN3LBsanuPogIrAKrJdCA_fM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOhUs8zULbpWtsF3CjL-ZubsOPL9SsVur2wuw5nEPon0JzbuwyAgELGy9rTUpDmlpmMTPGc3X5xHMIEzvxPmVX2WS-uL5KoYEnSFztAo0Azq2O7zE_Fp9kZyh7s-V1qDLxofS-mgqO_kd0crJbdTOCqLIDJBo4N5LNC_GfyPPTAr2-odYIiK5r5AlQbc3ukG0SwA1PU6tDhLghxoduklPJajLAW3z0nLfyOLukR-4UVn_RSvXF9lJ9hIwPXPY_SH6EWMTDfbMobxMR_OvJmkVbD3N6Xv2F0mdf3xLDR92QYaHJDLHoVsDGy-yztKXbWoUwflczB7kCsHjvuRwol3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpmAaQ5a9lnHnisS_EQrBq32pHDyiFN7_N_4zqSgBspuSJ96BnDNNMBsqXtWuX-LSgoccVaRD6mfw6MWo_p68W_WheK4GAvHfBeuBJRbATLgIOSBE7p-e0rH1PyLyH6Ow9lkO99_yo0BEGs2b2IWFQCkrBdJ6JGPZS3MmpY-giS3SfLV0TAGTzHUHFSs0WipGDJrjUyT4vzxVVbHmrS_IF6zlUItM5bURQhFZig-_TSUYP-cJZeEOf3nDJ7YllZRUi7H67wWXtpag4c_X-aFsQ9RR9Ci2-rTEeVQtE6NPaZCjScWdNCQXTtJZyX1pEuwT81DP6pXpKhda-aaW-A-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT4rUiMz6d57FQN1Wx_LsYiq_F7H5inFuco6uv0hvmKbWZgzN-pwS15XMUkW7lFmnrdmPGKTg0fbXETctF7pjIzu_H47bAGVJu2-abDZXFbspJet5FZ1DSY_rFJzOei6SPGZcuARqaOoGhF1lpt0VXsbnF8AU-unhThhEJiqIP2XpJqIv3EaivxvKSVtFuf_WpdKHn00xnxvqFlW8gANkn239yqlQujbudN5CnXsFwW_TTiVi_WX_kf8nwDHfoAmag392WZWcF8geY9sKRKIGsJKJ1_L6OPDBinXo-xh9mHITdjHD_MIKRKkGrSdn_nOjb3AztG9EpTmblYravQDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEg1TdWoirLsWj6iBv4_zCy3uDkmjJn4kCjWgEU7yqt8WNJ6_8hg_AaqNBVYmQ_ztD7fSSg3wMI4lTyEAsWPncdB1dNs5DdfP4861g5PFdkVmJu2MqUWcGit_7d-T7iCa7Yr7HLb--0j_uKMiASXzhGYzmNaFEYk0wF_53TpOVI1ijX8udys68khSyB0ykHeXVAbU6D3mjBCLnkDgqK9-KJidlzVJan4YquP3-VJKa57cz0wOpUQWTIxg2vXjYGyWeli7LlgWp15Vt1Vd53nYx2QOEf-5h59FvwSSbqRA5c0JLGgGkVbpssBALyZanFx2bq244SjMtTW57mGWE14Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
