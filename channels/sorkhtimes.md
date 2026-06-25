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
<img src="https://cdn4.telesco.pe/file/PNRG_etRpTTkm3zzmu73fUlJOexZP4TUnPXM6UM2Vu-jg7bCVnMB5tI1fYgIcWZWpuD4ZHewd_JWe9knVuytuQ4vzLD0LTIMwO1KWeXLIq0-u7J9TV2FlBJWuWIJwPuziSr77727bZe0rbUFXO3XUR6n_MIfYgXzqheN3DJlZdfHBOJ4bxU85nH8b3MZUvE6y8Eot4T_JeMn6HEzBI8tvxlMg5CSa8Kc7IXeGwwWS4McoUO1L-Jjbe9wC6-OYrRJm9hVLTLtmzrJ_dk_FZoHHD73Xrve-Qa-kvIr-lZoN8EHYSv5JPUy38cAsVfR-ydawEZyQZ7SBYvvd6xdEycvPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 01:45:57</div>
<hr>

<div class="tg-post" id="msg-134297">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaBjxE9GmcgYfWQIp06hs6OCb-UFaL8O__oIFnu1CRYpBSnteNVpYgwbiWAlO1CQh-QxlmP9m2vak0XBsWvsJFIJE6Fs9QbsFABDwIhNQIHNkT6oklTnvJfqJF2RETiq0EbeoyeSgasyq-d1twhyzepszpGVSzqeH3lIvQS6EwcX69mqlNPlQxyIc-LGEiNNa5X9YPpVuBrDNM3CK8u8rIOi1-J9czR0TleoT9dRt6va48zWxnTh-3DZMKhJ8nCq1XBThCvdcjdn6ELdwc3gitDZViFdiMBem_Vrs4y4I4hbxtoIg_1iJbW7cticEf3xowuSQopm5kYmj3yTqZbqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه D جام‌جهانی ۲۰۲۶
[
آمریکا
🇺🇸
🆚
🇹🇷
ترکیه
]
⏰
بامداد پنجشنبه ساعت ۰۵:۳۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 462 · <a href="https://t.me/SorkhTimes/134297" target="_blank">📅 01:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEOZl0UoP2NWy85o0fG3dm6ESsaW2VH_eO0ZRvolYmQYSX2bbvWd0mMsme30C0OiXRQGcwWVyj1faShfA2Wi8LxVpBsgzFwwXrfVDkSJY1khhLj_OGT8Kwpzz6BIqL7vI6RndaVypSH1hPIFQrBO-s7pFt3ritBizwKMVceuxCknjqzu3DR9U3RMuSG2XSPSdZK7w0fwaPaT-OlaXp8mWNKLyTR7Ufxii8CdAcKbW8c7tk13_Fe7iZ-meJrCcGKcAHfjQxjae-uJeQnpwqCjRuwanU5r91JnwqoqZAicq525HWtygQP4zAr7i6b28yEHVUg-zDuJ5RRk79_CbZ9BPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پورعلی گنجی مشکلی برای بازی با چادرملو نداره و میخواد با دست بسته شده هم برای پرسپولیس بازی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/134296" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
میساکی:
✅
جام جهانی رو میدادن به خودمون، بخدا بهتر از آمریکا برگزارش میکردیم.آمریکا نتونست میزبان خوبی باشه.
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/134295" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134294">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
ترکیب احتمالی تیم از دید ورزش سه:
🔴
رفیعی
🔴
معامله گری، ابرقویی، پورعلی گنجی، گرا
🔴
عالیشاه،باکیچ، سرلک، عمری،
🔴
بیفوما، شکاری  نظرتون چیه
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/134294" target="_blank">📅 23:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134293">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fafbef8e3.mp4?token=Jv-Lomx9Qug4g9qOWrQzoXuN4vVsC4lff782-Mz9U-UYHbc5VboyJ4KNArFaxmo2Xs5iAAQybKT_g0Pogjr2HCn1lCGVPci-FMzE0B_TvMruU4leCYGl8KYydw3CiQKENdhRjz2vXLHmT7CEBWvE1V1Setli0mb0-N3BWf-hmsuWYtYaJ3sjJnD4L4bZ9DyOlRFPXfN9mQecSSjukYevW3nEdMO0ZlgR8Ryp1TzebtVecu4g6DV8JE5lQgEkm4hOQgxgE6uy5t9Cjr3O-iIYNFG-mvrpDu409iIk6S7y0KAX2flwsBdgtl77AbeD-MNQ4sVUWmgjpOHvrdnoGaNP-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fafbef8e3.mp4?token=Jv-Lomx9Qug4g9qOWrQzoXuN4vVsC4lff782-Mz9U-UYHbc5VboyJ4KNArFaxmo2Xs5iAAQybKT_g0Pogjr2HCn1lCGVPci-FMzE0B_TvMruU4leCYGl8KYydw3CiQKENdhRjz2vXLHmT7CEBWvE1V1Setli0mb0-N3BWf-hmsuWYtYaJ3sjJnD4L4bZ9DyOlRFPXfN9mQecSSjukYevW3nEdMO0ZlgR8Ryp1TzebtVecu4g6DV8JE5lQgEkm4hOQgxgE6uy5t9Cjr3O-iIYNFG-mvrpDu409iIk6S7y0KAX2flwsBdgtl77AbeD-MNQ4sVUWmgjpOHvrdnoGaNP-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی: بنظرم ایران می‌تونه مساوی هم به راحتی از مصر بگیره و صعود کنه، با بازیی که جلو بلژیک کردیم بنظرم میتونیم سوییس رو شکست بدیم و صعود کنیم حتی به مرحله یک هشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/134293" target="_blank">📅 23:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
همون همیشگی
🔴
موعود بنیادی‌فر داور بازی پرسپولیس و چادرملو شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/134292" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134291">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/134291" target="_blank">📅 23:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
با اعلام سازمان لیگ دنیل گرا برای بازی فردا مشکلی نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134290" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134289">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
محمدحسین صادقی پس از چند روز عدم حضور در تمرینات پرسپولیس، اعلام کرد به دلیل مشکلات خانوادگی فعلاً به تهران نمی‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134289" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134288">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوتبالی :برای بازی پرسپولیس و ذوب آهن دنیل گرا  مدافع راست خارجی پرسپولیس محروم بود و نمی‌توانست بازی کند اما بازی لغو شد
🔴
حالا باید دید آیا مدافع راست خارجی قرمزها می‌تواند تیمش را مقابل چادرملو همراهی کند یا محروم است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/134288" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134287">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNDbIrMD4dEV3tcGKmdOVsrnj1nq8XS7Rft-PIMF-_c2R2vhOaXCA3zoKPmfiiUl4ENPXH03jeD5G4fuE91Awm9g2iywPQ458rEVbvZqTEiOgtr97B0fecHqpCioukHh2ihoRd2uU7rdJ_c5u5Qw0RpE9sB-0MfYBanIS-Ybl0N6CqjMgTj2A_rsH-fy1bfFeB0u-jHRZLsFT6iYp4rwIQrK6-wXT9wSzMdWRkuFtbVOMotARgE58YJJT94pVMsdMQu1t8zFFHCrU20BDXAgOwl4GMEiKtvx5yN-exaIjEoRdY_T7z6_tjtT8-JoSJpgUlbHszJYY_smueRuICLSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جدول خروجی‌های تراکتور در سایت ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/134287" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134286">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/134286" target="_blank">📅 21:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4WOnCjXXOUuTU-renF3pQfgIkAagduWyEjdCWmkc9X7_X2EXXyS23it26WuclT1tiPaZN8NjKQmqQh4IICBTIxvNiic4lhZCge3lJnkA-x4wIC2VjdZ-Dby04tnmmoQiSva0E-9XnrM1pA2A8F6TOaxVwIl43jRa1Piy-OYavvy4CHvx1hLdTe5wyNupafkJBTWfCeNTEvGo9TDVS1qoMC9Y3jJHIGFuyUtcHdRgwTZgolUckZdRskCoNGwl2JCF0aMqslhkIoorMEtyuGbb6w9aRlVh5pGEa3A-_MbdGayw2T6aGByQaxNqlrMnF1nFK2f5cG0AxMxqre7z9DOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بازی پرسپولیس و چادرملو درصورتی که مساوی به اتمام برسد مستقیم به ضربات پنالتی خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/134285" target="_blank">📅 21:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134284">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
او پیش از این، از تمایل به فسخ قرارداد بدون دریافت غرامت گفته بود اما اكنون خواهان دریافت غرامت شده است و خواهان مبلغی از قرارداد فصل آینده خود شده است.
🔴
البته او خواستار مبلغ بالایی نشده است اما به‌دلیل اینکه، او و دستیارانش ۴۰۰ هزار دلار طلب دارند و مبلغی…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/134284" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0xgvhQMMlLtXxZa4p0prUYGm2guXDl9o5NW7oBkstQdiWMmrw4am2BEbfsv-InLen3rO-wVqqTc5F4EdMcBlM6T9uX0axSJH8HhoR37is6XHywo46xYzbeMoD5kK_Lolr1mZBycnD8dlKWuzXiFR8KluLo6Sr4Pv98ft-bzN80Q_C29AQLlkg8F9pVhk-0YHO8Tdc9dzs0fShiUrgDv1gVHfc6kidt0A6Cxnb2k5Rk3PnlIC0q1Cq2_-xFtqp-zmuVUzIOo2uz8hrKLBGec_J_B4Cgs9oJaYSRYHDiqnxHee2gH21rzy4rcAOv3-c7gQmhhmvmxr17er7xwBTITCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدارهای امشب و بامداد فردا جام‌جهانی رو در وینکوبت با بونوس ویژه پیش‌بینی کن!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/134283" target="_blank">📅 21:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3H31nPC7Wtl34WVnQ1G5zL370ovivBYYPo56oWX74lZ-dCsVtDiNS4LHB4M0lT9r-iXR8nSvoh4fDSK366EA6grlGGjkKmUCSPCFXrYHZDx_apEe-xq4LH3YQukweoRQBdQTkKbYYCT1JztACnh7RGycoq6Hnseuf4ArOY6U4Ai-WOEFOqqevAmuNt0Cq0l_xjnrZiy1-uOqc8sssQee8Mh9VYVtylo2w6foK-I3RSEIF3FmGzJloOteW3VrE1a-JiH-uE16122zuzTJ1sTpI3dpUnrj1vl7CHXwwkBlfP18_gU7ZsRNXdOGK1SGN1zeOmKUEsL5R3W3Vxh8RtXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شاگردان اوسمار امروز آخرین جلسه تمرینی خود را پیش از دیدار برابر چادرملو برگزار کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/134282" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134281" target="_blank">📅 20:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/134280" target="_blank">📅 20:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🔴
🔴
#فوری
🔴
سرمربی پرسپولیس در فصل بیست و ششم لیگ برتر خارج از دو گزینه موجود نیست
🗣️
یا اوسمار ویه را بعد پایان پلی اف همچنان سرمربی پرسپولیس می ماند
🗣️
یا اسکوچیچ در صورت توافق رسمی و محترمانه با اوسمار، به عنوان سرمربی فصل پیش روی قرمزها فعالیت می کند./مهدی…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134279" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
فوتبال جام جهانی و نشون ندادن به خاطر والیبال ..خود والیبال از ست دوم قطع شده و دیگه نتونستن از جایی دزدی کنن و پخش کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/134278" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🔴
ارتباط اوسمار و مدیریت پرسپولیس وارد چالش‌هایی شده است.
✅
به گزارش خبرنگار قرمزآنلاین، روابط باشگاه و اوسمار حسابی شکراب شده به گونه ای که ارتباط مدیران با این مربی قطع شده است.
❗️
البته خلیلی به عنوان سرپرست موقت و معاون ورزشی همه روزه اوسمار را در تمرینات…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134277" target="_blank">📅 19:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/134276" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134275" target="_blank">📅 19:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134274" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
بازی تو نود دقیقه تموم بشه مستقیم می‌ره پنالتی و وقت اضافه نداره این بازیهای سه جانبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134273" target="_blank">📅 19:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134272" target="_blank">📅 19:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134271" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
🤍
دنیس اکرت و جام‌جهانی سر نوشت ساز
‼️
💣
🚨
چند باشگاه مطرح لیگ برتری درحال بررسی شرایط برای جذب دنیس اکرت(درگاهی) هستند، البته پس از جام جهانی.
✔️
نکته مهم  این است که آنها صبر کرده‌اند و پس از جام جهانی و در صورت عملکرد قابل قبول برای جذب این بازیکن اقدام…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134270" target="_blank">📅 18:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
از آخرین بازی رسمی پرسپولیس ۱۲۷ روز می‌گذرد و پرسپولیسی‌ها فردا بعد از مدت‌ها به مصاف چادرملو می‌روند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/134269" target="_blank">📅 18:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
باشگاه تمایلی به حفظ اوسمار ندارد و در صورتی که با اسکوچیچ به توافق نرسد، گزینه های دیگری دارد.
🔴
به گزارش خبرنگار قرمزآنلاین، باشگاه پرسپولیس به غیر از دراگان اسکوچیچ گزینه های دیگری را هم برای نیمکت تیم در نظر دارد و هنوز با این مربی کروات به تپافق قطعی…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134268" target="_blank">📅 18:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
قدوسی ؛جدایی اوسمار قطعی شد و علاوه بر اسکوچیچ باشگاه یک گزینه دیگه هم داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134267" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
امیرحسین محمودی: اگر فوتبالیست نمی‌شدم احتمالاً کشتی‌گیر می‌شدم. اول کشتی را شروع کرده بودم و دو سال کشتی گرفتم. در کشتی هم خوب بودم و استعداد داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134266" target="_blank">📅 16:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❗️
ادعای قدوسی: پرسپولیس غیر از اسکوچیچ گزینه دیگری هم دارد!
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134265" target="_blank">📅 16:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔽
🔽
مدیران باشگاه سایپا خبر خرید امتیاز سایپا توسط پرسپولیس تکذیب کردند؛ بحث اصلی فقط سر فروش زمین تمرین سایپاست، نه خودِ تیم.
✍️
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134264" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
با اسکوچیچ هنوز چیزی روی کاغذ امضا نشده. ولی توافق درخصوص کلیات انجام شده.///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134263" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
درخواست ایران و مصر برای عدم برگزاری  مراسم ویژه همجنسگرایان توسط فیفا رد شد
🔴
فیفا: هواداران تو این بازی میتونن با پرچم‌های رنگین‌کمان وارد ورزشگاه بشن
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134262" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
پرسپولیس با وجود غایبان پرتعداد در بازی فردا، چاره‌ای جز پیروزی ندارد و باید با ترکیبی متفاوت، نخستین مانع مسیر آسیایی شدن را از پیش‌رو بردارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134261" target="_blank">📅 14:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
درخواست ایران و مصر برای عدم برگزاری  مراسم ویژه همجنسگرایان توسط فیفا رد شد
🔴
فیفا: هواداران تو این بازی میتونن با پرچم‌های رنگین‌کمان وارد ورزشگاه بشن
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134260" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134259" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
واکنش هواداران برزیل به ورود نیمار ؛ اینکه قدر ستاره شونو میدونن خیلی خوبه
🫡
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134258" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XssPkNki36LiuPUoxn33xqfolbfyOimZ-h0MXaVoQjEfg9ZS-nEMNOT6tHUW15jANQwP0bmpEc8QUNmfi6TUcBg2MO4Np_G8LU7yxn3mzaUdKqcfTTB7Ik4CHEB86s_NPPYsS21DKZ8g6d5uIdyHCeAu6ud2fv03IG0VNPO8ljYip9BNDU_cHh4WjK2YSpmgUhqgTsx5bj1SEtl5qX8xQBSmE_m4RT7P45yjjOlis_8VzRaYU17cbAmzbHhq-y3CVKYjnIzyLFvzZbrCV1q7twEy2-M5DkEgMIT_DH2H_ZSvtI_hu-imaWOdkdgqjGoiuVxFE1fvXEeLeLMt5fYeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول نهایی گروه c جام جهانی
👀
صعود قطعی برزیل و مراکش به دور بعدی رقابت ها ؛ اسکاتلندی ها باید فعلا منتظر بماند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134257" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCFvHXSX2PIIYkpmz6R3J0TXn-lHYkp4ivBBUm4rjB-Qv9CMzlGXZqzRLZb37QNM2JZrIcm-TF4DCrDW7Sw-9dRsKvW1BVvOfYCEjjInneKIZmxqcuKVxozhtLFzJwXh1s8stk3y5vr2pCpWosP4CbgDldXR_u379E5Lhnrk4PPLStz0X7VknBPff8-6YFswaEoz5EkNBoNWroWuaKrdeFoUgY_iIqjQkL-_6oKT8-GF5qwiC8OmpUEgDTQdCMdGYZplvyj3UKtKx6EsGlMEhZJN8ylXQJEQ-vTAOS8I3SbRKSJy6lYcfCSYHAp1g5KC7JgV_BEJA_4_XQ8EszWQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه  جام جهانی پس از پایان بازی های دورگروهی این گروه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134255" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ld_PfRYU8RkFTBsr-EZiW9nggDhrWcVDp0-45IY-pT8996Z-2lq1hGrXKY8lBWhoVq13zkEMXJkDQvqejCZ9D8LAe7ljD1n7Glzsmp1WBss3_6mh635NZdfeAFOH8lPhkrDTw10Gwf36j3_gnwN-Yl8OPIszh-aw6f9WV1hFRnWozqGoTxuJ-bOe77vI6Waz4pg3ZBRiP5coLZ4mn7auQzWoAUl2ocz1rKkAcwY9w6pqSA0vCmFkShPq6ByKryPmilEH7TFatfe2J0FjX5CnN1ubYz5gPqoWnAEu8wnRtuonypj-slYzl3tZ0PZRVYuo11rRpczg8nsh2djyxn88sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134254" target="_blank">📅 13:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
گرا اخرین بازی لیگ قبل تعطیلی رو محروم بوده و فردا تکلیفش برای بازی مقابل چادرملو مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134253" target="_blank">📅 12:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
خداداد نقش پررنگی در حضور اسکوچیچ در پرسپولیس داره/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134252" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
باشگاه فرهنگی ورزشی پرسپولیس با انتشار پیامی، صعود تیم نساجی مازندران به لیگ برتر فوتبال ایران را تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134251" target="_blank">📅 12:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyOo95rsXWc1UHywwohz6QBq7hTkEzsTtkIHRro6qYx9VPE9DyXVXr2oF81OujvhOHkl7y9EeFbZsbR8JKBk_EiXSJNWjyQNr3DzQr1HbDM6go2KsPJuFLlOubpqhlnPOti8FiLI0KguD3a7PCAx2bb-LqwdqD-wCvkjoYFdgy-YPgeJ1X-uHmRAJqSi5JSiMROhKgB_WkpgFdBwvzYWcDO220WOHeT3xtp0WxijInvJXW-SQQv5L8WoSGZNPy0WvItXWH3n3Rdtm0VHGjNIPAvnvEapTkBf_-atiJ8sPUDSmpLfwjNte3W806OQ6_Jih81-Ipjw7CLuxfJvX-1yiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اولین بازیکن آفریقایی تاریخ که در تمام بازی‌های مرحله گروهی جام جهانی گل زده
✅
اسماعیل سایباری قطعا یکی از پدیده‌های این جام تا این لحظه بوده:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134250" target="_blank">📅 11:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNnfbhO286gh8GaXShYoFPn2yhMY9HPVfNN6TyjTOLSmAhDZEQzHFegjGOVsf-XtN0YbjB557WE6AemVSeG1-uDJnQQ6-6UOtlkw--sIvsb2EwBlThuD1Y3QoVNIhAziFwkg78e5LoehYiSi7f_fM7fVyeOX7z6Aw8gs7rVtjAdlxoINYUNfiTr699A1NDUhet8_0ykUz6TuaktyDUXSYlaqU5rARPNOBdMnulNT9aA7_OodTI3nT02xBI4DdQ0rDafdGpooEvEpFlFPcCXNFFLqJadu3ZieEiYs-DWm5Q8M-ovfbEMLAJORmCdcPVOFTX0JHN07z3ShVTsxfwUAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اولین بازیکن آفریقایی تاریخ که در تمام بازی‌های مرحله گروهی جام جهانی گل زده
✅
اسماعیل سایباری قطعا یکی از پدیده‌های این جام تا این لحظه بوده:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134249" target="_blank">📅 11:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
منزل بیفوما و دنیل گرا پس گرفته شد  مذاکره برای فسخ دو خارجی پرسپولیس
🔴
فرهیختگان: باشگاه پرسپولیس به دو بازیکن خارجی تیمش اعلام کرده که اجازه ورود به آپارتمان خود را ندارند چرا که دوران حضورشان در این تیم به پایان رسیده است.
🔴
تیوی بیفوما و دنیل گرا هر…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134248" target="_blank">📅 11:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
فوتبال 360: مذاکرات پرسپولیس با هادی حبیبی نژاد مثبت بوده و این بازیکن در آستانه همکاری دوباره با اسکوچیچ قرار دارد. هادی در فولاد نیز شاگرد اسکوچیچ بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134247" target="_blank">📅 11:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📊
جدول گروه  جام جهانی پس از پایان بازی های دورگروهی این گروه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134246" target="_blank">📅 11:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWPoFg-a3tjBOQfNogQKROCrP9OZrL0tOsKi5FOdEoUTWpaGurBV38aqYPxRg-JMYtOTFq8ZyDHr1J7HUxipQ3VNPRs4u4Y2T-aL-fuuTefQwkTDI6U9mjyxHSLMxwf_zk4guTmE-HM3DoMDzI2nb3EDbzKSvMBa9C9fRwED7ggQxYod1OYIhQ5oNDAVMpNAyd0TkshNdjNFTT9YKsqmUsGqO-zhwJlHyWAVgDeVlsJU5U__Q93gse9t_AAMknoCLW79FRDXtCWheqTCrgDKx2bCzYaaG2etexFtbfhAsOzXoX3hblbgki7nw_KLbpFW3cKHbhCg-Is4FcId45EgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
📸
تصاویری از ورود کاروان تیم ملی ایران به سیاتل برای دیدار روز شنبه مقابل مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/134245" target="_blank">📅 11:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G83fvXDu8TmZWzRecK-3FhkrU0_fNIvz_5za88tzZvEmaZsUmAvPNxQOGz8C5IXH5l8j0__Yk645KhgAlZ-m7IkaxrvF3xcvJNvF5q9yjIwB5BNJ9AoixZKP-DV_OvORVgoIQ2WkPeKcL6mTuwVJ4-VI5E5vfhFCNM7bcsyqKcN384vcVfngJAc3-CCqnzSOM1U9efhxImzlMkwi5X7uuOiTGj3cREt7z4Q2t-a137GP795Zs8N_7YyEBZIoXAGxzq3f6_uEWwhciCGNOdp0mrBbmJK-iS8S8Oz6J427cduEAZsYQi9T8WxL2Ppc1hwARp8KCxxtQgTWRvS66qM3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس با وجود غایبان پرتعداد در بازی فردا، چاره‌ای جز پیروزی ندارد و باید با ترکیبی متفاوت، نخستین مانع مسیر آسیایی شدن را از پیش‌رو بردارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/134244" target="_blank">📅 10:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Naj3aubOBKKiBYCyinPG8AIp90aqE9U1-hf4FAaTKkPgFV3PXK_cYXbeRlpu_GAetepejbTtDv6dsS6gyJhZE1-JPNS3x8NCjJ8WBHyKpEeLNc8E3nDv4rk0XDs9vdav0Tmo-EZXp0SXnBOQwNcSg8j0xC-eXCiw4y-3wMxWuCYEYyJ5cxPFOP3tx2e4qj4EvaGk8rqgRMCNIz9vN-D1X-K5Pu5bIDxUD8Chra_B0jXKNnCnWmyOpCKnX4td1qB-fSD4HVCneZtnrCfOl3CW5RHNTrdEVzQlLo2FJBNpPrAgs5mtt8C0t-PTLEMWZcNJvh-Oo3RTGkGs-oWoKTjx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پنجره کیسه بسته است بابت بدهی خارجی .ولی اونوقت مجوز حرفه ای گرفتن.عجب داره واقعا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134243" target="_blank">📅 10:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
قرارداد عالیشاه برای فصل آینده معتبر است و این بازیکن فصل پیش‌رو نیز در جمع سرخپوشان حضور خواهد داشت. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134242" target="_blank">📅 10:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKIqkkg7Tk_3KFsYeDhKFAoLkvhbksdgnnYXMHeJmXVWryGvqFo91ggmn4rVnm1wfEfLqh_EepHG7flREwJQ52BoXg2Z_YuIvw6yz2DbhjbOrmttHDyquCfVrWiMDaJLdm_eCzF8y5DGcpxfG7DG6vkzEAN-g59uSIJtR4E9vfQae3SZSBysBZ42bxuBvYe8NlLy7UFukMatPLHcB0CXXnBpuFd4yoXODkNtrJugHajwUM4LHcfIFImdce1yZqD3Q4Iw7xrr_XLpWdAc2hSnILHNvjw3oYYh5TemFO6KPwfIxVGqLcLGKhwl5bueDP5SGYoKkDdjVt2oYQtMrlr20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه  جام جهانی پس از پایان بازی های دورگروهی این گروه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134241" target="_blank">📅 10:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
حمله تند سعید اخباری، سرمربی چادرملو به پرسپولیس: سهمیه آسیایی حق تیم ما بود، باید با تیمی بازی کنیم که از ما امتیاز کمتری داشت و سه هفته است در حال تمرین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134240" target="_blank">📅 10:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAJwY3zHVnnHTHOlvhmIngsxFCNzqooEvKDBUN9PUhGY2KkmS6BpvQV3P7BEiZmtgT59obxrmaG78JQoxvpYvb1ugTXitF6PjG9a8G7wyDy_ghTT0P7qlDxtAIih18MQu2EJjqJWjDuAuUhA1qNKV7HiD1q964jpWr-ossLW_QpeZYkh1bNHDDlY_dZqoyW3fHCzCbCplZzg9ms1sx41zlasqYO_U08wFN71vjxsl_L_0KNJaNhH9Puzmorqvs15aD3LMyUPCWeiGf2XAOm4gaUbJQDnwuBN7aYeSTCcoAsachqRq1t075OKLTt9Hpha111zmDKTeS-lL4qldDrd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون خوش ارتش سرخ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134239" target="_blank">📅 10:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtfOFcb9uJsDLUTaBzM7225-NZOcGHyww-Tt8yq3s4-2oMGIXomKutSsZUxiLh37bG6v21qBH-2dCPZdnFtYVXfqJ-_9eaiAAybSaNYDp0dcbP0KsSG3OQSKz2ZYHLvGLAe9K5OYjb9VOxuf09kDyaG58prRnUHJPrbbo1YOb8aRE0N7cUSae6oYlS_DY7tZwxcZgqCRAYRJFieaNJuKSq7-3a8_L-YmKJ_8tK7PzsVnmLsDBA9xRK_c4nBt9WAWmzYRk9MElvIp8KILPuPsVux64LBzu3t4hjNNxqcbJzkrWhkWEKfwtptZdMDcuGyZGK92dm4H2F_PyczD-qdMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه A جام‌جهانی ۲۰۲۶
[
جمهوری‌چک
🇨🇿
🆚
🇲🇽
مکزیک
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم
آزتکا مکزیکوسیتی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134238" target="_blank">📅 02:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNSYIxTVKy4-o8V8uoJemZMaJcb9CkzBUeQ575KxXFx79GTZH7ET5wV4zluUpKWu1EO_CXg6hednyAKG7m_GZN7q_BX1wI9bwXmZaYEBKgJIYVv1Ne1_zjuaxqZ3GCDAxm1Fx6IRWC-PJwXOuqAqWAtzu0zA0jKxuYigEPYuJuf6eSE2Qi4tiVgMiQ6FH59-r7bTZpmmKHru4RrHnEp89ekHUGYLRgMKxXbEnkHwY4QonPfrcQAfzNeYvCB8AC0c74NG2VuUKzilfoY0QF8UiX0mcncFr114Kob5pNFXlq2IVSEwX1TssxF0zFIskryvoG1JqW79iAmlWHPi2PLasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شباهت 100 از 100 بدون شک
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/134237" target="_blank">📅 01:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfdoMaHI875ESiEaFnIAHfhU1x6XEfVezDHIPlxEWvZgeBso4NQNBWyt7jRhzCcAFVEzMdcAsPGERtRcBJ5oSMWo8c8v6Zmyf1kEHP1tbDr9bxlP45-CZ6fJdnmPUZgXXKE7OocNSR3b11iRI6QQN4HDGXZWF5cVoSFTmDoZhzPU9xa18YI6sjGUzuwaA-I2jNUKij8gTB_rvJLPYOiX06B0z8M5A0Fpg-7gssmwuoQ6RgRENQ_y-rCrcA34NCFSbNPKRml8uRYoR3xbuCtXQB991U25mraim91OG4ME9kU9d6dY2YPLKy31pk8n4GCcokjDeoeolYEOJ_S660LvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه  جام جهانی پس از پایان بازی های دورگروهی این گروه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134236" target="_blank">📅 01:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
❗️
فارس : پیگیری ها از باشگاه پرسپولیس نشان میدهد  تاکنون قراردادی میان طرفین به امضا نرسیده و تنها توافقات اولیه و نهایی بر سر مسائل شخصی حاصل شده است.باتوجه‌به اینکه طاهری همچنان با باشگاه روبین کازان روسیه قرارداد دارد، پرسپولیس برای نهایی کردن این انتقال…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134235" target="_blank">📅 00:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
فوری از قرمز آنلاین: حضور اوسمار روی نیمکت تیم مقابل چادرملو قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134234" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
فوتبال جام جهانی و نشون ندادن به خاطر والیبال ..خود والیبال از ست دوم قطع شده و دیگه نتونستن از جایی دزدی کنن و پخش کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134233" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
والیبال فنا امشب لیگ ملتها هفته دوم شروع میشه و ایران ساعت ۱۰ مقابل فرانسه بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134232" target="_blank">📅 00:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/134231" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbN-wsFA7yoOHV202J6bEhwQ4nCnhhC7pdAqjVRBv2Lf71RK1uZbIn0br_8ZbbWI1WI0M0Mrr6lsc2xymJGJMvjQMAgfnEHp-xJdu_dHCoSxh9IIwmhsOLzHlqm5NeSRk7q4u1Ehpdfjnvh9WffErMsP7617GUDFdcpWgA4-2EmdlNJxKOR70TuArM0F7QNp4h479GBr_VDxBN8q6Vm_dA8KzT9snPufQIXgnbvBPAzn3Id4UAcRFzuu2XUQ7M9Av-3fbXZ-H8NPEVEuL6JLObj85fbMq9AWbeFgg-lLohrpKPKG5seCTW2IoJ1a85UUW0S60Ho-Tt14U4sodH5HZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
صفحه رسمی باشگاه دهوک عراق عکس ها و ویدیویی هایی از معارفه یحیی گل محمدی و دستیارش محمد عسگری را در پست و استوری به اشتراک گذاشته که نشان می دهد مراسم معارفه ویژه ای جذب پرافتخارترین مربی ایران در جام های سراسری برگزار شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134230" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
#فوووووووووووووری
🔴
با اعلام رسمی پایان فصل؛ قرارداد امید عالیشاه با پرسپولیس یک فصل دیگر به طور خودکار تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134229" target="_blank">📅 22:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
بازی سه جانبه
🔴
مسابقه پلی‌آف
📆
جمعه 5 تیر
🖥
چادرملو - پرسپولیس
⏰
ساعت 18:45
🏟
ورزشگاه پاس(تهران)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134228" target="_blank">📅 22:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134227" target="_blank">📅 21:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
❗️
البته ی بازی گروه b امشب پخش نمیشه چون ساعت 22 بازی والیبال فرانسه و ایران برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134226" target="_blank">📅 21:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: با ایران داداشی شدیم و به توافق «صلح‌ تاریخی» رسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134225" target="_blank">📅 21:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKvzeRNxManK7BceHlJ8-wR0GYsmHDPNvIlR7lYpyFcF1F08ixjkTDiCUC1fvh8d1Yywn2qb9YB5ynJ5pN7YGaLw9xtyhxnbXVvgUhm4bHb7K8eDFo0_R8f5x5ZMyJscqUxaVQJRfeb1ElQFjXlcO0o319kLYt8UvAWiCWcWckZahHalqOL_XZ3czCrXYkIC0F6Ym4d5-ybZ4WHC9C8N2ZN7t_SrIk6tqmIepVsb5M-G48HUXj7KJSSPPanfDsX-vrRJKg02eyiOkkd8iIavfXSwtRdmr42jnFlriUE6kErY0E8aXPgk7kkq4vfQUJYuQuHllXiVwfpnKYSnJctVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خطاب به هواداران کریستیانو رونالدو و لیونل مسی؛ به‌جای درگیر شدن در بحث‌های بی‌پایان و مقایسه، بیایید از تماشای این شکوه لذت ببریم
.
🔴
ما در دوران معجزه‌ای هستیم که هرگز تکرار نخواهد شد. این آخرین فصل‌های نمایش دو اسطوره است؛ قدردان این لحظات باشید، چون تاریخ فوتبال، پس از آن‌ها، دیگر هرگز بازگشتِ چنین عظمت‌هایی را نخواهد دید
😭
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134224" target="_blank">📅 21:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Majnoon Ye Rooz</div>
  <div class="tg-doc-extra">Hossein Sotoode @cafe_tarfannd</div>
</div>
<a href="https://t.me/SorkhTimes/134223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎤
حسین ستوده
نوحه محرمی
🏴
»ری اکشن فراموش
نشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134223" target="_blank">📅 21:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
عاشورا حسینی بر عموم شیعیان حضرت تسلیت باد
🖤
التماس دعا
🤲
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134222" target="_blank">📅 21:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134221" target="_blank">📅 20:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDXhOfQL_oDcd4nXxbGiqaVWybAi3rdeGx2TTzGLaG1Uwfj4_gw2O03RWm14PGe1Jilrg_XKcJs7NVIbDiaK7QvjaZXGrvD7-GFoVNIs2B3hCNnuFK4bFNPF7UomhCoQ4X6Zu-Bi8A_oXn3XV9DixdCTE0tivHm2-G_BvWqsguu_jFaAfkHqwJ9-S-5xIoDs3QtBKFpKn3_xvCqHfrj-cWOhsRHDgucqBoiVg9vKTzs0wgGMc3hIb-aYGQmKn2voECzkrwHrZNJ9hkJEVy0t0S-xEPbJ5IoG_73kPiDPlUjx2-j1XnwIbCCsxy-Cqr7UifimpU_2VYU6LnD7g4oNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه C جام‌جهانی ۲۰۲۶
[
برزیل
🇧🇷
🆚
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
]
⏰
بامداد چهارشنبه ساعت ۰۱:۳۰
🏟
استادیوم
هارد راک میامی
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134220" target="_blank">📅 20:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOf5IqiCrInDX96tj6ZSk79D0Mo9nDnVVXLC0unalybKNT8CTmJ4lhDYkGSoIggqUIV9UH_TU_o8BvaH6l_WKXj7WNke38GfBZ8Fs0pl3fMHmPnF8yzInayabVr0VbCnS1EPcUNgXbaNKotF-lXlAHQrWTRmrJ3tjx6t-XRASYAIi5oOQiY-j2lzkV7DxGA8rVP5I6qyXqkzCO8rchDJEOcA3PJ0UXojUklDay25llTNFxpIC6enr-snKb64KMFxAa-MCfYGPJ3-LGJcsfPPaswWMlCyTI32mn_ikrdPqhkFFt6Q0r2u3cBMWpUh-1Vh-Z0uxb8pLIQg54v5Yx-vKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134219" target="_blank">📅 20:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
اوسمار خودش اعلام کرده قرارداد نداره به شایعات توجهی نکنید دلال های ولدز…میخان باشگاه رو سرکیسه کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134218" target="_blank">📅 18:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
❗️
مارکو باکیچ: آماده بازی برای پرسپولیس هستم. دوست داشتم در جام جهانی برای تیم ملی ایران بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134217" target="_blank">📅 18:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAzvd7tG6a4ffSNnJUWa2A4oTO2gFJHDMdyzmXpa4DBJDJBjJ6OpTDT43k05wJmdDCtkUcCj94jaSv_niBefiOqkLt3Wk8e9DklmlUYz6y1iIksdJQVap3S8TEUc_-_0UhBaWatvZ1ti7AyNFkY1RIRO5y1MiarsXMUOut_F-THbWhuGaubQgEeed3bVmAE4CrNsCQrhnRoynzvyFpWjlBCevri85ALBhdBt4EFbWhAjtCjuqSQTYP09vE2Ve49giHqQLg-FE-bPsFolht2fSpcNMnS_bZzeu_F7Dq7KA18P14WPgtpPj2AiEWqN7Y-JDGWjS_037MSGWkxqQE5c_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽
رئیس فیفا اعلام کرد که در پایان رقابت‌های جام جهانی ۲۰۲۶، جام قهرمانی توسط رئیس‌جمهور آمریکا، دونالد ترامپ، به تیم قهرمان اهدا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134216" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
یاسین سلمانی در پرسپولیس میماند؟ آخرین گمانه‌زنی ها از ماندن ستاره خاموش پرسپولیس
◽️
یاسین سلمانی که پس‌از پارگی رباط صلیبی خود بازگشت موفقی در دو فصل اخیر سرخپوشان نداشت، بنظر میرسد یکبار دیگر شانس به او روی کرده و اوسمار ویرا قصد دارد این بازیکن را به…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134215" target="_blank">📅 18:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">◀️
از امشب بازیهای هر گروه به طور همزمان شروع میشه ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134214" target="_blank">📅 18:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
1. روز اول، بازی‌های چهارشنبه، ۳ تیر:
🔴
گروه B:  سوئیس
🇨🇭
×
🇨🇦
کادانا؛ ساعت ۲۲:۳۰ بوسنی
🇧🇦
×
🇶🇦
قطر؛ ساعت ۲۲:۳۰  2. روز دوم، بازی‌های پنجشنبه، ۴ تیر:  گروه C:  اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
×
🇧🇷
برزیل؛ ساعت ۱:۳۰ مراکش
😀
×
😀
هائیتی؛ ساعت ۱:۳۰  گروه A:  چک
🇨🇿
×
🇲🇽
مکزیک؛…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134213" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚫️
دور سوم مرحله گروهی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت، بازی‌‌های امشب و بامداد فردا رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
چرخش…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134212" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
خبرگزاری فارس: نقل و انتقالات پرسپولیس  تا زمان انتخاب سرمربی جدید متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134211" target="_blank">📅 16:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
فارس: بین پرسپولیس و اسکوچیچ در اغلب موارد به توافق رسیده‌اند و تنها اختلاف بر سر مدت زمان قرارداد باقی مانده است.
🔴
مهم‌ترین مانع موجود، مدت زمان قرارداد است. دراگان اسکوچیچ خواهان عقد قراردادی ۲ ساله با باشگاه پرسپولیس است اما مدیران این باشگاه خواهان قرار…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134210" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه کنیم.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134209" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💢
اوسمار خودش اعلام کرده قرارداد نداره به شایعات توجهی نکنید دلال های ولدز…میخان باشگاه رو سرکیسه کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134208" target="_blank">📅 16:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMpxwi4pHPI_bGU9YnPrkGBzJZcXNmEH_odPC1_iUaamWknPDC_73VabJZVmPbYxvfc_FY7UAiOIjuOrgLPF9dIWFgWsqpHI-a_OrTQz947WPXg0Anv_QVAG3xuv8VrI7GbgOIvSN_UNEKLOFWg5YoZStUGQzzXfCZYzFkrCzOFVqHm3WIuScSYFalD962QIowUw5eQ0R9r83_GkZOPNReYOGgt2TptX51yo8y7L5-S8SNH-bJXzFDGFWM9-Sqlvr-XQehS4AwIEpmrwaHVtKTk9an9Gxn402TOJAK37_Hl0llQupJKAtMtLGek1Y8DVq4gH6jwQPp2akyZTLAyttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دور سوم مرحله گروهی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت،
بازی‌‌های امشب و بامداد فردا رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134207" target="_blank">📅 16:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
طی ۲۴ ساعت آینده جدایی اوسمار ویرا از پرسپولیس به صورت رسمی اعلام خواهد شد.
🔴
بدین ترتیب و در صورت برگزاری مسابقات پلی‌آف احتمالا کریم باقری به صورت موقت هدایت پرسپولیس را بر عهده خواهد داشت. البته هنوز احتمال حضور اوسمار در پرسپولیس در این تورنمنت وجود…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134206" target="_blank">📅 15:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134205" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
اسماعیلی‌فر، ترابی و هاشم‌نژاد با تراکتور قرارداد دارن و تراکتور هم قصد فروششون رو نداره///آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134204" target="_blank">📅 14:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤩
تتوهای خانوادگی مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134203" target="_blank">📅 14:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134202" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134201" target="_blank">📅 13:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
اختلال در خدمات کارت محور بانک‌ها رفع شد و خدمات کارت‌ محور هم‌اکنون در دسترس مشتریان است و روند ارائه خدمات به روال عادی بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134200" target="_blank">📅 13:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134199" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
فرهیختگان : اوسمار تمایلی برای ادامه کار با میلاد محمدی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134198" target="_blank">📅 11:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ: ایران اگه توافق نکنه ظرف یک هفته تمام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134197" target="_blank">📅 11:46 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
