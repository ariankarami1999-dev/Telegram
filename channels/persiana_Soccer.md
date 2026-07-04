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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 371K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akvAmE3H-pdfeyY_1LhIbg7QDxDmMZ2riunh7LfzDz1qu3fWxvTnToRxQgylN1WS5oa8YMbS1MrhGkomezXKgZq2DYmrd8kvzuCVZoN2CInL6VKNXyptAPDEOR1CB2F6IwCtz1R2HkxkVYCM0CnKHnyjXNPCg0OCwFwLPUP1l4EcFZ9tfeXObtuDaOyI3pLYmiQe8WZwGbn-KK2q6SC1pW3r3sLqbgEWkF1bVGAWZEWmJKndM4txwi5I8CJrWHiakdMKEGoJVxn3A3CBfq-uK7rJm07haRjfl8VkMWItuyP0fGVwGuq2nDFP71X3gIxAIvlNTY7F0qHFf7YpwEofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCBLRZt8NZhnfrxj1bao49SdsmDSuCtXyjWQAtYPDVMAD0TfnFDtLnml-IEUnFVUM1D-lLYOur0wGoh0ekcnvvEaZ2G2l8oF2MGHbCoBQTSRxkGIIdHtmRTHqg9AoHtG4odME1YNkH7bV3utN0gLU8UR32ZtjYLhV_AT3U3F850Kh5D4tSW2PKoMo7lQ7tN95DFvO_Y7Mze_dqVjICXqnsCr34UK8UT1lHOWxMSq7CjHELwTRU9sm6B33zjvuDT_ICnezcr3BrSZIOOkfuakJKhXgSRPCedqn5WXDaRHgrB2n6_997m-gqyT0z_wS1kYyjcUhm7KC6U7_5mE1z-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOT3PEnKf11SOXOE7aWKqo37ZPSyFDkgLRPS5Iz3QHfHsN6TTHuegL5eNFEVfzoSCwn6QEQTOec_13I7PzX4TcjUs_wSkQB5uaIuSq0QOqF-brgDWoxq1-iibvI6YAxTuvazMHZCu0Vu_6ME2MdPuu2kZuzmt_7_5-9VsBoc7iHd8Ez59C-iO8r9HWHjC0xQrJZ_QZavZvYx5NgXNf9-gksCmTJjMqi3qTFo29OaoDVFH_nFT7WHHxawRuYoDtX8_hpJfzAottMcqixJRyWTbRhWiByhZUgcwJ3dbCDHvH5KDEEd4I7AsPI6N73mJhAQSqDQg_Zm1qKCmDkH1t6Fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83yXRAY30HV66FGWv_qtGw9hTdjcCd9IskvrY2OXc7KkpGg7sCm8evvbCNYqm5Fg1zfEtiL9dNpXzWY0ZNs8qA8mFzkcic35D9moWNFNkbtq_Qbwm9U27j841fnLSYX9bUF-sHtwBTgF-MvyBXN2Wlsbc5VUNP_2qfRCjmXUD1aFyZPLV5n7kOkeC-TqwblMPJuBFoSpGFkfbphaJEPWzJm88fzHgacVnvL1WtVHRXtOPgPMPm71UkbLzembMAOnk9UBjiP-A2hcgjvs59Tj2uPr1myZlKjVSR7DBxwA5R5eNfW6TQIR-l4nlIkS-ghMaYoVeP73skTLpjFzLTalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN75oZ5T0F-OObSMQgXqGLAWt-3jl1-egTT9c3egm252W8AAmyNXJZB-pXNam750UCfxXrLMuRcU-hZX-9OiWo-3w9DyJTjwrU0n3U_75-f3O2A59ThUIe_TKvLt-cSpMM_7YrZtj6CxXHd1pxCeltqK1hOk5p6oW__uOHFV_hgg3gMjAn8J185c_OqfoBYl7nhuGYYv3WJyP-VYlvU-5V7Tq5uWtERUXvdLOXWnEpKcssdzMSmV1iienWbc7Vpx6nBXAq0S2d_UpjywEMGcOkMbv-3zkxAZcKpWLy7dOjwC-ZzC1IQxfgUXrMBA-QC85DKzehuxEpWX-5-AALwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-WmUmdg286_cJooLu7PatmI6avX0lonYjxr-_t_35Tn73TXZkuUjAnEMdrSPgIJtSUFI3-J2mC9bMWJu0odXhxqjbA9r8bXOUH-5h16aTggo80FpqzOV0WVALqlI5_H8fWaehGA8ERLLMhn1asit6qlXBb4iN4xFmok_wqfpnYcg2MloEOxpPXsJuhiI7BZguPE4iwZUsy66nWqZhBZJFCpT43GAk9Ik3_69xwx04sxbAjCx1SitM0QW58AdPtL0ini3FdZL23SA23rC-Kan5kROgSMu7khayRr84x2acn8usw0fi6oksEMtaLWsTMboLYoVDu9NdaHvNhPkQcZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSo3WN7yzIfck_C1kuwYcswms7lJre8YEFYlAXloPOBzC5zRG1iWxxGPCCcc9WlRiPFrJNCv9zIG5sLSVUShjPZEnJSEShoea6vtahK6_fRAdxKwTfsIWIhGD4NS4MP5sC1JbxEeKZIdccJ-tRuLF2JfC8P4P6_spc6XOxUJSsR6-Uv-pXuaULyLIdC6Whus7sGvPlNidqZ61809GnqaGCQNN0A7KVIfMbxUv2ctglDtXQia-yG-zr_hkZecfZCtHAyaB5itGos2hUmOVDT-uS2oicD6EfH2Cl9T1SFfoTIM_BOft0owechezM8yUixpapvgFBdYMFarNNq43VxZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRZmIF_azQyJHTdKoqBTG-MhOAH2x3Ip7_CiRc6rTmZsZqEXp3X5BufR8oQHlnVb1ObC0Ri2hCUtnicdUlvKONVeKvB2I8P3RphPgJe_DuM-qxpBVktuS6QoBFUCbxOQPaltvR9yOQFzizm4nM7cuDrTCOn3ESC_A_ZRNHIrAUOoFKv7jbAug1Skoghb4ZgrANsIaHgmCB_da7Rd7wZbZBr-v12GZBKVCy3MOvfzTZz76w_V83S7whPmrT3N2VcBvYu1NeE3ZAjOk9U9Mgi31fGcUNk7x3UvNJ610EC9_4Bpc4HevTBwX4qV6mB-8R4LXfGPs6DigV7Exp0G3HY5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W2fbCdtVi_3z_hNqijYBJ0x-jcvakUkEZDxAJwbo1zWuvh4iWagIsB_LyBZskq4WqL9fIxJLsXRoek0dqRJyXAPogf9EqScR3Xw5Ei2BwGhhbx5skO9FB_gRRRaMHNCHgl-aAONiNixLSFyUGIMB5ZRfC2_jc5xxBohFb4y-KiWsCbHF8to5K3CvIvOS8CPeo6UZtoMpkVRzfZWJFLhBF5mnlasYo6UNOy8aa0jpIaJ8hV4j2OVkFALftDfP-e_UFpE8N2kgymcuv7WWKl7TkvDVhzUBf9PpvvRPLNvGWdJFhTxaj3zOcLjtQN03Y1WpwgToIHuM90DTrx2EG1lk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qi-GHpMTiiZPufGI53Bv6TUpSFs82DUrBRO0XCYhE3c9IrBH7jCmwfo7KvMu9aYoJAcvf2VI9TQKpI-Wc1wKZC5a4v8IsDClIMFCglKTcHoWSPs0QElniR-_PL_FOIu06WO85bNO6Nve0Fx9AnTVZwRcRAGISPOAiR_cShH1ejCyxyFs838yHKBGCu_DTXkAcqSOIhLwOXMhPqY8ZZI2QzCZ0lqzoZNRRdVDf71dwl7zhQfYNynn-qwuZp7hPJZrmTAZWKOQvWUKNwvrr19zQOjoDKrKYMI44Do7zehyh4JlEfSjrH6hbOBuhUY_Uk9_rnh07Dbld3w8ojSl4m3-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiFvRmKeWyQgBLnI1lNS0hDBC9e70ZRehfoNfDXL04PILZjZTNeO1owBRCumuzq_e4LkYKV1kB1mzjY9g9nov-tfjG2gnMqhMVfEntzX1Ow1tMLiWXICvjYf5blT0qnwjLga3F4mllxNhdb2Degt8KRVXTkUKtjCP16BBVX8FKfKvg5QbzOdUn1fmMo23UvHjabW974OiWWhUzyV_fp05X3QP84vEsR6EJF3JvWxWVDqD2jaNzO-j_Rs2lIC3cfGggWi87bHnVNYVbeZIMVn8ezOTtmYnj9VMvyPV8RyC00I4TfPJ2lJY9WD1mZNvSnLsL2mHbeKfWAnZcEBwilGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2N_ALIaREpI9Reso6DdYLfF3Zoyh1sx8a5ZDNBYw95zYVE6Wld_coCu9bm1ozsM1-tkrNvi67OgeF5Ih_UzxLsxdURqPWwNUYQq_imO02tZ_RKsFJc27A_-vSRKr7-B7YqnjBRqyxQLlLOF6mXzylgt3A336r_R4dWPv0R7MzBYIzRf8FlyoFyD8Ju2Jr5FvAf235AHYbqWCe78jyccguSbA5JL6FetSg5cWsVPC-krKe1Oe4YyIYL7lZcZLinOEikTEHjBeX9a2P8oa1BjhPNAGM5OE2hcA76xll2BIQfGX5FhwzI8fMEuCVFP0gD1RIBAbuN21rxdEySOh7uGAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X95lNE9XAi5rEKb4qmYoGbKQA4ARj3mfybwEm8Me86ulCoLvz1t5EKrkv_NkavP6j1N-m6oRm7nzd2vfeAZCKKbn4WdIV1RtlqIUKudcddxUfbMFhsFLWJDJABxS286fVsqqSV7ngTQLOTD97LQzE3sWtsI7Tu2oJ2NXpvOwrfwPhOKYzOKu1M-4QNS2OtMO5fZ9LfHjdMBjZTOu14FxLv7ltz02nDRJl3kfX13FH9zpX96-S72k-vCXCKMydZKNxxbTYCTDGBuBYXoO6kG0tXlwoIVlMMZH0HLKpOeEdnjQr7F6LEe5D0CjqmeWTnDqiyy93sahPS3CD1qaUX7Xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTMByOO5YS1stfeqwMDZSQn7ySyd0YPAMe019LUMUibkL2-SW77IkeyI2XFDXLgOrmI4Uz8qDVpI1hJNdzBRODw3QdkeBwcpP-ZOKgR064q2UGYh97HMYt7yJpZCAWalHii753tgKvyOYTD4u4t4zFloQNyzjZJ0JlpVyfxuX56qYEahW-zj9eZK2hmicKoDJ0RJjihbK7SEl9_R80rtiqL6aqRuRr9UjaEZvnLTRMRdBfVkVz8TP0Dq_Ddpj118wsyk1OJPtRR8VnECY4--08DUz1GbcgXmj8TwgXnSeQQiTTA2mY0UjlzXc4MNMgQu0FyktSKqAZ4HV0PPqCt5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAttYyzcemLm3v_pEcc6UNReIuyL4F4CDOF7aoRfxd1H1BMacduRm9BXoBxmAVvp0A_C8tfN-w4y08yRcTUaUkOfaEMOys7vhcNc7NoKidP3NdJNXRgqJxBio-rGJ_tPZICnZu1u2A9IlJs1EWSDFaFtWEU4tUr_MnjtQumgetzm2pppuFoq9bgfF-rRYFdiGgeCu2ckAGm5tbqzZ8diniWT6P5_asRKbW7nEVBJZZ6endey4wCspnCjt8fz8viZKPco1n6vf2iEk137clgKiUnWIFCXzuz1uaD1m50jvO0amoIREH3W2mATcpNHlwJPI_DPwZZU_WwUH280wFJHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHk6PFw0yfDNcwTmfVZKukh0KUcQhkS8V0jYZRhgCYRJPW8r6ZzO2c4uLb2m7szm8LcRDoNKqk6_g_fJk57Lla_J7wn2fmoTJstZSmeZBAypIiQlCFVpQCY4KHAtOXUDHBFTHtd_ekCtaaMgFwNtVhyouCWeiI-rgl0C9MLvxWUt9Kj9TFZ7Rxe3AkSAs7-cyKiS15LJ0C8v5jgjJOli4EtFtJKU5I_jptdhZGS7SDXD74FZ8hL_1nQUmZSN8iiYrrHsMojMu3lA7WQEZ51UglbvmvcFo2UiEN4zRo5rFwS4VtF6qdHBOjQlCEsIMQSFoRa43bjT9B40ISa9ecLRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqu4B9GErd0PrYGlkmh70zpJI6SV5gFBVX6R72DbdGqWjuo37yZdSBVK5WVi3dq4OFYkMJ0zRQZkkzdSoB-eRgcbG0aunj_T_PHMJ8SDYly2IV3wjVdU6J7juGE0X-hP7E-VOsWJbF-He0t-yuu1fsWrxaeUHOsiu5zQMIxj9bE7C34j5tM0fvscsDSnjRys_DHVV0mgTTBQhr72WhnbHvQr_B1DXH-SDoF060uEIeeRYx4WWjHqxNv1h7MVFzPNnc7q8xljXmxZk88O_k6nT2b4lMfktA8yonYvB79SSyJBze4euOnaDbBMxnkH1UG-MseakQNsDY3zZQKLXJE-PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiM0iZARqpSPZX05koXBE701w35N9uoqYcbWxOyhULCLAmvbwZDzWM0Tv1UDRLoGx7fRP0chSWEd2sdCrACeRB_IWzVCrqSUgDMUKWhuHNPMvwreMvzhndba_Xu5w3V-FVs8hfmVjMJC3i3pYR18LTQdaRO_hnlvayiuo31H_A7Gg6r0t1D2EHRx41TE2KoVTriYbp7e6Ka4E0oaOReIU-VCOOQgapeCtJDH3m9gHyF5tdEQ7OWdfXVfmTsWBWZaCRwMLZL8utYo2Heuwaea2iVlguvS-1Vs-xN0ztLPRwWEVu6Tbv8f5SDFOn4UARHxVdQZGehRFTXfsGoUGwjXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B18kpB3j-AcFarNIzL9sN7GfCsXK2qPkzFf0zrTLfx5LHkUKwr7LjeiqqWkvCZuL9rZrpuY-zQn6oR_vfuQrLNAjpC9Qq9Ydl4KhWjFfqQPvyYU6SkZdLEgiEr2vWSHqQRx4kOkJy0h7EoUxwmLzmCSuq5ghcinhUdBAGUyuNsfb-KwkawQB73LKwtpDypEGohWgUM0oerZ_olUIujDCxLCSAgdZkICDN1bXKPENDrDy2mplKHMiAJGa9f8aF0Q3s_j4KMe3B-XhCLWTHOhxW0-qJoK8OkNW1DRMSZgeqUC7zuLgEDryJWIOkjDlE0owUts7SFzEEKO1nt1Z23S9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=A0NLCteqOn_IfyFv5j9wKPvDV9NnCGgJr8klG2AucM85wDCYUbRvjOFelUzq5aWKpYmQud5fJBl9Ub0N_91QJDS8ITvphv4P0pdqRZcoNnEjNLAehjZaHOfz4SfKv4K_YfMOA_n36qQlIesT7Ob5BViUXFri066LMcWJCro-FaRjNS1mtWUoAJHZVQD9_SX6LtUdPMd8OosiHKiXg8tqf9CmBX18AZMlxQewx2wug5RNbMU--c1EIVyCPxUYApyZFPttLAXTUVWLVXD3B8rGXKgD0zSButQeMlcM6uJy8WVkiuvVl7JplX8iyovR2CiGsa1talE1wbt2rjHGzqKL-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=A0NLCteqOn_IfyFv5j9wKPvDV9NnCGgJr8klG2AucM85wDCYUbRvjOFelUzq5aWKpYmQud5fJBl9Ub0N_91QJDS8ITvphv4P0pdqRZcoNnEjNLAehjZaHOfz4SfKv4K_YfMOA_n36qQlIesT7Ob5BViUXFri066LMcWJCro-FaRjNS1mtWUoAJHZVQD9_SX6LtUdPMd8OosiHKiXg8tqf9CmBX18AZMlxQewx2wug5RNbMU--c1EIVyCPxUYApyZFPttLAXTUVWLVXD3B8rGXKgD0zSButQeMlcM6uJy8WVkiuvVl7JplX8iyovR2CiGsa1talE1wbt2rjHGzqKL-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbvUgXO0fLhY2E6QACO4B_Jg81ZGtBKEQLYWEXYxzNOFINkZVxzyMXcNNILivNP5vui4t9I2Iw2hQ8z7ChiM0yYCFUNajIXLej7a7qgezcI0q0ECFhJcH_xJLthjihe31t8gGKm5p1aPqHrYuDK4d8eO2kTRWZtjJkSIQFJ5WAdeMyqsYIttCs9pefxm4TFsh2AbqcH2LCGDxZ_TtrgDWVkoeWyufiv7lCFX5i01ANZOcYVpOAQyy1ImQN_9O2Sog0uF7E81c3vgnjz74BdxUy7eoTgwSk78PFARJt6yQsXuRxBigk8NbrM2YxwpyqLMwL9n51-utq51otAQIaccQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOqQzxaJBXPGcD60hSqHaS-6jUY630Gx860PyS1kEDg0KasSARwLNWewHm0RgH6Nu6f3HApHrb03oUkf95YfDlyo_MRqIt5L_77zoBzEDkEYMaVTPHZCUuOh09f0Kc0yvMx1s3ZMVgKf8o7s0C2MW7fMs4qciuavFENakloh2ARqtRvTqkzgEKetwE8eEetX9XQP3-HtEkxI9Ar94mO6paol5qTLc7CwjnbvVXPH3aeTSszb-miYOn9GVstEJ4uqrqpILXDUZp-KYh0KD629AdH5pCVQ4V-IjdDPoTWho8UKq1jJIS8mWnhy1k2eer6MCq9KHJ9Jjpklo8AEyKJsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=iRAxZD7y-Fi56Ja_YtAn6WyRRjiU_0ZuDRDwatgCAVHI-oJwJzDerEvXHe-xr_w2S4xd_cmkQgK8L5E1Qdh2JkmBP8_lKXfOJn6rlvWH6URXQ8njjliQue-RNUeTMb01StcOancjUkMBfjsVrZmq3Q_r6P-TLuQpPe2TAFhMINEz49qldj7Pqmuyven-N-mTzywIWBL4WMWPs8oq-ApdXge_sO5rHiYNDR9X7R-CUE7OoXqofCHtEe_rP7GcYZ0mQsaEUIKzInAVv0unzSx69DrHWFub26sqwduHNzhTbcdK3ba6K4TxEpn8DQQ3QX0AX3hHg6rdVOV_YAgGdv_98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=iRAxZD7y-Fi56Ja_YtAn6WyRRjiU_0ZuDRDwatgCAVHI-oJwJzDerEvXHe-xr_w2S4xd_cmkQgK8L5E1Qdh2JkmBP8_lKXfOJn6rlvWH6URXQ8njjliQue-RNUeTMb01StcOancjUkMBfjsVrZmq3Q_r6P-TLuQpPe2TAFhMINEz49qldj7Pqmuyven-N-mTzywIWBL4WMWPs8oq-ApdXge_sO5rHiYNDR9X7R-CUE7OoXqofCHtEe_rP7GcYZ0mQsaEUIKzInAVv0unzSx69DrHWFub26sqwduHNzhTbcdK3ba6K4TxEpn8DQQ3QX0AX3hHg6rdVOV_YAgGdv_98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNAJXz2hqoXiS1qkqwnVSMBnczA16ERSS8JB5gPg6bcaTrgy4IIE5ZRhXg8IyewA0AmVu1LLsFoSICTkRz88x7QyVBI-ml1eWDE6OalpxYBXVDcgftArR1c8oB0PX_gfnzwDPwDsq6ogYv8BWTTN2H7MJMJrJOsYkyqz6Llb5Kg4v2CB6BDy2wr-madursF3n7ZkqgY4Qwkfjs-ccfLciJtFBInpthhSYyT7OeO9ljtbiT86jUMs0_Rl9oSQvDnytBNyTjdqmUQaRVm-Xc-fCieBuu9qNmL8ls8d91hn2OV2hKmuBic1txguqEdyLh6vvuGv3RbmR_GiFDqFjdI5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWtgbsUWLPGhmEwyCYe5MbLk9hgPzXyNL6xgCv_3BvJse1fNAv2UE2-Qlqtp9xrVFP4qdZk640OJTdwkVItZbcnYLQqni8u1AofKJueR4MUxhMKWNbMDzKAS_H5SeYHXmQUYrdG6a774rTBT1H7UFPkXKxMzJfc7uqSNShtZtB6hmRJNseq5LHp9sTA95YgHo-Zh57_5oujWM8jEzmjKiu8bT-Wt62hiz8NTXjSyIPU8KA0qxa7TVSEgmWhiH2PMJCYEqGn4jG85amui9MSJGCDbrPeBsRgE_uzdDFq2C3qVX-9_udnITebAL-oWzquiJmJYQXDDKElIA4zxAZPxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olwBaR7srlb0vlwExWUzhMIBtzgU-lCoaJjPkTYveJVpMRlkFQqsGJOxbPc8yxuiBvfjrNlFUkQDvowp-5jMRPduVoqVmD21m6TYlGh_W_mmVnVfCbRyrXX0IGxup7Z1xrnAKhGWuH-bRs7-BChTwSyDUCWtk0rqsgg57l_XOjiJVXDAe8kDJtBH1ftqPTfPAp0YIQc1Cn69xbhdM1tRtjMF56ySd0AreEXdpeD1hDmgjgGKtEGqsjXcyuXzyHlDNHUk_pMFLWAEtE6o2is9XzU7A5dXFJ0MPxxYCJKB_iuFCi4IR3PmheZWQnm2xzh8Sm_jNJO4-aEWJkUjizPCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdpNHKsk1sFlnbS_HeaiSquNubF2LyRRPFca4xe9LOVZc-_KTkYJtS1z9KF_JKUyCpq_CmG_tPSghCtRus4VxPw6h3aejAA3rICtlGbwNMH52b5JxJYn6hdGWpwXu_339nftpgzeyicDhOgT5e1J_JJYkJwHp3l2bkFpWEulAhwR40UiYAouDQHnKgBE6fv63DR33vF62Q60KAV--SosrQR-Kj10aX9VUV9TgapmV0ZWLFkqp8I7XVvBxQoUJ-pEK6jozMo7bAfuDHlVHxkH_YK_3mbIOM6F4D_BGzBVTT6hEQHZCPH0zF09F9iy8_oosEcqgCNlX4bThRmcC2L-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2V0yQ1xjwXfMm1-SYqoAzlUQgQO1i0QikdhxcFRR6tAkZWAv5Bxe1viCymM-ewAQ8Sdsi0lNf-uQ6Kbd34k1BWnJ488CmK2pLSf_HpCAdeNZANQPLriPb0xLglmFiJq55RUzwh12UYHNB7zmeo7aSGR7DMEWzpOw-FTJvL5GGU-pZ70jD8zrFSnnabJMiUVhpmfTyzGuEpNipp0Nia64OphgpKVRGu14UKcOl55gcfFdVdw4AJOx9IIi-IAf23yOsPMUWaoJz9wwrx_3B8kju5i5NDpsu-EC3rAI82_dQsDcoX4PwfuXoTZYHiVJyyExR6Mq1BvSkaVB00NuqZJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=f8uaWOjVJRd49mlayFKkOEsUf5tJnO0CI07uvHHhENvGS5PGXOCenhaYt9jaWaxmVwcSZ8qBm5NjSPV0UXqPkmfB_susVn04auMthY4gXqCLBQ2BHWkbvzmosaQGZhGc4hAYYlTemF5U2KxpcXs73jolJne-2qMlDBbfavBMrRGLFhWy-2-4v6SA3e72jiQmaSVn_qcgpsRSR8tNpjizr83-wI7K8bw7kHB90Nkkmw1G22iXM3w8uvUreIf5wCDEljfVeig64jVxL8rZxwJZ6tYhSniTgOrkq148jpN_1Dtf0T4PhC5JGoVeSsBeSkvaLFJr2y5-tIUao-DFkC1kkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=f8uaWOjVJRd49mlayFKkOEsUf5tJnO0CI07uvHHhENvGS5PGXOCenhaYt9jaWaxmVwcSZ8qBm5NjSPV0UXqPkmfB_susVn04auMthY4gXqCLBQ2BHWkbvzmosaQGZhGc4hAYYlTemF5U2KxpcXs73jolJne-2qMlDBbfavBMrRGLFhWy-2-4v6SA3e72jiQmaSVn_qcgpsRSR8tNpjizr83-wI7K8bw7kHB90Nkkmw1G22iXM3w8uvUreIf5wCDEljfVeig64jVxL8rZxwJZ6tYhSniTgOrkq148jpN_1Dtf0T4PhC5JGoVeSsBeSkvaLFJr2y5-tIUao-DFkC1kkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8ljiyL4-H-OJz16urBddeQ27rRtfjG59vXbn_L22YnsOfA1YtGSkki50fn8kpivJ0vUHqromadIttasrbvX2_Bq5bKkUpxQcSYkpVGlYuPMLU1jGFBKmt_K4DMqYN3UjVh72_l76XpxkL-5iA9HDdxeTA1l165BWthw768WPdTz5AouC-ZdJWvzoKxwOttp8hp8KIRaTueB7Bu-jKwtgQccXrkvsYt2quAdWFnMeQ3gyvR1bPeOGfIsxxvngjF42Ern3K9t93nAuSBGNBkrwHMqcf0BxGJkj4r18Sjwo79pr43WZM-WTEcP1-f3tigG6bYCPZGCCXorPyVFLnUGYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0mU0pq3TzqJ_5AcCeYQ9WDyohW5OkO8SVlrnJ65YlVs2loP6f2j_k0hn3O6_rcMZmq7ZTYsvyU6Xu5uBfrKJeKLCtw3039FYkFzZ363o3BgPkA94qnd10lrvZnCm9SJpouEAqdloghKojLbMDCYG_q9IVxSn2gvdkSnmltTD2OaSTsjoDIJaGEtSI7ypHchH3QXbK7cgDQt1KA4FEK7fmDwpzUj_hR2cAJNAgh0-vsImyVlvuzVorfUuEGMrd_LG-MT2zDxny3-Ya7jIgdMJTIhmrDBqwnFGg0q0k8a0sVpJtB0YQ-EnqwaactzCiIBUjA852OpsjXYxzyR-iO_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzBXQ9O1YAo_YV48FL7QRpi-RbWIBOHkiwKe0qJb9A8DETeRGmJzzOb-oUTx3k-U8UX9BeFtM21wG0LslpgtOmof4AmIjRyA2aCJkLYJoQQ3FqQShttrviwgIjC26uSlL7ex0CaHUKx6N8hUOBke08qnqicCLfuRMoMOYDZ225YZpSpKyo4zDVRTSV7dXENkDxKPzbAA__jPsGlXKJr-uXLvk73uz1qxDGpRh-jYb-4cN_I9CywcETVkpJvMCsQpXxaPX7Leo8bzhItptQG48QljygxNa2aAAFGjYSoCZMpygjECAtK_JxNw0aSw262zGD0qDc4xaUQDmwSGFdUemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUuD5ujXtMgn0_rJIPp4VXN41BjLGT-wWr0vUmNX7Qm8rCxzNwX3rtrXVq0hd-T4CM6DfM8aCLjlRRmCmcmD2lMpiGyjnpit8NNR35ABACM2rtZyUDYVqt-k6NH_Tt8AB--CnnSb0maGJg_-lJ7aEIc9z5-884eZfB6C-UcHnksRQ_9CGLNHBVOUdVeL590J7GTM5Tnkx3WxcCsfysBpEBnZRJCkU7uokxuonKkA4uTQ_vAEc5ftocMdmKJniq3FMvWkXkbznwHcBmaJkCfH7-Cbtmddf6pRJqbzHOjswL5S4yIkh0FEF67uIA1C_sz9wOypcnNAb0Op1vkwFVVFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuA9ZgH8oqRAzBquvROC94rDTYUGiY2cAt8nMHvpQUIODKbQQb1H9SC6KP2fG8D19J_0saHwi8CIUbUIBfOq4eYD5opqNX51WPzMX5X-H5Hwx3x-Rwukian4JfkxuE21BriaCbkngGpQTMgrJfWox2_fjEb8HDk-5HtBjwFD4YxIlCBljHpcgr_vmmKhMSFUte7nUV3uWGUlSVL-T9Svzy29xene8YYxnDtfCz6QJmx4Fi191lqkuYhQ_a9bBpvh9aha-dgi_hi6AKJGy_MK95iqwtgDJBETCadRWadfBdljFTKCRW0VVT9CX-Kvr1Qm3IaqllAtN0_2d7hVd04ruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riap1xPqInHKn-UhDKbP2I3XnmDqoAXQeQRAPwOSE_ensMxFJQ4-q9YFVh7fFs1B_mQaZEvYHPTp7iZ2cJ4-ZkrkfYD2iDCzRqxqpwoo9szs9Drzx1aksH7MEmikH9g2Bjuboe2uPFqVd0h5OMin45B_OK5i3NT0g3lHIZb2-iH1YRyIDslSOcpLaKHhBT1BVjtnbyAhrNavzjKPuEjiJbfBF2JrmGxN-CXjkH0vckyBvfDU7QqmDcWphsR1FBRLEfPx3OrfsIgL_O-Z_hj-MvKX1LpJFU_9AYzHwJROxm7331tgVSWRa3i5vtnz8xffbmjOkZchEBWYOYfYIKscKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=mzEw4JpkHQ53bPbDsvOzUCpiji1NszsU_-7R2y5F5bVtO_LlXXNcrQEa1PgUxnoo-5E8m2TsptMIiRWB1vYTSog2WiJZTHn6AQwEFZcoWZKZkWGFWYJkYaBm0X97lzq611Qs7K11mEZWLMrdapwd1IWzrBGTVw5qo8ftgWP1DDDq6KFbsQuOZ1HayPqqm1itTtSHIxfYMKnXk6w7W3AIsnYknOC8N5ZQS3rqNnUtBH817JHrZmCoXZ2uhgUveIIlwXzueVeRRL_d7JnIdLkY-JyLoSLyrNfoNpIiDIEFg8y2CobBgNmCTguZuLGNNQlMEkd-r3kDmuNC5-2F4ImgJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=mzEw4JpkHQ53bPbDsvOzUCpiji1NszsU_-7R2y5F5bVtO_LlXXNcrQEa1PgUxnoo-5E8m2TsptMIiRWB1vYTSog2WiJZTHn6AQwEFZcoWZKZkWGFWYJkYaBm0X97lzq611Qs7K11mEZWLMrdapwd1IWzrBGTVw5qo8ftgWP1DDDq6KFbsQuOZ1HayPqqm1itTtSHIxfYMKnXk6w7W3AIsnYknOC8N5ZQS3rqNnUtBH817JHrZmCoXZ2uhgUveIIlwXzueVeRRL_d7JnIdLkY-JyLoSLyrNfoNpIiDIEFg8y2CobBgNmCTguZuLGNNQlMEkd-r3kDmuNC5-2F4ImgJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn1_2s5SiXcurKDPB6viSmyyAe987kg7kkaXTGuS8vmo8rlqBqCZ6TnT7jFvhjSVoORGlfX7hENEZDibPxoifpzZBw_Bqke0ufZ6TWe8tYHV0QNJX-lPzB8f-Kt9UWubS1yDm1g1kzkTrUL_wPGxFVONZaHJyYFtkVi-VFOXgO56bsmR5e_ewy8ccaP3jDrZntJyzzj54bq-q3IJ2h5beu9rOQMXwlys9h9AZWAldzNHd-msnETKIacLNF8_Jsp-3C_BPCvvXElj46C04c9kEqGzEVYGyUcNqmB64uNZNimrUuJWzMAd6AK9sPx1dNfNjKMQrORDY_UUp6zRcittsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWhQu88Gy_2VGyy0Yu-8xbLxTFnuphQCX98Fczt4I-VsnHLCJSMlMOLl9Xb5L3PnPb_DxyjSDG2oeCsJiC061rE7BdqkTxBbHZq6xx3JYpEFcPqmAggpmuLKIx29pwO831LYig02ACfUD_lfivzDyoFrkXyuXWJ3yihjqxvaBYKAcOni6gO3mC63Id50T__MlWqa4RNu-bdHPM_4Gl9T25MxZwED877_MN-w_ParIT0_IZ5shdi2US3WXsQ54STE-6mdDF_sqvP1B_U3HfLgCa05m6OgLWPZMsalHH1KsCynShcbUJHKnPiPhkLrHNikmHjH-oSmzWWiJ3MwbLckGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWkejD83jtKKvZLmMqvvdRvbBCYGUGmb51cL0ovKIcEa1TvTBotvbwjQyXXhLYrS3cIpe_7Aam9xMqOIg28p_vXVcb2763s6ZEbQGIVTi4ZDtDLIyfWFbSHrQYrSvzCiyX7FwIC9yKr0ecavpXEinhGip0JuIbrPIB0Wp2dHS-IGGgZvPhmx2bnW6KZO9ic6Baq-kmgF03kf9g4RwcmB8QcOilsOkYvn8iSo2qHlCFKsT7ezlvNZZmLTtnHMUVFYBBiMg-vBmxxB09XBf_AUPne8fgCzG-pq6pWnK-3Zi82lEP_QnmhqCHaqJDYSi10wns2XSbEYGhOIISJ_41riWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb7xVjDSth_GGT8CHFm309Wwv4_5Z-DpYn_x8xW6bH2LzaSm8RZNmyI0_9sy8zQt9fSQBGIMAhDx0TfTRfoaExcqGSEvwRvonn1AeToWuqy4NY61RH3mzb9a4G1wRmbgLLQHcPxKHOyD6rlqWLOBtHLceAzRvg7BJNZVizmnyAiQIlI1n7hdmnHWhVCDYywTrxzojeZbR0eLaTGGnl_5-vbIqXuTlUg6hUYHD8iK2U3jtuNGoBDSDKRJW1cbBktx6L21ZOmoF0k2N-l_4GsPjgSaKedOcr44W1kru9x_nnBErK5JMuQgulLpfbrGwugmOzNV5Xa0n5sGDhkNaPBJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbFtVrCy27O5Tnt4cHpx-86jpCSdrzqvdwcMnTGYPP4ZpX0TjT1-4X7we_6ENdhWygxSxXH5rvDo_nfSWPyqQpQ1AiDrrnq3J8zG_7AZZGAINRClQ0W3g0YrIcm0HGfz7h17dukfFgBxyX9AOHL1aKmLUU21rkGGRHGtCJqa00pOVl-xoWiR42xrCD7n2JbnaMEWweOr59_fPnPfRPKYs6U1UuLMMLiYIebwK-xZBBWuGmtCjaPKvJyRpM06pN5psqSYgFjTSDBfn4biPpfGqktbKo9JHMg4U2OjrFqxKPt0bkrJCgXRAFJJgJ9dyHpuYFqzJp9fkxnf7yEqnBrP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P51Dzd5qkAhe_fYP1hzWedTTY3Orc5LwuoGA2DuH5DJd1598Spw7dyD1CYgXbW-1bIFqpZzZmeGwFlf26ntSbeA7e4NFRXEM6ymEi__Pc6mX1xFiNoZxvpMqxzcEdki0cONkWhvOWmdrBnbFQMoTMT9JwAT_NL5hmtTjzA_I4UMitksX9yp1VuUbADVpXvxq0GEZLJoOaYZlRWQWi_SHBqS4Ds0bTKdu6TYq7HU6-B_iKhOfBZxNkXAUyJnnR7qZce2st9xqLee02E66tXewqsSaEiQ99RTiaLreKQ3W5EwIRw4eQ4g5427tFbgM5eAiE1AULIoNfNf3-QIc36Pn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGTfamVkwgHshHynfhn4d9XoRqqjLt_XC2Yq1rarimCKe60Ea8wNnx67ICpfYn_YgDeYlUNGwuKRwb_mqFSxi6AUAppSNY5ke9pOUFffyqTMn_6-ffJ7SwOoIfp84PrhYSzyqRLOzhcipeZpxVAaC6z5T_l84AqkI8dkBSC--mUTiH31Bu0Q6pRxPHpEcG35gFWyYREeNFv0HiX1Awr-X6U9CDVH-4v-j4z54Nge99Esxx6Sd3OisJlwgJPpa7ro2SH7hiBB9mi-UTfAJn-Kb6i8cQIk4RW1Mgh4hHzLzOKvlc9QMYaM_4O-WqeM9jqMW2d67VTbOenWooS3zWDzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqy9WSEXHTAHvYV2fdWhh8PdH1jJ1NGJBgmATI0ey8HRIz-2_QwjkGCzUrNQhEHZRrShVfPqZzslUlYNf5i8GbYAnzOcfvZjJYaVBbXndGD5Xfo6idoaDEkRbsOEOEQMSuJ3e47n0iy_ct735MVNf3o4ZWc7J4DT9r1mXMBByUZG_y4rsKbGOMHLrUYU-c7YiTL-LXHijSZbEOAJbRyJvBFacrQ3C-zXEWo8wozzy0n_3-uBQT1ZZjzZ1wHZ4gEvoc4uL_keD4A21zNemsZiRxx1_ZHCYhPF3svgFeRTlH03azwuV_1aEV6EUEyUcVR7YUJ8xnA7JI1gX8OOB-gp_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=pHG3c2kYSdH_AoFmk-fP5Ye63tZq5rPRBZQW7vrKq3eTq0WELxqbyUm5Jb4v_iDJnNqYaOL7XJaYkwi3hXUf5f_I_b1GdUqN5NLAkMSm_4nJCjAjNu1asbh0F3pOjl6a6bfuFTBcoL3fClyN_8qjyXIJYMm9QSshWG2ureJwCxpA8GyEvrufLIq1wuGpsY4ewoMJ3i3OEOuP-4lfX6KkOKglYT1Gi-JrbO-Jd1YdCcGlaxWklU7HKzSoTgtSF8pkWykRvzpoNCfckrIqQbxI7r5DlOucoqOUSL9MZonYLUJWs3IyXeYSmCVveT5IGlINP-PFwKJNPQ_rRCVAAJe41A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=pHG3c2kYSdH_AoFmk-fP5Ye63tZq5rPRBZQW7vrKq3eTq0WELxqbyUm5Jb4v_iDJnNqYaOL7XJaYkwi3hXUf5f_I_b1GdUqN5NLAkMSm_4nJCjAjNu1asbh0F3pOjl6a6bfuFTBcoL3fClyN_8qjyXIJYMm9QSshWG2ureJwCxpA8GyEvrufLIq1wuGpsY4ewoMJ3i3OEOuP-4lfX6KkOKglYT1Gi-JrbO-Jd1YdCcGlaxWklU7HKzSoTgtSF8pkWykRvzpoNCfckrIqQbxI7r5DlOucoqOUSL9MZonYLUJWs3IyXeYSmCVveT5IGlINP-PFwKJNPQ_rRCVAAJe41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT4dyR3ZEJPHcyoR4nwo1nm_HHgcMbnwAc0oUzimXXF-Am-06EUrYIuSUuEgIbUc-LR5miY5GQ4v067b0B1L2_3sC2kxW8u4PXIQlssVCaufvWiDeHRZTFq5Lxmpkrinr8IUex5vIPhBJ9xlKMkQAB20gmCtVhN3DYv_uXAFHwPaexVHRkGK-CNX-7UL4OeMpOHNwMHZQV_QqSKnRmBvhIM-qa1tiRIWf-dVAtqTC-m87TlMt96Y9C2QGJmZrS8rW5S338bmnUo5mp1NDuGLL1PWQBW4vRZ2PPqOAZwXs3fSlObIJmo-cxDddhera84dz-7EAPxw6SPcPKxBTOJsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTRqMQADuFT9Og4pjHfqYA9lgHHILt8e_P1UdQ6fsfrUqawBAYM6LnsyIdlcG8GMKLDxmEwLtiZzAfpWXrx2mihJ0UiaOeuTwdjWcw0GkJkb_Kj9z45BWpGIgDoI7HnyswuI8iOYcIlI0KrXl_Hni6WFKJMkgk49Gaz_eTauPq9gAX8CHanASJoM_zcPRQCC1mrk0JjdvvHKnWj2HJ9pzBLsCqdfOzp2fX8tC2SSyhdgP0gcAVSAY6NmnsGcTWANmBRg8o8F3mWzP_vecjJFu-OlA7whuZjqXi32-KFJjtDJ1A2oBTk7FAi6c2CxONcZA9dOfISrY-CvS4fJUOzDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hog3OYvE57O9vW8HPIV235IYfezxNI_UwtBIGJ8R25tEOYKDLXPzRvP863mMDk2pQ3BZEndXIjBncNYy3N7G6ARvvS0KOtw2STyKvg4y9FPQmREmioigieuyZQBVSho8bS-zwjzraZTzRNISDRl9XeZ5N22c9_KiFJ5FUc3hRIQEXhh2_Ufcs1EztNPgYFtEeNq_yOah2zNaOhJ30qy_mgeFVQDV6IHeCHyEyfMDuAq1RpMzei7Q1Mx42IAWwgKDERnhoossR10n9Lcyl0hdFnF5wH7PzygGNmQCFt0kv-tNFPKfSq2-bsA4dQMkwNPekfC1KGZ-L6vlIr6JH3ZZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=q7BvWUSVMM5VkOjGTtU4YI7udrkZ7tXmMvOVbfh9L6n9oS52YQf4EeFV1crZV5DKxshfH8m5MA0nUwgYuuVsoVF6ukLw1TBm5ArrkBR9Z4X6ZsdATC-8vUzSt1FYDUq_jJtd9pA1Q7uvDpmAAEPm0Lvn2bDlmhfGdM9W2eCtaarA_nzxpon1MH8_NqAWxZ2G1lNDKnHDV9fjmzST3W7dqTq12sxReAWDU7-R-fMPpTUHHgWKyax3J--MarsQ8qe-ySKhD5MkqNbq-9nxvb46mRgNXVBjgTrR33zgoCUQWJw46FXpvSfa0bbnWIqWQZbmq1bFfqmLjuHn-gxINZ6rGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=q7BvWUSVMM5VkOjGTtU4YI7udrkZ7tXmMvOVbfh9L6n9oS52YQf4EeFV1crZV5DKxshfH8m5MA0nUwgYuuVsoVF6ukLw1TBm5ArrkBR9Z4X6ZsdATC-8vUzSt1FYDUq_jJtd9pA1Q7uvDpmAAEPm0Lvn2bDlmhfGdM9W2eCtaarA_nzxpon1MH8_NqAWxZ2G1lNDKnHDV9fjmzST3W7dqTq12sxReAWDU7-R-fMPpTUHHgWKyax3J--MarsQ8qe-ySKhD5MkqNbq-9nxvb46mRgNXVBjgTrR33zgoCUQWJw46FXpvSfa0bbnWIqWQZbmq1bFfqmLjuHn-gxINZ6rGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdWt1jECuVUMajpWmigSmSVlqsmp1zI8_kF2u2n2wLPiZya0o9X_uNAF95suTmHa6IhWT2_Yu_LLnXM5yEbNojE2K9SO5d6B03zOl_anCPOCiSNawS9WrhBU-6groHo3_SaG9Jg6VAesWLzZnjufqZLy1h-LmBGc9Eevzm1cSp8ymepRajDyzIsXG46KNzpKQrx57c-8gcfmYHYxh5A_k1wpDoU1IlrWzwLS5glT48BZ1bKB0WhaqrXV4W_nS2i0mA2VyTHlOL9YmVs2yA95Q-S3Mn-vbT3FDVpBXeF2xihqDB1QvoCwOAksbL132CjjWoJR6bAQhtHcHUsBxJajnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=U3D5gbHMsTfk0o-EIVD9DZQQmy3aqss9nA5T4PfhfqM9YfBEHngVOFWnqHi95EtAvVIHh7AgKW8xE1pkCIXHRUVcgALDAe4waB_FBJfYJARby4D9blm1Tfc1yiMCcxhzRm-SGonRTtEtSx6Hk4WSZumoS_efTRcf2RBfh4BtHmOk1jNbl6BW8H-wMBmzXKtNmWvHlB8Z3A0pdRVB-9I6PlrbU0NBwN6Xck_pa9NIozfuiGP3LBKEM9NWHjN5XjicWw72ReYk7_2IHH2BYuHKrjcfztzW6JVjf28CCqnVrpn9VMOuuLqalHZF-hSmfmbH6mozU5Na03yuyXukua7fcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=U3D5gbHMsTfk0o-EIVD9DZQQmy3aqss9nA5T4PfhfqM9YfBEHngVOFWnqHi95EtAvVIHh7AgKW8xE1pkCIXHRUVcgALDAe4waB_FBJfYJARby4D9blm1Tfc1yiMCcxhzRm-SGonRTtEtSx6Hk4WSZumoS_efTRcf2RBfh4BtHmOk1jNbl6BW8H-wMBmzXKtNmWvHlB8Z3A0pdRVB-9I6PlrbU0NBwN6Xck_pa9NIozfuiGP3LBKEM9NWHjN5XjicWw72ReYk7_2IHH2BYuHKrjcfztzW6JVjf28CCqnVrpn9VMOuuLqalHZF-hSmfmbH6mozU5Na03yuyXukua7fcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD4OWR4c56Y2OKJH8jGJD2K7sQukhISe1Sg41sWcTV6uNRf_bt2qcitoRyj07HrwwKrSB2Xl_oETyS6ajviigsnza4EX7PWUPs1B6TRR2w0q_boZdqROu2KHyvUTr2kU1oAcNh6_nbpmjSM5PSblJCW__hWWHDENXSlJeet8eyCdvF953V8UqtKQcdhTrpEjEyg9CpQ9CDLInxrbeuEf5Fz4ubsfXEbG-s7H_nGU7_Lw92QdNZWBCg_LFGUCEAzjDe8LbPQmUWPr8zJL__NQkrUNdnxmLhyG-2bdCJa2_e_odq4lboQQ_anBRsqbTU006LzY1llRoQt3kGt-xcoASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ByOHHHlSpz_d5AKzSSJHk5oWqg71a4gBDX68Fvf7mO9cLEIPb9LgWpz5cN_fbVKOuhuHq_LJ6ODBkMj-_-1zVyMEM4jbnbN5tFAwmUGFnVk6b5VtihWRJtOEkyLptAJg-jbMscXWqOXnFmQycX-vuHO4lEXwOdt0-3HaVEP7w04AGV6cSMAPBPXk68QTE3VByu3yyGnuPBxp-trd0VY3qEFK78fFtCeA2ipCbABURy9EvGqkcw9g54zcpZbsR1SK7YUYn5zzA5AJgE82F1uH0CA-05WwzCNXiKVe3ejbWnvki8VLPxdGhhuMwpiFlDq5ZTvt2-RjP65E58IvJgiUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ByOHHHlSpz_d5AKzSSJHk5oWqg71a4gBDX68Fvf7mO9cLEIPb9LgWpz5cN_fbVKOuhuHq_LJ6ODBkMj-_-1zVyMEM4jbnbN5tFAwmUGFnVk6b5VtihWRJtOEkyLptAJg-jbMscXWqOXnFmQycX-vuHO4lEXwOdt0-3HaVEP7w04AGV6cSMAPBPXk68QTE3VByu3yyGnuPBxp-trd0VY3qEFK78fFtCeA2ipCbABURy9EvGqkcw9g54zcpZbsR1SK7YUYn5zzA5AJgE82F1uH0CA-05WwzCNXiKVe3ejbWnvki8VLPxdGhhuMwpiFlDq5ZTvt2-RjP65E58IvJgiUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=G5_DyV-kxe4SaC3EYpZb6y7zf4xVEResobTTN2xQu3k2WHOyDw9W7W22RjiG8ty-O0JGIn4YfpL2AwWwzmhCxx0THVuV2ee-tUQNd-6Q1m2asZLj9M0ai-dCP1SsofUrv3QtRdaxXiqn3Fvsxvdut7-yYx0rHyHNQ8UzTowTTkznuzDh8uFjq8dPAippfmlIq6vlXtj5yqOfWKWwfjcDDzJkDwo1KG1AWJEq9C7yPn1YPChlcg5U_rv3LzzrrXcwWRD2BFnnHMEj8kcEfN5rUMS4lqozlNGQN3hNwYl6bF0pcu_GqlpGlBwG9HkbY3jIAMHU7VE-hr38-WTEH829_2C7nQZao_bBndt6r1Wy1OUjjrj7MXsAyAld3pVfMsNlpkTa6Jxvghy4j7-uI2KVgdvqH0umWS_iCdOKaaGfPiw3eu63Q-iDPRyV9v8avTapMVelq-F5kyx6IxuUY-zSd6IPvYG20DKXEQkzWG_pspBpjZvDXKwypU44bzjaTz1gRlg_I2kSfI9F-dARvj_xTEcQgb5l0kWr0A4Hum5zwdDKc58-vwcV-xqM1K9VtMVP-la1nQuGL1dSeT6pxay9WWBCx_ajmambCuNC4F2b81bUUStuMo3r_9Tlq4dJTak31lpgqtd66Tm5GS2Rlgizg_Gkd7H0Qwtfo0ctLArc1K0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=G5_DyV-kxe4SaC3EYpZb6y7zf4xVEResobTTN2xQu3k2WHOyDw9W7W22RjiG8ty-O0JGIn4YfpL2AwWwzmhCxx0THVuV2ee-tUQNd-6Q1m2asZLj9M0ai-dCP1SsofUrv3QtRdaxXiqn3Fvsxvdut7-yYx0rHyHNQ8UzTowTTkznuzDh8uFjq8dPAippfmlIq6vlXtj5yqOfWKWwfjcDDzJkDwo1KG1AWJEq9C7yPn1YPChlcg5U_rv3LzzrrXcwWRD2BFnnHMEj8kcEfN5rUMS4lqozlNGQN3hNwYl6bF0pcu_GqlpGlBwG9HkbY3jIAMHU7VE-hr38-WTEH829_2C7nQZao_bBndt6r1Wy1OUjjrj7MXsAyAld3pVfMsNlpkTa6Jxvghy4j7-uI2KVgdvqH0umWS_iCdOKaaGfPiw3eu63Q-iDPRyV9v8avTapMVelq-F5kyx6IxuUY-zSd6IPvYG20DKXEQkzWG_pspBpjZvDXKwypU44bzjaTz1gRlg_I2kSfI9F-dARvj_xTEcQgb5l0kWr0A4Hum5zwdDKc58-vwcV-xqM1K9VtMVP-la1nQuGL1dSeT6pxay9WWBCx_ajmambCuNC4F2b81bUUStuMo3r_9Tlq4dJTak31lpgqtd66Tm5GS2Rlgizg_Gkd7H0Qwtfo0ctLArc1K0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiXgw1PLBeP-T7EaTMpU9ZNN9NRwG083ECH6vKSXqlqFpFDz6qBt7vHO3pviKucuOUKl3oRJtZjX57WYxWVKCNrT-3XJ9BS1Ixj7MjP78WaPnG3P07UAx1RFxpsKFYB-sYCW91iw8n6DR1j_wmhQoCqwR5cFZANnf9vKVdD4YK5UyVKX4ZO1hag2KikOrUqHpJNfGogfUZg1FplYO1Q3X4ZNrG1AHw-Q22bDsKOhWtFoJ0k1tZPfLfVV5RlUyDu2R9Navx6ovG-8BwE2ynBKstJl372rP_ltH9eZzkWxrKJnxZDyAvvfandybbd5MTHtiEk3smjP_iOmM6kaKnoo6SwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiXgw1PLBeP-T7EaTMpU9ZNN9NRwG083ECH6vKSXqlqFpFDz6qBt7vHO3pviKucuOUKl3oRJtZjX57WYxWVKCNrT-3XJ9BS1Ixj7MjP78WaPnG3P07UAx1RFxpsKFYB-sYCW91iw8n6DR1j_wmhQoCqwR5cFZANnf9vKVdD4YK5UyVKX4ZO1hag2KikOrUqHpJNfGogfUZg1FplYO1Q3X4ZNrG1AHw-Q22bDsKOhWtFoJ0k1tZPfLfVV5RlUyDu2R9Navx6ovG-8BwE2ynBKstJl372rP_ltH9eZzkWxrKJnxZDyAvvfandybbd5MTHtiEk3smjP_iOmM6kaKnoo6SwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iClgIbHfrfkIFHpt-n3vkdLofVdtq5n2OyBTYgg3Rl_EIzdpX5a_eh98o9qLwWOk8v6eGTQSJsa8UPOV64saVy1S-9TAkSYz1HVkdHTZkSnVKD_aWWavWM26GNk-5HDXStHkpBBMkOHvPbzePcFxw_xBSq_hp1aXwVUdfoumUu02m9Kh8ElNdidOrPe2uf4p1yuwkQBJh7lQ4_UfN_xLIeroDVsFcg4gpRnIRIUv71V83wiW75POMpkdTjaIPURcSSm8z2U6DUPGnsYnc80BkQ4OHrMXRt1H5K7sr5U25yn6O8dFSOrwg2PQtgWEG34s5-4XfV20JpMnHQ1y3qbBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=hLdxuK8NVz6gAEVtGJlDMSw9oJbEDT2rjLCcuWJSMJS30zOVvWPqJtYSbioeidrvigjo8A9_Zqf6KLnls5_mYmKLiUoc4OYAbz4NeGfxEGskDorJMoXgBoHCSbJd0nugiZ_5AjgyR7g2XIxAhe4VPHA6E3gKxMZj9CKPRo8WP1bBHMXhNGw3GePPgwRnYMSpspTX9BgPEncu7xBYUW8Py28ZGNGX-g7XbokpkrB19MHE2CpMKo5z_GW0IfMjo4YXIsdidjRjypu9EhTUFFPz2rV8ayAeh0tGG51CgIWLv6hi2P4eD_fX5WAa9HH3zigtUWdBJaLZyUK8Hk0-JFsyEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=hLdxuK8NVz6gAEVtGJlDMSw9oJbEDT2rjLCcuWJSMJS30zOVvWPqJtYSbioeidrvigjo8A9_Zqf6KLnls5_mYmKLiUoc4OYAbz4NeGfxEGskDorJMoXgBoHCSbJd0nugiZ_5AjgyR7g2XIxAhe4VPHA6E3gKxMZj9CKPRo8WP1bBHMXhNGw3GePPgwRnYMSpspTX9BgPEncu7xBYUW8Py28ZGNGX-g7XbokpkrB19MHE2CpMKo5z_GW0IfMjo4YXIsdidjRjypu9EhTUFFPz2rV8ayAeh0tGG51CgIWLv6hi2P4eD_fX5WAa9HH3zigtUWdBJaLZyUK8Hk0-JFsyEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=asohfskWUCrmnJb9p68t4eMaiujrPsYH1RYFx7ajaRNdJBOe80JckuLJWc3bDMSjGs5ySvHBdG30Re37N5apcFtst07wXKIK_akGjT5FjK5V5dr5tlU4_zCBEr2I4mLU7Ue543uowQn_9RzVLVE0Ii5tqhAImq1Mo7sis6mvd_lKtz431ETcm2yo9jbdY3hs--kKO4AI7EoZ1SyJkjsbpNOsQf38N7Dss7G4SIYF7p1yvJuGRKXMqdqLMPo3ibh7OhzC4boFpdvXDK9Y4pyg940JTD4y3ckbpHx2eAqD7QNnqv52tdgwGfC08u1lDkcenTeJ80DPjQdR9CYdFGXZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=asohfskWUCrmnJb9p68t4eMaiujrPsYH1RYFx7ajaRNdJBOe80JckuLJWc3bDMSjGs5ySvHBdG30Re37N5apcFtst07wXKIK_akGjT5FjK5V5dr5tlU4_zCBEr2I4mLU7Ue543uowQn_9RzVLVE0Ii5tqhAImq1Mo7sis6mvd_lKtz431ETcm2yo9jbdY3hs--kKO4AI7EoZ1SyJkjsbpNOsQf38N7Dss7G4SIYF7p1yvJuGRKXMqdqLMPo3ibh7OhzC4boFpdvXDK9Y4pyg940JTD4y3ckbpHx2eAqD7QNnqv52tdgwGfC08u1lDkcenTeJ80DPjQdR9CYdFGXZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=iA_AaTto5yKBcrl4jfWvG4sNkzPXXcVAzMn9MUHfljZgKq54Zh5tCgoSaRYGx_hMbTMBRrKAW3PcB-ig3z7JCMoHKjfxQE8VXtEGcSgYTs8-jmOOnWwplNTQQ8WfoGCIbFsULY8Upnfm0IMEVTbd6dqItdVJNBqHQPdJWBAZoi2FfdRaz6Nb3IYscEmqK25B6JoYbi8yu38TjhlyjRd2qKoqXd8uRxtFKD4Te5PEDs1feaMQyA62c2YVCYaJ171xpN3IyoDLIQ5X2bVrupcN34b39PCAHL1KJxcYMhUpGiZ2Al5Jh8iCZte9rwvfSnps8U42OC7Kxu9eXPsmrss4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=iA_AaTto5yKBcrl4jfWvG4sNkzPXXcVAzMn9MUHfljZgKq54Zh5tCgoSaRYGx_hMbTMBRrKAW3PcB-ig3z7JCMoHKjfxQE8VXtEGcSgYTs8-jmOOnWwplNTQQ8WfoGCIbFsULY8Upnfm0IMEVTbd6dqItdVJNBqHQPdJWBAZoi2FfdRaz6Nb3IYscEmqK25B6JoYbi8yu38TjhlyjRd2qKoqXd8uRxtFKD4Te5PEDs1feaMQyA62c2YVCYaJ171xpN3IyoDLIQ5X2bVrupcN34b39PCAHL1KJxcYMhUpGiZ2Al5Jh8iCZte9rwvfSnps8U42OC7Kxu9eXPsmrss4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8oVLR-bAbbP1CYzoWtMQ7iW1t3Nbbs6VEdsMwCrWEtOiq-BdrwDWeFOrDHdenUnX8erziMzE0b2AxkpPpwH76Gj7rtRBJe0_SZ_w8XvSkB3szG6SnCsJeOYFDCtPNG8vWRoLijzVGG88QXaofAqV8xWCGlsbKdFT7p6OhXdjRAqYPc0asJ3rVCAX4TQL-ogMY0nAhV2cHO_cycKulao1dIE5s2Hm07ZCBSYlguFvAIJPhEWtRsBx-FcUo9Sa_7fs59y6YKS-JkQQ7s7QVigu3j9FXFo-jLNReACcEr_9V6u0EdPEEbo0s5_wp42PO07EJS3rOuZ3qjqa7Z8Ltq6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFW3w1GQk5AOyQhP1JwwCaJCSj6de23lwEjmX8ZfLL7B-AdfNXUDaz38Z2H_rNh7hXjOfvSjU9mXQteZL5wRq9a5N2a9CSL8ue1jQY53mim7GwMMJrBn9r8PiYD7TJ-JSGxdw07GkMnTPbqhXX49v--ans9y5G7NrUiidCdtElCcy-YyZtCzncIvZdxbY5jKDSNTHsmXavCCTQ5x_WwzVwqrJz0G5iaxrM9n7FrSQlNo9kQ1W1jDE8qsVAMnf5xG9bz3gRRUy4vbgKMEmp4k7IvQac01GDBJCZv3uru3DxxjD7402FaZWkqtD7fUiwaM6OPmhVETld8EBFHsPgKgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzICUmY2QDIUD8zlxWrBHACRIjjc5wuc9bA9sR__QomenHlqc45QRVreM5f4Uepq7B1v34f_GBWqHBETSj2BSSrUls_FNILz24wxu73Nfns-hRkTLoeTLZxykrLQklMmk1Tb32gzHLbCjs5uUwjy6wSr2J2YXAMUQ0UMdxwOUarnmGLXarIzFvu7Onjt-ZrpPSkwOCS26SG5kpcCyGkyVzTx75WXmjKgF-xnDBCRFQ0Vg7auhRMGFyytvt0gSDLVYVSdE14S4w02zJ4Hg3QrX_a_35o1KnZX9-5Axk2pVWtu_4G2ivLFLvjcb4U1oDfKwY4l6UUDT9r4qPIig1pxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH5h_dlZ6XLIRf4mxJ0UvGG_V9TsCXFky3XQBBdElTYb71kE-nvCjnAspdaExSb9A8ecVqJPlpcCpiG3GmmGQc0gEEpCWSwmG3RRz-EwprqrputvAhCTfGk1HXtjkUOB1TtED-u152bWxBql4Gmd9JlgbLPK8OTkbbWGDv6rdPN5BRA7sIltcbjdXml2ybNmrlwWWNOXJNYmZPuqhIB_4YbL3dYvQSgx52wiVlfXZmhFyNJVRsKhABgZKDM4WwW14FmBrjU8auxnIsmqbekvNjld8SETUPzKRb9J_CMj8nk9JyDxCb08WChmyhGbzWDXG77VAnxhtbfLekDp3PUcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsTPeDYL2564_hPP_Er4wVAnwS7xkN4UoEee-3UJFT8v_756js4MagbWSGxyyoFKAgWHGl8C7V2r5EtIcVgNIfy5Ws6JA3jHNt3kYf7MzcUBHi8TL013hObZdEzfnlnclrT59jFylYS5Hcuhd2POpbL7AFgYD__BqsZocmDNo6jtiN0twGCk-wAWzWSRPjGCp2pX4ozMuhPttvXB1Uz7Aal1wmh31GF_mHj-_2neUrTK6i7e185BrGTznqtiVyGi0nRKgfw8qIvAO26erFJx3Myemyyz5LPKu3qBna06-OZXue30XIsFYm8e1XzhG04zH_k1BcZ-D-orGFlJpQeZtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLBs99RU7UNCasLgHsFdEuPTzEkoYrUr1bIN7pLI1tn2Rvd20vc70SUrZN6gB6vyjfX6-5SokvDFEputpG8oSM-JSOcyUGhcgfReMrKg2r9N0os-E3_-BDYkv4-JU5XBISy_yG5z4UOa0Z9cg5hwv-oFheOEFT1b1nEIyUDbjxc6H5Dk-zWyCHAHEjLdJwSTbrBcZR2WA_tkG3HsyJQ5r-dxwMNUlQSCbvziO693rF7H1iS4oyf6SCzorpngWjBTS0y4HarFuIKBIIb5PgSM2lxapr0pNarbxIFBESTe8P-J0I6a4u2j1TmbxRAB24EoeS8yXLnHYE3p_Y0S0Yb7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=JXLbxJmQRjs4NQ_ZfoRJA_05xx-9v3ZWqc3hVPQWX8hAU-cOWl-7pl63l7LkIDperP1235C8ZyA5kLnCyg0k5TJ2NV-DA-7hdmhcW4W-vlEGsH79e8tuysPDOlCjlgbBokrpLcTv8rujLXqTgUnPsJBVNYqnXnWLJl78WgV8CebecmFQ128s_z9d71rv33Z6DQ-xBXptznKxtQz2O152Aaxh6BssqtIeEea50LWOHWAB3hPVIRsGtgH8_L86UTnMqUWrAyU89beoQ5S6hhXe8jGJ-4kBK0sibeqv-dmSPvkrSEs4IDVyJZR6NPoM3ExBEu7vZpwx4WejI4Jo_wr8mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=JXLbxJmQRjs4NQ_ZfoRJA_05xx-9v3ZWqc3hVPQWX8hAU-cOWl-7pl63l7LkIDperP1235C8ZyA5kLnCyg0k5TJ2NV-DA-7hdmhcW4W-vlEGsH79e8tuysPDOlCjlgbBokrpLcTv8rujLXqTgUnPsJBVNYqnXnWLJl78WgV8CebecmFQ128s_z9d71rv33Z6DQ-xBXptznKxtQz2O152Aaxh6BssqtIeEea50LWOHWAB3hPVIRsGtgH8_L86UTnMqUWrAyU89beoQ5S6hhXe8jGJ-4kBK0sibeqv-dmSPvkrSEs4IDVyJZR6NPoM3ExBEu7vZpwx4WejI4Jo_wr8mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFCRLtdpZbQGvc9-35SsIsB_iaJ_MWc-wG8LtpsbNpWHAZP9ZN4k_k28PTQzB6IcqbfnxLRXBD_cO3SVWb-QTTkblQ37wgcxkGBea3sFlng0qalI83UWC-vvyhpyZwEHU-7iFSH2SI77A3lpG2J90o3_KvFdnPkeU2mWGNJSt63bznamxCFNM6mujYzSEdnK_6iVg2ocYA0dhyHkXXMVduxf4fND4ghHWkbSsJ7JWm2o2yX-YhwCVFeEK95YAInbjiLkDoBUITBp4HUspopHJqwQq6cfXfSlvsO4dtLmm152mlWXL1woOqa887u_DHUY0o5x-MXHnoRroGc6RzVYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrJi_snoGwXCn6TiX8K0nfYZa2wrD-XBnqkJJLkPJmNb5O0_p0jZbtQV7LjbT93kylbtgBVkPdSEltoJDF4WuaQ0XmUIRm3RIxuXY_C9uIBVvzCvmmqvwQyXupZKUVk0l6a9eQCNhumvi8P_Cd1359FRShMMYSGJ9xLFIQL2Rs3IihTLYW3Go4SjAzpd7Ct1mSyiRTM46Bx64Jm9Y8ZQHV591GfOa6Lj-Wz3NzMkMKpNYJl2ahGPsSuKpqEdBkyWZ7dvO-jmz_Clqic7aBpnpk5GFXi5TCx0pFeElFvAPiFCKyuBKkZZIm_F3H6fx6Dkfx5knbYBUwZEa8_KoCx6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEBzUPIRKMyXFEjxfojTvRkGJJof_NbW-cSqwBpVthVXIzylsbOQ-AdLj8Vy3fEsuAIFNNTu2kbZoQHPCpOFzLrCZN0sa_gIlHcSdsKtqMlZ1SvbS2shpiqFKiUg68u6JEZhYuW4v6BD-ZUjNW2G9RKDxXI8d_-6mXNTSLvRlt2wLaUb-cwh-I34lU1atA3HngXZLvhcj7Rp4C3iJRiDdEVkYYHWgzMq1h0SLLZQ7-PTNqIW6ePclkzDFOg1gPK45fiKFZ_8I7RwQIuCj8kS0cygtcy_8fDcKHc-geRqsGnEfHkhSlTV7Ypa41XVTALGZTPQYtPDF6KRunNggXMfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMfO0gdP-j8qSneO3rFxPOguuJfAhhW2Frm-XFQGGS7ywiPrDdgrVkj9U27nnsfyQf2SVTn1gW_WT2V7KiRr4s4kJifeFJWvH1C-iIpT30nfiOvY_Rnr3UN0smZXGB1llVpZmM_B8osqQOYyfBTOiT_ydtJFDPWV160GZhyB9GMkPkvK0fyt1eLt22iQIicuRTYQ6xjOlwJOV94pVe3Ey2w63uSJAizfEBcOPJKO54evDLZnstLB4AZqPDyLsOBNrOSL_6J5wAoyIOo90SqK3yP0ZHUgvzX4JUomVb47zG4jSfZssGBjGB8v3dXeTnLM3K8MSrfP_nUaR7d94dt01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPzxjXSuT1Bqugf1JPuCKjIYfjCAt-dpe_3raA_7sg_QiqsS8uKMN7GDpTf0JvmEVB7SAhcDv_oqqEkeWim3YF4yJqFRw21Qwt81kdKgbf7GYObHPzB8YKT1cm80LiyIBZK1JTNj_IhKYWI0u2lGubywgRP07E1oXBUY7VO3-x1ZHaJGnyBc5WUV20CGwWbqPtABE3eV0ruUVXoZyj5VmgsCjGkd0wqr-FAmhjzW8mtwNa5dwgbZ5nLGVNpkBJ1K2_dEuyW5AqjuDSJS_zjcGcK1fG3YGqprUCMLEarGZobj-L3Zj7vSMi4r8dir2FxuCszvBFQTxCGA-bEtEXXMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heh27hq3iAc2j9xLAOzYdl1VhIoAdAhX9pjRGnUBnsEZ624d8lxa5nXdQYnHeplhdQpe0EUP2yHcdhwjrDFRT9blGXXNqeUP0pABVAB8ggYy15cHp7hyYPLebwzLyl-FNFH_Ywa57aOv8wWul8itYA3R3vaGCiprPNjp9aJwI1R7r3u2FSJsx7jxliHEgH-Yw7GMopY_Z--Tzhqp28c8o4CyTLP3W_Emz2fY7gRrjTyPxvG05-4fdaBRI5AJZETKXv80qw0GUzi5LKZ5PVuQLVw6jHXbIYLCa-fIUQqsooI-wqhARAXekktkcStOPGkCcFZ1n9nMScc-Ad2_2j_9tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=Sr36mCO3C3f8Q1pbueQl__Cg-VxjC27nb8obr_IdVDaVuvYTI-F5gZy6D1odZtimls0KuLO9NeYV9fzbdsXh4ArrDr3FAqsrAqF76O7oWBXCPYpuncprRKaqwEhIRxBniJmshTrgk9W068a7XX6jSuWDfqXJBTc_-qfaR4e6DADsRjrlnxJe21PRfw8qQ7oaPiv2flCe0rOHqkZGsj3kQcC8ISvczBmT6rGa0s1gHqDojgZyKvcKXWs67COAzaFGpy_Binlk_Nc5KnAqPl2i1ODBR7GkoYq5iAbjqSxfSFSmkbtiN6pnrQwln-E4oTH2inrNEiN3uqOnIzaObZs4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=Sr36mCO3C3f8Q1pbueQl__Cg-VxjC27nb8obr_IdVDaVuvYTI-F5gZy6D1odZtimls0KuLO9NeYV9fzbdsXh4ArrDr3FAqsrAqF76O7oWBXCPYpuncprRKaqwEhIRxBniJmshTrgk9W068a7XX6jSuWDfqXJBTc_-qfaR4e6DADsRjrlnxJe21PRfw8qQ7oaPiv2flCe0rOHqkZGsj3kQcC8ISvczBmT6rGa0s1gHqDojgZyKvcKXWs67COAzaFGpy_Binlk_Nc5KnAqPl2i1ODBR7GkoYq5iAbjqSxfSFSmkbtiN6pnrQwln-E4oTH2inrNEiN3uqOnIzaObZs4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=YHbVMIqQ4XIqMcpnpXrAwAY-4Mbgj4kd268pt0dYs2SCvPI_UquZueKUqpQW3wy3G57aJJCXnboHm3yFMoyn0iE46GFjc6Gp-CFwV5YPtAQ_ZAjbVjx8JE0-7-rrsZocrGCVmiZDhm7O8iNjeW9FY8ZM06Oi1EVHUr_1L_i-WdHpn5o-IEBdD1ojufPOHvavBDjBD_u64P2t23ZZwSES-ZeMnsGcbibg9MdLSoWNhKcN1RRA1JIfK9UtvHdXqZGGkgKFgRMUP9jrM7JgM6iBhYQ3CBbUXtCYlbrMHzFyhiRl4fMLyJSI6oAolehUM_Wu8bCERq9dcHZSrV0S1DApTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=YHbVMIqQ4XIqMcpnpXrAwAY-4Mbgj4kd268pt0dYs2SCvPI_UquZueKUqpQW3wy3G57aJJCXnboHm3yFMoyn0iE46GFjc6Gp-CFwV5YPtAQ_ZAjbVjx8JE0-7-rrsZocrGCVmiZDhm7O8iNjeW9FY8ZM06Oi1EVHUr_1L_i-WdHpn5o-IEBdD1ojufPOHvavBDjBD_u64P2t23ZZwSES-ZeMnsGcbibg9MdLSoWNhKcN1RRA1JIfK9UtvHdXqZGGkgKFgRMUP9jrM7JgM6iBhYQ3CBbUXtCYlbrMHzFyhiRl4fMLyJSI6oAolehUM_Wu8bCERq9dcHZSrV0S1DApTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-YHyyW63F6pK2WIkNjPLLXMlu9hW2KoxZWizBwUOUwDSQSwGBbVyHrIyzCzUIJGdP0rntRSHjhZ8krXBtVjABVaDzOG3VW1P3afHqCYoCGo1h_NDSKAdtcCZfzn9yk0jqBru3ZBqQxkLUKuXcSiEtNdSOH7wv35JhpBz42AfSGNmdQT1Z8_sfGNY70hfRl8cGPcivrcTI_Y37DdxevrQgM0x8fo5IIRM7MPKIGfD5ethDxz1HqdDZ-5FeiDD615SZ-ZK8M-s9CyvHocRbTI6QrOmhSwsgAGzYwUts03opyZx2LwUXX8arrs9c4S4KxV90DJu9leBiTRvCnw-XfqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=qQ463nJ2XoJmwKwkxikdthgQTBzDViHU4QmKwN9KtWs_d99bCtr_Wkde8X95_4s_tfSaBBbxAFfOXzTP8FfubymZoOzXj-9MHC3Gq-iqVWNvIDWqnWhplGBSjazPtZCiqSfEEuHffM77UC3o0lN3iHnPWTiB4EacN1vGxACHkXLwnlghsnQFMbAdhgJ1f_eQJyfAEgndSa6JEFzxcUdEZ1pFoD6wu1Vu7zDobnmh3-BjI0zPLs-BKKSh8qc46ITEmn8rPD4iJyTaYf0Me2cJrRQsDPr7NvrrxmQPn85m3YxbgwlDkPFvfGnCWTuNR5D8bdM_VrU4FJkzG0Sr1OrufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=qQ463nJ2XoJmwKwkxikdthgQTBzDViHU4QmKwN9KtWs_d99bCtr_Wkde8X95_4s_tfSaBBbxAFfOXzTP8FfubymZoOzXj-9MHC3Gq-iqVWNvIDWqnWhplGBSjazPtZCiqSfEEuHffM77UC3o0lN3iHnPWTiB4EacN1vGxACHkXLwnlghsnQFMbAdhgJ1f_eQJyfAEgndSa6JEFzxcUdEZ1pFoD6wu1Vu7zDobnmh3-BjI0zPLs-BKKSh8qc46ITEmn8rPD4iJyTaYf0Me2cJrRQsDPr7NvrrxmQPn85m3YxbgwlDkPFvfGnCWTuNR5D8bdM_VrU4FJkzG0Sr1OrufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUmjNdfHNfAFfNB5w5wLR-asl4mhUML8FkzOnHejlybXlbY5Ixz9mFHTtZpmjD6Ve0WNX8JKJpAUA61KGh9M1eHmc7UYsqFkiSD-u9g1ZHqT4t4WTekKC3mZt3lHOvqBCX5a-2WP9PMSWfyTRNT2FgC-t50q4RXh-fQBEyZNjDZ3zLkTCc_Cds1JKdsu4QWvtzL6suUy65p4VXvka_b0FVHswefVIbDzrvjVR8sUojDH-ywmv-AIrWS4MOjEia10TIE73D-9u8SbN5WlPHVczbuo7Rs5MLSKWo4R3mbguYynslKzrvX1GQ9cOCUr5KIT2e5dLVmxC8ocLY39fAQIpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz75V9DyGzS-wAAu5gn1bYGrByL_xJ-kTHGCl8uwWnI6CDE8h1k5hZ4J9KWX9zqeyGyQFGdEq2P10XRuIiD-WVocYlSiVazg3XoPJopb7SnUNpt65v133y6ECnTgkL01x8sWQyfyxAk9Hq3RDBsSyn50f8jn3zVAdebO4vpFPtYk76l70bE7Q4SUCER_7bOJuKMzXQumbtiJBrD9jZZ-0qnebTNYcL8X_GRjoBfPgljF56cwcBSHezK3ivpNGWsEXQDXaDoZ2CLa3oiHjlfoK2_vEB-7sf0QnXBx7ZDSMHa-3-y5l3xvaHJlR12qE53NN1f_mt0IyeXuWfBwfWIcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
