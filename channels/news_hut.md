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
<img src="https://cdn4.telesco.pe/file/uajieOeGUUNjUJaVJZb2sxNf628ksEd69WIa4YSpNsCcfs9b9TwFxkYZpQNJUIpS8eVmwJTOCQvDj-t4RkrIOGDnNkm6GMw23uK1TyxprNS6_4FOs52RiQTSGYqcosWqzCElTfufXnhdzJcteiDG08HdFMr78duF1kP0plU9-2TQIY5gndXe4uGfRCoGpxNk-XwIMJBG0CfgEZPq0fBG37qaMsntzGyesvdFBrmH3TEJjAiHE0E-MEjvBCpP5vHJUYhqet4DyEiYLLZPf2WeXhJj_Fy_CzJ8lhbFX2ylRan7tDujSpJBbcjOB6-isltdOpMzD1YC62kVg6wNXIZl1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 10:24:21</div>
<hr>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=p3ETIpwli41cvTPRpZ44-935-Y3h2mBUjCFa0M-lgm--BFUOkcxSIde-JIU-oYNbJJT6KaofhYbrdy_qVlugeT04jmnhoBUSkkdOEpOE5Jee7wj_bQyXx78lHGj8xwT-UxJOTcuej88gMlm-14ySMtFaOAEpxPqQbnIOmaIorLVzGPteJmS7FZbb7mJXu9HVOKnG-jtSA0ewO_0ODFsyzZcQPbV_LW9dD3qfBKfsklJUqync9APVVb3TyF3h7yGOWqjOjkCEkCMWc-iCKfel1Y979xMiJ5E2hugGjVqno6VwQw4iCXSk0cdIeQNbTsYvDDZEI4tU6xJa5L9x18NlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvkmt0_TMWg8rsDElOiwNohIXRSROaSvufFjHaiHfn7DIpLMndd9LKrCNPUJNxUyKvQIHWcrQ_XKgipXogJ8g2eXHj101_j62lx3Nj-lIk44gSdihueI_v5Ka8vsB5jHgkaC4v1FqmaLEy49bcFjrnIBaIN1HTH4SwRp7DipNbT9usbtSCnu0pl6g_CcBajJ2OPFAYxEVqYs1QF7HYMgIS1rZ3Q-JlVKTVorHOdSBYfhlo7-oAz-i_5MBLHUktMu2RvS0ADXTBx9swtF--_UEEJRBUnbFgZkxjPFIt6scW5Wfur3VaylYUPGjSQRPm8vu40MV8Xt40Uug_7TFgYvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdujzBKrPQ-ebTwAzXCI55txLFvdyQtktHJcXwTIV_YwLYgVk9070Y2MOo6duk4aC5RYRIy4DSf2JKsdRAfhgZHhWje7tGkfGlo-rK2-X6mCteJZA1CcbDPRcnNh0rL1QhiTBL4TuwokaVzyNmrgDl5Dqdnxvy-7CvHZgxVMciJp5G9MdXt-K2Ice7K3HE6TS7Dwenku-fm68of_EwCzdcxVS2GYRkHgv0QpriIKpCq0d2F8IGZx9Ta0qLChvS20YzWHBTueuNjpFIR5_CktCL_ZeQsTkO2XbvnVP5UPAAP8R1BWpvAeC9-WfOh2EbuHZ4JTp3NTvSlXkkIs8MRHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKBbY5FZTcTIu2NAf1k6IfOSagNZrk_ZmJZ51LIMN-sU2xg2RR2sAanDMPWoAHJj3oovHqlvS1S-EzE-bU1AiRepAvsK3oprN9B3AJkeuYK9_TQ3p87gNatZOl4AuxaZYJx6JqhIoKIENGOvgCMx3RFE1qI_Dju0-LHUvRhFr4QsABn6r0GeaeExxYab18vPRUPXyALdzI04GQUyOmtfhyRa2S-pqIBgfV6IKAvH6rVdm-OFbaxDh-vMy5105CGT7VGsArM1FzPRQ-1TFZur4TDKC50RkjdLbAJvnfGjs8J--gUcJMxX_h3A06b4_WJTIvgvmBC-cL2Z1ClnV_KK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTi1Un8zG7pcYrgVVfVy0HWHvAfdN0ZQt0YODXDh3c4GikPRQZ3QgD7u9ZVCgXi5MXPxFMlQfj28VpEC8_cVhcZCePotzq4TJGQw_uHO-4w1C3FbRFYHjjfCt6tTk5YmU5kHdX_ryQW4CD6mtlFq379ZJtun4DyY9hangYfW1BcUGohCcf3vDLuWXDypvWlgnB6KOJb-boHAvCGSYVxK_48TtEBCbBo5PNDzQWUnSx-7ISnZHuM9toUkj6nRCBeLIUIW59Zn52feUgeqBNho-Gwesp2yQnGDuZBo731ZGgGidcelEsPRa4_Ip163vB9R1p_wwdIaCbJrFZlOOy4EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=SjtGn8mv2FGq_g6D7L-iVvvZDVui64RXLMHeE_OK9a1qmZIoIAOXWkdYJ1PCvxberaWOjeo1Fh3Q3l-HsdL8_-rZ3R_QsP4HzOmQj6Af9rhfVpoXX_PT77o_tJf6F0vDeiiIn1776arZ0SPPOJMPG6TkClpGZKZBymGTDdD5OojRLIRv-YlOf9_vHqc8_aE1t61nHN-q5ONc9N2YJia4WNhS0Ltfr_S32zAoHdXImMURDQLESQXPR9wu8Ozl6e13QNpgZCqL62ApR4OHFBp5JCXkHoK3NwhFj7JJyhVFKgM9eL0jAgPcenEI3crQLrdG-jshtDRY4uvrZn8O8rQNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJajQlr3Sk9vaQeP3K7Tak0AZWIMk8N2Tthjm67wHOgBkvVtc-HR_3PCvrzDSniVDG5WT5niektMuxvZXw_Twxl8a1VxcTTKyk4aJJX6ClCHFcixlaFqfnzStr_L87Wp_vccEWGj97gIhJQCE7zY0ApctX3bfOcpcxDoIQf9qM7ZERnvl3kqaqMGxzkLWzLF9saIdc0Fm4UBIwhV8p8_4eLTi0y4SxV_DtA1QkobguNsWRuG398GQPQC4V0A0wQrP9nx7TCaJb1gs2mPfy-pkvogzIaM6licTJ_aYJG377P_WNBgOou668rbQicYqxoH2G1nOSqXSInEckJVXe4U6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XctzEDdrJg468ZfVp0qpA5_RHVvGR1xwf0NoCxtXxIoBomdmtmJQOWTeujULquoRTBxTP-3CYxZChHoNHPFfnpsl80cm24BjBckL8gFbGQi1pQBR0-CJe8zy5TVKzA996qmIk6POmdx88E_T-fwOtFt90GItiJNDEJagNM-LnuXiZXOn8sRPJGAX_NQcWTqyzsI106UNBUQG2SBEegTQS0lENBUUPIoy9vpOAUSsxgXiX96iSUdljCaGYE5Lw8Vys3YGAuXJD8YrwSWdnmrCHkNSQaYS94_I0tAERTnWwEDdeKWFEknQqFDyg6INi4Kx3zNiyUs0r7ShVdc8rMJDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3W7DmsGszEBUF5UKh5lY2YU4dmtU0YyZHPu9TVs7MLq2c_Npa44oCZEJlS-RYruPiZIsw3tdhfTjajmTKDAyT3JVtDqyCUNjLDjUtQlH83fMaOR5u4QIl6mFzsMsVVnDg1zksCTYKyoLDMmgduFaCamIykRhm9vB2FRk--mFeMcZP57sqCHtgR5wX7sljMk9Ll32Ze8gxn8vA1yTFKlfksb3zA6NrXGjDNNDSzbY6JOZ2UYlhSf3pJuos06wTlDx-NoORP2HPyS7vOE_KS46TrwWDit589I9gcYlqStSk6TcOV8imcqBVPUpKs3epFIk8cXjlWVPkxw-4G8aBzieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VphKW7QLjPAk0ooEMwgmunBLsdJHNidxoCWhBpLSW89FmwdfV27uSH3EhGOZsHlsNzUr2aWahC2_kZMrlZUMhu3PGrYyXip8-lAaNNWuOsink_fNMBxzbYdxi7ZorW2sqg9FxZsjFHRw0WQtLzZk2jpcXDHdMZrpqeR6BgmRaznkgVNkbD7Gt8hEfV5HDLxBReefKtKthMLfov7AaixB8gwl-LgM44ayarm8H2JAfvEtGF9WeSLMtsj3dagxdyZGi4fm6M0rnIe27ZVU_tVkrY0RI8fyl0m5lqz2wyCtJuUEU-Jxx7b9xGGINb4RA75IW0B89zmqcgQ8sTFdIn6_Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=G7VDGotub5FW-lzo2C4q-S6mG5yZ9UD4PanedrtnzVsImumDxZOJriqQrNmuVpGsnEfDMwrXW4Zkypn9pBKbgOVloOC7_0zIu2koFPx_TAY-XRlTi2cxyS7EAsQ7-PIQ6bKGPkdOhij51fjb-1nW9WwU0Hj7aII16EIAvRkFScHBZsrvmj9iVCR3FaxBMKwj8sCLBhtXThiz4VOAWntVA5cH3LtBF2WMqqJeLMaY7yTdS5Eh8aPM9MpeOckpNDTK1m_rugo_JERLdHAFPU2kB9NhI1w1D8l0khXCqiXxTvnAaKP95cwPdlDN9uxJKoDcNNm3YjGCke3x0z5iFFSmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=hp-EdZSKwKuZ7nwdTA-IqET7QqywB6tZbbIcUJHyUPWDwpUKwIKJ2L-XFrD28cHuh7-l9tOgzGAwjb9DCMRH8uCPZJVI4u9VfRk0no1WSSAGVnUmDVos2I_7BrkNzYGZXkyGdHuyRCxHyv253Nrz5cNNSLBgPQpFKRC18vxVHtzQtO3NNedpnVyC8j79kg8RbP3rDOIsyJcR9uuDCdqqR9iPH00Pn6T_JrAENzjYE3qA6JtnofufutHnlJjsHdpULbhBWqa4noD70UAbUvsoKqBGcgZrAFkEnpTh8qHLyse5cwHJhG3qYIOCpf72Zsp5AsEEoLANWb1Pc7SOWgyzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT-cD1zxj5o1W0trsEUvBaTN-u0nNEBfYHczqgqekzisMc6NIVzHBjPg7OnMlSw2kY3P0jjhxPmHllJF7xfuwGrwZdbeoSeEoVn9JjAQ9s8YfhesCQUT02VF5LHGkfP3hWjY7c5LHaKA2H5coDEKhwQj76ZgTJmJRAt9FbeWCWYIbM6p555xJ-XYZH8Pk7NFx-u1EgT1sRY6w4u539_wP-97-BZC2RmNIVxS8YMfuY9vTjnUN6H1GRLZ5_8DVID827rvvSxKhMYyfL7711qG7i3Ai_7RZkKF8GMqYq28T82_1HQvhdinwes0BFGoYPFKxzWOAZHL4xmZhu88BEpO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=Wx3gJGMW5Oa9Eu6J9_iDggnIhYIKfRnvhrCsMz12DqyyuiLIzwDZ63iB5Ek45ndJIjzEW7hlzi3H9cWZuseviC-u3Nc8uWQ2lVbZLZk4oAOwhP4U2md07TlKC58ajTK4fGSc9UENGhlIOAv3XNOo2NYP1zOP1iRvpgtM2HAJ3G8tqUkW--8TWZHno9Ng2pILa5kMg2VZR-SHI8uyyIpZDVyVHcUh91GBLPUoNdlP3xBOoDGYUWUCcdWSMjuwcMAMHFt7pG7fEicZk30GiM0YKoqr0T2dy5YfiCWSQOf7HS_vJ9mY-eVELOQZaGzIU5kaZR1zIk3e0rzgiT4bVEaWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=kACtIKrvWbhSsw4xhig-YxB4OnYpmjxthFlI6E-wq6UrQbe7pjFva1M0ZuzxdwWjboB_3P88FFsiS2_Xch_k_q_VSluN8fKaEXRFPr2uyE_WLDqmJWptdC5JdXzIZ_-bMhfKI3tGkZlSNJAcQjQy9TPR_Hj8DU2Pq0p7vXbbgSZ8t1AJpWgSpcBMm4JS5_9zr-cJQFzC3CLRzQcS92jzzcCzxo0UA3mXm_pJ1Ck0IwS_n9Lt0pYVoWO49pdO94jTUxyksVhQei3OAKWTc6BeT3PaQOZZGkiQYPaVpSdoghAp9F9le-FKouEcwB-hnrUFFhR-1_7gBuZeq1CJGfDnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d972ece2.mp4?token=hHhKl9OxZTBJISu1bH7w5Ra_a3LPzbBEn-yGrPz2ErHpYSr74d1cG5M31Zm6K9oIgwyhwpqK62ZrOtEtV8OAhK2B9vAYnRbsgMojgabIya6NcW48voZ6MQj5-MT0_CwtrQqv1bum2-LZN3JPlKRlEfOm2GXs2k7xsDggPCCu_VgfhbRhHsTJh4Q_vEyIWPd1DI0pcZO6529C_ZQUiyRmliPRCNqeG7_Zpysvy9MQ0ZUwhEC3qaZnxr8gqsf-3lpbVf8MIBS3-4luDN5758zWhCodZTfd5bRoij6mm0gTGbOS7XBCSEr-cJ3cnDXhVX6EE2UEoXU83BQMXgeKxRoNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به یزد صدای جنگنده
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68396" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خفه شو کصکش
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68395" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامپ: هری‌کین هم خوبه ولی ممکنه تو پست اشتباهی بازی کنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68394" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=RHpm7ipjyfLbdNfpce33EnTCXChd8hEsGwxc39h3-2KFPJbPox_wGkX2StNdl4SXOqnb6wYCRhhsfbhmK0cSDtJkCQ9HRVveUMZi7r-Ge37_zdTFSGC04lK5MCdxqNwopnrDR2eK5F3x9acxWzpE_q7js7BOoohPvzhbloC_YinFKZARNDp6vKfPQ_jy2MYyeEdLRtYJOOqgKs-L7I4BPhp4xlr1NMHl4lOxYa_xTLcr1FfHGXgE6BlmvRrpzVhvBRWHv9HKC2LB_cSxc46wpDpWyOaTJRJUUeEMpF_cvHSn11CutMfqktg812Ho5feOLHtOHYXn9foubh8BEe5OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=RHpm7ipjyfLbdNfpce33EnTCXChd8hEsGwxc39h3-2KFPJbPox_wGkX2StNdl4SXOqnb6wYCRhhsfbhmK0cSDtJkCQ9HRVveUMZi7r-Ge37_zdTFSGC04lK5MCdxqNwopnrDR2eK5F3x9acxWzpE_q7js7BOoohPvzhbloC_YinFKZARNDp6vKfPQ_jy2MYyeEdLRtYJOOqgKs-L7I4BPhp4xlr1NMHl4lOxYa_xTLcr1FfHGXgE6BlmvRrpzVhvBRWHv9HKC2LB_cSxc46wpDpWyOaTJRJUUeEMpF_cvHSn11CutMfqktg812Ho5feOLHtOHYXn9foubh8BEe5OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=hj9USxLKlJLAssL4Hf8MO-WThe0bKes77NmR9u4tILZ6z8HXpHcPeSf4j8Fth2_q5LTY8mXry9HkLUgG-nc_XP4NZM6tiOBGN9Abg46Mv9bPDMRgjlWXYn3o9lAW2gfbM_z1rkPsDzdWlQ9T_jSgnWjZ2LuLGSQ7nMNQyz-5KjoJnLju9U5GzqsPK7Q_qT4uTZp4qdIRuc9SnoVVz2lQbXPo0uEKRTu64PPNlNykdT8rUU-fn_0qxH6URGiCqtqQ7M_I8vN4XUm2KXYYV4Y_1dZczVZPp8DG2bMFwx3tYYL_bnw1CFsMdDjeezuDIAxrdv9P6_CtEwIjrG4uMTRD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=hj9USxLKlJLAssL4Hf8MO-WThe0bKes77NmR9u4tILZ6z8HXpHcPeSf4j8Fth2_q5LTY8mXry9HkLUgG-nc_XP4NZM6tiOBGN9Abg46Mv9bPDMRgjlWXYn3o9lAW2gfbM_z1rkPsDzdWlQ9T_jSgnWjZ2LuLGSQ7nMNQyz-5KjoJnLju9U5GzqsPK7Q_qT4uTZp4qdIRuc9SnoVVz2lQbXPo0uEKRTu64PPNlNykdT8rUU-fn_0qxH6URGiCqtqQ7M_I8vN4XUm2KXYYV4Y_1dZczVZPp8DG2bMFwx3tYYL_bnw1CFsMdDjeezuDIAxrdv9P6_CtEwIjrG4uMTRD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=KZmPAMu4EVxosU7B3nV-XJghT17-MIWBk-zJ1-Cpe-Ewf0n4N1B_FuSAeOYkNXErGK7QgJHLRzrXmHeU7LP7htVtGxlC8hXWplMkNK61kpOewmqImxTNTuSjhFTx1NeYWijqJJQbDFcNy3lWNzmrFe_HDwfP6DriBs2FFzgS_vOngTix5bCS5yEr77lgdYaU2SSQYHjM95kD2H06f4k-DSd0wXEdvEP3WcTZoNc5ta2-IyAmInmbk4ZtrXXqKI1fYIcIBPIemE_X8RAFE8n9MNjexUViztudjADYZmOJeKYe66dn1yV5SQnaQlppk0dNQRVCN67eVfAd-WFA-9oQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=KZmPAMu4EVxosU7B3nV-XJghT17-MIWBk-zJ1-Cpe-Ewf0n4N1B_FuSAeOYkNXErGK7QgJHLRzrXmHeU7LP7htVtGxlC8hXWplMkNK61kpOewmqImxTNTuSjhFTx1NeYWijqJJQbDFcNy3lWNzmrFe_HDwfP6DriBs2FFzgS_vOngTix5bCS5yEr77lgdYaU2SSQYHjM95kD2H06f4k-DSd0wXEdvEP3WcTZoNc5ta2-IyAmInmbk4ZtrXXqKI1fYIcIBPIemE_X8RAFE8n9MNjexUViztudjADYZmOJeKYe66dn1yV5SQnaQlppk0dNQRVCN67eVfAd-WFA-9oQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZL8fXf9MwS-K3NRHY7QwXqjFOxyJuEXPWSTbqVtH_h-mOSq30yxS25WYWq3MFiLe0CID52RlTTd8xVeoBcZHejWwkkD7nUkWSA0tOY8rtnMEe3nUDPFNa61DNoO5vTi9LK_8vWt6ZIkBjfGosw-whTFd21xNjCbaaBZZMNms0ucZx9EACCoJQBh2vAlAt9RmyRRzpJb5sJkfJ8EWshTQedXHJZMt4I332CqPRCnnc5abRYNtFN6XCCdq9v_kmDxXOjqnzK7E0s_ZGs8Kz9EHOGfsCsfokIvN4-_oqzinsRoUlgv9seY4KtzlFGLq9FxA51xhE_JDHDJLBo7z830Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HftnfSSMsJg0my09wnU_gWoj7YBKJi9n6gqk6UAlK1HsYH6a8WqcYugE7Vdbah6Br_byWkbzWttbFST7NoFV2Xv3GtFWE1kicBoxVCGDP4_Wyw5F6c60oBcTXquTq6n_O84Ej9Ldo4IWzfgMyy9E06MdISQlYST4TadhWEEfPTnn8QRg3iDldk5TCSSjmK_vmiEsCB-EnZtBj-2sDblVQ3dPtEowZrI2LQ3dMbxxsT2wasakQLwGaRkiPxTQd90hPbeMEFEb7mSZxNOivIHTUY_fgYXbCNoM1ZuRqmty35b8LkjJ8Aond3hK7aJMNXGA3nUHlPN2IDfYUqJWDA7W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5SpthHiUKkyl_1yXcKj9u2x1xmXQJuKRsQvZ7AC7R6hItuwYGuDqKEftMMn5jCUwfEQcPC8279o0VjWdN1Ls9anijyVLLYDujdAGWrFhE6Ue3fjU4IWhThZHgel3UW4Gd8GwZvUea3L7Iz1yR0ZBWlvsX0vR0nQ7sJ6--vx1gTCOCwu-OZ4dZFJmLlFdTwYchnauU482KI6-VtRiAusZ29qIry4J7BSltezzV-5sl6uDxjGhcWRi58Hg2EY3l6GuYBticEmkeJKtReDk8oswdn3PC8K06LlYtCKTjzj4dAYwJ-SqKAYoqpIonUjJzDpvV21ZjmSqSReyXfqF2u1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qMem_kZwdJqm0HtKb_yMhbmIaiAB7vjohn3oGnIQpQiz1xhjWIxCSiIsqqm6c9iUkwRCK_TJm31mIvFc2k_HJOZJRspnl6LtlZ8LrQ8Q5i5ElKMQavhQBxFBxpwIuIFX2v2gxbhsEVhys2xtuwhMoI7AXVRQ8zJX7I5aDPYP0bp6bTJGdRE2GDpf6uJZmajMB4We8saGlnb9F4daSy4e4mgXrEVManro_diexU9g74NovwrnQjdwZwUM-abf7OyF1fQS5Wt5suC6DwHqtZ4Dz_pjNCCjwWzT3VzeU8dOP0pIZC7hxuQVEM_aDpABp5yuFc8EL-zMc-0Ox0yAtfDZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qMem_kZwdJqm0HtKb_yMhbmIaiAB7vjohn3oGnIQpQiz1xhjWIxCSiIsqqm6c9iUkwRCK_TJm31mIvFc2k_HJOZJRspnl6LtlZ8LrQ8Q5i5ElKMQavhQBxFBxpwIuIFX2v2gxbhsEVhys2xtuwhMoI7AXVRQ8zJX7I5aDPYP0bp6bTJGdRE2GDpf6uJZmajMB4We8saGlnb9F4daSy4e4mgXrEVManro_diexU9g74NovwrnQjdwZwUM-abf7OyF1fQS5Wt5suC6DwHqtZ4Dz_pjNCCjwWzT3VzeU8dOP0pIZC7hxuQVEM_aDpABp5yuFc8EL-zMc-0Ox0yAtfDZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k89jkYrxp3EGoefrFwv9C52wtdDTV1OuyxVQwKg2K30HK4JWiSmSSKygdt-eI3hvoVtcWoMne95DNVGAS4QwF93UlpKnoULABYLxfgWNgrDb7hlRwu9AjFnOKFtTxkTCk-EBmexui52Mhqz2l7ehPWJQtYm73fBKfBq4nxpmfBqTkQYyLiMqEpf0nnfD1XP8AziNsQ0cv9_axCR4IeQYVI1efjFjw58zASjUzE76sapzBK5v30UmKK04vY38b3pe2zqSFTWxrMK_Qa3uijCiATucRF52uA-LRwa8XQ1JgUYkuOO-uf05XBPXKKcCGiBqCCq4dUP918le6zG02tAJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2CrfA6txT02TOsgSUKZBsprW8JUGvfp9XFsHlqA_AAJDoFiQ1gzGiqS2Tuqc4vF2AxNfPKj8LGhaV_zZUVboJ-9IU4BepMZLXjKFxW5eeK8mTTaNS4-vNXKSp46HyvWjWnchYv-pujaTpot0zsF691_jpMfXuXdBlbG9nliMqKJFuZ3Hu9TJ6hGGUO64HGMVHxGT-1XnEGk_vcBWsy8RlN14a8QvF2DpYlw4t88fpQgniRULyKQrnnDJyrRcyw3YYn2bYsNgMRlugUwCIwuF-QC7pf968LuZkV1L1OknRozs9PAHirBbAxpR8MNCoiBWhqI5mfLcFNsuZDetqEdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=fqlmlINx84_8FtQ5bV2u7VxaxLcCwQOOELwxo38p5C0IH9NkIvUJ46OfIi65rU0-J1wkbU6MgX8_Ywpdqbj6RB0yRM8GG6K2-qr408_GQxP6XpzZCoCddZZ-dSibuan7uPzNXiOUJAXLscazLtkCzJN--Kb_X-EwZphUoFiqAx80WR5HmQL_5-qMccBcksf_dhUF8CINcRRoiMvZ67mtdGOxI65RX3mAkNw37Ue3-7N5vImkf1HtQAdJRpIcGpo5KSrZF9USsXDdI3A-aWl1VAYWYQPJiR1hdRf6EynEwb5DNyGjQD654yhA7G1MeMW8a3ruAwXuQiBTMjzS47F2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=fqlmlINx84_8FtQ5bV2u7VxaxLcCwQOOELwxo38p5C0IH9NkIvUJ46OfIi65rU0-J1wkbU6MgX8_Ywpdqbj6RB0yRM8GG6K2-qr408_GQxP6XpzZCoCddZZ-dSibuan7uPzNXiOUJAXLscazLtkCzJN--Kb_X-EwZphUoFiqAx80WR5HmQL_5-qMccBcksf_dhUF8CINcRRoiMvZ67mtdGOxI65RX3mAkNw37Ue3-7N5vImkf1HtQAdJRpIcGpo5KSrZF9USsXDdI3A-aWl1VAYWYQPJiR1hdRf6EynEwb5DNyGjQD654yhA7G1MeMW8a3ruAwXuQiBTMjzS47F2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=lr4jgmnfanKJltSOhD_jh-CiTc9Zqu4jiXnODlDa4gbc5Alhmv28fYm6kZ7Q18e4dBqleJjWK7n-9WnlTn3NEp_cx46tXjNbIyREBYBU5Gbn6Lirmv2cEny6O-gyTpV4X1a_sIXGBx0ecXacnH5Y2ujzaGq0LKrDFbG3P3iCoHlK7GlYA9ici8o7TFhGp_9_PP2MuR4zR7UwU3AX-6NJwbbL4yKEbgpPAtdSKuTwXiEIDiXj5yU9PTbC0PDi6g7HNglcqRFuPbKd6IIEXpqxljx9VUbyXtRW7b9A7vuwd9l562GOEg5lgPVB6IyuU6i5wJsfSG2k3nevGFHgz6qX4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=lr4jgmnfanKJltSOhD_jh-CiTc9Zqu4jiXnODlDa4gbc5Alhmv28fYm6kZ7Q18e4dBqleJjWK7n-9WnlTn3NEp_cx46tXjNbIyREBYBU5Gbn6Lirmv2cEny6O-gyTpV4X1a_sIXGBx0ecXacnH5Y2ujzaGq0LKrDFbG3P3iCoHlK7GlYA9ici8o7TFhGp_9_PP2MuR4zR7UwU3AX-6NJwbbL4yKEbgpPAtdSKuTwXiEIDiXj5yU9PTbC0PDi6g7HNglcqRFuPbKd6IIEXpqxljx9VUbyXtRW7b9A7vuwd9l562GOEg5lgPVB6IyuU6i5wJsfSG2k3nevGFHgz6qX4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkOMGVzgscZI-438bZ1jrTK6O_jPDHrqXCvA2--SgeqXRyCFwkC9vKOA0tumw7OsYhcvhyDeaGA5L6t3pVFISNsBc6KkRZu2t8riOP_skUYXK-CyoYtPUTkcDycxaQ9sT3lEbB-NlhYMH2h3Y0CIq2UuAVFOEqqQadfcET4TuHpbKLVQXiZiCRnF6nVvRH1vDkXm4xRy9JH2GPHAQPlz6WBP9B37Le4B6VSE75sNNql4H30-in0I5aVxqxE2JRW8BpqKWWb1oi29BcWgUC5sbwCwOMHrzTYIpQc7ffQ_l5a4R3phv1Kh3JZ3sorY7bmmWqA0jBzEwU9KdvYF3yo-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNvDygJ46lB2d4fviNUEd8BNBfEGFNwCz2-AxKmsBBELKPcJAcxavgVTPq_davIXkAnjqkEhd0IL3NwEIIYGeoO_i9nnMqhYszC1z6XpzZQcepY6guwGmP-X6Dcv51198-D8v8bA0nu8yk6cZEaTFKwYnjLwT7QISUE0nR8QVTZSlKEpOo831DZgySRLl3wbbTQedTVaruIX-uqLOhpr093eA1f9FhkfCBTGrCyCt12mLRDUqI0nMJ_OGYgPZs1GTrijCYZz7GiCeLUmyED4qzslIqTMPAXHyqTtQ5A9W4xdCeXrhDycfJoQJ-1izCr_9SI-gkvQRBc-YeWRYuZynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=IIoX8oclZ0zPaQWFM8NEMUX-jf2TjE5yl6qCQ7D-US_sP-oytNzbIGBcrwi3iR-SPlW-WYj0TxSFlw04lsVBTVDy7UvORFcOaQ_htcwu2b4X1-I8J9ztz2FXOw_aglZio5yVJ7icTXSpSnP9C67QUPlyJc7onVKaanEvv6HeJssGB_OvhZXRk_t3yEiJDqkxXWYHit_0xA5l3PtukfH9z7RxevnLuAckG9C1YkPSON_8vLg2IxBUvUynBnGRXucbxfvCFw0TufYXLmLpkrt8kHr13YPAyuAcrfaTKyXTcHY2kuXylNh27EjDOyWfdGmGwkLr1IdO9-L8HDkdFazaeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=IIoX8oclZ0zPaQWFM8NEMUX-jf2TjE5yl6qCQ7D-US_sP-oytNzbIGBcrwi3iR-SPlW-WYj0TxSFlw04lsVBTVDy7UvORFcOaQ_htcwu2b4X1-I8J9ztz2FXOw_aglZio5yVJ7icTXSpSnP9C67QUPlyJc7onVKaanEvv6HeJssGB_OvhZXRk_t3yEiJDqkxXWYHit_0xA5l3PtukfH9z7RxevnLuAckG9C1YkPSON_8vLg2IxBUvUynBnGRXucbxfvCFw0TufYXLmLpkrt8kHr13YPAyuAcrfaTKyXTcHY2kuXylNh27EjDOyWfdGmGwkLr1IdO9-L8HDkdFazaeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=hgCsc8x8ak0_GEkW7IJTRSSJnaLrSYIRfNg-3P_1oWQckQP_QuWJNvRSplRSJdirez8GRHYh0UaOjnE7mBkFjpOk0996RvmmwXFjl8D5PhNnmHegwdak0Skmv4c4dWc09mo5h7m4WtcPcqpW4CvOLqwRXVDjQRFhSZi7zqCVV8w9VFqGvXoSPWoiLmgETuuTTO_HDnG0G1J6l6XGdhyGXZV32rtO69T9Yd17Br-1gmja8Yu8ejnuNKCpKswo3IjWL2-pJG2bWQlva41JZbAmGLoVQ7gzWXFkarz11HNnTn90fW-83Xump3XQF7aJSlP-7HqJxun3MDQTAHoCDWco8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=hgCsc8x8ak0_GEkW7IJTRSSJnaLrSYIRfNg-3P_1oWQckQP_QuWJNvRSplRSJdirez8GRHYh0UaOjnE7mBkFjpOk0996RvmmwXFjl8D5PhNnmHegwdak0Skmv4c4dWc09mo5h7m4WtcPcqpW4CvOLqwRXVDjQRFhSZi7zqCVV8w9VFqGvXoSPWoiLmgETuuTTO_HDnG0G1J6l6XGdhyGXZV32rtO69T9Yd17Br-1gmja8Yu8ejnuNKCpKswo3IjWL2-pJG2bWQlva41JZbAmGLoVQ7gzWXFkarz11HNnTn90fW-83Xump3XQF7aJSlP-7HqJxun3MDQTAHoCDWco8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=K2vtPRl2DELt6tM4Tx-guukEAqd2yi8mAfPhtjcw3DzdsQvnXVCorsmLGr_tp-0_Z5kOiycps_e83mGuacEFqeNhLQGSDNdtnaSr8cE1AyIGq-CaQWSmO9a9V8Xu2rbL68uwalBrO6tbrBmVhnbja7ZpJwJU6XXLs3RQU1nlwpzE6ZAcGB-7Pj7Gyl-eCsk8dfwBkwMyyJhNNSa-bA-g-7jj0amoQCJsElBbEjI5eBUvgB2P03R8bLZayY1j_4Bz36suIFgQ7HOQoo2zV0wc8Xx4vJBNB4SqiRmKtZ2rrvkEbnIQCgVPg63lxnkcHIIewHI8jlJuBLVqkrDJdK0hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=K2vtPRl2DELt6tM4Tx-guukEAqd2yi8mAfPhtjcw3DzdsQvnXVCorsmLGr_tp-0_Z5kOiycps_e83mGuacEFqeNhLQGSDNdtnaSr8cE1AyIGq-CaQWSmO9a9V8Xu2rbL68uwalBrO6tbrBmVhnbja7ZpJwJU6XXLs3RQU1nlwpzE6ZAcGB-7Pj7Gyl-eCsk8dfwBkwMyyJhNNSa-bA-g-7jj0amoQCJsElBbEjI5eBUvgB2P03R8bLZayY1j_4Bz36suIFgQ7HOQoo2zV0wc8Xx4vJBNB4SqiRmKtZ2rrvkEbnIQCgVPg63lxnkcHIIewHI8jlJuBLVqkrDJdK0hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1pgfTeC3Khf-SRhJZ_clJqOYE5pwVyx0YolmSbCEo6Xwgo0cVu0X6CAn3PH6g-p1ehVP9oL_8JVFmNrou5c_3uaJDZtGiwBqiCQxWUfFN5XjKSP_UK8o7ooN8IrmGffNOrUlyA9hAxmUAzRXEdoG2jpg8lqsuRKzDLXdEgS2Zgza1sCyhCkXsD83B_hCXMmdseFXAaYJjubbfsYtPpIhz94MrrM2-bSUQTqIqp2fcPHb4Z-8uc4wciSQ0J_XNtKklV0fqQOuEGfCSvQgPc3QM_b5KBZIbRDvzdYv8IgOE6m-XY5rcgXpxUghJBxDKtwQH3_8opCukboFCWJcGOt_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gf442lBzcj3hVYSvsr_G-mxzsa7eRNGxW7LrekeidMiF3JSEgwPt9pY-_5DrwmUI7e6r1qZPCuYi0sH5b5Mt6HODqw90RwmpL8FeGMQdlXNuMQDJ8Lix3EjOfMY1RxLm9qBVjacrl2pmOxW5UVNB8Xxn-bGm7aSHXjIyHu9OYxFJEIiv1XmIKc_pL7alsKPhv0l-DIEdK-F2CLx1LDp4jANlrFRnwQXruKYrDyOqwUV2FO23MiU3m-Ud7_4P5a7g2bU4fAlQgPgmDssIt74xmRtcevmDmNedzSMu4lCfGPvpCHKWQ4jhgnBeWsMUgkpqMWlZIzgCIVTVNUyvVbGetQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWjvWJS5dJJsQO2fAxUkYYA_EMppTmLACIwPqVPjOsXh7Oh4d9k0pWNuOagVE_z6M_GR7CfqQcxQ4DR4algnryg_FYE3J0MNVEyggPy7IXTILacT_baR4zGRFc8SL5icMdO_WpIhZbUMaRPsZ5qzNc5zojIqH-Kmsen2pGHkcT3ZWI7JM7F7RYGXvLFGLLskwE_A-Vzl7wIdukgUy2TixDTCV99yJRAAUuO7NVDlulDrcZNPV7UuEeUBEazp_oqZ2y_GwOMrPYvqBvITtMcvq97iyZe06PlEYQAzr_aFxi0mjkYkjJ9APx_Aow86XyaHhNXHC8Z6LxtGm6Bgw0kgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7N0594nd-wPRimpvK6ks3CLJVVFUTuJ57FzWRaRwWOk1rVdL4jMtKblAqgL4yOLG8G__gpNPZskynCe-SgJXz7K0akIaGZ9BfDGhplI7b-IX-CwBIirj86oeEbPVJAPBkaNmZlBejoa5-Z8aDT4aXsSjeJcIgGHHe4eI7hev5h7gmfTU_4ylZkrlC8-LBAZFxyHTUoug4Rh3T2VVwTg3eLbngqtrXwP8D9n5XssWLdb200Li1vGYgDMAq8jZp42a5OlMFa2gcGVyc6nwFVCFFRVpEK2sapH-arSpWmTVXSO1x22zAoYwd_KS0QaBxz3n-XkvBT-0QXWiJiy_4sYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBAlUoO1O0AWduM87OmTp_7f5YheizMsOGEmoNhf_foslRLqBMoSVHjKa6aJ4hyVFhYfSIWg6FAfj-boWu2PGBGZeGFTDbunqq5jr2DF1ILjojle4ouZlt-MZKLbW66tES5WtxnzLFbbrW-740J5Znk__QuTh1sJEQXdRLHaN7mvvJ4izQ1v7_INvKU25y90tYHh_eCZSEsfGlZ_nHt6rgPLD9B8AmLJ3C5buZhRu04JxQDMBbqG3tZkn6dzo7y9yZrzDDww68lsAaVvDwF6LpZiSmev1jO1WwvEHTpqPtramshK1LuVAzU3R1_QPR4jV-zLnAOaZeLE3X2zUDuYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=u2h58VUAH9NCgNjtDNFFLPBAHVWE3RbpseAf4BJzTQV3nsjG7OdrwyX8i1pF9M0XpgUCRCqVBWqj6rY-f_emjY_B8nJdwfK1TyF1ZatIO_hfmXhv2-2po5J26MkhPBm5W3yfCCxdENpjePj9_MtTGR1i3arVK8OAmWR1yMoPdKP6GunVqu--B7XLfZkawgZETimV0EgriLw-M2IOCUdB9xAzSSD4z5M7fYHtPYT4QKx8S-LKPQMEVegqOLjZmjeUaGpYxfFb77IOu6CYQCaevFW78OHJCyAvdVBrPekIEIQj5svdJLP-iV2u1PDZI2zUosj7vrI5CV9ffbsxNrhB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=u2h58VUAH9NCgNjtDNFFLPBAHVWE3RbpseAf4BJzTQV3nsjG7OdrwyX8i1pF9M0XpgUCRCqVBWqj6rY-f_emjY_B8nJdwfK1TyF1ZatIO_hfmXhv2-2po5J26MkhPBm5W3yfCCxdENpjePj9_MtTGR1i3arVK8OAmWR1yMoPdKP6GunVqu--B7XLfZkawgZETimV0EgriLw-M2IOCUdB9xAzSSD4z5M7fYHtPYT4QKx8S-LKPQMEVegqOLjZmjeUaGpYxfFb77IOu6CYQCaevFW78OHJCyAvdVBrPekIEIQj5svdJLP-iV2u1PDZI2zUosj7vrI5CV9ffbsxNrhB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PatS9coku9R3M83weWP9nnphkwpeESB4OQ-YJw-uD92Jn2L3j-DM_d2cJFVVZr7w3AbPFDG8MjUzzaHAc4rUayNxgZ9KxX8xEeoESneno3qww_mKYaxLzYT3BaHde6teFQU1WS2p4rx2SJSWQOCIL3gq8KTQ4hSYnEY_wOAVaJzaauIYxS_EyeRxT6rUVGRi93UXZXzpfFV7jBERUxugPDkahbnrD6saBK1_4Dxf7RkVRhzK_dVL-8dSeKmuD_UYPIUeo-nFLAu2qUbmStsPBaqAzs0Xr4tUDQb-h22cXz9k9tFpyvayB-IsRubxpD1vmzfZ6m-yy9OpT0dNCrEy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=NK_zQXDguSAbkOdX7b7pSM3fkBdXM8sxgBZyIt6M07t0165CKgZEeU1J4-HoRAFUDYallP8nKVbNUwCBj4CIxHbUTdTtml4qsSQ9L26wGfq8i2Uk19VTNdRJ6m71YxzWND2NL7MZDK3qkoWhdg1ZV5nbFlOqlqXyAq20CyOFb-O8fcE7UzWQBV6fF4dwYohLTQfgCI5bxP6niYti0ddTZQasJjNO7tSll27xO9iUgMOEk85jDtjXdbyYLqgl_0ICf8XfNUlKO2_syO_BTopy6EPSb0_UKli8xvMsvSVHiJECDuQJDAhCcAT_iozxSZgXHYzyXhkX7b4oii_RtjJDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=NK_zQXDguSAbkOdX7b7pSM3fkBdXM8sxgBZyIt6M07t0165CKgZEeU1J4-HoRAFUDYallP8nKVbNUwCBj4CIxHbUTdTtml4qsSQ9L26wGfq8i2Uk19VTNdRJ6m71YxzWND2NL7MZDK3qkoWhdg1ZV5nbFlOqlqXyAq20CyOFb-O8fcE7UzWQBV6fF4dwYohLTQfgCI5bxP6niYti0ddTZQasJjNO7tSll27xO9iUgMOEk85jDtjXdbyYLqgl_0ICf8XfNUlKO2_syO_BTopy6EPSb0_UKli8xvMsvSVHiJECDuQJDAhCcAT_iozxSZgXHYzyXhkX7b4oii_RtjJDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=Vf4DD0QdSPrvjLvOS7B4wcT2lXRAsfDxj6kxjhRfmOBULkJ_VZimj3gKs4KAE_OBkVNtmGpZ_Sc9cSpYF64yDt1_Pu3KimPDepL6hGW6qeq1vNKm3MrpybzmbvvcdnDCxD9kKyJR0GHRbwr5IVebRRVSz67vbCjBSjAgzyK3jjGTveSnqthfXUhPaBi597ODWlurzuw4p03Q2nEGjMljc6fEEJWbEP0fswykL85nmfuYSJHp4Ycu1ThuuKXKpnm-II7g5QbPGcnVBFyn8eZfGJPF7yb2SHZTvf21AehXjEgu3RHB1I1vT0LDYefcw_36iI6rQuPSI8cyt0iWdRhRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=Vf4DD0QdSPrvjLvOS7B4wcT2lXRAsfDxj6kxjhRfmOBULkJ_VZimj3gKs4KAE_OBkVNtmGpZ_Sc9cSpYF64yDt1_Pu3KimPDepL6hGW6qeq1vNKm3MrpybzmbvvcdnDCxD9kKyJR0GHRbwr5IVebRRVSz67vbCjBSjAgzyK3jjGTveSnqthfXUhPaBi597ODWlurzuw4p03Q2nEGjMljc6fEEJWbEP0fswykL85nmfuYSJHp4Ycu1ThuuKXKpnm-II7g5QbPGcnVBFyn8eZfGJPF7yb2SHZTvf21AehXjEgu3RHB1I1vT0LDYefcw_36iI6rQuPSI8cyt0iWdRhRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHpVBiAVyP73HATPb5X0B-h_nffsiU9pWXDWbfuwGNYyBw2XtHfTsYo-xn933quchIt6Avv_eTt0OXg3AE_vzvBH0Xy5jzy2hN1PRtLTYNQZkJTaqyGfMrbGXoen2DpIHedQh5O92Ob2Gpu8lpV7f2YXeJ5hUdQnWcttQ9RXhFvsIfBPU9coFFckFu8byHLVvAcZXPU_Z6M4nzD-FHBFFpFKk73QJrXeVul32oSIxb5ZkI-uQ9rjvP0aUGdyUL5OcbS5m9rBBRM7w9qgHFxTEWIamZR3wGs6fDMdn98CmF-fCtVfw6tz573xqRUJpU_44LDGdLdv8H7XEK2Tv1N_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsl1IkJgE69UvBNHEEBc-KEBZFKW5che6ywwo86wu_SpBxJ_LcjNDg7RLE1dXA5-_6XDBs-DxG8d6Xm-nWWdcl6PCf_enyaX-0z298xPDYQmhAuXiSbr27ejidkJn31FYQJrWmoR_AOqkP1FXlYUVJKSqcNrDDycJqHAIkMk8_TCQF_hUUtHgZEe_Gk7yXTLGDSz2ibg3gRLK99GB7GRk8wmfuzHseFNNwPaWL2dK-5S_rgeFkBGXK2_3PQrzFoOEwS3MqaFDv84Dr_7YMSXYdkBfybc5t44JRj6P5UsbKSYcmy3ae7h5f_AUVKLqp90b8zNtXvEekZn8k5ZYvwkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-pP9ZKjz4Vf1Vwuo8-N41dJM5qpJ6CkjwVriTjA0LdYogbLMix58xpllNpM99qz9h_2Mf4UaFCOO6DODNW9P025t1d9Ujds2t5IzRonaK296z3sLElCKpQMGQZr5mMCi4JJPGs_meFz65TPaijbcn7RdKIfl7UrMck0EtUxoR0n8qhvd78DZfHN7irV8Obrsq--sfo01QlEE3AyN2n1g-zL0dBLELrMfFARmC87IXdWVqfEu4zaPZXy4H8KqS0W_zdo94dX5Ltxj9hNZ1pImQAzbFpT2c9nViRxAaBPJzahp_OBQ5l7_K_edo2R7m9_JiMstuhd47znPaEzP7pe0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lc6MEEIZCMaZyklUN0aFyPJDiNC5idMHeW4lnYoE6bTVpCpAmLEx6YGCZ2K-1eiVF8AOBzj7EDVuCNRiaWPNZrXMdsHPgwKSSA0SRNwaav_oy0idwV_3hDQ9wGJOct-bORgObNL9iqzXrSpkcvMndGOezLcnJ7171nFlXWVXSSgNUrYnLRfRILuNx8rfcAfE0EGyOezEe8aMKNYebViy-7aCMFwCH7_JI4J-Gx3tkQaqFx4z-Jc0r7kdRcQOzSo3s9kMLmVxan2BwxgcJQMFgxXdduS_5aeiK4cHe5_Tp4Ty80CQ-v1egsMqlLtLvUwSnhS3aUpSo5-XGTawClZlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ok6KH8lcwzCkf1nAzeMHwI7FqUZWr-ggpO0HcP93mXvjtSJ1czAW35uNR-0DxEkn6G2DXAd3Iyq48GAoLPRyfP1S5HfisYK9Ow_eKw1AfQrX6jfXd7Kr0j8Sr3zOmcjsllRgFOIFg_6ERJumTqe6LYwEImwei1UoXGx2zCanlc13qRPUtHRCJ2YIkF4JHXjGcG4BG55Xok_LT_xxIk-Tk5t7oxl6Gce6OPkc3WNbYCcAB7AzkndYq24XZp1O8Yts1pRL_cqLtAA6CE_Cx18GyFuEfyEsfAWRdlrMu3OZ6ujGyufqjqUyoX4LC7WOB1i_OD2QCHQkak5MP82eGd7pIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=iD1q8wfvLwUO0PNIidQLlbVQblIXBpLl800EKUXQdBH70u-X2MhWFdRPnPR3f7J0tH5W60UmkMc2WlbiS2_DUKnJui7UA47uYZ4L6RfYe6I37AtRWqGcPn1LEsX2rXjqdQvRiH5WUrHuwYBBSsTICrvB24qjT_DwgpoYh-dm_B0UarNlxsgqk917FqWw0cit1ZDIscAUA0KBTPed-1d--WV9-anMKm3irqh5qffSyqAEI8FDtI223y_FRhRvK6WQSH4zz3cwlBgAT1w34BaV7vVM4c_UfGy6PRTfAUzJ3oFWfYqMpTsnB_saRm_z4YEjcpdc2JvhQU__Se5yS_-9_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=iD1q8wfvLwUO0PNIidQLlbVQblIXBpLl800EKUXQdBH70u-X2MhWFdRPnPR3f7J0tH5W60UmkMc2WlbiS2_DUKnJui7UA47uYZ4L6RfYe6I37AtRWqGcPn1LEsX2rXjqdQvRiH5WUrHuwYBBSsTICrvB24qjT_DwgpoYh-dm_B0UarNlxsgqk917FqWw0cit1ZDIscAUA0KBTPed-1d--WV9-anMKm3irqh5qffSyqAEI8FDtI223y_FRhRvK6WQSH4zz3cwlBgAT1w34BaV7vVM4c_UfGy6PRTfAUzJ3oFWfYqMpTsnB_saRm_z4YEjcpdc2JvhQU__Se5yS_-9_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_6jpYnIXFZ0Sl3e9awSbUCRTFZ-q-gsjnBq13tu8gvXmuB22IE9eZ2F7Xx_-eddPsSqTowF9mnBV_8rwqguZmZ-jn6wmglfpeE09oFEq71c8nLhiJRLf05sO7PcnbiUaG8AWr_u5iQ-uXBs_F-DcZUhPE0jb92IGf5oaxLJNLugy49trVvEu73s-dz3SfWJVl1oB6R4lR3phPuv8yEcWwB5U18NJG5vFJ6iCW3MV6_GiBA0YruS_qRtyb4M0GjNV6WZPD8so1QMSVGeQhfOXlWeP9rhcgL9Nlyyx9pGNMM_ayzrsPhorajY_md-Gc_yoesJ5PoxYben2doR0-hlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=SRt7f7yV5zI70KxcDPvEZK-Y1NG5bc3rgnEA2xPjd3NgOXeVUK6wrb_4H1jAlazpswY5FBJMlGc9d7phrshA5AIOjYf0sJvoMMDh9HwmVyRm0lC1SHRO_pYyItxTxk4VQv-craVww7i-_LqWqwasWAd3dyLquY6NHpQc1cySou9drUEU9fE6a2rMeG4pGrGaONQEHWjr0xIF4IFuCZIEYkFjxzC1iGJr0v3P48MvPxsHXaeX4zMdsvzTwk0TAtkz44DdfusVPyQJSXIZ2JcLrfOatP4o1jkCvrHpKEwC0peyxIKngY_VsS28m-exMoAeTvT8dFrJjMFcQNxpWraX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=SRt7f7yV5zI70KxcDPvEZK-Y1NG5bc3rgnEA2xPjd3NgOXeVUK6wrb_4H1jAlazpswY5FBJMlGc9d7phrshA5AIOjYf0sJvoMMDh9HwmVyRm0lC1SHRO_pYyItxTxk4VQv-craVww7i-_LqWqwasWAd3dyLquY6NHpQc1cySou9drUEU9fE6a2rMeG4pGrGaONQEHWjr0xIF4IFuCZIEYkFjxzC1iGJr0v3P48MvPxsHXaeX4zMdsvzTwk0TAtkz44DdfusVPyQJSXIZ2JcLrfOatP4o1jkCvrHpKEwC0peyxIKngY_VsS28m-exMoAeTvT8dFrJjMFcQNxpWraX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=dUhMRUy68T8u6RC81t_IbT05cOTeNKCOJ0tlxC3FRkpfjmK1IT0CYo7z0H6IwygI6zD3-Ythk-dT9_KZ7aDF2OIKpgBY9R1vnTM6GU4zf6qgVZ0kO2ncFrRyzIVNUWJ-l3u1k4wmJ4KoRr7OCCtGx1nqfEsCLpAyH5ntol3ziYFAwxhw1iqtGTeggF4UsHZMDca245FTSjO9Llbc1IJ1hdUGLUcFV6ynO4PZY4HZpj7gGIwfAxGglUPN9tHMEIt9je-rt_7qXwKE_ikZrlb2oz0KEuqpGif13yqe6BsTOtyLGZ4F9yRCemzovyPzaeoX478y6qywGuPHFDytM4nhBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=dUhMRUy68T8u6RC81t_IbT05cOTeNKCOJ0tlxC3FRkpfjmK1IT0CYo7z0H6IwygI6zD3-Ythk-dT9_KZ7aDF2OIKpgBY9R1vnTM6GU4zf6qgVZ0kO2ncFrRyzIVNUWJ-l3u1k4wmJ4KoRr7OCCtGx1nqfEsCLpAyH5ntol3ziYFAwxhw1iqtGTeggF4UsHZMDca245FTSjO9Llbc1IJ1hdUGLUcFV6ynO4PZY4HZpj7gGIwfAxGglUPN9tHMEIt9je-rt_7qXwKE_ikZrlb2oz0KEuqpGif13yqe6BsTOtyLGZ4F9yRCemzovyPzaeoX478y6qywGuPHFDytM4nhBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sU4LEVEW2C3MN-wkk75_of_pJIL_FpMSnloK05WKSuSQzPYm_91Vlg7VGduCMh_3Z_kMD5N_J_4R9h01ObmPxlIkH2OFh9bCsmZpJNGnN6N2yITA3-MZLVQfbQxyr1qR8ReqseSvoZol9mOLiqMEe5N6hA2Y3hLTKUOPuUUA2RQ_-c_NbnirKfpUG6ATEBk3N1Xmss_T4BUo9O3naRZmEpdxC3qs7DEJd2byHGa3ITZ22ULvk-9R2eXbq74Y6t_0EMBTZPTY149faGIKASB6aD8ufbzUUXDXPkbscgwhieEM-xqlIQnVt95R1RnuGIhxxAkmWrmwEhnthRoolp5T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=Rel8tZDiq9pdshc3QtM84_8vRV-hL4s7_HOknu2mg8KHTLl4UWtAn9IQ8kqR8poUQxis8RFMWORuKgVF2ooRd6RJQtDc0G0nGz2tmj6EfTj6afpZd3Yyksdl5OtbhTNWztj-OMMuIX3G7G3vBGxIrfHg9GBGQymkZZGognw4wqYnzJHNxZUA-BAGzT2SjmO_gftnozhO38CluB_c1VxtgxiZ8surA-ACOuw7vtntwvPuUuD4YgykGbLR0M9d4hT3_h1k-MOnAHiuS3ieGnLRRo9IcQQCNNXWwGqAXUYJSuZ7SfMQQdjBikdJlcAv2KMavtyM-Va1Kzw99Wug35i6jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=Rel8tZDiq9pdshc3QtM84_8vRV-hL4s7_HOknu2mg8KHTLl4UWtAn9IQ8kqR8poUQxis8RFMWORuKgVF2ooRd6RJQtDc0G0nGz2tmj6EfTj6afpZd3Yyksdl5OtbhTNWztj-OMMuIX3G7G3vBGxIrfHg9GBGQymkZZGognw4wqYnzJHNxZUA-BAGzT2SjmO_gftnozhO38CluB_c1VxtgxiZ8surA-ACOuw7vtntwvPuUuD4YgykGbLR0M9d4hT3_h1k-MOnAHiuS3ieGnLRRo9IcQQCNNXWwGqAXUYJSuZ7SfMQQdjBikdJlcAv2KMavtyM-Va1Kzw99Wug35i6jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDtySuQmT5IJoEFKHFHuZvYvIEbLdbqeILQq-4FSlWFeL-V7LnMnIySIHSunThKy74aS1kZnDLhaIXV5kJ9sPF_9On9s-j_lk2JOfh1tVLfNrePRnUvU6SoofUi3EN3CAWyEFsre0EOfinZRtsS6rX8ciwxYZsU3vodkoyE_LXJ32renHa_7bdHTwzjUJdcOZEEb3jy2SRhCxgZR-aVrxUVZtMrEyU6DYI-tAZVMpi06GNPZVdvj75em9_0b_sau5_g6DQ9GxBqz1_IQwgw8IwGC2gzxUW9T06CnESL0v8Bw6T5aFHQvLAevu0YDhygCzK2-rw4kCEONIUCWNj-BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=o6vRwUvEq8oD4P8rF5omxzdpLRr8ysEeGdEgJd6jEPw0x20NIg6XUmpZjxwAM7efSjdrifKFfrv1TnIMdV_L1CN6s_jkqErr3zvLk5B9Bvx3LWZ6qgMSW2e_v3NROcebA4OBEmmujYvqaPQCycrZrVYjAC2zA5C-CUwAL3OEhebcqwUyHAvjPP_I2PahogAqMSO99rS77_Lz4ruUqfHTDj7YQpUUauLAt74KIOoz0yh8T3oi6_ZmzevcQXjW8buWFngBsMvcVYJ2anDOOi9LbPG-blWvCDQPqVUUjr9K2nDp09bbfKttU0VJyXAF_gPAGY6Cal8vRa27flxjG610pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=o6vRwUvEq8oD4P8rF5omxzdpLRr8ysEeGdEgJd6jEPw0x20NIg6XUmpZjxwAM7efSjdrifKFfrv1TnIMdV_L1CN6s_jkqErr3zvLk5B9Bvx3LWZ6qgMSW2e_v3NROcebA4OBEmmujYvqaPQCycrZrVYjAC2zA5C-CUwAL3OEhebcqwUyHAvjPP_I2PahogAqMSO99rS77_Lz4ruUqfHTDj7YQpUUauLAt74KIOoz0yh8T3oi6_ZmzevcQXjW8buWFngBsMvcVYJ2anDOOi9LbPG-blWvCDQPqVUUjr9K2nDp09bbfKttU0VJyXAF_gPAGY6Cal8vRa27flxjG610pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=o8ckpV1DKqq8wejF2o6HAxEkXmqjZh3LOUg-Z-lb5sXAwzp7-SPehdX7BdlEixpt1zC0FMkA2Iui1RIx2OiKqsbqK6xTotQUUxGQv8ejMFSJx1YdjAIFWVl-W2e5gXxi7NPPjlMH21346mBzFMWWYQW0frI2JN539BHEM9MNuU9Erd9Rv0mJqm45O_yQfFD6Mia6VFNbEJLHWhF4Zowmz-U7aZ0hJDQUG7ChTy9cOvCpaOG55LCUKxc5Enl8pi5YyBJhl8AOhiUE7ohlpeQ7JxIue0Wxy01Yl_vrmrWXPmADU34tlLYW0_dpnSGkVR5WTrd0CiSL3t8IeNXQD1_WQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=o8ckpV1DKqq8wejF2o6HAxEkXmqjZh3LOUg-Z-lb5sXAwzp7-SPehdX7BdlEixpt1zC0FMkA2Iui1RIx2OiKqsbqK6xTotQUUxGQv8ejMFSJx1YdjAIFWVl-W2e5gXxi7NPPjlMH21346mBzFMWWYQW0frI2JN539BHEM9MNuU9Erd9Rv0mJqm45O_yQfFD6Mia6VFNbEJLHWhF4Zowmz-U7aZ0hJDQUG7ChTy9cOvCpaOG55LCUKxc5Enl8pi5YyBJhl8AOhiUE7ohlpeQ7JxIue0Wxy01Yl_vrmrWXPmADU34tlLYW0_dpnSGkVR5WTrd0CiSL3t8IeNXQD1_WQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
