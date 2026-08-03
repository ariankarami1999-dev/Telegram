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
<img src="https://cdn4.telesco.pe/file/LHOFFhiazTWK7cVhJgmWtwL7gCMmVeMTDmPvPB-VYMQQ7oprYo_Q2SlDuiiRLKtY_r2jl1H0ylOKDqHnXkk0HyUJGCCZqkosH_Nl4lbMknjVER8kTbcMojyFiecAbosRqZ3lK7H5v18s-tASzdgmoK0vGp8RraI78Qi3nJhOZfPN5tt3VgTuv7Qb_Ce9q5lmObkDnmKNPCvh7rZUFGMIUEm3XxxOqiqL1mVp7Zm7RWRH57TV6iXBrsnsOeiZjgbTkzkgQ4HrEF9EHPzk-F5d31LHjy7lyV-HR61llYsSYbg952r7sK3zv33pG9sALRdUqVqdlqiffxyc94mWCBEYPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqjreoQOb16SkBrFmFPGc2SxKtkUVQO_ovP8ahDBgqntui4BiGqL2C3KYWaojls9LJkMRULY8rquNAAfQYkZzKPhzFAXAwXrQ5Mz_d2ngbs0W8JvObZ1Livq8ta4_kw0oq-20YDLqLiDx6BcD2w6qQKspX0Pxx7lc1dDUA1q5wF-npOJYbLgGJs3fx19ZyOPd-xf0hUjatPmsjub__gCcbutnkBT3Y8a9o378-HgD7RIbhwah_W_7pQbXRk0gxQdhOpSPaG4Eo6ysymIDAPumgfKrpwOlTaENRNU8f9vFVE5Mqefh_UQxMq80QTkbPMORZWia827BwyAUnhByDv12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idvg1-Z1zyyTKWOOEtZrU895NWbVAKmjnHsIWGTV3lmTdtM1IqKe9X8IuHDuD1Qw8KgO_TYfQy2eTOFTTgdHrDJvV0EXILzVZzm_8miwe6SDkl_4Vq73SbwKSl2mAdMG7VsDdt2FxuMQ9WaWJj6CK_HG6vK78Mq7GJy2lyboujunDd84DTKnNdyZcgNVzMfSFwMyhucCBmEr6PG076oP2UU9M7HWPlJlvyee-ah0PtN3hRfR0VIX3I4nIid-QzLV0CLc1k0yD2D44HQXqHIgXCcSwdF2vvCbDFlOjsUTEeCf6YtrKmHfYObHauCtzg_k9cRj754a1piBOFoZ0-eTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEfJtMeQ9exu3v3cTZvdplbvxWZg6udvmLsbPp2-Zt8XJIRDd-0hic3M_M_WxrfJE3xUefXvdoFeWVmOUhLzsvbUjykJlcbvFkNUCC4RyECvtvm7mjQYhMho-g6HtuY75KLnzAtccbnYI-5nNWkFbZE-_1nJHQeJxeOqrZ7zop39VWdFt8m1tEjyoprlpUYUd8PJDaLw1b-fUjT_ug0eTEgB3-xUCWyPlURyDSowMAcNOfs35r7U38Ysazrak_gbEYezDUPECdWpQiQ0ffvtlYNOACW-ARv31uvOcDePnvnPZkIhs5bFvZ5M6gGuSlq1cxNJqHQVLjNVm4AvFwbYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQOvin7quw4uH60SkxivND_6RdKd3_gOzhXcHN9aioeBU_jH2qvUyvZRC_SJZefI3ujUrqupiUyorVhGhYsz774NUGi5-EhGWobELC9ihGgtQOrR75ywdv1HhQv67eVAPknw0FkinRRqYebE5-z5VkfH5Y0NbMo4LfO7TE7-lAy7lHS2zSI-hNLa-wuwz6uyZPZb4GCB890SeQmhMttuOopaVMmIOwVAK4FMUt-86lDJFCaSy2w4cUSYBbAxnT4qIqKree5ETSap3t3-syQlWPmpIKcTfcNcn1XvI6j26JrpYsxrhTgVhPUuYpJ_PpvQq_rd5XS6Rkje0n1H-UGpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t37qk-tqgP693Q7NV3kUjUoOEyhgbbzJmnqzu24jbixdCWf0WyJqIsHCSItySi2_rg04RBoC5qKFWGrh2yOqri3_PcOuSqBERTyyjnUZ1lu6QWhVO1ATpDdRoXAtT0sGcVsYBcS725v3F-Ngy03mkgCD6WCszqeanNffHlX-gD7r9NFlPQZFSOxOVPn2rI029Z6Yfi0mkT1VSfrmVsii0Ml0tCjOIor_jPCEPZlvxUyMQtz-dHMeWRMmpVaVNwjSaXvHyYFjndz5Oh_B9_npF36xLTyeUezk2JnUUnUsAxOYBLk8L6IlvxE_aX_oWRCPiZ29WmZd30qxs7vOK3Pqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27047">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msPOh1OPKa5UFfsnagmoXwYk2YVxEfSOwMZiChUAH29C8vVMdavSCbsKImF32lzzo7HQxI1dCnrLN2bvtFIJQfyxrcu_EKHJdzETHAzg2p5jL9blOm7Z6apppKrUfUjzKWoWEyYWaRkkIcpKZ2TaZC8FcCRmTR-s77c-IybKEbFpouk4o369MQKtGhL19oHNXs85RBgtGiHZLyq24S3r3uiCEZkIv4mBeq0LZuQx29ULRge_VCyyecyLiEmydoncHZkE5DMIs3s1jhHgg5JaCMvVbY7yIAsDMwS89Yqxe9MW97o2M3IL08YGpj1VM24lfu3UcdNZvIBAgro3cRlCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/27047" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ5s12losXlH-ETyj2GoEj64rTWD0sQ2FtkMu53IVrTNXsKaBPBnBtEbQ6Hev4kIEV5GuTADMcnHU8H2NfMOs_P1DQM0rt9GdKSyLf1EA-5IeOtWjvZ8lIMG2uFr8n2hpGJXNNwTg2gusmJF7pM3EVSyrrGOhpWHwKWMRRmBOsuwjPx0Doj8-lSZ4Fz_R4iRwZk6YSTnYlCEpdImrZ-BWYYPp9UZD8hWmWe0xrUaglBxLIYoJ0sxJW1m3wTcElU9hedplZo3FICBH4_zURxpYdqpsl-M7FQZjUF9oLgQuwOIAA6mye6jHKoFVSj5O3KuzSSJwOO1zmoex5TPVy0WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTi4ky-eEJN-FWprxBMatN7mijtirC4LBjo8mUZbQHnSMyWxFIGAyMjf5RFIojlp-e0mN_Pp2pIdKjTrWZyFXHwxVT9WpYamTXLTRdA8o7g2Y67-dnoBRL_VsFwPBLWbdcpIlNEbX9gcveNATHGndGcg8Mjde02whlMFL2S8CvDVUrKZaCuafWWYaYKvnQaZPPtnp22mrFaMK83iBtc8vIDb42cZX5gndKhWKfGLtHe_-rLkc2OKEm51MAAkUOePhK_QaMW1DvlrATX2CaUV51F4zZ-wzFH2PHjZB2whLXmNZVfzidYXyY5s3hIB0DHDqyQMBMwgiLsU9fY4f8xBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-VH2baEseos4w0Q_nyLH33gaRPyocmxol6clW4ALGmnBOBWzlg5cFCVMwfOM7jzi_DSl2zLvG-tJZGx9agroI0im2XHdteYdSS8KAKOq2P98V5D0R_Y29xkTrN5UJFFSLsMRy-adoS5Yf67bpzdeFCCqHwjMjLGbQ9ooaWOKQpFPrF36-AF2AMd3URHTTWo3h2lDO_RsGALeU6Cgr2vdhhLQpqKxErsbeWLEPyb54Slno50jzn9ephB5iJL3gq96bOIiRJ2C3miX1zxSNtEJtnovPP8U7ko9ro4UECywEJQ_9leNCLFpP06ILiSiTyving9zi7hDvGAE4_TaDLU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ5OBpHPx7pYSYauVAm7SyyqcrQR12S2FVk5UJdljRJf_FXb1HJ-eWYoFt0WYq8at7aHmbXIfRxEAeVRNnX3ApExP4DPeTME4a1wjTDDLMtX9UMvgUM32h91haDItmwx_TU6vdAaEaM1vdHzehCTQKXdOc8_DlzGpOQdJhi6KpR6NPnv8qqoSqUQ78fL5r3mz0V-sTL7B5KqeZp34q4fCeCeQTfW16zyAnwz6bLetL9lti61WwNmyBKgVJKQlBGLM1WDgC_d3_LrLZKzie4s8Fj5_VOpPJ7cdGatelnJ-VMrf2bMkFbeldbNK18dAs5UPAAymJN-BBGbS_zS4nJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahm5JMMp_dTaKJXmsYQKDa3V1NSPh5fMwRWKM8X0j24b7BITpoXbDwfW9Cjg8klCVv-OrbzZ2QFkRPQL6HY2u-k0AJusCaZcr0LXmkWeJmXRb3UzNyRAvqoxvc-nY0zJDJ4MNJvZ2NeMUrkEUsBmEGfSNXMTsul-XsHuvqvswXHV6vtfkXOjSx6y88s0ojkB_ktzKhI218bVhi6jZ4bFcwK3035afobNggWo-HKIyvamsxr_Mfan0u3rhAhJIp4uJ2ANql1Av7eVlNwYtT4zNRe5mqtj15XRa4gk6F_r17csQCZsJnH_A1u1gV9SOOaksA1Bem9uG4bYm4XYDFiFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKlj2Q2SNYbehEmjcLUYnrHSgprVuOM1pt2IRf4FXPYFXjZLrIWfJgRAAEVuumICY5DEfo-IPQbsjR_nnj5WME0DR82N-lCdk8i2yjx4LKdzJMcyGFeVJNUP4cH4yyYb5RwLoa3IkqUTbnCtKaEJW3MrS4mshSfN1a-ivd06Un4BSlSTFVkJZHsNFmpc_1dwRB0821ApZCtBi4RBwm92PXyDaI6M9ZEAlLgBF9v0-Quoyk2ePItr5TPYKLysaJ116qPyVGh8qYKsKfx0RVKwZrPWxVpg7kAnDyL-NieIqJjKkjKnoRxeakHKPwVzVy_37XbjSnMR9QNFXCi4w4TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rNqPJcouuWsOqSu3e1kTCiWohimJkl7w-0gfnFMujmv76MM0DiSewLNNaGke8riyFSzGbKlotNlkMKZmJAENGvFVQJ1n9u86FNiH8wPrGDDvP-BLcBveNIGRAHoby7zuA6-eyh3PZ5x1-FvoRujEPruipAQXPpC0z71gDJ4MFE-dX7bB9TnR3nVPURkGGOxdPomZh9OhqKSPQTfelD0p_RbXgEatHyQyYpxJL-CW-uucHpzai7DjkAwVFurcUDKljw4tAG0zVOZXvWzj5rdbxEakzCWdYfZL0B51aZ8zHGQAjpEXZLPMb4J47aGnXH5o4tynconpXv9HbydB-lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5EGC-36J6cPMSMH7yz2DedDrR66rKHzDq_NIhRGQl3069m7S5m7N5oe8zhYyYIsh2WeOC6fxr2rTPIgb9eXOCyUz6NK08Ss1JSmJGGqvV2Pa7yJBYEK5SrCu-GgrPerXnCTuHAkahjVKqvTqA6ab4sw6nWeWAAb10GIoqGmeKigVbJVFTuhGWSu36uzQ1qRQT21cB6NcggLe-kr9bUqHzUhcEaJ-amYE4NKKUXhxlkNznNCBg7V4UkZbaN2oeHHfQh-IGR1WuMtPQBfNfQg4qfbhvVIPFRhJsckTTtcf1wxGoapYjCzblpUy4QBSii79PWDY3WtgZy_YU6MJtCTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6-I_HHcCFGVn-0kd_wF7_vF2E-YPA_HSp3eLBF1roahFI3Cc_F4oz_6AGf5iuHMRi6hi2073fxYEm04BSBGyp1NrjSbqFA_gVrllktv5VLHUWm20XQEj4HSJsjD8o2xyXKJTVFF464A-BljBBn2zS48VO4KDtQfYax62RFxdZ2HVBbqmGdagzwaN1XeXpfYTljGUKNM1lWtNS5LvB_Is-dq6NjwGXq0BDRVUkoyCJcfyyjgjMG54YRxHq7O32ZmQyQ0SnVHuwizAT-B3o-UwvtZr2NN3E_fOK6BxNCh7I3MmZHVOxIU6Ah0q3ZveJKD6vAuH4y1phExXFZ7g4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvkvtPvLbNxXMvPqOx3nCzzCxgX7xfKnfpdw1sAQGcgX8GNArXh-UU6m-5cfGHL8V5tOzJexwEyqqbUjqFa0F1aTriJ4tINWaa_iXef2LFuU0lxM_R_Uk2VbtMdunPIzNgD_RL2FRrU73vHM0jm1T-dPBiEcs6HGnjjThkwwuvdVFmitSSzqN934nH9gTCihhlAzXVg7SblL-Om3O1P-8m7BwR2vKeBTlsk0aLe3Y4bt2fsVXvf7QcjCcTTd6VghnVFi5nGlVGRrpPE45qPg8iPdIuCccUs5Sm2Sj6BE5nB7O8a3WFeDfLS_yEJVCs8xJi2cQfzRbEUe7h2gmx1JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVKBsvp33LVPzlWNvBejbR28J0kJvnIb8nfSCVfLG8t4f3NgIb220AQ2zEE6N3JeUfS9jlv469b-ZUemeHA2-L1aGA78SjxxlAnfJInAoRrwruJkVwLzWMZEhJE796jYjHMWAZJIIeqIVqId47i89N94u9xX0cOVXalckTg2qqiQOSzR9qlOq5bTiq9AeGeOlYTt26aX8rCWcK2hIg7arpCi00L9MspHiOZwnWg1TqwVYXdMukK_CVfRa_RoKF7IsjAohPhzghyY03lAfWq7dwLPpGmL2y7k_iSMbo1pJCxmINRK9zgZam4485xVWmNAUJ5wZ_wXYM_G0-lwEzVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMXV3VYGb73K0vFtmL5Pf57-jq0226FVbi76ZNbTMaWQlcWkIDYzixccL_rdZw6NU350YjmWNUg-xA6Q0Vle2f5X5JTRRYmhKYDsfIgCvVylemSA9OnhYSxHkWLBvqnEGnlanVjkc9HH7k7wCAGG2CzH5i_idOpExpon9Sv5lJ--HzhqMslkkARaIgLqKtOrKbzDizAw6bFNw0tnLLYwp5oQODygrL_sxXmM11tA0eb0aRs6I9wkbbObl52auCWGsJ1m2xQdRA8j9saRNLARdB8UCf6NeaPwUdwlERgtoYuwaR1V3YXWUo7qmUTDdAUTszH9FBAQCXGZIS0nPbqX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJo9enwt4zy58rIfDVqfnXv3kl7voNMgPrEsI2ERojZtXbn3__8m3DSrF4UOpYszAh3yBo1goNI0Uq1xZXD8md_5vwzitfS6b-Mvt2ljkIR7_ecJV0NuWGRHot9DtBTKyzmFI5ADPswA6LaydP-4m1B9QJFQjh4Hw5nJrnpcqHTEfYbXBHudv9jvALFKWMq_IcPXQ3p5oqdgQcHMgkLX3sLs3drSes4dqI8lBG_gNHGOdZC4vMFuL-YrnYZW2Y9iTaVGFJ7Oo-rgl15YqDnDD2Rz8d3tfZ_DHXwLGQYYxVxVelVVaTb2_lJo6R5Gf3noUuD-a76IaK1wHCpLcRYE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0AKEHVxaRhZK1UUZdxNVs9PBb5MRaz-cujCXOlLZ4c_PttON8vJHaZ0nwyaUyan4rAe7eEg7L4nopTAAqrpEnbGzIhtPHgZK2h8bTykdurj6j-Yz0HyGLJHTYfCGQBUR68aESYpYhpQtDFGDVkfOw7aCga-qKRW19QXpv5Ut-DULw2c-Qux6vFcj1zMD9CvFN50DNwj1Id5TAtD8RkMVp2bn_XGaDo3b4lMxbKvixP2v1gfRu-SZQpRALdf7OISaLWEZTPAoBW4S5UxTjHbHyPpMbqPPxSzngnrfG3Kqss7qc1gybwZ2a_6xeku9nsmDpPkYhZ1FsEv2tGGu8mJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mes7OGWkTAMIN169w8KBJG_sh4houu5KyWO7pexV3zsVnD25Dhtm_IotW8iiNWpBT-4ci8TUT0x1g-mrrjC__v9fmFdmesykSow9GL3X3xlXXjZWLmip43UUJBN8MjHplBVJ-TfKTIkUF8QU5GRNWaGLOk6v6X_cGymsngeBkWgeFhtnD-Io7dmWt-QhwYqcEa4B0pERhR6JlT00tu4c5vmDmZ7kRcMJ0lJWEBO3Ow6O3dCxDHkXmk7iOvMunjuQQFFKdpQ34GNsXLL3vtzZaxcNwiezEfcvx4VGIojzfFYcuHRwU8FUalyJuFC1i0y9Mj-G-HSqZfdwjZQTjnYz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNzNh6bV3tJJcOW60H0j7U9q01LECRyOK85_LUZ1WU8MLoOCotjh1GKdtMu3MQaA2zzWTm9IUkiFHtPblVy-XbdLH6mJTGjSYy_69HDkKVtMSuOdulPw0N_s7v-BMaNeak9AxQ68UB9Lqeh4ZvIgHF0FG3BwzFFHmBZ5JHWOKUNTEuwCl9SBCue9vkw8yLsgEXKTETkuuYSCEIwyEc-i8_t-zt8tlj-phr8wDv0v2nE8ZD7rq5X2uqEt-PP0EBuYncR20XtuF5wvHSmrLIfwWbiSFQ-ng9TfvCbqUQX56QJLkVdgXiV8BDnCStPvn-r98N4Dq81b7_FsS3RQc8jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo9NwkkDziBUxWOOigOqedvpCTetYt1SPhSLAi7Sy1d_OtDEOB-_xLA6OFmq-aufafP6ig8wfIcGzKC5SqKU8M6DH0Xm_yIAdPK2mhIjMuDv_q5e4TeXD5gUXhkQDFrwzosk5tmhxfvBOyjmny0iqMmTpQUi4pybpkWT5LWDnYsxtJHrG5Uy-nQ0NurlY3tnQOlDIG8J5y8QkCLZk3k4mLaBefhw7gKpDBLA97lNABzhcuwYOBe0YYP6xB7lv5ztVdrpsw4Bukc4c_b23BsX3FYmPXqV2VNmcK6gZgdX4gjvbaTGQMFyvHmEQKMYgporijzk6X7xfOSHl32Ni4WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMMKvOvdjzx80lvPNdW8CVDcDMz1ELu288W9WSclaAoTxdWoVe6H-sMn_FU77sjpGJVPmjeFffflNY1dno2gWSGYVedX5L-qKke_d7x6_Yii0JbH2sVIplGomTBR2iibL8NCb7oNEzfkMLUmDN6RQEJQl0sz0neWy2utXW_yga5tpR_6zotFanGoKTFBR2F1XSZBCjMFw8rkcF9KW6o-Aqw_yBakY6zBgtxp_eNbv465tkX3T2S9G8Q1LmFaZ2zOErVNSCm6DolBTIy_Y9MnkEKh3f2Oze9cc0SnuIu-sXlQV3EpnN6hvVQxto2labNI7wtNlGBje67Zap1p6TlNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi-IfJfrN77ghCOQbMKxdwoSqsd-h8TiZrsW9Ssi__f-9dbn5XZo6_NeBeg9Uxi1MnujX3N72B9Dsc2M_Rx__UC-dWljzMIHSDL3utsKpwzILWf5v6_BLMamDW-KL5N08L1KSPbMvEllea84qPhEPsjNfqbkjgjg-FqOPvteV3enYIKg68WIaqpmszeks-LG34jPHkgNxt_vtr5HSdW1SSdN7GgOtT0RcoeYVD8OBj8ZlZrkOJ25G40TYnlISSb2pjK68yzdTh0jXDzrEeHkJFk8DaPTpoq5rPiG-7i6akee83khSQKoa6PkHnD74llC-hJVE-8qvWl9RIgrwMn37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjGulgGRZquHXDPRWDXxV-vMy9xOcXzfe4CFT6FgmPY7KXpK1OejKL1DDFowRGjpLXIkplUFMweVQP2_a1D4Gj5qKsyZ4EdDrnwEu5pYIrFTTqgBGp_TxyTBeez-cYIjSd8kutWJRDEqn2kqKF_X1kISWphvWdw3Ki5EzDk2Vjt35cgoakkm8UnVJDT5_sU85F-zER2qm_hHYIjdXuOY39Cb7SYt0lgszXcKWbo_zMez7I6CottSMxaDcGtTdGIpajLUXEKhPamY10WaDBXFT_JkRzgq0M6OzVj2OMK-15B-vUk75C8rlClsUIdFMoLQpEyoZVnb0PjAvmEd-GW6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=qP88JUVm2HEFcLuoUx6otWffHwSbFiP5udcLdCjK-5EDWAzWlDo9Qy0Rmftlyr4PIYzBh63MpuWrshZBCTnVigqbHXIQbh03yuxDCrqGt8MdkLi6Ykw66dK716lxkwTXSJdIDqhNnmuHjb2wdOpJqVtG4Ls_wEDaIOAtgxjrq1jmFYFyM40V2vEQ0yufjg0Ztb7_Q_JTBnI1V-No-uUwNUx-TDgOvC73AbN2W_Ab6uP_-Ix5WOqF_ORGaWUrpPgKIdtoB1GQO-ERtz8_-_vaRt3ycCfeQ7a6BTXVlkMtM7qbqaW83ywUQ7bXwRhVyOTuxE5zQ4fcSe-ffHRDwsrpKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRML64vNqrdwk_xGQgEF6CQhv9oWzTsMjmk9xwYNmti65FtA4wpiK3PQjcnTX-WH3dkizz_ZVZkzXKMRhDBcvv-GVCIPxYKo1_Vq5SLpN9X8T6frO2JFjbjjxfqL96PLVTv6_sEeoBgj09PHL4vF_jDfRp7Z5LHLufYr3yFMNd-pjh5dSqvxHToEPkxlTBAR0svmLX-FPD6LCA97Sq2ydLXGS7lzT_d314wNN9wsUiBG1oNhhPM8uaNhf61APvTgbwkNSAZWph5Ldj4aqITmYwCkvWtp0lBn2IVqpL4GkwdGf7fB6yCzICvqMVtA8t1-NdhVaJjqqJMhbFAlUQT1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu2Hw68RqogfcpuztEdpHZ7B6kMoq1Bl8Jz660q_QQNTPbUR-wCcUWDi_BctUH0Um9FtwhjUKoC3mVe5HiVoJfWk27WxhtJWRIUOWVEPfv0K2u2tqik6N8HbrKD8puVUDgjcw-ASwwF5oi1xEZHCQg3M9zePYh_VsDBt9HvXE95kCbldtTjUIS8fpxbqiCHu1QIAtKH1OPyTKO6gR3vaCQ3clKgwWBz3GG-sI1t8GPRbaxadONuEGA90aei2W11VwI-4nXRKqSXde_0WQkVAsDUbSuVVsBM6fQB2eW9BLF3KGt2sC_fxTWpBYq_MTdbIwgrzH2Pmwv5FDblANRQ_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtnqiEvNMF0c5X7eslOduDPgGqj_R_1pX0MaO8qV_elNJ6jV069I5GWHcr2f-z_aQ2CkJXyoqBCK7YNnmEf7WV0QlU3KBUD7D5GjKq8LN7Hub-Q_Q2LfF5eqr7FQOqr6GhnxVpSSPDiD_n8S6-ipRaC41OxEy-FxrhN4iaIj3fXiHeWhVW7mm99G34oXkn0JubKxGakJFwfOrW3mf2Z4pP66fsFXl2S3_FIIzDKmzwRMonA_zaaYnS-ypWnyKG7YPic0VstxGNfuaBAqFBNmtqofOh37Qh5ebAn5Tn41xw20Kdrd1Z4Q7JxeYTK5b1sf6PXDjb0H4ovIcaXewlHi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-lrXivIsqZPFGKxIlb6qUQrn5kwcO1cNSfUk1ZkJbom7CuHlnQgHV0NTrQjT7x4aT6T_3liigQRPo0dyQaCt3xYkzItqTMxBhICChGEdR0aF1mGkLzBSQXpNdyIpsXsXREi32wpqjQrdtV9Ed73yOIy3XYIpLLkth7BfDI7S8EpX-CNt384ErxKC8ENOcgT722PuwW24tRUhaffXth8beFD7Sz6dFob1cYyNqgnaUU-iSJ5onNIfLjuS802nX4lOaDly0EyfL5vWalUk2Wat5fWOX1sNb-bau__YgcocPpQ0FNnNWGdKslGTuWMUfoh_2_IxDjyuMZ1pJnOpkiJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=K4UMRLRL-C1BR9Y3Umzf7BNyUITxkGzC9fiAV0uS16Dkkk7uMDJjBzu6xKOGfNcWynDfY7oa99RLRt5NPlATPk2v_7d2C4ZX9UlKCiF5a9KloNEd7ybLj_v6uluSbeD0EHeFOJY7BqueqZi0ew6jpRlB2nr8QryBbEugSTNRTVG3nH8QaInn9e8W0Y5AtfHnHoMn22RETrTJj0f7SPUuHrmLN03ZxCw9z3KD5bGjA737fEuUXh1CK0NAejj4nSEIqGefNi6dRkdS27J4-ZjEaCS6MT67V8pH9Xmtk5XNUsIL1yKTdmUzcPyYUJsyacMxJjHxRtCqore__woNX34snQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXBfn1CLg5xBsWn6hlEcc8sdTEV0sZmiX-XhQlWsyPim49hZ3RoQ5VdfAGwlMin-65Ci76fDc2RQLn_2FfbHFYOaykJ-FobIlmnmgFYVM9QhhhXijF7MN0Vx0hT321fps4HU1305HyB7Jw-mY5red8gyexF0hnYsL_bpmZjRRdAkKNIU2fXrZpGpTQ89v8XclKiJmLy2uVg8YE23K10Mmo-i_I6Q7KDNT-F1qf2vYoabXwtLe68KGoQczUnRf6Fglx74AJ8TonsWnUsczQRJCpvZM-AtMBJbU7v6uNqOo7PgKqUZ9tcY-tJ18WfwXh0fIhy6SyDJVvg_V6sKFJKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeCMp1KmcGY8NcfIV_fK4F5u_r8401-Kk6xZpf_0_zj1FTl7knjKkf_ippvkS2HPHLHoV1_RVBY6o1cEYIS_Tcbf3Bg5Gy5Y42FMhVJYTeJztHzpMeLwDq-MvQe1FhZI_M873VaTlrP-xNdF42EghcpRktMM1apc7U8yKBiuzRcnSFxrHuXfW7lHT_Wdw1E3q1MDZ05JVh8FvuRXpf_pYRrpGyDxptgS1qUHazMxeEGEM634WXdvpZbjqstFd2U7kxrXYSFhlx44EVJyMLEchu758OC2UYScztp9thP_-wrIqACjSO2go-CkSgG94bvOaEYICKUjCB-QRnuibi0QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1BeqBaOZi4K38FRHenY_tVHHseW6PKJS73Yd4mUB3O_gIBnAH3pCJHG5C6Y6dnuEbfTRuRTZPPmi3D8z5i2lWs2cAhkRh_aSKM-QcmU_2MbYYMFYecErjTrtUbwWWJoypvCz4xPVoVeEySyHRGYbuTYLzjCIj9Fk_Nmg49_Jqu-vd5uImnQi7FogNiI8XovghDmv7DpJahOCm01iCE52bVLgHxkOIRuiEzC7n5ovcnxiYs0J_51JKQuUo2aIFGMkTKiUc8hPGivYAKz-COr4JHHbwm18Y7QWroddg-LXldmLZ2qBvxVZEnpFnsOe7Js97Q2WtRUUETao_NPgMoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWnKBYc_pSm0pVR8OS5LZeHmO85X7wg0M1E6DiF8Ndljc8Ur6lXPgNnaVUOilb7a3aN-XC-87eAoA3wDzUOVMmyt-J4f-5O3amiqKl_rwYjwR1WqZeVPtbfZOj0_TAb_qYNifgwkB3y0j-78aKCJbj3hMKT4LMLVwHs8mfM_rkYsFDRhOjrtKHygPpIUgngVO9NY6ykToinPRk0bd9e8QeHdMMWAPCR_DvNDUfWWDVTXwHfYmt7QY9I5Y9ffh2EzqLCzvW1-baQWVzUZelXT2XKamS6GW2w2DEHm89PJTq7oMfGEaCp0W90FNcVhxCmOlWgyxAQSPiSolBd3f0OkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=Cu_Wp_L2Kzhj9PZbez6cAq81m3IqL-82zk-b9c3GOWBeR7wVXDCNedOdaQ__0olroFD2EF4CWVlGFWRs_XMTzsBRUoyxeUc-YMRN_vq8V2aIZ3mu7Ut8u5Gd9EK27pfJxDgQCLMCiHxD6wmGbYDcFl7GlzFpt6aKKDwneBJdRXj31VDp9tS_vuxgnObufX9HP0LEVifQQuV5bT-O3Kepu6etq-5YE093lTrdl2y2odB5IWXkRLUl6EjRm5_xl_1neXs6QBkZUKQOCL0Ya84zi0OYDUR1m-t0KD5xQF7v8VcKdDXiYF3RklNg8e5MNrOfR2Fr9zojSSo1oDp0qB9c_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=Cu_Wp_L2Kzhj9PZbez6cAq81m3IqL-82zk-b9c3GOWBeR7wVXDCNedOdaQ__0olroFD2EF4CWVlGFWRs_XMTzsBRUoyxeUc-YMRN_vq8V2aIZ3mu7Ut8u5Gd9EK27pfJxDgQCLMCiHxD6wmGbYDcFl7GlzFpt6aKKDwneBJdRXj31VDp9tS_vuxgnObufX9HP0LEVifQQuV5bT-O3Kepu6etq-5YE093lTrdl2y2odB5IWXkRLUl6EjRm5_xl_1neXs6QBkZUKQOCL0Ya84zi0OYDUR1m-t0KD5xQF7v8VcKdDXiYF3RklNg8e5MNrOfR2Fr9zojSSo1oDp0qB9c_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHn4qklj-NhSX3PwuYWMn__8U-nundCuQPL5OWA6oadXxB8bSCnGC61wPZK-83At00iH8Y_6iFt6PtVKAZuKRAcYUPYtFDKpr5xoBA8Tndx1crioyUoAGMR1H3QvI6z5LCobQuHW8lTNU2-vaqBYzyv4KUeP8Sro44u_9KEhNVhJMEWj0BR5-p67O9UlpDcgkfv8q3TUeZKCYXx9x3iir0-P1KtcAwc8rFqdt6uyqi_5UeIZbJerbbv8kacKEnHTW1dQrsLFPdk_AL-LA2lxZpvTfNNM59QUZrl53OmYMYCansXt2jiczSJAAQQXPImlcLo8osDaNsPEa8nTY_s4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTTAPPjxRbz-O3UlZ_hkAxAhrbwQ0gR0sKI03iqHxHtdyL9DUgv2kIG-_0DGFyDbBAadoo2c8J_hALm3jqyLxtO7cqHWCNRYK49Hle7QSNgbjs-vav69Mz6TCrmyYYLlSCjBp1Gfk6SeagT7VvnP0kvby_leftVEb0EeNODpwDncDfDLAXzv43D9pYMQMo8TxEu41BlKoLe7G_9u7mml0HE2vlW1AKuHEU0zkMOeq6S5L9YUGRjz4IIZTp5m4XSkis2UHt2gZg_1ll5m5MZGDEO3OTgkn6VWzA6Qq2_8XNfSs5M5vQ_hz44BfCIHMd0XkA9cCe-9jQQy--sFgaXJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUNB287OlyQj2GOMkFhurgQZCPSVZ2nZYwRywODQwQtchiFqqur4wRM1nSzOotOUUmQS5Kx2cALg8k8z1sHoQS_aJ16X8ZeIPdlPZir0ZEqKOBFHbj4weqEmk8mJI4ZReLFnudOW3GNOP1VCGt9AfUFTadODWuLv7tOWwZDLxYiFjGYZMN5bG9QOx6TkabnEGkoPZxCSaBftFZH9WEsHoEYt5GMFMIZlA1WY-FTuIJCi45MipU2TfLTLyjOSRpNND-GvumSSetgRHqQt-ciqvWaUj0N8-hw_e3_PHTDUhn4OaDnLP88tknkhfHXIQF-u2ViKLObjKUlzNfoAPuLymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSSc79XVLYB_D28xYGPUI_91qnCvL3xG7xFiqiqru5E41PZTOFyjmbJMBxn7z6ZYoWrBgNw_d8zI1y5RDsnieubbxxvm_XlkOurxz_looUBvx-Vy3QvysKeF7epr2B0a6_sL2xIvYxG4fgCtGH_50gJovJmx61m2YiKY9OvwK5ep9TgjkSf_6LGsEA_ObT069k0HtPl1gEUC_NFKSZfYgQ4z-tlXnE5CKEu7x1lHit7ngse0mepZpv28lQje6sIsWkQQ62EezprsJaWD6lCy0pzh420J0q5VRxomzvzV6NxCs1pewic4D40QCY8E1T59xlwGPdJL3pGAsZg2YiZ3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc5Q3-HltpAEQN5pO11H_rx6j9LLrSxOsTHgrKUeZSFl3DQGRpSfpXsOrbjk4G9-hvJf3k7UA5-estiWtqEcsihabDlDsqa9OPbIST8qq6XVySZ3pjXQ6D_nWjCEkSpT1Wt-scfiMPMgIHo79NyLLdTd9SqbuXtXZMM9STLnDEwn_nDkbtqzj4PR-1aCBZuFSqpPhHcc37VZcq70i8E4A9c0OADbS7mEaGkh3DiU9q8OcFmrHM33NNllqC8vtLunAG8UalFIogMcelTjpeXpmUhjTi0meOtC11bM7sShmkrHZn7PXhghOuPRQXmk9td04dfpStuMgdLPZn_gaUKNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0oTQZm0Ob_Mp996SKl32PG3vBs5wRj0W_FF2Uun9HXDLQROffBoHzICLgaYuFV9_GgDkSGDuCptrj9-LpxPpBKMK7wRsVZ57x6KS4Pv1AEdDXvjbmZDwSTEX4kjUsdxYSkskYbdHcJUc0ftUiCTySKpiOyTN9CoDerfj38ll6wg6YdLRyMhfWjjtZyLruLZZm_oAsWCXL8RXEMO7QvnjUEdWP2lsGIxuOLMQLBmLb6k40Qr3_3zma_MO_KcLKGGmNwnO_Pc0AVQJkhDz7y8RVPXoIqvbilCbRhO-lK259zPJ_Y5-v4Nk-HgvVnmpd4xI7mU2Bi_5gbBOwhHE03PSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aX89HFgHm8Xu3aqoT4pCzDALp-w373K2eFPLCE4-zYoOgZ7WtQwnvk0Cw8fzQnTDwqdD55Og5wDifHLJ4kF7v7cu3UwqHBIR2SUI6VTaJeFw7ohNt2aC1Zxn-JGS-RoJorYU-UhJUEgZiDPTZhmUurTiiDHoqqFDHZzF-GcU14CNUVLHkoEfN6bKAkNAGZjLgo_DgqUBns3SJFvXTv5tPzJ3WPwTA2JTjvHYEaPKCQw3rSLV9ati9tS-trDuaMbYj3YXgACI_5nSz0HSTbZ8wzzajXj35saErdK6puzcEZeq9xDhhPYKvKPOpogfKOVIol-WgHgCUhdOmqXuMuokzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZLcYR-hN3HYc4oLgelsXlvCsjwyUz7Bb3CeaYDSfmLtcjW5haVUc8Wb0hX4QCchucNQqovKWfGAUzAznWHp0CsRB_V6OQH02SEEL8OHCXxN9uIazZV81ycYkLI2wKjqnkQx5LE8zTZ4Qi_Lny8dng9J7apWNBN_yHI9vNdCvs6j2wZTqCb16tahXohDCVXZqchuOPQjGb2BSIhxIBpU8N4XovkGeri1lTCM8fHBqy6PT9Ng9b4ukWftLg9pkf2nhRxI4zbwQ_2bfN3YBmt8wtgG6vjZUlkHAGa7pzHAtTQezNmKw_kQ1nctqqH3AqZ0KyNMXZ2PjfDHpWHWHa5ruw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttILq7YHHLkU9-aEweaJC97r5vrMc5RjQ7H6ryeaDGJxffUZ7k6r7hWYVnjPNkao00G_899ZJ2RJeBVw-wP_cSHVB0v29aZ5odLGhGwcWJRCV8-zVhbw3H1YR788RPaFzvUsmfptAPzwX2mOBj-oTOAKo9whB9GhmtxYcM_FB4wpQFAMYuGxURcVM6x8bCnteItrl16q639n_bfYI-X8rEpCNACnekv_ZZiPEXFPgUOjSJqWn3QgB862Mxa_Y7BO5YBinKNwcYtATedXwXzLXYima6BTlLJ-jR3yPDslgNEm7kTpnvMecgbnlRSsJIGQc8WcFlvFlAkgpZgxsfFKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKXvr0uKtARpGDmsfckjwq3UXlAj0xBL3Vx1NuLOl6p8Ma3hZcZ0DaKKp-jyoqJCUat3iz0P8inm8u-neOJO4iWppWCFG71EBHuVLs0CxqC15aAH3CCt-iAlWsMyo9eJLCobZ1ihQLmKVcBrFZH303pol0er55XoCxFeB_C35LkUl_5iWUiDJDyFEXF_ty8ZRaRLehh5wnhyL-1F6HU61CTw6B59IW7sKNnF0yM1FrOZPGXxFbzAQRuQAc9sS6IBfYTIV0_qwf2QAU5_AWVR3PNrXnK3jqz_x4RZjdyRt8Ha3drmsgDpREYNTvKZPFoo_XxZPHs3Jx4SirTXGjK3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=ZBC1gcycJ541SDk741q1fMDC02etdRYAGVpuyFPehKeeB-o39VkzTco3Bpo82rncnnzrXg1Buod-KNmO5G6Fj8UkdyNgHyH_JMcAFKxt-3ZB5Ek_wK79LEwIW16A-0ZRYqpcvD_bCZB5-wR68dIBB0MkLg-5gCj6M7oWZ7QbDMwwnXxBjiVzXFgp_N2jLzXMvcivxm6VpTsaYYxUDyS6RNYkDS4xkabPbflNE-hyK28L8kZ-svvzpd6thc1hQVw1qDj8tdtS4v2BfIoiFl6ZW_hHLk3WJUKwKKTH6L6UQi7RxmhXBIs_8gMtiwjFveZ7352SrQf94koWTiZs_Jw5oZlwJFpqlOgACAL8OG87u0Hre_a8Qk7NOBdcDpTRWv58_Gt9ytnvUcLsaw1y2Jpq059t-_dLv4pbXWSSLg4cQF8Tg7GoO-8X98qYCo6YRX6cGXyZXSbAFtWFS5I7qrNhpXCz8IQWmzAwg6cTUDu3YuwgIknhmQKEYo-a1lcjBQC9LMv5UYyK58uDgDylVUDeAAB9yFxYdyAXPOvjtXD3uWdXCHEuQeuG7p3WwvaCVxxo6-Ru1YX_uw-fePRtEil-qTF1OXbRrOsYaHJ9TU4g54xL4BvEq8m9Bm69AfRJ54ZurJ3t8heFlo33pv_0r5mYnOZquCQakpEoQkjylA_v97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=ZBC1gcycJ541SDk741q1fMDC02etdRYAGVpuyFPehKeeB-o39VkzTco3Bpo82rncnnzrXg1Buod-KNmO5G6Fj8UkdyNgHyH_JMcAFKxt-3ZB5Ek_wK79LEwIW16A-0ZRYqpcvD_bCZB5-wR68dIBB0MkLg-5gCj6M7oWZ7QbDMwwnXxBjiVzXFgp_N2jLzXMvcivxm6VpTsaYYxUDyS6RNYkDS4xkabPbflNE-hyK28L8kZ-svvzpd6thc1hQVw1qDj8tdtS4v2BfIoiFl6ZW_hHLk3WJUKwKKTH6L6UQi7RxmhXBIs_8gMtiwjFveZ7352SrQf94koWTiZs_Jw5oZlwJFpqlOgACAL8OG87u0Hre_a8Qk7NOBdcDpTRWv58_Gt9ytnvUcLsaw1y2Jpq059t-_dLv4pbXWSSLg4cQF8Tg7GoO-8X98qYCo6YRX6cGXyZXSbAFtWFS5I7qrNhpXCz8IQWmzAwg6cTUDu3YuwgIknhmQKEYo-a1lcjBQC9LMv5UYyK58uDgDylVUDeAAB9yFxYdyAXPOvjtXD3uWdXCHEuQeuG7p3WwvaCVxxo6-Ru1YX_uw-fePRtEil-qTF1OXbRrOsYaHJ9TU4g54xL4BvEq8m9Bm69AfRJ54ZurJ3t8heFlo33pv_0r5mYnOZquCQakpEoQkjylA_v97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=CMYbcEKbjox5zXaCgPmggZGuGtUaaJv4JEhaSIWS1HYUsDBfb1EP-sjeayR4qh3gp_FGHGslEIAuSKi1QDE6sp_mIN8op1J0LfaNqYbpKzo4n9NDSNZiyGDT5D4iorvtZwccf45rgAX7wFQ8H9daENkwh1cISDeDVhkMrUJZx2ELdxkVlMeuTL-6_XVOV2DYeHWkHIELW0IA6Fyvspo7aB1NCH2URMfsvy08wgXyZrsza4e9Vf1bt0O7JLAmjHET7sUAmoeV0ZjTnZZ_-xaiJCOuSY9_nKfyUvKD3L_WmHH2Xq4QsxYRxCJuJVvE7xYjJ-Flo5nsqgidPlsfLhcDYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=CMYbcEKbjox5zXaCgPmggZGuGtUaaJv4JEhaSIWS1HYUsDBfb1EP-sjeayR4qh3gp_FGHGslEIAuSKi1QDE6sp_mIN8op1J0LfaNqYbpKzo4n9NDSNZiyGDT5D4iorvtZwccf45rgAX7wFQ8H9daENkwh1cISDeDVhkMrUJZx2ELdxkVlMeuTL-6_XVOV2DYeHWkHIELW0IA6Fyvspo7aB1NCH2URMfsvy08wgXyZrsza4e9Vf1bt0O7JLAmjHET7sUAmoeV0ZjTnZZ_-xaiJCOuSY9_nKfyUvKD3L_WmHH2Xq4QsxYRxCJuJVvE7xYjJ-Flo5nsqgidPlsfLhcDYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsR4919cHnwCv7BsALMaFoPN4eVpXCVFiJEcMpjHm76W2QurQx68LegUEwdlgTZ1l-B6orvYAUZp2t0eTpo8wlF8G3vg3-VGDRf19u8XPAcVTq5y8c-op9UvO5iJ4ZHGOmPnqYueC8CswNFrIw3qQBL2QEvpKA9yfuzXSkaD3VD0XsrWd2QnVRTenxqdpsT-NqEF7EeTbPn_Wjv9ReIrFy5bwpxZPQhxCuHEuL5qxZvD4sq7xTGFgq6oQcJ5cRBeh_ELVrmdG2vwGBmczVLv1j_WWkm1rhhAakV9f6qv2V77a27XUIrUz_tKkUjqe5CwhAXV1Svdo_Ba3Na77yYvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbDm5Xg0VXa0_16aTXLQ1QVRn5VZdlKMfgqf2pLBfa8Uxwcc4eqQM3Omz6uKfn0XzD_IsvPsYlpo9ROZwq64GunysQD0dK8BKEiC7C2dvsLCMpLewfeHYvGlz3VgNg8qgUwfpR0qpHnVklbar2gaKC2-42tjgd0PdcRBZITYS75Yt5fZeOodnnOjkSmXF9m1rpz9bMgIXMKZ58YOtpl-kvZfMjEYlgcuDTTnhjwiN0iwJBbioZakZAES4DrYuAE--bUGqN0O4ub6hRzwdPI6dvben1k8QGLtvWs83unyg6bVo1tEv5-tCgKD9tzy1RJbb-YDSpZ_L8xeolu7p40lGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfUWLGy_JvEReYzPsyungxBJh-43Rfmx71Qdc5ee0-m10AYQ1TWIQqQQfcoMbxv98cIrdYCTqXgRaMYHV47KXewG8Vh7iuq_ymRcZ-6yIRTt5nH--xe-9W4siPkBrNhk7lVfHj1ZtFax9MfFYpmf8TixEb3QIlEgOyJSzJ6TU5OUNJuaIJnZ-Z924HUjmFC1rASn-21l3jHj1vru9WdV7JJ9kJ6wVC6qGwjyt5LSN2JUUkOzp_UNMmZ1paME6_tF5Cg57r8vOTK2zw3cImOU3lx6igzXLgS1T8cQRO-TCa_NsWgplKD1wR5XhbQCYmNk0NYwPzwzhWKVxfxRwiHNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0okK-u_mTjyXob7wOhsFIn4d0ue9eh-ISAjyJ42Pvh9Ogd5Ldi_h--YidArsGr1bNtehxRddwkZG1OxlmCd3gB4yKsW5Xo0gv7oRJEXOI_PdSjUuzFh91tOqpT3kVhf-NmBRW6QUpPMKoCBTWaiobBvXXvwLb1Ea787S_qbsKNK7pKj6iitkX1YbxKG2oYnwsUBqq6aG4sOWuJR8dtmXA8XzBLRVV2cI4sUGNdxuSP-z-NtltPyPI6YgXqqmSZ9sUZLRt9rFJXXvVwAQNdBII-YY6AHU4PqnKa0XXwBDMLqF6j_IIYmjaFPMEk7N-lAz7KtBlx6xGjFTFEUpP-7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=r9vew68ZfBZOl5YY1bPnBcXx4hf_BizuG-CGdlQdbtguGt0ercXqEt16XWbpH4vsGusfnZiOpXI_BHc7W-Aw0Qo_eSwBcWlEqLklLj_84SxD7EX67rE96C21EP1FEyqfoxvsDF1xNZywIkQS7YZlCFOouwrcaFyBZa-kI4o4R-MjEJTr5r6RU3d9RYIPfkPl2kmKP8VtspCf1Foj26-9rk8e_l_zWwMfaUD3b0tO2cHDGUk4uwNBedMDBJ3tVhRUDd30l6Sx_ec0KJn_TqWTf55ZHCfBE885ay1EOzZDqNM6nJS658L5r3pOxw7zjjpT4QTvaQbg_URHDO7JbQidwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=r9vew68ZfBZOl5YY1bPnBcXx4hf_BizuG-CGdlQdbtguGt0ercXqEt16XWbpH4vsGusfnZiOpXI_BHc7W-Aw0Qo_eSwBcWlEqLklLj_84SxD7EX67rE96C21EP1FEyqfoxvsDF1xNZywIkQS7YZlCFOouwrcaFyBZa-kI4o4R-MjEJTr5r6RU3d9RYIPfkPl2kmKP8VtspCf1Foj26-9rk8e_l_zWwMfaUD3b0tO2cHDGUk4uwNBedMDBJ3tVhRUDd30l6Sx_ec0KJn_TqWTf55ZHCfBE885ay1EOzZDqNM6nJS658L5r3pOxw7zjjpT4QTvaQbg_URHDO7JbQidwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=HtsAPEz9OtT0QM_pGEAM6U81LwkeTdPOeyy280XoxXjOxgMNa7Ub5bKVIDZj-kGkbKv_Eq6tBNv2oUj0bN41tdR81DcPceXpEj-WYlzcv-ee6if_A8TMqswXGzD0KOazIH35wsbElcYcrdqJM_NAFbGsB-yOSxVCcoCe4e3eBq2PbAui0pZwWJM0umCcyWb5EXdlfjumybmOUwCxPYA7ClT2-FrEbuUm48Zjc0x6mPk-5d4LhpXoz2BPyQprGsQ0e-IBqhxojl9VzVxkMqmoiIWC_GS_WxfgUqk2XmovO_olfu-HHCPg1pnq07KaJdqhFGUEME34FmKIDXvBddNtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=HtsAPEz9OtT0QM_pGEAM6U81LwkeTdPOeyy280XoxXjOxgMNa7Ub5bKVIDZj-kGkbKv_Eq6tBNv2oUj0bN41tdR81DcPceXpEj-WYlzcv-ee6if_A8TMqswXGzD0KOazIH35wsbElcYcrdqJM_NAFbGsB-yOSxVCcoCe4e3eBq2PbAui0pZwWJM0umCcyWb5EXdlfjumybmOUwCxPYA7ClT2-FrEbuUm48Zjc0x6mPk-5d4LhpXoz2BPyQprGsQ0e-IBqhxojl9VzVxkMqmoiIWC_GS_WxfgUqk2XmovO_olfu-HHCPg1pnq07KaJdqhFGUEME34FmKIDXvBddNtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJoYP-qlPwOLqYOSYRaTu3ZTlOrKXM4l-RMc_14CVu6af3sdsBsJqxwvipgcitYTk_9F4zd2ljLXTTGtw6hhNl3TNI_Ygk_nkRbsn4nbLA6Xxev-ywG3AOUb1FO16NETFADvwRO-Ec8SAB2EAPM_oQXV0YVQIQxDIOdYQ7ifPyCvxuAP2XPgmH8XGCfnSXwNWg525GURXPvRIeKW8DAKyh0UGAm-gkBF_yeoqSamgzl-dBEn5axsdIPz2oBPZmheZ_I0apeT99vybnB2beHTdWX_u-ms_D2WzCHTxcFtOicMev-orlslbw62MxX0St-hqFz0gcH7yHXYKlemBEl9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdEC5PdKuoiS82oxWbglRCtua8rrbDtEttpZHHzNO6G9TliJWRcJwvESCNxBEPpI7bgyGPhh36nSXOJRT_wLuE1WVFAG8wn2OIvVI6UlJDbu14YQPQOlUPpIavy3QaDarQNlWIVBTc7p6bxDzL5c8LA5PnM2hNDyzgeBoF5_-KhPchuaUsNbaL7ijMAwhgeJCOa4xKcReRCHLMDbnPPWq7vt097G518czEZRacu75J9rqd8GYwWyukTHNM8UYCtV5XaBTb5iaGngJqzVfqGE469fpM1jxORxnc8iSv-UW9ca2nkLOxqBTaWC7j405vy2PTBheiy-0oB9CcmCxkzsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=RLUYqSAgtpQm2Y_u4vqstp9v7-ZgkksFbjeFIggrkCsQ3MLEZyWFUpQuNQl1HrLYFjBzZs9hJnxwR0VAhCjq5CWH9zSn3ij7EhULu1sRTjHggzkQM2gdrXqyIrHVsRP3BSftFgQBp-VTavAgJIOpdbD9CAfDs5EVbB0Vp-NoGPvhLXsSzkcapPisY5yw5ukf2ukHrCD-gGfuoqkTlIJxYbiTyJlW7xj2EUL7z_6lWcamIHibfO-bFTNNAvQYWFYD-Dt0FUYyZVf47vVuCzARgmlcK-naXnW9gLoIYHikfNemXD5n4tqKqfxl5FDwng7V7CznQkOEG-1J2qZQ6yzOOotgfJL1aLrPGJ-nAQsBAKgyxdot7Lc2lmCDuQ13OmWFh1KfauRU2PqDRlqAXHHIzaFJ9q6_6RjWiu5dbICxFQd8Qj53VAAmO_gr_3OmmPLHTufhGkmkrHS5Wm651L3jgIN2xfdhiFPO2LvsJYwrCS9fDtP692hVlwSh0B9C013G86zRFUGJase0PqGQGExZM1ImBTsAcDQ4-UIB-ai8F5IkwxM9fDDvJf67grAGP4AE1PWjCaT6Xd59WilryNDnkRhw_3gd9IiYXS-Wku42tI_XnYGoMaESInAFSwgeFUx5Ekt5zgDm-zZYwFzUa4wNo-3LoK8QNK1t7YSakMVTjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=RLUYqSAgtpQm2Y_u4vqstp9v7-ZgkksFbjeFIggrkCsQ3MLEZyWFUpQuNQl1HrLYFjBzZs9hJnxwR0VAhCjq5CWH9zSn3ij7EhULu1sRTjHggzkQM2gdrXqyIrHVsRP3BSftFgQBp-VTavAgJIOpdbD9CAfDs5EVbB0Vp-NoGPvhLXsSzkcapPisY5yw5ukf2ukHrCD-gGfuoqkTlIJxYbiTyJlW7xj2EUL7z_6lWcamIHibfO-bFTNNAvQYWFYD-Dt0FUYyZVf47vVuCzARgmlcK-naXnW9gLoIYHikfNemXD5n4tqKqfxl5FDwng7V7CznQkOEG-1J2qZQ6yzOOotgfJL1aLrPGJ-nAQsBAKgyxdot7Lc2lmCDuQ13OmWFh1KfauRU2PqDRlqAXHHIzaFJ9q6_6RjWiu5dbICxFQd8Qj53VAAmO_gr_3OmmPLHTufhGkmkrHS5Wm651L3jgIN2xfdhiFPO2LvsJYwrCS9fDtP692hVlwSh0B9C013G86zRFUGJase0PqGQGExZM1ImBTsAcDQ4-UIB-ai8F5IkwxM9fDDvJf67grAGP4AE1PWjCaT6Xd59WilryNDnkRhw_3gd9IiYXS-Wku42tI_XnYGoMaESInAFSwgeFUx5Ekt5zgDm-zZYwFzUa4wNo-3LoK8QNK1t7YSakMVTjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=cfMxA73vVdCxQBKl1a_3yHVpg3zUqbcLyxxtSNcrKYcSJuEOfnTFYCrUIR2VOmxXWvr5jpktFB7S-W9lX8fhbISo0BSxN4nBChzegPfKTWUmmZS3qnToME6WyS8ZQgANGxetpkaLJxJ55iE0PSScZo6LPIgqC4_ZTJc-2j5wcYkFflkvJy-MZxKdWoZg3SPp8P6eihY8xpove_8EUGjj5jlKoUM6bVLcCx13ebvB3t6LZbv1mINbE1_sjQ1zA16NsSHSBvNVZk26M0iKG5ViaG7eS8xt3dw6e3u9AfxCUF2DD811pb33bA0MopG_JzIq9N15MEjqxxc15GH8__U_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=cfMxA73vVdCxQBKl1a_3yHVpg3zUqbcLyxxtSNcrKYcSJuEOfnTFYCrUIR2VOmxXWvr5jpktFB7S-W9lX8fhbISo0BSxN4nBChzegPfKTWUmmZS3qnToME6WyS8ZQgANGxetpkaLJxJ55iE0PSScZo6LPIgqC4_ZTJc-2j5wcYkFflkvJy-MZxKdWoZg3SPp8P6eihY8xpove_8EUGjj5jlKoUM6bVLcCx13ebvB3t6LZbv1mINbE1_sjQ1zA16NsSHSBvNVZk26M0iKG5ViaG7eS8xt3dw6e3u9AfxCUF2DD811pb33bA0MopG_JzIq9N15MEjqxxc15GH8__U_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCf5_73-luRQxYfihC0Dv7ZRDFRTwSRNenhbuvjz5OesH3Tlqa78cqnfMH5gD5MMFwcq-0oYca5366yzktfZ6bPOwe8P9tszJYbEHBgI05bexBZ6JNpwplql84j_1bKSogsnx0wSxWKeE0kj0v6cGGpA5hS47lT_2ArSx1yVBnxZB9jQ1ia_I3IGs2LDi_Xngipg7NSWQSLUdWEfB6PYleDlNcm9U3fnE_p83D6fKl4KYLxlU2wWPKyiCSKd0A_f20vFM-uUFoUXSfJMckExo61d_aYb_sK9OB5FCs5T26_pGMcT5fSKBdYlWBzg11TDef2GOAdlkTfHmX2MLlVXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=VHVMREG-eWXHUvRWxZW9dKJq13veDihYNOUxANig8CTSMl7ccNBr_fsTlY4kLY6AWGuK8Y3jz1xVpLnYojcIGoTSsxCtE41JRj4xYCVr95hUhxddnyg-oNsHKLvaOoinUmfMAqIayEqDiTrhnog94qJGeYp14rWbw1XWpYsXTctGtUd-6zNcQeXYmWUbadfwDU-2966eXG63ODtnDOo8veLMvMx8g49Hi5e5iG88DiyAbXw29LF37o570I-0kG8bbPsfEH3YcLNMh1KwV3xyjrJ8YBG_t7n80ic7zzCN4JYZBiHJf76_ATiYbVPTyYHkcu4GUudUxd5QQ2GYq4pDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=VHVMREG-eWXHUvRWxZW9dKJq13veDihYNOUxANig8CTSMl7ccNBr_fsTlY4kLY6AWGuK8Y3jz1xVpLnYojcIGoTSsxCtE41JRj4xYCVr95hUhxddnyg-oNsHKLvaOoinUmfMAqIayEqDiTrhnog94qJGeYp14rWbw1XWpYsXTctGtUd-6zNcQeXYmWUbadfwDU-2966eXG63ODtnDOo8veLMvMx8g49Hi5e5iG88DiyAbXw29LF37o570I-0kG8bbPsfEH3YcLNMh1KwV3xyjrJ8YBG_t7n80ic7zzCN4JYZBiHJf76_ATiYbVPTyYHkcu4GUudUxd5QQ2GYq4pDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDcReFWmqzOUiduaRPP54o9FWBpcdyUxI4HMGO9tWfCr9u5qjLXnBZLc_eW13OXvnsDl2NXpOlpF-DnJSjrDmPWLvKmfu5WV-wORm3wo3q-p4E5DxxfdX6VQZdn5UOccmYVPvMqGrS2ntB7np6isEoMlTsgrx7y_9FOCdhGnQW5o1aa5-2_wJlrdm6I29zQljX3URYeovXUh0JhBtK_0scMPifgY-lIkgM4nQWvHC_NNWdRgZQxDs--Sfcaww4wz5SJ7bCarjyceHhzooIsmeH8fi6dhMGlGlzuQW1o0ShW-QUBilqArNv-8Sv0z-AkjGZRpBwphoKaTmSMk_M0mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke-P6aj7grHKOOK1JponKilcrbcdGrag6gUx9eglKWTfw0KJz65DZTt1sXXRR-irOytbZAzK8nntrvoJZ9IJUrfI9QOF9qSpANR0O_NUyno0crmkYuYZSNG41KLHKT9JRKcltwpbXWLsx28COqT00HeZBiemhtveuxLYVTZ2vq0UyFplkzQCmNBpv6Y7upZiz2hGMa-xLxCL5KEmdTAM1P-6R4zI5cKgwjk-hBq5Q68fs9nCbdVrnw3ZF0AWRKNtJ_WJfb-zOk2k6BK920FGzD4Z-PfaM1rw6RZnz_244xU0lT23RkT-lDmmZ-kYawTIBJYCtpCHO1Pq9R3qM_GRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z44UusXRfYmNBYePQuZAFwwA_3jDrPqjXsA4-7nAM4FRn38gjhr-03YTQ9aLQez1HaBdmoyPAsWyT10_oAZlvsut5RZRHCwLneM8ZlOPNdN9V0WFpYKJOXQrQATMUqU5E3RsH3KMhUg1C7gDiVYUUFweuKiaQllrwWY_BbhqVz0RcvH0INEXYu4a_1A_x65x9bYdwBumV5Jo6YdZ0ZBEK2lz6MHg009xgSgvY5vpxFqk5V2QFizQn6j2Tjb3SJ9hO1KLIymUliceDFuxjHWuuygQ7n_XnOI7ZwruMijQGuJ5dTjO7jEgFlqIlPgo7h8xDp3U-4SM02kxDAhvHl4dkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmRAyo3M9hkpy57IsFesz1ZlpDyoHk-tCso_R-uta75Ct11Jy0bOZ7i9r1e5ZzWse27knvX74mfyCJsicKWxX0uGtL9FWMdpzEPR80uyjR2HcfCFhr55Xav5Y-IAnwvcKhKa8E_8y9U5vYo05HywVTLLpckpc7dshZYjtQK7yDalX3UbP26Ryzw4PBmzGeQD9wCCgW37aKCEBsRRAyQ_H96pUpef1FGQpuf6ElG38vExRP4M3O1BAPUjVmGdXjl3byHIXyTFQ4hxwBDayzbKmx2K20Upa1wxugCxts0tG8eJw2OhJ3tJPCeeTg4ktd4znDNpNSH6hl4tdYn79S-ICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_B_IjvrcPomYmCXN2nEJcL9IzOp76N0LIYK7I0A6w5oK--3nUWMiiCrQBBS61NgNqLn9bOk-P7J1QgM9zys6pabJSEkYD-CCAYCe4uFQC74yqL43P2OI7-oWFv1YZr66U4JNBBqCvwaXCDSCxxeppXrdvesbKvWICmunka5nXI-5GXx-4roF_bgzNdsCe6WUgX9s57LogL5iBNSI11ql-INSRUR1SwDZ6Trm8_gJyKFi3Sss8zT55WpTuyFEG8pwAbXutXW8PFyyauGSON_92S9AdVbDzE2--lwgvmxxovjFs2Wx9ljXrpAhTa20dclwnQu9l9azonV2QwpLSAsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHb1zMvMB9xVZ5kCA1Ejobh5APEBgv5R8TS2TXtRCNPKBq3OIlomyeHQeGm0FceSEiYZn6TNLa4eDFeGWLSNQkLFiCcLobS2NKwTAA7DZfG99yl6N688IXQoxGoz6PECefZcD2Lg85nKW3AXyJ2Lp0fItAdjBsPYVBNuqWONl1VgA-M_U09Gkjm8ATYni4JwY-41FWc0ZtWmO_9sjEiavG_4b8Wn4RTtGUPmeEahRjevAo_xFG8hxZWg08cUjW2SbEgzFdJ1r280vZnxZIIw6oNS5JMlO9_d15wuNykRibuHko-uRmQHAdsQpnwfsMcZaYqdRE8lj8-3JEXPI5q47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQhKgqEQQWdQq0fvQ2rfPkAKBdKPIQt_haK0ZqgVIcDkYA0xU_PcZ-BM5tyV1nN0qu5STJQYwWOHN8q8C4NL3WqZjEjZjxSPCqF_LQPA_RCN7hbsmQBbL3RZdSg6Q-G8UWqPKvq25y6JIJWCsuMYyok-P07FxcTbM4Pal2HbL1V_PqR8rXz8Oca6C8aliQOLSUqwtJwFWFt4e3h7WZfXZoI8QPos1T1iXYWNPE9JcqtNM6Q0frw_vZzNfub4eaOUETBwp-driLO55g6-6XBKbt3RiSnvf73pdorcSOBpQ_0iJnYruIqNzeRqUk81gm3_5bwnqwyb7SQw8aV69hjxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSWrDrsafmMHxp2Qd8tsSjCkmsBmhSMJYp9UaXVj3eCdSUitU4HVDVwZobEsZYggxJbAut-YROVWYhs4VtZpKiF3lcB7xuaJmFJON2VHtRbfMpoa7kxWu15MLYTXfK0cOzlZo6vi_HC7n4vLmvqYzuin5kZ61up3Mn07GxuWgmfktKn00iCHjgD12OYp50TPtxJyAprBU01UX3XDvuSFq60JR3nM3ZijxKKCPM0p-NBT95dzn-JWLjB8KR_ejc3X-srINaIsuZb9ZLaG6rP11VQ2jMtL27J-dzlr-KeLBEnnZnbefWRJkSu6mQmzBlHOJcvH5zeTjltU9cFGJEfUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDwfywvuyiNmb-UXff4707uAit4LNJm0Rhga-VYAtRo_XaBHHzbkIQlukNgZCTkksKUk0kIMVN-iywum8AA7gRXrEXjJbk2wqZ8kXrtlRapjcQ8T1xMMCs7ySo4VW_KKVKbqkheIzno2NB8Jo-OqG4bS570Vcw_wVR8LaD4QL80HimlfWVJmC7sV4dZ5Jr9geUaMHyH8EYagzevAjv0irApFppUeUbmwRITdDdAHqlySiyfKzw8PcL2epRo5tVIlUrSZsYKV_16_OOK06KRlvCHAudEcDqgXJ2bjW4To9hn25c6Mrrm_adU1mNJT94sFn6zNN9DKFfoHj0vJ6VZrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTWDplVmwY8xg4SeiRzLYCDgs7EDmaSpftmKuDC-07pQSoIhyWgidakFU-jGTY6rJ3qpw8GbBCbqZNmzVMpZxKAMOIoeXW-sn9pLJrRrOurLDhIuefdRRHPDAYscMEnS8Dkofse1nksmBURGuH9Iqz4wWyYTP-jJXhfu5windVd4PpaQzBzx-ztcKzJEm3Daic6wU8HjKCT5X9rXlobS6nEmgcKFD2C7YOMgWrZf-szcdyuierAr7BSeWNgw9p8Y-6hhLIQL2VgAWSyi_Vl69c63c7x_gEExunr04rB-Ybn_ceIF4FgWMgaO2KaFF0qEeBmnTi7AIE8yvugjSPS31A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeMZHAllRU7PBQYx1oGCgkgaP1b_JIiY364FMt8HQ-9PvqOtxYt0oYUpRutrESFX_YBYEzszcz_Lte-lsSUBsiNbdX9rBhdLRq_6iIth5lJVsnJ4jELgPIGvhl9SBRnBaIAA30ystdTi1vhk2yj7sWhYRoehN5Hnvt3mircGtr84v-LY36-PMbzf7d8LGfLReEEErI7Hvjo70oraY2AbZwTszqs-VtZPZBFHFhkhhDxdUBbr2XdBm55iJcz7r3dFiwIgRAXL48Nxh1xl2rNlH0iDR3RcYNQsS8EK_EA2nXMMv9SRVxWKBaNIJSe6KKas9i3WvYgagM3gCskfbkS_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP9eX0FMG0LuOPZhr13PRYvgagbhd82hmN06PJHHbBK1BJJ8TvPEssMNxEcMKFJCQPIus-0tMYLsRkMphis6UDVlveNMYOcob4TizPU12naa1SOihaJwCfuX7w3-zbXFMk1lEOOZ4zUm_7Goe4tBfhBascbwtKAjqD74QaCLEwJtmXs0iz_FtBxFxtuWxYPh43p_kVjRFFBtLCT9qrS0PwLNbpKdWGL7W92YzMRS_kMWkz_OkZoghCLSu4YmmVBklHY_8aCl5FweFyjc0KmRUbH8GPRPtzIsbV0RZRvg2PnS9OSL3GVraLS39hFvT51OWcmpu9EPUxeEP0Nldv-igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTSSgcIm3IcZbB80-GNW2M5Rt6Pjsl3WxMwPQz0NAKNLe3R0AZ0QQO3nPEJxtjMgd13PrVRvMGrkVg9M8HCpUPw4fYpXyxm_A4QAD_GNCliV25s6x2W4pSBzpOdKoTnAKxXKJ2bAt9Jf7TMWhDMjhfLKBtkUb-yIBvRAYsd2VqoLWJ3d-wPdMV0_qlAaH6YGwhHmtk48r5ZefKX_Nasx6DvlQATWnib5hxzLWBqE56TPpD2GxbceX5AcGZ9dwUqHz8YWUAvQ9VKsoplbvF0vaVmkMm2THJQHXNFCOcSfNHmF-obtR3KnY7SvasE_XbJ9WFme9hftKEIeHxhDPGQy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvemY2Yw5g4mrNgRJiwpyS0PiaJFLOqJyhNt-q-lA3cBHM0ZRQBgj2PmGvN82SiBiHPqkjxyOfsYnHeG4mBN3Kz7X-OHYRVya_P7BY40Aiwxzqx68YQcnetWimAcM-Y23oHY5dFfVh9CGlPGoO6t_PKSChwVcgZvWjd6T-XSLwPvMxUAhHkNGyccIFMmuMcFVzPZ8r96hj8R-RsrdgUurzXMqQ_JxzbblMyE0jVlT3zqCWxAhnFdCjuaLT2QqrAxIbEmsfibOLUdX-gLRJb2tciXSVDGFVkEPWiXC7y5DbOkpElnECcGSvyEki9Al9a10QcBVlwUmjVWfMb99VZCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVz7FEJlqKgF5T7IcyE_BPye7I00As1p0IEyROLsxfW4zEEzMmWp2F3-FLLwTE_0q9dhtnRsbyB9VE3C2-NiQEdUGZq8ht_m340pLMWaeEOWhXztZQV3oUHfLOLyvA6GLxHN8-CjTTZmehiVlN4gB3su3JQDXCQWehYFR3cS_Xq6GZJcfC3XiLRQwBTl5iF6eUzryLFHABXhDnhhXfgEGVtJ5JBFOHeNh1l-Ji2JklHG2aU2tlJB70jcV1hC6SVLUfLZuVrOBUGGWk3DCYMQIQXYITbVt_9R6PaUd-Svy6yZiESDtgJmJ6wTT_7W983fRP3LvwgOHf2i_uxeABbcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S35ZfgAlx7oWZTdinxQEDyvXRSPQ_vJ756yXjBJDHpxbzpgwxV1bIiEhcClMPjL-Wu9lGz3d50B4DGurUZzdntqp9mU3NuA1QAXt8V5YlGyMYc1x3Befit2PldXYw-LSqm9Ity3Xkdg-cjGzgvG3Q4LgRtqSCOxV8Prk1gz-X5TIwQ-JWwS5nYc1dnQFDFFeWiZYYeVdKOT6OwFKolWfZrKGf2Vz-N-zzKlqdtSzG1V7YrqmBu6cgKTfPxLOEAgf00KrPwYhBeGrhg6P1Xsvq-0Y2R2ivUNx8MvQMaBTI6N0Y4x4_Mevxxy0XYLMMiJ9peX_RI-sbOwd-lVt2OIdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxTUBupdXjLkt_p4RVeoqSII87Eg9LvoFeRHPLE0ulug-Z1YAOtIPGCL4VLuuc7wKRl6Ab62MK3w4zJ1YVwuoeT2NzoVB3Fm6GVO29fwF-yezolXvxeFPrMDUay26WNW1B3rNEs3i94AhLQyge0g1CAk-O3TmM6Gzz8MatYkw6NyqTeV6IcVx8-y-fHcYdf0MTHQRXAmqNBdynrFo9k_LPoFHBkXuL_PH7q56H5MHiSUfMdJCzZ8TEEa0kB434a6S4C0KGPA5X7nVDajmYKzViQeUeG5khZBG6IvrJotb_qOzk4TxJAhAh41yAlz3bCMUw67eAWDfYporQGJ7JhpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQAyN69YsnWb-ecEO06ckdWTQ9WwyWBiAIJYVLBCDpgc0SGOM-qdk-taFBy5P7kdJbGAyq-rLigzI_V2OwNkndpQGshU5f53eY7OMfE21lQtJunAtrz5h8y-AQZmlyoFnLLVxEEIJa88cYlhr0C3I1wUG0CBKKMkXQVfajYaEfoEMiWfKMxPrI7p19CEwSzIXU7jRnSShB76zpb3-nTJQjifodCsl0GANeQCaQLPHUIkyEXDVlUJAIoO8afYusOl2Zo0-Tac68mr8Gc09ZAd7d6ZQwc684ezcWDMu79m3XpEFQCE46aZdo1qzB999n1X2FDTCqzIpqcaIQVEABnLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKDLKamfDVUDVWtyCJ5LjfC1ANdHjGqgZGa9mKhxaxyZfbg0EPkBWddeGKTLsbDjfaCsG8cW6df8_Sowresx7HjiSD2i1ViBa7CJ621tw1B-Ngysp1Z6UUy57dXf0A_0ELNHK05dEkzqaolFGObNaJ2SwCniDQ8hba4RvYkcIO8pDsuARBfkJx3p63pHC1TWcHFm2MUezwldwYhekK1NbeWSywGbhtk0LI3bHCxazDQBR-_p7aXBrtDLO11SEEPd5fl6bv2x0UahCwMEpdxSW1BwlRdtR_8GHhz1AQoQgdP7vBAgzLTel-GufWUa6p69X6kx0cgTbMcRQQhQ3f8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0lbFQI-J4XEFn8PwOOqZh4ZnakaQAn8pAzzQ9yZ9Vb4sScvd6kPlyLLR8h04M-Z9qGahWlPa8QAht4EpyIjRyaH6ghiPE3f0ZCOntl0ovOlt8H3KvKIs-vDGa06-bl2ONBYavouCqNtc5N4h4xKeCHyXKBSrMC8_Aqv7cUSQCsy4TouF-tbnWeuFev_NlJh98-5QRw3WxwFMtbisymS26tufM0lx6SQtntnRPI336VJQ2c8kqy4W8ktSYQmBZs6cSrhwGQ_ZOlahc7CUAbPzvFNBDBqLySnxgPxEuvogJJOOKzSP9WWn2j7YyK5oEwil1sXZ9GsTbwJro1YVxQWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=IQZIodCf7Fr_Q48s_Zty_MzHYOgoi3dtK7JiRYch58ep5HszIWYHJ0-0jTYak_aN5iABw2R5mDMRmXvm88KaN35yqzn5wOdOUvhtPNfw_8HufjRJuLmFxYXuosSJftQBRF_DCR4CxkzaUhdOtFgmE9io9m7PrFYm8MoYtsbEbgr4CTTquggQO2ztS2cIwp4Okd_c1xqzSHN01LwODPz2i8OLLnqTsfIHgPN6ospzvWkzXEIoA6h2t5dKB-nX9uHSVODC3ttOVYRlSyc6nV8Qw6pGXRhKVf0xxjFZPWKEOaTBc_ptxDXXpXl6GSiHKjdVIkwLc1gaqiLrkMPBOEN8RBdT5IZ0plmSDLVyQvtZ75GjaSZkAjnWGTb-lNniKaFqGSjShHRu4JSYhm75LO-9K5-srX3VCT2ZWQCl817kgbR6442fSbe4yEK7I4e7hqVneS64G2Hs_PfboQM93b7Cs1lYjDCx-zksHIQIiCZ8YLz69fNBDMudfD0cRsH7wrfY7Ppe85vpuBhPJBuJgcUpTj8VwrWplnql_k8IZU8LTDCuP0i9dZe_FZnPqKqNnqFfSyMa_XLvfGTQheZ6VidWWx_Jtpzf7IFH2p9RK6g-uDyJryzURLpnkO-HyAKbYD4rZo1iuANDV4VeJ9YJtsd3QWAuaNDB92ozQcAU2TPtYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=IQZIodCf7Fr_Q48s_Zty_MzHYOgoi3dtK7JiRYch58ep5HszIWYHJ0-0jTYak_aN5iABw2R5mDMRmXvm88KaN35yqzn5wOdOUvhtPNfw_8HufjRJuLmFxYXuosSJftQBRF_DCR4CxkzaUhdOtFgmE9io9m7PrFYm8MoYtsbEbgr4CTTquggQO2ztS2cIwp4Okd_c1xqzSHN01LwODPz2i8OLLnqTsfIHgPN6ospzvWkzXEIoA6h2t5dKB-nX9uHSVODC3ttOVYRlSyc6nV8Qw6pGXRhKVf0xxjFZPWKEOaTBc_ptxDXXpXl6GSiHKjdVIkwLc1gaqiLrkMPBOEN8RBdT5IZ0plmSDLVyQvtZ75GjaSZkAjnWGTb-lNniKaFqGSjShHRu4JSYhm75LO-9K5-srX3VCT2ZWQCl817kgbR6442fSbe4yEK7I4e7hqVneS64G2Hs_PfboQM93b7Cs1lYjDCx-zksHIQIiCZ8YLz69fNBDMudfD0cRsH7wrfY7Ppe85vpuBhPJBuJgcUpTj8VwrWplnql_k8IZU8LTDCuP0i9dZe_FZnPqKqNnqFfSyMa_XLvfGTQheZ6VidWWx_Jtpzf7IFH2p9RK6g-uDyJryzURLpnkO-HyAKbYD4rZo1iuANDV4VeJ9YJtsd3QWAuaNDB92ozQcAU2TPtYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI2LNb1QgrWB-6fFj3kfVUxIssIXdglbA4_e2I3sUbvO-J0gi3cZHApSgde6iUpoV37QB1IJKGZzCUI2cNXCF8e5u4a219RU-iu5YdaeJlP5o63KtLCgUeMXYTaICgBBOTcWIlM5xJcP88YZgtnHJB4fmjs44yoZ83mu6ouWawWYsxMoVsyDjv8TGQKUCIHlxAPoAILRKjAUHcvDxgaZC636-m8jWr4zHn8lqw95Mayq_8CmPluv1J7mvcfeCKlhVQGd7w05ujMNNfnT3nGcuPrTx53WQMiGPP8ruCOrC7jX4yzRC1boatzMfmsAAffPuaWGnJGk73uJWFkbIFfBXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uwgyf-Pt4XbBHjOu3msRuXa6Scvyq1tIU4f6MMhxQDCcNp5lhL6SCWJeIQ3s5-lZc463qNT82fh7d4G5AnrBGCUYktKaIflxdy7p7JF2at24JbfbRcVeKorIdjjsO9P-COB2RjqkKQtAQuujzI2lcxqnV4PNpwhPXVKZnySK6obcdoSIS8hIdYbMSAIpTStDkdJVWFM11H81SYWGwTH7lLPF0T4bu0N04IU-ws5zCT11j2BNfR2zCYlBk0DoCQFdj1WnIYFjcb3zqFE5nxxKwXFNXtDmynVGcOZfXh1r6l348Z1Kx8pA2QVdv71CPstiFjoIA6FV7OuY8OkzcBNbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZqLt13nOPfwMQjnoY5eBmRBUXqGruF7uyP1euv7oBWcSIDjVifxaG9oMRmhBl8vqsjLWrH1iCQoF8bikvcQDVEg1pr92vvb-NFzWnj7aAGp8iG3xAmzk0Of-aCLjFXQ4sZuu3LwwIJPmOsntaYqfDA97td8wVudv8SEltiKw631mfTEtdzlDKQSMEe8c0hWnY2ZdxDlknA-vNV0QwIt9Rq0IUlrSFSen__JgCHf5psS0xcNjJtzRqZSxJJB7KIKPMsJfTgMdVdrJYcBcMwm568O_nFQbOK0LoWK0_9Bi2fPYWxVtjWEf6DZ14hzruuME-WwaNEY7Ijk3XyHasBUyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asbjauhhBGW2L24XJrbHHwvJnGR5-z0h8-vw9DNeUnU5E3JhghtGxc9c59mAy7l_OVIjJgNh5NOrkOxQEIQmZrnODEDlc1IxOxAJZIAjVb4Y3kVAQenVAAmdAMTr-M16pKPM1zqrXpLnIPpKSF_r-AXxK14k31PPvy32Y3IovUR6TbS2XhsrC8gQZeVHh4Y7u5bqE26RrkKN7i72HAFow_L-zZxfO1P-zWkFNox-tj85p77pednBKT0QODFF88SFmy8RF78Cn0WP8OZSzSZLp4BGlOL6U4awM8WjvG_1nCu-wirqRh2gtxIp_B892UmDVS3rcHWOaZJn-MYcP6BX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ESsr4xqyJzH7nkuOXDvHDVzVz3sTVuKPqn6X41oBppblPK72R0N1BnNPbVUsMe2BK2BS660g6qXNp3JOO1TrgyUpTfg3uO9eO1oeRrG6gTiaob5ruzi8N7dAALyFSam0ARqUUsAMljJGx5jaOKUW1zdvok1oP90RebUDkWCXpn2M2JuM2nq165RDiIpWQuCBWH9a8BnEZTVUQcMJnu8dZ6MwxF0A3IavmbceoIFkNBM97lGEf4ZMvy94ssf2FyeEEeRd5fM1N3lmGi2u-8cGi17eckVbGJsh6VNKc5_JlXeoHYOUEIF5HZjHsweLkeS8dynXaQ1nTWTd__OqVLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=gJA2z5x6_KNfVD7ueEidmifBdr_meo20S12s4MK3ztJX_0G46r5k16_fwjt6WLRpLkd9vhn4biwUOshEqGKjPtGHmf4uGcIQlvebBjmPKpZ9tVbg-VL2vpVNS90BbyznMoG7A8eE33fBiEnBPHpwIb38-jlkX9jlUAeQS3fPshSRj9k0-6fl0aLARZSBiLZbUfxwFNh82XWjVjiKbqj_wNPBhK_oMuJbmgSFlQl4b599EAoRYgAjm_5Qze82SCpZogDhKeys92tDoTr5oMarko2dgWe9qxzxUrAF0l5rOw_Jv73fbubO-Nb4puYsoobP_YOyVomRPbrYVosIbVQBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=gJA2z5x6_KNfVD7ueEidmifBdr_meo20S12s4MK3ztJX_0G46r5k16_fwjt6WLRpLkd9vhn4biwUOshEqGKjPtGHmf4uGcIQlvebBjmPKpZ9tVbg-VL2vpVNS90BbyznMoG7A8eE33fBiEnBPHpwIb38-jlkX9jlUAeQS3fPshSRj9k0-6fl0aLARZSBiLZbUfxwFNh82XWjVjiKbqj_wNPBhK_oMuJbmgSFlQl4b599EAoRYgAjm_5Qze82SCpZogDhKeys92tDoTr5oMarko2dgWe9qxzxUrAF0l5rOw_Jv73fbubO-Nb4puYsoobP_YOyVomRPbrYVosIbVQBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKqdrvBOdme9TJ2QmSmYws7tS9LfZBC8fEKKOe3-R3GtgAspaL-jV-hVGSa1sD6XMpAZEWc0LUDakd9lktsVICMZZsFEONz4D4rteEk49AkMV8CV9zyMhSCDHBNPGFcEaUZQW3gnDq5bWLGDaKaMipIBBPzkNkdHs6O9l2mISZYINC7LDU9GFJJusklTd5jbPnc9PQVKw35h0ov50Wx0lRFuJQT2Pz-7pORK5ct004--j1QRCGoPqC8BGfnW7b10HbfeZ4Fco-wlVIvMyzMITvLV3coFeOfqKBjbQar4YNhdj1NSUQHIaiZW5PXGYn1eE8dym79l4bUt8dKlvkUWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=vvcbFsvkFbIOh0tXLBX4GEXhSkPXArOpEuu6ILk_KBA8OLbaIdslBAHyNTiNfoZcAh4hg_OafWe76YeAPrP6HngTXBysVw_Ap7cmjGh1aaYFXianOkaW1hIVVupO9Z1MWOVq4AZdiDmanitFgAlCRMiBW0uqRqGX2MBa7JSILZg9nX5rPzvqXi41jz1AWoyOaFEtVKdQU4HHDIrLOBgBuh6o7bMvb1vBnduygfltTQ5CJoVkOl4ETnVWs6olSLd6JlYZWZiE9Ae1HDabDcRvPJ_4sgyhL8kcBXqjtmJ71Klru_807N2FYe9QrdF0x1bGwzgLrR9kHRDS4fUZZ2XElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=vvcbFsvkFbIOh0tXLBX4GEXhSkPXArOpEuu6ILk_KBA8OLbaIdslBAHyNTiNfoZcAh4hg_OafWe76YeAPrP6HngTXBysVw_Ap7cmjGh1aaYFXianOkaW1hIVVupO9Z1MWOVq4AZdiDmanitFgAlCRMiBW0uqRqGX2MBa7JSILZg9nX5rPzvqXi41jz1AWoyOaFEtVKdQU4HHDIrLOBgBuh6o7bMvb1vBnduygfltTQ5CJoVkOl4ETnVWs6olSLd6JlYZWZiE9Ae1HDabDcRvPJ_4sgyhL8kcBXqjtmJ71Klru_807N2FYe9QrdF0x1bGwzgLrR9kHRDS4fUZZ2XElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji-HMFUbcIWbtd77-MmQbYyEAaVF9qGaZwA_L8VMYXjYBod_TcQrN3dw7y7h2aDjDtNOuDyGKwcZKxWNGFyIGvX2nTeqnG-TgThB-RV-_G4Zxp77knSmcRzr45LkserZfP8bRmKf4YuZlPfGELAOHFV0TEuoDD728ITWwVDOxgV_dG6j_yA6D2aGmhUJKjv0xbIjKkDaPWopFJlEaodD15U5kVW8C8oMj88EXde0Nny8xzZiLMSygqyc093Ykeo7jPhq-g26LGJkjm_8T8vzpChni3XL7woc8bV5-2TrTY7OGGQOV2vzdpA9hHzrnbs4LOndREpJVN2bYpKcyEPDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZigTZKwrr2ZdaQ16gEVxFur8Z27oAxvh5SmJPLd5dEed9C1CdUGZ9yFlyMOUc-AkKDmpfGniXKnDR9bODAVveSQt45_RlOmz2tQ90rTRW9uvpMebFjHJEytV2OMDLphYhuV_H-BcIUybfb_EMddWbpZRin6J4H9JGr-jFXl_4lqwngXaWlan1wwsELsmNhXeIZ2y9e0s9fpA4eFbgctSflA3LCW04K38fNhE18avYCS9eNAqPHFUy97WbE88TNj8wdC7rNpZI2dWhUgJFGET0PEa7aCibNoQCsqSocxaqvk8ReCQDGRFIVDDviCm5Qz2HzL6wBHxjNX3QM_lWSipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvtHZiT0HNpL3Dqkj1Mm1bh5Rs6-EJLZld_QT3pwci6LqtK0jrjIezkHaww5-VOP58czPVWkAi3fEkxdKagr4ykJ4VUSJcI7gBolwv9vFih5IFngxc1tNBfF6dYINjyXBSrakCOh7nb0j5M9bjGd0w-vv56pBf-KGUcVU2KIiIyUVcalt0SR_wsZEYb4yHei5idsZ-yQfEdSJGD-XBxZmcwbyFPVU6rJYAqKfUJzr1iKw_eSoCjVwROlxYLpBw0vgVOCJ0SOOPzwCk4R_ADf6RHBoj-idtFEFebq_yZVOAt4BFjyC69Eenj2xFh18Pq27l4oADmIVN3MnWQbE0ugjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oULiHOXyzUwkSKb1Vog6dZrd46LvZH7MG2eQrfqjY-GgL1ftxY-y7CqbfxLqt_rT_Ux37u0d_IOCTuIJ_O2TaeZAgEtNpbF5NpxqMeakXnV3gmBCpKRBKGVwt1fi-Tl2b-AsylgeiMl5clKurEmBX77ZcrMx5L2DvUu8nvDM3bJPLMbH_9MFIx6Gvw5hcFQUn5V9TTY-Hq8clYz9lXewtI9ktg_uXzMBBWPmHpm1nKwAlQFL_m43kzGgi9IfIy0Jq_yeppFkkbVHibhpx4HzhgQrOU4eFYUT6VARdm7Tw5uSRQE3pO4c6f68pWt1ho4xbrh2lQz97oFIMo1qLJmqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE69OryjP9w8uaIxWavNJ2fM3EeoYMtl0RRJUeIqJPt0OVbdE6CLoERZ2nuCw989p4TMslaseG9T_wGVcsNckwokAbKV0HSZPa6PKOIbY7SOmJ57T7dXCa4ouRpmkL2F7zhNYGYDWh9wC0TkZbShZJwvFVObxfxWqsNo7nurgv4duWa4MsP2AZnGOH2lyzHDOA5VPlUhlw4yOjMVtCTqA91lwp8FQQXVcsHNG6O1nZ7yZQXCqbLS2i_YVIopVEYL8v4VyTaGnkmDfAchMvFmZBzDn7FqG4JDmpjihaD1Li9Dg-M8A-k0WWy-e4i37os2aaJDiTCgRDLrK80f_wgL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIqO-hbQliLiqHAYr6NC-THoN5SV6LHZ1RPkBzXo3KkCwXZcQea0oZTXkH5LMRD7jNfIDLU-Q6l3QHt8oG9KO87bZdSiwUSv0lmOjiSY6luAjDKMQA7neBGbHe09d5mBCF_8RgkQY5HpRDW1JQJNqUDVhsbQfM-s3Tz55Y7EBwDPXMMSxBTgiVCf9CPLYVXTVdh3hmEs8geMpe3m-yVd99-k1EJZwMBd8W-6QJtMXrtddYPaZUmXOBidmhoNX4SSrDPcqUAu6y2hsV4BFe_6Ij8LH49D7YavngR8dKbB8cLEPplXIksrLC7Lb0BWnNWybG47_SeyGnrlczUN2y3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
