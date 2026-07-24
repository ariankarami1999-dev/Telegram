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
<img src="https://cdn4.telesco.pe/file/rp_LUFX0lCTrkEOG8Waw5f5TrwOGt5TpNW_7HbCpFuwUY-Vfv3yQ6lL1MXcq-xw7il9Ewr5AFGpJ3E-KQOXSB7AskIvh8WJR4MQU9VyvYby7v32mG1M7N5u1LWWRQ0JCOmMAyIzuhm4W9NTMiUMdgaAkM-6xTlX4Ae7raIgkDPwLJzfKej209vuZB1lJZEUKPPVqF-MJ9FZWYVuDURd7qtu-d9jtuFBIqJCbYfx9lbpAQV6vZ_2M0SN-oSwThhh-xir21DnTpG7P6pS8UjPQ9Y48JGfn251H4mrLvm6LJL7ABWqwY2wmiG-i0ExYsqrpAM6eFHli5q_RrEe8a-3kUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 567K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 20:31:06</div>
<hr>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D356DfrBjxu-fe15RdbSrf5sk4JrQWdfnktUbcM7kXkkgZbAWb5dAGQuqbkw3VTbYMbKJdafDXZkWnZwptR2EZSGlvoMxFJue46ZJCeyC9yoNOQ3zcUnVxc6JlcEYXh8bQohQ9s8GDJ-ULlinZDXDitFDCOba2sVG3frMmK1Zsxu4vNkvSSZtjGZpWLADk8ol6QY871BMkt9L6BwQsCxKzd7iUmdchRezrGFbMuCR65cc0S92A7xhO2ND1ZlTU-HbTjqv5MAN6IyMFMw1GGn5gbLaCw_hbvRx7lKQd-vBAL3IMpLZI11AMlkr8Bfvi019TTwUY3lOMp9xg7-WLfF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adiHrjmxbOVcdl-NSwNOCoR32RjDiMs-jBNcIXlc9D7vvABBx0UYwa5LYugQTp82HMZedE7Pe0GSbQnqvAtOvQ_DtDvsmP28yqS0S0RpoQSYLLSEi-mH_yeX0Lm4pyNq7GLfqnjpIXlTePM9BM_iNpSY3pkoV8lpjj3p3VaEV_gEXxMsSCjz0rhfl8Ctf_8bJ44y4UerEZXjykiuwR5zfW7F7D3DwaBvTQ6QCT8eLmSAmy0IjxOicbK2HrSKWxFpyuq_W_Qa11-hJfzYxlBit8BKbBEv9F4rcJ4_DEkfPgHpo_7eySD5JFGkPHfkfheXwAhnk1wkuu9_D8GmSFjrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSK5rT8PDCPNoEmxfAzdDKpkaryt-2PzKTSlF_tkIQNZio2Q0yRLjQKKp4fAkjle60QQBYpzrUTJ58ZFeuwn-kX9786J6Jog7gZEM-y7J1PeNGZenfytQZrVn_Ek9XVkCjMXJBVhcV77umG1P-3zmKMLKp5iNkuat2XB1UNwuS1WcQrRbybdY0vBJd585SgyGJZr5royQIhvYjbJ0dcDPNOxKosl6hgl9viAbIiiHzZHFd6Q3LCaXmo0YfpsBz2wEUcG4d906icoDkOKE0CnVG6IWerMci7iP0jSfI6BGCBzBFvAv1hXDSLEM0kyTuu5WpakxaQ1szukM7ZfDv0SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTBKtUloKdBtxGWKn_cM5J-qOXB1Vs8fsvo5IESAqdVhpMQY_f9TjOiKu45dRcZaoiRubumcqrFoUsQnIVASKdFbRcuu3Wtrny8fdCq-zfWMT3y3gp4BckTopbFsmc4ajnVMsXeTvPora5a5uEqcU6it-YFrr1KKK11be59XjOFJxY923tnXcB9QnXwcZ5alTfnaoRcXFRynm2RbAGS7yhGvdeWL_TTenJ5QioBBezUd6xizTkH8sdZYesBX1S0o_Yv99wPlms7xHFr-SxdlfkWm-P09vSbZnLdoVjUD7SV8prz2-uo0oS-mhMGJCaGpCIypqm4ld6puiBfBfnBSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0_kpAyX-0VlFZH9G8_xTXVyxCAeMiUPslhAUQxYog_pWoRmil0B8SkvHdTw-Pw91wMSJ1KyJDPaNWkex09vrY1FCHF5XYG3_lDWwuvlKH-mDmCGFPPJahxayBsNyGHf_eB7Zb6IWFBW2E11H5gRDvqGE3z6WExhPISvWnDAimbATnTlBEbkbJcvBsYkr_79itUuYB3QRLsZXaRh_WFBHb3MQx2jDZ8sa_fT3HwjO_wQ6HY3Ohj-sOAT9r5HB4lWW3L0Tp3JKdVFcBFoRY9_-KbmQPKv0DKeEu9OzBF60dDCou6Qn2B1cr0MdTrig5li-cOAflXBhiLLLAtvHRVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF6gJKPQ5le6S9AYAvX4Jd8A6mVkZXDFVE3yAbXgzjTf-rrrWcS9kbGqOU4t2427IMGmXJyPXQ69WwVlcJVvT33YJobPKa38JRSDHjGQVvx3qdpG1HQkKdUWs1RUovdkvbY6X9i7ZHq9vFTGo-qGDoQXZnx88-JW2BtrZMkQRlaFarepnhE15PoDHSSgTg0lOkrgraSlukcAeE6puzKeID_E_GPcd-tUt8akZUNJD0di2UfUMxWZFBrLthZziYRoj6JI4LO-q_-IooYlIDXLWwEXAgL_moHn6Hby86WElFXHR8FvgN646U11xKlv4d5z4QyZ5u4p6g8MpO3axY9ijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8JmbuyclesmmTDJd0i7Th6GBbGY0F13a9iTa8kgSAgRTcq2jYJop8yqlMrS2Wty_qQq6XCqpeCaacak9ZigzoYkG0c1d-rugkTEMvBM6m805YCpZRMNKH-V6YEvBi1D_QGRjDb8mBIbdpwh4yUj0kIu6FAZ8xllxxI7w013RJvNcDhL90WL6Nyr-H_7h3dEneypRPRNhEy_20e2RK3gFr2IN7XsyGt7dnB0aIU2r4Ss4gxapFm6uCr0Y6HTVrLvQ7sLxim4giLrMyff9XCrJ6KRslQXaBaDv3Xgza-qxnk6W_5JfDDVlgFat9nV0dwdzlDH5M75BI4EqEqdGLtfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=Y-Pmj-vbtpEh9Zzay_bWJbH2FEWUGhyJMHtc1K-qsQBgwLJ2q7zTgelgOAz9RjwW63Uy0kVQhnx2Y9C8OxiyAiuq8i6hDs75En1HZRI1Jpxagz9wWkKCLpCq_r4ihIivUJSkhXInH5AVKb4c8_XySqBSBeYi__kFzLXcKUn6CB8oWfmcEfCuLfj8-nSHIww4DemOmUuuFw-TjYSTBt9oubra4OqY7uD22lleEW3XXZAc_yH7ADxyo1vIZAtHXWoYTbNk6vPxhA_clFVCkcJqbsRsFFBYOU4YWodtb2uNr9E8ESFMF3p3cRj4zs9pnOr38igOcgPXhr2XJ-cu7UxL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP7An1s7NRi6vVvgAdCO_3Se0UDgzNKbpquHfAc-DWRLfReIorNcf1VyHly4Ug3LuxUU1HK5lyQz1tM6PxEtOp7GqvhiL8d0fl_j3BEtQIKzcLmbIYWV-rFCF6-VPKe95t3kjUYSzr49IuNXL_QUcvzjVvWGer7JGFnCPWsUc7ip4d1a0QKbAHWm6uJODMbNrsmFyomr9TQdcL9tg3Zh6V3F_I4M3aijJpNH52GSaYn9Bm0eGALP2WfrAbVh0mkksrkHnJzn780Fq880dj4Zcab9Br7iV5A1vm6WkvTEHd4prSTUnj2nMoIAxShl7XdHnbch3NXevZhKRkJGPDic3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
g2
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5l9OvpWtZTh5vIqAYvAUXepGvQfY3kiFQEs2MW8QnQ0Dx8Q7FXp7N2t8RMgjDemtNYmJQYGHEfNvzCSUV-VidOSEKGYQNDorb6DxBXD_fS_uJp-ZbZrDCN0AX5r32RgA7IEO5AzNZVcvicokmMnbcZtCLh1osvw27C30dg-FaweBG0nC0oZx5qUGFfhUZhYMTycCvkQI7TxpwMQ7hgKE_MmnJQ2BiYMZhV4c3lMjWacwiq-Zy1iLlU_sOByON8vqxcphcAjU-HIwrphefKU4FDIP8jeTGRssB16lV0Q1XjXJ4Eu-vIj2l63sKnola7BaUfdW-80u6sHiN3dR6REMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5r3JqBx383ilFjfwiGncwOijIDK_AFvfowYOQJ8FxADRT1e9pKejaStSRXfaCAQO_2cTye8Y4Eo2YKDFmDZEjtZnp_PkjtU3cEwewDdB9GCW7EjWgCXqs8zLTAIbd8Pfhc0Q5G0pkk-4A_xwSX32mG5JAwaO8p48rtK7MKmnpPmQktjBFdczBpeHhO5QJPBjnGruySQQDokTjGr4t7ehSa0vHZ2Fb85RbWl9qs5-4Rmb1H0Y9V_9bnUBmF9aQ1kYMQOYXlFAYU7-lu_XhA4HIOWlJwm6V5gWvtuuIt_p19chExnwT6JttmQqHzdMVNCL_1J1BN2WacUmfuxdrtBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkOSqd5HRi8I80ClCUcKDJ39m-49i4T6CS4UfEp5b9dfzntMD5AXyjie5RsKV8LVSoamsf8Rllhi7vpKQeFUmBgWoXSa-lsi6079m6Mgpx5L5btl93_uF4OE3xX0TAMXpurvmFCXsn8duQxQ3lOPa7TgLScAzqLJDkmwcujvxv0C_LkVUkDe8DvFVbRlIqIWrbfq10GhuFT3AaYpoJ46gWLuF8PgkaT7pAgTZVpBpRguEl8jPNaGH4Om3KjPgmWUyn3QwZeePvqP1-WnownRUzEDAFHzH-GWeUix2X4IZW9CgK1jt2c_2tRzbaOH0LSskzbhY5yEo6BpmOlaW0Hmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TxkDVpG3YWzT1YD-YL4gt9tBMCTTb5a-HYPkrQX00WZpsHUUiPOx5sNCVhH-W0caMLQ6BmV_ITQhZ9KR5CZCGSDjKzvrPKbH1AMEuWyFmug525KNULYVrbiGq-QYv06ZezA1fj4YNU4ZZqILB3f39jCO2TVtd_3ib171nLQlvAuAAJcBIbgphPwgUjIgVicD2VmChq2SkKyyY1fo-IUJxyj-MIPHwxCx__HTp9Wo8G19YOXM3DtvrxxdznIBzoQ3-wUGyGQeZopfuANabsrVBUG8eyrZJy6PqnZFtOdw1pWlbK8dBH_YTLEk9sAJ1iMrAeZ_nlEnWkxCFschmPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtZ2ojOTMKIQ6-mFTa41HtYO8IALxpraCz3jx2CuH7hkdAZCuhQia70nmSmUcTqP3-jiDv1AjEusq9zABfkwOaR0glDcOYk3cp-azs6DY-3Xp9UWGZZYStTRzkhc4-ZVw_wA3QyuV3ZlOBQkd8GZEUIej9tKk5CZE5qrh4BNB_bUOSqKEarxWRpQybBZPvh1yhm-l8Vk3Zix5k0VmrbOgar82iojdh0tKhl2h0lEghHW9FPRw8rA57z6rPbTndT9XfG0rYo6F657L7hoYE_7Y8uUYOCjUNMSkIJq49tPu2LqLmzoCuepdrpm8XvvlqeimfXz9P1XutVruIO4sBcmEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL_ya9qYa9YvZ0_XyivYRp5FluuhwpHAXnhq1oM_fPGwiqZECXnyOtO9IZMkWp6VZmyRDdORw1XPg4JdIpYJaOBex46jPmGoqAiPCJNIqsysolmSDcYu5GBX0AxPeBlkQWs0uBgpWWP6dVTYtMsQ9_7wNg9BgD3w-KuLD8VGcs4oL2C2ZWp6qScg0cDX3mVYOsWVFgG3W6t34zYfWT1-OMKPYJ0cReQbc5D6FNO_5fsixmGJUIQazy-QyfogBJuQ2Ce86G2mD12Dcn57io1e4Uxl0t2DuQl4l11XKfe4JFozTm_vmlRRseBT2jiqDkCAfVPtzYCtIpDpC7DQGgp6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ8sJekuGaGYaOpZXHcCX621hUSr_OJXK5bG6nfMEzb6WaA2N99fev8QDw4JFvvagPQr-zXez1co1C3cZa-HXVXgqzLw39SvEK5IrRDKT5_xDpOuJxWU9zmK52FgYgtPdkSrJ6xMZFapXPEhP_mWJ3jvCY0wtch4rXMKnQFY1ZgpTyUZ3YwOQm05FjCBfR1zVy6oFmcrColOneV1X1RNoisMnBjrgiblraW2C1yyuIOcnN-4PYmpY7HCAplc_MVj9KV0kPaGXV3pSDdQSU8JoTUejCDZtubVTRfRowrkFgE9R51HCHErRgvaaTX2ZXTZfiKuZAfCGUeuAod2asnXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9e7HbDU0ZGUwELnN9bHO_YaoF1LgqU-hkM0fqFI0DD6v76PA3mJKI1sB9JIXGA3vkfy1a4j7SyEwn9f2EO8UbYOeB4jPUGVq70ZdyIhDQdFJP-DvneSi5q61dT1Z5SHRyMcXPtEeWAUXhhgnQEmqad9kA9IKqV_1s23Q4zYh2tgDNIieHJGOyMy6AA9ILWCFLl7GbKnFABJnp9KTq9CnhbVlgaA0NJWJSwILgPobooLhDYxqrcoM64-1_KjBxmvtdleK0ijrTbyxQapZTNquMhwCcn-2wpRTbDuWRd_VEudQN8bgf7KHXIlUHY-pecDAP-dbee27eOqV8rDRU4erg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqLTVJdJxc871cs9QskzPhN_1EeRdLBvPhFhoLU_DVfcMURquK-wSf710Z8npSTkmM1Nvv57WfARGvsIXwRDLzYVCPTpUdxhPzmk-J9D8hDsrqJHsraQ4PiTboZbAJBtmIdTYNcgLmaNVEYLvtJD9a1T1xcHpWQTPtgCfrvc2SK1hLKPM7ljYtvA9zhi-n8_q4Cw66wSaIC9lBeO-9eqPs4dUWmXqAbsM0UvgVlOE50eu2FLefHRbruszUb77PYtkeXM57BfCOW8nAUepX8QhgtWMd33p3kBGlIpc2DSLDg2wxOLBQbTPeMcj-xOJMsznE5AvqRmqSHQRMydulWVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPP9TiCbyugdzsSr0abAsCvia4LlZmboVacJolh3MvW7z9rRiKgViyYjh5SRUWEkk2zujvIpkIGbwaaoIPmSyFqVMClsQazYcrGQUIUNpoeGySGIyXFafQaSRXxMoVWbOXsmZhNNygnrUkjaOkGp2lrvIDgULmWTW58_SE6r57RonH1i_aBQcL0gXR0eB8mLCiw8CGKsEShVV-12kB9YPCbjgp___cdYWxewQUb1ao3UzHT0jGce1U2rfrGG1X4vguHcG6n7mI_n3EGM2ljePsc3qn8lXKfjY4cI0sA67ptb91S1SaNlS550aAeXPdUTLrLRmnqmTFanK-4pRhns6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=nuH9RnLZMtbKFJTij3cj_vtvELAywThoaqI05uqZLO4gTQh_PyXW1s_4l7DVmzXf0EvjqdeD6o6L5qSwgp5ueJIRT9DIE27qgXdGkWbT3PuLD9YT3kg9upWAngUGDSjOhQPLu46eEJ5Q4t9OhrXKCdFw38n2M_cBCfh_-PKTySQNO0n-eGch0R9JeIx140w73gb4adfG2HC_qGn38UCxkATUjMM3XX3OfcCspIFeSrjdfEIAD50GZZs18J-dYZ1y4YawzpkhGULBOLsvvSQ5xy2_44aU-FqcnwRd9W8vDkxHHIxZ8oej2QSD3sj_TMOx5nahnGaHJVPcGTKLdowhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=nuH9RnLZMtbKFJTij3cj_vtvELAywThoaqI05uqZLO4gTQh_PyXW1s_4l7DVmzXf0EvjqdeD6o6L5qSwgp5ueJIRT9DIE27qgXdGkWbT3PuLD9YT3kg9upWAngUGDSjOhQPLu46eEJ5Q4t9OhrXKCdFw38n2M_cBCfh_-PKTySQNO0n-eGch0R9JeIx140w73gb4adfG2HC_qGn38UCxkATUjMM3XX3OfcCspIFeSrjdfEIAD50GZZs18J-dYZ1y4YawzpkhGULBOLsvvSQ5xy2_44aU-FqcnwRd9W8vDkxHHIxZ8oej2QSD3sj_TMOx5nahnGaHJVPcGTKLdowhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wboko6ffKh-zrv0bXQAkVvpwb7sjSmFXA_XEgzkPiCVB0FTY4pa22I0ej1UcZQQfbDwlb4U43TTmBET_43vBb18Jf-zvuqUKwUk7HdDm1sgl9qYswHICoUGtUBG0F488s5DPvp7JWFWoYohOf3bKKQVjYsexLF2vBoAoDXnYX-96on-EXX9roUBFGbRVQueZMIaOgN6BPnCwY5_dRzyt9myR1XE18Up3jSsW_GUdqEirK4Oegwc8aHIuWLdTJuW7HAnt6vHrnoyt0MRCXZyV4qnFtN26joFKK5zKJP7-BvIxUDGNta6zaIRSzVwAk9B9CJ5iWRt3uRTMO9PQphoF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvlME1rb6R5Yk_B9soZYXilYGx4BTys6e6PD-OYRSJRBFrS4TqPe1v18pHVXJiaQxZ-BEELAmnuUoslxtu-ILsq7WHYuxJaEp9UhkbUkxVVP7fpRLHlco6gX6Tu50DhmnOPhk67UIWFVLPPsS1egXIsVAUl6OBjzDYNq7ysK-JWWajSw9eRcyHiDmQgdkIGRCaVRyouS9qcWTOi7E-Mi1SoF3L0gNl9EfMFaVuYhfcZG8md3L6EkuFg24mDIyNWNl6tIczjtMQ61faLH13T_W6pfWqh2ow_lhEk_WaEqcHkmucGZDQOafPs7iKatRLojo5Qsf_5yIJ6rgEkmKlg8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyb_1Qh2ipAj0FkxQQmKW7luM8_HGBEa_jHKOoSYXpgMbcY6vh0RPSj7B06Zhp6njJ3YsTh9cYA9xA-YND2WxV00KcICEiO_fuKTQ2joxHRI1v9P3A6tyHIsTZvNh0kxnD-23Ja1Kqf-uV9fTM2khm1U8s88Dqe6JlCtrCNSG7TWUPHHWlnqW4MFzUcnHKSAcAFWrSOGAZtZ7rVcrwOXS_-Ekj05puFYhAw-lN53FmZ4aCGdxVt9EIVe0Jx5vc8I5PgAVDdbKy35qh8I7Hg_NDPJ6nsnY7NevqkxtkFfI4kfVpiVbLY2q_Xy54A-QqVijbHjOu-tevEUokNCjTBuBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=lUa2g7SFPbptLusUbW9wUVloAKs5GRWr9UGcv82e71iqNhtDUcmp7TO-oGdcP7yc0X7EUbcSeg5MCTzbaKS0O-h6EVFFk-jsK-x2x8wdSz1e14aMlMLBdIg9BaeU8qjOeaavAjxeGwFZHQcaWUgx7I2BlwXj-Ud-X6RPv90rUofzB4hqsQyDV7uAitKQwlHtSkUdcK7t6-THf5m-ZLH3EvljBCOu5sB0_9hMDISAuf4VPfwKWhdaLP-66uoEJLZxjKPf3RJVZDzAXyk3Z1snoMLGe18LYhzF1d2X5YQEyPqbLGAqWj9yA8Dcq6P0kqX6HHL6nY6P9CA5Az1JlHNo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=lUa2g7SFPbptLusUbW9wUVloAKs5GRWr9UGcv82e71iqNhtDUcmp7TO-oGdcP7yc0X7EUbcSeg5MCTzbaKS0O-h6EVFFk-jsK-x2x8wdSz1e14aMlMLBdIg9BaeU8qjOeaavAjxeGwFZHQcaWUgx7I2BlwXj-Ud-X6RPv90rUofzB4hqsQyDV7uAitKQwlHtSkUdcK7t6-THf5m-ZLH3EvljBCOu5sB0_9hMDISAuf4VPfwKWhdaLP-66uoEJLZxjKPf3RJVZDzAXyk3Z1snoMLGe18LYhzF1d2X5YQEyPqbLGAqWj9yA8Dcq6P0kqX6HHL6nY6P9CA5Az1JlHNo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEovRhJfT4LedUkJdNyWnLjMHsbVabN1fC-NfrH2yOS2zy4r84nx-9GgqEs3j56ANSV_95981SiuyVVZDAWsxLnseHQYDDUo6HoIK025RnhtBLClzvzR-2Urcsfr2ofCkCfMUpw1_CwU6uLXbHkgc4Epfe41K6aPFS_DT4Br9HPWFIZ0MdU9Z83uCt-Ts1vrmK383lTwGqnJEYK-nsEhQ-_6MM3zy3yGf-VJltAgIzVV2nyOUPjLbB06H8wqYQmOZLCmIGvD6hdUuWiHhY4DYJ9YmW4oSbPCuURazdZ-IjXxoe-mRYwANqci6mC4430256UejjMooJRS1djHoDBdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=YKjC1arikKHA1dIqxPBJ6TnZJ8gfXFVbM8ue4UYBFrJPtqrNz8PEh0lCAC_N11NBu_w38OmY7_lJ8ep-qUxCp6jEdgr2TOC0wKLvzE_iMkCsvDw5u6Lexx76L4O-uJooKwhkQSE5lYfArQhr3kB8dm7UwcIZusuqeKvTNyjLelQZbVrWxopaMHoqHqAw32aULirthUhoPOB8VFhPgdhYZlEV0JLHlW-a4sdI4hWCamNvEofBiUKDuEhWTJ0yfEvlmA0QweaWeW6omV8ZJxjvddCRtkn8NCAvSn2GOaRB8VNJOiu4eTfH0gPZMWFmdSNT4xIihx3ntXgppPFZA0lQ7V_mJBhOWQ1-mQbSIAubTdP9kq1_vkVYzrMgOTNmj1U7tdEzn4raQS8_3wMB4ZNRWCJGbwJnFCuXtOlarzOFf2EEPxRh-P908VGXonAAQ_5VsaGoq9NMKV8ev41PeTJSOtiPq8pTJ_zOybnlwKxUVliEXgzG95wug1PK9gNRUScUZbw26JBF8EW9i8NLDIrLrIF1vf4jK7SIngMnTH-sXiSRimzkptfEauPjdXFwkXobSFrICIjP9DU4i4IJIqtSyFJMY2_UCs2HEmIpN9ymYy5PRDOHRG0NDp-5mQPQDIsqUdtzzS1IN4ZlRvNvW3hX9lBZzjegVBEcXNV2rBKks5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=YKjC1arikKHA1dIqxPBJ6TnZJ8gfXFVbM8ue4UYBFrJPtqrNz8PEh0lCAC_N11NBu_w38OmY7_lJ8ep-qUxCp6jEdgr2TOC0wKLvzE_iMkCsvDw5u6Lexx76L4O-uJooKwhkQSE5lYfArQhr3kB8dm7UwcIZusuqeKvTNyjLelQZbVrWxopaMHoqHqAw32aULirthUhoPOB8VFhPgdhYZlEV0JLHlW-a4sdI4hWCamNvEofBiUKDuEhWTJ0yfEvlmA0QweaWeW6omV8ZJxjvddCRtkn8NCAvSn2GOaRB8VNJOiu4eTfH0gPZMWFmdSNT4xIihx3ntXgppPFZA0lQ7V_mJBhOWQ1-mQbSIAubTdP9kq1_vkVYzrMgOTNmj1U7tdEzn4raQS8_3wMB4ZNRWCJGbwJnFCuXtOlarzOFf2EEPxRh-P908VGXonAAQ_5VsaGoq9NMKV8ev41PeTJSOtiPq8pTJ_zOybnlwKxUVliEXgzG95wug1PK9gNRUScUZbw26JBF8EW9i8NLDIrLrIF1vf4jK7SIngMnTH-sXiSRimzkptfEauPjdXFwkXobSFrICIjP9DU4i4IJIqtSyFJMY2_UCs2HEmIpN9ymYy5PRDOHRG0NDp-5mQPQDIsqUdtzzS1IN4ZlRvNvW3hX9lBZzjegVBEcXNV2rBKks5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd7ER00m4UlLq9ttiRW0dZRiNgBaek0agEAyxEiqd_PHgVOBrWDxFZxAOFENwNunY2lhGCWTUXYObqP99AxDEqTpdBrd20NpDDOPP3PftMAZaoUAxHf4PW78aaZsmNkCyTkYODKsVogTUuzT1lujF8G_eVCNxE0kqRfuMjbJ9zteb1Tt3Jgm1M-fYhYF2IBYU5bfZuZppLqrUffC4t9WuXP2kRsVimK-6HosMIFcu1Kelyi40nF3K4CCA6XLgPZzYPZ28rLOa9JVYY9NKyZfXp_6OSiBYXjDAQXeLj2MOdaqFff7CExcUWTEofJeK0YCQ48nGCeNlL297KyC_r7f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpD9Begxs_PsODu1MpUp2RU8cPBsBxVASmjEOfL6R_L_6SadwktLzL6BOfhBkpzQNd_FB5bAVLbI_lI7wMMB37YS1Vke81yOpvex3bLXd-CnWW21oCHCG3bdNUB0wgP-grOF-7Jgu4ekfVXVzFA-laEf2H6oNXrBFZTv8VOJBNIC7FP5exWbZpr1XJb9s2rlGD98ZZhRZB9Mww3kmVt4Rbf3kGq0A5XMUoNFFp_NIbJJ1w0c9D1NQhdDNU-s9Pw3wxflisPnBBLSg6IHqs34Xioz6stD28qKOMCNbzTcwrZVjt-OdZOz7IC_6nS4010BrRnnkcHQNQLw_SaQVNac6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t32oM1m8k6o8TlavrfrB1X1tTukTCUFgrjFJWMaVts8OTV5LLBkWf1B_b_yDziyGSuTKpFD7gwhY6LliuvnflXEjL6eQWQb-gsTSUBVIRBRsq5oud3mphV0eyLaQmbMAF9gez_oulquU6zE3tW3LoV2nHmgs-MAbY1zvZhfhm6OWwRThQHYFgAytYOtHwVo5fk9mkXCkjFi-JD90NVFqrcW_gOHKh88JRZ-EDp_n-_K2FJQ0ARbE4_vlGeSax8qqAPpVgPjvPXS1mNxpLy9ZJt_eYwPVtB5g9D9X7oGghWr8skZR9D-ChhSGTYKbUYLDot-I6gl_AlwtXonL6T-jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0WzdxOTQTisFcg1n5Blwf4WLe0gDyKjoZoQhyQjgMmAgsF7Yrof2dtm9eoGd3PJtnH64W7iCxt6DciQF9q5S4_vJ5jDeX80IE0PmpemBxfmJoc_gk86NcLvU3amCY4SCaKACeJr0dyf8kj0wlDqEIhcnxobSwcdt0AwAPiAbBjROV5EF2qPOS4byjYakUPDv1QTeCwccyLYszFzh8qdH7jWhFDzKOpDXImN6xMQ0a85bioA-ul9Ju-RNs7c-dv1XBv199KEppABby2RnqPYLueaEHk7_yrK7hXCi8QQgW7DziKgX5dEGRnq9C9m5mLWE3E9-ymhwe-ysuzSUV4yBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع‌ترین بونوس‌های را در وینرو تجربه کنید
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
r2
📩
@winro_io</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26395" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utOb7K0QC71K33j7_d4xKK16BLNBz4Lefo9Ob_o_zZ-eYbluU4_tSjtCF_D3OJ1Xa3aDk5VO32jinyPeR9i5d65tuJv2Gfgu5LbZgFT5beWKyt0WLVfrgEHT8KsFn_bdzJtMbh2TB4WDo_K7VnheWPqYohMHfg6-cu57tKbOhyHBTzmFXLG_rKQtG4zCTVv_DE1SEfSDMDQ6UtGiDIXRuNQMjiCo58XzJ4CNFs0_sxZnSwEXz0RYwZnusUivdn2nRZMJsapcxN5nOOeigWs2TNqfsabirDADX-IqMqshhWmngG7MZMeGqJQNlOw3Fs1OWumx566NP2kyh0sixdK-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQdu4nFESrL2nLPq4K3zPV706u4D35xGvqQQmRNe6gqoKoc3KwN1qBL-UXzfPFbffxcl_7ansmRvsVjeMGh71VN7m8uqJO85LokXoBoldSLQhABTyKB0ziQBOXvdzBZU4MCZcIG66DJ8mAlRax0Ae-9btPeAMiheff8PkjXc6OYtkCEfBsjNTuZCDKszBg6z9RYrnJAf3lHq-ynd91QyXKNQJEMK9YJ02Ga4BW3s3NywR9OQO1noZD2P17cEZSgPJDUlVhLl3-AO0saxJCvIVLuThiD09Kj6cRRJLl-bLR-dx1JKUP1-we9_CxwBZ0azvUtzaeQbYNzNVuFcPsQwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJDtWKY3wZgG0ictDwztglWrQQqjWREo7BaAoj_6v6bQzh2Ub5csks2JurCKaeBsb9NyajkNV_9att0c5zT9gAe57JEa_euAWj_JthJySZ2S1E3cUc6Ma8SE4UYd9HEkB5lceAaVd14eIQyl3pHqYMp4uTuC3ifFilpw1EPx-lC0Yt1kAyIAWRjRDlUpTAyhI5OrGldtgiG6XWJ-JHNitCbCsGzi9rA8lFiVrQb_TSv5O-Eoo-pGp-NN71UCDIxXK7A1do0cxm2tBuZbc34qSDnD7P8yrPbNr8JAMvxlB92F2-UV3cB527BENCa_kRAAIZzpRqTfxHFYbGxXoaAudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/meEhyPpNH7PeBzsjEQ9OzAE9FL2KTQ4jL3vfzOJHG-LtJddtn1krUeHLh-fMydiNhBLw8vafYcpSMUa7JmLf0IqGhSN2T_XYqkgX1dX6Z97Pn98xmGhozTjZt3GXIy3PAVuOI-PL6aUFhjuF3Z61JfDHmYnzLnjQco64uq7wAkIyIh9mFukWh_XRtVKLPdoRZakRUtBdmYy3XfAzgpN08mDo7WlLahnnHuCvxsZzHuOjDtRuJoBB46PArXAvTTGZ9BG8p-UXawCJAj9pqc-x4zq1mvvfbXuW97uJx3lcb7zBq5flVp-hGp0emQJPLFjFTIp01yCFFS-pGcIKR0NY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGzFkZwI8AAgpVMLKhoe43m9a5GsVR5Om95ZdkcPJ1O_qreWrQ9s8FdkNq8ktIJuugHNFx40D5tflfU5KgeBegs5NBOvqtnfBekOjaviG81_3ydWixduo8r3lW7zUT1nyT1_t5De3vr8LGEPAQjoTu6IXsdL322964SeO5CKnMffc3r291Z4WLfnJfgt0rA0f1_wTTWW2C7xVdVrDeQEFhQds-QFSULZhIkT0sAREcdbraFFIzad61c9p5wiTbIVW3zhuYVIezGwzcbGcmPbkTV3UUesGUHPLmK0pY3YlWI1P7YEyaLZrtaHVTke3Jucy6E0Wp-Ok81TrCyjUj9JQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjEyvAMMfjdUMhggsRtHINTAV74G3acNhMfQuO_gFBWGmeYKdCMdZaOjkKrOhDXyykLOJkIj1IfpJDZ5EMMygsQEqQAAD1j7xIkEitqzo0L83IsSU8gWUF4HN1ITydKHC5GPuVdCBtigk4NWgtY-kMg33_prM-yOjs6oYXLHO5CN1Qhnx3VN-BuPveG7FD7BRFzuQNzffxM4X6C8t42KCQ9ZWVrQlRZpiaVrZLfvQsWya_RZ6Ov6NhSrlijUJKLRzNdNC_CStLG6-Xe9CM_7n2BUms8AB6YbokvRTBrM8th51S-L0rgodzbH4wxj8TZi2ZYYSFG52Q5IFepMaGAmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxD1pRjUi66pVi-RSezQuGXA7Ss6DnXq2a2gvpyK8oXfSq9evKzSf5s4pfjWiYM1QGapwhp0rDN0cEkdq8ZMy335FI0ORXQ4k_adeijZsO1qMQHVHjOddqEqaQQgEmrbKVBOeNQDYuMxRk9OejOpK03ng1doD9wMlg6v2Iko5Sm8nNZeTx4pUPFzXgKNvYzUTQCgxoIG15LPPLRnx0EB9_2-J2JOrxplX9U6sEGAd7AN_rVGGsGnGcra6lQ5vSF7WhtoB8L-U-W0HT4WeXJSpY1yZoHfDHmp-CFuwA4HLxd38o86Mm-ufHXDgq77LppDNf4SvXj1zHQUqf6iMMdqJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGAgErzms1wmkQ2kVOjAmrRfIccpiyQp5PprhkXWR1vAbpcRZwiZKxB9GiqRjukdrK6SDAOebtChiOBKZGmlCMZUiQZ_H3YLSLe8cft_nZrtstKqAg2e0PrOSiCtPtssHCkql5iNNbFm_eAE1_vQIQZDp43Ud3FLwX5sZdu0p_sjTh90hWKdGf0o5NQLBe32WtZDZBlGYl4hIfmcEA0QN3FhnUJS9XB_LTWSaiJ0FTqcMKaDlfjg3ZMK7UaXz6dOJw-xVTfbm6Ca8npN-TMCl2o_mbgH4-Ny9vdVbH6P1yrEJxPWVePMwsyJqI__GIet_qs1eXinfGll_EbuO53zDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggoXP_Uju0zmQGbng2ZYcg1uaXFWhr6YSWnRRXxLxVfVYuFYEAxpEEu9dEuBiJE7aG6a-fxDlBeHs_eGLtZuiPilTDRLCcAKx4luOV_YPOXWD7rHeaExUk78CW63CDfghaydfC64r1KdC71zaor-vWO-73rAjBqcFJkuXHdP_yY4TbGTljngHV65VC8VYj7jaV2DBN6D-A_CoPpIXKMOkwB2okdcoZg6ZfMzBAetSZX1tkxD6yRJAjKF23fVsJIsBzVfrWNlsEeNnsnbyJHbEjpyF8a8WQ1veBE0LK_jOwrZdb-DkTByySE1-DUWBFI6h-PUQyYUb28b2HjuWNBS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOJFy4zmvjmBNRQFrVy846kQNO4ym_IU34u199CxZgspVojefTOfg7zew1rr5Gr9hfe597QhBNNetnYbJbxYbqiqA52ZMAitNctdc1_2ERJIhiwPlm20lny_bgchc-yprxhIEJTo8PrHDl64wN1TWS4ji5KDzeqnRYOxTt09QFJ6SmBeUeeDw_s3rQveSGMsapV4PBhhSVinJqTFj9izZBHcCKAosearDZPDCHN-uY6gDj_TPOFpqBeKhfoWZESaOmEjpbwpPLhGSq5x9W4a2U79tEfT8UhMIweA6ufj23gukZHgaDI6vIpcOB1Lf3xH1i_jSzIBQx22Q-_nIxNEHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZV8-Jahct7bzVytppB7yyGqiKcLTtzpwJ3K-PpFacbc_67TfM3EtQZEqTLX9ne3z3YnSZEvyVkMoJVSNiy1-vtfgJ6AU-pa9_KG5_Ag4yMY_JHWDqzymYBdtDtnmBop0kCrjY-5D7fSUXsYRa54WJmL4jSWJ3-pZz5hcZ4an2Iyg705pPyjRg76YXm8kjflQrLG62eYmdQFdxkv-vWLDOVQgRnIJtTy4TL8_YGA731j8WWJxQCdeAdDfQoSYtFuVrFt5N4f8tZAisACF-xW0WXEakTYI-4S8zdPSn67hXdWrbQJaZvZaYt4LgVuYeO1n4w5H7oXvRls2xzSvZlmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=i7ipmJqOPyF7HPt46furw9EQwd0sf2Ki4NUjnvxOIvuPVnMwqtI0748TohIaTETJhMltAbYdWO_qtyInEU9zOCPSVGM9_aPqdnqBFfLHexI-uFbU5XKMgYSHmMr071Md7n7BkHHR37_ArvAU7c2j0sYi6osvodz9cJWmdebXnnm7BIxfXQy3u5A2XEia5LiwVpSh5-oyFL74zdFuud0XIfKAAud4FazELIzHDMP4pF18r-aP6SIcco1H5iCiSgCyptVFl0MPS5Rn98Yci-firGdfoXhsRUS86h1MjDTUx47ZS4mDbM8diB4IY8zEvEKWdWpYiSt0FsBMvgN31txliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=i7ipmJqOPyF7HPt46furw9EQwd0sf2Ki4NUjnvxOIvuPVnMwqtI0748TohIaTETJhMltAbYdWO_qtyInEU9zOCPSVGM9_aPqdnqBFfLHexI-uFbU5XKMgYSHmMr071Md7n7BkHHR37_ArvAU7c2j0sYi6osvodz9cJWmdebXnnm7BIxfXQy3u5A2XEia5LiwVpSh5-oyFL74zdFuud0XIfKAAud4FazELIzHDMP4pF18r-aP6SIcco1H5iCiSgCyptVFl0MPS5Rn98Yci-firGdfoXhsRUS86h1MjDTUx47ZS4mDbM8diB4IY8zEvEKWdWpYiSt0FsBMvgN31txliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkAd4kjhPuGIxtHC0zK9xZH4AgyMKxKzBb4gtIGqAbp2eImsIw_p7AxMW_2ucJMltVyQ0pZhcXeLcqXR1xs4tOgiGA07RDYDLj7HnQBvIkAvpez7cVDJw4GDvM9fkztVBu2R8x8JzXzib69CQEiGyXfHfLhBPaaBi0C90_L_KxiCOZaPWhYFicit8rVOH6E4je4rtpdOPPpLk4d9n5MfZg-Vc1yLVtdkG4DOA9yImYZjG6x7GK74x39SY3KVqxvGGFBpUbyh8TbQuvSk9vz2IlmeFDtXnz_qC3KQEP5Qtwa7bGvM6wl6mCCHxn2JA0BzWI4gozZkLm5I2jR4IKMM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHA8KuAcpPN5vzS5tNVQpxaEKt15veLTh_lpoMWD2dwnqlxBk9Tlj6-zYKvrKjmbj3WDzwn9Xku78rlT-zM-RFxii6ujPpCekSlPdeU6yNnZBPy6DzuLEL3OUvXm9PPP22IP01gOne8pKVQ88dk_U8lSS2pvR4m2c1L5kozq0EuhcHvtSnmUYtSu_Oso6IVS3nljGj6UAL-GW82PeebZZfrNajOG06rBxOiZqLPjnR7SM20lF2_RKE7HlsI7qmaK85QhW-wY-DqzZKw9fxtRbbrwoMolqOxgaUOoyxSXNRNwB2x3WLB1OzHChGahBVMduN20DHT3dMoCxL29m11tMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt_MxA9_6jKOy4GCzJzCqdsvboehefrTaTw8NHrbN8cJY1GslvbHcMPjtCVmLrh_WHvUEtRaeW_J1VW2BHOErnOm1c9v9xqgJV3r4IVOhcDwFOVGWczEeBgKPGZKQE-s8xq8GseYv33siPQZD2oISuUNtdwIXqBojPLXYnHhuy9m3vOk-mR-bw1kn0_38fYQY_BQtczxcPDjSDiqsq0u83DoDWW6ax6YUf67VC3tRKwCKyEKxJ0noDXaG3h7FsZvSxGuR4lBMnbPooaIX9D2qjfTbXj9Bd_M13NBLD8wuE-oV7A50gJ0R44zS1lKpN3YcpfM7VqUNalb0exGoKrt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84SnE0Y43GA1NCxw3pgxdKWlasYoVQTcdC0_RytkZJnI2RN291naxwdN58eVkqS7-Op4X6LPTGEgXgmV8rNjXnErxLge9O_jQRDEDnjtZfvmfc7s1kM3m4vGiP0tNhpn9f_AqpHJdfGED36-5eUgd9aoipC3VwZjUGUlMyWK9xtwiVz_ougpxNwmOhaB-mGX5BtAIrGcmB_6nmZ-3ZyDFYflKzcSZ7NingaRwB4Vht8_Lg5-FdYGKn3Uc_RUjaQy8LwRapXv-CjxBsy85jlz6IPHYtVEQWiWTrzxxHFivAqjk7HBWi55e_2cB_yy2ksq5bpKR-zP1SGAwmb8Eb2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=Aku6wwyQVT4x1OCA3OLXYdmgdOSE722ecatIOLqhg_O60_DYOwYQy2MzJJ4xVs5fNncNqyaVsrBx6nm5XKk6j48NiFGAeL_YhjqPqvbWe789sNRe4CcpD8YmKhdHz9Ck6bd7HaQsNN3yYotSZ-OaAZpsmzKwH98nNapFHb4YNIM2glQ2dMSE5vL7DzB1bV48vJLSQJBICPS4c9FKmGSpiwNy6lpUsueXamcNuP1JHvbHr20qzQd9O5_YnKnbJ-ywXU1rrQYcXQgaWhhPFxhDGMHzf5jeY9D0kRy_NxVyPvP-Lx3ilI8iBp-AKNLwCCa8BoC3aDdF_WjtokTWHeLjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=Aku6wwyQVT4x1OCA3OLXYdmgdOSE722ecatIOLqhg_O60_DYOwYQy2MzJJ4xVs5fNncNqyaVsrBx6nm5XKk6j48NiFGAeL_YhjqPqvbWe789sNRe4CcpD8YmKhdHz9Ck6bd7HaQsNN3yYotSZ-OaAZpsmzKwH98nNapFHb4YNIM2glQ2dMSE5vL7DzB1bV48vJLSQJBICPS4c9FKmGSpiwNy6lpUsueXamcNuP1JHvbHr20qzQd9O5_YnKnbJ-ywXU1rrQYcXQgaWhhPFxhDGMHzf5jeY9D0kRy_NxVyPvP-Lx3ilI8iBp-AKNLwCCa8BoC3aDdF_WjtokTWHeLjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=EMWjeIsissL1CrrBlrE2B_k0aEhgPh5ZVWqetl3kkQmnPhdCv_xyq8WJ4nCU5rp_-o0ARlFZfRQuNAA9kBf-w8LZF_7h-Q-5sJd1RNaTu8kv8lHA6fJZerfs_vfz8koHHWRN68Rrkuh_SlDwACulk7oyIOXm2yWq73_WXiFXWVq49Ggg0WQh_C8dNyjXudnAcrYcA-Bt2CLwQh96_CEYs0IRW2t4ETiHOSqBQVqjLoouPUq5bWBdIOL5qvwonTwYel5QzIT_FC4pfXUUsBSYn__ZN29IZ0yR9oW5xG8wFgaKXv7YwyhD4Vs6oZPHRtPumwV14UijPsdS-9uZ_8G08A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=EMWjeIsissL1CrrBlrE2B_k0aEhgPh5ZVWqetl3kkQmnPhdCv_xyq8WJ4nCU5rp_-o0ARlFZfRQuNAA9kBf-w8LZF_7h-Q-5sJd1RNaTu8kv8lHA6fJZerfs_vfz8koHHWRN68Rrkuh_SlDwACulk7oyIOXm2yWq73_WXiFXWVq49Ggg0WQh_C8dNyjXudnAcrYcA-Bt2CLwQh96_CEYs0IRW2t4ETiHOSqBQVqjLoouPUq5bWBdIOL5qvwonTwYel5QzIT_FC4pfXUUsBSYn__ZN29IZ0yR9oW5xG8wFgaKXv7YwyhD4Vs6oZPHRtPumwV14UijPsdS-9uZ_8G08A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHVn4oGVaH0BwvdGwpSzh3JiaMAZTTDv1OibnQXV769mm8WP8jNWgL5yN4_Lx5cpOKg7mInXzNG7XOZMrOaIzRMdXTXwSNOd9juc_wHG6DDR94wYMuDuimkbrLlLncyzSQcWQQBAfCB86gG8QStpiNBPmKojYRr6LKYaWtyqoLyJPKNsdLbYJsCmdbNygsmlS5iY_TFyYXONU_UeY5EhTguQfnxF6hVwkY63seYbo_2EnOs5ENQY9WZ36SzC_cFWq2OQyxF7vwihxwBdxMg8TY2hVpoMGNazNOJ-2LqTQ3Z5bFp04kHwLhYNlCJQDW-Bj0tMuaqGsDHbrxIrzFMsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoNGRaVLXvBLcqORH1v_AgkMnkYwdZTaM4M1LuY_FFNpIUSPxzCufllv5XF5U5E7mDSDfvYPLsEcaT3FCK6PCK0kumP5DXlPRY3pBssECGYyy0miSIlfYDXN7iKJt5PJ9vytQ1HWfKOxO0b8Lx2vffl6x2bBV7LLD66kvwB4Mc8T2MqVQgeeQ4A3Yk6IOue2_8v1VrbbN4pS5vSe3Ld1-mrBRKh0P6zhu8-cA0DQG-sQF6es4EiiqfSsXTzhiTzT6f11kEFHxGFM_aQ4cPAYIOKj04Ptcxf8sH91WLhqycAuWZyDfASGAkpAcgmSCMe8-jcWzHor3dz8RGQpcZY2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkhPnbX3RxoTlbuMmAVdu3T6Q-aM6fn0m4aQOhYDa0yH6g8OBDQ3QWrF-Jt7daUiy24O7_47ExQy2QVOXwKTVNeq0QgeNRcsOqg8J-lSfKntGh-7-mowHh-f1VvvimevlTL_MnTKTg6cVKX5fiiXqhzB7nd-uhPbGXShZGPLf_j8nz79SBaZdPtP6I2LREHd2hte8ozXX-6iif0XgTGxNJm3wzRJcJ7YF4szlXGGfGNhanceVuC6LKo7ekP8roIG6KMRSTPAR1gR0wzMc34TNVgan826Wp49v90mJzWdEtS_phPbQWoXRGkeBp1It-MLUzvzLNyo2v6TjWhlJYrbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlAyGVBufUECX4gpj-ELa2IKCmGDccUaRJcokAv2iFfK9sR_s4XzUPCcYOKUldWpUkAgxJC3KE10wP1r7zONP8e3EZ6eMQvMol0ZuMC4cHBVBFVF_hHgmCJEV6-u-RJdjCLXyMeq1KI0CHqWFBoJX9C_5SoaP3h8UND5O_a8pIGuU9jYTtmnh3fbGrP5GPgFLgtoiw4CG_FizSls90Y58lQJhO2XhcCOHlaafqMt3NmgMA-nJUIqOohvqE5LVDnZ2jahtXtSElF0JjWSqeKUQJT0ZHvkGMueLvQXvsmvKsoCWp7XR0OtY4qtHQXx1LJ_KqUUuXW9P97wwHeuoOcNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlROH4jfPzr6FZdcXVPwn1wJpX7ld6CKKUJAY9sU8N5vmW6ijNPBktQuUt-yXNr1QXzsTVgN5WzhSi8Rl7mhNgM8vzvDTyiUCBpaB2mBhTdHUexZELrCnNam7jqgCNkN2JnJXwHf3JBU6hquK265Ug-ZOs-QIQ5HoEw3gT_qkDhESxsPIg1hQ2EkkhdzChyChutRZUas-JJEjjZSJnfe0n4yuzY2VlTs3me8AxRJi_CAN2C_G91JT9hpODWIrF8Bd2-QKvdlnbjhNyqSZHdww24EYV39TGolaD_UuyiNTvshHcbL1hTArq3VIRKtpmKYr0Mo_ZfFTgnOphrbQqIdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1xQN5izSPmLFYrDPOt5T6XwaSgJWZQbK-npLkbd_bL31WQ--u2QaR8lhzuTm6F0oUCPWtZER-DSvjCPk7vIx2UxGki9YB5thu_jeLEUTuGXd7UV9Ke5SwmfTjNJImJLkGlLDsZICzuBF08PVieZIL6OU2Qge0o5Sgnk87GuCXr0fKST76eHlu3hFer4ZkHSHE_gyzNn4pSJXyjjxJFb2CHhzwjnOMGAgbqf6IsS2FScD-cS73dN4JDmL_ub6zoXcLf9KCJO2oBNDj8WE2y9RjELCqkJ2QVNf8FUbkbfBJMvLHz3BUFnR-tnearkSHiaID9r6vWh62t970enNohMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJWpHRV58f6-kC0UVu9sDk59bRlFDg4_4DpJHvf4wqhLV7xNJTf5IaCSQMxkKDs6QTbWpG8sMS24Fh62y7OrZzrMqg1yn7M-cYlQEOvwsP6y1Eqyx_QLq4u9flm52hZLcehMXJ3GbGxh0a7C97Rt_tqjFQe39GTfEYb1z_p0WEjn7MwzPCsj1qpNNmX409rYOlXBROoSMdsnwyyKVwqYlE83JzCZcuKU_lAdDYwH-i7yoAKYLppeq85ppuUnD2O2hcYYBEiOlRuZruqYfj2TonEp53pcHCmduTcIyU-9Rm9axBv2tGNtiG3P08p3h0Dw4HnhQ3R4knFlN8uzLLBgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHQ14H_qJ84mf2IuyFXXlMBtinGHxXeoMB-D0PHB3K1IsVUNGIf3q6oaZ3wf90rf2yQYHnu_iWEMVONngnjfjeMr5rHnO33Resqu0kpQ5k6pJkklVNxi8V9LzF1X7biZXou-P-uEyUUFzFVmnMbfdnf7bOvMyOPi9sgB23nwnq0ZyX7wA5cuAaqsxRSuIQM-sBXb3iC3u2HqCuN0-XKdLpCXsnnDEpk8NoScayldyJnUA_dJsf4_dXQxv9e_kK9RJvcyAbjMdxeJvB0PeUsRTwEDsW9jDwNIYmnjGi6MdmgkZbRDinhZU4Ql4r9C44NHLLWH88S9Ahf7bmAIBHBqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=nRfRpwJ60uKv6DG3A0dmDG6O6DXImNJAJb2g88Wx8JHwkeE863Hnyft_XpUM0F0hX2OOHK9gir69LMpS7brv9uG2kdloeaAb5ZkLIvj5eFcJ27WmxerY6mER1VKbFtdpbWbH5R46TVI7bvcJFMmM9UjouCI99x-4u8l8GRaBnWAx5RL23olpy6SsNB9XR_LavvUYmgTfv2HmnN4WFmVEh3z9oGOKVaALstGg8F6zbxQCAgxmw-M9ZOkgUMFR7ECzQQK5OEqCytH8FRMpmJ4tYNytc6hBum0qBR1WU5gHs0L5bQ0XlPktxsRcUm001BuNwSebbTGkka8Pan8X6cFJSTx21enCbSwuToBE4PiexJjUarFBXcTdG39Dc-8TBT4r2ygk04hhj3qinIyKPzv31mStpQRvrOYr8u9lNCNzb86kZ-7PNVNbun9MV_vaZd6fRBh7vqq-KE0Wv3DvjCtpDDvqoY6tnZZvAU17UkDGW0fYfvPUyauROAiH1Wh0dyEajjXzX-60JOCmMnAfd9BapkMT4xCMXPmDyoyIyiLH0-WJEyWMTrEEj8-Jlt1hhRtVLFJuRQpYFgoUhqal0LuI7UwWiYVBEfnj1hTBdegXsTySrY17FGM_2Ex-QoAxffT5jRH2rqh7AwRpkik9Bk3M-KDLIZD5Lqj2Y8pCHNw9y1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=nRfRpwJ60uKv6DG3A0dmDG6O6DXImNJAJb2g88Wx8JHwkeE863Hnyft_XpUM0F0hX2OOHK9gir69LMpS7brv9uG2kdloeaAb5ZkLIvj5eFcJ27WmxerY6mER1VKbFtdpbWbH5R46TVI7bvcJFMmM9UjouCI99x-4u8l8GRaBnWAx5RL23olpy6SsNB9XR_LavvUYmgTfv2HmnN4WFmVEh3z9oGOKVaALstGg8F6zbxQCAgxmw-M9ZOkgUMFR7ECzQQK5OEqCytH8FRMpmJ4tYNytc6hBum0qBR1WU5gHs0L5bQ0XlPktxsRcUm001BuNwSebbTGkka8Pan8X6cFJSTx21enCbSwuToBE4PiexJjUarFBXcTdG39Dc-8TBT4r2ygk04hhj3qinIyKPzv31mStpQRvrOYr8u9lNCNzb86kZ-7PNVNbun9MV_vaZd6fRBh7vqq-KE0Wv3DvjCtpDDvqoY6tnZZvAU17UkDGW0fYfvPUyauROAiH1Wh0dyEajjXzX-60JOCmMnAfd9BapkMT4xCMXPmDyoyIyiLH0-WJEyWMTrEEj8-Jlt1hhRtVLFJuRQpYFgoUhqal0LuI7UwWiYVBEfnj1hTBdegXsTySrY17FGM_2Ex-QoAxffT5jRH2rqh7AwRpkik9Bk3M-KDLIZD5Lqj2Y8pCHNw9y1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFheLdUnu88GnJmmsQUkshGMZlGGDn5IH-y1e6nS-tOx_Zq-oD4OKVVdpFCEbObSLt8C8Oy4lC3lzfDuzw5Hvsz9MWAslvDNHWxLLKvit9yZEEfaqBp5hqmXIr8ws_LhSQo1zUaVjmA60fBggTl7E0CJU9NIJQkhwAVpTAgi3vvZ0WaqR6GUYdYlk7EA8gecQRVxVtmYIGksNePQilN9V6QRTxdM4C6jbZct0WHY9uivfPz-QYgR0fOiP_uyGyRr3DeqSeNN6TCzv6KbL4UNEu-WM45suysACjsoOZ_UCbfzFuhYU3NfAAcHZidHdsJDRPb0JTUDenLbPp9P0fPYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvsXVRbb-0KyHlNqWl9X50JfRwVJ3oMcKyETc0JUWAfj5cPxrco3Tmo5OGnrGvOADLZ4nW0isvpLnwGL0RDZFKDCfU-ekLwgkYFexz13cKS1YJfEIr2nERH4O2j6lhOAsEG-X4fAfrbuTkgvpITEZVkLuXei1kXFpZr7hFxVZB5VLiyUE8IUfQ_DXtN7-ATyFxmjMNXls6L2O8cGUwwRjrPM67ZiIU8aiyDJUZRjy-jbcCVISara6yIr45Q2fiJ4yjvWlurtmyqVsnBLHtz6TFqyXZVE85-VHmXPfgqnmF5KM2-F92dURhRh8rozycZ3BhaUXlAjx1x49IBNMLicEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOzxIQbUSoklFEHeSJup7zzqvi7f3v9yiZZb0Gdcj4xBrT3V3CRsQV1zRRaHinvAQvhSSIfZf2oisnkVZQ7jianQfwtSRJHHpiYgvtdsNf3eDLhmHpxjvEMtUCsfumY7Bp3RpD5gYpqRq7LRpAP-jdL_Aqq3DceD0loo9hygsG4ie3tjMCFTn0FkGGMgsqBhDCpBGIWhSv64OQVgipXdm3dwe2-H5zBZePmyzlqB9Eq_MO9jvdZrPBms36zVuXWSc9nLe_wNbmYjXjXnjP4YqAniJXbzL97I-vAouF0HuSU6nzem32Pv6tkZ3-_9zYOWoMD4rs3K3KZ6kSSsM0nabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg0vtByJYbytUBNjzX2nAF1OfQashQElijHbJi8s4hA_3XoK4kKUAzcNCyV29bQEZUE3cI-xI8AOXDlbBA4DUI-IMKEupKvnM5uqb39_DRUlwdIf4z7-afrD7VYhPPTGej0z6hM6Uz-UGiFY4xdqWD1CrZbAYfva591WUkEiCQtsU5n5PrbGcdGqYFQ9H3TE4KRGUm7mA4h-BrXSceENcO0ObjIrZdQuLmpRs82upi0me3mWX_S4Z1h4kq_aABfhsDsZG9FVaQSCCoa0BQ1LodpHNKKZbWrVkj1L3r79HJZcNY_427krFeLL7gqIvppwmt9HXgGbjsqjOocVUgpN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPQhQ3E7FQ0goH74Cd0qPHrgWjWUd-jjqAVX2ceSyQWz0muALwTJnBh7-cXqGNHR3daRSr7uRwGiw02SIjYrpSx4O5Xi3vmkmVq9izy0mNLP-iHkX-fLCuJ7OzuT1G6G0156CLNbSacMiR4WRiy9w0YM1buw4ldZbsuWKCsp1kOUkUOqEO-avdZ9uXRR6bgbNVRGto6vrImQVB1D1uRncTDrgAbwpzC_7rGnmFCU9pc9xlhDzr_VS_VDTuU3Cs_odFKQENhFqvOy-AOQWMLGBWmrbRDzURDNt3ONlNUP7tPgC3L-fJ8CJ88w8lmpqpCU6mkt11VKJna8nFkbH4Bl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHV9E-aUPh6HPDeudpMwleRiZdJdiXGPiFYk1iht0llreztlqVlca4Fhm6USaSAEzw2TwlwWSf8ZIhKzbfAR5tsU3w0r78R5F2Pn-egpto14PKJs9sx6e894kULmOKi2rUqNA06G8p4E_QHVawXlvHDG8kNxvMVY2FX5Y6Em-ep9O5HM92ex6Sw7ow5MIPMcROiRknFxedh9fOEWEu6Azv6_dGvCWAdqdLz7QHWYS4-ZUWR24NQRe2C6_QkWK8f8yqEr4ey6Eb5r-rjg2fvFYvOwfAHbMDWSMNQnHOkOtnfBrW6P2eJd3g7PUcbxoBh__MFpnsfTtK93voIWGfLtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJTbqWXOQvUzQdVocuD8dnc_emGx-SHXfsQmBVtLN3g-BTjPNhpW1Ksk6-fFUARuOgQ5JnjNu_WporIg5cTU1LNyB4cRpQcL5o3q_onQAo-uMhPoDoIYTdbqAvQKhHSYK9U49Wi0CP7JMm4BSLMS2nI2IcMgLdzCZauhrd5vCKPiDpwyi-JvhFenYriSfxf82G3CGSzz3RriqdUpg9UGq3DznH8Wy9_EAXDjfVxvkY_kaTsktpeG3iQdLxk1YFX4oxtxnDvGxY2MAPqLCk8rjYexfl2V8Mxu9-NmZN-XgqGZ6AB2eXzoFCGbHfLHKXtLf-fwJCSgJWhfh4rU_mYggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=QTEq8v4hYUhSbkiJpIv_DdOiSZUTXC0r-6Z9_G_8OPpCwQaOBcxUes9XJ4LgYCuGmBFTKQnBcV-PJpeoXVrBbHvpAZcEGKh7I_l_y1ZeDoNUxgHfX9nWsk5DEg-jpOzj6WF4JwsSI99X4CEjTGCVL0FBlgTbl25LZTuY5Mjub5_uG9c14U10qgNb6B_xjAPPnWMRfvuPLF_ByEua7SMby6pjOspWk6jvuKRWDVXB-aLRBpysrZr1uEWUKKaE2imFMNoRGShDiX2N8bOewFJdEIMHH5JwKdN0WoGU0CpuqjzPnNAPC_Ihc-emATgX6rX6sMYQOjFmuB9nN182BVE6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=QTEq8v4hYUhSbkiJpIv_DdOiSZUTXC0r-6Z9_G_8OPpCwQaOBcxUes9XJ4LgYCuGmBFTKQnBcV-PJpeoXVrBbHvpAZcEGKh7I_l_y1ZeDoNUxgHfX9nWsk5DEg-jpOzj6WF4JwsSI99X4CEjTGCVL0FBlgTbl25LZTuY5Mjub5_uG9c14U10qgNb6B_xjAPPnWMRfvuPLF_ByEua7SMby6pjOspWk6jvuKRWDVXB-aLRBpysrZr1uEWUKKaE2imFMNoRGShDiX2N8bOewFJdEIMHH5JwKdN0WoGU0CpuqjzPnNAPC_Ihc-emATgX6rX6sMYQOjFmuB9nN182BVE6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=cz_t9orseU6Iw10OhM85FelNY56cCu1BmwVjy2eEEaCMNNcXRHVlb1U5STj2fmCYeSPCQCjUG_Xy7uJsneYtBmzKSZ1zvygUfRhiqy4N1lQSgxFyRra4x_kgMHMWlN_eOemOAB1cZlO08hUASurf7otybd9QyQFSt-GwO7RuvYfRwET4uWuN1g2HGIcru4aO9jwfj16d_OGza3SKqPxZrdeLTtAOJW-N4KdUSSCYQJab65xfnGFYl5LySkS-e4aO3NlPdWsM-_z8watyuMXs-cgY9XlUGU_Kp8-_1L03Cjj0RItHJyPLTwqWUonhjTv2EbMSEZnsF_M9KkBNuN7tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=cz_t9orseU6Iw10OhM85FelNY56cCu1BmwVjy2eEEaCMNNcXRHVlb1U5STj2fmCYeSPCQCjUG_Xy7uJsneYtBmzKSZ1zvygUfRhiqy4N1lQSgxFyRra4x_kgMHMWlN_eOemOAB1cZlO08hUASurf7otybd9QyQFSt-GwO7RuvYfRwET4uWuN1g2HGIcru4aO9jwfj16d_OGza3SKqPxZrdeLTtAOJW-N4KdUSSCYQJab65xfnGFYl5LySkS-e4aO3NlPdWsM-_z8watyuMXs-cgY9XlUGU_Kp8-_1L03Cjj0RItHJyPLTwqWUonhjTv2EbMSEZnsF_M9KkBNuN7tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzyGMgJcl1AYqDpW3_Ut98908VCru-K3M0xBXPO-Ns9vszRSYC8kDAYirjNtxPgE73XJNoMyqnFiEmD5MklbL9hRsE-SZHpFFhQvijUSqoKdRlKngFxuf_BioLhQrfR8VrdMiexYqcr8HRogaqlWBGhYi9d3nto66ycMRYRgjPVcCj7NYHsSwk95JfuATfQcW1m9UACiVgpTb6CZ9YXvgE0Hk5UbxMzZ7nAPD9aOUY6tcwJaSp5c2tp087gBJDXBLmHd0gtUt6NdkGJlbOsrPzBIqNns33QNG5d4eFc_OLHyAL-z-wFL8pJSOhXyZoiTvYrWB3I7zDujMrbZnODfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stqeo_5Mt4uGpocak62F7Hwr8StbcKjOeLoeugWu_dxOFcNZL1vfMsFQnNN4azP2s_bcxQJEISHwXLEOQ84mf3HgSdCPXgWSJL8S5qwwjYaUogNRzAh0ia-knGnaMUM0UArD19G-Rd2-4jkkLzrocLN7OEXJFOQ8I87yAyJyI2IQ1hDnegAf13Qy405Fhkc04QUVyBWR7gj-XRZIxADNUOJ6PiI0K9i3h_Em9SlG1PKnkliZxtlaRig4JsuIJwJHU5-ZFi8Xrb0Zhr1wgTuPcNf0BXI1OFSc3sPSiZERXDo4XRyeyf42XKKOLy0hpFv9XMCyaognIWKUwJhFViFEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihs3m-j0jRHjq1dXB3GQsDRFPl9OW7vUAl1mttkzeiukiI-ZAF5QN0y8q0FgglcmebFROidUhbRAGK0zZKKJ4RcA2cfQjs6w3lO-ZTtqAjFzjmJoE8rvZLaPoC8MQdU2XU1CTbELZpfNLRnRDsNvL294EynYPmCs5kqn_omMpO5A4sNI9r3Ah8lMbtoXgVWJUxyWP_JNMlW_0IJk1LTxUETVB74sod5MJiRQ9Oy3AOZ5zeqOT2X9wWa41llxQ96OGvDkY823VNyP4WrMLPdv8_knw1PNfQjmvjCjQfMl5o8Vh8FedbVjMUqFwyxPTrun165VPyTQeeloEb7aGCLb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1K41KOYs3X4xgV_aNZ6ltBClxflwegVKfq0EjtF4wCLcKCtj4mAA9MFxn0O_7q1Q_BDkvZgacCQAmVapkYQPXa2nJ0DorZiDdNvGc4KxQXcChwO7C_O4icZKt7EwAETl4nwtvTjr6KNA6Due-41Y7vkLJfR6X2iJrDF_QY1RFHP7QVX9wyjCRDTEsfRfeIWN6FkwjYAIQ-jlBGuxUKi1ARHWYBWRJx7vZmOdeuMlBnSAjyupQsvMD4eBKWzJZyfhLFaXD7E-kP8g4RWk2Xa_06alc_nX5UCkkMN1X9xhYPWnL8_BZeZD8kFJNf9zqeXrNRd06NUuSUrIq6LQNXozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzw1MBHQuQyB9Xfn9nFgW9PClLfQZjFNN1bQKNH6F0x5CaKmJLI52mu1TEzC4oRQXp5YTSbdTQuPpKnIhtujXMJOrq2jkSj7jRRdDTxEUDRAjc9ZoXPKbmpGnA0mtLqzH2gKl_BFIcfm8VNtUWzfYDf-qltOomUQkbXgCnQ1h2o5WdsxyaGSr_jpojmEljUv-rQDwiR7hSt08iEVpRoKetWyJ9d5g-OFIfnmgdsz9TkGTT2WxKYQiFR46E68ysFA5vCaDM3FoIrYg-QgyGqp94Idvui6hWOoWEl6tRZsxSKOCHsOC6Of0sTRHBftUeIJ3xXngfhdqapKxUl6qyZBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TloNH0oMnuPxMjKBe0tX1_ABe4c_i2nQc-Wx6j1jizxbzmeG2GjcfmT6PsOCahHzkJpNHEwrNg0M_dP5pDdId-IFxtXjVvOWR1ypcLQzi6Zer4CX7vdWWPfJYiB-ZtsSPcjoJMmOnqPWxE2NGrH-p8e0by2vOzNt-Qx4NDar1G-wu83Kwt5JPOA8qbkRILPFMF20WQKZtG2bIcyXpg7U6R7TTcFz2mhwK9U2mFugjNEiFNOL_MmjLSauJcibzawCGKb-juiUwwWCp0jLULDoMhqjb7Sh5wHPcKjMrK6MrrDxZFj9AkI0Xvn3HOATYq56NimbVkEysdXA1vTnF6ZRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-hhbxb1lI8wOPx6-HYaORL5NkhQDKrplD_-f-WSE0SYFKRflw7CaG3ermg4NbiiICdgBdhIsGzBq26aovYQbgcQIdNSlrs3jmwowGBDbXlLEAYZtzcVnv77oCeU9D8Yoq1w8mJseSK5jRaCaGCrmu306eSN082EIysN39noOy8o1-mSDcGWwvT8tmFxm4ncFIQEhtwnxoO3KGeov9B7YuL6zZXM8AnUwtgLuqJFCJD1TGy5K0nc4ks8na2Ji8IF5UBZ3I6aQa5rrTv49caBvjv3sXBN7YVAl-UDzjd3Vsw6qqzEPOn4lqNZfBvtFCVu65OCBat1WlpmFV0DkbcAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=iBuBtjwsL0AQlju4mpSt9EpwNHRAlt6O44bzVa7XBymNXBQzIPhMFDzQMGD2KGCqeU96ammq55UCSNRX8rSWZKFUZnKkyACkTYZ5aoIsmd9GedwE_xkM9eAOgHlPpjI2aR0QSD1OhAon85JL66NlPuFPnUQWXFPO4g38BAo5kwnTEH5V3bnUTGE4iVqy9OKivDvZvijzqZ3VCFvRt6jHpXKurBAXpu7JoErJGAZJOpoP7E8njGVZBWTYZpt8u-O6Wkhb02bLz4Due_M-CvIbDNYuF9Qhw8tql_-rjerR6Hn6nxba4LNJV1Lc4YeZ4MwKMkcI8zGVcGJLNAarSRcS8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=iBuBtjwsL0AQlju4mpSt9EpwNHRAlt6O44bzVa7XBymNXBQzIPhMFDzQMGD2KGCqeU96ammq55UCSNRX8rSWZKFUZnKkyACkTYZ5aoIsmd9GedwE_xkM9eAOgHlPpjI2aR0QSD1OhAon85JL66NlPuFPnUQWXFPO4g38BAo5kwnTEH5V3bnUTGE4iVqy9OKivDvZvijzqZ3VCFvRt6jHpXKurBAXpu7JoErJGAZJOpoP7E8njGVZBWTYZpt8u-O6Wkhb02bLz4Due_M-CvIbDNYuF9Qhw8tql_-rjerR6Hn6nxba4LNJV1Lc4YeZ4MwKMkcI8zGVcGJLNAarSRcS8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUFQeiahYbWqmj9rB8jl450VzXPZnQKt8IwDUbHMV1eycci5AJQRvqwCgo078css4fLpwhqC3tLvzS4Qyktj3yjCZanuLV2_6zwWOFAE5DrOljgJxpydJZaiUs7CQvpVYGWzO-GpMwyD0d3YSYkGe_OKb_U36iWgo3tfT4y3K2-3MVL1Hz_ualIJm2NECbsbPvaOtvjg30SRqTKgmisHoFw-YII5NYk0N985wpAiEMBriekf3NHulRP6hvD_gJp8KSNtFqGA_hH06QDlDwItcocG-j8ilm9SKwjy18a3vmMWHizbK7K1tYJX4dwSci92GdVOdkvZg5NF-hXOKAri5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=R4aZrdWgd73W5HL_FPTa6XE-9sAgeKAVQo_5-5l1kXOgByk_7fGuLXw3AOIYvNaVI5nuzv5pc01IH_SGFSQ1zODZGRRU5m-JB1iMWe6ufYNQ4exGN6CXlaOdDtfUdpOKiD4RzeHLMKfiNAm5Cb5GUwkG2w_PQCQqHdasx8QcAgZ9yqrvBYRw007Fyf-TNkYhwcZEaVVi-kxiVbkB4HpAo6dhovmCCZWKt0o51OdQglGK3eOziX48_kMZLa2yV96ar0igw2o8pm8uoF8ZmLQjSqYq8A_XbR8wizX_krlVHxyZ_8ZD8KizwLYCKpMVpdG5yqAJt_cac2UheqUd2eGO6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=R4aZrdWgd73W5HL_FPTa6XE-9sAgeKAVQo_5-5l1kXOgByk_7fGuLXw3AOIYvNaVI5nuzv5pc01IH_SGFSQ1zODZGRRU5m-JB1iMWe6ufYNQ4exGN6CXlaOdDtfUdpOKiD4RzeHLMKfiNAm5Cb5GUwkG2w_PQCQqHdasx8QcAgZ9yqrvBYRw007Fyf-TNkYhwcZEaVVi-kxiVbkB4HpAo6dhovmCCZWKt0o51OdQglGK3eOziX48_kMZLa2yV96ar0igw2o8pm8uoF8ZmLQjSqYq8A_XbR8wizX_krlVHxyZ_8ZD8KizwLYCKpMVpdG5yqAJt_cac2UheqUd2eGO6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1P2KIez2SXfPBRGu0YyG4TAf1Bpm8OU-4fNixi06GLT7OJ0Fxx4lcc8pL4nhVj5kP0xTTyzDEPZPN2XAqF9hJhwdrj00ZM2IEjlZDS52Lyzf6zzSUYlKQaE_Q8BcBqPxGd8ej5oogVkOR7n-E9JaLwnpFfKEhGV8isZc-gYYAnYfoPxr_A9jxe6Zqu8y4DTw3b2hv69tZNnyztbhceQsiXA0fYDJL6G1XWnRt5_otzcn4vc2hYEcD5Hk7Ka6JJPYPJopv_pOFv_QCFZxYsCBcHsvJU9ihxdMLnLGapTpo17bmz7KZkaeKJFDAYv5Gh2-gfdMpwEfdp0YexEg05k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=jx1v3i61-lzXOrLDxA2eVaE1ioQbnq4blYyO1Jl9hoTYqrHXrbFYJqlYojHprE3MWwo5CF-U1fLCKL_RhoCGCfQTM4EGHQbIoyP7l0D0QksGYiEAd6_vXh4myZnwcqvmJ00uzIk1kTWXlI2ND7hQmILVXIRiBaYn3yAQm9oATuWRU8uw3Tefj74r-XvU0yCAukJ4bVWKVe8CwaC_qB8u219iGwn1tedf6-G_L9RyE7Qn6Vvp5yluP9M9aC38_th97226m0vjIAAOd32yNdj8tDGinMV1xAI-h69Mbt14Qsof_fvzdzihRUCyupHZC0nxGzjexQBccqdh_OvxQtBEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=jx1v3i61-lzXOrLDxA2eVaE1ioQbnq4blYyO1Jl9hoTYqrHXrbFYJqlYojHprE3MWwo5CF-U1fLCKL_RhoCGCfQTM4EGHQbIoyP7l0D0QksGYiEAd6_vXh4myZnwcqvmJ00uzIk1kTWXlI2ND7hQmILVXIRiBaYn3yAQm9oATuWRU8uw3Tefj74r-XvU0yCAukJ4bVWKVe8CwaC_qB8u219iGwn1tedf6-G_L9RyE7Qn6Vvp5yluP9M9aC38_th97226m0vjIAAOd32yNdj8tDGinMV1xAI-h69Mbt14Qsof_fvzdzihRUCyupHZC0nxGzjexQBccqdh_OvxQtBEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8EGN8SJpN9FG7lJmgEF4Ltae08irB0Mo5RtewQhXc2FHWq03u7oTfzICyByBPxMPL9No-ZyFCaZAMjsuoe3gIbBlA44eQLeF8trU4iHUhBBAxAVgcOfm4pgXMiseBszBLaP3sbcuNWDJAsb6RFItZZwhMkj9mL7fuMFmg10-vQWUGYZrev2FUiotvN35yNhwndZowNx_sjo7D0j3gshEwgvc78MvMy7e1nJBPrrHMUo7wBoweyFzBXO3q-SwgmXLaaIAy9Qx07uv9tv3HdBMxjXa7xyOO7saIxzqE_TwsG0IqiwBt-3mkZKFfxX6Xnj1n34zmEQskJ1ZpAI-XsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXqTn5WW8O9UzKxZWZI7frj7qmJEA7YL4fo-cdhB2iKWxwwD8DLL6Xad9lvBjkkoQqg0GoCEiReAl_s44sXZCyrYIw5Au1HFPSXofDGYFqdMZUg3YRo-3QAknLDgSKQPdq-HC5t0oOPhzy50ffxGdbImIsJb17XMDqk3ZrjPT4SXxODZksuGJVcr8PttPiLhQHCuIO6XVGFZG8_OlZgZ_FdVCPIG4Yjd2AU_-dZzOzFuZQKJRlhAGhuHzarDoPlhayGZJwYf7AlZQ5KIjdXlTldxJqEl2T-ZJ-DWDhqJMx382hfGxdoOWKaLj-nGdbUs0LXb4UtNVpbsEt_M1yv20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyRNwfGIyRm6EsKrYy0eLj9gU9wqPO1WwVaP4xBu5MoScJM0TZkInWoyz4QKUYjDNPrCqAPZ_glpatJsXBZOuqJqZPM384P-cyFqX0qBXsq1Ybuk3MovMmf049ME-HbrJb6AnKNl5kyUVijK2-8jyjyMD3RcaYAhQ5um0onepRV7-pOOJgLfo-PL6fZ7VLZGu5OKURCAb0a3BNAGTi6Xh9VBQIWlfiLv7ec5JBteOfhRMRxCjd0jprTt4azdyM_nz_e_DWZRhCdxXjnhO0kd57P3jEcgrL-vfjqTlTO1xDu-QoUAfCEs5ZwqcdypQw21680077tBRta5pbxiAMqRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smxxr0ym1bKg1Nv4S6Ss1KVE-Vlk4g889Shyo52mWc7VD5hDVVuDfyAzRRXSm38qrwrxZ7mJonhAzfvOVRFS-cJa5SK9c5dLvwaZyIJnmc4IzcnY3IygvUpJRlp4u-2x9Noak3fZECU443vCrbOK3zGbi7QN3uTRW4nF_mVEWpKTJZIWqSDNog-0LsNmWFhCMUFXUubfoCmkH8ld9MEdURY0tlgurC4_VFhcUZSdXuCmPqRWcwFuDwez7HgKHqA2XEHcSp8HIvw4wOqu0gmWilR_ejhK3IQ_4j2KAOWhkaFy3NfgoVGjEGgtnuyZR-Sa16CkNe-bHHA6hK3J_abiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgqwAB4RN8QsWF-hmJ1kOskXcbVo6Fmmmo5RxV7LZKt-31r9c2552T68PM8YWXn0BPvKyahVa2BFfuw83Cesry39p_o_bWQ39ZQ6KZZ9Fg9KisD1YbkjAitD5ss1OV835LhpVC07ZwIkm0c84DJ6AnjmPc0WlTI8Carq61OgltBimLFtQtd_SNsdTGuHZhS-6Cn407LIpPX4B6QHRJZ2ZM4YJyjI3oSQkM93dhPvdmHm0RU5X3cJm1Kw5UfGOatuzkx3QzNN2jVz-uL4L9AOpepOo7bSRxN8aGDx8Zh4b0236H7pWu-2GhNTenk-bRbkRlhh81xq2W5KNLo01GuS6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0eFqZMhkfg-37yVojeCYiOq1wbfcv99IZ9Nk2C1HHo4yKzcVxMQpKHWy-iO9RJf-SLU1Mx0M4VHe24jR79pj0khTwUut27kGFy0oATU_bMA45eyOB0uZYFlGNDrJZfnwiFnSD73gjABzLHyJJCwWhRYZV2aF8_HC-L9UF18H4cWHwK07fP4SawNOxb7qVTBEepsh5_VWuuZ4Is3jRvWHQmXynHZ95P081RL-ixMMG36Vl9J7BZkflbceqCb3IURqMujRwHHavWSbaR_hj2H7n7CSzv6qMzInMJUr3QoiGC4m390wfRejFBfMMusoOTRKNNxYWGaR4gpQg-RbhU1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=Ux9AQLDDOaWzf8zUteSmeBIgUTTpLOz4NSfVJRBME5hBXWRAu3A4oOLatf_8xFv2duznGRgTFWMbPNxI5JncqDy3vlzurQjoRJjF27yx6P4yaucLA1QmjqYnLLfNiPJn2Wh2-e5_KWIGLZ3-55Sj6yGir72Lb7F_hhhrCeVYAKITP2Dt1Bvrg4gWzZCbh1Y3IWkpuFNHeQ1F64cGYvBfDRWZR3iWQoYR9aCjQO0OhzPVjt_To453T1-8u2eaLnI_iaeTj1vLYRYATR7Mu9p9cy25hyQjd66Mg39QNBzvi_eZt-xW_P0SGcFaXXNgGXsaEnVZERmW6RWOUq-P2RepCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=Ux9AQLDDOaWzf8zUteSmeBIgUTTpLOz4NSfVJRBME5hBXWRAu3A4oOLatf_8xFv2duznGRgTFWMbPNxI5JncqDy3vlzurQjoRJjF27yx6P4yaucLA1QmjqYnLLfNiPJn2Wh2-e5_KWIGLZ3-55Sj6yGir72Lb7F_hhhrCeVYAKITP2Dt1Bvrg4gWzZCbh1Y3IWkpuFNHeQ1F64cGYvBfDRWZR3iWQoYR9aCjQO0OhzPVjt_To453T1-8u2eaLnI_iaeTj1vLYRYATR7Mu9p9cy25hyQjd66Mg39QNBzvi_eZt-xW_P0SGcFaXXNgGXsaEnVZERmW6RWOUq-P2RepCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUhlbfm-cIk0NGKpVmH4PU7gXNE4XUgz2bTjuI9GuVCKrrM2QQ1hYa46z3rBmAvrTC0DqbudB1saAFBh8xcG3BcQfhr9OiK2avSV6_CMO3hncRkKZmOWmL6Zm-vChaP79eNI58yanNcWMXKU3TudNl-uj91EI2hv97L-dw9SBfz-8rnMMXNa7M6YfLR9AYaakhiYnIcdM4xb_KZ2R41j40hacLYpd9xrONTI9CRbWwZ7O4g6TlaB3jSvzTxFUwMxox8pS9h7eFuFNgnMk3mDjuMqXQW3G2Imh5Z5LRrV1XBehy6N89xZb7A5r5LL4R2xlnN9mqEkefVpRS_orVrVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfOJZ7RIZXzy15uWg-i6eBQVcYOychGXmRz-nALrehrdOYQg4yDha2qnyFYDTCMSoczgwCR3BhZEHTRtJrCPeZL5HRJ3Fvy-nsZ5Z1y37JP1zaAQRuvntswgq8iNsN9qakMWr2J9DY0gaL551q0nNIMealXTTwyqYmdC-cRav89FJjbObDpuOMwzalJYQyC8ad8KXQ45-8i9HXggXLA7FzB1A7pi0oYwyq7z7OrZJ3g9mvr0G_8hUFf8gXoTG9B-knU-r3yHMHXFS8fjqmGXtdHpNtcJ1W6t5BXKNOreUZ2z3ryLWy1VQJoWgSuFhG2hMEGYB8HPxZk6t39-dEL58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOTLSD5ml9z363R5uyenryBT3fZBK-9Xz_Wa7ShYEXD0Rg5DnjlaEDotp9WnquL0a1QqZFhbUyA10NveIMNnIuDmSUg8jz2warhzemA0KNMpSF4khefQBQwhHyfIKgsD29zldvqhe836_wkqMnYS1R8rVUaN2GltpR6JYZs_baIUdm5v122dzBVv8misv3EBeTGqpG6WlwspW2lAOYC_BUdhPunJyO5B0EzlTgbJw_My2EXJ16tL3sSBAiRHIuuNtUMreRVLbp8XvISKNlkLbUapsHso1SanqksuWABWoA1XJglaoQ9aiKitWXe5C2thXoMV-_Gdi4CjoOM3rWruwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=NtUvlWO07KVueHbHQHHVmVvZ7YCdG1rZg3xLU9zUCbIF9hM9K8Z5Ybq6eEEW2JPy6tTC5wmH75M95fOprDI5WNYT0LQNtsl3pCzdTlzdeoZxoq4XNxxrRQL1wofeS3-z2WL-3ery7ODTeE4FW-T1Gx70tV8NQPRM2RLAGwN4UqRMeEkFa2AiRtUNne0DGRPlUlgw8Y-sv0bKm87LLl5Td5460WHwvcSyufyWvXiC-mzQkz_OO28UwmVKEZ-EbIYlhZ6RaLE0C774XNgUdGNacQ5Fb26Kwrc2LfA5jHFEz8PXvim7bql658Xu7LLmlKdo1oGckq4Ef_hdRv4jQSk7lkrFXzWYJ9wAqDCz2hhvHBwqmfIWE08o923PhvKDlatrAdw2MUy4__3sAbGEgfJu7Wx6IdJEIm3En7UY4pbUJFRsxvIMdRBMrWUNsAxnjibP3ph5AMsNTr53669eJbQGT61TcoaM5OnjpYtk7NJU67zA1K_yCmeH6vT3gdCOCfILfQ8heJd6TBK94R5mFBg7Gd4vFK1vN82WRTM7qv_JPpYjmUvTh5QsU6n_iUQ22LHzRX4BSk_Q1xk42P14a4F5cIMKBQk-WcOILGfiqRDVmIFOFgx7VIgMRmyerM3hfNj70A-1WI5X-vSA78p3_cMIEQG6Tht3PeSaDlEi-Vjch4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=NtUvlWO07KVueHbHQHHVmVvZ7YCdG1rZg3xLU9zUCbIF9hM9K8Z5Ybq6eEEW2JPy6tTC5wmH75M95fOprDI5WNYT0LQNtsl3pCzdTlzdeoZxoq4XNxxrRQL1wofeS3-z2WL-3ery7ODTeE4FW-T1Gx70tV8NQPRM2RLAGwN4UqRMeEkFa2AiRtUNne0DGRPlUlgw8Y-sv0bKm87LLl5Td5460WHwvcSyufyWvXiC-mzQkz_OO28UwmVKEZ-EbIYlhZ6RaLE0C774XNgUdGNacQ5Fb26Kwrc2LfA5jHFEz8PXvim7bql658Xu7LLmlKdo1oGckq4Ef_hdRv4jQSk7lkrFXzWYJ9wAqDCz2hhvHBwqmfIWE08o923PhvKDlatrAdw2MUy4__3sAbGEgfJu7Wx6IdJEIm3En7UY4pbUJFRsxvIMdRBMrWUNsAxnjibP3ph5AMsNTr53669eJbQGT61TcoaM5OnjpYtk7NJU67zA1K_yCmeH6vT3gdCOCfILfQ8heJd6TBK94R5mFBg7Gd4vFK1vN82WRTM7qv_JPpYjmUvTh5QsU6n_iUQ22LHzRX4BSk_Q1xk42P14a4F5cIMKBQk-WcOILGfiqRDVmIFOFgx7VIgMRmyerM3hfNj70A-1WI5X-vSA78p3_cMIEQG6Tht3PeSaDlEi-Vjch4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=vjjiODfZ1Vt4F7aQ8VboDIr5j4XBl98iYHtmMUsacYiT5lRzn48yweD7gdKI8YuMPD0petL6LUgW4QvBtrOp63pe_dO2qSUvXL88_iKgjOVC5EXVaHtbup_MtEclmWtexVTwIviKC2cfmuQBgDXmsgViHrpF7rAXOM5ucEvn0yy9eUJyrmjgw-is2oujMDul6zMHweAnl2C77WWncFHIenOxTChu7b_ZaqMr4A4eZg4xfBkIyBQlRlLRfQC6yRpV7y0euAC_H8AAlANOFG8b0bRgkq9fIBg5yupz12tPj1kN8E8YcRL4Ay8vfYW0oehP_bfThamJEMtPI4GNpNUcEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=vjjiODfZ1Vt4F7aQ8VboDIr5j4XBl98iYHtmMUsacYiT5lRzn48yweD7gdKI8YuMPD0petL6LUgW4QvBtrOp63pe_dO2qSUvXL88_iKgjOVC5EXVaHtbup_MtEclmWtexVTwIviKC2cfmuQBgDXmsgViHrpF7rAXOM5ucEvn0yy9eUJyrmjgw-is2oujMDul6zMHweAnl2C77WWncFHIenOxTChu7b_ZaqMr4A4eZg4xfBkIyBQlRlLRfQC6yRpV7y0euAC_H8AAlANOFG8b0bRgkq9fIBg5yupz12tPj1kN8E8YcRL4Ay8vfYW0oehP_bfThamJEMtPI4GNpNUcEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=U-fz1M01_YqGrqgUkHckG-Gpcqf_JXKifYN8RGdQDoF14vZzOkUU-bNzVuotUl5DbaxMzxmQRV55wpKD6c4ByT-6y8XkIlLZL1Jm-PXKFPMZCBI7HxRpvVRxcgHDC8ssYZZaqbQqbbY2uQ3jPx6ia2R2XpGF_HSr_ajiXZHtQU0b8JXYbG4GcEanniasvEf8Jiul3bdtt-NDBFHNjGgyWDY3GcBT-S5i8bD8Xe2sR5FKXLKTKFyjttZ7CZNBMPSke5bZTZRhc_onCtFb3w33cWQHEiV1iEoqOQsCeyVBuvNcOb0A_5bAmWVCZJFmXf8BY9i62_fR-WBbPkKd_LdHSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=U-fz1M01_YqGrqgUkHckG-Gpcqf_JXKifYN8RGdQDoF14vZzOkUU-bNzVuotUl5DbaxMzxmQRV55wpKD6c4ByT-6y8XkIlLZL1Jm-PXKFPMZCBI7HxRpvVRxcgHDC8ssYZZaqbQqbbY2uQ3jPx6ia2R2XpGF_HSr_ajiXZHtQU0b8JXYbG4GcEanniasvEf8Jiul3bdtt-NDBFHNjGgyWDY3GcBT-S5i8bD8Xe2sR5FKXLKTKFyjttZ7CZNBMPSke5bZTZRhc_onCtFb3w33cWQHEiV1iEoqOQsCeyVBuvNcOb0A_5bAmWVCZJFmXf8BY9i62_fR-WBbPkKd_LdHSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lLAySdDZRZCXdkSNuzjZc6Kcnnw4WhAp47lpc17HkESz-oNQsPwar7nxLh2dI06pacC2FJv4YGgKvN1cK6Q9C5MGDRx9M7YGHZs9w9EUi_dajoedqOt2BAOHKWU3MPUx1sWdZeyswDfGDTsCVzlCUMsHydhMnEyoeeQA_aJcuW0kSB7ZY0GPmYIL7Dqohgv-j11Yv-hVhrdotW4aLvsDipt6GmHkcXEy2KsGUbcIW9zZD5c0kah-ff3omB-W8ho6ZHG4A0BrQd8cz4wE-soj_kv9LQpTzap8pz0Gwbv_fJmGcv81iVbCNQ2e-jdSze_HqaDKWuYaqLvLy5SMWKMagHMz8yEC1myRrGsWVFR8soKEfwRasJiQNXOVFmC47AHXWGqC56EG5xqq-Y2PnLOvfobE6mz3Rh5Ry-ootO5q2UjoQtmdN5OEZdSrArM26kap5X5BsFCFXLHUaNW6fEF_yTXgcVt8EwwmqpHpjmxWOMDhGsnW1qmDCKM61r7ddIIZXcnWJk3OJRGb_lZt9AF4TzVv8BVXTa9T_agYs3ym2-JZRUKM1WlT7yBY-UeadQqVmSAJrGPsbECjR901-cgCw31SEhLVyKdZE-VDql9iPvWMdNoucpQVUU6e1Zo47UkVrl2AqEq2ad83cZ7vUJnUMPsOuasdAS4WTxOES25IPec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=lLAySdDZRZCXdkSNuzjZc6Kcnnw4WhAp47lpc17HkESz-oNQsPwar7nxLh2dI06pacC2FJv4YGgKvN1cK6Q9C5MGDRx9M7YGHZs9w9EUi_dajoedqOt2BAOHKWU3MPUx1sWdZeyswDfGDTsCVzlCUMsHydhMnEyoeeQA_aJcuW0kSB7ZY0GPmYIL7Dqohgv-j11Yv-hVhrdotW4aLvsDipt6GmHkcXEy2KsGUbcIW9zZD5c0kah-ff3omB-W8ho6ZHG4A0BrQd8cz4wE-soj_kv9LQpTzap8pz0Gwbv_fJmGcv81iVbCNQ2e-jdSze_HqaDKWuYaqLvLy5SMWKMagHMz8yEC1myRrGsWVFR8soKEfwRasJiQNXOVFmC47AHXWGqC56EG5xqq-Y2PnLOvfobE6mz3Rh5Ry-ootO5q2UjoQtmdN5OEZdSrArM26kap5X5BsFCFXLHUaNW6fEF_yTXgcVt8EwwmqpHpjmxWOMDhGsnW1qmDCKM61r7ddIIZXcnWJk3OJRGb_lZt9AF4TzVv8BVXTa9T_agYs3ym2-JZRUKM1WlT7yBY-UeadQqVmSAJrGPsbECjR901-cgCw31SEhLVyKdZE-VDql9iPvWMdNoucpQVUU6e1Zo47UkVrl2AqEq2ad83cZ7vUJnUMPsOuasdAS4WTxOES25IPec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=jgYFzRGorY5dOaV4gLpY1l_CtqJQDpqpjw1-CRMybGI3keNEekgVWQ4ZCvpsoGt2koqELZqxyO6f2Puv4Jd3r6Mf42hCecp1PtxuLXIPBd8FpHtXGNXUYBJ5ZeGdLUtvsbeY1rGRmUUgz60_tOsEyx_JYz3IhKmcUJLOs1vyI110GeJS54CQpkrGf16UBY8LyHB8Qlp-iQ9TAhbqfFDYqknmDdsHRJF1DxzLoaXUuiESUJnFsHyT-EHKd8bkSQ8bscDr-bf-U3CMDCZjKwZh6TghSAldG9NDoY9WwJkztJAcLNEkRn-645oILoDbP4zWKTn-9A3lCHJGkqSn5t_AN6v_kndHGMbRq13U--qDgR9F-c8Qhsh81vKOmrbfbHeUhzUoWQaZ3kUauCcnZh_rvxA8zQivre8XdUQZcs8WMJBLwug2oxkBwSfUGFohcucjrmnFKDuwiKi6Gv_p72oTvEO4MpxOGL6oqtoECiBtRMR7kKqpKSj9eQipfTKgCXxmxP5YU-KzUoe1DpkhnS7mdk6YIfD4Kep9H79mVCuhrlP5fUK3K4wu_IMS_TDfEjkMyPZ7qPod0eTm0A-Pceiw2vek4gPpQxdqtOeNIP39hdRwYKDe3XmaGkawFnz7X51J0Y30OnjKwkxTO9SdGX2pSM8xEOh1jmBOLATj6uaTZ4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=jgYFzRGorY5dOaV4gLpY1l_CtqJQDpqpjw1-CRMybGI3keNEekgVWQ4ZCvpsoGt2koqELZqxyO6f2Puv4Jd3r6Mf42hCecp1PtxuLXIPBd8FpHtXGNXUYBJ5ZeGdLUtvsbeY1rGRmUUgz60_tOsEyx_JYz3IhKmcUJLOs1vyI110GeJS54CQpkrGf16UBY8LyHB8Qlp-iQ9TAhbqfFDYqknmDdsHRJF1DxzLoaXUuiESUJnFsHyT-EHKd8bkSQ8bscDr-bf-U3CMDCZjKwZh6TghSAldG9NDoY9WwJkztJAcLNEkRn-645oILoDbP4zWKTn-9A3lCHJGkqSn5t_AN6v_kndHGMbRq13U--qDgR9F-c8Qhsh81vKOmrbfbHeUhzUoWQaZ3kUauCcnZh_rvxA8zQivre8XdUQZcs8WMJBLwug2oxkBwSfUGFohcucjrmnFKDuwiKi6Gv_p72oTvEO4MpxOGL6oqtoECiBtRMR7kKqpKSj9eQipfTKgCXxmxP5YU-KzUoe1DpkhnS7mdk6YIfD4Kep9H79mVCuhrlP5fUK3K4wu_IMS_TDfEjkMyPZ7qPod0eTm0A-Pceiw2vek4gPpQxdqtOeNIP39hdRwYKDe3XmaGkawFnz7X51J0Y30OnjKwkxTO9SdGX2pSM8xEOh1jmBOLATj6uaTZ4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYzX8oV3T6dQ3Bhj_Nq828hSMpV3UZizOBhwTOur9JwsCGhm58QokbLWlnthFyeQvqVemukGVfpvOdpiL0JtlLLPwQ0IskjTlzVgvzVXq5k5k5jip4XyQuGz8o5m48HFH5f81lsjLH0hRndQK-dsONYJ_-MgPwleBhzkQO8sGEgbKMcYttsx3F6c0r7NwToHa85Hl8wYKRDFWjOavmm_NUfth6lugNKk7EzCQjCZTn6umuGJt0OcFwCRlnaPEkNK20Gn28uiUlpkxN9erG-Mtyq_9I7y0U-QEbzwYhaYWnLDr8CXcsRj5iOkYZjauD_BcFiNSjewr1I3jcn87CHn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
