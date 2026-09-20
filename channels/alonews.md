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
<img src="https://cdn4.telesco.pe/file/ZPSi90vRTDu91IdczzyjE9fw1FWiyCs2jDhaycyQK1U3sOidwlYF83dvDkwBfMmKM_SR7h-ydBliikj3CZvytwqdnHuT6u91Ogrlvt108zv0-jMkpPA6jyK-sNdHQ7LX7xroOg7r5dL7URCrmVKcvpSJzpa5jzzxYhmJidIqIVTRfe0huENWHehycAXVtemd9-G8RQHl4ff2C_uBEIjvqCqom8EJfMpuQ0MToUeyK1qQ2EW_H2KhGjkLAk_teovl5acPVX0d3nHEcRuNNbsG5CMunicQ1RkIWqQwCOlUxBRD7qYhJCOmAM79aiwTf7pUB7JMwcclVxps4Ht8wzEQrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-148430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یمن: نیروهای سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/alonews/148430" target="_blank">📅 21:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148429">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUtU04Bla49D948zkOtd_rsQROgGOW3ryl4a5wPv0FcSWkWeOqn7SKbmEQdPOhpysunQ6ByI52Cn94Nu3mgQMXmqyNmTdYwsOJ8VhMPGwdEdE5xGAUCSvmBtGxgfEqwBSUC7-A0i0SCd7Z8gki2QiGCTmeuWcGmshymRbq2GY27MDGjTlvY_6E3QMWkdGd27Pk-G4pjx4bNwh_DdIpXHMcelo82z9zIeBw0GZZ5jVvmUU7bB_Am2aGfjcDz0pWXWHWnk_3sjXM7ekZorUMD00Zb0H1R20MzuVR3eIJ69KIQTaYAZcQivTtlR2Z2BbY35RxurGQpsX0xbQ24EIDkR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمرین چین برای حمله به جت‌ها و سامانه‌های پدافندی آمریکا و ژاپن
‏
🔴
وبگاه بردی افریک: چین نمونه‌های هدف گیری جنگنده‌های F-35 و F-16 آمریکا، سامانه‌های پدافند هوایی پاتریوت و هواپیمای هشدار و کنترل هوابرد E-767  ژاپن را در یک میدان تیر ساخته است.
‏
🔴
چین از سال ۲۰۲۱ تاکنون، نمونه‌های تمرینی تجهیزات نظامی آمریکا  و ژاپن را در بیابان‌های سین‌کیانگ برای تمرین تیراندازی واقعی و کالیبراسیون موشک‌ها می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/148429" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148428">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ فردا در جریان بازدید خود از سازمان ملل، با ممدانی شهردار نیویورک ملاقات خواهد کرد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148428" target="_blank">📅 20:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148427">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: روزی که تفاهم‌نامه را دیدم گفتم چرا ترامپ باید چنین امتیازاتی را به ما بدهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148427" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148426">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: شکی در اصل مذاکره وجود ندارد اما به هیچ وجه نباید از مواضع‌مان کوتاه بیاییم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148426" target="_blank">📅 20:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148425" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-2z2lfiIAZ248xmTvT0kX9NvBOeR3b53CHtpFNEUApVkB-UADc66afi2RTSwOYIyb6vA0IBN6f8UbrypvjtrQpaFB-yRU79oAScW-hTYAy5KrxoFE6EjRaY03fvMjUikCx8RZvxZM0G8ATPN5pdDD8kRos1xkGJU1wML9EWL5ymCfYAtwfEsxuYKbAJ9YE4TgAD6lDT4nKJ5SF8mYiHZGKKHLH3XpsYnokTh9YMqgAzgG6Aj5LlDy__7ij1ws8cwXIO78H3L_GURUibqj9srkc2iLve2Tc0pjK4YvT6P4tKo8MVUTnBXxPa5OZg2dGbGOhILHvmOkXVligEVAxNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به وایت هَوُس رو نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/148424" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ارتش : انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148423" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آمریکا به‌دلیل شرایط امنیتی، تردد کارکنانش در عربستان را محدود کرد، سفر به «طائف» و «ینبع» نیازمند مجوز ویژه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/148422" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNiu7rLeW8GdJzLv8xUoAy8tOACViNkJ28TrxvLtEnJXGYOXr7q5lw7GbREsEw45m_IM1T8jQYz5rTYf730XRTMGQlLFXLIMZTim0UMhmEAUm3GISpw85AEgPOG1Pcy5CtRzDsjE9_HffTD6OhrG27En5i4Hk-KjrGsrsSMBRsJg2dtCMh9D-5bLYttL_YYZktgmkOY94WNzFMsUxoP6vq3A1OK6I3LH0TeJlKsxuYAeR996EY99YvECafU_WrSxb2KESvtX35SCQGICCcoYjQQ7y9tzRzDh1xiHXGZqqZFpadAr7mop5WnQ6bb1vNAIo88uzFhUFqjw-LMp2n8lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی نیروی هوایی اسرائیل، مناطق مرتفع علی الطاهر در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/148420" target="_blank">📅 20:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / راشا تودی: عباس عراقچی، وزیر امور خارجه ایران، وارد دوحه، پایتخت قطر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148418" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148417">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⛔️
بیایید ببینید هوش مصنوعیه یا نه
😂
⚠️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148417" target="_blank">📅 20:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148416" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHpeV6vnoo_8kP7_tnZuRRLP6L7jx5pL4U07axR1XlwlcPJBI12qfD7dlImrHIMtrV0yfoG8X11PT8Xr7a10AAqmb2LO8KCRMT58R2FZHuK9sVath7_Bsu9p5xeHV8zmleZCRvBYZnpQHxvybZc1gASbYLZWtpXaO6iQCoXxN-FPa2cOe81UAXMmPKEX_QjnV73xjBvPOigPFxwD1R63Gu5HHFX2oemKocE2W6BsJQpgNzjsz_HnfllNCsqz6bTSjFK7jiGS6riECwmReB8GCcgqVunlhTCFEzkchA2ml8NNiy5Xvdcc6cL-wPJiYRlfvYze2E6YYgvtPuy14XMWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/148415" target="_blank">📅 20:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: مایلم با پزشکیان در حاشیه اجلاس سازمان ملل دیدار کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148414" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود قدیریان بعد از قهرمانی در مسابقات جهانی بدنسازی گفت که مدال طلای خودم رو به رشت میبرم تا تقدیم مادر جاویدنام مسعود ذات پرور کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148413" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فرود اضطراری ایرباس در مسیر استانبول-تهران در تبریز
🔴
مدیر روابط عمومی فرودگاه بین‌المللی تبریز:   یک فروند ایرباس A330 «هما» که از استانبول عازم فرودگاه امام  بود، به‌دلیل نقص فنی اعلام وضعیت اضطراری کرد و در فرودگاه تبریز به‌سلامت فرود آمد.
🔴
تمامی مسافران در سلامت کامل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148412" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
اولین ربات تحلیل اقتصادی رایگان
‼️
🔴
اگه نمیدونی کجا سرمایه‌ گذاری کنی یه سر به اینجا بزن
👇
@Sygnl_bot
@Sygnl_bot</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148411" target="_blank">📅 19:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
محسن رضایی: برای یک جنگ سرنوشت‌ساز کاملا آماده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/148410" target="_blank">📅 19:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رسانه قطری : به نظر می‌رسد وزیر امور خارجه ایران عراقچی در حال سفری فوری به قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/148409" target="_blank">📅 19:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار سی‌ان‌ان‌: جلسه ترامپ در کمپ‌ دیوید، جهت بررسی و رایزنی درباره گزینه‌های حمله به یمن بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148408" target="_blank">📅 19:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY9jbgftV7dNzvQ2xTWnYKOE41-uDdiVKIBGTt9fthONg1HKWrSUs65KekAvWDCtPRwySuKbKHQah_HTzS1kMy_Zf3NwNShCoq0RLBQYLghPxUOWZncqDBupxqQ7oofme9RUV7R8qCubtFRjhpiO9KVIRWeJsLHJj-4IIpFTitItUcDSmX6bu2Q8_oY113uOLFltStvXmMKlkOCQoclFeDZb11OUxGCM3IusrrfvHoCS_ghMJS-J7viP2-TAL94CcHXAStNUgnR0B32CELmxrwsuJyD4sbrFlGkZ3KRNy1NlwRByBw70iqP8YtCbFYC-KjoSA-bvMHel-y3Rf0ICvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار معاون نخست‌وزیر چین و وزیر خزانه‌داری آمریکا
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، با «هه لی‌فنگ»، معاون نخست‌وزیر چین، در نیویورک دیدار کرد
🔴
این نشست در آستانه دیدار دونالد ترامپ و شی‌جین‌پینگ انجام شده است
🔴
بسنت، وزیر خزانه‌داری آمریکا در تشریح این نشست مدعی شده این مذاکرات به زمینه‌سازی برای پیشبرد منافع اقتصادی آمریکا و کسب نتایج ملموس برای مردم این کشور کمک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148407" target="_blank">📅 19:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه حمله به پالایشگاه مسکو که یک شهروند ایرانی آن را ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148406" target="_blank">📅 19:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srHNP_U6Ayg-15IodhyhiWZPv29J72XBOGZ8ux798btyguoOTqwtzcseLov9obYD4WhBhjW7NIUQdfJAArraTkB8a0pVUBOrorMqd0wvV1i-PRsgyNd7chTbiU9qCpduW2w-VzUabbXj3FOVy9paJoTDhG7Kc0LUero7jFYzan_3WwMqLbmUUmJpghJ3O1izipTBubJZNSJWeYUfMlY9HiEEKBPzrMqLRccyb3NLqBeqk3Ua7obtFQGLchhbEsZK6kiPWCzzP-WQCjxiXwFiCd2uyvzkwBrOBZR-2n1jiIa6r-lcWhJRX9QYIJJPDffkpCqGXbhiChRVCGJUgMAZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/آسمان اسرائیل کلیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/148404" target="_blank">📅 19:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148403" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر:
ما از مقامات دولت آمریکا تضمین‌هایی شنیده‌ایم که آمریکا می‌خواهد به توافق برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148402" target="_blank">📅 18:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR36Rx3T-ccYSZZfql-ECedcJrcWVZhRRRWdflOGsSmwFrAZVYL5EMZWN1ks3JO5x986aPMQ5Jt7R8PEfEdnG7gkOiJTilxaN9CCrAOMrhKTWatPUMV_VBmSdg1vzyLX7RZjdWd9FN75uAt6HJPLcNcCUf64rHxC9lbJJBWKFtjGLhEjw3G7ArnzUBb7E8llTu4RLbOtyRAZzUpdUfusXNoKjUzyJkkrVVfMMmolrcH2M7EfNY-C8ua1TdI-nNICh_57wLlInwZS10P5qYzJOdiGfYRHGulL8vT5vZtZs_-aXsQoX5sGoCesqDqkhO3JKRshZVaAaAgtF-yRQgPWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره اعمال شده بر بنادر ایران، مسیر حرکت 109 کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد شامل 4 کشتی بیشتر است که از آخرین به‌روزرسانی که روز جمعه منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/148401" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ارتش اسرائیل:
نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148400" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148399" target="_blank">📅 18:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وای‌نت: بیمارستان‌های سراسر اسرائیل به حالت اضطراری تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148398" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kciZ2hs6bsoVuQNFdoR_y633RHpPFHDkxW6-jxmcg6h-XehuGtIZNEaLzSsnPeFew3TwfNZWPKizDXfcHaMnobJwWmyWRt1dcOVARBMzfUpV01NiTKSYH5zDkMykPtBNMaruz2KycbF2vQGCQH0CqJBVhaxQCPwSLuwfOoWQRe1mMJBntESfQsShZhxdW9PqXFAVNvjC9Anj82bdReZL7syFJ5iCxNM8G4sPegICzF-3IO4ilQAdrXkW-egBH_QfDFc1VRX3CUw8hV_WLv9Vq2YpeOAH8NET3FwlOXhzWBuAOGUzaQQB-EwZRL9-YxoIvU0WNBPJrPW0Q7NyzaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت صندوقهای طلا پس سخنان ترامپ مبنی بر دیدار با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148397" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148396" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148395">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ها پنهان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148395" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148394">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:آمریکا در ارتباط دائمی با حوثی‌هاست، و آن‌ها توافق کرده‌اند که با آمریکا نجنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148394" target="_blank">📅 17:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148393">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: برخی از مقامات ایرانی پنهان شده‌اند و یافتن افرادی که قادر به انجام معامله باشند غیرممکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148393" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
🔴
سوال من این است که کی و آیا قرار است تمام ایران را منفجر کنم و آنها بهتر رفتار کنند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148392" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148391">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:  ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148391" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148390">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148390" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148389">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تداوم حملات عربستان به استان‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148389" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148388">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پزشکیان: صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد
🔴
نمی‌توانیم قانونی بنویسیم که ضمانت اجرایی ندارد؛ گاهی به نام دین بر روی مسائلی متمرکز می‌شویم که اصل نیستند
🔴
ایجاد توقع در بین جامعه بدون در نظر گرفتن ردیف بودجه معین و پشتوانه مالی، نادرست است
🔴
از بیان حرف‌هایی که حتی فرع هم نیستند، دور شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148388" target="_blank">📅 16:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148387">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خدمت اجباری سربازی در آلمان مجددا از سر گرفته می‌شود
🔴
وزارت دفاع فدرال آلمان در برلین: نیروهای مسلح فراخواندن مردان ۱۸ ساله برای خدمت سربازی را که علاقه خود به خدمت را ابراز نکرده‌اند، آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148387" target="_blank">📅 16:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148386">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t51QJlrCKsXNmUXnG2uW6jMTrPbHEFqhmWfZjVAAqcjfuHCCZ5vcdy4FyVrefVtCl4Zztz6QZWsnzkG6g6HcsTJg-A-L7f-6e1zN-oLdUQVn0aPYceMRMQMAj4FvQb6Ylb0UencDz6P0Kv5nm069Vs6Wb00S56dyQ7w4pktermER0_JAAUbTJokNJ6cBtYslXWb_IXSXVkmjJasgW24p7rNGsf5-feiQyi5pW7yCyNafEc6F8QuuofoXHf5G8RiBmUz3A30bW4Pg3gOwdap7RDmv9y4rHiHHZdhn0E9Svss2ReiXp7ZLgDIFZ94dzSGGx_Pg1VIhNb68zzl4egt7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاکنون، بیشتر هواپیماهای تانکر سوخت از قطر تخلیه نشده‌اند و بعید است که ایالات متحده قبل از تخلیه این پایگاه، حمله‌ای را آغاز کند، زیرا تقریباً 20 درصد از هواپیماهای تانکر سوخت ایالات متحده در این پایگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148386" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148385">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان به فالوور گفت تعقیب کننده
🔴
پزشکیان: حالا فالوور نگیم صداوسیما گیر نده بهمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148385" target="_blank">📅 16:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148384">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فارس: یگان‌های واکنش سریع ارتش در مرزها مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/148384" target="_blank">📅 16:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد که بر اساس اطلاعات دریافتی، ایالات متحده تصمیم گرفته است اقدامات خود علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148383" target="_blank">📅 16:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148382">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148382" target="_blank">📅 16:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر حملات توپخانه‌ای اسرائیل به مناطق یوهور الشقیف و خیام در جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/148381" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
تا دو انتخابات تعیین کننده و مهم در آمریکا و اسرائیل به ترتیب ۴۴ و ۳۷ روز باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148380" target="_blank">📅 16:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzxfyISyh5TI4kFzicyUftTmtLSXWGA6coW7v4EnL-l1y4LXkQkAonu5TD6V5hfeBbeyykL8uuSRsU5miTUNvQDCX6GBng8HiEMsVhFmdi6pB41Hru08rohyiprB4nxzW0nJzKZOmDmWS45tTrk5glQRlCFtG-sf6GEWAPfC_Qz76n98rJe1jQp2Btwzh4JZtbNMwPBK4Y8DP4GqX45q9aG2BsDKU0ALYcEsA4zOeA9emeoUvgpmQnLla16pYAkmDHE6EQ6_0PwYcQ6NPJW20NKIK3EtGl_L0ovXMckiODCiB8vUt59PYB4r1QWRg4HUatzW74yGIveSCD4fMbuh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💱
بات سیگنال و تحلیل خودکار
💱
اگه دنبال تحلیل و سینگال دقیق هستید حتما عضو ربات بشید
🆓
آیدی ربات:
@Sygnl_bot</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148379" target="_blank">📅 16:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148378">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اوکراین خطاب به پوتین: از پنجره کرملین سوختن مسکو را ببین
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148378" target="_blank">📅 16:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ژاپن: کره شمالی دومین موشک خود را شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148377" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فارین پالیسی: ترامپ و پوتین در جنگ، شباهت‌های زیادی به یکدیگر دارند
🔴
در تحلیلی در فارین پالیسی آمده است که هم دونالد ترامپ و هم ولادیمیر پوتین تصور می‌کردند جنگ‌هایشان با مقاومت جدی روبه‌رو نخواهد شد و در مدت کوتاهی به پایان می‌رسد.
🔴
نویسنده این مطلب معتقد است هر دو رهبر تا حدی تحت تأثیر روایت‌ها و تبلیغات خود قرار گرفتند و برای یک درگیری طولانی‌مدت آمادگی کافی نداشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/148376" target="_blank">📅 16:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
محسن رضایی:  اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند، چرا نمی‌آیند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/148375" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مرکز زبان وابسته به سفارت فرانسه در تهران با دستور قضایی پلمب شد.
🔴
قوه قضاییه اعلام کرد این مرکز بدون مجوزهای لازم فعالیت می‌کرد و پیش‌تر چند بار درباره ضرورت دریافت مجوز به مسئولان آن اخطار داده شده بود.
🔴
در گزارش قوه قضاییه، اتهاماتی مانند استفاده از آموزش زبان برای پروژه‌های علیه امنیت ملی و تسهیل خروج نخبگان از کشور نیز مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148374" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان: باید راهی پیدا کنیم که مردم ما به عزت و سربلندی و قدرت برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148373" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو برنامه سفر خود به آمریکا در روز های آینده را تغییر داده و بلافاصله پس از سخنرانی در مجمع عمومی سازمان ملل بدون دیدار با ترامپ به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148372" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra-M0eoynHmxgSCqVAfR3ZDtvK73FWawA3z0mSgs2W_vXGuhoZG8gjCqFcfBpiwrCW9DRft5Ihc9CzoQhFq1MeJfJIe83MF6US8ywaEpUe7KqqxfpSj5J0XiVvm0vmVuY-6jueOF_gb8kQJxQLi-7fSL92KGU59iCldcHFzsA6sGahnEpEPZuUctJumyBaAHCURcjF3F9t_cE7rKe0HPUYxT8cNJid3AmBzbynXOX1YKY7-4CC_TqczhoJOeyJn12kg23TbnOOLEVidl1WTL5wwWo4mFEqtoBozmQxPc1uR2YXrCT1aEaIxPlUDinKlJdUvegdRz4a86VavHdr2vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : به درخواست قوی ارتش ایالات متحده و به منظور حفظ امنیت ملی، من موافقت کرده‌ام که بنای باشکوه "طاق پیروزی" را که از دوران جنگ داخلی، یعنی سال‌ها پیش، برنامه‌ریزی شده بود و در محوطه "دایره پذیرایی" مجاور پل یادبود آرلینگتون قرار دارد، به یک مجموعه نظامی/طاق پیروزی درجه یک تبدیل کنم. این مجموعه برای نگهداری، ذخیره‌سازی و استفاده سریع از تعداد زیادی پهپاد، به همراه تک‌تیراندازها، در مناطق سقف و محوطه، و همچنین ذخیره‌سازی مقادیر زیادی مهمات تک‌تیراندازی، طراحی خواهد شد.
🔴
هیچ سازمانی مانند این در هیچ جای دنیا وجود نخواهد داشت. از بین 59 شهر و پایتخت برتر جهان، واشنگتن دی‌سی، تنها شهری است که طاق پیروزی ندارد، اما اکنون این مشکل برطرف خواهد شد و این طاق، بزرگترین طاق پیروزی در جهان خواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/148371" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148370" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148369">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقع در مسیر فروپاشی قرار دارد. در طول 10 سال آینده، آمریکا آن‌طور که امروز است، نخواهد بود.
🔴
اما ما و کشورهای عربی باقی خواهیم ماند. ما هستیم که باید این منطقه را سامان دهیم. ما باید امنیت را در خلیج فارس برقرار کنیم. ما باید یک پیمان برای همکاری اقتصادی ایجاد کنیم و در این منطقه با یکدیگر دوست باشیم.
🔴
ما یک خانواده هستیم – خانواده خلیج فارس. ما هشت کشور هستیم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری کنیم، در سرمایه‌گذاری‌های یکدیگر مشارکت کنیم و حتی یک ارز واحد و یک بازار مشترک داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/148369" target="_blank">📅 15:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148368">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی : اکنون به تمام کشورهای عربی و تمام کشورهای همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد.
🔴
اول اینکه، حتماً به شرکت‌های آمریکایی حمله خواهیم کرد – مانند شرکت‌های حفاری آمریکایی که به طور گسترده در اطراف ما فعالیت می‌کنند، شرکت‌های تجاری آمریکایی و کسب‌وکارهای آمریکایی.
🔴
ما آن‌ها را هدف قرار خواهیم داد و خواهیم گفت: حمله به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران – حمله به ازای حمله.
🔴
از طرف دیگر، ما همچنین به کشورهای همسایه هشدار می‌دهیم: با آمریکا همکاری نکنید، زیرا ما به طور متقابل پاسخ خواهیم داد. اگر یک کشور همسایه با آمریکایی‌ها در تحمیل یک محاصره اقتصادی به ایران همکاری کند – به عنوان مثال، در مسائل مالی و فعالیت‌های مرتبط با ما – ما به کشتی‌های آن کشور در تنگه هرمز تذکر خواهیم داد.
🔴
ما محدودیت‌هایی را بر تردد و عبور آن‌ها و همچنین برخی از فعالیت‌هایشان اعمال خواهیم کرد، یا ما به طور متقابل در مورد همکاری‌های اقتصادی پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/148368" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148367">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: ما باید طوری کار کنیم که چرخ تولید بچرخد و از کار نیفتد
🔴
هر جایی را که می توانیم قطع کنیم ولی نگذاریم چرخ تولید قطع شود
🔴
دشمن به دنبال این است که تولید ما از کار بیفتد؛ نبود تولید یعنی بیکاری و تورم و کمبود و گرفتاری
🔴
همه کمک کنند که تولید کنیم. باید این فرهنگ در جامعه جا بیفتد که ما خودمان در سرما بمانیم ولی چرخ تولید متوقف نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/148367" target="_blank">📅 15:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148366">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148366" target="_blank">📅 15:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148365">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پیشنهاد ایران به آمریکا به نقل از ارم‌نیوز امارات:
🔴
توقف غنی‌سازی بالای ۵ درصد
🔴
آزادسازی بخشی از دارایی‌های بلوکه‌شده
🔴
بازگشایی کامل تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148365" target="_blank">📅 15:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148364">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5da053393a.mp4?token=GYycMQryVydDrhYZw7vsbPjKVcO4i2_-wfamoFH3L4J72Bk8dqbP22FrOOzlUbgFy3npZAoJZw4gG2vWE2BOUf9xxj5XV9kzZtBPKTLOx1ju-IF_fqvJ0j7YiUtq-jVZMOkru7eeCtEsQphsPphxPDfScfhcVmVSEdEOmx01YfYT9QX-m-ZF7W0pL0QP0QJGmz5KvItGU1jw83DyMk1wuZxoANkghuvtyi_PHBXyKyFhapoYY6dcgUIw8tWuvf6UG_ejWOS-nEW7YpGWO8JqnRnDLYvRitPer78RFE4Qt_MNJlLiHHNLDtO-wnD3oFjnZpDsFnU5y4E0mdEUWmVGRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5da053393a.mp4?token=GYycMQryVydDrhYZw7vsbPjKVcO4i2_-wfamoFH3L4J72Bk8dqbP22FrOOzlUbgFy3npZAoJZw4gG2vWE2BOUf9xxj5XV9kzZtBPKTLOx1ju-IF_fqvJ0j7YiUtq-jVZMOkru7eeCtEsQphsPphxPDfScfhcVmVSEdEOmx01YfYT9QX-m-ZF7W0pL0QP0QJGmz5KvItGU1jw83DyMk1wuZxoANkghuvtyi_PHBXyKyFhapoYY6dcgUIw8tWuvf6UG_ejWOS-nEW7YpGWO8JqnRnDLYvRitPer78RFE4Qt_MNJlLiHHNLDtO-wnD3oFjnZpDsFnU5y4E0mdEUWmVGRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148364" target="_blank">📅 15:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148363">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تسنیم: در روزهای آینده پزشکیان قراره توی مجمع عمومی سازمان ملل در نیویورک حضور پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148363" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148362">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148362" target="_blank">📅 14:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148361">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فایننشال تایمز: عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد
🔴
ادعای یک منبع آگاه: خروج ریاض از این برنامه به علت فشار واشنگتن، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148361" target="_blank">📅 14:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148360">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=TsjK6fl-DM--pOIXux1eBXUCXgsUncXqMppVANG0t1cM1HOtA7u5Ugq_-ZOzRKHMs5Rszvf0UGHnWJjgfRbVR2lFPAERZCkplTqRznmgmXvuWOOSWt5BcOQ-CneuNZvuEQniNpmfdS6EZS99HC-bu8L32755B6fXT1R54hpv6Wc-A7gwUN3XctkDD28hgyyUDcSmzHR8cm0t39ST6u8tfYGo00umuURalpHPU5SydpMDciTMjxHwKzcViOp5Hi1ZYKOJyrhS8LutPK6iBEmxNHCi0sFu3B1iKXMRqTv5kH9LCu2dpp3g3P9MauF4GB7dvGdUPG7Ku-D0iGxgt3dBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=TsjK6fl-DM--pOIXux1eBXUCXgsUncXqMppVANG0t1cM1HOtA7u5Ugq_-ZOzRKHMs5Rszvf0UGHnWJjgfRbVR2lFPAERZCkplTqRznmgmXvuWOOSWt5BcOQ-CneuNZvuEQniNpmfdS6EZS99HC-bu8L32755B6fXT1R54hpv6Wc-A7gwUN3XctkDD28hgyyUDcSmzHR8cm0t39ST6u8tfYGo00umuURalpHPU5SydpMDciTMjxHwKzcViOp5Hi1ZYKOJyrhS8LutPK6iBEmxNHCi0sFu3B1iKXMRqTv5kH9LCu2dpp3g3P9MauF4GB7dvGdUPG7Ku-D0iGxgt3dBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین ۹ ماهواره به فضا پرتاب کرد
🔴
طبق گزارش رسانه‌های دولتی چین، این کشور ۹ ماهواره را با موفقیت با استفاده از موشک حامل «لیجیان-۱» به فضا پرتاب کرد.
🔴
به گزارش خبرگزاری دولتی شینهوا، این ماهواره‌ها عمدتاً برای پایش محیط فضایی، پیشگیری و کاهش خسارات ناشی از بلایای طبیعی و انجام آزمایش‌های علمی مورد استفاده قرار خواهند گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148360" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148359">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2zdX2O8glrKCdH7qRo9QmNJMWyIKy7OcgfRrqmSCJmHBJTPqUKtt4fIgmRdbEW8SeIWIqWvrJluTyceKhlBAduVoW8QEnQqFMdxK4osq3dxnSMt3USUgvyHjBC7DAnl5baGokzCi6saKzj4hov9N3pTkUmITozibRX32iFWAF-9c9uSDYtT1O33nZWt0ZBKJytoIdUK2D3bTmdpqp2nUb917CsMNg4hPw9XvZVbrcvJVhyqjD7EMRQtLM_J6-D2jBnZIfwZzyUeF6kfYimUVT2pytSHGyXp4LFfaX969ZJZkKoxwS54afuXuH3ZM9pPvjnbnS2AiW_LhL70u_BhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فکر کنم اگه روسیه بمب اتم داشت، اوکراین جرات نمی‌کرد اینطوری به پالایشگاه‌هاش حمله کنه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148359" target="_blank">📅 14:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148358">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سفارت آمریکا در امارات: با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری بیشتری به خرج دهند و نسبت به احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148358" target="_blank">📅 14:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148357">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سپاه : به ایالات متحده هشدار می‌دهیم که اگر هرگونه اشتباهی علیه ایران مرتکب شود، تمام مراکز و منافع آن در منطقه مورد حملات مداوم، موثر و دردناک قرار خواهد گرفت.
🔴
همچنین هشدار می‌دهیم که اگر کشورهای منطقه با ادامه سیاست‌های دوگانه خود در تهاجم به ایران، با این اقدام همسو شوند، ما آن‌ها را شریک در این عمل خصمانه تلقی خواهیم کرد و دیگر نمی‌توانند انتظار خویشتن‌داری یا مدارا از نیروهای ما را داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148357" target="_blank">📅 14:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148356">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حدادعادل: بنیاد زبان و ادبیات ترکی در تبریز تأسیس می‌شود؛ تقویت و حمایت از زبان و ادبیات ترکی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148356" target="_blank">📅 14:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148355">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرد
🔴
رئیس مرکز امور بین‌الملل و مدارس خارج از کشور وزارت آموزش و پرورش:
دولت کویت در اقدامی غیرقانونی، مدارس ایرانی فعال در این کشور را تعطیل کرده و مانع ادامه فعالیت‌های آموزشی این مدارس شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148355" target="_blank">📅 13:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رویترز: سهام عربستان سعودی و کشورهای حوزه خلیج فارس در آغاز معاملات پس از حملات اخیر به ریاض، پایتخت عربستان سعودی، کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148354" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=J37FSYtRWcqO_P-dZdYBYSTR0dFuKXJ3huiRgVw0l18My_i_3sI_JofGwBMF043fpDRigRP6LV65BYWz5iRGoXMJIyvYD-JTbd2aXtBZ1uPYMPnpA43gXx75b-1yg1RTFC35Bo2o-YFmKlXOBp0gXQbPm2mRGwcUfXZ0bHQPCAYGH_4FA4ErKCN4Qa94ET4cUzW7QaG28ZG4ad60v9q_biWmpXX2uXF0sdc1JN-GzAwPkgzLlAhtOFqWFkwn9R7CbzvocCbNOTl3K7fLBkcNY2f7RFWiQGQHH9XA88Flyj3FU3uwhi2JXRYebIM-NU3wRYM0YKM82-XfIxsY7d1DPbjfQtvJCWnzpbJW3oawVCfvpowuwJ2geUW3a5tF5ml0nOj6bATnVr7nWWs_DQExm8fOxbm8t5jHohRKQekuIhOWq6m1igTepaLkl5g8Z9ymwJCspYnXDBJYHLGUbA0NJBlkg3pxnvn9kycF1_Uv4ePIzjw7DulDuZOsRwYymj8Chs7ismJWaYUSWzQSpg0Sz3DePD22kn3gV_WsNT3DX421CwE0hmcEnrQujW1290B6PiG4ywIHBcp7Dw0nCGYVd3B3RBGFoveUCtjq97A0tC1BLlDHYKnlasqrVkg7ZA4oOCsXwpZGG4hQYhBAbYZI4E7DVh_yx3IaSA1FZwnZMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه وقوع تیراندازی در شهرک اسرائیلی نِوه تسوف (Neve Tzuf) در نزدیکی شهر البیره در کرانه باختری منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148353" target="_blank">📅 13:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cExOGfQhBj-mNfylYL7rOKZ2ibCqBZ08mh7n2Va3scXcFct5cv3XivlOPVBmjd1sEGTnG6oPq5phvjMgu2NK2fZ8470tPHAgy7lUO_SOZAcCbQZzis1NR-e1nUPW6IgdVQlwesmfeqK_jgjXgC15czdIyQn422vPMZ5sRAsLDPc3ZCzz4wpDw2lrYMEUjUwz4294V6cXAWlnDlhW07yzFUK1D7JcYKDhuiu5z8rCicbBETulpRmejbvQCTKRLb9EAuAZMYAdH05eWknIYTaeHUrTcmC8tDNaFEpv91UfpKiIdSv-bF3TSEjfiWuUH1lYca8BLT9GprL6xKU61awV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز با انتشار تصاویر ماهواره‌ای از تأسیسات هسته‌ای طالقان مدعی است فعالیت قابل‌توجهی در این محل دیده شده و یک سازه بتنی روی آن ساخته شده است
🔴
آنگونه که در تصاویر ماهواره ای مشخص شده است؛ ایران برزنتی را بر فراز تأسیسات تخریب‌شده و مستحکم‌شده‌ی مدفون نصب کرده است که فعالیت‌های بازسازی در زیر آن را از دید ماهواره‌ای یا شناسایی هوایی پنهان می‌کند.
🔴
فعالیت قابل توجهی در سراسر محل ساخت‌وساز قابل مشاهده است.
🔴
وسایل نقلیه ساختمانی، از جمله کامیون‌های کمپرسی، بولدوزرها، کامیون‌های پمپ بتن و میکسرهای بتن و جرثقیل‌ها، به طور فعال برای بازسازی این تأسیسات در حال کار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148352" target="_blank">📅 13:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حاجی‌دلیگانی: طرح سه فوریتی خروج از NPT تقدیم هیات رئیسه مجلس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148351" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / ایلان ماسک مجوز اتصال مستقیم گوشی به اینترنت ماهواره‌ای رو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/148350" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=Au41B8w9cDVsrQysuwJSwvwZV9qrYTe6hL7rZZIhGdx6uWTPJ60U5yRZ6kiRwOv5P-lbeRII0CVRHxwqS32OqRg6jJCrZvlHgLxTukENoFQxoqQKwqk8ApQd43O6euEIVx553bagxY-S8GqWQ3OC1_VzT8Q_RObA6KUVlcky8vRx1sv2XiG2F6UFNDf5WNhAQ7JZvhzSqAPh6rSEJVbIDGh_bubRIugNiR7yS0XmGcJx6MACxKnvnDfzyc9M_1VlL8ZBsCtg-86E3-D9jEHpkIq_3BI15kCiUEF4yENNvQ91OC2uYQTCWuOS1sobMjGfGa2Sgk8Pb0NPMeJKDNzPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی برلین آلمان، یک دختر تریان(آدمایی که فکر میکنن حیوونن) به یک خانم تو خیابون حمله میکنه و گازش می‌گیره، زنگ زدن پلیس، هر چقدر از دختره اسم و فامیل پرسیدن فقط پارس کرد، پلیسا هم بردنش به ی مرکز نگهداری از حیوانات
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/148349" target="_blank">📅 13:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گاردین به نقل از وزیران بریتانیایی گزارش می‌دهد:بودجه ماه آینده در بریتانیا به دلیل جنگ ایران ، دشوارتر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148348" target="_blank">📅 13:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فارن پالیسی: روسیه مایل است ایران در شرایط جنگی‌ بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/148347" target="_blank">📅 12:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
قالیباف: جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/148346" target="_blank">📅 12:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
زیدآبادی در کانال تلگرام خود نوشت:
احتمال ورود نیروهای زمینی برخی کشورهای منطقه به خاک یمن به قصد تصرف پایگاه‌های حوثی‌ها هم دور از انتظار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148345" target="_blank">📅 12:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148344" target="_blank">📅 12:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
واشنگتن‌تایمز نوشت: ترامپ قرار است چهارشنبه، شخصا در فرودگاه پایگاه مشترک اندروز از شی جین‌پینگ، رئیس‌جمهور چین، استقبال کند.
🔴
این کار غیرمعمول است، چون ترامپ معمولاً از رهبران خارجی در کاخ سفید استقبال می‌کند نه فرودگاه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148343" target="_blank">📅 12:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
با تصویب مجلس، وزارت کشور مکلف به راه‌اندازی «سامانه نظارت بر ارتباطات خارجی» شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148342" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148341" target="_blank">📅 12:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgPXYFb0WKkiLXP3fJzxviJDw5cH-O26YiMrDiVv3xVQ59Dx-Vu3PRKAklD-xgbUmS0Ji6xAjWh6s0yKSSz_h105Sfnaz6KKd4jXe4eR6UrEbNhHD7gYz1TjaeUbvAGjwSp220YjhYSG_aqiSnG3U8ixO-j8MYavqpPkIULtJodBcaEltFO8b4GYWhpRXVRYIJKJdEbjDz7-vnBkWMWhajlGpdQwDmKNGn4KKOYUTfV54eaUzE6HQvtiDd5SH3Lgzc-7s4Bcl_GZmzHezRKnLJtb9hXMTi4rHb-xKuPqVNqDkduDCbM0jY9pfAWU4F3m9WNr8guWbmBAPCr5TqBjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیمان اکبری، مجری انقلابی: کلیپی که از من بیرون اومده و کنار دوتا دختر خوابیدم هوش مصنوعی هست و میخوان خرابم کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148340" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
روزنامه کوریره دلا سرا: ایتالیا آماده اعزام ۴ کشتی جنگی به تنگه باب المندب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148339" target="_blank">📅 12:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=mywJW6cZCResEqqZLvvOQqonU3OhCcMMxU6K-tds-_hrw_PhMqGZhOeQeOgluzuQ0G3G6LnJA1CWOuMIq7aHWm93nxrNIdMmFSHsUB7flUCUFcj93rZ2lAA8HdvJ7NzWP_M9Wa9yH3xfRzvCiQO5EgNkejSUvdtbxz_tRmAf0cnFrdUk2tutFI58I32FmjszRGSlogT3p81BpzXO24SoL3hDOq7XRH4sPv39IPc7tRHInWKryl7coQL9eEQM4F_g3yj7h0TDRlGUAqF7JUrtw55vPPuOTtpMxaLmfRdzVRoipvEbwrklDTQ5e6g4Cfodlprfgo6-BYSsBKSjk0OzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c84f4e05.mp4?token=mywJW6cZCResEqqZLvvOQqonU3OhCcMMxU6K-tds-_hrw_PhMqGZhOeQeOgluzuQ0G3G6LnJA1CWOuMIq7aHWm93nxrNIdMmFSHsUB7flUCUFcj93rZ2lAA8HdvJ7NzWP_M9Wa9yH3xfRzvCiQO5EgNkejSUvdtbxz_tRmAf0cnFrdUk2tutFI58I32FmjszRGSlogT3p81BpzXO24SoL3hDOq7XRH4sPv39IPc7tRHInWKryl7coQL9eEQM4F_g3yj7h0TDRlGUAqF7JUrtw55vPPuOTtpMxaLmfRdzVRoipvEbwrklDTQ5e6g4Cfodlprfgo6-BYSsBKSjk0OzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: نظم کهنه‌ آمریکایی در غرب آسیا فروریخته است؛ مسیر آینده نه با التماس، بلکه با عقلانیت، شجاعت و مبارزه رقم خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/148338" target="_blank">📅 12:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دراپ سایت : بازگشت زودتر از موعد ترامپ از کمپ دیوید، ویدیوهایی از برخاستن بمب‌افکن‌های B-1 از بریتانیا و هشدار امنیتی آمریکا به شهروندان این کشور در خاورمیانه، نگرانی‌ها درباره احتمال آغاز دور جدیدی از تشدید تنش علیه ایران را افزایش داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148337" target="_blank">📅 12:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju8ZMDvCjgJVvghJM01q_rQRCjgjNF6p2YBewlVsaY5yPC9K5ro0jXJN9Q1wfIR59tEi9rPhJwair1Og5oTcVnpkpw7zRtWmDNOADtpPl0dztdDNaJZSCqqrA2Utk_ogShoi7jYpfY9CLjwfWE2TP-ALaxf1Ad9tyIAYppUwaHuG5g-XDSBW6ot8Dv3pzkpFGdjDWZ9Ec8zsa6GQbaHxPRmr1cxQFdiOG6tYaOZDhavBdMvhYo0HyAMVNUgZW-ix2_mYGhy9hJgZTRJFUkak6gfCLjtmwxhQYmmJOaBLskMB1tcU1XPVi1FdleYmppukE_aab8vjdkZ6vMKIWzyMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: ارزونی تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/148336" target="_blank">📅 11:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5FX14n73Wc2BgMowp5VerUkznx_OX9WpRIOtnNw8VjcMr2Pl-VprsNz8KvilLp2Z8vrMnvE5ENj5aAjBHPucB4h4XfvzoH3bfYwB9nrggPDZZJmTKbRAIzAkt1GaQ1KuyqpnjBMBUAyZOnhCkwyVUnIRHQxNi4uvJNTy2fuWo-6K5lkez4wiJEft0GjwTsVkI8cIsTZEd-IFwDhhYrjFYDOVLdUDeE7FbhxDyBW22JluClh8gR3ekNNguG1X0MupSpawcrKf2jCXpWRgkUWk10MXKhKPC-5tFtZx2qes30LaIKP7cM3oOHRXxTAHtZIcqz0Mopzov374m53n_9kQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حالی که تمام نگاه ها به قیمت نفت دوخته شده کمتر کسی متوجه است که این روزها حمل نفت در یک سوپرتانکر حامل ٢ میلیون بشکه به مقصد چین بشکه ای حدودا ٢۴ دلار یعنی بیش از ٢٠ درصد خود نفت هزینه دارد. رکورد بی سابقه ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148335" target="_blank">📅 11:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مدیرعامل مترو تهران: ساعت فعالیت مترو از اول مهر بدون تغییر، از ۵:۳۰ صبح آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148334" target="_blank">📅 11:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارتش اسرائیل عملیات تخریب را در مناطق مجدل زون و طیر حرفا در جنوب لبنان انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148333" target="_blank">📅 11:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148332" target="_blank">📅 11:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrlT8gbdKswixG6DkmW1_oFwaG9LM_MaSBjdiIE6srRwwCF3gwhC7GStiEjKbCNxz_TPdbVA-9nLLnY58h8QnIvlUJveeenH9F6rqxAjxJlIrDGe8jirJSfX6iGaGssHup_4yndTEfcoALHV7oWPBaiTkBVIp8LS9sA1tHoRsP0iEU5nT36qdR4DjH2iv1XWElrUnjvgRCEWd0adfF2DRxw6etfMF24zcfoNClGOGA5PdAjKsBMxzTwy5xjmCZmCypzYlj4oN4Cd4SM2F1CnHNnBIWVvpwQ9lcHMRie62fALRpN0w7-zHnrcNi_BtRrNYreROqTBgDoAFPIwgMk_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار بزرگ امنیتی آمریکا در خاورمیانه
🔴
سفارتخانه‌های آمریکا در سراسر خاورمیانه امروز به‌طور هماهنگ هشدارهای امنیتی صادر کردند.
🔴
رویداد: با توجه به تنش‌های موجود در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
به شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند توصیه شده است سطح هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند.
🔴
ایران: سفر نکنید؛ همین حالا کشور را ترک کنید
🔴
عراق: سفر نکنید
🔴
لبنان: سفر نکنید
🔴
سوریه: سفر نکنید
🔴
یمن: سفر نکنید
🔴
غزه: سفر نکنید
🔴
عربستان سعودی: در سفر تجدیدنظر کنید
🔴
بحرین: هشدار امنیتی صادر شد
🔴
عمان: هشدار امنیتی صادر شد
🔴
قطر: هشدار امنیتی صادر شد
🔴
کویت: هشدار امنیتی صادر شد
🔴
اردن: هشدار امنیتی صادر شد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/148331" target="_blank">📅 11:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148330">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
روزنامه عبری تایمز اسرائیل : عربستان سعودی برای مقابله و دفع حملات یمنی‌ها و به دلیل کمبود موشک‌های رهگیر، خواستار حمایت بین‌المللی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148330" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQsJc4iRhMbkExcMzwjf9ettocPmoJIpJQupYP_1WXQ-_wCrWuTeakXiaGMVy2_w3sMVFkil5FnNvnD37zjlqCZkMsNUvg4XcG_oSHCW0DPeE8NBLdMbiA3N-1PK7Ai23ysjtFtX0pGvPUbtrJLzIrM-RwhxwDfKPX9mtWTWVq2Nzugu-bClqHLfvCK2NjBpZR7kTzcZSwwBZITIFKkQbAlBTLTsjsmgrfdhjhVZcAbY0lD2Z86VW7L3lCVyo5bQjnME6tEd_SW2aGQDg1XkZOvnl6dW2SP4foLSMYJb2qjrlFBMCIH5jAa1xrZ_Nl0uXP1-d6YC3aPvy5bo_xf8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده جمهوری‌خواه آمریکا: یمن را از ایران آزاد کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148329" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / کره شمالی یک موشک بالستیک شلیک کرده است.
🔴
این موشک به احتمال زیاد به سمت دریای ژاپن در حال حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148328" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
