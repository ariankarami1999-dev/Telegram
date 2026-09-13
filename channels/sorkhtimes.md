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
<img src="https://cdn4.telesco.pe/file/FBMilpdKStYOPJKEZBob9hArFyw4wKXQ-hk_zLhS4vGwPieZVJmwQQI7TNdazBFd3_0qIFKAAQdRCY1ztiazVFYKANscflFJvdLAMs8UD4wOt-NnLUdHCcl8Ib81SpKAzCuqK_A5aRoxDuoA0Lh647Lb_ZaYN9-Fo1JpBI29tA3hBWa0GQbOgVSzZHybV5UjoYjAE29Mdrv1-YasyamaZ6cUO_WgkQVvnQye-rk3vGdoOYmc7jDBigIjMJuecpK9Rkz4jeGepOe7oYsC-IFiaUiTAJBIfvP4iVECLng5Wf3APp5L2Pl4GO6AGWd3UYr2g5OY1JDAvOBj52e0EVvfzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-139990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 183 · <a href="https://t.me/SorkhTimes/139990" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
دو ست و فعلا باختیم و واقعا زورمون به ژاپن نمی‌رسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/139989" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
میثاقی:
✔️
مهرداد محمدی یه چیزی گفت شش ماه محروم شد اما خداداد چهار ماه؛ ساکت الهامی هم شش ماه محروم شد!
✔️
یکی از دوستان حقوقی گفت شکایت قضایی این موضوع چهار ماه زندان دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/139988" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbQtEELfoHwhHj3EzMlnhxcGTp3xgnNj-CGIRLhWseRXK6Nuxe_Ak9BiWqytTeLqfCjA-ao9k8ca56WTX8dcda4Yz-ILLKaD92DQJEiO-zpkNtCNdzhDpQFbvAT8EyCM5I3fDZ8kSuJa73Jdh0XBJ84smqVSYM_UUTuNRh9WHHTAYSTvnwNJBC2RegckRQzty1uMcmI40sJAEU-6TdclyrN1fGKca9TLYmMMYTVlIdWv909kzfVC0B9H1_X0jWlLuZ6to5VcX8bOO8-ghXX9VAvZ-N-eDlJDSPOWWcZ7jV3rswEsdnnxdLABN0u6omT-2eYMCkmSRiyo1sHD758AhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پس از آنکه محسن خلیلی در ابتدا اعلام کرد: «جام حذفی برگزار نشود بهتر است»، حالا پیمان حدادی برای چندمین بار خواهان برگزاری این مسابقات شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/139987" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/139986" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/139985" target="_blank">📅 14:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/139984" target="_blank">📅 14:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEqt8DRkWyF9YQTOpXcRVmwb2Cz_fnUzvw1N-Z8zMmUHnWn0qhLtO5rwM-iC0819iquCRLGeYPxi9nNx_F7P4lrp_YCOE2TyKMBawAfOHbSyj4E7sKMLh0KAmchBfqcJISFVU28fbj7QhHEMNjpPjOBoNkMPj7o7-ug8n2RhlRB-DzLnI3slYCRHOknIz1RMr03Fqf6s8X_nvomTfDdi1KKfDWfdcgqtiRSn3-Ipe_aLC1UGiyrestjeecIYbmKwFVnz1HlmgbSnjn1MBmT28aI8W0wcGV_FHPj_cY6tQVUziO8K-RWOAg8uiWRXhAechq67150bgkNR-23iu7JL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Man United -
🔵
Man City
⏰
Tonight 19:00
🏟
Old Trafford
🟣
منچستریونایتد در اولدترافورد با تکیه بر انرژی هواداران و ضدحملات می‌تواند سیتی را به دردسر بیندازد، اما ضعف دفاعی‌اش نگرانی اصلی است.
سیتی با شروع قدرتمند فصل و خط حمله آماده، کنترل میانه میدان و فشار روی دفاع یونایتد را هدف می‌گیرد؛ دیداری که پتانسیل گل‌دار شدن دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/139983" target="_blank">📅 12:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/139982" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
💢
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/139981" target="_blank">📅 11:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/139980" target="_blank">📅 11:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139979">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=F1kNAYwwSjZbeVOe8hB69cnxqcRPQ75B0-7a_akMqH8MV_4SkI-i0qd_SOuLWroLz2TKfPOdRT7h-f6NmRiSHwVe3-OAME9X1ckt95afBe25OolKCCYRyYrsOgNIeI-T93xIdr2v7uQcbylCHr3mJ619ajWU3vO-yk-6-_cCQKX2Wq0xevyI5iBHytEwfrfDVikHfDM71uvueglpFw-vIlcmBG2IP-8Hug2kqDqePDly2phbqISm66HuPnf4wReTlXGu3XS2VorDQAQWjlcv6Vep8nYoJIw2jM0iI9lpbDbbx0354LiZzKKKF60y03uPtFlCmOXY1Q5dDv2kiPjZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=F1kNAYwwSjZbeVOe8hB69cnxqcRPQ75B0-7a_akMqH8MV_4SkI-i0qd_SOuLWroLz2TKfPOdRT7h-f6NmRiSHwVe3-OAME9X1ckt95afBe25OolKCCYRyYrsOgNIeI-T93xIdr2v7uQcbylCHr3mJ619ajWU3vO-yk-6-_cCQKX2Wq0xevyI5iBHytEwfrfDVikHfDM71uvueglpFw-vIlcmBG2IP-8Hug2kqDqePDly2phbqISm66HuPnf4wReTlXGu3XS2VorDQAQWjlcv6Vep8nYoJIw2jM0iI9lpbDbbx0354LiZzKKKF60y03uPtFlCmOXY1Q5dDv2kiPjZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/139979" target="_blank">📅 10:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA-RQEBXYU4ZdiyQEufujIxwLIkupph08DAR8lyrMt9AwUwa2OYiadZ3Pq1EWtSYizprLo4IRAdB5jMQ0dP_1PmopJDFf6AL9MxTfMVWr3aCHP1OkVdC1gbq41tL3MdsxwVFWDzyGP1WmFF-PsOtyfcWlLX1DJzV5X6I5wr8ioEIWx1td5J0Li61YJvq2ABsIh6yLNhSywsEX7xKyGvXQ2e6rgz3juIjy2UDlBI8W1tzQT9ah9qHnmljM1dqBeboAN_t901I1O46eQox5T6zHXD1bNuUBAmDdOzxud9eFfH0uypNXmaupi5ByGIEbcynAZW1bJzTWgiUuvahNk-X4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کاروان تیم فوتبال گل گهر امروز برای اولین بازی خود در لیگ قهرمانان آسیا مقابل الجزیره امارات راهی تاجیکستان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/139978" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHlH2VOE-kS65K0Rfo12I1vKlVFkNevy4MJbD1c70FPoub0_jveGKEIujHfyc1pKUZadzv3bZK-TSCjBbq7zPcn5kz7cz7II1MUvcQRqMwSKSE_qBgyiTSVgXz4XyXOrOq5cPhPGvG4EFm-FnJ7B3TtQ4CvrepAprYEfjIXUKGS7tUwunKTlmzk4F48t0S__cipcMun8EDEn6TWC68PuxM59SUfYH23YFFF-hmBQDYtEDoUA_N_ENfMnB3Fpxt3Hs4yDsioj4mci8TGqNLn5lIb60Qr7iNM1Kr-xYRHSAnN-GhN4_9Wio3_eYp_DOVdCZja5M3RminWe_tiko8txEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس امروز عصر در دیداری تدارکاتی به مصاف تیم شهید قندی یزد می‌رود. این دیدار در زمین شماره ۳ آزادی و پشت درهای بسته برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/139977" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🗣
🗣
🗣
🗣
🗣
🗣
حمید درخشان: هیچ‌کس در باشگاه پرسپولیس دوست نداشت موفقیت من را ببیند. همین‌جا در خبرورزشی با صراحت می‌گویم چند بازیکن آن زمان پرسپولیس کم‌فروشی کردند تا تیم نتیجه نگیرد و با حمید درخشان موفق نشود.
✔️
✔️
امیدوارم این بازیکنان حالا پس از گذشت ۱۲ سال جواب…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/139976" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/139975" target="_blank">📅 10:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqNm6EFykEIbGW2hdsLWoGTwWOME41G-Rh5qQkiN4BGFL-HNIKs1b9rscIOlHpRv1_pp8SZzI1qPFHfGDqclpjxe_iuM3NQmSbZBjAQMk1eI6R9s82Wv8NAor3KRz0Mr9rOxYzPwhiLYSoqDlIidQ03qvvXK8CWTDTgaa2b9-6mydEPc633pe-WkJlVU6maTLmRc6OpXVqFSGyofVkymUM--4SRa5yuLEB8CFH8dfMHzdZV6T0U254N18d5vYKMxbI9LdI0ly-peamjspBisf9t1u1q-upxJ_d_7ce7lJIzB0kYfzoeQNgDyYp2zjadaCiJXovtjgJE2bqDxi_8zHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗣
🔴
❤️
پیمان حدادی:
🔻
بازی با خیبر را لغو کردند تا یک‌ماه دیگر به صدر نرسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/139974" target="_blank">📅 08:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9pbHTCvXJ4bGa5YcyMCMmvjHb5j25e-OnOAiNm8Y-PgnnFPjItef2v_hqDOXk67Dsx21kn-qjQasolB9XfP2JuzqEB74HfLAgvFY6Vod69AET_h8GHOEuAPE8DLq5cy9odO69khNlzKO8txFcE1DGAV3ZBli-s1lhT5ORTw4AdqLssFYnNHAIEnPnaX-mBn2w45ldNaKKKIhb49B_VdKHc78vS8SNDOq_0Bf8M7_XsZIsuyMkZuAqfK00dD-7ECpVZAAyyIX9a59qKRNWiD4cH-IZm8Uypd2Y-LncRk2SznTT4QA5QXgTWb9hy0iNJuFUEzFnxrB_OdoXu29A2U7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/139973" target="_blank">📅 08:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139972" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=taIA5HTGHLbRc0YjCCkDT5J0adLiQVuLcTnvGH_7CtBRTBP6PRYnZqgX5ILVujP4ga1TNpJsIJJruaXX0pa-_3pfEXXjyyXBiNGLWEmruYBpdmdVrUM5YbkeZlNnjxsRjaLR8tZpnYa7d55FB5ITH5Lm9Zak9XQjPZHXfhKq4MQfeiikQf7o6K2bLBdw49rwLGU6AUaETvYUYO0A2rr998efEvk0h3HJzTyesXV1MJT5ISziZFOkTXeRcm-f5K3wLn2gd57YkPR0nNvIzlbqdWjtEXYyOIQoipr-CDD0EBm7iKHg-t28lRngOeRfe1Lgbad7DuCqgtNtSZOZSbIJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=taIA5HTGHLbRc0YjCCkDT5J0adLiQVuLcTnvGH_7CtBRTBP6PRYnZqgX5ILVujP4ga1TNpJsIJJruaXX0pa-_3pfEXXjyyXBiNGLWEmruYBpdmdVrUM5YbkeZlNnjxsRjaLR8tZpnYa7d55FB5ITH5Lm9Zak9XQjPZHXfhKq4MQfeiikQf7o6K2bLBdw49rwLGU6AUaETvYUYO0A2rr998efEvk0h3HJzTyesXV1MJT5ISziZFOkTXeRcm-f5K3wLn2gd57YkPR0nNvIzlbqdWjtEXYyOIQoipr-CDD0EBm7iKHg-t28lRngOeRfe1Lgbad7DuCqgtNtSZOZSbIJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139971" target="_blank">📅 00:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
‌ ۵-۶ بازیکن از پرسپولیس در فیفادی جاری به تیم ملی دعوت میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139970" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139969" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139968" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
درخشش بشار رسن در ازبکستان ادامه دارد؛ هتریک پاس گل این بازیکن در دیدار روز گذشته تیمش که با برتری 3 بر صفر پاختاکور همراه شد
✅
✅
آمار او در این فصل : 25 بازی، 4 گل، 9 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139967" target="_blank">📅 23:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139966" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❤️
پیمان حدادی: وقتی لیگ تموم شد و به همه جا اعلام کردن نیمه تمام هست، هیچ جای دنیا پس به تیمی جام نمیدن و خیلی غیر منطقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139965" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
ریکاردو ساپینتو؛سرمربی سابق استقلال:
🔻
من با مدیران زیادی کار کرده‌ام اما تابه‌حال مدیری به شهرت‌طلبی و دروغ‌گویی علی تاجرنیا ندیده‌ام.
✔️
✔️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد و انتظار داشت من مسائل تیم را با او…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139964" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139963" target="_blank">📅 23:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
ساپینتو: پیشنهاد عجیب تاجرنیا برای استقلال!
✔️
✔️
ساپینتو مدعی شد تاجرنیا به او گفته قرار است سعید فتاحی به استقلال اضافه شود تا با توجه به ارتباطاتش با داوران، مدیران سازمان لیگ و فدراسیون، مشکلات داوری و برنامه‌ریزی مسابقات را به نفع استقلال حل کند و…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139962" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❤️
پیمان حدادی: خیلی ها آرزوی قهرمانی دارن اما پرسپولیس در ۸-۹ سال اخیر ۶-۷ جام گرفته. بازی ما رو لغو کردن تا صدرنشینی ما یک ماه عقب بیفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139961" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❤️
حدادی: هاشمیان قبل و بعد از پرسپولیس کجا مربیگری کرده است؟ دوستان در یک سال، سه بار او را دعوت کرده‌اند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139960" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: محمد عمری تا ۳ هفته‌ی دیگر به تمرینات برمی‌گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139959" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139958" target="_blank">📅 22:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139956" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqaHyo8o79NeAm0cS3SQi_nPNyvone_ebFjV0UHtoOgy_A6lUpbd3uObydWgy7PjWjY51paSKBGQjdST6UV2jy9IZ9PbL3nwofs3AQqLyye6NGvKjG5_3qm0odfhW2I_FcdNToH6isuhHQutReLfDSxBf0idbjDRAG1YUbf3yf3SRO8hdMOyI20w6meuLOQZO4lRjnGL_AJ5OEGr2I7fS5dX1WJD9vcwdf1OnptA2-DQAKZ-T_7WYhwfvB-IKjvckykxffbj0vCXtGght6Q966lrnwLA5LnXxhsIJOhUQP1Pjn8yYivnnq6BXez9qDW0tUBZkBA6B2R0eW2kBCdk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139955" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6060af132f.mp4?token=DS6x3rw-Z0icq25Et3pS2ENYVOF7fVWeVKG36TAsMWpAf1galU-RG7VSyP8YClsDuPTxmXcBRTGxBkF6ed5sAZyInF7ARipWCD9Ab07cpS4Q237-WTc3EeBP9bLXVeTvLD3XgrtQxla8UZ5xTiJezljm5KfJYVbBW7jfncTvNltPz2M9ydJxIpasCMfY2LSjkfT9cX5YkQyAg0omSaRJ3KCgG9rqlfwBNXSZtFkVs9A__7O2UFZvuTj967u_BTtsTR1vRyXr9adN7EnamXetECOqbh05UXwVr_EQgD88ehlPcXOatLK-G1ltWxSZzkGiO0-DnC0YcXFUCnorSSxfeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6060af132f.mp4?token=DS6x3rw-Z0icq25Et3pS2ENYVOF7fVWeVKG36TAsMWpAf1galU-RG7VSyP8YClsDuPTxmXcBRTGxBkF6ed5sAZyInF7ARipWCD9Ab07cpS4Q237-WTc3EeBP9bLXVeTvLD3XgrtQxla8UZ5xTiJezljm5KfJYVbBW7jfncTvNltPz2M9ydJxIpasCMfY2LSjkfT9cX5YkQyAg0omSaRJ3KCgG9rqlfwBNXSZtFkVs9A__7O2UFZvuTj967u_BTtsTR1vRyXr9adN7EnamXetECOqbh05UXwVr_EQgD88ehlPcXOatLK-G1ltWxSZzkGiO0-DnC0YcXFUCnorSSxfeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:  حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139954" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
السد در 4 بازی اخیرش 19 گل زده
🔥
پ.ن یعنی دوباره قراره عروس بشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139953" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=exOmkYuJvarQnaX9zIqYJu6KM3UgAO8RKt5x2bwOwO7_Lv8GKj7MrEM90_yc7zPm1fIp2bedPQkJp73RbPe7FOBpTKzJF3ZRbUIry3VupDDQI9F6ZSMsfi_nc3hUI5_kn7XD8YuN_7ZGanTs2mS4WFpPD48_1bFSwHG_A29KTkuYx5hG467m-0QSYS16tNJ8V03gtzOkljCKGLO1fw4STL8LuteEgqddcFAbF9cqPCQqQ8Iof7maMa3SjhViUtxPe23-pyl6aV1508vfj4HDI9t_wV1eDMt3D15mApg8Z5p25HnAbqSazPwcL_S-zGF2lPMZ5NkVL-1yJdd1iroL4aj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=exOmkYuJvarQnaX9zIqYJu6KM3UgAO8RKt5x2bwOwO7_Lv8GKj7MrEM90_yc7zPm1fIp2bedPQkJp73RbPe7FOBpTKzJF3ZRbUIry3VupDDQI9F6ZSMsfi_nc3hUI5_kn7XD8YuN_7ZGanTs2mS4WFpPD48_1bFSwHG_A29KTkuYx5hG467m-0QSYS16tNJ8V03gtzOkljCKGLO1fw4STL8LuteEgqddcFAbF9cqPCQqQ8Iof7maMa3SjhViUtxPe23-pyl6aV1508vfj4HDI9t_wV1eDMt3D15mApg8Z5p25HnAbqSazPwcL_S-zGF2lPMZ5NkVL-1yJdd1iroL4aj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: بازی خیبر را عمدا به تعویق انداختند تا روند پرسپولیس را متوقف کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139952" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139951" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139950" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139949" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYqukD--X8yNJUkzMCcXGB3-xJdD28_JAh4uG2BPqVnoEwEJL_a5LaaamDD2G4Sn1rNwYneS3-pZ6tiY-8J8vIbaRckA1oZD07ju8jS45OdU6EKFe47QZj9DdE7ICWXOkobCnF9cW2siJd-ddO5EOuhH6x-qCddkCMhC9TeHUFXBVK6avpyP5BlpsCVLOxq1-v8c1-Cq6lKYdcyE_zH-Yca4VOToznat0fJ8ZAt5Z3aeOSIbvoGsop4-tIqlxPyT3_Tp6u6KCjLKzf_0IoVp1qaVmiSa1Dhds1qxmyAuvSl_1_mnAZ8G80cAq4aijpJdI3asKTuDvVP3YSGSwyRgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139948" target="_blank">📅 20:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fABzdIMJbvcdqX9dJO2YbkzDRaRgvJXQ9degmTtgHH9CojmnuxFGAgSiujxdc9Cwe66IStcBhrDCQ9_Bz5LIYihxVoPPzdrEaGXY8lrgzkTK9eQQxSAp3mHK4-CrvLUf_2GjgqU1MSOBrYWb-8uUFq1POK8nz5Yjc2TCXaT8SZCZqx3Wq0YO-1btg_9qXt054EDMmRaGOQX5S0344OUDn9uZ_e97cUMTSVd7Bncxd6asX2tyhbczdlpg9XqFBol2QDVWV3rvGYZb7WFusVQkI8IblNy5mmk45vwN-NWN0b3ymbLHfaIdojzTRehE2fUrTwgO9l8ZgHAdunRad03VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid -
⚪️
Rayo Vallecano
⏰
Tonight 22:30
🏟
Estadio Bernabèu
🟠
رئال با برتری کیفیت فردی و مالکیت توپ، از همان ابتدا برای کنترل بازی جلو می‌آید.
رایو وایکانو احتمالاً با دفاع فشرده و ضدحملات سریع، سعی می‌کند ریتم رئال را برهم بزند.
کلید بازی برای رئال، باز کردن لایه‌های دفاعی رایو و استفاده از فضاهای کناری خواهد بود.
با توجه به اختلاف کیفیت دو تیم، کفه ترازو به سود رئال مادرید است و شانس بردش بالاتر به نظر می‌رسد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=DaOv1hzYFR4PXkngk0-sdgmHjGwMNcsD9WOwFC_pjcK1C_HGxk1Xp9qthciI0C8HBni51wjIf8n9njw6hvW0suRfKqMoRW8QAadMp0B8gDEdSzOgVCJGXBnrywwj_qoiLL0ySzXD6jvtgZZ6_lWDLvno6TMxiafXXoxYiOIlxwqnVYjOOSDWlcPy7Vz-gwl6gx_xfMwohsJ8fvxR2ljCTLIeuMqZoOGrsWEyCvf3t7exUIu6SlPD2p3-NMUdHo6rR0fcChffBELgUS0PfMPAwaS7FZIPhTn-YkGdbBPxvm-9bslppzIfH0v729FzV2JsXgYFtLEX_-fd0K0NqxI7Zh2Rr6uZjgNKGCQwzEI2WKFEPLMY5eQjWAxYTAjDn3LDNrFuZstYHcah6Yp-nTW3pDd3yT9IBj-zQ0xuU3pib5RSaWnp8zYNDB3z9-sFvYTB6rqfsDRqfp3PyG94beHZ54_1VfSDDa8ST1cEZRlcY-bcTn0DJq7jJ2guNakarq5fYlHxr8YJZOJSWRhjTFugJO1HibzwLWiYiE40p8ex_LnftxqWzIyi05jSZpEoI-qKPLgwSY-3aPX-8d_iSpySANgqb8LdIgqROwSZ5TRnyKKvo0jupJwoG-BxO2E1St-nYJ4rRNq8u-GQJCYGqe4h2gL__iyma4z7n0Zd6YPXHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=DaOv1hzYFR4PXkngk0-sdgmHjGwMNcsD9WOwFC_pjcK1C_HGxk1Xp9qthciI0C8HBni51wjIf8n9njw6hvW0suRfKqMoRW8QAadMp0B8gDEdSzOgVCJGXBnrywwj_qoiLL0ySzXD6jvtgZZ6_lWDLvno6TMxiafXXoxYiOIlxwqnVYjOOSDWlcPy7Vz-gwl6gx_xfMwohsJ8fvxR2ljCTLIeuMqZoOGrsWEyCvf3t7exUIu6SlPD2p3-NMUdHo6rR0fcChffBELgUS0PfMPAwaS7FZIPhTn-YkGdbBPxvm-9bslppzIfH0v729FzV2JsXgYFtLEX_-fd0K0NqxI7Zh2Rr6uZjgNKGCQwzEI2WKFEPLMY5eQjWAxYTAjDn3LDNrFuZstYHcah6Yp-nTW3pDd3yT9IBj-zQ0xuU3pib5RSaWnp8zYNDB3z9-sFvYTB6rqfsDRqfp3PyG94beHZ54_1VfSDDa8ST1cEZRlcY-bcTn0DJq7jJ2guNakarq5fYlHxr8YJZOJSWRhjTFugJO1HibzwLWiYiE40p8ex_LnftxqWzIyi05jSZpEoI-qKPLgwSY-3aPX-8d_iSpySANgqb8LdIgqROwSZ5TRnyKKvo0jupJwoG-BxO2E1St-nYJ4rRNq8u-GQJCYGqe4h2gL__iyma4z7n0Zd6YPXHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
با توجه به لغو بازی با خیبر، پرسپولیس فردا در دیداری دوستانه به مصاف تیم شهید قندی یزد خواهد رفت.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139944" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139943" target="_blank">📅 17:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139942" target="_blank">📅 17:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139941" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFRH9uf1SF9Z3d_7NngY-iaDL39fpk4Qec5PW6K-hRMd25B3fkSxHVwMf9mjWV7iSwcAtC1IfJrQ37wYPLgA9WYxuNxcBlw2C1lrc9rvySZU068ZhruebiR_EKr04nucgW2s_Vb6zJ9ksfncwjVzoanxp14dKs9E_jOn2RkgYry_Y0sghNWzmUfiGaWWy152o70mb-GiG_8KwDdq2m44yDdARTqathVnI9b6wCgjIOVBQdNHehkRbcZcUlwLktfYYv5dBW5udALSRgzfvTZ3JEdUwgbe3FyeTJ887n8GltFlBCV311SHq4OwKvo0GuyKdBV0a29FCa2_-nC1LgcQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میلان در آزمون لاتزیو؛ جدالی نزدیک و تماشایی
⚽️
میلان با تکیه بر کیفیت هجومی و امتیاز میزبانی، دست بالاتری روی کاغذ دارد. لاتزیو اما با ساختار دفاعی و ضدحملاتش می‌تواند بازی را برای روسونری سخت کند. انتظار دیداری نزدیک می‌رود؛ جایی که جزئیات می‌تواند سرنوشت بازی را تعیین کند.
[
آث‌میلان
🔴
🆚
⚪️
لاتزیو
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139940" target="_blank">📅 16:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139939" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139938" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me1eE5GmiRkdXiY8WydDKn7nS-l3Cvybz4KYs_5fyFbdB7eqIV1nTpmtlYVnT1VWiS2P57CR1Z59q-jEHKEe9yZVJRgxwnVlbmM_6Mk4UJzp-2pYGKp3VwJEA4CEj7EKDWvHdxgKwxLfjt5keqzwEHR_Oe-gSw1xm6LqlJqP5yuH5P7v-gpg1Fl2_kkqxwGunvFD5TQB7JWqHQObv2nQqES06fBcivtiu4rLcykWuX4Aqlp-ecRWuPbdWvJUWkzGOYxk3sgSPBCdndXuWmQuFq0O7bMa_OFBp5K722ABN2QvcFANgDxk_cRDlyRwCOklUkywTcHjDds5D6ALB79aHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده است.
📊
۶ بازی | ۱۳۰ دقیقه
⚽️
۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139937" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
باشگاه آلومینیوم اراک هم از بازی کردن آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139936" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139935" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139934" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiLZBLduMLy5KNLyf-S1hDfvgnxktSq3vqmaTDF66ZIJTNooKRiuV951qPgiccVmF83fqJCc0qjolu4b0OcvQd9AA8iaeflHLVzGc0xVUPKQa5iid_db0Q6CUURfFU-thbZo-cEOCA600Oph4pDeyUBQwy7qTqhnB8HWwpsEoxvodpKyuynWWXkLtyUTZ4fXgExxXiFgGTXL6SdwnUC0PE_JqmTtROskmkeLa-gJKLL76XWX8AVg9tg_VRaNzfFyGwgLDwvY4bwhXLRQ2DFSV03ZnHsJfzqRx8ErMQFPc19wAkob96-iW4cYDAJZO9G_6wZ64KSuO-CKYryGGF0TpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139933" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlVPFq66wksFEwLeuWDx0_4w9kA9DxTNdmSCWjFoZay7WKssNX3hVhGI1vxMn0ZSWrkXdKw3x3wWgDCJVdratjEyXcr1rKXchC9BJIoG29eg-ogpM_HS8W0SvO--Z1wYeW-ZdLth4O7gkN3vSYqrQMC9JPHh756gTVyaLih96BbpZNGykWojCYUAMKQLwyygGoz4lAsjfhRh6dw5uoHNmUa49Cs6P-P9Xrh9mfZo51D7l3TClT_58TxwmNOjeqD6vaqAhQLDrhaPTOMkQ0uZyh1u1cIOPayDNFDII4T6Tn9JpWbE3qY53cOcUvylDIaBxNRxCSJVfYfSvZhpghj3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسپانسر دو باشگاه لیگ برتری نساجی (وارش) و تراکتور (آتا) توسط وزارت خزانه داری آمریکا تحریم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139932" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139931" target="_blank">📅 11:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
حمایت از خداداد عزیزی به رغم فحاشی های زشت و حمله بی اساس به فدراسیون فوتبال درباره var
✔️
✔️
سخنگوی فدراسیون فوتبال: قطعا و حتما امید عالیشاه هم زمانی که خداداد به استرالیا گل زد از آن گل خوشحال شده. هم عالیشاه و هم خداداد عزیزی برای این فوتبال عزیز هستند!…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139930" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
پروازهای ایران–بصره تعلیق شد؛ سفر استقلال در هاله‌ای از ابهام
❌
❌
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139929" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
پزشک‌باشگاه استقلال: یاسر آسانی هیچ مشکلی برای همراهی استقلال در بازی برابر السد قطر نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139928" target="_blank">📅 09:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0FyM3OK0oFIWfayg95fEmARtVKZTkznPpz_HoD1OHSguJ1hr761LY0VGsXMCVE4YJhAHBISBP93THEJszkI9F0O8KVd3Ikl0J-5HJBgWWJMlNmXwqCulz0srY4P563p0eECrEMmAQEUN_1dwr12KZgcDhD_0ODwkUWMvMLUHmNeODXEtBjamDX4iRoTOwct--Tl2iTuouud-FhCGh4e9JGTN61CdHoPq9ygcgU5U0wZocbAb8CuaYpoJgG6AaGon08EKjYW_xKvGeQzdYxWqCDmsrj6MjXlRxNIbs7nbc5rblxz3aphMpIXyEiBMUisWiBFvKL-mx_GKMGWrlXSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139927" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZcwngSYMHb8-CjMyRkx7z2MlBzhmVXBhkYpZogGa1hVcDsz-63t80UtcebsxDdHvX3UL9aTx2PeMo8oR-nbM6tNuMuGcjYh4iqPfNcp0KhbVa-uFP1HCq0B6cbpHbSThlFrFxGIe9dm1DM79m8nbmLmdiv263_gQ1yb2jHtUWihqOGCRvI9yD-VHGmq4q7lqb8DpnPumzu_UT67Iu8RphH442j9llNc2t7368VlAQZLSjZm0z-zGNEnDEFWMPzNIF3YXIJ2hdrSdeEb045AXMFkuxQd_eisHW6md3tnp85o8xuZUuJSEYHHLSqOJcaYlq7il-mppMijthMfz1xCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139926" target="_blank">📅 09:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqUZkTdt3KxPog6BFl1IXOz4uuRbgB0E7rn2s2ff06I5lintdNrV6S54AUUhVDtuoFXYPnB9EtJMhJmJj3iy2h6PXH7Uq0mIWTcfTJ2dROgNDsqpFTAt3aG9tLSEaEpLFH7y1UQR8kN8dqlJOdL_0K2SRLw19fTsoLCWPU3_sQstbjo8J4rDhfL2y3Y1lRkecBpiRa2-p5BCNzwTwg_kTIJj9SSYCq2UmeQoqGHHR3pz09kDEG8znTqwWRG3KtX47J1TvPxUQaMuWuZyxEn1cRHJYwlF_hwfsn02OgXENIvkKDjcJ1m_Z5Qt2OOW9I0tUe1nlYI5VmT1rBGbzjf5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
شلتون و تیافو؛ نبرد قدرت و جسارت برای صعود در نیویورک
[
فرانسیس تیافو
🆚
بن شلتون
]
⏰
بامداد شنبه ساعت ۰۲:۳۰
🎾
شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند ریتم مسابقه را در دست بگیرد. تیافو اما در رالی‌ها و تغییر سرعت، توانایی بالایی برای به‌هم‌زدن برنامه حریف دارد. اگر شلتون روی سرویس اول و ضربات فورهندش مسلط باشد، شانس برتری‌اش بیشتر می‌شود. با این حال، تجربه و تنوع تیافو می‌تواند این نبرد را به یک بازی نزدیک و جذاب تبدیل کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139925" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139924" target="_blank">📅 00:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
تارتار قصد داره که به اورونوف تایم بیشتری بازی بده تا اعتماد به نفس رفته این بازیکن برگرده و این بازیکن رو دوباره احیا کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139923" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎦
تحلیل مدعیان اصلی قهرمانی در لیگ از نگاه وحید هاشمیان؛ شانس اول قهرمانی به نظرم پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139922" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
براساس گزارش منابع خبری، مسعود پزشکیان با درخواست زنوزی بدنبال حل مشکل سربازی علیرضا بیرانوند تا پایان جام ملت‌های آسیا است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139921" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=myp5kq0PviBkwrRdvKQaABa0BN0OY-ZlMzp0jBKV5vPnIkAQhpemUC6idDs6hq5QQKNQHrHSt1XQsE3xD2Ux5Bx0HNgBncg81XgAdAArYbbs3TK--EcNEwwIKiG21sSbnj_hK-SJZwixrPD7sKIHldPXxAzWnTdeOhjI2lO-sdFQbI0RDoJ6vL5EhdWu_Hi_C22NZDjCkvTMbf0NilVXdIKJsUFmWNxTO66C-6TXs1hyjsmKfgTCKr5xr6VceVJ2n69WmxjvZI1BedHfRV8Q6SdarFyAYh8ToG2MPugaCZ3wsR__jm4gJG9AwM5Cyd0cxi6mmdQaQU40Vxnjv1L8tY_T9pJLP6CF5LkbZH-OkcWUXB1z4ob6j_j61oKzWeJO6CnF7FDyU-K-tfsr43-4-aXzCFFhLHwWc0WJto0iw09LnbHPZSrsQt7glF5NDEywr82X5U3dAaD9zMWeAdyJ3kQDhMYmzN6Tu5VeFxc_SXJHt0NQ7PUD_hfBSsH52H5nfiexpQeY9XY1ZmEwk1SCGVIdMQQYw3eKy3xXILMNFGPmyTMH45C9KkcpRKFpERdMgnsB7I7TibtWQ9MrnxwP44I0ZUoduwzoBayDADGZ74xB3Fn5zOJAkCeduZzZSHkpOEr8nA-i5dbhaoc0WLDWUyPoj2X2tjLVjz7vnNKi4kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=myp5kq0PviBkwrRdvKQaABa0BN0OY-ZlMzp0jBKV5vPnIkAQhpemUC6idDs6hq5QQKNQHrHSt1XQsE3xD2Ux5Bx0HNgBncg81XgAdAArYbbs3TK--EcNEwwIKiG21sSbnj_hK-SJZwixrPD7sKIHldPXxAzWnTdeOhjI2lO-sdFQbI0RDoJ6vL5EhdWu_Hi_C22NZDjCkvTMbf0NilVXdIKJsUFmWNxTO66C-6TXs1hyjsmKfgTCKr5xr6VceVJ2n69WmxjvZI1BedHfRV8Q6SdarFyAYh8ToG2MPugaCZ3wsR__jm4gJG9AwM5Cyd0cxi6mmdQaQU40Vxnjv1L8tY_T9pJLP6CF5LkbZH-OkcWUXB1z4ob6j_j61oKzWeJO6CnF7FDyU-K-tfsr43-4-aXzCFFhLHwWc0WJto0iw09LnbHPZSrsQt7glF5NDEywr82X5U3dAaD9zMWeAdyJ3kQDhMYmzN6Tu5VeFxc_SXJHt0NQ7PUD_hfBSsH52H5nfiexpQeY9XY1ZmEwk1SCGVIdMQQYw3eKy3xXILMNFGPmyTMH45C9KkcpRKFpERdMgnsB7I7TibtWQ9MrnxwP44I0ZUoduwzoBayDADGZ74xB3Fn5zOJAkCeduZzZSHkpOEr8nA-i5dbhaoc0WLDWUyPoj2X2tjLVjz7vnNKi4kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139920" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=fxNYbJ0ElCSH1v3mkx0L3ricc0lu4nIAkyfywZjR_XS5HzutlT74wQCVJM7yib0ccveaKRP8ZirPYl2fEQb1we29Wn5X_2Flfq_LugPxXDBzIpMj7eo_yIjOiuGXAS4TkIizepcc6xsbOFMTNWRqpIHFbaZZT-QmEI8BCG013UfA5-nD9jOBRa7KScG391p2WZOq966pgSJc7h6B-rySXZQ3gISQhTH3e9xUGmH6TSYJ6EC7r_WIxFbpb4_Fckare7wvND59SVEDP-jf3f4w4Q2WUzvF4fwy4nDTbJ03mjsc3mQWOBx4PhvVbmA72gnmwnUy556vUnVfQ_dxGYHHQCdWqDjuk1Ke-crFBX11IUDri5kCYuuRyXlgQ_toHGPu5F82HBRYJHJm4ji6sGYY5Do5y1siv3DF2A6eYIWZbdZlWukTekQxMxLj95VUugHUpNNkfS7Mn_xMhYapQeGPONozQe_mYZNW-UgXu2mJMzfPKxNOM6RjoKX29VzWHqM2tQdzXNGgN4dxfR9Yjch770Gko989c-H97QH-xmuvYd1oDeYjh1nVuwOVrh15RnpgU4IUWUQjIXapUPgKa-lwhyJ3MoXJ6S5xi7n_rAh8K23vlpsopissag3R2mWQNC-UH3eEVmF6jfNzFxP2k52rPe1O8Bc0682Vg7wIMsDTqqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=fxNYbJ0ElCSH1v3mkx0L3ricc0lu4nIAkyfywZjR_XS5HzutlT74wQCVJM7yib0ccveaKRP8ZirPYl2fEQb1we29Wn5X_2Flfq_LugPxXDBzIpMj7eo_yIjOiuGXAS4TkIizepcc6xsbOFMTNWRqpIHFbaZZT-QmEI8BCG013UfA5-nD9jOBRa7KScG391p2WZOq966pgSJc7h6B-rySXZQ3gISQhTH3e9xUGmH6TSYJ6EC7r_WIxFbpb4_Fckare7wvND59SVEDP-jf3f4w4Q2WUzvF4fwy4nDTbJ03mjsc3mQWOBx4PhvVbmA72gnmwnUy556vUnVfQ_dxGYHHQCdWqDjuk1Ke-crFBX11IUDri5kCYuuRyXlgQ_toHGPu5F82HBRYJHJm4ji6sGYY5Do5y1siv3DF2A6eYIWZbdZlWukTekQxMxLj95VUugHUpNNkfS7Mn_xMhYapQeGPONozQe_mYZNW-UgXu2mJMzfPKxNOM6RjoKX29VzWHqM2tQdzXNGgN4dxfR9Yjch770Gko989c-H97QH-xmuvYd1oDeYjh1nVuwOVrh15RnpgU4IUWUQjIXapUPgKa-lwhyJ3MoXJ6S5xi7n_rAh8K23vlpsopissag3R2mWQNC-UH3eEVmF6jfNzFxP2k52rPe1O8Bc0682Vg7wIMsDTqqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
❤️
🎙
انتقادهای تند وحید هاشمیان از مدیریت پرسپولیس: وقتی سرمربی دارید چرا به او احترام نمی‌گذارید و رسما اعلام می کنید که دنبال سرمربی دیگری هستید؟ همین می شود که بازیکن هم به سرمربی احترام نمی‌گذارد
🔴
همین جریان و اتفاق را هم برای اوسمار ایجاد کردند و این رفتار اصلا حرفه ای نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139918" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=AXP0sddLhb-WSJE8ts6VTr_p0rMoTn7bjxNLT76zE_c8pOTTtl7w1OssWY4t-RjhRQKQxW37tIcPvbtgJtI9zIrZpSnPkLkpQA1dY_OawQl0M3HWBKhB_tVUEiUvWQfrpr53LrOq3EQB9vLt2IhXk4S4YxYnYopgWbnBAkz70ILOZjaIdKvRzoMRLClV-mYS3MniJDeftd8sIBBcz7QTcUS2DUuPioqcna1ukWhBoI1qVqzNDRkUS9Tg3DIx_BKc0xr6vXsFAmyxLKlDihZzwrMCyWFLN6f7cXZ63W3h6UYHvH9p7KB9VJNmeqEjSl1B7s1AJRzL8_8k-N_NCExr2FTTSaIFG2VOS2Ljlb-rRKzlKDU3e08AM_IgtEVDxUMnOFfRbZUmsmuOedBowsKWnvB49JDBpfTbUJRi27UMIeFXs8OiYwc4g1FUWfCf_pUxBrjdrSkAj3KgoIldpJoxV5IYSzAR0Nl_mVJIDF1WjzQCjPHuFIzonmuv3XW4ZfdBLGC6x5AG0Nw12jSyKElYnP-szdoS2-IihlDRKVkmqM8GgzcC6eByuQKxLuElTx1gjaZ7MRO6Y-CtA-H8TeGR89AMLjEaLPHlT-ySKtGj0TQ_q2a6WH8FSahnKUTETQ_C9RvbqnV9Di_J0iRXMJH9IBwN41NJyHozRYHsqKFGM3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=AXP0sddLhb-WSJE8ts6VTr_p0rMoTn7bjxNLT76zE_c8pOTTtl7w1OssWY4t-RjhRQKQxW37tIcPvbtgJtI9zIrZpSnPkLkpQA1dY_OawQl0M3HWBKhB_tVUEiUvWQfrpr53LrOq3EQB9vLt2IhXk4S4YxYnYopgWbnBAkz70ILOZjaIdKvRzoMRLClV-mYS3MniJDeftd8sIBBcz7QTcUS2DUuPioqcna1ukWhBoI1qVqzNDRkUS9Tg3DIx_BKc0xr6vXsFAmyxLKlDihZzwrMCyWFLN6f7cXZ63W3h6UYHvH9p7KB9VJNmeqEjSl1B7s1AJRzL8_8k-N_NCExr2FTTSaIFG2VOS2Ljlb-rRKzlKDU3e08AM_IgtEVDxUMnOFfRbZUmsmuOedBowsKWnvB49JDBpfTbUJRi27UMIeFXs8OiYwc4g1FUWfCf_pUxBrjdrSkAj3KgoIldpJoxV5IYSzAR0Nl_mVJIDF1WjzQCjPHuFIzonmuv3XW4ZfdBLGC6x5AG0Nw12jSyKElYnP-szdoS2-IihlDRKVkmqM8GgzcC6eByuQKxLuElTx1gjaZ7MRO6Y-CtA-H8TeGR89AMLjEaLPHlT-ySKtGj0TQ_q2a6WH8FSahnKUTETQ_C9RvbqnV9Di_J0iRXMJH9IBwN41NJyHozRYHsqKFGM3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
❌
گلایه وحید هاشمیان از احمدی و مدیریت اسپانسر اصلی پرسپولیس؛ صحبتهای او حرفه ای نبود
🔻
احمدی گفت که هاشمیان نبود دورسون و امیری را رد می کرد و این حرف در رسانه حرفه ای نبود و میتوانست شخصا با خودم صحبت کند/ صحبتهای او فرار از مسئولیت بود و در شان یک مدیر نبود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139917" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139916" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
روشنک :
✔️
✔️
باشگاه‌هایی مثل سپاهان، آلومینیوم و.. به ما اعلام کردند که اگر هفته هفتم را برگزار کنیم نمی‌توانند بازیکن در اختیار تیم امید قرار دهند.
✔️
✔️
فقط پرسپولیس درخواستی برای لغو بازی‌اش در هفته هشتم نداشت.
✔️
✔️
نمی دانم سازمان لیگ چه گناهی مرتکب…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139915" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To423NLcMCK9l82hCcE1mmgafZ2zP_Ldhyx5IsKcqtZc-wdAcyYgdHMw3XLKsihG2Y2s2hGnoCxAZ6U70HDrFK2H29Un0wGoBGadS9wfOMVC-3gPkDLdqPF97odUQuemjTRJ5OSpVUJCjuxlmbnrm2INYN-Vh8IxQYq_AEktxl9ZDTYBl6rcfe1S1jRCrtL2l8QjVS-7kT4CX896RKEuXHiFNYKf8U0PVEJSG2FyeuPKS3AzfJrpTELj9sPiSjJr6fxY9OxPsQvY-StEuAq103Cd-OgedI8E840FEcsPuDPWaVR2ubYR02tFT8eM80ZkO-jrXfvxgVL_1qcDI48V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با وجود لغو دیدار برابر خیبر خرم‌آباد، پرسپولیس امروز هم طبق برنامه تمرین کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139914" target="_blank">📅 22:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=GrMdHSJFQyxTZ6SD9OL4JJUznpfvr6XCZhBk4_9moe7zVsnEKABXRLak2YkXMMEqGZ_Jb4gTxcKNmcVlVo_e81LKJeNn0qYbHAdkoaGNEPuXCnas0vcKF32OV6wiibtiPPinRjGF7CCtIy5RF-52AfBL7Orr1xejOFWN0HFSjPkTsb4rNEpz9intAnrYTjythJ43A3yLZmZDP5RYueqVksjiP_59kvCmhEEo5LLjUdtPMMXFfUa5zNj7pnvZoXJuL9bSVoGb2TUzyA_kLq9Aprzz1ZqWD3EvCn1gnJvN0nc4GTKFAqdEo6YDCz_7WH7L_3GktA8sGKFW4X3o8YXLi3UEmzA35YcW-gX-0lZ4RnfCdY7v3SvDK-ZW3az6WqD5eNIqGQG3nfqTvsXjZSIGHrooqFXfSNC26ur0PUzXw3Sj_HoKmLCqCEhj4H8mXDZPi6SOSfBjRCa_ELSL6It2NQye8LvhblIHPtgbymNPN9LCNX37H7hxKQXRNFsF5xBlYUD9O5PcRiWU9aW1WrMwW8Tu5G60zpV_B-8bNLC-0J60glEgIXk1JRrO-tRBOBW20Ki2C9zDnmwt27IQhcpMzeWJxSgU5pzCvUBTb4iYn2wM7fpGl9R-_ej9cCjD4odADdTp_0t-4cH5qcm_zABBN6c3mXg1sl3ayZ_HMme0eiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=GrMdHSJFQyxTZ6SD9OL4JJUznpfvr6XCZhBk4_9moe7zVsnEKABXRLak2YkXMMEqGZ_Jb4gTxcKNmcVlVo_e81LKJeNn0qYbHAdkoaGNEPuXCnas0vcKF32OV6wiibtiPPinRjGF7CCtIy5RF-52AfBL7Orr1xejOFWN0HFSjPkTsb4rNEpz9intAnrYTjythJ43A3yLZmZDP5RYueqVksjiP_59kvCmhEEo5LLjUdtPMMXFfUa5zNj7pnvZoXJuL9bSVoGb2TUzyA_kLq9Aprzz1ZqWD3EvCn1gnJvN0nc4GTKFAqdEo6YDCz_7WH7L_3GktA8sGKFW4X3o8YXLi3UEmzA35YcW-gX-0lZ4RnfCdY7v3SvDK-ZW3az6WqD5eNIqGQG3nfqTvsXjZSIGHrooqFXfSNC26ur0PUzXw3Sj_HoKmLCqCEhj4H8mXDZPi6SOSfBjRCa_ELSL6It2NQye8LvhblIHPtgbymNPN9LCNX37H7hxKQXRNFsF5xBlYUD9O5PcRiWU9aW1WrMwW8Tu5G60zpV_B-8bNLC-0J60glEgIXk1JRrO-tRBOBW20Ki2C9zDnmwt27IQhcpMzeWJxSgU5pzCvUBTb4iYn2wM7fpGl9R-_ej9cCjD4odADdTp_0t-4cH5qcm_zABBN6c3mXg1sl3ayZ_HMme0eiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
به مناسبت خداحافظی گولسیانی، یادی کنیم از گلش به مس تو دقایق پایانی که باعث قهرمانی پرسپولیس شد و باسن خیلی از کیسه کشارو سوزوند
❤️
🔥
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139913" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139912" target="_blank">📅 20:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
🤩
🤩
🤩
🤩
🤩
💬
گولسیانی:
⭐️
من تو تیمهای زیادی بازی کردم ولی یه تیم هست که وقتی یه بار داخلش بازی کنی و بدرخشی، دیگه از قلبت بیرون نمیره. نمیدونم چرا ولی وقتی یه بار تو پرسپولیس بدرخشی دیگه پرسپولیس میشه عضوی از خونوادت. من رو نخواستن ولی من تا ابد عاشق پرسپولیس…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139911" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVuoje9kmepaLp1cUND0VaBKYdFLCJ9--HwZxzXHDJxTGvl6q7Xu4K5UvCX_iuBoOGvejD1iEEDOTMc-AGl-sE55mVNrVvylm9iPWX2YU_fVT8epS3324HOZ9-RSNqbDqv--LHRdRki2BVrsWY6T1LVE8se-CcZG1I2cUnPT1pBaqIJQTFaKEz3ANZFpQUlxXU6zFICJVTmS18qyLDWqqEXJNna3WIrO1sWYqtg8e3-A_5m-AhyY0jtIooXi7GkgUVfetxolCU_FYzCO3OfFT78La2vQYwzgA42rUyYuEm73tj7wsA4_phduPm4HCqu6122pMPezww7aEhcAZcqEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽
سالاری از پست مشاوره مدیرعامل پرسپولیس استعفا داد.
🔻
محمد رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال که چندی قبل به عنوان مشاور پیمان حدادی مدیرعامل پرسپولیس انتخاب شده بود از این سمت استعفا کرده است.
🔻
سالاری به توصیه مهدی تاج رئیس فدراسیون فوتبال برای توسعه رده های پایه و کمک به فوتبال از تاریخ اول شهریور در پیامی به حدادی اعلام کرده که دیگر به عنوان مشاور او فعالیت نخواهد کرد و از این سمت استعفا داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139910" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
✔️
فراز کمالوند سرمربی خیبر: سازمان لیگ تصمیم بسیار درستی گرفته است که بازی‌ ما با پرسپولیس را لغو کرده است/ من نمی دانم سر و صدای دوستان برای چیست؟
☹️
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139909" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
فراز کمالوند سرمربی خیبر در گفتگو با ورزش سه:
🗣
باشگاه پرسپولیس ابوذر صفرزاده را از ما خواسته و ما گفتیم در شرایطی این بازیکن را می‌دهیم که حسین ابرقویی را بگیریم. همچنان هم در حال مذاکره هستیم و به نتیجه نرسیده‌ایم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139908" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQsi9GGkySSPKyVEfyj5CMP8GugvCzXg69PvoH9sHg3m4JSnxLRcO0UsuUJMAWNeUxsdXJCTNQjXxmu-cGywhsWS_KMpsvb1f103oC77JXHYSNUrubk3A00P0oAHt6f2Dr4Yt7lr_Ztjn0gw0ACHHptPc7xj25Q7D877FtQwtVbVQnoRDZE2um2DaA-Hj767n_lUu9TuFUxnunC_2osenTElc90JSw6wwi9cMhBNrSZiLqntJ6F15E36-hjRcsBdz6UPDBXHhFIVz4YSxBVvPlAu7HVXLsJwcvxJc3dgQWl6xgph31KTERPtJM1RT2ta0XSUIxxhQFVZaKrPY2EPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبردی نزدیک و تاکتیکی؛ والنسیا با تکیه بر امتیاز میزبانی به‌دنبال فشار بیشتر است و سویا امیدوار به استفاده از فضاهای دفاعی حریف و ضربه در ضدحملات؛ دیداری که می‌تواند تا دقایق پایانی کاملاً پایاپای دنبال شود.
[
سویا
🔴
🆚
⚪️
والنسیا
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139907" target="_blank">📅 19:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvCsRHpGV4mdXbIncuEP5lbvIjJcTyDCL4tsoPHJvg4DhmceINkTvuzxrZieZbRX5rFlSVhUhnC211kyyisYCfqJQ1sPtFeNYxtXOTzm0DNp29VN3-_7T0qHHJgiZBHjiqSpLVThFzKX4s1U8VMkAZlPlQASr6RvRU10fLU2PYsXfZ1h7Sux7YOG_9OHRW-0nAG-D02XUu6cR5b-ICxQrQdiZvk_pdbUMgz9wPckOdFo3-_4HVDvCABA42wS1yoNrne4sgF5MNDCdHs-ZDucDvoOOFuZu-jAMHzg9tCarRgHwktsP5mzI5mCUNqMzsMGW9Cu9WWtw74MXHMCbsIQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXvHn4qNQi_dYrLIyBDERJbSNfdhFVCk6tAI_tgyKtpTE9-FOXVGzJnMYhLMz0_lEL0mXh5KMe8LH0QqNhPazos6y2YYz6qmZU8rZWlcfMCfyj2zsOBW4bk1yHGAztU0qXuxvNB2SZpC79XM8E0Y2YCVypbNsotI-CF1kjv8TbYQXnu973nIC2s4lxD7FLBJwUs_11ZKaY9-FQ0E9X7f-q_Ynth8kam_1C0lxkL8TXn4qy4eULOaS8rv-ci681xjuna1qjQ1itaJt_JMeBDw0i7PxT0WxTVMQrfzEOH7wwdWGcICRh939R3XXTnkwYdv0sFJWTs4fXbxUJ3-TLFpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139900" target="_blank">📅 16:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139899" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
🧤
علیرضا بیرانوند نتوانست کلین شیت های خود را ادامه دهد تا رکورد هشت کلین‌شیت متوالی پیام نیازمند در لیگ نوزدهم، دست‌نخورده باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139898" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
فووووووووووووری
✔️
اسماعیل کارتال سرمربی فنرباغچه پس از مساوی مقابل رم در هفته لیگ قهرمانان اروپا از سمت خود استعفا داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139897" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139896" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139895" target="_blank">📅 15:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3ojZxXZP51i-NnUDR8I_L5v_eJYuqi3ryWn9nMtGxmN5pKgFq7UjXv6TrKMvklLTiUUnK8J11IZb77CipGyaIvDd-S84f6GjsKkTNG3TXIcK6QXUPEen4yC_7urMvT3Wk55Fut6j-ky1IqPS0SZbaN0IyT_gbwUdYJcGvBA_9ESLnCRWvmzsHUHEQZStQGIllCzTh9iBc-9Z-B8jRv-x89ekqCKRrmPOvKhicnUdW2EMEDBsNVDfiXeRbqroNkGdPk6YulvFRX2Wu8EPxAGCSuwv2WSk4qUzFT4jqGoUdSbA-n-N6F0ZKcf15orNKX3TOHENxTO4UEFGcqeBwHZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139894" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm1AoLs6FPEjp6RIcMU_RxRyKSK5IJtE9715UU72HkEu0v7kWJpbKMU66F-SmqmX6eIeHJj4BjANhhsfn4CD659TiYipaMuka_8QnhhGVHeWtuwozuLAEEZtk1U0iYyCtW_e-xUhSAI8TVuwTvMIEDODE7b1y4Pmnnfa2A8887I3o1bXsYvxYZkkshz25sz7g7Fthfi9FLzd7ES6fVqnPD5htXng-q034dwQAzmQKqDjrMa_pd938nkMPz6lNyJANhLqhMDBiYKikuRP_ECEo7fqwRe4wSlr2YyMaRR74sFsDCfeK7GNs7WGmsNXopbPi1yJZNxgMxP-e57ums-7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان نیز پیشنهاداتی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139893" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139892" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⬇
علوی سخنگوی فدراسیون فوتبال: پرسپولیس دوست داشت بازی‌اش لغو نشود؟ باید بگویم از آن طرف خیبر درخواست داشت که بازی‌‌اش لغو شود
✔️
✔️
خیبر فقط یک ملی‌پوش داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139891" target="_blank">📅 11:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR8HJYC86yoPWsUCzo_yYDQuDkkwM7U3vXjoRno61NyS3QSHwjWkaCNLipFjIDUBmSZ5NZe_qfvXIFfFJWCkECDkAJMnCv0z7hbe1WvFvtwLJdGIaXx5bo1KbOrFiGBk7F5IzoR3lNvgZImFODF9kcEr8S4aXLsqLSooGdYgQf2BJW0ABhsj8Titops7FGP94vviRh7YXtdVMoJKOaFpQeMIDA_FjhQEewINWJ_B_9zWydjVLpvG95pLyYt0LtXlxRVEOW9Qfp4w15sn1IkwsxQtpw6iqfyRoMdBUJ04Gfoxd_T4rEsv1D-RY8z3b9nyfpQulyLf0PLQXPZzlQyE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
از دیروز و با آغاز دور جدید تمرینات پویا اسمی مدافع وسط 17 ساله که همراه تیم ملی جوانان در ویتنام حضور داشت در تمرینات پرسپولیس حاضر شد و اکنون پرسپولیس سه مدافع آماده برای جانشینی محمدمهدی زارع در بازی با خیبر ( در صورت برگزاری ) در اختیار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139890" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139889" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
