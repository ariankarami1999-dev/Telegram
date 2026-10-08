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
<img src="https://cdn4.telesco.pe/file/Bw2ad-fv985ZnkQzD0Vhy_eqaDy0JXvVvWXT_6PHJ-HC4mnerxwb2YPCuhp7GOEpC8cDYerwB3juYdUqwdjcthuAPb6QGtJa1eAoBu8SfuEVqIbHPT1m0jrUx_y7sFU4whWNXS39CWOq6NFREynRAjyeH3zunIybsQRr9Hrp1DoWDk79m8P2gF5tAJsNOnFhTf0Dnc08WeW1MiRMmkMLM0Bc91PG4Ynr-gkUuUlKteaNKIHVe9eMyuKR5-BN1yHb8hcl1XrRlc1adRvQC8hxbPtG3LpTAZfCVm5PdCE_oJN8NUIv--bIf7OD30Tp3PKDZalzBp5EA4Q2fn1dyWcO8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 264K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3_g6QtqmaTF8FaPTz8JgT9DYSDqM_OwBAf5cViHckRu8w3k86wGbXDF-o8jkfvxrWB7CdpaQpzEu7RzwYv8d9VYvgdkHGdsBYhoQ3IeePKFocfJz-tnq1oqG66W4vy0QG8hYQngwcZcXOsXZiwBA503JPSJTiBkj-X0aADX7PYCZ5ZwtVyZdtx0XlGsLgyuMKwwSiwbapDNWGJ7C-Naz5HDUW7zhSdOB1oksRLTaa5RYwUjINtesXnpGgEw0AaBOiDMrIDwYiy-J2-aZz99H2vqyGqJcJ64aQ1maNXkwAW8Ax1wRQTYqGeXp3tg_6nO9Qgl8mWRSaJOK-m0DCoRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDWDbGOja70IGVMK1pKtiQLv7bbsnipdOcaWIryf1ymNoEatZUlxHNi8YXMZJiFMUBuGCWGEvwuptkMyrpvj2cOrdMjMpn_ZJaVetwkX77rybW-4T2wuXOl80baotHxuxW6NC_f2bRw9OU3WLeeXvoK-QPbwG47siZ4aF7ojXjh9WbuozEnvPN9X_snlvKf2fZJRTE7tN9qIGlvd3AMgPkezC6R45FqvxJ-1R2zVU9l3-NSSAv-Hn8ktvtpRyjerDRJ4TG6H5OjIfG6HL1BmZC2MQpApUmy3GVemJNvsTobocbdgxSyXgdxS_cJiIdAhSdWPa7iK07YuTrQe0i6rXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
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
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=MKktUFYY1vVhbXwiHQIDmS6L5aU0pyt-sUDkBPJLW7ufSpV4OGps-nYz6VrVEYsEtCnW1rJmdeM_8_ttO9zRQ7GSyupMn_14fDDsj_9-1q-J_a52kpSc8dJauysEPsm_w5Z9bkYKdkJVrVl6a4oGIlUrI8eBRxCrNr0dvFE1YiMdAEwwE8S9CAHYPRHAJ38aaVATuUAvxTyqFTfc70aDps64t0MXfSrLSaYOB0l0ZLkJycPv-7_gts4j6LRHqdi87PyYjSwAkR0FTXgX9ciSyzsXpJxJH_a_B-vwaDx28Srs5Ci2_5rHBL2ivL7t_9bloQFgAG_1OlUx0S8q2SwDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=MKktUFYY1vVhbXwiHQIDmS6L5aU0pyt-sUDkBPJLW7ufSpV4OGps-nYz6VrVEYsEtCnW1rJmdeM_8_ttO9zRQ7GSyupMn_14fDDsj_9-1q-J_a52kpSc8dJauysEPsm_w5Z9bkYKdkJVrVl6a4oGIlUrI8eBRxCrNr0dvFE1YiMdAEwwE8S9CAHYPRHAJ38aaVATuUAvxTyqFTfc70aDps64t0MXfSrLSaYOB0l0ZLkJycPv-7_gts4j6LRHqdi87PyYjSwAkR0FTXgX9ciSyzsXpJxJH_a_B-vwaDx28Srs5Ci2_5rHBL2ivL7t_9bloQFgAG_1OlUx0S8q2SwDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uftXsHtZ1aISWJYiHjOT0pcZJOl37NjwlMGxZ6xo1xm0-3I2byWUHG6Q5R7OhdJegGbfOHzkAg6cDrNc2YoofW2gROdyAFVGScUqnyTYdhE8IEOYpYobVFMvBNqq_rMydkEOKv_tEIIlcUhXF_uAemG3mkAfkqowm4xWGFdATeQ3Fufl6X5FxPK_Kojw_YY2RkDZHCE-mNs-tmn8J2c41xUM5OZ8TejFeGh0qjDMtrG1QzFiOR-UKneHAexWyVoTxfW4lgM1oaJWUa1sBvRlF45ZyXm4ah0uevidOg5XkvNqRH-1inBJHH6MP5e7DLEMRAiOH0SK9RwUH00efQ9SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=LZAS0HpipvBjHQVbcu6NfsKtOi_kcHRlzI-fdjAGTO-a7vI9Nd1-A4hW9syx1roMg0xMci7-j9pFhrCGDthvF7SY0ANOjw_kjgehzO5XTdHp8D87y1WrN57EGraCkNENg-8sRJq2DE7dhinLWFsS-MC3ulELlnk1TKMc_1yFMLHGCrG67bGDIpPR4DKJT-NJF9SNDcXmWpyHugq6GKfyWs4fUosZKLfyS_3Qdhjq-nAdVOmDOykAIOwo-CM22ZLlYdcIAGVveWnhOeNseiDTpFtspTlVz1E1ri_nKIRNREVAwDvkmWyAOZeJY9ds_Mskp_O1DIPJVnmklQJ4APxiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCWMbEdmvYh9m6JYRS3eQEP3vWufSzZHQuI9uNUkp-3c4z7cfSvedV-ufPjy-U3Tzm7Xrzva5KROHOzB7k24eAhUHpEY8YbYH4aNshFtVf7CJDa7ESs20LqBRr4slT5l-6fvouTa1yoxdUhet57FY7WCVIzu73LiVxxPIHVKD58J1jmIeVTZP4XD4wY5Y14mYp7IKJLr-8_e5emJ1HoliAFIXFwqKh-KMTs5AL2rgTUP1HjxL5WoFtRaAO2Jc3a18YAI4_lajSFIZU59zRFQ8pDCFnESPu0QJJ0kHHCtV3q9DYzHZM9YIsVfUdlNrwNuIPops3ooD5KasbUjkUW9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJGlPgCbBv5o5sLwhGU7db4oxMo0P72-7PcgR7xM6z8-Q81LDlVjJW4_ES8U-ZjyPZcm5kwgIlLP31K4rgsjiAYoUAimep_eaMaTJo2HnFSYDzArjDQ7b1PRkw5HUQLPE-jtD6Ih1lUAJoRUAqfrqilCZAEqcDYyY7PlC8ufTosgTcQw1J_JQFxFOytazZkhiNkNJTyYBrsXrehFYmyOVz_q92CzV8Z-jyKMx_FrDW7fc5KFpqMjLmxqoaf8Ibgfr4S2E0X0tDIJP_FsqfjqxH1jk4x0S2LDXz_Xprj1MPD385eEM3Pbl2tlaLOs3HnwmhV4_gi0CEBKFdfsFHErKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=beywME4Rnxil96E5lWNxWSHAWKbAaZD3xPFYqmmRIHjuFX3wkORwEQowV-K-ZyyQ3yoo77P_nMSp3HOpCfO1ZkRuWKBrpg3xQgWcy4V2mS4zHMjsPfAPmIx6ZufVzHTdTnaCjDc3RTU82xiS8ynry03_F9GAcHQjkD36NbfcZocUvMhgVjp1rQnmR4ic2I9jnu9NkvLOabRO9Pzml9V-gZHuNlx0faIH5Wd9Jv1shAXj8nN-mYllgVT8qdiGYkqiD2wtMVRE_oe9ZJTYgNMyUa6TFUZMsbKn6Emcn20GGUKYSIPlmTJ8DCZQT6AKHMHtWlDIPAzG454VegIgT0snhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=beywME4Rnxil96E5lWNxWSHAWKbAaZD3xPFYqmmRIHjuFX3wkORwEQowV-K-ZyyQ3yoo77P_nMSp3HOpCfO1ZkRuWKBrpg3xQgWcy4V2mS4zHMjsPfAPmIx6ZufVzHTdTnaCjDc3RTU82xiS8ynry03_F9GAcHQjkD36NbfcZocUvMhgVjp1rQnmR4ic2I9jnu9NkvLOabRO9Pzml9V-gZHuNlx0faIH5Wd9Jv1shAXj8nN-mYllgVT8qdiGYkqiD2wtMVRE_oe9ZJTYgNMyUa6TFUZMsbKn6Emcn20GGUKYSIPlmTJ8DCZQT6AKHMHtWlDIPAzG454VegIgT0snhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=FYGmTWwBgZWJWBpv_KeXmpE_ApDAQgO1KhrbVm9CKIDfSliP0ZCu3Jki1c4PaYcfQDDmXbr4skicnpNGXmNveDA2WwmsRniR7uv8NsMan3Pi7iZNYsMMfuhRHWYoBFyLLK3g2sH9_wdWgw_KaQNlhUfYe94WRVCEzJ16KWhkPouvkaVSIOUFlcg0DrZZ7icOKJvi_qA_PFpIh-LStAb1kiZPlR6Dgnf2QHSOqN47VpcaCqFqyGbHSj9AOvjrWnjPPOXaHm3s8kU9JQznPVTaztoE2F-uk-N3GOXnVaaOD0pNF8HgIoaG5hNle6HM3vDho-3oGO-o02BGopxWZ4IYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=FYGmTWwBgZWJWBpv_KeXmpE_ApDAQgO1KhrbVm9CKIDfSliP0ZCu3Jki1c4PaYcfQDDmXbr4skicnpNGXmNveDA2WwmsRniR7uv8NsMan3Pi7iZNYsMMfuhRHWYoBFyLLK3g2sH9_wdWgw_KaQNlhUfYe94WRVCEzJ16KWhkPouvkaVSIOUFlcg0DrZZ7icOKJvi_qA_PFpIh-LStAb1kiZPlR6Dgnf2QHSOqN47VpcaCqFqyGbHSj9AOvjrWnjPPOXaHm3s8kU9JQznPVTaztoE2F-uk-N3GOXnVaaOD0pNF8HgIoaG5hNle6HM3vDho-3oGO-o02BGopxWZ4IYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.  + احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84570" target="_blank">📅 22:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phD2cYXff7rgn0D99W3iYSdU-QMA8Qp-NGg34wLe8i3JV1B3VZDdiqxl870ytlAoWrS8kCRysV738MCMhuLOpIIu5ps2X4SXn0itD7_7lwgGj9mnrmAmwtqc30t5U4PtzPgm7YF-nsSnUGSpFGQFYDgPvEJSLUf1HJxxE9r0uXjWMvAXLHmCWckjtYMkRhsObuLhsoN67lyfKJzEcFkjN4HiGb8gDEu9f0aJ3xAMyE8WjFFXuWMir1WeJwGGR0d6B6DlL239LArYLJFvZHvl-WrrU88bidSSFcFAZu-Yhv6ZhJ8XMhoCd1Uv_8hd1sRbuosBpkJdyr324z63P-Zxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی اونایی که دیدن میدونن این کلیپ یکی از عجیب‌ترین و دارک‌ترین پدیده‌های مملکت بود. یارو حین کون دادن داشت نصیحت میکرد درس زندگی میداد و لا‌به‌لاش هم شاخ‌وشونه میکشید‌.
+ احیانا اگه فیلمشو ندیدید به هیچ‌وجه از دستش ندید پاره میشید از خنده
😂
😂
😂
📥
مشاهده کامل فیلم
@Shombol</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84569" target="_blank">📅 22:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQG-4dYKa3q0Ruah7nH829UGoB-wp_O99_Hv6LI5_9-USG6YOY8S_cGLvV0fopHAR7UPY4Yv_5ghEUNp17LN8pDlHJesjQ0QkiK-Fni_XgDnQb0IAdFBKO-URHehBMeQzpaZ72T36Hk5HHBCkHyhGZIgkCrwmG_hCkqPN-DNSs4zrzlqt-JqjMKBigMpccfvOyixVeO8skAR6aJasnK_8JM5SwUHBwthA6aregJVhrpLoYIJmwhT9V5PL4e0Hw3sT8Q_RFDTJae-Nhf8OMGcN8aCjNS1blccReYHv2z3Fms2be0G6vsJzM8LqGPCBPzWONe0YjFciwJ4IFQKnQLUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aie73gN64MO8-Rkj3Jsy_-QjPE_YUb6PU-ucTZJWact45-LFz4fRoOslgU9kaWXNu5uFTB4CV1iD0Eg1uTZyMajJjjwyn6izlaov3gU8cbuz7uB47osL7bHbammF15kxfZkmDh_eOuPOstuqCNn39nwc5vN929HizTdr5EIEi81zASJxzAA8m5PiIXnGzcuVHXteW0RRGLDXlCdsDe8JFBCnLg3GhLLCoUXGSAkZTBaR2BXHe2GRI1FaJ43_OHc-qEEsmomIUNLMEKBPMoCZ5turD1hWaLLqgQtAkTp6db7eFsodsQ7Yp6hhp6-xZ-2MycFc7eVRj5Jd_WbdZW7SzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJh6gZQeKPikS25xTnj9MNoRX0HWfxQ1OpAntzFSCQ_qDp0FdVHUPkN_fZmp0X5bzmsmamk-b64YFVPHC6JEEnM6EYdMN6T_MPbkEQwUT2v-2Lv2r7ToGRB_58hw1mSq6ai-cHZjpScxFrkGe7Ve5OC5wxz9HS-Vy5Fof11BF7f_Psi2Fok6JLRgGaqiwHlL-BSd6CNv1ko2zVM5HUBARY4Yt2Dv-bNW9JXcFFcwOBQ6DumZNTxacgN-LY8jYd3m0PEymVxNyLtbEoTqBEiIjw0eGJPwN45jQhG-KyyvHqKDiC_6nsXrKk6cQDMCb4-dXF8wabRWtWn4YUB6aaG20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MFWmIEmqiV6bzbLr_pdbbvST-3dylcEmlMv408SrBTczDJ3RyK9PLnuqOnyK_GhfFWsEu_3GBcQ4fV8dq3fY_oKUPw3l00A9qbC6GyWVldKQ1bgqBXCwvVyTy_aeSkzr-neFjamJNjDQd_fuB8GxMpcMfO39AuQ0YUtdQyNw-XCPxS17YKhbMojkG6qtgBiSp2jIscyiC2-F0Mw_YG5P3Cng3glwvXJTtgpiyX1sEMCMk4TrY0kXMns9juZEiC5kUuElmmtkmOWGO4EVDkLCywk3H2qXoC51Ufcg6hjlihcfvr28fkdi0tS5sWQ176MjuaBUPjfrJF-rpgVCO8d6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=MFWmIEmqiV6bzbLr_pdbbvST-3dylcEmlMv408SrBTczDJ3RyK9PLnuqOnyK_GhfFWsEu_3GBcQ4fV8dq3fY_oKUPw3l00A9qbC6GyWVldKQ1bgqBXCwvVyTy_aeSkzr-neFjamJNjDQd_fuB8GxMpcMfO39AuQ0YUtdQyNw-XCPxS17YKhbMojkG6qtgBiSp2jIscyiC2-F0Mw_YG5P3Cng3glwvXJTtgpiyX1sEMCMk4TrY0kXMns9juZEiC5kUuElmmtkmOWGO4EVDkLCywk3H2qXoC51Ufcg6hjlihcfvr28fkdi0tS5sWQ176MjuaBUPjfrJF-rpgVCO8d6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63SIZMnxLmAdnISagrsDKpupPU5ATmTEAax7cGgYOs1b7-JJ0UOznH-GZenKxbPznlnaXCkunT-vU84hJJPbOXpVd8ai_oCQq0wsh0s6zorG_TEuog5rXyATAdX7iIeqYOMwmzXXm7ibVERL8Cs2m0L9r6rETKddShL9odXarYs4ADHekmra4kJL8rms36z1aYZPWXRzVNHqMIFmqGl1ql_Ni2MvLrJ_qiPf-BASamiuxl3N9G63dg6cKJOYrVoCcTYzbtruTgNGAAUioQTADQY3ndqLAA7TIHOtzgKfousddmhuxYJkLqN3DmyogU37Vuy5mo4R8bHQ5VsTNj_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKHT0nFanJ1rb_E_2EjHdQbBIE19W1qHDkpzRsX_Pk2LeTbMi_toe0gCYcXshRCHM7GGXMWG5u93omQYFykEbWWOV_crfcl7AdgG7iwAdYwjVDXUrzSyTf0tL5KxWTibJ8l8CbZjtBQB1RNy1rhDj_sj1M2gETv3NV5maVO1Da30CKbRTPSWldlv_e36VvX5Ij-5OeZeyyr6kBDA26vqkcz7xOhHDgnufeDuSU7OrZAB7h_2QBqST2fW42X-jJsWTm7QtdaI7pDiLx0wGznXaDikFbMGOugOgNp_YhCPQHYQSzg6BReEWAwNDKxrEduD5ti4oTA_irre0szB0Odswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=sKuVDAQGcgHCyw_8CKFBZ4foUiTuYEwEETt6f8zqfhU4Io60VETjz3rzGgglooDr73hijkyaMaCOeJhhpWujSsTBfJBVWMw3ZxT12JQ7_yHvF8LQZrPO34AQSZeUJb-eR3b13UirixpkUnTNGyvatYHxxK11CELi0EyPihfdPFlajWkYJ0aF7V-SjzVF-776MmIHkyEZpyRn79yO2NQcgKXgFCpnnhYQBbbVbNQeFikwv8leV9XsdPOmu0Pe8a27VhFKWSNaiYQhuzypWdB8zCP9k9BORuIpc_xaDqZkDMJZ0YgVk0mQ2_ydCVt_THTtVcf0Xzs45Alenj6_YJLAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=sKuVDAQGcgHCyw_8CKFBZ4foUiTuYEwEETt6f8zqfhU4Io60VETjz3rzGgglooDr73hijkyaMaCOeJhhpWujSsTBfJBVWMw3ZxT12JQ7_yHvF8LQZrPO34AQSZeUJb-eR3b13UirixpkUnTNGyvatYHxxK11CELi0EyPihfdPFlajWkYJ0aF7V-SjzVF-776MmIHkyEZpyRn79yO2NQcgKXgFCpnnhYQBbbVbNQeFikwv8leV9XsdPOmu0Pe8a27VhFKWSNaiYQhuzypWdB8zCP9k9BORuIpc_xaDqZkDMJZ0YgVk0mQ2_ydCVt_THTtVcf0Xzs45Alenj6_YJLAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84555" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cH_15zAzFExJYBpzv7GJT_mvfgeEFB8YqTHKb8B-zIXlkKHpkeqkOBSKAQxVRbdOsaKgk-2XOFJhbINpkHIvQb5NX3QMxPmpAmALc2YdMFAh21U5ur53HobyvQT7vZR6p9vNB3ju09brDDzMeBdFAUBzfuKPel_xgKpQsjRnWxVQQGet8gxAw-Lw70tAavj44bCA-XuL9w0a1S2aiC3YBYvZX_o-REZMuhJqWUNEs9UzsRKXLMF5id8KAdeEdbmMMDtB9DLee6GvrP_0n1CckSRAZR1-SPkEvlLuzPDXKI2LI-ENSWVjV9NeDY00HXULgSKIpdQ-mOMauD8BwDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G15
🅰
🛒
ورود به سایت
👇
✅
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84554" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4fVkXDUn770a4HSRuIrzbKiKChIF8PK7aWnSVusZgMKdV_sKonpRwq_ztIeEr-MKS4jqbvl6yqg-IgbyYG0_UZvwKXRpgX5Rym-xepr7UPvEvN7BVaqosqa0mEXgvva3SiM2qG2ZTUnVVEpywNUuj_eEwipjATCXGQoc_aW9qQhpi5_PO9IwJp2zLOS4p3Ip8Oy1Z6PvcYvHguFIYs8oaS28PD6tnr56AJ56SvoP_Pnxgu9A-27EqppBq9Db3PUTWBUWq0fSx88RWaK4yBvnsa58-mpm-04Cf41uJuVcsxo9FeAfDXCs-7i0S3JSl9pyrPvuUeLHIx1X3h3J2FsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHcJ9CPvBgLHSyonItt3Ad1FoRY-alI-PlmwQndkoqN4OAbBoJvXN57nMRVEyOvYdot3TAScJaOUDdAXbXWC7n39uvOD0lh27N1Ki4WaKRDj6Xwu53rCOhz4doTbfLE8BlO_d8lt7VEcmTKE93WcpFdNajWq33TFzmaVqQYynmoBB0Xw48wbcGvs_nuUlf0p6InhzCxcyiEaH2ZCLBF_I7rlIVMcqq4NJvD089kM6-oF3l0tBdAtxtDkN94kbRfu4QIt8GpkQfClgoNtsfe_i0XTeK-URhRQs_QadT9iKrXuQ4aIZxp5eZiGz3ePGHJ4314JVKxEaTINEFBmLc9AkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T226oGAFfyiF7k9X0zESDo3jW8awmHNchMXra1oYCEWT_aXJim5BARc1Xwh8eVC6NGgUL0yDKl1YnrUsqTxqR9tYoPdhSBmXVLQgbHEyx1qCZKD3jkfklJdmpd8gysXVt2aRtfDnXWlCL40RSqJcTM9XmWiylLQizPPAJ9w0RZPIqvyr69pY_vYlw1HLWVoC33rZ9C1qc0x8u45CM3E5x-kMyEVXRx88ZdZeQg_aOYVHLsmRJ2KlPLbMmpORECr9NhLua3sW9pZUnxGaiKyRFeXNpkypYcm_-aUnFnTyczE4jPDT2QuMtOEn-pQoqHDIS-5fHdY-G9uO53kN1sSORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=fIKVzwvMB3hmHsyBnc6oXqETdFhHi6ZxXS-vJVYfwPz8jTpiUi4-m61zbV_h_VV93ElBwRp-g0-vdQm5VU-B5yhktBeT_7p_P-yu1zKqssqpupPo_GCv9nPjLJTJ2iFaZ9dwGGIvj5fC5FMaACv4OhM_mMeTQxRshwCStIZ62d0JHQUA8c_D8_GXJxiHQirC_o4kdvb6MubLFw9JbFYQWzc2gBN9Jeh3KAxlU6wNG3je5HoLbGrkXbEjqevnU5RAErZF42CJuAbnoMPVeTNf3H-1o2zLiCrrBPlSLkaXTcV9PM4Mi-4cgbFCkaLg3vfGxyD48rF94NhDfpP1fkEzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=fIKVzwvMB3hmHsyBnc6oXqETdFhHi6ZxXS-vJVYfwPz8jTpiUi4-m61zbV_h_VV93ElBwRp-g0-vdQm5VU-B5yhktBeT_7p_P-yu1zKqssqpupPo_GCv9nPjLJTJ2iFaZ9dwGGIvj5fC5FMaACv4OhM_mMeTQxRshwCStIZ62d0JHQUA8c_D8_GXJxiHQirC_o4kdvb6MubLFw9JbFYQWzc2gBN9Jeh3KAxlU6wNG3je5HoLbGrkXbEjqevnU5RAErZF42CJuAbnoMPVeTNf3H-1o2zLiCrrBPlSLkaXTcV9PM4Mi-4cgbFCkaLg3vfGxyD48rF94NhDfpP1fkEzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=vSf7gko4lo-erAiP5-JnDcwCy6GSrWAxaCD6pSoVAK9Ap8bI_d4sPO61JnwhvSMuvxf1y5LR3y_W6KHEY7eLwjTF7rrpOT7yNeNfMkXN8MXXzrj4TbeS47hBnXNBoCHliiFINvOqOfuyED02U6UYPAnvDqAGsdAEfwxIRfbqz0efD70vwcSstkgfWetHWhSlLL89XhI8dVlQWJqxSsiRd2alHidrMYyx2eMa_aEoXFO0O9c3IlNomxetm6I5tSmse9nAgNt7VGYkwvs-AJO4iypQUcV5AGv_ClDtM4osUBfUqjviqsq3Pv1ixHxnKjHrruPPU-hq-LKM1QHZ9tKdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=vSf7gko4lo-erAiP5-JnDcwCy6GSrWAxaCD6pSoVAK9Ap8bI_d4sPO61JnwhvSMuvxf1y5LR3y_W6KHEY7eLwjTF7rrpOT7yNeNfMkXN8MXXzrj4TbeS47hBnXNBoCHliiFINvOqOfuyED02U6UYPAnvDqAGsdAEfwxIRfbqz0efD70vwcSstkgfWetHWhSlLL89XhI8dVlQWJqxSsiRd2alHidrMYyx2eMa_aEoXFO0O9c3IlNomxetm6I5tSmse9nAgNt7VGYkwvs-AJO4iypQUcV5AGv_ClDtM4osUBfUqjviqsq3Pv1ixHxnKjHrruPPU-hq-LKM1QHZ9tKdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1EvrpF1WU6jxbnVliFcOsXGonaAUNdsYDBs7eZjatZtzmqHer2UATIXkdLJGmLQ2WrOGkrRo41UPJWRuJehY6pDYQbLPBO_BrMU_DPGR8m4RmfVoExRTzZ_qjur_XR2b7Y51-EyHvfacwT0Y8dI15qPb74YQXVWoZ_GXBYPaMF4VQO0ycH5zwsGnqdewA8AW8e1Bfwx3ao8Crmj32nrLsavGLvGyvQczS7V_IeQMYNHJ3UNNMVpCD3yasv_rLaVMYtbAKvZZEbN3TUJEAsB68eoJS2jIbK7Sf79YZ2dtcrZOzRvtzPX_Wu1QhS_yv4zlYDbKVVm5rKUL9P5bNnDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=Kr7WTUYyD59LB5Rj5tHiQOYyxwEApQmJvPTYDwKQlYPkHshCj_IhTi9CELCXl8wp0CZBNkdU3Pxv55lrNbUO_J7bANm479EKLF_YR1yHMQADTwxMO9jUoJfHJmluJxMyq5wzjE9-0Nsu8PbWTLPMcS8jXvdCpBJytMKiCVrAa88D_ZkNceuoHtkCWRz9cUgToN7Pggfj4yw99k3TyFi_hj0CnvaMBaufQEUb0Ji5uJaR-8WuQf5A8-mBYE84n1JlVmLZr09rXK-HtLmDOYnw7pcINivAQBzXHtCYioIMrEwg9jyj0mDZgnrO-OCSLuM7FnGzM3LJxXXwnEoW1ovpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=Kr7WTUYyD59LB5Rj5tHiQOYyxwEApQmJvPTYDwKQlYPkHshCj_IhTi9CELCXl8wp0CZBNkdU3Pxv55lrNbUO_J7bANm479EKLF_YR1yHMQADTwxMO9jUoJfHJmluJxMyq5wzjE9-0Nsu8PbWTLPMcS8jXvdCpBJytMKiCVrAa88D_ZkNceuoHtkCWRz9cUgToN7Pggfj4yw99k3TyFi_hj0CnvaMBaufQEUb0Ji5uJaR-8WuQf5A8-mBYE84n1JlVmLZr09rXK-HtLmDOYnw7pcINivAQBzXHtCYioIMrEwg9jyj0mDZgnrO-OCSLuM7FnGzM3LJxXXwnEoW1ovpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6L3yB3fgvzI6n8tH19PmFKIoRPAt1rBvF_2udbYBhmD4cVeFt-lWI8251ubQqktzNEOvnayE1EF2T-UZn0bxj-fqwOvO45FPMRokll2Y0i8D0R0UsIItfetIIcNRiC8ZWk9G0YM-pECwntt0y5xhQiSxNjDNGGe_QwGoGF1AQSTdo99c46c118mEtwVz98radHe8BVcB7RDt6gb-tpAvzfZtAQeK7pKnL2qxh3zlSutV8zeupxknJY6vo_78HWa3MCQ9y3Y_kHUinRWL3-eTr-Iu7m8FpjNI9kNvD7VQxotxiOaJ8JaVnI_kHq95UGCDYJ2FzUEdr3sNZqlfBolcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84542">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84542" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84541">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYUUxH4CTrRocXe7KE7NgZJMTGz8jslJFsKu2n4eU-DFB1bxOz8Pes4rml-C6AszAAqyGRAlABdl1vNjsHCghpk7cOap_91-1x5iwpWJrS9TpSSG25-buN_qPyae_n0lC9mDA-meloKPr6OvEXBGmPsp1eG67-FNkFvtltnVFRWaj37xiR1reqP3nj-t29iFbMpcqYs9xx6jtWslnQnJhynXRT2z1t5ZZ08C_zkDVHeax7NY6kagAznw7M-tkrndwRnAqdNFuzDalEvkhwQrOQnEExcEGDwhZkZ_9vp42mZoOos2Rbm-jvvAC07rii54kNYnTjMWEZ021vPICOFtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آرژانتین  - بنین
🌎
ساعت ۲:۳۰
⚽️
کلمبیا  - پرو
🌎
ساعت ۳:۱۵
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
آدرس سایت:r15
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84541" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2unE-NkfdaML5ALsZ_bRYdl2U3hZBqR3EINMDtFHfCfrCTizsVwC9n7tKZ4Htk2BTlb4TXgqXcpV645Nl9TdyIfYdt8rvISD79RXlZT8smc4zxmT26S367SJUYgfS9QjAEIe4GNMONuiX194jFVopjMld4oPWju7WOKtT6V9GCeqGtFuS2ISiEMXV0UJXJ5-lK6u-GI5T_iVlcSLvBERciD0Rq14i9-2GpINK0c1rdsfHzkPGyqQopswQ5uaRMO29rrAzCEipiyFba81z4a13dwNqtjpeZgMeMB5KmU1BOsMncVKa14_z51C2fpv-_E9XBZ5yHXQDPuDo4kMcrPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwon2WTRiW9oRmd_yfpu-M0lGsKxZlbL14Uiv7PjJTdH3-OLknHr0wE4I0vNNtJyXldQHhlou9KASne_aH5j0n7hGOXyeseQK0ereA4NQ0A2lus16MtQa623t3BhA3WNYdQBmzQWDCa2fxB3Rkstn5CQwf-_KItFcrkBD5emAhkK_eTYrXGWIDQFrC0czI-cfG7iBZGoo9DYUYEbYAtYyZvdQS3FNQNtwoEaxWr9O352Xy5lEG1diyCJIPrh5d-EWR02lCYC0XC6nQ0a3_jhg4xKdoVQJuc6VhMuTgtTissw7hh4Ocrz65TZGjbuHdrlAuxQgBqvKvUzz4BZfvrdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=J5fGIaUYUzRfMFCxJwyloFjn5aUzQRiUSFFmYQhxsrWG6paNmkfHQQLTwAFTfk7dggGK8Ruea68Flnh6La0AV3dcdgmOlycdD_nLP7Hsh74lNdODgTXvhjXFVkqBtVR5DBl2vrTEvWZfDre9llgGDntiU-hRVBu9MGW8yOD3hP5U3x1XZH0IpC9vlT2S_25I0BpeXP5lSFxslDwn5UAS5mdnlL_2mhA6fpD18gMcfSEfG0qbZOcHafmYznpEZBxBu7KF2aa1B6M2ouBJLVXdd1LasmUa03Z-ixckBStzbkn4ENwPz5O-Nq2_uMfCx-beXcfG1LDeI-bVvs91K-mk8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=J5fGIaUYUzRfMFCxJwyloFjn5aUzQRiUSFFmYQhxsrWG6paNmkfHQQLTwAFTfk7dggGK8Ruea68Flnh6La0AV3dcdgmOlycdD_nLP7Hsh74lNdODgTXvhjXFVkqBtVR5DBl2vrTEvWZfDre9llgGDntiU-hRVBu9MGW8yOD3hP5U3x1XZH0IpC9vlT2S_25I0BpeXP5lSFxslDwn5UAS5mdnlL_2mhA6fpD18gMcfSEfG0qbZOcHafmYznpEZBxBu7KF2aa1B6M2ouBJLVXdd1LasmUa03Z-ixckBStzbkn4ENwPz5O-Nq2_uMfCx-beXcfG1LDeI-bVvs91K-mk8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwlFs65Qu5ozmtNOfjz62zW-jLd6CwWzy4c4yquWbHz3BS7wcu3on4d-ZF_7HJjQXJOoccfkO0Mb35M0ASS7OlgrZsrXSv4rihUDpzg9rIBhR1HRebDZp0kIWRiA5fxGIPjYyXqKxVw7LFbxkNEpjjwU2yhN_pwVQr9LdN3ds3ai1n-xl-42szNx7TqazFirwToiJgKXxl6zp_v7IBZsTcdxWYEGLahhhp_4hUoGRnfIO1XueX52b9nAaQMAND7A64qq0eIhoK4QaySLwrhGBjpLL0ph_dlloALjXqkmQ8EscrTxekqqnxDa0gjgHqiRFNHct3kF92vIvqnUmwQjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4eGmfcZ--1Fhyet-8FXAnqYeMkgQrY534NjzW-lw_MWp1DcaKEKVRUidlANVJ_Ah59xImvuVnOhIsUqE-tZkd9LhB7KsmT5xnbOLiNM0GaKWWPU0qSZgibIwdC6g_P3ypPku4_BxhKSUUDwBoV0bVuVKmp6kGtferIF_m_zoPxA77qZ_qxhc4TY9d3SdhUifLOJ8GOPNyJG45Ns0xHC7nfGaJEQP2OPbuIaCXyVGqFqFRepCEK0YS6Ocome94zUnJWsRw77c2C6AuNkku51Ig5MeXO5atHfCA1wxCNq6D7x-kR9EHoVlab8uhmPyLBMTmkWHUcZK05gJkkoZQVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVyjtDISvFV-TGG0Q7tgDc0tGFcigOIzWX9Xw8ow0uKo_4hIuARZSXwHYYwAXubhd1KrcLFa5PVRmswaDKlyZ8E4dHsC6P5cL6DPSUzU3wTWsSWmlc1S32Hl7LBX91SNbqbkuGCNHYUUK79JcKgu4oCXWtKxpXgpH9AgNAal6CHCHKS1PwALwBRSujQaQKgC6Jxkrrm8vYia21gr0NVxFLAysOtzwhUNlmkFpRcWtcyg0KWyidObqrBf0NGuQ5qv3LMSFnsYotNOkUpz34DY6X6eqahWleSHxMArHUj6YzFiTxm1F4t-dGYYfpFVT0uzgiPQlnbavFgRuYg8iStrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlfBI4oVqz4E4rDVC7aQEm_ro6_Veit9S_gAjCsXWZvypjzSf-xr7642IXFVKeel2Z_3bv6swEP0fEipx4mv4mAJLo7H2NZotEH72gjaHm60psXG0RRO206iLnhH5sQGfXoMtFWVxPHpFhedM5buJ5QX_5gxIT5S1DEMrC2Xb5UTuiCJkl6oTexyaeB6HI0J7GWn8zuQpRzGzlJpLpu0LcmZ7i_QNiGpoe8_B1hvt1eiR17if3bVcH8dDj-xo-h0rc2UGiwE9S_v0TTe2p0c14PEkxlwdQW3nCLpw9qW1UE0DE-_2k05sFG-WxUyBiCYJ1ImsvAOUyhm9oLqq4H1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASCRWv-Yzw9K99SqxxGdH1L9L4_MTWvRKeTfwy1g2jXNe1lXFG4Ghp1Apo_QhAUcPsl9GdOkJtp5yANGuIBzu-xSwOAqHLQ3YHa-RgdS1Aao-1TASE1mOpuJoc3TL8pBjjHMcFIzE6sWIob58DWqmi-bAd6Ahm0DqjerubRVXgP91fyj6xwntgCxa9Oo9FWB-OP1Q9ayiTnQRr_uMhqFETLiseaujg6d4sZ3gEtK-BRQoD4p8EieSuA9rFjhSqmoeMBhKRWR60K40kw2kC9VypuCX3NmTZiNBZ_W8kpDjpSDoezVFo7RVPcbvrrPR59fEJzDK4kTh6KGZzJhKUIiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns6JKiPKSWurqiGUViO0jVFnqoD7zccIxsddjYGfliirSLBe-P-_AcZOux-SAMR-RYv_pMz4b1sd_Xe8qMOf3mv_RL_rf7-NgNG4Q-apAwC1_Kj_kkuCQJOV19l3T4i_lxdMfDH12vPmVGvOOA8EwKZMvXNMZXB0X06NpWVabksmQUlfh_5tDv1PX_8N48eAF9t6LFLS3RCtSGkpGxGXPdEE0RnFNFYF_PCZXtSc-l_2Q9L2GQBfa2l_pKGQ6t-RKt8P_g1gAsC7QNvfAYbnTgMEEWbO_ABK_egDU57PA8yHws_G6vauA0fpH-hg7g8nKWYsSswfI3ZDHQ7-W1LJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84516">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gycULrQT5efFQB5c-7Sle4g2PmAAe4R6Cvf2JJqP6lONvCV1AgCkvY4nojS3aEOsmwJH1ReVZFPjMzKJ0t0A1ibL7n-r73BqcM7gNS2STBMXylh6PRVhil8qukUXuvc5yksdNid-WTMO6eLaq6E4sEesQSpnlrWAHqsESCF9Izgr1hmSiEB7_PrWpYuVx7nsFdv6dDZQvvmBPYgOLHjZY6RJfJ6_h4ODr9DDGAiPLLdWHdAc4TWJjuzR6WrwSt3A6-CP8wpq9K3Powe8me90SFBwx9nD6iaVeYcOj7ltdxjq4Ll1WHl-8LXHSK2ZAlfhbtJn7c83wtJkxXr32gCtew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلثوم اکبری که 11 شوهرش رو به قتل رسونده بود، به 10 بار اعدام محکوم شد و این حکم به زودی اجرا میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84516" target="_blank">📅 21:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJMY9Qs6z2OiaY7Cuw1In8AkavbfGAHzPftbLwhsb61m79yrmIeAxE5Yu5Y-V3jQzObxFd6F_ipzyndOsXdoL7m-nS8RqmaOV0YBoo_pt_wHL9vFiuqYTG5gI6p0U9rFMxaU2bKM_FC9wRL1oTx76yStaxFiO0_xmMA1elC9ejv211T4oShpRTrUaPrqv_8T6VcRbv4F-cnHMhtT0FwNI_iRYQTGQ0RpPlW45j4GqyYrQGLOZVFYR8rsjsLfUtZVegOaBnVMPgQkxT2NwF1xtLsIIH99jvHIMEEpwp4Ov_qV7NxH3OQEFY523AOV9Bxk9KfCyAUMpyyx_yzvzYIc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی انقد پول فیلترشکن کند دادی؟
🤨
سرویس مولتی سرور با بیش از ۵ کشور مختلف و آیپی ثابت
👌
💎
سرویس های پر طرفدار :
💫
1 کاربره 1 ماهه با حجم نامحدود : 148T
💫
10  گیگابایت 1 ماهه : 45T
◽️
-همراه با تست رایگان
🫰
جهت دریافت تست رایگان و سفارش :
👨‍💻
@storkvpnsupport
🌐
Channel:
@StorkVpn</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84515" target="_blank">📅 21:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پوتین و پزشکیان جمعه با هم دیدار میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84514" target="_blank">📅 21:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Waiting</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84513" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmVvSGVgZBF7ds98l9soAM-7TtGYdZt1E6f-n2EU1F6cGmzVFJasazSq7eti06-9mccF1kPP7_Nkv02y6fs1vc2fbY_Jxoh0CsSXpq_diWa1VjbD91glR_l8-ZtFJv_9_hAFFe180qjDMaSGie5aCBOEmMdjtItrGTEV-EZv2GPzKxoGhIXcPdxOsC0us_xzCi4B5mv6K__MCLSwaHA91RGtjKfS6dYRfmCYdOgrwLew-EIW0DrtLea6fgU__QX-88iJDVPa5a3pIjKJ1nhVT0rnb33qTsvAvMkDGfw_2LD9H3TBEtun9LFzgtdQdCkL-IlK9_TUJu6XgT9F8oU0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام ویتینگ منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84512" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84511">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حمایت از آرتیست:  Download  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84511" target="_blank">📅 20:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84510">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ملت ویو هاشون میریزه میرن با یه رپر هایپ فیت میدن، دکی هم رفته با کسی که مخاطبای رپفارس با اون فهمیدن معنی فید بودن چیه فیت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84510" target="_blank">📅 20:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84509" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvv_aRoFLSNs_wngjv67-S0o50Df1Ka_GuGU1TmVGNNdGcJfD7HosYDZIARx8HmZhxL5rXpowHPxLNk1XK5851IYcC4ZdtOwXc6hdBx8ozTbk8qGmRM4aZ9Kjpi650RV46n3lFKNx4yxFoxPLuEGopcGHhwjzzIgXRJZ4qv8S8E1Ce5yekYsq71xsaHtwp5CbiHJvSodVKRo9ytHwPpKa3gMBiFNUG3durijvt1k5dpNNxg4Vdvf3zuhzveF1svEiLibkW3cxlm36JNGUIevrYTmjBxU1iyvwhRc-XUmzUHi5Kpeo0Vd6PjqAw6TkZO3mMBZms9V20walQ7GAnUeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان پایدار و هیپهاپولوژیست به نام "بچه مردم" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84508" target="_blank">📅 20:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=t9ANoAgHj0H5iVyGeRl-UCjQmiTDnZ7ZFADVm9bNMm58C7UrTqd-KYL5v5mrNpinaj3fb2D0N_BimZX06TOpcvbWFZHWN7tiROhq9JN1B-QqQIP-RuIt2dMqgb0CI4IQhXpbLGdVWJ577XBGUBmrrkHhBfwHDnV1Fr2oHfO5QsZRzQFhn_VSsvlpxoK0bgNJtxXbh68ZxpnbrH_bL7W0WaB4FMwtRytuSDv3XcywVy-MM0LHapDWAYeu7K_AlFB59TRrDgCH1W7WEAAglRRbophTb_W2c7UD1ZJ457bzJlmlkODD_XGaqU__nFsKupTB6gL7-lhdnWKYYBo5_jdu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab91fa8060.mp4?token=t9ANoAgHj0H5iVyGeRl-UCjQmiTDnZ7ZFADVm9bNMm58C7UrTqd-KYL5v5mrNpinaj3fb2D0N_BimZX06TOpcvbWFZHWN7tiROhq9JN1B-QqQIP-RuIt2dMqgb0CI4IQhXpbLGdVWJ577XBGUBmrrkHhBfwHDnV1Fr2oHfO5QsZRzQFhn_VSsvlpxoK0bgNJtxXbh68ZxpnbrH_bL7W0WaB4FMwtRytuSDv3XcywVy-MM0LHapDWAYeu7K_AlFB59TRrDgCH1W7WEAAglRRbophTb_W2c7UD1ZJ457bzJlmlkODD_XGaqU__nFsKupTB6gL7-lhdnWKYYBo5_jdu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق امشب آخرین بازی ملیشو میکنه و همچیز بعد ۲۰ سال تموم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84505" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=DLP4vCdbwCsnrt_TAOaWY-YzAjSZBuQptBmEKVU-tulNnfXE1fawH9oF8nRI3Na7LBmKNJrsJE41if6XzLTRkR1J6ZtiuChFyQqYo-XfKVlMI2ZZWkDmM0QyxcIvh7ZCPRPVd_VI_KWjW83n0ROKat-JWC9DetEHdSFRU3OI7BmUxFLOisYJ2eHm2HUzFduEjsl6QTzXtPAX_AGYZn0eJCQeA2qIoXZxDs0dt6xnwj7odON7_IR1v06ND8hR04dRY_Aj_m1jVJ0AFU9M0XPurqesz9WcxQGH4YQBrFc7Ip9LxZ2KRljHxqyoQ03JqEq-cdwWHXLmDI0b--GtcSoCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=DLP4vCdbwCsnrt_TAOaWY-YzAjSZBuQptBmEKVU-tulNnfXE1fawH9oF8nRI3Na7LBmKNJrsJE41if6XzLTRkR1J6ZtiuChFyQqYo-XfKVlMI2ZZWkDmM0QyxcIvh7ZCPRPVd_VI_KWjW83n0ROKat-JWC9DetEHdSFRU3OI7BmUxFLOisYJ2eHm2HUzFduEjsl6QTzXtPAX_AGYZn0eJCQeA2qIoXZxDs0dt6xnwj7odON7_IR1v06ND8hR04dRY_Aj_m1jVJ0AFU9M0XPurqesz9WcxQGH4YQBrFc7Ip9LxZ2KRljHxqyoQ03JqEq-cdwWHXLmDI0b--GtcSoCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکارترین پرونده فساد توی تاریخ ورزش کشور
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84503" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رایتل ورشکست شد به مزایده گذاشته شد
شستا آگهی مزایده عمومی دو مرحله‌ای فروش نقدی 100 درصد سهام شرکت خدمات ارتباطی رایتل را روی سامانه کدال منتشر کرد. ارزش پایه‌ این واگذاری 130 همت تعیین شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84502" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nn1IN9kuxWtQYiJRkkKS1lbgXZZ1Uq62JEgzqVHLqmkmHmrt2qXONkRNuLISc8D54PMn5SYkjm-J8XLPp-QHelfO57H96TbdJs3NaVtdOGRCoMJFjdnfOCyW84jBjekC3JpzbEK-53X3U2pMTUyVoQ1ROafdZAG8haZQfxV7leFeya3IJxn0JL_rBSXztJtRFFhO5GCE058gcoFSP46XcHqAmxAFd-Ul6VDcayLT3gUpDyfd0Yj0oaPUmfIFMFyVGr1iKZ0c8kx9VFUS3fKsDCyb6PEVGi7YoS-8qklrbBEZml3ZnV11LeTZzyYHldYA6YqxDN2BFOyB_HDMnhEV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=nn1IN9kuxWtQYiJRkkKS1lbgXZZ1Uq62JEgzqVHLqmkmHmrt2qXONkRNuLISc8D54PMn5SYkjm-J8XLPp-QHelfO57H96TbdJs3NaVtdOGRCoMJFjdnfOCyW84jBjekC3JpzbEK-53X3U2pMTUyVoQ1ROafdZAG8haZQfxV7leFeya3IJxn0JL_rBSXztJtRFFhO5GCE058gcoFSP46XcHqAmxAFd-Ul6VDcayLT3gUpDyfd0Yj0oaPUmfIFMFyVGr1iKZ0c8kx9VFUS3fKsDCyb6PEVGi7YoS-8qklrbBEZml3ZnV11LeTZzyYHldYA6YqxDN2BFOyB_HDMnhEV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره جلو چندتا دختر جوگیر میشه می خواست از تو یه ماشین بپره تو ی ماشین دیگه که بگا میره
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84501" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=fPutQlo2bPj676hsop856qOqrOIS2BkpT7QEGL8y8BkGLcvRr1SFnCjeRPZ7glZ-v1qd7rnqsLG6sRPoGr9SRKxaZqoIbStS4wHId-ScEae-cDrob0gqG64eEYmIhc3tdpzCjPNCDJWYq90AW9SQmYlQ75oTGovKfE3j34rzi3uxyL5I86RtJsEZNaGKw-J6QiUkFiuA5WOgfxWBWdzA01DDsN-VIgeJZbf4e5Rp5-Y4FpNfK2W5PaZqW2rX8T7obnLh686u5dvhB-3Q1gvfqb_Jt_gyqZIYKoptlBv48h9v9CdNPyfAkEU5rsnuQqZN_lIYflfAHNkLM7qhDrGKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ea14d958.mp4?token=fPutQlo2bPj676hsop856qOqrOIS2BkpT7QEGL8y8BkGLcvRr1SFnCjeRPZ7glZ-v1qd7rnqsLG6sRPoGr9SRKxaZqoIbStS4wHId-ScEae-cDrob0gqG64eEYmIhc3tdpzCjPNCDJWYq90AW9SQmYlQ75oTGovKfE3j34rzi3uxyL5I86RtJsEZNaGKw-J6QiUkFiuA5WOgfxWBWdzA01DDsN-VIgeJZbf4e5Rp5-Y4FpNfK2W5PaZqW2rX8T7obnLh686u5dvhB-3Q1gvfqb_Jt_gyqZIYKoptlBv48h9v9CdNPyfAkEU5rsnuQqZN_lIYflfAHNkLM7qhDrGKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که تو سال ۲۰۲۶ ایرانی ان:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84500" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNw49DcjXa9XY5Z6Y6PNHCdwApOUgiykYHwebPHjBDEftJ-EAKgKuxjMe4wTenBFfi9PLdmbeLCj-PtOQ31wPJmFKxzkpWNn-8se_Nw8rRRbqYyUYEryvid2rA4wnI-EYecY6SsaB85CnbDfxWpUI51Q5QclpLmDf7G35K53_TVq7XJzgZ8nBnoQ9U6snogYNdcJu0QuuGZJQbnlo_yur6a2VYGpyNn0eThMDpGL3L97LpliyoTSSTVVVFkLNJt6RMWoYcDxLf28oacPc-sgdCE7ytHLQ99ARZ1QC0gXrGY_q43ZEGs2VljKc6W7cjLiBr8iLASxgm6cUfSN5pngcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا نامزدش چطوری دلش اومد دل این بچه رو بشکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84499" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=lw1y9hwdGbmbk0prYyCejT4kgeAPgvGvkCV-ejOEfbmJ6Ux89XxfRXVDVIbJW4mt14Ce0zeFgA93YD-fZxKHxgK29GjxQCB5clP1SCbmaOzPMXsIkreGa9qctDYAAUXiF6WogSc6Q79hIW6q2NO8WioTWUt7ufbgQg4Cu0zVC2hQthI7PVsysOMs_Eca-ENZn2wocm1uxSqj-KQt_4NCrmanVMpXizlGffxcKg9p4ig5SdstqjyfWxfGTa9sU3X17VQr-VLidUhNAsioOOu3nV-evc5GSbGD6hucGM92ZmRMT_REQwwH8N6qrKGlJHOtcoRR59qj4g2_m1ck4yYL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=lw1y9hwdGbmbk0prYyCejT4kgeAPgvGvkCV-ejOEfbmJ6Ux89XxfRXVDVIbJW4mt14Ce0zeFgA93YD-fZxKHxgK29GjxQCB5clP1SCbmaOzPMXsIkreGa9qctDYAAUXiF6WogSc6Q79hIW6q2NO8WioTWUt7ufbgQg4Cu0zVC2hQthI7PVsysOMs_Eca-ENZn2wocm1uxSqj-KQt_4NCrmanVMpXizlGffxcKg9p4ig5SdstqjyfWxfGTa9sU3X17VQr-VLidUhNAsioOOu3nV-evc5GSbGD6hucGM92ZmRMT_REQwwH8N6qrKGlJHOtcoRR59qj4g2_m1ck4yYL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g14
🅰
📎
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84497" target="_blank">📅 18:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جوک برتر قرن
احضار سفیر فرانسه به وزارت خارجه ایران
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84496" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84495" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیدین گفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84494" target="_blank">📅 17:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8dqCtP-3VERUXqQFd6xlwa8sCWM0BtuIbO1l6svORqj28ymITzVGgY3rSuzMM935lSEL8Wxvi8jXnJ4IQ7tUpDnoDUHYXj-RB8LNuWUKGp5eAY5_PRu2Het1ENTCrJUbOj2TrKhBWgRihtuK_6Y281Q952DOyirzN2_d-1Gdq0AwysX-celKjJxvqAc3QfZsc3JsUBel8cLTzhHwHoPwqU7E7XBp0mZHmdfiG8sIoQcNwdI2yw_fJ4Hf03CJOclXTNLFNBzQkwIuOzCRM-VkUmd5rCLeuMO378CLQt5GWlHOqM7sCPVfGs8rWL-jaST8BRIUAOU2f97YXTuV-i67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا شکرت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84493" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGiXOZ6EL2UunnUcRN4BnBkbuhnm1_z1H_thpe4t0aO-zn30OuMwU4MzZUak0HWXA0fls5h-kbGzGoS2R7cn0HSoYxp9tXvLHl-5_wS_LpVp63mZIzXTC36dylwUySNQEAKISf_VyozTN1bArRUdeBflUeDdNMO_h1v47tuaZEsrMut5pbdqiMVspF8vp0Gl83JnyaUlLzyXkmSTX5CSzvuJxtcQlB7_BMn6kBpRnhcwanZmr1vGgXWTY0jFsfJhE8cWfS_rNZ7WbvolTHaGmS-MdEfCiza6KhGvQAIQoaXfODxpMYYkzYjK0vNfwuvBrBqpb3_iwx7JvlsPBptPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی فلج های مغزیه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84492" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
👨‍❤️‍👨
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84491" target="_blank">📅 12:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">من دقت کردم ویلسون هر وقت با ودکا مست میکنه ویس میگیره، انگلیسی صحبت میکنه خطاب به ایمانمون و عرفان و هیچکس، هروقت عرق سگی میخوره فارسی ویس میگیره خطاب به فدایی و پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84490" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwUhfm0nbUb6R57ZCBOPhw0sODYkDN1YWW14L56Rt1X17BAhk6CAK_6i6XiYFnwruhdZKmKjotiLB8qk36569RudrIJiS3qGnoa5uoUKveS-GuzVm_6OumJ1r_9lpxP6gmI6lR2YDX6CTZdy_p1Q2ImDb-CNUcd8JDJBEAiSsmwMjBvqvBdsUen62BytPImiZ20nvAaUqu_lBRvu8oZnYC6kWOJcF8OeJC_XaOxGYYdOrA7iNU8lfel1OGC-K5N-kFdxe_hYMux0zJOZOnkBdDao51q9HxsdVXazWdDsOkt1J4y3DtE8PelP9irIWZUb0e8b02TXpg4BGFuMX_6LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزار باهات رو راست باشم عرفان، همون قبلی ام به ورس تو میرسه میزنم آهنگ بعدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84489" target="_blank">📅 11:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هرچقدرم از خطرناک بودن طاعون تو اینستا کصشر تفت بدید من یکی این سری ماسک نمیزنم، کیرم تو این دنیاتون</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84488" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2951b20357.mp4?token=hc-lHJ75kgqyqxg-bHrzD7Uk3vxrkL03_8l0tvqMES-3u_6aRrXa0h1qrPK6MBTHV7lHWLUZSzbAGIwyu5Hba7mAWzcXQXXTCkbGkLGfxSiygYsEHOZVN97rTdo5p6QkEWDrvcyKKN-3Y5vru0w8dH542gjikWEEG0Y2_LoR3hP26KhtBqR_pmOHT5GRVYflBlH1g29abyl32o7aCpkNXpWW_GXxZ9YQ4G2gcgxahR7333RUfUTDYh87jdabnUg43BDjI-cFnl-s0i5NaDgJvPj7GItC5r2GlCLUJIj_J9MF3_T7hHzIrHF7eeWzn6Pzx5QfdhPWEdHypsdqkqd8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2951b20357.mp4?token=hc-lHJ75kgqyqxg-bHrzD7Uk3vxrkL03_8l0tvqMES-3u_6aRrXa0h1qrPK6MBTHV7lHWLUZSzbAGIwyu5Hba7mAWzcXQXXTCkbGkLGfxSiygYsEHOZVN97rTdo5p6QkEWDrvcyKKN-3Y5vru0w8dH542gjikWEEG0Y2_LoR3hP26KhtBqR_pmOHT5GRVYflBlH1g29abyl32o7aCpkNXpWW_GXxZ9YQ4G2gcgxahR7333RUfUTDYh87jdabnUg43BDjI-cFnl-s0i5NaDgJvPj7GItC5r2GlCLUJIj_J9MF3_T7hHzIrHF7eeWzn6Pzx5QfdhPWEdHypsdqkqd8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو بخدا من نبودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84487" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84486" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxaocOn7GssNvln9rvfI21JZCzJByW-QzfnKJRERHP0yxJTy3sGYnaQ0rPgpJ_ZiedJvWwJfcfQmukpnXaQKtl9n5Tmo7-8k6ugdwz729EaVwlZ101CqtY_TrWH-LyEZXdvM1sY6aLygHSM3-A-H-SYfKbrB-tV0oCDNEK7OrJlO3Uqit06qQn911tlz39p83S-5mc-End-8WC4KU3EWQy1y0uhxDsOrINkjHSxzTNEKFXwwFVF86qf-a6EQiJyXMOCv1dbTWc_TniIznK0tAjnoL0CQLRHI6kEF7WyuQgQJyijPkTNfOfF9gQ3oQFBHXCtIYKaN04L0SazP3C6HPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
کرواسی - اسپانیا
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - سوئیس
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R14
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84485" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcB5xIOUFUw8Yv8_XImYOoRV5tGxis1-RcHWN1kCdSsPdnBfMvhfxxp_BBWCqFixR2IOjoAtsmW3M7gKyvchyo8tKSxYcojxcNiGM-CHRo_KcMbZz4lV5Pw59ZqptGYuBmMg4TT03r-Ppnm-qL0EYxqfGc9SBRM0kDL7_8CYro2OIhuNujvBLbf68IGUw4EWYF4ZJaea1TvN5-gs1dG1lugdI7ZR6dxNmCDZ4ppJTYP55apt07Qy5PLzcYHM1DRO8B3pr2tIwHq7qjBamKp_DOLdJ4UxRbFrtKiauK3PJKDzuZX2DRE7wK-_LTZHCtGpZ6wxZ5BlsEM1iqx5WuS4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLo-XBSLkck-KiX9YMJDsBiNDmpATVrRHJ6m1vgGeKfZWv2Y5bDZDjqB9zMh5AFNbMUv9_npYUDrgC5aoR2_wHNGUPtduPeZcre7Fc-8oxT_InFDgfOdD1rgqbOzYa8-SZoA6SW_nLDo78XlY92MVw4PjjhknwEy8OgWrkgOLIHwg45nBBfTiVpznpIz51GS-OeG5Efu4Lk7vmH1i9hNPaFAp3mIjZNZFS0V6hmquugFwOGEBpxDXUtsLRAOnI-9ItrYk7C2K70IwwM0Y-05xmRQf50ICLHqREXxANr6IJDXLILFnJwgNxQqsoyUJyAVPNgOw8qmalqKpER_4DFk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOqO-vHVhE6h7Uu82w6eE7O7MZb8tmYQy_QEoDUFndO1gBpXHQ3rlbx9gVuKHOw0QappWu62Yhbcy_yX4mB7GfdLjjcq81MepvFA7T2vmhIt6RTswlMsfH8xhT4yQzoM-SGGkvxwy3gW07XMwi7nyrv-eyGVzdpSpavNueqIisH91XNR_atKAbHKTG6XIUYdVnm33J5gk49saDMmYdOzgsOYS2vucCJNU_TtjWHJ7mWMxGJhfgD0EYRcFz4RcokinfC7x8CPaM1m8cxcnqdl-zR1UobtJiB2-tLFL0Q-TEXqRKAU2AKhnfDice7nb5LkjtB4bwTuexlvtXRmJr5GFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4mO9S68sQR9ybjuzoqhw4SLALcI2BfN59ccm9iB-ghartp5faix0Nk_abr5cdvxvm6pp_To2YgNtl5ZHIb06pj7RnmKH9WN7t0VMVzfQcNpgm6l_WSSTC16amiTLo0zsznuQgEHRoftfkNOI0NWuBvIQtRVnX0I6hzokFpFwAPFkrbPLi0grP0cIMV0hr-yhyv6Nid2gmphSbTB1ze3sKtcYP2gr-PeuzwpvIOwtZxZymRKjMhtr0riuWsICn-FNYdRQ4qKj8SrmDFjcAmI9fBbMCQtDQtO0Ob4c3rKvBJN8MV_dzfrZYgx8zCqEoDaAeAA_jpLid7FTK5JVjo_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
