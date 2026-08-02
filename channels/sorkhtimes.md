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
<img src="https://cdn4.telesco.pe/file/XNtvGQNRq6bS4W15dE53VcKLPbvsc43h6hOWtQym9qQDC-792LwZ3R7Cg40OOyTl516bm6u_SYOFz-fSmlgra1g0K1NgDix3sqXuCiCQ2ru7VyBE2wmVt6l05XJwkgF7KTxUi5uXv_YkeXlND_bZ8DJ84aWVGcytZNcA-tt4RPkOIXCFiUSOyDQvsnFuE7jTkO4XKfOoLf63npGB-vo7hB7w6sxHdjFVIF18iibNpk2Q-qe2Th84yEARqtyim17QcfwHC5yZJc-VHPdpw6rhA4Q6N30m5LUh0XFM5I0oMWvQ-Hm8hUStcVMEu_EdkJ7z00F5twdF4Cz_dNvTkcXZEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 01:54:17</div>
<hr>

<div class="tg-post" id="msg-137253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVULSXznGlcnee7RkGNZVXpWQo5Dka7e-AgJkRTAlbgPyMetBkidmSOHXzjHbZGlzsucSiQQA-Heb_vR0pihkkWvmj6un5INYoguLwvLl0nH5BUi9zHWElNC6eDPbXAXRPe7RpGiZTOgzGYJjy-n59Ar_9RRvy5wpV9Z1mbe9TYdQ-VAfCJ3c7llRFE44GkM6A9c9-Cq6uAainiirIOfafqE9YSvuqXNi3_WstXiBWQaVZVOyrlLQHm2O9RPDHsPZrHAxo3DFmKajoGmbgcd1U8Zc5MrSKNA23SSBdqJIH8duOnu6qVxA9Na0zINa9trHGMZX9pEMKhKrpVteeo_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
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
<div class="tg-footer">👁️ 487 · <a href="https://t.me/SorkhTimes/137253" target="_blank">📅 01:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
🚨
طبق گزارشات اکثر سرورا و vpn های رایگان از کار افتادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SorkhTimes/137252" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SorkhTimes/137251" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
طبق گزارشات، اینترنت ایران امشب خیلی ضعیف بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/137250" target="_blank">📅 00:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
فوری به نقل از منابع داخلی ؛  اینترنت بین الملل به شدت ضعیف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/137249" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/137248" target="_blank">📅 00:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔽
🔽
🔽
ایری یک قدم دیگر به پرسپولیس نزدیک شد/مذاکره نساجی با جرجانی
🔽
🔽
نساجی با درخواست مجتبی حسینی مذاکراتش را با یاسین جرجانی آغاز کرده
🔽
🔽
بنظر میرسه کار انتقال ایری به پرسپولیس در آستانه نهایی شدن چون نساجی علاوه بر جذب جرجانی چهار دفاع وسط دیگر هم داره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/137247" target="_blank">📅 00:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚪️
⚪️
⚪️
⚪️
شنیده ها: استعلام اولیه باشگاه پرسپولیس از فیفا درباره جذب دانیال ایری مثبت بوده و مانعی برای انتقال نیست اما پرسپولیس برای اطمینان بیشتر، یک استعلام دیگر هم گرفته تا تکلیف نهایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/137246" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/137245" target="_blank">📅 23:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
🔴
کادرفنی خواهان جذب یه هافبک بازیسازه درحالی که هوادارا برای جذب محمد قربانی فشار میارن
🗣
🗣
باشگاه هنوز روی جذبش به نتیجه گیری نرسیده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137244" target="_blank">📅 23:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
✅
فوووووووووری
🚨
انتقال ابوالفضل رزاق پور به پرسپولیس به طور کامل کنسل شد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/137243" target="_blank">📅 23:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
‼️
نمودار ترسناک و فوق العاده غم انگیز... کمترین میزان ازدواج در ۳۰سال اخیر  و کمترین میزان زاد و ولد در ۷۰سال اخیر! سلامی تلخ به پیری جمعیت باید کرد... از هرایرانی بپرسید علت این فاجعه را چشم بسته عاملش را "اقتصاد فاجعه بار" خواهند نامید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/137242" target="_blank">📅 23:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/137241" target="_blank">📅 23:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
🔹
🔹
نتایج پرسپولیس زیرنظر تارتار
👀
13 گل زده و 0 گل خورده
🔥
🔴
پرسپولیس 3-0 شهدای رزکان
🔴
پرسپولیس 2-0 خیبر خرم‌آباد
🔴
پرسپولیس 1-0 آلانیا اسپور
🔴
پرسپولیس 1-0 پیرامیدز مصر
🔴
پرسپولیس 6-0 ارزروم اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/137240" target="_blank">📅 23:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjLrGfw1By7KZuGUxWn79HFa_QaIWW94_M3hJMDxvjki_JDL5Srzk_JDToPxTdHcYhy94laBFz5-xEmdPS13ZB25KogPinGhFjvjtZMRYFPB_dtgKZy3s5NKekRxc-s_lzlLfANEToR9dMhX5_NPRebvf38ch1SiJCkxA-FUzsWm_IWSUSu3vkIt9MAAuuOo0H9HjvSrgU62dFB6nvyhogOcVEfU_K-n_MEOx4HbwEYsRcXW-Lxds0TdNJSpXYxS1xQAqgh6Q7BCwzm1XMgYSIX7AQH7dgwLy340h_g9PQaclK_tmy3Nr8dPf0y-PVd4OZgI9ii8NHS3v5KNriKz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/137239" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9ZDde4nZKAVVB83vjZ804cpLyKXA51Nsu0Bag2ulSBh1Uuu-vCgpPZtwNzj9SPN4x6vp0XsUANNqyEYmMjdsjmsqP9kJJGPuxDlge_0KBUuyqlWQoUZ2eLCiX95VXY_EutWCb2vsvmgkomRVGTtBzyiHUlcOZxCajq1xAucOrYwah3DsTerBAxc2NTF-_OC83pN_nis-b05WdpvG95MrQSwEEuC_rfUAShCETyNiywjbCbZnBbyrz4FcaFiP1tTZiUnHLexJdcaEtbZ9QrJ_1uOR_5NOBVUBQA3N0r57w26nMxXCClD193KnczTFd5kJBRDZSOF9CBtJzrwP3ogSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
لهستان قهرمان لیگ ملتهای والیبال شد
🔴
لهستان  مقابل آمریکا 3 بر2  به پیروزی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/137238" target="_blank">📅 22:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjjUOGkciFed7mTg64OpwczOafErFK_O2FJzO68OP26QknU34bo17BbopxSLorWvqssDmvnWpQBTbb1zXH1YeTtPmGIwIHorUbLdPDhkggExSYSxYeNzGvc45RlLvLEcO9TWYUK450pYZPrrGwWBzHkdYhMKz41PAojlctwmFRc5csXpU6jT_rWC-jE7CaEF2J0LYJp6gKNSHu7L-B7FKNIpVdQ2yOlE5rnaZCqtb1mSd2H4MTdsnhubAZqlaGJajmgO5WIjTcMNB8w7rmkvRIfQPwV3CDUgp-A6O_NVpXrktLhlHw6sqYv8ySv9jlJWcvhSr27QIrAeTNuqRHCuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
فینالِ نسل‌ها؛ فریتز در اندیشه جام، جودار در سودای تاریخ‌سازی،
فریتز و جودار برای فتح جام مقابل هم می‌جنگند!
🎾
رقابت رافائل جودار
🇪🇸
-
🎾
تیلور فریتز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 997 · <a href="https://t.me/SorkhTimes/137237" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/137236" target="_blank">📅 21:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137235">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
ورزش سه: تیوی بیفوما تا این لحظه نتوانسته خودش را به تارتار ثابت کند و در نزدیکی درب خروجی باشگاه قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/137235" target="_blank">📅 21:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137234">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚠️
⚠️
⚠️
قدوسی: خرید سوم باشگاه قطعا در پست هافبک خواهد بود ولی تارتار هافبک خلاق و بازیساز میخواد و خصوصیات قربانی بیشتر دفاعی هست تا هجومی. باشگاه قراره به زودی در مورد قربانی تصمیم گیری کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/137234" target="_blank">📅 21:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137233">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/137233" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137232">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCY5CC6RFWkOsZJKhwVudPytSCypze7aqUeSfVn_ZKeDOIFeX8XPeBDUURZGXfupO6poQJE9vy2NjINUCkRaq8w6xpO4J4yVBiRNxXytqFWl4T-Aqv263dA1ycYX9Iyewuu9-lcvFQUxltsaA97sNs7G2h-ALtcem2hTVg6LU2ucJAe13bknMu2DCov9x7WVNdA1PVQc6NBrGXs7Bna1hDzHbnCWCPa6m8vZUBkPM9KEYgydyBy3uBCynVfrxsiQNCqG3iH4dNdmQcMwkyUzBwYgoB69iMsDgEoW0AYSJ11Wi2PbLNK3NNa8_0FdAzSlrssJT46af47VeGmOlwBbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/137232" target="_blank">📅 21:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZkAK5BpVuzgauzh0VnQYUkU75zY5SZ33OounEzkh7IteZFgEb04auCqQOUG7gvyz7-c6jmNrRKGDrFDH2DBI95CujZhTs9dXiCxEP8t7vWkkLDC-bhjB1D-TOlLUcU6evOWFN5GYw-fldnTei09WKVM3_KCLGh3ROSKO3v1ngUThp4h8XKX8LFyDopDe1neCV1He_DPcEHP7tlm9-tFvhfQe1JjqHLPw87REsJWZrDwYBZeixbB2JTGz7Caw8rD3xHDUH8Z9qhBrySwfOyvxlnai0os3tUXUA4WQotfh_u7RltmuEM1dqfcWmJhwE7PVkCf3E46HXnf8cLFj-bVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
به‌به بازوبند‌ کاپیتانی‌ رو ببین چه بهش میاد
©
🕶
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/137231" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏅
پرسپولیس الان یه دفاع چپ میخاد یه پلی میکر…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137230" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137229">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏅
پرسپولیس الان یه دفاع چپ میخاد یه پلی میکر…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/137229" target="_blank">📅 20:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137228">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⛔️
یه عده گاب میگن حدادی وعده اسکوچیچ،هاشم نژاد،حسین نژاد،ترابی و دانیال داده بود؛اقا بی زحمت یه مصاحبه بیارید که یک نفر از باشگاه چنین صحبت هایی رو کرده باشه من نامردم تا آخر فصل همه شونو نزنم
⛔️
چهار تا کانال کصشر برای جذب مخاطب خبر فیک پخش میکنن در نهایت…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137228" target="_blank">📅 20:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137227">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⛔️
یه عده گاب میگن حدادی وعده اسکوچیچ،هاشم نژاد،حسین نژاد،ترابی و دانیال داده بود؛اقا بی زحمت یه مصاحبه بیارید که یک نفر از باشگاه چنین صحبت هایی رو کرده باشه من نامردم تا آخر فصل همه شونو نزنم
⛔️
چهار تا کانال کصشر برای جذب مخاطب خبر فیک پخش میکنن در نهایت…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/137227" target="_blank">📅 20:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏅
در مقایسه با رقبا بهترین و پربار ترین نقل و انتقالات رو داشتیم ۱-۲ خرید خوب دیگم داریم، تیم تا ۷۰-۸۰ درصد پوست اندازی کرده، تا تیمی بودیم که اردو خارجی رفتیم و برخلاف سال های گذشته با تیم های خوبی بازی تدارکاتی برگزار کردیم.
🔴
واقعا موندم هوادار دنبال چیه،…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/137226" target="_blank">📅 20:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137225">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
هم تیم حریف و هم ما با ترکیب دوم مون به میدان رفتیم، یه عده خود تحقیر دنبال زیر بغل مارن، در صورتی که تا پارسال تو بازی های دوستانه اگر شکست میخوردیم تیمو به فحش میکشیدن…عقل ندارن یه عده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137225" target="_blank">📅 20:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137224">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
ارزش تیمی که 6 تا زدیم بهش ارزشش از استقلال، سپاهان و تراکتور بیشتره
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/137224" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137223">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GySSUtwad7TNAtNtopvW5TPn_5Hn-87awyD9T9Wo0kKO2DUW9KQCfoDYPUVgTJ2XOOZUqtV_dSKu60L8a6NUdxU5dz4oN3pmGExjJr6fcOaNKaNB6Wmz2GJwSyctA5O2K_HHpdTvx-Vo33RaRPknd5fWt4gpGPqryxf7j20j1qaBhTyQNqoQAjm2-I7xxtOB1RpfW1WKkUI0XLeFttH4YGdCFWug98H0WQpIok4R5VgL1xeAqsuBucTgi8NqtKKS-h66XLlGu0wE7rC_Eeqg2vEmp28IwVcx8wIgHb8UzlLp7VVhgq40lf1g0-nVlyaX1c6Z9Zp07bZqCbCgYnYLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارزش تیمی که 6 تا زدیم بهش
ارزشش از استقلال، سپاهان و تراکتور بیشتره
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/137223" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrkMm9lTbfclgug3fLUi9L2jK7i4JlCG0BGxH9SvT-yTW-5rk18y26_c_83-g6kwGYREwxYvtO5jHd-0dPp0-K84XkfFkbsrkyHlDEGcmVQQWctL8mMyUXfuGyu2dEihfUHtba9RHBPRPA-xI1cz37XZWKz8pr-Bagta-5aZ07bn42Azsm8itMlgpfReqZb7tKu_4gXgT1X0HKONpFRAxnguNJb8qGzLkDPiWbMQKKwHoEQcsET4l0XPH0UOpu5SvkyEZfpXGa9e4hOtPPMHSn_wD143pcgbDE97TOhAC6aLLB8biVnnsMCMKtRrCBvZ1oj-kYmEw-JgplVNvsqhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🤝
مهدی لیموچی، وینگر تیم فوتبال فولاد مبارکه سپاهان پس از مذاکره با باشگاه، قراردادش را به مدت یک فصل تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/137222" target="_blank">📅 19:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caXB0WjDl6lwzN5SCe5E2MfjB1iB8DwQAmOTK4xQBo0wplJlHPfihPGPMpC6xDQx55q0SmGosel99h6gNfQvGjoSi4hSRE7mNnumtDw8mjrk_lACXEJLXmj5CRqKUxdYDlgkr2Tqk2kzSZcPL_2jcJ5OGU3OiAhePr3Z8bb6mDWyzQdS2GbivzU21yICh4HpN97oiwF9NO6U0_n_XBM3dWR9JDjeK5rXs4u-eYFEKh0j1LCGNVRelIe_uhWo0x7EZAItnExhooQxIpLFuuzSk9ghaky4dFTIXmxy-GUaBWAsMZ82qRNZPnqv1pxjYVSvJ8UKrC8nL0XDIEmMwvsv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تصاویری از شادی بعد از گل علیرضا همائیفرد پس از باز کردن دروازه حریف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137221" target="_blank">📅 19:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137220">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5ZOOZuyPx6TkfTe4DKVQmNeDwFrPLktyfpesK9Z75baJffO3Kn1S2zEmCmkvnbHdaE-tuHVbbjhLyTKsyMLmIMKkY_g4nipiNSuS2RP-2AzfAOIhZYxAfu6YOU8kesQ0PRB2jS30pzb7wq14T_IqL3nyoOU26gtRORr37ZoQzzBm2WvP5P8udD1yHtZMC4n3kFDQiFM3eioAqX67NAF3wj8WOMB7P2J3W_Qfgmyy15yX4U9YBu5OE8IIzAXulRCYvAYZuUm42FcSvyf1fHW0pbF7ufZwWTLRc4-ZqLtG4rvMRCa4Gmq-9IKFxGBRYXSxynLBBjtkTZUvyVj1zODGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✅
رسمی؛
نیلوفر اردلان سرمربی تیم فوتبال بانوان پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/137220" target="_blank">📅 19:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🥅
گل‌ها: همایی‌فرد،شهرآبادی،صادقی،بیفوما محمودی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/137219" target="_blank">📅 19:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
پنج بر صفر جلو هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/137218" target="_blank">📅 19:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7QU3RQ84mp8xWQA97vhtD2cbECbpCvqfVeU4RgLAZLBvpAft7g7MaLvNTbU56cKVeUp_tynYcpq1TMPco1rlQAcDm04suFaRCBC45f3e4kFHXkRhtJ23R8o9A8XIh5-NvFMp7lhpsL4Hb--zHdDcGZMnHuRc1FufTNYxxGItYcM4jmBskM5oPtKZRmM8f5zv7TmZzkh1s6pTnHTg8uEEZBI3u9AjsdOSdFTTVaUSeoC-bikypQDKagYuyvB-m0oUPXoq0hzrajUEnvYaNKO1KI8f-oze3xc0WD78cR4pnNX39u463pvMaNuNwhOnJ7B2zuTPnZbsX8ctBXBdAHbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر ارزروم اسپور در آخرین دیدار تدارکاتی اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137217" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">▶️
تیم حریف…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137216" target="_blank">📅 19:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_njiRsLfOFYDce8S4K24pgMiTA5S1D6BCb6ArJKOoYJ4QYJtAALlPEvmWTJAKukYDb8HOPRd9BW9niTFu2YzoM-rmbFguHXEdSkYZzueqFQx7GDHsvcINogL3SADvR3xXJpxTHpbjhL7JhN_Y5hmDAAwe7JtNwvWOKdzUujP0TLQ7S1vKAwhDgxXRNspc3b6rz-9tZzBX56di2e_CgrfAYAuEdg69yS1pE8-VmpCmz_u-svJI6hZ5sxwBFntB3Y2FBneeCvdSfq5s37XO6GY4ZlBJtP0vnyzXJrdaMEK_ANOEbKIK09RABWIC4zWX3j0lf90xNiDObqZNYo2Hv4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
تیم حریف…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/137215" target="_blank">📅 19:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f27def464.mp4?token=WGnHMarMRTAldweD2ycpvoNgW0oaUYqbOhJ5X0vT7W2ANlEdKkQGCWFCdVpCjTa9c0uAVKADQf2wjQho1c2g_13rW8rwxY3FMw9TbkJlO55yZ5CPunmdOPo3oNHuUPlpGMo5DKFCkoT-LU3ryZ0uagLK-viCCAWPo1jrScq_efeXn5FJyYXZuVRkG3GWycDCHQZUt0MgRVvFVDMdn6TQy2pU5izLag9IPzRh7zdFs6S4__Visia6OskbHjuOnUMbS4qz09rMIEPCYZV7bTg0Y7Qh4aCdq6-Fwl-_IpV62Y3ceKWI0cL6YUq0nKF7aJbCOyAjZKYA_7EuDrGslMhUeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f27def464.mp4?token=WGnHMarMRTAldweD2ycpvoNgW0oaUYqbOhJ5X0vT7W2ANlEdKkQGCWFCdVpCjTa9c0uAVKADQf2wjQho1c2g_13rW8rwxY3FMw9TbkJlO55yZ5CPunmdOPo3oNHuUPlpGMo5DKFCkoT-LU3ryZ0uagLK-viCCAWPo1jrScq_efeXn5FJyYXZuVRkG3GWycDCHQZUt0MgRVvFVDMdn6TQy2pU5izLag9IPzRh7zdFs6S4__Visia6OskbHjuOnUMbS4qz09rMIEPCYZV7bTg0Y7Qh4aCdq6-Fwl-_IpV62Y3ceKWI0cL6YUq0nKF7aJbCOyAjZKYA_7EuDrGslMhUeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خاطره جالب پیام نیازمند از شکست دادن اورونوف در بازی FC 26
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/137214" target="_blank">📅 18:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
با وجود اینکه همایی فرد از شمس‌آذر و گل‌گهر پیشنهاد داشت، اما بعد از درخشش در تمرینات اردوی ترکیه، تارتار با جدایی او مخالفت کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/137213" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/137212" target="_blank">📅 18:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🔴
با جدایی رسمی مرتضی پورعلی گنجی حالا قطعا یک مدافع میانی باید جذب بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137211" target="_blank">📅 18:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/137210" target="_blank">📅 18:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
شکاری با استقلال مذاکره کرده و با باز شدن پنجره احتمال جذبش بالاست و اگه الان باز نشه زمستون یاغی میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/137209" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🔴
با جدایی رسمی مرتضی پورعلی گنجی حالا قطعا یک مدافع میانی باید جذب بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/137208" target="_blank">📅 17:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5XI-dhZISQSHm4aDTVoCcq5PWHCwvDgyTX63EtJSt43cK2ZLU9jdRYHhVxu-H9WUbNxS2XVy2NhhFsC3hdKgee13w-89SEjwEd1gkaAqxBXmZZVjHH6Tl6i9lFVWCMah_BELGER_YSbCxeuUZ19c4d7F5Z-uIi0bGFA-7pnsQxw7kGyQsDgg9mkA_9oRZPdbXfiwKJUKUfyUsXEk5eX-n1RvMVZ9hNrWEmTOvBMwgGC7Q7vEZNKrXRkyqyeE4EgtK9Ze8cCuEBgroJrolKgtAwTw5m_Ny0OZiY8euWw_spdosOECQ2cOrCwf0FKSmzI3XTmah1bcVGShq-Bn9nImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
فینالِ نسل‌ها؛ فریتز در اندیشه جام، جودار در سودای تاریخ‌سازی،
فریتز و جودار برای فتح جام مقابل هم می‌جنگند!
🎾
رقابت رافائل جودار
🇪🇸
-
🎾
تیلور فریتز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137207" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇮🇷
اعضای هیات رییسه فدراسیون فوتبال ترجیح می‌دهند در صورت برکناری امیر قلعه‌نویی، یک سرمربی داخلی دیگر جانشین او شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137206" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پخش زده بازی پرسپولیس  ارزروم اسپور ترکیه/پخش زنده به صورت لایو استریم هستش کلیک کنید همینجا راحت بالا میاره</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137205" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYZo1t6u_GBd1WEu8wVMYZh1b7lNkrc6kGHejV8EVlV331ZGeRDWZLJToOO2IvJDteWpY7Sb77kVGt74y-pzbg2rCxoTDaYSNP2g3ZujNkTJOmLA4o0lCGcqrfnqNvU6YgZmsQdBXoKU85_MpsketUMn5haaDjBY1iZDLaZP0G45x-Fg1o6xzvvM6JH_LxfJRo8Njecax7y8w72xTFqj1Qj4dCZj2NdvEgBYMKznxi3RQw9gxu5CzlFM48QrZOvUVyBlLRPnWER0BE_SEpOnG1OBL8W3MOG3Ko5XcnwgUib56YeN5GyuwqFxZ_HJ4k2Eoz9aqIrTP33pTbKfF7Wc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
💚
مهاجرانی، سخنگوی دولت: با خود آقای فردوسی‌پور در تماس هستیم و ایشان جزو افرادی هستند که به عنوان سرمایه‌های این کشور محسوب می‌شوند؛ ایشان و برنامه‌ای که خودشان ساختند تحت حمایت کامل دولت است و رییس جمهور دستور دادند هیچ سایت و برنامه‌ای بدون اجازه ایشان دیگر بسته نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/137204" target="_blank">📅 16:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز بازیکنان باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/137203" target="_blank">📅 16:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137201">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/137201" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137200">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtRimlOD1csA5dj8iAiqUFzSAwT_3iPc6Zvy0UT9o6g9E8cBf3XMsCijJUVY0bX-D3Aeo7DCMWxyMnXGdNkOOfZ3ZqTACSsH1f5WFiM-4b558CrVOMA4ZffBr486sAMDYUFXsWDxxRhdzbHTrUXWbNqrJSX_sCg2q67o-6KT6R19sbkiSLXEP0sgZl-08DFncWsHUPpZHvKIpx86W2KfQZ6y1HWqkwBF_DWCdUxMT5ZcE7KFi0vEzlF7fNdQivhg5P_jrqBKAeeL67-QiewTR_3QedpwQ35NfpTrwwAy5xrgpuwHLhqlY4bzGdvGqXwOGT5WwUh3bkEAw-CBYmD35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز بازیکنان باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137200" target="_blank">📅 15:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
قسمت اول چالش پرسش و پاسخ سرخ‌ها در اردو
⚡️
بازیکنان پرسپولیس در فضایی متفاوت، اطلاعات و سرعت عمل خود را به چالش کشیدند.
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/137199" target="_blank">📅 15:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
تارتار در اردوی ترکیه به محمودی: با ادامه‌ی این روند به جام ملت‌ها میری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137198" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
در حال حاضر سه ورزشگاه در تهران و شهرستان‌های اطراف وجود دارند که امکان میزبانی از مسابقات لیگ برتر را دارند. ورزشگاه‌های شهدای شهر قدس، اسلامشهر و ورزشگاه پاس از جمله ورزشگاه‌هایی هستند که می‌توانند برای برگزاری مسابقات مورد استفاده قرار گیرند.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137197" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
تارتار در اردوی ترکیه به محمودی: با ادامه‌ی این روند به جام ملت‌ها میری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/137196" target="_blank">📅 15:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137195">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✖️
✖️
✖️
تارتار:
⬇
⬇
تمرینات بسیار خوبی رو سپری کردیم بچها با انگیزه هستن و صد خودشون رو گذاشتن
⚪️
از طرف همین جمع قول می‌دم تمام شبانه‌روز خودمون رو بزاریم تا هر سه جام ممکن رو کسب کنیم
⚪️
همون‌طور که گفتین ایشالا دو سه بازیکن دیگه بهمون اضافه میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137195" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msZxB_xDh-V2Ood08C_RXJDq7zAp_7CMvkYeqA4yTkG9CQyifLiI0N_HhUCqCmzIaK_LOxRhveXnWx4DStxxUTHIu9T3lbNPZnJP34BnT6seM5kSnaNIOz9dCTQrdEq5UMU7t-KxK6qvQoOKqsW8rpDN2qFobQjOIOfauew-LOxTbN1AHaXg7E7_xyWx3vTwZB4HxZT8_im1JOxUzQHqqc_Zg89ERsHhB7IuVuXW8dhTiYZo824RbqOGdE6MHQ714Bv-f6U4Gw7DUSnGUaF-38a-5ibjhjof3sodH_LvbcPdZr-Y6hm2sjUH4sSzaZ0tGMuKsjSoawPuAZEcijAvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جدایی به‌خاطر یک پیراهن پرسپولیس! امضاها با شست‌وشو پاک شدند!
🔴
پدر یک خانواده در شهرستان سبزوار پس از آنکه همسرش پیراهن پرسپولیس او را شست، تصمیم به جدایی گرفت. دلیل این تصمیم عجیب، پاک شدن امضای چند بازیکن پرسپولیس روی این پیراهن بود؛ امضاهایی که برای او ارزش احساسی زیادی داشتند و با شست‌وشو از بین رفتند.
😔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137194" target="_blank">📅 13:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
سه ورزشگاه تهران آماده میزبانی هستند؛
⚡️
ستوده‌نژاد: ورزشگاه تختی خرداد سال آینده آماده می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137193" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
گفته میشه ورزشگاه آریوی اسلامشهر هم به گزینه میزبانی تیم‌ های تهرانی اضافه شده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137192" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137191" target="_blank">📅 12:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137190" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
الوحده برای فروش قربانی ۲ میلیون دلار میخواست و با رقمی که باشگاه قرار بود به عنوان دستمزد بده خیلی زیاد میشد و حدادی از جذبش منصرف شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137189" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH_obOGarBqp0UjXXRZ-J8SAOOduA00rofADKjLcRsWKjiDlwT216cMnLbq19glv5bFSRvS9rrGUHW62O5Ea4xK-90t-1qUvchhdFg4zz8aiU76TurnpLpC6Ic_bkakx8Ll0j6aB9P5WqsETvxClr4wtp-wTTaO7UD23WnvBAOtuadhrSHEX3SujIIWfEXkmAQ9tyDxg2PMSPicY775W5jcSoJbRQTIbIFfApENiC9eu8NKyvVCHwVweEqKdBh7g_4-nJnu2ELCQuSXAaSK51up0L8o-dMaycord_VJnQAkrF91WShtXJfhhnAStvkCcjXSCev4n72x-s4FJUwR5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137188" target="_blank">📅 10:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137187" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
محمد حسین صادقی امروز با مدیران باشگاه تماس گرفت و اعلام کرد مادرش دچار بیماری صعب اعلاج شده و اکنون در بیمارستانی در شیراز حضور دارد و به این دلیل در تمرینات شرکت نکرده است
🔴
🔴
مدیران باشگاه پس از این موضوع پرونده او را که به کمیته انضباطی ارجاع شده بود…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137186" target="_blank">📅 08:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💢
💢
رزاق آخرین خرید پرسپولیس در نقل و انتقالات
🔴
طبق شنیده ها ابوالفضل رزاق پور احتمالا آخرین خرید سرخپوشان پیش از شروع رقابت های لیگ برتر خواهد بود
🔴
رزاق پور امروز جلسه ای با مدیران باشگاه فولاد داشته و به صراحت اعلام کرده با‌توجه به شرایط حضورش در پرسپولیس…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137185" target="_blank">📅 08:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
ایالات متحده آماده و کاملاً مجهز است تا با قدرت نظامی، ترور و توانمندی‌ای که از زمان جنگ جهانی دوم بی‌سابقه است، جمهوری اسلامی ایران را سرکوب کند.
❌
با این حال، ایران و سایر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر طرح کلی یک معامله، هرگونه حمله‌ای…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137184" target="_blank">📅 08:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
فوری/ ترامپ: به درخواست ایران و کشورهای منطقه، حمله رو برای فراهم شدن زمینه توافق، متوقف کردم. ما کاملا آماده حمله بودیم اما حالا مذاکره می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137183" target="_blank">📅 08:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
ترامپ:
✅
در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137182" target="_blank">📅 08:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUrLOqeYtoVNu4kFmBqII4C5jwS5-FQlFFpsgWdYuUBQ3-pJiqHiLrGGGIokCWFaX3sfPNx_8hEuEnhBMogr3ztQ_rkKkTYlmHWI_ZCgyM-rPAOC8c64Tu0Zcdr9vvwpEzuvXlgnTzfj0SdBlX9c1ncrSm9AcczyJ_s4ASvByC1Io26KARQ5Fqi4qKhpCAPYAoVkwVftNn6po66FI5LalP5Uz378eoc9WDay2Gx0sTmDtt6VetvmX5TLJtCGPEQGLbqznRvKGd635AkT_eLLugWQT6SaOF8Pixr7Bg5V_RVVtqxsptxnbtvY1Lk4Of7wvtdJwz9B-lG9fEcWr5ve0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137181" target="_blank">📅 08:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQCCtnqI5r7rojzO8vuHzlLT5gQ7Ja_FC5pJv7sVCiLRMt7Qy8OV3oLETti0t-mQovuMdyEGn2eKwCCA2xLhZmiHt3xD2iYAgMjEqliN2qZc8KmoAf2ncbe2rBKMcU-AfHII96sDIG3QavjMQJFR2Wxj7NKpG5qNyuo0Swceh_wfmAUCqy1PUJfykIP43m4DTVJ5hUuWK3UvbtLnbaItCTzhOoaKjr4byM9yyP7AW0Z8B6HiligSXizcXWpJ5luOAKoFjLggEDgpGALrSaNCfTyqgkzrMHEndv_ES-znT_rlDDRsgudDF3CL39l3NBKrv4F0euuh1UVpY3BJQAhJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال غول‌ها؛ جدال لهستان و آمریکا برای تاج قهرمانی لیگ ملت‌ها!
🔴
فینال لیگ ملت‌های والیبال ۲۰۲۶ بین لهستان و آمریکا، تقابل دو تیمی است که با نمایش‌های کم‌اشتباه و سرویس‌های قدرتمند به دیدار پایانی رسیده‌اند. لهستان با برتری قاطع مقابل آمریکا در مرحله مقدماتی از نظر روحی دست بالا را دارد، اما آمریکا پس از حذف ژاپن نشان داده در بازی‌های بزرگ توانایی تغییر روند مسابقه را دارد. انتظار می‌رود کیفیت دریافت اول و عملکرد مهاجمان در توپ‌های حساس، تعیین‌کننده قهرمان این نبرد جذاب باشد.
🏐
اوج هیجان همراه با وینکوبت، یکشنبه ساعت ۱۵:۰۰ دوتیم لهستان
🇵🇱
-
🇺🇸
آمریکا به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی دیدار فینال لیگ‌ملت‌های والیبال با بیشترین آپشن، همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137180" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
✔️
مدیران باشگاه پرسپولیس موفق شدن‌ با اقدام جدید‌ خود به توافق با باشگاه فولاد‌ برای جذب ابوالفضل رزاق پور نزدیک شوند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137179" target="_blank">📅 00:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137178" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137177" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137176" target="_blank">📅 00:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137175" target="_blank">📅 00:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137174" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137173" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137172" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
❌
شاید مرتضی یک فصل دیگر ماندگار شود....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137171" target="_blank">📅 23:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKuMTkHrZ5gKvU8sOX6kWPJ7rvRyHcmx3TxpPbjB1CpeCVd5tkn5-ZagzQqnklK2Im5xqS0P7MBQk-Ig-q45640yKqz0Jko4dFI2r5Whd5JXEjJCoES-T4Nt3NsQ5OvBtfLONRWYd-NRdGPR3zG6QltJPnhMw3eP-Rr5lprWcVMTBC1RN0i-sN112DZ-o8jQJiFcEH4KjV9iCe9W9CcDA4YJTNmJGHgiqgLImNCugd_lqcvCcSWO1bryB1r3VDbX2-43xeu-EXQ5irg5-vob0ASaLqAwSi71Bh_VggsVszR8t6m8Gbw2tAd3_fc57VuS7uaqmWBmWO2G8-A87Zx7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
علیرضا اشرف به عنوان مدیر رسانه‌ای جدید تیم فوتبال پرسپولیس منصوب شد و بار دیگر به جمع سرخپوشان برگشت
💛
✍️
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137170" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔄
🔄
🔄
حسین‌نژاد نمیاد پرسپولیس/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137169" target="_blank">📅 22:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
⚠️
باشگاه فردا میخواد برای رزاق پور نامه بزنه و پیشنهاد معاوضه بیفوما و 80 میلیارد پول در ازای جذب این بازیکن رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137168" target="_blank">📅 22:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚡️
⚡️
علی بازگشا: پورعلی‌گنجی فعلاً بازیکن پرسپولیس است، اما درباره آینده‌اش هنوز تصمیم نهایی گرفته نشده؛ باشگاه هم سیاست جوان‌گرایی را دنبال می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137167" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
✔️
علی بازگشا: پیگیر شرایط دانیال ایری هستیم
⁉️
در مورد شرایط دانیال ایری از فیفا استعلام گرفتیم. دومین نامه خودمان را به فیفا زدیم تا استعلام بگیریم. فعلا نمی‌خواهم جواب استعلام اول را بگویم تا جواب استعلام دوم هم به دست ما برسد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137166" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🔴
🔴
🔴
دانیال ایری مدافع تیم فوتبال نساجی در آستانه عقد قرارداد با باشگاه پرسپولیس قرار گرفته است…
⏳
😀
البته ذکر شده که این قرارداد به صورت قرضی است و سپس اعلام شده باشگاه پرسپولیس میتواند با پرداخت مبلغی این قرارداد را دائمی کند…
🗣
🗣
شرطی در قرارداد نوشته شده…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137165" target="_blank">📅 22:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137164" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137163" target="_blank">📅 22:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137162" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
محمد ربیعی هم  در تراکتور ابقا شد.و خبری از اوسمار نیست
🔴
قرارداد ربیعی بند تمدید داشته که در پی توافق با باشگاه تراکتور فعال شد.
🔴
تراکتور نیم نگاهی به اوسمار و طغرل ساغلام داشت و شرایط و وضعیت انها را بررسی کرده بود اما پیشنهاد ارائه شده جدی نبود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137161" target="_blank">📅 22:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
ترامپ: هر کشوری جای ایران بود تا الان تسلیم شده بود اما اونا نشدن، من اونا رو تحسین می‌کنم. شجاع و سرسخت هستن ولی خب تهش تسلیم میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137160" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📎
📎
تصویری از جلسه امروز پیمان حدادی و مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137159" target="_blank">📅 22:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
❌
فوری از ورزش سه: دانیال ایری این هفته با توافق جدید دو باشگاه نساجی و پرسپولیس سرخ پوش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137158" target="_blank">📅 21:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
#فوری | سی‌بی‌اس نیوز و به نقل از مقام‌های ارشد آمریکایی:
🔻
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است؛ اقدامی که شامل برق تمامی غیرنظامیان نیز خواهد شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137157" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQs6yfEPpVY8jk6tO-k5f448MWSKUWQMy9_woD5K2mJvGP3n1CjRzxC6KcDo4XZnsOVi7uGzh_fwhV4UhBYUSFOFHgYp5Xh-DmTRNP08CP9VlxCR7ZUOed8hinFmMyJ1UPOESICvA-X9g6oUNgvIDxP7zbWLlE0TPBfsDHX8w78cVInbOtB7RZpEXwTOOlEo7iJQN-2-sCPHYhm1km-cqKalR_HjjUVhXhf-e5Fh1YvzuyJcOxC8KeyGx2OShFZjEAD5Cy77Y8HH_QR-xAtyNaALlkD0tsnKvloDo8m5kG-EiL8un_yD6ef9UowKGChu_osutI9gi68cv-RRBMDvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
گفته میشه ورزشگاه آریوی اسلامشهر هم به گزینه میزبانی تیم‌ های تهرانی اضافه شده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/137156" target="_blank">📅 21:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
⚠️
فوووووووووووووووووری
⚠️
⚠️
صحبت های جدیدی درباره باز شدن پرونده انتقال احتمالی دانیال ایری به پرسپولیس مطرح شده و گفته می‌شود این بازیکن ممکن است در این هفته با توافق مجدد بین پرسپولیس و نساجی به جمع قرمزپوشان بپیوندد.
🗞
ورزش سه
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137155" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
با بازگشت مهدی ترابی به تمرینات تراکتور، پروفایل وی در ترانسفرمارکت به‌حالت اولیه بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137154" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه: سیزده سال از عمرم رو با عشق به پیراهن پرسپولیس زندگی کردم. با کوله‌باری از خاطره میرم. برای همه شما آرزوی بهترین‌ها رو میکنم. کسب قهرمانی ها و کاپیتانی پرسپولیس، همیشه در جانم زنده خواهند ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137153" target="_blank">📅 20:55 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
