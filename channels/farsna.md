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
<img src="https://cdn4.telesco.pe/file/Hvpr_Q44tgiHuR9qmbd4gTcOw-QR_Kp4XkfnFpWhnjLi1nzgIoI58xuIzBZl4gVeWAPYuCVSciwmy6a_KHxQLa_1VKpNyqPdzF4Rg93ONN46p0w7F0vRQtdMYsc87BH6UeXXLfgzTvf386FOcx9zqGWlqXySvKprXJjWU89C0mp5RHxQfImLCLDFGZCJVOEPHlyCOjwkI2X_G5EtvvoGnHSf0p14ud-hBnkK8cajbTYeDNbeyiiYYg0Fsbj2--fjdeZwHmI7dwgLd_JZelhZ_eYVW8zoepXkuXnrbdA_unlFUnX1wXK3CNsYNZx4Wh2vwy58LrYXx3kkIsEEgW4ajA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-466063">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران امروز هم مهمان تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/466063" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466062">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض به قیمت بنزین، سخنرانی ونس را مختل کرد
🔹
«بن براور»، نامزد دموکرات مجلس نمایندگان فلوریدا، در جریان سخنرانی معاون ترامپ، با فریاد به قیمت بالای بنزین، جنگ با ایران و پرونده اپستین اعتراض کرد.
🔹
او با کنایه از ونس و ترامپ تشکر کرد و گفت: «ممنون بابت قیمت‌های بالای بنزین و پروندۀ اپستین.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/466062" target="_blank">📅 17:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466061">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCJR6CuOSBHWImlb1yowILvAHeezQs2-O-jhTUCFeGLhiBPnqKpoxiVISajNbUHe_X4T71cXldVlVUodz6AyB_OVRUgPej2Z2KC_ofonLWg2ORBTxN3ckYEk0h56DY5majF3fr_BBqBpxUVN6WjNOjnk3kL3R9ak6o2yg7lSsOEYoVQwBrYk9KsFkQWvmhySNPD9zQJ7_ShTOSpLTKJYj4spO7LBh2j_D7QBhwQSQBllzsB7Nb5MZ9JMuW6n9PK1_oIuRkYUofIOfjYFDA6XwqeUfAqquhZdEKMjLh_SSRAwijtq10wO4E_WhoaqhueMJrGfTACZHN_mCKMQrBF2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبگان سر قرار همیشگی حاضر شدند
دکتر افشین معاون علمی رئیس جمهور و جمعی از نخبگان کشور که هر سال در دیداری حضوری با رهبر انقلاب، پای صحبت‌ها و رهنمودهای ایشان درباره آینده علمی و پیشرفت ایران می‌نشستند، امسال در مشهد، ضمن زیارت مرقد مطهر امام رضا(ع)  در جوار مزار رهبر شهید گرد هم آمدند تا سنت دیدارهای سالانه را در قالب تجدید بیعت با ایشان برگزار کنند.
@Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/466061" target="_blank">📅 17:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466060">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXOuXcDdw77eo8SezzrYZI5ICDD1YWcyYXLaDFdWvfWFu7HCDTSPgkcOwg1v5erflrp1X-qjI1-DeoXTnkdtF0B2xoEPOkiiJQyx0SZIoZgL0401xQmA7Ljbeufmw0_RkPGfka07FdTd_8Be0OiEwEuH5qxo34rxgN_9g_ymWyMa1C00-BhpqmrslJOX7mzSqeoqbmVFee28Wx0gC4V-OyBEka9AicTgGa2ubywDtzCfp-DjUpHqNhXn9V4JDikit_D9MEN9JK-s438Z1aW0aFSSwsn6z7DtT6jdD-5xsqHu78GGaviDSLv9nzBVMoQQ6uxUh8wsIU8yFHwmK2F4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/466060" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466059">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/466059" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466058">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNLiUpJ9IfsYZXQ--XYuAJ6B66aIgk06gCase3eP6Md4_5ngo3tgtGCpMXZMoJVGkqwpADe5fymgG8wiQTFErK8vkx40krPt2vLQer389mZ26fybHW51QiLin5OnJr4cjCQhlqu4qnWFOcOLoUeQXnfoxNoviHkyQYEFS6rABif4yzA4iroCwlCbaHcN-R5ZK7mu5M_H3RvdPd-Pm2kCWg6Kif25OtqRIO1nMKn7pvQDHu0AJhX7q8D-GWXzH7FlkmoeGLTTeeJw0EJ60g7TkLVWajAIoLox8Lr34hwJG4Zu7pRyhyCwQxUpfov3I15Og6ZfHAu222lJ0t8WCCbC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی معاملات شبانهٔ تتر در صرافی‌های دیجیتال
🔹
طبق اعلام صرافی‌های ارز دیجیتال، از چهارشنبه ۸ مهر تا یکشنبه ۱۲ مهر ۱۴۰۵، بازار تتر-تومان هر روز از ساعت ۹ تا ۲۱ فعالیت خواهد داشت.
🔹
همچنین در این مدت، سقف خرید روزانهٔ تتر برای هر کاربر ۲ هزار تتر تعیین شده…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/466058" target="_blank">📅 17:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466057">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/466057" target="_blank">📅 17:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466056">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc2-M2HPT9GJbztM5C6DuTf7twMqhhI1V450V9pt8VjQ6njAoPI4tTW_s6x8l6O6_rWkOTifAZW-3PUxDuXjgoUlj7bC8G6cDaCVKDdedfMHCptjQgzNdPQUNZZ8babuLyPicfOxQkVLPXjn3XzFcGyrctie7FIeU-yAZ-_DxzIE1B655yT9Qj9CxFJZnU2_YfRsSxNzaA6DaCCMfNp6TcCBmmXUwS382zdsyhRs3dQR28HL2gZVq60lHBy1uL2Qk9yzcmhHH1Nwu6LSsxd5PzUIT7U4saq-Dh3N8UjnNDoZB-UMIA3TBkcfURsYNsd7Q2qs0Rg2lG3Oo6QIP72NAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/466056" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466055">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXGCpY8aNzMarHYYloMbofqfkLnF65-IrJX9kxMUJLxY75h1kjzik_tenmoeSWOm6SSCaOREM8Wa1esD8gbcKt7gWLUGwPPd_epbGvDm9X5APXrm7_belbIs7RchpygRfpTm4lQtstRYVNPi-4qujhkvCoHROWpkcYkiYTCAOXY1vcwvzMwbmmmWfLkTc5PuHEz2Ra0l0c21nG4aJTIjNnWlb8l_dyy3GpBIwCR5R9RN9co47l9CHExBvnpWGQ_HdbPXlbgNY09Us-SzCsQF5GfrbdGLtUdwk2NtBQREbwCGEJxfn8CTZ0hFnaCLJ9qK9baljtyD4bo6wKqOomVjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: عربستان در ۲ ساعت گذشته بیش از ۱۰ حملهٔ هوایی به پایتخت یمن انجام داده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/466055" target="_blank">📅 16:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466054">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQwfqaqOsyW1DMSoL9ajZRuYZZ0p8Zofp-TdH0bRh1HKIiA5siMxQq8dcCWhwO--N_3WyVYGD4DkztZkuYZGhc2CaRoRE409v1FmOLpnc1owrb4onfSRAEsdjCvi9vPL7-dYma0YdNaxh4FIS7NHCuTWoq7FpoMoiWbmpWRZ8Qtfw61wqBmrq_1yJ-sEQ8L66-5yEhY-tQNCovYAo3-wD6S-Wv7owv-UR9QJAZ8MoTd4-zdpRGMux__vxA1ydugaognvJpHc8ZV8tXz0wlgxw46BiiyXX1rFywiYllogT-aQqH4IvjcHfPSWtLDlYy495Z9DVkyX-jXzmj1B34QZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۳۰ هزار نیروی پاکستانی در عربستان مستقر شدند
🔹
اسلام‌آباد در بحبوحه تنش‌های بین ریاض و صنعا، ۳۰ تا ۴۰ هزار نیروی نظامی خود را به عربستان اعزام کرده تا به این کشور در دفاع از مرزهای زمینی‌اش در مقابل حملات نیروهای مسلح یمن کمک کند.
🔹
یکی از مقامات پاکستانی در گفتگو با رویترز تأکید کرده که قرار نیست این نیروها در عملیات نظامی در خاک یمن شرکت کنند. به گفته این مقام، نیروهای پاکستانی از سال گذشته به تدریج در چندین نوبت به عربستان فرستاده شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/466054" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466051">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های مادریگراس اسپانیا رودخانه شد
🔹
بارش شدید و بی‌سابقۀ باران در منطقۀ مادریگراس در ۲۵۰ کیلومتری مادرید، خیابان‌ها را به رودخانه‌های خروشان تبدیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/466051" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466050">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمانی آرزویمان این بود که آمریکا به ما موشک ۱۲۰ کیلومتری بدهد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/466050" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466049">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKc3ioZLavwttrsRD15INKyo0GZtEQ7u6ekkUN2Em1KeIzhRkrMTyk-UhAuQ4sooG1IgWqWEUvpoaeMSizy26sY05U4PSd8Yyhuvt_Vvm6rCRRCdHPkAShKIIbDPyefhUADPE6t5yam9y6b5KtbGikdnZ2wBTpn7waAbXBT0ouA1CcTFwbT4rTkAHQ_CA5Hp396cBYgg7aIv5jt_K-MTv04WqfTdNPvghKbh8-yr0oXMi86o9LUz3F1dZfCMgtr_FJ5THfM0FQyFjOKKK9ThZJUMr2YFMCA_9BGMWpXNBpAan7nt3rqg-bMDHXpQKBcLsqKOHN7QDwB0f_-3Dmt-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعم تلخ وابستگی را از عراقی‌ها جویا شوید
🔹
گاهی برای فهمیدن معنای استقلال، لازم نیست سراغ کتاب‌های علوم سیاسی برویم؛ کافی است به کشوری نگاه کنیم که برای برقراری یک خط پروازی، دسترسی به درآمد نفتی خود و حتی انتخاب نخست‌وزیرش، ناچار است ملاحظات قدرتی بیرون از مرزهایش را در نظر بگیرد. عراق امروز یکی از روشن‌ترین نمونه‌های این وضعیت است.
🔹
استقلال برای یک کشور، کلمه‌ای تشریفاتی نیست که تنها در قانون اساسی، سرود ملی و پرچم آن خلاصه شود. استقلال یعنی کشوری بتواند درباره سرنوشت خود تصمیم بگیرد؛ یعنی دولت بتواند در چارچوب منافع ملی خود تصمیم بگیرد، حتی اگر تصمیمش با خواست یک قدرت بزرگ همخوان نباشد.
🔹
درغیراین‌صورت، ممکن است کشوری روی کاغذ مستقل باشد، اما در بزنگاه‌های مهم، اختیارش محدود شود؛ آن هم نه الزاماً با حضور سرباز خارجی در خیابان‌های پایتخت، بلکه با ابزارهایی به‌مراتب پیچیده‌تر؛ تحریم، دلار، نظام بانکی، تجارت، فناوری، امنیت و تهدید به قطع حمایت.
🖼
اما تجربۀ عراق چه درسی دربارۀ معنای واقعی استقلال به ما می‌دهد؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/466049" target="_blank">📅 16:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466048">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQTFKTWyzYT6A_55XER9RQDrh8cNo6qoRZHBa2W4A6hYytUVVYJJIHpkxS_H6e1OB8kVtO9bmXfjQehZJWppqplK4EHoSfbODAJuq5jymuP6Vju7g9UQPQz8vZMWesnHkrJH6A4wV9OwROmMgZPX_EG1uxsXWg17Free-qGECoO0w5RJnjYiwtIxROOZPOysLzrCNK9TFEMaHMQA25CAn0N864I3Dt66-KK0mAtN_4t7v_hj-7oa_8aQ3-JdN6XUzZLp1qhNSrruwnJq-FGW9AP4p5m_Rd882Wj8cckiRSwOx_HEu_dmv_ImWO6Uw3yElLzEQsliUWOhyX8ww0deKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/466048" target="_blank">📅 16:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466047">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/466047" target="_blank">📅 15:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466046">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران با قهرمانی در بازی‌های آسیایی از ژاپن انتقام گرفت
🏐
ایران ۳ - ۱ ژاپن
🇯🇵
۲۶ | ۲۵ | ۲۱ | ۲۴
🇮🇷
۲۸ | ۱۹ | ۲۵ | ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/466046" target="_blank">📅 15:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466045">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466045" target="_blank">📅 15:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466044">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آذرپیرا با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/466044" target="_blank">📅 15:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466043">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvfsoXZcJWJQd1RqBQVpKO1X8k7ctEedW3zA_IF21i9f7sCvZWt_m6FmjM2md8LrwWHBfJIRkB6v3rfyFNtw9CpcKF4_bSTtV3j0ebEjYfQkIsbQhsH5OXrLaH0o5Sr2bxKiM3LTHgLZb8sheZRrXBni5FXQx3x9AjB6LJr47dEJwOhfbb_FjqQC7n6WYFNQOS8gdrT7y_sR48aUKTCnUDLrOsQYgiSdz2c6K08jJafHS3RP0aJBBmOYKWKSAqDTLFUc_vAE-rqrlMyqJe8sT2WM4L0rz-qmj_wlbRr-fKLaRkdjKVACyIPOIFE5Hqj8oIYPQjjpD42MY9BDebxA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کهن‌ترین درخت گردوی ایران ثبت ملی شد
🔹
مدیرکل میراث فرهنگی لرستان: کهن‌ترین درخت گردوی کشور با قدمتی حدود هزار سال در منطقه کهمان شهرستان سلسله لرستان، در فهرست میراث طبیعی ملی ثبت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/466043" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REKQGXGwbSjhD5hQdoipXFi5N9Dal2-dqrE5WL2Tu6Yw95K8amW09W2st-6lzimJIjTrpUGQaZraCGqdj1sznZvQZRDRPd3TwClHBU6Iy9VmoC1ui-JhIt1hMzTITLz5dGfZI4-utGzb_A-wsF0y8sS_EZocI2oVEO2SQ7XfeFmfwQ6HVIfHnLcv_JMXmwMECRF3AFsqARfkaMIh9fTJqQAH_MHjEmJlsBh0wX_WgKy_ZkjKW01Q6aE9jqhEuwOQql2R6X7o3XdR_6mgT9mm16nNsz82O5ntuXlwx0n3e8PXCpGtCmO2Eh3A_A1gKrbdRG8HhdWh8MqWZBeEQ_4U4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466042" target="_blank">📅 15:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRMtM_hSp4iFzsiXTg85a1y3uNIZCGGpGMRLhElTKAvVewOg9QZ_iY7LXm7iXM44ErukoZRI8tflYXiJXZ7ax57WaDT9OSNgO82w-GJRVGnE_7xbpWDmY6K4pb6NeucutQv0RiUS4iBo8Lc5DulbSKLhD685FcxtF4nnmMdH7kdmOC0OZKyZyGAeWEDTidHrN4oyMLZihUCHWXedEPWem2uZdYg97zXJQssL3CU5tvaTwmHKIJlBB4478ymelOOfeeleuE2xaMxyEFWjCkS_yl-P5LnmF-A9m1oyv3hMHQfDBcy0-Us5a04J7cIpVxzMBYfJO6ARmd3aTREukxUEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZcxM7pDKy0UX2P4uHbtBvRKj6w9XjfcDjK13knSpdETcfOHUK8AtD3Vpe89t16DjPrbq0AZ7YlEWDBhEXM-AF5BPKs1t2AIJCKlJ6-1Unh2GrUxhA6tHZ766sc91-xPPVAM8RYOQih0dVxcLpHv1WdaJwd7vFzgig0hhuEU72_6zwz4yS02NHTeLyPKED19JmiNFA_Nay_-TF2xxlnoJtNPxENR0hRr4sy9kol-mDheIdc_7h27bjjnGPleCHrCq9Y5sJH-OjPk2rOfuKse_8fV8N-AIyk9IXH7VW8padC3jZ86Bp4U0gA4THc2Aic-QsVVXIeBRq8h86MPRQsduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiZkcb__ZHsCDO8uUNT-AW30Z6ryds-ssf8V_GL4zlRDGfGp6Mk0lXtCJ03VieWS3d7uOymJhFRfziEtyG4m1Er9SJZmHxv9hJyANnYsR7jzsWcREeBVp3Hgg-_Cyd1xYfj5QX18NhBBIus6SGbakuuzKEi6OaNPuM_wq91EuSEHzsA2NzByEhkLOJSBudBkRlF17SFZHAByqy4k_WZ700-VQdYiTkOVGCWCJB0bwFUzcFmvkol6aoO1OG5q27GoRnFlhX6ZtW2HriHhTByHofRPpN8A8jKv6UBpN1OyaeTuxwZ1Enbl0SVlh8f9w6QhKoZbSOfiwa78BkRu-tEu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4PeYp_n2HCavGA4G2OrdQyVA2763G5A_gdJ6TwEv4siueTDoYyQMj6jXMH_4upvR3PNj_WWNRoJBMyMbtrtjRLRGHjEtX5ydoFJllVil5KtGnVLxhhKup_p_Ac5EZLO62esclwBLNwql2XZlkzZBsYAV8cRIEnT4b7eUEzuwK20-H13bFPB-JiFHl1D2MYxYJmSSM3o87Z1V0MGILbu1w4LOlQPgWWjg_qtrFRMlJFPxuWWe1Zy46aJk-AexSwZnWCEHYa1TAhCOaiMLWXmUTJbjjntz_hQGHqsAcrs7CMvfFZRVWIGkVnCiqH2QTR4QYFskT9pD-heyMQEoJBOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5SVBO-fmu0DvXv1_0VI6PmNeFiwBBflZaQ6D14stBHpLbNbJEblPvPqVU_ZvBk6vTAYuoj6DXWxX2EsSPHPzCOnkENaUCR8mfz34akdv2ZXt6ia6zIGdnDlHhnpHMA1zYDPt4ibfmwMvKBmBWlwQtGKYsW_DATVp9zKsHUhMOMfiDbyJTqU0DyWHtkdoT-jVbgceztrN82eEOjebSbpq5RI6vJwyRr0Ame-ETpCTEiPlLvcq6bccis4ndRVIq82q4aC_pA5GsDuVdUP_3-dNVOk8id6FoOJRCEsYoA6D-b80VCi0wx_h8QWI9HZlmaLtyApWaugFEZzzUmvKwhraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pA3bLomA_0S0K9fRdotlhJ3q-ammiREbuOUJotytuBSS8RRyhW0NjglD5KT19miOVYiVc77sqySx9NshsSU3RjeZICU9LKw7CW_thC1pLYZkbBPVWW8tjlS3VMM2J72LpHCeoad54zf-UgjtxDhWgm9SttXi6zu5RPiLmW7vCyY5SHhjPSN8l5hR0exXmltuqXWN25aPgt4LYbgmgNeZvQLfmewhATehF7CjU_SYuQajxuX4mNmcrhmIRqroxBotBW8kGpVGzqcBBAEdiPtx8VzsEmFyQQDnZSl4ujgkFNRMM3N6h_JhFID_KFCkLE1F4pwyZ2WGT7ghHlW5venKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8CRxBlvn32TQEJqgl8sXcDIOlxnb3biH6owAZaxzBzhHUI4LxhY5gk8JpF31dqL1ketKQ_owDuY44iM_YDl9zwfJb6JrD6f_RKr3srROLbV1GIwvcgzhkkJn0f6TaL3KxLkLfGLOVkI3aCgpdh-hWJRMeTU89MOAc8J1chEzqDJpKAMqhcIkin6d5D5vuX8_zNaxG-EWlHCcc2EbkhP28OzEaVaB0_7PSCJsW9i8tCT3WahlgPhKgObl7C6Prh33mdCElZDf3bVZm9_qt-5t__G9nZDBiXcbFWmVwmRHzB4knsv36FHtiAyiHqdRIV0Bf5NxGfzZZA8XgS1L9Msww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای حرم مطهر رضوی و رواق دارالذکر؛ مزار نورانی «آقای شهید ایران».
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/466035" target="_blank">📅 15:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🥇
اهدای مدال طلای یونس امامی و بالا رفتن پرچم ایران
@Sportfars</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/466034" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466033">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌آذرپیرا طلایی شد
🔹
امیرعلی آذرپیرا در فینال مسابقات کشتی بازی‌های آسیایی ۱۰-۰ حریف ازبکستانی‌اش را شکست داد. @Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/466033" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466032">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi8YzB2l7wJZFIEDs9NEeSxyLp1qOIOq_brU_pD2nv34V-uEHThoZSwC8_H00UaApfCs7yyePckRqCBB6y-bK2ATS6g_SQb6f4MBtD_flqa0UdpYB_gV7WfYAgkfKwO471Hada2BE3fhQklidNTDSS-5IL5_mUh4QRksUV5pAQQDUbJ_JGVtgnG-zpcf5zIQbxi_i68Px0fjXCxhA5_VtmLnvU0HFEamuFkM5nxhEiwz0bhhQ1Zb-cYasYBYg4NDsAd70pScIMpHdDP9COLoyKOkI1q98ExpQ9RKmCT7gzzWh2FMhF09iXwH1VgCIWJm7r7bShj0yuSTE8zWMz-dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/466032" target="_blank">📅 14:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466031">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌ آذرپیرا به فینال رسید
🔹
در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی آزاد، امیرعلی آذرپیرا ۴ بر ۳ آرش یوشیدای ژاپنی را برد و به فینال رسید.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/466031" target="_blank">📅 14:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آرین سلیمی با پرچم ایران پس‌از کسب طلای بازی‌های آسیایی
🔹
آرین سلیمی در دیدار نهایی تکواندوی بازی‌های آسیایی با برتری مقابل حریف ازبکستانی خود شانزدهمین مدال طلای کاروان ایران را به‌دست آورد. سلیمی در راند اول ۲۶ بر ۴ و در راند دوم ۲۰ بر ۸ به…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/466030" target="_blank">📅 14:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCsjAWSRdtqaVtnuL4d7ErQoLGpbOWEycGcnUhY5Wb4QwgJOzHyWBM8Tt3GWl8dzQnzzA42ucZSDmtQp48URsECxpRS0a554F9EtTQRvD3UYH-6ZlOzAezLnApo5bke8OnpxMKRMrGTa_ve__t7doDXcnUPLitn4ccldF7GFZ-quGGjNQlQs9da0ncTuxtqZH_TBksXW_UVb7ViMGoafbKSh5mclmVPKxRZxQarctbcDScjilBzd-jjM8BI_GZ9lwwCUTM4rTbGPJf9MSYo4hirBCKbQCRncstc38O6BD7plsUX3yncjrjqxdY8r4u1sFZ6jp5wQphObflBqvn68eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/466029" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5mUc2vKc7Vf9NplBjuYWq30i9M4AvvwPeujy5LhE-5_GJOZiISAQOl1FMmQ_vGcTaA-aMJzMmZNjsgmdNRdqPuNM47l5xUx-yicDuv7PlZt2x5ji_4WjzS8etFBaF5NqNSdUllxEhKLA2bxLYl05P-gXDrQwb53NW8MFYskxfo3r4VMmuUmLjwVfGbsGK_PM6uZtYevE1LOjOIFzcFRIWdKAvQuu7QVRh9vLVOKPAlkFultmI_ReqsqOPDWaYUD8Hvnhm_PafMB-gKqdwB37Sc90SyOmfsRyPeUjBDhyW-czm9zWB3n2DkEmTtk83TJ97EEy1y-_kg4eNJVqR8jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ml-1HIbP8VHtCJZ5Jjp2txe4sDBl4J0Y_gm5BJocFCxfue-EVp9ShCD475Zxfdm7H6CXQHDR6-cvfKMk_nv39IfeHMsjrj7ht9uFqEYckNsoYDbduxFDNBX4dXAQnsE_l0dYVs_oWNa04via0cKQR3bh9XNeYZmREB2z-cGk6uQN9EULmTcGYTsHUGQLg1FhmTooAzQ97gwr2FgRdIMoqoE8qILOMxDuDXikH6qHCRsw2IQi6Q4O-UMoU8vldGDvb5CL7Ko4ufb3-hOQJ31GNzE4A0lFGsfpaJcgsqxKdAShMJDynTOuDcjc3gHIJJ1W3s8MrcbEahZc448R8L-14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlaixRhP3uGBrBgcKymfUhRZMssc1NEoTixrfZzcvdqgBckcOcJAG5Ee5XxnQutNpCrvh1f4WbAt4RPxq4rG3GiN3G0UhnZQGITA-CRzZJjmhNb4fMszWQLlcnx_PFRPgH9VKIt7N8sLMjU7ooP4gDOyQem_znrbtlk6OTJl_YDjT02xi7ce4wOaPonpAj8oUtSnWNpGdiPDwxr2ZuZo3mmMoTUDAft9H9OslVIoIfNrklyzExdI2Zu8m3GoVdAhMKkno0D5b3k1cheuRDwodwGdfp3W7-BCAgOBLkU204M988MNM4A618MWPz-y5okhNjmreipPrI6t6UkxokNsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZBcdlIy0zx217Ku_Z0C4-ow2oA-mtpSCdUyVGmIvhFgcChtvTbsHmfOXZnbYoFi6z4cYr9eUhB0WwhjaoPn1NO51DBiZdP3ijRlBBdkU3fRgRZx4diq5aAhP7W87ga1ewfhQyVJUuVxzpqGsITKy4WhPOX_wP1rQmN8zuuOrJMlRk6nEuCR83YGzjqe4QXkDJ1GMigPkRZTGYxVO8DDSa6mcucn9JvwiXHsQ9UBCTnbdb1XUxgYf1DgRsWpb6TK70InxAug02Kxm2wu5_uBFSZbFsn6vbSeifG-Paqs3yxIJageEPCk4AvTRIpWeHht1oIUZ17wAXmJ2GHOJkUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btBHvWd9Zb2C3WTlXRuZsM5loWbY6AkywLQhPxu_KSVhg3db8uL-z-StvuGsXeb4u4018U_TfbeVXjDjkIea4fAQuM7rNjlr8F63Z89lBWekOVwNBgtDNOFpuMDBKJ7fyQX3Lf5woCsH26UFMmfLTG2StIk23vaZmQtWdpsWh0hugupxCmp0k1AQnGsnHqPl0l9uEtTPGrHKbvE6QLV_xIXhFSWN4EHsaDEUQPcHqiigFGAsGNL96F6bsliiENzS_NctT3zdo4UUkIyPisjd8dMuEgug8vy1ixVjIFhwQOSUCOYQs0v1YENajqqg8xQ8izf38gAkGuOk_vtISFDhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PezgJfH0DRDDO5_3UNNfmIZAeJRn-CQprzMxNhG1u9xxVX3xZh3HyelTPQIccoysBLDt761Ts2EACxuM51JY_0SfaGaeVs5u8eE6Z_AjwSd9OA8fBXeznJAMzS0Bx6XT6H07BLZuZCIdI0v_wSjQY7dKX8DfGeMPjegdFl6WiUzomRVg4-WvpH9xbeGGcjPk3XVoiONQfj0oBiaXlN1S3ammxPGyBfCtcwNRGbf_qneYAFiX8inZuDjz8e3zaZtkat7oF1A_oeSiCgPojGuXdYfCsKNSIxXD9cpP2aX8kEJezyrvUcFLj5DXX5oyGjU0cpukvM84yifnda2sW0Y4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpsZLDoOCwuHQWxI8SwHHZX1-kRQroWik9UteFPPrLMRI7FDvocHm9TBUVsBepLSelBUlNx_alJc-5nAueuxv5GCivwd8XJ8n7E6hLq_prYXJ948uIhzFi1u-_XD9C9EORLYhvik__LD1Dc-L9gYPZhZvAYQdEJPtP0-SrIecRTALEluO0Pp7QAE_HimwLFLZ3ey4dGKzpbQIn9GOs3hB7mM2m4H1HnAwq522IR8QZHhOkLVdy_RtGtUFRN21Nkv5x1bemqg9Tlbh-KRkQiHm3HodmECofPAc8vkRvrNuu5VGzjv0UDG3Y346yIBe2Xn7uR41hpjm2BTQhb_voYwMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گردو از باغ‌های خرم‌آباد
عکاس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/466022" target="_blank">📅 14:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10e00e80b.mp4?token=svaAnWGyiejOQy8NcNjuiiU0wTcsGcskzcNe11eNydyQUcO81B06vfsJUYFpiP9J6f6IYxd6TryTyp3oB_0ah0w_RF3jak98u_m6EhbXqRHzWiJrRAYnP_bwN7xXCCYl2sWLz91bT00DCdyU-ahyw2YLdGPFn-OMDyJt03AcKEixRVgn5y5jdmGqnDzhLaIG1pvJhzBpiBU1EgqwqkoY5A__-9TkCtqJuiKRrKmreQhJe7z17Hyc0713iL5xF52WhfKchVmU-Y0YN1JICZwrP9XLrDdgPQFeWqE4EQmgQVFCAKSw1SD3vsJiqb9rpVER811kad7rc-0MnSHwrvMQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10e00e80b.mp4?token=svaAnWGyiejOQy8NcNjuiiU0wTcsGcskzcNe11eNydyQUcO81B06vfsJUYFpiP9J6f6IYxd6TryTyp3oB_0ah0w_RF3jak98u_m6EhbXqRHzWiJrRAYnP_bwN7xXCCYl2sWLz91bT00DCdyU-ahyw2YLdGPFn-OMDyJt03AcKEixRVgn5y5jdmGqnDzhLaIG1pvJhzBpiBU1EgqwqkoY5A__-9TkCtqJuiKRrKmreQhJe7z17Hyc0713iL5xF52WhfKchVmU-Y0YN1JICZwrP9XLrDdgPQFeWqE4EQmgQVFCAKSw1SD3vsJiqb9rpVER811kad7rc-0MnSHwrvMQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امامی به فینال رسید
🔹
یونس امامی در مرحلهٔ نیمه‌نهایی وزن ۷۴ کیلوگرم کشتی آزاد، ۳ بر ۲ حریف قزاقستانی را برد و به فینال رسید  @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/466021" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0309f01f6f.mp4?token=qvyhIOgbnIUXuVn4EaaR63snvgvj6_S2K5LeVkgdrrvmNc9Zo3Y0VmK-0sIp-cxfZPi2Lh9qEXRF2NKFmSslgIe91FsmiWo0FwHVXSWqnIEx8ZHSsbR_C-DAxc1wAzFNc49L9BpAIasOFy-OoS157x98Mk9fsHEr71TZFVFUZmh09cvlf5um7WIMUjh-UIW8GBXLDW9QBPR9DVcWKHRxhhhIquD7onQ6PEUixvBpjMJrfSOggDzKW5Sjo7-XF3weqrcv41sG3pGP1zgyPX6ANdo33EuePFll3BpefgJnBCfCNBAV-xSOP2VQYldbKBNfzaGTc8ZqO8LL5eACXJT1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0309f01f6f.mp4?token=qvyhIOgbnIUXuVn4EaaR63snvgvj6_S2K5LeVkgdrrvmNc9Zo3Y0VmK-0sIp-cxfZPi2Lh9qEXRF2NKFmSslgIe91FsmiWo0FwHVXSWqnIEx8ZHSsbR_C-DAxc1wAzFNc49L9BpAIasOFy-OoS157x98Mk9fsHEr71TZFVFUZmh09cvlf5um7WIMUjh-UIW8GBXLDW9QBPR9DVcWKHRxhhhIquD7onQ6PEUixvBpjMJrfSOggDzKW5Sjo7-XF3weqrcv41sG3pGP1zgyPX6ANdo33EuePFll3BpefgJnBCfCNBAV-xSOP2VQYldbKBNfzaGTc8ZqO8LL5eACXJT1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در جنگ ۴۰ روزه، نیروی زمینی ارتش فرصت تجاوز زمینی را از آمریکا گرفت
🔹
نیروهای زبده و تیپ‌های نیروی زمینی با استقرار در مرزها اجازه ندادند آمریکا جرئت تجاوز زمینی پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466020" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD7z-52uWf5sY3yI6lw6kBYR6Q7v3FHwxSNX3sIEImw5C-eb75COrC221Egb7_iaTToeiQVItELPl8vMdOjAthrcB1oNL-rT8_C38reKkevnWc-XM8yiUjW_TpzaW9PGlCEaX4ZQLJq92UzDr7svjPf7M-Y-tbeOHyLMU78m5FYR_-a6vhIPtTsE6YSeli4V1vStgiCZzNPdzVUEumxuAnROhn_hGsaM9Bp-BH7jV-zuOgmXfsrwiq7NSELWCCFeW7_fQPHR-8n9N50z1LO2evxkUYG1__tFsLSj3BQC3aYUEKUIhbj-vfXDMZe8lsbqFvl1FT6CR7YHnEXJ8SSvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBJlmdgalrOOr-dBijOpeY2poUywGJ8x_pFVe-o9qAhAA9QR55vS_iTquOhAS0K66kTqNtmYoxVw1knz-DL_riQuVnkAp_KUbhKRohtNiWSDSMjhZT0F4wMqI2ssmOFMQUYy7k5zcvthPsqftCY28TVTjlvENy4swmZ7Wauj4T8ov0a67AMij0sOiUQKgfnPcv-ifp9gbsdBU9n2PFE6Y57vKwv4G7AvzbIrVsQhEdIrYdvtze9uF1GJ1hLDr9QcVXyXTIao8jsglrLYH69VDD1AWEBduSCGclTSI91jsSi7ZaWeuc7zBy2s8_a7XVHeyxBmqmPMW6U-GHP1QAnz6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اشک‌های حاجی‌‌موسایی هنگام دریافت مدال نقره
🔸
مهدی حاجی‌‌موسایی در فینال مسابقات تکواندو به حریف تایلندی‌اش باخت و نقره گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466018" target="_blank">📅 13:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت اطلاعات: ۴ شبکه خرابکاری خیابانی منهدم و ۳۱ عامل مرتبط با دشمن بازداشت شدند
🔹
سربازان گمنام امام زمان(عج) در اداره‌کل اطلاعات استان کرمان ۳۱ عضو ۴ شبکه سازمان‌یافته خرابکاری را در سیرجان شناسایی و بازداشت کردند.
🔹
این مزدوران برای حضور در فراخوان‌های سراسری سازماندهی شده بودند و کوکتل مولوتف و ابزار تخریب دوربین‌های شهری تهیه کرده بودند.
🔹
اعضای این شبکه‌ها در دی‌ماه ۱۴۰۴ نیز به گفته وزارت اطلاعات، در آتش‌زدن فرمانداری، تخریب بانک‌ها و ادارات، تخریب اموال عمومی و خصوصی و حمله به مقر پلیس با هدف دستیابی به سلاح نقش داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466017" target="_blank">📅 13:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhZwfkeH4kRG2BBsfmLQCr07yLLH3fYJu3j88KPZ5DRgCksBh4hCbrdPR8OXkfgSR74yCjHRYGzKWsOHOLYeNfk36BV3rf70syqm4z0mZsFoogu-U6qdndAgz3WIDmpHCgO9re1OK3Aw8qlwGaJLzjTyjkviVxHgMNpOyWvLjJjWdjLAN-w8J2lI_Rmv1nRXRMEN18xqMmXFIwHJhcNHJn52baygzbms0DM2EEt0qZCEHOEy_jY5RU-FzeykLq8UB572aA2Xm_WJRuhuy_gPScSctc1zaCzWoglHU1cdkfZ_s_DRkZHpOmTd0ZvWkf4ghF_BspzOSTHLvO_V4pjBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز هفتهٔ بورس با عبور از رکورد ۷.۹ میلیون
🔹
شاخص کل بورس که امروز رکورد تاریخی ۷ میلیون و ۹۰۸ هزار واحد را ثبت کرد، در پایان معاملات به ۷ میلیون و ۷۸۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466016" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466015" target="_blank">📅 12:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466014">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f96ccd1a9.mp4?token=lHbYSOCvxfP2SgfSs5nTUkOHyphNZYvtj1lWw5RJvqtJ0_rEX-yjUDuuXQweyjt4cqsvapB_2TitiKrWHcLuSCF7Mfab0_TzoxY5Is7-NqNX8I3dt_WURgHa-l3hHQpzXecXu9LXZg1AFoLQ9nJgdo7_kwkUS8cRG5AJ38dN-tOAwGnrjqxEIe2e5ot1NIzI-lP19UBdOPS16j19tye2aEp8TWe9ltG5QmS8i6pfDv5l6M7uA-gD-FEBoWq0dfQ2NPtrbSoGr2VwL0l-WhSNK6exBhiITnlew4bF7gQyWIJIZ4zA9d9aCRtStZSS0up1NFCib73HoQN4Tm4KJuGIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز آرین سلیمی قطعی شد
🔹
آرین سلیمی در مرحلهٔ یک‌چهارم نهایی وزن ۸۰+ کیلوگرم تکواندو بازی‌ای آسیایی ناگویا، با «هائو تانگ» از چین مبارزه کرد و دو راند پیاپی به برتری دست یافت تا ضمن صعود به نیمه نهایی، مدال برنز خود را قطعی کند.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466014" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izi3Poz--GNGTxJhC0mDe7uEc45b2YWJdbHBQ0WtjqvW5-nxjWSnvINujIeyyWzKoNChLuYKr5KLa-uv-Y_y64QbB_iGQZJYErY1dj0cgQKoZs13VUTGKHKk_t200WCGqEOKgezKJSDu1z4ZnKmS_Zc6inc0LrDAJdFtZB8Rv2s36aWccOqzphqdMwRqJ24JjXzGKS0q4fieYDA87tWske3Kc-_bs0oYZYjlEo7qvTEwbU7R7OZ3zXHO-GvrgO9-TBbXs-z5EARJ0v0z24hgZUvHWqMBPaoaJDJOkwc4jVMTyfLdJTjowlsgGpIFeO5mo__jur-2LcEnH_jJPU-thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: فراجا نماد پلیس مقتدر، هوشمند و حرفه‌ای است
🔹
فرمانده کل سپاه در پیامی به سردار رادان نوشت: «فراجا امروز نماد پلیس مقتدر، هوشمند، حرفه‌ای و متکی به پشتوانه مردمی است.
🔹
فراجا با تکیه بر نیروی انسانی مؤمن و انقلابی، توانسته است پایدارسازی امنیت و آرامش اجتماعی را در هم‌افزایی با سایر نیروهای مسلح و نهادهای امنیتی در سراسر کشور تحکیم بخشد.»
🔹
سرلشکر وحیدی همچنین با گرامیداشت یاد شهدای فراجا، از نقش آنان در دفاع از امنیت و مقابله با اشرار، قاچاقچیان، مفسدان اقتصادی و مخلان نظم و امنیت تجلیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466013" target="_blank">📅 12:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تیراندازی در مقابل دادگستری مهاباد
🔹
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد در آذربایجان‌غربی تیراندازی توسط فردی مسلح انجام شد.
🔹
پیگیری‌های اولیه خبرنگار فارس از وقوع تیراندازی در جریان یک درگیری خانوادگی حکایت دارد.
📝
هنوز اطلاعاتی درباره شمار مصدومان احتمالی این تیراندازی در دست نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466012" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تشکیل پروندهٔ قضایی برای فوت ۴ نوزاد در بیمارستان میبد یزد
🔹
دادستان میبد: برای فوت ۴ نوزاد در بیمارستان میبد پرونده تشکیل شد. احتمالاتی چون قصور پزشکی، قطعی برق و مشکلات زیرساختی درحال بررسی است و نوزادان برای تشخیص علت فوت به پزشکی قانونی ارجاع شده‌اند.
🔹
تاکنون علت قطعی فوت مشخص نشده و در صورت احراز قصور یا تخلف، با عوامل متخلف طبق قانون برخورد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466011" target="_blank">📅 12:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki6b4EmtwBacD1sdzIz5vIggtyVcFNsfkBBdBn_vVoEQlVtrm4dnfatEo28CH1R37aRI85WcOPi2WTBF5MA4lvwxtE9Tx3uUGDsZPcpw0K2aeMEic6KHF16tv_0Abl8_H_NcWeYEG8nHtnFZWY0n4ifg2vXiPHowI2jq4dKL8RcNEy2gaJ4IRnUHhjpDAQ6C_4XTOQLxU68VAgqt3qqFwgUx4tojjefGfNTG7DAvWuChlddbakpkup9UChiOIJn_Du_130xoFiA0xqDyHLHlFIGvQPYozXvhuPTkU4Q3Pm7i4FFZqNMxLVTL8u76x9ZRQPh5YmoyHIeUjlZAV8CaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZu_MPjmaj-mh0r5txVaDOSCOT5YFI7rgWgiLhwra4awJHCG8rgOfyRtpml5yO62LNU2hkBGvht7kGRDrLWszsatHkUGFpjjyIULsKHsAnWHknkf2YHwnaUqUGY_rOdjeS3cR-TnonyhOLoKWOUYMs-3JAfZYjeEjDTXL7pRSTHzJ4n9BDAUkoaBvPnxdbnLlDwiY0uZJi3Kl23wqCPITitkTliyxpUYDBh4aEAPBNiWAnQa0pEz-UysH_cLnjJxuRH2OAnNs33vrH9WK9OEb1WZX_oWnJzkg3BOFM67QHKkRDnsnRqG_mA-GFCU-SUmJgdWagvXr-VKkR6cwL7vKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اختلال در فرود پهپاد جاسوسی آمریکا
🔹
یک فروند پهپاد شناسایی MQ-4C Triton نیروی دریایی آمریکا پس‌از آنچه به‌نظر می‌رسد «فرود ناموفق» و عبور از انتهای باند بوده، در حاشیهٔ رودخانه در نزدیکی ایستگاه دریایی «می‌پورت» در ایالت فلوریدا متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/466009" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4cF7P6jC-QyUSgpgs_qt1WaiBG41L0LaSFPbVGzTYX6uBL-C4nb_zfHWCMxRkfaOsFxnZP6HcRWJJAPAL3T4J8o2wXjVOSE3KdmBisFzZyGTBn-sULGdsY6Iz_4OdFTpCD2PJWFoGaBEvrB5XdX8z-Vp-KoNPTTSJIPJq_QRFDT6Vfb9mjGQCCAbkRi3S48MjyKd8OYN_XTx0B0fwn8tpsoqnIrcEKy_2YnXNPojgvh7-s5hR5wSOyET5EPde02odP2dcRTAfA5ryNtC-SwOT0V5c0uGeyXEI5lgf4P0-nqHdigKgDCXehS-UT-m8I63hvfD9j17uFVooJMU5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس مهرماه سال ۱۴۰۵ تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا ۱۳ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/466008" target="_blank">📅 11:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d0da5230.mp4?token=gKpzMBoToGQcngRUkJX5-WruPiINGfIlOSW1umTR3gOzCpFxE2Eqy2SkAV9YevLI0BdYIgiAQ4ejEj2uL2aV7GLMhMg7ImBc8ciWIyj8uwxJpsbbpzYLsFGCxL-6UJXJz_MCoyw_CJW_R9A73sawfC0hLD1XCR41MvanwfqOVud8XKFZjq2Nsvr2f0cmCzUleQC3zIZRL1XZurRu5Q-F_h3TEhHHo8jaj34VY5f6zpINdh_KFtZzcGhc9uZBVr3-cnJ3gthb8URGo1n_D6v7a9bNE8Au2Noiaw5QQL0MBieiAAjR8YQOml2cwMVS6KTFPdoNGf-efShs77GNN6_C-Z8qZV8tKvEwC8EO8iO5hCfNMiMc0eQDo3iqm6Xk0XUgCP3yV1JHxLi1eKZVFEKdTljPq2h_65zgcHRKKXNjWCbCIYL_wz8jmouqhHS3WYAepg5o7G4HtCDqEv_lTTdXtIAmD2sssvOqmjN1LKu5cPDkiJbkkeFMBb8yOHk-hKOMf-3j6hFkOiXFLWugA8mJvZnvNIIfiV0rFPhWaik-1AkweHpMiNrSjKIU-qzuEzanHDXVJdkDKEOnBlDozCJjqgrXCgqQ_Nx1jlj8XPRNEVibUmT4NiUPd8JLuUpcHBNwW6ruuQX4tJauF4pE51OvrJi3mWVgC3VjVEgKCrVb5MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی نقره‌ گرفت
🔹
مهدی حاجی‌موسایی در دیدار نهایی تکواندوی بازی‌های آسیایی مقابل حریف تایلندی شکست خورد و به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/466007" target="_blank">📅 11:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTaOcPF6-D81vvL3pRYbmE9IK-elrhFKmcBnxwcfgKL8UR4txWSwLvbvBVyqLD9lrX8k9CF-9JfpeYKUzp44zgktb22RGMg6sMQqJiFYFH_dGevrF6c3alvRc8R2bUDvbcfwK7eUBPVfrSsdWIL8JglGFZCZMtSN3hSzr3RsRZCSwU3TjnGU1N7fFjUQ3VN0wRQ8Od1MUS93TZh5sc_RPsp8bnH-t7ByrZOvDGNdXEe4O1MJacqIXmwa0waHaeLfxrY5x0VaRTF1FGQzGVjUQL2hl9an7SzL8uC_4Cb88SEIWtSYIqiLgU8k1uR9prMYs9b-PIPUmc_yTItD0vJi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی‌ وزارت کشور برای برگزاری انتخابات تمام‌الکترونیک شوراها
🔹
وزیر کشور: با وجود شرایط جنگی و فشارهای اقتصادی، تجهیزات کامل و کافی برای برگزاری انتخابات تمام‌الکترونیک آماده شده است.
🔹
تمام تجهیزات، دستگاه‌ها و تعرفه‌ها در سراسر کشور توزیع شده و آمادۀ…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/466006" target="_blank">📅 11:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBCp0YtFz4dhm0gwDwOkiWPHEOU1DGuDQRIb_EdHMi7J6OJp1sNLEwyn5CXjcj797UGVQ38_8FCTnLRTRYL7zLO5O0Zazv-FtNgyxNEb4twB0-mOfPxwNn7NLtZdlFtWMrlKrVV585q8_7LZ8DH0D1rJdC4qPLL1o55htNbaG5M6XMzkWMhX9Xt_Zr6-laXJa3QF-FvGLKyD8SZErRC5TiuQ8Q8AMltYTZBVBRi5ZbJOmemQtF4tODutAG-R-5tE3PZmtPCIx44Q-DM13k1BlDC2cTEaL4Oy6cg8y0fZ_-UIVeIgzMWMVDc_hcBAM6uZgjJQiuKVHLhuFtx0vi5Zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puirWOTuT7rTFglLJqmIJoUVKZ-yB-jTsHtkCwyytCwhftFf9iz2h7r5Pv4dhgan4ak1V7shLcZlztPkj-DAXTuZh7u-Mo4zu80uu0yS-hxe1YBHY7vdCrKn98GHU7BVfEmSGiR6c5IHKs6FZbEfmNwUM4CY325gcW6J4MIG3_aabZkbuf32F02ArLOOdtvD8bf__AjKzsckOab1VFhQ52RssROIR_4U-i8wxTWnNmrK9KNtlH1WcF65GydH1TBmdJaVmhzRj0m1wbXeDnxNeH-r0uf7RbkGa5_MM9glowM5mTSiD40s5qzVgYZEcqVSa4MVfYwAQzaRTiVZ5aiQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHfYbctcbi_UyiDSLfb42PKy4muwNzsBvqtrws2IpThL7E7rJlwuR_7Zum93kMEN51gbcnfDrYCsnB-YCKAbDiy092y3gZRNJZU7m_EOtqg2ZsCR7v6oXxdxCjLkPcBBGC87-NrGjX0Dl_yd96S6IGGE73PJwt4ulYyaGnCWasgp4cSSs4d-lDSC5p6Y7HTSbrA51zkNQwXrLrKOQrEivXMZiLVbpJ3F7NEQiVTOhkZVTpe5t4pvL-OiYtxzp2lZoavVwYFgoS75EYowxmzSEl4uWD5dINGBTxa85YyNzV5PCTJJqoSUlqwCOiNGNeLaDtxixfXuTlpk99mM4-0z2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGuIKFHp7_4wRuF-uscxwIyC0h-rhhOFcd-oge9rrv8kbA2XMyiahNR_h2ehzI2if6_YxVisSGmdBIhuwgpFZpavgRCxY0kad7b5Cr5E-81ixOkO7Za8Ia7LyrfwqteK9mmE1cRBrBAuRqyQNe8EUFaH0gYCc6QSqeP_t8UgkqdSEePkhMdpwfZrQlzIRq_Lwd408SnaGnmygIXMmm9Pn9YsXBN7vAt3kpITuPBbbwVdUNLk-XGDTtaOxZ2u7kFoo66B5AWMK20YzrjUjpJW-TAtRtNBT7KXQnOQPdiD7kdxIU5eKQ9jg_aYJhiICKgH9t2QdJeAZuZsnIx747KReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuolJ9OMhW8O0HYaq1X_CEAubA2iqXYP6cdLogMB4lm6EzkOb00JOYbWs43fKKm1Aw74p6pGrL25KVesrLimgSXn0a1XcjW5BN-DuadQozdUIJMdde56dxjG2Z6s698trfRvJ1jQh-G30tl7zPG-7e-E1EckBM4RLRSFDtPwWJfkaCjmUXe9-CnMoPDCVqjYK7MIBGBy4p6UaS-W_gtSs3GLchmVZBJibleOad08OniYtuXGjqJyNwma62-TNa1f5nJn1vDr_U76dvHlu0FLA6_GxSh49wQ2qcvS2z2P_zx3LzXjHBsQpEucTFTjtSOfTbkJpgBv4HSK-68Z2-yevQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزهای برداشت پسته در پروین‌آباد مرکزی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/466001" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2BOf3J_z5PozYWkrHKwUBmPaytcpRxvLKCqa5RssrhOYRz7wWUfW2EvtjCWI3G2-WO3yfr0yZ_4Q9bUZxuW9RQmRpOFzrLa_CQDYAAWn3b9k9-CzAsNGB4XLAWm3UVSfuauCPTf5N_VYNYB2mUuB5LJ7XKHeq5Mfiao55CvVg_QaDlFEn8NskPqWIVG95GG_sSSLawCooRZMuAjFEh7KDjODeCW4cDYT_ORlkWabXUTYrJiCo5YAVACapSFhKHmVAPuiXUKXpRo3-wJ9ND4Mg1dmWUstJe_DQ53vAS5yIWvClrgq_6xLjSiYP9dOMHGNty9kfYZc7Y11x30i2aK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان، میانجی بی‌طرف یا طرف منافع آمریکا؟
🔹
در حالی که پاکستان نقش میانجی را بین ایران و آمریکا برعهده گرفته است، وزیر خارجه این کشور خلاف تفاهم‌نام اسلام آباد، خلاف خط قرمز ایران و هم‌راستا با منافع آمریکا، خواهان عبور نامحدود کشتی‌ها شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/466000" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cfdb285d.mp4?token=Tg6vwd9IJTmvCa5lq7hicddPKv7N0ZJHl8oZC6tr4R99MR7qR1ALnjjA2HYb3tCEtw2VIRh5Nygb9maR90-DSu3xS15YsPTvuY8QMDbQVRr301wT69LBwmAzzaQFaqHyAfjVqagm8GPPFVgRf7fiRhJxRykZPqhNeCBN6SdhuhwJq8HMrziGlkoa7dPiWtHpyoQesmbwRzRJ6ItxzIQbTyHGryhPPzgxfO8My_GuzQaBhsUflm9P88PEvHbwatC5sG69sV1bNFXLOE5ZazJThKhI9IVfBx6e6Ny4tgARK3oE8ktGpWbNsN9wiJo43YmwNuXReqOtdGNuJ_R9ZJfc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بوسه حسین یکتا بر تصویر شهید لبنانی در منطقه نبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/465999" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e49ed69e1.mp4?token=orEZdIT0RWFeeELP_5OreYG_2TRmmWp_p-zYitTZQVcAzzvee0qNBqlSM5SLOZemD_GVzcAn2u-jhcP-Eng8V5Ux3kV7S2y11C7IaBnr4cPYDLGkPBUDdpy7Woz8lrfcC03D9HrYttZkhwvlLkV_f6Bvp4UkBWx3StwH0n0uaCH-Ism1wxc-91PeuHBZj1lhD5c10KHf46ix0CWFI01vpVUuy__kfSGLnmUOCk65Mk1R8EaQjz7fzMj4AlwOJ4551_l2kZUDuFsat-H94UjPPhnx-gNNA-lo4qT50Mh33EcmJvac_kuKKCqL5oWRiec8cjbCMJq7RUYz8YNRchJt8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رتبه‌های برتر کنکور امسال از کدام شهرها بودند  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/465998" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dc49736a.mp4?token=cxyh5zmHk6BB1mzm_NsRmTDmtb8oGH2cDWShykuqbx-qWbISupzDzHK84cA_THFeUqAIh5Kx9zmqwMuzf10RLPxge_NVmPHeU0LpE48hG-gd7f6pg31AblvGlvLOzBFGEQC5NcBHbMqmpK1at7kj7O1Th_vmOMrpnW3gQt9OiS31eGFlYOh-iMxyQXOu-yb2X5KsM_KUwgqrUmqE4SJb6NbNx5NkyoQhVBSeA5phaJyp-YkP2l0qS_-f9PUNISY7fT_izAooPX5_J_4p2rMzUvWa0eZu8twQ1FD2TJibQr0L69DZysCM2k7GXF4VEy9l4yijZoH3tHJOB8Hyi4n6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌های طولانی بنزین در امارات
🔹
درپی افزایش ۱۶ درصدی قیمت بنزین در امارات، خودروها پیش از اعمال گرانی برای سوخت‌گیری در جایگاه‌ها صف کشیدند.
🔹
افزایش قیمت سوخت درپی بسته‌بودن تنگهٔ هرمز، گرانی نفت جهانی و اختلال در عرضه و انتقال انرژی رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/465997" target="_blank">📅 11:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwG_g_j2bfWuG_CrLYhMp4o0d9XQfFvq5w7hdbiQpg1QbHR4Zt9TfCh_he9qRYddVMWBh2q8TwMcOxoFxlCEBiKs1MVOww1w370auNLC7HzLynkxuBbyMaOycW3BCTZSVK1ph4xQul-Mn4ZXTHBsnj3Byrw7155KDDptV2hLU9e2V1Y277GapMHjarFgGpaFfOXLtBeKgnO0S_GYiRi6Fvrc6GrQFFuVcG9Cdbe-Qh8mc4Zx6uyzNp0TXY5q4PFg12_yhuXOMrKNsuqT7xmxwJL73nw0KAmr_Qi-WwkDqtcoxfu0WhsiEvcZvAxBlvJOL2i5Vljz7dkAaN9yrdsUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKK1Ijomhw3VAzOwqaXoymAV-mKz6cL3IqXgi2Js-2BW3Vg_Ppj6CTySkUFR5y8ygUSjCjY6P8sxl4qcSTRMxmGqM6jFH5gLxAm9eNvPioFyN-NE-YU5_guDwabEgpHJzfijl66ktfaWB2K-XuFGnILTszqmuDGxAs7ggpmyb1yaxrc2VTKm_NdcU9KeamK1rAVM9Ybmz9WynANGmG20jjIORjuFtzVJtzISMxuLJnhR0zvhx6lGhjOcotRi_PP0Bo4Qk_qBQabD0DiaChILLeKVgwHRDT0GEMSmqDoBCy2urHyh8GDOVz71-EWt-ELGNMBtaRPAFdgg0H3pcQ-UcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2Ru5-Tlcw97SaElF6KC94NeS3taJFDVHvYReKHXfBIhG6xEg8ij5b8BJXtojqLtJVl9yO7utCwwju30yBXZfzQNrfcmztx0cT1G5CrFTnU4Z50KukSZYxfY2bEgNDL4MvdRVj7SBYPe4whVevJeMRbMyztW8LmE1X7pQqrmzLkecTTJXmIMy7F54Pam9UkY0noRs-JA-DU_7y22Sr6yecUoQhfl0U09acCZ392jQrHSC7c-MEYx5ebMGGiHMzViCk1CInT_7XyHMARvQhjsgxKvlUMuxsCqycXRhwWKtCxgV0j7-m0EpCdfcstd_ANBi9n3dHush4QEvrtdNdCSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTHRtR4xz6nOwdKLMmAS_JqW05IV_HAbZfUgeJM1BhU0hObHYIDTwAkiwfWyC4W2US6GwjCRDXP1Fvbgv0wkRweLgglbxPScGf27vb1Q-5kMeZwNXzAAjFLJMowISOlVcwJUD2Kkx00P4WEqKAAgFIwKKWI0LO2gVrQJ9XR9YrsiTWIGX29F41uV2ygSR_tIwLtoPwVNd8sfaApKqXTsjWs6mS_ENykHRMYNR_cZtTfX58JZjIB6t5MY56JJ9GQ06E9H4YOsMc-yOhrKwWo5tX44v3jRxedN7x-dyj4Jv5abjEOWnrw0T5Js76Uwy96JLieQmVzjETp39yltP4t2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SF0KngjQ8IJSaVw5ynkNHBRhN4MWDfNW6XKrAhxIWHBscAaSdgyucd8AT4CcO8dVwD-LseAk9teEcn41KOrieEMMGGjZhAYbTF5EY8UBJu2GGq8_SE2VBzO58ZcBiLPCqY1jqnU0BUTG2eebtDBLWdTows9IIbWgpfzaNCwnaHQ-zmpVuwkfmdMyj2NvUxB3X0cBsCjcJZgN3QFVMEEbqTgut88crAC3zYxUlvcMGxVXZmaafV9yeR7s37Ygwja8Y_umWerswCuCkwKOzOj8F-wnJLeHWLUnueoOV4olmp3kOeVzx-gBZXfchFECT4PdxPMNkcg1KuVQAt3xTRZYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور هنر
🔹
۱‌. غزل کرمی
🔹
۲. هدی ناصری طاهری
🔹
۳. ملیکا شجاعی @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465992" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d8a9de0f.mp4?token=MAgadmMe1iTsfdNs6D9lg-4FGzldAL3S_WEQeaMau_lMHxU__pgMednj6pYNTxDbo6DCxR2VfkOPUE0j3gosLC84DCqQcgHa-T0dyzv83TjDsBjFDffOLMHLbMpgT_1KlCZc_o1BvlqblUhODOCQpYYL07woyTmwaS4JKlB9cU-TKM7z5kdYLj_K3DU210aWVle4OqtjKJxTaP_eVuhoj3y1e-4GA3a7pf8rpGX1AkKPx7jnbN3Rp5KSS7Sxupfw2Cy2RZIarKPxCMTHW5jhp8xyDcupR32hf3g0yxZIuLLH4O2KRo-HyZ3jav7M51Uvv5R_Zx6TE_njsxpxqXW0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور زبان‌های خارجی
🔹
۱. ثنا اکرمی
🔹
۲. سارا اعلایی
🔹
۳. ساینا دهاقان دهنوی @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/465991" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698d1a0e28.mp4?token=GpG1W0M5nJ4nUM15WXh4o9GLfODhkUE28y1PQuP7xjjowj5cM0VWDJVyDpw7icRhqwK_E6fuBB0mKq7C3FlEmqGAoz4c5F5E52ZCQCSMAtFpHnEJDjya_XlUyNxEuy0TABWLJLvdSzPTlIWDfKkXrkUX837T9uvSvK2BlsEJlDMKP9vA8HSSYOnRZFqdD5AwF6kNfcLu3bqyyTid2hobUZ2zBQDAoWeC7bHgYcpwLm5jZWp1t5i8S6xRQuPKz8cHb4VVzQ6_c0XS7UPGX9vW0MWa7CxOQnM4c4ARfqpA1UpaZ7uOGY-Ec4LhozI7po1l-TeymcVavmBQFTuHysjjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم ریاضی
🔹
۱. اشکان کریمی
🔹
۲. امیرکیان رئیسی بهان
🔹
۳. امیرحسین جعفری @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465990" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89758407b.mp4?token=Jsm6iIwIIhtaI0nz-lK5Y8b5a0twzQnvtGczGjmp5znq6JT3H6ShTROKkqLD4Hm3bMoQ_Taz9SxVku22oTSVvPMgrNcjlutwm8IsxQvhDFqybLI1tqVwqOpvPSZt7vpIo7mW5iK8lAuoZK2mwPMUAiRaJkktjhEjBklZSbnS9irvw9x0UXnZiTP0JPmv3QAn625WghMm1UA6UuH3VuZFZhOZKcD_CwmluZ4y-zAoPA9W9d76x1_IQ2-dhitIQ6rv0cBFm2_EzlSzYBfSh95HND7_nIdwA-cOX5W12q7KX4V8oR2MBpGYVKkOs-6QhljaK2_E6eMpCHVmr605YvL4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم تجربی
🔹
۱. آرش محمدی
🔹
۲. سیدآروین حسینی
🔹
۳. علی جعفری @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/465989" target="_blank">📅 10:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42af7f2d26.mp4?token=f60P6rF9NroSlgbdtV7vdPYjfLMqCwi0dcOLWXlEJZC3DJl5j4gtFfyrV41xvdUAj3wdotJwI_02KCCv47MjtohodSP86OllM68Udo9gca6eMD2brLc-La9rK04m-_-u2dHKFVsJSfUxrLDZAbSdSM14j8hrFGDxKdQg3BYUer6ZEHzapZKpD8eQFQOf4R8nRF86LRII-pk8VoYQK08hh2ZRDpFzGOIx046mYvxSMFnkrYPlLQgv5K3KbBJ5Yay-UCGRWUNKoFcnYYckRvCdRMHv7ZPEnU80cJLlw1MRzz177OPxC7qKoFpO7ef6I0AgEuiXNFLBbDZSleXN8nWxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبه‌های برتر کنکور علوم انسانی
🔹
۱. پریزاد نیرومند
🔹
۲. یاس هاشمی
🔹
۳. پوریا زارعی محمودآبادی @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/465988" target="_blank">📅 10:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d38177d2c.mp4?token=ZDlaKKVwUVe4CNaaAKvc-T7w2WhyaaWGRpncV7LPyZK3iiWUSjf9xOem3hLDmDwaNyLT2Lnl_Al7DuGjxI0c2sbztquokR4bGEzHaRn22ALo9J9gaUQLAYn2_LTfq0-Os6qFVfS_dr5jpX8r-YMHuksYR0AZDL_Jg-hSIrWxUwthCcBAbHhyJo4cwW8xYQkOrSFMEEHuyferM7JZy3Ud88ggOBqWA57l77g7Uce4qOkN05OPnqj9Ytqns1V6-FfjEupCwOuHAKre_BgtrUdf6stMkEKIe2QIMMORp93vKmajg9H-TzXKDy_ZnO22buXjXr7JSGGXagFsi4oJcEZArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/465987" target="_blank">📅 10:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e635afaa1d.mp4?token=Ck1dXX4uR8O20neIE1CV18209g-8dp39wSJO3DQAJXe7YjLoGkA9UC6CvQxCUYFxfVb3bUVfbEsHjrDh4p8I1zjXFFLpFA0cpLtpS2J1Eb0LYl9P2xLKarfzf9MWlP09JNlzltlJwUnx9AMkqlHY-IpjD4MA1oQ4IcAy9bWREym12DfDuwH_dsvqchtarWixAVYm5vElF2fMem0gq-1mM_fIwq6wE-RdJ0zNEWyhA3iDnNa4vy75FRp-cV58X8AtQRdfzff0_JEMLmlFLDKjrkGnpGYbTqvNiRHODzdI59wMFFcVSodmsn0yq48NkPawzYKj2iIj__qrZwvblOfwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیاره، معاون سازمان سنجش آموزش: تا ۱۰ روز آینده نتایج کنکور سراسری ۱۴۰۵ اعلام می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/465986" target="_blank">📅 10:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2e23b992.mp4?token=rooyDoG-D_KnWGFMKiB7Ak-9oS54eIhNKMX70VJfOzmg7HaU0fBGEwsU6nrVYjaTPSZX7fgnX21inX8pmRFcEYSZ4i1Y71stvEYx0Eev1R23UehMQM3WvlgBoOmw1MvDfzs6H1MhVGtjfyQbBF_gvFLZA-0vllVZrqGhPVZaUdI89lRjK-C9VMm3yC0N4Ru58YrJXDsqKeI9rNr_SyH5jqt-bSqwcc2B9ynU6LVEv4ftH259Q81CWStvLDxJ9KfM6MnASBtnFttRdvRsAHtXb0E1hdnwMtagzQw02YBz_U_qN6pJEmqIMFzPyE-S7ttMO9DFupXdt-c-tNQQtr5maA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا  یک برد دیگر در تکواندو بانوان
✅
فاطمه احمدی در نخستین مبارزه خود در وزن ۶۷+ کیلوگرم مسابقات تکواندو با نتیجه ۲ بر صفر مقابل لین یی‌چن از چین‌تایپه به پیروزی رسید و راهی مرحله بعد شد.  @Sportfars</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/465985" target="_blank">📅 10:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465982">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHr-Fg74HC_o2nxTu5V4ONz6q1LUk_wo8pImwGffsSQGPNwydtZnZePXhYIYb4_OYLukteF7iiQ4LbFq6okbt8RD_rVYXjyCYSjr6hCgPKYlaiJD7r23g1usYqYkL7-CQtATjtV2KIEnXB8Iz_Pndxp63EyiEgHwcguJ0MtaBlrv6EvBITuKqyHQNIOZzwK7NVdJ8tHCxnjM1_d9jcxTj8yEA-wTMkIJm4iSU8bqBn41l_M7g_xBvGu3g0-CQz21RaQRVEAU-fR5zTF028yg0RsDqAuzM7JfbHI1PPNMd_VXxGbrLCpPt4jVd5JgdyttD02EgVpRLE3WMztTtjIzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVb_THql9qPsqwMLewur04y5CScgKxGFJLCw6he6kHp7ox1fNhtWfwjYsePH_JWSljVZccNaN9jHZK1gx4QcjMh8H6qzbRYO-MCwMn_dPNDeInCGZfgr5DIuMw-QkdZGhgUZ2zbePCmI2TWX28ELKyistKGXe51EEKb7JIqQ1i2cOj1mhOg1mZ5rx7lOttW08Hs-Wv5cUnVGfd_1mQtXQdq2CkyCJZTx4WHz92OydhDSOcUQKKwXnvmGr_n7c4Ou6BC0ePmDWy1Psn3R1pha01sLUR7HiA03BiZCLNrvpSnqaegL0BKj4s7k-DXa4OF1Nfq_WJfRsQQyDvT567zMNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86287d76d.mp4?token=tOKg63leROKb317dVyRmQJGZpBKc8XOlKbbqEyg6wGlSv6phM8YtfGOIrnpHIm8bplEQNG_ilW25lOS7c6epE1WhxRqrBGKq1r3zaAJSSg9lHvPPXUUkBjxEm-pxc8uVok0o-L5gXKPSdgkkOIWNEpR8e2yYxtkVbVk32Qb01LHh9cF6qzPbKdKTdw0QMjSXU2mciXGTzgYDiCBqjoTb7O3mAHP-zOOmcx0KrBCJEVglqhlgraZS-WsxL-fPKaN7cyuP97v9BZt0olor6VGo3YTbOJK-IDgVUv3Ot5paeULVK23V_9A3Dfufa6Wjfode9AOAc41nBjSSrgNow-aC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استوری‌های راحله امینیان از وضعیت مدارس لبنان و تنها خواسته مردم لبنان؛ «فقط سلام ما را به مردم ایران برسانید»
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/465982" target="_blank">📅 10:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465981">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViQcU6vgDjrVi0-9HKx9AAAsFdXpUgyiUdTu0-OpkrBChGtBFQuprl3_25lhNL7_FPUnvgb2NipSMZi34YzIfiBtkahAg_Y4Cv_DxQzUIcyKY57MGTUQLPa4Rru3L64nxKNoBy0Ct35YtjZfgKmpMnJmm5VLKQ0rU3MQVqbcLFdWoMiiqahVGGYJ8-2blZGKko3-kLwA2JoX9NRlOjpptc6srPTA8Hw_PZ0ZDxE9TTz9Rr7TStvb2X21XHgNz_R6lfNPy_ONpY_E3p0WVWp0vJla5SVa7Xkz5_a_H9on3NrSM7hBjQ7M6w-a8D0oNEvkH8tZ9nAnOJuIGjsTAq-_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در مسیر غیرقانونی تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که بامداد امروز سمت چپ یک نفتکش در فاصلهٔ ۴ مایلی شرق عمان هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/465981" target="_blank">📅 10:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8d6aa62.mov?token=O3qLhSzuxscTldFPD32g1v1qdU5x_oq1MyX5Y6bFZUFAuHF_XMerjpThkRSkSLp_E_trh9XkbEHPe-RObD-0WVOv4NuLaZZNZPkrRm200qB4RUAl5OGlhTJxjDmMUelj77v2_FnRAx8mm7ayvJnNpyyZ2Uua5qk4uAyAHehYp6hsW-MNZTU3ULmONAKvcqF-txXmHmBNc4vXG1vQeKBbmWCTOB7ToBactT1z1D-rdBq4TgCjQ3V9Yh2KdFVbWRPBy-J1dK-AtPo9oOJKy2PYs7oCuVmeAbGoNi_If9yzO-o8Temi_u4fwddd9i5p55g-rDVQt209yj8slF-kFD9hYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رده‌بندی تمام ایرانی بدون سرمربی!
🔹
با توجه به اینکه دیدار رده‌بندی پدل بازی‌های آسیایی بین دو تیم ایران در حال برگزاری است، سرمربی تیم ملی در جایگاه ویژه، تماشاگر این مسابقه شد و هدایت هیچ‌کدام از تیم‌ها را بر عهده نگرفت. @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/465980" target="_blank">📅 10:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b3fc0d84.mp4?token=G7Z_li4iVIMQoRnlqKpQyj6AgA5idh50fAY5kGGRN6yLyQE0qdKrZ9f6bgR25Yb6nl5fRnVGByYi9cKzsyCrIXQN56iX75-ZCidq5qxyocbQJtD0On0IfJeMkrt7v30rlssLm0BeWLomF_B9aAAkAjV15JGWGSE92ftlGCuGtca3nTiXUg9kBbCzbolya0YBHMVTq-sG0aFYbk3bahG5LAjZaizck34pt6Dquvf677kBu3q79C5NaXBg74B36834CN_S2gMAmYIta0Ip070405uc-oQa3w-xyseeZ7EQqDjkrPGx0Zp2L5pu6eyDkAP0sqKM3i-0NxedgV7Zsnx_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مجاهدان لبنانی پس از حمله اسرائیل به ایران و شهادت رهبر ما وارد جنگ شدند و با چند هزار شهید، نقش بازدارنده‌ای در برابر دشمن ایفا کردند
🔸
برای احترام به این فداکاری‌ها کافی است فقط ایرانی باشید.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/465979" target="_blank">📅 10:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b040582fd6.mp4?token=dihD_ngtigztTPcM86-7Lwz3L6aVxiTsfDXbaZkJezGUOlMhsncjPmAPj3gQ0utNUtDPwy5V7YFQy9sYIKi5OcFRfzB-H9S6XzRjjAb6S6uKdbtw-Fmw2hFwjkXsh9AMg5zTb2FpMBMJuwA2xtMJeDkSPid4TpB8EHGYQDYuxpV2ijc1YroZHrvehaTBbcAs4IE7wZnPOtddc5kA_JqcAyVB-10a5MkRfq2FL8fPyM4XBVmdB7CgfZ2pUSD5nAfxXuOd0DoDvaQM5wGmEP3JG1d5THMDRk-Jydi1fSn-eBWP2LAl9qfz9LA48ztA-AtglOfRKp6BL2jyOcs4AlHULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور، رئیس سابق سازمان برنامه‌وبودجه: ۱۰ میلیون خودروی فرسوده، بنزین را می‌بلعند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/465978" target="_blank">📅 09:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e47fdeb.mp4?token=SLlyMFk7FDOdScZvYNIzmd6jTsXbAof-vuOZTpuGuVxYFFwNTzdjFXh3aY2i6nHkEu1MGhJQWzOmGHrSZAwyQ_Tu4-xQqiB_1-e5z6PwspTkath8QN2PGNbC1vrNVxYCvYJkKUWqjbz7e1XfEC0zQuAloW3dwS_jYOHcFj0HhVtt9KSqOpLJf0tnriOQZisyqWiTEhLCq5NlafCwjTsiLLzLFZg--0RZDPll21bKIac751PnNcOmyvCSu8efZo8ThR0JJOm4s-P9pWcIF9BCi8o8w4CmGEYqzOc3PIN3XrvtLuAU27iafb77TD4Y37FrAqU2iaRgwhUIhuogXAinJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در لبنان: مقابل رزمندگان، مجروحان و خانواده‌های شهدای لبنان جز شرمندگی احساس دیگری نداشتم؛ این مجاهدان دارند جهاد می‌کنند
🔹
خانواده‌هایی را دیدیم که چند شهید داده‌اند، خانه‌شان را از دست داده‌اند و در اتاق‌های کوچک زندگی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/465977" target="_blank">📅 09:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یکی از متهمان پروندۀ دوومیدانی در کره‌جنوبی به ایران برمی‌گردد
🔹
یکی از اعضای تیم ملی دوومیدانی ایران که در جریان رقابت‌های قهرمانی آسیا در کره جنوبی با اتهام آزار جنسی مواجه شده بود، پس از پایان مراحل اولیه تحقیقاتی و رفع ممنوع‌الخروجی، به‌زودی به ایران بازمی‌گردد.…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465976" target="_blank">📅 09:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a14e06e9c.mp4?token=RnCZIGiYyOkKviBuVN1j7ttqVIoxuaYbb6hzphjPEefi3VOJ9Bc6IgnVgL5Jd6sNOB1sX0tHypq1gcl7bdIgBCoGO19ZyIayAP7b9HVh_OdgcIAQWNbcLEhFFEJRhHmA5iQ-hjCMQn_oQSF7FMN6TYr5KE4ayQWLdREUBzuF2qzSon81MNQQg2yN0dfDQzK0aQ2qimzv8gCUDNks5-TfMfPfWB689XAxx1Pxu-DyViFItRoMcNdJq7y8FcGWA5zup5iiER1lW0uuF6ZyM110plmb__BJRCDZuJV6jNE8Frx8cGZ8S0dh6L01BZAaHL7YaSTG-VVzEdPL3Mun0XGs9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن آرامکو در ریاض خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465973" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465972">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/simzBoesBqiMimDGGA0PWPCf8HEEcqrYpysoJJPttkSkYKIPa4f_8Ufajfi7taLUHug5baqe_f4KmpeGsCf4eKT3_7cuiKniy4KOYz-A8i8RpEGMN0jQik-Y2hKGXoO9Sbo4a6w0gG96HMYaMcCcjsyCWi7JXbu-As3WcjGwhHTKKuX4Vy8yxUgxSfvOjAnd8xvpOjv1Rl-riBVbvf6Lx51Oo4qXh6VZBuv6mlwSTKA1d4rI5u-aLAohmTlvgpb-Zvcb5soJs-oA-NTpWiT-9Ypgp3F5owHnITO9wmTFEvKDpJHeCMw4Y0BkdmwOn58AFNvwKc3zWt2oGgHmgu7_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین نقشهٔ نفتکش‌های تنبیه‌شده توسط ایران در تنگهٔ هرمز
🔹
جدیدترین نقشهٔ مؤسسهٔ واشنگتن که نفتکش‌های هدف‌قرارگرفته توسط ایران در یک‌ماه گذشته را نشان می‌دهد، حداقل اصابت به ۲۰ نفتکش در مسیر غیرقانونی تنگهٔ هرمز را ثبت کرده است.
🔸
این در حالی است که ترامپ همچنان مدام مدعی «نابودکردن نیروی دریایی ایران» می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465972" target="_blank">📅 09:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کشف سلاح کمری و فشنگ از دکهٔ فروش روزنامه در تهران
🔹
پلیس تهران از کشف یک سلاح کمری، ۲ خشاب و ۱۶ تیر جنگی در بازرسی از یک دکهٔ روزنامه‌فروشی در خیابان مولوی خبر داد و اعلام کرد که «متصدی این واحد صنفی به دلیل نگهداری غیرمجاز سلاح تحت پیگرد قضایی قرار گرفته است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465971" target="_blank">📅 09:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465970">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d58c47b27.mp4?token=bbmei9iqL357tpC_DNKUPljzIb4udfU7MIuY_6PLCsWTpzxqAQn1j6S15CLryS8oHSgmUB_7M5pgWpw2C57onFk1IeqlHRcTvyRF_7eckXouj1x_yUK3xknUMUkQSdlZAOqEN1KJSN0mVaCXbIMadAakEcdHe1ktSxgxG3RjxNa7QXoTrV4ZMNcmHhq2U2fZd1eANHWKl22JNJ2TmyMWa1_IUt3oqsyCdi77Nw5qoJzMnC_Gk2zcGIkUxr1v8FTsT8vMA4ki7NtshG-YR6dsPQQJLzaVTuIBiPzLXbOOnpxP374EgFNd8RsPXXp209YlL4OYE6wPb3941_dQEpWsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d58c47b27.mp4?token=bbmei9iqL357tpC_DNKUPljzIb4udfU7MIuY_6PLCsWTpzxqAQn1j6S15CLryS8oHSgmUB_7M5pgWpw2C57onFk1IeqlHRcTvyRF_7eckXouj1x_yUK3xknUMUkQSdlZAOqEN1KJSN0mVaCXbIMadAakEcdHe1ktSxgxG3RjxNa7QXoTrV4ZMNcmHhq2U2fZd1eANHWKl22JNJ2TmyMWa1_IUt3oqsyCdi77Nw5qoJzMnC_Gk2zcGIkUxr1v8FTsT8vMA4ki7NtshG-YR6dsPQQJLzaVTuIBiPzLXbOOnpxP374EgFNd8RsPXXp209YlL4OYE6wPb3941_dQEpWsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: بیش از ۷ ماه است که برخی مردم در جنوب لبنان آواره‌اند و تقریباً بدون امکانات در یک مدرسه زندگی می‌کنند، اما با صلابت ایستاده‌اند
🔹
با همه این سختی‌ها، آن‌ها حال رهبر معظم انقلاب و مردم ایران را از ما می‌پرسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465970" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0b96e3f8.mp4?token=aaepDG087H6BsnY79X-APl4sKLaBZma03arPRQeIunuXcqrL6KpptoTuTe2iroosyC7_5MegCJmbLv5rEbYsfRyE1Xd85IFIWDGyT5I0uoczzEapiwCTAp1APamjj6zIh6ofSj1WVoU5VS0dJ4BhkMKOtGFAOoaydTl__xzTNNX3TQELkEmbokB1oXTCxw2POn0XmN53dozzCVTzI7mEVHKajOhmKYQ6aLwD8k1tk8OINv5sFRHHSf8JrH5FGp0U-iTjqY-f2p6_N7hS4IB67bKGWav8Cs1FqyLM3uhznB1GaObA2K0cLP4SHp6LyvOwyye2v5H1BOxCSYHq75B8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0b96e3f8.mp4?token=aaepDG087H6BsnY79X-APl4sKLaBZma03arPRQeIunuXcqrL6KpptoTuTe2iroosyC7_5MegCJmbLv5rEbYsfRyE1Xd85IFIWDGyT5I0uoczzEapiwCTAp1APamjj6zIh6ofSj1WVoU5VS0dJ4BhkMKOtGFAOoaydTl__xzTNNX3TQELkEmbokB1oXTCxw2POn0XmN53dozzCVTzI7mEVHKajOhmKYQ6aLwD8k1tk8OINv5sFRHHSf8JrH5FGp0U-iTjqY-f2p6_N7hS4IB67bKGWav8Cs1FqyLM3uhznB1GaObA2K0cLP4SHp6LyvOwyye2v5H1BOxCSYHq75B8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رده‌بندی تمام ایرانی بدون سرمربی!
🔹
با توجه به اینکه دیدار رده‌بندی پدل بازی‌های آسیایی بین دو تیم ایران در حال برگزاری است، سرمربی تیم ملی در جایگاه ویژه، تماشاگر این مسابقه شد و هدایت هیچ‌کدام از تیم‌ها را بر عهده نگرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465969" target="_blank">📅 08:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سیاوش جمشیدی، از اوباش مسلح شهرکرد اعدام شد
🔹
کلاهبرداری، تهدید، سرقت، حمل و نگهداری سلاح جنگی، مشارکت در آدم‌ربایی، قدرت‌نمایی، واردکردن صدمة بدنی عمدی، تهدید با سلاح گرم و شلیک با سلاح کمری مقابل حوزة علمیه شهرکرد، از جمله سوابق متعدد سیاوش جمشیدی بود.
🔹
جمشیدی همچنین در جریان کودتای دی پارسال فعال بود و با سلاح جنگی به‌سمت مأموران پلیس شلیک کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465968" target="_blank">📅 08:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af39fa7c6.mp4?token=BLWAuT-D9dGDwlc_vIePKpcx3Zd9uq0F45XZVVaVpJG2qH-1jtSpLDm4OzbkXFR_MFrWBYti_SuEIyDKQIus8q6ECKLtK_PFmfJM_Ao__f_m8oOzBkQcpUyHIQALMdLxbTArOnNzMDdLlZwsqbkT0brjrNloFyqgsYgQtGDkjxudassPK2zZ_rI20cnOTi0Vyi-51p06Jf-7uqNPfKKpqF3PVucHY6OxqqP_LlMZvIwIkUpPIPpaq1AQKjDMU2FkLJFHd1olsr0EOfqZCDOPohnVsPGdVDDd31UmrGsPR6ZKegSwsbHpjRB5sxI-8MGwl8wRdz1yuiyMihdsctax10bwlym6bSQn3p1g7VEtd2evahx6CVnKL-zlMPJWJ7J9-btVDLcEMt5rHj-pLp5qC9xHAqWv-3yBTH_yxYi7MApqRhBs3hAgKNLs5zs3s23SbsB7zun2N_iJp43FuaM8zO6Jg2xqDCk1Xs0lPy_443w1yaFAIQt00JetIdk7PJpqtpy0_QaPCxmCk6VUqTr4XcSKOmP7AiCYpv8_b-VdfAh0HGtPp5rNfzjBbZi2JQFhlHOnjGLQkADFScaOXPwe7DgQrgcwtTEUHEi5TNfqhfOgMKAgBQzvVYmqknJaz8S-cFm_uoj9Isao0Jphi7m-lZOvGo17k6LokGRc2ksewPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af39fa7c6.mp4?token=BLWAuT-D9dGDwlc_vIePKpcx3Zd9uq0F45XZVVaVpJG2qH-1jtSpLDm4OzbkXFR_MFrWBYti_SuEIyDKQIus8q6ECKLtK_PFmfJM_Ao__f_m8oOzBkQcpUyHIQALMdLxbTArOnNzMDdLlZwsqbkT0brjrNloFyqgsYgQtGDkjxudassPK2zZ_rI20cnOTi0Vyi-51p06Jf-7uqNPfKKpqF3PVucHY6OxqqP_LlMZvIwIkUpPIPpaq1AQKjDMU2FkLJFHd1olsr0EOfqZCDOPohnVsPGdVDDd31UmrGsPR6ZKegSwsbHpjRB5sxI-8MGwl8wRdz1yuiyMihdsctax10bwlym6bSQn3p1g7VEtd2evahx6CVnKL-zlMPJWJ7J9-btVDLcEMt5rHj-pLp5qC9xHAqWv-3yBTH_yxYi7MApqRhBs3hAgKNLs5zs3s23SbsB7zun2N_iJp43FuaM8zO6Jg2xqDCk1Xs0lPy_443w1yaFAIQt00JetIdk7PJpqtpy0_QaPCxmCk6VUqTr4XcSKOmP7AiCYpv8_b-VdfAh0HGtPp5rNfzjBbZi2JQFhlHOnjGLQkADFScaOXPwe7DgQrgcwtTEUHEi5TNfqhfOgMKAgBQzvVYmqknJaz8S-cFm_uoj9Isao0Jphi7m-lZOvGo17k6LokGRc2ksewPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: می‌توانیم اهداف متحرک را با موشک بالستیک دوربرد بزنیم
🔹
مشاور فرمانده نیروی هوافضای سپاه: یکی از چالش‌های ما، اصابت موشک بالستیک دوربرد به هدف متحرک بود که در چند روز گذشته محقق شد؛ موفقیت‌های بیشتری نیز در راه است.
🔹
در هر عملیات، با استفاده…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465967" target="_blank">📅 08:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465966">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7fdb6739.mp4?token=mxz6rWvxPD-yvPacUMJL6IuH72e8AJirX09yg6ARjbHweFkj_zzbc1ZcbLLw2vZb8VGjkBuyV9QYHj_EsUXVFoHTBf9C3w9mzMhbGFWKbV8bzHuVZTpCNUHQDRjZS1KMxA0zqbZyuxlarRQa88zTrlJuyKZCd-OeKZdktE_wniSKvsqbiIBlkRHWdRYAK6w4E_fGEYrmyOjPTIyxJHHuaI0MVHVCI6bOAkOfijIEp0b9BHo-0kI9Z87jJGAAxrDYZEOgntGCmdmmirOfPh0lsTJ2n8ac21cYJP-VPIl5lgLzbHGe1rYL7PZgD-rfq6s3oaGu3TMa_68stAG9KFvbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7fdb6739.mp4?token=mxz6rWvxPD-yvPacUMJL6IuH72e8AJirX09yg6ARjbHweFkj_zzbc1ZcbLLw2vZb8VGjkBuyV9QYHj_EsUXVFoHTBf9C3w9mzMhbGFWKbV8bzHuVZTpCNUHQDRjZS1KMxA0zqbZyuxlarRQa88zTrlJuyKZCd-OeKZdktE_wniSKvsqbiIBlkRHWdRYAK6w4E_fGEYrmyOjPTIyxJHHuaI0MVHVCI6bOAkOfijIEp0b9BHo-0kI9Z87jJGAAxrDYZEOgntGCmdmmirOfPh0lsTJ2n8ac21cYJP-VPIl5lgLzbHGe1rYL7PZgD-rfq6s3oaGu3TMa_68stAG9KFvbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: انگشترهای اهدایی رهبر معظم انقلاب برای خانواده‌های شهدای لبنان مثل «خاتم سلیمان» ارزشمند بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465966" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465958">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106db1b8b3.mp4?token=JdHUib_hciwop9bVgDLLGQYDsHxQDPNB49QkEupXOCJh7Lbm7eQk-pdo5_c3_cIS-AKTPl5GeILyXETJJ0MT-3AsXJbqmxHbU4i18sjAelzPyDzX63q4afCcqTuczqKoCYPwx5N-Uipmkfeu0LG6zoN7aH1kY0Fh-xZts5opDtur201cX2qNpJNayItVtsRG0aXsE-JJCkuP7QlBqcPHL2Wh9ATORlo023kY79ZpRdWDkYhlLho7qHKem6WRWfK0V7yOuBlBha7zfDIYOPRQxVTM3MdjaaykSbULPpA-Seu7fft8ngCF3p9XpRY87uz5TDzSCziZCG8XmM_G00tNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106db1b8b3.mp4?token=JdHUib_hciwop9bVgDLLGQYDsHxQDPNB49QkEupXOCJh7Lbm7eQk-pdo5_c3_cIS-AKTPl5GeILyXETJJ0MT-3AsXJbqmxHbU4i18sjAelzPyDzX63q4afCcqTuczqKoCYPwx5N-Uipmkfeu0LG6zoN7aH1kY0Fh-xZts5opDtur201cX2qNpJNayItVtsRG0aXsE-JJCkuP7QlBqcPHL2Wh9ATORlo023kY79ZpRdWDkYhlLho7qHKem6WRWfK0V7yOuBlBha7zfDIYOPRQxVTM3MdjaaykSbULPpA-Seu7fft8ngCF3p9XpRY87uz5TDzSCziZCG8XmM_G00tNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالیدن چشم‌ها می‌تواند منجر به پیوند قرنیه شود!
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465958" target="_blank">📅 08:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465957">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نامهٔ ۶۵۳ استاد بانو به وزیر علوم: چارچوب‌های روشن پوشش در محیط‌های علمی را تدوین و ابلاغ کنید
🔹
زیست عفیفانه در دانشگاه، نه یک انتخاب، که یک ضرورت است. ‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🔹
هر آنچه به ارتقای تمرکز علمی، حفظ وقار محیط آموزشی و تقویت امنیت روانی یاری رساند، از لوازم بنیادین حکمرانی علمی و فرهنگی است
🔹
غلبه ظواهر و حواشی بر فعالیت‌های علمی و پژوهشی باید متوقف شود.
🔹
حمایت از مدیران دانشگاهی در صیانت از حرمت محیط‌های آموزشی و پژوهشی باید مورد توجه قرار گیرد.
🔹
تدوین و ابلاغ چارچوب‌های روشن، متناسب و متین درباره الزامات پوشش و رفتار در محیط‌های علمی ضروری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465957" target="_blank">📅 07:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465956">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌ آذرپیرا به هم به نیمه‌نهایی رسید
🔹
در وزن ۹۷ کیلوگرم کشتی آزاد، امیرعلی آذرپیرا در دور دوم با نتیجهٔ ۱۰ بر صفر هملیف از ترکمنستان را شکست داد و به نیمه نهایی رسید.
🔹
آذرپیرا در این مرحله با آرش یوشیدا دارندهٔ مدال برنز جهان مبارزه خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465956" target="_blank">📅 07:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465955">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امامی به فینال رسید
🔹
یونس امامی در مرحلهٔ نیمه‌نهایی وزن ۷۴ کیلوگرم کشتی آزاد، ۳ بر ۲ حریف قزاقستانی را برد و به فینال رسید
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465955" target="_blank">📅 07:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465954">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
هواشناسی مازندران: به‌دلیل تغییرات جوی شدید، فعالیت‌های دریایی از اوایل وقت شنبه ۱۱ مهرماه تا عصر دوشنبه ۱۳ مهر ممنوع است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465954" target="_blank">📅 07:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465953">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2538348579.mp4?token=GUHNStEck_hfEaNLCWPkEkOOOjeitRlIgyqbPMKWLEgwkvd4rTAlZMwKSuusFSKKasAvKFyiNPcuP1hcdbMBfEpmBNExy4lJQUb3rBEVQPoarw__SqvKabogWyx_Uf8xFLQojJsYRnyD6FVAsurL8G7luIEkvIn-L9Yw4z8ZW02A_se2jtzeDmfNbf24FtXg-nI2Isa47ahYIyaS6wVLnUQQgKmSUCjA3J5AZpaRtiliYYKVVgJfOYuG3Wrs8kO8XcGYMDfxCDx0wbw-wBQleoQTvaZ2hbO2D7Jfni2o8Wy501p9W_kqP3eR1Tt0EYONRnz8jtuJQvbplzF64IdvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2538348579.mp4?token=GUHNStEck_hfEaNLCWPkEkOOOjeitRlIgyqbPMKWLEgwkvd4rTAlZMwKSuusFSKKasAvKFyiNPcuP1hcdbMBfEpmBNExy4lJQUb3rBEVQPoarw__SqvKabogWyx_Uf8xFLQojJsYRnyD6FVAsurL8G7luIEkvIn-L9Yw4z8ZW02A_se2jtzeDmfNbf24FtXg-nI2Isa47ahYIyaS6wVLnUQQgKmSUCjA3J5AZpaRtiliYYKVVgJfOYuG3Wrs8kO8XcGYMDfxCDx0wbw-wBQleoQTvaZ2hbO2D7Jfni2o8Wy501p9W_kqP3eR1Tt0EYONRnz8jtuJQvbplzF64IdvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید حدادیان: در ۲ جنگ اخیر تعداد شهدای حزب‌الله لبنان ۲ برابر شهدای ایران بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465953" target="_blank">📅 07:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465952">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRTpSd4177KZuQntE-nYv1v3Kh3Q4lt7XQ1b89gW8rHakn4nwJwnXNUGOZe-93ZKyAKvu49dAGD8l27WCdzeYXyShs3hl8s8_HLUP3i3lDTMlqRqzs0juap4H5DJCLyXUgT6aCwLOKTpk0b3Em2CFfsF2KOTx6zfMI8BGuixuF01d-9deDpHf6XdtecmB8r7SMO7ViKk9ip04cH00Le3-ScTzOJcy36YUwjoqTQoxPQ564RR_nOaK9TTaQqh1zWBJRhHR9bZFfekd_IeHey-ThYemw-5ErSi2YrDjykZKBcxqTr9qM7IzokfdbwikOYjwfQk23fMmgaPN4D0g8ohCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ نفتکش در ۵ روز در هرمز به آتش کشیده شدند
🔸
درحالی‌که تقریبا هر روز ترامپ می‌گوید که تنگه هرمز باز است و آن را کنترل می‌کنیم، گزارش‌ها نشان می‌دهد که نیروی دریایی سپاه هر روز تقریبا بیش از یک نفتکش را هدف گرفته است.
🔹
اکانت رهیابی‌های دریایی منچ‌اوسینت بر اساس آمار نیروی دریایی انگلیس می‌گوید ۲ نفتکش کویتی و ۳ نفتکش اماراتی در ۴ روز مورد هدف واقع شده‌اند. حالا با دو نفتکش هدف گرفته شده در روز جمعه، ایران ۷ نفتکش را در ۵ روز هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465952" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آذرپیرا به حریفش رحم نکرد
🔹
امیرعلی آذرپیرا در وزن ۹۷ کیلوگرم کشتی آزاد با نتیجهٔ ۱۰ بر صفر مقابل محمد گلزار از پاکستان به پیروزی رسید. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465951" target="_blank">📅 07:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465950">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مدال برنز آرین سلیمی قطعی شد
🔹
آرین سلیمی در مرحلهٔ یک‌چهارم نهایی وزن ۸۰+ کیلوگرم تکواندو بازی‌ای آسیایی ناگویا، با «هائو تانگ» از چین مبارزه کرد و دو راند پیاپی به برتری دست یافت تا ضمن صعود به نیمه نهایی، مدال برنز خود را قطعی کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465950" target="_blank">📅 07:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465949">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حذف کشتی‌گیر آزاد با شکست مقابل تاجیکستان
🔹
علی مومنی در وزن ۵۷ کیلوگرم کشتی آزاد بازی‌های آسیایی ناگویا با نتیجهٔ ۴ بر ۱ مقابل آیال بلولیوبسکی از تاجیکستان شکست خورد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465949" target="_blank">📅 06:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465948">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ناهید کیانی از دور رقابت‌ها کنار رفت
🔹
ناهید کیانی، در وزن ۵۷- کیلوگرم تکواندوی بازی های آسیایی ناگویا در مرحلهٔ یک‌چهارم نهایی مقابل حریفش از چین‌تایپه با نتیجهٔ ۲ بر یک شکست خورد و از راهیابی به مرحلهٔ نیمه‌نهایی بازماند ، و از دور رقابت‌ها کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465948" target="_blank">📅 06:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465947">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شنا و صیادی در دریای مازندران ممنوع شد
🔹
هواشناسی مازندران: به‌دلیل تغییرات جوی شدید، فعالیت‌های دریایی از اوایل وقت شنبه ۱۱ مهرماه تا عصر دوشنبه ۱۳ مهر ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465947" target="_blank">📅 06:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آذرپیرا به حریفش رحم نکرد
🔹
امیرعلی آذرپیرا در وزن ۹۷ کیلوگرم کشتی آزاد با نتیجهٔ ۱۰ بر صفر مقابل محمد گلزار از پاکستان به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465946" target="_blank">📅 06:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465945">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">امامی قهرمان المپیک را برد و صعود کرد
🔹
یونس امامی در وزن ۷۴ کیلوگرم کشتی آزاد با نتیجهٔ ۷ بر ۶ مقابل رازامبک جمالوف قهرمان المپیک پاریس به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465945" target="_blank">📅 05:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465944">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b494059ca.mp4?token=Mi7Y00Xtr2t-sJLChiFgLR0LP2XaTuEeUv_bgGL7qACGRYKjydNR7hQuKDYrXbSJZUtyFp_Y4-sTFMXuPzoe9eFaAzHHrQ3Z5Lcluyz2rTXpB1DYtjf8jAgxJts91sj8_OenxTnP2Bg-ivKtfse2GpjVMvHS17oLd-F9P3ysXHZZ3YtRJLAVlpYwsH4C793YiJToI6W3DLHyUXBTK-RAAmfthBEMHjhjANwFDLszHo_36LlyeoOTGFC8VwCx4y7JkXnVEcCfFWbx1XQua7OJJWIvXXUxv48VnRvaUpWb4Kw4w4fS1bFpM2If2RT9mIXUBfHvzuqEvCNaZIJAiPOrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b494059ca.mp4?token=Mi7Y00Xtr2t-sJLChiFgLR0LP2XaTuEeUv_bgGL7qACGRYKjydNR7hQuKDYrXbSJZUtyFp_Y4-sTFMXuPzoe9eFaAzHHrQ3Z5Lcluyz2rTXpB1DYtjf8jAgxJts91sj8_OenxTnP2Bg-ivKtfse2GpjVMvHS17oLd-F9P3ysXHZZ3YtRJLAVlpYwsH4C793YiJToI6W3DLHyUXBTK-RAAmfthBEMHjhjANwFDLszHo_36LlyeoOTGFC8VwCx4y7JkXnVEcCfFWbx1XQua7OJJWIvXXUxv48VnRvaUpWb4Kw4w4fS1bFpM2If2RT9mIXUBfHvzuqEvCNaZIJAiPOrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
یک برد دیگر در تکواندو بانوان
✅
فاطمه احمدی در نخستین مبارزه خود در وزن ۶۷+ کیلوگرم مسابقات تکواندو با نتیجه ۲ بر صفر مقابل لین یی‌چن از چین‌تایپه به پیروزی رسید و راهی مرحله بعد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465944" target="_blank">📅 05:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: شاید درست بعد از انتخابات جنگ با ایران تمام شود
🔹
رئیس‌جمهور آمریکا که به بیان اظهارات تکراری شهرت دارد، باز هم گفت که جنگ با ایران به‌زودی پایان خواهد یافت.
🔹
او گفت جنگ با ایران به هر نحوی به زودی پایان خواهد یافت شاید درست پس از انتخابات میان‌دوره‌ای.
🔹
ترامپ همچنین یک بار دیگر وعده داد که بعد از اتمام جنگ، قیمت نفت پایین خواهد آمد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465943" target="_blank">📅 03:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMSiKpJBiVxR2aEf4xHq8CUh_BBK3u609rJe8AR3zb84XRVRdpQivKi4vFQZDkUAH-7Nl-V3g_osgiSAFutj0WTYI_3zkHRgloAYXNpmuIBpmeV_yMpPBRRhYQYbOiVCT3RYwwtaLVT3sr6jYLCQrTkb8MJ06rWR4Gd4fk3V-e5XP7Qd-HSomB6r6j_LHPlO96Qf70kXZS7q-U3G0_mFKbZ4jFhGBL-nXdbUo3I49KaDv6Ct8Dufb-SWQ9NA5YndZ923PMnZoZNF_rOR_Y5t1c_Ql4qourALK5CtTe6SDramDuFolhCzbZ-JnlncO3x5pcxt66cYBw6RC5a-numCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNLJQhsanXWvFVrMv3AWWRbOpkLHyooEUyIWBSA-N9fEvtOkRPIi_anGniDK6bWr64EZYqKN-lHUjQps-0l9x6Whz8kZPg5308BLXtGRi5AIwo3zriOdBN9kvkfYd1OvMg_I16BXqn7vYl4dqU73UI3c08-Wm6fOiKU1gMUNYue3LYZ8oNzjrClBnuwGfuGn7DPoku2ckMrk0FWQPDg4l38nWacAwSc4mkv6axExFmhHVgurqwuYAKy4cssYYHdtlC03vSDX4BsBdHC9mLjV4iuWUN6NQOxlbZ_8VDRu4z32Z7gOEo3mdNE1xqxf_5Dbs4Lm3FYii4KQR-rkJOuuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLG3WC75OcuQ-Z4xt4TfGy3Z2sFDRXLNeMmGpdhTrDxp87RB2BwfcCjfTQ1BFEsuHEIbZN4B0DVq2fobnXLJ5PSZYSPikhdkTGrvr4gKaXUUij6kmM5cXiHhbbOuf-6ZKAOJgK-rs8D_SQLuU81-QREStu9Cx0OeCwMwWtUqmigXk6MrI-_FSn2rcp1gqHzpFAXjnRxjesIVVJq66tpqkPf_m8-Nxx_iEKVJxPfqsSnZjKxxoBTjrs8jeNIn9hmmgCbDRdys7C3p35p0IGmgJJJo7DfFVYfaA49djyZJ52LHwnxpXGNnesknfcz5SuHhxgMEysa6tKV3j6KH5kZXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP1_3I3M8I66p71GfO3mJuATlsq9-ZMPXfniMh3n2ftFS3kGATHqhUBCmIpT5HJYjqyEi6eCbkW_h05VNMlW_C0ald0B6aLnT12fWHnaFphaxPJYfWvB_hf6dM4WUuGkcc020nYEHqhCKbOq4YVknICjrLzQxBr4NQZdt455MqQu14rqzXRrcr2OHT937bHU3A_TASnuZ7filmv_B_sva8DaiAJNT7pZnlVejm0eaVY5_Oe4Ivo-_EvjkB4AxyUgtqrukpyaGwhOHvyz7dSp1w1aahObc8zEQgb0pIx2nIQofIAHjk-8rVsrvuEL6KZnHJXVneNISg__DkfIUlEkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPwzSucqmSgKdJZz4Ut7nS10GpPlQm8TFfAY7PGjP-AXu1hudPYtq0cpZ5jhnlM1kg_6ffAsxgZEfwC75hjZC8Qg5jUTmFZZpPtd0dRgK93qBTlNlHyx2Am7D11cd1QU0xNgQddTCBOL1MdMRylFKKqT2rjIMLlfEQ0HmjekAy-VAyMj_Gg8FppW4BSHCLI8nZOBHBDd8R6v2fMLT-pJNp-iWCQxkRNShv4pSRdkgD1hGKrpnqhiVYC0AoqYF23DkvLNGG7WmLC-Gnrpi2ZXp1YCgrnL0Vjd06aFvF1jbqjeGVLN94-tM3gqOnX1mITUB00PaDN3pB8y4NEjp166NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qg9t2cuqi-D0HImjTD0OrzGTJZbOdfzyzJSg3flm8Q6x6GyCW8hjZINr0Xrd5copuSr_Mmz6hpg1Ruwrtx_Wpe1PQPuFOufpg-P7xoufIaDtCMQmJ8UM5MY-P7_HblivitVlxL3VC7QF4hVr9N7mWIeb-ZVmCM4JFPOEWybuxr1meswRufkZ1ZN0OJc4PyYveCvdA8YOJ8wuIa8c0ZQAYRkfeu0oTDxGNMrJ1thAXHPsTlfaboAxvupCckctxgHY3qL7l6O9aEOjvC1vL8eXZ6dI6d66-0ShMlfALfwmw5yFwNzUhuxdteLOUQ112NkcfZABNNxLHYMYIgBaY0vtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJT5oSGD0Y1hGOtZtmJTUEEFFqEpImaC4jAIa_Uj1XrWc6Ko7h3gArG9zfIAkA_lqD9P94-X-wrNarg-MwunrbUkSt_yizprug0xxl3SVu3R9eMZcoJVIWVoP6OU5kU4IXlpFWNAzO2cYvUedBsukYzIW8l3uQCyoRABeQfL4H8slqo4mVuDQT53kD56rg_f8I4dGS47tE99dD8-Sidl_pDW0FsLsYq-ANLJNUM0p8y6pdllDYg_xbh4_xuGZBDNNNQZYk5Niq49y88s6dZU-CRQDwK1fkMqWd_F06ZS-Upw8yWNuc8KU82Hfv7VwlZ1Gtmia5BxBQpcyQZ1tP0dHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادوارهٔ شهدای غریب در اسارت خراسان شمالی، در بجنورد برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465936" target="_blank">📅 03:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع بیمارستانی در غزه:
بر اثر بمباران یک منزل مسکونی در غرب شهر غزه، ۵ تن از جمله یک دختربچه به شهادت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465935" target="_blank">📅 03:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3348161d28.mp4?token=rq8K4J7-m1BEJthXjzxloZ8E-7JvRmARkI4sLYmMJFscBL48b3aIyFK3tl3FEyPtvFe6rDCjLNWvRBXSUPeZywDHQS2QGAqchwTM-jfIMEaVEbw0Q9PqaLuEVorHYYN2mcTUkGgY6qFP_HZP5DDK85JWq884cThgptUZc8fiXLXpOvdO5Bf7Jse8Wi9VYFhfjeAh_qrkeAJFAoKhIw_WaBR50cbCwNeCRkbC8sVzgSNpVFh-oBJ_Gqry3r4eAp8KYGt0pejb6ZsAl9x9OtDwIeR03Dy_gOwlyptl39fMameYaY_XgwJt-HqLM8ReTOW1mmgoD_pFDbQZ7Iao3X3uHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3348161d28.mp4?token=rq8K4J7-m1BEJthXjzxloZ8E-7JvRmARkI4sLYmMJFscBL48b3aIyFK3tl3FEyPtvFe6rDCjLNWvRBXSUPeZywDHQS2QGAqchwTM-jfIMEaVEbw0Q9PqaLuEVorHYYN2mcTUkGgY6qFP_HZP5DDK85JWq884cThgptUZc8fiXLXpOvdO5Bf7Jse8Wi9VYFhfjeAh_qrkeAJFAoKhIw_WaBR50cbCwNeCRkbC8sVzgSNpVFh-oBJ_Gqry3r4eAp8KYGt0pejb6ZsAl9x9OtDwIeR03Dy_gOwlyptl39fMameYaY_XgwJt-HqLM8ReTOW1mmgoD_pFDbQZ7Iao3X3uHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه را از خودت بهتر بدان
🎙
استاد کافی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465934" target="_blank">📅 03:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8KILq1pXdVwgLK5XHcGswZmQvm9Uvbbdo6hQsIaLEoBLcOIhGqOnAfrwyneDKdUI3O4T1IdFylYZWDEdGprUFgW7hmzIdlc7Ml07dIyefsYN5SL-tmYDJaJrXAQzr0pEo8jNhZhdwXvBxbLll_5s-K29_NW-rJks94xqJNEL1RPEsxL_l9hnf7MrAez4KEpu2ifrVYkfW9zchR7IuqBYR9LYgw7EM7dASSUsjlLwPmjYC5W_Cn_Uuoo4WCyD4QWLT4V2bIoYrT2CDGq7jPD7FV6HC-t6mA2s03XxNKUIyNsrhXfD2jSnLF3j0pyN9oaUhw8_DJXN_idz5ifvzFxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از وقوع یک حادثهٔ امنیتی برای یک نفت‌کش در ۴ مایلی شرق سواحل عمان خبر داد.
🔹
گفته می‌شود این نفتکش از سمت چپ بدنه مورد اصابت پرتابهٔ ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465933" target="_blank">📅 02:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIxEo_7e1AoQfDcmhT0LTj-JLM621wpiz2TwC6O5DAc0ruOf77362wzN7hkgZTtSOuHaWqlau6ULxOGlNkZLh3Gnl4J_Xp1skdHbxZSemcG-TAj0kIThdctDd0VYBDvw9wkS9hF-7hGl6rocXongD_dMzyBrvxNxtVFztwVvvu9D1-W9u1N1v4SwVJqgUyV9_SwIYSusTpArNRKprDuYGFKBBA-th_9jr7fDXLnui7xT62M-Yr7bbP7CdYqX5juDj-ihsbNUQmG3JFWbqXy32P8dQ8AFZd20hOdwsc70QylCA4pad_qaTgdKuRoX66eOVTFbbO5jQIi3oR7_RJIYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به خلبان‌های متجاوز به خاک ایران مدال داد
🔹
آمریکا بار دیگر از نظامیانی که در عملیات علیه ایران مشارکت داشته‌اند تقدیر کرد.
🔹
این بار هفت خلبان جنگندهٔ اف-۲۲ رپتور به دلیل نقشی که در عملیات موسوم به «چکش نیمه‌شب» و حمله به تأسیسات هسته‌ای ایران در ژوئن ۲۰۲۵ داشتند، یکی از بالاترین نشان‌های نظامی این کشور را دریافت کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465932" target="_blank">📅 02:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کرهٔ‌شمالی پرتابه‌ای به سوی دریا شلیک کرد
🔹
کرهٔ‌شمالی بامداد شنبه در بحبوحهٔ افزایش تنش‌ها میان پیونگ‌یانگ و سئول یک پرتابهٔ نامشخص را به سمت آب‌های سواحل شرقی خود شلیک کرد.
🔹
ستاد مشترک نیروهای مسلح کرهٔ‌جنوبی اعلام کرد این پرتابه از خاک کره شمالی به سمت دریای شرقی شلیک شده است.
🔹
ارتش کرهٔ‌جنوبی هنوز اعلام نکرده است که پرتابهٔ شلیک‌شده یک موشک بالستیک بوده یا نوع دیگری از سلاح. مقام‌های نظامی این کشور هم جزئیات بیشتری دربارهٔ برد، مسیر پرواز و محل فرود احتمالی آن ارائه نکرده‌اند.
🔹
این شلیک در حالی انجام شده است که تنش‌ها میان دو کره افزایش یافته است. ماه گذشته، انفجار مین‌های زمینی در مرز دو کشور به زخمی شدن سه سرباز کرهٔ‌جنوبی منجر شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465931" target="_blank">📅 01:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کمک‌هزینهٔ ۴ میلیون تومانی برای متولدین ۱۴۰۵ و به‌بعد تهرانی
🔹
زاکانی، شهردار تهران: در راستای طرح حمایت مدیریت شهری از فرزندآوری، برای متولدین ۱۴۰۵ و بعد، کمک هزینهٔ ماهانه حدود ۳.۵ تا چهار میلیون تومانی در نظر گرفته شده است.
🔹
جزئیات این طرح و همچنین آمار دقیق مشمولان، به‌زودی اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465930" target="_blank">📅 01:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6ce17d3f.mp4?token=ItXsXpkMzjw8obPNfhb3_xlZaYzIRq9xTUUXiUvMlnWOW5bNN1DFE3X0XSiH5Jm286BZ_fdF2ZV3tghJ8swQL6D-4-AhfAAEBGz5MVysK_qwHXCCC_83wIIWUolxGNrKVmdcpC140lCrGeIPTkWZWAy9h1a6Xlk3YAhtl7KB4GhGZrCJx0o-P4O1eJsf5ZXPrUx1M190bbUy6KMelTAT2S5s7yhd8CsBj6q4SCjEte8zwx61d6aUwrMuHOJL4Ec4c2pU7pO2MO2SmPGee1GA6jE3Fw0n78z8HPxb6Nb7CDFbaST7utKETU-0cdfV2NKh26uf2A20Q_QOZTf-82iU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6ce17d3f.mp4?token=ItXsXpkMzjw8obPNfhb3_xlZaYzIRq9xTUUXiUvMlnWOW5bNN1DFE3X0XSiH5Jm286BZ_fdF2ZV3tghJ8swQL6D-4-AhfAAEBGz5MVysK_qwHXCCC_83wIIWUolxGNrKVmdcpC140lCrGeIPTkWZWAy9h1a6Xlk3YAhtl7KB4GhGZrCJx0o-P4O1eJsf5ZXPrUx1M190bbUy6KMelTAT2S5s7yhd8CsBj6q4SCjEte8zwx61d6aUwrMuHOJL4Ec4c2pU7pO2MO2SmPGee1GA6jE3Fw0n78z8HPxb6Nb7CDFbaST7utKETU-0cdfV2NKh26uf2A20Q_QOZTf-82iU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در محضر خانواده‌ کم‌سن‌ترین شهید سال‌های اخیر لبنان: پدر شهید نقل می‌کند که بعد از حادثه پیجرها، شهید اصرار داشته یک چشم و کلیه خودش را به رزمندگان مجروح اهدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465929" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465928">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یمن، اخراج نظامیان آمریکا را به ملت عراق تبریک گفت
🔹
مهدی المشاط، رئیس شورای عالی سیاسی یمن از اخراج نظامیان آمریکایی از عراق تحت عنوان
«دستاورد تاریخی بزرگ و پیروزی ملی»
یاد کرد.
🔹
او این مسئله را به ملت عراق تبریک گفت و تأکید کرد این دستاورد پس از بیش از دو دهه حمله، اشغالگری و سلطه‌طلبی، سرکوب ملت عراق، ایجاد تفرقه اتفاق افتاد.
‌
🔹
وی اخراج نظامیان آمریکایی را حاصل پایداری، مقاومت و فداکاری‌ ملت عراق دانست و گفت این مسئله، تاییدی بر حق این کشور در برخورداری از حاکمیت و استقلال است.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465928" target="_blank">📅 00:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465927">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465927" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465926">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۵</div>
</div>
<a href="https://t.me/farsna/465926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۴ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465926" target="_blank">📅 00:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465925">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7057a07fa.mp4?token=jb5CEyakwmo95ODW-EE931Lx_tXy-E607B34m2xsKT6dANRgdOzaH6ouMm2kIrEcjLkAC83n-FLK1JsvkhXkUwsG3oFPy99bDbcjbjisjb7kWmsVRkaO8jrk7ee8ql8-maRNH9_s_6Y_t84oyhZRIapD1I19xuCzyQQV6STlSTbt7myWHAUnw6aK4l1B5h4D--NJ1eywolivt8P4Ut8wqcj8xex1lsfKh1hGi32aLcXXR3GhMA96GZDTVH4fxpirFjdSc2RbCsy4h3uznPbQlzR4EsCWaPCTUD9tcOKw-lkELxn3BhSHJNrXeqUBJUZnypJGwCua3AD-TC9opuflUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7057a07fa.mp4?token=jb5CEyakwmo95ODW-EE931Lx_tXy-E607B34m2xsKT6dANRgdOzaH6ouMm2kIrEcjLkAC83n-FLK1JsvkhXkUwsG3oFPy99bDbcjbjisjb7kWmsVRkaO8jrk7ee8ql8-maRNH9_s_6Y_t84oyhZRIapD1I19xuCzyQQV6STlSTbt7myWHAUnw6aK4l1B5h4D--NJ1eywolivt8P4Ut8wqcj8xex1lsfKh1hGi32aLcXXR3GhMA96GZDTVH4fxpirFjdSc2RbCsy4h3uznPbQlzR4EsCWaPCTUD9tcOKw-lkELxn3BhSHJNrXeqUBJUZnypJGwCua3AD-TC9opuflUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در لبنان: زنان لبنانی به ما می‌گفتند «دل‌مان به قدرت شما ایرانی‌ها و ایران قرص است»
🔹
این حرف را از خانواده‌ای شنیدم که ۸ شهید داده بود، اما از اقتدار و آرامش مردم ایران می‌گفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465925" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465924">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بیانیهٔ مشترک آمریکا و متحدانش علیه ایران در سالگرد مکانیسم ماشه
🔸
آمریکا به‌همراه ۵۰ کشور متحدش به مناسبت سالگرد اجرایی‌شدن سازوکار موسوم به مکانیسم ماشه بیانیه‌ای مشترک صادر کردند.
🔹
در این بیانیه بدون اشاره به نقض عهد کشورهای غربی در برجام، مسئولیت بازگشت تحریم‌ها عمدتاً متوجه ایران دانسته شده و از کشورهای جهان خواسته شده است محدودیت‌های اعمال‌شده علیه تهران را اجرا کنند.
🔹
این بیانیه روز پنجشنبه، دوم اکتبر، از سوی مجموعه‌ای از کشورهای عضو «ابتکار امنیت مقابله با اشاعه» منتشر شد و آمریکا، انگلیس، فرانسه و آلمان از جمله امضاکنندگان آن بوده‌اند.
🔹
آمریکا و کشورهای همراه آن در بیانیهٔ جدید اعلام کرده‌اند که به اجرای محدودیت‌های بازگشته ادامه خواهند داد.
🔹
آن‌ها مشخصاً بر جلوگیری از انتقال تجهیزات، فناوری و موادی تأکید کرده‌اند که به گفتهٔ آن‌ها می‌تواند در فعالیت‌های هسته‌ای حساس، توسعهٔ سلاح‌های کشتار جمعی یا سامانه‌های حمل آن‌ها مورد استفاده قرار گیرد.
🔹
بیانیه همچنین از تحریم‌های آمریکا علیه ایران با عنوان
«عملیات طرد اقتصادی»
حمایت کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465924" target="_blank">📅 00:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465923">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمله به یک ابرنفتکش در ساحل آمریکا
🔸
اف‌بی‌آی و گارد ساحلی آمریکا در حال بررسی حملهٔ سایبری به یک ابرنفتکش در نزدیکی سواحل تگزاس هستند.
🔹
بر اساس این گزارش، نفوذ به سامانهٔ پیشرانهٔ این کشتی انجام شده است. هنوز مشخص نیست هکرها چه مدت به این سیستم دسترسی داشته‌اند و با استفاده از آن قادر به کنترل چه بخش‌هایی از کشتی بوده‌اند.
🔹
در گزارش‌های تکمیلی، نام این نفتکش VL Prosperity و زمان حمله ۷ اوت ۲۰۲۶ هنگام عبور از تنگهٔ جبل‌الطارق ذکر شده است.
🔹
برخی رسانه‌ها نیز مدعی شده‌اند هکرها در عملکرد موتور، سیستم خنک‌کننده و ناوبری کشتی اختلال ایجاد کرده‌اند؛ اما مقامات آمریکایی این جزئیات را رسماً تأیید نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465923" target="_blank">📅 00:20 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
