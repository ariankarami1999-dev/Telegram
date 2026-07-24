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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 566K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8JmbuyclesmmTDJd0i7Th6GBbGY0F13a9iTa8kgSAgRTcq2jYJop8yqlMrS2Wty_qQq6XCqpeCaacak9ZigzoYkG0c1d-rugkTEMvBM6m805YCpZRMNKH-V6YEvBi1D_QGRjDb8mBIbdpwh4yUj0kIu6FAZ8xllxxI7w013RJvNcDhL90WL6Nyr-H_7h3dEneypRPRNhEy_20e2RK3gFr2IN7XsyGt7dnB0aIU2r4Ss4gxapFm6uCr0Y6HTVrLvQ7sLxim4giLrMyff9XCrJ6KRslQXaBaDv3Xgza-qxnk6W_5JfDDVlgFat9nV0dwdzlDH5M75BI4EqEqdGLtfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJYDFRfYfUubrf7oaV5_jDdunHiL6pFBrmXAAz91qlwAAeiiddvZyjsh9Vszq0LWVEutGbDcFGtcczVIoDk-oiCXHIUsSDXS-QGMyyabUA34SsllYqVCcqf5CF7s5JPVW-SvhnNXsj1skDEBUdmL7Jq-IidqXx3FL5tqxldUz5NOmU_62diL31Z3k7xF2kCL5XJ8b_ilvgDFAB4ZXAhlUjB3i3sAr3jhOGBhI5krHULB1F3sux3LDOP4mkEC244BjH1vKj1t0RfA7PVpOCXaFVFoQKTspsmNDDY0HN0177mkPIZCimjVWPTAA6_4yIHTs25q8jQIeC7JGaMFBq0htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP7An1s7NRi6vVvgAdCO_3Se0UDgzNKbpquHfAc-DWRLfReIorNcf1VyHly4Ug3LuxUU1HK5lyQz1tM6PxEtOp7GqvhiL8d0fl_j3BEtQIKzcLmbIYWV-rFCF6-VPKe95t3kjUYSzr49IuNXL_QUcvzjVvWGer7JGFnCPWsUc7ip4d1a0QKbAHWm6uJODMbNrsmFyomr9TQdcL9tg3Zh6V3F_I4M3aijJpNH52GSaYn9Bm0eGALP2WfrAbVh0mkksrkHnJzn780Fq880dj4Zcab9Br7iV5A1vm6WkvTEHd4prSTUnj2nMoIAxShl7XdHnbch3NXevZhKRkJGPDic3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26422">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/26422" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5l9OvpWtZTh5vIqAYvAUXepGvQfY3kiFQEs2MW8QnQ0Dx8Q7FXp7N2t8RMgjDemtNYmJQYGHEfNvzCSUV-VidOSEKGYQNDorb6DxBXD_fS_uJp-ZbZrDCN0AX5r32RgA7IEO5AzNZVcvicokmMnbcZtCLh1osvw27C30dg-FaweBG0nC0oZx5qUGFfhUZhYMTycCvkQI7TxpwMQ7hgKE_MmnJQ2BiYMZhV4c3lMjWacwiq-Zy1iLlU_sOByON8vqxcphcAjU-HIwrphefKU4FDIP8jeTGRssB16lV0Q1XjXJ4Eu-vIj2l63sKnola7BaUfdW-80u6sHiN3dR6REMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5r3JqBx383ilFjfwiGncwOijIDK_AFvfowYOQJ8FxADRT1e9pKejaStSRXfaCAQO_2cTye8Y4Eo2YKDFmDZEjtZnp_PkjtU3cEwewDdB9GCW7EjWgCXqs8zLTAIbd8Pfhc0Q5G0pkk-4A_xwSX32mG5JAwaO8p48rtK7MKmnpPmQktjBFdczBpeHhO5QJPBjnGruySQQDokTjGr4t7ehSa0vHZ2Fb85RbWl9qs5-4Rmb1H0Y9V_9bnUBmF9aQ1kYMQOYXlFAYU7-lu_XhA4HIOWlJwm6V5gWvtuuIt_p19chExnwT6JttmQqHzdMVNCL_1J1BN2WacUmfuxdrtBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbyhI9-Tn7p-IlxbP4DcL3z-j_1up07y3z_rrxDlCXi7G-tdFW938dfI9uLSavCE_iNzMDN1_iGOnObcxWIppOAzSucPvvluNK81U2ca73YZkEnZA8kk7gPS12gx94kRfh8d6kpWKaNwZ71hAdpr-865TWQT-DryvQeHLNW71HxsQJc_78cRrfdBgdz0cAPx93Pu9nPSZiVQ-mtzl5RWwtyD0oSULH1sbrYW3Q0m4uiA3FyxJptu_HHzpBoLVe15z5suVRlCTF3uIwLZsycHuCRMCbgOl4bbSsopWlGc0dVfEFc5LM0Tk_ajjalJwO22ZlWxJT3ti5Q4hhK7WZnP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkOSqd5HRi8I80ClCUcKDJ39m-49i4T6CS4UfEp5b9dfzntMD5AXyjie5RsKV8LVSoamsf8Rllhi7vpKQeFUmBgWoXSa-lsi6079m6Mgpx5L5btl93_uF4OE3xX0TAMXpurvmFCXsn8duQxQ3lOPa7TgLScAzqLJDkmwcujvxv0C_LkVUkDe8DvFVbRlIqIWrbfq10GhuFT3AaYpoJ46gWLuF8PgkaT7pAgTZVpBpRguEl8jPNaGH4Om3KjPgmWUyn3QwZeePvqP1-WnownRUzEDAFHzH-GWeUix2X4IZW9CgK1jt2c_2tRzbaOH0LSskzbhY5yEo6BpmOlaW0Hmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOb9gS_DojrErMGlHwiSzi7WN9zs31oQyWVbhN5NmOBt3wk-kQCjeodQf5XHE0r3b4nnC3VhGWyB9U4yxYpJcKDBXwdyvNCXIA1f1Mi9rEuVSJdBSefV5lKpXATo9AAEv54iynJ5Y3j3j0vi5Yjzwfmj2Zq-cVOolMde3zOfr2cvt1mV5Nw75ujrwTE1TXtGvHBgpq6Da2Jp0F3wE_rkt_NBjynDZ8thN4FGiAryYeD07arRU62OABvFLZlaIvfWd_iz15TGdo1OirjCGEWj1p0027B-nNmPeRdUcQfucqT1uWKtGDad5vtc7jIXwLMr50gCVwDZi2FlE4Y6PtDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiXDbJl3q8vE5-AuA1PeDBlzYFt-VB52nXiPa5uPZsiRKYwO5a2EtE5m6W41KzgKLPoh4fP9DfYk0rUDtH2dsRGBpKo7rCiB7-FBtEelajYFL4teBuSGBAomBB8Koni8xAEB3rUDF3dpnP1LdqZfiqpZTmndqP1ovcWpSILF0pR19ihrEiSK0rteQQ90k4mi_ZmB_5keHMMEBXUdVwbgSzjmhlWHCJgBkV7P9JQjw1k-zTiMx1yKlyEEH08i5VhZ9xO9U9_5ox3OpdEBTPve4O6ayMj3KAjHbgF17QKFX0kuTgfYTcZcTGSDdRAHZhJzMgmC3I6E_CH3v15iQ7OvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7TxkDVpG3YWzT1YD-YL4gt9tBMCTTb5a-HYPkrQX00WZpsHUUiPOx5sNCVhH-W0caMLQ6BmV_ITQhZ9KR5CZCGSDjKzvrPKbH1AMEuWyFmug525KNULYVrbiGq-QYv06ZezA1fj4YNU4ZZqILB3f39jCO2TVtd_3ib171nLQlvAuAAJcBIbgphPwgUjIgVicD2VmChq2SkKyyY1fo-IUJxyj-MIPHwxCx__HTp9Wo8G19YOXM3DtvrxxdznIBzoQ3-wUGyGQeZopfuANabsrVBUG8eyrZJy6PqnZFtOdw1pWlbK8dBH_YTLEk9sAJ1iMrAeZ_nlEnWkxCFschmPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtZ2ojOTMKIQ6-mFTa41HtYO8IALxpraCz3jx2CuH7hkdAZCuhQia70nmSmUcTqP3-jiDv1AjEusq9zABfkwOaR0glDcOYk3cp-azs6DY-3Xp9UWGZZYStTRzkhc4-ZVw_wA3QyuV3ZlOBQkd8GZEUIej9tKk5CZE5qrh4BNB_bUOSqKEarxWRpQybBZPvh1yhm-l8Vk3Zix5k0VmrbOgar82iojdh0tKhl2h0lEghHW9FPRw8rA57z6rPbTndT9XfG0rYo6F657L7hoYE_7Y8uUYOCjUNMSkIJq49tPu2LqLmzoCuepdrpm8XvvlqeimfXz9P1XutVruIO4sBcmEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL_ya9qYa9YvZ0_XyivYRp5FluuhwpHAXnhq1oM_fPGwiqZECXnyOtO9IZMkWp6VZmyRDdORw1XPg4JdIpYJaOBex46jPmGoqAiPCJNIqsysolmSDcYu5GBX0AxPeBlkQWs0uBgpWWP6dVTYtMsQ9_7wNg9BgD3w-KuLD8VGcs4oL2C2ZWp6qScg0cDX3mVYOsWVFgG3W6t34zYfWT1-OMKPYJ0cReQbc5D6FNO_5fsixmGJUIQazy-QyfogBJuQ2Ce86G2mD12Dcn57io1e4Uxl0t2DuQl4l11XKfe4JFozTm_vmlRRseBT2jiqDkCAfVPtzYCtIpDpC7DQGgp6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26412" target="_blank">📅 15:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ8sJekuGaGYaOpZXHcCX621hUSr_OJXK5bG6nfMEzb6WaA2N99fev8QDw4JFvvagPQr-zXez1co1C3cZa-HXVXgqzLw39SvEK5IrRDKT5_xDpOuJxWU9zmK52FgYgtPdkSrJ6xMZFapXPEhP_mWJ3jvCY0wtch4rXMKnQFY1ZgpTyUZ3YwOQm05FjCBfR1zVy6oFmcrColOneV1X1RNoisMnBjrgiblraW2C1yyuIOcnN-4PYmpY7HCAplc_MVj9KV0kPaGXV3pSDdQSU8JoTUejCDZtubVTRfRowrkFgE9R51HCHErRgvaaTX2ZXTZfiKuZAfCGUeuAod2asnXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ درباره آخرین وضعیت مهدی محبی پیگیری کردیم و مشخص‌شدکه این بازیکن مذاکرات مفصلی‌با تراکتور داشته و حتی توافقات بین طرفین انجام‌شده امافعلامبلغ رضایت نامه محبی به حساب باشگاه اتحاد کلبا واریز نشده. ضمن این که نزدیکان محبی اعلام کردند این بازیکن اگه…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26411" target="_blank">📅 15:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9e7HbDU0ZGUwELnN9bHO_YaoF1LgqU-hkM0fqFI0DD6v76PA3mJKI1sB9JIXGA3vkfy1a4j7SyEwn9f2EO8UbYOeB4jPUGVq70ZdyIhDQdFJP-DvneSi5q61dT1Z5SHRyMcXPtEeWAUXhhgnQEmqad9kA9IKqV_1s23Q4zYh2tgDNIieHJGOyMy6AA9ILWCFLl7GbKnFABJnp9KTq9CnhbVlgaA0NJWJSwILgPobooLhDYxqrcoM64-1_KjBxmvtdleK0ijrTbyxQapZTNquMhwCcn-2wpRTbDuWRd_VEudQN8bgf7KHXIlUHY-pecDAP-dbee27eOqV8rDRU4erg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اولین هتریک‌ شش‌فوق‌ستاره فعلی فوتبال جهان درنخستین‌بازی دوران حرفه‌ایشون درمستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26409" target="_blank">📅 14:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqLTVJdJxc871cs9QskzPhN_1EeRdLBvPhFhoLU_DVfcMURquK-wSf710Z8npSTkmM1Nvv57WfARGvsIXwRDLzYVCPTpUdxhPzmk-J9D8hDsrqJHsraQ4PiTboZbAJBtmIdTYNcgLmaNVEYLvtJD9a1T1xcHpWQTPtgCfrvc2SK1hLKPM7ljYtvA9zhi-n8_q4Cw66wSaIC9lBeO-9eqPs4dUWmXqAbsM0UvgVlOE50eu2FLefHRbruszUb77PYtkeXM57BfCOW8nAUepX8QhgtWMd33p3kBGlIpc2DSLDg2wxOLBQbTPeMcj-xOJMsznE5AvqRmqSHQRMydulWVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که هفت روز پیش خبر دادیم؛ باشگاه‌گلگهر بزودی از امیررضا رفیعی دروازه بان جدیدخود رونمایی خواهدکرد. در قبال این انتقال قرارشده پوریا لطیفی فر ستاره جوان سیرجانی ها با قراردادی چهارساله شاگرد تارتار در پرسپولیس شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26408" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPP9TiCbyugdzsSr0abAsCvia4LlZmboVacJolh3MvW7z9rRiKgViyYjh5SRUWEkk2zujvIpkIGbwaaoIPmSyFqVMClsQazYcrGQUIUNpoeGySGIyXFafQaSRXxMoVWbOXsmZhNNygnrUkjaOkGp2lrvIDgULmWTW58_SE6r57RonH1i_aBQcL0gXR0eB8mLCiw8CGKsEShVV-12kB9YPCbjgp___cdYWxewQUb1ao3UzHT0jGce1U2rfrGG1X4vguHcG6n7mI_n3EGM2ljePsc3qn8lXKfjY4cI0sA67ptb91S1SaNlS550aAeXPdUTLrLRmnqmTFanK-4pRhns6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26407" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2KPsec5ukmjxLHlh93UiTR5GEsr5pZeNMvIxxo9BIwPboywY1enhk0Qk-CQkOdq6tMmy6QB4ql8LdwyebtSB5_HwMFCapZ0Isa_RwlQjTz8qIMhLNAj3PHU9usegKXfMg2N9ox7C1OUq5ItkXMQ2QPFUglotQGzz5c2vST-6GL76NLqMlNWeZper2YD6AQv57DHItJRpWgfgJUk0pCwRDd0EyoY2qvzWRu96Sor3M2wsGKcHHKCN6U0yzo8N-9WLjGlwPwsdKIDz0Djo-GLa4po6SLrE2Unl6dVFHEDZ2Ty60fxjxt-dgNuzj9wjDdlQk3HFjIdE9M02_57tJGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درخصوص محمد مهدی محبی ستاره سابق سپاهانی‌ها زیاد سوال‌پرسیدین‌که وضعیت او به کجا رسید؟ سعی‌میکنیم‌تاپایان امشب‌جزئیات‌دقیق‌وکامل درباره تیم جدید او بگیریم در کانال پوشش بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26406" target="_blank">📅 13:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac23bf53f5.mp4?token=ubb0GwnhEtS6eg7AmX5TjFCWUTCpiASctAIvkpNcqxzS062r3TF76XQS6ytRfkp_-SuYitzLLkGei_jC2zATMHARpNOGbUq32IEoUAP-bDdIRIh3j4HxXygKKNCrzWqS5sx8qZod1rrOOCJBGw-Ic1CRJSJrbvXzfbtWkBFB5XnYVwvkKJW6DB-Ik-dLfjTKXIWQW0BcOnURbFP-VE4_lz2Q1Sx4GKaYZHnEzsuNgSuspoUWuO3XEla-D4S9lIl_XFyh4-4msC2fAcv7J5qmK8myMl_qNkW3u3LeSOT2uCD1gywt8flxWHkNgPYA4NFcuEiaiWtxF3VJbTRR7tEeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
امیر قلعه نویی:
به‌جای اینکه مارو تو کتاب گینس ثبت کنن، با پاریسن ژرمن مقایسه‌مون کردن! آخه پاریس تیمه که مارو باهاش مقایسه میکنین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26405" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQbaeAN36II6r40lZ0l2nDa6GHCrK9E7ErZmSW0EOnUpK_DCIASE0MlEqtt67-zXxQYzlkV58_3mp5fgt6EkH0dakZuKhg9pJCV4OlHMwmLIAAH7Y41_A66ZXrbV4jX8QEpAq2f08mzAvme7kRb1krMQW3ISrn8rOEGypazcx0yyBvNLhE3RA-gyXcw85XboqyUePHVjkN0KTL5uE8PRlTYFLLtyUxZXFzl0oIm3KK24F37muMLcqZYuRtDGCXW_2SApHwrFfaSumfwpjMgJJ-DxvRBbny77VBcz94hruFLSyyIyGgX-o43z2FuCB4ICRTDYxt6nCQ5xVW774TC_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو سوپرگل دیدنی پوریا لطیفی‌فر ستاره 22 ساله فصل گذشته گل‌گهر به سیدپیام نیازمند در بازی مقابل پرسپولیس؛ این‌بازیکن بزودی با عقد قرار دادی چهار ساله به عضویت باشگاه پرسپولیس در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26404" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P86JkuCTS4YODiYG70Xdhcd5o9zIVEevQw-GeSfMmvYwngkWwytxD6UonZ7cIHjJJ_DiR7JKnLaufROncBH612DBgNWIwgs6-1bGB61S1A7KcnKL_ohG2xmXw4soDgVP6lKxGRnSbPlzChR0Fmx4CD5jkVyRWS6G8hCCYOXaihsFzrBMygp-lSAKeiH4w2cMA9ai-cJaSUHzL3Z6tR2SP8IiPMEDCMQvwlOtbbc7DOFfp73-FdNezTbtvYuxZeBz7y0bXv1DjywSJuUb6tLwhV7dgwmTo4qTxUoegpSBfn-A-WjjkWOwnwPL5aGylTl36RcVF_SMgGfyUQNS7wxwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال بایستی ظرف 40 روز آینده بایستی 350 هزاردلاربه‌موسی‌جنپو و 500 هزار دلار به داکنز نازون بدهد تا پرونده به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26403" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV83bXhkByfkTCGFl6-OYn7xpH3ZnBzmLszEqqTKOH_LEfdwY7-ycg1SnY3VtQ1-tmWvJL4l9QDPF89etTAGh5Fjbx1tkkGS8r-YtsYM3feulgcOUNF-KkPHqS1yv3EKLQuBEanW0ce4cNN4iT-edn6drEFR_N0sFFjH3AcTYOdLvc3wUUEpC1JB_juIB5xmkJPsmVox7Rm7i0bUsghwIK_SiNwBBOMj06TQ2VZjax8oze7PRdL2s_TSb8qBcifxOgxWqD0_CEKC0fClCFzTAooTSfnQ5RQFfYZLIACu6gYGpaxfztvfdS2ZrLMEv2PJhyLysck47u-T9iwL_aMipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26402" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534adda0c.mp4?token=EOSC76St6nMtLm5r8bk7W1--8qpEblQ7Zuuk9hDWG952_XUnHnFEG34EbqBX7CmC2ZCc95jjg_62MHWrnCGsRJTRPTgQPue0ML-ZktQHGMEspdGCrfQu5kt8wdDnvCHySCrREen3Wmli7SJB4gr1tmBSR7tO78TjfUQWrtbLUTCgCTCzSTqMTvPgbQ-oRe1mLtuINnDYySkQLIjYFMj36H1S3-gMg0SPJVjHMTb__pxhbqhJkMpZbNoVTGRiTreQWbe2QY2bXgBXa8mlE-4KbGRC7wKnn4lISgT0Ge04BwJvMd9PibX7orQsLVaY9ZTmYLbm_LSIlrj6VpZCmOvQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه هامبورگ با انتشار این گل دیدنی مهدی مهدوی کیا باپیراهن این تیم درفصل 2005 تولد 49 سالگی اسطوره باشگاه پرسپولیس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26401" target="_blank">📅 12:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyvyD1_33B0htX8BHvXQR7ABEALKSH-rrzRyGf7MkRkkfmnhLQAS704ojd_A5GXGogyvFC2dusymphFf2cKxof9Zv-Po_E16dTI3arg5wnYd4UA6-COzQDUixVB2Lz77SSVtEtV3rjG7S4zgTg_xuxsoUJsfjOqXCLY1C4BmW3Qv43C34zwfvHoEt_PrEkMSiXNEIw58oEvXMsrFib1km9dItKou9fV2DeFQ0IN0wuW8Rt5JFH_hWL5BPDHaLUOKpdi07p0P3cKZNbPd7I_fHMH0JJUiT2Ndd1GcW15vorFilaHYNCjLkAWkHx2DUC1Uwm4I7YsZH5GbcTNG_u-Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26400" target="_blank">📅 12:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef077fbb0a.mp4?token=mvqAITOQwsSvaOLZ5JWH2j3-zcuEmlndL8MggZB2EWARattgRwFIsH4WF7SS6cUVQoPqF9cp29vA2WbrczGUKl8HrtHrUwlG_MV3tOyO_RAcD0C-to5Qcv3WZo1xnN8VdgTrq-SqDu0-p92gMgSDrABH-SwGV3oBEIlYZi0CH0ZNHin6cYqzkqS-gybEgKHRNzzOBvnCqyJJxixDtTH-lUMlVzuV8AWP_tqCbjSqDeUUDZSAelIUd42d8etYitiASSfp5a3KREkhTGxbjEpImKXWDKs2nRbivh5XdG82apb2k8_kK-mAj5ONJcZRQJzLBI_xYlI-V3rp-Bix6y3neBRsu521zSxN_8an_hFOGlTsLKSSfCQwIjNt8yuckcUpRM9mP9egLmookZDaMsVF1ZD2OiNZ1EvAqt4-GxXV65O4lVclDJU9lBAFavympiKdRVJAJ15sASCDtb2pGfNX3TriXrWbBAt_Opekpob8L-2sYI2QxnU-_BeWDxFLkOOLJYjf-35hXjwQikzbAUOWS58UAfxWkpxrJ9GoocH-3Pifufda0BkPMHU0IPSGuaEMUy4d9aeWT9uJs76s4GtDBmvg1TZKWlxj8aB3IS8b3dJnKFS5B2HUMg6SAICstjc3prd28v9LTZBpD8zUe914jP_z9SRF8hlDgvDuhUM4bDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجینا وقتی‌ کریس‌رونالدو بهش قول داده بود فردای قهرمانی‌توجام‌جهانی مراسم عروسی میگیرند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26399" target="_blank">📅 12:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUI-spun1GbdK8_K3EjZNthOtlMV_Ln_cIYaP5C2ZiAWA8Ud7nTyznlBiBqMwmVQBbD-nhdgByHFMT7-qf3Y_QHx8ZgTJE1fCyyGjavCrxtl5T4MdnIHWhQJemKGS9aadVtiURVjKxd6rELxCgJaL9zHe4QH1UWh5voFKzWAlWB63xtqlR9e_MEtyDz7hVA3XRbDnMw7ARSAg5yt9468QpR5yuE95W5qY1SnOrdQYO3aaJyAxuhSpTKmgoXqAqMEi-3YSWe8d6lvNFgTQiEbOZWXZ4YH-zNgNIqZmMn4jDX2COX8YESk4kM8GcPXYQ4O1TDD4jyiqWebDYDEHxqdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دستاوردهای فوتبال اسپانیا در رقابت‌های ملی و باشگاهی در قرن 21؛ بیشترین قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26398" target="_blank">📅 11:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26397">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj8oAPi2EQf0CYUOceZ90DqI4Oh4TB0i-dowcStoCGRLiA9cqyiunK8aAYya4h38XumcYm9SNXdo1_PY9XIy4miWQcXjOF-cubejdeYUSKK3046p25kbaaAR5Ru4cIPNHeY_32gIN1zsHNsS4Pudk-iGoQ_1IJjft8cYn436ZrxcrGoiQ1lY8YAeBHrxkphsE9qwxJao0wwzwLkgTIC-bpZmpDHO-mYB46_KsbGNvx9MSojlU_OKEWW0SXjG6yCKxtWqFayiGjUqQ21zgJOdsne4ob4KFrnc3wB5YDKl1zLgrrOM3pqGBwY2YPQnb91pKcfp-Dai6PoPkJlta7KaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبری که الان رسانه‌ها منتشر کردند که یاسر آسانی روز شنبه هفته‌آینده وارد تهران خواهد شد رو دیشب اعلام کردیم دیگه. مدیریت باشگاه به خودش و مدیربرنامه‌های اصلی‌اش گفته که شنبه بیا هم پول این فصل رو میدیم بهت هم باهات قرارداد بلند مدت میبندیم. دیگه باشگاه منتظره…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26397" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t32oM1m8k6o8TlavrfrB1X1tTukTCUFgrjFJWMaVts8OTV5LLBkWf1B_b_yDziyGSuTKpFD7gwhY6LliuvnflXEjL6eQWQb-gsTSUBVIRBRsq5oud3mphV0eyLaQmbMAF9gez_oulquU6zE3tW3LoV2nHmgs-MAbY1zvZhfhm6OWwRThQHYFgAytYOtHwVo5fk9mkXCkjFi-JD90NVFqrcW_gOHKh88JRZ-EDp_n-_K2FJQ0ARbE4_vlGeSax8qqAPpVgPjvPXS1mNxpLy9ZJt_eYwPVtB5g9D9X7oGghWr8skZR9D-ChhSGTYKbUYLDot-I6gl_AlwtXonL6T-jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26396" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swoM_8xnreMr8100hBOQH0ZfdzOHMyMO-hj3JJlH5qVpye3Hg3cHxJ_Lfgn6k866QraaqgGKAFl0FdHkhckQ0CtrMkMoDtXn8JT9MMidzsRzXIrAqQdW6_MGLcXLSFW_To5pdZcogqZqVmriF8tfaX86rzKGch2OYGJsD5Z6D3s1dXGoDvGfTeU8eutFUcTqb_S43zywa04SnOtHDw7aPgtJ-WaXDVgGrFVxu_9IKxxMBAGyk1ya6BXoBaBE0Ys0OXHoOdby9Nqdq8PCMqZ6iUpdn4GNKz1hXWEUxEsASThzCiAeGqSUIfcDc8W2mUJmoAj7Hui-MdqDJBWzaib_vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26395" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrOLJ_HNg4QorUs_0hze0V7GxUumD4Mk6IRRXN8j4xRYSsSkz5lym47qtFZyt1EumjxJ0JKaHmQqVQQXc40XFXvvLKsMcx8CmQDPcFfJ9zSLSh_WTjVTmcK49O1iA6Q8yBg_FKogWyTyPCXzp1CsFtNPtW_htBHXXGfozXReEPaHOAmp8os9sPSOQTVlpPSOsqpbwd0CJSME1LST3VwkDaunXOWiO56JcvoBQd_iXPei-q7CGyHXQ1W6gh0YL8ze94hHyecWN_qdICdWBsd51H0vcUrzLUcWFfyjt3thFP6dKKIzs7RGjdM6nr8pBcCXRdU5tjcln8vRf6Ris68waw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26394" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmojt7hyWGPFraUZ4q-FWXjsJOgd91WQUxO369ez33Rb6gD2plyMywgScDxDt0bA5ui2cTB4alkcCP0wy38sXSn5RXnlH1ZF8Rmgzxv6h_zJrC48bFG6hmmL_VZrO6H2mCxGMmIeERSFuIVdJd27rT_tjOsqe0DpsqF23Jjtl_1EQhE3PMI11qd9WKioLcOdYdRWv6LUSm0ueBSznhueh05JsIp23zJhepSvMOOgANLM6JQM6XOi-hbEPvAnfw5if1fOqkm9kIx09zPJLFGGBmz0YGpG6RR4xaJB66JAtTlhVrTNzYXJyoR-9VrWgfEuIRejYmDlOOzToLVjbxO3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdWUVoqjWY-b3rOEy7hbjrDruZjULMBKn5PTyDL-Oaca_wsMlW72DYYCjqyXhfZCYyEzpWINFLW4vJaM9XXR3VJnHNlM40M7McaSzVdalhNlXrrFtP6LG9JSWu33U3FQqNf2T3ZKOsp1N3garWiCsuqnunL6u-Vl6N3YEusbe0VbUMx4xxakNxPNSs54j2pUAYbD8HGjhZGbT_ids6s7frebdWSyF7CXXL6MIwyMqltmndmwLMEhwO_NYlbCL4zdCeRi6hDPoomVvD1RkAFNIpfLG-8-1jPY2fXx9oUz30JS2JXLm-lQpADs7HPrA6v53foStMFWQ74uoCovyZWBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDHQ7N35JbBIhPt3J6T5s89hTBNit8hUrYpHx747j8mkKwHe4DKMq_B_gCP_SVKM1mVSqtLtWAAKd-E5EK2DlbZueL-P8WyVDPSu-lwChAGs2gtSFAuTOXx7eQd8unl1Q5bqXDHUxk_BCAAcar_PJjzke0C_VsI5GBghvMnm4reOSztcPsy-5qXnLNvUILwwc8wsYOrIFmImJlFjlxsSqqsWfSB-hpOQ3hZVGo7J6k_su10j_aOBMvkOpVGZmdNNZREH2uzxbT2DObr8cH0G0fEntmCdyTqjLg6bb_JspT6MWZU4HcKRypmM0AFcuTR12MOSXWtw1PfmHfSOEP1tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bafI0AUhrdh4oop5OyTbv7ieB_uCy-vra3V3zR80ssxge8RUQFVUQK8CVNi_FUOSTbuoOG_ftvNFt6kKLFm3KIcOJsfeOxlkUfZMHTFbCN_epNp4krIoAp_M6GwX4eRUn0tGdx3M4WrazW7G0Z14qtA0mXCGmrbPDvJPkdPgD4aTnQMLcF5j11WoKhDcVFwJ4NjoAOEe33XAf-NLqcDTpxXlch-hXH-qwRqh9Oxqs1pS1wzCpah9DslGNdJFr751gzkbZyc7rTW1BTdSylJ7I7Nr4re1dDrsQnVOBq1hCJdfUnlpA4sSw9c1xcMgG6slO8jMTJsz27x_UXykWkEBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-HGK8fXC8_8EyN4JgPJ4c5nh56YK5Imczf7Slekowi1oNOzZMiVVShjKTIdViWYfanMaHQaCdcT_poJpNXy4fX7Z3SqppAANWOIWrQybYLDi3tn164XBJ88LcVFWg42-uNsYm_pWtgpx3B2IrfDkigy7ZwhhythbNOyQ1IAkCOWnU8KG4cAoTZHFzqVo7TorH6Cn_F0N6uLjChAUSX2i4_POx1ZLOZSX1IEU5GadlW27CqBNLzQAIAV8y0j6d7FE7fKoD7cl6vtPA8uE_t2bC6WkR301mtpB6VDnsKDFPvkDJnOFBGU0zTu7EuW6BFrAT42eMLow2gJ9hq1uYdppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTqJ9chgkRZKg5mxehSFvGs_ta3VLcvUrFG2MITsDA2wBGNCZyU6Imum_JUBbeE4fHjCcpflaT2_-uwrC-Af-iOttLnJQ4XlU--eQO1oURBMbsxo09y3QCfFs0JziP1WnlbJl_UBaqVKMr2fF3YXHiakxZoVHR98c3r1mFGUNgZ0nXrr-EwAslHqksYfKhvDxYgDkhGEVIUQnQA6cZMvFxnhtussblLpAHqRGBIlc2DYKVvKBDsQbSv7DV3PKBQZnFB0nNg_49XhbVJTnVYG5Zi5GfMTjoX6tpXzVKPPoLdfGy7pQLcafAlt5-5HpYy9nSQy7l1CSc2WM7Q9a2MycQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjjch_iZCUtYk1oGIuFQyRsGw8X2FPszXJYi7AOrAHbHA1R-du2bFJRZmcAPcD0lnXceURWjdoBmVQM0iGkk8q-WwMJ2UrVfIr6q9g8B6RPOqJrF5XcGHi4vKnGEOXFudi4eZGxK9maAKEJneWT6Lihdg7J_z5-eOwr1HycNndij_CEGaAyJwizjT7Uvpl1gNS_ghCMOhySXctcPvCYoSfAyI5MrNrw9spO41XlIJF-h_qqtJ_bVPxP4L2qWyKEbcKhOYSYiBuv_iXRCV7aaQl6j7e7htg8yx2lf0QNq-AIEi0EVFDog_zbH-e7_vkhiORy7mEx300pVVB2qxq8twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STCix7UQleNaCEwRbm6zVQdaXo6pJ3mjEtKcnpmW4VL3SLuS6Ts6tGfQpfR0N5335B0mnMelh7hMg27PTZTEKgewp1ahitURFiz3oQ0G0IOXbKLgIybtVmlA_4iS5NinUFglTca8k1qVcFVdNVVKyq_jEopV3QVp-VPmgJbIdz7GRtan6RBoPEv5i_F2cGUEVf6uF_pQImWRJD1nkUct_T1UPGs_W5BxKqcXeoCfhX2drZdDR_9hpQZq2p5z7XNNt4CKFvQOPxvN5WWd-fAV-kN1kuD5gqyX12iOGipsk5YA1UEDa9xz4_C10EmOk01adNF-OXVBlc3jWk7WWghmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naeksJRd-hGzgzDlHoemfxwYxIn_zmNSMoaH8R4_OqYa5LlJgjcum9mC-jTGZm70oK_UA198FcxPMp1BQ7AyGzGMxjUIRCuUZz_LIn64U9oC1vpZfbvsT5K3i44Ga3rqXh3_JBTDbgnB8HoT-nQQjNHPfDpDRx31PGsCT6RFOQY4osUiQJ3yoIqsFlvy2py5OInWcS1dJsy8A5XueNbpUOx6UUFmSN1Ya0GfEq7oqodwzSstREvNZ1Veb6-8kdt7UjRwZqovapWxNGw0A-ZnJYIlaLY5dDDBG5EEyymIf7L4T_ogCW5fKY0vFFeGPW46NA-serSGtUkkvJOUcOKIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJsnymRtjoH_u8sw3vxey5aR3O6Uwhxrgj__sxVKN86Zp2C6T8LPBzga5gzrq8whtttgIxrGmdgOC4BR3kHCAZkxkludBb4yjPA6tJwZHRSAVJeNcc4EvxpjpO9lXd_N25BKqykpYQhoAv4tS0TvAmZPI_l3yF5wGyqMnlciw8mUM8BBsCMtpUYCKrqF-y5hHUTO0wRghzZoTJnNpK-WE2yhfz6KY2xtj-Rc3kZthURt-jAzguCEGWeY6wpXl0FkHeRaSYhuGUopS9XWrpTCDjg9jDtYd6Lia36mi8Avln3Q-3pm02g5diK9mBGOJAEjN06V8G9OOUBEu2y3fvujRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=WsfILwm1-SVPByO3DQZLygdtKpDIzyzAcQpe3pRUk4JGBDksnicWlocf7W_ApX2Zi_27nV8IZU1ERxMCQ1R0uDZdG0t_Wa9lUo5Tds4IWpfgxSPGUzkyI4GMId6xZfweMNsrU5hFzvwgpJUuc4rR8X6k9WMOoCDqQ6DGjqotXFYBAYQ-NHelEzpX4P39jlKIg7SZkQbJXkNpklgBieTfy3xsSdR8BLab2wrT1iD0f7570UQjdWKJZDt_5lQTtmW5USBgVufwlxaDlJEHXry8bAf7I_gBd_4aN7uH4oz9rF3cdmSMP39nyEifCvm4rnTjPgrbIFUBHAiXWG5Aj-4Eaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=WsfILwm1-SVPByO3DQZLygdtKpDIzyzAcQpe3pRUk4JGBDksnicWlocf7W_ApX2Zi_27nV8IZU1ERxMCQ1R0uDZdG0t_Wa9lUo5Tds4IWpfgxSPGUzkyI4GMId6xZfweMNsrU5hFzvwgpJUuc4rR8X6k9WMOoCDqQ6DGjqotXFYBAYQ-NHelEzpX4P39jlKIg7SZkQbJXkNpklgBieTfy3xsSdR8BLab2wrT1iD0f7570UQjdWKJZDt_5lQTtmW5USBgVufwlxaDlJEHXry8bAf7I_gBd_4aN7uH4oz9rF3cdmSMP39nyEifCvm4rnTjPgrbIFUBHAiXWG5Aj-4Eaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrupWOlelBiIma3QakMOAtmyMSEEfdtti9QFry5jHzC69obdKvtBJMLZf-7Im9XNAg4PLgvI8mZL42RBqigm288WKe_zy8O9Lk5_3RYq9j2Rc_QKpZ5npcuU9w1n-Y99Lsu6wSOlKfsU8zsd0ZPRrgykPoyJg-UiyOUpH-g-midr_mJBMdddljX2S8cLW6Tpu2JJk8qTkBBOnlIjcdYHKCQO1hMsugnG8CsGj8s--DiSpo-htVkSl3noIM9IisHc_1TLimYn93nAAeadsMrfkvo4LlUywxJyJ6gW9WpklBLXMnerE-nl74xZAVf1E73CMszcj2CQUideJ6ayk3eRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2kd_Ifr9qJt6xJqTn3EcWHvBENs_S_SCh7d7tj4qc7A6NWGEoOL3IDui5GDUHclpZsGakkj-Ra8LcQMItO9X4N_RPd7MKWGpFPwrZa9Mhxa-F7FuSIhS6O72mGrST9NzesSei9IGhXKMO5q4yf19v25ZPyxWv8NBEWTFGWz9NXRllMsw4VcIfbnUEyxdT4MJZnNqdJl4fuqVYZnPuTesDzIHpd70dXC7tbaGgBPfcS1d0D_ae8LXGhTzd8ewTAQLpEmljC78vLfM3DdsU-qmt1E9IXqyYgQHXOKYMeHwYzicDmgO8ShHB6rtpvurvP8Scd6OVX8RdFQGg1pIQvVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrP9EAovq5V2h7y9XgBHBRTv2tcfFEwm4l4GwSqLCIv4oxJKltGUtyS4CJg7O9qdHiau_GebKaq1h2Os4ytRENw5yCX4CuJeuN_QJqpFiJ1_vk_Qa8_xZad4N6zYP2-pPPE_fyETtJDSoeV2y4dgnk285DEjq-Rwf2nwGzDa5KF9PtpqX3mhPjDQ8OhGLrUIfCfCJzG9ymlORGdQg5GGR5zo53M9DleP2CFxcs_rr2Lh88ARKZtHjldrwUiQQV19-HTan6Fy55moCpx4jhViFvCKAykZh0d7FF4MdEwuEQ5ACHCSRjveEn4XyfOPY6rtgzJBAplQ7i5g_ibXfF3_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb9HZ5mVZoXGg_IaMNXvgQdVRv_IPnBZpB1e3RiQN986pkzv5sjU1hvzTjxrov63OFyhCsnlhSghL7Z1ii-YMrDVlho-wRp_Aarmh0MPsdFBSf8LsS7xaenjGrrmvDlTE7i2JdLy1wO9gYitH-3wBVtIs0VlLfkBzuGlbSO0SocvRmCDb3cwnSrn48-FWNG5u7xET1xr4B6HJTLNeKJBX5wW_A7b7mxZSWZnFr9rJheD7suYS1Pj84fZgHmGYdROUGLjqA7kg4Wcu2a34aFaxlDnckzZeq-6lsPioK41jkz3kxh2vjWKTRVkfmNFJslyyUyAfi_Iy6uFrCVNV98uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=lPtE7_h3swckuiCxhRLVFsj4NDceTwA5fJllxv79inqZ_I3oAGQfMJB9_PPbhs7ob7lilTnbQnznRLPtI_oK40WHtYksaT_2turNJwoOS9CJM1v5pfITCRxm19GGOiD9obXlGSaQuugwMUPWIGC4QZXYf7l7O5ySlYcwfMW-PGB6rA193P2qU4eGeVysgi6tRnVoz-s2iHHqJW1KSsrc2bU04H4ZmOe7ZnhhSuhpd-hcIMDWBPCaxSPea5zu90oJVuv56KPjeFCr9Rf1mPRUVhYhiGlS-2xxwr3c4SZWCS2yl8gw0GaVERFrle0_bvKHzmy398BU9cqxMbFkLccQ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=lPtE7_h3swckuiCxhRLVFsj4NDceTwA5fJllxv79inqZ_I3oAGQfMJB9_PPbhs7ob7lilTnbQnznRLPtI_oK40WHtYksaT_2turNJwoOS9CJM1v5pfITCRxm19GGOiD9obXlGSaQuugwMUPWIGC4QZXYf7l7O5ySlYcwfMW-PGB6rA193P2qU4eGeVysgi6tRnVoz-s2iHHqJW1KSsrc2bU04H4ZmOe7ZnhhSuhpd-hcIMDWBPCaxSPea5zu90oJVuv56KPjeFCr9Rf1mPRUVhYhiGlS-2xxwr3c4SZWCS2yl8gw0GaVERFrle0_bvKHzmy398BU9cqxMbFkLccQ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=RcrYCEngIwM_Oa52vZ6w5adFozSB3uQNovg9UbFFDZ9gKhUh0YPE7ViAU58p6WE6EMZoh8p3nShomhQ6e8MhzuitutzsxQCuiQ4te9xxBAtICce58Iv1qGBa63L3TwvbpfmS06VqjX4ihM00VkUVwvlgWXMyM0hYZySaPNutpynBE1D_VqjpBmP-Mup9VCEUaVPsmTtEetjawIF2eDJg_0oEyrLIMJSJvtjpCGoDhzXpHmX0zotxSSV8ZWudV-8qI2VGSQy5mMr2GvfV0fZTwdvrhjNjdSOUeJBuLgoZc1E0JpDj3WRmXfd-yiBWOUFs5_Cw5RmTPZk7rhLBXudspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=RcrYCEngIwM_Oa52vZ6w5adFozSB3uQNovg9UbFFDZ9gKhUh0YPE7ViAU58p6WE6EMZoh8p3nShomhQ6e8MhzuitutzsxQCuiQ4te9xxBAtICce58Iv1qGBa63L3TwvbpfmS06VqjX4ihM00VkUVwvlgWXMyM0hYZySaPNutpynBE1D_VqjpBmP-Mup9VCEUaVPsmTtEetjawIF2eDJg_0oEyrLIMJSJvtjpCGoDhzXpHmX0zotxSSV8ZWudV-8qI2VGSQy5mMr2GvfV0fZTwdvrhjNjdSOUeJBuLgoZc1E0JpDj3WRmXfd-yiBWOUFs5_Cw5RmTPZk7rhLBXudspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op3S2hoywlmWbKYX416ZVajPEuBh7SvTquQiarxE3BE9kvtQEeQC5qjr2XNMfdivEWxPHe_5kKlD_VdKS13lex6siQ0yKD9NragiAUHydXz2s3rEyEAqibmieLPZfGH2vAWOAQbKJ14GP0TJk-y4WJZtxQMjEiXzfsMfuIzn3y65D4RsiVT9lvHICZaRoakywYlKtGIOWeRfF0L5g6wisrWI4ldF-3-EcvcWsLUBwqw7aLoBmX5OtLvwhDnhNmEOjFdhXwvgsWFRoSCxlKSIQnmg5V9M8CmeDTiqxpkoF9lM-9kvy7QfrKvJ3hIQTi-aIqR0sYFCgM3yak4Q22U3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0K3ADzB27HlFiAbaOimGHFTvUnoJEBAHDNJ1-1J7OMMBMXS7pxpAsONnEBvkntXkIketrEEfH0bjTT4Yzz9jqcLjX66eZX_YJ8fmy1sWp03EnXsTrxQkzK4cgWP-aL9NmTqFEtKri80pUhYXxpZNpzP1Jy2-inEwBCnq1rH0gGkmnMVWimoH-vP8ZPpTHDzWiULWEE9z4qMuTiIZq5GH_uzhtnK8-KOk9fsFYhKMxODrJsQSwjXDTq3lUDmSJvmdyIpvrvBH8jlh1H6Vym8RPzZWG25blI3kQfWan_Y4AtBxmvvUWdaV-Lnl41CI5kInCoKYkNauubLGiPAHm7fPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubajCOhVFUeYMEvf6Dvd5pVIMjaPbh7S7cxFRO0pujuuPX4v-zdAj5C2Lju7dIL4IruSshcXa4F2MUe1oFWtI6eaUaFDeyl4FUT6LdHNZue91PcRk23H4x_AM-zAQBhnrt02V0PoVXrmgGs917i2YE-5bYI0N2dZcVZ_HAvVR5n_EiTUE2aWPcenRhLYq_bd5Pxkiq9cRvICTCb4I4QrrMQRvTM142tLQOT4MwTUY4QZmtnBC9RfDPszbn-4L3JrequLW8PIMEjnCpFrwfM5LxoS5r4g2P3sVCJ5w9dRWFXkJW6TfNF_y9iR4MWru75uNFX4nrM8GrGwR5mTKZOHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0hZAhj2zeiEqqR8YIbQg_eW2T2EdveqAWA1WIP1ZWls2WzwE7Cp1j72Ay5P94tNDMXDzcIaG8EiOrRLmfMSt8H1d3nUBdRJ15be6g-_907GEQNqtlWWRwLaUFOvB41LihRMKkzEQeEfWz112ROqfp-I679D0U1-1LVtBRWeN5af5ZzZbxEB8PvN-tMVeM9aLyodwiadwTib1WE_6ATRdSPo_eCyWOzV2CrMRFHN6dfJuKu7Fa516uQAvYgrW7fJ72sgepaMIyTJhdWhZPrNZrgAFmsoj6DIUdXU5r_jTTWvZDKEiKJYtN8HDqavJVhL3lxGNqwwr0UPuylIipJy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-vzM8MbWCw-qhh0ZDZiLGGdKiCi6fzc1CALNASWJNlOzLg13uHcEUFQc4fX7hjiMG6KU0Qo52gN27mvyV6_m5lp64q0zW2B7UfA-IeJlABg6xJu7k5ucJA_JxkzyayGs_e-Ag-W5o8cT6gevLZmv0aAh_B-N-oWgHpi0F-JPia17TN7GiaeZuajQkN5k7WqDQnuyp2o4K2A9nZ5zEKtxHXTTPkCERpqnxgJZPp8M76fTCX7vgJR50tJOaoIB3aLub4xemxt6myoJZHmLBWfdHYm-00Sg4QeXIqvihfPTLM8r23FfEAHf3dhMjBPON-fJPNI8QYp8IcBiShraxOTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEdXJhD_e1SYDNp9BYO1xp_33y2AylHeGgPH6JkDHfJ0dvxJJ0CCWqqXZBJo4JX-YkQEmzZGlWRuEUAJED8LBIPqgzMSYkaMrgcH36ZW6s9PP_n-asjDXn-mEVjwSbA7Fc192wqjMpujW6PkiEQ-erNUDPnwXchLkzpoORQWpE0usjoF1bs852PGO1rJkWNcppQOT7hIamfLl7nYrxY01DXpTX7rOw0xVZoPXea0xm914lc80HEr7aXQr7FqUnuG2-3RwVrpyiTTVrQWoxW4bJCgqVnvauJcd2GfxD7KUxK5mmWUnVtMNx4dT1LnNfQs3VmodjgHeN1b0DBsZNXUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFyDF9LTDlyPe9roViKYHMWaxB1-t1eaBWD5pMDfRFbzqdQuBG5zEgl2Oulqezkvsje4G6oLMeOf4BTkeqaHQCQ5Yr-vLgzjEpso01vkILBF5s8S2kMz05SVikt89vDEoId8CARQo-_DOkT8Fd7HRXnwVc-cPFB7K6Y7kpd6Zlge64cgQ4QIdXqQaZxOczwc_3mDRRnQFyMy0EpXbjt9GQNfPRdZg10CHTrehWf8PsgMlhScu6oDNGlcCyzJVrffqWSwIqNt4KqBSMjBS8my7i2h_FtJFB6BNgY73aO114CMvmU5_wh6soJ9vfC9SpTBOIUDHRDO6QIXGXaNG70mdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0vPVACIqQw6ZqqeJrfYYpTpDk3014xIUpxIH0_igOVRL_3gSBaBYf6tyLd7_vHbLGtCVmcM-YpDI9nJ81nJ1ZH_7V7SCqDia6xe4xAoERlpX72SvVEZ-jlTE7FevOeg2JuVri8DexS8KCS0rTK6c50vR5VAMslDxjbVNLb-ercknKBUjFx3-SKYXsXHnWaWG6ZLq6H7hb4EYkS0itKyUsbi1TCNjwuqhbjxTrGrDLezWpvn3Mb8ZAVHYdVNMwuG2nHRT38KIlJW1diFsf2hkBwI8cahCcc-w2sS6_HN96rgcVbfMx2OwBcFMhieNLE71dti3aiIdCykODKVeUCaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=rSbdWfPt0sgTi6wwsYBnzECIjKBYlWbppy-ZiDwcxjoX8ru9CbotBuk_FKJXATmgA57-sR-RWYY5T8MFRnO-xKSX8qyJJ8ADvhQoWrvpob_NDJz1l_FBYCar4owd_Zhv5wjawb_NWs2FUCdZPDW7JdxszMO81dpDL3B2m478dUkUvtAdslSKDlSfkxgpjlYV1qKzxrQCjiE8DiVd0swcDdGlPV0W2AzRaQzLP6zLOxwYS0J9Tr44SlZqOp6kYHJkdoRkw8Eqsw2Io2MgySKwsOtNoWnqFS1ZAyOPr1GE4fHHt8f2qMO_n2z56rqn_CKSGjw952wAABqNQYajfQyq328NIBa3PoW1wH5PP3F2-QGH9K25-dQa3VLr-unCUYouN0bGOo5MU51WlVWHtco83ac97FC88BQnuUmD0ZJr7ONts4XGDTeLYMSw3Stc8hFpXWzomzbLETN4atColb7FRyvepL4o4nJFTsGMP8uaji_acrYR6jIoV-Hy0b-q6MWeVPNVAvOqbDCtfjVdGrsTrigjZcGlGVrCscEXtr2xOX7RbPjUJF1F1C2Kkocr3Pyl9XrPP7sWhL9PHUH-gcAnfTg14AXuwCURIAVrLwwlmdXI_j8eCkjeGU5NDz2nAwNtklPhB-25OyHbHZ59xFZpjxfrp-ifA9JW8XLm6sG70r4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=rSbdWfPt0sgTi6wwsYBnzECIjKBYlWbppy-ZiDwcxjoX8ru9CbotBuk_FKJXATmgA57-sR-RWYY5T8MFRnO-xKSX8qyJJ8ADvhQoWrvpob_NDJz1l_FBYCar4owd_Zhv5wjawb_NWs2FUCdZPDW7JdxszMO81dpDL3B2m478dUkUvtAdslSKDlSfkxgpjlYV1qKzxrQCjiE8DiVd0swcDdGlPV0W2AzRaQzLP6zLOxwYS0J9Tr44SlZqOp6kYHJkdoRkw8Eqsw2Io2MgySKwsOtNoWnqFS1ZAyOPr1GE4fHHt8f2qMO_n2z56rqn_CKSGjw952wAABqNQYajfQyq328NIBa3PoW1wH5PP3F2-QGH9K25-dQa3VLr-unCUYouN0bGOo5MU51WlVWHtco83ac97FC88BQnuUmD0ZJr7ONts4XGDTeLYMSw3Stc8hFpXWzomzbLETN4atColb7FRyvepL4o4nJFTsGMP8uaji_acrYR6jIoV-Hy0b-q6MWeVPNVAvOqbDCtfjVdGrsTrigjZcGlGVrCscEXtr2xOX7RbPjUJF1F1C2Kkocr3Pyl9XrPP7sWhL9PHUH-gcAnfTg14AXuwCURIAVrLwwlmdXI_j8eCkjeGU5NDz2nAwNtklPhB-25OyHbHZ59xFZpjxfrp-ifA9JW8XLm6sG70r4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMbO_-cLmmXg_AddXHX5HWpuUmj-_uqBLak1r6UWQU7bf68EbHObkoik39C012_os6AzITbiJIgvmgjrWkxKdnQjzDiFa2wNt-rxP7bip0-QvpBYyz7yq2SQIv_4RJk86C9mtF-DdO5FdbpI77GBf-KY_jtmwgpL6uT6eeVOXcRbwC0iDOEgnV3I8JEAYjtgP4E8CpVXHIAgeAa20zSuo2O5-RzOgjov7RPh0TZy7VL4kvgBLdCC5KSjCVMi4xPrI4X1FTXhuXzjC1fdRgS4gymvfel0L8u6LBrluq3PCo4-Zxi7GiA_XELMtwEe8-ea9KaFwi3Swv2WaPy-1zkGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbfIwJ4h-VbWRnSDP5DPu26TauIWPkRZKQm3ydK-d2XQQbXz_4Nxh2_iBskGI1ApGRRxXZrWMJS-oriFGyvBjWCSve7psoG8qGCX3ef6XIkkocI0Qx2o4bnWLtiIKN7m_Z9eC1aS9ncKIXEW57xVsnS9pMJg1M2Wt4RnCyO-Ze0NiA8VPZsgPdWOEd6ywuSM1emDwUB5Tle_dsMI2h5Ld5DDmh7e1heCvHocZWNbhkE4VM1pt-vDhxat-Kqrr7yHA-zno0MYsOHpsphVVMpw6GxHOQHnVkCqE0JzjAiGStk-HbhccYzsJaT6Nw-NCgxKCJNBy95fZmjdxMWAu3RX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPT9QVOt73HzranE2tqyixxo-451pUyMXtNBU_Daj1oTu9nMeUBb8AbdmSd0q5jIPYFwwe-HoBGw4IX5utRfo2u0yugPguT-P3pYuHfVAaJ8ZPWWgk-3Eckoi5xhFuEUglmCoI3vPPEN-d0kpyBozc09grrzMA0TvfZHaBLLlCYx49gTNBw2oIuZ_EV5zDuHr281wKYEIh-g3eFTXe411piZqEy1kgVt5QxksWYI93RF9eQ9-yBKPQ7jLf115nwOONFAfLQtlP0qfqMvcg6ZmUTCpR0PekURGN_zSRexhZOzPxRUlVnbEFst8NZSQQfS_i3rOtZ1T5khrv-3T6_HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6bYWMVFr7Sw0jEWoYICZDW6Y0SO2cM-P-6v_7WlYU7mvNGbHnr7NiwhayMLbPcl8J60sFkVGh-zS8w3xuOQo48gTmVvVCn7j2GMip3tJ4osqz9H2diCFjjdHlVUvaGbUtnFPGO3RkpXm42FA2JVB9FMOaQ7KdYAgQFQWKuGt973lbtuS2HX22IYr09ocl6HrHarwPeLbKCSAIOP5epdyc3Rb5JTnQYFDepQ-seDxNziH5RMDxSokihVfdXGybi4RF_BcM6XQD9DsSq23X4gfeZe463ixRYtTiZAv3s2OZ0uRBDSOC2d3DPl6rpz0NvI8bEROL7WOmPEFVHXCzhxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbCggMG-xzEKFQ_VfAz80mkdSWqArT7A4USkDua3pRh38doJGNSh7hn_0yyaoKtJydudHYLzK2fs693JXZIYFPB7yYiLKfYCbuxuA9D2UCcB6jJRsIY1P8UncTq2C-B0948ivrRD26cE42Pg1F3ZGE3vJDT-gaCmG9d3owpRm3k9Lmv-DTeXwhq9fzFRrjStkPu_rsFtOzr9TMrywaLY_PxN1DcLQRBd77vJiWJHXG5Q5fJiwtk9sikKm4ZidLluMMQFUuHmnUVc6EIONq7v7VDmuyrEuRshRjQCO-qxg-kk-tTHvtxRTvajbwBgqha0qua7UVtIlCNRfYzewN50Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sadt7UpM67uAvVUp7_YnLD37W-1570ULFR29q9AJqRg5zEzPaR-bQ7MSSuzaBgh1MKqsN9E6C5aFw9FJulWncw_97rvEBA4IJN1y5dh78LQsNMDl_CGPen4EZa8MkO_nEVannVjVD2t6hlq450PvkH8WIjQp05Qni6IuKLTXL6G3KwDkvxbHNXx3NxADj-msjSNl1Vv8OGQAldeGItrgt7duSNzrFRte5wEBsu3Mwk_C9_dfB9u2tW1DEZrq3IAhmxQHBMT6B7geSUp18jQV6bEHO27xWcJMnsdqKCQH2XIPNoRiqR0UCPikmzAB5Vqd2OvpIqPKBQJW9dP3sf-BaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXEv5ZHEQAiA5SjSIxx4CLHzVvWNX4sWRDFwYYswBeVzdeu4Iu1MkKGhV5F4An6nacYzGFCOYXH6eZeePlXbQvwYDLLBm-jI1w4WunhkkUQPEuIn07O-ZVJcrlN4Lm00xs7pDNMl7zfsCo0Jb-HCOS0QgWRFkBQcaKWvJ43jxNAj8yQaZUrF9PC_0AYrXG4KRaLrozGA_Y5BzaHEMaUbGjHSKyk64cQamNQTTH8XQwFIvbV2FeVHicIoLf3-5hKysTYQXZO7DyaB-GL4tTYb_nFfz-vHpaYTxPEEBqa9aLX73XP9TPZ0_4uysk3BU66LsaeQzhOtgMs5yOYEZA23lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=NIDrbKrSP-itL9qKc6o-biCaFH8z11m5hDn8vRmrdBkavPVAG5xFpxuYUrF2gownqiKlls2omQ5p9timmu95RW0zmBxVNdNJrtJfY0ZjdZawzb1tSKaoBoA7ygw_3Ww8LKfK8dkHKjHfwZRbqF5uUplXf3MrxWdi4TZBMNRyhBNSxVVHRAV3dIDDPqSOk0j8UYXtCI6o6_z845OnFgMD3s4pg0L-P63nL5edPSUSLedVBZdmCSO21zdaijAu2-NlljYQ8jRsK6uE7Yp-DOu7Yu986hM3nVz14z9TriM91Wwf19N85CLJptHBkdcPuRBfqw0b8m4EcNdmryCmxkfh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=NIDrbKrSP-itL9qKc6o-biCaFH8z11m5hDn8vRmrdBkavPVAG5xFpxuYUrF2gownqiKlls2omQ5p9timmu95RW0zmBxVNdNJrtJfY0ZjdZawzb1tSKaoBoA7ygw_3Ww8LKfK8dkHKjHfwZRbqF5uUplXf3MrxWdi4TZBMNRyhBNSxVVHRAV3dIDDPqSOk0j8UYXtCI6o6_z845OnFgMD3s4pg0L-P63nL5edPSUSLedVBZdmCSO21zdaijAu2-NlljYQ8jRsK6uE7Yp-DOu7Yu986hM3nVz14z9TriM91Wwf19N85CLJptHBkdcPuRBfqw0b8m4EcNdmryCmxkfh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=M64mVgUazwBcYoC-c1Nyfn1JBSjCqkphORCP0cXdlbl28TuS5uXA02yL1rgGdqnEBHNGOrT860aHLp91vjqExOYCDC4Pi_WMAIeife4n0NNEt7AQp7Dr8FuyqYMeIgTIOFfOU2ANGn4E0gqNZ3FYGyv_DcC8h9FQ-UO5nfBstlU7_K3XTUca9-N98iBOZZTfFWfKTypYFawL3_2cxiWEZA21UtqbZPgrv9Py9oOQwdw2Y3Mo1rIYFo9zh_8IzV5LfahZandG6cSwTuBG9UrSWMkNOFsiitSjpWPC9UTk0QMFHNSPhjBUBxhXry9v7Il23nP709CZFt67hxDCE2iTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=M64mVgUazwBcYoC-c1Nyfn1JBSjCqkphORCP0cXdlbl28TuS5uXA02yL1rgGdqnEBHNGOrT860aHLp91vjqExOYCDC4Pi_WMAIeife4n0NNEt7AQp7Dr8FuyqYMeIgTIOFfOU2ANGn4E0gqNZ3FYGyv_DcC8h9FQ-UO5nfBstlU7_K3XTUca9-N98iBOZZTfFWfKTypYFawL3_2cxiWEZA21UtqbZPgrv9Py9oOQwdw2Y3Mo1rIYFo9zh_8IzV5LfahZandG6cSwTuBG9UrSWMkNOFsiitSjpWPC9UTk0QMFHNSPhjBUBxhXry9v7Il23nP709CZFt67hxDCE2iTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i93FXeMtl0X5_EtOkS8LkfomVzK6iHbGEAu4kxhByULuRLzHrq9Fzto7xjq7h-_0yRwvqpRgZLG0lgMDhBEKTEHQrYxUl_UlBjDHN4k9OHHyTRs3pJuu6dZnkGE4wftc_q_g4OsJEqtekKtATSsDq1bcwTUyd-ab8M_xbN92vS7j4a34d5Deg1UTw4E9SWIrW_1A4ce1cIP2xlajCwg8WsltETQG7PE4Jip6wGfzyiQc0T5cVOACT7KrCSW2eLxaBCLy2lOF_OlJeAYxpwetzk8jYDYdW_y07G0Bh_LXftFVtKXXcX-0JMlA7-icYQGX1dt7_o6gOQmhNHoW3cmwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4-cldz9qS2rzV7adBxHuQv44Rv8FZH3W2A86HjJzfGfHdEq_WNiYW0LMfDqpA8aU13gUqY5aHfaRCvB-888ojdhPI7Y-SPD_Q-NM-74y8WmVSS062b7Q_PYAoRagrNUpJJvwxOD7zfyW3tu1fhrmMQcCEk2n6wdXK_rnpx21jot7dPpQNOYErlc9TG3aX0Gs5hdJ24PHp07HR2ZTnIyGTCQ_1bbndA1ACeoWIfQfU_e6Sb7onmpHun7_fHn1omBwhzKi4LZnTjyCabvMjnYjAKlcYujL_4564Z99YG4tl7hffd1-io9mPvtcf__4AE2SGWJR_RHCzooFUNeTxZWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih9HuyOA5wcHMooP1qMfDCVZT9RzpAlU48leVtWJljAjzKWYHoxrvNhOeUhYdX9QZCAPtKEPP7YHgOtVCNN-AnbfYcWC5BSYLGXriM37Hy8ZB1cYHf7QXoqKokaMnlqfYO-_QpMZ54p4vmKwjs5tGubBDSSn7E_MwWzqtuGswoSyzn2t3iRlaCM44hq3nWkXte0LIr2Du33Qzu2TeaAs0OSPpCM5Oh9Jc7D2fWzZ2K3tIRLsSlxcK0lP2-czwf9bIAmpqrApEotTr8H1Qx2oriklE0qXHGTi2r9Zi5_mixwpCwhTojXwanHCXE_uWS-qSnSROP3msI1vjyIDvKwrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSaD_MlfZwlAFSHpj5kqGJM_EdPpv_vPc6UEcPUJ_-uTDe7dCVqeoG-W7XbagmCtf0wiUi8R7PHfz9kuWXEAoqGEWfgPTQq3SX3vSaF0UdCL3L4xXttv8bb5w1NFCJz3awe9pSdWVG1TOH0OOowwGNz6I07lGVFdf1LilHpi4aSqf0vyawn_GNn3beHND6kbiduevcnOrdwwm0CrJTpNsdhYJwsEEEGcnqjOAC1rlQceecidmuI5p5l6y0AUG8A5v6U3y4kBk7RqpHBSdOOL3aP0Rgy8dquFtsc2Op_Zbenly8HdE5qgMy7oB6MhGTnZ8hxai10dnGj9qMbhtEh88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4D-gYPHEFBTMz3fZykAszSygIYHFOyx2QpkR3L5rLziVuduyGraIV6atNmwYZQEIS7x5hgPn--Iyn_HWbeuJbOvSsQoDGDaKiPJ4ddIyNPbTqvQpCszjrHFtMkX4APSDDIl0VrDSeKuc72rlswMw7VJa2NFQXSPQ2dQJD7RgCyN4Ra_3pv4TFIpSQBZH3gG6ZwAx6ipCuoZVdPj4Jt8GdzUTXl4Q6hBcRnV3eiStWddwF59q1-45D3x5MER8CZyRI1zIODwZhPwjZyfql9OR64IJ3LOh7uI-c-psZFTj6-3gLGGHwjq-nIY5D32Z96hFf7lV546kHOShSUfwk6ZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjjCbhZHgryRMfcl-6_mo_H0h3hbc_BcdvdyAAO6-drOT2V4izEIjtavcYluefusWhyP5zQJtdy6r3en6wZRfolqK5Q5mHkK3PXwu2diEtH2GYRK0Iii_J5wcK5gBxop6NmgoxSGaofoFBv7B6hiYhiIEpKGEcKZzGla0m2R0bq84vvUJSi1VAviNWWkhoWfaWwHIRiQsymJSjdgfF-zqk1BxjO6C_FDucbMR76XZHl4fqHRmIlNhuu-bvgXU2QAtDS4Nbx1ad2rOxe0JU1EbvEnmrIE1NxmNUjCZee5tP8DuGF9ga-iAQVJSrO6m-SlnC1JKQqQxOqWTiybLpCD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8d5WH4yubscKUOFF-U2RWQMa1-MBsqlAwGyrZl1818m2aX3vurLDyGVNjazleo_X5Fl8oubDrOWmc4wf6td5lGr-3NtopNILSPUzLAlhbp2FJCnfCoq-u2dFP6-Qm3NkDK2aB2HtNlJ8VeNnxqzOp_YDxh6t_8i9duOHqnMTF8wh4g3LKWLR3v6pChjDMXRR_cO1rkWN2FApIKVUKBO11a7MgdFSVvvA2dz3JtVZsyXGN1KcUeYq5Ht_H1EIY-w-J7ukaUdekKI-Ex-P2heThtVsmE6c6F_BC8xmK7idzKJSZufODvCb6Kgh45GxRQMVG4tIysg2o_Ni-1eKDzcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=FBPWEWPgR2dnd__3h-zGUdB9tPxG5RsHZQrXhXB0F8hTA6uZbhJz2uF_6LDrrLoTpy358XDgmE2UNZMdSoMPtbtp9mflqJvqswmtPtGQ0Xg7tLSEDTDKdEqXMKL6HeZ1Clp8cKyiOqwuTEpjsD-DJ2qweN557AbjOIJdDhpzExOLO9GwByQJKaOsVazwJMFS1HB7B8PA4fVDxJ_3ip7UCEQzJZVEOFMpDFuzHsLECZD42aB889SnyvN1Z6JP28st5C8gEXGWie4GDjkNoLx8t_bJp-UeeMOjI4nbDscryGf2mnkzsUWPiA8LU7XJtadrllWAVwhd4pcapB8LdR4VOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=FBPWEWPgR2dnd__3h-zGUdB9tPxG5RsHZQrXhXB0F8hTA6uZbhJz2uF_6LDrrLoTpy358XDgmE2UNZMdSoMPtbtp9mflqJvqswmtPtGQ0Xg7tLSEDTDKdEqXMKL6HeZ1Clp8cKyiOqwuTEpjsD-DJ2qweN557AbjOIJdDhpzExOLO9GwByQJKaOsVazwJMFS1HB7B8PA4fVDxJ_3ip7UCEQzJZVEOFMpDFuzHsLECZD42aB889SnyvN1Z6JP28st5C8gEXGWie4GDjkNoLx8t_bJp-UeeMOjI4nbDscryGf2mnkzsUWPiA8LU7XJtadrllWAVwhd4pcapB8LdR4VOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGeuZstLHQ9Jg9bUWBGw--dVa461jVuKABSJiS3UiqTCHkUEaLZ6WuGuA1K9I1NOfTZmD_wRV3e4Lkk7gzZD16BGh1u2x9QlSArrYyjbNx48cIUFoeIe8Lg4YYutBocyg7ewD8AwrKcnCMN3-sfqhE5dqRp_jrdY8OvU78ZrccsvVS1wNLz0pBeZp0S7vbiGCB_B-e41q6dxwjJg4mgZp1VLyBHahXXrycRVARaZQWemDYa0P7RTdUUGFYifACXyRSTsysR220OazRYJrbc1rDvA8MbVRDssviBq0yRGvKlwCbGnqlzcB9DXMnLPR0QrbDa3pbDk9zhAHXJYBfVsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=bs7s5RO6vbB_9fDJexgtGJ_uCF8J0gQ1uewIT8-zXeCleGw9e5mMk0MmUjeUBIUJD64U6HekZ15lHmOfyeA1MJLBaqaIZPkFm_481jMD3v7ixjQ5i-BUlKh3L--tjDWOcZwOF4vk4HeT-tb1p3RX6wq4rxD9J6HQErSp7HgP7ITA60d4J6rOz0BkpvRI8IBMMSF718O5QvSkQrRDl-cHSIuz57Svx-JMetWbazBhMWYoBG0xIyS4Q2sDsiWTIJILoPlZqHVIBh-RY65WAf9y50WR6IDo8WaCIbr7lyQurNt52hPefbpW7eskmCNFXM_s91DGYOBHnHinh7mK66TFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=bs7s5RO6vbB_9fDJexgtGJ_uCF8J0gQ1uewIT8-zXeCleGw9e5mMk0MmUjeUBIUJD64U6HekZ15lHmOfyeA1MJLBaqaIZPkFm_481jMD3v7ixjQ5i-BUlKh3L--tjDWOcZwOF4vk4HeT-tb1p3RX6wq4rxD9J6HQErSp7HgP7ITA60d4J6rOz0BkpvRI8IBMMSF718O5QvSkQrRDl-cHSIuz57Svx-JMetWbazBhMWYoBG0xIyS4Q2sDsiWTIJILoPlZqHVIBh-RY65WAf9y50WR6IDo8WaCIbr7lyQurNt52hPefbpW7eskmCNFXM_s91DGYOBHnHinh7mK66TFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCjR8AJPeVqaOKu4l6kJuq6EByQHLlHVHAlK1s_RNLMZxAU14QpnIppmDtipjjh2D0AciIIwFJjkjZlQu052_P0e5xY2mcl_9t6AFDqAFLAzZzKZDbt8xHJCaBmKZgRPjjdmfaesFE4AmhQ1vhCrmA5bDafUoX1bnpMepudbKUt_lU9WS2s02KHNCKb1Qhz5GSRF21P3pcxob6vX8zge_QGlm2pevT7jzgrsMJnbTpCXpsIzyI-3dsOVZR510Dm9cLuxxfNt6KNjsyBaXJ7QLaObDz_guarjii0LX-0u7c7PtEY-HA-k5wA0DLWzuOML2Q7Xzie1qUmd7UCe5rJ_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=dGMCGcfxDqrDTn6rHBVJNeYfBwpdF0I0VqMiagZ2WpNoh5OSIumSEwczRGHiyU9x0XGNJb7pY3tiTG6qPefH0-EgO1SJ1j73JYLTY9R8FZp5FCgFMB5TyFroiLE-w6vdAAL_GGrCJaqyWT5PN9zuh8pZUdiKV2kA12L7-8WuxhnWprSCpwOh9wm7zY2mQHTJvfOboh_U7Ze3luj3LaWO5TLV_f9j4wt8h74FKQZ_7W69ve23d7PU3RLg9YUgZjIPOBRi-BUTusgrL5yPI6GdxlULAQp7A15thCMJ7reD09OnUdrrKjZ_2hM6lb2VOWt1FgH08ikZEvcnu-J9i51vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=dGMCGcfxDqrDTn6rHBVJNeYfBwpdF0I0VqMiagZ2WpNoh5OSIumSEwczRGHiyU9x0XGNJb7pY3tiTG6qPefH0-EgO1SJ1j73JYLTY9R8FZp5FCgFMB5TyFroiLE-w6vdAAL_GGrCJaqyWT5PN9zuh8pZUdiKV2kA12L7-8WuxhnWprSCpwOh9wm7zY2mQHTJvfOboh_U7Ze3luj3LaWO5TLV_f9j4wt8h74FKQZ_7W69ve23d7PU3RLg9YUgZjIPOBRi-BUTusgrL5yPI6GdxlULAQp7A15thCMJ7reD09OnUdrrKjZ_2hM6lb2VOWt1FgH08ikZEvcnu-J9i51vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw4wKvPI5UWp7xdBsBmLUkYmmVDVn-z4gHDkyR4XOOZZndBwUEat3jjMB766vVpCjkNeiRTQHvDbb-6E9KiQzncGtKYg9gEXHJS9HGGwL0s602tj_9Zh4hT-waNMaLAPki8ZRH8dvmae2UA7zZCKUDMvPcvGuot6pZqZHj94UFBf3y4257mM3ParIVJRonfgdwaFwZtjpughM2GtpA-r7CJUtlQuci-2rqC9Q3zWjd7pkLvJ4uUWdl7Cb5jsBhsK7SO0zzduelyxevIBqLdzY_cnMLDz2PwRNy7QQuF7nu4M-ehoieUeBNtym2GQkfQDGhR42PVnFfkCABf__wKg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgbyxW-215RbuI2wX-wXOFL7aZwQlW45vmvS1ssjCDWkVehVDWradAGkHLCmfxuFYK8KJbFo5XZeP8edeyoX9yJz8hbVUWg19G17DLWUBb0tyHv74DpJnFbORQ6fVa944Mg_vEkitT8EDjAu7wb4v84GxuYH80PoJVFIVDyUVdOItEsSsZosxh4JKZZlepaxG0_JECDmVBjemHzgrs8iujG2wbnCUNB4zuw8H-xAbHibBZEQAvNi_QIW_OeFG9QeEgVUcYCSidqCAHpbiyWtny04-ykANxFbVcuPJBYlFRSjP1TrhSV-MmMVG5xpcAuK9LqwVnG6wEnB5OSW261zzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS9nhUIYQpvkLk1VgwmyWsoC2mnixxwF5XmICN2Tr2wYGM3tIMS5SYzmCJK_6a1sZC3qw4msh9GC81cAAUDimMG554KCxcGhYmzV46rlEboFmNI0V2hTMoQfoTaiwLJYuOxCrZGq93LBXkXN5KImNpJYB132VQrjbC-nJ8t-TsSlH3FA9AhJGH-qUY6FjBzVD_7GV4wPMRNWTGkEVHfJxND-qcNc7I5ru8-MN-TUk7Iv0yH-B9BZeovlT3FpOy2m83VWjRsu9GR65mLdlOQbGAgnTUMhMGx0hXx0fVi8CRxq_S7D7ZV0pgon2_2L0TqRC8zAeeIiKR86LNdhtZULyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDYFFf9lMVsgKoQ2UUCBdEa5DfREJwonkPAWKYjgcbJ7sRE8NDA2593Zgr0FgCY_33E-oanW_Ca_O_dn-OoLUCFXg6RZZgLHTbUJiy0S7jTkPqboASZMU7VovD5QDYIsrhbd1Y9dYDmCAf8ernCl13e5uIg66MLC4zMFVf-S_KpBFXUQsVNA8M8xtsyUz-MXBwXjEgFDpS7UGTrYoeFd_bJH12ZRPXO9YJbGFFtldcFFuCQxqKZZ5gyYWwPFWv7HqzMaG47OvbFZ5i43EzDDrPi3M1uG-VCesp28D7btEf--FFjlX6TBLle5lNOazWgGm7X4AASayY4KVWx_rfAqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6K43NLBpph0qxGrjYyCE9Za_CZKi0ROnymeJqwV4OpmL_uJKpcEq3pPmHH71Tr5V1N6V7WOi3V4Ps5UFl8hhI0hnlNm_kB6heIRghroA-2GVt_K4od4RJDPUwEcYvrdJ4FdX_Fx0-RQ_5k30SBrOj95ZS3eRaGMm0byoV77gKE8Yj-KtGe-T66qlyHhw7WekWDr4nHmDY6gvt2gx7ajyfSde85aNa8wErIWP-dp_LsMSD5vQZzTSIYVsZ7LSBeDhkaWKNy0Fe8dJl0gGb7ZUocM_Wb2YtT3jCVvXdTNi7PLBxvdw0TfpbKMrnY6VXKO2NAVzUPoD5cd1zMtLzw7sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTiq697XnCpojAs2e8LlRJu5xcSZ52V-XEa8MJr1Ri4qzUGfRvGNcNqWZ0H_een3PSCoUY0PX4YHjHdP_KWOYv-Wh5Cp3XFphtr9L9qR-0T7zz3EsorDA_54EZou93F01uMVBwRzD506jSuFlqZCoN3HYwmnLUzi0U1QfgA12qV_Nb0W7f0AaxEmt7rOaVPZJlxHCH2pbS7vkVi7w80nfEoPNXoG0xfQG-P1sOb5nLVEKVHIWwXbkN79jxHnmNhtnuJHn2iWJOn1bXAx3WjWNm3dfJEtBc-YGmhOpcf9FXGe8xzRpcdpcxUhN_1eSUQfRDkiuUa2A7MUtt5TxtQB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=iorJZ3xpKYJwlFWbWe684-Dy71TWij6a28ZL6dnrCtRh_Wk_0CcElTUnlNkuoioiST2YRueRzrCaAuKEr7J3ARnM1u6HDObbhWSOiPcbGy9tulIyW7bbWEnsoFFRodCBhfUmlvGMwHsgIiZjo53mfLo6Y9xZ7iCGw3Ax2CkTsgn0vBsdzERRUPJK1tlQTq4qH3euCi89QOBkGTX_vrg_Y65AARlHdm9TXGeu1s_ZATh8DLkNV9-xWfrC58bUDr7VzYBesJaZkPdeQtKE3JIK1-fserhDbfix24ALNkbqTdreka1WF-c5pTqMuPNnJA9wZued1_jTWlgOlYOSF7bbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=iorJZ3xpKYJwlFWbWe684-Dy71TWij6a28ZL6dnrCtRh_Wk_0CcElTUnlNkuoioiST2YRueRzrCaAuKEr7J3ARnM1u6HDObbhWSOiPcbGy9tulIyW7bbWEnsoFFRodCBhfUmlvGMwHsgIiZjo53mfLo6Y9xZ7iCGw3Ax2CkTsgn0vBsdzERRUPJK1tlQTq4qH3euCi89QOBkGTX_vrg_Y65AARlHdm9TXGeu1s_ZATh8DLkNV9-xWfrC58bUDr7VzYBesJaZkPdeQtKE3JIK1-fserhDbfix24ALNkbqTdreka1WF-c5pTqMuPNnJA9wZued1_jTWlgOlYOSF7bbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NICurmn7ZWH6WMA9qqnMGxEfGTbc6at55AzYDD_O76bXYUbNjPIQORTA3kto9eUbYG_EDiZ38gWtUqyL1rZRjygr-D7zu-IqZXB9QGSzHT7Ou9o4kedutApRpcmRsxIWoPkiorGIgrqHgHSpKIoAG4l0o838prC3BcP8AYCuR3c0Fu7p-9aEoontE34JdgpJ5welphx3-JtddA3K8Liy67AxPpvYghxgCo-P9H8bJNBmkGHYxMEpI_KjwQl6Dr-Bv3cpogmVVO8lqEfdiP49WdmTBdhjDTkiuuWvkdJ6j3B-_BtGxa78RKgCzR0TuRgHElOb56P7RJlagufUPlgQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy14_jv-E4kznV9WxOdz54vV4wqpgd9gYmuvW5quTwUmx-iUVfLuCdQpvRBWGsAq9Qaa6mxuw9PywWrIyDqf7gsajsjDhbtX8ARFBbyaDZo3u-HPPOMKp6nGqLaV1IDMAHZ-wbFFB1QvUONt8XHxlJg-5c8hCX4qRl_YE4Y5F2zOTR3pvstlZDWIKnY2BpuqX-X-de9GvuN6Se6X1B_4oaW5ieK4y2Qx-LAmxC8nDceYQSrEf_svuyIR9gGjSuBIzuEECOX8sr3gLzoFrDUIjt1u4RITJ9O-yVfN3CFtnja2F3brMMDQeDOkZDuLXquTGjese1Uq3vYIVwCBY36vAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMbNfx4cbDD6D2VJfhy4jyWh8zCQe9RQEhv2r81tMHsTzLldSM9mh1Nfq9wTX7RvOPELnN39X77G2XIyY3FTlqusQkAL7dFg3_bl3HNmcGxuTM2oStCoriY-41nOUJmun1aUE51np1vJIkojNz6Qi5Q0PwBXv_u2XeF276lRAx2CVR8NerbtBBDZbAuWtkqY86_YMWo2LZFxWkzZZmLE6JU9yIPOwJddXv2hdg22pD0K8j6k1XjTCa9JPW-ERT7JH0jzU28iO2Fa22G8n07uPrQjQsupnPcMA5qqJw2SzGUd9SjoCoF8b7eXpSOsdMi5pucp-XupHZKVWjyaGhrr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR7Jy3yXBVA2svKABYCR9LwqyF4xa_CO3GZjvXvCyCr2VhQnszk9s6ockzm_UMVx15cxVlk88DK7yhhHl_DFJyvOv5vR1vUJVqn40lSPzj3QxuN_1XJMAfZJ9Ic67aO3krp4IDl7LUcIWZyMJZCNyB0nyQTiuFVQVu7abVTIh-R0-VFaHk195rzYLPrzj_2MH09kxLGhaSDCuW8cT0KQ5WXyPSt9V5hJBZjDyAJOydjYbuzBfvUtNWOkeYIhe7ffD8ebafYBIWeHZKrGJ5MSUepsCaTC3yCAR3PJs3W0kr7YUjCIZl7jgMVZ-Wy3wGDeMTshs5JwX5KEFvnsiyxDgyMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR7Jy3yXBVA2svKABYCR9LwqyF4xa_CO3GZjvXvCyCr2VhQnszk9s6ockzm_UMVx15cxVlk88DK7yhhHl_DFJyvOv5vR1vUJVqn40lSPzj3QxuN_1XJMAfZJ9Ic67aO3krp4IDl7LUcIWZyMJZCNyB0nyQTiuFVQVu7abVTIh-R0-VFaHk195rzYLPrzj_2MH09kxLGhaSDCuW8cT0KQ5WXyPSt9V5hJBZjDyAJOydjYbuzBfvUtNWOkeYIhe7ffD8ebafYBIWeHZKrGJ5MSUepsCaTC3yCAR3PJs3W0kr7YUjCIZl7jgMVZ-Wy3wGDeMTshs5JwX5KEFvnsiyxDgyMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=AOPFb3XZadxZC2Z-1wJbUPZ40bn4auQah50M94UqLoSXjvSj559L6FHOphDxdyHc6Dm4ohxzvAE_u957KXeAMQa7sZWX3-obtBftBU8BMtf7v48lckRWZvkQaNIr-FSzKKZrtQLRfx5q2sg7GJAU1cWUBoQqMlQ_7UagOKFKZkjIoBwWVenx3XT8nqo__v9QIkjdmROGjvDOPFFJ0Iwzr_N2QwqFW8nTb6oi_Qre5bZsgROXKnb1iVTddrkfajFm1L_IimTxEbwVoZ9WZyojBRkurSxUQfU1dZYnGIdV6ZbY_dAKiDVr4m393R0JnQpI0ACKM8vWzLblZq29G-sFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=AOPFb3XZadxZC2Z-1wJbUPZ40bn4auQah50M94UqLoSXjvSj559L6FHOphDxdyHc6Dm4ohxzvAE_u957KXeAMQa7sZWX3-obtBftBU8BMtf7v48lckRWZvkQaNIr-FSzKKZrtQLRfx5q2sg7GJAU1cWUBoQqMlQ_7UagOKFKZkjIoBwWVenx3XT8nqo__v9QIkjdmROGjvDOPFFJ0Iwzr_N2QwqFW8nTb6oi_Qre5bZsgROXKnb1iVTddrkfajFm1L_IimTxEbwVoZ9WZyojBRkurSxUQfU1dZYnGIdV6ZbY_dAKiDVr4m393R0JnQpI0ACKM8vWzLblZq29G-sFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=g8N2kcZRhi7ojm0YmXqRKlI70kPpJzy3p5UaWRalkQ0VLg-h8ZB5KZIsZ_8TQj_A-C_ltqcw6O-HFSHhf4_l6Ny4CjwF3MhyVBeHHil-ALX1RZHVehc6AExmcq11O6BSuBHaikbh6EVQJsISb82q9Cx5eXE2Ff2du6EtJ4kdNp-2FKO6KF_8ynwcKmH8iGdDL8YHH-KSQjFWpyKRoG0Sc6WwzB0JELd8lmAe4YDcH02nbiGzi21UDekwIBdbBaoKwkit3h9j14BFJr3Yf0FZ6sTj38qIT3ewl2Sz4lQmNfC-OiD_ijqhgWNxpbCmg64JaRkK64rnydhqF1HeXDgzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=g8N2kcZRhi7ojm0YmXqRKlI70kPpJzy3p5UaWRalkQ0VLg-h8ZB5KZIsZ_8TQj_A-C_ltqcw6O-HFSHhf4_l6Ny4CjwF3MhyVBeHHil-ALX1RZHVehc6AExmcq11O6BSuBHaikbh6EVQJsISb82q9Cx5eXE2Ff2du6EtJ4kdNp-2FKO6KF_8ynwcKmH8iGdDL8YHH-KSQjFWpyKRoG0Sc6WwzB0JELd8lmAe4YDcH02nbiGzi21UDekwIBdbBaoKwkit3h9j14BFJr3Yf0FZ6sTj38qIT3ewl2Sz4lQmNfC-OiD_ijqhgWNxpbCmg64JaRkK64rnydhqF1HeXDgzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=Azy02fOT3qqFJ8LE5ca1Kq9NKNPIboN6ZNTmZUd8Dpsce9COKNGHDOD_mw68S_OKpESfAiVcqg0djKJoHLGOZsYRFxuQeJCSfYwMLyr_ykvBP0n-xdsG87UPJ8ihkgd0XIl0LiNx0JFjv8Utef2VupXn7W3FTn-M8OGpGa0ytSBKxUef89s2Sv3BeeWwsO1G3t_l610rRtyCylFCwBLqDDGt6FrQN1wcC6rKb6xkCBkzVGbuYsTlvOrWBiHpv95zspEbmRJoSgAb9LGtMS6AJLIK6NuEqF6b9tUQo-SYKBYtbRH2k-YgUdinFJF7bPTBV6LlOih_Ito-CE9o1CaqoXjAiW3_IkJuoT8JseephsiaavdP186wpTRo4eJ1NRC0qAnITW6lfSZPEnX01ZJy32qrKNmRek_EbAnOG6yZ6htbj0fdYZctuDx__zM8-0JLRy7_6ekqwCHkweC7Z_7lDaPMAljIMAnmswb1a39TY-9oQVyDvFnuTjz5Xgu8wrOr1vojR4Y3bht9JaphWDhZfl7Uo4V9Esm5t2f3Z_9myWhyGVoNZODeMWMHjtNRu4dSXWwMcdNM9pIlmQgf7WahxLEQd29uKIjABN_mkI2COsS3pCxnNf8ZayXqSyz6VldQ9XaGM0CpeP6x3AKoRMoh4gqtMDjvR--KDiVMfCjKA5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=Azy02fOT3qqFJ8LE5ca1Kq9NKNPIboN6ZNTmZUd8Dpsce9COKNGHDOD_mw68S_OKpESfAiVcqg0djKJoHLGOZsYRFxuQeJCSfYwMLyr_ykvBP0n-xdsG87UPJ8ihkgd0XIl0LiNx0JFjv8Utef2VupXn7W3FTn-M8OGpGa0ytSBKxUef89s2Sv3BeeWwsO1G3t_l610rRtyCylFCwBLqDDGt6FrQN1wcC6rKb6xkCBkzVGbuYsTlvOrWBiHpv95zspEbmRJoSgAb9LGtMS6AJLIK6NuEqF6b9tUQo-SYKBYtbRH2k-YgUdinFJF7bPTBV6LlOih_Ito-CE9o1CaqoXjAiW3_IkJuoT8JseephsiaavdP186wpTRo4eJ1NRC0qAnITW6lfSZPEnX01ZJy32qrKNmRek_EbAnOG6yZ6htbj0fdYZctuDx__zM8-0JLRy7_6ekqwCHkweC7Z_7lDaPMAljIMAnmswb1a39TY-9oQVyDvFnuTjz5Xgu8wrOr1vojR4Y3bht9JaphWDhZfl7Uo4V9Esm5t2f3Z_9myWhyGVoNZODeMWMHjtNRu4dSXWwMcdNM9pIlmQgf7WahxLEQd29uKIjABN_mkI2COsS3pCxnNf8ZayXqSyz6VldQ9XaGM0CpeP6x3AKoRMoh4gqtMDjvR--KDiVMfCjKA5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=joU7aaUcdQwZZ4wc-zh-3OMdM-QETwPZfeZ6XWFhmUqNi3zNDtl_NGyNDuI-LlfSExK0d47ItKjgmE8FOFHeh8LEa6-Smi_fPsCBCrvzUNZWSqqPz-TdV9oxKKT-YQjkDfkxd1uRc9FnK3zTpkSXq8WKJPDFJdDZ7_H4Tac_UmbEKm83Dva0j5yVO0pvz-goot8lOiGe3VIixfK00sDSIhygvoDMV6C75NHxFgGT7Bn5iXiGl7BRWwhY-nJkTzLBGioTtQGnL9GBycvEns0NGXrldVCz6oybMJdzRu4_zHGyOxRRuNFfmK6q43eUHUftwOBKFPdVMS_FIhI7SNMRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=joU7aaUcdQwZZ4wc-zh-3OMdM-QETwPZfeZ6XWFhmUqNi3zNDtl_NGyNDuI-LlfSExK0d47ItKjgmE8FOFHeh8LEa6-Smi_fPsCBCrvzUNZWSqqPz-TdV9oxKKT-YQjkDfkxd1uRc9FnK3zTpkSXq8WKJPDFJdDZ7_H4Tac_UmbEKm83Dva0j5yVO0pvz-goot8lOiGe3VIixfK00sDSIhygvoDMV6C75NHxFgGT7Bn5iXiGl7BRWwhY-nJkTzLBGioTtQGnL9GBycvEns0NGXrldVCz6oybMJdzRu4_zHGyOxRRuNFfmK6q43eUHUftwOBKFPdVMS_FIhI7SNMRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBlOtX5NI-c1XJdRVHNKDmEF8b8MjiWoxkRSK2WWPf45xPTQClNpMg1CGx3m-36BI-Rnz1C0nPOo_NkMCycb8EAzqLYpCoXK_yW43Hx7FhRRS5THMdlRAdXgX0fKmBJ-qzZ4w7sKQeoLiEyLW9lcfP3qMjNQwF9SeZyeV51PCIQYNRWNoVqFWWD-_wivtePUCMA-awgxcjF2qLh0gLuXNyo6RY99Uh7M8nER0Y3u3psfEaOKBz3-ROWbZd081ZIJqJ1T51ecLkwkHdxAdE3e595nVdRb5m4Yoz5NHCABMqa-fMu0VQjZPfEjNyu3KtZm2IYa05Mx9iAe2UZ7KDRGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=FbY3t88oSaLl4pGI7j1tSwOSEFjqrKdgYlMkpwJVeMIHkkDs-f9AxO-M-7TabJqS6ooXXqBtldZaV4qbUUV86EHffIwWopZ93ZrKiW4ob46rbJJ5j5EXlv_TVgEJsSx-mKK_tAmRUAlIwZlYzQXBU5_5DhXV99ptEZmv-uvXT4SbGkyRM8OP9WusesAIqPWucWmWGDTzfeUaff9_HXTwjYLuizkXuRJgqxnbbdhhWkd9v4eJhTMQqWGd_5ICu1UsKV1YZIVRZvp3pCflL2GquvW5sqWZY1Scee5mcm59czpT2dSKtXGsEXaZNbvldm5m4b2EvCdrmgFCH5i0nlF5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=FbY3t88oSaLl4pGI7j1tSwOSEFjqrKdgYlMkpwJVeMIHkkDs-f9AxO-M-7TabJqS6ooXXqBtldZaV4qbUUV86EHffIwWopZ93ZrKiW4ob46rbJJ5j5EXlv_TVgEJsSx-mKK_tAmRUAlIwZlYzQXBU5_5DhXV99ptEZmv-uvXT4SbGkyRM8OP9WusesAIqPWucWmWGDTzfeUaff9_HXTwjYLuizkXuRJgqxnbbdhhWkd9v4eJhTMQqWGd_5ICu1UsKV1YZIVRZvp3pCflL2GquvW5sqWZY1Scee5mcm59czpT2dSKtXGsEXaZNbvldm5m4b2EvCdrmgFCH5i0nlF5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=c5lMUVjZsKloyLaSoOYMa8AKzx0dYy7_NT8_cBUut080KsuCagxDQFp6bx5vw5OYc6aNRbbM8VZPlED28uWSopESNcVw3gmZbE3UhSvuEOAuIfElMFFqv6yS3KxTwjZFYya9eZaiAeOxaHSNWeLEPpnpmBJmt1oZquyBCRojKSS_NDZ9BTmxc_fBhL8lG3DfUbeQhbpJ9LrS2OZgAYi5Ad-bXUXKL2LgixpHfu4lDUVTqtt7UYEvufj_uFZn8I1DSN8_VmHrL27IdssqHacKwLLG7rYp3OzUVBqr7Esa_KfH2D7vrdNeOdB_7REkBIDnDsSpcC3Mwraxnz_jasVE1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=c5lMUVjZsKloyLaSoOYMa8AKzx0dYy7_NT8_cBUut080KsuCagxDQFp6bx5vw5OYc6aNRbbM8VZPlED28uWSopESNcVw3gmZbE3UhSvuEOAuIfElMFFqv6yS3KxTwjZFYya9eZaiAeOxaHSNWeLEPpnpmBJmt1oZquyBCRojKSS_NDZ9BTmxc_fBhL8lG3DfUbeQhbpJ9LrS2OZgAYi5Ad-bXUXKL2LgixpHfu4lDUVTqtt7UYEvufj_uFZn8I1DSN8_VmHrL27IdssqHacKwLLG7rYp3OzUVBqr7Esa_KfH2D7vrdNeOdB_7REkBIDnDsSpcC3Mwraxnz_jasVE1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0It8VqZH1Hc9BJScjRlzI0jFXRLdbP6ZGAwN-CG4eZleck3IlZ7h-e9QfZ29OUhNqjrIloUvlpcM203HHV7j2qZqc0bTCREkysQ33aB1nOlqm6DzgyxFnKxEAFdVZGKphbp5BKsyGna9tEVvzSgvDOuwyOxbq1nGDcB6pcrWj29Ft1VmqNFgvY6T5TGeGMi02PVybvkbMOEX5P8Ptdo5zlDhzJa3Ei1NxqWiFPUhafBm43t4ame-IjgASDHZEnM5sGmJOywTpMCJsSMHkJMBX_OVi1OnF_QtE1J4FVLDPgiImxjuHCXZJjaMwabg4AWBR3Q0oYvUH6-nKYqr54g4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=JrZa_vwBMF7CSwLNAyNg84gBUx1rzIcfUEihxzPoHY6FjxKwG1oyAPKqkYzLKgMXCe4ETK5n7HmiLsgcDAVEX2tk_lNclKvWHYORUc8zVHY7RqltWm310U_9d7qEAJsxYIQfgYlPpUET_w9g76KTeKECh02DNFVudJF-Lemz1tEfLvEFAPQg28SE8meDVlVsPegXu5VK0Cp5u0m7lW-yHn0pOXn3Q7yxV9W6_7n8MXL30FLRnpcPQzNlknWOJ6Oa9mK0fHXBqN2g4jG-2AmzTfglJuHWbRTJmUjhjSys94Jb2edTIuB64ervZZwbwKuUan5vfnkSjgG8BAx70DQPLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=JrZa_vwBMF7CSwLNAyNg84gBUx1rzIcfUEihxzPoHY6FjxKwG1oyAPKqkYzLKgMXCe4ETK5n7HmiLsgcDAVEX2tk_lNclKvWHYORUc8zVHY7RqltWm310U_9d7qEAJsxYIQfgYlPpUET_w9g76KTeKECh02DNFVudJF-Lemz1tEfLvEFAPQg28SE8meDVlVsPegXu5VK0Cp5u0m7lW-yHn0pOXn3Q7yxV9W6_7n8MXL30FLRnpcPQzNlknWOJ6Oa9mK0fHXBqN2g4jG-2AmzTfglJuHWbRTJmUjhjSys94Jb2edTIuB64ervZZwbwKuUan5vfnkSjgG8BAx70DQPLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-pwyZV1GNrXHeIzNRQIKT3RCqANqaEJixOThMZj_AsWr1lOPsRQ2GDqL9vGQpiGPd0cvrVuAEr6YrNUHlmO4txdP8-BSLzUtVo09_MerSNArwlvA8QJmqb-q-C--UUtrRSrUBjEs1IYGrSEI-DotDPLDSi_c6QRtjufHZSaGmgBsXoRF5_oyQ3MKZQxBKfSL0TO6WKSeMgipbTlDHN1OPZVw4-_2-ynCvwMUee7ZvnMTuDCdXCTGdUoJ8c6cAFE2rL6GVMhYdoUyFraRDauu0eanvOwwF_nEXhFK3X7X4UUiKJMsQha-pIMPU2CsZeyNi4GpFHHmDq5eVdfKKz4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
