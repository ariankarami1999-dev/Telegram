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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 371K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBcKyuu4zBK59MLdfUOCITTuAOZoYQ0y84bbG5af_Smy8t4Aj1swZeYJPYuQOGdMyCxmKRT09TIOugGVS45rEhxvxF4UJRCkkElCfIzbZF8uaP5RtyIkfShBj1LA3j6j-d7RLV3jXLtKT0N70lXmz603Ogn3ytCXQHGT6V33R9zX2b8Lwx3eqjVT6Q4Nsv-rEXZK1A3ZJ7cL3x03QimH5WrbFXVT7pXGRTGwgv8uktQbzzi1QPKIAtju6i-AT3rttLi3G046UKUrEoTlsSUinEaNvn8xmU4y4xZTmkwzkxrnCizMfc8FRu7VVQCuTCvgVMGB1jwUmhr2yY_CpUk32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSlFoStaTyA4MFtka6b3wMlGAvF2NIqahPXqddcD7MTTN6ux7s1T1w4SgscK8Iby948N8StXeAjerhEmiBD6aKTomY8CJUifgHTp_nrBUi7hcECa73btaBtVSGOHoyylqJK3rbK5b6lvst9HrLx7R2YgaA_9gp3YNT6SmFriodwV5rAmzR8HAzupJXERCnv-6FJwLj4I0F-pF7TANHaWzqib9VTxB9wdxkOxxOoqP-WLFFk8M4YvQwlXbKuEGbwPYUlfxZXr7MJd_OMFAA8243eBlrzNZtvCL9AuJfzgxcYlBCYsh8NRyYoTUf0hh87zNvAU8iV5GNJ5VVkrfZfXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akvAmE3H-pdfeyY_1LhIbg7QDxDmMZ2riunh7LfzDz1qu3fWxvTnToRxQgylN1WS5oa8YMbS1MrhGkomezXKgZq2DYmrd8kvzuCVZoN2CInL6VKNXyptAPDEOR1CB2F6IwCtz1R2HkxkVYCM0CnKHnyjXNPCg0OCwFwLPUP1l4EcFZ9tfeXObtuDaOyI3pLYmiQe8WZwGbn-KK2q6SC1pW3r3sLqbgEWkF1bVGAWZEWmJKndM4txwi5I8CJrWHiakdMKEGoJVxn3A3CBfq-uK7rJm07haRjfl8VkMWItuyP0fGVwGuq2nDFP71X3gIxAIvlNTY7F0qHFf7YpwEofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCBLRZt8NZhnfrxj1bao49SdsmDSuCtXyjWQAtYPDVMAD0TfnFDtLnml-IEUnFVUM1D-lLYOur0wGoh0ekcnvvEaZ2G2l8oF2MGHbCoBQTSRxkGIIdHtmRTHqg9AoHtG4odME1YNkH7bV3utN0gLU8UR32ZtjYLhV_AT3U3F850Kh5D4tSW2PKoMo7lQ7tN95DFvO_Y7Mze_dqVjICXqnsCr34UK8UT1lHOWxMSq7CjHELwTRU9sm6B33zjvuDT_ICnezcr3BrSZIOOkfuakJKhXgSRPCedqn5WXDaRHgrB2n6_997m-gqyT0z_wS1kYyjcUhm7KC6U7_5mE1z-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOT3PEnKf11SOXOE7aWKqo37ZPSyFDkgLRPS5Iz3QHfHsN6TTHuegL5eNFEVfzoSCwn6QEQTOec_13I7PzX4TcjUs_wSkQB5uaIuSq0QOqF-brgDWoxq1-iibvI6YAxTuvazMHZCu0Vu_6ME2MdPuu2kZuzmt_7_5-9VsBoc7iHd8Ez59C-iO8r9HWHjC0xQrJZ_QZavZvYx5NgXNf9-gksCmTJjMqi3qTFo29OaoDVFH_nFT7WHHxawRuYoDtX8_hpJfzAottMcqixJRyWTbRhWiByhZUgcwJ3dbCDHvH5KDEEd4I7AsPI6N73mJhAQSqDQg_Zm1qKCmDkH1t6Fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83yXRAY30HV66FGWv_qtGw9hTdjcCd9IskvrY2OXc7KkpGg7sCm8evvbCNYqm5Fg1zfEtiL9dNpXzWY0ZNs8qA8mFzkcic35D9moWNFNkbtq_Qbwm9U27j841fnLSYX9bUF-sHtwBTgF-MvyBXN2Wlsbc5VUNP_2qfRCjmXUD1aFyZPLV5n7kOkeC-TqwblMPJuBFoSpGFkfbphaJEPWzJm88fzHgacVnvL1WtVHRXtOPgPMPm71UkbLzembMAOnk9UBjiP-A2hcgjvs59Tj2uPr1myZlKjVSR7DBxwA5R5eNfW6TQIR-l4nlIkS-ghMaYoVeP73skTLpjFzLTalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMrdfcb4j5sFhsnPHManqwOArAgvtwVsL6-mmgbwx_wpGtBgFp_GvrXNjpZATOatMOb3DNGM5T8lNeoB4UPbwP28IkxQvzAe1HF4i87yJ39CRqZGSb_dRH9WvFx6DesL0cqh_Mwaga-eZQgfvTNfFibI2IFLFUCpgn5LW8CkAo8WYWzm7f55e9_kpWtp2uR11UfaxAV_ak20Z8b50sHPcS3XXwIFNedUTV0lRHZAi6vYLLdxtwuesvFZ3zYOaievtZVQFPI1ulY3frK2Vxgpar5MQpU-wizB1KoyY9TeBkxqSXkfJ7YP2G60NrWUwRbqTQnILK153Cr2lQL6yb9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN75oZ5T0F-OObSMQgXqGLAWt-3jl1-egTT9c3egm252W8AAmyNXJZB-pXNam750UCfxXrLMuRcU-hZX-9OiWo-3w9DyJTjwrU0n3U_75-f3O2A59ThUIe_TKvLt-cSpMM_7YrZtj6CxXHd1pxCeltqK1hOk5p6oW__uOHFV_hgg3gMjAn8J185c_OqfoBYl7nhuGYYv3WJyP-VYlvU-5V7Tq5uWtERUXvdLOXWnEpKcssdzMSmV1iienWbc7Vpx6nBXAq0S2d_UpjywEMGcOkMbv-3zkxAZcKpWLy7dOjwC-ZzC1IQxfgUXrMBA-QC85DKzehuxEpWX-5-AALwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-WmUmdg286_cJooLu7PatmI6avX0lonYjxr-_t_35Tn73TXZkuUjAnEMdrSPgIJtSUFI3-J2mC9bMWJu0odXhxqjbA9r8bXOUH-5h16aTggo80FpqzOV0WVALqlI5_H8fWaehGA8ERLLMhn1asit6qlXBb4iN4xFmok_wqfpnYcg2MloEOxpPXsJuhiI7BZguPE4iwZUsy66nWqZhBZJFCpT43GAk9Ik3_69xwx04sxbAjCx1SitM0QW58AdPtL0ini3FdZL23SA23rC-Kan5kROgSMu7khayRr84x2acn8usw0fi6oksEMtaLWsTMboLYoVDu9NdaHvNhPkQcZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSo3WN7yzIfck_C1kuwYcswms7lJre8YEFYlAXloPOBzC5zRG1iWxxGPCCcc9WlRiPFrJNCv9zIG5sLSVUShjPZEnJSEShoea6vtahK6_fRAdxKwTfsIWIhGD4NS4MP5sC1JbxEeKZIdccJ-tRuLF2JfC8P4P6_spc6XOxUJSsR6-Uv-pXuaULyLIdC6Whus7sGvPlNidqZ61809GnqaGCQNN0A7KVIfMbxUv2ctglDtXQia-yG-zr_hkZecfZCtHAyaB5itGos2hUmOVDT-uS2oicD6EfH2Cl9T1SFfoTIM_BOft0owechezM8yUixpapvgFBdYMFarNNq43VxZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU499nIgXIHoxoqXO5Wa49KTyFxso7HkxwaKq1wq2i73IOJHlXYoEmqslAjMQdgn5qDHyJtlpeFAHJWEyQHi7LBJIf4QyPlzkbTglRzlY7NMP5Hqa0TDA2Upxxbu3_Fyx4cfdTITblAg-8_oywEfhBUp8-57ZTJP8DRncLP4YaYvkZ6ZCtITx4plaBxVRhxqtm3cH-JLQf6l6h3Lm0z6zcGmjJdLxZWYr3_P_WeU4OQqscwa6UlUKQw4oHShIVmEvHe6jmXwuUluLthrKs7jyNA6BMbx4B0leylxWQio-NRQbLaTTCGhZpfjlpKPABD7AjB089xdftCwB0cPkn3aqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LeFKsKXSfvDPHaJxqdopy6No1M444SWWrNSM1SBp-OO9LUB6--INzcmrNKKg1pI-AD4THzVvRqseEqYj3aNeiLLpIReR7aWg_umRVZ7Xgeq9HldLG7OgCDu8O7Gx62LJflIz_Scy_MTwesbYUhw3zsJQ82aoFHk9oigQyWL6drSKLvBT3TJljql-Z_b9ZThBdhEEiJG1UkIjpLhn7w2GE4nx_NUdoKePOc_al8i1P1t7dasdp79_fqS7dXwAXgLAJGpDj8hArGiaeiyoPP1IHV1kBu3hyOKiEo8US5xfMvdS6FUIwvbb5E4RD01m8_-oGNsETgRk9C5s_V_bByqH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qi-GHpMTiiZPufGI53Bv6TUpSFs82DUrBRO0XCYhE3c9IrBH7jCmwfo7KvMu9aYoJAcvf2VI9TQKpI-Wc1wKZC5a4v8IsDClIMFCglKTcHoWSPs0QElniR-_PL_FOIu06WO85bNO6Nve0Fx9AnTVZwRcRAGISPOAiR_cShH1ejCyxyFs838yHKBGCu_DTXkAcqSOIhLwOXMhPqY8ZZI2QzCZ0lqzoZNRRdVDf71dwl7zhQfYNynn-qwuZp7hPJZrmTAZWKOQvWUKNwvrr19zQOjoDKrKYMI44Do7zehyh4JlEfSjrH6hbOBuhUY_Uk9_rnh07Dbld3w8ojSl4m3-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiFvRmKeWyQgBLnI1lNS0hDBC9e70ZRehfoNfDXL04PILZjZTNeO1owBRCumuzq_e4LkYKV1kB1mzjY9g9nov-tfjG2gnMqhMVfEntzX1Ow1tMLiWXICvjYf5blT0qnwjLga3F4mllxNhdb2Degt8KRVXTkUKtjCP16BBVX8FKfKvg5QbzOdUn1fmMo23UvHjabW974OiWWhUzyV_fp05X3QP84vEsR6EJF3JvWxWVDqD2jaNzO-j_Rs2lIC3cfGggWi87bHnVNYVbeZIMVn8ezOTtmYnj9VMvyPV8RyC00I4TfPJ2lJY9WD1mZNvSnLsL2mHbeKfWAnZcEBwilGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2N_ALIaREpI9Reso6DdYLfF3Zoyh1sx8a5ZDNBYw95zYVE6Wld_coCu9bm1ozsM1-tkrNvi67OgeF5Ih_UzxLsxdURqPWwNUYQq_imO02tZ_RKsFJc27A_-vSRKr7-B7YqnjBRqyxQLlLOF6mXzylgt3A336r_R4dWPv0R7MzBYIzRf8FlyoFyD8Ju2Jr5FvAf235AHYbqWCe78jyccguSbA5JL6FetSg5cWsVPC-krKe1Oe4YyIYL7lZcZLinOEikTEHjBeX9a2P8oa1BjhPNAGM5OE2hcA76xll2BIQfGX5FhwzI8fMEuCVFP0gD1RIBAbuN21rxdEySOh7uGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaiVEx03J9FhPNFB_TzkzcKs2CHv_as9RsYdagW-PJrQDWDbaACTtpvmlqT5WDg9wn_psyEmAdKySwYqPtd6ZzTK5dQ4QjIf_IkNDS0qE193uvJpibCnYa5IGp0sYBCcQUwXm4KXI9Sk53-dkU6XosasXonqfkFpZ9RYa0cjinJiSWsl94dAu_S8MMwAqhQlgFWoo582g1mENakU8oT5bBfMNpm3q1Fj7tFRL4ZGHxhC3Uw0uJQOwmg4qwrAClW2dLq8JSmdvpVQEZ9pDp_o14kSO6i0kkbKF9c5I8W2NpPEdeJdnqwg1vXldg_QUoiaZp6InG6z4Ev3TK3ejxl1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=KXRjF4RwJr7q_kI2EMCJQsiSK8Q876MQdQ8RQyFI0ouCgcmsIgLrIRv_AyYbv0w2IIwTxqbQeQCWhmQPO6YF6BMHCA-9gq4jJrbK2DzKzxoqjfSIpfqhUwhPPRPm-1Bnmisufvcqlx0xnuMOK6pd9YGvyILnBcqiziqqVbQ1SXnKmNfBRSvu56BbLGAugbR40fKOldS-8mvOVehLsulf47z6kmrcQ4wE1PvWzCPq048RGtcJ7Qxi6DTJcmLwaZGj25Oh6nMuQ07uvFEhsVsytFQC5Y5Qf2HRRETp0rZaCH-nNng_g2cvLBCpPEcLX0hfa0SLX1-QRZRuE9Lw87fd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=KXRjF4RwJr7q_kI2EMCJQsiSK8Q876MQdQ8RQyFI0ouCgcmsIgLrIRv_AyYbv0w2IIwTxqbQeQCWhmQPO6YF6BMHCA-9gq4jJrbK2DzKzxoqjfSIpfqhUwhPPRPm-1Bnmisufvcqlx0xnuMOK6pd9YGvyILnBcqiziqqVbQ1SXnKmNfBRSvu56BbLGAugbR40fKOldS-8mvOVehLsulf47z6kmrcQ4wE1PvWzCPq048RGtcJ7Qxi6DTJcmLwaZGj25Oh6nMuQ07uvFEhsVsytFQC5Y5Qf2HRRETp0rZaCH-nNng_g2cvLBCpPEcLX0hfa0SLX1-QRZRuE9Lw87fd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTMByOO5YS1stfeqwMDZSQn7ySyd0YPAMe019LUMUibkL2-SW77IkeyI2XFDXLgOrmI4Uz8qDVpI1hJNdzBRODw3QdkeBwcpP-ZOKgR064q2UGYh97HMYt7yJpZCAWalHii753tgKvyOYTD4u4t4zFloQNyzjZJ0JlpVyfxuX56qYEahW-zj9eZK2hmicKoDJ0RJjihbK7SEl9_R80rtiqL6aqRuRr9UjaEZvnLTRMRdBfVkVz8TP0Dq_Ddpj118wsyk1OJPtRR8VnECY4--08DUz1GbcgXmj8TwgXnSeQQiTTA2mY0UjlzXc4MNMgQu0FyktSKqAZ4HV0PPqCt5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAttYyzcemLm3v_pEcc6UNReIuyL4F4CDOF7aoRfxd1H1BMacduRm9BXoBxmAVvp0A_C8tfN-w4y08yRcTUaUkOfaEMOys7vhcNc7NoKidP3NdJNXRgqJxBio-rGJ_tPZICnZu1u2A9IlJs1EWSDFaFtWEU4tUr_MnjtQumgetzm2pppuFoq9bgfF-rRYFdiGgeCu2ckAGm5tbqzZ8diniWT6P5_asRKbW7nEVBJZZ6endey4wCspnCjt8fz8viZKPco1n6vf2iEk137clgKiUnWIFCXzuz1uaD1m50jvO0amoIREH3W2mATcpNHlwJPI_DPwZZU_WwUH280wFJHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24924" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5_fdzg8sthhi5SHHVEh9unntbU9Gh3l8oey38ziUruWKzM5OXHoowcR_lTyZr711UfYLNvx4cegGPYkcerl9gEaJPNTb8uzdYzNvXPJ39q4pWjc1PKv7Ti8ki1irsm1wWCbfumdhvgj0-2M4js_vKS_P5GBB5g5sjL5bp67G6QrT5XP-x7ZXpeqjCd4gZmDkBkMcpAX5Lea0asJ1w9fIpVNMfen2CS7GGuya0UvWROFFJL6EYNvcc3vbZHf4XNodiSS5E3gJaGBVRzGlQlBXF4_aJfw8i8bVau2XzTLkDgJFMAKjKboBV8IZ6LFclQkEPWKKgqPuwADnb2nwru0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONV7lIuh71yl4tNgfXjGtkHnH99CJE_yCmvuKaGyLAW2CMUAS9Cfo-hIgaAerl0QdHlIpaflfwjGAgTWJYA5sv8k6MGjqeVGn34HrzlEN3ZIIm4il5FvZeQ3ZfYNNKRVZCN-_dPgkOVx7lsyr4SU_QSBt2Kw6E-mM0iMb7aK0YdG8Oj4f1W_8nfhKm4sc_bG5c6Q49HDs8k-3G6sWxdiBotZ3s1ca-zMVlNlyylFm7qWihzTba6L7vBqS625DjYWxTGxjemNz_V1K9CtFAd0oskCqI_1aR0NgY3IxYo9c11N8RAKZPCXaG-KGQhQHgwwOkfRhZ-AGFqr2WK-LdYc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqr6KVPM094z3ivqePXRbEMFTcq2ObjZIx6WIFKq5uPS46fnIn-rZ4lcVw8xx4Av1rvq8EQyWqgtHvdUvSD3OqmmyFqnC9a58RrPl50sHHpF8w0aIOfUUvT5tt2268ATeUBKKcJnzW3_8PYlXCwmBB-133Cw-YiGM0xAB87i4nJ_QwnpbMAqz_2_DHzL-q_zg4wjNOs8vSMYEZEVcthFXsuLD32vH4n9F9AegOCKFGa39sxNZBBQAryP98bY2XgfacgQZ_lSoRU3SrpE0TwEQVgWJUMUjCshQbi2ww2D-3dUTrm8WcPa0uTlwBTtdkOqNd7YMKy-hIEusQjulBegkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqT8oovkSabbsVfuyTxOR8Nu-9fgBhXolRmX7feBrL2QTZrFkshHQLoMaJcG_RktUm7I0Dtx1NQyjLQHpGvwvN5Th1TYGdEANCznZIHwq3t6uQFmqZcEEpc5Xn_rHBvNXCbBorNmj5ybSQhP898q5HWiqCozc1hhHnAud5uo19uTm0niEDhPZM3kJyhVaxfB-zroHBiNEbp6S9jQVtIOXiB8JegiajPVHLRcQ0kJcxnotZpKY-6JOD9VbCtZ5hhfSpL0NB6R8bTDnLqjViTO6LWtRN7d7r059MdMit_7XalQDtk374UoMRKyK0XzB6Zb0iY1ki6zIm7vLyJN6Nq0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvFqmPzY39aGU3AjfqC86cze7-0yZPiHnTdunKC8hi2B7CICRCGtgWiCys7xmJ7O6W4uSTluNRptsKvQ_lB5IQtQhY3UbiuRk_AJxgZOsVZhCKuuZmzgpn4Zf_uVGtzNY9b4DcKY6oQHaeF7_Ae6ARZyegFH9QnKQue-mQEMEgjl1hcqMCdmUzvfeoad_7w6T84IEIQ-kIQfvrM0_ouPEr0UBTjCtWaBhe321U2xr4mEhAAkyuLvgqd8db3uJ0iHzePWwUvK0WQTZ9EAvvkZEIolY0VxSWPVMbiRrgyKjV4lr9N4Xvf_rxcOm7DMRwsNJyu4-kWJ10mxYyZJrkYZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=ukBJl5Mmxl2PHO05fhfjSItyNngg1EOhTr_gm4fahcNxNCBGC0wmDfa1x1C1O9bc0UTRqvrJjKIFkNxoJ6V7QINF22kDwYCAn1rFqmgWouboySp-GMKDwloqhNn-z25kc0CQxFMzTmzizzrg5iMHjfm_dqbMkVAG42ZxwhjOoMlog3H-tl-JokBXYMBzarab_U6keWdGUtdEV5rjIDQ9zX5usdNj65STwvyq-Xe3WwP6TqXJRuPWL2k8H5pyvFNpJqGzwTLNSi1iXQ7tc1Bej-1Kvk7Vc5BxBoR8y6AxhmfQPut-RVgb0usp6KTtU24iChIY-DIAqHbgIWcoWiYN2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=ukBJl5Mmxl2PHO05fhfjSItyNngg1EOhTr_gm4fahcNxNCBGC0wmDfa1x1C1O9bc0UTRqvrJjKIFkNxoJ6V7QINF22kDwYCAn1rFqmgWouboySp-GMKDwloqhNn-z25kc0CQxFMzTmzizzrg5iMHjfm_dqbMkVAG42ZxwhjOoMlog3H-tl-JokBXYMBzarab_U6keWdGUtdEV5rjIDQ9zX5usdNj65STwvyq-Xe3WwP6TqXJRuPWL2k8H5pyvFNpJqGzwTLNSi1iXQ7tc1Bej-1Kvk7Vc5BxBoR8y6AxhmfQPut-RVgb0usp6KTtU24iChIY-DIAqHbgIWcoWiYN2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbvUgXO0fLhY2E6QACO4B_Jg81ZGtBKEQLYWEXYxzNOFINkZVxzyMXcNNILivNP5vui4t9I2Iw2hQ8z7ChiM0yYCFUNajIXLej7a7qgezcI0q0ECFhJcH_xJLthjihe31t8gGKm5p1aPqHrYuDK4d8eO2kTRWZtjJkSIQFJ5WAdeMyqsYIttCs9pefxm4TFsh2AbqcH2LCGDxZ_TtrgDWVkoeWyufiv7lCFX5i01ANZOcYVpOAQyy1ImQN_9O2Sog0uF7E81c3vgnjz74BdxUy7eoTgwSk78PFARJt6yQsXuRxBigk8NbrM2YxwpyqLMwL9n51-utq51otAQIaccQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch09otTrs-ZrUkoAAgH5qSYFfrAhHiG1lbxlPfFKmr8Y-AlTLewPfGHshJ6GjoKazR_dZjKI81TkqZhGGStCpP2-reaCJ6CAdlCMA9YvtpV8OMsZTF1nYgMvyZ6-FsWf_m3K-t8AHluDMEurwb8TD2Bb1bbEY3bGTvHhE-KW6xuDCo_P14ho2gxXjklfi6__osZa_YfA-2VrIKMl7SMnCoYUBRhOykrVdnUOhVLZyj5CgMvHG2Xgm442U6Qev7KBzNt97UR3rMiV8ddfObsTUZEsF_ePH0lfb83jYArXEPFM_LRoLBbpEqcsO54kOA5RIyTYr0wHMc48SuQPWLt9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=RXkwkNCq1WCsPKkQ-Fz9e4JYoKmVPncrLzhgz2DMsLPUhxoOJToDiFiiDOLrmyk8lgrYP7R8LrSC2cFWF-GEoBJ8VfQuFMaN7mORML-gFdUXgoEV4ByRDwjzxsCfSdCEh95tk-dj_Leo5M3ETx9pQJNB7pkJDd8Q8kJ560LMT359aGwe2hjpXVNulVO6VoZ975lQI-ob5wc3-j3J_JSqNSUJrSEIRITwdOLy4DmFThAcbwgUIkwVv42fRmtBcDREI1QyK3hHG0_Y4c9zW-klfviInJzGIk1p0Qytkp-p9wFL9-9BOMxvKt3AtLOXOklyz4wspIja3f3cleh8-LDCxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=RXkwkNCq1WCsPKkQ-Fz9e4JYoKmVPncrLzhgz2DMsLPUhxoOJToDiFiiDOLrmyk8lgrYP7R8LrSC2cFWF-GEoBJ8VfQuFMaN7mORML-gFdUXgoEV4ByRDwjzxsCfSdCEh95tk-dj_Leo5M3ETx9pQJNB7pkJDd8Q8kJ560LMT359aGwe2hjpXVNulVO6VoZ975lQI-ob5wc3-j3J_JSqNSUJrSEIRITwdOLy4DmFThAcbwgUIkwVv42fRmtBcDREI1QyK3hHG0_Y4c9zW-klfviInJzGIk1p0Qytkp-p9wFL9-9BOMxvKt3AtLOXOklyz4wspIja3f3cleh8-LDCxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq3EpOi88fB7JX5FNH5sEDbdsZsuMAj6Bm8pBZu8cI-asFRPinfKdAF7ZNHNBZecKpxBQK6SMYD0Bbq3qt9QLY42pDl73uJDc_v5MFCWZ5eNFyH0y2tznGKTTHnoikTX2rGQCt9WR2prFNQLfCVfaeS1SjRR4WNGjF-mVzO6D4ILVjx0bw8WZxC_LKcvQFUyw-1hGFF0ux6NLz2NSIHOYggC2LzcoNRwooYU4n8Rquvv7ibDX-QWjPLDaIqlsZso5mzhAMsMUxYQu_Iufj-VMRmBaSw6BWy_MMXgfbIVMGjWGhNm8AP3Fik-P_L45Su7bj16gYcQybpTfcM2lLH6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_9o2vr0nf8_J6yyuN_2wrXF7BrPF78XFsfD8jFSlb4RT-PxcWVt8CYVFe8tuzLfBUccdEVVPBQ5ERgcRuPD3oWpGLAfk8XU2laL-keZwBZSfS20c2fqMM4sSpbDlP9Fd1OPGdDhJGfwN07JT7aIqITLzubtiGNDuOHIlH_qrKzTxedtWFsEPvz88X4qT32S3I4psxVl6KY3SjiUfpJXGHi2KESlU0_z5-lPtK-FwOe--zCldNkZOAczp2DcerFnRRRzKsZLO5MuZffd_CK0FJ-_DQ9u8csJS6zJTb8te6KrCjYL3tB7OQsYb6PZhj1ZBI5HcqIZuuwv2e4NmQ8jUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Btnp7qociJ3Xx3Fgr5TjXpPj4EVRrVjMqc0xcxzQz5dWwL1MaeWsSqR3yBVwo7iwb2QP_DuAE-I56aBN8eQekKdL7YfmreFHfO-aB19O4tkfXAbKzGc40ZOT-QeTySE6oWWtNKO1mQA2nRYWviLV-xPDAYsW2MC87UqLU3Tti6qLkOwA7ZiXjMWOVIphFfaL1-yAqot8wFROAoLMs4xv_nTPFC6lHx58g1Hwc4mWD3jvErSe8_CaVfwolIF1Nfk9kaBegc1HkOkUy_Sq8WUM46gQUKAd1CGjz1PHuHgYLmAfHuA7mH3aNZxQUnIyNMaK1ppw0Lt5216f2_KCKM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2H6ab8CO1BF7ygnWgXz00w4B37TeFHKhEl1qY3V4IHquiiLI1buuiKMkp4_dneFXHwyUa1GQfb9oda_dIHhkzNnCoD_2MBHW6YQq5V20vJuVUZfoLH3UXYFd8IpMVYpBE8I_eIVFdae3Fez78CFlk88Z7IcUKNL6TX1aVMhK8kIB248CQN7qq-O2JUmbIcCP9ZIg5JecsaHvTP0pzh5grwGioEEYOPHS_YEuL5_qA7g5mBte6ctAPrfVPaeTPGrN_6nssOvq06bJPld57OYtdYyH3igGPJWy51FXjA4GPi4DCryc5LP0muoq9VfG4Zq6riGzqpwvuT3YX8ywEx5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQKyx-ufzrIhcUJIoti9o2sFwL8H-atjYykyKwvrs5OaKD36-w9iDO6OARZJ2FsxISgIentEHIbsgGAYjCUYJNUL66mqZKWmcP6FdddA19y5KTQqOtnzt0V89eOF_cmnhfHcYv689UdNNnClawcyfLXqB0O17shin_cjIlJEQ2mvgwAMBqkOIKxxUj4V60TlzUX7exGpkJZoXsLEe1FtlqN-wHgYg6hU5pShiKHyCwKnhv5o45kIqlf8CkSs-ETpZppXc1pzyXDjC10TrH07_I4BeqgkBQsVObthxr-e-gbm6MtIGUnbQMWWby_r7rely5EBa1UX3j0IpjDKCeJUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=SHfuuHOK2tnCiSTnPVX1Gupxh6P7L3KXH5UMlcHevwdMD1CT-_Fxl3sBRPV4Xs7sP36uYkFMrxQ5P1tJloa63tZXXJX9S5rVYqcogIKRbOdqXyjY42ilawq-zOW_eMizbEinkxPb2tLTv1icey5Xs5yLJtk81p0IQTT5_IhHIU2Vfh5N6-D3SSS2pTQFeI9qBXPWU1WimOCjb6Pptnor5zTfH71Pu564xF3hTFhv35I2FHc-Y5ngkvfS7E7tFLXxQ6jnm2IKJlhi82Rf53f5YKv5wWhUWKvpgXR8d4f9C88VJN7ttrJBDelaurdjd91ohxbK6caqdxjW4YUJ_r8a2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=SHfuuHOK2tnCiSTnPVX1Gupxh6P7L3KXH5UMlcHevwdMD1CT-_Fxl3sBRPV4Xs7sP36uYkFMrxQ5P1tJloa63tZXXJX9S5rVYqcogIKRbOdqXyjY42ilawq-zOW_eMizbEinkxPb2tLTv1icey5Xs5yLJtk81p0IQTT5_IhHIU2Vfh5N6-D3SSS2pTQFeI9qBXPWU1WimOCjb6Pptnor5zTfH71Pu564xF3hTFhv35I2FHc-Y5ngkvfS7E7tFLXxQ6jnm2IKJlhi82Rf53f5YKv5wWhUWKvpgXR8d4f9C88VJN7ttrJBDelaurdjd91ohxbK6caqdxjW4YUJ_r8a2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVX_51PuNsmVw3jiVq3pumXwBZPietDO6S0SOs_eDZrm4kVfFjMvw59kOP-wXKMbaG8sByFXJwiXHe71kCYmmE81JGwhWnS1PKbLNKisHfUI32vGbeJZAEh2n601EJ1hLywTySzj5mXdCggxmWeexeRCZ2Mvqc8gRsiP3oOU5N-Y8oxAYZQFIWulPW5fAo87L_qpk8cXVwQr_s2bGf17WG19Lcwed5firaXT9WKK6tBTmklIqaVMXZi2QPqEO-uPGbEjiWUPUwulbDWqKP_UGx1LQI0Y62Kbg0245H6NUOUOMUMVODDVh949sCJ1uHHB3_x9sM4dYe6xreDJ1Jh9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5DO-yTPnb5lZHYh9g68J521jJyAryJ0lD4S8Dx8kpefYJc-pXNn07RhVc2OkRRVPRPSx8IwYvp31RGmVHaetLE_e-woc0vzxHAGmvVDbb5hmryqCvvvVfvHu-9TwmBsF4CG-rXtI_pZpUGMsKm88_GNZAh0jahF4mCDh6kSD1SWXQNQq3Mduxzya1ybJzml1CWz5E8awbDN3C1UE7k1PEdGT9hHVS9fKjtSbu-TiJIN6fROubkz88OZoZm19FdubVMXC4Ax7Rs3Kei3-GqMvQ2NEU3nR_xggTEx8APR-FC6-tL2h6TWhrjXc4VKtFqHMMUCIKS4Ex0DRq2aSHGhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7KhmtR2Jib0EjJTtk2_16atxTxR6ULtp5m5iFiz-kB9kQruvyKfauXQwWl4zQF-RPjGDdzGDqdMKk_gDh1yQpWRB-nC3D-PFhqr_51cltf8saf4LHQIHbWSDdkz53Yky_UGxoYCaBjsrPIpJO9dABPtDnJaL59avb1UqOQxA-D7lQaox-fL0Hxk3IPNI5-3X297ahPsFb_n-uhCLpB3V36WTbscJgMei4XVCEpXA2wGhErERAeyYrCpUb3nUgfPdA2hBUzvX9XwpbhU-RfvQW-vH2uMUehnVh7ICVf0y8jfuhGXfYnI89PF3sqycpMC2JUoA92o_fI-LFMoLzE-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK3nzAr1WaYgdb3pCriv4IeyK5HY8dWs2fhaWdaYcYja9htkGKYwB1itDFMY4EkvLYGFRmBMZvO3uNGsnjVngTtUvNFOTW5yJbMeH6xFZ4zl2fZ4FBa7-lH-wQhfiG_caPy3TKkbVpeR7ZmTLRg-V1NuseNPzRUH5hQjsKZu6GxODnu0f5OnJ23jdOsCqM21LrEejLblCC8scJG04yQF31Ubj-4Oyat8Kpjf0F3NrdEmBiewx2S6jP3-XTfzoi9ZYC7G6iD_MJcC5a8ljsGJuSY2OcxfGFpG9R7mNk4S4wB6J27JZtY0dxX92fQhtePeksSOuvjo9dHUPKJMGYdd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOcbxztWRlgkc5Bmg2s55ucbZN3zAk-TfNnzdXPpboj6dzY_U8hbPI4JnD0wD2azbhwzztbVj67Hykx4qTARSGDjIwLFRTVVv-Sk_U-9TcLDSYGsU_Ao-1YhELPLG-5KoO30onYCIPOhy7U3pJGZYBEBiM08CgKDsxAKIWdqQ-E9-QRbKK6XPg2ir3pI3eO7XSL553wY9TpRLi8sBxlerPTRLS_UwJaNnfeETdxcIZswrYoBiGYVLb4jDW_5cYDzy1kwbtWQxKfcSfndvq0I5mjouLv0h3WpXjd-6goDhl1m7-yJ5Li8rl9-r82bfK_mXvmcBoY9f5A_DIIPuY2hdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXKQiy6aQq1GPz1LnaxF6u1hR_OO0LmAqorJrH99afC_IbBhAAVafeneDP0IkIqW2FNuwRHNOI0526SY4wlbRssid57fNLnmyzJp_gGngK0pJZygcP5kzkBQh2p6OhtEv0zPscdctgEtX3izlQHHaxsIfvw4OPC4p57oQjWTJyN2BcJsCFYhPgC_FJGQwSq3kRpheyhTisLNlz9w3LVlAp7OZ-m_Rpq0WHpcaSkAMsoTfsceG18xcIl40TuUqjPM66lAOGq89JQgJzojhfezN497oqpKbd1T3uGYsxv5_L1oSEnJxXwMn6MBHvbfSi9CD7Fh_LRvxEh7zKM2JKQe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=d7tWF8YkAZi5Qjph3VOl_VhqzJB_59j35SuxxZxAbFYIbwlGlE66f7j8RHrjFHsQUsjLnQUjQzcPGJ9w8m7reRiF03exBGNmTtH7xt2XuUzRqc5rrr9VAEzeHABQeoR8OIpnBPbqMskVobCXJ3wrWZgyXgYPVXstxcB0S0cZR10LC1HbLwDhrbqCHqQzSKoY7YIygzs_mPqLRuT0zZyiyE2tnAdbTmsYDHguX2yRMfngoSmNGZJu9GQ-vJgnLgcf4j8SQ6Uf6jOCO7q6tvACV4DsHpJaOkFR7bygzKm1UYb9BLB6lSK-IIzbCN0Sh0orgZECvwRf-PpieGJUDxIXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=d7tWF8YkAZi5Qjph3VOl_VhqzJB_59j35SuxxZxAbFYIbwlGlE66f7j8RHrjFHsQUsjLnQUjQzcPGJ9w8m7reRiF03exBGNmTtH7xt2XuUzRqc5rrr9VAEzeHABQeoR8OIpnBPbqMskVobCXJ3wrWZgyXgYPVXstxcB0S0cZR10LC1HbLwDhrbqCHqQzSKoY7YIygzs_mPqLRuT0zZyiyE2tnAdbTmsYDHguX2yRMfngoSmNGZJu9GQ-vJgnLgcf4j8SQ6Uf6jOCO7q6tvACV4DsHpJaOkFR7bygzKm1UYb9BLB6lSK-IIzbCN0Sh0orgZECvwRf-PpieGJUDxIXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJeGEawKlj4nEXlU625b9WE0HBkiwfusoSLlJPTAknCv3IDg7SfgYfGtCPeP12R4SGPEU8QU8aMl6-tvV5dhcQsJ2Yx8Dl5as7NcxdZ0v3mwJeutV8L_wClc7eV8VKoFS02pJrfIRuOSmO0RghWeQ-e6TNikV6K6Tk5dASigSmsN13fZlKXoiBcs1KJfmr8__HXhuyCiOyb7jjGMHTbvVTFEVGqDOzzWSYPBeOaVdsyoKi3F9iQSiN77hUctOZ-o5qBwLRQVWgINgjQnEi9kzvCe0ZV_vpDtA44vdreYDppY-W4qeQ0liuRG9T0MwGBU0GoxHV7dg81SGdXeqdy9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4zlbnQUJBZYugFfdIS0ExUGn030Gp-TWiDPT2BD-f9TrOh4A-KhEc6gWGINcMwUAYB6KFBv256x6tQaEaezhf2EHej_1v03OshdhvifnfLzJp7TdeTb63LIRjcX7m68Pcox00aIdl8LwfAJjMQqrq3A9wVM4TVA-_GB4NdKTkR9LtK5CcrruTSxfQcf4szM3tc4fibc1ApYQSz8aVzjRMJD_2t7ofLJIdOQ6cVsxmbpy49x9d0XvCGU1HiFEkNe1sPgXM9Mn4EG-MwdxCg5aBTfu3Vnjb8VRXO2FfI9rSjFlkx2vk_8_JoeQMJSeTkRLaAJ_GyzjHZ8gIH76Rxjew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLc7vWh2cvPmRRoVXzUvik9kZXpi5Z-omC7EhNPd1Tg82g9mD5rYMK6x2wlCUmWMrRRV8Y1_p3_QBJzxz0TQtANROdTRjzAtKt4G0dMKANNHy6agNC2hhV6GvoUHyOZbsqfJUdrcfPGJtBDqXdYLEJ8c6IQxZTtf3qMNQJtJBcR9CjR_QmUOlY88zeCKJ64Wp5DUyG1FIFKPTiBK6wmPp1kLRXW0Hs7jmg2jBIC4ifyzvwGqlZa6H0TARfxxePtWAiloAEdWQCcvakC-XpdvBiq5wgd3wAvW5Q6OwSqyRA5ewVZoNwsJGxbQRGcUYgpd09TOm7Yj5J0bFGkp8jyWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBwZQuMDOhEEt-5EnPtajYw_EGDbyT2LgUSxtSWT47YW8suMZnYlg__5ZrvLREXoQ6O9xMcN6JSx8ovXeChh9BWrXZn-StJPJz9STeqjhnzLbJMSjaXRXly5RmFESAdphAdhs5Mh0k3xTkAeTh14ll7przqVGVk6esSAzL30P8seHiLZoHshzArGCrULru1xB-Lpx3XhRjZzwxSipRZ__RJkFgVUgokAcJRaiUCflzQKy2yYZ6EKxJFc7Ntew6s3oOurVT7v4loGthUmt993dCaWg1F-DYA2QS1LCqt2u7w5c21XKRR8qWNdbQrJ6Evkdxg9oe8Qz3PFt_51H8EP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfUncpVyQOlmPktJA2bO6_05P0Soubca66aJs4Vh68amHsHlepGVgQ3wHhMCsRDuOxoYSXO1sV48B905d8GnhrAFhRSGBFEsu4uvZVXaCJ7TAG85AD11DgIv6Lu-0VW63YTWMHzwj_kyLueG31K49pA1EGGryIVcbWltlzVKGzRedfMKJuIQHjRqiLsKo0gwR2r5haMKTa4crX4motLOviqBVq5feWmjhay7RYhux1YBpR6yxxF9r_Dfox7uyzprkPEDVwFy52ycxQ3LnQeO68hAQpudZYzG8m_fFK2hK3iZLU4zta2aw_zPdU8a9v8McyTdZKXvgPbQzx0jSk9Pyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1G3VA-YWfBwpERlcP0xFQ-RyCbaQRmxsBv-uH2sP8Or84659Dffk_lBrCZ26otedKJ2tzHGUu6V3CBolE9-GeCI2SPDsxjHenaIz_vzK_qWFKdSKAKF2ZM0IOqV77rwd2muEms97YvKXMERcY8uZPLgtpyHb7Gi7CN7NK-ymGabOcA3HVUbrms2hC0V7vdCGZBexQFOJSPV41F-5bTruQvbgS0pdKksEV2ryP_1O06o203h3gyZdlaQdkGqBoOUY5tuQ-0sCfQYpdZlxI4uwFudy7JmtmJndRRaxustEIl_ZqYr8R_cF00pQVq4yHIVgW2ojznjtlJ2CNQiBcqoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZM2t6tNSN8NhNJRgH2P-FYe_KVaJmKeIx58GJPdh2bBdUdFP5lsLkimx3RDDA049nByfJ9lRczASKxf5tWaHhyefvxDbCEd3RViSiQ7ruMED1QLHqzW7WLWxCCddaP-GQ5JmkYlGT7aOBZTSSGrSP0nPTmIfK_Bo5-fSKU4VybJEAJ6oktQ_Erur9Hu8qLjHfWE3e47ccQLrbmxsyCOaSB43YRPYccBGX8eRvTgvEa7MXrhaAQqL91ZM9-cRM_tN-VRPekJAEVviCC8uOdUiriBQJJD__pG-Z9jLDoBZtLyd_LDKR8I8tBcq-XeLtCftOf2cV3FiPEybm8OewiIzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooh6sf5HMFWYWqIgiLxqU3WtBf_HdjfZG_q3sP1Aqp3pKfKIN61QVaU9cPUCZ8KEsHi3pFuKwNCSwg0eqtII-InIzD9yEajPH4DJ6FFT2LkuJznTHtNrFc0MbmHl-X3aDbWNQLn7VR3iJfh-j1QWPAcxj9IHge3No9pVncCXKO46PqGAUROkZLq0Y--Rc6JQltlTo5C7hY9smfQveoipOUfyNNVWkdBcuLwUZUTRLSM0OGvfXbniszLbdB3vkTNcWMJqWdiTFnarBHINxwYrvfxLJrYxA2PY-vR_MW2aLdC8-_WgVk2gGi33psIacKRLvweh6kAvmaBhUCXCOxBdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=Yes6iTwJ_I9aHIWI_HBF2NIwMp3bvV0sHhyVt6tYnfABBTmzEwP6eeinN99d23SgE7r1HIyKGTvxvS0XPsS77svAAdep19Myw4atDtrfFnpM4GLw9bOR60J6mQmyY0sa7qg4XlE_By6fNCVHsQY396rmlXl6t8cf6FLdEQugiv_ho8m7mX9B9l6SvYO6spcQIhZSjaj_Ti_qpkGUokRS01qFPuhZwwjdyMyHxczo-XyZjf7PaKalcPDJZ_huZqJBipLFyl1bjjwIuw5gzsEBR6VlxIbq7ZaAHCzHlpLmAF8oebBbIs1we17I_ZJumymDFLb4LcvpPcPNC7xvAIdCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=Yes6iTwJ_I9aHIWI_HBF2NIwMp3bvV0sHhyVt6tYnfABBTmzEwP6eeinN99d23SgE7r1HIyKGTvxvS0XPsS77svAAdep19Myw4atDtrfFnpM4GLw9bOR60J6mQmyY0sa7qg4XlE_By6fNCVHsQY396rmlXl6t8cf6FLdEQugiv_ho8m7mX9B9l6SvYO6spcQIhZSjaj_Ti_qpkGUokRS01qFPuhZwwjdyMyHxczo-XyZjf7PaKalcPDJZ_huZqJBipLFyl1bjjwIuw5gzsEBR6VlxIbq7ZaAHCzHlpLmAF8oebBbIs1we17I_ZJumymDFLb4LcvpPcPNC7xvAIdCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJNLZxfxYtWtSWYVRa_fmS8IaiN8g81YQ6FfYxYfe1WmUfxjH7q5XiJuC6VZm2i5BzBcJBEGLZlf1EVoPkD5LLYRIluQDEb8g_FTwXGEfVpF0s4zAurVIrX02l4n2Pk3i5plcFcBM4yNJvJOh-TXUWuFRuib81xx3fHBzhtMpucqzrGjyehlf70H3I0dLXFY172RRVVlxbPMZaG-2_7n8pSm4cAskC9Oy7zFQO3j13BEE69EY7vZwRi2oa9DSbm5kBF_L0Osbo_TXtLYVqJOxRjRk26VGI2acDhwM3eJZDWTd3zuJIHrlSsLORd2hY7xK19G7unCJ1cvR61not5-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyxbXSmdwt_Kbi0a0eJN3XD3oJFqxlLa0MSbD5L3q6ydZpqJY-5mGgfUrSC7utXARf4Qqlf2AMb9wvnZyEY3JgOdFZPEmDedAEWRmwqIcTC8CzJzYJ4GDCI_xHoJ36TvEu7OkYG1yWH8C9UrR5g3mREdmpUItcbvbioWEGRrVEF9dSpvUOzPSK4s8210ucKq9ES2MerYvXdGEKFzKwM_v6yKo9nLH88A16UB7C7X9ksotEQ2n_fQ8_3bKJ1Jf9qaQ7dpXSkFsFrQTkh9EErchwt4WPl5UqI-_FteuEmHJ_S5y5ehvNcGRf6PUBhuEk88uL7201t7IFYUFRTb34cleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXiC1fSpG9XGIaS3sAablp2SmPYkwWPj9aRg87v7K-M4L1xany7H0E3KVqB7FvtuUWxHsP8DOtByVNLghXr8-3DTPn9r_9wQYSSSH_mLEhbWpEdY5ocJqeitmbV0uy1joj30vnmGi6RDLzmUZibXneOT2ILQFMwdQLAv_scBtCr-mwQr-H3UYCwnQZPZQvK0Z5fdK8JRyPxf_wKIY8fdWLB2YzaTKfKFjylbJKo_2JBY2ypc0nFPnxK1MAx3IOMpILwXxigztV5NPFCw5g21vbcwVE48_FZt_5W4tHjHLNhQhMLxUAQL86GkmfW8XmyuN0DbWcGM0CuWYlUtEgl9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=nlyFV_qxM7J2Q_F7nsMxLyitX7UqOA1V8si8iQxOoLE5od9VGyqJ6Ue9r-DQNwaKL5X91oa6IkQluu7rDu_9PWCvZnTqUiXhWUk0CwzWQkjU20B-3jekpm9RD_F9gVFw5Pb3HnbbS3bcCt88eSJYLcn3PQCoL10TVIkYFPrh4Ew7Qnw6Ay8xxr09UikHqoVtJqGj87dCtBRMmvROBtXefvHrpyMlfRQHSnpUguacxD_Bt-PmmO-qXH_w6H-AFqJ6RChXuXckKwXpd-w1lGmV0iYOlQfNHxFZZniI19LF3YOUg9tlsklB0LLKiP70sit3O8xJ8DURbsiVVv9t-muQPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=nlyFV_qxM7J2Q_F7nsMxLyitX7UqOA1V8si8iQxOoLE5od9VGyqJ6Ue9r-DQNwaKL5X91oa6IkQluu7rDu_9PWCvZnTqUiXhWUk0CwzWQkjU20B-3jekpm9RD_F9gVFw5Pb3HnbbS3bcCt88eSJYLcn3PQCoL10TVIkYFPrh4Ew7Qnw6Ay8xxr09UikHqoVtJqGj87dCtBRMmvROBtXefvHrpyMlfRQHSnpUguacxD_Bt-PmmO-qXH_w6H-AFqJ6RChXuXckKwXpd-w1lGmV0iYOlQfNHxFZZniI19LF3YOUg9tlsklB0LLKiP70sit3O8xJ8DURbsiVVv9t-muQPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJih2WQhsMipPy6lueQ-a2Cv1t5enykuG6maV_kiDoX5CU9dZYhLqbP20iMpUUepQ-132enN-zAc58bazvnAdPD3wBqlwnSIrqMt-6Rk0_xdEAEQ9fgKr1frmE8MDvtmr45xDD-UBf6jbn5cvyE82GRoh8a1p7fl-ZJrIKbq3llaXvuPRZsGsjRzfAIyV3YMccwlaIBSzED74J7FHl661LHUZ708KgFHvb3Gr9eRSGkSKdPJObxTaTyM5kyd5cj84x7Ias3En68oa8wB_6rNNor-WYNZeEzoSiro3TdL3aWpYG3Xka_49ZuMsaYaPsNK-LSOs23BwwTvfWuW0qFMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=rlS42g8zrp5ShfsC6eA9LpzM2v8E_NLYijBahOkqibkZYXkfZF0vKCnb_cZwItI7w3PM7SR_-1b_Qx4GvMOvdLlgRQS_ukoDs1rp3f7X4iXxuB2_Sqn8t-uYBb5QNEG2TipBab2IWQfr_A7OWKlXKUyIK2hrPwcy0_0JnpR4qDgEuD-li2lUIIV2bPH4eP2zkXIHjcWIhi1ruuIvwX8jZLJdz9IDb_WWSsQnSz-phzgh49gQpbOoysWlhnmaJc3OcSqmQpOwWvLXCoaOTjYnsMMO7toSwiEmgnWSHPOZEZoyqWOi7kKaiiOTNqHpVdXsZZeq-P464Kk6qUBx6A93MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=rlS42g8zrp5ShfsC6eA9LpzM2v8E_NLYijBahOkqibkZYXkfZF0vKCnb_cZwItI7w3PM7SR_-1b_Qx4GvMOvdLlgRQS_ukoDs1rp3f7X4iXxuB2_Sqn8t-uYBb5QNEG2TipBab2IWQfr_A7OWKlXKUyIK2hrPwcy0_0JnpR4qDgEuD-li2lUIIV2bPH4eP2zkXIHjcWIhi1ruuIvwX8jZLJdz9IDb_WWSsQnSz-phzgh49gQpbOoysWlhnmaJc3OcSqmQpOwWvLXCoaOTjYnsMMO7toSwiEmgnWSHPOZEZoyqWOi7kKaiiOTNqHpVdXsZZeq-P464Kk6qUBx6A93MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUe20oBz8A_vV22tn6v1xiMVmxx_qXlCTKZNzU5PvMtDnzVrDnbqYkpUHADHM96_KilFj9ID00N0lo_9l1kGfRegYWuhHgv7YKW6YUBzu5Ubdml3i_q3QqdAuxT2NEBK0XsBWv4Pxa9M32P4oHBj8TyzhbRMJlP_W2xkn66pf1G_aHecjo7rZU2vGZMDK-Dqd72ISnpJPegmlOfPRz1bhlO9gZDm6bouXZjr9IiG6Awjo1DXOyhYRpspDTeuw0KUHU-D5uq4wuFCqtkYgtGV2ViLV3ViugLUdLpfPXycqlmbkPq_xHIJ03DG7L3MLtPT6i72bA_B1mhdrjXWLqd-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=iZj3VdL2OJOo3FfjimA79lo6UQtuR4x5jEPnuANbCeBHDvtIXxMl9X4RQDu2msFCFPV1YpBw2e4GoKjk2s52rlwy2-m0TgPV85bxamgq7wRBElX8jrJ6XC0KY-NmvWyU9Hg8CAUZ_ghcFN69585ySvFFtPTC5RrYofbUJ109sNaqW-pZdtUSIFIreqwllsjMV-dl0pE33aMlTAjD-zw7TlXo7RK4VULbAr--ZfY5jY3Tnuhj7EYcKD-bu_kzaowmQRck6N3OyJR0UtMbXMXwJaN4KYhHX7p0VXSd5HtN4WDn9gNelkgG_LU4y6ug7M79m30feAlu8-b0Q0fUiNXERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=iZj3VdL2OJOo3FfjimA79lo6UQtuR4x5jEPnuANbCeBHDvtIXxMl9X4RQDu2msFCFPV1YpBw2e4GoKjk2s52rlwy2-m0TgPV85bxamgq7wRBElX8jrJ6XC0KY-NmvWyU9Hg8CAUZ_ghcFN69585ySvFFtPTC5RrYofbUJ109sNaqW-pZdtUSIFIreqwllsjMV-dl0pE33aMlTAjD-zw7TlXo7RK4VULbAr--ZfY5jY3Tnuhj7EYcKD-bu_kzaowmQRck6N3OyJR0UtMbXMXwJaN4KYhHX7p0VXSd5HtN4WDn9gNelkgG_LU4y6ug7M79m30feAlu8-b0Q0fUiNXERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=mKMHtr-YgJMGvbd-cx0bcHkeQ5v-l3H-5cqgWRgntjt08f3j2c7WEfJf_xNfgyKYPrpOTo0hvLaXzLLDBVx3TO8Sz7FjtGFC3tbf46yHhBhiVugh60WZmzd082aOHxqoy35dVOx5JuZ3_O1ZqKA-Ev2GYAidRw4MIBcxvlL7l_nLM67mk6VJresemVXMhKwYcAqiK4b8Ef4vtbbkJ3rQpvuhuVTwkMZF2E7pLwI2EiJqPJ32-vrjMYWJfMQ_Sg0SrRAqe7gawozLfp1e8IxpOcIMQZhYdTRshN8TpX9sZ1QYbpO1_8IqHDSxDYpvlJk4wG9keL92qK3EJx6XYzzClYEy--Gn4ttDBhQ-ZP8axECVGV_LhoXfwednM9yWHSHbj6Sb2UU6hylZ80bjkD6qLbSmqEB3G0ZBAtwIfDZxfimRM9C1johx9zNAETMZufbGm3jHkN6Cb6pQFuNM34Gjnw49nat1HK5G0TDcFABdh7tBN1T3EN_hAg-dEjhuZ-Rr7LIs_TwsmzCkjoB0jWmlvQtCI5aOLtvWcAyd-F-WpNs2lzRgFi6FKd-hD9ZAADZVlx8NAPfVLxv3MhC3IfNpHjfIS_M2PN1T0h3d8uWw4uQYno8TBbNnG5g6jmZHP54K6vYQ6ixRBLyeQSwW62tVsWdtlAJaamWvKYqStCbJ_Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=mKMHtr-YgJMGvbd-cx0bcHkeQ5v-l3H-5cqgWRgntjt08f3j2c7WEfJf_xNfgyKYPrpOTo0hvLaXzLLDBVx3TO8Sz7FjtGFC3tbf46yHhBhiVugh60WZmzd082aOHxqoy35dVOx5JuZ3_O1ZqKA-Ev2GYAidRw4MIBcxvlL7l_nLM67mk6VJresemVXMhKwYcAqiK4b8Ef4vtbbkJ3rQpvuhuVTwkMZF2E7pLwI2EiJqPJ32-vrjMYWJfMQ_Sg0SrRAqe7gawozLfp1e8IxpOcIMQZhYdTRshN8TpX9sZ1QYbpO1_8IqHDSxDYpvlJk4wG9keL92qK3EJx6XYzzClYEy--Gn4ttDBhQ-ZP8axECVGV_LhoXfwednM9yWHSHbj6Sb2UU6hylZ80bjkD6qLbSmqEB3G0ZBAtwIfDZxfimRM9C1johx9zNAETMZufbGm3jHkN6Cb6pQFuNM34Gjnw49nat1HK5G0TDcFABdh7tBN1T3EN_hAg-dEjhuZ-Rr7LIs_TwsmzCkjoB0jWmlvQtCI5aOLtvWcAyd-F-WpNs2lzRgFi6FKd-hD9ZAADZVlx8NAPfVLxv3MhC3IfNpHjfIS_M2PN1T0h3d8uWw4uQYno8TBbNnG5g6jmZHP54K6vYQ6ixRBLyeQSwW62tVsWdtlAJaamWvKYqStCbJ_Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhXPtRGdPBf3LUANJmLzjS2iFGsbh2S1llLNtk4G0Q4sMyX09chfrB38J3GbuoQcuAi5Wm8oyFHfmrNpGxTKtjClpM3ZXU79Cvy42S7vlvomTFDrJkpA2xo-En2A-_0Qz91lqvMU9O0xee0fto0Tw0EMEQYgCvir2m-Be8UgSrEYKfLUYhhArAqhY7V1Aj6TyRoM5PAotmShDZDFV0txEAWYuRXxg6OTb5xDv5CNlYeGxPb_yi7SI-hki8dFpwUEKhcZ_XILYEGITscLET8icUv1nbgRk_MaT1vMA0I_b88OYLyW1hbyyBJjpKVS-0qYlBGZkuAlL9_d8ykd4OxudvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhXPtRGdPBf3LUANJmLzjS2iFGsbh2S1llLNtk4G0Q4sMyX09chfrB38J3GbuoQcuAi5Wm8oyFHfmrNpGxTKtjClpM3ZXU79Cvy42S7vlvomTFDrJkpA2xo-En2A-_0Qz91lqvMU9O0xee0fto0Tw0EMEQYgCvir2m-Be8UgSrEYKfLUYhhArAqhY7V1Aj6TyRoM5PAotmShDZDFV0txEAWYuRXxg6OTb5xDv5CNlYeGxPb_yi7SI-hki8dFpwUEKhcZ_XILYEGITscLET8icUv1nbgRk_MaT1vMA0I_b88OYLyW1hbyyBJjpKVS-0qYlBGZkuAlL9_d8ykd4OxudvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cuf0SUkTiIRhBBLBcoN-NOb1rkDd606QjYCkwXnSDEm6SA2XpOmI8zWY6UDaJetvT7FJiInbSFQlqHSTanuiVYiyDpQxaYw3h1p958aTzy3YDeoFbVeTYWOGXiNRuaGWbjAFpGKIq73BAyUe9TNHdmBlsYyQwXLWgfTjgZ1XoSjkrSP0VKRELxIuHKyO1-a0irKAD-2BI98mlqXDY5ZO0VLGZzAM0V7Q5b4czTYDgaJTV1pO0KRZKCDBuNNgfmgErFBrEIKWIqf6CyG6D4g3wbZTbNvq6bBXrpaOHYzuceIdqI8HVrl9mKv19e3xhVC13ggZk59tGuAwQp37WvTllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=keFN05IF1GpDYSIykuUAZe-t8MwqvSIpROGxBlnbyHMLQpw9ACGluEWkJV5so9bfGXn_wct1RMwg0TirGHd2QFMdI7FjTERgBYZRXHjur4OM45R2K1y_Sc-WlDLyfV9TOULc0BV_X_YIFj24WhnlSSfA-OkK8rUrN8eP5RfMouQutGjmpbJDDDeRp6EC1Z6hLJYapnnUPuBPdvToSuviYCAvw7dFlogCWWgugxUwNQW34veT631S2uiKYfQGzeGmR6yR9pRYYjJgRsTWfmm5sfjQ9eF-PIycSlr8iN1fWtqptL3iW9Z3dAVCahUJLTPC5k8y5idwoFSmfwHwVBFG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=keFN05IF1GpDYSIykuUAZe-t8MwqvSIpROGxBlnbyHMLQpw9ACGluEWkJV5so9bfGXn_wct1RMwg0TirGHd2QFMdI7FjTERgBYZRXHjur4OM45R2K1y_Sc-WlDLyfV9TOULc0BV_X_YIFj24WhnlSSfA-OkK8rUrN8eP5RfMouQutGjmpbJDDDeRp6EC1Z6hLJYapnnUPuBPdvToSuviYCAvw7dFlogCWWgugxUwNQW34veT631S2uiKYfQGzeGmR6yR9pRYYjJgRsTWfmm5sfjQ9eF-PIycSlr8iN1fWtqptL3iW9Z3dAVCahUJLTPC5k8y5idwoFSmfwHwVBFG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=vjdPGk71TfLin21HsrV6CAH7WNDJF-M-Oqg8BOQW6gJvNOtPAn76dTDDPKGnKRCydNb1WH7iNWxhM7avm_tLBZk98hXWOzxbX2DLZ5NkXMgvkRnbtH_BZCzAS0tgCYfznu4SgrVEh-hGtRKcqEPSIBSv2_gX9TQJkjrOnFlwVHhKsgjNcTtr7Z_Dzj7pMKHkjb8PfLu9Myfj9ULn1J6sGaFyPnqjb-gKMeMhIT0RPbVngfe9gWogP3QRDcOwvCYXuXaYs5_pWdGicxdfqEmKJSv7hYv3e6NHzVUb62TcnvbWelFqxcNOuiMk0R5PvwZLnZa_bsictB4SpjRNenivrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=vjdPGk71TfLin21HsrV6CAH7WNDJF-M-Oqg8BOQW6gJvNOtPAn76dTDDPKGnKRCydNb1WH7iNWxhM7avm_tLBZk98hXWOzxbX2DLZ5NkXMgvkRnbtH_BZCzAS0tgCYfznu4SgrVEh-hGtRKcqEPSIBSv2_gX9TQJkjrOnFlwVHhKsgjNcTtr7Z_Dzj7pMKHkjb8PfLu9Myfj9ULn1J6sGaFyPnqjb-gKMeMhIT0RPbVngfe9gWogP3QRDcOwvCYXuXaYs5_pWdGicxdfqEmKJSv7hYv3e6NHzVUb62TcnvbWelFqxcNOuiMk0R5PvwZLnZa_bsictB4SpjRNenivrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=id99aAY61ljkfnY6tAmJNhWYblLUkuNAPmmWexnPTSFrDw75k1Zmpy6RlcetPl8-26noUzV0BUPKO_YSUur2sxOgc24jL4L3tzc2ZmMMnuieSkF9d2ukc9Vzgo6VOsvRggGEo7WzaRn-CrKeAYbFm6gg-H5RQamPhP1zNMNRZWGM8Mc2KBTHLThHULeSXHJnjoRo9XC0kaEqBKRjcvuX1DhrG-zKsfCE2d3tAj2gO8CDM8D76EwKPk6Sq9YGPWGidOsO7QkWFt-F79J5w3X6EPhwK4f65btkAaqILP85dymOVuE14hqt9Nc95LOCnbzihfYJGJuAib6PEhmTlLuSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=id99aAY61ljkfnY6tAmJNhWYblLUkuNAPmmWexnPTSFrDw75k1Zmpy6RlcetPl8-26noUzV0BUPKO_YSUur2sxOgc24jL4L3tzc2ZmMMnuieSkF9d2ukc9Vzgo6VOsvRggGEo7WzaRn-CrKeAYbFm6gg-H5RQamPhP1zNMNRZWGM8Mc2KBTHLThHULeSXHJnjoRo9XC0kaEqBKRjcvuX1DhrG-zKsfCE2d3tAj2gO8CDM8D76EwKPk6Sq9YGPWGidOsO7QkWFt-F79J5w3X6EPhwK4f65btkAaqILP85dymOVuE14hqt9Nc95LOCnbzihfYJGJuAib6PEhmTlLuSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt7f0CUrLMS0gjmxKa60ZTFqPNk3bvzVPpVU1-vzMcOh3cgQ8TQxG23Kz4Ql1z_4JVIZC2B7sVJXtZUOW9ghZmxLOzrBJW-4NLqnp7M33DCKwjmG4HKAVq1r2SR1R1Di9KxHvrLIg7eBqq_YNY8seTNfcxwQMEE6CTqOUMtHIUbWfoWTZoN3Ya7VbHLKFYR8iMuysfQURVWyt032yQsdwndjACh4fKG9Q8QXPm0v1cwC5T1dFB-RVZYvspVHTgsYB8cC8GVI8K2pvzCfRsc4Gpqs9Jha8WyAAt2KZ7LnwBFH4P1AKaSHxDUk1DA03B741xzS2KolwaM4k-xDSfRlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFLzGJUfQU3t6PSTuSKEXnbLY9YZ5qSkxT-z6MZNF-G9Dk4qVignFqFfWLv0yGnWQyBhWxuism_f0udpE8INI8ZUx8-Qign-4g6kXpf3EqqVZ9bW0xGGNC4EWDyjUgbUCoz43VD_4r5RcLuUAxDeXuDFAtgD9rznAoxWCfWlxUFNGsmcPv7QWwdvF8UepVpHduNsN6BWGskofJCk1FJUz_HQIn3kwc-IXsmA_BsSeMsDn5q8ZwBd9w-37VHhZxHHdaTbNHrTEApnyEsuWox6NICX5zFzqLA5-P4tHeHAD-S1bsZsYdAF7V2zCgMUPh6r0s50DdTMigjGSZI4DJa0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSy6S3IKNwbCaAhdQpDaPsOexL9_ZpOgI1XG2jsKSnXb7hoREDo_tHBCYhx4jD966H_gNGzdvYgceMv8TQ-T5tvzzB3JvcUnGHOKLVY485I8WiQOmcNGiwPZ5q_GYehR1HO5TWrWWqwDb7ZVuWQ3oH0555Blif7XMGa8Coeke7NY-HpnLWSlG6-CHA-aLAJH_ht6QMe6x1SSFIcuJ0I7PAPPL6SQTlo4qDJaFO9CyS-JLoDIDw739_j4SaDexcN_b4PydiDh6GRP763xVRn4_iT0IlLI7WTrdZbhKbVzRfS7nLUrVqmR7N-4lOkNxwrpgN5fsPVPx1f6VbbZpekSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2z0KDAusMeBx3a_C7ciBeqnBzueCs5M1vf5hpgrg-hAw3pTYKF9O-ZsA9npAkqOlYaymJvEjlYy_Au79qKWoVw6qR6uD1gMrm7fg9CBjsSb11_CFLkFvIA_EDSP-nZRUfn7eNQzLhy8NpVEVbVOLQUTkT4TFLi1P-YPF4UjDqBLAAODvwG6_aSU7fUrI1A1eOGKfcD009osQldZwOZZVWsvgUkuYSpaTzM2JDekCvEDLkJu3TKLmxatUu6OGbod86UKlqdVdKr3puRTWwX2OKszODluiVWxMBFSRcn1TITqnzHKml2Iun18K9_znylJ2XenBCorUsqx7sskGNJmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOIyLKTWDsrewVF9dD9BAXshTc_G7vFaKzWhL4G2x-O8KvRbRfMz81NjbfwDYQZC3zD3kmWxczA_d7PpDDRelsuN18WRlmnTr0W9i5vFxa8S5p1f6qhYYCcscTeRy7MyrQ4xcS2OBmZL2MA1oe1y4JOjiaQhGrWj-ozc__yuQr9zAr5hoKqXnVLPeq369No4diAz-aGl3eXj259-B-2cpePv1ER-7xy_Xi9HN8g5iSsRCBLUV55lqGgbB3naejBxxbrWtcrK-jGlMEfjtg0Rbj9fr0s-Q8fEbw2HmEE5NjZAFTQT0FGXvrYXRBU7BiJWPtsqkIPGt7nOJhZAVSOatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCOSm_v3aWwwmFJP_X_dmiI2YM-GRfrZNEZxlzkYR1jhxh-eVf34KpiQ4Milpu8qWmN7spbIiBv4NJXEZEeTMhxXVwhKdCEJgC5Pgnm4uk_w9NDtG7TxSxYE0Rq6GOpyfVDgbPdSFw0ZnsPBUROqBh1QDvzQqr5kv_bJEA4tpgs-7j4Pijo16upDQ3OTTloSc8vYMkoWPb_pEYBZkCFZvBFnQbI311DQN048jNzBIKkyNbBZ1YiEtv3wRhIItE1LT1g-WlBaM1RCD3DiyKmEkbI8l1JcpXl6O29nYU-JzQzUQh5oWHR5Mr_059HcWHKN9g08Tfte6SoFJ6dbWaMebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=TSd3HH6ldp3jvsGtl-LKiv8IQ8yM1WCkWRQiOMlVPiwV-R8Zvy5WHU15ov6R3W03eFXZfvaJ1c9sgUbdN1grZ5Zmoaxg5lWwf3eNtfCIBTCXUkV4fTOAHNzmS_Ge0e5JalgXl_NKmGSElnkUE68sKNGwq6ISndQfTXlyllCGI7xoOsQMjVopue9F8jNvDAIsAB5JCQtR7_NzZsr61m6XJdwr3kJE8a1SwTFJo1IIHkkEdbs9ObGMYa4KJ8Ycv2vTnLT5GD6ZEg0CJGCyK3RxUglZsNGK39o8dQT2qAVUnoUdFFsXQeAPqfslQcKn4LIqV5A_5TwFWjcn7Lwenzosqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=TSd3HH6ldp3jvsGtl-LKiv8IQ8yM1WCkWRQiOMlVPiwV-R8Zvy5WHU15ov6R3W03eFXZfvaJ1c9sgUbdN1grZ5Zmoaxg5lWwf3eNtfCIBTCXUkV4fTOAHNzmS_Ge0e5JalgXl_NKmGSElnkUE68sKNGwq6ISndQfTXlyllCGI7xoOsQMjVopue9F8jNvDAIsAB5JCQtR7_NzZsr61m6XJdwr3kJE8a1SwTFJo1IIHkkEdbs9ObGMYa4KJ8Ycv2vTnLT5GD6ZEg0CJGCyK3RxUglZsNGK39o8dQT2qAVUnoUdFFsXQeAPqfslQcKn4LIqV5A_5TwFWjcn7Lwenzosqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaOU46MwZZ_gw7rBgcYbgvVDJoTcEPqurDSma-TnCOoX20kwwIC6PzaxRtcXIE8AOUe0L2qYALR-AbZ6PRq6aS7rkOsiYqPJi8TLGxzVTwqr5DATVKMyfPyqdhPaMArYo7R8n615pa3SXj7JNJR6FmBa6JWTIGXKjTAo64jcOlFqqOc2qv_182JvGMm4Y4qKsKrFbP2x-mW6JKLABQ3G5dTIlKcLhxnSrp3KUcdEjavRa-v7Ve8M1JJFr9_ZCi--uDH11RkLj_K3lSpYyvo2fC3iJ6iwwxadj9zFdnx5xBoPMvqQNaCa-6pV2vAMr4PcDpyaAJ51Y3gmBQBkeBnVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFA-m3Vv-Eitr2vN6uvzV7b5UMmpKhpg8NjByuyojgxua13LIP6xfy6DqMx0qv158kUlTdcT9c3umiSkjqZL3uVDCXfYGNIGYTme7mwsmKJl6GnEOOJ_ObXG6oTUmZoyoJ3zpbBDgJOMDPDoVPv_QKVjrm6BOJKWkOUg_zOAMk90SXJca3WQUPJrRYhIArarSX1TJiryFC1IAWed9NC0eA_VFIld6vDWH8KZb2tA3S2xhQysVTItEtko7wmfMl7qnTkNX2YUGkBpT-bJWxMsntAba6CSEk7IlxLneRGPYuowlYpgqbkrV3EEH-DBfARaJo_3MzlQBEBtWl4f3RNOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAjWrIVBmrT_l6kj9zcSOyzuaZZQNCX7YX6WvnO7YDfuEZcLP823N6oANv2072QIO0IT20zqAkfFr-nOozPS07PpkSxXmRb6k2BbUs-7_wFMWHBWmMeJWNiAtPItnV4_TvmzP4NKAVHts9mHRgmC_PAG0jmGUNeS4vFY9rI99GGvjWvTaN_XDuxUqi7R_nzkuw6RFlnQTmyWp8q6EzQFqwBUcYrTXwtppUI523rdkfBDQpqVJMTaMVmu9LIqtfQObjSKYzeOQoE5jTfnVyrPgFyZXIVouwOmol2-XDskX6SAyGzFEwWT8GK38yWqe1PWNONkUgaHnuEdjgHupY1y5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OysaPN8zUIIeF2LgUXUhYVgFvuKbn6Kq7thIFSrRQ_4G3K3XL9BR3FRNuDIkhJ1Y0OPZ-nOlbqhheOzYNVgXCOaqhhziNQ4oO-iGzO0fDTJQfGzpkf2iL4kDwgxDAGExSsMTNxhCi6mcRjXD7z1EqEHbMZJQjqHqLQlmmWUTXrelPvRn7v3lzEzSAZdvgmB6WCTFRidqZ8LvDE4MqzjbZMWVayQd2Hl8YP_DfXGTyl_MvbiSa8ihtjg5g1hU3Cbo2zwq1xkOZnd0I2UnVh1tv9VxmUEc60UZ60z6y9b2fRRBuCLbYL1bHVOOgyeD2z3BolkatxyZhcTl0hOTRg5YBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrklbQtPdMUdBsJHhKlN-_dgJ4fn4Yt4LRcTilwttfcyWL-Z6nP3r-C_k3HEvkjJblrLFuTcOtD30ev2drOCxwg9ox3Q1TmiocEd8qE8kzj1s8hxcGWmGY6Sdh9yZS9jijRwu7IxbtfIEWkIZI1VEQ5wxvif_6nVf_sb5V4hc2OCTH9aDh3ldwwiri0jdO9MS6PhF1AEiA-xo10WnfK0JyAbib6HfYlzZJ08LtyZDLD56dWB-_ADE4MgEzB3DGwBL1rNOCxpNe08hR9C9rwtGPrVs31sKsGQEgZvaqITtIIzug2XDkAjkuQ8O2wQyn8N-oUzJiNG0RRXmVrAZ8-nrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrcsxrIkdSMgRPh_I787do7ZO6ZV3eBtkYBi3vlIpqepAykJLiovPdC1q_fI9EeEy0lvoF2i92psfZhtQ444_K-TnLGOJ6-6Fxd5ig2hUVpt5syUthCMKcB8d6BrXsFW-B1c65vgFtQsT-1c_y1rxCBc3XuB3MpUSIsK1k4JjKU9IcXt4XnnHYSxGPx_RpeNGZ_eiCxHOBRnScdTNdZXlLlAzxri64QR8xcu1PKcIXk8t2spM1xbkxiU-Znu6auv8YE7KsF1TLmQH81gbPT8vmnLJf8X3wrUs6jQUowbauEEZu-WqWhQxqR000u_Tsy9-EiUMBxFJC64C_3c7BQ-aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=M9hX4gdOb_dgb3KkSuxxAuSJtWPp2hI_94lJhONt54xjEP3OMSffaFbzOWyjktqXy9pnr2mA5dcODqZkz7JkDi20ROhnakQqofx5S27mtYdLM_pO-ge4-ZMFdUO6b6GHway7AkaedsLMo9YWH0sTxOmIRtqCOgtoSbE1Ph0Ai8OZKJgY_MpiANDDzenwGBFVnZGkWBsbY74StyensBmWtsHTGI7_F6XXUMkoJn8ayTsfKun31KJU5VnrsM1hxWHikNDy-duCqw825XKgiPZymffkQ-DJqrzVc7gg6CkahN3etRKbWMWevNCBK0xkLwcapPmNJ06FXLKlNfc53UcbyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=M9hX4gdOb_dgb3KkSuxxAuSJtWPp2hI_94lJhONt54xjEP3OMSffaFbzOWyjktqXy9pnr2mA5dcODqZkz7JkDi20ROhnakQqofx5S27mtYdLM_pO-ge4-ZMFdUO6b6GHway7AkaedsLMo9YWH0sTxOmIRtqCOgtoSbE1Ph0Ai8OZKJgY_MpiANDDzenwGBFVnZGkWBsbY74StyensBmWtsHTGI7_F6XXUMkoJn8ayTsfKun31KJU5VnrsM1hxWHikNDy-duCqw825XKgiPZymffkQ-DJqrzVc7gg6CkahN3etRKbWMWevNCBK0xkLwcapPmNJ06FXLKlNfc53UcbyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=c9odBKgFBNhGCt2baB_sFMW_o0enwHyt5T8R7CKOESsXLqvD6lP18D7WEPgnU0RQ8PU4Vuw9tMgz74dDTqRp0gg5WCvSOKcnist3JHyKNlABUNVzAoXmaXdtaQRAHaTAtktuBUCXuuUP1eD8gO4-JqMXIjg-JJA7gu8XiSTKo23X3Htrk8AY6evYinKw286rbHeO2in4_hz1GADjEfu8Xx1R10e8dxfWeFBvaGhRwJB6cqjn26OVwQoRZ68DMM9J8UTBFTk4JgvZQGvdKJJ-qZjSru0tyCcU_iMWvuJKsoRQtxp2_L4pbSlmXWt8EoiHvW2ixXVynw68tUnd9z3HMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=c9odBKgFBNhGCt2baB_sFMW_o0enwHyt5T8R7CKOESsXLqvD6lP18D7WEPgnU0RQ8PU4Vuw9tMgz74dDTqRp0gg5WCvSOKcnist3JHyKNlABUNVzAoXmaXdtaQRAHaTAtktuBUCXuuUP1eD8gO4-JqMXIjg-JJA7gu8XiSTKo23X3Htrk8AY6evYinKw286rbHeO2in4_hz1GADjEfu8Xx1R10e8dxfWeFBvaGhRwJB6cqjn26OVwQoRZ68DMM9J8UTBFTk4JgvZQGvdKJJ-qZjSru0tyCcU_iMWvuJKsoRQtxp2_L4pbSlmXWt8EoiHvW2ixXVynw68tUnd9z3HMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKEHFDzoCnOWABoDI-kpVjsAaTBM0Y6BqjWdJCSbaOYerNr2_SyAuSgXMKIihJAVhhtZcrpBcT376AwtlAg8Sjb88ivzXCC0qeXDOhVpVI2_A60WeQF0asxYHAvNpCUfsJUWR1_8NMGbET8e1Bn0W_ftJTQIDAQ22XW5TS_sKSveYg3sQ77d1aGRm0JsObVxecNTpF7ViVa9zxt48mIdnpAjw5KihIsQKIiAqGb_G81DqMuKK4bpe2v1mzjaAYWO2neDyIvkN39X5-2ZT9MbWxmCmZqaaJxzzwtM2rm32FqjWx8ACXzeYcY6v2bYDm44dQ5Mtkb3vGGQQmSV8ukSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
