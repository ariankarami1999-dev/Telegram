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
<img src="https://cdn4.telesco.pe/file/YHQZN0z1707El812QT5YjPaelTgvKnaV7QdqERTlfoZ22OW5IGIvK4TyHKWzy0OA-6jCJ9SGjiGTCFCc_9HT0qbYEj7ep7jInbB39dCQAQPLe9xYmxC9E8Mu56BG-WYa-DYgq-Jvt7t1pOYaHoVdp8xwEh9Y6lFSLCjIT5JYpHVXexTSYic-YXxV1VOCa3xQfHfmUXAsRZA_gA7SPx9GVVQjpJ7DWE4e7dnoZw3lVBq4KSiFgi5kZYNNpSOo5XWc1dpXqOj44DPDNLIsZ64QD-dtmaCpeoC0EwBSUv0zHZgO67hxf9RUw2EEEUP0YLN4cQNolsDC9gu--aNb1NjAHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-697491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرنگار جنجالی آکسیوس، افسر واحد ۸۲۰۰ ارتش اسرائیل از آب درآمد
تسنیم:
🔹
باراک راوید بیش از آنکه خبرنگار باشد، افسر واحد ۸۲۰۰ ارتش اسرائیل است و شاید این قلب فهم ماجراست! نیوز وان (news۱) از رسانه‌های اسرائیلی چند سال پیش درباره او نوشته است که راوید پیشتر درجه‌دار واحد ۸۲۰۰ ارتش اسرائیل بوده و با درجه سروان از آن {در ظاهر} خارج شده است!
🔹
مجله Vanity Fair آمریکایی نیز درباره راوید به صراحت به سابقه او در اطلاعات نظامی اسرائیل اشاره و حضور او در واحد ۸۲۰۰ ارتش را تایید می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/697491" target="_blank">📅 16:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦
می‌دونستین این خطوط زمینی در ایستگاه‌های مترو چه جوری طراحی شده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/697490" target="_blank">📅 16:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1_WSJ_oa0vxsYiH_pVNOCnvV4Iz63JtVZFJyGJVNlML1p_BqK-EM6RcoAi4ezVzTKoc9MG24IzTeCKPssykBkBQcprDKvTar5XDY6f1MgyOAa8rbIKJf-DsNJnR5Z1TgRKOht3_1HuXYKaKQR6HlFzw4iBMkuxGtdb9DFd4Aog8TtXdTiDNl16ZrcDJVJJyetdf03rxctfr0cQWA7e4Hae3poy73Pc9JZdYopVSzGf4lEWpv3P1qtBlg5NNi7DSZRQnGa_cBZ6hwTsCo7PIptimF89JOsuWqIGz-oEfcyT8kfRu1HjzkitCFRShsluysgyCKzpu082pNcpMmyRRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ نقطه راهبردی در کنترل انصارالله یمن
🔹
در سپتامبر ۲۰۲۶ مجموعاً ۱۰ نقطه راهبردی شامل ۵ پایگاه، ۳ فرودگاه، یک بندر و ۲ جزیره در غرب یمن در کنترل انصارالله قرار گرفته‌اند.
🔹
در میان این نقاط، فرودگاه المخا، فرودگاه بنی‌الحکم، بندر المخا و جزیره میون به‌دلیل نزدیکی به باب‌المندب و مسیر کشتیرانی دریای سرخ از اهمیت جغرافیایی بالاتری برخوردارند.
🔹
همچنین جزیره میون با باند هوایی حدود ۱.۸۵ کیلومتر و جزیره زُقَر با باندی نزدیک به ۲ کیلومتر، از مهم‌ترین نقاط جزیره‌ای این فهرست هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/697489" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۲</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/ جلسۀ دوم
🔹
سخنران: پناهیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/697488" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزه‌ای شگفت‌انگیز در اعماق آب‌های قبرس!
🌊
🗿
🔹
این موزه زیرآبی در سال ۲۰۲۱ با نصب حدود ۹۳ مجسمه انسان و درخت در عمق ۸ تا ۱۰ متری دریا ساخته شد تا به‌مرور به زیستگاهی برای آبزیان و صخره‌ای زنده تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/697487" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab408a0297.mp4?token=Od4vxha7U-QVtdJbGAhv35Pzg-uzc58qF9kq3ZQmK0mfTVubik3ZahAkVOGv1L_q5Tr3z23q1R3Sj7uIQYXwE-KqIh0MlIOTtDundgYclwNZb43SHYiXPbfBJWyjGbE__jCuH_2SShT9R4b7gbvQ0rGdttCk70GLDH8NAAQUIhVGTd1-BsjQt_t2in6962hY9ffD6UdiUAhasHscTfy8j55v698S2aHS-2CfXJhHIbpjCeJbYY0jRxJrZ-BvmUAxy1o2dAEdbqv0YZrtpKgHv3EyQOn_dLhnbxldQ8-54QgSjNrBsHeCZeMM7FwHUoLNxJ6DLJQeeH6sXFFTLJKEroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab408a0297.mp4?token=Od4vxha7U-QVtdJbGAhv35Pzg-uzc58qF9kq3ZQmK0mfTVubik3ZahAkVOGv1L_q5Tr3z23q1R3Sj7uIQYXwE-KqIh0MlIOTtDundgYclwNZb43SHYiXPbfBJWyjGbE__jCuH_2SShT9R4b7gbvQ0rGdttCk70GLDH8NAAQUIhVGTd1-BsjQt_t2in6962hY9ffD6UdiUAhasHscTfy8j55v698S2aHS-2CfXJhHIbpjCeJbYY0jRxJrZ-BvmUAxy1o2dAEdbqv0YZrtpKgHv3EyQOn_dLhnbxldQ8-54QgSjNrBsHeCZeMM7FwHUoLNxJ6DLJQeeH6sXFFTLJKEroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی به آخرین وضعیت دموکرات‌ها و جمهوری‌خواهان در انتخابات آمریکا
اکبر مختاری، کارشناس مسائل آمریکا:
🔹
نظرسنجی‌ها نشان می‌دهد که دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا، شانس بسیار بالایی برای کسب اکثریت در مجلس نمایندگان دارند. اما در سنا، رقابت بسیار نزدیک‌تر و پیچیده‌تر از این حرف‌هاست./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/697485" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: با پاکستان و ترکیه همکاری می‌کنیم تا همه مسیرهای زمینی ایران را قطع کنیم/ احتمالاً این هفته یک میلیارد دلار رمزارز ایران را توقیف خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/697484" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
گزافه‌گویی نخست‌وزیر پیشین قطر: ایران دشمن اصلی ماست اما این به معنای کنار گذاشتن روابط شفاف با آن نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/697483" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سکوت سنگین در صحنه جرم؛ روایت میدانی از قتل پاساژ سعدی
🔹
روایت خبرفوری از صحنه‌ی جرم و آخرین شنیده‌ها از زبان شاهدان عینی  درباره قتل پاساژ سعدی را در این ویدیو ببینید
@TV_Fori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/697482" target="_blank">📅 16:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697480">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEa-dmneug3sdAosCW0u1PWkhLmUkxiRgDuNtkyvF92dKN0h6Fw_eJe-Dn2mqNMh62JkSab_OfvdrIBpSZTmJyOiqIZGxvuNl00s9Yyoh7btcpyB1rNOXdrusvzSWXzhomsVKLjJqj38EYjTQbBRUIPAPVaRaYesWB2Q8NO7htZmmCAORM2toAH7TOPIZz66Z-58hIzR6GjPyLtKmoeFivY4qcyxcutrZDrN4H75kR9JDpm1VXsgBBATUAYBrfDXWPDHMT06cJVgSrh-nG9t7QnHUmTQ8z23YRGp3toYeKMlIiJydyiePWTgFsSh-3WFVwcNwzLBhZTmodnw0x615Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفسر سیاسی آمریکایی:
آمریکا در جنگ با ایران است.
روسیه از ایران حمایت می‌کند.
آمریکا نفت از روسیه می‌خرد.
آمریکا در حال تأمین مالی جنگی علیه خودش است. قضیه هر بار فقط احمقانه‌تر و احمقانه‌تر می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/697480" target="_blank">📅 16:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697479">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای ترامپ: من معتقدم ایران مسئول حادثه هواپیمای فلای‌دبی است
🔹
ترامپ: عقب‌نشینی بمب‌افکن‌های آمریکایی از بریتانیا، در پی یک تهدید صورت گرفت و ما می‌دانیم چه کسی پشت این تهدید قرار دارد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/697479" target="_blank">📅 15:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f84dd6e8d.mp4?token=BnD-c2ab_b8R4iyid7colW8sFLLsBox5ZmlWH63QAnYlZlAcqLyb2o2I0LWATAVbAwHyynz7L7X5gFvMVfkh1vB2Wi-dwlE8Jl3GYcQCiLmUoEAnqWbh8mWiphGR-s4HsBdRENFVvK6RekwHwfdW4yCEDr7aVn9sW4P-dfSnuUPLiNT1hu5zzRjcEQ_ZJGekwElHfMcWNUyGBSjB2LRnmnIJtUBtj2yFSa5Pn3CITW-c-AI6K4RkuQd5hg37x6VCxRYIoz7MPtPxwp5vOzb0BwFPmVr8MVhYrryxuzDs00uZrO7QQvbKDCqAF41G2QWdb1ze1vonnzWc4Ahz3JvQmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f84dd6e8d.mp4?token=BnD-c2ab_b8R4iyid7colW8sFLLsBox5ZmlWH63QAnYlZlAcqLyb2o2I0LWATAVbAwHyynz7L7X5gFvMVfkh1vB2Wi-dwlE8Jl3GYcQCiLmUoEAnqWbh8mWiphGR-s4HsBdRENFVvK6RekwHwfdW4yCEDr7aVn9sW4P-dfSnuUPLiNT1hu5zzRjcEQ_ZJGekwElHfMcWNUyGBSjB2LRnmnIJtUBtj2yFSa5Pn3CITW-c-AI6K4RkuQd5hg37x6VCxRYIoz7MPtPxwp5vOzb0BwFPmVr8MVhYrryxuzDs00uZrO7QQvbKDCqAF41G2QWdb1ze1vonnzWc4Ahz3JvQmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/697478" target="_blank">📅 15:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697475">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieG3G1nY95_gN9OOnH_t7OnLc0LriwAaW14Ht77kb6xeUEQQEM3fER8bV_bl2dkMXhMgrcf-yE43tk2e0OlOwY5TxxUP2kxgPcuQLzbKz3FM6z1DgT2DbSlA7DPJcfIH-3vWWmyziNrnFl10-tPVcpG9k6KDogVZZWkbn8Zz7R_9ldNJvs5C042X3JUAN5MSctPBkWqiQdFpqo6j3jsCTOJ4VFOo4G4iEOcQ7hvULdE_5xPXTFrkVkx4skFw6FLuTIXfJTK6Qge9v5-FTYb-CqqNPTLOeeglSBHOH6LLpPdklRDTSiKDjwjYwOMvn9rslWZMmz7s-IWss-dlkM-Gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuysPgxMRSEKoMvLe_LRXhSX6QCyzUvYxFwX51LuAHymhK28sRtAUE93Fw6svGX6ykbmmrhXrY2NmahVYerG_Gp_MHy0wwAZFNkmdXHUwLxpkTsNULGZHfvZ-_yCBQJisIgKbkoBYaIYG_-6UL0714p9KtULZO_krrZy8GYnZkAAaYMMJSnw3IHkAngmJ0wDMreChkdBVkLzf1OH76whj84TaBJFt8tV3GCmvWKavjkYnpGfI2zbFr32C6tKFYfMTyGlwEkEXitb-XW8pSX_mk32D3ZYpHp3zG-mM9LT2_dYYawB4qZEucIaRtAsn0WlAnaer8kIhnLYoSHekHZklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0BIi6svlZ4nlsrDKi53jZ9v72NMK38p9TWzApmaPAR2o7RUu-TcuTXPQ_IWY_X39DcV98amLbAZTjvheRUvNrqkWyfPsoPMb6sGSl-CU8S06yH-LmBZTk34_zElM-looE3VN5oAW_lSlQGVApkZ_cmojkt3KmUGa7b8iwUo3e_iLrI7TLtKMloPseLhcHMQ0QEGyawu__LWf-Z-cVcL2o9FqxaahcIqD3QTj4LQ9_V-12bXPIp8Djz0SeAhXeL7ZkhDKKm8c-DeEquaQ9qosEYYDgxetM_YzW7Tkn4A5M6vfRkcTaeyuMUQDU8G7igJPg3PeLUmqOokakwsx2CXlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این جلوه‌های رنگی فیلتر دیجیتال نیست؛ حاصل برخورد نور با بال‌های مرغ مگس‌خوار سیاه ژاکوبین است!
🦜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697475" target="_blank">📅 15:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697474">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQnFbceawf3FTSeRBm_qPqadEB0pvtyuDu1RYw-8QXFCLtfmFsVwAvEDbr7fXBEydZ_EGmMeJQ7FBgVYEG8Fb9ca-cSRepwmxJ_JPj3Y56EOtMHLqnQzd64znFVz36pjK1JAxNVO_SUiFFrqTM2COJds1gvt6-5CULFP5CD7RLDHNedzLfc9wc6F_DHopeeHk9OqEJjHYl6JSqz3y4trY_Hqp3_ZwRBVPAduhOkLHoJB81padHOU5lvy6Vst5fAiOnCEf59IX_GbQaqV0w5MAkRktJ-BZw2141W9afMOcNXHnaTpFT1uGWz2118WoJxBlpUdMtPW7g4PrwLwYkDfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیجانات بازار ارز چگونه فروکش کرد؟
🔹
از زمانی که
طرح عرضه دلار به «کد ملی»
در حاشیه قیمت بازار کلید خورد،
ترمز رشد پرشتاب قیمت ارز نیز کشیده شد.
این رویکرد بازی را در بازار تغییر و هیجان را کاهش داد.
🔹
در شرایط جنگ و محاصره،
آمریکا به‌دنبال القای خالی‌بودن دست سیاست‌گذار ارزی بود؛
تا جایی که معاون خزانه‌داری این کشور در مصاحبه با بی‌بی‌سی مدعی شد
فروش نفت و منابع مالی در دسترس ایران رو به پایان است و این فشارها ایران را به زانو در خواهد آورد.
🔹
در چنین فضایی، اقدام بانک مرکزی پاسخی صریح و مقتدرانه بود:
نشان دادن دست پر بانک مرکزی و مدیریت روانی بازار با عرضه گسترده.
در این میان، منتقدانی این اقدام را «اتلاف منابع» خواندند؛ اما در
اوج جنگ ادراکی و ناامنی روانی بازار،
انفعال به بهانه حفظ ذخایر، زمین بازی را دودستی تقدیم سفته‌بازان می‌کرد.
بانک مرکزی باید با اقتدار وارد میدان می‌شد تا انتظارات منفی را کنترل نماید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/697474" target="_blank">📅 15:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697473">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2cb1edcc4.mp4?token=mRRca4tbciJOzL8qUvbBQeCykX7tGKeVgR-LHZDTRzDotXIRlDkXN3_TDe35rUt-pp9_Cqi5MiOd8S9UlkuWHudLonRVW7wJZvD9Z0Htmhw72ki-WionHv5xxTe8HJr09mGGupB7nqFZl45FNElfc1JLB6BJcdFV0FeJSvT8ojrjq3PsubfXSkhYZNWDYOJaxESBclwAhzFbeRnehVikYdI4z_Wj3qUH3g_77cHrzZoi_TK3SPXS5-zlI28ua2hXmE4Ai4BDJSl_A7Ij8MFY91OIv8RxlwSFwdfGoQWTZ_4vLa4JFCsBSNGO_huZGWhINmOkh7pW2mXpkxZAzylaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2cb1edcc4.mp4?token=mRRca4tbciJOzL8qUvbBQeCykX7tGKeVgR-LHZDTRzDotXIRlDkXN3_TDe35rUt-pp9_Cqi5MiOd8S9UlkuWHudLonRVW7wJZvD9Z0Htmhw72ki-WionHv5xxTe8HJr09mGGupB7nqFZl45FNElfc1JLB6BJcdFV0FeJSvT8ojrjq3PsubfXSkhYZNWDYOJaxESBclwAhzFbeRnehVikYdI4z_Wj3qUH3g_77cHrzZoi_TK3SPXS5-zlI28ua2hXmE4Ai4BDJSl_A7Ij8MFY91OIv8RxlwSFwdfGoQWTZ_4vLa4JFCsBSNGO_huZGWhINmOkh7pW2mXpkxZAzylaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آتش‌سوزی یک نفتکش در تنگه‌هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/697473" target="_blank">📅 15:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697472">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پاسخ وزرات بهداشت به روانشناسی زرد/ اقدام به روان درمانی بدون تخصص کاملاً تخلف است
محمدرضا شالبافان، مدیر کل دفتر سلامت روانی، اجتماعی و اعتیاد وزارت بهداشت:
🔹
اینکه افراد مختلف اطلاع‌رسانی علمی کنند حتی اگر روانشناس یا روانپزشک نباشند، ارزشمند است و ایرادی ندارد، اما اگر افرادی تخصص مربوطه را ندارند و اقدام درمانی انجام بدهند؛ کاملا تخلف است.
🔹
افرادی که مداخلات روان درمانی انجام می‌دهند نیازمند یکسری اقدامات قانونی هستند که سازمان روانشناسی در این خصوص پیگیر است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/697472" target="_blank">📅 15:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKiC-V7LCshxrjOCTdez1ixKEEOHlKF28kodCgr-iekRDRdD22dOczgqz0_Xag5oan1ooAYV0mYPZQRwcV0PsLGvx5TWy22LU0wEl41wZIIOcHd6yoMBvT91dHpXmLYENWrfj5YPi_8CNWGkLqV6VX5Bvm7Gf9Dwi2jHw6ixt8j5fS-FBIcgNYF6lBHL8bSzmEbiVNCcOLAdp6qo5GfLKwiwgH0G-Z2RrqKOCAsRJkEqoUulbqRxxfKAFbLN4c3kQ1gl2x_F4nCv2A3vaDq-01ePHfYTHXSd3ZPUE5TOyIic8C5kUCvG73IlAcohvDSZ5zN4oCHzIIz7W_InKeWZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snssFHzN_kpYn5XWBhHaQmPJTzfkhrnOxbCdmhyplPh0bP2J8gm00Gpg28Og7UmJxkji9QP5a2uGOXuq7Z_YyB0TjE3xvaBpnnj0xPZ7zmOVbuoeEurJXq5I4oro8uz-IHw3a1an029CAJsh8dra6KsHzVJNjPJdTxNZS8GYm2RgbFcpyGu6Hhcj6S8TmDGo-Gbs2DdsQUPUcVffsxq9d6S_IgwkS3GPRK_C7XvNfgRwlGCax1Ac-hUMiF92Mp4b_jui-dJqjteKmNvuzpO3IA44GXbiWuujsspAjO6vltZdwvxps0YRSr4b5x_3joT9IN0yLu4e7UI10N5GBILa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMb1ZFiVOn5qrloOSXPl2C3mmZFWE0cL4iyM-OaN8CigVvWmXCw7U2SgZRfRk9mLerUC9DiAMVynP0j5lnfBwgaIrM6YykpE_tiMHEVedof7OcJnTW31cA4-w3YQ306IxaGSr0fcanNnmQ4gwW3hSMOre-qdypQ06QPyg-M1MYVdT1clqQdWuYknsrQYAiaDo3BHBTSTeHQzVfbMOhf2MwgbGiyi9H6-11jitqWv7mY246jmWlqFxlk5p3Bsr1U2Aklgb6RkPrcSj3WbelzjfyZY1an9-2ULlk66GuBdIKH3LNsdhc5tvcPGgQXj1ZIzIUqRibNjtM9eUl9Oi2YU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mK79585Y8hbFfqVdJcdAWfH4TJI-lcl_5VcnHy4WAZRKFsrNg69ZIDqDQl3gyMO9iECXuhWAh6jqOch8eyZPwXG-RMAwbgJZdpIrG76hYU2fDoxcFp-13zhvbGSjdTMXwxAf69eLlyuvX3twSRJYBGmmuror5LqlUI7aV0Rdo_FTIyFFcww0_nSajyUTj1xKyHZGya2AOQp5G51jUSVPn_093wd4SarY8taUVD_0pEbJfqCAPdTvQmVJNVH415S-ntO17tUTEMfj-kQzdx4GJUT2uQQnrvRZxmqSpGXkuS4clpXJPOq9NTrfjAhRlaTcGhIguAYKR-sXp1SJvn4vXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIqHt14V_qmGOJaK_f2Y0C-7qr5i2J7Fn1xPH58RX_M48PNJro0Akd6xC681MHkuu_j5PVtj8IoJxGWHY9YiySVbufSve32AjaLkOUUFyVlvvAfGkL_UtL2vmwj5nMmXIsw6FMS4rto-fdp2n1CVkwrUjjp0UUn9BTw9Frdnd8njH2Cosrwy5oKVQIdEqeqm5ZfRlJzpcH0vX2hLTB_68ec5Jd5oMS4LmEA6O-cqDZVdcNiNaxmlbuRpiTCrWvOBymPSWoBk7GN2Huht3590p7bb1Ue3uHXwv8V9e8HTQ3FtugLoiwkSIoSifIie-W7EVcEfuXj7haaTwZbthnQICg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر
قرص‌جوشان دقیقاً برای چی خوبه
؟
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/697467" target="_blank">📅 15:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697466">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0a45d897.mp4?token=fZ-XhvUT4I0h0PKmG_Gj5oZFErmoNv1Tf9zkfbteL6nBFSqTpdhhMmFfq5LqIorBCZwncD-07c6tFAjbF6q59-QZUNBdbrELf46OwCi8tnmbYzDESzBs2wWvVfprwnpMQk-UrNK0GFTU7sF5WzhaAMs1df-r7JawUeh0y6uWFQreBkO9fh8Wm9DMToWrxqOd1V0eoqT4Y7mK9bVkfMcS_vYFHr1Z6h39928IGcZcV18SllD09y9E6M8XhK81prpQN7YUyOvqw--N-YL1RiD8fRPE8j_PkFxbUHFcXo7VQud0WOgTaIL_R4WcbWLIlRDIU_D6oIrk6ke4P2BSc0WKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0a45d897.mp4?token=fZ-XhvUT4I0h0PKmG_Gj5oZFErmoNv1Tf9zkfbteL6nBFSqTpdhhMmFfq5LqIorBCZwncD-07c6tFAjbF6q59-QZUNBdbrELf46OwCi8tnmbYzDESzBs2wWvVfprwnpMQk-UrNK0GFTU7sF5WzhaAMs1df-r7JawUeh0y6uWFQreBkO9fh8Wm9DMToWrxqOd1V0eoqT4Y7mK9bVkfMcS_vYFHr1Z6h39928IGcZcV18SllD09y9E6M8XhK81prpQN7YUyOvqw--N-YL1RiD8fRPE8j_PkFxbUHFcXo7VQud0WOgTaIL_R4WcbWLIlRDIU_D6oIrk6ke4P2BSc0WKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معارض سعودی: تعطیلی فرودگاه ریاض برای بن‌سلمان خطرناک‌تر از قطع نفت است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697466" target="_blank">📅 15:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697465">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
هاآرتص: هزینه حمل‌ونقل یک نفتکش در حال حاضر از هزینه پرتاب یک موشک اسپیس‌ایکس هم بیشتر شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697465" target="_blank">📅 15:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697464">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1LgnLZ4wOMi3kROuUOTM3t5i0EC1-Skfe-hgVpVGiO-BJtDx6IdcxAc9L-NL01jPrDyuJjFW18GtvyN7-XMdeKQ8j9nefcYIQAioHQN2iGCgstLb-6-JXN8JtcmFzM58qa5IY1lEMJ7lsydvQUNJJWmHIcHLJ6DFOwRzsi8Tgc4zrlgyk7r1J8LwyDNH8mSxByqjV2xHlj5SUnLSePzR74Ap3yVqpmA2PQguDSc7qOy6kewBGpAcb2j9C0MG5i9m1K6jW-uz0TQczt7x8ZMP79RW47CdOZW7VRcHBzLlW4p8yEA4Qkb1CO9371nBqKPpHS1ywm5od3jtxcmcgI_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه: شرکت‌های هواپیمایی باید صورت‌حساب خسارت‌هایشان را برای ترامپ و نتانیاهو بفرستند و از آن‌ها غرامت بخواهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697464" target="_blank">📅 15:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697463">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: ایران جنگید و شهید داد، نمی‌شود اختیار تنگه هرمز دست عمان باشد!
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا با فشار بر عمان به‌دنبال آن است که تمام مسیر عبور کشتی‌ها از تنگه هرمز در آب‌های سرزمینی این کشور قرار بگیرد، موضوعی که ایران با آن مخالف است.
🔹
آن‌ها ابتدا با عبور کشتی‌ها با هماهنگی نیروی دریایی سپاه موافقت کرده بودند، اما بعداً از موضع خود عقب‌نشینی کردند.
🔹
ایران واگذاری اختیار تردد به عمان را نمی‌پذیرد، چراکه جنگ را ما کردیم و شهدا را ما دادیم و نمی‌شود اختیار تنگه هرمز دست عمان باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697463" target="_blank">📅 15:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697462">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxGCI6VWWftYpO60r3k99grY8S2FfWCGbdYdNUy9pzsxn1i9JJdVJwl0XK3E5oScbKFfWmfhXSBUrxOFTCaPRY9qCo4UwHnbp0UsXH4sGOv_DrHZoqCXdwmoBpxL_2snIXNAcNV8nJm1AmxzBN0UcQgDWHKaiwvJJemMoBgHhBz84T0yCqF80kFNFWegQC9h_fd-tcG-NjYJWuUhZ4G_qiG1z0rDRFh44CGrnXQaaBqhlRcrRJJm9iJ7bxwlmDlO__8QCTQdFLlYzqkmlJZX4U3fa8GN4j3qS6r6tnTkJBjbZDo4mR1J0wCPcDam9H45YNaWQyahozm5boZIvduBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه نگار کانادایی: احساس می‌کنم که ترامپ بعد از شکست جمهوری‌خواهان در انتخابات میان‌دوره‌ای، جنگ جهانی سوم را آغاز خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/697462" target="_blank">📅 15:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697461">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تصاویری منتشر شده از لحظه حمله یمن به فرودگاه بین‌المللی ملک خالد در ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/697461" target="_blank">📅 15:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428cf0b54a.mp4?token=qaX0cj0DFJ2IVfWOmmeaHsAXbbxpzCPov9NcAaPDKxHiNNNYYwqjsGZTytuetoWNEyZCP_cXifVPYAQZjuW2Y9j5f8Y43TNEu3OeERgT4EOyiaiLwHpNndfyww76udMURX8XfGTI7NmbkS_1rKUp0OSQmnzI9DLA8DzGTvXVnyuTa-82eulP1ysXkZYuYfthjAXM9vK3gM9EUGRYxzbw1yWlnHRENj-s_l40qeZklj5r-EVc5BtGgKpQt0FZlkoQ1AufPP9e1HxnfTjdb-cGerRXpDjO4lPvUbS5_0GyuiMnilyoLFHv5dJwrEp2fvGgS5oVsidU-0JlJ_VewC6J_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428cf0b54a.mp4?token=qaX0cj0DFJ2IVfWOmmeaHsAXbbxpzCPov9NcAaPDKxHiNNNYYwqjsGZTytuetoWNEyZCP_cXifVPYAQZjuW2Y9j5f8Y43TNEu3OeERgT4EOyiaiLwHpNndfyww76udMURX8XfGTI7NmbkS_1rKUp0OSQmnzI9DLA8DzGTvXVnyuTa-82eulP1ysXkZYuYfthjAXM9vK3gM9EUGRYxzbw1yWlnHRENj-s_l40qeZklj5r-EVc5BtGgKpQt0FZlkoQ1AufPP9e1HxnfTjdb-cGerRXpDjO4lPvUbS5_0GyuiMnilyoLFHv5dJwrEp2fvGgS5oVsidU-0JlJ_VewC6J_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از خداحافظی عجیب خانم کمبرلی سفیر آمریکا در یونان با روبیو وزیر امورخارجه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/697460" target="_blank">📅 14:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
به اصرار دکتر محمدحسین امید، اسم وی از روی خوابگاهی که به نام او زده شده بود پایین آورده شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/697459" target="_blank">📅 14:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156e1734ac.mp4?token=JkoJri1L3oYOAzcRQ6hWpDTJhwAlhfKbRuxheAYkKOjcn43u7EtJdjvCB8ujJF6dGHyJ88a0kzbHi0KSBDJiRxWS_yJl04znFUwnyfog7rOuuiSADHqS_CVpRre1r929ia09Rnf3bOnnYyz6i2NdjRWN1NPAHh-p0lZhdwvdb0Y6eArisnz4XI5FXXWOBzNf14P6KjFeBHHN-N08QNpEiv1cew6Lk0vaxgOX-I7iWQ4zNnlndrAtuJDdrGSoVb_cKmDA06uE0-4-OIbABZXx8-qinz_ce9oa3dcKSivRVAebCzOjpOgyxesIuKzkhoQFWhCM2cpnQTAMxtY7aiOXlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156e1734ac.mp4?token=JkoJri1L3oYOAzcRQ6hWpDTJhwAlhfKbRuxheAYkKOjcn43u7EtJdjvCB8ujJF6dGHyJ88a0kzbHi0KSBDJiRxWS_yJl04znFUwnyfog7rOuuiSADHqS_CVpRre1r929ia09Rnf3bOnnYyz6i2NdjRWN1NPAHh-p0lZhdwvdb0Y6eArisnz4XI5FXXWOBzNf14P6KjFeBHHN-N08QNpEiv1cew6Lk0vaxgOX-I7iWQ4zNnlndrAtuJDdrGSoVb_cKmDA06uE0-4-OIbABZXx8-qinz_ce9oa3dcKSivRVAebCzOjpOgyxesIuKzkhoQFWhCM2cpnQTAMxtY7aiOXlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان کشته شدن ۱۲ نفر و زخمی شدن ۳۰۹ نفر در حمله به فرودگاه ملک خالد را تایید کرد   ملیت کشته شدگان حمله یمن به فرودگاه ریاض طبق اعلام رسمی:
🔹
۴ شهروند عربستانی
🔹
۲ شهروند بنگلادشی
🔹
یک آمریکایی، یک مصری، یک اردنی، یک سوری، یک فلسطینی و یک سودانی بودند.…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/697458" target="_blank">📅 14:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e9d0d1c4.mp4?token=W92INX3EinBYx2EnjusIraJfOpJIhUiizIIWUwLWUiHOqPgMxanRGBtjueNQWA8O48rAFZPMRqqmpKqYAKYqsXRJYmR1h24gkUuOWmEA9UnfKmpZVbZtXdtVDh8RT-vGtMrS5DVDKjG6_mGpOIOQLmqh09ajlVsZmTr9Qp8SUsi0zmyfVEp_J0kI6dKTqQzYFnhePp5wtE3AxeWoutYd8OTo-2EsuYGrpr5CuutAWHp_JB1dHIY30GfiHPk0jCBpUGrCtxrzVWqQsIlBNUrL6iosmgmz-NonypETNycmKMc43XTotR7dygkvTHWmDCsROyJNkG1ncBmv9EoGizZkuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e9d0d1c4.mp4?token=W92INX3EinBYx2EnjusIraJfOpJIhUiizIIWUwLWUiHOqPgMxanRGBtjueNQWA8O48rAFZPMRqqmpKqYAKYqsXRJYmR1h24gkUuOWmEA9UnfKmpZVbZtXdtVDh8RT-vGtMrS5DVDKjG6_mGpOIOQLmqh09ajlVsZmTr9Qp8SUsi0zmyfVEp_J0kI6dKTqQzYFnhePp5wtE3AxeWoutYd8OTo-2EsuYGrpr5CuutAWHp_JB1dHIY30GfiHPk0jCBpUGrCtxrzVWqQsIlBNUrL6iosmgmz-NonypETNycmKMc43XTotR7dygkvTHWmDCsROyJNkG1ncBmv9EoGizZkuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسان ژاپنی دُم رباتیکی پوشیدنی طراحی کردن که با الهام از دم حیوانات، به حفظ تعادل و کاهش خطر زمین‌خوردن سالمندان کمک میکنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/697457" target="_blank">📅 14:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رئیس مرکز آمار ایران: برآورد فعلی جمعیت کشور، مطابق برآوردهای پیش‌تر اعلام‌شده، حدود ۸۷ میلیون نفر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/697456" target="_blank">📅 14:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود/ مردم همکاری کنند فشار دشمنان شکست خواهد خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697455" target="_blank">📅 14:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bd09cd46.mp4?token=KNn6llPnIojq8b8xrKDMqe_iajKN4SAOhYpY3iZULE1k5YRb8y3BGoOO9xLrb0psLlSgtOlnLJQM0fVIAZCAK1Jzz8gB9dzT4s5zrSE2icOXrQCFVHkmBcO9pJfcmZsjdY7rMcZRUKl-9ruxUJDnMtdX7CeS_5Yv3zOdRRBPxEImvGQVBYqbEOC74eJOn9iXXwePWilYaqnocmyD8aKFjS9VKJhrY1TaGq5_7QB9vJPElQzZQkp1ameJohEZvtCx0Xh3Hhpgk3f4kz4g4e6lWHVhLjnGWjY0cLuyAcSQ_89zPnmWPmcgHacycOEwjneLZmWhHn7LR5Tk82QlXuoJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bd09cd46.mp4?token=KNn6llPnIojq8b8xrKDMqe_iajKN4SAOhYpY3iZULE1k5YRb8y3BGoOO9xLrb0psLlSgtOlnLJQM0fVIAZCAK1Jzz8gB9dzT4s5zrSE2icOXrQCFVHkmBcO9pJfcmZsjdY7rMcZRUKl-9ruxUJDnMtdX7CeS_5Yv3zOdRRBPxEImvGQVBYqbEOC74eJOn9iXXwePWilYaqnocmyD8aKFjS9VKJhrY1TaGq5_7QB9vJPElQzZQkp1ameJohEZvtCx0Xh3Hhpgk3f4kz4g4e6lWHVhLjnGWjY0cLuyAcSQ_89zPnmWPmcgHacycOEwjneLZmWhHn7LR5Tk82QlXuoJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایا مدعی رزمایش موشکی نیروهای نظامی ایران در غرب کشور شد/ مسئولین تاکنون درباره صحت این تصاویر توضیحی ارائه نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/697453" target="_blank">📅 14:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008da17ca9.mp4?token=BKhpI7P7pKF6FZpUL94I_hKXdOoX9jYOUSwTJXoYyRqYSy58pcY-n0sAmEG7g2S75UyK54TP8xAaFcCcPTyOOIpSJOgatFVUasFDrdXe3J4l1DKnkO6GHo57LIU4T_NcTTs2JRGkImtBs-3PonSL_RN2WiEYnMqQjK0-x3eYLybP_yLkmVG482pPhs1dYb3qWhPwKKJiHZJ8WBNyElzwkdp5z7kthOtMZCn_3Iu9GhiMgW5bYgvTzBF4KYwSAluI6Nf19VxDxweDnoNa3370UXoZauq_JYM2hvnZm7xeeFym9auW2fvSjnZwllVfK4VT3esxxNyPVcGAVwIr-cDsUE_6W7y_qLuELF4JvN2EyRFqH5YnCivEIeBYSXADjTcxe4fgGO6E6Dc_j-W2K1womtgDsW-Wk4IvwIIK2FyOEUiBQ__eM_2RnWcOS5OEYhr8LJWMBPTxJjSA3Rjh9iltqdVbkrymAvQJr-0d4iDwMyMbPF38DwnCvzpfdxYKqROC569GVjqUd4yj_dFqrU-W-9uS6EGotfIWqn8wE-fnQX2QEmCCvWG6d4i1l9OFC-W0Vm2j_FpOCLIfwJP21T_DxEU6CQogxT94Jzn5KzhzIN5zWoBEahHkJx461niM4i6TlkLMMDkq5XYfo6fHbOmJugWRoxxP4hAr1J9TidnV4WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008da17ca9.mp4?token=BKhpI7P7pKF6FZpUL94I_hKXdOoX9jYOUSwTJXoYyRqYSy58pcY-n0sAmEG7g2S75UyK54TP8xAaFcCcPTyOOIpSJOgatFVUasFDrdXe3J4l1DKnkO6GHo57LIU4T_NcTTs2JRGkImtBs-3PonSL_RN2WiEYnMqQjK0-x3eYLybP_yLkmVG482pPhs1dYb3qWhPwKKJiHZJ8WBNyElzwkdp5z7kthOtMZCn_3Iu9GhiMgW5bYgvTzBF4KYwSAluI6Nf19VxDxweDnoNa3370UXoZauq_JYM2hvnZm7xeeFym9auW2fvSjnZwllVfK4VT3esxxNyPVcGAVwIr-cDsUE_6W7y_qLuELF4JvN2EyRFqH5YnCivEIeBYSXADjTcxe4fgGO6E6Dc_j-W2K1womtgDsW-Wk4IvwIIK2FyOEUiBQ__eM_2RnWcOS5OEYhr8LJWMBPTxJjSA3Rjh9iltqdVbkrymAvQJr-0d4iDwMyMbPF38DwnCvzpfdxYKqROC569GVjqUd4yj_dFqrU-W-9uS6EGotfIWqn8wE-fnQX2QEmCCvWG6d4i1l9OFC-W0Vm2j_FpOCLIfwJP21T_DxEU6CQogxT94Jzn5KzhzIN5zWoBEahHkJx461niM4i6TlkLMMDkq5XYfo6fHbOmJugWRoxxP4hAr1J9TidnV4WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفت میلیون برای یک جلسه؛ کنکور یا رقابت جیب‌ها؟
🔹
وقتی قبولی در کنکور فقط به درس خوندن ختم نمی‌شه و پای جیب خانواده‌ها هم وسط میاد؛ آیا رقابت بر سر دانشه یا توان مالی؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697452" target="_blank">📅 14:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b16ed0a34.mp4?token=ShmUN1FpeRLn46hmYgIU_hLGZsF9wZ4sDgjkLRjuYzkYVAolu6pJbQ6QQF3g-qynjvdU-F8--9og1eZY_9DRSq9aEipy0v1iOsnZPNtssh69at9OfIOkWFyoLNGeODRmcsKSdKlOBR_pskkr4QQFeb06WEVdtADSR_mE9CuTRCE567O4abMeh3PEwC6vVmbSWZXP8MwwwM8nv_U4QWeKAHet7jx5qdjJnYmQ848cQJsgHsrg3wKZxrde_E_-nTrcs1nRCNTc7SYPvqwzneTcsJOo-8z1UovzEOZoa1n0n-SH0HC2V25jQ7ZVrC82GIwAVX_T07xgkW2rQx0OjcpZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b16ed0a34.mp4?token=ShmUN1FpeRLn46hmYgIU_hLGZsF9wZ4sDgjkLRjuYzkYVAolu6pJbQ6QQF3g-qynjvdU-F8--9og1eZY_9DRSq9aEipy0v1iOsnZPNtssh69at9OfIOkWFyoLNGeODRmcsKSdKlOBR_pskkr4QQFeb06WEVdtADSR_mE9CuTRCE567O4abMeh3PEwC6vVmbSWZXP8MwwwM8nv_U4QWeKAHet7jx5qdjJnYmQ848cQJsgHsrg3wKZxrde_E_-nTrcs1nRCNTc7SYPvqwzneTcsJOo-8z1UovzEOZoa1n0n-SH0HC2V25jQ7ZVrC82GIwAVX_T07xgkW2rQx0OjcpZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشرشده از آب‌گرفتگی معابر و خیابان‌های شیرگاه پس از نخستین بارش پاییزی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697451" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96db896ba5.mp4?token=V3FYc5YLV512hGlPVTEGqY6bon3GOZXCNicGuw_cze_rCJHM_7z7RYuaBHUJGkFzl9dJ9UwHcRNilYqvyYQ2XQUIVUg-j-QYuMB5dpVqJYPniHPbFOCRa_E0mIJ7x7Cjxo86OdAZwW1Q84mXvhvW4fpm2j1XBQC_SYpcteZoEVZTA7ZXRpyfX7BQt-bghkt8HZlhVjkGzTecmxItWnOoztwVZv_IhULLq-t2INmjsHLSzv6gRB5KCav4EmyM0UxqybnWncAEyUg0KUjKVb0v9ZB0nSrz6U81MTf2CMRjcUIh7lScK_BwYllYEnT1luI0LI9_vOAa2_p4mTEX27Icpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96db896ba5.mp4?token=V3FYc5YLV512hGlPVTEGqY6bon3GOZXCNicGuw_cze_rCJHM_7z7RYuaBHUJGkFzl9dJ9UwHcRNilYqvyYQ2XQUIVUg-j-QYuMB5dpVqJYPniHPbFOCRa_E0mIJ7x7Cjxo86OdAZwW1Q84mXvhvW4fpm2j1XBQC_SYpcteZoEVZTA7ZXRpyfX7BQt-bghkt8HZlhVjkGzTecmxItWnOoztwVZv_IhULLq-t2INmjsHLSzv6gRB5KCav4EmyM0UxqybnWncAEyUg0KUjKVb0v9ZB0nSrz6U81MTf2CMRjcUIh7lScK_BwYllYEnT1luI0LI9_vOAa2_p4mTEX27Icpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صعود نفس‌گیر با موتورسیکلت کراس!
🏍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697450" target="_blank">📅 14:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5057416.mp4?token=DUuoEC_eFnkCvE_PNakufcYdEnscrRzfM37jXBn9kh_KFWgiFNLYSI11-O-XMDQvRD8cMnwznooDqvkWkYptO4-Vl49W_qArTlFRLJLYbD4ukV6HfJUvfcJNd3dskY1Ceuq-nN7IhlThnUUDUeJKKGA6rkF3_nsAgpbH7wb9LIqn4_QY2NOJypQ5S0UzF60_XjOW9qBtRLrLqVYdfotWvX-b4af06EcgqexhgQ0cCdQI1HtGh_velFmi2QblySPQFnRr0n1V-zDNpMHNRkvISpEAmkJyHjtj0ciYSK0qKftK5u53bnoPxljSSeIg0Bl4EQW_9sILav13CpVksS_bUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5057416.mp4?token=DUuoEC_eFnkCvE_PNakufcYdEnscrRzfM37jXBn9kh_KFWgiFNLYSI11-O-XMDQvRD8cMnwznooDqvkWkYptO4-Vl49W_qArTlFRLJLYbD4ukV6HfJUvfcJNd3dskY1Ceuq-nN7IhlThnUUDUeJKKGA6rkF3_nsAgpbH7wb9LIqn4_QY2NOJypQ5S0UzF60_XjOW9qBtRLrLqVYdfotWvX-b4af06EcgqexhgQ0cCdQI1HtGh_velFmi2QblySPQFnRr0n1V-zDNpMHNRkvISpEAmkJyHjtj0ciYSK0qKftK5u53bnoPxljSSeIg0Bl4EQW_9sILav13CpVksS_bUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت بغض آلود رهبر شهید از حاج قاسم سلیمانی
او کسی بود که آقای شهید ایران این چنین از غمش می‌گریست
برای شهید بودن باید مثل شهدا زندگی کرد
رفیق با معرفت مثل حاج قاسم سلیمانی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697449" target="_blank">📅 14:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94dcfe9617.mp4?token=t06gcg0a6OCfNJRofmQD-t7mpRUllHxHAIW1H49tYx4bHj1LmJuTA9Maf6BDCQWOyTPuOgrQ2xVexf3zYOU6B3OZxJO-ngFU-zEhRFiP2i51mIGSD1dEVjVEEWESqldKBBaRHMqDVwXkMVe3UoeFyQQ2k88d5c2diEsGMT2-1yS7-Yk2KAhPj5uf3ToT5NUQEoUXjlciSJcGg-OPx1hpRtSvmNle-fEj9i0fvgVJ9PX9_xlfGy_NzQNwc7U80SgzyarhhvRhKcrtOx91Dhc7dQnoEON_jLG7V1kTDmItfRSOSjjTOkTICKoA3UbQ-j3q0KfMel_mvN0jFjOZTjr8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94dcfe9617.mp4?token=t06gcg0a6OCfNJRofmQD-t7mpRUllHxHAIW1H49tYx4bHj1LmJuTA9Maf6BDCQWOyTPuOgrQ2xVexf3zYOU6B3OZxJO-ngFU-zEhRFiP2i51mIGSD1dEVjVEEWESqldKBBaRHMqDVwXkMVe3UoeFyQQ2k88d5c2diEsGMT2-1yS7-Yk2KAhPj5uf3ToT5NUQEoUXjlciSJcGg-OPx1hpRtSvmNle-fEj9i0fvgVJ9PX9_xlfGy_NzQNwc7U80SgzyarhhvRhKcrtOx91Dhc7dQnoEON_jLG7V1kTDmItfRSOSjjTOkTICKoA3UbQ-j3q0KfMel_mvN0jFjOZTjr8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پربازدید از اعتراضات دانش آموزی در فرانسه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/697448" target="_blank">📅 14:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFt4Gu7J7eXG51BPER36t9vymA46RlxVl9xJvj5i3_aAkXPT-OGk5bG5XHsbN7VxzlwoKGBvyCZA9OTyWdm1wewpm2OcsuHKcDQc1ewESd2g_r2OdaTLW1GGc9f4H9m73joThwnZ25omfW-sYih1WqOuzSln9h8e7xGG3jdu8bg0Hwx0nrSSLhjMwHm8izF6DYBJVnEm27QkG3ZlglVPUDBoszZfnW3-KATGioWTVJRZFjx30utmZinBQZ8SqT6vBpeF1N2YI75rAxydRffyU4dPHXdittMFHv8xkKNGHjxk5-5pNPUMI9UvB_HvMnM7Q7jC73zlWqHtFeO3YdEMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/debk0maePKiIwerbTMFSxYWlbexQe8D5QU3C46r2JnFlxNA6UHc2Tc5h78xe_iYBoQ8rdwoN53PuarCi5qAyyuKHsmHLxJcYDzxwvibVNBM1L6YUk2ja7Xmz_2jOuvX-R57d9Ayjido14cilXm__vssUnBF0ges7QEgjizr644UjHHD6VSqIvX1dIN1NT909CPobsqfVU-dZloGbeGSqh4k0DBTRNDpejpzvOiMdFBiMDoGO-eIr5FTWRD_RyC8MSelVloOuF4qhe--xmvfI9HdAXltfE9GWVo2mb7g37ykBnIeMmD7l5ds71yCHo9AjjzLMQHuH3PWaZ8JWD5HEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xvk0CL-8sEpSL5GaZi3GvA4Gi6kK3DzBUKNP4ECLcZ6y4PRPK92zv6AtwDV_ZX15E35B9nRLO97ODLlOc-b0OxA5Qon_FNYMv47RbtVsnxHHYgmePHY-c0GKx1dmnrbzopOEu1q-ec62ENYNWbrR5qAMYJL-U9zXFFRQfXrd-MbJ8WniGrJ6Jo1A0KqIExUf83tbHO66XKjvSv0eylC5hKLPz86rIEDiOlCUFx8bNesBLgdpnYPNChRGbZzTTEGGCPGss-v_f0p7eHwNO-caH5Ah4i0hddiasb36w35Hw9AL9oWZNuZHuZcqtcYIkJzledjoqtkKjaxZJ1CIDuNiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lj1ZZlt2sjLlmL0dkauTe2t8QUR7KE6TVxttsIq3dMuvmc-q_Kh6SUtlsbfTpjkclTztp7K8nCQ4xQ8RRJiMSLuYKe3GageBJLi_8I-ZxhUalM2nffENIb1HbJO6leALdrRsUy0_yMyjEx81XCJuP1-mbk2xnTB-I46m55icVfg9eND1I-YLEu3JMUCfES-6RxcO8Mzm65pEmyI3LZ2hFnCXzsrp-LtrCWuD9TGVbnmM3MP7p0FSMpVb_WfL38ONxmHi_Uqk3JifIfMCIvFwlIcJXWrgMRW1JnUcs1HnIdOOe23V-O3ZaCuhEXKuTixQLqXxq3Aj5JPKRk3Te76PLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onylk_YmQDOJwHfz2jWTCx9i6dLgpKLb21j-ybyxACEnoDUQx4gNTCVKB5N1iDPChgtCdDQJicCyvEYfj6V38jCme-WsREZxXJ78-HBIXGMf6frdfMuPRCWJTZKXScpFUsqAD4cppGG47uFgANqxxxd7bSVrJKA2jletyc0DPV25NmLOPy5C-0NvOAEzjP6G1q_5MG4Tct7LABVsRhtk_UH8WZ4dCkIquQCA27GZbn1u1mMx3wTW9G-OmqWBPOVHVtphv1j2Llpln8m8vWKyyazOQAjM7ppMv5goTeJx3by89vJwx5D3OJ6fAFIBjP07Ejnbg1u75kVUrQAA99Bcpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hW82cszhVmZrJXSbcuPV4m8rBAR8178TdoTEI7ecBdUhWMBgfsP-q8V7-LIs99JSyGLkeCv0v0qDmfKA8a2FeeKlZ-2sQ1N-moGp1QsgZcYfk5M1Sgw5Tdm8A4wXmStaFFoBAwv8p68C3pBMdPCJreNcWOGIY2wVAu_shtkNVar-2E9beawZq9avFGbxY2MzWHcfwYAb7IKHScmJXx4ZPjywvhmIqn2gXhIoTZEb34M-b7gC9pnr1xFfGMK_TPHvn4OimZ1gDKLtXQgIODup-WnHG-NE4PepQoS-r55uQ7CpRl_CjcA69Dzh4RN2fWYcoVDe3SZAV59bq9JbYnYAOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با هر مدل شلوار چه کفشی رو نباید بپوشیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/697442" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
دادگاه یا داوری؟
🔺
هر اختلاف تجاری به مسیری درست برای حل‌وفصل نیاز دارد؛ با داوری تخصصی، سریع و محرمانه می‌توان اختلافات را اصولی حل‌وفصل کرد. مرکز داوری اتاق تهران؛ مسیری مطمئن برای حل اختلافات داخلی و بین‌المللی فعالان اقتصادی.
🌐
وب‌سایت:
https://arbitration.tccim.ir/
☎️
تماس: ‎۰۲۱۸۸۷۱۳۵۳۷</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/697441" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2728528ff5.mp4?token=CdYbsJpUZVeAZm_M6i1VF162kTpuwkz68sWEA-iN1Np8P-Hya1fzwwSQ45qWaMzXaRYGD-bSK_3MOD7xItD9fZnX-Xg7WMfDaWngY3gSvh3fPtWIcaei9Cbi1PCZg9zslJqKwGWC0LE8_kcHl7aDIB4VLrDxhHnwke6Qpvf__sAZl_7_W75FNQ4L7qxzuBT1CLfOUnF1zCoAATyM9UzwhcvhooaJ2eKpPB1lCMAfcpB9YFH4Mhwt9eGx6Jw4eAXLU651uZnqdTmcdOmfQrnTrOgW7mGderXsCA9S501EIsVdvBmuIuSXUo4n7Z5NSp4jdyLpsbDtlhMEjTNbCXoKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2728528ff5.mp4?token=CdYbsJpUZVeAZm_M6i1VF162kTpuwkz68sWEA-iN1Np8P-Hya1fzwwSQ45qWaMzXaRYGD-bSK_3MOD7xItD9fZnX-Xg7WMfDaWngY3gSvh3fPtWIcaei9Cbi1PCZg9zslJqKwGWC0LE8_kcHl7aDIB4VLrDxhHnwke6Qpvf__sAZl_7_W75FNQ4L7qxzuBT1CLfOUnF1zCoAATyM9UzwhcvhooaJ2eKpPB1lCMAfcpB9YFH4Mhwt9eGx6Jw4eAXLU651uZnqdTmcdOmfQrnTrOgW7mGderXsCA9S501EIsVdvBmuIuSXUo4n7Z5NSp4jdyLpsbDtlhMEjTNbCXoKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از انفجار شدید در خط لوله گاز در سن‌خوان آمریکا
🔹
باتوجه به خسارات گسترده و قطع گاز همچنان مسئولین از اظهار نظر در مورد علت این انفجار خودداری می کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/697440" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رمزگشایی قاضی‌القضات از یک پرونده فساد
🔹
بعد از گفت‌وگوی رئیس قوه قضاییه با شاکی و متهمین یک پرونده مشخص شد شاکی خودش هم در پرونده متهم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/697439" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJv_x80tjvkke0I2dL8zSaVaD4dT_pouTK-8q1ppGRxnJMY5UfmqCFNrfuJGe7gU3SSIqN1tfgiN5oiY7-gQdbjKdZZn4C6kJp67BXc0nY5AQyC8NRsxBipIZls_cABc0F4qZDR1X6eFEplKpPYUPKqLzflKYMF05RFFvXhjyCWc4uFANQ_Rfi-be_8cMtS2tYwa_6ImXYf7se4LKorXEGJ1FmNxKyYqOhp0uYqiUWosyzWEc9kWc4WMTTT5SqBSNxzQg_R9YJt4z0TY9t1OOviGG6E6f_CuE0Jl2TOTL9ZUUZLXBq_3yUqlpHImXWkoSZWFjeqKbbccHTl4T3OBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم کدام استان‌ها بیشتر وارد بازار کار شده‌اند؟
🔹
نرخ مشارکت اقتصادی نشان می‌دهد چه سهمی از جمعیت بالای ۱۵ سال هر استان، شاغل یا در جست‌وجوی کار هستند. بر اساس این آمار، زنجان با ۴۸.۹ درصد بیشترین و ایلام با ۲۹.۹ درصد کمترین نرخ مشارکت اقتصادی را دارند.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/697438" target="_blank">📅 13:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnl98Sf1DYrn0Dl1kDBMfFaR6lHJkU83ROky6jWdcwdZsLdyaY_whklJYdWD3cfPUhRlfP8YZ8iNu8MQ7DR3nIzO1ZuKzVp9i0kLhbRQqzDrTGbCNkU-wAcHL_aDghLGpuJuxtFsHEMJVOnbvMPKecOaWq1YKRpL_MoYakfDsXaKxyGBjxNM-QycIHb8yKmGBfFd2smlg71MGp0tnyBWIV5eMzl70btzuTlZZilWXXXjRSTW-mck7W4Xp5kwtLbXbL44_RktZlNK1HrQlpw3oV8tCuxWr52lPcWGd12zFqC63Pgd6BTHWaT2ibRWZ3Mcw4teFXl6A2balInWAFk0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باز کردن قفل ویندوز فقط با چند حرکت روی عکس!
💻
🔹
به Settings > Accounts > Sign-in options برید، گزینه Additional Settings رو خاموش کنید و دوباره وارد همین بخش بشید. حالا گزینه Picture Password رو انتخاب کنید، یه عکس بذارید و حرکت دلخواهتون رو برای باز کردن قفل تنظیم کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697436" target="_blank">📅 13:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621ec04f67.mp4?token=eitcWNTy_e8ctARS_VMH-7JHBm8zP6xK-uQHkfx8ir5TS4gNO6Fz_v5-UfRSh-dkalpm4mj6MkJY531Xwlb-5qWyfo_gEzTisB7qeBxS8f3U7QFiv-_shXI8rEZplyoay9HRpFzq82I7Y74sXjRD1NckpGUIpGnSekrbCyYKs0QDHU3mbrJoHyjuhj0gs6rxVrurf1Dw4opfICgljha3SucS12u5kL1QKqVOSdC_Mcnwd4VO3sg0yCS7srWxr5mb1UMo-cn9jq8ggVrJA2S_GYAtotCSklz7B3b39QbZH7CcH7WYQZSsuZ7qt--jvudQEgwP6dHifKzBQTThuY4JzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621ec04f67.mp4?token=eitcWNTy_e8ctARS_VMH-7JHBm8zP6xK-uQHkfx8ir5TS4gNO6Fz_v5-UfRSh-dkalpm4mj6MkJY531Xwlb-5qWyfo_gEzTisB7qeBxS8f3U7QFiv-_shXI8rEZplyoay9HRpFzq82I7Y74sXjRD1NckpGUIpGnSekrbCyYKs0QDHU3mbrJoHyjuhj0gs6rxVrurf1Dw4opfICgljha3SucS12u5kL1QKqVOSdC_Mcnwd4VO3sg0yCS7srWxr5mb1UMo-cn9jq8ggVrJA2S_GYAtotCSklz7B3b39QbZH7CcH7WYQZSsuZ7qt--jvudQEgwP6dHifKzBQTThuY4JzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرکل سلامت روان وزارت بهداشت: کمبود برخی داروهای روان‌پزشکی جدی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/697434" target="_blank">📅 13:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_u2sktah874FTrm63t4VIJfAI3vem2LNniBP9WuPZLxUjVyxOnY1bugiK8E6YH2UghQgzdBwoLM6uZMSWa6Doq_oSA1ePCFYW58BmZ3XrUTAUGioU5NfhCXG5KKj871EXBDHWKe_8HGTPxD0INDG5M7yOPTxNt1NoIXscDry8MClkmMITSQtpJnNfRPI9aiIw_9rc0aN9aFOwh-g81FBifhvbDTHiILlGawqbxM5nfGQ7xuP4vpnt8Ey5Tc9KWHHhsKq6HpbZt6pz7v-aZShdLytyOTEHYE8xVT7XwaMA81pbCf4qlkFDjZszdYz-T4J_w2D8NFYvQCFqPggNIBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
جاعودی «مَشک ضریح امام حسین (ع)»؛ عطرِ ارادت در خانه شما
اثری هنری و بی‌نظیر که با الهام از نمادهای ماندگار کربلا و ضریح مطهر سیدالشهدا (ع) طراحی و پرداخته شده است. این جاعودی جلوه‌ای از هنر آیینی است که با سوختن هر عود، عطر دلدادگی و آرامش معنوی را در فضای خانه یا محل کار شما جاری می‌سازد.
مشخصات محصول:
🔸
طرح:
مَشک ضریح مطهر امام حسین (ع)
🔸
جنس:
پلی‌استر باکیفیت و با دوام
🔸
ابعاد:
۲۰.۵ × ۸ × ۸ سانتی‌متر
🔸
وزن:
۵۳۰ گرم
💰
قیمت اصلی:
۲,۲۷۹,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه:
۱,۹۹۰,۰۰۰ تومان
📩
جهت ثبت سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697433" target="_blank">📅 13:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZzk0xJWiO7XGN-XIFulk3OCsck1mGKy6z2b8SG8Z2cyHiUOs9qLfh4iHSgE64ctheEl4LLzB1XYJHKhwncAN3l3Z9o9U1247ucVZwdgLCzN2AX18WRpAzaiBTGyvPFSo_t7NfTNdBNeIzAAgprgg2dRDr3Ea9rPACDejSxGOGWccWu2qNazFCzGELDU3KF7l-bwmUg3XCLYrZ_UOilngMFZauryrvt7q_Mu-VbQ7H4S40UmCyvWfu6EMztqKPI-RCnG0PfWfwV8fwFXcUbRxssfhTczK9R4OQpZ3DlOx1fyQnpaI-35QIMTVYiVF9IYefKO2rkMwCJj_S_4IPOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری دومین رویداد پاراسوارکاری «جام پیشرفت»
🔹
دومین رویداد سوارکاری و پاراسوارکاری «جام پیشرفت» سال ۱۴۰۵ به همت فدراسیون سوارکاری جمهوری اسلامی ایران و به مناسبت گرامیداشت روز ملی پارالمپیک برگزار شد.
🔹
این رویداد ورزشی با هدف ترویج فرهنگ مشارکت و برابری در ورزش، نمایش توانمندی‌های ورزشکاران دارای معلولیت و ایجاد فرصتی ارزشمند برای درخشش استعدادهای این حوزه برگزار گردید. در این رقابت‌ها، ورزشکاران با نمایش مهارت‌های خود، بار دیگر توانمندی‌های خود را در عرصه ورزش به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/697432" target="_blank">📅 13:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رجیستری آیفون ۱۸؛ ۲۰۰ میلیون تومان فقط برای قانونی شدن گوشی | ماجرای جنجالی آیفون ۱۸ چیست؟
🔹
انتشار تصویری از هزینه احتمالی رجیستری آیفون ۱۸ پرو‌مکس، بار دیگر بحث درباره هزینه‌های واردات تلفن‌همراه و تناسب آن با قدرت خرید مصرف‌کنندگان ایرانی را داغ کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251543</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/697431" target="_blank">📅 13:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fec219318.mp4?token=kWUh4Eqr3b7PdbOme3tfhR7XCMj74L9GHLBpYe9pJkWcClhXqm1UjwSEbMaxKAjhHqSYKOuxUDUPoeqKfyssftpPgKE-UUneTxf9BHaADdfy3QjvmF4fGhibmjMxcrn7ns59zAP517BmC3UCUDMNW60-pwOSyuQQ4AASBDZ1mtZgbM3WGd5h1qLMZZQkAHONlaHVp80rINOIXZYb8Zc4NUBSwwy23qF-AwKqJazss7CRay5ty0dUJdX5uOSX_9gK9wzLPk3UWz483FujTOPXE0BFVCZ4U9kt3G_md5YHWJEWMdn00fjEfTRzJr3sp2QowH2NWEfWYuRE1CM-CeAuCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fec219318.mp4?token=kWUh4Eqr3b7PdbOme3tfhR7XCMj74L9GHLBpYe9pJkWcClhXqm1UjwSEbMaxKAjhHqSYKOuxUDUPoeqKfyssftpPgKE-UUneTxf9BHaADdfy3QjvmF4fGhibmjMxcrn7ns59zAP517BmC3UCUDMNW60-pwOSyuQQ4AASBDZ1mtZgbM3WGd5h1qLMZZQkAHONlaHVp80rINOIXZYb8Zc4NUBSwwy23qF-AwKqJazss7CRay5ty0dUJdX5uOSX_9gK9wzLPk3UWz483FujTOPXE0BFVCZ4U9kt3G_md5YHWJEWMdn00fjEfTRzJr3sp2QowH2NWEfWYuRE1CM-CeAuCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نپال باز هم اسیر سیل شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697430" target="_blank">📅 13:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd8ca7d3d.mp4?token=hkBFjPsrKlGHnXD6VvI_mH9oamn-NeENJHHYUppU29Q0yHcniEax9p5DHka3FB2d66pliVztcxY2dXEyYTOdQE1p9Ck5cwmEjTk8TQUBc0zsvbrLoLSYURF1by2OYTVKe56CRqbcgXKpPlPlXElisYVLO-iIktCmCvxTMkzkHIk9bqFkA9t1tuAWe7haZvNc1I7n2ehe-vvpY3l18HBHXr3uW10bG9w1V4LuDsk5aRfKHC5MSmzvRvChr4cMpw_kerAQCRTMs14Clkdw-0G7rwik-vdBK01W7-YYny6WDKo9MIbZovGuQR3UDU32jj6NyAdV1G8z5q16GO5tsQVbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd8ca7d3d.mp4?token=hkBFjPsrKlGHnXD6VvI_mH9oamn-NeENJHHYUppU29Q0yHcniEax9p5DHka3FB2d66pliVztcxY2dXEyYTOdQE1p9Ck5cwmEjTk8TQUBc0zsvbrLoLSYURF1by2OYTVKe56CRqbcgXKpPlPlXElisYVLO-iIktCmCvxTMkzkHIk9bqFkA9t1tuAWe7haZvNc1I7n2ehe-vvpY3l18HBHXr3uW10bG9w1V4LuDsk5aRfKHC5MSmzvRvChr4cMpw_kerAQCRTMs14Clkdw-0G7rwik-vdBK01W7-YYny6WDKo9MIbZovGuQR3UDU32jj6NyAdV1G8z5q16GO5tsQVbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا فکر کرده بودین چوب‌خط در گذشته چه کاربردی داشته؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697429" target="_blank">📅 13:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبرای ایرانی سربلند</strong></div>
<div class="tg-text">🔹
درآمد تضمین شده روزانه ۶۰ میلیون تومن سود خالص
🔹
راه اندازی خط تولید سوخت از انواع ضایعات
🤑
تامین تضمینی مواد اولیه ؛ خرید تضمینی تمام تولیدات طبق قرارداد رسمی
💡
نقد - اقساط ( بازپرداخت اقساط از محل سود خرید تضمینی )
مشاوره رایگان
◀️
02191007871
اینستاگرام
🔹
.
.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/697428" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11dd7913fd.mp4?token=u0JLroDD1UpviTJGydrOv3ZAVQ4aSXFTyCNpqLmNx1UpLF5jyxI2FT8VgVIuso4IpILQZv-1DjVvKm8HPt1dTsxZGdsStk1B11PYm9UOHxLEr8Cpz3Zogp90O7hd5xlUDcdTQZd14upUFaev7gVkPJcNRk7GJ4jaNJSnWC9nRAEqmqgT3F9LKv1fwv5DT-5vvmgfhZu5rnWX5LtVNrCnFPgMnHxdcr1n13Y0GSQFzNGQM1NUoZN-AHsoO9mmlpD4ccx2QGLQfRVqBJ6YMYB40WBRVcjdrofKk6G_othV3JzII9uMLXTf6vChhJLXWYN7ItKuGB86fZY_ujyw4G6Btw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11dd7913fd.mp4?token=u0JLroDD1UpviTJGydrOv3ZAVQ4aSXFTyCNpqLmNx1UpLF5jyxI2FT8VgVIuso4IpILQZv-1DjVvKm8HPt1dTsxZGdsStk1B11PYm9UOHxLEr8Cpz3Zogp90O7hd5xlUDcdTQZd14upUFaev7gVkPJcNRk7GJ4jaNJSnWC9nRAEqmqgT3F9LKv1fwv5DT-5vvmgfhZu5rnWX5LtVNrCnFPgMnHxdcr1n13Y0GSQFzNGQM1NUoZN-AHsoO9mmlpD4ccx2QGLQfRVqBJ6YMYB40WBRVcjdrofKk6G_othV3JzII9uMLXTf6vChhJLXWYN7ItKuGB86fZY_ujyw4G6Btw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا اورست رو در دل شب دیده بودین؟ ترسناک و خیره‌کننده!
🏔️
🌌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/697427" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwO-0jEtCDJmtIcMN-YS9EThoIgH6RH_uCJ589Stp3yT7Mz4Y8CnNlwEBW252yGpSOGiGbnsRO1De_nFmq3_PIsBkX76YOnD2ajXznl_50ybjSyeoeTKRviAF-oJkSzen8txeMBLul1cy5_0VpbE8ejTKu0lVJ8LRqkvJTEeHcMzPFbiCNx5DS7fjtM_VstI1nSGEyuPn28OTuJJOEd5MBD-XutexPV8_oeJm_DAVFfoG8qV0CaJX5Tki3hZiDUYkQvZI85SsEuitZqnkf08qmWEAuOjYYG_0Q47hk2uQQJ-KIFxx2UzJYtcdBhAJ8o8nbWHUc19KpLZr-K0v8pfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر دندان‌درد چه معنی‌ای داره؟‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697424" target="_blank">📅 12:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM2Gu_tdYpGs3il962ynnU8vB4q-bjv1g_TD75gdi7KBuDnvXiRc03K1pO7GuOZYttFPsxxuTpwtT5IvaebhAovWo1_EaWfynSMDDpLad9BUZckB8Cd2qVknawYfEckw4JPCYnuTyyIpjW7sqspDAScnO37DpMNRy0d65jmERJDM57_ox17pga6bzIiB60pcdxcMas6P1R8aCiF5wek6bsbbLBgzHR7_6N1fKr_BWoYz-GWTxMnJSQxNHqwKSCjJ4XUtgSZzJFxXLi_d8C_NEoFob1QlLjBUVdhehS1BvcZZgPETkXYzQr1vTRbRggoIXLZDJoYCuMa5mSibBJCWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش آنلاین طلا توسط بانک‌ها ممنوع شد!
🔹
ریسک بالای پلتفرم‌های طلا باعث شد بانک مرکزی ورود بانک‌ها به این بازار را ممنوع کند. اما حالا تکلیف خریداران طلا چیست؟
🔹
پاسخ مشترک بانک مرکزی و مجلس یک چیز است: صندوق‌های
طلای
بورس
کالا
.
🔹
در این سازوکار؛ طلا مستقیماً از بورس کالا تامین می‌شود و پشوانه دارد  و همه چیز شفاف است.
🔹
برای همین هم این روزها استقبال از صندوق‌هایی مثل
«
رز
ترنج
»
افزایش داشته است؛ صندوقی که ماهانه تا ۱۵
همت معامله می‌شود و تسویه بسیار سریعی دارد.
🔹
اما خرید صندوق طلا حتما از طریق کارگزاری‌های مورد تایید سازمان بورس است که امکان خرید و فروش آنلاین هم دارد،
آموزش خرید را اینجا ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697423" target="_blank">📅 12:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFLc8iQZNMqC1RgnGtES9R6h3M0wrMEQ_cRE-7w-Nbv1XsHvzfcFsV35MKMnGkHwrqRjlZ1L8q8O3oIMWkjKGSupXgeQ9Q1x0Aty62fPRmIX2HeF2ECCjXmVax3rXZCCvKcLL0bDJzuZdwgYh8Cr4bwkP_Q2IY6-2PKfgu1LwU2YJf16J21QBuTpQQ3-Fx2jQw2RE0LWJaWn4fisY5BqMSQyAT_mSoyu8d4kx96To9AZTh6eBZVSQDmpfh-00yXmMxFTYMW0hHNHSjEsl1BOePNx0CCy2pwGuqEbPHDtWhUtPBSHAfPCpsZ_QENwzdwSkVKwqKNozwxOCOLnbyU6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKprHht6WzSvO-4kVC4HZ1qcseek3GAK_GPBJ5mFuuDbCu_VHJ1sgVBCbxjM9_z260Z8IWyj394Ze1HuuXPydWgwxz0ufbRuhgGkltpPsGcy8AiJrWM27zQ6Akg3BkLnE91QSqQwucN75kczccI7Q-5bZ9T1ePErjU3CkF-cZH-NSM-pvOu8TxcAiJDxQF0oYIyeHREJByP07T0TfqEBzq9MXQ_fNdwfYgTRL72Lii29gMgwoEXMbYAnZwrgdrYfoFSeoDSvhjQ6qNLYBZ7xDd-BYiaDftUoU6GAi3RI3vhYgmCzWRjGEi_Hg7bSVYK0fryVoGGjhzzIdoDqA10TXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی با حرکت وینیسیوس که در بازی شب گذشته رئال مادرید باعث اخراجش شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/697421" target="_blank">📅 12:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۳۵ سیلاب خسارت‌بار از ابتدای سال آبی/ ۴ نفر جان باختند و ۲ نفر مفقود شدند
امید محترمی، سخنگوی سازمان مدیریت بحران کشور در
#گفتگو
با خبرفوری:
🔹
از ابتدای سال آبی تاکنون ۳۵ مورد سیلاب خسارت‌بار در کشور ثبت شده و ۴ نفر در استان گلستان بر اثر سیلاب جان باخته‌اند و ۲ نفر نیز همچنان مفقود هستند.
🔹
سیلاب در استان گلستان موجب انسداد ۱۸ محور روستایی و قطع برق ۱۹ روستا شد، ۱۵ واحد مسکونی نیز آسیب دیدند.
🔹
در استان اردبیل طغیان رودخانه‌ها و مسیل‌ها به تلف شدن ۷۵ رأس دام منجر شد و نزدیک به ۷۰ واحد مسکونی آب‌گرفتگی پیدا کردند.
🔹
تاکنون ۸۵۰ کیلومتر از رودخانه‌های اصلی کشور لایروبی اساسی شده‌است، پیش‌بینی‌ها از بارش‌های قابل‌توجه در دو ماه آینده به‌ویژه در استان‌های حاشیه زاگرس حکایت دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/697420" target="_blank">📅 12:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad255a96e6.mp4?token=nuVAmrDcbxthWwxnGeQgZ4PvF8TR-RnNPpqVBEQuZt28QFh2ZbNsFGuQY8T4eUlFnCip4kDK-nL9Kuxyc5fmZGR5RDeV6QvQDCytUxYa9hLtKTC86jNwa3QRCeiZgizHUTJJ6TR3bdO70A89sTb9CkL2N27W2ilzp77fKp0hRAhdKmtXyAGbiQXKIbyub72EOHaQAEgs-TyI2KCMYMv_TaIaXT1RG9voVamIVk_Osabyo-tEmqw8z8MTky14NKA41caf1zi7c4R8zYc578rmg2lfmHuIhcM9G_ECuZ2Z6twRqqcDOufZLeXEEF32DxPSu_U9JyQCs67Mt-8wTZPSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad255a96e6.mp4?token=nuVAmrDcbxthWwxnGeQgZ4PvF8TR-RnNPpqVBEQuZt28QFh2ZbNsFGuQY8T4eUlFnCip4kDK-nL9Kuxyc5fmZGR5RDeV6QvQDCytUxYa9hLtKTC86jNwa3QRCeiZgizHUTJJ6TR3bdO70A89sTb9CkL2N27W2ilzp77fKp0hRAhdKmtXyAGbiQXKIbyub72EOHaQAEgs-TyI2KCMYMv_TaIaXT1RG9voVamIVk_Osabyo-tEmqw8z8MTky14NKA41caf1zi7c4R8zYc578rmg2lfmHuIhcM9G_ECuZ2Z6twRqqcDOufZLeXEEF32DxPSu_U9JyQCs67Mt-8wTZPSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار احسان علیخانی با مرتضی مهرزاد پس از ۱۷ سال/ پسری که سال‌ها خودش را از نگاه آدم‌ها پنهان کرده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/697419" target="_blank">📅 12:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDDvJGMPLJZSqmw9kdsHJQ4uRvjaaKggYa01k9-t0mKYnR_eO--l56VqMMui6U6MNJos9NySWfi7q3571dpwDuaMEFyHS2-j9-fnXLwINNL6clF7_ESkUzpbssb3V3ocQ-KGKpQiDJKw7WOectbh1dkjhTjKyISBbp9FoTvWdORYk5RJkvowePTvOCCTzVypOgExQECVfdAIne2wXHxeOArASgwjykHv9UP96V25DJEES-pS6abZJgx4bu-W3QuIp_dvQJ1G6t9aXvCGhSzTgxypkWayPl5scOtG3X7NKxVtbXgzkrzs3-rjT8syU7MFdksYEA-2IYfts4-jLRjliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه جالب سفارت ایران در غنا به حکومت فرانسه
🔹
پاریس یک عطر جدید عرضه کرد؛ منحصراً برای افراد زیر ۱۸ سال. با رایگان‌سازیِ (پاشیدن) توسط پلیس فرانسه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/697416" target="_blank">📅 12:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de63b1897.mp4?token=P0iArn_e9jmfN_9GLoV-1nAAbb5agkLdxWyJkHxMRRKZM1FrVqVIYzGISb0plWIpjrHdAD4xpeUNMJOrDV-ixH7p3hA1uRc5wAoXA-iCVqU-ZyJycmwYpCZ8XnNsf58KQlSHSAf__pLZPBAvAmxfJIpjh3r5CUFsLyzlIwmN4d0b4OCqpvAzfkLluHPj6bhvFx6HjuagSbQqAxBld8wd1cWKFIimeWxGZckxxmlbeuam6Gg8PLO4Km-mKxz7woQGM-T5ySM4t4svJagYlfQ0znlAx7UWm_5dB6l2p1a935CcyE-s3Xje5CfPUANOzH5FpY-qkk2U8OjqsVgMRGI-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de63b1897.mp4?token=P0iArn_e9jmfN_9GLoV-1nAAbb5agkLdxWyJkHxMRRKZM1FrVqVIYzGISb0plWIpjrHdAD4xpeUNMJOrDV-ixH7p3hA1uRc5wAoXA-iCVqU-ZyJycmwYpCZ8XnNsf58KQlSHSAf__pLZPBAvAmxfJIpjh3r5CUFsLyzlIwmN4d0b4OCqpvAzfkLluHPj6bhvFx6HjuagSbQqAxBld8wd1cWKFIimeWxGZckxxmlbeuam6Gg8PLO4Km-mKxz7woQGM-T5ySM4t4svJagYlfQ0znlAx7UWm_5dB6l2p1a935CcyE-s3Xje5CfPUANOzH5FpY-qkk2U8OjqsVgMRGI-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای هوایی از شیری که به گله‌ای حمله و طعمه خود را شکار می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/697415" target="_blank">📅 12:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWWc0Httkx4QYESgy8mByroiaNbQorWY6R6twiWyoiRkKF-m38PNSTNGn_dloKfsNY720X_kmsYSpzdW7M3bjKy4UD3QIdx2POsdc5utLx-GwvxyUotAri9QDuggTQJ9EkYuHhO6GTw7e-jMdkbj3gScPlljv4JPs3hjuQUEBHC9X15YEFZZa3QYq4t3R5Bz64lu0HRu5v8suaUx_aNCDi1eR4ucaao6g5c1ekSJdBWOBJm_mjSKVa40CGF7dKxgWGm0nmsbEL5KvRflIPCABFKwl_Vi3J7W11viemZHqXT3HLOd96gQX7cejgPOsomanMZdp-Mm8vpyiKsR098HkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از اورانیوم ایران تا گازوئیل آمریکا | معمای سیاست دوگانه روسیه در جنگ | میانجی صلح ایران یا معامله‌گر با آمریکا؟
🔹
دیدار ولادیمیر پوتین، رئیس‌جمهور روسیه، با مسعود پزشکیان در ترکمنستان و تماس تلفنی بعدی او با دونالد ترامپ، بار دیگر مسکو را در کانون تحرکات دیپلماتیک برای پایان جنگ ایران و آمریکا قرار داده است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3251551</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/697414" target="_blank">📅 12:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3zHdfNjZ-w7tdjKAPhOLhxx5pBcmntbukBONeoTJtiZjKKQXFoZNZbWB2X5gE28vAupTjlf6gRL0GU2c_kBiChRb7huFy534__XwNI2jszbMXUPINyhBvpXIpo1hp_NnRy-WCdJIuvtf6ndWFDpKHvoNGIVpDEscnZ36C241SdSslkZsercbXIVMtXLSz5yWM_Fo0MW1hceDjJQkWyTg-jbmLy19l_WnkdayYTcJrpfBwuPWyUy6WCgaieLNNLM9wx-npZJup1oQxqeMSE35YUSmNctwwnr7gltbyFx71-2u0PWr31MLFIQIhIS5X1ACvGjNG4kNGSOiQ0bJheo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/loXapCa5EJPs7fj1IDe0aH30PQHdXhnZNSmbvFD0TTx7raPgTOzx3a0CKEFwuH7W7x9s-uUibd_menvIwFNrOZ5QWGSSLKGdoFZWbG9h4Ydpi2ak5rRl2n0y1EJWsZpTO6Br9JwVySl9CkYpuS4xCdAzPHGa_zeMBUJv4AQRyxkvNb7iz9fjDY5Nc7Xcbi9KaUkB5RlOMcvZB_iNMKUIRveVRMGK5JDtI5CM-tj8FoOm6tbRTMQ0SKXZtYml6nsUZiR2rOcniqkeLCN193vInPDMnXe_zyMiGLbKxeJ09lCkbdQx9u2eVhJz_hexg_tYQPcVXHlaSebjxJxrlfyJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7HW3uyLMvidxrTeBDucyNIM-YTxekTrMNp7mbkFUJzhkmrxyfvjQEsuwqj28VN3SPrFQCETn5iInH2aAGCXAj1KLyHXQ1aQcVVvUJ0I_b4q96tvViggAlp7cpRAjHIZSpP8iPI6PrK-fHcspHvqHEKgc-ipV8Z91pRRDgfyty0tqxhqq2EBchDLhD5pQLSKU3UtiQ5jhP7Kjx5qaWlPx5B30fGpVxIf6aPaRD7GSCyHDwJ0OAEgF6ZedWg8QljnnI9xLAkUqs9DkGSN4un028VS4C2H_pfjFcI86wwuH7wC9VWYm3VPm2dV2zJU_-ZUT0-KsCNc9Mx6U4JlvwqBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3qNvcV_dpbZOSm6h5_L-j_a-Vc8C-0tlbJ0b41BdR7RawBjA9JUCv4FBQG_VrxCkvPy2_MNcDqX4J1l4kYbEMZbfjdW2C6rrhKNmLzq4jU43dkUJoLyD2bqnmIguCtyhSMPFuS6M7_RcE_OGi1ShwHKJN8GwbHPvuro8r5ujZQBhNIABSFBYu71oU1qQ_3_Cv8KLZZRUDB-_WA8y8GAO4YYknW1Kuy0LawqnhPcQFfuUJh_4tCZf7iR1NgOu7maqM4-Lgqg1Y-vjHUQevlDc_90C6XppIJ8cdv7tYO8DGGaEUOAnbZlBTToySB1ez757PAtx5lanvQaaRU2Pe_oaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oS2GiOwJS6bgMfINBNtfMQWifPcCQjklv5AHis69jCByghAlbRFAU3-0Gv4YTKo3co4LTcZxC2-GMrFiPozKiavUtxkDCEcgGGb0W94HmrmQYNZX7Zy76qJTYE_PecolxlGSXDjwAsEZqPwc-9Mra0Ct2U9q_g3wMGQH1-mzXzqrMbJsEfZztbE3z5ilIsqoiubi2rQ2Ud9hPMc2vXOlJ8HpCBRo405R5Ce2a9Vp3TY2S8p9ePMHDAmRMa7qCaaUDDyR7rCb21KaCDKQ8QTEjZtrD8PY5Ir23kNzG3aAZu4eJGUFK9dVGEsNuwREJ9TFqDYER-5DqyXfXK8Ik3N00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huFf9BEXLX5Zd5HE7aGxdHHGkZ6xMx-O9IrwnD6jBzWpoCWB7LqYfXgscUkKTy4JI4eXgCLb95GDNa5VuFbv4edEsfWCVyDATsAmsVLwGw6zZpONLm5FhVJzRDvqVu_Y1jZoJm67yaq7iX8oHB9dp0Oznjmc6br9JRm72myvs0LURRN6I4JwMKUToiSUbNG1bgz3eesTKUT_6k5YZbCHPCww8VotinLtlS1GIk5oe1qYWugt5HMRiTC74tZ5hLj_6Vqd0QsDaHgQRMVDV39T0UVYum6WrvbtbWt1Rkvq9lyViOcnEmFq_GKvSsAIWyQsK_rZqAer_ex214prD2-ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwEeNMzq_Mm6mt7u8640IBViDnZF5hF6-_N6xjZ_u2m_4N9_IVYzxPMLbSjKIgGUzbf3Kqm91dTQohUsqCI9vZjavqsQ_jyC4kW1zDRKpEkYXkPSlAt7q71PivnndPYPnvwqIYqAoFY_vlc0SJIw0sLZHPRtYJlMatIXHNbtXOxN4-eYRGQaVnY6vAlos4hzsXjyybta7O7myTRjUXHfwfg-NyzFbXVqGJ4ODFJS3gozADkmN6ab6I9Mps-KUwtwU_ff5T7-CaUVkZpP8Hzz7WLmibWKuMDZ2984U3_khZkNslXyH5VRlTc0wncz6NWvAMzncMPlsqiNvO6RDSQMrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ده‌ تا از فیلم‌ها و انیمیشن‌هایی که هر پدر دخترداری باید ببینه
🎀
👨🏻‍🍼
#سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/697406" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLsUUNoNwYVMBl3qWI0n3W7hDeqni9Wg-Sme8WHAW6A3SS24rmiyhHriUohIs7tC0z87ToB4IbCmTq3PYiWjk24m19AGJt61iVo-a48B3PZAfhwxS7-uhmywHjfNT7jhl9GaSUEArrd0D4r9dNc_DAAHz7LaH7-yYqFHlOjdfQ0zqLg8CXHey9FUsi5rH_aH8NO7sPyWctlfokyJ7eeThehTW1UnVRB6Lm2LWFa715FQxRqRaAS1XWIQuf6jgUVfwVm2LFFeRDEEP1Bz7ISqZp74wsUgCu-TmPF5Gc7p64jthzWdTEZm9QLEqFAW6v_F6yHoQZl2j93MOLSmnmflJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697405" target="_blank">📅 12:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18b9d23b.mp4?token=V1vGyhwgXnh5ZJCz6sDaB3BznNp8lR2QK6hfmwQUsDgr245X4gSDHfGb_2KKNzECkumnxMYYioomuB2_165EfAX4wUgS_35-EFggwNoRSRZeK2OparQv6If8J4EVrZtOOinjdJDdAZ-thFV77X5hGnT9wrcJuyOdN7fqMzL_td2axCXvP8o2a687FKtIBMWtFJX7Ha1oppR-zPEo-IwRR8MWVebS83Qi6KgDNUR351beC_KamToyWqPJ2axvf9Rl5QhOyo_Ay-5ZkcmgpkvCDUuUEQbyEdmCYIieVfDTo3S6_ULLug9muHYgLGNO3FnertKi2-cp4KqY6-qT8SrNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18b9d23b.mp4?token=V1vGyhwgXnh5ZJCz6sDaB3BznNp8lR2QK6hfmwQUsDgr245X4gSDHfGb_2KKNzECkumnxMYYioomuB2_165EfAX4wUgS_35-EFggwNoRSRZeK2OparQv6If8J4EVrZtOOinjdJDdAZ-thFV77X5hGnT9wrcJuyOdN7fqMzL_td2axCXvP8o2a687FKtIBMWtFJX7Ha1oppR-zPEo-IwRR8MWVebS83Qi6KgDNUR351beC_KamToyWqPJ2axvf9Rl5QhOyo_Ay-5ZkcmgpkvCDUuUEQbyEdmCYIieVfDTo3S6_ULLug9muHYgLGNO3FnertKi2-cp4KqY6-qT8SrNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: سوپرنفتکش متخلف در تنگه هرمز با مین برخورد و در آتش می‌سوزد
🔹
عاقبت هر نفتکش متخلفی که قوانین تنگه هرمز را نادیده بگیرد، همین است. و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697404" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزیر گردشگری: طول عمر درختان چنار باغ‌موزه سعدآباد از حکومت آمریکا بیشتر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697403" target="_blank">📅 11:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE7kYCj3qo53rTQJMG2bwjWJdk1l91L2DMlm_uwpWOQGA-eKhEHRpF-3jjokXx7QNErZjQouHKoCt-nvEgTv-kfYdeVtfpJlwsQEp8tnZZqsxNc2o90xgzkxZ5e5SyR591daRkz94s4VLhDiRcmhG9bqDHUyXVHH--LiBNmRNIAjqR6fX2k74QpWOjoCOyqLmZ5iPg6Bu6RTB33ceqXF32wxRyTV8htLaMk47QcID7VxCVIpNouGJB-E7JvGYgqahhf4EQgDOR_aj1zM6vCz8iYUe_fy_5YkqVwJpTtWC4VBsrQaDASD5Bn_HFBMXQr9aPlTYlh1TmmgcRlFxntHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعت بیولوژیکی برای نوشیدن قهوه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/697402" target="_blank">📅 11:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
،
چله "چهارم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
|
محمد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697401" target="_blank">📅 11:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283eb4e2c8.mp4?token=eY02fkncF8jHTCBLGh6UcFyvSfbUiTdmJbJQH-GBHsM4EFUF30bXDfcddtuhpKTfRNlATklZ6foEeI-YgXF0qOVyvlLoCO06l24qh8HMH5oZBHn8HrNImiSzQK4uTcse-XsMtoMBM7FWM4bo-px0qrm-oyMpm0Yv8BGnPgWypn2iJqo80ENPQgYcfeuTseXQlXe14XYwPf6BOPidjZX9XzrcegyF8k0JGeRhcDynGnHSYD-74GjMjgu6PbTznKEvHuN0umXNPGrX0MfteioQpOjO_42Wm86_F18ccGAO_ax7JW8vwstbw2EN3E0tvCVyEqCzkmMgxTxxmC4EVleQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283eb4e2c8.mp4?token=eY02fkncF8jHTCBLGh6UcFyvSfbUiTdmJbJQH-GBHsM4EFUF30bXDfcddtuhpKTfRNlATklZ6foEeI-YgXF0qOVyvlLoCO06l24qh8HMH5oZBHn8HrNImiSzQK4uTcse-XsMtoMBM7FWM4bo-px0qrm-oyMpm0Yv8BGnPgWypn2iJqo80ENPQgYcfeuTseXQlXe14XYwPf6BOPidjZX9XzrcegyF8k0JGeRhcDynGnHSYD-74GjMjgu6PbTznKEvHuN0umXNPGrX0MfteioQpOjO_42Wm86_F18ccGAO_ax7JW8vwstbw2EN3E0tvCVyEqCzkmMgxTxxmC4EVleQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان جالب پزشکیان از پدری که زمان مرگ فرزندانش را نصیحت می‌کرد
🔹
اگر باهم یکی شویم و متحد باشیم، دشمنان نمی‌توانند ما را خم کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/697400" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbdf11e85.mp4?token=VkqnG8PKQPTaWiDeTpDipr8E4_CoHk_lrQZpFlFLTVXFOjJC4UERG2bzkc4QzeVO9nekTISzgSBy6lC9ACBlRO2P2ecuNAzxBQJm1yX_30uULvUGaApauKSgh4usRELG4GsuHFRlo8hbFWKzTVnhqUvALNiWx68F2pgdtrcCYR-G9x1SwqDI6BbwORu7d4JAwZPH-EYy_QH7SzQjYYccxc7cy9LMw35Uao-Y2Qsvz4inAQMmzILNextPGcqdhXIvxEhMS3DQhtepYXKUlXd6BPIRyDZnT2IlW0QnIsxGKeIIg-T1c_yShQuA5ERhIl1MrLIEClfgz4IoNj9SvDZBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbdf11e85.mp4?token=VkqnG8PKQPTaWiDeTpDipr8E4_CoHk_lrQZpFlFLTVXFOjJC4UERG2bzkc4QzeVO9nekTISzgSBy6lC9ACBlRO2P2ecuNAzxBQJm1yX_30uULvUGaApauKSgh4usRELG4GsuHFRlo8hbFWKzTVnhqUvALNiWx68F2pgdtrcCYR-G9x1SwqDI6BbwORu7d4JAwZPH-EYy_QH7SzQjYYccxc7cy9LMw35Uao-Y2Qsvz4inAQMmzILNextPGcqdhXIvxEhMS3DQhtepYXKUlXd6BPIRyDZnT2IlW0QnIsxGKeIIg-T1c_yShQuA5ERhIl1MrLIEClfgz4IoNj9SvDZBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب شور به‌ دلیل چگالی بالاتر، شناوری بدن رو افزایش می‌دهد
🔹
در مصر صدها دریاچه نمکی وجود دارد که به دلیل شوری زیاد، می‌توان به‌ راحتی روی آب شناور ماند؛ بدون اینکه تلاش زیادی کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697399" target="_blank">📅 11:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=UMqwBaTzsM-wLjX6E3vr_8Il9eiNxkRTF415PXN10U_tyGF0ElQ1syE9OiTH2lp3h1hJewNOrHVhwlgHL154VJZZfZzfIEv6R1_2_52TFFG1veQRkr3BXSwPPiSBcl14H2emIBo5TMU7k8MkLvx-HxMQ-xDzsJrOUfAlIlHTD-NasRz99Gb_ClbBUMcVtDZ-v6PiMfuVgPqGrVtudtUKpJpHipc5YHTf79fHkvAPv7WD8AVKpZnvdhCUfU3xyHVLP5Ffe9d2sLcsTUKSo3Gdu7Lomn4AVbnqa5upE8gLOzyYN3RIXYDdU8NeqgfKKdcmxgxyk-O0AX23Bunzofr8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=UMqwBaTzsM-wLjX6E3vr_8Il9eiNxkRTF415PXN10U_tyGF0ElQ1syE9OiTH2lp3h1hJewNOrHVhwlgHL154VJZZfZzfIEv6R1_2_52TFFG1veQRkr3BXSwPPiSBcl14H2emIBo5TMU7k8MkLvx-HxMQ-xDzsJrOUfAlIlHTD-NasRz99Gb_ClbBUMcVtDZ-v6PiMfuVgPqGrVtudtUKpJpHipc5YHTf79fHkvAPv7WD8AVKpZnvdhCUfU3xyHVLP5Ffe9d2sLcsTUKSo3Gdu7Lomn4AVbnqa5upE8gLOzyYN3RIXYDdU8NeqgfKKdcmxgxyk-O0AX23Bunzofr8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌زدگی و اشک یک دانش‌آموز از دیدن پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697398" target="_blank">📅 11:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXHsQhA9cfIWiVNCwhgK62VVfSHigjDqx0Fh2sqQhOXm7o93Ad6L63t9ai94yC4N-Qw5VAPMjqakM2GPDpBRMQycsW5Y0u3X905lwWhNEzuGwSX8fF7TJZtRmwRoV50DsP7EkuFJCe2WpIUtSDLJ0Mn-A6CK1qos7pReJzTMttvJub9NW5qUt7_39AmbjpCIeTtzRAHlr1fLN5kcZaHfsSs76GSYHoN1jnBYsDhOHDKOBpL9xV_w9X5gsrSNwvvY2V7NOo-cRAfUriGexchqTTCwlzz5CRTdbO_CKWjEB_GPI5ghCFg6Mp9OFaOlxuiUIIKF7O5-FEfii2_q4dKDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت بزرگداشت حافظ
«حافظ را با صدای شما روایت می‌کنیم…»
🎙
🔹
مخاطبین گرامی خبرفوری، برای مشارکت در این فراخوان کافیست یک پیام صوتی حدود ۱۵ ثانیه‌ای ضبط کنید. از حس‌وحال خود هنگام تفأل به دیوان حافظ، خاطره‌تان از اشعار او، یا تأثیری که غزلیات خواجه شیراز بر لحظات زندگی‌تان داشته است، برای ما بگویید.
🔸
همچنین می‌توانید یکی از غزل‌های موردعلاقه‌تان را دکلمه کرده و برداشت خود از عرفان و اندیشه حافظ را با الوفوری به اشتراک بگذارید
👇
#بزرگداشت_حافظ
@Ertebat_baforii
@Alo_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697397" target="_blank">📅 11:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=UNPAWXML0pE61Q4IHU8dv9EacRk0S1X0LcZyMeo6B1g_gNN_3gNrX4vKrZ_pwpzeXDusH4BF8iuxVLTOHuesh6-tbz0y3HzDrG--7ZU8i7SLNKmGU1QUOOZr-rnsqZO_AOiWxbi6dkbxuhhQVpbmSc9pgiM0MaIDM6btDVoE83sIdYx7FUOky_00IETeCBC8jo3ZxtGph12QmdGR6y2CS8Rsxcn6JYbCPpprE2_8Yb1YTjtDsdu6JLDpDF3cXbOMwIr50FUzCi_T-5Jxq455ETP4FnPXYEohFXeTXKBuMN3fX7MZWFObUkhw7i6iAnOJeQ6_LfxBJqZzfLE_lPNFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=UNPAWXML0pE61Q4IHU8dv9EacRk0S1X0LcZyMeo6B1g_gNN_3gNrX4vKrZ_pwpzeXDusH4BF8iuxVLTOHuesh6-tbz0y3HzDrG--7ZU8i7SLNKmGU1QUOOZr-rnsqZO_AOiWxbi6dkbxuhhQVpbmSc9pgiM0MaIDM6btDVoE83sIdYx7FUOky_00IETeCBC8jo3ZxtGph12QmdGR6y2CS8Rsxcn6JYbCPpprE2_8Yb1YTjtDsdu6JLDpDF3cXbOMwIr50FUzCi_T-5Jxq455ETP4FnPXYEohFXeTXKBuMN3fX7MZWFObUkhw7i6iAnOJeQ6_LfxBJqZzfLE_lPNFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین لحظاتی پیش در واکنش به پیشنهاد ترامپ مبنی بر مذاکره، مرکز داده یاندکس در منطقه ولادیمیر روسیه را هدف قرار داد و باعث از دسترس خارج شدن و اختلال در خدمات سراسری روسیه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/697396" target="_blank">📅 11:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697395">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
درستی یا نادرستی فروش ارز توسط بانک مرکزی
🔹
اخیرا بانک مرکزی اعلام کرده که به هر ایرانی تا ۱۰۰۰۰ دلار می فروشد. آیا این اقدام درست است یا آنطور که برخی می گویند خالی کردن خزانه بانک مرکزی و ارزپاشی و اموری از این دست است؟ پاسخ اجمالی من این است که اگر محرک رشد قیمت ارز، کمبود اسکناس در بازار باشد و بانک مرکزی از ذخیره اسکناس خوبی برخوردار باشد، فروش ارز کار درستی است و می تواند مقابله با این محرک باشد.
🔹
در شرایطی که وزیر خزانه داری آمریکا دلار ۳۰۰ هزار تومانی را وعده داده و تلاش می کند اقتصاد ایران را دچار فروپاشی کند، مقابله بانک مرکزی باید مورد تایید فعالان سیاسی باشد. متاسفانه کسانی که کینه آقای همتی را از زمان توئیتهایش به دل گرفته اند فرصتی یافته اند تا عقده های خود را بیرون بریزند و توجه ندارند که آب به آسیاب دشمن می ریزند در بدترین زمان ممکن و در غیرقابل دفاع ترین شکل ممکن. کاش اندک دوراندیشی داشتند اگر دلسوز این کشورند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697395" target="_blank">📅 11:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697394">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ddde1634.mp4?token=JcW_P-TwqmnF6efNvS2Pd_9GSWskE9UiaYplloOYV6k58e9TZl7L8g_VdglDUOXS-EsjpkMGXaEMYEsvIzJdfA6v82hmmWlWFP8W6i8NMW7zgLg01QFqXPkK4sxSMQGo-7ax-uguYyaiibj6o3LlOqFSgSxg5g4YyqrWgzJ9PfaZwpdbiuTRwjr6H6O0HzWQAktCNYtI-MGNGuFiJrQRVW8aUsHHI8opdFBkC6x0KqV2AW_CDoVS8sY2NzCUtD57GiIvTDY_15Lm4lQERGONKKeBPzI12BQ3xPcTiNwrckkREjv2H2hgfYBT-r_Ypou2NeLSwQbep96wqhCBmaDdUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ddde1634.mp4?token=JcW_P-TwqmnF6efNvS2Pd_9GSWskE9UiaYplloOYV6k58e9TZl7L8g_VdglDUOXS-EsjpkMGXaEMYEsvIzJdfA6v82hmmWlWFP8W6i8NMW7zgLg01QFqXPkK4sxSMQGo-7ax-uguYyaiibj6o3LlOqFSgSxg5g4YyqrWgzJ9PfaZwpdbiuTRwjr6H6O0HzWQAktCNYtI-MGNGuFiJrQRVW8aUsHHI8opdFBkC6x0KqV2AW_CDoVS8sY2NzCUtD57GiIvTDY_15Lm4lQERGONKKeBPzI12BQ3xPcTiNwrckkREjv2H2hgfYBT-r_Ypou2NeLSwQbep96wqhCBmaDdUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین میشه با قیچی آشپزخانه این همه کار انجام داد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/697394" target="_blank">📅 11:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697393">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em7fRneWvrdBd-KMokUsK--XlCjiV0iv0ePASXCyhGm_qaGPM1m_G8ujYvUHdGTQ7pooUDtVEnYMAvKkBzb-f30yqJr4IW3gbxGZwQH4jNCTORXlFdgnB1V6k8XriOmHoIHvw-jo2RdTibV3TXKqLzi-yjqbkctdlijFzDtBTDkHMjSdx_wx_wE9jYwwehr2jbNP31sydTaLaavUBXPOzDsizA03clW9e-SOa9uYanL6hGTSDo_3uJPUjoo8t_qY1Tg4uSBFQniFHYRT06SsYyA4kcb2Jp-2jBF87jXPzGjQO20xklOaQKxZclNCm9S2dMUYUUrSLPx0y1L8IePwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا انتخابات مسیر جنگ را تعیین نمی‌کند؟ | جنگی فراتر از میدان نبرد | هزینه‌های سیاسی ترامپ در حال افزایش است
🔹
جنگ هفت‌ماهه ایران و آمریکا، با وجود خسارت‌های سنگین نظامی و اقتصادی، همچنان در بن‌بست راهبردی قرار دارد. واشنگتن با تکیه بر برتری نظامی، محاصره دریایی و محدودکردن صادرات نفت ایران تلاش می‌کند تهران را به پذیرش خواسته‌های خود وادار کند؛ اما ایران، با وجود آسیب‌، حاضر نیست توافقی را بپذیرد که به اعتقاد مقام‌هایش تضمین معتبری برای اجرای تعهدات طرف آمریکایی ندارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251522</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/697393" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هشدار دوباره ارتش یمن به پروازها و شرکت‌های هوایی درباره فرودگاه‌های عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/697391" target="_blank">📅 11:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9548362d2.mp4?token=R5-O_2k4wURHQrTtaddDrLMd1TqqBYJY8fcBCmbWM7paw5Yd34C8jiABYdZMRz50H4R9HOGqdvp_aqKpiOcZBQ1AVgmrzgnxnTIkiN5M1C4Jr3SJDUCA5tB_gwbQYtSqCH3xlYU6t1SPfo8DPfx_dEqgeHHwLu5i-EAuyk-hgLhNklPSc3S8ztWhGnTbmhGkfvCi1atOrDAO1-BwFxd807TtrGut9jis3-QieHZHwH7861GO_vZAb5FRJ3TtwyeA86aak8dGR4mb7HiUyARsVTL-9h5TWmqI7Bd_-Qt8M7V2vZUHCdZEcVDmeUqWURYpvO4LNZpSwIAbxwEnspyz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9548362d2.mp4?token=R5-O_2k4wURHQrTtaddDrLMd1TqqBYJY8fcBCmbWM7paw5Yd34C8jiABYdZMRz50H4R9HOGqdvp_aqKpiOcZBQ1AVgmrzgnxnTIkiN5M1C4Jr3SJDUCA5tB_gwbQYtSqCH3xlYU6t1SPfo8DPfx_dEqgeHHwLu5i-EAuyk-hgLhNklPSc3S8ztWhGnTbmhGkfvCi1atOrDAO1-BwFxd807TtrGut9jis3-QieHZHwH7861GO_vZAb5FRJ3TtwyeA86aak8dGR4mb7HiUyARsVTL-9h5TWmqI7Bd_-Qt8M7V2vZUHCdZEcVDmeUqWURYpvO4LNZpSwIAbxwEnspyz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی بی‌نظیر از جزیره قشم
😍
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/697390" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
دستگیری ۳ تروریست جیش‌الظلم در چابهار
🔹
۳ نفر از اعضا و مرتبطین گروهک تروریستی جیش‌الظلم در شهرستان چابهار و روستای درگس شهرستان دشتیاری دستگیر شدند. خانه امن این گروهک تروریستی تحزیه‌طلب در منطقه عثمان‌آباد چابهار به‌ همراه محموله سلاح و مهمات شامل یک قبضه سلاح m4، دو قبضه سلاح کلاشینکف به‌ همراه مقادیری مهمات سلاح‌ m16 کشف گردید.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/697388" target="_blank">📅 10:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e117dc832.mp4?token=Q5yo5vzwFc9KE7g1ec7Fb5KC0sZ9PhTpba3Yv6WG-OIMk1irQo1_cE-HESb4Q4wEqXQxV6zE_iOzgho5zQ7-TUAe8zbe9twBnLegqkHTgSZ4rlLLSx2B5dSQ_IW4zyyJyH5BN71N2w1Ko1YfDfVpJgkVffHpLUzSPlmSihxPedUF6VEEXa1bqgsold6sN8lWbHHheIT6SqlR-PjibJ0uQtRzU4GTuupbsMAB99RtS8vFDpl8LqZjE03i8QErG9O4pPcGLs45jwrXpdCIwRSHCBA2G6M3BQOh2gMu9YPZCF-yjnKlbSBOlzx8o41wpYidU0ZSTr8LlE-s1cSFiKLHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e117dc832.mp4?token=Q5yo5vzwFc9KE7g1ec7Fb5KC0sZ9PhTpba3Yv6WG-OIMk1irQo1_cE-HESb4Q4wEqXQxV6zE_iOzgho5zQ7-TUAe8zbe9twBnLegqkHTgSZ4rlLLSx2B5dSQ_IW4zyyJyH5BN71N2w1Ko1YfDfVpJgkVffHpLUzSPlmSihxPedUF6VEEXa1bqgsold6sN8lWbHHheIT6SqlR-PjibJ0uQtRzU4GTuupbsMAB99RtS8vFDpl8LqZjE03i8QErG9O4pPcGLs45jwrXpdCIwRSHCBA2G6M3BQOh2gMu9YPZCF-yjnKlbSBOlzx8o41wpYidU0ZSTr8LlE-s1cSFiKLHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا هر بار جریان شما قدرت را در دست می‌گیرد، رفتار دشمن نه‌تنها تغییر نمی‌کند، بلکه در مواردی تهاجمی‌تر هم می‌شود؟
🔹
ظریف می‌گوید: «ما باید به‌ جای نگاه تهدیدمحور، نگاهی فرصت‌محور به جهان و محیط پیرامون‌مان داشته باشیم.»
🔹
اما سؤال اینجاست: هشت سال هر امتیازی که برای توافق لازم بود به آمریکا دادید و نتیجه شد برجامی که آمریکا به‌راحتی از آن خارج شد. هشت سال هم در دولت خاتمی از «گفت‌وگوی تمدن‌ها» گفتید، اما پاسخ آمریکا قرار گرفتن ایران در «محور شرارت» بود.
🔹
در دولت فعلی هم که به جریان فکری شما نزدیک است، ایران با دو جنگ بزرگ روبه‌رو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/697387" target="_blank">📅 10:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون حقوقی وزارت خارجه: ایران هیچگاه دنبال جنگ نبوده اما جنگیدن را خوب بلد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/697385" target="_blank">📅 10:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=aiJAzHhdUwW7ZtIiflw1lwDuK2kvdVSBkb-euaCiFkyw6wPVL9Ok6z-ZPAAz7iVK-K-yHIk5M7nEaY1CgpDt1bNUcxLbX3U3tAAjV7PcJEo5XJ-74OWwtrP3Xtf-3Ige1amBfnuPOdqdOe55BOO3YCXuDya1maFkXJ8yJxEJ4iTCvo0_mOIusMdqlyAvArkcgIXU1uwZdxu_BsPD25002T0aUxQSo9I3PjLjcggbqRKZ3rpN00qBQIYIYZaNecCnjz583IdbcFOnXLVK7-zK_GcLZDlzGSLZQVP5uC75wOOIl9sigpXisKS8rH7iYbQynQFL5O1QVprBJUSODOV14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=aiJAzHhdUwW7ZtIiflw1lwDuK2kvdVSBkb-euaCiFkyw6wPVL9Ok6z-ZPAAz7iVK-K-yHIk5M7nEaY1CgpDt1bNUcxLbX3U3tAAjV7PcJEo5XJ-74OWwtrP3Xtf-3Ige1amBfnuPOdqdOe55BOO3YCXuDya1maFkXJ8yJxEJ4iTCvo0_mOIusMdqlyAvArkcgIXU1uwZdxu_BsPD25002T0aUxQSo9I3PjLjcggbqRKZ3rpN00qBQIYIYZaNecCnjz583IdbcFOnXLVK7-zK_GcLZDlzGSLZQVP5uC75wOOIl9sigpXisKS8rH7iYbQynQFL5O1QVprBJUSODOV14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید باران و آب‌گرفتگی خیابان‌ها در گرگان، شب گذشته
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/697384" target="_blank">📅 10:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697383">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قبض آب ۳۰ میلیاردی برای یک مجتمع مسکونی در تهران
مدیرعامل آبفای تهران:
🔹
گران‌ترین قبض صادر شده در سالیان اخیر، مبلغی نزدیک به ۳۰ میلیارد تومان برای یک مجتمع ۴۰ واحدی در شمال شهر تهران در یک دورهٔ تقریباً ۶ ماهه بوده است.
🔹
عمدهٔ مصرف نجومی این مجتمع به‌ دلیل استفاده از چیلر جذبی بوده که طبق مقررات ملی ساختمان، استفاده از آن برای این نوع مصارف ممنوع است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/697383" target="_blank">📅 10:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697382">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مهلت ثبت‌نام چهارمین دوره جایزه ملی جوانی جمعیت تا ۳۰ مهر تمدید شد
🔹
مهلت ثبت‌نام در چهارمین دوره جایزه ملی جوانی جمعیت تا ۳۰ مهرماه ۱۴۰۵ تمدید شد.
🔹
این رویداد در راستای اجرای ماده ۱۹ قانون حمایت از خانواده و جوانی جمعیت و با هدف شناسایی، معرفی و تقدیر از اقدامات و الگوهای موفق در حوزه جمعیت، سالانه برگزار می‌شود.
🔹
چهارمین دوره این جایزه در هفت بخش رسانه‌ها، سازمان‌های مردم‌نهاد، دستگاه‌های اجرایی، شرکت‌ها و مؤسسات خصوصی، مدیران، نخبگان و خانواده‌ها برگزار خواهد شد.
🔹
علاقه‌مندان می‌توانند برای ثبت‌نام و کسب اطلاعات بیشتر به پایگاه اینترنتی ستاد ملی جمعیت به نشانی
www.setadjamiat.ir
و بخش «ثبت‌نام جایزه ملی جوانی جمعیت» مراجعه کنند.
🔹
این رویداد ۲۴ آبان‌ماه ۱۴۰۵ به ریاست دکتر مرضیه وحیددستجردی، دبیر ستاد ملی جمعیت، برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/697382" target="_blank">📅 10:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697381">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed39942dda.mp4?token=JF3Izw2q4LWq_GC4ZBlzH2UwRdUG8I7Z_jF3RWqFX6KlYnS2Y5sp35oxZVU7NweiQyM6izlu-GXGFlW45UOg4u8xHy-hf0qyT7aC4sPsOFo6xmggKnCXRhouuUle-LgAjcwmh5rL1bHTBcU28SYpSfEQeRszWndGfkmRtG_xUVyX5xohV47m0SyzkQbZCsz57Ejb2wucSopgtj_3yIXnBthCd3KmYY0CMcf6CjRJoL-DPXb8gm128CoTuGfrdUYFyEXzKwx2plEYPgrJK_4A9gGd2ey6A_pvrjq39B1DIJHJFIjwCPraobM96lLAbYFbnOgVZVhxDttRw4CU-e-YMmnS8CLLe5U2pRyTLZUMbM61gcDqzxAUp_2AXXAxFVljC6QpXZAz0uUwce2qekXHywCtJhfHos9zJMeOZ8CvI58YxQ2LMjMmhQGC8Dw8j3LBksl8QeC97TvAAxW8UBODsLqK8joD6tvvzXvb6T77iE5ET1yX0rttDTYVqFHOeuLCr3b5tC0DG6KgjvhwCqizEf6acsJdqCFtywtaGxfx_L5yzRwKVpcUQRrHCPyZHvuNyuaXNkkR5I_n8MnnBfJpG0fzhg3GwqoV3BoTg9ch0O_kcKN8ZQO-vuh9X81UaPAlP30Kf2CMv2BwD0wg7HMJe17Rv6qPuaojDScreBr4r-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed39942dda.mp4?token=JF3Izw2q4LWq_GC4ZBlzH2UwRdUG8I7Z_jF3RWqFX6KlYnS2Y5sp35oxZVU7NweiQyM6izlu-GXGFlW45UOg4u8xHy-hf0qyT7aC4sPsOFo6xmggKnCXRhouuUle-LgAjcwmh5rL1bHTBcU28SYpSfEQeRszWndGfkmRtG_xUVyX5xohV47m0SyzkQbZCsz57Ejb2wucSopgtj_3yIXnBthCd3KmYY0CMcf6CjRJoL-DPXb8gm128CoTuGfrdUYFyEXzKwx2plEYPgrJK_4A9gGd2ey6A_pvrjq39B1DIJHJFIjwCPraobM96lLAbYFbnOgVZVhxDttRw4CU-e-YMmnS8CLLe5U2pRyTLZUMbM61gcDqzxAUp_2AXXAxFVljC6QpXZAz0uUwce2qekXHywCtJhfHos9zJMeOZ8CvI58YxQ2LMjMmhQGC8Dw8j3LBksl8QeC97TvAAxW8UBODsLqK8joD6tvvzXvb6T77iE5ET1yX0rttDTYVqFHOeuLCr3b5tC0DG6KgjvhwCqizEf6acsJdqCFtywtaGxfx_L5yzRwKVpcUQRrHCPyZHvuNyuaXNkkR5I_n8MnnBfJpG0fzhg3GwqoV3BoTg9ch0O_kcKN8ZQO-vuh9X81UaPAlP30Kf2CMv2BwD0wg7HMJe17Rv6qPuaojDScreBr4r-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسه‌ها شروع شده و چه چاشتی خوشمزه‌تر از این شکلات‌های سالم و رژیمی برای بچه‌ها  مواد لازم:
🔹
آردنخودچی: ۱/۵ لیوان
🔹
پودرکاکائو: ۱ ق غ
🔹
خرما : ۱۰ عدد
🔹
بادام زمینی آسیاب شده : ۲ ق غ
🔹
شیر : یک سوم لیوان
🔹
عسل : ۱ ق غ
🔹
شکلات تلخ + پودربادام زمینی  #آشپزی…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/697381" target="_blank">📅 10:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXnd6iqa5U82PXp-sjqCRs8z5PtpqUuISBdiFDUrGLFwB8P6W2TFyFcVpOgRM0OLupvpfDYAtu6B0MaS7JmFmnwaXJ0myvEq6Pa96QK9xgDA5NlWq-bwey7eT7mKg05-jNX0eHV2Il9zz2Bh1q5wa4okd1L6kT60ybBAlIPaKdEUD0Sxx5euZHN3TL48VvPRRG5v_yWZOhaZP8z2XwJWZYfDe1vOZk0xxuRLy2y9BAXkQvXv_BUyNs0X1k7MQP2LRAhVnEjeUM-SVOc2WfueVGpLlgrfn0ThKkJRL_t3WeSqiEx2kvtwz96iy-3wyxmuvWUMYXZgMhIBml1WkU6Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نایب‌رئیس هیات‌مدیره سندیکای صنعت مخابرات ایران: گزارشی درباره خطر فروپاشی اکوسیستم ارتباطی کشور به مقام معظم رهبری ارائه شده است
🔹
فرامرز رستگار، دبیر و نایب‌رئیس هیات‌مدیره سندیکای صنعت مخابرات ایران، اعلام کرده پس از یک دهه هشدار درباره وضعیت زیرساخت‌های ارتباطی و بی‌نتیجه ماندن پیگیری‌ها از دستگاه‌های اجرایی، گزارشی درباره خطر فروپاشی اکوسیستم ارتباطی کشور به مقام معظم رهبری ارائه شده است. به گفته او، سرکوب تعرفه‌ها و سیاست‌گذاری‌های نادرست باعث شده درآمد فعلی صنعت ارتباطات پاسخگوی هزینه‌های توسعه و نوسازی شبکه نباشد و ادامه این روند می‌تواند کل زنجیره صنعت، از اپراتورها و پیمانکاران تا تولیدکنندگان تجهیزات و نیروی متخصص را با مشکل روبه‌رو کند./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/697379" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4713915c.mp4?token=vQu29gxw5idK05OtsbwZwd98VWmYwBE97bRaxuouNEQuwQXl67pI2xKO8Yf_CkVTO5J6xEnV9HDhfgQeuHg7ow3mWWntkKOHcvtm0SGrLNMcZKtTFcN2HU_GRDYu64jU82P0wA-4NoNxtpW79tcMN-PwaF_6ktEVWWeN88ExfnCE4V38jnyhoLQ4X1iZbLa0yjHfVYP5adrPufqG2t3MhisEkXRekhsFgCsUqe4ihHW1hpz8kWnqXdXVMcQGwAeSWldRD4raAsVy3z_JjvVhubBwdeSLqIKSSaDsgI7azRLbJqi5nauBeg93aXB3ho46QPnNMq4aefvrEJ5z128VBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4713915c.mp4?token=vQu29gxw5idK05OtsbwZwd98VWmYwBE97bRaxuouNEQuwQXl67pI2xKO8Yf_CkVTO5J6xEnV9HDhfgQeuHg7ow3mWWntkKOHcvtm0SGrLNMcZKtTFcN2HU_GRDYu64jU82P0wA-4NoNxtpW79tcMN-PwaF_6ktEVWWeN88ExfnCE4V38jnyhoLQ4X1iZbLa0yjHfVYP5adrPufqG2t3MhisEkXRekhsFgCsUqe4ihHW1hpz8kWnqXdXVMcQGwAeSWldRD4raAsVy3z_JjvVhubBwdeSLqIKSSaDsgI7azRLbJqi5nauBeg93aXB3ho46QPnNMq4aefvrEJ5z128VBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیلاب در بخش‌هایی از شهر انگوت از توابع شهرستان گرمی استان اردبیل  #اخبار_اردبیل در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/697378" target="_blank">📅 10:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مدارس ریاض، پایتخت عربستان، غیرحضوری شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697377" target="_blank">📅 09:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/80d3f98128.mp4?token=mupOQAv9U-AazDODOyJDnl07K8JM3D7HImGKh1xHzOJcLnO34TfVsYbK84DZRLJ2IlNOfUapUgCiBnIqj6WZr2YugbnOv1jAMMl0tmMPbhis6CMuNwPxxFf2l90GHrQGiAJ1Yur2GUUzJuxIS4tR6WSYX97Lp8m7h75hw5aLC2_U-yIcmMZVOulQbzNOJMNNY0QkthvaQCd-kBXG1bgoVLnqAoEXn6bqTaO8Fh6t7mo-NMkE1tJevwWatf1HhmD3OOq8aRIW44Ijm42jmKcEZQ2aQkgvhusx9fanNPih78Xj-NjC8zoUVEfAc66k_fPbfKh-Wqrh9GoX75oJajWSB21Jf2CtngIshKSpBe5PDXUd_KCXJyJk8OIrAILr41D7AWBs5WcjF9oZEfOM3nW7FG4dVDGaNXTGY4ma9WfSwcrChIN7mQDPaW1v5PAygj7whwtqzJAqvejEv6fBI9C8mxhCLzUH0ps2RaNUVZwn1ivUm0rXiZkq_sVvbYWlz5rZmn_yZbixvRz1XTsqBktex_vff404R2b15-2C-GFYSScO_9NJ9c1wk-w32VrZGhMDldETH6fGl4zsF9zj_7PumerGztKq1AygwhkI6bpFt0j_uLsLOTYfk0ZvFpSDttjr1kuGADHJTNYv12ghUuw4PadbIFG5s2xxt16PpveicHc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/80d3f98128.mp4?token=mupOQAv9U-AazDODOyJDnl07K8JM3D7HImGKh1xHzOJcLnO34TfVsYbK84DZRLJ2IlNOfUapUgCiBnIqj6WZr2YugbnOv1jAMMl0tmMPbhis6CMuNwPxxFf2l90GHrQGiAJ1Yur2GUUzJuxIS4tR6WSYX97Lp8m7h75hw5aLC2_U-yIcmMZVOulQbzNOJMNNY0QkthvaQCd-kBXG1bgoVLnqAoEXn6bqTaO8Fh6t7mo-NMkE1tJevwWatf1HhmD3OOq8aRIW44Ijm42jmKcEZQ2aQkgvhusx9fanNPih78Xj-NjC8zoUVEfAc66k_fPbfKh-Wqrh9GoX75oJajWSB21Jf2CtngIshKSpBe5PDXUd_KCXJyJk8OIrAILr41D7AWBs5WcjF9oZEfOM3nW7FG4dVDGaNXTGY4ma9WfSwcrChIN7mQDPaW1v5PAygj7whwtqzJAqvejEv6fBI9C8mxhCLzUH0ps2RaNUVZwn1ivUm0rXiZkq_sVvbYWlz5rZmn_yZbixvRz1XTsqBktex_vff404R2b15-2C-GFYSScO_9NJ9c1wk-w32VrZGhMDldETH6fGl4zsF9zj_7PumerGztKq1AygwhkI6bpFt0j_uLsLOTYfk0ZvFpSDttjr1kuGADHJTNYv12ghUuw4PadbIFG5s2xxt16PpveicHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با فواید پای مرغ آشنا شوید؛ از کلاژن‌سازی تا سلامت مفاصل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/697374" target="_blank">📅 09:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سازمان هواپیمایی مصر از تعلیق تمامی پروازهای قاهره به مقصد فرودگاه ملک خالد ریاض خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/697373" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697371">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وزارت ورزش و جوانان: حدود ۱۸ میلیون نفر در کشور هنوز ازدواج نکرده‌اند که از این تعداد، حدود ۱۰ میلیون نفر مرد و ۸ میلیون نفر زن هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/697371" target="_blank">📅 09:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
هزینه وکالت نقل‌وانتقال و تعویض پلاک خودرو چه‌قدر است؟  سخنگوی سازمان ثبت اسناد و املاک کشور:
🔹
درباره درباره هزینه‌های تنظیم وکالت نقل‌وانتقال و تعویض پلاک خودرو، حق‌الثبت ۳۰ هزار تومان، حق‌التحریر ۶۷۵ هزار تومان، مالیات بر ارزش افزوده حق‌التحریر با نرخ…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/697370" target="_blank">📅 09:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697369">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a3a9b8c2.mp4?token=r3zZW2Lf1oE6keHq7hyJv0yg8ZX90sCcsV4P_-Eu3ER9NO8LCwjjvlQmMXh5tk00Ba_Z_1Zs4FrSCO0zvBbIjRe3ipGzIvsK7cm1c_XeSHJmPxr0B5hww4eSXUmGFYa_uyuOZS8b245fRcIoW3ZGlW83_SKSMqoL_ny-Ni9GPC81rwvDMZwBwAA-M8rkUvpYI4F2saqAHXWZxufSTHIiCZtPrj76H7dK7FtjKTzazdKP8E8jJYtd18QtsSUFyZ16jj7LcEO_Jd5yGVteJ5tREUdeLEQPD3EsMZChrEMztmn_QJVQ9SJJf4N4pbMHn3QFg9StsgtiBI5H_gMLpAcBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a3a9b8c2.mp4?token=r3zZW2Lf1oE6keHq7hyJv0yg8ZX90sCcsV4P_-Eu3ER9NO8LCwjjvlQmMXh5tk00Ba_Z_1Zs4FrSCO0zvBbIjRe3ipGzIvsK7cm1c_XeSHJmPxr0B5hww4eSXUmGFYa_uyuOZS8b245fRcIoW3ZGlW83_SKSMqoL_ny-Ni9GPC81rwvDMZwBwAA-M8rkUvpYI4F2saqAHXWZxufSTHIiCZtPrj76H7dK7FtjKTzazdKP8E8jJYtd18QtsSUFyZ16jj7LcEO_Jd5yGVteJ5tREUdeLEQPD3EsMZChrEMztmn_QJVQ9SJJf4N4pbMHn3QFg9StsgtiBI5H_gMLpAcBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کسانی که حملات اضطرابی و پنیک بهشون دست میده؛ این روش می‌تونه خیلی بهشون کمک کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/697369" target="_blank">📅 09:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697368">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه بیستم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697368" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه بیستم؛ خیرماندگار
🔹
معمولا در بحران ها، وسوسه‌های ترس‌گونه سه بار به انسان حمله می‌کنند اگر انسان در ذکر الهی قرار گیرد می‌تواند تجربه‌ نبرد زندگی خود را بخوبی طی کند.
🔹
اگر انسان‌های یک جامعه در سختی‌ها بتوانند بحران‌ها را مدیریت کرده و تصمیمات درست بگیرند به ملتی توانمند تبدیل می‌شوند.
🔹
تحلیل و پیش‌بینی آینده دلهره‌آور است و انسان باید با مشاهده‌گری و استفاده از نور نامهای خداوند خیر و نیکی را خلق کند.
🔹
کانال ورود نور البر پروردگار، احسان و نیکوکاری به پدر و مادر و پرداخت خیرات و حسنات به نیت آن‌هاست.
🔹
نور مبارک البر موجب صحت و عافیت می‌شود،ایمان وباور انسان را افزایش داده و با ایجاد فرصت نیکی او را در جاه و مقام نیکو قرار می‌دهد.
🔹
به برکت نام مبارک البر سرزمین ایران، در برکت و رونق الهی قرار می‌گیرد روزی زمینی به روزی آسمانی وصل شده و این سرزمین سرشار از نیکی، گشادگی روزی و آمرزش خداوند می‌شود.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/697368" target="_blank">📅 09:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هزینه وکالت نقل‌وانتقال و تعویض پلاک خودرو چه‌قدر است؟
سخنگوی سازمان ثبت اسناد و املاک کشور:
🔹
درباره درباره هزینه‌های تنظیم وکالت نقل‌وانتقال و تعویض پلاک خودرو، حق‌الثبت ۳۰ هزار تومان، حق‌التحریر ۶۷۵ هزار تومان، مالیات بر ارزش افزوده حق‌التحریر با نرخ ۹ درصد معادل ۶۰ هزار و ۷۵۰ تومان، هزینه صدور الکترونیکی سند ۳۰ هزار تومان و هزینه اوراق نیز ۳۰ هزار تومان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/697367" target="_blank">📅 08:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd947e503.mp4?token=TeNgfWIcDCr-0kigzOuLlzIgZ754Z-sYNRJ28cCxK7MV1sJk8EbGURHHuvrkBgxeBBUD-KaH2o9h9ZDC2z4fG2T-9NwblYl-vI1BiGHDWFoUBY78gVULEH6mcsQwxLNxAk-CUhuDejlRGDTLGMvcyWXlcMdRB3a-gHNjeu__z5qy6Ts1uBV92ocgZZiTPIHl_lVS37aaTlfx2IgaqBtV6P--iLub7h_k6aovZNTx90zw2EaXtB4nGBEzsu_yoO3vXZrQ8T8DLjJLQMzmtlzQXM-Pa-hsQNYfyhqxpVzCwK86Cdm5-uVeP_Jc0fYATC7MVbK1tl5TSglsIhxjFpwawg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd947e503.mp4?token=TeNgfWIcDCr-0kigzOuLlzIgZ754Z-sYNRJ28cCxK7MV1sJk8EbGURHHuvrkBgxeBBUD-KaH2o9h9ZDC2z4fG2T-9NwblYl-vI1BiGHDWFoUBY78gVULEH6mcsQwxLNxAk-CUhuDejlRGDTLGMvcyWXlcMdRB3a-gHNjeu__z5qy6Ts1uBV92ocgZZiTPIHl_lVS37aaTlfx2IgaqBtV6P--iLub7h_k6aovZNTx90zw2EaXtB4nGBEzsu_yoO3vXZrQ8T8DLjJLQMzmtlzQXM-Pa-hsQNYfyhqxpVzCwK86Cdm5-uVeP_Jc0fYATC7MVbK1tl5TSglsIhxjFpwawg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن لگویی، این بار مارکوی غارنشین را روایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/697366" target="_blank">📅 08:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb16b9252.mp4?token=C_vj_zq80N9At73hkDCGXZVL72OzbDXNv_0_EEZvNUQYT-Jd-ssRKIZxU3ZNyP64lEUkPTjw-SLeP_ox7T5raSsrhi14VhuCEr8nsBC6Tu9ndapWXRKZbjoy25-Ylur4J6imyxMX5sgjzMBgmkzgZuDuuAolOgFGlBe3Tb1tXctlza5srIL8uFt38f8y_I58UVS1eBRrxcr4rt3Ab6DB-llBj3jiX5o-NcHqIURP2JW6CzTDxzWngX_1vkUUxb-hrRn1HLcO_Sx5dztgigiT7dThdT7jY8an0Og3aQlnIXtctnQ90XW7QxYcFJe0FVRHrqUVRJVsGqm5y0D-21GkYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb16b9252.mp4?token=C_vj_zq80N9At73hkDCGXZVL72OzbDXNv_0_EEZvNUQYT-Jd-ssRKIZxU3ZNyP64lEUkPTjw-SLeP_ox7T5raSsrhi14VhuCEr8nsBC6Tu9ndapWXRKZbjoy25-Ylur4J6imyxMX5sgjzMBgmkzgZuDuuAolOgFGlBe3Tb1tXctlza5srIL8uFt38f8y_I58UVS1eBRrxcr4rt3Ab6DB-llBj3jiX5o-NcHqIURP2JW6CzTDxzWngX_1vkUUxb-hrRn1HLcO_Sx5dztgigiT7dThdT7jY8an0Og3aQlnIXtctnQ90XW7QxYcFJe0FVRHrqUVRJVsGqm5y0D-21GkYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ تمرین ساده برای کسانی که گودی کمر دارند #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697365" target="_blank">📅 08:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
به گزارش میدل ایست نیوز، دو هواپیمای عازم ایران پس از دریافت‌ نکردن مجوز ورود به حریم هوایی کشور به دلایل امنیتی، به فرودگاه نجف عراق بازگشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697364" target="_blank">📅 08:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شرط جدید افزایش اعتبار کالابرگ برای ۴۰ میلیون نفر اعلام شد/ مهلت ثبت‌نام تا سه شنبه
سازمان برنامه و بودجه کشور:
🔹
حدود ۴۰ میلیون نفر از هموطنان (حدود ۱۸ میلیون و ۳۰۰ هزار خانوار) پس از تکمیل فرم خوداظهاری و ثبت درخواست در پنجره ملی خدمات دولت، مشمول افزایش کالابرگ خواهند شد.
🔹
سازمان برنامه‌وبودجه: سامانه دولت من فقط برای کسانی فعال است که پیامک پرسشنامه برایشان ارسال شده است
🇮🇷
✊
@AkhbareFori
| Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/697363" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رائفی‌پور: روس‌ها به دنبال این هستند که ترامپ دوباره رای بیاورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/697362" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
طوفان «ایسایاس» در آمریکا ۴ کشته بر جای گذاشت؛ صدها هزار نفر در خاموشی فرو رفتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/697361" target="_blank">📅 08:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_wlRTy685tt5LMdm0Sl-0YO9L0kvemkd-ujdhO7y5OkpDBcafSnpaxq3Pi92Yb1bjCcxcFdn_BVt_Mxu1cmtBXwH_QH_WiNMGaJuGIyVd0E0P7Dhfufx5PrPt6nTkAjxOCox3NXNYWnv73ofqHRerPsd7eFtF7TT9wzLcDjxqEYzuerBVn3yA8GpxpVQJ2pUqs92Z3ayovJbjN2TY7l1WnLUeLbYeiKKLJqJh-9-GAkPKgrF_kKZM7ysgVWt4mvZr7jZqcP6Q10pCkTZay2ui-keqHFWe_q5yo8EiXKiZ1J6pDRFKMlxUmve1hgJMiK_D14G0FZdSsTONly8BrA4_ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_wlRTy685tt5LMdm0Sl-0YO9L0kvemkd-ujdhO7y5OkpDBcafSnpaxq3Pi92Yb1bjCcxcFdn_BVt_Mxu1cmtBXwH_QH_WiNMGaJuGIyVd0E0P7Dhfufx5PrPt6nTkAjxOCox3NXNYWnv73ofqHRerPsd7eFtF7TT9wzLcDjxqEYzuerBVn3yA8GpxpVQJ2pUqs92Z3ayovJbjN2TY7l1WnLUeLbYeiKKLJqJh-9-GAkPKgrF_kKZM7ysgVWt4mvZr7jZqcP6Q10pCkTZay2ui-keqHFWe_q5yo8EiXKiZ1J6pDRFKMlxUmve1hgJMiK_D14G0FZdSsTONly8BrA4_ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین
ترامپ دیوانه به ایرانی‌ها: ایرانیا میگن همه رو می‌کشیم، بعد میگن الحمدلله الحمدلله
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697359" target="_blank">📅 08:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=CqMWsrbpvgG6BvjEfU2rMkD4g89KQWkIfhWoujKF65F8fdTsp-AMmThXzWR2qerFMb8rJPK9mFUI7q8MGftGTmUkpx8mgnvS33-u7DzEXg9QQoJ6_aqvmPQpgbGLVxQaVZptIMFHP4xpAeAR-F-PdANQcZZB6uEOiO_XrsbZqW1xwCULcW1kUQye2ElBU2NsG1n1MBMlQu2zo2KG77RU7_8IYTF08OFdzrRS7fDSPvQ7VH91EQt0OwvHjj1ot8dOlT4Q5Fnc6IFmVEvgP_9DAqaD2yghWUmI2yUzgvDqVOuAtH4-RFZlPRqW1ChoP6g1XslFj5PysMmk1z-2c8sqQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=CqMWsrbpvgG6BvjEfU2rMkD4g89KQWkIfhWoujKF65F8fdTsp-AMmThXzWR2qerFMb8rJPK9mFUI7q8MGftGTmUkpx8mgnvS33-u7DzEXg9QQoJ6_aqvmPQpgbGLVxQaVZptIMFHP4xpAeAR-F-PdANQcZZB6uEOiO_XrsbZqW1xwCULcW1kUQye2ElBU2NsG1n1MBMlQu2zo2KG77RU7_8IYTF08OFdzrRS7fDSPvQ7VH91EQt0OwvHjj1ot8dOlT4Q5Fnc6IFmVEvgP_9DAqaD2yghWUmI2yUzgvDqVOuAtH4-RFZlPRqW1ChoP6g1XslFj5PysMmk1z-2c8sqQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به هواداراش: این فوق‌العاده است. من می‌توانم احمق‌ترین حرف‌ها را بزنم، و شما تشویق می‌کنید
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697358" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ترامپ متوهم برای هزارمین بار: ما در حال بررسی این موضوع هستیم که نام تنگه هرمز را به "تنگه ترامپ" تغییر دهیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/697357" target="_blank">📅 08:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
دانشگاه علوم پزشکی گلستان: حادثهٔ سیل در برخی شهرستان‌ها از جمله مینودشت، تاکنون یک فوتی و ۲ مفقودی در پی داشته است
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/697356" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
